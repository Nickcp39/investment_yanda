# TSLA Checker Report — mega7_2026-07-28 refresh (baseline mega7_2026-06-19)

**裁定: CLEAN**

**真实状态标签: `DECISION_DRAFT`**（completeness ~57%；未过度宣称 COMPLETE — 措辞铁律 PASS）

**verdict / size / ceiling: new_money=WATCH · existing=HOLD · business=uncertain · init 0% / max 3%（conditional, cyclical+narrative+key-man capped）· ceiling=WATCH**
← 是否被完整度正确封顶: **是**。完整度 57% 落 40–60% 带 → 上限 WATCH；new_money=WATCH 未超顶。size 与耐久性匹配（周期/未确认，非 Core 级；max 3% = low-starter，init 0%）。base-IRR 封顶（−12% 无 MOS）与完整度封顶方向一致。

**数据新鲜度: PASS（freshness_check.json, exit 0）— 且 Checker 独立复跑复现 PASS**
- 独立复跑 `verify_freshness.py`（输出写到 scratchpad，未覆盖 dossier）→ status=PASS, exit 0。独立 Yahoo 重抓 `refetched_yahoo=307.44000244140625`，与卡价 $307.44 **到分一致**（这正是 INC-001 缺失的独立拉取）。
- Checker 另做**直连 Yahoo chart 校验**（1y 日线）: meta regularMarketPrice=307.44 · fiftyTwoWeekHigh=498.83 · fiftyTwoWeekLow=297.82，末根 bar 2026-07-28=307.44。
- **不是 52 周极值抓取（与 INC-001 相反）**: 现价 $307.44 ≠ 序列极值（收盘序列 min=302.63 / intraday low=297.82）；是 2026-07-28 真实末收。de-rate 轨迹**独立复现**: 7/22 $374.01 → 7/23 $319.69（−14.52%，财报反应）→ 7/28 $307.44。真实抛售，非数据 bug。
- freshness.json manifest: 每个 LIVE 字段 ≥2 独立源（price 3 源、market_cap/52wk/shares/litigation 各 2、guidance 3）。价格走 Yahoo chart API + 3 源交叉。
- 唯一 WARN: T6 active_litigation（$1T 薪酬包源 2025-11-06，264d>45d）→ **非 block**，manifest 已说明为最新权威治理事件、按 overhang 处理，Runner 明确预告"T6 WARN expected"。

**Gate 勾选: A✓ / B✓(注) / C✓(注) / D✓ / E✓ / F✓**（无未过硬项；注见下）
- A 范围/完成标准/状态标签 — 全 ✓（as_of/目的/时间跨度冻结；完成标准先写=DECISION_DRAFT 55–75%；标签不 stale）。
- B 证据脊柱 — ✓，但为 **focused-refresh 的轻量脊柱**: 7/28 目录无独立 `claim_ledger.csv/source_register.md/facts.md`，来源改由 `decision_card.sources_used[]`（11 源带日期/tier/link）+ `freshness.json` 承载；Q2 新 claim 三源交叉（Electrek/CNBC/teslarati）。SEC 10-Q 逐行未直取（O1，已标 OPEN）。KOL/社媒未用于支撑 BUY（且 verdict=WATCH/0%）。DECISION_DRAFT 层可接受。
- C 11-Stage/IC 面板 — ✓（诚实范围）: 本轮为聚焦刷新，M2/M3 carry+adj、M4/M5/M6 refreshed；未重跑全 11 stage / IC 面板。6/19 基线 `companies/tsla/2026-06-19/` 含完整 11 stage 及 `ic_panel.md`，"carry forward"前提成立。未宣称 COMPLETE → 不要求全覆盖。
- D 模型/数学 — ✓ 全部独立复算通过（见下）。
- E Open Questions — ✓ O1/O2/O5/O7 各分类，明确"均不解封价格/利润池封顶"。
- F 审计/一致性 — ✓ 数字前后一致（独立核验）；schema 完整且版本戳 `lean-6module-v1 / none / 2026-07-28`；报真实状态。

**FIX 清单: 无（CLEAN）。**
下列为**非阻断观察项**（下一轮收口，不影响本轮裁定）:
1. `O7 股数口径`（freshness.json/valuation.md/decision_card）: 卡用 diluted 3,528M（FY25 carry）算市值/每股，stockanalysis 现示 ~3.95B basic → 市值区间 $1.08–1.21T。已诚实披露 + 保守旗标（若 3.95B，每股/IRR 再差 ~11%，阶梯偏乐观）。非错价，是待关 OPEN。
2. `freshness.json` T6 active_litigation WARN（264d）: 非 block，已 justified；下轮确认无更新权威治理事件即可。
3. `low_high_hug_justified:true`（freshness.json price 字段）为 Runner 可控旗标 — 本例**不 load-bearing**（现价 +3.23% off intraday low，已在 3% band 外，T2 无需该旗标即 PASS），且低位已被独立证实为真实抛售，未掩盖 INC-001。仅记录。
4. 轻量证据脊柱（见 Gate B）: 若后续要升 STARTER/COMPLETE，需补 7/28 自有 `claim_ledger.csv` + SEC 10-Q 分部利润（O1）。

**伪造引语/失配数字: 无。**
- 伪造引语: 无。7/28 文件中零投资人具名引用（段永平/巴菲特/芒格/Marks/Klarman 均未出现）；runner_dissent 仅泛引"five souls/chair 同框架"作对照，无归因引语。抓到的引号串均为内部论点措辞（C2 预测、regime 轮动描述），非引语。
- 失配数字: 无。独立复算全部吻合 — 市值 3528M×307.44=$1.0846T（卡 $1.085T，T3 0.00%）；P/E 307.44/1.08=284.7x（卡 285x）；off-high −38.4%、off-low +3.23%；IRR bear −22.9%/base −12.4%/bull +11.1%/moonshot +27.4%（卡 −23/−12/+11/+27，逐一对齐）；per-share 与 exit×OE、+净现金 identity 均闭合。delta_vs_0619 的 6/19→7/28 迁移（base −17→−12、bull +5→+11、P/E 371→285、mcap $1.413T→$1.085T）自洽。
- regime 已真正并入 M4/M5（非忽略）: M4 显含"AI-capex-audit regime punishes exactly this profile" + Q2 actuals；M5 有完整 regime 传导表（半导体暴跌/AI-capex 审计/苹果$5T>NVDA/FOMC），**CXMT/内存显式 N/A（无 memory 敞口）而非漏掉**。M4 −1→−2、M6 −2→−1 对冲逻辑成立。

**一句话:** 这轮 TSLA 可信度高 — 价格 $307.44 三源+独立重抓到分一致、de-rate 轨迹可复现，**是 INC-001 的正面反例（真实末收贴近而非等于 52 周低）**；数学全闭合、verdict 被 57% 完整度正确封在 WATCH、无伪造引语、regime 真并入 M4/M5；诚实标 DECISION_DRAFT。唯一实质待办是股数口径（O7）与 SEC 分部利润（O1），均已标 OPEN 且不解封 WATCH → **CLEAN**。

---
*Checker 独立动作留痕: (1) 复跑 `scripts/verify_freshness.py --dossier companies/tsla/2026-07-28 --out <scratchpad>` → PASS/exit0, refetched 307.44; (2) 直连 Yahoo 1y 校 52wk band + 末 6 根 bar；(3) 复算 IRR/mcap/PE/per-share/off-high/off-low；(4) grep 伪造引语=0；(5) 核对 6/19 基线 dossier 存在且含 ic_panel.md。*
