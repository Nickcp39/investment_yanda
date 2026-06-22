# GOOGL Moat / Bottleneck v2

Last updated: 2026-06-16

Status: `P0_PASS_1 working memo`。本文件只补第 6 层 Moat / Bottleneck，不代表 Google v2 完整重跑已完成。

决策视角：10 年 owner earnings。

---

## 0. 一句话结论

Alphabet 仍有真实护城河，但护城河的形态正在从“搜索框 + 默认分发 + 广告拍卖”迁移到“商业意图入口 + AI/agent 界面 + 全栈算力 + Cloud 数据重力”。存量护城河很强，增量护城河尚未被 owner earnings 证明。

三条总裁决：

- **旧护城河是否正在迁移？** 是。旧河不是消失，而是从经典 Search 结果页迁移到 AI Mode / AI Overviews / Gemini / Android / Chrome / YouTube / Cloud 的多入口任务完成系统。
- **Google 控制的是搜索框还是商业意图入口？** 历史上两者都控制；未来要承保的是它能否继续控制商业意图入口。搜索框仍强，但 AI 助手、垂直电商、retail media、设备级 agent 都能在搜索框之前截流意图。
- **AI capex 是新护城河还是防守税？** 分层看。TPU、全栈工程、Cloud 数据重力和现成分发有机会成为新护城河；电力、数据中心、上游芯片/封装/HBM、折旧和融资稀释也可能只是保住旧河的防守税。当前公开证据不能证明 blended incremental ROIC。

---

## 1. 证据纪律

标签：

- `A1`：SEC 文件或官方 earnings release。
- `A2`：官方电话会 transcript / 官方 Google blog，作为管理层陈述使用。
- `LEGAL`：法院、监管机构或 DOJ/EC 官方材料。
- `OPEN`：重要但未直接证明。
- `INFERENCE`：由证据推导的技术/经济判断，非直接披露。

核心一手证据锚：

- FY2025 10-K：Search & other 收入 $224.5B；YouTube ads $40.4B；Google Network $29.8B；Google Services $342.7B；Google Cloud $58.7B；Search paid clicks +6%、CPC +7%；Network impressions -7%、CPI +7%；TAC rate 从 20.7% 降至 20.3%；capex $91.4B；OCF $164.7B；purchase commitments $149.1B，其中 $113.0B 为 short-term，主要是 technical infrastructure 和 inventory orders。`A1`
- Q1 2026 release：Search & other +19% 至 $60.4B；YouTube ads +11% 至 $9.9B；Network 降至 $7.0B；Google Cloud +63% 至 $20.0B、OI $6.6B；total TAC $15.2B；回购 $0；发债 proceeds $31.4B。`A1`
- Q1 2026 10-Q：Q1 capex $35.7B vs Q1 2025 $17.2B；assets not yet in service $108.6B；data-center leases not yet commenced future payments $75.6B；公司预期 technical infrastructure investment 相对 2025 显著增加。`A1`
- June 2026 FWP / 424B5：$80B equity capital raise 用于 AI infrastructure / global compute；2026 capex expected $180B-$190B，2027 capex expected to significantly increase；debt balance over $100B；Cloud backlog over $460B，其中约 50% expected recognized within 24 months。`A1`
- DOJ Search remedies：法院禁止 Google 维持/签订与 Google Search、Chrome、Google Assistant、Gemini app 分发相关的 exclusive contracts，要求提供部分 search index / user-interaction data 和 search ads syndication。DOJ 称 Google 占美国约 90% search queries，并通过默认协议锁定 billions of devices。`LEGAL`
- FY2025 10-K legal section：Search final judgment 已进入分发限制、data sharing、syndication；adtech remedy proposal 包含可能 materially affect business 的 structural remedies；EC adtech fine EUR3.0B，Alphabet 计提 $3.5B charge。`A1/LEGAL`
- Google 官方 TPU / AI infrastructure blog：Ironwood 是第七代 TPU、为 inference 设计；Google Cloud 将 AI Hypercomputer 定位为 optimized full-stack infrastructure。`A2`

---

## 2. 护城河总表

| 护城河 / 瓶颈 | 7 Powers / Greenwald / Buffett 视角 | 当前强度 | 方向 | 证据质量 | 最关键监控 |
|---|---|---:|---|---|---|
| Search habit / default distribution | Network economies、brand habit、customer captivity、分发权 | 强，但被监管削弱 | 迁移中 | A1 + LEGAL | Search 增速、TAC、默认分发 remedies |
| Ad auction liquidity | Network economies、switching costs、scale economies | 自有面强；Network 弱化 | 混合 | A1 | CPC/paid clicks、Network 下滑、adtech remedies |
| YouTube network | Network economies、brand、creator switching costs | 中强 | 稳定偏正 | A1/A2 | watch time、creator economics、subscriptions |
| Android / Chrome distribution | Distribution power、ecosystem captivity | 中强，但被监管削弱 | 承压 | A1 + LEGAL | remedy implementation、默认位、app bundling |
| Cloud switching / data gravity | Switching costs、scale economies、process power | 增强 | 正向 | A1/A2 | backlog conversion、margin durability |
| TPU / full-stack cost advantage | Process power、scale economies、proprietary know-how | 有潜力，未证明 | 正向但缺量化 | A2 + INFERENCE | cost per AI response、utilization、TPU adoption |
| Gemini / AI distribution | 分发权、bundling、data/network effects | 有潜力，早期 | 正向但未定 | A1/A2 + OPEN | AI Search RPM、Gemini paid conversion |
| Data center / power / compute bottleneck | 只有被拥有并高 ROIC 变现时才是 cornered resource | 混合 | 趋紧 | A1 + INFERENCE | capex/OCF、电力、折旧、leases、share count |

---

## 3. Search Habit / Default Distribution

### 机制

Google Search 的护城河不是“有一个搜索框”，而是习惯与分发叠加：用户在信息、购物、本地服务、地图、旅行、金融、技术问题上默认从 Google 系统开始；Chrome omnibox、Android、Google app、Maps、YouTube 和分发协议进一步降低进入摩擦。

按 7 Powers，这是 **network economies + brand habit + distribution power**；按 Greenwald，这是 demand-side customer captivity；按 Buffett，这是无需显性涨价也能通过 auction CPC 体现的定价权。

### 为什么能转化为超额利润

Search 捕获的是购买/决策前的商业意图。广告主不是买泛注意力，而是在买可衡量的高意图客户获取。只要 ROI 成立，广告主愿意继续出价；广告主分散且拍卖清算，使 Google 能捕获高意图流量的经济租。

### 证据

- FY2025 Search & other revenue $224.5B，Search paid clicks +6%、CPC +7%。`A1`
- Q1 2026 Search & other revenue $60.4B，+19%。`A1`
- 管理层称 AI Mode / AI Overviews 正在增加 Search usage，queries at all-time high。`A2`
- 本地 raw extract 记录 Q1 2026 paid clicks +13%、CPC +5%。`A1/local extract`
- TAC rate FY2025 从 20.7% 降至 20.3%；Q1 2026 local extract 也显示 TAC / Google advertising revenue 改善。`A1`
- DOJ remedies 直接针对默认分发和排他协议，说明默认分发是经济上足够重要的竞争瓶颈。`LEGAL`

### 攻击面

- **监管削弱默认分发**：Search final judgment 限制 exclusive contracts，并要求数据共享 / syndication。
- **AI answer 绕过搜索框**：ChatGPT、Perplexity、Anthropic、Gemini app、Apple/OEM assistant、vertical agents 都可能在经典 SERP 前截流。
- **商业旅程压缩**：agent 从研究到下单一站完成，可能减少广告位、点击和归因。
- **TAC 上升**：不能长期排他时，Google 可能需要用更高成本重新买回流量或接受份额下降。

### 监控指标

- Search & other growth、paid clicks、CPC。
- TAC dollars / TAC rate，尤其 Search & other vs Network 口径。`OPEN`
- 默认协议、DOJ remedies 执行、Chrome/Android 默认位变化。
- AI Overview / AI Mode query volume 与 monetization。`OPEN`
- AI Search RPM vs traditional Search RPM。`OPEN - blocking`
- 商业查询 share、agentic checkout volume。`OPEN`

### 承保判断

当前仍强，但正在迁移。真正要保的是商业意图入口，不是旧搜索框形式本身。

---

## 4. Ad Auction Liquidity

### 机制

Google Ads 是流动性市场：

```text
更多用户意图 -> 更多广告库存与转化信号
更多广告主出价 -> 更高出清价与更高填充
更好 ROI -> 预算留存和更多竞价
```

自有面 Search / Maps / Gmail / YouTube / Discover / Shopping / AI Mode 最强；第三方 Network 较弱，因为 TAC 高、open web 承压、监管更直接攻击 adtech 中介栈。

### 为什么能转化为超额利润

广告主在 Google 上买的是 measurable ROI。Google 通过 auction liquidity 捕获广告主愿付价格与服务成本之间的 spread；广告主的 campaign、conversion tags、attribution、Smart Bidding、Performance Max / AI Max 工作流形成 switching costs。

### 证据

- FY2025 Google advertising revenue $294.7B；Google Services revenue $342.7B，segment OI $139.4B。`A1`
- FY2025 Search paid clicks +6%、CPC +7%，量价同升。`A1`
- Q1 2026 Search & other +19%；YouTube ads +11%；Google advertising 从 $66.9B 增至 $77.3B。`A1`
- 管理层称超过 30% customer Search spend 使用 AI-enabled campaigns（AI Max / Performance Max）。`A2`
- 负面：Google Network FY2025 从 $30.4B 降至 $29.8B，Q1 2026 YoY -4%。`A1/A2`
- 监管负面：adtech remedy proposal 包含 structural remedies，可能 materially affect business；EC adtech fine EUR3.0B，Alphabet 计提 $3.5B charge。`A1/LEGAL`

### 攻击面

- **DOJ / EC adtech remedies**：拆分、互操作或数据开放可能削弱纵向一体化 auction edge。
- **Retail media / vertical ads**：Amazon、Walmart、TikTok Shop、travel verticals 等在交易附近捕获意图。
- **AI commerce agents**：关键词竞价可能让位于 agent 工作流中的 offer / placement。
- **Privacy / signal loss**：cookie、归因、用户级信号弱化会降低广告主 ROI 信心。
- **Network secular decline**：第三方网页广告池收缩可能持续。

### 监控指标

- CPC、paid clicks、conversion rate、advertiser ROI。`OPEN where not disclosed`
- AI-enabled campaigns adoption 与 conversion lift。
- Google Network revenue、impressions、CPI。
- TAC mix shift。
- adtech remedy final judgment。
- retail media share、agentic commerce adoption。`OPEN/INFERENCE`

### 承保判断

自有面 auction liquidity 是强护城河；第三方 Network 和 integrated adtech stack 已经有负面证据，不能无条件当成同等强度的护城河。

---

## 5. YouTube Network

### 机制

YouTube 是双边网络：

```text
观众 watch time -> 吸引创作者 -> 内容供给增加 -> 更多观众
广告/订阅收入 -> 创作者变现 -> 创作者留存 -> 内容供给加深
```

推荐系统用观看行为数据改善匹配；长视频、Shorts、music、podcasts、live、CTV、subscriptions 扩大使用场景。

### 为什么能转化为超额利润

YouTube 能通过广告和订阅变现注意力，并通过创作者生态形成内容供给壁垒。但它的定价权弱于 Search：注意力可替代，创作者/版权方需要分成，TikTok/Reels/streaming/podcasts 争夺时间。

### 证据

- FY2025 YouTube ads revenue $40.4B，up from $36.1B。`A1`
- Q1 2026 YouTube ads +11% 至 $9.9B。`A1`
- 管理层称 YouTube 已连续三年领导美国 streaming watch time，并称 YouTube subscriptions revenue continues to grow faster than ads，尤其 Music & Premium。`A2`
- Q1 2026 release 称 Alphabet paid subscriptions 达 350M，YouTube 与 Google One 是 key drivers，但未单独拆分 YouTube 订阅。`A1`

### 攻击面

- **短视频竞争**：TikTok、Reels 等争夺时间和创作者。
- **创作者 multi-homing**：头部创作者可转向多平台、直接订阅、直播、电商、podcast。
- **AI-generated video**：增加供给，也可能压低内容稀缺性。
- **版权/内容成本**：music、sports、podcasts、premium video 可能抬高成本。
- **广告周期性**：brand ads 相比高意图 Search 更周期。

### 监控指标

- watch time / streaming share。
- creator count、creator payout、creator churn。`OPEN`
- Shorts monetization vs long-form。`OPEN`
- YouTube Premium / Music / TV subscribers and ARPU。`OPEN`
- YouTube ads growth vs Search growth。
- creator revenue share / content cost inflation。`OPEN/INFERENCE`

### 承保判断

YouTube 是真实网络效应，但质量不如 Search 的高意图广告。它扩展 Alphabet 的注意力面和广告主触达面，不应被承保成与 Search 等价的定价权。

---

## 6. Android / Chrome Distribution

### 机制

Android 和 Chrome 是分发基础设施：Android 把 Google 服务预置到移动端；Chrome 把 omnibox、sync、identity、extensions 和 web default 变成入口；Play / Maps / Gmail / Photos / YouTube / Search / Assistant-Gemini 互相导流。

这不是单独利润池，而是把流量喂给 Search、YouTube、Play、Gemini 和 subscriptions 的管道。

### 为什么能转化为超额利润

分发降低获客成本、保住默认行为，并把利润体现在下游：

- Search ads 来自 default search access points。
- YouTube engagement 与 subscriptions。
- Play fees / in-app purchase economics。
- Gemini 默认分发与 AI-agent 入口。
- identity / personalization / data feedback 改善广告相关性。

### 证据

- 10-K 定义 Search & other 包括来自 search distribution partners 的默认搜索流量。`A1`
- Google Services 包含 ads、Android、Chrome、devices、Maps、Play、Search、YouTube。`A1`
- DOJ remedies 禁止与 Google Search、Chrome、Google Assistant、Gemini app 分发相关的 exclusive contracts，并限制 app placement / revenue-share tying。`LEGAL`
- 10-K 披露 Android / Play 相关 antitrust proceedings、ordered remedies、appeals / settlements。`A1/LEGAL`

### 攻击面

- **Search distribution remedies**：弱化 default placement 的排他性。
- **Android / Play remedies**：第三方 app store、billing 和 app placement 改变生态控制。
- **Apple / Samsung / OEM AI**：设备级 assistant 可能成为比 Google Search 更前置的入口。
- **AI browser**：Perplexity/OpenAI 类浏览器攻击 Chrome omnibox。
- **数据共享 remedies**：search data / syndication 可提高 rival quality。

### 监控指标

- Chrome / Android search default share by geography。`OPEN`
- TAC paid to distribution partners、default agreement terms。`OPEN`
- DOJ remedy implementation and appeals。
- Play revenue / take rate / billing impact。`OPEN`
- Gemini default placement across Android / Chrome / Workspace / Search。
- AI-browser adoption。`OPEN/INFERENCE`

### 承保判断

Android/Chrome 仍是强分发资产，但不再能假设“默认位可无限排他购买”。护城河还在，排他性被法院和监管压低。

---

## 7. Cloud Switching Costs / Data Gravity

### 机制

Cloud 护城河不是“规模大”四个字，而是 switching costs + data gravity：

- 企业把数据、应用、identity、security、observability、workflows、AI pipelines 迁入云。
- BigQuery、Vertex AI、GKE、Workspace、Security、Gemini Enterprise 等形成工作流嵌入。
- AI 加深 data gravity：training、fine-tuning、RAG、agents、inference 都需要低延迟接近企业数据。

### 为什么能转化为超额利润

Cloud 只有在高利用率和软件/AI attach 覆盖资本密集度时才赚超额利润：

```text
multi-year commitments + high utilization + software/AI attach
-> higher gross margin / operating margin
```

如果客户扩容快于 multi-cloud 迁出，且 Google 能摊薄网络、数据中心、security、model、engineering 成本，Cloud 就从“追赶型 IaaS”变为高质量平台。

### 证据

- FY2025 Google Cloud revenue $58.7B，+36%；OI $13.9B。`A1`
- Q1 2026 Google Cloud revenue $20.0B，+63%；OI $6.6B，季度 operating margin 约 32.9%。`A1`
- Q1 2026 release 称 Cloud backlog over $460B，QoQ nearly doubled。`A1`
- June 2026 FWP 称 backlog 约 50% expected recognized over next 24 months。`A1`
- 管理层称 Cloud revenue would have been higher if demand could be met，说明短期更像供给约束而非需求不足。`A2`
- 管理层称 enterprise AI solutions 首次成为 Cloud primary growth driver。`A2`

### 攻击面

- **AWS/Azure**：大客户保留 multi-cloud 议价权。
- **专用 AI 云 / GPU 云**：CoreWeave 类玩家和 hyperscalers 在 GPU availability / price 上竞争。
- **Mega-deal margin risk**：大型 AI 合约可能低 margin、可取消或再议价。`OPEN`
- **折旧滞后**：当前 margin 可能早于新 capex 的完整折旧冲击。
- **Backlog 质量**：RPO 中不同产品、硬件、TPU、服务、Workspace 的 margin 未披露。

### 监控指标

- Cloud revenue growth、operating margin 多季度趋势。
- backlog/RPO、conversion timing、renewals、expansion。
- depreciation growth and utilization。
- GCP vs Workspace vs TPU hardware/service mix。`OPEN`
- Cloud AI gross margin、customer concentration。`OPEN`
- large customer multi-cloud displacement。`OPEN/INFERENCE`

### 承保判断

Cloud 是最清晰的新护城河候选：需求、backlog、margin inflection 都是真证据。最大 blocker 是：backlog 能否在折旧、电力、硬件更新、融资成本后转成高 incremental ROIC。

---

## 8. TPU / Full-Stack Cost Advantage

### 机制

TPU/full-stack 逻辑：

```text
custom silicon + model architecture + compiler/runtime + network + data center + serving stack
-> lower cost per training/inference unit
-> 更低 AI response cost
-> Search / Gemini / Cloud AI 能以更好 margin 扩张
```

按 Greenwald，这是 production advantage / process power；按 7 Powers，是 process power + scale economies。

### 为什么能转化为超额利润

AI Search、Gemini、YouTube recommendation、Cloud AI、Workspace AI、agentic commerce 都需要 inference。如果 Google 每次 response 的成本下降快于 AI usage 增长：

- AI features 能防守/扩张 Search 而不永久压垮 margin。
- Cloud 能卖 AI infrastructure 且保持 attractive margin。
- Gemini subscriptions 不需要无限 compute subsidy。
- 自研 TPU 可部分绕开 Nvidia tax。

### 证据

- Google 官方称 Ironwood 是 seventh-generation TPU，purpose-built for inference，TPU 长期支持 Google training / serving workloads 和 Cloud customers。`A2`
- 管理层称 Gemini 3 升级后，AI Overviews / AI Mode 的 core AI responses cost 降低超过 30%。`A2`
- Q1 2026 release 称 first-party model APIs direct customer use 处理超过 16B tokens per minute，QoQ +60%。`A1/A2`
- June 2026 FWP 称 model APIs 处理 19B tokens per minute，monthly developers building with models 超过 8.5M。`A1`
- Cloud margin expansion 和 backlog 是间接正面信号。`A1`

### 未证明

- TPU cost per token vs Nvidia GPU alternatives。`OPEN`
- TPU 在 Alphabet internal AI workloads 中的占比。`OPEN`
- TPU manufacturing / HBM / foundry / packaging constraints。`OPEN`
- TPU Cloud gross margin by offering。`OPEN`
- 30% cost reduction 是否足以抵消 AI usage growth 和传统点击 cannibalization。`OPEN/INFERENCE`

### 攻击面

- **Nvidia ecosystem 追赶**：GPU hardware/software 迭代可能压缩 TPU 优势。
- **上游依赖**：TPU 设计自有，但制造、封装、HBM、networking、power 仍受外部约束。
- **开源小模型效率**：足够好的小模型可降低 hyperscale full-stack 优势。
- **利用率风险**：需求变化或硬件快速过时会让 capex 变低回报资产。
- **客户偏好**：企业可能偏好 Nvidia portability，而不是 TPU lock-in。

### 监控指标

- AI response cost / token cost / inference gross margin。`OPEN`
- TPU utilization、external customer adoption、backlog attach。`OPEN`
- capex 中 servers vs data centers/networking split。
- AI Search latency and serving cost。
- Nvidia GPU purchases vs TPU deployment。`OPEN`
- Cloud AI infrastructure margin vs core GCP margin。`OPEN`

### 承保判断

TPU/full-stack 是高潜力 process-power claim，但不是已验证的财务护城河。现在只能承保为“战略上关键、财务上待证”。

---

## 9. Gemini / AI Distribution

### 机制

Gemini 不是单个模型，而是可插入 Google 全部分发面的 AI layer：

- Search / AI Mode / AI Overviews。
- Android / Pixel / Chrome。
- Workspace。
- YouTube creator tools / ads tools。
- Google Cloud / Vertex / APIs。
- Maps / Gmail / Photos / commerce workflows。

许多 AI 模型公司有模型、缺分发；Google 的差异是模型、数据、分发、广告、Cloud、订阅、设备入口同时存在。

### 为什么能转化为超额利润

Gemini 只有在以下几类结果出现时才是护城河：

- 提高 Search query volume / commercial intent coverage。
- conversational / complex queries 的 RPM 不低于传统 Search。
- 提升 ads conversion 和 advertiser ROI。
- 带动 paid AI subscriptions。
- 加深 Workspace / Cloud switching costs。
- 降低内部运营成本，提高广告、creator、Cloud 效率。

否则 Gemini 只是防守旧产品所需的功能成本。

### 证据

- Q1 2026 release 称 consumer AI plans 为 strongest quarter ever，driven by Gemini App；Gemini Enterprise paid MAUs QoQ +40%。`A1`
- 管理层称 AI Mode / AI Overviews drive greater Search usage，包括 commercial queries。`A2`
- 管理层描述 Direct Offers in AI Mode、retailer ad formats、AI Mode / Gemini 中的 agentic checkout。`A2`
- 管理层称 Gemini 正部署到 ads infrastructure，超过 30% Search spend 使用 AI-enabled campaigns。`A2`
- FWP 称 monthly developers building with Google models 超过 8.5M，model API tokens 19B/min。`A1`

### 攻击面

- **Model parity**：GPT/Claude/open models 足够好后，模型本身很难单独成为 moat。
- **用户起点迁移**：用户可能直接从 ChatGPT/Claude/Perplexity/Apple assistant 开始任务。
- **Monetization gap**：AI experiences 可能广告密度更低、点击率更低、compute cost 更高。
- **监管延伸**：DOJ remedies 明确触及 Google Assistant 和 Gemini app 分发。
- **信任/错误成本**：商业、健康、金融、本地服务中的 hallucination 会损害采用或增加责任。

### 监控指标

- Gemini App MAU/DAU、retention、paid conversion、ARPU。`OPEN`
- AI Mode / AI Overviews penetration and query mix。
- AI Search RPM vs traditional Search RPM。`OPEN - blocking`
- commercial query conversion、agentic checkout volume。`OPEN`
- Workspace Gemini attach、Gemini Enterprise paid MAUs、churn。`OPEN`
- API token volume、developers、revenue per token。`OPEN`

### 承保判断

Gemini 是护城河迁移载体。它可能保住商业意图入口，但只有当 monetization 和 unit compute economics 被证明后，才是财务护城河。

---

## 10. Data Center / Power / Compute Bottleneck

### 机制

AI 把软件规模变成物理瓶颈：

```text
AI products -> accelerators / servers / networking / data centers / power / cooling / land / leases
```

关键区分：

- **Owned bottleneck**：Alphabet 拥有稀缺 capacity，并能以高 ROIC 变现。
- **External bottleneck**：Alphabet 只是向芯片、HBM、封装、电力、grid、土地、建设、lease 持有人付费。

瓶颈不等于护城河。只有“拥有 + 难复制 + 能高回报变现”才是护城河。

### 为什么可能转化为超额利润

如果 Alphabet 能更早、更便宜、更高效地拿到 capacity，并用 TPU/full-stack 降低 unit cost，同时 Cloud/AI/Search/Gemini 能付得起资本成本，它就能把基础设施变成收费公路。

### 为什么可能失败

如果所有大玩家都能用资本买类似 capacity，或者上游供应商拿走租，或者 utilization / 折旧 / 电力 / 融资成本吞掉收益，基础设施就从 moat 变成 capex sink。

### 证据

- FY2025 capex $91.4B，主要是 technical infrastructure。`A1`
- Q1 2026 capex $35.7B vs Q1 2025 $17.2B。`A1`
- Q1 2026 assets not yet in service $108.6B，主要是 technical infrastructure。`A1`
- Q1 2026 data-center lease payments not yet commenced $75.6B，commence 2026-2031。`A1`
- FY2025 purchase commitments $149.1B，其中 $113.0B short-term，主要 technical infrastructure / inventory orders。`A1`
- Alphabet pending acquisition of Intersect，data center and energy infrastructure solutions provider，$4.8B。`A1`
- FWP：2026 capex expected $180B-$190B，2027 expected significantly increase。`A1`
- FWP：$80B equity offerings；过去一年 debt raised over $85B，总 debt balance over $100B。`A1`
- 管理层称 compute constrained，Cloud revenue would have been higher if demand could be met。`A2`

### 攻击面

- **Power / grid**：并网、PPA、许可、能源 availability 可能是真正硬约束。`INFERENCE`
- **Supplier capture**：Nvidia、foundries、HBM、networking、switchgear、transformers、EPC 捕获租。
- **Depreciation wave**：资产入 service 前 margin 可能好看，折旧后来。
- **Financing dilution**：equity、mandatory converts、debt、buyback pause 把成本转给股东。
- **Local regulatory / environmental**：数据中心能耗、水耗、选址可能遇到阻力。
- **Obsolescence**：AI hardware useful life 可能短于会计寿命。`OPEN/INFERENCE`

### 监控指标

- capex / OCF、FCF / revenue、FCF/share。
- assets not yet in service、depreciation、useful-life assumptions。
- data-center leases、purchase commitments。
- power procurement、PPA commitments、MW capacity、grid interconnection timing。`OPEN`
- utilization、Cloud backlog conversion。
- debt、equity issuance、buyback resumption、share count。
- incremental Cloud / AI gross margin vs incremental capex。`OPEN`

### 承保判断

这是最重要瓶颈，但不能自动叫护城河。更准确的标签是：

```text
monetization side: possible moat
supply side: known cost sink
shareholder return bridge: unresolved
```

---

## 11. 护城河迁移地图

### 仍然成立的旧资产

- 用户习惯仍在。
- Search commercial intent 仍在变现。
- 广告主仍需要 measurable ROI。
- YouTube 仍聚合大量注意力。
- Android / Chrome 仍有分发权。
- Cloud 已经有真实 demand、backlog、profitability。

### 正在变化的价值捕获点

```text
旧：query -> links -> ads -> click -> merchant
新：task -> AI answer/agent -> recommendation -> offer/ad/subscription/API/checkout
```

迁移后的护城河变量：

- 从 CPC 到 AI answer monetization。
- 从结果页广告到 Direct Offers / agentic checkout。
- 从 browser default 到 assistant default。
- 从文本 query data 到 multimodal/contextual data。
- 从轻资本软件经济到重 compute 经济。

### Search box vs commercial intent

Search box 是旧表现形式；commercial intent 是真实利润源。Q1 2026 Search +19% 说明旧形式尚未破裂，但 DOJ remedies 与 AI agent 同时说明入口形态不稳定。Google 正通过 AI Mode、Gemini、Android、Chrome、UCP/agentic commerce 把新入口拉回自家系统。

### AI capex 分层裁决

| capex 结果 | 标签 | 需要证据 |
|---|---|---|
| AI response cost 下降快于 AI usage 增长 | 新成本护城河 | cost/token、cost/query、margin proof |
| Cloud 客户高 margin 锁定 | 新 switching-cost moat | backlog conversion、renewal、Cloud margin |
| Search query 和 monetization 被 AI 扩大 | moat migration | AI Search RPM、commercial query proof |
| 只是防止用户离开 Search / Gemini | defensive tax | revenue holds but FCF/share deteriorates |
| 上游供应商拿租、utilization 滞后 | capex trap | capex up、depreciation up、FCF/share down |

当前证据支持“可能形成新护城河”，但没有排除“防守税”。

---

## 12. 证伪清单

护城河弱于预期，如果出现：

- Search & other 连续两季低于 high single digit while AI usage rising。
- paid clicks 转负，CPC 无法弥补。
- AI Search RPM 明显低于传统 Search。`OPEN`
- TAC rate 明显上升，默认分发成本恶化。
- Network decline 扩散到 Search / YouTube 自有面。
- adtech structural remedies 实质削弱 auction efficiency / data advantage。
- Cloud margin 在折旧到来后显著回落。
- Cloud backlog 转化慢或 margin 低。
- capex / OCF 长期 >70% 且无 ROI 证据。
- FCF/share 多年下降，尽管 revenue / operating income 增长。
- equity issuance / mandatory converts / buyback pause 造成持续稀释。
- Gemini 分发增长但 monetization 主要是低 ARPU subscription + 高 compute cost。
- TPU 成本优势长期无法量化，同时 Nvidia/GPU spending 仍高。

护城河强于预期，如果出现：

- AI Mode / AI Overviews penetration 上升时 Search & other 仍保持 double-digit growth。
- AI Search monetization 接近或高于传统 Search。
- Cloud margin 经历折旧周期后仍保持 25%-30%+。
- capex intensity 见顶，FCF/share 重新增长。
- TPU / AI Hypercomputer 获得外部高 margin workload。
- Gemini 成为默认 assistant/workflow，且 paid conversion / ads monetization 可见。
- DOJ / EC remedies 停留在行为性限制，没有结构性破坏 Search 或 adtech economics。

---

## 13. 主要来源 URL

一手 / 官方来源：

- Alphabet FY2025 Form 10-K: https://www.sec.gov/Archives/edgar/data/1652044/000165204426000018/goog-20251231.htm
- Alphabet Q1 2026 Form 10-Q: https://www.sec.gov/Archives/edgar/data/1652044/000165204426000048/goog-20260331.htm
- Alphabet Q1 2026 earnings release: https://s206.q4cdn.com/479360582/files/doc_financials/2026/q1/2026q1-alphabet-earnings-release.pdf
- Alphabet Q1 2026 earnings call transcript: https://abc.xyz/investor/events/event-details/2026/2026-Q1-Earnings-Call-2026-nW8kCrBAKS/default.aspx
- Alphabet June 2026 FWP: https://www.sec.gov/Archives/edgar/data/1652044/000119312526251733/d160205dfwp.htm
- Alphabet June 2026 424B5: https://www.sec.gov/Archives/edgar/data/1652044/000119312526257690/d159942d424b5.htm
- DOJ Search remedies press release: https://www.justice.gov/opa/pr/department-justice-wins-significant-remedies-against-google
- DOJ U.S. and Plaintiff States v. Google LLC case page: https://www.justice.gov/atr/case/us-and-plaintiff-states-v-google-llc
- Google Ironwood TPU official blog: https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/ironwood-tpu-age-of-inference/
- Google Cloud AI infrastructure at Next '26: https://cloud.google.com/blog/products/compute/ai-infrastructure-at-next26
- EC AT.40670 Google Adtech case page: https://competition-cases.ec.europa.eu/cases/AT.40670

本地来源：

- `companies/googl/raw/p0_sec_extracts_v2.md`
- `companies/googl/raw/q1_2026_call_ai_search.md`
- `companies/googl/completion_checker_v2.md`
- `companies/googl/moat_map.md`
- `companies/googl/bottleneck_map.md`
- `companies/googl/value_chain_map.md`
- `companies/googl/memo-v2.md`

---

## 14. 仍未解决 Blockers

Blocking：

- `OPEN`: AI Overviews / AI Mode RPM vs traditional Search RPM。
- `OPEN`: capex maintenance vs growth split。
- `OPEN`: 2026-2027 AI capex 的 incremental ROIC，需扣除 depreciation、utilization、power、leases、SBC、debt、dilution。
- `OPEN`: Cloud backlog margin、cancellation risk、customer concentration、TPU hardware/service mix。
- `OPEN`: TPU unit cost / performance / utilization vs Nvidia GPU alternatives。
- `OPEN`: Gemini App / AI Mode retention、paid conversion、ARPU、ad load、commerce conversion。
- `OPEN`: power capacity、data-center MW、PPA economics、grid interconnection timing、local regulatory constraints。

Monitoring but not blocking alone：

- DOJ / EC remedies final implementation and appeals。
- YouTube Shorts and subscription economics。
- Android / Play remedy economics。
- Network revenue decline 是否继续限于第三方 open-web 面。

---

## 15. 改动文件

- `companies/googl/moat_bottleneck_v2.md`

