import json
import torch
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from PIL import Image
from transformers import AutoImageProcessor, AutoModelForDepthEstimation

from pipeline.config import DEPTH_MODEL, PROCESSED_DIR
from pipeline.utils.vram import get_device, unload_model, log_vram
from pipeline.utils.image import load_image


def run() -> dict:
    print("=== Stage 8: Depth Estimation (Depth Anything V2) ===")
    device = get_device()
    log_vram("before load")

    processor = AutoImageProcessor.from_pretrained(DEPTH_MODEL)
    model = AutoModelForDepthEstimation.from_pretrained(
        DEPTH_MODEL, torch_dtype=torch.float16
    ).to(device)
    model.eval()
    log_vram("model loaded")

    img = load_image(PROCESSED_DIR / "preprocessed.png")
    inputs = processor(images=img, return_tensors="pt").to(device)

    with torch.no_grad():
        outputs = model(**inputs)

    depth = outputs.predicted_depth[0].cpu().float().numpy()

    # Interpolate to original size
    w, h = img.size
    depth_resized = np.array(
        Image.fromarray(depth).resize((w, h), Image.BILINEAR)
    )

    # Normalize for visualization
    depth_norm = (depth_resized - depth_resized.min()) / (
        depth_resized.max() - depth_resized.min() + 1e-8
    )

    # Save 16-bit depth
    depth_16 = (depth_norm * 65535).astype(np.uint16)
    Image.fromarray(depth_16).save(PROCESSED_DIR / "depth_map.png")

    # Save visualization
    fig, axes = plt.subplots(1, 2, figsize=(14, 7))
    axes[0].imshow(np.array(img))
    axes[0].set_title("Input")
    axes[0].axis("off")
    im = axes[1].imshow(depth_norm, cmap="inferno")
    axes[1].set_title("Depth Map (Depth Anything V2)")
    axes[1].axis("off")
    plt.colorbar(im, ax=axes[1], fraction=0.046, label="Relative depth")
    plt.tight_layout()
    plt.savefig(PROCESSED_DIR / "depth_visualization.png", dpi=150)
    plt.close()

    # Analyze depth in artifact region
    detection = json.loads((PROCESSED_DIR / "detection_bbox.json").read_text())
    bbox = detection["bbox"]
    x1, y1, x2, y2 = bbox
    artifact_depth = depth_norm[y1:y2, x1:x2]

    center_depth = float(artifact_depth[
        artifact_depth.shape[0] // 4 : 3 * artifact_depth.shape[0] // 4,
        artifact_depth.shape[1] // 4 : 3 * artifact_depth.shape[1] // 4,
    ].mean())
    edge_depth = float(np.concatenate([
        artifact_depth[0, :], artifact_depth[-1, :],
        artifact_depth[:, 0], artifact_depth[:, -1],
    ]).mean())

    # DA v2: higher value = closer to camera, so convex surface has higher center
    is_convex = center_depth > edge_depth

    result = {
        "model": DEPTH_MODEL,
        "depth_range": [float(depth_resized.min()), float(depth_resized.max())],
        "artifact_center_depth": round(center_depth, 4),
        "artifact_edge_depth": round(edge_depth, 4),
        "surface_appears_convex": is_convex,
    }
    (PROCESSED_DIR / "depth_meta.json").write_text(json.dumps(result, indent=2))
    print(f"  Center depth: {center_depth:.4f}, Edge depth: {edge_depth:.4f}")
    print(f"  Surface appears convex: {is_convex}")

    unload_model(model, processor)
    log_vram("after unload")
    return result
