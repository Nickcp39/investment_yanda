# Source Register

Purpose: assign stable source IDs before claims enter `claim_ledger.csv`.

| source_id | Tier | Source | Date | URL / Local path | Notes |
|---|---|---|---|---|---|
| SRC-001 | A1 | Latest 10-K | YYYY-MM-DD | | Primary filing |
| SRC-002 | A1 | Latest 10-Q / earnings release | YYYY-MM-DD | | Primary filing |
| SRC-003 | A1 | Proxy statement | YYYY-MM-DD | | Governance / compensation |
| SRC-004 | B1 | Earnings transcript | YYYY-MM-DD | | Management commentary |
| SRC-005 | B2 | Independent industry source | YYYY-MM-DD | | Context only |

Tier rules live in `../../sources/source_policy.md`.

