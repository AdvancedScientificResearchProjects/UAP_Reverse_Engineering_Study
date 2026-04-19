# Chernobrov — *Путешествия во времени: миф или реальность?* (2001/2002) — PART 2 of 4

**Source:** `books/downloads/fb2_chunks/PV-01_part2of4.txt`
**Effective source:** `books/downloads/fb2_text/527877_Puteshestviya_vo_vremeni.txt`
**Source code:** `PV-01-p2` → merge bucket `B-PV01`
**Bibliographic ID:** Chernobrov V.A., *Путешествия во времени: миф или реальность?* — М.: Олимп / АСТ-ЛТД, 2002 (signed to print 2001). ISBN 5-17-005519-5.

> **Extraction note (chunking artifact).** The raw file `PV-01_part2of4.txt` is a naive byte-slice of the source FB2 and falls **entirely inside a concatenation of base64-encoded cover/illustration `<binary>` blocks** (52 embedded images). It contains **zero book prose**. All actual book text in the FB2 ends at byte 1,966,404 (`</body>`) — well inside part 1. This extract therefore covers the **logical second quarter** of the book body (characters 261,705 – 523,428 of the decoded text `527877_Puteshestviya_vo_vremeni.txt`, i.e. the 25–50% slice of real prose). Chapters covered: tail of *«Страх потеряться во Времени»*, *«Машина времени и фальсификации»*, *«Образ путешественника»*, *«Хрононавигация»* (polety в Прошлое and Будущее), *«Этика вмешательства»*, *«Цели полетов»*, *«Цикличность Времени и Истории»*, *«Бифуркационные точки»*, *«Правила движения во Времени»*, start of *«Будущее Время»*, *«Предсказания извне»*, *«Периодическая проскопия»*, *«Проскопия перед катастрофами»*, *«Что чувствовали люди во время видений Будущего»*.

> **Audit scope.** Pre-theory/narrative material (focus topics in the source task). This chunk is light on device claims (no "Лабораторий Астра", no "Космопоиск", no MV-generator specs) and heavy on historical/anecdotal "time-anomaly" case studies and Chernobrov's own prescriptive framework ("Правила движения во Времени"). Those cases — and the *Правила* document itself — ARE new technical/normative claims proper to this book and are captured below. Device-spec material for this book appears later (parts 3-4 body) and in part 1 (already covered).

---

## 1. ТАКСОНОМИЯ / ТЕРМИНОЛОГИЯ / TAXONOMY (Chernobrov's own)

### 1.1 Determinologization block from "Правила движения во Времени (Проект)" §1.2
Chernobrov formalises his operational vocabulary here for the first time in book form (dating the terms):

**RU (verbatim):**
> «1.1. Настоящие Правила движения во Времени устанавливают единый порядок хроноперемещений, хронопортаций и хроновмешательств для всего человечества во всем объеме нашего Пространства-Времени. […] 1.2. В Правилах приняты следующие основные понятия и термины.
> **Дисторсия** — искаженное восприятие пилотом течения времени. По мнению американских авиационных врачей, данное явление приводит к тому, что гибнет около 20 % всех летчиков, не сумевших или не успевших вовремя катапультироваться.
> **MB (машина времени)** — управляемый транспортный аппарат для перемещения в физическом Времени. (Термин введен Г. Уэллсом в 1885 году, аббревиатура введена автором правил в 1985 году.)
> **Хрононализм** — проявившиеся в последнее время взгляды на нашу реальность и наше Время, наш вариант развития Истории и наше Прошлое как нечто единственно возможное и единственно существующее. […] Самым известным приверженцем хрононализма был физик С. Хокинг, однако в конце 1995 года он поменял свою точку зрения на противоположную. (Термин введен в 1999 году автором правил.)
> **Хронопортация** — мгновенное или очень быстрое перемещение во Времени.»

**EN paraphrase:** Chernobrov's 2001 "Code of Time-Movement Rules" defines four terms. (a) *Distorsion* = pilot's distorted perception of time flow; he asserts US aviation physicians attribute "about 20%" of non-ejecting fighter-pilot deaths to it. (b) *MV* (машина времени) = "controlled transport apparatus for movement in physical Time"; he credits Wells (1895, mistakenly rendered "1885") with the term and **claims he himself coined the Cyrillic abbreviation "МВ" in 1985**. (c) *Chrononalism* = the dogma that our history/past is unique/unchangeable; "term introduced by author of rules in 1999"; Chernobrov claims Stephen Hawking held this view until "end of 1995" when he reversed it. (d) *Chronoportation* = instantaneous/very-fast transit.

> **Instrument / figure reference embedded in text:** "Рис. 35. Сфера применения перспективных полевых летательных аппаратов" — a log-log diagram of размер vs скорость летательного аппарата (ось скоростей до "с" = скорости света) is inserted in this chapter. No numerical scale beyond the decade labels `10¹ … 10¹⁰` and `0,01 / 0,1 / c` is given.

### 1.2 Operational rules — 7 normative clauses
**RU (verbatim, condensed to clause cores):**
> «1.4. Участники хронополетов должны действовать таким образом, чтобы не создавать опасности для движения и не причинять вреда друг другу, обитателям своего и иного Времени, жителям параллельных миров, не изменять естественный ход течения Истории, не оказывать никакого давления на сторонников или противников хрононализма, не предоставлять им никаких сведений и не оставлять никаких значимых следов в ином Времени.
> 1.5. При встрече двух или более MB в каком-либо физическом Времени и/или параллельном мире контакт между ними запрещен — за исключением случаев, когда один из встретившихся подает сигналы бедствия. Преимущественным правом на беспрепятственный проезд (пролет) пользуется та из двух MB, которая движется в направлении из Прошлого в Будущее.
> 1.5.1. При встрече в ином Времени с MB или пилотом MB, не подающим признаков жизни, участники хронополетов обязаны сделать все для выяснения степени дееспособности встреченного экипажа. […] В случае обнаружения в ином Времени исправной MB с дееспособным экипажем обнаруживший их обязан, не вступая с ними в контакт, удалиться на безопасное расстояние в Пространстве и/или Времени.
> 1.5.2. В случае обнаружения погибшего экипажа и/или неисправной MB участники хронополетов обязаны отвезти тела и отбуксировать эту MB в Настоящее Время (точку старта); если это невозможно — замаскировать тела и MB; а если и это невозможно — уничтожить их, сделав все, чтобы они не попали в руки аборигенов.
> 1.6. При появлении дисторсии или возникновении иных признаков потери ориентации во Времени пилоты MB обязаны прекратить все виды операций во Времени за исключением тех, что направлены на восстановление ориентации.
> 1.7. При встрече двух или более MB, часть из которых находится в режиме обычного полета во Времени, а часть — в режиме мгновенной хронопортации, преимущество в движении отдается хронопортируемым аппаратам.
> 1.8. Всякое значительное хроновмешательство должно быть заранее согласовано с рассчитывающим центром через хроноинспекторов или напрямую. […] 2. […] (Настоящие Правила составлены в 1991—2001 годах.)»

**EN paraphrase:** Seven prescriptive clauses. §1.4 = no harm, no information-leak, no history-change. §1.5 = no inter-MV contact except distress; right-of-way to the MV moving *Past→Future*. §1.5.1 = dead/unconscious crew → rescue; healthy crew → retreat without contact. §1.5.2 = recovered dead/disabled MV → tow to start-point; failing that, hide; failing that, destroy so aborigines can't obtain. §1.6 = if distorsion onset, suspend all operations except re-orientation. §1.7 = in mixed encounters, chronoporting MV has right-of-way. §1.8 = any significant interference must be pre-cleared with a "computing centre via chrono-inspectors". §2 = "Rules drafted 1991–2001."

> **Audit value:** This is the most explicit normative document Chernobrov attaches his own authorship to; it contains no physics but establishes his self-assignment as *legislator* of the protocol. It pre-dates (by 5–10 yrs) similar soft-law speculations in Western TT literature. The 20% aviation-distorsion figure is unsourced.

### 1.3 Other taxonomic novelties in this chunk
- **"Случайная проскопия"** vs **"периодическая случайная проскопия"** vs **"проскопия перед катастрофами"** — Chernobrov's tripartite classification of precognition.
- **Four-way classification of "predictions"**: (1) ложные/шарлатанские; (2) правдивые тайные (concealed → sbudutsya); (3) правдивые зашифрованные (sense only post-event → no influence); (4) implied fourth class — правдивые открытые which influence history and thereby fail to sbyvayutsya.
- **"Бифуркационные точки Времени"** — historical-branching nodes where parallel-universes diverge; borrowed from math (`bifurcus` = two-pronged) and applied to the history of Russia/Tamerlane.

---

## 2. ТЕМПОРАЛЬНЫЕ АНОМАЛИИ / CASE STUDIES / TIME ANOMALIES (dated, placed)

### 2.1 Roman-Moscow 1700-year coincidence (Chudakov 'spiral of time')
**RU (verbatim):** «московские исследователи Наталья и Сергей Чудаковы. Анализируя случаи, происходившие с именитыми двойниками, они заключили, что "двойники могут встречаться в истории только через определенные периоды времени". По их представлениям, шаг, который разделяет точки спирали времени, находящиеся на соседних витках, равняется 1700 годам (как в случае с Цезарем и Петром I).»

**EN:** Muscovite researchers N. and S. Chudakov posit a "time-spiral step" of exactly **1,700 years** between "twin" historical figures (Caesar ↔ Peter I the chief example). Chernobrov refines their step claim with an Atlantis→Hiroshima "vselenskaya nedelya" (universal week) of 11,500 years (1 ≈ 9,500 BCE → 1945 CE).

### 2.2 Chizhevsky 11-year solar-activity ↔ history cycle
Cited as the base periodicity: «Выведенный им период в 11 лет довольно близок к 12-летнему циклу восточного календаря […] Как заметил еще А. Чижевский, все основные катаклизмы и войны за тысячи лет регулярно случались и случаются с периодичностью в среднем раз все в те же 11 лет». Chernobrov expressly *inverts* Chizhevsky: events are not Sun-driven, but — he suggests — driven by a *periodic density of time-visitors* from the future whose visits correlate with the 11-yr UFO-sighting rhythm:
- Cited UFO-activity peaks: **1908; 1946–1947; 1953–1954; 1967–1968; 1977–1978; 1989–1990** (periods 8–12 yrs).
- Hlebnikov's own "12-yr cycle of Russia": 1905; 1917; 1929; 1941; 1953; 1965; 1977; 1989; 2001(?).

### 2.3 The 26 August coincidence cluster (Russia)
**RU (verbatim):** «26 августа 1381 года хан Тохтамыш взял Москву, а 26 августа 1395 года Тамерлан, шедший на Москву, внезапно повернул назад. 26 августа 1612 года войско гетмана Ходкевича […] было разбито ополчением Минина и Пожарского […] 26 августа 1812 года […] Бородинская битва […] 26 августа 1831 года российские войска генерал-фельдмаршала И. Паскевича взяли мятежную Варшаву».

### 2.4 Exhumation of Tamerlane → onset of WWII (Samarkand-June-1941 legend)
The block in §"Бифуркационные точки" reframes the "если вскроют могилу Тимура, случится великая из войн" legend as a documented bifurcation-point. No date for the exhumation is given in this slice; Chernobrov only asserts the warning existed among contemporaries of Tamerlane (d. 1405).

### 2.5 UFOs observed at historic moments
- 1989, **1-й Съезд народных депутатов** — UFO alongside Kremlin Palace of Congresses.
- **октябрь 1990**, Kiev, Площадь Октябрьской революции — UFO over hunger-strike of students/deputies demanding resignation of Ukrainian SSR Sovmin chairman.
- «неопознанные объекты висели над полями великих сражений» (unsourced cluster claim).
- Proximity-to-prototype claim: «Многие из HJIO находились вблизи экспериментальных образцов космических кораблей, самолетов, ракет».

### 2.6 Periodic UFO-revisits (same location, regular interval)
**List with places + dates (verbatim transcription of Chernobrov's enumeration):**
«в феврале 1913 года над Торонто (Канада); в 1950-м — над Фармингтоном (штат Нью-Мексико, США); в 1950-м — на Колыме (СССР); в 1956-м … в 1977-м — на Новой Гвинее; в 1977-м — в провинции Уэска (Испания); в 1982—1983 годах — в Жирновске (Волгоградская область, СССР); в 1986-м — в Старой Полтавке (Волгоградская область, СССР); в июле—декабре 1989-го — в деревнях Нестерка и Латыголь; в октябре—декабре того же года шарообразные объекты — в Дубровке, Кумельщине и Стешинах (Вилейский район, Белоруссия, СССР); над Ладожским озером (Ленинградская область); в апреле—июле 1996-го в Измире (Турция); в апреле 1997-го — в деревне Никитино (Псковская область); в 1998-м — в Свеклино (Псковская область)».
> Sources: «НЛО», 1990 № 1 с. 8; «НЛО», 1997 № 4; 1999 № 23.

### 2.7 Andrei Reutov case (Russian "chronodouble" story, undated)
A 17-year-old Russian, Andrei Reutov, killed when their truck overturned; an unrelated boy who had joined the party and looked exactly like Reutov «исчез бесследно»; from 1987–1991 Reutov's father allegedly saw his son flying in "on a UFO" landing near the house, observed also by neighbours; re-investigated from June 1997 by Kaluga researcher **Андрей Перепелицын**.

### 2.8 "Titanic" precognition complex
- 1898, М. Робертсон, new. *«Тщетность»* — predicts "Titan" iceberg sinking.
- 1896, М. Чиел, «СС» — earlier mutation-crime novella.
- 1912 *Titanic* matches the novella in: April collision, "непотопляемость"-hype, celebrity manifest, insufficient lifeboats.
- 1939 *Titanian* (27 yrs later): in same region, rudder on hunch orders "стоп-машина", avoids iceberg.

### 2.9 Lincoln-Kennedy coincidence set
Verbatim itemisation in Chernobrov's text: both elected exactly 100 yrs apart (1860/1960); both shot from behind, in the head, on Friday, in front of their wives; Lincoln in Ford's Theatre / Kennedy in a *Lincoln* made by *Ford*; both surnames 7 letters, full names 13; Lincoln's 1859 candidacy letter in "Cincinnati Gazette" mentioned a "John Kennedy" (then acting Navy Secretary); Dallas-issued dollar bill "two weeks before" JFK's murder has serial letter "K" (Dallas is the 11th FRB district). Sources: «Свет» 1996 № 8, с. 60–61; «Правда» 1996, 6–15 декабря.

### 2.10 Tarkovsky precognition cluster (Chernobrov's preferred case)
- **Лето 1952** — геологическая экспедиция под Енисеем; Tarkovsky spent night in a сторожка, thrice heard disembodied voice «Уходи отсюда!» (cited from «В. Куриленко»).
- **1986** — Стокгольм: filming location-scouting for *Жертвоприношение*, Tarkovsky stopped car in an area and stated "Вот место катастрофы"; "несколько месяцев" later Olof Palme was assassinated on that exact spot.
- *Сталкер* (1979): "Зона" вокруг "4-го бункера" → **6 years later** Chernobyl accident at reactor block 4.
- Same film: operator held shot of drowned calendar page **"28 декабря"** — "много лет" later proved to be Tarkovsky's own death date.
- Wife Larisa died «на той же койке, в той же палате, в той же больнице, в тот же час, от той же болезни»; buried at Sainte-Geneviève-des-Bois, Paris. Source: NTV, 23.01.1998.

### 2.11 Ayback Tleukhanov (1991)
19-year-old Kazakh painter Айбек Тлеуханов, «за четыре месяца до своей смерти от гангрены в 1991 году», depicted on his canvases both the cause of his fatal infection (nail in knee) and "время смерти".

### 2.12 Fatima — 13 October 1917
«13 октября 1917 года на поле возле Фатимы собралась многотысячная толпа, приехал сам Папа Римский. Наконец пришествие началось, все собравшиеся отчетливо видели прилетевший с неба странный аппарат, по описаниям весьма похожий на классическую летающую тарелку! От аппарата исходил сильный жар, настолько сильный, что одежды, промокшие под неутихающим дождем, очень быстро просохли».
> Chernobrov treats Fatima as a classic UFO-prediction event rather than a religious one; warns the "Russian revolution" content of the 3rd Fatima secret may be anti-Soviet forgery.

### 2.13 Tushino / Fedorov helicopter crash — 2 June 2000
**RU (verbatim):** «2 июня 2000 года в 100 метрах от Тушинской детской больницы в Москве разбился на вертолете знаменитый хирург-офтальмолог и политик Святослав Николаевич Федоров. Его многие отговаривали лететь в командировку на своем вертолете "Газель" (французкая разработка 1967 года) в не столь уж далекий Тамбов; многим, как выяснилось позже, снились странные аллегорические сны.» Source: «Комсомольская правда», 2000, 20 июня, с. 12.

### 2.14 Il-76 Astrakhan — 21 June 2000
«21 июня 2000 года у военного транспортника Ил-76, перевозившего 220 дагестанских призывников, после промежуточной посадки в Астрахани стало неожиданно отказывать оборудование. Героический экипаж из 11 человек во главе с Андреем Зеленко с огромным трудом посадил уже горящую машину с полными баками. Самолет взорвался и сгорел, но выскочить из дверей и спастись успели все.» Reported pre-boarding refusal/reluctance by призывники — Chernobrov frames as *mass distributed precognition*.

### 2.15 Булунгу (Кабардино-Балкария) selevoi stream
In a total-destruction mudslide, «погиб всего один человек и несколько коров» because the majority of villagers had left the day before for pastures, weddings, deliveries. Commission chairman **полковник Владимир Шилин**: «Я не могу поверить в счастливый случай. Видимо, Христос, или Аллах, или кто-то другой простер над ними свою руку».

### 2.16 Logan Airport "Majestic" crash — Stephen King follow-up to D. Staunton
Chernobrov reproduces King's phone-survey of the airline:
- 16 ticket-holders failed to board (normal absentee rate ≤3 on Denver–Boston line).
- 15 additional cancellations (normal ≤8).
- Headline "94 dead" could have read "31 spared".
- Staunton's ground-truth statistic (pre-ECM computer-reworked): **catastrophe-fated** transport averaged **61% occupancy** vs **76%** on sister safe flights → 15-point differential across years.

### 2.17 Churchill 1941 PVO car incident
«В 1941 году Черчилль после очередной проверки батарей ПВО вернулся к своей машине и хотел сесть на свое привычное место — переднее сиденье. Но вдруг его что-то остановило, и он сел сзади.» (Front-seat would have been hit by bombing.)

### 2.18 Mendeleev periodic-table dream
Used as the locus classicus of "sonnoye nauchnoye otkrytie" — direct claim: «Дмитрий Иванович Менделеев сделал свое открытие Периодической системы химических элементов именно во сне. […] Менделеев одновременно сделал два открытия — в химии, а также в теории и практике изобретательства».

### 2.19 Aleksandr S. Pushkin / декабрь 1825 hare omen
«В декабре 1825 года поэт Александр Сергеевич Пушкин, который никогда не скрывал своей веры в приметы и предсказания, выехал из села Михайловского на встречу со своими друзьями-декабристами. Но путь ему неожиданно перебежал заяц. […] И Пушкин решил вернуться.» Framed as a survival event preventing his presence at 14 Dec 1825 uprising.

### 2.20 Rasputin / Vyrubova diary prophecies
Two dated entries transcribed verbatim from the Vyrubova court diary:
- **Март 1913**: "From my death — 25th year" (died 1916 → 1916 + 25 = **1941**, invasion of USSR).
- **Февраль 1916**: "видит остров и два города — и нет городов, и нет людей. Были, говорит, и в огне сгорели. […] япошек Бог не помилует" (≈30 yrs → Hiroshima/Nagasaki 1945).

### 2.21 Vanga Gushterova
«болгарская ясновидящая Ванга, предсказавшая президенту США Джорджу Бушу развод с женой и взрыв его самолета в 1990 году.» Chernobrov lists the *error* as the anchor year. Baba Vanga (Гущерова Вангелия Пандева) died 1996.

### 2.22 Sidik Afghan
Quoted alongside Vanga as a (pre-1990) reliable date-predictor who then failed in 1990.

### 2.23 Bakhtin 1818 voice-prediction brochure
«В 1818 году в Петербурге из-под пера вольнодумца, общественного писателя, статского советника Ивана Ивановича Бахтина (1754—1818) вышла брошюра "Вдохновенные идеи"». Chernobrov quotes Bakhtin's self-description of hearing an "тихий, но внятный и, я бы сказал, упрямый голос, не раз возвещавший мне день и обстоятельства событий, которые должны были произойти".

### 2.24 Andrey Tarkovsky's mentor + Soloviev
Cited inline: Соловьёв В., *Творения Платона*, М., 1899; Блон Ж., *Великий час океанов* (Atlantic), М., 1978, с. 80.

### 2.25 Hitler-astrology "ефрейтор Шикльгрубер" intuition
Chernobrov claims Hitler started receiving "прямо в голову малопонятные приказы" in WWI that "saved his life in combat", and credits a possible "inner voice" for his later tactical successes vs professional generals. Framed as a "dark-side precognition" case.

### 2.26 Kovalevsky / Joan-of-Arc precognition typology
Cited source: Ковалевский П.И. (Pavel Ivanovich, 1849–1923), Russian psychiatrist — classifies Joan-of-Arc's "dar predvideniya i predchuvstviya" as a form of hyperaesthesia in "neurasthenic types".

### 2.27 Vladimir Safonov (parapsychologist, Moscow)
Self-reported: «перед поездкой на железнодорожный вокзал "просто сосредоточился"... и увидел всех своих будущих попутчиков по купе».

### 2.28 Сэргэлэн (Хубсугульский аймак)
«монгольская ясновидящая Сэргэлэн, последняя из рода шаманов Хубсугульского аймака, просто "знает", что умрет через 28 лет». (Counted as precognition of own death.)

### 2.29 "Реванш России" (Россич, 1997) — failed Yeltsin death forecast
«Святослав Россич (вероятно, псевдоним) предсказывал смерть президента России на 17.12 вечера 14 марта 1997 года».

### 2.30 9 March 1997 "Жигули" solar-eclipse scare
K. Ashirov (academic, д. геол.-мин. наук) + T. Borgest (Samara): lunar-tidal wave would trigger earthquake in Zhiguli, collapse of the Volga HPP dams, tsunami down to Caspian. Publicised → panic in cities south of Samara; Chernobrov personally appeared on Saratov TV (editor L. Baranova) to calm the public. Forecast failed.

### 2.31 Hokkaido 1992 "Gay-Maya capsule" hoax (fallback case)
Alleged 1999 dispatch of "доктор Ричард Мейсон Перел" via time machine for 25 minutes backward to 1918; body reportedly found in "Нью-Йорк полис курьер" dated **26.02.1918** as "Таинственный мужчина обнаружен мертвым в капсуле"; capsule "первоначальный размер которой составлял 12 метров" allegedly compressed in transit — crushing Perel. Chernobrov debunks this as unverifiable (no trace of the paper or of Perel).

### 2.32 Nizhny-Novgorod MV hoax — 1998
«В 1998 году большое хождение в прессе и Интернете получили перепечатки или ссылки на сверхсенсационное сообщение об испытаниях машины времени в Нижнем Новгороде, в котором участвовал известный популяризатор науки Альберт Абрамович Валентинов.» Chernobrov called Valentinov, who admitted it was a joke; Valentinov also interviewed **Козырева** and reviewed work of "других исследователей".

### 2.33 "Буэнос-Айрес 130-местный самолет" hoax — 1999
Urban-legend account of a burning 130-seat aircraft en-route Buenos Aires that "выровнялся сам", later claimed to have landed in an impossible time-slipped airport. Chernobrov marks it as fabricated.

### 2.34 Gay-Maya 1992 hoax (Sabittini / Benavides)
«В 1992 году археологи Жозе Сабиттини и Аугут Бенавидес поведали миру о своей находке в гватемальских джунглях. […] Небо над джунглями приобрело ярко-фиолетовую окраску». Cited to польская газета «Скандаля». Chernobrov's own search for the authors failed.

### 2.35 Yuri Nikitin "Царские забавы" — Peter-Gorbachev zerkal'nost'
Saratov writer Nikitin: Russian/Soviet rulers are split into two hunter-averse cases (Феодор Алексеевич Романов 1661–1682; Михаил Сергеевич Горбачёв, р. 1931) separated by exactly three centuries. Parallels: rule 6 yrs; under strong female influence; teetotallers; fought privileges; amnestied dissidents; ended reign in smuta. Nikitin's extrapolation: next such ruler ≈ XXIII century. Source: «Комсомольская правда», 1998, 22 мая, с. 6.

### 2.36 Hlebnikov 1885–1922 cycle-of-Russia
Hlebnikov (self-styled time-traveller) "рассчитал цикл жизни России — СССР на 'основании божественного видения'" — a 12-year periodicity later matched by 1905/1917/1929/1941/1953/1965/1977/1989/2001.

### 2.37 The Stalingrad/Leningrad mirror (1943↔1944)
«В январе 1943 года была прорвана блокада Ленинграда, а в феврале закончилась ликвидация группировки войск под Сталинградом; ровно через год, 27 января 1944-го, была окончательно снята блокада Ленинграда, а 17 февраля 1944-го ликвидирован окруженный "котел" на Украине.»

---

## 3. ИНСТРУМЕНТЫ / DEVICE-ADJACENT CLAIMS / INSTRUMENTS

> This chunk is **essentially devoid of laboratory hardware specs**. What appears is diffused through Chernobrov's fictional framings and is listed here for audit completeness; it is NOT first-hand equipment description.

### 3.1 "Машина / Лаборатория / Энергоотсек" — fictional narrative
Embedded inside a short-story-style frame (the chapter fragments *«Шрам на спине»*, *«Временный маятник»*). The narrator describes a lab with:
- **красная кнопка** opening a cellophane-wrapped "пистолет Макарова" from a retractable shelf
- a control panel with many пульты and information displays
- "энергоотсек за стенкой" — a "batareya moschnykh generatorov" whose winding-down is audible
- "stretched" priborovyye striki that settle on "ograniliteli"
- circuit "zapas raschet­noy prochnosti 'semerku'" → max 10–12 "tsiklov kolebaniy" before "perogeraniye" (burn-out)
- power-fed MV that, when the "rubil'nik" at the lab is not pulled, creates a "маятник-поглотитель" — a self-reinforcing chain sucking the pilots back into repeated loops.
**These are narrative-grade descriptions, not calibrated equipment specs.** Audit classification: *literary*, not *technical*.

### 3.2 Figure 35 (see §1.1 above)
Log-log plot: abscissa = craft speed (0.01 … c); ordinate = size (10¹⁰ … 10⁻¹). Unscaled. "Сфера применения перспективных полевых летательных аппаратов." No device identified.

### 3.3 20% aviation-distorsion fatality figure
Attributed only to "American aviation physicians" — no citation.

### 3.4 Absence of expected references
- No mention of **Лаборатории "Астра"** in this text slice (the two "Астра*" hits refer to "astral warriors" and "Astrakhan").
- No mention of **Космопоиска** in this slice.
- No mention of **МВ-2 / МВ-3** generator designations.
- No mention of **Бартини**, **Козырева** device specifics (only Valentinov's interview, passing).
- No mention of **Николаев Б./Н.** experiments (only "С.Н. Фёдоров" surgeon).
- No MRI/NMR, no ampere/volt, no solenoid numbers.

---

## 4. ПРИСВАИВАНИЕ АВТОРСТВА / PRIORITY CLAIMS (by Chernobrov himself)

| Item | Claim | Date stamped by Chernobrov |
|------|-------|----------------------------|
| Cyrillic abbreviation **МВ** | "аббревиатура введена автором правил" | **1985** |
| Term **хрононализм** | "термин введен в 1999 году автором правил" | **1999** |
| Text of "Правила движения во Времени" | "составлены" | **1991–2001** |
| Operational classification of precognition (случайная / периодическая / предкатастрофная) | Implicit authorial framework | 2001 edition |

---

## 5. CYCLE TABLE (Chernobrov's own assembly of candidate "fundamental periods")

Quoted verbatim from his "цифры, названные" list:

> «минутные: 14 минут (или, другими словами, это — "цикл[...]"; […]»

Continues on the body side as:
- 532 years = 28×19 = **1 Indikton** = Великий Пасхальный круг; 410 years (Fomenko shift).
- Millennial scale: 1; 1.7; 2.2; 2.5 (Club catastrophe cycle); 10.5; 10.8; 11; **11.76** (Chudakov spiral cycle); 21; 25.91 (Earth axis); 220 (galactic year); 614; 617 (Manu); 8640 (mahaYuga) tys.
- Mega-scales: 11 mln; 13; 34; 35; 56; 70; 217 (cycles **Ефремова–Заколдаева–Шпитальной**); 8600 (Krishna-day-of-Brahma); 8640 (Kalpa); 100 000 000 – 400 000 000 mln (kalachakra).

> **Audit value:** This is Chernobrov's most comprehensive taxonomy of conjectured cosmic periods in the 2001 book; it cross-references (a) **Chizhevsky** (11 yr); (b) **Fomenko** (410 yr, dismissively); (c) **Chudakov spiral** (11.76 tys); (d) **Ефремов / Заколдаев / Шпитальная** composite cycles (megatys). None come with the reasoning that would elevate them from numerology.

---

## 6. METHODOLOGICAL SELF-STATEMENTS (verbatim)

### 6.1 On fabrication-filtering
«За годы сбора информации о таинственных происшествиях, связанных с фокусами во Времени, я конечно же не раз сталкивался с сомнительными сообщениями. При явной дезинформации откидывал такие истории сразу, а иногда — после долгой или быстрой (как получалось) проверки фактов. Что греха таить, некоторые, казалось бы, "наиправдивейшие истории", как выяснилось, были выдуманы частично или полностью.»

### 6.2 On the Valentinov call-back
«при появлении слухов я просто позвонил ему. Оказалось — журналист просто пошутил, еще раз доказав, как легко можно "купить" СМИ...» — Chernobrov asserts personal telephone verification of at least one major 1998 media hoax.

### 6.3 On epistemic humility about prophecy vocabulary
«Все их инструкции будут сводиться в конечном счете к простой фразе: "Идите и смотрите!"»

---

## 7. MISCELLANEOUS DATED STATEMENTS

- Rome → Third Rome (Moscow) parallel set; Caesar ↔ Peter I (1700-yr spiral).
- Year-of-Snake smuta rule: 1605, 862 (unreliable), 1689; Pugachev; author adds "год выхода этой книги — тоже год Змеи…" → dating the book to a **year of the Snake = 2001** (Eastern calendar), confirming publication intent.
- Ocean-floor toxic-container projection: "Океаны ежегодно за счет переработки грунта морскими грунтоедами […] опускаются на 1 см. Если толщина стенок контейнеров 1 метр, несложно подсчитать, что грунтоеды за 100 лет разъедят стенки смертельного контейнера, и к **2050—2070 годам** жизнь в Мировом океане будет уничтожена". (Cited as В. Шемщука's hypothesis about Atlantean self-destruction via bio-war.)
- Atlantis-weapon parallel: "11.5 тысячелетия (т. е. через 1 вселенскую неделю) […] в 1945 году, две атомные бомбы взорвались также в островном государстве, в городах Хиросима и Нагасаки".
- Alexandria library → Byzantium → Moscow transfer; "библиотека Ивана Грозного / государева Либерия" still sought; "213 году до н. э. император Китая Цинь Шихуанди приказал сжечь книги".

---

## 8. CROSS-REFERENCE MAP (against §3 of 03_user_provided_research_2026-04-18.md)

| Target §3 topic | In this chunk? | Chunk locus |
|-----------------|----------------|-------------|
| Лаборатории "Астра" | **NO** (absent) | — |
| Космопоиск | **NO** (absent) | — |
| MV-2 / MV-3 generator | **NO** (narrative generator only) | §3.1 |
| 1989 Сторожевое / ВВС-inst. case | **NO** | — |
| Козырев instruments | Passing mention only (Valentinov interviewed Kozyrev) | §2.32 |
| Chizhevsky 11-yr cycle | **YES** | §2.2 |
| Fomenko 410-yr shift | YES, dismissive | §5 |
| Chudakov 1700/11760-yr spiral | **YES** | §2.1, §5 |
| Tarkovsky precognition cluster | **YES** | §2.10 |
| Rasputin/Vyrubova | **YES** | §2.20 |
| Fatima 13.10.1917 | **YES** | §2.12 |
| Titanic / Titan / Titanian | **YES** | §2.8 |
| Lincoln↔Kennedy | **YES** | §2.9 |
| Staunton/King 61% occupancy rule | **YES** | §2.16 |
| Il-76 Astrakhan 21.06.2000 | **YES** (fresh for 2001 edition) | §2.14 |
| Fyodorov 02.06.2000 crash | **YES** (fresh for 2001 edition) | §2.13 |
| Rules of MV (Правила движения во Времени, 1991-2001) | **YES — novel book-grade primary document** | §1.1–1.2 |

---

## 9. AUDIT FLAGS

1. **Primary-source status of "Правила":** This is Chernobrov's most durable doctrinal text, drafted 1991→2001. It is *his normative doctrine*, not a physics claim, and should be logged as **policy/manifesto** under B-PV01 rather than as an instrument claim.
2. **Distorsion "20%" figure:** Unsourced in-text. No aviation-medicine citation. Flag as **unsupported**.
3. **Claimed personal coinage of МВ (1985) and хрононализм (1999):** No corroborating contemporaneous documentation in this chunk; verify against part-1 and against Kosmopoisk bulletins of 1985/1999 for independent confirmation.
4. **1998 Valentinov "Нижний Новгород MV" hoax:** Chernobrov takes credit for personally debunking it. Primary-source-grade journalistic claim — verifiable against *Российская газета* archives.
5. **61% / 76% occupancy statistic (Staunton/King):** Secondary quote of secondary quote. No primary Staunton publication cited.
6. **Alleged 12-m time-machine capsule, Perel, NYC 1918:** Explicitly debunked by Chernobrov as impossible to verify — should **not** be indexed as a factual capture case.
7. **Булунгу mudslide rescue:** Transcribed quote of commission chairman "V. Shilin" — ostensibly verifiable; no date given in this slice.
8. **Absent device specs:** Any reader seeking the *physical Machine* material should go to parts 3–4 body (if preserved in the byte-split; otherwise to the full `527877_Puteshestviya_vo_vremeni.txt` after char 523,428).

---

## 10. BIBLIOGRAPHY CROSS-LINKS IN SLICE

- Уэллс Г., *Машина времени*
- Азимов А., *Бессмертный*
- Сильверберг Р., *Наковальня времени*, М.: Вече, 1993
- Нортон А., *Поиск на перекрестке времен / Поиск во времени*, М.: Джокер, 1993
- Андерсон П., *Коридоры времени*, СПб.: Северо-Запад, 1993
- Кинофильм *Терминатор* (США)
- Кинофильм *Назад в будущее*
- Скрыгин Л., *Считаются пропавшими без вести*, М.: Современник, 1996
- Ковалевский П.И., *О сумасшествии* etc.
- Монтень М., *Опыты*, кн. I–II, М.: Наука, 1980, с. 44
- Соловьёв В., *Творения Платона*, М., 1899
- Блон Ж., *Великий час океанов (Атлантический)*, М., 1978, с. 80
- *Комсомольская правда*, 1998 22 мая с. 6; 2000 20 июня с. 12
- *Правда*, 1996 6–15 декабря
- *Свет*, 1996 № 8 с. 60–61
- *НЛО*, 1990 № 1 с. 8; 1997 № 4; 1999 № 23
- *Мир* (Волгоград), 22.02.1993, с. 2
- *Наука и жизнь*, 1996, № 11, с. 96
- NTV, 23.01.1998 (Tarkovsky obituary context)

---

*End of PV-01 Part 2 extract.*
