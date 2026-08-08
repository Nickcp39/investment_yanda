# ORCL Research Status — run_date 2026-08-07

## 状态标签

**`DECISION_DRAFT`** — **不是 `COMPLETE`**。

> 措辞纪律（CHECKER §1）：本轮**未**跑完全部 gate，因此**不得**说"完成 / 彻底跑完 / research complete"。
> 正确表述：**"完成到决策草案（DECISION_DRAFT），被 Gate B / Gate C 阻塞。"**

| 字段 | 值 |
|---|---|
| pipeline_version | `lean-6module-v1.1` |
| weights_version | `none` |
| run_date | 2026-08-07 |
| **as_of** | **2026-08-06**（最后已结算收盘；08-07 美东 13:45 市场仍在交易）|
| as_of_price | **$143.47** |
| **completeness** | **~58%** |
| verdict ceiling | **WATCH**（58% 落在 40–60% 档）|
| 实际 verdict | **WATCH** — **未超顶** ✅ |
| 数据新鲜度 | **PASS**（`freshness_check.json`，exit 0，T1–T6 全绿）✅ |

## 本轮完成了什么

| 产出 | 状态 |
|---|---|
| `step0_plan.md` | ✅ 范围/完成标准/方法论风险先于结论冻结 |
| `facts.md` | ✅ 每条带 source_id；一手 vs 媒体分层 |
| `raw/` × 4 | ✅ **8-K 完整损益表、五年三表、价格序列、媒体摘录全部落盘** |
| `business_model.md` | ✅ 两台机器的经济性对比 |
| `value_chain_map.md` | ✅ 含与四家的链条位置对照 |
| `bottleneck_map.md` | ✅ **含完整版「回喂」序列清单** |
| `moat_map.md` | ✅ 含 M-B（Multicloud DB）这条被低估的路线 |
| `financials/financial_quality.md` | ✅ (a)(b)(c) 三问的完整回答 |
| `operator_underwriting.md` | ⚠️ **不给评分**（一手证据不足，O7）|
| `inversion_map.md` | ✅ 含与四家的失败路径对照表 |
| `valuation.md` | ✅ 三情景 + **锚点敏感性自曝** + 价格梯子 |
| `decision_card.md` / `.json` | ✅ 版本戳齐全 |
| `ic_panel.md` | ⚠️ **简版**（无第二轮批判，无引语）|
| `model/scenario_model.csv` | ✅ 含三档敏感性行 |
| `claim_ledger.csv` | ✅ 60 条，带 tier + 验证状态 |
| `source_register.md` | ✅ 含"未能取得的来源 → OPEN"对照表 |
| `freshness.json` + `freshness_check.json` | ✅ **PASS** |
| `completion_checker.md` | ✅ |

## Gate 勾选（对照 `_mega7_2026-06-19/CHECKER.md`）

| Gate | 状态 | 未过项 |
|---|:--:|---|
| **A. Scope & Definition** | ✅ | — |
| **B. Evidence** | ❌ | **无任何 A1 级直连来源**（sec.gov / oracle.com 全部 403）。8-K 走复刻页（A1-proxy），已与独立聚合器逐行对账。电话会 transcript 未取得 → CFO ROIC 表述为二手 |
| **C. 11-Stage 覆盖** | ❌ | 八模块各有产物 ✅；但 **Stage 8 IC Panel 为简版**（无第二轮批判）；operator 模块不给评分 |
| **D. Model & Math** | ✅ | 三情景与假设对账、implied expectations 从当前价反推、owner earnings 桥显式且**自曝不闭合**、公式可审计（`scenario_model.csv`）|
| **E. Open Questions** | ✅ | 10 项全部分类 blocking/monitoring/non-blocking；blocking 项显式封顶 |
| **F. Audit & Consistency** | ✅ | 数字前后一致（T5 机械校验通过）；版本戳齐；状态标签诚实 |
| **活体新增：数据新鲜度（机械门）** | ✅ | `verify_freshness.py` exit 0，T1–T6 全绿，独立重抓 $143.47 完全一致 |

**结论：B 与 C 未过 → 不得标 COMPLETE。当前标签 `DECISION_DRAFT` 是诚实的。**

## 阻塞项（决定下一轮做什么）

| 优先级 | OPEN | 需要的来源 | 一旦关闭会怎样 |
|:--:|---|---|---|
| **1** | **O1** OpenAI 信用 + 10-K 客户集中度原文 | OpenAI 财务报道；ORCL 10-K | **解除 binding_constraint。若正面，buy_below 可从 $101 上调至 ~$121**（见 ic_panel Marks 少数意见）|
| **2** | **O5** 维护 vs 增长 capex 拆分 | 10-K / 电话会 | base IRR 在 +0.9% ~ +9.7% 之间收敛 → 可能直接翻转裁决 |
| **3** | **O2** 折旧年限 | 10-K 会计政策 | 决定 D&A $9,315M 是否被低估 |
| **4** | **O3** 资本化利息 | 10-K | 决定真实资金成本是否高于 22.3% 的 EBIT 占比 |
| 5 | **O4** 电话会一手 transcript | Motley Fool / 公司 IR | 验证 CFO "high 20s" 与 ROIC 口径原文 |
| 6 | **O6** OCI 分部毛利率 | The Information / 10-K | C5 / K-E 的直接读数 |
| 7 | **O7** Form 4 / DEF 14A | SEC | operator 模块可给评分 |
| 8 | O8 / O9 / O10 | 卖方预期史 / CDS / 完整 BS | 精度提升，不改裁决 |

## 本轮的运行限制（如实记录）

1. **`sec.gov` / `oracle.com` / `investor.oracle.com` 全部返回 HTTP 403**（机器人拦截）→ 无 A1 级直连来源。
2. **WebSearch 预算在中途耗尽（200/200）** → 其后仅能在已发现的 URL 上用 WebFetch 取数，
   O1（OpenAI 财务）、O6（The Information 报道）、O9（CDS）因此无法关闭。
3. **子 agent 在本轮被禁用**（前一段运行因 fan-out 耗尽预算而中断）→ 全部研究由主线程串行完成。
4. 上述三条**已如实反映在 completeness 58% 中**，未以"完成度更好看"的方式表述。

## 下一轮触发条件

- **Q1 FY2027 财报（预计 2026-09-14）** —— 首个可检验点：
  毛利率是否如管理层预告继续 "step down"？RPO 是否续增？capex 是否按 $70B 净现金路径执行？
- **任何 OpenAI 的融资/收入/合约新闻** → 直接作用于 O1。
- **任何评级动作**（S&P 跌破 BBB− 或 Moody's 下调）→ K-D。
- **价格跌破 ~$121.50 或 ~$101** → 触发梯子复核（但须先看 O1 状态）。
- **回喂清单的用途**：GOOGL/AMZN/META/MSFT 中**任何一家跨过 C7（开始发股权融 capex）**
  → 立刻把本卡的 `## 回喂` 章节重读一遍并应用。
