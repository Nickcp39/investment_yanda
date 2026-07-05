# GEHC Valuation (M6)

Last updated: 2026-07-04 | as_of: 2026-07-04 | as_of_price: **$65.57**
See `model/scenario_model.csv` for full IRR computations.

---

## Current Setup

| Item | Value | Source |
|---|---|---|
| Share price (2026-07-02 close) | **$65.57** | YAHOO-GEHC-PRICE / GEHC-SA-STATS (2 independent sources, exact match) |
| Shares outstanding | **454.89M** | GEHC-SA-STATS |
| Market cap | **~$29.83B** | derived: 454.89M × $65.57 |
| Net debt (Q1 2026, most current) | **~$7.90B** | derived: debt $10.13-10.17B − cash $2.29B |
| Enterprise value | **~$37.73B** | derived |
| 52-wk range | **$58.75 – $89.77** | YAHOO-GEHC-PRICE / GEHC-SA-STATS |
| Position in range | **−27.0% off high, +11.6% above low** — lower third of range | derived |

**Low-hug check (inverse of the GEV/MSFT high-hug tripwire)**: Price sits near the LOW end of its 52-week range. Is this a stale/erroneous read, or justified by genuine fundamentals? **JUSTIFIED**: FY2026 guidance was cut after Q1 2026 (adj EBIT margin, adj EPS, FCF all reduced — facts.md E36), Q1 2026 net income fell YoY, orders decelerated sharply (+10.3%→+1.1% organic), and China revenue is confirmed down −15% YoY. The price decline tracks a real, multi-data-point deterioration, not a data artifact. This dossier independently re-verified the $65.57 price against 2 sources, both dated to the same 2026-07-02 close — not a stale or mis-keyed value.

---

## Why Trailing Multiples Are Roughly Trustworthy Here (Unlike the GEV Exemplar)

Unlike GEV (where trailing GAAP multiples were badly distorted by one-off gains — tax releases, M&A remeasurement — requiring heavy normalization), **GEHC's reported and adjusted figures are reasonably close to each other**, and the trailing P/E is internally consistent: TTM EPS $4.17 × trailing P/E 15.72x = $65.55, matching the actual price $65.57 almost exactly [facts.md E51-E52]. This is a useful sanity check that the screener data is coherent, not corrupted.

| Metric | Value | Read |
|---|---|---|
| Trailing P/E (TTM) | **15.72x** | Reasonable for a moderate-growth med-tech with margin currently under pressure |
| Forward P/E (FY2026E) | **13.15x** (screener) / **13.1-13.7x** (derived from guided EPS $4.80-5.00) | Cross-checks closely against screener — good consistency |
| TTM revenue | $20.98B (+6.0%) | |
| TTM net income | $1.91B (−12.6%) | Declining — reflects the Q1 2026 margin miss flowing through trailing figures |

---

## Clean Forward Multiple Analysis

**FY2025 adj EBIT**: $20,625M × 15.3% = **$3,156M**. D&A is NOT separately disclosed in any source reviewed this run (OPEN item O2) — estimated at ~3.5% of revenue (a general med-tech approximation, NOT GEHC-confirmed) giving **est. adj EBITDA ~$3.88B**.

| Metric | Calc | Multiple |
|---|---|---|
| Current EV / FY2025 adj EBITDA (est.) | $37.73B / $3.88B | **~9.7x** |
| Current EV / FY2026E adj EBITDA (est., guide midpoint) | $37.73B / ~$4.07B | **~9.3x** |
| Current EV / FY2026E adj EPS (P/E basis) | $65.57 / $4.90 (midpoint) | **~13.4x** |
| Siemens Healthineers (peer) | — | **~7.9x EV/EBITDA**, 1.6x EV/Revenue [MULTIPLES-VC-SIEMENS-HEALTHINEERS] |

**GEHC vs Siemens Healthineers**: GEHC trades at approximately a **19% PREMIUM** to Siemens Healthineers on EV/EBITDA (~9.3-9.7x vs 7.9x) — the OPPOSITE of a "cheap vs peer" setup. **Important caveat**: this is not a fully clean comp — Siemens Healthineers is a larger, more diversified business (includes Varian oncology and lab diagnostics alongside imaging, which is only 56% of its FY2025 sales per facts.md E44c), so some of the multiple gap may reflect genuine differences in growth mix (GEHC's PDx segment growing 9-22% organically vs a more mature diversified peer) rather than GEHC being "expensive." Still, this rules out a simple "GEHC trades cheap vs the obvious peer" argument as a stand-alone reason to buy.

**Conclusion**: GEHC is NOT statistically cheap on a peer-relative EV/EBITDA basis despite sitting near its 52-week low and having just cut guidance. The stock's discount to its own 52-week high reflects a genuine earnings reset that has already been partly absorbed into the current multiple — this is closer to "fairly priced given the reset" than "irrationally cheap," a materially different setup than the "exceptional business at the wrong price" (GEV) or "wrong price on a great business, correctable" (MSFT) exemplar patterns.

---

## Three-Scenario IRR Analysis

Methodology: EBITDA-multiple exit approach (5-year and 3-year horizons), consistent with the GEV/MSFT exemplar methodology. Full detail in `model/scenario_model.csv`.

### Bear Case: China Erosion Spreads + PCS Structural + Margin Keeps Compressing

| Item | Assumption |
|---|---|
| Revenue CAGR | +1.5%/yr (China erosion offsets US/Other growth; PCS keeps declining) |
| Exit adj EBITDA margin (Yr5) | 12.5% (further compression from current 13.5% Q1 print) |
| Exit multiple | 8.0x (de-rates below Siemens Healthineers peer, reflecting lower-quality growth perception) |
| Net debt Yr5 | $9.5B (continued debt-funded M&A without matching EBITDA growth) |
| **3-yr IRR** | **−29.5%** |
| **5-yr IRR** | **−15.5%** |

### Base Case: FY2026 Guidance Achieved, PCS Stabilizes, China Contained (Not Reversed)

| Item | Assumption |
|---|---|
| Revenue CAGR | +3.5%/yr (in line with FY2026 organic guide 3-4%) |
| Exit adj EBITDA margin (Yr5) | 16.0% (partial recovery toward FY2024's 16.3% peak as tariffs fade per guidance) |
| Exit multiple | 9.5x (holds near current level) |
| Net debt Yr5 | $8.0B (modest deleveraging as FCF stabilizes) |
| **3-yr IRR** | **−7.2%** |
| **5-yr IRR** | **−0.1%** (essentially flat) |

### Bull Case: AI Monetization Proven, PCS Turnaround, Margin Expansion, Re-Rate

| Item | Assumption |
|---|---|
| Revenue CAGR | +6.0%/yr (AI-driven ASP/attach premium materializes — currently unproven, facts.md O7; PDx keeps compounding; PCS turns around) |
| Exit adj EBITDA margin (Yr5) | 18.5% (margin expansion past FY24 peak, AI/software mix improving profitability) |
| Exit multiple | 11.5x (re-rates above current level and above Siemens Healthineers, reflecting proven differentiation and re-accelerating growth) |
| Net debt Yr5 | $5.5B (strong FCF generation enables real deleveraging) |
| **3-yr IRR** | **+12.0%** |
| **5-yr IRR** | **+12.7%** |

---

## IRR Table Summary

| Scenario | 3-yr IRR | 5-yr IRR | vs 8% hurdle |
|---|---|---|---|
| Bear | −29.5% | −15.5% | FAIL |
| Base | −7.2% | −0.1% | FAIL |
| Bull | +12.0% | +12.7% | PASS (both horizons) |

**Read**: This is a genuinely different shape than the GEV exemplar (all 3 scenarios fail at 3yr; only bull passes at 5yr) — here, the BASE case is roughly FLAT at 5 years (not deeply negative), meaning the current price is close to a "fair, no-margin-of-safety" level for the base case specifically, while bear is a real, meaningful downside and bull requires the AI/turnaround thesis to actually prove out. **The investment decision hinges entirely on whether you believe the bull-case catalysts (AI monetization, PCS turnaround, China stabilization) are more likely than the bear-case continuation (China spreading, PCS structural, margin never recovering) — the base case alone does not clear the hurdle and does not provide a margin of safety.**

---

## Buy-Below Analysis

| Target | Target IRR | Approx price | vs $65.57 | Rationale |
|---|---|---|---|---|
| No-chase (above this, negative EV even in base) | — | **~$72** (near current, modest premium) | +10% | Base case is already flat-to-negative above current price; do not average up |
| **STARTER entry (test position)** | ~8% base-case-adjacent | **~$55–58** | −13% to −16% (near/at 52wk low $58.75) | At the 52-week low, base case would clear or approach the 8% hurdle at 5yr; still requires bear-case not to materialize |
| **CORE entry (real margin of safety)** | ~10-12% base case | **~$48–50** | −24% to −27% | Requires base case (not bull) to clear hurdle with genuine cushion; would represent a further ~25% drawdown from here |
| Deep value / max conviction | 15%+ even in a soft-bear scenario | **~$40** | −39% | Near financial-crisis-level pricing for a company with this revenue base; unlikely absent a much more severe deterioration |

**Binding constraint on price**: The current price does NOT offer a margin of safety in the base case — it is close to base-case fair value, meaning the investment case currently depends on the BULL scenario (AI monetization + PCS turnaround + China stabilization) materializing, none of which are yet evidenced (all are OPEN items: O4 PCS root cause, O7 AI revenue attribution, and the China trend itself is still deteriorating as of the latest data, E44b). This is a "wait for a better price OR wait for bull-case evidence" setup, not a "buy now, business quality overwhelms price" setup (unlike MSFT) and not a "great business, price kills it" setup (unlike GEV) — it is closer to **"decent business, price roughly fair, thesis unproven."**
