# FBI-IR-B18 — FBI Photo B18 / Фото ФБР B18

## Metadata / Метаданные

- **Source code / Код источника:** `FBI-IR-B18`
- **Agency / Агентство:** FBI (collected); imagery derived from a U.S. military system; submitted to AARO
- **Incident date / Дата инцидента:** Late 2025 (HUD timestamp `12/31/99 18:21:02` is **incorrect** — system date/time was not set; per metadata)
- **Location / Местоположение:** Western United States (specific area redacted)
- **Document kind / Тип документа:** PDF wrapping IR sensor JPG capture
- **Slug / Slug:** `fbi-photo-b18`
- **Raw file / Исходный файл:** `raw/pdf/fbi-photo-b18.pdf`
- **Transcript / Транскрипт:** `transcripts/fbi-photo-b18.txt` (bogus timestamp `12/31/99 18:21:02` only — HUD numerals not OCR-recovered; image-only PDF)
- **Source URL / URL источника:** https://www.war.gov/medialink/ufo/release_1/fbi-photo-b18.pdf
- **Cluster context / Контекст кластера:** Part of 32-photo FBI Western US 2025 IR cluster; B18 is the **closing frame of Burst 2** (~18:21:02). Cluster-level analysis in `analysis/topical/region-fbi-western-us-2023-2025.md`.

## Summary / Резюме

Monochrome IR still showing **"two small, dark, elongated objects"** near the center of the frame in the **lower left** quadrant. B18 is the last frame of Burst 2 by HUD timestamp and the **only** Burst-2 frame to place objects in the lower-left quadrant — every other Burst-2 frame puts objects in the upper-right or center. This positional shift to the opposite quadrant suggests the targets have moved significantly across the field of view by the close of Burst 2.

**RU:** Монохромный ИК-снимок с **"двумя маленькими, тёмными, удлинёнными объектами"** вблизи центра кадра в **нижнем левом** квадранте. B18 — последний кадр Серии 2 по HUD-таймстампу и **единственный** кадр Серии 2, размещающий объекты в нижнем левом квадранте — каждый другой кадр Серии 2 размещает объекты в верхнем правом или центре. Это смещение положения в противоположный квадрант предполагает, что к концу Серии 2 цели значительно переместились по полю зрения.

## Key claims / Ключевые заявления

| # | Claim / Заявление | Verdict / Вердикт | Source location / Расположение в источнике |
|---|-------|---------|-----------------|
| 1 | Image is a U.S. military system still from 2025, submitted by FBI to AARO.<br/>**RU:** Снимок получен из военной системы США 2025 года, передан ФБР в AARO. | ✅ CORROBORATED | metadata description |
| 2 | Two small, dark, elongated objects are visible near frame center in the **lower-left** quadrant.<br/>**RU:** Два маленьких, тёмных, удлинённых объекта видны вблизи центра кадра в **нижнем левом** квадранте. | ✅ CORROBORATED (AARO narrative) | metadata description |
| 3 | B18 is the final frame of Burst 2 (highest HUD timestamp in the B-series).<br/>**RU:** B18 — последний кадр Серии 2 (наибольший HUD-таймстамп в серии B). | ✅ CORROBORATED (verified against full B-series timestamp set) | comparative timestamp audit |
| 4 | Lower-left quadrant placement is unique within Burst 2.<br/>**RU:** Размещение в нижнем левом квадранте уникально в Серии 2. | ✅ CORROBORATED (verified across B1–B24 metadata) | comparative metadata audit |
| 5 | HUD timestamp `12/31/99 18:21:02` is **not** the actual capture time (RTC unset).<br/>**RU:** HUD-таймстамп `12/31/99 18:21:02` **не** является фактическим временем съёмки (RTC не установлен). | ⚠ PARTIAL (relative ordering within burst is usable; absolute time is bogus) | transcript + metadata disclaimer |

## Cross-references / Перекрёстные ссылки

**Within PURSUE corpus / В корпусе PURSUE:**
- Burst 2 sisters / Кадры-сёстры Серии 2: `FBI-IR-B13`, `FBI-IR-B14`, `FBI-IR-B15`, `FBI-IR-B16`, `FBI-IR-B17`, `FBI-IR-B19`, `FBI-IR-B20`, `FBI-IR-B21`, `FBI-IR-B22`, `FBI-IR-B23`, `FBI-IR-B24`
- Elongated-object cohort / Когорта удлинённых объектов: `FBI-IR-B13`, `FBI-IR-B22`, `FBI-IR-B23`
- [`FBI-IR-B07`](FBI-IR-B07.md) — Burst-1 helicopter anchor / якорный кадр Серии 1 с вертолётом
- [`FBI-USPER-302`](FBI-USPER-302.md) — companion FD-302 statement (orb that "broke into multiple objects" and "outran the helicopter at high speed" — B18's lower-left displacement at the end of Burst 2 is consistent with high-speed lateral movement) / сопроводительное заявление FD-302 (шар, который "распался на несколько объектов" и "обогнал вертолёт на высокой скорости" — нижне-левое смещение B18 в конце Серии 2 согласуется с высокоскоростным боковым движением)
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

- **Distinguishing feature / Отличительная черта:** Last Burst-2 frame; only one with lower-left object placement; elongated objects (vs. circular). / Последний кадр Серии 2; единственный с размещением объекта в нижнем левом; удлинённые объекты (в отличие от круглых).
- **Burst-time placement / Временное размещение в серии:** Burst 2, t = +2m09s after B19's Burst-2 opener (18:18:53 → 18:21:02). Burst 2 closes here; total Burst-2 span ≈ 2m09s.
