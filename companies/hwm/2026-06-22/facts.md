# HWM Facts Ledger (M1 Evidence Spine)

As-of: 2026-06-22 | Run: 2026-06-23 | Pipeline: lean-6module-v1.1

Classification: EVIDENCE (primary/corroborated) · INTERPRETATION · SENTIMENT · OPEN · CONTRADICTIONS

---

## EVIDENCE — price & capitalization (LIVE, >=2 sources, see freshness.json)

- **As-of price = $280.36** (last fully-settled NYSE close 2026-06-22). Yahoo chart API + stockanalysis history + Google Finance agree. Today 2026-06-23 was an active unsettled session (~$275.1 intraday at run time); as_of pins to the prior settled close. [YAHOO-HWM-PRICE, HWM-SA-STATS]
- 52-week high **$290.63**, low **$169.45** -> at $280.36, -3.5% off high / +65% off low. [YAHOO-HWM-PRICE, HWM-SA-STATS]
- Shares outstanding ~**400.3M** (10-Q cover 400,713,557 @ 2026-03-24; stockanalysis 400.11M; "401M at period end"). Market cap ~**$112.2B** at $280.36; EV ~**$114.3B**. [HWM-10Q-Q1-2026, HWM-SA-STATS]
- Valuation: trailing P/E ~65x (TTM EPS $4.31); forward P/E ~57x (FY26E adj EPS $4.94); EV/FY26E adj EBITDA ~37x; P/TTM FCF ~68x. [HWM-SA-STATS]

## EVIDENCE — Q1 2026 results (reported 2026-05-07; PRNewswire + 8-K)

- Revenue **$2,313M, +19% YoY** (vs $1,942M Q1 2025). [HWM-Q1-2026-PR]
- GAAP net income **$580M**; GAAP diluted EPS **$1.44**; adjusted EPS **$1.22**. [HWM-Q1-2026-PR]
- Adjusted EBITDA **$740M**, margin **32.0%** (+320bps YoY from 28.8%). [HWM-Q1-2026-PR]
- Free cash flow **$359M** after capex **$94M** (asset-light conversion). [HWM-Q1-2026-PR]
- Buyback **$300M** in Q1 @ avg **$230.43/share**; dividend **$0.12/qtr** (+20% YoY). [HWM-Q1-2026-PR, HWM-CAPALLOC]
- Segments: Engine Products **$1,253M (+29%)**, 36.6% EBITDA (+400bps); Fastening Systems **$471M (+14%)**, 31.8%; Engineered Structures **$294M (-3%)**, 22.4%; Forged Wheels **$295M (+17%)**, 30.5%. [HWM-Q1-2026-PR]
- End markets: commercial aero **+20%**, defense aero **+10%**, gas turbines **+39%**; commercial transportation volumes **-11%**. [HWM-Q1-2026-PR]
- Balance sheet: cash **$2,435M**; total debt ~**$4,500M** (LT $4,050M + ST $450M); net debt ~**$2,065M** (~0.7x FY26E EBITDA). [HWM-Q1-2026-PR]
- M&A: completed **CAM** acquisition 2026-04-06 for ~**$1.8B**; acquired **Brunner Mfg** ~$120M (2026-02-06); sold **Savannah** disk-forging facility 2026-03-31 for ~$230M ($93M pre-tax gain). [HWM-Q1-2026-PR]

## EVIDENCE — FY2026 guidance (RAISED at Q1, 2026-05-07)

- Revenue **$9,575-9,725M** (baseline $9,650M, +$550M). [HWM-Q1-2026-PR, HWM-Q1-2026-8K]
- Adjusted EBITDA **$3,025-3,095M** (baseline $3,060M, +$300M, +140bps). [HWM-Q1-2026-PR]
- Adjusted EPS **$4.88-5.00** (baseline $4.94, +$0.49). [HWM-Q1-2026-PR]
- Free cash flow **$1,700-1,800M** (baseline $1,750M, +$150M). [HWM-Q1-2026-PR]

## EVIDENCE — 10-year financial trend (stockanalysis, consistent with filings)

| FY | Revenue | Op margin | Diluted EPS | FCF |
|---|---:|---:|---:|---:|
| 2021 | $4,972M | 15.0% | $0.59 | $250M |
| 2022 | $5,663M | 16.2% | $1.11 | $540M |
| 2023 | $6,640M | 18.1% | $1.83 | $682M |
| 2024 | $7,430M | 22.0% | $2.81 | $977M |
| 2025 | $8,252M | 24.8% | $3.71 | $1,431M |
| TTM | $8,623M | — | $4.31 | $1,656M |

Clean secular margin expansion + FCF ramp; no dilution (share count falling on buyback). [HWM-SA-FINANCIALS]

## EVIDENCE — operator & governance

- **John C. Plant**, Exec Chairman & CEO (age ~71). Prior: CEO/Chairman TRW Automotive (sold to ZF ~$13.5B, 2015); led Arconic->Howmet separation; CEO HWM 2019-20, Co-CEO 2020-21, CEO 2021-present. Univ. of Birmingham (economics/accounting/law), Fellow Inst. of Chartered Accountants. [HWM-PLANT-BIO]
- Capital allocation: completed $2.45B / 34.0M-share multi-year buyback since 2021; $1,047M authorization remaining (2026-05-04); +20% dividend. Fitch upgraded to **A-** (2026-02-13) from BBB+; all 3 agencies >=3 notches into IG. [HWM-CAPALLOC, HWM-FITCH-UPGRADE]
- One-share-one-vote; no dual-class.

## INTERPRETATION

- HWM is a quality_compounder riding a genuine commercial-aero up-cycle + engine-spares annuity; Engine Products is a true bottleneck (certified superalloy airfoils). Business +2; price -2.
- Diversifies the user's BTC/GOOGL/NBIS AI/liquidity single factor (aero/defense cycle, not AI-capex).

## SENTIMENT (leads only, not load-bearing)

- Sell-side / aggregator commentary uniformly bullish on the Q1 beat + raised guide ("margin breakout", "raises 2026 outlook"). Treated as sentiment; does not support BUY at this price.

## OPEN

- O1: Precise **spares** figure (~$520M, +36%, 23% of revenue) is from a StockTitan/SimplyWallSt summary, NOT primary release text (release confirms qualitatively only). Confirm vs 10-Q before treating as load-bearing.
- O2: No direct SEC full-text 10-Q/10-K extraction this pass (used release + aggregators).
- O3: No clean normalized owner-earnings bridge (Q1 GAAP $1.44 includes $93M Savannah gain; adj $1.22 used).
- O4: CAM ($1.8B) revenue/EBITDA contribution and integration risk from Q2 not yet visible.
- O5: Plant succession / bench depth below CEO is thin in public disclosure (key-man risk).

## CONTRADICTIONS

- None material. Apparent market-cap spread ($110.1B stockanalysis vs $112.2B derived) is purely the price-date difference (06-23 intraday $275.20 vs 06-22 settled $280.36), not a share-count discrepancy.
