# Real → new physics validation pipeline / Конвейер валидации «реальное → новая физика»

**EN:** This file fixes the operational pipeline used to decide whether a non-standard signature is **complex but already-known nonlinear physics**, or a **genuinely new (or badly described) physical regime**. The pipeline has 7 ordered steps, 5 acceptance criteria, 3 named error modes, and one explicit boundary condition that says where new science actually begins.

**RU:** Этот файл фиксирует операционный конвейер, по которому решается, является ли нестандартная сигнатура **сложной, но уже известной нелинейной физикой**, или **действительно новым (или плохо описанным) физическим режимом**. Конвейер состоит из 7 упорядоченных шагов, 5 критериев приёмки, 3 поименованных ошибочных мод и одного явного граничного условия, обозначающего, где собственно начинается новая наука.

---

## Core principle / Основной принцип

**EN:** No "magic" is involved. The whole pipeline collapses to: **controlled variables → reproducibility → scaling**. If any one of those three is missing, every later inference is invalid.

**RU:** Никакой «магии». Весь конвейер сводится к одному: **контролируемые переменные → воспроизводимость → масштабирование**. Если отсутствует любое из этих трёх — все последующие выводы недействительны.

---

## The 7-step pipeline / 7-ступенчатый конвейер

### Step 1 — Parameter isolation / Шаг 1 — Изоляция параметров

**EN:** Vary one parameter at a time (voltage, pulse duration, inter-pulse delay, geometry, …). If the effect "drifts" with everything → the observation is noise/chaos. If the effect tracks a single parameter → the observation is physics.

**RU:** Менять по одному параметру за раз (напряжение, длительность импульса, задержку между импульсами, геометрию, …). Если эффект «плавает» от всего — наблюдение есть шум/хаос. Если эффект следует одному параметру — наблюдение есть физика.

### Step 2 — Threshold search / Шаг 2 — Поиск порога

**EN:** Look for a sharp transition at a specific value of the controlling parameter. Example: nothing below 12 kV, effect appears at 12.5 kV, effect grows above 13 kV. A threshold turns "random occurrence" into a **regime** of the system.

**RU:** Искать резкий переход при конкретном значении управляющего параметра. Пример: ниже 12 кВ — ничего, на 12.5 кВ — эффект появляется, выше 13 кВ — усиливается. Наличие порога превращает «случайное появление» в **режим** системы.

### Step 3 — Temporal structure / Шаг 3 — Временна́я структура

**EN:** Check delays, pulse shape, drift. The critical question is: **is there a stable temporal signature?** A stable temporal signature, even of an unexplained effect, is sufficient to call the process reproducible.

**RU:** Проверить задержки, форму импульса, дрейф. Критический вопрос: **есть ли стабильная временна́я сигнатура?** Стабильная временна́я сигнатура даже непонятного эффекта достаточна, чтобы назвать процесс воспроизводимым.

### Step 4 — Multi-channel verification / Шаг 4 — Мультиканальная проверка

**EN:** Compare independent channels — EM, optical, current, mechanical. If they coincide in time → one underlying process. If they diverge in time → several distinct processes are running in the same event and must be separated before any further interpretation.

**RU:** Сравнить независимые каналы — EM, оптический, токовый, механический. Если совпадают по времени — один базовый процесс. Если расходятся по времени — в одном событии идут несколько разных процессов, которые должны быть разделены до любой дальнейшей интерпретации.

### Step 5 — Scaling / Шаг 5 — Масштабирование

**EN:** Increase energy and/or system size. Check whether the structure of the effect is preserved. If yes → fundamental process. If no → local instability.

**RU:** Увеличивать энергию и/или размер системы. Проверять, сохраняется ли структура эффекта. Сохраняется — фундаментальный процесс. Не сохраняется — локальная нестабильность.

### Step 6 — Modelling / Шаг 6 — Моделирование

**EN:** Try to describe the effect through plasma physics, EM models, nonlinear dynamics. Three outcomes: model fits → known physics; model partially fits → complex regime; model fails → candidate for further investigation. Step 6 alone never declares new physics — it only flags candidates for Step 7.

**RU:** Попытаться описать эффект через плазменную физику, EM-модели, нелинейную динамику. Три исхода: модель совпала → известная физика; модель совпала частично → сложный режим; модель не совпала → кандидат для дальнейшего исследования. Шаг 6 сам по себе никогда не объявляет новую физику — он лишь маркирует кандидатов для шага 7.

### Step 7 — Hypothesis crash-test / Шаг 7 — Краш-тест гипотезы

**EN:** Change the medium. Change the material. Change the frequencies. Watch what happens to the effect. If it disappears under reasonable substitutions → it was a property of one specific configuration, not a universal process. If it survives or transforms in a structured way → the effect has its own physics, not borrowed from the configuration.

**RU:** Поменять среду. Поменять материал. Поменять частоты. Смотреть, что происходит с эффектом. Если он исчезает при разумных заменах — это было свойство одной конкретной конфигурации, а не универсальный процесс. Если эффект выживает или трансформируется структурированно — у эффекта своя собственная физика, не одолженная у конфигурации.

---

## Five criteria for a "real new effect" / Пять критериев «реально нового эффекта»

**EN:** An effect is treated as a serious candidate for new (or badly described) physics if **all five** of the following hold:

1. ✅ It is **reproducible** — same conditions, same effect, across runs and across rigs where possible.
2. ✅ It has a **threshold** — there is a critical value of some control parameter where it switches on.
3. ✅ It has a **signature** — a stable, structured fingerprint in time / frequency / cross-channel correlation.
4. ✅ It **scales** — the structure survives changes in energy and/or system size.
5. ✅ It does **not** fit the existing model — known physics cannot reproduce it.

Any single one of these five is **not** sufficient. All five must hold simultaneously.

**RU:** Эффект рассматривается как серьёзный кандидат на новую (или плохо описанную) физику только если выполнены **все пять** условий:

1. ✅ **Воспроизводится** — одинаковые условия дают одинаковый эффект от запуска к запуску и, по возможности, на разных установках.
2. ✅ **Имеет порог** — существует критическое значение управляющего параметра, при котором эффект включается.
3. ✅ **Имеет сигнатуру** — стабильный структурированный отпечаток во времени / частоте / межканальной корреляции.
4. ✅ **Масштабируется** — структура сохраняется при изменении энергии и/или размера системы.
5. ✅ **Не укладывается в существующую модель** — известная физика не воспроизводит эффект.

Любого одного из пяти **недостаточно**. Все пять должны выполняться одновременно.

---

## Three common error modes / Три типичные ошибки

**EN:**

- **Error 1 — "one strange signal = discovery."** A single odd trace is noise/artifact until it has been reproduced. This is the most common failure mode.
- **Error 2 — ignoring noise and artifacts.** Without separating noise from signal at Steps 1–4, "the anomaly" can be an instrument response, ground-loop coupling, or a calibration drift.
- **Error 3 — mixing several processes.** Without multi-channel verification (Step 4), what is reported as "one effect" is often two or three distinct processes interpreted as one.

**RU:**

- **Ошибка 1 — «один странный сигнал = открытие».** Одиночный странный трек есть шум/артефакт, пока не воспроизведён. Самая распространённая ошибочная мода.
- **Ошибка 2 — игнорирование шумов и артефактов.** Без разделения шума и сигнала на шагах 1–4 «аномалия» может оказаться инструментальным откликом, наводкой по контуру земли или дрейфом калибровки.
- **Ошибка 3 — смешение нескольких процессов.** Без мультиканальной проверки (шаг 4) то, что отчитывается как «один эффект», часто оказывается двумя–тремя разными процессами, интерпретируемыми как один.

---

## Where real science actually begins / Где собственно начинается реальная наука

**EN:** The interesting zone is **not** "wow, an anomaly". The interesting zone is:

> The effect is stable **but** not fully explained.

This is **not** an "anomaly". This is a **boundary of a model**. It is where existing theory has its edge, and it is where productive new work happens. A real new discovery does not look like a spectacular spike; it looks like a **strange but stable pattern**.

**RU:** Интересная зона — это **не** «ого, аномалия». Интересная зона — это:

> Эффект стабилен, **но** не полностью объяснён.

Это **не** «аномалия». Это **граница модели**. Это место, где существующая теория достигает предела, и именно там происходит продуктивная новая работа. Реальное новое открытие не выглядит как зрелищный всплеск; оно выглядит как **странный, но стабильный паттерн**.

---

## Honest summary / Честный итог

**EN:** Working at this level means searching not for spectacular effects or powerful flashes, but for **repeatability, parameter dependence, and structure**. Without those three, no signature — however striking — counts toward new physics.

**RU:** Работа на этом уровне означает поиск не зрелищных эффектов и не мощных всплесков, а **повторяемости, зависимости от параметров и структуры**. Без этих трёх ни одна сигнатура — какой бы яркой она ни была — не идёт в зачёт новой физики.

---

## Navigation / Навигация

- Sub-archive README / README подархива: [`../README.md`](../README.md)
- Signature methodology / Методология сигнатур: [`signature-methodology.md`](signature-methodology.md)
- Anomaly classification / Классификация аномалий: [`anomaly-classification.md`](anomaly-classification.md)
- UAP application / Применение к НАЯ: [`uap-application.md`](uap-application.md)
- Root README / Корневой README: [`../../README.md`](../../README.md)
