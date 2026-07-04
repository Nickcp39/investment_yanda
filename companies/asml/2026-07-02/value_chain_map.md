# ASML Value Chain Map (M3)

As-of: 2026-07-02

## Where ASML sits

```
ASML supply base                ASML (the choke point)        Chip fabs (customers)      End demand
(Zeiss optics, Cymer/light  ->  integrates & sells       ->   TSMC, Samsung, Intel,  ->  NVDA GPUs, Google TPU,
 source, Trumpf lasers,          EUV + DUV lithography          SK hynix, Micron           AWS Trainium, Apple SoC,
 10,000s of precision parts)     systems + service              |                          all AI accelerators + HBM
        ^                              ^                         v
        |                              |____ INSTALLED-BASE SERVICE (recurring, decades) ____|
   ASML is the integrator/gatekeeper of the whole EUV ecosystem (esp. Zeiss high-NA optics, in which it holds a stake)
```

## Value-capture logic

- **Upstream (suppliers):** ASML orchestrates a deep, hard-to-replicate supplier web — most critically **Carl Zeiss SMT** (the EUV/High-NA optics, effectively a co-monopoly ASML has invested in), the light source (Cymer, ASML-owned), and Trumpf lasers. This ecosystem is itself a barrier: even a would-be competitor would have to rebuild it. ASML captures the integration rents.
- **ASML node (the ultimate choke point):** ASML is the ONLY firm that can deliver a working EUV scanner. This is not "leading share" — it is a **100% monopoly** on the single tool leading-edge chips cannot be made without. That is why it holds ~50-53% gross margin and can raise ASPs into every new generation (DUV -> EUV 0.33 NA -> High-NA 0.55 NA).
- **Downstream (fabs):** Customers are concentrated and enormous (TSMC, Samsung, Intel, SK hynix, Micron), and they have scale — but **they cannot route around ASML.** There is no second EUV source. The power asymmetry runs ASML's way on EUV (the opposite of a typical component supplier). On DUV the customers have more options (Nikon/Canon), which is also where the China policy risk sits.
- **Service (the annuity):** Once a machine ships, ASML earns decades of service, spare parts and field upgrades (Installed Base Management, ~28% of sales). The installed base — and thus the annuity — grows with every shipment. This layer is far less cyclical than new-tool sales.

## Pricing power evidence

- Gross margin ~50-53% and rising toward a 56-60% target by 2030 (Investor Day) — extraordinary for capital equipment.
- EUV ASPs have climbed from ~EUR100M+ (early NXE) to ~EUR350M+ (High-NA EXE:5200), and customers pay because there is no alternative.
- Q1 2026: China (the price-competitive DUV layer) fell to 19% of system sales, yet gross margin still printed 53.0% — because the lost DUV was low-margin and replaced by high-margin EUV. This is the pricing-power tell.

## Where the chain is weakest

- **DUV / China layer:** the mature-node, export-controlled part of the book (Nikon/Canon compete; policy can shut it) — ~20% of 2026 revenue at structural risk (M5).
- **Customer capex cyclicality:** ASML's revenue is a derivative of a handful of customers' capex budgets, which swing hard with the semi cycle (2023 was a down year; FCF fell to EUR4.4B from EUR8.2B).
- **Supplier single-points:** heavy dependence on Zeiss for optics — a strength (shared moat) but also a concentration.
