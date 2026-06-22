# NVDA Inversion Map (M5) — as_of 2026-06-19

> 反过来想: 什么会杀死这门生意 / 让今天 $145.48 买入永久亏损？区分**结构性破裂(硬 veto 候选)** vs **size 控制/haircut**。

## 失败路径
| # | 失败路径 | 类型 | 严重度 | 当前读数 |
|---|---|---|---|---|
| F1 | **AI capex pull-forward** — hyperscaler 在周期高点提前/重复下单，AI capex 周期回撤，DC 需求 air-pocket（1–2 季腰斩）| size 控制（非结构性）| 高 | Q1 +85%、Q2 指引 $91B 仍升；但无法证伪部分是 pull-forward [binding constraint] |
| F2 | **custom silicon 替代** — CSP 自研 ASIC（TPU/Trainium/MTIA）+ AMD MI 在推理侧抢份额，DC 份额结构性下滑 | **可升级为结构性破裂**（若大规模迁移）| 高 | 定量份额未取 [O4]；当前 DC 仍 +92%，份额未见坍塌 |
| F3 | **毛利率正常化** — 竞争 + 客户议价把 GM 从 75% 压向 55–65% | haircut | 中高 | Q1 GM 74.9%（极值）；base 已假设回落 |
| F4 | **China 永久损失** — 出口管制全年归零并扩大 | haircut（已部分兑现）| 中 | Q1 China DC 出货 $0、Q2 指引归零 [S002]；已压进情景 |
| F5 | **库存/承诺减值** — 备货($25.8B)与 purchase obligations 在需求软化时计提（FY26 已有 $4.5B H20 先例）| 周期尾部 | 中 | 存货升、CoWoS 承诺 OPEN [O6] |
| F6 | **估值 de-rate** — forward ~19x 在增长减速/情绪转空时压缩 | size 控制 | 中 | 现价已距高点 −38%、贴 52 周低 → 部分已发生 |
| F7 | **key-man** — Huang 离任/失能且无 succession | 耐久性封顶 | 中 | 无公开 succession 披露 [O3] |

## 永久减值 vs 可恢复
- **永久减值仅来自 F2 的极端版本**（custom silicon 致 NVDA 沦为商品化 GPU 供应商、CUDA 护城河被绕过）——这是唯一的硬 veto 候选，但**当前一手数据不支持**（DC +92%、网络 +199%、份额未坍塌）→ 仍是监控项，未触发。
- F1/F3/F4/F5/F6 = 周期/估值 air-pocket，**资产负债表 fortress（净现金 $72B）下可存活**，非永久减值。

## 硬 veto 判定
- **不触发硬 veto**: thesis 耐久性未结构性破裂（瓶颈真实、份额未坍塌），资产负债表能存活。前瞻不确定性（pull-forward / China / custom silicon 未定量）= **haircut + size 控制 + kill 监控**，不是 veto。这正是修好的老病（SNDK 教训：别因前瞻不确定就 over-veto 真瓶颈）。

## Kill 标准（→ monitor.md / decision_card）
- K1: Q2/Q3 FY27 营收**实质性 miss $91B 指引**（需求是 pull-forward 非耐久）→ 砍回 tracking。
- K2: **DC 营收连续环比下滑 或 DC 毛利率急压**（瓶颈/定价权证伪）。
- K3: **可信证据显示大规模 CSP 设计迁出 NVDA 到 custom silicon/AMD 致 DC 份额结构性下滑**（F2 升级为结构性破裂）→ 重估耐久性天花板（可能 exit）。
- K4: **库存/供应承诺大额减值**（备货未转化为营收）。
- K5: Huang 离任/失能且无可信 succession → 下调耐久性天花板（trim 非必 exit）。
- K6: 价格隐含 5y IRR < 8%（≈ 价格 > ~$200，base 假设下）→ 估值纪律 no-chase。
