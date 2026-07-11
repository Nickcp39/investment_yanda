# TER Decision Card — as_of 2026-07-10

**pipeline_version**: lean-6module-v1.1 · **weights_version**: none · **run_date**: 2026-07-10
**context_label**: cyclical_ate_duopoly_at_peak_multiple__robotics_option_loss_making
**status**: DECISION_DRAFT · **completeness**: ~58%

> Batch: AI-robotics 4-leaders (`companies/_ai_robotics_2026-07-10/`). TER = "the only one with real deployed robotics revenue" (UR cobots + MiR AMRs). **Finding: robotics is ~7% of revenue and loss-making; the value engine is cyclical semiconductor test (ATE) at a probable earnings peak.**

## 锁定结论
| 字段 | 值 |
|---|---|
| as_of price | **$359.60**（2026-07-10 收盘，≤ as_of；Yahoo + stockanalysis 双源）|
| market cap | **~$56.29B**（156.54M 股 × $359.60）|
| 52wk range | $88.60 – $487.91（现价 −26.3% 距高点，+306% 距低点）|
| business_verdict | **good**（ATE 是优质双寡头，但周期性；robotics 拖累）|
| new_money_verdict | **WATCH（0%）** |
| existing_position_verdict | **HOLD** |
| suggested_initial / max size | **0% / 0%（新钱）** |
| buy_below | **~$270**（起步观察价，非公允 MOS；真 MOS ~$180–220）|
| verdict ceiling | 完整度 ~58% → **WATCH（40–60 区间）**；价格+周期门同向压到 WATCH |
| binding_constraint | **价格 + 周期位置（无 MOS，半导体测试需求处 late/可能顶）** |

## 六模块信号
| 模块 | 角色 | 信号 | 信心 | 一句话 |
|---|---|---|---|---|
| M1 证据脊柱 | confidence | **+2** | high | Q1'26 + FY2025 全一手；多年营收序列+价格双源交叉 |
| M2 主题/机制 | context+conviction | **+1** | high | 钱在半导体测试(86.6%)的 AI 测试超级周期；robotics 只是 7% 且亏损——**thesis 错配** |
| M3 利润池/耐久 | conviction | **+1** | med | Semi Test = 真 ATE 双寡头(高壁垒但周期)；Robotics = 低壁垒、亏损、低于盈亏线 |
| M4 财务现实 | conviction | **+1** | med | 高质量但周期；2026 是峰值(Q1 单季 NI ≈ FY25 的 72%)，Q2 指引环比下滑 |
| M5 反演/陷阱 | risk | **−1** | med | 无结构性破裂/无资产负债表风险；但 capital-cycle 顶 + robotics 概念陷阱 = size/no-chase 输入 |
| M6 定价/仓位 | price+output | **−2** | high | ~40–43x 峰值 2026E、~102x FY25、~65x+ 正常化；三情景 bull 仅 +2.3% IRR，base −15%、bear −26% → **无 MOS，负不对称** |

## capital_cycle lens（针对 robotics 段判，附 semi-test 注）
- **applicable**: partial · **stage**: robotics = early/trough-exiting；semi-test(主导) = late/可能顶 · **supply_barrier**: robotics = low-med；semi-test = high(ATE 双寡头)
- **read**: robotics 段供给能响应、无硬瓶颈、且低于盈亏线——是**期权/概念**不是 NVDA 式锁死瓶颈；不知道复苏是真需求拐点还是工业自动化周期回归。主导的 semi-test：可见 70% AI 营收 + ATH margin = 共识 late-cycle，2026-07 HBM 过剩抛售 = 供给侧信号。
- **caution**: **PEAK（semi-test，价值驱动）→ 压向 WATCH/no-chase**；robotics = TROUGH-WATCHLIST（只观察，不加 size）。

## 价格带（见 model/scenario_model.csv，锚 $359.60）
- **No new money @ $359.60** — 硬 no-chase。
- **Watch→Starter 观察**: ~$250–280（`buy_below ≈ $270`），fwd ~28–32x，结构化小仓 3–4%，仍是"AI 台阶是结构性"的赌注。
- **Add（真 MOS）**: ~$180–220，周期恐慌洗盘但不破 ATE 双寡头 → 加向 8–10%（周期封顶）。
- **下行**: bear ~$79（净现金可存活，非永久减值，只是周期 de-rate）。

## 三情景（5y IRR @ $359.60）
| 情景 | y5 EPS | 退出 P/E | y5 价 | 5y 总回报 | 5y IRR |
|---|---:|---:|---:|---:|---:|
| Bull（AI 测试结构性台阶） | $11.50 | 35x | ~$402 | +11.8% | **+2.3%** |
| Base（2026 是周期顶，回归） | $5.75 | 28x | ~$161 | −55.2% | **−14.8%** |
| Bear（顶+内存过剩下行；robotics→0） | $3.58 | 22x | ~$79 | −78.0% | **−25.6%** |

> 连 bull 都只勉强跑平，base/bear 大幅为负 → 现价负不对称。对比 NVDA：那是"卓越非周期生意，仅价格贵"(base +4.8%)；这里是"价格贵 + 周期峰值 + robotics 期权亏损"，对新钱严格更差。

## Kill Criteria
K1 Semi Test 营收/订单连续 2 季环比下滑（AI 测试是 pull-forward 峰非结构台阶）· K2 HBM/内存测试或 AI-ASIC 测试过剩（2026-07 抛售的恐惧成真）· K3 Robotics 持续低于 ~$365M 盈亏线/亏损扩大 → 期权减记至 ~0 · K4 Advantest/新进者结构性夺 SoC/内存测试份额（唯一可升 veto）· K5 GM 跌破 ~55% 周期底或大额库存减记 · K6 价格持续 >~$270 无正常化盈利支撑 → 维持 WATCH/no-chase（现已触发）。

## 批次 thesis 直答（详见 thesis_answer.md）
(a) **robotics 收入占比** = 7.1%(Q1'26 $91M/$1,282.5M) / ~9.6%(FY2025 ~$308M/$3,190M)。(b) **真是预期?** robotics 需求既非暴增亦非现金——FY 亏损、低于盈亏线、5 年停滞；真正暴增的是**半导体测试**(周期性 AI capex)。(c) **capital_cycle**（robotics 段）= partial/early-trough/低壁垒/无硬瓶颈；semi-test = PEAK caution。(d) **真瓶颈 vs 概念**: ATE = 真双寡头瓶颈(但周期)；robotics = 概念/低壁垒。(e) **拆分**: 现价 ~95%+ 买的是周期 ATE，~3–5% 是亏损的 robotics 期权——**买的不是具身智能龙头**。

## runner_dissent
机械模块(M1+2/M2+1/M3+1/M4+1)看似能撑 STARTER，ATE 双寡头确属优质；但我 override 到 WATCH：(1) M6 是 −2 不是 −1——不同于 NVDA(仅价格问题、生意卓越非周期)，这里是**峰值周期盈利上的贵倍数**，价格与周期位置同时不利；(2) 批次看 TER 的真正理由(已部署 robotics 收入)在证据面前**证伪**——robotics 7%、亏损、低于盈亏线，没有"已在赚钱的 robotics 瓶颈"；(3) capital-cycle PEAK + 2026-07 内存过剩抛售 = late-cycle 非买点。完整度 ~58% 无论如何封顶 WATCH。方向：ATE 半边质量对，价格错、robotics thesis 错 → WATCH，STARTER 触发在 ~$250–280(非峰值盈利)。

## OPEN（封顶完整度 ~58%）
O1 Q1'26 10-Q 资产负债/债务 · O2 分部经营利润(2025/2026) · O3 proxy/operator life-arc · O4 FY2025 robotics 精确值(~$308M 推算) · O5 Advantest 份额趋势 · O6 AI 测试是结构台阶还是 pull-forward 峰(核心 open)。
