# META Decision Card — as_of 2026-06-19

**pipeline_version**: lean-6module-v1 · **weights_version**: none · **run_date**: 2026-06-19
**context_label**: good_business_fairly_to_richly_priced_capex_anchor_unresolved · **status**: DECISION_DRAFT · **completeness**: ~62%

## 锁定结论
| 字段 | 值 |
|---|---|
| as_of price | **$577.22**（2026-06-18 收盘，≤ as_of）|
| market cap | **~$1.48T**（~2,564M 稀释股 × $577.22）|
| business_verdict | **good**（广告引擎满血好生意）|
| new_money_verdict | **WATCH** |
| existing_position_verdict | **HOLD** |
| suggested_initial_size | **0%**（现价不建仓）|
| suggested_max_size | **~5%**（即便建仓也封在 Starter 区，控制人 + 周期/capex 不确定）|
| buy_below | **~$480**（base 8% 门槛公允价）|
| verdict ceiling | **STARTER**（完整度 ~62%）；价格压实际 verdict 到 **WATCH** |
| binding_constraint | **价格 + owner-earnings 锚不确定性（capex ROI O4），非生意质量** |

## 六模块信号
| 模块 | 角色 | 信号 | 信心 | 一句话 |
|---|---|---|---|---|
| M1 证据脊柱 | confidence | **+2** | high | 锚定季度+全年载荷数全回挂 A1；缺口=haircut/封顶 |
| M2 主题/机制 | context+conviction | **+1** | high | 广告双寡头满血（+33%/单价 +12%/DAP 3.56B），但 OS/监管外部约束 |
| M3 利润池/耐久 | conviction | **+1** | med | 网络效应+定价权强、护城河加宽；OS/监管 + 控制人无约束 haircut |
| M4 财务现实 | conviction | **+1** | high | 报表强但 owner earnings 被 capex 吃（FCF yield 3.4%）、停回购、加杠杆 |
| M5 反演/陷阱 | risk | **−1** | med | capex 黑洞最可能、流量入口改写唯一可升 veto（无证据）；无资产负债表死亡 |
| M6 定价/仓位 | price+output | **−1** | med | base IRR +4% < 8% 门槛、现价高出公允价 ~21% → 价格 binding |

## 价格带
- **Buy-below（base 8% 门槛）**: **~$480**（−17%）。
- **Starter zone**: ~$480–520（向 52 周低 $520），仅 grant capex 复利时有 modest MOS。
- **No-chase**: > ~$640（+11%）。
- **下行参考**: bear ~$332（−42%，可存活非破产）。

## 三情景（5y IRR，hurdle 8%）
| 情景 | OE 起点 | CAGR | 退出倍数 | y5 每股 | 5y IRR |
|---|---:|---:|---:|---:|---:|
| Bear | $55B | +2% | 14x | ~$332 | **−10.5%** |
| Base | $62B | +10% | 18x | ~$701 | **+4.0%** |
| Bull | $65B | +16% | 22x | ~$1,171 | **+15.2%** |

> 锚敏感性: FCF 锚($50B) base ~0% / 中点($62B) +4% / 经营 NI 锚($75B) +10% —— **base 过不过门槛全看 capex ROI（O4）**。

## Kill / 升级 Criteria
K1 价格回撤 ~$480 → STARTER-eligible（升级）/ K2 capex ROI 量化兑现 → 上修锚、base ~+10%、STARTER-eligible（升级，O4 胜负手）/ K3 营收个位数 + 单价转负 → 引擎证伪（REJECT 候选）/ K4 capex 升但 OI 不增（黑洞坐实）/ **K5 流量入口结构改写 or 反垄断拆分（唯一可升 veto，exit 候选）**。

## runner_dissent
反方（防 too_small_missed_asymmetry）: META 可能是地表最强广告引擎，若 capex 是复利（单价 +12% 是旁证），经营 NI 锚下 base ~+10% 有 modest MOS。框架据**三条客观事实**给 WATCH 而非 STARTER（且明确非 REJECT）: ①保守锚 base +4% < 门槛、FCF yield 3.4%——现价无 MOS；②锚选 FCF vs 经营 NI 把 base 从 ~0% 拉到 ~+10%，全取决于未量化的 capex ROI（O4），为乐观锚付现价=为未证假设付钱；③控制权≫经济权益 + 停回购全押 capex + 提案全否=重资本无约束期激励错配（within-band haircut，非自动降级；2022 同结构曾验证为正）。生意没破裂、资产负债表死不了→business_verdict=good、非 REJECT。详见 decision_card.json。

## OPEN（封顶完整度）
O1 10-K 逐行（维护 vs 增长 capex）· O2 RL 全年逐行 · O3 proxy 精确持股/薪酬 · **O4 capex ROI 定量（胜负手）** · O5 Llama/生成式货币化 · O6 OBBBA 持续税率。
