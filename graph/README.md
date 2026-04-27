# UAP Reverse-Engineering — Facts & Events Graph

**EN:** Interactive bilingual knowledge-graph of facts, events, persons, institutions, phenomena, sources and hypotheses extracted from the `UAP_Reverse_Engineering_Study` repository. Renders in the browser via Cytoscape.js, with EN/RU toggle, type filters, search, fcose layout, and a side-panel dossier view. Same Kumu-blueprint property-graph format as the sibling `ASRP_ecosystem_marketing/graph/` graph — entity ids are stable across both, so the two can be merged into a single Neo4j-class DB later.

**RU:** Интерактивный двуязычный граф знаний по фактам, событиям, людям, институциям, явлениям, источникам и гипотезам, извлечённым из репозитория `UAP_Reverse_Engineering_Study`. Отрисовывается в браузере через Cytoscape.js, с переключателем EN/RU, фильтрами по типу, поиском, fcose-раскладкой и боковой панелью «досье». Тот же property-graph-формат Kumu, что и в соседнем графе `ASRP_ecosystem_marketing/graph/` — id сущностей стабильны между ними, и оба графа можно объединить в одну Neo4j-class БД.

---

## Quick start / Быстрый старт

```bash
# from this directory / из этого каталога
python3 -m http.server 8765
# open http://127.0.0.1:8765/preview.html
# открыть http://127.0.0.1:8765/preview.html
```

Регенерация JSON / re-generate the JSON:

```bash
python3 build_blueprint.py
```

Что писать в Kumu / Kumu cloud import:
1. Open <https://kumu.io>, create a new project, choose **Blueprint** import
2. Drag-and-drop `uap_kumu.json` into the Kumu canvas

---

## Structure / Структура

```
graph/
├── README.md              ← this file / этот файл
├── build_blueprint.py     ← Python source-of-truth · ID-anchors + integration / Python-источник истины
├── uap_kumu.json          ← generated property-graph / сгенерированный property-graph
├── preview.html           ← browser viewer · EN/RU toggle / браузерный просмотр · EN/RU
├── libs/                  ← vendored Cytoscape + fcose + cose-bilkent
│   ├── cytoscape.min.js
│   ├── cytoscape-fcose.js
│   ├── cytoscape-cose-bilkent.js
│   ├── cose-base.js
│   └── layout-base.js
└── fragments/             ← per-track entity extractions / поэтрековые извлечения
    ├── agentA_dubna_lazar.py    (Track 4 + Track 2)
    ├── agentB_chernobrov.py     (Track 3)
    ├── agentC_osint_people.py   (Track 5 + Track 6 + Track 8)
    └── agentD_track1.py         (Track 1 — UAP-FRAG-001 ECP + AI/CV)
```

---

## Final stats / Итоговые цифры

|                                        | count   |
|----------------------------------------|---------|
| elements / сущностей                   | 275     |
| connections / связей                   | 447     |
| orphans / висячих сущностей            | 0       |
| dangling connections / битых связей    | 0       |
| RU label coverage / покрытие RU-меток  | 100 %   |
| RU description coverage / покрытие     | 100 %   |
| facts / фактов                         | 64      |
| · confidence high / уверенность высокая| 40      |
| · confidence medium / средняя          | 17      |
| · confidence low / низкая              | 7       |

### Type breakdown

| type / тип            | count |
|-----------------------|------:|
| fact                  | 64 |
| event                 | 50 |
| person · external     | 35 |
| source                | 35 |
| institution           | 34 |
| hypothesis            | 21 |
| phenomenon            | 13 |
| person · team         | 5 |
| tooling-class         | 5 |
| outreach              | 4 |
| theory-anchor         | 3 |
| project               | 2 |
| cluster               | 2 |
| patent                | 1 |
| accreditation         | 1 |

---

## Honesty policy / Политика добросовестности

**EN:** Every fact node carries an explicit `confidence` field (`high` / `medium` / `low`) and a `source` field pointing at a primary-source id. Lazar-class single-witness claims are stored at `confidence="low"`. For each major Lazar claim there is a separate fact-node recording the contradicting evidence with `confidence="high"` and the appropriate edge direction (`challenges` / `contradicted-by`). The graph honestly shows where the evidence is weakest.

**RU:** Каждый факт несёт явное поле `confidence` (`high` / `medium` / `low`) и поле `source` со ссылкой на id первоисточника. Заявления уровня одиночного свидетеля (как у Лазара) хранятся с `confidence="low"`. Для каждого крупного заявления Лазара существует отдельный факт-узел с противоречащими данными при `confidence="high"` и соответствующим направлением рёбер (`challenges` / `contradicted-by`). Граф честно показывает, где доказательная база слабее всего.

---

## Cross-graph compatibility / Совместимость с соседним графом

**EN:** The following ids are identical across this graph and `<asrp-marketing-repo>/graph/asrp_kumu.json`. A `MERGE` / `UNWIND` script in any property-graph DB (Neo4j, Memgraph, ArangoDB, Amazon Neptune) will deduplicate them into a single node:

| shared id | label |
|-----------|-------|
| `p-db`, `p-vo`, `p-mk`, `p-kz`, `p-aovs` | ASRP team members |
| `p-burilova` | Tatyana Burilova (HSP percipient) |
| `p-lazar`, `p-chernobrov`, `p-cardillo` | external persons |
| `inst-jinr`, `inst-doe`, `inst-darpa`, `inst-nswc`, `inst-stanford`, `inst-cortical`, `inst-boeing` | institutions |
| `p-nolan` | external persons |
| `or-doe`, `or-stanford`, `or-nci`, `or-cortical` | outreach tracks |
| `pj-uap`, `pj-plasma` | projects |
| `pat-fbhfs` | patent |
| `acc-darpa` | accreditation |
| `th-temporal`, `th-3dt`, `th-hyperbolic` | theory anchors |
| `ev-ecp` | ECP-2026-04-04 master event |

---

## Tracks covered / Охваченные треки

| Track | Subject | Source files | Entities |
|-------|---------|--------------|---------:|
| 1 | UAP-FRAG-001 ECP + AI/CV multi-pipeline | `reports/`, `experiments/`, `pipeline/` | ~30 |
| 2 | Bob Lazar archive 1989–2026 | `bob-lazar-archive/` | ~40 |
| 3 | Vadim Chernobrov / Kosmopoisk 1982–2017 | `chernobrov-archive/` | ~50 |
| 4 | Dubna / Element 115 | `dubna-element-115-analysis/` | ~50 |
| 5 | OSINT methodology | `osint-intelligence-analysis/` | ~10 |
| 6 | FBI 11-scientist cluster (2026-04-19) | `people-analysis/` | ~30 |
| 8 | Cross-archive synthesis | `analysis/cross-archive-synthesis.md`, `analysis/uap-taxonomy.md` | bridges |

(Track 7 — Corporate / Economic — is a placeholder in the parent README and intentionally absent here.)

---

## Future migration to a graph DB / Миграция в графовую БД

The `uap_kumu.json` format is **property-graph**, identical in semantics to Neo4j / ArangoDB / Memgraph / Amazon Neptune. A future `MERGE` / `UNWIND` Cypher script will turn this JSON plus the marketing graph JSON into one live graph DB without any content loss; ids are deliberately stable across both.

---

## Build invariants / Инварианты сборки

`build_blueprint.py` enforces the following at end of each run:

- **0 orphans** — every element has at least one connection
- **0 dangling connections** — every connection's `from` and `to` resolve to known elements
- **0 duplicate ids** — `E()` silently skips re-definitions, so anchor IDs (e.g. `p-lazar`) defined in section 0 take precedence
- **100 % `descriptionRu` coverage**, **100 % `labelRu` coverage**
- Confidence breakdown printed for facts; non-trivial low-confidence count means the graph is honestly cautious about the Lazar-class material
