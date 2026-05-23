# ════════════════════════════════════════════════════════════════════
# AGENT I — PURSUE Declassification archive (Track 11) — RELEASE 02 EXTENSION
# Sources: war-gov-pursue-archive/ (PURSUE Release 02, war.gov 2026-05-22)
# Authored 2026-05-23 in support of war-gov-pursue-archive Stage 14
#
# This file extends agentI_war_gov_pursue.py with R02 entities. The split mirrors
# the war.gov manifest.json (R01) vs manifest_r02.json (R02) provenance split.
# R02 introduces 3 new contributing agencies (CIA, DOE, ODNI), the New Mexico
# nuclear-weapons-complex institutional cluster (LANL, Sandia, Pantex, Pajarito
# Astronomers, 17th OSI District), 11 new persons (LaPaz, Tuck, Warren, plus 8
# NASA Mercury/Apollo astronauts), and 13 new events spanning 1948→2025.
#
# Cross-link highlights:
# - DOW-D017 Sandia 1948-1950 ↔ FBI 62-HQ Cabell Memo Feb 1949 (operational pair)
# - ODNI-D001 USPER orange-orb 2025 ↔ R01 FBI Western US IR-photo corpus (PdfPair)
# - PR072 Kazakhstan 2022 ↔ chernobrov-archive Soviet-territory corpus
# ════════════════════════════════════════════════════════════════════

# ----- CLUSTER ---------------------------------------------------------

E("cluster-pursue-release-02", "PURSUE Release 02 (Track 11, R02)", "cluster",
  label_ru="PURSUE Релиз 02 (Трек 11, R02)",
  description="The 2026-05-22 Department of War (DoW) PURSUE Release 02 — 64 declassified UAP records published 14 days after R01. Zero source-code overlap with R01 (77 R01 codes ∩ 64 R02 codes = ∅). Composition: 6 new PDFs + 7 NASA audio + 51 DOW PR050-PR099 video records. Expands the PURSUE agency-set from 4 (DoW/FBI/NASA/State) to 7 distinct contributing agencies plus ODNI coordinating body — first-ever PURSUE contribution from CIA, DOE, and ODNI. Combined R01+R02 corpus reaches 225 records. Key institutional signal: DOE breaks its historical categorical-exclusion posture with 3 records anchored in the New Mexico nuclear-weapons complex (Pantex, LANL, LANL-embedded astronomers).",
  description_ru="PURSUE Релиз 02 Министерства войны США (DoW) от 22 мая 2026 — 64 рассекреченные записи по НАЯ, опубликованные через 14 дней после R01. Нулевое пересечение кодов источников с R01 (77 кодов R01 ∩ 64 кода R02 = ∅). Состав: 6 новых PDF + 7 аудио NASA + 51 видеозапись DOW PR050-PR099. Расширяет набор ведомств PURSUE с 4 (DoW/FBI/NASA/State) до 7 различных контрибьюторов плюс координирующее ведомство ODNI — первый вклад в PURSUE от ЦРУ, DOE и ODNI. Совокупный объём R01+R02 достигает 225 записей. Ключевой институциональный сигнал: DOE снимает историческое категорическое исключение тремя записями, привязанными к ядерно-оружейному комплексу Нью-Мексико (Pantex, ЛАНЛ, астрономы при ЛАНЛ).",
  source="war-gov-pursue-archive/manifest_r02.json")

# ----- INSTITUTIONS — new agency contributors --------------------------

E("inst-cia-pursue", "Central Intelligence Agency (PURSUE contributor)", "institution",
  label_ru="Центральное разведывательное управление (контрибьютор PURSUE)",
  description="CIA — first appearance in PURSUE via R02 CIA-UAP-D001: a HUMINT debriefing (Nov 1972 – Nov 1973) of a former Soviet citizen describing Sary Shagan Weapons Testing Range, embedded with one explicit 'unidentified aerial phenomenon' inside an otherwise conventional ABM/SAM/laser-research intelligence report. UAP body detail is REDACTED while the surrounding HUMINT scaffold is structurally CORROBORATED.",
  description_ru="ЦРУ — первое появление в PURSUE через R02 CIA-UAP-D001: HUMINT-дебрифинг (ноябрь 1972 – ноябрь 1973) бывшего советского гражданина с описанием полигона Сары-Шаган, встроенный с одним явным «неопознанным аэрокосмическим явлением» в обычный разведывательный отчёт о ABM/SAM/лазерных исследованиях. Описание самого НАЯ — ⬛ REDACTED, а окружающий HUMINT-каркас — ✅ структурно CORROBORATED.",
  source="war-gov-pursue-archive/analysis/per-document/CIA-UAP-D001_USSR-SARY-SHAGAN-1973.md")

E("inst-doe-pursue", "Department of Energy (PURSUE contributor — first DOE contribution)", "institution",
  label_ru="Министерство энергетики США (DOE, контрибьютор PURSUE — первый вклад DOE)",
  description="DOE — first appearance in PURSUE via R02 (3 records: DOE-D001 Pantex radar incident, DOE-D002 Tuck correspondence 1976, DOE-D003 Pajarito Astronomers 1986). Historically DOE has declined to release UFO/UAP-related material under categorical exclusions tied to nuclear-weapons-information control; R02 is the first PURSUE release in which DOE contributes material — three records, all anchored in the New Mexico nuclear-weapons complex. This is a verifiable institutional posture change at the agency that controls the most sensitive UAP-adjacent corpus (Hanford, Oak Ridge, Sandia, LANL, NTS, Pantex). Note: distinct PURSUE-namespaced node from the anchor 'inst-doe' (which represents the broader DOE first-reader posture on the ASRP repo).",
  description_ru="DOE — первое появление в PURSUE через R02 (3 записи: DOE-D001 инцидент с радаром Pantex, DOE-D002 переписка Тука 1976, DOE-D003 астрономы Pajarito 1986). Исторически DOE отказывалось рассекречивать UFO/UAP-материалы по категорическим исключениям, связанным с контролем ядерно-оружейной информации; R02 — первый релиз PURSUE с материалом DOE — три записи, все привязанные к ядерно-оружейному комплексу Нью-Мексико. Проверяемое изменение институциональной позиции ведомства, контролирующего самый чувствительный UAP-смежный корпус (Hanford, Oak Ridge, Sandia, ЛАНЛ, NTS, Pantex). Отличается от anchor-узла 'inst-doe', который представляет более широкую позицию первого читателя DOE по ASRP-репозиторию.",
  source="war-gov-pursue-archive/analysis/MASTER_pursue_claims.md")

E("inst-odni-pursue", "ODNI (PURSUE contributor)", "institution",
  label_ru="ODNI (контрибьютор PURSUE)",
  description="Office of the Director of National Intelligence — first appearance in PURSUE via R02 ODNI-UAP-D001: USPER first-person narrative by a senior USIC officer of a helicopter encounter at a U.S. weapons test range in late 2025. Explicitly paired in the war.gov CSV metadata with R01 FBI Photo A001-A008 + B001-B024 + USPER Statement (32 R01 records). This single PdfPair is 'the single most consequential R01↔R02 cross-link' per the MASTER claims document.",
  description_ru="Офис директора национальной разведки — первое появление в PURSUE через R02 ODNI-UAP-D001: повествование от первого лица USPER от старшего сотрудника USIC о встрече с вертолётом на полигоне испытаний оружия США в конце 2025. Явно спарено в метаданных CSV war.gov с R01 FBI Photo A001-A008 + B001-B024 + USPER Statement (32 записи R01). Этот единичный PdfPair — «самая важная перекрёстная связь R01↔R02» согласно MASTER claims document.",
  source="war-gov-pursue-archive/analysis/per-document/ODNI-UAP-D001_USPER-ORANGE-ORBS-2025.md")

# ----- INSTITUTIONS — New Mexico nuclear-weapons complex --------------

E("inst-sandia", "Sandia National Laboratories", "institution",
  label_ru="Национальные лаборатории Сандия",
  description="DOE national laboratory, Albuquerque NM. Invoked twice in R02: (1) as image-enhancement provider for the Pantex Ground Surveillance Radar Tower incident (DOE-D001), and (2) as the geographic locus 'Sandia Base / Kirtland AFB / 17th OSI District 1948-1950' for the DOW-D017 Green Fireballs compilation. The 1948-1950 Sandia Base operational programme is structurally paired with the FBI 62-HQ-Sr164 Cabell Memorandum #4 (Feb 1949) — same response window, two federal entry points (FBI custodianship of the Cabell Memo vs. OSI custodianship of the Sandia operational record).",
  description_ru="Национальная лаборатория DOE, Альбукерке, штат Нью-Мексико. Упоминается в R02 дважды: (1) как поставщик улучшения изображения для инцидента с радарной башней наблюдения Pantex (DOE-D001), и (2) как географическое местоположение «База Сандия / Авиабаза Киртланд / 17-й район OSI 1948-1950» для компиляции зелёных фаерболлов DOW-D017. Оперативная программа Базы Сандия 1948-1950 структурно спарена с меморандумом ФБР 62-HQ-Sr164 Cabell #4 (фев. 1949) — то же временное окно реакции, две федеральные точки входа.",
  location="Albuquerque, New Mexico, USA",
  source="war-gov-pursue-archive/analysis/per-document/DOW-UAP-D017_SANDIA-GREEN-FIREBALLS.md")

E("inst-pantex", "Pantex Plant (TX)", "institution",
  label_ru="Завод Pantex (Техас)",
  description="DOE-NNSA nuclear-weapons assembly and disassembly facility, near Amarillo Texas. Operated by Consolidated Nuclear Security LLC (CNS) for DOE-NNSA. Site of the DOE-D001 incident: Ground Surveillance Radar Tower captures an unidentified object; Sandia performs image enhancement. Object description is ⬛ REDACTED under UCNI (Unclassified Controlled Nuclear Information) while the process chain (radar capture → Sandia enhancement → archival) is ✅ CORROBORATED. CNS as Pantex operator is also a Track 7 corporate-overlay target relevant to the EG&G → Amentum lineage mapping.",
  description_ru="Завод DOE-NNSA по сборке и разборке ядерного оружия, около Амарилло, штат Техас. Эксплуатируется Consolidated Nuclear Security LLC (CNS) для DOE-NNSA. Место инцидента DOE-D001: радарная башня наземного наблюдения фиксирует неопознанный объект; Сандия выполняет улучшение изображения. Описание объекта ⬛ REDACTED под UCNI (Unclassified Controlled Nuclear Information), а процессная цепочка (захват радаром → улучшение Сандии → архивирование) ✅ CORROBORATED. CNS как оператор Pantex также является целью корпоративного наложения Трека 7 для маппинга линии EG&G → Amentum.",
  location="Carson County, Texas, USA",
  source="war-gov-pursue-archive/analysis/per-document/DOE-UAP-D001_PANTEX-RADAR.md")

E("inst-pajarito-astronomers", "Pajarito Astronomers (LANL-embedded amateur astronomy club)", "institution",
  label_ru="Pajarito Astronomers (любительский астроклуб при ЛАНЛ)",
  description="LANL-embedded amateur astronomy club. Hosted Dr John Warren (LANL AT-6 division) for talk 'Why Should a Scientist be Concerned about UFO's?' on 29 May 1986 at Fuller Lodge, Los Alamos. Documents institutional UAP engagement at LANL during precisely the decade the Bob Lazar narrative covers (1986 vs Lazar's claimed 1988-89 S-4 tenure) — providing critical contextual reading material for Lazar's claims without corroborating or refuting them.",
  description_ru="Любительский астрономический клуб при ЛАНЛ. Принимал д-ра Джона Уоррена (ЛАНЛ, дивизия AT-6) с лекцией «Почему учёный должен интересоваться НЛО?» 29 мая 1986 в Fuller Lodge, Лос-Аламос. Документирует институциональное вовлечение ЛАНЛ в UAP-тематику именно в десятилетие, охватываемое нарративом Лазара (1986 vs заявленный Лазаром период S-4 1988-89) — предоставляя критический контекст для заявлений Лазара, не подтверждая и не опровергая их.",
  source="war-gov-pursue-archive/analysis/per-document/DOE-UAP-D003_PAJARITO-ASTRONOMERS.md")

E("inst-17th-osi", "17th OSI District (1948-1950)", "institution",
  label_ru="17-й район OSI (1948-1950)",
  description="Air Force Office of Special Investigations 17th District (Kirtland AFB / Sandia Base, Albuquerque NM) — the operational custodian of the 1948-1950 UAP sighting compilation released as DOW-D017. Classified sightings into three District categories (green-fireball / disc / misc), consulted Dr Lincoln LaPaz, and operated a technical impactment-sampling programme at Socorro from 24 July 1949. The 17th OSI District documentary record is a methodological ancestor of the modern OSINT validation pipeline.",
  description_ru="17-й район Управления специальных расследований ВВС (Авиабаза Киртланд / База Сандия, Альбукерке, штат Нью-Мексико) — оперативный хранитель компиляции UAP-наблюдений 1948-1950, выпущенной как DOW-D017. Классифицировал наблюдения по трём районным категориям (зелёные фаерболлы / диски / прочее), консультировался с д-ром Линкольном Лапазом и управлял технической программой отбора проб ударов в Сокорро с 24 июля 1949. Документальная запись 17-го района OSI — методологический предок современного OSINT-конвейера валидации.",
  source="war-gov-pursue-archive/analysis/per-document/DOW-UAP-D017_SANDIA-GREEN-FIREBALLS.md")

E("inst-uscg", "U.S. Coast Guard (PURSUE contributor via DOW)", "institution",
  label_ru="Береговая охрана США (контрибьютор PURSUE через DOW)",
  description="USCG — first appearance in PURSUE via R02 DOW-PR065 + DOW-PR066: USCG C-144 fixed-wing IR observation of a 'tic-tac IR hot' UAP at Tyndall AFB on 24 April 2024. Distributed under the DOW agency banner inside PR050-PR099, not as a separate USCG agency lane.",
  description_ru="Береговая охрана США — первое появление в PURSUE через R02 DOW-PR065 + DOW-PR066: ИК-наблюдение «tic-tac IR hot» НАЯ с самолёта C-144 USCG на Авиабазе Тиндалл 24 апреля 2024. Распространено под знаменем ведомства DOW внутри PR050-PR099, а не как отдельная линия USCG.",
  source="war-gov-pursue-archive/analysis/MASTER_pursue_claims.md#§13.1")

E("inst-norad", "NORAD (PURSUE contextual)", "institution",
  label_ru="NORAD (контекст PURSUE)",
  description="North American Aerospace Defense Command — contextual institution for R02 DOW-PR071 (USAF ANG F-16C Lake Huron shootdown of 12 February 2023). NORAD was the operational command authority for the publicly-acknowledged shootdown sequence; the PR071 video record is the DoW-internal raw-asset counterpart to the public NORAD press cycle.",
  description_ru="Командование воздушно-космической обороны Северной Америки — контекстная институция для R02 DOW-PR071 (сбитие F-16C Национальной гвардии ВВС над озером Гурон 12 февраля 2023). NORAD был оперативной командной инстанцией для публично подтверждённой последовательности сбития; видеозапись PR071 — внутриведомственный сырой-актив DoW, парный публичному пресс-циклу NORAD.",
  source="war-gov-pursue-archive/analysis/MASTER_pursue_claims.md#§13.1")

# ----- PERSONS — R02 PDF principals -----------------------------------

E("person-lincoln-lapaz", "Dr Lincoln LaPaz (consultant, 1948-1950)", "person · external",
  label_ru="Д-р Линкольн Лапаз (консультант, 1948-1950)",
  description="University of New Mexico meteoriticist (Institute of Meteoritics). Consulting expert to the 17th OSI District for the Sandia Green Fireballs 1948-1950 programme. Drove the impactment-sampling expectation (a meteoritic-origin recovery would have validated his discipline); programmatic non-recovery is itself a documentary signal. Named in DOW-D017.",
  description_ru="Метеоритолог Университета Нью-Мексико (Институт метеоритики). Консультант 17-го района OSI по программе зелёных фаерболлов Сандии 1948-1950. Двигал ожидание отбора проб ударов (восстановление метеоритного происхождения подтвердило бы его дисциплину); программное невосстановление — само по себе документальный сигнал. Назван в DOW-D017.")

E("person-james-tuck", "Dr James L. Tuck (LANL senior physicist)", "person · external",
  label_ru="Д-р Джеймс Л. Так (старший физик ЛАНЛ)",
  description="Manhattan Project veteran and senior LANL physicist. Subject of DOE-D002 (1976 correspondence): requested a simulated-atomic-bomb recipe to study large atmospheric vortices reported in the Condon Report; correspondent links to ball lightning, McCampbell UFOLOGY (1976), and Einstein unified-field-theory work. Documents institutional LANL UAP-adjacent engagement in 1976, one decade before the Pajarito Astronomers Warren talk (1986).",
  description_ru="Ветеран Манхэттенского проекта и старший физик ЛАНЛ. Субъект DOE-D002 (переписка 1976): запросил рецепт симуляции атомной бомбы для изучения крупных атмосферных вихрей, описанных в Condon Report; корреспондент ссылается на шаровую молнию, McCampbell UFOLOGY (1976) и работы Эйнштейна по единой теории поля. Документирует институциональное UAP-смежное вовлечение ЛАНЛ в 1976, на десятилетие раньше лекции Уоррена при астрономах Pajarito (1986).")

E("person-john-warren", "Dr John Warren (LANL AT-6 division)", "person · external",
  label_ru="Д-р Джон Уоррен (ЛАНЛ, дивизия AT-6)",
  description="LANL physicist in the AT-6 division. Speaker at the Pajarito Astronomers talk 'Why Should a Scientist be Concerned about UFO's?' on 29 May 1986 at Fuller Lodge, Los Alamos. Documents institutional LANL UAP-engagement during the Lazar-tenure decade (1986 vs Lazar's claimed 1988-89 S-4 work). Named in DOE-D003.",
  description_ru="Физик ЛАНЛ в дивизии AT-6. Спикер лекции при астрономах Pajarito «Почему учёный должен интересоваться НЛО?» 29 мая 1986 в Fuller Lodge, Лос-Аламос. Документирует институциональное UAP-вовлечение ЛАНЛ в десятилетие пребывания Лазара (1986 vs заявленная Лазаром работа на S-4 в 1988-89). Назван в DOE-D003.")

# ----- PERSONS — NASA Mercury / Apollo astronauts (R02 audio corpus) --

E("person-gordon-cooper", "Gordon Cooper (Mercury MA-9, 1963)", "person · external",
  label_ru="Гордон Купер (Mercury MA-9, 1963)",
  description="NASA Mercury astronaut. Pilot of Mercury-Atlas 9 (MA-9, 1963). Subject of one of the seven R02 NASA audio excerpts: the MA-9 'fireflies' verbal record.",
  description_ru="Астронавт NASA по программе Mercury. Пилот Mercury-Atlas 9 (MA-9, 1963). Субъект одного из семи аудиофрагментов NASA в R02: голосовая запись «светлячков» с MA-9.")

E("person-scott-carpenter", "Scott Carpenter (Mercury MA-7)", "person · external",
  label_ru="Скотт Карпентер (Mercury MA-7)",
  description="NASA Mercury astronaut. Pilot of Mercury-Atlas 7 (MA-7). Named in the R02 NASA Mercury/Apollo audio corpus.",
  description_ru="Астронавт NASA по программе Mercury. Пилот Mercury-Atlas 7 (MA-7). Назван в аудиокорпусе Mercury/Apollo NASA R02.")

E("person-walter-schirra", "Walter Schirra (Mercury MA-8)", "person · external",
  label_ru="Уолтер Ширра (Mercury MA-8)",
  description="NASA Mercury astronaut. Pilot of Mercury-Atlas 8 (MA-8). Named in the R02 NASA Mercury/Apollo audio corpus.",
  description_ru="Астронавт NASA по программе Mercury. Пилот Mercury-Atlas 8 (MA-8). Назван в аудиокорпусе Mercury/Apollo NASA R02.")

E("person-virgil-grissom", "Virgil 'Gus' Grissom (Mercury MR-4)", "person · external",
  label_ru="Вирджил «Гас» Гриссом (Mercury MR-4)",
  description="NASA Mercury astronaut. Pilot of Mercury-Redstone 4 (MR-4 / Liberty Bell 7). Named in the R02 NASA Mercury/Apollo audio corpus.",
  description_ru="Астронавт NASA по программе Mercury. Пилот Mercury-Redstone 4 (MR-4 / Liberty Bell 7). Назван в аудиокорпусе Mercury/Apollo NASA R02.")

E("person-charles-conrad", "Charles 'Pete' Conrad (Apollo 12, 1969)", "person · external",
  label_ru="Чарльз «Пит» Конрад (Apollo 12, 1969)",
  description="NASA Apollo astronaut. Commander of Apollo 12 (November 1969). Named in the R02 NASA audio corpus together with Apollo-12 LMP Alan Bean.",
  description_ru="Астронавт NASA по программе Apollo. Командир Apollo 12 (ноябрь 1969). Назван в аудиокорпусе NASA R02 вместе с LMP Apollo 12 Аланом Бином.")

E("person-alan-bean", "Alan Bean (Apollo 12 LMP, 1969)", "person · external",
  label_ru="Алан Бин (Apollo 12 LMP, 1969)",
  description="NASA Apollo astronaut. Lunar Module Pilot of Apollo 12 (November 1969). Named in the R02 NASA audio corpus together with Apollo-12 commander Charles Conrad.",
  description_ru="Астронавт NASA по программе Apollo. Пилот лунного модуля Apollo 12 (ноябрь 1969). Назван в аудиокорпусе NASA R02 вместе с командиром Apollo 12 Чарльзом Конрадом.")

E("person-gene-cernan", "Eugene 'Gene' Cernan (Apollo 17 CDR, 1972)", "person · external",
  label_ru="Юджин «Джин» Сернан (Apollo 17 CDR, 1972)",
  description="NASA Apollo astronaut. Commander of Apollo 17 (December 1972) — the last Apollo lunar landing. Named in the R02 NASA audio corpus together with Apollo-17 LMP Harrison Schmitt. Cross-link target: VM6 active-investigation photograph (R01 ev-vm6-apollo17).",
  description_ru="Астронавт NASA по программе Apollo. Командир Apollo 17 (декабрь 1972) — последняя лунная посадка Apollo. Назван в аудиокорпусе NASA R02 вместе с LMP Apollo 17 Гаррисоном Шмиттом. Цель кросс-связи: фотография активного расследования VM6 (R01 ev-vm6-apollo17).")

E("person-harrison-schmitt", "Harrison 'Jack' Schmitt (Apollo 17 LMP, 1972)", "person · external",
  label_ru="Гаррисон «Джек» Шмитт (Apollo 17 LMP, 1972)",
  description="NASA Apollo astronaut and geologist. Lunar Module Pilot of Apollo 17 (December 1972). Named in the R02 NASA audio corpus together with Apollo-17 commander Gene Cernan. Cross-link target: VM6 active-investigation photograph (R01 ev-vm6-apollo17).",
  description_ru="Астронавт-геолог NASA по программе Apollo. Пилот лунного модуля Apollo 17 (декабрь 1972). Назван в аудиокорпусе NASA R02 вместе с командиром Apollo 17 Джином Сернаном. Цель кросс-связи: фотография активного расследования VM6 (R01 ev-vm6-apollo17).")

# ----- EVENTS — R02 PDF cases -----------------------------------------

E("ev-sandia-green-fireballs-1948-1950", "Sandia Base / Kirtland 17th-OSI Green Fireballs 1948-1950 (DOW-D017)", "event",
  date="1948-1950",
  label_ru="Зелёные фаерболлы Базы Сандия / Киртланд 17-й район OSI 1948-1950 (DOW-D017)",
  description="Sandia Base / Kirtland AFB / 17th OSI District 1948-1950 compilation of UAP sightings. Classified in three District categories (green-fireball / disc / miscellaneous). Dr Lincoln LaPaz consulting expert. Technical impactment-sampling programme at Socorro from 24 July 1949 onward. Camp Hood TX cross-correlation. Starvation Peak Incident reference. Verdict: ✅ CORROBORATED. Structurally paired with the FBI 62-HQ-Sr164 Cabell Memorandum #4 (Feb 1949): same response window, two federal entry points — FBI custodianship of the Cabell Memo (form-side taxonomy) vs OSI custodianship of the Sandia record (operational implementation).",
  description_ru="Компиляция UAP-наблюдений Базы Сандия / Авиабазы Киртланд / 17-го района OSI 1948-1950. Классифицирована по трём районным категориям (зелёные фаерболлы / диски / прочее). Д-р Линкольн Лапаз — консультант-эксперт. Техническая программа отбора проб ударов в Сокорро с 24 июля 1949. Кросс-корреляция Camp Hood, Техас. Ссылка на Starvation Peak Incident. Вердикт: ✅ CORROBORATED. Структурно спарено с меморандумом ФБР 62-HQ-Sr164 Cabell #4 (фев. 1949): то же окно реакции, две федеральные точки входа — ФБР как хранитель меморандума Cabell (форменная сторона таксономии) vs OSI как хранитель Сандийской записи (оперативная реализация).",
  source="war-gov-pursue-archive/analysis/per-document/DOW-UAP-D017_SANDIA-GREEN-FIREBALLS.md")

E("ev-socorro-impactment-1949", "17th-OSI Socorro impactment-sampling programme (24 July 1949 →)", "event",
  date="1949-07-24",
  label_ru="Программа отбора проб ударов 17-го района OSI в Сокорро (24 июля 1949 →)",
  description="Technical impactment-sampling programme at Socorro NM begun 24 July 1949 under the 17th OSI District green-fireball investigation. Driven by Lincoln LaPaz's meteoritic-origin hypothesis: physical recovery would have validated his discipline. Programmatic non-recovery is itself a documentary signal of an exotic-source hypothesis the operational record could not close. Distinct from (and earlier than) the 1964 Socorro physical-trace anchor in FBI Sr438.",
  description_ru="Техническая программа отбора проб ударов в Сокорро, штат Нью-Мексико, начата 24 июля 1949 в рамках расследования зелёных фаерболлов 17-го района OSI. Двигалась гипотезой метеоритного происхождения Линкольна Лапаза: физическое восстановление подтвердило бы его дисциплину. Программное невосстановление — само по себе документальный сигнал экзотической гипотезы источника, которую оперативная запись не смогла закрыть. Отличается (и предшествует) якорю физических следов в Сокорро 1964 в FBI Sr438.",
  source="war-gov-pursue-archive/analysis/per-document/DOW-UAP-D017_SANDIA-GREEN-FIREBALLS.md")

E("ev-pantex-radar-incident", "Pantex Ground Surveillance Radar Tower UAP capture (DOE-D001)", "event",
  label_ru="Захват НАЯ радарной башней наземного наблюдения Pantex (DOE-D001)",
  description="Pantex (DOE-NNSA nuclear-weapons assembly facility, TX) Ground Surveillance Radar Tower captures unidentified object. Sandia performs image enhancement. Verdict: ⬛ REDACTED on object description (UCNI — Unclassified Controlled Nuclear Information); ✅ CORROBORATED on the process chain (radar capture → Sandia enhancement → archival custody → release). First DOE PURSUE contribution alongside DOE-D002 and DOE-D003.",
  description_ru="Радарная башня наземного наблюдения Pantex (объект DOE-NNSA по сборке ядерного оружия, Техас) фиксирует неопознанный объект. Сандия выполняет улучшение изображения. Вердикт: ⬛ REDACTED для описания объекта (UCNI — неклассифицированная контролируемая ядерная информация); ✅ CORROBORATED для процессной цепочки (захват радаром → улучшение Сандии → архивное хранение → релиз). Первый вклад DOE в PURSUE наряду с DOE-D002 и DOE-D003.",
  source="war-gov-pursue-archive/analysis/per-document/DOE-UAP-D001_PANTEX-RADAR.md")

E("ev-tuck-correspondence-1976", "James Tuck atmospheric-vortex correspondence (1976, DOE-D002)", "event",
  date="1976",
  label_ru="Переписка Джеймса Така об атмосферных вихрях (1976, DOE-D002)",
  description="James L. Tuck (Manhattan Project veteran, senior LANL physicist) requests simulated-atomic-bomb recipe to study large atmospheric vortices reported in the Condon Report. Correspondent links to ball lightning, McCampbell UFOLOGY (1976), and Einstein unified-field-theory work. Verdict: ✅ CORROBORATED. Same conceptual genealogy as element-115 propulsion-physics discourse — cross-link target for dubna-element-115-analysis sibling archive.",
  description_ru="Джеймс Л. Так (ветеран Манхэттенского проекта, старший физик ЛАНЛ) запрашивает рецепт симуляции атомной бомбы для изучения крупных атмосферных вихрей, описанных в Condon Report. Корреспондент ссылается на шаровую молнию, McCampbell UFOLOGY (1976) и работы Эйнштейна по единой теории поля. Вердикт: ✅ CORROBORATED. Та же концептуальная генеалогия, что и дискурс о двигательной установке на 115-м элементе — цель кросс-связи для смежного архива dubna-element-115-analysis.",
  source="war-gov-pursue-archive/analysis/per-document/DOE-UAP-D002_JAMES-TUCK-CORRESPONDENCE.md")

E("ev-pajarito-astronomers-warren-1986", "Pajarito Astronomers Warren talk (29 May 1986, DOE-D003)", "event",
  date="1986-05-29",
  label_ru="Лекция Уоррена для астрономов Pajarito (29 мая 1986, DOE-D003)",
  description="Pajarito Astronomers (LANL-embedded amateur astronomy club) hosts Dr John Warren (LANL AT-6) for talk 'Why Should a Scientist be Concerned about UFO's?' on 29 May 1986 at Fuller Lodge, Los Alamos. Verdict: ✅ CORROBORATED. Documents institutional LANL UAP engagement during the decade overlapping the Lazar narrative — providing contextual reading material for Lazar's claims without corroborating or refuting them.",
  description_ru="Астрономы Pajarito (любительский астроклуб при ЛАНЛ) принимают д-ра Джона Уоррена (ЛАНЛ, AT-6) с лекцией «Почему учёный должен интересоваться НЛО?» 29 мая 1986 в Fuller Lodge, Лос-Аламос. Вердикт: ✅ CORROBORATED. Документирует институциональное UAP-вовлечение ЛАНЛ в десятилетие, пересекающееся с нарративом Лазара — предоставляет контекстный материал для заявлений Лазара, не подтверждая и не опровергая их.",
  source="war-gov-pursue-archive/analysis/per-document/DOE-UAP-D003_PAJARITO-ASTRONOMERS.md")

E("ev-sary-shagan-cia-hum-1973", "CIA HUMINT debriefing — Sary Shagan 1972-1973 (CIA-D001)", "event",
  date="1972-11/1973-11",
  label_ru="HUMINT-дебрифинг ЦРУ — Сары-Шаган 1972-1973 (CIA-D001)",
  description="CIA HUMINT debriefing (Nov 1972 – Nov 1973) of former Soviet citizen describing Sary Shagan Weapons Testing Range. Otherwise conventional ABM/SAM/laser-research intelligence report containing one embedded 'unidentified aerial phenomenon'. Verdict: ✅ structurally CORROBORATED on HUMINT scaffold; ⬛ REDACTED on UAP body detail. First-ever CIA PURSUE contribution. Direct U.S.-side intelligence parallel to Chernobrov's USSR-side field-investigation corpus.",
  description_ru="HUMINT-дебрифинг ЦРУ (ноябрь 1972 – ноябрь 1973) бывшего советского гражданина с описанием полигона Сары-Шаган. В остальном обычный разведотчёт о исследованиях ABM/SAM/лазеров с одним встроенным «неопознанным аэрокосмическим явлением». Вердикт: ✅ структурно CORROBORATED по HUMINT-каркасу; ⬛ REDACTED по описанию НАЯ. Первый в истории вклад ЦРУ в PURSUE. Прямая параллель разведсообщества США к корпусу полевых расследований Черноброва в СССР.",
  source="war-gov-pursue-archive/analysis/per-document/CIA-UAP-D001_USSR-SARY-SHAGAN-1973.md")

E("ev-usper-orange-orb-2025", "USPER orange-orb helicopter encounter late 2025 (ODNI-D001)", "event",
  date="2025",
  label_ru="Встреча USPER с оранжевыми сферами с вертолёта в конце 2025 (ODNI-D001)",
  description="USPER (US Person) first-person narrative by senior USIC officer: helicopter encounter at a U.S. weapons test range in late 2025. FLIR 'super-hot' closing object split-into-two; 'countless orange orbs swarming' at mountain backdrop; 'T'-formation orbs at 700 ft hover sequentially flaring/dimming; same orbs subsequently 'chasing' fighter jets at ~23,000 ft AGL. Verdict: ✅ CORROBORATED at narrative-evidence tier; ⬛ REDACTED on witness identity by USPER policy. Explicitly PdfPairs with R01 FBI Photo A001-A008 + B001-B024 + R01 USPER Statement (32 R01 records) — the single most consequential R01↔R02 cross-link.",
  description_ru="Повествование от первого лица USPER (гражданин США) от старшего сотрудника USIC: встреча с вертолётом на полигоне испытаний оружия США в конце 2025. FLIR-«сверхгорячий» сближающийся объект, разделяющийся на два; «бесчисленные оранжевые сферы, роящиеся» на фоне горы; сферы в «Т»-формации на высоте 700 футов последовательно вспыхивают/тускнеют; те же сферы затем «преследуют» истребители на высоте ~23 000 футов AGL. Вердикт: ✅ CORROBORATED на уровне нарративных свидетельств; ⬛ REDACTED по личности свидетеля по политике USPER. Явно PdfPairs с R01 FBI Photo A001-A008 + B001-B024 + R01 USPER Statement (32 записи R01) — самая важная перекрёстная связь R01↔R02.",
  source="war-gov-pursue-archive/analysis/per-document/ODNI-UAP-D001_USPER-ORANGE-ORBS-2025.md")

# ----- EVENTS — Operationally significant R02 PR-series videos --------

E("ev-lake-huron-shootdown-2023", "F-16C Lake Huron UAP shootdown 12 February 2023 (PR071)", "event",
  date="2023-02-12",
  label_ru="Сбитие НАЯ F-16C над озером Гурон 12 февраля 2023 (PR071)",
  description="DOW-UAP-PR071: 'USAF ANG F-16C (callsign [CALLSIGN]) Shoots Down UAP over Lake Huron with [CALLSIGN]' — DoW-internal raw-asset counterpart to the publicly-acknowledged Lake Huron shootdown of 12 February 2023. NORAD operational command context. Verdict: ✅ CORROBORATED.",
  description_ru="DOW-UAP-PR071: «F-16C ANG ВВС США (позывной [CALLSIGN]) сбивает НАЯ над озером Гурон с [CALLSIGN]» — внутриведомственный сырой-актив DoW, парный публично подтверждённому сбитию над озером Гурон 12 февраля 2023. Контекст оперативного командования NORAD. Вердикт: ✅ CORROBORATED.",
  source="war-gov-pursue-archive/analysis/MASTER_pursue_claims.md#§13.1")

E("ev-kazakhstan-pr072-2022", "Kazakhstan IIR Administrative Revision 2022 (PR072)", "event",
  date="2022",
  label_ru="Административная ревизия IIR Казахстан 2022 (PR072)",
  description="DOW-UAP-PR072: 'ADMINISTRATIVE REVISION: IIR 1777 J0032 22 Kazakhstan' — extends ASRP Soviet-archive cross-reference into 2022. Verdict: ✅ CORROBORATED. Cross-archive bridge to chernobrov-archive Soviet-territory corpus and to the existing R01 Kazakhstan 1994 cable (Tajik Air B747SP FL410).",
  description_ru="DOW-UAP-PR072: «АДМИНИСТРАТИВНАЯ РЕВИЗИЯ: IIR 1777 J0032 22 Казахстан» — расширяет кросс-ссылку ASRP на советский архив до 2022. Вердикт: ✅ CORROBORATED. Кросс-архивный мост к корпусу полевых расследований СССР chernobrov-archive и к существующей R01 кабельной телеграмме Казахстан 1994 (Tajik Air B747SP FL410).",
  source="war-gov-pursue-archive/analysis/MASTER_pursue_claims.md#§13.1")

E("ev-tyndall-uscg-2024", "USCG C-144 Tyndall AFB tic-tac IR 24 April 2024 (PR065+PR066)", "event",
  date="2024-04-24",
  label_ru="USCG C-144 Тиндалл «тик-так» ИК 24 апреля 2024 (PR065+PR066)",
  description="DOW-UAP-PR065 + DOW-UAP-PR066: USCG C-144 fixed-wing IR observation of a 'tic-tac IR hot' UAP at Tyndall AFB on 24 April 2024. First USCG appearance in PURSUE (distributed under the DOW agency banner). Verdict: ⚠ PARTIAL.",
  description_ru="DOW-UAP-PR065 + DOW-UAP-PR066: ИК-наблюдение «tic-tac IR hot» НАЯ с самолёта C-144 USCG на Авиабазе Тиндалл 24 апреля 2024. Первое появление USCG в PURSUE (распространено под знаменем ведомства DOW). Вердикт: ⚠ PARTIAL.",
  source="war-gov-pursue-archive/analysis/MASTER_pursue_claims.md#§13.1")

E("ev-kabul-afsoc-2017", "AFSOC Kabul UAP July 2017 (PR064)", "event",
  date="2017-07",
  label_ru="AFSOC Кабул НАЯ июль 2017 (PR064)",
  description="DOW-UAP-PR064: 'AFSOC Kabul UAP Jul 2017' — pre-withdrawal Kabul-area incident, otherwise unreported in the public record. Verdict: ⚠ PARTIAL.",
  description_ru="DOW-UAP-PR064: «AFSOC Кабул НАЯ июль 2017» — инцидент в районе Кабула до вывода войск, в остальном не задокументированный в публичных источниках. Вердикт: ⚠ PARTIAL.",
  source="war-gov-pursue-archive/analysis/MASTER_pursue_claims.md#§13.1")

E("ev-2021-04-12-cluster", "PR050-PR099 CENTCOM cluster 2021-04-12 segmentation", "event",
  date="2021-04-12",
  label_ru="Кластер CENTCOM 2021-04-12 в сегментации PR050-PR099",
  description="One of the multi-video CENTCOM date-clusters surfacing in the R02 PR050-PR099 corpus (segmented across multiple assets). Date-level operational tempo signal for the CENTCOM AOR 2020-2024 dominance pattern (≥25 of 50 R02 videos in CENTCOM AOR).",
  description_ru="Один из мультивидео-кластеров CENTCOM по датам, проявляющихся в корпусе R02 PR050-PR099 (сегментировано по нескольким активам). Сигнал оперативного темпа уровня даты для паттерна доминирования AOR CENTCOM 2020-2024 (≥25 из 50 видео R02 в AOR CENTCOM).",
  source="war-gov-pursue-archive/analysis/MASTER_pursue_claims.md#§13")

E("ev-aug-oct-2020-centcom-cluster", "PR050-PR099 CENTCOM cluster Aug-Oct 2020", "event",
  date="2020-08/2020-10",
  label_ru="Кластер CENTCOM PR050-PR099 август-октябрь 2020",
  description="The August-October 2020 CENTCOM AOR concentration in the R02 PR050-PR099 video corpus (Iran / Syria / Iraq / Persian Gulf / Arabian Sea / Gulf of Oman). Operationally-significant tempo cluster.",
  description_ru="Концентрация в AOR CENTCOM август-октябрь 2020 в видеокорпусе R02 PR050-PR099 (Иран / Сирия / Ирак / Персидский залив / Аравийское море / Оманский залив). Операционно значимый кластер по темпу.",
  source="war-gov-pursue-archive/analysis/MASTER_pursue_claims.md#§13")

E("ev-ma9-fireflies-1963", "Mercury MA-9 'fireflies' verbal record (Cooper, 1963)", "event",
  date="1963",
  label_ru="Голосовая запись «светлячков» с MA-9 (Купер, 1963)",
  description="Mercury-Atlas 9 (MA-9, 1963) verbal record of Gordon Cooper's 'fireflies' observation — one of the seven R02 NASA Mercury/Apollo audio excerpts. Continues the R01 NASA spaceflight-cluster pattern (Gemini 7, Apollo 11/12/17, Skylab) backward into Mercury.",
  description_ru="Голосовая запись Mercury-Atlas 9 (MA-9, 1963) наблюдения «светлячков» Гордона Купера — один из семи аудиофрагментов Mercury/Apollo NASA в R02. Продолжает паттерн NASA-кластера пилотируемых полётов R01 (Gemini 7, Apollo 11/12/17, Skylab) назад в эпоху Mercury.",
  source="war-gov-pursue-archive/analysis/MASTER_pursue_claims.md#§12.1")

# ----- HYPOTHESIS / FINDING NODES -------------------------------------

E("hyp-cabell-sandia-1949-pair", "DOW-D017 Sandia 1948-1950 is the operational arm of FBI-62HQ-Sr164 Cabell Memo (Feb 1949)", "hypothesis",
  label_ru="DOW-D017 Сандия 1948-1950 — оперативное плечо меморандума ФБР 62-HQ-Sr164 Cabell (фев. 1949)",
  description="The Sandia Base / 17th OSI District 1948-1950 compendium (DOW-D017) is the operational implementation of the FBI 62-HQ-Sr164 Cabell Memorandum #4 (February 1949). The two records form a response-pair in 1949 across two federal entry points: FBI custodianship of the Cabell Memo (form-side propulsion taxonomy that persisted 75 years into modern AARO MISREP fields) vs OSI custodianship of the Sandia operational record (technical impactment-sampling programme at Socorro under Lincoln LaPaz). Strongest single new R02→R01 structural pairing established by §14.1 of MASTER claims doc.",
  description_ru="Компендиум Базы Сандия / 17-го района OSI 1948-1950 (DOW-D017) — оперативная реализация меморандума ФБР 62-HQ-Sr164 Cabell #4 (февраль 1949). Две записи образуют пару реакции в 1949 через две федеральные точки входа: ФБР как хранитель меморандума Cabell (форменная сторона таксономии двигательных установок, сохраняющаяся 75 лет в современных полях MISREP AARO) vs OSI как хранитель оперативной Сандийской записи (техническая программа отбора проб ударов в Сокорро под Лапазом). Сильнейшее единичное новое R02→R01 структурное спаривание, установленное в §14.1 MASTER claims doc.",
  source="war-gov-pursue-archive/analysis/MASTER_pursue_claims.md#§14.1")

E("hyp-doe-categorical-exclusion-broken", "R02 is the first PURSUE release in which DOE breaks its categorical-exclusion posture", "hypothesis",
  label_ru="R02 — первый релиз PURSUE, в котором DOE снимает категорическое исключение",
  description="The U.S. Department of Energy has historically declined to release UFO/UAP-related material under categorical exclusions tied to nuclear-weapons-information control. R02 is the first PURSUE release in which DOE contributes material — three records (DOE-D001 Pantex, DOE-D002 Tuck, DOE-D003 Pajarito), all anchored in the New Mexico nuclear-weapons complex. This is a verifiable institutional posture change at the agency that controls the most sensitive UAP-adjacent corpus (Hanford, Oak Ridge, Sandia, LANL, NTS, Pantex). Documented in §12.4 of MASTER claims doc.",
  description_ru="DOE исторически отказывалось рассекречивать UFO/UAP-материалы по категорическим исключениям, привязанным к контролю ядерно-оружейной информации. R02 — первый релиз PURSUE с материалом DOE — три записи (DOE-D001 Pantex, DOE-D002 Так, DOE-D003 Pajarito), все привязанные к ядерно-оружейному комплексу Нью-Мексико. Проверяемое изменение институциональной позиции ведомства, контролирующего самый чувствительный UAP-смежный корпус (Hanford, Oak Ridge, Sandia, ЛАНЛ, NTS, Pantex). Задокументировано в §12.4 MASTER claims doc.",
  source="war-gov-pursue-archive/analysis/MASTER_pursue_claims.md#§12.4")

E("hyp-odni-fbi-photo-pairing", "ODNI-D001 USPER orange-orb 2025 is the explicit eyewitness narrative for R01 FBI Western US 2025 IR-photo corpus", "hypothesis",
  label_ru="ODNI-D001 USPER оранжевые сферы 2025 — явное свидетельское повествование для R01 ИК-фотокорпуса ФБР Западные США 2025",
  description="The ODNI R02 record explicitly PdfPairs in the war.gov CSV metadata with R01 FBI Photo A001-A008 + B001-B024 + USPER Statement (32 R01 records). This makes ODNI-D001 the eyewitness narrative for the R01 FBI Western US 2025 IR-photo cluster. Per §14.1 of MASTER claims doc: 'This is the single most consequential R01↔R02 cross-link.' Material implication: the R01 IR-photo corpus is no longer a stand-alone visual record; it now has a senior-USIC-officer narrative attached via PdfPair.",
  description_ru="Запись ODNI R02 явно PdfPairs в метаданных CSV war.gov с R01 FBI Photo A001-A008 + B001-B024 + USPER Statement (32 записи R01). Это делает ODNI-D001 свидетельским повествованием для R01 ИК-фотокластера ФБР Западные США 2025. Согласно §14.1 MASTER claims doc: «самая важная перекрёстная связь R01↔R02». Материальное следствие: R01 ИК-фотокорпус больше не является отдельной визуальной записью; теперь у него есть нарратив старшего сотрудника USIC, прикреплённый через PdfPair.",
  source="war-gov-pursue-archive/analysis/MASTER_pursue_claims.md#§14.1")

# Anchor for the Cabell Memo as a standalone event (not previously defined as event;
# only referenced inside src-fbi-62hq-master description). Required as the paired target.
E("ev-fbi-62hq-sr164-cabell-memo-1949", "FBI 62-HQ-Sr164 Cabell Memorandum #4 (Feb 1949)", "event",
  date="1949-02",
  label_ru="Меморандум ФБР 62-HQ-Sr164 Cabell #4 (фев. 1949)",
  description="Cabell Memorandum #4, FBI Case 62-HQ-83894 Serial 164, February 1949. The form-side propulsion-taxonomy standardisation document whose sub-categories (propeller/jet, rotor, oscillating airfoil/Katzmayr effect, visible exhaust) persisted 75 years into the modern AARO MISREP 'UAP Propulsion Means' fields (typically 'UNK'). Anchor for the hyp-pursue-cabell-form-stagnation hypothesis (R01) and now structurally paired with the R02 DOW-D017 Sandia Base 1948-1950 operational record.",
  description_ru="Меморандум Cabell #4, дело ФБР 62-HQ-83894 серийный 164, февраль 1949. Форменно-сторонний документ стандартизации таксономии двигательных установок, чьи подкатегории (винт/реактивный, ротор, колеблющийся профиль / эффект Katzmayr, видимый выхлоп) сохранялись 75 лет в современных полях «UAP Propulsion Means» MISREP AARO (обычно «UNK»). Якорь гипотезы hyp-pursue-cabell-form-stagnation (R01) и теперь структурно спарен с оперативной записью R02 DOW-D017 Базы Сандия 1948-1950.",
  source="war-gov-pursue-archive/analysis/per-document/DOW-UAP-D017_SANDIA-GREEN-FIREBALLS.md")

# ════════════════════════════════════════════════════════════════════
# EDGES
# ════════════════════════════════════════════════════════════════════

# ----- R02 PDF events → cluster (publishes / member-of) ---------------

C("ev-sary-shagan-cia-hum-1973", "cluster-pursue-release-02", "member-of", direction="directed")
C("ev-pantex-radar-incident", "cluster-pursue-release-02", "member-of", direction="directed")
C("ev-tuck-correspondence-1976", "cluster-pursue-release-02", "member-of", direction="directed")
C("ev-pajarito-astronomers-warren-1986", "cluster-pursue-release-02", "member-of", direction="directed")
C("ev-sandia-green-fireballs-1948-1950", "cluster-pursue-release-02", "member-of", direction="directed")
C("ev-usper-orange-orb-2025", "cluster-pursue-release-02", "member-of", direction="directed")

# Notable R02 video / audio events → cluster
C("ev-lake-huron-shootdown-2023", "cluster-pursue-release-02", "member-of", direction="directed")
C("ev-kazakhstan-pr072-2022", "cluster-pursue-release-02", "member-of", direction="directed")
C("ev-tyndall-uscg-2024", "cluster-pursue-release-02", "member-of", direction="directed")
C("ev-kabul-afsoc-2017", "cluster-pursue-release-02", "member-of", direction="directed")
C("ev-2021-04-12-cluster", "cluster-pursue-release-02", "member-of", direction="directed")
C("ev-aug-oct-2020-centcom-cluster", "cluster-pursue-release-02", "member-of", direction="directed")
C("ev-ma9-fireflies-1963", "cluster-pursue-release-02", "member-of", direction="directed")
C("ev-socorro-impactment-1949", "cluster-pursue-release-02", "member-of", direction="directed")

# ----- Agency contributors → cluster (publishes — first DOE/CIA/ODNI) -

C("inst-cia-pursue", "cluster-pursue-release-02", "publishes", direction="directed")
C("inst-doe-pursue", "cluster-pursue-release-02", "publishes", direction="directed")  # first DOE PURSUE contribution
C("inst-odni-pursue", "cluster-pursue-release-02", "publishes", direction="directed")

# R01 agencies that also contribute to R02 (DoW + NASA, via PR-series and audio)
C("inst-dow", "cluster-pursue-release-02", "publishes", direction="directed")
C("inst-nasa-pursue", "cluster-pursue-release-02", "publishes", direction="directed")

# AARO operational lead continues across R02
C("inst-aaro-pursue", "cluster-pursue-release-02", "operational-lead-of", direction="directed")

# ----- Cluster connects to parent project + to R01 cluster ------------

C("cluster-pursue-release-02", "pj-uap", "investigated-by (Track 11)", direction="directed")
C("cluster-pursue-release-02", "cluster-pursue-release-01", "supersedes (additive, no source-code overlap)", direction="directed")

# ----- Person ↔ event / institution membership ------------------------

C("person-lincoln-lapaz", "ev-sandia-green-fireballs-1948-1950", "member-of (consultant)", direction="directed")
C("person-lincoln-lapaz", "ev-socorro-impactment-1949", "member-of (driving hypothesis)", direction="directed")
C("person-james-tuck", "inst-lanl", "member-of", direction="directed")
C("person-james-tuck", "ev-tuck-correspondence-1976", "member-of (principal correspondent)", direction="directed")
C("person-john-warren", "inst-lanl", "member-of (AT-6 division)", direction="directed")
C("person-john-warren", "ev-pajarito-astronomers-warren-1986", "member-of (speaker)", direction="directed")

# Mercury / Apollo astronauts → mission events + NASA institution
C("person-gordon-cooper", "ev-ma9-fireflies-1963", "member-of (pilot)", direction="directed")
C("person-gordon-cooper", "inst-nasa-pursue", "member-of", direction="directed")
C("person-scott-carpenter", "inst-nasa-pursue", "member-of", direction="directed")
C("person-walter-schirra", "inst-nasa-pursue", "member-of", direction="directed")
C("person-virgil-grissom", "inst-nasa-pursue", "member-of", direction="directed")
C("person-charles-conrad", "inst-nasa-pursue", "member-of", direction="directed")
C("person-alan-bean", "inst-nasa-pursue", "member-of", direction="directed")
C("person-gene-cernan", "inst-nasa-pursue", "member-of", direction="directed")
C("person-harrison-schmitt", "inst-nasa-pursue", "member-of", direction="directed")

# Apollo 17 crew narrative cross-link to R01 VM6 active investigation
C("person-gene-cernan", "ev-vm6-apollo17", "related-to (Apollo 17 crew)", direction="directed")
C("person-harrison-schmitt", "ev-vm6-apollo17", "related-to (Apollo 17 crew)", direction="directed")

# ----- Institutional hierarchy: NM nuclear-weapons complex ------------

C("inst-pajarito-astronomers", "inst-lanl", "member-of (embedded amateur club)", direction="directed")
C("inst-lanl", "inst-doe-pursue", "member-of (DOE national laboratory)", direction="directed")
C("inst-sandia", "inst-doe-pursue", "member-of (DOE national laboratory)", direction="directed")
C("inst-pantex", "inst-doe-pursue", "member-of (operated by CNS LLC for DOE-NNSA)", direction="directed")
C("inst-17th-osi", "inst-dow", "member-of (AFOSI district under DoW lineage)", direction="directed")
C("inst-uscg", "inst-dow", "related-to (R02 distribution under DOW banner)", direction="directed")

# ----- Event ↔ institutional context ---------------------------------

C("ev-pantex-radar-incident", "inst-pantex", "related-to (incident site)", direction="directed")
C("ev-pantex-radar-incident", "inst-sandia", "related-to (image-enhancement provider)", direction="directed")
C("ev-sandia-green-fireballs-1948-1950", "inst-sandia", "related-to (geographic locus)", direction="directed")
C("ev-sandia-green-fireballs-1948-1950", "inst-17th-osi", "related-to (operational custodian)", direction="directed")
C("ev-pajarito-astronomers-warren-1986", "inst-pajarito-astronomers", "related-to (host)", direction="directed")
C("ev-pajarito-astronomers-warren-1986", "inst-lanl", "related-to (institutional locus)", direction="directed")
C("ev-tuck-correspondence-1976", "inst-lanl", "related-to (Tuck affiliation)", direction="directed")
C("ev-sary-shagan-cia-hum-1973", "inst-cia-pursue", "archived-by", direction="directed")
C("ev-pantex-radar-incident", "inst-doe-pursue", "archived-by", direction="directed")
C("ev-tuck-correspondence-1976", "inst-doe-pursue", "archived-by", direction="directed")
C("ev-pajarito-astronomers-warren-1986", "inst-doe-pursue", "archived-by", direction="directed")
C("ev-sandia-green-fireballs-1948-1950", "inst-dow", "archived-by", direction="directed")
C("ev-usper-orange-orb-2025", "inst-odni-pursue", "archived-by", direction="directed")
C("ev-lake-huron-shootdown-2023", "inst-norad", "related-to (operational command authority)", direction="directed")
C("ev-tyndall-uscg-2024", "inst-uscg", "related-to (USCG C-144 platform)", direction="directed")

# ----- R02 ↔ R01 internal cross-links (paired-with — primary edges) ---

# DOW-D017 Sandia 1948-1950 ↔ FBI 62-HQ-Sr164 Cabell Memo Feb 1949 (operational pair)
C("ev-sandia-green-fireballs-1948-1950", "ev-fbi-62hq-sr164-cabell-memo-1949", "paired-with (operational implementation)", direction="undirected")
C("ev-fbi-62hq-sr164-cabell-memo-1949", "src-fbi-62hq-master", "member-of (Serial 164 of master file)", direction="directed")

# ODNI USPER orange-orb 2025 ↔ R01 FBI Western US IR-photo corpus (PdfPair)
# (R01 IR-photo corpus is not yet a standalone node; pair to FBI institution + FBI 62-HQ source)
C("ev-usper-orange-orb-2025", "inst-fbi", "paired-with (PdfPair: FBI Photo A001-A008 + B001-B024 + USPER Statement)", direction="undirected")
C("ev-usper-orange-orb-2025", "src-fbi-62hq-master", "paired-with (R01 FBI Western US IR-photo corpus)", direction="undirected")

# Lake Huron 2023 + Tyndall 2024 continue the modern Western-US-2023 / Atlantic-coast active-investigation thread
C("ev-lake-huron-shootdown-2023", "ev-western-us-2023", "related-to (federal LE / military active-investigation cluster)", direction="undirected")

# ----- Cross-archive bridges (sibling-archive navigation, no claim imports) -

# Kazakhstan PR072 2022 → chernobrov-archive Soviet-territory corpus
C("ev-kazakhstan-pr072-2022", "p-chernobrov", "related-to (Soviet-territory cross-archive bridge)", direction="directed")

# Sary Shagan CIA HUM 1973 → chernobrov-archive Soviet-side parallel
C("ev-sary-shagan-cia-hum-1973", "p-chernobrov", "related-to (US-side intel parallel to Chernobrov USSR-side)", direction="directed")

# DOE-D002 Tuck 1976 → dubna / element-115 conceptual genealogy (atomic-bomb sim + atmospheric vortices)
C("ev-tuck-correspondence-1976", "phen-mc115", "related-to (atomic-physics conceptual genealogy)", direction="directed")

# DOE-D003 Pajarito 1986 + DOE-D002 Tuck 1976 → Lazar narrative (LANL during Lazar-tenure decade)
C("ev-pajarito-astronomers-warren-1986", "p-lazar", "related-to (institutional LANL UAP engagement during Lazar-tenure decade)", direction="undirected")
C("ev-tuck-correspondence-1976", "p-lazar", "related-to (LANL UAP-adjacent engagement decade earlier than Lazar S-4 claim)", direction="undirected")

# Pantex operator CNS LLC → Track 7 corporate cluster (EG&G → Amentum lineage)
C("inst-pantex", "cluster-track7-corporate", "related-to (CNS LLC corporate-overlay target)", direction="directed")

# 17th OSI District → OSINT methodology (documentary ancestor)
C("inst-17th-osi", "meth-validation-pipeline", "related-to (documentary methodological ancestor)", direction="directed")

# ----- Hypothesis / finding nodes → cluster + anchors -----------------

C("hyp-cabell-sandia-1949-pair", "cluster-pursue-release-02", "synthesizes-from", direction="directed")
C("hyp-doe-categorical-exclusion-broken", "cluster-pursue-release-02", "synthesizes-from", direction="directed")
C("hyp-odni-fbi-photo-pairing", "cluster-pursue-release-02", "synthesizes-from", direction="directed")

# Hypothesis anchors
C("ev-sandia-green-fireballs-1948-1950", "hyp-cabell-sandia-1949-pair", "anchors", direction="directed")
C("ev-fbi-62hq-sr164-cabell-memo-1949", "hyp-cabell-sandia-1949-pair", "anchors", direction="directed")
C("hyp-cabell-sandia-1949-pair", "hyp-pursue-cabell-form-stagnation", "supports (R02 extends the 75-year stagnation thesis)", direction="directed")

C("ev-pantex-radar-incident", "hyp-doe-categorical-exclusion-broken", "anchors", direction="directed")
C("ev-tuck-correspondence-1976", "hyp-doe-categorical-exclusion-broken", "anchors", direction="directed")
C("ev-pajarito-astronomers-warren-1986", "hyp-doe-categorical-exclusion-broken", "anchors", direction="directed")
C("inst-doe-pursue", "hyp-doe-categorical-exclusion-broken", "anchors (subject institution)", direction="directed")

C("ev-usper-orange-orb-2025", "hyp-odni-fbi-photo-pairing", "anchors", direction="directed")
C("inst-odni-pursue", "hyp-odni-fbi-photo-pairing", "anchors (subject institution)", direction="directed")

# ----- Active investigations linked to parent project ------------------

C("ev-usper-orange-orb-2025", "pj-uap", "active-investigation (PURSUE R02)", direction="directed")
C("ev-pantex-radar-incident", "pj-uap", "active-investigation (PURSUE R02)", direction="directed")
C("ev-sandia-green-fireballs-1948-1950", "pj-uap", "active-investigation (PURSUE R02)", direction="directed")
