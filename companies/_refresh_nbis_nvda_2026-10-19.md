# 批次：NBIS + NVDA 抛售后重跑 · 2026-10-19

**pipeline** lean-6module-v1.1 · **as_of** 2026-10-16 收盘（10-19 盘中运行，不用当日未收盘价）· **基准** 两家各自的 2026-09-05 卡
**触发原因**：10-06 高点以来科技与芯片抛售（QQQ −6.6%，SMH −19%，NBIS −45%，NVDA −12%），持有人问「能不能买」。

## 一句话

两家的**价格条件都在本轮第一次满足**，两家的**证据条件都没满足**，裁决都是 WATCH 不动；两家的决定都压在下一份文件上：NBIS 的 Q3'26 6-K（日期未公告，去年 11-11），NVDA 的 Q3 FY27 现金流量表（约 11-18）。

| | NBIS | NVDA |
|---|---|---|
| 价格 | $165.47（−26.9% vs 09-05） | $214.13（−7.0%） |
| 带 | $150–180，**首次进带** | $148.30–222.44，**首次进带**（带顶下 3.7%） |
| 新一手证据 | 四份 6-K：$57.5 亿可转债（0.50% 2030 / 4.50% 2034，转股价 $313–325）、Palantir、Inferize、AGM | Q2 FY27 10-Q（XBRL+正文）、8-K 收购 Hugging Face $119 亿 |
| 本轮核心发现 | 杠杆分支从计划变成事实（$37.5 亿计划 → $57.5 亿落地），同业 CoreWeave 债券 79 美分；K-G 转红、K-VAL 转绿，红灯 1 个，不触发减仓 | OCF 只有 NI 的 40% 的原因是**应收账款单季 +$224 亿**（五个客户各占 ≥10%，账期 90 天到 1 年）+ 存货 +$58 亿；倒挂 = $77.7 亿股权投资收益（已确认）；供应承诺 $2,790 亿 |
| 模块 | 0/+1/+1/0/−2/+1，净 +1（前 −1） | +2/+1/+2/−1/−2/0，净 +2（前 +3） |
| new money / existing | **WATCH / HOLD** | **WATCH / HOLD** |
| STARTER 触发 | 价格 <$180 ✅ **且** 披露 active MW ❌（四个季度未披露，Q3 是第五次） | STEP 1 改写：Q3 OCF/NI ≥70% 或 AR/季收入回到 0.45–0.50，且无大客户计提；STEP 2 价格 ≤ $222.44 开 3–5% |
| freshness gate | PASS（T1–T6 全过） | PASS（T6 WARN：指引源 51 天，接受） |
| checker | CLEAN（self-checked） | CLEAN（self-checked） |

## 对持有人的直接含义（不是建议）

- 按 `trading-desk/discipline.md` §3.1，BUY 需要 verdict ≥ STARTER，两家都是 WATCH，**规则没触发**。「跌了很多」在那份文件里被明确列为非理由。
- 按 `trading-desk/risk_limits.md`，当前 T0，单票真金上限 **$500**。即使触发，量级也在这里。
- NBIS 现有仓位：HOLD，监控规则（两红减仓）未触发；Q3 发布当天重跑。
- NVDA：卡上第一次出现「会计口径 base IRR 过 8% 门槛」（8.8%），但现金口径仍为零；两者之差就是 Q3 要回答的应收账款问题。

## 本批次的缺口

- NBIS：Q3 未发布；2029/2031 旧可转债换股后剩余本金未核实；C110、C-NEW-ATM 未对到一手行项目；10-01 提价只有单一低知名度来源。
- NVDA：10-Q 的客户收入集中度与中国段落只经二手读到；$4 亿 H200 计提未在原文核到；五个 ≥10% 应收客户的名字未披露；CNBC 的 OpenAI 报道原文 403。
- 角色隔离：单代理自检，不是独立 Checker。

## 文件

`companies/nbis/2026-10-19/`、`companies/nvda/2026-10-19/`，各含 decision_card.md/json、facts.md、valuation.md、refresh_note.md、freshness.json、freshness_check.json/txt、model/scenario_model.csv、checker_report.md。
