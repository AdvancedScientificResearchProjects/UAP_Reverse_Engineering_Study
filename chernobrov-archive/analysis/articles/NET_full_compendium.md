# NET (New Energy Technologies) — Full Compendium of 4 Issues

**Source code:** `B-NET-FULL` (merge of `NET-03-2001`, `NET-06-2002`, `NET-09-2003`, `NET-12-2003`)
**Publisher:** Faraday Laboratories Ltd (ООО «Лаборатория Новых Технологий Фарадей»), St. Petersburg
**Editor-in-chief:** Alexander V. Frolov
**Languages:** English-translated from Russian (NET is bilingual; the extracted OCR is the EN edition)
**Source files:**
- `books/downloads/extracted_text/net_03_2001.txt` (442 KB, 4727 lines)
- `books/downloads/extracted_text/net_06_2002.txt` (596 KB, 6198 lines)
- `books/downloads/extracted_text/net_09_2003.txt` (458 KB, 4890 lines)
- `books/downloads/extracted_text/net_12_2003.txt` (360 KB, 4080 lines)

---

## OVERVIEW & CROSS-FILE FINDINGS

### Mishin identity (USER-RES §17 verification)

In all four NET issues Alexander M. Mishin is consistently styled **"Dr. Alexander M. Mishin"** or simply **"A.M. Mishin"**. He is **NEVER** called «академик / academician» in any of these primary sources. The single use of the word "Academician" close to a Mishin name in NET-09-2003 line 2031 / 2051 / 2076 actually refers to **Academician A.F. Mitkevich** (a different person, on electromagnetic dynamics) — disambiguation confirmed by full-line context. In NET-12-2003 the only "academicians" named are **Vladimir Fortov** and **Gennady Mesyats** in the Global Energy Prize sidebar (line 2382, 2390) — neither is Mishin and neither is connected to the Faraday Lab time-machine work.

→ **USER-RES claim that Mishin is an "academician consultant" to the Faraday/Chernobrov circle is NOT supported by NET primary text.** Mishin is a peer contributor (separate articles on aetherodynamics) cited by Frolov as an aether-as-liquid analogy source (NET-03-2001 line 1330: "The analogy between ether and liquid is considered and experimentally proved by Dr. Alexander M. Mishin [7] and others").

### f = c/d frequency formula — PRIMARY DERIVATION LOCATION

The formula **f = 1/T = c/d → 4.28×10¹⁰ Hz at d = 7 mm** appears verbatim in **NET-12-2003 lines 286–305** inside Frolov's article *"Method and Device to Control Temporal Parameters of Physical Processes by Means of Changing of Energy Density of Space"*. This is the canonical English-language derivation — same content as the F-12R Russian paper already analyzed in `analysis/articles/F-12R_faraday_patent_paper.md`. **No earlier or alternative derivation exists in NET-03-2001, NET-06-2002, or NET-09-2003.** The 2002 article *"Physical Principles of The Time Machine"* (NET-06-2002) is qualitative — it does NOT contain f = c/d.

### Patent process — chronology

- **NET-06-2002**: Frolov (Time Machine Project, May 29 2002) — "All new aspects disclosed in this paper are the subject of a patent process. Faraday Labs Ltd organizes experimental program on the topic." → **patent intent declared, no application yet**.
- **NET-09-2003**: Frolov (Some Experimental News, late 2002) — Russian Federation patent claim **#2002128658** of October 25, 2002 filed for **vortex drive** propulsion (NOT the time machine). Time-machine work still labelled "we have signed Contract with Dr. Chernobrov, Moscow, on the topic" (line 199–201).
- **NET-12-2003**: Frolov — Russian Federation patent claim **#2003110067** filed **April 9, 2003** for the time-machine quasi-monopole device (NET-12-2003 line 387–388). This is the canonical patent application discussed in F-12R.

### Lovondatr generation cross-references found

- **NET-03-2001**: explicitly named "LOVONDATR-7" (line 281) — the 2001 Moscow human-experiment build.
- **NET-12-2003**: implicit "7th model" reference (line 94: *"In all the earliest Machines (except the 7th model) this volume still has not exceeded the volume of a football"*) — confirms numbering. Diameters: outer 2.1 m, inner payload 1 m → matches Lovondatr-7 in `articles_and_patent.md`.
- **NET-06-2002 and NET-09-2003**: refer to "4th version" (NET-06-2002 line 737–739: *"Dr. Chernobrov reported about 3% change of the time course in 4th version of the system, which was tested with a human inside"* — actually conflates Lovondatr-4 and the 2001 result; the 2001 result is from Lovondatr-7).

---

# SECTION 1 — NET #3, November–December 2001 (`NET-03-2001`)

## Table of contents (verbatim, lines 5–23)

1. Time is a Mystery of the Universe — Dr. Lavrenty S. Shikhobalov, St. Petersburg
2. **Experiments with a Man in the Time Machine** — Dr. Vadim Chernobrov, Moscow
3. Time is a Physical Substance — Dr. Kirill P. Butusov, St. Petersburg
4. Experimenting with Time — Prof. Velimir Abramovich, Time Institute, Rotterdam
5. **Practical Application of Time Rate Control (TRC) Theory** — Alexander V. Frolov
6. Irving Langmuir and Atomic Hydrogen — Dr. Nicholas Moller, Greece
7. Hydrogen Energy — Studennikov V.V., Kudymov G.I.
8. About Strange Effects Related to Rotating Magnetic Systems — M. Pitkanen, Finland
9. The Transdimensional's Lifters Experiment — Jean-Louis Naudin, France
10. On the Great Constant 137.036 — Dr. Anatoly Rykov
11. Inertial Propulsion Drives — Boris D. Shukalov
12. Technical Design of Antigravitational Spacecraft "Silver Cup" — Eugeny Kovalyov, Latvia
13. Gravito-Inert Mass — J.A. Asanbaeva, Bashkiria
14. Propulsion from Relativity Effect of Inertial Force — Takuya Ishizaka, Japan
15. Physical Properties of Axion Fields — Alexander Shpilman, Kazakhstan
16. On the Significance of Conical Shape of Rotor in Clem's Generator — A.V. Frolov
17. On History of Cold Nuclear Fusion in Russia of 1960s — A.V. Frolov

## §1.1 Lovondatr-7 protocol — VERBATIM (Chernobrov article, lines 248–423)

This is the **complete primary record** of the August 26, 2001 first-human-in-TM experiment.

### Construction (lines 281–311)

> **Construction of LOVONDATR-7**
>
> Editors: the name LOVONDATR in Russian means a trap for musk-rat. This name historically belongs to all Chernobrov's designs, because the creation of the first TM was masked as a research project on creation of electromagnetic trap for musk-rats.
>
> In summer 2001, after several years of preparation work, Kosmopoisk began the assembling of the biggest system of this type. The works lasted about 3 months; about one hundred people took part in the construction and assembling of the Time Machine system. There were:
> - **a sphere of 30 cm with a double electromagnetic work surface (EWS)**
> - **inside of the sphere of 1 meter with a double EWS**
> - **placed inside of another sphere of 2,1 meters with a triple EWS**
>
> Each EWS is a system of solenoids emitters, which create the convergent electromagnetic wave… The entire triple construction (like Russian doll Matroyshka) was supposed to use for the experiments with mice. For the experiments with a man we took out the inner EWS and the medium EWS worked as a module of useful load (UL). The medium and external spheres have the doors for access of a man and load. Also they have a simple system of life support (in particular, there are systems of passive and active conditioning and removal of the condensate).

**Geometry summary:** Three nested spheres, **outer Ø 2.1 m (triple EWS) → middle Ø 1.0 m (double EWS, becomes payload bay for human) → inner Ø 0.30 m (double EWS, removed for human)**. Roughly 100 builders. Build time ≈ 3 months. EWS = solenoid emitters generating convergent electromagnetic waves.

### Experiments with animals (lines 248–311)

- **Mice batch 1:** 21 mice delivered from Moscow → most died (anomalous-zone influence + high temperature).
- **Mice batch 2:** 10 lab mice → 25 of 31 total died across both batches; surviving 6 survived 2-hour exposure → cleared next stage.
- **Cat ("Plombir"):** Selected by Maria Lorenz; cat refused — felt the field at 200 m, scratched Masha (foster mother), fled into forest before each run, returned after each shutdown.
- **Dog ("Lunokhod" — "Moon-buggy"):** Black male, white breast, unknown breed, appeared in forest after young Moon decline. Boarded with fear, released himself at minute 108 of planned 2-hour run. No health deviations observed in dog or final mouse batch.
- **August 26, 2001, 7 p.m.:** Final medical examination of Lunokhod completed → decision to proceed with human.

### First human flight — Ivan Konov (lines 332–354)

> The first man to take part in the experiment was **Ivan Konov**. Possibly this name will go down in history as a name of the first temporonaut… we can be absolutely sure that it was the first attempt to travel the man in Time by means of the technical device, and it is a real fact.
>
> The first flight of a man in Time took place from **7.30 p.m. till 8.00 p.m. (August 26, 2001)**. **Deceleration of the physical Time was registered during the half an hour of reference Time. The maximal decrease in the speed of Time constituted 3% regarding to the speed of reference Earth Time.** Dr. V. Chernobrov, Head of the experiments, made measurements and control of TM from the outside.

### Subsequent volunteers (lines 356–360)

> Since after the Konov's flight, in this day and the next days some more people took part in the experiments on deceleration of Time inside the TM. They were:
> **Dr. V. Chernobrov, V. Fokeev, A. Gavritchenko, D. Kurkov, M. Lorenz, L. Kuleshova, E. Golovina and others.**

**Total roster confirmed: 9 named individuals** (Konov + Chernobrov + 7 others).

### Subjective effects (lines 362–397)

- 1 man among 9 felt nothing.
- 5 of 6 men: slight pulse increase, easy giddiness, mild itch on skin.
- All 3 women reported the largest range of effects: starry sky appearance, luminous vortex, color spots in field of vision, body twist, "astral leaving body", freezing of extremities.
- External observers: only headache.
- **Pre-startup phenomena (most surprising):** ozone smell at hundreds of metres, sudden appearance and disappearance of radiation (instrument-detected), strange lighting effects (including repeated lighting effects in sky above the device), strange sounds from inside, before any apparatus inside could produce them.

### Conclusions (lines 314–423)

- Deceleration vs acceleration are **distinctly different phenomena**: deceleration smooth and stable; acceleration with sharp jumps, dependent on time-of-day, Moon phase, operator presence near TM, mechanical vibration.
- Deceleration "<1 hour per hour" cannot be considered travel to the Past.
- "Present Time is the transition or conversion of a multi-alternative Future Time in the unchangeable Past Time."
- "Law of the top of a tree" — return is possible only if no interference with the past.
- **6-dimensional Earth-world** posited (length, width, height, age/date of Time, variant of History, density/rate of Time) — confirms Bartini's 3-time-dimensions theory.
- Harmful effects: NOT from movement in Time itself, but from **gradient of Time-rate across body parts**.
- White-mist boundary visible between regions of different Time-rate — proposed as biological alarm signal.
- "Inside of the laboratory setup it was also discovered that Time could be changed with some inertia. Areas of space having different Time rates have vague borders."

## §1.2 Frolov — "Practical Application of Time Rate Control (TRC) Theory" (lines 1092–1376)

Co-published companion to Chernobrov's protocol. Key derivations:

### Speed-of-time-course formula (line ~1186, eq. F.1)

> According to Kozyrev, the speed of the course of time (rate of cause-effect transformations) can be calculated as
>
> **υ = c·α ≈ c / 137**         (F.1)
>
> where c is the speed of light. Increase of the fine structure constant means an increase of the speed of the course of time for our space-time.

→ This is **NOT** the f = c/d engineering formula (that comes only in 2003). This is a Kozyrev-derived velocity-of-causality identification with c/137.

### Defense / weapon application

Frolov develops causality-loop weapon concept: if system B can shrink the cause-effect interval such that effect arrives where cause was (with delay), the response action can hit the launching system A by exploiting "speed of time course" reduction in B's space → forcing macro-quantum behaviour. Aether-buoyancy analogy: "the area of slowed time is forced out in the corresponding direction, to the more dense ether. **It is a theoretical basis to create the teleportation systems.**"

### Ether-buoyancy / Mishin reference (line 1330)

> The analogy between ether and liquid is considered and experimentally proved by **Dr. Alexander M. Mishin [7]** and others.

Reference [7]: Mishin A.M. *The physical system of artificial biofield*, NET #1, p. 45; *Main principles of etherodynamics*, NET #2, p. 32. → **Mishin = peer-cited aether researcher, not consultant. Title: "Dr." not "Academician."**

## §1.3 Chernobrov — "Experiments on Change of the Direction and the Rate of Time" (lines 873–918)

Second Chernobrov article in same issue (different framing — historical/methodological). Key technical claims:

- 4 lab systems built since 1988; 5th under construction.
- All clock-types tested: electronic, quartz, mechanical, nuclear; **specially produced doubled quartz generators** to compare frequencies of standard heat-shielded generators.
- Time-rate range investigated: **+0.99 < t/tE < +1.01** — same ±1% envelope as Lovondatr-7.
- Single-experiment record deceleration: **−4 minutes per 8 hours = −30 sec/hour**; routine: −1.5 sec/h decel, +0.5 sec/h accel.
- Maximum EWS Ø ≈ 1 m, minimum (internal) Ø = **115 mm** — sufficient for control equipment, detectors, insects, and lab mice.

## §1.4 Other contributors of interest

- **Butusov** — *Time is a Physical Substance* (lines 519–869): derives Hubble constant H ≈ δ_e ≈ 6.24·10⁻¹⁸ s⁻¹ ≈ 192.6 km/s/MPC from Yarkovsky-mass-growth hypothesis; explains red shift without expansion of Universe; introduces "physical substance-time" filling nuclei. Mathematical-physics ground for the Faraday Lab "aether density = time density" reform.
- **Shikhobalov** (St. Petersburg, NIIM) — Editor-Frolov-annotated review of Kozyrev causal mechanics; introduces relational-vs-substantial time conceptions; positions N.A. Kozyrev as the founder of "active properties of time" doctrine.
- **Abramovich** (Time Institute, Rotterdam) — *Experimenting with Time* (lines 921–1090): EM-spectrum-as-time mathematics, Tesla quotation, **explicit endorsement of Chernobrov as the experimental pioneer**: *"according to the extremely important work of Vadim Chernobrov, the pioneer of intensive experimenting with the change of rate of time flow caused and controlled by EM fields, the path has been found leading to the full cognition and mastering of Time."* (line 1061–1067) — **This is the strongest external endorsement of Chernobrov in NET; comes from a non-Russian academic.**

---

# SECTION 2 — NET #3(6), May–June 2002 (`NET-06-2002`)

## Table of contents (lines 5–25)

1. Large-Scale Sakharov Condition — D. Noever & C. Bremner (NASA Marshall)
2. **Matter as a Resonance Longitudinal Wave Process** — A.V. Frolov
3. **Physical Principles of The Time Machine** — A.V. Frolov ← **REFERENCED AS [8] IN F-12R/NET-12-2003**
4. **Time Machine Project** — A.V. Frolov (Faraday Labs Ltd × Chernobrov contract announcement, May 29 2002)
5. Kozyrev-Dirak Radiation — Ivan M. Shakhparonov
6. The Electrical Vortex Non-Solenoidal Fields — S. Alemanov
7. Physical Mechanism of Nuclear Reactions at Low Energies — V. Oleinik, Yu. Arepjev
8. The Evolution of Lifter Technology — T. Ventura
9. Reality and Consciousness in Education and Activity — A. Smirnov
10. Old New Energy — Y. Andreev, A. Smirnov
11. On the Influence of Time on Matter — A. Belyaeva
12. Life Without Diseases and Ageing-Preventive Electrical Bio-heater Features — A. Belyaeva
13. Technical Report on Belyaeva's High-Efficient Ceramic Heater — Sh. Mavlyandekov
14. **Fundamental Properties of Aether** — A. Mishin
15. Effect of Magnetic Blow Wave Field on Wine Systems — Shakhparonov et al.
16. Nikola Tesla and Instantaneous Electric Communication — V. Korobeynikov
17. The Unified Gravitation Theory — I. Kuldoshin
18. New Sources of Energy from the Point of View of Unitary Quantum Theory — Sapogin, Ryabov, Graboshnikov
19. Antigravitation Force and Antigravitation of Matter — A.K. Gaponov
20. The Capacitor Which Has Energy of Atomic Bomb — Review of Gaponov

## §2.1 Frolov — "Physical Principles of The Time Machine" (lines 706–870)

**This is the article cited in the F-12R patent paper as reference [8].** It does NOT contain the f = c/d derivation — that comes one year later in NET-12-2003. NET-06-2002 article is the **conceptual / qualitative groundwork**.

### Verbatim opening — Chernobrov endorsement (lines 706–768)

> Experimental success of research team headed by Dr. Vadim A. Chernobrov, Moscow was reported in [1]. The time course can be controlled as rate of any process in local space-time (inner space of the Time Machine). It can be decelerated or accelerated by means of special "converging electromagnetic waves"… In Chernobrov's design of the Time Machine this process is organized by means of several spherical envelops, which consist of several electromagnets. Electronic control unit controls the processes in this design. Dr. Chernobrov reported about 3% change of the time course in 4th version of the system, which was tested with a human inside. The goal of Dr. Chernobrov's work is to research the medical aspects and experimental investigation of the principles. Several important conclusions were obtained from the project: the time course can be controlled and character of the changes is different for acceleration and deceleration mode.

**Note the discrepancy:** Frolov writes "4th version… tested with a human inside" — but the human run was actually on **Lovondatr-7** (per Chernobrov's own NET-03-2001 protocol). Either Frolov used an earlier numbering (counting only "main" generations) or this is editorial conflation. The 3% figure matches.

### Aether-vortex and chronal-charge framework (lines 770–869)

- Time is "one of possible description of real physical properties of our Universe" (not abstract math).
- Kozyrev's "time density" → **reinterpreted by Frolov as aether density** (the terminology reform later codified in F-12R).
- **Toroidal aether-vortex-as-autonomous-spacetime** thesis: rotation of heavy cone (lead) entrains aether → toroidal aether ring → laser tangent to cone → luminous ring → autonomous closed 4-D space-time can be built as toroidal aether vortex.
- Critique of Prof. Robert Mallett (Connecticut U.) — *"Mallett is very far from physical basis of the effects. The key of time rate control is technology of artificial aether flow."*
- Introduction of **chronal (temporal) charge**: zero-charge body moves Past→Future at standard rate; decelerated time = negative chronal charge; accelerated = positive.
- **Aether-induction (analog of Faraday induction):** moving chronal charge produces chronal field; accelerated motion produces aether-induction → secondary deceleration of time in nearby area. *"Some provisional data was received by Frolov from simple experiments on the rotation of a heat source."*
- "It is necessary to create or to collect some chronal charge in a 'flux condenser' and then to accelerate it in space up to some velocity." — explicit *Back to the Future* analogy used by Frolov himself.
- **Patent declaration:** *"All new aspects disclosed in this paper are the subject of a patent process. Faraday Labs Ltd organizes experimental program on the topic. Practical application of this technology is new energy systems and propulsion methods."*

### References (line 862–869)

1. Chernobrov V.A. *Experiments with a man in the Time Machine*, NET #3 Nov–Dec 2001, p. 6.
2. Kozyrev N.A. *Selected works*, Leningrad State University, 1991.
3. Frolov A.V. *Practical application of the Time Rate Control theory*, NET #3 Nov–Dec 2001, p. 15.
4. Mallett R.L. *Weak gravitational field of the electromagnetic radiation in a ring laser*, Phys. Lett. A, 2000.

→ Both NET-03-2001 articles cited; **no Mishin reference here** (Mishin appears in [2] of *Matter as a Resonance Longitudinal Wave Process*, the preceding article).

## §2.2 Frolov — "Time Machine Project" / Faraday × Kosmopoisk contract (lines 913–942, dated May 29 2002)

> **Faraday Labs Ltd and Dr. Vadim Chernobrov have signed the agreement on scientific-research work on investigation of active properties of time.**
>
> In the course of the previous experimental works, carried out by Dr. Chernobrov's research team during the period from 1984–2002, four versions of Time Machine had been made and tested. At these devices (the biggest system is about 1 meter in diameter) the effects of deceleration and acceleration of time course were created and measured. The principles of control of time course velocity were based on the interconnection of electromagnetic processes and physical properties of space-time. Special electromagnets, operating in pulse mode, are placed at the spherical frame. They create the so-called converging wave, which by Alexander Frolov is a longitudinal wave in nature.
>
> Coupled with aetherodynamics time conception, which was suggested by Alexander V. Frolov, the works on the control of space-time parameters gain the possibility for development and commercial application. As a theoretical basis there are those N. Kozyrev works where his conception of "time density" are replaced by that of "aether density" according to Frolov.
>
> **In September 2002, Faraday Labs Ltd Company plans to complete testing of the first experimental system, and to start the patenting and research of applied aspects, first of all in medicine.**

**Photo caption confirms:** "Alexander V. Frolov, General Director Faraday Labs Ltd and Ph.D. Dr. Vadim A. Chernobrov have just signed the Contract." → contract signing photographed, May 29, 2002.

## §2.3 Frolov — "Matter as a Resonance Longitudinal Wave Process" (lines ~440–660)

Theoretical groundwork for the longitudinal-wave / aether interpretation. Key claim: every element of matter is a resonance process of aether oscillations (longitudinal); de Broglie matter waves explainable as longitudinal aether waves; gradient of aether pressure → gravity control. References Mishin [2] and Butusov [3].

## §2.4 Mishin — "Fundamental Properties of Aether" (around line 3080)

Mishin's article in this issue (around line 3080 in the OCR; same text as referenced from the longitudinal-wave Frolov paper). Develops ether-as-viscous-gas with antigravitational forces between bodies of different temperature; "non-traditional nuclear processes where conditional reactions of decay and fusion occur at the usage of quasimatter". Self-references prior Mishin papers in NET #1 and #2. **No co-authorship with Chernobrov, no consultant role declared.**

## §2.5 Other notable content

- **Shakhparonov** — *Kozyrev-Dirac Radiation*, *Effect of Magnetic Blow Wave on Wine* (lines 1270, 3239): claims MBW (magnetic blow wave) = magnetic monopole; tests on wine biological aging effect. Shakhparonov-style monopole work is conceptually adjacent to Chernobrov's quasi-monopole but methodologically separate.
- **Ventura** — *The Evolution of Lifter Technology* (line ~2199): T.T. Brown patent history; NASA patent #6,317,310; lifter replication; Transdimensional Technologies; "UFO wreckage" anecdote on materials.
- **Oleinik / Arepjev** — physical mechanism for nuclear reactions at low energies (Chernobyl alternative scenario without monopoles).

---

# SECTION 3 — NET #6, November–December 2002 (`NET-09-2003`)

(Filename `net_09_2003.txt` — but the masthead says "Issue #6 November–December 2002". The internal numbering is one version behind the filename. The four-issue user-provided codename `NET-09-2003` refers to this volume.)

## Table of contents (lines 5–28)

1. **Some Experimental News** — A.V. Frolov
2. On the Possibility of Controlling of the Course of Time — V.P. Oleinik, Yu.C. Borimsky, Yu.D. Arepjev
3. Spontaneous Polarization of Some Glasses and Inexhaustible Energy Source of DC — Sapogin, Ryabov
4. New Fuelless Space Power Engineering — V.D. Dudyshev
5. Electrodynamic Explanation of Ball Lightning — S.B. Alemanov
6. Nature of Torsion Fields — V.V. Uvarov
7. **Matter, Space and Time in Conception of Aether Field** — A.M. Mishin
8. Patent Experts Now are Between a Rock and a Hard Place — V. Sharov
9. Reidar Finsrud's Perpetual Mobile in Norway — John Pasley
10. Physical Quantum Vacuum is a Source of EM Energy — P.M. Shalyapin
11. What is Instantaneous Electrical Communication — V.I. Korobeynikov
12. Investigation of Single-Wire Electric Power System — Strebkov, Avramenko, Nekrasov, Roschin
13. Fuelless Monothermic Engine (Y. Volodko)
14. On Viktor S. Grebennikov Discoveries (review)
15. Experimental Study of Properties of Time (review)
16. Bedini Generator — David Mason
17. Article Update for An Introduction to Gravity — Lew P. Price
18. The CIP Engine Principle — Robert L. Cook
19. The Energy Machine of Joseph Newman — M. Williamson
20. What is RQM Technology? (review)
21. **Experimental Data on Time Control by Acad. A.I. Veinik**
22. The Space Power Generator by P. Tewari (review)

## §3.1 Frolov — "Some Experimental News" (lines 29–276)

Status report on Faraday Lab Ltd 2002 R&D programme. **Critical for cross-referencing NET-12-2003.**

### Vortex Drive (lines 49–82)

- 2002 R&D summary: fuelless power generation, reaction-less propulsion, longitudinal wave generation.
- **Russian Federation patent claim #2002128658** filed October 25, 2002 — *"Method and Device to Create Propulsion Force by Means of Transformation of Rotational Motion into Translational Motion"*. **This is the vortex-drive patent, NOT the time-machine patent.** Cone rotor with helical spiral; aluminum body; rotor outer Ø 80 mm, outlet Ø 20 mm; 12 V battery; 50 W input; balance accuracy 0.1 g.
- Cites prior art: 8 USA patents (Woodward 5280864, Thornson 4631971, Shimshi 5427330, Booden 5782134, Claxton 5557988, Butka 5111087/5334060/5410198, Schnur 3979961) + Russian patent claim #589150 + RU useful-model #34 (Khrunichev Space Center / Menshikov / Akimov / Kachekan / Svetlichny).

### High Efficiency Transformators (lines 134–161)

- Standard transformer, 50×50 mm cross-section, electrotechnical steel, 500 W – 1 kW rating. Goal: over-unity self-running mode via permalloy + digital control unit.

### Magnet Generator-Alternator (lines 162–187)

- Ceramic Barium permanent magnets 50×50×10 mm, 1 Tesla, rotor Ø 400 mm, 12 VDC drive.
- **Frolov's signature design idea:** "decrease of electric input power if useful load is connected to generator coils, i.e. the rotor is accelerated by load connection. This method was proposed by Alexander V. Frolov." Back-EMF as acceleration cause.
- Notes USA-patent prior art with plasma rotor (very complicated).

### Vacuum tube as power generation source (lines 178–187)

- Increase electron kinetic energy via potential (scalar) field after thermionic emission.
- Test bench: GU-74 vacuum tube, present output milliwatts; target kilowatts.

### Longitudinal Wave Generation and Time Control (lines 190–272)

> Longitudinal wave is considered as wave of energy density in space that allows to develop productive aether experimental approach and corresponding technical methods for **space-time engineering, antigravitation and time control ideas**. We have signed Contract with Dr. Chernobrov, Moscow, on the topic and other authors are also involved in the project. **Special conference and workshop are planned (April 2003 in Moscow) to discuss this topic.** One of the systems is a spherical design, on the body there are placed several emitters of the longitudinal waves.
>
> Detection of focused longitudinal waves in the center of the system can be made by means of any radio-electronics element, for example it can be usual resistor of the balanced scheme, transistor or quartz oscillator… We have investigated frequencies up to **1 MHz**. The system is powered by **12 VDC, 15 A** source.

→ This is the **first announcement of the April 2003 Moscow conference** that produces NET-12-2003. Frolov names "Special conference and workshop" as the planned venue. Frequency range "up to 1 MHz" significantly **lower** than the f = c/d 43 GHz target — confirms the f = c/d formula was a **theoretical / design upper limit**, not a measured operating frequency in 2002.

### Processing of Radioactivity Wastes (lines 210–219)

R&D in collaboration with St.-Petersburg atom-smasher lab. Spectrum shift detected; total radioactivity unchanged in test. Continuing.

### Asymmetrical Capacitors as Electrogravitics Propulsion (lines 221–230)

- Replication of T.T. Brown USA patent #3187206 (1965). Solid-state dielectric of "gradiental permittivity" being developed with St.-Petersburg institutes.

## §3.2 Conference announcement form (lines 785–807)

> **Congress "The Time Machine"**
>
> Faraday Labs Ltd invite you to participate in our scientific congress, workshop and discussion on time control topics. It is planned April 2003. Main topics of the congress are the technological basis of time control experiments, practical applications of this method in medicine and other technologies. **Organizing committee: PhD. Vadim A. Chernobrov (KOSMOPOISK research center) and Alexander V. Frolov (Faraday Labs Ltd).**
>
> Please, contact us http://www.faraday.ru or email congress@faraday.ru Phone/fax 7-812-380-6564
> Please send this pre-registration form by post: P.O. Box 37, St. Petersburg, Russia 193024 congress@faraday.ru

→ **Co-chair structure of the conference confirmed: Chernobrov (Kosmopoisk) + Frolov (Faraday Labs).** Pre-registration form printed in the issue.

## §3.3 Oleinik / Borimsky / Arepjev — "On the Possibility of the New Communication Method and Controlling of the Time Course" (lines 277–782)

Kiev Polytechnic Institute + Institute of Semiconductor Physics, Ukraine. Report at VI International Conference *Material Science and Material Properties for Infrared Optoelectronics*, Kiev, May 22–24, 2002.

- Claims STR does not forbid superluminal signals (kinematic vs dynamic argument).
- Quantum-electrodynamic mechanism for cold nuclear reactions: free electron whose ground-state localization is several × hydrogen atom captures multiple nuclei → Coulomb barrier deformed → tunnel fusion. Universal mechanism.
- **Alternative Chernobyl scenario** (line 681–688): rejects Urutskoev's hypothesis of magnetic-monopole reactor penetration; proposes free-electron pulse from electric subcircuit short circuit.
- Cites Akimov, Lavrent'ev, Kozyrev's selected works. **No connection to Chernobrov or Frolov directly** but published as part of the time-control issue.

## §3.4 Acad. A.I. Veinik — "Experimental Data on Time Control" (lines 4805–4823)

Single-page note. **Critical detail for f = c/d cross-reference:**

> The principle of work of the device is based on operations with chronal matter, which first is obtained from the ambient space, then accumulated (concentrated), and radiated. The plates (1) of 350 × 70 × 21 mm size are placed into grooves of pasteboard supports (4), which are installed on the textolite disc (5) of 735 mm diameter. The ring (2) of **70 mm exterior diameter, 7 mm thickness, and 14 mm height** is fixed on the 2.66 meter suspension (3). There were used **70 plates**, directed at a tangent to the middle of the ring (2) thickness.

Reference: Veinik A.I. *Thermodynamics of Real Processes*, Minsk 1991, p. 576, ISBN 5-343-00837.

→ **The "7 mm" appears here as a ring thickness, NOT as an electromagnet axial offset d.** Veinik's chronal-matter device uses 70 plates around a 70 mm ring suspended at 2.66 m. This is an **independent Veinik design** — not Chernobrov-Frolov geometry, not connected to f = c/d. Mention here for completeness; Veinik is referenced as Acad. (academician) — he is the only "academician" actively on the time-control side in this issue.

## §3.5 Mishin — "Matter, Space and Time in Conception of Aether Field" (lines 2252–2376)

Mishin's third NET issue contribution. Develops aether-as-viscous-gas; secondary vortex-wave structures formed by matter; spectrum-energy cascades ("red" and "violet"). References his own NET prior contributions [1]–[6]. **No co-authorship with Chernobrov, no role described as consultant.**

## §3.6 Sharov — "Patent Experts Now are Between a Rock and a Hard Place" (lines 2379+)

Russian Patent Office context piece — confirms patenting environment. Discusses Marsol (perished with family from oil-monopoly action), Latchinov hydrogen electrolysis 1888, Papaleksi 1948. Editor's note frames the legitimacy struggle for over-unity / time-control patents at Rospatent.

---

# SECTION 4 — NET #3 (Issue #12), May–June 2003 (`NET-12-2003`)

This is the post-conference issue documenting the **April 12, 2003 "The Time Machine" conference in Moscow** organized by Faraday Laboratories Ltd. Internal masthead also numbers it "Issue #3 May–June 2003". The "Issue #12" label refers to its position in the cumulative NET sequence.

(Note: this issue is the source for the F-12R Russian-language patent paper already analyzed in detail at `analysis/articles/F-12R_faraday_patent_paper.md`. The English content here is the parallel English edition.)

## Table of contents (lines 3–29)

1. **Works on the Designing of Time Machines** — V.A. Chernobrov
2. **Control of Temporal Parameters of Physical Processes** — A.V. Frolov ← **f = c/d derivation**
3. Etherodynamics as a New Field of Physics — V.A. Atsukovsky
4. Electromagnetic Gravitational Interaction — V.Ya. Kosyev
5. Medium for Existing of Matter in Nature — A.V. Rykov
6. Adams Motor — S.S. Abramov
7. Field Transformation in the Model of Extended Space — D.Yu. Tsipenyuk
8. Joe Flynn's Parallel Path Magnetic Technology — Tim Harwood
9. Flynn Laboratory Photos
10. Flux-machine and Its Analogies (review)
11. Russian Patents on Alternative Energetics
12. Gravitational Spaceships — G.R. Uspensky
13. On Velocity of Drive-Free Motion — S.A. Gerasimov, V.V. Stashenko
14. Electromagnetic Self-Action — S.A. Gerasimov, A.V. Volos
15. Uranium Photoaccumulator — A.I. Yegorov
16. Global Energy Prize (reportage)
17. Teleportation — A.V. Pashova
18. "Mass Defect" in Home Conditions — P.V. Sherbak
19. **Aether as Unified Field** — A.M. Mishin
20. Global Energy — P.M. Kanarev
21. Fusion Processes of Molecules of Oxygen, Hydrogen and Water — P.M. Kanarev
22. Plasma Energy Power Generation — Bruce A. Perreault
23. News
24. The Marcus Device Controversy — Tim Ventura
25. Systems of Conversion of Thermal Energy to Mechanical (review)
26. I. Prigozin
27. Letters

### Editorial framing (lines 30–34)

> On April 12 of 2003 a scientific conference **"The Time Machine"** was organized by Faraday Laboratories Ltd in Moscow, Russia. It was devoted to the experiments on control of spacetime physical properties. At the conference there were discussed problems of time and gravitation in the context of etherodynamics, experiments and applied aspects of these technologies. Below we publish a review of the main reports presented at the conference.

## §4.1 Chernobrov — "Works on the Designing of Time Machines" (lines 37–159)

Conference opening report. Introduces the **quasi-monopole** terminology more rigorously than NET-03-2001.

### Quasi-monopole definition (lines 41–78) — VERBATIM

> To conduct the experiments on the influence upon physical Time (density of space energy) some special devices were used as a general method of such influence. These devices can create converging waves which can cause the appearance of **quasi-monopole** in the confined space. **Quasi-monopole is a part of space which has some parameters of hypothetical unitary monopole or bunch of such particles** (in particular, it allows registering one magnetic pole by means of measuring equipment from the outside at some distance from this pole).
>
> The pilot experiments have shown that it is very difficult (if not impossible) to create long-living quasi-monopole by means of permanent magnets or electromagnets operating on direct currents (in this case quasi-monopole represents a space with one outer and one inner magnetic pole). It can be explained by the fact that lines of force of the "inner pole" invariably find a weak spot in the heterogeneous surface of magnets and break out. As a result, at the device along with one "outer" magnetic pole there is a local output of magnetic lines of the "inner" pole.
>
> During the designing of new devices there was a task to create a quasi-monopole situation in the confined space. **This situation should be created not uniformly but transiently by pulsation method.** Frequency of work of electromagnetic oscillators first of all was selected depending on linear dimensions of the devices. **Selection of the frequency was made in such a way that one period of pulsation does not exceed the period of time which is necessary for electromagnetic waves to reach the center and opposite waves of the device.**

→ This last sentence is the **physical motivation** for the f = c/d formula derived by Frolov in §4.2: the period of pulsation T must not exceed d/c, where d is the device's geometric scale → ω ≥ c/d.

### Devices and EWS layers (lines 65–94)

- Multi-layer "quasi-monopole" with **3 to 5 EWS** (electromagnetic work surfaces).
- Series-and-parallel solenoid oscillators (simplest design).
- Outer EWS Ø 0.9 m max; inner Ø **115 mm** (sufficient for lab animals + control detection devices).
- "Payload" terminology adopted from cosmonautics; placed at center of symmetry.
- "**In all the earliest Machines (except the 7th model) this volume still has not exceeded the volume of a football.** The device with an outer diameter of 2.1 m and inner payload section of 1 m has the maximum size. It allows making human-aided experiments." → confirms 7th = Lovondatr-7 = 2.1 m / 1 m human-bay.

### TM as Time-jet propulsion (lines 90–136)

- Bidirectional Time effect: TM affects payload AND environment; external effect ~×10 smaller, opposite sign, ∝ 1/cube of distance.
- *"In other words, TM influences not only its inner part and pay load but also the environment. It bears a strong resemblance to jet propulsion but in Time and not in Space. It is a flight which is realized by rejection of Time instead of mass."* — original Chernobrov framing.
- Acceleration vs deceleration asymmetry: deceleration smooth, acceleration jumpy (matches NET-03-2001 conclusions).
- Time-rate inertia and residual effects in soil-after-exposure.
- Reaffirms 6-D Earth model (length, width, height, age/date, History-variant, Time-rate).

## §4.2 Frolov — "Method and Device to Control Temporal Parameters of Physical Processes by Means of Changing of Energy Density of Space" (lines 162–427)

**Canonical English-language f = c/d derivation. Same content as F-12R Russian paper.** Verbatim segment:

### Three-layered electromagnet — frequency formula (lines 279–315) — VERBATIM

> Fig. 1 represents a three-layered electromagnetic emitter. This electromagnetic emitter is designed according to the invention in which the directed radiation of wave of energy density is created along the axis of the device.
>
> The device is designed according to the idea by **Vadim A. Chernobrov for creation of the directed wave of energy density by means of phase shift in propagation of impulse front in three current branches**, namely i₁, i₂, i₃. These branches are displaced along the electromagnet axis at some distance d.
>
> The device works in the following way. When the pulsed generator is activated, front of current pulse i₀ appears at the output 4. Impulse front at branch 1 advances impulse front at branch 2 that is caused by spatial shift of current branches 1, 2, 3 relatively to each other along the electromagnet axis at the distance d. Impulse front at branch 2 in its turn advances impulse front at branch 3 for a certain time T. The second output of the electromagnet 5 is placed in such a way that impulse front at branch 1 will phase lag behind the impulse front at branch 2 (which in its turn will phase lag behind the impulse front at branch 3) for the same period of time T. Therefore at branch 5 the united impulse front is generated again.
>
> Time T can be calculated in the following way:
>
> > **T = d / c (seconds)         (1)**
>
> where c is a constant of propagation of impulse front. This constant is known as velocity of light.
>
> At each impulse the T (i.e. the value of relative lag of impulse front) is a constant value. Thus high-frequency consequent excitation of layers of the electromagnet appears at each impulse. The frequency of the excitation is calculated in the following way:
>
> > **f = 1 / T          (2)**
>
> where T is relative lag of impulse front in seconds.
>
> **There is an example of frequency calculation: for the shift distance d = 7 mm we can calculate a lag T = (7 / 2.997924) × 10⁻¹¹ = 2.335 × 10⁻¹¹ (seconds) and frequency f = 1/T approximately comes to 4.28 × 10¹⁰ (Hertz).**
>
> Thus this design of three-layered electromagnetic emitter allows creating the waves of super-high-frequency band (for example of millimeter range) without the use of a semiconductor or other radio components.

→ **f = 1/T = c/d. d = 7 mm → T = 2.335×10⁻¹¹ s → f ≈ 4.28×10¹⁰ Hz ≈ 43 GHz (mm-wave EHF band). Idea attributed to Chernobrov; engineering realization by Frolov. No semiconductor required.**

### Variants and patent claim (lines 312–423)

- **Fig. 2** — magnetostrictive ferrite-core variant (efficiency boost).
- **Fig. 3** — spherical distribution of emitters on upper/lower hemispheres of openable frame.
- **Fig. 4** — detector placement.
- **Fig. 5** — three-layer spherical electric capacitor with three-phase pulsed generator drive (no magnetic monopole modeling required; "compresses/decompresses" aether; aether "pumped in/out" of center).
- **Fig. 6** — gas-filled inner/outer frame, three plasma electrodes, three-phase pulsed gen (consequent layer-wise plasma excitation).
- **Fig. 7** — schematic electric circuit.

> **Russian Federation patent claim #2003110067 was filled April 9, 2003.** At present time we are interested in marketing for this technology as well as in search of additional investment and partners.

References [1]–[12] include Kozyrev, Prigozhin, Sakharov, Puthoff (*Can the vacuum be engineered for space flight applications?*), Butusov (Time as physical substance, 1990; Symmetrization of Maxwell-Lorenz, 1991), Belostotsky, Atsukovsky, **Frolov A.V., Physical Principles of The Time Machine, NET #3(6), pp. 8–10, SPb, 2002 [8]**, Faraday vol. 3, Polyakov, **V.A. Chernobrov, Mysteries of Time, M. 1999 [12]**.

## §4.3 Conference participants (etherodynamics report list)

Per the editorial framing and TOC, the April 12 2003 Moscow "Time Machine" conference key reporters include:

- **V.A. Chernobrov** (Kosmopoisk, Moscow) — opening report on TM design.
- **A.V. Frolov** (Faraday Lab Ltd, St. Petersburg) — control of temporal parameters / f=c/d derivation.
- **V.A. Atsukovsky** — *Aetherodynamics as a New Field of Physics* (Theory and Experiments) — confirms aether wind, references D. Miller 1925 results. Standalone aether-gas / aether-amer model. (lines 428–470)
- **V.Ya. Kosyev** (Nizhny Novgorod) — *Electromagnetic Gravitational Interaction* — Searl-effect converter (350 kg cylindrical stator + 24 magnetic rollers); 35% weight decrease at frequency, 550 rpm spontaneous acceleration, 7 kW electromagnetic transducer load. (lines 471–579)
- **A.V. Rykov** — *Medium for Existing of Matter in Nature* — physical-vacuum-as-electric-dipole-lattice; (+) and (-) charge difference 7.85×10⁻⁴¹ C generates gravity. (lines 581–711)
- **D.Yu. Tsipenyuk** — Field transformation in extended space.
- **A.M. Mishin** — *Aether as Unified Field* — sequel to his earlier NET aether work; aether vortex hierarchy / matreshka structure, energy-information barrier, biofield as topoharmonic part of physical body, yang/yin balance. (lines 2704–2941)

### Mishin in NET-12-2003 — title verification (line 2704)

The byline reads **"Alexander M. Mishin, Russia"** with address Planernaya Str., 79-208, St. Petersburg. **No academician title given.** Mishin's references in this article cite his own earlier NET papers and his 1996/1999/2001/2003 RAS conference proceedings — he is a member of the same Faraday-publishing-orbit but presented as an independent peer researcher.

## §4.4 Other content of interest

- **Atsukovsky's photo** appears at line 466 in the editorial layout (caption: "Report by Vladimir A. Atsukovsky").
- **Kanarev** (Kuban State Agrarian University) — *Global Energy* and *Fusion Processes of Molecules*: claims 10× efficiency electrodynamic water destruction; cites *Yusmar*, *Termovikhr*, *Noteka* commercial cavitation heaters.
- **Pashova** — *Teleportation* (lines 2432+): EPR-paradox review; quantum-state teleportation history (Aspect 1980, Bennett 1993, Zeilinger 1997, Polzik 2001 cesium-cloud pair); Australian National University laser-beam teleport.
- **Ventura** — *The Marcus Device Controversy*: continuation of his lifter/electrogravitics coverage from NET-06-2002.
- **Russian Patents on Alternative Energetics** (item 11) — collected patent abstracts.

## §4.5 Patent process discussion

- Frolov's article ends with the explicit RU patent claim **#2003110067 / April 9, 2003** for the time-machine quasi-monopole device.
- Editorial note (Kanarev section, line ~3001): *"It is known that a priority of results of theoretical investigations is their publication in press. Usually, such priority is a personal one. Generally a patent is a priority of the results of experimental investigations… A published patent is a genie released from a bottle. No finesse of the authors to hamper a reproduction of experimental data given in a patent without the participation of the authors can stop the process of their implementation."* — general patent-philosophy framing for the issue.
- Russian Patents review (item 11): published patent specifications of Russian alternative-energetics inventions.

---

# CROSS-ISSUE INDEX

## Lovondatr generation map

| Generation | Source citation | Geometry | Year |
|---|---|---|---|
| Lovondatr-1 | NET-03-2001 line 916–918 (implicit "first laboratory system since 1988"); NET-12-2003 line 82–84 | outer ≈ 0.9 m, inner ≈ 115 mm | 1988+ |
| Lovondatr-4 | NET-06-2002 line 737–739 | (Frolov says "4th version… tested with a human inside" — 3% effect) | ~1996–2000 |
| Lovondatr-7 | NET-03-2001 lines 281–311 (explicit naming), NET-12-2003 line 94 (implicit) | nested 2.1 m × 1.0 m × 0.30 m | summer–Aug 2001 |

## Frolov's NET article timeline

| Issue | Title | Key contribution |
|---|---|---|
| NET-03-2001 | Practical Application of TRC Theory | υ = c·α ≈ c/137 (Kozyrev derivation) |
| NET-06-2002 | Matter as Resonance Longitudinal Wave Process | de Broglie / longitudinal aether identification |
| NET-06-2002 | Physical Principles of The Time Machine | Aether-density terminology reform; chronal charge; "flux condenser" Back-to-the-Future analogy |
| NET-06-2002 | Time Machine Project | May 29 2002 Faraday × Kosmopoisk contract signing |
| NET-09-2003 | Some Experimental News | Vortex-drive RU patent #2002128658 (Oct 25 2002); April 2003 conference announcement |
| NET-12-2003 | Method and Device to Control Temporal Parameters | **f = c/d derivation; RU patent #2003110067 (April 9 2003)** |

## Chernobrov's NET article timeline

| Issue | Title | Key contribution |
|---|---|---|
| NET-03-2001 | Experiments with a Man in the Time Machine | **Lovondatr-7 protocol; Ivan Konov; 9 named volunteers; 3% deceleration; Aug 26 2001** |
| NET-03-2001 | Experiments on Change of the Direction and Rate of Time | Methodological/historical companion; ±1% Time envelope; doubled quartz generators |
| NET-12-2003 | Works on the Designing of Time Machines | Conference report; **rigorous "quasi-monopole" definition**; pulsation period ≤ d/c motivation; 7th-model = 2.1 m / 1 m human bay |

## Mishin's NET article timeline (relevant subset)

| Issue | Title | Position in Faraday-Chernobrov work |
|---|---|---|
| NET #1 (2001) | The Physical System of Artificial Biofield | Background reference for ether-as-liquid analogy |
| NET #2 (2002) | Main Principles of Etherodynamics | Background reference |
| NET-06-2002 | Fundamental Properties of Aether | Independent peer contribution; cited by Frolov [2] in *Matter as Resonance LW Process* |
| NET-09-2003 | Matter, Space and Time in Conception of Aether Field | Independent peer contribution |
| NET-12-2003 | Aether as Unified Field | Conference contribution; aether-vortex matreshka; biofield as topoharmonic |

→ **Mishin published 5 articles across NET in 2001–2003. He is consistently styled "Dr. Alexander M. Mishin" (no academician). He is cited by Frolov as supportive theoretical-experimental backdrop on aether-as-viscous-gas, but he is NOT named as a consultant, co-author, contract party, or executive collaborator on the Chernobrov-Frolov time-machine project.**

## Conference cross-reference (USER-RES §17 / §18)

The April 12 2003 "Time Machine" conference participants identified across NET-09-2003 (announcement) and NET-12-2003 (proceedings):

- **Confirmed organizers:** V.A. Chernobrov (Kosmopoisk) + A.V. Frolov (Faraday Labs Ltd)
- **Confirmed speakers (NET-12-2003 TOC + bylines):** Chernobrov, Frolov, Atsukovsky, Kosyev, Rykov, Tsipenyuk, Mishin
- **NOT confirmed in NET text (claimed in USER-RES §18):** E.D. Sorokodum, A.N. Solenyy — these names do NOT appear in NET-12-2003's TOC, bylines, or editorial frame. They may have been speakers but no NET-published proceedings record them.

---

# DELTAS VS EXISTING ARCHIVE

Items here that are **NOT** in `analysis/articles/F-12R_faraday_patent_paper.md` or `analysis/articles/articles_and_patent.md`:

1. **Full Lovondatr-7 protocol with named 9 volunteers** — Konov + Chernobrov + Fokeev + Gavritchenko + Kurkov + M. Lorenz + Kuleshova + Golovina + "others". F-12R explicitly stated this was missing from its source file.
2. **Animal-experiment narrative** — 31 mice (25 dead), Plombir cat refusal, Lunokhod dog 108-min release, Aug 26 2001 chronology including 7 p.m. medical exam.
3. **Subjective effects per gender** — 1 of 9 men felt nothing; 5 of 6 men slight effects; all 3 women full effects (starry sky, luminous vortex, body twist, astral leaving).
4. **Pre-startup phenomena** — ozone at hundreds-of-metres, sky lighting effects, radiation appear/disappear.
5. **Frolov NET-06-2002 "Physical Principles" full text** — the qualitative aether-vortex / chronal-charge / aether-induction / Back-to-the-Future framework that precedes the f=c/d engineering derivation. F-12R only cross-referenced this as [8].
6. **Faraday × Kosmopoisk contract date (May 29 2002)** with photographic confirmation of signing.
7. **NET-03-2001 Frolov "Practical Application of TRC Theory"** — υ = c·α ≈ c/137 derivation; Kozyrev causality-loop weapon application; teleportation theoretical basis.
8. **Frolov's vortex-drive patent RU #2002128658 (Oct 25 2002)** — separate from time-machine patent; 80 mm/20 mm cone-rotor design.
9. **Cumulative R&D map of Frolov 2002 programme** — vortex drive + high-eff transformer + magnet alternator + vacuum-tube ZPE + longitudinal-wave/time + radioactivity processing + asymmetric capacitor (T.T. Brown).
10. **Veinik (NET-09-2003) experimental device specs** — 70 plates, 350×70×21 mm, 70 mm Ø ring with 7 mm thickness, 2.66 m suspension. Veinik's "7 mm" is unrelated to the Chernobrov-Frolov f=c/d offset.
11. **April 2003 Moscow conference advance announcement and pre-registration form** (NET-09-2003 lines 785–807).
12. **Abramovich (Rotterdam) endorsement of Chernobrov as the international experimental pioneer** (NET-03-2001 lines 1061–1067).
13. **Mishin authorship census** — 5 articles, never as academician, never as project consultant.
14. **Patent-process editorial framing** — Sharov (NET-09-2003) on Russian Patent Office obstruction; Kanarev (NET-12-2003) on patent-as-priority philosophy.

# OUTSTANDING / UNRESOLVED

- The Frolov-conflated "4th version… tested with a human inside" (NET-06-2002) vs Chernobrov's own "Lovondatr-7 = 2001 human run" (NET-03-2001) — likely an editorial slip; the actual human run was on the 7th machine. Worth noting in any narrative reconciliation.
- USER-RES §18 names "А.Н. Солёный" and "Е.Д. Сорокодум" as conference speakers — not present in NET-published proceedings; either NET selected only a subset of presentations for publication, or the USER-RES conference roster derives from a different source (faraday.ru landing page archives?).
- Mishin's *consultant* role asserted in USER-RES is unsupported by NET; if such a role exists, it must come from a non-NET source (private correspondence, faraday.ru notices, or a misreading of his peer-author position).
