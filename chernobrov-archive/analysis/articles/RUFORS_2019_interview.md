# RUFORS-19 — Source Analysis

**Source code:** RUFORS-19
**File analyzed:** `books/downloads/rufors_interview_2019_ok.html`
**File size:** 911 240 bytes (911 KB)
**Format:** Single-page HTML capture from `ok.ru` (Odnoklassniki video hosting)
**Analysis date:** 2026-04-19
**Analyst note:** Source had not been previously processed.

---

## 1. Executive Finding (read this first)

**This source contains NO interview text.**

The 911 KB HTML file is a saved web page from `https://ok.ru/video/940853498245`. It is the
*video viewer page* for an OK.RU upload — i.e., browser chrome, navigation,
recommendation rail, comment widgets, cookie banners, and meta tags around an embedded
video player. After stripping HTML/JS/CSS the entire human-readable text is **15 696
characters**, of which roughly 1.2 KB is the video metadata block (title + chapter
timestamps + donation links) and the remaining ~14 KB is unrelated OK.RU recommended
videos and site UI.

The interview itself is a **2 h 21 min 12 s video** (`og:video:duration = 8472`
seconds). It is *not* embedded as audio or transcript in the HTML. To extract any
substantive content one would have to **download the video file from ok.ru and
transcribe it** (analogous to the existing `/audio/` and `/transcripts/` workflow).

Therefore the rest of this document records what *is* present in the HTML (metadata,
provenance, chapter map, side-channel evidence) and explicitly flags every research
question from the task brief as **NOT ANSWERABLE FROM THIS FILE**.

---

## 2. Provenance and Identification

### 2.1 What the file actually is

| Field | Value |
| --- | --- |
| Hosting platform | OK.RU (Odnoklassniki, mail.ru-group video) |
| Canonical URL | `https://ok.ru/video/940853498245` |
| Video numeric ID | `940853498245` |
| Embed URL | `https://ok.ru/videoembed/940853498245` |
| Content ID | `477913287296` |
| Status | `published`, `is_official=no`, `allow_embed=false` |
| Video upload date | **2019-02-06 20:46:48 +03:00** (Moscow time) |
| Video modify date | 2019-02-06 20:46:48 +03:00 (identical → never edited) |
| Duration | 8 472 s = **2 h 21 min 12 s** |
| Aspect / size | 491 × 275 |
| Views (at capture) | 403 |
| Likes / comments | 0 / 0 |
| Re-shares | 15 |
| Adult flag | false |

### 2.2 Title (verbatim, Russian)

> **«Вадим Чернобров / История без истории / Интервью без купюр / Николай Субботин / RUFORS»**

Literal translation:
*"Vadim Chernobrov / History Without History / Uncut Interview / Nikolai Subbotin /
RUFORS"*

### 2.3 Uploading channel

The HTML's "page header" attributes the upload to a channel called
**«Древо Мидгард-Земли»** ("Tree of Midgard-Earth"), 7 K subscribers at capture time.
This is *not* RUFORS itself and *not* Subbotin's primary channel — it is a third-party
re-upload with an esoteric / Slavic-paganism flavour (the same channel/page also
links to an **«Ассоциация "#Протоистория"»** group with branded VK/Facebook/OK
mirrors).

This matters: it means the 2019-02-06 timestamp is the **mirror upload date**, not the
recording date.

### 2.4 Recording date — inferred, not stated

The description states the interview was filmed by Subbotin **for his film
*"Неизвестный Аркаим"* ("Unknown Arkaim")** and for "a cycle of historical features".

- Subbotin's *Unknown Arkaim* footage was shot in the early-to-mid 2010s.
- Chernobrov died **21 May 2017**.
- The interview is described as «без купюр» / «без монтажа» ("uncut / unedited").

So the recording itself is **pre-May 2017** (likely 2014-2016 given the *Unknown
Arkaim* production window) and the 2019-02-06 OK.RU upload is **posthumous re-
publication**, not a posthumous interview as the brief tentatively framed it. The
person speaking in the video is Chernobrov himself, alive, in conversation with
Subbotin — *not* a 2019 retrospective by collaborators.

### 2.5 Interviewer

**Nikolai Subbotin** — head of the **RUFORS** project (Russian UFO Research Station,
rufors.ru). A long-time documentary maker / interviewer in the Russian
ufology/protohistory milieu, frequent on-screen partner of Chernobrov in
Kosmopoisk-adjacent productions.

### 2.6 Interviewee

**Vadim Aleksandrovich Chernobrov** himself — sole interviewee.

(There is **no** "collaborator round-table about the late Chernobrov" content in this
source, contrary to the working hypothesis in the task brief.)

---

## 3. Chapter Map (the only substantive content present)

The OK.RU description carries the video's table of contents as timestamp markers.
This is the entire substantive portion of the file:

| Timestamp | Russian topic | English gloss |
| --- | --- | --- |
| 00:00 – 01:42 | (intro) | intro / handshake |
| **01:42** | динозавры в наши дни, экспедиция на озеро Лабынкар | Dinosaurs in the present day; Lake Labynkyr expedition |
| **45:30** | мифология и сказки о драконах и динозаврах в недавнем прошлом | Myth & folklore of dragons / dinosaurs in the recent past |
| **51:07** | хрономиражи | Chrono-mirages (time-mirages) |
| **1:04:19** | комплекс Хара-Хора | Khara-Khora complex |
| **1:30:01** | пирамиды и подземные города Кавказа | Caucasus pyramids and underground cities |
| **1:45:14** | якутские котлы, Елюю-Черкечех | Yakut "cauldrons", Elyuyu-Cherkechekh |
| **1:56:16** | Аркаим, Гардарика, страна городов | Arkaim, Gardarika, "Land of Cities" |
| **2:04:22** | русские мумии в китайских пирамидах | "Russian" mummies in Chinese pyramids |
| (to 2:21:12) | (closing) | wrap |

**Topical reading.** This is a *historical-anomalies / proto-history* interview, not a
time-machine / Lovondatr / Kosmopoisk-org interview. The single segment that touches
the Kosmopoisk-physics agenda at all is the **51:07 "хрономиражи"** chapter — but
chrono-mirages are a long-standing Chernobrov topic predating Lovondatr (he treats
them as eyewitness reports of past/future visual bleed-through, not as device
output). There is no chapter on time machines, Lovondatr, Faraday Lab, Frolov,
patents, or Medveditskaya Gryada.

### 3.1 Implication for the corpus

The interview's content domain is largely orthogonal to the
machine-and-patent thread that the chernobrov-archive is auditing. Even if the video
were transcribed in full, the expected yield of new claims about
Lovondatr / RU 2003110067 / Faraday Lab / Medveditskaya is **low**, with the only
plausible payoff sitting inside the ~13-minute "хрономиражи" block (51:07-1:04:19).
Lake Labynkyr (45 min of dinosaur cryptozoology) is unrelated to the engineering
audit.

---

## 4. Brief Item-by-Item Response

The task brief asks for nine extraction targets. Marking each against what the HTML
actually contains:

| # | Brief item | Status | Note |
| --- | --- | --- | --- |
| 1 | Identity of interviewee(s) | **Partial** | Chernobrov (alive); interviewer Subbotin. From metadata only. |
| 2 | Date and venue | **Partial** | Upload 2019-02-06; recording pre-May 2017; venue not stated. |
| 3 | Reflections on Chernobrov (bio / methodology / character) | **NOT IN FILE** | Requires video transcription. |
| 4 | Posthumous claims about Lovondatr / time-machine / Kosmopoisk programs | **NOT IN FILE** | Also: this is *not* a posthumous interview — Chernobrov is the speaker. |
| 5a | Lovondatr device(s) post-2017 status | **NOT IN FILE** | Recording pre-dates his death; cannot speak to post-2017 status by definition. |
| 5b | Kosmopoisk org continuation | **NOT IN FILE** | Same. |
| 5c | Patent RU 2003110067 later opinions | **NOT IN FILE** | Not in chapter map. |
| 5d | Medveditskaya site situation | **NOT IN FILE** | Not in chapter map. |
| 6 | New / revised claims | **NOT IN FILE** | Requires transcription; *low* expected yield based on topical scope. |
| 7 | Frolov / Faraday Lab mentions | **NOT IN FILE** | Not in chapter map. Highly unlikely given subject matter. |
| 8 | Contradictions with Chernobrov's published claims | **NOT IN FILE** | Cannot assess without transcription. |
| 9 | Photos / diagrams referenced | **NONE** | The HTML has one OG-image (the OK.RU video thumbnail) and no in-text figures, captions, or galleries. |

---

## 5. Side-Channel Evidence Worth Recording

A few items in the HTML are useful as corpus metadata even though they aren't
"interview content":

### 5.1 Subbotin / RUFORS payment & contact endpoints (2019)

The description block includes Subbotin's then-active donation rails. Recording for
provenance / cross-referencing other RUFORS materials of the same vintage:

- VISA: `4693 9575 5039 1432`
- QIWI: `+7 926 048 22 70`
- WebMoney: `R168439290866`, `Z164600031569`, `E152065403192`
- Yandex.Money wallet: `410012842224350`
- PayPal: `info@rufors.ru` / `paypal.me/rufors`

Email `info@rufors.ru` aligns with the rufors.ru domain and is a useful
authentication marker if other 2018-2019 Subbotin attributions need to be checked.

### 5.2 Affiliated social-media properties

Branded under "Ассоциация #Протоистория" by the re-uploading channel:

- vk.com/protohistory
- facebook.com/protohist/
- facebook.com/groups/protohistory/
- ok.ru/protohistory

These are the *re-uploader's* accounts, not RUFORS proper. They imply this video
escaped RUFORS's primary distribution into the Slavic-protohistory ecosystem, which
explains the very low view count (403) compared to comparable RUFORS uploads on
YouTube.

### 5.3 Cross-recommendation hint

The OK.RU recommendation rail in the HTML lists, among ~60 unrelated videos, exactly
one relevant Chernobrov item:

- **«Вадим Чернобров. Машина Времени»** — channel "Игорь Медведев" — 2 h 37 m, 128
  views.

This duration matches **transcript `01_Chernobrov_MashinaVremeni_2h37.mp3`** already
present in the archive. So OK.RU's recommender has correctly clustered this upload
with the existing primary "Mashina Vremeni" interview but offers no additional
sources we don't already have.

### 5.4 Visual asset

A single still is referenced — the OK.RU auto-generated video thumbnail:

`https://iv.okcdn.ru/videoPreview?id=1179369932160&type=47&idx=30&tkn=3gFaJkkZUYct4GjBLmX13TfN0Hc&i=1&fn=external_8`

Not an interview diagram; not worth archiving.

---

## 6. Recommendations

1. **Do not integrate this file into MASTER as an "interview source".** The HTML
   carries no interview text, only catalog metadata. Treating it as an analyzed
   article would inflate the corpus's apparent coverage.

2. **Reclassify** in the catalog as a *video pointer* (analogous to a YouTube/OK.RU
   bookmark), not a textual interview. Suggested catalog row:

   - title: «История без истории»
   - speaker: V. Chernobrov
   - interviewer: N. Subbotin (RUFORS)
   - format: video, 2 h 21 min, OK.RU re-upload
   - upload date: 2019-02-06 (recording pre-May 2017)
   - URL: https://ok.ru/video/940853498245
   - relevance to engineering audit: **low** (proto-history / cryptozoology focus)
   - one chapter of partial relevance: 51:07-1:04:19 "хрономиражи"

3. **If the engineering audit wants the chrono-mirage segment**, the cheap action is
   to download the OK.RU stream, trim 51:00-1:05:00, and run the existing Groq
   Whisper pipeline against the ~13-minute clip. Full-video transcription is not
   justified by topical scope.

4. **Do not flag any "new" or "contradictory" Chernobrov claims** based on this
   source. The HTML does not support any such finding either way.

5. **Re-label the source code** if the catalog distinguishes textual vs.
   audio/video sources — consider `RUFORS-19-VID` to make the format explicit
   and prevent a future analyst from re-opening the same dead-end.

---

## 7. Method Notes

- HTML stripped with a Python regex pass: scripts and styles deleted, then
  `<[^>]+>` removed, HTML entities unescaped, whitespace collapsed.
- Stripped output: 15 696 chars (`[rufors-tmp]`, ephemeral).
- Mention frequency in raw HTML: `Чернобров` 28, `Субботин` 18, `RUFORS` 13,
  `Аркаим` 10, `Хара-Хора` 5, `Лабынкар` 5. All occurrences traced back to the
  `<meta name="description">` / `og:description` blocks (i.e. the same description
  text repeated across multiple meta tags) plus the visible page header. None
  appear in body prose because there is no body prose.
- Zero hits for: «Лавондатр», «Ловондатр», «Космопоиск», «Фролов», «патент»,
  «Медведицкая», «машина времени» (substring only inside a recommended-video
  title), «Faraday». Confirms the chapter map is exhaustive of topical content.
