# Inversion / Risk Map — NBIS

Last updated: 2026-06-18

Source base: operator/inversion raw (SRC-001, SRC-004, SRC-014, SRC-019, SRC-020). "Invert" — how does the bull thesis die?

## If I Wanted This Company To Fail

| Attack path | Mechanism | Evidence today | Early warning | Permanent damage? |
|---|---|---|---|---|
| **A. Build-out / delivery slip** | Miss energization schedule → miss revenue → trigger MSFT late-delivery LDs/termination (C015) | Active power only ~170MW YE2025; transformer/gen shortages (C020, C022) | First disclosed missed/renegotiated tranche; active-MW stall | Medium — refunds + impaired contract-collateralized debt |
| **B. Customer churn / clawback** | MSFT/Meta build own capacity or cut orders; contract concentration | MSFT precedent of walking from ~2GW 3rd-party capacity (2025); HSBC CRWV "Reduce" read-across (C041) | MSFT/Meta capex-guide cut; non-renewal language | High — backlog is the whole thesis |
| **C. GPU depreciation shock** | B200→GB300→Rubin cadence destroys residual value faster than 5-yr schedule | NBIS extended life 4→5yrs into faster cadence; Hopper rents −28% YoY (C011) | 2nd life extension; falling revenue/MW; impairment | High — write-downs + margin reset |
| **D. Financing/dilution squeeze + capex air-pocket** | $20–25B capex vs ~−$3.7B FCF; demand wobble pulls prepayment/debt funding | +27% dilution; capex raised; FCF deeply negative (C038, C010) | Deferred-revenue growth stalls; ATM activated; convert terms worsen | High — forced dilution at low price |
| **E. Hyperscaler in-house silicon** | TPU/Trainium/Maia commoditize Nvidia-rental neoclouds | Anthropic up to 1M TPUs; custom-ASIC share rising | Inference migrating off Nvidia; price/GPU-hr decline | Medium — structural 2027+ |
| **F. Russian-legacy / regulatory tail** | Sanctions/indemnity surprise; data-sovereignty | Volozh delisted; Trade Controls Policy; NVIDIA is investor | New sanctions action; undisclosed indemnity surfaces | Low–Medium — mostly reputational now |

## Risk Types

| Risk | Short-term volatility | Permanent impairment | Monitoring metric |
|---|---|---|---|
| Business model disruption | Med | Med (E) | inference-vs-training mix; ASIC adoption |
| Competition / commoditization | High | Med–High (B, E) | price per GPU-hr; gross margin trend |
| Regulation / legal | Low | Low–Med (F) | sanctions news; 20-F contingencies |
| Capital intensity | High | High (D) | capex/revenue; FCF; deferred-rev growth |
| Management / culture | Low | Low–Med | comp design; conglomerate focus |
| Balance sheet | Med | Med (D) | net debt (principal); convert overhang |
| Valuation | **High** | — | EV/forward-sales vs growth realization |

## Kill Criteria (→ feed `monitor.md`)

We should downgrade or TRIM/EXIT if:

- [ ] **Active power / connected MW stalls** vs the 800MW–1GW YE2026 connected target, OR a **Microsoft/Meta tranche is publicly missed/renegotiated** (paths A+B).
- [ ] **Customer concentration confirmed >60% with a take-back clause** (resolves C014/C015 to the bad case), OR an anchor cuts/pauses its capex.
- [ ] **Second depreciation-life extension or a GPU impairment** appears in a filing; or realized revenue/MW declines sequentially (path C).
- [ ] **Funding flips from customer-funded to dilution-funded** — deferred-revenue growth stalls **and** ATM/equity issuance accelerates while FCF stays deeply negative (path D).
- [ ] FY2026 capex confirmed at the **$31–35B** high end without commensurate active-MW/ARR conversion (capital sink).

## Disconfirming Evidence (what would make the bear case wrong)

- [ ] Active power scales on/ahead of plan AND a **third large non-MSFT/Meta anchor** signs (demand breadth, path B refuted).
- [ ] Capex/revenue ratio **falls** while ARR conversion holds (capital intensity normalizing, path D refuted).
- [ ] Realized price per GPU-hr **holds or rises** through the GB300/Rubin transition (path C refuted).
- [ ] Clean ICFR opinion under Deloitte for FY2026 (accounting-quality flag cleared).

## The 3 that matter most (ranked)

1. **D — financing/dilution squeeze meets a capex air-pocket** (arithmetic, not narrative; the model only works while demand funds it).
2. **A/B — delivery slip triggers the Microsoft contractual clawback** (the clause is explicit; concentration is real).
3. **C — GPU depreciation shock** (NBIS's own 4→5yr change makes this self-inflicted-risk-visible).
