# ASML Facts Ledger (M1 Evidence Spine)

As-of: 2026-07-02 | Run: 2026-07-04 | Pipeline: lean-6module-v1.1

Classification: EVIDENCE (primary/corroborated) · INTERPRETATION · SENTIMENT · OPEN · CONTRADICTIONS

Currency note: ASML reports in **EUR**. The as-of price is the **NASDAQ USD** line (the security the freshness gate re-fetches). EUR/USD = 1.1423 (2026-07-02) is used for the EUR-EPS -> USD-multiple bridge.

---

## EVIDENCE — price & capitalization (LIVE, >=3 sources, see freshness.json)

- **As-of price = $1769.32** (last fully-settled NASDAQ close 2026-07-02, down -4.0% / -$73.72 on the day). Yahoo chart API + stockanalysis + WallStreetZen all print $1769.32. [YAHOO-ASML-PRICE, ASML-SA-STATS, ASML-WSZ-STATS]
- 52-week high **$1,999.96**, low **$683.48** -> at $1769.32, -11.5% off high / +159% off low. This is a near-high entry after an enormous 12-month run (the stock roughly tripled off its 52wk low). [YAHOO-ASML-PRICE, ASML-WSZ-STATS]
- Previous close **$1,843.04** (2026-07-01). [ASML-SA-STATS]
- Shares outstanding **385.42M** (WSZ 385,417,665; AGM 2026 filing: 388,147,674 issued − 3,224,029 treasury = 384,923,645 outstanding @ 2026-03-25; stockanalysis 385.4M). Market cap **~$681.93B** (WSZ, dated 2026-07-02) = 385.42M x $1769.32 = $681.9B (identity-consistent). [ASML-WSZ-STATS, ASML-AGM-2026]
- Valuation: trailing P/E **~62.4x**; forward P/E **~47.2x** (stockanalysis, on its 2026E). Reconciliation via EUR: FY2025 EPS EUR24.73 x 1.1423 = $28.25 -> trailing 62.6x (matches). 2026E consensus EUR35.95 x 1.1423 = $41.07 -> forward ~43x on that basis. Headline: **~62x trailing / ~44-47x forward.** [ASML-SA-STATS, YAHOO-EURUSD]
- NOTE (data): stockanalysis reports market cap $719.43B on a higher (~406M) share basis; the identity-consistent 385.42M x price = $681.93B is used. Divergence flagged (see OPEN O3).

## EVIDENCE — FY2025 results (reported 2026-01-28; ASML press release + 6-K)

- Total net sales **EUR32.7B** (EUR32,667M). [ASML-Q4-2025-PR]
- Net income **EUR9.6B**; gross margin **52.8%**; basic EPS **EUR24.73**. [ASML-Q4-2025-PR]
- Free cash flow **EUR12,253M** (operating cash flow EUR13,827M − capex EUR1,574M); ~37.5% FCF/sales — capital-light for a hardware franchise. [ASML-SA-FINANCIALS]
- Q4 2025: net sales **EUR9.7B**; **net bookings EUR13.2B (EUR7.4B EUV)** — a record order quarter; **year-end 2025 backlog EUR38.8B.** [ASML-Q4-2025-PR]
- Capital return: FY2025 dividend **EUR7.50/share** (+17%); new **EUR12B buyback** program through 2028. [ASML-Q4-2025-PR]

## EVIDENCE — Q1 2026 results (reported 2026-04-15; ASML release + 6-K + IR deck)

- Total net sales **EUR8.8B** (+~13% YoY; −sequentially from EUR9.7B Q4'25); net system sales **EUR6.3B** (EUV **EUR4.1B**, non-EUV EUR2.1B), installed base management (service) **EUR2.5B**. [ASML-Q1-2026-6K]
- Gross margin **53.0%** (high end of guide, EUV-mix driven); net income **EUR2.8B** (31.4% margin); basic EPS **EUR7.15**; **79 lithography systems** sold. [ASML-Q1-2026-PR, ASML-Q1-2026-6K]
- **China fell to 19% of system sales** (from 36% in Q4'25); the drop is concentrated in lower-margin DUV. **Korea was the #1 market at 45% of system sales** (memory makers buying for AI). [ASML-Q1-2026-IRDECK]
- Buyback **EUR1.1B** (~0.9M shares) in Q1 under the 2026-2028 program. [ASML-Q1-2026-PR]
- **FY2026 guidance RAISED to EUR36-40B net sales** (from EUR34-39B at Q4'25), GM **51-53%**, on AI-driven demand. [ASML-Q1-2026-PR]

## EVIDENCE — 5-year financial trend (stockanalysis, cross-checked to filings)

| FY | Revenue (EURm) | Gross margin | Op margin | Net income (EURm) | FCF (EURm) |
|---|---:|---:|---:|---:|---:|
| 2021 | 18,611 | 52.7% | 36.3% | 5,883 | 9,945 |
| 2022 | 21,173 | 49.7% | 34.6% | 6,396 | 8,153 |
| 2023 | 27,559 | 50.0% | 34.5% | 8,115 | 4,381 |
| 2024 | 28,263 | 50.5% | 35.2% | 8,349 | 10,303 |
| 2025 | 32,667 | 52.8% | 36.9% | **9,600** (ASML primary) | 12,253 |
| TTM (Mar'26) | 33,693 | ~52% | ~37% | ~9,900 | 8,971 |

Revenue +12%/yr CAGR (2021-25); gross margin structurally ~50-53%; FCF lumpy (down-cycle 2023) but strong. Share count falling on buyback. [ASML-SA-FINANCIALS, ASML-Q4-2025-PR]

## EVIDENCE — the moat / mechanism (EUV monopoly)

- ASML is the **sole producer of EUV lithography** worldwide — the only tool able to pattern the smallest features on leading-edge logic (TSMC/Samsung/Intel) and advanced DRAM. No qualified competitor exists. [ASML-INVDAY-2024, multiple]
- **High-NA EUV (0.55 NA, EXE:5200 class):** Intel deployed the industry-first EXE:5200B (Dec 2025); Samsung + SK hynix expected first mass adopters 2027-28; **TSMC has declined High-NA for its 1.4nm node on cost** (~$400M/tool). First High-NA memory/logic products expected "within months" (May 2026). [ASML-HIGHNA]
- 2030 model (Investor Day 2024): sales **EUR44-60B**, gross margin **56-60%**, on a double-digit EUV spending CAGR 2025-30 and a >$1T semiconductor TAM by 2030. [ASML-INVDAY-2024]

## EVIDENCE — operator & governance

- **Christophe Fouquet**, President & CEO since **2024-04-25**. MSc Physics, **Institut Polytechnique de Grenoble (1997)**; roles at Applied Materials + KLA-Tencor; **joined ASML 2008** (marketing/product mgmt); **EVP EUV 2018** (industrialized EUV); Chief Business Officer 2022; CEO 2024. A technologist who rose through the EUV program. [ASML-FOUQUET-BIO]
- Governance: **two-tier board** (5-member Board of Management under CEO + 9-member independent Supervisory Board); **strict one-share-one-vote, no dual class**; **Stichting Preferente Aandelen ASML** holds a preference-share option as an anti-hostile-takeover backstop only (standard Dutch structure; not a control-entrenchment device). No holder >~15% of votes. [ASML-GOV-2025]

## EVIDENCE — China export-control status (LIVE-qualitative, freshest sources)

- **June 2026 (freshest):** US Commerce Secretary Lutnick alleged a possible unauthorized EUV transfer to a Chinese customer; **ASML formally denies** ("No indication of any ASML EUV System in China"; states all 314 EUV machines accounted for). US presented evidence of EUV transport-equipment/component shipments -> **BIS enforcement risk on components** (parallels the Applied Materials Feb 2026 settlement, which was for components/units routed via Korea, not full systems). [ASML-CHINA-BIS]
- **April 2026:** bipartisan **MATCH Act** introduced — would **ban ALL DUV shipments to China** (the permitted sales ~= **20% of ASML's 2026 revenue**) and require the Netherlands to align export controls within **150 days** or face unilateral US action. [ASML-CHINA-MATCH]
- ASML has **never shipped EUV to China**; the Netherlands has restricted DUV immersion tools since Jan 2023. Management guided China to **~20% of 2026 sales** (from 33% in 2025); Q1'26 already at 19%. CEO: the EUV ban sets China's leading-edge back "10-15 years." [ASML-CHINA-MATCH, ASML-CHINA-BIS]

## INTERPRETATION

- ASML is the single deepest chokepoint in the semiconductor stack — a genuine EUV monopoly upstream of every leading-edge AI chip (NVDA GPUs, Google TPU, AWS Trainium all require TSMC/Samsung leading-edge, which requires ASML EUV). Business quality is exceptional (+2).
- This is an **AI-STACK name**: it ADDS to the investor's BTC/GOOGL/NBIS "AI + liquidity" factor. It is NOT a diversifier — but it is a uniquely differentiated chokepoint (a monopoly toll, not another GPU/cloud bet).
- The binding question is PRICE (M6) and the China/cyclicality tail (M5), not business quality or completeness.

## SENTIMENT (leads only, not load-bearing)

- Sell-side skew strongly bullish (~38 buy / 2 sell, "Strong Buy" aggregate) post-Q1 beat-and-raise; framed as "quietest moat in AI." Treated as sentiment; does not by itself justify entry at ~62x.

## OPEN

- **O1:** FY2025 net income discrepancy — stockanalysis EUR10,213M / EPS EUR26.26 vs ASML-primary EUR9.6B / EUR24.73. Primary used; stockanalysis series otherwise consistent for prior years. Resolve against the 20-F when extracted.
- **O2:** ASML **stopped publishing quarterly net bookings from 2026** -> Q1'26 order intake not formally disclosed (only qualitative "strong AI-driven order intake"). Backlog EUR38.8B (Jan 2026) is the last hard number; reduced forward visibility is a real (if minor) transparency downgrade.
- **O3:** Market-cap source spread ($681.93B identity-consistent vs $719.43B stockanalysis on a higher share basis) — used the identity-consistent figure; reconcile share count vs the 20-F.
- **O4:** No direct SEC 20-F / full-filing extraction this pass (used official ASML releases + 6-K + aggregators). Load-bearing numbers all corroborated >=2 sources.
- **O5:** EUR->USD multiple bridge introduces FX noise in the forward P/E (43x on EUR EPS vs 47x reported); the through-cycle valuation conclusion is insensitive to this.

## CONTRADICTIONS

- Amsterdam EUR line (~EUR1,634, 2026-07-04) vs NASDAQ USD line ($1769.32) — same security, not a contradiction (FX + the day's move).
- FY2025 net income (O1) is the one genuine data conflict; resolved in favor of the ASML primary release.
