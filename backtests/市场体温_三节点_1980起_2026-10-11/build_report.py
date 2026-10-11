#!/usr/bin/env python
"""report.md from stats_temp.json + gauges.csv. Then md_to_pdf."""
import json, sys, numpy as np, pandas as pd
from pathlib import Path
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass
HERE = Path(__file__).resolve().parent
S = json.load(open(HERE/"stats_temp.json", encoding="utf-8")); G = pd.read_csv(HERE/"gauges.csv")
AS = S["as_of"]; L = S["levels"]; N = S["nodes"]; NE = S["ndx_eras"]; SE = S["spx_eras"]; GL = S["gold_levels"]; H = S["heat_by_group"]; GS = S["gold_splice"]
g = {r["指标"]: r for r in G.to_dict("records")}
PF = json.load(open(HERE/"panel_fits.json", encoding="utf-8"))


def frow(lab, era):
    r = PF[lab][era]; return f"| {lab} | {era} 底起 {r['start']} | P = {r['a']:,.0f} × {1+r['g']/100:.3f}^t | {r['g']:.1f}% | {r['dev']:+.0f}% | {r['pct']:.0f} | {r['implied']['3']:,.0f} / {r['implied']['5']:,.0f} |"


FROWS = chr(10).join(frow(lab, era) for lab in ("纳指100", "标普500", "黄金") for era in ("2000", "2008", "2015", "2021"))


def f(r, v):
    if v != v: return "—"
    return r["fmt"].format(v)


def row(name, cols=("现值", "分位 1980 起", "分位 2009 起", "分位 2016 起", "分位 2022 起", "2007 顶", "2015 顶", "2021 顶", "2009 底", "2016 底", "2022 底")):
    r = g[name]; out = [name.replace("（", "(").replace("）", ")")]
    for c in cols:
        v = r[c]
        if c.startswith("分位"): out.append("—" if v != v else f"{v:.0f}")
        else: out.append(f(r, v))
    return "| " + " | ".join(out) + " |"


def heat_word(h):
    return "过热" if h >= 85 else ("偏热" if h >= 65 else ("中性" if h >= 35 else ("偏冷" if h >= 15 else "过冷")))


def tbl(names):
    return "\n".join(row(n) for n in names)


HEAD = "| 指标 | 现值 | 1980 起分位 | 2009 起 | 2016 起 | 2022 起 | 2007 顶 | 2015 顶 | 2021 顶 | 2009 底 | 2016 底 | 2022 底 |\n|---|---|---|---|---|---|---|---|---|---|---|---|"
price = tbl(["标普500 偏离 1980 起趋势线", "标普500 相对 200 日均线", "标普500 过去 3 年价格回报", "标普500 过去 5 年总回报（1993 起）", "标普500 距历史最高", "纳指100 偏离 1985 起趋势线", "纳指100 相对 200 日均线", "QQQ 过去 3 年总回报"])
val = tbl(["标普500 CAPE", "标普500 滚动 PE", "标普500 盈利收益率 − 10 年国债（Fed 模型）", "纳指100 前瞻 PE（2001 起）"])
eco = tbl(["失业率", "Sahm 指标（3 月均值 − 12 月最低）", "CPI 同比", "收益率曲线 10 年 − 3 月", "实际短期利率（3 月国库券 − CPI 同比）", "10 年国债收益率"])
liq = tbl(["M2 同比", "VIX（1990 起）", "美元指数 DXY"])
gold = tbl(["黄金实际价格（按今日 CPI 折算）", "黄金 / 标普500 比值", "黄金过去 3 年回报", "黄金 / M2（美元每十亿美元 ×1000）"])
heat_rows = "\n".join(f"| {k} | {v:.0f} | {heat_word(v)} |" for k, v in sorted(H.items(), key=lambda x: -x[1]))
g80, gcape, gfed, gu, gcpi, gcv, grr, gt = (g[k] for k in ("标普500 偏离 1980 起趋势线", "标普500 CAPE", "标普500 盈利收益率 − 10 年国债（Fed 模型）", "失业率", "CPI 同比", "收益率曲线 10 年 − 3 月", "实际短期利率（3 月国库券 − CPI 同比）", "10 年国债收益率"))
gr, gg3, ggm, ggs = (g[k] for k in ("黄金实际价格（按今日 CPI 折算）", "黄金过去 3 年回报", "黄金 / M2（美元每十亿美元 ×1000）", "黄金 / 标普500 比值"))

tpl = open(HERE/"report_template.md", encoding="utf-8").read()
md = eval('f"""' + tpl + '"""')
open(HERE/"report.md", "w", encoding="utf-8").write(md); print("report.md written", len(md))
