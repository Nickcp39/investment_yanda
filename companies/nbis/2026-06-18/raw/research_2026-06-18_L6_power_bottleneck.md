# NBIS Research Run — Layer 5/6: Power & Datacenter Buildout Bottleneck (LEAD QUESTION)

- Run date: 2026-06-18
- Method: general-purpose research subagent, web sweep (primary anchor: Nebius Q1 2026 Letter to Shareholders / SEC 6-K, May 13 2026, read page-by-page; plus secondary press)
- Status: ⚠️ **UNAUDITED RESEARCH DIGEST.** Claims here are NOT yet promoted to facts. Per pipeline rule (`source -> raw -> claim_ledger.csv -> facts.md -> analysis -> memo`), every load-bearing number must be entered into `claim_ledger.csv` and audited before use in any analysis file or memo.
- Subagent id (may expire across sessions): a8b3b5a84a9cca9b3
- Subagent tokens: 107,525 | tool_uses: 14

---

# Nebius Group (NASDAQ: NBIS) — Is Power the Binding Bottleneck on the Datacenter Buildout?

*Buy-side infrastructure research | As of 2026-06-18 | Primary anchor: Nebius Q1 2026 Letter to Shareholders (SEC 6-K), May 13, 2026*

---

## BOTTOM LINE (answering "is power the bottleneck, yes/no, and what's the real binding constraint")

1. **No — raw power *availability* is not NBIS's binding constraint, and "building power plants" is a mischaracterization of what NBIS does.** Nebius does **not** build or own utility-scale power generation. It builds/owns AI data centers that draw contracted grid/utility power, supplemented at some US sites by **behind-the-meter on-site natural-gas generation** (built by partners, e.g., DataOne in New Jersey, or via the **Bloom Energy** fuel-cell deal) specifically to *avoid* the power-delivery problem. [PRIMARY]

2. **The genuine binding constraint is "capacity" — i.e., the speed of converting contracted power into *connected, energized, GPU-filled* operational data centers.** Management says this explicitly and repeatedly: CEO Volozh — *"Capacity today is the main bottleneck to revenue growth"* (Q3 2025); CFO Alonso — *"we sold out our capacity as demand continued to exceed available supply"* (Q1 2026). Demand is *not* the constraint (it's ~3.5x oversubscribed); they sell everything they build. [PRIMARY]

3. **Within "capacity," the hardest sub-constraints are (a) physical build speed, (b) long-lead electrical equipment, and (c) grid interconnection — and grid interconnection is the one NBIS is deliberately engineering around.** Volozh: *"The physical world simply cannot build data centers fast enough… massive shortages in basic physical components, like transformers and gas generators."* The $2.6B / 328 MW Bloom Energy behind-the-meter deal (May 2026) and the gas-microgrid New Jersey site exist precisely to bypass multi-year utility interconnection queues. So power *delivery/interconnection* is a real friction — but NBIS treats it as a solved/route-around problem, not a hard ceiling. [PRIMARY for quotes; SECONDARY for Bloom deal terms]

4. **GPU allocation and capital are explicitly NOT the current constraints.** GPU scarcity was "last year's problem," now de-risked via a deepened NVIDIA partnership ($2B NVIDIA equity investment, Exemplar Cloud status on GB300, early Vera Rubin access). Capital is abundant: $9.3B cash, $6.3B raised in Q1 2026, >$46B contracted backlog (Meta ~$27B + Microsoft ~$17.4–19.4B) used as financing; capex *raised* to ~$20–25B for 2026. [PRIMARY]

5. **On power, NBIS is in the top tier of pure-play neoclouds — a modest advantage, not a disadvantage.** Contracted power **>3.5 GW (guided to >4 GW by YE2026)**, with **>75% owned** — neck-and-neck with CoreWeave on contracted power, ahead of Crusoe/Nscale/Lambda, and with better ownership economics and cleaner/cheaper Nordic power. NBIS's one relative gap vs. Crusoe is the lack of a native "bring-your-own-power" generation capability — which the Bloom Energy deal is now closing. (Only Oracle/OCI, a full hyperscaler, clearly outscales it.) [PRIMARY for NBIS; SECONDARY for peers]

> **One-line answer for the user:** NBIS does not "build power plants," and electricity *supply* is not the gating factor. The binding constraint is the end-to-end **build-and-energize cycle** (shell + long-lead electrical gear + interconnection) that turns secured power into live, revenue-generating capacity. Power *delivery* is a friction NBIS is solving with behind-the-meter generation; power *availability* it has largely already locked up.

---

## A. NBIS's Power / Datacenter Model — what they actually do

**Verdict: NBIS is a data-center developer/operator, NOT a power producer.** The "builds power plants" framing is false as stated, with one nuance (behind-the-meter on-site generation at partner-built US sites). Three layers:

**(a) Owned, greenfield data centers drawing grid/utility power — the core model (>75% of contracted power).** [PRIMARY — Q1 2026 letter, pp. 3, 6]
- *"In total, our owned facilities will deliver 3 GW of capacity across five sites… reinforcing our commitment to a capital-efficient model with attractive long-term unit economics."*
- *"Owned capacity now accounts for more than 75% of our contracted power."*
- These campuses connect to grids/utilities via secured power contracts. Example — Missouri/Independence (1.2 GW) connects to municipal utility **Independence Power & Light**, which is reopening the retired Blue Valley gas plant to serve it; on-site generation is only "under study" for a *future* phase. [PRIMARY letter; SECONDARY: Missouri DED, GovTech Jan 28 2026]

**(b) Leased / colocated capacity — for speed-to-market.** Cost of revenue explicitly includes *"expenses incurred for co-location and operating lease agreements."* [PRIMARY — Q1 2026 letter, p. 10] Colo/partner sites: Iceland (Verne), France (Paris/Equinix, Lille), UK (Ark, Kao Data), and a new Spain colo. [PRIMARY/SECONDARY]

**(c) Behind-the-meter on-site generation — the nuance, and it is built by PARTNERS, not owned-and-operated by NBIS as a generation business.**
- **New Jersey (Vineland):** facility developed by partner **DataOne** to NBIS's design; ~85% of power self-generated on-site from **natural gas** via existing pipeline (≈32 gas engines + diesel backup), ~15% from local utilities. NBIS's own framing: *"behind-the-meter electricity and advanced energy technology."* [PRIMARY — Nebius blog, Mar 5 2025; SECONDARY — WHYY Mar 25 2026, DCK Mar 7 2025] Ownership of the gas engines (NBIS vs. DataOne) is **not disclosed**.
- **Bloom Energy fuel cells (announced May 20–21, 2026):** up to **$2.6B in service fees, 328 MW installed / 250 MW guaranteed**, structured as **three 10-year phases**, first phase live 2026. NBIS purchases the power output; **Bloom installs/operates/maintains** — i.e., NBIS is the offtaker, not the generator-owner. Explicit rationale: *"a competitive advantage against rivals still waiting in utility interconnection queues."* [SECONDARY — Crypto Briefing / CNBC, May 2026]

**How NBIS itself defines "power" (verbatim, the key framing for an infra analyst) [PRIMARY — Q1 2026 letter, p. 6]:**
1. **Contracted power** — *"power secured by contracted land and power commitments"*
2. **Connected power** — *"power connected into fully built and equipped data centers"*
3. **Active power** — *"power being consumed by installed, operational IT equipment and available for revenue generation"*

The gap between *contracted* and *active* **is** the binding constraint.

---

## B. Site-by-Site Footprint (mid-2026)

Capacity figures are nameplate/full-buildout unless noted. Map in the Q1 2026 letter (p. 2) plots: Iceland, Finland, UK, France, Spain, Israel + US sites in **Minnesota, Kansas City, Missouri, Pennsylvania, New Jersey, Oklahoma, Alabama**.

| Site | Power (MW) | Status | Model | Utility / power source | Source |
|---|---|---|---|---|---|
| **Finland — Mäntsälä** (flagship) | **75 MW** (tripled from 25) | Operational | Owned | Finnish grid, low-carbon; free cooling, PUE ~1.1–1.13, district-heat reuse | [PRIMARY] Nebius newsroom Oct 2024 |
| **Finland — Lappeenranta** (NEW) | **Up to 310 MW** | Under construction | Owned | "Predominantly low-carbon"; first capacity 2027 | [PRIMARY] Nebius newsroom Mar 31 2026 |
| **Kansas City, MO** (Patmos / KC Star bldg) | 5 MW live → **40 MW** ceiling | Operational | Colo (Patmos) | Evergy (secondary) | [PRIMARY] Nebius blog Nov 2024 |
| **Independence, MO** (NEW, flagship US) | **Up to 1.2 GW** (200 MW phase 1) | Broke ground May 12 2026; ops ~2027 | Owned | Independence Power & Light (Blue Valley gas plant rebuild); interim NextEra/Evergy wind | [PRIMARY] Nebius + City of Independence FAQ |
| **New Jersey — Vineland** | **Up to 300 MW** (300–350 range; 100 MW modules) | Under construction; small-scale live H2 2025 | Partner-built (DataOne) | **Off-grid gas microgrid** (~85% on-site gas) | [PRIMARY] Nebius Mar 2025; [SECONDARY] WHYY |
| **Pennsylvania** (NEW) | **Up to 1.2 GW** (250–300 MW phase 1) | Planned/announced May 13 2026 | Owned | Not disclosed; "secured power"; phased from 2027, full by ~2030 | [PRIMARY] Q1 2026 letter |
| **Alabama — Birmingham (BHM01)** | ~300 MW (reported) | Active construction; ops 2027 | Owned | Not confirmed | [PRIMARY] letter (active construction); [SECONDARY] DCD for 300 MW |
| **Israel — Mega Or** (Beit Shemesh + Masmiyya; earlier Modi'in) | **80 MW** leased (58 + 22); Modi'in 8 MW live | Leased / under construction | Lease | Israeli grid (n/d) | [SECONDARY] DCD, CTech |
| **UK — London/Surrey/Harlow** | ~16 MW (Ark) + 22 MW (Kao) → **~65 MW by 2027** | Operational/deploying | Colo | Host-facility grid | [PRIMARY] Nebius UK newsroom; [SECONDARY] DCD |
| **France — Béthune/Lille** (NEW) | **240 MW** (former Bridgestone plant) | Planned; ~half live by YE2026 | Build w/ partner Azur | Not specified | [SECONDARY] DCD, Reuters/TheStar Feb 12 2026 |
| **France — Paris** | n/d | Operational | Colo (Equinix PA10) | 100% renewable (PPA+EAC) | [SECONDARY] |
| **Iceland — Keflavik** | **10 MW** | Operational | Colo (Verne) | 100% hydro + geothermal | [PRIMARY] Nebius + Verne |
| **Spain** (NEW) | n/d | New colo | Colo | n/d | [PRIMARY] Q1 2026 letter |
| **Minnesota; Oklahoma** | n/d | On map (p. 2) | n/d | n/d | [PRIMARY] letter map only |

- **Texas:** No NBIS Texas site found (the Texas GPU-cloud activity is competitors IREN/Crusoe/Nscale). [Inference from absence of sources]
- The canonical **nebius.com/hardware** page lags the press announcements (omits Independence/Lappeenranta/Béthune/Birmingham/Israel).

---

## C. Total Power Capacity Roadmap (management's own numbers)

**Contracted power progression** (capacity-guidance chart, Q1 2026 letter p. 2 + body p. 6) [PRIMARY]:

| As of | Contracted power | Note |
|---|---|---|
| Aug 2025 (guidance) | **>1 GW** | |
| Nov 2025 (guidance) | **>2.5 GW** | *(This is the "2.5 GW" some secondary sources still cite — it is stale.)* |
| YE2025 (actual) | **>2 GW** | Q4 2025 letter |
| Feb 2026 (guidance) | **>3 GW** by YE2026 | |
| **End Q1 2026 (actual)** | **"exceeds 3.5 GW"** | *"far surpassing the goal of 3 GW we set for the end of the year"* |
| **Current YE2026 guidance (raised May 2026)** | **>4 GW** | *"with any additional contracts contributing to capacity growth in 2027 and beyond"* |

- **Connected power target:** *"We continue to expect 800MW to 1GW of connected power by year-end [2026]."* [PRIMARY, p. 6]
- **Active power:** **YE2025 actual ≈170 MW** (vs. a 100 MW target) [PRIMARY — Q4 2025 letter]. **No Q1 2026 or 2026 active-power target is disclosed** — management cites uncertainty in build + GPU-delivery + energization timing. This is the single most decision-relevant number the company withholds. [Confirmed against primary PDF]
- **Owned fleet:** *"3 GW of capacity across five sites"*; *"owned capacity now accounts for more than 75% of our contracted power."* [PRIMARY, pp. 3, 6]
- **2027+:** Missouri & Alabama operational 2027; Pennsylvania phased from 2027 (250–300 MW) to 1.2 GW by ~2030. **No single explicit YE2027 GW target** is published — guidance formally extends only to YE2026. [PRIMARY]
- **Supporting capex:** Q1 2026 capex ~$2.5B [PRIMARY, p. 10]; full-year 2026 capex guided ~$20–25B (raised from $16–20B) [PRIMARY — earnings call].

---

## D. The Binding Constraint — Rank-Ordered (NBIS-specific, not industry-general)

**#1 — Build-and-energize "capacity" (the explicit, stated bottleneck).** [PRIMARY]
- Volozh (Q3 2025): *"Capacity today is the main bottleneck to revenue growth, and we are now working to remove this bottleneck."*
- Alonso/CFO (Q3 2025): *"our revenue growth was limited only by the capacity that we were able to bring online."* (Q1 2026): *"Once again, we sold out our capacity as demand continued to exceed available supply."*
- This is the contracted→connected→active conversion gap. It is THE constraint.

**#2 — Long-lead electrical equipment + construction speed (the hardest *components* of capacity).** [PRIMARY]
- Volozh (Mar 2026): *"The physical world simply cannot build data centers fast enough… massive shortages in basic physical components, like transformers and gas generators."*
- COO Korolenko (Q1 2026): *"component inflation in our 2026 program was… around low single digits as a percentage of total spend"* — confirms equipment cost/availability pressure, but manageable.

**#3 — Grid interconnection (a real friction NBIS routes around, not a hard ceiling).** [PRIMARY strategy + SECONDARY framing]
- NBIS's behind-the-meter strategy (NJ gas microgrid; Bloom Energy 328 MW) exists precisely to bypass utility interconnection queues (industry queues run ~4–8+ years in PJM/congested regions). The $2.6B Bloom deal is the clearest proof grid-delivery is a binding factor industry-wide — and that NBIS is solving it structurally. See Section E.

**#4 — Data center shell / cooling (incl. liquid cooling for GB200/GB300).** Not flagged by management as a gate; NBIS already runs GB300 NVL72 (Europe's first; Exemplar Cloud status) with closed-loop liquid cooling at Finland sites. Folded into "build speed" above. [PRIMARY]

**#5 — GPU allocation from NVIDIA — NOT a current constraint (de-risked).** [PRIMARY]
- Volozh (Mar 2026): *"A year ago, getting allocations of GPUs was the main challenge. Now, the constraints go deeper into the silicon"* (memory chips). NVIDIA = "differentiated supply-chain certainty," $2B equity investment, early Rubin/Vera access. CRO Boroditsky: *"we are still selling out across all chip types"* — demand > supply because of deploy-capacity, not chips.

**#6 — Capital / financing — NOT a constraint (abundant).** [PRIMARY]
- $9.3B cash; $6.3B raised in Q1 2026 ($2B NVIDIA equity + $4.3B converts); $2.3B Q1 operating cash inflow; >$46B contracted backlog used as financing; capex *raised* to ~$20–25B. Risk factors note the *ability* to "obtain sufficient financing" as a standard caveat, but funding is described as enabling "disciplined capacity expansion." [PRIMARY, pp. 4, 10–11]

**NOT a constraint at all — demand.** *"Compute and cloud needs are vastly exceeding capacity"*; pipeline up ~3.5x QoQ; *"4 or more customers competing for every GPU we bring online."* [PRIMARY]

---

## E. Grid Interconnection Specifics (key sites)

- **NBIS's deliberate model is to avoid utility interconnection queues via on-site/behind-the-meter generation**, rather than wait in them. [PRIMARY strategy; SECONDARY queue-length framing]
- **New Jersey (Vineland):** islanded gas microgrid; bypasses PJM queue; majority of remaining capacity targeted online H2 2026. The disclosed real-world risk is a **New Jersey DEP air-emissions permit** (application filed Dec 16 2025, reportedly still pending spring 2026 per analyst Substack) — *not* a grid-interconnection delay. Local opposition (Sierra Club). [SECONDARY/analyst — treat permit status as unverified]
- **Missouri (Independence):** Independence Power & Light delivers initial power **H2 2026** via Southwest Power Pool, generated at the rebuilt Blue Valley plant (Independence Power Partners); future on-site generation under study. Bloom Energy fuel cells (250 MW guaranteed) anchor here, live 2026. [PRIMARY letter; SECONDARY GovTech/Crypto Briefing]
- **Pennsylvania:** *"lights up by the end of 2027 with the first around 250 to 300 megawatts… full 1.2 gigawatts by 2030"* (COO Korolenko, Q1 2026 call). Power "secured" but utility undisclosed. [PRIMARY]
- **Finland (Lappeenranta):** described in trade press as having *"a straightforward grid connection… rather than the multi-year interconnection queue."* [SECONDARY]
- **Utility partners are mostly undisclosed** — by design, because NBIS leans on municipal utilities willing to add generation (Independence) and on-site/private generation (DataOne, Bloom, Azur) rather than congested investor-owned-utility interconnection.

---

## F. Energy Sourcing / PPAs / Sustainability

- **Group 2024 figure: 94% of electricity from low-carbon sources**; market-based emissions intensity 0.04 tCO₂e/MWh. [PRIMARY — 2024 Sustainability Report, Jul 10 2025] — but this **predates** the gas-heavy US buildout and will likely come under pressure.
- **Europe is clean; US is gas-heavy.** Finland (low-carbon grid, free cooling, PUE ~1.1–1.13, Mäntsälä district-heat reuse covering ~65–72% of the town's heating demand), Iceland (100% hydro+geothermal), Paris/UK (100% renewable via PPA+EAC). **US flagships (NJ Vineland ~85% on-site gas; Missouri gas-plant rebuild) are natural-gas-centric.** [PRIMARY for Europe; SECONDARY for US gas detail]
- **Only one quantified, source-specified renewable PPA found:** Verne/Iceland, 10 MW hydro+geothermal. Other PPAs referenced generically (no MW/counterparty). No renewable PPA disclosed for Vineland, Kansas City, or the new Finnish builds. [PRIMARY/SECONDARY]
- **No published net-zero target year and no SBTi commitment** could be found — NBIS states a directional "avoid → reduce → low-carbon-source" hierarchy only. Certifications: ISO 14001 (environmental); SOC 2/3, ISO 27001, HIPAA, NIS2, DORA (security). [PRIMARY]

---

## G. Management Commentary on Power (direct quotes)

**Arkady Volozh (CEO):** [PRIMARY]
- *"Capacity today is the main bottleneck to revenue growth, and we are now working to remove this bottleneck."* (Q3 2025 call, Nov 11 2025)
- *"Everything we build with is sold."* (Q1 2026 call, May 13 2026)
- *"The physical world simply cannot build data centers fast enough. The real issue is the broader supply chain… We see massive shortages in basic physical components, like transformers and gas generators."* (interview, Mar 27 2026)
- *"A year ago, getting allocations of GPUs was the main challenge. Now, the constraints go deeper into the silicon."* (Mar 2026)

**Dado Alonso (CFO):** *"Once again, we sold out our capacity as demand continued to exceed available supply… We just raised prices again… and we are still selling out across all chip types at the higher prices."* (Q1 2026) [PRIMARY]

**Andrey Korolenko (COO):** *"We delivered all our capacity commitments across our Microsoft and Meta customers."* / Pennsylvania *"lights up by the end of 2027 with the first around 250 to 300 megawatts."* (Q1 2026) [PRIMARY]

**Marc Boroditsky (CRO):** *"we are typically seeing 4 or more customers competing for every GPU we bring online."* (Q1 2026) [PRIMARY]

**Did they say power IS the bottleneck?** Indirectly yes — they call *capacity* the bottleneck and define it as power-delivery infrastructure (contracted→connected→active), with the supply-chain pinch being power *equipment*. **GPU supply? No** (last year's problem). **Capital? No** (abundant).

---

## H. Peer Comparison on Power Access

| Company | Contracted/secured power | Live today | Power model | Public? |
|---|---|---|---|---|
| **Oracle / OCI** | **~10 GW secured (3-yr)**; ~7 GW Stargate planned | 400 MW added in Q3 FY26 | Own/operate + Stargate JV + grid | ORCL |
| **CoreWeave** | **>3.5 GW contracted** | **>1.0 GW active** | Lease → buying ownership (Core Scientific ~1.3 GW) | CRWV |
| **NBIS** | **>3.5 GW → >4 GW guided** | 800 MW–1 GW *connected* target YE26 | **Own-build (>75%) + colo** | NBIS |
| **Crusoe** | 4.5 GW gas secured; ~2.1 GW Abilene | ~1.2 GW Abilene ramping | **Own-build + BYO behind-the-meter gen** | Private |
| **Nscale** | 1.3 GW greenfield pipeline (8 GW aspirational) | ~30 MW + early | Hybrid (Nordic owned + leased + JV) | Private |
| **Lambda** | **>320 MW committed** | ~20 leased DCs | **Lease-heavy** | Private |

**Assessment:** NBIS has a **modest power *advantage*, not a disadvantage**, among pure-play neoclouds.
- **Tied with CoreWeave on contracted power (>3.5 GW)**; ahead of Crusoe/Nscale/Lambda. Only Oracle (a full hyperscaler, mixed-use) clearly outscales it.
- **Better ownership economics:** >75% owned vs. Lambda's lease-heavy model and CoreWeave's $9B scramble to *buy* ownership (Core Scientific).
- **Cleaner/cheaper power + cold-climate cooling** in the Nordics — the same thesis Nscale validates.
- **Caveat:** CoreWeave is ahead on *deployed/active* power (>1 GW vs. NBIS's YE2026 *connected* target of 800 MW–1 GW). And NBIS lacked Crusoe-style native generation — but the Bloom Energy deal now closes that gap. The "sub-scale" worry is outdated at >3.5 GW contracted. [SECONDARY for peers; PRIMARY for NBIS]

---

## I. Microsoft Deal — Capacity / Power Implications

- **Terms (SEC 6-K, Sept 8 2025):** 5-year commercial GPU-capacity agreement; **base ~$17.4B through 2031, expandable to ~$19.4B** via built-in option; **~$6.96B upfront**, remainder invoiced monthly. Served from **Vineland, NJ**, in tranches across 2025–2026. The $33B figure in some headlines is **Microsoft's total spend across multiple neoclouds (Nebius, CoreWeave, Nscale, Lambda)** — not the NBIS deal. [PRIMARY 6-K; SECONDARY for the $33B clarification]
- **What/how much:** **100,000+ NVIDIA GB300 GPUs** (chip count from secondary/Bloomberg reporting; the 6-K says only "dedicated GPU infrastructure capacity"). **MW carve-out specifically for Microsoft is NOT disclosed** — site total is ~300 MW. [SECONDARY]
- **Power implication:** Fulfilled via the **off-grid gas microgrid**, deliberately sidestepping the PJM interconnection queue → power *delivery* timing is decoupled from utility energization. The 6-K includes **liquidated damages for late delivery** and per-tranche termination if NBIS misses dates and can't provide alternative capacity — the explicit contractual link between delivery delay and the contract. [PRIMARY]
- **Status (Q1 2026, May 13 2026):** NBIS says it **delivered all Microsoft/Meta commitments and is on schedule**; first tranche delivered Nov 2025; *"most of the volumes will be coming in Q3 and Q4 [2026]."* The live external risk is the **NJ air-emissions permit** for on-site gas, not interconnection. [PRIMARY status; SECONDARY/analyst permit]
- **Other anchors:** **Meta ~$27B** (5-yr, Mar 16 2026: $12B dedicated Vera Rubin capacity from early 2027 + $15B optional) — supersedes an earlier ~$3B Nov 2025 deal; **NVIDIA $2B** strategic investment + >5 GW deployment partnership by 2030. Total backlog >$46B. [PRIMARY]

---

## COULD NOT VERIFY (flag list)

1. **Current ACTIVE power (live revenue-generating MW) as of Q1 2026** — NBIS discloses contracted (>3.5 GW) and connected target (800 MW–1 GW YE26) but **gives no Q1 2026 active-power number** (last hard figure ≈170 MW at YE2025). Confirmed against the primary PDF — this is a genuine company omission.
2. **Explicit YE2027 contracted/connected/active targets in GW** — guidance formally runs only to YE2026 (>4 GW contracted). 2027 is qualitative.
3. **MW (and exact GPU count) dedicated specifically to Microsoft at Vineland** — not broken out in any primary source.
4. **"100,000 GB300" in a NBIS primary filing** — confirmed only in secondary (Bloomberg-sourced) press; the 6-K says "dedicated GPU infrastructure capacity."
5. **NJ DEP air-permit status for Vineland** — pending-permit claim is from an analyst Substack self-identifying as non-expert opinion; no primary regulatory record found.
6. **Specific utility names** for Mäntsälä, Lappeenranta, Béthune, Pennsylvania, Birmingham, Israel (Evergy/NextEra for KC/Missouri appear only in secondary; the primary names IPL/IPP/Blue Valley/SPP).
7. **Ownership of the NJ gas generators and the Bloom fuel cells** (NBIS vs. partner) — structures point to NBIS as offtaker, not owner-operator, but exact asset ownership undisclosed.
8. **Birmingham 300 MW** — reported by trade/local press, not NBIS-confirmed.
9. **Minnesota and Oklahoma US sites** — appear on the Q1 2026 letter map (p. 2) but with **no disclosed MW, status, or details**.
10. **Peer caveats:** CoreWeave "8 GW by 2030" (consistent figure is "+5 GW additional"); Core Scientific deal final close status; Nscale 8 GW Monarch (WV) campus — all directional/unverified. Several SEC/DCD/CNBC/OpenAI primary URLs returned HTTP 403 to automated fetch; figures corroborated via syndicated outlets and transcript aggregators.

---

### Key Primary Sources
- **Q1 2026 Letter to Shareholders (SEC 6-K), May 13 2026** — `https://assets.nebius.com/assets/aa1bc2e6-df83-40cd-a6a2-95e7cda3d16c/Nebius%20SHL_Q1%202026.pdf` *(read in full, page-by-page)*
- Q4 2025 shareholder letter (6-K), Feb 12 2026 — `https://www.sec.gov/Archives/edgar/data/0001513845/000110465926013946/tm266173d1_ex99-2.htm`
- Microsoft deal 6-K, Sept 8 2025 — `https://www.sec.gov/Archives/edgar/data/0001513845/000110465925088312/tm2525580d1_6k.htm`
- Finland 310 MW, Mar 31 2026 — `https://nebius.com/newsroom/nebius-to-construct-310-mw-ai-factory-in-finland`
- Missouri groundbreaking, May 12 2026 — `https://nebius.com/newsroom/nebius-breaks-ground-on-gigawatt-scale-ai-factory-in-independence-missouri`
- NJ + Iceland, Mar 5 2025 — `https://nebius.com/blog/posts/300-mw-new-jersey-and-iceland-regions`
- Meta $27B + NVIDIA $2B — `https://nebius.com/newsroom/nebius-signs-new-ai-infrastructure-agreement-with-meta` ; `https://nvidianews.nvidia.com/news/nvidia-and-nebius-partner-to-scale-full-stack-ai-cloud`
- Sustainability — `https://nebius.com/sustainability` ; `https://nebius.com/sustainability/turning-heat-into-a-resource`

### Key Secondary Sources
- Q1 2026 call transcripts — Motley Fool (`fool.com/.../nebius-nbis-q1-2026-earnings-transcript/`), Investing.com, Globe & Mail
- Q3 2025 call — Investing.com transcript; Benzinga (Nov 12 2025)
- Volozh "four Cs" interview — Money Times (Mar 27 2026), Oninvest (Mar 30 2026)
- Bloom Energy deal — Crypto Briefing / CNBC (May 2026)
- Vineland gas/permits — WHYY (Mar 25 2026), Sierra Club (Feb 2026)
- Missouri power — GovTech (Jan 28 2026); Pennsylvania/Béthune/Birmingham — DCD; peers — DCD, Datacenter Knowledge, Data Center Frontier

---

**Net for thesis:** The premise ("NBIS is building power plants and that's the constraint") is backwards on both counts. NBIS builds *data centers*, not power plants, and contracts (or self-generates behind-the-meter) the electricity. Power *availability* is largely locked up (>3.5 GW contracted, top-tier among peers). The true gating factor is the **physical build-and-energize cycle** — shell construction, long-lead transformers/switchgear/generators, and interconnection timing — which is exactly why "connected" and "active" power lag "contracted" power, and exactly why management calls *capacity* (not power, not GPUs, not capital) the bottleneck.
