# ISRG Research Status

Ticker: ISRG | As-of: 2026-07-02 | Run: 2026-07-04 | Pipeline: lean-6module-v1.1 | Weights: none

## Honest status: **DECISION_DRAFT** (not COMPLETE)

One-pass live run. Freshness gate PASS (price triple-sourced, $426.01, 0% delta). The verdict is
well-supported: every load-bearing Q1 2026 / FY2025 number is primary (10-Q / earnings release), competitor
status is FDA/company-primary, and the operator picture is proxy/PR-primary. Completeness (~72%) and a few OPEN
items (direct EDGAR full-text, non-GAAP owner-earnings bridge, the *magnitude* of the instrument-life I&A
impact, exact China % of revenue) cap it below COMPLETE. The core call (STARTER, thin-but-positive base IRR) is
robust; the swing factor is the Q2 (2026-07-16) instrument-life/annuity read.

## 11-stage checklist

| # | Stage | File | Status |
|---|---|---|---|
| 0 | Plan / thesis gate | step0_plan.md | DONE |
| 1 | Source register | source_register.md | DONE |
| 2 | Claim ledger | claim_ledger.csv | DONE |
| 3 | Facts (evidence spine, M1) | facts.md | DONE |
| 4 | Raw extracts | raw/ | DONE |
| 5 | Business model + value chain + moat + bottleneck (M2/M3) | business_model.md, value_chain_map.md, moat_map.md, bottleneck_map.md | DONE |
| 6 | Financial reality (M4) | financials/financial_quality.md, model/*.csv | DONE |
| 7 | Operator underwriting (life-arc) | operator_underwriting.md | DONE |
| 8 | Inversion / trap (M5) | inversion_map.md | DONE |
| 9 | Valuation / price / position (M6) | valuation.md, model/scenario_model.csv | DONE |
| 10 | IC panel + memo + decision card | ic_panel.md, decision_card.json/.md | DONE |
| 11 | Monitor + freshness | monitor.md, freshness_check.json | DONE (freshness PASS) |

## Gates NOT yet passed (what would raise to COMPLETE)

- Direct SEC EDGAR full-text 10-Q/10-K extraction (EDGAR HTML 403'd the fetcher; used StockTitan 10-Q mirror +
  SEC-hosted 8-K text via search; numbers corroborated >=2 sources).
- Clean normalized owner-earnings bridge (GAAP $2.28 vs non-GAAP $2.50).
- The *magnitude* of the instrument-life (6→15-use) impact on I&A-per-procedure — the bull/bear crux — is a
  forward unknown; Q2 (2026-07-16) is the read.
- Exact China % of revenue and China-specific tariff dollar impact.
- Independent Checker pass (this is the Runner output; Checker not yet run).

## Final verdict summary

- Business: **exceptional**. New money: **STARTER** (initial ~3-4%). Existing: **HOLD/ADD-on-weakness**. Max
  size: ~8-12% (below top Core tier until Hugo + instrument-life resolve). Buy-below: 8% base IRR already met at
  $426; add ~$412; CORE ~$364.
- Binding constraint: **COMPLETENESS + one open business inflection** (instrument-life I&A + Hugo), NOT price —
  the ~30% de-rate gave a positive base IRR. Diversification value (non-AI-factor) is a real positive.
