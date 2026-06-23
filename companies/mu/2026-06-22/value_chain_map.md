# MU Value Chain Map — as_of 2026-06-22

## Where Micron sits

```
[Equipment: ASML / AMAT / Lam / Tokyo Electron]  ->  [MEMORY MAKERS: Micron / SK Hynix / Samsung]  ->  [Advanced packaging / OSAT]  ->
   (litho, etch, deposition)                          (DRAM, HBM, NAND)                                (HBM stacking, CoWoS-adjacent)
        ^ upstream pricing power                            ^ MICRON                                         |
                                                                                                             v
                                          [GPU/accelerator makers: NVIDIA, AMD, custom ASIC] -> [Hyperscalers / AI clouds] -> [Enterprises]
                                                   (HBM is a critical input)                       (the demand source)
```

## Profit-pool position

- **Micron is a component supplier into the AI compute stack.** HBM is a *critical, scarce input* to every
  high-end AI accelerator (NVIDIA Vera Rubin uses Micron HBM4). This gives Micron a seat at the AI-economics
  table it never had in commodity memory — but it is a *supplier* seat, not the bottleneck owner (NVIDIA is).
- **Upstream (equipment):** ASML/AMAT/Lam have their own pricing power; Micron's capex flows partly to them.
- **Peers (the oligopoly):** SK Hynix (HBM leader, ~53-62%), Samsung (~25-35%), Micron (#3, ~11-20%). DRAM is
  a true 3-player oligopoly — the consolidated structure is the source of whatever pricing discipline exists.
- **Downstream (customers):** NVIDIA/AMD/custom-ASIC makers buy HBM; hyperscalers buy DRAM/SSD directly and
  indirectly. Customer concentration is rising toward AI/data-center.

## Value-capture read

- In the **commodity** layer (majority of bits), Micron is a price-taker; the pool is cyclical and shared.
- In the **HBM/leading-node DC-DRAM** layer, Micron captures genuinely higher margins (74% BU GM) because the
  product is technically gated (advanced packaging, leading-edge yield) and capacity-allocated under
  multi-year contracts. This is the structurally better pool — but Micron holds the *smallest* share of it.
- **Net:** Micron captures real, growing economics from the AI buildout, but as the #3 player in the
  differentiated pool and a price-taker in the commodity base. The capture is strong NOW; its durability
  depends on holding HBM share through the HBM4/HBM4E transition.
