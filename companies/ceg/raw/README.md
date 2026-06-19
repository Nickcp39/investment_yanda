# Raw Source Notes — CEG

This folder holds original-source extracts and neutral research digests for the CEG case.

Rules (same as the template / NBIS case):

- One file per research block (mapped to a pipeline layer), named `research_2026-06-19_L<block>_<topic>.md`.
- Preserve exact source IDs (S1–S12, see `../source_register.md`), dates, and URLs.
- Separate quoted/extracted facts ([PRIMARY]/[SECONDARY]) from analyst comment.
- Do **not** write investment conclusions here — conclusions live in the module files and `../memo-v1.md`.
- Every load-bearing number must be promoted to `../claim_ledger.csv` and `../facts.md` before any module/memo uses it.

## Block inventory (this run)

| File | Layer | Topic | Status |
|---|---|---|---|
| `research_2026-06-19_L3-4_financials.md` | L3-4 | FY2025 / Q1'26 financials, PTC floor, leverage, capital return | digest |
| `research_2026-06-19_L4_business_model_value_chain.md` | L4 | Merchant generation model + hyperscaler-PPA value chain | digest |
| `research_2026-06-19_L5-6_moat_bottleneck.md` | L5-6 | Un-buildable carbon-free baseload; FERC + Calpine + PPAs | digest |
| `research_2026-06-19_L6_LEAD_scarcity_rent.md` | L6 | **LEAD** — is the scarcity rent durable or priced + FERC-hostage? | digest |
| `research_2026-06-19_L7-8_operator_inversion.md` | L7-8 | Dominguez capital allocation; the 5 pre-registered kills | digest |
| `research_2026-06-19_L9_valuation_market.md` | L9 | Multiples, peer comp, analyst targets, scenarios | digest |

## Provenance caveat

This case was **decomposed from a completed Block-1 evidence pack** (the research was already done). These raw files therefore reproduce the pack's findings grounded in `../source_register.md`, rather than re-running a fresh web sweep. Two primary release URLs (S1 FY2025, S2 Q1'26) returned HTTP 404/410 on automated re-fetch 2026-06-19; their figures are carried at pack confidence and flagged for re-confirmation against the SEC-filed 10-K/10-Q at next review. Items the pack itself could not verify (Microsoft PPA price; post-Calpine net-debt/EBITDA; any new post-Meta PPA) are carried as UNVERIFIED throughout.
