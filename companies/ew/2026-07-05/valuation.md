# EW Valuation (M6)

Last updated: 2026-07-05 | as_of: 2026-07-05 | as_of_price: **$94.37**
See `model/scenario_model.csv` for full IRR computations.

---

## Current Setup

| Item | Value | Source |
|---|---|---|
| Share price (2026-07-02 close) | **$94.37** | YAHOO-EW-PRICE (independent script re-fetch) / STOCKANALYSIS-EW (2 independent sources, exact match) |
| Shares outstanding | **575.80M** | STOCKANALYSIS-EW |
| Market cap | **~$54.34B** | derived: 575.80M × $94.37 (ties exactly to stockanalysis.com's own reported $54.34B) |
| Net cash (Q1 2026 basis) | **~$3.36B** (cash $2.4455B + investments $1.5116B − LT debt $0.5985B) | derived |
| Enterprise value | **~$50.98B** | derived: mkt cap − net cash |
| 52-wk range | **$72.30–$94.47** (stockanalysis) / **$72.65–$94.37** (Yahoo, independent re-fetch) | STOCKANALYSIS-EW / YAHOO-EW-PRICE |
| Position in range | **AT or within ~0.1-0.3% of the 52-week HIGH** — a high-hug situation | derived |

**High-hug check (the exact NVDA-incident-style tripwire, T2)**: Price sits essentially AT its own 52-week high. Is this a stale/erroneous read, or justified by genuine fundamentals? **JUSTIFIED, but with essentially zero margin of safety by construction**: Q1 2026 revenue growth ACCELERATED to +16.7% YoY (vs FY2025's own +11.5%), TWO consecutive quarterly guidance RAISES occurred (Q4 2025 report, then Q1 2026 report), TMTT is compounding at 35-56%, and Q1 2026 adjusted EPS beat consensus (facts.md I1). This is a genuine momentum-driven high, independently re-verified via 2 sources at the exact frozen as_of_price ($94.37, 0.0% delta) — not a data artifact. However, by definition, a justified high-hug means the price is NOT offering a margin of safety; it means the market has already substantially priced in the good news, which is the central valuation tension of this dossier.

---

## Why GAAP Trailing Multiples Are Misleading Here (Similar Issue to GEV, Opposite Direction from GEHC)

Unlike GEHC (where trailing multiples were roughly trustworthy) and more like GEV's exemplar caution (though in the OPPOSITE direction — GEV's GAAP was inflated by one-off GAINS; EW's GAAP is DEPRESSED by one-off COSTS), EW's trailing P/E of **51.14x** is NOT representative of underlying earnings power — it reflects FY2025 GAAP EPS of $1.81, which absorbed $325.4M of litigation expense + $146.9M of impairment (facts.md E16). The much more decision-relevant **forward P/E of 30.80x** uses the cleaner, guided-EPS basis ($2.95-$3.05 for FY2026).

| Metric | Value | Read |
|---|---|---|
| Trailing P/E (GAAP, TTM) | **51.14x** | Badly distorted by one-off litigation/impairment charges — NOT a useful valuation anchor |
| Forward P/E (FY2026E guided) | **30.80x** (screener) / **~31.0-32.0x** (derived: $94.37 / $2.95-3.05 midpoint $3.00) | Cross-checks closely — this is the more decision-relevant multiple |
| FY2025 adjusted diluted EPS | $2.56 | Trailing-adjusted P/E: $94.37/$2.56 ≈ **36.9x** |

**Even on the CLEAN, adjusted/forward basis, EW is not cheap** — 30-37x earnings is a substantial premium multiple, though one that is at least partially justified by the accelerating growth profile (Q1 2026 +16.7% YoY) and expanding-toward-guided margins, unlike a "premium multiple on decelerating growth" red flag.

---

## Clean Forward Multiple Analysis (EV/EBITDA Basis)

**FY2025 adjusted operating income**: $6.070B × 27.1% = **$1.645B**. D&A is NOT separately disclosed in any source reviewed this run (OPEN item, facts.md O5) — estimated at ~3.5% of revenue (same convention used in the GEHC exemplar, NOT EW-confirmed), giving **est. FY2025 adj EBITDA ~$1.857B**.

| Metric | Calc | Multiple |
|---|---|---|
| Current EV / FY2025 adj EBITDA (est.) | $50.98B / $1.857B | **~27.4x** |
| Current EV / FY2026E adj EBITDA (est., guidance midpoint: +10% rev, ~28.5% margin) | $50.98B / ~$2.137B | **~23.9x** |

**This is a genuine GROWTH multiple, not a value multiple.** For comparison, GEHC (same batch) trades at ~9.3-9.7x EV/EBITDA and Siemens Healthineers at ~7.9x — EW trades at **roughly 2.5-3x the EV/EBITDA multiple** of the hardware-heavy imaging peers reviewed elsewhere in this batch. This is not necessarily "wrong" — EW's growth rate (+16.7% Q1 2026), margin profile (27-29% vs GEHC's mid-teens), net-cash balance sheet, and deep clinical-evidence moat are all genuinely superior business-quality characteristics that justify SOME premium — but a ~3x multiple premium is a large gap to justify on quality alone, and it means the stock is pricing in a great deal of continued excellent execution with very little room for disappointment.

**No clean, EW-specific direct peer multiple was found this run** (Medtronic and Abbott are named competitors, facts.md E39, but this run did not pull their current EV/EBITDA multiples for a direct comp — flagged OPEN for next refresh; qualitatively, both are larger, more diversified med-tech conglomerates trading at more moderate multiples than a pure-play structural-heart grower like EW, similar to how GEHC compares to Siemens Healthineers).

---

## Three-Scenario IRR Analysis

Methodology: EBITDA-multiple exit approach (5-year and 3-year horizons), consistent with the GEHC/GEV/MSFT exemplar methodology. Full detail in `model/scenario_model.csv`.

### Bear Case: TAVR Decelerates + TMTT Undershoots + China Stays Sub-Scale + Litigation Recurs + Multiple De-Rates

| Item | Assumption |
|---|---|
| Revenue CAGR | +6.0%/yr (TAVR guideline/CMS-expansion thesis matures faster than hoped; TMTT undershoots guidance as Abbott holds share; China remains structurally sub-scale — inversion_map.md Kill Paths 1-3) |
| Exit adj EBITDA margin | 23.5% (Yr3) / 24.5% (Yr5) — the unexplained FY2025 litigation spike proves partially recurring, depressing margin ~4-5pts vs FY25's 27.1% adjusted level |
| Exit multiple | 19.0x (Yr3) / 18.0x (Yr5) — de-rates sharply from current 27.4x, reflecting a "growth story disappoints" re-rate, though still at a premium to hardware-peer multiples |
| Net cash Yr-end | $4.2B (Yr3) / $5.5B (Yr5) — still accumulates given minimal capex/debt needs, even in the bear case |
| **3-yr IRR** | **−8.7%** |
| **5-yr IRR** | **−3.1%** |

### Base Case: FY2026 Guidance Roughly Achieved, Margin Holds Near Guided Range, Multiple Compresses Modestly

| Item | Assumption |
|---|---|
| Revenue CAGR | +9.0-9.5%/yr (consistent with the raised 9-11% FY2026 guide, moderating slightly in later years as TAVR's core franchise matures) |
| Exit adj EBITDA margin | 28.0% (Yr3) / 28.5% (Yr5) — holds near the guided "high end of 28-29%" range |
| Exit multiple | 25.0x (Yr3) / 24.0x (Yr5) — MODEST compression from the current rich 27.4x toward a still-premium-but-less-extreme level, as growth normalizes from today's accelerating pace |
| Net cash Yr-end | $4.2B (Yr3) / $6.0B (Yr5) |
| **3-yr IRR** | **+7.2%** |
| **5-yr IRR** | **+7.4%** |

**This is a THIN, near-miss FAIL** — within ~0.6-0.8pt of the 8% hurdle at both horizons, a materially closer call than GEHC's flat-to-negative base case in the same batch. The base case here reflects genuinely strong operating performance (guidance achieved, margin holds) — the reason it still narrowly misses the hurdle is that even a MODEST multiple compression (27.4x → 24-25x, arguably a conservative/reasonable assumption for a stock currently priced at its own 52-week high) is enough to erase almost the entire return, because so little margin of safety exists in the entry price itself.

### Bull Case: TMTT/SAPIEN M3 Prove a Second Growth Engine, CMS NCD Expands TAVR, China Stabilizes, Margin Expands, Multiple Holds

| Item | Assumption |
|---|---|
| Revenue CAGR | +13.0-14.0%/yr (TMTT sustains high-30s/40s% growth for longer, TAVR gets a genuine CMS NCD-driven volume boost, China stabilizes/improves via continued evidence generation) |
| Exit adj EBITDA margin | 30.0% (Yr3) / 31.0% (Yr5) — margin expansion past the top of current guidance as scale and mix (TMTT growing into profitability) improve |
| Exit multiple | 28.0x (Yr3) / 27.0x (Yr5) — holds near/slightly above the current level, reflecting confirmed premium-compounder status |
| Net cash Yr-end | $4.2B (Yr3) / $6.5B (Yr5) |
| **3-yr IRR** | **+17.7%** |
| **5-yr IRR** | **+15.3%** |

---

## IRR Table Summary

| Scenario | 3-yr IRR | 5-yr IRR | vs 8% hurdle |
|---|---|---|---|
| Bear | −8.7% | −3.1% | FAIL |
| Base | +7.2% | +7.4% | **FAIL (thin, near-miss)** |
| Bull | +17.7% | +15.3% | PASS (both horizons) |

---

## Buy-Below / Starter-Zone Discipline

Solving the base-case (5yr) terminal-value bridge for the entry price that exactly clears the 8% hurdle: **~$91.87** — i.e., the CURRENT price ($94.37) is only about **2.7% above** the level at which the base case would exactly clear the hurdle with zero cushion. This is a remarkably thin gap (much thinner than GEHC's, where the base case was flat/negative even well below its own 52-week-low level) — it reflects a fundamentally STRONGER business (EW) priced at a level with almost no room for error, versus GEHC's more ambiguous business quality priced at a level that doesn't clear the hurdle even with a bigger fundamentals margin.

**For a REAL margin of safety** (targeting 10-12% base-case IRR, not just clearing 8%), the base-case-implied entry price falls to approximately **$77-84** — notably, this overlaps closely with the stock's own 52-week LOW ($72.30-$72.65). This is a clean, internally consistent signal: **EW's 52-week low is roughly where this dossier's own base-case discipline would recommend starting a position**, not an arbitrary technical level.

- **Buy-below (hurdle-clearing, thin margin)**: ~$91-92
- **Starter zone (real cushion, 10-12% base-case IRR)**: **$77-84** (approaches/at the 52-week low)
- **Do-not-chase zone**: Above ~$100 without a corresponding fundamentals upgrade (e.g., confirmed CMS NCD expansion, TMTT beating its already-raised guidance, or a clean explanation that fully resolves the litigation-expense-spike question) — pure multiple expansion from here would push the base case further into hurdle-failing territory.

---

## Comparison to GEHC (Same Batch)

| | GEHC | EW |
|---|---|---|
| Business quality | Good, not exceptional; margin compressing 3 consecutive periods; China -15% YoY confirmed | Strong and improving; margin expanding-to-guided; China structurally weak but not (yet) declining from an established base |
| Price position | Low-hug (-27% off high) — justified by real deterioration | **High-hug (at 52wk high)** — justified by real acceleration |
| Base case 5yr IRR | ~-0.1% (flat, fails) | **+7.4% (fails, but a thin near-miss)** |
| Binding constraint | COMPOUND — neither business nor price favors investor | **PRICE** — business quality is genuinely strong; price is the constraint |
| Balance sheet | Rising net debt (~$7.9B and climbing) | **Net cash (~$3.4B), fortress-like** |

EW is a structurally BETTER business than GEHC on nearly every dimension examined this run (growth direction, margin direction, balance sheet, moat depth/type) — but it is priced far more richly for that quality, producing a superficially similar "WATCH, base case fails the hurdle" verdict through an almost entirely different mechanism: GEHC fails because the business itself carries real unresolved doubts even at a fair-to-cheap price; EW fails (barely) because the business is executing very well but the price has already captured nearly all of that execution quality, leaving no cushion.
