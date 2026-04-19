# TV-99 part 1/2 — Technical extract

**Source file:** `books/downloads/fb2_chunks/TV-99_part1of2.txt`
**Total size (part 1):** 741 417 UTF-8 chars (~1.35 MB).
**Source code:** `TV-99-p1` (parts merge → `B-TV99`).
**Book:** В.А. Чернобров — «Тайны Времени». Более полная версия книги, вышедшей в издательстве «Олимп» в 1999 году. Авторская электронная версия от 06.01.2000.
**Format of citations:** char-offset in the plain-text chunk (single long line). "≈X%" = X% of 741 417 chars.
**Cross-reference tag:** `USER-RES-2026-04-18` (perplexity-research/03_user_provided_research_2026-04-18.md §1).

---

## 0. Dedication / bibliographic framing (RU verbatim)

> «Герберту УЭЛЛСУ, Феликсу ЗИГЕЛЮ, Николаю КО3ЫРЕВУ — посвящается» (offset ~930, ≈0.1% of chunk).
- EN: "Dedicated to H. Wells, F. Zigel, N. Kozyrev."
- Editor's note: "Более полная версия книги «Тайны Времени», вышедшей в издательстве «Олимп» в 1999 году. Авторская электронная версия от 6.01.2000" (offset ~820). → **USER-RES §1 confirms:** publisher "АСТ-Олимп, 1999, 416 стр." Here the electronic author-version is dated 06.01.2000, which is newer than the first 1993 самиздат and the 1999 «Олимп» print.

---

## 1. Устройство (Ловондатр) — construction

Dense bloc around offset **700 500 … 716 000** (≈94.5% – 95.8% of chunk). This is the single longest technical passage in Part 1. Key verbatim claims:

### 1.1 Name & assembly/first-run dates (offset 701 241, ≈94.6%)
> «Первая модель МВ „Ловондатр“ была закончена 7 апреля, заработала же она 8 апреля 1988 года, тогда же были получены первые, более чем скромные, результаты.»
- EN: "The first MT model 'Lovondatr' was finished on April 7, started to work on April 8, 1988; at that time the first — extremely modest — results were obtained."
- **USER-RES §1 alignment (confirmed):** "сборка закончена 7 апреля 1988 г., заработала 8 апреля 1988 г."
- Name etymology (same block, offset ~701 800): cover story told to the shop foreman was a "ловушка для ондатр" (muskrat trap) → hence "Ловондатр". Official classification: «Экспериментальная электромагнитная ловушка для ловли ондатр» (offset ~702 280).

### 1.2 First public report — 12 April 1991 (offset ~701 930, ≈94.7%)
> «…первый весьма популяризированный „репортаж с места события“ вскоре опубликовала газета МАИ, произошло это в день 30-летия первого полета человека в космос и в день ставшего знаменитым таинственного сасовского взрыва. [2]08.»
- EN: "The first popularized 'on-the-spot report' was soon published by the MAI newspaper, on the 30th anniversary of the first manned spaceflight and the day of the famous mysterious Sasovo explosion."
- 30-year anniversary of Gagarin's flight = **12 April 1991** (USER-RES §9 confirms).

### 1.3 Institutional collaborators (offset ~700 730, ≈94.5%)
> «В создании установки большую добровольную помощь оказали некоторые специалисты Московского Авиационного Института им.Орджоникидзе, завода им.Хруничева, НПО „Салют“, НПО „Энергия“, других организаций и отдельные изобретатели и специалисты в самых различных областях. Надо оговориться сразу — далеко не все знали конечную цель работы, и, как правило, энтузиасты помогали внедрению новой „приставки к ракетному двигателю“, новой „сверхмощной всенаправленной антенной“ и т.д.»
- EN: Voluntary participation of specialists of MAI (Moscow Aviation Institute n.a. Ordzhonikidze), Khrunichev plant, NPO "Salyut", NPO "Energia" — most of them were not told the real goal; they believed they were helping to develop a "supplement to a rocket engine" or "super-powerful omnidirectional antenna."
- **USER-RES §1 alignment (confirmed):** "при поддержке специалистов МАИ, завода им. Хруничева, НПО «Салют» и НПО «Энергия»."
- **New-to-us detail:** the institute is named in full — «Московский Авиационный Институт им.Орджоникидзе» (MAI n.a. Ordzhonikidze).

### 1.4 Generations (4 in 5 years) — offset ~706 875 (≈95.3%)
> «Всего же за 5 лет было сделано 4 экспериментальных установки МВ разной степени сложности (в настоящий период строятся две следующие)…»
- EN: "Four experimental MT installations of different complexity were built in 5 years; two more are presently under construction."
- **USER-RES §1 alignment (confirmed):** «За пять лет (1988–1993) созданы четыре экспериментальные установки».

### 1.5 Size of максимальной / минимальной ЭРП (offset 705 049 / 705 126, ≈95.1%)
> «Размер максимальной ЭРП в первой установке составлял около 1 м, диаметр минимальной (внутренней) ЭРП равнялся 115 мм, что оказалось достаточным для помещения внутрь датчиков контроля и подопытных животных…»
- EN: "The outer ERP in the first installation was ~1 m, the innermost ERP was 115 mm in diameter — enough for control sensors and test animals (insects and lab mice)."
- **SPECIFIC NUMBERS:** outer ERP ~ **1 m**; inner ERP = **115 mm**.
- **USER-RES §6 alignment:** "внешняя ЭРП — до 0,9 м; внутренняя — 115 мм" (from 2003 Faraday paper). The 115 mm figure is already established in 1999 TV-99 Part 1.

### 1.6 Number of ERP layers (offset 704 753, ≈95.0%)
> «…чечевицеобразный или шаровидный корпус с укрепленным на нем множеством электромагнитов, соединенных между собой последовательно и параллельно. В различных экспериментах использовалось от 3 до 5 таких поверхностей, названных электромагнитными рабочими поверхностями (ЭРП). Все слои ЭРП различных диаметров монтировались последовательно друг в друге (подобно матрешке). Внешний слой либо крепился на силовую оболочку, либо одновременно сам являлся такой оболочкой.»
- EN: "Lens-shaped or spherical body with many electromagnets connected in series and parallel. 3–5 such surfaces were used, called electromagnetic working surfaces (ERP). ERP layers of different diameters were mounted one inside another (like a matryoshka). The outer layer was either attached to the load-bearing shell or was itself the shell."
- **SPECIFIC NUMBERS:** ERP count = **3 to 5** layers.
- **USER-RES §1 alignment (confirmed):** "чечевицеобразные аппараты с замкнутой пространственной конструкцией... матрёшки слои плоских электромагнитов, скрученных в виде эллипсоидов."
- **Author's acronym ЭРП** is introduced explicitly (offset 704 832) as *«электромагнитная рабочая поверхность»*.

### 1.7 Canonical mandatory subsystems (offset ~705 540, ≈95.2%)
> «Все наши экспериментальные аппараты, с виду кстати напоминающие НЛО, в обязательном порядке включали в себя: замкнутую пространственную конструкцию с особыми электромагнитными свойствами, блок управления, блок питания и измерительную аппаратуру; на некоторых модификациях отдельно обкатывались и другие системы.»
- EN: "All our experimental apparatuses — which resembled UFOs — necessarily included: a closed spatial construction with special EM properties, a control unit, a power unit, and measurement equipment; on some modifications other systems were separately tested."
- **USER-RES §1 alignment (confirmed):** "замкнутой пространственной конструкцией, блоком управления, блоком питания и измерительной аппаратурой."

### 1.8 Payload compartment (offset 712 023, ≈96.0%)
> «Объем отсека полезной нагрузки, находящейся в центре симметрии МВ, во всех Машинах не превышал объема футбольного мяча.»
- EN: "The payload compartment volume, at the MT's center of symmetry, in all Machines did not exceed the volume of a football (soccer ball)."
- **USER-RES §1 alignment (confirmed):** "объём отсека полезной нагрузки — не превышал объёма футбольного мяча."
- Term coined: «полезная нагрузка (ПН)», «термин ПН введен по аналогии с аналогичным термином в космонавтике» (offset ~711 980).

### 1.9 ERP material design vision (post-1999 target) — offset ~721 500 (≈97.4%)
> «Делать оболочку придется с помощью молекулярных (атомных) технологий на основе новых композитных материалов со слоями электромагнитов из перспективного нитевидного сверхпроводящего полимера Литтла (рабочая температура ожидается до 2400 градусов К!), либо из другого горячего сверхпроводника.»
- EN: "The shell will have to be built with molecular (atomic) technologies, on new composites with EM layers made from the prospective filamentary superconducting Little polymer (operating T up to 2400 K!) or another high-T superconductor."
- **SPECIFIC NUMBER:** expected operating T up to **2400 K**; material = "нитевидный сверхпроводящий полимер Литтла" (Little's filamentary superconducting polymer).
- **New-to-us fact** (not in USER-RES §1): the TV-99 Part 1 already names "Little's filamentary superconducting polymer" as the target material class for future MT shells.

---

## 2. Принципы работы

### 2.1 EM-field configuration definition — offset 706 402 (≈95.3%)
> «Нужную конфигурацию электромагнитных полей создавала электромагнитная рабочая поверхность (ЭРП) — вложенные друг в друга по принципу матрешки слои плоских электромагнитов, скрученных в виде эллипсоидов.»
- EN: "The required EM-field configuration was produced by the electromagnetic working surface (ERP) — matryoshka-nested layers of planar electromagnets rolled into ellipsoid shapes."
- **USER-RES §1 alignment (confirmed exactly):** wording is essentially the same sentence USER-RES reproduces.

### 2.2 Control / tunability — offset ~706 550 (≈95.3%)
> «Режим работы, задаваемый блоком управления, мог быть самым разнообразным, для каждой модели МВ можно было подобрать целые области благоприятных соотношений частот, напряженности и режима переключения, среди которых конечно же были и наиболее оптимальные…»
- EN: "The operating regime, set by the control unit, was highly variable — for each MT model there existed whole regions of favorable ratios of frequency, field strength, and switching regime; optimal regions existed within these."
- **SPECIFIC NUMBERS (qualitative):** tunable parameters = frequency, field-strength amplitude, switching mode.

### 2.3 3-sphere induction scheme & gravitational target — offset ~707 020 (≈95.4%)
> «Исследовались несколько вариантов конфигураций полей, в том числе и такой, при котором путем последовательного наведения в системе из 3 сфер можно было добиться вращения силовых линий магнитного и электрического полей, находящихся под прямым углом друг к другу. Цель — посредством этих двух видов полей попытаться управлять 3 составляющей поля, предположительно гравитационной…»
- EN: "Several field configurations were tested, including one where sequential induction in a 3-sphere system produced rotation of the magnetic and electric field lines at right angles to each other. The goal — via these two field types, try to control a 3rd field component, presumably gravitational."
- **SPECIFIC NUMBERS:** a **3-sphere** system; **E ⊥ B** with rotating lines; the 3rd component is assumed **gravitational**.
- **New-to-us detail** not in USER-RES §1: explicit "вращения силовых линий магнитного и электрического полей, находящихся под прямым углом" → the author explicitly frames this as a crossed-E×B rotating-lines geometry aimed at producing a gravitational component.

### 2.4 Dual-purpose shell (MT + propulsion) — offset ~721 220 (≈97.3%)
> «В реальных летательных аппаратах будущего достаточно будет соорудить всего одну многослойную оболочку ЭРП, а затем в полете лишь переключать ее для работы в режиме МВ, либо в режиме полевого двигателя для создания тяги. Можно и совместить оба режима работы, доведя частоту таких переключений до нескольких сот в секунду.»
- EN: "In real future flying craft one multilayered ERP shell will suffice — during flight it will be switched between MT mode and field-propulsion mode. Both modes can be combined by increasing the switching frequency to several hundred per second."
- **SPECIFIC NUMBER:** mode-switching frequency **≈ several hundred Hz**.
- **New-to-us detail:** the "several hundred Hz" number is mapped to UFO observational data in the next passage.

### 2.5 UFO emission parameters linked to MT mode-switching — offset ~727 700 and ~733 360 (≈98.2%, ≈98.9%)
> «Американские самолеты радиоэлектронной разведки не раз фиксировали излучение, идущее от летящих НЛО (чаще всего сообщается, что такое излучение имеет частоту 3000 МГц с повторением 600 импульсов/с).»
- EN: "US ELINT planes recorded radiation from flying UFOs (most often reported: frequency 3000 MHz, repetition 600 pulses/s)."
- **SPECIFIC NUMBERS:** **3000 MHz** carrier, **600 pulses/s** repetition.
> «…переключать с большой частотой режимы работы (до нескольких сотен раз за секунду; узнаете зафиксированные параметры в 3000 Мгц и 600 имп[ульсов]…»
- EN: "…switch the modes at high frequency (up to several hundred per second; recognize the recorded parameters of 3000 MHz and 600 pulses/s)."
- Chernobrov explicitly ties the "600 pulses/s" UFO signature to the proposed MT mode-switch rate.
- **Other cited frequency (offset 679 775, ≈91.7%):** context of Y. Kunyansky's contactee claim — «3 генератора сообща в соотношении 1:0,5:0,25 создали частоту излучения 3,3 ГГц.» This is reported 2nd-hand (contactee), not Chernobrov's experiment. EN: "3 generators together in 1:0.5:0.25 ratio generate 3.3 GHz radiation."

### 2.6 Open-schema creates thrust — offset ~721 100 (≈97.3%)
> «Но уже сейчас эксперименты подтвердили возможность использования МВ с разомкнутой схемой для создания подъемной силы в НЛО-подобных аппаратах: 400-граммовая модель показала тягу 10 г. [2]12…»
- EN: "Already the experiments have confirmed that an MT with open schema can create lift for UFO-like craft: a 400-gram model produced a 10-g thrust."
- **SPECIFIC NUMBERS:** model mass **400 g**, demonstrated thrust **10 g (force)**.
- **USER-RES §1 alignment (confirmed):** "30 апреля 1991 г. — новая модификация МВ с разомкнутой схемой; показана тяга ~10 г при 400-граммовой модели." Exact match.

### 2.7 Broadcast-through-time test 30 April 1991 — offset ~720 400 (≈97.1%)
> «Когда 30 апреля 1991 года заработала новая модификация МВ, то с самого начала ее режим работы был промодулирован таким образом, чтобы передать закодированное послание к тем, кто сможет получить его. В конце переданного текста стояла просьба через 5 минут подтвердить факт получения передачи. И вот, секунда в секунду в зените появился наш старый знакомый!»
- EN: "When the new MT modification started on April 30, 1991, its regime was modulated from the start to transmit a coded message to whoever could receive it. The text ended with a request to confirm reception after 5 minutes. Second-by-second, our old acquaintance (the 'three-beacon' UFO) appeared at the zenith on cue."
- **SPECIFIC NUMBER:** 5-minute ack-wait.
- Reinforces 30 April 1991 as the second-generation open-scheme début.

---

## 3. Измерения (Measurement methods & results)

### 3.1 Instrument stack — offset ~707 600 (≈95.4%)
> «ИЗМЕРЕНИЕ ТЕМПА ХОДА ВРЕМЕНИ проводилось всеми возможными известными современными способами измерения времени: использовались все виды электронных, кварцевых, механических, атомных часов; а также специально изготовленные дублированные кварцевые генераторы (в которых сравнивались показания частот измеряющего и эталонного разнесенных теплоизолированных генераторов); световодные диоды (в которых фиксировалось изменение в скорости прохождения светового пучка заданного участка световода) и иные способы. До и после опыта (а реже и в ходе опыта) ход измерительных часов периодически сравнивался с эталонными часами и сигналами точного времени по радио. Хотя на некоторые виды измерительных приборов, например на кварцевые часы, оказывали побочное влияние иные физические факторы, но дублирование методов измерения позволяло существенно уменьшить погрешность измерения…»
- EN: Measurement used **electronic, quartz, mechanical, and atomic clocks**; custom-built **twin thermally-isolated quartz-generator pairs** comparing measurement vs reference frequencies; **fiber-optic diode delay-line tests** (change in light-pulse transit time through a fixed fiber section); other methods. Instrument clocks were compared to reference and to radio time-signals before and after runs (sometimes during). Method duplication reduced error.
- **New-to-us detail** beyond USER-RES §1 generic "измерительная аппаратура": explicit **three orthogonal methods** — (a) traditional clocks incl. atomic, (b) dual thermally-isolated quartz-oscillator beat comparison, (c) fiber-optic light-pulse delay.

### 3.2 First-result numbers (quantitative) — offset ~708 130 (≈95.5%)
> «РЕЗУЛЬТАТ ПЕРВЫХ ЭКСПЕРИМЕНТОВ нас и огорчил, и порадовал, и озадачил. При некоторых режимах работы установки (не всегда предсказанных) достигалось изменение скорости течения Времени (то, что профессор Н.Козырев называл плотностью Времени t/tо) порядка долей секунд в эталонный земной час. Много это или мало? Для реальных МВ ничтожно мало, для начала — много.»
- EN: First-run time-rate change was "на уровне долей секунд в эталонный земной час" (fractions of a second per reference Earth hour).
- **USER-RES §1 alignment (consistent):** "разница в показаниях часов до 0,5 секунды в час" — the book phrasing is "порядка долей секунд в эталонный земной час" (on the order of fractions of a second per hour). **Note:** the explicit "0.5 s/hr" figure for the first model is not literally in this Part-1 passage; the book gives "до +0,5 с/ч ускорения" as a ceiling and "–1,5 с/ч замедления" — see §3.3 next. → **USER-RES alignment partial; the "0.5 s/hr" may be the specific +0,5 c/ч acceleration ceiling.**

### 3.3 Peak results — offset ~708 475 (≈95.5%)
> «И только в одном из опытов по не до конца понятным пока причинам замедление составило —4 минуты за 8 часов (30 секунд/час). В других опытах было зафиксировано и с точки зрения рабочей теории объяснено замедление темпа Времени до —1,5 с/ч и ускорение до +0,5 с/ч. Если принять наше обычное земное „эталонное“ Время как tо=+1, то станет понятным, что мы пока изучаем диапазон скорости Времени +0,99&lt;t/tо&lt;+1,01.»
- EN: "In one experiment, for still-unclear reasons, the slowdown reached **−4 min over 8 h (= −30 s/hr)**. In other experiments, slowdowns down to **−1.5 s/hr** and speed-ups up to **+0.5 s/hr** were recorded and theoretically explained. With Earth's reference time t₀ = +1, the operating range is **+0.99 < t/t₀ < +1.01**."
- **SPECIFIC NUMBERS:** single peak **−30 s/hr** (= −4 min / 8 h); routine slowdown **−1.5 s/hr**; routine speed-up **+0.5 s/hr**; envelope **±1%** of Earth's reference.
- **USER-RES §1 alignment (partial):** USER-RES says "последующие модификации — до 40 секунд в час"; the book's Part 1 gives **peak 30 s/hr**. → **POTENTIAL CONFLICT / number-refinement:** 40 s/hr may be a later (Part 2 / later-edition) revision; Part 1 of the 1999 edition caps the confirmed peak at 30 s/hr.
- **USER-RES §6 alignment (confirmed):** the **+0.99 < t/t₀ < +1.01** (±1%) envelope matches the 2003 Faraday paper exactly — already present in 1999 Part 1.

### 3.4 External field falls off as r⁻³ — offset ~710 660 (≈95.7%)
> «Во время экспериментов фиксировалось, как и ожидалось, изменение Времени и вне установки МВ, только подобное изменение с обратным знаком было примерно на порядок ниже внутреннего (вполне в соответствии с геометрическими законами — обратно пропорционально кубу расстояния).»
- EN: "Time-change outside the MT was detected, with opposite sign, roughly an order of magnitude smaller than inside, consistent with inverse-cube geometry."
- **SPECIFIC NUMBER:** external time-rate perturbation ∝ **1/r³**, opposite sign, ~×0.1 of internal.
- **USER-RES §6 alignment (confirmed):** matches the 2003 Faraday paper.

### 3.5 New units — offset ~709 200 (≈95.7%)
> «Поначалу пользовались размерностями измерения „милисекунд/сутки“ (с „плюсом“ или „минусом“), затем „с/сутки“, „с/ч“. По мере роста эффективности МВ, вероятно, в ход пойдут уже размерности типа „с/с“, „мин/с“, „ч/с“, „сутки/с“ и даже (страшно подумать!) „год/с“ и т.д.»
- > «Для простоты в экспериментах мы измеряли разницу в показаниях часов „внутри“ и „снаружи“, что можно было бы образно назвать „перепадом Времени“ — величиной, показывающей, на сколько секунд мы замедляем (ускоряем) Время внутри МВ за 1 секунду „забортного“ эталонного времени. В реальных МВ, возможно, удобнее будет пользоваться понятием безразмерной величины „скорости Времени“ (или „плотности Времени“, что, однако, одно и то-же, хотя и трудно представить „отрицательные плотности“). Эта величина показывает уже отношение между ходом внутреннего и внешнего (забортного) Времен и измеряется в „реальных секундах“, или сокращенно в „секреалях“…»
- EN: Early units = ms/day (±); later s/day, s/hr. Future scaling: s/s, min/s, h/s, day/s, year/s. Distinction: «перепад Времени» (Δt, dimensional) vs «скорость Времени» = «плотность Времени» = t/t₀ (dimensionless, measured in "секреалях" — "real seconds"). Negative "densities" hard to interpret.
- **New-to-us vocabulary:** **«секреали»** = "real seconds" = dimensionless t/t₀. Not present in USER-RES §1.

---

## 4. Результаты экспериментов

### 4.1 Test subjects — offset ~705 280 (≈95.1%) and offset ~712 330 (≈96.1%)
> «…использовались различные виды насекомых и лабораторные мыши…»
- EN: "Various insects and lab mice were used."
- Scope list confirmed: insects (book mentions тараканы elsewhere, p. ~23 388, in unrelated anecdote; lab mice are the primary vertebrate subjects in THE MT experiments) + lab mice.

### 4.2 Lethality threshold and the "1.5-sec" boundary — offset ~712 330 (≈96.1%)
> «Первые опыты с перемещением насекомых и мышей в прошлое Время закончились плачевно для подопытных (разницы в 1,5 секунды, увы, не пережил почти никто). У тех из людей, кто имел неосторожность находиться рядом с МВ, появились болезненные симптомы, аналогичные описанным в эксперименте с „Элдриджем“ (речь о них пойдет позже). Лишь после доработки схемы „испытатели“ перенесли процедуру перемещения. [2]09.»
- EN: "First experiments with moving insects and mice into the past Time ended tragically for the test subjects — a 1.5-second difference was survived by almost none. Humans incautious enough to stand near the MT developed symptoms similar to those described in the Eldridge experiment (covered later). Only after redesign did the 'testers' survive the procedure."
- **SPECIFIC NUMBER:** lethality threshold = **1.5 seconds** (not 2 s).
- **USER-RES §1 CONFLICT:** USER-RES says *"разница в 2 секунды — не пережил почти никто"*; the book says **1.5 секунды**. → **FLAGGED: USER-RES §1 vs TV-99 Part 1 — 2 s vs 1.5 s discrepancy.** This is a factual conflict to resolve (likely a USER-RES transcription/paraphrase error; the verbatim book number is 1.5 s).
- Note: the analog suggested is Eldridge (Philadelphia Experiment), i.e. human harm from edge-of-MT Δt, confirming author's position that symptoms track differential-Δt not absolute-Δt.

### 4.3 First survivor: mouse "Number Seven" — offset ~712 775 (≈96.1%)
> «Можно также добавить, что первой удачно перенесла опыт с замедлением Времени мышь „Номер Семь“. Радует то, что после завершения серии экспериментов она „на заслуженной пенсии“ прожила весь остаток своего мышинного века, что дает некоторую надежду на безопасный исход будущего эксперимента по перемещению во Времени человека…»
- EN: "The first to successfully survive a time-slowdown experiment was mouse 'Number Seven'. After the series she lived out the rest of her mouse life 'in deserved retirement', giving some hope for a safe future human experiment."
- **New-to-us detail:** named animal "мышь Номер Семь" (mouse #7) as the first survivor — not in USER-RES §1.

### 4.4 Qualitative asymmetry: slowdown vs speed-up — offset ~713 700 (≈96.3%)
> «Так, замедление происходило значительно более плавно и устойчиво; при ускорении наблюдались резкие скачки в показаниях, протекание этого режима характеризовалось общей неустойчивостью и зависимостью от любых внешних факторов. В частности, неустойчивость ускорения заключалась и в том, что при фиксированной мощности величина скорости Времени зависела от времени суток и расположения Луны, возможно, и от других причин, в том числе — от присутствия рядом оператора. Даже небольшое внешнее воздействие, например механическая тряска, приводили к изменению величины скорости, в том числе и к значительному.»
- EN: Slowdown = smooth, stable; speed-up = jumpy, unstable, depends on time-of-day, Moon position, operator presence, mechanical vibration.
- **USER-RES §5 alignment (confirmed):** this is exactly the "замедление плавное и стабильное; ускорение нестабильное, зависит от времени суток, фазы Луны, присутствия оператора, механических вибраций" finding that USER-RES §5 attributes to the 2001 Faraday paper. **NEW-TO-US:** this result was already present in 1999 TV-99 Part 1.

### 4.5 Inertia of time-change — offset ~715 900 (≈96.6%, truncated at chunk boundary)
> «Внутри лабораторных установок также было зафиксировано, что Время может изменяться с некоторой инерционностью. Участки пространства с различным Временем имеют между собой расплывчатые, нечетк[ие границы]…»
- EN: "Inside the lab setups it was recorded that Time can change with some inertia. Space regions with different Time have blurry, unclear boundaries between them."
- **USER-RES §6 alignment (confirmed):** the "inertial effect of time change" reported in the 2003 Faraday paper is already in 1999 Part 1.

### 4.6 3-light-beacon UFO overflight 18 March 1990 — offset ~718 700 (≈97.0%)
> «Поздним вечером 18 марта 1990 года во время испытаний установки улучшенной модификации в небе над МВ появился и стал описывать круги огромный НЛО с тремя „габаритными огнями“.»
- EN: "Late evening March 18, 1990, during tests of an improved-modification installation, a huge UFO with three 'navigation lights' appeared and began circling above the MT."
- Was captured by TV-crew "Добрый вечер, Москва" after ~30 min chase along the ring road.
- Linked by Chernobrov to a 1991-04-30 repeat (§2.7).

---

## 5. Теория

### 5.1 6-D / 7-D Space-Time — offset ~5 300 (≈0.7%)
> «Само Время, точнее, Пространство-Время, которое я считаю 6-мерной, а возможно, и 7-мерной субстанцией, древними издревле так или иначе… ассоциировалось с семеркой…»
- EN: "Time itself — more precisely Space-Time — which I consider to be 6-dimensional, and possibly 7-dimensional, was in antiquity one way or another linked to the number seven…"
- **USER-RES §1 alignment (confirmed):** "Пространство-Время — 6-мерная (возможно 7-мерная) субстанция."

### 5.2 Kozyrev's 7 properties (full verbatim) — offset ~10 327 (≈1.4%)
> «Он же в своих многочисленных работах по „причинно-следственной механике“ утверждал, что „Время обладает 7 свойствами“, которые и воспроизводим ниже. Время по-Козыреву:
> 1) взаимодействуя с веществом звезд, является источником их энергий;
> 2) обладает направленным ходом и плотностью;
> 3) поглощается и излучается материальными телами;
> 4) экранируется, заслоняется (стеклом, металлом) или отражается (зеркалом);
> 5) не преломляется;
> 6) не распространяется как свет, появляется сразу во всей Вселенной;
> 7) не является материальным носителем.»
- EN:
  1. interacting with stellar matter, is the source of stars' energy;
  2. has directional flow and density;
  3. is absorbed and emitted by material bodies;
  4. is shielded (glass, metal) or reflected (mirror);
  5. is not refracted;
  6. does not propagate like light — appears instantly throughout the Universe;
  7. is not a material carrier.
- **USER-RES §1 alignment (confirmed):** "Козырев: «причинно-следственная механика», 7 свойств Времени." The 7-property list is given verbatim in TV-99 Part 1.
- Additional attribution in same paragraph: similar 7-property list was transmitted to Uzbek ufologist **Михаил Сергеевич ЕЛЬЦИН** by alleged aliens (offset ~10 860).

### 5.3 Kozyrev's Sirius experiment summary — offset ~67 500 (≈9.1%)
> «…на звезду (чаще всего это был яркий Сириус, находящийся на расстоянии 8 световых лет от нас) наводился телескоп, в фокусе которого находился регистратор излучения (например, кварцевый генератор). Результат опыта: датчик зафиксировал излучение, пришедшее сразу из трех точек: 1) оттуда, где мы видим звезду сейчас и где она находилась 8 лет назад (скорость этого зафиксированного излучения равна обычной скорости света); 2) оттуда, где она находится сейчас на самом деле (скорость излучения чрезвычайно большая или мгновенная); 3) и из точки, где она будет через 8 лет!»
- EN: Kozyrev's telescope + quartz detector aimed at **Sirius (8 ly)** registered radiation from 3 points simultaneously: (1) past visible position (light-speed), (2) actual "now" position (near-instant speed), (3) position **8 years in the future**.
- **SPECIFIC NUMBER:** distance 8 ly; latency of source 2 = "near-instant"; source 3 = +8 y future.

### 5.4 Bartini 6-D / 3-D Time — offset ~716 920 (≈96.7%)
> «…можно считать косвенным образом доказанным, что Время имеет более чем 1 измерение, т.е. подтверждаются теоретические выкладки О.Бартини, считавшего, что Время имеет 3 измерения. Следовательно, наш земной мир можно считать 6-мерным, где измерениями соответственно являются: длина; ширина; высота; возраст или дата Времени; вариант истории или размытость Времени; плотность или скорость Времени.»
- EN: "It is indirectly proven that Time has more than 1 dimension — confirming O. Bartini's theory that Time has 3 dimensions. Hence our Earth world is 6-dimensional: length; width; height; **age/date of Time**; **variant of History / blurriness of Time**; **density/speed of Time**."
- **USER-RES §1 alignment (exact match):** "6D мир: 3 координаты пространства + 3 координаты Времени — дата, вариант Истории, плотность/скорость Времени."

### 5.5 Wheeler wormholes / Einstein-Rosen bridge placement — offset ~717 500 (≈96.8%)
> «Понятие „Стрелы времени“, таким образом, полностью отсутствует в четвертом измерении (дате Времени), но входит частным случаем в понятие шестого (скорости Времени), с которым одновременно также связаны физические понятия гравитации и энергии. Понятия „моста Эйнштейна-Розена“, введенное в 1916 году, или „червячного хода“, введенного в научный обиход Джоном УИЛЕРОМ в конце 1950-х годов, таким образом связаны с перемещением в 5-м и 6-м измерениях.»
- EN: The "Arrow of Time" is absent from the 4th dim (date) but is a special case of the 6th (speed of Time), which also connects gravity and energy. **Einstein-Rosen bridge (1916)** and **Wheeler's wormholes (late-1950s)** relate to movement in the 5th and 6th dimensions.
- **SPECIFIC DATES:** 1916 (Einstein-Rosen); late-1950s (Wheeler).

### 5.6 Non-material substrate for NLO influence — offset ~690 800 (≈93.2%)
> «Полученные данные также позволили предположить, что по крайней мере у части этих объектов не что-нибудь, а именно их оболочка влияет на темп и направление хода Времени…»
- EN: "Data suggest that for at least some of these objects (UFOs), it is precisely their **shell** that affects the tempo and direction of Time."
- Directly links the 1987-start "моделирование причинно-следственных связей" to the ERP-shell architecture of the Lovondatr (§1.6).

### 5.7 A. Weinik, E. Kamenkov, F. Zigel — precursor work — offset ~688 300 (≈92.8%)
> «Начиная с 1967 года в Московском авиационном институте им.Орджоникидзе под руководством профессора Феликса Юрьевича ЗИГЕЛЯ и до 1987 года (когда Зигель уже болел) проводились исследования техногенных НЛО. Благодаря этому при выполнении работ по открытой госбюджетной теме „Предварительные исследования аномальных явлений в атмосфере“ был накоплен целый массив разрозненных и классифицированных сведений об этом явлении. Целый ряд талантливых маевских сотрудников, среди которых был и мой будущий научный руководитель профессор Евгений Федорович КАМЕНКОВ, в 1970-х годах занимались тем, что просчитывали динамические, прочностные, энергетические и прочие характеристики НЛО.»
- EN: Since 1967, at MAI n.a. Ordzhonikidze, under Prof. **F.Yu. Zigel's** leadership until 1987 (when he became ill), research into "technogenic UFOs" was done under the open-budget topic **"Preliminary studies of atmospheric anomalous phenomena"**. In the 1970s, Prof. **E.F. Kamenkov** (Chernobrov's future scientific supervisor) and others calculated dynamical, strength, and energetic parameters of UFOs.
- **New-to-us detail** (not in USER-RES §1): Chernobrov's scientific supervisor at MAI was named as **Prof. Evgeniy Fedorovich Kamenkov**; predecessor-topic official code-name "Предварительные исследования аномальных явлений в атмосфере" since 1967 under F.Yu. Zigel.

### 5.8 Start-of-modeling 1987 — offset ~690 400 (≈93.1%)
> «И с 1987 года начались наши первые попытки моделирования причинно-следственных связей и физических процессов, происходящих с НЛО, всех процессов, что были достоверно зафиксированы при изучении следов, обломков, а также кино-, фото— и телеметрических изображений этих объектов.»
- EN: "From 1987 our first attempts began to model cause-and-effect relations and physical processes of UFOs — all processes reliably captured from traces, debris, film-, photo-, and telemetric imagery."
- Theory-work starts **1987**, build-start **1988**. Matches USER-RES §1 chronology.

### 5.9 Date aphorism (physical exper. start) — offset ~8 569 (≈1.2%)
> «…эксперименты непосредственно с лабораторным прототипом Машины Времени стартовали 7-ю месяцами позже в ночь с 7 на 8 мая 1988 года. Ну а перелом в проведении опытов наступил в 1997-м…»
- EN: "Experiments directly with the lab prototype of the Time Machine started 7 months later, on the night of 7–8 May 1988. The breakthrough came in 1997."
- **USER-RES §1 alignment (confirmed):** "Первые опыты по изменению хода Времени стартовали в ночь с 7 на 8 мая 1988 года."
- **⚠ INTERNAL NOTE:** here the author gives the **night of 7→8 MAY 1988**, yet in §1.1 he states **7–8 APRIL 1988** for the machine itself. Chernobrov's interpretation: 7/8 April = Lovondatr first-run of the device; 7/8 May = full "experiments on changing Time's flow" started a month later (i.e. after iterative commissioning and tuning). USER-RES §1 slightly blurs these two moments — USER-RES ambiguously says "ночь с 7 на 8 мая 1988" for "первые опыты по изменению хода Времени" AND "8 апреля 1988" for "первая модель заработала". The book separates them: machine first-run 8 April vs proper time-change-experiments 7/8 May.

---

## 6. История (chronology distilled from Part 1)

| Date | Event | Offset |
|---|---|---|
| 1916 | Einstein–Rosen bridge introduced | ~717 640 |
| late-1950s | Wheeler introduces wormholes | ~717 700 |
| 1967 | MAI Ordzhonikidze — "Preliminary studies of atmospheric anomalous phenomena" topic starts under F.Yu. Zigel | ~688 450 |
| 1970s | E.F. Kamenkov et al. compute UFO dynamics/energetics at MAI | ~688 900 |
| 1987 | Chernobrov begins modeling UFO cause-and-effect relations → MT concept | ~690 400 |
| 1987 Oct | 7 months before 7/8 May 1988 — theoretical work begins in earnest | ~8 569 |
| **7 April 1988** | Lovondatr-1 assembly finished | 701 267 |
| **8 April 1988** | Lovondatr-1 first run, first modest results | 701 295 |
| **Night of 7/8 May 1988** | Full time-rate-change experiments begin | 8 569 |
| **18 March 1990** | 3-beacon UFO sighting above improved-modification MT; filmed by "Добрый вечер, Москва" TV crew | 718 700 |
| 12 April 1991 | First MAI newspaper public report on Lovondatr (30th anniversary of Gagarin flight; same day as Sasovo explosion) | 701 930 |
| **30 April 1991** | New open-scheme MT modification first run; coded 5-min challenge to UFOs; 400 g model → 10 g thrust | 720 400 + 721 100 |
| 1993 | Book "Тайны Времени" first self-pub, small print run | 8 700 |
| Nov 1996 | A. Weinik dies; last met Chernobrov 1996 | 670 500 |
| 1997 | "breakthrough" year in experiments | ~8 680 |
| 1999 | AST-Olimp 1st published edition of "Тайны Времени" | ~820 |
| 06 Jan 2000 | Author's electronic version (this text) | ~830 |

---

## 7. Безопасность

### 7.1 The lethality sentence (definitive phrasing)
- See §4.2 above — book says **1.5 seconds differential** not "2 seconds" as in USER-RES.
- Verbatim: *«разницы в 1,5 секунды, увы, не пережил почти никто»* (offset ~712 470).
- Adjacent: *«болезненные симптомы, аналогичные описанным в эксперименте с „Элдриджем"»* → symptoms analogous to Philadelphia Experiment on humans standing near operating MT.

### 7.2 Harm mechanism — offset ~715 440 (≈96.5%)
> «Обнаружено также, что вредное воздействие на организм производит не сам процесс перемещения во Времени, а разница скорости изменения Времени на различных участках тела.»
- EN: "It was discovered that harm to the organism is caused not by the process of Time-shift itself, but by the **difference in the rate of Time-change between different parts of the body**."
- **Key safety principle:** gradient-Δt across body, not absolute Δt, is the damage driver. **Design consequence:** payload must fit inside uniform-field core (footnote: "football-sized" compartment).
- **USER-RES §1 alignment:** USER-RES only mentions aggregate "не пережил почти никто" without this differential-gradient mechanism. **→ New-to-us nuance.**

### 7.3 Bystander harm — offset ~712 605 (≈96.1%)
> «У тех из людей, кто имел неосторожность находиться рядом с МВ, появились болезненные симптомы, аналогичные описанным в эксперименте с „Элдриджем"…»
- EN: "Those humans who were careless enough to stand near the MT developed symptoms similar to those of the 'Eldridge' experiment…"

### 7.4 X-ray/radiation hazard (linked to UFO-mode) — offset ~738 800 (≈99.6%)
> «Откуда взялось рентгеновское излучение и почему его видит человеческий глаз? До и после луча Времени это страшное излучение было и вновь стало безобидным солнечным видимым светом. (А рентгеновские лучи, следовательно, — это еще одна опасность для свидетелей!?).»
- EN: "Where did the X-ray come from and why does the human eye see it? Before and after the Time-beam, that terrible radiation was ordinary harmless visible sunlight. (X-rays therefore are another hazard for witnesses!)"
- Hypothesis: Time-compression turns visible light into X-rays in the near field. **Hazard warning** to witnesses.

### 7.5 General "fear the strange fogs" — offset ~740 630 (≈99.9%)
- Chapter title: «Время и техника безопасности: БОЙТЕСЬ СТРАННЫХ ТУМАНОВ!!!» (Time and safety: FEAR THE STRANGE FOGS!!!).
- Link: the "белый туман"/"странная дымка" visual signature of the altered-Time zone is the primary field-safety alarm (matches USER-RES §5 "введён термин 'белый туман'").

---

## 8. UAP/НЛО связь (UFO connection as foundation of principle)

### 8.1 Explicit architectural borrowing — offset ~728 400 (≈98.2%)
> «Электромагнитная рабочая поверхность (ЭРП, использовавшаяся в наших экспериментах), создающая мощные электромагнитные поля оболочка, — это же отличительная черта аппарата МВ! Эксперименты, напомню, показал[и]…»
- EN: "The ERP used in our experiments — a shell that creates powerful EM fields — is a characteristic feature of the MT apparatus! The experiments, I remind you, showed [it matches UFO observations]."
- Explicit statement: ERP architecture is **both** our MT design AND what we observe in UFOs.

### 8.2 UFO as MT: ports are engines, not windows — offset ~731 150 (≈98.6%)
> «Иллюминаторы на эллипсоидах чаще всего не являются „окнами для обзора“, это — основной движитель объекта. Такой же как „шары“ на днищах НЛО. Вся разница между ними в количестве (шаров чаще всего бывает 3 штуки, реже — 4, 6 или 9) и мощности.»
- EN: "'Portholes' on ellipsoids are mostly not viewing windows — they are the main propulsor of the craft. Same as the 'spheres' on the UFO belly. Difference: count (usually 3, sometimes 4, 6 or 9) and power."
- **SPECIFIC NUMBERS:** 3 (most common), 4, 6, or 9 sphere-drives; minimum 3 for stabilization.

### 8.3 UFO 3-mode propulsion — offset ~732 700 (≈98.8%)
> «Во время полета НЛО применяет три режима полета: только во Времени, только в Пространстве (частота излучения двигателя при этом порядка тысяч МГц), одновременно во Времени и Пространстве (о других возможных режимах пока умолчим).»
- EN: UFOs fly in 3 modes: pure-Time, pure-Space (engine RF ~thousands of MHz), combined Time+Space. Combined = alternate with "several hundred times per second" switching (ties to §2.4/§2.5).

### 8.4 Transparency under X-ray, engine stop, paralysis, weight-loss — offset ~738 800+ (≈99.6%)
A rapid-fire list of UFO-proximity phenomena explained via MT physics:
- "прозрачными" objects in beam ⇒ X-ray blue-shifted visible light (§7.4)
- car engine stop ⇒ "изменение значения электрического сопротивления материалов" (resistance change of materials in altered-Time field)
- lightness sensation ⇒ speed-up of Time → impulse increase + apparent g reduction
- paralysis / stiffness ⇒ slowdown mode
- painful effects ⇒ non-uniform rates across body (§7.2)
- "instant appearance/disappearance" ⇒ MT propulsion at >20 g undetectable ⇒ teleportation candidate.
- **SPECIFIC NUMBER:** "ускорение свыше 20 g для стороннего наблюдателя абсолютно неуловимо" (offset ~740 060).

### 8.5 Landing-sites as hints — offset ~240 471+ (≈32.4%+)
Chunk contains extensive discussion of Medveditskaya gryada, landing spots of UFOs, but the explicit "50 mest posadok" figure from USER-RES §1 is not located in Part 1 with that exact number; what Part 1 provides is a qualitative census:
> «…только на территории России таковых несколько сотен. На нескольких десятках из них мы пробовали проводить хроноизмерения, и примерно в половине случаев точнейшие часы начинали „врать" самым явным образом.» (offset ~33 910, ≈4.6%)
- EN: "in Russia alone there are several hundred such places. On several dozen we tried hronoizmereniya (time-measurements); in roughly half the cases the most precise clocks began to 'lie' manifestly."
- **SPECIFIC NUMBERS:** several hundreds of chronal anomaly sites in Russia; ~several dozen measured; ~50% showed clock deviation.
- **USER-RES §1 "50 мест посадок":** Part 1 of TV-99 does not give a single "50" figure; the "ок. 50%" is a measurement hit-rate, not a site count. → **Minor USER-RES paraphrase drift** (not a hard conflict, but the "50" in USER-RES §1 likely derives from a different context / later section).

---

## 9. Персоны и институты

| Name | Role | Offset | Notes |
|---|---|---|---|
| Герберт УЭЛЛС | Dedicatee; "Машина Времени" (novel) | ~875 | Epigraph + many refs |
| Феликс Юрьевич ЗИГЕЛЬ | Dedicatee; MAI professor, doc., headed UFO topic 1967–1987 | 8 213 / 106 098 / 688 450 | Chernobrov's senior predecessor at MAI |
| Николай Александрович КОЗЫРЕВ | Dedicatee; Pulkovo astronomer; "причинно-следственная механика" & 7 properties | 9 539 / 67 501 / 682 850 | Sirius experiment described ≈1.4%, 9.1%, 92.2% |
| Альберт (Виктор) Иосифович ВЕЙНИК | Cor.-member Belarus AoS; repeated Kozyrev; switched to religion; burned books; died Nov 1996 | 669 898 | Own chronal-field theory; denied MT possibility |
| Анатолий Федорович ОХАТРИН | Moscow physicist; repeated Kozyrev mirror-exp. | ~670 180 | Mentioned alongside Weinik |
| Михаил Сергеевич ЕЛЬЦИН | Uzbek-Asian contactee-ufologist; received 7-property list "from alien pilots" | 10 978 | |
| Прф. Евгений Фёдорович КАМЕНКОВ | MAI; Chernobrov's scientific supervisor; computed UFO dynamics 1970s | 688 900 | **NEW (not in USER-RES §1)** |
| МАИ им. Орджоникидзе | Full institution name | 688 449 / 700 750 | Ordzhonikidze version, not "Moscow Aviation Institute" bare |
| завод им. Хруничева | Manufacturing contributor | 29 516 / 700 792 | First mention in "Kursky with anomalous water" anecdote at offset 29 516, then as Lovondatr fabricator at 700 792 |
| НПО "Салют" | Collaborator on MT | 184 099 / 700 808 | |
| НПО "Энергия" | Collaborator; also mentioned re 'Ожерелье' pyramid-crystal exp. (Semenov, Aryakov, Osipov) | 269 400 / 700 821 | **NEW**: names **П.Ф. Арькова, В.Г. Осипова, Ю.П. Семенова (rukov. OKB Energia)** on unrelated "Ожерелье" experiment |
| Марина ПОПОВИЧ | Test pilot ("101 мировой и 126 всесоюзных рекордов"); **NOT cosmonaut Pavel Popovich** | 303 131 | USER-RES/Perplexity likely conflated Marina (test pilot) with cosmonaut Pavel — book explicitly names test pilot context (Як-25РБ, МиГ-21, Galaliy) |
| С.П. КОРОЛЕВ / ОКБ-1 | Royalty helicopter for Tunguska x-ray hunt (historical) | 109 866 / 109 932 | |
| Юрий Евгеньевич ЦИПЕНЮК | Researched pyramid time-density with Chernobrov; Egypt/Moscow | ~279 000 | **NEW** |
| Карл ГОЛОД / Александр ГОЛОД | Pyramid builder; 44-m pyramid near Moscow (1999) | ~269 800 | |
| академик Мишин | **NOT found** in Part 1 — USER-RES §1 attribution "академик Мишин" is likely from later book / article | — | **FLAGGED: USER-RES §1 references "академик Мишин" but TV-99 Part 1 has no hit** |

### Further named engineers/scientists (supporting cast in Part 1):
- **С.Т. КУРСКИЙ** — Khrunichev engineer, "water with ±energy" anecdote (offset 29 516).
- **В.В. МАШКОВ** — deputy chief engineer, "Taganrog Aviation" (offset 100 100).
- **Г.М. ГРЕЧКО** — future cosmonaut, Tunguska 1960s inspection on Korolev's helicopter (offset 110 500).
- **Ален К. ХОЛТ (NASA)** — cited as theoretically confirming MT possibility (offset ~674 000).
- **Джон УИЛЕР** — Wheeler, wormholes introducer (offset ~717 700).
- **Oberto BARTINI (О.)** — 3D-Time theorist (offset 716 926). Only 1 mention in Part 1.

---

## CROSS-REFERENCE SUMMARY (USER-RES §1 ↔ TV-99 Part 1)

| USER-RES §1 claim | TV-99 Part 1 status |
|---|---|
| Первые опыты 7/8 мая 1988 | ✅ offset 8 569 — exact match (but note book separates "7/8 April 1988 device first run" from "7/8 May 1988 first time-rate experiments") |
| Сборка 7 апреля 1988, запуск 8 апреля 1988 | ✅ offset 701 267 — verbatim |
| МАИ + Хруничев + Салют + Энергия | ✅ offset 700 730 — verbatim (+ MAI full name = im. Ordzhonikidze) |
| 4 установки за 5 лет (1988-1993) | ✅ offset 706 875 |
| Чечевицеобразные + матрёшка эллипсоидов | ✅ offset 704 566 / 706 400 |
| Первая модель: до 0,5 с/ч | ⚠ PARTIAL — book gives "порядка долей секунд/ч" and explicit ceiling +0,5 с/ч acceleration, max slowdown −1,5 с/ч, single peak −30 с/ч |
| Последующие модификации: до 40 с/ч | ❌ NOT IN PART 1 — Part 1 caps at −30 с/ч (−4 min/8 h) |
| Объём футбольного мяча | ✅ offset 712 023 — verbatim |
| "Разница в 2 секунды — не пережил почти никто" | ❌ **CONFLICT** — book says **1,5 секунды**, not 2 (offset 712 470) |
| 30.04.1991 разомкнутая схема, 400 г модель → 10 г тяга | ✅ offset 720 400 / 721 100 — exact numbers |
| Время = 6D (возможно 7D) | ✅ offset 5 300 |
| Козырев: причинно-следственная механика, 7 свойств | ✅ offset 10 327 — full verbatim list |
| Бартини: 6D = 3 простр. + 3 Врем. (дата, вариант Истории, плотность) | ✅ offset 716 926 — exact match |
| ЭРП = авторское сокращение | ✅ offset 704 832 |
| академик Мишин | ❌ NOT IN PART 1 |
| 50 мест посадок | ⚠ Part 1 instead reports "several hundreds of anomaly sites in Russia, several dozen measured, ~50% showed deviation" — the "50" figure may be a misreading |

---

## Flagged specific numerical claims (single-table)

| Quantity | Value | Offset (≈% of chunk) |
|---|---|---|
| MT device outer ERP diameter (1st unit) | ~1 m | 705 049 (95.1%) |
| MT device inner ERP diameter (1st unit) | 115 mm | 705 126 (95.1%) |
| # of ERP layers | 3–5 | 704 753 (95.0%) |
| Payload compartment volume | football-sized | 712 023 (96.0%) |
| # of MT installations built 1988-1993 | 4 | 706 875 (95.3%) |
| Future shell material operating T | up to 2400 K (Little polymer) | 721 500 (97.4%) |
| Open-scheme demo: model mass | 400 g | 721 180 (97.3%) |
| Open-scheme demo: thrust | 10 g (force) | 721 100 (97.3%) |
| Typical first-run Δt | fractions of s / hr | 708 200 (95.5%) |
| Peak slowdown (single run) | −4 min / 8 h = −30 s/hr | 708 450 (95.5%) |
| Routine slowdown max | −1.5 s/hr | 708 500 (95.5%) |
| Routine speed-up max | +0.5 s/hr | 708 510 (95.5%) |
| Time-rate envelope | +0.99 < t/t₀ < +1.01 | 708 700 (95.5%) |
| External field fall-off | ∝ 1/r³, opposite sign, ~×0.1 internal | 710 660 (95.7%) |
| Mode-switch frequency (design) | several hundred Hz | 721 220 (97.3%) |
| UFO emission frequency | 3000 MHz | 727 800 (98.2%) |
| UFO emission pulse rate | 600 pulses/s | 727 830 (98.2%) |
| Contactee "Kunyansky" MT freq. (2nd-hand) | 3.3 GHz @ 1:0.5:0.25 amp ratio, 3 generators | 679 775 (91.7%) |
| Time-gradient lethality threshold | 1.5 s differential | 712 470 (96.1%) |
| Undetectable-accel. threshold | >20 g | 740 060 (99.8%) |
| Kozyrev Sirius experiment distance | 8 ly | 67 500 (9.1%) |
| Kozyrev future-source offset | +8 y | 67 700 (9.1%) |
| Einstein-Rosen bridge | 1916 | 717 640 (96.8%) |
| Wheeler wormholes | late-1950s | 717 700 (96.8%) |
| MT project theory-start | 1987 | 690 400 (93.1%) |
| Lovondatr-1 assembly | 7 April 1988 | 701 267 (94.6%) |
| Lovondatr-1 first run | 8 April 1988 | 701 295 (94.6%) |
| Full time-rate experiments start | night 7/8 May 1988 | 8 569 (1.2%) |
| UFO 3-beacon overflight | 18 March 1990 | 718 700 (97.0%) |
| MAI newspaper 1st public report | 12 April 1991 | 701 930 (94.7%) |
| Open-scheme MT first run + 5-min ack | 30 April 1991 | 720 400 (97.1%) |
| Breakthrough year | 1997 | 8 680 (1.2%) |
| 1st print | 1993 (самиздат) / 1999 (АСТ-Олимп) | ~820 |
| Electronic author version | 06.01.2000 | ~830 |
