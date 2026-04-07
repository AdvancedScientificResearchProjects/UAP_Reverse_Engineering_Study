import json
import torch
from transformers import AutoProcessor, AutoModel

from pipeline.config import SIGLIP2_MODEL, SIGLIP2_PROMPTS, PROCESSED_DIR
from pipeline.utils.vram import get_device, unload_model, log_vram
from pipeline.utils.image import load_image


def run() -> dict:
    print("=== Stage 4: Text-Image Matching (SigLIP2) ===")
    device = get_device()
    log_vram("before load")

    processor = AutoProcessor.from_pretrained(SIGLIP2_MODEL)
    model = AutoModel.from_pretrained(
        SIGLIP2_MODEL, torch_dtype=torch.float16
    ).to(device)
    model.eval()
    log_vram("model loaded")

    img = load_image(PROCESSED_DIR / "artifact_crop.png")

    # Process prompts one at a time to avoid OOM
    all_scores = []
    for prompt in SIGLIP2_PROMPTS:
        inputs = processor(
            text=[prompt],
            images=[img],
            padding="max_length",
            return_tensors="pt",
        ).to(device)

        with torch.no_grad():
            outputs = model(**inputs)

        score = torch.sigmoid(outputs.logits_per_image[0, 0]).cpu().item()
        all_scores.append(score)

    scored = sorted(
        zip(SIGLIP2_PROMPTS, all_scores),
        key=lambda x: x[1],
        reverse=True,
    )

    print("  Scores:")
    for prompt, score in scored:
        marker = " <<<" if score == scored[0][1] else ""
        print(f"    {score:.4f} | {prompt}{marker}")

    result = {
        "model": SIGLIP2_MODEL,
        "scores": [{"prompt": p, "score": round(s, 4)} for p, s in scored],
        "top1_prompt": scored[0][0],
        "top1_score": round(scored[0][1], 4),
    }
    (PROCESSED_DIR / "siglip_scores.json").write_text(json.dumps(result, indent=2))

    unload_model(model, processor)
    log_vram("after unload")
    return result
