# TMO Valuation (M6)

Last updated: 2026-07-05 | as_of: 2026-07-05 | as_of_price: **$523.44**
See `model/scenario_model.csv` for full IRR computations.

---

## Current Setup

| Item | Value | Source |
|---|---|---|
| Share price (2026-07-02 close) | **$523.44** | Independent Yahoo re-fetch / TMO-SA-STATS (2 independent sources, exact match) |
| Shares outstanding | **371.62M** | TMO-SA-STATS |
| Market cap | **~$194.52B** | TMO-SA-STATS; derived: 371.62M × $523.44 ≈ $194.52B (consistent) |
| Net debt (Q1 2026, most current, post-Clario) | **~$39.9B** | derived: debt $43.2B − cash $3.3B |
| Enterprise value | **~$234.4B** | derived |
| 52-wk range | **$403.36 – $643.99** (screener) / $403.47 – $638.18 (independent Yahoo re-fetch) | TMO-SA-STATS / YAHOO-TMO-PRICE |
| Position in range | **−18.7% off high, +29.7% above low** — middle-to-upper-middle of range | derived |

**Low/high-hug check**: Price sits neither near its 52-week low nor its 52-week high — this is NOT a tripwire situation (T2 should pass cleanly on distance alone). The price has recovered meaningfully from its $403 low (a level likely touched during a Q1-2026-earnings-adjacent or earlier-2026 selloff, not independently dated this run) following the Q1 2026 beat-and-raise (revenue/EPS beat, guidance raised — facts.md E27-E28, E33-E34), but remains ~19% below its 52-week high. This is a materially different setup than the GEHC exemplar's justified-low-hug pattern — TMO's price action appears to be tracking a genuine, evidenced operating improvement (not a data-error concern in either direction).

---

## Why Trailing Multiples Require Some Care Here

TMO's GAAP and adjusted figures diverge more than GEHC's did: FY2025 GAAP operating margin was 17.38% vs. adjusted operating margin 22.7% [facts.md E12-E13] — a meaningful ~530bps gap, reflecting TMO's heavy amortization of acquired intangibles (given ~$65B of goodwill+intangibles on a ~$110B asset base, E26) and other GAAP-to-adjusted reconciling items not itemized in sources reviewed this run. This is a normal, expected feature of a decades-long serial acquirer (unlike GEV's one-off-gain distortion, this is a STRUCTURAL, recurring GAAP/adjusted gap, not a one-time item) — but it means **adjusted metrics (not GAAP) are the more meaningful basis for valuation and peer comparison** here, consistent with how sell-side and the company itself frame results.

| Metric | Value | Read |
|---|---|---|
| Trailing P/E (TTM, GAAP) | **28.77x** | Meaningfully higher than GEHC's 15.72x — reflects TMO's higher-quality, more-recurring (consumables/reagents/CRO-services-heavy) revenue mix and lower cyclicality |
| Forward P/E (FY2026E) | **20.63x** (screener) | Large gap vs. trailing (28.77x → 20.63x) driven by both earnings growth AND the GAAP/adjusted-EPS distinction |
| TTM revenue | $45.20B (+5.4%) | |
| TTM net income | $6.85B (+5.1%) | |
| TTM EPS | $18.19 (+6.7%) | |

---

## Clean Forward Multiple Analysis

**FY2025 adjusted operating income**: $10.11B (22.7% margin) [facts.md E13, E15]. D&A is NOT separately disclosed in any source reviewed this run (OPEN, facts.md O1/O4) — estimated at ~5.0% of revenue (a higher estimate than the GEHC exemplar's 3.5%, reflecting TMO's larger acquired-intangible-amortization base) giving **est. adj EBITDA ~$12.34B**.

| Metric | Calc | Multiple |
|---|---|---|
| Current EV / FY2025 adj EBITDA (est.) | $234.4B / $12.34B | **~19.0x** |
| Independently-sourced screener EV/EBITDA (cross-check) | — | **~18.0x-19.3x** (GuruFocus, YCharts — facts.md E55) |
| Danaher (closest disclosed peer) | — | **~18.8x EV/EBITDA** (facts.md E56) |
| TMO's own 5-year average EV/EBITDA | — | **~20.2x** (facts.md E55) |

**TMO vs. Danaher**: TMO trades at approximately **19.0x** (derived) vs. independently-sourced screener range 18.0-19.3x, essentially **IN LINE with Danaher's ~18.8x** — a materially different finding than GEHC's 19% PREMIUM to Siemens Healthineers. This cross-validation (derived multiple matching independently-sourced screener data within a tight band) is a useful internal-consistency check on this dossier's methodology. **TMO is also trading modestly BELOW its own 5-year historical average (~20.2x)** — a mild, not dramatic, discount-to-own-history signal (consistent with the GuruFocus "Modestly Undervalued" screener characterization, facts.md S2, though that characterization is not independently verified valuation work and should be weighted lightly).

**Conclusion**: TMO is **roughly fairly valued relative to its closest disclosed peer (Danaher) and modestly below its own historical average** — neither a statistically cheap bargain nor an obviously expensive setup. This is a genuinely different valuation conclusion than GEHC (traded at a premium to peer) and is closer to a "fair price, real business quality, some open questions" setup than either the GEV exemplar ("exceptional business, terrible price") or GEHC ("ambiguous business quality, fair-not-cheap price").

---

## Three-Scenario IRR Analysis

Methodology: EBITDA-multiple exit approach (5-year and 3-year horizons), consistent with the GEV/MSFT/GEHC exemplar methodology. Full detail in `model/scenario_model.csv`.

### Bear Case: China/Academic-Government Softness Structural + BIOSECURE Tailwind Fails to Materialize + Multiple De-Rates

| Item | Assumption |
|---|---|
| Revenue CAGR | +0.5%/yr (3yr) to +1.0%/yr (5yr) — Analytical Instruments softness spreads/proves structural; BIOSECURE/Clario underdelivers |
| Exit adj EBITDA margin (Yr3/Yr5) | 21.0% / 20.0% (compression from current 22.7% as growth stalls and fixed-cost leverage reverses) |
| Exit multiple | 15.0x / 14.5x (de-rates below Danaher peer, reflecting "growth story broken" market re-rating) |
| Net debt terminal | $47.0B / $44.0B (continued debt-funded M&A without matching EBITDA growth, partially offset by microbiology divestiture proceeds) |
| **3-yr IRR** | **−20.8%** |
| **5-yr IRR** | **−13.6%** |

### Base Case: FY2026 Guidance Roughly Achieved, Analytical Instruments Stabilizes, BIOSECURE Delivers as Guided

| Item | Assumption |
|---|---|
| Revenue CAGR | +4.5%/yr (consistent with FY2026 guided range $47.3-48.1B, i.e., +6-8% reported for FY2026 specifically, moderating toward organic-plus-modest-M&A pace thereafter) |
| Exit adj EBITDA margin (Yr3/Yr5) | 23.5% / 24.5% (modest improvement as Clario integration completes and mix shifts toward higher-margin CRO/bioproduction) |
| Exit multiple | 19.0x / 19.5x (holds near current level, in line with Danaher peer) |
| Net debt terminal | $33.0B / $26.0B (gradual deleveraging as FCF normalizes and microbiology divestiture proceeds are applied) |
| **3-yr IRR** | **+0.3%** |
| **5-yr IRR** | **+4.6%** |

### Bull Case: AI/Instrument Strategy Monetizes, BIOSECURE Tailwind Exceeds Guidance, Margin Expansion, Re-Rate

| Item | Assumption |
|---|---|
| Revenue CAGR | +7.5%/yr (AI-driven ASP/attach premium in Analytical Instruments materializes — currently unproven, facts.md O7; BIOSECURE/CRO reshoring accelerates beyond current guidance; bioproduction keeps compounding at 7%+) |
| Exit adj EBITDA margin (Yr3/Yr5) | 25.5% / 27.0% (margin expansion as AI/software mix improves profitability and Clario/BIOSECURE-driven CRO growth carries higher incremental margin) |
| Exit multiple | 21.5x / 22.5x (re-rates toward/above own 5yr historical average, reflecting proven AI differentiation + structural BIOSECURE tailwind) |
| Net debt terminal | $27.0B / $18.0B (strong FCF generation enables real deleveraging) |
| **3-yr IRR** | **+12.8%** |
| **5-yr IRR** | **+14.1%** |

---

## IRR Table Summary

| Scenario | 3-yr IRR | 5-yr IRR | vs 8% hurdle |
|---|---|---|---|
| Bear | −20.8% | −13.6% | FAIL |
| Base | +0.3% | +4.6% | FAIL |
| Bull | +12.8% | +14.1% | PASS (both horizons) |

**Read**: This is directionally SIMILAR in shape to the GEHC exemplar (bear/base fail, only bull passes), but with two notable differences: (1) TMO's bear case is materially LESS severe (−20.8%/−13.6% vs. GEHC's −29.5%/−15.5%), reflecting TMO's more diversified segment mix (three distinct recurring-revenue engines vs. GEHC's two) and currently-in-line (not premium) peer valuation; (2) TMO's base case at 5 years (+4.6%) is closer to — though still below — the 8% hurdle than GEHC's near-flat base case (−0.1%), reflecting TMO's more favorable starting valuation (in line with peer vs. GEHC's 19% premium) and more stable recent margin trajectory. **The investment decision still hinges on whether the bull-case catalysts (AI monetization, BIOSECURE tailwind exceeding guidance, Analytical Instruments reacceleration) are more likely than the bear-case continuation (China/academic softness proving structural, BIOSECURE underdelivering) — the base case alone does not clear the hurdle at either horizon, though it comes closer than the GEHC comparable.**

---

## Buy-Below Analysis

| Target | Target IRR (base case) | Approx price | vs $523.44 | Rationale |
|---|---|---|---|---|
| No-chase (above this, base case IRR turns more negative) | — | **~$560-580** | +7% to +11% | Base case already barely clears 0% at 3yr near current price; do not chase toward the 52wk high without a fundamentals upgrade |
| **STARTER entry (test position)** | ~8% base-case, 5yr | **~$440-450** | −16% to −17% (below 52wk low $403 is deeper still, but $440-450 is the level where base-case 5yr IRR crosses 8%) | At this level, the base case would clear the 8% hurdle at 5 years with a real (if modest) cushion |
| **CORE entry (real margin of safety)** | ~10-12% base case, 5yr | **~$375-405** | −23% to −28% (near/below the 52wk low) | Requires base case (not bull) to clear hurdle with genuine cushion; roughly coincides with the 52-week low ($403.36-403.47) |
| Deep value / max conviction | 15%+ even in a soft-bear scenario | **~$340-360** | −31% to −35% | Would require a further meaningful drawdown from the 52wk low; unlikely absent a much more severe deterioration (e.g., BIOSECURE reversal + Analytical Instruments structural decline confirmed simultaneously) |

**Binding constraint on price**: The current price ($523.44, middle of the 52-week range) does NOT offer a base-case margin of safety at either 3 or 5 years (0.3% and 4.6% respectively, both below the 8% hurdle) — but it is closer to clearing the hurdle than the GEHC comparable, and the required discount to reach an 8%-clearing STARTER zone (~$440-450, roughly −16% to −17% from current) is proportionally similar to (not dramatically worse than) typical starter-zone discounts seen in this pipeline's other dossiers. This is a "reasonably-priced, genuinely solid business, but still short of a margin-of-safety entry point" setup — closer to the MSFT exemplar's "great business, right price, just finish the research" pattern than to GEHC's "ambiguous business quality, fair-not-cheap price" pattern, but not fully there either, given the unresolved China-quantification and AI-monetization open items (facts.md O2, O7).
