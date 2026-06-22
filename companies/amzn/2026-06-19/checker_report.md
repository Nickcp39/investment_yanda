# AMZN Checker Report — mega7_2026-06-19

裁定: **CLEAN**
真实状态标签: **DECISION_DRAFT**（与 research_status.md 自述一致；未谎称 COMPLETE）
verdict / size / ceiling: **WATCH · 新钱 size 0% · ceiling = WATCH（价格封顶）** ← 是否被完整度正确封顶: **是**

## Gate 勾选: A✓ / B✓ / C✓ / D✓ / E✓ / F✓
- **A Scope**: ticker / share class（post-20:1 split）/ as_of=2026-06-19 / 决策问题 / 时间跨度全冻结；完成标准先于结论写下；状态标签 DECISION_DRAFT 不 stale。✓
- **B Evidence**: source_register 8 个来源各带名+日期+link/path+tier；raw/ 有原始 8-K HTML（两份本地落盘 ~600KB 各）+ raw_extracts.md 原文短摘；claim_ledger.csv 每行带 source_id + tier + 验证状态；facts.md 严格分 EVIDENCE/INTERPRETATION/SENTIMENT/OPEN/Contradictions；memo 无裸 claim（每条挂 [Sxxx] 或显式 OPEN）。**KOL/社媒零进 EVIDENCE**；S006 电话会口径明确降权 B1/A2 转述、backlog/Trainium 仅作线索不支撑 buy。✓
- **C 覆盖**: Stage 0–10 各有产物（business/financial_quality/value_chain/moat/bottleneck/operator/inversion/valuation 八模块齐）；Stage 8 IC Panel 存在，五灵魂（段永平主审 + Buffett/Munger/Marks/Klarman）各出票 + 一轮 critique。✓
- **D Model & Math**: segment_model + scenario_model 双口径三情景；owner earnings 桥**显式标记不闭合**（净利 vs 正常化 OE 分开、用 band 表达）；implied IRR 从当前价反推；关键公式可审计。✓（O4 拆分缺一手已诚实降级，未假装算出点估）
- **E Open Questions**: O1–O6 分类，O4（$200B capex 维护/增长拆分 + ROIC）显式标 blocking 并封顶 verdict；其余标 haircut/非封顶。✓
- **F Audit & Consistency**: audit.md 查过 stale（首次建档无 v1/v2）；数字前后一致（见下）；decision_card.json schema 完整且版本戳 = lean-6module-v1 / weights none / run_date 2026-06-19。✓

## 独立验证结果（非信任 Runner）
1. **载荷数回原始来源**: 直接 grep raw/_q1_2026_8k_ex991.html 与 _fy2025_q4_8k_ex991.html，逐项命中：净销售 $181.5B、AWS +28% 到 $37.6B、OI $23.9B、净利 $30.3B、Anthropic 税前收益 $16.8B（"included in non-operating income from our investments in Anthropic"）、OCF TTM $148.5B、FCF TTM $1.2B、Q1 capex 44,203 / TTM 151,003、长债 65,648→119,074；FY25 营收 $716.9B、OI $80.0B、AWS OI $45.6B、FCF $11.2B。**全部一手命中，无失配。**
2. **数字重算（PowerShell）**: 市值 10,874M×$244.39 = $2,657.5B ≈ $2.66T（卡片 2657000000000 ✓）；P/E 244.39/7.17 = 34.1 ✓；AWS OI 占比 FY25 57.0% / Q1 59.4%（卡片"57–59%" ✓）；起始收益率 NOPAT 67/2657=2.52%、OE 55/2657=2.07%（卡片 2.1–2.5% ✓）；5y IRR bear −13.6%/base −1.5%/bull +7.6%（卡片 −13.5/−1.5/+7.7 ✓，舍入级一致）；现价距 52 周高 −11.1%、距低 +22.9%（"−11% / 中上部" ✓）。**全口径对账通过。**
3. **外部交叉验证**: WebSearch 独立确认 Q1 2026 营收 $181.5B、AWS +28%/$37.6B/15 季最快/run-rate ~$150B、OI $23.9B 13.1% 记录、AWS AI run-rate >$15B；SEC 8-K 与 aboutamazon IR 链接真实存在、public_date 2026-04-29 真实。
4. **IC Panel 伪造引语排查**: 通读五灵魂，**未发现杜撰逐字名言**。唯一带引号的 Munger 短语（"Show me the incentive...""Invert, always invert"）为公开反复表述、非编造；Buffett 1986 股东信 owner earnings、Marks "it's not what you buy, it's what you pay"、Klarman margin of safety、段永平"不为清单/平常心"均以**立场/释义**呈现而非伪造原话。模块开头铁律 2 显式声明"不放进引号假装逐字原话"，执行到位。抽查 2 条（Munger 激励、段永平私有化测试）均为真实可考立场。✓
5. **verdict 上限**: 完整度 ~62% → 完整度 ceiling = STARTER（60–80）；价格无 MOS（base IRR 负）→ 价格封顶 WATCH，取更严者。verdict=WATCH **未超顶**，且 0% size 与"周期/未确认不得给开仓档"一致。✓
6. **状态标签诚实**: research_status.md 明写"诚实标签：这是决策草案 DECISION_DRAFT，不是 COMPLETE"，措辞与标签匹配，无"彻底跑完/full research complete"越级表述。✓
7. **活体新鲜度**: 最新一季为 Q1 2026（ended 2026-03-31，8-K filed 2026-04-29）+ FY25 全年，as_of=2026-06-19 当下确为最新可得季报；价格走 Yahoo chart API（S004，repo 既定来源，非 Stooq），2026-06-18 close 作 ≤as_of 冻结边，处理合规。✓

## FIX 清单
无强制 FIX。可选改进（非封顶、不影响裁定）：
1) decision_card.json M3 finding 写"~57-59% of total OI"，facts.md INTERPRETATION 写"~59%"——两者均落在已验证区间（FY25 57% / Q1 59%），口径轻微不统一，建议任一处注明"FY25 57% / Q1 59%"以彻底消歧。(decision_card.json / facts.md)
2) O4（$200B capex 维护/增长拆分 + ROIC）与 O5（backlog/Trainium 官方 transcript）是解 WATCH 封顶的胜负手，后续补一手即可升完整度 >80% — 已在 monitor/research_status 记录，仅作进度提醒。

## 伪造引语 / 失配数字
**无。** 无杜撰逐字名言；as_of_price / market_cap / P/E / AWS OI 占比 / 起始收益率 / 三情景 IRR / 52 周位置在 decision_card(.json+.md) / valuation.md / facts.md / audit.md / scenario_model.csv 间**完全一致**，且全部回挂一手 8-K（重算 + 原文 grep + 外部 WebSearch 三重核对通过）。

## 一句话
**这家这轮可信度高：载荷性当前事实（Q1 2026 + FY25）全部回挂落盘的 SEC 8-K 原文并经独立重算与外部交叉验证，数字零失配、引语零杜撰、状态标签诚实（DECISION_DRAFT 而非 COMPLETE）、verdict=WATCH 被价格正确封顶（先于 62% 完整度的 STARTER 封顶生效），与 GOOGL 同构、与 NVDA 价格友好相反——CLEAN，唯一实质短板是 owner earnings 桥因 $200B capex 拆分缺一手（O4）已被诚实降级而非掩盖。**
