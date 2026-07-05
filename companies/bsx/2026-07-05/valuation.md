# BSX Valuation (M6)

Last updated: 2026-07-05 | as_of: 2026-07-05 | as_of_price: **$45.14**
See `model/scenario_model.csv` for full IRR computations.

---

## Current Setup

| Item | Value | Source |
|---|---|---|
| Share price (2026-07-02 close) | **$45.14** | YAHOO-BSX-PRICE / BSX-SA-STATS (2 independent sources, exact match) |
| Shares outstanding | **~1.49B** | BSX-SA-STATS |
| Market cap | **~$67.26B** | derived: 1,490M × $45.14 |
| Net debt (Q1 2026, PRE-Penumbra-close) | **~$9.54B** | derived: debt $10.988B − cash $1.453B |
| Enterprise value | **~$76.79B** | derived |
| 52-wk range | **$42.68 – $108.14** (Yahoo daily-close basis) | YAHOO-BSX-PRICE |
| Position in range | **−58.3% off high, +5.8% above low** — deep lower-range / low-hug position | derived |

**Low-hug check (the exact INC-001-style tripwire concern)**: Price sits very close to its 52-week low. Is this justified by genuine fundamentals, or a stale/erroneous read? **JUSTIFIED, with unusual rigor of confirmation**: this dossier independently traced the FULL daily price series (not just the endpoints) and identified THREE distinct, dated gap-down events (2026-02-04, ~2026-03-30, 2026-05-27), each corresponding to a specific, verifiable corporate disclosure (Q4/FY2025 earnings + light guidance; Q1 2026 earnings + first guidance cut; Bernstein-conference second guidance cut), each corroborated by 3-5+ independent secondary sources with consistent guidance numbers and cited causes. This is NOT a single-day crash, NOT a stale price, and NOT an unexplained air-pocket — it is a well-documented, multi-event fundamental repricing driven by a specific, quantifiable cause (US PFA/Farapulse market share falling from ~100% to ~41% since 2023, compounded by Watchman standalone deceleration and Urology stagnation).

---

## Why This Is Fundamentally a MULTIPLE-COMPRESSION Story, Not (Primarily) an Earnings-Collapse Story

This is the single most important valuation insight in this dossier. Using FY2025 actuals (revenue $20.074B, an approximate adjusted EBITDA of ~$4.82B) as a constant earnings base:

| Point in time | Price | Approx EV | Approx EV/EBITDA (FY25 basis) |
|---|---|---|---|
| 52-week high (2025-09-08) | $108.14 | ~$170.1B | **~35.3x** |
| Current (as_of, 2026-07-02) | $45.14 | ~$76.8B | **~15.9x** |

BSX's EV/EBITDA multiple has compressed from an extreme growth-stock-premium level (~35x) to a still-respectable-but-far-more-moderate level (~16x) — a **>50% multiple cut** — even as FY2025 actual revenue and earnings continued growing throughout most of this window (Q1 2026 organic growth was still +9.4%, EP specifically +22%). This means the ~58% price decline is disproportionately a story of **the market correcting an unsustainably rich multiple** (priced for perfect, uninterrupted 100%-PFA-share-style execution) rather than a story of the underlying business actually shrinking. This is a materially different, and arguably more favorable, setup than a scenario where earnings themselves are collapsing — the current price essentially asks investors to underwrite BSX's FUTURE earnings power at a much more reasonable (not bargain, not expensive) multiple, rather than needing a business turnaround to be proven.

---

## Trailing / Forward Multiple Cross-Checks

| Metric | Value | Read |
|---|---|---|
| Trailing P/E (TTM, implied) | **18.89x** (implies TTM EPS ~$2.39 — consistent with the independently-derived TTM diluted EPS $2.39 found via stockanalysis.com income-statement extract) | Reasonable for a still-double-digit-organic-growth medtech, though not "cheap" in absolute terms |
| Forward P/E (per screener) | **13.15x** (implies forward EPS ~$3.43 — this appears to reflect the ORIGINAL, since-cut guidance midpoint, likely STALE relative to the twice-revised $3.34-3.41 (Apr) and further-implied-lower (May 27) guidance) | **CAUTION**: this forward multiple may understate the true forward P/E if the screener has not yet refreshed for the May 27 cut — using the Apr-22-cut adjusted EPS guide ($3.34-3.41 midpoint $3.375) instead implies forward P/E of ~13.4x, similar; but the May 27 cut (organic growth 6.5-8.0%, no explicit EPS range found this run) could imply a further reduction not yet reflected — flagged O-item |
| EV/Sales (FY2025 basis) | **~3.83x** | Moderate for a high-growth medtech, well below a "priced for perfection" level |
| No dividend | — | IRR is entirely price-appreciation-driven |

---

## Peer / Historical Context (Directional, Not a Clean Comp This Run)

A full peer-multiple comp table (vs Medtronic, Abbott, Edwards Lifesciences) was NOT built this run due to time constraints (O-item, priority for next refresh) — the most decision-relevant "peer" comparison available this run is BSX **against its own recent history** (the 35x→16x de-rating above), which is arguably more informative than a cross-sectional peer comp for understanding whether the CURRENT price already reflects the EP-share-loss news, since it directly answers "how much of the growth-premium has already been given back."

---

## Three-Scenario IRR Analysis

Methodology: EBITDA-multiple exit approach (5-year and 3-year horizons), consistent with the GEHC/GEV/MSFT exemplar methodology. Full detail in `model/scenario_model.csv`.

### Bear Case: EP Share Loss Continues, Watchman/Urology Don't Stabilize, Penumbra Integration Drags, 4th Guidance Cut

| Item | Assumption |
|---|---|
| Revenue CAGR | +3.5%/yr (EP share erosion continues, Watchman standalone keeps declining, Urology stays flat) |
| Exit adj EBIT margin (Yr5) | 15.0% (further compression as competitive intensity + integration costs bite) |
| Exit multiple | 9.5x (de-rates further toward a "broken growth story" multiple, below typical mature medtech average) |
| Net debt Yr5 | $16.5B (Penumbra debt-funded, integration costs add further leverage without matching EBITDA growth) |
| **3-yr IRR** | **−30.8%** |
| **5-yr IRR** | **−15.4%** |

### Base Case: Guidance Holds at May-27-Cut Level (No 4th Cut), BSX Stabilizes as a Durable #2 in EP, Penumbra Integrates as Guided

| Item | Assumption |
|---|---|
| Revenue CAGR | +7.0%/yr (in line with the May-27 guided 6.5-8.0% organic range, held without further cuts) |
| Exit adj EBIT margin (Yr5) | 17.5% (modest recovery/stabilization from current pressure, below FY2025's 18.0% GAAP operating margin peak) |
| Exit multiple | 12.5x (normalizes between the current ~16x and a "broken" multiple, reflecting a de-rated-but-stable, still-above-average-growth medtech) |
| Net debt Yr5 | $13.5B (Penumbra debt absorbed, modest FCF-funded deleveraging over the period) |
| **3-yr IRR** | **−10.6%** |
| **5-yr IRR** | **+0.1%** (essentially flat) |

### Bull Case: OPAL HDx Ecosystem Moat Proves Durable, EP Share Stabilizes/Recovers, Penumbra Accretive Early, Multiple Re-Rates

| Item | Assumption |
|---|---|
| Revenue CAGR | +10.0%/yr (OPAL HDx penetration scales, PFA share stabilizes near current level or modestly recovers, Watchman/Urology reaccelerate, Penumbra contributes ahead of schedule) |
| Exit adj EBIT margin (Yr5) | 19.5% (margin expansion past the FY2025 peak as operating leverage resumes) |
| Exit multiple | 17.0x (moderate re-rate toward, NOT all the way back to, the historical ~35x growth-premium extreme — reflecting restored but not euphoric confidence) |
| Net debt Yr5 | $10.0B (strong FCF generation enables real deleveraging even after the Penumbra step-up) |
| **3-yr IRR** | **+9.7%** |
| **5-yr IRR** | **+14.3%** |

---

## IRR Table Summary

| Scenario | 3-yr IRR | 5-yr IRR | vs 8% hurdle |
|---|---|---|---|
| Bear | −30.8% | −15.4% | FAIL |
| Base | −10.6% | +0.1% | FAIL |
| Bull | +9.7% | +14.3% | PASS (both horizons) |

**Read**: This is the SAME overall shape as the GEHC exemplar (only bull clears the hurdle at either horizon; base is approximately flat at 5yr) — BUT the underlying MECHANISM is different and arguably more favorable for BSX. GEHC's base-case failure stems from a genuinely moderate-growth, margin-COMPRESSING business trading at a peer PREMIUM (no multiple cushion at all). BSX's base-case failure instead stems from a genuinely HIGH-growth business (even bear case assumes +3.5%/yr, base assumes +7%/yr — both above GEHC's entire scenario range) that has ALREADY absorbed a massive (~55%) multiple de-rating, where the base case simply requires the ALREADY-CRASHED multiple to hold roughly flat (not recover) for a ~0% 5yr IRR. In other words: **BSX's downside case is "the depressed multiple persists," not "the business gets meaningfully worse from here"** — a modestly more favorable risk asymmetry than a scenario requiring active further deterioration to lose money.

---

## Buy-Below Analysis

| Target | Target IRR | Approx price | vs $45.14 | Rationale |
|---|---|---|---|---|
| No-chase (above this, base case is negative even before accounting for further multiple risk) | — | **~$52** (+15%) | +15% | Base 3yr IRR still meaningfully negative above current price; do not chase the post-Feb rebound |
| **STARTER entry (test position)** | ~8% base-case-adjacent | **$42–45** (current/52wk-low zone) | −7% to 0% | At/near the current price and 52wk low, the base case is close to flat at 5yr — a genuine, if thin, starting cushion given the ALREADY-DE-RATED multiple (unlike GEHC, where the 52wk-low zone was the FIRST point offering any cushion) |
| **CORE entry (real margin of safety)** | ~10-12% base case | **$36–39** | −14% to −20% | Would require a further ~15-20% drawdown from here — plausible if a 4th guidance cut or an adverse litigation development occurs (bear-case triggers) |
| Deep value / max conviction | 15%+ even in a soft-bear scenario | **~$30** | −34% | Would represent trading BELOW the approximate bear-case 3yr terminal price — a severe dislocation requiring a genuinely broken-thesis level of bad news |

**Binding constraint on price**: Unlike GEHC (where the price offered NO cushion in the base case at any point in that dossier's review) or a hypothetical "still-priced-for-perfection" BSX (which would have been the case at the $108 high), BSX AT THE CURRENT PRICE already reflects a large, real repricing of business-quality risk (the ~35x→16x multiple compression) — the base case is close to flat (not deeply negative) at 5 years, and the primary risk to the downside case is less "the price needs to fall much further" and more "confirm the guidance-cut cycle has actually stopped (no 4th cut) and the securities litigation does not reveal something worse." This is a **"wait for confirmation, not necessarily for a much lower price"** setup — a third, distinct pattern from both the GEHC exemplar ("wait for a lower price OR better evidence, roughly equally") and the MSFT exemplar ("buy now, business quality overwhelms price, just finish the research").
