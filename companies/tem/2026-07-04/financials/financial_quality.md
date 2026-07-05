# TEM Financial Quality (M4)

Last updated: 2026-07-04 | as_of: 2026-07-04 | sources: facts.md, claim_ledger.csv

NORMALIZATION NOTE: TEM's financials are less "distorted by one-offs" than a mature industrial (contrast GEV) and more accurately described as **genuinely pre-profitability with an improving trajectory** — the key analytical task here is not stripping out non-recurring gains, but assessing (a) burn-rate trend quality, (b) the extent to which cash growth is self-funded vs financing-funded, and (c) dilution/capital-structure risk.

---

## One-Off / Base-Effect Registry

| Item | Amount | Period | Nature | Normalized Action |
|---|---|---|---|---|
| AstraZeneca warrant termination gain | $39.1M (FY2024) | FY2024 non-cash reconciliation | Non-recurring; distorts FY2025 Data/Insights YoY comp base | Note when reading Insights "growth %" — Q4 2025 Insights +69.5% is stated EX this effect |
| Tax valuation-allowance benefit | $46.18M | Q1 2025 (prior-year comp) | One-off tax benefit that inflated the Q1-2025 net-loss comp base | Explains why Q1 2026 net loss ($125.9M) looks WORSE than Q1 2025 ($68.0M) despite an operationally-improving business — remove this base effect when comparing YoY net loss trend |
| Stock-based comp step-down | $534.1M (FY24) -> $124.7M (FY25) | FY2024 vs FY2025 | IPO-driven RSU vesting/acceleration concentrated in FY2024 (IPO year) | FY2025's $124.7M (~10% of revenue) is the more representative go-forward run-rate, not FY2024's figure |
| Ambry, Paige AI, Deep 6 AI, OneOme acquisitions | $376.7M cash (FY2025 investing) | FY2025 | M&A-driven inorganic growth, funded by debt/equity issuance not FCF | Underlying organic growth rate is LOWER than the blended reported growth rate; Ambry alone contributed $63.5M revenue in one early quarter |

---

## Normalized Cash-Flow Bridge

### FY2025
| Item | GAAP | Read |
|---|---|---|
| Revenue | $1,271.8M | +83.4% YoY, real |
| Net loss | $(245.0)M | Improved from $(705.8)M FY2024, but FY2024 was inflated by a warrant fair-value charge — some improvement is base-effect, some is real |
| Adjusted EBITDA | $(7.4)M | Improved $97.3M YoY — genuine trajectory improvement, "even after" 4 acquisitions |
| OCF | $(218.1)M | WORSE in $ terms than FY2024's $(189.0)M, but off a much larger revenue base (burn/revenue improved from -27% to -17%) |
| Cash-flow funding source | Financing +$884.1M vs Operating+Investing -$616.4M | **100% of FY2025's net cash increase was financing-driven** (convertible notes, term loan, ATM), not self-funded |

### Q1 2026 (most recent quarter)
| Item | GAAP | Read |
|---|---|---|
| Revenue | $348.1M | +36.1% YoY |
| Net loss | $(125.9)M | Wider than Q1-2025's $(68.0)M, but ~$46.2M of that gap is a one-off tax-benefit base effect (see registry above), not operational deterioration |
| Loss from operations | $(84.7)M | vs $(68.7)M Q1-2025 — a genuine, smaller ($16M) operational widening, worth watching but not alarming given 36% revenue growth |
| OCF | $(73.3)M | **Improved ~31% from $(105.6)M Q1-2025** — the cleanest signal that underlying cash burn is genuinely improving faster than GAAP net loss suggests |
| Cash-flow funding source | Financing $(0.3)M (roughly neutral) vs Operating+Investing $(83.3)M | Q1 2026 alone was NOT propped up by new financing — cash simply declined ($604.8M -> $521.2M) by the organic burn amount. (The large financing event of the period, the $460M May 2026 convertible notes, closed AFTER this 10-Q's period-end and is a LIVE/subsequent item — facts.md E48-E53.) |

**Key finding**: the Q1 2026 OCF improvement (-$73.3M vs -$105.6M, a 31% improvement on 36% revenue growth) is the single most encouraging financial-quality data point in this dossier — it suggests real operating leverage is emerging, not just top-line growth.

---

## Multi-Year Trend (Annual, from 10-K three-year comparison)

| Metric | FY2023 | FY2024 | FY2025 |
|---|---|---|---|
| Revenue | $531.8M | $693.4M | $1,271.8M |
| Revenue growth YoY | — | +30.4% | +83.4% |
| Net loss | $(214.1)M | $(705.8)M | $(245.0)M |
| Adjusted EBITDA | $(154.2)M | $(104.7)M | $(7.4)M |
| Adj EBITDA margin | -29.0% | -15.1% | -0.6% |
| OCF | n/a (not extracted this run) | $(189.0)M | $(218.1)M |
| Burn / Revenue | n/a | -27.3% | -17.1% |

**Trend analysis**: Adjusted EBITDA margin has improved from -29.0% (FY2023) to -0.6% (FY2025), and management guides to a POSITIVE ~4% adj EBITDA margin for FY2026 (~$65M / ~$1.59B). This is a genuine, multi-year, monotonic improvement in the core operating-leverage story — the growth is not merely being bought with widening losses, contrary to a common bear-case caricature of high-growth healthcare-AI names. However, the improvement in $ burn terms is much less clean (OCF burn actually widened in absolute dollars from FY2024 to FY2025), so the "improving" read is entirely a RATIO story (burn relative to a fast-growing revenue base), not an absolute-dollar story.

---

## Dilution / Capital Structure Analysis

| Metric | Value | Read |
|---|---|---|
| Class A shares YE2024 | ~157.1M | Baseline |
| Class A shares Q1 2026 | ~174.4M | +11% in 5 quarters |
| Total shares (incl. Class B) as_of | 179,404,620 | Used for market-cap derivation |
| ATM facility remaining (YE2025) | ~$300.0M | Live, disclosed dilution lever, not yet exhausted |
| Original Convertible Notes (2030) | $729.3M outstanding (Q1 2026), conversion price $84.19 | 39% above as_of_price $60.27 — not yet in-the-money |
| **New Convertible Notes (2032, priced May 2026)** | $460.0M, conversion price **$69.26**, 0.00% coupon, capped call to $98.94 | Only **~15% above as_of_price $60.27** — the CLOSER, more near-term dilution overhang; a rally to $69-70 (well within a plausible 12-month range given the 52wk high of $104.32) begins activating this tranche |
| Total gross debt-like obligations (post-May-2026 refinancing, approximate) | ~$1.39B (2030 Notes $729M + 2032 Notes $460M + Convertible Promissory Note $199M, LESS the retired $304.6M Term Loan/Revolver) | Shift from secured bank debt (with Ares-affiliated covenants) to unsecured zero-coupon convertible debt — reduces covenant risk and near-term cash-interest burden, but increases total share-dilution optionality at a LOWER strike |

**Dilution verdict**: Real, ongoing, multi-vector (ATM + M&A stock + SBC-driven RSU vesting + now TWO convertible-note tranches with strike prices $69.26 and $84.19). Shareholders should model per-share value assuming continued share-count growth in the high single digits to low double digits annually until the company is self-funding, and should be aware the newer $69.26-strike notes activate a dilution/hedging dynamic well before the older $84.19-strike tranche.

---

## Cash Runway

| Input | Value |
|---|---|
| Cash + marketable securities, Q1 2026 (10-Q period-end) | $643.8M (cash $521.2M + marketable equity securities $117.9M, approx.) |
| Post-May-2026-refinancing cash effect | +$441.9M net proceeds from new Notes, LESS $307.7M used to repay Term Loan/Revolver, LESS $31.2M capped call = **~+$103.0M net cash impact**, before ongoing operating burn since Q1-end |
| Recent quarterly OCF burn rate | ~$(73.3)M/quarter (Q1 2026), improving trend |
| **Simple runway estimate** | Roughly **2+ years** at the current burn rate before any further capital raise, materially LENGTHENED by the May 2026 refinancing's net cash inflow — though further ATM/debt issuance remains a live possibility given the company's demonstrated appetite for M&A-funded growth |

**This is NOT a "cash-burning story with no visible runway."** The combination of an improving OCF-burn trend, a large disclosed cash balance, and a just-completed opportunistic refinancing (zero-coupon, extending maturity to 2032) gives Tempus real optionality and time. The risk is not imminent insolvency; the risk is CONTINUED DILUTION as the primary funding mechanism for growth, and a capital structure that assumes continued access to receptive convertible-debt/equity markets.

---

## Earnings Quality Assessment

**Yellow flags** (disclosed, not hidden, but warranting monitoring):
1. Related-party revenue (SB Tempus + Pathos) growing from ~$0.6M to ~$21.8M in one year within the Data and Applications segment (facts.md E43) — a meaningful and fast-growing slice of the "exciting" segment's growth is transactions with counterparties the founder/CEO has an economic interest in on both sides.
2. FY2025's cash growth was 100% financing-driven, not operational — a normal and disclosed fact for a growth-stage company, but one that should temper any narrative implying the business is close to self-funding.
3. Aggressive M&A cadence (4 acquisitions in ~1 year) funded substantially by debt/equity issuance rather than FCF, pre-profitability — increases integration risk and capital-structure complexity simultaneously.

**No red flags found at the accounting-fraud/going-concern level** in the primary text extracted: no going-concern qualification found in the liquidity sections reviewed (10-K/10-Q both state existing cash is sufficient for at least the next 12 months — E precedent in facts.md O4), no restatements found, no auditor-independence issues surfaced in this run's search.

**Overall financial quality**: FAIR AND IMPROVING. This is a genuine growth-stage healthcare-AI company with real, accelerating revenue, a credible (if thin-margin) path to adjusted profitability in FY2026, and an improving cash-burn trajectory — but it is NOT YET a self-funding business, dilution is structurally embedded in its financing model (now via TWO convertible-note tranches with progressively closer strike prices), and the related-party revenue growth deserves ongoing scrutiny. This is meaningfully weaker financial quality than either exemplar (GEV: FCF-positive, net-cash, dividend-paying; MSFT: massive FCF, net cash, dividend-paying) — as expected for a 2-year-public, pre-profitability name, but the gap should be explicitly priced, not glossed over by the AI narrative.
