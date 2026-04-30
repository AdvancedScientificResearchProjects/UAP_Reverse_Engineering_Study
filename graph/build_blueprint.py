#!/usr/bin/env python3
"""Build a Cytoscape.js / Kumu.io JSON blueprint of the UAP Reverse-Engineering
Study repository — Facts & Events knowledge graph.

Covers: people (Lazar, Chernobrov, JINR/LLNL physicists, FBI 11-cluster scientists,
ASRP team), institutions (JINR Dubna, LLNL, AFRL, NASA JPL, MIT PSFC, LANL,
Kosmopoisk, MAI, S-4, Faraday Labs, FBI, NGA, KazAtomProm, etc.),
phenomena (Element 115/Moscovium, Sport Model craft, Three-star UFO, Medveditskaya
Ridge, time-rate anomalies, UAP-FRAG-001), sources (peer-reviewed papers, primary
interviews, books, working methodology notes), facts (with confidence
tags: high / medium / low) and hypotheses (Lazar S-4 narrative, Lovondatr time
machine, OSINT validation pipeline, Cardillo Gabriella Rev A, Banchenko UAP origin
taxonomy, etc.).

Honesty policy: every Lazar / Chernobrov / single-witness claim is a `fact` with
`confidence="low"` and is linked BOTH to corroborating and contradicting facts.
Peer-reviewed primary-source claims (Phys. Rev. C 69 021601(R) 2004, GSI 2013
replication, IUPAC 2016 naming, FBI 2026-04-19 announcement) are `confidence="high"`.
ASRP-internal reproducible-but-not-yet-peer-reviewed material is `confidence="medium"`.

Output: uap_kumu.json — fed to preview.html for in-browser rendering, also drag-
and-drop into Kumu.io for cloud rendering.

ID compatibility: shared IDs with <asrp-marketing-repo>/
graph/asrp_kumu.json (e.g. p-lazar, p-chernobrov, p-cardillo, p-db, p-vo, inst-jinr,
inst-doe, pj-uap, th-temporal, th-3dt, th-hyperbolic, ev-ecp) — the two graphs
can be merged into one property-graph DB later via UNWIND.
"""
import json
from pathlib import Path

elements = []
connections = []
_seen_ids = set()

# Emoji icon per element type — rendered INSIDE the node circle as SVG data-URI.
TYPE_ICONS = {
    # reused from marketing graph
    "legal-entity":      "🏢",
    "person · team":     "👤",
    "person · external": "👥",
    "project":           "🚀",
    "patent":            "📜",
    "publication":       "📄",
    "channel":           "📡",
    "outreach":          "🤝",
    "institution":       "🏛️",
    "event":             "📅",
    "theory-anchor":     "💡",
    "tooling-class":     "🛠️",
    "cluster":           "🎯",
    "funding-source":    "💰",
    "accreditation":     "🏅",
    # NEW for UAP graph
    "fact":              "🧪",
    "phenomenon":        "🛸",
    "source":            "📜",
    "hypothesis":        "🧬",
}


_dup_definitions = []  # records every silently-skipped re-definition for audit

def E(eid, label, etype, label_ru=None, description_ru=None, **kwargs):
    """Emit one element. De-duplicates by id (first definition wins);
    re-definitions are recorded in _dup_definitions for audit so they
    surface in the build report instead of silently disappearing."""
    if eid in _seen_ids:
        _dup_definitions.append({"id": eid, "type": etype, "label": label,
                                 "description": kwargs.get("description", "")[:100]})
        return
    _seen_ids.add(eid)
    e = {"id": eid, "label": label, "type": etype, "icon": TYPE_ICONS.get(etype, "•")}
    if label_ru:
        e["labelRu"] = label_ru
    if description_ru:
        e["descriptionRu"] = description_ru
    e.update(kwargs)
    elements.append(e)


def C(efrom, eto, ctype="related-to", direction="directed", **kwargs):
    """Emit one connection."""
    c = {"from": efrom, "to": eto, "type": ctype, "direction": direction}
    c.update(kwargs)
    connections.append(c)


# ════════════════════════════════════════════════════════════════════════════
# 0. ANCHOR NODES — IDs shared with the ASRP marketing graph
#    Defined here so the UAP graph is standalone-renderable and ids stay
#    compatible for future merge into a single Neo4j-class DB.
# ════════════════════════════════════════════════════════════════════════════

# People — ASRP team
E("p-db", "Denis Y. Banchenko", "person · team",
  label_ru="Банченко Денис Юрьевич",
  description="Founder & CEO of ASRP · Program Director and methodology author for the UAP Reverse Engineering Study · author of the Banchenko-Technology stack and the 3-category UAP origin taxonomy",
  description_ru="Основатель и CEO ASRP · директор программы и автор методологии UAP Reverse Engineering Study · автор стека Banchenko-Technology и 3-категорной таксономии происхождения UAP",
  role="Program Director · Founder & CEO of ASRP",
  location="Baikonur, Kazakhstan")

E("p-vo", "Valeria A. Ovseannicova", "person · team",
  label_ru="Овсянникова Валерия Александровна",
  description="Director of Biomedical Research Department · plasma/agri/yeast protocol authorship · ECP session lead · reverse-engineering reproduction of artifact functions",
  description_ru="Директор департамента биомедицинских исследований · протоколы плазмы/агро/дрожжей · лидер ECP-сеансов · реверс-инжиниринг отдельных функций артефактов",
  role="CBE (Chief Biomedical Engineer)",
  location="Kishenev, Moldova")

E("p-mk", "Mykhailo M. Kapustin", "person · team",
  label_ru="Капустин Михаил Михайлович",
  description="CTO · Director of AI and IT Department · platform engineering · AI infrastructure across pipeline + ECP analytics",
  description_ru="CTO · директор департамента ИИ и ИТ · платформенная инженерия · инфраструктура ИИ для конвейера и аналитики ECP",
  role="CTO",
  location="Berlin, Germany")

E("p-kz", "Kyryl Zmiienko", "person · team",
  label_ru="Змиенко Кирилл",
  description="Chief AI Engineer · AI analysis, data validation, ECP protocol design · author of AI Pipeline Protocol v3.1 · conducted SigLIP2 control test 2026-04-09",
  description_ru="Главный ИИ-инженер · ИИ-анализ, валидация данных, дизайн протокола КП · автор протокола ИИ v3.1 · провёл контрольный тест SigLIP2 09.04.2026",
  role="Chief AI Engineer")

E("p-aovs", "Alexander Ovsyannikov", "person · team",
  label_ru="Овсянников Александр",
  description="IT Specialist · IT support across the UAP study pipelines",
  description_ru="ИТ-специалист · ИТ-поддержка конвейеров UAP",
  role="IT Specialist")

# Already-existing percipient
E("p-burilova", "Tatyana Burilova", "person · external",
  label_ru="Бурилова Татьяна",
  description="HSP Percipient · ECP-2026-04-04-003 session participant",
  description_ru="Перципиент ВСКЧ · участница сеанса ECP-2026-04-04-003")

# People — external (cross-graph anchors that get heavy usage from sub-agents)
E("p-lazar", "Bob Lazar", "person · external",
  label_ru="Боб Лазар",
  description="American claimant · in 1989 said he reverse-engineered alien craft propulsion at S-4 (Papoose Lake, Nevada) · introduced 'Element 115' as the propulsion fuel · most-cited modern UAP-disclosure source · credentials disputed",
  description_ru="Американский заявитель · в 1989 г. сообщил о реверс-инжиниринге двигательной установки внеземного аппарата на объекте S-4 (озеро Папуса, Невада) · ввёл «Элемент 115» как топливо · наиболее цитируемый современный источник UAP-разоблачения · академические документы оспорены")

E("p-chernobrov", "Vadim Chernobrov", "person · external",
  label_ru="Чернобров Вадим Александрович",
  description="Russian engineer and ufologist (1965–2017) · founder of Kosmopoisk (1982) · creator of the Lovondatr time-machine programme (1988–2017) · 32 published books · died 18 May 2017",
  description_ru="Российский инженер и уфолог (1965–2017) · основатель Космопоиска (1982) · создатель программы Ловондатр (1988–2017) · 32 опубликованные книги · умер 18 мая 2017 г.")

E("p-cardillo", "Robert Cardillo", "person · external",
  label_ru="Роберт Кардилло",
  description="Former Director of NGA (2014–2019) · published 'Gabriella Rev A' analytical framework on the 11-scientist cluster (LinkedIn, April 2026) · also engaged with the ASRP.media Dubna interview repost (2026-04-22)",
  description_ru="Бывший директор NGA (2014–2019) · опубликовал аналитическую рамку «Gabriella Rev A» по кластеру 11 учёных (LinkedIn, апрель 2026) · также взаимодействовал с репостом интервью ASRP.media о Дубне (22.04.2026)")

# Institutions — anchor IDs
E("inst-jinr", "JINR Dubna (Объединённый институт ядерных исследований)", "institution",
  label_ru="ОИЯИ Дубна (Объединённый институт ядерных исследований)",
  description="Joint Institute for Nuclear Research, Dubna · founded 1956 · 18 member states historically · primary site for synthesis of superheavy elements 113–118 · co-published Phys. Rev. C 69 021601(R) 2004 with LLNL on first synthesis of element 115",
  description_ru="ОИЯИ, Дубна · основан 1956 · 18 стран-членов исторически · основной центр синтеза сверхтяжёлых элементов 113–118 · соавтор Phys. Rev. C 69 021601(R) 2004 с LLNL по первому синтезу 115-го элемента",
  url="https://www.jinr.ru")

E("inst-doe", "U.S. Department of Energy / LANL", "institution",
  label_ru="Министерство энергетики США (DoE) / ЛАНЛ",
  description="US Department of Energy · operates LANL, LLNL, etc. · supplied the ²⁴³Am target enabling the 2003 Dubna synthesis · documented first reader on the UAP Reverse Engineering Study repo",
  description_ru="Министерство энергетики США · управляет ЛАНЛ, LLNL · поставило мишень ²⁴³Am для синтеза в Дубне 2003 · задокументированный первый читатель UAP-репозитория")

E("inst-darpa", "DARPA", "institution",
  label_ru="DARPA",
  description="US Defense Advanced Research Projects Agency · long-running Boeing reverse-engineering BAA programmes · ASRP holds DARPA BAA portal access (acc-darpa)",
  description_ru="Управление перспективных исследовательских проектов Минобороны США (DARPA) · многолетние программы реверс-инжиниринга Boeing по BAA · ASRP имеет доступ к порталу DARPA BAA (acc-darpa)")

E("inst-nswc", "NSWC IHD / NAVSEA", "institution",
  label_ru="NSWC IHD / NAVSEA",
  description="Naval Surface Warfare Center, Indian Head Division (under NAVSEA) · Robert Cardillo holds Configuration Management roles here (CCMP·CISCM)",
  description_ru="Naval Surface Warfare Center, Indian Head Division (входит в NAVSEA) · Роберт Кардилло занимает должности по управлению конфигурацией (CCMP·CISCM)")

# Project + cross-graph
E("pj-uap", "UAP_Reverse_Engineering_Study", "project",
  label_ru="UAP_Reverse_Engineering_Study",
  description="Public reverse-engineering analysis hub · 8 tracks: Artifact (UAP-FRAG-001) · Lazar · Chernobrov · Dubna · OSINT · People · Corporate · Cross-archive synthesis · DoE first-reader · ASRP-published",
  description_ru="Публичный хаб реверс-инжиниринга · 8 треков: Артефакт (UAP-FRAG-001) · Лазар · Чернобров · Дубна · OSINT · Люди · Корпоративный · Кросс-архивный синтез · первый читатель — DoE",
  status="🔬 research",
  url="https://github.com/AdvancedScientificResearchProjects/UAP_Reverse_Engineering_Study")

E("pj-plasma", "Hyperbolic_Field_BloodPlasma_Study", "project",
  label_ru="Hyperbolic_Field_BloodPlasma_Study",
  description="ASRP plasma study reproducing T₀/T₊/T₋ phenotype in plasma fibrin without thermal/chemical/ionizing exposure · drove the Cortical Labs engagement",
  description_ru="Исследование плазмы крови ASRP · воспроизведение фенотипа T₀/T₊/T₋ в фибрине плазмы без термического/химического/ионизирующего воздействия · стало триггером взаимодействия с Cortical Labs",
  status="🔬 research")

E("pat-fbhfs", "FBHFS — Fractal Biomedical Hyperbolic Field System (Kazpatent)", "patent",
  label_ru="FBHFS — Фрактальная биомедицинская система гиперболического поля (Казпатент)",
  description="KZ 2025/1095.1 · scientific base for DAAT Crystal + ASRP.fashion + plasma study · cited as the anchor patent under which UAP-adjacent oncology framing connects",
  description_ru="KZ 2025/1095.1 · научная база для DAAT Crystal + ASRP.fashion + исследования плазмы · якорный патент, под которым связана UAP-смежная онкологическая рамка")

# Theory anchors — already in marketing graph
E("th-temporal", "Temporal-desynchronization hypothesis", "theory-anchor",
  label_ru="Гипотеза темпоральной десинхронизации",
  description="Banchenko hypothesis that cancer phenotypes correspond to disturbed local-time-rate regimes (T₀/T₊/T₋) · communicated to Nolan as the core hypothesis · UAP-adjacent because the same field-physics framework is invoked",
  description_ru="Гипотеза Банченко: онкофенотипы соответствуют нарушенным локальным режимам темпа времени (T₀/T₊/T₋) · передана Nolan как ключевая · UAP-смежна, поскольку использует ту же полевую физику")

E("th-3dt", "Three-Dimensional Time framework", "theory-anchor",
  label_ru="Каркас 3D-времени",
  description="Three-dimensional time formalism · DOI 10.1142/S2424942425500045 · used by ASRP as the formal mathematical backbone for the temporal-desynchronization regime",
  description_ru="Формализм 3-мерного времени · DOI 10.1142/S2424942425500045 · используется ASRP как формальный математический каркас для режима темпоральной десинхронизации")

E("th-hyperbolic", "Hyperbolic Dispersion Materials for Cancer Detection", "theory-anchor",
  label_ru="Материалы с гиперболической дисперсией для онкодиагностики",
  description="Theoretical anchor cited in ASRP plasma + DAAT studies · justifies the FBHFS field protocols",
  description_ru="Теоретический якорь, цитируемый в исследованиях плазмы и DAAT ASRP · обосновывает протоколы FBHFS")

E("ev-ecp", "ECP-2026-04-04 session", "event",
  date="2026-04-04",
  label_ru="ECP-сеанс 04.04.2026",
  description="Master ECP-2026-04-04 session · UAP-FRAG-001 artifact study · 3 percipients · contains 3 sub-sessions",
  description_ru="Мастер-сеанс ECP-2026-04-04 · исследование артефакта UAP-FRAG-001 · 3 перципиента · содержит 3 подсессии")

# Track 1 / Track 7 cross-graph anchors (mirrored from ASRP marketing graph)
E("p-nolan", "Dr. Garry Nolan", "person · external",
  label_ru="Д-р Гарри Нолан",
  description="Stanford · Life Sciences, Bioinformatics, Cancer Research · UAP-adjacent oncology · documentary 'The Phenomenon of Disclosure'",
  description_ru="Стэнфорд · науки о жизни, биоинформатика, онкология · UAP-смежная онкология · фильм «The Phenomenon of Disclosure»",
  role="Stanford · Life Sciences, Bioinformatics, Cancer Research",
  location="Stanford, USA")

E("inst-stanford", "Stanford University", "institution",
  label_ru="Стэнфордский университет",
  description="Private research university · home of the Nolan Lab · target of Track-1 ECP / temporal-desync engagement",
  description_ru="Частный исследовательский университет · база Nolan Lab · цель аутрича Трека 1 (ECP / темпоральная десинхронизация)")

E("inst-cortical", "Cortical Labs", "institution",
  label_ru="Cortical Labs",
  description="Australian neural-organoid + biocompute startup · in active review of ASRP plasma research (2026-Q2) · Track-1 sibling-research bridge",
  description_ru="Австралийский стартап нейрооргaноидов и биовычислений · ведёт активный обзор плазменного исследования ASRP (Q2 2026) · мост к Track-1")

E("inst-boeing", "Boeing", "institution",
  label_ru="Boeing",
  description="US aerospace prime · disclosed DARPA BAA reverse-engineering line ≈$40M/year (illustrative DoD prime engagement target) · Track 7 placeholder for corporate / economic analysis",
  description_ru="Американский аэрокосмический prime · DARPA-BAA reverse-engineering line ≈$40 млн/год (DoD prime, иллюстративная цель) · placeholder для Track 7 (корпоративный/экономический анализ)")

# Track 2 (Lazar) — supporting persons / patrons named in bob-lazar-archive but not yet surfaced
E("p-bigelow", "Robert Bigelow", "person · external",
  label_ru="Роберт Бигелоу",
  description="American real-estate magnate · founder of Bigelow Aerospace and BAASS · funded the AAWSAP / DIA UAP-research programme · known associate of Lazar's circle and a major patron of post-1989 UAP investigation",
  description_ru="Американский магнат недвижимости · основатель Bigelow Aerospace и BAASS · финансировал программу AAWSAP / DIA по UAP · известный патрон расследований UAP после 1989 г.")

E("p-akers", "Mike Akers (Las Vegas Channel 8 cameraman)", "person · external",
  label_ru="Майк Эйкерс (оператор канала 8 Лас-Вегас)",
  description="KLAS-TV Channel 8 cameraman · filmed Lazar's 1989 Best Evidence interviews · technical witness whose footage anchors the original Lazar broadcast record",
  description_ru="Оператор KLAS-TV (канал 8) · снимал интервью Лазара «Best Evidence» 1989 г. · технический свидетель, чьи материалы являются якорем оригинальной трансляции Лазара")

E("inst-jfes", "JFES (Joint Financial / Engineering Services) — placeholder", "institution",
  label_ru="JFES — Joint Financial / Engineering Services (placeholder)",
  description="Track 7 placeholder · UAP reverse-engineering budget structure announced by Denis Banchenko (working session, 2026-04-26) · awaiting source material",
  description_ru="Placeholder Трека 7 · структура бюджета реверс-инжиниринга UAP, анонсирована Денисом Банченко (рабочая сессия, 26.04.2026) · ожидаются исходные материалы")

E("acc-darpa", "DARPA BAA proposal-portal access", "accreditation",
  label_ru="Доступ ASRP к порталу заявок DARPA BAA",
  description="ASRP holds DARPA BAA proposal-portal access · enables direct submission to Boeing-class reverse-engineering programmes",
  description_ru="ASRP имеет доступ к порталу заявок DARPA BAA · позволяет прямую подачу в программы реверс-инжиниринга класса Boeing")

E("or-doe", "DoE / Los Alamos — first-reader event", "outreach",
  label_ru="DoE / Лос-Аламос — событие первого читателя",
  description="Documented first-reader event on the UAP_Reverse_Engineering_Study repo immediately after publication · routes Track-1/4 disclosure to DoE channels",
  description_ru="Задокументированное событие первого читателя репозитория UAP_Reverse_Engineering_Study сразу после публикации · направляет раскрытие Трека-1/4 в каналы DoE")

E("or-stanford", "Stanford / Nolan Lab — admin handoff", "outreach",
  label_ru="Стэнфорд / Nolan Lab — admin-передача",
  description="Active outreach track · admin handoff via Dyan Dalton (Feb 2026) · ECP/temporal-desync framing communicated as core UAP-adjacent oncology hypothesis",
  description_ru="Активный аутрич-трек · admin-передача через Dyan Dalton (фев. 2026) · рамка ECP/темпоральной десинхронизации передана как ключевая UAP-смежная онко-гипотеза")

E("or-nci", "NCI SBIR FY26 — submission then systemic cancellation", "outreach",
  label_ru="NCI SBIR FY26 — подача и системная отмена",
  description="ASRP submitted novel therapeutic technology to NCI SBIR FY26 · programme-wide cancellation 2025-10-01 · documented cross-graph (or-nci in marketing graph)",
  description_ru="ASRP подал новую терапевтическую технологию в NCI SBIR FY26 · общесистемная отмена программы 01.10.2025 · задокументировано в кросс-графе (or-nci в маркетинг-графе)")

E("or-cortical", "Cortical Labs — active negotiations (2026-Q2)", "outreach",
  label_ru="Cortical Labs — активные переговоры (Q2 2026)",
  description="Cortical Labs is reviewing ASRP plasma research · 2026-Q2 active engagement · entry-point for Track-1 sibling-research validation",
  description_ru="Cortical Labs ведёт обзор плазменного исследования ASRP · активный контакт Q2 2026 · точка входа для валидации сибл-ресёрча Трека 1")

# Cross-graph source nodes (separate from theory-anchors so DOIs are filterable)
E("src-3dt-paper", "Three-Dimensional Time paper (2025)", "source",
  label_ru="Статья «Три измерения времени» (2025)",
  description="Three-Dimensional Time formalism · DOI 10.1142/S2424942425500045 · primary citable reference for the th-3dt theory anchor",
  description_ru="Формализм 3-мерного времени · DOI 10.1142/S2424942425500045 · первичная цитируемая ссылка для theory-anchor th-3dt",
  url="https://doi.org/10.1142/S2424942425500045")

E("src-hyperbolic-paper", "Hyperbolic Dispersion Materials for Cancer Detection paper", "source",
  label_ru="Статья «Материалы с гиперболической дисперсией для онкодиагностики»",
  description="Peer-reviewed paper on hyperbolic-dispersion materials for cancer detection · provides the theoretical backbone for FBHFS protocols · DOI to be confirmed (placeholder URL points at the in-repo lookup until DOI is published)",
  description_ru="Peer-reviewed статья по материалам с гиперболической дисперсией для онкодиагностики · обеспечивает теоретическую базу протоколов FBHFS · DOI уточняется (placeholder-URL указывает на in-repo lookup до публикации DOI)",
  url="https://www.researchgate.net/search/publication?q=hyperbolic%20dispersion%20materials%20cancer%20detection")

E("src-faruk-delphos-2021", "Erol Faruk — Delphos CE2 Case (2021)", "source",
  label_ru="Эрол Фарук — Дело Delphos CE2 (2021)",
  description="Erol Faruk · single-author peer-reviewed CE2-class chemistry analysis of the Delphos UAP physical-trace case · the only peer-reviewed chemical analysis in the Delphos record · confidence anchor for any 'biometal' claim around UAP-FRAG-001",
  description_ru="Эрол Фарук · одноавторская peer-reviewed CE2-химия следа НАЯ Дельфос · единственный рецензируемый химический анализ в материалах Delphos · якорь уверенности для «биометалла» вокруг UAP-FRAG-001")

E("src-percipient-sketch-237398", "Percipient hand-drawn disc sketch (2026-04-02)", "source",
  label_ru="Перципиентский набросок диска (02.04.2026)",
  description="Hand-drawn UAP disc sketch with annotation 'умер. часть / проводимость' · received from ECP-session percipient via Denis Banchenko · stored in repo at data/raw/percipient-sketches/2026-04-02_session_disc_sketch.jpg · primary visual context for UAP-FRAG-001",
  description_ru="Ручной набросок диска НАЯ с подписью «умер. часть / проводимость» · получен от перципиента ECP-сессии через Дениса Банченко · хранится в репо в data/raw/percipient-sketches/2026-04-02_session_disc_sketch.jpg · первичный визуальный контекст для UAP-FRAG-001",
  url="data/raw/percipient-sketches/2026-04-02_session_disc_sketch.jpg")

# Track-7 cluster (active — see fragments/agentE_track7_corporate.py for full population)
E("cluster-track7-corporate", "Track 7 — Corporate / Economic Analysis", "cluster",
  label_ru="Трек 7 — Корпоративный / экономический анализ",
  description="Defense-prime contractor constellation behind the UAP record. Anchor thesis: EG&G (1947) → URS (2002) → AECOM (2014) → Amentum (2020) → NYSE: AMTM (2024) is the documented Lazar-S-4-contractor lineage. Cluster includes 4 engineering primes (LMT, BA, RTX, NOC) + services-prime ring (Amentum, Leidos, Jacobs, etc.) + 2 HSP role-class scan targets at Amentum (public CEO scan target + public CTO scan target, depersonalized per protocol_corporate_scan.md v1.1). Public-source-only.",
  description_ru="Созвездие prime-подрядчиков обороны за UAP-нарративом. Якорный тезис: EG&G (1947) → URS (2002) → AECOM (2014) → Amentum (2020) → NYSE: AMTM (2024) — задокументированная линия подрядчика Lazar-S-4. Кластер включает 4 инженерных prime (LMT, BA, RTX, NOC) + сервисное кольцо (Amentum, Leidos, Jacobs и др.) + 2 ролево-классовые цели HSP-сканирования в Amentum (публичная цель CEO + публичная цель CTO, деперсонализировано по protocol_corporate_scan.md v1.1). Только публичные источники.")

# Additional Lazar-corpus persons (per review)
E("p-friedman", "Stanton T. Friedman", "person · external",
  label_ru="Стэнтон Фридман",
  description="Nuclear physicist (1934–2019) · ufology researcher · public Lazar critic · disputed Lazar's MIT/Caltech credentials and S-4 narrative on multiple shows",
  description_ru="Физик-ядерщик (1934–2019) · уфолог-исследователь · публичный критик Лазара · оспаривал документы MIT/Caltech и нарратив S-4 на ряде передач")

E("p-corbell", "Jeremy Kenyon Lockyer Corbell", "person · external",
  label_ru="Джереми Корбелл",
  description="American filmmaker · 'Bob Lazar: Area 51 & Flying Saucers' (2018) · co-host of recent BL18 / WeaponizedTV episodes with George Knapp",
  description_ru="Американский режиссёр · «Bob Lazar: Area 51 & Flying Saucers» (2018) · соведущий поздних BL18 / WeaponizedTV вместе с Джорджем Кнаппом")

E("p-rogan", "Joe Rogan", "person · external",
  label_ru="Джо Роган",
  description="Host of Joe Rogan Experience · interviewed Lazar (JRE #1315 in 2019, JRE #2479 in 2026) · interviewed Dan Farah (JRE #2416, 2025) on Age of Disclosure documentary",
  description_ru="Ведущий Joe Rogan Experience · интервью с Лазаром (JRE #1315 в 2019 г., JRE #2479 в 2026) · интервью с Дэном Фарой (JRE #2416, 2025 г.) о документальном «Age of Disclosure»")

# Split IUPAC and IUPAP
E("inst-iupap", "IUPAP — International Union of Pure and Applied Physics", "institution",
  label_ru="ИЮПАП — Международный союз теоретической и прикладной физики",
  description="Joint with IUPAC issued the 2011 decline of the 2004 Dubna element-115 discovery and the 2016 Moscovium naming · separate from IUPAC despite often joint Working Party action",
  description_ru="Совместно с ИЮПАК — отказ 2011 г. в признании дубнинского открытия 115-го элемента 2004 г. и наименование Московий в 2016 г. · отдельная организация от ИЮПАК, несмотря на частые совместные рабочие группы")

# Standalone events: NCI cancellation + DoE first-reader
E("ev-nci-cancellation-2025", "NCI SBIR FY26 programme cancellation", "event",
  date="2025-10-01",
  label_ru="Отмена программы NCI SBIR FY26 (01.10.2025)",
  description="NCI SBIR FY26 programme-wide cancellation · ASRP novel-therapeutic submission caught in the cancellation · documented in marketing-graph or-nci",
  description_ru="Общесистемная отмена программы NCI SBIR FY26 · подача ASRP по новой терапевтич. технологии попала под отмену · задокументировано в маркетинг-графе или-nci")

E("ev-doe-first-reader", "DoE / Los Alamos first-reader event on UAP repo", "event",
  date="2026",
  label_ru="DoE / Лос-Аламос — первый читатель UAP-репозитория",
  description="Documented first-reader event on the UAP_Reverse_Engineering_Study repository immediately after public release · routes the repo to DoE channels (no specific date disclosed)",
  description_ru="Задокументированное событие первого читателя репозитория UAP_Reverse_Engineering_Study сразу после публичного выпуска · направляет репозиторий в каналы DoE (точная дата не раскрыта)")

# JRE 2416 event
E("ev-jre-2416-farah", "Joe Rogan Experience #2416 — Dan Farah on Age of Disclosure", "event",
  date="2025",
  label_ru="Joe Rogan Experience #2416 — Дэн Фара об «Age of Disclosure»",
  description="JRE #2416 with Dan Farah · UAP-disclosure-context broadcast · Russian-dub copy archived in UAP repo · 7 cataloged claims in analysis/external-podcasts.md",
  description_ru="JRE #2416 с Дэном Фарой · транслирует контекст раскрытия НАЯ · копия с рус. дубляжом в репо · 7 каталогизированных claim-ов в analysis/external-podcasts.md")

# ASRP team / project linkage to UAP
C("p-db", "pj-uap", "founder & program-director", direction="directed")
C("p-vo", "pj-uap", "biomedical-research-director", direction="directed")
C("p-mk", "pj-uap", "CTO", direction="directed")
C("p-kz", "pj-uap", "Chief AI Engineer", direction="directed")

# Theory anchor linkage to ECP / artifact framing — bridge to marketing graph reuse
C("th-temporal", "pj-uap", "framing for", direction="directed")
C("th-3dt", "th-temporal", "formal backbone for", direction="directed")
C("th-hyperbolic", "th-temporal", "supports", direction="directed")
C("pat-fbhfs", "pj-uap", "scientific base", direction="directed")
C("pj-plasma", "pj-uap", "sibling research", direction="directed")
C("inst-doe", "pj-uap", "first-read by", direction="directed")


# ════════════════════════════════════════════════════════════════════════════
# 1. AGENT A — Dubna / Element 115 + Bob Lazar archive
# ════════════════════════════════════════════════════════════════════════════
exec(Path(__file__).parent.joinpath("fragments/agentA_dubna_lazar.py").read_text(encoding="utf-8"))

# ════════════════════════════════════════════════════════════════════════════
# 2. AGENT B — Chernobrov / Kosmopoisk archive
# ════════════════════════════════════════════════════════════════════════════
exec(Path(__file__).parent.joinpath("fragments/agentB_chernobrov.py").read_text(encoding="utf-8"))

# ════════════════════════════════════════════════════════════════════════════
# 3. AGENT C — OSINT methodology + 11-scientist cluster + cross-archive synthesis
# ════════════════════════════════════════════════════════════════════════════
exec(Path(__file__).parent.joinpath("fragments/agentC_osint_people.py").read_text(encoding="utf-8"))

# ════════════════════════════════════════════════════════════════════════════
# 4. AGENT D — Track 1 ECP + AI/CV multi-pipeline study (UAP-FRAG-001)
# ════════════════════════════════════════════════════════════════════════════
exec(Path(__file__).parent.joinpath("fragments/agentD_track1.py").read_text(encoding="utf-8"))

# ════════════════════════════════════════════════════════════════════════════
# 5. AGENT E — Track 7 Corporate / Economic Analysis (EG&G → Amentum lineage)
# ════════════════════════════════════════════════════════════════════════════
exec(Path(__file__).parent.joinpath("fragments/agentE_track7_corporate.py").read_text(encoding="utf-8"))

# ════════════════════════════════════════════════════════════════════════════
# 6. AGENT F — Theoretical foundations sub-archive (Track 7 sub-cluster)
# ════════════════════════════════════════════════════════════════════════════
exec(Path(__file__).parent.joinpath("fragments/agentF_theoretical_foundations.py").read_text(encoding="utf-8"))

# ════════════════════════════════════════════════════════════════════════════
# 7. AGENT G — Track 9 UAP scientific publications corpus
# ════════════════════════════════════════════════════════════════════════════
exec(Path(__file__).parent.joinpath("fragments/agentG_uap_publications.py").read_text(encoding="utf-8"))


# ════════════════════════════════════════════════════════════════════════════
# 8. CROSS-ARCHIVE BRIDGES — connections that span sub-agent outputs
# ════════════════════════════════════════════════════════════════════════════

# Lazar ↔ Dubna: element 115 as the critical bridge
C("phen-mc115", "hyp-lazar-s4", "central-claim-of", direction="directed")
C("hyp-cb-soviet-lineage", "hyp-lazar-s4", "parallel-but-disjoint", direction="undirected")

# Chernobrov ↔ Lazar: explicit non-reference (Soviet vs American line)
C("hyp-cb-soviet-lineage", "p-lazar", "does-not-reference", direction="directed")

# OSINT methodology applied to the four data-bearing sibling tracks
C("meth-uap-application", "phen-mc115", "applies-to-as-positive-control", direction="directed")
C("meth-uap-application", "hyp-lazar-s4", "applies-to-as-failed-validation", direction="directed")
C("meth-uap-application", "hyp-cb-time-machine", "applies-to-as-partial-failure", direction="directed")
C("meth-uap-application", "cluster-fbi-11", "applies-to-as-statistical-signature", direction="directed")
C("meth-uap-application", "phen-uap-frag-001", "applies-to-with-error-mode-3", direction="directed")
C("meth-validation-pipeline", "meth-uap-application", "instantiated-by", direction="directed")
C("meth-signature-methodology", "meth-validation-pipeline", "feeds", direction="directed")
C("meth-anomaly-classes", "meth-validation-pipeline", "feeds", direction="directed")

# UAP repo as parent project of every track
C("pj-uap", "phen-mc115",         "investigates (Track 4)", direction="directed")
C("pj-uap", "p-chernobrov",       "investigates (Track 3)", direction="directed")
C("pj-uap", "p-lazar",            "investigates (Track 2)", direction="directed")
C("pj-uap", "phen-uap-frag-001",  "investigates (Track 1)", direction="directed")
C("pj-uap", "cluster-fbi-11",     "investigates (Track 6)", direction="directed")
C("pj-uap", "meth-validation-pipeline", "uses methodology (Track 5)", direction="directed")

# Cardillo connecting role: NSWC IHD + Cardillo ↔ FBI cluster + ASRP outreach
C("p-cardillo", "inst-nswc", "employed-at", direction="directed")
C("p-cardillo", "inst-nga",  "former-director-of", direction="directed")

# ─── REVIEW FIX BRIDGES ─────────────────────────────────────────────
# (1) cross-graph anchor connections
C("p-nolan", "inst-stanford", "employed-at", direction="directed")
C("inst-stanford", "or-stanford", "subject of engagement", direction="directed")
C("inst-cortical", "or-cortical", "subject of engagement", direction="directed")
C("or-cortical", "pj-plasma", "engaged-with", direction="directed")
C("or-stanford", "th-temporal", "communicated to Nolan as core hypothesis", direction="directed")
C("p-nolan", "th-temporal", "engaged-as", direction="directed")
C("or-nci", "ev-nci-cancellation-2025", "documented-by", direction="directed")
C("or-doe", "ev-doe-first-reader", "documented-by", direction="directed")
C("ev-doe-first-reader", "pj-uap", "first-read event on the repo", direction="directed")
C("inst-doe", "or-doe", "submission to authority", direction="directed")
C("acc-darpa", "inst-darpa", "DARPA BAA proposal-portal access", direction="directed")
C("inst-boeing", "pj-uap", "DoD reverse-engineering benchmark target", direction="directed")
C("inst-boeing", "cluster-track7-corporate", "member-of", direction="directed")
C("inst-jfes", "cluster-track7-corporate", "member-of", direction="directed")
C("inst-darpa", "cluster-track7-corporate", "related-to", direction="directed")
C("cluster-track7-corporate", "pj-uap", "scope-of", direction="directed")

# (2) DOI source nodes link to theory anchors
C("src-3dt-paper", "th-3dt", "documents", direction="directed")
C("src-hyperbolic-paper", "th-hyperbolic", "documents", direction="directed")
C("src-3dt-paper", "th-temporal", "formal backbone for", direction="directed")

# (3) Faruk Delphos source as confidence anchor for "biometal" framing
C("src-faruk-delphos-2021", "phen-uap-frag-001", "confidence anchor for material-class claim", direction="directed")
C("src-faruk-delphos-2021", "f-ai-coral-material", "supports", direction="directed")
C("p-db", "src-faruk-delphos-2021", "cites", direction="directed")

# (4) Percipient sketch source
C("src-percipient-sketch-237398", "phen-uap-frag-001", "primary visual context", direction="directed")
C("src-percipient-sketch-237398", "ev-ecp", "submitted by percipient at", direction="directed")

# (5) Honesty-policy patches: 3 missing Lazar challenge edges (CRITICAL #3)
C("f-lazar-credentials-disputed",  "f-lazar-electret-hull-2026", "challenges", direction="directed")
C("f-lazar-credentials-disputed",  "f-lazar-la1000-codename",    "challenges", direction="directed")
C("f-lazar-credentials-disputed",  "f-lazar-s4-tenure",          "challenges", direction="directed")
C("f-mc115-no-practical-use",      "f-lazar-electret-hull-2026", "contradicts physics-of", direction="directed")
C("f-cardillo-no-attribution",     "f-mccasland-uap-hint",       "challenges", direction="directed")
C("f-coordinated-action-not-concluded", "f-mccasland-uap-hint",  "challenges", direction="directed")

# (6) New persons → Lazar-corpus bridges
C("p-friedman", "p-lazar", "publicly disputed", direction="directed")
C("p-friedman", "f-lazar-credentials-disputed", "supports", direction="directed")
C("p-corbell", "src-bl18", "produced", direction="directed")
C("p-rogan", "src-jre-1315", "host of", direction="directed")
C("p-rogan", "src-jre-2479", "host of", direction="directed")
C("p-rogan", "ev-jre-2416-farah", "hosted", direction="directed")

# (7) JRE-2416 event chains
C("ev-jre-2416-farah", "src-jre-2416-farah", "documented-by", direction="directed")
C("ev-jre-2416-farah", "p-lazar", "discusses", direction="directed")

# (8) IUPAC ↔ IUPAP split
C("inst-iupap", "ev-iupac-declines-2011", "co-issued", direction="directed")
C("inst-iupap", "ev-iupac-moscovium-2016", "co-issued", direction="directed")
C("inst-iupap", "inst-iupac", "joint-working-party-with", direction="directed")

# (9) Track 2 supporting persons (Bigelow, Akers)
C("p-bigelow", "p-lazar", "patron of UAP research circle", direction="directed")
C("p-akers", "src-klas-1989a", "filmed", direction="directed")
C("p-akers", "src-klas-1989b", "filmed", direction="directed")
C("p-bigelow", "inst-darpa", "AAWSAP-related institutional context", direction="directed")

# Orphan-fix bridges (close out nodes that sub-agents defined but didn't connect)
C("p-aovs", "pj-uap", "IT-specialist for", direction="directed")
C("inst-darpa", "pj-uap", "potential reverse-engineering programme target", direction="directed")
C("inst-iupac", "ev-iupac-moscovium-2016", "issued naming recommendation", direction="directed")
C("inst-iupac", "ev-iupac-declines-2011", "issued initial decline", direction="directed")
C("inst-iupac", "ev-gsi-replication-2013", "accepted after replication", direction="directed")
C("ev-jinr-founded", "f-jinr-founded-1956", "documented-by", direction="directed")
C("inst-jinr", "f-jinr-founded-1956", "characterised-by", direction="directed")
C("ev-setka-launched-1977", "f-setka-launched", "documented-by", direction="directed")
C("inst-izmiran", "ev-setka-launched-1977", "coordinated", direction="directed")
C("ev-lazar-jre2026", "src-jre-2479", "documented-by", direction="directed")
C("p-lazar", "ev-lazar-jre2026", "appeared-at", direction="directed")
C("ev-osint-methodology-captured", "src-osint-methodology-notes", "produced", direction="directed")
C("p-db", "ev-osint-methodology-captured", "captured", direction="directed")
C("ev-ai-llm-visual", "src-ai-llm-report", "documented-by", direction="directed")
C("src-ai-llm-report", "tool-llm-visual", "describes-output-of", direction="directed")


# ════════════════════════════════════════════════════════════════════════════
# 6. ENRICH WITH TAGS + DUPLICATE-DETECTION REPORT
# ════════════════════════════════════════════════════════════════════════════

# Russian labels for facts/events that the sub-agents emitted with description_ru
# only — patched here as a single source of truth so coverage hits the ≥85 % target.
RU_LABEL_PATCHES = {
    # Dubna / Element 115 (agent A)
    "f-mc115-synth-2003":               "Первый синтез 115-го элемента (ОИЯИ + LLNL, 2003)",
    "f-mc115-iupac-name":               "IUPAC присвоил название Московий (Mc) — 28.11.2016",
    "f-mc115-halflives":                "Все известные изотопы Mc — мс…секунды (нестабильны)",
    "f-mc115-no-practical-use":         "ОИЯИ: у самого 115-го элемента нет практического применения",
    "f-llnl-am243-supplier":            "LLNL поставила мишень ²⁴³Am для синтеза 2003 г.",
    "f-usa-never-jinr-member":          "США никогда не были членом ОИЯИ (равноправный соавтор, не участник)",
    "f-shef-70-atoms":                  "Фабрика СТЭ — первый эксперимент: ~70 атомов Mc за 40 дней",
    "f-shef-100-flerovium":             "Фабрика СТЭ — второй эксперимент: ~100 атомов флеровия (Fl)",
    "f-gsi-replication-2013":           "GSI Дармштадт + Лунд независимо воспроизвели синтез (август 2013)",
    "f-jinr-founded-1956":              "ОИЯИ основан 26 марта 1956 г. в Дубне 11 государствами",
    "f-setka-launched":                 "Запущены советские UAP-программы СЕТКА-АН и СЕТКА-МО (1977–1978)",
    "f-kazakhstan-uranium":             "Казахстан — крупнейший производитель урана (КазАтомПром >40 % мирового)",
    "f-lazar-claimed-element-115-1989": "Лазар публично заявил о Элементе 115 как топливе S-4 (1989)",
    "f-lazar-115-existence-correct":    "Существование 115-го элемента: заявление Лазара 1989 г. оказалось верным",
    "f-lazar-115-stability-disputed":   "Стабильный изотоп 115-го по Лазару — оспаривается данными ОИЯИ/SHEF",
    "f-lazar-credentials-disputed":     "Академические документы Лазара (MIT/Caltech) — оспорены",
    "f-lazar-223g-claim":               "Лазар: 223 г 115-го на загрузку реактора — превышает мировое производство",
    "f-lazar-reactor-mechanism-claim":  "Лазар: бомбардировка протонами 115-го → антиматерия (механизм)",
    "f-lazar-gravity-claim":            "Лазар: 115-й излучает усиливаемые волны Гравитации-A",
    "f-lazar-la1000-codename":          "Лазар: внутриобъектный код 115-го — «LA-1000»",
    "f-knapp-physicists-2018":          "Кнапп 2018: 3 физика «не смогли исключить» стабильную версию 115-го",
    "f-lear-misattrib-antimatter":      "Фраза «115→116→антиматерия» — Джона Лира (1998), не Лазара",
    "f-mc115-no-natural-occurrence":    "У 115-го элемента нет природных изотопов на Земле",
    "f-asrp-psycholinguistic-editorial":"Психолингвистическая сноска ASRP.media — редакционная рамка, не ОИЯИ",
    "f-shef-targets-119-120":           "Фабрика СТЭ нацелена на синтез 119-го и 120-го (2020–)",
    "f-moore-mc290-not-stable":         "Мур 2025: Mc-290 → ~1.52 с (всё ещё не стабилен)",
    "f-lazar-sport-model-dims":         "Размеры Sport Model в корпусе Лазара дрейфуют (52→40→52 фт)",
    "f-lazar-electret-hull-2026":       "Лазар 2026: гипотеза электретной обшивки Sport Model (новое утверждение)",
    "f-lazar-s4-tenure":                "Лазар: пребывание на S-4 — декабрь 1988 – апрель 1989 (стабильно в корпусе)",
    "f-jinr-18-countries-2021":         "Представитель ОИЯИ: «представители 18 стран работают здесь» (2021)",
    "ev-lazar-jre2026":                 "Лазар на Joe Rogan Experience #2479 (2026)",
    "ev-setka-launched-1977":           "Запуск советских СЕТКА-АН/МО UAP-программ (1977–1978)",
    # Chernobrov (agent B)
    "f-cb-lovondatr-name-origin":       "Название «Ловондатр» — прикрытие МАИ (ловушка для ондатр)",
    "f-cb-lovondatr7-geometry":         "Ловондатр-7: матрёшка 30 см / 1 м / 2.1 м, 7 ЭРП",
    "f-cb-konov-result":                "Опыт Конова: ≈−3 % замедления времени за 30 мин (26.08.2001)",
    "f-cb-lethal-threshold":            "Летальный порог: 1.5 с/живой цикл",
    "f-cb-f-c-over-d":                  "Формула резонанса f = c/d; d = 7 мм → ≈43 ГГц",
    "f-cb-patent-never-granted":        "Патент РФ 2003110067 не выдан (FA92-прекращён 21.04.2005)",
    "f-cb-50-mg-expeditions":           "~50 экспедиций на Медведицкую гряду 1982–2014, ~906 добровольцев",
    "f-cb-153-pictograms":              "153 аутентичных пиктограммы каталогизированы 1950–2010",
    "f-cb-piloted-tm-forecast-unmet":   "Прогноз «пилотируемая МВ через 10–15 лет» не реализован к 2017",
    "f-cb-tm-no-peer-review":           "Рецензированных воспроизведений Ловондатра не найдено",
    "f-cb-mice-deaths":                 "Первая серия Ловондатра: 31 мышь, 25 погибших",
    # People-cluster (agent C)
    "ev-eskridge-death":                "Эми Эскридж: смерть при неясных обстоятельствах",
    "ev-chavez-disappear":              "Энтони Чавес: исчезновение в районе Альбукерке",
    "ev-cassias-disappear":             "Мелисия Кассиас: исчезновение в районе Лос-Аламоса",
    "ev-tores-disappear":               "Моника Хасин-Тореза: исчезновение в калифорнийском лесу",
    "ev-garcia-disappear":              "Стивен Абел Гарсия: исчезновение в районе Канзас-Сити",
    "ev-thomas-found-dead":             "Джейсон Томас: тело найдено в озере (Массачусетс)",
    "ev-loureiro-killed":               "Нуно Лаурейро: убит в MIT",
    "ev-mccasland-disappear":           "Уильям Маккаслэнд: исчезновение в Альбукерке",
    "ev-grillmar-killed":               "Карл Грилмар: убит у себя дома (Калифорния)",
    "ev-fbi-consolidate":               "ФБР консолидирует расследование 11 учёных (19.04.2026)",
    "ev-cardillo-linkedin-post":        "Кардилло публикует «Gabriella Rev A» в LinkedIn",
    "ev-db-linkedin-comment":           "Банченко публикует ссылку на UAP-исследование под постом Кардилло",
    "ev-osint-methodology-captured":    "Документирование OSINT-методологии сигнатур Банченко (26.04.2026)",
    "f-cluster-status-breakdown":       "Кластер статусов: 5 исчезли / 2 убиты / 1 найден мёртв / 3 неясно",
    "f-cluster-geo-ca-nm":              "Калифорния (4) + Нью-Мексико (3) = 7/11 кейсов",
    "f-cluster-time-concentration":     "8 из 11 кейсов сконцентрированы в 2025–2026 гг.",
    "f-cassias-phone-reset":            "Мелисия Кассиас: оба телефона сброшены до заводских до исчезновения",
    "f-mccasland-uap-hint":             "Транскрипт о Маккаслэнде: один генерал работал с UAP/UFO-программами",
    "f-fbi-search-patterns":            "ФБР ведёт 8 кросс-кейсовых паттернов поиска (Патель 19.04.2026)",
    "f-cluster-specialisation-homogeneity": "Все 11 кейсов: ядерное/двигатели/плазма/астрофизика/UAP-сферы",
    "f-lanl-two-in-one-month":          "ЛАНЛ: два сотрудника исчезли в мае–июне 2025 г. с интервалом в месяц",
    "f-jpl-three-cases":                "NASA JPL: 3 фигуранта — крупнейший институциональный кластер",
    "f-cardillo-no-attribution":        "«Gabriella Rev A» Кардилло — без присвоения мотива (не конспирологична)",
    "f-coordinated-action-not-concluded":"Координированный мотив не доказан — disclaimer (high-confidence anti-вывод)",
    # ev orphans potentially introduced by the new patches — pre-emptive coverage
}
for el in elements:
    if el["id"] in RU_LABEL_PATCHES:
        el["labelRu"] = RU_LABEL_PATCHES[el["id"]]
    el.setdefault("tags", [el["type"]])

# Validation: dangling connections (from/to id not in elements)
known_ids = {el["id"] for el in elements}
dangling = [(c["from"], c["to"], c["type"]) for c in connections
            if c["from"] not in known_ids or c["to"] not in known_ids]
orphan_ids = known_ids - {c["from"] for c in connections} - {c["to"] for c in connections}

# Confidence breakdown
conf_breakdown = {"high": 0, "medium": 0, "low": 0, "unspecified": 0}
for el in elements:
    if el["type"] == "fact":
        c = el.get("confidence", "unspecified")
        conf_breakdown[c if c in conf_breakdown else "unspecified"] += 1

# RU coverage
ru_label_count = sum(1 for el in elements if el.get("labelRu"))
ru_desc_count = sum(1 for el in elements if el.get("descriptionRu"))


# ════════════════════════════════════════════════════════════════════════════
# 7. WRITE JSON
# ════════════════════════════════════════════════════════════════════════════

out_path = Path(__file__).parent / "uap_kumu.json"
out_path.write_text(json.dumps({
    "elements": elements,
    "connections": connections,
}, ensure_ascii=False, indent=2))

# Stats report
print(f"Wrote {out_path}")
print(f"  elements   : {len(elements)}")
print(f"  connections: {len(connections)}")
if _dup_definitions:
    print(f"  duplicate-id skips: {len(_dup_definitions)}")
    for d in _dup_definitions:
        print(f"    SKIPPED {d['id']:<22} ({d['type']}): {d['label'][:60]}")
print(f"  orphans    : {len(orphan_ids)}  {'(' + ', '.join(sorted(orphan_ids)) + ')' if orphan_ids else ''}")
print(f"  dangling C : {len(dangling)}")
if dangling:
    for f, t, k in dangling[:20]:
        miss = f if f not in known_ids else t
        print(f"    {f} -[{k}]-> {t}   (missing: {miss})")
print(f"  facts:")
for k, v in conf_breakdown.items():
    print(f"    confidence={k:<12} : {v}")
print(f"  RU label coverage      : {ru_label_count}/{len(elements)} = {100*ru_label_count/len(elements):.1f}%")
print(f"  RU description coverage: {ru_desc_count}/{len(elements)} = {100*ru_desc_count/len(elements):.1f}%")

# Type breakdown
type_counts = {}
for el in elements:
    type_counts[el["type"]] = type_counts.get(el["type"], 0) + 1
print(f"  type breakdown:")
for t, n in sorted(type_counts.items(), key=lambda x: -x[1]):
    print(f"    {t:<22} : {n}")
