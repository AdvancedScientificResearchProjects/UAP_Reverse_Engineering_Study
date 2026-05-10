# ════════════════════════════════════════════════════════════════════
# AGENT H — PURSUE Declassification archive (Track 11)
# Sources: war-gov-pursue-archive/ (PURSUE Release 01, war.gov 2026-05-08)
# Authored 2026-05-09 in support of war-gov-pursue-archive Stage 13
# ════════════════════════════════════════════════════════════════════

# ----- CLUSTER ---------------------------------------------------------

E("cluster-pursue-release-01", "PURSUE Release 01 (Track 11)", "cluster",
  label_ru="PURSUE Релиз 01 (Трек 11)",
  description="The 2026-05-08 Department of War (DoW) PURSUE Release 01 — 161 declassified UAP records from DoW, FBI, NASA, and the Department of State, made public via war.gov/UFO under the Presidential Unsealing and Reporting System for UAP Encounters (PURSUE). Spans 1944 foo-fighters → 2025 FBI Western US IR cluster. Archive posture is release-confirmation rather than single-witness testimony or institutional science: 75 percent CORROBORATED-at-observation-level, 100 percent record coverage achieved across 158 per-document analytical cards + 7 topical syntheses + MASTER claims document.",
  description_ru="PURSUE Релиз 01 от Министерства войны США (DoW) от 8 мая 2026 — 161 рассекреченная запись по НАЯ от DoW, ФБР, NASA и Госдепартамента, опубликованная на war.gov/UFO в рамках программы Presidential Unsealing and Reporting System for UAP Encounters (PURSUE). Охватывает foo-fighters 1944 → ИК-кластер ФБР Western US 2025. Архивная позиция — подтверждение через релиз, а не свидетельство одного человека или институциональная наука: 75% CORROBORATED на уровне наблюдения, 100% покрытие записей по 158 аналитическим карточкам + 7 тематическим синтезам + MASTER-документу заявлений.",
  source="war-gov-pursue-archive/README.md")

# ----- INSTITUTIONS ----------------------------------------------------

E("inst-dow", "Department of War (DoW, formerly DoD)", "institution",
  label_ru="Министерство войны США (DoW, бывш. DoD)",
  description="US Department of War — publisher of the PURSUE Release 01. AARO sits inside DoW. Issues mission reports (MISREP D-series) and unresolved UAP reports (PR-series videos) under structured-form taxonomies inherited from the 1949 Cabell Memorandum #4.",
  description_ru="Министерство войны США — публикатор PURSUE Релиз 01. AARO находится в DoW. Издаёт mission reports (MISREP, серия D) и нерешённые UAP-отчёты (серия PR, видео) по структурированным форменным таксономиям, унаследованным от Cabell Memorandum #4 1949 г.",
  source="war-gov-pursue-archive/catalog/source_codes.md")

E("inst-fbi", "Federal Bureau of Investigation (FBI)", "institution",
  label_ru="Федеральное бюро расследований (ФБР)",
  description="FBI — contributor of FBI Case 62-HQ-83894 master file (1947-1976), Western US IR-photo cluster (FBI-IR-A/B series 2025), September 2023 bronze ellipsoid case (FBI ELLIPSE Sr3/4/5 + AI-composite), USPER-302 senior-official late-2025 encounter, and pre-1956 historical FBI 100-DE legacy material.",
  description_ru="ФБР — поставщик мастер-файла дела 62-HQ-83894 (1947-1976), ИК-кластера Western US (серии FBI-IR-A/B, 2025), дела бронзового эллипсоида сентября 2023 (FBI ELLIPSE Sr3/4/5 + ИИ-композит), USPER-302 — встреча высокопоставленного чиновника конца 2025, и довоенного исторического материала FBI 100-DE.",
  source="war-gov-pursue-archive/catalog/typology.md")

E("inst-nasa-pursue", "NASA (PURSUE contributor)", "institution",
  label_ru="NASA (контрибьютор PURSUE)",
  description="NASA contribution to PURSUE Release 01: 14 records spanning Gemini 7 (1965), Apollo 11/12/17 (1969-1972), and Skylab (1973-1974) crew transcripts, debriefings, and imagery. Includes the VM6 active-investigation Apollo 17 photograph (DoW 'opened a case' and 'obtained the original film'). Released under MDR; not the agency's first UAP-related release but the first integrated into a federal-wide tranche.",
  description_ru="Вклад NASA в PURSUE Релиз 01: 14 записей по Gemini 7 (1965), Apollo 11/12/17 (1969-1972) и Skylab (1973-1974) — транскрипты экипажа, debriefings и снимки. Включает фотографию активного расследования VM6 с Apollo 17 (DoW «открыло дело» и «получило оригинальную плёнку»). Рассекречено через MDR; не первый UAP-релиз агентства, но первый, интегрированный в федеральную траншу.",
  source="war-gov-pursue-archive/analysis/topical/era-1965-1974-nasa-spaceflight.md")

E("inst-state-pursue", "Department of State (PURSUE contributor)", "institution",
  label_ru="Государственный департамент США (контрибьютор PURSUE)",
  description="Department of State contribution to PURSUE Release 01: 7 diplomatic cables 1952-2004 (1952 SECRET memo, 1963 EOP/NASC Hunter 'Space Alien Race Question', PNG 1985 Wewak overflights, KAZ 1994 Tajik Air B747SP, TBI 2001, MEX 2003, TKM 2004). 4 of 7 PDFs missing from the release tranche (gap-cards exist).",
  description_ru="Вклад Госдепартамента в PURSUE Релиз 01: 7 дипломатических кабелей 1952-2004 (секретная памятка 1952, Hunter EOP/NASC 1963 «Space Alien Race Question», полёты над Wewak в PNG 1985, Tajik Air B747SP в KAZ 1994, TBI 2001, MEX 2003, TKM 2004). 4 из 7 PDF отсутствуют в транше релиза (карточки-пробелы существуют).",
  source="war-gov-pursue-archive/analysis/topical/modality-state-cables-1952-2004.md")

E("inst-aaro-pursue", "AARO (All-domain Anomaly Resolution Office)", "institution",
  label_ru="AARO (Офис разрешения аномалий всех доменов)",
  description="AARO — operational lead for UAP triage inside DoW. PURSUE Release 01 metadata uses AARO descriptions for video and image records. Documented metadata-inconsistency pattern (PR28 mislabel of D7 vs actual-D25 match; PR29 mislabel of D8 vs actual-D27 match) is a structural cataloging defect, not noise. Modern MISREP forms inherit Cabell-1949 propulsion-taxonomy.",
  description_ru="AARO — оперативный руководитель триажа НАЯ в DoW. Метаданные PURSUE Релиз 01 используют описания AARO для видео и изображений. Задокументированный паттерн несогласованности метаданных (PR28 размечен как D7 вместо фактического D25; PR29 размечен как D8 вместо фактического D27) — структурный каталогизационный дефект, а не шум. Современные формы MISREP наследуют таксономию двигательных установок Cabell 1949.",
  source="war-gov-pursue-archive/analysis/MASTER_pursue_claims.md")

# ----- SOURCES ---------------------------------------------------------

E("src-pursue-rel-01", "PURSUE Release 01 portal (war.gov/UFO)", "source",
  label_ru="Портал PURSUE Релиз 01 (war.gov/UFO)",
  description="Public-source URL for the 161-record PURSUE Release 01 tranche, published 2026-05-08 at https://www.war.gov/UFO/. Aggregates PDFs, mp4 videos, and jpg images across DoW, FBI, NASA, and State agencies into a single rolling-release portal.",
  description_ru="Публично-источниковый URL для транши PURSUE Релиз 01 из 161 записи, опубликованной 8 мая 2026 на https://www.war.gov/UFO/. Агрегирует PDF, mp4-видео и jpg-изображения от DoW, ФБР, NASA и Госдепа в единый портал rolling-release.",
  source="war-gov-pursue-archive/manifest.json")

E("src-fbi-62hq-master", "FBI Case 62-HQ-83894 master file", "source",
  label_ru="Мастер-файл дела ФБР 62-HQ-83894",
  description="FBI Headquarters Case 62-HQ-83894 — the master FBI UAP case file, with sections (S1-S10) and serials (Sr1-Sr500+) spanning 1947-1976. Includes the 1949 Cabell Memorandum #4 (Sr164) which standardized the propulsion-taxonomy form persisting in modern MISREP fields, the 1957 Pinar del Rio Cuba case (S09), the 1964 Socorro physical-trace anchor (Sr438), and the 1949-1950 Oak Ridge cluster (S05).",
  description_ru="Дело ФБР штаб-квартиры 62-HQ-83894 — мастер-файл UAP ФБР, с секциями (S1-S10) и серийными номерами (Sr1-Sr500+) с 1947 по 1976 г. Включает Cabell Memorandum #4 1949 г. (Sr164), стандартизировавший форму таксономии двигательных установок, сохраняющуюся в современных полях MISREP, дело Pinar del Rio Cuba 1957 г. (S09), якорь физических следов в Сокорро 1964 г. (Sr438) и кластер Oak Ridge 1949-1950 (S05).",
  source="war-gov-pursue-archive/analysis/topical/era-1944-1968-historical.md")

E("src-cometa-1999", "COMETA 1999 report (only civilian/foreign source)", "source",
  label_ru="Отчёт COMETA 1999 (единственный гражданский/иностранный источник)",
  description="French civilian COMETA report ('Les OVNI et la Defense'), published 1999 by an independent committee of former French government and military officials. The only civilian and only foreign-language record in PURSUE Release 01. Endorses extraterrestrial hypothesis as 'the best scientific hypothesis' and discusses MHD propulsion mechanisms; treats Roswell-as-disinformation and Mogul-balloon-as-cover in Appendix 5.",
  description_ru="Французский гражданский отчёт COMETA («Les OVNI et la Defense»), опубликованный в 1999 г. независимым комитетом бывших французских правительственных и военных чиновников. Единственная гражданская и единственная иноязычная запись в PURSUE Релиз 01. Поддерживает внеземную гипотезу как «лучшую научную гипотезу» и обсуждает механизмы МГД-двигателя; в Приложении 5 трактует Розуэлл как дезинформацию и баллон Mogul как прикрытие.",
  source="war-gov-pursue-archive/analysis/per-document/COMETA-1999.md")

E("src-dos-1963-eop-nasa", "1963 Hunter EOP/NASC 'Space Alien Race Question' memo", "source",
  label_ru="Памятка Hunter EOP/NASC 1963 «Space Alien Race Question»",
  description="Maxwell W. Hunter II (NASC Professional Staff) memo to State Department's Office of International Scientific Affairs, 18 July 1963. The earliest unambiguously-EOP-level US Government record discussing first-contact policy in this corpus. Contains the famous concession 'no one of consequence is going to take this rubbish seriously unless it happens. At that point, our policy will be determined in the traditional manner of grand panic.'",
  description_ru="Памятка Maxwell W. Hunter II (профессиональный персонал NASC) Бюро международных научных дел Госдепартамента, 18 июля 1963. Самая ранняя однозначно EOP-уровневая запись правительства США, обсуждающая политику первого контакта в этом корпусе. Содержит знаменитое признание «никто значительный не будет воспринимать эту чепуху всерьёз, пока это не произойдёт. На этой точке наша политика будет определена в традиционной манере великой паники».",
  source="war-gov-pursue-archive/analysis/per-document/DOS-1963-EOP-NASA.md")

E("src-dow-1948-nl-intel", "1948 USAFE TT 1524 (Holland intercept + Swedish lake-crash)", "source",
  label_ru="USAFE TT 1524 1948 (голландский перехват + катастрофа на шведском озере)",
  description="USAFE Top Secret transmittal TT 1524 to General Cabell, November 1948. Preserves verbatim the Swedish Intelligence Service working assessment that the objects 'originate from some previously [unknown] or unidentified technology, possibly outside the earth' — a first-tier ETH text routed at General-Cabell level fifteen years before the Hunter 1963 memo. Closes by addressing Cabell directly: 'we are inclined not to discredit entirely this somewhat spectacular theory… What are your reactions?'",
  description_ru="USAFE Top Secret transmittal TT 1524 генералу Cabell, ноябрь 1948. Дословно сохраняет рабочую оценку шведской разведслужбы: объекты «происходят от некоторой ранее [неизвестной] или неопознанной технологии, возможно, вне земли» — текст первого порядка по гипотезе ETH, направленный на уровне генерала Cabell за пятнадцать лет до памятки Hunter 1963 г. Заканчивается прямым обращением к Cabell: «мы склонны не дискредитировать полностью эту несколько впечатляющую теорию… Какова Ваша реакция?»",
  source="war-gov-pursue-archive/analysis/per-document/DOW-1948-NETHERLANDS-INTEL.md")

# ----- EVENTS / KEY CASES ----------------------------------------------

E("ev-vm6-apollo17", "VM6 Apollo 17 active-investigation photograph (1972)", "event",
  label_ru="Фотография активного расследования VM6 с Apollo 17 (1972)",
  description="Apollo 17 photograph cataloged by DoW under active-investigation status: 'opened a case' and 'obtained the original film'. The only NASA record in PURSUE Release 01 under explicit active investigation. Apollo 17 verbal record (NASA-D2 voice, NASA-D5 science debrief, NASA-D6 technical debrief) contains zero contemporaneous reference to a triangular formation, raising open question of whether VM6 documents real-time non-reporting, off-tape voice in unreleased curation, or an image-side artifact.",
  description_ru="Фотография с Apollo 17, каталогизированная DoW под статусом активного расследования: «открыло дело» и «получило оригинальную плёнку». Единственная запись NASA в PURSUE Релиз 01 под явным активным расследованием. Голосовой и debriefing-материалы Apollo 17 (NASA-D2 голос, NASA-D5 научный debrief, NASA-D6 технический debrief) не содержат современных упоминаний треугольной формации, что поднимает вопрос: документирует ли VM6 нерепортинг в реальном времени, off-tape голос в неопубликованной кураторской выборке или артефакт изображения.",
  source="war-gov-pursue-archive/analysis/per-document/NASA-VM6.md")

E("ev-western-us-2023", "DOW-WESTERN-US-2023 federal-LE pursuit case", "event",
  label_ru="DOW-WESTERN-US-2023 — дело преследования с участием федеральных правоохранительных органов",
  description="2023 Western US event flagged by AARO as 'among the most compelling' cases in the PURSUE corpus. Federal law-enforcement-witness pursuit of a stationary fiery orb at AARO-measured ~1050 m altitude, ~12-18 m diameter (measurement methodology not published). Sits inside the broader Western-US 2023-2025 cluster that also includes the September 2023 bronze ellipsoid case (FBI ELLIPSE Sr3/4/5 + AI composite) and the 2025 FBI Western-US IR-photo cluster + USPER-302 senior-official 302.",
  description_ru="Событие 2023 в Western US, помеченное AARO как «один из наиболее compelling» в корпусе PURSUE. Преследование стационарного огненного шара свидетелем-сотрудником федерального правоохранительного органа на высоте ~1050 м (по измерению AARO), диаметр ~12-18 м (методология измерения не опубликована). Входит в более широкий Western-US кластер 2023-2025, включающий также дело бронзового эллипсоида сентября 2023 (FBI ELLIPSE Sr3/4/5 + ИИ-композит) и ИК-кластер ФБР Western US 2025 + 302 высокопоставленного чиновника USPER-302.",
  source="war-gov-pursue-archive/analysis/per-document/DOW-WESTERN-US-2023.md")

E("ev-sept-2023-ellipsoid", "September 2023 bronze ellipsoid case (FBI ELLIPSE)", "event",
  label_ru="Дело бронзового эллипсоида сентября 2023 (FBI ELLIPSE)",
  description="September 2023 case at an undisclosed US test site: three contractor witnesses (Sr3 lead, Sr4 corroborating, Sr5 corroborating) observed a metallic-bronze ellipsoid 'almost hovering, slowly moving from east to west' at Blackhawk-2x-3x size estimate (FBI Lab composite resolves this to 130-195 ft range). Sr4 and Sr5 page 1 systematically absent from release; only Sr3 has full 2-page narrative. AI-generated FBI Lab composite distinguishes 'materialized out of a bright light' entry phenomenology that does not appear in Sr3 or Sr4 — likely originates with Sr5 (whose page 1 is missing).",
  description_ru="Дело сентября 2023 на нераскрытом тестовом полигоне США: три свидетеля-подрядчика (Sr3 ведущий, Sr4 подкрепляющий, Sr5 подкрепляющий) наблюдали металлически-бронзовый эллипсоид, «почти зависший, медленно движущийся с востока на запад» с размером в 2-3 Blackhawk (композит FBI Lab сводит к диапазону 130-195 футов). Страница 1 Sr4 и Sr5 систематически отсутствует в релизе; только Sr3 имеет полное 2-страничное повествование. ИИ-сгенерированный композит FBI Lab выделяет феноменологию входа «материализовался из яркого света», которая не появляется ни у Sr3, ни у Sr4 — вероятно, исходит от Sr5 (чья страница 1 отсутствует).",
  source="war-gov-pursue-archive/analysis/per-document/FBI-ELLIPSE-Sr3.md")

# ----- HYPOTHESIS NODES ------------------------------------------------

E("hyp-pursue-cabell-form-stagnation", "75-year propulsion-taxonomy stagnation (Cabell 1949 → AARO 2026)", "hypothesis",
  label_ru="75-летняя стагнация таксономии двигательных установок (Cabell 1949 → AARO 2026)",
  description="The 1949 Cabell Memorandum #4 propulsion sub-categories (propeller/jet, rotor, oscillating airfoil/Katzmayr effect, visible exhaust) inherited by modern AARO MISREP 'UAP Propulsion Means' fields (typically 'UNK'). Form-side infrastructure has not evolved to record plasma, gravity manipulation, MHD, 'no visible mechanism', or zero-inertia hover. Combined with the 1948 USAFE TT 1524 ETH-question text, this implies the formal infrastructure to record an ETH-positive answer existed at general-officer level in 1948-1949 and was structurally bounded the same way for 75 years.",
  description_ru="Подкатегории двигательных установок Cabell Memorandum #4 1949 г. (винт/реактивный, ротор, колеблющийся профиль/эффект Katzmayr, видимый выхлоп), унаследованные современными полями «UAP Propulsion Means» в MISREP AARO (обычно «UNK»). Форменная инфраструктура не эволюционировала, чтобы записывать плазму, манипуляцию гравитацией, МГД, «отсутствие видимого механизма» или зависание без инерции. В сочетании с текстом USAFE TT 1524 1948 г. о вопросе ETH это подразумевает, что формальная инфраструктура для записи ETH-позитивного ответа существовала на уровне генерала уже в 1948-1949 гг. и была структурно ограничена так же на протяжении 75 лет.",
  source="war-gov-pursue-archive/analysis/MASTER_pursue_claims.md")

# ----- CLUSTER MEMBERSHIP ---------------------------------------------

C("inst-dow", "cluster-pursue-release-01", "publishes", direction="directed")
C("inst-fbi", "cluster-pursue-release-01", "member-of", direction="directed")
C("inst-nasa-pursue", "cluster-pursue-release-01", "member-of", direction="directed")
C("inst-state-pursue", "cluster-pursue-release-01", "member-of", direction="directed")
C("inst-aaro-pursue", "cluster-pursue-release-01", "operational-lead-of", direction="directed")

C("src-pursue-rel-01", "cluster-pursue-release-01", "member-of", direction="directed")
C("src-fbi-62hq-master", "cluster-pursue-release-01", "member-of", direction="directed")
C("src-cometa-1999", "cluster-pursue-release-01", "member-of", direction="directed")
C("src-dos-1963-eop-nasa", "cluster-pursue-release-01", "member-of", direction="directed")
C("src-dow-1948-nl-intel", "cluster-pursue-release-01", "member-of", direction="directed")

C("ev-vm6-apollo17", "cluster-pursue-release-01", "member-of", direction="directed")
C("ev-western-us-2023", "cluster-pursue-release-01", "member-of", direction="directed")
C("ev-sept-2023-ellipsoid", "cluster-pursue-release-01", "member-of", direction="directed")

C("hyp-pursue-cabell-form-stagnation", "cluster-pursue-release-01", "synthesizes-from", direction="directed")

# ----- INSTITUTIONAL EDGES --------------------------------------------

C("inst-fbi", "src-fbi-62hq-master", "owns", direction="directed")
C("inst-nasa-pursue", "ev-vm6-apollo17", "originated", direction="directed")
C("inst-fbi", "ev-sept-2023-ellipsoid", "investigates", direction="directed")
C("inst-dow", "ev-western-us-2023", "investigates", direction="directed")
C("inst-state-pursue", "src-dos-1963-eop-nasa", "owns", direction="directed")
C("inst-dow", "src-dow-1948-nl-intel", "owns", direction="directed")
C("inst-dow", "src-pursue-rel-01", "publishes", direction="directed")

C("src-fbi-62hq-master", "hyp-pursue-cabell-form-stagnation", "anchors", direction="directed")
C("src-dow-1948-nl-intel", "hyp-pursue-cabell-form-stagnation", "anchors", direction="directed")

# ----- CROSS-ARCHIVE BRIDGES (navigational only — no claim imports) ---

C("cluster-pursue-release-01", "pj-uap", "investigated-by (Track 11)", direction="directed")

# Theme 1 (Element 115 / Moscovium) — propulsion thread shared with Lazar/Dubna
C("src-fbi-62hq-master", "phen-mc115", "form-side context for", direction="directed")
C("src-cometa-1999", "phen-mc115", "MHD propulsion topic shared with", direction="directed")

# Theme 3 (Soviet aerospace lineage) — diplomatic-cable thread shared with Chernobrov/Dubna
C("src-pursue-rel-01", "p-chernobrov", "Cold-War-era topical adjacency", direction="directed")

# Active investigations linked to project parent (UAP repo)
C("ev-vm6-apollo17", "pj-uap", "active-investigation (PURSUE)", direction="directed")
C("ev-western-us-2023", "pj-uap", "active-investigation (PURSUE)", direction="directed")
C("ev-sept-2023-ellipsoid", "pj-uap", "active-investigation (PURSUE)", direction="directed")
