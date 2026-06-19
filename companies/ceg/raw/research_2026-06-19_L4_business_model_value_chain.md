# CEG Research Run — Layer 4: Business Model + Value Chain

- Run date: 2026-06-19
- Method: decomposition of the Block-1 evidence pack, grounded in `../source_register.md` (S1, S4, S8, S12).
- Status: ⚠️ **UNAUDITED RESEARCH DIGEST.** Promoted to `../claim_ledger.csv` (C012–C014, C020–C021, C025) and `../facts.md`.

---

## BOTTOM LINE

CEG makes money at the **generation node**: it owns ~22 GW of nuclear (plus, post-Calpine, ~23 GW of mostly gas + Geysers geothermal and a large retail book) and sells electrons into PJM/wholesale at gas-set clearing prices, capturing margin = market price − ~$0 nuclear fuel, partially hedged forward. It is a **merchant** (not rate-regulated) generator, so it keeps the upside (and wears the downside) of power prices. The **new profit lever** — the reason this is an "AI" story and not just a utility — is **bespoke, long-dated PPAs to hyperscalers** that convert merchant price volatility into **contracted, PTC-floored annuity streams at a premium to wholesale.** The bottleneck "makes money" precisely by selling scarce carbon-free baseload to buyers (hyperscalers) whose demand is price-insensitive and accelerating.

---

## A. How CEG earns — the generation node [S1, PRIMARY]

- **Largest US merchant generator.** Not a regulated utility earning an allowed ROE on rate base — it sells into competitive wholesale markets and keeps the spread. (C020)
- **Nuclear is the engine:** ~22 GW at ~95% CF, near-zero marginal fuel cost. In a market where the clearing price is set by the *marginal* (usually gas) unit, a ~$0-fuel baseload unit captures a wide inframarginal margin. (C004, C020)
- **Hedging:** output is partially hedged forward; year-by-year hedge ratios undisclosed (a key open gap — caps precision on near-term EPS sensitivity to power curves).

## B. What Calpine changed [S4, PRIMARY]

- Closed **2026-01-07** → ~55 GW combined, **largest US power producer.** (C012)
- Adds **~23 GW (mostly gas + Geysers geothermal)** plus a **large retail book**. (C023, business-model implication)
- **Mix shift:** toward dispatchable gas + integrated retail-plus-generation; **carbon-free share ~90% → ~58%.** This is the "dilutes purity" critique — but dispatchable gas is also what makes the combined fleet able to *firm* intermittent renewables and serve 24/7 datacenter load.
- Deal structure: $26.6B ($16.4B equity / ~50M shs + $4.5B cash + ~$12.7B assumed debt); guided >20% FY26 EPS-accretive. (C014)

## C. The new profit lever — hyperscaler PPAs [S12, S1]

- **Mechanism:** sign 15–20 yr PPAs with hyperscalers that pay a **premium to wholesale** for carbon-free, 24/7, matched power → converts merchant volatility into a **contracted annuity** with a **§45U PTC floor (~$25/MWh)** underneath. (C021)
- **Flagship:** Microsoft 20-yr PPA tied to **Crane** (ex-TMI Unit 1, ~835 MW). Microsoft matches its PJM datacenter load with Crane output. **Front-of-the-meter** — Crane injects to the grid; MSFT buys across PJM — *not* behind-the-meter like Talen/AWS. (C013) **Pricing UNDISCLOSED.**
- **Second deal:** Meta buys the clean attributes of the 1,092-MW **Clinton** plant from June 2027. (MED confidence.)
- **The catch (key for the equity):** Crane's upside is **already contracted to Microsoft** at an undisclosed (likely fixed) price → it **caps CEG's own upside** on that unit. The marginal *new* AI PPA is the swing variable for re-rating. (C013, C021)

## D. Value chain — where profit is captured [S8]

```text
Upstream                    Generation node (CEG)          Offtake / downstream        End demand
Uranium / fuel ────────┐
Gas (Calpine) ─────────┼──► CEG: ~22 GW nuclear      ──► Wholesale (PJM, gas-set) ──► AI datacenters,
Grid / PJM / FERC ─────┤      + ~23 GW gas/geo +          + bespoke hyperscaler        industrial,
Transmission / queue ──┘      retail; ~95% CF nuke         PPAs (MSFT/Meta), retail     households
```

- **Scarce input CEG OWNS:** existing carbon-free baseload (nuclear) — the thing that cannot be newly built. This is the durable profit-capture point. (C022)
- **Upstream dependence:** PJM/FERC market rules (resolved favorably, see `../bottleneck_map.md`), interconnection/queue timing (residual risk; full PJM deliverability upgrades ~2030).
- **Downstream demand:** hyperscaler 2026 capex ~$725B (+77%): AMZN $200B, MSFT $190B, GOOGL $190B, META $115–135B. (C025) Demand is the opposite of a problem — it is accelerating and price-insensitive for carbon-free 24/7 power.

## E. Profit pool / bargaining power

| Layer | Players | Margin profile | Bargaining power |
|---|---|---|---|
| Fuel (uranium/gas) | suppliers | commodity | Low–Med (nuclear fuel ~$0 marginal) |
| **Generation — carbon-free baseload** | **CEG, VST, TLN, NRG** | wide inframarginal margin; PTC-floored | **High** — scarce, un-buildable, price-insensitive buyers |
| Transmission / market rules | PJM, FERC | regulated | Med (resolved favorable for co-location) |
| Offtake — hyperscalers | MSFT, META, AMZN, GOOGL | pay premium for 24/7 carbon-free | **High but motivated** — need the power, capex accelerating |

**Where is profit captured?** At the **generation node CEG controls**, because the scarce asset (existing carbon-free baseload) sits there and the buyers are both powerful *and* desperate. Unlike NBIS (sandwiched between NVIDIA upstream and 2 whale customers), CEG **owns the scarce input** — its squeeze risk is regulatory/market-structure (largely resolved) and execution (Calpine), not supplier/buyer power.

---

## COULD NOT VERIFY (flag list)

1. **Microsoft PPA price** — undisclosed; cannot size Crane PPA premium-to-wholesale. (C013)
2. **Meta/Clinton terms** — MED confidence; structure (attributes-only vs full offtake) and price not in primary.
3. **Retail book economics post-Calpine** — margin contribution of the acquired retail business not separately disclosed.
4. **Hedge ratios** — undisclosed; near-term power-price sensitivity not precisely modelable.

## Key sources

- S1 — CEG FY2025 earnings release, 2026-02-23
- S4 — CEG–Calpine completion release, 2026-01-07
- S8 — Hyperscaler 2026 capex compilation (FT/CNBC), 2026-02 — cnbc.com/2026/02/06/...
- S12 — Microsoft–Constellation Crane PPA, 2024-09 / restated — constellationenergy.com newsroom

**Net for thesis:** CEG monetizes the bottleneck by owning the scarce asset and selling it forward to price-insensitive hyperscalers under PTC-floored contracts. The model is sound and the demand is accelerating; the equity-specific nuance is that the *first* great deal (Crane→MSFT) is already locked, so the re-rate depends on the *next* one.
