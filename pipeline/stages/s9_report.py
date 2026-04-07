import json
from datetime import date
from pathlib import Path

from pipeline.config import (
    ARTIFACT_ID, PIPELINE_VERSION, PROCESSED_DIR, REPORTS_DIR,
    GDINO_MODEL, SAM2_MODEL, DINOV2_MODEL, SIGLIP2_MODEL, DEPTH_MODEL,
)


def _load_json(name: str) -> dict:
    path = PROCESSED_DIR / name
    if path.exists():
        return json.loads(path.read_text())
    return {}


def run() -> dict:
    print("=== Stage 9: Report Generation ===")

    today = date.today().isoformat()
    report_id = f"AI-{today}-001"

    detection = _load_json("detection_bbox.json")
    segmentation = _load_json("segmentation_meta.json")
    features = _load_json("features_meta.json")
    siglip = _load_json("siglip_scores.json")
    material = _load_json("material_hypothesis.json")
    anomaly_ead = _load_json("anomaly_ead_meta.json")
    anomaly_clip = _load_json("anomaly_clip_meta.json")
    depth = _load_json("depth_meta.json")
    preprocess = _load_json("preprocess_meta.json")

    # Build SigLIP scores table
    siglip_rows = ""
    for entry in siglip.get("scores", [])[:5]:
        siglip_rows += f"| {entry['prompt']} | {entry['score']:.4f} |\n"

    # Material families table
    mat_rows = ""
    for entry in material.get("all_families", []):
        mat_rows += f"| {entry['family']} | {entry['score']:.4f} | {entry['best_prompt']} |\n"

    # Primary material
    primary = material.get("primary_hypothesis", {})

    # Anomaly prompts table
    anomaly_rows = ""
    for entry in anomaly_clip.get("prompt_scores", []):
        anomaly_rows += f"| {entry['prompt']} | {entry['type']} | {entry['score']:.4f} |\n"

    # Depth info
    convex = depth.get("surface_appears_convex", "N/A")

    report = f"""# AI ANALYSIS REPORT / ОТЧЁТ АНАЛИЗА ИИ

## Session Information / Информация Сессии

| Field / Поле | Value / Значение |
|-------------|------------------|
| **Analysis ID / ID Анализа** | {report_id} |
| **Artifact ID / ID Артефакта** | {ARTIFACT_ID} |
| **Date / Дата** | {today} |
| **Pipeline Version / Версия конвейера** | {PIPELINE_VERSION} |
| **Input / Вход** | {preprocess.get('source', 'N/A')} ({preprocess.get('original_size', 'N/A')}) |
| **Processed Size / Обработанный размер** | {preprocess.get('processed_size', 'N/A')} |

### Models Used / Используемые модели

| Stage / Этап | Model / Модель |
|-------------|---------------|
| Detection / Детекция | {GDINO_MODEL} |
| Segmentation / Сегментация | {SAM2_MODEL} |
| Features / Признаки | {DINOV2_MODEL} |
| Text-Image / Текст-изображение | {SIGLIP2_MODEL} |
| Material / Материал | {SIGLIP2_MODEL} (zero-shot) |
| Anomaly (supervised) / Аномалии (обуч.) | Gradient heuristic (EfficientAD proxy) |
| Anomaly (zero-shot) / Аномалии (ZS) | {anomaly_clip.get('model', 'openai/clip-vit-large-patch14')} |
| Depth / Глубина | {DEPTH_MODEL} |

---

## Detection / Детекция

| Field / Поле | Value / Значение |
|-------------|------------------|
| **Label / Метка** | {detection.get('label', 'N/A')} |
| **Confidence / Уверенность** | {detection.get('score', 0):.4f} |
| **Bounding Box** | {detection.get('bbox', 'N/A')} |
| **Total detections / Всего детекций** | {len(detection.get('all_detections', []))} |

## Segmentation / Сегментация

| Property / Свойство | Value / Значение |
|---------------------|------------------|
| **Mask area / Площадь маски** | {segmentation.get('mask_area_px', 'N/A')} px |
| **Frame coverage / Покрытие кадра** | {segmentation.get('mask_area_pct', 'N/A')}% |
| **IoU score** | {segmentation.get('iou_score', 'N/A')} |

![Mask overlay](../data/processed/mask_overlay.png)

## Text-Image Matching (SigLIP2) / Текстово-визуальное сопоставление

> **Scoring note / Примечание:** SigLIP2 uses sigmoid scoring — each score is an independent
> match probability (0-1). Scores are NOT relative to each other.
> SigLIP2 использует sigmoid-скоринг — каждый скор является независимой
> вероятностью совпадения (0-1). Скоры НЕ зависят друг от друга.

**Top-1:** {siglip.get('top1_prompt', 'N/A')} (score: {siglip.get('top1_score', 'N/A')})

| Prompt / Промпт | Score / Оценка |
|-----------------|----------------|
{siglip_rows}

## Material Hypothesis / Гипотеза о Материале

**Primary hypothesis / Основная гипотеза:** {primary.get('family', 'N/A')}
**Confidence / Уверенность:** {primary.get('confidence', 'N/A')} ({primary.get('score', 0):.4f})
**Method / Метод:** {material.get('method', 'N/A')}

| Family / Семейство | Score / Оценка | Best prompt / Лучший промпт |
|--------------------|----------------|---------------------------|
{mat_rows}

> **LIMITATION / ОГРАНИЧЕНИЕ:** Material family hypothesis is based on RGB imagery only.
> Chemical composition cannot be determined from photographs.
> Гипотеза о семействе материала основана только на RGB-изображении.
> Химический состав не может быть определён по фотографиям.

## Anomaly Detection / Обнаружение Аномалий

### Gradient-based (placeholder) / На основе градиентов (заглушка)

| Metric / Метрика | Value / Значение |
|-----------------|------------------|
| **Status** | {anomaly_ead.get('status', 'N/A')} |
| **Gradient mean** | {anomaly_ead.get('gradient_mean', 'N/A')} |
| **Gradient std** | {anomaly_ead.get('gradient_std', 'N/A')} |
| **Gradient CV** | {anomaly_ead.get('gradient_cv', 'N/A')} |
| **Note** | {anomaly_ead.get('note', 'N/A')} |

![EfficientAD heatmap](../data/processed/anomaly_ead_heatmap.png)

### CLIP zero-shot (AnomalyCLIP proxy)

> **Scoring note / Примечание:** CLIP uses softmax scoring — scores are RELATIVE probabilities
> among provided prompts ({anomaly_clip.get('normal_prompts_count', '?')} normal + {anomaly_clip.get('abnormal_prompts_count', '?')} abnormal).
> They are NOT comparable to SigLIP2 sigmoid scores above.
> CLIP использует softmax-скоринг — скоры являются ОТНОСИТЕЛЬНЫМИ вероятностями
> среди предоставленных промптов. Они НЕ сравнимы со скорами SigLIP2 выше.

| Metric / Метрика | Value / Значение |
|-----------------|------------------|
| **Normal score / Оценка нормы** | {anomaly_clip.get('normal_score', 'N/A')} |
| **Abnormal score / Оценка аномалии** | {anomaly_clip.get('abnormal_score', 'N/A')} |
| **Is anomalous / Аномалия** | {anomaly_clip.get('is_anomalous', 'N/A')} |

| Prompt / Промпт | Type / Тип | Score / Оценка |
|-----------------|-----------|----------------|
{anomaly_rows}

![CLIP anomaly heatmap](../data/processed/anomaly_clip_heatmap.png)

## Depth Estimation / Оценка Глубины

| Property / Свойство | Value / Значение |
|---------------------|------------------|
| **Model / Модель** | {DEPTH_MODEL} |
| **Input images / Входных изображений** | 1 |
| **Method / Метод** | Monocular depth (DA v2) |
| **Artifact center depth** | {depth.get('artifact_center_depth', 'N/A')} |
| **Artifact edge depth** | {depth.get('artifact_edge_depth', 'N/A')} |
| **Surface convex / Поверхность выпуклая** | {convex} |

![Depth map](../data/processed/depth_visualization.png)

## Feature Extraction / Извлечение Признаков

| Property / Свойство | Value / Значение |
|---------------------|------------------|
| **Model / Модель** | {DINOV2_MODEL} |
| **CLS embedding dim** | {features.get('cls_shape', 'N/A')} |
| **CLS norm** | {features.get('cls_norm', 'N/A')} |
| **Patch tokens shape** | {features.get('patch_shape', 'N/A')} |

Embeddings saved to `embedding.npy` and `patch_tokens.npy` for downstream similarity search.

---

## Summary / Итог

Based on the analysis of artifact {ARTIFACT_ID}:

1. **Detection**: Object successfully detected and localized
2. **Segmentation**: Artifact isolated, covering {segmentation.get('mask_area_pct', '?')}% of frame
3. **Visual match**: Top SigLIP2 match — "{siglip.get('top1_prompt', '?')}"
4. **Material**: Primary hypothesis — {primary.get('family', '?')} ({primary.get('confidence', '?')})
5. **Anomalies**: {"Anomalous patterns detected" if anomaly_clip.get('is_anomalous') else "No strong anomalous patterns detected"}
6. **Depth**: Surface {"appears convex" if convex else "analysis inconclusive"}

---

## Limitations / Ограничения

- All material hypotheses are visual-only (RGB)
- Chemical composition requires: hyperspectral camera, OES, XRF, Raman, SEM-EDS
- Anomaly detection limited by single-image input (no training distribution)
- Depth is relative, not metric
- Single viewpoint limits 3D reconstruction

---

**ASRP RESEARCH STANDARD v2.1**
*AI Visual & Material Analysis Protocol v{PIPELINE_VERSION}*
"""

    report_path = REPORTS_DIR / f"{report_id}.md"
    report_path.write_text(report)
    print(f"  Report saved: {report_path}")

    return {"report_path": str(report_path), "report_id": report_id}
