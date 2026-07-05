# BFLY Value Chain Map (M2 companion)

Last updated: 2026-07-04 | as_of: 2026-07-04 (as_of_price $7.68) | sources: facts.md, source_register.md

---

## Industry Definition

On the surface, Butterfly looks like a medical-device company (point-of-care ultrasound / POCUS). Underneath, it is better analyzed as a **fabless semiconductor company with a medical-device go-to-market layer bolted on top** — the wafer is fabricated at TSMC exactly like any other chip company's silicon [E12], and the company is now explicitly monetizing that chip IP outside medicine entirely via Butterfly Embedded [E52-53]. This dual identity matters: it means BFLY inherits both medtech-style risks (FDA clearance, clinical litigation, hospital sales cycles) AND semiconductor-style risks (single-foundry dependence, Taiwan geopolitical concentration) that a "normal" medical-device company sourcing commodity piezo crystals from multiple vendors would not carry to the same degree.

---

## Core POCUS Value Chain — From Wafer to Patient

```text
[TSMC — Taiwan]  →  [Benchmark Electronics — Thailand]  →  [BUTTERFLY]  →  [Customers]  →  [Patient]
  Wafer fab of         Assembly/test of                    Chip design IP    Hospital        Diagnostic
  Ultrasound-on-       finished iQ+/iQ3                     + AI/software     systems          imaging at
  Chip semiconductor   probes                                + brand           Individual       point of
  (non-exclusive FSA,                                        + direct sales/   clinicians       care
  min-purchase                                                distributors     Veterinarians
  commitment)                                                                  (unnamed 11%-
                                                                                concentration
                                                                                customer, O1)
     ↑                        ↑                                  ↑
  E12                        E12                            E12, E13, E52,
  SINGLE-SOURCE                                              E55, E62-64
  SUPPLY RISK
```

**Where Butterfly captures value**: chip design (IP, ~665 patents expiring 2030-2046, E13), the AI/software layer built on top of the imaging data (Compass AI, Gestational Age tool, E52/E55), and the brand/direct-sales relationship with clinicians. Butterfly does **not** capture manufacturing margin — it is asset-light/fabless by design, outsourcing both wafer fabrication (TSMC) and final assembly (Benchmark) [E12]. This is analogous to how a fabless semiconductor company (e.g., the broader industry pattern of design-house-plus-foundry) separates IP/design value from manufacturing scale value — except here the end customer is a hospital, not another electronics company.

**Where Butterfly is exposed**: the flip side of being asset-light is being **single-source dependent**. The Foundry Service Agreement with TSMC is non-exclusive (meaning BFLY has no exclusivity claim on TSMC's capacity) and carries a minimum-purchase commitment (meaning BFLY has a fixed downside cost obligation even if volumes disappoint) [E12]. Taiwan-based wafer fabrication is a genuine, direct geopolitical exposure — this is not a generic "supply chain risk" boilerplate line, it is the literal, physical location where 100% of Butterfly's core product's most valuable component is made. A medical-device company sourcing off-the-shelf piezo crystals from multiple vendors would not carry this specific concentration; a chip company by definition does. See bottleneck_map.md for the full risk treatment.

---

## Profit Pool by Layer

| Layer | Players | Revenue pool (BFLY-attributable) | Margin/return profile | Bargaining power |
|---|---|---|---|---|
| Upstream — wafer fab | TSMC (sole source) [E12] | Not disclosed (COGS input, embedded in Product cost) | TSMC's own margins are not BFLY's to capture; BFLY pays foundry pricing + minimum commitment | HIGH (TSMC) — non-exclusive FSA, BFLY is a small customer relative to TSMC's overall book; BFLY has no leverage to demand priority capacity |
| Upstream — assembly/test | Benchmark Electronics, Thailand [E12] | Embedded in Product COGS | Standard contract-manufacturing margins (not BFLY's) | Moderate — assembly/test is a more commoditized, multi-sourceable step than wafer fab |
| **Company layer — chip design + software + brand** | **Butterfly** | Product $63.44M (65.0%) + Software/services $34.17M (35.0%) = $97.61M FY25 [E15] | GAAP gross margin 46.9% FY25 (one-off-depressed) / adjusted 64.9% FY25 -> 68.9% Q1'26 [E16, E26] | BFLY has real brand/patent position (E13) but has historically lacked pricing power strong enough to reach profitability (net loss -$77.1M FY25, E19) |
| **Company layer — Embedded licensing (separate value-capture logic)** | **Butterfly (licensor) + Midjourney and 8 other partners (licensees)** [E53-54] | Midjourney: $15M one-time + $10M/yr (5yr) + up to $9M milestones + rev-share [E53]; contributed $6.8M of Q4'25 revenue alone | Near-100% margin (licensing, minimal COGS) — the single biggest driver of the 5-quarter gross-margin improvement per I1 | BFLY holds the IP being licensed — favorable position in this specific relationship, though the counterparties (Midjourney et al.) chose to license rather than build their own chip, implying the make-vs-buy economics favored licensing for them at this scale |
| Downstream — hospital systems / distributors | Unnamed; ~11% revenue concentration in one unnamed customer [E59] | N/A (customer, not a value-chain layer BFLY monetizes further) | N/A | Some leverage — large health systems and the unnamed 11%-customer likely have negotiating power on price/terms; distributor economics not disclosed |
| Downstream — individual clinicians/vets | 145,000 unique device users, 100+ countries [E59] | N/A | N/A | LOW individually — fragmented, price-taking customer base; this fragmentation is actually favorable to BFLY (no single individual clinician has leverage) |
| End demand | Patients (imaging), and indirectly Midjourney's own end-customers (non-medical) | N/A | N/A | N/A |

---

## The Second, Structurally Different Value Chain: Butterfly Embedded

Butterfly Embedded is not a downstream extension of the POCUS chain above — it is a **parallel value chain** where Butterfly stops at IP/platform licensing and lets the licensee build and own the entire downstream product and customer relationship:

```text
[TSMC/Benchmark — same chip supply chain, E12]  →  [BUTTERFLY — licenses chip IP/platform]  →  [Licensee builds OWN product]  →  [Licensee's OWN customers]
                                                        ↑                                            ↑
                                                   E52-53: exclusive,                          Midjourney: builds its own
                                                   non-transferable,                            AI-image-generation-adjacent
                                                   field-of-use-limited                         hardware; BFLY does not
                                                   license; $15M+$10M/yr                         control or capture value
                                                   (5yr)+$9M milestones+                         from what Midjourney
                                                   rev-share+chip-purchase                       ultimately builds beyond
                                                   payments                                      the license/royalty terms
```

This is a **fundamentally different value-capture model** from the core POCUS business:

- **Core POCUS**: BFLY owns the entire chain from chip design through direct customer relationship through software subscription revenue — a direct-to-customer model where BFLY captures value at multiple touchpoints over the life of the customer relationship (hardware sale + recurring software).
- **Butterfly Embedded**: BFLY captures value **once, at the licensing/royalty layer**, and then the licensee (Midjourney, or one of 8 other signed partners, E54) owns everything downstream — product design, branding, end-customer relationship, and most of the ultimate value creation if the licensee's product succeeds. BFLY's economics here resemble a technology-licensing business (fixed fee + milestones + revenue share) more than a medical-device annuity — closer in kind to how a component-IP licensor operates than to how Butterfly's own core hardware/subscription business operates.

The coexistence of these two models inside one company is itself notable: it means BFLY's revenue mix going forward depends on two different sales/business-development motions (direct clinical sales vs. enterprise technology licensing) that require different organizational capabilities. Butterfly Garden (30 partners, a software-app marketplace built on BFLY's SDK) is a third, related-but-distinct ecosystem play, separate from the 9-partner Embedded licensing program [E54] — facts.md does not clarify the exact boundary or overlap between Garden and Embedded partners, which is worth flagging as a minor definitional gap.

---

## Supply / Demand Dynamics

- **Demand drivers**: POCUS adoption trend (cost/portability advantage over $30-120k cart-based ultrasound, E64); expanding AI/software feature set (Gestational Age AI, E55/E78) that widens clinical use cases; Embedded-licensing demand from non-medical technology companies wanting sensing/imaging capability without building their own chip (validated by Midjourney + 8 other signed partners, E53-54).
- **Supply constraints**: single-source TSMC wafer fab with a non-exclusive agreement and a minimum-purchase commitment [E12] — this is the binding physical constraint in the entire chain (detailed in bottleneck_map.md).
- **Cyclicality**: not strongly evidenced either way in facts.md; revenue has grown in each disclosed period (FY23->FY24->FY25->Q1'26, E15/E25) with no cyclical downturn on record, but the company is young (SPAC-merger 2021, E8) and has not been tested through a full economic cycle.
- **Pricing mechanism**: list pricing on hardware ($2,700-3,900, E52) positioned as a discount to alternatives [E64] — suggests BFLY is currently a price-taker/value-competitor in hardware, not a price-setter; software subscription pricing ($300-420/yr) is company-set; Embedded licensing pricing is individually negotiated per deal (Midjourney terms disclosed exactly, E53; other 8 partners' terms not disclosed).
- **Substitute pressure**: incumbent cart-based ultrasound (GE, Philips, Siemens, Canon, top-5 holding ~55% of the overall ultrasound market, E65) and handheld competitors using different or overlapping approaches (GE Vscan Air, Philips Lumify, Clarius, Exo, EchoNous — E66-69) all compete for the same POCUS budget dollar; see bottleneck_map.md for whether BFLY's chip-based approach is a durable differentiator against these substitutes.

---

## Customer Concentration

- ~145,000 unique device users cumulative, 100+ countries — a broad, fragmented individual-clinician base [E59].
- ~11% of FY2025 revenue from a single unnamed customer [E59] — plausibly Midjourney given Q4 2025 timing, but not A1-confirmed; flagged OPEN (O1). This is a meaningful concentration for a company of BFLY's size (11% of ~$97.6M FY25 revenue is roughly $10.7M from one counterparty) and is worth monitoring given the ramping nature of Embedded-licensing deals (large individual contracts can create lumpy concentration even if the overall customer base is fragmented).
- No segment-level or geographic P&L is disclosed (single reportable operating segment, E11) — limits the precision with which value-chain-layer profitability can be independently verified beyond what's in the table above.

---

## Verdict: Where the Value Really Sits

Butterfly's defensible value-capture position is narrower than "we make ultrasound machines" — it is specifically **chip design IP + the AI/software layer trained on accumulated imaging data + a still-developing brand/clinical-trust position**, wrapped in an asset-light manufacturing structure that avoids capital intensity but creates single-source supply dependency. The Embedded-licensing line is a genuine, contractually-verified (E53) second value-capture mechanism validating that the chip IP itself has standalone worth outside medicine — but it does not change the fact that BFLY neither owns nor controls the actual scarce physical resource (advanced semiconductor fabrication capacity) that makes the whole model possible. That dependency, and whether it constitutes a moat or a vulnerability, is the subject of bottleneck_map.md.
