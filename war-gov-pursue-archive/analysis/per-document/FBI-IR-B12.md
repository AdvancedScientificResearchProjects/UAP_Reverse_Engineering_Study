# FBI-IR-B12 — FBI Photo B12 / Фото ФБР B12

## Metadata / Метаданные

- **Source code / Код источника:** `FBI-IR-B12`
- **Agency / Агентство:** FBI (collected); imagery derived from a U.S. military system; submitted to AARO
- **Incident date / Дата инцидента:** Late 2025 (HUD timestamp `12/31/99 18:11:12` is **incorrect** — system date/time was not set; per metadata)
- **Location / Местоположение:** Western United States (specific area redacted)
- **Document kind / Тип документа:** PDF wrapping IR sensor JPG capture
- **Slug / Slug:** `fbi-photo-b12`
- **Raw file / Исходный файл:** `raw/pdf/fbi-photo-b12.pdf`
- **Transcript / Транскрипт:** `transcripts/fbi-photo-b12.txt` (HUD numerals `15  15` and bogus timestamp `12/31/99 18:11:12` only — image-only PDF)
- **Source URL / URL источника:** https://www.war.gov/medialink/ufo/release_1/fbi-photo-b12.pdf
- **Cluster context / Контекст кластера:** Part of 32-photo FBI Western US 2025 IR cluster; B12 is the seventh Burst-1 frame, +70 seconds after the B7 helicopter capture. Cluster-level analysis in `analysis/topical/region-fbi-western-us-2023-2025.md`.

## Summary / Резюме

Monochrome IR still showing a "small, dark, circular object … in the upper right quadrant of the frame" against an "indistinct mountain range." Description is verbatim identical to B11 — only the HUD timestamp differs (+6s). Reads as a continuous tracking sequence with stable target geometry.

**RU:** Монохромный ИК-снимок с "маленьким, тёмным, круглым объектом … в верхнем правом квадранте кадра" на фоне "неразличимого горного хребта". Описание дословно идентично B11 — отличается только HUD-таймстамп (+6 с). Читается как непрерывная последовательность сопровождения со стабильной геометрией цели.

## Key claims / Ключевые заявления

| # | Claim / Заявление | Verdict / Вердикт | Source location / Расположение в источнике |
|---|-------|---------|-----------------|
| 1 | Image is a U.S. military system still from 2025, submitted by FBI to AARO.<br/>**RU:** Снимок получен из военной системы США 2025 года, передан ФБР в AARO. | ✅ CORROBORATED | metadata description |
| 2 | A small, dark, circular object is in the upper-right quadrant.<br/>**RU:** Маленький, тёмный, круглый объект находится в верхнем правом квадранте. | ✅ CORROBORATED (AARO narrative) | metadata description |
| 3 | Background is an indistinct mountain range.<br/>**RU:** Фон — неразличимый горный хребет. | ✅ CORROBORATED | metadata description |
| 4 | HUD timestamp `12/31/99 18:11:12` is **not** the actual capture time (RTC unset).<br/>**RU:** HUD-таймстамп `12/31/99 18:11:12` **не** является фактическим временем съёмки (RTC не установлен). | ⚠ PARTIAL (relative ordering within burst is usable; absolute time is bogus) | transcript + metadata disclaimer |
| 5 | B12's AARO description is verbatim identical to B11 (only timestamp differs).<br/>**RU:** Описание AARO B12 дословно идентично B11 (отличается только таймстамп). | ✅ CORROBORATED | comparative metadata audit |

## Cross-references / Перекрёстные ссылки

**Within PURSUE corpus / В корпусе PURSUE:**
- Verbatim sister / Дословная сестра: `FBI-IR-B11` (+6s before)
- Burst 1 sisters / Кадры-сёстры Серии 1: `FBI-IR-B01`, `FBI-IR-B03`, `FBI-IR-B04`, `FBI-IR-B06`, [`FBI-IR-B07`](FBI-IR-B07.md), `FBI-IR-B08`, `FBI-IR-B09`, `FBI-IR-B10`
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

- **Distinguishing feature / Отличительная черта:** Verbatim duplicate of B11's AARO narrative (+6s later) — a clean steady-tracking pair within Burst 1. / Дословный дубликат нарратива AARO B11 (+6 с спустя) — чёткая пара устойчивого сопровождения в Серии 1.
- **Burst-time placement / Временное размещение в серии:** Burst 1, t = +70s after B7 anchor (18:10:02 → 18:11:12).
