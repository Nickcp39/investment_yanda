# Bottleneck Map — NBIS

Last updated: 2026-06-18

Purpose: identify where scarcity creates pricing power, strategic control, or vulnerability — and answer the LEAD question: **is power / "building power plants" the binding bottleneck on NBIS's buildout?**

---

## TL;DR — the power question, answered

**The premise "NBIS builds power plants and power is the bottleneck" is wrong on both counts.**

1. **NBIS does not build power plants.** It builds/owns **data centers** (>75% of contracted power is owned facilities — 3 GW across 5 sites) that draw contracted grid/utility power. At some US sites it uses **behind-the-meter on-site gas** (New Jersey ~85% gas) and the **Bloom Energy** fuel-cell deal — but those are built/operated by **partners**; NBIS is the offtaker, not a generation business. (C028, C024, C025)

2. **Power *availability* is NOT the binding constraint** — NBIS has already locked up **>3.5 GW contracted (guide >4 GW YE2026)**, top-tier among pure-play neoclouds. Demand is the opposite of a problem: "everything we build is sold," "4+ customers per GPU," prices raised and still sold out. (C018, C029)

3. **The real binding constraint is "capacity" — the speed of converting contracted power into *connected → active* (energized, GPU-filled, revenue-generating) data centers.** Management says this in plain words: *"Capacity today is the main bottleneck to revenue growth."* (C021)

4. **The hardest sub-link is the physical build-and-energize chain**, specifically **long-lead electrical equipment** — Volozh: *"massive shortages in basic physical components, like transformers and gas generators."* Grid interconnection is a real friction that NBIS **deliberately routes around** with behind-the-meter generation. (C022, C024, C025)

5. **What is NOT the bottleneck:** GPU allocation (de-risked via NVIDIA), capital (>$9.3B cash, RPO $33.6B + prepayments as financing), and demand. (C023, C009, C029, C044)

> So if you're worried "can they get the power?" — largely yes, already contracted. The thing that actually gates revenue is **how fast contracted megawatts become live megawatts** — and the scarce inputs there are transformers/switchgear/gas-gens, construction speed, and interconnection timing. The single most decision-relevant number — **active power (live MW)** — is the one NBIS stopped disclosing after YE2025 (~170 MW). (C020)

---

## Bottleneck Inventory

| Bottleneck | Type | Who controls it? | Evidence | Is it binding for NBIS? | Beneficiary |
|---|---|---|---|---|---|
| **Build-and-energize cycle** (contracted→connected→active MW) | physical / capital | NBIS + EPC/equipment/utility partners | Mgmt names "capacity" as THE bottleneck; active power only ~170MW YE2025 vs >3.5GW contracted (C019–C021) | **YES — #1** | whoever can build fastest |
| **Long-lead electrical gear** (transformers, switchgear, gas gensets) | physical supply chain | Global OEMs (industry-wide shortage) | Volozh quote (C022); COO low-single-digit component inflation (C022) | **YES — #2 (hardest input)** | incumbents w/ supplier relationships |
| **Grid interconnection / power delivery** | physical / regulatory | Utilities, ISOs (PJM etc.) | NJ gas microgrid + Bloom 328MW exist to *bypass* queues (C024, C025) | **Partial — routed around**, not a hard ceiling | players who self-generate / pick friendly utilities |
| **Power availability (contracted MW)** | physical / capital | NBIS (via land+power contracts) | >3.5GW contracted, >75% owned, guide >4GW (C018) | **NO — largely secured** | NBIS (top-tier position) |
| **GPU allocation** | supply / relationship | NVIDIA | "last year's problem"; $2B NVIDIA equity + early Rubin access (C023, C034) | **NO — de-risked** | NVIDIA partners |
| **Capital / financing** | capital markets | NBIS + debt/equity + customer prepays | $9.3B cash; RPO $33.6B + $4.8B deferred rev; converts (C009, C044, C046) | **NO — abundant now** (but see capital-intensity risk) | well-funded scaled players |
| **Demand** | market | AI labs / hyperscalers | sold out, 4+ customers/GPU, raised prices (C029) | **NO — excess demand** | all capacity owners |
| **Liquid cooling / shell (GB200/GB300)** | physical / technical | NBIS + DC builders | already runs GB300 NVL72 w/ closed-loop cooling (Finland) | folded into build speed | technically-capable operators |

---

## The "power as bottleneck" question, dissected

**Three distinct things get conflated under "power":**

| If "power bottleneck" means… | Verdict for NBIS | Why |
|---|---|---|
| Can they secure enough electricity (contracted MW)? | **Not a constraint** | >3.5 GW already contracted; top-tier vs peers (C018) |
| Can they get it *delivered* (grid interconnection)? | **Friction, but engineered around** | Behind-the-meter gas (NJ) + Bloom fuel cells bypass utility queues (C024, C025) |
| Can they *energize and fill* it fast enough (build-out)? | **YES — this is the real bottleneck** | "capacity is the main bottleneck"; transformer/gen shortages (C021, C022) |

**Does NBIS build power plants?** No. It (a) signs power/land contracts with utilities, (b) at US sites contracts **partners** to build behind-the-meter on-site gas generation (DataOne in NJ; Bloom fuel cells in MO), and (c) buys the output. The closest thing to "owning a power plant" is a municipal utility (Independence Power & Light) *rebuilding* the Blue Valley gas plant to serve NBIS's Missouri campus — but NBIS doesn't own it. (C024, C025, C026, C028)

---

## Questions (the template's bottleneck tests)

- **Can competitors buy around the bottleneck?** Partly. The bottleneck is industry-wide (everyone faces transformer/gen shortages and interconnection queues). NBIS's *relative* edge is (i) >75% owned capacity, (ii) cheap clean Nordic power + free cooling, (iii) early behind-the-meter generation. CoreWeave is ahead on *active* MW; Crusoe has native bring-your-own-generation. So NBIS is top-tier but not uniquely advantaged — the bottleneck is shared, and being first/fastest is the game.
- **Temporary or structural?** Mostly **structural for 2026–2028** (the AI buildout super-cycle keeps electrical-equipment and construction supply tight), but it is a *speed/throughput* constraint, not a permanent ceiling. As supply chains catch up, the constraint eases — which is double-edged (see Risk).
- **Does the company own the bottleneck or merely depend on it?** It **depends on** the build-and-energize chain (it owns the DCs but relies on equipment OEMs, EPCs, utilities, and partner-generators). It does **not own** the scarce input (transformers/gens). This is a dependence, not a moat.
- **Does solving it improve economics or destroy returns via capex?** This is the crux. Converting contracted→active requires **$20–25B/yr capex (C032)** against deeply negative FCF (C010). Every megawatt energized adds revenue **and** capital intensity. Returns only compound if utilization stays high and GPU residual values hold — see `inversion_map.md` (depreciation path) and `valuation.md`.

---

## Risk — the bottleneck is not a moat

A bottleneck this capital-hungry is as much a **vulnerability** as an advantage:

1. **It's a capacity ceiling on revenue.** Revenue is literally gated by how many MW go active. Miss the build schedule → miss revenue → (if it's a delivery commitment) trigger Microsoft's late-delivery liquidated-damages/termination clause (C015). The bottleneck *is* the churn risk.
2. **It's a cost sink.** "Solving" it = $20–25B/yr capex, ~7× revenue, FCF ≈ −$3.7B (C005, C010). The bottleneck consumes the capital that the bull case assumes compounds.
3. **It eases for everyone eventually.** When transformer/gen/construction supply catches up, the scarcity that lets NBIS "sell out at higher prices" (C029) also lets competitors and hyperscalers add supply → commoditization + pricing pressure (the neocloud bear case).
4. **The key metric is hidden.** NBIS discloses contracted power (impressive) but **not** Q1'26 active power (the number that proves conversion). Watch this — see `monitor.md`.

**Bottom line:** Power isn't the wall; the *build-and-energize throughput* is — and it's a throughput constraint that costs $20–25B/yr to push against, with the proof-of-conversion metric (active MW) currently undisclosed.

---

*Linked: `value_chain_map.md` (where the scarce inputs sit), `inversion_map.md` (how the build chain breaks the thesis), `monitor.md` (active-power + tranche-delivery early-warning).*
