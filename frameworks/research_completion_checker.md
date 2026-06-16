# Research Completion Checker

Purpose: prevent the research process from calling work "complete" before it is actually complete.

This file is a mandatory gate for any company-level "full rerun", "complete memo", "finished research", or "buy-side decision package".

---

## Non-Negotiable Language Rule

Do not say any of the following unless the company-specific completion checker is marked `COMPLETE` and every required gate is checked:

- "完成了"
- "彻底跑完了"
- "完整重跑完成"
- "final memo"
- "full buy-side research complete"

Allowed language when gates are not complete:

- "完成到 P0 / P1 / P2"
- "完成了第一阶段"
- "working memo"
- "initial model pass"
- "draft / incomplete"
- "blocked by these open gates"

---

## Status Labels

| Status | Meaning | What Can Be Said |
|---|---|---|
| `NOT_STARTED` | No real evidence work has begun. | "尚未开始" |
| `SCAFFOLD` | Templates, HTML, or outline exist, but evidence gates are not run. | "搭了框架" |
| `P0_PASS_1` | First critical evidence/model pass exists, but ledger/facts/audit are incomplete. | "P0 第一轮完成" |
| `P1_PARTIAL` | Most modules have evidence, but open blockers remain. | "主体研究部分完成" |
| `DECISION_DRAFT` | Memo exists, but final audit/monitor/verdict gates are incomplete. | "决策草案" |
| `COMPLETE` | All required completion gates are checked. | "完整完成" |

---

## Universal Completion Gates

All boxes must be checked in the company-specific checker before claiming complete.

### A. Scope And Definition

- [ ] Research scope is frozen: ticker, share class, date, decision purpose, time horizon.
- [ ] Completion standard is written before the final answer.
- [ ] The current status label is not stale.

### B. Evidence Engineering

- [ ] Source register has every source used in memo/model.
- [ ] Raw extracts exist for every important claim.
- [ ] Claim ledger is updated with source tier, verification status, and source IDs.
- [ ] Facts file is updated only from verified or clearly marked derived claims.
- [ ] No memo claim appears without either a fact/source ID or explicit `OPEN` label.
- [ ] Stale claims from prior versions are either updated or marked archived.

### C. Ten-Layer Research

- [ ] 1. Direction Selection complete.
- [ ] 2. Business Thesis / Quality Gate complete.
- [ ] 3. Evidence Engineering complete.
- [ ] 4. Accounting Trend Validation complete.
- [ ] 5. Industry / Value Chain complete.
- [ ] 6. Moat / Bottleneck complete.
- [ ] 7. Operator Underwriting complete.
- [ ] 8. Inversion / Risk complete.
- [ ] 9. Valuation / Margin of Safety complete.
- [ ] 10. Decision / Monitoring complete.

### D. Model And Math

- [ ] Revenue driver model is built and tied to evidence.
- [ ] Expense / capex model is built and tied to evidence.
- [ ] Owner earnings model is rebuilt for the current version.
- [ ] Implied expectations model is rebuilt from current price.
- [ ] Scenario outputs reconcile with source data and assumptions.
- [ ] Key formulas and derived figures are auditable.

### E. Open Questions And Blockers

- [ ] Every open question is classified as `blocking`, `monitoring`, or `non-blocking`.
- [ ] Blocking questions cap the verdict explicitly.
- [ ] Non-blocking questions have a reason why they do not block.
- [ ] Evidence backlog is updated with next actions.

### F. Audit And Consistency

- [ ] Internal audit checks stale self-descriptions.
- [ ] File index / README reflects current status.
- [ ] Old versions are marked archive or failed pilot where appropriate.
- [ ] `git diff --check` or equivalent content check is run.
- [ ] Final answer reports the actual status, not a more flattering status.

---

## Required Final Self-Check

Before telling the user the work is complete, answer these in the company-specific checker:

1. What is the exact status label?
2. Which required gates remain unchecked?
3. What evidence would change the status to `COMPLETE`?
4. Are there any stale files still claiming a different status?
5. Is the final answer using allowed language for the status?

If any answer is unclear, the work is not complete.

