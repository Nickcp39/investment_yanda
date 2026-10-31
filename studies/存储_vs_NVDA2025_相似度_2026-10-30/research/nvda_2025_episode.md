# NVIDIA 2025 年 1–5 月「业绩强、股价跌」时刻档案（供与 MU / SNDK 逐季对比）

整理日 2026-10-30。标注规则：**[P#] = PRIMARY**（NVIDIA 新闻稿 / SEC 8-K、10-Q、10-K / 公司一手披露），**[S#] = SECONDARY**（媒体、数据商），**[D] = 自算**（算式写在旁边）。来源编号见 §7。股价一律为 Yahoo chart API 的拆股调整收盘价 [S1]（10:1 拆股 2024-06-10 生效，拆股前价格已 /10；未做股息调整，NVDA 每季 $0.01 股息可忽略）。

## 0. 摘要

- **业绩一直强，但“超预期幅度”在收窄**：Q1 FY25–Q3 FY26 七个季度营收全部高于指引中值，超幅 +8.5% → +7.3% → +7.9% → **+4.9%（Q4 FY25）→ +2.5%（Q1 FY26，H20 拖累）** → +3.9% → +5.6% [P1–P7][D]。低点前后两次财报环比仍 +12%，但下季指引环比只有 +9.3% 和 **+2.1%**（含约 $8.0B H20 收入损失）[P4][P5]。
- **毛利率在下行**：非GAAP GM 78.9%（Q1 FY25）→ 73.5%（Q4 FY25）→ 指引 71.0%（Q1 FY26）；Q1 FY26 含 $4.5B H20 计提实报 61.0%，不含 71.3% [P1][P4][P5]。原因是 Blackwell 系统级产品切换 + 一次性计提，不是售价下跌；管理层同时承诺年底回到 mid-70s，Q4 FY26 实报 75.2% 兑现 [P10e][P9]。
- **股价**：收盘高点 **2025-01-06 $149.43** → 收盘低点 **2025-04-04 $94.31（−36.9%）**；盘中低点 2025-04-07 $86.62（距 01-07 盘中高点 $153.13 为 −43.4%）[S1][D]。DeepSeek 日 2025-01-27 单日 −16.97%，市值蒸发约 $589B（Bloomberg）/ $593B（Reuters）[S1][S9]。
- **收复与之后**：2025-06-25 收盘 $154.31 首次站上前高——距低点 82 个日历日（55 个交易日），距高点 170 天。低点后 6 个月（2025-10-06）$185.54 = **+96.7%**；12 个月（2026-04-06）$177.64 = **+88.4%**；12 个月内最高收盘 2025-10-29 $207.04（+119.5%），随后又回撤 20.2% 到 2026-03-30 $165.17 [S1][D]。
- **低点时的空头逻辑**：H20 对华出口需许可（04-09 通知，04-15 8-K 称计提最多约 $5.5B）、对等关税、DeepSeek 算力效率、Blackwell 机柜过热/客户推迟订单、毛利率掉到 low-70s、TD Cowen 称微软退租约 2GW、客户集中 [P11][S2][S10][S11][S16][P13]。
- **同期客户 capex 不降反升**：1–2 月 MSFT FY25 约 $80B、META $60–65B、GOOGL 约 $75B、AMZN 约 $100B+（四家合计约 $320B）；4–5 月 META 上调到 $64–72B，GOOGL 重申 $75B，MSFT 称 FY26 仍增长但增速放缓 [P15][P16][S12–S15]。**需求端的一手指引没有坏，坏的是估值和情绪。**
- **估值几乎是唯一的变量**：前瞻 P/E 从 1 月约 34–37x 压到 4 月约 20.9–22.5x；跟踪 P/E 从约 59x 降到约 32x [S3][S4][S2][D]。同期共识 EPS 只小幅下修（Bloomberg：截至 04-21 的一个月内全年 EPS 共识 −1.5%）[S2]。事后看，FY26 实际 EPS $4.77 比 2025-05-28 的 Zacks 共识 $4.19 高 13.8% [P9][S6][D]。
- **结构上与存储不同**：NVDA 毛利率连续 12 个季度维持在 71–79%（一次性项目除外），价格由 NVDA 自己定，供给受 CoWoS 约束（“demand for Blackwell is expected to exceed supply for several quarters”）[P10c]。对比存储时可检验四点：①收入和指引是否仍环比增长；②毛利率下滑是成本/产品原因还是售价原因；③客户 capex 指引同期升还是降；④跌价期共识 EPS 是否基本没动。NVDA 2025 年四点都成立。

## 1. 季度表（Q1 FY25 – Q3 FY26，前后各加一行背景）

金额 $M（DC、库存、承诺为 $B）。QoQ / YoY / OPM 由营收和营业利润自算 [D]，与新闻稿四舍五入后的百分比一致。

| 季度 | 季末 | 报告日 | 营收 | QoQ | YoY | GM GAAP | GM 非GAAP | 非GAAP OPM | 非GAAP EPS | DC $B | 库存 $B | 存货/产能采购承诺 $B |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Q4 FY24（背景）| 2024-01-28 | 2024-02-21 | 22,103 | +22.0% | +265% | 76.0 | 76.7 | 66.7% | 0.516 | 18.4 | 5.28 | not fetched |
| Q1 FY25 | 2024-04-28 | 2024-05-22 | 26,044 | +17.8% | +262% | 78.4 | 78.9 | 69.3% | 0.612* | 22.56 | 5.86 | 18.8 |
| Q2 FY25 | 2024-07-28 | 2024-08-28 | 30,040 | +15.3% | +122% | 75.1 | 75.7 | 66.4% | 0.68 | 26.27 | 6.68 | 27.8 |
| Q3 FY25 | 2024-10-27 | 2024-11-20 | 35,082 | +16.8% | +94% | 74.6 | 75.0 | 66.3% | 0.81 | 30.77 | 7.65 | 28.9 |
| Q4 FY25 | 2025-01-26 | 2025-02-26 | 39,331 | +12.1% | +78% | 73.0 | 73.5 | 64.9% | 0.89 | 35.6 | 10.08 | 30.8 |
| Q1 FY26 | 2025-04-27 | 2025-05-28 | 44,062 | +12.0% | +69% | 60.5 | 61.0（不含 H20：71.3）| 52.8%（不含 H20：63.1%）| 0.81（不含 H20：0.96）| 39.1 | 11.33 | 29.8 |
| Q2 FY26 | 2025-07-27 | 2025-08-27 | 46,743 | +6.1% | +56% | 72.4 | 72.7（不含 H20 回冲：72.3）| 64.5% | 1.05 | 41.1 | 14.96 | 未单独披露（含非存货义务合计 45.8，上季 43.5）|
| Q3 FY26 | 2025-10-26 | 2025-11-19 | 57,006 | +22.0% | +62% | 73.4 | 73.6 | 66.2% | 1.30 | 51.2 | 19.78 | 50.3（“supply-related”）|
| Q4 FY26（背景）| 2026-01-25 | 2026-02-25 | 68,127 | +19.5% | +73% | 75.0 | 75.2 | not fetched | 1.62 | 62.3 | not fetched | 95.2（10-K，仅检索摘要）|

来源：营收、GM、营业利润、EPS、库存取自各季新闻稿 [P8][P1–P7][P9]；DC 精确值（Q1–Q3 FY25）和采购承诺取自 CFO Commentary [P10a–g]；Q3 FY26 承诺 $50.3B 另见 10-Q [P12]。*Q1 FY25 EPS 拆股前为 $6.12，/10 = 0.612。Q1 FY26 不含 H20 的 OPM = (23,275+4,538)/44,062 = 63.1% [D]。后续：总承诺 $119B（Q1 FY27）→ $279B（Q2 FY27），见 §6 [P14]。

## 2. 指引 vs 实际

| 季度 | 收入指引中值 | 实际 | 超中值 [D] | 非GAAP GM 指引中值 | 实际 | 差 | 下季收入指引中值 | 隐含下季环比 [D] | 下季 GM 指引 |
|---|---|---|---|---|---|---|---|---|---|
| Q1 FY25 | 24,000 [P8] | 26,044 | +8.5% | 77.0 | 78.9 | +1.9pt | 28,000 | +7.5% | 75.5 |
| Q2 FY25 | 28,000 | 30,040 | +7.3% | 75.5 | 75.7 | +0.2 | 32,500 | +8.2% | 75.0 |
| Q3 FY25 | 32,500 | 35,082 | +7.9% | 75.0 | 75.0 | 0.0 | 37,500 | +6.9% | 73.5 |
| Q4 FY25 | 37,500 | 39,331 | +4.9% | 73.5 | 73.5 | 0.0 | 43,000 | +9.3% | 71.0 |
| Q1 FY26 | 43,000 | 44,062 | +2.5%（加回未发货 $2.5B H20：+8.3%）| 71.0 | 61.0 / 71.3 | −10.0 / +0.3 | 45,000（含 −$8.0B H20）| +2.1% | 72.0 |
| Q2 FY26 | 45,000 | 46,743 | +3.9% | 72.0 | 72.7 / 72.3 | +0.7 / +0.3 | 54,000（不含 H20 对华）| +15.5% | 73.5 |
| Q3 FY26 | 54,000 | 57,006 | +5.6% | 73.5 | 73.6 | +0.1 | 65,000 | +14.0% | 75.0 |
| Q4 FY26（背景）| 65,000 | 68,127 | +4.8% | 75.0 | 75.2 | +0.2 | 78,000 | +14.5% | 75.0 |

算式示例：Q1 FY26 加回未发货 = (44,062+2,500)/43,000 − 1 = +8.3%；Q2 FY26 隐含环比 = 45,000/44,062 − 1 = +2.1%。指引均为 ±2% 收入、±50bp GM [P1–P9]。
LSEG 共识 EPS 超幅 [S7]：9.5%（Q1 FY25）→ 6.0% → 8.6% → 5.5% → 2.8%（Q1 FY26，按不含 H20 的 $0.96 对 $0.93）→ 4.2% → 4.0%（Q3 FY26）。Zacks 口径下 Q1 FY26 是“miss”（$0.81 vs $0.85），说明各家对 H20 的处理口径不同 [S6]。

## 3. 财报日股价反应 [S1][D]

NVDA 都在盘后发布，所以“报告日收盘”就是发布前的价格，反应 = T+1 收盘 / 报告日收盘 − 1。52 周高点按此前 365 个日历日的最高收盘价计算。

| 季度 | 报告日 | T−1 收盘 | 报告日收盘 | T+1 收盘 | T+1 反应 | 距 52 周收盘高点（高点日）|
|---|---|---|---|---|---|---|
| Q4 FY24 | 2024-02-21 | — | 67.47 | 78.54 | +16.41% | −8.7%（73.90, 02-14）|
| Q1 FY25 | 2024-05-22 | 95.39 | 94.95 | 103.80 | +9.32% | −0.5%（95.39, 05-21）|
| Q2 FY25 | 2024-08-28 | 128.30 | 125.61 | 117.59 | −6.38% | −7.4%（135.58, 06-18）|
| Q3 FY25 | 2024-11-20 | 147.01 | 145.89 | 146.67 | +0.53% | −2.0%（148.88, 11-07）|
| **Q4 FY25** | **2025-02-26** | 126.63 | 131.28 | 120.15 | **−8.48%** | **−12.1%（149.43, 2025-01-06）**|
| **Q1 FY26** | **2025-05-28** | 135.50 | 134.81 | 139.19 | **+3.25%** | −9.8%（149.43）|
| Q2 FY26 | 2025-08-27 | 181.77 | 181.60 | 180.17 | −0.79% | −0.9%（183.16, 08-12）|
| Q3 FY26 | 2025-11-19 | 181.36 | 186.52 | 180.64 | −3.15% | −9.9%（207.04, 10-29）|
| Q4 FY26 | 2026-02-25 | 192.85 | 195.56 | 184.89 | −5.46% | −5.5%（207.04）|

规律：从 Q2 FY25 起，即使收入超指引，次日反应多数为负（7 次里 5 次）。离低点最近的 Q1 FY26 报告（坏消息最多：H20 计提，指引里扣掉 $8.0B）反而次日 +3.25%，属于“利空出尽”。

## 4. 2025 年 1–5 月这段行情

### 4.1 时间线（价格来自 [S1]）
| 日期 | 事件 | 收盘 / 涨跌 |
|---|---|---|
| 2025-01-03 | 微软：FY25 将投约 $80B 建 AI 数据中心 [P16] | — |
| **2025-01-06** | **收盘历史新高**，市值约 $3.66T [S20] | **$149.43** |
| 2025-01-07 | 盘中高点 $153.13 后回落 | $140.14（−6.2%）|
| 2025-01-13 | The Information/Reuters：MSFT、AWS、Google、Meta 削减部分 GB200 机柜订单，原因是过热和互连故障 [S10] | — |
| **2025-01-27** | **DeepSeek 日** | **$118.42（−16.97%）** |
| 2025-02-24 | TD Cowen：微软取消约“几百 MW”租约 [S11] | — |
| 2025-02-26 | Q4 FY25 财报：超指引 4.9%，GM 指引降到 71.0% [P4] | 次日 $120.15（−8.48%）|
| 2025-03-26 | TD Cowen：微软 6 个月内在美欧放弃约 2GW 项目 [S11] | — |
| 2025-04-03 / 04 | 对等关税公布后连续两天下跌 | −7.81% / −7.36% |
| **2025-04-04** | **收盘低点** | **$94.31** |
| 2025-04-07 | **盘中低点 $86.62** | $97.64 |
| 2025-04-09 | 美国政府通知 H20 出口需许可 [P11]；同日关税暂停 90 天 | $114.33（+18.72%）|
| 2025-04-14 | 美国政府称许可要求无限期有效 [P11] | — |
| 2025-04-15 盘后 | 8-K：Q1 FY26 预计计提“最多约 $5.5B”（H20 库存、采购承诺、准备金）[P11] | 04-16：$104.49（−6.87%）|
| 2025-04-21 | 二次探底；Bloomberg：约 21 倍预期盈利 [S2] | $96.91（−4.51%）|
| 2025-05-28 | Q1 FY26：实际计提 $4.5B（少于预警的 $5.5B），Q1 另有 $2.5B H20 未能发货，Q2 指引扣掉约 $8.0B [P5] | 次日 $139.19（+3.25%）|
| 2025-06-25 | 首次收盘站上前高 | $154.31 |

2025 年月末收盘：1 月 120.07｜2 月 124.92｜3 月 108.38｜4 月 108.92｜5 月 135.13｜6 月 157.99｜7 月 177.87 [S1]。
跌幅 [D]：收盘对收盘 94.31/149.43 − 1 = −36.9%；盘中对盘中 86.62/153.13 − 1 = −43.4%。低点后 1 个月（05-05）$113.82（+20.7%），3 个月（07-07）$158.24（+67.8%），6 个月 +96.7%，12 个月 +88.4%。

### 4.2 低点时的空头逻辑
1. **出口管制 / H20**：Q1 FY26 计提 $4.5B，Q1 未发货 $2.5B，Q2 少收约 $8.0B [P5]。
2. **关税 / 衰退**：贸易战前景不明，电子产品豁免只是临时的，衰退会拖累盈利预期 [S2]。
3. **DeepSeek 效率**：担心算力需求被压缩 [S9]。
4. **Blackwell 爬坡**：GB200 机柜过热、客户推迟订单 [S10]；Q2 FY25 因低良率材料计提库存准备并改了光罩 [P10b]。
5. **毛利率下滑**：Kress 2025-02-26 称爬坡期 GM 在“low 70s”，年底回到“mid-70s”[S16]。
6. **Digestion / capex 见顶**：微软退租 [S11]；超大规模厂商需求可能“slow down on the margins”，2026 年 capex 存疑 [S2]。
7. **客户集中**：FY25 三家直接客户占收入 12%、11%、11%，另有一家间接客户估计 ≥10% [P13]；大型 CSP 约占 DC 收入 45–50% [P10a–d]。

### 4.3 同期超大规模厂商的 capex 指引
| 公司 | 2025 年 1–2 月 | 2025 年 4–5 月 | 方向 |
|---|---|---|---|
| MSFT | 01-03：FY25（截至 2025 年 6 月）约 $80B [P16] | 04-30：FY26 capex 继续增长，但增速低于 FY25 [S14]；同期有 TD Cowen 退租报告 [S11] | 维持，增速放缓 |
| GOOGL | 02-04：2025 年约 $75B（市场原先预期约 $58–60B）[S12] | 04-24：重申约 $75B [S13]（7 月再上调到 $85B）| 维持 → 后来上调 |
| META | 01-24/29：$60–65B [S12] | 04-30：**上调到 $64–72B**（前次 $60–65B）[P15] | 上调 |
| AMZN | 02-06：Q4 capex $26.3B，“reasonably representative” 2025 年节奏（约 $100B+）[S15] | 05-01：Q1 capex 约 $24.3B，同比 +74% [S15] | 维持 |

四家 2025 年计划合计约 $320B（2024 年约 $246B）[S12]。

## 5. 低点估值与共识预期修正

| 指标 | 2025-01-06 高点（$149.43）| 2025-04-04 低点（$94.31）|
|---|---|---|
| 跟踪 P/E（GAAP，按已报告 TTM）[D] | 149.43 / 2.541 = **58.8x**（2.541 = Q4 FY24 0.493 + Q1 0.598 + Q2 0.67 + Q3 0.78）| 94.31 / 2.94（FY25）= **32.1x** |
| 跟踪 P/E（非GAAP）[D] | 149.43 / 2.618 = 57.1x（0.516 + 0.612 + 0.68 + 0.81）| 94.31 / 2.99 = 31.5x |
| 媒体引用的前瞻 P/E | **34x** “next year's expected earnings”，59x 跟踪（Fool，2025-01-06/07）[S4]；Zacks 36.58x（日期未核实）| **20.9x**（Fool 04-08，数据来自 YCharts）[S3]；**21x**（Bloomberg 04-21，股价约 $97）[S2] |
| 用当时共识算的前瞻 P/E [D] | Jan 共识 not found | 94.31 / 4.19（Zacks 2025-05-28 的 FY26 共识，≈ NTM）= **22.5x**；盘中低点 86.62 / 4.19 = 20.7x |
| “事后” NTM P/E（用实际非GAAP EPS）[D] | 149.43 / 4.05 = **36.9x**（0.89 + 0.81 + 1.05 + 1.30；用不含 H20 的 0.96 则 35.6x）| 94.31 / 4.77（FY26 实际）= **19.8x** |

- **压缩幅度** [D]：事后口径 19.8/36.9 − 1 = −46%；媒体口径 21/34 − 1 = −38%。股价跌了 36.9%，而同期共识 EPS 只是小幅下修，所以**跌幅基本都来自估值压缩**。另有 MarketWatch/FactSet 口径的跟踪 P/E：01-27 为 40.3x，用的是含估计值的 CY2024 EPS [S8]。
- **共识修正的方向（能找到的部分）**：
  - Bloomberg 04-21：全年 EPS 共识一个月内 −1.5%，收入共识 −1.2% [S2]。
  - Zacks：财报前修正趋势为“mixed”；FY26 共识 EPS $4.19、收入 $193.52B（2025-05-28）[S6]。
  - 此后一路上修：FY26 实际 EPS $4.77 [P9]，比 5-28 的共识高 13.8%（4.77/4.19 − 1）[D]；实际收入 $215,938M（44,062 + 46,743 + 57,006 + 68,127）比共识高 11.6% [D]。
  - **2025 年 1 月时的 FY26 共识：not found**（Wayback 存档页被机器人拦截）。

## 6. 毛利率与定价结构（用来对比存储的价格周期）

- **非GAAP GM 序列** [P]：Q3 FY24 75.0｜Q4 FY24 76.7｜Q1 FY25 78.9｜Q2 75.7｜Q3 75.0｜Q4 73.5｜Q1 FY26 61.0（不含 H20：71.3）｜Q2 72.7（72.3）｜Q3 73.6｜Q4 FY26 75.2｜Q1 FY27 75.0｜Q2 FY27 75.0 [P14]。剔除一次性项目后，12 个季度落在 **71.3–78.9%** 的区间。
- **下滑原因都是成本和产品组合，不是售价** [P10]：Q2 FY25“Blackwell 低良率材料的库存准备”；Q3 FY25 从 H100 转向“更复杂、成本更高的系统”；Q4 FY25 同上；Q1 FY26 是 H20 计提加系统初期爬坡；Q3 FY26 恢复，理由是“improved mix and cost structure”。下滑和回升都提前给了指引，并且兑现（Q2 FY25 起实际与指引中值相差 ≤0.3pt，剔除 H20 项目）。
- **供给受限**：Q3 FY25 CFO 称“Both Hopper and Blackwell systems have certain supply constraints”，以及“demand for Blackwell is expected to exceed supply for several quarters in fiscal 2026” [P10c]。Q3 FY26 黄仁勋说“Blackwell sales are off the charts, and cloud GPUs are sold out” [P7]。TrendForce：NVIDIA 占 2025 年 CoWoS 需求 60% 以上，据报锁定了台积电 2025 年 70% 以上的 CoWoS-L 产能 [S17]。
- **库存周转**：DSI 95 → 81 → 78 → 86 → 59 天（Q1 FY25 → Q1 FY26）[P10a–e]。库存从 $5.9B 增到 $19.8B（Q3 FY26），增速大致与收入同步（Q2–Q3 FY26 未披露 DSI）。
- **集中度在上升**：Q3 FY26 四家直接客户分别占 22%、15%、13%、11% [P12]（FY25 为 12%、11%、11% [P13]）。
- **与存储的对照**：NVDA 的 GM 由自己的产品切换节奏决定，定价权在 NVDA；存储的 GM 由 DRAM/NAND 合约价决定，跌价期共识 EPS 往往被大幅下修，这正是 NVDA 2025 年**没有**发生的事。另外 NVDA 本身是存储的大买家：总承诺从 $119B 增到 $279B，公司称主要用于采购存储 [P14]。

## 7. 来源

PRIMARY（均于 2026-10-30 抓取）
- [P1–P9] NVIDIA 财报新闻稿，URL = `https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-` + 后缀：P1 Q1 FY25（2024-05-22）`first-quarter-fiscal-2025`｜P2 Q2 FY25（2024-08-28）`second-quarter-fiscal-2025`｜P3 Q3 FY25（2024-11-20）`third-quarter-fiscal-2025`｜P4 Q4 FY25（2025-02-26）`fourth-quarter-and-fiscal-2025`｜P5 Q1 FY26（2025-05-28）`first-quarter-fiscal-2026`｜P6 Q2 FY26（2025-08-27）`second-quarter-fiscal-2026`｜P7 Q3 FY26（2025-11-19）`third-quarter-fiscal-2026`｜P8 Q4 FY24（2024-02-21）`fourth-quarter-and-fiscal-2024`（另：Q3 FY24 `third-quarter-fiscal-2024`、Q2 FY24 `second-quarter-fiscal-2024`）｜P9 Q4 FY26（2026-02-25）`fourth-quarter-and-fiscal-2026`
- [P10a–g] CFO Commentary（8-K Ex.99.2），前缀 https://www.sec.gov/Archives/edgar/data/1045810/ ：a 000104581024000113/q1fy25cfocommentary.htm｜b 000104581024000262/q2fy25cfocommentary.htm｜c 000104581024000315/q3fy25cfocommentary.htm｜d 000104581025000021/q4fy25cfocommentary.htm｜e 000104581025000115/q1fy26cfocommentary.htm｜f 000104581025000207/q2fy26cfocommentary.htm｜g 000104581025000228/q3fy26cfocommentary.htm
- [P11] 8-K 2025-04-15（报告期 2025-04-09，H20）https://www.sec.gov/Archives/edgar/data/1045810/000104581025000082/nvda-20250409.htm
- [P12] 10-Q Q3 FY26 https://www.sec.gov/Archives/edgar/data/1045810/000104581025000230/nvda-20251026.htm
- [P13] 10-K FY25 https://www.sec.gov/Archives/edgar/data/1045810/000104581025000023/nvda-20250126.htm
- [P14] Q2 FY27 CFO Commentary（2026-08）https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000073/q2fy27cfocommentary.htm
- [P15] Meta Q1 2025 PR 2025-04-30 https://investor.atmeta.com/investor-news/press-release-details/2025/Meta-Reports-First-Quarter-2025-Results/default.aspx
- [P16] Microsoft “The Golden Opportunity for American AI”（Brad Smith），2025-01-03 https://blogs.microsoft.com/on-the-issues/2025/01/03/the-golden-opportunity-for-american-ai/

SECONDARY
- [S1] Yahoo Finance chart API，NVDA 日线（抓取于 2026-10-30）https://query1.finance.yahoo.com/v8/finance/chart/NVDA
- [S2] Bloomberg “Nvidia Investors Balk at Beaten Down Valuation as Risks Mount”，2025-04-21（Tiger 转载）https://itiger.com/hant/news/1199176621
- [S3] Motley Fool，2025-04-08 https://www.fool.com/investing/2025/04/08/is-nvidia-severly-affected-by-president-trumps-tar
- [S4] Motley Fool AU，2025-01-07（原文发于 Fool.com 2025-01-06）http://www.fool.com.au/2025/01/07/why-the-nvidia-share-price-just-rallied-to-a-record-high/
- [S6] Zacks via Finviz “Nvidia (NVDA) Q1 Earnings Miss Estimates”，2025-05-28 https://finviz.com/news/68495/nvidia-nvda-q1-earnings-miss-estimates
- [S7] Reuters/LSEG 财报前瞻，2026-02-24（Tiger 转载）https://www.itiger.com/hans/news/2613307737
- [S8] MarketWatch（Dow Jones），2025-01-28，FactSet 数据 https://itiger.com/news/2506511976
- [S9] Bloomberg 2025-01-27 https://www.bloomberg.com/news/articles/2025-01-27/asml-sinks-as-china-ai-startup-triggers-panic-in-tech-stocks ；Reuters $593B（Business Standard 转载）https://www.business-standard.com/amp/markets/news/deepseek-sparks-ai-stock-selloff-nvidia-loses-record-593-bn-in-mcap-125012800095_1.html
- [S10] Reuters 转述 The Information，2025-01-13 https://thestar.com.my/tech/tech-news/2025/01/13/nvidia039s-biggest-customers-delaying-orders-of-latest-ai-racks-the-information-reports
- [S11] DCD 关于 TD Cowen 报告（2025-02-24 / 03-26）https://datacenterdynamics.com/en/news/microsoft-cancels-up-to-2gw-of-data-center-projects-says-td-cowen
- [S12] TheWrap，2025 年 2 月 https://www.thewrap.com/meta-google-microsoft-amazon-spend-big-on-ai-2025
- [S13] Alphabet 重申 $75B 的报道 https://www.verdict.co.uk/alphabet-75bn-ai-2025/ （内容仅来自检索摘要）
- [S14] SiliconANGLE，2025-04-30 https://siliconangle.com/?p=694654
- [S15] Motley Fool，2025-02-09 https://www.fool.com/investing/2025/02/09/100-billion-reasons-to-buy-amazon-stock-hand-over ；SiliconANGLE，2025-05-01 https://siliconangle.com/?p=694892
- [S16] Fortune，2025-02-26 https://fortune.com/2025/02/26/nvidia-earnings-call-stock-market-investors-expectations-wall-street/
- [S17] TrendForce，2025-02-24 https://www.trendforce.com/news/2025/02/24/news-tsmc-reportedly-sees-cowos-order-surge-with-nvidia-securing-70-of-2025-cowos-l-capacity/
- [S20] Reuters，2025-01-06（WHBL 转载）https://whbl.com/2025/01/06/nvidia-ceo-set-to-take-stage-at-ces-just-after-shares-hit-record-high/

## 8. 未核实 / 缺口

- 2025 年 1 月（高点时）的 FY26 共识 EPS：not found。Zacks 的 36.58x 前瞻 P/E 无法确认日期（页面被机器人拦截）。Barchart 的 24x / 26.6x 未打开原文。
- Q4 FY24 和 Q3 FY24 的同比用的是上年营收 6,051 和 5,931，这两个数没有重新抓取，只核对了与新闻稿的 +265%、+206% 一致。
- Q2 FY26 的存货/产能承诺没有单独披露。二手转录称 Q3 电话会说“supply commitments +63% QoQ”，倒推 50.3/1.63 ≈ $30.9B，未核实。FY26 10-K 的 $95.2B 仅来自检索摘要；Q1 FY27 的 $119B 已由 [P14] 确认。
- [S13]（GOOGL 04-24 重申）和 [S15]（AMZN Q1 $24.3B）基于二手摘要，未读到电话会原文。拜登 AI Diffusion Rule（2025-01-13）在本次检索中未核实，所以没有列入时间线。
- Q4 FY25–Q3 FY26 的 DC 收入只有新闻稿里四舍五入后的 $B 数。Q4 FY26 的非GAAP 营业利润和库存未抓取。
- 第 3 节的 52 周高点用收盘价计算；用盘中高点会略有不同（例如 2025-01-07 盘中 $153.13）。
