# NVDA Decision Card — as_of 2026-06-19

**pipeline_version**: lean-6module-v1 · **weights_version**: none · **run_date**: 2026-06-19
**context_label**: exceptional_bottleneck · **status**: DECISION_DRAFT · **completeness**: ~65%

## 锁定结论
| 字段 | 值 |
|---|---|
| as_of price | **$145.48**（2026-06-18 收盘，≤ as_of）|
| market cap | **~$3.55T**（24,391M 稀释股 × $145.48）|
| business_verdict | **exceptional** |
| new_money_verdict | **STARTER** |
| existing_position_verdict | **HOLD** |
| suggested_initial_size | **4%**（区间 3–5%）|
| suggested_max_size | **~12%**（Confirmed 封顶，周期股不进 Core）|
| buy_below | **~$150**（现价区即可建仓）|
| verdict ceiling | **STARTER**（完整度 ~65% → 60–80% 区间）|
| binding_constraint | **run-rate 可持续性（pull-forward + custom-silicon 份额），非价格** |

## 六模块信号
| 模块 | 角色 | 信号 | 信心 | 一句话 |
|---|---|---|---|---|
| M1 证据脊柱 | confidence | **+2** | high | 锚定季度+全年全回挂 A1/A2；缺口=haircut |
| M2 主题/机制 | context+conviction | **+2** | high | 全栈 AI 算力瓶颈，多季一手坐实（DC +92%、网络 +199%、Q2 指引 $91B）|
| M3 利润池/耐久 | conviction | **+2** | med | CUDA+全栈+网络捕获最大利润池；operator 4/5；推理份额是战场 |
| M4 财务现实 | conviction | **+2** | high | owner earnings 干净(capex-light, FCF=OE ~$182B)、净现金 $72B；无 capex 黑洞 |
| M5 反演/陷阱 | risk | **−1** | med | pull-forward + custom-silicon = size 控制；无结构性破裂/无资产负债表死亡 → 非 veto |
| M6 定价/仓位 | price+output | **+1** | med | forward 19x、yield 5.1%、base IRR +13%、贴 52 周低 → 价格友好，结构化 starter |

## 价格带
- **Starter 主锚**: $130–150（现价区），initial 3–5%。
- **Add zone**: $110–130（向 52 周低破位）或营收连续兑现指引后 → 加向 8–12%。
- **No-chase**: > ~$200（隐含 IRR <8%）。
- **下行参考**: bear ~$80（−45%，可存活非永久减值）。

## 三情景（5y IRR，hurdle 8%）
| 情景 | OE 起点 | CAGR | 退出 P/OE | y5 每股 | 5y IRR |
|---|---:|---:|---:|---:|---:|
| Bear | $160B | −8% | 18x | ~$80 | **−11%** |
| Base | $182B | +12% | 20x | ~$266 | **+13%** |
| Bull | $185B | +22% | 24x | ~$495 | **+28%** |

## Kill Criteria
K1 营收实质 miss $91B 指引 / K2 DC 连续环比降或 GM<65% / **K3 大规模 CSP 迁出致份额结构性下滑（唯一可升 veto，exit 候选）** / K4 库存承诺大额减值 / K5 价格 >~$200（IRR<8%）/ K6 Huang key-man。

## runner_dissent
现价贴 52 周低可能是市场提前嗅到 AI capex pull-forward 拐点，单季 $91B 指引无法证伪 run-rate 中的抢装成分。但与 GOOGL 不同，**价格不是卡点**（forward 19x 已隐含减速、owner earnings 干净、资产负债表死不了、bear 可存活）→ 框架据客观事实给 STARTER 而非 WATCH；前瞻不确定性控制 size（封 Confirmed ~12%）、不否决。详见 decision_card.json。

## OPEN（封顶完整度）
O1 10-K 逐行 · O2 10 年精确序列 · O3 proxy/operator 细节 · O4 custom-silicon 定量份额 · O5 China 损失量级 · O6 供应承诺/库存风险。
