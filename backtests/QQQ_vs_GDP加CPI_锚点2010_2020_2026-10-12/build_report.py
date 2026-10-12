#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""report.md from stats_gdp.json + table_anchor_*.csv via report_template.md (f-string template evaluated at runtime)."""
import json, sys, pandas as pd
from pathlib import Path
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass
HERE = Path(__file__).resolve().parent
S = json.load(open(HERE/"stats_gdp.json", encoding="utf-8"))
AS = S["as_of"]; G = S["gdp"]; PR = S["premium"]; DC = S["decomp"]; BF = S["buffett"]; A10 = S["anchor_2010"]; A20 = S["anchor_2020"]; TR20 = S["anchor_2020_trough"]
PREM = PR["1990-2024"]["premium"]


def tbl(k):
    T = pd.read_csv(HERE/f"table_anchor_{k}.csv")
    return "\n".join(f"| {r.资产} | {r.年化:.1f}% | {r.名义GDP年化:.1f}% | {r.超出GDP:+.1f} | ×{1+r.总涨幅/100:.2f} | ×{1+r.GDP线涨幅/100:.2f} | {r.累计超出GDP线:+.0f}% | {r.超出GDP加头部溢价线:+.0f}% | {r.相当于透支GDP年数:.0f} 年 |" for r in T.itertuples())


T10, T20 = tbl("2010"), tbl("2020")
row = {k: {r["资产"]: r for r in S[f"anchor_{k}"]["rows"]} for k in ("2010", "2020")}
q10, s10, w10 = row["2010"]["QQQ 含分红"], row["2010"]["SPY 含分红"], row["2010"]["全市场 Wilshire 5000"]
q20, s20, w20 = row["2020"]["QQQ 含分红"], row["2020"]["SPY 含分红"], row["2020"]["全市场 Wilshire 5000"]


def dec_rows(k):
    d = DC[k]; out = []
    for lab, m, pelab in (("标普500", "spx", "滚动 PE"), ("纳指100", "ndx", "前瞻 PE")):
        x = d[m]; out.append(f"| {lab} | ×{x['price']:.2f} | ×{x['gdp']:.2f} | ×{x['eps_over_gdp']:.2f} | ×{x['pe']:.2f}（{pelab} {x['pe0']:.1f} → {x['pe1']:.1f}） | ×{x['eps']:.2f} |")
    return "\n".join(out)


D10, D20 = dec_rows("2010"), dec_rows("2020")
prem_rows = "\n".join(f"| {k} | {v['eps_cagr']:.1f}% | {v['ngdp_cagr']:.1f}% | {v['premium']:+.1f} pp |" for k, v in PR.items())
tpl = open(HERE/"report_template.md", encoding="utf-8").read()
md = eval('f"""' + tpl + '"""')
open(HERE/"report.md", "w", encoding="utf-8", newline="\n").write(md); print("report.md written", len(md))
