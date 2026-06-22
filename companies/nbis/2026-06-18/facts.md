# Facts Foundation — NBIS

Last updated: 2026-06-18

Rule: this file is for **audited facts only** (claim_ledger status = `verified`). Inferred, disputed, promotional, or secondary-only points stay in `claim_ledger.csv`. Each row cites a claim_id / source_id.

## Company Identity

| Item | Fact | source_id |
|---|---|---|
| Legal name | Nebius Group N.V. | SRC-001 |
| Ticker | NBIS (Nasdaq) | SRC-001 |
| Exchange / domicile | Nasdaq; Amsterdam (Dutch N.V.); ex-Yandex N.V. | SRC-001 |
| CIK | 0001513845 | SRC-001 |
| Reporting basis | **U.S. GAAP** (foreign private issuer; files 20-F / 6-K, no 10-Q) | SRC-001 |
| Relisting | Nasdaq trading resumed 2024-10-21 after Russia-asset divestiture (closed 2024-07-15) | C037 |

## Business (one line)

NBIS builds and operates **AI data centers** (GPU "neocloud") — **it does not build or own power plants** (C028). Core = AI Cloud GPU compute sold largely via multi-year anchor contracts; plus AI Studio platform and non-core stakes (Toloka, ClickHouse, Avride, TripleTen).

## Key Financial Facts (US GAAP, USD)

| Metric | Period | Value | claim_id | Notes |
|---|---|---:|---|---|
| Revenue | FY2025 | $529.8M (+479%) | C001 | |
| Revenue | Q1 2026 | $399.0M (+684%) | C003 | |
| Revenue | FY2024 | $117.5M orig / $91.5M restated | C002 | basis differs (Toloka) |
| ARR (exit) | Mar 2026 | $1.9B | C004 | **unaudited**, last-month×12 |
| Capex | FY2025 | $4,066M (~7.7× revenue) | C005 | |
| Capex | Q1 2026 | $2,472.9M | C006 | |
| Adj. EBITDA (group) | FY2025 / Q1'26 | −$64.9M / +$129.5M | C007 | first +Q = Q4'25 |
| Pre-tax net income | FY2025 | +$13.8M | C008 | **only** due to +$598.9M ClickHouse gain |
| Implied FCF | FY2025 | ≈ −$3.66B | C010 | OCF inflated by prepayments |
| Cash | Mar 31 2026 | $9,298.2M | C009 | |
| Debt (carrying) | Mar 31 2026 | $8,450.4M (all convertibles) | C009 | principal $10,041.8M |
| Capital raised since relisting | 2024-10→2026-03 | ~$12.5B+ | C038 | |
| Basic share dilution | Sep'24→Mar'26 | +~27% (199.3M→253.9M) | C038 | + convert/warrant overhang |

## Market Snapshot (LIVE data — as_of 2026-06-18; see `freshness.json`)

| Item | Value | source_id | Notes |
|---|---:|---|---|
| **Share price (as_of close)** | **$286.69** | SRC-018 | last close ≤ 2026-06-18 (Yahoo adjclose); re-verified vs stockanalysis + websearch (0.0% delta) |
| Market cap (basic) | ~$72.79B | SRC-018 | 253.9M basic × $286.69 = $72,790,591,000 |
| Market cap (diluted wtd-avg) | ~$88.58B | SRC-018 | 308.97M × $286.69 |
| Enterprise value (basic) | ~$71.9B | SRC-018 | + carrying net cash ~+$0.85B |
| 52-week range (intraday) | $43.89 – $298.80 | SRC-018 | price is **−4.0% off the 52wk high** (ATH region; Nasdaq-100 inclusion 6/22) — *priced for perfection* |
| LIVE-qualitative (contracts/power/ARR) | see `freshness.json` | SRC-001/002/004/007 | MSFT $17.4→19.4B / Meta ~$2.88B + ~$27B; >3.5GW contracted (>75% owned); ~170MW active YE2025; YE26 exit-ARR target $7–9B |

## Power / Capacity Facts (LEAD QUESTION)

| Item | Period | Fact | claim_id |
|---|---|---|---|
| Contracted power | Q1 2026 | **>3.5 GW** (YE2026 guide >4 GW); **>75% owned** | C018 |
| Power stages | — | contracted → connected → active; connected target 800MW–1GW YE2026 | C019 |
| Active power | YE2025 | **~170 MW** (no Q1'26 figure disclosed) | C020 |
| Stated bottleneck | Q3'25 | management: **"capacity is the main bottleneck"** | C021 |
| Hard sub-constraint | 2026-03 | shortages of **transformers and gas generators** (long-lead electrical) | C022 |
| GPU supply | 2026-03 | **not** the constraint anymore (de-risked via NVIDIA) | C023 |
| Demand | Q1'26 | **not** a constraint — sold out, "4+ customers per GPU", raised prices | C029 |
| Power model | — | grid/utility power + behind-the-meter on-site gas (NJ ~85% gas; partner-built/operated) | C024, C028 |

## Contracts / Backlog / Revenue-Quality Facts

| Item | Fact | claim_id |
|---|---|---|
| Microsoft | up to $17.4B (→$19.4B) through Oct 2031; ~$6.96B upfront | C013 |
| Meta (1st) | ~$2.88B 5-yr (Dec 2025), take-or-pay | C047 |
| Meta (2nd) | up to ~$27B (Mar 2026): $12B firm Vera Rubin from 2027 + **$15B optional/resaleable** | C047 |
| **RPO (audited metric)** | **$33,585M at Q1 2026** (from $21,333M YE2025) | C043, C044 |
| "Backlog" (~$46–50B) | **media sum of deal ceilings, NOT a company figure** — use RPO | C045 |
| Deferred revenue | $4,778M at Q1 2026 (from $1,578M YE2025); +$3.2B prepayments in Q1 | C046 |
| **Contract structure** | **take-or-pay** (customer pays irrespective of utilization) **+ NBIS delivery obligation** (customer gets service-credit/termination + LDs if NBIS misses) — **resolved, not contradictory** | C014, C015 |
| Customer concentration | MSFT+Meta ≈ ~90%+ of contracted backlog; **exact % not disclosed** | C051 |
| Demand breadth | 25+ named non-anchor customers; self-serve pipeline +~3.5× QoQ; **no $ values disclosed** | C048 |
| Revenue mix | AI Cloud ~98% of group rev; AI Studio/Token Factory not separately disclosed | C049 |

## Governance Facts

| Item | Fact | claim_id |
|---|---|---|
| Founder / controller | Arkady Volozh — ~52–55% **voting** on ~11–13% **economic** (Class B 10 votes, LASTAR Trust) | C035 |
| Structure | Dual-class; Nasdaq "Controlled Company" | C035 |
| Incentive metrics | share-price/equity-driven; **no disclosed ROIC/capex-efficiency hurdle**; FY25 SBC $83.2M | C036 |
| NVIDIA stake | 1,190,476 Cl A (13F) **+** $2B pre-funded warrant (21.07M sh, not yet in 13F) | C034 |

## Accounting Red Flags (verified)

- **Depreciation life extended 4→5 yrs** (eff. Jan 1 2026), −$167.6M FY2026 dep — same year as a fixed-asset material weakness (C011, C012).
- **Adverse ICFR two years running**; open material weaknesses in PP&E and TripleTen rev-rec; auditor Reanda → Deloitte (C012).
- Net income flattered by a $598.9M **non-cash** ClickHouse mark (C008).

## Open Fact Gaps (not yet promotable — see claim_ledger / Open Questions)

- [x] ~~MSFT/Meta take-or-pay vs terminable~~ — **RESOLVED**: take-or-pay (customer-side) + delivery obligation w/ termination/LD (NBIS-side); not contradictory (C014/C015).
- [x] ~~Business-model / non-anchor customer detail~~ — **DONE** (2026-06-18 agent; see `business_model.md`, raw L4 files).
- [ ] FY2026 capex actual ($20–25B vs $31–35B) — C032/C033; await Q2 2026 6-K.
- [ ] Q1'26 **active power (MW)** — withheld by company (last figure ~170MW YE2025).
- [ ] Customer concentration **exact %** (top-1/top-5) — disclosure exists in 20-F XBRL but not retrieved; manual pull needed.
- [ ] Russia-divestiture indemnities / contingent liabilities (C037).
