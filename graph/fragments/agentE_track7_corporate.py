# ════════════════════════════════════════════════════════════════════
# AGENT E — Track 7 Corporate / Economic Analysis
# Sources: corporate-economic-analysis/README.md + analysis/*.md +
#          companies/*.md + people/_scan-targets/*.md
# Authored 2026-04-26..27 working sessions
# ════════════════════════════════════════════════════════════════════

# ----- INSTITUTIONS — defense primes + EG&G genealogy ------------------

E("inst-egng", "EG&G Inc. (defunct standalone since 2002)", "institution",
  label_ru="EG&G Inc. (несамостоятельна с 2002)",
  description="US defense and technical-services contractor founded 1947 by Edgerton, Germeshausen, and Grier as MIT spin-off to instrument US nuclear-weapons tests. Principal NTS instrumentation contractor 1947–1992. EG&G Special Projects (Las Vegas) operated portions of NTS. Acquired by URS Corporation in 2002. Bob Lazar's stated employer-of-record at S-4.",
  description_ru="Американский оборонный и технико-сервисный подрядчик, основан в 1947 г. Эдгертоном, Гермесгаузеном, Грайером как спин-офф MIT для приборного обеспечения ядерных испытаний. Основной подрядчик приборного обеспечения NTS 1947–1992. EG&G Special Projects (Лас-Вегас) обслуживало части NTS. Поглощена URS Corporation в 2002. Заявленный Лазаром формальный работодатель на S-4.",
  source="corporate-economic-analysis/companies/egng.md")

E("inst-urs", "URS Corporation (acquired by AECOM 2014)", "institution",
  label_ru="URS Corporation (поглощена AECOM в 2014)",
  description="US engineering and construction-services firm. Acquired EG&G's federal-services line in 2002. Acquired by AECOM in 2014. Intermediate node in the EG&G → Amentum corporate genealogy.",
  description_ru="Американская инжиниринговая и строительно-сервисная фирма. Поглотила федерально-сервисную линию EG&G в 2002. Поглощена AECOM в 2014. Промежуточный узел в корпоративной генеалогии EG&G → Amentum.",
  source="corporate-economic-analysis/analysis/egng-amentum-succession.md")

E("inst-aecom", "AECOM (NYSE: ACM)", "institution",
  label_ru="AECOM (NYSE: ACM)",
  description="US engineering, construction, and management-services firm. Acquired URS in 2014. Spun off Management Services as Amentum in 2020. Intermediate node in the EG&G → Amentum corporate genealogy. Continues as standalone entity post-spinoff.",
  description_ru="Американская инжиниринговая, строительная и управленческо-сервисная фирма. Поглотила URS в 2014. Выделила Management Services в Amentum в 2020. Промежуточный узел в корпоративной генеалогии EG&G → Amentum. Продолжает существовать как самостоятельный субъект после spinoff.",
  source="corporate-economic-analysis/companies/egng.md")

E("inst-amentum", "Amentum Holdings (NYSE: AMTM)", "institution",
  label_ru="Amentum Holdings (NYSE: AMTM)",
  description="US engineering and technical-services prime contractor. Spun off from AECOM Management Services 2020. Merged with Jacobs Critical Mission Solutions (CMS) 2024. Listed NYSE: AMTM in post-merger structure. Member of Triad LLC (LANL operator) and LLNS LLC (LLNL operator). Present-day successor of the EG&G federal-services lineage.",
  description_ru="Американский инжиниринговый и технико-сервисный prime-подрядчик. Выделена из AECOM Management Services в 2020 г. Слилась с Jacobs Critical Mission Solutions (CMS) в 2024 г. Листинг NYSE: AMTM в посткорпоративной структуре. Член Triad LLC (оператор LANL) и LLNS LLC (оператор LLNL). Современный преемник линии федеральных сервисов EG&G.",
  source="corporate-economic-analysis/companies/amentum.md")

E("inst-jacobs", "Jacobs Solutions (NYSE: J)", "institution",
  label_ru="Jacobs Solutions (NYSE: J)",
  description="US engineering and professional-services firm. Spun off Critical Mission Solutions (CMS) division which merged into Amentum in 2024. Member of MSTS LLC (NNSS operator).",
  description_ru="Американская инжиниринговая и профессионально-сервисная фирма. Выделила подразделение Critical Mission Solutions (CMS), которое слилось с Amentum в 2024. Член MSTS LLC (оператор NNSS).",
  source="corporate-economic-analysis/companies/amentum.md")

E("inst-leidos", "Leidos Holdings (NYSE: LDOS)", "institution",
  label_ru="Leidos Holdings (NYSE: LDOS)",
  description="US defense, intelligence, and engineering services prime. Spun off from SAIC in 2013. Absorbed Lockheed Martin's Information Systems & Global Solutions (IS&GS) in 2016. Member of CNS LLC (Y-12 / Pantex operator). Co-inheritor of LM federal-services line.",
  description_ru="Американский prime в обороне, разведсервисах и инжиниринге. Выделена из SAIC в 2013. Поглотила Information Systems & Global Solutions (IS&GS) Lockheed Martin в 2016. Член CNS LLC (оператор Y-12 / Pantex). Сонаследник линии федеральных сервисов LM.",
  source="corporate-economic-analysis/companies/leidos.md")

E("inst-lmt", "Lockheed Martin (NYSE: LMT)", "institution",
  label_ru="Lockheed Martin (NYSE: LMT)",
  description="Largest US defense prime by revenue. Skunk Works (Advanced Development Programs, Palmdale) — historical SR-71, F-117, F-22 black programs. Lockheed Martin Space (Denver) handles classified satellite payloads. Historical operator of LANL via LANS LLC (until 2018 transition to Triad LLC).",
  description_ru="Крупнейший американский оборонный prime по выручке. Skunk Works (Advanced Development Programs, Палмдейл) — исторические чёрные программы SR-71, F-117, F-22. Lockheed Martin Space (Денвер) — секретные спутниковые полезные нагрузки. Исторически — оператор LANL через LANS LLC (до перехода 2018 г. на Triad LLC).",
  source="corporate-economic-analysis/companies/lockheed-martin.md")

E("inst-boeing", "Boeing (NYSE: BA)", "institution",
  label_ru="Boeing (NYSE: BA)",
  description="US engineering prime, dual-use aerospace/defense. Phantom Works (advanced prototyping, St. Louis / Huntington Beach) — analog of Skunk Works. Typical responder to DARPA Aerospace-Innovations BAA RFPs cited as benchmark in Track 5 OSINT methodology.",
  description_ru="Американский инженерный prime двойного назначения авиакосмос / оборона. Phantom Works (продвинутое прототипирование, Сент-Луис / Хантингтон-Бич) — аналог Skunk Works. Типичный респондент DARPA Aerospace-Innovations BAA RFP, упоминаемых как benchmark в OSINT-методологии Трека 5.",
  source="corporate-economic-analysis/companies/boeing.md")

E("inst-rtx", "RTX Corporation (NYSE: RTX)", "institution",
  label_ru="RTX Corporation (NYSE: RTX)",
  description="US engineering prime, formed by 2020 merger of Raytheon and United Technologies; renamed RTX 2023. Sensor / radar / EW heritage: AESA radars (APG-79/APG-82), Patriot, hypersonics, AMRAAM. Dominant US sensor / radar / EW supplier.",
  description_ru="Американский инженерный prime, образован слиянием Raytheon и United Technologies в 2020 г.; переименован в RTX в 2023. Наследие сенсоров / РЛС / РЭБ: AESA РЛС (APG-79/APG-82), Patriot, гиперзвук, AMRAAM. Доминирующий американский поставщик сенсоров / РЛС / РЭБ.",
  source="corporate-economic-analysis/companies/raytheon-rtx.md")

E("inst-noc", "Northrop Grumman (NYSE: NOC)", "institution",
  label_ru="Northrop Grumman (NYSE: NOC)",
  description="US engineering prime. B-2 Spirit and B-21 Raider stealth bombers; classified space and missile-defense work. Pantex partner. Canonical example of long-running classified-aerospace programmatic structure.",
  description_ru="Американский инженерный prime. Стелс-бомбардировщики B-2 Spirit и B-21 Raider; засекреченные космос и ПРО. Партнёр Pantex. Канонический пример долгосрочной программной структуры засекреченного авиакосмоса.",
  source="corporate-economic-analysis/companies/northrop-grumman.md")

# ----- PEOPLE — public C-level executives ------------------------------

E("p-amtm-ceo-scan-target", "Public CEO scan target — Amentum Holdings", "person · external",
  label_ru="Публичная цель сканирования CEO — Amentum Holdings",
  description="Role-class scan target: the public CEO of Amentum Holdings (post-2024-merger structure). Subject of HSP role-class scan 2026-04-26 per protocol_corporate_scan.md v1.1 (depersonalization-by-default). Subject's full legal name is intentionally NOT recorded in this graph or in the public dossier; the dossier addresses the role-class signal layer only. Public-source references only: corporate 'About' page + public LinkedIn metadata (no photographs stored in repo).",
  description_ru="Цель сканирования ролевого класса: публичный CEO Amentum Holdings (структура после слияния 2024 г.). Субъект HSP-сканирования ролевого класса 26.04.2026 по protocol_corporate_scan.md v1.1 (деперсонализация по умолчанию). Полное юридическое имя субъекта намеренно НЕ фиксируется в графе или публичном досье; досье обращается только к слою сигнала ролевого класса. Только публичные источники: корпоративная страница «About» + публичные LinkedIn-метаданные (фотографии в репо не сохраняются).",
  source="corporate-economic-analysis/people/_scan-targets/amentum-ceo-scan-target.md")

E("p-amtm-cto-scan-target", "Public CTO scan target — Amentum Holdings", "person · external",
  label_ru="Публичная цель сканирования CTO — Amentum Holdings",
  description="Role-class scan target: the public CTO of Amentum Holdings (recognised on a 'Top CTO to Watch 2026' listing). Subject of HSP role-class scan 2026-04-26 per protocol_corporate_scan.md v1.1 (depersonalization-by-default). CTO-class scan registers stronger technical-content markers than CEO-class scan. Subject's full legal name is intentionally NOT recorded in this graph or in the public dossier. Public-source references only: corporate 'About' page + public LinkedIn metadata (no photographs stored in repo).",
  description_ru="Цель сканирования ролевого класса: публичный CTO Amentum Holdings (отмечена в публичном листинге «Top CTO to Watch 2026»). Субъект HSP-сканирования ролевого класса 26.04.2026 по protocol_corporate_scan.md v1.1 (деперсонализация по умолчанию). Сканирование класса CTO регистрирует более сильные маркеры технического содержания, чем класс CEO. Полное юридическое имя субъекта намеренно НЕ фиксируется в графе или публичном досье. Только публичные источники: корпоративная страница «About» + публичные LinkedIn-метаданные (фотографии в репо не сохраняются).",
  source="corporate-economic-analysis/people/_scan-targets/amentum-cto-scan-target.md")

# ----- EVENTS — M&A genealogy ------------------------------------------

E("ev-egng-urs-acquisition-2002", "URS acquires EG&G technical-services (2002)", "event",
  date="2002",
  label_ru="URS поглощает EG&G technical-services (2002)",
  description="2002 acquisition of EG&G's technical-services arm by URS Corporation. EG&G ceases as standalone entity. First step in the EG&G → Amentum lineage.",
  description_ru="Поглощение технико-сервисного направления EG&G компанией URS Corporation в 2002 г. EG&G перестаёт быть самостоятельной. Первый шаг в линии EG&G → Amentum.",
  source="corporate-economic-analysis/analysis/egng-amentum-succession.md")

E("ev-urs-aecom-acquisition-2014", "AECOM acquires URS (2014)", "event",
  date="2014",
  label_ru="AECOM поглощает URS (2014)",
  description="2014 acquisition of URS Corporation by AECOM. Federal-services line transitions to AECOM Management Services. Second step in the EG&G → Amentum lineage.",
  description_ru="Поглощение URS Corporation компанией AECOM в 2014 г. Линия федеральных сервисов переходит в AECOM Management Services. Второй шаг в линии EG&G → Amentum.",
  source="corporate-economic-analysis/analysis/egng-amentum-succession.md")

E("ev-aecom-amentum-spinoff-2020", "AECOM Management Services spun off as Amentum (2020)", "event",
  date="2020",
  label_ru="AECOM Management Services выделена в Amentum (2020)",
  description="2020 spinoff of AECOM's Management Services unit as standalone Amentum. Federal-services lineage carried forward intact. Third step in the EG&G → Amentum lineage.",
  description_ru="Выделение AECOM Management Services как самостоятельной Amentum в 2020 г. Линия федеральных сервисов наследуется без разрыва. Третий шаг в линии EG&G → Amentum.",
  source="corporate-economic-analysis/analysis/egng-amentum-succession.md")

E("ev-amentum-jacobs-cms-merger-2024", "Amentum + Jacobs CMS merger; NYSE: AMTM listing (2024)", "event",
  date="2024",
  label_ru="Слияние Amentum + Jacobs CMS; листинг NYSE: AMTM (2024)",
  description="2024 merger of Amentum with Jacobs Solutions' Critical Mission Solutions (CMS) division. Listed on NYSE under ticker AMTM in post-merger structure. Capstone of the EG&G → Amentum lineage.",
  description_ru="Слияние Amentum с подразделением Critical Mission Solutions (CMS) Jacobs Solutions в 2024 г. Листинг NYSE под тикером AMTM в посткорпоративной структуре. Capstone линии EG&G → Amentum.",
  source="corporate-economic-analysis/companies/amentum.md")

# ----- HYPOTHESES ------------------------------------------------------

E("hyp-egng-s4-contractor", "EG&G is the named-as-employer contractor at S-4", "hypothesis",
  label_ru="EG&G — подрядчик-работодатель, названный по S-4",
  description="Lazar's testimony corpus (KLAS-TV 1989 + Lazar Tape 1991 + JRE 1315 2019 + JRE 2479 2025) consistently identifies EG&G Special Projects (Las Vegas) as the contractor that hired him onto the S-4 programme. Single-source / Lazar-testimony only — no independent corroboration of the EG&G employment paperwork. The hypothesis is the testimonial bridge from Track 2 (Lazar) to Track 7 (Corporate). Confidence: low — single-source.",
  description_ru="Корпус свидетельств Лазара (KLAS-TV 1989 + Lazar Tape 1991 + JRE 1315 2019 + JRE 2479 2025) последовательно идентифицирует EG&G Special Projects (Лас-Вегас) как подрядчика, оформившего его на программу S-4. Только единственный источник / свидетельства Лазара — без независимой корроборации документов трудоустройства EG&G. Гипотеза — свидетельский мост от Трека 2 (Лазар) к Треку 7 (Корпоративный). Уверенность: низкая — один источник.",
  confidence="low",
  source="corporate-economic-analysis/analysis/lazar-s4-contractor-bridge.md")

E("hyp-amentum-egng-legacy", "Amentum is the corporate-genealogy successor of EG&G's federal-services line", "hypothesis",
  label_ru="Amentum — линейный преемник федерально-сервисной линии EG&G",
  description="The corporate-genealogy chain EG&G (1947) → URS (2002) → AECOM (2014) → Amentum (2020) → NYSE: AMTM (2024) is documented end-to-end in public M&A records. The hypothesis is genealogical, not testimonial — Amentum's lineage status is documented; whether any substantive UAP-programmatic continuity carries forward is NOT claimed and remains an open hypothesis space, not a closure. Confidence: high (for the lineage chain itself) / not-claimed (for substantive continuity).",
  description_ru="Цепочка корпоративной генеалогии EG&G (1947) → URS (2002) → AECOM (2014) → Amentum (2020) → NYSE: AMTM (2024) задокументирована end-to-end в публичных M&A-записях. Гипотеза — генеалогическая, не свидетельская: статус Amentum как линейного преемника задокументирован; перенос какой-либо субстантивной UAP-программной преемственности НЕ утверждается и остаётся открытым полем гипотез, не закрытием. Уверенность: высокая (для самой цепочки) / не-утверждается (для субстантивной преемственности).",
  confidence="high",
  source="corporate-economic-analysis/analysis/egng-amentum-succession.md")

# ----- SUB-CLUSTERS within Track 7 ------------------------------------

E("cluster-engineering-primes", "Engineering primes (LMT, BA, RTX, NOC)", "cluster",
  label_ru="Инженерные prime (LMT, BA, RTX, NOC)",
  description="Four US defense engineering prime contractors: Lockheed Martin (Skunk Works), Boeing (Phantom Works), RTX Corporation (sensor / radar / EW), Northrop Grumman (B-2 / B-21). Combined revenue FY24 ≈ $270B. Inner ring of the prime-contractor constellation.",
  description_ru="Четыре американских оборонных инженерных prime-подрядчика: Lockheed Martin (Skunk Works), Boeing (Phantom Works), RTX Corporation (сенсоры / РЛС / РЭБ), Northrop Grumman (B-2 / B-21). Совокупная выручка FY24 ≈ $270 млрд. Внутреннее кольцо созвездия prime-подрядчиков.",
  source="corporate-economic-analysis/analysis/industry-landscape.md")

E("cluster-services-inheritors", "Services-prime inheritors (Amentum, Leidos)", "cluster",
  label_ru="Сервисное кольцо — наследники (Amentum, Leidos)",
  description="Two US services-prime inheritors of EG&G / SAIC / LM IS&GS federal-services lineages: Amentum (EG&G → URS → AECOM → Amentum) and Leidos (SAIC-2013 spinoff + LM IS&GS-2016 absorption). Both members of multiple DoE national-laboratory operator consortia.",
  description_ru="Два американских сервисных prime-наследника линий федеральных сервисов EG&G / SAIC / LM IS&GS: Amentum (EG&G → URS → AECOM → Amentum) и Leidos (spinoff SAIC 2013 + поглощение LM IS&GS 2016). Оба — члены нескольких консорциумов операторов национальных лабораторий DOE.",
  source="corporate-economic-analysis/analysis/industry-landscape.md")

# ----- FACTS — public market data --------------------------------------

E("f-amentum-marketcap", "Amentum public market data (FY24)", "fact",
  label_ru="Публичные рыночные данные Amentum (FY24)",
  description="Amentum (NYSE: AMTM) — revenue ~$13B FY24; ~50,000 employees; market cap ~$5–6B (2025 snapshot); HQ Chantilly, Virginia.",
  description_ru="Amentum (NYSE: AMTM) — выручка ~$13 млрд FY24; ~50 000 сотрудников; рыночная капитализация ~$5–6 млрд (снимок 2025); штаб-квартира Чантильи, Вирджиния.",
  confidence="high",
  source="corporate-economic-analysis/companies/amentum.md")

E("f-lmt-marketcap", "Lockheed Martin public market data (FY24)", "fact",
  label_ru="Публичные рыночные данные Lockheed Martin (FY24)",
  description="Lockheed Martin (NYSE: LMT) — revenue ~$71B FY24; ~122,000 employees; HQ Bethesda, Maryland.",
  description_ru="Lockheed Martin (NYSE: LMT) — выручка ~$71 млрд FY24; ~122 000 сотрудников; штаб-квартира Бетесда, Мэриленд.",
  confidence="high",
  source="corporate-economic-analysis/companies/lockheed-martin.md")

E("f-boeing-marketcap", "Boeing public market data (FY24)", "fact",
  label_ru="Публичные рыночные данные Boeing (FY24)",
  description="Boeing (NYSE: BA) — revenue ~$78B FY24; ~170,000 employees; HQ Arlington, Virginia.",
  description_ru="Boeing (NYSE: BA) — выручка ~$78 млрд FY24; ~170 000 сотрудников; штаб-квартира Арлингтон, Вирджиния.",
  confidence="high",
  source="corporate-economic-analysis/companies/boeing.md")

E("f-rtx-marketcap", "RTX public market data (FY24)", "fact",
  label_ru="Публичные рыночные данные RTX (FY24)",
  description="RTX Corporation (NYSE: RTX) — revenue ~$80B FY24; ~185,000 employees; HQ Arlington, Virginia.",
  description_ru="RTX Corporation (NYSE: RTX) — выручка ~$80 млрд FY24; ~185 000 сотрудников; штаб-квартира Арлингтон, Вирджиния.",
  confidence="high",
  source="corporate-economic-analysis/companies/raytheon-rtx.md")

E("f-noc-marketcap", "Northrop Grumman public market data (FY24)", "fact",
  label_ru="Публичные рыночные данные Northrop Grumman (FY24)",
  description="Northrop Grumman (NYSE: NOC) — revenue ~$41B FY24; ~101,000 employees; HQ Falls Church, Virginia.",
  description_ru="Northrop Grumman (NYSE: NOC) — выручка ~$41 млрд FY24; ~101 000 сотрудников; штаб-квартира Фолс-Чёрч, Вирджиния.",
  confidence="high",
  source="corporate-economic-analysis/companies/northrop-grumman.md")

E("f-leidos-marketcap", "Leidos public market data (FY24)", "fact",
  label_ru="Публичные рыночные данные Leidos (FY24)",
  description="Leidos Holdings (NYSE: LDOS) — revenue ~$16B FY24; ~47,000 employees; HQ Reston, Virginia.",
  description_ru="Leidos Holdings (NYSE: LDOS) — выручка ~$16 млрд FY24; ~47 000 сотрудников; штаб-квартира Рестон, Вирджиния.",
  confidence="high",
  source="corporate-economic-analysis/companies/leidos.md")

# ----- SOURCES — public filings + working notes ------------------------

E("src-amentum-10k-fy24", "Amentum Holdings 10-K (FY24)", "source",
  label_ru="Amentum Holdings 10-K (FY24)",
  description="Amentum Holdings annual report on Form 10-K for fiscal year 2024. SEC EDGAR primary public filing. Provenance grade A.",
  description_ru="Годовой отчёт Amentum Holdings по форме 10-K за FY24. Первичная публичная отчётность SEC EDGAR. Уровень провенанса A.")

E("src-lmt-10k-fy24", "Lockheed Martin 10-K (FY24)", "source",
  label_ru="Lockheed Martin 10-K (FY24)",
  description="Lockheed Martin annual report on Form 10-K for fiscal year 2024. SEC EDGAR primary public filing. Provenance grade A.",
  description_ru="Годовой отчёт Lockheed Martin по форме 10-K за FY24. Первичная публичная отчётность SEC EDGAR. Уровень провенанса A.")

E("src-boeing-10k-fy24", "Boeing 10-K (FY24)", "source",
  label_ru="Boeing 10-K (FY24)",
  description="Boeing annual report on Form 10-K for fiscal year 2024. SEC EDGAR primary public filing. Provenance grade A.",
  description_ru="Годовой отчёт Boeing по форме 10-K за FY24. Первичная публичная отчётность SEC EDGAR. Уровень провенанса A.")

E("src-rtx-10k-fy24", "RTX Corporation 10-K (FY24)", "source",
  label_ru="RTX Corporation 10-K (FY24)",
  description="RTX Corporation annual report on Form 10-K for fiscal year 2024. SEC EDGAR primary public filing. Provenance grade A.",
  description_ru="Годовой отчёт RTX Corporation по форме 10-K за FY24. Первичная публичная отчётность SEC EDGAR. Уровень провенанса A.")

E("src-noc-10k-fy24", "Northrop Grumman 10-K (FY24)", "source",
  label_ru="Northrop Grumman 10-K (FY24)",
  description="Northrop Grumman annual report on Form 10-K for fiscal year 2024. SEC EDGAR primary public filing. Provenance grade A.",
  description_ru="Годовой отчёт Northrop Grumman по форме 10-K за FY24. Первичная публичная отчётность SEC EDGAR. Уровень провенанса A.")

E("src-leidos-10k-fy24", "Leidos Holdings 10-K (FY24)", "source",
  label_ru="Leidos Holdings 10-K (FY24)",
  description="Leidos Holdings annual report on Form 10-K for fiscal year 2024. SEC EDGAR primary public filing. Provenance grade A.",
  description_ru="Годовой отчёт Leidos Holdings по форме 10-K за FY24. Первичная публичная отчётность SEC EDGAR. Уровень провенанса A.")

E("src-banchenko-track7-2026-04-26", "Banchenko corporate-session brief (2026-04-26)", "source",
  label_ru="Бриф корпоративной сессии Банченко (26.04.2026)",
  description="Working analytical notes by Denis Banchenko on EG&G → Amentum corporate-genealogy thesis and Track 7 v1 inventory. Authored 2026-04-26. Preserved verbatim in raw/denis_2026-04-26_egng_amentum_brief.md.",
  description_ru="Рабочие аналитические заметки Дениса Банченко по тезису корпоративной генеалогии EG&G → Amentum и инвентарю v1 Трека 7. Составлены 26.04.2026. Сохранены дословно в raw/denis_2026-04-26_egng_amentum_brief.md.")

E("src-banchenko-track7-2026-04-27", "Banchenko companies-and-patents brief (2026-04-27)", "source",
  label_ru="Бриф компаний и патентов Банченко (27.04.2026)",
  description="Working analytical notes by Denis Banchenko on company-by-company adversarial cross-validation framing, patent-portfolio surfacing, and forward-link to bio-engineering carve-out. Authored 2026-04-27. Preserved verbatim in raw/denis_2026-04-27_companies_patents_brief.md.",
  description_ru="Рабочие аналитические заметки Дениса Банченко по рамке adversarial кросс-валидации по каждой компании, обзору патентных портфелей и forward-link к биоинженерному ответвлению. Составлены 27.04.2026. Сохранены дословно в raw/denis_2026-04-27_companies_patents_brief.md.")

# ════════════════════════════════════════════════════════════════════
# CONNECTIONS — Track 7 internal + cross-archive bridges
# ════════════════════════════════════════════════════════════════════

# Corporate genealogy chain (succession edges)
C("inst-egng", "ev-egng-urs-acquisition-2002", "acquired-by", direction="directed")
C("ev-egng-urs-acquisition-2002", "inst-urs", "acquired-into", direction="directed")
C("inst-urs", "ev-urs-aecom-acquisition-2014", "acquired-by", direction="directed")
C("ev-urs-aecom-acquisition-2014", "inst-aecom", "acquired-into", direction="directed")
C("inst-aecom", "ev-aecom-amentum-spinoff-2020", "spinoff-from", direction="directed")
C("ev-aecom-amentum-spinoff-2020", "inst-amentum", "spinoff-into", direction="directed")
C("inst-jacobs", "ev-amentum-jacobs-cms-merger-2024", "merger-into", direction="directed")
C("inst-amentum", "ev-amentum-jacobs-cms-merger-2024", "merger-into", direction="directed")
C("inst-egng", "inst-amentum", "legacy-of", direction="directed")

# Lazar S-4 contractor bridge (load-bearing)
C("p-lazar", "inst-egng", "claims employer-of-record", direction="directed")
C("inst-egng", "hyp-egng-s4-contractor", "central-claim-of", direction="directed")
C("hyp-egng-s4-contractor", "hyp-lazar-s4", "supports", direction="directed")
C("inst-amentum", "hyp-amentum-egng-legacy", "central-claim-of", direction="directed")
C("hyp-amentum-egng-legacy", "hyp-egng-s4-contractor", "extends-by-lineage", direction="directed")
C("f-lazar-credentials-disputed", "hyp-egng-s4-contractor", "challenges", direction="directed")

# CEO + CTO employer-of edges
C("p-amtm-ceo-scan-target", "inst-amentum", "scan-target-at", direction="directed")
C("p-amtm-cto-scan-target", "inst-amentum", "scan-target-at", direction="directed")

# Sub-cluster membership
C("inst-lmt", "cluster-engineering-primes", "member-of", direction="directed")
C("inst-boeing", "cluster-engineering-primes", "member-of", direction="directed")
C("inst-rtx", "cluster-engineering-primes", "member-of", direction="directed")
C("inst-noc", "cluster-engineering-primes", "member-of", direction="directed")
C("inst-amentum", "cluster-services-inheritors", "member-of", direction="directed")
C("inst-leidos", "cluster-services-inheritors", "member-of", direction="directed")

# Track 7 cluster membership (promote from placeholder)
C("inst-egng", "cluster-track7-corporate", "member-of", direction="directed")
C("inst-amentum", "cluster-track7-corporate", "member-of", direction="directed")
C("inst-leidos", "cluster-track7-corporate", "member-of", direction="directed")
C("inst-lmt", "cluster-track7-corporate", "member-of", direction="directed")
C("inst-rtx", "cluster-track7-corporate", "member-of", direction="directed")
C("inst-noc", "cluster-track7-corporate", "member-of", direction="directed")
C("inst-jacobs", "cluster-track7-corporate", "member-of", direction="directed")
C("inst-aecom", "cluster-track7-corporate", "member-of", direction="directed")
C("inst-urs", "cluster-track7-corporate", "member-of", direction="directed")
C("cluster-engineering-primes", "cluster-track7-corporate", "sub-cluster-of", direction="directed")
C("cluster-services-inheritors", "cluster-track7-corporate", "sub-cluster-of", direction="directed")

# Fact citations
C("f-amentum-marketcap", "inst-amentum", "describes", direction="directed")
C("f-lmt-marketcap", "inst-lmt", "describes", direction="directed")
C("f-boeing-marketcap", "inst-boeing", "describes", direction="directed")
C("f-rtx-marketcap", "inst-rtx", "describes", direction="directed")
C("f-noc-marketcap", "inst-noc", "describes", direction="directed")
C("f-leidos-marketcap", "inst-leidos", "describes", direction="directed")

# Source citations (10-K filings → fact nodes)
C("src-amentum-10k-fy24", "f-amentum-marketcap", "primary source for", direction="directed")
C("src-lmt-10k-fy24", "f-lmt-marketcap", "primary source for", direction="directed")
C("src-boeing-10k-fy24", "f-boeing-marketcap", "primary source for", direction="directed")
C("src-rtx-10k-fy24", "f-rtx-marketcap", "primary source for", direction="directed")
C("src-noc-10k-fy24", "f-noc-marketcap", "primary source for", direction="directed")
C("src-leidos-10k-fy24", "f-leidos-marketcap", "primary source for", direction="directed")
C("src-banchenko-track7-2026-04-26", "hyp-amentum-egng-legacy", "primary source for", direction="directed")
C("src-banchenko-track7-2026-04-27", "cluster-track7-corporate", "primary source for", direction="directed")

# DoE national-lab consortium membership (Track 4 / Track 6 bridges)
C("inst-amentum", "inst-llnl", "consortium-member-of", direction="directed",
  description="Member of LLNS LLC consortium operating LLNL")
C("inst-amentum", "inst-lanl", "consortium-member-of", direction="directed",
  description="Member of Triad LLC consortium operating LANL (post-2024 via Jacobs CMS)")
C("inst-leidos", "inst-doe", "consortium-member-of", direction="directed",
  description="Member of CNS LLC consortium operating Y-12 / Pantex")

# Cross-archive bridges
C("inst-amentum", "cluster-fbi-11", "consortium-member-employer-overlap", direction="directed",
  description="Triad LLC consortium membership creates indirect employer-overlap with LANL-affiliated cluster cases (Cassias, Chavez)")
C("inst-egng", "p-lazar", "named-as-employer-of", direction="directed")
C("meth-uap-application", "cluster-track7-corporate", "OSINT-validation-target", direction="directed")
