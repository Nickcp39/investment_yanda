# NFLX Completion Checker（Stage I 自审）

Ticker: NFLX | As-of: 2026-08-06 | Run: 2026-08-07 | Pipeline: lean-6module-v1.1
审计者：**Runner 自审**（独立 Checker 尚未跑 —— 这本身是升 COMPLETE 的前置条件之一）

---

## Stage I 审计清单

**Source coverage**
- SEC 一手 14 项（10-K 4 视图、10-Q 7 视图、8-K 2、EDGAR 索引）+ 4 份股东信 + 3 个价格源。
- ❌ **竞争对手一手证据 0 项**（未达 P1）——O4。
- ❌ **Proxy / 治理一手 0 项**（未达 P1）——O7。
- ✅ 情绪/KOL 材料 0 项被用作论据。

**Key claims without source_id**
- 无。43 条 claim 全部带 source_id + URL + public_date（`claim_ledger.csv`）。
- 派生值（市值、比率、IRR、锚）统一标 `DERIVED` 并给出算式。

**Conflicting numbers**
- 检出 1 处并已解决：公司自报 TTM FCF $11,151M vs 逐行计算 $11,152M ——
  **$1M 差异为四舍五入**，双向确认，无实质冲突。
- 检出 1 处需长期注意：FY26 FCF 指引"剔一次性"有两种口径
  （税前全剔 $9.7B vs 管理层税后口径 $11.0B）。**未强行统一，两者都进敏感性表。**

**Stale facts**
- 最新一手财务：Q2'26 10-Q（2026-07-17），距 as_of **20 天**。✅
- 最新指引：Q2'26 股东信（2026-07-16），距 as_of **21 天**。✅
- ⚠️ `active_litigation` 源为 FY2025 10-K（2026-01-23），距 as_of **195 天** ——
  **T6 WARN，已接受**：年报是或有事项的权威披露，且 Q2'26 10-Q 未浮现新的重大事项。

**D1/C2 contamination（叙事/情绪污染）**
- ✅ 无。本 dossier 未使用任何媒体、卖方或 KOL 材料作为论据。
- ⚠️ **主动隔离 1 项**：子代理提供的"Netflix 在美国电视时长退居第 4"线索，
  因原始 URL 丢失无法核验 ⇒ 明确标注为未验证，隔离在 `raw/` §8，
  **未进入 facts.md，未用于任何论证链，未影响裁决**。
  它转为 O4 监控项并**计入压低 completeness 的理由**。

**Math/model errors**
- 复核项与结果：
  - 市值恒等式：4,163.94M × $73.69 = $306,840.7M ✅（T3 PASS，0.00%）
  - FCF 定义勾稽：FY23/FY24/Q1'26/Q2'26 四点全部对上公司自报 ✅
  - TTM 滚动（FY2025 − H1'25 + H1'26）逐项复算 ✅
  - **回撤恒等式**：每股 OE +0.3% × 倍数 −45.2% = −45.0% = 实际股价变动 ✅ **精确闭合**
  - GAAP 交叉验证：EPS +12.8% × 倍数 −51.2% = −45.0% ✅ **同样闭合**
  - 七个锚的 IRR 逐个复算，与 `model/scenario_model.csv` 一致 ✅
  - 财报日复合：0.949×0.8993×0.9782×0.9028×0.9274 = 0.6990 → −30.1% ✅
- **未发现算术错误。** 两条独立恒等式同时精确闭合，是本次计算可信度的最强证据。

**Missing primary sources**
- ❌ Nielsen The Gauge（竞争份额）——**最实质的缺口**，O4。
- ❌ DEF 14A（薪酬/持股/董事会/继任）——O7。
- ❌ Q3'25/Q1'26 股东信原文未逐字提取（仅用其汇总数据，已由 Q2'26 信的五季度表覆盖）——影响很小。

**Management claims not verified**
- "price changes ... consistent with prior price changes and our expectations" ——
  **无法验证**（提价幅度与流失率均未披露）。已在 `business_model.md` §2 标注为管理层口径。
- "GenAI ... lower cost than traditional methods" —— **零量化**，O6。
  已明确不给任何数字，只转为可证伪命题。
- FY2026 各项指引 —— 尚未兑现。**缓解证据**：FY2025 四项指引全部达成或超出，
  且管理层主动披露自家好数字里的水分（$700M 巴西时点、$2.8B 分手费影响）——
  指引可靠性有 track record 支撑，但**不等于已兑现**。

**Valuation assumptions too aggressive?**
- 自查结论：**偏保守，不偏激进。**
  - 锚取中点 $10.0B，**低于**管理层前瞻口径 $11.0B，且**不给"稳态 1.0x"任何信用**；
  - 退出倍数 base 20x（对一个 100% 经常性收入的年金不算慷慨；bull 才用 24x）；
  - base OE CAGR 10%，**低于** FY26 指引隐含的 20%+ 经营利润增长；
  - 回购 −2%/yr，**低于**实际年化 −2.7%。
- **唯一可被质疑为激进的假设：base 隐含"现金转化停止恶化"**（比率从 1.13x 缓降到 1.05x）。
  ⚠️ **这一条今天没有数据支持**，已在 `decision_card.md` runner_dissent 与
  `inversion_map.md` §3 明确点名为"整张卡的承重墙"。

**Risks not quantified**
- ✅ F1（内容跑步机）：已量化 —— bear −3.8%/yr。
- ✅ F4/F6/F7：已在情景与锚敏感性中体现。
- ❌ **F2（注意力替代）未量化** —— 缺 O4 的份额数据，只能定性。
- ❌ **F3（AI 摧毁规模摊薄）未量化** —— 长周期尾部风险，10 年 IRR 模型无法表达
  （它推翻的是退出倍数假设本身）。**已通过把 max size 封在 6% 来处理**，
  而不是假装它进了模型。

**Verdict ceiling**
- completeness ~62% ⇒ 规则上限 **STARTER**。
- 实际裁决 **WATCH**，由**锚不确定性 + base IRR 差 0.5pp** 压到上限之下。
- ⇒ **上限未被触碰，裁决不是被完整度绑架的。** ✅

---

## Freshness gate

```
STATUS: PASS (exit 0)
price: card=73.69  refetched_yahoo=73.69 (2026-08-06)  -> PASS (2 independent sources within 1%)
T1 52wk band containment ........ PASS  65.08 <= 73.69 <= 126.71
T2 low/high hug ................. PASS  +13.2% off low, -41.8% off high
T3 market-cap identity .......... PASS  0.00%
T4 distance-from-high reconcile .. PASS  narrative -41.8% vs implied -41.8% (gap 0.0pt)
T5 single value of truth ........ PASS  73.69 present in all price-bearing files
T6 guidance freshness ........... PASS  newest source 2026-07-17 (20d)
T6 active_litigation ............ WARN  newest source 2026-01-23 (195d)  <- accepted, see above
```

**拆股声明已显式落盘**（`freshness.json.SPLIT_ADJUSTMENT_DECLARATION`）：
10:1，公告 2025-10-30 / 登记 2025-11-10 / 分派 2025-11-14 / 首个调整后交易日 2025-11-17，
一手 8-K 确认，并用 10-K 对 FY2023 EPS 的重述（$12.03 → $1.20）做内部一致性验证。
**这是 INC-001 同型风险的定点防御。**

---

## 交付物清单

| 文件 | 状态 |
|---|---|
| `step0_plan.md` | ✅ |
| `facts.md` | ✅ 纯一手 |
| `business_model.md` | ✅ 含年金机制 + 量/价分离 |
| `value_chain_map.md` | ✅ |
| `bottleneck_map.md` | ✅ |
| `moat_map.md` | ✅ 结构性 vs 先发 |
| `financials/financial_quality.md` | ✅ |
| `operator_underwriting.md` | ⚠️ PARTIAL（proxy 未查，O7） |
| `inversion_map.md` | ✅ |
| `valuation.md` | ✅ **含锚敏感性表（核心交付物）** |
| `ic_panel.md` | ✅ |
| `decision_card.md` / `.json` | ✅ 版本戳齐全 |
| `claim_ledger.csv` | ✅ 43 条 |
| `source_register.md` | ✅ |
| `research_status.md` | ✅ |
| `model/scenario_model.csv` | ✅ |
| `freshness.json` / `freshness_check.json` / `.txt` | ✅ **PASS** |
| `raw/primary_extracts_fy2025_and_q2_2026.md` | ✅ |
| `raw/reconciliation_and_drawdown_math.md` | ✅ |
| `completion_checker.md` | ✅ 本文件 |

## 自审结论

**产出可用于决策，状态 DECISION_DRAFT，completeness ~62%。**

裁决（WATCH / 0% / buy_below ~$70.50）**建立在扎实的一手财务基础上**，
两条独立恒等式精确闭合，freshness gate 通过，无算术错误，无叙事污染。

**它的薄弱处已被诚实定位且未被掩盖**：竞争份额零证据（O4）、
proxy 零核查（O7）、以及最重要的——**owner-earnings 锚依赖一个公司从不披露的拆分（O1）**。
这三条中，**O1 是 binding constraint 并已被写进裁决本身**，
O4/O7 是下次刷新的首要补课项。

**一个诚实的 62% 胜过一个编造的 90%。**
