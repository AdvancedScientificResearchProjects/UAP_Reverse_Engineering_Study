# Gershtein archive — Diagrams / Диаграммы

Visual diagrams (Mermaid sources, hand-authored SVG tables, rendered PNGs)
summarising M.B. Gershtein's claims as catalogued in
`analysis/MASTER_gershtein_claims.md`.

Визуальные диаграммы (исходники Mermaid, рукописные SVG-таблицы и
готовые PNG-рендеры), обобщающие заявления М.Б. Герштейна по результатам
синтеза в MASTER-документе.

## Mermaid sources / Исходники Mermaid

| File | Purpose (EN) | Назначение (RU) |
|---|---|---|
| `timeline_career.mmd` | Career arc 1972–2026: birth, first sighting, RGS, 14 books, 21.03.2026 watershed lecture | Карьерный путь 1972–2026: рождение, первое наблюдение, РГО, 14 книг, лекция 21.03.2026 |
| `soviet_program_chain.mmd` | Setka-AN/MO → Galaktika → Horizon → NIT-3/54 institutional genealogy + KGB/MO archives + 1993–1997 dossier exfiltration | Институциональная цепочка «Сетка» → «Галактика» → «Горизонт» → НИТ-3/54 + архивы КГБ/МО + вывоз досье 1993–1997 |
| `nde_ufo_thesis.mmd` | NDE↔UFO thesis (NN 17, 14.10.2023): inputs → three-types-of-mind → cross-cultural patterns → NN 62 vital-energy refinement → centrifuge counter-evidence | Тезис связи НЛО↔ОСО (NN 17): входы → три типа разума → кросс-культурные параллели → уточнение через жизненную энергию (NN 62) → контрдоказательство центрифуги |
| `cross_archive_intersections.mmd` | Edges from Gershtein corpus to chernobrov-archive (Dalnegorsk/Petrozavodsk/MG) and bob-lazar-archive (NN 28 dismissal); Anfalov NN 23 adjacent | Связи корпуса Герштейна с архивами Черноброва (Дальнегорск, Петрозаводск, МГ) и Лазара (отказ NN 28); сопряжённый материал Анфалова (NN 23) |
| `corpus_thematic_map.mmd` | Mindmap: 81 sources clustered across 13 thematic sections (§1–§13), anchor codes per section | Майндмэп: 81 источник по 13 тематическим разделам (§1–§13), якорные коды |

## Standalone SVG tables / Самостоятельные SVG-таблицы

Hand-authored SVGs in the same visual convention as
`bob-lazar-archive/diagrams/` and `chernobrov-archive/diagrams/`. Each follows
the universal three-table contract for ASRP archives.

Рукописные SVG в той же визуальной конвенции, что и в `bob-lazar-archive/` и
`chernobrov-archive/`. Каждый файл следует универсальному контракту трёх
таблиц для архивов ASRP.

| File | Purpose (EN) | Назначение (RU) |
|---|---|---|
| `claim_corroboration.svg` | 16 most-cited Gershtein claims × 9 primary source codes; cross-source verification matrix (verbatim / partial / n/a / untestable) | 16 ключевых заявлений × 9 первичных кодов источников; матрица кросс-источниковой верификации (дословно / частично / н/д / непроверяемо) |
| `source_credibility_matrix.svg` | 27 representative source codes (of 81 deduplicated) tiered A→E by evidentiary strength; verbatim from MASTER §0 | 27 представительных кодов (из 81 дедуплицированного), уровни A→E по силе свидетельств; дословно из MASTER §0 |
| `numerical_params_table.svg` | 20 key quantitative claims from MASTER §0.0 (Soviet programmes, NDE, methodology, multiverse, totals); status-tagged (STABLE / DRIFTED) | 20 ключевых количественных заявлений по MASTER §0.0 (сов. программы, ОСО, методология, мультиверс, итоги); со статусом (устойчиво / дрейф) |

## Rendered PNGs / Готовые PNG-рендеры

PNG renders of the five `.mmd` files, in `rendered/`. Generated from Python
(matplotlib + networkx + graphviz `dot`), not Mermaid CLI — see «Regeneration»
section below.

PNG-рендеры пяти `.mmd` файлов, в каталоге `rendered/`. Сгенерированы из
Python (matplotlib + networkx + graphviz `dot`), не через Mermaid CLI — см.
раздел «Перегенерация» ниже.

| File | Source | Backend |
|---|---|---|
| `rendered/timeline_career.png`              | `timeline_career.mmd`              | matplotlib horizontal-timeline |
| `rendered/soviet_program_chain.png`         | `soviet_program_chain.mmd`         | graphviz `dot` (hierarchical) |
| `rendered/nde_ufo_thesis.png`               | `nde_ufo_thesis.mmd`               | graphviz `dot` (LR layout) |
| `rendered/cross_archive_intersections.png`  | `cross_archive_intersections.mmd`  | matplotlib + custom layout |
| `rendered/corpus_thematic_map.png`          | `corpus_thematic_map.mmd`          | matplotlib radial mind-map |

## Conventions / Конвенции

- Format: Mermaid (`.mmd`) for source diagrams, hand-authored SVG for
  standalone tables; PNG renders in `rendered/`.
- Top comment block of each `.mmd` file: bilingual EN/RU description +
  source-code citations.
- Node labels: bilingual EN/RU pairs where space allows.
- Source codes cited verbatim from MASTER §0 (no invented codes).
- Each `.mmd` file kept under 100 lines.
- SVG palette mirrors `chernobrov-archive` and `bob-lazar-archive`:
  legend cells `#9ad17b` / `#f6c85f` / `#f29c99` / `#bfcfe7` / `#d9d9d9`,
  alternating row backgrounds `#f8fafc` / `#ffffff`, header bar `#1f2937`.

## Regeneration / Перегенерация

Image artifacts (3 SVGs + 5 PNGs) are produced by `gershtein-archive/generate_diagrams.py`,
which is **gitignored** per the `gershtein-archive/*.py` rule in the repo
`.gitignore`. The script and its venv are local-only; only the generated
image files are committed.

Артефакты (3 SVG + 5 PNG) генерируются скриптом `gershtein-archive/generate_diagrams.py`
(в `.gitignore` по правилу `gershtein-archive/*.py`). Скрипт и venv —
локальные, в репозиторий попадают только сгенерированные изображения.

```bash
# From gershtein-archive/
uv venv                                              # creates .venv (gitignored)
uv pip install matplotlib pillow svgwrite networkx graphviz
.venv/bin/python generate_diagrams.py                # writes 3 SVGs + 5 PNGs
```

Requirements:
- Python 3.10+
- `graphviz` system package (provides `dot` binary) — used for the two
  flowchart-shaped renders. If `dot` is missing, the script falls back to a
  networkx + matplotlib spring layout for those two files.
- For Cyrillic node labels in graphviz output, the `fonts-dejavu` system
  package must be installed (script requests `DejaVu Sans` font).
