# FBI-IR-B24 — FBI Photo B24 / Фото ФБР B24

## Metadata / Метаданные

- **Source code / Код источника:** `FBI-IR-B24`
- **Agency / Агентство:** FBI (collected); imagery derived from a U.S. military system; submitted to AARO
- **Incident date / Дата инцидента:** Late 2025 (HUD timestamp `12/31/99 18:19:40` is **incorrect** — system date/time was not set; per metadata; OCR rendered `:` as `.`)
- **Location / Местоположение:** Western United States (specific area redacted)
- **Document kind / Тип документа:** PDF wrapping IR sensor JPG capture
- **Slug / Slug:** `fbi-photo-b24`
- **Raw file / Исходный файл:** `raw/pdf/fbi-photo-b24.pdf`
- **Transcript / Транскрипт:** `transcripts/fbi-photo-b24.txt` (bogus timestamp `12/31/99 18:19.40` only — HUD numerals not OCR-recovered; image-only PDF)
- **Source URL / URL источника:** https://www.war.gov/medialink/ufo/release_1/fbi-photo-b24.pdf
- **Cluster context / Контекст кластера:** Part of 32-photo FBI Western US 2025 IR cluster; B24 is a **Burst 2** frame (~18:19:40), the highest-numbered B-frame but **not** the chronologically last — B18 (18:21:02) closes Burst 2 by HUD timestamp. Cluster-level analysis in `analysis/topical/region-fbi-western-us-2023-2025.md`.

## Summary / Резюме

Monochrome IR still showing "**a single dark, irregular-shaped object** … visible just above the center of the reticle." B24 is one of only two Burst-2 frames describing a single object (the other is B23, +7s before) and the **only** Burst-2 frame combining single-object + irregular-shape. Sequenced immediately after B23, it likely captures the same merger/occlusion event from a slightly later instant.

**RU:** Монохромный ИК-снимок с "**единственным тёмным объектом неправильной формы** … видимым чуть выше центра марки прицела". B24 — один из только двух кадров Серии 2, описывающих единственный объект (другой — B23, +7 с до), и **единственный** кадр Серии 2, сочетающий единственный объект + неправильную форму. Следующий непосредственно после B23, он, вероятно, запечатлевает то же событие слияния/перекрытия из чуть более поздней точки.

## Key claims / Ключевые заявления

| # | Claim / Заявление | Verdict / Вердикт | Source location / Расположение в источнике |
|---|-------|---------|-----------------|
| 1 | Image is a U.S. military system still from 2025, submitted by FBI to AARO.<br/>**RU:** Снимок получен из военной системы США 2025 года, передан ФБР в AARO. | ✅ CORROBORATED | metadata description |
| 2 | A single dark, irregular-shaped object is visible just above reticle center.<br/>**RU:** Единственный тёмный объект неправильной формы виден чуть выше центра марки прицела. | ✅ CORROBORATED (AARO narrative) | metadata description |
| 3 | B24 + B23 are the only two Burst-2 frames describing a single object.<br/>**RU:** B24 + B23 — единственные два кадра Серии 2, описывающих единственный объект. | ✅ CORROBORATED (verified across B1–B24 metadata) | comparative metadata audit |
| 4 | B24's "irregular" + single-object combination is unique within Burst 2.<br/>**RU:** Комбинация "неправильная форма" + единственный объект B24 уникальна в Серии 2. | ✅ CORROBORATED | comparative metadata audit |
| 5 | Despite the highest filename number, B24 is not the last frame chronologically (B18 follows at 18:21:02).<br/>**RU:** Несмотря на наибольший номер имени файла, B24 хронологически не является последним кадром (B18 следует в 18:21:02). | ✅ CORROBORATED (timestamp comparison across full B-series) | comparative timestamp audit |
| 6 | HUD timestamp `12/31/99 18:19:40` is **not** the actual capture time (RTC unset).<br/>**RU:** HUD-таймстамп `12/31/99 18:19:40` **не** является фактическим временем съёмки (RTC не установлен). | ⚠ PARTIAL (relative ordering within burst is usable; absolute time is bogus) | transcript + metadata disclaimer |

## Cross-references / Перекрёстные ссылки

**Within PURSUE corpus / В корпусе PURSUE:**
- Immediate predecessor / Непосредственный предшественник: `FBI-IR-B23` (+7s before; the other single-object Burst-2 frame / другой кадр Серии 2 с единственным объектом)
- Burst 2 sisters / Кадры-сёстры Серии 2: `FBI-IR-B13`, `FBI-IR-B14`, `FBI-IR-B15`, `FBI-IR-B16`, `FBI-IR-B17`, `FBI-IR-B18`, `FBI-IR-B19`, `FBI-IR-B20`, `FBI-IR-B21`, `FBI-IR-B22`
- [`FBI-IR-B07`](FBI-IR-B07.md) — Burst-1 helicopter anchor / якорный кадр Серии 1 с вертолётом
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

- **Distinguishing feature / Отличительная черта:** Single irregular-shape object — pairs with B23 as the only single-object Burst-2 frames; likely the same merger/occlusion moment as B23 captured 7 seconds later. / Единственный объект неправильной формы — в паре с B23 как единственные кадры Серии 2 с единственным объектом; вероятно, тот же момент слияния/перекрытия, что и B23, зафиксированный 7 секунд спустя.
- **Burst-time placement / Временное размещение в серии:** Burst 2, t = +47s after B19 (18:18:53 → 18:19:40). Filename order ≠ chronological order: by HUD timestamp Burst 2 runs B19 → B20 → B21 → B22 → B23 → B24 → B13 → B14 → B15 → B16 → B17 → B18. / Порядок имён файлов ≠ хронологический порядок: по HUD-таймстампу Серия 2 идёт B19 → B20 → B21 → B22 → B23 → B24 → B13 → B14 → B15 → B16 → B17 → B18.
