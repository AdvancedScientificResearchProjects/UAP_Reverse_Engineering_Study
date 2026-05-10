# FBI-IR-B23 — FBI Photo B23 / Фото ФБР B23

## Metadata / Метаданные

- **Source code / Код источника:** `FBI-IR-B23`
- **Agency / Агентство:** FBI (collected); imagery derived from a U.S. military system; submitted to AARO
- **Incident date / Дата инцидента:** Late 2025 (HUD timestamp `12/31/99 18:19:33` is **incorrect** — system date/time was not set; per metadata; OCR rendered `:` as `*` and `.`)
- **Location / Местоположение:** Western United States (specific area redacted)
- **Document kind / Тип документа:** PDF wrapping IR sensor JPG capture
- **Slug / Slug:** `fbi-photo-b23`
- **Raw file / Исходный файл:** `raw/pdf/fbi-photo-b23.pdf`
- **Transcript / Транскрипт:** `transcripts/fbi-photo-b23.txt` (bogus timestamp `12/31/99 18*19.33` only — HUD numerals not OCR-recovered; image-only PDF)
- **Source URL / URL источника:** https://www.war.gov/medialink/ufo/release_1/fbi-photo-b23.pdf
- **Cluster context / Контекст кластера:** Part of 32-photo FBI Western US 2025 IR cluster; B23 is a **Burst 2** frame (~18:19:33). Cluster-level analysis in `analysis/topical/region-fbi-western-us-2023-2025.md`.

## Summary / Резюме

Monochrome IR still showing "**a single dark, elongated object** … visible near the edge of the reticle to the right of center." B23 is the **only** Burst-2 frame to describe a *single* object rather than two — every other Burst-2 frame describes two (or "one to two") objects. Combined with the elongated descriptor, B23 may capture either (a) the moment when one of the two objects briefly merged with or occluded the other, or (b) one of the two objects falling outside the frame.

**RU:** Монохромный ИК-снимок с "**единственным тёмным, удлинённым объектом** … видимым вблизи края марки прицела правее центра". B23 — **единственный** кадр Серии 2, описывающий *единственный* объект, а не два — каждый другой кадр Серии 2 описывает два (или "один или два") объекта. В сочетании с дескриптором "удлинённый" B23 может запечатлевать либо (a) момент, когда один из двух объектов кратко слился с другим или закрыл его, либо (b) выход одного из двух объектов за пределы кадра.

## Key claims / Ключевые заявления

| # | Claim / Заявление | Verdict / Вердикт | Source location / Расположение в источнике |
|---|-------|---------|-----------------|
| 1 | Image is a U.S. military system still from 2025, submitted by FBI to AARO.<br/>**RU:** Снимок получен из военной системы США 2025 года, передан ФБР в AARO. | ✅ CORROBORATED | metadata description |
| 2 | A single dark, elongated object is visible near the edge of the reticle, right of center.<br/>**RU:** Единственный тёмный, удлинённый объект виден вблизи края марки прицела, правее центра. | ✅ CORROBORATED (AARO narrative) | metadata description |
| 3 | B23 is the **only** Burst-2 frame to describe a single object.<br/>**RU:** B23 — **единственный** кадр Серии 2, описывающий единственный объект. | ✅ CORROBORATED (verified across B1–B24 metadata) | comparative metadata audit |
| 4 | The single-object reading in mid-Burst-2 (between two-object frames B22 and B24) is anomalous; suggests merger, occlusion, or an out-of-frame second target.<br/>**RU:** Прочтение единственного объекта в середине Серии 2 (между кадрами с двумя объектами B22 и B24) аномально; предполагает слияние, перекрытие или вторую цель вне кадра. | ⬜ UNRESOLVED (cannot disambiguate from text alone) | inference |
| 5 | HUD timestamp `12/31/99 18:19:33` is **not** the actual capture time (RTC unset).<br/>**RU:** HUD-таймстамп `12/31/99 18:19:33` **не** является фактическим временем съёмки (RTC не установлен). | ⚠ PARTIAL (relative ordering within burst is usable; absolute time is bogus) | transcript + metadata disclaimer |

## Cross-references / Перекрёстные ссылки

**Within PURSUE corpus / В корпусе PURSUE:**
- Burst 2 sisters / Кадры-сёстры Серии 2: `FBI-IR-B13`, `FBI-IR-B14`, `FBI-IR-B15`, `FBI-IR-B16`, `FBI-IR-B17`, `FBI-IR-B18`, `FBI-IR-B19`, `FBI-IR-B20`, `FBI-IR-B21`, `FBI-IR-B22`, `FBI-IR-B24`
- Elongated-object cohort / Когорта удлинённых объектов: `FBI-IR-B13`, `FBI-IR-B18`, `FBI-IR-B22`
- [`FBI-IR-B07`](FBI-IR-B07.md) — Burst-1 helicopter anchor / якорный кадр Серии 1 с вертолётом
- [`FBI-USPER-302`](FBI-USPER-302.md) — companion FD-302 statement (objects "broke into multiple objects" — B23's single-object reading inverts that pattern, possibly capturing the moment of recombination or a tracking-loss event) / сопроводительное заявление FD-302 (объекты "распались на несколько объектов" — прочтение единственного объекта B23 инвертирует этот паттерн, возможно фиксируя момент рекомбинации или событие потери сопровождения)
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

- **Distinguishing feature / Отличительная черта:** Only Burst-2 frame with a single object, sandwiched between two-object frames B22 (+14s before) and B24 (+7s after). Suggests transient merger/occlusion or one target moving out of frame. / Единственный кадр Серии 2 с единственным объектом, зажатый между кадрами с двумя объектами B22 (+14 с до) и B24 (+7 с после). Указывает на кратковременное слияние/перекрытие или выход одной цели за пределы кадра.
- **Burst-time placement / Временное размещение в серии:** Burst 2, t = +40s after B19 (18:18:53 → 18:19:33).
