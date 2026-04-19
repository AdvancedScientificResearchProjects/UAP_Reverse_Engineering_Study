# SCRIBD-487 — Scribd document 487087395 ("3-2.pdf")

**Source code:** `SCRIBD-487`
**Source file:** `books/downloads/scribd_487087395.html`
**File size:** 1,023,545 bytes (~1 MB) raw HTML
**Origin URL:** `https://www.scribd.com/document/487087395/3-2-pdf`
**Cataloged:** 2026-04-19

---

## 1. Document Identification

| Field | Value | Source |
|---|---|---|
| Scribd document ID | 487087395 | URL, og:url |
| Scribd display title | "Document Analysis and Data Insights" | `<title>`, h1 `data-e2e="mobile-doc-page-title"` (Scribd-generated) |
| Original filename | `3-2.pdf` | og:title, schema.org `MediaObject.name`, internal `"title":"3-2.pdf"` |
| Schema.org type | `MediaObject` (additionalType: Product) | JSON-LD block |
| Uploader (NOT author) | Leon Blažinović — Scribd user 364320689 | `<a href="/user/364320689/Leon-Bla%C5%BEinovi%C4%87">`, schema.org `author.name` |
| Page count | 3 | `data-e2e="metadata-page-count-wide">3 pages<` (three independent placements: sticky, mobile, metadata) |
| Internal `"page_count"` field | 3 | hypernova hydration JSON |
| Document description | Empty (`"description":""` in internal payload) | Real description is empty; only the AI auto-summary is shown |
| ISBN | null | hypernova payload |
| Document language (declared) | English (`inLanguage: "en"` in JSON-LD) | schema.org `MediaObject.inLanguage` |
| Upload date (derived from image asset timestamp 1607219299) | 2020-12-06 01:48:19 UTC | scribd image URL `/img/document/487087395/.../1607219299` |
| Access flag `"is_archive"` | true | hypernova payload |
| `"isAccessibleForFree"` | true | JSON-LD |
| Stated author | "Leon Blažinović" — same as uploader; this is **NOT the document's author**, it is the Scribd uploader's name re-used as schema.org author | JSON-LD |
| Sharing/embed thumbnail | `https://imgv2-2-f.scribdassets.com/img/document/487087395/original/750455af2c/1?v=1` | meta og:image |

**Filename interpretation.** "3-2.pdf" is consistent with a numbered fragment of a multi-part scan (e.g. issue 3, page 2, or section 3, file 2). No further provenance is encoded in the HTML — the original PDF's metadata is not exposed by Scribd's preview.

---

## 2. Content Accessibility — PREVIEW-ONLY, NO PAGE TEXT

The HTML file is **Scribd's marketing/preview viewer chrome**, not the document body. It contains:

- Site chrome, navigation menus, FAQ blocks, login/signup widgets (~99% of HTML)
- A short AI-generated description (one paragraph, ~85 words) repeated 3× verbatim across mobile/desktop/sticky DOM placements
- A schema.org JSON-LD `MediaObject` record
- A schema.org JSON-LD `FAQPage` block with 9 boilerplate Q&A pairs that have **nothing to do with the document content** (about "technological advancements", "industry competitiveness", "economic policies" — generic templates)

### What is NOT in the file:

- **No `pageserver` / `outer_page_*` / `text_layer` / `absimg` divs** — Scribd's actual rendered page text layers are absent. The 3 document pages exist only as raster images on Scribd's CDN, not embedded in this HTML.
- **No `jsonp_url` page-by-page resource pointers** beyond a single thumbnail image URL.
- **No paywall / login-wall / subscriber-only flags** — the document is marked `isAccessibleForFree: true` and `is_archive: true`, but the HTML simply does not include the page text. Reading the actual 3 pages requires opening Scribd in a browser, where the pages render as images.
- **No paragraph-by-paragraph snippet fields** (`"text"`, `"snippet"`, `"contents"`).

**Conclusion:** the document **content** is accessible to a human Scribd visitor (3 image pages, free), but is **not present in this downloaded HTML**. Only Scribd's AI-generated 85-word abstract is recoverable from this file.

---

## 3. The Only Substantive Text In The File — AI Auto-Summary

Verbatim from `<p class="_1RepZ1">` (and identically in og:description, twitter:description, meta description):

> "Experiments were conducted with mice, cats, and dogs in a time machine (TM) prototype before attempting experiments with humans. Mice and some cats died due to high temperatures in the anomalous field. A stray cat named Plombir was chosen but sensed the field and escaped. A stray dog named Lunokhod was used next and left after 108 minutes showing stress. The first human, Ivan Konov, was in the TM from 7:30-8:00pm on August 26, 2001 for deceleration experiments. Preliminary conclusions found deceleration was smoother than acceleration, which showed instability and dependence on external factors."

**Provenance of this text.** This is a Scribd-side AI summary of the underlying PDF, not a transcription. It is in **English**, while the underlying source material (Чернобров «Эксперименты с Человеком», NET #3 Nov-Dec 2001) is **Russian**. The summary therefore reflects machine paraphrasing and may carry translation drift.

### Named entities extracted from the summary

| Entity | Role | Cross-ref |
|---|---|---|
| **Plombir** (Пломбир) | Stray cat, escaped before experiment | `articles_and_patent.md` line 126–127 (cat «Пломбир» verbatim from TM-02 line 214–215) |
| **Lunokhod** (Луноход) | Stray dog, 108 min in TM, "showing stress" | `articles_and_patent.md` line 129 (dog «Луноход» verbatim from TM-02 line 216) |
| **Ivan Konov** (Иван Конов) | First human subject | `articles_and_patent.md` lines 137-148, 153, 167, 558, 594 |
| **TM (time machine prototype)** | Apparatus | F-12R `articles_and_patent.md` Lovondatr family; F-12R paper §1.3 (Lovondatr-7, Ø 2.1 m / inner 1 m, human-capable) |

### Numerical / temporal facts in the summary

| Value | Item | Cross-ref |
|---|---|---|
| 108 minutes | Lunokhod (dog) session length | New here vs. F-12R paper (which omits animal-protocol numerics); appears in `articles_and_patent.md` line 562 ("Dog Луноход minutes 108") confirming consistency with the canonical TM-02 source |
| 7:30 PM – 8:00 PM (30 min) | Konov human session | Matches `articles_and_patent.md` line 558 ("26 Aug 2001, 19:30–20:00, 3% deceleration") |
| 26 August 2001 | Konov session date | Matches USER-RES §5 / TM-02 protocol |
| (3% deceleration) | NOT in this Scribd summary | Notably **absent** from the AI summary, even though the underlying primary source explicitly states "−3% relative to Earth reference time" (TM-02 line 220). This is the single most-cited numerical result of the entire Konov experiment, and Scribd's auto-summary dropped it. |
| Direction of effect | "deceleration experiments" (slowdown of time inside TM) | Matches Russian source: t/t₀ < 1 |

---

## 4. Boilerplate AI FAQ Block — Marker of Auto-Summary, Not Real Content

Scribd injected 9 `FAQPage` Q&A entries into the JSON-LD. None of them describe the document. The questions are generic templates:

1. "How does the document describe the relationship between technological advancements and industry competitiveness?"
2. "What strategic recommendations does the document make for organizations facing technological disruption?"
3. "How does the document suggest mitigating the risks associated with rapid industrial expansion?"
4. "According to the document, what are the long-term implications of current economic policies on national growth?"
5. "What are the primary factors contributing to the growth of a specific economic sector discussed in the document?"
6. "What synergies are identified between differing industries in the document, and how do they benefit each other?"
7. "In the context of policy implementation mentioned, what are the potential obstacles and how might they be addressed?"
8. "How does market regulation impact consumer and corporate behavior according to the document?"
9. "What role does public perception play in the adoption of innovative solutions as per the document's analysis?"

The "answers" similarly talk about workforce training, regulatory frameworks, and infrastructure — none of which are present in a 3-page Russian time-machine report. **These FAQ blocks are SEO-pollution boilerplate** automatically generated by Scribd's AI without reading the actual document. They should be ignored entirely.

---

## 5. Cross-Comparison With Existing Analyses

### 5.1 vs. F-12R (`F-12R_faraday_patent_paper.md`)

F-12R explicitly notes (lines 21, 415, 475):

> "The file does **NOT** contain the «Experiments with a Man» protocol (NET #3 Nov–Dec 2001). This file is the May–June 2003 issue. No mentions of «Иван Конов», «3 %», «Ловондатр», «31 мышь», or the 9 volunteers appear anywhere in the text. … That material must be sourced from the NET #3 Nov–Dec 2001 issue (a different PDF)."

**SCRIBD-487 is exactly the missing 2001 protocol material that F-12R lacks** — the Scribd 3-page PDF "3-2.pdf" overlaps the very content F-12R was missing: cat Plombir, dog Lunokhod (108 min), human Konov (26 Aug 2001, 30 min), and the qualitative deceleration-vs-acceleration finding (also stated in F-12R §7.4 from a different angle).

The Scribd file's 3-page count is consistent with this being a fragment / excerpt of the larger NET #3 (Nov-Dec 2001) "Эксперименты с Человеком" article — likely pages 2-4 or 1-3 of one section, hence the "3-2.pdf" filename.

### 5.2 vs. `articles_and_patent.md` (TM-02 / NE-03 / REX cross-cuts)

Every named entity and numeric value in the SCRIBD-487 AI summary corresponds to an entity already documented in `articles_and_patent.md`:

| SCRIBD-487 (AI summary, English) | `articles_and_patent.md` (Russian primary source) |
|---|---|
| "stray cat named Plombir" | «добрейший Пломбир» (TM-02 line 214–215, articles_and_patent.md line 127) |
| "stray dog named Lunokhod was used next and left after 108 minutes" | dog «Луноход», 108 min (line 129, line 562) |
| "Ivan Konov, was in the TM from 7:30-8:00pm on August 26, 2001" | «И.Конов … 26 августа», 19:30–20:00 (line 137–168, line 558) |
| "Mice and some cats died due to high temperatures in the anomalous field" | Consistent with TM-02 mouse-mortality preamble (preceding the 31-mouse / 3% sequence) |
| "deceleration was smoother than acceleration, which showed instability and dependence on external factors" | F-12R line 132–157 (`F-12R_faraday_patent_paper.md` §7.4): «замедление происходило значительно более плавно и устойчиво; при ускорении наблюдались резкие скачки … зависимостью от любых (или многих) внешних факторов» — **direct overlap** between the 2001 NET article (SCRIBD-487 source) and the 2003 NET patent paper (F-12R) |

### 5.3 What SCRIBD-487 adds that is NOT yet in the analyses

Three small unique facts from the AI summary that are **not** spelled out in the existing analyses (which focus on Russian primary text):

1. **"high temperatures in the anomalous field" as cause of mouse/cat mortality** — the existing analyses note mouse mortality but do not pin the cause to thermal effects. The English summary's "high temperatures" framing is a distinct claim worth tracing back to the original Russian text once it is OCR-extracted.
2. **Lunokhod stayed exactly 108 min and "left showing stress"** — `articles_and_patent.md` records the 108-minute figure (line 562) but does not include the behavioral observation ("showing stress"). New qualitative datum.
3. **Plombir "sensed the field and escaped"** — the SCRIBD-487 summary collapses the Russian narrative ("каким-то непостижимым образом почувствовал ее слабое поле … изодрав когтями Машу … быстро скрылся в лесу") into a single phrase that ascribes purposeful sensing to the cat. The word "sensed" is the AI's interpretation of «почувствовал».

### 5.4 What SCRIBD-487 omits that IS in the analyses

- **−3% deceleration magnitude** (the headline result of the Konov session) — absent from the AI summary.
- **Symmetrical / dual quartz oscillators** as the measurement chain — absent.
- **Car-battery power source** for the field-located test (REX-C1) — absent.
- **The 7+ subsequent human volunteers** named in TM-02 line 153 (Фокеев, Гавриченко, Курков, Лоренц, Кулешова, Головина) — absent.
- **Lovondatr-7 outer Ø 2.1 m / inner Ø 1 m geometry** — absent.

The AI summary is therefore **lower-fidelity** than the existing primary-source analyses. It should be treated as a pointer to the underlying NET #3 (Nov-Dec 2001) article, not as an independent corroborating source.

---

## 6. Catalog Conclusion

| Item | Verdict |
|---|---|
| Is the file substantive primary-source content? | **No.** It is 1 MB of Scribd preview chrome around an 85-word AI auto-summary. |
| Is the underlying PDF "3-2.pdf" substantive? | **Yes, almost certainly.** It is a 3-page fragment of (most likely) Чернобров's NET #3 Nov-Dec 2001 «Эксперименты с Человеком» — the same article that F-12R analysis flags as missing. |
| Is the actual page text recoverable from this HTML? | **No.** No text layer is embedded; only an image-thumbnail URL. Recovering the page text requires opening Scribd in a browser and OCR-ing the rendered page images, or downloading the original PDF separately. |
| Is the AI summary trustworthy? | **Partially.** Named entities (Plombir, Lunokhod, Konov), the date (26 Aug 2001), the duration (7:30-8:00 PM), and Lunokhod's 108 min match the canonical Russian primary source. But the headline numeric result (−3%) is missing, and the FAQ block is unrelated boilerplate. |
| Should this file be cited as a source? | **No** for the underlying claims — cite the NET #3 Nov-Dec 2001 primary source. **Yes** as a pointer indicating that the original article is hosted in fragmentary form on Scribd by uploader Leon Blažinović (user 364320689), uploaded ~2020-12-06. |

### Action items implied for the broader audit

1. **Locate the underlying PDF** — either fetch the 3 page images from Scribd, or find the full NET #3 Nov-Dec 2001 issue through other channels. The Scribd page exists; only the HTML wrapper here is content-empty.
2. **Once the PDF is retrieved**, expect to be able to fill the gap explicitly noted in F-12R analysis §16.1 (Konov 3% protocol) and to cross-validate the "high-temperature mouse mortality" framing introduced uniquely by the AI summary.
3. **Mark the FAQ JSON-LD block as boilerplate** in any downstream tooling that scrapes Scribd metadata — it will mislead any LLM treating it as document-derived Q&A.
