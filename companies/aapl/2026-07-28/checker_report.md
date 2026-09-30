# AAPL Checker Report — mega7_2026-07-28
（ruleset: `companies/_mega7_2026-06-19/CHECKER.md` · Checker 独立于 Runner）

裁定: **CLEAN**

真实状态标签: **DECISION_DRAFT（~55% 完整度）** — 诚实，未 overclaim COMPLETE。`research_status.md` 明写"诚实标签：DECISION_DRAFT……不是 COMPLETE"，与 `decision_card.md`(status=DECISION_DRAFT)、`decision_card.json` 一致。

verdict / size / ceiling: 新钱 **WATCH** / 存量 **HOLD** / business **exceptional**；init 0% · max 15%（条件于价格 ≤$210）。 ← 是否被完整度正确封顶: **是**。完整度 ~55% → 上限 WATCH（40–60% 档），new_money=WATCH 恰在顶、未超。且卡明示真正 binding 的是价格门（M6 −2），完整度封顶与价格封顶双重落在 WATCH。size 与耐久性匹配：耐久性 HIGH/非周期，现价 init=0%，无"周期/未确认给 Core 级 size"违规。

数据新鲜度: **PASS**（`freshness_check.json` status=PASS, exit_code 0）。
- `verify_freshness.py` 独立重抓 Yahoo = 340.0799865722656，3 独立源(yahoo/stockanalysis/websearch) pairwise 0.0% delta。
- Tripwires: T1 band PASS(201.5≤340.08≤342.89) · T2 low/high hug PASS(+68.8% off low, −0.8% off high) · T3 mktcap identity PASS(14726M×340.08=5.008T=卡值) · T4 SKIP · T5 single-value-of-truth PASS · T6[guidance] PASS。
- 唯一 T6[active_litigation] = **WARN**（Google TAC 源 2026-06-01，57d>45d）。这是 WARN 非 FAILURE（failures=[]），dossier 已诚实标注"carried, confirm still latest"→ **非阻断**，机械门仍 PASS。

价格完整性（独立复核）: **PASS**。
- Checker 独立走 Yahoo chart API 重抓：regularMarketPrice=**340.08**、52wk hi=**342.89**、52wk lo=**201.5**、prevClose 336.91 — 与卡逐项精确吻合。
- **不是 INC-001**。INC-001 是把 52 周**低**塞进现价槽伪造便宜(向下推导错)→ 翻出错误 BUY。本案是真实、live、3 源坐实的 52 周**高**hug（−0.8% off 盘中高 342.89 / = 收盘高），$5T 里程碑为可查事件；"错"的方向是保守而非虚高，且 verdict 正确反映"贵"(WATCH/no-chase/base IRR~0%)。卡的 INC-001 guard 注 + freshness `low_high_hug_justified=true` 处理得当。
- 衍生数内部自洽（Checker 重算逐项对上）：mktcap $5.008T、P/OE 41.7x、OE yield 2.40%、P/FCF 38.8x、净现金/市值 1.24%、vs$231 +47%、vs$210 +62%、价格 Δ +14.1%、6/19 mktcap $4.39T、base 5y IRR ≈0.0%（终值 339.5 / 现价 340.08）。全部 tie out。
- Delta vs 6/19 已对照真实 `companies/aapl/2026-06-19/decision_card.json` 核验：as_of 298.01 / WATCH / HOLD / buy_below 231 / max 15 / exceptional，全部与 delta 叙述一致；6/19 binding_constraint 亦坐实 ~36x→41.7x、2.7%→2.40%、完整度 ~60%→~55%。

Gate 勾选: A ✓ / B ✓* / C ✓* / D ✓ / E ✓ / F ✓
- A Scope: ticker/share class/as_of=2026-07-28/决策目的/时间跨度冻结；焦点刷新范围明写；状态标签不 stale。✓
- B Evidence: `sources_used` S001–S014 带 date/tier/id；载荷一手数 carry 自 6/19 一手源；价格 3 源。*注:焦点刷新沿用 6/19 的 `source_register.md`/`claim_ledger.csv`，7/28 目录未重建证据台账——此为 focused-refresh 设计,配 DECISION_DRAFT/~55% 且未称 COMPLETE,可接受。
- C 覆盖: M1–M6 各有产物(decision_card/valuation/inversion_map/delta)。*Stage 8 五灵魂 IC panel 未在本刷新重跑(carry 自 6/19 `ic_panel.md`);以 chair-voice `runner_dissent` 代之——未称 COMPLETE,scope 内可接受。
- D Model & Math: OE 桥 carry；implied expectations 从**现价 $340.08** 反推；三情景与假设对账；公式可审计且内部一致(已重算)。✓
- E Open Questions: O1–O8 分类，价格门显式封顶 verdict，完整度显式封顶；O3 关闭有据。✓
- F Audit: 数字前后一致；版本戳 pipeline=lean-6module-v1 / weights=none / run_date=2026-07-28(合规)；诚实报状态；T6 WARN 已如实上浮。✓

FIX 清单: **无阻断项**。仅非阻断提示（不改裁定）：
1) `freshness_check.json` T6 WARN — `active_litigation`(Google TAC)源 57d 陈旧。已诚实标注,非阻断;下轮或 escalate 前建议重确认仍是最新事件(`freshness.json` active_litigation 字段)。
2) 版本标签细节: `decision_card.json` pipeline_version="lean-6module-v1",而 `freshness.json` note 自称跑的是"lean-6module-v1.1 freshness gate"。纯标签口径差异,v1 在允许清单内且 v1.1 新鲜度机械门确已跑并 PASS——非缺陷。
3) 锚定季度 Q2 FY26(ended 2026-03-28)较 as_of 已 4 个月;6 月季(fiscal Q3 FY26)7/30 才出(as_of 后 2 天),共识仅作估计未入 OE(O7)。卡已把 M1/M4 信心降 MED、完整度 60%→55% 反映之——处理诚实。

伪造引语/失配数字: **无**。未见伪造五灵魂 IC 引语(grep 无命中);`runner_dissent` 的"Duan 让 AAPL 到 ~60%"、"2016 SEVERE-UNDERSIZE"为事实性释义/回测引用,非伪造带假出处的引号。无失配数字(全部重算对上)。regime(半导体暴跌/CXMT/capex 审计/FOMC-Warsh/7·30 财报)确已并入 M4(capex-light=相对强项)与 M5(F1–F8 逐条叠 regime),非被忽略。

一句话: **可信度高**——价格由 Checker 独立 Yahoo 复核精确坐实(贴 52 周高但属真实 justified,非 INC-001 误锚),机械新鲜度门 PASS,verdict 被完整度+价格双重正确封至 WATCH,size 与 HIGH 耐久性匹配,标签诚实(DECISION_DRAFT ~55%,不称 COMPLETE),无伪造/失配,regime 已实质并入;唯一 T6 active_litigation 57d WARN 为非阻断且已诚实上浮。裁定 **CLEAN**。
