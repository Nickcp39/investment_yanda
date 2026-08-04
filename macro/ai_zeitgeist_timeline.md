# AI 思潮时间轴 — 市场每个季度在担心什么

## Snapshot

- Topic: 2024Q3 → 2026Q3 共 9 个季度，AI 叙事（市场共识关注点）的逐季迁移，以及下一步的推演
- Region: US mega-cap tech + 半导体 + 软件
- Method: 以"市场当季**争论的焦点问题**"为切片，而不是以股价涨跌为切片
- Last updated: 2026-08-03
- 上下文链接: 接续 `macro/2026Q1_hyperscaler_capex_check.md`（该文的"切换信号"表在本文 §4 被部分证伪/修正）
- 姊妹方法论: `studies/jp_cn_relative_timeline/zeitgeist_healthcare.md`（同样的"思潮相对时间轴"手法）

---

## 0. 一句话结论

**每一轮质疑都比上一轮往资产负债表更深处走一层**：从"收入在哪"（损益表右边）→"技术还行不行"（产品）→"谁给客户出钱"（交易对手）→"折旧怎么算"（会计）→"谁被 AI 吃掉"（需求端重定价）→"算力卖给谁、卖多少钱"（供需与定价权）。

2026 年 7 月的财报季是一个**结构性断点**：四家 hyperscaler 全部上修 capex，但市场第一次**分裂定价**（MSFT/AMZN 大涨，META/GOOGL 大跌）。这意味着 "AI capex" 作为一个**单一交易**已经死了。

---

## 1. 逐季思潮切片

| 季度 | 市场在问的问题 | 触发事件 | 思潮关键词 |
|---|---|---|---|
| **2024 Q3** | 钱花出去了，**收入在哪**？ | Sequoia《AI's $600B Question》、Goldman《Gen AI: too much spend, too little benefit》（均 6 月）；8 月初日元套息平仓引发全球抛售 | **第一次质疑，但被无视** |
| **2024 Q4** | **预训练撞墙了吗**？ | 11 月多家报道下一代模型（Orion 等）进展放缓；OpenAI o1 / test-time compute 登场 | **换一条 scaling 曲线继续信** |
| **2025 Q1** | 是不是**根本不需要这么多算力**？ | 1/27 DeepSeek R1 → NVDA 单日 -17%、蒸发约 $6000 亿；同期 Stargate $5000 亿宣布；2 月 TD Cowen 报 MSFT 取消数据中心租约 | **效率恐慌**；黄仁勋以"三条 scaling law"（预训练/后训练/推理时）把叙事扳回 |
| **2025 Q2** | AI 扛不扛得住**宏观冲击**？ | 4/2 对等关税 → 宏观短暂盖过 AI；随后 hyperscaler 财报全部重申/上修 capex | **AI 被证明"政策免疫"**，capex 信仰反而加强 |
| **2025 Q3** | **谁在给买家出钱**？ | 9 月 Oracle-OpenAI $3000 亿合同、NVDA 向 OpenAI 投最高 $1000 亿；8 月 MIT NANDA "95% 企业 AI 试点无可衡量 ROI"；Altman 本人说"泡沫" | **循环融资 / round-tripping 元年**——第一次是结构性质疑而非估值质疑 |
| **2025 Q4** | **利润是不是会计做出来的**？ | 11/11 Burry 指控 hyperscaler 延长 GPU 折旧年限虚增利润（2026-28 少计约 $1760 亿）；11/25 NVDA 罕见发内部备忘录点名反驳；Oracle $380 亿发债；Meta 表外 SPV 融资；11 月 Gemini 3 用 TPU 训成、超过 GPT-5 | **下沉到会计与资产负债表**；同时 **TPU/ASIC 叙事崛起，NVDA 独占性首次被真实挑战** |
| **2026 Q1** | **谁会被 AI 吃掉**？ | 1/29-30 Anthropic 发布 Claude Cowork → 记者用 $5-15 一小时复刻 Monday.com；48 小时内软件板块蒸发 $2850 亿，1/29 是自 2020 年 3 月以来软件最差单日；MSFT 单日蒸发约 $3600 亿、年内一度接近 -40% 回撤 | **SaaSpocalypse**——AI 第一次被定价为"破坏者"而不只是"受益者" |
| **2026 Q2** | 谁卖**铲子的铲子**？ | 存储超级周期（MU FQ2 收入 +57%；Seagate/WDC/SanDisk 翻倍级涨幅）；光通信/光电轮动；机器人与"物理 AI"；SOX 12 个月 +130%，6/22 创历史新高约 14,655 | **叙事从"谁做模型"转向内存/光模块/电力/机器人**；ROI 拷问同时开始成型 |
| **2026 Q3** | 算力**还稀缺吗**？值多少钱？ | 6/3 AVGO Q3 AI 指引 $160 亿 < 预期 $172 亿，股价 -12~13%；7/1 Meta Compute 宣布卖闲置算力，META +8.8% 而 **MU -10.6%、AMD -6.9%**；7 月初 SOX 单日 -7%；开源权重模型把等能力推理成本两年压掉约 95% | **稀缺性叙事被解构**；"AI with receipts"（要收据）成为主流语言 |

---

## 2. 2026 年 7 月财报季 — 分裂定价

| 公司 | 2026 capex guide | 动作 | 市场反应 |
|---|---|---|---|
| MSFT | FY27 $2550–2600 亿（vs CY26 $1900 亿，+35%） | 上修 | **+8~9%** |
| AMZN | ~$2200 亿 | 上修 | **+8~10%**（盘后） |
| GOOGL | $1950–2050 亿 | 上修 | **-5%** |
| META | $1300–1450 亿（抬高下限） | 上修 | **-9~10%**（盘后） |

**四家做的事一样，市场给的分完全相反。** 分野不在花多少，而在**能不能把 capex 挂钩到已确认的需求**：
- MSFT：Azure +43%（超 39-40% 指引）、年化破 $1000 亿、backlog $678 亿→$6780 亿量级
- AMZN：AWS 加速
- META：纯 inhouse 投入，没有外部收入对应（Meta Compute 就是对这个批评的回应）
- GOOGL：capex 上修 + 2027 还要再加，但云收入兑现节奏没跟上预期

四家在电话会上给出了**同一套辩护话术**：先承诺长周期资产（土地、厂房、电力），短周期资产（芯片）**推迟到看得见需求前几个月才下单**。这套话术本身就是思潮转变的产物——它是说给"要收据"的市场听的。

---

## 3. Core View — 下一步市场会想什么

### Base Case（55%）：**算力商品化 + 折旧墙合流 → AI 基建从成长股估值切到周期股估值**

两件事在 2026H2–2027 会撞在一起：

1. **折旧墙落地。** 2026 年四大 hyperscaler capex 约 $7250 亿（同比 +77%）。按 5–6 年直线折旧，从 2027 年起每年新增约 $1200–1450 亿折旧费用进损益表。而"季度 AI 收入 > 季度折旧"这条最基本的线，行业**是在 2025 Q4 才刚刚跨过的**——跨过的时候，2026 年这波 capex 还没进折旧表。所以 2027 年的 EPS 会被折旧实打实地压。Burry 那笔账（$1760 亿）当时被当成空头言论，2027 年会变成卖方模型里的标准科目。

2. **算力从稀缺品变成商品。** Meta Compute、xAI 卖算力、neocloud 产能过剩——**供给侧开始出现愿意卖闲置产能的人**。一旦算力有了公开的现货价格曲线，"稀缺溢价"就没有了，整条产业链的估值框架从 DCF-成长切到周期股（看价格、看库存、看产能利用率）。

**这个转变的 tell 已经出现了**：7/1 Meta 宣布卖算力，**META 涨 8.8%，而 Micron 跌 10.6%、AMD 跌 6.9%**。市场已经开始用周期股的方式反应了——增加供给 = 利好卖服务的、利空卖设备的。这是标准的商品逻辑，不是成长股逻辑。

历史镜像是 **1999-2001 的宽带/暗光纤**：需求预测没错（互联网流量确实涨了），但产能建太快、单位价格塌了，赚钱的从铺光纤的转移到用光纤的。

### 次要线索（各 10-15%，可能与 Base Case 并行）

- **信用事件。** 五大云厂商债务融资从 2022 年的约 $400–500 亿升到 2026 年的约 $1900 亿；2026 年前三个半月发债已超 2025 全年。下一个焦点是 AI 相关信用利差、SPV/表外结构、neocloud 的偿付能力。**第一个真实违约会一次性重定价所有东西**——这是尾部但破坏力最大。
- **"谁被吃掉"的第二波。** SaaSpocalypse 是第一波（per-seat 授权模式）。第二波候选：BPO/外包、广告代理、初级法务、初级咨询、客服。逻辑一样——AI agent 直接替代按人头计价的服务。
- **电力/物理约束替代芯片约束。** 芯片能买到之后，变电站、并网排队、水、变压器成为真瓶颈。这条对 CEG 这类标的是直接的（但注意：repo 里 CEG 的卡片已指出旗舰产能被微软锁死，涨的是行业不是它）。
- **计价模式从"卖席位/卖token"转向"卖结果"（outcome-based）。** 谁先跑通，谁就摆脱了被 agent 打掉的宿命。

### What Would Change My Mind

| 信号 | 方向 | 重要度 |
|---|---|---|
| 出现公开、可交易的算力现货价格指数 | 确认商品化 | ⭐⭐⭐ |
| 任一 hyperscaler 缩短 GPU 折旧年限（主动认账） | 确认折旧墙，短期利空长期利好 | ⭐⭐⭐ |
| 任一 hyperscaler **下修** capex guide（哪怕只是上限） | 确认周期转向 | ⭐⭐⭐ |
| AI 相关高收益债利差走阔 >150bp | 信用线索启动 | ⭐⭐⭐ |
| Meta 重启回购 / AMZN FCF 回正 | **证伪**——现金压力小于预期 | ⭐⭐ |
| 企业 AI 支出从"试点预算"转为"替代人力的经常性预算"科目 | **证伪**——需求端真实兑现，capex 合理 | ⭐⭐⭐ |
| 推理 token 总量维持年 2× 增长四年（学术界给的偿付corridor下限） | **证伪**——建多少用多少 | ⭐⭐ |

---

## 4. 对 `2026Q1_hyperscaler_capex_check.md` 的修正

原文（2026-05-06）给的切换信号是：

> "任何 hyperscaler 单季营收增速回落 ≥3pp + capex 维持上修 guide → 叙事从增长切到消化"

**7 月财报的实际结果比这个更细，需要修正**：切换不是整体性的，而是**分化式**的。四家全部上修 capex、且收入端都没有明显回落，但市场仍然把 META 和 GOOGL 砍了。所以真正的切换信号不是"增速回落"，而是：

> **"capex 能否挂钩到已披露的、外部客户付费的需求"** —— 挂得上的（MSFT/AMZN）继续给成长估值，挂不上的（META inhouse、GOOGL 云兑现慢）开始被要求折价。

原文那张"信号表"里"财报会议出现 absorb/digest/moderate 这些词"这一条**仍然有效且尚未触发**——四家的话术依然是增长语言，只是加了一层"短周期资产延后下单"的风险管理修辞。这层修辞本身值得作为新指标跟踪。

---

## 5. Indicators（实时跟踪）

| Indicator | Current Reading (2026-08-03) | Direction | Why It Matters |
|---|---|---|---|
| 四大 hyperscaler 2026 capex 合计 | ~$7250 亿（YoY +77%） | ↑ 仍在上修 | 折旧墙的分子 |
| 五大云厂商债务融资余额 | ~$1900 亿（2022 年约 $400-500 亿） | ↑↑ | 信用线索 |
| 季度 AI 收入 vs 季度折旧 | 2025Q4 首次转正 | 边际 | 最基本的偿付线 |
| 等能力推理成本 | 两年 -95%（$30/Mtok → <$0.5/Mtok） | ↓↓↓ | 商品化速度 |
| SOX 指数 | 6/22 历史高点约 14,655 后回落，7 月初单日 -7% | ↓ | 稀缺溢价消退 |
| 卖闲置算力的玩家数 | Meta、xAI（2 家，从 0 起） | ↑ | **商品化最直接的先行指标** |
| 管理层话术 | "增长" + "短周期资产延后下单" | → 未见 absorb/digest | 切换前的最后一层修辞 |
| AAPL/NFLX 相对吸引力 | 现金返还稀缺性仍在上升 | ↑ | 对照组 |

---

## 6. Sources

**2026 Q3（最新）**
- [Meta pops 9% as company makes cloud push to sell excess AI compute — CNBC (2026-07-01)](https://www.cnbc.com/2026/07/01/meta-stock-cloud-ai-compute.html)
- [Meta, like SpaceX, looks to turn excess AI compute into cash — TechCrunch (2026-07-01)](https://techcrunch.com/2026/07/01/meta-like-spacex-looks-to-turn-excess-ai-compute-into-cash/)
- [Broadcom Q3 AI chip revenue guidance misses expectations, shares fall 13% — KuCoin](https://www.kucoin.com/news/flash/broadcom-q3-ai-chip-revenue-guidance-misses-expectations-by-12b-shares-drop-13)
- [Big Tech Earnings Scorecard July 31 2026 — TradingKey](https://www.tradingkey.com/analysis/stocks/us-stocks/262067315-big-tech-earnings-scorecard-microsoft-amazon-apple-july-31-2026-tradingkey)
- [The AI Capex Warning: Alphabet Sets a Tense Stage — Wall Street Horizon](https://www.wallstreethorizon.com/blog/the-ai-capex-warning)
- [Microsoft Q4 FY2026 earnings — CNBC (2026-07-29)](https://www.cnbc.com/2026/07/29/microsoft-msft-q4-earnings-report-2026.html)
- [Open Weight Models Are Turning Inference Into A Control Point — Forbes (2026-07-18)](https://www.forbes.com/sites/janakirammsv/2026/07/18/open-weight-models-are-turning-inference-into-a-control-point/)
- [Memory Scarcity, Open Models, and the Restructuring of the AI Industry 2026-2030 — arXiv](https://arxiv.org/html/2607.07207)
- [AI Inference Cost Reduction 2026: Down 95% in Two Years](https://valueaddvc.com/blog/how-ai-inference-costs-have-dropped-95-in-two-years-and-what-happens-next)

**2026 Q1-Q2**
- [SaaSpocalypse Now: AI Is Disrupting SaaS — Forbes (2026-02-06)](https://www.forbes.com/sites/petercohan/2026/02/06/saaspocalypse-now-ai-is-disrupting-saas---but-not-all-software-is-doomed/)
- [SaaSpocalypse 2026: Why AI Just Wiped $285B from Software Stocks — NxCode](https://www.nxcode.io/resources/news/saaspocalypse-2026-software-stock-crash)
- [The "AI with Receipts" Era: 2026 as the Year of Financial Accountability (2026-01-13)](https://markets.financialcontent.com/stocks/article/marketminute-2026-1-13-the-ai-with-receipts-era-why-2026-is-the-year-of-financial-accountability-for-tech-giants)
- [Hyperscaler AI Capex 2026: D&A Lag, Debt Wave — Silicon Analysts](https://siliconanalysts.com/analysis/hyperscaler-ai-capex-depreciation-wall-2026)
- [Hyperscalers Tap External Financing as AI Capex Outruns Cash Flow — FactSet](https://insight.factset.com/hyperscalers-tap-external-financing-as-ai-capex-outruns-cash-flow)
- [AI capex cycle: war-proof for now — Allianz (2026-03-25)](https://www.allianz.com/content/dam/onemarketing/azcom/Allianz_com/economic-research/publications/specials/en/2026/march/2026_03_25_AI.pdf)

**2025**
- ['Big Short' investor Michael Burry accuses AI hyperscalers of artificially boosting earnings — CNBC (2025-11-11)](https://www.cnbc.com/2025/11/11/big-short-investor-michael-burry-accuses-ai-hyperscalers-of-artificially-boosting-earnings.html)
- [Nvidia name-checks Michael Burry in secret memo pushing back on AI bubble allegations — CNBC (2025-11-25)](https://www.cnbc.com/2025/11/25/nvidia-pushes-back-on-charges-that-ai-investment-is-a-bubble.html)
- [How long before a GPU depreciates? — CNBC (2025-11-14)](https://www.cnbc.com/2025/11/14/ai-gpu-depreciation-coreweave-nvidia-michael-burry.html)
- [Gemini 3 gives Google a boost in the AI race against OpenAI and Nvidia — CNN (2025-11-29)](https://www.cnn.com/2025/11/29/tech/ai-chips-google-gemini-3-tpu-nvidia)
- [Nvidia, OpenAI, and the trillion-dollar loop — The Register (2025-11-04)](https://www.theregister.com/2025/11/04/the_circular_economy_of_ai/)
- [MIT: 95% of enterprise AI pilots fail to deliver measurable ROI — Healthcare IT News](https://www.healthcareitnews.com/news/mit-95-enterprise-ai-pilots-fail-deliver-measurable-roi)
- [Nvidia drops nearly 17% as DeepSeek sparks global tech sell-off — CNBC (2025-01-27)](https://www.cnbc.com/2025/01/27/nvidia-falls-10percent-in-premarket-trading-as-chinas-deepseek-triggers-global-tech-sell-off.html)

**2024**
- [AI's $600 Billion Question: The Growing Gap Between Investment and Revenue — Marketing AI Institute](https://www.marketingaiinstitute.com/blog/ai-economic-impact)

**Repo 内部源**
- `macro/2026Q1_hyperscaler_capex_check.md`（2026-05-06，一手 IR 数据）
- `macro/2026Q2_memory_supercycle_research.md`
- `sources/videos/`（2024-01 → 2026-07 中文美股博主逐字稿，连续情绪切片）
