# NVDA Decision Card — as_of 2026-07-10 (REFRESH)

**pipeline_version**: lean-6module-v1.1 · **weights_version**: none · **run_date**: 2026-07-10
**context_label**: exceptional_bottleneck_no_margin_of_safety · **batch**: ai_robotics_2026-07-10 · **status**: DECISION_DRAFT · **completeness**: ~65%

> **LIGHT REFRESH of `../2026-06-20/`.** 价格 $210.69 → **$210.96**（2026-07-10 收盘，+0.13% 实质持平；Yahoo 再抓 + stockanalysis 两源一致，过 `verify_freshness.py`）。FILED 财务（Q1 FY27 / FY26）未变。新增 **robotics lens**（见 `robotics_lens.md`）回答本批 thesis。**估值结论未变：无安全边际 → 新钱 WATCH。**

## 锁定结论
| 字段 | 值 |
|---|---|
| as_of price | **$210.96**（2026-07-10 收盘，≤ as_of；2 源交叉）|
| market cap | **~$5.145T**（24,391M × $210.96）|
| business_verdict | **exceptional** |
| new_money_verdict | **WATCH（0%）** |
| existing_position_verdict | **HOLD** |
| suggested_initial_size | **0%**（现价无安全边际）|
| suggested_max_size | **0%（新钱）**；回调进 STARTER 区再开 |
| buy_below | **~$181**（base 5y IRR = 8% hurdle 中性价）|
| verdict ceiling | **STARTER**（完整度 ~65%）；价格门更严，封到 **WATCH** |
| binding_constraint | **价格（无 MOS）** — base IRR +4.7% < 8% hurdle，距高点仅 −10.8% |

## 六模块信号
| 模块 | 角色 | 信号 | 信心 | 一句话 |
|---|---|---|---|---|
| M1 证据脊柱 | confidence | **+2** | high | 锚定季度全回挂 A1/A2；LIVE 价 $210.96 二源交叉；新增机器人段取数 |
| M2 主题/机制 | context+conviction | **+2** | high | 全栈 AI 算力瓶颈（DC +92%、网络 +199%、Q2 $91B）；机器人非被买的机制（<1%）|
| M3 利润池/耐久 | conviction | **+2** | med | CUDA+全栈捕获最大利润池；operator 4/5；$80B 回购在 near-high；机器人护城河真但未变现 |
| M4 财务现实 | conviction | **+2** | high | OE 干净(capex-light, FCF=OE ~$182B)、净现金 $72B；桥闭合（未变）|
| M5 反演/陷阱 | risk | **−1** | med | 无结构破裂；pull-forward+custom-silicon=size 控制；China=可恢复期权；机器人 capital-cycle caution=NONE |
| M6 定价/仓位 | price+output | **−1** | high | forward **28x**、yield **3.5%**、base IRR **+4.7% < 8%**、距高点 −10.8% → **价格无 MOS，是卡点** |

## Batch thesis 直答（详见 robotics_lens.md）
- **(a) 机器人收入占比**：**<1%（估 ~0.3–0.5%，未披露）**。机器人埋在 Automotive 平台（FY26 $2.35B ≈ 1.09%，且多为汽车 DRIVE 非机器人）；DC=~92%。**买 NVDA = 买 AI 算力，非机器人 alpha。**
- **(b) 真需求 vs 预期**：机器人这块**主要 anticipation**——真实在卖的是 Jetson/IGX 模块 + Isaac/GR00T 平台 + 具名生态（dated 产品事件），但**收入体量未进报表**；已发生现金是汽车 DRIVE（~1%），不是机器人。
- **(c) capital_cycle（机器人段）**：applicable=**partial/largely N/A** · stage=**early/pre-inflection** · supply_barrier=**high（软件栈）但未赚超额回报** · caution=**NONE**（非见顶，是未变现期权）。真正要用此 lens 的是 DC/GPU 段（partial/late?/CUDA-high）。
- **(d) 真瓶颈 vs 概念**：平台/开发者层**是真护城河**（可证伪转换成本），但当前尺度**仍主要是概念/期权**；已变现的真瓶颈是 AI 算力。
- **(e) 拆分**：现价 ~100% 买的是 AI 数据中心算力（~28x fwd）；机器人=近乎免费的嵌入式看涨期权，付 0 溢价、拿 0 机器人 alpha。要纯机器人敞口 → NVDA 是错误载体。

## 价格带
- **No new money @ $210.96** — 已在 ~$181 无 MOS 线之上。
- **Starter 区**: ~$155–181（base IRR 回到 8% hurdle 之上），initial 3–5%。
- **Add 区**: ~$142–155 或营收连续兑现指引后 → 加向 8–12%。
- **No-chase**: 现价即 no-chase；向 $236.54 ATH 硬不追。下行参考 bear ~$80。

## 三情景（5y IRR @ $210.96，hurdle 8%）
| 情景 | OE 起点 | CAGR | 退出 P/OE | y5 每股 | 5y IRR |
|---|---:|---:|---:|---:|---:|
| Bear | $160B | −8% | 18x | ~$80 | **−17.6%** |
| Base | $182B | +12% | 20x | ~$266 | **+4.7%** |
| Bull | $185B | +22% | 24x | ~$495 | **+18.6%** |

> base **+4.7% < 8% hurdle** → 现价无安全边际。8%-中性入场 ≈ $181，现价在其上方（付溢价）。

## WATCH → STARTER 触发
价格回调进 **~$155–181**（base IRR 回到 8%+），thesis 不变。机器人专项 re-rate 触发：NVDA 把 robotics 拆成独立收入行 + 持续 +xxx% Y/Y（概念→变现瓶颈）——在此之前它只是免费期权，非买入理由。

## Kill Criteria
K1 营收实质 miss $91B / 环比降 / GM<65% · K2 **大规模 custom-silicon 迁出致 DC 份额结构性下滑（唯一可升 veto）** · K3 库存承诺大额减值（$4.5B H20 先例）· K4 价格持续 >~$181 无估值上调 → 维持 WATCH（现已触发）· K5 Huang key-man。

## runner_dissent
沿用并重申 06-20：卓越自筹瓶颈（FCF=OE ~$182B、净现金 $72B、DC +92%），bull IRR +18.6%，为何不开小仓？框架 override 到 WATCH，因价格是卡点：base +4.7% < 8%，距 ATH 仅 −10.8%。就本批 thesis：机器人叙事是真平台位置但**非 NVDA 内可买的机器人瓶颈**——<1% 营收、主要 anticipation、对现价贡献 ~nil。现价买 NVDA 是无 MOS 的 AI 算力估值判断，附送一张机器人彩票，不是机器人 alpha。

## OPEN（封顶完整度）
O1 10-K 逐行 · O3 proxy/operator · O4 custom-silicon 定量份额（blocking）· O5 China H200 金额量级 · **O7 纯机器人收入（未披露，估 <1%）** · **O8 humanoid 起量量级/时点（期权，未建模）**。
