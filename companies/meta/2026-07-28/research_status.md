# META Research Status — as_of 2026-07-28

最后更新: 2026-07-28（mega7_2026-07-28 现价重跑）· as_of=2026-07-28 · pipeline_version=lean-6module-v1 · weights_version=none
**诚实标签: DECISION_DRAFT（focused refresh，非 COMPLETE，非从零重研究）· completeness ~60%**

Decision question: 在 $593.41、且 Q2-2026 财报（7/29 盘后）+ FOMC 双二元事件前一天、在"AI capex 审计"regime 里，META 对新钱/存量各该怎么办？

Current stage: **现价重跑完成 → Decision Card 锁定（2026-07-28）**

**Verdict = WATCH（新钱 initial 0% / buy-below ~$480 / max ~5% if entered）· existing HOLD · ceiling STARTER（完整度封顶）· 价格 + 事件风险压实际 verdict 到 WATCH**

> 这是**决策草案（DECISION_DRAFT）**，不是 COMPLETE。业务基线（M2/M3）沿用 6/19 快速复核；M4/M5/M6 用现价 + 当前 regime 重算。O4（capex ROI）仍是 blocking 胜负手，且其首次读数在 as_of 之后一天（7/29）。

---

## 本轮做了什么（focused refresh 范围）
| 项 | 状态 | 说明 |
|---|---|---|
| 现价重抓 + 交叉验证 | ✅ | Yahoo chart API $593.41（2026-07-28 收盘）= stockanalysis.com $593.41，0.0% delta；非 52 周极值贴合 |
| M2/M3 thesis-break 复核 | ✅ | 无破裂，沿用 6/19（广告满血、护城河耐久、操作者 3/5）|
| M4 Q2-2026 财报并入 | ⚠️ **N/A — 未披露** | META 2026-07-29 盘后才发；锚沿用 Q1-2026；Q2 共识 rev ~$60.2B/EPS ~$7.18 仅作 M2/M5 语境 |
| M5 regime 叠加 | ✅ | 半导体崩 / capex 审计 / CXMT / FOMC 打到 META 的具体读数 |
| M6 现价重估 | ✅ | base IRR +3.4% < 8%；buy-below ~$480；价格带刷新 |
| 两轴 verdict 重导 | ✅ | new_money WATCH / existing HOLD |
| freshness.json | ✅ | 每 LIVE 字段 ≥2 独立源 |
| verify_freshness.py | ⏳ | 见下"freshness_check"状态 |

## Final Verdict 摘要
**WATCH · 新钱 0% / buy-below ~$480 / max ~5% · 好生意 + 价格没变便宜（略贵）+ owner-earnings 锚未决 + 关键财报在 as_of 之后一天。**

- 广告引擎满血（Q2 共识 +27%），生意质量不是问题。
- 但 owner earnings 仍被 capex 吃（FCF yield ~3.3%）；Q2 未出 → 锚沿用 Q1-2026。
- 现价 $593.41 比 6/19 的 $577.22 **高 +2.8%**（非像别家变便宜）→ base IRR +3.4% < 8%，高出保守公允价 ~24% → **价格仍是 binding constraint，且略紧**。
- regime（AI capex 审计）正集中定价 META 的未决 O4；Q2 财报 + FOMC 同在 7/29（as_of 之后一天）→ 新钱事件前建仓 = 差风险回报。
- 完整度 ~60% 封 ceiling 在 STARTER；价格 + 事件把实际 verdict 压到 WATCH。

## freshness_check 状态 = **PASS（exit 0）**
- 已生成 `freshness.json`（LIVE manifest，price/market_cap/52wk/shares + active_litigation + guidance，各 ≥2 源）。
- 已跑 `python scripts/verify_freshness.py --dossier companies/meta/2026-07-28` → **status=PASS, exit 0**（`freshness_check.json` / `.txt` 已落盘）。
- T1–T5 全 PASS：价格独立重抓 593.41 = 卡值（0% delta，Yahoo + stockanalysis 双源）；非 52 周极值贴合（+14.1% off low / −25.5% off high）；市值恒等 0.02%；single-value-of-truth 通过。
- T6 guidance PASS（1d）；T6 active_litigation WARN（58d，非阻断，反垄断状态已复核方向未变）。

## 升 verdict / 解封顶路径
①价格回撤到 ~$480（base 8% 门槛）→ STARTER-eligible；②**7/29 Q2 印证 capex 复利**（营业利润率在高 capex 下扩张）→ 上修锚、base ~+10% → STARTER-eligible（解 blocking O4）；③10-K 逐行(O1) + proxy(O3) + RL 全年(O2) 补齐 → 完整度 >80%，配合价格可评更高 verdict。

## 与 6/19 的差异
见 `delta_vs_0619.md`：价格 +2.8%（MOS 未改善反略差）、Q2 未披露（锚沿用）、regime 叠加（净风险 + 一个 CXMT 二阶小正项）、反垄断方向未变。verdict WATCH/HOLD **维持不变（REAFFIRM）**。

## OPEN gate（封顶完整度）
**O4 capex ROI 定量（blocking 胜负手，7/29 读数）**· O1 10-K 逐行 · O2 RL 全年 · O3 proxy 精确持股/薪酬 · O5 Llama/生成式货币化 · O6 OBBBA 持续税率 · **[本轮新增] Q2-2026 实际数（7/29 盘后，as_of 之后一天）未并入**。
