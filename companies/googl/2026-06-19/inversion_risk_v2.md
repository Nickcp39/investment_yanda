# GOOGL Inversion / Risk v2

Last updated: 2026-06-16

Status: `P0_PASS_1 risk module draft, not final research completion`

Scope: Layer 8 of the Google v2 rerun. This file is intentionally limited to
inversion, risk paths, thresholds, and disconfirming evidence. It should connect
directly to `monitor-v2.md`.

Core question:

> If I wanted Alphabet to fail as a 10-year owner investment, how would I attack
> the business, the economics, the capital allocation, and the multiple?

Current base case is not "Google is failing." Current evidence says Search is
still strong, Cloud has accelerated, and AI demand is real. The inversion case is
that these facts can remain true for a while while owner earnings per share still
get damaged by lower Search economics, higher compute intensity, structural
remedies, dilution, and multiple compression.

---

## 1. Current Evidence Snapshot

| Area | Latest read | Risk interpretation |
|---|---:|---|
| Search & other revenue | Q1'26 $60.399B, +19.1% YoY | No revenue-level evidence of Search collapse yet. |
| Search paid clicks | Q1'26 +13% YoY | Usage / engagement still supports monetization. |
| Search CPC | Q1'26 +5% YoY | Auction price is still positive, but AI-specific RPM is undisclosed. |
| TAC rate | Q1'26 19.7%, down from 20.6% | Mix shift toward Search is favorable today. |
| Google Network revenue | Q1'26 $6.971B, -3.9% YoY | Open-web ad weakness is a value-chain warning signal. |
| Cloud revenue / margin | Q1'26 $20.028B, +63.4%; OI margin 32.9% | Strong, but needs multi-quarter proof after depreciation and TPU hardware revenue timing. |
| Cloud backlog | $462B at Q1'26 end; just over 50% expected within 24 months | Visibility is high, but backlog margin and cancellability are not solved. |
| Capex / OCF | Q1'26 capex $35.674B vs OCF $45.790B, 77.9% | Capex is now the central owner-earnings risk. |
| TTM FCF | Q1'26 TTM FCF $64.429B | FCF is compressed despite strong revenue and operating profit. |
| Buybacks / financing | Q1'26 repurchases $0; net debt proceeds $31.379B; June 2026 equity plan $80B | Capital return regime has changed. |
| Governance | Page / Brin control about 52.7% voting power through Class B | Outside shareholders cannot force capital discipline. |
| Price / valuation | Finance snapshot 2026-06-16: GOOGL about $373, market cap about $4.52T | Multiple leaves little room for a messy AI capex transition. |

---

## 2. Failure Path Matrix

### F1. AI Answer / Agent Disintermediation

Mechanism:

AI answers and agents become the user's default commercial interface. Users ask
the assistant, compare products inside the assistant, and let the assistant
complete the transaction. Google may still serve some information, but it loses
the highest-value handoff: query intent to ad auction to merchant click. The
attacker does not need to kill Search usage immediately. It only needs to move
the final commercial decision, attribution, and transaction data away from
Google-controlled surfaces.

Time scale:

1 to 3 years for early signal through query mix, paid clicks, CPC, and merchant
integrations. 3 to 7 years for default behavior to migrate. Full damage within
10 years if the next generation of shopping, travel, local, and productivity
queries starts outside Google.

Permanent damage vs temporary fluctuation:

Permanent if Google loses default habit, advertiser attribution, and merchant
transaction data. Temporary if AI Overviews, AI Mode, Gemini, Chrome, Android,
Maps, and UCP keep the agent workflow inside Google's surfaces and preserve
commercial measurement.

Today's evidence:

Search is not broken yet: Q1'26 Search & other revenue grew 19.1%, paid clicks
grew 13%, and CPC grew 5%. Management says AI Overviews and AI Mode are driving
greater Search usage and commercial query growth. The negative evidence is in
Alphabet's own risk factor: competitors may offer better experiences, consumers
may change how they obtain information online, and Google may need to spend
significant resources to compete.

Early signals:

- Search & other growth decelerates while AI answer usage rises.
- Paid clicks weaken before revenue weakens.
- CPC weakens in retail, finance, travel, local services, or shopping-like
  categories.
- Google referral traffic and merchant-reported Google-attributed conversions
  fall even if query volume looks healthy.
- Agentic checkout volume grows outside Google surfaces.
- Default distribution remedies make rival assistants easier to preload.

Kill criteria:

- Search & other revenue growth is <=8% YoY for two consecutive quarters without
  a macro-only explanation.
- Paid clicks are negative for two consecutive quarters while management still
  says AI query volume is rising.
- Management or advertiser commentary identifies AI answers / agents as a cause
  of lower click opportunity, lower conversion attribution, or lower ad load.
- Android, Chrome, browser, or OEM distribution changes produce measurable
  Search share loss in core markets.

Disconfirming evidence:

- Search & other remains double-digit growth while AI Mode / AI Overviews
  penetration rises.
- Paid clicks and CPC both stay positive across multiple quarters.
- UCP, AI Mode checkout, Gemini app, Chrome, Android, Maps, and Search retain
  merchant and advertiser attribution.
- Google discloses that AI-driven commercial queries have equal or better
  monetization than traditional Search.

### F2. Search RPM Risk

Mechanism:

AI can increase query count while reducing revenue per query or contribution
margin per query. The answer page may have fewer ads, different ad formats,
weaker click intent, more complex attribution, and higher inference cost. In that
case the headline metric "queries are up" is misleading: Google would be
serving more expensive interactions with lower RPM.

Time scale:

0 to 2 years through CPC, paid clicks, TAC, other cost of revenues, and Services
margin. 3 to 5 years through durable contribution-margin compression.

Permanent damage vs temporary fluctuation:

Permanent if users prefer low-ad AI answers and advertisers cannot measure or
bid against them at traditional Search ROI. Temporary if Google invents native
AI ad formats that improve coverage and conversion.

Today's evidence:

The key metric is not disclosed: AI Overviews / AI Mode RPM versus traditional
Search RPM. Current visible metrics are positive: Q1'26 paid clicks +13%, CPC
+5%, and TAC rate down to 19.7%. Management says more than 30% of customer
Search spend uses AI-enabled campaigns, and says Direct Offers and AI Mode ads
are in early tests. That supports the bull case, but it does not close the RPM
gap.

Early signals:

- CPC growth turns flat or negative while paid clicks remain positive.
- Paid clicks grow but Search & other revenue growth falls below the paid
  clicks x CPC relationship.
- Google Services margin compresses despite positive Search revenue.
- "Other cost of revenues" grows faster than Services revenue because AI answer
  serving costs rise.
- Advertisers report lower ROAS or weaker attribution inside AI answer formats.

Kill criteria:

- AI Search RPM is disclosed or reliably triangulated at 20%+ below traditional
  Search RPM for four quarters.
- CPC is negative for two consecutive quarters while paid clicks are positive.
- Google Services operating margin falls by 300 bps+ YoY for two consecutive
  quarters due primarily to AI serving cost, not one-time legal items.
- Management avoids AI Search monetization disclosure while Search growth falls
  below high single digits.

Disconfirming evidence:

- AI-enabled campaigns continue to show better conversions for the same spend.
- Google discloses AI Mode / AI Overview RPM parity or premium.
- CPC and paid clicks both remain positive as AI query share rises.
- Cost per core AI response continues to fall enough to protect contribution
  margin.

### F3. Capex Black Hole

Mechanism:

Google spends hundreds of billions on data centers, servers, networking,
electricity, and TPU/GPU capacity to defend Search and compete in Cloud. If the
spend is defensive rather than high-return growth capex, revenue and operating
income may grow while owner earnings per share stagnate. The damage comes
through capex, depreciation, energy costs, interest, leases, purchase
commitments, paused buybacks, and possible equity dilution.

Time scale:

1 to 3 years for capex/OCF, assets not yet in service, and financing to show up.
3 to 7 years for depreciation, utilization, and replacement cycles to decide
incremental ROIC.

Permanent damage vs temporary fluctuation:

Permanent if the infrastructure becomes a low-return replacement cost for the
old Search moat or if AI hardware becomes obsolete before earning its cost of
capital. Temporary if capex peaks, utilization fills, Cloud and Search absorb
depreciation, and FCF/share resumes compounding.

Today's evidence:

Q1'26 capex was $35.674B, up 107% YoY, versus OCF of $45.790B. Capex/OCF was
77.9%. Assets not yet in service increased to $108.597B at March 31, 2026.
Alphabet guides 2026 capex to $180B to $190B and says 2027 capex will
significantly increase versus 2026. Q1'26 repurchases were $0, net debt
proceeds were $31.379B, and the June 2026 financing documents describe an $80B
equity capital raise tied to AI infrastructure and compute.

Early signals:

- Capex guidance is raised again without a numeric payback or ROIC framework.
- Assets not yet in service grow faster than revenue and faster than in-service
  PPE.
- Depreciation, energy, and data-center operations cost grow faster than revenue.
- Purchase commitments and lease backstops grow faster than OCF.
- Buybacks stay paused while SBC continues.
- Management frames capex as capacity urgency rather than returns.

Kill criteria:

- Full-year capex/OCF remains >70% for two consecutive years without disclosed
  incremental ROIC improvement.
- FCF/share declines for two consecutive years.
- Net share count rises by >1% in a year because buybacks no longer offset SBC
  and equity issuance.
- Depreciation and data-center operations cost cause consolidated operating
  margin to fall despite double-digit revenue growth.
- A material data-center, TPU, or AI infrastructure impairment is recorded.

Disconfirming evidence:

- Capex/OCF falls below 60% while Search and Cloud stay healthy.
- FCF/share grows again after the capex build.
- Cloud backlog converts at high margin and Search AI monetization is at least
  comparable to traditional Search.
- Management provides utilization, payback, and incremental ROIC metrics that
  connect capex to owner earnings.

### F4. Cloud Margin Deterioration

Mechanism:

Cloud looks like a second high-quality engine, but AI infrastructure revenue can
be lower margin, more cyclical, more hardware-heavy, and more depreciation-heavy
than software-like Cloud revenue. Backlog may include TPU hardware sales,
long-duration contracts, or capacity commitments that convert at lower margins
than the Q1'26 snapshot implies.

Time scale:

1 to 2 years for margin normalization and backlog conversion. 3 to 5 years for
price competition, utilization, and depreciation to reveal real economics.

Permanent damage vs temporary fluctuation:

Permanent if Cloud becomes a capital-intensive commodity compute reseller.
Temporary if Q1'26 margin normalizes modestly but stays high because Google's
TPU, software, data, security, and enterprise workflow stack creates real cost
advantage and switching costs.

Today's evidence:

Q1'26 Cloud revenue grew 63.4% to $20.028B and Cloud operating income grew to
$6.598B, a 32.9% operating margin. Management says backlog reached $462B and
just over 50% should convert to revenue in 24 months. It also says TPU hardware
revenues will be lumpy and mostly recognized in 2027, Wiz will create a low
single-digit margin headwind, and higher technical infrastructure investment
will pressure depreciation and energy cost.

Early signals:

- Cloud revenue remains high growth but operating margin falls below 25%.
- Backlog grows but backlog-to-revenue conversion slows.
- Cloud OI dollars flatten despite revenue growth.
- TPU hardware sales create revenue spikes without durable margin.
- Customers overrun initial commitments but Google cannot fulfill because of
  capacity limits.
- Price cuts by cloud peers show up in GCP gross/operating margin.

Kill criteria:

- Cloud operating margin falls below 20% for two consecutive quarters while
  revenue still grows >25%.
- Cloud operating income is flat or down YoY for two consecutive quarters.
- Backlog conversion is materially below management's "just over 50% in 24
  months" expectation.
- Management attributes margin pressure to AI compute pricing, utilization, or
  depreciation rather than temporary acquisition costs.

Disconfirming evidence:

- Cloud operating margin stays >=30% for several quarters after higher
  depreciation begins.
- Cloud OI grows at least in line with Cloud revenue.
- Backlog converts into revenue on schedule with no margin disappointment.
- Google shows TPU / full-stack infrastructure delivers structurally lower unit
  cost than GPU-only competitors.

### F5. Regulatory Structural Remedy

Mechanism:

Regulators attack the distribution and adtech structure that makes Google's
intent machine self-reinforcing. Remedies can reduce default Search access,
force data/syndication sharing, ban exclusive agreements, or separate parts of
the adtech stack. The risk is not a fine. The risk is a structural impairment to
distribution, auction liquidity, data advantage, or take rate.

Time scale:

Event-driven over 0 to 3 years for orders and appeals. Economic impact can take
3 to 7 years as contracts renew and competitors use mandated access.

Permanent damage vs temporary fluctuation:

Permanent if remedies remove default distribution, force divestiture, or create
durable rivals using Google's data and ad syndication. Temporary if outcomes are
fines, narrow behavioral changes, or remedies that Google absorbs without share
loss or margin loss.

Today's evidence:

The DOJ search remedy already bars certain exclusive contracts relating to
Google Search, Chrome, Google Assistant, and Gemini, and requires certain search
index/user-interaction data and search/text-ad syndication to rivals. In adtech,
the DOJ won a monopolization decision in 2025, and Alphabet's 2025 10-K says the
DOJ's adtech remedy proposal includes structural remedies that could harm the
business. The EC also sent DMA preliminary findings related to Google Search
self-preferencing and Google Play steering.

Early signals:

- OEM, browser, carrier, or platform contracts renew with weaker default
  economics or lower exclusivity.
- Search share declines in markets affected by remedies.
- TAC rises because Google pays more to preserve non-exclusive placement.
- Competitors use mandated index / interaction data to improve search or AI
  products.
- Adtech remedy drafts include divestiture, auction separation, or data
  firewalls.
- EU DMA findings convert into binding changes, fines, or product redesigns.

Kill criteria:

- A final order or settlement requires divestiture of Ad Manager, AdX, Chrome,
  Android distribution assets, or other structural separation.
- Default Search agreements are banned or economically impaired enough to reduce
  Search share in core markets.
- Regulators require open access to Search/ads data at terms that materially
  reduce Google's data advantage or take rate.
- TAC rises by 300 bps+ from remedy-related distribution changes.

Disconfirming evidence:

- Remedies remain behavioral, narrow, and non-structural.
- Google keeps default distribution through compliant non-exclusive agreements.
- Search share and TAC remain stable after remedy implementation.
- Appeals narrow the most damaging remedy terms.

### F6. Ad Budget Migration

Mechanism:

Advertisers shift budget toward retail media, social/video, CTV, marketplaces,
vertical search, creator commerce, and AI/agentic shopping platforms where the
transaction data is closer to purchase. Google keeps broad search volume, but
the highest-intent categories migrate to closed loops that can prove conversion
better.

Time scale:

1 to 3 years for category CPC and budget share. 3 to 7 years if retail media and
agentic commerce become the default transaction layer.

Permanent damage vs temporary fluctuation:

Permanent if Google loses merchant conversion data and bottom-funnel attribution
in the highest-value verticals. Temporary if Google remains the discovery,
comparison, and checkout layer through Search, YouTube, Maps, Merchant Center,
AI Mode, Gemini, and UCP.

Today's evidence:

Mixed. Q1'26 Search & other grew 19% driven by retail and financial services,
and YouTube ads grew 11%. But Google Network revenue fell 4%, showing weaker
open-web ad inventory. Management is explicitly building AI Mode offers, retail
ad formats, UCP, and direct checkout experiences, which confirms that the
transaction layer is contested.

Early signals:

- Retail, finance, travel, local, and shopping CPC weaken before aggregate CPC.
- Google Network weakness spreads to YouTube direct response or Search.
- Merchant comments show higher ROI in marketplace / retail media than Google.
- UCP adoption happens outside Google-controlled surfaces.
- Advertisers increase spend in closed-loop commerce platforms while Search
  budget growth slows.

Kill criteria:

- Google advertising revenue growth falls below 5% for four quarters while
  broader digital ad spending is positive.
- Search & other grows below market for four quarters in core commercial
  verticals.
- Retail / finance CPC is negative for two quarters without macro weakness.
- YouTube direct response slows while CTV / creator commerce competitors gain
  share.

Disconfirming evidence:

- Search CPC and paid clicks stay positive in commercial verticals.
- AI Max, Performance Max, Direct Offers, and UCP improve conversion and keep
  merchant data inside Google.
- YouTube direct response and living-room monetization continue to grow.
- Network weakness remains isolated and does not bleed into owned surfaces.

### F7. Talent / Product Execution

Mechanism:

Google fails not from lack of assets, but from product execution. The best AI
talent leaves or is diluted by bureaucracy. Gemini, AI Mode, Cloud AI, and ads
tools lag user expectations. Products become fragmented across Search, Gemini,
Chrome, Android, Workspace, and Cloud. Trust failures, latency, model quality,
or monetization delays make users and enterprises choose alternatives.

Time scale:

0 to 2 years for product share and adoption signals. 3 to 5 years for talent
loss and product misses to show up in revenue. Full 10-year damage if Google is
not the default AI workflow for consumers, developers, or enterprises.

Permanent damage vs temporary fluctuation:

Permanent if AI product habit forms elsewhere and Google cannot regain default
status. Temporary if product quality improves quickly and distribution pulls
users back.

Today's evidence:

Positive evidence exists: management says Search latency improved, core AI
response cost fell, Gemini Enterprise paid MAUs grew 40% QoQ, and Cloud
customers are processing large token volumes. Negative evidence is structural:
Alphabet's 10-K warns that similar or superior competing AI technologies, poor
responsiveness to user/customer needs, or misallocated investment could harm
financial results. SBC is also large, so talent retention is costly: Q1'26
cash-flow SBC add-back was $6.751B and 10-Q total SBC was $7.2B.

Early signals:

- Gemini / AI Mode usage or paid conversion stalls.
- Google loses frontier model benchmark parity for multiple releases.
- Cloud AI customer wins slow or workloads migrate to competitors.
- Top AI researchers or product leaders depart in clusters.
- Product incidents create trust or brand damage.
- SBC and headcount rise without matching product adoption.

Kill criteria:

- Gemini / AI Mode paid or active-user metrics decline for two consecutive
  quarters after broader launch.
- Cloud AI revenue slows sharply despite industry AI workload growth.
- Two major product cycles in a row are perceived as behind OpenAI, Anthropic,
  Microsoft, Meta, or other agent platforms.
- Key AI leadership departures coincide with delayed product launches or model
  quality gaps.

Disconfirming evidence:

- Gemini, AI Mode, and Search AI usage keep rising with strong retention.
- Google maintains frontier model parity and lower serving cost.
- Cloud AI customer count, token usage, backlog, and paid MAUs grow while margin
  stays high.
- Talent retention improves without SBC as a percentage of revenue rising.

### F8. Governance / Control Risk

Mechanism:

Dual-class control lets founders and management pursue very long-duration AI
infrastructure bets with limited outside shareholder influence. That can be a
strength when the bets are right, but a risk when capital intensity rises,
buybacks pause, equity is issued, and management does not disclose hard ROI
metrics. The attack is simple: let Google overbuild because nobody can force
discipline soon enough.

Time scale:

Immediate for financing and disclosure. 3 to 7 years for whether capital
allocation creates or destroys owner earnings.

Permanent damage vs temporary fluctuation:

Permanent if control structure enables repeated low-return capex, dilution,
acquisitions, or Other Bets funding with no corrective mechanism. Temporary if
founder control supports patient high-ROIC investment and management eventually
proves returns.

Today's evidence:

As of the 2025 10-K, Larry Page and Sergey Brin controlled about 52.7% of voting
power through Class B shares. Q1'26 repurchases were $0 despite $69.5B remaining
authorized. June 2026 financing documents give management broad discretion in
use of proceeds and describe common/preferred/ATM equity issuance tied to AI
infrastructure and compute. Management discusses ROIC frameworks, but no public
numeric hurdle rate, payback period, or utilization target is disclosed.

Early signals:

- Capex guidance rises repeatedly without numeric return metrics.
- Management issues equity or preferred stock while still not proving FCF/share
  accretion.
- Share count rises despite large historic buyback authorizations.
- Compensation remains tied more to revenue/product scale than FCF/share or
  ROIC.
- Major acquisitions or infrastructure backstops increase complexity without
  clear return disclosure.

Kill criteria:

- Net share count rises >2% cumulatively over two years while FCF/share is flat
  or down.
- Additional $100B+ debt/equity/preferred funding is raised for AI capex without
  disclosed incremental ROIC.
- Management refuses to provide capex ROI, utilization, or payback metrics for
  four consecutive earnings cycles.
- Material impairment, stranded capacity, or abandoned data-center spend occurs
  and governance response is cosmetic.

Disconfirming evidence:

- Management links capex to measurable ROIC, utilization, payback, and FCF/share.
- Share count stabilizes or declines after the capex peak.
- Compensation and capital allocation messaging shift toward owner earnings.
- Board / management cancel or delay projects when returns weaken.

### F9. Valuation Risk

Mechanism:

Even if Google remains an excellent company, the stock can fail if the entry
price assumes a smooth AI transition. A low owner-earnings yield plus uncertain
capex conversion means the investor can be right on products but wrong on
returns. Multiple compression can erase years of operating progress.

Time scale:

Immediate for entry price. 3 to 10 years for realized IRR.

Permanent damage vs temporary fluctuation:

Permanent for the investor if capital is deployed at a price that requires
unrealistic owner-earnings compounding. Temporary if price falls far enough or
owner earnings inflect enough to restore margin of safety.

Today's evidence:

Finance snapshot on 2026-06-16 showed GOOGL around $373 and market cap about
$4.52T. The local implied-expectations model uses owner earnings branches of
roughly $52B defensive, $65B midpoint, and $80B growth. At current-like market
cap, that is roughly 87x, 70x, and 57x owner earnings. The model is directional
and needs rebuild, but it shows the price assumes the AI capex cycle works.

Early signals:

- Price stays high while FCF/share falls.
- Multiple remains high despite capex/OCF >70%.
- Market treats non-operating equity gains as core earnings.
- Buybacks remain paused, reducing per-share support.
- Consensus raises revenue estimates but lowers FCF/share or owner earnings.

Kill criteria:

- Stock price implies <8% 10-year IRR under conservative owner-earnings branches
  after refreshed capex and dilution assumptions.
- Price-to-owner-earnings remains >35x while FCF/share is declining.
- Net dilution begins while the stock trades at an owner-earnings yield below
  3%.
- A buy decision requires the growth-capex branch to be right and has no margin
  of safety under the mixed branch.

Disconfirming evidence:

- Price falls to a level where the defensive or mixed branch offers acceptable
  IRR.
- Owner earnings per share inflect upward despite elevated capex.
- Capex/OCF normalizes, buybacks resume, and the multiple is supported by
  FCF/share growth rather than narrative.

---

## 3. Cross-Risk Interactions

| Interaction | Why it matters | Monitor linkage |
|---|---|---|
| AI disintermediation plus Search RPM | Usage can rise while RPM falls; headline queries are not enough. | Search growth, paid clicks, CPC, AI RPM proxy, Services margin. |
| Capex black hole plus Cloud margin | Cloud can grow while incremental returns disappoint. | Cloud revenue, Cloud OI margin, backlog conversion, capex/OCF, D&A. |
| Regulation plus ad budget migration | Remedies can make it easier for rival search, adtech, and agent platforms to capture budget. | DOJ/EU event log, TAC rate, Search share proxies, CPC by vertical. |
| Governance plus valuation | Dual-class control and high multiple magnify mistakes because outside shareholders cannot force a pivot. | Share count, SBC, buybacks, debt/equity issuance, ROI disclosure, price/OE. |

---

## 4. Blockers Still Unresolved

- AI Overviews / AI Mode RPM versus traditional Search RPM is not disclosed.
- Maintenance capex versus growth capex remains unsolved.
- Cloud backlog margin, cancellation terms, and actual 24-month conversion are
  not proven.
- Management has referenced ROIC discipline but has not disclosed a numeric AI
  capex hurdle rate, utilization target, or payback period.
- The implied-expectations / buy-below model needs a full rebuild after updated
  financing dilution and capex split.

---

## 5. Source Anchors

- Alphabet Q1 2026 Form 10-Q: https://www.sec.gov/Archives/edgar/data/1652044/000165204426000048/goog-20260331.htm
- Alphabet Q1 2026 earnings release, Exhibit 99.1: https://www.sec.gov/Archives/edgar/data/1652044/000165204426000043/googexhibit991q12026.htm
- Alphabet FY2025 Form 10-K: https://www.sec.gov/Archives/edgar/data/1652044/000165204426000018/goog-20251231.htm
- Alphabet Q1 2026 official earnings call transcript: https://abc.xyz/investor/events/event-details/2026/2026-Q1-Earnings-Call-2026-nW8kCrBAKS/default.aspx
- Alphabet June 2026 FWP: https://www.sec.gov/Archives/edgar/data/1652044/000119312526251733/d160205dfwp.htm
- Alphabet June 2026 424B5 supplement: https://www.sec.gov/Archives/edgar/data/1652044/000119312526257690/d159942d424b5.htm
- DOJ search remedies press release: https://www.justice.gov/opa/pr/department-justice-wins-significant-remedies-against-google
- DOJ adtech monopolization press release: https://www.justice.gov/opa/pr/department-justice-prevails-landmark-antitrust-case-against-google
- European Commission DMA preliminary findings on Alphabet: https://digital-markets-act.ec.europa.eu/commission-sends-preliminary-findings-alphabet-under-digital-markets-act-2025-03-19_en
- European Commission adtech fine press release: https://ec.europa.eu/commission/presscorner/detail/en/ip_25_1992
- Local model inputs: `companies/googl/model/search_unit_economics_v2.csv`, `companies/googl/model/capex_bridge_v2.csv`, `companies/googl/model/cloud_quality_v2.csv`, `companies/googl/model/owner_earnings_v2.csv`, `companies/googl/model/implied_expectations_v2.csv`
