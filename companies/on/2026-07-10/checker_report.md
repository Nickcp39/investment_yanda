# ON Checker Report — mega7_2026-06-19

裁定: **CLEAN**
真实状态标签: **DECISION_DRAFT** (诚实；一次严谨 Runner pass，本报告即所缺的独立 Checker；O1/O2/O5 open，未标 COMPLETE)
verdict / size / ceiling: new money **WATCH** · existing **HOLD** · size 0% now (STARTER 3–5% 仅在 ~$65–72) · 完整度 ~63% → ceiling **STARTER**  ← 是否被完整度正确封顶: **是**（WATCH 在 STARTER 顶之下；实际 verdict 由 price + thesis-stage 再压，非完整度压）
数据新鲜度: **PASS**（freshness_check.json status==PASS, exit 0）  ← 有 PASS 产物
Gate 勾选: A✓ / B✓ / C✓ / D✓ / E✓ / F✓ （无未过项）

## 独立复核（不信任 Runner，实测）
- **价格独立重抓**: Yahoo chart API 实测 `regularMarketPrice=95.96`, `fiftyTwoWeekHigh=134.92`, `fiftyTwoWeekLow=44.56` — 与 dossier **penny-identical**。第二源 stockanalysis (S006) 亦 95.96。≥2 独立源一致 <1%。✓
- **市值恒等**: 389.19M × 95.96 = $37.35B ≈ card $37.34B（<0.05% 误差）。✓
- **52 周位置**: +115.3% off low、−28.9% off high — 叙述与算术一致。✓
- **版本戳**: decision_card.json = `lean-6module-v1.1` / weights `none` / run_date `2026-07-10`。✓
- **跨文件对账**: $95.96、$37.34B、net debt −$603M、Q1'26 rev $1,513.3M、GM 38.5%、EPS $0.64、FCF $217.2M 在 facts/valuation/decision_card/memo/claim_ledger 前后一致。✓
- **裸 claim / 来源纪律**: memo 每条挂 fact/source_id 或 OPEN；KOL 视频 S011(D1) 仅作 batch lead，未进 facts、未支撑 verdict；AI-DC $ 与 robotics design-win 明确标 B2-relayed INTERPRETATION(O2)，未冒充 EVIDENCE。✓
- **IC panel 引语**: 顶部明示"无伪造引语；lens/释义，非直接引用"；五灵魂(段/巴菲特/芒格/Marks/Klarman)均为框架释义。**无伪造投资者引语**。✓

## 批次 THESIS 诚实性（本批核心）
- **robotics_revenue_pct ≈ 0%**（de minimis；design-win/demo only，O3 blocking 明文记录"无 dated robotics revenue/orders/units"）— **有据非手挥**。
- **demand = ANTICIPATION** — 证据支撑：真实 dated 现金只在 auto($797M)、industrial、AI-DC POWER($250M'25→$500M'26E)；robotics 现金为零。
- **CAPITAL_CYCLE 已对 robotics 段施加**: applicable=no(robotics)/partial(core)；stage = demand trough→early，**valuation late**；supply_barrier low-med；caution **PEAK-lean(valuation)**，+115% off low = 共识非底部入场。诚实。
- **real_bottleneck = CONCEPT/commodity**（robotics）：38.5% GM + 4 rivals + 无 switching cost 证伪定价瓶颈；核心 auto/industrial = REAL 但 MED + cyclical，非垄断定价。justified。
- **option-value vs core-value split 已做**: $95.96 买的 ~92% 是已 re-rate 的周期复苏 + 小 AI-DC-power ramp + ~$0-cash robotics 期权。

## FIX 清单
无（可选清理，不影响裁定）:
1) S007 buyback 日期跨文件轻微不一（source_register "2025-10 approx" vs sources_used "2026" vs facts "2026–2028"）— cosmetic，非 load-bearing。
2) freshness 一条 T6 WARN：guidance 源 2026-05-04 距今 67d(>45d)。合理——Q1 财报电话即最新权威事件，下次财报约 8 月；WARN 不 block，status 仍 PASS。建议在 monitor 标注"待 Q2 财报刷新"。

伪造引语/失配数字: **无**。价格双源实测一致；市值/52 周/段位算术自洽；IC 引语标注为释义。
一句话: **这轮可信度高——载重数字全 primary 且双源实测对得上，freshness 机械门真过，批次 robotics 论点诚实地把 onsemi 判成"披机器人外衣的周期股、机器人现金≈0"，verdict WATCH 未越顶、未被叙事绑架；CLEAN。**
