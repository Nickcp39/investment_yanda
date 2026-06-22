# NVDA Decision Card — as_of 2026-06-20

**pipeline_version**: lean-6module-v1.1 · **weights_version**: none · **run_date**: 2026-06-20
**context_label**: exceptional_bottleneck_no_margin_of_safety · **status**: DECISION_DRAFT · **completeness**: ~65%

> CORRECTED RE-RUN. Supersedes `../2026-06-19/` (preserved as the error sample), which used **$145.48** — approximately the **52-week LOW ($142.03)** — as the current price. The real last close was **$210.69**. See `backtests/framework_validation/INCIDENTS.md` INC-001. This run passes the `verify_freshness.py` gate (price cross-checked vs Yahoo + stockanalysis + websearch).

## 锁定结论
| 字段 | 值 |
|---|---|
| as_of price | **$210.69**（2026-06-18 收盘，≤ as_of；3 源交叉验证）|
| market cap | **~$5.139T**（24,391M 稀释股 × $210.69）|
| business_verdict | **exceptional** |
| new_money_verdict | **WATCH（0%）** |
| existing_position_verdict | **HOLD** |
| suggested_initial_size | **0%**（现价无安全边际）|
| suggested_max_size | **0%（新钱）**；回调进 STARTER 区再开 |
| buy_below | **~$181**（base 5y IRR = 8% hurdle 的中性价）|
| verdict ceiling | **STARTER**（完整度 ~65% → 60–80% 区间）；价格门更严，封到 **WATCH** |
| binding_constraint | **价格（无 MOS）** — base IRR +4.8% < 8% hurdle，距高点仅 −11% |

## 六模块信号
| 模块 | 角色 | 信号 | 信心 | 一句话 |
|---|---|---|---|---|
| M1 证据脊柱 | confidence | **+2** | high | 锚定季度+全年全回挂 A1/A2；价格已 3 源交叉验证（v1.1 门）|
| M2 主题/机制 | context+conviction | **+2** | high | 全栈 AI 算力瓶颈，多季一手坐实（DC +92%、网络 +199%、Q2 指引 $91B）|
| M3 利润池/耐久 | conviction | **+2** | med | CUDA+全栈+网络捕获最大利润池；operator 4/5；$80B 回购但在 **near-high 而非低位** |
| M4 财务现实 | conviction | **+2** | high | owner earnings 干净(capex-light, FCF=OE ~$182B)、净现金 $72B；无 capex 黑洞 |
| M5 反演/陷阱 | risk | **−1** | med | pull-forward + custom-silicon = size 控制；China 改判：H200 许可重启=**可恢复期权**，非永久损失 |
| M6 定价/仓位 | price+output | **−1** | high | forward **28x**、yield **3.5%**、base IRR **+4.8% < 8%**、距高点 −11% → **价格无 MOS，是卡点** |

## 价格带
- **No new money @ $210.69** — 已在 ~$181 无 MOS 线之上。
- **Starter 区**: ~$155–181（base IRR 回到 8% hurdle 之上），initial 3–5%。
- **Add 区**: ~$142–155（向 52 周低，base IRR ~12–14%）或营收连续兑现指引后 → 加向 8–12%。
- **No-chase**: 现价即 no-chase；向 $236.54 ATH 硬不追。
- **下行参考**: bear ~$80（−62% from $210.69，可存活非永久减值）。

## 三情景（5y IRR @ $210.69，hurdle 8%）
| 情景 | OE 起点 | CAGR | 退出 P/OE | y5 每股 | 5y IRR |
|---|---:|---:|---:|---:|---:|
| Bear | $160B | −8% | 18x | ~$80 | **−17.6%** |
| Base | $182B | +12% | 20x | ~$266 | **+4.8%** |
| Bull | $185B | +22% | 24x | ~$495 | **+18.6%** |

> base **+4.8% < 8% hurdle** → 现价无安全边际。对比 2026-06-19 错版（用 $145.48 算出 base +13%）：那 +13% 其实是**52 周低点 $142 附近**的入场收益率，被错当成了今天的价格。

## Kill Criteria
K1 营收实质 miss $91B 指引 / 营收环比降 / GM<65% · K2 **大规模 CSP 迁出致份额结构性下滑（唯一可升 veto，exit 候选）** · K3 库存承诺大额减值（FY26 有 $4.5B H20 先例）· K4 价格持续 >~$181 且无估值上调 → 维持 WATCH/no-chase（现已触发）· K5 Huang key-man。

## runner_dissent
多头本能：卓越、自筹资金的瓶颈生意（FCF=OE ~$182B、净现金 $72B、DC +92%），bull 5y IRR +18.6%，为何不开小仓？框架override 到 WATCH，因为**这次价格就是卡点**：base 5y IRR +4.8% 低于 8% hurdle，股价距 ATH 仅 −11%（不在低位），单季 $91B 指引无法为"可能是周期顶的 run-rate"溢价买单。这与 2026-06-19 的 dissent（"价格不是卡点，$145 近 52 周低"）**正好相反**——那个推理致命地把 52 周低 $142.03 错当成了现价。改正后：真实 $210.69 无安全边际；WATCH，等回调进 ~$155–181（STARTER）或 ~$142–155（add）。生意质量无疑，入场价有疑。详见 decision_card.json。

## OPEN（封顶完整度）
O1 10-K 逐行 · O2 10 年精确序列 · O3 proxy/operator 细节 · O4 custom-silicon 定量份额 · O5 China H200 重启的金额量级 · O6 供应承诺/库存风险。
