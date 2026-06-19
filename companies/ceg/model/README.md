# Model — CEG

This folder holds the structured valuation scenarios for Constellation Energy.

Files:

```text
model_assumptions.md   # drivers behind valuation.md (bear/base/bull EPS x multiple)
scenario_model.csv     # bear/base/bull: adj-EPS x terminal P/E -> price, reconciled to memo-v1 ranges
```

Discipline (same as template / NBIS):

- **Explicit units** — EPS in USD, multiples in x, prices in USD.
- **Source IDs in notes** — drivers cite claim_ids (C0xx) from `../claim_ledger.csv`.
- **Historical facts separated from forecasts** — actuals (FY2025 / Q1'26) cite `../facts.md`; everything forward is an assumption.
- **Bear/base/bull visible** — and the implied prices are **reconciled to land inside the locked `../memo-v1.md` ranges** (bear $200–230 / base $300–340 / bull $400+).

Why **not** an owner-earnings DCF: combined-entity FCF is not cleanly reported post-Calpine (the +64% Q1'26 revenue is an acquisition artifact) and year-by-year hedge ratios are undisclosed, so a 10-yr cash-flow DCF would be false precision. The defensible anchor is **forward adjusted-operating-EPS × a terminal multiple**, bracketed by merchant peers (16–18x) and the franchise premium (24–30x), and cross-checked against Street targets ($300–390, median ~$370). The §45U PTC (~$25/MWh to 2032) floors the power-price downside, which is why the bear is a *multiple compression on an intact franchise* rather than an earnings collapse.

Optional CSVs (`historicals.csv`, `sensitivity.csv`) not built this pass — revisit once the Q1'26 10-Q gives clean combined-entity figures.
