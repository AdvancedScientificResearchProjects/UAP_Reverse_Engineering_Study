# PURSUE Release 01 — Irrelevant / problematic sources / Нерелевантные / проблемные источники PURSUE Релиз 01

Records with data quality, integrity, or recoverability issues. Includes corrupted source artifacts, content duplicates with URL-encoding variants, and metadata anomalies.

**RU:** Записи с проблемами качества данных, целостности или восстановимости. Включает повреждённые исходные артефакты, дубликаты содержимого с вариантами URL-кодирования и аномалии метаданных.

## 1. Corrupted at source — irrecoverable / Повреждённые в источнике — невосстановимые

### `DOW-FOO-1944` — Foo-fighters / 415th Night Fighter Squadron

**File / Файл:** `raw/pdf/331_120752_numeric_files_1944_E2_80_931945_37153_german_armament_equipment_documents.pdf`
**Size / Размер:** 2,734,064 bytes
**Topic / Тема:** SHAEF cables, "night phenomena (foofighters)", flak rockets, 415th Night Fighter Squadron observations (1944–1945) / Кабели SHAEF, «ночные феномены (фу-файтеры)», зенитные ракеты, наблюдения 415-й эскадрильи ночных истребителей (1944–1945)

**Issue / Проблема:** PDF root `/Pages` tree contains no `/Kids` array; xref table broken; not openable by any tested PDF engine. / Корень PDF дерева `/Pages` не содержит массива `/Kids`; таблица xref нарушена; не открывается ни одним протестированным PDF-движком.

**Recovery attempts (all failed) / Попытки восстановления (все неудачные):**
- `qpdf --check` → `root of pages tree has no /Kids array`
- `gs -o repaired.pdf -sDEVICE=pdfwrite ...` → `Couldn't initialise file. No pages will be processed`
- `pikepdf.open(...)` → `PdfError: root of pages tree has no /Kids array`
- `pdf2image.convert_from_path(...)` → `Unable to get page count`

**Diagnosis / Диагноз:** Corruption is in the source artifact published by war.gov, not in the local copy (sha256 verified by re-download with identical hash). This is the **earliest chronological document in the entire release** and the only document of this period.

**RU:** Повреждение в исходном артефакте, опубликованном war.gov, а не в локальной копии (sha256 верифицирован повторной загрузкой с идентичным хэшем). Это **хронологически наиболее ранний документ во всём релизе** и единственный документ этого периода.

**Status / Статус:** Excluded from `transcripts/` extraction and `analysis/per-document/`. Documented as a high-priority "open question" in `analysis/MASTER_pursue_claims.md` Appendix A.

**RU:** Исключён из извлечения `transcripts/` и `analysis/per-document/`. Задокументирован как «открытый вопрос» высокого приоритета в Приложении A `analysis/MASTER_pursue_claims.md`.

**Next actions / Следующие действия:**
1. Re-attempt download from war.gov in 2–4 weeks (xref may be regenerated server-side). / Повторить загрузку с war.gov через 2–4 недели (xref может быть перегенерирован на стороне сервера).
2. Check `web.archive.org` Wayback for an earlier capture of this asset URL. / Проверить `web.archive.org` Wayback на предмет более ранней копии этого URL актива.
3. If unrecoverable, consider FOIA request for replacement copy from FBI Vault or NARA. / Если невосстановим, рассмотреть запрос FOIA на замену из FBI Vault или NARA.

---

## 2. Sha256-identical duplicates (same file content, different URL-encoded names) / Sha256-идентичные дубликаты (одинаковое содержимое файла, разные URL-кодированные имена)

The portal serves identical assets at multiple URL-encoded paths. The `manifest.json` records all variants for provenance, but only one copy in each group needs analysis.

**RU:** Портал обслуживает идентичные активы по нескольким URL-кодированным путям. `manifest.json` записывает все варианты для происхождения, но для анализа нужна только одна копия в каждой группе.

### Group 1 — `DOW-1947-AMC-MEMO` (sha256 `85d659d6b2208610...`) / Группа 1

- `raw/pdf/18_100754_ general 1946-7_vol_2.pdf` (space variant / вариант с пробелом)
- `raw/pdf/18_100754__20general_201946-7_vol_2.pdf` (URL-encoded `%20` variant / вариант URL-кодирования `%20`)

**Canonical / Канонический:** prefer `18_100754_ general 1946-7_vol_2.pdf` (space-decoded / декодированный пробел).

### Group 2 — `DOS-1963-EOP-NASA` (sha256 `aba3ec3b8ef02403...`) / Группа 2

- `raw/pdf/59_214434_sp_16_7.18.1963.pdf`
- `raw/pdf/59_214434_sp_16_[7.18.1963].pdf`

**Canonical / Канонический:** `59_214434_sp_16_[7.18.1963].pdf` (matches metadata title / совпадает с заголовком метаданных).

### Group 3 — `DOW-D23` (sha256 `ea1cd5296143f378...`) / Группа 3

- `raw/pdf/dow-uap-d23-mission-report-united-arab-emirates-october-2023(1).pdf`
- `raw/pdf/dow-uap-d23-mission-report-united-arab-emirates-october-2023.pdf`

**Canonical / Канонический:** `…october-2023.pdf` (without `(1)` suffix / без суффикса `(1)`).

### Group 4 — `DOW-D32` (sha256 `fd4deb1e48fcfa7f...`) / Группа 4

- `raw/pdf/dow-uap-d32-mission-report,-syria-october-2024(1).pdf`
- `raw/pdf/dow-uap-d32-mission-report,-syria-october-2024(2).pdf`
- `raw/pdf/dow-uap-d32-mission-report,-syria-october-2024.pdf`

**Canonical / Канонический:** `…october-2024.pdf` (without numeric suffix / без числового суффикса).

**Net unique files in `raw/pdf/` / Нетто уникальных файлов в `raw/pdf/`:** 121 − 5 = 116 unique PDFs by content / 116 уникальных PDF по содержанию.

---

## 3. Metadata-side slug discrepancies / Расхождения slug на стороне метаданных

The portal scrape recorded 158 metadata `.md` files for 161 INDEX records. The 3-record gap is explained by URL-encoding duplicates above (where `(1)` / `(2)` variants did not generate separate metadata cards because the slug normalization collapsed them).

**RU:** Скрапинг портала зафиксировал 158 файлов метаданных `.md` для 161 записи INDEX. Разрыв в 3 записи объясняется дубликатами URL-кодирования выше (где варианты `(1)` / `(2)` не создали отдельных карточек метаданных, поскольку нормализация slug их свернула).

**Assessment / Оценка:** No data loss in metadata. The 158 files cover all 161 unique-by-content records. / Потерь данных в метаданных нет. 158 файлов охватывают все 161 запись, уникальную по содержанию.

---

## 4. Records with `Incident Date: N/A` / Записи с `Incident Date: N/A`

Many FBI 62-HQ-83894 sections, NASA images, and the COMETA report have no incident date because the document's primary purpose is summary/aggregate rather than single-event reporting. These sort to the end of `catalog/documents.md` and are not flagged as anomalies.

**RU:** Многие разделы FBI 62-HQ-83894, снимки NASA и отчёт COMETA не имеют даты инцидента, поскольку основная цель документа — сводка/агрегат, а не отчёт об одном событии. Они сортируются в конец `catalog/documents.md` и не помечаются как аномалии.

---

## 5. Records with degraded OCR / Записи с деградировавшим OCR

### Pattern: image-only PDFs (no actionable text) / Паттерн: PDF только с изображениями (нет пригодного текста)

OCR was attempted but produces minimal/noise text because the PDF is fundamentally an image with no embedded textual content (e.g., FBI-IR-A* and B* photos wrapping JPG frames in PDF containers).

**RU:** OCR попытался обработать, но производит минимальный/шумовой текст, поскольку PDF является принципиально изображением без встроенного текстового содержимого (напр., фото FBI-IR-A* и B*, оборачивающие JPG-кадры в PDF-контейнеры).

**Examples / Примеры:**
- `FBI-IR-B04` (`fbi-photo-b4.pdf`) — OCR output: `15 / 12/31/99 18:12:16 / 15` (only the camera HUD timestamp / только временна́я метка HUD камеры)
- Most `FBI-IR-A0*` and `B0*` similar / Большинство `FBI-IR-A0*` и `B0*` аналогично

**Handling / Обработка:** These records are valuable as imagery; their `transcripts/{slug}.txt` contains the brief HUD text plus the metadata description, sufficient for grep but not for claim extraction. / Эти записи ценны как изображения; их `transcripts/{slug}.txt` содержит краткий текст HUD плюс описание метаданных, достаточно для grep, но не для извлечения заявлений.

---

## 6. Inferred from corpus, not explicit anomalies / Выведенные из корпуса, не явные аномалии

### Heavy redaction (per release policy) / Тяжёлые редакции (согласно политике выпуска)

Redactions are explicitly applied to / Редакции явно применяются к:
- Witness identities / Личностям свидетелей
- Government facility locations / Местоположениям государственных объектов
- Military site details unrelated to UAP / Военным деталям, не связанным с НАЯ

Per release policy, **phenomenology descriptions are not redacted / описания феноменологии не редактируются**. Verification against the OCR'd corpus has been spot-checked across the per-document cards. / Верификация относительно OCR-корпуса выборочно проверена в карточках по документам.

### Inferred missing companions / Выведенные отсутствующие сопутствующие

Some PR-series videos arrive without companion MISREP PDFs (e.g., several PR23–PR47 are video-only). Whether the missing reports are unredacted-text documents withheld for next-tranche release, or simply do not exist as separate items, is unclear from this release.

**RU:** Некоторые видео серии PR поступают без сопутствующих PDF рапортов MISREP (напр., несколько PR23–PR47 только видео). Являются ли отсутствующие отчёты нередактированными текстовыми документами, удержанными для выпуска следующей транши, или просто не существуют как отдельные элементы — из данного релиза неясно.

---

## 7. PDFs absent from raw/ (download failures during scrape) / PDF, отсутствующие в raw/ (сбои загрузки при скрапинге)

The following records appear in `data/INDEX.md` and have metadata in `_inbox/.../data/metadata/` but their PDF files are **not present** in `raw/pdf/`. These were apparently dropped by the original Zen browser scrape and need re-download from war.gov.

**RU:** Следующие записи присутствуют в `data/INDEX.md` и имеют метаданные в `_inbox/.../data/metadata/`, но их PDF-файлы **отсутствуют** в `raw/pdf/`. По всей видимости, они были пропущены при исходном скрапинге Zen-браузером и требуют повторной загрузки с war.gov.

| Source code / Код источника | Slug (in metadata) / Slug (в метаданных) | Status / Статус | Notes / Примечания |
|-------------|-------------------|--------|-------|
| `DOS-1952-MEMO` | `59_64634_711.5612[7-2852` | PDF missing / PDF отсутствует | 1952 State Department memo on UFO reports + Air Force opinions; metadata describes it but no file present in raw/pdf/. The transcript at `transcripts/59_214434_sp_16_*.txt` is a misattribution — both `59_214434_*` files contain the **1963** Hunter EOP/NASC memo, not the 1952 memo. / Меморандум Госдепа 1952 года об отчётах НЛО + мнениях ВВС; метаданные описывают, но файл в raw/pdf/ отсутствует. Транскрипт `transcripts/59_214434_sp_16_*.txt` — неверная атрибуция: оба файла `59_214434_*` содержат меморандум Hunter EOP/NASC **1963** года, а не 1952. |
| `DOS-TBI-2001` | `state_department_uap_cable_3,_tbilisi,_georgia,_october_30,_2001` | PDF missing / PDF отсутствует | No `dos-uap-d3-cable-3-tbilisi-*.pdf` in raw/pdf/. / В raw/pdf/ нет `dos-uap-d3-cable-3-tbilisi-*.pdf`. |
| `DOS-MEX-2003` | `state_department_uap_cable_5,_mexico,_september_16,_2003` | PDF missing / PDF отсутствует | No `dos-uap-d5-cable-5-mexico-*.pdf` in raw/pdf/. Notable: cable allegedly contains Mexican Congress UAP testimony / alien corpses claim. / В raw/pdf/ нет `dos-uap-d5-cable-5-mexico-*.pdf`. Примечательно: кабель предположительно содержит показания Конгресса Мексики по НАЯ / утверждение о внеземных телах. |
| `DOS-TKM-2004` | `state_department_uap_cable_4,_ashgabat,_turkmenistan,_november_5,_2004` | PDF missing / PDF отсутствует | No `dos-uap-d4-cable-4-turkmenistan-*.pdf` in raw/pdf/. / В raw/pdf/ нет `dos-uap-d4-cable-4-turkmenistan-*.pdf`. |

**Recovery plan / План восстановления:** Re-attempt download of these 4 PDFs from war.gov directly. The slug-collision with the 1963 EOP/NASC memo (which DOES have a PDF) suggests the scrape may have stopped after first match on shared filename prefix.

**RU:** Повторить загрузку этих 4 PDF непосредственно с war.gov. Коллизия slug с меморандумом EOP/NASC 1963 (у которого PDF ЕСТЬ) предполагает, что скрапер мог остановиться после первого совпадения по общему префиксу имени файла.

**Per-document cards for these files** are written as **gap-cards** (in `analysis/per-document/`) — they document the metadata but explicitly note the absent source and refuse to fabricate claims.

**RU:** **Карточки по документам для этих файлов** написаны как **gap-карточки** (в `analysis/per-document/`) — они документируют метаданные, но явно отмечают отсутствующий источник и отказываются фабриковать заявления.

## Summary table / Сводная таблица

| Category / Категория | Count / Количество | Action / Действие |
|----------|------:|--------|
| Corrupted at source / Повреждённые в источнике | 1 | Re-download attempt scheduled / Запланирована попытка повторной загрузки |
| Duplicate by sha256 / Дубликат по sha256 | 5 extra files (4 groups) / 5 дополнительных файлов (4 группы) | Mark canonical, retain provenance / Обозначить канонический, сохранить происхождение |
| Metadata gap (URL-encoding) / Пробел метаданных (URL-кодирование) | 3 | Resolved (no loss) / Решено (без потерь) |
| Image-only PDFs (OCR noise) / PDF только с изображениями (OCR-шум) | ~32 (FBI-IR cluster / кластер FBI-IR) | Imagery primary; metadata in transcripts / Изображение первично; метаданные в транскриптах |
| Heavy redaction / Тяжёлые редакции | corpus-wide / по всему корпусу | QA verification task / Задача верификации QA |
| **PDFs absent from raw / PDF, отсутствующие в raw** | **4 DOS records / 4 записи DOS** | Re-download from war.gov / Повторная загрузка с war.gov |

**Net analyzable records / Нетто анализируемых записей:** 156 / 161 (1 corrupted foo-fighters + 4 absent DOS PDFs excluded / 1 повреждённый foo-fighters + 4 отсутствующих PDF DOS исключены).
