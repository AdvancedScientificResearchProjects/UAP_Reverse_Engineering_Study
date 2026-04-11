# AI Analysis Pipeline / Конвейер ИИ-анализа

Multi-stage computer vision pipeline for UAP-FRAG-001 analysis. Full protocol specification: [experiments/protocol_ai.md](../experiments/protocol_ai.md).

Многоэтапный конвейер компьютерного зрения для анализа UAP-FRAG-001. Полная спецификация протокола: [experiments/protocol_ai.md](../experiments/protocol_ai.md).

---

## Stages / Этапы

| # | File | Input | Output | Model |
|---|------|-------|--------|-------|
| 0 | `stages/s0_preprocess.py` | `data/raw/UAP-FRAG-001.jpg` | `preprocessed.png`, `preprocess_meta.json` | — |
| 1 | `stages/s1_detect.py` | `preprocessed.png` | `detection_bbox.json` | `IDEA-Research/grounding-dino-tiny` |
| 2 | `stages/s2_segment.py` | `preprocessed.png`, `detection_bbox.json` | `mask.png`, `artifact_crop.png`, `segmentation_meta.json` | `facebook/sam2-hiera-tiny` |
| 3 | `stages/s3_features.py` | `artifact_crop.png` | `features_meta.json` | `facebook/dinov2-large` |
| 4 | `stages/s4_siglip.py` | `artifact_crop.png` | `siglip_scores.json` | `google/siglip2-so400m-patch14-384` |
| 5 | `stages/s5_material.py` | `artifact_crop.png` | `material_hypothesis.json` | `google/siglip2-so400m-patch14-384` |
| 6 | `stages/s6_anomaly_ead.py` | `artifact_crop.png` | `anomaly_ead_meta.json` | EfficientAD |
| 7 | `stages/s7_anomaly_clip.py` | `artifact_crop.png` | `anomaly_clip_meta.json` | CLIP (ViT-B/16) |
| 8 | `stages/s8_depth.py` | `preprocessed.png`, `detection_bbox.json` | `depth_map.png`, `depth_meta.json` | `depth-anything/Depth-Anything-V2-Small-hf` |
| 9 | `stages/s9_report.py` | all `*_meta.json` | AI analysis report | — |

---

## Running / Запуск

```bash
python -m pipeline.run
```

Requires `data/raw/UAP-FRAG-001.jpg` (see [Issue #4](https://github.com/AdvancedScientificResearchProjects/UAP_Reverse_Engineering_Study/issues/4)).
Требуется `data/raw/UAP-FRAG-001.jpg`.

## Configuration / Конфигурация

All model names, prompts, and thresholds live in [`config.py`](config.py).
Все модели, промпты и пороги — в [`config.py`](config.py).

## Utilities / Утилиты

- `utils/image.py` — image loading, cropping, mask overlay
- `utils/vram.py` — GPU memory management, model unloading
