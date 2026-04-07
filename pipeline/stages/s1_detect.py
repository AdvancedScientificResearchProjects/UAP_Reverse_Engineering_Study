import json
import torch
import numpy as np
from contextlib import nullcontext
from PIL import Image
from transformers import AutoProcessor, AutoModelForZeroShotObjectDetection

from pipeline.config import (
    GDINO_MODEL, GDINO_PROMPT,
    GDINO_BOX_THRESHOLD, GDINO_TEXT_THRESHOLD, PROCESSED_DIR,
)
from pipeline.utils.vram import get_device, unload_model, log_vram
from pipeline.utils.image import load_image


def run() -> dict:
    print("=== Stage 1: Detection (Grounding DINO) ===")
    device = get_device()
    log_vram("before load")

    processor = AutoProcessor.from_pretrained(GDINO_MODEL)
    model = AutoModelForZeroShotObjectDetection.from_pretrained(
        GDINO_MODEL, torch_dtype=torch.float32
    ).to(device)
    log_vram("model loaded")

    img = load_image(PROCESSED_DIR / "preprocessed.png")
    inputs = processor(images=img, text=GDINO_PROMPT, return_tensors="pt").to(device)

    ctx = torch.amp.autocast("cuda") if device.type == "cuda" else nullcontext()
    with torch.no_grad(), ctx:
        outputs = model(**inputs)

    results = processor.post_process_grounded_object_detection(
        outputs,
        inputs["input_ids"],
        threshold=GDINO_BOX_THRESHOLD,
        text_threshold=GDINO_TEXT_THRESHOLD,
        target_sizes=[img.size[::-1]],
    )[0]

    boxes = results["boxes"].cpu().numpy().tolist()
    scores = results["scores"].cpu().numpy().tolist()
    labels = results["labels"]

    print(f"  Detected {len(boxes)} objects")
    for i, (box, score, label) in enumerate(zip(boxes, scores, labels)):
        print(f"    [{i}] {label}: score={score:.3f}, bbox={[int(c) for c in box]}")

    if not boxes:
        print("  WARNING: No detections. Using center crop fallback.")
        w, h = img.size
        cx, cy = w // 2, h // 2
        r = min(w, h) // 4
        best_box = [cx - r, cy - r, cx + r, cy + r]
        best_score = 0.0
        best_label = "fallback_center"
    else:
        best_idx = int(np.argmax(scores))
        best_box = [int(c) for c in boxes[best_idx]]
        best_score = scores[best_idx]
        best_label = labels[best_idx]

    detection = {
        "bbox": best_box,
        "score": float(best_score),
        "label": best_label,
        "all_detections": [
            {"bbox": [int(c) for c in b], "score": float(s), "label": l}
            for b, s, l in zip(boxes, scores, labels)
        ],
    }

    out_path = PROCESSED_DIR / "detection_bbox.json"
    out_path.write_text(json.dumps(detection, indent=2))
    print(f"  Best: {best_label} @ {best_score:.3f}, bbox={best_box}")

    unload_model(model, processor)
    log_vram("after unload")
    return detection
