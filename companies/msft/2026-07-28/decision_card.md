# MSFT Decision Card — as_of 2026-07-28

`lean-6module-v1` · weights `none` · run_date `2026-07-28` · **DECISION_DRAFT**（非 COMPLETE）
context: `quality_compounder_de-rated_capex-audit_pre-Q4-binary`

## 结论(两轴)
| 轴 | 结论 | 变化 vs 6/19 |
|---|---|---|
| **生意** | `exceptional` | 不变 |
| **新钱 new_money** | **`STARTER`** · 初始 **3%** · 上限 **9%** | 方向不变;初始 4%→3%(MOS 变薄+二元事件) |
| **存量 existing** | **`HOLD`** | ADD→HOLD(价涨出回补区+财报在即) |
| **buy_below** | **$436**(no-chase) | 不变 |

- 现价 **$393.35**(2026-07-28 close;三源 0.0% 一致)· 市值 ~**$2.922T** · P/E ~23.3×
- base 10y IRR **~9.1%**(>8% 门槛,变薄)· MOS 到 $436 **~10%** · bull ~14.8% / bear ~−0.3%(breakeven)
- 距 52 周高 **−29.2%**($555.45)· 距 52 周低 **+12.6%**($349.20)

## 六模块信号
| 模块 | 角色 | 信号 | 一句话 |
|---|---|---:|---|
| M1 证据 | confidence | **0** | 现价 $393.35 三源重验无 bug;完整度 ~63%,收敛缺口的 Q4/10-K 未在手 |
| M2 主题 | context | **+1** | thesis 无破;OpenAI $250B Azure 承诺强化需求;MSFT 是轮动相对受益方 |
| M3 护城河 | conviction | **+2** | 多护城河+RPO $627B+operator 5/5+一股一票;内存降价是成本顺风 |
| M4 财务 | conviction | **+1** | **Q4 未出(7/29 盘后)**;carry Q3/FY25;capex-审计年待验;actuals pending |
| M5 反演 | risk | **−1** | 无硬 veto;F1 capex ROI + F3 需求裂缝?+ F4 OpenAI 集中度;+K-F |
| M6 定价 | price | **+1** | $393.35 仍有正 MOS 支持开仓;但薄化+二元事件→更小/分批 |

## binding constraint
**研究完整度 ~63%(非价格)**：O2 capex 维护/成长拆分仍全开(OE 区间 $73–125B、base $112B 是假设)、O3 OpenAI 经济学收窄未闭合、O4 分部利润率未取。完整度 <80% 封顶 STARTER、堵 CORE。**叠加时点约束**:收敛这些缺口的 Q4 FY26 财报+10-K 于 **2026-07-29 盘后**发布(同日 FOMC/Warsh)——买在盲区是本轮执行风险。价格端本身仍有 ~10% MOS。

## kill 标准(监控)
- **K-A** capex/OCF >70% 连两年+FCF/股降+无 ROIC(现 ~57% 🟡,7/29 看全年)
- **K-B** Azure ≤+25% 连两季(需求归因)(Q4 指引 +39-40% cc 🟢)
- **K-C** OpenAI 经济学恶化 / $250B Azure 承诺反悔(4/27 重组偏正 🟢🟡)
- **K-D** AI run-rate 塌+Copilot 走弱(现 $37B/+123% 🟢)
- **K-E** IRR <8%(价 >$436)(现 ~9.1% 🟢,变薄)
- **K-F(新)** 半导体暴跌被 7/29 证实为 AI 需求裂缝(Azure 实际减速)/ capex 大超且无 ROI 框架 → 不加、重审。内存降价对 MSFT 是成本顺风勿误读

## runner dissent(诚实)
有强理由**等一天**:收敛所有缺口的 Q4+10-K 与 FOMC 都在 7/29 盘后;在半导体暴跌+capex-审计年里、IRR 仅微超门槛、MOS 变薄时买在二元事件盲区,可议为 WATCH-穿越-财报。我保留 STARTER 方向(方法论不把不确定性当 veto;starter 就是小额试;print 可能跳空向上使入场消失;MSFT 仍是 Mega7 里唯一正 MOS+净现金+一股一票的相对优选),但**初始收到 3% 并建议分批**(1.5% 财报前可选 / 确认后补齐),或直接等 7/29 落地看反应。存量 ADD→HOLD 纯因价涨 3.7% 出回补区+二元在即,无卖出触发。最大未验依赖仍是 O2(整个 owner-earnings base $112B 依赖 ~40% capex 为成长的假设),capex-审计 regime 抬高了在这一点上判断错误的代价。

## 关键来源
Yahoo chart API + stockanalysis.com($393.35, 2026-07-28)· MSFT Q3 FY26 IR(4/29)· FY25 10-K · MSFT IR 财报日公告(7/08, Q4 定 7/29 盘后)· OpenAI $250B Azure 承诺 · batch PLAN(regime)。完整见 `decision_card.json` sources_used + `freshness.json`。
