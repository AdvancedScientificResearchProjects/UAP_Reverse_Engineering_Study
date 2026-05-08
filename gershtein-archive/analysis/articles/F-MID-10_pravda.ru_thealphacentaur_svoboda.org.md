# F-MID-10 — Pravda.ru tag-page + Radio Svoboda Subbotnee Interview + TheAlphaCentauri video index

**Subject:** Mikhail Borisovich Gershtein (b. 1972), Russian ufologist, last chairman of the UFO Commission of the Russian Geographical Society (St-Petersburg branch).

**Source files:**
1. `articles/sources/pravda.ru__tags_mikhail-gershtejjn.html` (52,801 bytes)
2. `articles/sources/svoboda.org__a_24188032.html.html` (82,548 bytes)
3. `articles/sources/thealphacentauri.net__163377-d0b2d0bed0b5d0bdd0bdd18bd0b5-d181d0bad180d18bd0b2d0b0.html` (144,074 bytes)

**Source codes:** `F-PRAVDA-TAGS`, `F-SVOBODA-2011`, `F-ALPHA-VOENNYE`

**Assembly note:** Three independently-recoverable web items, ranging in date from 2003 to 2025. Of the three, **F-SVOBODA-2011 (actually an interview transcript dated 31 May 2003)** carries the bulk of substantive verbatim content — a full conversation with Mikhail Gershtein conducted by Olga Pispanen (presenter Andrey Trukhan). The AlphaCentauri page is essentially a video-description page (chapter timestamps + short blurb) for a 2025 interview hosted on the popular-science portal; the page itself does not contain interview text, only a chapter index. The Pravda.ru page is a tag/biographical landing page listing tagged articles — only one substantive article tile is present.

**Date discrepancy on Svoboda:** The task brief refers to the Svoboda interview as «from 2011», but the page metadata explicitly reads **«31 мая 2003»** (`time datetime="2011-12-30T..."` at the page footer is the *page-archive* timestamp; the published-on date inside the body is 31 May 2003, and the section labeled «Архив 1997-2004» on the page also confirms early-2000s vintage). All extracted claims below are attributed to the *interview content* (2003), with the archive-page timestamp from RFE/RL noted as 2011 only as a republication marker. No verbatim text contradicts a 2003 origin.

---

## 0. Recoverable surface metadata

### 0.1 Pravda.ru tag-page (`F-PRAVDA-TAGS`)

| Field | Value |
|---|---|
| URL | `https://www.pravda.ru/tags/mikhail-gershtejjn/` |
| Page title | «Михаил Герштейн. Последние новости на сегодня» |
| Page type | Tag landing page (Schema.org `Person` + tagged-articles list) |
| Created | 2021-08-29T18:59:46Z (Schema.org `dateCreated`) |
| Tagged articles displayed in capture | 1 (Pyramids piece by А. Артамонов, 2017-09-27) |
| Editorial blurb (lines 398–408) | Biographical sketch of Gershtein (verbatim quoted in §1 below) |
| Description (meta) | «Михаил Борисович Герштейн — учёный-уфолог, журналист, писатель.» |
| Publisher | ООО «Техномедиа», Pravda.Ru |
| Paywall / login-wall | None — page is publicly served |

### 0.2 Radio Svoboda interview (`F-SVOBODA-2011`)

| Field | Value |
|---|---|
| URL | `https://www.svoboda.org/a/24188032.html` |
| Page title | «Субботнее интервью. Михаил Герштейн» |
| Programme | «Субботнее интервью» (Saturday Interview) |
| Presenter | Андрей Трухан (Andrey Trukhan) |
| Interviewer | Ольга Писпанен (Olga Pispanen) |
| Subject | Михаил Герштейн |
| Published date in body | **31 мая 2003** (line in page body) |
| Page-archive note | «Архив 1997-2004» — Svoboda's legacy-archive bucket |
| Identifier in URL slug | `24188032` (RFE/RL article ID) |
| Programme description | Self-described in opener as live interview about the Petersburg UFO incidents around 28 March 2003 |
| Paywall / login-wall | None — open RFE/RL legacy archive |
| Restrictions in Russia | RFE/RL is designated «иностранный агент» / undesirable in RF; site is blocked in Russia, accessible via VPN/external |

### 0.3 TheAlphaCentauri video page (`F-ALPHA-VOENNYE`)

| Field | Value |
|---|---|
| URL | `https://thealphacentauri.net/163377-...` (slugified Cyrillic) |
| Page title | «ВОЕННЫЕ СКРЫВАЛИ КОНТАКТЫ С НЛО! Бывший глава Уфологической комиссии Михаил Герштейн» |
| Author of post | Alexandr Tarlakovsky |
| Date | **Лис 14, 2025** (i.e. November 14, 2025, in Ukrainian month notation «Листопад») |
| Section | «Відео» (Video) |
| Comments | 2; views: 203 |
| Content type | Video embed + chapter-index (timecodes 00:00 → 01:20:17) + 6-bullet teaser |
| Page language | Bilingual chrome (Ukrainian site UI) + Russian post body |
| Paywall / login-wall | None for viewing the page; comments require login («Будь ласка, увійдіть у свій профіль») |
| Site self-description | Astronomy/space-news community site |

---

## SECTION 1. F-PRAVDA-TAGS — pravda.ru biographical sketch

The pravda.ru page is, in substance, a curated *biographical card* used as the landing page for any Pravda.Ru article tagged with «Михаил Герштейн». The recoverable substantive content is exclusively the editorial blurb (lines 398–408 of the HTML) plus the Schema.org `articleBody` payload (line 301), which is a near-duplicate of the same text. The single tagged article still visible on the page tile (line 419–433) is by another author and only mentions Gershtein-adjacent topics.

### 1.1 Gershtein institutional affiliations (Pravda biography)

**RU** «Михаил Борисович Герштейн (1972) — автор книг, возглавляет Уфологическую комиссию Русского географического общества, одновременно являясь заместителем начальника управления 13-го департамента Академии национальной безопасности.»
**EN:** "Mikhail Borisovich Gershtein (b. 1972) — author of books, heads the UFO Commission of the Russian Geographical Society, simultaneously serving as deputy head of administration of the 13th department of the Academy of National Security."

- This is the *only* place across the three sources that names the «13-го департамента Академии национальной безопасности» as a Gershtein post; no further detail is given on the page.

### 1.2 Origin of personal interest in ufology — Plesetsk rocket / superrefraction event

**RU** «Проблемами уфологии стал интересоваться с подросткового возраста (после личного наблюдения в атмосфере редкого физического явления, которому в дальнейшем нашлось объяснение в рамках известных науке законов физики): несмотря на научное объяснение «чуда» (взлет ракеты с космодрома «Плесецк», отраженный сверхрефракцией в верхних слоях атмосферы) стремление разгадать тайну настоящих «летающих тарелок» не угасало.»
**EN:** "He began to take an interest in ufology in his teenage years (after a personal observation of a rare atmospheric physical phenomenon which later received an explanation within laws of physics known to science): despite the scientific explanation of this 'miracle' (a rocket launch from the Plesetsk cosmodrome reflected by superrefraction in the upper atmosphere), the desire to unravel the mystery of real 'flying saucers' did not fade."

- Notable: the editorial blurb itself frames Gershtein's *foundational* sighting as already solved — a Plesetsk rocket launch made anomalous by atmospheric super-refraction. This is unusually explicit for a tag-page.

### 1.3 First publications, education, RGO timeline, NEXUS editorship

**RU** «Публикуется с 1988 года ("Техника — молодежи", "НЛО" и др.)»
**EN:** "Published since 1988 ('Tekhnika — molodezhi', 'NLO', and others)."

**RU** «Окончил Российский государственный педагогический университет: специалист в области географии и биологии.»
**EN:** "Graduated from the Russian State Pedagogical University: specialist in geography and biology."

**RU** «С октября 1995 по 1999 год М. Б. Герштейн являлся действительным членом Русского Географического общества, членом бюро Комиссии планетологии».
**EN:** "From October 1995 to 1999 M. B. Gershtein was a full member of the Russian Geographical Society and a member of the bureau of the Planetology Commission."

**RU** «В 2002 году он был восстановлен в рядах РГО и избран председателем Уфологической комиссии.»
**EN:** "In 2002 he was reinstated in the ranks of the RGO and elected chairman of the UFO Commission."

**RU** «С 2004 по 2006 год занимал должность ответственного редактора российско-австралийского журнала о непознанном «NEXUS».»
**EN:** "From 2004 to 2006 he held the post of executive editor of the Russian-Australian magazine of the unexplained 'NEXUS'."

### 1.4 External link

The page links one external profile: `https://www.koob.ru/gershtein/` (koob.ru e-library author page), labeled «Профиль на сайте koob.ru». No other Gershtein-bibliography is enumerated on the page.

### 1.5 What the Pravda page does NOT carry

- No interview content with Gershtein.
- No Pravda.Ru article authored *by* Gershtein.
- No quotes from him.
- The «Тагированные материалы» list shows only **one** non-empty tile (an article «Пирамиды оказались древними "хрущевками"» by А. Артамонов, 27 Sep 2017), which is generic and not Gershtein-authored. Three of the four tile slots in the captured first page are empty.
- The Schema.org `articleBody` field merely repeats the on-page biographical paragraph.

### 1.6 Pravda-only claim-block summary

Pravda contributes **6 claim-blocks**: §1.1, §1.2, §1.3 (×3 sub-claims about education / RGO / NEXUS), §1.4. The page is a thin biographical card; the bulk is duplicated metadata.

---

## SECTION 2. F-SVOBODA-2011 — Subbotnee Interview (31 May 2003)

This is the substantive document of the trio. The interview was prompted by the late-March 2003 wave of UFO-sighting reports in St Petersburg and Leningrad Oblast (Карельский перешеек / Karelian Isthmus, Lomonosov, садоводства). The full Q&A spans the first ~80% of the captured page. All quotes below are verbatim from the page body.

### 2.1 Opening identification of Gershtein

**RU** «Гость нашей субботней программы Михаил Герштейн – председатель уфологической комиссии Русского географического общества, главный редактор электронного бюллетеня "УфоНавигатор" международного центра уфлогических исследований и академии безопасности России, автор книг о феномене НЛО "Заблудившиеся во времени" и "По ту сторону НЛО".»
**EN:** "The guest of our Saturday programme is Mikhail Gershtein — chairman of the UFO Commission of the Russian Geographical Society, editor-in-chief of the electronic bulletin 'UfoNavigator' of the International Centre for Ufological Research and the Academy of Security of Russia, author of books on the UFO phenomenon 'Zabludivshiesya vo vremeni' and 'Po tu storonu NLO'."

- Notable: the 2003 framing already lists «По ту сторону НЛО» as published — situates that book pre-2003.
- The role of «УфоНавигатор» editor-in-chief is named — separate from the «NLO»/«Anomaliya» strands.

### 2.2 Trukhan's opener — «главный уфолог России»

**RU** «С Михаилом Герштейном, главным уфологом России, беседует Ольга Писпанен.»
**EN:** "With Mikhail Gershtein, the chief ufologist of Russia, Olga Pispanen converses."

- The «главный уфолог России» title is editorial framing by RFE/RL, not Gershtein's own claim — but it indicates how the broadcaster positioned him in 2003.

### 2.3 Petersburg «UFO invasion» context (28 March 2003)

**RU** «Поводом к нашему сегодняшнему разговору послужили многократные сообщения в средствах массовой информации о том, что в Питере началось вторжение НЛО – буквально такие заголовки приводятся в газетах, также печатаются интервью сотнями очевидцев.»
**EN:** "The occasion for today's conversation was the repeated reports in mass media that a UFO invasion has begun in Peter [St Petersburg] — literally such headlines appear in the newspapers, and interviews with hundreds of eyewitnesses are also being published."

### 2.4 Position of academic science — «ученые ничего не сказали»

**RU** «На самом деле ни один из ученых пока еще по этому поводу ничего не сказал. Потому что ученые, даже из Пулковской обсерватории предпочитают всех очевидцев отсылать к нам.»
**EN:** "In fact, not one of the scientists has yet said anything on this score. Because scientists — even from Pulkovo Observatory — prefer to redirect all eyewitnesses to us."

- Key methodological assertion: Pulkovo Observatory routes UFO witnesses to Gershtein's commission rather than handling them in-house.

### 2.5 Field methodology — capture, copy, cross-check, radar

**RU** «В первую очередь наше исследование заключается в том, чтобы как можно быстрее по горячим следам зафиксировать это самое явление, пока не выветрилось из памяти очевидцев. Если есть какие-то свидетельства материальные, то есть фотографии, видеозаписи, сделать копии. Все это дело как следует проанализировать, затем свериться с соответствующими службами – в первую очередь ПВО (туда тоже был послан запрос по поводу 28 марта), затем с аэропортом "Пулково", где ведется радарная регистрация и сохраняются магнитные записи.»
**EN:** "First and foremost our research consists of fixing this very phenomenon as fast as possible while the trail is hot, before it has evaporated from the eyewitnesses' memory. If there are any material evidences — photographs, video recordings — make copies. Analyse all of this properly, then cross-check with the appropriate services — first of all PVO [Air Defence] (a request about 28 March was also sent there), then with Pulkovo airport, where radar registration is kept and magnetic recordings are preserved."

### 2.6 Pulkovo radar utility — automatic geometry

**RU** «В некоторых особо важных случаях нам приходится давать специальный запрос и когда появляется НЛО, всегда интересно, был ли он зафиксирован на радаре, потому что дает целую массу информации об объекте автоматически. Например, высота, дистанция до объекта от аэропорта "Пулково", все это высчитывает пулковский радар автоматически.»
**EN:** "In some particularly important cases we have to file a special request, and when a UFO appears it is always interesting whether it was captured on radar, because it yields a whole mass of information about the object automatically. For example, altitude, distance from Pulkovo airport — all this is calculated automatically by the Pulkovo radar."

### 2.7 Operational link with Pulkovo since 1995

**RU** «Они с нами сотрудничают, не скажу, что с большим удовольствием, потому что все-таки наши просьбы отвлекают от ежедневной работы в аэропорту. Но, тем не менее, начиная с 95-го года, у нас контакт налажен достаточно серьезно с аэропортом "Пулково", с диспетчерским центром, с диспетчерской вышкой, есть телефон прямые. Так что если объект наблюдается, можно позвонить по мобильному телефону в аэропорт и специально посмотреть в ту сторону, радаром "пощупать", что же это такое.»
**EN:** "They cooperate with us — I won't say with great pleasure, because our requests do distract from daily airport work. But nonetheless, since 1995 we have established quite a serious contact with Pulkovo airport, with the dispatch centre, with the dispatch tower; there are direct telephones. So if an object is observed, one can call the airport on mobile and have them specifically look in that direction and 'probe' it with the radar to see what it is."

- Concrete operational claim: a *direct phone line* to Pulkovo dispatch since 1995.

### 2.8 28 March 2003 case — three appearances over ~3 hours, brightness, distance

**RU** «Так много очевидцев данного случая, потому что, во-первых, объект был чрезвычайно яркий, а во-вторых, он висел на высоте три с половиной километра примерно, по приблизительным подсчетам.»
**EN:** "There were so many eyewitnesses of this case because, firstly, the object was extremely bright, and secondly, it hung at an altitude of approximately three and a half kilometres, by approximate calculations."

**RU** «И поскольку его яркость была чрезвычайно велика, настолько, что, например, в одном из садоводств увидел это объект человек, который только что прошел операцию по зрению, у него глаукома, и он, несмотря на это, увидел этот объект, хотя практически ничего другого не видит.»
**EN:** "And since its brightness was extraordinarily great — so much so that in one of the dacha settlements this object was seen by a man who had just had eye surgery, he has glaucoma, and nonetheless he saw this object although he sees practically nothing else."

**RU** «Этот объект видели даже в Ломоносове, хотя он зависал над Карельским перешейком. Это порядка 80 километров по прямой, но, тем не менее, объект был увиден и там».
**EN:** "This object was seen even in Lomonosov, although it was hovering above the Karelian Isthmus. That is around 80 kilometres in a straight line, but nonetheless the object was seen there too."

**RU** «28 марта этот объект появлялся трижды. Первое появление его было где-то примерно в 20 часов 25 минут. Затем он появился второй раз, но уже достаточно далеко – над Ладожским озером, в 9 часов с минутами, и третье его появление было в 23.07. И каждый раз он от получаса до 15 минут находился практически неподвижно, так, что его можно было совершенно спокойно рассмотреть, сбегать за видеокамерой.»
**EN:** "On 28 March this object appeared three times. Its first appearance was at approximately 20:25. Then it appeared a second time, but already quite far away — above Lake Ladoga, at 9 PM with minutes, and its third appearance was at 23:07. And each time, for between half an hour and 15 minutes, it remained practically motionless so that one could calmly examine it, run for a video camera."

- Key parameters: altitude ~3.5 km; visible from Lomonosov (≈80 km baseline); three appearances at ~20:25, ~21:0X, and 23:07; static-hover episodes of 15–30 min each.

### 2.9 Five video tapes already collected

**RU** «У нас есть в настоящий момент пять видеопленок, запечатлевших этот объект, и в ближайшее время, мы не сомневаемся, будет еще больше.»
**EN:** "We currently have five video tapes that captured this object, and we do not doubt that in the near future there will be more."

### 2.10 Why UFOs cluster near military / nuclear / missile sites

**RU** «Конечно, этому есть объяснение. В первую очередь потому, что это ключевые жизненно важные точки в любом обществе. И любая организация, любое общество, которое хочет изучить другое общество, должно в первую очередь контролировать вот эти точки жизненно важные. Так, кстати, было 28-го числа, потому что все места, где зависал этот объект, везде под ними были воинские части.»
**EN:** "Of course there is an explanation for this. First of all because these are key vital points in any society. And any organisation, any society that wants to study another society must, first and foremost, control these vital points. So it was, incidentally, on the 28th, because in all places where this object hovered, there were military units underneath."

### 2.11 First Chechen War — UFO sightings, fireballs, «к большой крови»

**RU** «Дело в том, что в первую чеченскую войну очень много сообщений приходило от людей, которые там воевали, от местных жителей, которые бежали из Грозного, что наблюдались неопознанные летающие объекты. Во время первого вторжения в Чечню наблюдались огненные шары, наблюдались объекты, причем, наблюдались они очень низко и, естественно, самые мрачные предположения рождали в головах очевидцев, что, дескать, появился красный шар, значит к большой крови. Фактически эти предположения оправдались в полной мере.»
**EN:** "The thing is that during the first Chechen war very many reports came from people who fought there, from local residents who fled from Grozny, that unidentified flying objects were observed. During the first invasion of Chechnya, fireballs were observed, objects were observed — and they were observed very low — and naturally the most gloomy conjectures were born in the eyewitnesses' heads, that, you know, a red ball appeared so that means [it portends] great bloodshed. In fact these conjectures were fully borne out."

### 2.12 Loss of Chechnya channel after 1997 — last letter

**RU** «К сожалению, после 97-го года мы перестали получать из Чечни сообщения, потому что там уже все разрушено, сообщать практически никому, все русскоязычное население оттуда бежало. Самое последнее письмо, которое мы получили, оно к нам пришло в 97-м году, точнее, его принесли родственники человека, который из-за инвалидности не смог из Чечни бежать. Он там остался один в полуразрушенной квартире, и когда он сидел в инвалидном кресле перед окном, ему пришлось дважды наблюдать пролет неопознанных летающих объектов над Грозным.»
**EN:** "Unfortunately, after 1997 we stopped receiving reports from Chechnya, because everything there is already destroyed, there is practically no one to report, all the Russian-speaking population fled. The very last letter we received came in 1997 — more precisely, it was brought by relatives of a man who, because of his disability, could not flee from Chechnya. He stayed there alone in a half-destroyed flat, and when he sat in his wheelchair in front of the window, he had to observe twice the flight of unidentified flying objects over Grozny."

### 2.13 Verification methodology — material evidence + signature features

**RU** «Проще всего, когда есть независимые материальные свидетельства. То есть фотографии, видеозаписи и так далее, то есть есть возможность проверить, сопоставить.»
**EN:** "It is simplest when there are independent material evidences — photographs, video recordings, and so on — that is, there is the possibility to verify, to compare."

**RU** «Во-вторых, существуют так называемые типичные признаки характерного НЛО, которые ни один серьезный уфолог не станет помещать в статье, чтобы они не стали руководством к действию для людей, которые хотят какую-то мистификацию устроить. И вот эти очень характерные черточки, если в описании свидетеля присутствуют, значит все в порядке, можно работать дальше. Если они отсутствуют или каким-то образом искажены, значит случай сомнительный, и его в лучшем случае положить в папку с надписью "поискать других подтверждений".»
**EN:** "Secondly, there exist so-called typical signs of a characteristic UFO which no serious ufologist will publish in an article, so that they don't become a guide to action for people who want to stage some mystification. And these very characteristic features — if they are present in the witness's description, then everything is in order, one can work further. If they are absent or somehow distorted, then the case is dubious, and at best one puts it in a folder labelled 'look for other confirmations'."

- Methodological hallmark: a deliberately *unpublished* checklist of UFO signatures, withheld to prevent hoax-coaching.

### 2.14 Soviet program scope — title of Academy of Sciences / MoD theme

**RU** «Такое исследование проводилось и, более того, сама тема изучения НЛО при советской власти по линии Академии наук и Министерства обороны она так и называлась: "Изучение аномальных аэрокосмических объектов и их воздействие на технику, личный состав и так далее". То есть в первую очередь ученых и военных интересовало, какое воздействие оказывают эти объекты, физическое, психическое и так далее.»
**EN:** "Such research was carried out, and moreover the very theme of UFO study under Soviet rule along the Academy of Sciences and Ministry of Defence line was called: 'Study of anomalous aerospace objects and their impact on technology, personnel, etc.' That is, first of all the scientists and the military were interested in what impact these objects exert — physical, psychic, and so on."

- Verbatim Soviet program title given by Gershtein: «Изучение аномальных аэрокосмических объектов и их воздействие на технику, личный состав и так далее».

### 2.15 EM-effect cases — engines, lamps, searchlights

**RU** «В присутствии этих объектов выходят из строя двигатели автомобилей, гаснут лампочки, гаснут прожекторы. Кстати, в одной из военных частей был случай, когда пытались на НЛО навести прожектор, как только навели на него прожектор, он сразу погас. Полезли туда военные внутрь, перегорела лампа. Вывернули, вкрутили другую, опять направили прожектор на НЛО, лампа опять перегорает. И так шесть раз, пока им не надоело лампу менять, пока они не поняли, что еще так дальше и весь запас ламп к прожектору просто иссякнет. А НЛО висело спокойно в течение получаса.»
**EN:** "In the presence of these objects, car engines fail, lamps go out, searchlights go out. Incidentally, in one military unit there was a case where they tried to direct a searchlight at a UFO; as soon as they pointed the searchlight at it, it immediately went out. The soldiers climbed in there — the lamp had burnt out. They unscrewed it, screwed in another, again directed the searchlight at the UFO, the lamp again burns out. And so six times, until they got tired of changing the lamp, until they realised that if it went on like this their entire stock of searchlight lamps would simply run out. And the UFO hung calmly for half an hour."

### 2.16 1984 Caspian incident — fighter wing + helicopters

**RU** «В 84-м году, например, был случай на Каспии, когда пытались НЛО прижать к воде целое звено истребителей, а снизу этот объект подкарауливали вертолеты. Так он с такой легкостью уходил от истребителей на высоту, на которую они не могли летать, слишком низко к воде прижимался, а когда приближались вертолеты, наоборот, уходил свечой верх, так что не могли такой маневр повторить.»
**EN:** "In 1984, for example, there was a case on the Caspian, when an entire wing of fighters tried to press a UFO against the water, while from below this object was lain in wait for by helicopters. It eluded the fighters with such ease at altitudes which they could not fly, pressed too low to the water, and when the helicopters approached, on the contrary, it pulled up vertically — so that they could not repeat such a manoeuvre."

### 2.17 1989 Arkhangelsk Oblast incident — tracer rounds deflected by «защитное поле»

**RU** «В 89-м году, например, в Архангельской области был случай, когда неопознанный летающий объект приблизился к вышке одной из зон в поселке, и там по этому объекту пытались стрелять. Очевидцы из других вышек наблюдали как трассирующие пули, а в автомате у часового каждая десятая пуля была трассирующей, подлетали к этому объекту, делали зигзаг, возвращались на свою территорию и летели дальше. То есть защитное поле отклонило пулю от объекта и направило дальше, чтобы они не повредили никого, ничего.»
**EN:** "In 1989, for example, in Arkhangelsk Oblast there was a case when an unidentified flying object approached the watchtower of one of the camp-zones [penal-colony watchtower] in a settlement, and they tried to fire at this object. Eyewitnesses from other watchtowers observed how tracer bullets — and in the sentry's automatic [rifle] every tenth bullet was a tracer — flew up to this object, made a zigzag, returned to their own territory and flew on. That is, a protective field deflected the bullet from the object and directed it on so that it would not damage anyone, anything."

### 2.18 Late-1980s Omsk Oblast crash — large troop cordon, identification uncertain

**RU** «В конце 80-х годов очень сильно нашумел случай в Омской области, когда там упал некий неизвестный летательный аппарат, там оцепляли весь район, но что за аппарат упал, честно говоря, я не могу сказать, что это был инопланетный. Может это был какой-то секретный самолет, может быть ракета, но плотность сцепления, которая была там устроена, она впечатляла не только местных жителей, но и военных, которые случайно это наблюдали. Какой бы ни был секретный самолет, но такую массу военных нагнать туда для оцепления...»
**EN:** "At the end of the 1980s the case in Omsk Oblast was much talked about, when some unknown flying apparatus fell there, they cordoned off the whole district, but what kind of apparatus fell — honestly, I cannot say that it was extraterrestrial. Perhaps it was some secret aircraft, perhaps a rocket, but the density of the cordon that was set up there impressed not only the local residents but also the military who happened to observe it. Whatever the secret aircraft, but to drive such a mass of military there for a cordon..."

- Notable: Gershtein refuses to commit to ET hypothesis on the Omsk crash; explicitly admits «не могу сказать, что это был инопланетный».

### 2.19 Disinformation about crashed-disc cases

**RU** «Безусловно, такие случаи были зафиксированы, и я бы даже сказал, что слухов о подобного рода историях чрезвычайно много. Настолько много, что они мне кажутся специально размноженными по определенному шаблону дезинформации. Чтобы забить историю о каком-то реальном крушении НЛО, просто выдумываются десятки ложных историй о крушениях НЛО и выбрасываются в обществе, в этой мешанине пойди найди тот единственный действительно реальный, который произошел.»
**EN:** "Undoubtedly, such cases have been recorded, and I would even say that rumours about stories of this kind are extremely numerous. So numerous that to me they seem to be specially propagated according to a certain template of disinformation. In order to drown out the story of some real UFO crash, dozens of false stories about UFO crashes are simply invented and thrown into society — and in this jumble, just try to find the single really real one that occurred."

- Disinformation-template thesis articulated as early as 2003.

### 2.20 International cooperation — only public information shared

**RU** «То есть уфология в принципе в очень многих западных странах является областью исследований, близко связанной с оборонкой. То есть они делятся только общедоступной информацией и той, которую можно совершенно спокойно почерпнуть, скажем, из западных газет, из западных журналов и так далее. А то, что накоплено действительно в ходе собственных исследований, а не из общедоступных источников, как правило, к нам не поступает.»
**EN:** "That is, ufology in principle in very many Western countries is a field of research closely connected with the defence industry. So they share only publicly accessible information and that which can be calmly drawn, say, from Western newspapers, Western magazines and so on. But what is really accumulated in the course of their own research, not from publicly accessible sources, as a rule does not reach us."

### 2.21 Skepticism about contactees — five cases in seven+ten years

**RU** «На самом деле, если серьезно подходить к этой проблеме, то лично я за семь лет работы в газете "Аномалия" и в географическом обществе за десятилетие практических исследований с такими случаями сталкивался не более пяти раз. В очень многих случаях не было никаких ни дополнительных подтверждений, ни чего-либо еще, что могло бы позволить относиться к этим случаям достаточно серьезно.»
**EN:** "In fact, if one approaches this problem seriously, then I personally — over seven years of work at the newspaper 'Anomaliya' and in the Geographical Society for a decade of practical research — have encountered such cases no more than five times. In a very large number of cases there were neither any additional confirmations nor anything else that could allow us to treat these cases sufficiently seriously."

- Quantitative skeptical claim: ≤5 contactee/humanoid encounters across 7 years at *Anomaliya* and 10 years at RGO that survived scrutiny.

### 2.22 Telepathic-channelers — psychiatric filter, none passed

**RU** «А что касается тех людей, которые получают телепатическую информацию откуда-то сверху, то я не встречал ни одного человека, к информации которого можно было бы относиться серьезно. Более того, у нас был опыт работы с привлечением независимого психиатра к подобного рода сообщениям. И ни один людей, который утверждал, что он общается с подобного рода существами телепатически, получают от них какие-то послания и так далее, ни один из них этого фильтра не прошел.»
**EN:** "As for those people who receive telepathic information from somewhere above, I have not met a single person whose information could be taken seriously. Moreover, we had experience of working with an independent psychiatrist on reports of this kind. And not one of the people who claimed that he communicates with beings of this kind telepathically, that they receive messages from them and so on, not one of them passed this filter."

- Concrete methodology: Gershtein's commission used an *independent psychiatrist* to vet telepathic-channeler claims; none passed.

### 2.23 Genuine contact cases — psychic preservation, retained skepticism

**RU** «На самом деле, когда происходит реальный контакт с НЛО, то на психику это фактически не воздействует, то есть человек остается нормальным, здравомыслящим и, более того, иногда не теряет своего скептицизма. Мне приходилось встречаться со случаями, когда человек продолжал не верить в НЛО, несмотря на то, что он его видел своими собственными глазами. Я ему говорю – а что же это тогда было? "Ну не знаю, вертолет с огнями или какая-нибудь американская секретная машина или еще что-нибудь, а в вашего гуманоида все равно не верю".»
**EN:** "In reality, when a real contact with a UFO occurs, it does not in fact affect the psyche; that is, the person remains normal, sane, and moreover sometimes does not lose his scepticism. I have had occasion to meet cases where a person continued not to believe in UFOs despite the fact that he had seen one with his own eyes. I say to him — well then what was it? 'Well, I don't know, a helicopter with lights or some American secret machine or something else, but in your humanoid I still don't believe'."

### 2.24 Safety guidance — keep distance, exhaust-cone analogy

**RU** «Безусловно, правила безопасности существуют, и самое главное из них гласит, что к этим объектам приближаться, по крайней мере настолько, чтобы попасть в зону освещения, окружающее этот объект, не рекомендуется. Это то же самое, как подходить сзади к реактивному самолету с работающим мотором, то есть можно обжечься выхлопом очень здорово.»
**EN:** "Without doubt, safety rules exist, and the chief of them states that approaching these objects — at least so closely as to enter the illumination zone surrounding the object — is not recommended. It is the same as approaching from the rear a jet aircraft with its engine running — that is, one can be very seriously burned by the exhaust."

**RU** «И как в случае с реактивным самолетом пилот не замечает человека, подошедшего сзади к соплу очень неосторожно, точно так же и пилоты НЛО могут не заметить человека, и он может получить серьезные либо ожоги, либо травмы, либо ранения, может отбросить волной при старте. Может произойти практически все, что угодно. Но в большинстве этих случаев не было преднамеренного, злономнамеренного воздействия на человека.»
**EN:** "And just as in the case of a jet aircraft the pilot does not notice a person who has approached the nozzle very carelessly from behind, in exactly the same way UFO pilots may not notice a person, and he may receive serious burns, traumas or injuries, may be thrown by a wave at takeoff. Practically anything can happen. But in the majority of these cases there was no deliberate, malicious impact on the person."

- Casualty model: incidental industrial-accident analogue, not deliberate hostility.

### 2.25 Svoboda contribution summary

The 2003 Svoboda interview is the only one of the three sources that yields *substantive ufological content*. It produces approximately **24 distinct claim-blocks** above (§2.1–§2.24). It documents Gershtein's RGO-era operational picture: Pulkovo radar liaison since 1995, *Anomaliya* tenure (~7 years before mid-2003 ⇒ ~1996+), the Soviet AAS program title verbatim, the 1984 Caspian and 1989 Arkhangelsk military cases, the late-80s Omsk crash (treated agnostically), the disinformation-template thesis on crashed-disc lore, and a striking methodological practice of using an *independent psychiatrist* to vet telepathic-channeler cases.

---

## SECTION 3. F-ALPHA-VOENNYE — TheAlphaCentauri video index (14 Nov 2025)

The TheAlphaCentauri page is essentially a **video-description / chapter-index** page. It does not contain the actual interview text — only six teaser bullets and an explicit table of timecodes. All extracted text is verbatim from the page.

### 3.1 Page title (as published)

**RU** «ВОЕННЫЕ СКРЫВАЛИ КОНТАКТЫ С НЛО! Бывший глава Уфологической комиссии Михаил Герштейн»
**EN:** "THE MILITARY HID CONTACTS WITH UFOs! Former head of the UFO Commission Mikhail Gershtein"

- Note the past-tense title «Бывший глава» — by November 2025 the page already characterises Gershtein's RGO Commission tenure as concluded.

### 3.2 Editorial blurb — claimed first-time disclosures

**RU** «Михаил Герштейн — бывший председатель Уфологической комиссии Русского географического общества, автор 14 книг об аномальных явлениях. В этом интервью Михаил впервые рассказывает о:»
**EN:** "Mikhail Gershtein — former chairman of the UFO Commission of the Russian Geographical Society, author of 14 books on anomalous phenomena. In this interview Mikhail tells for the first time about:"

- Bibliographic claim: «автор 14 книг» — 14 books on anomalous phenomena. (To be cross-checked against catalog.)

### 3.3 Six advertised topics (verbatim list)

**RU** «Секретных военных программах СССР по изучению НЛО»
**EN:** "Secret military programmes of the USSR for the study of UFOs"

**RU** «Личном наблюдении летающей тарелки в 1986 году»
**EN:** "Personal observation of a flying saucer in 1986"

**RU** «Засекреченных документах, которые американцы вывезли из России»
**EN:** "Classified documents that the Americans took out of Russia"

**RU** «Реальных контактах военных с неопознанными объектами»
**EN:** "Real contacts of the military with unidentified objects"

**RU** «Почему над военными базами постоянно наблюдают НЛО»
**EN:** "Why UFOs are constantly observed above military bases"

**RU** «Уникальные свидетельства из закрытых архивов КГБ и Министерства обороны СССР.»
**EN:** "Unique testimonies from the classified archives of the KGB and Ministry of Defence of the USSR."

- The 1986 personal-sighting claim is cross-checkable against the Pravda biographical sketch (§1.2), where the formative event is described as a Plesetsk-rocket / superrefraction observation in his teens (Gershtein b. 1972 → ~14 years old in 1986).

### 3.4 Chapter index (verbatim timecodes)

The page lists **30 chapter timestamps** spanning 00:00 → 01:20:17 (≈80 minutes). Verbatim:

> «00:00 Тизер 
> 00:54 Цензура НЛО в СССР 
> 01:43 Первое наблюдение: летающая тарелка над Ленинградом 
> 05:32 Как я стал уфологом в 19 лет 
> 06:44 Отношение к НЛО в советское время 
> 08:31 Пики наблюдений: 1977 и 1989-1991 годы 
> 09:23 Откуда взялись архивы с 1800-х годов 
> 10:56 Серьезные скептики vs фанатики 
> 13:11 Военные программы: НИИ-22 и НИИ-50 
> 16:56 Почему архивы до сих пор засекречены 
> 18:48 Американец вывез секретные документы за икру 
> 20:41 США: дезинформация и фальшивые гуманоиды 
> 23:27 Обратный инжиниринг: плазменные технологии от НЛО 
> 27:34 Слушания в Конгрессе США — пыль в глаза? 
> 29:25 Трамп и его "секретное оружие" 
> 29:47 Украина: НЛО как военная дисциплина 
> 32:03 НЛО на линии фронта — свидетельства военных 
> 33:32 Что нужно для веры в НЛО? 
> 35:43 Демонстрация силы: корабли над столицами 
> 37:18 Похищения и пробы почвы — зачем? 
> 40:08 Что делать при встрече с НЛО 
> 41:26 Грузия, 1978: три кандидата наук VS защитное поле 
> 46:52 Угрозы и репрессии для уфологов 
> 49:29 Секта, которая нападала на московских уфологов 
> 50:16 Контакты и психика: что происходит с людьми 
> 53:19 Внутри НЛО: описания очевидцев 
> 54:47 Зачем они следят за военными базами? 
> 57:13 Космическая экспансия человечества — угроза соседям? 
> 59:53 "Если меня похитят…" — личный ответ 
> 01:03:32 Вопросы пришельцам и древнегреческий истребитель 
> 01:05:11 5% необъяснимых случаев 
> 01:09:03 Охота на НЛО: когда расстреляли деревню 
> 01:12:32 Как систематизировать сбор данных сегодня 
> 01:16:15 Что изменится, если докажут существование НЛО? 
> 01:20:17 Заключение»
**EN (selected key chapters):** "Censorship of UFOs in the USSR / First observation: flying saucer over Leningrad / How I became a ufologist at 19 / Attitude towards UFOs in Soviet times / Peaks of observations: 1977 and 1989–1991 / Where the archives from the 1800s came from / Serious sceptics vs fanatics / Military programmes: NII-22 and NII-50 / Why the archives are still classified / An American took out classified documents for caviar / USA: disinformation and fake humanoids / Reverse engineering: plasma technologies from UFOs / Hearings in the US Congress — dust in the eyes? / Trump and his 'secret weapon' / Ukraine: UFOs as a military discipline / UFOs on the front line — testimonies of the military / What is needed to believe in UFOs / Demonstration of force: ships above capitals / Abductions and soil samples — why? / What to do upon encountering a UFO / Georgia, 1978: three candidates of science VS the protective field / Threats and repressions for ufologists / The sect that attacked Moscow ufologists / Contacts and psyche: what happens to people / Inside the UFO: descriptions of eyewitnesses / Why do they watch over military bases? / Cosmic expansion of mankind — a threat to neighbours? / 'If they abduct me…' — personal answer / Questions to aliens and the Ancient Greek fighter / 5% of inexplicable cases / Hunting for UFOs: when they shot up a village / How to systematise data collection today / What will change if the existence of UFOs is proved / Conclusion"

### 3.5 Notable index-only data points

Even without the audio, the chapter index alone yields several cross-checkable claims for this archive:

- **Chapter @ 01:43:** Personal sighting *over Leningrad* — corroborates the 1986/teen-age sighting (per teaser §3.2).
- **Chapter @ 05:32:** «Как я стал уфологом в 19 лет» — a date-anchored autobiographical claim: 19 years old → 1991.
- **Chapter @ 08:31:** «Пики наблюдений: 1977 и 1989-1991 годы» — Gershtein names two USSR-era peaks (1977 and the 1989–1991 cluster).
- **Chapter @ 13:11:** «Военные программы: НИИ-22 и НИИ-50» — names two NII (research-institute) numbers as the Soviet UFO study units. (Cross-check against the «Сетка» / «Галактика» framing common in other Gershtein interviews.)
- **Chapter @ 18:48:** «Американец вывез секретные документы за икру» — claim that a named American carried out classified Soviet UFO documents «in exchange for caviar» (idiom for an absurdly low price).
- **Chapter @ 41:26:** «Грузия, 1978: три кандидата наук VS защитное поле» — 1978 Georgia case with three candidates of science vs a UFO «protective field» (parallels the 1989 Arkhangelsk «защитное поле» pattern in §2.17).
- **Chapter @ 49:29:** «Секта, которая нападала на московских уфологов» — alleges a sect physically attacked Moscow ufologists.
- **Chapter @ 01:09:03:** «Охота на НЛО: когда расстреляли деревню» — case where, in pursuit of a UFO, soldiers «shot up a village».
- **Chapter @ 01:05:11:** «5% необъяснимых случаев» — Gershtein's residual-mystery quantification (5% inexplicable).
- **Chapter @ 23:27:** «Обратный инжиниринг: плазменные технологии от НЛО» — segment claims plasma reverse-engineering from UFOs.

### 3.6 What the TheAlphaCentauri page does NOT carry

- No interview transcript.
- No statements from Gershtein in his own words on the page; only chapter labels (which are the *editor's* phrasing, not necessarily Gershtein's).
- No publication/citation of the 14 books referenced in the blurb.
- The video itself is hosted via embed; the embed code is in the page chrome but the audio/video stream is not part of the captured HTML.

### 3.7 AlphaCentauri contribution summary

This source produces approximately **15 claim-blocks** — but they are **second-order claims**: about the *advertised content* of an interview, not about facts attested by Gershtein on this page. The chapter-index is internally redundant with what other Gershtein interviews already cover; its value here is as a *map* indicating which themes Gershtein systematically returns to in 2025-vintage long-form interviews (military programs, KGB archives, Georgia 1978, Arkhangelsk-style protective-field cases, abductions, contact-psychology, 5% residual).

---

## Cross-references

### Within this F-MID-10 file

- **Pravda §1.2** (Plesetsk rocket / superrefraction sighting in teens) ↔ **AlphaCentauri §3.2** (1986 personal sighting) ↔ **AlphaCentauri chapter @ 05:32** («стал уфологом в 19 лет», ~1991): all three are *facets* of the same biographical kernel — early-1986 atmospheric sighting at age 13–14, formal career start at 19 (~1991), formative motive intact despite later natural explanation.
- **Pravda §1.3** (RGO 1995–1999 + reinstated 2002 as commission chair) ↔ **Svoboda §2.1** («председатель уфологической комиссии РГО» as of May 2003) ↔ **AlphaCentauri §3.1** («Бывший глава» as of Nov 2025): consistent timeline of Commission chairmanship from 2002 to a now-concluded period as of 2025.
- **Svoboda §2.7** (Pulkovo radar contact since 1995) ↔ **Pravda §1.3** (RGO membership starting October 1995): the 1995 inflection point — RGO membership and Pulkovo contact begin in the same year.
- **Svoboda §2.17** (Arkhangelsk 1989 — tracer bullets deflected by «защитное поле») ↔ **AlphaCentauri chapter @ 41:26** (Georgia 1978 — three candidates of science vs «защитное поле»): the «protective field» motif is consistent across two cases reported a decade apart.
- **Svoboda §2.14** (Soviet program title verbatim) ↔ **AlphaCentauri chapter @ 13:11** («Военные программы: НИИ-22 и НИИ-50»): both reference the Soviet AAS military-science complex; AlphaCentauri lists specific NII numbers absent from Svoboda.
- **Svoboda §2.19** (disinformation-template thesis) ↔ **AlphaCentauri chapter @ 20:41** («США: дезинформация и фальшивые гуманоиды»): consistent disinformation-skepticism stance from 2003 to 2025.
- **Svoboda §2.21–§2.22** (≤5 contactee cases; psychiatrist-vetting protocol) ↔ **AlphaCentauri chapter @ 50:16** («Контакты и психика»): persistent methodological commitment to contactee skepticism and psychiatric filtering.

### To other gershtein-archive items (same archive)

- The «По ту сторону НЛО» and «Заблудившиеся во времени» books named in **Svoboda §2.1** are catalogued in `gershtein-archive/books/INDEX.md` — both pre-2003 according to the interview framing.
- The «Аномалия» newspaper tenure mentioned in **Svoboda §2.21** (~7 years by 2003 → ~1996 onward) provides a publication-history anchor that other archive items can be checked against.
- The «УфоНавигатор» electronic bulletin and the «Международный центр уфлогических исследований и Академия безопасности России» named in **Svoboda §2.1** (also Pravda §1.1, «13-го департамента») are institutional affiliations distinct from the RGO Commission chairmanship — useful to disambiguate which hat Gershtein wore in which publication.

### To external archives (chernobrov-archive, RUFORS, etc.)

- The «защитное поле» motif (Svoboda §2.17, AlphaCentauri @ 41:26) overlaps with motifs in chernobrov-archive cases of bullet/laser deflection.
- The disinformation-template thesis (Svoboda §2.19) is a recurring trope in the broader Russian-ufology discourse of the 1990s–2000s.

---

## Sections-not-covered (of the 11 standard Gershtein themes)

Standard themes (per archive convention):

| # | Theme | Pravda | Svoboda 2003 | AlphaCentauri 2025 |
|---|---|---|---|---|
| 1 | RGO UFO Commission chairmanship and institutional role | **partial** (1995/1999/2002 timeline) | **covered** (chair as of 2003; methodology) | **partial** (titled «бывший глава» 2025) |
| 2 | Tunguska investigations | not covered | not covered | not covered |
| 3 | Dalnegorsk (Height 611, 29 Jan 1986) case work | not covered | not covered | not covered (chapter index does not name it) |
| 4 | Petrozavodsk phenomenon (20 Sep 1977) | not covered | not covered | **partial** (chapter @ 08:31 names «1977» as observation peak) |
| 5 | KGB / Setka / military UFO files and declassification advocacy | not covered | **partial** (Soviet program title in §2.14; Arkhangelsk 1989, Caspian 1984, Omsk crash) | **partial** (chapters on KGB archives, NII-22/NII-50, classified archives, American-with-caviar export) |
| 6 | Soviet/Russian historical UFO chronology and archival research | not covered | **partial** (1984, 1989, late-80s) | **partial** (chapter @ 09:23 «архивы с 1800-х годов»; chapter @ 08:31 «1977 и 1989-1991») |
| 7 | Critique of contactee / cult / pseudo-ufology figures | not covered | **covered** (§2.21–§2.23 contactee skepticism, psychiatrist filter) | **partial** (chapter @ 49:29 «секта, которая нападала на московских уфологов»; chapter @ 50:16 contact-psyche) |
| 8 | Books: «Изнанка НЛО», «По ту сторону НЛО», «Тунгусский метеорит: 100 лет великой тайне», etc. | **partial** (koob.ru link only; no titles listed) | **partial** («По ту сторону НЛО» and «Заблудившиеся во времени» named in §2.1) | **partial** («автор 14 книг» blurb only; no titles) |
| 9 | Media appearances, interviews, lectures | **partial** (Pravda is itself a tag-page indexing media appearances) | **this is itself one such appearance** | **this is itself one such appearance** |
| 10 | Position on extraterrestrial-hypothesis vs psycho-social / unknown-natural-phenomenon framings | **partial** (Plesetsk-superrefraction shows openness to natural explanation) | **covered** (Omsk-crash agnosticism §2.18; disinfo thesis §2.19) | **partial** (chapter @ 01:05:11 «5% необъяснимых случаев») |
| 11 | Personal biography and trajectory through post-Soviet ufology milieu | **covered** (RGO timeline, NEXUS editorship, 13-th-dept post) | **partial** (Anomaliya tenure §2.21; UfoNavigator editorship §2.1) | **partial** (chapter @ 05:32 «уфологом в 19 лет»; chapter @ 01:43 first sighting) |

**Themes fully not covered by the trio:**
- Theme 2 (Tunguska): no mention in any of the three.
- Theme 3 (Dalnegorsk / Height 611): no mention in any of the three.

**Themes covered substantively (by at least one source):**
- 1, 5, 7, 10 — primarily by Svoboda 2003.
- 11 — across all three sources cumulatively.

**Themes that appear only as chapter labels (not actual content):**
- AlphaCentauri's coverage is *advertised* but not *captured* in the page bytes — the text on the page is index-only.

---

## Source-availability note

| Source | Public access | Paywall | Login-wall | Geographic blocking | Recoverable text |
|---|---|---|---|---|---|
| `F-PRAVDA-TAGS` (pravda.ru) | Open | None | None | None (Russian-language site, served globally) | Full HTML body; biographical blurb fully recoverable in Russian |
| `F-SVOBODA-2011` (svoboda.org) | Open from outside RF | None on the article | None for reading | **Blocked inside Russian Federation** — RFE/RL is designated «иностранный агент» / «нежелательная организация»; access requires VPN/external. RFE/RL legacy archive 1997–2004 bucket. | Full transcript fully recoverable; ~24 substantive claim-blocks |
| `F-ALPHA-VOENNYE` (thealphacentauri.net) | Open page | None | **Login required to comment** («Будь ласка, увійдіть у свій профіль»). Reading the page is unauthenticated. | Page itself = video index + 6-bullet teaser only. **The interview audio/video is not part of the captured HTML**; full content would require fetching the embedded video stream separately. |

**Practical access recommendations:**
- Pravda.ru and TheAlphaCentauri pages can be archived directly with `curl`/`wget` and yield their full content as captured.
- Svoboda.org content is open-access globally except inside RF; audit-quality re-fetch should be done from a non-RF egress point.
- TheAlphaCentauri's *real* payload (the interview itself) lives in the embedded video and is **not** in the captured HTML. To extract Gershtein's actual statements behind the chapter labels, the video must be downloaded and transcribed separately. Treat the chapter labels as *editorial paraphrase*, not as Gershtein's verbatim words.

---

## Extraction methodology notes

- All three files are HTML; verbatim Russian was extracted by removing site chrome, scripts, and ads, then preserving the article-body text byte-by-byte.
- Pravda.ru: the substantive text occurs in lines 301 (Schema.org `articleBody` JSON-LD) and 397–408 (rendered HTML); both are duplicates.
- Svoboda.org: the interview body is reconstructed from `<p>`-bound paragraphs in the RFE/RL legacy-archive template; the page also retains the full RFE/RL navigation chrome which was elided. Quotes are 1:1 byte-faithful.
- TheAlphaCentauri.net: the chapter index is the only Gershtein-content portion of the page; the rest is site chrome (Ukrainian) and recent-comments rail (off-topic SpaceX/JPL/Mars threads, irrelevant to this analysis).
- Where the AlphaCentauri page uses Ukrainian month notation («Лис 14, 2025» = November 14), the Gregorian equivalent is preserved.

---

## Per-file claim-block counts

| File | Source code | Claim-blocks | Notes |
|---|---|---:|---|
| pravda.ru tag-page | F-PRAVDA-TAGS | **6** | Biographical card; thin but factual |
| Svoboda interview (31 May 2003) | F-SVOBODA-2011 | **24** | Substantive; primary source of the trio |
| TheAlphaCentauri video page | F-ALPHA-VOENNYE | **15** | Index-only; second-order claims |
| **Total** | | **45** | within target range 30–80 |

End of F-MID-10.
