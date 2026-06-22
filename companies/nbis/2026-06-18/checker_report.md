# NBIS Checker Report — lean-6module-v1.1 (as_of 2026-06-18)

裁定: **CLEAN**

真实状态标签: **DECISION_DRAFT** （research_status / memo-v1 / decision_card / audit / completion_checker 五处一致；显式声明 "本轮 ~70%、非 COMPLETE"，并诚实区分"新钱 WATCH（价格）vs 存量 HOLD（生意更好）"——语言诚实，无 "COMPLETE/建仓" 越级措辞）

verdict / size / ceiling: **新钱 WATCH（buy-below ~$150–180）/ 存量 HOLD** · 新钱初始 0% · 上限暂封 ≤4%（仅在价格 de-rate + active MW 证明转化后讨论）· **ceiling = 价格无安全边际（主）+ 完整度 ~70%（次，active MW 缺口）**
← 是否被正确封顶: **是**。价格端 $286.69 无 MOS（EV ≈ 2.1× 全部 RPO、≈ 9× YE26 exit-ARR 当兑现、bear −50%+）→ 新钱不可越过 WATCH 上 STARTER；完整度 ~70% + active MW（O-A）缺口独立堵 STARTER。verdict = WATCH，**未越顶**（既未给新钱 STARTER，也未把存量打到 EXIT/TRIM-on-price——存量 HOLD 反映生意被一手验证更好，逻辑自洽且与 MSFT 案镜像清晰）。size 与耐久性匹配：新钱 0%、上限 ≤4%，未在 active MW 未证明 + 负 FCF + 控股治理下给 Starter/Core 级 size，合规。

## Gate 勾选: A✓ / B✓ / C✓ / D✓ / E✓ / F✓ （独立复核全过；下列为已验证项与轻微观察）

- **A. Scope & Definition** ✓ — ticker/报告基准(20-F/6-K, 无 10-Q)/as_of=2026-06-18/决策目的(LEAD 电力瓶颈 + 存量仓位 + 新钱)/十年跨度 已冻结；完成标准先于结论写下；状态标签不 stale（旧单视频 brief `../../nbis.md` 标 C 级对照）。
- **B. Evidence** ✓ — source_register 含每个 memo/model 用到的来源(21 源)；claim_ledger.csv 51 行带 source_id + tier；facts.md 只收 verified 行 + 显式 LIVE 快照。**来源纪律已守**：RPO $33.6B（审计口径）与"$46–50B backlog"（媒体=合同上限和）明确区分；capex $20–25B（电话会 B1）vs $31–35B（二手）正确标 OPEN，FCF 一律用已报 OCF−capex 口径（≈ −$3.66B），未用未确认 capex 算 FCF。KOL（旧 nbis.md）只进对照/SENTIMENT，未支撑结论。**LIVE 数据入 freshness.json ≥2 源，verify_freshness.py PASS**。
- **C. 10-Layer 覆盖** ✓ — 8 模块产物齐全（business/value_chain/moat/bottleneck/operator/inversion/financial_quality/valuation）；Stage 8 IC Panel 存在，五灵魂（段永平主审 + Buffett/Munger/Marks/Klarman）各出票 + 一轮 critique（含 steelman-the-bull）。
- **D. Model & Math** ✓ — owner-earnings DCF **显式判定不可用**（FCF 负至 ≥2028），改 EV/forward-sales 三情景 + implied-expectations，理由写明；implied expectations 从 $286.69 反推；三情景与假设/来源对账，公式可审计（标注忽略后续稀释 → bear/base 实际更低）。
- **E. Open Questions** ✓ — O-A（active MW）/O-B（集中度 %）/O-C（FY26 capex）/O-D（Russia indemnity）分类清楚；**O-A 显式封顶（blocking STARTER）**，O-B/O-C/O-D 标 monitoring/non-blocking 并给不封顶理由。
- **F. Audit & Consistency** ✓ — decision_card.json schema 完整且**版本戳 = lean-6module-v1.1 / none / run_date 2026-06-21**（已戳，卡有效可比）；数字前后一致（见下）。

## 独立验证结果（不只信 Runner — 手算复核）

1. **数字对账 — 全部 tie out**：
   - market_cap (basic) = 286.69 × 253.9M = **$72,790,591,000 ≈ $72.79B** ✓（json `as_of_market_cap` 72790591000 一致；freshness T3 复核 0.00%）
   - market_cap (diluted) = 286.69 × 308.97M = **$88.58B** ✓
   - EV (basic, carry 净现金 +$0.85B) = **~$71.9B** ✓
   - **EV/RPO** = 71.9 / 33.585 = **~2.1×** ✓（card 写 ~2.2×，差异来自 EV 取 71.9 vs 72.5；同一量级，已在容差内，建议口径统一见 FIX-1）
   - **EV / YE26 exit-ARR** = 71.9 / (7–9) = **~8.0–10.3×** ✓（card "8–10×" 一致）
   - **capex/rev FY25** = 4,066 / 529.8 = **~7.7×** ✓
   - **距 52wH** = 286.69/298.80 − 1 = **−4.05%** ✓（freshness T4 narrative −4.0% vs card-implied −4.1%，gap 0.1pt，PASS）
   - **持有人 gain** = 286.69/192.5 − 1 = **+48.9% ≈ "+50%"** ✓
   - as_of_price **$286.69** 在 decision_card.json / .md / valuation.md / facts.md / model/scenario_model.csv **五处完全一致**（freshness T5 PASS），无失配。
2. **价格新鲜度 — 独立核验**：verify_freshness.py 独立重抓 Yahoo last-close ≤ 2026-06-18 = **286.69**（card 286.69，delta 0.0%）；3 独立源（yahoo + stockanalysis + websearch）一致。**关键点**：$286.69 在 52wk 高位（−4% 距 intraday ATH $298.80，且 = adjclose 52wk high）→ T2 low/high-hug 会触发,但 `low_high_hug_justified=true` 已声明且**理由成立**（"priced for perfection 近高点正是论点"——这是新钱 WATCH 的驱动,不是 INC-001 式抓错极值）。**与 INC-001(NVDA 抓成 52wk 低)相反方向,且这次是有意的高位读数 + 三源核验**,非数据错误。
3. **伪造引语检查 — 无**：抽查 ic_panel §1.2 Munger 的 "Show me the incentive and I will show you the outcome" / "Invert, always invert" / "EBITDA = bullshit earnings" 挖苦 — 均为 Munger 公开反复表述的真实立场；Buffett owner-earnings(1986 股东信)/"price is what you pay…" / Marks second-level thinking & "forward but with caution" / Klarman《Margin of Safety》"先看下行" — 均标注为 lens/公开立场释义。panel §0 纪律明确声明"凡引用均为公开著作/股东信/备忘录里反复表述的立场,不放进引号假装逐字原话",**无杜撰具体名言**。
4. **来源真实性 / 时效**：FY2025 20-F（CIK 0001513845，foreign private issuer）、Q1'26 6-K 股东信（2026-05-13）、MSFT 合同 6-K ex-99.1（2025-09-08）均为 NBIS 正确主源；RPO $33,585M、contracted power >3.5GW、active ~170MW YE2025、MSFT up to $17.4→19.4B、Meta ~$2.88B+~$27B 与 facts/claim_ledger 一致。Q1'26 6-K（报 2026-05-13）是 as_of 当下最新季度披露；价格 2026-06-18 收盘为最新交易日；无过期数字被当"当前"。

## 数据新鲜度门 (freshness gate)
- `freshness.json` + `freshness_check.json` 存在；`verify_freshness.py --dossier companies/nbis/2026-06-18` → **STATUS PASS (exit 0)**。
- price 三源核验 0.0% delta；T1 band ✓ / T2 hug ✓(justified)/ T3 mcap-identity ✓(0.00%)/ T4 dist-from-high ✓(gap 0.1pt)/ T5 single-value-of-truth ✓。
- 唯一 WARN：T6 `active_litigation` newest source 2026-04-30 = 49d（>45d）——**WARN 级、非阻断**（Russia/20-F 事件本就低频；已确认是当下最新 authoritative 状态，无更新事件）。`guidance` PASS（36d）。

## FIX 清单
（无强制 FIX。以下为非阻断的轻微观察，不影响 CLEAN 裁定）
1. **轻微/口径** — EV 在 valuation.md 写 ~$72.5B（@ ~$288 旧 intraday）而重算 @ $286.69 为 ~$71.9B；EV/RPO 因此 card 写 ~2.2× vs 重算 ~2.1×。同一量级、结论不变，建议下一轮把 EV 全文统一到 $71.9B @ $286.69 口径以消除 0.6B 残差。
2. **轻微/已自披露** — active MW（O-A）是公司 withhold 的关键转化指标；Runner 已在 facts/inversion/monitor/audit/ic_panel 多处显式标 blocking 并据此封顶，处理透明，无需修，仅作风险登记（盯 Q2'26 6-K ~Aug）。
3. **轻微** — `source_register.md` 仍含 SRC-099（旧单视频 brief）；已正确标 C 级 + "NOT a fact source" 且未被任何 load-bearing claim 引用，不构成裸 claim；保留作对照可。

## 伪造引语 / 失配数字: **无**
- 投资人引语：无杜撰，均标注为 paraphrase/公开立场/lens。
- 数字：as_of_price / market_cap / EV / 各倍数 / 距高点 / 持有 gain 跨 5 文件一致，且手算 tie out。

## 一句话
这家这轮**可信度高**：一手底座扎实（FY2025 20-F + Q1'26 6-K + MSFT 合同），数字跨文件且手算全部 tie out，无裸 claim、无伪造引语、版本戳齐全，**freshness gate PASS（价格三源核验、高位读数已正当 justify）**，verdict（新钱 WATCH / 存量 HOLD）被**价格无安全边际（主）+ 完整度（次）**正确封顶且 Runner 诚实自承非 COMPLETE，并与 MSFT 案（完整度封顶、价格有正 MOS）形成干净的镜像对照 — 是一份诚实、可比、未夸大的 DECISION_DRAFT。**CLEAN。**
