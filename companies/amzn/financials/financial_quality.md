# AMZN Financial Quality (M4) — as_of 2026-06-19

来源: FY25 8-K Ex99.1 [S002] / Q1 2026 8-K Ex99.1 [S001]。模型见 `../model/*.csv`。

## 1. 盈利能力与趋势
- **营收轨迹**: FY23 ~$574.8B → FY24 $638.0B → FY25 $716.9B（+12%）→ Q1 2026 $181.5B（+17%，年化 ~$726B 且环比加速）。稳健双位数复合。
- **营业利润大幅扩张**: FY24 $68.6B → FY25 $80.0B → Q1 2026 季 $23.9B（**创纪录 13.1% 营业利润率**）。零售利润率从 2022 谷底回升 + AWS 利润扩张双驱动。
- **AWS 利润核心**: FY25 AWS OI $45.6B（营业利润率 ~35.4%）；Q1'26 AWS OI $14.2B（~37.8%）。AWS 占总 OI ~57–59%。
- **净利质量警告**: Q1 2026 GAAP 净利 $30.3B **含 $16.8B 税前非经营性 Anthropic 投资收益** → GAAP EPS $2.78 被显著放大，经营性盈利远低。FY25 净利 $77.7B 同样含股权投资收益。**看估值须用营业利润/正常化盈利，不能用 GAAP EPS 直接算 P/E。**

## 2. 现金流与 owner earnings 桥（本案核心难点）
- FY25: OCF $139.5B − capex $131.8B = **FCF $11.2B**（vs $38.2B 上年）。
- Q1 2026 TTM: OCF $148.5B − capex $151.0B ≈ **FCF $1.2B**（capex 已超过 OCF）。
- **owner earnings ≠ 当前 FCF**（与 NVDA 的"OE≈FCF"截然相反，与 GOOGL 同病但更极端）:
  - 当前 FCF 近零**不是**因为生意不赚钱（营业利润 $80B、OCF $148.5B），而是因为 **capex（$131.8B FY25 / $151B TTM / 计划 $200B 2026）远超折旧**——这是**增长 capex**，把经营现金流全部再投资。
  - **正常化 owner earnings 的核心拆分（O4，缺一手）**: capex 中维护性部分 vs 增长性部分。若维护性 capex 仅占一小部分（行业惯例 + AWS 资产长久期），则正常化 owner earnings 远高于 $1.2B FCF，可能在 $40–70B 量级；但**这取决于增长 capex 的 ROIC——若 $200B capex 赚不回资本成本，则是价值毁灭而非递延收益**。
  - **这是本案 owner earnings 桥无法在一遍内闭合的根因**: 数字本身（OCF/capex）是 A1 一手，但"capex 维护 vs 增长拆分 + 增量 ROIC"是前瞻判断，须等几年回报兑现或 10-K 逐行补（O1/O4）。

## 3. 资产负债表
- 现金+证券 (2026-03-31) ~$143.1B；金融性长债 $119.07B（**Q1 内激增 ~$53.4B 为 AI capex 融资**）→ **净现金仍正 ~+$24B**（仅金融债）；计入长租 $90.8B 则净债务约 −$67B。
- PP&E net $397.5B（季增 ~$40B）→ 资产负债表正在快速"重资产化"。
- **判断**: 资产负债表**可存活**（净现金正、OCF $148.5B 巨大），但**弹性正在主动消耗**（加杠杆 + capex 吞 FCF）。这不是 NVDA 式 fortress，也不是危机；是"用强资产负债表 + 杠杆给 AI 豪赌融资"的中间态。

## 4. 三情景（估值起点用正常化 owner earnings，须从营业利润反推，不用当前 FCF）
见 `../model/scenario_model.csv`。要点:
- **Bull**: $200B AI capex 赚回高 ROIC、AWS 维持 +25%+、零售利润率续升、广告放量 → 正常化 owner earnings 5y 高复合、capex 强度回落后 FCF 释放 → 现价隐含 IRR 高（>15%）。
- **Base**: AWS 增速从 +28% 回落到稳态 ~15–18%、零售利润率温和升、capex ROIC 中等（赚回资本成本但非超额）、capex 强度高位维持数年压制 FCF → 正常化 owner earnings 温和增长 → 现价 P/E ~34x GAAP（含股权收益失真），SOTP 公允价值接近现价，IRR ~7–10%。
- **Bear**: $200B capex ROIC 低于资本成本（AI 需求 air-pocket / AWS 份额被超大规模 + 自研芯片侵蚀 / 折旧浪潮压利润）、零售利润率回吐、加杠杆遇利率/需求双杀 → owner earnings 被折旧与利息侵蚀、de-rate → 现价下行 −30–45%。**资产负债表可存活（OCF $148.5B），非永久减值，但价值毁灭于 capex。**

## 5. 与 2023 盲测案对照（关键差异）
- 2023-02-03: ~$103/股、市值 ~$1.06T、零售亏损/利润率谷底（含 Rivian 减记）、AWS 减速、~18,000 裁员。**卡点 = 零售成本结构是否结构性受损**。
- 2026-06-19: $244.39/股、市值 ~$2.66T、**零售利润率创纪录回升（thesis 已兑现）、AWS 重新加速 +28%**——2023 的卡点已解除。**但新的卡点出现: $200B AI capex 把 FCF 压到近零 + 加杠杆 + GAAP 净利被 Anthropic 收益失真 + 估值不便宜（P/E 34x、贴 52 周高）**。binding constraint **从"零售周期触底"转向"AI capex 的 ROI + owner earnings 在重投资期如何看 + 价格是否有 MOS"**。

## OPEN
- O1 10-K 逐行（D&A、capex 维护 vs 增长、commitments、Anthropic 会计）；O4 $200B capex ROIC / 维护性占比（owner earnings 桥胜负手）；O6 Anthropic 持仓与公允价值失真。
