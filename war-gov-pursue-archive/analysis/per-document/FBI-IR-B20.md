# FBI-IR-B20 — FBI Photo B20 / Фото ФБР B20

## Metadata / Метаданные

- **Source code / Код источника:** `FBI-IR-B20`
- **Agency / Агентство:** FBI (collected); imagery derived from a U.S. military system; submitted to AARO
- **Incident date / Дата инцидента:** Late 2025 (HUD timestamp `12/31/99 18:18:58` is **incorrect** — system date/time was not set; per metadata; OCR rendered `:` as `.`)
- **Location / Местоположение:** Western United States (specific area redacted)
- **Document kind / Тип документа:** PDF wrapping IR sensor JPG capture
- **Slug / Slug:** `fbi-photo-b20`
- **Raw file / Исходный файл:** `raw/pdf/fbi-photo-b20.pdf`
- **Transcript / Транскрипт:** `transcripts/fbi-photo-b20.txt` (HUD numerals `15  15` and bogus timestamp `12/31/99 18:18.58` only — image-only PDF)
- **Source URL / URL источника:** https://www.war.gov/medialink/ufo/release_1/fbi-photo-b20.pdf
- **Cluster context / Контекст кластера:** Part of 32-photo FBI Western US 2025 IR cluster; B20 is the second Burst-2 frame (~18:18:58), +5s after B19. Cluster-level analysis in `analysis/topical/region-fbi-western-us-2023-2025.md`.

## Summary / Резюме

Monochrome IR still showing "**one to two small, dark, objects** … visible just above and to the right of the center of the reticle." B20 is the transitional frame between B19's single sub-pixel cluster and the rest of Burst 2's clear two-object frames — AARO's "one to two" hedging is unique to B20 and B21, suggesting partial resolution of a second object that wasn't yet definitive. Carries Burst-1-style HUD numerals `15  15`.

**RU:** Монохромный ИК-снимок с "**одним или двумя маленькими, тёмными объектами** … видимыми чуть выше и правее центра марки прицела". B20 — переходный кадр между единственным субпиксельным скоплением B19 и остальными чёткими кадрами Серии 2 с двумя объектами — хеджирование AARO "один или два" уникально для B20 и B21, указывая на частичное разрешение второго объекта, который ещё не был окончательно определён. Несёт цифры HUD `15  15` в стиле Серии 1.

## Key claims / Ключевые заявления

| # | Claim / Заявление | Verdict / Вердикт | Source location / Расположение в источнике |
|---|-------|---------|-----------------|
| 1 | Image is a U.S. military system still from 2025, submitted by FBI to AARO.<br/>**RU:** Снимок получен из военной системы США 2025 года, передан ФБР в AARO. | ✅ CORROBORATED | metadata description |
| 2 | "One to two small, dark, objects" are visible just above and right of reticle center.<br/>**RU:** "Один или два маленьких, тёмных объекта" видны чуть выше и правее центра марки прицела. | ✅ CORROBORATED (AARO narrative) | metadata description |
| 3 | "One to two" hedging language appears only in B20 and B21 — transitional frames within Burst 2.<br/>**RU:** Хеджирующее выражение "один или два" появляется только в B20 и B21 — переходных кадрах в Серии 2. | ✅ CORROBORATED (verified across B1–B24 metadata) | comparative metadata audit |
| 4 | B20 carries Burst-1-style HUD `15  15` like B19, before the sensor mode change.<br/>**RU:** B20 несёт HUD `15  15` в стиле Серии 1, как и B19, до смены режима сенсора. | ⚠ PARTIAL (consistent with mode change after B21; not explicitly disclosed) | transcript comparison |
| 5 | HUD timestamp `12/31/99 18:18:58` is **not** the actual capture time (RTC unset).<br/>**RU:** HUD-таймстамп `12/31/99 18:18:58` **не** является фактическим временем съёмки (RTC не установлен). | ⚠ PARTIAL (relative ordering within burst is usable; absolute time is bogus) | transcript + metadata disclaimer |

## Cross-references / Перекрёстные ссылки

**Within PURSUE corpus / В корпусе PURSUE:**
- Verbatim sister / Дословная сестра: `FBI-IR-B21` (+8s after, identical "one to two small, dark, objects" wording)
- Burst 2 sisters / Кадры-сёстры Серии 2: `FBI-IR-B13`, `FBI-IR-B14`, `FBI-IR-B15`, `FBI-IR-B16`, `FBI-IR-B17`, `FBI-IR-B18`, `FBI-IR-B19`, `FBI-IR-B22`, `FBI-IR-B23`, `FBI-IR-B24`
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

- **Distinguishing feature / Отличительная черта:** Half of the "one to two" transitional pair (with B21) — bridge between B19's single sub-pixel object and the cleanly two-object Burst-2 frames. / Половина переходной пары "один или два" (с B21) — мост между единственным субпиксельным объектом B19 и чёткими кадрами Серии 2 с двумя объектами.
- **Burst-time placement / Временное размещение в серии:** Burst 2, t = +5s after B19 (18:18:53 → 18:18:58).
