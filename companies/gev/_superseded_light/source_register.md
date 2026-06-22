# Source Register — GEV

Last updated: 2026-06-19

Purpose: assign stable source IDs before claims enter `claim_ledger.csv`. IDs are referenced throughout `facts.md` and the analysis modules.

Tier scheme: **A1** = SEC primary filing (10-K / 10-Q / 8-K). **A2** = company primary (IR newsroom, press release PDF, investor-update deck, official PR). **B1** = management commentary (earnings-call transcript). **B2** = independent analyst / financial press / industry data. **C** = KOL/video (narrative only, never a fact).

| source_id | Tier | Source | Date | URL / Local path | Notes |
|---|---|---|---|---|---|
| S1 | A1 | GEV FY2025 10-K (gev-20251231) | filed Feb 2026 | sec.gov/Archives/edgar/data/0001996810/000199681026000015/gev-20251231.htm | Annual report; segment revenue/op income, FY2025 net income incl. tax-valuation-allowance release, FCF, RPO, capital allocation |
| S2 | A1 | GEV Q1 2026 10-Q (gev-20260331) | filed Apr 2026 | stocktitan.net/sec-filings/GEV/10-q...2e29f22ab875.html | Q1'26 revenue/net income, Prolec remeasurement gain, contract-liability inflow, RPO $163.3B split, cash/debt |
| S3 | B1 | GEV Q1'26 earnings call transcript | 2026-04-22 | fool.com/earnings/call-transcripts/2026/04/22/ge-vernova-gev-q1-2026-earnings-transcript/ | 100 GW under contract (44+56), slots sold-out-through-2029, +10–20% pricing, $42B Electrification backlog, $5.3B WC benefit / $4.8B FCF, $4.5B M&A gains, segment margins, FY26 guide. **Confirmed by WebFetch 2026-06-19.** |
| S4 | A2 | GEV Dec 2025 Investor Update (raises outlook, doubles dividend, increases buyback) | 2025-12-09 | gevernova.com/news/press-releases/ge-vernova-raises-multi-year-financial-outlook-doubles-dividend-increases-buyback-authorization | Dividend $0.25→$0.50/qtr; buyback $6B→$10B ($3.3B spent by Dec 3 2025); 2028 targets rev $52B, Power 22% / Electrification 22% / Wind 6% / company 20% EBITDA. **Confirmed by WebFetch 2026-06-19.** |
| S5 | A1/A2 | GEV Q1'26 press release (8-K) | 2026-04-22 | gevernova.com/sites/default/files/gev_webcast_pressrelease_04222026.pdf | Q1'26 results PR; Prolec buy-in completion, segment detail. (PDF binary on fetch — figures cross-read from S2/S3.) |
| S6 | B2 | stockanalysis.com GEV statistics | 2026-06-18 | stockanalysis.com/stocks/gev | Price, market cap, screener multiples (trailing P/E 32, EV/EBITDA 85x, fwd P/E 60) — **distorted by one-offs, flagged** |
| S7 | B2 | GMInsights gas-turbine market-share data | 2026 | gminsights.com (gas turbine market) | GT share ~18.5% of all gas turbines 2025; GEV+Siemens Energy+Mitsubishi ≈ two-thirds heavy-duty |
| S8 | B2 | Power-Eng / Power-Engineering turbine-slot analysis | 2026 | power-eng.com | Slot scarcity / lead-time / pricing-path-to-$600/kW industry color |
| S9 | B2 | Tom's Hardware / CNBC hyperscaler 2026 capex compilation | 2026-02 | tomshardware.com; cnbc.com | 2026 hyperscaler capex ≈ $725B (+77%): AMZN $200B, GOOGL $175–185B, MSFT $190B, META $115–135B — the shared-switch input |
| S99 | C | (none yet) | — | — | No KOL/video source used. Reserved. |

Tier rules: A1/A2 primary preferred for every load-bearing number; B2 for market/industry context only; C never promoted to a fact. Time-sensitive claims must carry a date. See `../../sources/source_policy.md` if present.
