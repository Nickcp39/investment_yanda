# GOOGL Decision Card — as_of 2026-06-19

**pipeline_version**: lean-6module-v1 · **weights_version**: none · **run_date**: 2026-06-19
**context_label**: great_business_no_margin_of_safety · **status**: DECISION_DRAFT (refresh of v1/v2, ~2026-06-16) · **completeness**: ~75%

> **LIGHT REFRESH, not a rebuild.** 3-day delta (06-16→06-18) immaterial; verdict/size/ceiling/buy-below 全部不变。详见 `refresh_note_2026-06-19.md`。

## 锁定结论
| 字段 | 值 |
|---|---|
| as_of price | **$368.03**（2026-06-18 收盘，≤ as_of 2026-06-19；3 日 −1.4%）|
| market cap | **~$4.46T**（12,116M 稀释股 × $368.03；回购暂停股数回升）|
| business_verdict | **good**（10 年级好生意）|
| new_money_verdict | **WATCH** |
| existing_position_verdict | **HOLD**（个人现 0% 仓位）|
| suggested_initial_size | **0%** |
| suggested_max_size | **0%**（现价；价格回到 ~$113 才重开 panel 评 starter 1–3%）|
| buy_below | **~$113**（base 10% IRR 锚）|
| verdict ceiling | **WATCH**（硬规则封顶已解除；ceiling 来自价格无安全边际）|
| binding_constraint | **价格无安全边际（base 10y IRR −3.0%，连 bull +5.2% 都 <8%），非信息不足** |

## 六模块信号
| 模块 | 角色 | 信号 | 信心 | 一句话 |
|---|---|---|---|---|
| M1 证据脊柱 | confidence | **+1** | med | 锚定季度+10-K 全回挂 ~50 条 A1；硬 GAP=仅 3 年序列 + capex 维护/成长拆分未披露；完整度 ~75% 封顶 |
| M2 主题/机制 | context+conviction | **+2** | high | 双边平台变现商业意图 + 卖算力；Search +19% / Cloud +63% / backlog $460B，收入上行真实 |
| M3 利润池/耐久 | conviction | **+1** | med | 存量护城河 Strong 但处形态切换期，增量护城河未证实；operator 28/40，$180B capex 无回报纪律框架 + 52.7% 投票权无外部纠错杠杆 |
| M4 财务现实 | warning | **−1** | high | 报表净利 $160B 高估 owner earnings($51–82B) 2–3 倍；营收 +31% 而 FCF 停滞（capex 吃掉）；SBC $27.1B + 回购归零稀释裸露 |
| M5 反演/陷阱 | risk | **−1** | med | F1×F3 合流=收入增但 owner earnings 永久稀释；F2 监管结构性救济=尾部；全部压在"维护vs成长 capex 拆分"一个不可观测变量 → haircut 非 veto |
| M6 定价/仓位 | price+output | **−2** | high | **卡点**。~$368 = 69x OE、起始 yield 1.46%；bear −13.1% / base −3.0% / bull +5.2% 全 <8% → 价格端封顶 WATCH |

## 价格带（安全边际阶梯）
- **当前 ~$368**: avoid 区（>~$300 连 bull IRR 都 <8%）→ **0%，不开仓**。
- **~$134**（8% 门槛）: 进观察，尚不构成 starter。
- **~$113**（base 10%，**buy-below 主锚**）: 重开 IC panel 评 STARTER（试仓 1–3%）。
- **~$95**（Core 12%）/ **~$48**（bear-8% 下行保护锚）。
- 任何建仓前先确认 K-A/K-D 未触发（防价值陷阱）。

## 三情景（10y IRR @ $368/$370，hurdle 8%）
| 情景 | OE 起点 | revenue CAGR | 退出 P/OE | OE_y10 | 10y IRR |
|---|---:|---:|---:|---:|---:|
| Bear | $52B | ~6% | 14x | $63B | **−13.1%** |
| Base | $65B | ~11% | 20x | $140B | **−3.0%** |
| Bull | $80B | ~15% | 26x | $248B | **+5.2%** |

> 要在 $370 赚 10%，需 owner earnings 十年复合 ~22%（十年做到 ~7x）——峰值增速 + capex 同时见顶回落两个乐观假设叠加。

## Kill Criteria（三态，详见 monitor.md）
K-A 搜索变现：Search & other 连 2 季 ≤+8% 且归因 AI（现 +19% 🟢）/ K-B capex 黑洞：FCF/share 连 2 年降 且 capex/OCF >70%（Q1'26 ~78% 🟡）/ K-C 资本配置纪律：连 2 季无 capex ROI 框架 或 TPU 减值（现框架不存在 🟡/🔴）/ K-D 监管尾部：DOJ adtech 结构性救济（待裁 🟡）/ **K-E 估值纪律：买入价隐含 10y IRR <8%（现价 $368 🔴 ACTIVE 卡点，唯 ~$113 解除）**。

## runner_dissent
错过型风险真实（好公司极少跌 −70% 到 ~$113，"等回调"可能等不到，机会成本对照 QQQ 4 年 2.03×；已记于 memo §10）。但框架**不**像 NVDA 那样 override 到 STARTER，因为与 NVDA 不同，**GOOGL 价格就是卡点**：~69x OE 连 bull IRR 都 +5.2%(<8%)、owner earnings 质量差（营收 +31% 而 FCF 停滞、报表净利被非现金股权收益虚增 2–3 倍、回购暂停稀释裸露）、资产负债表在为 capex **加杠杆**而非护底。这正是 ceiling 规则要防的"好生意错价格"——残余 capex/incremental-ROIC 不确定性只在价格给出安全边际后才重要。3 日刷新后裁决不变。详见 decision_card.json。

## OPEN（封顶完整度 ~75%）
O1 维护 vs 成长 capex 拆分（最高优先级，决定 base 落点）· O2 10 年精确序列（仅 3 年，Buffett 漏桶无法做）· O3 D&A 绝对值待 10-K 核实 · O4 sell-side 一致预期/行业估值锚未拉 · O5 DOJ adtech 结构性救济尾部量化未进 bear。
