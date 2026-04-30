# Adversarial-OSINT validation runs / Покомпанийные прогоны валидации adversarial-OSINT

Bilingual EN+RU **placeholder directory** for per-company adversarial-OSINT validation outputs. The methodology is described in [`../adversarial-osint-framing.md`](../adversarial-osint-framing.md). This directory is the **execution layer** of that methodology.

---

## Status / Статус

**EN:** **Scheduled for v5+, not yet executed.** As of v4 (2026-04-30) this directory contains only the README placeholder. Per-company runs (one file per company in `companies/` directory) are scheduled for the v5+ research pass.

**RU:** **Запланировано на v5+, ещё не исполнено.** На момент v4 (2026-04-30) каталог содержит только README-заглушку. Покомпанийные прогоны (один файл на компанию из каталога `companies/`) запланированы на исследовательский проход v5+.

---

## Workflow / Рабочий процесс

**EN:** When per-company adversarial-OSINT runs are executed, each company gets one file:

```
analysis/adversarial-osint-runs/
├── README.md                    — this file
├── amentum.md                   — pending v5+
├── lockheed-martin.md           — pending v5+
├── boeing.md                    — pending v5+
├── raytheon-rtx.md              — pending v5+
├── northrop-grumman.md          — pending v5+
├── leidos.md                    — pending v5+
├── honeywell.md                 — pending v5+
└── egng.md                      — pending v5+
```

Each per-company file follows the output template in [`../adversarial-osint-framing.md`](../adversarial-osint-framing.md): consensus / divergence-flag / unique-contribution-per-pass annotations, with explicit pointers to the company's `companies/<name>.md` source-of-truth file.

**RU:** Когда покомпанийные прогоны adversarial-OSINT исполнены, каждая компания получает один файл (см. структуру выше). Каждый покомпанийный файл следует выходному шаблону из [`../adversarial-osint-framing.md`](../adversarial-osint-framing.md): аннотации консенсус / флаг расхождения / уникальный вклад прохода, с явными указателями на файл-источник правды компании `companies/<name>.md`.

---

## Example of methodology in narrative form / Пример методологии в нарративной форме

**EN:** [`../ukraine-context-pass.md`](../ukraine-context-pass.md) (v4) applies the 3-pass framing to a thematic question (whether Ukrainian entities surface in the archive) rather than to a single company. It exemplifies a "null-finding probe → partial-finding" result. The thematic-vs-company distinction is intentional: thematic passes go directly into `analysis/`; per-company passes go into `analysis/adversarial-osint-runs/`.

**RU:** [`../ukraine-context-pass.md`](../ukraine-context-pass.md) (v4) применяет 3-проходную рамку к тематическому вопросу (всплывают ли украинские сущности в архиве), а не к одной компании. Файл иллюстрирует результат «зонд нулевого вывода → частичный результат». Разграничение тематический-против-покомпанийного намеренно: тематические проходы идут прямо в `analysis/`; покомпанийные проходы — в `analysis/adversarial-osint-runs/`.

---

[← Adversarial-OSINT framing methodology / Методология рамки adversarial-OSINT](../adversarial-osint-framing.md) · [← Track 7 README / README Трека 7](../../README.md)
