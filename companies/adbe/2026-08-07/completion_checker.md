# ADBE Completion Checker — self-audit

as_of 2026-08-07 | run_date 2026-08-07 | pipeline `lean-6module-v1.1`
基准：`companies/_mega7_2026-06-19/CHECKER.md` + `frameworks/research_completion_checker.md`

> **这是 Runner 自审，不是独立 Checker。** 独立 Checker 若复核，应重跑 `verify_freshness.py` 并抽查 `claim_ledger.csv` 的 source_id。

---

## 裁定：**FIX-NEEDED（相对 COMPLETE）／ 作为 DECISION_DRAFT 则 CLEAN**

**真实状态标签**：`DECISION_DRAFT`
**verdict / size / ceiling**：STARTER / 3%（max 6%）/ 上限 STARTER（completeness 68%，60–80% 档）→ **是否被完整度正确封顶：是**
**数据新鲜度**：**PASS**（`freshness_check.json`，exit 0）

---

## Gate 勾选

### A. Scope & Definition
- [x] ticker / share class（单一普通股，无双层）/ as_of=2026-08-07 / 决策目的 / 时间跨度 已冻结
- [x] 完成标准先于结论写下（`step0_plan.md`）
- [x] 状态标签不 stale（`research_status.md` 明确标 DECISION_DRAFT 并附措辞纪律声明）

### B. Evidence（M1 证据脊柱）
- [x] `source_register.md` 含每个来源（名 + 日期 + link + tier），21 条，含 fetch notes 与失败记录
- [x] `raw/` 对每条重要 claim 有原始摘录（`primary_extracts.md` 逐条 verbatim；`arr_history.md` 单独落盘核心数据集）
- [x] `claim_ledger.csv` 带 source tier + 验证状态 + source_id（118 条）
- [x] `facts.md` 只收已验证或明确标注的派生 claim（推算值一律标「推算」）
- [x] memo 内无裸 claim（每条要么有 source_id，要么显式 OPEN）
- [x] **来源等级**：15 条 A1 一手（SEC EDGAR 直连正文）；B1 聚合器的每条载荷性数字均对 A1 交叉核对
- [x] **未引用任何未经证实的竞品数字**——二手转述的 Firefly ARR 被排除在 EVIDENCE 之外，仅作 OPEN 线索

### C. Stage 覆盖
- [x] 八模块各有产物：business_model / financial_quality / value_chain_map / moat_map / bottleneck_map / operator_underwriting / inversion_map / valuation
- [x] **IC Panel 存在**：五灵魂（Buffett / Munger / 段永平 / Marks / Klarman）各出票，**3 STARTER / 2 WATCH 非一致**
- [x] **无伪造引语**：`ic_panel.md` 全文**不含任何引号内的投资人原话**，只描述有据可查的一般立场并显式声明该纪律

### D. Model & Math（M4/M6）
- [x] owner earnings 桥按现金口径重建（FCF − SBC），与 GAAP 净利、non-GAAP EPS 三者分开列示
- [x] **implied expectations 从当前价反推**（8% 门槛下需 OE 年化 +0.29%）
- [x] 三情景输出与假设对账，公式可审计（`model/scenario_model.csv`，含 method 段说明 IRR 定义）
- [x] **(a) 拆解三口径互相校验，恒等式零残差**（1.7445 × 0.22128 = 0.38602 → −61.40%）
- [ ] ⚠️ **收入驱动模型未逐产品线建立** —— 因 Adobe 已把三分部合并为一个报告分部且撤掉 ARR 分层，**无法建立**。以分层收入推算（`business_model.md` §2）替代，已标注为推算

### E. Open Questions
- [x] 每个 open question 分类 blocking / monitoring / non-blocking（5 / 4 / 1）
- [x] blocking 项显式封顶 verdict（68% → STARTER 上限）
- [x] non-blocking 给出不封顶理由（O9 只影响作图）

### F. Audit & Consistency
- [x] `research_status.md` 反映当前真实状态，含措辞纪律声明
- [x] **数字对账**：`as_of_price` **$265.74** 在 facts.md / valuation.md / decision_card.md / model/scenario_model.csv 中逐字一致（T5 PASS）；market_cap、P/E、FCF 收益率各模块引用一致
- [x] `decision_card.json` schema 完整且**版本戳齐**：`lean-6module-v1.1` / `none` / `2026-08-07`
- [x] 最终答案报真实状态，不报更好看的状态

### 活体专属（lean-6module-v1.1 机械门）
- [x] **`python scripts/verify_freshness.py --dossier companies/adbe/2026-08-07` 已运行，`freshness_check.json` status=PASS，exit 0**
- [x] `freshness.json` manifest 存在，每个 LIVE 字段带 ≥2 独立源（price / market_cap / 52wk_high / 52wk_low / shares_out / guidance / active_litigation / leadership_status / disclosure_basis_change）
- [x] 价格源合规：Yahoo chart API（仓库既定来源）+ stockanalysis 交叉，delta 0.03%；校验器独立重抓 delta 0.23%
- [x] **`low_high_hug_justified` 诚实填 false 且附说明**——ADBE 距 52 周低点 +39.8%、距高点 −28.4%，**不是 hug，未申请任何豁免**。T1/T2 靠自身通过

---

## Tripwire 结果（`freshness_check.txt` 原文）

```
STATUS: PASS  (exit 0)
[PASS] T1 52wk band containment: 190.12 <= 265.74 <= 370.86
[PASS] T2 low/high hug: +39.8% off low, -28.3% off high
[PASS] T3 market-cap identity: 398M x 265.74 = 0.106T vs card 0.106T (0.00%)
[PASS] T4 distance-from-high reconciliation: narrative -28.4% vs card-implied -28.3% (gap 0.1pt)
[PASS] T5 single value of truth: as_of_price 265.74 present in all price-bearing files
[PASS] T6 LIVE-qualitative freshness [active_litigation]: newest source 2026-07-17 (21d)
[WARN] T6 LIVE-qualitative freshness [guidance]: newest source 2026-06-11 is 57d before as_of (> 45d)
```

**T6 WARN 的处理**：**不抑制，确认为正确状态。** Adobe 按季披露，Q3 FY2026 截至 as_of 未申报（季度约 2026-08-28 结束）。2026-06-11 **就是**最新的权威指引事件；期间唯一的公司申报是 2026-07-17 的 8-K（CLO 留任函，Item 5.02），不含任何指引内容。已在 `freshness.json` 的 `age_note` 中说明。

---

## FIX 清单（要走到 COMPLETE 必须关掉的）

1. **O3 — 读 FY2025 10-K 的 purchase obligations 章节**（`ADBE-10K-FY25`）。owner earnings 桥唯一可能被推翻的输入。**最高优先级。**
2. **O8 — 取竞争对手一手财务**（Canva / Figma / OpenAI / Google 图像视频产品）。需要 web search 预算。关掉它 M3 才可能从 0 移动。
3. **O2 / O10 — 取 Q2 FY2026 电话会逐字稿**，确认 Firefly ARR 与管理层对 freemium 影响 ARR 的原话。
4. **O1 — 持续监控**：Q3 FY2026 是否恢复任何分层披露，或第三次退化（K-E）。
5. **O7 — 监控 CEO/CFO 任命。**
6. **O6 — 读 10-Q 的 G&A 与或有事项附注**，解释 +44.8% 的跳升与 $30M 诉讼计提。
7. **O9 —（低优先）** 重试 Adobe investor datasheet PDF，补 FY2023/FY2024 Total ARR 历史值。

---

## 伪造引语 / 失配数字检查

- **伪造引语：无。** `ic_panel.md` 显式声明不含投资人原话；所有引号内的英文均为 SEC 文件的 verbatim 摘录，附 URL。
- **失配数字：无。** `as_of_price` 265.74 通过 T5；market-cap 恒等式通过 T3；距高点叙述通过 T4。
- **已披露的一处数据分歧**：as_of 收盘 $265.74 vs 另一路抓取主张的 $260.24（−2.07%）。**已在 facts.md E13、valuation.md §0、freshness.json、decision_card 中四处一致披露，并给出敏感性（base 10y IRR +14.15% → +14.63%，裁决不变）。未隐藏。**
- **已披露的一处与任务简报的分歧**：简报参考「YTD 2026 −20.5%」，本 dossier 自算 **−24.07%**（2025-12-31 收盘 $349.99 → $265.74）。以自算为准并已标注。简报的 −61.5% 与本算 −61.40% 一致。

---

## 一句话：这家这轮可信到什么程度

**财务与估值部分（M4/M6）可信度高——15 条 SEC 一手、恒等式零残差、机械门 PASS，(a) 的拆解与 (b) 的净新增 ARR 趋势可以直接拿去用。**
**护城河与竞争部分（M3）可信度低——竞争侧证据为零，且公司已把最关键的运营指标撤下。**
**因此本卡的正确读法是：「崩的是倍数不是生意」这个结论在已披露的数字上是稳的；「未来还会不会崩」这个问题本轮没有回答，也没有假装回答。**
