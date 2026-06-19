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
| mu_2025-03-21 | MU | 2025-03-21 | Q2 FY25; memory down-leg + HBM/AI mix | cyclical_inflection (+ HBM bottleneck) | **built** (self-run; audit/score pending) |
| aapl_2016-05-12 | AAPL | 2016-05-12 | Q2 FY16: first revenue decline in 13y; "ex-growth?" fear | quality_compounder mispriced as ex-growth | **materials — test-ready ✓** |
| intc_2024-08-02 | INTC | 2024-08-02 | Q2'24 crash: miss + ~15% layoffs + dividend suspended, −26% day | real turnaround-bottom vs falling knife | **built+scored** (WINNER +445%; **FAIL** — missed turnaround, size-dist 3) |
| dis_2021-11-11 | DIS | 2021-11-11 | Q4 FY21: Disney+ sub miss; linear TV decline | structural-decline trap behind a strong brand | **materials — test-ready ✓** |
| pfe_2022-02-08 | PFE | 2022-02-08 | Q4'21: COVID windfall, optically low P/E | false-cheap (peak-earnings) value trap | **materials — test-ready ✓** |
| pypl_2021-07-29 | PYPL | 2021-07-29 | near ATH; eBay migration; rising competition | expensive decelerating-growth de-rating trap | **materials — test-ready ✓** |
| meta_2022-11-10 | META | 2022-11-10 | Q3'22 (first rev decline) + ~11k layoffs / cost discipline | cost-panic washout vs broken ad + RL money pit | **materials — test-ready ✓** |
| amzn_2023-02-03 | AMZN | 2023-02-03 | Q4'22; AWS decel, retail losses, cost discipline | margin-trough winner vs impaired retail + slowing AWS | **materials — test-ready ✓** |
| nvda_2023-05-25 | NVDA | 2023-05-25 | Q1 FY24 ~$11B guide (vs ~$7.2B); generative-AI demand | exceptional_bottleneck vs priced-for-perfection | **materials — test-ready ✓** |
| intc_2021-04-23 | INTC | 2021-04-23 | Q1'21 + IDM 2.0; DCG −20%, GM off highs, capex ↑; near a high | value trap near top (contrast to intc_2024-08-02) | **built+scored** (TRAP; **PASS** — correctly avoided) |
| googl_2024-06-14 | GOOGL | 2024-06-14 | post Q1'24; first dividend + $70B buyback; AI-Overviews/DOJ overhang | founder-controlled quality_compounder | **built+scored** (WINNER; PASS · size-dist 1) |

## Balance check (the point of the set)

- **Winners:** SNDK, NBIS, AAPL-2016, INTC-2024, META-2022, AMZN-2023, NVDA-2023 (+ GOOGL legacy; MU-2025 self-run, outcome TBD).
- **Traps:** DIS, PFE, PYPL, INTC-2021.
- The hard discrimination test = **INTC-2024 (real bottom) vs PFE-2022 / PYPL-2021 (value traps)**, and the **INTC-2021 (trap, near top) vs INTC-2024 (winner, near bottom)** pair on the *same company* — all "looked beaten down / cheap," only some reversed. A pipeline that buys every dip catches the falling knives too.

## Workflow per case

```
materials (this round)  ->  blind Runner locks decision_card  ->  Lookahead Auditor (CLEAN/LEAK)  ->  Scorer writes outcome_score
```

## Notes

- **Sealed outcome labels (WINNER/TRAP) are intentionally NOT recorded in the case folders** — a future blind Runner reads its own case folder, which stays label-free. The winner/trap split above is the orchestrator's tracker; do not point a blind Runner at this index.
- Each `materials` pack must pass a look-ahead audit before (or at the start of) its blind test. The 4 batch-2 packs (META/AMZN/NVDA/INTC-2021) passed a **self-applied** checker (CLEAN / CLEAN-WITH-NOTES); an **independent** (separate-agent) look-ahead pass is still recommended before the blind Runner, plus per-case rows added to `LOOKAHEAD_CHECKER.md`'s forbidden registry (each pack's `material_audit.md` provides a derived row).
- `mu_2025-03-21` was a **single-agent self-run** (collect + decide in one pass), not the blind-collect → separate-Runner → separate-Scorer flow; treat its decision as illustrative and re-run cleanly if used for scoring.
- **Operator/founder dossiers (2026-06-17):** every materials pack now includes `operator_background.md` (formation-first life-arc + required dark-arc + durability-ceiling grade 1–5), per `../COMPANY_MATERIAL_TEMPLATE.md` + `../../companies/_operator_underwriting_template.md`. Team grades: **NVDA / AMZN / AAPL / GOOGL 4/5 · META / PFE / PYPL / INTC-2024 / INTC-2021 3/5 · DIS 2.5/5**. (Higher = founder/long-arc team that can raise the durability ceiling; lower = fracture / key-man / governance discount.)
- `companies/googl/` and `companies/nbis/` are **full-information** research folders — NOT backtests; do not feed them to a blind runner.
