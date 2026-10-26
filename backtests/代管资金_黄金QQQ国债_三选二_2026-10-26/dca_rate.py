#!/usr/bin/env python
"""Lump sum vs 3/6/12-month DCA for QQQ (and BRK.B), from starts that look like today (QQQ 5-12% below its high).
Weekly starts; DCA = equal monthly tranches, uninvested cash earns 0 (same convention as the 2026-10-11 study).
Metrics per horizon: median / p10 / worst total return on committed capital, share of starts where DCA beats lump,
worst interim drawdown measured against capital committed so far, and share still below cost after 1 year.
Outputs: dca_rate.csv, dca_rate.json"""
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass
HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
MT = REPO / "data" / "market_temp"
qqq = pd.read_csv(MT / "QQQ_daily.csv", parse_dates=["date"]).set_index("date").sort_index()["adj_close"]
brk = pd.read_csv(HERE / "data" / "BRKB_daily.csv", parse_dates=["date"]).set_index("date").sort_index()["adj_close"]
px_close = pd.read_csv(MT / "QQQ_daily.csv", parse_dates=["date"]).set_index("date").sort_index()["close"]
dd_from_high = px_close / px_close.cummax() - 1


def paths(p, start_i, months, horizon_days):
    """value path of 1 unit of capital: lump (months=0) or equal tranches every 21 trading days"""
    n = len(p)
    end = start_i + horizon_days
    if end >= n:
        return None
    if months == 0:
        shares = 1.0 / p.iloc[start_i]
        val = p.iloc[start_i:end + 1].values * shares
        committed = np.ones(end - start_i + 1)
    else:
        tranche = 1.0 / months
        shares = 0.0
        val = np.zeros(end - start_i + 1)
        committed = np.zeros(end - start_i + 1)
        cash = 1.0
        for j in range(end - start_i + 1):
            if j % 21 == 0 and j // 21 < months:
                shares += tranche / p.iloc[start_i + j]
                cash -= tranche
            val[j] = shares * p.iloc[start_i + j] + cash
            committed[j] = 1.0 - cash
    return val, committed


def run(p, label, starts, horizons=((1, 252), (3, 756), (5, 1260)), months_list=(0, 3, 6, 12)):
    rows = []
    for h_name, h in horizons:
        res = {m: [] for m in months_list}
        for i in starts:
            for m in months_list:
                r = paths(p, i, m, h)
                if r is None:
                    continue
                val, com = r
                # interim drawdown vs committed capital (what the holder sees as "loss" at the time)
                invested_dd = ((val - 1.0) / 1.0)  # vs total capital (cash counted at par)
                res[m].append(dict(ret=val[-1] - 1, min_interim=float(invested_dd.min()), below_cost_1y=float(val[min(252, h)] < 1.0)))
        lump = pd.DataFrame(res[0])
        for m in months_list:
            df = pd.DataFrame(res[m])
            rows.append(dict(标的=label, 期限=f"{h_name}y", 方式="一次性" if m == 0 else f"分 {m} 个月", 起点数=len(df), 中位回报=df.ret.median() * 100, p10回报=df.ret.quantile(.1) * 100,
                             最差回报=df.ret.min() * 100, 最深浮亏中位=df.min_interim.median() * 100, 最深浮亏最差=df.min_interim.min() * 100,
                             一年后仍亏概率=df.below_cost_1y.mean() * 100, 胜过一次性比例=float((df.ret.values > lump.ret.values).mean() * 100) if m else np.nan))
    return pd.DataFrame(rows)


weekly = np.arange(0, len(qqq), 5)
since09 = weekly[weekly >= qqq.index.searchsorted(pd.Timestamp("2009-03-09"))]
like_today = [i for i in since09 if -0.12 <= dd_from_high.iloc[i] <= -0.05]
all99 = weekly[weekly >= qqq.index.searchsorted(pd.Timestamp("1999-03-10"))]
T = []
T.append(run(qqq, "QQQ · 2009 起全部起点", since09).assign(样本="2009 起全部"))
T.append(run(qqq, "QQQ · 2009 起、起点距高 −5%~−12%（像今天）", like_today).assign(样本="像今天"))
T.append(run(qqq, "QQQ · 1999 起全部起点", all99).assign(样本="1999 起全部"))
bi = np.arange(0, len(brk), 5)
bi = bi[bi >= brk.index.searchsorted(pd.Timestamp("2009-03-09"))]
T.append(run(brk, "BRK.B · 2009 起全部起点", bi).assign(样本="BRK 2009 起"))
out = pd.concat(T, ignore_index=True)
out.to_csv(HERE / "dca_rate.csv", index=False, float_format="%.1f", encoding="utf-8-sig")
json.dump({"n_like_today": len(like_today), "like_today_dates_sample": [str(qqq.index[i].date()) for i in like_today[::20]], "as_of": str(qqq.index[-1].date())},
          open(HERE / "dca_rate.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
pd.set_option("display.width", 250)
print("like-today starts:", len(like_today), "e.g.", [str(qqq.index[i].date()) for i in like_today[::25]])
print(out.round(1).to_string(index=False))
