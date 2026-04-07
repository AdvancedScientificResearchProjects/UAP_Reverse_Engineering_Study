import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from PIL import Image
from scipy.ndimage import gaussian_filter

from pipeline.config import PROCESSED_DIR
from pipeline.utils.image import load_image


def run() -> dict:
    print("=== Stage 6: Anomaly Detection (EfficientAD-like heuristic) ===")
    print("  NOTE: EfficientAD requires training data. Using texture-gradient")
    print("  anomaly heuristic as proxy for single-image analysis.")

    img = load_image(PROCESSED_DIR / "artifact_crop.png")
    img_np = np.array(img).astype(np.float32)

    # Load mask if available
    mask_full = np.array(Image.open(PROCESSED_DIR / "mask.png").convert("L"))
    detection = json.loads((PROCESSED_DIR / "detection_bbox.json").read_text())
    bbox = detection["bbox"]
    x1, y1, x2, y2 = bbox
    pad = 15
    h_full, w_full = mask_full.shape
    x1c, y1c = max(0, x1 - pad), max(0, y1 - pad)
    x2c, y2c = min(w_full, x2 + pad), min(h_full, y2 + pad)
    mask_crop = mask_full[y1c:y2c, x1c:x2c]

    # Resize mask to match crop
    mask_resized = np.array(
        Image.fromarray(mask_crop).resize(
            (img_np.shape[1], img_np.shape[0]), Image.NEAREST
        )
    )

    gray = np.mean(img_np, axis=2)

    # Multi-scale gradient magnitude as anomaly proxy
    scales = [1.0, 2.0, 4.0]
    anomaly_map = np.zeros_like(gray)
    for sigma in scales:
        smoothed = gaussian_filter(gray, sigma=sigma)
        gx = np.gradient(smoothed, axis=1)
        gy = np.gradient(smoothed, axis=0)
        grad_mag = np.sqrt(gx**2 + gy**2)
        anomaly_map += grad_mag

    anomaly_map /= len(scales)

    # Apply mask
    if mask_resized.shape == anomaly_map.shape:
        anomaly_map[mask_resized == 0] = 0

    # Normalize to [0, 1]
    if anomaly_map.max() > 0:
        anomaly_map = anomaly_map / anomaly_map.max()

    # Save heatmap
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    axes[0].imshow(img_np.astype(np.uint8))
    axes[0].set_title("Artifact")
    axes[0].axis("off")
    im = axes[1].imshow(anomaly_map, cmap="jet", vmin=0, vmax=1)
    axes[1].set_title("Anomaly Heatmap (gradient-based)")
    axes[1].axis("off")
    plt.colorbar(im, ax=axes[1], fraction=0.046)
    plt.tight_layout()
    plt.savefig(PROCESSED_DIR / "anomaly_ead_heatmap.png", dpi=150)
    plt.close()

    # Gradient stats (after normalization to [0,1]) for distribution analysis
    masked_values = anomaly_map[anomaly_map > 0] if anomaly_map.max() > 0 else np.array([0.0])
    raw_mean = float(masked_values.mean())
    raw_std = float(masked_values.std())
    raw_p95 = float(np.percentile(masked_values, 95)) if len(masked_values) > 0 else 0.0
    # Coefficient of variation — high CV means non-uniform gradient distribution
    cv = raw_std / raw_mean if raw_mean > 0 else 0.0

    result = {
        "method": "placeholder — gradient-based heuristic",
        "status": "LIMITED — EfficientAD requires training set, unavailable for single-image analysis",
        "note": "Gradient magnitude map only shows texture edges, not true anomalies. "
                "No anomaly threshold is calibrated. Use for visualization only.",
        "gradient_mean": round(raw_mean, 4),
        "gradient_std": round(raw_std, 4),
        "gradient_p95": round(raw_p95, 4),
        "gradient_cv": round(cv, 4),
    }
    (PROCESSED_DIR / "anomaly_ead_meta.json").write_text(json.dumps(result, indent=2))
    print(f"  Gradient mean: {raw_mean:.4f}, std: {raw_std:.4f}, CV: {cv:.4f}")

    return result
