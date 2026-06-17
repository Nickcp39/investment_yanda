# Progress Note - 2026-06-17

## Scope Preserved

This note preserves the current framework-validation progress before pushing.

Main work completed:

- Updated the interactive framework page so every node can expose execution flow and deliverable templates.
- Built a P1 Lean Case for SNDK as of 2025-06-16 under `backtests/framework_validation/cases/sndk_2025-06-16/`.
- Separated runner-visible files from scorer-only outcome scoring.
- Added `source_completeness_audit.md` after a second source pass.
- Clarified that the SNDK runner verdict is not a current-year new-money view.

## SNDK 2025 Locked Runner Verdict

As-of date: 2025-06-16.

Runner-visible conclusion:

- New-money verdict: STARTER.
- Suggested initial size: 1.5%.
- Max size before confirmation: 3.0%.
- Context label: spinoff_forced_seller + cyclical_inflection.
- M5 veto flag: false.

Important distinction:

- The runner did not say "buy 3% immediately."
- The runner said "start around 1.5%; cap at 3% before margin / cloud-enterprise demand confirmation."

## Evidence Coverage

P1 evidence now includes:

- Nasdaq spin-off / trading notice.
- Sandisk separation and listing releases.
- Sandisk Q3 FY2025 results.
- Sandisk Q3 FY2025 10-Q.
- Sandisk Form 10/A / information statement.
- Sandisk S-1/A resale registration and WDC retained-stake overhang.
- June 2025 secondary offering releases.
- TrendForce NAND / enterprise SSD industry context.
- Micron Q2 FY2025 peer memory-cycle context.
- Local Yahoo chart API quote row for 2025-06-16.

Status:

- Sufficient for P1 Lean Case.
- Not a P2 deep case.

Known gaps:

- Full Q3 FY2025 earnings-call transcript was searched but not integrated because the accessible transcript source was not reliable enough.
- Customer-level hyperscaler NAND procurement truth remains unavailable from public pre-as-of evidence.
- No full NAND ASP model was built.

## Human Judgment Dependency

The SNDK case exposed a pipeline limitation:

AI can find evidence that enterprise SSD / AI storage demand may be improving, but it cannot fully judge future demand durability from public evidence alone.

Proposed control variable:

```text
HJD = Human Judgment Dependency
```

Use:

- HJD is not a seventh module.
- It is a size-control variable across M2-M6.
- If a key future-demand variable is unresolved, the model can allow STARTER but cannot unlock larger size.

SNDK HJD examples:

- Is AI enterprise SSD demand durable or just inventory restocking?
- Will NAND supplier discipline hold after pricing improves?
- Can Sandisk capture the profit pool, or will Samsung / SK Hynix / Micron capture most of it?

Control rule:

```text
target_size = min(model_suggested_size, human_judgment_cap)
```

For SNDK:

- HJD unresolved -> initial size 1.0%-1.5%.
- HJD unresolved -> max before confirmation 3.0%.
- Human or market confirmation required before larger size.

## Files To Commit In This Progress Push

Intended commit scope:

- `backtests/asof_2025_06_16_sndk_pipeline_test.md`
- `backtests/data/asof_2025_06_16_sndk_quotes.csv`
- `backtests/framework_validation/`

Explicitly excluded from this progress push:

- `BTC_analysis_tool/`
- `backtests/cases/mu_2025-03-21/`

