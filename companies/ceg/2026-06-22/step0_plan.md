# CEG (Constellation Energy) Step 0 Research Plan

Last updated: **2026-06-22**
Batch: **mempower4 LIVE** (as_of 2026-06-22) — AI-datacenter power leg (with VRT)
Mode: **Live decision card** (current price, fresh-initiation). Holder owns 0 shares. Seeded from `companies/ceg/` (2026-06-19).

## Research Question

```text
1. (LEAD — bottleneck) Is CEG's existing nuclear fleet a DURABLE scarcity rent —
   carbon-free baseload you physically cannot build new, sold to datacenters at
   premium PPAs with a PTC price floor — or is the AI-power premium already fully
   priced and exposed to a single regulatory switch (FERC co-location)?
2. (DECISION) At today's price, STARTER / WATCH / REJECT, and at what price/evidence.
3. (KILL) What breaks the scarcity-rent thesis?
```

## Thesis gate (one gate; pass/fail before a verdict)

> **GATE:** CEG earns a *persistent, structurally protected* excess return on a scarce, un-buildable asset, AND that rent is not primarily hostage to a single regulatory switch, AND the price embeds a margin of safety vs the bear.
> **Evidence required to PASS:** (a) physical scarcity (no new-build on horizon) [C022]; (b) positive structural ROIC / owner earnings [C002–C004]; (c) FERC co-location resolved not-hostile [C015]; (d) a legislated downside floor [C019]; (e) price below the no-margin line, with a defined bear floor [C027r, C028r].
> **Result: PASS** — all five hold as of 2026-06-22. (FERC defused, PTC survived, leverage de-risked to ~2.25x, bear ~−20% floored, Street targets all above price.)

## Why now

- Cleanest "AI shortage of power → nuclear cash flow" expression; the generation-side counterweight to VRT (downstream) in this batch.
- Fresh primary data available: Q1'26 10-Q (leverage, shares, Calpine consideration), latest FERC posture, latest PPAs.

## Non-Goals

- Not a power-price timing trade.
- Do not treat the Microsoft headline (or its rumored $100–115/MWh price) as the thesis — the price is undisclosed; verify PPA terms / FERC path.
- No verdict above the completeness ceiling (one parallel pass = DECISION_DRAFT → STARTER max).

## Source Budget (status 2026-06-22)

| Source type | Min | Have? |
|---|---:|---|
| Latest 10-Q (Q1'26) | 1 | ✅ S13 |
| FY2025 release | 1 | ✅ S1 (SEC 10-K second-confirm OPEN) |
| Earnings call transcript | 2-4 | ✅ S14 (Q1'26) + prior |
| TMI/Microsoft PPA + Crane restart | 1 | ✅ S12, S6 (price undisclosed) |
| Calpine docs (close + consideration) | 1 | ✅ S4, S13 |
| FERC co-location ruling + context | 1-2 | ✅ S5 |
| Competitor / peer (VST, TLN, NRG) | 2-3 | ✅ S9 (multiples) |
| Live price (Yahoo chart API + 2 cross-checks) | 1 | ✅ S15, S9 |

## Stop conditions

- **STOP and cap at STARTER** if: combined-entity FCF unconfirmed AND no NEW premium PPA AND SEC 10-K headline not second-confirmed (all true → DECISION_DRAFT). ← current state.
- **STOP and downgrade** if any kill fires (see `inversion_map.md`).
- **STOP and upgrade toward CORE** only if: NEW premium-nuclear PPA priced AND deleverage reaches ~2.0x AND SEC headline second-confirmed.

## Kill criteria (pre-registered)

- FERC durably blocks/curtails co-location → premium-PPA model capped. **[DEFUSED]**
- Power prices fall toward/below the PTC floor → upside compresses. **[FLOORED]**
- Calpine deal proves dilutive / over-levered / re-carbonizes. **[PARTIAL, DE-RISKED — ~2.25x]**
- Nuclear PTC repealed or weakened. **[NOT TRIGGERED]**
- Shared switch: hyperscaler capex guidance slope turns down. **[ACCELERATING +77%]**
