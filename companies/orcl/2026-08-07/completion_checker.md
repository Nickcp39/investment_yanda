# ORCL Completion Checker — run_date 2026-08-07

> Runner 自查（**非独立 Checker**）。独立 Checker 若跑，应产出 `checker_report.md`。
> 本文件按 `_mega7_2026-06-19/CHECKER.md` 的 A–F gate + verdict-ceiling + 机械新鲜度门逐项自评。

**裁定（自评）**: `FIX-NEEDED`（Gate B、Gate C 未过）
**真实状态标签**: `DECISION_DRAFT`
**verdict / size / ceiling**: WATCH / 0% / ceiling=WATCH → **被完整度正确封顶：是** ✅
**数据新鲜度**: **PASS**（`freshness_check.json`，exit 0）✅

---

## A. Scope & Definition ✅

- [x] ticker / share class（ORCL，NYSE，单一股权类别）/ **as_of = 2026-08-06** / 决策目的 / 时间跨度 10y 已冻结（`step0_plan.md`）
- [x] 完成标准先于结论写下（`step0_plan.md` §4）
- [x] 状态标签不 stale（`research_status.md`）
- [x] **as_of ≠ run_date 的理由已显式说明**（08-07 市场未收盘）

## B. Evidence ❌ 未过

- [x] `source_register.md` 含每个来源（名 + 日期 + link + tier）
- [x] `raw/` 对重要 claim 有原始摘录（4 个文件，含完整 8-K 损益表）
- [x] `claim_ledger.csv` 带 source tier + 验证状态 + source_id（60 条）
- [x] `facts.md` 只收已验证或明确标注的派生 claim
- [x] memo 无裸 claim（每条有 source_id 或显式 OPEN）
- [x] 一手 vs KOL/媒体分层：媒体一律标 `[MEDIA]`，未独立验证者不支撑 BUY
- [ ] ❌ **来源等级不达标**：`sec.gov`、`oracle.com`、`investor.oracle.com` 本轮全部 403
      → **无任何 A1 级直连来源**。8-K 数字走 A1-proxy（复刻页），已与独立聚合器（A2-3）逐行对账，
      但**这不等于读了原文**。10-K 完全未取得。
- [ ] ❌ **电话会一手 transcript 未取得** → CFO "ROIC high 20s"、ROIC 口径、FY2027 净 capex 指引
      全部为**二手转述**。已在 facts.md / claim_ledger 中逐条标注 `MEDIA_REPORTED_CALL_SECONDHAND`。

## C. 11-Stage 覆盖 ❌ 未过

- [x] 八模块各有产物：Business ✅ / Financial Quality ✅ / Value Chain ✅ / Moat ✅ /
      Bottleneck ✅ / Operator ⚠️（不给评分）/ Inversion ✅ / Valuation ✅
- [ ] ❌ **Stage 8 IC Panel 为简版**：五灵魂各出一票 ✅，但**未做第二轮相互批判**。
- [x] **无伪造引语**：`ic_panel.md` 明示"全部为框架释义，非引语"；全卡不含任何一手引语。
      CFO 的 "high 20s" 与 "step down" 标注为媒体转述，未包装成直接引语。

## D. Model & Math ✅

- [x] 营收/费用/capex 模型 tied to evidence（FY2027 指引 $90B、净 capex $70B、融资 $40B 均带 source）
- [x] **owner earnings 桥按当前版本重建，且显式自曝不闭合**（`financial_quality.md` §1）：
      净利 $16,984M vs 正常化 OE₀ $11B/$16B/$23B 三档分开列出
- [x] implied expectations 从**当前价 $143.47** 反推（8% 门槛价 $121.50、10% 价 $101.13、12% 价 $84.46）
- [x] 三情景输出与假设对账，关键公式可审计（`model/scenario_model.csv`，含 10 行，其中 3 行为敏感性）
- [x] **锚点敏感性显式**：维护 capex $9.3B/$18B/$25B → base IRR +9.7%/+6.2%/+0.9%

## E. Open Questions ✅

- [x] 10 项全部分类：blocking（O1/O2/O3/O5）· monitoring（O4/O6/O8/O10）· non-blocking（O7/O9）
- [x] blocking 项显式封顶 verdict（O1 为 binding_constraint 的直接来源）
- [x] non-blocking 项给出不封顶理由

## F. Audit & Consistency ✅

- [x] README/research_status 反映当前真实状态，无 stale 自述
- [x] **数字对账（T5 机械校验通过）**：`as_of_price 143.47` 在 facts.md / valuation.md /
      model/scenario_model.csv / decision_card.md **全部出现且一致**
- [x] `decision_card.json` schema 完整，**版本戳 = `lean-6module-v1.1` / `none` / `2026-08-07`** ✅
- [x] 最终答案报**真实**状态（DECISION_DRAFT / 58%），不报更好看的状态

## 活体专属：数据新鲜度（MECHANICAL 硬门）✅ PASS

```
FRESHNESS CHECK - ORCL as_of 2026-08-06  [verify_freshness-v1]
STATUS: PASS  (exit 0)
price: card=143.47 refetched_yahoo=143.47000122070312 (2026-08-06) -> PASS
  [PASS] T1 52wk band containment: 114.5 <= 143.47 <= 345.72
  [PASS] T2 low/high hug: +25.3% off low, -58.5% off high
  [PASS] T3 market-cap identity: 2880M x 143.47 = 0.413T vs card 0.413T (0.00%)
  [PASS] T4 distance-from-high reconciliation: narrative -58.5% vs card-implied -58.5% (gap 0.0pt)
  [PASS] T5 single value of truth: as_of_price 143.47 present in all price-bearing files
  [PASS] T6 LIVE-qualitative freshness [guidance]: newest source 2026-07-09 (28d)
```

- [x] `verify_freshness.py` 已运行，`freshness_check.json` 已提交且 `status == "PASS"`
- [x] `freshness.json` manifest 存在，每个 LIVE 字段带 ≥2 独立源
- [x] 价格走 Yahoo chart API + stockanalysis 交叉验证（delta 0.00%）
- [x] **INC-001 防线生效**：as_of 特意设为 2026-08-06 而非 run_date 2026-08-07，
      因为 08-07 美东 13:45 市场仍在交易（盘中 $144.88）。若误用盘中价，
      所有衍生数会内部自洽地错下去——这正是 INC-001 的失败模式。

---

## Verdict 上限核验

| completeness | verdict 上限 | 本卡 |
|---|---|---|
| < 40% | INFO-GAP | |
| **40–60%** | **WATCH** | ✅ **58% → 上限 WATCH，实际 WATCH，未超顶** |
| 60–80% | STARTER | |
| > 80% | CORE 可讨论 | |

**size 与耐久性匹配核验**：耐久性 = `uncertain`（合并实体），且存在真实的永久损失路径（M5 −2）。
→ suggested_max_size 0%、conditional_max_size **2%（而非 3%）** —— **匹配** ✅

---

## FIX 清单（下一轮必做，按优先级）

1. **`source_register.md` / `facts.md`** — 取得 **FY2026 10-K 原文**，关闭 O2（折旧年限）、O3（资本化利息）、
   O10（完整资产负债表 → 替换派生的 EBITDA/D&A）、O1 的一半（客户集中度披露原文）。
   *绕过 403 的可行路径：SEC EDGAR 全文检索 API、annualreports.com、last10k、或本地下载。*
2. **`facts.md` F7.2 / `claim_ledger.csv` C052-C053** — 取得 **Q4 FY2026 电话会一手 transcript**，
   把 CFO "high 20s" 与 ROIC 口径从 `MEDIA_REPORTED_CALL_SECONDHAND` 升级或撤销。
3. **`financial_quality.md` §4.3 / OPEN-O1** — 取得 **OpenAI 的收入 run-rate / 烧钱 / 融资状况**。
   **这是唯一能解除 binding_constraint 的一项。**
4. **`ic_panel.md`** — 补第二轮相互批判，使 Gate C 达标。
5. **`operator_underwriting.md`** — 取得 DEF 14A + Form 4，使该模块可评分（O7）。
6. **`valuation.md` §6** — 取得卖方预期修正史（O8），使 de-rating 分解的第三层可用估值预期而非仅已报告 EPS。

## 伪造引语 / 失配数字

**无。**
- 全卡不含任何一手引语；`ic_panel.md` 顶部已明示五灵魂表述为框架释义。
- 管理层表述（"high 20s"、"step down"）标注为媒体转述，未包装成直接引语。
- 数字失配：T5 机械扫描通过；de-rating 分解已做乘法对账（0.3290 × 1.3433 = 0.4420 = −55.80%，与股价变动完全吻合）。

## 一句话：这家这轮可信到什么程度

**财务事实层（FY2026 损益/现金流/资产负债表、RPO 规模、评级动作）可信度高**——
8-K 完整损益表已落盘并与独立聚合器逐行对账，机械新鲜度门全绿。
**但两件决定裁决的事都建立在二手证据上**：OpenAI 占 RPO 的比例（媒体+S&P 估计，Oracle 从不点名），
以及管理层的 ROIC 口径与目标（电话会二手转述）。
**因此这张卡的"事实"可信，"裁决"应被读作"在无法看见一半交易对手的前提下的保守取值"。**
**而它的最高价值输出——`## 回喂` 序列清单——依赖的全部是已验证的一手/对账过的财务数字与公开日期，
是本卡中最可靠的一部分。**
