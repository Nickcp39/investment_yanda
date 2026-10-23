---
name: market-temp
description: 一键跑「市场体温」流水线（scripts/market_temp）：QQQ 位置、纳指四把周期尺子、25 个价格/估值/经济/流动性/黄金指标、GDP 基准线、定投 σ 通道、集中度，然后在本会话里补齐抓不到的数据并写近两周行情解释。用户说「跑一下市场体温」「QQQ 现在在哪 / 高不高 / 在水下吗」「更新一下体温」时使用。
---

# /market-temp

数值永远由 Python 算，AI 只做三件事：解释行情、补数据、写解读。**不要手改 temp.json / gauges.csv / history.csv / data/market_temp 里的任何数字。**

## 步骤

1. 跑流水线（有网就带抓取；用户说"用缓存"或网络不通时加 `--no-fetch`）：
   ```bash
   python scripts/market_temp/run.py
   ```
   stdout 最后 6 行是摘要；输出目录名在 `output/market_temp/LATEST.txt`。失败看该目录下 `run_log.txt`。
2. 读 `output/market_temp/<as_of>/temp.md`（一页结论、QQQ 位置、四把尺子、σ 通道、GDP 线、集中度、25 指标、和上一轮比、数据新鲜度）和 `needs_ai.json`。
3. AI 步骤，在本会话完成，写进 `output/market_temp/<as_of>/ai_notes.md`（中文，每个数字带来源 URL 和日期，不给买卖建议）：
   - **近两周美股为什么这样动**：WebSearch / WebFetch 查 Reuters、Bloomberg、WSJ、CNBC、FactSet、美联储/BLS 原文，3–5 条，每条一句话 + 来源 + 日期。
   - **数据补齐**：`needs_ai.json` 里每一项（常见：FRED M2 本机不可达、LBMA 403、stockanalysis 403）去官方或可靠来源找最新值，表格：数据项 | 最新值 | 数据日期 | 来源 | 备注。找不到写「未核实」。可以用内置浏览器。
   - **读数怎么读**：5–8 行，五组热度各说明什么，和 `history.csv` 上一行比变了什么，下次最该盯哪一项。结尾「以上是体温读数，不是建议。」
4. 回复用户 ≤ 12 行：QQQ 收盘与距最高、四把尺子（2000/2008/2015/2021 底起）偏离与时代分位、前瞻 PE 与 CAPE、五组热度与总热度、σ 通道位置、和上一轮比变了什么、数据缺口。决定是用户的。
5. 用户要 PDF 时：`python scripts/market_temp/run.py --no-fetch --pdf`（写到 `output/pdf/市场体温_<as_of>.pdf`）。要回看某天：`--as-of YYYY-MM-DD`（写到 `output/market_temp/_backfill/`，不动 LATEST 和 history）。

## 约定

- 带日期的输出目录是记录，不回头改；同一天重跑覆盖同一目录。
- `history.csv` 每个 as_of 一行，是我们自己的体温日志；画趋势时读它。
- 方法与 `backtests/市场体温_三节点_1980起_2026-10-11`、`QQQ_现在高不高_2026-10-08`、`QQQ_vs_GDP加CPI_锚点2010_2020_2026-10-12` 一致，细节见 `scripts/market_temp/README.md`。
