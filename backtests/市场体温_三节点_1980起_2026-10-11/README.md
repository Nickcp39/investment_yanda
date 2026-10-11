# 市场体温计 · 三节点与 1980 起 · 2026-10-11

问题：现在的经济与市场是过热还是过冷。把最大的几个盘子（标普500、纳指100、美债、黄金、CPI、M2、失业率）放在同一张表上：每个指标给 1980 起分位、三个节点（2008 / 2015 / 2021 周期）各自底部之后的分位，以及在三顶三底当天的读数。

## 成品
- PDF：`output/pdf/市场体温计_三节点_1980起_2026-10-11.pdf`（7 页）
- `gauges.csv`：25 个指标 × （现值、四个基准分位、三顶三底读数、热度）
- `stats_temp.json`：节点日期、各底部起的趋势线统计、黄金高点、分组热度
- `fig/01-07`：标普 1980 起 / 估值 / 纳指三节点趋势线 / 黄金 / 通胀与流动性 / 经济温度 / 体温计条形图

## 脚本链
```
python fetch_prices.py       # Yahoo：^GSPC ^SP500TR SPY ^NDX QQQ ^TNX ^IRX ^FVX ^VIX GC=F HG=F CL=F DX-Y.NYB
python fetch_macro.py        # BLS v1（CPI-U、失业率，10 年分段）；LBMA 黄金（403 则复制黄金批次缓存）；复制 M2 / CAPE / NDX 前瞻 PE
python build_temperature.py  # → fig/, gauges.csv, stats_temp.json
python build_report.py       # report_template.md（f-string 模板）→ report.md
python ../../scripts/md_to_pdf.py report.md ../../output/pdf/市场体温计_三节点_1980起_2026-10-11.pdf "市场体温计 · 三节点与 1980 起 · 2026-10-11"
```

## 数据注意
- FRED 本机不可达，失业率与 CPI 走 BLS 公开接口；M2 用黄金批次缓存（到 2026-07）。
- LBMA 当日 403，黄金用缓存到 2026-09-08，之后接 COMEX 近月 GC=F（接续日相差 <1%）。
- 报告模板放在 `report_template.md` 由脚本 eval：CPython 3.9 对超长 UTF-8 行会误报 "Non-UTF-8 code"，把长中文 f-string 放进 .py 会炸。
- NBER 衰退区间手工录入（1980、1981–82、1990–91、2001、2007–09、2020）。

## 一句话结论（截至 2026-10-09）
资产价格过热（价格组热度 82，黄金 81），估值偏热（70，CAPE 41.8 但相对 5.2% 的国债无溢价），经济晚周期偏热（69：失业率 4.2% 低但从 3.4% 回升，CPI 3.7% 再加速，曲线倒挂后转正），流动性中性（62）。没有一项过冷。价格偏离与 CAPE 都高于 2007 和 2021 两个顶。
