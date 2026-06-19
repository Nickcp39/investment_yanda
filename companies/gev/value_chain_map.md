# Industry / Value Chain — GEV

Last updated: 2026-06-19

Source base: L5-6 raw, S7 (market structure), S3 (backlog/pricing). Facts: `facts.md`.

## Industry Definition

**Electrification supply chain — the "physical-power" layer of the AI/load-growth build-out:** the OEMs that make the scarce, long-lead capital equipment every new gigawatt of demand must buy — **heavy-duty gas turbines** (firm/dispatchable generation) and **grid equipment / large transformers** (delivery). GEV is a vertically-integrated leader across Power (gas + nuclear/SMR + services), Electrification (grid/transformers), and Wind.

## Value Chain Map

```text
Upstream                          Company layer              Downstream                  End demand
Specialty metallurgy /  ─────────┐
  forgings / castings            │
Turbine components / ─────────────┼──► GE Vernova ──► Utilities / IPPs / ──► Electricity for AI
  controls                       │    (Power: gas +     data-center devs;      data centers, grid
Copper / electrical steel ───────┤    nuclear + svc;    grid operators;        load growth,
  (transformers)                 │    Electrification;  EPC / construction     electrification,
EPC / construction ──────────────┘    Wind)                                    industrial demand
```

## Profit Pool

| Layer | Players | Margin / return profile | Bargaining power |
|---|---|---|---|
| Upstream — components / metallurgy | forging/casting/controls suppliers | varies; some tight (electrical steel, copper) | Medium — inputs to the bottleneck, not the bottleneck |
| **Company — heavy-duty turbines** | **GEV + Siemens Energy + Mitsubishi** (~two-thirds heavy-duty) | equipment near cost-to-low-margin; **services high-margin annuity** | **High** — 3-maker oligopoly, GEV *sets* equipment price (+10–20%) |
| Company — Electrification / transformers | GEV (Prolec), Hitachi Energy, Siemens, Eaton, Hubbell | 18%+ rising to 22%; capacity-constrained | High — transformer shortage = pricing power |
| Downstream — customers | utilities, IPPs, hyperscalers/DC developers, grid operators | varies | Medium — **prepaying deposits** to secure scarce slots (C017) |

**Where is profit captured?** GEV sits **on the bottleneck** — the heavy-duty gas-turbine and large-transformer links are the scarcest in "AI needs power now," and a 3-maker oligopoly controls turbines. GEV captures the durable profit in **two places**: the **services annuity** ($87B RPO, structural) and, *cyclically right now*, the **equipment-pricing premium** (+10–20%). Downstream customers are funding the seller (deposits) to get capacity — the opposite of buyer power. (C013, C016, C017)

## Supply / Demand

- **Demand drivers:** electrification + AI data-center load growth + aging grid replacement. Currently demand **far exceeds** turbine slot supply (sold out through 2029; customers booking 2031+). (C014, C015)
- **Supply constraints:** heavy-duty turbine capacity (3 makers, multi-year qualification, measured 20→24 GW/yr adds) and large transformers (capacity-constrained). GEV *rations* turbine capacity deliberately. (C018, C019)
- **Cyclicality:** the equipment leg is tied to the AI/power capex super-cycle — the central risk (overbuild → digestion). The services leg is largely *insulated* from the cycle. (shared switch — kill d)
- **Pricing mechanism:** multi-year equipment orders at +10–20% (set, not taken) + reservation deposits + a contractual services annuity. (C016, C017)
- **Substitute pressure:** SMR/nuclear (GEV's own BWRX-300, longer-dated), storage+renewables for some peaker duty, demand-side efficiency. Structural but slow vs the current gas-turbine bottleneck.

## Porter five forces (quick)

| Force | Strength | Note |
|---|---|---|
| Supplier power (components) | **Medium** | tight in spots (electrical steel/copper), but not the binding constraint |
| Buyer power (utilities/DC devs) | **Low (now)** | prepaying deposits for scarce slots; GEV sets price |
| New entrants | **Very Low** | metallurgy/IP, multi-year qualification → effectively impossible near-term |
| Substitutes | **Medium (rising, slow)** | SMR, storage+renewables — structural but longer-dated |
| Rivalry | **Low–Medium** | 3-maker oligopoly with apparent pricing discipline (measured capacity) |

## GEV's position in the chain

**Strong and bottleneck-owning** — GEV is one of three firms controlling the scarcest physical link in the AI-power build-out, *sets* equipment price, *rations* capacity like an owner, and compounds a sticky services annuity. The caveat the value-chain view makes explicit: the **equipment** pricing power is *demand-pull from the hyperscaler capex cycle* (kill d), so the premium is cyclical even though the *structure* (oligopoly) and the *services rent* are durable. Moat durability assessed in `moat_map.md` / `bottleneck_map.md`.
