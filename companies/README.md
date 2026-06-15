# Companies

This folder holds company-specific research. Each real company should live in its own ticker folder, for example:

```text
companies/googl/
companies/mu/
companies/circle/
```

Canonical template:

- `companies/_company_research_template/`

Pilot example:

- `companies/googl/`

## Folder Rules

1. Do not put new company memos directly under `companies/`.
2. Create or copy a ticker folder first.
3. Keep raw material, claim ledger, facts, analysis, valuation, and final memo separate.
4. KOL/video notes can inform questions, but cannot become facts without primary-source support.
5. `memo-v1.md` is written last.

## Standard Company Folder

```text
companies/<ticker>/
  README.md
  research_status.md
  step0_plan.md
  source_register.md
  raw/
  claim_ledger.csv
  facts.md
  financials/
  model/
  business_model.md
  value_chain_map.md
  moat_map.md
  bottleneck_map.md
  operator_underwriting.md
  inversion_map.md
  valuation.md
  memo-v1.md
  monitor.md
  postmortem.md
```

## Evidence Promotion Rule

```text
source -> raw note -> claim_ledger.csv -> facts.md -> analysis module -> memo-v1.md
```

Anything that skips this path is treated as an opinion, not a fact.

