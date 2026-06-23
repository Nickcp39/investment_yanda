# Business Model — VRT

Last updated: **2026-06-22** (refreshed from 2026-06-19 seed)

Source base: business-model + value-chain raw (S1, S2, S5, S7), facts.md. Facts: `facts.md` / `claim_ledger.csv`.

## One-Sentence Business

Vertiv sells **critical digital infrastructure** — the "grey space" power and thermal systems between the utility feed and the IT rack — as a **broad-line, single-vendor integrator**, increasingly as a **co-engineered power *and* thermal stack** validated against NVIDIA reference rack designs, monetized through equipment plus a higher-margin recurring **services** layer.

## Who Pays?

| Customer | Product | Why they pay | Recurrence | Evidence |
|---|---|---|---|---|
| **Hyperscalers (Big-4)** | integrated power + thermal stack for AI racks | speed-to-deploy; single validated vendor; reliability is non-negotiable | order-driven (backlog), ~75% of demand | C018, C023 |
| **Colocation / enterprise DC** | UPS, switchgear, busway, CDUs, thermal | grey-space reliability + density support | order-driven + services | C016 |
| **Existing installed base** | lifecycle services (commissioning, maintenance, monitoring) | uptime SLA, single throat to choke | **recurring, higher-margin** | C016 |

## Revenue Engine

| Revenue stream | Pricing unit | Volume driver | Price driver | Main risk |
|---|---|---|---|---|
| **Power** (UPS, switchgear, busway, **800V DC**) | $/system | rack count + density; 800V DC from 2027 | integration + reliability premium | ABB/Eaton/Schneider; commoditization at component edge |
| **Thermal** (CDUs, cold-plate, fluid networks, dry coolers) | $/system; **$-content/rack rises with density** | liquid mandatory above ~50kW | system/integration premium | cold-plate/CDU commoditizing (DTC +26% CAGR) |
| **Services** (lifecycle) | contract / per-event | installed base | recurring premium | in-house / third-party service |

**Where profit is captured:** not in any one commodity component, but in **owning the integrated, NVIDIA-validated reference design + speed-to-deploy.** VRT is the **only broad-line single-vendor integrator shipping a co-engineered power AND thermal stack for an NVIDIA rack** (C019). Peers split the chain (Schneider breadth, ABB/Eaton power, SMCI server box); cold-plate/CDU makers (Boyd/CoolIT/Modine) sit *inside* VRT's bill of materials (C022). The 800V DC programs (launch 2H26, ship 2027) extend the franchise (C017). **The ThermoKey acquisition (closed 2026-06-12, C034) deepens the thermal chain into heat-rejection and shores up the structurally weak EMEA region** (where Q1'26 organic was −29%).

## Ten-Year Existence Test

- **Problem in 10 years?** Yes — datacenters always need power + thermal; rising rack density makes the thermal problem *harder*, not easier.
- **Why VRT remains well-placed?** Owns the integration/reference-design layer + breadth + speed; extending to 800V DC; #1 (tied) liquid-cooling share (~11.3%); now deeper in heat-rejection (ThermoKey).
- **What changes the thesis?** Hyperscaler capex slope rolling over (no floor, highest beta); component commoditization bleeding *up* into the system layer; Schneider out-executing. (see `inversion_map.md`)

## Business Quality Scorecard

| Question | Answer | Evidence | Score (1–5) |
|---|---|---|---:|
| High willingness to pay? | Yes — speed-to-deploy + reliability + validated NVIDIA stack | C018, C019 | 4 |
| Recurring / habit-forming? | Services recurring; hardware order-driven; switching cost = validated fast-deploy system, but no take-or-pay | C016, C024 | 3 |
| Does scale improve economics? | Yes — margins *expanding* (20.4%→22.8–23.8% guide) as it grows; FCF-positive | C002, C014 | 4 |
| Reinvest at attractive returns? | Yes — positive ROIC today; net cash funds bolt-on thermal M&A (ThermoKey) + buybacks | C028, C034 | 4 |
| Inside circle of competence? | Requires underwriting the hyperscaler capex cycle (highest-beta name) | step0_plan | 3 |

**Net:** a genuinely **high-quality** business — real pricing power, expanding margins, strong cash conversion, a defensible integration moat. It is *not* a low-quality cyclical. The two things that keep it from a clean CORE buy are **price** (~50-54x forward at $345, `valuation.md` — richer than the seed's ~48x) and **cycle exposure with no floor** (~75% downstream of four hyperscalers' discretionary capex, `bottleneck_map.md`) — plus the one disclosure blemish (still-withheld orders/B2B). Quality is high; the gate is valuation + beta + transparency, not the business.
