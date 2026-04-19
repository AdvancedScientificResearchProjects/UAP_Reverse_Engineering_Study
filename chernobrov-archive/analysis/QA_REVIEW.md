## Review Gate 1 — Batch 1 Chernobrov transcripts 07-19 audit (2026-04-18)

**Reviewer:** Fresh QA agent (Opus 4.7), no prior context from Batch 1 producers
**Scope:** 5 per-interview files + case catalogs + 5 topical files covering transcripts 07-19
**Primary reference:** USER-RES-2026-04-18
**Verdict:** **PASS** — analysis fidelity is high; minor clarifications recommended (see §G).

---

### Check A — Hallucination sample (25 verbatim quote verifications)

Quotes sampled diversely across the 5 per-interview files and verified against transcripts with ±30s timestamp tolerance.

| # | File / Code | Timestamp | Quote fragment | Verdict |
|---|-------------|-----------|----------------|---------|
| 1 | 07_13 / HRON-14 | [01:47:29] | "мы вынуждены делать многослойные установки" | VERBATIM |
| 2 | 07_13 / HRON-14 | [01:47:48] | "как матрешка в матрешке" | VERBATIM |
| 3 | 07_13 / HRON-14 | [01:51:14] | "из семи сфероидов … осталось шесть" | VERBATIM |
| 4 | 07_13 / HRON-14 | [01:31:40] | "порядка 40 тысяч оборотов в минуту" | VERBATIM |
| 5 | 07_13 / HRON-14 | [01:03:23] | "порядка 200 случаев за год" | VERBATIM |
| 6 | 11_12 / GH-14 | [01:14:30] | "квазимонополь" + rotating EM fields | VERBATIM |
| 7 | 11_12 / GH-14 | [01:30:31] | "лов-андатор … зашифрованное для своих" | VERBATIM |
| 8 | 11_12 / GH-14 | [01:44:30] | "использовали 5-оболочные машины" | VERBATIM |
| 9 | 11_12 / GH-14 | [00:35:03] | "дублированных кварцевых генераторов" | VERBATIM |
| 10 | 11_12 / GH-14 | [00:38:02] | "центрифуге … доводили до 9G" | VERBATIM |
| 11 | 11_12 / GH-14 | [00:42:12] | "в парке Горького … прыгал с тарзанки" | VERBATIM |
| 12 | 08_09_10_14_19 / 3ZV-NLO | [00:07:58] | "от нуля … до 20 тысяч километров в час" | VERBATIM |
| 13 | 08_09_10_14_19 / 3ZV-NLO | [00:19:37] | "80 на 80 на 50 метров треугольник" | VERBATIM |
| 14 | 08_09_10_14_19 / PM-39 | [00:02:34] | "материалист … не верю в то, что не написано в учебнике физики" | VERBATIM |
| 15 | 08_09_10_14_19 / PM-39 | [00:13:21] | "в шестимерном пространстве-времени" | VERBATIM |
| 16 | 08_09_10_14_19 / PM-39 | [00:30:15] | "мы живем в шестимерном пространстве времени" | VERBATIM |
| 17 | 15_17_18 / MG-DOC-17 | [00:03:26] | "высотах не ниже 40 сантиметров" (ball lightning) | VERBATIM |
| 18 | 15_17_18 / MG-DOC-17 | [00:04:23] | "четырьмя сотнями" (~400 ball-lightning traces) | VERBATIM |
| 19 | 15_17_18 / MG-DOC-17 | [00:06:07] | "пастух Бесен Мамай" | VERBATIM |
| 20 | 15_17_18 / MG-DOC-17 | [00:14:22] | "80 на 50 метров" triangle footprint | VERBATIM |
| 21 | 15_17_18 / MG-DOC-17 | [00:18:19] | "14 экземпляров и 6 модификаций" | VERBATIM |
| 22 | 15_17_18 / NLO-DPL-24 | [01:29:22] | "200 случаев, только по России" | VERBATIM |
| 23 | 16 / KP-LEC-13 | [01:51:57] | "в полтора раза, ровно, не больше, не меньше" (radiation) | VERBATIM |
| 24 | 16 / KP-LEC-13 | [01:02:33] | "уфолог Хребалин из города Лабинска" | VERBATIM |
| 25 | 16 / KP-LEC-13 | [01:07:58] | "пилот Балуев, который их фотографировал" | VERBATIM |

**Result: 25/25 VERBATIM, 0 hallucinations, 0 timestamp-off, 0 paraphrased.**

**Per-file hallucination score:**
- `07_13_heavy_mv.md`: 5/5 VERBATIM
- `11_12_mv_lectures.md`: 6/6 VERBATIM
- `08_09_10_14_19_thematic.md`: 5/5 VERBATIM
- `15_17_18_field_media.md`: 6/6 VERBATIM
- `16_krugi_na_polyakh.md`: 3/3 VERBATIM

**Check A verdict: PASS**

---

### Check B — Numerical-claim cross-check against USER-RES-2026-04-18

| Claim | Agent asserted | Source-grep verdict | USER-RES position | Status |
|-------|---------------|---------------------|-------------------|--------|
| 7-layer matryoshka (file 07) | "из семи сфероидов … осталось шесть" as 4.5m unit; maximum in-use 5-shell (file 11) | File 07 [01:51:14] = 7 planned, 6 final; File 11 [01:44:30] = "максимально … 5-оболочные" | USER-RES 3-5 typical | CONSISTENT. Agent's "7-layer" framing in 07_13 references the 7-sphere assembly plan. The deployed-max is 5 (GH-14) or 6 (HRON-14 4.5m). No false extension of USER-RES. |
| 40,000 rpm rotation | File 07 [01:31:40] | VERBATIM — "при скоростях вращения порядка 40 тысяч оборотов в минуту" | Not in USER-RES — NEW finding | VERIFIED NEW |
| 14 installations + 6 modifications (MG-DOC-17) | File 15 [00:18:19] | VERBATIM — "создано 14 экземпляров и 6 модификаций" | USER-RES §11 table = minimum 7 | VERIFIED EXTENSION. USER-RES is a floor count ("минимум 7 Ловондатр"); the 14+6 figure is a total-over-30-years accounting that subsumes Ловондатр + follow-on platforms. Not in conflict. |
| 80×50m triangle (MG-DOC-17) vs 80×80×50 (USER-RES / file 08) | File 15 says 80×50 (footprint); File 08 says 80×80×50 (full triangle reconstruction) | Both VERBATIM in respective sources | USER-RES cites 80×80×50 | NOT A CONTRADICTION. File 15 [00:14:22] reports the visible crop footprint ("80 на 50"); file 08 [00:19:37] reports the reconstructed airborne triangle geometry ("80×80×50"). Different measurements. Agent's framing could be clearer but is not wrong. |
| 1.5× radiation DECREASE in circles (file 16) | File 16 [01:51:57] | VERBATIM — "понижается на одну цифру … в полтора раза, ровно" | USER-RES says "понижение ~30%" | CONSISTENT. "В полтора раза" = ÷1.5 = –33.3%, matching USER-RES "~30%" rounded. |
| 400 ball lightning traces on single slope (MG-DOC-17) | File 15 [00:04:23] | VERBATIM — "исчислялось четырьмя сотнями" | Not in USER-RES — NEW | VERIFIED NEW |
| 200 unexplained cases/year Russia (NLO-DPL-24) | File 17 [01:29:22] + file 07 [01:03:23] | VERBATIM twice — "порядка 200 случаев" | Not in USER-RES — NEW | VERIFIED NEW (cross-confirmed in two independent lectures) |

**Check B verdict: PASS — all numbers trace to exact verbatim source; agent's claimed new findings (40k rpm, 14+6 installations, 400 ball-lightning, 200 cases/yr) are all genuine extensions of USER-RES, not hallucinations.**

---

### Check C — Grep for Lazar / element 115 / Area 51 / Roswell / S-4

Patterns searched (case-insensitive) across all 19 transcripts:
- `лазар|Lazar|Боб Лаз` → **0 matches**
- `115 элемент|element 115|элемент 115` → **0 matches**
- `Area 51|Зона 51|Розуэлл|Roswell|S-4|Сикрет-4` → **0 matches**
- `муаскоп|Moscovium|Unbip|унбиб` → **0 matches**

**Check C verdict: PASS — agent's claim of ZERO mentions across all 19 transcripts is CONFIRMED.**

Important negative finding: Chernobrov's entire lecture corpus (19 files, ~1.5M chars of transcribed Russian) contains NO reference to Bob Lazar, element 115, Area 51, or Roswell. This is load-bearing for the MASTER synthesis — Chernobrov's time-machine program is developed in complete rhetorical isolation from American reverse-engineering folklore.

---

### Check D — Duplicate flagging (file 01 vs file 13)

Sampled the opening 40 lines of both files. Findings:
- Both begin with identical venue ("Муром"), identical date framing ("середина лета 2014 года" at [00:02:03]), identical transit itinerary (Северный Ледовитый океан → Волга/Волгоград → Медведицкая гряда), identical flashback list (Владимир, Юрьев-Польский, Вологодская область, Архангельская область).
- Both are 2h37m, both attributed to Муром 2014 Kosmopoisk transit lecture on Машина Времени.
- YouTube IDs differ (`fAeumSyWHAk` vs `yeL7msYWhxc`), confirming separate uploads.
- Phrase "у меня с собой на флешке доклады по полсотни разным тем" appears verbatim in both at ~[00:02:23].

**Check D verdict: PASS — duplicate flag is ACCURATE.** File 01 and file 13 are two re-encodings/re-uploads of the same Murom 2014 lecture. The agent's ~80% overlap estimate is defensible. Agent correctly derived novel content in file 07 (HRON-14 Guzeripl 2014) while marking file 13 as NEW-vs-DUPLICATE-flagged relative to file 01.

---

### Check E — Case-catalog completeness (file 16 crop circles)

- Case entries: **38 numbered (## 1 — ## 38) + 1 Appendix (## 39) = 38 enumerated + lost-cases appendix**. Matches agent's "38 cases" claim.
- Sampled 5 case timestamps:
  1. Медведицкая гряда 1993 → Хребалин at [01:02:33] ✓
  2. Новокубанск 1996 → Балуев at [01:07:58] ✓
  3. Свекольное поле 1999 → [01:21:18] ✓
  4. Васюринская 2013 → [02:17:06]–[02:18:46] ✓ (within the recoverable framing window of the transcription-gap segment)
  5. Point-source reconstruction 2009 → [02:32:43] "высоте порядка полусотни метров" ✓

- **Denis-hypothesis honesty check:** File 16 per-interview explicitly states "Verdict: NO EXPLICIT IDENTIFICATION in this lecture. Chernobrov does NOT utter the word 'Ловондатр' or any reference to his own lab device during the pictogram discussion." Confirmed by grep: 0 occurrences of Ловондатр/лов-андатор/ловушка/ондатр in file 16 transcript. Agent is honest about the bridge being inferential.

**Check E verdict: PASS**

---

### Check F — 14-minute transcription gap in file 16

- Gap confirmed: lines 1117–1162 of transcript `16_KrugiNaPolyakh_2013_2h57.txt` span [02:17:52] → [02:32:12] (≈14.3 min).
- Content: 40 near-identical repetitions of "Пиктограмма Васюринская." at roughly 20s intervals — classic ASR stuck-state failure.
- Recoverable framing: intact Chernobrov speech at [02:17:06]–[02:18:46] provides the Vasyurinskaya intro (horse eyewitness, steam, hot earth, 24°C background, slight warmth inside, week-later persistence). Resume at [02:32:12] picks up with "случай с 2009 годом, легко геометрические построения" — topic shift to point-source reconstruction. 
- What is lost: bulk of the Vasyurinskaya July 2013 field account + possibly 1-2 intermediate cases.

**Check F verdict: PASS — agent's transcription-gap flag is accurate; damage scope correctly described.**

---

### Check G — Minor clarifications recommended (not blocking)

1. **File 07 §1.1 ("7-layer matryoshka"):** The cleanest reading of [01:51:14] is "7 spheroids in the initial build → 6 in the final assembly" NOT "7 nested shells." The file's cross-reference note already flags this as a 4.5m unit. Recommend adding explicit note: "7 sphere count is the assembly plan; effective shell maximum per GH-14 [01:44:30] is 5."

2. **File 08 vs File 15 "80×50 vs 80×80×50":** Two genuinely different measurements (crop footprint on Medveditskaya vs full-triangle reconstruction). Agent correctly records each. A single sentence cross-reference between the two per-interview files would prevent MASTER-synthesis confusion.

3. **USER-RES §11 "минимум 7 Ловондатр" vs MG-DOC-17 "14 экземпляров":** Agent noted this as "consistent"; recommend explicit bridging sentence: "USER-RES count is Ловондатр-family only (7+); MG-DOC-17 14 = Ловондатр + додекаэдральные + tесловские follow-on platforms over 30 years." Source support comes from file 07 [01:49:46] "около 10 установок. Говорю около, потому что трудно их точно посчитать. Части одной становились частью другой."

---

### Overall Verdict: **PASS**

- **Check A:** 25/25 quotes VERBATIM, 0 hallucinations.
- **Check B:** All numeric claims traced to exact source text.
- **Check C:** Zero Lazar/115/Area51/Roswell mentions confirmed across all 19 transcripts.
- **Check D:** file 01/13 duplication flag accurate.
- **Check E:** 38 enumerated cases confirmed; Denis-hypothesis flag honest.
- **Check F:** 14-min transcription gap confirmed.
- **Check G:** Three minor clarifying footnotes recommended but non-blocking.

Batch 1 analysis is cleared for progression to MASTER synthesis.

---

## Review Gate 2 — Batch 2 Validation (2026-04-18)

**Reviewer:** Fresh QA agent (Opus 4.7, 1M-context), no prior context from Batch 2 producers
**Scope:** 14 merged `B-*` bibliographic references + 2 article analyses (16 files, ~1.06 MB total) + 21 chunk-extract predecessors, cross-checked against 32 source FB2 texts, 9 chunk sources, and 10 raw-HTML/PDF extracts.
**Primary reference:** USER-RES-2026-04-18 (`03_user_provided_research_2026-04-18.md`).
**Verdict:** **CONDITIONAL PASS** — extraction fidelity is high (29/30 quote-checks hit source within normalisation tolerance; 1 paraphrase). Three non-trivial issues must be resolved before MASTER synthesis: (a) the "2 sec lethality" number carried in USER-RES is contradicted by the source books (which say 1.5 sec); (b) the "50 landing sites as Ловондатр design basis" claim is **not found anywhere** in the corpus (nor in USER-RES); (c) the "academic Мишин consulted on Ловондатр" claim is **not in any book** (only in a secondary research doc, `01_early_kosmopoisk`). These three must be re-sourced or retracted in Batch 3.

---

### §1 Executive Summary

| Check | Result |
|---|---|
| A. Hallucination spot-check (30 quotes) | **29/30 MATCH** (24 verbatim, 5 match-after-normalisation for NBSP `\u00a0` / soft-hyphen `\u00ad` / quote-style «»↔„" / guillemets). **1 PARAPHRASE** (B-MG05 "Бесен Мамай" — only "Мамай" verifiable in MG-05 FB2 source; "Бесен" not present). 0 hallucinations, 0 source-missing. |
| B. USER-RES numerical alignment | Majority align; **3 load-bearing conflicts** + **2 confirmed EXTENSIONS**. See §3. |
| C. Completeness inventory | 14 merged + 21 chunks + 2 article files = 37 outputs. Covers 33 distinct FB2 works (the 13 books that got full `B-*` files plus 20 short works inside `B-SMALL_batch1`+`batch2`). **0 files missing** vs FB2 source (32 texts) — in fact, coverage = 103 % because SMALL batches also absorb a duplicated "Остановись, мгновенье" variant and the two duplicate FB2s (`11101` alt + `536017`). |
| D. Chunk-merge integrity | All 6 merged B-* spot-checked reference their predecessor chunk IDs explicitly (`[PV-01-p1]`, `[TV99-p1]`, etc.). Key claims from chunks (e.g. PV-01-p1 char 167 000 for Ловушка-на-зверя) carry through to merged file with correct offsets. |
| E. Critical-flag audit | 5/5 flags resolved; see §6. |

---

### §2 Hallucination Spot-check — 30 Quotes

Normalisation applied: `\u00a0`→space, `\u00ad`→`''`, `«»`/`„"` unified, HTML entities decoded. "MATCH" = verbatim or match-after-normalisation. Sources = `fb2_text/*.txt` or `extracted_text/*.txt` depending on file type.

| # | Merged file | Quote fragment | Expected source | Result |
|---|---|---|---|---|
| 1 | B-PV01 | «Ловушку на зверя» | 527877_Puteshestviya | **MATCH** (off 166804) |
| 2 | B-PV01 | «мышь Номер Семь» | 527877_Puteshestviya | **MATCH** (off 178069) |
| 3 | B-PV01 | «Размер электромагнитной рабочей поверхности в первой» | 527877_Puteshestviya | **MATCH** (off 167902) |
| 4 | B-PV01 | «30 секунд/час» + «4 минуты за 8 часов» | 527877_Puteshestviya | **MATCH** (both present; after `\u00ad` strip) |
| 5 | B-PV01 | «сфера, каждая точка которой излучает» | 527877_Puteshestviya | **MATCH** (off 161412) |
| 6 | B-TV99 | «Первая модель МВ «Ловондатр» была закончена» | 81958_Tayny_Vremeni | **MATCH** (off 701178; merged file uses „" low-high quotes, source uses «» guillemets — normalisation trivial) |
| 7 | B-TV99 | «Николаю КО3ЫРЕВУ — посвящается» (note: digit 3 in "КО3ЫРЕВ" is OCR artefact carried through verbatim) | 81958_Tayny_Vremeni | **MATCH** (off 916; OCR kept) |
| 8 | B-TPV01 | «Ну а перелом в проведении опытов наступил в 1997» | 634626_Tayny_i_paradoksy + 81958 | **MATCH** (both editions) |
| 9 | B-TPV01 | «Глава изъята по соображениям цензуры» | 634626/81958 | **MATCH** |
| 10 | B-SS | «АВТОСТОП НЕ САМОЦЕЛЬ, А СПОСОБ ДОСТИЖЕНИЯ ЦЕЛИ» | 81959_Spravochnik_stalkera | **MATCH** |
| 11 | B-SS | «тайга — закон, медведь — прокурор» | 81959_Spravochnik_stalkera | **MATCH** (merged file used ASCII hyphens; source uses em-dash) |
| 12 | B-SS | «1,5 сек/час» | 81959_Spravochnik_stalkera | **MATCH** (off 431554) |
| 13 | B-MG05 | «Медведицкая гряда» (title fidelity) | 867021_Medveditskaya_gryada | **MATCH** (89 occurrences across 16 files) |
| 14 | B-MG05 | «пастух Бесен Мамай» (Batch-1 QA quote carried over in MG-05 context) | 867021 + 537990 | **PARAPHRASE** — MG-05 FB2 contains "Мамай" (5 hits) but not "Бесен". Full name appears in the `15_17_18_field_media.md` transcript from Batch-1. Merged B-MG05 treats MG-DOC-17 transcript material separately so this is not strictly wrong, but Batch-3 should cite the transcript rather than the book for this name. |
| 15 | B-PMF | «Подмосковье» / «феномены» | 634914_Podmoskove_fenomeny | **MATCH** |
| 16 | B-MPN | «Места посадок НЛО — По следу „Треугольника"» | 536019_Mesta_posadok_NLO | **MATCH** |
| 17 | B-MPN | «17 более-менее достоверных мест посадок НЛО в этой зоне» | 536019_Mesta_posadok_NLO | **MATCH** (numerically load-bearing — see §6 item 3) |
| 18 | B-EZM | «Энциклопедия загадочных мест Земли» | 178644_Enciklopediya_zagadochnykh | **MATCH** |
| 19 | B-EAYAV | «Энциклопедия аномальных явлений» | 537990_Enciklopediya_anomalnykh | **MATCH** |
| 20 | B-EAYAV | «Ловондатр» (cross-index presence) | 537990 + 7 other FB2 | **MATCH** (17 occurrences in 8 files) |
| 21 | B-TPM | «Тайны параллельных миров» | 92671_Tayny_parallelnykh_mirov | **MATCH** |
| 22 | B-SVL | «академик Мишин» | 536011_Sushchestvuyut_voperi_logike | **MATCH** (context = Nazi-UFO docs, NOT Ловондатр consulting — see §6 item 4) |
| 23 | B-SVL | «существуют вопреки логике» | 536011 | **MATCH** ("Существуют" title-case; "вопреки логике" phrase 6 hits in 4 files) |
| 24 | B-TMV | «Тунгусский» | 536010_Tungusskiy_meteorit_i_vremya + others | **MATCH** |
| 25 | B-KP | «Круги на полях» | crop_circles_raw.txt (PDF-extracted) | **MATCH** |
| 26 | B-KP | 153 подтверждённые формации (numeric count) | crop_circles_raw.txt | **MATCH** (count corroborated in Batch-1 QA check at file 16) |
| 27 | B-SMALL | «Мишин» + «Луноход» | 536011 + 536009 | **MATCH** |
| 28 | F-12R | «3000 МГц» (NLO emission freq → design param) | faraday_12rus + 634626 + 536011 + 178644 + 634914 | **MATCH** (10 total hits) |
| 29 | F-12R + articles | «RU 2003110067» + patent-filed date | faraday_12rus + net_12_2003 | **MATCH** (2 hits) |
| 30 | articles | «Ivan Konov» / «Иван Конов» | net_03_2001 (English only) + 867021_Medveditskaya (Russian, as "И. Конов") | **MATCH** (surprise finding — Конов appears in MG-05 book too, not only in NET 2001) |

**Result:** 29/30 MATCH, 1 PARAPHRASE, 0 hallucinations, 0 source-missing.
**Per-file score:** B-PV01 5/5, B-TV99/TPV01 4/4, B-SS 3/3, B-MG05 1/2 (Бесен Мамай paraphrase), B-PMF 1/1, B-MPN 2/2, B-EZM 1/1, B-EAYAV 2/2, B-TPM 1/1, B-SVL 2/2, B-TMV 1/1, B-KP 2/2, B-SMALL 1/1, F-12R 2/2, articles_and_patent 1/1.

---

### §3 USER-RES Alignment / Conflict Table

Every numerical/qualitative claim shared between a merged file and USER-RES was checked. Status codes: **ALIGN** = same number/phrase; **EXTEND** = books add detail beyond USER-RES (not contradicting); **CONFLICT** = direct contradiction between book and USER-RES.

| # | Claim | Merged-file value | USER-RES value | Source-grep | Status |
|---|---|---|---|---|---|
| 1 | First Ловондатр build finished / working | 7 April 1988 (built) / 8 April 1988 (working) | Identical | 81958 off 701178 | **ALIGN** |
| 2 | 5-year production → 4 installations | 4 installations 1988–1993 | Identical | 81958 off 706 875 | **ALIGN** |
| 3 | Outer ЭРП (model 1) | ≈ 1 m | ≈ 1 m | 527877 off 167 902 | **ALIGN** |
| 4 | Inner ЭРП (model 1) | 115 mm | 115 mm | 527877 off 169 333 | **ALIGN** |
| 5 | ЭРП layer count | 3–5 | 3–5 (USER-RES §1 and §6 both) | 81958 off 704 753 | **ALIGN** |
| 6 | ANIMAL LETHALITY THRESHOLD | **1.5 секунды** (PV-01, TV-99, TPV-01 all verbatim) | **2 секунды** (USER-RES §1, sentence 5) | Books: 2 hits "разницы в 1,5"; 0 hits for "2 секунды" in any FB2 | **CONFLICT — USER-RES appears wrong. Books say 1.5 s, not 2 s.** |
| 7 | Max recorded slowdown/speedup | **30 сек/час** (single outlier) / **−1.5 сек/час слышать stable / +0.5 сек/час stable** | USER-RES §1 row: "до 40 секунд в час"; "first model 0.5 s/h, later 40 s/h" | Books: "30 секунд/час" = 4 hits; "40 секунд в час" = 0 hits; "40 сек/час" = 0 hits | **CONFLICT — USER-RES "40 s/h" figure is not in any book. The correct single-outlier book value is 30 sec/hr; stable band is ±1.5 / +0.5.** |
| 8 | Payload volume (small) | "не превышал объёма футбольного мяча" | same | 527877 + 81958 | **ALIGN** |
| 9 | 30 April 1991 open-schema test | **absent from books** (only mentioned in USER-RES §1) | Thrust ~10 g on 400 g model | not found in any FB2 | **CANNOT CONFIRM from books** — this claim is only in USER-RES and presumably in the газета МАИ 1991 piece (USER-RES §9). B-SMALL batches do not list a 1991 газета МАИ analysis. |
| 10 | 26 August 2001 first human trial | PV-01 v2-p3 footnote verbatim; articles_and_patent dated 19:30–20:00 МСК | 26 Aug 2001, 19:30–20:00 МСК | 527877 off 1 hit | **ALIGN** (first temporonaut named "Ivan Konov" only in NET 2001 English + MG-05; PV-01 book does NOT name him — verified absent by grep "Конов" in 527877 = 0) |
| 11 | Ловондатр-7 = "seventh model" | B-PV01 §1.3 infers "7 generations by Aug 2001"; F-12R treats as confirmed | USER-RES §5 "Ловондатр-7" row | PV-01 text says "за 5 лет … 4 установки, строятся две следующие, и только что (август 2001) двухметровая" → reconstructable as 4+2+1=7. The number "7" as model index is NOT spelled out in the books themselves. | **EXTEND** (merged files correctly infer from the 4+2+1 arithmetic; USER-RES §5 names "Ловондатр-7" — that exact label is the NET-2001 / kosmopoisk forum usage, not Chernobrov's book terminology). |
| 12 | Outer diameter 2.1 m (human-scale) | 2 m ("двухметровая установка") in PV-01; 2.1 m in NET-03 | 2.1 m | 527877 + faraday_12rus | **ALIGN** with rounding caveat |
| 13 | Inner 1 m sphere (human-payload) | F-12R §1 | 1 m | faraday_12rus | **ALIGN** |
| 14 | 31 mice / 25 died (NET 2001) | articles_and_patent §1 | 31 mice / 25 died | net_03_2001 | **ALIGN** |
| 15 | Dog Luna-khod 108 min | articles_and_patent §1 | 108 min | net_03_2001 + B-SMALL | **ALIGN** |
| 16 | Cat Pломбир refuses field | articles_and_patent §1 | same | net_03_2001 | **ALIGN** |
| 17 | 9 human subjects total | articles_and_patent §1 | 9 | net_03_2001 | **ALIGN** |
| 18 | −3% human max Time slow | articles_and_patent §1 | −3% | net_03_2001 | **ALIGN** |
| 19 | Patent RU 2003110067 discontinued | articles_and_patent §4.3: 2005-04-21 FA92 withdrawal | USER-RES §10: "Заявка прекращена" | faraday_12rus + Google Patents | **ALIGN and EXTENDED** (exact FA92 date added) |
| 20 | Frequency formula f = c/d, d = 7 mm → 43 GHz | F-12R §2 | same | faraday_12rus | **ALIGN** |
| 21 | "50 landing sites as Ловондатр design basis" | B-MPN §0 header states this as its cross-ref target, but the BOOK itself documents **17 sites** at Medveditskaya | **NOT in USER-RES** | 536019 + 81959: both say 17 | **CONFLICT** — the "50 sites" phrase appears nowhere in either the books or USER-RES. Merged B-MPN header should not attribute this to USER-RES §1. |
| 22 | Academic V.P. Mishin consulted on Ловондатр | B-SVL q18 finds Мишин in context of Nazi-UFO-docs, NOT Ловондатр | **NOT in USER-RES §1** (appears only in `01_early_kosmopoisk`, which is a separate secondary research doc, not USER-RES) | 536011 = 2 mentions, neither linked to Ловондатр | **SOURCE-MISSING** — this claim has no direct book support. |
| 23 | Quasi-monopole cocoon theory | B-PV01 §2.2, B-TV99 §1.8, F-12R §6 | USER-RES §6 and §10 | 527877 + faraday_12rus | **ALIGN** |
| 24 | Bartini 6D world | B-PV01 §5.3, F-12R §10 | USER-RES §1, §5 | 527877 + net_03_2001 | **ALIGN** |
| 25 | MAI + Khrunichev + Salyut + Energia build partners | B-PV01 §0.3 (Хруничев 1 hit) | USER-RES §1 | 527877 | **ALIGN** (Khrunichev only, other partners not explicitly in PV-01 prose; this should be tightened in MASTER) |
| 26 | Kosmopoisk 1982–2005: 465 expeditions / 4030 participants / 170 groups | B-SS §6 | not in USER-RES | 81959 | **EXTEND** |
| 27 | 14 installations + 6 modifications (MG-DOC-17 transcript) | Batch-1 already carried this; B-MG05 §refers to transcript | USER-RES §11 "минимум 7 Ловондатр" | Transcript, not book | **EXTEND (carried from Batch 1)** |

**Conflicts flagged for Batch 3 resolution:**
1. Row 6 — **1.5 s vs 2 s lethality threshold**: books uniformly say 1.5 s; USER-RES says 2 s. MASTER must use 1.5 s and footnote USER-RES discrepancy.
2. Row 7 — **30 s/h outlier vs 40 s/h USER-RES peak**: books say 30 s/h (single outlier) and ±1.5/+0.5 s/h stable; USER-RES headline "40 s/h" is not substantiated by the monographs. 40 may come from NET-03 or conference abstracts; re-verify.
3. Row 21 — "50 landing sites": not in any book, not in USER-RES. Retract unless a specific source citation can be produced.
4. Row 22 — "Мишин Ловондатр consultant": present only in secondary research doc, not in USER-RES and not in any book.
5. Row 9 — "30 April 1991 open-schema / 10 g thrust on 400 g model" — cannot verify from books; depends entirely on 1991 газета МАИ physical archive.

---

### §4 Completeness — File Inventory

**Source population:**
- FB2 texts: **32 files** (13 major books + 19 shorter works / variant reprints, incl. 1 duplicate: `11101` alt + `536017` same work)
- FB2 chunks v2: 9 files (PV-01 × 3, SS × 2, EZM, MPN, TPM, SVL × 1 each)
- Extracted raw: 10 files (crop_circles PDF, Faraday PDFs, 4 NET issues, 2 VBCH, ufologii, faraday_timemachine)

**Analysis output population:**
- `analysis/books/B-*.md`: **14 merged files** (as enumerated in task spec)
- `analysis/books/chunks/*.md`: **21 chunk extracts** (predecessors to merged files)
- `analysis/articles/*.md`: **2 files** (F-12R, articles_and_patent)

**Expected per "43 agents originally planned":** unclear what the 43 baseline was; likely = (21 chunk agents) + (14 merge agents) + (2 article agents) + (5 or 6 verification / cross-ref agents). If so, 37 visible outputs match. **No missing B-*.md file** relative to the 13 expected major-book targets.

**Coverage gaps worth noting for MASTER:**
1. No dedicated analysis of газета МАИ 1991 (USER-RES §9) — PDF not in `extracted_text/`. This is the origin of the 30.04.1991 10-g-thrust claim and should be fetched.
2. No dedicated analysis of `kosmopoisk.org/temporology/index.html` (USER-RES §12, §13, §14, §15 all cite this URL) — only `KP-TEM` brief note inside `articles_and_patent.md §5`. A full scrape would be valuable.
3. No analysis of Academia.edu "Report on Time Machine Experiments" (USER-RES §17) — only mentioned.

**File-count verdict:** **PASS** for the books/articles scope actually funded in Batch 2.

---

### §5 Merge Integrity (Chunk → Merged)

Sampled 6 merged files and traced their chunk predecessors:

| Merged file | Chunks referenced in header | Verification |
|---|---|---|
| B-PV01 | PV-01_part1, PV-01_part2, PV-01_v2_part2, PV-01_v2_part3 (part3, part4 flagged as empty/base64) | Header §0.1 character-window table matches; key Ловондатр content correctly localised to v1-p1 chars ~163 k–205 k; 26 Aug 2001 footnote correctly attributed to v2-p3 |
| B-TV99_TPV01 | TV-99_part1, TV-99_part2, TPV-01_part1, TPV-01_part2 | Claim tags `[TV99-p1]`, `[TV99-p2]`, `[TPV01-p1]`, `[TPV01-p2]` used consistently; CORE vs NEW-2001 markers applied |
| B-SS | SS_part1, SS_part2 | Chunk→merge map spelled out in header; Part 1 = doctrine, Part 2 = casework — confirmed by content |
| B-MG05 | MG-05_part1, MG-05_part2, MG-05_part3 | 3-chunk merge → 394-line output; key quotes (17 sites, Медведицкая, И. Конов) preserved |
| B-EAYAV | EAYAV_part1, EAYAV_part2 | Both chunks present as predecessors; encyclopaedic A–Z structure preserved |
| B-PMF | PMF_part1, PMF_part2 | 2→1 merge; 249 lines is shortest of the merged set but coverage proportional to Podmoskove FB2 size (634914 is 250 KB, half of TV-99) |

All merged files cite their predecessor chunks by filename in the `## Source chunks consolidated` header. **No orphan claims** were found that lacked a chunk-level predecessor.

**Merge-integrity verdict: PASS.**

---

### §6 Critical Conflict Audit (5 Flagged Items)

1. **"2 sec lethality" (USER-RES §1) vs "1.5 sec" (books)** — **CONFIRMED CONFLICT**. Greps: "разницы в 1,5 секунды … не пережил почти никто" = 2 hits across 81958_Tayny_Vremeni and 634626_Tayny_i_paradoksy. "разницы в 2 секунды" or "2 секунды … не пережил" = 0 hits in any FB2. **Resolution: Books are correct; USER-RES sentence 5 of §1 carries a transcription error. MASTER should cite 1.5 s.**

2. **"40 sec/hr" (USER-RES §1) vs "1.5 s/hr slowdown + 0.5 s/hr speedup" (SS) vs "30 sec/hr peak" (TV-99)** — **PARTIAL CONFLICT**. Book text says: "замедление составило 4 минуты за 8 часов (30 секунд/час)" (single outlier); then stable band "−1,5 сек/час и ускорение до +0,5 сек/час". USER-RES's 40 s/h is not in any book. It may originate from NET-03 2003 article (check `net_06_2002.txt` / `net_09_2003.txt`); the extracted_text grep for "40 сек" in NET files is also 0. **Resolution: MASTER should report "30 s/h single outlier; ±1.5/+0.5 s/h stable band" as the book-supported range, and flag the 40 s/h claim as unsourced unless NET-03 originals can be re-checked.**

3. **"50 landing sites as design basis" (claimed by Batch-2 to be in USER-RES §1)** — **NOT IN ANY BOOK, NOT IN USER-RES**. Grep across all FB2: "50 мест" = 0, "полсотни мест" = 0, "пятидесяти мест" = 0. USER-RES itself: no mention. The B-MPN merged file attributes this to USER-RES §1 in its `## §0 Cross-ref primary` field (line 7) — this attribution is erroneous. The BOOK catalogues **17 sites** at Medveditskaya zone. **Resolution: Correct the B-MPN header to cite "USER-RES §1 *claim to be verified*"; in MASTER, use 17 sites (Medveditskaya) + Chernobrov's own wider catalog of ~490 observations, NOT 50.**

4. **"Академик Мишин attributed to Ловондатр consulting" (per USER-RES §1 via early-publications doc)** — **NOT IN USER-RES, NOT IN BOOKS**. USER-RES grep for "Мишин" = 0 hits in `03_user_provided_research_2026-04-18.md`. Source of Мишин/Ловондатр link is `01_early_kosmopoisk_chernobrov_KEY_FINDINGS.md` line 63, 75, 90 (a different research doc). In the BOOKS: Мишин appears only in B-SVL (SVL FB2) twice, in context of Nazi-UFO documents (он "в ту пору сам принимавший участие в поисках" documentation of Nazi saucers), NOT consulting on Ловондатр. **Resolution: Drop the Мишин/Ловондатр claim from MASTER unless a primary-source citation (газета МАИ 1991? Chernobrov interview?) can be produced. The SVL context is about Third-Reich saucer-docs, a different line of work.**

5. **"Patent RU 2003110067 discontinued 2005 (per Google Patents)"** — **YES, IN ARTICLES ANALYSIS**. `articles_and_patent.md` §4 lines 344–347 and §4.3 line 393: "Application Discontinuation" code FA92, effective 2005-04-21; "Acknowledgement of application withdrawn (lack of supplementary materials submitted)"; publication date 2004-11-27; never granted. This aligns with and extends USER-RES §10 ("Заявка прекращена"). **Resolution: No action needed; MASTER can cite §4.3 of `articles_and_patent.md` directly.**

---

### §7 Recommendations for Batch 3 MASTER Synthesis

1. **Adopt the 1.5 s lethality threshold** (books) and footnote USER-RES §1 discrepancy. Consider whether USER-RES's "2 s" may refer to a *symmetric* 2-s window (±1 s) vs the book's "1.5 s absolute shift" — but barring new evidence, treat books as canonical.
2. **Report the slowdown/speedup band as "30 s/h single outlier, ±1.5 s/h slowdown and +0.5 s/h speedup stable"**. The "40 s/h" USER-RES figure should either be sourced to NET-03 directly with a quote, or dropped.
3. **Retract the "50 landing sites" phrasing everywhere**. The book-supported figures are 17 (Medveditskaya catalog) and 490 (observation catalog). MASTER should not claim the Ловондатр design was derived from analysis of "50 landing sites" unless a primary Chernobrov citation is produced.
4. **Retract the "academic Мишин consulted on Ловондатр" claim** unless a direct Chernobrov citation is produced (газета МАИ 1991 archive is the most plausible origin; this file was not in the Batch-2 input set and should be fetched for Batch 3).
5. **Fix the B-MPN header cross-ref** (`B-MPN_mesta_posadok_NLO.md` line 7) to either cite the correct USER-RES section or drop the cross-ref.
6. **Sample the OCR-integrity of crop_circles_raw.txt** more carefully for MASTER — B-KP is built on PDF-extracted text with known column-flow artefacts, and the 153/154/80 statistics have subtle row/column ambiguity (noted in the merged file itself).
7. **Keep Batch-2's discovery that "Ivan Konov" appears in MG-05 book** (not only in NET 2001) — this is a small but useful cross-attestation that MASTER should preserve.
8. **Flag `academia.edu` "Report on Time Machine Experiments"** (USER-RES §17) as unanalysed — if MASTER intends to claim Chernobrov+Frolov joint 2003 trials used "shielded mechanical+electronic chronometers", that file needs to be fetched.

**Overall verdict for Batch 2: CONDITIONAL PASS.** Extraction fidelity is strong (29/30 quotes match with minor normalisation tolerances; zero hallucinations; full file-coverage of the 32-FB2 source corpus). The conditions are the 5 flagged claims above — resolve them (or explicitly mark them as retracted) before proceeding to MASTER synthesis. Chunk→merge integrity is clean; article analyses are thorough; patent legal-status audit is strong. Batch 2 is ready for MASTER synthesis with the above corrections applied.

---

## Review Gate 5 — Comprehensive Hallucination Audit (2026-04-19)

**Reviewer:** Fresh QA agent (Opus 4.7), no prior context from quote-producing agents
**Scope:** 50 verbatim Russian quotes sampled across all final analysis outputs (1× MASTER, 16× B-* book analyses, 2× article analyses, 4× per-interview analyses)
**Goal:** Test for hallucination, paraphrasing, or wrong attribution at corpus scale
**Verdict:** **PASS** — 50/50 quotes verifiable in primary sources (45 strict MATCH + 5 OCR-EQUIVALENT). Zero hallucinations, zero misattributions, zero unsourced claims.

---

### §1 Methodology

1. **Sampling.** 50 quote sites picked deterministically from blockquoted Russian text (`> «…»`) and inline `«…»` strings ≥ 30 chars in each target analysis file:
   - 8 from `MASTER_chernobrov_claims.md`
   - 2 from each of 16 `B-*` book analyses (32 quotes)
   - 2 from each of 2 article analyses (4 quotes)
   - 1 from each of 4 per-interview analyses (4 quotes)
   - Sampling tier weighted toward §1.x device-architecture, §2 operating-principles, §4 measured-results, §7 lethality, and §11 contradictions sections (the load-bearing claims).
2. **Source mapping.** Each quote's stated source code (`B-TV99` → `81958_Tayny_Vremeni.txt`, `B-EUFO` → `ocr-pipeline/out/ufologii_FULL.md`, `TM-02` → `tm_feb2002_vstretimsya_vchera.html`, etc.) was looked up against the canonical FB2 / OCR / HTML file.
3. **Substring search with normalisation.** A Python harness (`/tmp/verify_quotes.py`) was used to search each quote against its declared source file with the following normalisation passes (in order):
   - quote-character unification (`«»„""`'` → `"`); em/en/minus dash → ASCII `-`; NBSP/thin-space → space; soft hyphen `\xad` stripped; `ё → е`; Latin OCR substitutions `MB → МВ`, `HJI0/HJIO → НЛО`; OCR word-split `(\w)-\s+(\w) → \1\2`.
   - aggressive pass: also strip surviving quote chars and bracketed editor inserts (`[…]` ≤ 30 chars).
   - 60-char prefix and 30-char prefix fall-backs for OCR/PDF artefacts.
4. **Verdict categories.**
   - **MATCH** = full normalised substring present in declared source.
   - **OCR-EQUIVALENT** = quote present in OCR-derived source but with OCR-specific artefacts (e.g. `управляе мый` for `управляемый`, missing dash, line-broken Cyrillic, Latin-Cyrillic homoglyph) that the analysis correctly cleaned. Acceptable for OCR-tier sources (`B-EUFO`, `B-VBCH10`, `B-HRON03`).
   - **PARAPHRASE** = factual content present, but wording compressed or rearranged.
   - **HALLUCINATION** = no substring or factual equivalent found in any candidate source.
   - **SOURCE-MISSING** = source file itself not present in archive.
5. **Pass criterion.** ≥ 45 / 50 in MATCH ∪ OCR-EQUIVALENT = PASS.

---

### §2 Per-file results

| Analysis file | Sampled | MATCH | OCR-EQUIV | Paraphrase | Hallucination | Source-missing |
|---|---|---|---|---|---|---|
| `MASTER_chernobrov_claims.md` | 8 | 7 | 1 (M8 — Grail/Космопоиск, OCR + editor `[Грааля]` insert) | 0 | 0 | 0 |
| `B-PV01_puteshestviya_vo_vremeni.md` | 2 | 2 | 0 | 0 | 0 | 0 |
| `B-TV99_TPV01_core_time_books.md` | 2 | 2 | 0 | 0 | 0 | 0 |
| `B-MG05_medveditskaya_gryada.md` | 2 | 2 | 0 | 0 | 0 | 0 |
| `B-PMF_podmoskove.md` | 2 | 2 | 0 | 0 | 0 | 0 |
| `B-EAYAV_enciklopediya_anomalnykh.md` | 2 | 2 | 0 | 0 | 0 | 0 |
| `B-SS_spravochnik_stalkera.md` | 2 | 2 | 0 | 0 | 0 | 0 |
| `B-MPN_mesta_posadok_NLO.md` | 2 | 2 | 0 | 0 | 0 | 0 |
| `B-EZM_zagadochnye_mesta_zemli.md` | 2 | 2 | 0 | 0 | 0 | 0 |
| `B-TPM_parallelnye_miry.md` | 2 | 2 | 0 | 0 | 0 | 0 |
| `B-SVL_sushchestvuyut_vopreki_logike.md` | 2 | 2 | 0 | 0 | 0 | 0 |
| `B-TMV_tungusskiy_meteorit_vremya.md` | 2 | 2 | 0 | 0 | 0 | 0 |
| `B-KP_krugi_na_polyakh.md` | 2 | 2 | 0 | 0 | 0 | 0 |
| `B-HRON03_hroniki_vizitov_NLO.md` | 2 | 2 | 0 | 0 | 0 | 0 |
| `B-EUFO_enciklopediya_ufologii.md` (OCR) | 2 | 0 | 2 | 0 | 0 | 0 |
| `B-VBCH10_vremya_bessmertie_chelovek.md` (OCR) | 2 | 0 | 2 | 0 | 0 | 0 |
| `articles/articles_and_patent.md` | 2 | 2 | 0 | 0 | 0 | 0 |
| `articles/F-12R_faraday_patent_paper.md` | 2 | 2 | 0 | 0 | 0 | 0 |
| `per-interview/01_02_mashina_vremeni_lectures.md` | 1 | 1 | 0 | 0 | 0 | 0 |
| `per-interview/06_sledy_puteshestvennikov.md` | 1 | 1 | 0 | 0 | 0 | 0 |
| `per-interview/07_13_heavy_mv.md` | 1 | 1 | 0 | 0 | 0 | 0 |
| `per-interview/16_krugi_na_polyakh.md` | 1 | 1 | 0 | 0 | 0 | 0 |
| **TOTAL** | **50** | **45** | **5** | **0** | **0** | **0** |

---

### §3 Issues detail (all 5 non-strict-MATCH cases — every one resolved as OCR-EQUIVALENT)

| # | Quote head | Claimed source | Actual finding | Verdict |
|---|---|---|---|---|
| 1 | «поисками чаши [Грааля] сейчас занимается «Космопоиск», и нельзя пока говорить, на какой след мы напали» | `B-VBCH10` p. 207 | Source has «поисками чаши сейчас занимается «Кос-\nмопоиск», и нельзя пока говорить, на какой след мы напали — по разным причинам…». Editor's bracket `[Грааля]` is an explanatory insert legitimised by surrounding chapter context (Grail discussion). Rest matches verbatim once OCR line-breaks (`Кос-\nмопоиск`) are normalised. | **OCR-EQUIVALENT + editor insert** |
| 2 | «МВ (машина времени) — управляемый транспортный аппарат для перемещения в физическом Времени. (Термин введён Г. Уэллсом в 1885 году, аббревиатура введена В. Чернобровым в 1985 году…)» | `B-EUFO` (Энциклопедия уфологии, 2007) | Source OCR has `MB (машина времени) управляе мый транспортный аппарат для перемещения в физическом Времени. (Термин введен Г. Уэллсом в 1885 году, аббревиатура введена B. Чернобровым в 1985 году…)`. Cleaning required: Latin `MB` → Cyrillic `МВ`, restore missing em-dash, rejoin `управляе мый`, Latin `B.` → Cyrillic `В.`. Verbatim once OCR artefacts are normalised. | **OCR-EQUIVALENT** |
| 3 | «НЛО могут менять направление своего движения под прямым углом практически мгновенно, причём, согласно существующим у нас физическим законам, ускорение в момент поворота должно составлять тысячи G» | `B-EUFO` | Source OCR: `…менять направление своего дьижения под прямым углом практически мгновенно, причем, согласно существующим y нас физическим законам, ускорение в момент поворота должно составлять тысячи G…`. Cleaning: `дьижения → движения`, Latin `y` → Cyrillic `у`, ё-restoration. Verbatim once OCR artefacts are normalised. | **OCR-EQUIVALENT** |
| 4 | «В 2003 году я получил письмо от москвича Андрея Яблонского, прочитавшего эту главу в первом издании …» | `B-VBCH10` (2010, OCR) | Match (line breaks only). | **OCR-EQUIVALENT** |
| 5 | «…элементарный расчет показывает, что тех миллисекунд, которые затрачивает пуля на полет и внедрение в человеческое тело, совсем недостаточно для того, чтобы человек успел сосредоточиться и затормозить даже самую крошечную дробинку…» | `B-VBCH10` (2010, OCR) | Match (line breaks only; OCR is clean here). | **OCR-EQUIVALENT** |

**No paraphrases, no misattributions, no hallucinations were detected in the 50-quote sample.** A few near-misses on the first pass (e.g. `MPN-2` "Пульсирующее излучение из-под земли") turned out to be true MATCHES once OCR word-break (`из- лучение`) was handled — these were classified MATCH after re-running with the corrected normaliser and are *not* counted as paraphrases.

---

### §4 Verdict

**PASS** by the criterion ≥ 45/50 in (MATCH ∪ OCR-EQUIVALENT). Achieved **50/50 = 100 %**, with zero hallucinations and zero misattributions across the entire corpus of 22 sampled analysis files.

This Gate 5 audit confirms the cumulative finding of Review Gates 1 (`PASS, 25/25 verbatim`) and 2 (`CONDITIONAL PASS, 29/30 match`) at MASTER-corpus scale: **the analysis pipeline does not fabricate Russian quotations**. All sampled `«…»` strings either reproduce primary-source wording verbatim or are demonstrably correct cleanings of OCR-degraded primary text (with editor inserts marked by `[…]` brackets where used).

The two newest OCR-tier inputs (`B-EUFO` 2007 — 117 KB, and `B-VBCH10` 2010 — 126 KB) carry their predicted higher OCR-equivalent rate (4 of 4 sampled quotes = 100 % OCR-EQUIVALENT, 0 strict MATCH), but **every artefact identified was a genuine OCR-pipeline degradation in the source**, not an analyst-introduced rewrite. The cleaning the analysts did is conservative and verifiable by re-grep against the OCR text with normalisation.

---

### §5 OCR-source verification notes

**`B-EUFO` (Энциклопедия уфологии 2007 — `ocr-pipeline/out/ufologii_FULL.md`):**
- OCR pipeline produces typical artefacts: Latin/Cyrillic homoglyph swaps (`MB ↔ МВ`, `B. ↔ В.`, `y ↔ у`, `c ↔ с`), word-internal spacing (`управляе мый`), letter substitutions (`дьижения` for `движения`), periodic missing punctuation (em-dashes silently dropped between `…)` and following sentence). No analyst-introduced Cyrillic-letter-substitution detected.
- Sample 1 (МВ definition entry, p. early-A): full sentence reconstructable from OCR with 4 cleaning operations, all standard.
- Sample 2 (НЛО maneuvering paragraph): full sentence reconstructable with 3 cleaning operations.
- Recommendation: keep §0.5 of MASTER's source-code table flag noting `B-EUFO` is OCR-derived; consumers of MASTER can grep `ufologii_FULL.md` directly with the same normaliser if they want to re-verify.

**`B-VBCH10` (Время, Бессмертие, Человек 2010 — `ocr-pipeline/out/vbch_FULL.md`):**
- OCR cleaner (line breaks only, very few letter-substitution errors). 2 of 2 sampled quotes match strict-verbatim once line breaks are joined.
- The MASTER quote on Holy Grail / «Космопоиск» (M8) uses a `[Грааля]` editor insert. This is a *legitimate clarification* (the immediately preceding source text discusses the Grail explicitly, then the original sentence begins with the bare noun `чаши`). The convention should be retained — but a footnote in MASTER §11 / §0.0 noting "bracketed inserts in `B-VBCH10` quotes are editorial and not in the source" would improve transparency.
- Recommendation: no retractions; one editorial-convention footnote suggested.

**`B-HRON03` (Хроники визитов НЛО 2003 — `hroniki_vizitov_nlo_ocr.txt`, also OCR-derived):**
- 2 of 2 sampled quotes strict MATCH on first pass — this OCR is high-quality and the analysis did not need cleaning beyond standard whitespace.

**`B-KP` (Круги на полях — `extracted_text/crop_circles_raw.txt`, PDF-extracted):**
- 2 of 2 strict MATCH after standard hyphen-rejoin (`из- лучение → излучение`). Analyst correctly closed PDF-column word breaks.
- Cross-reference: Review Gate 2 §6 item 6 already flagged the column-flow risk; this Gate 5 sample of 2 quotes shows that risk did not realise into wrong claims.

**Overall OCR audit conclusion:** OCR-tier sources behave as predicted. Cleaning operations done by the analysis are all of the standard reconstructive type (rejoin hyphenated word breaks, restore Cyrillic ↔ Latin homoglyphs, restore dropped punctuation, restore ё where it was lost). No instance of analyst-introduced new wording, deletion of qualifications, or misquotation was detected.

---

## Review Gate 6 — Coverage Summary (2026-04-19, folded from former `COVERAGE_AUDIT.md`)

**Scope:** inventory of every source file under `chernobrov-archive/` cross-referenced against every analysis output.

**Headline numbers:**
- **Source population:** 151 files across 11 categories — 19 audio transcripts, 32 FB2 plaintext books, 26 FB2 chunk extracts, 10 PDF originals, 10 PDF-extracted texts, 10 OCR-pipeline outputs, 26 substantive HTML pages, 9 HTML indexes, 1 Cloudflare-blocked page, 5 Perplexity research files, 3 catalog files.
- **Analysis output population:** 75 files — 1 MASTER, 3 reviews (this file + FINAL_REVIEW + 01_02_comparison), 8 per-interview, 8 topical, 17 B-*, 29 chunks, 2 articles, 2 cases, 5 Perplexity (also counted as source).
- **Transcript coverage:** 19/19 (100 %).
- **FB2 book coverage:** 32/32 (100 %) — 13 via dedicated `B-*` files, 19 via `B-SMALL_batch1/2`.
- **PDF coverage:** 6/6 substantive PDFs (100 %) via `B-EUFO`, `B-VBCH10`, `B-KP`, `B-HRON03`, `F-12R`, Faraday-TM.
- **HTML coverage:** all substantive Chernobrov-topic pages covered; redundant mirrors (Avidreaders, NaturalWorld, Klex, CoolLib, Fantlab) intentionally unreferenced.
- **Perplexity:** 5/5 files referenced via USER-RES + KEY-FINDINGS codes.

**Substantive gaps addressed in v0.5.1:**
1. **NET compendium (`B-NET-FULL`):** four NET issues (#3 2001, #6 2002, #9 2003, #12 2003) consolidated into `analysis/articles/NET_full_compendium.md` (~158 KB), integrating 5 new source codes and 4 new §0.0 numerical parameters (rows 79–82).
2. **RUFORS-19 (Subbotin/RUFORS 2019 interview):** identified as a video-transcript pointer only; chapter list recorded (Хара-Хора, якутские котлы, Аркаим, русские мумии в китайских пирамидах). No dedicated analysis produced — content is late-period field/hronomirage material without engineering claims.
3. **SCRIBD-487087395 (`scribd_487087395.html`):** AI-preview only. English paraphrase of TM-02 / Lovondatr-7 protocol; folded into `articles_and_patent.md` as 4th secondary source alongside REX. No standalone analysis needed.
4. **Structural gaps accepted:** газета МАИ 1991 physical archive and academia.edu «Report on TM Experiments» 2002–2003 remain as acknowledged primary-source acquisition tasks (MASTER §12.6 #1–#2); Hayakawa blog confirmed as off-topic noise; NE #3 2003 conference context (17 other papers) out of Chernobrov scope.

**Verdict:** source-to-analysis coverage is complete for all Chernobrov-authored material; remaining gaps are primary-source acquisition tasks, not analysis gaps.

---

## Review Gate 7 — Cross-Document Consistency Summary (2026-04-19, folded from former `CONSISTENCY_AUDIT.md`)

**Scope:** MASTER (1319 lines, 13 sections, 78 numerical params at v0.5.0 → 82 at v0.5.1) cross-checked against 17 books, 2 articles, 8 per-interview files.

**Methodology:** ripgrep-based string verification of MASTER claims against named source documents; quote-level cross-checks where MASTER cites a verbatim Russian passage.

**Headline result:** **0 substantive contradictions** across 30 sampled numerical parameters, 20 sampled timeline dates, 7 person attributions, 6 site dimensions, and the 4 generation-count reconciliations (4 / 7 / 10 / 14+6).

**3 minor MASTER fixes applied (v0.5.1):**
1. **§0.0 item 1 — Gen-1 outer ЭРП Ø sourcing:** 0,9 m figure was mis-attributed to `B-TV99` offset 705049 (that offset says «около 1 м»). Re-sourced to `F-12R` (2003) + `NE-03-PG` + `NET-12-2003`. Status badge changed ✅ → ⚠ DRIFTED; drift (1 m 1999 → 0,9 m 2003) documented in new §11.12.
2. **§0.0 item 13 — "до 40 s/hr" corroboration:** added `B-SVL` row 118 as undercited supporting source; claim now rests on monograph + anthology + paraphrase trio rather than anthology + paraphrase duo.
3. **§0.0 item 33 + §1.6 (I-7 spacecraft):** re-labelled "designed 1992, first published 2001" after `B-PV01` figure caption «Ирма-7», 1992 год» confirmed a 9-year design-to-publication gap. Documented in new §11.13.

**USER-RES handling (5/5 PASS):** all five Review-Gate-2 honesty items (1.5 s lethality vs USER-RES 2 s; 30 s/h vs 40 s/h; "50 sites" phantom; Mishin-as-consultant; patent RU 2003110067 status) are explicitly handled with reconciliation rationale in MASTER §0.0 + §11 + §12 cross-references.

**Date drift:** 0 contradictions across 20 sampled timeline events.
**Person attribution:** 0 misattributions. The Frolov disambiguation (Valery vs Alexander Vladimirovich) is correctly handled in three places (B-TV99, B-PV01, MASTER §10.4).
**Site dimensions:** 1 minor display issue (item 54 "80 × 50" reading ambiguously vs B-MG05 canonical "50 × 80 × 80") — acceptable as already flagged by MASTER.

**Verdict:** consistency audit **PASS** — no constituent file contradicts MASTER; all known drift is openly flagged in §11.

---

## Review Gate 8 — USER-RES Alignment Summary (2026-04-19, folded from former `USERRES_ALIGNMENT.md`)

**Scope:** USER-RES-2026-04-18 (`03_user_provided_research_2026-04-18.md`, 336 lines, 18 numbered sections + summary table + 4 caveats = 23 reviewable units) cross-checked against MASTER + books + articles.

**Headline counts:**
- **~50 ALIGNED** — USER-RES claim present verbatim or substantively in MASTER with same number/value.
- **~70 EXTENDED** — MASTER carries USER-RES claim AND adds material from primary books (most `§0.0` rows #37–#78 are predominantly EXTENSIONS).
- **7 CONTRADICTED** — all reconciled in MASTER §11:
  1. 1,5 s lethality vs USER-RES «2 s» (§11.4 + §7.2 + §0.0 #20)
  2. 30 s/hr outlier + ±1,5 s/hr routine vs USER-RES «40 s/hr» headline (§11.1 + §0.0 #13 vs #14)
  3. «50 landing sites» phantom — RETRACTED (§11.2 + §8.1 + §0.0 #43)
  4. Academician Mishin as Lovondatr consultant — UNATTESTED (§11.6 + §10.3 + §12.3)
  5. «Астра» as laboratory vs primary-source СККБ (design bureau) (§11.9 + §10.5)
  6. Series claim («Время и Земля» / «Космос» / «Темпоронавтика») not verified in `B-VBCH10` (§11.11)
  7. USER-RES §5 «9 человек» / «5 из 6 мужчин» vs TM-02 verbatim 1+7=8 / «4 из 5 мужчин» (§0.0 #29 + §4.4)
- **2 MISSING** (both pre-flagged in MASTER §12.6 as open primary-source acquisition tasks, not analysis gaps):
  1. Газета МАИ 1991 physical archive (USER-RES §9)
  2. academia.edu «Report on Time Machine Experiments» 2002–2003 (USER-RES §17)

**Verdict:** every USER-RES section §1–§18 plus the summary table and 4 caveats is addressed in the archive analyses; the 4 critical paraphrase issues identified by prior reviews all have explicit MASTER §11 reconciliation entries; EXTENSIONS substantially outrun USER-RES. Audit closes **PASS**. No load-bearing corrections required.

**Top 5 EXTENDED facts** (where the archive significantly outruns USER-RES):
1. 2002 MG field tests — 12-min / 114-min / 1-min UFO-response latencies (MASTER §1.5 + §8.3 + §0.0 #40-#42).
2. `B-VBCH10` (2010) «body-as-spontaneous-Lovondatr» unification thesis (MASTER §5.7 + §0.0 #61-#74).
3. Patent discontinuation date 2005-04-21 with FA92 code + 9-claim breakdown (MASTER §11.5 + §0.0 #30-#32).
4. `B-EUFO` Anfalov–Dulce–Element-115 single cross-reference — only direct Lazar cross-ref in any Chernobrov primary source (MASTER §0.0 #75 + §9.5).
5. Tunguska Zolotov 1960s chrono-deceleration RE-CONFIRMED by Космопоиск 1996 (MASTER §0.0 #65 + §6.2).
