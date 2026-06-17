# Lean Company Backtest Material Template

Status: `LEAN TEMPLATE`
Updated: 2026-06-16

Purpose: give every historical company test enough material to judge capital
allocation without recreating a full GOOGL-style research folder.

This template deliberately folds the Meigu Touziwang / TradesMax style into the
core process. It is not a new scouting layer. The questions "why now?", "what
is the market repricing?", "where is the bottleneck?", and "what one metric will
force an update?" live inside the thesis and value-chain modules.

The rule is simple:

```text
theme first -> mechanism second -> ticker third -> evidence -> price -> size
```

No separate `theme_scout.md`, `narrative_map.md`, `first_principles.md`,
`buy_below_and_mos.md`, or `position_risk.md` is required by default. Those
ideas are mandatory, but they are embedded into the six files below.

---

## 0. Package Sizes

| Package | Use Case | File Count | Use |
|---|---:|---:|---|
| `P0 Probe` | Fast blind test, known as-of date. | 5-7 | Find obvious routing failures. |
| `P1 Lean Case` | Default multi-agent backtest. | 9-12 | Score and tune the pipeline. |
| `P2 Deep Case` | Only after P1 exposes a hard dispute. | 16-24 | Rebuild full company research. |

Default to `P1`. P2 is a promotion, not the norm.

---

## 1. Six Decision Modules

The old 10 layers are compressed into six decision modules. Each module must
emit a signal that can change the final position size.

| Module | Absorbs Old Layers | Core Question | Output File |
|---|---|---|---|
| M1. Evidence Spine | Layer 3 | What did we know by the as-of date, and how reliable is it? | `evidence_spine.md` |
| M2. Theme / Mechanism Thesis | Layers 1-2 plus narrative and first principles | Why this company now, what is changing, and what mechanism could create value? | `thesis_mechanism.md` |
| M3. Profit Pool / Durability | Layers 5-7 | Who captures the economics, why does it persist, and who runs it? | `profit_pool_durability.md` |
| M4. Financial Reality | Layer 4 plus normalized economics | Do accounting, margins, cash flow, balance sheet, and cycle position confirm or refute the thesis? | `financial_reality.md` |
| M5. Inversion / Trap Test | Layer 8 | What would make this a permanent-loss mistake or value trap? | `inversion_trap_test.md` |
| M6. Price / Position / Monitor | Layers 9-10 | At this price, what size should we own, add, hold, trim, or avoid? | `decision_card.md` + `decision_card.json` |

This is the integration point:

- News, sentiment, KOL notes, and TradesMax-style material feed M2 as leads.
- First-principles reasoning is the first half of M2, not a separate file.
- Value-chain and bottleneck thinking live in M3, not a separate scout layer.
- Safety margin and portfolio risk live in M6, not separate valuation and risk
  documents.
- Evidence completeness is M1 confidence. It can haircut size, but it should not
  automatically cap every interesting idea at `WATCH`.

---

## 2. P1 Lean Case Folder

Recommended path:

```text
backtests/cases/<ticker>_<as_of>/
  case_control.md
  sources_used.csv
  raw_extracts.md
  evidence_spine.md
  thesis_mechanism.md
  profit_pool_durability.md
  financial_reality.md
  inversion_trap_test.md
  decision_card.md
  decision_card.json
  lookahead_audit.md
  outcome_score.md
```

### Required Content

| File | Required Content |
|---|---|
| `case_control.md` | ticker, company, as-of date, decision question, allowed/forbidden evidence, price date. |
| `sources_used.csv` | source_id, title, public_date, url_or_path, type, used_for. |
| `raw_extracts.md` | neutral excerpts or close paraphrases from filings, releases, transcripts, dated news, and market data. |
| `evidence_spine.md` | audited facts, open questions, source quality, confidence grade. |
| `thesis_mechanism.md` | the integrated TradesMax-style scout plus first-principles business thesis. |
| `profit_pool_durability.md` | value chain, bottleneck, moat, operator, capital allocation. |
| `financial_reality.md` | financial trend, normalized owner earnings, cycle/trough/peak check, balance sheet. |
| `inversion_trap_test.md` | kill paths, false-cheap diagnosis, structural decline checks, what would prove us wrong. |
| `decision_card.md` | human memo: verdict, price bands, size, add/trim/exit rules, monitor. |
| `decision_card.json` | machine-readable output for scoring and weighting. |
| `lookahead_audit.md` | no post-as-of data, no outcome-aware language. |
| `outcome_score.md` | scorer-only result after blind verdict is locked. |

If the case is very simple, `raw_extracts.md` and `evidence_spine.md` may be
combined for P0. Do not split more files unless a module genuinely becomes too
large to audit.

---

## 3. M2 Integrated Thesis Template

`thesis_mechanism.md` must answer these questions in one compact memo.

```text
Theme:
Why now:
Market narrative:
What the market may be overemphasizing:
What the market may be underemphasizing:
Capital flow evidence:
Demand shock:
Scarce resource / bottleneck:
Who pays:
Unit of value:
Unit of cost:
Profit pool:
Why this company captures it:
One metric that will force market update:
Catalyst:
Kill condition:
Initial context label:
```

This is where the Meigu Touziwang method is absorbed. The output is a hypothesis
and context label, not a buy decision.

Allowed context labels:

```text
quality_compounder
exceptional_bottleneck
cyclical_inflection
spinoff_forced_seller
turnaround
structural_decline_trap
false_cheap_value_trap
yield_or_balance_sheet_trap
too_hard
```

---

## 4. M6 Decision Card Standard

`decision_card.md` must force the research into a portfolio action.

```text
Business verdict:
New-money verdict:
Existing-position verdict:
Suggested initial size:
Suggested max size:
As-of price:
Buy-below price:
Starter zone:
Add zone:
Hold zone:
Trim / no-chase zone:
Reject / avoid zone:
Main reason to own:
Main reason not to own:
Binding constraint:
Evidence confidence haircut:
Downside if wrong:
Upside if right:
Add trigger:
Trim trigger:
Exit / kill criteria:
Next monitor event:
```

Uncertainty must become a smaller size, a wider price band, or a specific open
question. It should not automatically become `WATCH / 0%` when the setup has
clear asymmetry and survivable downside.

---

## 5. Machine-Readable Output

Every P1 case must include `decision_card.json`.

```json
{
  "ticker": "",
  "as_of": "",
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
  "sources_used": [
    {"source_id": "", "public_date": "", "url_or_path": ""}
  ]
}
```

---

## 6. Case-Type Emphasis

The same six modules run for every company, but weights change by context.

| Context | Must Drive The Decision | Common Failure |
|---|---|---|
| `quality_compounder` | M2, M3, M6 | selling or avoiding because classic multiple looks high. |
| `exceptional_bottleneck` | M2, M3, M4, M6 | missing the starter because valuation looks optically expensive. |
| `cyclical_inflection` | M2, M4, M5, M6 | using trough or peak earnings incorrectly. |
| `spinoff_forced_seller` | M1, M2, M4, M6 | treating messy first-quarter optics as true economics. |
| `turnaround` | M4, M5, M6 | trusting management before balance-sheet survival is clear. |
| `structural_decline_trap` | M3, M4, M5 | calling low P/E a margin of safety. |
| `yield_or_balance_sheet_trap` | M4, M5, M6 | ignoring debt, capex needs, or dividend fragility. |

---

## 7. Minimum Evidence Mix

| Source Type | P0 | P1 | P2 |
|---|---:|---:|---:|
| SEC filings / official releases | 1-2 | 3-6 | 8-15 |
| Earnings call / management commentary | 0-1 | 1-3 | 3-6 |
| Historical price / market cap | 1 | 1 | 2-4 |
| Dated news / market narrative | 2-5 | 5-12 | 15-30 |
| Industry / peer / sell-side context | 0-1 | 1-4 | 5-10 |
| Local video / KOL / social leads | optional | optional | optional |

Source treatment:

- Company filings, releases, and transcripts can support evidence directly.
- Reputable news can support reported facts and narrative context.
- Local notes, YouTube, X, Reddit, and KOL material are topic leads or sentiment
  only unless independently verified.
- Any source after the as-of date is forbidden for the blind runner.

---

## 8. Assignment Prompt

```text
You are the blind Runner for <TICKER> as of <YYYY-MM-DD>.

Use only information public on or before the as-of date.
Do not look up or mention later stock performance, later filings, later guru
actions, or known outcomes.

Produce a P1 Lean Case under:
backtests/cases/<ticker>_<as_of>/

Use the six-module template in:
backtests/framework_validation/COMPANY_MATERIAL_TEMPLATE.md

The key integration rule is:
theme first -> mechanism second -> ticker third -> evidence -> price -> size

Do not create extra scout, narrative, first-principles, valuation, or risk files
unless a module genuinely becomes too large to audit. Put those ideas into M2,
M3, M4, M5, and M6.

Lock `decision_card.json` before any outcome scoring.
Do not score the outcome. Another agent will do that.
```

---

## 9. What Changed From The Old Template

Deleted as default standalone files:

```text
narrative_map.md
first_principles.md
business_model.md
value_chain_map.md
moat_bottleneck.md
operator_underwriting.md
valuation.md
buy_below_and_mos.md
position_risk.md
blind_memo.md
monitor_plan.md
```

They were not removed as concepts. They are compressed into:

```text
thesis_mechanism.md
profit_pool_durability.md
financial_reality.md
inversion_trap_test.md
decision_card.md
```

The goal is fewer files, fewer places to hide indecision, and stronger pressure
to turn research into a right-sized portfolio action.
