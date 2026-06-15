# Topic Selection Engine

Purpose: build a repeatable way to choose research directions before choosing
stocks. This is inspired by the local 美股投资网 archive, Serenity-style
chokepoint research, and buy-side research practice.

Important boundary:

This is only the first module of the investment research pipeline. It answers
"what deserves research?" It does not answer "is this a good business?", "is the
price cheap?", or "should we buy?" Those answers require the evidence,
accounting, moat, operator, inversion, valuation, and IC memo stages in
`frameworks/investment_research_pipeline_detailed.md`.

Core idea:

Good research direction usually appears before good stock selection. The
process is not "find a ticker." It is:

1. Find where the world is changing.
2. Find where capital is flowing.
3. Find what becomes scarce because of that change.
4. Find which listed companies control the scarce link.
5. Verify with primary data before valuation.

## The Six Radars

### 1. Capex Radar

Question: where are the largest companies spending real money?

Signals:

- hyperscaler capex guidance
- data-center buildout
- cloud RPO/backlog
- GPU/ASIC orders
- long-term power contracts
- factory or fab expansion
- customer prepayment and committed capacity

Why it matters:

Management can tell stories, but capex reveals what they believe strongly enough
to fund.

Examples from the archive:

- AI data centers
- GPU and ASIC supply
- optical interconnects
- power and nuclear
- Google TPU / Broadcom / ASIC supply chain
- neoclouds

### 2. Bottleneck Radar

Question: what must exist for the theme to work, but is hard to scale quickly?

Signals:

- physical constraints: power, cooling, land, grid, fiber, materials
- technical constraints: photonics, ASIC, memory bandwidth, packaging
- regulatory constraints: nuclear approvals, defense procurement, drug trials
- manufacturing constraints: qualified suppliers, long lead-time equipment

Why it matters:

Obvious winners are often already expensive. Bottlenecks can be earlier,
smaller, and less understood.

Examples:

- AI cloud needs power, cooling, optical links, memory, storage, ASICs.
- Humanoid robots need actuators, reducers, motors, sensors, batteries.
- AI PC needs CPU/NPU cycle, memory, OS integration, local inference use cases.

### 3. Catalyst Radar

Question: what event will force the market to update?

Signals:

- earnings
- product launches
- GTC / WWDC / Google I/O / developer conferences
- IPO calendars
- analyst days
- regulatory decisions
- major contracts
- index inclusion
- election / tariff / policy changes

Why it matters:

A good thesis can stay invisible for years. Catalysts make other people look.

Examples from the archive:

- NVDA earnings previews
- big-tech earnings previews
- GTC preview
- Figma / CRWV / SpaceX-related IPO themes
- tariff and Fed regime videos

### 4. Dislocation Radar

Question: did price move faster than fundamentals?

Signals:

- sharp selloff after earnings
- "AI will kill this industry" panic
- downgrade clusters
- short reports
- retail crowding
- forced selling or liquidity stress
- valuation compression without business deterioration

Why it matters:

Dislocation creates either danger or opportunity. The research job is to
separate emotional repricing from real impairment.

Examples:

- SaaS after AI-agent fears
- UNH after fund pressure and headline risk
- Apple / Tesla / Oracle / Nvidia pullbacks
- "if AI trade collapses, what defensive stocks survive?"

### 5. Institutional Translation Radar

Question: what are professional analysts and funds debating, and what is the
one variable underneath the debate?

Signals:

- Goldman / Morgan Stanley / Bernstein / JPMorgan reports
- hedge-fund positions or short reports
- 13F changes
- management commentary
- expert-call style language
- consensus revisions

Why it matters:

Retail usually sees the conclusion late. The useful part is to find the hidden
assumption behind the institutional debate.

Examples:

- "AI destroys SaaS" versus "AI expands software TAM"
- Google AI capex: value-creating investment or FCF drain?
- Amazon AWS: cloud resource seller or AI infrastructure platform?

### 6. Narrative Gap Radar

Question: what is the market talking about in a lazy way?

Signals:

- everyone says "AI beneficiary" but cannot name the specific monetization path
- everyone says "bubble" but cannot identify which metric is broken
- everyone says "cheap" but cannot explain the catalyst
- everyone talks about a leader while ignoring suppliers
- a company is valued using the old category while its business mix changed

Why it matters:

The opportunity is often in the gap between simple narrative and actual
mechanism.

Examples:

- "AI is good for Nvidia" becomes "who supplies optical links, power, memory,
  custom silicon, and data-center infrastructure?"
- "AI kills search" becomes "does AI search reduce clicks, increase query depth,
  improve conversion, or shift ad formats?"
- "SaaS is dead" becomes "which SaaS has workflow depth, data gravity, and
  distribution strong enough to survive AI?"

## Direction Scorecard

Score each new topic from 0 to 3.

| Dimension | 0 | 1 | 2 | 3 |
|---|---:|---:|---:|---:|
| Real-world change | vague story | small change | clear shift | structural shift |
| Capital flow | no money | talk only | budgets visible | signed capex/contracts |
| Bottleneck | none | possible | clear | severe and hard to scale |
| Listed exposure | unclear | many weak links | several names | one/few direct names |
| Catalyst | none | distant | known event | near-term forced update |
| Data verifiability | low | mostly media | some filings | primary data available |
| Valuation gap | no gap | unclear | possible | clear mispricing candidate |
| Risk clarity | unknown | vague risks | known risks | kill conditions explicit |

Interpretation:

- 0-8: ignore or park.
- 9-14: watchlist only.
- 15-19: start a research note.
- 20-24: full research plan.

## How 美股投资网 Seems To Do It

Based on the local archive and recent titles, their direction engine looks like:

1. Start with what the market already cares about: AI, Nvidia, big-tech earnings,
   IPOs, Fed, tariffs, SaaS, SpaceX, defense, healthcare.
2. Pick a timely hook: earnings this week, IPO soon, sharp selloff, new product,
   "Goldman list," "20x oversubscription," "AI crash hedge."
3. Translate the hook into a mechanism:
   - cloud AI means capex and power
   - capex means chips, optics, cooling, grid, data centers
   - AI agents mean SaaS pricing pressure
   - AI PC means local compute and component refresh
4. Map that mechanism to tickers.
5. Give a simple actionable frame: buy, avoid, target, entry, or watch metric.

This is why the titles look "right" even when individual claims still need
verification. The direction is chosen from large capital flows and live market
debates, not from random ticker hunting.

## How We Should Use It

Before opening a full company research project, fill this template:

```text
Theme:
Why now:
Capital flow evidence:
Bottleneck:
Listed companies:
Primary sources needed:
Catalyst:
Key metric:
Kill condition:
Initial direction score:
```

No topic becomes a buy decision at this stage. It only becomes a research queue
candidate.

## Example: Google

Theme:
AI is changing search, cloud, and capex economics.

Why now:
Alphabet's AI capex and Berkshire buying changed the market's attention.

Capital flow evidence:
Capex guidance, Google Cloud growth, RPO/backlog, TPU deployment, AI product
integration.

Bottleneck:
Inference cost, distribution, data, ad monetization, TPU supply chain, power.

Listed companies:
GOOGL/GOOG first, then AVGO and selected AI infrastructure suppliers only after
source verification.

Key metric:
Can AI product integration grow query depth, commercial conversion, cloud
backlog, and operating profit faster than capex depresses free cash flow?

Kill condition:
AI search reduces high-intent ad economics, capex rises without visible return,
or regulation damages default distribution and data advantages.
