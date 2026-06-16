# GOOGL Industry / Value Chain v2

Last updated: 2026-06-16

Status: `P0_PASS_1 input - Layer 5 Industry / Value Chain`

Purpose: map where value is created and captured across Search ads, YouTube ads, Google Network, Cloud/GCP, TPU/AI infrastructure, data centers/power, AI agents/search alternatives, and semiconductor suppliers.

Evidence discipline:
- `A1` = official filing / earnings release.
- `A2` = official company call transcript / IR presentation / product documentation.
- `Structural inference` = buy-side judgment from disclosed business structure; not used as a precise numeric claim.

---

## 1. One-Page Answer

Google is one of the most important companies to study in the AI value chain because it sits on both sides of the transition:

- The old profit pool is `Search intent -> ad auction -> advertiser ROI`.
- The new profit pool is `user task -> AI answer/agent -> transaction/workflow -> compute -> chips/power/cloud/model monetization`.

Google still captures the largest profit pool in its own business through Search and Google Services. In Q1 2026, Google Services produced $40.6B of operating income on $89.6B of revenue, a 45.3% operating margin. Search & other alone was $60.4B of quarterly revenue, +19%, with paid clicks +13% and CPC +5%.

But the AI shift moves scarcity upstream:

- NVIDIA captures accelerator economics.
- Broadcom captures custom AI accelerator/networking economics.
- TSMC captures advanced node / foundry / packaging economics.
- Data-center land, grid interconnection, power, cooling, and equipment vendors capture more of the capex flow.
- Cloud platforms capture enterprise AI demand if utilization and pricing hold.
- AI agents/search alternatives can capture the user task before it reaches Google Search.

Google's advantage is vertical breadth: Search, YouTube, Android, Chrome, Gmail, Maps, Workspace, Gemini, GCP, TPUs, data centers, and ad auctions. Its risk is that breadth has become capital intensive. If AI requires much more compute per monetized query while agents reduce ad inventory or attribution, Google could grow revenue while owner earnings lag.

Module verdict:

> Google is a first-tier research target, but not the purest AI bottleneck. The core underwriting question is whether Google can migrate commercial intent from classic Search into AI answers and agents while earning high returns on the infrastructure buildout.

---

## 2. Value Chain Map

```text
User intent / task
  -> interface and distribution
     -> monetization layer
        -> model / software layer
           -> cloud / data center layer
              -> accelerators / networking / foundry / power
```

| Layer | Main players | Profit-pool type | Google role | Bottleneck / attack surface |
|---|---|---|---|---|
| User intent / tasks | Google Search, YouTube, Amazon, Meta, OpenAI, Anthropic, Perplexity, Apple | Attention, commercial intent, workflow initiation | Incumbent owner of broad commercial intent | Agents can start and complete tasks outside Google |
| Interface / distribution | Search, Chrome, Android, Gemini, AI Mode, YouTube, Gmail, Workspace | Default behavior and habit | Very strong consumer distribution | DOJ/EU default remedies; AI-native interfaces |
| Ads / commerce monetization | Google Ads, Meta Ads, Amazon Ads, merchants | Auction take-rate, attribution, conversion data | Strongest in Search; meaningful in YouTube; weak in Network | AI answer formats may reduce click inventory and attribution |
| Cloud / enterprise monetization | AWS, Azure, GCP, OCI | Usage, multiyear contracts, data gravity, AI infra | GCP now material and profitable | Capacity constraints, margin by backlog type, GPU/TPU supply |
| Model / agent layer | Gemini, GPT, Claude, Llama, open-source models | Subscription, API usage, workflow automation | Owns Gemini/DeepMind; embeds into Search/GCP/Workspace | Model commoditization; inference cost; agent security |
| Accelerators / networking | NVIDIA, Broadcom, AMD, Google TPU, networking/optics vendors | Hardware gross margin and scarcity rent | TPU is partial hedge; Google also buys GPUs/networking | NVIDIA/AVGO/TSMC pricing power; supply constraints |
| Foundry / packaging | TSMC, Samsung, Intel Foundry, OSAT/packaging | Advanced wafer and packaging capacity | Indirect dependency for TPU/GPU supply | TSMC advanced-node capacity and CoWoS/packaging |
| Data centers / power | Hyperscalers, utilities, power equipment, land, EPC, cooling | Physical capacity, grid access, energy | Owns global data-center footprint; spending heavily | Power availability, energy price, depreciation, permitting |

---

## 3. Search Ads

Primary source anchors:
- Alphabet Q1 2026 10-Q: https://www.sec.gov/Archives/edgar/data/1652044/000165204426000048/goog-20260331.htm
- Alphabet Q1 2026 earnings release: https://www.sec.gov/Archives/edgar/data/1652044/000165204426000043/googexhibit991q12026.htm
- Alphabet Q1 2026 call transcript: https://abc.xyz/investor/events/event-details/2026/2026-Q1-Earnings-Call-2026-nW8kCrBAKS/default.aspx

Chain:

```text
Web / merchants / local businesses
  -> users search with intent
     -> Google Search / AI Overviews / AI Mode
        -> ad auction and merchant surfaces
           -> advertisers pay for measurable demand
```

Facts:
- Q1 2026 Google Search & other revenue: $60.4B, +19%.
- Paid clicks +13%; CPC +5%.
- Management says AI Overviews and AI Mode are driving greater Search usage and growth in overall queries, including commercial queries.
- Management says Gemini improves intent understanding and helps monetize longer, more complex searches that were previously hard to monetize.

Where profit is captured:
- The money is captured at Google's owned interface and auction layer.
- Advertisers are fragmented; pricing is auction-based and tied to ROI.
- Web publishers supply content but generally have little direct bargaining power against Google Search indexing.
- Distribution partners have bargaining power through TAC, especially default placement.

Pricing power:
- Strongest in Google's portfolio.
- Evidence: both paid clicks and CPC grew in Q1 2026 while Search revenue grew 19%.
- The auction structure lets advertiser ROI and competition set price; Google controls quality score, formats, matching, and measurement.

Bottlenecks:
- Default user habit.
- Query scale and intent data.
- Ad auction liquidity.
- Measurement and advertiser tools.
- Ability to place ads in AI answer/agent workflows without harming user experience.

Attack surface:
- AI answer engines reduce classic search result page impressions.
- Agents complete tasks without users clicking through Google.
- Regulatory remedies can impair defaults or adtech integration.
- AI compute cost per query can rise faster than ad yield.

Key open item:
- AI Overviews / AI Mode RPM relative to traditional Search RPM is not disclosed. This is the most important missing unit-economic variable.

---

## 4. YouTube Ads And Subscriptions

Primary source anchors:
- Alphabet Q1 2026 10-Q: https://www.sec.gov/Archives/edgar/data/1652044/000165204426000048/goog-20260331.htm
- Alphabet Q1 2026 call transcript: https://abc.xyz/investor/events/event-details/2026/2026-Q1-Earnings-Call-2026-nW8kCrBAKS/default.aspx
- Alphabet FY2025 Q4 release: https://www.sec.gov/Archives/edgar/data/1652044/000165204426000012/googexhibit991q42025.htm

Chain:

```text
Creators / rights owners
  -> YouTube inventory and recommendation system
     -> viewer attention across mobile, web, CTV, Shorts, live
        -> brand/direct-response ads + subscriptions
```

Facts:
- Q1 2026 YouTube ads revenue: $9.9B, +11%.
- YouTube ad growth was driven by direct response followed by brand.
- Subscriptions, Platforms & Devices revenue grew to $12.4B, +19%, helped by YouTube Music/Premium and Google One, including AI plans.
- FY2025 YouTube revenue across ads and subscriptions exceeded $60B.

Where profit is captured:
- Google captures platform take-rate on ads and subscriptions.
- Creators and rights holders capture a meaningful share of economics, so YouTube's gross economics are structurally less clean than Search.
- Advertisers pay for attention and conversion, not pure high-intent search.

Pricing power:
- Good, but below Search.
- YouTube has audience scale, recommendation data, creator supply, and CTV reach.
- However, creators can multi-home, and viewer attention is more substitutable than search intent.

Bottlenecks:
- Creator ecosystem.
- Recommendation relevance.
- CTV and Shorts monetization.
- Brand safety and measurement.
- Subscription bundling with Music/Premium/TV.

Attack surface:
- Short-form and social video alternatives.
- Streaming/CTV competition.
- Content acquisition costs and revenue share.
- AI-generated video can expand supply and pressure ad rates if inventory grows faster than demand.

Key open item:
- YouTube ads and subscriptions are not fully separated in segment profit disclosure; creator/content acquisition economics are not disclosed with enough precision for a stand-alone profit-pool model.

---

## 5. Google Network

Primary source anchor:
- Alphabet Q1 2026 10-Q: https://www.sec.gov/Archives/edgar/data/1652044/000165204426000048/goog-20260331.htm

Chain:

```text
Third-party websites/apps
  -> Google ad serving / AdSense / AdMob
     -> advertisers
        -> publisher revenue share + Google take-rate
```

Facts:
- Q1 2026 Google Network revenue: $7.0B, down 4%.
- Network impressions declined 9%; cost-per-impression rose 6%.
- Decline was primarily from AdSense, partly offset by AdMob.

Where profit is captured:
- Google earns intermediation economics, but publishers/app developers take revenue share.
- This is a weaker profit pool than owned-and-operated Search/YouTube.

Pricing power:
- Moderate to weak versus Search.
- Google does not own the user surface.
- Open-web inventory faces privacy changes, adblocking, policy changes, and competition from walled-garden ad platforms.

Bottlenecks:
- Ad stack integration.
- Advertiser demand.
- Publisher/app distribution.

Attack surface:
- Open-web decline.
- Privacy regulation and browser changes.
- DOJ/EU scrutiny of adtech.
- Shift of ad budgets to owned surfaces: Google Search/YouTube, Amazon, Meta, TikTok, retail media.

Research implication:
- Network is not the Google thesis. It is a negative indicator if decline accelerates, but mix shift away from Network can also improve aggregate Google ad quality because owned surfaces have better control and margins.

---

## 6. Cloud / GCP

Primary source anchors:
- Alphabet Q1 2026 10-Q: https://www.sec.gov/Archives/edgar/data/1652044/000165204426000048/goog-20260331.htm
- Alphabet Q1 2026 call transcript: https://abc.xyz/investor/events/event-details/2026/2026-Q1-Earnings-Call-2026-nW8kCrBAKS/default.aspx

Chain:

```text
Enterprises / AI labs / developers
  -> GCP, Workspace, Vertex/Gemini, cybersecurity, data analytics
     -> Google data centers + TPUs/GPUs
        -> usage revenue / subscriptions / multiyear backlog
```

Facts:
- Q1 2026 Google Cloud revenue: $20.0B, +63%.
- Q1 2026 Cloud operating income: $6.6B; operating margin 32.9%, up from 17.8% in Q1 2025.
- Backlog reached $462B and nearly doubled sequentially.
- Management said just over 50% of Cloud backlog is expected to be recognized within 24 months.
- Management said the majority of backlog is related to typical GCP contracts, but it also includes TPU hardware sales.
- Management said Cloud revenue would have been higher if Google could meet demand.

Where profit is captured:
- GCP captures compute, storage, data, AI infrastructure, platform, cybersecurity, and Workspace revenue.
- Cloud customers can be sticky because workloads, data, and multiyear commitments create switching costs.
- However, upstream chip/power/data-center vendors capture a large share of incremental capex before Google earns revenue.

Pricing power:
- Improving, based on margin expansion and backlog growth.
- Still not proven across a full depreciation/capacity cycle.
- Google competes against Azure, AWS, OCI, specialized AI clouds, on-prem deployments, and customer-owned chips.

Bottlenecks:
- Available AI compute.
- TPUs / GPUs.
- Data-center capacity and interconnection.
- Enterprise trust, security, compliance, and migration.
- Ability to monetize Gemini/Vertex/Workspace AI at high incremental margin.

Attack surface:
- Azure enterprise distribution.
- AWS scale and developer default.
- Oracle AI cloud contracts and customer-funded capacity.
- GPU/TPU supply and power constraints.
- Depreciation and energy costs pressuring margin after capex ramps.

Research implication:
- Cloud is the credible second engine, not a side quest. The question is backlog quality: if $462B converts at high margin, AI capex may be growth capex; if it converts at low margin or requires repeated capacity raises, it is closer to a capital-intensive utility.

---

## 7. TPU / AI Infrastructure

Primary source anchors:
- Alphabet Q1 2026 call transcript: https://abc.xyz/investor/events/event-details/2026/2026-Q1-Earnings-Call-2026-nW8kCrBAKS/default.aspx
- Alphabet Q1 2026 10-Q: https://www.sec.gov/Archives/edgar/data/1652044/000165204426000048/goog-20260331.htm
- Alphabet June 2026 424B5 supplement: https://www.sec.gov/Archives/edgar/data/1652044/000119312526257690/d159942d424b5.htm

Chain:

```text
Model training / inference demand
  -> TPU and GPU clusters
     -> servers, networking, storage, cooling
        -> GCP rental, internal Search/YouTube/Gemini usage, selective TPU hardware sales
```

Facts:
- Q1 2026 capex: $35.7B, mostly technical infrastructure.
- Management said approximately 60% of technical infrastructure investment was servers and 40% was data centers/networking equipment.
- 2026 capex guide: $180-190B.
- 2027 capex expected to significantly increase versus 2026.
- Management says Google owns frontier models and silicon and has a vertically optimized AI stack.
- Management says TPU hardware sales to select customers will begin producing a small percent of revenue later in 2026, with most in 2027.

Where profit is captured:
- Google uses TPUs internally to lower cost and improve performance for Search, Gemini, YouTube, and Cloud.
- Google rents AI infrastructure through GCP.
- Google may sell TPU hardware selectively, but that is not yet the core model.
- Upstream suppliers still capture value through chips, memory, networking, advanced foundry, packaging, power, and construction.

Pricing power:
- Potentially high if TPU offers durable cost/performance advantage and GCP customers adopt it.
- Not yet fully proven because Google does not disclose TPU cost, performance, mix, utilization, or margin.

Bottlenecks:
- Full-stack co-design: model, compiler, TPU, networking, serving, data center.
- Scale of internal workloads.
- Ability to allocate scarce compute across DeepMind, Search, YouTube, Cloud, Workspace, Gemini app, and external customers.

Attack surface:
- NVIDIA GPU ecosystem remains the dominant external standard.
- Broadcom/custom ASIC ecosystems can supply other hyperscalers.
- TSMC and advanced packaging capacity remain upstream constraints.
- If TPU cannot attract external developers or if GPU software remains stickier, TPU advantage may remain mostly internal.

Research implication:
- TPU is Google's most important structural hedge against the NVIDIA tax, but its economics are not disclosed enough to underwrite as a stand-alone profit pool.

---

## 8. Data Centers And Power

Primary source anchors:
- Alphabet Q1 2026 10-Q: https://www.sec.gov/Archives/edgar/data/1652044/000165204426000048/goog-20260331.htm
- Alphabet Q1 2026 call transcript: https://abc.xyz/investor/events/event-details/2026/2026-Q1-Earnings-Call-2026-nW8kCrBAKS/default.aspx

Chain:

```text
Land / permits / grid interconnection / power
  -> data centers / networking / cooling / servers
     -> available compute capacity
        -> Search AI, Gemini, YouTube, GCP, Workspace, external AI customers
```

Facts:
- Q1 2026 capex was $35.7B.
- Full-year 2026 capex guide is $180-190B.
- Management expects 2027 capex to significantly increase.
- Management explicitly called out future pressure from depreciation and data-center operations costs such as energy.
- Q1 2026 assets not yet in service increased sharply in local P0 extracts, reflecting capacity still under build.

Where profit is captured:
- Data-center owners capture value if utilization is high and pricing holds.
- Utilities, power equipment vendors, land owners, construction/EPC firms, cooling suppliers, networking suppliers, and equipment vendors capture a large capex flow.
- Google captures value only after capacity is deployed and monetized through ads, subscriptions, cloud, or internal cost savings.

Pricing power:
- Google has scale buying power, but power/grid scarcity can shift bargaining power to local utilities, energy suppliers, and equipment suppliers.
- The physical layer is becoming a gating item, not just a cost line.

Bottlenecks:
- Grid interconnection and reliable power.
- Transformers and power equipment.
- Permits, land, water/cooling.
- Network capacity.
- Server delivery and deployment timing.

Attack surface:
- Capex lead times and underutilization.
- Energy price inflation.
- Regulatory/local opposition to data-center expansion.
- Depreciation pressure before revenue ramps.
- Competitors pre-committing scarce power/data-center capacity.

Research implication:
- The data-center/power layer is where AI turns software economics into industrial economics. It is the layer that can convert Google from a high-margin ad platform into a more capital-intensive compounder unless utilization and pricing stay high.

---

## 9. Semiconductor Suppliers

### NVIDIA

Primary source:
- NVIDIA Q1 FY2027 release: https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-first-quarter-fiscal-2027

Facts:
- Q1 FY2027 revenue $81.6B, +85%.
- Data Center revenue $75.2B, +92%.
- GAAP gross margin 74.9%.
- Data Center compute revenue $60.4B; Data Center networking revenue $14.8B.

Value-chain position:
- NVIDIA captures the most visible current AI rent because its accelerators, networking, and software ecosystem are scarce.
- Google is both a buyer and a partial substitute through TPU.
- If Google must keep buying large amounts of GPUs, AI economics leak upstream.

### Broadcom

Primary source:
- Broadcom Q2 FY2026 release: https://investors.broadcom.com/news-releases/news-release-details/broadcom-inc-announces-second-quarter-fiscal-year-2026-financial

Facts:
- Q2 FY2026 revenue $22.2B, +48%.
- AI semiconductor revenue $10.8B, +143%.
- Q3 AI semiconductor revenue expected to grow over 200% to $16.0B.
- Adjusted EBITDA $15.2B, 69% of revenue.

Value-chain position:
- Broadcom captures custom AI accelerator and networking economics.
- Hyperscaler custom silicon, including TPU-like strategies, can shift some value from general GPU vendors toward custom ASIC and networking suppliers.
- Broadcom is therefore both an upstream beneficiary of Google's strategy and a sign that custom silicon is a real profit pool.

### TSMC

Primary sources:
- TSMC FY2025 annual report: https://investor.tsmc.com/static/annualReports/2025/english/index.html
- TSMC Q1 2026 results: https://investor.tsmc.com/english/quarterly-results/2026/q1
- TSMC Q1 2026 presentation: https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-04/a7e3abe65a3fbc342aa55f9f53a5490dd621c1ac/1Q26%20Presentation%20%28E%29.pdf
- TSMC Q1 2026 transcript: https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-04/3cef85204275f94fd111485cfdf4adb3c0263c45/TSMC%201Q26%20Transcript.pdf

Facts:
- Q1 2026 revenue $35.9B, +40.6% YoY in USD.
- Q1 2026 gross margin 66.2%; operating margin 58.1%.
- HPC was 61% of Q1 revenue.
- 3nm was 25% of wafer revenue; 5nm was 36%; 7nm was 13%; advanced technologies were 74%.
- 2026 capex expected toward high end of $52-56B.
- Management said demand is robust, especially HPC and AI, supply remains tight, and demand continues to increase.

Value-chain position:
- TSMC is the advanced manufacturing bottleneck beneath GPUs, custom ASICs, and TPUs.
- Google can design TPUs, but it cannot avoid the foundry layer.
- TSMC is a cleaner expression of advanced AI hardware capacity than Google, but it does not capture downstream ad/search/cloud economics.

Research implication:
- In AI infrastructure, Google is not at the top of the immediate scarcity stack. NVIDIA/Broadcom/TSMC capture a large share before Google monetizes the compute.

---

## 10. AI Agents And Search Alternatives

Primary source anchors:
- OpenAI ChatGPT agent: https://chatgpt.com/features/agent/
- OpenAI ChatGPT agent launch: https://openai.com/index/introducing-chatgpt-agent/
- OpenAI workspace agents: https://openai.com/index/introducing-workspace-agents-in-chatgpt/
- Alphabet Q1 2026 call transcript: https://abc.xyz/investor/events/event-details/2026/2026-Q1-Earnings-Call-2026-nW8kCrBAKS/default.aspx

Chain:

```text
User asks agent to do a job
  -> agent researches / browses / reasons / acts
     -> agent chooses merchant/app/source/workflow
        -> transaction/subscription/API/cloud usage
```

Why this attacks Search:
- Classic Search monetizes the moment a user expresses intent.
- Agents can capture the same moment and complete the workflow without a classic search results page.
- If agents become the default demand allocator, Google loses some control over ad inventory, attribution, and merchant relationships.

Why Google can defend:
- Search, AI Mode, Gemini, Android, Chrome, Gmail, Maps, Workspace, and YouTube give Google massive distribution.
- Management says AI Overviews/AI Mode are driving query growth, including commercial queries.
- Management is developing agentic commerce and Universal Commerce Protocol to support shopping journeys from discovery to purchase support.
- Google can move ads from links into AI-assisted commercial moments if user experience and advertiser ROI hold.

Where profit may be captured:
- Consumer subscription fees.
- Enterprise seats and agents.
- API usage.
- Cloud consumption.
- Ads or sponsored commercial information inside answers/actions.
- Transaction take-rates or merchant services.

Pricing power:
- Not yet proven. AI-native agents are early, product usage is visible qualitatively, but public unit economics are sparse.
- OpenAI and peers can challenge user behavior, but private company filings do not provide enough public revenue/margin/capex evidence for precise profit-pool sizing.

Attack surface for Google:
- Lower click-through from answer pages.
- Fewer monetizable ad slots.
- More expensive inference per query.
- Agents abstract away merchant/source choice.
- Prompt-injection and trust issues may slow agent adoption, but they do not eliminate the strategic threat.

Research implication:
- Agents are the key disintermediation risk. The right monitor is not generic ChatGPT usage; it is whether commercial tasks shift away from Google-controlled surfaces and whether Google preserves ad yield inside AI Mode/Gemini.

---

## 11. Supply / Demand And Bottleneck Summary

| Area | Demand signal | Supply constraint | Who has pricing power now? | Google read |
|---|---|---|---|---|
| Search ads | Q1 Search +19%; paid clicks +13%; CPC +5% | User trust, query volume, ad inventory | Google | Strong current moat, but AI RPM unknown |
| YouTube ads/subs | Ads +11%; subscriptions helped SP&D +19% | Creator supply, attention, rights | Google + creators | Good asset, less clean than Search |
| Network | Revenue down 4%; impressions down 9% | Open web inventory and privacy | Weaker | Not thesis-critical |
| GCP / Cloud AI | Revenue +63%; backlog $462B | Compute capacity, chips, data centers, power | Cloud vendors and upstream suppliers | Potential second engine; backlog margin unknown |
| TPUs / AI infra | Internal/external compute demand; TPU sales emerging | Advanced silicon, packaging, deployment | Google if TPU advantage is real; suppliers still strong | Strategic hedge, not yet quantified |
| Accelerators | NVDA Data Center +92%; AVGO AI semis +143% | GPU/ASIC/networking supply | NVDA / AVGO | Upstream leakage from Google capex |
| Foundry | TSMC HPC 61%; advanced nodes 74%; supply tight | Leading-edge fabs and packaging | TSMC | Dependency for TPU/GPU ecosystem |
| Data centers/power | 2026 Google capex $180-190B; 2027 up | Grid, power, land, permits, equipment | Local physical bottlenecks | Main owner-earnings risk |
| Agents | Product rollout by OpenAI/Google/MSFT/others | Trust, security, workflow reliability | Undecided | Biggest interface risk |

---

## 12. Final Industry / Value Chain Verdict

Google is still one of the most worth-studying companies in the AI/Search/Cloud/ads chain because it is the incumbent owner of the highest-quality ad intent pool and also a serious AI infrastructure/model/cloud operator.

But the profit-pool map is less favorable than a simple "AI helps Google" story:

- Search remains the current cash engine.
- YouTube is meaningful but pays creators and faces attention competition.
- Network is declining and strategically less important.
- GCP is becoming a real profit engine, with exceptional current growth and backlog.
- TPU/full-stack AI may be a cost advantage, but the economics are not disclosed.
- Semis and foundry suppliers are capturing very large current AI rents.
- Data centers and power are turning AI into a heavy capex cycle.
- AI agents can attack the interface layer where Search historically captured intent.

The investment conclusion from this module is `research yes, buy not proven`.

For Google to be the best AI investment expression, the next evidence must show:
- AI Search monetization is not materially dilutive.
- GCP backlog converts at attractive margins.
- TPU/full-stack infra lowers unit cost or creates external revenue.
- Capex intensity peaks or at least produces visible incremental ROIC.
- Agentic commerce keeps user task flow inside Google-controlled surfaces.

Until then, Google is best framed as a high-quality, high-uncertainty transition case. For pure current AI bottleneck capture, NVDA / AVGO / TSM are better comparables. For enterprise AI workflow, MSFT is cleaner. For commerce ads, AMZN is cleaner. For AI-enhanced consumer ads with less direct Search disruption, META is cleaner.

---

## 13. Source URLs

Alphabet:
- https://www.sec.gov/Archives/edgar/data/1652044/000165204426000048/goog-20260331.htm
- https://www.sec.gov/Archives/edgar/data/1652044/000165204426000043/googexhibit991q12026.htm
- https://abc.xyz/investor/events/event-details/2026/2026-Q1-Earnings-Call-2026-nW8kCrBAKS/default.aspx
- https://www.sec.gov/Archives/edgar/data/1652044/000165204426000018/goog-20251231.htm
- https://www.sec.gov/Archives/edgar/data/1652044/000165204426000012/googexhibit991q42025.htm
- https://www.sec.gov/Archives/edgar/data/1652044/000119312526257690/d159942d424b5.htm

Peers / suppliers:
- https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-first-quarter-fiscal-2027
- https://investors.broadcom.com/news-releases/news-release-details/broadcom-inc-announces-second-quarter-fiscal-year-2026-financial
- https://investor.tsmc.com/static/annualReports/2025/english/index.html
- https://investor.tsmc.com/english/quarterly-results/2026/q1
- https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-04/a7e3abe65a3fbc342aa55f9f53a5490dd621c1ac/1Q26%20Presentation%20%28E%29.pdf
- https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-04/3cef85204275f94fd111485cfdf4adb3c0263c45/TSMC%201Q26%20Transcript.pdf
- https://www.microsoft.com/en-us/investor/earnings/fy-2026-q3/press-release-webcast
- https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q3
- https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-First-Quarter-Results/default.aspx
- https://s21.q4cdn.com/399680738/files/doc_financials/2026/q1/Meta-03-31-2026-Exhibit-99-1_final.pdf
- https://www.sec.gov/Archives/edgar/data/1341439/000119312526265848/orcl-ex99_1.htm
- https://www.sec.gov/Archives/edgar/data/1341439/000119312526100148/orcl-ex99_1.htm
- https://chatgpt.com/features/agent/
- https://openai.com/index/introducing-chatgpt-agent/
- https://openai.com/index/introducing-workspace-agents-in-chatgpt/

---

## 14. Remaining Blockers

- AI Overviews / AI Mode RPM vs classic Search RPM is not disclosed.
- AI Mode / Gemini commercial query share is not disclosed.
- Google does not disclose TPU cost/performance, TPU utilization, or TPU vs GPU mix.
- Google does not split maintenance capex from growth capex.
- GCP backlog margin and mix are not disclosed at the granularity needed for owner-earnings underwriting.
- Power cost, grid interconnection timing, and data-center utilization by cohort are not disclosed.
- AI-native agent companies lack public filing-level economics, so their profit-pool impact remains mostly structural rather than quantified.
