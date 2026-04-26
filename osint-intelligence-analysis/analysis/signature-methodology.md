# Signature analysis methodology / Методология анализа сигнатур

**EN:** This file fixes the working definitions used across the whole UAP Reverse Engineering Study to read physical-signal data: what counts as a *signature*, how an *ordinary* signature is structured, how a *non-standard* signature is structured, and into which of four operational classes any observation should be placed before any further interpretation is allowed.

**RU:** Этот файл фиксирует рабочие определения, используемые во всём исследовании реверс-инжиниринга НАЯ для чтения данных по физическим сигналам: что именно считается *сигнатурой*, как устроена *обычная* сигнатура, как устроена *нестандартная* сигнатура и в какой из четырёх операционных классов должно быть помещено любое наблюдение, прежде чем разрешается дальнейшая интерпретация.

---

## 1. Definition of a signature / Определение сигнатуры

**EN:** A signature is **not** a single trace. It is a multi-component fingerprint of a physical regime, formed by the simultaneous combination of:

1. **Time-domain shape** of the recorded pulse (front, peak, decay).
2. **Frequency content** (spectrum: broadband noise vs discrete lines).
3. **Cross-channel correlation** between independent sensors — typically electromagnetic (EM), optical, current/voltage, and where available mechanical/acoustic.
4. **Inter-channel delay structure** — what arrives first, what arrives later, and how stable that ordering is across runs.

A signature is the *handwriting* of a regime; any one of the four components alone is insufficient.

**RU:** Сигнатура — это **не** один трек. Это многокомпонентный отпечаток физического режима, образованный одновременной комбинацией:

1. **Формы во временной области** записанного импульса (фронт, пик, спад).
2. **Частотного содержимого** (спектр: широкополосный шум vs дискретные линии).
3. **Корреляции между каналами** независимых сенсоров — обычно электромагнитный (EM), оптический, ток/напряжение, при наличии — механический/акустический.
4. **Структуры задержек между каналами** — что приходит первым, что позже, и насколько стабилен этот порядок от запуска к запуску.

Сигнатура — это *почерк* режима; любая из четырёх компонент по отдельности недостаточна.

---

## 2. Standard ("ordinary") signatures / Стандартные («обычные») сигнатуры

**EN:** A regime is treated as standard when all four of the following hold:

- **Sharp threshold.** Below a critical control parameter (voltage, energy, pressure) — nothing. At and above it — the effect appears cleanly. No effect is observable below the threshold, no plateau or pre-effect "hum".
- **Predictable pulse shape.** Fast leading front, single dominant peak, exponential (or exponential-like) decay. The shape is set by the standard linear/weakly-nonlinear physics of the medium.
- **Broadband, structureless spectrum.** Energy is spread over a wide band of frequencies; no narrow lines stand out above the background.
- **Repeatability.** Identical input parameters produce identical output, within measurement noise.

A signature satisfying all four points is treated as a **stable, possibly nonlinear, but well-described regime**. No further interpretation is permitted beyond what existing models already cover.

**RU:** Режим считается стандартным, когда выполнены все четыре условия:

- **Чёткий порог.** Ниже критического значения управляющего параметра (напряжение, энергия, давление) — ничего. На пороге и выше — эффект появляется чисто. Ниже порога эффект не наблюдается, нет плато и предварительного «гудения».
- **Предсказуемая форма импульса.** Быстрый передний фронт, единственный доминирующий пик, экспоненциальный (или близкий к экспоненциальному) спад. Форма задана стандартной линейной/слабонелинейной физикой среды.
- **Широкополосный, бесструктурный спектр.** Энергия распределена по широкой полосе частот; узкие линии не выделяются над фоном.
- **Повторяемость.** Идентичные входные параметры дают идентичный выход в пределах шума измерения.

Сигнатура, удовлетворяющая всем четырём пунктам, рассматривается как **стабильный, возможно нелинейный, но хорошо описанный режим**. Дальнейшая интерпретация сверх того, что уже покрывают существующие модели, не допускается.

---

## 3. Non-standard signatures / Нестандартные сигнатуры

**EN:** The defining property of a non-standard signature is that **the system stops being single-valued**: the same nominal input no longer maps to a single output. The diagnostic features are:

- **Multiple peaks.** Instead of one dominant impulse, a comb of peaks at irregular intervals — indicates either several superimposed processes or feedback inside the system.
- **Temporal drift.** Peaks shift their position across consecutive shots; the system is unstable or self-organizing on a slow timescale.
- **Narrow spectral lines.** Discrete frequencies emerge above the broadband floor — indicates resonance, mode locking, or partial coherence in what is otherwise a "dirty" plasma/breakdown.
- **System memory.** The response to pulse N depends on pulses 1 … N − 1: pulse 1 is weak, pulse 2 is stronger, pulse 3 stronger still, or vice versa. The medium has been *prepared* by the prior history.
- **Channel desynchronization.** EM is recorded at time t₀; the optical channel arrives at t₀ + Δt with non-trivial Δt; current/voltage may lead or lag both. Several physically distinct processes are running in the same event.
- **Energy localization / filamentation.** The signal originates from a sub-region (a filament, a hot spot) instead of being volumetrically distributed — self-focusing or channel formation has occurred.

Any one of these features, sustained across runs, is sufficient to reclassify the regime out of "standard" — but is **not** sufficient on its own to call it new physics.

**RU:** Определяющее свойство нестандартной сигнатуры — **система перестаёт быть однозначной**: тот же номинальный вход уже не отображается в один и тот же выход. Диагностические признаки:

- **Множественные пики.** Вместо одного доминирующего импульса — гребёнка пиков на нерегулярных интервалах; указывает либо на несколько наложенных процессов, либо на обратную связь внутри системы.
- **Временной дрейф.** Пики смещаются от выстрела к выстрелу; система нестабильна или самоорганизуется на медленной шкале.
- **Узкие частотные линии.** Над широкополосным фоном появляются дискретные частоты — резонанс, синхронизация мод или частичная когерентность в том, что иначе было бы «грязной» плазмой/пробоем.
- **Память системы.** Отклик на импульс N зависит от импульсов 1 … N − 1: импульс 1 слабый, импульс 2 сильнее, импульс 3 ещё сильнее — или наоборот. Среда *подготовлена* предыдущей историей.
- **Рассинхронизация каналов.** EM фиксируется в момент t₀; оптика приходит в t₀ + Δt с нетривиальным Δt; ток/напряжение могут опережать или отставать. В одном событии параллельно идут несколько физически разных процессов.
- **Локализация энергии / филаментация.** Сигнал исходит из подобласти (филамент, горячая точка), а не распределён по объёму — произошла самофокусировка или образование канала.

Любой из этих признаков, устойчиво повторяющийся в серии запусков, достаточен для переклассификации режима из «стандартного» — но **не** достаточен сам по себе, чтобы назвать его новой физикой.

---

## 4. Four-class operational classification / Операционная классификация из четырёх типов

**EN:** Every observation, before any deeper analysis, is forced into exactly one of four classes:

**RU:** Любое наблюдение, до какой-либо более глубокой интерпретации, помещается ровно в один из четырёх классов:

| Class | EN — definition | RU — определение |
|---|---|---|
| **Type 1 — Stable nonlinearity** | Repeatable, predictable, fully covered by existing nonlinear-physics models. | Воспроизводимо, предсказуемо, полностью покрыто существующими моделями нелинейной физики. |
| **Type 2 — Transient regime** | Partially chaotic, sensitive to small parameter changes; behaves differently between regions of parameter space. | Частично хаотично, чувствительно к малым изменениям параметров; ведёт себя по-разному в разных областях пространства параметров. |
| **Type 3 — Self-organization** | Structure emerges (filaments, standing patterns, repeating motifs) where structure was not put in by the experimenter. | Появляется структура (филаменты, стоячие паттерны, повторяющиеся мотивы) там, где экспериментатор её не закладывал. |
| **Type 4 — "Anomalous"** | Does **not** fit existing models, **but** is reproducible. This is the only class that can be a candidate for new physics. | **Не** укладывается в существующие модели, **но** воспроизводится. Единственный класс, который может быть кандидатом на новую физику. |

**EN:** Type 4 is *not* the same as "we got a strange single trace" — that is reserved for noise/artifact. Type 4 requires reproducibility plus model failure; without both, the observation is downgraded.

**RU:** Тип 4 — это *не* то же самое, что «у нас получился странный одиночный трек» — такое относится к шуму/артефактам. Тип 4 требует одновременно воспроизводимости и провала модели; без обоих условий наблюдение понижается в классе.

---

## 5. Where the strangest signatures appear / Где появляются самые странные сигнатуры

**EN:** Empirically, the most informative non-standard signatures cluster where **three conditions coincide**:

1. **Nanosecond-scale pulses** (so the system is far from equilibrium).
2. **A nonlinear medium** (plasma, near-breakdown gas, certain solids).
3. **Feedback** (system memory, geometric or electromagnetic).

When all three coincide, three observable consequences become typical: standing structures inside plasma, self-sustaining regimes that outlive the driving pulse, and non-standard EM emission spectra. These are the regions where the validation pipeline ([`validation-pipeline.md`](validation-pipeline.md)) is applied with the most weight.

**RU:** Эмпирически наиболее информативные нестандартные сигнатуры группируются там, где **совпадают три условия**:

1. **Импульсы наносекундного масштаба** (система далеко от равновесия).
2. **Нелинейная среда** (плазма, газ у порога пробоя, некоторые твёрдые тела).
3. **Обратная связь** (память системы, геометрическая или электромагнитная).

Когда все три совпадают, типичны три наблюдаемых следствия: стоячие структуры в плазме, самоподдерживающиеся режимы, переживающие задающий импульс, и нестандартные спектры EM-излучения. Это области, где конвейер валидации ([`validation-pipeline.md`](validation-pipeline.md)) применяется с наибольшим весом.

---

## Navigation / Навигация

- Sub-archive README / README подархива: [`../README.md`](../README.md)
- Anomaly classification / Классификация аномалий: [`anomaly-classification.md`](anomaly-classification.md)
- Validation pipeline / Конвейер валидации: [`validation-pipeline.md`](validation-pipeline.md)
- UAP application / Применение к НАЯ: [`uap-application.md`](uap-application.md)
- Source / Источник: [`../raw/chatgpt_69ed8711_signature_methodology.txt`](../raw/chatgpt_69ed8711_signature_methodology.txt)
- Root README / Корневой README: [`../../README.md`](../../README.md)
