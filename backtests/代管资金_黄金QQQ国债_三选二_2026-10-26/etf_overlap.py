#!/usr/bin/env python
"""BRK.B / QQQ / SPY / VOO: how much do they overlap, and does holding all of them add anything over holding one?
Data: Yahoo v8 (BRK-B 1996-, VOO 2010-, BRK-A for market cap), SPY/QQQ from data/market_temp, holdings from data/market_temp.
Outputs: data/*.csv, etf_overlap.json, fig/05_etf_overlap.png"""
import csv
import datetime as dt
import json
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass
HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
MT = REPO / "data" / "market_temp"
D = HERE / "data"
D.mkdir(exist_ok=True)
F = HERE / "fig"
plt.rcParams.update({"font.family": ["Microsoft YaHei", "SimHei"], "axes.unicode_minus": False, "figure.dpi": 150, "axes.grid": True, "grid.alpha": .3,
                     "axes.spines.top": False, "axes.spines.right": False, "font.size": 9, "legend.fontsize": 8, "axes.titlesize": 10.5})
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36", "Accept": "text/html,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.9"}
BRK_CASH_BN, BRK_SECURITIES_BN, BRK_ASOF = 359.2, 340.8, "2026-06-30"   # 10-Q Q2 2026: cash+T-bills (insurance & other); equity + fixed maturity securities


def yahoo(sym):
    p2 = int((dt.datetime.utcnow() + dt.timedelta(days=2)).timestamp())
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{urllib.parse.quote(sym)}?period1=0&period2={p2}&interval=1d&events=div%2Csplits&includeAdjustedClose=true"
    js = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
    res = js["chart"]["result"][0]
    ts, q, adj = res["timestamp"], res["indicators"]["quote"][0]["close"], res["indicators"]["adjclose"][0]["adjclose"]
    meta = res["meta"]
    reg = meta.get("currentTradingPeriod", {}).get("regular", {})
    if meta.get("regularMarketTime", 0) < reg.get("end", 0) and ts and ts[-1] >= reg.get("start", 10**12):
        ts, q, adj = ts[:-1], q[:-1], adj[:-1]
    rows = [(dt.datetime.utcfromtimestamp(t).date().isoformat(), float(c), float(a)) for t, c, a in zip(ts, q, adj) if c is not None and a is not None]
    with (D / f"{sym.replace('-', '')}_daily.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["date", "close", "adj_close"])
        w.writerows(rows)
    s = pd.DataFrame(rows, columns=["date", "close", "adj_close"])
    s["date"] = pd.to_datetime(s["date"])
    return s.set_index("date")


brkb, voo, brka = yahoo("BRK-B"), yahoo("VOO"), yahoo("BRK-A")
spy = pd.read_csv(MT / "SPY_daily.csv", parse_dates=["date"]).set_index("date")
qqq = pd.read_csv(MT / "QQQ_daily.csv", parse_dates=["date"]).set_index("date")
AS_OF = str(qqq.index[-1].date())


def m(df):
    s = df["adj_close"].resample("MS").first().dropna()
    s.index = s.index.normalize()
    return s


A = pd.DataFrame({"SPY": m(spy), "QQQ": m(qqq), "BRK.B": m(brkb)}).dropna()
A = A[A.index >= "1999-04-01"]
R = A.pct_change().dropna()
S = {"as_of": AS_OF, "sample_3": f"{A.index[0].date()}→{A.index[-1].date()}"}
S["corr_monthly"] = R.corr().round(2).to_dict()
b = np.polyfit(R["SPY"], R["QQQ"], 1)
S["qqq_beta_on_spy"] = float(b[0])
S["qqq_r2_on_spy"] = float(np.corrcoef(R["SPY"], R["QQQ"])[0, 1] ** 2)
b2 = np.polyfit(R["SPY"], R["BRK.B"], 1)
S["brk_beta_on_spy"] = float(b2[0])
S["brk_r2_on_spy"] = float(np.corrcoef(R["SPY"], R["BRK.B"])[0, 1] ** 2)

MIX = {"SPY": {"SPY": 1}, "QQQ": {"QQQ": 1}, "BRK.B": {"BRK.B": 1}, "QQQ50/SPY50": {"QQQ": .5, "SPY": .5}, "SPY50/BRK50": {"SPY": .5, "BRK.B": .5},
       "QQQ50/BRK50": {"QQQ": .5, "BRK.B": .5}, "三者各1/3": {"QQQ": 1 / 3, "SPY": 1 / 3, "BRK.B": 1 / 3}, "QQQ40/SPY30/BRK30（你的定投比例）": {"QQQ": .4, "SPY": .3, "BRK.B": .3},
       "QQQ60/BRK40": {"QQQ": .6, "BRK.B": .4}, "QQQ40/SPY20/BRK40": {"QQQ": .4, "SPY": .2, "BRK.B": .4}, "QQQ40/SPY10/BRK50": {"QQQ": .4, "SPY": .1, "BRK.B": .5},
       "QQQ40/BRK60": {"QQQ": .4, "BRK.B": .6}, "QQQ50/SPY10/BRK40": {"QQQ": .5, "SPY": .1, "BRK.B": .4}, "QQQ30/BRK70": {"QQQ": .3, "BRK.B": .7}}
rows = {}
for name, w in MIX.items():
    r = sum(R[k] * v for k, v in w.items())
    cum = (1 + r).cumprod()
    yrs = (cum.index[-1] - cum.index[0]).days / 365.25
    w5 = (cum.shift(-60) / cum - 1).dropna() * 100
    dd = (cum / cum.cummax() - 1) * 100
    rows[name] = dict(年化=(cum.iloc[-1] ** (1 / yrs) - 1) * 100, 年化波动=r.std() * np.sqrt(12) * 100, 最大回撤=dd.min(), 回撤2022=dd[dd.index.year == 2022].min(),
                      回撤2000_02=dd[(dd.index.year >= 2000) & (dd.index.year <= 2002)].min(), 五年中位=w5.median(), 五年最差=w5.min(), 五年最差起点=str(w5.idxmin().date()),
                      五年为负比例=(w5 < 0).mean() * 100, 担保人期望赔付=(-w5.clip(upper=0)).mean())
M = pd.DataFrame(rows).T
M.to_csv(HERE / "etf_overlap_metrics.csv", float_format="%.1f", encoding="utf-8-sig")
S["metrics_1999"] = M.round(1).to_dict("index")
# SPY vs VOO
V = pd.DataFrame({"SPY": m(spy), "VOO": m(voo)}).dropna()
V = V[V.index >= "2010-10-01"]
yrs_v = (V.index[-1] - V.index[0]).days / 365.25
S["spy_vs_voo"] = dict(window=f"{V.index[0].date()}→{V.index[-1].date()}", spy_cagr=((V["SPY"].iloc[-1] / V["SPY"].iloc[0]) ** (1 / yrs_v) - 1) * 100,
                       voo_cagr=((V["VOO"].iloc[-1] / V["VOO"].iloc[0]) ** (1 / yrs_v) - 1) * 100, corr=float(V.pct_change().dropna().corr().iloc[0, 1]), fee_spy=0.0945, fee_voo=0.03)
# BRK cash share of market cap
try:
    html = urllib.request.urlopen(urllib.request.Request("https://stockanalysis.com/stocks/brk.b/", headers=UA), timeout=30).read().decode("utf-8", "ignore")
    mcap_txt = re.search(r"Market Cap[^0-9]{0,300}?([\d.,]+)\s*([BT])", html, re.S)
    mcap = float(mcap_txt.group(1).replace(",", "")) * (1000 if mcap_txt.group(2) == "T" else 1)
    src = "stockanalysis.com/stocks/brk.b"
except Exception as e:  # noqa: BLE001
    mcap = float(brka["close"].iloc[-1]) * 1.43e6 / 1e9
    src = f"BRK-A close × 1.43M A-equivalent shares (stockanalysis failed: {str(e)[:60]})"
S["brk"] = dict(mcap_bn=mcap, mcap_source=src, cash_bn=BRK_CASH_BN, securities_bn=BRK_SECURITIES_BN, asof=BRK_ASOF, cash_share_of_mcap=BRK_CASH_BN / mcap * 100,
                securities_share_of_mcap=BRK_SECURITIES_BN / mcap * 100, brkb_close=float(brkb["close"].iloc[-1]), brkb_date=str(brkb.index[-1].date()))
# holdings overlap (top-25 lists cached by the temperature pipeline)
try:
    hq = pd.read_csv(MT / "qqq_holdings_top.csv")
    hs = pd.read_csv(MT / "spy_holdings_top.csv")
    both = set(hq["symbol"]) & set(hs["symbol"])
    S["holdings"] = dict(qqq_top25_weight=float(hq["weight"].sum()), spy_top25_weight=float(hs["weight"].sum()), names_in_both_top25=sorted(both),
                         spy_weight_of_shared=float(hs[hs["symbol"].isin(both)]["weight"].sum()), qqq_weight_of_shared=float(hq[hq["symbol"].isin(both)]["weight"].sum()),
                         brk_weight_in_spy=float(hs[hs["symbol"].str.upper().str.startswith("BRK")]["weight"].sum()))
except Exception as e:  # noqa: BLE001
    S["holdings"] = {"error": str(e)}
json.dump(S, open(HERE / "etf_overlap.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False, default=float)

fig, axes = plt.subplots(1, 2, figsize=(13, 4.8))
ax = axes[0]
for k, c in (("SPY", "#1f4e79"), ("QQQ", "#e36c09"), ("BRK.B", "#2e7d32")):
    s = A[k] / A[k].iloc[0] * 100
    ax.plot(s.index, s.values, color=c, lw=1, label=f"{k}（年化 {rows[k]['年化']:.1f}%，最大回撤 {rows[k]['最大回撤']:.0f}%）")
ax.set_yscale("log")
ax.set_title(f"1999-04 起 100 美元（含分红）· 月度相关 QQQ–SPY {S['corr_monthly']['QQQ']['SPY']:.2f}，BRK–SPY {S['corr_monthly']['BRK.B']['SPY']:.2f}")
ax.legend(loc="upper left")
ax = axes[1]
for k, c in (("SPY", "#1f4e79"), ("QQQ", "#e36c09"), ("BRK.B", "#2e7d32"), ("QQQ40/SPY30/BRK30（你的定投比例）", "#c00000")):
    r = sum(R[kk] * v for kk, v in MIX[k].items())
    cum = (1 + r).cumprod()
    w5 = (cum.shift(-60) / cum - 1).dropna() * 100
    ax.plot(w5.index, w5.values, color=c, lw=1, label=f"{k[:18]}（最差 {w5.min():+.0f}%）")
ax.axhline(0, color="black", lw=.6)
ax.set_title("之后 5 年总回报 %")
ax.legend(loc="upper left")
fig.tight_layout()
fig.savefig(F / "05_etf_overlap.png")
plt.close(fig)
pd.set_option("display.width", 220)
print(M.round(1).to_string())
print(json.dumps({k: S[k] for k in ("corr_monthly", "qqq_beta_on_spy", "qqq_r2_on_spy", "brk_beta_on_spy", "brk_r2_on_spy", "spy_vs_voo", "brk", "holdings")}, indent=1, ensure_ascii=False, default=float))
