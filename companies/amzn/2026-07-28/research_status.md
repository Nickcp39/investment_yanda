# AMZN Research Status — as_of 2026-07-28

最后更新: 2026-07-28（mega7_2026-07-28 活体批次刷新）· pipeline_version=lean-6module-v1 · weights_version=none

**诚实标签: `DECISION_DRAFT`（~62% 完整度）· 不是 COMPLETE。** 本轮是**聚焦刷新**（换今天的价 + 叠加 regime，重算 M4/M5/M6，重导两轴 verdict），**非从零重研究**；durable 业务分析（M2/M3）沿用 6/19 基线并快速复核。

Decision question: 在 2026-07-28 的 regime（半导体暴跌轮动 / AI-capex 审计年 / 财报周 / FOMC）下，$230.86 的 AMZN 对新钱是否有安全边际？存量该怎么处理？

## Final Verdict 摘要
**新钱 WATCH · 存量 HOLD · size 0% · buy-below ~$178 · business good。** 价格 −5.5%（$244.39→$230.86）改善 base 5y IRR 到 −0.4%、bull 到 +8.9%，**但仍无 MOS**（起始收益率 ~2%、base ~0）；owner-earnings 桥仍不闭合（$200B capex，O4）；**Q2-2026 财报 7/30 才出、无法并入**。regime 放大 AMZN 最弱的 FCF-转化维度但未破坏 thesis。verdict 相对 6/19 **不变**。

## 数据新鲜度（强制机械门）— PASS
- `python scripts/verify_freshness.py --dossier companies/amzn/2026-07-28` → **STATUS: PASS（exit 0）**，`freshness_check.json` 已落盘。
- 价格 $230.86 三独立源一致（Yahoo / statmuse / stockanalysis，delta 0.0%）；独立 Yahoo 重抓 = $230.86 亦一致。
- Tripwires 全过：T1 band（196 ≤ 230.86 ≤ 274.99）· T2 未贴极值（+17.8% off low / −16.0% off high）· T3 市值恒等（10,874M×230.86=$2.510T，0.01%）· T4 距高对账（叙述 −16.0% = 卡隐含 −16.0%）· T5 单一真值（230.86 现于所有价格文件）· T6 指引新鲜（最新源 2026-07-15，13d）。
- **INC-001 防护确认**：$230.86 非 52 周极值（+17.8% 高于 52 周低），未复现 NVDA 抓极值 bug。

## Stage Checklist（刷新范围）
| Stage | Artifact | Status |
|---|---|---|
| 0 Idea Intake | ../_mega7_2026-07-28/PLAN.md | ✅ |
| M1 证据/价格 | freshness.json + freshness_check.json（PASS）| ✅ 价格三源；⚠️ Q2 未出 |
| M2 Business | 沿用 ../2026-06-19/business_model.md（快速复核：无破裂，Anthropic/Trainium 强化）| ✅ carry |
| M3 Moat/Operator | 沿用 ../2026-06-19/moat_map.md + operator_underwriting.md（快速复核：无变化）| ✅ carry |
| M4 Financial Reality | decision_card 内 + delta_vs_0619.md（**Q2-2026 7/30 未并入**）| ⚠️ partial（桥不闭合 O4 + Q2 pending）|
| M5 Inversion | inversion_map.md（叠 2026-07-28 regime）| ✅ refreshed |
| M6 Valuation | valuation.md（现价 $230.86 重算三情景）| ✅ refreshed |
| 两轴 verdict | decision_card.json + .md（版本戳）| ✅ locked |
| Δ vs 6/19 | delta_vs_0619.md | ✅ |
| 状态 | research_status.md | ✅ |

## OPEN gate（封顶完整度 ~62% → ceiling STARTER；价格更严 → 实际 WATCH）
- **O0 Q2-2026 未出（2026-07-30，迫近的二元催化）** — 本轮最大信息缺口，决策锁定于 print 前。
- **O4 $200B capex 维护/增长拆分 + 增量 ROIC（blocking，owner-earnings 桥胜负手）**。
- O1 10-K 逐行 · O3 DEF 14A proxy/operator 细节 · O5 backlog/Trainium 一手 · O6 Anthropic 会计。

## 升 verdict / 解封顶路径
①价格跌破 ~$178（MOS 出现、base IRR 回中个位数、贴 52 周低）→ 升 STARTER；②7/30 起 capex 强度回落 + FCF 回升 + AWS 增量利润匹配 capex（capex ROIC 兑现）→ 解 O4；③10-K 逐行 + proxy → 完整度 >80% 解 CORE 讨论。

## Next Review
**2026-07-30 Q2-2026 财报（迫近）**：AWS 增速、总营业利润率、capex 强度与 FCF、$200B 进度、任何 FCF 释放信号 → 直接影响 M4/O4 与是否升/降档。**FOMC 2026-07-29（Warsh）**：利率 → F4 杠杆/贴现率。价格触发：跌破 ~$178 → 升档 STARTER 候选。

## 独立性说明
本 Runner 不给自己打分；Checker 独立按 `../_mega7_2026-06-19/CHECKER.md` 出 `checker_report.md`。不确定项已入 runner_dissent / OPEN / delta_vs_0619。
