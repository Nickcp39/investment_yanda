# GPU 云行业经济学与同业定价 — NBIS 研究 (track: industry & peers)

as_of 2026-10-23（行情取 2026-10-22 收盘）。标签：**P** = PRIMARY（公司文件/官网/交易所行情），**S** = SECONDARY（媒体、研究、指数商博客、聚合站）。带 "≈" 或"推算"的是本文算术，算式写在旁边。

## 0. 摘要

- **价格端的利润池没塌，在涨。** H100 租价 2025-09 见底（SDH100RT 约 2.13），2026-10-22 为 **$2.88/GPU-hr**（7 日 +10.3%），≈+35%。B200 指数 YTD +27.6%（S）。这一轮抛售**不是**现货租价下跌引起的。
- **Nebius 10-01 涨价有一手证据**：nebius.com/prices 的 Wayback 存档（P）显示 10-01 新增 "Effective October 1, 2026" 一列，H100 $3.85→$4.50（+16.9%），B300 $7.85→$9.50（+21.0%），现在页面只显示新价。这是第二次涨价，05-07 到 07-12 之间已涨过一次（H100 $2.95→$3.85）。5 月起累计 H100 +52.5%，B300 +55.7%。但挂牌价只反映边际稀缺，收入主体是长约。
- **单位经济学对折旧年限高度敏感**：每 IT MW 资本开支约 $47M，长约收入 $20–25M/MW·年，EBITDA 60%。EBIT/资本开支在 6/5/4/3 年折旧下分别约为 15%/12.6%/8.8%/2.6%，**折旧 ≥5 年才过 Gartner 的 12% ROIC 门槛**。现金回收期约 3.5 年；按短约价格 $40–50M/MW 约 1.3 年。
- **同业（10-22）**：CRWV、IREN、APLD、CIFR、WULF 距 2026 高点 −60% 到 −72%，ORCL −49%，**NBIS −44.5%，跌得最少也最贵**（EV/RPO 1.36x，CRWV 0.74x、ORCL 0.77x）。NBIS 净债务约 $2.2B（占 EV 5%），CRWV $46B（占 EV 60%）：市场把 NBIS 当权益融资的成长股，把 CRWV 当杠杆信用。
- **CoreWeave 信用压力（行业模板）**：9.625% 2032 债 10-14 约 79.5c（收益率约 15%），5 年 CDS 10-15 创纪录 1,194.5bp（6 月 452bp），S&P 评级 B+。原因：利息压过营业利润（Q2 利息 $640M，调整后营业利润 $128M；Q3 指引 $860–940M 对 $200–260M），叠加 CPI 偏热和 Gartner 报告（都在 10-14）。**没有找到契约或再融资问题**，压力在下一笔融资的成本。
- **需求端**：四大云厂商 2026 年资本开支指引合计约 $733B（7 月底；年初约 $640B），GOOGL、MSFT 都说 2027 年继续增长；ORCL RPO $664B。裂缝在 OpenAI：02 月 2030 年算力计划由 $1.4T 降到 $600B（CNBC）；04-27 WSJ 报道营收和用户未达标，CFO 担心付不起算力合同；04-29 FT 报道 Stargate 部分放弃。**10 月的新报道未找到。**
- **NBIS backlog 集中但对手方优质**：MSFT $17.4–19.4B，Meta $3B，加上 Meta 2026-03 最高 $27B（$12B 专用 + 最高 $15B 未售产能兜底）。推算 MSFT+Meta 约占 RPO $33.6B 的 **90%+**。Meta 兜底的作用类似 Nvidia 对 CRWV 的兜底。
- **历史类比**：倒下的（Global Crossing、Exodus）都是举债建网而收入跟不上；活下来的（Level 3、Equinix）在底部拿到了战略资本或做了债转股；IREN 2022 年靠无追索 SPV 保住母公司。**差异在于**光纤能用 20 年以上，过剩最终被吸收；GPU 只有 3–6 年寿命，只能靠减值出清。
- **EV 口径**：题目的 EV 约 $37B 复现不出来。stockanalysis 口径下 10-22 为 $45.8B（在 $165.47 时约 $47.5B），据此 EV/当前 ARR 约 15.3x，EV/年底 ARR 中值约 5.7x。请资产负债表 agent 核对。

## 1. GPU 租价（2024 → 2026-10）

**1a. Nebius 官网挂牌价（P，nebius.com/prices，Wayback 存档逐期解析；$/GPU-hr，按需）**

| 快照 | H100 | H200 | B200 | B300 | 备注 |
|---|---|---|---|---|---|
| 2025-06-29 | 2.95 | 3.50 | – | – | 承诺价 "from" H100 $2.00 / H200 $2.30；"长约最多省 35%" |
| 2026-03-01 | 2.95 | 3.50 | 5.50 | – | |
| 2026-05-07 | 2.95 | 3.50 | 5.50 | 6.10 | |
| 2026-07-12（08-19、09-01 相同） | **3.85** | 4.50 | 7.15 | 7.85 | 可抢占价固定：H100 2.15 / B300 4.30 |
| 2026-10-01 快照，"Effective Oct 1" 列 | **4.50** | 5.40 | 8.50 | 9.50 | 可抢占价改为动态 "from $0.79/$0.99"，上限为按需价 −$0.01；Genoa CPU $0.10→$0.13 |
| 2026-10-23 实时页 | 4.50 | 5.40 | 8.50 | 9.50 | 只剩新价列 |

各段涨幅：H100 2.95→3.85 +30.5%，3.85→4.50 +16.9%，累计 +52.5%。H200 累计 +54.3%，B200 累计 +54.5%，B300 6.10→9.50 累计 +55.7%（与媒体报道的"约 56%"一致）。第一次涨价：Barchart/Yahoo 2026-05-22 报道 Nebius 把 H100 从 $2.95 调到 $3.85，股价 05-21 +14.7%（S）。存档只能把时间框在 05-07 到 07-12 之间。
**解读**：挂牌价只覆盖边际按需客户，不能换算成已实现均价。可抢占价下限 $0.79 说明闲时有空余产能拍卖，不能据此推断利用率。

**1b. 指数与第三方**

| 指标 | 数值 | 日期 | 来源 |
|---|---|---|---|
| Silicon Data 指数页 | **H100 $2.88**（7 日 +10.3%）；H200 $3.51；B200 $6.29（7 日 +9.0%）；B300 $7.35 | 2026-10-22 | silicondata.com（S，指数商） |
| SDH100RT 历史 | 2025-08 2.22–2.26；2025-09 中旬低点 2.13；2026-07-27 2.75；2026-09-07 2.63 | | SD 博客（S；2025 年数值来自搜索摘要，未直接打开） |
| SD H100 中位数 | 云厂商 2024H2 $9.34 → 2025H2 $6.26（−33%）；neocloud 2025H2 $3.33；marketplace $1.95；美东非云厂商 $1.35（Q3'25）→ $2.90（Q3'26） | 2025-12-21 / 2026-07-31 | SD 博客（S） |
| SDB200RT | 2026-09-01 为 5.62，YTD +27.6%；**期限曲线倒挂**：09-07 12 个月期 5.39，现货 5.69（−5.3%） | 2026-09 | SD 博客（S） |
| Ornn OCPI H100（成交价指数） | $3.17（09-07）；随后 $3.28 创新高，月涨 22% | 2026-09-08 | KuCoin 转 MarsBit（S） |
| SemiAnalysis 1 年期 H100 合约 | $1.70（2025-10）→ $2.35（2026-03），+38% | | 二手引用（S，原文未取得） |
| Nvidia CFO Kress（Q1 FY27 电话会） | H100 租价 YTD +20%，A100 约 +15% | 2026-05-22 报道 | Barchart/Yahoo（S，转述电话会） |
| AWS P5（H100）按需价 | −44%（自 2025-06-01） | 2025-06-05 | AWS What's New（P） |

**结论**：2024 年到 2025 年中是下行段，主要是云厂商降价（AWS −44%）加上 marketplace 跌到约 $2。2025 年第三、四季度见底，2026 年回升：H100 ≈+35%（2.13→2.88），Blackwell +28% YTD，Nebius 挂牌价 +52–56%。**边际风险**：B200 期限曲线倒挂，说明买方预期 12 个月后价格略低；各家追踪器口径差距很大，H100 从 $0.94 marketplace 到 $7.4 云厂商都有，所以只看方向，不看绝对值。

## 2. 单位经济学与折旧敏感性

**输入（每 1 IT MW，GB300 NVL72，长约）**
- 机架：约 132–140kW/架 → 约 7.35 架/MW → 约 529 GPU/MW。单架价格：裸架 $3.7–5.0M，部署后约 $5.7M（Spheron；Data Gravity 2026-08，S）。→ **IT 资本开支取 $35M/MW**（7.35 × 约 $4.75M）。
- 数据中心土建、电力、冷却**取 $12M/MW**（假设，20 年折旧），合计 **$47M/MW**。交叉验证（均 S）：黄仁勋 $50–60M/MW；前 AWS 高管约 $30M/MW；SemiAnalysis GB300 集群约 $40M/MW。
- 收入：NBIS Q2'26 电话会（2026-08-12，MarketBeat 转述，S）：四笔长约（平均每笔 >$1B）yield **$20–25M/MW**；≤6 个月短约 **$40–50M/MW 或更高**；预付款覆盖长约相关资本开支 50–60%；首次 Blackwell 拍卖成交价比此前最高价高 15%。
  **口径核对（推算）**：529 GPU × 8,760h × $4.86/hr ≈ $22.5M。即长约 $20–25M/MW 对应 Blackwell Ultra 约 $4.3–5.4/GPU-hr，$40–50M/MW 对应约 $8.6–10.8/hr，接近 B300 按需挂牌价 $9.50。由此判断这是**年收入/IT MW**，不是 TCV。H100 对照：约 730 GPU/MW × $2.0 × 8,760 ≈ $12.8M/MW，与 SemiAnalysis 的"neocloud 约 $12M/MW"吻合（S）。
- EBITDA 率取 60%，参照 CoreWeave Q2'26 调整后 EBITDA 率 59%（P）。→ EBITDA $13.5M/MW·年。电费只占小头：1.3MW × 8,760 × $0.08 ≈ $0.9M。

**折旧敏感性（推算；DC 统一按 $12M/20 年 = $0.6M）**

| IT 折旧年限 | 年折旧 | EBIT | EBIT 率 | EBIT/资本开支 | 税前（CRWV 式：70% 债 @9.5% = $3.13M 利息） | 税前（NBIS 式：30% 可转债 @2.5% = $0.35M） |
|---|---|---|---|---|---|---|
| 6 年 | 6.43 | 7.07 | 31% | 15.0% | 3.94 | 6.72 |
| 5 年 | 7.60 | 5.90 | 26% | 12.6% | 2.77 | 5.55 |
| 4 年 | 9.35 | 4.15 | 18% | 8.8% | 1.02 | 3.80 |
| 3 年 | 12.27 | 1.23 | 5% | 2.6% | **−1.90** | 0.88 |

- 现金回收期 = 47 / 13.5 ≈ **3.5 年**，已经接近"3 年经济寿命"的悲观假设。短约 $45M/MW、运营成本绝对额不变（约 $9M）时，EBITDA 约 $36M，回收期约 **1.3 年**。NBIS 管理层据称给过约 22 个月的回收期（聚合站转述，S，未核实），介于两者之间，可能是用扣除预付款后的资本开支算的。
- 盈亏平衡：3 年寿命下 EBIT=0 需要收入约 $20.4M/MW（12.27/0.6）；4 年寿命下要达到 12% ROIC 需要收入约 $25M/MW。**也就是说，NBIS 长约 $20–25M/MW 恰好落在"4–5 年寿命才及格"的区间**。合同到期后能以什么价格续租，是真正的风险变量。
- 残值：amcompute 预测 H100 第 4 年残值为原价 22–49%（中值 36%），第 5 年 9–33%，第 6 年 4–11%。6 年直线折旧第 4 年账面 33%，被评为 "aggressive but defensible"（S，2026-10-17）。

**各公司折旧年限**（amcompute 汇总，2026-10-10，S，附各 10-K/20-F 链接）：CoreWeave 6 年（2023-01 由 5 年延长）；Oracle 6 年（FY2025 由 5 年延长）；MSFT、GOOGL 6 年（2022/23 由 4 年延长）；Meta 5.5 年（2025-01）；Amazon 部分服务器由 6 年**缩短**到 5 年（2025-01，唯一缩短的一家）；IREN 5 年；**Nebius 服务器与网络设备 2026-01 由 4 年延长到 5 年**（Q1'26 股东信，P，见内部 06-18 档），GPU 是否单独仍按 4 年，二手说法矛盾，未核实。

- **Burry 的批评**（2025-11，S：Saxo、Techstrong）：云厂商把服务器折旧年限拉长，但 GPU 产品周期只有 2–3 年。他估计 2026–2028 年五大厂合计少计折旧约 $176B，到 2028 年 ORCL 利润被高估约 27%，META 约 21%。
- **公司层面粗算（上限估计，假设全部 D&A 都来自 6 年资产）**：CRWV TTM D&A $3.99B，营收 $7.59B，营业利润 −$0.20B（stockanalysis，P 级数据转录）。改成 4 年寿命，D&A ×1.5 → +$2.0B，营业利润约 −$2.2B；改成 5 年，+$0.8B，约 −$1.0B。NBIS TTM D&A $765M，营业利润 −$507M。2026 年 4→5 年的延长据估减少当年 D&A 约 $168M（S）。

## 3. 同业对比（2026-10-22 收盘；行情：Yahoo chart + stockanalysis，P 级行情；资产负债为最近报告期）

| | NBIS | CRWV | IREN | ORCL | APLD | CIFR | WULF |
|---|---|---|---|---|---|---|---|
| 收盘 10-22 | 159.17 | 55.60 | 25.51 | 125.54 | 19.09 | 8.32 | 11.32 |
| 2026 收盘高点（日期） | 286.69（06-18） | 137.98（05-06） | 67.84（05-27） | 248.15（06-01） | 49.65（05-28） | 29.18（06-18） | 28.98（06-18） |
| 距高点 | **−44.5%** | −59.7% | −62.4% | −49.4% | −61.6% | −71.5% | −60.9% |
| 09-30 以来 | −32.5% | −36.2% | −37.6% | −8.6% | −21.7% | −47.4% | −23.5% |
| 10-22 单日 | −7.2% | −10.1% | −8.4% | −2.8% | −9.0% | −8.9% | −11.3% |
| 市值 | 43.6B | 30.7B | 10.1B | 380.6B | 5.8B | 3.5B | 5.7B |
| EV（stockanalysis） | 45.8B | 76.7B | 12.0B | 512.6B | 9.3B | 8.2B | 8.3B |
| 净债务 | 2.15B | 46.0B（含约 16.5B 租赁） | 1.94B | 132.1B | 3.53B | 4.75B | 2.62B |
| 净债务/EV | 5% | 60% | 16% | 26% | 38% | 58% | 32% |
| TTM 营收 | 1.36B | 7.59B | 0.71B | 71.8B | 0.87B | 0.19B | 0.17B |
| 前瞻指标 | FY26 指引 3.0–3.4B；2026 年底 ARR 7–9B | FY26 指引 12.4–13.2B | 2026 产能已签 ARR 约 $4B（约 $1B 已运营） | FY27 营收 ≥$90B | 未来 12 个月投产 600MW+ | – | – |
| Backlog/RPO | RPO 33.6B（>40B "committed backlog"） | 104B（Q3 初另签 >25B） | 未找到总数（MSFT 9.7B/5 年） | RPO 664B | 约 36B（S） | 未核实 | Fluidstack 360MW 6.7B（2025，S） |
| EV/TTM 营收 | 33.8x | 10.1x | 17.0x | 7.1x | 10.7x | 43x | 50x |
| EV/前瞻 | FY26 中值 14.3x；ARR 中值 5.7x | FY26 中值 6.0x | 已签 ARR 3.0x | FY27 5.7x | – | – | – |
| EV/Backlog | 1.36x | 0.74x（0.59x 含 +25B） | – | 0.77x | 0.26x | – | – |
| 信用 | 2030 0.5% / 2034 4.5% 可转债；二级价格未找到 | 见下 | 未找到 | S&P BBB−（2026-07-09，S）；2032 债收益率约 7.24%（10-14，S） | 未找到 | Google 为 Fluidstack 租约兜底 $1.4B（S） | Google 兜底 $3.2B，持股约 14%（S） |

算式：EV/前瞻 = EV ÷ 指引中值，例如 NBIS 45.78/3.2 = 14.3x，45.78/8 = 5.7x；CRWV 76.69/12.8 = 6.0x；ORCL 512.64/90 = 5.7x。EV/Backlog：NBIS 45.78/33.6，CRWV 76.69/104，ORCL 512.64/664，APLD 9.31/36。NBIS 的净债务取 6/30 数据，未计入 8 月可转债：发行 +$5.75B 债，$0.8B 旧债换股，净现金 +约 $5.68B，加总后净债务降到约 $1.4B（未计 Q3 现金消耗）。
业务模式不同：APLD、CIFR、WULF 主要是出租机房（hosting/colo，不买 GPU），收入/MW 远低于 GPU 云，但资产寿命长；NBIS、CRWV、IREN 是 GPU 云；ORCL 是综合云厂商。

**CoreWeave 信用压力明细（10 月）**
- 债券：9.625% 2032 约 79.5c，收益率约 15%（10-14，TIKR 2026-10-19，S）；9.75% 2031 收益率约 14.9%（investinglive 10-15 转 CNBC，S）；10-15 反弹后 Oct-2031 82.8c、Jun-2030 91.3c（roic.ai 搜索摘要，S，原页 403）。
- CDS：5 年期 10-15 创纪录 1,194.5bp，6 月为 452bp（TIKR，S）；约 1,000bp 对应约 63% 的 5 年隐含违约概率（Reuters，经 LDS 转述，S）。
- 债务：6/30 借款约 $35.1B + 租赁约 $16.5B = $51.6B。Q2 新增 $3.1B 公开银团延迟提款贷款、>$10B 无担保债和可转债（含首笔欧元债），Jane Street 投资 $1B（Q2 新闻稿，P）。现金 $5.52B（P）。
- 起因见摘要；另有 AI 债券供给拥挤（GOOGL/AMZN/META/ORCL 年内发债 >$228B，截至 10-13，LSEG，S）。CEO Intrator 称市场 "irrational"。
- **契约和再融资**：没有找到任何违约、豁免或到期墙报道。Nvidia 兜底购买未售产能至 2032-04-13（S）。Microsoft 占 FY2025 营收约 67%（10-K，经二手转述，S）。
- 对 NBIS 的传导：10-14 当天 CRWV −16%，NBIS 约 −10%（S）。NBIS 可转债票息 0.5–4.5%，CRWV 无担保债约 9.6–9.75%；NBIS CFO 称 2026 年客户预付款 >$9B（S）。但 NBIS 2026 年资本开支 $20–25B，2027 年仍需外部融资，"下一块钱的成本"同样会冲击它。

**私有公司（S）**：Lambda 在融最多 $4B 的 IPO 前轮，投前约 $14.5B，目标 2027 年上市（WSJ，2026-10-06）。Crusoe 在谈 $3B 融资，2025-10 估值约 $10B（Bloomberg，2026-07）。Together、Fluidstack 的数据未找到；Fluidstack 的租约由 Google 兜底。

## 4. 需求端

**资本开支指引（7 月底 Q2 财报，Platformonomics 2026-07-31 汇总公司口径，S）**

| | Q2'26 资本开支 | 2026 全年指引 | 2027 表述 |
|---|---|---|---|
| Amazon | $54.8B | 约 $220B（原约 $200B，主因内存涨价） | 2027 年"仍然产能不足" |
| Alphabet | $44.9B | $195–205B（原 $180–190B） | "increase significantly in 2027" |
| Meta | $31.1B | $130–145B | 为 2026–27 年产能最大化；另有 BlackRock 表外数据中心 |
| Microsoft | $41B（含融资租赁） | 日历 2026 年约 $175B（原约 $190B，作者认为主要是租赁重分类） | FY27 资本开支同比增长 |
| Oracle（P，Q1 FY27，2026-09-10） | 单季 $28.5B，TTM ≈$75.7B | FY27 营收 ≥$90B | RPO $664B（+$209B 同比）；FCF −$5.4B；ATM 发股 $20B；"需求增长快于供给" |

四家 2026 年合计 ≈ 220 + 200 + 137.5 + 175 ≈ **$733B**（取中值）。下一个检验点是 10 月底的 Q3 财报，具体日期本 track 未核实。

**AI 实验室**
- OpenAI（均为 S）：02-20 CNBC 报道 2030 年算力支出计划从 $1.4T 降到 $600B，2030 年营收预期 >$280B。04-15 Stargate 挪威直采取消，Microsoft 接手，英国项目暂停。**04-27 WSJ（Reuters 转述）**：年初多个月度营收目标未达成（在编程和企业市场输给 Anthropic），2025 年底未达成 10 亿周活目标，CFO Friar 担心付不起未来算力合同；Altman 和 Friar 回应称 "ridiculous"。04-29 FT：Stargate 重组、部分放弃，转向双边合同。反方证据：04-30 OpenAI 称提前达成 10GW，其中 3GW 签于过去 90 天（含 Amazon 2GW）。**没有找到 10 月的新营收缺口报道。**
- Anthropic：与 Google/Broadcom 签 3.5GW TPU（2026-04，Broadcom 文件，经二手转述），2027 年起上线；The Information 报道其对 Google Cloud 的 5 年承诺约 $200B（S，未证实）。xAI：未找到。
- Gartner（2026-10-14；原页 403，经 CRN Asia、Dealroom 转述，S）：2030 年前 **>80% 的 neocloud 不再独立运营**（被收购、合作或倒闭）；2030 年底前 **>$3.5T** 投入面临减值风险；2026 年 AI 基建约 $1T，2027–30 年再投 $6T，要达到 12% ROIC 需累计营收 $8.5T，Gartner 预测不超过 $3.6T；AI-optimized IaaS 2027 年 $66B、2030 年 $174B。**口径疑点（推算）**：ORCL IaaS $7.4B×4 ≈ $29.6B，加 CRWV $12.8B、NBIS $8B，≈ $50B，三家 2026 年 run-rate 已接近 Gartner 2027 年整个市场，说明定义很窄。80% 只宜作方向性判断。

**NBIS 锚定客户与集中度**
- Microsoft：5 年 $17.4B，最高 $19.4B，Vineland NJ，2025-09（6-K，P，见历史档）。Meta：$3B（2025-11，P）。Meta 新协议（2026-03，Nebius newsroom + 6-K，P）：最高约 **$27B**，其中 $12B 为专用产能，2027 年初起用 Vera Rubin 交付；另有最高 $15B 未售产能，由 Meta 在部署后 5 年内兜底购买，Nebius 优先转售第三方。Q2'26 四笔长约：Reflection、Cohere、一家美国 neolab、一家美国量化交易公司，平均每笔 >$1B（S）。
- **集中度推算**：RPO YE2025 $21.3B → Q1'26 $33.6B（+$12.3B ≈ Meta $12B 专用）。(17.4 + 3.0 + 12.0) / 33.6 ≈ **96%**。这是上限估计，因为没有扣除已确认收入，且 Microsoft 可能按 $17.4B 下限计入。保守说法是 MSFT+Meta ≈ RPO 的 **90%+**。公司未披露分客户比例。RPO 中 29% 在 24 个月内确认（内部 09-05 档）。
- 判断：对手方是两家投资级公司，加上 Meta 兜底，所以违约风险低。真正的风险是**交付**：延迟会触发违约金或终止条款。另一风险是 2027 年以后的续约价格。

## 5. 历史类比（简）

| 案例 | 事实 | 来源 |
|---|---|---|
| Global Crossing | 2002-01-28 申请 Ch.11；债务 $12.4B，年利息约 $600M；靠举债建 27 国网络，流量增长低于预期 | Information Age（S） |
| Exodus（托管/IDC） | 2001-09-26 申请 Ch.11；债务约 $3.5B；2001 年 Q2 亏损 $538M；GE Capital 提供 $200M DIP | SEC 8-K（P）；InformationWeek（S） |
| Level 3（幸存） | 2002-07-08 发行 $500M 9% 10 年期可转债（转股价 $3.41），Longleaf $300M、Berkshire $100M、Legg Mason $100M 认购，用于行业整合中的收购 | SEC 8-K（P）；CNN（S） |
| Equinix（幸存） | 2002-10-02 宣布与 i-STT、Pihana 合并；STT 以可转债注资 $30M；赎回 >$116M 13% 优先票据；2002-12-31 完成 | Equinix SEC 425 / 8-K（P） |
| 2018 Giga Watt | 2018-11 申请 Ch.11；BTC 从约 $19,000 跌到约 $4,400；资产 <$50k，负债 $10–50M | The Block、Crowdfund Insider（S） |
| 2022 Core Scientific | 2022-12-21 申请 Ch.11，债务约 $1B（设备融资），客户 Celsius 违约成为导火索；2024-01 走出破产，削债约 $400M，老股东保留约 60% | The Block、Globe and Mail（S） |
| 2022 Iris Energy（今 IREN） | 两个无追索 SPV 设备贷违约，2022-11-18 被要求偿还 $107.8M；矿机停机，母公司因风险隔离幸存 | SEC 20-F FY2023（P） |

**幸存者的共同点**：(1) 底部有现金跑道，能拿到战略资本（Level 3、Equinix）；(2) 债务隔离：无追索 SPV 或债转股（IREN、Equinix）；(3) 客户信用好（Core Scientific 的导火索就是客户违约）；(4) 资产寿命长，光纤过剩最终被吸收。**GPU 不满足 (4)**，必须在合同期内收回现金。对应到 NBIS 的指标是投资级客户占比、预付款覆盖率、低票息长久期融资，三项都好于 CRWV；但 2026 年资本开支 $20–25B 对应营收约 $3.2B，融资窗口仍然关键。

## 6. 来源

| 标题 | 日期 | URL | 标签 |
|---|---|---|---|
| Nebius pricing（实时 + Wayback 快照 20250629/20260301/20260507/20260712/20260819/20260901/20261001） | 2026-10-23 / 各快照 | https://nebius.com/prices ; https://web.archive.org/web/20261001030509/https://nebius.com/prices | P |
| Nvidia says H100 GPU prices…（Barchart） | 2026-05-22 | https://finance.yahoo.com/markets/stocks/articles/nvidia-says-h100-gpu-prices-195641894.html | S |
| Silicon Data H100 index page | 2026-10-22 | https://www.silicondata.com/products/silicon-index/h100 | S |
| SD 博客：H100 price over time / by region Q3 2026 / B200 Aug 2026 | 2025-12-21 / 2026-07-31 / 2026-09 | https://www.silicondata.com/blog/h100-rental-price-over-time （另两篇同目录：h100-rental-prices-by-region-q3-2026、b200-rental-price-august-2026-update） | S |
| H100 rental prices rise 22% in a month（Ornn） | 2026-09-08 | https://www.kucoin.com/news/flash/nvidia-h100-gpu-rental-prices-rise-22-in-a-month | S |
| AWS EC2 NVIDIA GPU price reduction | 2025-06-05 | https://aws.amazon.com/about-aws/whats-new/2025/06/pricing-usage-model-ec2-instances-nvidia-gpus | P |
| GPU Depreciation Schedules / depreciation vs market（amcompute） | 2026-10-10 / 10-17 | https://www.amcompute.com/gpu-depreciation-schedules | S |
| Burry: Big Short（Saxo） | 2025-11-12 | https://www.home.saxo/content/articles/equities/big-short-12112025 | S |
| NVL72 cost（Data Gravity） | 2026-08 | https://www.datagravity.dev/p/how-much-does-an-nvidia-nvl72-cost | S |
| Nebius Q2 earnings call highlights（MarketBeat） | 2026-08-12 | https://www.marketbeat.com/instant-alerts/nebius-group-q2-earnings-call-highlights-2026-08-12/ | S |
| Nebius–Meta agreement（newsroom + 6-K Ex-99.1） | 2026-03 | https://nebius.com/newsroom/nebius-signs-new-ai-infrastructure-agreement-with-meta ; https://www.sec.gov/Archives/edgar/data/1513845/000110465926027886/tm268879d1_ex99-1.htm | P |
| CoreWeave Q2 2026 Results | 2026-08-11 | https://investors.coreweave.com/news/news-details/2026/CoreWeave-Reports-Strong-Second-Quarter-2026-Results/default.aspx | P |
| CoreWeave fell 25% on bond distress（TIKR） | 2026-10-19 | https://www.tikr.com/blog/coreweave-stock-fell-25-last-week-on-bond-distress-is-it-a-buy-now | S |
| CoreWeave bonds trade like distressed debt（investinglive） | 2026-10-15 | https://investinglive.com/stocks/coreweave-bonds-trade-like-distressed-debt-as-ai-spending-outpaces-balance-sheets/ | S |
| CoreWeave shares and bonds slide（LDS，转 Reuters） | 2026-10-20 | https://letsdatascience.com/news/coreweave-shares-and-bonds-slide-as-debt-fears-grip-ai-build-b082a38e | S |
| stockanalysis statistics（7 只代码）+ Yahoo chart API 日线 | 2026-10-22 | https://stockanalysis.com/stocks/nbis/statistics/ ; https://query1.finance.yahoo.com/v8/finance/chart/NBIS | P 级行情 |
| Oracle Q1 FY27 results（Placera 转载） | 2026-09-10 | https://www.placera.se/pressmeddelanden/oracle-announces-q1-results-driven-by-triple-digit-growth-in-cloud-infrastructure-revenues-20260910 | P |
| Follow the CAPEX: Q2 2026 Scoreboard | 2026-07-31 | https://platformonomics.com/2026/07/follow-the-capex-q2-2026-scoreboard/ | S |
| Gartner 80% neoclouds（CRN Asia 转述；Gartner 原页 2026-10-14 返回 403） | 2026-10 | https://www.crnasia.com/news/2026/cloud/gartner-80-of-neoclouds-to-lose-independence-by-2030-as-ai | S |
| OpenAI falls short of targets, WSJ（Reuters） | 2026-04-27 | https://finance.yahoo.com/markets/stocks/articles/openai-falls-short-revenue-user-031016813.html | S |
| OpenAI cuts spending plan（ForkLog 转 CNBC） | 2026-02-23 | https://forklog.com/en/openai-reduces-spending-plans-by-800-billion-amid-stargate-project-setback/ | S |
| OpenAI scales back Stargate in Europe（Techzine） | 2026-04-15 | https://techzine.eu/news/infrastructure/140487/openai-scales-back-stargate-in-europe-microsoft-fills-the-gap | S |
| FT: Stargate reworked（Newsquawk） | 2026-04-29 | https://www.newsquawk.com/headlines/openais-usd-500bln-stargate-plan-to-secure-computing-power-is-being-reworked-and-in-some-places-abandoned-ft-reports | S |
| OpenAI hit 10 GW goal（The Decoder） | 2026-04-30 | https://the-decoder.com/openai-says-it-hit-its-10-gigawatt-compute-goal-years-ahead-of-schedule/ | S |
| IREN contracted ARR $4B（Pulse2） | 2026-08-27 | https://pulse2.com/iren-contracted-arr-reaches-4-billion-as-ai-cloud-revenue-jumps-nearly-eightfold/ | S |
| Applied Digital FQ1 rent（Trefis） | 2026-10-13 | https://www.trefis.com/articles/618482/how-much-of-applied-digitals-fiscal-q1-revenue-was-rent/2026-10-13 | S |
| Lambda $4B pre-IPO round（LDS 转 WSJ） | 2026-10-06 | https://letsdatascience.com/news/lambda-pursues-4-billion-pre-ipo-funding-round-909f4022 | S |
| Global Crossing Ch.11 | 2002-01 | https://www.information-age.com/global-crossing-files-for-chapter-11-bankruptcy-23571 | S |
| Exodus 8-K / Level 3 8-K / Equinix 425 | 2001-09 / 2002-07 / 2002-10 | https://www.sec.gov/Archives/edgar/data/1013740/0000891618-01-501801.txt ; https://www.sec.gov/Archives/edgar/data/0000794323/000095013002004905/dex991.txt ; https://www.sec.gov/Archives/edgar/data/1101239/000101287002003998/d425.htm | P |
| Core Scientific Ch.11（The Block） | 2022-12-21 | https://www.theblock.co/post/196925/core-scientific-files-chapter-11-bankruptcy | S |
| Iris Energy 20-F FY2023（SPV default） | 2023 | https://www.sec.gov/Archives/edgar/data/0001878848/000114036123043816/brhc20058647_20f.htm | P |
| Giga Watt Ch.11（Crowdfund Insider） | 2018-11 | https://www.crowdfundinsider.com/2018/11/141608-north-american-crypto-mining-firm-giga-watt-files-for-bankruptcy/ | S |

## 7. 未核实 / 缺口

1. **10-22 板块单日大跌**（NBIS −7.2%、CRWV −10.1%、WULF −11.3%）的原因未查到，留给新闻 agent。
2. CoreWeave 10-16 之后的债券和 CDS 没有一手报价；82.8c/91.3c 只看到搜索摘要。契约或再融资问题是"没找到"，不是"已确认没有"。
3. Nebius GPU 折旧年限：服务器与网络设备 5 年明确，GPU 是否单独按 4 年说法矛盾；20-F 附注未读到（SEC 拦截）。
4. $/MW 是年收入还是 TCV：本文用 GPU-hr 反推判断为年收入；约 22 个月回收期只有聚合站转述。
5. NBIS 分客户集中度未披露，90%+/96% 是推算；RPO $33.6B 与 ">$40B backlog" 口径未厘清。
6. 题目 EV 约 $37B 与本文 $45.8–47.5B 不一致，请资产负债表 agent 复核（是否把可转债当作权益）。
7. Gartner 原文 403，只看到转述，模型未公开。
8. OpenAI 10 月营收缺口报道未找到，只有 2026-04-27 WSJ；xAI 资本开支未找到；四大云厂商 Q3 财报未出；MSFT $175B 与 $190B 口径有歧义。
9. SemiAnalysis 1 年期合约指数、Ornn 10 月读数未直接取得；各追踪器口径相差最多约 8 倍。
10. IREN、APLD、CIFR、WULF 10 月口径 backlog 和各家债券价格未找到。
