# GOOGL Evidence Backlog v2

Last updated: 2026-06-16

Purpose: convert the v2 memo into concrete evidence tasks. Each task should eventually produce raw notes, claim-ledger entries, fact promotions, and memo updates.

---

## P0 - Blocks Before Any Buy Decision

| ID | Task | Output | Status |
|---|---|---|---|
| GOOGL-V2-P0-01 | Pull Q1 2026 earnings call transcript and identify every management comment about AI Search monetization, AI Overviews, AI Mode, and ad load. | `raw/q1_2026_call_ai_search.md` + `claim_ledger_v2_candidates.csv` | v2 output complete; AI RPM remains undisclosed |
| GOOGL-V2-P0-02 | Build Search unit-economics table: paid clicks, CPC, TAC, Search revenue, AI feature penetration, and any disclosed RPM proxy. | `model/search_unit_economics_v2.csv` | v2 output complete; no disclosed AI RPM proxy |
| GOOGL-V2-P0-03 | Build capex bridge: FY2023-FY2026 capex, D&A, assets not in service, leases not commenced, technical infrastructure, and estimated maintenance/growth split. | `model/capex_bridge_v2.csv` + `model/capex_owner_earnings_bridge_v2.csv` | v2 output complete; maintenance/growth split remains OPEN |
| GOOGL-V2-P0-04 | Pull Cloud multi-quarter trend: revenue, operating income, operating margin, backlog/RPO, conversion timing, and commentary on AI workloads. | `model/cloud_quality_v2.csv` + `value_chain_v2.md` | v2 output complete; backlog margin remains OPEN |
| GOOGL-V2-P0-05 | Rebuild owner earnings model with explicit capex branches: growth, defensive, mixed/delay. | `model/owner_earnings_v2.csv` + `model/capex_owner_earnings_bridge_v2.csv` | v2 output complete with branch range |
| GOOGL-V2-P0-06 | Build implied expectations model from current price: required OE CAGR, margin, capex intensity, terminal multiple, share count. | `model/implied_expectations_v2_final.csv` + `valuation_v2.md` | v2 output complete; BUY still blocked by MOS and open evidence |

---

## P1 - Blocks That Improve Confidence

| ID | Task | Output | Status |
|---|---|---|---|
| GOOGL-V2-P1-01 | Pull Alphabet 2025 annual report / 10-K full segment table and validate annual Search, YouTube, Network, subscriptions lines. | `raw/2025_10k_segment_extract.md` | pending |
| GOOGL-V2-P1-02 | Verify Berkshire Q1 2026 Alphabet position and June 2026 private placement terms; separate 13F holdings from financing participation. | `raw/berkshire_google_2026.md` | partially done |
| GOOGL-V2-P1-03 | Verify H&H Q1 2026 GOOG holding and compare with Q4 2025 to calculate share change, not market value change. | `raw/hh_google_13f_delta_2026.md` | partially done |
| GOOGL-V2-P1-04 | Pull DOJ search and adtech case status; classify remedies into fine, behavior remedy, or structural remedy. | `inversion_risk_v2.md` + `monitor-v2.md` | covered in risk/monitor outputs; dedicated raw file still optional |
| GOOGL-V2-P1-05 | Compare Google with MSFT, AMZN, META on AI capex, Cloud margin, ad exposure, and owner earnings pressure. | `peer_profit_pool_v2.md` | v2 output complete |

---

## P2 - Monitoring Blocks

| ID | Task | Output | Status |
|---|---|---|---|
| GOOGL-V2-P2-01 | Set quarterly monitor thresholds for Search growth, paid clicks, CPC, TAC, Cloud margin, capex/OCF, FCF/share, share count. | `monitor-v2.md` | v2 output complete |
| GOOGL-V2-P2-02 | Track AI-native competitors: ChatGPT search, Perplexity, Apple Intelligence, Meta AI, Amazon retail media. | `competitive_monitor_v2.md` | pending |
| GOOGL-V2-P2-03 | Track consumer AI subscriptions and Gemini adoption signals. | `subscription_monitor_v2.md` | pending |

---

## Promotion Rule

No new claim enters `facts.md` unless it has:

1. a stable source URL or local source file;
2. a precise excerpt or table row in `raw/`;
3. a `claim_ledger.csv` entry with source tier and verification status;
4. a clear downstream use in the v2 memo, model, or monitor.
