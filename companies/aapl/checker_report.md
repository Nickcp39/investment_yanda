# AAPL Checker Report — mega7_2026-06-19

裁定: **CLEAN**（含 1 项 nit fix，不影响 verdict）

真实状态标签: **DECISION_DRAFT**（措辞与档案全程一致；无 COMPLETE 越级语言）

verdict / size / ceiling: **新钱 WATCH（0%）/ 存量 HOLD · max ~15% · ceiling WATCH（价格门 binding）** ← 是否被完整度正确封顶: **是**
- 完整度 ~60% → 完整度天花板落 STARTER（60–80）下沿；M6 价格门更严，把 verdict 封到 WATCH。WATCH 未超任一上限。size 0% 与"无 MOS"匹配；耐久性 HIGH 未被用来抬 size（仅在价格配合时才支持 Core）—— size 与耐久性匹配规则通过。

Gate 勾选: A✓ / B✓ / C✓ / D✓ / E✓ / F✓（全过；4B/4F partial 已显式标注为 haircut，不阻断 DECISION_DRAFT）

## 独立复核（非信任 Runner）
- **裸 claim**: 无。facts.md 载荷数全挂 [S001]/[S002]，价格 [S005]，WWDC [S006]，TAC 风险显式标 OPEN/B1（不入 EVIDENCE、不直接支撑 verdict）。KOL/社媒明确未使用（source_register §取数说明）。
- **raw 实存性**: 复核 `raw/_q2fy26_8k.html`(169KB) 与 `raw/_q4fy25_8k.html`(198KB) 确为 SEC EX-99.1 原文，grep 逐项命中全部载荷数：Q2 111,184 / 56,994 / 30,976 / 20,497 / 14,725,873 / 54,781 / 29,578 / 2.01；FY25 416,161 / 112,010 / 109,158 / 64,377 / 90,711 / 15,004,697。非空壳、非杜撰。
- **decision_card schema**: 完整且版本戳 = lean-6module-v1 / weights none / run_date 2026-06-19 ✓。六模块信号齐全，sources_used 带 public_date。
- **数字独立重算（awk）**: 市值 4,388.5B ✓ | TTM NI 122,575M ✓ | P/E 35.8x ✓ | P/OE 36.6x ✓ | OE yield 2.73% ✓ | 净现金 61,884M = 1.41% 市值 ✓ | base IRR +2.64%（档案 +2.7%，四舍五入一致）✓ | buy-below 8% = $231.1 ✓ | Q2 GM 49.27% ✓ | Services FY25 +13.5% ✓ | China FY25 −3.8% ✓ | iPhone Q2 +21.7% ✓。decision_card / valuation.md / facts.md / audit.md 四处同一数字前后一致。
- **IC panel 伪造引语**: 无。panel 铁律 2 明令不放杜撰逐字引号；抽查 Buffett「price is what you pay, value is what you get」与 Munger「great business at a fair price」均为公开反复表述的真实立场，且未冒充逐字原话，标为"真实可考立场"。段永平"不为清单/100% 私有化测试"为其公开框架。合规。
- **价格新鲜度/合规**: 价格走 Yahoo chart API（repo 既定，非 Stooq）✓。raw JSON regularMarketTime 解出 2026-06-18 收盘 = ≤ as_of 2026-06-19 的最后交易日；2026-06-19 当日未当冻结边沿。最新季 = Q2 FY26（ended 2026-03-28）为当下最新可得，无过期数字当"当前"。
- **状态诚实**: completion_checker / research_status / README 全用 DECISION_DRAFT / WATCH / HOLD，明列 4B/4F partial 与 O1–O6 OPEN；无"彻底跑完/full complete"。

## FIX 清单
1) **(nit, 非阻断)** 52 周低价失配：`raw/_yahoo_price.json` 原值 `fiftyTwoWeekLow: 196.86`，但 `facts.md` line 34、`decision_card.json` 无、`raw/primary_extracts.md` BLOCK C 与 `source_register.md` 均写 **$198.96**（数字转置 96↔98 抄录错误）。该数非载荷项（52 周低不进估值/IRR），不改 verdict；但属源对账错误，建议改回 $196.86 以对齐一手。指到: `companies/aapl/facts.md`、`companies/aapl/source_register.md`、`companies/aapl/raw/primary_extracts.md`。

## 伪造引语 / 失配数字
- 伪造引语: **无**。
- 失配数字: **仅 1 项 nit** —— 52 周低 196.86(源) vs 198.96(档案)，非载荷、不影响任何结论。所有载荷数（市值/P-E/P-OE/OE yield/IRR/净现金/GM/分部）独立重算全部对得上。

## 一句话
这家这轮**可信**：载荷事实全回挂可核验的一手 SEC 原文、关键算术独立重算逐项 tie、版本戳齐、verdict 被价格门正确封到 WATCH（未越完整度上限）、无伪造引语、状态标签诚实为 DECISION_DRAFT；唯一瑕疵是一个非载荷的 52 周低价抄录转置（196.86→198.96），改一行即净。
