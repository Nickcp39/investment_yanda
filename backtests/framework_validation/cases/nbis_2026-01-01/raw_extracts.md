# Raw Extracts - NBIS as of 2026-01-01

Neutral excerpts / close paraphrases from primary filings, official releases, the CEO
shareholder letter, dated industry sources, and market data. Every item is dated on or
before 2026-01-01. Square brackets are clarifications added by the runner; everything
else is quoted or closely paraphrased from the cited source.

---

## A. As-of price and capitalization (S014)

Daily OHLC for NBIS, late December 2025 (Yahoo Finance chart API v8, saved to
`backtests/data/asof_2025_12_31_nbis_quotes.csv`):

| date | open | high | low | close | volume |
|---|---:|---:|---:|---:|---:|
| 2025-12-22 | 92.97 | 95.90 | 91.10 | 93.23 | 11,303,100 |
| 2025-12-23 | 90.31 | 92.97 | 88.31 | 90.03 | 8,885,700 |
| 2025-12-24 | 90.23 | 91.42 | 88.65 | 91.13 | 3,338,000 |
| 2025-12-26 | 91.51 | 91.62 | 86.74 | 87.59 | 6,234,600 |
| 2025-12-29 | 84.45 | 88.61 | 84.29 | 86.04 | 8,076,100 |
| 2025-12-30 | 86.38 | 86.96 | 84.56 | 85.17 | 5,802,300 |
| **2025-12-31** | **85.37** | **86.47** | **82.90** | **83.71** | **7,055,900** |

- **As-of price (2025-12-31 close): $83.71.** Last trading day on/before the 2026-01-01 as-of date.
- Shares issued & outstanding 9/30/25 (S012): 251,807,222 (218,158,548 Class A + 33,648,674 Class B), excl. 110,233,722 treasury Class A shares.
- **As-of market cap (all shares x close): ~$21.1B** (251,807,222 x $83.71 = $21.08B). Class A-only basis: ~$18.3B.
- Late-Dec 2025 context: stock drifted from ~$93 (Dec 22) to ~$84 (Dec 31), i.e., a soft tape into year-end.

---

## B. FY2024 baseline (S001, reported 2025-02-20)

- "In Q4 2024, the Group's revenue of $37.9 million increased 466% year over year, driven primarily by the core AI infrastructure business, which grew 602% year over year."
- "For the full year 2024, the Group's revenue of $117.5 million increased 462% year-over-year."
- "Cash and cash equivalents as of December 31, 2024, stood at $2,449.6 million on a consolidated basis."
- "Full year 2024 adjusted EBITDA loss was $266.4 million and net loss from continuing operations was $396.9 million."
- "Based on contracts already in place, MarchARR will be at least $220 million, and we have additional potential deals in the pipeline." [ARR = annualized run-rate revenue; the early-2025 launch point.]

## C. ARR / revenue trajectory across 2025 (S003-S006, S012-S013)

| Period | Group revenue | Core AI infra ARR (exit) | Group adj EBITDA | Cash (period end) | Quarter capex |
|---|---:|---:|---:|---:|---:|
| Q4'24 / FY24 | $37.9M / $117.5M | ~$220M (MarchARR floor) | -$75.5M / -$266.4M | $2,449.6M | n/a |
| Q1'25 (S003/S004) | $55.3M (+385%) | ~$249M end-March (+684% YoY); ~$310M April | -$62.6M | $1,447.0M | $544.0M |
| Q2'25 (S005/S006) | $105.1M (+625% YoY, +106% QoQ) | $430M end-June | -$21.0M (core positive ahead of plan) | $1,679.3M | $510.6M (H1 $1,054.5M) |
| Q3'25 (S012/S013) | $146.1M (+355% YoY, +39% QoQ) | ~$551M end-Sept (core grew 400% YoY) | -$5.2M (core ~19% margin) | $4,794.8M | $955.5M |

- Q2'25 net income from continuing operations was **+$502.5M**, but adjusted net loss was **-$91.5M** (S005). The GAAP profit was driven by a one-time gain on revaluation of the Toloka equity stake, not by operations.
- Q3'25 net loss from continuing operations was **-$119.6M** (S012).
- Core AI infrastructure was ~90% of group revenue in Q3'25 (S013).

## D. Q3 2025 balance sheet (S012, as of 9/30/25 vs 12/31/24)

| Item | 12/31/24 | 9/30/25 |
|---|---:|---:|
| Cash and cash equivalents | 2,434.7 | 4,794.8 |
| Property and equipment | 846.7 | 3,314.4 |
| Investments in non-marketable equity securities | 90.7 | 835.1 |
| TOTAL ASSETS | 3,548.6 | 10,102.2 |
| Debt, current | 6.1 | 16.0 |
| Debt, non-current [convertible notes] | 0.0 | 4,090.8 |
| Total liabilities | 294.9 | 5,291.4 |
| Total shareholders' equity | 3,253.7 | 4,810.8 |

- Net cash position at 9/30/25: cash $4,794.8M vs total debt ~$4,106.8M -> roughly **net-cash / near-flat** at the quarter end (before subsequent capex draw-down).
- D&A Q3'25 $99.0M (hardware depreciated over a 4-year period, "which we believe is conservative"; S013).
- 9M-2025 cash used in operating activities -$432.4M; 9M-2025 purchases of PP&E -$2,010.0M (S012).

## E. Microsoft agreement (S007, S008; announced 2025-09-08)

- "Under this multi-year agreement, Nebius will deliver dedicated capacity to Microsoft from its new data center in Vineland, New Jersey starting later this year." (S007)
- "...the total contract value is about $17.4 billion through 2031. Microsoft may also acquire additional services and/or capacity under the Agreement, which would increase the total contract value to about $19.4 billion." (S008)
- "The GPU Services will be deployed in several tranches during 2025 and 2026." Five-year term. (S008)
- Financing intent: "Nebius expects to finance the capital expenditure associated with the contract through a combination of cash flow coming from the deal and the issuance of debt secured against the contract... at terms enhanced by the credit quality of the counterparty." (S007)
- CEO: "...we expect to secure significant long-term committed contracts with leading AI labs and big tech companies. I'm happy to announce the first of these contracts, and I believe there are more to come." (S007)

## F. Meta agreement (S012, S013; announced 2025-11-11)

- "Today we are pleased to announce our second large AI infrastructure deal, this time with Meta. Our agreement with Meta is valued at approximately $3 billion, with a five-year term. Over the next three months, we plan to deploy the capacity needed to service the agreement. In fact, demand for this capacity was overwhelming, and the size of the contract was limited to the amount of capacity that we had available." (S013)

## G. Capacity / power guidance (S013, dated 2025-11-11)

- "Last quarter we guided for 1GW of contracted power by the end of 2026. We are currently in the process of securing additional sites that would bring our total contracted power (i.e., secured land with power) to approximately 2.5GW by the end of 2026. Of this contracted amount, we expect to have 800MW to 1GW of connected power (i.e., power connected to built data centers) by the end of 2026."
- "We are on track for 220 MW of connected power and 100 MW of active power by the end of 2025."
- Three power definitions: (1) contracted = secured by contracts; (2) connected = connected into data centers; (3) active = consumed by IT equipment.
- Footprint: data centers in North America (Kansas City B200 cluster; New Jersey for Microsoft), Europe (Finland expansion; UK B300 deployment), Middle East (Israel B200, launched October).
- "The only real limitation on our revenue growth in 2025 has been the amount of capacity that we have been able to bring online."

## H. 2026 ARR target and financing plan (S013, dated 2025-11-11)

- "...we believe that we can achieve annualized run-rate revenue (ARR) of $7 billion to $9 billion by the end of 2026." [ARR = last month of quarter x 12.]
- "To support our aggressive growth plans in 2026 and to maintain this pace of growth in 2027, we will utilize at least three sources of financing: corporate debt, asset-backed financing, and equity. We believe we will be able to secure asset-backed debt on attractive terms, supported by the creditworthiness of our largest customers. We will maintain a disciplined capital structure."
- "...we will be putting in place an at-the-market (ATM) equity program for up to 25 million Class A shares... we will remain dilution-sensitive..." (also S012)
- CEO framing: "2025 has been a building year... we believe that we have successfully laid the foundations for an outstanding 2026 — a year that should firmly position us among the top AI cloud businesses globally. And at the same time, 2026 is still just the beginning."
- [Runner note: the Q3 letter cover graphic displays "$4.3 billion expected annualized run-rate revenue at year-end 2026," which conflicts with the $7-9B ARR target stated twice in the letter body. The $4.3B figure matches the September 2025 capital raised, not an ARR target; the runner treats the stated ARR target as $7-9B and flags the cover figure as a likely design artifact.]

## I. September 2025 financing (S009, S010, S011)

- Convertible senior notes priced 2025-09-10, upsized to $2.75B: $1.375B of 1.00% notes due Sept 15, 2030 and $1.375B of 2.75% notes due Sept 15, 2032; conversion price ~$138.75 (50% premium over $92.50). (S009)
- Concurrent equity offering: $1.0B of Class A ordinary shares at $92.50/share (10,810,811 shares), 30-day greenshoe; lead bookrunner Goldman Sachs. (S010)
- Combined gross proceeds ~$4.2B at the Sept 15 closings (after the equity greenshoe ~$4.3B). Use of proceeds: compute/hardware, land, data-center expansion. (S011)

## J. Background: relisting, divestiture, NVIDIA stake (S015-S017)

- Relisting: trading resumed on Nasdaq under NBIS on 2024-10-21 (halted since Feb 2022 as Yandex N.V./YNDX). (S016)
- Yandex divestiture: 2024-02-05 agreement to sell Russian operations for RUB 475B (~$5.4B) at the mandated >=50% discount; closed in two stages mid-2024. Retained businesses: AI cloud (Nebius), Toloka, Avride, TripleTen, and a stake in ClickHouse. (S017)
- December 2024 raise: ~$700M at $21.00/share; investors included NVIDIA, Accel, and Orbis. NVIDIA's individual stake size was not disclosed. (S015)
- Equity-stake optionality: Uber strategic investment/commitments up to $375M in Avride (Oct 2025); Toloka May 2025 round implied ~$6.35B valuation; minority ClickHouse stake. (S013, S023)

## K. Industry / neocloud context (S018-S021)

- CoreWeave (closest public neocloud comp): IPO priced $40/share on 2025-03-27, ~$1.5B raised, implied EV ~$23B; 2024 revenue $1.9B (+737% YoY); Microsoft = 62% of 2024 revenue (customer concentration). (S018)
- CoreWeave Q3'25 (reported 2025-11-10): revenue $1.36B (+134% YoY), backlog ~$55B; flagged data-center delivery delays. (S019)
- IEA "Energy and AI" (2025-04): data-center electricity demand projected to more than double to ~945 TWh by 2030; ~20% of planned projects at risk of delay; multi-year transmission and turbine lead times -> contracted power is the binding industry constraint. (S020)
- Nasdaq-100 reconstitution announced 2025-12-13 (effective Dec 22): NBIS was NOT added -> no passive-index demand tailwind as of the as-of date. (S021)

## L. Market positioning / sentiment (dated 2025) (S022, plus S009/S012)

- Short interest ~33.07M shares = 15.47% of float as of late Dec 2025 (vs ~5.6% peer average), ~2.76 days to cover. (S022) -> a contested, heavily-debated stock.
- Goldman Sachs initiated coverage at Buy with a $68 price target on 2025-07-14, raised to $155 on 2025-11-14 (only major-bank initiation on/before the as-of date) [secondary, dated headline].
- The Sept 2025 equity print at $92.50 and the convertible conversion reference at $138.75 are dated market anchors set by the company's own financing.
