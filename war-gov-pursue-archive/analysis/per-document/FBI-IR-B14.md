# FBI-IR-B14 — FBI Photo B14 / Фото ФБР B14

## Metadata / Метаданные

- **Source code / Код источника:** `FBI-IR-B14`
- **Agency / Агентство:** FBI (collected); imagery derived from a U.S. military system; submitted to AARO
- **Incident date / Дата инцидента:** Late 2025 (HUD timestamp `12/31/99 18:20:08` is **incorrect** — system date/time was not set; per metadata; OCR rendered `:` as `.`)
- **Location / Местоположение:** Western United States (specific area redacted)
- **Document kind / Тип документа:** PDF wrapping IR sensor JPG capture
- **Slug / Slug:** `fbi-photo-b14`
- **Raw file / Исходный файл:** `raw/pdf/fbi-photo-b14.pdf`
- **Transcript / Транскрипт:** `transcripts/fbi-photo-b14.txt` (HUD numeral `3` and bogus timestamp `12/31/99 18.20:08` only — image-only PDF)
- **Source URL / URL источника:** https://www.war.gov/medialink/ufo/release_1/fbi-photo-b14.pdf
- **Cluster context / Контекст кластера:** Part of 32-photo FBI Western US 2025 IR cluster; B14 is a **Burst 2** frame (~18:20:08), the *two-object* phase. Cluster-level analysis in `analysis/topical/region-fbi-western-us-2023-2025.md`.

## Summary / Резюме

Monochrome IR still showing **"two small, dark, circular objects"** near the center of the frame. Notably, B14 is the **only** B-frame that calls out a "**digital artifact or distortion … visible along the edge of the redaction box in the lower right quadrant**" — i.e., AARO is acknowledging visible redaction-edge artifacting. This is forensically important: the "redactions before submission" applied to imagery have a discernible boundary in B14.

**RU:** Монохромный ИК-снимок с **"двумя маленькими, тёмными, круглыми объектами"** вблизи центра кадра. Примечательно, что B14 — **единственный** кадр серии B, указывающий на "**цифровой артефакт или искажение … видимое вдоль края блока редактирования в нижнем правом квадранте**" — то есть AARO признаёт видимую артефактность края редактирования. Это имеет криминалистическое значение: "редактирование перед передачей", применённое к снимкам, имеет различимую границу в B14.

## Key claims / Ключевые заявления

| # | Claim / Заявление | Verdict / Вердикт | Source location / Расположение в источнике |
|---|-------|---------|-----------------|
| 1 | Image is a U.S. military system still from 2025, submitted by FBI to AARO.<br/>**RU:** Снимок получен из военной системы США 2025 года, передан ФБР в AARO. | ✅ CORROBORATED | metadata description |
| 2 | Two small, dark, circular objects are visible near frame center.<br/>**RU:** Два маленьких, тёмных, круглых объекта видны вблизи центра кадра. | ✅ CORROBORATED (AARO narrative) | metadata description |
| 3 | A digital artifact / distortion is visible along the edge of the **redaction box** in the lower-right quadrant.<br/>**RU:** Цифровой артефакт / искажение видно вдоль края **блока редактирования** в нижнем правом квадранте. | ✅ CORROBORATED (AARO explicitly acknowledges redaction-edge artifact — unique to B14) | metadata description |
| 4 | HUD timestamp `12/31/99 18:20:08` is **not** the actual capture time (RTC unset).<br/>**RU:** HUD-таймстамп `12/31/99 18:20:08` **не** является фактическим временем съёмки (RTC не установлен). | ⚠ PARTIAL (relative ordering within burst is usable; absolute time is bogus) | transcript + metadata disclaimer |
| 5 | B14 is the only B-frame whose narrative explicitly mentions a redaction box.<br/>**RU:** B14 — единственный кадр серии B, нарратив которого явно упоминает блок редактирования. | ✅ CORROBORATED (verified across B1–B24 metadata) | comparative metadata audit |

## Cross-references / Перекрёстные ссылки

**Within PURSUE corpus / В корпусе PURSUE:**
- Burst 2 sisters / Кадры-сёстры Серии 2: `FBI-IR-B13`, `FBI-IR-B15`, `FBI-IR-B16`, `FBI-IR-B17`, `FBI-IR-B18`, `FBI-IR-B19`, `FBI-IR-B20`, `FBI-IR-B21`, `FBI-IR-B22`, `FBI-IR-B23`, `FBI-IR-B24`
- [`FBI-IR-B07`](FBI-IR-B07.md) — Burst-1 helicopter anchor / якорный кадр Серии 1 с вертолётом
- [`FBI-USPER-302`](FBI-USPER-302.md) — companion FD-302 statement (orb "broke into multiple objects" — Burst 2 two-object cohort consistent with this narrative) / сопроводительное заявление FD-302 (шар "распался на несколько объектов" — когорта двух объектов Серии 2 согласуется с этим повествованием)
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

- **Distinguishing feature / Отличительная черта:** **Only B-frame to acknowledge a visible redaction-box edge artifact.** Suggests rectangular masking applied to obscure redacted content — locating the redaction may help triangulate what was masked (e.g., terrain reference, military installation, time-of-day badge). / **Единственный кадр серии B, признающий видимый артефакт края блока редактирования.** Предполагает прямоугольное маскирование, применённое для скрытия отредактированного содержимого — местонахождение редактирования может помочь триангулировать, что было замаскировано (напр., топографический ориентир, военный объект, метка времени суток).
- **Burst-time placement / Временное размещение в серии:** Burst 2, t ≈ +1m15s after B19 (18:18:53 → 18:20:08).
