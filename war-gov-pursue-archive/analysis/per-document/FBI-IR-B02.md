# FBI-IR-B02 — FBI Photo B2 / Фото ФБР B2

## Metadata / Метаданные

- **Source code / Код источника:** `FBI-IR-B02`
- **Agency / Агентство:** FBI (collected); imagery derived from a U.S. military system; submitted to AARO
- **Incident date / Дата инцидента:** Late 2025 (no HUD timestamp recovered from OCR — only the `15   15` HUD numerals)
- **Location / Местоположение:** Western United States (specific area redacted)
- **Document kind / Тип документа:** PDF wrapping IR sensor JPG capture
- **Slug / Slug:** `fbi-photo-b2`
- **Raw file / Исходный файл:** `raw/pdf/fbi-photo-b2.pdf`
- **Transcript / Транскрипт:** `transcripts/fbi-photo-b2.txt` (only `15   15` HUD numerals — **timestamp not OCR-recovered**, image-only PDF)
- **Source URL / URL источника:** https://www.war.gov/medialink/ufo/release_1/fbi-photo-b2.pdf
- **Cluster context / Контекст кластера:** Part of 32-photo FBI Western US 2025 IR cluster. B2 is one of two B-frames (B2 and B5) where the OCR did not recover a HUD timestamp — burst placement must be inferred from the (single-object) target description, which puts B2 in **Burst 1**. Cluster-level analysis in `analysis/topical/region-fbi-western-us-2023-2025.md`.

## Summary / Резюме

Monochrome IR still showing a "small, dark, circular object … in the upper right quadrant" against an "indistinct mountain range or cloud formation." Target description is essentially identical to B1, B11, and B12 (modal Burst-1 frame). The OCR did not recover a usable timestamp, so B2's exact place in the burst sequence cannot be fixed from text alone — but the *single-object* description places it firmly in Burst 1, not Burst 2.

**RU:** Монохромный ИК-снимок с "маленьким, тёмным, круглым объектом … в верхнем правом квадранте" на фоне "неразличимого горного хребта или облачного образования". Описание цели практически идентично B1, B11 и B12 (модальный кадр Серии 1). OCR не восстановил пригодный таймстамп, поэтому точное место B2 в последовательности серии не может быть определено по тексту — но описание *единственного объекта* твёрдо помещает его в Серию 1, а не в Серию 2.

## Key claims / Ключевые заявления

| # | Claim / Заявление | Verdict / Вердикт | Source location / Расположение в источнике |
|---|-------|---------|-----------------|
| 1 | Image is a U.S. military system still from 2025, submitted by FBI to AARO.<br/>**RU:** Снимок получен из военной системы США 2025 года, передан ФБР в AARO. | ✅ CORROBORATED | metadata description |
| 2 | A small, dark, circular object is visible in the upper-right quadrant.<br/>**RU:** Маленький, тёмный, круглый объект виден в верхнем правом квадранте. | ✅ CORROBORATED (AARO narrative) | metadata description |
| 3 | Background is an indistinct mountain range or cloud formation.<br/>**RU:** Фон — неразличимый горный хребет или облачное образование. | ✅ CORROBORATED | metadata description |
| 4 | HUD timestamp not recoverable from OCR (only `15   15` numerals).<br/>**RU:** HUD-таймстамп не восстановим из OCR (только цифры `15   15`). | ⚠ PARTIAL (timestamp likely present in raw image but OCR-missed) | transcript |
| 5 | B2 belongs to Burst 1 by target-class inference (single object, mountain/cloud background).<br/>**RU:** B2 относится к Серии 1 по выводу класса цели (единственный объект, фон гора/облако). | ⬜ UNRESOLVED (no direct timestamp evidence) | comparative analysis |
| 6 | Sensor format: monochrome IR with central crosshair reticle, HUD `15  15` overlay.<br/>**RU:** Формат сенсора: монохромный ИК с центральной прицельной маркой, наложение HUD `15  15`. | ✅ CORROBORATED | metadata + transcript |

## Cross-references / Перекрёстные ссылки

**Within PURSUE corpus / В корпусе PURSUE:**
- Burst 1 sisters / Кадры-сёстры Серии 1: `FBI-IR-B01`, `FBI-IR-B06`, [`FBI-IR-B07`](FBI-IR-B07.md), `FBI-IR-B08`, `FBI-IR-B09`, `FBI-IR-B10`, `FBI-IR-B11`, `FBI-IR-B12`, `FBI-IR-B03`, `FBI-IR-B04`
- `FBI-IR-B05` — the other timestamp-missing B-frame / другой кадр серии B без таймстампа
- [`FBI-IR-B07`](FBI-IR-B07.md) — only frame with helicopter visible; anchors USPER-302 cross-link / единственный кадр с видимым вертолётом; якорь перекрёстной ссылки USPER-302
- [`FBI-USPER-302`](FBI-USPER-302.md) — companion FD-302 statement / сопроводительное заявление FD-302
- [`DOW-WESTERN-US-2023`](DOW-WESTERN-US-2023.md) — likely overlapping event campaign / вероятно пересекающаяся событийная кампания
- See [`topical/region-fbi-western-us-2023-2025.md`](../topical/region-fbi-western-us-2023-2025.md) for cluster-level analysis / см. анализ на уровне кластера

## Open questions / Открытые вопросы

1. What is the actual sensor-time of this frame within the larger Western US 2025 IR cluster? See burst-time analysis in [`region-fbi-western-us-2023-2025.md`](../topical/region-fbi-western-us-2023-2025.md).

   **RU:** Каково фактическое время сенсора для данного кадра в более широком ИК-кластере Западных США 2025 года? См. анализ времени серий в [`region-fbi-western-us-2023-2025.md`](../topical/region-fbi-western-us-2023-2025.md).

2. What does the underlying JPG (wrapped inside this PDF) look like at full resolution? The PDF wrapper does not expose camera/lens/sensor metadata.

   **RU:** Как выглядит исходный JPG (обёрнутый в PDF) в полном разрешении? Обёртка PDF не раскрывает метаданные камеры/объектива/сенсора.

3. Does this frame correlate with the USPER-302 narrative arc? See [`FBI-USPER-302`](FBI-USPER-302.md) and [`DOW-WESTERN-US-2023`](DOW-WESTERN-US-2023.md) for the ground-pursuit context.

   **RU:** Коррелирует ли данный кадр с повествовательной дугой USPER-302? См. [`FBI-USPER-302`](FBI-USPER-302.md) и [`DOW-WESTERN-US-2023`](DOW-WESTERN-US-2023.md) для контекста наземного преследования.

## Notes / Замечания

- **Distinguishing feature / Отличительная черта:** No HUD timestamp in OCR output — one of only two B-frames (B2, B5) in this state. May warrant manual visual inspection of the raw PDF to recover the timestamp and pin B2 inside Burst 1. / Нет HUD-таймстампа в выводе OCR — один из только двух кадров серии B (B2, B5) в таком состоянии. Может потребовать ручного визуального осмотра исходного PDF для восстановления таймстампа и привязки B2 внутри Серии 1.
- **Burst-time placement / Временное размещение в серии:** Burst 1 (inferred from target class), exact ordering unknown.
