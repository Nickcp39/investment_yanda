# 2026 Q1 Hyperscaler 财报 Check — AI Capex 周期是否进入消化期

## Snapshot

- Topic: FAANG + MSFT 最新季报数据，回答"主导叙事是否从增长切到消化"
- Region: US mega-cap tech
- Time horizon: Q1 2026 (calendar) actuals + 2026 全年 guidance
- Last updated: 2026-05-06
- 上下文链接: 接续上一轮关于 AI 循环融资 (NVDA→OAI, AMD warrant, Oracle $300B 合同) 的判断

## Research Question

上一轮给出了三个观察指标，本次要回答其中之一：
> "超大规模厂商 capex/FCF：MSFT/GOOGL/META 财报，capex 增速开始压 FCF 增速 = 资本市场会开始重新定价"

具体子问题：
1. Q1 2026 capex 实际数 vs 2025 同期增速？
2. 2026 全年 capex guidance 有没有上修 / 维持 / 下修？管理层口风变化？
3. FCF 是否开始被 capex 拖累（绝对额、增速、margin）？
4. AI 相关收入披露口径有没有变（更具体？更含糊？）？
5. 任何关于 vendor financing / 客户预付款 / OpenAI 之类对手方的提及？

## 范围 (用户 2026-05-06 确认：聚焦传统互联网公司)

用户指令: "主要是传统互联网公司，而不是 AI 公司" — 切换视角：
不是看 AI 阵营 (NVDA/MSFT-OAI 绑定) 投了多少，
而是看广告/零售/消费这些"产生现金的传统业务"被 AI capex 吃掉多少 FCF。
**这个视角更早、更准** — 现金端最先承压。

| 优先级 | 公司 | 业务底色 | 为什么重要 |
|---|---|---|---|
| 必须 | META | 广告 100% | capex 增速最猛，纯 inhouse AI，广告 FCF 被吃多少 |
| 必须 | GOOGL | 搜索广告 + Cloud | 搜索广告 cash cow + TPU 自研 capex 双线 |
| 必须 | AMZN | 零售 + AWS | AWS 是输出端 (受益), 但 AMZN 本身也在投 AI capex |
| 简版 | AAPL | 硬件 + 服务 | 对照组：相对独立，capex 不大，看现金返还节奏 |
| 简版 | NFLX | 流媒体 | 对照组：基本无 AI capex 暴露，看 FCF margin |
| 跳过 | MSFT | Azure + OAI | 用户明示去掉，深度 AI 阵营绑定 |

## 每家公司收集字段

- Q1 2026 capex 实际数 (绝对额 + YoY)
- Q1 2026 OCF 和 FCF (绝对额 + YoY)
- capex / OCF 比率
- 2026 全年 capex guidance (vs 上次 guidance)
- 业绩电话会上 AI 相关原话（管理层 tone）
- 任何关于客户集中度、预付款、vendor financing 的披露

## 执行计划

| Block | 内容 | 来源优先级 | 状态 |
|---|---|---|---|
| 1 | META Q1 2026 — IR press release + 关键 quote | IR primary > 路透/CNBC | **done** ✅ |
| 2 | GOOGL Q1 2026 — 同上 | 同 | **done** ✅ |
| 3 | AMZN Q1 2026 — 同上 | 同 | **done** ✅ |
| 4 | AAPL FQ2 2026 (calendar Q1 2026) — 简版 | 同 | **done** ✅ |
| 5 | NFLX Q1 2026 — 简版 (对照组) | 同 | **done** ✅ |
| 6 | 汇总表 + 段永平 lens 收口：传统互联网现金 vs AI capex | n/a | **done** ✅ |

每个 block 用 1-2 个 fetch 拿到一手数据 (IR press release > 10-Q)，secondary 只用来补管理层电话会 quote。

## 数据汇总 (Q1 2026, calendar)

| 公司 | Q1 营收 (YoY) | Q1 Capex | Q1 FCF | 2026 Capex Guide | 回购/分红信号 | 灯号 |
|---|---|---|---|---|---|---|
| META | $56.3B (+33%) | $19.84B | $12.4B | **$125–145B (上修 +$10B)** | **回购 = $0** | 🔴 |
| GOOGL | $109.9B (+22%) | $35.7B | TTM $64.4B | **$180–190B (上修 +$5B)** + 2027 "significantly increase" | n/a | 🔴 |
| AMZN | $181.5B (+17%) | $44.2B (P&E) | **TTM $1.2B (-95%!)** | $200B (Feb guide) | n/a | ⚫ (黑灯) |
| AAPL | $111.2B (+17%) | H1 $4.3B | OCF $28B+ | (未单独 guide, 历来低) | **新增 $100B 回购** + 加股息 | 🟢 |
| NFLX | $12.25B (+16%) | (内容投入,非 AI) | $5.09B (含一次性) | FCF $12.5B 全年 | (无 AI capex 暴露) | 🟢 |

### 三个 hyperscaler 关键算式

- **META**: capex 同比 +44% ($13.7B→$19.84B), OCF 同比 +34% ($24.0B→$32.2B) — capex 增速首次超过 OCF。FCF 增速 (+20%) 远低于营收增速 (+33%)，**剪刀差已经打开**。
- **GOOGL**: Q1 capex $35.7B vs TTM FCF $64.4B = **单季 capex ≈ TTM FCF 的 55%**。年化 capex $185B (中位) > 任何合理 FCF 预测。
- **AMZN**: TTM FCF $1.2B 是字面意义的"接近零"。$181.5B 收入规模的公司，FCF 几乎全数被资本支出吞噬。Anthropic 持仓的 mark-to-market 收益 $16.8B 让 GAAP 净利润好看，但**与现金流无关**。

## Core View

### Base Case (50%)
**叙事还在"增长"段，但"切换前的资产负债表姿势"已经全部摆好。**
- 三家广告/电商巨头都上修了 2026 capex guide，没有一家踩刹车
- 但同时：META 停了回购、AMZN FCF 塌 95%、GOOGL CFO 明说 2027 还要再加
- 这意味着资本市场目前还在"接受" — 因为收入增速也在加速 (META 33% 是 2021 来最快, AWS 28% 是 15 季度新高, GOOGL Cloud backlog 翻倍到 $462B)
- 收入端的加速暂时为 capex 加速买了 alibi
- 切换点不需要等"顶"，只需要其中**任何一家**出现一个季度收入增速回落 + capex 维持现行 guide。那一天，叙事就从"增长正反馈"切到"消化"。

### Upside Risk (重新评估的情况)
- AI 真的进入"杀手级 enterprise 应用爆发"阶段 (~$200B/年 capex 直接对应 enterprise SaaS 升级周期), 收入端跟得上
- GOOGL Cloud backlog $462B 是真信号 — 如果未来 24 个月一半转化率成立 ($230B 收入兑现), 那 capex 是合理的
- AMZN 通过 Anthropic + 自研 Trainium 占据"非 NVDA"算力位

### Downside Risk
- AMZN FCF 已经在 $1.2B 这个危险水位 — 任何 AWS 增速回落 (从 +28% 滑回 +20%) + capex 维持，FCF 就是负的
- META capex 上修是因为"组件涨价"(管理层原话) — 这是 NVDA pricing power 的传导，意味着**capex 通胀** + meta inhouse AI 还没产生显著商业化收入
- GOOGL TPU "sales to select customers" 是新动向 — 谁在买？如果是 OAI、Anthropic 这种生态对手方，那就是循环融资的另一面 (上轮我们讨论过的 NVDA→OAI 模式的镜像)
- 三家 hyperscaler capex 集中度都在升 — 部分对应 NVDA、部分对应自研 ASIC，但供应商集中度本身就是上轮指标 #2

### What Would Change My Mind (即"切换信号" — 比"找顶"早)
| 信号 | 重要度 |
|---|---|
| 任何 hyperscaler 单季营收增速回落 ≥3pp + capex 维持上修 guide | ⭐⭐⭐ 最早 |
| META 重启回购 (= 现金压力小于预期) → 反向利好 | ⭐⭐ |
| AWS 增速跌回 25% 以下 + AMZN FCF 转负 | ⭐⭐⭐ |
| 财报会议出现 "absorb" / "digest" / "moderate" / "pull-in" 这些词 | ⭐⭐⭐ |
| OpenAI 下一轮估值持平或回撤 (上轮指标 #1) | ⭐⭐ |
| 一家 hyperscaler 把 capex guide 下修 (即使只是 top-end) | ⭐⭐⭐ 决定性 |

## 段永平 lens 收口

> "投资就是看公司值不值。值，就是公司创造现金流的能力。"

- **AAPL 是唯一在做股东价值的 hyperscaler.** $100B 回购 + 加息，capex 极少，AI 外包。这是经典的"产生现金 → 还给股东"。值不值另说，但行为正确。
- **NFLX 也是清醒的.** 内容投入是 amortized 的"capex"，FCF 实打实在产生 ($12.5B 全年 guide)，与 AI 周期解耦。
- **META、GOOGL、AMZN 三家都在做"把现金流 forward 折现去赌 AI"的事.** 区别只是程度：
  - AMZN 已经把 FCF 烧光 (TTM $1.2B)
  - META 停了回购 (现金重新定向)
  - GOOGL 还有 TTM FCF $64.4B 缓冲，但 2027 还要再加
- 段永平最警惕的不是"capex 大"，而是 **"capex 大到必须靠融资或停止股东返还"**。这三家已经过了这条线。
- 但段永平也不会去做空 — 因为 narrative 切换的时点不可预测，**且收入端加速暂时为 capex 加速买单**。
- **正确动作是观察，不是行动**：
  - **不在这三家加仓** (估值已经隐含 capex 兑现 → 任何低于 expectation 的兑现都是负 alpha)
  - **AAPL/NFLX 的资产配置吸引力相对上升** (cash return 的稀缺性变高)
  - 持有现有仓位 (如果有) 但**把 sell 触发线设在 "信号表" 中任意一项触发**
  - 避免把 NVDA/AMD 看作"安全的 picks-and-shovels" — 他们的客户 (这三家 hyperscaler) 现在也在借钱给他们花钱

## Indicators (实时跟踪)

| Indicator | Current Reading (2026-05-06) | Direction | Why It Matters | Source |
| --- | --- | --- | --- | --- |
| META 2026 capex guidance | $125-145B | ↑ 上修 +$10B | capex 仍在加速 | IR 2026-04-29 |
| GOOGL 2026 capex guidance | $180-190B | ↑ 上修 +$5B | 同上 + 2027 还要加 | IR 2026-04-29 |
| AMZN 2026 capex guide | $200B | ↑ 大幅 | FCF 已被吃光 | Q4'25 + Q1'26 |
| AMZN TTM FCF | **$1.2B (-95% YoY)** | ↓↓↓ | 现金创造能力实质性恶化 | Q1'26 |
| META Q1 buybacks | **$0** | ↓↓ | 历史首次同期为 0 | Q1'26 |
| AAPL 新增回购授权 | **$100B** | → | 对照组：现金返还稀缺性 | Q2 FY26 |
| 管理层 tone 关键词 | "milestone", "unprecedented demand" | → 仍在 "增长" 段 | 没看到任何 "absorb"/"digest" | 财报会议 |

## Sources

- META Q1 2026: [IR press release](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-First-Quarter-2026-Results/default.aspx) (2026-04-29) · [CNBC summary](https://www.cnbc.com/2026/04/29/meta-q1-earnings-report-2026.html) · [Fortune 145B capex](https://fortune.com/2026/04/29/meta-zuckerberg-145-billion-ai-spending-roi/)
- GOOGL Q1 2026: [Alphabet IR](https://abc.xyz/investor/news/news-details/2026/Alphabet-Announces-First-Quarter-2026-Results-2026-X-ge4Dm6bf/default.aspx) (2026-04-29) · [BigGo finance summary](https://finance.biggo.com/news/US_GOOGL_2026-04-29) · [SEC 8-K exhibit](https://www.sec.gov/Archives/edgar/data/1652044/000165204426000043/googexhibit991q12026.htm)
- AMZN Q1 2026: [Amazon IR](https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-First-Quarter-Results/) · [TNW FCF -95%](https://thenextweb.com/news/amazon-q1-2026-anthropic-aws-earnings) · [Investing.com slides](https://www.investing.com/news/company-news/amazon-q1-2026-slides-aws-surges-28-record-margins-offset-by-capex-93CH-4647447)
- AAPL Q2 FY2026: [Apple Newsroom](https://www.apple.com/newsroom/2026/04/apple-reports-second-quarter-results/) (2026-04-30) · [MacRumors summary](https://www.macrumors.com/2026/04/30/apple-2q-2026-earnings/) · [IndexBox $100B buyback](https://www.indexbox.io/blog/apple-q2-2026-earnings-eps-beats-estimates-iphone-revenue-misses-amid-buyback-news/)
- NFLX Q1 2026: [Netflix shareholder letter PDF](https://ir.netflix.net/files/doc_financials/2026/q1/FINAL-Q1-26-Shareholder-Letter.pdf) (2026-04-16) · [Variety summary](https://variety.com/2026/tv/news/netflix-earnings-q1-2026-1236723851/)
