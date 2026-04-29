# Intelligence-analysis methodology — Track 7 / Методология разведывательного анализа — Трек 7

---

## What "intelligence-analysis" means here / Что значит «разведывательный анализ» здесь

**EN:** The phrase "intelligence analysis" is used in this archive in its **structured-analytic-tradecraft** sense, applied to **public-source data only**. It is *not* covert collection, *not* classified material, *not* signals intelligence, *not* human-intelligence elicitation. The pose is the same as Track 5: an analyst with public feeds, working in the open, applying named techniques drawn from the public intelligence-analysis literature (CIA Tradecraft Primer; Heuer; Pherson). The qualifier in the file title — "intelligence-analysis" — denotes the **method**, not the source class.

**RU:** Словосочетание «разведывательный анализ» используется в этом архиве в смысле **структурно-аналитического ремесла** (structured analytic tradecraft), применяемого **только к данным из публичных источников**. Это *не* скрытый сбор, *не* засекреченные материалы, *не* SIGINT, *не* HUMINT-эликитация. Поза — та же, что в Треке 5: аналитик с публичными фидами, работающий в открытую, применяющий именованные техники из публичной литературы по разведывательному анализу (CIA Tradecraft Primer; Хойер; Ферсон). Квалификатор в заголовке файла — «разведывательный анализ» — обозначает **метод**, а не класс источников.

---

## How it differs from Track 5 / Чем отличается от Трека 5

**EN:** Track 5 (`osint-intelligence-analysis/`) defines a generic OSINT methodology — the signature-cluster framework for distinguishing standard from non-standard signatures across physical-experiment data. Track 7 **specialises** that methodology to **corporate-economic targets**.

**RU:** Трек 5 (`osint-intelligence-analysis/`) определяет общую методологию OSINT — сигнатурно-кластерную рамку различения стандартных и нестандартных сигнатур на данных физических экспериментов. Трек 7 **специализирует** эту методологию на **корпоративно-экономических объектах**.

**Track-7 source classes (specialisation of Track 5) / Классы источников Трека 7 (специализация Трека 5):**

- **SEC EDGAR filings** — 10-K (annual), 10-Q (quarterly), 8-K (current events), DEF 14A (proxy), Form 4 (insider transactions), Form 10 (registration). // Отчётность SEC EDGAR.
- **M&A press releases** — corporate communications wires (Business Wire, PR Newswire) and acquirer / target IR pages. // Пресс-релизы по M&A.
- **LinkedIn** — public profiles of named executives and engineers; corporate "About" / employee-count pages. // LinkedIn — публичные профили и страницы компаний.
- **Industry conference presentations** — AFCEA, NDIA, AUVSI, AIAA, IEEE, AAAS — public proceedings. // Презентации с отраслевых конференций.
- **Patent filings** — USPTO Patent Public Search and Google Patents; assignee-by-company queries. // Патентная отчётность USPTO.
- **Government-contract records** — USAspending.gov, FPDS-NG (Federal Procurement Data System), SAM.gov, DOE / NNSA M&O contract awards pages. // Записи о государственных контрактах.
- **Trade-press reports** — Defense News, Aviation Week, SpaceNews, Inside Defense — paywalled but cited. // Отраслевая пресса.

---

## Structured analytic techniques used / Используемые структурно-аналитические техники

**EN:** The named techniques applied in Track 7 are drawn from the standard public corpus of intelligence-analysis tradecraft.

**RU:** Названные техники, применяемые в Треке 7, взяты из стандартного публичного корпуса разведывательно-аналитического ремесла.

| Technique / Техника | Application in Track 7 / Применение в Треке 7 |
|---|---|
| Analysis of Competing Hypotheses (ACH) / Анализ конкурирующих гипотез | Used on the EG&G → S-4 employer-of-record claim against four counter-hypotheses (incomplete identification; misattribution; cover-employer; correct identification). / Применён к claim «EG&G — работодатель по S-4» против четырёх контр-гипотез (неполная идентификация; ошибочная атрибуция; cover-employer; корректная идентификация). |
| Link analysis / Анализ связей | Used to map executive overlaps across the prime constellation and to map the M&O-LLC consortium memberships across DOE labs. / Применён для отрисовки пересечений руководителей в созвездии prime и членств в M&O-LLC по лабораториям DOE. |
| Signature analysis / Сигнатурный анализ | Inherited from Track 5: applied to corporate-disclosure patterns (10-K segment-reporting changes around classified-program transitions). / Унаследован из Трека 5: применён к паттернам корпоративного раскрытия (изменения сегментной отчётности 10-K вокруг переходов засекреченных программ). |
| Chronological / event analysis / Хронологический / событийный анализ | The 22-year EG&G → Amentum timeline and the 1989–2025 Lazar-broadcast timeline are run as parallel event streams for cross-correlation. / 22-летняя хронология EG&G → Amentum и хронология эфиров Лазара 1989–2025 идут параллельными потоками событий для кросс-корреляции. |
| Key-assumptions check / Проверка ключевых предпосылок | Every Track-7 file has an explicit "What this file does NOT claim" section that surfaces and bounds working assumptions. / Каждый файл Трека 7 имеет явную секцию «Чего этот файл НЕ утверждает», поверх которой обнажаются и ограничиваются рабочие предпосылки. |
| Quality-of-information check / Проверка качества информации | Every claim is graded against the four-tier provenance scheme below. / Каждая claim градируется по четырёхуровневой схеме провенанса ниже. |

---

## Adversarial framing — multi-LLM cross-validation / Адверсариальная рамка — multi-LLM кросс-валидация

**EN:** As a methodological device, Track 7 uses **multi-LLM cross-validation** — running the same corporate-research prompt across multiple independently-built large language models — to surface omissions, biases, and confabulations in single-LLM corporate research. This is documented forward-link to `analysis/adversarial-llm-framing.md` (Sprint v2 placeholder).

The repository policy on this device is explicit:

- Multi-LLM cross-validation is a **bias-surfacing instrument**, like a second analyst.
- Multi-LLM output is **never** a content-author. The repository **never** cites an LLM as the source of a fact.
- Where an LLM exchange is the proximate origin of a working note, the human author (Banchenko or contributor) is the cited author and is responsible for source-checking before the note enters the repository.

**RU:** В качестве методологического устройства Трек 7 использует **multi-LLM кросс-валидацию** — прогон одного и того же корпоративно-исследовательского промпта на нескольких независимо построенных больших языковых моделях — для обнажения пропусков, смещений и конфабуляций в single-LLM корпоративном исследовании. Это forward-link на `analysis/adversarial-llm-framing.md` (placeholder Sprint v2).

Политика репозитория по этому устройству явная:

- Multi-LLM кросс-валидация — **инструмент обнажения смещений**, как второй аналитик.
- Вывод multi-LLM **никогда** не является автором содержания. Репозиторий **никогда** не цитирует LLM как источник факта.
- Где обмен с LLM — непосредственный исток рабочей заметки, цитируемым автором является человек (Банченко или контрибьютор), несущий ответственность за источниковедческую проверку до попадания заметки в репозиторий.

---

## Confidence grades / Уровни уверенности

**EN:** The four-grade scheme matches Track 5; operational definitions are restated for Track-7 use.

**RU:** Четырёхуровневая схема совпадает с Треком 5; операционные определения переформулированы под использование Трека 7.

| Grade / Уровень | Operational definition / Операционное определение |
|---|---|
| **High** / **Высокий** | Multiple independent public-source corroborations; primary documents (e.g. SEC filing) available. / Множественные независимые подтверждения из публичных источников; доступны первичные документы (напр., SEC filing). |
| **Medium** / **Средний** | One primary source plus secondary corroboration (industry analyst, trade-press) without contradicting evidence. / Один первичный источник плюс вторичное подтверждение (отраслевой аналитик, профильная пресса) без противоречащих свидетельств. |
| **Low** / **Низкий** | Single non-primary source, or primary source with known reliability concerns. / Один невторичный источник, или первичный источник с известными претензиями к достоверности. |
| **Single-source** / **Один источник** | Exactly one source, no independent corroboration; **explicitly flagged**. / Ровно один источник, без независимого подтверждения; **явно помечается**. |

---

## Falsifiability standard / Стандарт фальсифицируемости

**EN:**
- Every claim in Track 7 must be checkable against a public source.
- Every "single-source" claim must have a counter-claim or null-finding noted in the same file.
- **Absence of evidence is not evidence of absence**, and is recorded as such (e.g. "no public DOE / NNSA contractor record names EG&G Special Projects as the S-4 operator; this is a null finding, not a refutation").
- Where a claim cannot be operationalised against a public source, it is removed or downgraded to "speculation" with the appropriate label.

**RU:**
- Каждая claim в Треке 7 должна быть проверяемой против публичного источника.
- Каждая «одноисточниковая» claim должна иметь контр-claim или null-finding, отмеченный в том же файле.
- **Отсутствие свидетельств — не свидетельство отсутствия**, и фиксируется как таковое (напр., «ни одна публичная запись DOE / NNSA по подрядчикам не называет EG&G Special Projects оператором S-4; это null finding, не опровержение»).
- Если claim не поддаётся операционализации против публичного источника, она удаляется или понижается до «спекуляция» с соответствующей меткой.

---

## Provenance grades for company files / Уровни провенанса для файлов компаний

**EN:** Every per-company file in `companies/` is graded by the highest available source class.

**RU:** Каждый файл компании в `companies/` градируется по наивысшему доступному классу источников.

| Grade / Уровень | Source class / Класс источников |
|---|---|
| **A** | SEC filings — 10-K, DEF 14A, 8-K, Form 10. / Отчётность SEC — 10-K, DEF 14A, 8-K, Form 10. |
| **B** | Wikipedia (with cited primary references) + corporate "About" page. / Wikipedia (с цитируемыми первичными ссылками) + раздел «About» сайта компании. |
| **C** | Press releases / industry analyst reports / trade press. / Пресс-релизы / отчёты отраслевых аналитиков / отраслевая пресса. |
| **D** | Lazar-testimony — used **only** for the EG&G S-4 link, **not** for any other corporate claim in the archive. / Свидетельство Лазара — используется **только** для связки EG&G ↔ S-4, **не** для какой-либо другой корпоративной claim в архиве. |

---

## What this file does NOT claim / Чего этот файл НЕ утверждает

- **EN:**
  - It does **not** assert that the methodology described constitutes covert intelligence collection.
  - It does **not** treat any LLM output as a content-author or source-of-fact.
  - It does **not** claim that "single-source" claims are false; it requires that they be flagged.
  - It does **not** treat absence of public evidence as refutation; it requires explicit null-finding registration.
  - It does **not** advance a conspiracy frame; the methodology is publicly documented structured-analytic tradecraft applied to public sources.

- **RU:**
  - Он **не** утверждает, что описанная методология представляет собой скрытый разведывательный сбор.
  - Он **не** трактует вывод какой-либо LLM как автора содержания или источник факта.
  - Он **не** утверждает, что «одноисточниковые» claim ложны; он требует их явной пометки.
  - Он **не** трактует отсутствие публичных свидетельств как опровержение; он требует явной регистрации null finding.
  - Он **не** продвигает конспирологическую рамку; методология — публично задокументированное структурно-аналитическое ремесло, применяемое к публичным источникам.

---

[← Corporate-Economic Analysis README](../README.md) · [Root README / Корень проекта](../../README.md)
