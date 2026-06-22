# GEV (GE Vernova) Step 0 Research Plan

Last updated: 2026-06-19
Test batch: AI-electricity bottleneck — power/grid layer (1 of 3, with [[CEG]], [[VRT]])
Mode: **Live decision card** (current price, fresh-initiation BUY / NO-BUY). Holder owns 0 shares.

## Research Question

```text
1. (LEAD — bottleneck) Is GEV a DURABLE toll booth on electrification
   (gas-turbine slots + grid/transformer lead times the binding constraint
   on every new datacenter), or a CYCLICAL order surge that normalizes once
   the current capex wave is built? Who actually owns the bottleneck —
   does GEV set the price, or just ride demand?
2. (DECISION) At today's price, is the durable bottleneck rent enough to
   justify the multiple, or is it priced for execution? BUY / NO-BUY / WATCH,
   and at what price/evidence each becomes right.
3. (KILL) What would prove the toll-booth thesis wrong?
```

## Thesis hypothesis (analyst prior — knowledge to 2026-01, MUST verify in Block 1)

- GEV spun out of GE in **April 2024**; 3 segments: **Power** (gas + nuclear
  services), **Wind** (loss-making drag), **Electrification** (grid/transformers).
- Bull case = the *bottleneck is physical and structural*: heavy-duty gas-turbine
  capacity is a 3-maker oligopoly (GE / Siemens Energy / Mitsubishi), slots
  reportedly sold out multiple years; large-transformer lead times measured in
  years. That = pricing power on the two scarcest links in "AI needs power now."
- Bear case = Wind keeps bleeding; the order book is a one-off electrification
  surge; expanding capacity to meet it compresses ROIC (classic "solving the
  bottleneck destroys returns" risk from `bottleneck_map.md`).

## Why now

- Pure-play electrification leader, ~2 yrs post-spin → first clean full-year
  financials as an independent co; investor-day targets now testable vs actuals.
- It is the one name the holder named directly ("GE 可能好点") and wrongly assumed
  was state-backed — explicitly NOT a 国企, no sovereign backstop. Price it as a
  plain cyclical-industrial-with-a-moat, not as "safe."

## Non-Goals

- Not a short-term earnings-trade call.
- Do not let "AI electricity" narrative substitute for backlog/margin evidence.
- No memo before the evidence layer (source_register → claim_ledger → facts) exists.

## Source Budget (all PENDING — fresh case)

| Source type | Min | Have? |
|---|---:|---|
| Latest 10-K (FY2025) | 1 | ☐ |
| Latest 10-Q | 1 | ☐ |
| Earnings call transcripts | 2-4 | ☐ |
| Investor day / guidance deck | 1 | ☐ |
| Backlog / orders disclosure (segment) | 1 | ☐ |
| Competitor filings (Siemens Energy, Mitsubishi, ETN/Hubbell on grid) | 2-4 | ☐ |
| Independent industry (gas-turbine slot, transformer lead-time data) | 2-3 | ☐ |

## Research Blocks

| Block | Question | Output | Status |
|---|---|---|---|
| 1. Evidence foundation | What is true? | `source_register.md`, `claim_ledger.csv`, `facts.md` | pending |
| 2. Financial quality | Real economics (segment margins, FCF, Wind drag)? | `financials/financial_quality.md` | pending |
| 3. Business model | How it makes money (equipment vs services mix)? | `business_model.md` | pending |
| 4. Industry/value chain | Where is profit captured? | `value_chain_map.md` | pending |
| 5. Moat/bottleneck | LEAD Q — durable rent or cyclical? | `moat_map.md`, `bottleneck_map.md` | pending |
| 6. Operator | Who runs it; capital allocation post-spin? | `operator_underwriting.md` | pending |
| 7. Inversion | How does it fail? | `inversion_map.md` | pending |
| 8. Valuation | Priced for execution? | `valuation.md` | pending |
| 9. Decision | BUY/NO-BUY/WATCH + monitor | `memo-v1.md`, `monitor.md` | pending |

## Kill criteria (pre-registered)

- Gas-turbine slot pricing rolls over / order cancellations appear in backlog.
- Wind segment losses widen instead of narrowing toward break-even.
- Capacity-expansion capex pushes segment ROIC down (bottleneck = cost sink).
- **Shared switch:** hyperscaler capex guidance slope turns down (see batch note —
  the single upstream variable common to GEV / CEG / VRT).
