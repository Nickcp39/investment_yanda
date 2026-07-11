# NVDA Refresh Note — as_of 2026-07-10

**Type**: LIGHT REFRESH of `../2026-06-20/` (not a rebuild) · **batch**: `ai_robotics_2026-07-10`
**pipeline_version**: lean-6module-v1.1 · **weights_version**: none · **run_date**: 2026-07-10 · **status**: DECISION_DRAFT

---

## What changed

1. **Re-priced (freshness gate)**: $210.69 (2026-06-20) → **$210.96** (2026-07-10 close, last ≤ as_of).
   - Yahoo chart re-fetch $210.96 + stockanalysis $210.96 (2 independent sources, agree to the penny).
   - Path: dipped to ~$192 (6/26), recovered to $210.96 (7/10). **Net +0.13% — essentially flat.**
   - 52wk band: high $236.54 (unchanged ATH), low **$161.61** (the old $142.03 low rolled OUT of the trailing 52-week window; stock now +30.5% off the low, −10.8% off high).
   - `verify_freshness.py` → **STATUS: PASS (exit 0)**. T1–T5 PASS; T6 two WARN (export-control 114d, guidance 51d old — carried, non-blocking; no newer authoritative event found this refresh).

2. **Added robotics lens** (`robotics_lens.md` + `robotics_thesis` block on the card) answering batch PLAN.md §1 (a–e).

3. **Carried forward unchanged** (FILED / price-irrelevant): Q1 FY27 + FY26 financials, business_model, moat/bottleneck/value-chain maps, inversion_map, owner-earnings bridge, raw SEC filings. FILED numbers were independently verified correct in the 06-20 run.

## What did NOT change — the verdict

**new_money WATCH (0%) / existing HOLD**, binding_constraint = **PRICE (no margin of safety)**. Because price is flat, the entire 06-20 valuation carries: base 5y IRR **+4.7% < 8% hurdle**, forward ~28x, −10.8% off ATH. The robotics lens does not add a buyable increment — it **reinforces** that NVDA at $210.96 is an AI-datacenter compute valuation call, not robotics alpha.

## Batch thesis — one-paragraph answer

NVDA is the real "demand-surged + hard bottleneck + already printing cash" leader **for AI-datacenter compute** (~92% of revenue), NOT for robotics. Robotics/embodied-AI is **<1% of revenue and undisclosed** — buried in the Automotive market platform (FY26 $2.35B ≈ 1.09%, itself mostly autonomous-vehicle DRIVE, not robots). The robotics business that exists is **dev-kit/module hardware (Jetson Thor/T4000, IGX Thor) + Isaac/GR00T/Cosmos platform + named ecosystem** — real dated *product* events, but the *revenue* is anticipation, not cash. Capital-cycle lens on the robotics segment: **partial/largely N/A, early/pre-inflection, high software barrier but no excess return yet → caution NONE** (it is an unmonetized option, not a top). Real bottleneck vs concept: a genuine platform/developer moat (CUDA + Isaac switching cost, falsifiable) but **still mostly concept/option at current scale**. Split: at $210.96 ~100% of the market cap is the AI-compute franchise; robotics is a near-free embedded call worth ~nil today. **Buying NVDA for robotics exposure is 99% buying AI compute — the wrong vehicle for pure robotics** (see TER/ON/NOVT in this batch).

## Honesty label
DECISION_DRAFT, not COMPLETE. LIVE data (price) passed the mechanical ≥2-source freshness gate. Blocking OPEN: custom-silicon quantitative DC-share erosion (O4). Robotics-specific OPEN: standalone robotics revenue undisclosed (O7), humanoid ramp magnitude/timing (O8). Prior OPENs (10-K line items O1, proxy O3, China H200 magnitude O5) persist.
