import json
import torch
from transformers import AutoProcessor, AutoModel

from pipeline.config import SIGLIP2_MODEL, MATERIAL_PROMPTS, PROCESSED_DIR
from pipeline.utils.vram import get_device, unload_model, log_vram
from pipeline.utils.image import load_image


def run() -> dict:
    print("=== Stage 5: Material Hypothesis (SigLIP2 zero-shot) ===")
    device = get_device()
    log_vram("before load")

    processor = AutoProcessor.from_pretrained(SIGLIP2_MODEL)
    model = AutoModel.from_pretrained(
        SIGLIP2_MODEL, torch_dtype=torch.float16
    ).to(device)
    model.eval()
    log_vram("model loaded")

    img = load_image(PROCESSED_DIR / "artifact_crop.png")

    all_prompts = []
    prompt_to_family = {}
    for family, prompts in MATERIAL_PROMPTS.items():
        for p in prompts:
            all_prompts.append(p)
            prompt_to_family[p] = family

    # Process one prompt at a time to avoid OOM
    prompt_scores = {}
    for prompt in all_prompts:
        inputs = processor(
            text=[prompt],
            images=[img],
            padding="max_length",
            return_tensors="pt",
        ).to(device)

        with torch.no_grad():
            outputs = model(**inputs)

        score = torch.sigmoid(outputs.logits_per_image[0, 0]).cpu().item()
        prompt_scores[prompt] = score

    # Aggregate by family (max score per family)
    family_scores = {}
    family_best_prompt = {}
    for prompt, score in prompt_scores.items():
        family = prompt_to_family[prompt]
        if family not in family_scores or score > family_scores[family]:
            family_scores[family] = score
            family_best_prompt[family] = prompt

    ranked = sorted(family_scores.items(), key=lambda x: x[1], reverse=True)

    print("  Material family scores:")
    for family, score in ranked:
        marker = " <<<" if family == ranked[0][0] else ""
        print(f"    {score:.4f} | {family}{marker}")

    top_family = ranked[0][0]
    top_score = ranked[0][1]

    if top_score >= 0.9:
        confidence = "HIGH"
    elif top_score >= 0.7:
        confidence = "MEDIUM"
    else:
        confidence = "LOW"

    result = {
        "model": SIGLIP2_MODEL,
        "method": "SigLIP2 zero-shot",
        "primary_hypothesis": {
            "family": top_family,
            "score": round(top_score, 4),
            "confidence": confidence,
            "best_prompt": family_best_prompt[top_family],
        },
        "all_families": [
            {
                "family": f,
                "score": round(s, 4),
                "best_prompt": family_best_prompt[f],
            }
            for f, s in ranked
        ],
    }
    (PROCESSED_DIR / "material_hypothesis.json").write_text(
        json.dumps(result, indent=2)
    )
    print(f"  Primary: {top_family} ({confidence}, {top_score:.4f})")

    unload_model(model, processor)
    log_vram("after unload")
    return result
