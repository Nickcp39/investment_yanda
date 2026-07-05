# BFLY Financial Quality (M4)

Last updated: 2026-07-04 | as_of: 2026-07-04 | sources: facts.md, claim_ledger.csv

NORMALIZATION FOCUS: BFLY's GAAP net loss significantly OVERSTATES true cash deterioration (large non-cash addbacks + working-capital timing), while its GAAP gross margin was DEPRESSED by a genuine one-time inventory charge in FY2025. Both directions matter -- an investor reading only headline GAAP net loss would miss real recent improvement; an investor reading only Q1 2026 gross margin (68.9%) without the FY2025 context would miss that FY2025's 46.9% GAAP figure was a one-off, not a trend break.

---

## One-Off Distortion Registry

| One-Off | Amount | Period | Nature | Normalized Action |
|---|---|---|---|---|
| Excess & obsolete (E&O) inventory write-down | $17.4M | FY2025 (mostly, per E&O gross-margin reconciliation) | Technological advancements in underlying components + product-portfolio changes [E16] | Add back to gross profit for a clean margin read (46.9% GAAP -> 64.9% adjusted) |
| Sezonov indemnification litigation accrual | $3.0M (Q4'25) + $3.3M (Q1'26), partially offset by $6.0M insurance recovery (Q1'26) | FY2025 Q4 / FY2026 Q1 | Indemnification obligation tied to legacy SPAC-merger litigation, unrelated to core operations [E18, E30] | Company already excludes from its own "Other" opex characterization as non-representative; treat consistently in any owner-earnings view |
| Stock-based compensation | $23.4M (FY2025) / $5.5M (Q1 2026) | Ongoing | Non-cash but real economic dilution cost | Add back for cash-flow bridge (below), but do NOT ignore for per-share dilution purposes -- SBC is a genuine cost to existing holders even though it doesn't consume cash directly |
| Public share offering | $81.0M net (Jan 2025) | One-time financing event | Real cash inflow, but at a dilutive $3.15/share price (well below current $7.68) [E37] | Not an operating one-off; flagged for dilution-history purposes, not P&L normalization |
| Warrant fair-value changes | +$2.27M (FY2025) / +$0.41M (Q1 2026) | Ongoing (small, declining -- public warrants expired 2026-02-12 [E42]) | Non-cash mark-to-market on now-expired public warrants | Immaterial going forward since the warrants have expired; historical noise only |

---

## Normalized P&L Bridge

### FY2025 Normalization
| Item | GAAP | Adjustment | Normalized |
|---|---|---|---|
| Revenue | $97.61M | -- | $97.61M |
| Gross profit / margin | $45.73M / 46.9% | +$17.4M E&O write-down | **$63.13M / 64.9%** (company's own adjusted-gross-profit figure [E16]) |
| Loss from operations | -$86.42M | +$17.4M E&O (non-cash portion largely) | ~-$69.0M (approximate; company does not publish a fully reconciled adjusted operating loss) |
| Net loss | -$77.06M | -- | **-$77.06M GAAP is the headline, but see cash-flow bridge below for the more decision-relevant figure** |
| Adjusted EBITDA | -$26.53M | (company's own non-GAAP measure, already excludes SBC, E&O writedowns, warrant FV changes, litigation, D&A) | **-$26.53M** -- this is the cleanest single per-period profitability proxy BFLY itself provides [E21] |
| Net cash used in operating activities | -$12.70M | -- | **-$12.70M** -- the single most decision-relevant cash-quality number: dramatically better than the -$77.06M GAAP net loss [E38] |

**Key**: FY2025 Adjusted EBITDA -$26.5M and net cash used in operations -$12.7M are the two cleanest metrics. The -$77.1M GAAP net loss overstates cash deterioration by a wide margin because of $23.4M SBC + $17.6M inventory/vendor-advance writedowns (both non-cash) plus a $12.8M deferred-revenue working-capital tailwind [I2].

### Q1 2026 Normalization
| Item | GAAP | Adjustment | Normalized |
|---|---|---|---|
| Revenue | $26.53M | -- | $26.53M |
| Gross profit / margin | $18.29M / 68.9% | None needed -- no one-off this quarter | **68.9%** (genuinely clean, no adjustment required) [E26] |
| Net loss | -$12.68M | -- | -$12.68M |
| Adjusted EBITDA | -$6.14M | (company's own non-GAAP measure) | **-$6.14M** [E28] |
| Net cash used in operating activities | -$13.89M | Includes annual employee/management bonus payout (seasonal) [E29] | **-$13.89M**, but this quarter is seasonally the heaviest cash-use quarter of the year per management commentary; not a clean run-rate for the other 3 quarters |

**Key**: Q1 2026's GAAP-to-Adjusted-EBITDA gap is much narrower than FY2025's (no one-off inventory charge this quarter), and the gross margin of 68.9% required ZERO non-GAAP adjustment -- this is the strongest evidence in the whole dossier that the underlying unit economics have structurally improved, not merely been dressed up by one-time addbacks [I1].

---

## Multi-Year Trend (Annual)

| Metric | FY2023 | FY2024 | FY2025 |
|---|---|---|---|
| Revenue | $65.90M | $82.06M | $97.61M |
| Revenue growth | -- | +24.5% | +19.0% |
| Gross Profit (GAAP) | $16.86M | $48.83M | $45.73M |
| Gross Margin (GAAP) | 25.6% | 59.5% | 46.9% (E&O-depressed) |
| Gross Margin (Adjusted) | n/a in facts.md | 59.6% | 64.9% |
| Operating expenses | $162.47M | $123.24M | $132.15M |
| Loss from operations | -$145.61M | -$74.41M | -$86.42M |
| Net loss | -$133.70M | -$72.49M | -$77.06M |
| Net loss margin | -202.9% | -88.3% | -79.0% |
| Adjusted EBITDA | (not in facts.md for FY23) | -$38.88M | -$26.53M |
| Weighted-avg diluted shares | 205.39M | 211.68M | 247.12M |
| Net loss per share | -$0.65 | -$0.34 | -$0.31 |

**Trend analysis**: The revenue and margin trend is genuinely improving, but not linearly and not without noise:
- Revenue: +48% cumulative over 2 years (2023->2025), decelerating slightly in growth RATE (24.5% -> 19.0%) even as guidance implies a further step-down for FY2026 (~20-24% guided, [E33])
- GAAP gross margin is volatile (25.6% -> 59.5% -> 46.9%) because of large one-off inventory charges in both FY2023 (a $21.1M excess-inventory loss per the prior-year MD&A comparison embedded in the 10-K) and FY2025 ($17.4M E&O charge) -- the ADJUSTED gross margin trend (59.6% -> 64.9% -> 68.9% through Q1'26) is the much cleaner, monotonically improving signal [I1]
- Net loss margin has improved every year (-202.9% -> -88.3% -> -79.0%) despite the FY2025 one-off charge -- a genuine trend, not an artifact
- Net loss PER SHARE improved even faster (-$0.65 -> -$0.34 -> -$0.31) than net loss margin alone would suggest, BUT this is partly because the FY2025 dilutive raise increased the share count denominator -- i.e., some of the per-share improvement is arithmetic (more shares to spread the loss over), not purely operating leverage. Both effects are real and should not be conflated.

---

## Cash Flow / Burn / Runway Analysis (the central financial question for this name)

| Metric | FY2024 | FY2025 | Q1 2026 |
|---|---|---|---|
| Net cash used in operating activities | -$41.71M | -$12.70M | -$13.89M |
| Net cash used in investing activities | -$2.66M | -$3.35M | -$0.95M |
| Net cash from financing activities | -$1.50M | +$77.76M (incl. $81.0M raise) | +$2.31M |
| Net change in cash | -$45.86M | +$61.71M | -$12.54M |
| Period-end cash & equivalents | $88.78M | $150.49M | $137.95M |

**Ex-financing cash burn** (the cleanest "how fast is the business itself burning cash" measure, backing out the one-time capital raise): FY2024 ~-$44.4M (op + investing) / FY2025 ~-$16.0M (op + investing) / Q1 2026 ~-$14.8M (op + investing). **This shows a dramatic, real improvement from FY2024 to FY2025 (-$44.4M -> -$16.0M, a ~64% reduction)**, though Q1 2026 alone annualized (~-$59M/yr) would look worse than FY2025's full-year pace -- however, Q1 is explicitly flagged by management as the seasonally heaviest quarter (annual bonus payout) [E29], so a full-year FY2026 read should not be extrapolated from Q1 alone.

**Runway math** (Runner-derived, since the company does not publish a formal FY2026 FCF guide): At $137.95M cash (2026-03-31) and a guided FY2026 Adjusted EBITDA loss of $21-25M [E34] (used here as a reasonable full-year cash-burn proxy given the business's capital-light, positive-working-capital-in-recent-quarters profile), implied runway is **in excess of 5 years** even assuming zero further revenue growth beyond guidance and zero additional financing. This is a materially different risk profile from a typical pre-revenue biotech or early-stage device company burning down a 12-18 month runway. Management's own "sufficient for the next 12 months" language [E39] is therefore a conservative, not an alarming, disclosure -- it is boilerplate required disclosure language, not a signal of near-term distress.

**Caveat**: this runway estimate uses Adjusted EBITDA as a burn proxy, not a true unlevered FCF figure (which would also subtract capex and any working-capital swings); FY2025 capex was small (~$3.35M investing outflow), so the proxy is reasonable but not exact [O5].

---

## Balance Sheet Quality

| Metric | FY2024 (YE) | FY2025 (YE) | Q1 2026 |
|---|---|---|---|
| Cash and cash equivalents | $88.78M | $150.49M | $137.95M |
| Total assets | $256.08M | $296.53M | $285.92M |
| Total liabilities | $87.25M | $100.55M | $94.70M |
| Total stockholders' equity | $168.83M | $195.98M | $191.22M |
| Debt | None identified (no debt line items in balance sheet) | None identified | None identified |
| Restricted cash (lease-related letter of credit) | n/a in facts.md | $4.0M | $4.0M |

**Balance sheet is clean and simple**: no debt identified in any balance sheet reviewed -- BFLY has financed entirely through equity issuance, which is dilutive but carries zero bankruptcy/covenant/leverage risk. Total liabilities ($94.7-100.6M) are modest and mostly operating (deferred revenue, accrued expenses, operating lease liabilities) rather than financial obligations. Accumulated deficit of $879.2M [E24] reflects the cumulative cost of building the technology/commercial base since inception, not a distressed-balance-sheet signal given the substantial equity cushion ($191-196M) still in place.

---

## Dilution History (a first-class financial-quality question for this name, per the task brief)

| Period | Weighted-avg diluted shares | YoY change | Driver |
|---|---|---|---|
| FY2023 | 205.39M | -- | Baseline (post-SPAC + ongoing equity comp) |
| FY2024 | 211.68M | +3.1% | Ordinary equity-comp dilution, no major capital raise |
| FY2025 | 247.12M | +16.7% | Primarily the Jan-2025 27.6M-share, $81.0M-net public offering at $3.15/share [E37] -- a genuinely dilutive raise at a depressed price |
| 10-Q cover (2026-04-20) | 261.27M (point-in-time, not weighted-avg) | +2.6% vs FY2025 weighted-avg over ~4 months | Ongoing equity-comp vesting, no new major offering identified [E31] |

**Assessment**: Dilution is real and has been the primary financing mechanism (no debt used), but the RATE has decelerated sharply since the Jan-2025 raise -- the +16.7% FY2025 jump was a one-time capital-raise event, not an ongoing pace, and the subsequent ~2.6%-in-4-months pace is consistent with ordinary equity-compensation dilution at a company this size, not a repeat emergency raise. Given the >5-year runway estimate above, a NEAR-TERM repeat of the Jan-2025-style large dilutive offering does not look imminent on current information, though the 62.4M-share equity-plan reserve (16.1M ungranted) [E41] represents a persistent low-single-digit-percent/year overhang from ordinary equity compensation that will continue regardless.

---

## Earnings Quality Assessment

**Red flags at the accounting level**: NONE material identified. The company transparently discloses and separately reconciles its one-off items (E&O inventory charge, litigation accruals, warrant FV changes) rather than burying them inside an unexplained "other" bucket -- see facts.md E16-E18, E30. No going-concern qualification identified from the auditor in either the 10-K or 10-Q [E39].

**Genuine risks to future earnings quality**:
1. If the Butterfly Embedded / Midjourney-style licensing revenue (near-100% margin) does NOT continue to grow as a share of the mix, the recent gross-margin improvement trajectory [I1] could stall or partially reverse, since the improvement is substantially mix-driven, not purely a hardware-cost reduction.
2. The ~11%-single-customer revenue concentration [E59, O1] is a real earnings-quality risk that cannot be sized without knowing the customer's identity or contract terms.
3. Unreserved litigation exposure (Rose securities class action, [E44, O7]) is a genuine tail risk to future earnings/balance sheet that is not currently reflected in any P&L or balance-sheet line item.
4. Continued equity-comp dilution (SBC $23.4M/yr, [E41 context]) is a real, ongoing cost to per-share value even though it does not appear in the cash burn figures above.

**Overall financial quality**: GOOD-and-genuinely-IMPROVING, but still LOSS-MAKING with a THIN track record of the improvement (5 quarters: Q1'25 through Q1'26). The single best piece of evidence for financial-quality optimism is the Adjusted gross margin trend (59.6% -> 64.9% -> 68.9%) requiring progressively less non-GAAP massaging each period [I1]. The single best piece of evidence for caution is that this is still a company guiding to a FY2026 Adjusted EBITDA LOSS of $21-25M [E34] with an unresolved ~11% customer concentration and unreserved legacy litigation -- genuinely better than 2 years ago, not yet a proven, durable, profitable business model.
