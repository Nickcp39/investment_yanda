# Industry / Value Chain — CEG

Last updated: **2026-06-22**

Source base: business-model/value-chain raw, hyperscaler capex (S8). Facts: `facts.md`.

## Industry Definition

**US competitive (merchant) power generation — the carbon-free baseload layer feeding the AI/datacenter buildout.** CEG is the largest US merchant producer: it sells electrons into competitive wholesale markets (principally PJM) rather than earning a regulated allowed return on rate base. Within the AI-electricity bottleneck, CEG is the **generation-side** expression (un-buildable carbon-free baseload); VRT is the downstream thermal/power-management layer of the same buildout.

## Value Chain Map

```text
Upstream                         Generation node (CEG)         Offtake                    End demand
Uranium / nuclear fuel ──────┐
Natural gas (Calpine) ────────┼──► CEG: ~32 GW nuclear   ──► Wholesale (PJM,       ──► AI datacenters
Grid / PJM / FERC rules ──────┤     (~95% CF, ~$0 fuel)       gas-set clearing)          (MSFT, META, AMZN,
Transmission / interconnect ──┘     + ~23 GW gas/geo +    ──► Bespoke hyperscaler         GOOGL, CyrusOne),
                                    retail book                PPAs + retail              industrial, households
```

## Profit Pool

| Layer | Players | Margin / return profile | Bargaining power |
|---|---|---|---|
| Fuel — uranium / gas | suppliers | commodity | **Low** (nuclear marginal fuel ~$0) |
| **Generation — carbon-free baseload** | **CEG**, VST, TLN, NRG | **wide inframarginal margin; PTC-floored**; ~95% CF nuclear | **High** — owns the scarce, un-buildable asset; buyers price-insensitive |
| Generation — dispatchable gas | CEG (Calpine), independents | spark spread + capacity | Medium |
| Transmission / market rules | PJM, FERC | regulated | **Medium** — co-location resolved favorable (5-0, C015) |
| Offtake — hyperscalers | MSFT, META, AMZN, GOOGL | pay premium for 24/7 carbon-free | **High but motivated** — capex +77% to ~$725B (C025) |

**Where is profit captured?** At the **generation node CEG controls** — the scarce asset (existing carbon-free baseload) sits there, and the buyers are simultaneously powerful *and* desperate for it. The key contrast with NBIS (sandwiched between supplier NVIDIA and whale customers). **CEG owns its scarce input**, so its risk is regulatory/market-structure (largely resolved) and execution (Calpine, now de-risked) — not supplier/buyer squeeze.

## Supply / Demand

- **Demand drivers:** AI/datacenter load + broader electrification. Hyperscaler 2026 capex **~$725B (+77%)**: AMZN $200B, MSFT $190B, GOOGL $190B, META $115–135B. (C025) Price-insensitive demand for carbon-free 24/7 power. **Single-factor tie:** this is the same demand driver under NBIS and VRT.
- **Supply constraints:** carbon-free baseload supply is **effectively fixed** — no new large reactor on time/budget in a generation; greenfield ~10–15yr; restarts are scarce one-offs. (C022)
- **Cyclicality:** power prices are cyclical, but the **§45U PTC (~$25/MWh to 2032) floors the downside.** (C026)
- **Pricing mechanism:** PJM clearing (gas-set) for merchant volume; bespoke premium PPAs for contracted volume.
- **Substitute pressure:** SMRs, new gas, renewables-plus-storage — real over a *decade*, none able to add carbon-free baseload at scale on the AI buildout's timeline.

## Porter five forces (quick)

| Force | Strength | Note |
|---|---|---|
| Supplier power (fuel) | **Low** | nuclear marginal fuel ~$0; gas is a commodity |
| Buyer power (hyperscalers) | **Medium** | concentrated but motivated; capex accelerating; they *cannot* self-build nuclear |
| New entrants | **Low (for nuclear baseload)** | can't build new reactors on a relevant horizon; this IS the moat (C022) |
| Substitutes | **Low–Medium** | SMR/gas/renewables real over a decade, not on AI's timeline |
| Rivalry | **Medium** | VST/TLN/NRG compete for PPAs, but the scarce-asset position is CEG's |

## CEG's position in the chain

Top of the carbon-free-baseload layer: **largest US producer, ~95% nuclear CF, near-zero marginal cost, a legislated PTC floor, and a growing book of premium hyperscaler PPAs.** Unlike NBIS, CEG **owns the scarce upstream input** rather than renting it — its value-chain position is *strong and self-owned*, the squeeze risk being regulatory (resolved favorably) and execution (Calpine, now de-risked), not supplier/buyer power. Moat durability in `moat_map.md`; the LEAD question in `bottleneck_map.md`.
