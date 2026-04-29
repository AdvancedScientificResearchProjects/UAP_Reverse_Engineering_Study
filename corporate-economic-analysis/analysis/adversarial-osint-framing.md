# Adversarial OSINT framing — 3-pass cross-validation / Адверсариальная OSINT-рамка — кросс-валидация в 3 прохода

---

## Premise / Предпосылка

**EN:** Adversarial OSINT framing is a **methodological device**, not a content layer. Each per-company file in [`../companies/`](../companies/) and each analytical claim in [`./`](./) benefits from running three independent adversarial passes over the same public-source surface — positive-control, devil's-advocate, and null-finding — and reconciling the outputs into the file's documented narrative. The output of the framing is the surfaced disagreement between the three passes; that disagreement is what the analyst then resolves into a guarded claim. This file documents the framing; it does **not** execute it.

**RU:** Адверсариальная OSINT-рамка — это **методологический приём**, а не слой содержания. Каждый покомпанийный файл в [`../companies/`](../companies/) и каждый аналитический вывод в [`./`](./) выигрывает от трёх независимых адверсариальных проходов по одной и той же публично-источниковой поверхности — positive-control, devil's-advocate и null-finding — с последующим примирением выводов в документированный нарратив файла. Выход рамки — выявленное несогласие между тремя проходами; именно это несогласие аналитик разрешает в осторожно-сформулированный вывод. Этот файл документирует рамку; он её **не** исполняет.

---

## The 3 passes / Три прохода

### Pass 1 — Positive control / Проход 1 — Позитивный контроль

**EN:** "What is publicly documented?" The positive-control pass collects only well-attested facts from canonical primary sources — SEC EDGAR filings, government-contract records, official corporate communications, peer-reviewed press. The output is a list of documented facts, each tagged with a source-of-record reference. The pass deliberately suppresses interpretation; it produces what an analyst would defend as "indisputable, well-sourced, factual."

**RU:** «Что публично задокументировано?» Проход positive-control собирает только хорошо подтверждённые факты из канонических первичных источников — заявок SEC EDGAR, записей по госконтрактам, официальных корпоративных коммуникаций, рецензируемой прессы. Выход — список задокументированных фактов с указанием источника-по-записи. Проход намеренно подавляет интерпретацию; он производит то, что аналитик защитит как «бесспорное, хорошо источникованное, фактическое».

### Pass 2 — Devil's advocate / Проход 2 — Адвокат дьявола

**EN:** "What is publicly disputed or contested?" The devil's-advocate pass actively searches for skeptical positions, contrary press, regulatory criticism, post-mortems, and alternative interpretations of the same data. The output is a list of counter-claims and competing readings, each sourced. The pass deliberately privileges the *strongest* skeptical case — not the easiest one. Particularly important when the positive-control pass returned a clean narrative; clean narratives are the most likely to have been omitting their counter-cases.

**RU:** «Что публично оспаривается или дискутируется?» Проход devil's-advocate активно ищет скептические позиции, противоречащую прессу, регуляторную критику, post-mortems и альтернативные интерпретации тех же данных. Выход — список контр-утверждений и конкурирующих прочтений, каждое с источником. Проход намеренно отдаёт приоритет *сильнейшему* скептическому случаю — не самому простому. Особенно важен, когда positive-control дал чистый нарратив; чистые нарративы чаще всего опускают контр-кейсы.

### Pass 3 — Null-finding probe / Проход 3 — Зонд нулевого вывода

**EN:** "What is conspicuously absent from the public record?" The null-finding pass is the hardest of the three and the one most often skipped. It documents structured absences — categories of information that *should* exist in the public record by analogy to comparable entities, but that *do not* surface for the target. Examples: a comparable competitor publishes 10-K segment-level revenue, but the target reports only consolidated figures; a comparable acquisition has a documented integration-team named in proxy filings, but the target acquisition does not. The output is a list of absences, each with provenance for the comparable cases that establish what should have been visible.

**RU:** «Что заметно отсутствует в публичном реестре?» Проход null-finding — самый трудный из трёх и тот, который чаще всего пропускают. Он документирует структурированные отсутствия — категории информации, которые *должны* существовать в публичном реестре по аналогии с сопоставимыми сущностями, но которые для целевого объекта *не* всплывают. Примеры: сопоставимый конкурент публикует выручку 10-K по сегментам, а цель отчитывается только консолидированно; у сопоставимого поглощения есть задокументированная команда интеграции, названная в заявке-прокси, а у целевого поглощения — нет. Выход — список отсутствий, каждый с провенансом по сопоставимым случаям, устанавливающим, что должно было быть видимо.

---

## Repo policy reminder / Напоминание о политике репозитория

**EN:** The analytical product in this archive is **human-curated**. The 3-pass framing is a methodological aid that the human analyst applies; the framing itself is **never named as the content-author** of any claim, and tooling used to assist the framing (LLMs, search tools, scripts) is **never named as content-author** in any file in this archive. The same convention is followed in Track 5 ([`../../osint-intelligence-analysis/`](../../osint-intelligence-analysis/)) and in the Track 7 [intelligence-analysis methodology](./intelligence-analysis-methodology.md) — methodology files document the device; content files document the claim, with the human analyst as the author-of-record.

**RU:** Аналитический продукт в этом архиве — **куратируется человеком**. 3-проходная рамка — методологический помощник, применяемый аналитиком-человеком; сама рамка **никогда не называется автором содержания** какого-либо вывода, а инструментарий, использованный в её поддержку (LLM, поисковые инструменты, скрипты), **никогда не называется автором содержания** ни в одном файле этого архива. Та же конвенция действует в Треке 5 ([`../../osint-intelligence-analysis/`](../../osint-intelligence-analysis/)) и в [методологии разведывательного анализа](./intelligence-analysis-methodology.md) Трека 7 — файлы методологии документируют приём; содержательные файлы документируют вывод, с аналитиком-человеком как автором-по-записи.

---

## How this differs from / extends `intelligence-analysis-methodology.md` / Чем отличается от и расширяет `intelligence-analysis-methodology.md`

**EN:** [`./intelligence-analysis-methodology.md`](intelligence-analysis-methodology.md) is the strategic-frame document — what "intelligence analysis" means in this archive, the source classes used, the structured-analytic techniques (ACH, link analysis, signature analysis, key-assumptions check, quality-of-information check). Adversarial OSINT framing is a **tactical companion** to that document — a specific routine the analyst runs *inside* the structured-analytic-tradecraft frame, applied per-file when reconciling first-pass output. The 3-pass framing complements the **key-assumptions check** technique: positive-control surfaces the assumed facts, devil's-advocate surfaces the assumed-but-contestable, null-finding surfaces the assumed-by-omission. All three then feed the file's "What this file does NOT claim" guard.

**RU:** [`./intelligence-analysis-methodology.md`](intelligence-analysis-methodology.md) — стратегический рамочный документ: что значит «разведывательный анализ» в этом архиве, какие классы источников используются, какие структурно-аналитические техники (ACH, анализ связей, сигнатурный анализ, проверка ключевых предпосылок, проверка качества информации). Адверсариальная OSINT-рамка — **тактический спутник** этого документа: конкретная процедура, которую аналитик прогоняет *внутри* структурно-аналитической рамки ремесла, применяемая по-файлово при примирении вывода первого прохода. 3-проходная рамка дополняет технику **проверки ключевых предпосылок**: positive-control выявляет принятые факты, devil's-advocate выявляет принятое-но-оспоримое, null-finding выявляет принятое-через-упущение. Все три затем питают защитный раздел файла «Чего этот файл НЕ утверждает».

---

## Output template per company file / Выходной шаблон по покомпанийному файлу

**EN:** When the 3-pass framing has been applied to a `companies/<name>.md` file, the recommended output structure is a brief reconciliation note appended to the file's narrative — not a separate section per pass. The reconciliation surfaces what the three passes agreed on (consensus), where they disagreed (divergence flag), and what each pass uniquely contributed (positive-only / contested-only / absent-only annotations on individual claims). The reconciliation is short — one paragraph — and points the reader to the underlying source of each guarded claim.

**RU:** Когда 3-проходная рамка применена к файлу `companies/<name>.md`, рекомендуемая структура выхода — краткая примирительная заметка, добавляемая к нарративу файла, — не отдельная секция на проход. Примирение выявляет, в чём три прохода согласились (консенсус), где они разошлись (флаг расхождения) и что каждый проход внёс уникально (аннотации positive-only / contested-only / absent-only по индивидуальным выводам). Примирение — короткое, в один абзац — и направляет читателя к первичному источнику каждого осторожно-сформулированного вывода.

---

## What this file does NOT claim / Чего этот файл НЕ утверждает

- **EN:**
  - It does **not** prescribe any particular tooling for executing the 3 passes.
  - It does **not** name LLMs, search engines, or other tools as content-authors.
  - It does **not** assert that the 3-pass framing has been applied uniformly across all existing Track-7 files; it documents the framing for use going forward.
  - It does **not** replace the [`intelligence-analysis-methodology.md`](intelligence-analysis-methodology.md) frame; it complements it.
  - It does **not** advance any UAP-related substantive claim; this is a methodology file.

- **RU:**
  - Он **не** предписывает какой-либо конкретный инструментарий для исполнения трёх проходов.
  - Он **не** называет LLM, поисковые системы или иные инструменты авторами содержания.
  - Он **не** утверждает, что 3-проходная рамка единообразно применена ко всем существующим файлам Трека 7; он документирует рамку для применения в дальнейшем.
  - Он **не** заменяет рамку [`intelligence-analysis-methodology.md`](intelligence-analysis-methodology.md); он её дополняет.
  - Он **не** выдвигает каких-либо UAP-связанных содержательных утверждений; это файл методологии.

---

[← Corporate-Economic Analysis README](../README.md) · [Intelligence-analysis methodology / Методология разведывательного анализа](./intelligence-analysis-methodology.md) · [Root README / Корень проекта](../../README.md)
