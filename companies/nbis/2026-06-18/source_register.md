# Source Register — NBIS

Last updated: 2026-06-18

Purpose: assign stable source IDs before claims enter `claim_ledger.csv`.

Tier scheme: **A1** = SEC primary filing (20-F/6-K/13F/13G). **A2** = company primary (IR newsroom, shareholder letter PDF, official PR, policy doc). **B1** = management commentary (earnings-call transcript, founder interview). **B2** = independent analyst / financial press. **C** = KOL/video (narrative only, never a fact).

| source_id | Tier | Source | Date | URL / Local path | Notes |
|---|---|---|---|---|---|
| SRC-001 | A1 | FY2025 Form 20-F | 2026-04-30 | sec.gov/Archives/edgar/data/1513845/.../nbis-20251231x20f.htm | Annual report; income stmt, cash flow, ICFR, dep policy, MSFT/Meta rev recognition, governance |
| SRC-002 | A2/A1 | Q1 2026 Letter to Shareholders (6-K) | 2026-05-13 | assets.nebius.com/.../Nebius%20SHL_Q1%202026.pdf | Power definitions, capacity guidance, Q1'26 financials, capex |
| SRC-003 | A2/A1 | Q4 2025 / FY2025 shareholder letter (6-K) | 2026-02-12 | sec.gov/Archives/edgar/data/1513845/.../tm266173d1_ex99-2.htm | YE2025 contracted >2GW, active ~170MW, first group +EBITDA |
| SRC-004 | A1 | Microsoft deal 6-K, ex-99.1 | 2025-09-08 | sec.gov/Archives/edgar/data/1513845/.../tm2525580d1_ex99-1.htm | MSFT contract terms, LDs, termination clause |
| SRC-005 | A1 | FY2024 results 6-K | 2025-02-20 | EDGAR (CIK 1513845) | FY2024 $117.5M orig, Q4'24 $37.9M |
| SRC-006 | A2 | Q1 2025 shareholder letter (6-K) | 2025-05-20 | nebius.com IR | Q1'25 ARR $249M |
| SRC-007 | A2 | Meta + NVIDIA partnership PRs | 2026-03-16 | nebius.com/newsroom; nvidianews.nvidia.com | Meta ~$27B; NVIDIA $2B warrant + >5GW |
| SRC-008 | A1 | NVIDIA 13F-HR | 2026-05-15 | sec.gov/Archives/edgar/data/1045810/.../information_table.xml | NVIDIA holds 1,190,476 NBIS Cl A |
| SRC-009 | A1 | Situational Awareness LP 13G | 2026-05-27 | EDGAR (CIK 1513845) | 12,410,060 sh = 5.6% Cl A |
| SRC-010 | B2 | Bloom Energy deal coverage | 2026-05-20 | CNBC / Crypto Briefing | $2.6B / 328MW fuel cells, behind-the-meter |
| SRC-011 | A2 | Nebius newsroom — Finland 310MW | 2026-03-31 | nebius.com/newsroom/nebius-to-construct-310-mw-ai-factory-in-finland | Lappeenranta |
| SRC-012 | A2 | Nebius newsroom — Missouri groundbreaking | 2026-05-12 | nebius.com/newsroom/nebius-breaks-ground...independence-missouri | 1.2GW site, IPL power |
| SRC-013 | A2 | Nebius blog — NJ + Iceland | 2025-03-05 | nebius.com/blog/posts/300-mw-new-jersey-and-iceland-regions | Vineland gas microgrid |
| SRC-014 | B1 | Q1 2026 earnings call transcript | 2026-05-13 | Motley Fool / Investing.com | Volozh/Alonso/Korolenko/Boroditsky quotes; capex $20-25B |
| SRC-015 | B1 | Q3 2025 earnings call transcript | 2025-11-11 | Investing.com / Benzinga | "Capacity is the main bottleneck" |
| SRC-016 | B1 | Volozh "four Cs" interview | 2026-03-27 | Money Times / Oninvest | Transformer/gas-gen shortage quote |
| SRC-017 | A2 | 2024 Sustainability Report | 2025-07-10 | nebius.com/sustainability | 94% low-carbon (pre-US-gas buildout) |
| SRC-018 | B2 | Market data aggregators | 2026-06-18 | stockanalysis.com / MarketBeat / Benzinga | Price, mkt cap, multiples, short interest, PTs |
| SRC-019 | B2 | Morgan Stanley research | 2026-05-14 | TheStreet / Nasdaq / MarketScreener | Equal-Weight, PT $126→$144; −96.8% EBIT (single-sourced) |
| SRC-020 | B2 | HSBC CoreWeave "Reduce" note | 2025-07-17 | Investing.com / MarketScreener | Peer read-across (CRWV, not NBIS) |
| SRC-021 | A2 | nebius.com board / governance | 2026-06-18 (accessed) | nebius.com/board-of-directors | Board, Volozh bio |
| SRC-099 | C | `../../nbis.md` (old detector brief) | 2026-05-04 | companies/nbis.md | Single-video-source narrative; NOT a fact source |

Tier rules live in `../../../sources/source_policy.md`.
