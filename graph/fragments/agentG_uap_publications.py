# ════════════════════════════════════════════════════════════════════
# AGENT G — Track 9 UAP scientific publications corpus
# Sources: uap-scientific-publications/
# Authored 2026-04-30 Banchenko corporate working session
# ════════════════════════════════════════════════════════════════════

# ----- CLUSTER ---------------------------------------------------------

E("cluster-uap-publications", "UAP scientific publications corpus (Track 9)", "cluster",
  label_ru="Корпус научных публикаций по UAP (Трек 9)",
  description="Literature catalog consolidating public-source scientific publications addressing the UAP / UFO domain — peer-reviewed academic papers, government reports, observation-program technical outputs, and historically-significant grey literature. Does NOT validate the cataloged claims; consolidates them so the broader research can reference a stable provenance register.",
  description_ru="Каталог литературы, консолидирующий публично-источниковые научные публикации, обращающиеся к UAP / UFO-домену — рецензируемые академические работы, правительственные отчёты, технические выходы программ наблюдений, исторически значимая «серая литература». НЕ валидирует каталогизированные утверждения; консолидирует их так, чтобы более широкое исследование могло ссылаться на стабильный регистр провенанса.",
  source="uap-scientific-publications/README.md")

# ----- INSTITUTIONS / RESEARCH SURFACES -------------------------------

E("inst-galileo-project", "Harvard Galileo Project (founded 2021)", "institution",
  label_ru="Galileo Project (Гарвард, основан 2021)",
  description="Multi-modal UAP observation-program at Harvard Faculty of Arts and Sciences led by Avi Loeb, founded 2021. Designs and operates observatory hardware combining optical, infrared, radar, and acoustic sensors. Anchor publications hosted on galileo.fas.harvard.edu and arXiv.",
  description_ru="Программа мультимодального наблюдения UAP в Гарвардском факультете искусств и наук, возглавляемая Авраамом Лёбом, основана в 2021 г. Проектирует и эксплуатирует обсерваторное оборудование, объединяющее оптические, инфракрасные, радарные и акустические сенсоры. Опорные публикации размещены на galileo.fas.harvard.edu и arXiv.",
  source="uap-scientific-publications/sources/galileo-project-papers.md")

E("inst-hessdalen-project", "Hessdalen Project (Norway, ongoing 1980s+)", "institution",
  label_ru="Hessdalen Project (Норвегия, с 1980-х гг.)",
  description="Long-running automated ground-station monitoring of recurring atmospheric light phenomena in the Hessdalen valley, Norway. Established collaboration of Østfold University College and Italian / international researchers (Strand, Teodorani, Hauge). Peer-reviewed publications in Journal of Scientific Exploration, Radio Science.",
  description_ru="Долгосрочный мониторинг автоматизированной наземной станцией повторяющихся атмосферных световых явлений в долине Hessdalen, Норвегия. Устоявшееся сотрудничество Østfold University College и итальянских / международных исследователей (Strand, Teodorani, Hauge). Рецензируемые публикации в Journal of Scientific Exploration, Radio Science.",
  source="uap-scientific-publications/sources/hessdalen-papers.md")

E("inst-aaro", "DoD All-domain Anomaly Resolution Office (AARO)", "institution",
  label_ru="Управление DoD по разрешению аномалий во всех доменах (AARO)",
  description="DoD office established 2022 to coordinate UAP collection / analysis / resolution across the US defense and intelligence communities. Public reports include the Historical Record Report Vol. I (March 2024).",
  description_ru="Управление Министерства обороны США, учреждённое в 2022 г. для координации сбора / анализа / разрешения UAP в оборонном и разведывательном сообществах США. Публичные отчёты включают Historical Record Report Vol. I (март 2024).",
  source="uap-scientific-publications/sources/aaro-public-reports.md")

E("inst-odni", "Office of the Director of National Intelligence (ODNI)", "institution",
  label_ru="Офис директора национальной разведки (ODNI)",
  description="US Intelligence Community statutory body authoring annual UAP reports per FY2021 Intelligence Authorization Act. Co-publishes annual UAP reports with DoD / AARO since 2021.",
  description_ru="Установленный законом орган разведывательного сообщества США, готовящий ежегодные отчёты по UAP согласно Intelligence Authorization Act FY2021. Со-публикует ежегодные отчёты по UAP с DoD / AARO с 2021 г.",
  source="uap-scientific-publications/sources/dni-uap-reports-2021-2024.md")

E("inst-nasa-uap-team", "NASA UAP Independent Study Team (2022-2023)", "institution",
  label_ru="Независимая исследовательская группа NASA по UAP (2022-2023)",
  description="16-member independent study team chaired by David Spergel, commissioned by NASA in 2022; final report published September 2023. Hosted on nasa.gov.",
  description_ru="Независимая исследовательская группа из 16 человек под председательством Дэвида Шпергеля, заказана NASA в 2022 г.; окончательный отчёт опубликован в сентябре 2023 г. Размещён на nasa.gov.",
  source="uap-scientific-publications/sources/nasa-uap-study-2023.md")

E("inst-scu", "Scientific Coalition for UAP Studies (SCU)", "institution",
  label_ru="Scientific Coalition for UAP Studies (SCU)",
  description="Non-profit research organization (US) publishing peer-reviewed and society-published UAP research. Authors associated with the coalition include Robert Powell, Kevin Knuth, Travis Taylor, Garry Nolan, Massimo Teodorani.",
  description_ru="Некоммерческая исследовательская организация (США), публикующая рецензируемые и обществоиздаваемые исследования по UAP. Авторы, связанные с коалицией, включают Robert Powell, Kevin Knuth, Travis Taylor, Garry Nolan, Massimo Teodorani.",
  source="uap-scientific-publications/sources/scu-uap-papers-collection.md")

# ----- PERSONS (published authors of public papers) -------------------

E("p-loeb-a", "Avi Loeb", "person · external",
  label_ru="Авраам Лёб",
  description="Theoretical physicist, Frank B. Baird Jr. Professor of Science at Harvard. Founder and head of the Galileo Project (2021+). Public-figure author of multiple peer-reviewed papers on the project's anchor work.",
  description_ru="Физик-теоретик, профессор Гарвардского университета (кафедра Frank B. Baird Jr.). Основатель и руководитель Galileo Project (2021+). Публичный автор нескольких рецензируемых работ по опорной работе проекта.",
  source="uap-scientific-publications/sources/galileo-project-papers.md")

E("p-pasulka-dw", "D.W. Pasulka", "person · external",
  label_ru="D.W. Pasulka",
  description="Professor of Religious Studies, UNC Wilmington. Author of American Cosmic (Oxford UP 2019) and Encounters (St. Martin's 2023), peer-reviewed and academic-press monographs on UAP / contact narratives in religious-studies framing.",
  description_ru="Профессор религиоведения в UNC Wilmington. Автор American Cosmic (Oxford UP 2019) и Encounters (St. Martin's 2023), рецензируемых академических монографий по UAP / нарративам контакта в рамке религиоведения.",
  source="uap-scientific-publications/sources/pasulka-american-cosmic.md")

E("p-eghigian-g", "Greg Eghigian", "person · external",
  label_ru="Грег Эгигян",
  description="Professor of History and Bioethics at Penn State University. Author of After the Flying Saucers Came: A Global History of the UFO Phenomenon (Oxford UP 2024) — peer-reviewed academic monograph.",
  description_ru="Профессор истории и биоэтики в Penn State University. Автор After the Flying Saucers Came: A Global History of the UFO Phenomenon (Oxford UP 2024) — рецензируемой академической монографии.",
  source="uap-scientific-publications/sources/eghigian-history-ufology.md")

E("p-wendt-a", "Alexander Wendt", "person · external",
  label_ru="Александр Вендт",
  description="Professor of International Security and International Relations at Ohio State University. Co-author with Raymond Duvall of 'Sovereignty and the UFO' in Political Theory vol. 36 no. 4 (2008) — peer-reviewed top-tier political-theory journal article.",
  description_ru="Профессор международной безопасности и международных отношений в Ohio State University. Соавтор (с Raymond Duvall) статьи «Sovereignty and the UFO» в Political Theory т. 36 № 4 (2008) — рецензируемой статье в журнале первого ряда по политической теории.",
  source="uap-scientific-publications/sources/wendt-duvall-sociological.md")

E("p-kean-l", "Leslie Kean", "person · external",
  label_ru="Лесли Кин",
  description="Investigative journalist (NYT contributor). Author of UFOs: Generals, Pilots, and Government Officials Go on the Record (2010) — investigative non-fiction work that established a peer-reviewed-adjacent foundation for later academic citation. Helped break 2017 NYT Tic-Tac story.",
  description_ru="Журналистка-расследователь (NYT contributor). Автор UFOs: Generals, Pilots, and Government Officials Go on the Record (2010) — расследовательской документальной книги, заложившей рецензируемо-смежное основание для последующего академического цитирования. Способствовала публикации статьи NYT Tic-Tac 2017 г.",
  source="uap-scientific-publications/sources/kean-uap-history.md")

E("p-nolan-g", "Garry Nolan", "person · external",
  label_ru="Гарри Нолан",
  description="Professor of Pathology, Stanford University School of Medicine. Frequent SCU contributor on UAP-related biological / material analysis research.",
  description_ru="Профессор патологии в Stanford University School of Medicine. Регулярный участник SCU по исследованиям UAP-связанного биологического / материального анализа.",
  source="uap-scientific-publications/sources/scu-uap-papers-collection.md")

# ----- SOURCES ---------------------------------------------------------

E("src-kean-2010-uap-history", "Kean 2010 — UFOs: Generals, Pilots, and Government Officials", "source",
  label_ru="Kean 2010 — UFOs: Generals, Pilots, and Government Officials",
  description="Investigative non-fiction (Harmony / Three Rivers Press 2010) compiling first-hand testimony from senior military pilots, government officials, and aviation professionals.",
  description_ru="Расследовательская документальная книга (Harmony / Three Rivers Press 2010), компилирующая свидетельства из первых рук от старших военных лётчиков, государственных чиновников и авиационных профессионалов.",
  source="uap-scientific-publications/sources/kean-uap-history.md")

E("src-pasulka-american-cosmic", "Pasulka — American Cosmic + Encounters", "source",
  label_ru="Пасулька — American Cosmic + Encounters",
  description="American Cosmic: UFOs, Religion, Technology (Oxford UP 2019) + Encounters: Experiences with Nonhuman Intelligences (St. Martin's 2023). Religious-studies framing of contact narratives.",
  description_ru="American Cosmic: UFOs, Religion, Technology (Oxford UP 2019) + Encounters: Experiences with Nonhuman Intelligences (St. Martin's 2023). Религиоведческая рамка нарративов контакта.",
  source="uap-scientific-publications/sources/pasulka-american-cosmic.md")

E("src-eghigian-2024-history-ufology", "Eghigian 2024 — After the Flying Saucers Came", "source",
  label_ru="Эгигян 2024 — After the Flying Saucers Came",
  description="After the Flying Saucers Came: A Global History of the UFO Phenomenon (Oxford UP 2024). Peer-reviewed academic monograph in history-of-science / cultural-history frame.",
  description_ru="After the Flying Saucers Came: A Global History of the UFO Phenomenon (Oxford UP 2024). Рецензируемая академическая монография в рамке истории науки / культурной истории.",
  source="uap-scientific-publications/sources/eghigian-history-ufology.md")

E("src-wendt-duvall-2008", "Wendt & Duvall 2008 — Sovereignty and the UFO", "source",
  label_ru="Вендт и Дюваль 2008 — Sovereignty and the UFO",
  description="Peer-reviewed academic article in Political Theory vol. 36 no. 4 (2008), pp. 607-633. SAGE Publications. Political-theory frame on UAP non-recognition by sovereign states.",
  description_ru="Рецензируемая академическая статья в журнале Political Theory т. 36 № 4 (2008), сс. 607-633. SAGE Publications. Политико-теоретическая рамка непризнания UAP суверенными государствами.",
  source="uap-scientific-publications/sources/wendt-duvall-sociological.md")

E("src-nasa-uap-2023", "NASA UAP Independent Study Team Report (2023)", "source",
  label_ru="Отчёт независимой исследовательской группы NASA по UAP (2023)",
  description="Government-commissioned report (NASA 2023, chair David Spergel). Hosted on nasa.gov.",
  description_ru="Государственный заказной отчёт (NASA 2023, председатель Дэвид Шпергель). Размещён на nasa.gov.",
  source="uap-scientific-publications/sources/nasa-uap-study-2023.md")

E("src-dni-odni-uap-reports", "ODNI UAP Reports 2021-2024 (annual)", "source",
  label_ru="Отчёты ODNI по UAP 2021-2024 (ежегодные)",
  description="ODNI Preliminary Assessment of UAP (June 2021) + 2022 + 2023 + 2024 annual UAP reports per FY2021 Intelligence Authorization Act. Hosted on dni.gov.",
  description_ru="Предварительная оценка UAP от ODNI (июнь 2021) + 2022 + 2023 + 2024 ежегодные отчёты по UAP согласно Intelligence Authorization Act FY2021. Размещены на dni.gov.",
  source="uap-scientific-publications/sources/dni-uap-reports-2021-2024.md")

E("src-aaro-public-reports", "AARO public reports (2024+)", "source",
  label_ru="Публичные отчёты AARO (с 2024+)",
  description="DoD AARO public reports including Historical Record Report Vol. I (March 2024). Hosted on defense.gov / aaro.mil.",
  description_ru="Публичные отчёты AARO Министерства обороны США, включая Historical Record Report Vol. I (март 2024). Размещены на defense.gov / aaro.mil.",
  source="uap-scientific-publications/sources/aaro-public-reports.md")

E("src-hessdalen-papers", "Hessdalen Project peer-reviewed papers", "source",
  label_ru="Рецензируемые работы Hessdalen Project",
  description="Peer-reviewed papers by Strand, Teodorani, Hauge et al. (1998-2010+) on the Hessdalen automated ground-station monitoring of atmospheric light phenomena. Published in Journal of Scientific Exploration, Radio Science.",
  description_ru="Рецензируемые работы Strand, Teodorani, Hauge и др. (1998-2010+) по автоматизированной наземной станции мониторинга атмосферных световых явлений в Hessdalen. Опубликованы в Journal of Scientific Exploration, Radio Science.",
  source="uap-scientific-publications/sources/hessdalen-papers.md")

E("src-nimitz-flir-analyses", "Nimitz Tic-Tac FLIR/radar analyses", "source",
  label_ru="FLIR / РЛС-анализы Nimitz Tic-Tac",
  description="Multiple analyses of the 2004 USS Nimitz Tic-Tac incident — SCU 2019 paper (Powell et al.), Mick West skeptical analyses, AARO public material. Mix of peer-reviewed-adjacent and grey literature.",
  description_ru="Несколько анализов инцидента Nimitz Tic-Tac 2004 г. — статья SCU 2019 (Powell и др.), скептические анализы Mick West, публичный материал AARO. Сочетание рецензируемо-смежного и «серой литературы».",
  source="uap-scientific-publications/sources/nimitz-flir-analyses.md")

E("src-galileo-project-papers", "Galileo Project anchor papers", "source",
  label_ru="Опорные работы Galileo Project",
  description="Anchor papers + observatory-design technical reports from Harvard Galileo Project (Loeb, Cloete et al.). Hosted on galileo.fas.harvard.edu and arXiv preprints.",
  description_ru="Опорные работы + технические отчёты по конструкции обсерватории Galileo Project в Гарварде (Loeb, Cloete и др.). Размещены на galileo.fas.harvard.edu и в arXiv-препринтах.",
  source="uap-scientific-publications/sources/galileo-project-papers.md")

E("src-scu-papers-collection", "SCU collected UAP research papers", "source",
  label_ru="Собрание работ SCU по UAP",
  description="Scientific Coalition for UAP Studies — collected papers, conference proceedings, peer-reviewed Journal of Scientific Exploration / Limina articles. Authors: Powell, Knuth, Taylor, Nolan et al.",
  description_ru="Scientific Coalition for UAP Studies — собрание работ, материалы конференций, рецензируемые статьи в Journal of Scientific Exploration / Limina. Авторы: Powell, Knuth, Taylor, Nolan и др.",
  source="uap-scientific-publications/sources/scu-uap-papers-collection.md")

E("src-nrgscapes-cross-ref", "NRGscapes-Lab cross-reference (Track 7 ↔ Track 9)", "source",
  label_ru="Кросс-ссылка NRGscapes-Lab (Трек 7 ↔ Трек 9)",
  description="Cross-reference pointer: NRGscapes-Lab (Andrew Morgan) heterodox-physics body of work is fully cataloged in Track 7 theoretical-foundations sub-archive. Track 9 cross-references it without duplication.",
  description_ru="Указатель кросс-ссылки: гетеродоксально-физический корпус работ NRGscapes-Lab (Andrew Morgan) полностью каталогизирован в подархиве theoretical-foundations Трека 7. Трек 9 кросс-ссылается на него без дублирования.",
  source="uap-scientific-publications/sources/nrgscapes-cross-ref.md")

E("src-frolov-cross-ref", "Frolov 4D-physics cross-reference (Track 7 ↔ Track 9)", "source",
  label_ru="Кросс-ссылка Фролов 4D-физика (Трек 7 ↔ Трек 9)",
  description="Cross-reference pointer: Alexander V. Frolov 4D / vortex / scalar lineage cataloged in Track 7 theoretical-foundations sub-archive. Track 9 cross-references without duplication.",
  description_ru="Указатель кросс-ссылки: линия 4D / вихрь / скаляр Александра В. Фролова каталогизирована в подархиве theoretical-foundations Трека 7. Трек 9 кросс-ссылается без дублирования.",
  source="uap-scientific-publications/sources/frolov-cross-ref.md")

# ----- CLUSTER MEMBERSHIP ---------------------------------------------

C("inst-galileo-project", "cluster-uap-publications", "member-of", direction="directed")
C("inst-hessdalen-project", "cluster-uap-publications", "member-of", direction="directed")
C("inst-aaro", "cluster-uap-publications", "member-of", direction="directed")
C("inst-odni", "cluster-uap-publications", "member-of", direction="directed")
C("inst-nasa-uap-team", "cluster-uap-publications", "member-of", direction="directed")
C("inst-scu", "cluster-uap-publications", "member-of", direction="directed")

C("p-loeb-a", "cluster-uap-publications", "member-of", direction="directed")
C("p-pasulka-dw", "cluster-uap-publications", "member-of", direction="directed")
C("p-eghigian-g", "cluster-uap-publications", "member-of", direction="directed")
C("p-wendt-a", "cluster-uap-publications", "member-of", direction="directed")
C("p-kean-l", "cluster-uap-publications", "member-of", direction="directed")
C("p-nolan-g", "cluster-uap-publications", "member-of", direction="directed")

C("src-kean-2010-uap-history", "cluster-uap-publications", "member-of", direction="directed")
C("src-pasulka-american-cosmic", "cluster-uap-publications", "member-of", direction="directed")
C("src-eghigian-2024-history-ufology", "cluster-uap-publications", "member-of", direction="directed")
C("src-wendt-duvall-2008", "cluster-uap-publications", "member-of", direction="directed")
C("src-nasa-uap-2023", "cluster-uap-publications", "member-of", direction="directed")
C("src-dni-odni-uap-reports", "cluster-uap-publications", "member-of", direction="directed")
C("src-aaro-public-reports", "cluster-uap-publications", "member-of", direction="directed")
C("src-hessdalen-papers", "cluster-uap-publications", "member-of", direction="directed")
C("src-nimitz-flir-analyses", "cluster-uap-publications", "member-of", direction="directed")
C("src-galileo-project-papers", "cluster-uap-publications", "member-of", direction="directed")
C("src-scu-papers-collection", "cluster-uap-publications", "member-of", direction="directed")
C("src-nrgscapes-cross-ref", "cluster-uap-publications", "member-of", direction="directed")
C("src-frolov-cross-ref", "cluster-uap-publications", "member-of", direction="directed")

# ----- AUTHORSHIP / PRIMARY-SOURCE EDGES -------------------------------

C("p-kean-l", "src-kean-2010-uap-history", "author-of", direction="directed")
C("p-pasulka-dw", "src-pasulka-american-cosmic", "author-of", direction="directed")
C("p-eghigian-g", "src-eghigian-2024-history-ufology", "author-of", direction="directed")
C("p-wendt-a", "src-wendt-duvall-2008", "author-of", direction="directed")
C("p-loeb-a", "src-galileo-project-papers", "author-of", direction="directed")
C("p-loeb-a", "inst-galileo-project", "lead-of", direction="directed")
C("p-nolan-g", "src-scu-papers-collection", "author-of", direction="directed")

# Government-report-of edges
C("src-nasa-uap-2023", "inst-nasa-uap-team", "government-report-of", direction="directed")
C("src-dni-odni-uap-reports", "inst-odni", "government-report-of", direction="directed")
C("src-aaro-public-reports", "inst-aaro", "government-report-of", direction="directed")

# Observation-program-of edges
C("src-galileo-project-papers", "inst-galileo-project", "observation-program-of", direction="directed")
C("src-hessdalen-papers", "inst-hessdalen-project", "observation-program-of", direction="directed")

# Peer-reviewed-by edges (publication infrastructure)
C("src-pasulka-american-cosmic", "src-eghigian-2024-history-ufology", "peer-reviewed-by", direction="undirected",
  description="Both works are Oxford UP peer-reviewed monographs; this edge marks shared publication infrastructure not direct review.")

# SCU institution → its papers
C("src-scu-papers-collection", "inst-scu", "published-by", direction="directed")
C("src-nimitz-flir-analyses", "inst-scu", "published-by", direction="directed")

# ----- CROSS-ARCHIVE BRIDGES -------------------------------------------

# Track 9 ↔ Track 7 theoretical-foundations (overlapping corpus)
C("cluster-uap-publications", "cluster-theoretical-foundations", "overlapping-corpus", direction="undirected")
C("src-nrgscapes-cross-ref", "src-morgan-2025-scalar-field", "overlapping-corpus", direction="directed")
C("src-frolov-cross-ref", "src-frolov-vixri-pdf", "overlapping-corpus", direction="directed")
C("src-frolov-cross-ref", "src-frolov-narod-4d", "overlapping-corpus", direction="directed")

# ════════════════════════════════════════════════════════════════════
# v5 ADDITION — Banchenko Arcanum-12 cycle (ASRP-internal-author sub-corpus)
# ════════════════════════════════════════════════════════════════════

# ----- SUB-CLUSTER ----------------------------------------------------

E("cluster-banchenko-arcanum-cycle", "Banchenko Arcanum-12 cycle (ASRP-internal author)", "cluster",
  label_ru="Цикл Банченко на Arcanum-12 (ASRP-внутренний автор)",
  description="Sub-cluster of Track 9 cataloging the ASRP-internal-author cycle of articles by Denis Banchenko on the Arcanum-12 educational platform — the 'Как я нашёл дорогу домой' cycle plus adjacent articles. Methodologically and topically adjacent to UAP reverse-engineering hypothesis space; consolidated as distinct sub-corpus from externally-authored peer-reviewed / grey / government literature. Banchenko-as-author validation contour applies (see corporate-economic-analysis/analysis/adversarial-osint-framing.md).",
  description_ru="Подкластер Трека 9, каталогизирующий ASRP-внутренний цикл статей Дениса Банченко на образовательной платформе Arcanum-12 — цикл «Как я нашёл дорогу домой» плюс смежные статьи. Методологически и тематически смежен пространству гипотез UAP-реверс-инжиниринга; консолидирован как отдельный подкорпус от внешне-авторской рецензируемой / серой / правительственной литературы. Применяется контур валидации Банченко-как-автор (см. corporate-economic-analysis/analysis/adversarial-osint-framing.md).",
  source="uap-scientific-publications/analysis/banchenko-arcanum-cycle.md")

# ----- PERSON (ASRP-internal author) ----------------------------------

E("p-banchenko-d", "Denis Banchenko", "person · external",
  label_ru="Денис Банченко",
  description="ASRP program director and methodology author. Author of the 'Как я нашёл дорогу домой' cycle on Arcanum-12 educational platform. Public-figure author — name is referenced across the existing UAP_Reverse_Engineering_Study corpus as the methodology source (Tracks 1, 4, 5, 6, 7).",
  description_ru="Директор программы ASRP и автор методологии. Автор цикла «Как я нашёл дорогу домой» на образовательной платформе Arcanum-12. Публичный автор — имя упоминается во всём корпусе UAP_Reverse_Engineering_Study как источник методологии (Треки 1, 4, 5, 6, 7).",
  source="uap-scientific-publications/analysis/banchenko-arcanum-cycle.md")

# ----- SOURCES (4 confirmed Arcanum URLs + 1 pending placeholder) -----

E("src-arcanum-banchenko-332456d3", "Banchenko Arcanum-12 cycle entry 332456d3", "source",
  label_ru="Запись цикла Банченко на Arcanum-12 332456d3",
  description="Banchenko 'Как я нашёл дорогу домой' cycle entry, slug 332456d3-15e9-46ff-b14b-e3b20599b224. Hosted on Arcanum-12 educational platform (arcanum12th.education). Russian-language. Platform may require authentication for full text.",
  description_ru="Запись цикла Банченко «Как я нашёл дорогу домой», slug 332456d3-15e9-46ff-b14b-e3b20599b224. Размещена на образовательной платформе Arcanum-12 (arcanum12th.education). На русском языке. Платформа может требовать авторизацию для полного текста.",
  source="uap-scientific-publications/sources/arcanum-banchenko-cycle-332456d3.md")

E("src-arcanum-banchenko-3d4f3da4", "Banchenko Arcanum-12 cycle entry 3d4f3da4", "source",
  label_ru="Запись цикла Банченко на Arcanum-12 3d4f3da4",
  description="Banchenko 'Как я нашёл дорогу домой' cycle entry, slug 3d4f3da4-ee93-4652-a61d-001ebc9da2c5. Hosted on Arcanum-12 educational platform (arcanum12th.education). Russian-language. Platform may require authentication for full text.",
  description_ru="Запись цикла Банченко «Как я нашёл дорогу домой», slug 3d4f3da4-ee93-4652-a61d-001ebc9da2c5. Размещена на образовательной платформе Arcanum-12 (arcanum12th.education). На русском языке. Платформа может требовать авторизацию для полного текста.",
  source="uap-scientific-publications/sources/arcanum-banchenko-cycle-3d4f3da4.md")

E("src-arcanum-banchenko-2a5ebe26", "Banchenko Arcanum-12 cycle entry 2a5ebe26", "source",
  label_ru="Запись цикла Банченко на Arcanum-12 2a5ebe26",
  description="Banchenko 'Как я нашёл дорогу домой' cycle entry, slug 2a5ebe26-e5f1-4c90-962b-91203fa37899. Hosted on Arcanum-12 educational platform (arcanum12th.education). Russian-language. Platform may require authentication for full text.",
  description_ru="Запись цикла Банченко «Как я нашёл дорогу домой», slug 2a5ebe26-e5f1-4c90-962b-91203fa37899. Размещена на образовательной платформе Arcanum-12 (arcanum12th.education). На русском языке. Платформа может требовать авторизацию для полного текста.",
  source="uap-scientific-publications/sources/arcanum-banchenko-cycle-2a5ebe26.md")

E("src-arcanum-banchenko-2ccb5339", "Banchenko Arcanum-12 cycle entry 2ccb5339", "source",
  label_ru="Запись цикла Банченко на Arcanum-12 2ccb5339",
  description="Banchenko 'Как я нашёл дорогу домой' cycle entry, slug 2ccb5339-820a-4296-b24d-1d453a94c2be. Hosted on Arcanum-12 educational platform (arcanum12th.education). Russian-language. Platform may require authentication for full text.",
  description_ru="Запись цикла Банченко «Как я нашёл дорогу домой», slug 2ccb5339-820a-4296-b24d-1d453a94c2be. Размещена на образовательной платформе Arcanum-12 (arcanum12th.education). На русском языке. Платформа может требовать авторизацию для полного текста.",
  source="uap-scientific-publications/sources/arcanum-banchenko-cycle-2ccb5339.md")

E("src-arcanum-banchenko-pending", "Banchenko Arcanum-12 cycle pending entries (~8 expected)", "source",
  label_ru="Ожидаемые записи цикла Банченко на Arcanum-12 (~8 ожидается)",
  description="Placeholder source entry tracking the pending portion of the 'Как я нашёл дорогу домой' cycle on Arcanum-12. Cycle is approximately 12 articles in total; 4 are confirmed as standalone provenance entries; ~8 remain pending submission. Tracked as v6+ open work-item.",
  description_ru="Заглушка-запись источника, отслеживающая ожидающую часть цикла «Как я нашёл дорогу домой» на Arcanum-12. Цикл — около 12 статей в сумме; 4 подтверждены как отдельные записи провенанса; ~8 остаются в ожидании отправки. Отслеживается как открытый рабочий пункт v6+.",
  source="uap-scientific-publications/sources/arcanum-banchenko-cycle-pending.md")

# ----- SUB-CLUSTER MEMBERSHIP ----------------------------------------

C("cluster-banchenko-arcanum-cycle", "cluster-uap-publications", "sub-cluster-of", direction="directed")

C("p-banchenko-d", "cluster-banchenko-arcanum-cycle", "member-of", direction="directed")
C("src-arcanum-banchenko-332456d3", "cluster-banchenko-arcanum-cycle", "member-of", direction="directed")
C("src-arcanum-banchenko-3d4f3da4", "cluster-banchenko-arcanum-cycle", "member-of", direction="directed")
C("src-arcanum-banchenko-2a5ebe26", "cluster-banchenko-arcanum-cycle", "member-of", direction="directed")
C("src-arcanum-banchenko-2ccb5339", "cluster-banchenko-arcanum-cycle", "member-of", direction="directed")
C("src-arcanum-banchenko-pending", "cluster-banchenko-arcanum-cycle", "member-of", direction="directed")

# ----- AUTHORSHIP EDGES ----------------------------------------------

C("p-banchenko-d", "src-arcanum-banchenko-332456d3", "author-of", direction="directed")
C("p-banchenko-d", "src-arcanum-banchenko-3d4f3da4", "author-of", direction="directed")
C("p-banchenko-d", "src-arcanum-banchenko-2a5ebe26", "author-of", direction="directed")
C("p-banchenko-d", "src-arcanum-banchenko-2ccb5339", "author-of", direction="directed")
C("p-banchenko-d", "src-arcanum-banchenko-pending", "author-of", direction="directed")

# ════════════════════════════════════════════════════════════════════
# v6 ADDITION — 17 HIGH-priority Perplexity-research-audit sources
#                + 2 adversarial-balance entries (Condon + Blue Book)
# ════════════════════════════════════════════════════════════════════

# ----- NEW INSTITUTION (CNES / GEIPAN) --------------------------------

E("inst-cnes-geipan", "CNES / GEIPAN (France, 1977-present)", "institution",
  label_ru="CNES / GEIPAN (Франция, с 1977 г.)",
  description="Centre national d'études spatiales (CNES) GEIPAN office — the only national-government civilian UAP investigation office continuously operating from 1977 to present. Institutional lineage: GEPAN (1977-1988) → SEPRA (1988-2004) → GEIPAN (2005-present). Maintains the only national-government-curated UAP case database with structured A/B/C/D classification, public per-case dossiers, 3200+ entries.",
  description_ru="Офис GEIPAN при Centre national d'études spatiales (CNES) — единственный национальный правительственно-гражданский UAP-исследовательский офис, непрерывно работающий с 1977 г. по настоящее время. Институциональная линия: GEPAN (1977-1988) → SEPRA (1988-2004) → GEIPAN (2005-наст. вр.). Поддерживает единственную национальную правительственно-куратируемую базу данных UAP-случаев со структурированной классификацией A/B/C/D, публичными покаждоисточниковыми досье, 3200+ записей.",
  source="uap-scientific-publications/sources/geipan-cnes-database.md")

# ----- NEW PERSONS (published authors of v6 HIGH papers) --------------

E("p-knuth-k", "Kevin H. Knuth", "person · external",
  label_ru="Кевин Х. Кнут",
  description="Associate Professor of Physics, University at Albany (SUNY). Lead author of Knuth K.H. et al. 2025 New Science of UAP (Progress in Aerospace Sciences, 33-author landmark) and co-author of Knuth/Powell/Reali 2019 Entropy on Nimitz flight characteristics. UAPx co-investigator (Szydagis et al. 2025 PiAS).",
  description_ru="Доцент кафедры физики, University at Albany (SUNY). Ведущий автор работы Knuth K.H. и др. 2025 New Science of UAP (Progress in Aerospace Sciences, 33-авторская веха) и соавтор Knuth/Powell/Reali 2019 Entropy по лётным характеристикам Nimitz. Со-исследователь UAPx (Szydagis и др. 2025 PiAS).",
  source="uap-scientific-publications/sources/knuth-2025-new-science-uap.md")

E("p-powell-r", "Robert Powell", "person · external",
  label_ru="Роберт Пауэлл",
  description="Co-founder, Scientific Coalition for UAP Studies (SCU). Lead author of SCU 2019 Nimitz CSG-11 forensic report, Knuth/Powell/Reali 2019 Entropy on flight characteristics, and Powell et al. 2022 SCU Ubatuba isotope re-analysis.",
  description_ru="Соучредитель Scientific Coalition for UAP Studies (SCU). Ведущий автор криминалистического отчёта SCU 2019 по Nimitz CSG-11, Knuth/Powell/Reali 2019 Entropy по лётным характеристикам и Powell и др. 2022 SCU повторного изотопного анализа Ubatuba.",
  source="uap-scientific-publications/sources/powell-2019-nimitz-csg11-forensic.md")

E("p-hancock-l", "Larry J. Hancock", "person · external",
  label_ru="Ларри Дж. Хэнкок",
  description="Researcher / author. Lead of the SCU/Zenodo 2023 UAP Pattern Recognition Study 1945-1975 US Atomic Warfare Complex (grey-literature precursor) and co-author of the peer-reviewed Limina V2N1 2025 indications-analysis sequel (Grosvenor / Hancock / Porritt).",
  description_ru="Исследователь / автор. Ведущий SCU/Zenodo Исследования паттернов UAP 1945-1975 для атомно-вооружённого комплекса США 2023 г. (грей-лит предшественник) и соавтор рецензируемого преемника анализа индикаций Limina V2N1 2025 г. (Grosvenor / Hancock / Porritt).",
  source="uap-scientific-publications/sources/hancock-2023-scu-pattern-recognition.md")

E("p-vallee-j", "Jacques Vallée", "person · external",
  label_ru="Жак Валле",
  description="Computer scientist and ufologist; co-author across a 25-year continuous lineage of UAP material-and-energy analysis papers — Vallée 1998 JSE physical analyses of 10 cases; Nolan / Vallée / Jiang / Lemke 2022 Progress in Aerospace Sciences improved instrumental techniques + isotopic analysis; Vallée / Dini / Mestchersky 2025 Progress in Aerospace Sciences radiative-energy estimate; co-author of the 33-author Knuth et al. 2025 PiAS landmark.",
  description_ru="Компьютерный учёный и ufolog; соавтор 25-летней непрерывной линии работ по анализу материи и энергии UAP — Vallée 1998 JSE физический анализ 10 случаев; Nolan / Vallée / Jiang / Lemke 2022 Progress in Aerospace Sciences улучшенные инструментальные методики + изотопный анализ; Vallée / Dini / Mestchersky 2025 Progress in Aerospace Sciences оценка излучательной энергии; соавтор 33-авторской вехи Knuth и др. 2025 PiAS.",
  source="uap-scientific-publications/sources/vallee-1998-material-samples.md")

E("p-villarroel-b", "Beatriz Villarroel", "person · external",
  label_ru="Беатрис Виларроэль",
  description="Astrophysicist, Nordita-KTH (Stockholm Observatory). Lead investigator of the VASCO program. Second author on Bruehl & Villarroel 2025 Sci. Rep. — the peer-reviewed POSS-I transients ↔ nuclear-testing + UAP-reports statistical analysis.",
  description_ru="Астрофизик, Nordita-KTH (Стокгольмская обсерватория). Ведущий исследователь программы VASCO. Второй автор Bruehl & Villarroel 2025 Sci. Rep. — рецензируемого статистического анализа транзиенты POSS-I ↔ ядерные испытания + сообщения UAP.",
  source="uap-scientific-publications/sources/bruehl-villarroel-2025-poss-nuclear.md")

E("p-kirkpatrick-s", "Sean M. Kirkpatrick", "person · external",
  label_ru="Шон М. Киркпатрик",
  description="Physicist (DoD); founding director of the All-domain Anomaly Resolution Office (AARO) 2022-2023. Co-author of Medina / Brewer / Kirkpatrick 2023 Sci. Rep. environmental analysis of public UAP sightings — the only NUFORC-scale geospatial study with an active US-government UAP-office co-author. Track 9 cites the methodology, NOT the broader AARO political tenure.",
  description_ru="Физик (DoD); учредительный директор All-domain Anomaly Resolution Office (AARO) 2022-2023. Соавтор Medina / Brewer / Kirkpatrick 2023 Sci. Rep. экологического анализа публичных сообщений UAP — единственного геопространственного исследования NUFORC-масштаба с действующим соавтором из правительственного UAP-офиса США. Трек 9 цитирует методологию, а НЕ более широкий политический срок AARO.",
  source="uap-scientific-publications/sources/medina-brewer-kirkpatrick-2023-environmental.md")

# ----- NEW SOURCES (17 HIGH + 2 adversarial-balance = 19) -------------

E("src-knuth-2025-new-science-uap", "Knuth et al. 2025 — The New Science of UAP", "source",
  label_ru="Knuth и др. 2025 — Новая наука о UAP",
  description="33-author landmark synthesis in Elsevier Progress in Aerospace Sciences (Q1). First peer-reviewed multinational global synthesis of historical government UAP studies covering Scandinavia, WWII, US, Canada, France, Russia, China; arXiv 2502.06794.",
  description_ru="33-авторский синтез-веха в Elsevier Progress in Aerospace Sciences (Q1). Первый рецензируемый мультинациональный глобальный синтез исторических правительственных исследований UAP, охватывающий Скандинавию, ВВ2, США, Канаду, Францию, Россию, Китай; arXiv 2502.06794.",
  source="uap-scientific-publications/sources/knuth-2025-new-science-uap.md")

E("src-watters-loeb-2023-multimodal-observatories", "Watters/Loeb/Laukien 2023 — Multimodal Ground-Based Observatories", "source",
  label_ru="Watters/Loeb/Laukien 2023 — Мультимодальные наземные обсерватории",
  description="Galileo Project methodology paper, Journal of Astronomical Instrumentation 2023, DOI 10.1142/S2251171723400068. Defines the canonical Science Traceability Matrix (STM) and six-modality sensor stack including quasistatic E/B field instrumentation.",
  description_ru="Методологическая работа Galileo Project, Journal of Astronomical Instrumentation 2023, DOI 10.1142/S2251171723400068. Определяет канонический Science Traceability Matrix (STM) и шестимодальный сенсорный стек, включая инструментирование квазистатических E/B полей.",
  source="uap-scientific-publications/sources/watters-loeb-2023-multimodal-observatories.md")

E("src-domine-2025-galileo-allsky-ir", "Domine et al. 2025 — All-Sky IR Camera Array Commissioning", "source",
  label_ru="Domine и др. 2025 — Ввод всенебесной ИК-камерной решётки",
  description="MDPI Sensors 2025, DOI 10.3390/s25030783. First quantified end-to-end performance baseline of the Galileo 8-camera LWIR all-sky array; YOLO+SORT pipeline; likelihood-based outlier upper-limit framework reusable as Track 5 OSINT methodology template.",
  description_ru="MDPI Sensors 2025, DOI 10.3390/s25030783. Первая количественная сквозная производительностная базовая линия 8-камерной LWIR-всенебесной решётки Galileo; конвейер YOLO+SORT; правдоподобно-статистическая рамка верхней границы выбросов, переиспользуемая как методологический шаблон Трека 5 OSINT.",
  source="uap-scientific-publications/sources/domine-2025-galileo-allsky-ir.md")

E("src-szydagis-uapx-2025", "Szydagis et al. 2025 — UAPx First Field Expedition", "source",
  label_ru="Szydagis и др. 2025 — Первая полевая экспедиция UAPx",
  description="Elsevier Progress in Aerospace Sciences 2025; arXiv preprint 2312.00558. First peer-reviewed write-up of an instrumented UAPx field expedition (Catalina Island July 2021); ~1 hr triggered visible + 600 hr untriggered IR + 55 hr radiation; proposed 3-5σ rule-set for hard-science UAP analysis.",
  description_ru="Elsevier Progress in Aerospace Sciences 2025; arXiv-препринт 2312.00558. Первая рецензируемая работа по инструментированной полевой экспедиции UAPx (остров Каталина, июль 2021 г.); ~1 час триггерированного видимого + 600 часов нетриггерированного ИК + 55 часов радиации; предложенное правило 3-5σ для научно-строгого анализа UAP.",
  source="uap-scientific-publications/sources/szydagis-uapx-2025.md")

E("src-knuth-powell-reali-2019-nimitz-physics", "Knuth/Powell/Reali 2019 — Estimating Flight Characteristics of Anomalous UAVs", "source",
  label_ru="Knuth/Powell/Reali 2019 — Оценка лётных характеристик аномальных UAV",
  description="MDPI Entropy 2019, DOI 10.3390/e21100939; companion in MaxEnt 2019 proceedings (DOI 10.3390/proceedings2019033026). Bayesian / MaxEnt extraction of acceleration / velocity / energy bounds (~100g to thousands of g, Mach 40-60) for the 2004 Nimitz Tic-Tac and adjacent encounters.",
  description_ru="MDPI Entropy 2019, DOI 10.3390/e21100939; компаньон в материалах MaxEnt 2019 (DOI 10.3390/proceedings2019033026). Байесовская / макс-энтропийная экстракция границ ускорения / скорости / энергии (~100g до тысяч g, Мах 40-60) для Tic-Tac Nimitz 2004 и смежных столкновений.",
  source="uap-scientific-publications/sources/knuth-powell-reali-2019-nimitz-physics.md")

E("src-bruehl-villarroel-2025-poss-nuclear", "Bruehl & Villarroel 2025 — POSS-I Transients ↔ Nuclear Testing + UAP Reports", "source",
  label_ru="Bruehl & Villarroel 2025 — Транзиенты POSS-I ↔ ядерные испытания + сообщения UAP",
  description="Springer Nature Scientific Reports 2025 (Sci. Rep. 15:34125). First peer-reviewed statistical test linking pre-Sputnik POSS-I sky-survey transients to above-ground nuclear weapons tests and contemporaneous UAP reports; nuclear↔transient p=0.008 (+45% within ±1 day). All-tests-pooled — NOT site-specific.",
  description_ru="Springer Nature Scientific Reports 2025 (Sci. Rep. 15:34125). Первый рецензируемый статистический тест, связывающий пред-спутниковые транзиенты обзора неба POSS-I с надземными ядерными испытаниями и современными им сообщениями UAP; ядерные↔транзиент p=0.008 (+45% в окне ±1 день). Все-испытания-агрегированный — НЕ конкретно-сайтовый.",
  source="uap-scientific-publications/sources/bruehl-villarroel-2025-poss-nuclear.md")

E("src-medina-brewer-kirkpatrick-2023-environmental", "Medina/Brewer/Kirkpatrick 2023 — Environmental Analysis of Public UAP Sightings", "source",
  label_ru="Medina/Brewer/Kirkpatrick 2023 — Экологический анализ публичных сообщений UAP",
  description="Springer Nature Scientific Reports 2023, DOI 10.1038/s41598-023-49527-x. Bayesian-regression model of NUFORC sightings 2001-2020 (n≈98,000) across the conterminous US with environmental covariates; opportunity-to-see null model for any geospatial UAP cluster claim. Co-author Kirkpatrick = founding AARO director.",
  description_ru="Springer Nature Scientific Reports 2023, DOI 10.1038/s41598-023-49527-x. Байесовско-регрессионная модель сообщений NUFORC 2001-2020 гг. (n≈98 000) по contiguous-территории США с экологическими ковариатами; null-модель «возможность увидеть» для любого геопространственного UAP-кластерного утверждения. Соавтор Kirkpatrick = учредительный директор AARO.",
  source="uap-scientific-publications/sources/medina-brewer-kirkpatrick-2023-environmental.md")

E("src-grosvenor-hancock-porritt-2025-atomic-complex", "Grosvenor/Hancock/Porritt 2025 — UAP Indications 1945-1975 US Atomic Warfare Complex", "source",
  label_ru="Grosvenor/Hancock/Porritt 2025 — Индикации UAP 1945-1975, Атомно-вооружённый комплекс США",
  description="Limina V2N1 (SCU journal, founded 2022), DOI 10.59661/001c.131854. Indications-analysis study (n=874) testing four intent scenarios over the US atomic-warfare complex 1945-1975; concludes 'Atomic Weapons Survey' scenario fits best. Methodology adapted from US IC threat-and-warnings doctrine (Grabo 2004).",
  description_ru="Limina V2N1 (журнал SCU, основан 2022), DOI 10.59661/001c.131854. Анализ индикаций (n=874), тестирующий четыре интентных сценария по атомно-вооружённому комплексу США 1945-1975 гг.; делает вывод, что сценарий «Atomic Weapons Survey» подходит лучше всего. Методология адаптирована из доктрины indications-and-warnings IC США (Grabo 2004).",
  source="uap-scientific-publications/sources/grosvenor-hancock-porritt-2025-atomic-complex.md")

E("src-hancock-2023-scu-pattern-recognition", "Hancock et al. 2023 — UAP Pattern Recognition 1945-1975 Atomic Complex", "source",
  label_ru="Hancock и др. 2023 — Паттерны UAP 1945-1975, атомный комплекс",
  description="SCU/Zenodo grey-literature precursor (n=590) of the 2025 peer-reviewed Limina sequel. Pattern-recognition correlating UAP incidents with US atomic-warfare-complex installations: LANL, Sandia, Oak Ridge, Hanford, Pantex, Kirtland AFB, Manzano weapons-storage.",
  description_ru="SCU/Zenodo «серо-литературный» предшественник (n=590) рецензируемого преемника Limina 2025 г. Паттерн-распознавание, коррелирующее инциденты UAP с объектами атомно-вооружённого комплекса США: LANL, Sandia, Oak Ridge, Hanford, Pantex, Kirtland AFB, склад вооружений Manzano.",
  source="uap-scientific-publications/sources/hancock-2023-scu-pattern-recognition.md")

E("src-vallee-1998-material-samples", "Vallée 1998 — Physical Analyses 10 Cases Material Samples", "source",
  label_ru="Vallée 1998 — Физический анализ 10 случаев с материальными образцами",
  description="Journal of Scientific Exploration Vol. 12 No. 3 (1998). Foundational catalog of UAP-material physical analyses with isotopic / metallurgical / chemical assay protocols (Ubatuba, Council Bluffs, Maury Island, etc.). Methodological precursor for Track 1 UAP-FRAG-001 chain-of-custody and assay-protocol documentation.",
  description_ru="Journal of Scientific Exploration т. 12 № 3 (1998). Базовый каталог физических анализов UAP-материалов с изотопными / металлургическими / химическими протоколами (Ubatuba, Council Bluffs, Maury Island и др.). Методологический предшественник для документации цепочки кастоди и протоколов анализа Трека 1 UAP-FRAG-001.",
  source="uap-scientific-publications/sources/vallee-1998-material-samples.md")

E("src-powell-2022-ubatuba-isotope", "Powell et al. 2022 — 1957 Brazilian Ubatuba Fragment Isotope Ratios", "source",
  label_ru="Powell и др. 2022 — Изотопные соотношения бразильского фрагмента Ubatuba 1957",
  description="SCU 2022 high-resolution isotope-ratio mass-spectrometry (HR-ICPMS) and chemical-composition re-analysis of the 1957 Ubatuba fragment. Methodological precedent for Track 1 UAP-FRAG-001 isotopic analysis pipeline; companion to Nolan/Vallée 2022 PiAS peer-reviewed methodology frame. 65-year custody chain explicitly noted.",
  description_ru="SCU 2022 г. высокоразрешающая масс-спектрометрия изотопных соотношений (HR-ICPMS) и химико-композиционный повторный анализ фрагмента Ubatuba 1957 г. Методологический прецедент для конвейера изотопного анализа Трека 1 UAP-FRAG-001; компаньон рецензируемому методологическому каркасу Nolan/Vallée 2022 PiAS. 65-летняя цепочка кастоди явно отмечена.",
  source="uap-scientific-publications/sources/powell-2022-ubatuba-isotope.md")

E("src-powell-2019-nimitz-csg11-forensic", "Powell et al. 2019 — Forensic Analysis Nimitz CSG-11 Encounter", "source",
  label_ru="Powell и др. 2019 — Криминалистический анализ столкновения Nimitz CSG-11",
  description="SCU 2019 forensic report integrating FLIR1/Gimbal/GoFast clips with Princeton/Higgins radar-track reconstructions and pilot-debrief witness chains (Fravor, Slaight, Day). Methodological centre of gravity for the entire Nimitz Tic-Tac literature.",
  description_ru="SCU 2019 г. криминалистический отчёт, объединяющий клипы FLIR1/Gimbal/GoFast с реконструкциями радарных треков Princeton/Higgins и цепочками опросов пилотов (Fravor, Slaight, Day). Методологический центр тяжести всей литературы по Tic-Tac Nimitz.",
  source="uap-scientific-publications/sources/powell-2019-nimitz-csg11-forensic.md")

E("src-lomas-2025-uap-assessment-matrix", "Lomas et al. 2025 — UAP Assessment Matrix", "source",
  label_ru="Lomas и др. 2025 — Матрица оценки UAP",
  description="Elsevier Acta Astronautica 2025 (Q1 aerospace-engineering, IF≈2.5). Structured evidence-evaluation matrix for UAP cases — formal scoring rubric applicable to Track 5 OSINT signature-classification, Track 3 Chernobrov-USSR ranking, and Track 8 cross-archive case-comparison.",
  description_ru="Elsevier Acta Astronautica 2025 (Q1 аэрокосмически-инженерный, IF≈2.5). Структурированная матрица оценки свидетельств для UAP-случаев — формальная оценочная рубрика, применимая к классификации сигнатур Трека 5 OSINT, ранжированию Чернобров-СССР Трека 3 и кросс-архивному сравнению случаев Трека 8.",
  source="uap-scientific-publications/sources/lomas-2025-uap-assessment-matrix.md")

E("src-nolan-vallee-2022-isotopic-aerospace-forensics", "Nolan/Vallée/Jiang/Lemke 2022 — Improved Instrumental Techniques + Isotopic Analysis", "source",
  label_ru="Nolan/Vallée/Jiang/Lemke 2022 — Улучшенные инструментальные методики + изотопный анализ",
  description="Elsevier Progress in Aerospace Sciences Vol. 128 (2022), DOI 10.1016/j.paerosci.2021.100788. Methodology-anchor citation for Track 1 isotopic-analysis pipeline. Stanford-domain (Nolan, Jiang) + ex-NASA-Ames (Lemke) + Vallée co-authorship in Q1 PiAS — establishes HR-ICPMS / SIMS / TIMS as legitimate aerospace-forensics technique.",
  description_ru="Elsevier Progress in Aerospace Sciences т. 128 (2022), DOI 10.1016/j.paerosci.2021.100788. Методолого-якорная ссылка для конвейера изотопного анализа Трека 1. Stanford-домен (Nolan, Jiang) + ex-NASA-Ames (Lemke) + соавторство Vallée в Q1 PiAS — устанавливает HR-ICPMS / SIMS / TIMS как легитимную аэрокосмическо-криминалистическую методику.",
  source="uap-scientific-publications/sources/nolan-vallee-2022-isotopic-aerospace-forensics.md")

E("src-vallee-dini-mestchersky-2025-radiative-energy", "Vallée/Dini/Mestchersky 2025 — Radiative Energy Estimates Ground-Level UAP", "source",
  label_ru="Vallée/Dini/Mestchersky 2025 — Оценки излучательной энергии наземного UAP",
  description="Elsevier Progress in Aerospace Sciences 2025. Quantitative radiative-energy estimate for a ground-level UAP case. First peer-reviewed PiAS UAP-energy-budget paper. Fourth and most recent entry in the 25-year Vallée material-and-energy lineage (1998 → 2003 → 2022 → 2025).",
  description_ru="Elsevier Progress in Aerospace Sciences 2025. Количественная оценка излучательной энергии для наземного UAP-случая. Первая рецензируемая PiAS-работа по энергетическому бюджету UAP. Четвёртая и наиболее недавняя запись в 25-летней линии Vallée по анализу материи и энергии (1998 → 2003 → 2022 → 2025).",
  source="uap-scientific-publications/sources/vallee-dini-mestchersky-2025-radiative-energy.md")

E("src-aaro-aui-2025-workshop", "DoD AARO + AUI 2025 — UAP Workshop: Narrative Data Infrastructures", "source",
  label_ru="DoD AARO + AUI 2025 — Семинар по UAP: инфраструктуры нарративных данных",
  description="DoD AARO + Associated Universities Inc. (AUI) 2025 workshop on UAP narrative-data infrastructures. First known explicit US-government convening on UAP narrative-data tooling. Hosted on aaro.mil / aui.edu.",
  description_ru="Семинар DoD AARO + Associated Universities Inc. (AUI) 2025 г. по инфраструктурам нарративных данных по UAP. Первый известный явный правительственный созыв США по инструментарию нарративных данных по UAP. Размещение на aaro.mil / aui.edu.",
  source="uap-scientific-publications/sources/aaro-aui-2025-workshop.md")

E("src-geipan-cnes-database", "CNES / GEIPAN — Online UAP Cases Database (1977-present)", "source",
  label_ru="CNES / GEIPAN — Онлайн-база данных UAP-случаев (с 1977 г.)",
  description="The only national-government-curated UAP case database with structured A/B/C/D classification, public per-case dossiers, 3200+ entries continuous 1977-present. Subsumes GEPAN (1977-1988) → SEPRA (1988-2004) → GEIPAN (2005-present) institutional lineage and the CAIPAN 2014 workshop.",
  description_ru="Единственная национальная правительственно-куратируемая база данных UAP-случаев со структурированной классификацией A/B/C/D, публичными покаждоисточниковыми досье, 3200+ записей непрерывно с 1977 г. по наст. вр. Включает институциональную линию GEPAN (1977-1988) → SEPRA (1988-2004) → GEIPAN (2005-наст. вр.) и семинар CAIPAN 2014.",
  source="uap-scientific-publications/sources/geipan-cnes-database.md")

E("src-condon-report-1968", "Condon Report 1968 — Scientific Study of UFOs", "source",
  label_ru="Отчёт Кондона 1968 — Научное исследование НЛО",
  description="University of Colorado UFO Project (Edward U. Condon, 1966-1968). ~1500 pages with appendices, 14,885 underlying record pages, 59 individually-investigated cases. Canonical scientific-establishment null-finding on UAP; basis for Project Blue Book termination 1969. Adversarial-balance pair with AARO Historical Record V1 (2024).",
  description_ru="UFO Project Университета Колорадо (Edward U. Condon, 1966-1968). Около 1500 страниц с приложениями, 14 885 страниц лежащих в основе записей, 59 индивидуально расследованных случаев. Канонический научно-истеблишментальный null-вывод по UAP; основание для прекращения Project Blue Book 1969 г. Состязательно-балансирующая пара с AARO Historical Record V1 (2024).",
  source="uap-scientific-publications/sources/condon-report-1968.md")

E("src-blue-book-archives", "USAF Project Blue Book Archives 1952-1969 (NARA RG341)", "source",
  label_ru="Архивы Project Blue Book ВВС США 1952-1969 (NARA RG341)",
  description="12,618 reports collected by USAF 1952-1969, digitised at the National Archives (NARA Record Group 341). Subsumes predecessor sub-projects: Project SIGN (1947-1948), Project GRUDGE (1948-1949), Project Twinkle (1949-1951, green-fireballs LANL/SNL/White Sands cluster). Officially terminated 1969 on the basis of the Condon Report.",
  description_ru="12 618 сообщений, собранных ВВС США 1952-1969 гг., дигитизированы в Национальных архивах (NARA Record Group 341). Включает предшественниковые подпроекты: Project SIGN (1947-1948), Project GRUDGE (1948-1949), Project Twinkle (1949-1951, кластер зелёных болидов LANL/SNL/Уайт-Сэндс). Официально прекращён в 1969 г. на основании Отчёта Кондона.",
  source="uap-scientific-publications/sources/blue-book-archives.md")

# ----- v6 CLUSTER MEMBERSHIP (all new sources + persons + inst) -------

C("inst-cnes-geipan", "cluster-uap-publications", "member-of", direction="directed")

C("p-knuth-k", "cluster-uap-publications", "member-of", direction="directed")
C("p-powell-r", "cluster-uap-publications", "member-of", direction="directed")
C("p-hancock-l", "cluster-uap-publications", "member-of", direction="directed")
C("p-vallee-j", "cluster-uap-publications", "member-of", direction="directed")
C("p-villarroel-b", "cluster-uap-publications", "member-of", direction="directed")
C("p-kirkpatrick-s", "cluster-uap-publications", "member-of", direction="directed")

C("src-knuth-2025-new-science-uap", "cluster-uap-publications", "member-of", direction="directed")
C("src-watters-loeb-2023-multimodal-observatories", "cluster-uap-publications", "member-of", direction="directed")
C("src-domine-2025-galileo-allsky-ir", "cluster-uap-publications", "member-of", direction="directed")
C("src-szydagis-uapx-2025", "cluster-uap-publications", "member-of", direction="directed")
C("src-knuth-powell-reali-2019-nimitz-physics", "cluster-uap-publications", "member-of", direction="directed")
C("src-bruehl-villarroel-2025-poss-nuclear", "cluster-uap-publications", "member-of", direction="directed")
C("src-medina-brewer-kirkpatrick-2023-environmental", "cluster-uap-publications", "member-of", direction="directed")
C("src-grosvenor-hancock-porritt-2025-atomic-complex", "cluster-uap-publications", "member-of", direction="directed")
C("src-hancock-2023-scu-pattern-recognition", "cluster-uap-publications", "member-of", direction="directed")
C("src-vallee-1998-material-samples", "cluster-uap-publications", "member-of", direction="directed")
C("src-powell-2022-ubatuba-isotope", "cluster-uap-publications", "member-of", direction="directed")
C("src-powell-2019-nimitz-csg11-forensic", "cluster-uap-publications", "member-of", direction="directed")
C("src-lomas-2025-uap-assessment-matrix", "cluster-uap-publications", "member-of", direction="directed")
C("src-nolan-vallee-2022-isotopic-aerospace-forensics", "cluster-uap-publications", "member-of", direction="directed")
C("src-vallee-dini-mestchersky-2025-radiative-energy", "cluster-uap-publications", "member-of", direction="directed")
C("src-aaro-aui-2025-workshop", "cluster-uap-publications", "member-of", direction="directed")
C("src-geipan-cnes-database", "cluster-uap-publications", "member-of", direction="directed")
C("src-condon-report-1968", "cluster-uap-publications", "member-of", direction="directed")
C("src-blue-book-archives", "cluster-uap-publications", "member-of", direction="directed")

# ----- v6 AUTHOR-OF EDGES --------------------------------------------

# Knuth — leads 3 papers + co-authors UAPx
C("p-knuth-k", "src-knuth-2025-new-science-uap", "author-of", direction="directed")
C("p-knuth-k", "src-knuth-powell-reali-2019-nimitz-physics", "author-of", direction="directed")
C("p-knuth-k", "src-szydagis-uapx-2025", "author-of", direction="directed")

# Powell — co-authors Nimitz physics + 3 SCU reports
C("p-powell-r", "src-knuth-powell-reali-2019-nimitz-physics", "author-of", direction="directed")
C("p-powell-r", "src-powell-2019-nimitz-csg11-forensic", "author-of", direction="directed")
C("p-powell-r", "src-powell-2022-ubatuba-isotope", "author-of", direction="directed")

# Hancock — leads SCU 2023 + co-authors Limina 2025
C("p-hancock-l", "src-hancock-2023-scu-pattern-recognition", "author-of", direction="directed")
C("p-hancock-l", "src-grosvenor-hancock-porritt-2025-atomic-complex", "author-of", direction="directed")

# Vallée — 4 papers across 25-year lineage (1998 → 2022 → 2025) + Knuth 2025 co-author
C("p-vallee-j", "src-vallee-1998-material-samples", "author-of", direction="directed")
C("p-vallee-j", "src-nolan-vallee-2022-isotopic-aerospace-forensics", "author-of", direction="directed")
C("p-vallee-j", "src-vallee-dini-mestchersky-2025-radiative-energy", "author-of", direction="directed")
C("p-vallee-j", "src-knuth-2025-new-science-uap", "author-of", direction="directed")

# Villarroel — Bruehl/Villarroel 2025 + Knuth 2025 co-author
C("p-villarroel-b", "src-bruehl-villarroel-2025-poss-nuclear", "author-of", direction="directed")
C("p-villarroel-b", "src-knuth-2025-new-science-uap", "author-of", direction="directed")

# Kirkpatrick — Medina/Brewer/Kirkpatrick 2023
C("p-kirkpatrick-s", "src-medina-brewer-kirkpatrick-2023-environmental", "author-of", direction="directed")

# Loeb — Watters/Loeb/Laukien 2023 + Domine 2025 (already lead-of inst-galileo-project)
C("p-loeb-a", "src-watters-loeb-2023-multimodal-observatories", "author-of", direction="directed")
C("p-loeb-a", "src-domine-2025-galileo-allsky-ir", "author-of", direction="directed")

# Nolan — Nolan/Vallée 2022 + Knuth 2025 co-author
C("p-nolan-g", "src-nolan-vallee-2022-isotopic-aerospace-forensics", "author-of", direction="directed")
C("p-nolan-g", "src-knuth-2025-new-science-uap", "author-of", direction="directed")

# ----- v6 INSTITUTIONAL / PROGRAM / PEER-REVIEW EDGES -----------------

# Galileo Project ↔ observation-program papers
C("src-watters-loeb-2023-multimodal-observatories", "inst-galileo-project", "observation-program-of", direction="directed")
C("src-domine-2025-galileo-allsky-ir", "inst-galileo-project", "observation-program-of", direction="directed")

# SCU ↔ SCU-published reports
C("src-powell-2019-nimitz-csg11-forensic", "inst-scu", "published-by", direction="directed")
C("src-hancock-2023-scu-pattern-recognition", "inst-scu", "published-by", direction="directed")
C("src-powell-2022-ubatuba-isotope", "inst-scu", "published-by", direction="directed")
C("src-grosvenor-hancock-porritt-2025-atomic-complex", "inst-scu", "published-by", direction="directed")

# Government convening / database edges
C("src-aaro-aui-2025-workshop", "inst-aaro", "government-report-of", direction="directed")
C("src-geipan-cnes-database", "inst-cnes-geipan", "government-report-of", direction="directed")

# ----- v6 GREY-LIT PRECURSOR-OF EDGES (paired evolutions) -------------

C("src-hancock-2023-scu-pattern-recognition", "src-grosvenor-hancock-porritt-2025-atomic-complex",
  "grey-lit-precursor-of", direction="directed",
  description="SCU/Zenodo 2023 grey-literature pattern-recognition study is the empirical-base precursor to the 2025 Limina V2N1 peer-reviewed indications-analysis sequel (same dataset, formalised methodology).")

C("src-powell-2022-ubatuba-isotope", "src-nolan-vallee-2022-isotopic-aerospace-forensics",
  "grey-lit-precursor-of", direction="directed",
  description="SCU 2022 grey-literature Ubatuba isotope re-analysis is paired with the Nolan/Vallée 2022 PiAS peer-reviewed methodology frame for the same instrument-class isotopic workflow.")

