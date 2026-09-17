# 复现说明

- `data/ff12.csv`, `data/ff_factors.csv`: Ken French Data Library (CRSP 2026-07), 12 行业月度收益 + 三因子/RF
- `data/eia_T07.01.csv` 等: EIA Monthly Energy Review 公开 CSV (`https://www.eia.gov/totalenergy/data/browser/csv.php?tbl=T07.01`), 年度值取 YYYYMM 末两位 = 13
- `data/yahoo_monthly.json`: Yahoo chart API 复权月线 (adjclose), 17 只
- `data/ff_eras.json`, `data/eia_summary.json`: 中间结果

核心表的算法(均在 `analyze.py`):
1. 时代年化 = ∏(1+r_m) 后按月数年化;市场 = Mkt-RF + RF
2. 需求 CAGR = (Gen_b / Gen_a)^(1/(b−a)) − 1,发电量取 ELETPUS(总)
3. 相关系数 = 8 个时代的 (发电量 CAGR, 公用事业年化 − 市场年化) 的 Pearson r
4. 回撤 = 含股息累计净值的峰谷
5. 个股时代收益 = 月末复权价比值年化
