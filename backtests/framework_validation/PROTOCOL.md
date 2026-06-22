# Lean Framework Validation Protocol

Status: `DESIGN - NOT YET RUN`
Updated: 2026-06-16

This protocol replaces the earlier "run every company through 10 separate
layers" operating style. The 10 old capabilities are still represented, but the
runner works through six compact decision modules so the process does not turn
into a document factory.

The validation objective remains the same: run blind historical cases using
only information public as of a frozen date, lock the decision, then score
whether the pipeline gave the right size and the right reason.

---

## 0. Core Design

The pipeline under test is:

```text
theme first -> mechanism second -> ticker third -> evidence -> price -> size
```

Meigu Touziwang / TradesMax-style work is absorbed into the core as a direction
and mechanism discipline:

- find the live theme or dislocation;
- identify the bottleneck or profit-pool shift;
- name the catalyst and one key metric;
- then verify with dated primary and secondary sources;
- only then decide price and position size.

It is not allowed to become an extra standalone layer.

---

## 1. Six Modules Under Test

| Module | Role | Old Layers Absorbed |
|---|---|---|
| M1. Evidence Spine | confidence | Evidence Engineering |
| M2. Theme / Mechanism Thesis | context + conviction | Direction, Business Thesis, narrative, first principles |
| M3. Profit Pool / Durability | conviction | Value Chain, Bottleneck, Moat, Operator |
| M4. Financial Reality | conviction or warning | Accounting Trend, normalized owner earnings, cycle position |
| M5. Inversion / Trap Test | risk or veto | Inversion / Risk |
| M6. Price / Position / Monitor | price + output | Valuation, MOS, Decision, Sizing, Monitoring |

Each module must emit a signal. A module that cannot change the final size is
not doing useful work.

---

## 2. No-Lookahead Rules

Each case has a frozen `as_of` date.

Allowed evidence, if public date is on or before `as_of`:

- SEC filings, 10-K, 10-Q, 8-K, proxy, investor deck.
- Earnings releases and official call transcripts.
- Historical price, market cap, and share count.
- Dated news, reputable media, analyst headlines, and market narrative.
- Local notes or videos only as topic leads or sentiment, never as final proof.

Forbidden before the locked verdict:

- Any filing, price, product update, guidance, news, or stock performance after
  the as-of date.
- Later guru or institutional actions.
- Outcome-aware language such as "as we know it later rallied".

Every load-bearing claim must appear in `sources_used.csv` or be traceable to a
source ID in the module files.

---

## 3. Agent Roles

### Runner

Inputs:

- ticker;
- as-of date;
- this protocol;
- the lean material template;
- permission to fetch only evidence public on or before the as-of date.

The Runner must:

- produce the P1 Lean Case files in `COMPANY_MATERIAL_TEMPLATE.md`;
- lock `decision_card.json`;
- not score the outcome;
- write a `runner_dissent` field if the mechanical pipeline result feels wrong.

### Lookahead Auditor

The Auditor checks:

- all source dates;
- no post-as-of facts;
- no outcome-aware phrasing;
- whether social/KOL material was treated only as a lead unless verified.

Output: `CLEAN` or `LEAK`. A leaked case is void.

### Scorer

The Scorer receives the locked Runner output and the sealed case label.

The Scorer judges:

- size-distance error;
- whether the right module drove the decision;
- whether a veto should have fired;
- whether the pipeline missed a winner, walked into a trap, or sized correctly.

### Synthesis

The Synthesis agent aggregates all cases:

- confusion matrix;
- size-distance errors;
- dominant module errors;
- failure tags;
- weight and gate patch recommendations.

---

## 4. Runner Output Schema

**Provenance (mandatory).** Every card MUST stamp `pipeline_version` and `weights_version` — the current
active ids from [`VERSIONS.md`](VERSIONS.md) — plus `run_date` (the lock date, distinct from `as_of`). The
same two ids are echoed into the `results.csv` row at scoring time and MUST match. **A run whose version is
not recorded on its card is void / non-comparable.**

**Freshness (mandatory, v1.1).** Every live dossier — and every backtest case — MUST carry a `freshness.json`
manifest (every LIVE datum with ≥2 independent sources) AND a committed `freshness_check.json` produced by
[`scripts/verify_freshness.py`](../../scripts/verify_freshness.py) with `status=="PASS"`. **A card whose freshness
check is absent, BLOCK, or UNVERIFIABLE is void / non-comparable — exactly as with a missing version stamp.**
`as_of_price` is the single source of truth and MUST be byte-identical wherever it appears. LIVE data (price,
market cap, 52-week band, shares, plus export-control / litigation / guidance) is re-verified mechanically against
≥2 independent sources at lock time — **not by eye, and not by a date-only "looks current" check** (that is the
hole INC-001 exploited). LIVE vs FILED decay class is defined in [`sources/source_policy.md`](../../sources/source_policy.md).

Every Runner must produce `decision_card.json`:

```json
{
  "ticker": "",
  "as_of": "",
  "pipeline_version": "",
  "weights_version": "",
  "run_date": "",
  "context_label": "",
  "as_of_price": 0,
  "as_of_market_cap": 0,
  "module_signals": [
    {
      "module": "M2 Theme / Mechanism Thesis",
      "role": "context | conviction | risk | price | confidence",
      "signal": 0,
      "confidence": "low | med | high",
      "finding": "",
      "drivers": ["source_id"]
    }
  ],
  "business_verdict": "bad | uncertain | good | exceptional",
  "new_money_verdict": "REJECT | WATCH | STARTER | CORE",
  "existing_position_verdict": "EXIT | TRIM | HOLD | ADD",
  "suggested_initial_size_pct": 0,
  "suggested_max_size_pct": 0,
  "buy_below_price": 0,
  "starter_zone": "",
  "add_zone": "",
  "trim_or_no_chase_zone": "",
  "binding_constraint": "",
  "kill_criteria": [""],
  "runner_dissent": "",
  "sources_used": [
    {"source_id": "", "public_date": "", "url_or_path": ""}
  ]
}
```

Signal scale:

```text
+2 = strongly supports ownership / size increase
+1 = mildly supports ownership
 0 = neutral or not applicable
-1 = warning
-2 = strong warning or veto candidate
```

---

## 5. Sealed Case Label Schema

The Runner never sees this.

```json
{
  "case_id": "googl_2024-06-14",
  "mechanical_label": "WINNER | TRAP",
  "context_label": "quality_compounder",
  "dominant_modules": ["M2", "M3", "M6"],
  "veto_expected": false,
  "correct_size_band": "STARTER..CORE",
  "key_variable": "",
  "outcome_window": "12m | 24m | 36m",
  "outcome_note": ""
}
```

---

## 6. Scoring Rubric

Score size, not just direction.

| Outcome | Pass | Partial | Fail |
|---|---|---|---|
| Winner | `STARTER` or `CORE`, or explicit structured starter. | `WATCH` but names the correct key variable and clear buy/add trigger. | `REJECT`, or `WATCH / 0%` with avoid framing. |
| Trap | `REJECT`, or `WATCH` with correct structural decline diagnosis. | `WATCH` for weak or incomplete reason. | `STARTER` or `CORE`. |

Reasoning score:

```text
sound = correct key variable, correct module dominance, no lookahead
shallow = direction acceptable but mechanism weak
wrong_reason = outcome accidentally right but mechanism wrong
```

Size-distance score:

```text
0 = within correct band
1 = one band too small or too large
2 = two bands away
3 = opposite action, e.g. buy trap or reject winner
```

---

## 7. Round 1 Case Matrix

Runner-visible:

| # | Ticker | As-of Date | Anchor |
|---|---|---|---|
| 1 | NVDA | 2023-05-25 | Q1 FY2024 print; guidance shock |
| 2 | META | 2022-11-10 | Q3 2022 plus 11,000-job layoff / cost discipline |
| 3 | GOOGL | 2024-06-14 | post Q1 2024, same anchor as old backtest |
| 4 | AMZN | 2023-02-03 | Q4 2022; AWS decel, retail losses, cost discipline |
| 5 | INTC | 2021-04-23 | Q1 2021 / IDM 2.0 strategy |
| 6 | PYPL | 2021-07-29 | Q2 2021, near high, still growing/profitable |
| 7 | DIS | 2021-11-11 | Q4 FY2021; streaming sub miss, brand strong |
| 8 | PFE | 2022-02-08 | Q4 2021; COVID windfall, optical low P/E |

Sealed expectations:

| # | Class | Context | Key Variable | Expected Band |
|---|---|---|---|---|
| 1 | WINNER | exceptional_bottleneck | AI compute bottleneck, pricing power, customer ROI | STARTER..CORE |
| 2 | WINNER | quality_compounder / turnaround | ad business intact, cost panic reversed | STARTER..CORE |
| 3 | WINNER | quality_compounder | commercial intent gateway, Cloud inflection, FCF | STARTER..CORE |
| 4 | WINNER | quality_compounder / cyclical_inflection | retail margin trough, AWS durability, cost discipline | STARTER |
| 5 | TRAP | structural_decline_trap | process loss, capex burden, share loss | REJECT..WATCH |
| 6 | TRAP | false_cheap_value_trap | take-rate decline, competition, eBay migration | REJECT..WATCH |
| 7 | TRAP | structural_decline_trap | linear TV decline plus streaming losses | REJECT..WATCH |
| 8 | TRAP | false_cheap_value_trap | COVID earnings normalization, patent cliff risk | REJECT..WATCH |

---

## 8. Hold-Winner Probe

For NVDA and GOOGL, run a second date after the stock has materially appreciated.

Goal: test whether the system separates:

```text
new money may wait
existing position should hold
thesis is still intact
```

The output should be a position delta, not a single blunt verdict.

---

## 9. Change Control

Do not patch weights after one case.

Patch only after:

- at least 8 cases are scored;
- failure modes are tagged;
- each proposed weight or gate change has a mechanism reason;
- results are recorded in `WEIGHTING_HARNESS.md` ledgers.
