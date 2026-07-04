# ASML Raw Extracts (light — release / 6-K / IR-deck / aggregator based)

As-of: 2026-07-02 | Run: 2026-07-04

> One-pass LIVE run. Raw material is the set of official ASML releases, the Q1 2026 6-K, the Q1 2026 IR deck,
> Investor Day 2024, plus reputable financial data (stockanalysis, WallStreetZen) and dated China-policy media.
> No direct SEC 20-F full-text extraction this pass (O4). All load-bearing numbers corroborated >=2 sources.

## Price (LIVE, re-fetched by gate)

- Yahoo chart API (ASML, NASDAQ) last close <= 2026-07-02 = **$1,769.32** (verified via scripts/market_data_download.fetch_yahoo).
- stockanalysis overview (2026-07-02): price $1,769.32, prev close $1,843.04, 52wk $683.48-$1,999.96, trailing P/E 62.38, fwd P/E 47.21, shares 385.40M.
- WallStreetZen (2026-07-02): price $1,769.32, mcap $681.93B, shares 385,417,665, 52wk $683.48-$1,999.96.
- EUR/USD (Yahoo, 2026-07-02) = 1.1423.

## FY2025 (ASML release 2026-01-28)

- Net sales EUR32.7B (EUR32,667M); net income EUR9.6B; GM 52.8%; EPS basic EUR24.73.
- Q4'25 net sales EUR9.7B; net bookings EUR13.2B (EUR7.4B EUV); YE backlog EUR38.8B.
- Dividend EUR7.50/sh (+17%); new EUR12B buyback through 2028.
- FCF (stockanalysis): OCF EUR13,827M - capex EUR1,574M = FCF EUR12,253M.

## Q1 2026 (ASML release + 6-K + IR deck, 2026-04-15)

- Net sales EUR8.8B; net system EUR6.3B (EUV EUR4.1B, non-EUV EUR2.1B); IBM/service EUR2.5B.
- GM 53.0%; net income EUR2.8B (31.4%); EPS EUR7.15; 79 systems.
- China 19% of system sales (from 36% Q4'25); Korea #1 at 45%. Buyback EUR1.1B.
- FY2026 guide RAISED to EUR36-40B (from EUR34-39B), GM 51-53%.

## Moat / High-NA / operator

- EUV: ASML sole global producer. High-NA (0.55 NA, EXE:5200): Intel deployed first (Dec 2025); Samsung/SK hynix 2027-28; TSMC declined for 1.4nm on ~$400M/tool cost; first High-NA chips "within months" (May 2026).
- 2030 model (Investor Day 2024-11-14): sales EUR44-60B, GM 56-60%, double-digit EUV CAGR.
- Fouquet: MSc Physics Grenoble INP 1997; AMAT + KLA; joined ASML 2008; EVP EUV 2018; CBO 2022; CEO 2024-04-25.
- Governance: two-tier board; one-share-one-vote, no dual class; Stichting preference-share anti-takeover backstop.

## China policy (LIVE)

- MATCH Act (Apr 2026): would ban all DUV to China (~20% of 2026 rev); 150-day NL alignment.
- June 2026: Lutnick/BIS EUV-component-in-China allegation; ASML denies ("all 314 machines accounted"). Component-enforcement risk (cf. Applied Materials Feb 2026 settlement).

## Data conflicts logged

- FY2025 net income: ASML-primary EUR9.6B / EPS EUR24.73 vs stockanalysis EUR10,213M / EPS EUR26.26 (O1; primary used).
- Market cap: identity $681.93B vs stockanalysis $719.43B on higher share basis (O3; identity used).
