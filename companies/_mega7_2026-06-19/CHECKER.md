# Mega7 活体批次 — 质检门 (CHECKER)

**用途**: 每家 dossier 跑完后,由独立 Checker agent 据此打分,产出 `companies/<ticker>/checker_report.md`。批次末尾汇一份 `_mega7_2026-06-19/checker_summary.md`。

这是**活体运行的完成度 + 质量门**,改造自 `frameworks/research_completion_checker.md`(A-F gate)+ `companies/googl/audit.md`(verdict-ceiling)+ 来源纪律。**不是 lookahead 审计**——本批 as_of=今天,无未来可泄漏。

---

## 0. Checker 独立性

Checker **不是** Runner 自己。它收到锁定的 dossier,只判定:gate 是否真过、状态标签是否诚实、verdict 是否被完整度正确封顶、有无伪造引语/失配数字。输出 `CLEAN` 或 `FIX-NEEDED + 具体清单`。

## 1. 状态标签(必须诚实,对齐 research_completion_checker)

`NOT_STARTED → SCAFFOLD → P0_PASS_1 → P1_PARTIAL → DECISION_DRAFT → COMPLETE`

**措辞铁律**: 除非公司 checker 全 gate ✓ 且标 `COMPLETE`,否则禁说"完成/彻底跑完/full research complete";未到则用"完成到 P1 / 决策草案 / blocked by these gates"。Checker 若发现 `research_status.md` 用了超出真实标签的措辞 → 直接 `FIX-NEEDED`。

## 2. 完成度 Gate(逐项勾,缺一不能称 COMPLETE)

### A. Scope & Definition
- [ ] ticker / share class / as_of=2026-06-19 / 决策目的 / 时间跨度 已冻结。
- [ ] 完成标准先于结论写下。
- [ ] 当前状态标签不 stale。

### B. Evidence(M1 证据脊柱)
- [ ] `source_register.md` 含 memo/model 用到的每个来源(名 + 日期 + link/path + tier)。
- [ ] `raw/` 对每条重要 claim 有原始摘录。
- [ ] `claim_ledger.csv` 带 source tier + 验证状态 + source_id。
- [ ] `facts.md` 只收已验证或明确标注的派生 claim。
- [ ] memo 里无"裸 claim"(每条要么有 fact/source_id,要么显式 `OPEN`)。
- [ ] **来源等级**: 一手(SEC 文件/财报电话/官方统计)优先;KOL/美股投资网/社媒只作线索或情绪,**未独立验证不得进 facts、永不直接支撑 BUY**。

### C. 11-Stage 覆盖
- [ ] Stage 0-10 全部 ≥ P0 一遍(Business / Financial Quality / Value Chain / Moat / Bottleneck / Operator / Inversion / Valuation 八模块各有产物)。
- [ ] **Stage 8 IC Panel 存在**:五灵魂(段永平主审 + 巴菲特/芒格/Marks/Klarman)各出票;**任何引语有一手出处或标注为释义,无伪造**。

### D. Model & Math(M4/M6)
- [ ] 营收驱动模型、费用/capex 模型建立且 tied to evidence。
- [ ] owner earnings 桥按当前版本重建(净利 vs 正常化 OE 分开)。
- [ ] implied expectations 从**当前价**反推。
- [ ] 三情景输出与来源/假设对账;关键公式可审计。

### E. Open Questions
- [ ] 每个 open question 分类 `blocking / monitoring / non-blocking`。
- [ ] blocking 项显式封顶 verdict;non-blocking 给出不封顶理由。

### F. Audit & Consistency
- [ ] 内部审计查过 stale 自述;README/research_status 反映当前状态。
- [ ] 数字对账:`as_of_price`、`market_cap`、P/E、FCF yield、各模块引用的同一数字**前后一致**。
- [ ] `decision_card.json` schema 完整且**版本戳 = `lean-6module-v1` / `none` / `run_date`**(缺戳 = 卡作废/不可比)。
- [ ] 最终答案报真实状态,不报更好看的状态。

## 3. Verdict 上限核验(audit.md 硬规则)

按 dossier 完整度封 verdict 上限,Checker 核对 `decision_card` 的 verdict 未超顶:

| completeness | verdict 上限 |
|---|---|
| < 40% | INFO-GAP |
| 40-60% | WATCH |
| 60-80% | STARTER |
| > 80% | CORE 可讨论 |

并核对 **size 与耐久性匹配**:周期/未确认的不得给 Core 级 size;天花板由耐久性(含 operator life-arc 评级)而非单纯"确认"定。

## 4. 活体专属检查(本批新增) — 数据新鲜度现为**强制机械门**(lean-6module-v1.1)

> 背景: INC-001(NVDA 用 $145.48≈52周低当现价,真实 $210.69,45% 错价翻了 verdict,Checker 仍盖 CLEAN)。
> 教训: **人工勾选"无明显过期数字"挡不住一个数值错误**——错价的所有衍生数都内部自洽。因此本项由判断式升级为机械式。

- [ ] **数据新鲜度(MECHANICAL,硬门)**: `python scripts/verify_freshness.py --dossier <dossier>` 已运行,`freshness_check.json` 已提交且 `status=="PASS"`(exit 0)。**无 PASS 产物 = 自动 FIX-NEEDED;Checker 无权以人工判断放行。** 该脚本独立重抓价格、交叉验证 ≥2 独立源、跑结构 tripwire(含"现价≈52周低/高"探测)。
- [ ] **freshness.json manifest 存在**: 每个 LIVE 字段(price/market_cap/52wk/shares + 出口管制/诉讼/guidance)带 ≥2 独立源。LIVE/FILED 决期分级见 `sources/source_policy.md`。
- [ ] **价格源合规**: 价格走 Yahoo chart API(repo 既定来源),并由 ≥2 源交叉验证(单源 + 只验日期 = INC-001 的洞,不再接受)。
- [ ] **GOOGL 刷新特例**: GOOGL 不要求重建;但同样须有 `freshness.json` + 一次 `verify_freshness.py` PASS(它本就手动重抓过 3 个 close,本项把它形式化)。

## 5. 输出格式(`checker_report.md`)

```
# <TICKER> Checker Report — mega7_2026-06-19
裁定: CLEAN | FIX-NEEDED
真实状态标签: <NOT_STARTED..COMPLETE>
verdict / size / ceiling: <...>  ← 是否被完整度正确封顶: 是/否
数据新鲜度: PASS(freshness_check.json) | BLOCK  ← 无 PASS = 强制 FIX-NEEDED
Gate 勾选: A_/B_/C_/D_/E_/F_  (列未过项)
FIX 清单: 1) ... 2) ...   (每条指到文件)
伪造引语/失配数字: 无 | 列出
一句话: 这家这轮可信到什么程度
```

## 6. 批次级检查(`checker_summary.md`,Phase 3)

- [ ] 7 家状态标签 + verdict 一览;哪些 FIX-NEEDED。
- [ ] **单因子集中度旗标**(METHODOLOGY §5):七名是否全骑"AI capex + 流动性";叠加已持有 BTC/GOOGL/NBIS 后的隐藏单一押注。一句话判断。
- [ ] 跨家一致性:同一宏观假设(AI capex 周期、利率)在 7 家间无自相矛盾。
