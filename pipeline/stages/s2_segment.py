import json
import torch
import numpy as np
from PIL import Image
from transformers import AutoProcessor, AutoModelForMaskGeneration

from pipeline.config import SAM2_MODEL, PROCESSED_DIR
from pipeline.utils.vram import get_device, unload_model, log_vram
from pipeline.utils.image import load_image, save_image, apply_mask_overlay, crop_to_bbox


def run() -> dict:
    print("=== Stage 2: Segmentation (SAM2) ===")
    device = get_device()
    log_vram("before load")

    detection = json.loads((PROCESSED_DIR / "detection_bbox.json").read_text())
    bbox = detection["bbox"]

    processor = AutoProcessor.from_pretrained(SAM2_MODEL)
    model = AutoModelForMaskGeneration.from_pretrained(
        SAM2_MODEL, torch_dtype=torch.float16
    ).to(device)
    log_vram("model loaded")

    img = load_image(PROCESSED_DIR / "preprocessed.png")
    w, h = img.size

    inputs = processor(
        images=img,
        input_boxes=[[bbox]],
        return_tensors="pt",
    ).to(device)

    with torch.no_grad():
        outputs = model(**inputs)

    # Post-process masks to original size
    masks = processor.post_process_masks(
        outputs.pred_masks,
        inputs["original_sizes"],
    )  # list of [num_boxes, num_masks, H, W]

    iou_scores = outputs.iou_scores.cpu().numpy()[0][0]
    best_mask_idx = int(np.argmax(iou_scores))
    mask = masks[0][0][best_mask_idx].cpu().numpy().astype(np.uint8)

    mask_area = mask.sum()
    total_area = mask.shape[0] * mask.shape[1]
    area_pct = mask_area / total_area * 100

    print(f"  Mask shape: {mask.shape}, area: {mask_area} px ({area_pct:.1f}%)")
    print(f"  IoU score: {iou_scores[best_mask_idx]:.3f}")

    # Save mask
    mask_img = Image.fromarray(mask * 255)
    save_image(mask_img, PROCESSED_DIR / "mask.png")

    # Save overlay
    img_np = np.array(img)
    overlay = apply_mask_overlay(img_np, mask)
    save_image(overlay, PROCESSED_DIR / "mask_overlay.png")

    # Save cropped artifact
    crop = crop_to_bbox(img, bbox, pad=15)
    save_image(crop, PROCESSED_DIR / "artifact_crop.png")

    # Save masked artifact (transparent bg)
    masked_rgba = np.zeros((*mask.shape, 4), dtype=np.uint8)
    masked_rgba[..., :3] = img_np
    masked_rgba[..., 3] = mask * 255
    save_image(Image.fromarray(masked_rgba), PROCESSED_DIR / "artifact_masked.png")

    result = {
        "mask_area_px": int(mask_area),
        "mask_area_pct": round(area_pct, 2),
        "iou_score": float(iou_scores[best_mask_idx]),
        "bbox": bbox,
    }
    (PROCESSED_DIR / "segmentation_meta.json").write_text(
        json.dumps(result, indent=2)
    )

    unload_model(model, processor)
    log_vram("after unload")
    return result
