# PURSUE Declassification Archive (war.gov, Release 01) / Архив рассекречивания PURSUE (war.gov, Релиз 01)

A research archive of the **2026-05-08 Department of War (DoW) PURSUE Release 01** — 161 declassified UAP records from DoW, FBI, NASA, and the Department of State, made public via [https://www.war.gov/UFO/](https://www.war.gov/UFO/) under the **Presidential Unsealing and Reporting System for UAP Encounters (PURSUE)**.

Исследовательский архив **первой транши PURSUE от Министерства войны США (Department of War, DoW)**, опубликованной 8 мая 2026 года: 161 рассекреченная запись по НЛО / НАЯ от DoW, ФБР, NASA и Госдепартамента, обнародованная на [https://www.war.gov/UFO/](https://www.war.gov/UFO/) в рамках программы **Presidential Unsealing and Reporting System for UAP Encounters (PURSUE)**.

**EN:** 121 PDFs + 28 mp4 videos + 14 jpg images, 158 per-document analytical cards, 7 topical syntheses, MASTER claims document (6362 lines, EN-primary with RU synopsis), and a QA review certifying citation fidelity, cross-link integrity, and 100% record coverage across the corpus.

**RU:** 121 PDF + 28 mp4-видео + 14 jpg-изображений, 158 аналитических карточек по документам, 7 тематических синтезов, MASTER-документ заявлений (6362 строки, основной язык EN с русским синопсисом), QA-обзор с подтверждением цитатной верности, целостности перекрёстных ссылок и 100% покрытия корпуса.

![Timeline of PURSUE Release 01 records 1944–2026 / Хронология записей PURSUE Релиз 01 1944–2026](diagrams/rendered/timeline.png)

*Chronological overview of PURSUE Release 01 records spanning 1944–2026. / Хронологический обзор записей PURSUE Релиз 01 за 1944–2026 годы.*

---

## QUICK NAVIGATION / БЫСТРАЯ НАВИГАЦИЯ

| Section / Раздел | Purpose / Назначение | File / Файл | Status / Статус |
|------------------|----------------------|-------------|-----------------|
| Master claims synthesis / Мастер-синтез заявлений | Cross-cluster topical synthesis with key claims index, RU synopsis, redaction patterns, coverage gaps / Междукластерный тематический синтез с индексом ключевых заявлений, русским синопсисом, паттернами редакций и пробелами покрытия | [`analysis/MASTER_pursue_claims.md`](analysis/MASTER_pursue_claims.md) | ✅ Available / Доступно |
| Document catalog / Каталог документов | Chronological table of all 161 records / Хронологическая таблица всех 161 записи | [`catalog/documents.md`](catalog/documents.md) | ✅ Available / Доступно |
| Source codes registry / Реестр кодов источников | Stable ID convention + verdict marker legend / Конвенция стабильных ID + легенда меток вердиктов | [`catalog/source_codes.md`](catalog/source_codes.md) | ✅ Available / Доступно |
| Document typology / Типология документов | 10 document-type clusters with descriptions / 10 кластеров типов документов с описаниями | [`catalog/typology.md`](catalog/typology.md) | ✅ Available / Доступно |
| Irrelevant / corrupted sources / Нерелевантные / повреждённые источники | Corrupted PDF + slug collisions + missing-PDF gaps / Повреждённый PDF + коллизии slug + пропущенные PDF | [`catalog/irrelevant_sources.md`](catalog/irrelevant_sources.md) | ✅ Available / Доступно |
| Per-document cards / Карточки по документам | 158 analytical cards (one per record + 1 bonus) / 158 аналитических карточек (по одной на запись + 1 бонус) | [`analysis/per-document/`](analysis/per-document/) | ✅ Available / Доступно |
| Topical syntheses / Тематические синтезы | 7 cross-cluster syntheses (era, region, modality, propulsion) / 7 междукластерных синтезов (эпоха, регион, модальность, двигательная установка) | [`analysis/topical/`](analysis/topical/) | ✅ Available / Доступно |
| Transcripts / Транскрипты | 162 text artifacts (118 PDFs via pdftotext, 28 video metadata, 14 image metadata + AARO descriptions) / 162 текстовых артефакта (118 PDF через pdftotext, 28 метаданных видео, 14 метаданных изображений + описания AARO) | [`transcripts/`](transcripts/) | ✅ Available / Доступно |
| Visual diagrams / Визуальные схемы | 8 Mermaid diagrams + rendered PNG (timeline, geo-map, verdict-distribution, Cabell propulsion taxonomy, agency record distribution, Sept 2023 ellipsoid case flow, Western US burst timeline, redaction pattern matrix) / 8 Mermaid-схем + рендеры PNG | [`diagrams/`](diagrams/) | ✅ Available / Доступно |
| Manifest / Манифест | sha256 + provenance for all raw files / sha256 + происхождение всех исходных файлов | [`manifest.json`](manifest.json) | ✅ Available / Доступно |

---

## What's in this repo / Что внутри репозитория

```
war-gov-pursue-archive/
├── README.md                              ← you are here / вы здесь
├── manifest.json                          ← sha256 + provenance for raw files
│
├── catalog/                               ← record indices and meta-research
│   │                                        индексы записей и мета-исследование
│   ├── documents.md                       Chronological 161-record table /
│   │                                      Хронологическая таблица 161 записи
│   ├── source_codes.md                    Stable ID convention + verdict marker legend /
│   │                                      Конвенция стабильных ID + легенда меток вердиктов
│   ├── typology.md                        10 document-type clusters /
│   │                                      10 кластеров типов документов
│   └── irrelevant_sources.md              Corrupted / collision / missing-PDF gaps /
│                                          Повреждённые / коллизионные / пропущенные PDF
│
├── transcripts/                           ← extracted text per record /
│   │                                        извлечённый текст по каждой записи
│   ├── {slug}.txt                         pdftotext extracts (118 native + OCR-augmented)
│   └── {slug}.metadata.txt                AARO description for video / image records (42)
│
├── raw/                                   ← gitignored: symlinks into _inbox (16+ GB)
│   │                                        в .gitignore: симлинки в _inbox
│   ├── pdf/                               (121 PDFs)
│   ├── video/                             (28 mp4)
│   ├── img/                               (14 jpg)
│   └── ocr/                               (67 OCR-augmented PDFs from EasyOCR pipeline)
│
├── analysis/                              ← per-record + cross-record analysis
│   │                                        анализ по записям + между записями
│   ├── MASTER_pursue_claims.md            ⭐ Master synthesis (6362 lines, EN-primary + RU §0.RU)
│   ├── per-document/                      158 cards (one per source code + 1 bonus)
│   │   ├── DOW-D{n}.md                    DoW MISREP / D-series cards
│   │   ├── DOW-PR{n}.md                   DoW unresolved PR-video cards
│   │   ├── FBI-62HQ-S{n}.md / Sr{n}.md    FBI Case 62-HQ-83894 cards
│   │   ├── FBI-IR-A{nn}.md / B{nn}.md     FBI Western US IR-photo cards
│   │   ├── FBI-ELLIPSE-*.md               Sept 2023 bronze ellipsoid case
│   │   ├── FBI-USPER-302.md               Late-2025 federal-LE 302
│   │   ├── NASA-D{n}.md / VM6.md          NASA spaceflight cards
│   │   ├── DOS-*.md                       Department of State cables
│   │   ├── COMETA-1999.md                 Only civilian / foreign source
│   │   └── DOW-{historical}.md            1944-1949 historical records
│   └── topical/                           7 cross-cluster syntheses
│       ├── era-1944-1968-historical.md
│       ├── era-1965-1974-nasa-spaceflight.md
│       ├── modality-state-cables-1952-2004.md
│       ├── propulsion-tech-claims.md
│       ├── region-centcom-2013-2026.md
│       ├── region-fbi-western-us-2023-2025.md
│       └── region-indopacom-2020-2026.md
│
└── diagrams/                              ← visual components
    │                                        визуальные компоненты
    ├── timeline.mmd                       1944-2026 chronology /
    │                                      Хронология 1944-2026
    ├── geo_map.mmd                        Regional clusters by AOR /
    │                                      Региональные кластеры по зонам ответственности
    ├── verdict_distribution.mmd           Pie chart of 1522 claim verdicts /
    │                                      Круговая диаграмма 1522 вердиктов заявлений
    ├── cabell_propulsion_taxonomy_       75-year propulsion-taxonomy stagnation
    │   1949_to_aaro_2026.mmd              (1949 Cabell Memo #4 → AARO MISREP 2026) /
    │                                      75-летняя стагнация таксономии двигателей
    ├── agency_record_distribution.mmd     161 records by agency + DoW/FBI/NASA
    │                                      sub-clusters / Распределение по агентствам
    ├── sept_2023_ellipsoid_case_flow.mmd  FBI ELLIPSE released-vs-withheld map /
    │                                      Карта опубликовано vs скрыто
    ├── western_us_2023_2025_burst_       FBI-IR B-series two ~3-min bursts at
    │   timeline.mmd                       18:10 / 18:19 / Два всплеска ~3 мин
    ├── redaction_pattern_matrix.mmd       6 redaction-pattern mechanisms with
    │                                      recoverability tags / Паттерны редакций
    └── rendered/*.png                     Pre-rendered PNG outputs /
                                            Предварительно отрендеренные PNG
```

---

## Start here / С чего начать

**EN — If you want the synthesis-level findings:** → [`analysis/MASTER_pursue_claims.md`](analysis/MASTER_pursue_claims.md) (start with §0.0 key claims index for a 35-claim summary, or §0.RU for the Russian synopsis)

**RU — Если нужны выводы синтез-уровня:** → [`analysis/MASTER_pursue_claims.md`](analysis/MASTER_pursue_claims.md) (начните с §0.0 индекса ключевых заявлений — 35 заявлений, или §0.RU для русского синопсиса)

**EN — If you want a specific document:** → look up its source code in [`catalog/source_codes.md`](catalog/source_codes.md), then read [`analysis/per-document/{CODE}.md`](analysis/per-document/) (every record has its own card).

**RU — Если нужен конкретный документ:** → найдите его код источника в [`catalog/source_codes.md`](catalog/source_codes.md), затем читайте [`analysis/per-document/{CODE}.md`](analysis/per-document/) (у каждой записи своя карточка).

**EN — If you want the chronological catalog:** → [`catalog/documents.md`](catalog/documents.md) (all 161 records, sorted by incident date).

**RU — Если нужен хронологический каталог:** → [`catalog/documents.md`](catalog/documents.md) (все 161 записи, по дате инцидента).

---

## The corpus at a glance / Корпус с одного взгляда

### By cluster / По кластерам

| Cluster / Кластер | Records / Записей | Cards / Карточек | Era / Эпоха |
|---|---:|---:|---|
| NASA spaceflight / NASA космические полёты | 14 | 13 + 1 bonus | 1965–1974 |
| FBI Case 62-HQ-83894 (master) / Дело ФБР 62-HQ-83894 | 18 | 18 | 1947–1976 |
| FBI Western US IR (A-series jpg) / FBI Western US IR (серия A jpg) | 8 | 8 | 2025 |
| FBI Western US IR (B-series PDF) / FBI Western US IR (серия B PDF) | 24 | 24 | 2025 |
| FBI ELLIPSE (Sept 2023 bronze ellipsoid) / FBI ELLIPSE (бронзовый эллипсоид сент 2023) | 4 | 4 | 2023 |
| FBI 100-DE legacy / FBI 100-DE наследие | 2 | 2 | 1949–1950 |
| FBI USPER-302 (late 2025) / FBI USPER-302 (конец 2025) | 1 | 1 | 2025 |
| DoW MISREP D-series / DoW MISREP D-серия | 45 | 42 | 2013–2026 |
| DoW unresolved PR-videos / DoW нерешённые PR-видео | 28 | 28 | 2020–2025 |
| DoW Incident Summaries / DoW сводки инцидентов | 3 | 3 | 1944–1948 |
| DoW historical (pre-1956) / DoW исторические (до 1956) | 6 | 6 | 1944–1949 |
| Department of State cables / Кабели Госдепартамента | 7 | 7 | 1952–2004 |
| COMETA 1999 (civilian / foreign) / COMETA 1999 (гражданский / иностранный) | 1 | 1 | 1999 |
| **Totals / Итого** | **161** | **158** | **1944–2026** |

### By verdict marker (across all 1522 per-document claims) / По меткам вердиктов (по всем 1522 заявлениям)

| Marker / Метка | Meaning / Значение | Count / Количество | Share / Доля |
|---|---|---:|---:|
| ✅ CORROBORATED | Verbatim primary source or ≥2-source corroboration / Дословный первичный источник или ≥2-источника | 1136 | 74.6% |
| ⚠ PARTIAL | Qualified / inferential / partial coverage / Условное / выводное / частичное покрытие | 161 | 10.6% |
| ⬜ UNRESOLVED | AARO status pending; no closeout / Статус AARO не определён; без закрытия | 108 | 7.1% |
| ⬛ REDACTED | Material redaction or page missing / Существенная редакция или пропущенная страница | 70 | 4.6% |
| 🟧 ANALYTICAL FLAG | AARO metadata inconsistency OR plausible analyst interpretation / Несоответствие метаданных AARO ИЛИ обоснованная аналитическая интерпретация | 24 | 1.6% |
| ❌ EXPLAINED | Mundane explanation documented in source / Обыденное объяснение зафиксировано в источнике | 23 | 1.5% |

See [`diagrams/rendered/verdict_distribution.png`](diagrams/rendered/verdict_distribution.png) for the pie chart.

---

## Pipeline notes / Замечания по конвейеру

**EN:**
- **Source acquisition:** [https://www.war.gov/UFO/](https://www.war.gov/UFO/) via Zen browser through the Assistant Bridge WebExtension on 2026-05-08.
- **OCR:** EasyOCR (PyTorch CUDA on RTX 3060) + reportlab invisible text + pikepdf composition; threshold 0.30, DPI 200. 67/68 image-only PDFs successfully OCR'd; 1 corrupted-at-source (`DOW-FOO-1944` — `/Pages tree contains no /Kids array`, identical-failure across qpdf / gs / pikepdf / pdf2image).
- **Text extraction:** `pdftotext -layout` over the OCR'd PDF (or native text PDF where present). Sample QA against transcripts gave 95% verbatim-PASS rate over 38 sampled citations.
- **Manifest:** sha256 over all raw files (230 files including OCR-augmented derivatives). 4 sha256-duplicate groups documented in `catalog/irrelevant_sources.md`.
- **Diagrams:** Mermaid (CLI v11.14.0) → SVG rendered via puppeteer + cached Chrome 131.
- **Analytical pipeline:** built bottom-up — 158 per-document cards first, then 7 topical syntheses, then the 8-section MASTER as a layered synthesis. QA closed with 3 independent audits (citation/verdict, cross-link integrity, coverage stats).

**RU:**
- **Получение источников:** [https://www.war.gov/UFO/](https://www.war.gov/UFO/) через Zen-браузер с расширением Assistant Bridge WebExtension, 8 мая 2026.
- **OCR:** EasyOCR (PyTorch CUDA на RTX 3060) + reportlab невидимый текст + композиция pikepdf; порог 0.30, DPI 200. Успешно OCR'нуто 67/68 PDF без текстового слоя; 1 повреждён в источнике (`DOW-FOO-1944` — `/Pages tree contains no /Kids array`, одинаковый сбой qpdf / gs / pikepdf / pdf2image).
- **Извлечение текста:** `pdftotext -layout` поверх OCR-PDF (или нативного PDF с текстом). Выборочный QA-аудит на 38 цитатах: 95% дословных PASS.
- **Манифест:** sha256 по всем исходным файлам (230 файлов включая OCR-производные). 4 группы sha256-дубликатов задокументированы в `catalog/irrelevant_sources.md`.
- **Диаграммы:** Mermaid (CLI v11.14.0) → SVG-рендер через puppeteer + кэшированный Chrome 131.
- **Аналитический конвейер:** построен снизу вверх — сначала 158 карточек по документам, затем 7 тематических синтезов, затем 8-секционный MASTER как наслоённый синтез. Закрыт тремя независимыми аудитами (цитаты/вердикты, целостность перекрёстных ссылок, статистика покрытия).

---

## Verdict marker convention / Конвенция меток вердиктов

The 🟧 marker has a **dual-meaning convention** across the archive (documented in [`catalog/source_codes.md`](catalog/source_codes.md)):

1. **AARO METADATA INCONSISTENCY** — when the AARO-supplied metadata conflicts with the document content (e.g., the PR28-labeled-as-D7 / actually-matches-D25 mismatch).
2. **PLAUSIBLE INTERPRETATION** — when an analyst-side hypothesis (typically a mundane explanation) is offered as an interpretive overlay rather than as a factual claim.

Маркер 🟧 имеет **двойное значение** по всему архиву (см. [`catalog/source_codes.md`](catalog/source_codes.md)):

1. **НЕСОГЛАСОВАННОСТЬ МЕТАДАННЫХ AARO** — когда поставленные AARO метаданные противоречат содержанию документа (напр., PR28 размечен как D7, но содержание соответствует D25).
2. **ОБОСНОВАННАЯ АНАЛИТИЧЕСКАЯ ИНТЕРПРЕТАЦИЯ** — когда аналитическая гипотеза (обычно обыденное объяснение) предлагается как интерпретирующий слой, а не как утверждение факта.

In every case where 🟧 is applied, the surrounding text makes the intended sense explicit / Во всех случаях применения 🟧 окружающий текст делает интенцию явной.

---

## Scope and limitations / Объём и ограничения

### What's in scope / Что входит в объём

**EN:**
- All 161 records from PURSUE Release 01 (DoW, FBI, NASA, State).
- Per-document analytical cards with claim-level verdict markers grounded in transcript line numbers.
- Cluster-level topical syntheses by era, region, and modality.
- A MASTER claims document organizing the entire corpus.
- Cross-archive references (pointers only — no claim imports from sibling archives).

**RU:**
- Все 161 записи из PURSUE Релиз 01 (DoW, ФБР, NASA, Госдеп).
- Аналитические карточки по документам с метками вердиктов на уровне заявлений, привязанные к номерам строк транскриптов.
- Кластерные тематические синтезы по эпохам, регионам и модальностям.
- MASTER-документ заявлений, организующий весь корпус.
- Перекрёстные ссылки на смежные архивы (только указатели — без переноса заявлений).

### What's not in scope / Что не входит в объём

**EN:**
- Future PURSUE tranches (Release 02+ will arrive in subsequent updates).
- Claims from sibling ASRP archives (bob-lazar, chernobrov, gershtein, dubna) — even where they overlap with PURSUE content, claims are not imported, only cross-referenced.
- Independent third-party investigation of the underlying events.
- Skeptic / debunker analysis (this archive faithfully extracts and verdict-tags what is in the released documents; truth-evaluation belongs to the reader).

**RU:**
- Будущие транши PURSUE (Релиз 02+ появятся в последующих обновлениях).
- Заявления из смежных ASRP-архивов (bob-lazar, chernobrov, gershtein, dubna) — даже там, где они пересекаются с PURSUE, заявления не импортируются, а только cross-ссылаются.
- Независимое стороннее расследование самих событий.
- Скептический / разоблачительный анализ (архив добросовестно извлекает и маркирует вердиктами то, что есть в опубликованных документах; оценка истинности — за читателем).

### Known gaps / Известные пробелы

**EN:**
- `DOW-FOO-1944` — corrupted at source. Recovery path: web.archive.org or future re-download.
- `DOS-1952-MEMO`, `DOS-TBI-2001`, `DOS-MEX-2003`, `DOS-TKM-2004` — 4 of 7 DOS PDFs missing from the release. Gap-cards exist; recovery would require a future PURSUE re-release or FOIA.
- Sr4 + Sr5 of FBI-ELLIPSE — page 1 systematically absent (only page 2 of 2 released for both corroborating witnesses).
- Roswell, Mogul, Lazar S-4, Grusch testimony, Project Blue Book, Robertson Panel, Condon Report, Tic Tac, GoFast, Gimbal, recovered material / non-human biologics — completely absent from this tranche.

**RU:**
- `DOW-FOO-1944` — повреждён в источнике. Путь восстановления: web.archive.org или повторная загрузка позднее.
- `DOS-1952-MEMO`, `DOS-TBI-2001`, `DOS-MEX-2003`, `DOS-TKM-2004` — 4 из 7 PDF Госдепа отсутствуют в релизе. Карточки-пробелы существуют; восстановление потребует будущего ре-релиза PURSUE или запроса FOIA.
- Sr4 + Sr5 FBI-ELLIPSE — страница 1 систематически отсутствует (опубликована только страница 2 из 2 для обоих подкрепляющих свидетелей).
- Розуэлл, Mogul, Лазар S-4, показания Груша, Project Blue Book, Robertson Panel, отчёт Condon, Tic Tac, GoFast, Gimbal, восстановленный материал / нечеловеческая биология — полностью отсутствуют в этой транше.

See [`analysis/MASTER_pursue_claims.md`](analysis/MASTER_pursue_claims.md) §9 (Coverage gaps) for the full inventory and analysis.

---

## Related archives / Связанные архивы

- **EN:** Cross-archive synthesis: [`../analysis/cross-archive-synthesis.md`](../analysis/cross-archive-synthesis.md) — Theme 4 (federal disclosure lineage) registers PURSUE in the broader ASRP corpus.
- **RU:** Кросс-архивный синтез: [`../analysis/cross-archive-synthesis.md`](../analysis/cross-archive-synthesis.md) — Тема 4 (линия федерального раскрытия) регистрирует PURSUE в более широком корпусе ASRP.

Cross-archive intersections (pointers only) / Пересечения с другими архивами (только указатели):

- [`../bob-lazar-archive/`](../bob-lazar-archive/) — propulsion / element 115 thread overlap with FBI 62-HQ-83894 propulsion-related serials and the 1996 Vandenberg booster-failure record. / Пересечение по теме двигательной установки / элемента 115 с сериями FBI 62-HQ-83894 по двигательной установке и записью о сбое ускорителя Vandenberg 1996.
- [`../chernobrov-archive/`](../chernobrov-archive/) — Soviet/Russian-era multi-witness aerial cases that contextualize PNG 1985 and Holland-Sweden 1948. / Советские/российские многосвидетельские воздушные случаи, контекстуализирующие PNG 1985 и Нидерланды-Швеция 1948.
- [`../gershtein-archive/`](../gershtein-archive/) — methodology for atmospheric / propagation alternative explanations relevant to high-altitude contrails and NASA spaceflight optical phenomena. / Методология альтернативных объяснений атмосферного / распространительного характера, применимая к высотным инверсионным следам и оптическим явлениям космических полётов NASA.
- [`../dubna-element-115-analysis/`](../dubna-element-115-analysis/) — element-115 propulsion thread overlap with FBI 62-HQ-83894. / Пересечение темы двигательной установки элемента-115 с FBI 62-HQ-83894.

---

## Citation / Цитирование

**EN:** If you use this archive in research, please link back to the repository. This is a working research archive. Corrections and additions welcome via pull request.

**RU:** Если вы используете этот архив в исследовании, пожалуйста, дайте ссылку на репозиторий. Это рабочий исследовательский архив. Исправления и дополнения приветствуются через pull request.

---

## ASRP ECOSYSTEM / ЭКОСИСТЕМА ASRP

<div align="center">

### Parent Repository / Родительский Репозиторий

</div>

| Repository / Репозиторий | Direction / Направление | Link / Ссылка |
|-------------------------|------------------------|---------------|
| **UAP Reverse Engineering Study / Исследование по Реверс-Инжинирингу НАЯ** | UAP fragment analysis (AI + archival + ECP) / Анализ фрагмента НАЯ (ИИ + архив + КП) | [View / Просмотр](https://github.com/AdvancedScientificResearchProjects/UAP_Reverse_Engineering_Study) |

---

<div align="center">

**ASRP RESEARCH STANDARD v2.1**

**Organization / Организация:** Advanced Scientific Research Projects (ASRP)

</div>

---

> **Support / Поддержать:** if this work is valuable to you — https://asrp.tech/en/patrons
