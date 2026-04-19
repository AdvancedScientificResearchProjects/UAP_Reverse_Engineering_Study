# MG-05 Part 2 of 3 — Extract (Chernobrov, "Медведицкая гряда")

**Source file:** `books/downloads/fb2_chunks/MG-05_part2of3.txt`
**Source code:** `MG-05-p2` (merge target: `B-MG05`)
**Primary reference cross-check:** `perplexity-research/03_user_provided_research_2026-04-18.md` §4 (Медведицкая гряда corpus)
**Analysis date:** 2026-04-18

---

## CRITICAL FINDING — CHUNK CONTAINS NO BOOK TEXT

After byte-level analysis of the source file, **`MG-05_part2of3.txt` contains ZERO extractable book text**. The chunk is 2,713,946 bytes of pure base64-encoded binary payload (embedded JPEG images from the original FB2 archive). No Cyrillic characters, no XML tags, no prose of any kind.

### Forensic evidence

1. **File structure:** single line, 2,713,946 ASCII bytes, no line terminators, max line length 65,536 (classic base64 stream).
2. **Cyrillic byte count:** `0` (searched for UTF-8 lead bytes `0xD0`/`0xD1` across the entire file — none present).
3. **XML/FB2 markers absent:** `<p>`, `<section>`, `<binary>`, `<body>`, `<title-info>`, `<?xml`, `<FictionBook` — all return `-1` on search.
4. **Character distribution** (first 10K bytes) matches base64 alphabet (`A-Za-z0-9+/=`), with no whitespace or punctuation outside that set.
5. **Content boundaries:**
   - File head: `OWF0y/bgY61HNK8/jiGK3dlilVitWyDV4UPxwdFGB1R1Ioekd…` — mid-stream base64.
   - File tail: `…Y35Z/AZP/wBpT9mYmB2S+1AnaHem9MHevkKfUlp3Uz+hLFj/gPwM/qRJY69euX9gT7f2o/wAGN+2+C1ycf+BSB//Z` — classic JPEG trailer signature (`//Z` = JPEG `FFD9` end-of-image marker in base64).

### Cause — chunking artifact

Cross-comparison with sibling chunks confirms the splitter bisected the FB2's large embedded image block:

| Chunk | Size | Cyrillic bytes | Contains book text? |
| --- | --- | --- | --- |
| `MG-05_part1of3.txt` | 2,972,645 B | 420,043 | **YES** — all book prose, ending ~offset 950,841; balance is base64 image prefix |
| `MG-05_part2of3.txt` | 2,713,946 B | **0** | **NO** — mid-stream base64 image payload only |
| `MG-05_part3of3.txt` | 2,494,324 B | **0** | **NO** — tail of base64 image payload, ending with JPEG trailer |

Total book text (including all prose, photo captions, and embedded reports) lives **entirely within the first ~950 KB of `MG-05_part1of3.txt`**. Parts 2 and 3 contain only the FB2's `<binary>` section (scanned photographs from expeditions, maps of the гряда, etc.) encoded as base64.

---

## Technical claims extracted from this chunk

**None.** There is no textual content in this chunk to extract claims from.

### Topics not covered here (would-be locations)

All nine focus topics for Медведицкая гряда — landing sites, engine-stall zones, 44-expedition statistics, ball lightning ("жгуч"), хрональные аномалии, "чёртово логово", магнитные аномалии, подземные тоннели/пирамидальные курганы, свидетельские отчёты — **are NOT present in part 2**. These topics, if covered by Chernobrov in this book, will appear in:

- **`MG-05_part1of3.txt`** (byte range 0 – ~950,841) — sole locus of book text for MG-05.

Part-1 extraction should therefore be treated as the **complete text corpus** of "Медведицкая гряда" for analytical purposes; parts 2 and 3 contribute only photographic evidence that would require OCR or visual inspection (out of scope for text extraction).

---

## Recommendations for the `B-MG05` merge

1. **Do not re-process parts 2 and 3 for text extraction.** They yield zero signal at any amount of compute.
2. **Treat `MG-05_part1_extract.md` as canonical** for all nine focus topics. If part-1 extraction reports low claim density, that reflects the book's actual text-to-image ratio (heavy photographic documentation), not a sampling gap.
3. **Optional binary rescue path** (only if the photo captions are discovered to be embedded in image metadata or if page-level OCR is later justified):
   - Decode base64 streams from parts 1 (tail) + 2 + 3 into JPEG(s).
   - Feed JPEGs through OCR for any visible Russian text (captions, map labels, document scans).
   - This is NOT recommended at present — the FB2 extractor should have preserved all text prose in the XML, so the binary section is almost certainly pure photography.
4. **Reporting in `B-MG05`:** mark part-2 and part-3 as "no-text chunks (base64 binary)" with one-line justification pointing at this extract.

---

## Cross-reference check vs. primary reference §4 (Medveditskaya corpus)

The user-provided research document lists Медведицкая гряда content as belonging to Chernobrov's broader published-work corpus (referenced under "Тайны и Парадоксы Времени" §2 of the primary reference: *«часы "отстают" … на Медведицкой гряде … "на доли секунды в час"»*). Those claims are summary-level and originate from OTHER Chernobrov titles, not MG-05 itself. Part-2 of MG-05 provides no additional cross-referenceable claims because it contains no text.

No conflict with the primary reference is introduced by this empty extract.

---

## Extract metrics

| Metric | Value |
| --- | --- |
| Source bytes processed | 2,713,946 |
| Cyrillic bytes detected | 0 |
| XML tags detected | 0 |
| Book-text claims extracted | 0 |
| Target extract size | 30–50 KB |
| Actual extract size | ~4 KB (forensic note only) |
| Rationale for undersized output | Source chunk contains no extractable text content |
