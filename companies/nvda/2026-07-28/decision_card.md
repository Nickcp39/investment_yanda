# NVDA Decision Card — as_of 2026-07-28

**pipeline_version**: lean-6module-v1 · **weights_version**: none · **run_date**: 2026-07-28
**context_label**: exceptional_bottleneck_no_MOS_derated_into_capex_audit · **status**: DECISION_DRAFT · **completeness**: ~65%

> REFRESH of `../2026-06-20/` (baseline) and `../2026-07-10/`. Price re-priced to **$197.01** (2026-07-28, −6.5% vs 06-20) on the **7/28 semiconductor crash** (NVDA led, ~$300B market value wiped). **NVDA has NOT reported Q2 FY27** — that print is **2026-08-26**, after as_of — so the owner-earnings model is carried forward unchanged; only price + regime move. Passes the `verify_freshness.py` gate (price cross-checked Yahoo + stockanalysis, both $197.01).

## 锁定结论
| 字段 | 值 |
|---|---|
| as_of price | **$197.01**（2026-07-28；Yahoo chart API + stockanalysis 两源到分）|
| market cap | **~$4.806T**（24,391M × $197.01；stockanalysis $4.77T、彭博 ~$4.83T 交叉验证）|
| business_verdict | **exceptional**（未变；7/28 是重定价非破裂）|
| new_money_verdict | **WATCH（0%）** — 仍无安全边际，但更接近 starter |
| existing_position_verdict | **HOLD** — 无 kill 触发，业务未受损 |
| suggested_initial_size | **0%**（现价无 MOS）|
| suggested_max_size | **0%（新钱）**；回调进 STARTER 区再开 3–5% |
| buy_below | **~$181**（base 5y IRR = 8% hurdle 中性价，未变）|
| verdict ceiling | 完整度 ~65% → **STARTER**；价格门更严 → 封 **WATCH** |
| binding_constraint | **价格（无 MOS）+ regime（capex 审计/custom-silicon）双卡点** |
| Q2 FY27 已报? | **否**（档期 2026-08-26，在 as_of 之后）|

## 六模块信号（符号 vs 06-20 未变；叙事叠 regime）
| 模块 | 角色 | 信号 | 信心 | 一句话 |
|---|---|---|---|---|
| M1 证据脊柱 | confidence | **+2** | high | 锚定季度+全年一手全挂；价格 2 源交叉验证；Q2 未报（8/26）|
| M2 主题/机制 | context+conviction | **+2** | high | 全栈 AI 算力瓶颈未破；7/28 暴跌是拥挤交易回撤非机制断裂 |
| M3 利润池/耐久 | conviction | **+2** | med | CUDA+全栈护城河未破，仍 ~87% 份额；custom-silicon 能见度上升=监控更活跃 |
| M4 财务现实 | conviction | **+2** | high | OE 干净(FCF=OE ~$182B、净现金 $72B)；**无 Q2 新数**，China 新增 25% 抽成 |
| M5 反演/陷阱 | risk | **−1** | med | 无结构破裂，但 regime（capex 审计+ASIC 放量+鹰派贴现）令风险侧更重 |
| M6 定价/仓位 | price+output | **−1** | high | forward **26x**、yield **3.8%**、base IRR **+6.2% < 8%**、距高点 −16.7% → 仍无 MOS，缺口收窄 |

## 价格带
- **No new money @ $197.01** — 仍在 ~$181 无 MOS 线之上 +8.8%。
- **Starter 区**: ~$155–181（base IRR 回 8%+），initial 3–5%；鉴于 regime 风险，宁可靠近 $164 的 52 周低再动。
- **Add 区**: ~$142–155（需破 $164 的 52 周低，base IRR ~12–14%）或营收连续兑现指引后 → 加向 8–12%。
- **No-chase**: 现价即 no-chase；向 $236.54 ATH 硬不追。
- **下行参考**: bear ~$80（−59% from $197.01，可存活非永久减值）。

## 三情景（5y IRR @ $197.01，hurdle 8%）
| 情景 | OE 起点 | CAGR | 退出 P/OE | y5 每股 | 5y IRR | vs 06-20 |
|---|---:|---:|---:|---:|---:|---:|
| Bear | $160B | −8% | 18x | ~$80 | **−16.5%** | −17.6% |
| Base | $182B | +12% | 20x | ~$266 | **+6.2%** | +4.8% |
| Bull | $185B | +22% | 24x | ~$495 | **+20.2%** | +18.6% |

> base **+6.2% 仍 < 8% hurdle** → 现价无安全边际，但 hurdle 缺口从 3.2pp 收窄到 1.8pp。y5 每股未变（无新一手财务数），只有价格与 IRR 变。

## Kill Criteria
K1 **Q2 FY27（8/26）** 实质 miss $91B / 营收环比降 / GM<65% · K2 **大规模 CSP custom-silicon 迁出致份额结构性下滑（唯一可升 veto）** · K3 库存/承诺大额减值（$4.5B H20 先例；盯 HBM/CoWoS）· K4 价格持续 >~$181 且无估值上调 → WATCH/no-chase（现已触发）· K5 Huang key-man · **K6（regime）AI-capex 审计触发 hyperscaler capex 削减 → 需求 air-pocket**。

## runner_dissent
多头本能：价格更友好了（base IRR +6.2%、回撤 −16.7%、7/28 是拥挤交易回撤非破裂，瓶颈+CUDA 护城河未破、DC +92%、净现金 $72B），为何不趁跌开小仓？框架 override 到 WATCH，因为（a）base IRR 仍低于 8% hurdle、价格仍在 ~$181 之上 +8.8%；（b）**价格跌是有原因的**——regime（capex 审计+可见的 custom-silicon 放量+Warsh 鹰派贴现率）抬高了 bear 腿的概率权重，便宜入场一半是风险溢价补偿，此处要**更多**安全边际而非更少；（c）胜负手 Q2 FY27（8/26）尚未落地，市场在一个**未确认季度**上重定价。诚实定位：比 06-20 更接近 starter，但**尚未到**。回调到 ≤$181（更理想靠近 $164 52 周低）且 thesis 未破 → 转 STARTER。存量 HOLD，无破裂。

## OPEN（封顶完整度 ~65%）
O1 10-K 逐行 · O3 proxy/operator 细节 · O4 custom-silicon 定量份额（blocking）· O5 China H200 量级 + 25% 抽成毛利拖累 · O6 供应/库存(HBM/CoWoS)承诺 · **O7 Q2 FY27 未报（blocking，至 8/26）**。
