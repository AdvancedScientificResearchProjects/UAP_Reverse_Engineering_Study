import json
import torch
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from PIL import Image
from transformers import CLIPProcessor, CLIPModel

from pipeline.config import (
    ANOMALY_NORMAL_PROMPTS, ANOMALY_ABNORMAL_PROMPTS, PROCESSED_DIR,
)
from pipeline.utils.vram import get_device, unload_model, log_vram
from pipeline.utils.image import load_image


CLIP_MODEL = "openai/clip-vit-large-patch14"


def run() -> dict:
    print("=== Stage 7: Zero-shot Anomaly (CLIP-based) ===")
    print("  NOTE: Using CLIP zero-shot as AnomalyCLIP proxy.")
    print("  Scores use softmax — they are RELATIVE probabilities among prompts,")
    print("  not absolute confidence values.")
    device = get_device()
    log_vram("before load")

    processor = CLIPProcessor.from_pretrained(CLIP_MODEL)
    model = CLIPModel.from_pretrained(
        CLIP_MODEL, torch_dtype=torch.float16
    ).to(device)
    model.eval()
    log_vram("model loaded")

    img = load_image(PROCESSED_DIR / "artifact_crop.png")

    all_prompts = ANOMALY_NORMAL_PROMPTS + ANOMALY_ABNORMAL_PROMPTS
    inputs = processor(
        text=all_prompts,
        images=img,
        return_tensors="pt",
        padding=True,
    ).to(device)

    with torch.no_grad():
        outputs = model(**inputs)

    logits = outputs.logits_per_image[0].cpu().float()
    probs = torch.softmax(logits, dim=-1).numpy()

    n_normal = len(ANOMALY_NORMAL_PROMPTS)
    normal_score = float(probs[:n_normal].sum())
    abnormal_score = float(probs[n_normal:].sum())

    print("  Prompt scores (softmax-relative):")
    for prompt, prob in zip(all_prompts, probs.tolist()):
        tag = "[N]" if prompt in ANOMALY_NORMAL_PROMPTS else "[A]"
        print(f"    {tag} {prob:.4f} | {prompt}")
    print(f"  Normal total: {normal_score:.4f}")
    print(f"  Abnormal total: {abnormal_score:.4f}")

    # Patch-level anomaly map via sliding window
    # Use ALL normal+abnormal prompts, compute abnormal ratio per patch
    w, h = img.size
    patch_size = min(w, h) // 4
    stride = patch_size // 2

    anomaly_map = np.zeros((h, w), dtype=np.float32)
    count_map = np.zeros((h, w), dtype=np.float32)

    patches = []
    coords = []
    for y in range(0, h - patch_size + 1, stride):
        for x in range(0, w - patch_size + 1, stride):
            patch = img.crop((x, y, x + patch_size, y + patch_size))
            patches.append(patch)
            coords.append((x, y))

    # Process patches one at a time to avoid OOM
    patch_scores = []
    for patch in patches:
        patch_inputs = processor(
            text=all_prompts,
            images=patch,
            return_tensors="pt",
            padding=True,
        ).to(device)
        with torch.no_grad():
            patch_out = model(**patch_inputs)
        patch_logits = patch_out.logits_per_image[0].cpu().float()
        patch_probs = torch.softmax(patch_logits, dim=-1).numpy()
        # Abnormal ratio = sum of abnormal probs
        abn_ratio = float(patch_probs[n_normal:].sum())
        patch_scores.append(abn_ratio)

    for (x, y), score in zip(coords, patch_scores):
        anomaly_map[y:y + patch_size, x:x + patch_size] += score
        count_map[y:y + patch_size, x:x + patch_size] += 1

    count_map[count_map == 0] = 1
    anomaly_map /= count_map

    # Save heatmap (no normalization to 0-1 to preserve absolute scale)
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    img_np = np.array(img)
    axes[0].imshow(img_np)
    axes[0].set_title("Artifact")
    axes[0].axis("off")
    vmax = max(anomaly_map.max(), 0.5)
    im = axes[1].imshow(anomaly_map, cmap="jet", vmin=0, vmax=vmax)
    axes[1].set_title("Anomaly Heatmap (CLIP zero-shot, abnormal ratio)")
    axes[1].axis("off")
    plt.colorbar(im, ax=axes[1], fraction=0.046, label="Abnormal prompt ratio")
    plt.tight_layout()
    plt.savefig(PROCESSED_DIR / "anomaly_clip_heatmap.png", dpi=150)
    plt.close()

    result = {
        "model": CLIP_MODEL,
        "method": "CLIP zero-shot (AnomalyCLIP proxy)",
        "scoring": "softmax — scores are relative probabilities among all prompts, not absolute confidence",
        "normal_prompts_count": n_normal,
        "abnormal_prompts_count": len(ANOMALY_ABNORMAL_PROMPTS),
        "normal_score": round(normal_score, 4),
        "abnormal_score": round(abnormal_score, 4),
        "is_anomalous": abnormal_score > normal_score,
        "prompt_scores": [
            {"prompt": p, "score": round(s, 4), "type": "normal" if p in ANOMALY_NORMAL_PROMPTS else "abnormal"}
            for p, s in zip(all_prompts, probs.tolist())
        ],
    }
    (PROCESSED_DIR / "anomaly_clip_meta.json").write_text(json.dumps(result, indent=2))
    print(f"  Anomalous: {result['is_anomalous']} (abnormal={abnormal_score:.4f} vs normal={normal_score:.4f})")

    unload_model(model, processor)
    log_vram("after unload")
    return result
