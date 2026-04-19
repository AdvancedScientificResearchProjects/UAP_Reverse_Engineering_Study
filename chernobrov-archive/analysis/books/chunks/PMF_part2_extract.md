# PMF Part 2 of 2 — Technical Claims Extract

**Source file:** `books/downloads/fb2_chunks/PMF_part2of2.txt`
**Source code:** `PMF-p2` (merge → `B-PMF`)
**Book:** Чернобров В.А., Климов В.А., Гаврилов Л.Г. — «Подмосковье: феномены, аномалии, чудеса. Путеводитель»
**Extraction date:** 2026-04-18

---

## CRITICAL FINDING: NO TEXTUAL CONTENT IN PART 2

`PMF_part2of2.txt` (2,312,199 bytes / 2.3 MB) contains **zero extractable textual claims**. The file is a single line with no line terminators (`ASCII text, with very long lines (65536), with no line terminators`) consisting entirely of base64-encoded binary image data.

### Quantitative verification

| Metric | Value |
|---|---|
| Total characters | 2,312,199 |
| Cyrillic characters | 0 |
| Latin words / English prose | 0 |
| XML / FB2 tags (`<`, `<binary`, `<body`, `FictionBook`) | 0 occurrences each |
| Base64 token segments (whitespace-separated) | 31,687 |

### Evidence the data is image binary

- Base64 decode of the file yields a byte stream whose tail ends with `... eb 1f ff d9` (hex) — the standard **JPEG End-Of-Image marker `FF D9`**.
- Decoded head bytes do not match a single JPEG SOI (`FF D8`) because the file is a **concatenation of multiple JPEG binary sections** from the FB2 source (the original `<binary>` blocks of the FB2 container holding photographs/illustrations).
- Last 500 characters of the file show the trailing base64 terminating with `...8J/Z` which decodes to the JPEG EOI, confirming the file terminates a JPEG stream.

### Evidence from Part 1 confirming spillover

- `PMF_part1of2.txt` (also 2,312,231 bytes) contains the actual book text. Cyrillic ratio: **14.1%** (326,691 Cyrillic chars in 2,312,231 total).
- The last Cyrillic character in Part 1 is at byte offset **408,204**.
- Immediately after that offset, Part 1 transitions into base64 image data (verified tail: `...местность заброшена. /9j/4AAQSkZJRgABAQEASABIAAD/2wBDAAMCAgIC...`). `/9j/4A...` is the base64 prefix for a JPEG starting with `FF D8 FF E0` (JFIF/JPEG SOI + APP0).
- The text `Примечания 1 Церковь феноменально не сориентирована по сторонам света, местность заброшена.` is the FINAL sentence of the book body (footnote #1), confirming all narrative/technical prose of PMF ends inside Part 1 at ~byte 408,204.
- The remaining ~1.9 MB of Part 1 plus the entire 2.3 MB of Part 2 is a continuous base64 image payload (≈ 4.2 MB of base64 ≈ ~3.1 MB of decoded JPEG photographs — guidebook illustrations).

### Structural conclusion about the FB2 chunking pipeline

The upstream `fb2_chunks` splitter appears to have stripped `<binary>...</binary>` tag framing and then naïvely split by byte offset, so:
- Part 1 = (all textual `<section>` content) + (first ~1.9 MB of concatenated image base64).
- Part 2 = (remaining ~2.3 MB of concatenated image base64 terminating with JPEG EOI `FF D9`).

No text was truncated — Part 1 holds the complete narrative. Part 2 is pure binary spillover.

---

## Claims extracted from PMF Part 2

**None.** The file contains no prose, no tables, no captions, no footnotes, and no technical statements of any kind.

All technical claims for book `B-PMF` must be drawn from `PMF_part1of2.txt` (the Part 1 extract). The Part 1 extract fully represents the textual scope of the book; merging Part 1 and Part 2 extracts for `B-PMF` therefore requires no additions from Part 2.

---

## Recommendation for the merge step (B-PMF)

1. Treat `PMF_part2_extract.md` as an **empty contribution** during the merge → `B-PMF`.
2. The canonical `B-PMF` extract should be a direct promotion of `PMF_part1_extract.md` (pending) with a metadata note referencing this finding.
3. If higher-quality text is needed, re-run FB2 extraction with a parser that (a) preserves FB2 XML structure, (b) separates `<body>` from `<binary>` elements, and (c) outputs text-only chunks for `<body>` content. Suggested tools: `fb2-to-txt`, `pandoc --from=fb2`, or a custom `lxml` parser that extracts `//body//text()` only.
4. Any photographs/illustrations needed for the visual corpus can be recovered by base64-decoding and carving JPEGs from the concatenated stream formed by (Part 1 bytes 408,204→end) + (all of Part 2).

---

## Cross-reference with primary research document

Primary reference `perplexity-research/03_user_provided_research_2026-04-18.md` does not catalogue «Подмосковье: феномены, аномалии, чудеса» as a numbered entry in its main books list (entries 1–4 cover «Тайны Времени», «Тайны и Парадоксы Времени», «Эксперименты по созданию Машины Времени», and «Время, Бессмертие, Человек»). The PMF guidebook is therefore a **secondary / context source** for the anomalous-zones corpus rather than a primary chronotech-engineering source, consistent with its role as a regional tourist/anomalies путеводитель.

Relevant thematic anchors from the primary reference that can be paired with Part 1 content (not Part 2):
- Line 50: «часы "отстают" в районе падения Тунгусского метеорита, на Медведицкой гряде, местах посадок НЛО — на доли секунды в час» — if Part 1 names any Podmoskovye chrono-anomaly zones with similar clock-lag magnitude, they belong with this cluster.
- Line 88: «исследования "Космопоиска" по хрональным аномалиям в "гиблых местах"» — PMF catalogues Moscow-region «гиблые места» by definition.

No Part 2 content contributes to either anchor because Part 2 contains no text.
