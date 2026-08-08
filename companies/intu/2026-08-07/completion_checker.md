# INTU Completion Checker — as_of 2026-08-06 / run_date 2026-08-07

自评（Runner 自查，非独立 Checker）。裁定基准见 `companies/_mega7_2026-06-19/CHECKER.md`。

**真实状态标签：DECISION_DRAFT（~62%）** —— 未使用"完成/跑完/complete"字样。

---

## A. Scope & Definition

- [x] ticker / 股份类别（单一普通股）/ as_of=2026-08-06 / run_date=2026-08-07 / 决策目的 / 10 年跨度 已冻结（`step0_plan.md`）
- [x] 完成标准先于结论写下（step0 §"需要 ≥2 源验证的锚定事实"+"已知的硬边界"）
- [x] 状态标签不 stale：DECISION_DRAFT，与 62% 一致
- [x] **FY/CY 边界已显式处理**：FY 结束 7/31；FY2026 全年未公布（2026-08-25）在 step0、facts、decision_card.json、freshness.json 四处重复标注

## B. Evidence（M1）

- [x] `source_register.md` 含 19 个来源，全部带名称 + 日期 + URL + tier
- [x] `raw/` 有 5 份原始摘录，含三份 SEC 原文与一份政策专题
- [x] `claim_ledger.csv` 94 条，带 source_id + tier + 验证状态（VERIFIED / DERIVED / ESTIMATE / PARTIAL / UNVERIFIED / INFERENCE / VERIFIED_ABSENT）
- [x] `facts.md` 只收一手已验证或明确标注的派生值；KOL/券商观点**未进 facts.md**（Goldman 只出现在 inversion_map / decision_card 的叙事对照中）
- [x] memo 无裸 claim
- [x] 来源等级：全部财务数字来自 SEC 原文直取（非聚合站）
- [ ] **未过**：管理层引语只有 B1 二手转录（**O6**）；政策为 B1 press 转述 IRS 一手邮件（**未直取 irs.gov**）
- [x] **推断已明确标注**："FY2026 是第一个无 Direct File 的税季" 在 `raw/policy_*.txt` 与 claim_ledger C085 明确标为 **INFERENCE**，未进 facts.md

## C. 模块覆盖

- [x] Business Model / Financial Quality / Value Chain / Moat / Bottleneck / Operator / Inversion / Valuation **八模块各有产物**
- [x] Stage 8 IC Panel 存在，五灵魂各出票
- [x] **无伪造引语**：`ic_panel.md` 开头显式声明"以下不是任何投资人的真实发言……本文件不含任何引语"

## D. Model & Math

- [x] owner earnings 桥按当前版本重建（会计侧 $5.02B / 现金侧 $4.15B / 拒绝公司 non-GAAP $6.65B），**两处质量陷阱（$1.4B 递延税、$2.05B SBC）显式剔除**
- [x] implied expectations 从**当前价**反推（12x/16x/20x 三档 → 3.6%–8.6% OE/股 CAGR）
- [x] 三情景 + **8 档敏感度**（`model/scenario_model.csv` 12 行）
- [x] 关键公式可审计：回撤分解两条独立口径互证到 −60.1%
- [x] 数字前后一致：$321.91 / $88.06B / 19.6x / +10.2% 在 card / valuation / facts / csv 全一致

## E. Open Questions

- [x] 分类完成：blocking（O1/O2/O5/O6/O9）· monitoring（O3/O4/O7/O8/O10–O15）
- [x] blocking 项显式封顶 verdict（62% → 上限 STARTER）
- [x] monitoring 项给出不封顶理由

## F. Audit & Consistency

- [x] `research_status.md` 反映真实状态，措辞未越级
- [x] `decision_card.json` schema 完整，**版本戳齐全**：`lean-6module-v1.1` / `none` / `2026-08-07`
- [x] 最终答案报真实状态

## 4. 数据新鲜度（机械硬门）

- [x] `python scripts/verify_freshness.py --dossier companies/intu/2026-08-07` 已运行
- [x] `freshness_check.json` 已生成，**status = PASS（exit 0）**
- [x] `freshness.json` manifest 存在，8 个 LIVE 字段各带 ≥2 源（含 guidance / active_litigation / policy_status 三个定性字段）
- [x] 价格走 Yahoo chart API + stockanalysis 双源，delta **0.00%**；验证器独立重抓得 321.9100

| Tripwire | 结果 |
|---|---|
| T1 52 周区间包含 | **PASS** 252.84 ≤ 321.91 ≤ 762.48 |
| T2 低/高点贴合 | **PASS** +27.3% off low, −57.8% off high；`low_high_hug_justified` 已如实填写理由（−60% 回撤下值得显式说明，但事实上并未贴合任一极值） |
| T3 市值恒等 | **PASS** 0.00% |
| T4 距高点叙事对账 | **PASS** gap 0.0pt |
| T5 单一真值 | **PASS** 321.91 出现在全部四个载价文件 |
| T6 定性新鲜度 | **2 个 WARN**（见下） |

**T6 WARN 的处置（不构成 BLOCK）**
- `guidance` 最新源 2026-05-20，距 as_of **78 天** > 45 天窗口。**这是正确的**——
  下一次权威事件是 2026-08-25 的 Q4/FY2026 财报，在 as_of **之后**。**不存在更新的权威事件可用。**
- `active_litigation` 最新源 2026-06-02，距 as_of **65 天**。诉讼细节列为 **O8**，
  且已在 manifest 中显式说明未从法院/10-K 一手核实。
- 两项均已在 `freshness.json` 的 value 字段中写明限制，**不隐藏**。

## 3. Verdict 上限核验

| completeness | 上限 | 本卡 |
|---|---|---|
| 60–80% | **STARTER** | **STARTER** ✅ 未越顶 |

- [x] size 与耐久性匹配：business=good（非 exceptional）→ 初始 2% / 上限 6%，未给 Core 级 size
- [x] 上限的解锁条件写明且有日期（2026-08-25 / 2026-09-17）

---

## 自评裁定：**CLEAN（有保留）**

**保留项（若由独立 Checker 复核，这三条最可能被开 FIX）**

1. **O6 未闭合**：`decision_card.md`、`facts.md`、`business_model.md`、`operator_underwriting.md` 四处
   引用了管理层引语，全部只有 B1 二手转录。**已在每处标注，但仍是本卡最大的引证弱点。**
2. **O9 未闭合**：TurboTax 护城河的支点（IRS 报送资质）是推理不是引证。
   `bottleneck_map.md` 已在开头用醒目标注声明，但这不改变它是缺口的事实。
3. **as_of 与 run_date 不同日**：as_of=2026-08-06（最后结算收盘），run_date=2026-08-07。
   这是刻意的选择（房规"settled close ≤ today"，08-07 当日未结算），
   已在 `step0_plan.md` / `decision_card.json` / `freshness.json` / `source_register.md` 四处说明，
   且机械门以 as_of=2026-08-06 跑出 PASS。**若 Checker 认为应与文件夹日期强制一致，此项需讨论。**

**一句话：这轮的财务与回撤归因部分可信度高（SEC 原文直取、双口径互证、机械门 PASS）；
政策与竞争部分是 B 级证据 + 部分推理；管理层引语未升 A 级。62% 是诚实的读数。**
