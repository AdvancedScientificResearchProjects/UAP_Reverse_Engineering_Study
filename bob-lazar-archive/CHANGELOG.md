# Changelog / История изменений

All notable changes to the Bob Lazar Interview Archive.
Format: bilingual side-by-side (EN / RU) per ASRP v2.1.

Все значимые изменения архива интервью Боба Лазара.
Формат: двуязычный бок-о-бок (EN / RU) согласно ASRP v2.1.

---

## v1.1.0 — Batch 4 (Navigation & Polish) — 2026-04-14

**EN — Added:**
- `CHANGELOG.md` (this file) — bilingual version history per ASRP v2.1.
- README navigation polish: quick-nav anchors verified, transcript count reconciled (24 including S-4 doc `52_`).
- Final lint pass: dead-link scan, commit-history verification, file-count audit.

**EN — Changed:**
- README top-line summary brought in sync with post-batch-2 structure (bilingual merged master, deleted RU-only files).

**EN — Removed:**
- Stale references to deleted files (`MASTER_technical_claims_RU.md`, `RU_TRANSLATION_REVIEW.md`, `README.en.md`) reported for cleanup.

**RU — Добавлено:**
- `CHANGELOG.md` (этот файл) — двуязычная история версий согласно ASRP v2.1.
- Полировка навигации README: якоря быстрой навигации проверены, количество транскриптов согласовано (24 с учётом документалки S-4 `52_`).
- Финальный lint-проход: скан битых ссылок, проверка истории коммитов, аудит количества файлов.

**RU — Изменено:**
- Верхняя сводка README приведена в соответствие со структурой после batch 2 (объединённый двуязычный мастер, удалённые RU-файлы).

**RU — Удалено:**
- Устаревшие ссылки на удалённые файлы (`MASTER_technical_claims_RU.md`, `RU_TRANSLATION_REVIEW.md`, `README.en.md`) вынесены на очистку.

---

## v1.0.3 — Batch 3 (Visuals) — 2026-04-14

Commit: `b021beb` — `feat(lazar): batch 3 — visual components (Mermaid + SVG, ASRP v2.1)`

**EN — Added:**
- 5 Mermaid diagrams rendered to PNG: timeline of appearances, reactor flow, gravity modes, claim evolution, S-4 facility layout.
- 1 Mermaid PNG: Element 115 machining steps.
- 3 SVG technical schematics: Sport Model cutaway, top view, emitter detail.
- 3 SVG data-viz matrices: source credibility (24×5), numerical parameters, claim corroboration.
- 14 image insertions across `MASTER_technical_claims.md`, `README.md`, `catalog/interviews.md`.
- Per-agent reviews `REVIEW_3A_structural_mermaid.md`, `REVIEW_3B_technical_schematics.md`, `REVIEW_3C_data_viz.md` — all PASS.

**EN — Changed:**
- 1 count fix: 23 → 24 appearances after S-4 doc integration.

**RU — Добавлено:**
- 5 диаграмм Mermaid, отрендеренных в PNG: хронология выступлений, схема реактора, режимы гравитации, эволюция заявлений, план объекта S-4.
- 1 PNG Mermaid: этапы обработки Элемента 115.
- 3 технические SVG-схемы: разрез Sport Model, вид сверху, детализация эмиттера.
- 3 SVG-матрицы данных: доверие к источникам (24×5), числовые параметры, перекрёстное подтверждение заявлений.
- 14 вставок изображений в `MASTER_technical_claims.md`, `README.md`, `catalog/interviews.md`.
- Ревью по агентам `REVIEW_3A_structural_mermaid.md`, `REVIEW_3B_technical_schematics.md`, `REVIEW_3C_data_viz.md` — все PASS.

**RU — Изменено:**
- Исправлено 1 число: 23 → 24 выступления после интеграции документалки S-4.

---

## v1.0.2 — Batch 2 (Bilingual merge) — 2026-04-14

Commit: `cecefbf` — `feat(lazar): batch 2 — bilingual side-by-side merge (ASRP v2.1)`

**EN — Added:**
- Merged `MASTER_technical_claims.md` — EN + RU side-by-side (1446 lines).
- 12 per-interview + topical files translated to bilingual.
- 4 catalog files translated to bilingual: `interviews.md`, `research-1989-2005.md`, `research-2006-2018.md`, `research-2018-2026.md`.
- Merged `README.md` — EN + RU side-by-side.
- Per-agent reviews `REVIEW_2A_master_merge.md`, `REVIEW_2B_perinterview_topical.md`, `REVIEW_2C_catalog_readme.md` — all PASS.

**EN — Changed:**
- QA Gate 1 polish fixes applied: Nellis Range wording in §12.1 and §12.3.

**EN — Removed:**
- `MASTER_technical_claims_RU.md` (content merged into bilingual MASTER).
- `RU_TRANSLATION_REVIEW.md` (audit obsolete after merge).
- `README.en.md` (content merged into bilingual README).

**RU — Добавлено:**
- Объединённый `MASTER_technical_claims.md` — EN + RU бок-о-бок (1446 строк).
- 12 файлов per-interview + topical переведены в двуязычный формат.
- 4 файла каталога переведены в двуязычный формат: `interviews.md`, `research-1989-2005.md`, `research-2006-2018.md`, `research-2018-2026.md`.
- Объединённый `README.md` — EN + RU бок-о-бок.
- Ревью по агентам `REVIEW_2A_master_merge.md`, `REVIEW_2B_perinterview_topical.md`, `REVIEW_2C_catalog_readme.md` — все PASS.

**RU — Изменено:**
- Применены правки QA Gate 1: формулировка Nellis Range в §12.1 и §12.3.

**RU — Удалено:**
- `MASTER_technical_claims_RU.md` (содержимое объединено в двуязычный MASTER).
- `RU_TRANSLATION_REVIEW.md` (аудит устарел после объединения).
- `README.en.md` (содержимое объединено в двуязычный README).

---

## v1.0.1 — Batch 1 (Content enrichment) — 2026-04-14

Commit: `d6bee03` — `feat(lazar): batch 1 — content enrichment`

**EN — Added:**
- 5 new S-4 doc parameters: 3-inch tube, pewter antenna, 140–150 MHz, 10 ms recycle, 52'9" dimension.
- ASRP Media Element 115 / Dubna interview integrated (catalog + §1.11 of MASTER).
- §0.0 Key Numerical Parameters quick-reference table (34 rows).
- §12 Conclusions section (consistent / drifted / verifiable).
- April 13 chat-dump video (dailymotion `x8nd5fv`) added to catalog.

**EN — Changed:**
- QA Review Gate 1 PASS: 0 hallucinations, 5/5 verbatim quotes verified.

**RU — Добавлено:**
- 5 новых параметров из документалки S-4: 3-дюймовая трубка, оловянная антенна, 140–150 МГц, рецикл 10 мс, размер 52'9".
- Интегрировано интервью ASRP Media об Элементе 115 / Дубна (каталог + §1.11 MASTER).
- §0.0 — таблица быстрой справки по ключевым числовым параметрам (34 строки).
- §12 — раздел выводов (согласующиеся / дрейфующие / верифицируемые).
- Видео чат-дампа от 13 апреля (dailymotion `x8nd5fv`) добавлено в каталог.

**RU — Изменено:**
- QA Review Gate 1 — PASS: 0 галлюцинаций, 5/5 дословных цитат верифицированы.

---

## v1.0.0 — Initial commit — 2026-04-14

Commits: `58a160a` — `add: bob lazar interview archive (1989-2026)` + `d2c762d` — `add: S4 documentary (Vendittelli 2026) transcript + analysis`

**EN — Added:**
- 23 transcribed appearances (Whisper, timestamped) — KLAS 1989 → JRE #2479 2026.
- S-4 documentary (Vendittelli 2026) transcript: 1h54m, source code `S4DOC-26`.
- Per-interview and topical technical analysis files.
- Master technical claims synthesis (EN + RU parallel files at this stage).
- Initial QA reviews.
- MASTER updated with 70 new lines across 11 sections from the S-4 doc.

**RU — Добавлено:**
- 23 транскрибированных выступления (Whisper, с таймкодами) — KLAS 1989 → JRE #2479 2026.
- Транскрипт документалки S-4 (Vendittelli 2026): 1ч54м, код источника `S4DOC-26`.
- Файлы технического анализа по интервью и по темам.
- Мастер-синтез технических заявлений (EN + RU — параллельные файлы на этом этапе).
- Первичные QA-ревью.
- MASTER дополнен 70 новыми строками в 11 разделах из документалки S-4.
