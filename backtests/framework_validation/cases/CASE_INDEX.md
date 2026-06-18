# Backtest Case Index

Last updated: 2026-06-18

Master tracker for the framework-validation as-of backtest cases. Each case lives in `cases/<ticker>_<as_of>/` and follows `../COMPANY_MATERIAL_TEMPLATE.md` + `../PROTOCOL.md`.

## Status legend

- `built+scored` — full P1 case, decision locked, look-ahead audited, outcome scored.
- `built` — full P1 case, decision locked + audited; outcome score pending.
- `materials` — as-of-clean evidence pack collected (case_control + sources_used + raw_extracts + evidence_spine); **decision deferred to a future blind test run**.
- `legacy/partial` — old-format or stub only.
- `planned` — in the matrix, not started.

## Cases

| case_id | ticker | as-of | anchor | test it exercises | status |
|---|---|---|---|---|---|
| sndk_2025-06-16 | SNDK | 2025-06-16 | spin-off + NAND/AI-storage cycle | spin-off / cyclical inflection | **built+scored** |
| nbis_2026-01-01 | NBIS | 2026-01-01 | post-Q3'25; MSFT/Meta deals; ~2.5GW power | exceptional_bottleneck (winner) | **built** (outcome_score pending) |
| aapl_2016-05-12 | AAPL | 2016-05-12 | Q2 FY16: first revenue decline in 13y; "ex-growth?" fear | quality_compounder mispriced as ex-growth | **materials — test-ready ✓** |
| intc_2024-08-02 | INTC | 2024-08-02 | Q2'24 crash: miss + ~15% layoffs + dividend suspended, −26% day | real turnaround-bottom vs falling knife | **materials — test-ready ✓** |
| dis_2021-11-11 | DIS | 2021-11-11 | Q4 FY21: Disney+ sub miss; linear TV decline | structural-decline trap behind a strong brand | **materials — test-ready ✓** |
| pfe_2022-02-08 | PFE | 2022-02-08 | Q4'21: COVID windfall, optically low P/E | false-cheap (peak-earnings) value trap | **materials — test-ready ✓** |
| pypl_2021-07-29 | PYPL | 2021-07-29 | near ATH; eBay migration; rising competition | expensive decelerating-growth de-rating trap | **materials — test-ready ✓** |
| googl (asof_2024-06-16) | GOOGL | 2024-06-16 | post Q1'24 | quality_compounder | **legacy/partial** (old-format backtest + evidence_pack stub) |
| — | META | 2022-11-10 | Q3'22 + layoffs/cost discipline | turnaround / quality (winner) | planned |
| — | AMZN | 2023-02-03 | Q4'22; AWS decel, cost discipline | cyclical/quality (winner) | planned |
| — | NVDA | 2023-05-25 | Q1 FY24 guidance shock | exceptional_bottleneck (winner) | planned |
| — | INTC | 2021-04-23 | IDM 2.0 near a high | value trap near top | planned |

## Balance check (the point of the set)

- **Winners:** SNDK, NBIS, AAPL-2016, INTC-2024 (+ GOOGL, planned META/AMZN/NVDA).
- **Traps:** DIS, PFE, PYPL (+ planned INTC-2021).
- The hard discrimination test = **INTC-2024 (real bottom) vs PFE-2022 / PYPL-2021 (value traps)** — all "looked beaten down / cheap," only one reversed. A pipeline that buys every dip catches the falling knives too.

## Workflow per case

```
materials (this round)  ->  blind Runner locks decision_card  ->  Lookahead Auditor (CLEAN/LEAK)  ->  Scorer writes outcome_score
```

## Notes

- **Sealed outcome labels (WINNER/TRAP) are intentionally NOT recorded in this index or the case folders** — a future blind Runner may read these files, and must stay blind. Labels are held by the orchestrator/scorer only.
- Each `materials` pack must pass a look-ahead audit before (or at the start of) its blind test.
- `companies/googl/` and `companies/nbis/` are **full-information** research folders — NOT backtests; do not feed them to a blind runner.
