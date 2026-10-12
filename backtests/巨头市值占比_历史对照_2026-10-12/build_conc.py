#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Market concentration as an overheating gauge: largest company's share, top-10 share, Nasdaq-100 share of the market.
Current numbers from stockanalysis.com (market caps, ETF weights, as of 2026-10-08/10); history from Apollo (Bloomberg),
GW&K, CRSP/Morningstar, Finaeon/GFD, Zweig (via Axios). Outputs fig/*.png, stats_conc.json."""
import json, sys, numpy as np, pandas as pd
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass
from pathlib import Path
HERE = Path(__file__).resolve().parent; D = HERE/"data"; F = HERE/"fig"; F.mkdir(exist_ok=True)
plt.rcParams.update({"font.family": ["Microsoft YaHei", "SimHei"], "axes.unicode_minus": False, "figure.dpi": 150, "axes.grid": True, "grid.alpha": .3,
                     "axes.spines.top": False, "axes.spines.right": False, "font.size": 9, "legend.fontsize": 8, "axes.titlesize": 11})
NAVY, ORANGE, RED, GREEN, GRAY, PURPLE, TEAL, GOLD, BROWN = "#1f4e79", "#e36c09", "#c00000", "#2e7d32", "#7f7f7f", "#6a3d9a", "#0b7285", "#b8860b", "#8c564b"
S = {}
# ---- current ----
sp = pd.read_csv(D/"sp500_mcaps.csv"); nd = pd.read_csv(D/"ndx100_mcaps.csv"); spy = pd.read_csv(D/"spy_holdings_top.csv"); qqq = pd.read_csv(D/"qqq_holdings_top.csv")
sp_tot, nd_tot = sp.mcap_usd.sum(), nd.mcap_usd.sum()
nv = float(sp[sp.symbol == "NVDA"].mcap_usd.iloc[0])
S["now"] = dict(as_of="2026-10-08/10", nvda_mcap_T=nv/1e12, sp500_total_T=sp_tot/1e12, ndx_total_T=nd_tot/1e12, nvda_share_sp500_cap=nv/sp_tot*100, nvda_weight_spy=float(spy.weight.iloc[0]),
                nvda_share_ndx_cap=nv/nd_tot*100, nvda_weight_qqq=float(qqq.weight.iloc[0]), top10_sp500_cap=sp.mcap_usd.nlargest(10).sum()/sp_tot*100, top10_spy=float(spy.weight.head(10).sum()),
                top3_sp500_cap=sp.mcap_usd.nlargest(3).sum()/sp_tot*100, top3_spy=float(spy.weight.head(3).sum()), top10_ndx_cap=nd.mcap_usd.nlargest(10).sum()/nd_tot*100, top10_qqq=float(qqq.weight.head(10).sum()),
                top3_qqq=float(qqq.weight.head(3).sum()), ndx_over_sp500_cap=nd_tot/sp_tot*100, spy_top10=spy.head(10)[["symbol", "weight"]].values.tolist(), qqq_top10=qqq.head(10)[["symbol", "weight"]].values.tolist())
# total US market (Siblis 2026-06-30 $75.3T) scaled by Wilshire 5000 since then
w = pd.read_csv(D.parent.parent/"QQQ_vs_GDP加CPI_锚点2010_2020_2026-10-12"/"data"/"W5000_daily.csv", parse_dates=["date"]).set_index("date").close
ndx = pd.read_csv(D.parent.parent/"QQQ_vs_GDP加CPI_锚点2010_2020_2026-10-12"/"data"/"NDX_daily.csv", parse_dates=["date"]).set_index("date").close
us_tot_now = sp_tot/0.82; S["now"]["us_total_T_est"] = us_tot_now/1e12; S["now"]["siblis_2026_06_30_T"] = 75.3; S["now"]["w5000_change_since_0630"] = float(w.iloc[-1]/w[:"2026-06-30"].iloc[-1]-1)*100; S["now"]["nvda_share_us_est"] = nv/us_tot_now*100; S["now"]["ndx_share_us_est"] = nd_tot/us_tot_now*100
# ---- history ----
ap = pd.read_csv(D/"apollo_largest_weight_by_year.csv")
S["largest_sp500_hist"] = dict(source="Apollo Global (Bloomberg), 2026-01, year-end largest weight in S&P 500; read off chart ±0.1pp", top=ap.sort_values("weight_pct", ascending=False).head(12).to_dict("records"))
TOP10_SP = [(1985, 19.5), (1999, 25.2), (2014, 18.0), (2020, 28.6), (2025, 40.7), (2026.5, 37.9), (2026.78, S["now"]["top10_spy"])]  # GW&K + SPY weights now
TOP10_CRSP = [(1932.4, 37.3), (2025.8, 37.7)]  # CRSP total US market, month-end peaks
TOP10_FIN = [(1875, 30), (1894, 22), (1903, 29), (1925, 17), (1964, 32), (1993, 16), (2001, 24), (2014, 16), (2024, 32.5)]  # Finaeon: top-10 share of top-500 stocks
LARGEST_TOTAL = [(1900, 9, "标准石油"), (1929, 3, "AT&T"), (1932.4, 13, "AT&T（Zweig/WSJ 转引）"), (1960, 7, "最大公司（Finaeon）"), (1995, 2, "最大公司（Finaeon）"), (2026.78, S["now"]["nvda_share_us_est"], "英伟达（估算）")]
S["series"] = dict(top10_sp=TOP10_SP, top10_crsp=TOP10_CRSP, top10_finaeon=TOP10_FIN, largest_total=LARGEST_TOTAL)
# NDX share of US market proxy: NDX/W5000 ratio scaled so today's value equals the estimated share
r = (ndx/w).dropna(); share = r/r.iloc[-1]*S["now"]["ndx_share_us_est"]
S["ndx_share_proxy"] = dict(now=float(share.iloc[-1]), peak2000=float(share["2000"].max()), peak2000_date=str(share["2000"].idxmax().date()), low2002=float(share["2002":"2003"].min()), at2010=float(share["2010"].iloc[0]), at2020=float(share["2020"].iloc[0]), peak2021=float(share["2021"].max()), low2009=float(share["2008":"2009"].min()), at1990=float(share["1990"].iloc[0]))
json.dump(S, open(HERE/"stats_conc.json", "w", encoding="utf-8"), indent=2, ensure_ascii=False, default=float)
print(json.dumps(S["now"], indent=1, ensure_ascii=False, default=float)); print(S["ndx_share_proxy"])


def save(fig, name): fig.tight_layout(); fig.savefig(F/name, dpi=150); plt.close(fig); print("fig", name)


# F1 largest weight in S&P 500 by year
fig, ax = plt.subplots(figsize=(10, 4.4)); cmap = {"Apple": NAVY, "NVIDIA": RED, "IBM": GRAY, "AT&T": BROWN, "Exxon Mobil": GOLD, "General Electric": TEAL, "Microsoft": PURPLE, "Walmart": ORANGE}
for comp, g in ap.groupby("company"): ax.bar(g.year, g.weight_pct, color=cmap.get(comp, GRAY), label=comp, width=.8)
ax.bar([2026.8], [S["now"]["nvda_share_sp500_cap"]], color=RED, width=.8, hatch="//", edgecolor="white"); ax.annotate(f"2026-10 英伟达 {S['now']['nvda_share_sp500_cap']:.1f}%（市值口径）\nSPY 权重 {S['now']['nvda_weight_spy']:.1f}%", (2026.8, S["now"]["nvda_share_sp500_cap"]), xytext=(-8, 12), textcoords="offset points", ha="right", fontsize=8, color=RED, fontweight="bold")
ax.set_ylim(0, 9.6); ax.set_ylabel("%"); ax.set_title("图 1 · 标普500 第一大权重股的占比，1981–2026（年末值；来源 Apollo / Bloomberg，2026-10 为本报告计算）"); ax.legend(loc="upper left", ncol=4, fontsize=7.5)
save(fig, "01_largest_weight_sp500.png")
# F2 top-10 shares
fig, ax = plt.subplots(figsize=(10, 4.4))
for ser, col, lab, mk in [(TOP10_SP, NAVY, "标普500 前十大占比（GW&K；2026-10 为 SPY 权重）", "o"), (TOP10_CRSP, RED, "全美市场前十大占比（CRSP，1932-05 与 2025-10 两个峰值）", "s"), (TOP10_FIN, TEAL, "前 500 家中前十大占比（Finaeon/GFD）", "^")]:
    x = [p[0] for p in ser]; y = [p[1] for p in ser]; ax.plot(x, y, marker=mk, lw=(0 if col == RED else .9), color=col, label=lab, ms=6)
    for xx, yy in ser: ax.annotate(f"{yy:.0f}", (xx, yy), xytext=(0, 5), textcoords="offset points", ha="center", fontsize=7, color=col)
ax.set_ylabel("%"); ax.set_xlim(1870, 2030); ax.set_title("图 2 · 前十大公司占比：三个口径的历史点位"); ax.legend(loc="upper center", fontsize=7.5)
save(fig, "02_top10_history.png")
# F3 NDX share proxy
fig, ax = plt.subplots(figsize=(10, 3.8)); ax.plot(share.index, share.values, lw=.9, color=NAVY, label="纳指100 市值 ÷ 全美市值（代理：NDX/W5000 指数比，按今日实际占比定标）")
for d, t in [("2000-03-27", "2000 顶"), ("2002-10-07", "2002 底"), ("2021-11-19", "2021 顶")]: d = pd.Timestamp(d); ax.annotate(f"{t} {share[:d].iloc[-1]:.0f}%", (d, share[:d].iloc[-1]), xytext=(0, 8), textcoords="offset points", ha="center", fontsize=8, color=GRAY)
ax.plot([share.index[-1]], [share.iloc[-1]], "o", color=RED, ms=5); ax.annotate(f"{share.iloc[-1]:.0f}%", (share.index[-1], share.iloc[-1]), xytext=(6, 2), textcoords="offset points", color=RED, fontsize=8, fontweight="bold")
ax.set_ylabel("%"); ax.set_title("图 3 · 纳指100 占全美股票市值的比例（1989 起代理序列）"); ax.legend(loc="upper left")
save(fig, "03_ndx_share_proxy.png")
# F4 current top-10 bars
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 3.8))
for ax, df, lab, col in [(ax1, spy, f"SPY 前十大权重，合计 {spy.weight.head(10).sum():.1f}%", NAVY), (ax2, qqq, f"QQQ 前十大权重，合计 {qqq.weight.head(10).sum():.1f}%", RED)]:
    d = df.head(10); ax.barh(d.symbol[::-1], d.weight[::-1], color=col); ax.set_title(lab); ax.set_xlabel("%")
    for i, v in enumerate(d.weight[::-1]): ax.annotate(f"{v:.1f}", (v, i), xytext=(3, -3), textcoords="offset points", fontsize=7.5)
fig.suptitle("图 4 · 现在的前十大（stockanalysis.com，2026-10-08）", fontsize=11); save(fig, "04_top10_now.png")
