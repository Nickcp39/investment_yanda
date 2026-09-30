# NVDA Research Status — as_of 2026-07-28

**Honest status label: `DECISION_DRAFT`** (NOT COMPLETE). Completeness ~65% (carried from the 06-20 baseline; regime adds new open questions, does not close old ones).
**pipeline_version**: lean-6module-v1 · **weights_version**: none · **run_date**: 2026-07-28
**Run type**: focused refresh of `../2026-06-20/` — re-price at $197.01, re-run M4/M5/M6, overlay the 2026-07-28 regime, carry forward the durable M2/M3 business analysis after a quick re-check. NOT a from-scratch rebuild.

## Freshness gate (MECHANICAL, hard door)
- `python scripts/verify_freshness.py --dossier companies/nvda/2026-07-28` → **STATUS: PASS (exit 0)**.
- `freshness_check.json` committed. Independent Yahoo re-fetch = $197.00999 vs card $197.01 (0.0% delta). Price cross-checked across 2 independent sources (Yahoo chart API + stockanalysis, both $197.01).
- Tripwires: **T1–T6 all PASS**. T2 (the INC-001 tell) clean: +20.1% off 52wk low, −16.7% off 52wk high — not hugging an extreme. T3 market-cap identity 0.01%. T4 distance-from-high reconciles (−16.7% narrative vs −16.7% card-implied). T5 single-value-of-truth ($197.01 in all price-bearing files). T6 qualitative freshness now GREEN (export-control 13d, guidance/earnings-date 8d).

## What was refreshed this run
- **Price / valuation (M6)**: $210.69 → **$197.01** (−6.5%). Base 5y IRR +4.8% → **+6.2%** (still < 8% hurdle). `valuation.md`, `model/scenario_model.csv` rebuilt at $197.01.
- **Inversion (M5)**: `inversion_map.md` re-done with the full regime overlay (7/28 crash, capex audit, CXMT/memory, custom-silicon visibility, FOMC/Warsh, China H200 actually shipping). Kill criteria updated (K1 → Q2 8/26; K6 regime added).
- **M4 earnings check**: NVDA has **NOT** reported Q2 FY27 (scheduled **2026-08-26**, after as_of). Owner-earnings model carried forward unchanged. Only new M4 input = 25% USG cut on H200-to-China.
- **M2/M3 quick re-check**: no thesis-breaking event. CUDA + full-stack moat intact, ~87% merchant DC share, operator (Huang 4/5) unchanged. Custom-silicon threat more VISIBLE (monitor), not realized (no structural break).
- New files: `decision_card.json` + `.md`, `valuation.md`, `inversion_map.md`, `delta_vs_0619.md`, `freshness.json`, `freshness_check.json`, `research_status.md`, `model/scenario_model.csv`.

## Verdict (two axes, derived separately)
- **new_money: WATCH (0%)** — price still binds (base IRR +6.2% < 8%, +8.8% above the ~$181 buy-below); regime raises risk. Verdict ceiling by completeness = STARTER; price gate binds harder → WATCH.
- **existing_position: HOLD** — business unimpaired, no kill criterion fired; 7/28 is a repricing.
- **business: exceptional** (unchanged).

## Gates NOT passed / OPEN (cap completeness ~65%)
- **O4 (blocking)**: custom-silicon quantitative DC-share erosion — still not primary-sourced; regime makes it more urgent.
- **O7 (blocking until 2026-08-26)**: Q2 FY27 actuals not yet reported — the swing data point.
- O1 10-K line items, O3 proxy/operator detail, O5 China H200 magnitude + 25%-cut margin drag, O6 inventory/CoWoS/HBM commitment risk.
- This run did NOT rebuild the full 11-stage dossier (no fresh ic_panel/monitor/memo for 07-28); it is a decision-card refresh on the 06-20 baseline per the batch PLAN. Durable business modules (business_model, moat_map, operator_underwriting) reference the 06-20/06-19 versions.

## Wording discipline
Do NOT call this "complete / full research". It is a **decision draft** (P1 refresh) that passes the mechanical freshness gate and honestly caps its verdict at the completeness ceiling. Doubts are logged in `delta_vs_0619.md` and `runner_dissent`.
