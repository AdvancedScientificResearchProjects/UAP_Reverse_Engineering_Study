# FBI-IR-B19 — FBI Photo B19 / Фото ФБР B19

## Metadata / Метаданные

- **Source code / Код источника:** `FBI-IR-B19`
- **Agency / Агентство:** FBI (collected); imagery derived from a U.S. military system; submitted to AARO
- **Incident date / Дата инцидента:** Late 2025 (HUD timestamp `12/31/99 18:18:53` is **incorrect** — system date/time was not set; per metadata; OCR rendered `:` as `.`)
- **Location / Местоположение:** Western United States (specific area redacted)
- **Document kind / Тип документа:** PDF wrapping IR sensor JPG capture
- **Slug / Slug:** `fbi-photo-b19`
- **Raw file / Исходный файл:** `raw/pdf/fbi-photo-b19.pdf`
- **Transcript / Транскрипт:** `transcripts/fbi-photo-b19.txt` (HUD numerals `15  15` and bogus timestamp `12/31/99 18:18.53` only — image-only PDF)
- **Source URL / URL источника:** https://www.war.gov/medialink/ufo/release_1/fbi-photo-b19.pdf
- **Cluster context / Контекст кластера:** Part of 32-photo FBI Western US 2025 IR cluster; B19 is the **opening frame of Burst 2** (~18:18:53), ~6m37s after B4 closed Burst 1. Cluster-level analysis in `analysis/topical/region-fbi-western-us-2023-2025.md`.

## Summary / Резюме

Monochrome IR still showing "**a small cluster of dark pixels, forming an object,** … visible at the **exact center of the reticle**." B19 is the **opening frame of Burst 2** (earliest Burst-2 timestamp) and is the only B-frame to use the "small cluster of dark pixels" descriptor — possibly suggesting a barely-resolved or sub-pixel target at long range. The HUD numerals `15  15` (rather than Burst-2's `3`) suggest B19 was captured before the sensor mode change that characterizes the rest of Burst 2.

**RU:** Монохромный ИК-снимок с "**маленьким скоплением тёмных пикселей, образующих объект,** … видимым в **точном центре марки прицела**". B19 — **открывающий кадр Серии 2** (наиболее ранний таймстамп Серии 2) и единственный кадр серии B, использующий дескриптор "маленькое скопление тёмных пикселей" — возможно, указывает на едва разрешённую или субпиксельную цель на большом расстоянии. Цифры HUD `15  15` (а не `3` Серии 2) предполагают, что B19 был снят до смены режима сенсора, характерной для остальной части Серии 2.

## Key claims / Ключевые заявления

| # | Claim / Заявление | Verdict / Вердикт | Source location / Расположение в источнике |
|---|-------|---------|-----------------|
| 1 | Image is a U.S. military system still from 2025, submitted by FBI to AARO.<br/>**RU:** Снимок получен из военной системы США 2025 года, передан ФБР в AARO. | ✅ CORROBORATED | metadata description |
| 2 | A small cluster of dark pixels forming an object is at the exact center of the reticle.<br/>**RU:** Маленькое скопление тёмных пикселей, образующих объект, находится в точном центре марки прицела. | ✅ CORROBORATED (AARO narrative) | metadata description |
| 3 | "Small cluster of dark pixels" descriptor is unique to B19 (no other B-frame uses this language).<br/>**RU:** Дескриптор "маленькое скопление тёмных пикселей" уникален для B19 (ни один другой кадр серии B не использует это выражение). | ✅ CORROBORATED (verified across B1–B24 metadata) | comparative metadata audit |
| 4 | B19 carries Burst-1-style HUD numerals `15  15` despite being the first Burst-2 frame — sensor mode transition.<br/>**RU:** B19 несёт цифры HUD `15  15` в стиле Серии 1, несмотря на то что является первым кадром Серии 2 — переход режима сенсора. | ⚠ PARTIAL (consistent with mode change between bursts; not explicitly disclosed) | transcript comparison |
| 5 | B19 opens Burst 2 (earliest HUD timestamp in the burst).<br/>**RU:** B19 открывает Серию 2 (наиболее ранний HUD-таймстамп в серии). | ✅ CORROBORATED (verified against full B-series timestamp set) | comparative timestamp audit |
| 6 | HUD timestamp `12/31/99 18:18:53` is **not** the actual capture time (RTC unset).<br/>**RU:** HUD-таймстамп `12/31/99 18:18:53` **не** является фактическим временем съёмки (RTC не установлен). | ⚠ PARTIAL (relative ordering within burst is usable; absolute time is bogus) | transcript + metadata disclaimer |

## Cross-references / Перекрёстные ссылки

**Within PURSUE corpus / В корпусе PURSUE:**
- Burst 1 closer / Закрывающий кадр Серии 1: `FBI-IR-B04` (18:12:16, ~6m37s before B19)
- Burst 2 sisters / Кадры-сёстры Серии 2: `FBI-IR-B20`, `FBI-IR-B21`, `FBI-IR-B22`, `FBI-IR-B23`, `FBI-IR-B24`, `FBI-IR-B13`, `FBI-IR-B14`, `FBI-IR-B15`, `FBI-IR-B16`, `FBI-IR-B17`, `FBI-IR-B18`
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

- **Distinguishing feature / Отличительная черта:** Opens Burst 2 with a near sub-pixel target ("cluster of dark pixels"); carries Burst-1-style HUD `15  15` rather than Burst-2's `3`. Reads as the moment of re-acquisition before the operator zooms / changes sensor mode, after which the second object resolves and the rest of Burst 2 becomes two-object. / Открывает Серию 2 с почти субпиксельной целью ("скопление тёмных пикселей"); несёт HUD `15  15` в стиле Серии 1, а не `3` Серии 2. Читается как момент повторного захвата цели до того, как оператор увеличивает/меняет режим сенсора, после чего разрешается второй объект и остальная часть Серии 2 становится двухобъектной.
- **Burst-time placement / Временное размещение в серии:** Burst 2, t = 0 (opening frame).
