# GOOGL Decision Card — as_of 2026-07-28

**pipeline_version**: lean-6module-v1 · **weights_version**: none · **run_date**: 2026-07-28
**context_label**: great_business_no_margin_of_safety_capex_audit_regime · **status**: DECISION_DRAFT · **completeness**: ~72%

> **PRICE + REGIME re-pricing of the 6/19 dossier, with the Q2-2026 print (reported 2026-07-22) folded in.** An intermediate same-quarter run exists at `../2026-07-24/` (priced at the $317.69 earnings trough); this card re-prices that same Q2 data at **$333.71** after a +5% bounce and overlays the **7/28 semiconductor-crash / AI-capex-audit** regime. Independent WebSearch corroborated every Q2 figure. Verdict UNCHANGED. See `delta_vs_0619.md`.

## 锁定结论
| 字段 | 值 |
|---|---|
| as_of price | **$333.71**（2026-07-28 收盘，Yahoo chart API + stockinvest.us 双源；较 6/19 $368.03 **−9.3%**）|
| market cap | **~$4.081T**（12,230M A+B+C 股 × $333.71；回购 $0 股数续升）|
| business_verdict | **good**（10 年级好生意，Q2 运营面更强）|
| new_money_verdict | **WATCH** |
| existing_position_verdict | **HOLD**（个人现 0% 仓位）|
| suggested_initial_size | **0%** |
| suggested_max_size | **0%**（现价；价格回到 ~$117 才重开 panel 评 starter 1–3%）|
| buy_below | **~$117**（base 10% IRR 锚，Q2 后微升自 $113）|
| verdict ceiling | **WATCH**（完整度 ~72% 封顶 STARTER；价格更低封 WATCH）|
| binding_constraint | **价格无安全边际（base 10y IRR −1.5%，连 bull +7.7% 都 <8%）；被 M4（K-B 触发）强化** |

## 六模块信号
| 模块 | 角色 | 信号 | Δvs6/19 | 信心 | 一句话 |
|---|---|---|:--:|---|---|
| M1 证据脊柱 | confidence | **+1** | = | high | Q2 一手财报入库，证据更全（含实际 D&A + FCF 桥），WebSearch 交叉验证；但维护/成长 capex 拆分 + 无 ROI 门槛的核心 GAP 未变；完整度 ~72% |
| M2 主题/机制 | context+conviction | **+2** | = | high | 需求全面走强：Cloud +82%/backlog $513.9B/利润率 35.5%、Search +17%（AI 增益非侵蚀）；已在 +2 天花板 |
| M3 利润池/耐久 | conviction | **+1** | = | med | 增量护城河首现"是"（Cloud 高利润率二度兑现）vs capex 加码至 $205B 仍无 ROI 框架 + 52.7% 投票权无外部纠错；净持平 |
| M4 财务现实 | warning | **−2** | **↓ −1→−2** | high | **本轮唯一动的模块**：capex 警告兑现——Q2 FCF 转负 −$5.9B，TTM FCF −20%，capex/OCF ~71%（单季 115%），回购 $0 + 发行优先股/债，指引升至 $195–205B；净利 $112B 中 ~$99B 是非现金股权收益 |
| M5 反演/陷阱 | risk | **−1** | = | med | F1×F3 合流被拆解：F3 capex 兑现、F1 搜索侵蚀被证伪(+17%)、F2 监管缓和；叠 7/28 regime——capex 审计正打在 GOOGL 命门，但它非存储/韩国/卖芯片股（作为买方甚至受益于硬件降价）→ 估值/陷阱风险非特许经营死亡 |
| M6 定价/仓位 | price+output | **−2** | = | high | **卡点**。$333.71 三情景 10y IRR 全 <8%（bear −11.7%/base −1.5%/bull +7.7%）；+5% 反弹把 bull 推回 8% 以下；按 TTM FCF ~76.6x，比 6/19(69.6x)、7/24(72.9x) 都更贵 |

## 价格带（安全边际阶梯，模型自 6/19→Q2 未变）
- **当前 ~$333.71**: avoid 区（>~$323 连 bull IRR 都 <8%）→ **0%，不追 +5% 反弹**。
- **~$139**（8% 门槛）: 进观察，尚不构成 starter。
- **~$117**（base 10%，**buy-below 主锚**）: 重开 IC panel 评 STARTER（试仓 1–3%）。
- **~$99**（Core 12%）/ **~$50**（bear-8% 下行保护锚）。
- 任何建仓前先确认 bull 论点（capex 见顶 + FCF/share 回升 + ROI 框架出现）未被证伪。

## 三情景（10y IRR @ $333.71，hurdle 8%）
| 情景 | @$317.69(7/24) | **@$333.71(7/28)** | 说明 |
|---|---:|---:|---|
| Bear | −11.3% | **−11.7%** | 防御低回报读，退出 14x |
| Base | −1.0% | **−1.5%** | 峰后回落，退出 20x — 仍为负 |
| Bull | +8.2% | **+7.7%** | 完美 capex 转化，退出 26x — **反弹后跌回 8% 以下** |

> 关键：7/24 谷底 bull 尚 +8.2% 勉强过线；+5% 反弹到 $333.71 后 **无任何情景过 8% 门槛**。bull-8% 临界价 ~$323.6，现价在其上。

## Kill Criteria（三态，详见 inversion_map.md）
K-A 搜索变现：Search +17% 🟢 / **K-B capex 黑洞：Q2 FCF 转负、TTM capex/OCF ~71%、FCF/share −28%、回购$0 股数升 🔴 触发中**（Cloud 高利润率+backlog 为 incremental-ROIC 逃生阀）/ K-C 资本配置：连 2 季无 ROI 门槛、指引升至 $205B 🟡/🟠 / K-D 监管：DOJ 搜索无拆分、adtech 待裁法官偏行为救济 🟢/🟡 / **K-E 估值纪律：现价隐含 10y IRR <8% 🔴 ACTIVE 卡点，唯 ~$117 解除** / K-REGIME 若 AI-capex 轮动把价拖向 ~$250–280 提前重开 panel（改善入场 IRR 而非破论点）。

## runner_dissent
错过型风险比 6 月更大：Cloud 已用 35.5% 利润率 + $513.9B backlog + op income ~翻三倍证明"增量 ROIC 撑得住"（正是 6 月空头需要的证伪证据），F1/F2 两条永久路径均减弱，且 7/28 轮动可能正是最终送出可买价格的催化。但框架**不** override 到 STARTER，因为价格自谷底不降反升：$333.71 的 base IRR 仍为负(−1.5%)，+5% 反弹后连 bull(+7.7%)都不过 8%——等于全价买乐观情景零缓冲；且本季 capex-吃-FCF 论点**兑现**（FCF 转负、FCF/share 自峰值 −28%、稀释裸露、发行优先股+债、capex 升至 $205B 仍无 ROI 门槛），按 TTM FCF 反而更贵(~76.6x)。9% 的跌配 20% 的 FCF 下滑不是安全边际。**等价格（~$99–117），别等更好的故事——故事已经够好。**

## OPEN（封顶完整度 ~72%）
O1 维护 vs 成长 capex 拆分（最高优先级，决定 base 落点）· O2 capex ROI 门槛/预期 ROIC 仍未披露 · O3 Cloud 35.5% 利润率在 Q3 第三方算力桥接下的可持续性 · O4 DOJ adtech 最终救济形态 · O5 FOMC(周三 Warsh) 利率路径对长久期估值的折现冲击 · O6 未重建完整 owner-earnings 桥/十年逐年序列（仅并入 Q2 关键行）。
