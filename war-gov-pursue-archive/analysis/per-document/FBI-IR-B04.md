# FBI-IR-B04 — FBI Photo B4 / Фото ФБР B4

## Metadata / Метаданные

- **Source code / Код источника:** `FBI-IR-B04`
- **Agency / Агентство:** FBI (collected); imagery derived from a U.S. military system; submitted to AARO
- **Incident date / Дата инцидента:** Late 2025 (HUD timestamp `12/31/99 18:12:16` is **incorrect** — system date/time was not set; per metadata)
- **Location / Местоположение:** Western United States (specific area redacted)
- **Document kind / Тип документа:** PDF wrapping IR sensor JPG capture
- **Slug / Slug:** `fbi-photo-b4`
- **Raw file / Исходный файл:** `raw/pdf/fbi-photo-b4.pdf`
- **Transcript / Транскрипт:** `transcripts/fbi-photo-b4.txt` (HUD numerals `15  15` and bogus timestamp `12/31/99 18:12:16` only — image-only PDF)
- **Source URL / URL источника:** https://www.war.gov/medialink/ufo/release_1/fbi-photo-b4.pdf
- **Cluster context / Контекст кластера:** Part of 32-photo FBI Western US 2025 IR cluster; B4 is the **closing frame of Burst 1** (~18:12:16, ~6m37s before Burst 2 opens). Cluster-level analysis in `analysis/topical/region-fbi-western-us-2023-2025.md`.

## Summary / Резюме

Monochrome IR still showing a "small, dark, circular object … in the center right quadrant, close to the center of the frame" against "an indistinct, possibly natural, landscape." B4 is the last frame in Burst 1 — after B4, the sensor goes silent for ~6m37s before Burst 2 opens at B19/18:18:53. By this point in the burst, the object has settled near reticle center and the AARO descriptor reads "natural landscape" rather than the earlier "mountain range or cloud formation."

**RU:** Монохромный ИК-снимок с "маленьким, тёмным, круглым объектом … в правом центральном квадранте, вблизи центра кадра" на фоне "неразличимого, возможно природного, ландшафта". B4 — последний кадр Серии 1: после B4 сенсор замолкает на ~6 мин 37 с, прежде чем Серия 2 открывается у B19/18:18:53. К этому моменту в серии объект осел вблизи центра марки прицела, а дескриптор AARO читается "природный ландшафт", а не прежнее "горный хребет или облачное образование".

## Key claims / Ключевые заявления

| # | Claim / Заявление | Verdict / Вердикт | Source location / Расположение в источнике |
|---|-------|---------|-----------------|
| 1 | Image is a U.S. military system still from 2025, submitted by FBI to AARO.<br/>**RU:** Снимок получен из военной системы США 2025 года, передан ФБР в AARO. | ✅ CORROBORATED | metadata description |
| 2 | A small, dark, circular object is in the center-right quadrant, close to frame center.<br/>**RU:** Маленький, тёмный, круглый объект находится в правом центральном квадранте, вблизи центра кадра. | ✅ CORROBORATED (AARO narrative) | metadata description |
| 3 | Background described as "indistinct, possibly natural, landscape".<br/>**RU:** Фон описывается как "неразличимый, возможно природный, ландшафт". | ✅ CORROBORATED | metadata description |
| 4 | HUD timestamp `12/31/99 18:12:16` is **not** the actual capture time (RTC unset).<br/>**RU:** HUD-таймстамп `12/31/99 18:12:16` **не** является фактическим временем съёмки (RTC не установлен). | ⚠ PARTIAL (relative ordering within burst is usable; absolute time is bogus) | transcript + metadata disclaimer |
| 5 | B4 is the last frame of Burst 1; gap of ~6m37s precedes Burst 2.<br/>**RU:** B4 — последний кадр Серии 1; пауза ~6 мин 37 с предшествует Серии 2. | ✅ CORROBORATED (verified against full B-series timestamp set) | comparative timestamp audit |
| 6 | Sensor format: monochrome IR with central crosshair reticle, HUD `15  15` overlay.<br/>**RU:** Формат сенсора: монохромный ИК с центральной прицельной маркой, наложение HUD `15  15`. | ✅ CORROBORATED | metadata + transcript |

## Cross-references / Перекрёстные ссылки

**Within PURSUE corpus / В корпусе PURSUE:**
- Burst 1 sisters / Кадры-сёстры Серии 1: `FBI-IR-B01`, `FBI-IR-B03`, `FBI-IR-B06`, [`FBI-IR-B07`](FBI-IR-B07.md), `FBI-IR-B08`, `FBI-IR-B09`, `FBI-IR-B10`, `FBI-IR-B11`, `FBI-IR-B12`
- Burst 2 opener / Открывающий кадр Серии 2: `FBI-IR-B19` (18:18:53, ~6m37s later)
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

- **Distinguishing feature / Отличительная черта:** Last frame of Burst 1; closes the single-object phase. Background description shifts to "natural landscape" — possibly a different look angle as tracking continues. / Последний кадр Серии 1; закрывает фазу единственного объекта. Описание фона сдвигается к "природному ландшафту" — возможно, иной угол обзора по мере продолжения сопровождения.
- **Burst-time placement / Временное размещение в серии:** Burst 1, t ≈ +2m14s after B7 anchor (18:10:02 → 18:12:16); ~6m37s gap follows before Burst 2 opens.
