# MSFT Checker Report — mega7_2026-06-19

裁定: **CLEAN**

真实状态标签: **DECISION_DRAFT** （research_status / memo / decision_card 三处一致；无 "COMPLETE/完整重跑完成" 越级措辞 — 反而显式声明 "本轮未达 COMPLETE"，语言诚实）

verdict / size / ceiling: **STARTER**（new money）/ existing **ADD** · 初始 4% · 上限暂封 9% · ceiling = STARTER（完整度 ~65% + OpenAI/capex 信息缺口，**非价格**）
← 是否被完整度正确封顶: **是**。completeness ~65% 落在 60–80% 区间 → 上限 STARTER；verdict = STARTER，**未越顶**（既未上 CORE，也未因价格退回 WATCH——价格端有正 MOS，封顶来源是完整度，逻辑自洽且与 GOOGL 案对照清晰）。size 与耐久性匹配：4% 起、上限 9% 待两缺口补强，未在未确认 capex ROI 下给 Core 级 size，合规。

## Gate 勾选: A✓ / B✓ / C✓ / D✓ / E✓ / F✓ （独立复核全过；下列为已验证项与轻微观察）

- **A. Scope & Definition** ✓ — ticker/share class(one-share-one-vote)/as_of=2026-06-19/决策目的/十年跨度 已冻结；完成标准先于结论写下；状态标签不 stale（cold-start 无旧版本）。
- **B. Evidence** ✓ — source_register 含每个 memo/model 用到的来源（名+日期+link+tier）；claim_ledger.csv ~40 行带 source_id + tier + destination；facts.md 只收 A1/A2 或显式 derived；memo 无裸 claim。**来源纪律已守**：FY26 $190B capex 指引正确标为 B2/OPEN（来自电话会，未拿 transcript），**FCF 计算一律用现金流量表自有 PP&E 口径（$107B 年化），未用 $190B 算 FCF** — 这是最容易被滥用的点，Runner 处理正确。KOL/媒体（coindcx/CNBC/AlphaStreet）只进 SENTIMENT/lead，未直接支撑 BUY。
- **C. 11-Stage 覆盖** ✓ — 八模块产物齐全（business/financial_quality/value_chain/moat/bottleneck/operator/inversion/valuation）；Stage 8 IC Panel 存在，五灵魂（段永平主审 + Buffett/Munger/Marks/Klarman）各出票 + 一轮 critique。
- **D. Model & Math** ✓ — owner_earnings_bridge.csv 把 OE 区间（$73/112/125B）按 capex 拆分假设分开列示，明确标 "derived-assumption"，未把假设当证据；implied expectations 从当前价 $379.40 反推；三情景与假设对账，公式可审计。
- **E. Open Questions** ✓ — O1–O7 分类清楚；O2/O3 显式封顶 verdict（blocking→STARTER），O4/O5/O7 标 monitoring/non-blocking 并给不封顶理由。
- **F. Audit & Consistency** ✓ — decision_card.json schema 完整且**版本戳 = lean-6module-v1 / none / 2026-06-19**（已戳，卡有效可比）；数字前后一致（见下）。

## 独立验证结果（不只信 Runner）

1. **数字对账 — 全部 tie out**（手算复核）：
   - market_cap = 379.40 × 7.428B = **$2,818B** ✓（json `as_of_market_cap` 2.818e12 一致）
   - P/E = 2818 / 125.2 (TTM NI) = **22.5×** ✓
   - 收益率 = 125.2 / 2818 = **4.44%** ✓
   - FCF yield = 72.9 / 2818 = **2.59%** ✓；P/FCF = **38.7×** ✓
   - as_of_price $379.40、市值 $2.82T、P/E 22.5×、收益率 4.44% 在 decision_card.json / .md / valuation.md / facts.md / claim_ledger.csv **五处完全一致**，无失配。
2. **伪造引语检查 — 无**：抽查 ic_panel §1.2 Munger 的 "Show me the incentive and I will show you the outcome" 与 "Invert, always invert" — 均为 Munger 公开反复表述的真实立场，且 panel 在 §0 纪律明确声明 "凡引用均为公开著作/股东信/备忘录里反复表述的立场，不放进引号假装逐字原话"，Buffett owner-earnings(1986 股东信)/Marks second-level thinking/Klarman《Margin of Safety》同理标注为 lens/释义，**无杜撰具体名言**。
3. **来源真实性 — 已 WebSearch 核验**：Microsoft Q3 FY2026 财报确为 **2026-04-29** 发布，revenue $82.9B(+18%)、Azure +40%、AI run-rate $37B、Microsoft Cloud $54.5B(+29%)、RPO $627B、FY26 capex ~$190B — 与 dossier 的 E8/E11/E12/E13/E14 及 source public_date 完全吻合（来源：CNBC / Microsoft IR / AlphaStreet，2026-04-29）。SEC XBRL CIK 0000789019 为 MSFT 正确 CIK。价格源走 Yahoo chart API（repo 既定源），非失效的 Stooq ✓。
4. **数据新鲜度** ✓：Q3 FY26（end 2026-03-31，报 2026-04-29）是 as_of=2026-06-19 当下最新季报；价格 2026-06-18 收盘为最新交易日；无过期数字被当 "当前"。

## FIX 清单
（无强制 FIX。以下为非阻断的轻微观察，不影响 CLEAN 裁定）
1. **轻微** — `source_register.md` 把 MSFT-8K-2026-06（2026-06-05 filed）列为 A1 源并标 "verify item"，但 facts O5 自承其 item 内容本轮未读。它未被任何 load-bearing claim 引用（仅登记待核），故不构成裸 claim；建议下一轮或读其 item、或从主源表移到 "待核 OPEN" 区以免误读为已用证据。
2. **轻微/已自披露** — base IRR +9.5% 依赖 OE0=$112B（~40% capex 为成长）这一不可观测假设；Runner 已在 runner_dissent、owner_earnings_bridge、ic_panel §2③ 三处显式标注为 assumption 并据此封顶 STARTER，处理透明，无需修，仅作风险登记。

## 伪造引语 / 失配数字: **无**
- 投资人引语：无杜撰，均标注为 paraphrase/公开立场/lens。
- 数字：as_of_price / market_cap / P/E / 收益率 / FCF yield 跨 5 文件一致，且与公开记录吻合。

## 一句话
这家这轮**可信度高**：财务一手底座扎实（10yr XBRL + 已核验的 Q3 FY26 IR），数字跨文件且对公开记录全部 tie out，无裸 claim、无伪造引语、版本戳齐全，verdict(STARTER) 被完整度(~65%)正确封顶且 Runner 诚实自承未到 COMPLETE — 是一份诚实、可比、未夸大的 DECISION_DRAFT。
