# Source Register — CEG (Constellation Energy)

Last updated: **2026-06-22** (LIVE refresh of the 2026-06-19 seed)

Purpose: assign stable source IDs before claims enter `claim_ledger.csv`.

Tier scheme: **A1** = SEC primary filing (10-K / 10-Q / 8-K). **A2** = company primary (IR, earnings release, deck, PR). **A3** = government/regulatory primary (FERC / NRC / IRS / statute). **B1** = management commentary (call transcript). **B2** = independent analyst / financial press. **C** = KOL/video (narrative only, never a fact).

| source_id | Tier | Source | Date | URL / Path | Supports |
|---|---|---|---|---|---|
| **S1** | A2 | CEG FY2025 earnings release | 2026-02-23 | constellationenergy.com/news (FY2025 results) | FY2025 revenue/EPS/FCF, CF 94.7%, capital return — C001–C004, C020–C022 |
| **S2** | A1/A2 | CEG Q1 2026 8-K / earnings | 2026-05-11 | stocktitan.net/sec-filings/CEG/8-k...111d3b4cfb03 | Q1'26 rev/EPS, CF 92.3%, FY26 guide affirmed — C005–C010, C023, C030 |
| **S13** | A1 | CEG Q1 2026 **10-Q** | 2026-05-11 | sec.gov/Archives/edgar/data/0001868275/000186827526000067/ceg-20260331.htm | **Net debt ~$21.3B, 361.19M shares, Calpine consideration $21,835M** — C011r, C014 |
| **S14** | B1 | CEG Q1 2026 earnings call transcript | 2026-05-11 | fool.com/earnings/call-transcripts/2026/05/11/constellation-ceg-q1-2026 | Guidance commentary, accretion ~$2/share — C009, C010 |
| **S4** | A2 | CEG–Calpine completion release | 2026-01-07 | industrialinfo.com/.../constellation-energy-completes-calpine-acquisition--351594 | Calpine close, +23 GW — C012 |
| **S5** | A3 | FERC Order, Docket EL25-49 (193 FERC ¶61,217) | 2025-12-18 | FERC E-1-EL25-49-000 | 5-0 enabling order; accept-in-part 2026-04-16 — C015–C016 |
| **S6** | A3 | NRC draft EA / FONSI (Crane restart) | 2026-06-08 | Federal Register | Crane restart 2027, comment to 2026-07-08 — C017–C018 |
| **S7** | A3 | IRS §45U / Notice 2025-37; OBBBA P.L.119-21 §70510 | 2025-07 | irs.gov/credits-deductions/zero-emission-nuclear-power-production-credit | §45U survived OBBBA; ~$25/MWh floor to 2032 — C019, C026 |
| **S11** | A2 | CEG–LS Power divestiture (COMPLETED) | 2026-03 | CEG IR / LS Power PR | $5B/4.4 GW sale completed, cash in — C024 |
| **S8** | B2 | Hyperscaler 2026 capex compilation (FT/CNBC) | 2026-02 | cnbc.com/2026/02/06 | ~$725B +77% — C025 |
| **S9** | B2 | stockanalysis.com (CEG price/mcap/multiples/peers) | 2026-06-22 | stockanalysis.com/stocks/ceg/ | Price $277.75, fwd P/E, peers — C027r |
| **S15** | B2 | Yahoo Finance quote + chart API | 2026-06-22 | finance.yahoo.com/quote/CEG/ ; query1.finance.yahoo.com/v8/finance/chart/CEG | Price $277.17/$277.64, 52wk $240.51–$412.70 — C027r, C029 |
| **S16** | B2 | stockanalysis.com analyst forecast | 2026-06-18 | stockanalysis.com/stocks/ceg/forecast/ | Targets avg $360 / low $296 / high $441, 23 analysts, Buy — C028r |
| **S12** | A2/B2 | Microsoft–Constellation Crane PPA (20-yr) | 2024-09 | constellationenergy.com newsroom; datacenterdynamics.com | 20-yr PPA, front-of-meter; **price undisclosed** — C013 (price UNVERIFIED) |

## Notes on verification (2026-06-22)

- **Price** verified via Yahoo chart API (repo-mandated source) and cross-checked against stockanalysis.com + Yahoo quote — 3 independent sources within 0.21%. Freshness gate PASS.
- **S13 (10-Q)** is the headline upgrade this pass: it converts the seed's *estimated/disputed* leverage (C011) into a *primary* figure (net debt ~$21.3B; pro-forma ~2.25x) and confirms shares (361.19M) and Calpine consideration ($21,835M).
- **S12 (Microsoft PPA):** existence HIGH; **pricing UNDISCLOSED by CEG.** Secondary press estimates ($100–115/MWh) conflict with each other and are **explicitly held out of `facts.md`** as unconfirmed commentary — never used to support BUY.
- **C-tier / KOL:** none used for any number.
- Tier rules align with `sources/source_policy.md`.
