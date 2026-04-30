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
