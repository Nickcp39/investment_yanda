# Mega7 活体批次 — `mega7_2026-07-28`(现价正式重跑)

**批次 ID**: `mega7_2026-07-28` · **as_of**: 2026-07-28
**pipeline_version**: `lean-6module-v1` · **weights_version**: `none` · **run_date**: 2026-07-28
**方法**: 读 `mega7_2026-06-19` 各家 dossier 做**业务基线**(M2 主题 / M3 护城河·operator,6 周内不变,快速复核即可),用**今天的价**重算 **M4/M5/M6** + 叠加**当前 regime**,重导两轴 verdict。**不是从零重研究。**
**诚实目标**: `DECISION_DRAFT`(~55–75% 完整度),**不是 COMPLETE**。
**回测出处**: pipeline 经 10-case 验证(9 PASS / 1 FAIL,`backtests/framework_validation/`)。

---

## 新时间线的 regime(所有 Runner 必须叠加进 M4/M5/M6)
- **半导体暴跌(7/28)**:KOSPI 年内第 8 次熔断、SOX 从高点 −25%、SK 海力士腰斩。
- **轮动**:资金从 AI 硬件 / 存储 / 韩国科技撤 → 价值 / 消费 / 防御 + **苹果($5T,反超 NVDA)**。
- **"AI capex 审计年"**:市场拷问 $125–200B/yr 的 capex 多久转成 FCF;capex-ROI 是胜负手。
- **CXMT(长鑫)上市** +466% / ~$488B(超 Intel),2016 年成立 → 打存储"稀缺溢价",冲击任何 memory / AI-硬件敞口的 M3/M5。
- **本周 = Mega7 财报周**:每个 Runner 必须查 ≥ 6/19 有没有出 Q2-2026 财报并并入(M4 大刷新)。**FOMC 周三(Warsh 记者会)**,利率待定。
- 除 AAPL(在高点)外,6 家现价已从 52 周高 **−16%~−37%** → 入场 IRR/MOS 改善,但 capex 审计同时抬升风险。

## 现价锚(Yahoo chart API 已验;防 INC-001:latest ≠ 52 周极值)
| Ticker | as_of_price | 52wk hi | 52wk lo | 6/19 基线 | 6/19 新钱 verdict |
|---|---|---|---|---|---|
| AAPL | 340.08 | 340.08 | 201.50 | `2026-06-19` | WATCH |
| MSFT | 393.35 | 542.07 | 349.20 | `2026-06-19` | **STARTER**(唯一) |
| GOOGL | 333.71 | 402.62 | 187.82 | `2026-06-19` | WATCH |
| AMZN | 230.86 | 274.99 | 196.00 | `2026-06-19` | WATCH |
| NVDA | 197.01 | 236.54 | 164.07 | `2026-06-20`(修正) | WATCH |
| META | 593.41 | 790.00 | 520.26 | `2026-06-19` | WATCH |
| TSLA | 307.44 | 489.88 | 297.82 | `2026-06-19` | WATCH + 存量 TRIM |

## 三阶段(workflow;角色隔离 Checker ≠ Runner)
1. **Runner ×7**(并行):刷新 dossier + 锁 `2026-07-28` decision_card + freshness.json。
2. **Checker ×7**(独立):过 `_mega7_2026-06-19/CHECKER.md` → `checker_report.md`。
3. **Synthesis**:7 卡排序 + 单因子集中度(METHODOLOGY §5)→ `mega7_synthesis.md`(+ dashboard 由 orchestrator 建)。

## 每家产物 → `companies/<ticker>/2026-07-28/`
`decision_card.json`/`.md` · `valuation.md`(现价) · `inversion_map.md`(叠 regime) · `delta_vs_0619.md`(变了什么+为什么) · `research_status.md` · `freshness.json` · `checker_report.md`
