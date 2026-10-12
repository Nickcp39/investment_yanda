# 巨头市值占比 · 历史对照与过热标定 · 2026-10-12

问题：英伟达占市场多大比例，历史上的巨头顶峰时占多大，前十大与纳指100 的占比如何，能否作为过热标定。所有数字按口径分列（标普500 市值 / SPY 权重 / 纳指100 市值 / QQQ 权重 / 全美估算）。

- PDF：`output/pdf/巨头市值占比_历史对照_2026-10-12.pdf`（5 页）
- 现值：stockanalysis.com 成分市值列表与 ETF 持仓（2026-10-08/10），`data/sp500_mcaps.csv`、`ndx100_mcaps.csv`、`spy_holdings_top.csv`、`qqq_holdings_top.csv`；全美市值 = 标普500 合计 ÷ 0.82（假设）
- 历史：Apollo《The extreme weight of AI in the S&P 500》(2026-01, Bloomberg) 图读数 `data/apollo_largest_weight_by_year.csv`（PDF 在 data/）；GW&K《After the Peak》(2026-07)；CRSP/Morningstar；Finaeon《200 Years of Market Concentration》；Zweig/WSJ 经 Axios（AT&T 1932 约 13%）
- 脚本：`build_conc.py`（fig/01–04、stats_conc.json）→ `build_report.py`（report_template.md → report.md）→ md_to_pdf
- 关键数：英伟达 = 标普500 市值 7.3% / SPY 8.3% / 纳指100 市值 11.6% / QQQ 8.3% / 全美约 6%；标普口径 1981 起最高；全美口径低于 1932 AT&T 13%、1900 标准石油 9%。前十大：SPY 39.1%、标普市值 42.4%、CRSP 全美 37.7%（2025-10，超 1932）；QQQ 前十大 46.8%、纳指市值口径 69.1%。纳指100 ≈ 标普500 合计的 63%，占全美约 52%（代理序列 2000 顶约 43%）。
- 用户表中未核实项：GM 1955、IBM 1967、柯达 1972、思科 2000、微软 2024、标准石油 1929。
