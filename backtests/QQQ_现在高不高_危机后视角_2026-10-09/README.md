# QQQ 现在高不高 · 危机后视角 · 2026-10-09

上一版 `QQQ_现在高不高_2026-10-08/` 用 1985 年以来的全部历史做基准。这一版按用户要求改成「每次经济危机结束、复苏开始之后」的样本：

- 时代 A：2002-10-07 起（互联网泡沫底之后）
- 时代 B：2009-03-09 起（金融危机底之后）

每个维度的趋势线、中位数、分位数都只用各自时代内的数据重算；2020-03 不单独成时代（5 个月收复，样本太短）。

## 成品

- PDF：`output/pdf/QQQ_现在高不高_危机后视角_2026-10-09.pdf`
- 图：`fig/01..09_era_*.png`（每维度一张，参考线按时代分别画）
- 数据：`stats_era.json`（全部数字）、`similar_episodes_by_era.csv`（高位之后的回报案例）、`report.md`

## 脚本链

```
python fetch_prices.py          # Yahoo 日线 → data/*_daily.csv；开盘中会剔除当日未收盘行
python build_era_charts.py      # → fig/*.png, stats_era.json, similar_episodes_by_era.csv
python build_era_report.py      # → report.md（数字全部从 stats_era.json 注入）
python ../../scripts/md_to_pdf.py report.md ../../output/pdf/QQQ_现在高不高_危机后视角_2026-10-09.pdf "QQQ 现在高不高 · 危机后视角 · 2026-10-09"
```

## 数据来源

- 价格：Yahoo Finance v8 chart API（QQQ/SPY 复权，^NDX/^GSPC 价格）
- 纳指100 前瞻/滚动 PE：historyofmarket.com `/api/ndx/forward-pe.json`（CC BY 4.0），复制自上一版 data/
- CAPE / S&P PE：multpl.com 月频，复制自上一版 data/
- M2 / CPI：复制自 `黄金_货币供应_估值_2026-08-07/data/`（至 2026-07；FRED 当晚不可达）

## 关键结论（截至 2026-10-08 收盘）

用 2009 起的尺子，价格偏离趋势 +12%，正好在本时代 90 分位线上；过去 5 年回报只有 31 分位；前瞻 PE 67 分位；科技相对大盘 +0%。用 2002 起的尺子，价格偏离 +36%，95 分位，接近 2021。两把尺子差一次 2008。CAPE 与 纳指100÷M2 在任何尺子下都是极端。
