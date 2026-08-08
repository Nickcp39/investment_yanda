# NFLX Research Status

Ticker: NFLX | As-of: **2026-08-06** | Run: **2026-08-07**
Pipeline: **lean-6module-v1.1** | Weights: **none**

## 诚实状态：**DECISION_DRAFT**（不是 COMPLETE）· completeness **~62%**

一次 pass 的实时运行。**Freshness gate PASS（exit 0）**，价格双源 + 独立重取三向确认，
delta 0.00%，全部 6 条 tripwire 通过（1 条 WARN，已说明）。

**裁决的财务基础非常扎实**：FY2023–FY2025 与 Q1/Q2 2026 的每一个 load-bearing 数字
都是 SEC 一手（XBRL / R-file 直读），公司自报 FCF 与逐行计算相差 $1M。
**裁决的竞争与治理基础则明显偏薄**：竞争份额零一手证据（O4）、proxy 零一手核查（O7）。

完整度被压在 ~62% 的**实质原因有两类**，必须分开看：
- **(甲) 公司已停止披露**（研究做得再多也拿不到）：付费会员数、ARM、churn（O2）；
  广告底层指标（O3）；维护 vs 增长内容支出拆分（O1）。
- **(乙) 本次运行没做到**（下次可补）：竞争份额（O4）、proxy 治理（O7）、
  卖方远期倍数序列（O5）。

**(甲) 类是本案的结构性特征，不是研究缺陷**——它本身就是一条投资结论
（外部人验证年金质量的能力在系统性下降），已计入 K-E 与 M4 的扣分。

## 11 阶段清单

| # | 阶段 | 文件 | 状态 |
|---|---|---|---|
| 0 | Plan / thesis gate | `step0_plan.md` | ✅ DONE |
| 1 | Source register | `source_register.md` | ✅ DONE（竞品与 proxy 未达 P1，已标注） |
| 2 | Claim ledger | `claim_ledger.csv` | ✅ DONE（43 条，全部带 source_id + URL + 日期） |
| 3 | Facts（证据脊柱 M1） | `facts.md` | ✅ DONE（纯一手） |
| 4 | Raw extracts | `raw/primary_extracts_fy2025_and_q2_2026.md`、`raw/reconciliation_and_drawdown_math.md` | ✅ DONE |
| 5 | 商业模式 + 价值链 + 护城河 + 卡点（M2/M3） | `business_model.md`、`value_chain_map.md`、`moat_map.md`、`bottleneck_map.md` | ✅ DONE |
| 6 | 财务现实（M4） | `financials/financial_quality.md`、`model/scenario_model.csv` | ✅ DONE |
| 7 | Operator underwriting | `operator_underwriting.md` | ⚠️ **PARTIAL**——只承保了行为证据，**proxy 未核查（O7）** |
| 8 | 反演 / 陷阱（M5） | `inversion_map.md` | ✅ DONE |
| 9 | 估值 / 价格 / 仓位（M6） | `valuation.md`、`model/scenario_model.csv` | ✅ DONE（含**锚敏感性表**，本次核心交付物） |
| 10 | IC panel + decision card | `ic_panel.md`、`decision_card.md`/`.json` | ✅ DONE |
| 11 | Monitor + freshness | `freshness.json`、`freshness_check.json`/`.txt` | ✅ DONE（**PASS**） |

## Brief 五问的交付状态

| 问题 | 状态 | 交付位置 |
|---|---|---|
| **(a) 内容摊销 / owner-earnings 锚** | ✅ **完整交付** | `valuation.md` §2（七锚 + 敏感性表，跨度 4.4pp）；`business_model.md` §3；`raw/reconciliation_and_drawdown_math.md` §1–4 |
| **(b) 年金是否完好** | ⚠️ **部分交付（受公司披露限制）** | `business_model.md` §2。**量/价无法严格分离**——公司 2025 起停披会员数与 ARM。已给推断并标注为推断 |
| **(c) 为什么跌 45%** | ✅ **完整交付** | `raw/reconciliation_and_drawdown_math.md` §5–6：**≈100% 倍数压缩，每股 owner earnings +0.3%**，恒等式精确对上；另有财报日/WBD 时间分解 |
| **(d) AI 角度** | ✅ **已取立场且可证伪** | `decision_card.json.ai_position`（3 条可证伪命题）；`moat_map.md` §4。**无量化数据（O6）——公司未披露，拒绝编造** |
| **(e) 护城河结构性 vs 先发** | ✅ **完整交付** | `moat_map.md`：**唯一结构性腿 = 规模摊薄内容成本**；品牌/数据判定为先发。**但缺竞争份额一手证据（O4）** |

## 未通过的闸（补上才能升 COMPLETE）

1. **O1（胜负手）**：维护性 vs 增长性内容支出拆分 —— **公司从未披露**，
   直接决定锚（$8.35B–$12.5B，跨 4.4pp IRR）。**这是 binding constraint。**
2. **O4**：竞争份额（Nielsen The Gauge，Netflix vs YouTube 的电视时长占比与排名）——
   **零一手证据**。含一条**未核验**的"退居第 4"线索，已隔离在 `raw/` §8，未用于任何论证。
   这是 (e) 判断最缺的外部证据。
3. **O7**：proxy（DEF 14A）一手核查全缺 —— 薪酬/持股/董事会/继任未承保。
   **最该查的一条：薪酬是否与 FCF/每股指标挂钩**（若只挂营收与经营利润，
   激励与当前最关键的"现金转化"问题是错配的）。
4. **O2/O3**：会员数、ARM、churn、广告底层指标 —— **公司已停披**，外部不可得。
5. **O5**：卖方一致预期与远期倍数时点序列 —— (c) 的分解仅用已实现 TTM 现金流自建，
   方法上更保守但少一层交叉验证。
6. **独立 Checker 尚未跑**（本文件是 Runner 产出）。

## 最终裁决摘要

- **business_verdict: good**（不是 exceptional——护城河只有一条结构性腿，参与度仅 +2%）
- **new_money_verdict: WATCH**｜**existing: HOLD**｜初始仓位 **0%**｜max **~6%**
- **buy_below ~$70.50**（base 10y IRR = 8%），距现价 **−4.3%**——**本系列离买点最近的一张卡**
- **三情景 10y IRR：bear −3.8% / base +7.5% / bull +15.1%**（锚 $10.0B）
- **锚敏感性：+5.6% → +10.0%（跨度 4.4pp），8% 门槛的分水岭在 OE₀ ≈ $10.43B**
- **binding_constraint = owner-earnings 锚的不确定性（O1），不是生意质量，也不完全是价格**

## 下一个监控事件

**Q3 2026 财报（预计 2026 年 10 月中）** —— 本卡是本库第一张**"等数据 > 等价格"**的卡：

1. **现金内容支出 / 摊销比**是否如指引回落至 ≤1.05x（**K-A，胜负手**）
2. **FCF 同比**是否在 Q2 的 −32.7% 之后转正
3. **UCAN 营收增速**（提价全季生效后）是否回到 +10% 以上（K-B）
4. FY2026 广告收入是否在 ~$3B 轨道上
5. FY2026 FCF ~$12.5B 指引是否维持

> **若 K-A 解除，锚可上修至 A4（$11.0B），base 立即变 +8.6%，
> 本卡应当天翻 STARTER——不需要更低的价格。**
