# MSFT Raw Extracts (primary-source摘录)

取数日期: 2026-06-19 · 来源见 `../source_register.md`

> 本文件存一手数据的结构化摘录(XBRL companyconcept API 拉的审计序列 + 官方 IR 财报口径)。每块标 source_id。SEC 全文 10-K/10-Q 段注未逐字下载本轮(403 + 时间),用 XBRL 聚合值 + IR press release 替代;标注于 source_register fetch note。

---

## Block 1 — 10 年财务序列 (SEC XBRL, CIK 0000789019, FY end 6/30) [MSFT-XBRL-FACTS]

| FY (end 6/30) | Revenue $B | Op income $B | Op margin | Net income $B | OCF $B | Capex $B | Buyback $B | Dividend $B |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 2016 | 91.2 | 26.1 | 28.6% | 20.5 | — | — | — | — |
| 2017 | 96.6 | 29.0 | 30.0% | 25.5 | — | — | — | — |
| 2018 | 110.4 | 35.1 | 31.8% | 16.6* | 43.9 | 11.6 | 10.7 | 12.7 |
| 2019 | 125.8 | 43.0 | 34.2% | 39.2 | 52.2 | 13.9 | 19.5 | 13.8 |
| 2020 | 143.0 | 53.0 | 37.1% | 44.3 | 60.7 | 15.4 | 23.0 | 15.1 |
| 2021 | 168.1 | 69.9 | 41.6% | 61.3 | 76.7 | 20.6 | 27.4 | 16.5 |
| 2022 | 198.3 | 83.4 | 42.1% | 72.7 | 89.0 | 23.9 | 32.7 | 18.1 |
| 2023 | 211.9 | 88.5 | 41.8% | 72.4 | 87.6 | 28.1 | 22.2 | 19.8 |
| 2024 | 245.1 | 109.4 | 44.6% | 88.1 | 118.5 | 44.5 | 17.3 | 21.8 |
| 2025 | 281.7 | 128.5 | 45.6% | 101.8 | 136.2 | 64.6 | 18.4 | 24.1 |

\* FY2018 net income depressed by one-time ~$13.7B tax charge (TCJA repatriation); pre-tax trend intact.

**读数**:
- 10 年营收 91.2→281.7B = ~3.1×,CAGR ~12%;营业利润率从 28.6% 升到 45.6%(运营杠杆 + mix 转云)。
- **capex 拐点**:FY23 28.1B → FY24 44.5B → FY25 64.6B(两年翻 2.3×),AI 数据中心军备竞赛,与 GOOGL 同因子。
- **资本回报转向**:buyback 从 FY22 峰值 32.7B 降到 FY25 18.4B(为 capex 让路);dividend 单调上升(连续 20+ 年增派,本轮 24.1B)。
- FCF FY25 = 136.2 − 64.6 = **71.6B**;FCF/净利 ~70%(capex 在吃 FCF,但未吃到负)。

---

## Block 2 — 最新季度 Q3 FY2026 (qtr end 2026-03-31) [MSFT-Q3-2026-ER / -PERF]

- 总营收 **$82.9B,+18% YoY (+15% 不变汇率)**
- 营业利润 **$38.4B,+20% YoY**;营业利润率 **46.3%**
- 净利 **$31.8B,+23% YoY**;摊薄 EPS **$4.27,+23% YoY**
- 分部:
  - Productivity & Business Processes **$35.0B,+17% (+13% cc)** — M365 / Copilot / LinkedIn / Dynamics
  - Intelligent Cloud **$34.7B,+30% (+28% cc)** — Azure / server products
  - More Personal Computing **$13.2B,−1% (−3% cc)** — Windows / devices / search / gaming
- **Azure & other cloud services +40% YoY (+39% cc)** — 超管理层 37–38% 指引,逆转此前多季减速
- **Microsoft Cloud 营收 $54.5B,+29% (+25% cc)** — 单季首破 $50B
- **Commercial RPO(剩余履约义务)$627B,+99% YoY** — 巨额已签约未确认订单
- **AI 业务年化 run-rate 超 $37B,+123% YoY** [A1 IR, MSFT-Q3-2026-PERF]

---

## Block 3 — FY26 YTD (9 个月, 2025-07-01→2026-03-31) [MSFT-XBRL-FACTS]

- 营收 $241.8B(vs 9mFY25 $205.3B,**+17.8% YoY**)
- 营业现金流 $127.5B
- capex(PP&E 购置)$80.1B → 年化 ~$107B(纯 PP&E,不含融资租赁产能)
- TTM(推算):营收 $318.3B · 净利 $125.2B · OCF $170.2B · capex $97.3B · **FCF $72.9B** · capex/OCF ~57%

> **口径差异(重要)**:电话会 FY26 capex 指引 ~$190B 含**融资租赁/leased 数据中心产能**;XBRL 现金流量表的 PP&E 现金购置 9mo 仅 $80.1B(年化 ~$107B)。两个口径都对,但**不能混用** — $190B 是"含租赁的总产能投入承诺",$107B 是"自有 PP&E 现金支出"。FCF 用后者算。[reliability_note]

---

## Block 4 — 资产负债表 (2026-03-31) [MSFT-XBRL-FACTS]

- 现金及等价物 $32.1B + 短期投资 $46.2B = **$78.3B 流动性**
- 长期债务(非流动)$31.4B(从 FY24 $42.7B 持续下降)
- 股东权益 $414.4B
- **净现金 ~$47B**(不含其他长期负债/经营租赁);资产负债表稳健,非加杠杆做 capex(对比 GOOGL 净发债融资 capex)

---

## Block 5 — 股本与资本回报 [MSFT-XBRL-FACTS / MSFT-PROXY-2025]

- 流通股 ~7.428B(2026-04-23 cover date);多年缓慢回购净减(无大规模稀释)
- buyback + dividend 双轨;Q3 FY26 单季返还股东 ~$10.2B
- **一股一票,无双层股权,无创始人投票控制**(Gates/Ballmer 已大幅退出;治理为标准 one-share-one-vote)— 与 GOOGL/META 创始人控制结构形成鲜明对照

---

## Block 6 — 经营者 [MSFT-PROXY-2025 / 公开]

- CEO **Satya Nadella**(2014-02 上任,2021 起兼董事长);FY25 总薪酬 ~$96.5M(~90% 股权挂钩,+22% YoY 随股价)
- CFO **Amy Hood**(2013 起);长任期、口径稳定、纪律性强(运营杠杆兑现的执行者)
- 董事会:独立多数;2025 提名 Walmart CFO John David Rainey 入board;2025 proxy 有 AI 风险相关股东提案
