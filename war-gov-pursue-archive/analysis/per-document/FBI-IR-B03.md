# FBI-IR-B03 — FBI Photo B3 / Фото ФБР B3

## Metadata / Метаданные

- **Source code / Код источника:** `FBI-IR-B03`
- **Agency / Агентство:** FBI (collected); imagery derived from a U.S. military system; submitted to AARO
- **Incident date / Дата инцидента:** Late 2025 (HUD timestamp `12/31/99 18:11:34` is **incorrect** — system date/time was not set; per metadata)
- **Location / Местоположение:** Western United States (specific area redacted)
- **Document kind / Тип документа:** PDF wrapping IR sensor JPG capture
- **Slug / Slug:** `fbi-photo-b3`
- **Raw file / Исходный файл:** `raw/pdf/fbi-photo-b3.pdf`
- **Transcript / Транскрипт:** `transcripts/fbi-photo-b3.txt` (HUD numerals `15  15` and bogus timestamp `12/31/99 18:11:34` only — image-only PDF)
- **Source URL / URL источника:** https://www.war.gov/medialink/ufo/release_1/fbi-photo-b3.pdf
- **Cluster context / Контекст кластера:** Part of 32-photo FBI Western US 2025 IR cluster; B3 sits in **Burst 1** (single-object phase, ~18:10–18:12). Cluster-level analysis in `analysis/topical/region-fbi-western-us-2023-2025.md`.

## Summary / Резюме

Monochrome IR still showing a "small, dark, circular object … just to the right of the center of the reticle" against an "indistinct mountain range or cloud formation." B3 is a near-centered target (closer than B1's "upper right quadrant"). At t = 18:11:34 it is the second-to-last Burst-1 frame, suggesting the operator has refined tracking by this point in the sequence.

**RU:** Монохромный ИК-снимок с "маленьким, тёмным, круглым объектом … чуть правее центра марки прицела" на фоне "неразличимого горного хребта или облачного образования". B3 — почти центрированная цель (ближе к центру, чем "верхний правый квадрант" у B1). При t = 18:11:34 это предпоследний кадр Серии 1, что указывает на то, что к этому моменту в последовательности оператор уточнил сопровождение.

## Key claims / Ключевые заявления

| # | Claim / Заявление | Verdict / Вердикт | Source location / Расположение в источнике |
|---|-------|---------|-----------------|
| 1 | Image is a U.S. military system still from 2025, submitted by FBI to AARO.<br/>**RU:** Снимок получен из военной системы США 2025 года, передан ФБР в AARO. | ✅ CORROBORATED | metadata description |
| 2 | A small, dark, circular object is visible just right of reticle center.<br/>**RU:** Маленький, тёмный, круглый объект виден чуть правее центра марки прицела. | ✅ CORROBORATED (AARO narrative) | metadata description |
| 3 | Background is an indistinct mountain range or cloud formation.<br/>**RU:** Фон — неразличимый горный хребет или облачное образование. | ✅ CORROBORATED | metadata description |
| 4 | HUD timestamp `12/31/99 18:11:34` is **not** the actual capture time (RTC unset).<br/>**RU:** HUD-таймстамп `12/31/99 18:11:34` **не** является фактическим временем съёмки (RTC не установлен). | ⚠ PARTIAL (relative ordering within burst is usable; absolute time is bogus) | transcript + metadata disclaimer |
| 5 | Sensor format: monochrome IR with central crosshair reticle, HUD `15  15` overlay.<br/>**RU:** Формат сенсора: монохромный ИК с центральной прицельной маркой, наложение HUD `15  15`. | ✅ CORROBORATED | metadata + transcript |

## Cross-references / Перекрёстные ссылки

**Within PURSUE corpus / В корпусе PURSUE:**
- Burst 1 sisters / Кадры-сёстры Серии 1: `FBI-IR-B01`, `FBI-IR-B06`, [`FBI-IR-B07`](FBI-IR-B07.md), `FBI-IR-B08`, `FBI-IR-B09`, `FBI-IR-B10`, `FBI-IR-B11`, `FBI-IR-B12`, `FBI-IR-B04`
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

- **Distinguishing feature / Отличительная черта:** Object position has migrated from upper-right (B1) to "just right of center" (B3) — minor but consistent with active tracking refinement during Burst 1. / Положение объекта переместилось из верхнего правого (B1) к "чуть правее центра" (B3) — незначительно, но согласуется с активным уточнением сопровождения в ходе Серии 1.
- **Burst-time placement / Временное размещение в серии:** Burst 1, t ≈ +1m32s after B7 anchor (18:10:02 → 18:11:34); penultimate Burst-1 frame before B4 closes the burst at 18:12:16.
