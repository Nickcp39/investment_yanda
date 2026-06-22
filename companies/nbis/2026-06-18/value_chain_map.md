# Industry / Value Chain — NBIS

Last updated: 2026-06-18

Source base: power/bottleneck raw (SRC-002, SRC-014), financials/operator raws. Facts: `facts.md`.

## Industry Definition

**AI compute infrastructure — the "neocloud" layer:** specialist providers that buy NVIDIA GPUs, build/operate AI-optimized data centers, and rent GPU compute (training + inference) to AI labs, hyperscalers, and enterprises. NBIS is a **full-stack, vertically-integrated** neocloud (owns DCs + networking + an AI Studio platform), vs lease-heavy peers.

## Value Chain Map

```text
Upstream                         Company layer            Downstream                 End demand
NVIDIA (GPUs) ───────────┐
Transformers/switchgear/ ─┼──► NBIS (owns DCs, ──► Anchor: Microsoft, ──► AI apps, model
  gas gensets (OEMs)      │     networking, AI       Meta; + self-service    training/inference,
Utilities / power /       │     Studio, ops)         / enterprise / labs     enterprise AI
  interconnection         │
EPC / construction ───────┘
```

## Profit Pool

| Layer | Players | Margin / return profile | Bargaining power |
|---|---|---|---|
| **Upstream — GPUs** | **NVIDIA** | ~75% GM, dominant | **Very high** — sets allocation, prices; also NBIS investor (C034) |
| Upstream — electrical gear / power | Transformer/gen OEMs, utilities | tight supply, rising prices | **High** (shortage = the bottleneck, C022) |
| Upstream — construction/EPC | DC builders, partners (DataOne, Azur) | cyclical | Medium |
| **Company — neocloud** | **NBIS**, CoreWeave, Crusoe, Lambda, Oracle | ~69% GM, but ~7× capex/rev, FCF−; core seg EBITDA ~45% (C007) | **Medium** — pricing power *now* (sold out), erodes if supply catches up |
| Downstream — customers | MSFT, Meta, AI labs, enterprises | varies | **High & concentrated** — 2 whales dominate backlog (C017) |

**Where is profit captured?** Today **NVIDIA captures the most durable profit** upstream; the neocloud layer earns good gross margins but bleeds cash on capital intensity, sandwiched between a dominant supplier (NVIDIA) and concentrated, powerful buyers (MSFT/Meta). NBIS's bet is that owning capacity + full-stack + cheap power lets it hold margin as the layer matures.

## Supply / Demand

- **Demand drivers:** AI training + inference build-out; sovereign-AI (EU). Currently **vastly exceeds supply** — "4+ customers per GPU," prices raised and still sold out. (C029)
- **Supply constraints:** the build-and-energize chain — transformers/gensets, construction, interconnection (see `bottleneck_map.md`). NOT GPUs (de-risked) or capital. (C022, C023)
- **Cyclicality:** tied to the AI capex super-cycle — the central macro risk (overbuild → air-pocket). Reflexive: cheap financing amplifies up, tightens down.
- **Pricing mechanism:** mix of multi-year committed/anchor contracts (take-or-pay vs terminable disputed, C014/C015) + on-demand/self-service. Spot GPU-hour prices (e.g. Hopper −28% YoY) signal commoditization at the trailing edge. (C041)
- **Substitute pressure:** hyperscaler in-house silicon (TPU/Trainium/Maia) and hyperscalers' own capacity — the structural 2027+ threat to Nvidia-rental neoclouds. (path E)

## Porter five forces (quick)

| Force | Strength | Note |
|---|---|---|
| Supplier power (NVIDIA) | **High** | allocation + price setter; mitigated by NBIS being an NVIDIA investee/partner |
| Buyer power (MSFT/Meta) | **High** | concentration; contractual clawback leverage (C015) |
| New entrants | **Medium–High** | capital is available; the gate is build speed + power, not money |
| Substitutes | **Medium (rising)** | custom ASICs, hyperscaler self-supply |
| Rivalry | **High** | CoreWeave, Crusoe, Lambda, Oracle, hyperscalers all racing for power/MW |

## NBIS's position in the chain

Top-tier among pure-play neoclouds on **contracted power (>3.5GW, >75% owned)** and **power cost/cleanliness** (Nordic), with full-stack differentiation (AI Studio). But it does **not own the scarce upstream input** (GPUs = NVIDIA; electrical gear = OEMs) and faces **concentrated, powerful buyers**. So its value-chain position is *strong-but-squeezed* — competitive among neoclouds, structurally subordinate to NVIDIA and its two anchor customers. Moat durability assessed in `moat_map.md`.
