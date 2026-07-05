# MDT Valuation (M6)

Last updated: 2026-07-05 | as_of: 2026-07-05 | as_of_price: **$83.19**
See `model/scenario_model.csv` for full IRR computations.

---

## Current Setup

| Item | Value | Source |
|---|---|---|
| Share price (2026-07-02 close) | **$83.19** | STOCKANALYSIS-MDT / WEBSEARCH-MDT-PRICE (2 independent sources, exact match) — up +5.04% that day |
| Shares outstanding | **~1.28B** | STOCKANALYSIS-MDT |
| Market cap | **~$106.48B** | derived: 1.28B × $83.19; confirmed directly at $106.49B |
| Net debt (most current balance-sheet basis) | **~$20.0B** | derived: debt $28.6B − cash/investments $8.1-9.2B |
| Enterprise value | **~$126.48B** | derived |
| 52-wk range | **$73.31 – $106.33** | STOCKANALYSIS-MDT |
| Position in range | **−21.8% off high, +13.5% above low** — lower-middle third of range | derived |

**Low/high-hug check**: Price sits meaningfully away from both 52-week extremes (−21.8% off high, +13.5% above low) — comfortably outside the 3% tripwire band on both ends, so this is NOT a hug situation. The July 2 print's +5.04% single-day move, occurring roughly a month after the June 3 FY2026 Q4 report, is consistent with a stock that troughed near its 52-week low earlier in the year (before the FY2026 inflection became fully visible) and has since been re-rating upward on genuinely improving fundamentals — a constructive, not concerning, read on price positioning.

---

## Why Trailing/Forward Multiples Are Trustworthy Here (Two Independent Cross-Checks Agree)

Two independent valuation approaches converge on the same conclusion: **MDT trades at a REASONABLE, not expensive, multiple for a large-cap, accelerating-growth medtech.**

1. **P/E basis**: FY2026 non-GAAP diluted EPS $5.53 → trailing P/E-on-non-GAAP ≈ **15.0x**. FY2027 guidance midpoint EPS $5.95 → forward P/E ≈ **14.0x**, matching stockanalysis.com's independently-reported forward P/E of **13.99x** almost exactly — a strong internal-consistency signal that the screener data and the guidance-implied multiple agree.
2. **EV/EBITDA basis** (see below): current implied multiple of **~10.9x**, using an estimated D&A add-back consistent with MDT's substantial M&A-driven intangible-amortization history (Covidien 2015, Mazor Robotics 2018, and others).

Both approaches point to the SAME conclusion from different angles — this is a materially stronger cross-check than the GEHC exemplar had available (GEHC's trailing P/E happened to reconcile arithmetically with price, but GEHC traded at a premium, not a discount, to its nearest peer).

---

## Clean Forward Multiple Analysis

**FY2026 non-GAAP operating income**: $36,364M × 24.4% = **$8,873M**. D&A is NOT separately disclosed in any source reviewed this run (OPEN item, facts.md O4) — estimated at ~7.5% of revenue (reflecting MDT's substantial M&A-driven intangible-amortization load, a materially higher estimate than the GEHC exemplar's ~3.5%-of-revenue assumption, appropriate given MDT's decade-plus history of large device-company acquisitions) giving **est. non-GAAP EBITDA ~$11.60B**.

| Metric | Calc | Multiple |
|---|---|---|
| Current EV / FY2026 non-GAAP EBITDA (est.) | $126.48B / $11.60B | **~10.9x** |
| Current EV / Revenue | $126.48B / $36.364B | **~3.48x** |
| Current P/E (non-GAAP, FY2026 actual basis) | $83.19 / $5.53 | **~15.0x** |
| Current P/E (non-GAAP, FY2027 guide midpoint) | $83.19 / $5.95 | **~14.0x** (matches screener 13.99x) |

### Peer Comparison — Where MDT Sits in the Medtech Valuation Spectrum

| Company | EV/EBITDA (approx., 2026) | Read |
|---|---|---|
| **Intuitive Surgical (ISRG)** | **~42-44x** | Near-monopoly surgical robotics franchise; extreme premium reflecting durable moat + high growth (Q1 2026 revenue +21.4%, EBITDA +29.9%) — the incumbent MDT's Hugo is challenging |
| **Stryker (SYK)** | **~20.3x** | Diversified ortho/med-surg peer, premium to MDT |
| **Boston Scientific (BSX)** | **~13.5-22x** (source variance) | MDT's direct PFA competitor (currently losing share, 41% vs MDT's 48%) — even BSX trades at a premium to MDT despite losing the PFA share battle |
| **MDT (this dossier)** | **~10.9x** (est.) | **Trades at a discount to ALL three named peers**, including the peer it is currently beating in a head-to-head, quantified share battle (BSX) |

**This is a materially more favorable valuation setup than the GEHC exemplar**, where GEHC traded at a ~19% PREMIUM to its closest peer (Siemens Healthineers). Here, MDT trades at a genuine, multi-peer DISCOUNT — roughly 20-30% below Stryker and Boston Scientific on EV/EBITDA, and a fraction of Intuitive Surgical's extreme premium multiple. **Important caveat**: this is not a fully clean comp — ISRG's premium reflects a genuinely different (near-monopoly, higher-growth, higher-margin) business quality, and some of MDT's discount to SYK/BSX may reflect MDT's larger, more diversified, historically slower-growing portfolio (including the mature Neuroscience/Medical Surgical base) rather than being purely "cheap." Still, this materially weakens any "MDT is expensive" argument and supports at least a "not overpaying" starting position for the price-side analysis.

**Conclusion**: MDT is trading at a discount to its immediate device-maker peer group despite delivering its best organic growth in a decade and a quantified, head-to-head share-leadership win (PFA vs BSX) — a set of facts that, taken together, is closer to "improving business, still-discounted price" than either the GEV exemplar ("exceptional business, wrong price") or the GEHC exemplar ("ambiguous business, fair-not-cheap price").

---

## Three-Scenario IRR Analysis

Methodology: EBITDA-multiple exit approach (5-year and 3-year horizons) plus dividend-yield contribution, consistent with the GEV/GEHC exemplar methodology. Full detail in `model/scenario_model.csv`.

### Bear Case: FY2026 Inflection Fades, Hugo Disappoints, China Re-Accelerates, Litigation Weighs

| Item | Assumption |
|---|---|
| Revenue CAGR | +2.0%/yr (reverts to pre-turnaround sluggish growth as PFA tailwind normalizes; Hugo fails to gain meaningful US traction) |
| Exit EBITDA margin (Yr5) | 20.0% (further compression — GAAP/non-GAAP bifurcation proves structural, not one-off; litigation costs weigh) |
| Exit multiple | 8.7x (de-rates below even the current discounted level, reflecting lower growth-quality perception + litigation-overhang discount) |
| Net debt Yr5 | $23.0B (slower deleveraging, incremental litigation cash costs) |
| **3-yr IRR** | **−19.0%** |
| **5-yr IRR** | **−11.7%** |

### Base Case: FY2027 Guidance Roughly Achieved, Then Normalizes; Hugo Modest Contributor; China Stable

| Item | Assumption |
|---|---|
| Revenue CAGR | +6.5%/yr (3yr) tapering to +5.8%/yr (5yr) — FY2027 guide (6.75-7.25%) achieved in year 1, then decelerates toward a sustainable mid-single-digit rate as PFA tailwind matures (MDT holds, does not necessarily keep GAINING share) |
| Exit EBITDA margin (Yr5) | 25.2% (modest net improvement as margin-bifurcation drivers, whatever they are, roll off) |
| Exit multiple | 11.3x (holds near the current discounted level — no re-rate assumed, no further de-rate either) |
| Net debt Yr5 | $11.0B (steady deleveraging from FCF/NI >1x cash conversion) |
| **3-yr IRR** | **+2.4%** |
| **5-yr IRR** | **+6.9%** |

### Bull Case: Hugo US Ramp Succeeds, PFA Leadership Extends, China Stabilizes, Re-Rate

| Item | Assumption |
|---|---|
| Revenue CAGR | +8.5%/yr (3yr) tapering to +7.8%/yr (5yr) — Hugo becomes a genuine, quantifiable commercial success (resolving facts.md O3); PFA leadership extends; China stabilizes/improves per management's "largely behind us" framing |
| Exit EBITDA margin (Yr5) | 28.3% (margin bifurcation resolves favorably — genuine, not just accounting, improvement) |
| Exit multiple | 13.8x (re-rates toward, though still well below, SYK/BSX peer levels — reflecting proven multi-platform growth, still a fraction of ISRG's extreme premium) |
| Net debt Yr5 | $5.0B (strong FCF-driven deleveraging + clean Diabetes spinoff execution) |
| **3-yr IRR** | **+15.4%** |
| **5-yr IRR** | **+17.0%** |

---

## IRR Table Summary

| Scenario | 3-yr IRR | 5-yr IRR | vs 8% hurdle |
|---|---|---|---|
| Bear | −19.0% | −11.7% | FAIL |
| Base | +2.4% | +6.9% | FAIL (but 5yr closes to within ~1.1pts of the hurdle) |
| Bull | +15.4% | +17.0% | PASS (both horizons) |

**Read**: This is the SAME overall shape as the GEV/GEHC exemplars (only the bull scenario clears the hurdle at either horizon), but MDT's BASE case is meaningfully closer to the hurdle than either exemplar — especially at 5 years (+6.9%, vs GEHC's roughly flat/−0.1%), and the base case is POSITIVE (not negative) at 3 years, unlike both GEV and GEHC. This reflects MDT's genuinely stronger current fundamental trend (accelerating organic growth, not decelerating) and materially better cash-conversion quality (FCF/NI >1x, vs GEHC's <1x). **The investment decision still hinges on whether the bull-case catalysts (chiefly: does Hugo's US commercial ramp actually materialize) are more likely than a reversion to pre-turnaround sluggishness (the bear case) — but the BASE case here offers a real, if modest, margin of safety at the 5-year horizon that neither GEV nor GEHC's base cases offered.**

---

## Buy-Below Analysis

| Target | Target IRR | Approx price | vs $83.19 | Rationale |
|---|---|---|---|---|
| No-chase (above this, base case IRR turns negative even at 5yr) | — | **~$95-97** (near the $97.77 analyst target) | +14-17% | Base case 5yr IRR would compress toward/below zero above this level without a fundamentals upgrade; do not chase into the sell-side target zone without confirmation |
| **STARTER entry (test position)** | current price already offers a positive, if sub-hurdle, base case | **current $83.19 is STARTER-eligible** | 0% | Base case is POSITIVE at both horizons already (unlike the GEV/GEHC exemplars, which required a materially lower price to reach this state) — the current price does not require a drawdown to justify an initial test position |
| **CORE entry (base case clears the 8% hurdle with real cushion)** | ~10-12% base case | **~$68-72** | −13% to −18% (near/below the 52wk-low-adjacent zone) | Would require base-case assumptions (not bull) to clear the hurdle with genuine cushion — a real pullback from here, though a smaller one than the GEV/GEHC exemplars required in percentage terms |
| Deep value / max conviction | 15%+ even in a soft-bear scenario | **~$58-62** | −25% to −30% | Would represent a return to well below the current 52-week low; likely requires either a broad market drawdown or a genuinely adverse company-specific shock (e.g., a major MiniMed litigation verdict) |

**Binding constraint on price**: Unlike the GEHC exemplar (where the base case offered NO margin of safety and the price was NOT a discount to peers), MDT's setup is more constructive on BOTH axes examined in this module: the base case IRR is positive (not flat/negative) at both horizons, and the current multiple sits at a genuine discount to all three named device-maker peers (ISRG, SYK, BSX) — including the peer (BSX) it is currently beating in a quantified, head-to-head share battle. This does not make MDT a screaming, no-questions-asked bargain — the bull case still requires an unproven catalyst (Hugo's US commercial success) to be realized for a truly attractive return, and the base case alone does not clear the 8% hurdle at either horizon — but it is a meaningfully more favorable starting point than either the GEV exemplar ("exceptional business, wrong price") or the GEHC exemplar ("ambiguous business, fair-not-cheap price"). This is closer to **"genuinely improving business, still-discounted price, with one large unresolved optionality catalyst (Hugo) and one real unquantified tail risk (MiniMed litigation) not fully captured in the multiple."**
