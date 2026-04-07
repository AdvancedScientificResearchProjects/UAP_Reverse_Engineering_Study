from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
PIPELINE_ROOT = Path(__file__).resolve().parent

RAW_DIR = PROJECT_ROOT / "data" / "raw"
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
REPORTS_DIR = PROJECT_ROOT / "reports" / "ai_reports"

INPUT_IMAGE = RAW_DIR / "UAP-FRAG-001.jpg"
ARTIFACT_ID = "UAP-FRAG-001"

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
REPORTS_DIR.mkdir(parents=True, exist_ok=True)

# Preprocessing
PREPROCESS_MAX_SIDE = 1024

# Grounding DINO
GDINO_MODEL = "IDEA-Research/grounding-dino-tiny"
GDINO_PROMPT = "unusual stone artifact . metallic fragment . mineral specimen ."
GDINO_BOX_THRESHOLD = 0.25
GDINO_TEXT_THRESHOLD = 0.20

# SAM2
SAM2_MODEL = "facebook/sam2-hiera-tiny"

# DINOv2
DINOV2_MODEL = "facebook/dinov2-large"

# SigLIP2
SIGLIP2_MODEL = "google/siglip2-so400m-patch14-384"
SIGLIP2_PROMPTS = [
    "a metallic fragment with unusual surface texture",
    "a mineral specimen with crystalline structure",
    "an oxidized metal artifact",
    "a ceramic fragment with geometric patterns",
    "a fossilized biological specimen",
    "a slag or industrial byproduct",
    "an engineered metamaterial sample",
    "a corroded copper or bronze artifact",
    "a volcanic rock with surface patterns",
    "a meteorite fragment",
    "a natural stone with erosion patterns",
    "an unknown material with regular surface ridges",
]

# Material hypothesis prompts (SigLIP2 zero-shot)
MATERIAL_PROMPTS = {
    "Metallic / Ferrous-like": [
        "a piece of rusted iron or steel",
        "a corroded ferrous metal fragment",
    ],
    "Metallic / Non-ferrous-like": [
        "a corroded copper or bronze artifact",
        "an oxidized aluminum fragment",
        "a tarnished silver object",
    ],
    "Ceramic / Oxide": [
        "a ceramic fragment with glaze",
        "a piece of fired clay pottery",
    ],
    "Mineral / Crystalline": [
        "a crystalline mineral specimen",
        "a quartz or feldspar crystal",
    ],
    "Mineral / Amorphous": [
        "an amorphous mineral or obsidian",
        "a volcanic glass fragment",
    ],
    "Biological / Organic": [
        "a fossilized shell or bone",
        "a calcified biological specimen",
        "a coral or sea urchin fossil",
    ],
    "Polymeric": [
        "a synthetic polymer fragment",
        "a piece of resin or plastic",
    ],
    "Exotic / Metamaterial": [
        "an engineered metamaterial with periodic structure",
        "a synthetic material with unusual microstructure",
    ],
}

# AnomalyCLIP prompts
ANOMALY_NORMAL_PROMPTS = [
    "a smooth uniform surface",
    "a natural stone surface",
    "a regular material texture",
]
ANOMALY_ABNORMAL_PROMPTS = [
    "unusual surface pattern with non-biological regularity",
    "non-natural geometric structure",
    "engineered micro-texture with mechanical precision",
    "anomalous material boundary between different substances",
    "artificial grooves with perfectly uniform spacing",
    "synthetic surface markings or inscriptions",
]

# Depth Anything V2
DEPTH_MODEL = "depth-anything/Depth-Anything-V2-Small-hf"

# Report
PIPELINE_VERSION = "3.0"
