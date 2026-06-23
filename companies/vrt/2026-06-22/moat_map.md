# Moat Map — VRT

Last updated: **2026-06-22** (refreshed from 2026-06-19 seed; thesis unchanged)

Source base: moat/bottleneck raw (S5, S7, S2), facts.md. Pairs with `bottleneck_map.md`.

## Moat Summary

| Moat source | Evidence | Metric | Durability | Attack surface |
|---|---|---|---|---|
| **Intangible / design authority** | **co-developed NVIDIA GB200 NVL72 7MW power+cooling reference architecture** — closest thing to a standard | n/a | **Medium–High** | NVIDIA could broaden reference partners; standards evolve |
| **Switching costs** | integrated, validated, fast-deploy single-vendor power+thermal system | qualitative | **Medium** | per-rack, not per-fleet; no take-or-pay lock-in |
| Network effects | none meaningful | — | None | — |
| **Cost / breadth advantage** | only broad-line vendor spanning power AND thermal for an NVIDIA rack; ThermoKey adds heat-rejection breadth | ~20% adj op margin, expanding to 27% | **Medium** | Schneider matches breadth (co-leader) |
| Efficient scale | #1 liquid-cooling share ~11.3% (2025) | share | **Medium** | duopoly — Schneider ~tied; component layer commoditizing |
| Supplier access | cold-plate/CDU OEMs sit *inside* VRT's BoM | — | Medium | multi-sourced; ThermoKey internalizes some dry-cooler supply |
| Technology extension | **800V DC** launch 2H26, ship 2027 | — | **Medium–High** | keeps VRT ahead at the system layer as components commoditize |

## ROIC–WACC Lens

- **Current ROIC: positive and rising** — ~20% adjusted operating margin FY25, guided 22.8–23.8% FY26, 27% target 2030; FCF-positive (~$1.9B FY25). **Unlike NBIS, the excess returns exist today** — the question is durability through the cycle, not existence. (C002, C014, C032)
- Estimated WACC: mid-to-high single digits / low teens (FCF-positive, net cash, but high-beta).
- **Spread: positive today.** Excess returns are real now; the risk is the *competitive-advantage period* being capped by the capex cycle, not by the moat eroding.
- Reinvestment runway: large (rising density → rising $-content per rack) — but gated by the hyperscaler capex slope, not by VRT's reinvestment ability.
- Competitive-advantage period: **medium** — anchored to NVIDIA reference-design authority + being first/fastest with the integrated stack; persists as long as density keeps rising AND the capex slope holds.

## Moat verdict

**A genuine, share-gaining integration moat — but one with no cycle shock-absorber.** The moat is real and *causes excess returns today* (unlike NBIS): design authority over NVIDIA reference racks, the only broad-line single-vendor power+thermal stack, #1 (tied) liquid-cooling share, extending to 800V DC and (via ThermoKey) deeper into heat-rejection. It governs **share** — VRT keeps winning content per rack. What it does **not** govern is **cycle exposure**: ~75% of demand is four hyperscalers' discretionary capex with no contracted floor (the highest-beta name in the basket). So the moat is durable *for share*, fragile *for cycle*. It hardens further if 800V DC extends the system-layer lead and liquid-cooling share rises vs Schneider; it weakens if the component commoditization bleeds up into the system layer or Schneider out-executes.

## Moat Falsification — the moat is weaker than we think if:

- [ ] Liquid-cooling share **slips toward Schneider / ODMs** (the duopoly tilts against VRT).
- [ ] DTC / ODM bypass (SMCI-style bundled box) takes share at the **system** layer, not just components.
- [ ] **800V DC fails to extend** the franchise (commoditization reaches the power layer).
- [ ] NVIDIA broadens reference-design partners → design-authority edge dilutes.
- [ ] A hyperscaler capex air-pocket shows the moat governs *share* but not *cycle* — the $110.06 low (~one year ago) is the reminder that share leadership did not provide a floor.

## Notes

Per the guardrail: a moat must cause *persistent* excess returns. VRT **clears that bar today** (positive, expanding ROIC) — which is the key difference from NBIS (negative ROIC, "not a moat yet"). VRT's moat is real. The discipline here is the opposite of NBIS's: don't let "the moat is real" obscure that **the moat does not insulate against the capex cycle** — see `bottleneck_map.md` (integration bottleneck owned, component bottleneck supplied into, capex-slope switch shared) and `inversion_map.md` (no floor). The refresh (price $333→$345) does not change the moat read; it only makes the *price* paid for this share-but-not-cycle moat richer (see `valuation.md`).
