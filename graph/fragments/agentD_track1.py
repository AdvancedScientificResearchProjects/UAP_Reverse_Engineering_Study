# ════════════════════════════════════════════════════════════════════
# TRACK 1 — UAP-FRAG-001 ECP + AI multi-pipeline study (sub-agent D)
# ════════════════════════════════════════════════════════════════════

# ── PHENOMENON ───────────────────────────────────────────────────────

E("phen-uap-frag-001", "UAP-FRAG-001 (artifact under study)", "phenomenon",
  label_ru="UAP-FRAG-001 (исследуемый артефакт)",
  description="Physical fragment under triple-pipeline study (ECP + AI/CV + archival). "
              "Disclosed reference data: 'biometal', variable radioactivity, unknown manufacturing technology. "
              "Cross-pipeline comparison: 10 verifiable parameters, 7/10 exact matches, 2 partial, 1 complete miss. "
              "Methodological constraint: 2/3 percipients had compromised blinding.",
  description_ru="Физический фрагмент в тройном конвейере исследований (КП + ИИ/CV + архив). "
                 "Референсные данные: «биометалл», переменная радиоактивность, неизвестная технология производства. "
                 "Кросс-конвейерное сравнение: 10 проверяемых параметров, 7/10 точных совпадений, 2 частичных, 1 промах. "
                 "Методологическое ограничение: у 2/3 перципиентов нарушено ослепление.")

# ── PERSONS ──────────────────────────────────────────────────────────

E("p-vsemiletov", "Vladislav Semiletov", "person · external",
  label_ru="Семилетов Владислав",
  description="L4 Secondary Percipient · ECP session ECP-2026-04-04-001 · 2026-04-04 ~15:20 · "
              "full blinding maintained (interviewed first). "
              "Self-assessed signal clarity 10/10, confidence 10/10.",
  description_ru="Перципиент L4 · ECP-сеанс ECP-2026-04-04-001 · 04.04.2026 ~15:20 · "
                 "полное ослепление сохранено (опрошен первым). "
                 "Самооценка чёткости сигнала 10/10, уверенности 10/10.")

E("p-ebelousova", "Ekaterina Belousova", "person · external",
  label_ru="Белоусова Екатерина",
  description="L4 Secondary Percipient · ECP session ECP-2026-04-04-002 · 2026-04-04 ~15:40 · "
              "BLINDING COMPROMISED — heard Vladislav's response before her own session.",
  description_ru="Перципиент L4 · ECP-сеанс ECP-2026-04-04-002 · 04.04.2026 ~15:40 · "
                 "ОСЛЕПЛЕНИЕ НАРУШЕНО — слышала ответ Владислава до своего сеанса.")

# ── ECP SUB-EVENTS ───────────────────────────────────────────────────

E("ev-ecp-vlad", "ECP-2026-04-04-001 · Vladislav Semiletov session", "event",
  date="2026-04-04",
  label_ru="ECP-2026-04-04-001 · Сеанс Семилетова Владислава",
  description="Session ID ECP-2026-04-04-001 · ~15:20 · L4 percipient · full blind · "
              "key perceptions: beacon/signal function, part of larger moving system, "
              "non-terrestrial origin, coral-like material with iron/oxides.",
  description_ru="Session ID ECP-2026-04-04-001 · ~15:20 · перципиент L4 · полное ослепление · "
                 "ключевые восприятия: функция маяка/сигнала, часть большей движущейся системы, "
                 "внеземное происхождение, коралловый материал с железом/оксидами.")

E("ev-ecp-ek", "ECP-2026-04-04-002 · Ekaterina Belousova session", "event",
  date="2026-04-04",
  label_ru="ECP-2026-04-04-002 · Сеанс Белоусовой Екатерины",
  description="Session ID ECP-2026-04-04-002 · ~15:40 · L4 percipient · BLINDING COMPROMISED · "
              "key perceptions: scanning/protection device, 'bolt in a machine', "
              "cold reptilian-type owner, salts/minerals material, age 2-3 thousand years.",
  description_ru="Session ID ECP-2026-04-04-002 · ~15:40 · перципиент L4 · ОСЛЕПЛЕНИЕ НАРУШЕНО · "
                 "ключевые восприятия: сканирующее/защитное устройство, «гайка в машине», "
                 "холодный рептильный владелец, материал — соли/минералы, возраст 2-3 тысячи лет.")

E("ev-ecp-tat", "ECP-2026-04-04-003 · Tatyana Burilova session", "event",
  date="2026-04-04",
  label_ru="ECP-2026-04-04-003 · Сеанс Буриловой Татьяны",
  description="Session ID ECP-2026-04-04-003 · ~15:45 · L4 percipient · BLINDING COMPROMISED · "
              "signal clarity 7/10, confidence 6/10 · key perceptions: beacon/tracker transmitting "
              "to mothership, humanoid owner ~2-2.5m with crab/octopus features.",
  description_ru="Session ID ECP-2026-04-04-003 · ~15:45 · перципиент L4 · ОСЛЕПЛЕНИЕ НАРУШЕНО · "
                 "чёткость 7/10, уверенность 6/10 · ключевые восприятия: маяк/трекер на материнский корабль, "
                 "человекоподобный владелец ~2-2.5м с чертами краба/осьминога.")

# ── AI / CV EVENTS ───────────────────────────────────────────────────

E("ev-ai-cv-001", "AI CV Pipeline run · AI-2026-04-07-001", "event",
  date="2026-04-07",
  label_ru="Запуск ИИ CV-конвейера · AI-2026-04-07-001",
  description="Pipeline v3.0 run on UAP-FRAG-001.jpg [720×1280] · "
              "stages: Grounding DINO → SAM2 → DINOv2 → SigLIP2 → EfficientAD → CLIP → DepthAnything v2 · "
              "primary result: Biological/Organic HIGH (0.98 sigmoid), no anomalies, convex surface.",
  description_ru="Запуск конвейера v3.0 на UAP-FRAG-001.jpg · "
                 "этапы: Grounding DINO → SAM2 → DINOv2 → SigLIP2 → EfficientAD → CLIP → DepthAnything v2 · "
                 "главный результат: Биологический/Органический HIGH (0.98 sigmoid), аномалий нет.")

E("ev-ai-llm-visual", "LLM visual blind analysis · AI-2026-04-07-001-llm-visual", "event",
  date="2026-04-07",
  label_ru="Слепой визуальный анализ LLM · AI-2026-04-07-001-llm-visual",
  description="Claude Opus 4.6 multimodal blind analysis · isolated subagent with no ECP/reference access · "
              "primary hypothesis: fossilized sea urchin Echinoidea/Cidaridae (70-80%) · "
              "noted: greenish tint (possible glauconite/copper minerals), unusual dense serrated microtexture.",
  description_ru="Слепой мультимодальный анализ Claude Opus 4.6 · изолированный субагент без доступа к ECP/референсу · "
                 "основная гипотеза: ископаемый морской ёж Echinoidea/Cidaridae (70-80%) · "
                 "отмечено: зеленоватый оттенок, плотная зубчатая микротекстура, радиальная 5-лучевая симметрия.")

E("ev-ai-ctrl-test", "SigLIP2 control test · AI-2026-04-09-CTRL", "event",
  date="2026-04-09",
  label_ru="Контрольный тест SigLIP2 · AI-2026-04-09-CTRL",
  description="SigLIP2 zero-shot control test · UAP-FRAG-001 vs 13 control images · "
              "artifact score 0.891 · Z=0.916 (80th percentile) · within 1 std of fossil mean (0.732) · "
              "color anomaly: V=90 dark blue-gray vs typical fossil V=164-169 · analyst: Zmiienko Kyryl.",
  description_ru="Контрольный тест SigLIP2 zero-shot · UAP-FRAG-001 vs 13 контрольных изображений · "
                 "скор артефакта 0.891 · Z=0.916 (80-й процентиль) · в пределах 1 стд. откл. от среднего по окаменелостям · "
                 "цветовая аномалия: V=90 vs типичный V=164-169 · аналитик: Змиенко Кирилл.")

# ── FACTS ────────────────────────────────────────────────────────────

E("f-ecp-blinding-compromised", "Blinding compromised for 2 of 3 percipients", "fact",
  source="src-ecp-protocol-v2",
  confidence="high",
  label_ru="Ослепление нарушено у 2 из 3 перципиентов",
  description="Explicitly documented in percipient reports: Ekaterina (ECP-002) heard Vladislav's session before her own; "
              "Tatyana (ECP-003) heard both Vladislav and Ekaterina before her session. Only Vladislav (ECP-001) had full blinding.",
  description_ru="Явно зафиксировано в отчётах перципиентов: Екатерина и Татьяна слышали предыдущие сеансы. "
                 "Только Владислав (ECP-001) имел полное ослепление как первый перципиент.")

E("f-ecp-7-of-10", "7/10 percipient-response exact matches with reference", "fact",
  source="src-ai-cv-report",
  confidence="medium",
  label_ru="7/10 точных совпадений ответов перципиентов с референсом",
  description="Cross-pipeline comparison table: 10 verifiable parameters scored across 3 percipient sessions against disclosed reference · "
              "7 exact, 2 partial, 1 complete miss · CONSTRAINT: 2/3 percipients had compromised blinding.",
  description_ru="Таблица кросс-конвейерного сравнения: 10 проверяемых параметров · 7 точных, 2 частичных, 1 промах · "
                 "ОГРАНИЧЕНИЕ: у 2/3 перципиентов нарушено ослепление.")

E("f-ecp-theme-beacon", "Repeated theme: beacon/signal/tracker function", "fact",
  source="src-ai-cv-report",
  confidence="medium",
  label_ru="Повторяющаяся тема: функция маяка/сигнала/трекера",
  description="All 3 percipients independently described a signalling/beacon function. NOTE: Ekaterina and Tatyana had heard Vladislav's 'маячок' framing before responding.",
  description_ru="Все 3 перципиента описали сигнальную/маяковую функцию. ПРИМЕЧАНИЕ: Екатерина и Татьяна слышали формулировку Владислава «маячок» до ответа.")

E("f-ecp-theme-part-of-system", "Repeated theme: part of a larger system", "fact",
  source="src-ai-cv-report",
  confidence="medium",
  label_ru="Повторяющаяся тема: часть большей системы",
  description="All 3 percipients identified the artifact as a component of a larger system. Matches reference parameter. Blinding caveat applies.",
  description_ru="Все 3 перципиента идентифицировали артефакт как компонент большей системы. Совпадает с референсом. Применима оговорка об ослеплении.")

E("f-ecp-theme-non-terrestrial", "Repeated theme: non-terrestrial origin", "fact",
  source="src-ai-cv-report",
  confidence="medium",
  label_ru="Повторяющаяся тема: внеземное происхождение",
  description="All 3 percipients attributed non-terrestrial origin. Blinding caveat applies for Ekaterina and Tatyana.",
  description_ru="Все 3 перципиента указали на внеземное происхождение. Применима оговорка об ослеплении.")

E("f-ecp-theme-non-autonomous", "Repeated theme: non-autonomous instrument", "fact",
  source="src-ai-cv-report",
  confidence="medium",
  label_ru="Повторяющаяся тема: неавтономный инструмент",
  description="All 3 percipients described the artifact as a non-autonomous tool without independent consciousness.",
  description_ru="Все 3 перципиента описали артефакт как неавтономный инструмент без самостоятельного сознания.")

E("f-ecp-contradiction-flight-vs-stationary", "Contradiction: flight/dynamic (V) vs. stationary placement (E+T)", "fact",
  source="src-ai-cv-report",
  confidence="high",
  label_ru="Противоречие: полёт/динамика (В) vs. стационарное размещение (Е+Т)",
  description="Vladislav described active dynamic flight; Ekaterina and Tatyana described the artifact as a stationary device. "
              "Single complete miss across 3-percipient comparison.",
  description_ru="Владислав описал активный полёт; Екатерина и Татьяна описали стационарное устройство. "
                 "Единственный полный промах в кросс-сравнении.")

E("f-ai-coral-material", "AI: 0.98 sigmoid Biological/Organic (coral / sea urchin fossil)", "fact",
  source="src-ai-cv-report",
  confidence="medium",
  label_ru="ИИ: 0.98 sigmoid Биологический/Органический (коралл / ископаемый морской ёж)",
  description="SigLIP2 zero-shot material classification: Biological/Organic family score 0.98 (HIGH). "
              "LIMITATION: RGB cannot determine chemical composition, alloy, or radioactivity.",
  description_ru="Классификация материала SigLIP2: Биологический/Органический — 0.98. "
                 "ОГРАНИЧЕНИЕ: RGB не определяет химсостав, сплав или радиоактивность.")

E("f-ai-no-anomaly", "AI: no significant surface anomalies detected", "fact",
  source="src-ai-cv-report",
  confidence="high",
  label_ru="ИИ: значимых поверхностных аномалий не обнаружено",
  description="CLIP zero-shot: normal 0.755, abnormal 0.245 → is_anomalous=False. EfficientAD proxy: LIMITED.",
  description_ru="CLIP zero-shot: норма 0.755, аномалия 0.245 → is_anomalous=False. EfficientAD proxy: ОГРАНИЧЕНО.")

E("f-ai-ctrl-within-fossil-range", "AI control test: artifact within statistical range of real fossils", "fact",
  source="src-ai-ctrl-report",
  confidence="medium",
  label_ru="Контрольный тест ИИ: артефакт в статистическом диапазоне реальных окаменелостей",
  description="Artifact bio/organic score 0.891; fossil-group mean 0.732, Z=0.916, within 1 std — "
              "not statistically distinguishable from genuine echinoid fossils by visual classification alone.",
  description_ru="Скор артефакта 0.891; среднее по окаменелостям 0.732, Z=0.916, в пределах 1 стд. откл. — "
                 "статистически неразличим от настоящих окаменелостей только по визуальной классификации.")

E("f-ai-color-anomaly", "AI control test: anomalous dark blue-gray coloration (V=90, H=89)", "fact",
  source="src-ai-ctrl-report",
  confidence="high",
  label_ru="Контрольный тест ИИ: аномальная тёмная сине-серая окраска (V=90, H=89)",
  description="HSV: UAP-FRAG-001 V=90, H=89 (blue-gray). Typical calcified echinoid fossils: V=164-169. "
              "Possible explanations: pyritization, phosphatization, non-biological material with biomorphic geometry, artificial modification.",
  description_ru="HSV: V=90, H=89 (сине-серый). Типичные окаменелости: V=164-169. "
                 "Возможные объяснения: пиритизация, фосфатизация, небиологический материал, искусственная модификация.")

E("f-ai-rgb-cannot-determine", "AI pipeline limitation: RGB cannot determine chemistry/radioactivity", "fact",
  source="src-ai-protocol-v31",
  confidence="high",
  label_ru="Ограничение ИИ-конвейера: RGB не определяет химсостав / радиоактивность",
  description="Standard RGB photography cannot determine chemical composition, alloy, crystallographic structure, "
              "radioactivity, or internal density. Required: hyperspectral, OES, XRF, Raman, SEM-EDS, gamma spectroscopy.",
  description_ru="RGB-фотография не может определить химсостав, сплав, структуру, радиоактивность или плотность. "
                 "Требуется: гиперспектральная камера, ОЭС, РФА, рамановская, СЭМ-ЭДС, гамма-спектроскопия.")

# ── TOOLING-CLASS ─────────────────────────────────────────────────────

E("tool-siglip2", "SigLIP2 SO400M (Google) — text-image encoder", "tooling-class",
  label_ru="SigLIP2 SO400M (Google) — текстово-визуальный энкодер",
  description="google/siglip2-so400m-patch14-384 · 400M params · sigmoid scoring · "
              "primary material result: Biological/Organic 0.98 · also used in control test.",
  description_ru="google/siglip2-so400m-patch14-384 · 400M параметров · sigmoid-скоринг · "
                 "основной результат: Биологический/Органический 0.98.")

E("tool-effad", "EfficientAD (via Anomalib) — surface anomaly detector", "tooling-class",
  label_ru="EfficientAD (через Anomalib) — детектор поверхностных аномалий",
  description="Stage s6 in pipeline · student-teacher architecture · LIMITATION: gradient-only proxy used for single-image analysis.",
  description_ru="Этап s6 · архитектура студент-учитель · ОГРАНИЧЕНИЕ: использована прокси-заглушка на основе градиентов.")

E("tool-clip", "CLIP ViT-B/16 (OpenAI) — zero-shot anomaly classifier", "tooling-class",
  label_ru="CLIP ViT-B/16 (OpenAI) — zero-shot классификатор аномалий",
  description="Stage s7 · AnomalyCLIP proxy · softmax scoring · result: normal 0.755, abnormal 0.245.",
  description_ru="Этап s7 · прокси AnomalyCLIP · softmax-скоринг · результат: норма 0.755, аномалия 0.245.")

E("tool-llm-visual", "Claude Opus 4.6 — blind multimodal visual analysis", "tooling-class",
  label_ru="Claude Opus 4.6 — слепой мультимодальный визуальный анализ",
  description="claude-opus-4-6 · launched as isolated subagent · primary hypothesis: Echinoidea/Cidaridae fossil (70-80%).",
  description_ru="claude-opus-4-6 · запущен как изолированный субагент · основная гипотеза: окаменелость Echinoidea/Cidaridae (70-80%).")

E("tool-depth-anything", "Depth Anything V2 Small — monocular depth estimation", "tooling-class",
  label_ru="Depth Anything V2 Small — монокулярная оценка глубины",
  description="depth-anything/Depth-Anything-V2-Small-hf · stage s8 · result: surface convex=True, center 0.561, edge 0.254.",
  description_ru="depth-anything/Depth-Anything-V2-Small-hf · этап s8 · результат: поверхность выпуклая=True.")

# ── HYPOTHESES ────────────────────────────────────────────────────────

E("hyp-beacon-navigation", "Hypothesis: artifact is a beacon / navigation component", "hypothesis",
  label_ru="Гипотеза: артефакт — маяк / навигационный компонент",
  description="Cross-percipient hypothesis · Tatyana adds location-transmission to mothership · cannot be verified by RGB CV pipeline.",
  description_ru="Межперципиентная гипотеза · Татьяна добавляет передачу локации на материнский корабль · не может быть проверено RGB CV-конвейером.")

E("hyp-part-larger-system", "Hypothesis: artifact is a fragment of a larger non-terrestrial system", "hypothesis",
  label_ru="Гипотеза: артефакт — фрагмент большей внеземной системы",
  description="All 3 percipients converge. Partially supported by reference data. Cannot be confirmed by visual CV methods alone.",
  description_ru="Все 3 перципиента сходятся. Частично подтверждается референсом. Не может быть подтверждено только визуальными методами.")

# ── SOURCES ──────────────────────────────────────────────────────────

E("src-ecp-protocol-v2", "ECP Protocol v2.0", "source",
  label_ru="Протокол КП v2.0",
  description="experiments/protocol_ecp.md · version 2.0 · defines percipient levels (L1-L4), reporting format, validation matrix.",
  description_ru="experiments/protocol_ecp.md · v2.0 · уровни перципиентов (L1-L4), формат отчётности, матрица валидации.",
  url="experiments/protocol_ecp.md")

E("src-ai-protocol-v31", "AI Pipeline Protocol v3.1", "source",
  label_ru="Протокол ИИ-конвейера v3.1",
  description="experiments/protocol_ai.md · v3.1 · defines model stack, material taxonomy, anomaly pipeline, limitations · author: Zmiienko Kyryl.",
  description_ru="experiments/protocol_ai.md · v3.1 · стек моделей, таксономия материалов, конвейер аномалий · автор: Змиенко Кирилл.",
  url="experiments/protocol_ai.md")

E("src-ai-cv-report", "AI Analysis Report AI-2026-04-07-001", "source",
  label_ru="Отчёт ИИ-анализа AI-2026-04-07-001",
  description="reports/ai_reports/AI-2026-04-07-001.md · pipeline v3.0 · full CV results + cross-pipeline ECP comparison.",
  description_ru="reports/ai_reports/AI-2026-04-07-001.md · конвейер v3.0 · полные результаты CV + кросс-сравнение с КП.",
  url="reports/ai_reports/AI-2026-04-07-001.md")

E("src-ai-llm-report", "LLM Visual Analysis Report AI-2026-04-07-001-llm-visual", "source",
  label_ru="Отчёт LLM-визуального анализа",
  description="reports/ai_reports/AI-2026-04-07-001-llm-visual.md · Claude Opus 4.6 blind multimodal analysis.",
  description_ru="reports/ai_reports/AI-2026-04-07-001-llm-visual.md · слепой мультимодальный анализ Claude Opus 4.6.",
  url="reports/ai_reports/AI-2026-04-07-001-llm-visual.md")

E("src-ai-ctrl-report", "AI Control Test Report AI-2026-04-09-CTRL", "source",
  label_ru="Отчёт контрольного теста ИИ AI-2026-04-09-CTRL",
  description="reports/ai_reports/AI-2026-04-09-control-test.md · SigLIP2 zero-shot control · 13 images · Z-score, percentile, HSV.",
  description_ru="reports/ai_reports/AI-2026-04-09-control-test.md · контрольный тест SigLIP2 · 13 изображений · Z-оценка, HSV.",
  url="reports/ai_reports/AI-2026-04-09-control-test.md")

E("src-pipeline-readme", "AI Pipeline README", "source",
  label_ru="README ИИ-конвейера",
  description="pipeline/README.md · documents 9-stage pipeline (s0 preprocess → s9 report), model-to-stage mapping.",
  description_ru="pipeline/README.md · 9-этапный конвейер (s0 препроцессинг — s9 отчёт), маппинг моделей.",
  url="pipeline/README.md")

# ── CONNECTIONS ───────────────────────────────────────────────────────

# Percipients → sessions
C("p-vsemiletov",  "ev-ecp-vlad", "is-percipient-of",   direction="directed")
C("p-ebelousova",  "ev-ecp-ek",   "is-percipient-of",   direction="directed")
C("p-burilova",    "ev-ecp-tat",  "is-percipient-of",   direction="directed")

# Sub-sessions → parent ECP event
C("ev-ecp-vlad",   "ev-ecp",      "is-sub-session-of",  direction="directed")
C("ev-ecp-ek",     "ev-ecp",      "is-sub-session-of",  direction="directed")
C("ev-ecp-tat",    "ev-ecp",      "is-sub-session-of",  direction="directed")

# AI events → parent project
C("ev-ai-cv-001",     "pj-uap",   "conducted",          direction="directed")
C("ev-ai-llm-visual", "pj-uap",   "conducted",          direction="directed")
C("ev-ai-ctrl-test",  "pj-uap",   "conducted",          direction="directed")
C("ev-ai-llm-visual", "ev-ai-cv-001", "is-sub-session-of", direction="directed")

# Artifact is subject of all pipeline events
C("phen-uap-frag-001", "ev-ecp",          "subject-of", direction="directed")
C("phen-uap-frag-001", "ev-ai-cv-001",    "subject-of", direction="directed")
C("phen-uap-frag-001", "ev-ai-llm-visual","subject-of", direction="directed")
C("phen-uap-frag-001", "ev-ai-ctrl-test", "subject-of", direction="directed")

# Tool usage
C("tool-siglip2",       "ev-ai-cv-001",    "applies-method", direction="directed")
C("tool-effad",         "ev-ai-cv-001",    "applies-method", direction="directed")
C("tool-clip",          "ev-ai-cv-001",    "applies-method", direction="directed")
C("tool-depth-anything","ev-ai-cv-001",    "applies-method", direction="directed")
C("tool-siglip2",       "ev-ai-ctrl-test", "applies-method", direction="directed")
C("tool-llm-visual",    "ev-ai-llm-visual","applies-method", direction="directed")

# Tools produce facts
C("tool-siglip2",       "f-ai-coral-material",          "produces-result", direction="directed")
C("tool-clip",          "f-ai-no-anomaly",              "produces-result", direction="directed")
C("tool-effad",         "f-ai-no-anomaly",              "produces-result", direction="directed")
C("tool-siglip2",       "f-ai-ctrl-within-fossil-range","produces-result", direction="directed")
C("tool-siglip2",       "f-ai-color-anomaly",           "produces-result", direction="directed")

# Analyst connections
C("p-kz", "ev-ai-ctrl-test",  "conducted",  direction="directed")
C("p-kz", "src-ai-protocol-v31", "authored", direction="directed")
C("p-kz", "src-ai-ctrl-report",  "authored", direction="directed")

# Facts → sources (documented-in)
C("f-ecp-blinding-compromised",         "src-ecp-protocol-v2", "supports",      direction="directed")
C("f-ecp-7-of-10",                      "src-ai-cv-report",    "supports",      direction="directed")
C("f-ecp-theme-beacon",                 "src-ai-cv-report",    "supports",      direction="directed")
C("f-ecp-theme-part-of-system",         "src-ai-cv-report",    "supports",      direction="directed")
C("f-ecp-theme-non-terrestrial",        "src-ai-cv-report",    "supports",      direction="directed")
C("f-ecp-theme-non-autonomous",         "src-ai-cv-report",    "supports",      direction="directed")
C("f-ecp-contradiction-flight-vs-stationary", "src-ai-cv-report", "supports",   direction="directed")
C("f-ai-coral-material",                "src-ai-cv-report",    "supports",      direction="directed")
C("f-ai-no-anomaly",                    "src-ai-cv-report",    "supports",      direction="directed")
C("f-ai-ctrl-within-fossil-range",      "src-ai-ctrl-report",  "supports",      direction="directed")
C("f-ai-color-anomaly",                 "src-ai-ctrl-report",  "supports",      direction="directed")
C("f-ai-rgb-cannot-determine",          "src-ai-protocol-v31", "supports",      direction="directed")

# Cross-method convergence
C("f-ai-coral-material",       "f-ecp-theme-beacon",          "related-to",    direction="directed")
C("f-ai-coral-material",       "f-ecp-theme-non-terrestrial", "related-to",    direction="directed")
C("f-ai-ctrl-within-fossil-range", "f-ai-coral-material",     "supports",      direction="directed")
C("f-ai-color-anomaly",        "f-ai-ctrl-within-fossil-range","challenges",   direction="directed")

# Methodology constraint chain
C("f-ecp-7-of-10",      "f-ecp-blinding-compromised",  "constrained-by", direction="directed")
C("f-ecp-theme-beacon", "f-ecp-blinding-compromised",  "constrained-by", direction="directed")
C("f-ecp-theme-part-of-system",    "f-ecp-blinding-compromised", "constrained-by", direction="directed")
C("f-ecp-theme-non-terrestrial",   "f-ecp-blinding-compromised", "constrained-by", direction="directed")
C("f-ecp-theme-non-autonomous",    "f-ecp-blinding-compromised", "constrained-by", direction="directed")
C("f-ecp-contradiction-flight-vs-stationary", "f-ecp-blinding-compromised", "constrained-by", direction="directed")

# RGB limitation constrains AI facts
C("f-ai-rgb-cannot-determine", "f-ai-coral-material",          "constrained-by", direction="directed")
C("f-ai-rgb-cannot-determine", "f-ai-ctrl-within-fossil-range","constrained-by", direction="directed")

# Hypotheses ← supporting facts
C("f-ecp-theme-beacon",           "hyp-beacon-navigation",     "supports", direction="directed")
C("f-ecp-theme-non-terrestrial",  "hyp-beacon-navigation",     "supports", direction="directed")
C("f-ecp-theme-non-autonomous",   "hyp-beacon-navigation",     "supports", direction="directed")
C("f-ecp-theme-part-of-system",   "hyp-part-larger-system",    "supports", direction="directed")
C("f-ecp-theme-non-terrestrial",  "hyp-part-larger-system",    "supports", direction="directed")
C("f-ecp-contradiction-flight-vs-stationary", "hyp-beacon-navigation", "challenges", direction="directed")

# Protocols govern events
C("src-ecp-protocol-v2",   "ev-ecp",       "employed-at",  direction="directed")
C("src-ai-protocol-v31",   "ev-ai-cv-001", "employed-at",  direction="directed")
C("src-pipeline-readme",   "ev-ai-cv-001", "employed-at",  direction="directed")

# Pipeline README → tooling
C("src-pipeline-readme", "tool-siglip2",        "related-to", direction="directed")
C("src-pipeline-readme", "tool-effad",          "related-to", direction="directed")
C("src-pipeline-readme", "tool-clip",           "related-to", direction="directed")
C("src-pipeline-readme", "tool-depth-anything", "related-to", direction="directed")
