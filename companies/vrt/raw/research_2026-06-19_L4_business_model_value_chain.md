# VRT Research Run — Layer 4: Business Model, Value Chain & the NVIDIA Integration Stack

- Run date: 2026-06-19
- Method: decomposition of the deep buy-side pack; anchors = VRT Q1'26 release/call (S1/S2), VRT×NVIDIA GB200 NVL72 reference design (2024, S5), liquid-cooling share (S7).
- Status: ⚠️ **UNAUDITED RESEARCH DIGEST.** Not promoted to facts until through `../claim_ledger.csv`.
- Mapped claims: C016–C022, C033

---

# Vertiv — How It Makes Money & Where Profit Is Captured

## 1. ONE-SENTENCE BUSINESS

Vertiv sells **critical digital infrastructure** — the "grey space" power and thermal systems that sit between the utility feed and the IT rack — as a **broad-line, single-vendor integrator**, increasingly as a **co-engineered power *and* thermal stack** validated against NVIDIA reference rack designs, monetized through equipment + a higher-margin recurring **services** layer.

## 2. THE THREE PRODUCT LINES (who pays, why)

| Line | What it is | Why the customer pays | Recurrence | claim_id |
|---|---|---|---|---|
| **Power** | UPS, switchgear, busway/busbar, **increasingly 800V DC** | rack power distribution & protection; reliability is non-negotiable | order-driven; 800V DC launches 2H26, ships 2027 | C016, C017 |
| **Thermal** | CDUs (coolant distribution units), coil / cold-plate, fluid networks, **dry coolers** | rising rack density makes liquid cooling mandatory above ~50kW | order-driven; rising $-content per rack | C016, C021 |
| **Services** | lifecycle (commissioning, maintenance, monitoring) | uptime SLA, speed-to-deploy, single throat to choke | **recurring, higher-margin** | C016 |

**Where the profit is actually captured:** not in any one commodity component, but in **owning the integrated reference design + speed-to-deploy.** VRT's edge is being the only broad-line vendor that ships a *co-engineered power AND thermal stack* for an NVIDIA rack (C019) — the "single throat to choke" for a hyperscaler racing to energize capacity.

## 3. THE NVIDIA INTEGRATION STACK (the differentiator)

- VRT **co-developed the NVIDIA GB200 NVL72 7MW power+cooling reference architecture** (2024, S5) — a *single, validated, fast-deploy* power+thermal design for an NVIDIA rack. (C018)
- This is the closest thing in the value chain to an **industry standard**: when NVIDIA publishes a reference rack, the validated power+thermal stack that ships with it is a default-vendor position.
- VRT is **extending the franchise to 800V DC** (launch 2H26, ship 2027) — next-gen rack power distribution that follows rising density, keeping VRT ahead of the commoditization curve at the *system* layer. (C017)

> The integration stack is the moat's load-bearing element: peers can match individual components, but the *co-engineered, validated, single-vendor power+thermal system* is what a hyperscaler buys for speed. Detail in `../moat_map.md`.

## 4. VALUE-CHAIN MAP — how peers split the chain

```text
Upstream                     Company layer              Downstream                End demand
Cold-plate / CDU /  ───┐
  coolant OEMs         │
  (Boyd, CoolIT,       │
   Modine — inside     ├──► VERTIV (broad-line   ──► Hyperscalers       ──► AI training /
   VRT's BoM)          │     single-vendor            (Big-4 ~75% of        inference compute
Power components /     │     power+thermal+           discretionary
  switchgear OEMs      │     services integrator;     AI capex)
EPC / construction ────┘     NVIDIA reference
                             design authority)
```

**Peers split the chain — VRT spans it:**

| Player | Position vs VRT | Threat type | claim_id |
|---|---|---|---|
| **Schneider Electric** | matches breadth — **the main peer** (~co-leader in liquid cooling) | direct, duopoly | C020 |
| **ABB / Eaton** | **power-weighted** (don't match thermal breadth) | partial (power only) | — |
| **SMCI (Supermicro)** | captures the **server box**, bundles cooling | partial threat (vertical bypass) | — |
| **Boyd / CoolIT / Modine** | cold-plate / CDU component makers — **sit INSIDE VRT's BoM** | input suppliers, not competitors | C022 |

**Profit-pool read:** the **component layer is commoditizing** (cold plates / CDUs multi-sourced; direct-to-chip [DTC] market ~+26% CAGR with many suppliers — C022), so margin there compresses. VRT **defends by owning the system/integration layer** — the validated reference design + breadth + speed-to-deploy — and supplies *into* the commoditizing component layer rather than competing in it. (C033)

## 5. PORTER (quick)

| Force | Strength | Note |
|---|---|---|
| Supplier power (component OEMs) | **Low–Medium** | cold-plate/CDU multi-sourced; they sit inside VRT's BoM |
| Buyer power (Big-4 hyperscalers) | **High & concentrated** | ~75% of demand is 4 customers' discretionary capex (C023) |
| New entrants | **Medium** | component entry easy; *integrated validated single-vendor stack* is the gate |
| Substitutes | **Medium** | SMCI bundled box; ODM direct-to-chip — contained, not zero |
| Rivalry | **High** | Schneider co-leads; ABB/Eaton power-weighted |

## 6. TEN-YEAR EXISTENCE TEST

- **Problem in 10 years?** Yes — datacenters will always need power + thermal; rising density makes the thermal problem *harder*, not easier.
- **Why VRT remains well-placed?** Owns the integration/reference-design layer + breadth + speed; extending to 800V DC; #1 (tied) liquid-cooling share.
- **What changes the thesis?** Hyperscaler capex slope rolling over (no floor, highest beta); component commoditization bleeding *up* into the system layer; Schneider out-executing. (see `../inversion_map.md`)

---

**Bottom line for the memo:** VRT is a broad-line "grey-space" integrator whose durable profit comes from **owning the co-engineered, NVIDIA-validated power+thermal reference stack + speed-to-deploy + services**, not from any one commodity component. Peers split the chain (Schneider breadth, ABB/Eaton power, SMCI server box); the cold-plate/CDU makers sit *inside* VRT's bill of materials. The franchise extends to 800V DC. The structural caveat: the system layer is strong, but ~75% of demand is four hyperscalers' discretionary capex — the business spans the value chain but rides the capex cycle (see `../bottleneck_map.md`).
