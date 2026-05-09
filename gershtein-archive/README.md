# Mikhail B. Gershtein Research Archive (1972–) / Архив Михаила Б. Герштейна (1972–)

A research archive of **Mikhail Borisovich Gershtein** (b. 27 July 1972), Russian ufologist, journalist, and writer; last chairman of the UFO Commission of the Russian Geographical Society's St-Petersburg branch. Coverage: UFO/UAP institutional history of the USSR/Russia, secret programs **«Сетка», «Галактика», НИТ-3, НИТ-54**, the NDE↔UFO link thesis, parallel-worlds / multiverse hypothesis, reincarnation themes, contactees, poltergeist, cryptozoology, religious readings of anomalous phenomena, and methodological critique of "academic ufology".

Полный исследовательский архив материалов **Михаила Борисовича Герштейна** (р. 27 июля 1972 г.), русского уфолога, журналиста и писателя; последнего председателя Уфологической комиссии РГО (Санкт-Петербургское отделение). Тематическое покрытие: институциональная история уфологии в СССР и России, секретные программы **«Сетка», «Галактика», НИТ-3, НИТ-54**, тезис о связи НЛО с околосмертным опытом, гипотеза параллельных миров / мультивселенной, тема реинкарнации, контактёры, полтергейст, криптозоология, религиозные интерпретации аномальных явлений и методологическая критика «академической уфологии».

**EN:** 62 Whisper-large-v3-turbo transcripts (2016–2026), 21 articles + 3 PDFs (incl. one self-authored 1 MB UAP-archive compendium), 10 book bibliography pages, 2 full book texts, complete Perplexity-dialog provenance with sha256 manifest. Master synthesis available: `analysis/MASTER_gershtein_claims.md` (v0.5.0).

**RU:** 62 транскрипции Whisper-large-v3-turbo (2016–2026), 21 статья и 3 PDF (включая 1 МБ собственный «Глобальный архив UAP-исследований» Герштейна), 10 книжных библиографических страниц, 2 полных книжных текста, полная провенанс-цепочка от Perplexity-диалога с манифестом sha256. Мастер-синтез доступен: `analysis/MASTER_gershtein_claims.md` (v0.5.0).

**Note on transcription pipeline / Примечание о транскрипции:** The corpus was originally to be transcribed via Groq's hosted `whisper-large-v3` API; the per-hour audio rate-limit (7200 sec ASPH) was hit on chunk 7 of the first file. The pipeline was migrated mid-flight to a self-hosted PC2 build of `voxtype` running `whisper-large-v3-turbo` on a Vulkan-accelerated NVIDIA RTX 3060 Laptop GPU; all 62 mp3 files transcribed successfully there with zero failures over a single 3-hour wall-clock pass.

Корпус изначально планировалось транскрибировать через хостинговый API Groq `whisper-large-v3`; почасовой лимит аудио (7200 сек ASPH) был исчерпан на 7-м чанке первого же файла. Пайплайн «на лету» был перенаправлен на самохостный сборку `voxtype` на втором ПК (модель `whisper-large-v3-turbo` через Vulkan на ноутбучной NVIDIA RTX 3060); все 62 mp3 транскрибированы без единого сбоя за один 3-часовой проход.

---

## QUICK NAVIGATION / БЫСТРАЯ НАВИГАЦИЯ

| Section / Раздел | Purpose / Назначение | File / Файл | Status / Статус |
|---|---|---|---|
| Main Technical Reference / Главный технический справочник | Unified bilingual claims synthesis / Единый двуязычный синтез утверждений | [`analysis/MASTER_gershtein_claims.md`](analysis/MASTER_gershtein_claims.md) | ✅ Available / Доступно |
| Appearances Catalog / Каталог выступлений | Chronological catalog 2016–2026 / Хронологический каталог 2016–2026 | [`catalog/interviews.md`](catalog/interviews.md) | ✅ Available / Доступно |
| Raw Transcripts / Сырые транскрипты | 62 Whisper-large-v3-turbo RU transcriptions / 62 транскрипта Whisper-large-v3-turbo (RU) | [`transcripts/`](transcripts/) | ✅ Available / Доступно |
| Per-Interview Analysis / Анализ по интервью | Per-transcript bilingual claim digests / Подробные двуязычные дайджесты по транскриптам | [`analysis/per-interview/`](analysis/per-interview/) | ✅ Available (35 files) / Доступно (35 файлов) |
| Topical Analysis / Тематический анализ | Same content grouped by topic / То же содержание по темам | [`analysis/topical/`](analysis/topical/) | ⏳ Reserved for v0.6.x / Зарезервировано для v0.6.x |
| Articles & PDFs / Статьи и PDF | Reviews of 21 articles + 3 PDFs / Ревью 21 статей и 3 PDF | [`analysis/articles/`](analysis/articles/) | ✅ Available (12 files) / Доступно (12 файлов) |
| Books Analysis / Анализ книг | Bibliography + 2 full-text book extracts / Библиография и 2 полнотекстовые книги | [`analysis/books/`](analysis/books/) | ✅ Available (4 files) / Доступно (4 файла) |
| External Research / Внешние исследования | Perplexity-dialog provenance + cross-archive links / Провенанс Perplexity-диалога и кросс-архивные связи | [`analysis/external-research/`](analysis/external-research/) | ⏳ Reserved for v0.6.x / Зарезервировано для v0.6.x |
| Visual Diagrams / Визуальные схемы | Mermaid sources + rendered SVG/PNG / Исходники Mermaid и SVG/PNG | [`diagrams/`](diagrams/) | ⏳ Reserved for v0.6.x / Зарезервировано для v0.6.x |
| QA Review / QA-ревью | Hallucination + cross-source audit / Аудит галлюцинаций и кросс-источников | `analysis/_map/` | ✅ Available (internal) / Доступно (внутренний рабочий каталог) |

---

## What's in this repo / Что внутри репозитория

```
gershtein-archive/
├── README.md                                ← you are here / вы здесь
├── manifest.json                            ← provenance, sha256, paths /
│                                              провенанс, sha256, пути
├── SUMMARY.md                               ← gather-time corpus summary /
│                                              исходное резюме корпуса
│
├── catalog/                                 ← meta-research /
│   │                                          мета-исследование
│   ├── interviews.md                        Chronological 62-row table /
│   │                                        Хронологическая таблица 62 источников
│   ├── youtube_catalog.json                 Per-video metadata from yt-dlp /
│   │                                        Метаданные по каждому видео из yt-dlp
│   ├── transcript_filename_map.json         Original yt-dlp slug → normalized name /
│   │                                        Соответствие оригинальных имён нормализованным
│   ├── classified_links.json                55 URLs typed (video / article / book / ...) /
│   │                                        55 URL по типу
│   ├── irrelevant_sources.md                5 filtered URLs + 1 unavailable + 2 paywalled /
│   │                                        5 отфильтрованных URL + 1 недоступный + 2 платных
│   └── perplexity_dialog/                   Verbatim Perplexity capture /
│                                            Дословный захват диалога Perplexity
│
├── transcripts/                             ← 62 normalized Whisper transcripts /
│   │                                          62 нормализованных транскрипта Whisper
│   ├── 01_Fenist-2016_aperitiv_Mikhail_Gershteyn_o_nauke_..._49s.txt
│   ├── ... (62 files, ~4 MB / 62 файла, ~4 МБ)
│   └── 62_21_03_2026_Gipotezy_ob_NLO_..._1h36.txt
│
├── videos/                                  ← only metadata (no mp4 in git) /
│   ├── INFO_JSON/                              только метаданные (mp4 не в git)
│   │   └── *.info.json (62)                 yt-dlp metadata per video
│   └── (raw mp4 lives on /mnt/data/uap-gershtein-raw/videos/)
│
├── articles/                                ← articles + PDFs /
│   ├── INDEX.md                                статьи и PDF
│   ├── sources/                             21 raw HTML/PDF /
│   │                                        21 сырых HTML/PDF
│   └── extracted_text/                      pre-extracted plain text for big PDFs/HTMLs /
│                                            предварительно извлечённый текст
│
├── books/                                   ← books /
│   ├── INDEX.md                                книги
│   ├── catalog_pages/                       8 publisher/library bibliography pages /
│   │                                        8 страниц каталогов издательств/библиотек
│   └── full_texts/                          2 actual book texts (ruslit + scribd) /
│                                            2 полнотекстовых книги (ruslit + scribd)
│
├── audio/                                   ← gitignored placeholder for 1.1 GB mp3 /
│                                              плейсхолдер; 1.1 ГБ mp3 не в git
├── raw/                                     ← gitignored placeholder for 24 GB mp4 /
│                                              плейсхолдер; 24 ГБ mp4 не в git
│
├── diagrams/                                ← visual components /
│   ├── *.mmd                                   визуальные компоненты
│   └── rendered/*.png|svg
│
└── analysis/                                ← extracted technical content (v0.5.0) /
    │                                          извлечённое содержание (v0.5.0)
    ├── MASTER_gershtein_claims.md           ⭐ Unified bilingual synthesis (§0–§13 + Appendices A/B) /
    │                                          ⭐ Единый двуязычный синтез (§0–§13 + Приложения A/B)
    │
    ├── per-interview/                       35 per-source / per-pair / per-triple bilingual digests /
    │                                          35 двуязычных дайджестов по источникам/парам/тройкам
    ├── articles/                            12 article + PDF reviews / 12 ревью статей и PDF
    ├── books/                               4 book reviews incl. bibliography master /
    │                                          4 ревью книг, включая библиографический справочник
    ├── topical/                             Reserved for v0.6.x / Зарезервировано для v0.6.x
    └── external-research/                   Reserved for v0.6.x / Зарезервировано для v0.6.x
```

Raw mp4 (24 GB) and mp3 (1.1 GB) are intentionally not committed; they live on `/mnt/data/uap-gershtein-raw/` and are referenced by absolute path in [`manifest.json`](manifest.json). See [`raw/README.md`](raw/README.md) and [`audio/README.md`](audio/README.md) for the pointer convention. This mirrors the `dubna-element-115-analysis/raw/` and `chernobrov-archive/audio/` pattern already used in this repository.

Сырые mp4 (24 ГБ) и mp3 (1.1 ГБ) преднамеренно не коммитятся; они живут на `/mnt/data/uap-gershtein-raw/` и отсылаются по абсолютному пути в [`manifest.json`](manifest.json). См. [`raw/README.md`](raw/README.md) и [`audio/README.md`](audio/README.md). Этот паттерн уже использован в `dubna-element-115-analysis/raw/` и `chernobrov-archive/audio/`.

---

## Start here / С чего начать

**EN — If you want raw transcripts:** → [`transcripts/`](transcripts/)
**RU — Если нужны сырые транскрипты:** → [`transcripts/`](transcripts/)

**EN — If you want the chronological catalog of all appearances:** → [`catalog/interviews.md`](catalog/interviews.md)
**RU — Если нужен хронологический каталог всех выступлений:** → [`catalog/interviews.md`](catalog/interviews.md)

**EN — If you want to know how the corpus was assembled:** → [`catalog/perplexity_dialog/`](catalog/perplexity_dialog/) + [`manifest.json`](manifest.json)
**RU — Если нужно понять, как был собран корпус:** → [`catalog/perplexity_dialog/`](catalog/perplexity_dialog/) + [`manifest.json`](manifest.json)

**EN — If you want only Gershtein's own writings:** → [`articles/sources/ufo-com.net__kolonka_*`](articles/sources/) + [`articles/sources/ufology-news.com__u_18672430_Ufology_News_Global_archive_UAP-study_and_UFO-ide.pdf`](articles/sources/) + [`books/full_texts/`](books/full_texts/)
**RU — Если нужны только собственные тексты Герштейна:** см. ту же ссылку.

---

## The corpus at a glance / Корпус с одного взгляда

| Category / Категория | Count / Кол-во | Size / Объём | Notes / Примечания |
|---|---|---|---|
| YouTube videos transcribed / Транскрибированные видео | 62 | ≈ 4 MB text / 24 GB mp4 / 1.1 GB mp3 | mp4/mp3 NOT in git / mp4/mp3 не в git |
| Articles + PDFs / Статьи и PDF | 21 | 36 MB | 18 HTML + 3 PDF |
| Books bibliography pages / Библиография | 8 | 0.8 MB | publisher/library catalog dumps |
| Books full text / Полные тексты книг | 2 | 1.9 MB | ruslit + scribd extracts |
| Filtered-out / Отфильтрованные источники | 5 | — | irrelevant URLs, see [`catalog/irrelevant_sources.md`](catalog/irrelevant_sources.md) |
| Unavailable on YouTube / Недоступно на YouTube | 1 | — | `nuiQhQ1Ap2s` |
| Paywalled book sources skipped / Платные книжные источники | 2 | — | `lib-dpr.ru`, `ast.ru` (kept stub HTML for traceability) |

---

## Source provenance / Происхождение источников

**EN:** This corpus was assembled in a single Perplexity Library dialog on 2026-05-07 (UTC). The user query was: «найди все интервью Михаила Герштейна, статьи связанные с UAP, НЛО, реинкорнацией сознаний и так далее». Perplexity returned 55 unique URLs from its Deep-Research mode. Of those: 17 YouTube videos + 1 VK video → downloaded; 19 article URLs + 3 PDF URLs + 1 reddit thread → downloaded; 9 book-catalog pages → downloaded; 5 unrelated URLs → filtered out (see [`catalog/irrelevant_sources.md`](catalog/irrelevant_sources.md)). 2 of the 17 YouTube URLs were playlists; expansion of those playlists raised the unique-video count from 17 to 63 (one of which, `nuiQhQ1Ap2s`, was unavailable at download time, leaving 62 transcribed videos).

**RU:** Корпус собран за один диалог Perplexity Library 2026-05-07 (UTC). Запрос пользователя: «найди все интервью Михаила Герштейна, статьи связанные с UAP, НЛО, реинкорнацией сознаний и так далее». Perplexity в режиме Deep Research вернул 55 уникальных URL: 17 ссылок на YouTube + 1 на VK; 19 статей; 3 PDF; 1 reddit-обсуждение; 9 книжных каталогов; 5 нерелевантных URL отфильтрованы. Две из YouTube-ссылок были плейлистами; их раскрытие расширило 17 уникальных видео-URL до 63, из которых одно (`nuiQhQ1Ap2s`) было недоступно — итого 62 транскрибированных видео.

Original Perplexity URL: <https://www.perplexity.ai/search/3533ca17-d2ab-4213-ad76-12cf61ee2f5f>

---

## Source rights / Авторские права на источники

**EN:** Raw `mp4` files and the auto-extracted `mp3` derivatives are downloaded from public YouTube via `yt-dlp` and kept locally only (not redistributed in this repo). The 62 transcripts are derivative works produced by Whisper-large-v3-turbo on those audio files; they are committed for analysis purposes. The 21 article HTMLs + 3 PDFs were downloaded from open-access pages on the named hosts; they are retained for traceability. If a source's licence forbids redistribution, the appropriate fallback is to drop the raw HTML and keep only the per-article markdown analysis under [`analysis/articles/`](analysis/articles/). Two paywalled book sources were skipped entirely; library/publisher catalog pages preserve the bibliographic metadata only.

**RU:** Сырые mp4 и автоизвлечённые mp3 скачаны с публичного YouTube через `yt-dlp` и сохраняются только локально (не публикуются в этом репозитории). 62 транскрипта — производные произведения от Whisper-large-v3-turbo, коммитятся для аналитических целей. 21 HTML-статья и 3 PDF скачаны со свободно-доступных страниц по указанным хостам и сохранены для отслеживаемости. Если лицензия источника запрещает редистрибуцию, корректный откат — удалить сырой HTML и оставить только markdown-анализ статьи в [`analysis/articles/`](analysis/articles/). Два платных книжных источника пропущены целиком; каталоги библиотек/издательств сохраняют только библиографические метаданные.

---

## Status / Статус

- **v0.5.0 — released 2026-05-09 / выпущено 2026-05-09.**
- **EN:** Full per-source analysis available: `MASTER_gershtein_claims.md` (§0–§13 + Appendices A/B), 35 per-interview/per-pair/per-triple bilingual digests, 12 article-and-PDF reviews, 4 book reviews including the unified bibliography master. ⚪ ADJACENT verdict label introduced for material from another researcher's framework. Cross-archive references to Chernobrov (§12.1) and Lazar (§12.2) included.
- **RU:** Полный анализ по источникам доступен: `MASTER_gershtein_claims.md` (§0–§13 + Приложения A/B), 35 двуязычных дайджестов по интервью/парам/тройкам, 12 ревью статей и PDF, 4 ревью книг, включая единый библиографический справочник. Введена метка ⚪ ADJACENT для материалов из чужой исследовательской рамки. Включены перекрёстные ссылки на архивы Черноброва (§12.1) и Лазара (§12.2).
- **v0.1.0 (2026-05-07):** Initial Perplexity ingest — raw data + catalog + manifest only. / Первичная загрузка с Perplexity — только сырые данные, каталог и манифест.
