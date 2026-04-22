# Changelog / История изменений

All notable changes to the Chernobrov / Kosmopoisk research archive.
Format: bilingual side-by-side (EN / RU) per ASRP v2.1.

Все значимые изменения архива исследований Черноброва / «Космопоиск».
Формат: двуязычный бок-о-бок (EN / RU) согласно ASRP v2.1.

---

## v0.5.3 — SLEDY-55 Ч2 ingest + per-interview 06→06_20 merge — 2026-04-20

**EN — Added:**
- `transcripts/20_SlediPutesh_Ch2_2h55.txt` — fresh Whisper pass of Part 2 of the 21–22 October 2015 broadcast on Народное Славянское Радио (2h55m, 2397 segments, 260 KB; YouTube `Ptq5z7AQn2I`). Part 1 was the pre-existing `06_SlediPutesh_2h55.txt` (itself ending on a cliff-hanger photo-method teaser at `[02:55:16]`). Ч2 opens at `[00:01:07]` with the host bridge «Итак, переходим к следующему пункту заявленного нашего общения, это разговор о фотографиях» and delivers the full photo-evidence block + Q&A that Ч1 had deferred.
- New source code `SLEDY-55` for the merged 5h51m broadcast; split into `SLEDY-55-C1` (Ч1 = transcript 06) and `SLEDY-55-C2` (Ч2 = transcript 20) chunk sub-codes for citation granularity. Listed in MASTER §0.3.
- `analysis/per-interview/06_20_sledy_puteshestvennikov.md` — existing 06 file renamed; Ч2 content appended as sections §18–§28 (≈ 350 new lines, bilingual RU-first). New sections cover: photo-anomaly thesis & methodology (§18); Bralorne Canadian 1930s-photograph case-study with NTV crew (§19 — 9 subsections); Hawking 2012 time-traveller party (§20); 2015 Medveditskaya hronokapsula field experiment + Dmitry covert-call result (§21); 1920s Rabfak-student case (§22); Domodedovo 21.12.1998 + Archangelsk VHS backlog + "relative from the future" anecdote (§23); Q&A technical claims incl. 3-dimensions-of-time + January-2016-mobile-МВ-crowdfunding + Belimov/Volzhskaya cross-ref to `B-PV01` (§24); Ч2-only names/books (§25–§26); Ч2 absences (§27); position in corpus (§28).
- 3 new `§0.0` MASTER numerical-params items (83–85): (83) Bralorne Canadian 1930s-photograph investigation; (84) 2015 Medveditskaya hronokapsula field experiment; (85) Domodedovo airport luggage-locker drop 21 December 1998.
- 3 new MASTER `§6.5` timeline rows: July 2015 hronokapsula; 21–22 October 2015 `SLEDY-55` broadcast; January-2016-announced mobile-chassis МВ crowdfunding.
- New MASTER `§11.16` clarifying that the "deliberate-bait photograph" framing (Ч2 §19.7) is single-source to `SLEDY-55-C2` and not corroborated in any book chapter in the current archive corpus; Ч2 generalised claim «NLO каждый раз при новом включении новой установки» noted as single-source extension of the 2002 Medveditskaya Lovondatr-7 sequence (MASTER §8.3 / `B-HRON03` §32.4).

**EN — Changed:**
- MASTER header Scope line: «20 transcripts covering 19 distinct lectures» → «21 transcripts covering 19 distinct lectures», with explicit note on both source-merges (08+20_Zigelevsky = ZIG-17; 06+20_SlediPutesh_Ch2 = SLEDY-55). v0.5.3 summary added.
- MASTER `§0.3` Video-lectures table: new `SLEDY-55` row describing the 5h51m single broadcast and its C1/C2 chunk split; row explicitly notes Ч2 ASR stuck-loop pathology (~2 min of unrecoverable segments between `[01:10]` and `[01:13]`). Transcript count updated to 21.
- `README.md`: transcript count «20» → «21»; both QUICK NAVIGATION Raw Transcripts row and Corpus Statistics YouTube-lectures row reflect the new dual-merge structure; per-interview analyses count 8 → 9 files; per-interview dir listing shows `06_20_sledy_puteshestvennikov.md` (renamed from `06_sledy_puteshestvennikov.md`); Transcripts code table gains `SLEDY-55` row; Status header v0.5.3.
- Per-interview 06 file renamed in place: `06_sledy_puteshestvennikov.md` → `06_20_sledy_puteshestvennikov.md`. Header rewritten to dual-transcript form (SLEDY-55-C1 + SLEDY-55-C2, 351 min total, Source code split). Existing §1–§17 Ч1 content preserved unchanged except §15 gets a bridge-note to §18 continuation.

**Top 5 novel findings from Ч2** (per analysis, single-source to `SLEDY-55-C2` unless noted):
1. Chernobrov's **"deliberate-bait photograph"** trace-mechanic (§19.7) — an original inversion of the enforcement-failure model; no book-chapter corroboration found (§11.16).
2. **Bralorne Canadian 1930s-photograph investigation** — NTV federal-channel field crew, museum-director-reveals-to-Russians-only, Russian-language inscriptions, non-gold-mine site, censored broadcast (§19 + §0.0 item 83).
3. **2015 Medveditskaya hronokapsula experiment** + Dmitry-covert-call with unpredicted-class in-camp response (§21 + §0.0 item 84).
4. **Domodedovo 21 December 1998 luggage-locker drop** — date-pinned case-anchor for an artefact Chernobrov retains but has never published (§23.1 + §0.0 item 85).
5. **January 2016 mobile-chassis МВ crowdfunding announcement** — architecture shift from fixed matryoshka to vehicle-portable (§24.3 + §6.5 timeline).

**RU — Добавлено:**
- `transcripts/20_SlediPutesh_Ch2_2h55.txt` — свежий прогон Whisper Части 2 эфира 21–22 октября 2015 г. на Народном Славянском Радио (2h55m, 2397 сегментов, 260 КБ; YouTube `Ptq5z7AQn2I`). Часть 1 — ранее существовавший `06_SlediPutesh_2h55.txt`, оборванный на клиффхэнгере о фотографиях в `[02:55:16]`. Ч2 открывается в `[00:01:07]` связкой ведущего «Итак, переходим к следующему пункту заявленного нашего общения, это разговор о фотографиях» и содержит полный блок о фотоуликах + Q&A.
- Новый код источника `SLEDY-55` для объединённого 5h51m эфира, разделённый на `SLEDY-55-C1` (Ч1 = транскрипт 06) и `SLEDY-55-C2` (Ч2 = транскрипт 20). Указан в MASTER §0.3.
- `analysis/per-interview/06_20_sledy_puteshestvennikov.md` — существующий файл 06 переименован; контент Ч2 добавлен разделами §18–§28 (~350 новых строк, двуязычно RU-first). Новые разделы: тезис и методология фотоулик (§18); **Брэлорнская канадская фотография 1930-х** + съёмочная группа НТВ (§19 — 9 подразделов); вечеринка Хокинга для путешественников во времени 2012 (§20); **хронокапсула Медведицкой гряды июль 2015** + эксперимент Дмитрия (§21); случай рабфаковца 1920-х (§22); **Домодедово 21.12.1998** + ВХС-архив Архангельска + анекдот «родственница из будущего» (§23); технические заявления Q&A включая три измерения времени + **мобильная МВ-кампания на январь 2016** + кросс-реф к Белимов/Волжская регрессивно-гипнотическая группа в `B-PV01` (§24); имена/книги, упомянутые только в Ч2 (§25–§26); отсутствия в Ч2 (§27); место в корпусе (§28).
- 3 новых пункта §0.0 MASTER (83–85): (83) Брэлорнская канадская фотография 1930-х; (84) хронокапсула Медведицкой гряды июль 2015; (85) камера хранения Домодедово 21.12.1998.
- 3 новые строки хронологии MASTER §6.5: июль 2015 хронокапсула; 21–22 октября 2015 эфир `SLEDY-55`; объявленная январь-2016 мобильная МВ-кампания.
- Новый §11.16 MASTER: уточнение, что концепт «намеренно-приманочной фотографии» (§19.7 Ч2) — single-source, не подтверждён ни одной главой книги в текущем корпусе; обобщение Ч2 «НЛО при каждом новом включении новой установки» — single-source-расширение 2002 г. последовательности Ловондатр-7 на МГ.

**RU — Изменено:**
- Строка области MASTER: «20 транскриптов, покрывающих 19 различных лекций» → «21 транскрипт, покрывающий 19 различных лекций» с явным указанием обоих мержей источников. Добавлена сводка v0.5.3.
- Таблица видеодокладов MASTER §0.3: новая строка `SLEDY-55`, описывающая 5h51m эфир и его разбиение C1/C2; явно отмечена патология стак-лупов Whisper Части 2 (~2 мин нечитаемых сегментов между `[01:10]` и `[01:13]`). Общее число транскриптов обновлено до 21.
- `README.md`: число транскриптов «20» → «21»; обе строки QUICK NAVIGATION и Corpus Statistics отражают новую структуру двойного мержа; число per-interview-анализов 8 → 9; листинг директории показывает `06_20_sledy_puteshestvennikov.md`; таблица кодов транскриптов получает строку `SLEDY-55`; заголовок Status v0.5.3.
- Файл per-interview 06 переименован на месте: `06_sledy_puteshestvennikov.md` → `06_20_sledy_puteshestvennikov.md`. Заголовок переписан в двухтранскриптную форму. Существующее содержание §1–§17 Ч1 сохранено без изменений, за исключением того, что §15 получает переходную ссылку на продолжение §18.

**Топ-5 новых находок из Ч2** (single-source к `SLEDY-55-C2`, если не отмечено иначе):
1. Концепт **«намеренно-приманочной фотографии»** Черноброва (§19.7) — оригинальная инверсия модели «trace-через-неудачу-протокола»; корреляция в книжном корпусе отсутствует (§11.16).
2. **Расследование Брэлорнской канадской фотографии 1930-х** — съёмочная группа НТВ, директор музея раскрывает материалы только русским, надписи на русском языке, место «не золотая шахта», вырезание из эфира (§19 + §0.0 п. 83).
3. **Эксперимент с хронокапсулой Медведицкой гряды 2015** + скрытый 30-минутный отклик Дмитрия с непредсказуемой внутрилагерной реакцией (§21 + §0.0 п. 84).
4. **Камера хранения Домодедово 21 декабря 1998** — кейс-якорь с датой, артефакт сохранён, но никогда не публиковался (§23.1 + §0.0 п. 85).
5. **Январь 2016: объявление о краудфандинге мобильной МВ** — архитектурный сдвиг от стационарной матрёшки к транспортной (§24.3 + §6.5 хронология).

---

## v0.5.2 — Final-Lecture Anchor — 2026-04-19

**EN — Added:**
- `transcripts/20_ZigelevskyChteniya_49_3zvNLO_2017-03-25_22min.txt` — fresh Groq Whisper-large-v3 pass of the 49th Zigelevsky Readings lecture (Moscow, 25 March 2017, 22 min; YouTube `4YGeR1KsXy0`).
- `analysis/per-interview/20_zigelevsky_2017_3star.md` (~36 KB, 9 focus sections) — dedicated ZIG-17 analysis: morphology & kinematics (§1), observation history 1989–2017 (§2), geography (§3), aviation interaction (§4), specific cases incl. 2001 Arzamas-16 all-day track (§5), engineering reconstructions (§6), Kosmopoisk methodology (§7), «миролюбив и неконфликтен» behavioural assessment (§8), and **§9 What is NOT said** — the critical negative findings (no TM, no Ловондатр, no Lazar, no future-descendants).
- Transcript `08_3zvezdnie_NLO_22min.txt` **retroactively identified as the same 25 March 2017 Zigelevsky Readings source** — dual transcript confirmation (identical YouTube URL, identical 22-min duration, identical moderator intro, identical topic title, identical verbatim phrases incl. «миролюбив и неконфликтен», «80 на 80 на 50 метров», «примерно две сотни групп космопоиска»). Folds 08 into the `ZIG-17` source code; 08 is Chernobrov's FINAL PUBLIC LECTURE as well.

**EN — Changed:**
- `catalog/interviews.md` row 51: venue/date anchor added (25 March 2017, 49th Zigelevsky Readings, Moscow); source code `3ZV-NLO` → `ZIG-17`; row tagged as FINAL PUBLIC LECTURE with 2-month-before-death marker; both transcript files listed. New row 57a added under 2017 section as cross-link. Header corpus statement updated to «20 transcripts / 19 distinct lectures».
- `catalog/research-2010-2017.md`: added 2017 timeline row highlighting 25.03.2017 as Chernobrov's final public lecture; updated per-interview analysis table to reference new 20_zigelevsky file; corpus-closure text updated.
- `analysis/MASTER_chernobrov_claims.md`:
  - §0.3 source-code table: new `ZIG-17` row with full description; `3ZV-NLO` deprecated as alias.
  - §6.5 timeline: new 25 March 2017 entry between 2015 and 18 May 2017 death rows.
  - **New §8.8 ZIG-17 (2017 final public lecture)** — dedicated 3zv-morphology block with verbatim-parameter table, aviation-interaction summary, 10–11 Oct 2001 Arzamas-16 case, additional case anchors (2000 Azerbaijan, 1997 RF video, 2010s Moon silhouette), canonical trajectory nodes, and **CRITICAL NEGATIVE FINDING** clarifying no-time-machine-identification in this lecture.
  - **New §11.15** — clarifies that the «3-star UFO = time machine» reading is NOT Chernobrov's claim; the MV↔3zv identification is an analyst's cross-reference inference from `B-HRON03` §32.4 (2002 Medveditskaya Lovondatr-7 field test +12 / +114 / +1 min correlations), which uses temporal-statistical «появился … после» language rather than identity language. Chernobrov had 15 years after 2002 to state the correlation on the lecture circuit and chose not to, including in ZIG-17.
  - Header scope/synthesis-date updated to v0.5.2.
- `README.md`: transcript count «19 Whisper transcripts» → «20 Whisper-large-v3 transcripts (2.1 MB) covering 19 distinct lectures (files 08 and 20 = same 25 Mar 2017 Zigelevsky source, two Whisper passes)»; QUICK NAVIGATION and Corpus Statistics rows updated; Transcripts code table gains `ZIG-17` entry flagged as final public lecture; per-interview directory listing grows from 8 to 9 files (adds `20_zigelevsky_2017_3star.md`); new Key Findings entry #14 on final lecture + MV↔3zv clarification; Status header updated to v0.5.2.

**RU — Добавлено:**
- `transcripts/20_ZigelevskyChteniya_49_3zvNLO_2017-03-25_22min.txt` — свежий проход Groq Whisper-large-v3 лекции на 49-х Зигелевских чтениях (Москва, 25 марта 2017, 22 мин; YouTube `4YGeR1KsXy0`).
- `analysis/per-interview/20_zigelevsky_2017_3star.md` (~36 КБ, 9 фокус-разделов) — выделенный анализ ZIG-17: морфология и кинематика (§1), история наблюдений 1989–2017 (§2), география (§3), взаимодействие с авиацией (§4), конкретные случаи включая суточное отслеживание 2001 г. → Арзамас-16 (§5), инженерные реконструкции (§6), методология Космопоиска (§7), поведенческая оценка «миролюбив и неконфликтен» (§8), и **§9 Что НЕ сказано** — критические отрицательные находки (нет МВ, нет Ловондатр, нет Лазара, нет гипотезы «потомков из будущего»).
- Транскрипт `08_3zvezdnie_NLO_22min.txt` **ретроспективно идентифицирован как тот же источник 25 марта 2017, 49-е Зигелевские чтения** — подтверждение двойного транскрипта (одинаковый YouTube URL, одинаковая длительность 22 мин, одинаковое вступление ведущего, одинаковое название темы, одинаковые дословные фразы, включая «миролюбив и неконфликтен», «80 на 80 на 50 метров», «примерно две сотни групп космопоиска»). 08 сливается в код источника `ZIG-17`; 08 также является ФИНАЛЬНОЙ ПУБЛИЧНОЙ ЛЕКЦИЕЙ Черноброва.

**RU — Изменено:**
- `catalog/interviews.md` строка 51: добавлен anchor места/даты (25 марта 2017, 49-е Зигелевские чтения, Москва); код источника `3ZV-NLO` → `ZIG-17`; строка помечена как ФИНАЛЬНАЯ ПУБЛИЧНАЯ ЛЕКЦИЯ с маркером «2 месяца до смерти»; перечислены оба файла транскрипта. Добавлена новая строка 57a в раздел 2017 как кросс-ссылка. Заголовочное описание корпуса обновлено на «20 транскриптов / 19 различных лекций».
- `catalog/research-2010-2017.md`: добавлена строка хронологии 2017, подчёркивающая 25.03.2017 как финальную публичную лекцию Черноброва; обновлена таблица per-interview-анализов со ссылкой на новый файл 20_zigelevsky; обновлён текст закрытия программы.
- `analysis/MASTER_chernobrov_claims.md`:
  - §0.3 таблица кодов источников: новая строка `ZIG-17` с полным описанием; `3ZV-NLO` помечен как deprecated alias.
  - §6.5 хронология: новая запись 25 марта 2017 между 2015 и 18 мая 2017.
  - **Новый §8.8 ZIG-17 (финальная публичная лекция 2017)** — выделенный блок по морфологии 3zv с таблицей дословных параметров, обзором взаимодействия с авиацией, случаем 10–11.10.2001 Арзамас-16, дополнительными case-anchors (2000 Азербайджан, 1997 первое видео РФ, 2010-е силуэт на Луне), каноническими узлами траекторий, и **КРИТИЧЕСКАЯ ОТРИЦАТЕЛЬНАЯ НАХОДКА**: в этой лекции отсутствует отождествление с машиной времени.
  - **Новый §11.15** — уточнение, что чтение «трёхзвёздник = машина времени» НЕ является утверждением Черноброва; отождествление MV↔3zv — инференция аналитика из кросс-ссылки на `B-HRON03` §32.4 (2002 полевой тест Ловондатр-7 на МГ, корреляции +12 / +114 / +1 мин), в котором используется темпорально-статистический язык «появился … после», а не язык тождества. Чернобров имел 15 лет после 2002 г. для публичной артикуляции корреляции на лекционном контуре и выбрал не делать этого, в том числе в ZIG-17.
  - Заголовок области/даты синтеза обновлён на v0.5.2.
- `README.md`: счёт транскриптов «19 Whisper transcripts» → «20 транскриптов Whisper-large-v3 (2.1 МБ), покрывающих 19 различных лекций (файлы 08 и 20 = один источник 25.03.2017 Зигелевские чтения, два прохода Whisper)»; строки QUICK NAVIGATION и Corpus Statistics обновлены; таблица кодов транскриптов получает запись `ZIG-17`, помеченную как финальная публичная лекция; листинг директории per-interview растёт с 8 до 9 файлов (добавлен `20_zigelevsky_2017_3star.md`); новая запись Key Findings #14 о финальной лекции + уточнение MV↔3zv; заголовок Status обновлён на v0.5.2.

---

## v0.5.1 — Review-driven fixes + NET compendium integration — 2026-04-19

**EN — Fixed (3 review-driven corrections to MASTER §0.0):**
- §0.0 item 1 — Gen-1 outer ЭРП Ø re-sourced. The 0,9 m figure was incorrectly attributed to `B-TV99` offset 705049, but TV-99 verbatim says «около 1 м». The 0,9 m figure originates only in `F-12R` (2003) + `NE-03-PG` (2003) + `NET-12-2003` (2003). Status badge changed ✅ → ⚠ DRIFTED. Drift documented in new §11.12: 1 m (1999) → 0,9 m (2003).
- §0.0 item 13 — "до 40 s/hr" sourcing strengthened. Added `B-SVL` row 118 which carries the same figure verbatim («совпадает»), strengthening this drifted-but-attested claim from anthology + paraphrase duo to monograph + anthology + paraphrase trio.
- §0.0 item 33 + §1.6 (I-7 spacecraft) — re-labelled "designed 1992, first published 2001". The «Ирма-7» figure caption in `B-PV01` §8.5 explicitly reads «Ирма-7", 1992 год». Documented in new §11.13.

**EN — Added — NET 4-issue compendium integration (`B-NET-FULL`):**
- Source: `analysis/articles/NET_full_compendium.md` (~158 KB merge of 4 NET issues: NET-03-2001, NET-06-2002, NET-09-2003, NET-12-2003).
- §0 Source Codes: 5 new codes — `NET-03-2001`, `NET-06-2002`, `NET-09-2003`, `NET-12-2003`, `B-NET-FULL`.
- §0.0 (Quick-ref numerical params): 4 new items (79–82, all marked ➕ NEW): (79) Frolov υ = c·α ≈ c/137 TRC theory; (80) Frolov vortex-drive RU patent #2002128658 (25 Oct 2002); (81) 29 May 2002 Faraday × Kosmopoisk contract signing; (82) 12 April 2003 Faraday Labs × Kosmopoisk «Time Machine» Conference, Moscow.
- §0.0 source-list updates: item 9 (f=c/d) + item 10 (worked example) added `NET-12-2003` lines 286–305 as canonical EN derivation; items 25–28 (mice / cat / dog / Konov) added `NET-03-2001` lines 248–354 as primary EN protocol; item 29 (2001 cohort) reconciled to 9 confirmed by NET English primary (status changed ⚠ DRIFTED → ✅).
- §2.3 expanded: canonical-derivation-locations note; NET-06-2002 «Physical Principles» clarified as qualitative only.
- §4 Measured Results — 3 sub-sections expanded: §4.3 Konov primary source; §4.4 Volunteers (9-roster reconciled); §4.5 Animals (cat «Plombir» / dog «Lunokhod» details).
- §5 Theoretical Basis — new §5.8a Frolov υ = c·α ≈ c/137 TRC theory (Kozyrev-derived, distinct from f=c/d).
- §6 Timeline — 3 new entries: 29 May 2002 contract; 25 Oct 2002 vortex-drive patent; 12 April 2003 expanded with speaker list.
- §10 Institutional Network — §10.3 Honorary leads table: new row "Dr. Alexander M. MISHIN" (explicitly NOT академик and NOT Faraday/Lovondatr consultant); §10.4 Frolov / Faraday Lab: vortex-drive patent added.
- §11 Contradictions — strengthened §11.6 (Mishin retraction: "academician consultant" ❌ RETRACTED); new §11.12 (1 m → 0,9 m drift); §11.13 (I-7 1992 → 2001 gap); §11.14 (conference roster USER-RES §17 vs NET-12-2003 discrepancy).

**EN — Changed:**
- README.md corpus stats — articles row extended with NET compendium; article-analyses count 2 → 3.
- MASTER scope/synthesis-date header updated to v0.5.1; END «Compiled from» line updated.
- Source code registry: 18 → **23** entries in §0.
- §0.0 row count: 78 → **82** rows.

**RU — Исправлено (3 правки в MASTER §0.0 по результатам ревью):**
- §0.0 п. 1 — Внешний Ø ЭРП Gen-1 переатрибутирован. Значение 0,9 м было ошибочно приписано `B-TV99` offset 705049, однако TV-99 буквально говорит «около 1 м». Значение 0,9 м присутствует только в `F-12R` (2003) + `NE-03-PG` (2003) + `NET-12-2003` (2003). Бейдж статуса изменён ✅ → ⚠ DRIFTED. Дрейф задокументирован в новом §11.12: 1 м (1999) → 0,9 м (2003).
- §0.0 п. 13 — Источники для «до 40 с/ч» усилены. Добавлена строка 118 из `B-SVL`, дословно воспроизводящая тот же показатель («совпадает»), усиливая этот дрейфовавший, но подтверждённый показатель с дуэта «антология + пересказ» до трио «монография + антология + пересказ».
- §0.0 п. 33 + §1.6 (аппарат I-7) — переатрибутирован как «спроектирован 1992, впервые опубликован 2001». Подпись к рисунку «Ирма-7» в `B-PV01` §8.5 буквально читается «Ирма-7", 1992 год». Задокументировано в новом §11.13.

**RU — Добавлено — Интеграция NET-компендиума из 4 выпусков (`B-NET-FULL`):**
- Источник: `analysis/articles/NET_full_compendium.md` (~158 КБ, слияние 4 выпусков NET: NET-03-2001, NET-06-2002, NET-09-2003, NET-12-2003).
- §0 Коды источников: 5 новых кодов — `NET-03-2001`, `NET-06-2002`, `NET-09-2003`, `NET-12-2003`, `B-NET-FULL`.
- §0.0 (Числовые параметры быстрой справки): 4 новых пункта (79–82, все ➕ NEW): (79) теория Фролова υ = c·α ≈ c/137 (TRC); (80) патент Фролова RU #2002128658 на вихревой движитель (25 окт 2002); (81) подписание контракта Faraday × Космопоиск 29 мая 2002; (82) конференция «Машина Времени» Faraday × Космопоиск, Москва 12 апреля 2003.
- §0.0 обновления списка источников: пп. 9 + 10 (f=c/d) — добавлен `NET-12-2003` строки 286–305 как канонический EN-вывод; пп. 25–28 (мыши / кошка / пёс / Конов) — добавлен `NET-03-2001` строки 248–354 как первичный EN-протокол; п. 29 (когорта 2001) — согласован к 9, подтверждённым первичным EN-источником NET (статус ⚠ DRIFTED → ✅).
- §2.3 расширен: указание на канонические места вывода; пояснение, что NET-06-2002 «Physical Principles» — только качественный текст.
- §4 Измеренные результаты — расширены 3 подраздела: §4.3 Конов; §4.4 Волонтёры (ростер 9); §4.5 Животные (кошка «Пломбир» / пёс «Луноход»).
- §5 Теоретическая база — новый §5.8a теория Фролова υ = c·α ≈ c/137 (TRC, Козыревская родословная, отличная от f=c/d).
- §6 Хронология — 3 новые записи: 29 мая 2002 контракт; 25 окт 2002 патент на вихревой движитель; 12 апреля 2003 расширено списком спикеров.
- §10 Институциональная сеть — §10.3 таблица почётных руководителей: новая строка «д-р А.М. МИШИН» (прямо НЕ академик и НЕ консультант Faraday/Ловондатр); §10.4 Фролов / Faraday Lab: добавлен патент на вихревой движитель.
- §11 Противоречия — усилен §11.6 (ретракция Мишина: «academician consultant» ❌ ОТОЗВАНО); новые §11.12 (дрейф 1 м → 0,9 м); §11.13 (разрыв I-7 1992 → 2001); §11.14 (несоответствие списка конференц-докладчиков USER-RES §17 vs NET-12-2003).

**RU — Изменено:**
- README.md статистика корпуса — строка статей расширена NET-компендиумом; счёт анализов статей 2 → 3.
- Заголовок области/даты синтеза MASTER обновлён на v0.5.1; финальная строка «Compiled from» обновлена.
- Реестр кодов источников: 18 → **23** записей в §0.
- Кол-во строк §0.0: 78 → **82**.

---

## v0.5.0 — OCR Complete for Encyclopedia + 2010 Book — 2026-04-19

**EN — Added — two new merged book references (corpus 14 → 16):**
- `analysis/books/B-EUFO_enciklopediya_ufologii.md` (117 KB, 14 thematic sections) — consolidated from 5 OCR chunks (`chunks/B-EUFO_p{1..5}_extract.md`, ~277 KB OCR raw). Source: Чернобров В.А., «Энциклопедия уфологии». М.: Вече, 2007. 464 pp., тираж 5000, ISBN 978-5-9533-2542-4. Signed for press 27.07.2007. First Russian-language ufology encyclopedia.
- `B-VBCH10` (~126 KB merged, 3 chunks) — extracts from `chunks/B-VBCH10_p{1,2,3}_extract.md` (~830 KB OCR raw). Source: Чернобров В.А., «Время, Бессмертие, Человек. Отчёт сталкера». М.: РИПОЛ классик, 2010. 320 pp., тираж 5000, ISBN 978-5-386-01752-1. Second edition extending pre-existing material (p. 99).
- Both books added to `MASTER_chernobrov_claims.md` §0 and §0.0 (items 61–78 — 18 new numerical / qualitative claims).

**EN — Added — §0.0 numerical params (items 61–78, all ➕ NEW):**
- (61) Cave time-perception series 1996–2008: 121 series, 280 days, 843 participants (Сьяны + Никиты).
- (62) Centrifuge experiments at Academy of Aviation & Space Medicine, до 9 G.
- (63) Firewalking experiment 02.05.2009 Медведица, 6-метровая дорожка горящих углей.
- (64) Pyramid frog-entombment 1999–2000 Медведицкая гряда.
- (65) Tunguska Zolotov 1960s chrono-deceleration RE-CONFIRMED by Космопоиск 1996 ✅ CRITICAL.
- (66) Severomorsk Soviet Philadelphia replica 1980s (Минсредмаш + Минэлектронпром, anti-SDI).
- (67) MAI ↔ РПИ 1993 teleportation attempt + МАИ 2003 paired-installation experiments cancelled.
- (68) 17 chrono-* terms coined by Chernobrov / Космопоиск 1985–2002.
- (69) СККБ «Астра» of Космопоиск at МАИ им. Орджоникидзе (early 1990s).
- (70) Standing R&D consortium for «гравитационных электромагнитных движителей»: МАИ + ЦНИИМаш + НПО «Энергия» + Космопоиск.
- (71) Body as spontaneous Lovondatr — central unification thesis of `B-VBCH10`.
- (72) ОУВ (Орган Управления Временем) — Chernobrov's 2010 coinage.
- (73) Body-emitted Time-field can soften Si-Si bonds (biophysical extension).
- (74) Chernobrov personal NDE 1984 (frozen at −40 °C).
- (75) Anfalov on Dulce 1979 with TRANS-V-ELEMENT 115 — single direct Lazar cross-ref in entire `B-EUFO`.
- (76) «Сталкер» 8-instrument Time-physics field kit (1999).
- (77) Okhatrin microleptonic Tesla-antenna method.
- (78) Folk legends as темпоральное оружие framework + Holy Grail under active 2010 «Космопоиск» investigation.

**EN — Added — MASTER new subsections:**
- §3.6 «Сталкер» 8-instrument field kit; §3.7 Cave time-perception experiments.
- §5 lexicon extended (ОУВ, ССС / ОССС / ПССС triad); §5.7 Body-as-spontaneous-Lovondatr UNIFICATION THESIS; §5.8 Okhatrin microleptonic Tesla-antenna method.
- §6 Timeline — 13 new entries across pre-1988, 1990s, 2000s, late period.
- §8.6 UFO acceleration envelope (≈5100 g) + chrono-shielding interpretation; §8.7 Folk legends + Holy Grail Космопоиск investigation.
- §9.5 Anfalov on Dulce 1979 with TRANS-V-ELEMENT 115.
- §10.5 build-partners table — 5 new institutional rows.
- §11.10 institutional segregation (2007 + 2010 omit Frolov / Faraday circuit); §11.11 series claim not verified in `B-VBCH10`.

**EN — Changed:**
- README.md corpus stats 14 → 16 B-*; PDF status table OCR COMPLETE; Key Findings extended (Tunguska Zolotov re-confirmation; Severomorsk replica; body-as-Lovondatr thesis); Known Gaps closed for OCR.
- MASTER header v0.5.0 (2026-04-19); «Compiled from» line references 16 book analyses.
- Source code registry: 16 → 18 entries (added full `B-EUFO` row; `B-VBCh10` placeholder promoted to full `B-VBCH10`).

**RU — Добавлено — два новых объединённых книжных справочника (корпус 14 → 16):**
- `analysis/books/B-EUFO_enciklopediya_ufologii.md` (117 КБ, 14 тематических секций) — консолидирован из 5 OCR-чанков (`chunks/B-EUFO_p{1..5}_extract.md`, ~277 КБ OCR-сырца). Источник: Чернобров В.А., «Энциклопедия уфологии». М.: Вече, 2007. 464 с., тираж 5000, ISBN 978-5-9533-2542-4. Подписано в печать 27.07.2007. Первая русскоязычная энциклопедия по уфологии.
- `B-VBCH10` (~126 КБ в объединённом виде, 3 чанка) — извлечения из `chunks/B-VBCH10_p{1,2,3}_extract.md` (~830 КБ OCR-сырца). Источник: Чернобров В.А., «Время, Бессмертие, Человек. Отчёт сталкера». М.: РИПОЛ классик, 2010. 320 с., тираж 5000, ISBN 978-5-386-01752-1. Второе издание, расширяющее ранее существовавший материал (с. 99).
- Обе книги добавлены в `MASTER_chernobrov_claims.md` §0 и §0.0 (пп. 61–78 — 18 новых численных / качественных заявлений).

**RU — Добавлено — §0.0 числовые параметры (пп. 61–78, все ➕ NEW):**
- (61) Пещерные серии восприятия времени 1996–2008: 121 серия, 280 дней, 843 участника (Сьяны + Никиты).
- (62) Эксперименты на центрифуге в Академии авиационной и космической медицины, до 9 G.
- (63) Эксперимент с хождением по огню 02.05.2009 Медведица, 6-метровая дорожка горящих углей.
- (64) Замуровывание жабы в пирамиде 1999–2000 Медведицкая гряда.
- (65) Хронозамедление Золотова 1960-х на Тунгуске ПЕРЕПОДТВЕРЖДЕНО «Космопоиском» 1996 ✅ CRITICAL.
- (66) Северомoрский советский повтор «Элдриджа» 1980-х (Минсредмаш + Минэлектронпром, anti-SDI).
- (67) МАИ ↔ РПИ 1993 попытка телепортации + МАИ 2003 парно-установочные эксперименты отменены.
- (68) 17 хроно-* терминов, введённых Чернобровом / «Космопоиском» 1985–2002.
- (69) СККБ «Астра» «Космопоиска» при МАИ им. Орджоникидзе (начало 1990-х).
- (70) Постоянный R&D-консорциум «гравитационных электромагнитных движителей»: МАИ + ЦНИИМаш + НПО «Энергия» + «Космопоиск».
- (71) Организм как самопроизвольная Ловондатр — центральный тезис объединения `B-VBCH10`.
- (72) ОУВ (Орган Управления Временем) — неологизм Черноброва 2010.
- (73) Поле Времени, эмитируемое организмом, способно размягчать Si-Si связи.
- (74) NDE Черноброва 1984 (замерзание при −40 °C).
- (75) Анфалов о Дульсе 1979 с ТРАНС-V-ЭЛЕМЕНТОМ 115 — единственный прямой кросс-реф на Лазара во всей `B-EUFO`.
- (76) «Сталкер» — 8-приборный полевой комплект физики времени (1999).
- (77) Метод Охатрина для микролептонной антенны Теслы.
- (78) Народные легенды как фреймворк темпорального оружия + Грааль в активном расследовании «Космопоиска» 2010.

**RU — Добавлено — новые подразделы MASTER:**
- §3.6 «Сталкер» 8-приборный полевой кит; §3.7 Пещерные эксперименты по восприятию времени.
- §5 лексикон расширен (ОУВ, триада ССС / ОССС / ПССС); §5.7 тезис «Организм как самопроизвольная Ловондатр»; §5.8 метод Охатрина для микролептонной антенны Теслы.
- §6 Хронология — 13 новых записей по до-1988, 1990-м, 2000-м и позднему периоду.
- §8.6 Огибающая ускорения НЛО (≈5100 g) + интерпретация хроно-экранирования; §8.7 Народные легенды + расследование Грааля «Космопоиском».
- §9.5 Анфалов о Дульсе 1979 с ТРАНС-V-ЭЛЕМЕНТОМ 115.
- §10.5 таблица партнёров сборки — 5 новых институциональных строк.
- §11.10 институциональная сегрегация (2007 + 2010 опускают Фролов / Faraday круг); §11.11 серия книг не подтверждена в `B-VBCH10`.

**RU — Изменено:**
- README.md статистика корпуса 14 → 16 B-*; таблица статуса PDF — OCR ВЫПОЛНЕН; раздел ключевых находок расширен (переподтверждение Золотова на Тунгуске; Северомоск-повтор; тезис «тело-как-Ловондатр»); раздел Известных пробелов закрыт по OCR.
- Заголовок MASTER v0.5.0 (2026-04-19); строка «Compiled from» ссылается на 16 книжных анализов.
- Реестр кодов источников: 16 → 18 записей (добавлена полная строка `B-EUFO`; заглушка `B-VBCh10` повышена до полного `B-VBCH10`).

---

## v0.3.0 — MASTER Synthesis Complete — 2026-04-18

**EN — Added:**
- `analysis/MASTER_chernobrov_claims.md` (target 100–150 KB, 13 sections, bilingual RU+EN side-by-side) — unified synthesis of every technical claim across transcripts, books, articles, patents, and meta-research.
- `README.md` (bilingual RU-first, mirroring `bob-lazar-archive` structure).
- `CHANGELOG.md` (this file).

**EN — Changed:**
- Source-code convention finalised: `B-*` prefix for all books (e.g. `B-TV99`, `B-TPV01`, `B-PV01`, `B-MG05`, `B-HRON03`, `B-KP`, `B-MPN`, `B-EAYAV`, `B-EZM`, `B-SS`, `B-SVL`, `B-TMV`, `B-TPM`, `B-PMF`, `B-SMALL`); transcript codes by venue + year (`MUR-14`, `HRON-14`, `LAI-14`, `MV-46`, `MG-DOC-17`, `KP-LEC-13`, `KP-N24-58`, `NLO-DPL-24`); article / patent codes (`TM-02`, `NE-03-PG`, `NE-03-FP`, `PAT-RF2003`, `F-12R`); meta-research codes (`USER-RES-2026-04-18`, `KEY-FINDINGS-01`).

**EN — Verified:**
- Review Gate 2 PASS: 29/30 verbatim quotes matched against source, 0 hallucinations in MASTER.
- 3 paraphrase errors in §1 caught during Review Gate 2 and corrected: lethal threshold "2 seconds" → 1.5 seconds (per verbatim source); MV-device generations reconciled across Lovondatr-1 … Lovondatr-7; Frolov formula attribution normalised to `NE-03-FP`.

**RU — Добавлено:**
- `analysis/MASTER_chernobrov_claims.md` (цель 100–150 КБ, 13 секций, двуязычный RU+EN бок-о-бок) — единый синтез всех технических утверждений из транскриптов, книг, статей, патентов и мета-исследований.
- `README.md` (двуязычный RU-первичный, зеркалирует структуру `bob-lazar-archive`).
- `CHANGELOG.md` (этот файл).

**RU — Изменено:**
- Финализирована конвенция кодов источников: префикс `B-*` для всех книг; коды транскриптов по месту + году; коды статей / патента; коды мета-исследований.

**RU — Проверено:**
- Review Gate 2 PASS: 29/30 дословных цитат сверены с источником, 0 галлюцинаций в MASTER.
- 3 ошибки пересказа в §1 пойманы на Review Gate 2 и исправлены: летальный порог «2 секунды» → 1,5 секунды (по дословному источнику); поколения устройств МВ согласованы по Ловондатр-1 … Ловондатр-7; атрибуция формулы Фролова нормализована к `NE-03-FP`.

---

## v0.2.0 — Batch 2: Book & Article Analysis — 2026-04-18

**EN — Added:**
- 14 merged `B-*` book references (total ~1 MB): `B-TV99_TPV01_core_time_books.md` (combined 1999 + 2001), `B-PV01_puteshestviya_vo_vremeni.md`, `B-MG05_medveditskaya_gryada.md`, `B-HRON03_hroniki_vizitov_NLO.md`, `B-KP_krugi_na_polyakh.md`, `B-MPN_mesta_posadok_NLO.md`, `B-EAYAV_enciklopediya_anomalnykh.md`, `B-EZM_zagadochnye_mesta_zemli.md`, `B-SS_spravochnik_stalkera.md`, `B-SVL_sushchestvuyut_vopreki_logike.md`, `B-TMV_tungusskiy_meteorit_vremya.md`, `B-TPM_parallelnye_miry.md`, `B-PMF_podmoskove.md`, `B-SMALL_batch1.md` + `B-SMALL_batch2.md`.
- 2 article / patent analyses: `articles_and_patent.md` (covering `TM-02`, `NE-03-PG`, `NE-03-FP`, `PAT-RF2003`); `F-12R_faraday_patent_paper.md`.
- 21 extraction-chunk intermediates under `analysis/books/chunks/`.

**EN — Processed:**
- All 32 FB2 books from Flibusta extracted to plaintext (`books/downloads/fb2_text/`, 37 MB).
- 5 major PDFs fully indexed where text-layered: Encyclopedia of Ufology (169 MB, OCR pending at this stage); Crop Circles / Kosmopoisk (8.7 MB); Faraday 12rus patent paper (2.7 MB); Chronicles of UAP Visits (2.1 MB); VBCh 2010 (136 MB, OCR pending).
- 10 HTML articles + patent pages processed.

**EN — Known issues (at time of v0.2.0):**
- OCR pending on the two large PDFs (Encyclopedia of Ufology 169 MB; VBCh 2010 136 MB) — closed in v0.5.0.
- Large (1.3 GB) `chunks/` intermediate tree retained for traceability; not intended for downstream consumption.

**RU — Добавлено:**
- 14 объединённых книжных справочников `B-*` (всего ~1 МБ): `B-TV99_TPV01_core_time_books.md` (объединённый анализ двух базовых книг по теории времени 1999 + 2001); `B-PV01_puteshestviya_vo_vremeni.md`; `B-MG05_medveditskaya_gryada.md`; `B-HRON03_hroniki_vizitov_NLO.md`; `B-KP_krugi_na_polyakh.md`; `B-MPN_mesta_posadok_NLO.md`; `B-EAYAV_enciklopediya_anomalnykh.md`; `B-EZM_zagadochnye_mesta_zemli.md`; `B-SS_spravochnik_stalkera.md`; `B-SVL_sushchestvuyut_vopreki_logike.md`; `B-TMV_tungusskiy_meteorit_vremya.md`; `B-TPM_parallelnye_miry.md`; `B-PMF_podmoskove.md`; `B-SMALL_batch1.md` + `B-SMALL_batch2.md` (агрегат коротких работ).
- 2 анализа статей / патента: `articles_and_patent.md` (покрывает `TM-02`, `NE-03-PG`, `NE-03-FP`, `PAT-RF2003`); `F-12R_faraday_patent_paper.md` — отдельное ревью патентной статьи Faraday 12rus.
- 21 промежуточный чанк-извлечение под `analysis/books/chunks/`.

**RU — Обработано:**
- Все 32 FB2-книги с Флибусты извлечены в плейнтекст (`books/downloads/fb2_text/`, 37 МБ).
- 5 крупных PDF полностью проиндексированы там, где есть текстовый слой: «Энциклопедия уфологии» (169 МБ, OCR — на тот момент ещё не выполнен); «Круги на полях» / Космопоиск (8.7 МБ); Faraday 12rus patent paper (2.7 МБ); «Хроники визитов НЛО» (2.1 МБ); ВБЧ 2010 (136 МБ, OCR — на тот момент ещё не выполнен).
- 10 HTML-статей и страниц патентов обработаны.

**RU — Известные проблемы (на момент v0.2.0):**
- OCR не выполнен для двух крупных PDF («Энциклопедия уфологии» 169 МБ; ВБЧ 2010 136 МБ) — закрыто в v0.5.0.
- Большое (1.3 ГБ) дерево промежуточных чанков `chunks/` сохранено для прослеживаемости; не предназначено для потребления downstream.

---

## v0.1.0 — Batch 1: Transcript Analysis — 2026-04-18

**EN — Added:**
- Per-interview analyses (8 files covering 19 transcripts): `01_02_mashina_vremeni_lectures.md`, `03_04_05_mixed.md`, `06_sledy_puteshestvennikov.md`, `07_13_heavy_mv.md`, `08_09_10_14_19_thematic.md`, `11_12_mv_lectures.md`, `15_17_18_field_media.md`, `16_krugi_na_polyakh.md`.
- Topical restructurings (8 files): `01_02_mashina_vremeni_topical.md`, `03_04_05_topical.md`, `06_sledy_topical.md`, `07_13_topical.md`, `08_09_10_14_19_topical.md`, `11_12_topical.md`, `15_17_18_topical.md`, `16_krugi_topical.md`.
- Case catalogs: `16_pictograms_case_catalog.md` — 153 authentic crop pictograms (1950–2010); `06_chernobrov_case_catalog.md` — case registry from Chernobrov's own lectures.
- `01_02_comparison.md` — early cross-check of overlapping lectures.
- `QA_REVIEW.md` — Review Gate 1 PASS.

**RU — Добавлено:**
- Анализы по интервью (8 файлов, 19 транскриптов).
- Тематические перегруппировки (8 файлов).
- Каталоги случаев: `16_pictograms_case_catalog.md` — 153 подлинных пиктограммы (1950–2010); `06_chernobrov_case_catalog.md` — реестр случаев из собственных лекций Черноброва.
- `01_02_comparison.md` — ранняя сверка пересекающихся лекций.
- `QA_REVIEW.md` — Review Gate 1 PASS.

---

## v0.0.1 — Corpus Acquisition — 2026-04-18

**EN — Added:**
- 19 YouTube lectures transcribed with Whisper-large-v3 (Russian), ≈2.1 MB of text — `01_…_2h37.txt` through `19_GravitatsionnyeAnomalii_12min.txt`.
- 32 Flibusta FB2 downloads (34 archives in `books/downloads/flibusta_books/`; 32 yielded unique plaintexts after deduplication).
- 5 major PDFs downloaded: Encyclopedia of Ufology (169 MB); Crop Circles / Kosmopoisk (8.7 MB); Faraday 12rus patent paper (2.7 MB); Chronicles of UAP Visits (2.1 MB); VBCh 2010 — Time, Immortality, Human (136 MB).
- Journal PDFs: `net_03_2001.pdf`, `net_06_2002.pdf`, `net_09_2003.pdf`, `net_12_2003.pdf` (New Energy issues with Chernobrov / Frolov material).
- HTML article captures: Flibusta author page, Koob index, Kosmopoisk temporology page, Trinitarian Academy 2002/2003 reports, Livelib, Natural World, Avidreaders, Obuchalka, Klex, Royallib, Fileskachat, Hayakawa blog, Frolov Wikireading, Medveditskaya Ridge Avidreaders.
- Perplexity research (2 files): `01_early_kosmopoisk_chernobrov.md` + `01_…_KEY_FINDINGS.md`; `02_chernobrov_time_works.md` + `02_…_thinking.md`.
- User-provided meta-research (1 file): `03_user_provided_research_2026-04-18.md` (source-of-truth for Lovondatr-7 dimensions, Konov trial, 1.5 s lethal threshold, patent discontinuation date, etc.).
- Catalog support: `catalog/deep_research.md`; `catalog/denis_youtube_catalog.json`; `catalog/whisper_alternatives.md`.

**RU — Добавлено:**
- 19 лекций YouTube, транскрибированных Whisper-large-v3 (русский), ≈2.1 МБ текста.
- 32 загрузки FB2 с Флибусты (34 архива в `books/downloads/flibusta_books/`; 32 дали уникальные плейнтексты после дедупликации).
- 5 крупных PDF скачано: «Энциклопедия уфологии» (169 МБ); «Круги на полях» / Космопоиск (8.7 МБ); Faraday 12rus patent paper (2.7 МБ); «Хроники визитов НЛО» (2.1 МБ); ВБЧ 2010 — «Время, Бессмертие, Человек» (136 МБ).
- Журнальные PDF: `net_03_2001.pdf`, `net_06_2002.pdf`, `net_09_2003.pdf`, `net_12_2003.pdf» (выпуски «Новой энергетики» с материалами Черноброва / Фролова).
- HTML-захваты статей: страница автора Флибуста, индекс Koob, страница темпорологии Космопоиска, отчёты Академии тринитаризма 2002/2003, Livelib, Natural World, Avidreaders, Обучалка, Klex, Royallib, Fileskachat, блог Хаякавы, Фролов Wikireading, Медведицкая гряда Avidreaders.
- Исследования Perplexity (2 файла): `01_early_kosmopoisk_chernobrov.md` + `01_…_KEY_FINDINGS.md`; `02_chernobrov_time_works.md` + `02_…_thinking.md`.
- Пользовательский мета-анализ (1 файл): `03_user_provided_research_2026-04-18.md` (источник истины для размеров Ловондатр-7, испытания Конова, летального порога 1,5 с, даты прекращения патента и т. д.).
- Каталог-поддержка: `catalog/deep_research.md`; `catalog/denis_youtube_catalog.json`; `catalog/whisper_alternatives.md`.
