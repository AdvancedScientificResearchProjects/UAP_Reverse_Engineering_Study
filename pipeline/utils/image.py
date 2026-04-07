import cv2
import numpy as np
from PIL import Image
from pathlib import Path


def load_image(path: Path) -> Image.Image:
    return Image.open(path).convert("RGB")


def load_cv2(path: Path) -> np.ndarray:
    img = cv2.imread(str(path))
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


def save_image(img: Image.Image | np.ndarray, path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(img, np.ndarray):
        if img.dtype == np.float32 or img.dtype == np.float64:
            img = (img * 255).clip(0, 255).astype(np.uint8)
        cv2.imwrite(str(path), cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
    else:
        img.save(path)


def resize_max_side(img: Image.Image, max_side: int) -> Image.Image:
    w, h = img.size
    if max(w, h) <= max_side:
        return img
    scale = max_side / max(w, h)
    new_w, new_h = int(w * scale), int(h * scale)
    return img.resize((new_w, new_h), Image.LANCZOS)


def apply_mask_overlay(img: np.ndarray, mask: np.ndarray, alpha: float = 0.4) -> np.ndarray:
    overlay = img.copy()
    color = np.array([0, 255, 0], dtype=np.uint8)
    overlay[mask > 0] = (
        overlay[mask > 0] * (1 - alpha) + color * alpha
    ).astype(np.uint8)
    return overlay


def crop_to_bbox(img: Image.Image, bbox: list[int], pad: int = 10) -> Image.Image:
    x1, y1, x2, y2 = bbox
    w, h = img.size
    x1 = max(0, x1 - pad)
    y1 = max(0, y1 - pad)
    x2 = min(w, x2 + pad)
    y2 = min(h, y2 + pad)
    return img.crop((x1, y1, x2, y2))
