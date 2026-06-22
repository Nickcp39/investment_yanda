# Business Model — NBIS

Last updated: 2026-06-18

Source base: business-model + contract-quality raws (SRC-001, SRC-002), facts.md. Facts: `facts.md` / `claim_ledger.csv`.

## One-Sentence Business

NBIS rents AI-optimized GPU compute (training + inference) from data centers it largely owns — sold via a three-tier model dominated today by two long-dated take-or-pay anchor contracts (Microsoft, Meta), with a fast-growing but still-small self-service / inference (AI Studio / "Token Factory") book and a portfolio of non-core stakes (ClickHouse, Avride, Toloka, TripleTen) used as funding.

## Who Pays?

| Customer | Product | Why they pay | Recurrence | Evidence |
|---|---|---|---|---|
| **Microsoft** | dedicated GPU capacity (Vineland NJ) | own-capacity shortfall; speed-to-GPU | 5-yr take-or-pay, monthly through Oct 2031 | C013, C014 |
| **Meta** | dedicated compute (Vera Rubin from 2027) | capacity for AI buildout | 5-yr; $12B firm + $15B optional | C047 |
| **25+ named enterprises** (Cloudflare, Prosus, Shopify, Revolut, monday.com, Sword Health, 1X…) | AI Cloud + Token Factory inference | cheaper/faster than building or hyperscalers | committed + on-demand | C048 |
| **AI-native / model builders** (Recraft, Prime Intellect, Higgsfield…) | reserved GPU clusters | need frontier GPUs (B200/GB200) at scale | reserved | C048 |
| **Sovereign (UK)** | NBIS-built capacity (14k Blackwell) | EU/UK data sovereignty | multi-year build | C048 |

## Revenue Engine

| Revenue stream | Pricing unit | Volume driver | Price driver | Main risk |
|---|---|---|---|---|
| **Anchor contracts (MSFT/Meta)** ~most of contracted $ | $/GPU committed, take-or-pay | capacity built & energized | private; ~$6.96B MSFT upfront | concentration; delivery slip → termination/LD (C015) |
| **Reserved / committed clusters** | $/GPU-hr (H100 $2.15…) | enterprise + model-builder demand | raised in Q1'26 (sold out) | commoditization as supply catches up |
| **On-demand / self-service** | $/GPU-hr (H100 $3.85…) | self-serve pipeline +3.5× QoQ | sold out, pricing power now | spot prices fall (Hopper −28% YoY) |
| **AI Studio / Token Factory** | per-token inference | inference shift | managed-platform premium | not separately disclosed; small $ today |
| **Non-core stakes (SOTP)** | n/a — monetized to fund capex | round/IPO events | mark-to-market | non-cash; lumpy (ClickHouse +$780.6M Q1'26) |

**Revenue mix:** AI Cloud ≈ **98%** of group revenue; Token Factory is the fastest-growing line but immaterial in dollars so far. (C049) Committed-vs-spot split is **not disclosed** — the single biggest revenue-quality unknown after concentration.

## Ten-Year Existence Test

- **Problem in 10 years?** Yes — demand for AI compute (esp. inference) is structurally growing; someone must own/operate the data centers.
- **Why NBIS remains well-placed?** Owned capacity (>75%), cheap clean Nordic power, deep NVIDIA relationship, full-stack + managed inference, EU/sovereign positioning.
- **What changes the thesis?** Hyperscaler in-house silicon (TPU/Trainium) commoditizing Nvidia-rental; the AI-capex cycle reversing; GPU residual-value collapse. (see `inversion_map.md`)

## Business Quality Scorecard

| Question | Answer | Evidence | Score (1–5) |
|---|---|---|---:|
| High willingness to pay? | Yes now — sold out, raised prices, take-or-pay anchors | C029, C014 | 4 |
| Recurring / habit-forming? | Contracted (sticky if NBIS delivers) but compute is movable; weak switching costs | C015, moat_map | 3 |
| Does scale improve economics? | Yes (GM ~69%, cost of rev 49%→26%) — **but** capex ~7× revenue offsets it | C007, C005 | 3 |
| Reinvest at attractive returns? | Demand huge, but ROIC negative today; returns are a forecast | financial_quality | 2 |
| Inside circle of competence? | Requires underwriting GPU cycle + AI capex cycle + hyperscaler strategy — hard | step0_plan | 2 |

**Net:** a real, improving business with genuine pricing power *today*, but quality is gated by extreme capital intensity, concentration, and weak switching costs. Not yet a high-quality compounder; it's an early-cycle, capacity-led growth business priced like a winner (see `valuation.md`).
