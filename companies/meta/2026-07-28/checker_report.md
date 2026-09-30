# META Checker Report — mega7_2026-07-28 (against _mega7_2026-06-19/CHECKER.md)

裁定: **CLEAN**
真实状态标签: **DECISION_DRAFT**（focused price-refresh；research_status/decision_card 自述一致，显式「非 COMPLETE，非从零重研究」，全程用「决策草案/REAFFIRM/focused refresh」，**未冒称 COMPLETE** → 措辞合规）
verdict / size / ceiling: **new_money=WATCH（initial 0% / buy-below ~$480 / max 5%）· existing=HOLD · ceiling=STARTER（完整度 ~60%）· 价格 + 事件择时把实际压到 WATCH** ← 是否被完整度正确封顶: **是**
数据新鲜度: **PASS（freshness_check.json, status=PASS, exit_code=0）**

Gate 勾选: **A✓ / B✓(carry) / C✓(carry) / D✓ / E✓ / F✓**（无阻断未过项；B/C 为 6/19 CLEAN 全量 dossier 沿用 + 本轮 no-thesis-break 复核，符合 DECISION_DRAFT 的诚实层级，未冒称 COMPLETE）

---

## 独立核验明细（不信 Runner，逐项重算）

### 价格完整性（INC-001 核心）✓
- as_of_price **$593.41** 在全部 10 个 price-bearing 文件中**单值一致**（grep：593.41 遍布 decision_card.json/.md、valuation、delta、inversion、research_status、model、freshness*、txt）。6/19 的 $577.22 **仅**出现在显式对照语境（「6/19 的 $577.22」「vs 577.22」），**无一处**把旧价当现价 → T5 single-value-of-truth PASS。
- **非 52 周极值贴合**：独立重算 +14.1% off low（$520.26）/ −25.5% off high（$796.25），在带内 → **INC-001 clear**（对照 NVDA $145≈52wk-low 的失败向量）。
- 双独立源：Yahoo chart API $593.41 + stockanalysis.com $593.41，0.0% delta；freshness_check.json 记录 refetched_yahoo=**593.4099731445312**（较卡值更精，系脚本真实产出而非手写 593.41 → authenticity 信号）。
- 52wk 高用 $796.25（实时 stockanalysis + CNBC，双源 0%），任务/ PLAN 表列 $790，差 0.8%，对每条 tripwire/verdict **immaterial**，Runner 已显式标注取更准值。

### D. Model & Math ✓（独立重算，全部 tie out，venv python）
- mcap: 2545M × 593.41 = **$1,510.2B**，vs 卡 $1,510B → 0.02% ✓
- fwd 经营 P/E: 1510 / 74.8 = **20.19x**（卡 ~20.2x）✓；FCF yield 49.6/1510 = **3.28%**（卡 ~3.3%）✓；trailing GAAP 1510/60.46 = **24.98x**（卡 ~25.0x）✓
- IRR（y5/593.41）^0.2−1：Bear **−11.0%** / Base **+3.4%** / Base-opt **+9.9%** / Bull **+14.6%** → **四条全对**卡值 ✓
- 公允价 @8%：base 701/1.08^5 = **$477.1**（现价 +24.4% ABOVE，卡 ~24%）✓；opt 950/1.08^5 = **$646.6**（现价 −8.2%，卡 ~8% below）✓
- delta vs 6/19 全对：price **+2.80%**（卡 +2.8%）、mcap **+2.04%**（卡 +2%）、6/19 base IRR **+4.0%**、6/19 距高 **−27.5%**、premiums vs $477 分别 **+21%/+24%** ✓
- owner-earnings 锚口径正确：op NI ~$74.8B 年化（剔 $8.03B 一次性税收）vs FCF ~$49.6B，差额=增长 capex；估值用 FCF/op NI，**未用 GAAP NI 直接估** ✓

### §3 Verdict 上限核验 ✓
- 完整度 ~60% 落在 40-60/60-80 边界。**无论取哪侧**（WATCH 顶 或 STARTER 顶），实际 new_money=**WATCH** 均 ≤ 上限 → **未超顶**。卡虽写「ceiling STARTER」但**实际交付的 verdict 是 WATCH**（被价格 + 7/29 双二元事件压下），未动用该 headroom → 无 overclaim。
- size：init 0% / max 5% = starter 级封顶，operator 3/5 + O4 未决 → **非 Core-sized**，与耐久性匹配 ✓；existing=HOLD 合理（引擎完好、资产负债表存活、非离谱高估、无证伪）✓

### §4 活体新鲜度（机械硬门）✓
- freshness_check.json **status=PASS / exit_code=0** 已提交 → 满足机械门（无 PASS 产物才自动 FIX-NEEDED）。
- freshness.json manifest 齐：price(yahoo+stockanalysis)、52wk_hi/lo(stockanalysis+CNBC)、shares、active_litigation(techtimes+ftc.gov)、guidance(blockonomi+SEC 8-K) 各 ≥2 源；**INC-001 关键的 price/52wk 均真双独立源**。
- 价格源合规：Yahoo chart API（repo 既定源）+ ≥2 源交叉 0% → 非「单源+只验日期」的 INC-001 洞。
- 本轮 T1–T5 全 PASS（我逐条手算复现：band containment / +14.1%off-low−25.5%off-high / mcap 0.02% / dist-from-high 0.0pt / single-value-of-truth）；T6 guidance PASS(1d)；T6 active_litigation **WARN(58d>45d)** — 属 PASS 运行内的告警，Runner 已复核反垄断方向未变，**非 FAIL、非阻断**。

### Regime / Earnings 并入核验 ✓
- 任务点名的 regime（半导体崩 / CXMT / capex-audit / earnings）**确已并入 M4/M5**，非忽略：M5 finding 明列半导体 de-rate（7/15~$681→−13%，无利润池冲击）、AI-capex 审计轮出（META 站被轮出侧、正被集中定价的恰是 O4）、CXMT 二阶温和利多（不卖存储、或降未来 capex 元件价）、7/29 Q2+FOMC+Warsh 三事件同日；M4 载明 Q2 未出 / 锚沿用 Q1 / capex $125–145B（由 memory/networking 涨价驱动）；inversion_map 有专节、delta §3 有 regime overlay。
- **Earnings 诚实**：reported_q2=false 处理正确 — Q2-2026 于 **7/29 盘后**（as_of 之后一天）才发，锚沿用 Q1-2026，胜负手 O4 首读显式标「<24h away, UNKNOWN」→ **无 look-ahead 泄漏**（不假装已知 Q2）。

## FIX 清单
**无（0 项阻断）。** 以下为 non-blocking nits，不改裁定：
1. **market_cap 的第二源是 derived 恒等式**（2545×593.41），与 stockanalysis 同源略循环；但 INC-001 向量（price）本身真双独立源，market_cap 仅 price×shares → 可接受。（`freshness.json` market_cap 字段）
2. **完整度恰在 60% 边界**：卡按「60-80 下沿」取 STARTER 顶；严格读法 60% 属 40-60 的 WATCH 顶。因实际交付 WATCH，两种读法皆不超顶 → immaterial。（`valuation.md` §7 / `decision_card.md` ceiling 行）
3. **no-chase $640 vs buy-below $480 的判断带偏松**（$640 处 base IRR 已 ~+1.8%，远 <8%）；系 6/19 原样沿用（6/19 已 CLEAN），且方向保守（现价即已 WATCH/不买）→ 非错。（`decision_card.json` trim_or_no_chase_zone）

## 伪造引语 / 失配数字
**无。** 本轮 focused refresh **不含 ic_panel.md，全程无 IC 逐字引语** → 零伪造风险（6/19 IC 面板已由 6/19 checker 核为无伪造，本轮沿用）；runner_dissent 为 Runner 本人声音、非归名引语。独立重算 12+ 项数字全部 tie out，跨 10 文件价格/市值/IRR/公允价前后一致，无失配。

## 一句话
META 这轮**高度可信**：价格 $593.41 双源 0% 且非 52 周极值（INC-001 clear）、所有衍生数（mcap/P-E/FCF-yield/四情景 IRR/公允价/delta）逐项手算 tie out、freshness 机械门 PASS(exit 0)、verdict 被完整度正确封顶且实际诚实压到 WATCH、regime 与「Q2 未出」均如实并入而无 look-ahead、状态标签诚实标 DECISION_DRAFT(~60%)——是一份纪律到位、明确记录「META 是没变便宜的 Mega7 例外、O4 首读在 as_of 之后一天」的 REAFFIRM 决策草案，**CLEAN**。
