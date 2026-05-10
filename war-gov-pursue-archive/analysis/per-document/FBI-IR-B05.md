# FBI-IR-B05 — FBI Photo B5 / Фото ФБР B5

## Metadata / Метаданные

- **Source code / Код источника:** `FBI-IR-B05`
- **Agency / Агентство:** FBI (collected); imagery derived from a U.S. military system; submitted to AARO
- **Incident date / Дата инцидента:** Late 2025 (no HUD timestamp recovered from OCR — only the `15   15` HUD numerals)
- **Location / Местоположение:** Western United States (specific area redacted)
- **Document kind / Тип документа:** PDF wrapping IR sensor JPG capture
- **Slug / Slug:** `fbi-photo-b5`
- **Raw file / Исходный файл:** `raw/pdf/fbi-photo-b5.pdf`
- **Transcript / Транскрипт:** `transcripts/fbi-photo-b5.txt` (only `15   15` HUD numerals — **timestamp not OCR-recovered**, image-only PDF)
- **Source URL / URL источника:** https://www.war.gov/medialink/ufo/release_1/fbi-photo-b5.pdf
- **Cluster context / Контекст кластера:** Part of 32-photo FBI Western US 2025 IR cluster. B5 is the **second** B-frame (alongside B2) where OCR did not recover a HUD timestamp. Burst placement must be inferred from the description, which puts B5 in **Burst 1**. Cluster-level analysis in `analysis/topical/region-fbi-western-us-2023-2025.md`.

## Summary / Резюме

Monochrome IR still in which "**no distinct objects are clearly visible** within the central area of the frame," against an "indistinct formation, possibly a mountain range." B5 is the **only** B-frame whose AARO description explicitly states no distinct object is visible — every other frame in the B-series describes at least one dark object. This makes B5 either a tracking-loss frame, a misidentified frame at the start/end of acquisition, or an empty-search frame inserted for completeness.

**RU:** Монохромный ИК-снимок, в котором "**в центральной области кадра не видно чётко различимых объектов**" на фоне "неразличимого образования, возможно горного хребта". B5 — **единственный** кадр серии B, описание AARO которого явно заявляет, что чётко различимых объектов не видно — каждый другой кадр серии B описывает хотя бы один тёмный объект. Это делает B5 либо кадром потери сопровождения, либо ошибочно идентифицированным кадром в начале/конце захвата цели, либо пустым поисковым кадром, включённым для полноты.

## Key claims / Ключевые заявления

| # | Claim / Заявление | Verdict / Вердикт | Source location / Расположение в источнике |
|---|-------|---------|-----------------|
| 1 | Image is a U.S. military system still from 2025, submitted by FBI to AARO.<br/>**RU:** Снимок получен из военной системы США 2025 года, передан ФБР в AARO. | ✅ CORROBORATED | metadata description |
| 2 | **No distinct objects clearly visible** within the central frame area.<br/>**RU:** **В центральной области кадра чётко различимых объектов не видно.** | ✅ CORROBORATED (AARO narrative — unique to B5 across the entire B-series) | metadata description |
| 3 | Background is an indistinct formation, possibly a mountain range.<br/>**RU:** Фон — неразличимое образование, возможно горный хребет. | ✅ CORROBORATED | metadata description |
| 4 | HUD timestamp not recoverable from OCR (only `15   15` numerals).<br/>**RU:** HUD-таймстамп не восстановим из OCR (только цифры `15   15`). | ⚠ PARTIAL (timestamp likely present in raw image but OCR-missed) | transcript |
| 5 | B5 belongs to Burst 1 by background-class inference (mountain range, no two-object structure).<br/>**RU:** B5 относится к Серии 1 по выводу класса фона (горный хребет, без структуры двух объектов). | ⬜ UNRESOLVED (no direct timestamp evidence; could plausibly bracket either burst) | comparative analysis |
| 6 | B5 is the only B-frame where AARO declares no object visible.<br/>**RU:** B5 — единственный кадр серии B, где AARO заявляет об отсутствии видимых объектов. | ✅ CORROBORATED (verified across B1–B24 metadata) | comparative metadata audit |

## Cross-references / Перекрёстные ссылки

**Within PURSUE corpus / В корпусе PURSUE:**
- `FBI-IR-B02` — the other timestamp-missing B-frame / другой кадр серии B без таймстампа
- Burst 1 sisters (object-bearing) / Кадры-сёстры Серии 1 (с объектами): `FBI-IR-B01`, `FBI-IR-B03`, `FBI-IR-B04`, `FBI-IR-B06`, [`FBI-IR-B07`](FBI-IR-B07.md), `FBI-IR-B08`, `FBI-IR-B09`, `FBI-IR-B10`, `FBI-IR-B11`, `FBI-IR-B12`
- [`FBI-IR-B07`](FBI-IR-B07.md) — only frame with helicopter visible; anchors USPER-302 cross-link / единственный кадр с видимым вертолётом; якорь перекрёстной ссылки USPER-302
- [`FBI-USPER-302`](FBI-USPER-302.md) — companion FD-302 statement (mentions object that "broke into multiple objects" and outran the helicopter — B5 could plausibly be the moment the target was lost) / сопроводительное заявление FD-302 (упоминает объект, который "распался на несколько объектов" и обогнал вертолёт — B5 правдоподобно может быть моментом потери цели)
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

- **Distinguishing feature / Отличительная черта:** **Empty frame — no object reported by AARO.** Unique within the entire 24-frame B-series. Plausible explanations: (a) tracking-loss moment, (b) operator pre-acquisition frame released for chronological completeness, (c) the moment the "super-hot orb" of USPER-302 disappeared from view. / **Пустой кадр — AARO не сообщает об объекте.** Уникален во всей 24-кадровой серии B. Правдоподобные объяснения: (a) момент потери сопровождения, (b) кадр предзахвата оператора, включённый для хронологической полноты, (c) момент исчезновения "супер-горячего шара" USPER-302 из поля зрения.
- **Burst-time placement / Временное размещение в серии:** Burst 1 (inferred from background class), exact ordering unknown. Worth manual visual inspection of the raw PDF to recover the timestamp.
