# GEV Research Status

Last updated: 2026-06-19

Company: GE Vernova (NYSE: GEV) · spun from GE April 2024

Decision question:
1. (LEAD — bottleneck) Is GEV a **durable** toll booth on electrification, or a **cyclical** order surge priced as permanent? Does it set the price or just ride demand?
2. (DECISION) At $1,109.73, is the durable rent enough to justify the multiple? BUY / NO-BUY / WATCH, and at what price/evidence each becomes right.
3. (KILL) What proves the toll-booth thesis wrong?

Current stage: **✅ Blocks 1–9 complete (v1).** Evidence base + 9-block analysis + memo + monitor written. Remaining = a few primary-confirmation gaps (below) and forward quarterly monitoring.

Verdict: **WATCH** (lean STARTER sub-~$950) · info-completeness **78/100** · rank **#2 of 3** in the AI-electricity batch. **LEAD answer:** GEV owns a real, binding bottleneck and sets price like an owner, but the **durable rent is the services annuity** ($87B RPO); the **equipment-pricing premium is a cyclical peak the market capitalizes as permanent.** See `bottleneck_map.md` + `memo-v1.md`.

Read first (IC packet): `memo-v1.md` → `financials/financial_quality.md` (the one-off reconciliation) → `bottleneck_map.md` → `valuation.md`.

---

## Block Checklist — all done

| Block | Question | Artifact | Status |
|---|---|---|---|
| 1. Evidence foundation | What is true? | `source_register.md` (9 src), `claim_ledger.csv` (35 rows), `facts.md` | ✅ done |
| 2. Financial quality | Real economics (segment margins, FCF, Wind) + **one-off normalization** | `financials/financial_quality.md`, `model/` | ✅ done |
| 3. Business model | Equipment vs services mix; the annuity | `business_model.md` | ✅ done |
| 4. Industry / value chain | Where is profit captured? | `value_chain_map.md` | ✅ done |
| 5–6. Moat / bottleneck (LEAD) | Durable rent or cyclical? | `moat_map.md`, `bottleneck_map.md` | ✅ done |
| 7. Operator | Capital allocation post-spin | `operator_underwriting.md` | ✅ done |
| 8. Inversion | How does it fail? (incl. Wind) | `inversion_map.md` | ✅ done |
| 9. Valuation | Priced for execution? (clean-multiple bridge) | `valuation.md`, `model/scenario_model.csv` | ✅ done |
| 10. Decision / monitor | WATCH + triggers | `memo-v1.md`, `monitor.md` | ✅ done (postmortem stub — pending outcome) |

Raw research digests (Block-mapped): `raw/research_2026-06-19_L3-4_financials.md`, `..._L4_business_model_services_annuity.md`, `..._L5-6_moat_bottleneck.md`, `..._L7-8_operator_inversion.md`, `..._L9_valuation.md`.

---

## Source confirmation (this run)

- **S3 (Q1'26 call)** and **S4 (Dec 2025 investor update)** re-confirmed via WebFetch 2026-06-19 — load-bearing numbers (100 GW, +10–20% pricing, $42B Electrification backlog, $4.5B M&A gains, $5.3B WC benefit, $4.8B FCF, dividend/buyback, 2028 targets rev $52B / 22% / 22% / 6%) all match the evidence pack.
- **S5 (Q1'26 PR PDF)** returned binary on fetch → figures cross-read from S2/S3.
- One reconciliation: the call states a **$5.3B working-capital benefit** and **$4.5B M&A gains**; the pack cited a **+$5.6B contract-liability inflow** and **~$4.0B Prolec + $0.33B Proficy**. Reconciled in `claim_ledger.csv` (C006/C007) — same phenomena, slightly different line cuts; conclusion unchanged.

## Open Questions (primary-confirmation gaps — do not block the conclusion)

- [ ] **Reservation-fee / cancellation terms** — undisclosed; governs the durability test (kill a). Pull from 10-Q notes when available.
- [ ] **GEV-specific *heavy-duty* GT share** vs precise Siemens/Mitsubishi split — only ~two-thirds-combined and ~18.5%-of-all-turbines sourced (S7, MED).
- [ ] **Clean normalized-FCF bridge** stripping advance-payment timing — needed to tighten EV/FCF (C007).

## Pollution Checks

- [x] No KOL/video used as a fact (S99 reserved, empty).
- [x] Fact / interpretation / assumption separated ([PRIMARY]/[SECONDARY] tags; claim_ledger status grading).
- [x] Every load-bearing number carries a source ID (claim_ledger 35 rows; facts all cite claim_id/source).
- [x] Every thesis variable has a kill condition (`monitor.md` + `inversion_map.md`).
- [x] memo does not run ahead of evidence (WATCH rests on valuation + inversion + bottleneck).
- [x] ⚠️ One-off distortion carried through `financials/` → `valuation.md` → `model/`.

## Consistency with pre-existing files

`step0_plan.md`, `facts.md`, `memo-v1.md` were already written and are **preserved unchanged** — this run's modules are consistent with all three (same WATCH verdict, same 78/100, same #2-of-3, same kill-criteria status, same one-off framing).
