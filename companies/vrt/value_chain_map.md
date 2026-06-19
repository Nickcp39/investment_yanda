# Industry / Value Chain — VRT

Last updated: 2026-06-19

Source base: business-model/value-chain raw (S1, S2, S5, S7), facts.md. Facts: `facts.md`.

## Industry Definition

**Critical digital infrastructure — the datacenter "grey space":** the power (UPS, switchgear, busway, increasingly 800V DC) and thermal (CDUs, cold-plate, fluid networks, dry coolers) systems that sit between the utility feed and the IT rack, plus the lifecycle services around them. VRT is a **broad-line, single-vendor integrator** that spans both power and thermal — and, uniquely, ships a **co-engineered, NVIDIA-validated power+thermal stack** for AI racks.

## Value Chain Map

```text
Upstream                     Company layer              Downstream                End demand
Cold-plate / CDU /  ───┐
  coolant OEMs         │
  (Boyd, CoolIT,       │
   Modine — inside     ├──► VERTIV (broad-line   ──► Hyperscalers       ──► AI training /
   VRT's BoM)          │     single-vendor            (Big-4 ~75% of        inference compute,
Power components /     │     power + thermal +        discretionary        enterprise / colo
  switchgear OEMs      │     services integrator;     AI capex)
EPC / construction ────┘     NVIDIA reference
                             design authority)
```

## Profit Pool

| Layer | Players | Margin / return profile | Bargaining power |
|---|---|---|---|
| Upstream — components | Boyd, CoolIT, Modine (cold-plate/CDU); switchgear OEMs | commoditizing (DTC +26% CAGR, many suppliers) | **Low–Medium** — sit inside VRT's BoM |
| Upstream — construction/EPC | DC builders | cyclical | Medium |
| **Company — grey-space integration** | **VERTIV**, Schneider (co-leader); ABB/Eaton (power-weighted) | **~20% adj op margin, expanding to 27% target; FCF-positive** | **Medium–High** — owns design authority + speed; duopoly with Schneider |
| Downstream — customers | Big-4 hyperscalers, colo, enterprise | varies | **High & concentrated** — ~75% is 4 customers' discretionary capex (C023) |

**Where is profit captured?** VRT captures durable profit at the **integration/system layer** — owning the validated NVIDIA reference design + speed-to-deploy + breadth + services — *above* a commoditizing component layer (cold plates/CDUs) and *below* a concentrated, powerful set of hyperscaler buyers. It **owns the integration bottleneck and supplies into the component bottleneck** (C033). The structural caveat: it captures system-layer profit but rides four customers' discretionary capex with no contracted floor.

## Supply / Demand

- **Demand drivers:** AI training + inference build-out; rising rack density (GB200 NVL72 ≈132kW, GB300 ≈142kW) forcing liquid cooling above ~50kW → **VRT $-content per rack rises**. (C021)
- **Supply constraints:** VRT's own throughput (manufacturing/integration capacity, components) — but demand, not supply, is the swing; the gating variable is the **hyperscaler capex slope**, not VRT's ability to build.
- **Cyclicality:** **highest-beta name in the basket** — ~75% downstream of Big-4 discretionary capex, no PPA-style floor. β confirmed by the 110→380 range. (C023, C030)
- **Pricing mechanism:** order-driven equipment + recurring services; integration/validated-stack premium at the system layer; commoditization pressure at the component layer.
- **Substitute pressure:** SMCI bundled box (vertical bypass); ODM direct-to-chip; Schneider (co-leader). Contained, not zero.

## Porter five forces (quick)

| Force | Strength | Note |
|---|---|---|
| Supplier power (component OEMs) | **Low–Medium** | cold-plate/CDU multi-sourced; inside VRT's BoM |
| Buyer power (Big-4 hyperscalers) | **High** | ~75% of demand is 4 customers' discretionary capex |
| New entrants | **Medium** | component entry easy; integrated validated single-vendor stack is the gate |
| Substitutes | **Medium** | SMCI box, ODM DTC — contained |
| Rivalry | **High** | Schneider co-leads; ABB/Eaton power-weighted |

## VRT's position in the chain

**Strong at the system layer, exposed at the cycle layer.** VRT is #1 (tied with Schneider) in liquid cooling, owns the NVIDIA reference-design authority, spans power *and* thermal where peers split the chain, and extends to 800V DC. Its value-chain position is *strong-and-spanning* — it captures the integration profit *and* the component makers sit inside its BoM. But it is **structurally subordinate to the hyperscaler capex cycle**: ~75% of demand is four buyers' discretionary spend with no floor. So its position is **strong-but-cyclical** — a real, share-gaining integration moat that rides the capex cycle with no shock-absorber. Moat durability assessed in `moat_map.md`; cycle exposure in `bottleneck_map.md` and `inversion_map.md`.
