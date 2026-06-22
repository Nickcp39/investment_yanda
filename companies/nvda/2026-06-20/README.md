# NVDA Dossier — CORRECTED re-run (as_of 2026-06-20)

**Verdict: WATCH（新钱 0%）/ 存量 HOLD** · status **DECISION_DRAFT** · 完整度 ~65% · ceiling = STARTER（价格门更严，封到 WATCH）· pipeline **lean-6module-v1.1**

> ⚠ **这是对 `../2026-06-19/` 的修正重跑。** 那一版把现价写成 **$145.48**（≈ 52 周最低 $142.03），真实价是 **$210.69**（Yahoo + stockanalysis + websearch 三源一致）。45% 错价把 base 5y IRR 从真实的 +4.8% 抬成 +13%，verdict 从 **WATCH** 误判成"价格友好 STARTER #1"。根因与机制修复见 `backtests/framework_validation/INCIDENTS.md` **INC-001**。本版已过 `scripts/verify_freshness.py`（见 `freshness_check.json` status=PASS）。

一句话: NVDA 是 AI 全栈算力瓶颈，owner earnings 干净（capex-light, FCF≈OE ~$182B）、净现金 ~$72B —— **生意卓越**；但现价 $210.69（forward ~28x, OE yield 3.5%, base 5y IRR **+4.8% < 8% hurdle**, 距高点仅 −11%）**无安全边际**，价格成为 binding constraint → 新钱 **WATCH**。镜像 GOOGL/AAPL（好生意，贵）。China 由错版"永久损失"改判为 **H200 许可重启 = 可恢复期权**。

## 文件结构（修正决策包）
本目录是 **freshness-corrected 决策包**。决策关键文件已按 $210.69 重写并内部对账；价格无关模块从 `../2026-06-19/` 原样带过（fundamentals 未变）；被错价污染的衍生文件（ic_panel / memo / audit / brief / operator_underwriting / financial_quality 等）**未带过**，仍可在 `../2026-06-19/` 查阅，结论以本目录 decision_card 为准。

| 文件 | 内容 | 状态 |
|---|---|---|
| **decision_card.json + .md** | 锁定卡（v1.1 版本戳，verdict WATCH）| ✅ 重写 |
| **valuation.md + model/scenario_model.csv** | M6 估值（base IRR +4.8%，价格带）| ✅ 重写 |
| **facts.md** | EVIDENCE/INTERPRETATION/SENTIMENT/OPEN（价格/China/情绪已改正）| ✅ 重写 |
| **claim_ledger.csv + source_register.md** | 来源分级（+ S008/S010/S011，LIVE 加 decay 轴）| ✅ 重写 |
| **inversion_map.md** | M5 失败路径（China 改判，F6 价格成卡点）| ✅ 重写 |
| **freshness.json** | LIVE 数据 manifest（≥2 源/字段）| 🆕 v1.1 |
| **freshness_check.json + .txt** | `verify_freshness.py` 产物（status=PASS）| 🆕 v1.1 门 |
| business_model.md / moat_map.md / bottleneck_map.md / value_chain_map.md | M2/M3 生意+护城河（价格无关）| 带自 06-19 |
| model/financial_history.csv / owner_earnings_bridge.csv | M4 FILED 财务（价格无关）| 带自 06-19 |
| raw/_q1fy27pr.html / _q1fy27cfo.html | 一手 SEC 原文 | 带自 06-19 |

## 诚实标签
DECISION_DRAFT，非 COMPLETE。载荷性当前事实（FY26 + Q1 FY27）全回挂 A1/A2 且独立复核；**LIVE 数据（价格/China）经 ≥2 源交叉验证并过机械 freshness 门**。OPEN: 10-K 逐行、10 年序列、proxy、custom-silicon 定量份额（blocking）、China H200 重启金额量级、供应承诺。
