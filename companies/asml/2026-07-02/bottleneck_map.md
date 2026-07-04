# ASML Bottleneck Map (M3)

As-of: 2026-07-02

## The bottleneck question: who holds the scarce resource?

In the AI compute stack — GPUs/TPUs -> leading-edge wafers -> lithography -> EUV scanners — the single scarcest, least-substitutable resource is **the EUV scanner itself.** ASML is the sole holder. Every leading-edge transistor NVIDIA, Google, Amazon, Apple or AMD designs must be printed on a machine that only ASML can make. This is the deepest node in the entire chain — upstream of the chips, upstream of the fabs.

## Bottleneck stack (top of the AI compute tower down)

| Layer | Scarce? | Who holds it | ASML position |
|---|---|---|---|
| AI models / hyperscalers | No (many) | OpenAI, Google, Meta, ... | Demand pull |
| AI accelerators (GPU/TPU/ASIC) | Concentrated | NVDA, Google, AMD, Broadcom | Customer's customer |
| Leading-edge foundry | **Very scarce** | TSMC (~Samsung, Intel) | Direct customer |
| **EUV lithography** | **THE choke point (100%)** | **ASML — sole source** | **The monopoly node** |
| EUV optics / light source | Near-monopoly | Zeiss (optics), Cymer (ASML-owned) | Owns/partners the sub-bottleneck |
| Precision components | Somewhat | Trumpf + specialist web | Integrator/gatekeeper |

## Why this matters for the thesis

- The bottleneck explains the ~50-53% gross margin and the pricing power: economics concentrate at the scarcest, most-irreplaceable node, and ASML sits exactly there.
- It also explains the factor read: ASML is **upstream of NVDA, Google TPU and AWS Trainium** — it is the same AI-capex wave, one layer deeper and monopolistic. Owning ASML is a differentiated way to own "the AI buildout," but it is STILL the AI buildout (adds to the book's AI factor).
- Unlike HWM, whose bottleneck is volume-cyclical but competitively shared, ASML's bottleneck is **competitively exclusive** (no peer) yet **still volume-cyclical** (customer capex swings). So the bottleneck protects the *position and margin* through a cycle but NOT the *revenue level* — the exact shape of the M5/M6 risk.

## Bottleneck risk

- **Volume, not position:** an AI-capex digestion or a broad semi down-cycle cuts throughput hard (2023 FCF fell ~55%) even though ASML remains the only EUV source. The monopoly does not protect the multiple.
- **Policy scissors on the DUV sub-layer:** the mature-node/China part of the book (~20% of 2026 rev) can be legislated away (MATCH Act) without touching the EUV monopoly — a bottleneck-adjacent, policy-driven revenue risk.
- **Indigenous-EUV tail:** if China (SMEE) ever closes the ~10-15yr gap, the exclusivity erodes — long-dated, low near-term probability, high severity; the one thing to watch for the *moat itself*.

## One metric that forces a market update

**EUV order intake / backlog trajectory + China revenue trend.** ASML stopped publishing quarterly bookings in 2026 (a transparency downgrade), so the tells are now: (a) the semi-annual/annual backlog vs the EUR38.8B YE2025 anchor, (b) whether AI-driven EUV demand keeps replacing lost China DUV (Q1'26 said yes: China 19%, GM still 53%), and (c) any escalation of export controls from DUV toward EUV components (the June 2026 BIS risk).
