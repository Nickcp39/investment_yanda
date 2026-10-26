#!/usr/bin/env python
"""Gold / QQQ / Treasuries, pick two: monthly-rebalanced mixes measured the way a guarantor reads them
(5-year rolling windows: median, worst, share negative, expected shortfall; max drawdown; 2022).

Two samples:
  A. 1985-10 → 2026-09  equity = Nasdaq-100 price (1985–1999) spliced to QQQ adj close (1999–)   [tech tilt, as the mandate wants]
  B. 1970-01 → 2026-09  equity = S&P 500 total return (Shiller to 1987, SP500TR after)            [adds the 1970s and the 1980 gold top]
Gold = LBMA PM fix (1968–2026-09-08) spliced to COMEX GC=F. Treasury = constant-maturity 5-year par-bond proxy built from ^FVX
(carry + duration × yield change + convexity), validated against IEF (10-year proxy from ^TNX) over 2002–2026. Cash = 13-week bill (^IRX).
Outputs: metrics_1985.csv, metrics_1970.csv, stats.json, fig/01..04
"""
import json
import sys
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
D11 = REPO / "backtests" / "代管资金_5年保本任务_投研_2026-10-11" / "data"
F = HERE / "fig"
F.mkdir(exist_ok=True)
plt.rcParams.update({"font.family": ["Microsoft YaHei", "SimHei"], "axes.unicode_minus": False, "figure.dpi": 150, "axes.grid": True, "grid.alpha": .3,
                     "axes.spines.top": False, "axes.spines.right": False, "font.size": 9, "legend.fontsize": 8, "axes.titlesize": 10.5})
NAVY, ORANGE, RED, GREEN, GRAY, PURPLE, TEAL, GOLD = "#1f4e79", "#e36c09", "#c00000", "#2e7d32", "#7f7f7f", "#6a3d9a", "#0b7285", "#b8860b"
Y5_NOW, IBTL_NOW = 4.81, 4.83
P_USD = 52548.0


def daily(path, col="close"):
    df = pd.read_csv(path, parse_dates=["date"]).set_index("date").sort_index()
    return df[col].dropna()


def monthly(s):
    m = s.resample("MS").first().dropna()
    m.index = m.index.normalize()
    return m


# ---------------- assets ----------------
ndx, qqq = daily(MT / "NDX_daily.csv"), daily(MT / "QQQ_daily.csv", "adj_close")
q0 = qqq.index[0]
eq_tech = pd.concat([ndx[ndx.index < q0] * qqq.iloc[0] / ndx[ndx.index <= q0].iloc[-1], qqq])
g = pd.read_csv(MT / "gold_lbma_pm_daily.csv", parse_dates=[0])
g = g.set_index(g.columns[0]).iloc[:, 0].astype(float).dropna().sort_index()
gcf = daily(MT / "GCF_daily.csv")
gold = pd.concat([g, gcf[gcf.index > g.index[-1]]])
fvx, tnx, irx = daily(MT / "FVX_daily.csv"), daily(MT / "TNX_daily.csv"), daily(MT / "IRX_daily.csv")
sh = pd.read_csv(REPO / "backtests" / "QQQ_现在高不高_2026-10-08" / "data" / "shiller_monthly.csv", parse_dates=["dt"]).set_index("dt").sort_index()
sh = sh[sh["P"].notna()]
tr_sh = ((1 + (sh["D"] / 12) / sh["P"].shift(1)) * (sh["P"] / sh["P"].shift(1))).fillna(1).cumprod()
sptr = monthly(daily(MT / "SP500TR_daily.csv"))
cut = pd.Timestamp("1988-01-01")
eq_spx = pd.concat([tr_sh[tr_sh.index < cut], sptr[sptr.index >= cut] * tr_sh[cut] / sptr[cut]])


def bond_proxy(y_monthly, n):
    """constant-maturity par bond total return from a yield series (pct). r_t = carry + price change from yield move."""
    y = y_monthly / 100
    out = [1.0]
    for i in range(1, len(y)):
        y0, y1 = y.iloc[i - 1], y.iloc[i]
        dur = (1 - (1 + y0) ** -n) / y0
        mod = dur / (1 + y0)
        conv = dur * (dur + 1) / (1 + y0) ** 2
        r = y0 / 12 - mod * (y1 - y0) + 0.5 * conv * (y1 - y0) ** 2
        out.append(out[-1] * (1 + r))
    return pd.Series(out, index=y.index)


fvx_m, tnx_m, irx_m = monthly(fvx), monthly(tnx), monthly(irx)
b5 = bond_proxy(fvx_m, 5)
b10 = bond_proxy(tnx_m, 10)
cash = (1 + irx_m.shift(1) / 100 / 12).fillna(1).cumprod()
# validate the proxy against IEF (7-10y Treasury ETF, adj close) 2002-08 → 2026-09
ief = monthly(daily(D11 / "IEF_daily.csv", "adj_close"))
common = ief.index.intersection(b10.index)
ief_r, b10_r = ief[common].pct_change().dropna(), b10[common].pct_change().dropna()
yrs_v = (common[-1] - common[0]).days / 365.25
VALID = dict(window=f"{common[0].date()}→{common[-1].date()}", ief_cagr=((ief[common].iloc[-1] / ief[common].iloc[0]) ** (1 / yrs_v) - 1) * 100,
             proxy10_cagr=((b10[common].iloc[-1] / b10[common].iloc[0]) ** (1 / yrs_v) - 1) * 100, corr_monthly=float(ief_r.corr(b10_r)),
             ief_maxdd=float((ief[common] / ief[common].cummax() - 1).min() * 100), proxy10_maxdd=float((b10[common] / b10[common].cummax() - 1).min() * 100))

# ---------------- mixes ----------------
MIXES = {
    "QQQ 100": {"eq": 1}, "黄金 100": {"gold": 1}, "国债5年 100": {"b5": 1}, "现金 100": {"cash": 1},
    "QQQ80/金20": {"eq": .8, "gold": .2}, "QQQ70/金30": {"eq": .7, "gold": .3}, "QQQ60/金40": {"eq": .6, "gold": .4}, "QQQ50/金50": {"eq": .5, "gold": .5},
    "QQQ80/债20": {"eq": .8, "b5": .2}, "QQQ70/债30": {"eq": .7, "b5": .3}, "QQQ60/债40": {"eq": .6, "b5": .4}, "QQQ50/债50": {"eq": .5, "b5": .5},
    "金60/债40": {"gold": .6, "b5": .4}, "金50/债50": {"gold": .5, "b5": .5}, "金40/债60": {"gold": .4, "b5": .6},
    "QQQ60/金20/债20": {"eq": .6, "gold": .2, "b5": .2}, "QQQ50/金25/债25": {"eq": .5, "gold": .25, "b5": .25}, "QQQ40/金30/债30": {"eq": .4, "gold": .3, "b5": .3},
    "QQQ70/现金30": {"eq": .7, "cash": .3},
}


def run(eq_series, start, label):
    A = pd.DataFrame({"eq": monthly(eq_series), "gold": monthly(gold), "b5": b5, "cash": cash}).dropna()
    A = A[A.index >= start]
    R = A.pct_change().dropna()
    rows, curves = [], {}
    for name, w in MIXES.items():
        r = sum(R[k] * v for k, v in w.items())
        cum = (1 + r).cumprod()
        curves[name] = cum
        yrs = (cum.index[-1] - cum.index[0]).days / 365.25
        w5 = (cum.shift(-60) / cum - 1).dropna() * 100
        w10 = (cum.shift(-120) / cum - 1).dropna() * 100
        dd = (cum / cum.cummax() - 1) * 100
        rows.append(dict(组合=name, 年化=((cum.iloc[-1]) ** (1 / yrs) - 1) * 100, 年化波动=r.std() * np.sqrt(12) * 100, 最大回撤=dd.min(), 回撤2022=dd["2022"].min() if "2022" in str(dd.index.year.tolist()) or (dd.index.year == 2022).any() else np.nan,
                         五年中位=w5.median(), 五年最差=w5.min(), 五年最差起点=str(w5.idxmin().date()), 五年5分位=w5.quantile(.05), 五年为负比例=(w5 < 0).mean() * 100,
                         担保人期望赔付=(-w5.clip(upper=0)).mean(), 十年中位=w10.median(), 十年最差=w10.min(), 窗口数=int(len(w5))))
    M = pd.DataFrame(rows).set_index("组合")
    M.to_csv(HERE / f"metrics_{label}.csv", float_format="%.1f", encoding="utf-8-sig")
    corr = R[["eq", "gold", "b5"]].corr().round(2).to_dict()
    # protection structure, rolling with the 5y yield at each start (locked) + at today's IBTL yield
    y5 = fvx_m.reindex(A.index).ffill() / 100
    eqm = A["eq"]
    e5 = (eqm.shift(-60) / eqm - 1).dropna()
    starts = e5.index
    hist = pd.Series([(1 / (1 + y5[t]) ** 5) * (1 + y5[t]) ** 5 + (1 - 1 / (1 + y5[t]) ** 5) * (1 + e5[t]) - 1 for t in starts], index=starts) * 100
    bnow = 1 / (1 + IBTL_NOW / 100) ** 5
    now = (bnow * (1 + IBTL_NOW / 100) ** 5 + (1 - bnow) * (1 + e5) - 1) * 100
    prot = dict(hist_median=hist.median(), hist_worst=hist.min(), hist_worst_start=str(hist.idxmin().date()), now_median=now.median(), now_worst=now.min(), now_p5=now.quantile(.05), bond_share_now=bnow * 100)
    # sub-periods
    subs = {}
    for a, b in (("1970", "1979"), ("1980", "1999"), ("2000", "2009"), ("2010", "2019"), ("2020", "2026")):
        seg = A[a:b]
        if len(seg) > 12:
            yy = (seg.index[-1] - seg.index[0]).days / 365.25
            subs[f"{a}–{b}"] = {k: ((seg[k].iloc[-1] / seg[k].iloc[0]) ** (1 / yy) - 1) * 100 for k in ("eq", "gold", "b5", "cash")}
    return M, curves, corr, prot, subs, A


M85, C85, corr85, prot85, subs85, A85 = run(eq_tech, "1985-10-01", "1985")
M70, C70, corr70, prot70, subs70, A70 = run(eq_spx, "1970-01-01", "1970")
S = dict(as_of=str(A85.index[-1].date()), proxy_validation=VALID, corr_1985=corr85, corr_1970=corr70, protection_1985=prot85, protection_1970=prot70,
         subperiods_1985=subs85, subperiods_1970=subs70, metrics_1985=M85.round(1).to_dict("index"), metrics_1970=M70.round(1).to_dict("index"),
         gold_now=float(gold.iloc[-1]), gold_date=str(gold.index[-1].date()), principal_usd=P_USD)
json.dump(S, open(HERE / "stats.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False, default=float)

# ---------------- figures ----------------
fig, ax = plt.subplots(figsize=(11, 5))
for name, c in (("QQQ 100", NAVY), ("黄金 100", GOLD), ("国债5年 100", GREEN), ("QQQ50/金50", ORANGE), ("QQQ60/债40", TEAL), ("金50/债50", PURPLE)):
    s = C85[name]
    ax.plot(s.index, s.values * 100, color=c, lw=1.1, label=f"{name}（年化 {M85.loc[name, '年化']:.1f}%，最大回撤 {M85.loc[name, '最大回撤']:.0f}%）")
ax.set_yscale("log")
ax.set_title("图 1 · 1985-10 起 100 美元：三个单资产与三种两两组合（月度再平衡，纳指100 价格接 QQQ 含分红）")
ax.legend(loc="upper left")
fig.tight_layout()
fig.savefig(F / "01_growth_1985.png")
plt.close(fig)

fig, ax = plt.subplots(figsize=(11, 4.8))
for name, c in (("QQQ 100", NAVY), ("QQQ50/金50", ORANGE), ("QQQ60/债40", TEAL), ("金50/债50", PURPLE), ("QQQ50/金25/债25", RED)):
    s = C85[name]
    w5 = (s.shift(-60) / s - 1).dropna() * 100
    ax.plot(w5.index, w5.values, color=c, lw=1, label=f"{name}（最差 {w5.min():+.0f}%，中位 {w5.median():+.0f}%）")
ax.axhline(0, color="black", lw=.6)
ax.set_ylabel("之后 5 年总回报 %")
ax.set_title("图 2 · 从每个月起算的 5 年总回报（担保人看的那条线）· 1985 起")
ax.legend(loc="upper left", ncol=2)
fig.tight_layout()
fig.savefig(F / "02_rolling5y_1985.png")
plt.close(fig)

fig, axes = plt.subplots(1, 2, figsize=(13, 5.2))
for ax, M, ttl in ((axes[0], M85, "1985 起（QQQ）"), (axes[1], M70, "1970 起（标普替代 QQQ）")):
    for name, r in M.iterrows():
        c = GOLD if "金" in name and "QQQ" not in name else (ORANGE if "金" in name and "债" not in name else (TEAL if "债" in name and "金" not in name else (RED if "金" in name and "债" in name else NAVY)))
        ax.scatter(r["五年最差"], r["五年中位"], color=c, s=28, zorder=3)
        ax.annotate(name, (r["五年最差"], r["五年中位"]), fontsize=6.5, xytext=(3, 2), textcoords="offset points")
    ax.axvline(0, color="black", lw=.6)
    ax.set_xlabel("5 年最差总回报 %（越右越好）")
    ax.set_ylabel("5 年中位总回报 %")
    ax.set_title(f"图 3 · 担保人前沿 · {ttl}")
fig.tight_layout()
fig.savefig(F / "03_frontier.png")
plt.close(fig)

fig, ax = plt.subplots(figsize=(9, 4.2))
labels = list(subs70.keys())
x = np.arange(len(labels))
for i, (k, c, lab) in enumerate((("eq", NAVY, "标普500 含分红"), ("gold", GOLD, "黄金"), ("b5", GREEN, "5 年国债（持续滚动）"), ("cash", GRAY, "现金"))):
    ax.bar(x + (i - 1.5) * .2, [subs70[l][k] for l in labels], width=.2, color=c, label=lab)
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_ylabel("年化 %")
ax.set_title("图 4 · 分时段年化：黄金有过 20 年的熊市（1980–1999），债有过 2020–2022")
ax.legend()
fig.tight_layout()
fig.savefig(F / "04_subperiods.png")
plt.close(fig)

pd.set_option("display.width", 220)
print("proxy validation", VALID)
print("corr 1985", corr85)
print(M85[["年化", "最大回撤", "回撤2022", "五年中位", "五年最差", "五年最差起点", "五年为负比例", "担保人期望赔付", "十年最差"]].round(1).to_string())
print("protection 1985", prot85)
print("sub 1985", json.dumps(subs85, indent=None, default=float))
print("--- 1970 (S&P) ---")
print(M70[["年化", "最大回撤", "五年中位", "五年最差", "五年最差起点", "五年为负比例", "担保人期望赔付", "十年最差"]].round(1).to_string())
print("protection 1970", prot70)
print("sub 1970", json.dumps(subs70, indent=None, default=float))
