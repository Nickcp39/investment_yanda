# TSLA Checker Report — mega7_2026-06-19

裁定: **CLEAN**（一项次要修正建议，不改 verdict/状态）
真实状态标签: **DECISION_DRAFT**（诚实；研究自述无 COMPLETE 越级措辞）
verdict / size / ceiling: **WATCH · 新钱 0% · ceiling = WATCH** ← 是否被完整度正确封顶: **是**（完整度 ~55% → WATCH 区间；价格更紧地独立封顶，未越顶）

## Gate 勾选
- **A. Scope & Definition** ✓ — ticker/share class(单一普通股)/as_of=2026-06-19/决策目的/时间跨度均冻结；完成标准（11-stage + lean-6module）先于结论；状态标签 DECISION_DRAFT 不 stale。
- **B. Evidence(M1)** ✓ — source_register 12 源含名/日期/link/tier；raw_extracts 对每条载荷 claim 有摘录；claim_ledger 带 tier + source_id + 验证状态；facts.md 严格分 EVIDENCE/INTERPRETATION/SENTIMENT/OPEN；memo 无裸 claim（每条挂 [Sxxx] 或显式 OPEN）。**来源纪律到位**：robotaxi/Optimus/FSD 一律入 SENTIMENT/INTERPRETATION，明确不进 EVIDENCE、不支撑 buy；无 D1 社媒进 EVIDENCE。SEC 403 缺口诚实登记为 O1（关键缺口）。
- **C. 11-Stage 覆盖** ✓ — 八模块各有产物；Stage 8 IC Panel 五灵魂（段永平主审 + Buffett/Munger/Marks/Klarman）各出票 + 一轮 critique + 扩展灵魂（Li Lu/Soros/Graham）触发检查。**无伪造引语**（见下）。
- **D. Model & Math(M4/M6)** ✓ — 营收/费用/capex 模型 tied to evidence；owner earnings 桥（GAAP NI vs 正常化 OE）分开；implied expectations 从当前价 $400.49 反推（市场已定价 moonshot）；三情景 + moonshot 与假设对账，公式可审计（已独立重算，见下）。
- **E. Open Questions** ✓ — O1-O6 分类清楚；O1(分部利润)/O2(robotaxi 单位经济) 显式封顶完整度；价格封顶给出独立、不依赖完整度的理由。
- **F. Audit & Consistency** ✓ — audit.md 查过 stale（首次建档无 v1/v2 残留）；数字前后一致；decision_card.json schema 完整且版本戳 = lean-6module-v1 / weights none / run_date 2026-06-19（**戳齐，卡有效可比**）。

## 独立验证项（不信任 Runner，逐项查）
1. **数字勾稽（已用 PowerShell 重算）**: market cap $1,412.9B(≈$1.41T) ✓ / P/E 370.8≈371x ✓ / P/FCF 227.2x ✓ / OE yield 0.35% ✓ / FCF yield 0.44% ✓ / IRR bear −26.8% base −16.9% bull +5.4% moon +20.8% ✓（与卡 −27/−17/+5/+21 一致）/ 距高 −19.7% 高于低 +38.7% ✓ / 营业利润率 FY22 16.8%→FY25 4.6% ✓ / Q1 GM 21.1% ✓。**decision_card / valuation.md / facts.md / audit.md 四处同价 $400.49、同股数 3,528M、同市值，无失配。**
2. **verdict 未越顶**: 完整度 55% 上限 = WATCH；卡给 WATCH，**未越顶**。size 与耐久性匹配：uncertain 生意 + key-man + 价格无 MOS → 0%，符合"周期/未确认不得 Core"。
3. **伪造引语检查**: ic_panel §0 显式声明"不放进引号假装逐字原话，引用均为公开著作/股东信/备忘录反复表述的立场"。抽查 — Buffett owner earnings(1986 股东信定义) + "price is what you pay"、Munger "show me the incentive / invert"、Marks second-level thinking、Klarman margin-of-safety、段永平"买股票就是买公司/不为清单/私有化测试" — **均为真实可考的公开立场，无杜撰逐字名言**。合规。
4. **来源真实性（WebSearch 抽验）**: (a) S009/S010 $1T pay package — CBS/Bloomberg/CNBC 证实 2025-11-06 股东 75% 批准、423.7M 股 grant、ISS/Glass Lewis/挪威主权基金异议，public_date 真实；(b) S004 Tesla 官方 X 交付报告 URL 实在，FY25 交付 1,636,129 / 能源 46.7GWh 与报告逐字一致。**两源均真实存在、日期真实。**
5. **数据新鲜度**: 锚定季 Q1 2026(ended 2026-03-31) 为 as_of 当下最新季报；价格 2026-06-18 收盘(≤ as_of 最新可得)。价格走 Yahoo chart API（repo 既定源），非 Stooq。**合规、无过期数字当现行。**

## FIX 清单
1) **[次要，建议不强制]** facts.md L24 / raw_extracts Block C2 称能源储能 FY25 46.7GWh "翻倍以上(more than doubled)"。公开数据 2024 ≈31.4GWh → 46.7GWh 实为 **+48%**，非"翻倍"。属增长腿无疑（thesis 不变、不进 DELIVERED OE），但措辞夸大约 1.5×。建议改为"同比约 +48%/接近翻倍"。**不影响 verdict/size/ceiling**（能源利润率本就 O5 OPEN、不计入 DELIVERED OE）。指到: `companies/tsla/facts.md`、`companies/tsla/raw/raw_extracts.md`。

## 伪造引语 / 失配数字
**无。** 引语全部为标注的释义/公开立场，无杜撰名言；recompute 的所有数字（市值/P-E/P-FCF/IRR/利润率/价格位置）与 decision_card、valuation、facts、audit 完全一致，无跨文件失配。唯一瑕疵是上条能源增速措辞夸大，非数字失配（46.7GWh 数值正确），不动 thesis。

## 一句话
**这家这轮可信度高**：决策驱动事实多源交叉 + 独立重算全部勾稽、来源真实可考、引语无杜撰、版本戳齐、WATCH-0% verdict 被完整度(55%)与价格(无 MOS)双重正确封顶且诚实标 DECISION_DRAFT；唯一可挑是能源"翻倍"措辞略夸（+48% 实际），不改结论 —— 判 **CLEAN**。
