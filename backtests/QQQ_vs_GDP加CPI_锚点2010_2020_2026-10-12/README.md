# QQQ / SPY vs「GDP + CPI」基准线 · 锚点 2010 与 2020 · 2026-10-12

基准 = 名义 GDP（≈ 实际 GDP + CPI）。从 2010-01-04 和 2020-01-02 出发，把名义 GDP 线画在资产自己的起点上，量资产跑在线上多远；再把超出部分拆成「盈利 ÷ GDP」和「市盈率」两项（价格 = GDP × 盈利/GDP × PE）。头部溢价 = 1990–2024 标普500 名义 EPS 年化 − 名义 GDP 年化 = 2.2pp。

- PDF：`output/pdf/QQQ_SPY_vs_GDP加CPI基准_锚点2010_2020_2026-10-12.pdf`（5 页）
- 数据：BEA gdplev.xlsx（季度到 2025Q1，之后按最近四季增速外推并标灰）、世界银行年度 GDP、BLS CPI-U、multpl 标普 PE（名义 EPS = 价格 ÷ PE；multpl 的 earnings 表是通胀调整值，不能直接用）、historyofmarket 纳指前瞻 PE、Yahoo（QQQ/SPY/RSP/IWM/VT 复权，^NDX ^GSPC ^W5000）
- 脚本：`fetch_prices.py` → `build_gdp.py`（fig/01–05、table_anchor_*.csv、stats_gdp.json）→ `build_report.py`（report_template.md → report.md）→ md_to_pdf
- 关键数（截至 2026-10-09）：2010 起名义 GDP 年化 4.8%，QQQ 超出 GDP 线 +753%（相当于 46 年 GDP 增长），SPY +321%，全市场 +201%；2020 起 QQQ +147%、SPY +80%。拆解：纳指 2010 起 ×16.4 = GDP ×2.19 × 盈利/GDP ×5.67 × PE ×1.24；2020 起 PE ×0.99。巴菲特指标 = 2010 的 3.0 倍、2020 的 1.6 倍。
