# Lookahead Checker — As-of Integrity Gate (v1, rough)

这是 as-of 回测的"防穿越"检查器规格——保证一个 case 的材料/决策**只用了截止日之前的信息**,且材料包里不含任何决策/结果。Generalizes the Lookahead Auditor role (`PROTOCOL.md` §3) into an actionable checklist. Run it as an independent agent (preferred) or manually.

## When to run

1. **After each material pack is collected** (this batch) — gate before the pack is marked test-ready.
2. **Again on the full P1 case** before scoring a blind test (decision included).

## Verdict

- **CLEAN** — no post-cutoff data, no outcome leakage, (material packs) no decision present.
- **CLEAN-WITH-NOTES** — only trivial, non-load-bearing issues; safe to proceed after the noted fixes.
- **LEAK** — any load-bearing post-cutoff fact, or (material pack) a decision/outcome is present. **A LEAK voids the pack** until fixed.

Output: write `lookahead_audit.md` (decision case) or `material_audit.md` (material pack) into the case folder, in the format of `cases/sndk_2025-06-16/lookahead_audit.md` (Audit Verdict · Source Date Check table · Claim Traceability · Outcome-Aware Language · Post-Cutoff Intrusion · Evidence Misuse · Decision).

## Checklist

1. **Source-date check** — every `sources_used.csv` row has `public_date ≤ as_of`. Web-verify the most-recent and highest-risk rows (don't trust the CSV's self-reported date). Flag any source after as-of.
2. **Claim traceability** — load-bearing claims in the pack trace to an allowed `source_id`.
3. **Outcome-aware language** — scan for hindsight phrasing ("later", "subsequently", "as we now know", "went on to", "rallied/collapsed to") and any post-as-of price.
4. **Post-cutoff fact intrusion** — go through the per-case forbidden registry below, one item at a time; each must be ABSENT.
5. **Evidence misuse** — KOL / social / video used only as a lead, never as core proof; company optimistic framing not stated as verified fact.
6. **(Material packs only) No decision / no outcome** — the pack must contain NO buy/sell verdict, NO `decision_card`, NO thesis/valuation that pre-empts the future blind test. Extracts must be neutral.

## Per-case forbidden registry (as_of + key post-cutoff traps to catch)

| case | as_of | forbid anything after | high-risk traps to specifically check are ABSENT |
|---|---|---|---|
| aapl_2016-05-12 | 2016-05-12 | 2016-05-12 | Berkshire's Apple stake (Q1'16 13F filed ~2016-05-16 → **out**), AirPods (Sep 2016), iPhone 7 and later, any Services-boom narrative, FY2016 H2+ results, the multi-year price appreciation |
| intc_2024-08-02 | 2024-08-02 | 2024-08-02 | any post-crash price recovery / "later surge", Gelsinger departure (Dec 2024) + new CEO, 18A ramp / foundry customer wins, US-government / CHIPS equity stake, ANY 2024-H2 / 2025 / 2026 development |
| dis_2021-11-11 | 2021-11-11 | 2021-11-11 | 2022 stock decline, Chapek ouster / Iger return (Nov 2022), widening DTC losses 2022-23, price hikes / password-sharing crackdown, FY2022+ results |
| pfe_2022-02-08 | 2022-02-08 | 2022-02-08 | 2022-24 COVID-revenue collapse, Seagen acquisition (2023), later guidance cuts, the fall to ~$25, post-date patent-cliff realizations |
| pypl_2021-07-29 | 2021-07-29 | 2021-07-29 | Pinterest acquisition rumor (Oct 2021), 2022 guidance cuts / user-growth deceleration, the stock collapse, Alex Chriss CEO (Sep 2023), the 2026 ~$43 price |
| nvda_2023-05-25 | 2023-05-25 | 2023-05-25 | the 10:1 split (Jun 2024), the run to $1T→$3T, FY2024/FY2025 results, Blackwell, any post-print rally beyond 5/25, the Q1 FY24 10-Q filed 2023-05-26 (one day after → out) |
| meta_2022-11-10 | 2022-11-10 | 2022-11-10 | the 2023 "Year of Efficiency" (Feb 2023), the recovery to $300→$400+, FY2022 full-year results (reported Feb 2023), 2023+ results, later Reality Labs losses, the AI-capex pivot |
| amzn_2023-02-03 | 2023-02-03 | 2023-02-03 | the 2023 recovery to $180+, AWS re-acceleration, the March-2023 additional layoffs, Q1'23 results (late Apr 2023), FY2023+ results, the Rivian-mark recovery |
| intc_2021-04-23 | 2021-04-23 | 2021-04-23 | the entire post-2021 decline, the 2023 dividend cut, Gelsinger departure (Dec 2024), 18A / foundry-customer outcomes, the fall to ~$20s, the Mercury Research Q1'21 share report (~2021-05-09 → out), any post-2021 results |
| googl_2024-06-14 | 2024-06-14 | 2024-06-14 | the +111% run to ~$373, the DOJ search-monopoly liability ruling (Aug 2024), Q2'24+ results, Anat Ashkenazi's actual CFO performance (her 2024-07-31 start was pre-announced = known; her results = out), any 2025 development |
| mu_2025-03-21 | 2025-03-21 | 2025-03-21 | the post-as-of HBM-ramp outcome, the run / drawdown after 3/21, Q3 FY2025+ results, any 2025-H2 / 2026 development |

Extend this registry as new cases are added.

## How to invoke (checker agent prompt, sketch)

```
You are the Lookahead Checker for <case_id>. Read its pack (case_control, sources_used,
raw_extracts, evidence_spine[, decision files if present]) + this LOOKAHEAD_CHECKER.md.
Run the 6-point checklist. Web-verify doubtful source dates. Apply the per-case forbidden
registry row for <case_id>. Write <material_audit.md|lookahead_audit.md> with verdict
CLEAN / CLEAN-WITH-NOTES / LEAK and the standard tables. Return a one-line verdict + issue count.
```

## Notes

- v1 / rough — refine thresholds and extend the registry after the first batch is audited.
- The checker must be an **independent** pass (a different agent than the collector/runner) — that independence is the whole point (see the NBIS case, where the checker overruled the orchestrator's wrong leak suspicion).
