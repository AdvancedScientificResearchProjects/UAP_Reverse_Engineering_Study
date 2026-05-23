# war-gov-pursue-archive — CHANGELOG

## v0.2.0 — 2026-05-23 — Release 02 ingestion

### Added
- **64 new records** from PURSUE Release 02 (war.gov, published 2026-05-22):
  - 6 PDFs from 4 agencies (CIA, DOE, DOW, ODNI — all but DOW are new to PURSUE)
  - 7 NASA audio excerpts (Mercury–Apollo programmes, 1961–1972)
  - 51 DOW unresolved/pending video reports (PR050–PR099; 50 unique DVIDS assets)
- New per-document cards (`analysis/per-document/`):
  - `CIA-UAP-D001_USSR-SARY-SHAGAN-1973.md` — first CIA record in PURSUE corpus
  - `DOE-UAP-D001_PANTEX-RADAR.md` — Pantex nuclear-weapons facility radar imagery
  - `DOE-UAP-D002_JAMES-TUCK-CORRESPONDENCE.md` — LANL physicist correspondence on UFOs (1970s)
  - `DOE-UAP-D003_PAJARITO-ASTRONOMERS.md` — 1986 Los Alamos amateur astronomy club UFO talk
  - `DOW-UAP-D017_SANDIA-GREEN-FIREBALLS.md` — 1948–1950 Sandia/Kirtland/LANL Green-Fireball corpus (66 MB compendium, the headline R02 document)
  - `ODNI-UAP-D001_USPER-ORANGE-ORBS-2025.md` — first-person USIC senior officer narrative, pairs with R01 FBI Western US IR photos
- New catalog file: `catalog/documents-r02.md` (chronological 64-record table)
- New manifest: `manifest_r02.json` (sha256 + DVIDS asset mapping for all 6 PDFs + 6 thumbnails + 57 unique videos)
- New topical synthesis: `analysis/topical/r02-nm-nuclear-complex-1948-1986.md`
- Extended `analysis/MASTER_pursue_claims.md` with Release 02 section
- Extended `catalog/source_codes.md` with R02 code registry (CIA, DOE, ODNI, DOW-D017, DOW-PR050..099, NASA-D008..D014)
- Raw symlinks: `raw/r02/{pdf,thumbnails,video,uap-data.csv}` → `_inbox/2026-05-22-war-gov-pursue-r02/`

### Cross-archive
- Updated `analysis/cross-archive-synthesis.md` to add R02 implications under Theme 4 (Federal disclosure lineage)
- Updated `graph/fragments/agentI_war_gov_pursue.py` with R02 entities (CIA, DOE, ODNI institutions; LANL/Sandia/PANTEX/Pajarito edges to people-analysis Track 6)
- Updated root `README.md` Track 11 counts (161 → 225 records, 11 → 13 agencies via CIA, DOE, ODNI)

### Cross-reference findings
- **ODNI-UAP-D001 pairs explicitly with 32 R01 records** (FBI Photo A001–A008 + B001–B024 + USPER Statement) via the official `PdfPair` field in the war.gov CSV. ODNI-UAP-D001 is the eyewitness narrative for the R01 FBI Western US 2025 IR-photo corpus.
- **R02 introduces zero overlapping codes with R01** (verified via 77 R01 codes vs 64 R02 codes ∩ = ∅). All R02 D-codes (DOW-D017, NASA D008–D014) fill gaps in R01 numbering; all R02 PR-codes (050–099) continue R01's PR19–PR49 sequence.

### Sources
- Master database: https://www.war.gov/Portals/1/Interactive/2026/UFO/uap-data.csv (291 KB)
- Document bundle: https://www.war.gov/medialink/ufo/052226/release_02/release_02_document_bundle.zip (67 MB)
- Video bundle: https://d34w7g4gy10iej.cloudfront.net/uap052226.zip (5.6 GB)
- DVIDS API used for record↔asset mapping (api.dvidshub.net, requires `Origin: https://www.war.gov` header)

### Method
- All 64 records sha256-verified
- pdftotext -layout used for the 6 PDF transcripts (no OCR pass needed; PDFs are native-text)
- Video/audio transcripts (Whisper) deferred to v0.2.1

### Pending (v0.2.1+)
- Whisper transcripts for 57 DVIDS audio/video files
- Per-document cards for the 51 PR-series videos (template-based, low-effort)
- Per-document cards for the 7 NASA audio excerpts (low-effort, mission-context)
- Render `diagrams/rendered/r02_*` Mermaid diagrams (R02 verdict distribution, R02 agency breakdown)

---

## v0.1.0 — 2026-05-10 — Initial archive release (Release 01)

### Added
- 161 records from PURSUE Release 01 (war.gov, published 2026-05-08):
  - 121 PDFs, 28 videos, 14 images
  - Agencies: Department of War (82), FBI (57), NASA (14), Department of State (7), Other/COMETA (1)
- Full catalog (`catalog/{documents,typology,source_codes,irrelevant_sources}.md`)
- 67 OCR-augmented PDFs via EasyOCR + reportlab + pikepdf pipeline (PC2 RTX 3060)
- 158 per-document cards (`analysis/per-document/`) covering all major records
- 7 topical syntheses (`analysis/topical/`): historical 1944–1968, NASA spaceflight 1965–1974, CENTCOM 2013–2026, INDOPACOM 2020–2026, FBI Western US 2023–2025, State Dept cables 1952–2004, propulsion tech claims
- `analysis/MASTER_pursue_claims.md` — full corpus claim synthesis
- `analysis/QA_REVIEW.md` — verbatim-quote audit, hallucination cross-check
- Rendered diagrams: `diagrams/rendered/verdict_distribution.png`, `agency_record_distribution.png`, `cabell_propulsion_taxonomy_1949_to_aaro_2026.png`
- `graph/fragments/agentI_war_gov_pursue.py` graph fragment for `uap_kumu.json`
- Cross-archive integration: Theme 4 in `analysis/cross-archive-synthesis.md`; Track 11 in root README
- 1 file corrupted at source: `331_120752_..._german_armament_equipment_documents.pdf` (Foo-fighters / 415th NFS / SHAEF — irrecoverable from war.gov; xref-table broken; recovery attempts via qpdf, ghostscript, pikepdf all failed; future retry from web.archive.org pending)
