# SYK Valuation (M6)

Last updated: 2026-07-05 | as_of: 2026-07-05 | as_of_price: **$326.54**
See `model/scenario_model.csv` for full IRR computations.

---

## Current Setup

| Item | Value | Source |
|---|---|---|
| Share price (2026-07-02 close) | **$326.54** | YAHOO-SYK-PRICE / SYK-SA-STATS (2 independent sources, exact match) |
| Shares outstanding | **383.36M** | SYK-SA-STATS |
| Market cap | **~$125.18B** | derived: 383.36M × $326.54 = $125,182M (matches frozen input to <0.01% delta) |
| Net debt (Q1 2026, most current) | **~$11.85B** | derived: total debt $14.72B − cash $2.88B |
| Enterprise value | **~$137.03B** | derived |
| 52-wk range | **$281.00 (2026-05-11) – $404.87 (2025-07-23)** | YAHOO-SYK-PRICE / SYK-SA-STATS |
| Position in range | **−19.4% off high, +16.2% above low** — mid-range, comfortably outside either hug band | derived |

**Recovery-arc check (distinct from both the GEV/MSFT high-hug and the GEHC low-hug tripwire patterns)**: The 52wk high ($404.87) was set 2025-07-23 — BEFORE the March 2026 cyber incident. The 52wk low ($281.00) was set 2026-05-11 — DURING/shortly after the cyber-incident trough and Q1 miss. The current price ($326.54) sits +16.2% above that low, reflecting a partial market re-rating as the disruption resolved and guidance was maintained. This is a genuinely different shape than GEHC's "low justified by ongoing deterioration" pattern — here, the low is dated to a PAST, discrete, already-resolved event (operations restored by early April 2026, facts.md E21), and the current price reflects a MID-RECOVERY position, not a still-deteriorating one. Independently re-verified: $326.54 confirmed against 2 sources, both dated to the 2026-07-02 close.

---

## Why Trailing Multiples Require Care Here (Unlike a Clean Trailing-P/E Read)

Trailing P/E (37.79x, facts.md E5) is materially elevated relative to forward P/E (20.86x) — a ~45% gap, reflecting the fact that trailing GAAP EPS is depressed by the Q1 2026 miss (adjusted EPS −8.5% YoY on the cyber incident) flowing through the trailing-twelve-month window, while forward P/E is based on FY2026 guided adjusted EPS ($14.90-15.10, midpoint $15.00) which explicitly assumes H2 2026 recapture of the disruption. **This is the key valuation-methodology decision point in this dossier**: trailing multiples currently OVERSTATE how expensive the stock is (because they're weighed down by a one-off, well-explained disruption quarter), while forward multiples are the more decision-relevant lens, PROVIDED the H2 2026 recapture assumption embedded in guidance actually holds (facts.md O6).

| Metric | Value | Read |
|---|---|---|
| Trailing P/E (TTM) | **37.79x** | Distorted upward by the Q1 2026 cyber-incident-driven EPS miss flowing through the trailing window — NOT the right lens for steady-state valuation right now |
| Forward P/E (FY2026E) | **20.86x** (screener) | Based on guided adjusted EPS $14.90-15.10; the more decision-relevant multiple, contingent on H2 2026 guidance holding |
| Sanity check: fwd P/E × guided EPS midpoint | 20.86 × $15.00 = **$312.90** | Reasonably close to current price ($326.54, ~4.2% above this derived value) — broadly consistent, not internally contradictory |

---

## Clean Forward Multiple Analysis

**FY2025 adj operating income**: $25,116M × 26.3% = **$6,606M**. D&A is NOT separately disclosed in any source reviewed this run (OPEN item, facts.md O9-adjacent) — estimated at ~4.5% of revenue (a reasoned approximation given capex ran 3.03% of revenue and a heavy-M&A medtech typically shows somewhat higher D&A than capex due to acquired-intangible amortization, NOT a SYK-confirmed figure) giving **est. adj EBITDA ~$7.74B**.

| Metric | Calc | Multiple |
|---|---|---|
| Current EV / FY2025 adj EBITDA (est.) | $137.03B / $7.74B | **~17.7x** |
| Current EV / FY2026E adj EBITDA (est., guide-consistent growth) | ~$137B / ~$8.4B | **~16.3x** |
| Forward P/E (screener, FY2026E) | — | **20.86x** |
| Medtronic (MDT), peer | — | **13.67x fwd P/E** |
| Zimmer Biomet (ZBH), peer | — | **10.98x fwd P/E** |
| Intuitive Surgical (ISRG), peer | — | **45.96x fwd P/E** |

**SYK vs peers**: SYK's 20.86x forward P/E sits at a **~53% premium to MDT (13.67x)** and a **~90% premium to ZBH (10.98x)**, but at a **~55% discount to ISRG (45.96x)**. This is a coherent, explainable comp position, not an anomaly: SYK's organic growth (10.3% FY2025) is structurally faster than the more mature MDT/ZBH profiles, justifying a real premium; ISRG's discount reflects ISRG's higher structural growth ceiling (soft-tissue TAM still expanding, no comparable large-scale hardware competitor, higher recurring-instrument-revenue-per-procedure model) which SYK does not currently match. **This rules out a simple "SYK is expensive vs its closest ortho peers" argument** (it is, but for a growth-differentiated reason) and also rules out a simple "SYK is cheap vs the broader medtech-robotics category" argument (it is, relative to ISRG, but ISRG is not a clean like-for-like comp given the non-overlapping soft-tissue vs orthopedic focus, facts.md E38).

**Conclusion**: Unlike GEHC (which traded at a premium to its closest peer despite sitting near its 52-week low — a "not cheap despite looking cheap" trap), SYK's premium to MDT/ZBH is well-explained by a genuine, disclosed growth differential, and the stock's mid-range price position reflects a partially-priced-in recovery from a real, dated, resolving disruption — closer to "fairly priced for a strong compounder currently absorbing one confirmed disruption" than either "cheap" or "priced for perfection."

---

## Three-Scenario IRR Analysis

Methodology: EBITDA-multiple exit approach (3-year and 5-year horizons), consistent with the GEV/GEHC exemplar methodology. Full detail in `model/scenario_model.csv`.

### Bear Case: Cyber Recapture Fails + China Robotics Erosion Materializes + Tariffs Prove Structural

| Item | Assumption |
|---|---|
| Revenue CAGR | +3.0-3.5%/yr (organic growth stays well below the 8-9.5% FY2026 guide; the $375M cyber-incident deferral is NOT recaptured; China domestic robotics erode Stryker's China position the way United Imaging eroded GEHC's) |
| Exit adj EBITDA margin (Yr5) | 28.0% (further compression from the current ~30.8% estimated base, tariffs prove structural not transient) |
| Exit multiple | 12.0-12.5x (de-rates toward the MDT/ZBH peer range, reflecting a "growth story disrupted, moat under real pressure" market re-rating) |
| Net debt Yr5 | $13.0B (limited deleveraging without matching EBITDA growth) |
| **3-yr IRR** | **−14.0%** |
| **5-yr IRR** | **−5.0%** |

### Base Case: FY2026 Guidance Achieved, Cyber Incident Recaptured, No Further Disruption

| Item | Assumption |
|---|---|
| Revenue CAGR | +8.5%/yr (in line with the FY2026 organic guide midpoint of 8.0-9.5%, sustained) |
| Exit adj EBITDA margin (Yr5) | 32.5% (modest expansion from the current ~30.8% estimated base as the disruption fades and Mako procedure-volume operating leverage continues) |
| Exit multiple | 17.5-18.0x (holds near the current ~17.7x level) |
| Net debt Yr5 | $6.0-10.0B (real deleveraging as strong OCF/NI conversion continues, facts.md financial_quality.md) |
| **3-yr IRR** | **+11.1%** |
| **5-yr IRR** | **+12.5%** |

### Bull Case: Implant Pull-Through Confirmed, Mako Platform Expansion Succeeds, China Position Holds

| Item | Assumption |
|---|---|
| Revenue CAGR | +10.5-11%/yr (implant pull-through thesis confirmed and monetized; Mako Shoulder/Spine launches succeed in expanding the addressable procedure base; China robotics position holds share — the United-Imaging-style erosion risk does NOT materialize for Stryker) |
| Exit adj EBITDA margin (Yr5) | 34.5% (meaningful expansion as Mako-driven mix-shift and operating leverage compound) |
| Exit multiple | 20.0-21.5x (re-rates toward, but still meaningfully below, ISRG's 45.96x — reflecting proven multi-indication robotics economics without assuming SYK closes the full structural-growth gap to ISRG) |
| Net debt Yr5 | $2.0-8.0B (strong deleveraging) |
| **3-yr IRR** | **+21.6%** |
| **5-yr IRR** | **+21.1%** |

---

## IRR Table Summary

| Scenario | 3-yr IRR | 5-yr IRR | vs 8% hurdle |
|---|---|---|---|
| Bear | −14.0% | −5.0% | FAIL |
| Base | +11.1% | +12.5% | **PASS** |
| Bull | +21.6% | +21.1% | **PASS** |

**Read**: This is a materially different, more favorable shape than BOTH the GEV exemplar (all 3 scenarios fail at 3yr, only bull passes at 5yr) AND the GEHC dossier (bear/base fail at both horizons, only bull clears the hurdle). **Here, the BASE CASE ALREADY CLEARS THE 8% HURDLE at the CURRENT PRICE, at both the 3-year (+11.1%) and 5-year (+12.5%) horizons, with real (not razor-thin) margin.** Only the bear case — which requires a genuine failure of the cyber-incident recapture AND a materialized China robotics erosion AND structural (not transient) tariff pressure, i.e., multiple simultaneous adverse events — fails the hurdle. **The investment decision at the current price does NOT require betting on the bull-case catalysts (confirmed implant pull-through, a successful Shoulder launch, defended China share) — it only requires the base case (guidance achieved, cyber incident genuinely a one-off) to hold, which is a lower bar to clear than either exemplar's base case.**

---

## Buy-Below Analysis

| Target | Target IRR (base case, 5yr) | Approx price | vs $326.54 | Rationale |
|---|---|---|---|---|
| **No-chase ceiling** (above this, base case no longer clears the 8% hurdle at 5yr) | 8% | **~$401** | +22.8% | Near the 52wk high ($404.87) — a sensible, intuitive ceiling: paying near the all-time-high level would require the bull case, not just the base case, to work |
| **STARTER (current price already qualifies)** | ~10% | **~$366** or below | current price ($326.54) is BELOW this level | The current price already clears a 10%-IRR base-case bar with room to spare — this is a genuinely different setup than GEHC, where a STARTER entry required waiting for a lower price |
| **CORE entry (full margin of safety)** | ~12% | **~$334** | −2.3% (essentially at current price) | The current price ($326.54) sits just below the level needed for a full 12%-IRR base-case cushion — meaning today's price is ALREADY close to a genuine CORE-quality entry, not merely a STARTER-quality one |
| Deep value / max conviction | Bear-case breakeven | **~$206** (3yr bear breakeven) | −36.9% | Would require a severe, multi-factor deterioration (cyber recapture fails + China erosion + structural tariffs) to reach; not the base expectation |

**Binding constraint on price**: Unlike GEHC (where the current price offered NO margin of safety in the base case, forcing a "wait for a better price or wait for bull-case evidence" posture) and unlike the GEV exemplar (exceptional business, but price required near-perfection), **SYK's current price already sits close to a genuine base-case margin of safety** — the base case clears the 8% hurdle with real cushion at both 3yr (+11.1%) and 5yr (+12.5%) horizons, and the CORE-quality entry level (~$334, +12% IRR cushion) is barely above today's price. **This is a "the price already works if the base case holds" setup, not a "wait" setup** — the key remaining question is not primarily about price, but about EVIDENCE: specifically, whether the H2 2026 cyber-incident recapture materializes (facts.md O6) and whether China robotics competitive dynamics remain contained (facts.md O3) rather than replicating the United Imaging/GEHC erosion pattern. This is a genuinely different binding constraint than either exemplar — see decision_card and ic_panel for how this translates into a verdict.
