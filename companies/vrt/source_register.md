# Source Register — VRT

Last updated: 2026-06-19

Purpose: assign stable source IDs before claims enter `claim_ledger.csv`. IDs are kept consistent with `facts.md` (S1–S8).

Tier scheme: **A1** = SEC primary filing (10-K / 10-Q / 8-K / proxy). **A2** = company primary (IR newsroom, earnings release/8-K exhibit, investor-conference deck, official PR). **B1** = management commentary (earnings-call transcript, executive interview). **B2** = independent analyst / financial press / industry data. **C** = KOL/video (narrative only, never a fact).

| source_id | Tier | Source | Date | URL / Local path | Notes |
|---|---|---|---|---|---|
| S1 | A2/A1 | VRT Q1 2026 earnings release / 8-K | 2026-04-22 | investors.vertiv.com (Q1 2026 release) | Q1'26 sales/margin/EPS/FCF, regional organic, raised FY26 guide; **orders/B2B/backlog NOT in release** |
| S2 | B1 | VRT Q1 2026 earnings call transcript | 2026-04-22 | fool.com/earnings/call-transcripts/2026/04/22/vertiv-vrt-q1-2026-earnings-transcript/ | Mgmt "orders up YoY," backlog "elongated"; explicitly declines headline quarterly orders/B2B; 800V DC cadence |
| S3 | A2/A1 | VRT Q4 / FY2025 earnings release | ~2026-02-11 | investors.vertiv.com (Q4 2025 release) | FY2025 sales/margin/FCF; backlog $15.0B (+109%); Q4 B2B ~2.9x; TTM organic orders +81%; Q4 organic orders +252% |
| S4 | A2 | 2026 Investor Conference deck (Greenville SC) | 2026-05-19 | investors.vertiv.com/files/doc_presentations/2026/05/19/Vertiv-2026-Investor-Conference_May-19-2026.pdf | 2030 targets: organic rev CAGR 20–22%, adj op margin 27%; raised ceilings vs 2024 investor day |
| S5 | A2 | Vertiv × NVIDIA GB200 NVL72 reference design | 2024 | vertiv.com (co-develop press release) | Co-engineered 7MW power+cooling reference architecture for NVIDIA GB200 NVL72 rack |
| S6 | B2 | stockanalysis.com VRT statistics | 2026-06 | stockanalysis.com/stocks/VRT | Price, market cap, multiples, net cash, 52-wk range, analyst targets (aggregator) |
| S7 | B2 | MarketsandMarkets liquid-cooling share | 2025–26 | marketsandmarkets.com | VRT ~11.3% liquid-cooling share (2025), ~tied Schneider; DTC market CAGR |
| S8 | B2 | "Backlog Silence" analysis (Seeking Alpha) | 2026 | seekingalpha.com | Independent flag on the Q1'26 orders/B2B/backlog non-disclosure after a +252% Q4 |
| S9 | B2 | Hyperscaler 2026 capex coverage | 2026-02 | Tom's Hardware / CNBC | Big-4 2026 capex ~$700–725B (+62–77%); AMZN ~$200B, GOOGL $175–185B, META $115–135B, MSFT $110–120B |

Tier rules live in `../../sources/source_policy.md`.

## Source-quality note (VRT-specific)

VRT is a US domestic filer (10-K / 10-Q / 8-K, full SEC disclosure + quarterly calls) — a **higher-transparency baseline than the NBIS 20-F/6-K FPI regime**. That makes the **one** deliberate withdrawal — headline quarterly orders / book-to-bill / backlog in Q1'26 (S1/S2) — stand out more, not less. The binding gap in this case is therefore not a structural disclosure-regime limitation; it is a discretionary management choice, which is why it is treated as a soft negative throughout (`inversion_map.md`, `monitor.md`, `research_status.md`).
