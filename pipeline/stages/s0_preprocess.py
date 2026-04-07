import json
from pathlib import Path
from PIL import Image

from pipeline.config import INPUT_IMAGE, PROCESSED_DIR, PREPROCESS_MAX_SIDE
from pipeline.utils.image import load_image, save_image, resize_max_side


def run() -> dict:
    print("=== Stage 0: Preprocess ===")
    img = load_image(INPUT_IMAGE)
    orig_size = img.size
    print(f"  Original size: {orig_size}")

    img = resize_max_side(img, PREPROCESS_MAX_SIDE)
    new_size = img.size
    print(f"  Resized to: {new_size}")

    out_path = PROCESSED_DIR / "preprocessed.png"
    save_image(img, out_path)

    meta = {
        "original_size": list(orig_size),
        "processed_size": list(new_size),
        "source": str(INPUT_IMAGE.name),
        "output": str(out_path.relative_to(out_path.parent.parent.parent)),
    }
    (PROCESSED_DIR / "preprocess_meta.json").write_text(
        json.dumps(meta, indent=2)
    )
    print(f"  Saved: {out_path}")
    return meta
