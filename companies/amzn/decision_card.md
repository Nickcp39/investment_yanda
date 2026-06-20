# AMZN Decision Card — as_of 2026-06-19

**pipeline_version**: lean-6module-v1 · **weights_version**: none · **run_date**: 2026-06-19
**context_label**: good_business_wrong_price_capex_reinvestment · **status**: DECISION_DRAFT · **completeness**: ~62%

## 锁定结论
| 字段 | 值 |
|---|---|
| as_of price | **$244.39**（2026-06-18 收盘，≤ as_of）|
| market cap | **~$2.66T**（10,874M 稀释股 × $244.39）|
| business_verdict | **good**（引擎质量 good→exceptional，现金转化在重投资期受压）|
| new_money_verdict | **WATCH** |
| existing_position_verdict | **HOLD** |
| suggested_initial_size | **0%** |
| suggested_max_size | **0%**（升 STARTER 前不建仓）|
| buy_below | **~$175–180**（base 5y IRR 回 8% 门槛）|
| verdict ceiling | **WATCH**（价格封顶，先于完整度 62% 的 STARTER 封顶生效）|
| binding_constraint | **价格无 MOS（起始收益率 2.1–2.5%、base IRR 负）+ owner earnings 桥因 $200B capex 不闭合**，非生意质量 |

## 六模块信号
| 模块 | 角色 | 信号 | 信心 | 一句话 |
|---|---|---|---|---|
| M1 证据脊柱 | confidence | **+2** | high | 锚定季度+全年全回挂 A1（SEC 8-K Ex99.1 落盘）；缺口=haircut |
| M2 主题/机制 | context+conviction | **+2** | high | 三引擎复利机器；AWS 重新加速 +28%、零售利润率创纪录；新主题=$200B AI capex 豪赌 |
| M3 利润池/耐久 | conviction | **+1** | med | AWS 捕获西方第二大云利润池；operator 4/5；非独占瓶颈→不享瓶颈溢价 |
| M4 财务现实 | warning | **−1** | med | **owner earnings 桥不闭合**：FCF 近零($1.2B)、capex 吞 OCF；GAAP 含 $16.8B Anthropic 收益；加杠杆 |
| M5 反演/陷阱 | risk | **−1** | med | capex ROI/AWS 份额=size 控制+监控；无结构性破裂/资产负债表能存活 → 非 veto |
| M6 定价/仓位 | price+output | **−1** | high | 起始收益率 2.1–2.5%、base IRR −1.5%（给足 capex 信用）、贴 52 周高 → **价格是卡点** |

## 价格带
- **现价 $244 = 不追**（base IRR 负、bull 才勉强够门槛）。
- **Watch 观察**: ~$180–195。
- **Starter 候选**: ≲ $175（base IRR 回 8% 门槛，约 52 周低附近）→ **解 WATCH 封顶**。
- **下行参考**: bear ~$118（−52%，资产负债表存活）。

## 三情景（5y IRR，hurdle 8%）— headline 用 NOPAT 口径（给足 capex 信用）
| 情景 | NOPAT 起点 | CAGR | 退出倍数 | y5 每股 | 5y IRR |
|---|---:|---:|---:|---:|---:|
| Bear | $60B | +6% | 16x | ~$118 | **−13.5%** |
| Base | $67B | +13% | 20x | ~$227 | **−1.5%** |
| Bull | $70B | +18% | 24x | ~$353 | **+7.7%** |

> 即便给足 capex 信用，base IRR 负、bull 仅 +7.7%（<8%）。保守 owner earnings 口径更低。赔率向下不对称。

## Kill / 升档 Criteria
K1 capex 大增但 AWS 增量利润不匹配（ROIC 恶化，唯一可升 veto）/ K2 AWS <15% 且份额走弱 / K3 总营业利润率<9% / K4 净债务恶化+OCF 停滞 / **K5 价格跌破 ~$175 → 解封顶升 STARTER** / K6 Anthropic 公允价值反向失真。

## runner_dissent
机械结论 WATCH **正确**——教科书式"好生意错价格"，与 GOOGL 同构。两个反向风险记录: ①too_small_missed_asymmetry（修好的老病）——若 $200B capex 是又一个 AWS，WATCH 会错过 → 故给 WATCH 不给 REJECT，留 STARTER 升档线（价格 ≤$175 或 capex ROI 兑现）；②owner earnings 桥不闭合（O4）使 base IRR 精度受限，但双口径都指向价格贵，WATCH 稳健。与 NVDA 关键差异: 价格不友好（起始收益率 2.1–2.5% vs 5.1%）、FCF 近零 vs 干净。详见 decision_card.json。

## OPEN（封顶完整度）
O1 10-K 逐行 · O2 10 年精确序列 · O3 proxy/operator 细节 · **O4 $200B capex 维护/增长拆分 + ROIC（blocking，owner earnings 桥胜负手）** · O5 backlog/Trainium 一手 · O6 Anthropic 会计。
