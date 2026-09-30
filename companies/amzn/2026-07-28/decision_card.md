# AMZN Decision Card — as_of 2026-07-28

**pipeline_version**: lean-6module-v1 · **weights_version**: none · **run_date**: 2026-07-28
**context_label**: good_business_wrong_price_capex_reinvestment · **status**: DECISION_DRAFT · **completeness**: ~62%
**regime**: AI-capex 审计年 / 半导体暴跌轮动 / 财报周（**Q2 未出，7/30 才发**）/ FOMC 7/29（Warsh）

## 锁定结论
| 字段 | 值 |
|---|---|
| as_of price | **$230.86**（2026-07-28 收盘，三源一致 delta 0.0%）|
| market cap | **~$2.51T**（10,874M 稀释股 × $230.86）|
| business_verdict | **good** |
| new_money_verdict | **WATCH** |
| existing_position_verdict | **HOLD** |
| suggested_initial_size | **0%** |
| suggested_max_size | **0%** |
| buy_below | **~$178**（MOS-emergence / STARTER 触发线，贴 52 周低；严格 base=8% 在 ~$154）|
| verdict ceiling | **WATCH**（价格封顶，先于完整度 62% 的 STARTER 封顶生效）|
| binding_constraint | **价格无 MOS（起始收益率 2.2–2.7%、base IRR −0.4%）+ owner-earnings 桥不闭合（$200B capex O4）+ Q2 财报 2 天后未并入** |

## 六模块信号（vs 6/19 无档位变化）
| 模块 | 角色 | 信号 | 信心 | 一句话 |
|---|---|---|---|---|
| M1 证据脊柱 | confidence | **+2** | high | 价格三源 0.0% 一致 @$230.86（非极值）；锚定季全回挂一手；**新 gap：Q2-2026 未出（7/30）** |
| M2 主题/机制 | context+conviction | **+2** | high | 三引擎复利机器；**Anthropic 5GW + Trainium2/3 强化** AWS-AI 需求+自研护城河；无 thesis 破裂 |
| M3 利润池/耐久 | conviction | **+1** | med | AWS 西方第二大云利润池；operator 4/5；**CXMT/存储暴跌不伤 AMZN 护城河（它是买方）** |
| M4 财务现实 | warning | **−1** | med | owner-earnings 桥仍不闭合（FCF ~$1.2B / capex $200B）；**Q2 print 2 天后、capex-审计核心测试** |
| M5 反演/陷阱 | risk | **−1** | med | regime 抬升 F1（capex ROIC）/F4（FOMC 利率）salience，未升 veto；资产负债表存活 |
| M6 定价/仓位 | price+output | **−1** | high | $230.86：base IRR −0.4%、bull +8.9%、起始收益率 ~2% → **价格仍是卡点，无 MOS** |

## 价格带
- **现价 $230.86 = 不追**（base IRR ~0、仅 bull 够门槛）。
- **Watch 观察**：~$180–200。
- **Starter 候选（解封顶）**：~$175–180（MOS 出现、base IRR 回中个位数、贴 52 周低）→ 解 WATCH 封顶。
- **完整 MOS（严格 base=8%）**：~$154。
- **下行参考**：bear ~$118（−49%，资产负债表存活）。

## 三情景（5y IRR，hurdle 8%）— NOPAT 口径（给足 capex 信用）
| 情景 | y5 每股 | 5y IRR @$230.86 | (对照 @$244.39) |
|---|---:|---:|---:|
| Bear | ~$118 | **−12.6%** | −13.5% |
| Base | ~$226 | **−0.4%** | −1.5% |
| Bull | ~$353 | **+8.9%** | +7.7% |

> 价格 −5.5% 抬升 IRR ~+1.1%/年；base 仍 ~0、仅 bull 刚过门槛；保守 OE 口径更低（base ~−4.9%、bull ~+6.1%）。**仍无 MOS。**

## Kill / 升档 Criteria
K1（capex-审计核心）7/30 起 capex 续增但 AWS 增量利润 + FCF 不匹配（ROIC 恶化，唯一可升 veto）/ K2 AWS <15% 且份额走弱 / K3 总营业利润率 <9% / **K4 FOMC 利率鹰派冲击 + 杠杆模型双杀** / **K5 hyperscaler capex-ROI 全行业 re-rate → 或推价穿 buy-below（升档）** / **K6 价格跌破 ~$178 → 解封顶升 STARTER** / K7 Anthropic 公允价值反向失真。

## runner_dissent（摘要）
机械结论 WATCH/HOLD 不变且仍**正确**——教科书"好生意错价格"，与 GOOGL 同构。三反向风险：①**timing**——本卡锁定于 Q2 print（7/30）前 2 天，capex→FCF 是审计年胜负手，临二元事件不宜给新钱建仓；②too_small_missed_asymmetry——若 $200B capex 是又一个 AWS，WATCH 会错过 → 故给 WATCH 不给 REJECT，留 STARTER 升档线；③O4 桥不闭合使 base IRR 精度受限，但双口径都指向价格贵。regime 细读：半导体/存储暴跌对 AMZN 混合偏中性（内存买方 + 自研隔离），非纯利空。详见 decision_card.json / delta_vs_0619.md。

## OPEN（封顶完整度）
**O0 Q2-2026 未出（7/30，迫近）** · O1 10-K 逐行 · O2 10 年精确序列 · O3 proxy/operator 细节 · **O4 $200B capex 维护/增长拆分 + ROIC（blocking，owner-earnings 桥胜负手）** · O5 backlog/Trainium 一手 · O6 Anthropic 会计。
