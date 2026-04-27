# ════════════════════════════════════════════════════════════════════
# OSINT-INTELLIGENCE-ANALYSIS — methodology layer (Track 5)
# Sources: osint-intelligence-analysis/README.md + analysis/*.md
# Authored by Denis Banchenko, 2026-04-26
# ════════════════════════════════════════════════════════════════════

E("meth-signature-methodology", "OSINT 4-class signature classification framework", "hypothesis",
  label_ru="4-классовая методология классификации сигнатур OSINT",
  description="Multi-component fingerprint methodology: time-domain shape + frequency content + cross-channel correlation + inter-channel delay structure. Four operational classes: Type 1 Stable Nonlinearity / Type 2 Transient / Type 3 Self-Organization / Type 4 Anomalous. Only Type 4 (reproducible + model-defying) is a new-physics candidate.",
  description_ru="Методология многокомпонентного отпечатка: форма во временной области + частотное содержимое + межканальная корреляция + структура задержек. Четыре операционных класса: Тип 1 Стабильная нелинейность / Тип 2 Переходный / Тип 3 Самоорганизация / Тип 4 Аномальный. Только Тип 4 (воспроизводимый + вне модели) — кандидат на новую физику.",
  source="osint-intelligence-analysis/analysis/signature-methodology.md")

E("meth-anomaly-classes", "OSINT 5-case anomaly classification (ns-plasma, laser, DBD, pulse-power, RF)", "hypothesis",
  label_ru="5-кейсовая классификация аномалий OSINT (нс-плазма, лазер, ДБР, pulse-power, RF)",
  description="Five experimentally documented cases used as reusable templates: (1) atmospheric-pressure nanosecond plasma — multi-pulse EM comb + channel desync; (2) laser-induced breakdown — filamentation + self-sustaining channel; (3) dielectric-barrier discharge — system memory + chaos-to-structure; (4) pulse-power into solids — conductivity jump + threshold delay; (5) RF/microwave-plasma — new frequency generation + shot-to-shot instability.",
  description_ru="Пять экспериментально задокументированных кейсов как повторно используемые шаблоны: (1) нс-плазма при атм. давлении; (2) лазерный пробой — филаментация; (3) ДБР — память системы; (4) pulse-power в твёрдых телах — скачок проводимости; (5) RF/СВЧ-плазма — генерация новых частот.",
  source="osint-intelligence-analysis/analysis/anomaly-classification.md")

E("meth-validation-pipeline", "OSINT 7-step validation pipeline (real → new physics)", "hypothesis",
  label_ru="7-ступенчатый конвейер валидации OSINT (реальное → новая физика)",
  description="7 ordered steps: (1) parameter isolation, (2) threshold search, (3) temporal structure, (4) multi-channel verification, (5) scaling, (6) modelling, (7) hypothesis crash-test. 5 acceptance criteria — all must hold: reproducible / has threshold / has signature / scales / does not fit existing model. 3 named error modes: one strange signal ≠ discovery; ignoring noise/artifacts; mixing several processes.",
  description_ru="7 упорядоченных шагов: (1) изоляция параметров, (2) поиск порога, (3) временна́я структура, (4) мультиканальная проверка, (5) масштабирование, (6) моделирование, (7) краш-тест гипотезы. 5 критериев приёмки — все должны выполняться одновременно. 3 типичные ошибки.",
  source="osint-intelligence-analysis/analysis/validation-pipeline.md")

E("meth-uap-application", "OSINT methodology application across UAP archive tracks", "hypothesis",
  label_ru="Применение методологии OSINT по трекам UAP-архива",
  description="Maps the methodology onto all 4 data-bearing sibling archives: Dubna/Element-115 = positive control (passed all 7 steps, Phys. Rev. C 2004); Lazar = fails 5 of 5 criteria except 'Z=115 exists' (standard physics); Chernobrov = fails Steps 1+2, partial Step 4; People-cluster = statistical signature not physical, validation incomplete; ECP artifact = compromised blinding = error mode 3.",
  description_ru="Накладывает методологию на все 4 смежных подархива с данными. Дубна/Элемент 115 — положительный контроль. Лазар — проваливает 5 из 5 критериев. Чернобров — частично шаг 4. Кластер людей — статистическая, не физическая сигнатура. ECP-артефакт — нарушенное ослепление = ошибка 3.",
  source="osint-intelligence-analysis/analysis/uap-application.md")

# Sources — OSINT methodology
E("src-osint-methodology-notes", "Banchenko OSINT methodology working notes (2026-04-26)", "source",
  label_ru="Рабочие заметки Банченко по OSINT-методологии (26.04.2026)",
  description="Working analytical notes by Denis Banchenko on signature methodology, anomaly classification, and validation pipeline. Single source for all four OSINT analysis files. Authored 2026-04-26. Preserved verbatim in raw/banchenko_2026-04-26_signature_methodology_notes.txt.",
  description_ru="Рабочие аналитические заметки Дениса Банченко по методологии сигнатур, классификации аномалий и конвейеру валидации. Единственный источник четырёх OSINT-аналитических файлов. Составлены 26.04.2026. Сохранены дословно в raw/banchenko_2026-04-26_signature_methodology_notes.txt.")

# ════════════════════════════════════════════════════════════════════
# PEOPLE-ANALYSIS — institutions
# ════════════════════════════════════════════════════════════════════

E("inst-afrl", "Air Force Research Laboratory (AFRL)", "institution",
  label_ru="Лаборатория авиационных исследований ВВС США (AFRL)",
  description="Principal in-house research and technology organisation of the US Air Force, Wright-Patterson Air Force Base. Covers aerospace, directed-energy, sensors, materials, and advanced concepts. Former head: William Neal McCasland (retired major-general).",
  description_ru="Основная внутренняя научно-технологическая организация ВВС США, авиабаза Райт-Паттерсон. Охватывает авиакосмическую, направленных энергий, сенсорную, материаловедческую тематики. Экс-руководитель: Уильям Нил Маккаслэнд.")

E("inst-nasa-jpl", "NASA Jet Propulsion Laboratory (JPL)", "institution",
  label_ru="Лаборатория реактивного движения NASA (JPL)",
  description="NASA's primary planetary-science and deep-space-mission laboratory, Pasadena, California. Managed by Caltech. Three cluster members affiliated: Hassen-Tores, Maiwald, Higgs.",
  description_ru="Основная лаборатория планетарных наук и дальнего космоса NASA, Пасадена, Калифорния. Управляется Caltech. Три участника кластера: Хасин-Тореза, Майвальд, Хиггс.")

E("inst-aerojet", "Aerojet Rocketdyne", "institution",
  label_ru="Aerojet Rocketdyne",
  description="US aerospace and defense propulsion manufacturer. Monica Hassen-Tores held dual affiliation with NASA JPL and Aerojet Rocketdyne, specialising in materials and alloys for rocket engines.",
  description_ru="Американский производитель авиакосмических и оборонных двигателей. Моника Хасин-Тореза имела двойную аффилиацию с NASA JPL и Aerojet Rocketdyne, специализируясь на материалах и сплавах для ракетных двигателей.")

E("inst-kcnsc", "Kansas City National Security Campus (KCNSC)", "institution",
  label_ru="Национальный кампус безопасности в Канзас-Сити (KCNSC)",
  description="US facility producing non-nuclear components of weapons systems, Kansas City, Missouri. Stephen Abel Garcia worked here as a contractor.",
  description_ru="Американский объект, производящий неядерные компоненты систем вооружений, Канзас-Сити, Миссури. Стивен Абел Гарсия работал здесь по контракту.")

E("inst-lanl", "Los Alamos National Laboratory (LANL)", "institution",
  label_ru="Лос-Аламосская национальная лаборатория (ЛАНЛ)",
  description="US Department of Energy national laboratory, Los Alamos, New Mexico. Portfolio: nuclear weapons, non-proliferation, fundamental science, high-performance computing. Two cluster members: Melisia Cassias (employee) and Anthony Chavez (retired former employee).",
  description_ru="Национальная лаборатория Министерства энергетики США, Лос-Аламос, Нью-Мексико. Ядерное оружие, нераспространение, фундаментальная наука. Двое в кластере: Мелисия Кассиас (сотрудник) и Энтони Чавес (отставной).")

E("inst-caltech", "California Institute of Technology (Caltech)", "institution",
  label_ru="Калифорнийский технологический институт (Caltech)",
  description="Private research university, Pasadena, California. Operates NASA JPL under cooperative agreement. Caltech astrophysicist Karl Grillmar is a cluster member.",
  description_ru="Частный исследовательский университет, Пасадена, Калифорния. Управляет NASA JPL по кооперационному соглашению. Астрофизик Caltech Карл Грилмар входит в кластер.")

E("inst-mit-psfc", "MIT Plasma Science and Fusion Center (MIT PSFC)", "institution",
  label_ru="Центр плазмы и термоядерного синтеза MIT (MIT PSFC)",
  description="MIT's principal in-house plasma physics and fusion centre, Massachusetts. One of the strongest plasma/fusion programmes in the United States. Head: Nuno Loureiro (killed December 2025).",
  description_ru="Основной внутренний плазменно-фьюжн-центр MIT, Массачусетс. Одна из сильнейших программ плазмы/синтеза в США. Руководитель: Нуно Лаурейро (убит, декабрь 2025 г.).")

E("inst-ies", "Institute for Exotic Sciences (IES, Alabama)", "institution",
  label_ru="Институт экзотических наук (IES, Алабама)",
  description="Research institute focused on exotic sciences, Alabama. Co-founded by Amy Eskridge. The cluster's only non-conventional-national-lab affiliation.",
  description_ru="Исследовательский институт в области экзотических наук, Алабама. Сооснователь — Эми Эскридж. Единственная нестандартная лаборатория в кластере.")

E("inst-novarti", "Novarti (Massachusetts)", "institution",
  label_ru="Novarti (Массачусетс)",
  description="Massachusetts-based company. Jason Thomas was an employee; body recovered from a lake in 2025 with no signs of violence per police.",
  description_ru="Компания в Массачусетсе. Джейсон Томас был её сотрудником; тело найдено в озере в 2025 г., полиция — признаков насилия нет.")

E("inst-fbi", "US Federal Bureau of Investigation (FBI)", "institution",
  label_ru="Федеральное бюро расследований США (ФБР)",
  description="US federal law enforcement agency. Under Director Kash Patel, announced consolidated investigation of 11-scientist cluster on 19 April 2026 on Fox News Sunday Morning Futures with Maria Bartiromo.",
  description_ru="Федеральное правоохранительное ведомство США. Под руководством директора Кэша Пателя объявило о консолидированном расследовании кластера из 11 учёных 19 апреля 2026 года на Fox News Sunday Morning Futures.")

E("inst-nga", "National Geospatial-Intelligence Agency (NGA)", "institution",
  label_ru="Национальное агентство геопространственной разведки США (NGA)",
  description="Principal US Intelligence Community member for GEOINT and multi-source analytical model integration. Robert Cardillo served as Director 2014–2019, prior to which he held senior posts at DIA.",
  description_ru="Ключевой член разведсообщества США по GEOINT и мультиисточниковой аналитике. Роберт Кардилло — директор 2014–2019, ранее старшие посты в DIA.")

# ════════════════════════════════════════════════════════════════════
# PEOPLE-ANALYSIS — cluster super-node
# ════════════════════════════════════════════════════════════════════

E("cluster-fbi-11", "FBI 11-scientist cluster (consolidated 2026-04-19)", "cluster",
  label_ru="Кластер ФБР: 11 учёных (консолидирован 19.04.2026)",
  description="11 US scientists at top national laboratories (AFRL, NASA JPL, Aerojet Rocketdyne, LANL, KCNSC, MIT PSFC, Caltech, IES, Novarti) who died or disappeared 2022–2026. Status breakdown: 5 disappeared (no body recovered), 2 killed (named suspects on file), 1 found dead no signs of violence, 2 died in earlier years minimal detail, 1 died unclear circumstances. FBI Director Kash Patel announced unified investigation 2026-04-19 on Fox News Sunday Morning Futures with Maria Bartiromo. Also analysed under Cardillo's Gabriella Rev A framework.",
  description_ru="11 американских учёных из ведущих нацлабораторий, погибли или исчезли 2022–2026. Статусы: 5 исчезли, 2 убиты (подозреваемые известны), 1 найден мёртвым без признаков насилия, 2 умерли ранее (детали минимальны), 1 умерла при неясных обстоятельствах. Директор ФБР Кэш Патель объявил единое расследование 19.04.2026 на Fox News Sunday Morning Futures с Марией Бартиромо.")

# ════════════════════════════════════════════════════════════════════
# PEOPLE-ANALYSIS — 11 individual scientists
# ════════════════════════════════════════════════════════════════════

E("p-mccasland", "William Neal McCasland", "person · external",
  label_ru="Уильям Нил Маккаслэнд",
  description="Retired US Air Force major-general, former head of AFRL (Wright-Patterson). Status: DISAPPEARED — February 2026, Albuquerque, New Mexico. No body recovered. Left at home: phone, eyeglasses, health-tracking device. Took: wallet and .38-caliber revolver. Air Force hoodie found nearby later. Case open.",
  description_ru="Отставной генерал-майор ВВС США, бывший руководитель AFRL (Райт-Паттерсон). Статус: ИСЧЕЗ — февраль 2026 г., Альбукерке, Нью-Мексико. Дома остались телефон, очки, монитор здоровья. С собой: кошелёк и револьвер 38-го калибра. Неподалёку найдена толстовка ВВС. Дело открыто.")

E("p-tores", "Monica Hassen-Tores", "person · external",
  label_ru="Моника Хасин-Тореза",
  description="Metallurgical engineer at NASA JPL and Aerojet Rocketdyne, specialising in materials and alloys for rocket engines. Status: DISAPPEARED — 2025, California. No body recovered. Disappeared during a hike in a California forest; companion was metres away, turned aside briefly, she was gone — silent disappearance. Subsequent search produced no results.",
  description_ru="Инженер-металлург NASA JPL и Aerojet Rocketdyne, специализация — материалы и сплавы для ракетных двигателей. Статус: ИСЧЕЗЛА — 2025 г., Калифорния. Исчезла в походе в калифорнийском лесу при бесшумном исчезновении. Поиски результата не дали.")

E("p-garcia", "Stephen Abel Garcia", "person · external",
  label_ru="Стивен Абел Гарсия",
  description="Contractor at Kansas City National Security Campus (non-nuclear weapons-system components facility). Status: DISAPPEARED — 2025. No body recovered. Car, keys, and phone left at home. No vehicle taken, no keys taken.",
  description_ru="Подрядчик на Kansas City National Security Campus (неядерные компоненты систем вооружений). Статус: ИСЧЕЗ — 2025 г. Машина, ключи и телефон остались дома.")

E("p-cassias", "Melisia Cassias", "person · external",
  label_ru="Мелисия Кассиас",
  description="Employee of Los Alamos National Laboratory. Status: DISAPPEARED — June 2025. No body recovered. Found at home after disappearance: car, handbag, keys, and BOTH phones — and both phones had been reset to factory settings prior to disappearance. FBI investigation explicitly flags digital device cleanup as a search pattern.",
  description_ru="Сотрудник Лос-Аламосской национальной лаборатории. Статус: ИСЧЕЗЛА — июнь 2025 г. Дома: машина, сумка, ключи, оба телефона — оба сброшены до заводских настроек. ФБР явно ищет признак цифровой очистки устройств.")

E("p-chavez", "Anthony Chavez", "person · external",
  label_ru="Энтони Чавес",
  description="Former employee of Los Alamos National Laboratory (retired at time of disappearance). Status: DISAPPEARED — May 2025. No body recovered. House and car left locked; no signs of struggle. Disappeared one month before LANL colleague Melisia Cassias.",
  description_ru="Бывший сотрудник Лос-Аламосской национальной лаборатории (пенсионер). Статус: ИСЧЕЗ — май 2025 г. Дом и машина закрыты, признаков борьбы нет. Исчез за месяц до коллеги Кассиас из того же ЛАНЛ.")

E("p-grillmar", "Karl Grillmar", "person · external",
  label_ru="Карл Грилмар",
  description="Astrophysicist at California Institute of Technology (Caltech). Status: KILLED — February 2026. Shot at his home. Named suspect on file. Suspect visited the home twice — conflict on first visit, suspect shot Grillmar on second visit. Motive not established in public record.",
  description_ru="Астрофизик Калифорнийского технологического института (Caltech). Статус: УБИТ — февраль 2026 г. Застрелен у своего дома. По делу назван подозреваемый, приезжавший дважды. Мотив в публичной записи не установлен.")

E("p-loureiro", "Nuno Loureiro", "person · external",
  label_ru="Нуно Лаурейро",
  description="Professor at MIT and head of the MIT Plasma Science and Fusion Center — one of the strongest plasma/fusion programmes in the US. Status: KILLED — December 2025. Investigation identified a named suspect; motive described as unclear in the public source.",
  description_ru="Профессор MIT, руководитель Центра плазмы и термоядерного синтеза MIT — одна из сильнейших программ плазмы/синтеза в США. Статус: УБИТ — декабрь 2025 г. Следствие вышло на подозреваемого; мотив не установлен.")

E("p-thomas", "Jason Thomas", "person · external",
  label_ru="Джейсон Томас",
  description="Employee of Novarti (Massachusetts). Status: FOUND DEAD — 2025, Massachusetts. Disappeared, body subsequently recovered from a lake. Police reported no signs of violence. Family cited difficult emotional state following death of parents.",
  description_ru="Сотрудник Novarti (Массачусетс). Статус: НАЙДЕН МЁРТВЫМ — 2025 г. Исчез, тело найдено в озере. Полиция — признаков насилия нет. Семья ссылалась на тяжёлое эмоциональное состояние.")

E("p-maiwald", "Frank Maiwald", "person · external",
  label_ru="Франк Майвальд",
  description="Specialist at NASA Jet Propulsion Laboratory (JPL). Status: DIED — earlier years (year unspecified in public source). Listed in source paired with Michael Higgs as two JPL deaths in earlier years; characterised as a serious specialist whose death was notable. Cause not specified.",
  description_ru="Специалист NASA JPL. Статус: УМЕР — предыдущие годы (год в источнике не указан). В источнике сгруппирован с Майклом Хиггсом как двое умерших в JPL в предыдущие годы. Причина не указана.")

E("p-higgs", "Michael Higgs", "person · external",
  label_ru="Майкл Хиггс",
  description="Specialist at NASA Jet Propulsion Laboratory (JPL). Status: DIED — earlier years (year unspecified in public source). Listed in source paired with Frank Maiwald as two JPL deaths in earlier years; characterised as a serious specialist whose death was notable. Cause not specified.",
  description_ru="Специалист NASA JPL. Статус: УМЕР — предыдущие годы (год в источнике не указан). В источнике сгруппирован с Франком Майвальдом. Причина не указана.")

E("p-eskridge", "Amy Eskridge", "person · external",
  label_ru="Эми Эскридж",
  description="Co-founder of the Institute for Exotic Sciences (Alabama). Status: DIED UNCLEAR CIRCUMSTANCES — 2022. Earliest case in the cluster by date. Added to consolidated cluster only at FBI consolidation in 2026 — not at time of death, four years later.",
  description_ru="Сооснователь Института экзотических наук (Алабама). Статус: УМЕРЛА ПРИ НЕЯСНЫХ ОБСТОЯТЕЛЬСТВАХ — 2022 г. Самый ранний кейс кластера. Включена в общий кластер только при консолидации ФБР в 2026 г. — спустя четыре года после смерти.")

# ════════════════════════════════════════════════════════════════════
# PEOPLE-ANALYSIS — events (deaths / disappearances / key dates)
# ════════════════════════════════════════════════════════════════════

E("ev-eskridge-death", "Amy Eskridge dies under unclear circumstances", "event",
  date="2022",
  description="Co-founder of Institute for Exotic Sciences (Alabama) dies in 2022 under circumstances described as not clearly understood. Earliest case in the FBI cluster. Included in consolidated set only in 2026.",
  description_ru="Сооснователь Института экзотических наук (Алабама) умирает в 2022 г. при неясных обстоятельствах. Самый ранний кейс кластера. Включена в консолидированный кластер только в 2026 г.")

E("ev-chavez-disappear", "Anthony Chavez disappears from Albuquerque area", "event",
  date="2025-05",
  description="Former LANL employee (retired) disappears in May 2025. House and car left locked; no signs of struggle. No body recovered.",
  description_ru="Бывший сотрудник ЛАНЛ (пенсионер) исчезает в мае 2025 г. Дом и машина закрыты, признаков борьбы нет.")

E("ev-cassias-disappear", "Melisia Cassias disappears from Los Alamos area", "event",
  date="2025-06",
  description="LANL employee disappears in June 2025. Both phones found at home reset to factory settings. No body recovered. One month after fellow LANL figure Anthony Chavez.",
  description_ru="Сотрудник ЛАНЛ исчезает в июне 2025 г. Оба телефона найдены дома сброшенными до заводских настроек. Через месяц после Чавеса из того же ЛАНЛ.")

E("ev-tores-disappear", "Monica Hassen-Tores disappears on California forest hike", "event",
  date="2025",
  description="NASA JPL / Aerojet Rocketdyne metallurgical engineer disappears in 2025 during a hike in a California forest. Companion metres away; turned aside briefly, she was gone — silent disappearance. No body recovered.",
  description_ru="Инженер-металлург NASA JPL / Aerojet Rocketdyne исчезает в 2025 г. во время похода в калифорнийском лесу. Спутник в нескольких метрах — бесшумное исчезновение. Тело не найдено.")

E("ev-garcia-disappear", "Stephen Abel Garcia disappears from Kansas City area", "event",
  date="2025",
  description="KCNSC contractor disappears in 2025. Car, keys, and phone left at home. No body recovered.",
  description_ru="Подрядчик KCNSC исчезает в 2025 г. Машина, ключи, телефон остались дома. Тело не найдено.")

E("ev-thomas-found-dead", "Jason Thomas found dead in Massachusetts lake", "event",
  date="2025",
  description="Novarti (Massachusetts) employee disappears then body found in a lake in 2025. Police report no signs of violence. Family cited difficult emotional state.",
  description_ru="Сотрудник Novarti (Массачусетс) исчезает, тело находят в озере в 2025 г. Полиция — признаков насилия нет.")

E("ev-loureiro-killed", "Nuno Loureiro killed at MIT", "event",
  date="2025-12",
  description="MIT Professor and head of MIT Plasma Science and Fusion Center killed in December 2025. Named suspect identified by investigators; motive not established in public record.",
  description_ru="Профессор MIT и руководитель Центра плазмы и термоядерного синтеза MIT убит в декабре 2025 г. Следствие вышло на подозреваемого; мотив не установлен.")

E("ev-mccasland-disappear", "William Neal McCasland disappears in Albuquerque NM", "event",
  date="2026-02",
  description="Retired USAF major-general and former AFRL head disappears February 2026 in Albuquerque, New Mexico. Phone, eyeglasses, health-tracking device left at home; took wallet and .38-caliber revolver. Air Force hoodie found nearby. No body recovered.",
  description_ru="Отставной генерал-майор ВВС США и экс-руководитель AFRL исчезает в феврале 2026 г. в Альбукерке, Нью-Мексико. Телефон, очки, монитор здоровья дома; взял кошелёк и револьвер. Толстовка ВВС найдена неподалёку.")

E("ev-grillmar-killed", "Karl Grillmar shot at his home in California", "event",
  date="2026-02",
  description="Caltech astrophysicist Karl Grillmar shot at his residence in February 2026. Named suspect visited the home twice — conflict on first visit, shooting on second visit. Motive not established in public record. Same month as McCasland disappearance.",
  description_ru="Астрофизик Caltech Карл Грилмар застрелен у дома в феврале 2026 г. Подозреваемый приезжал дважды — конфликт в первый раз, убийство во второй. Мотив не установлен. Тот же месяц, что и исчезновение Маккаслэнда.")

E("ev-fbi-consolidate", "FBI consolidates investigation of 11-scientist cluster", "event",
  date="2026-04-19",
  description="FBI Director Kash Patel announces on Fox News Sunday Morning Futures with Maria Bartiromo that the Bureau is consolidating all eleven scientist deaths/disappearances into a single coordinated investigation. Scope: common classified-info access, common projects/facilities, time-geography overlaps, possible foreign-state involvement, modus-operandi patterns, digital device cleanup. Patel stated arrests would follow if collusion established.",
  description_ru="Директор ФБР Кэш Патель объявляет на Fox News Sunday Morning Futures с Марией Бартиромо об объединении всех 11 дел в единое скоординированное расследование. Ищутся: общий доступ к секретным данным, общие проекты, временные/географические совпадения, иностранное вмешательство, почерк M.O., цифровая очистка устройств.")

E("ev-cardillo-linkedin-post", "Robert Cardillo publishes Gabriella Rev A framework on LinkedIn", "event",
  date="2026-04",
  description="Robert Cardillo (former NGA Director 2014-2019) publicly applies his 'Gabriella Rev A' analytical framework to the same eleven cases on LinkedIn. Framework: multifactor analytics + cluster analysis + anomaly detection + scenario modelling. Explicit non-conspiratorial posture: building a hypothesis space, not declaring a conclusion.",
  description_ru="Роберт Кардилло (экс-директор NGA 2014–2019) публично применяет аналитическую рамку «Gabriella Rev A» к тем же 11 кейсам в LinkedIn. Четыре столпа: мультифакторная аналитика, кластерный анализ, поиск аномалий, сценарное моделирование. Явно неконспирологическая позиция.")

E("ev-db-linkedin-comment", "Denis Banchenko posts UAP study link under Cardillo LinkedIn thread", "event",
  date="2026-04-26",
  description="Denis Banchenko (ASRP project owner) posts a comment under Cardillo's LinkedIn thread linking to the UAP Reverse-Engineering Study and the Hyperbolic Field/Plasma Study. Cardillo did not respond directly but did not remove the comment. Analysed as a 'point of entry' — material seen and not filtered as noise by an analyst at IC level.",
  description_ru="Денис Банченко (владелец проекта ASRP) размещает комментарий под постом Кардилло в LinkedIn со ссылкой на UAP Reverse-Engineering Study. Кардилло не ответил, но и не удалил комментарий. Аналитически: точка входа.")

E("ev-osint-methodology-captured", "Denis Banchenko documents OSINT signature methodology", "event",
  date="2026-04-26",
  description="Denis Banchenko (project owner) authors working analytical notes on signature methodology, anomaly classification, and validation pipeline. Preserved at raw/banchenko_2026-04-26_signature_methodology_notes.txt. Basis of all four OSINT analysis files.",
  description_ru="Денис Банченко (владелец проекта) составляет рабочие аналитические заметки по методологии сигнатур, классификации аномалий и конвейеру валидации. Сохранено в raw/banchenko_2026-04-26_signature_methodology_notes.txt. Основа четырёх OSINT-файлов анализа.")

# ════════════════════════════════════════════════════════════════════
# PEOPLE-ANALYSIS — facts about the cluster
# ════════════════════════════════════════════════════════════════════

E("f-cluster-status-breakdown", "Cluster status breakdown: 5 disappeared / 2 killed / 1 found dead / 2 died earlier / 1 died unclear", "fact",
  source="people-analysis/analysis/cluster-summary.md",
  confidence="high",
  description="Public-record status tabulation: 5 disappeared without body (McCasland, Hassen-Tores, Garcia, Cassias, Chavez); 2 killed with named suspects (Grillmar, Loureiro); 1 found dead no signs of violence (Thomas); 2 died earlier years minimal detail (Maiwald, Higgs); 1 died unclear circumstances (Eskridge).",
  description_ru="Статусная разбивка: 5 исчезли без тела; 2 убиты с названным подозреваемым; 1 найден мёртвым без признаков насилия; 2 умерли в предыдущие годы (детали минимальны); 1 умерла при неясных обстоятельствах.")

E("f-cluster-geo-ca-nm", "California (4 cases) and New Mexico (3 cases) account for 7 of 11", "fact",
  source="people-analysis/analysis/cluster-summary.md",
  confidence="high",
  description="Geographic pattern: California carries 4 cases (Hassen-Tores, Grillmar, Maiwald, Higgs — consistent with JPL/Caltech concentration); New Mexico carries 3 (McCasland/Albuquerque, Cassias/Los Alamos, Chavez/Los Alamos); Massachusetts 2 (Loureiro/MIT, Thomas/Novarti); Missouri 1 (Garcia/KCNSC); Alabama 1 (Eskridge/IES).",
  description_ru="Географический паттерн: Калифорния — 4 кейса; Нью-Мексико — 3; Массачусетс — 2; Миссури — 1; Алабама — 1.")

E("f-cluster-time-concentration", "8 of 11 dated cases concentrated in 2025–2026", "fact",
  source="people-analysis/analysis/cluster-summary.md",
  confidence="high",
  description="Time pattern: 2022 = 1 (Eskridge); 2023 = 0; 2024 = 0; 2025 = 6 (Hassen-Tores, Garcia, Cassias Jun, Chavez May, Loureiro Dec, Thomas); 2026 = 2 (McCasland Feb, Grillmar Feb). May–June 2025 sub-window: two LANL disappearances one month apart. February 2026: one disappearance and one killing in same month.",
  description_ru="Временной паттерн: 2022 — 1; 2023 — 0; 2024 — 0; 2025 — 6; 2026 — 2. Подокно май–июнь 2025: два исчезновения из ЛАНЛ с разницей в месяц. Февраль 2026: одно исчезновение и одно убийство в одном месяце.")

E("f-cassias-phone-reset", "Melisia Cassias: both phones factory-reset before disappearance", "fact",
  source="people-analysis/people/melisia_cassias.md",
  confidence="medium",
  description="After Cassias's June 2025 disappearance, both of her phones were found at home and both had been reset to factory settings. FBI investigation cross-tabulates this with its 'digital cleanup of devices' search pattern. Source: secondary recap (Gera Sheriff YouTube). No primary law-enforcement record cross-check performed.",
  description_ru="После исчезновения Кассиас в июне 2025 оба её телефона найдены дома сброшенными до заводских настроек. ФБР ищет «цифровую очистку устройств» как паттерн. Источник: вторичная сводка.")

E("f-mccasland-uap-hint", "McCasland transcript hint: one general worked with UAP/UFO problem (unverified)", "fact",
  source="people-analysis/people/william_neal_mccasland.md",
  confidence="low",
  description="The YouTube transcript host suggests that one of the eleven ('the very first general') had worked with the UFO/UAP problem. This attribution is NOT corroborated against a primary source in the present archive. Recorded here as a low-confidence flag, not as an established fact.",
  description_ru="Ведущий YouTube предполагает, что один из одиннадцати («самый первый генерал») занимался проблематикой НАЯ/UAP. Это НЕ сверено с первичным источником в данном архиве. Зафиксировано как низкодостоверный флаг.")

E("f-fbi-search-patterns", "FBI investigation 8 cross-case search patterns per Patel 2026-04-19", "fact",
  source="people-analysis/analysis/fbi-cluster-investigation.md",
  confidence="high",
  description="Per Kash Patel (Fox News, 2026-04-19): FBI is searching for — (1) common classified-info access; (2) common projects/programmes/facilities; (3) time-geography overlaps; (4) possible foreign-state involvement; (5) signs of coordination/conspiracy; (6) repeating modus operandi esp. disappearances; (7) digital device cleanup (cf. Cassias both phones reset); (8) behavioural overlaps and pre-disappearance contacts.",
  description_ru="По заявлению Кэша Пателя (Fox News, 19.04.2026): ФБР ищет 8 межкейсовых паттернов: общий доступ к секретам, общие программы/объекты, временно-географические совпадения, иностранное вмешательство, признаки координации, повторяющийся почерк, цифровая очистка устройств, поведенческие совпадения до исчезновения.")

E("f-cluster-specialisation-homogeneity", "All 11 cases cluster in nuclear / propulsion / plasma / astrophysics / exotic-sciences fields", "fact",
  source="people-analysis/analysis/cluster-summary.md",
  confidence="high",
  description="Specialisation pattern: nuclear/weapon programmes (Cassias, Chavez, Garcia, McCasland); propulsion/rocket-engine alloys (Hassen-Tores, Maiwald, Higgs); plasma/fusion (Loureiro); astrophysics (Grillmar); exotic sciences (Eskridge); adjacent/undetailed (Thomas). No pure-mathematics or unrelated life-sciences personnel in the set.",
  description_ru="Специализационный паттерн: ядерные/оружейные программы; двигатели/сплавы; плазма/синтез; астрофизика; экзотические науки. Ни одного представителя чистой математики или несмежных наук в наборе.")

E("f-lanl-two-in-one-month", "Two LANL-affiliated persons disappeared May–June 2025 one month apart", "fact",
  source="people-analysis/analysis/cluster-summary.md",
  confidence="high",
  description="Anthony Chavez (retired LANL, May 2025) and Melisia Cassias (active LANL employee, June 2025) disappeared from the Los Alamos area within one month of each other. Both cases open. Time-and-institution overlap is one of the FBI's explicit search criteria.",
  description_ru="Энтони Чавес (отставной ЛАНЛ, май 2025) и Мелисия Кассиас (действующий сотрудник ЛАНЛ, июнь 2025) исчезли из района Лос-Аламоса с разницей в месяц. Оба дела открыты.")

E("f-jpl-three-cases", "NASA JPL has 3 cluster members — largest single-institution count", "fact",
  source="people-analysis/analysis/cluster-summary.md",
  confidence="high",
  description="JPL carries the highest per-institution count in the cluster: Hassen-Tores (also Aerojet Rocketdyne), Maiwald, and Higgs. Los Alamos is second with 2. All other institutions have 1 each.",
  description_ru="JPL имеет наибольшее число участников кластера на одно учреждение: Хасин-Тореза, Майвальд, Хиггс. Лос-Аламос на втором месте с 2. Все остальные учреждения по 1.")

E("f-cardillo-no-attribution", "Cardillo's Gabriella Rev A framework is explicitly non-conspiratorial and non-attributional", "fact",
  source="people-analysis/analysis/cardillo-gabriella-framework.md",
  confidence="high",
  description="Robert Cardillo (former NGA Director) explicitly does NOT claim conspiracy, does NOT attribute the cluster to extraterrestrial activity, foreign-state action, or any single causal agent. His framework builds a hypothesis space for an analytically-defensible cluster — standard IC tradecraft.",
  description_ru="Роберт Кардилло (экс-директор NGA) явно НЕ утверждает заговор, НЕ атрибутирует кластер ни к внеземной активности, ни к действиям иностранных государств. Рамка строит поле гипотез — стандартная практика разведсообщества.")

E("f-coordinated-action-not-concluded", "Coordinated foul play not concluded — open dataset status per FBI framing", "fact",
  source="people-analysis/analysis/fbi-cluster-investigation.md",
  confidence="high",
  description="DISCLAIMER (high-confidence anti-conclusion): as of 2026-04-19 the FBI has NOT concluded that coordinated action or foul play connects the eleven cases. Patel explicitly stated the investigation is looking for cross-links, not that cross-links have been found. Opposite outcome — finding no cross-links — is equally an analytical result. This is tagged high-confidence because Patel's exact framing is documented (broadcast); the cautious wording is the verifiable claim itself.",
  description_ru="ОТКАЗ ОТ ИНТЕРПРЕТАЦИИ (высокая уверенность в анти-выводе): по состоянию на 19.04.2026 ФБР НЕ пришло к выводу о координированных действиях. Патель явно заявил, что расследование ИЩЕТ межкейсовые связи, а не что они найдены. Помечено high-confidence, поскольку формулировка Пателя задокументирована (трансляция); сама осторожная формулировка и есть проверяемое утверждение.")

# ════════════════════════════════════════════════════════════════════
# PEOPLE-ANALYSIS — hypotheses and analytical frameworks
# ════════════════════════════════════════════════════════════════════

E("hyp-cardillo-gabriella", "Cardillo 'Gabriella Rev A' analytical framework", "hypothesis",
  label_ru="Аналитическая рамка «Gabriella Rev A» Кардилло",
  description="Robert Cardillo (former NGA Director 2014-2019, ex-DIA senior posts) applied framework to the 11-scientist cluster. Four pillars: multifactor analytics, cluster analysis, anomaly detection, scenario modelling. Output: hypothesis space, not single-cause attribution. Applied to same institutional set as FBI investigation: LANL (≥2), NASA JPL (≥3), MIT PSFC (1), AFRL (1), Caltech (1), KCNSC (1), IES Alabama (1). Also references FBI consolidation and DoE ex-staff overlap.",
  description_ru="Аналитическая рамка Роберта Кардилло (экс-директор NGA 2014–2019, ранее старшие посты в DIA) применена к кластеру 11 учёных. Четыре столпа: мультифакторная аналитика, кластерный анализ, выявление аномалий, сценарное моделирование. Выход: поле гипотез, а не единичная атрибуция.",
  source="people-analysis/analysis/cardillo-gabriella-framework.md")

E("hyp-cluster-statistical-signature", "People cluster as statistical signature — validation incomplete per OSINT methodology", "hypothesis",
  label_ru="Кластер людей как статистическая сигнатура — валидация не завершена (методология OSINT)",
  description="Per osint-intelligence-analysis/analysis/uap-application.md: the 11-scientist cluster is a statistical rather than physical signature, but the same 5-criteria validation lens applies. Criteria: threshold (does death rate exceed base rate?), scaling (does pattern hold cross-country/decade?), signature (common modus across 6+ of 11?), reproducibility (does pattern reappear in independent investigations?), model failure (exceeds occupational-hazard + selection-bias explanations?). All 5 must hold to upgrade from 'suggestive' to 'structural'. Currently: validation incomplete.",
  description_ru="Согласно osint-intelligence-analysis/analysis/uap-application.md: кластер — статистическая, не физическая сигнатура, но та же линза из 5 критериев применима. Для повышения из 'наводящего' в 'структурный' все 5 должны выполняться. Статус: валидация не завершена.",
  source="osint-intelligence-analysis/analysis/uap-application.md")

E("hyp-uap-tax-3", "Banchenko 3-category UAP origin taxonomy", "hypothesis",
  label_ru="Трёхкатегорная таксономия происхождения UAP (Банченко)",
  description="Denis Banchenko (working session, 2026-04-06) proposed 3 origin categories as a classification vocabulary (not an empirical claim): (1) Interstellar — from another star system; canonical archive: Lazar S-4. (2) Parallel-reality / interdimensional — from a parallel branch of reality; canonical archive: Chernobrov anomalous zones. (3) Temporal — time-travellers or objects displaced in time; canonical frame: Chernobrov time-machine + ECP artifact working hypothesis 'мы следуем во времени объекта'. People-cluster is explicitly NOT one of these categories — it is an adjacent class: human-impact field around the reverse-engineering programme.",
  description_ru="Денис Банченко (рабочая сессия, 06.04.2026): 3 категории как классификационный словарь (не эмпирическое утверждение): (1) Межзвёздные; (2) Параллельная реальность / межмерные; (3) Темпоральные. Кластер людей — НЕ одна из этих категорий, а смежный класс человеческого импакта.",
  source="analysis/uap-taxonomy.md")

E("hyp-ecp-temporal-placement", "ECP artifact UAP-FRAG-001 tentatively placed in temporal category", "hypothesis",
  label_ru="ECP-артефакт UAP-FRAG-001 предварительно помещён в темпоральную категорию",
  description="Working hypothesis only (not confirmed categorisation): artifact under study in root experiments/ placed in Banchenko taxonomy category 3.3 (temporal) based on Denis's framing 'мы следуем во времени объекта'. Reference data from session ECP-2026-04-04: object is a navigation beacon for temporal UAP navigation, part of triangulation system, biometal, variable radioactivity, Mountains of Kazakhstan (Tian Shan / Taraz area). ECP session showed compromised blinding (error mode 3 per OSINT methodology).",
  description_ru="Только рабочая гипотеза: артефакт помещён в категорию 3.3 (темпоральная) по формулировке Дениса «мы следуем во времени объекта». Референсные данные ECP-2026-04-04: навигационный маяк для темпоральных UAP, часть триангуляционной системы, биометалл, Казахстан (Тянь-Шань/Тараз). Сеанс ECP — нарушенное ослепление (ошибка 3).",
  source="analysis/ecp_validation_report.md")

# ════════════════════════════════════════════════════════════════════
# PEOPLE-ANALYSIS — sources
# ════════════════════════════════════════════════════════════════════

E("src-gera-sheriff-youtube", "YouTube — Gera Sheriff 'Убиты или пропали 11 специалистов' (2026-04-22)", "source",
  label_ru="YouTube — Гера Шериф «Убиты или пропали 11 специалистов» (22.04.2026)",
  description="Primary per-person data source for the 11-scientist cluster. Gera Sheriff (self-identified retired US sheriff, Broward County FL, now RU-language YouTube commentator). Video 16:27, published 2026-04-22. Provenance grade: secondary recap of public reporting and Patel/Bartiromo Fox News statement. Transcript at raw/youtube_q9VV_11_scientists_FBI_2026-04-22.txt.",
  description_ru="Первичный источник подробностей по 11 учёным. Гера Шериф (отставной шериф США, округ Бравард, Флорида, ныне RU-канал YouTube). Видео 16:27, опубликовано 22.04.2026. Провенанс: вторичная сводка публичных сообщений и заявления Пателя/Бартиромо.")

E("src-fox-patel-2026", "Fox News Sunday Morning Futures — Kash Patel FBI statement (2026-04-19)", "source",
  label_ru="Fox News Sunday Morning Futures — заявление Кэша Пателя ФБР (19.04.2026)",
  description="Primary broadcast source for FBI consolidation announcement. FBI Director Kash Patel on Fox News Sunday Morning Futures with Maria Bartiromo, 19 April 2026. Cited via YouTube transcript recap. Provenance grade: secondary recap adequate for cluster-level documentation.",
  description_ru="Первичный телевизионный источник объявления о консолидации ФБР. Директор ФБР Кэш Патель на Fox News Sunday Morning Futures с Марией Бартиромо, 19 апреля 2026 г.")

E("src-cardillo-linkedin", "Robert Cardillo LinkedIn post — Gabriella Rev A framework (April 2026)", "source",
  label_ru="Пост Роберта Кардилло в LinkedIn — рамка «Gabriella Rev A» (апрель 2026)",
  description="Public LinkedIn post by Robert Cardillo (former NGA Director) introducing and applying the Gabriella Rev A analytical framework to the 11-scientist cluster. Primary OSINT artefact. Strategic-context analysis preserved in raw/banchenko_2026-04-26_cardillo_gabriella_framework_notes.txt (Banchenko working notes, 2026-04-26).",
  description_ru="Публичный пост Роберта Кардилло (экс-директор NGA) в LinkedIn с представлением рамки «Gabriella Rev A» применительно к кластеру 11 учёных. Первичный OSINT-артефакт.")

E("src-jre-2416-farah", "Joe Rogan Experience #2416 — Dan Farah (Russian dub, 2025)", "source",
  label_ru="Joe Rogan Experience #2416 — Дэн Фара (русский дубляж, 2025)",
  description="Dan Farah (producer, The Age of Disclosure 2025) on JRE #2416. Russian dub provided by Denis Banchenko, 2026-04-01. Key claims: Lazar propulsion description in 2025 independently matches 1989 Lazar account per Farah's sources; 'dozens of crashed craft of non-human origin' since 1940s per Senate IC contacts. Transcript at bob-lazar-archive/transcripts/external/jre_2416_dan_farah_RU.txt.",
  description_ru="Дэн Фара (продюсер «Эпохи раскрытия» 2025) на JRE #2416. Русский дубляж предоставлен Денисом Банченко, 01.04.2026. Ключевые утверждения: описание двигателя Лазара совпадает с источниками Фары 2025; «десятки разбившихся аппаратов нечеловеческого происхождения» с 1940-х.")

# ════════════════════════════════════════════════════════════════════
# CROSS-ARCHIVE / TAXONOMY / EXTERNAL — analysis/ root
# ════════════════════════════════════════════════════════════════════

E("hyp-cross-archive-element115-thread", "Cross-archive Element 115 convergence: Lazar (1989) → Dubna/JINR+LLNL (2003) → SHEF (2020)", "hypothesis",
  label_ru="Межархивная конвергенция по Элементу 115: Лазар (1989) → Дубна/ОИЯИ+LLNL (2003) → ФСЭ (2020)",
  description="Cross-archive synthesis theme 1: Lazar's 1989 claim that element 115 existed as a stable isotope was followed by JINR+LLNL joint synthesis (²⁴³Am+⁴⁸Ca, U-400 cyclotron, Phys. Rev. C 69 021601R, 2004), IUPAC naming as Moscovium 2016, and SHEF production of ~70 atoms in 40 days (2020). Lazar's 'stable isotope' property is contradicted by Dubna's sub-second lifetimes. Chernobrov archive does not discuss element 115 directly.",
  description_ru="Тема 1 кросс-архивного синтеза: заявление Лазара 1989 г. о стабильном изотопе элемента 115 → синтез ОИЯИ+LLNL 2003 → именование московием ИЮПАК 2016 → ФСЭ ~70 атомов 2020. «Стабильность» Лазара противоречит субсекундным временам жизни в Дубне.",
  source="analysis/cross-archive-synthesis.md")

E("hyp-cross-archive-spacetime-thread", "Cross-archive space-time distortion convergence: Lazar Gravity-A/B ↔ Chernobrov Lovondatr", "hypothesis",
  label_ru="Межархивная конвергенция по искажению пространства-времени: Gravity-A/B Лазара ↔ Ловондатр Черноброва",
  description="Cross-archive synthesis theme 2: Lazar's gravity-wave propulsion (Gravity-A + Gravity-B, element 115 as source, space-time deformation rather than traversal) and Chernobrov's Lovondatr programme (7 generations 1988-~2005, micro-temporal effects via EM toroidal/cylindrical chambers, sub-second time-rate deviations measured against external references). Conceptual overlap on gravitational distortion of space-time; programs are independent and each contested on its own terms.",
  description_ru="Тема 2: гравитационно-волновой движитель Лазара (Gravity-A/B, элемент 115, деформация пространства-времени) и программа «Ловондатр» Черноброва (7 поколений 1988–~2005, микро-темпоральные эффекты, отклонения темпа времени в долях секунды). Концептуальное пересечение по гравитационному искажению; программы независимы.",
  source="analysis/cross-archive-synthesis.md")

E("src-ecp-session-2026", "ECP session ECP-2026-04-04 validation report — UAP-FRAG-001", "source",
  label_ru="Отчёт валидации ECP-сеанса ECP-2026-04-04 — UAP-FRAG-001",
  description="Three-percipient ECP session on artifact UAP-FRAG-001 (navigation beacon, temporal UAP navigation, Kazakhstan/Tian Shan area, biometal, variable radioactivity). 70% exact matches, 90% exact+partial vs reference data. Primary limitation: compromised blinding (Ekaterina and Tatyana heard Vladislav before responding) = error mode 3 per OSINT validation pipeline. Analyst: Zmiienko Kyryl. Date: 2026-04-06.",
  description_ru="Три перципиента по артефакту UAP-FRAG-001 (навигационный маяк, темпоральная навигация, Казахстан/Тянь-Шань, биометалл, переменная радиоактивность). 70% точных совпадений. Нарушенное ослепление = ошибка 3 конвейера OSINT. Аналитик: Кирилл Змиенко. Дата: 06.04.2026.")

# ════════════════════════════════════════════════════════════════════
# CONNECTIONS — OSINT methodology layer
# ════════════════════════════════════════════════════════════════════

C("p-db", "meth-signature-methodology", ctype="authored", direction="directed")
C("p-db", "meth-anomaly-classes", ctype="authored", direction="directed")
C("p-db", "meth-validation-pipeline", ctype="authored", direction="directed")
C("p-db", "meth-uap-application", ctype="authored", direction="directed")
C("src-osint-methodology-notes", "meth-signature-methodology", ctype="cited-from", direction="directed")
C("src-osint-methodology-notes", "meth-anomaly-classes", ctype="cited-from", direction="directed")
C("src-osint-methodology-notes", "meth-validation-pipeline", ctype="cited-from", direction="directed")
C("src-osint-methodology-notes", "meth-uap-application", ctype="cited-from", direction="directed")
C("meth-signature-methodology", "meth-validation-pipeline", ctype="succeeds", direction="directed")
C("meth-anomaly-classes", "meth-validation-pipeline", ctype="applies-to", direction="directed")
C("meth-validation-pipeline", "meth-uap-application", ctype="applies-to", direction="directed")
C("meth-uap-application", "pj-uap", ctype="applies-to", direction="directed")

# OSINT methodology applied to sibling archives
C("meth-validation-pipeline", "p-lazar", ctype="applies-to", direction="directed")
C("meth-validation-pipeline", "p-chernobrov", ctype="applies-to", direction="directed")
C("meth-validation-pipeline", "cluster-fbi-11", ctype="applies-to", direction="directed")
C("meth-uap-application", "cluster-fbi-11", ctype="classifies", direction="directed")

# ════════════════════════════════════════════════════════════════════
# CONNECTIONS — institutions to cluster / individuals
# ════════════════════════════════════════════════════════════════════

C("p-mccasland", "inst-afrl", ctype="employed-at", direction="directed")
C("p-tores", "inst-nasa-jpl", ctype="employed-at", direction="directed")
C("p-tores", "inst-aerojet", ctype="employed-at", direction="directed")
C("p-garcia", "inst-kcnsc", ctype="employed-at", direction="directed")
C("p-cassias", "inst-lanl", ctype="employed-at", direction="directed")
C("p-chavez", "inst-lanl", ctype="employed-at", direction="directed")
C("p-grillmar", "inst-caltech", ctype="employed-at", direction="directed")
C("p-loureiro", "inst-mit-psfc", ctype="employed-at", direction="directed")
C("p-thomas", "inst-novarti", ctype="employed-at", direction="directed")
C("p-maiwald", "inst-nasa-jpl", ctype="employed-at", direction="directed")
C("p-higgs", "inst-nasa-jpl", ctype="employed-at", direction="directed")
C("p-eskridge", "inst-ies", ctype="employed-at", direction="directed")
C("p-cardillo", "inst-nga", ctype="employed-at", direction="directed")

# ════════════════════════════════════════════════════════════════════
# CONNECTIONS — individuals to cluster super-node
# ════════════════════════════════════════════════════════════════════

C("p-mccasland", "cluster-fbi-11", ctype="member-of-cluster", direction="directed")
C("p-tores", "cluster-fbi-11", ctype="member-of-cluster", direction="directed")
C("p-garcia", "cluster-fbi-11", ctype="member-of-cluster", direction="directed")
C("p-cassias", "cluster-fbi-11", ctype="member-of-cluster", direction="directed")
C("p-chavez", "cluster-fbi-11", ctype="member-of-cluster", direction="directed")
C("p-grillmar", "cluster-fbi-11", ctype="member-of-cluster", direction="directed")
C("p-loureiro", "cluster-fbi-11", ctype="member-of-cluster", direction="directed")
C("p-thomas", "cluster-fbi-11", ctype="member-of-cluster", direction="directed")
C("p-maiwald", "cluster-fbi-11", ctype="member-of-cluster", direction="directed")
C("p-higgs", "cluster-fbi-11", ctype="member-of-cluster", direction="directed")
C("p-eskridge", "cluster-fbi-11", ctype="member-of-cluster", direction="directed")

# ════════════════════════════════════════════════════════════════════
# CONNECTIONS — events to individuals (death/disappearance)
# ════════════════════════════════════════════════════════════════════

C("p-eskridge", "ev-eskridge-death", ctype="died-on", direction="directed")
C("p-chavez", "ev-chavez-disappear", ctype="disappeared-on", direction="directed")
C("p-cassias", "ev-cassias-disappear", ctype="disappeared-on", direction="directed")
C("p-tores", "ev-tores-disappear", ctype="disappeared-on", direction="directed")
C("p-garcia", "ev-garcia-disappear", ctype="disappeared-on", direction="directed")
C("p-thomas", "ev-thomas-found-dead", ctype="died-on", direction="directed")
C("p-loureiro", "ev-loureiro-killed", ctype="died-on", direction="directed")
C("p-mccasland", "ev-mccasland-disappear", ctype="disappeared-on", direction="directed")
C("p-grillmar", "ev-grillmar-killed", ctype="died-on", direction="directed")

# ════════════════════════════════════════════════════════════════════
# CONNECTIONS — FBI investigation
# ════════════════════════════════════════════════════════════════════

C("inst-fbi", "ev-fbi-consolidate", ctype="announced", direction="directed")
C("ev-fbi-consolidate", "cluster-fbi-11", ctype="investigated-by", direction="directed")
C("inst-fbi", "cluster-fbi-11", ctype="investigated-by", direction="directed")
C("src-fox-patel-2026", "ev-fbi-consolidate", ctype="cited-from", direction="directed")
C("src-gera-sheriff-youtube", "cluster-fbi-11", ctype="cited-from", direction="directed")
C("f-fbi-search-patterns", "ev-fbi-consolidate", ctype="cited-from", direction="directed")
C("f-cluster-status-breakdown", "cluster-fbi-11", ctype="cited-from", direction="directed")
C("f-cluster-geo-ca-nm", "cluster-fbi-11", ctype="cited-from", direction="directed")
C("f-cluster-time-concentration", "cluster-fbi-11", ctype="cited-from", direction="directed")
C("f-cluster-specialisation-homogeneity", "cluster-fbi-11", ctype="cited-from", direction="directed")
C("f-lanl-two-in-one-month", "inst-lanl", ctype="cited-from", direction="directed")
C("f-lanl-two-in-one-month", "p-cassias", ctype="cited-from", direction="directed")
C("f-lanl-two-in-one-month", "p-chavez", ctype="cited-from", direction="directed")
C("f-jpl-three-cases", "inst-nasa-jpl", ctype="cited-from", direction="directed")
C("f-cassias-phone-reset", "ev-cassias-disappear", ctype="cited-from", direction="directed")
C("f-cassias-phone-reset", "f-fbi-search-patterns", ctype="applies-to", direction="directed")
C("f-coordinated-action-not-concluded", "cluster-fbi-11", ctype="cited-from", direction="directed")
C("f-mccasland-uap-hint", "p-mccasland", ctype="cited-from", direction="directed")

# ════════════════════════════════════════════════════════════════════
# CONNECTIONS — Cardillo framework
# ════════════════════════════════════════════════════════════════════

C("p-cardillo", "hyp-cardillo-gabriella", ctype="authored", direction="directed")
C("p-cardillo", "ev-cardillo-linkedin-post", ctype="authored", direction="directed")
C("p-cardillo", "inst-nga", ctype="employed-at", direction="directed")
C("hyp-cardillo-gabriella", "cluster-fbi-11", ctype="documented", direction="directed")
C("src-cardillo-linkedin", "hyp-cardillo-gabriella", ctype="cited-from", direction="directed")
C("ev-cardillo-linkedin-post", "hyp-cardillo-gabriella", ctype="cited-from", direction="directed")
C("f-cardillo-no-attribution", "hyp-cardillo-gabriella", ctype="cited-from", direction="directed")
C("p-db", "ev-db-linkedin-comment", ctype="authored", direction="directed")
C("ev-db-linkedin-comment", "ev-cardillo-linkedin-post", ctype="applies-to", direction="directed")
C("ev-db-linkedin-comment", "pj-uap", ctype="cited-from", direction="directed")

# ════════════════════════════════════════════════════════════════════
# CONNECTIONS — UAP taxonomy / cross-archive synthesis
# ════════════════════════════════════════════════════════════════════

C("p-db", "hyp-uap-tax-3", ctype="authored", direction="directed")
C("hyp-uap-tax-3", "p-lazar", ctype="classifies", direction="directed")
C("hyp-uap-tax-3", "p-chernobrov", ctype="classifies", direction="directed")
C("hyp-uap-tax-3", "hyp-ecp-temporal-placement", ctype="framed-by", direction="directed")
C("hyp-uap-tax-3", "cluster-fbi-11", ctype="classifies", direction="directed")
C("hyp-cross-archive-element115-thread", "p-lazar", ctype="cited-from", direction="directed")
C("hyp-cross-archive-element115-thread", "inst-nswc", ctype="cited-from", direction="directed")
C("hyp-cross-archive-spacetime-thread", "p-lazar", ctype="cited-from", direction="directed")
C("hyp-cross-archive-spacetime-thread", "p-chernobrov", ctype="cited-from", direction="directed")
C("hyp-cluster-statistical-signature", "cluster-fbi-11", ctype="applies-to", direction="directed")
C("hyp-cluster-statistical-signature", "meth-validation-pipeline", ctype="framed-by", direction="directed")
C("hyp-ecp-temporal-placement", "src-ecp-session-2026", ctype="cited-from", direction="directed")
C("hyp-ecp-temporal-placement", "meth-validation-pipeline", ctype="challenges", direction="directed")
C("src-jre-2416-farah", "p-lazar", ctype="cited-from", direction="directed")
C("meth-uap-application", "hyp-cardillo-gabriella", ctype="supports", direction="directed")
C("inst-lanl", "cluster-fbi-11", ctype="member-of", direction="directed")
C("inst-nasa-jpl", "cluster-fbi-11", ctype="member-of", direction="directed")
C("inst-afrl", "cluster-fbi-11", ctype="member-of", direction="directed")
C("inst-mit-psfc", "cluster-fbi-11", ctype="member-of", direction="directed")
C("inst-caltech", "cluster-fbi-11", ctype="member-of", direction="directed")
C("inst-kcnsc", "cluster-fbi-11", ctype="member-of", direction="directed")
C("inst-ies", "cluster-fbi-11", ctype="member-of", direction="directed")
C("inst-novarti", "cluster-fbi-11", ctype="member-of", direction="directed")
