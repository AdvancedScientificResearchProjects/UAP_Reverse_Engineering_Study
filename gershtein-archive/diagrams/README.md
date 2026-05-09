# Gershtein archive — Diagrams / Диаграммы

Visual diagrams (Mermaid sources; rendered SVG/PNG to follow) summarising
M.B. Gershtein's claims as catalogued in `analysis/MASTER_gershtein_claims.md`.

Визуальные диаграммы (исходники Mermaid; SVG/PNG будут добавлены), обобщающие
заявления М.Б. Герштейна по результатам синтеза в MASTER-документе.

## Diagram catalog / Каталог диаграмм

| File | Purpose (EN) | Назначение (RU) |
|---|---|---|
| `timeline_career.mmd` | Career arc 1972–2026: birth, first sighting, RGS, 14 books, 21.03.2026 watershed lecture | Карьерный путь 1972–2026: рождение, первое наблюдение, РГО, 14 книг, лекция 21.03.2026 |
| `soviet_program_chain.mmd` | Setka-AN/MO → Galaktika → Horizon → NIT-3/54 institutional genealogy + KGB/MO archives + 1993–1997 dossier exfiltration | Институциональная цепочка «Сетка» → «Галактика» → «Горизонт» → НИТ-3/54 + архивы КГБ/МО + вывоз досье 1993–1997 |
| `nde_ufo_thesis.mmd` | NDE↔UFO thesis (NN 17, 14.10.2023): inputs → three-types-of-mind → cross-cultural patterns → NN 62 vital-energy refinement → centrifuge counter-evidence | Тезис связи НЛО↔ОСО (NN 17): входы → три типа разума → кросс-культурные параллели → уточнение через жизненную энергию (NN 62) → контрдоказательство центрифуги |
| `cross_archive_intersections.mmd` | Edges from Gershtein corpus to chernobrov-archive (Dalnegorsk/Petrozavodsk/MG) and bob-lazar-archive (NN 28 dismissal); Anfalov NN 23 adjacent | Связи корпуса Герштейна с архивами Черноброва (Дальнегорск, Петрозаводск, МГ) и Лазара (отказ NN 28); сопряжённый материал Анфалова (NN 23) |
| `corpus_thematic_map.mmd` | Mindmap: 81 sources clustered across 12 thematic sections (§1–§13), anchor codes per section | Майндмэп: 81 источник по 12 тематическим разделам (§1–§13), якорные коды |

## Conventions / Конвенции

- Format: Mermaid (`.mmd`), matches sibling-archive convention
  (`bob-lazar-archive/diagrams/`, `chernobrov-archive/diagrams/`).
- Top comment block: bilingual EN/RU description + source-code citations.
- Node labels: bilingual EN/RU pairs where space allows.
- Source codes cited verbatim from MASTER §0 (no invented codes).
- Each `.mmd` file kept under 100 lines.

## Rendering / Рендеринг

The `.mmd` files render directly on GitHub. To produce PNG/SVG locally:

```bash
npm install -g @mermaid-js/mermaid-cli
mmdc -i timeline_career.mmd -o rendered/timeline_career.png
mmdc -i soviet_program_chain.mmd -o rendered/soviet_program_chain.png
mmdc -i nde_ufo_thesis.mmd -o rendered/nde_ufo_thesis.png
mmdc -i cross_archive_intersections.mmd -o rendered/cross_archive_intersections.png
mmdc -i corpus_thematic_map.mmd -o rendered/corpus_thematic_map.png
```

Rendered outputs go in `rendered/` (currently empty — populated when
`mermaid-cli` is run as part of release prep).
