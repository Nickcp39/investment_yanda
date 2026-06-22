# NVDA Financial Quality (M4) — as_of 2026-06-19

来源: FY26 10-K [S003] / Q4FY26 PR [S004] / Q1 FY27 PR+CFO [S001/S002]。模型见 `model/*.csv`。

## 1. 盈利能力与趋势
- **营收轨迹**: FY24 $60.9B → FY25 $130.5B → FY26 $215.9B（+65%）→ Q1 FY27 run-rate $81.6B/季（年化 ~$326B，且环比仍 +20%）。三年 ~10x，由 Data Center 单引擎驱动。
- **毛利率**: FY23 56.9%（gaming/crypto 下行年）→ FY24 74.99% → FY26 71.1% → Q1 FY27 74.9%。Blackwell 放量后回到 ~75%，定价权强。
- **营业利润率**: Q1 FY27 GAAP 营业利润 $53.5B / 营收 $81.6B = **65.6%**。极高经营杠杆。
- **净利质量警告**: Q1 GAAP 净利 $58.3B > 营业利润 $53.5B，差额主要为**可交易股权证券公允价值收益**（头寸 $30.2B，季内从 $12.9B 翻倍）→ **GAAP 净利被非经营性收益放大**，看估值应用 non-GAAP（EPS $1.87）或经营 owner earnings。

## 2. 现金流与 owner earnings 桥
- Q1 FY27: OCF $50.34B − capex $1.76B = **FCF $48.55B**（FCF/OCF 96%）。
- FY26: OCF ~$102.7B − capex $6.1B = **FCF ~$96.6B**（B1 近似，待 10-K 核）。
- **owner earnings ≈ FCF**（与 GOOGL 截然相反）: capex/营收 FY26 仅 ~2.8%，维护性 capex 极低，无"增长 capex 吃掉 owner earnings"问题。NVDA 是 **capex-light、研发驱动**（研发是费用化、即时计入），owner earnings 与报表自由现金流高度一致——但应从 GAAP 净利中**剔除股权证券收益**，得经营性 owner earnings ≈ non-GAAP 净利 ≈ $45–46B/季 run-rate（年化 ~$180–185B）。

## 3. 资产负债表
- 净现金 ~$72B（现金+证券 $80.6B − 债务 $8.47B）→ **fortress**，可存活任何 AI capex 周期回撤。
- 存货升至 $25.8B（vs $21.4B 上季）→ Blackwell 备货；需监控若需求软化的库存/承诺减值风险（参 FY26 曾有 $4.5B H20 计提先例）。
- 股本: 稀释股 24,391M，回购 + $80B 新授权 → 股本由"增发稀释"转为"净回购"（与 GOOGL 回购归零相反）。

## 4. 三情景（owner earnings 起点用经营性 ~$180B 年化，剔除股权收益）
见 `model/scenario_model.csv`。要点:
- **Bull**: AI 推理需求长期化 + 份额守住 + 网络/系统扩 TAM；owner earnings 5y CAGR 高、退出倍数维持 → 现价隐含 IRR 高（>15%）。
- **Base**: 增速从 +85% 大幅减速到稳态、毛利率从 75% 回落到 ~65–68%（custom silicon 竞争）、China 永久损失 → 仍正增长，现价 P/E ~16–19x forward 留有边际，IRR ~10–14%。
- **Bear**: AI capex pull-forward 兑现、DC 需求 air-pocket（一两季回撤）、custom silicon 抢推理份额、毛利率压到 55–60% → owner earnings 阶段性腰斩，de-rate；现价下行 −40–55%（向 52 周低破位）。**但资产负债表存活，非永久减值。**

## 5. 与 2023 盲测案对照（关键差异）
- 2023-05-25: ~$0.94T、trailing GAAP P/E ~198x、forward 不可导出、DC 刚 inflect（季 $4.28B）、Gaming −38%。**估值是 air-pocket 风险主因**。
- 2026-06-19: ~$3.55T、trailing GAAP P/E ~30x、**forward ~16–19x**、DC 已 $75B/季并经多季验证、资产负债表更厚、回购+股息上调。**估值起点远低于 2023，需求已被多季一手数据坐实** → 本案的 binding constraint **从"估值 air-pocket"转向"需求耐久性 vs pull-forward / 份额 vs custom-silicon"**。

## OPEN
- O1 10-K 逐行现金流/D&A/purchase commitments；O6 供应链 purchase obligations 与存货风险定量。
