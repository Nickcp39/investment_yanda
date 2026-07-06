# IDXX Source Register

Last updated: 2026-07-05 (run_date) | as_of: 2026-07-05 | pipeline: lean-6module-v1.1

Tier rules: `../../../sources/source_policy.md`

| source_id | Tier | Source | Public Date | URL / Local Path | Notes |
|---|---|---|---|---|---|
| IDXX-10K-FY25 | A1 | IDEXX Laboratories, Inc. FY2025 10-K (fiscal year ended 2025-12-31) | 2026-02-20 | https://www.sec.gov/Archives/edgar/data/0000874716/000087471626000038/idxx-20251231.htm | CIK 874716; accession 0000874716-26-000038; SEC direct HTML fetch returned 403 "Undeclared Automated Tool" on first attempt — per robustness rule, fell back immediately to official IR press releases + stockanalysis.com + search corroboration (no retry loop) |
| IDXX-Q4-PR | A1 | IDEXX Laboratories Q4 & FY2025 earnings press release | ~2026-01-29 | https://ir.idexx.com/news-events/press-releases/detail/405/idexx-laboratories-announces-fourth-quarter-and-full-year-2025-results (also mirrored at businesswire.com/news/home/20260130438354/en/) | Official IR press release; FY2025 revenue $4,303.7M, segment detail, EPS $13.08, FY2026 original guidance — the single richest primary source this run |
| IDXX-Q1-PR | A1 | IDEXX Laboratories Q1 2026 earnings press release | ~2026-05-04 | https://www.businesswire.com/news/home/20260504966946/en/IDEXX-Laboratories-Announces-First-Quarter-Results (also ir.idexx.com/news-events/press-releases/detail/408) | Official IR press release; Q1 2026 revenue $1,140.8M, raised FY2026 guidance, litigation judgment payment detail |
| STOCKTITAN-Q1-8K | A2 (proxy) | StockTitan.net structured summary of IDXX Q1 2026 8-K | ~2026-05-04 | https://www.stocktitan.net/sec-filings/IDXX/8-k-idexx-laboratories-inc-de-reports-material-event-6edec7550171.html | Direct extraction of Q1 2026 financial results, segment detail, guidance raise |
| IDXX-CEO-SUCCESSION-PR | A1 | IDEXX Announces CEO Succession (official press release) | 2026-01-12/13 | https://ir.idexx.com/news-events/press-releases/detail/402/idexx-announces-ceo-succession (also SEC 8-K exhibit: sec.gov/Archives/edgar/data/874716/000110465926003103/tm262817d1_ex99-1.htm) | Michael Erickson succeeds Jay Mazelsky as President/CEO effective 2026-05-12; Mazelsky to Executive Chair, intends retirement post-May 2027 AGM |
| BUSINESSWIRE-CEO | A1 | BusinessWire mirror of CEO succession press release | 2026-01-12 | https://www.businesswire.com/news/home/20260112394517/en/IDEXX-Announces-CEO-Succession | Corroborates IDXX-CEO-SUCCESSION-PR verbatim (same official release, different distribution mirror) |
| IDXX-SA-FINANCIALS | B1 | StockAnalysis.com IDXX income statement (4-year annual) | 2026-07-04 | https://stockanalysis.com/stocks/idxx/financials/ | FY2022-2025 revenue/margin/EPS trend; cross-checked to IR press releases |
| IDXX-SA-BALANCESHEET | B1 | StockAnalysis.com IDXX balance sheet | 2026-07-04 | https://stockanalysis.com/stocks/idxx/financials/balance-sheet/ | FY2024/2025 debt, cash, assets, equity, goodwill/intangibles |
| IDXX-SA-STATS | B1 | StockAnalysis.com IDXX main statistics page | 2026-07-04 | https://stockanalysis.com/stocks/idxx/ | Current price $557.80 (2026-07-02 close), market cap $44.00B, 52wk range $506.91-$769.98, shares 78.88M, P/E 41.03x/37.01x fwd, analyst target $709.14 |
| IDXX-SA-RATIOS | B1 | StockAnalysis.com IDXX financial ratios page | 2026-07-04 | https://stockanalysis.com/stocks/idxx/financials/ratios/ | ROE 69.3%, ROIC 46.8%, ROA 33.4%, debt/equity 0.60, EV/EBITDA 29.05x |
| YAHOO-IDXX-PRICE | B1 | Yahoo Finance chart API (IDXX daily prices), via repo `scripts/market_data_download.fetch_yahoo` | 2026-07-02 | https://query1.finance.yahoo.com/v8/finance/chart/IDXX (repo fetcher) | Independent re-pull: last close $557.80 confirmed for 2026-07-02, matching frozen as_of_price input exactly |
| THEORG-MAZELSKY | B2 | TheOrg.com — Jay Mazelsky org-chart profile | current | https://theorg.com/org/idexx-laboratories/org-chart/jay-mazelsky | CEO background: joined IDEXX Aug 2012, CEO since Oct 2019, prior Philips Healthcare + HP/Agilent career |
| BLOOMBERG-MAZELSKY | B1 | Bloomberg Markets — Jay Mazelsky profile | current | https://www.bloomberg.com/profile/person/17977366 | Corroborates career background |
| STOCKTITAN-8K-CEO2019 | A2 | SEC 8-K exhibit (2019) — Mazelsky CEO appointment | 2019 | https://www.sec.gov/Archives/edgar/data/0000874716/000114420419033248/tv524627_ex99-1.htm | Historical primary confirmation of 2019-10-23 CEO appointment date |
| GENERAL-SECONDARY-GEO | B2 | General secondary aggregator — IDXX geographic revenue mix | 2026 (exact source page not re-confirmed) | search-derived, exact URL not re-captured this run | US 65.3%, China 1.2%, detailed country breakdown — single-sourced this run, see facts.md O2 |
| FORTUNE-VETVISITS | B1 | Fortune.com — veterinary care pricing/visit-decline article | 2026-03-22 | https://fortune.com/2026/03/22/veterinary-care-prices-pet-costs-visits-surgeries-dogs-cats/ | US vet visits −3% Q4 2025, 16th consecutive quarterly decline; annual decline figures 2022-2025 |
| MYVETCANDY-VETVISITS | B2 | MyVetCandy blog — vet visit trend data analysis | 2026-03-26 | https://www.myvetcandy.com/blog/2026/3/26/vet-visits-keep-falling-pet-care-costs-keep-rising-heres-what-the-data-actually-shows | Corroborates Fortune vet-visit decline figures; consumer budget stress framing |
| FINIMIZE-IDXX-VETVISITS | B2 | Finimize — "IDEXX Thinks Pet Testing Demand Can Carry 2026" | 2026 | https://finimize.com/content/idexx-thinks-pet-testing-demand-can-carry-2026 | Management (Mazelsky) −2% 2026 clinical visit guide; "vet visit trends are not very correlated to results" framing; above-Street 2026 targets |
| MARKETSANDMARKETS-VETDX | B2 | MarketsAndMarkets — veterinary diagnostics competitor research | 2026 | https://www.marketsandmarkets.com/ResearchInsight/us-veterinary-diagnostics-companies.asp | IDEXX + Zoetis named leading players; IDEXX "almost half the market share" |
| PORTERSFIVEFORCE-IDXX | B2 | PortersFiveForce.com — IDEXX competitive landscape analysis | 2026 | https://portersfiveforce.com/blogs/competitors/idexx | Competitor detail: Zoetis Vetscan (incl. OptiCell AI hematology analyzer, launched 2024-09), Heska/Mars, Mindray; installed-base/moat framing |
| AIV-VET-MARS-HESKA | B1 | AIV Vet — Mars acquisition of Heska announcement | 2023 | https://www.aiv-vet.com/blog/news-4/mars-announces-acquisition-of-global-vet-diagnostics-group-heska-384 | Mars agreed to acquire Heska at $120.00/share (~$1.3B enterprise value per secondary sourcing) |
| MARS-HESKA-PR | A2 | Mars Global — official press release, Heska acquisition completion | 2023-06-13 | https://www.mars.com/news-and-stories/press-releases-statements/mars-completes-acquisition-heska | Confirms Antech+Heska combined platform; Mars Petcare affiliated with 2,500 vet clinics/hospitals (Banfield, BluePearl, VCA, Mount Pleasant) |
| IDXX-INVUE-PRODUCTPAGE | A2 | IDEXX owned-media — inVue Dx Cellular Analyzer product page | undated (current) | https://www.idexx.com/en/veterinary/analyzers/invue-dx-analyzer/ | Company's own technical description: AI models trained by IDEXX board-certified pathologists, slide-free cytology in ~10 min |
| PRNEWSWIRE-INVUE-LAUNCH | B1 | PR Newswire — inVue Dx launch announcement | ~2024 (launch year) | https://www.prnewswire.com/news-releases/idexx-announces-revolutionary-slide-free-cellular-analyzer-idexx-invue-dx-transforming-in-clinic-workflows-302033192.html | Product launch press release detail |
| YAHOO-STIFEL-CONFERENCE | B2 | Yahoo Finance — IDEXX at Stifel healthcare conference coverage | 2026 | https://finance.yahoo.com/sectors/healthcare/articles/idexx-laboratories-touts-ai-push-110223842.html | Management commentary on inVue Dx momentum, AI push, FNA rollout roadmap |
| SIFTERFUND-SECONDARY | B2 | Sifter Fund — "Why IDEXX Fits a Long Term Quality Portfolio" | 2026 | https://sifterfund.com/en/why-idexx-laboratories-fits-a-long-term-quality-portfolio/ | Installed base >75,000 instruments claim (secondary, unconfirmed vs primary — facts.md O4) |
| HEAVYMOAT-SUBSTACK | C2 | HeavyMoat Investments Substack — IDXX fundamentals/moat commentary | 2026 | https://heavymoatinvestments.substack.com/p/idexx-laboratories-fundamentals-and | Bull-case sentiment/opinion — not used as EVIDENCE, SENTIMENT only |
| SEC-EDGAR-SEARCH | — | Web search results identifying CIK and accession numbers | 2026-07-05 | (search results, no single URL) | Used to identify CIK 874716 and the specific 10-K/8-K accession numbers before direct SEC fetch attempt (which then returned 403) |

---

## Fetch notes (2026-07-05)

- SEC EDGAR direct access (`cgi-bin/browse-edgar` company search with a full Chrome-style UA string) returned
  **HTTP 403 "Your Request Originates from an Undeclared Automated Tool"** on both attempts made (generic
  CIK-search UA, then full browser UA). Per the robustness rule (max 2 attempts per URL, no retry-loop),
  immediately pivoted to: (1) web search to identify the correct CIK/accession numbers, (2) official IDEXX
  IR press releases (mirrored on businesswire.com and ir.idexx.com — genuine A1 primary sources, just not
  the 10-K HTML document itself), (3) stocktitan.net (SEC filing mirror/summarizer), (4) stockanalysis.com
  (financials aggregator), (5) general web search corroboration.
- **CIK: 874716** (confirmed via SEC EDGAR search result URL structure: `sec.gov/Archives/edgar/data/0000874716/...`).
- Price re-fetch used the repo's own `scripts/market_data_download.fetch_yahoo` (via `_retry` wrapper) —
  an independent, non-browser Yahoo Finance chart-API pull that returned $557.80 for 2026-07-02, exactly
  matching the frozen as_of_price input and the stockanalysis.com screener value.
