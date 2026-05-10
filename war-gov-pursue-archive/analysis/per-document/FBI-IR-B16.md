# FBI-IR-B16 — FBI Photo B16 / Фото ФБР B16

## Metadata / Метаданные

- **Source code / Код источника:** `FBI-IR-B16`
- **Agency / Агентство:** FBI (collected); imagery derived from a U.S. military system; submitted to AARO
- **Incident date / Дата инцидента:** Late 2025 (HUD timestamp `12/31/99 18:20:41` is **incorrect** — system date/time was not set; per metadata; OCR rendered `:` as `.`)
- **Location / Местоположение:** Western United States (specific area redacted)
- **Document kind / Тип документа:** PDF wrapping IR sensor JPG capture
- **Slug / Slug:** `fbi-photo-b16`
- **Raw file / Исходный файл:** `raw/pdf/fbi-photo-b16.pdf`
- **Transcript / Транскрипт:** `transcripts/fbi-photo-b16.txt` (HUD numeral `3` and bogus timestamp `12/31/99 18.20.41` only — image-only PDF)
- **Source URL / URL источника:** https://www.war.gov/medialink/ufo/release_1/fbi-photo-b16.pdf
- **Cluster context / Контекст кластера:** Part of 32-photo FBI Western US 2025 IR cluster; B16 is a **Burst 2** frame (~18:20:41). Cluster-level analysis in `analysis/topical/region-fbi-western-us-2023-2025.md`.

## Summary / Резюме

Monochrome IR still showing "**two dark, irregular-shaped objects**" just right of center in the upper-right quadrant. B16 differs from sister Burst-2 frames in calling out **irregular** (non-circular, non-elongated) object shapes — only Burst-2 frame to use this descriptor. Could indicate rotation, partial occlusion, or a different aspect angle on the same target pair.

**RU:** Монохромный ИК-снимок с "**двумя тёмными объектами неправильной формы**" чуть правее центра в верхнем правом квадранте. B16 отличается от кадров-сестёр Серии 2 тем, что указывает на **неправильную** (не круглую, не удлинённую) форму объектов — единственный кадр Серии 2 с таким дескриптором. Может указывать на вращение, частичное перекрытие или иной угол аспекта на ту же пару целей.

## Key claims / Ключевые заявления

| # | Claim / Заявление | Verdict / Вердикт | Source location / Расположение в источнике |
|---|-------|---------|-----------------|
| 1 | Image is a U.S. military system still from 2025, submitted by FBI to AARO.<br/>**RU:** Снимок получен из военной системы США 2025 года, передан ФБР в AARO. | ✅ CORROBORATED | metadata description |
| 2 | Two dark, **irregular-shaped** objects are visible just right of center, upper-right quadrant.<br/>**RU:** Два тёмных объекта **неправильной формы** видны чуть правее центра, верхний правый квадрант. | ✅ CORROBORATED (AARO narrative) | metadata description |
| 3 | "Irregular-shaped" descriptor is unique to B16 within Burst 2 (others use "circular" or "elongated").<br/>**RU:** Дескриптор "неправильной формы" уникален для B16 в Серии 2 (другие используют "круглый" или "удлинённый"). | ✅ CORROBORATED (verified across B1–B24 metadata) | comparative metadata audit |
| 4 | HUD timestamp `12/31/99 18:20:41` is **not** the actual capture time (RTC unset).<br/>**RU:** HUD-таймстамп `12/31/99 18:20:41` **не** является фактическим временем съёмки (RTC не установлен). | ⚠ PARTIAL (relative ordering within burst is usable; absolute time is bogus) | transcript + metadata disclaimer |
| 5 | Sensor format: monochrome IR with simplified central crosshair, HUD numeral `3` overlay.<br/>**RU:** Формат сенсора: монохромный ИК с упрощённой центральной прицельной маркой, наложение цифры HUD `3`. | ✅ CORROBORATED | metadata + transcript |

## Cross-references / Перекрёстные ссылки

**Within PURSUE corpus / В корпусе PURSUE:**
- Burst 2 sisters / Кадры-сёстры Серии 2: `FBI-IR-B13`, `FBI-IR-B14`, `FBI-IR-B15`, `FBI-IR-B17`, `FBI-IR-B18`, `FBI-IR-B19`, `FBI-IR-B20`, `FBI-IR-B21`, `FBI-IR-B22`, `FBI-IR-B23`, `FBI-IR-B24`
- [`FBI-IR-B07`](FBI-IR-B07.md) — Burst-1 helicopter anchor / якорный кадр Серии 1 с вертолётом
- [`FBI-USPER-302`](FBI-USPER-302.md) — companion FD-302 statement (orb "broke into multiple objects") / сопроводительное заявление FD-302 (шар "распался на несколько объектов")
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

- **Distinguishing feature / Отличительная черта:** Only Burst-2 frame with "irregular-shaped" two-object descriptor. Hints at non-rigid morphology, occlusion, or aspect-angle change. / Единственный кадр Серии 2 с дескриптором двух объектов "неправильной формы". Намекает на нежёсткую морфологию, перекрытие или изменение угла аспекта.
- **Burst-time placement / Временное размещение в серии:** Burst 2, t ≈ +1m48s after B19 (18:18:53 → 18:20:41).
