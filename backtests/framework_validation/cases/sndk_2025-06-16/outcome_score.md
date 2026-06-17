# SC Outcome Score - SNDK 2025-06-16

This file is scorer-only. It deliberately uses post-2025-06-16 outcome evidence and must not be used by the blind runner.

## 0. Score Verdict

- Case: SNDK as of 2025-06-16.
- QA verdict for runner files: CLEAN.
- Pipeline decision: STARTER, 1.5% initial size, max 3.0% before confirmation.
- Outcome class: extreme winner.
- Score: PASS.
- Size-distance error: 0 for direction, 1 for size conservatism acceptable given uncertainty.

## 1. Outcome Measurement

| field | value |
|---|---|
| As-of price | $44.21 |
| Later comparison anchor | 2026-06-16 local quote row |
| Later price anchor | $1,991.55 |
| Approximate price multiple | 45.05x |
| Approximate return | +4,405% |
| Outcome class | winner |

Outcome price source:

- `backtests/data/asof_2025_06_16_sndk_quotes.csv`

Post-as-of business validation source:

- Sandisk Q3 FY2026 release, 2026-04-30: revenue $5.95B, GAAP net income $3.615B, GAAP diluted EPS $23.03, non-GAAP diluted EPS $23.41, Datacenter revenue $1.467B, and Q4 FY2026 revenue guide of $7.75B-$8.25B.

## 2. Decision Quality

| question | answer | notes |
|---|---|---|
| Did winner receive at least STARTER? | yes | New-money verdict was STARTER. |
| Did pipeline avoid GAAP-loss rejection? | yes | M4 normalized goodwill impairment and focused on margin / cycle confirmation. |
| Was size directionally right? | yes | Small starter was correct given evidence uncertainty. |
| Was dominant module correct? | yes | M2 / M4 / M6 drove the decision, with M5 capping size. |
| Did pipeline chase current-year valuation? | no | The runner did not issue a 2026 new-money verdict. |

## 3. Module Attribution

| module | original signal | hindsight assessment | adjustment hypothesis |
|---|---:|---|---|
| M1 | 0 | Correct; evidence was enough for small size but not high confidence. | Do not use short history as automatic veto. |
| M2 | +2 | Correct; spin-off + AI storage + supply discipline was the key. | Keep spinoff_forced_seller + cyclical_inflection context. |
| M3 | +1 | Correct; Sandisk captured profit pool, but moat was still cyclical. | Avoid calling it a quality compounder too early. |
| M4 | +1 | Correct; GAAP loss was misleading, but confirmation was needed. | Normalize non-cash impairment and cycle position. |
| M5 | -1 | Correct; risks were real but did not justify veto. | Cap size, do not reject. |
| M6 | +2 | Correct; $6.4B equity value allowed asymmetric payoff. | Price / size module should permit starter before perfect evidence. |

## 4. Failure Tags Avoided

- confidence_used_as_veto: avoided.
- trailing_accounting_trap: avoided.
- too_small_missed_asymmetry: avoided.
- valuation_overweighted: avoided.
- inversion_veto_missed: avoided because M5 capped size without firing false veto.

## 5. Results.csv Row

```text
lean_six_module_v0,W_v0,sndk_2025-06-16,spinoff_forced_seller+cyclical_inflection,WINNER,1.5,STARTER,HOLD,STARTER..CORE,0,false,false,"M2/M4/M6","M2/M4/M6",sound,"none","Correct small starter; later outcome validates that uncertainty should have been sized, not vetoed."
```

## 6. Weighting Proposal

Do not tune weights from this single case alone. Tentative rule to test across more cases:

When `spinoff_forced_seller + cyclical_inflection` has:

1. non-cash GAAP distortion,
2. survivable balance sheet,
3. independent industry evidence of supply-demand improvement,
4. forced-seller or holder-base dislocation,
5. explicit add / kill triggers,

the pipeline should allow a 1%-2% starter even before clean trailing owner earnings exist.
