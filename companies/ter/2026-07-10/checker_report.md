# TER Checker Report — mega7_2026-06-19 (AI-robotics batch)

裁定: **CLEAN**
真实状态标签: **DECISION_DRAFT** (completeness ~58%, 一次跑 — 诚实, 无 "完整完成/COMPLETE" 措辞)
verdict / size / ceiling: **new money WATCH (0%) · existing HOLD · size 0% · ceiling = WATCH (40–60% band)** ← 是否被完整度正确封顶: **是**。WATCH ≤ ceiling；价格 + capital-cycle 独立也指向 WATCH，非仅完整度伪影。
数据新鲜度: **PASS** (`freshness_check.json` status==PASS, exit_code 0) ← 有 PASS 产物，非强制 FIX。

## 独立复算 (skeptical re-fetch, 2026-07-10)
- Yahoo chart API (query1 **和** query2 两端点) 独立重抓: **price $359.60**, 52wk high **$487.91**, 52wk low **$88.60** — 与 dossier 逐位吻合。
- 市值恒等式: 156.54M × $359.60 = **$56.29B** ✓ (T3, delta 0.00%)。
- 七月崩盘序列独立确认: 07-06 $379.52 → 07-07 **$343.11** → 07-10 $359.60，与 facts/decision_card 的 "-29% peak-to-trough" 叙事一致。
- 第二独立源: dossier manifest 用 stockanalysis($359.60); Stooq 已反爬失效(与 repo 既知一致，不算缺口)。两独立 Yahoo 端点 + stockanalysis 三点一价，价格合规。
- FY2025 NI $554M → $56.29B/$554M = **101.6× ≈ ~102×** ✓；Robotics Q1'26 $91M/$1,282.5M = **7.1%** ✓；FY2025 robotics ~$308M/$3,190M = **~9.6%**(明确标 derived/O4)✓。

## Gate 勾选
- **A. Scope** ✅ — ticker/common/as_of 2026-07-10/新钱决策/5y 冻结 (step0_plan)；完成标准先写；标签不 stale。
- **B. Evidence** ✅ — source_register 全源带日期+tier+link；raw/ 有摘录；claim_ledger 带 tier+verify+destination；facts 只收已验证/明标 derived；memo 无裸 claim；D1 KOL 视频 (L1) 仅作 batch lead，从不进 EVIDENCE、从不支撑 verdict ✓。
- **C. 11-Stage** 🟡 — Stage 0–10 各有产物 (八模块齐)；Stage 8 IC panel 存在，五灵魂 (段永平主审) 各出票。**Stage 4 (segment op-income by year, O2) 与 Stage 7 (proxy/operator life-arc, O3) 标 🟡 OPEN** — 已分类为 monitoring，非 blocking，已封顶 WATCH。属完整度 haircut，非 gate 硬失败。
- **D. Model & Math** ✅ — 营收/分部模型、owner-earnings bridge、三情景从**当前价 $359.60** 反推 (bull +2.3% / base −14.8% / bear −25.6% IRR)，csv 可审计，与来源对账。
- **E. Open Questions** ✅ — O1 non-blocking / O2·O3·O5·O6 monitoring / O4 minor；blocking 项封顶 WATCH，non-blocking 给理由。
- **F. Audit & Consistency** ✅ — as_of_price $359.60 全文件一致 (T5)；市值恒等 (T3)；decision_card schema 完整且戳 **lean-6module-v1.1 / none / 2026-07-10** ✓；最终报真实状态。

## §4 强制新鲜度机械门
`verify_freshness.py` 产物 `freshness_check.json` 已提交，**status=PASS / exit 0**；T1–T5 全 PASS(52wk 含容、low/high hug +305.9%/−26.3%、市值恒等、distance-from-high、single-value-of-truth)。T6 两条 **WARN**(guidance 源 2026-04-29 / litigation 源 2026-04-28，距 as_of 72–73d > 45d)—**预期且已文档化**:Q1'26 是最新披露,Q2 财报在 as_of 之后,非隐瞒;非 blocking。WARN 不降 PASS。

## 批次 THESIS 诚实性核验 (本批专项)
- **robotics_revenue_pct = 有源**: Q1'26 **7.1%** [S001 一手 8-K PR]；FY2025 **~9.6%** [S005 B1，明标 derived/O4]。非手挥。
- **demand REAL-vs-ANTICIPATION = ANTICIPATION**,证据支撑: 分部亏损 (Q1'25 op loss −$22M)、低于自身 ~$365M breakeven、~5 年 $300–400M 停滞至下滑、具身 AI 上行仅 =一个 NVIDIA GTC demo("Generalist")=线索非现金。真正爆发需求在 semi-test (AI capex),且是周期性。诚实。
- **CAPITAL_CYCLE lens 已按 mandate 施于 robotics 分部**: applicable=partial;robotics stage=early/trough-exiting、supply barrier low-med(cobot/AMR 商品化,Fanuc/ABB/Doosan/Techman/JAKA);dominant semi-test=late/possible-peak,2026-07 HBM 过剩抛售 + 扩产放缓 = late-cycle 供给信号。caution=PEAK(压至 WATCH/no-chase)。到位。
- **real_bottleneck verdict = 有据**: Semi Test = 真 bottleneck(前沿 AI 芯片必测、只有 TER+Advantest、58–61% GM、qualification 转换成本)但**周期性**;Robotics = **CONCEPT**(无强制购买力、有替代、低转换、亏损)。即 TER 确有硬瓶颈——只是**不是 robotics 那个**。诚实且可证伪。
- **option-value-vs-core-value split 已做**: $56.29B 中 ~95%+ = 周期 ATE 峰值倍数,~3–5% = 亏损 robotics "具身 AI 期权"(~$308M 收入 × 慷慨 5–8× P/S)。valuation §4 + thesis (e) 明确。

## IC Panel 引语核验
五灵魂全部**明标为框架 lens/释义**("All views are framework lenses / paraphrase, NOT fabricated quotes. No investor quotation is attributed as verbatim")。**无伪造 verbatim 引语**。

## FIX 清单
无强制 FIX。以下为**升级至 STARTER/COMPLETE 前应闭合的既知 haircut**(Runner 已诚实记为 OPEN,非 gate 失败):
1. O2 — 2025/2026 分部经营利润(Semi Test vs Robotics 逐年盈利)：`facts.md` §OPEN / `audit.md`。锐化 robotics-drag,不太可能翻 WATCH。
2. O3 — proxy / operator life-arc(CEO Greg Smith 任期、董事会、激励)：`operator_underwriting.md` 仍 provisional 3.5/5。
3. O5 — Advantest 份额趋势(双寡头耐久性)：唯一可能改变结构性 thesis 的 veto 路径,应持续盯。
(以上到文件,均已在 dossier 内分类,非隐藏。)

## 伪造引语 / 失配数字
**无。** 价格独立三源对齐;市值恒等成立;robotics % 双口径(7.1% Q1 / ~9.6% FY)均带 basis;cash 口径差异(Dec'25 $322M vs Q1'26 ~$400M)系不同日期,非矛盾;版本戳完整。

## 一句话
这轮 **可信到 DECISION_DRAFT (~58%)**:价格逐位复算、freshness 机械门真过、verdict 被完整度正确封顶在 WATCH、robotics thesis 被一手证据诚实证伪(≤10% 收入、亏损、低于 breakeven、期权而非现金),无伪造引语、无失配数字、无裸 claim——**CLEAN**。核心信息:ATE 双寡头是看得懂的好生意,但现价 $359.60 在周期峰值用峰值倍数(~40–43× 2026E / ~102× FY2025),无安全边际,且把 TER 放进本批的 robotics 理由不成立 → 新钱 WATCH,STARTER 触发 ~$250–280(非峰值盈利且 AI-test 仍在打印)。
