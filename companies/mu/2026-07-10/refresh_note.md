# MU Refresh Note — as_of 2026-07-10

**Type**: LIGHT REFRESH of `../2026-06-22/` (not a rebuild)
**pipeline_version**: lean-6module-v1.1 · **weights_version**: none · **run_date**: 2026-07-10 · **status**: DECISION_DRAFT

---

## What changed

1. **Re-priced (freshness gate)**: $1,184.88 (2026-06-22) → **$979.30** (2026-07-10 last close ≤ as_of).
   - Yahoo chart daily close $979.30 + stockanalysis history $979.30 — **2 independent sources, agree to the penny**.
   - Path: post-Q3 pop to a **new ATH $1,255** (6/25 close $1,213.56), then a **memory-sector bear market** (SK Hynix cautious HBM4 outlook) dragged it down — 7/1 $1,032 → 7/10 **$979.30** → still falling after as_of (7/16 $853). **Net −17.3%.**
   - 52wk band: high reset to **$1,255** (post-earnings ATH), low **$103.38** (unchanged). Price **−22.0% off high**, +847% off low.
   - `verify_freshness.py` → **STATUS: PASS (exit 0)**. T1–T5 PASS; T2 low/high-hug PASS (mid-band, not hugging either extreme — INC-001 tripwire clear despite the parabola).

2. **Folded in Q3 FY2026 actuals** (reported 2026-06-24, AFTER the prior as_of — the prior card was locked 2 days before):
   - Revenue **$41.46B** (+24% vs $33.5B guide; +74% QoQ; +346% YoY); non-GAAP GM **84.9%**; non-GAAP EPS **$25.11** / GAAP **$24.67**; OCF **$25.39B**, adj FCF **$18.3B**, capex **$7.1B**; DRAM **$31.3B** (76%).
   - **Q4 FY26 guide: rev $50.0B / GM ~86% / EPS $31.00 — a beat-and-RAISE.** 16 multi-year SCAs; HBM4 shipping in high volume.
   - **This is the OPPOSITE of the prior card's watched "Q3 top signal" (kill #7).** No kill criterion fired.

3. **Applied the capital-cycle lens** (`capital_cycle` block on the card): late/peak, PEAK caution — record-and-rising 85%+ margins, capex building into the peak, first external cracks (SK Hynix, peers −20%+). Supply response/glut not yet confirmed in MU's own numbers.

4. **Carried forward unchanged** (price-irrelevant / structural): business model, moat/bottleneck/value-chain maps, operator underwriting, inversion map, the normalized-EPS framework, competitive/HBM structure. Normalized bands ($165/$440/$950) carried, with a qualitative upward bias toward base+ from the SCA durability evidence (not chased into the numbers).

## What did NOT change — the verdict

**new_money WATCH (0%) / existing HOLD**, binding_constraint = **PRICE / cycle-position (no margin of safety on normalized economics)**, buy_below ~$650, max size ~12%.

## Does the −17% drop flip the verdict? — NO

| | Prior (2026-06-22, $1,184.88) | Now (2026-07-10, $979.30) |
|---|---|---|
| vs base fair (~$440) | ~2.7× base fair (+169%) | **~2.23× base fair (+123%)** |
| vs bull fair (~$950) | **+25% ABOVE bull** | **~+3% (roughly AT bull)** |
| Honest 5y IRR (bull / base / bear) | negative | **~0% / −15% / −30%** |
| vs avg analyst target | +23% above (~$965) | ~25–33% BELOW (~$1,300, raised) |
| New money / Existing | WATCH / HOLD (lean TRIM) | **WATCH / HOLD (lean TRIM softened)** |

The drop moved price **from ABOVE the honest bull fair value to roughly AT it** — a genuine improvement in the MOS picture — but it is **insufficient** to create a margin of safety: still ~2.23× base-normalized fair value with ~0% return even in the honest bull case, and the first sector cracks now visible on record 85%+ peak-cycle margins. The one-directional capital-cycle PEAK caution caps the verdict at WATCH/TRIM and prevents the dip from reading as a buy.

## The honest tension (runner_dissent, condensed)

MU fell −17% on a **blowout beat-and-raise** — a peak-MULTIPLE de-rating / sector-sentiment event, not a thesis break. This partly **vindicates** the prior WATCH (the peak multiple compressed exactly as feared → value off normalized, not run-rate). But a momentum reader now sees a stock −22% off its high, printing accelerating records, consensus target ~$1,300, slower-shipping competitors — and calls it a fat pitch. If HBM durability proves structural through the next down-leg (the 16 SCAs are real evidence), this WATCH will look too cautious and $979 a decent cyclical entry — that is the honest residual risk. The framework overrides because the bull case annualizes peak 85%+ margins the industry has never sustained through a cycle. Existing-holder lean-to-TRIM **softened**: ~17% of the de-rating already happened and fundamentals improved, so a disciplined trim near record margins is still defensible but far less urgent than at $1,185.

## Honesty label

DECISION_DRAFT, not COMPLETE. LIVE data (price) passed the mechanical ≥2-source freshness gate. Blocking evidentiary OPEN: **Q3 FY26 line items are currently 2-source aggregator [stocktitan + cnbc], pending direct SEC-8-K re-fetch** (magnitude well-corroborated). Forward OPENs persist: through-cycle margin durability, HBM4 share, true normalized EPS, top-vs-mid-cycle-scare.
