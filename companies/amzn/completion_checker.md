# AMZN Completion Checker — as_of 2026-06-19

**Status label: `DECISION_DRAFT`** （完整度 ~62%；**非 COMPLETE**）

依据 `frameworks/research_completion_checker.md` 的 A–F gate。

## A. Scope And Definition
- [x] Scope frozen: AMZN, 单一普通股, as_of 2026-06-19, 新钱建仓决策, 10 年视角。
- [x] Completion standard 写在最终答案前（本批现实目标 = DECISION_DRAFT）。
- [x] 状态标签非 stale（首次建档，全文件同 as_of）。

## B. Evidence Engineering
- [x] Source register 含所有 memo/model 用到的来源（S001–S008）。
- [x] 关键 claim 有 raw 摘录（raw/raw_extracts.md，含本地 SEC 8-K HTML 落盘）。
- [x] Claim ledger 含 tier/验证状态/source_id/destination。
- [x] Facts 仅收已验证或明标派生的 claim；GAAP 净利 Anthropic 失真警告已贯穿。
- [x] memo 每条 claim 有 source_id 或显式 OPEN。
- [x] 无 prior 版本（首次建档；历史盲测案仅作 thesis 先验，未当当前事实）。

## C. Ten-Layer Research
- [x] 1 方向 / [x] 2 业务 thesis / [x] 3 证据 / [partial] 4 会计趋势（**owner earnings 桥不闭合: capex 维护/增长拆分 O4**）/ [x] 5 价值链 / [x] 6 护城河/瓶颈 / [partial] 7 operator（proxy OPEN O3）/ [x] 8 反演 / [x] 9 估值 / [x] 10 决策/监控。

## D. Model And Math
- [x] 营收驱动（三段细分）tied to evidence。
- [partial] 费用/capex 模型（capex 总额 A1，但**维护 vs 增长拆分 + ROIC 缺一手 O4**）。
- [partial] owner earnings 桥（**显式标记无法闭合**，用双口径 band 代替点估）。
- [x] 隐含预期/三情景从现价重建（双口径 IRR 勾稽 audit §4）。
- [x] 情景与来源一致（标 E1 scenario）。
- [x] 关键公式可审计。

## E. Open Questions And Blockers
- [x] OPEN 分类: O1/O2/O5/O6 monitoring; O3 non-blocking; **O4 $200B capex 维护拆分+ROIC = blocking（owner earnings 桥胜负手）**。
- [x] Blocking 问题显式封顶 verdict（但实际生效卡点是价格 → WATCH，比完整度封顶更严）。
- [x] 非阻断问题给了不阻断理由。
- [x] backlog 在 monitor.md Next Review。

## F. Audit And Consistency
- [x] 内部审计查 stale（audit §5，无 stale）。
- [x] research_status 反映当前状态。
- [x] 无旧版本需归档。
- [x] decision_card.json 通过 JSON 校验。
- [x] 最终答案报真实状态（DECISION_DRAFT 非 COMPLETE）。

## Required Final Self-Check
1. **状态标签**: DECISION_DRAFT。
2. **未过 gate**: C4 会计趋势（owner earnings 桥不闭合 O4）、C7 operator（proxy O3）、D2 费用模型（capex 拆分）、D3 owner earnings 桥（band 非点估）。
3. **升 COMPLETE 需要**: 10-K 逐行 capex 维护/增长拆分 + 增量 ROIC（解 O4）+ proxy（O3）+ Anthropic 会计（O6）→ 完整度 >80%。但**价格封顶 WATCH 独立于完整度——即便完整度到 80%，价格无 MOS 仍封 WATCH，须等价格跌破 ~$175 才升 STARTER**。
4. **stale 文件**: 无。
5. **措辞匹配**: 全文用 "决策草案/DECISION_DRAFT/WATCH"，未用 COMPLETE。
