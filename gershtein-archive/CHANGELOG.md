# Changelog / История изменений

All notable changes to the Gershtein research archive.
Format: bilingual side-by-side (EN / RU) per ASRP v2.1.

Все значимые изменения архива исследований Михаила Б. Герштейна.
Формат: двуязычный бок-о-бок (EN / RU) согласно ASRP v2.1.

---

## v0.1.0 — Initial Perplexity ingest — 2026-05-07

**EN — Added:**
- 62 normalized Whisper-large-v3-turbo transcripts under `transcripts/`. Filenames are `NN_TitleSlug_duration.txt` sorted chronologically by YouTube upload date (01 = 2016-09-25 «Фенист-2016: аперитив», 62 = 2026-03-25 «Гипотезы об НЛО и аномальных явлениях»). Every file carries a 3-line header: `# <title>` / `# Source: <webpage_url>` / `# Transcribed: 2026-05-07 (Whisper-large-v3-turbo)`. Mapping from original yt-dlp slugs is preserved in `catalog/transcript_filename_map.json`.
- `catalog/interviews.md` — chronological 62-row catalog table.
- `catalog/youtube_catalog.json` — per-video yt-dlp metadata (id, title, uploader, upload_date, duration, webpage_url, view_count, description, tags).
- `catalog/transcript_filename_map.json` — name-mapping from original yt-dlp slugs to repo-style filenames (62 entries).
- `catalog/classified_links.json` — verbatim copy of the gather-time URL classifier output (55 URLs typed as video / article / pdf / book_catalog / irrelevant / web_thread).
- `catalog/irrelevant_sources.md` — table of the 5 filtered URLs (yamaha.com, artsmoscow.ru, ru.wikipedia.org Sakharov, tiktok.com, polpred.com) with reasons; plus notes on 1 unavailable YouTube video and 2 paywalled book sources.
- `catalog/perplexity_dialog/` — verbatim capture of the source Perplexity dialog (`answer.txt`, `answer.json`, `links_tab.json`, `README.md`).
- `videos/INFO_JSON/` — 62 yt-dlp `*.info.json` files (one per transcribed video).
- `articles/sources/` — 21 articles (18 HTML + 3 PDF) downloaded from open-access pages.
- `articles/extracted_text/` — pre-extracted plain-text versions of the 3 PDFs and the 2 large HTMLs (>300 KB) that downstream analysis agents will consume.
- `articles/INDEX.md` — bibliographic table with sha256 + size for each of the 21 articles.
- `books/catalog_pages/` — 8 publisher/library bibliography pages (livelib, bookvoed, ast.ru, klex, elib.nlb.by, lib-dpr, ufo-com.net/books).
- `books/full_texts/` — 2 full book texts (ruslit.net «Тайны НЛО и пришельцев» preview, ru.scribd.com «Уфология через взаимодействие человека и НЛО»). Each kept as both raw HTML and pre-extracted `.txt`.
- `books/INDEX.md` — table with kind/host/sha256/size for each of the 10 book items.
- `manifest.json` — repo-side provenance manifest with rewritten paths, transcription pipeline notes, and pointers to the 24 GB mp4 / 1.1 GB mp3 on `/mnt/data/uap-gershtein-raw/`.
- `SUMMARY.md` — copy of the gather-time corpus summary.
- `raw/README.md` and `audio/README.md` — placeholder explainers pointing at `/mnt/data/uap-gershtein-raw/`.
- `analysis/` skeleton folders (`per-interview/`, `topical/`, `articles/`, `books/`, `external-research/`) — empty pending v0.5.x batched-agent pass.
- Repo-root `.gitignore` carve-outs for `gershtein-archive/raw/videos/`, `gershtein-archive/audio/`, `gershtein-archive/raw/*.mp4`, `*.mp3`, `*.webp`, `gershtein-archive/*.py`, `*.sh`, `*.log`, `gershtein-archive/.venv/`, `gershtein-archive/wav_tmp/`, `gershtein-archive/audio_chunks/` — mirrors the `chernobrov-archive` and `dubna-element-115-analysis` carve-out style.
- New git branch `gershtein-archive` (matches the `chernobrov-archive` and `bob-lazar-archive` per-person branch convention).

**EN — Pipeline notes:**
- Source: a single Perplexity Library dialog (2026-05-07) — query «найди все интервью Михаила Герштейна, статьи связанные с UAP, НЛО, реинкорнацией сознаний и так далее». 55 unique URLs returned by Perplexity in Deep-Research mode.
- Video download: `yt-dlp 2026.03.17`, profile `bv*[height<=720]+ba/b[height<=720]/best`, mp4 merge.
- Audio extraction: `ffmpeg libmp3lame q=7`, mono, 16 kHz (Whisper-friendly).
- Transcription primary attempt: Groq hosted `whisper-large-v3` API → hit ASPH per-hour rate-limit on chunk 7 of file 1.
- Transcription actual: `voxtype` on a second PC running `whisper-large-v3-turbo` on a Vulkan-accelerated NVIDIA RTX 3060 Laptop GPU. 62/62 successful, 0 failures, single ~3 h wall-clock pass.
- Two paywalled book sources (`lib-dpr.ru`, `ast.ru`) were skipped after retries (lib-dpr returned a 23 KB stub, ast.ru returned 404 then a search-page fallback). The 23 KB and 163 KB stubs are kept under `books/catalog_pages/` for traceability only.

**EN — Known-issues recorded for downstream agent passes:**
- Whisper occasionally produced silence-loop hallucinations (e.g. transcript `26_*` in early v0.1.0 → `na8SJVuRHd4` had a phrase repeated 4×). The `catalog/transcript_filename_map.json` is preserved so post-processing can match each transcript back to its `info.json` for `start/end` timestamp anchoring during claim extraction.
- `magazines.gorky.media` (642 KB HTML) extracted only 1.7 KB of plain text — likely a soft login wall. The downstream analysis agent for that source must rely on the Perplexity-summarised claim and either skip or escalate.
- `roii.ru` (20 MB academic almanac) and `ivanovo.ac.ru` (11 MB sci-collection) are mostly unrelated to Gershtein; a filtering agent must run first to reduce the input before content-analysis agents touch them.

---

**RU — Добавлено:**
- 62 нормализованных транскрипта Whisper-large-v3-turbo в `transcripts/`. Имена файлов — `NN_TitleSlug_duration.txt`, отсортированы хронологически по дате загрузки на YouTube (01 = 2016-09-25 «Фенист-2016: аперитив», 62 = 2026-03-25 «Гипотезы об НЛО и аномальных явлениях»). Каждый файл содержит 3-строчный заголовок: `# <title>` / `# Source: <webpage_url>` / `# Transcribed: 2026-05-07 (Whisper-large-v3-turbo)`. Соответствие оригинальным yt-dlp-слагам сохранено в `catalog/transcript_filename_map.json`.
- `catalog/interviews.md` — хронологическая таблица из 62 строк.
- `catalog/youtube_catalog.json` — yt-dlp-метаданные по каждому видео (id, title, uploader, upload_date, duration, webpage_url, view_count, description, tags).
- `catalog/transcript_filename_map.json` — соответствие исходных yt-dlp-имён нормализованным именам (62 записи).
- `catalog/classified_links.json` — дословная копия классифицированного списка URL (55 ссылок по типам).
- `catalog/irrelevant_sources.md` — таблица 5 отфильтрованных URL с причинами; примечания о 1 недоступном видео и 2 платных книжных источниках.
- `catalog/perplexity_dialog/` — дословный захват исходного диалога Perplexity.
- `videos/INFO_JSON/` — 62 yt-dlp `*.info.json` (по одному на транскрибированное видео).
- `articles/sources/` — 21 статья (18 HTML + 3 PDF) с открытым доступом.
- `articles/extracted_text/` — предварительно извлечённый plain-text для 3 PDF и 2 крупных HTML.
- `articles/INDEX.md` — библиографическая таблица с sha256 и размером по каждой статье.
- `books/catalog_pages/` — 8 страниц каталогов издательств/библиотек.
- `books/full_texts/` — 2 полных книжных текста (ruslit.net «Тайны НЛО и пришельцев» и ru.scribd.com «Уфология через взаимодействие человека и НЛО»).
- `books/INDEX.md` — таблица из 10 книжных позиций.
- `manifest.json` — репо-провенанс с переписанными путями, описанием транскрипционного пайплайна и указателями на /mnt/data/.
- `SUMMARY.md` — копия исходного резюме корпуса.
- `raw/README.md` и `audio/README.md` — плейсхолдеры с указателями на /mnt/data/.
- Скелет `analysis/` (`per-interview/`, `topical/`, `articles/`, `books/`, `external-research/`) — пустые папки в ожидании прогона батчей агентов в v0.5.x.
- Расширения корневого `.gitignore` для `gershtein-archive/raw/videos/`, `audio/`, `*.mp4`, `*.mp3`, `*.webp`, `*.py`, `*.sh`, `*.log` — повторяет конвенцию `chernobrov-archive` и `dubna-element-115-analysis`.
- Новая git-ветка `gershtein-archive` (соответствует именованию `chernobrov-archive` и `bob-lazar-archive`).

**RU — Заметки по пайплайну:**
- Источник: один диалог Perplexity Library (2026-05-07), запрос: «найди все интервью Михаила Герштейна, статьи связанные с UAP, НЛО, реинкорнацией сознаний и так далее». 55 уникальных URL от Perplexity в режиме Deep Research.
- Скачивание видео: `yt-dlp 2026.03.17`, профиль `bv*[height<=720]+ba/b[height<=720]/best`, склейка в mp4.
- Извлечение аудио: `ffmpeg libmp3lame q=7`, mono, 16 kHz (под Whisper).
- Первая попытка транскрипции: hosted-API Groq `whisper-large-v3` → лимит ASPH (часовое аудио) исчерпан на 7-м чанке 1-го файла.
- Реальная транскрипция: `voxtype` на втором ПК с моделью `whisper-large-v3-turbo` через Vulkan на ноутбучной NVIDIA RTX 3060. 62/62 успешно, 0 сбоев, один проход ~3 часа.

**RU — Известные особенности для последующих агентских проходов:**
- Whisper иногда давал silence-loop-галлюцинации (напр., в транскрипте `na8SJVuRHd4` фраза повторена 4 раза). Сохранён `catalog/transcript_filename_map.json`, чтобы пост-обработка могла сопоставить каждый транскрипт с его `info.json` для дальнейшей привязки таймстемпов.
- `magazines.gorky.media` (642 КБ HTML) дал только 1.7 КБ plain-text — вероятно soft-login wall. Агенту по этому источнику нужно опираться на резюме Perplexity или эскалировать.
- `roii.ru` (20 МБ академический альманах) и `ivanovo.ac.ru` (11 МБ научный сборник) на 80%+ не имеют отношения к Герштейну; перед content-анализом обязателен фильтрующий проход.
