# NVDA Inversion Map (M5) — as_of 2026-06-20

> 反过来想: 什么会杀死这门生意 / 让今天 **$210.69** 买入永久亏损？区分**结构性破裂(硬 veto 候选)** vs **size 控制/haircut**。
> **CORRECTED** vs `../2026-06-19/`：现价 $210.69（非错版的 $145.48≈52周低）；China 由"永久损失"改判为"可恢复期权"。

## 失败路径
| # | 失败路径 | 类型 | 严重度 | 当前读数 |
|---|---|---|---|---|
| F1 | **AI capex pull-forward** — hyperscaler 在周期高点提前/重复下单，AI capex 周期回撤，DC 需求 air-pocket（1–2 季腰斩）| size 控制（非结构性）| 高 | Q1 +85%、Q2 指引 $91B 仍升；但无法证伪部分是 pull-forward |
| F2 | **custom silicon 替代** — CSP 自研 ASIC（TPU/Trainium/MTIA）+ AMD MI 在推理侧抢份额，DC 份额结构性下滑 | **可升级为结构性破裂**（若大规模迁移）| 高 | 定量份额未取 [O4]；当前 DC 仍 +92%，份额未见坍塌 |
| F3 | **毛利率正常化** — 竞争 + 客户议价把 GM 从 75% 压向 55–65% | haircut | 中高 | Q1 GM 74.9%（极值）；base 已假设回落 |
| F4 | **China** — 出口管制再度收紧致全年归零 | haircut（双向，当前偏松）| 中 | Q1 China DC 出货 $0；**但 2026-02 H200 许可重发、3 月已收订单 [S010/S011]** → 当前是**未计入的上行期权**，非永久损失；下行是许可被撤回 |
| F5 | **库存/承诺减值** — 备货($25.8B)与 purchase obligations 在需求软化时计提（FY26 已有 $4.5B H20 先例）| 周期尾部 | 中 | 存货升、CoWoS 承诺 OPEN [O6] |
| F6 | **估值 de-rate** — forward ~28x 在增长减速/情绪转空时压缩 | **价格卡点（已是 binding）** | **中高** | 现价 $210.69 距高点仅 −11%、在区间上部；base IRR +4.8% < 8% → **无 MOS，已是 verdict 卡点** |
| F7 | **key-man** — Huang 离任/失能且无 succession | 耐久性封顶 | 中 | 无公开 succession 披露 [O3] |

## 永久减值 vs 可恢复
- **永久减值仅来自 F2 的极端版本**（custom silicon 致 NVDA 沦为商品化 GPU 供应商、CUDA 护城河被绕过）——这是唯一的硬 veto 候选，但**当前一手数据不支持**（DC +92%、网络 +199%、份额未坍塌）→ 仍是监控项，未触发。
- F1/F3/F4/F5 = 周期/需求 air-pocket，**资产负债表 fortress（净现金 $72B）下可存活**，非永久减值。
- **F6（估值）现在是 verdict 的实际卡点**：不是永久减值风险，而是"现价无安全边际"——把新钱 verdict 从 STARTER 压到 WATCH。

## 硬 veto 判定
- **不触发硬 veto**: thesis 耐久性未结构性破裂（瓶颈真实、份额未坍塌），资产负债表能存活。前瞻不确定性（pull-forward / China / custom silicon 未定量）= **haircut + size 控制 + kill 监控**，不是 veto（SNDK 教训：别因前瞻不确定就 over-veto 真瓶颈）。
- **但 M6 价格门是另一回事**：业务不被 veto，不代表现价值得买——$210.69 无 MOS，新钱 WATCH。

## Kill 标准（→ monitor.md / decision_card）
- K1: Q2/Q3 FY27 营收**实质性 miss $91B 指引** 或 DC 营收连续环比下滑 或 GM<65%（需求/定价权证伪）→ 砍回 tracking。
- K2: **可信证据显示大规模 CSP 设计迁出 NVDA 到 custom silicon/AMD 致 DC 份额结构性下滑**（F2 升级为结构性破裂）→ 重估耐久性天花板（可能 exit）。【唯一可升 veto】
- K3: **库存/供应承诺大额减值**（备货未转化为营收；FY26 有 $4.5B H20 先例）。
- K4: 价格持续 > ~$181（base 5y IRR < 8%）且无估值上调 → 维持 WATCH/no-chase（**现价 $210.69 已触发**）。
- K5: Huang 离任/失能且无可信 succession → 下调耐久性天花板（trim 非必 exit）。
