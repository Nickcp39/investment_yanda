# NBIS Checker Report — mega7_2026-06-19 (LIGHT REFRESH as_of 2026-07-10)

裁定: **CLEAN**
真实状态标签: **DECISION_DRAFT** (完整度 ~70%, 非 COMPLETE — 措辞诚实, dossier 全程用 "LIGHT REFRESH / DECISION_DRAFT / warming", 无 "完成/full research complete" 越级用词)
verdict / size / ceiling: new-money **WATCH (0%)** / max ≤4% / ceiling = **STARTER (60–80% 完整度)** — **被完整度正确封顶: 是** (WATCH < STARTER 顶; size 未给 Core, 匹配 "周期/未确认" 耐久性)
数据新鲜度: **PASS** (`freshness_check.json`, exit 0) — 且 Checker 独立重抓复核 (下详)

---

## 数据新鲜度 (MECHANICAL 硬门) — 核心, 本轮 refresh 的全部意义

`freshness_check.json`: status=PASS, exit_code=0, validator=verify_freshness-v1, pipeline=lean-6module-v1.1.
- price card=219.65 vs refetched_yahoo=219.6499… → PASS; 2 独立源 (yahoo + websearch) 0.0% delta.
- 6 条 tripwire 全 PASS (T1 band / T2 low-high hug / T3 mcap identity / T4 distance-from-high / T5 single-value-of-truth), 1 条 WARN (T6 litigation 源 71d), 0 FAIL.

**Checker 独立重抓 (不信任 runner, 亲自验价 — INC-001 防线):**
用 PowerShell 直连 Yahoo chart API, 精确 timestamp→日期映射, 得 2026 年 6 月底–7 月中日收盘:
```
2026-06-30 276.17 | 07-01 229.18 | 07-02 215.62 | 07-07 195.19
2026-07-10 219.65 | 07-13 210.51 | 52wH 299.86 | 52wL 49.00
```
→ **2026-07-10 收盘 = $219.65, 与卡完全一致**; dossier 的整条价格路径 ($276.17 峰→07-01 掉→07-07 ~$195.19 谷→07-10 $219.65) 逐点对上原始数据。52wk band ($49.00 / $299.86) 亦对上。**INC-001 未重演** (NVDA 那次是 52 周低当现价; 本轮价格经独立源坐实无误)。
另: Yahoo regularMarketPrice 现 ~$176 (七月中当期报价), runner 在 `freshness.json` 明确区分 "as_of 收盘 ≠ 当期报价" 并拒用 stockanalysis $45.4B 当期市值 — 纪律正确。

## Gate 勾选
- **A Scope**: ✓ ticker/share-class/as_of=2026-07-10/决策目的/时间跨度 已冻结; 状态标签不 stale; refresh_of 指向 06-18。
- **B Evidence**: ✓ LIVE 字段各 ≥2 源 (freshness.json manifest); FILED 底座带自 06-18 claim_ledger; SENTIMENT (Meta-cloud / MU) 明确**未 promote 进 facts/EVIDENCE**, 只作 lead — 符合来源纪律 (KOL/传闻不直接支撑 BUY)。
- **C 11-Stage / IC**: ✓ (轻刷不重建; M1–M5 与八模块底座带自 06-18; 未新增五灵魂票据, 故**无新引语**可伪造)。
- **D Model & Math**: ✓ EV/forward-sales 三角 + implied-expectations 反推自**当前价 $219.65**; 三情景对账 (下 tie-out)。
- **E Open Questions**: ✓ blocking (active MW withheld) 显式封顶完整度~70%; non-blocking 分类清楚。
- **F Audit & Consistency**: ✓ 数字前后一致 (下); 版本戳完整; README/refresh_note 报真实状态。

## 数字对账 (@ $219.65) — 全部 tie out
- 市值 basic: 253.9M × 219.65 = **$55,769,135,000** = 卡 as_of_market_cap (精确到元)。✓
- 市值 diluted: 308.97M × 219.65 ≈ $67.87B ✓; EV basic = 55.77 − 0.85 净现 = **$54.92B** ✓
- Off 52wH: (219.65−299.86)/299.86 = **−26.7%** ✓; Off 52wL: (219.65−49)/49 = **+348.3%** ✓
- 跌幅: (219.65−286.69)/286.69 = **−23.4%** ✓
- EV/RPO: 54.92/33.585 = **1.64×** ✓; EV/Rev FY26E: 54.92/3.44 = **~16×** ✓; EV/ARR 现: 54.92/1.9 = **~28.9×** ✓; EV/ARR YE26-exit: 54.92/(7–9) = **6.1–7.8×** ✓
- STARTER gap: 距 $180 = −18% / 距 $150 = −32% (from-here framing, 一致) ✓

## 版本戳
`decision_card.json`: pipeline_version=**lean-6module-v1.1**, weights_version=**none**, run_date=**2026-07-10** → **合规** (v1.1/none/run_date 齐全, 卡不作废)。.md 头部同戳一致。

## 新财报是否真折入
NBIS **自身** Q2 2026 6-K **as_of 时未出** — dossier 正确声明 "无新 NBIS filed earnings", 未编造季度数。任务所指 "新财报" = **MU (Micron) Q3 FY2026 (~2026-06-24)** 作**资本周期 read-through** 真实折入: 见 facts.md §capital-cycle、freshness.json guidance、decision_card capital_cycle 块与 M5、sources_used SRC-MU-Q3FY26。结论方向正确 (HBM 售罄=上游高壁垒紧, **不** 缓解 NBIS 所处低壁垒出租段的供给信号)。✓ 且明确标为 read-through, 未越级当 NBIS 基本面。

## 伪造引语 / 失配数字
**无。** 未新增带引号的一手引语 (轻刷); runner_dissent 是 runner 自述推理非归因引语; 全部数值经独立重算与重抓核验, 无失配。

## 次要观察 (不构成 FIX-NEEDED)
1. `decision_card.json` 的 `buy_below_price=165` 是单值, 而叙述用带 **$150–180**; 165 为带中点, 自洽, 但单值与带并存需读者留意 (建议后续统一为 band 字段)。
2. T6 WARN: active_litigation 最新源 2026-04-30 (71d > 45d 阈)。属 WARN 非 FAIL, status 仍 PASS; Russia 尾部本就 "unchanged, low-med, 大多声誉性", runner 已声明本轮无新证券诉讼。可接受, 记录待下轮刷新时确认仍为最新权威事件。

## 一句话
**这轮可信到 "机械价格门真过、数字逐条对账、越级用词零、SENTIMENT 未污染 EVIDENCE" 的程度** — 价格 $219.65 经 Checker 独立重抓坐实 (INC-001 未重演), verdict 被完整度正确封顶为 WATCH(warming), 是一份诚实的 DECISION_DRAFT 轻刷。**CLEAN。**
