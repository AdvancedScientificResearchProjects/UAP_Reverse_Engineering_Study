# FBI-IR-B11 — FBI Photo B11 / Фото ФБР B11

## Metadata / Метаданные

- **Source code / Код источника:** `FBI-IR-B11`
- **Agency / Агентство:** FBI (collected); imagery derived from a U.S. military system; submitted to AARO
- **Incident date / Дата инцидента:** Late 2025 (HUD timestamp `12/31/99 18:11:06` is **incorrect** — system date/time was not set; per metadata)
- **Location / Местоположение:** Western United States (specific area redacted)
- **Document kind / Тип документа:** PDF wrapping IR sensor JPG capture
- **Slug / Slug:** `fbi-photo-b11`
- **Raw file / Исходный файл:** `raw/pdf/fbi-photo-b11.pdf`
- **Transcript / Транскрипт:** `transcripts/fbi-photo-b11.txt` (HUD numerals `15  15` and bogus timestamp `12/31/99 18:11:06` only — image-only PDF)
- **Source URL / URL источника:** https://www.war.gov/medialink/ufo/release_1/fbi-photo-b11.pdf
- **Cluster context / Контекст кластера:** Part of 32-photo FBI Western US 2025 IR cluster; B11 is the sixth Burst-1 frame, +64 seconds after the B7 helicopter capture. Cluster-level analysis in `analysis/topical/region-fbi-western-us-2023-2025.md`.

## Summary / Резюме

Monochrome IR still showing a "small, dark, circular object … in the upper right quadrant of the frame" against an "indistinct mountain range." Modal Burst-1 description; functionally a duplicate of B10/B12 except for HUD timestamp.

**RU:** Монохромный ИК-снимок с "маленьким, тёмным, круглым объектом … в верхнем правом квадранте кадра" на фоне "неразличимого горного хребта". Модальное описание Серии 1; функционально дублирует B10/B12, отличаясь только HUD-таймстампом.

## Key claims / Ключевые заявления

| # | Claim / Заявление | Verdict / Вердикт | Source location / Расположение в источнике |
|---|-------|---------|-----------------|
| 1 | Image is a U.S. military system still from 2025, submitted by FBI to AARO.<br/>**RU:** Снимок получен из военной системы США 2025 года, передан ФБР в AARO. | ✅ CORROBORATED | metadata description |
| 2 | A small, dark, circular object is in the upper-right quadrant.<br/>**RU:** Маленький, тёмный, круглый объект находится в верхнем правом квадранте. | ✅ CORROBORATED (AARO narrative) | metadata description |
| 3 | Background is an indistinct mountain range.<br/>**RU:** Фон — неразличимый горный хребет. | ✅ CORROBORATED | metadata description |
| 4 | HUD timestamp `12/31/99 18:11:06` is **not** the actual capture time (RTC unset).<br/>**RU:** HUD-таймстамп `12/31/99 18:11:06` **не** является фактическим временем съёмки (RTC не установлен). | ⚠ PARTIAL (relative ordering within burst is usable; absolute time is bogus) | transcript + metadata disclaimer |
| 5 | Sensor format: monochrome IR with central crosshair reticle, HUD `15  15` overlay.<br/>**RU:** Формат сенсора: монохромный ИК с центральной прицельной маркой, наложение HUD `15  15`. | ✅ CORROBORATED | metadata + transcript |

## Cross-references / Перекрёстные ссылки

**Within PURSUE corpus / В корпусе PURSUE:**
- Burst 1 sisters / Кадры-сёстры Серии 1: `FBI-IR-B01`, `FBI-IR-B03`, `FBI-IR-B04`, `FBI-IR-B06`, [`FBI-IR-B07`](FBI-IR-B07.md), `FBI-IR-B08`, `FBI-IR-B09`, `FBI-IR-B10`, `FBI-IR-B12`
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

- **Distinguishing feature / Отличительная черта:** No unique features beyond burst-time placement. / Нет уникальных черт помимо временного размещения в серии.
- **Burst-time placement / Временное размещение в серии:** Burst 1, t = +64s after B7 anchor (18:10:02 → 18:11:06).
