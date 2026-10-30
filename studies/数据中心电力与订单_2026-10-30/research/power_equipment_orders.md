# 电力设备厂商订单：数据中心需求是否仍在确认（截至 2026-10-30）

- 研究日：2026-10-30。SEC EDGAR 与公司 IR 文件均于当天抓取。本文不构成投资建议。
- 覆盖范围：GEV、Siemens Energy、MHI、Caterpillar、Cummins、Vertiv、Eaton、Bloom Energy；Schneider 只列了二手数据；Hitachi Energy 未覆盖。
- 标注规则：
  - **P** 指一手来源：SEC 文件（8-K、10-Q、10-K、XBRL），或公司 IR 发布的 PDF，包括公司官网自己挂出的电话会文字稿。
  - **S** 指二手来源：第三方转录稿或新闻，只在找不到一手来源时使用。
  - "未披露"表示公司没有给出该数字。"推算"表示数字由我根据已披露数字计算，计算方法写在旁边。
- 机器可读数据见 `../data/power_equipment_orders.csv`，共 426 行，长表格式。GEV Q3 新闻稿和演示材料的纯文本副本见 `../raw/`。

---

## §0 结论

1. **最近一季的订单和积压仍在创新高，没有出现掉头。** 下列口径中，没有一家公司的总 book-to-bill 低于 1，没有取消，也没有降价：
   - GEV 2026Q3：订单 $29.3B（有机 +96%），RPO $196.7B，燃机积压加 SRA 达 122 GW。
   - Caterpillar 2026Q3：积压约 $78B（S，来自电话会；10-Q 尚未发布）。
   - Siemens Energy FQ3（4–6 月）：订单 €17.9bn，积压 €162bn。
   - MHI FQ1（4–6 月）：大型燃机在手 80 台 / 35 GW。
2. **但增量在放缓，而且放缓集中在与数据中心直接相关的电气化环节和新签环节。** 具体信号：
   - GEV 电气化的数据中心订单从 Q2 的 $2.7B 降到 Q3 的约 $1.4B；电气化 book-to-bill 从 2.5 降到 1.7，再降到 1.4；电气化订单有机 −9%（公司解释为去年同期基数高）。
   - GEV 每季新签燃机 GW 依次为 24、21、20、11。
   - CAT 积压每季净增依次为 +11.5B、+9.4B、约 +5.9B。
   - Siemens 管理层预告 FQ4 订单低于前三季。
   - MHI 预测 FY26 的 GTCC 订单同比下降（基数高）。
   - Vertiv 宣布今后不再披露订单。
3. **数据中心占比多为定性，能给出数字的很少。**
   - GEV：燃机合同 GW 中"approximately 80% are traditional customers and 20% are for data centers"；电气化今年前三季数据中心订单超过 $6B，推算约占同期电气化订单 $18.8B 的三分之一。
   - Siemens Energy："Data centers are an important additional driver, but they are not the foundation of our outlook"。
   - CAT 和 Cummins 只说发电业务增长"primarily in data center applications"。
   - Vertiv 和 BE 的业务几乎全部面向数据中心。
4. **价格仍在上涨，但电网设备涨价已近顶部。**
   - 燃机：GEV 2026 年订单 $/kW 约比 2025 年高 50%；MHI 称"Order pricing has not declined"；Siemens 称"Pricing in Gas Services remains very strong"。
   - 电网设备：Siemens 称欧洲价格已"stabilized at a high level"，今后利润率扩张靠执行，"rather than further broad-based price increases"。
5. **没有一家管理层说超大规模客户或 neocloud 在暂停。**
   - GEV 被直接问到客户是否有融资困难、是否要求退出 SRA，CEO 回答"No, David, we're not"。
   - Vertiv 称项目层面"nothing out of the ordinary"。
   - 唯一的书面风险信号来自 BE 的 Q3 10-Q：风险因素写到了数据中心禁令、融资变难、neocloud 被视为高信用风险、可能的价格压力。
6. **对 Nebius、CoreWeave 等 neocloud 的含义。** 上游设备订单还在确认 2027–2030 年的物理建设，GEV 已在卖 2032 年的交付位置，CAT 接单排到 2029/2030 年。但数据中心专属的电气化订单本季环比腰斩，这是第一条需要验证的裂缝。下一批验证点：
   - Eaton 和 Cummins 的 Q3 财报（11 月初）。
   - Siemens Energy FQ4（2026-11-11）。
   - MHI 上半年（11 月上旬）。
   - GEV 2027 年 1 月财报，看电气化数据中心订单能否回到每季 $2B 以上。
   - **一句话判断：仍在上升，增速开始见顶，尚未掉头。**

---

## 1. GE Vernova（GEV），2026Q3 于 2026-10-28 发布

> 注意：仓库 09-05 卡写的 Q3 日期是 2026-10-21，实际发布日是 **2026-10-28**（8-K 和 10-Q 同日提交）。

### 1.1 公司层面季度序列（P）

| 季末 | 订单 | 有机增速 | 收入 $m | 调整后 EBITDA 率 | RPO $m | 合同负债+递延收入 $m | 当季合同负债现金流入 $m（推算） |
|---|---:|---:|---:|---:|---:|---:|---:|
| 2025-03-31 | 约 10.3B（推算：分部重述数相加） | — | 8,032 | 5.7% | 123,438 | 18,851 | 1,124 |
| 2025-06-30 | 约 12.5B（推算：同上） | — | 9,111 | 8.5% | 128,650 | 19,751 | 736 |
| 2025-09-30 | 14.6B | +55% | 9,969 | 8.1% | 135,269 | 20,304 | 559 |
| 2025-12-31 | 22.2B | +65% | 10,956 | 10.6% | 150,238 | 25,950 | 5,600 |
| 2026-03-31 | 18.3B | +71% | 9,339 | 9.6% | 163,276 | 31,949 | 5,574 |
| 2026-06-30 | 24.2B | +88% | 11,104 | 11.3% | 176,284 | 40,037 | 8,121 |
| **2026-09-30** | **29.3B** | **+96%** | **12,642** | **15.4%** | **196,721** | **45,747** | **5,816** |

- 来源：
  - RPO 和合同负债取自 XBRL 标签 `RevenueRemainingPerformanceObligation` 和 `ContractWithCustomerLiability`。
  - 当季合同负债现金流入，用 XBRL 中 `IncreaseDecreaseInContractWithCustomerLiability` 的累计数逐季相减得出。
- Q3 的 RPO 拆分：设备 $104.1B，其中 33%、60%、97% 分别在 1、2、5 年内确认；服务 $92.7B。

### 1.2 分部（P）

分部数据说明：2026 年起分部口径重组。2025 年前三季用 2026 年新闻稿中的重述对比数；2025Q4 用旧口径，未重述。

| 季末 | Power 订单 / 收入 / 分部 EBITDA 率 | Electrification 订单 / 收入 / 率 | Wind 订单 / 收入 / 率 |
|---|---|---|---|
| 2025-03-31 | 6,263 / 4,449 / 11.6% | 3,366 / 1,840 / 11.1% | 640 / 1,850 / — |
| 2025-06-30 | 7,109 / 4,785 / 16.4% | 3,283 / 2,162 / 14.5% | 2,063 / 2,245 / −7.3% |
| 2025-09-30 | 7,832 / 4,863 / 13.4% | 5,069 / 2,565 / 15.1% | 1,833 / 2,647 / −2.3% |
| 2025-12-31（旧口径） | 11,693 / 5,749 / 16.9% | 7,424 / 2,960 / 17.1% | 3,145 / 2,368 / −9.5% |
| 2026-03-31 | 10,008 / 4,971 / 16.3% | 7,112 / 2,959 / 17.8% | 1,199 / 1,432 / −26.7% |
| 2026-06-30 | 16,729 / 5,477 / 18.8% | 6,347 / 3,637 / 18.4% | 1,249 / 2,026 / −13.6% |
| **2026-09-30** | **21,780 / 6,067 / 21.4%** | **5,371 / 3,862 / 19.1%** | **2,140 / 2,741 / 2.6%** |

- 金额单位为 $m。
- 2026Q3 的 book-to-bill（推算 = 订单 / 收入）：
  - Power 3.59x。
  - Electrification 1.39x；公司口径为"approximately 1.4"，Q1 约 2.5，Q2 约 1.7。
  - Wind 0.78x。
  - 全公司 2.32x；管理层原话为"more than 2-for-1"。
- 2026Q3 分部 RPO（$m）：
  - Power 130,854，其中设备 54,422；2025-09-30 为 84,216，其中设备 18,977。
  - Electrification 46,148，其中设备 42,204。
  - Wind 19,952，同比下降。
- Electrification 设备积压（$B）逐季为 26.5、30.5、38.6、40.6、42.2。Q1 起含 Prolec 约 $5B。季增依次为 +4.0、+8.1、+2.0、**+1.6**。

### 1.3 燃机：GW、交付窗口与价格（P）

| 季末 | 积压+SRA 合计 GW | 其中积压 GW | 其中 SRA GW | 当季新签 GW（SRA+订单） | SRA 转订单 GW | 当季发货 GW |
|---|---:|---:|---:|---|---:|---:|
| 2025-06-30 | 55 | 29 | 25 | — | — | — |
| 2025-09-30 | 62 | 33 | 29 | 略超 12（12 + 1） | 7 | 4 |
| 2025-12-31 | 83 | 40 | 43 | 24（21 + 3） | 8 | 3 |
| 2026-03-31 | 100 | 44 | 56 | 21（19 + 2） | 6 | 4 |
| 2026-06-30 | 116 | 53 | 63 | 20（18 + 2） | 10 | 3 |
| **2026-09-30** | **122** | **64** | **58** | **11（8 + 3）** | **13** | **5** |

- 年末目标：2026Q1 定为 ≥110 GW，Q2 上调到 ≥125 GW，Q3 再上调到 **≥130 GW**。
  - 要达到 130 GW，Q4 需净增 ≥8 GW。若发货仍约 5 GW，新签需约 13 GW（推算）。
- Q3 燃机订单 112 台、16.6 GW，去年同期 29 台、7.4 GW：
  - 重型燃机 55 台，其中 HA 21 台。
  - 航改型燃机 57 台。
- Q3 发货 32 台、5.3 GW。
- **交付窗口：**
  - Q1 电话会："we sold a lot of 2030 slots"；当时 2029 和 2030 两年合计约剩 10 GW。
  - Q2 电话会：年底"mostly sold out through '30, and to have sold more than half of the 30 gigawatts of '31 production slots"。
  - Q3 电话会："This quarter, we sold multiple slots for 2032 delivery"。
  - Q3 电话会还提到一个拐点："backlog is now greater than our SRA balance"。
- **产能**（Q2 新闻稿）：2026Q3 年化 20 GW，2028 年 24 GW，2030 年 30 GW。
- **价格：**
  - Q1：1H26 订单 $/kW 比 4Q25 高 10–20 个点。
  - Q3："3Q orders were priced more than 20% above 4Q25 equipment orders"，部分原因是航改型占比高。
  - Q3："Full year 2026 Gas orders pricing per kW will be approximately 50% higher than full year 2025 orders"。
  - 管理层预计 Q4 的 $/kW 低于 Q3，原因是航改型更少、50Hz 机组更多，原话为"not because the demand is softer"。
- **数据中心占比**（Q3 电话会，P）："approximately 100 customers in 25 different countries, of which approximately 80% are traditional customers and 20% are for data centers"。Q1、Q2 也是约 20%。

### 1.4 电气化中的数据中心订单（P）

| 季度 | 电气化数据中心订单 | 当季电气化订单 | 占比（推算） |
|---|---:|---:|---:|
| 2025 全年 | 少于 $2.4B（Q1 称"more than all of last year"） | 19.3B（旧口径） | — |
| 2026Q1 | $2.4B | 7.1B | 约 34% |
| 2026Q2 | $2.7B | 6.3B | 约 43% |
| **2026Q3** | **约 $1.4B** | 5.4B | 约 26% |
| 2026 前三季 | 超过 $6B | 18.8B | 超过 32% |

- 来源：Q1 新闻稿；Q2、Q3 为公司官网发布的电话会文字稿。
- 其他进展：首单 MV-UPS 来自 hyperscaler；6 MW 户外固态变压器（SST）已获 hyperscaler 中标通知，Q4 签约。
- 收购 Trench Group（约 €8.0bn / $9.0B），预计 2027 年底交割。

### 1.5 指引变化（P）

| 发布日 | FY26 收入 | 调整后 EBITDA 率 | FCF |
|---|---|---|---|
| 2026-01-28 | $44–45B | 11–13% | $5.0–5.5B |
| 2026-04-22 | $44.5–45.5B | 12–14% | $6.5–7.5B |
| 2026-07-22 | $45.5–46.5B | 12–14% | $11.5–12.5B |
| **2026-10-28** | **$46.5–47.5B** | **13.5–14.5%** | **$16–17B** |

- 分部指引：
  - Power 有机增长 19–21%，原为 18–20%；分部利润率 19–21%，原为 17–19%。
  - Electrification 收入 $14.5–15.0B，利润率"trending toward the higher end"of 18–20%。
  - Wind 亏损 $400–500M，原为约 $400M。
- 2028 年展望最后一次更新在 2026-01-28：收入 $56B（原为 $52B），调整后 EBITDA 率 20%，2025–2028 累计 FCF ≥$24B。2026 年三份季度新闻稿都没有重述或修改。管理层称将在下次 Capital Markets Day 给出 2030 年指引，日期在 2027 年 1 月财报会上公布。
- 回购授权从 $10B 提高到 $20B。

### 1.6 放缓信号检查

| 信号 | 结果 |
|---|---|
| 订单减速 | **部分出现。** 公司总订单仍加速（+96%）。但 Electrification 有机 −9%（公司称 3Q25 同步调相机大单抬高了基数），数据中心订单 $2.7B → $1.4B，每季新签燃机 GW 24 → 21 → 20 → 11。管理层称航改型"wouldn't say that will sustain the 2Q, 3Q run rate ... in 4Q"。 |
| 取消 / 推迟 | **未见。** 原话："No, David, we're not"，回答的是融资困难、退出 SRA、SRA 转化放慢三个问题。 |
| book-to-bill < 1 | 全公司 2.3x、Power 3.6x、Electrification 1.4x，均未低于 1。Electrification 已连续两季下降。Wind 0.78，与数据中心无关。 |
| 客户暂停 | 未见。 |
| 降价 | **未见。** Q4 的 $/kW 环比下降是机型结构所致，管理层明确说不是需求转弱。 |

### 1.7 GEV Q3 2026 对仓库 GEV 卡观察项的影响（不改卡，只列变化）

观察项定义见 `companies/gev/2026-09-05/decision_card.json`。

1. **利润率能否走向约 20%（对应 K-F 和"WATCH → STARTER"条件 2）：明显改善。**
   - 调整后 EBITDA 率从 Q2 的 11.3% 升到 **15.4%**，有机 14.7%。
   - Power 分部 **21.4%**，离 2028 年 Power 目标 22%（2026-01 新闻稿，P）只差 0.6 个百分点。管理层说 Q3 通常是服务业务利润率最低的季度，同时也是首个以更高价格批量发货的季度（原话"first quarter of our 5 gigawatt of gas power equipment shipments at better prices"）。
   - FY26 指引上调到 13.5–14.5%。推算 Q4 隐含利润率约 16–19%，中值约 17.9%。
   - **K-F 没有触发，反而在快速收敛。**
   - 另一处需要注意：卡里 2028 年的锚是 $52B 收入。公司 2026-01 已把 2028 年收入目标上调到 $56B，按 20% 利润率推算 EBITDA 约 $11.2B，高于卡的 base 情形（$8.5B）和 bull 情形（$10.4B）。这一点需在下次刷新卡时处理。
2. **合同负债（K-E）：仍在增长，但增速放慢，且 Q4 指引隐含会进一步放慢。**
   - 余额从 $40.0B 增至 **$45.7B**。Power 为 $33.2B，2025 年末为 $16.5B。
   - 季度现金流入从 Q2 的 $8.1B 降到 Q3 的 **$5.8B**，季末余额实际增加 $5.7B。
   - **K-E 未触发。**
   - 但 FY26 FCF 指引 $16–17B 减去前三季 $15.3B，推算 Q4 FCF 只有 **$0.7–1.7B**。这说明 Q4 的预付款和 SRA 流入预计会大幅放缓，或被其他支出抵消。此项为推算，需在 1 月财报验证。
   - 全年 FCF 约为调整后 EBITDA 的 2.3–2.7 倍，中值约 2.5 倍（推算：FCF 指引 16–17 ÷ 指引隐含 EBITDA 6.3–6.9）。**对客户预付款（float）的依赖没有降低。**
3. **SRA 与积压（K-B）：结构改善，新签放缓。**
   - SRA 从 63 GW 降到 **58 GW**，原因是 13 GW 转为确定订单，不是取消。确定积压从 53 GW 升到 **64 GW**，首次超过 SRA。
   - 合计 122 GW，年末目标 ≥130 GW。已开始销售 2032 年交付位置。
   - 当季新签 11 GW，是过去 5 个季度的最低值。
   - **K-B 未触发。**
4. **燃机价格（K-A）：未触发。** 3Q 订单 $/kW 比 4Q25 高 20% 以上，全年约高 50%。
5. **数据中心与 hyperscaler（K-D）：未触发，但出现第一条裂缝。** 电气化数据中心订单环比约 −48%（$2.7B → $1.4B，推算），电气化 book-to-bill 降到 1.4。管理层原话："We expect the fourth quarter to, as it normally is, to be our largest quarter of orders in the year while growing our backlog, probably more in the fourth quarter than we did in the third quarter"。
6. **卡中引用的 2028 目标需更新（不改卡）。** 2026-01-28 的新闻稿（P）给出的 2028 年展望为：
   - 收入 $56B，原为 $52B。
   - 调整后 EBITDA 率 20%。
   - Power 和 Electrification 分部利润率均为 22%。
   - 累计 FCF ≥$24B。
   - 06-19 卡的 E27 仍是 2025-12 的 $52B 口径。

---

## 2. Siemens Energy（ENR.DE），财年截至 9 月，FQ4 FY26 将于 2026-11-11 发布

最新已发布的是 **FQ3 FY26**（2026 年 4–6 月），于 2026-08-05 发布。2026-09-30 召开了 FQ4 的 pre-close call，公司官网发布了文字稿。

| 季末（财季） | 集团订单 €m | 集团 B2B | 集团积压 | Gas Services 订单 €m（可比同比） | GS B2B | GS 积压 | GS 利润率（不含特殊项目） | Grid Tech 订单 €m（可比同比） | GT B2B | GT 积压 | GT 利润率（不含特殊项目） |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2024-12-31（FQ1 FY25） | 13,668 | — | — | 5,009 | — | — | — | 5,117 | — | — | — |
| 2025-03-31（FQ2 FY25） | 14,433 | — | — | 7,038 | — | — | — | 5,209 | — | — | — |
| 2025-06-30（FQ3 FY25） | 16,613 | — | — | 6,180 | — | — | 13.0% | 4,218 | — | — | 15.9% |
| 2025-12-31（FQ1 FY26） | 17,609 | 1.82 | €146bn | 8,751（+81.4%） | 2.83 | €60bn | 16.6% | 5,964（+21.8%） | 1.95 | €45bn | 17.6% |
| 2026-03-31（FQ2 FY26） | 17,749 | 1.72 | €154bn | 8,869（+32.4%） | 2.55 | €66bn | 15.9% | 6,996（+41.5%） | 2.28 | €49bn | 17.1% |
| **2026-06-30（FQ3 FY26）** | **17,926** | **1.57** | **€162bn** | **9,967（+61.9%）** | **2.65** | **€73bn** | **17.3%** | **5,367（+27.6%）** | **1.48** | **€51bn** | **19.9%** |

- 来源：各季 Earnings Release（P）。
- **燃机 GW**（FQ3 演示材料，P）：
  - 当季确定订单 15 GW，其中 12 GW 由 SRA 转化；发货 6 GW。
  - 客户承诺合计 95 GW：确定积压 69 GW，SRA 26 GW。
- pre-close call 中的燃机数据：
  - 前三季确定燃机订单约 40 GW，其中 Q3 为 15 GW。
  - 财年末承诺合计"trending towards ... approximately 100 gigawatts"。
  - 2030 年年交付能力目标约 30 GW。
- **数据中心表述（P）：**
  - GS FQ3："Demand from the U.S., including large orders related to data centers"。
  - 演示材料："Continued strong U.S. demand, especially for data center related gas turbines"。
  - GT FQ3："substantial growth in the transformer business including data center projects"。
  - pre-close call 给出了燃机市场规模的基础假设："annual market of around 110 to 120 gigawatts ... with a further 10 to 20 gigawatts of potential upside from data centers"。
  - pre-close call 也明确说："Data centers are an important additional driver, but they are not the foundation of our outlook"。
- **SRA 质量**（pre-close）：
  - SRA 通常约 6 个月内转为确定订单。
  - 原话："We have not seen any delays or cancellations of previously signed slot reservation agreements or orders"。

**放缓信号检查**

| 信号 | 结果 |
|---|---|
| 订单减速 | **有，且是公司自己预告的。** 原话："the fourth-quarter order intake is expected to be below the exceptionally strong levels of the first three quarters"。另外，Grid Tech FQ3 订单环比从 €7.0bn 降到 €5.4bn，pre-close 称 FQ4 没有 HVDC 大单。 |
| book-to-bill < 1 | 集团、GS、GT 都没有低于 1，但集团从 1.82 降到 1.57，GT 从 2.28 降到 1.48。Siemens Gamesa 曾低于 1（FQ2 为 0.33），与数据中心无关。 |
| 取消 / 推迟 | 未见，引语见上。 |
| 降价 | **燃机未见**，原话"Pricing in Gas Services remains very strong"。**电网设备涨价放缓**：欧洲受监管市场价格"stabilized at a high level"，今后"margin expansion will increasingly be driven by backlog conversion ... rather than further broad-based price increases"。 |

---

## 3. 三菱重工（MHI, 7011.T），FY2026 上半年（4–9 月）截至 10-30 尚未发布

IR 资料库最新是 **FY2026 Q1**（4–6 月）。往年上半年业绩在 11 月上旬发布。

| 期末 | 大型燃机订单（台 / GW） | 大型燃机在手（台 / GW） | GTCC 订单（¥bn） |
|---|---|---|---|
| FY24 全年（至 2025-03-31） | 25 台 / 11 GW | 48 台 / 21 GW | 1,474.4（全年） |
| FY25 Q1（至 2025-06-30） | 8 台 / 4 GW | 53 台 / 23 GW | 602.5 |
| FY25 Q2（至 2025-09-30） | 15 台（推算：上半年 23 台减 Q1 8 台） | 67 台 | — |
| FY25 Q3（至 2025-12-31） | 8 台（推算：前三季 31 台减上半年 23 台） | 75 台 | — |
| FY25 Q4（至 2026-03-31） | 4 台（推算：全年 35 台减前三季 31 台） | 74 台 / 33 GW | FY25 全年 2,652.6 |
| **FY26 Q1（至 2026-06-30）** | **10 台 / 4 GW**（美国 4 台、日本 6 台） | **80 台 / 35 GW** | **930.0** |

- 来源：fy20261q、fy20254q、fy20253q、fy20252q 各期演示材料附录，以及 fy20261q 的 Q&A（P）。
- FY26 预测：
  - GTCC 订单 ¥2,400bn，Q1 财报时从 2026-05-12 给出的 ¥2,300bn 上调，但仍低于 FY25 实际的 ¥2,652.6bn。
  - Energy Systems 订单 ¥3,550bn，低于 FY25 的 ¥3,936.7bn，同比 −¥386.7bn。
  - 公司原话："Strong order intake to continue primarily in GTCC despite YoY decline"。
- Q&A（P）：
  - "Order pricing has not declined, and the profitability of newly booked projects continues to improve gradually"。
  - Q1 订单的交付期"generally scheduled for delivery between 2028 and 2030"。
- 数据中心：Q1 材料只有"order intake particularly strong in North America and Asia"，**没有披露数据中心占比**。

**放缓信号检查**

| 信号 | 结果 |
|---|---|
| 订单减速 | 公司预测 FY26 的 GTCC 和 Energy Systems 订单同比下降，原因是基数高；季度订单波动大。 |
| 卖方疑虑 | Q&A 中有分析师提问"supply-demand conditions may begin to soften, particularly for small- and mid-sized gas turbines"。MHI 回答：大型燃机，特别是美国核心客户，"there has been no change in the strong supply-demand environment"。 |
| 取消 / 降价 | 未见。 |

---

## 4. Caterpillar（CAT），2026Q3 于 2026-10-29 发布

| 季末 | 总积压（$B） | 积压季增 | Power & Energy 销售 $m | 其中发电外部销售 $m | P&E 分部利润 $m（利润率，推算） |
|---|---:|---:|---:|---:|---|
| 2025-03-31 | — | — | 5,783 | 1,996 | 1,288（22.3%） |
| 2025-06-30 | — | — | 7,037 | 2,407 | 1,554（22.1%） |
| 2025-09-30 | 39.8 | — | 7,463 | 2,634 | 1,633（21.9%） |
| 2025-12-31 | 51.2 | +11.4 | — | — | — |
| 2026-03-31 | 62.7 | +11.5 | 7,031 | 2,817 | 1,450（20.6%） |
| 2026-06-30 | 72.1 | +9.4 | 8,238 | 3,098 | 2,027（24.6%） |
| **2026-09-30** | **约 78（S）** | **约 +5.9（推算）** | **8,784（+18%）** | **3,421（+30%）** | **2,143（24.4%）** |

- 来源：
  - 积压到 Q2 取自 10-Q 和 10-K（P）。
  - Q3 积压取自电话会转录稿（S）。CAT 的 Q3 10-Q 尚未提交，8-K 新闻稿只写了"record backlog"，没有给金额。
- P&E 口径：2026 年新闻稿给出的 2025 年对比数是重述后的 P&E 口径。2025Q4 旧口径（Energy & Transportation）不可比，因此留空。
- **P&E 分部积压：未披露。**
- **数据中心表述：**
  - Q3 新闻稿（P）："Sales increased mainly in turbines and turbine-related services and in large reciprocating engines, primarily in data center applications"。
  - 电话会（S）：
    - 发电业务对终端用户的销售 +75%。
    - "we're now taking some large reciprocating orders as far out as 2029 and turbine orders into 2030"。
    - "bringing additional capacity online is still the top pacing factor for growth in Power and Energy"。
    - 大型往复式发动机产能目标：到 2030 年约为 2024 年的 3 倍。

**放缓信号检查**

| 信号 | 结果 |
|---|---|
| 订单减速 | 积压仍在增长，但季增从 +11.5B、+9.4B 降到约 +5.9B（推算，S）。电话会称 58% 的积压在 12 个月内出货，上季为 59%。 |
| 指引 | 电话会（S）："In Power and Energy, we anticipate moderate sales growth in the fourth quarter versus the prior year as we lap a strong prior year fourth quarter and continue to ramp capacity"。销售增速受产能限制，不是需求问题。 |
| 取消 / 暂停 / 降价 | 未见。Q3 价格贡献为正，P&E +$216m。 |

---

## 5. Cummins（CMI），截至 10-30 Q3 尚未发布

EDGAR 上没有 Q3 的 8-K；去年 Q3 在 2025-11-06 发布。下表数据到 2026Q2。

| 季末 | Power Systems 销售 $m | 其中发电产品线 $m | 分部 EBITDA 率 |
|---|---:|---:|---:|
| 2025-03-31 | 1,649 | 1,001 | — |
| 2025-06-30 | 1,889 | 1,205 | — |
| 2025-09-30 | 1,996 | 1,280 | 22.9% |
| 2025-12-31 | 1,929 | 1,245 | 21.7% |
| 2026-03-31 | 1,956 | 1,283 | 29.5% |
| **2026-06-30** | **2,255（+19%）** | **1,536（+27%，推算）** | **24.5%** |

- 来源：新闻稿中的产品线表（P）。
- 积压和订单：**未披露。**
- 数据中心表述（P，2Q26 新闻稿）：
  - "robust customer orders for standby power for data centers"。
  - "demand for data center power generation remains robust"。
  - Power Systems："driven primarily by increased power generation demand, particularly for data center markets in the United States, China and Asia Pacific"。
  - FY26 收入指引上调到 +10–13%。
- **放缓信号：到 Q2 为止未见。Q3 待发布。**

---

## 6. Vertiv（VRT），2026Q3 于 2026-10-28 发布

| 季末 | 净销售 $m | 有机订单同比 | book-to-bill | 积压 | 流动递延收入 $m（XBRL） |
|---|---:|---|---|---|---:|
| 2025-06-30 | 2,638 | 约 +15% | 约 1.2x | $8.5B | 1,257.3 |
| 2025-09-30 | 2,676 | 约 +60% | 约 1.4x | $9.5B | 1,131.9 |
| 2025-12-31 | 2,880 | 约 +252% | 约 2.9x | $15.0B | 1,814.7 |
| 2026-03-31 | 2,650 | **未披露** | 未披露 | 未披露 | 2,461.8 |
| 2026-06-30 | 3,274 | **未披露** | 未披露 | 未披露 | 3,633.7 |
| **2026-09-30** | **4,313（+61%，有机 +55%）** | **>+100%** | **未披露** | **未披露** | **4,120.5** |

- 来源：各季新闻稿（P）；递延收入取自 XBRL 标签 `ContractWithCustomerLiabilityCurrent`（P）。
- Q4 指引有机 +49–51%；FY26 中值 $14.65B，有机 +38%。
- 电话会（S）：
  - Executive Chairman Cote："Orders are strong no matter how you look at them with or without Neocloud ... we are not planning to share orders data going forward"。
  - CEO 回答项目是否推迟："nothing out of the ordinary from what we have seen in the industry over the years"。
  - 积压口径："We do not call a capacity agreement a backlog"。

**放缓信号检查**

| 信号 | 结果 |
|---|---|
| 订单减速 | Q3 订单 >+100%，未见减速。 |
| 披露倒退 | **2026 年起不再给 backlog 和 book-to-bill**，现在又宣布今后不披露订单。这降低了 VRT 作为先行指标的价值。 |
| 预付放缓 | 递延收入季增从 Q2 的 +$1.17B 降到 Q3 的 **+$0.49B**（推算）。可能是交付加快消化了预付，不能单独解读为需求放缓。 |
| 暂停 / 取消 / 降价 | 未见。电话会称"expect positive price cost in 2026"。 |

---

## 7. Eaton（ETN），截至 10-30 Q3 尚未发布

EDGAR 上没有 Q3 的 8-K；多家日历网站称在 2026-11-03 发布，未经公司确认（S）。下表为 Electrical Americas（EA），数据到 2026Q2。

| 季末 | EA 积压 $m | 积压有机同比 | 订单有机同比（TTM） | book-to-bill（TTM） | EA 销售 $m | 公司总积压 |
|---|---:|---:|---:|---:|---:|---:|
| 2025-09-30 | 12,009 | +9% | +7% | 1.1 | 3,410 | $18.4B |
| 2025-12-31 | 13,246 | +19% | +16% | 1.2 | 3,506 | $19.8B |
| 2026-03-31 | 14,459 | +32% | +42% | 1.2 | 3,600 | $22.8B |
| **2026-06-30** | **15,175** | **+33%** | **+41%** | **1.3** | **3,951** | **$24.1B** |

- 来源：10-Q 和 10-K 的分部"Performance metrics"表（P）。
- 口径说明：2026 年分部重组，2025 年两期为旧口径。2026Q1 报告口径积压 +44%，含收购。
- **数据中心订单增速：未披露数字。** 2Q26 新闻稿原话："While data centers remain a key growth driver, we are benefiting from robust demand across our end markets"。

**放缓信号检查**

| 信号 | 结果 |
|---|---|
| 订单减速 | TTM 订单增速从 +42% 到 +41%，持平在高位。由于是 TTM 口径，单季拐点会被平滑，需看 Q3。 |
| book-to-bill / 积压 | book-to-bill 升至 1.3，积压有机 +33%。 |
| 取消 / 降价 | 未见。 |

---

## 8. Bloom Energy（BE），2026Q3 于 2026-10-22 发布

| 季末 | 收入 $m | 备注 |
|---|---:|---|
| 2025-03-31 | 326.0 | |
| 2025-06-30 | 401.2 | 取自 10-Q/A |
| 2025-09-30 | 519.0 | |
| 2025-12-31 | 777.7 | 推算：全年减前三季 |
| 2026-03-31 | 751.1 | |
| 2026-06-30 | 1,065.4 | 取自 10-Q/A |
| **2026-09-30** | **1,235.8（+138%）** | 毛利率 33.8% |

- 来源：XBRL 和 Q3 新闻稿（P）。
- FY26 收入指引 $4.4–4.6B，今年第三次上调。
- 客户订金：2025 年末 $78.2M，2026-09-30 为 **$661.4M**（P，10-Q）。10-Q 的解释是"new deposits associated with recently executed customer agreements"。
- 狭义 RPO（产品加安装）：$394.4M 增至 $661.2M（P）。**这不是商业意义上的积压。**
- **商业积压金额：未披露。** 电话会（S）："our backlog is continuing to expand faster than our revenue"。
- 仓库 09-28 卡记录的"2025 年末积压约 $20B"为二手来源，本次未找到一手出处。

**放缓信号检查**

- 收入、订金和指引全部向上。
- Q3 10-Q 风险因素中有以下表述（P）：
  - 纽约州 2026 年 7 月对新超大规模数据中心发布禁令，"Similar moratoriums have since been introduced in many other states"。
  - "Obtaining financing for data center development has generally become more difficult"。
  - "neoclouds, co-location service providers ... are also increasingly viewed as high credit risks"。
  - 若客户被视为高信用风险，"projects unable to obtain economical financing may be cancelled, margin pressure may increase as developers negotiate lower prices"。
- 同一份 10-Q 也写道："Despite recent increasing opposition to data center development, demand for our Energy Server systems ... has continued to be robust"。
- 我无法确认这些风险因素是不是 Q3 新增的，因为没有和 Q2 的 10-Q 逐字比对。

---

## 9. 选做：Schneider Electric 与 Hitachi Energy

- **Schneider，2026Q3，10-16 发布（全部为 S，未取到一手新闻稿）：**
  - 收入约 €11.5bn，有机约 +17%。另一家媒体给出的是报告口径 +17.9%、有机 +16.9%，两者有出入。
  - CFO 原话（据 Utility Dive）：数据中心"triple-digit demand growth"出现在"three out of the last four quarters"。
  - CFO 不拆分 neocloud 敞口；CEO 称"extremely careful to select those companies that will be there in the long term"。
- **Hitachi Energy：未覆盖。** 搜索只找到 Hitachi Energy India 2025 年的数据，日立集团 2026 年 7–9 月的数据未确认，不列入。

---

## 10. 跨公司小结：最新一季的方向

| 公司（最新季） | 订单 / 积压方向 | 数据中心占比（原话或数字） | 放缓信号 |
|---|---|---|---|
| GEV（2026Q3） | ↑↑ 订单 +96%，RPO $197B，122 GW | 燃机 GW 约 20% 为数据中心；电气化数据中心订单前三季超过 $6B | 电气化数据中心订单 $2.7B → $1.4B；新签 GW 降到 11 |
| Siemens Energy（FQ3） | ↑ 订单 €17.9bn，积压 €162bn | "not the foundation" | 公司预告 FQ4 订单低于前三季；GT 的 book-to-bill 降到 1.48 |
| MHI（FQ1） | ↑ 在手 80 台 / 35 GW | 未披露 | FY26 GTCC 订单预测同比下降 |
| CAT（2026Q3） | ↑ 积压约 $78B（S） | "primarily in data center applications" | 积压季增收窄到约 +5.9B；Q4 P&E 增速"moderate" |
| Cummins（2Q26） | ↑ Power Systems +19% | "robust ... for data centers" | Q3 未出 |
| Vertiv（2026Q3） | ↑↑ 订单 >+100% | 几乎全部为数据中心 | 停止披露订单 |
| Eaton（2Q26） | ↑ EA 积压 +33%，book-to-bill 1.3 | 定性："key growth driver" | TTM 订单增速持平；Q3 未出 |
| BE（2026Q3） | ↑ 收入 +138%，订金 ×8.5 | 主要为数据中心 | 风险因素：禁令、融资、neocloud 信用 |

---

## 11. 来源表

| id | 内容 | URL | 日期 | P/S |
|---|---|---|---|---|
| GEV_PR_3Q26 | GEV 3Q26 新闻稿（8-K EX-99） | https://www.sec.gov/Archives/edgar/data/1996810/000199681026000162/gevpressrelease3q26.htm | 2026-10-28 | P |
| GEV_10Q_3Q26 | GEV 3Q26 10-Q | https://www.sec.gov/Archives/edgar/data/1996810/000199681026000163/gev-20260930.htm | 2026-10-28 | P |
| GEV_PRES_3Q26 | GEV 3Q26 演示材料 | https://www.gevernova.com/sites/default/files/gev_webcast_presentation_10282026.pdf | 2026-10-28 | P |
| GEV_TR_3Q26 | GEV 3Q26 电话会文字稿（公司官网） | https://www.gevernova.com/sites/default/files/gev_webcast_transcript_10282026.pdf | 2026-10-28 | P |
| GEV_PR_2Q26 | GEV 2Q26 新闻稿 | https://www.sec.gov/Archives/edgar/data/1996810/000199681026000147/gevpressrelease2q26.htm | 2026-07-22 | P |
| GEV_TR_2Q26 | GEV 2Q26 电话会文字稿（公司官网） | https://www.gevernova.com/sites/default/files/gev_webcast_transcript_07222026.pdf | 2026-07-22 | P |
| GEV_PR_1Q26 | GEV 1Q26 新闻稿 | https://www.sec.gov/Archives/edgar/data/1996810/000199681026000063/gevpressrelease1q26.htm | 2026-04-22 | P |
| GEV_TR_1Q26 | GEV 1Q26 电话会文字稿（公司官网） | https://www.gevernova.com/sites/default/files/gev_webcast_transcript_04222026.pdf | 2026-04-22 | P |
| GEV_PR_4Q25 | GEV 4Q25 新闻稿（含 2028 年展望） | https://www.sec.gov/Archives/edgar/data/1996810/000199681026000012/gevpressrelease4q25.htm | 2026-01-28 | P |
| GEV_PR_3Q25 | GEV 3Q25 新闻稿 | https://www.sec.gov/Archives/edgar/data/1996810/000199681025000159/gevpressrelease3q25.htm | 2025-10-22 | P |
| GEV_XBRL | GEV XBRL companyfacts | https://data.sec.gov/api/xbrl/companyfacts/CIK0001996810.json | 抓取于 2026-10-30 | P |
| ENR_ER_Q3 | Siemens Energy FQ3 FY26 Earnings Release | https://p3.aprimocdn.net/siemensenergy/30018eed-275d-4e73-811e-b49d004cdc3d/2026-08-05-Earnings_Release_Q3_FY26_EN-pdf_Original%20file.pdf | 2026-08-05 | P |
| ENR_PRES_Q3 | Siemens Energy FQ3 分析师演示材料 | https://p3.aprimocdn.net/siemensenergy/3e846440-66dd-4a56-be75-b49d004e6741/2026-08-05_Q3_Analyst_presentation-pdf_Original%20file.pdf | 2026-08-05 | P |
| ENR_ER_Q2 | Siemens Energy FQ2 FY26 Earnings Release | https://p3.aprimocdn.net/siemensenergy/d38d682a-d64f-4f9e-b4fe-b4480041e5ea/2026-05-12-Earnings_Release_Q2_FY26_EN-pdf_Original%20file.pdf | 2026-05-12 | P |
| ENR_ER_Q1 | Siemens Energy FQ1 FY26 Earnings Release | https://p3.aprimocdn.net/siemensenergy/f8b7f2d2-e4f2-4fe5-8295-b3ee005765a4/2026-02-11_Earnings-Release-Q1-FY26-pdf_Original%20file.pdf | 2026-02-11 | P |
| ENR_PRECLOSE | Siemens Energy FQ4 FY26 pre-close call 文字稿（公司官网） | https://p3.aprimocdn.net/siemensenergy/e8ced7ab-8dcc-48e5-b0b5-b4d500fee9a5/2026-09-30---Q4-FY26-Pre-Close-Call_transcript-pdf_Original%20file.pdf | 2026-09-30 | P |
| MHI_PRES_1Q26 | MHI FY2026 Q1 演示材料 | https://www.mhi.com/finance/library/result/pdf/fy20261q/presentation.pdf | 2026-08 | P |
| MHI_QA_1Q26 | MHI FY2026 Q1 Q&A | https://www.mhi.com/finance/library/result/pdf/fy20261q/qa_20261q.pdf | 2026-08 | P |
| MHI_PRES_4Q25 | MHI FY2025 全年演示材料 | https://www.mhi.com/finance/library/result/pdf/fy20254q/presentation.pdf | 2026-05 | P |
| MHI_PRES_3Q25 | MHI FY2025 Q3 演示材料 | https://www.mhi.com/finance/library/result/pdf/fy20253q/presentation.pdf | 2026-02 | P |
| MHI_PRES_2Q25 | MHI FY2025 上半年演示材料 | https://www.mhi.com/finance/library/result/pdf/fy20252q/presentation.pdf | 2025-11 | P |
| CAT_ER_3Q26 | CAT 3Q26 新闻稿（EX-99.1） | https://www.sec.gov/Archives/edgar/data/18230/000001823026000052/ex991toformcat3q2026earnin.htm | 2026-10-29 | P |
| CAT_ER_2Q26 | CAT 2Q26 新闻稿 | https://www.sec.gov/Archives/edgar/data/18230/000001823026000040/ex991toformcat2q2026earnin.htm | 2026-08-04 | P |
| CAT_ER_1Q26 | CAT 1Q26 新闻稿 | https://www.sec.gov/Archives/edgar/data/18230/000001823026000017/ex991toformcat1q2026earnin.htm | 2026-04-30 | P |
| CAT_10Q_2Q26 | CAT 2Q26 10-Q（积压 $72.1B） | https://www.sec.gov/Archives/edgar/data/18230/000001823026000046/cat-20260630.htm | 2026-08-05 | P |
| CAT_10Q_1Q26 | CAT 1Q26 10-Q（积压 $62.7B） | https://www.sec.gov/Archives/edgar/data/18230/000001823026000021/cat-20260331.htm | 2026-05-06 | P |
| CAT_10K_FY25 | CAT FY25 10-K（积压 $51.2B） | https://www.sec.gov/Archives/edgar/data/18230/000001823026000008/cat-20251231.htm | 2026-02-13 | P |
| CAT_10Q_3Q25 | CAT 3Q25 10-Q（积压 $39.8B） | https://www.sec.gov/Archives/edgar/data/18230/000001823025000048/cat-20250930.htm | 2025-11-03 | P |
| CAT_TR_3Q26 | CAT 3Q26 电话会转录稿（Motley Fool） | https://www.fool.com/earnings/call-transcripts/2026/10/29/caterpillar-cat-q3-2026-earnings-call-transcript/ | 2026-10-29 | S |
| CMI_ER_2Q26 | Cummins 2Q26 新闻稿 | https://www.sec.gov/Archives/edgar/data/26172/000002617226000026/cmi2026q28-kex99.htm | 2026-08-04 | P |
| CMI_ER_1Q26 | Cummins 1Q26 新闻稿 | https://www.sec.gov/Archives/edgar/data/26172/000002617226000013/cmi2026q18-kex99.htm | 2026-05-05 | P |
| CMI_ER_4Q25 | Cummins 4Q25 新闻稿（2025 分季产品线表） | https://www.sec.gov/Archives/edgar/data/26172/000002617226000004/cmi2025q48-kex99.htm | 2026-02-05 | P |
| CMI_ER_3Q25 | Cummins 3Q25 新闻稿 | https://www.sec.gov/Archives/edgar/data/26172/000002617225000036/cmi2025q38-kex99.htm | 2025-11-06 | P |
| VRT_ER_3Q26 | Vertiv 3Q26 新闻稿 | https://www.sec.gov/Archives/edgar/data/1674101/000162828026067707/q32026exhibit991vrt10282026.htm | 2026-10-28 | P |
| VRT_ER_2Q26 | Vertiv 2Q26 新闻稿 | https://www.sec.gov/Archives/edgar/data/1674101/000162828026050323/q22026exhibit991vrt07292026.htm | 2026-07-29 | P |
| VRT_ER_1Q26 | Vertiv 1Q26 新闻稿 | https://www.sec.gov/Archives/edgar/data/1674101/000162828026026379/q12026exhibit991vrt04222026.htm | 2026-04-22 | P |
| VRT_ER_4Q25 | Vertiv 4Q25 新闻稿（积压 $15.0B，book-to-bill 2.9x） | https://www.sec.gov/Archives/edgar/data/1674101/000167410126000006/exhibit991vrt02112026.htm | 2026-02-11 | P |
| VRT_ER_3Q25 | Vertiv 3Q25 新闻稿（积压 $9.5B） | https://www.sec.gov/Archives/edgar/data/1674101/000167410125000020/q32025exhibit991vrt10222025.htm | 2025-10-22 | P |
| VRT_ER_2Q25 | Vertiv 2Q25 新闻稿（积压 $8.5B） | https://www.sec.gov/Archives/edgar/data/1674101/000167410125000006/q22025exhibit991vrt7302025.htm | 2025-07-30 | P |
| VRT_XBRL | Vertiv XBRL companyfacts | https://data.sec.gov/api/xbrl/companyfacts/CIK0001674101.json | 抓取于 2026-10-30 | P |
| VRT_TR_3Q26 | Vertiv 3Q26 电话会转录稿（Motley Fool） | https://www.fool.com/earnings/call-transcripts/2026/10/28/vertiv-vrt-q3-2026-earnings-call-transcript/ | 2026-10-28 | S |
| ETN_10Q_2Q26 | Eaton 2Q26 10-Q | https://www.sec.gov/Archives/edgar/data/1551182/000155118226000030/etn-20260630.htm | 2026-07-31 | P |
| ETN_10Q_1Q26 | Eaton 1Q26 10-Q | https://www.sec.gov/Archives/edgar/data/1551182/000155118226000013/etn-20260331.htm | 2026-05-05 | P |
| ETN_10K_FY25 | Eaton FY25 10-K | https://www.sec.gov/Archives/edgar/data/1551182/000155118226000007/etn-20251231.htm | 2026-02-26 | P |
| ETN_10Q_3Q25 | Eaton 3Q25 10-Q | https://www.sec.gov/Archives/edgar/data/1551182/000155118225000036/etn-20250930.htm | 2025-11-04 | P |
| ETN_ER_2Q26 | Eaton 2Q26 新闻稿 | https://www.sec.gov/Archives/edgar/data/1551182/000155118226000027/etn06302026exhibit99.htm | 2026-07-31 | P |
| ETN_ER_1Q26 / 4Q25 / 3Q25 | Eaton 各季新闻稿 | https://www.sec.gov/Archives/edgar/data/1551182/000155118226000010/etn03312026exhibit99.htm ；…/000155118226000002/etn12312025exhibit99.htm ；…/000155118225000033/etn09302025exhibit99.htm | 2026-05-05 / 2026-02-03 / 2025-11-04 | P |
| BE_ER_3Q26 | Bloom 3Q26 新闻稿 | https://www.sec.gov/Archives/edgar/data/1664703/000162828026066890/ex991_q326financialresults.htm | 2026-10-22 | P |
| BE_10Q_3Q26 | Bloom 3Q26 10-Q | https://www.sec.gov/Archives/edgar/data/1664703/000162828026066931/be-20260930.htm | 2026-10-22 | P |
| BE_XBRL | Bloom XBRL companyfacts | https://data.sec.gov/api/xbrl/companyfacts/CIK0001664703.json | 抓取于 2026-10-30 | P |
| BE_TR_3Q26 | Bloom 3Q26 电话会转录稿（Motley Fool） | https://www.fool.com/earnings/call-transcripts/2026/10/22/bloom-energy-be-q3-2026-earnings-call-transcript/ | 2026-10-22 | S |
| SU_UD_3Q26 | Schneider 3Q26 报道（Utility Dive） | https://www.utilitydive.com/news/schneider-electric-data-center-earnings/833358/ | 2026-10-19 | S |
