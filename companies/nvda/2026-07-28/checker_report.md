# NVDA Checker Report — mega7_2026-06-19 CHECKER applied to the `2026-07-28` refresh

裁定: **CLEAN**（附一条**跨档案遗留告警**，非本档失效项）
真实状态标签: **DECISION_DRAFT**（~65%，诚实标注"NOT COMPLETE"，含 wording-discipline 段）— 未越级措辞。
verdict / size / ceiling: new-money **WATCH（0%）** / existing **HOLD** / initial 0% · max 0%（新钱）/ ceiling **STARTER**（完整度 65% → 60–80% 档）。价格门更严 → 封到 WATCH。 ← 是否被完整度正确封顶: **是**（WATCH ≤ STARTER ceiling；未越顶，反而更保守，且明写理由）。
数据新鲜度: **PASS**（`freshness_check.json` status==PASS, exit 0）← 非 BLOCK。**我用真 Python（py 3.9）独立重跑 `verify_freshness.py`，STATUS PASS / exit 0，重生成的 `freshness_check.json` 与已提交版 byte-identical** → 该 PASS 可复现、非手工伪造。
Gate 勾选（按 `_mega7_2026-07-28/PLAN.md` 所定"现价+regime 轻刷新"范围）: A✓ / B~ / C(范围外·N/A) / D✓ / E✓ / F✓（B 见下：本档无独立 source_register/claim_ledger，但溯源在 card.sources_used 内自洽完整）

---

## 0. 范围界定（决定"缺 ic_panel/source_register"是否算缺陷）

`companies/_mega7_2026-07-28/PLAN.md` 明确本批为**现价重估 + regime 叠加**，读 06-19 dossier 做**业务基线**（M2/M3 六周内不变，快速复核），**"不是从零重研究"**。其"每家产物"清单只列：`decision_card.json/.md · valuation.md · inversion_map.md · delta_vs_0619.md · research_status.md · freshness.json · checker_report.md`。

NVDA 07-28 档**恰好交齐这 7 项**（本 report 为第 7 项）。`ic_panel.md / source_register.md / claim_ledger.csv / facts.md / audit.md` **不在本批范围内**——其缺席是**批次设计使然，不是漏做**。故 CHECKER §2 的 A–F 完整度清单按"决策草案 for scope"口径核，而非按 COMPLETE 口径。

## 1. 独立复核（verify, don't trust）

- **价格 / INC-001 探测**: `verify_freshness.py` 独立 Yahoo 再抓 = **$197.00999** ≈ 卡值 **$197.01**（0.0% delta），Yahoo chart API + stockanalysis 两源到分一致。**T2（INC-001 的探针）clean：+20.1% off 52wk 低 / −16.7% off 52wk 高 = 区间中部，未贴任一极值。** 这正是 INC-001（$145.48≈52 周低当现价）的失败模式——本档**明确不复现**。
- **市值恒等式**: 24,391M × 197.01 = **$4,805,271M**；卡值 4,805,691M（差 0.009%，T3 报 0.01%，容差内；隐含约 24,393M 股，immaterial）。
- **派生数手工重算全对**（py 复算）: forward P/E **26.34**（卡 ~26.3x）· trailing P/E **40.21**（卡 ~40x）· 起始 OE yield **3.79%**（卡 3.8%）。
- **三情景 IRR 全对**: 由 CSV 的 oe_year5×exit + 净现金 反推每股 = **$80.4 / $266.2 / $494.9**（卡 $80/$266/$495），再算 5y IRR = **−16.5% / +6.2% / +20.2%**（与卡逐一吻合）。base +6.2% < 8% hurdle → 无 MOS 结论成立；缺口 8−6.2=**1.8pp**。
- **δ vs 06-20 基线核对**（读 `../2026-06-20/decision_card.json` 实值）: 价格 $210.69→$197.01（**−6.49%**）· base IRR **+4.8%→+6.2%**（缺口 3.2pp→1.8pp）· buy_below **$181 未变** · 六模块符号 **+2/+2/+2/+2/−1/−1 未变** · verdict **WATCH/HOLD 未变** · drawdown **−11%→−16.7% off ATH**、+20.1% off low。全部自洽。

## 2. Verdict 上限 / size 核验

- 完整度 65% → ceiling **STARTER**（60–80%）。new_money **WATCH** 严格 ≤ STARTER，**未越顶**。档内明写"完整度封 STARTER；M6 价格门更严 → 实际封 WATCH"——封顶逻辑正确且更保守。
- size 与耐久性匹配: 新钱 initial 0% / max 0%；add-zone 因周期性显式封在 **Core 以下**。周期/未确认季度**未被 Core 化**。✓

## 3. 诚实标签 / regime 并入 / 伪造项

- **诚实标签 ✓**: status=DECISION_DRAFT，`research_status.md` 显式"Honest status label: DECISION_DRAFT (NOT COMPLETE)" + "Wording discipline"段（"Do NOT call this complete/full research"）。`reported_q2_fy27=false` 明示 Q2 未报（档期 8/26，在 as_of 后）——市场在**未确认季度**上重定价，档内如实点破。无 COMPLETE 过度声称。
- **regime 真并入 M4/M5（非忽略）✓**: `inversion_map.md` 有完整 regime 传导表（7/28 半导体暴跌 / AAPL $5T 反超 / AI-capex 审计 / CXMT / FOMC-Warsh / China H200 实际开船），失败路径 F1–F7 重写，**M5 明推到 −1 更负端**；M4 明记"无 Q2 新数 + China 25% 抽成"；`kill_criteria` 新增 **K6（capex 审计→hyperscaler capex 削减→需求 air-pocket）**。regime 是**并入定价与风险模块**，不是贴在旁边。
- **伪造引语: 无。** 07-28 档**不含任何 IC panel / 投资人引语**（本批范围外）；`runner_dissent` 是 runner 自身口径（允许）。无引号内逐字伪造。
- **失配数字: 无（本档内）。** $197.01 / $4.806T / 26.3x / 3.8% / IRR −16.5·+6.2·+20.2 / −16.7% off ATH 在 decision_card(.json/.md)、valuation、inversion_map、delta、research_status、freshness 六处前后一致（T5 通过），并经独立重抓 + 恒等式 + IRR 复算全部通过。

## 4. FIX 清单

**本档无阻断性 FIX。** 以下为**遗留告警 + 轻记**（不改变 CLEAN 裁定）：

1. **[跨档案遗留告警·非本批范围]** NVDA 档树内**唯一的 Stage-8 IC panel** = `companies/nvda/2026-06-19/ic_panel.md`，至今仍**未作废**地呈现"**五票一致 STARTER**、当前价站在买方这边（forward **19x** / yield **5.1%** / base IRR **13%**）"——建立在 **INC-001 错价 $145.48** 之上，与当前 **WATCH（无 MOS，26.3x / 3.8% / +6.2%）直接相反**。**07-10 Checker 已在其 FIX#1 提出，至今未加 void/superseded 标注。** 07-28 档**未引用、未依赖**该 panel（`research_status` 只回挂 business_model/moat_map/operator_underwriting），故**不属本档缺陷**；但作为 repo 卫生项应处理。**建议**：在 `2026-06-19/ic_panel.md` 顶部加一行 `SUPERSEDED — 结论基于 INC-001 错价 $145.48，已被 2026-06-20+ 推翻，勿引用其 STARTER 结论`。责任归 06-19 档 owner，非 07-28 refresh。
2. **[Gate B·轻]** 本档无独立 `source_register.md` / `claim_ledger.csv`（本批范围外）。溯源集中在 `decision_card.json.sources_used`：module_signals 用到的每个 driver（S001/S002/S003/S004/S206/S208/S210/S211/S212/S214）**均在 sources_used 内可回挂**，自洽完整；且区分了 primary（SEC 8-K/10-K = S001–S004）vs commentary（S214 显标 B/C tier，"informs monitor not verdict"）。可接受；若后续升到 COMPLETE 需补正式 register。
3. **[Gate F·cosmetic]** 卡打 `pipeline_version: lean-6module-v1`（CHECKER §F 认可的合法戳），而 06-20 基线打 `lean-6module-v1.1`（freshness 机械门那个子版本）。属版本戳回落到 canonical，**非缺陷**，记录备查。

## 5. 一句话

本轮 NVDA 是一次**诚实、机械新鲜度独立可复现过关（我用真 Python 重跑 exit 0、artifact byte-identical）、派生数与 06-20 δ 全部手工对得上、明确不复现 INC-001（价格区间中部非贴低）**的现价+regime 刷新：WATCH（新钱 0%）/ HOLD 正确封顶、regime 真并入 M4/M5、无伪造引语/失配数字、诚实标 DECISION_DRAFT——**按本批 `PLAN.md` 所定范围，本档 clean 且交齐产物**；唯一实质告警是**跨档案遗留**的 06-19 IC panel 仍停在被 INC-001 错价推翻的 STARTER 结论且未标 superseded（07-10 已提、责任在 06-19 档），本档未引用它、故不失效，但建议 repo 侧补一行作废标注。

---
*Checker 独立性声明*: 本报告由独立 Checker 出具（≠ Runner）。核验方法 = 真 Python 重跑 `verify_freshness.py`（exit 0，artifact byte-identical）+ 手工重算全部派生数（py 3.9）+ 逐项比对 06-20 基线 decision_card + 按 `_mega7_2026-07-28/PLAN.md` 范围核 A–F gate。
