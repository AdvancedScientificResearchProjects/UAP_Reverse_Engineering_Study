import json
import torch
import numpy as np
from transformers import AutoImageProcessor, AutoModel

from pipeline.config import DINOV2_MODEL, PROCESSED_DIR
from pipeline.utils.vram import get_device, unload_model, log_vram
from pipeline.utils.image import load_image


def run() -> dict:
    print("=== Stage 3: Feature Extraction (DINOv2-L) ===")
    device = get_device()
    log_vram("before load")

    processor = AutoImageProcessor.from_pretrained(DINOV2_MODEL)
    model = AutoModel.from_pretrained(
        DINOV2_MODEL, torch_dtype=torch.float16
    ).to(device)
    model.eval()
    log_vram("model loaded")

    img = load_image(PROCESSED_DIR / "artifact_crop.png")
    inputs = processor(images=img, return_tensors="pt").to(device)

    with torch.no_grad():
        outputs = model(**inputs)

    # CLS token embedding
    cls_embedding = outputs.last_hidden_state[:, 0, :].cpu().numpy().astype(np.float32)
    # Patch tokens for spatial features
    patch_tokens = outputs.last_hidden_state[:, 1:, :].cpu().numpy().astype(np.float32)

    np.save(PROCESSED_DIR / "embedding.npy", cls_embedding)
    np.save(PROCESSED_DIR / "patch_tokens.npy", patch_tokens)

    result = {
        "model": DINOV2_MODEL,
        "cls_shape": list(cls_embedding.shape),
        "patch_shape": list(patch_tokens.shape),
        "cls_norm": float(np.linalg.norm(cls_embedding)),
    }
    (PROCESSED_DIR / "features_meta.json").write_text(json.dumps(result, indent=2))
    print(f"  CLS embedding: {cls_embedding.shape}, norm={result['cls_norm']:.3f}")
    print(f"  Patch tokens: {patch_tokens.shape}")

    unload_model(model, processor)
    log_vram("after unload")
    return result
