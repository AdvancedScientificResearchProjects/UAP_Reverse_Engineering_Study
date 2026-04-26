# Anomaly classification — five experimental cases / Классификация аномалий — пять экспериментальных кейсов

**EN:** Five experimentally documented cases used as concrete templates for non-standard signatures. For each case: setup, "ordinary" expected result, observed non-standard signature, physical interpretation, and the key insight that makes the case reusable.

**RU:** Пять экспериментально задокументированных кейсов в роли конкретных шаблонов для нестандартных сигнатур. По каждому кейсу: установка, «обычный» ожидаемый результат, наблюдаемая нестандартная сигнатура, физическая интерпретация и ключевой инсайт, делающий кейс пригодным для повторного применения.

---

## Case 1 — Atmospheric-pressure nanosecond plasma / Кейс 1 — Наносекундная плазма при атмосферном давлении

**EN:** Setup: ~5–20 ns pulses at tens of kV applied to air or nitrogen at atmospheric pressure. Ordinary expected result: a single breakdown event, broadband emission noise, brief flash. Observed non-standard signature: multi-pulse EM response (a comb of EM peaks within one nominal "shot"), narrow spectral lines uncharacteristic of a "dirty" plasma, and a delay between EM emission and the optical channel — light arrives *after* the EM signal. Physical interpretation: the plasma forms in stages, with a fast electron-driven process preceding a slower ion-driven process. Key insight: a single applied pulse can drive **several distinct phases inside the medium**.

**RU:** Установка: импульсы ~5–20 нс при десятках кВ, среда — воздух/азот при атмосферном давлении. Обычный ожидаемый результат: один пробой, широкополосный шум излучения, кратковременная вспышка. Наблюдаемая нестандартная сигнатура: многоимпульсный EM-отклик (гребёнка EM-пиков внутри одного номинального «выстрела»), узкие спектральные линии, не характерные для «грязной» плазмы, и задержка между EM-излучением и оптическим каналом — свет приходит *после* EM-сигнала. Физическая интерпретация: плазма формируется ступенчато — быстрый электронный процесс предшествует более медленному ионному. Ключевой инсайт: один поданный импульс может запускать **несколько фаз внутри среды**.

---

## Case 2 — Laser-induced breakdown / Кейс 2 — Лазерный пробой

**EN:** Setup: femtosecond or nanosecond laser focused into a solid target or into air. Well-studied area. Ordinary expected result: breakdown at the focal point with a localized plasma flash. Observed non-standard signature: (i) **filamentation** — instead of a point, a long thin channel; (ii) a **self-sustaining channel** that persists longer than the driving laser pulse; (iii) a hybrid spectrum — broadband continuum coexisting with narrow lines simultaneously. Physical interpretation: self-focusing in the nonlinear-optical regime, with the formed plasma further amplifying the field and locking the channel in. Key insight: **energy does not stay where the experimenter "placed" it** — the medium reshapes the energy deposition geometry.

**RU:** Установка: фемто- или наносекундный лазер, сфокусированный в твёрдую мишень или в воздух. Хорошо изученная область. Обычный ожидаемый результат: пробой в фокусе и локализованная вспышка плазмы. Наблюдаемая нестандартная сигнатура: (i) **филаментация** — вместо точки — длинный тонкий канал; (ii) **самоподдерживающийся канал**, живущий дольше задающего лазерного импульса; (iii) гибридный спектр — широкополосный континуум сосуществует с узкими линиями одновременно. Физическая интерпретация: самофокусировка в режиме нелинейной оптики; образующаяся плазма дополнительно усиливает поле и фиксирует канал. Ключевой инсайт: **энергия не остаётся там, куда её «поместил» экспериментатор** — среда сама переформировывает геометрию энерговклада.

---

## Case 3 — Dielectric-barrier discharge / Кейс 3 — Диэлектрический барьерный разряд

**EN:** Setup: a series of nanosecond-spaced pulses applied across an electrode pair separated by a dielectric layer. Ordinary expected result: each pulse independently produces a breakdown across the gap. Observed non-standard signature: (i) **system memory** — pulse 1 weak, pulse 2 stronger, pulse 3 stronger still, the response builds up; (ii) **spatial localization** — successive discharges follow the same pre-existing channel geometry; (iii) **chaos → structure** — the discharge starts random and locks into a stable pattern after a few pulses. Physical interpretation: residual ionization, surface charge accumulation on the dielectric, and a "prepared medium" effect. Key insight: the system **remembers prior states** — the response to a pulse is a function of the pulse history, not just the present pulse.

**RU:** Установка: серия импульсов с наносекундными интервалами, поданная на пару электродов, разделённых диэлектриком. Обычный ожидаемый результат: каждый импульс независимо вызывает пробой в зазоре. Наблюдаемая нестандартная сигнатура: (i) **память системы** — импульс 1 слабый, импульс 2 сильнее, импульс 3 ещё сильнее, отклик нарастает; (ii) **пространственная локализация** — последовательные разряды идут по одной и той же ранее проложенной геометрии каналов; (iii) **хаос → структура** — разряд начинается случайно и через несколько импульсов фиксируется в устойчивом паттерне. Физическая интерпретация: остаточная ионизация, накопление поверхностного заряда на диэлектрике, эффект «подготовленной среды». Ключевой инсайт: система **запоминает предыдущие состояния** — отклик на импульс есть функция истории импульсов, а не только текущего импульса.

---

## Case 4 — Pulse power into solid materials / Кейс 4 — Pulse-power в твёрдых материалах

**EN:** Setup: nanosecond-scale current pulse driven through a solid sample. Ordinary expected result: a smooth conductivity response governed by the bulk material properties. Observed non-standard signature: (i) a **conductivity jump** — low → abruptly high; (ii) a **threshold delay** — the effect is not instantaneous, there is a lag before the jump; (iii) **spiky noise** in place of a clean signal — the trace is ragged with sub-pulses. Physical interpretation: micro-breakdowns inside the bulk, localized heating, and likely transient phase transitions in the solid. Key insight: in a "homogeneous" solid the regime can be **dominated by sub-microscopic events** that the macroscopic measurement only sees as a jump and noise.

**RU:** Установка: наносекундный токовый импульс, пропускаемый через твёрдый образец. Обычный ожидаемый результат: гладкий отклик проводимости, определяемый объёмными свойствами материала. Наблюдаемая нестандартная сигнатура: (i) **скачок проводимости** — низкая → резко высокая; (ii) **задержка порога** — эффект не мгновенный, есть лаг до скачка; (iii) **шум с пиками** вместо чистого сигнала — трек «рваный», с под-импульсами. Физическая интерпретация: микропробои внутри объёма, локальный нагрев, вероятные транзиентные фазовые переходы в твёрдом теле. Ключевой инсайт: в «однородном» твёрдом теле режим может **определяться субмикроскопическими событиями**, которые макроизмерение видит лишь как скачок и шум.

---

## Case 5 — RF / microwave pulse interaction / Кейс 5 — Взаимодействие RF / микроволновых импульсов

**EN:** Setup: short microwave pulses interacting with a plasma or a nonlinear material. Ordinary expected result: linear reflection/transmission with output frequency equal to input frequency. Observed non-standard signature: (i) the **reflected signal is no longer equal to the input** — its amplitude or shape is altered; (ii) **new frequencies are generated** (f → f₁ + f₂ + …); (iii) **shot-to-shot instability** — each pulse produces a different output. Physical interpretation: the medium itself is nonlinear and its properties are being modulated by the interaction in real time. Key insight: at this regime the **medium is no longer a passive scatterer** — it becomes part of the signal-generation process.

**RU:** Установка: короткие микроволновые импульсы, взаимодействующие с плазмой или нелинейным материалом. Обычный ожидаемый результат: линейное отражение/прохождение, выходная частота равна входной. Наблюдаемая нестандартная сигнатура: (i) **отражённый сигнал больше не равен входу** — изменена амплитуда или форма; (ii) **генерируются новые частоты** (f → f₁ + f₂ + …); (iii) **нестабильность от выстрела к выстрелу** — каждый импульс даёт разный выход. Физическая интерпретация: сама среда нелинейна, и её свойства модулируются взаимодействием в реальном времени. Ключевой инсайт: в этом режиме **среда перестаёт быть пассивным рассеивателем** — она становится частью процесса генерации сигнала.

---

## Common pattern across all five cases / Общий паттерн всех пяти кейсов

**EN:** All five cases co-instantiate the same four conditions: a fast pulse, a nonlinear medium, a multi-channel response, and a system that has memory or history. Whenever those four coincide, non-standard signatures should be expected as the *baseline* — not as exceptions.

**RU:** Все пять кейсов одновременно инстанцируют одни и те же четыре условия: быстрый импульс, нелинейная среда, многоканальный отклик и система с памятью/историей. Всегда, когда эти четыре условия совпадают, нестандартные сигнатуры следует ожидать как *базовое поведение*, а не как исключение.

---

## Navigation / Навигация

- Sub-archive README / README подархива: [`../README.md`](../README.md)
- Signature methodology / Методология сигнатур: [`signature-methodology.md`](signature-methodology.md)
- Validation pipeline / Конвейер валидации: [`validation-pipeline.md`](validation-pipeline.md)
- UAP application / Применение к НАЯ: [`uap-application.md`](uap-application.md)
- Source / Источник: [`../raw/chatgpt_69ed8711_signature_methodology.txt`](../raw/chatgpt_69ed8711_signature_methodology.txt)
- Root README / Корневой README: [`../../README.md`](../../README.md)
