# IDXX Value Chain Map (M3 companion)

Last updated: 2026-07-05 | as_of: 2026-07-05 | sources: facts.md, business_model.md

---

## Chain

```
Upstream                    IDEXX                              Downstream
--------                    -----                              ----------
Optics/sensors/reagent   -> R&D + manufacturing of           -> Veterinary practices
raw materials, camera       analyzers (Catalyst, ProCyte,        (independent + corporate-owned
components, chemistry       SediVue, inVue Dx) + consumables     e.g. Banfield/VCA/BluePearl)
supply chain (not            (slides/cartridges/reagents)      -> Reference lab customers (practices
independently verified                                            without in-house instruments)
this run)                -> AI models trained by IDEXX        -> Corporate veterinary networks
                             board-certified pathologists         (Mars-owned Banfield/VCA/BluePearl,
                             (inVue Dx cytology interpretation)    National Veterinary Associates, etc.)
                          -> Practice-management software      -> Pet owners (end consumer, pays the
                             (Cornerstone/ezyVet/Neo) +            practice, not IDEXX directly --
                             VetConnect PLUS connectivity          IDEXX is B2B, one step removed from
                          -> Reference laboratory network          the ultimate demand shock absorber)
                             (runs complex assays practices
                             can't do in-house)
```

**Key structural feature**: IDEXX sits between pet owners' willingness-to-pay (proxied by vet-visit
frequency and per-visit diagnostic spend) and veterinary practices' purchasing decisions. IDEXX does NOT
sell to the end consumer — it sells diagnostic capability to the practice, which then bills the pet owner.
This means IDEXX's revenue is a function of (a) how many pets visit vets, (b) how many tests each visit
generates, and (c) what fraction of those tests run on IDEXX vs competitor equipment/reference labs.

---

## Profit Pool Table

| Layer | Owns the profit pool? | Evidence | Durability |
|---|---|---|---|
| Instrument manufacturing (hardware) | Partial — low/breakeven-margin "razor," not the profit driver | E18: $200.2M instrument revenue vs $3,407.2M recurring revenue | Low margin by design; strategic, not profit-driven |
| Consumables (VetLab slides/cartridges/reagents) | **YES — the core profit pool** | E14: $1,496.8M, +14.8% reported, fastest-growing recurring line | High — genuine razor/blade lock-in, proprietary consumable formats |
| Reference lab services | **YES — second profit pool** | E15: $1,424.1M, +6.6% reported | High — requires IDEXX's own lab network/logistics, a real scale barrier |
| AI/software layer (inVue Dx algorithms, VetConnect, practice software) | Emerging — real product, ASP contribution not separately quantified | E59-E62; facts.md O5 | Unclear yet — genuinely differentiated technically, monetization mechanism (embedded in instrument+consumable pricing, not separately metered) makes it hard to isolate as its own profit pool |
| Rapid assays (SNAP tests) | Weakening — the one shrinking recurring line | E16: −3.0% reported FY2025 | Lowest — most commoditized, most exposed to Zoetis/generic competition |
| Downstream (veterinary practices) | No — practices capture value via service fees to pet owners, not from IDEXX's product margin | — | N/A — IDEXX's customer, not IDEXX's competitor for the profit pool |

---

## Bottleneck Candidates (full detail in bottleneck_map.md)

1. **Installed-base consumable lock-in** (proprietary slide/cartridge formats, not interchangeable across
   vendors) — the classic, strongest bottleneck.
2. **Reference-lab logistics/scale** (national/international courier network, sample-processing capacity)
   — a genuine infrastructure barrier a software-only or hardware-only entrant cannot quickly replicate.
3. **AI-model training data** (IDEXX's proprietary corpus of pathologist-labeled cytology/blood-morphology
   images used to train the inVue Dx models) — potentially a genuine, compounding data-moat if IDEXX
   continues to be the largest single source of vet-diagnostic imaging data, though NOT independently
   quantified this run (no disclosed dataset size, model-accuracy benchmark vs competitors, or third-party
   validation found — flag for next refresh).
4. **INVERTED bottleneck (against IDEXX)**: Mars Petcare's captive ~2,500-hospital network (Banfield, VCA,
   BluePearl) owning Heska analyzers + Antech reference labs creates a channel where Mars can direct its
   OWN hospitals' diagnostic spend to its OWN diagnostics business, structurally excluding IDEXX from that
   subset of the market regardless of product merit. This did not exist as a combined entity before the
   2023 Heska acquisition and is the most significant NEW competitive-structure risk versus a decade ago.
