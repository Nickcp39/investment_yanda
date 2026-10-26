#!/usr/bin/env python
"""20-year horizon: are Treasuries worth holding, and how much does a principal guarantee cost at 20 years vs 5?

Inputs (all already cached in the repo):
  Shiller monthly 1871-2023 (P, D, CPI, GS10)        backtests/QQQ_现在高不高_2026-10-08/data/shiller_monthly.csv
  S&P 500 total return daily 1988-                   data/market_temp/SP500TR_daily.csv
  NDX price 1985-, QQQ adj 1999-, ^TNX ^FVX 1970-    data/market_temp/*_daily.csv
  BLS CPI-U 1978-                                     data/market_temp/bls_cpi_unrate_monthly.csv
Outputs: stats.json, windows_20y.csv, fig/01_20y_windows.png, fig/02_bond_share_vs_horizon.png, fig/03_yield_history.png
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
F = HERE / "fig"
F.mkdir(exist_ok=True)
plt.rcParams.update({"font.family": ["Microsoft YaHei", "SimHei"], "axes.unicode_minus": False, "figure.dpi": 150, "axes.grid": True, "grid.alpha": .3,
                     "axes.spines.top": False, "axes.spines.right": False, "font.size": 9, "legend.fontsize": 8, "axes.titlesize": 10.5})
NAVY, ORANGE, RED, GREEN, GRAY, PURPLE, TEAL = "#1f4e79", "#e36c09", "#c00000", "#2e7d32", "#7f7f7f", "#6a3d9a", "#0b7285"

# current yields (Yahoo 2026-10-24 close via quote meta; FVX/TNX also in market_temp cache 10-23 close)
Y_NOW = {"3m": 4.03, "5y": 4.81, "10y": 4.99, "30y": 5.32}
CPI_YOY_NOW = 4.0  # BLS Sept 2026, from the 10-23 temperature run


def daily(label, col="close"):
    return pd.read_csv(MT / f"{label}_daily.csv", parse_dates=["date"]).set_index("date").sort_index()[col].dropna()


# ---------------- long monthly series: S&P total return, CPI, 10y yield ----------------
sh = pd.read_csv(REPO / "backtests" / "QQQ_现在高不高_2026-10-08" / "data" / "shiller_monthly.csv", parse_dates=["dt"]).set_index("dt").sort_index()
sh = sh[sh["P"].notna()]
tr_sh = (1 + (sh["D"] / 12) / sh["P"].shift(1)) * (sh["P"] / sh["P"].shift(1))
tr_sh = tr_sh.fillna(1).cumprod()
sptr = daily("SP500TR").resample("MS").first()
sptr.index = sptr.index.normalize()
cut = pd.Timestamp("1988-01-01")
tr = pd.concat([tr_sh[tr_sh.index < cut], sptr[sptr.index >= cut] * tr_sh[cut] / sptr[cut]])
bls = pd.read_csv(MT / "bls_cpi_unrate_monthly.csv")
bls["dt"] = pd.to_datetime(bls["month"])
cpi_b = bls.set_index("dt")["cpi_u_nsa"].dropna()
c0 = pd.Timestamp("1978-01-01")
cpi = pd.concat([sh["CPI"][sh.index < c0], cpi_b[cpi_b.index >= c0] * sh["CPI"][c0] / cpi_b[c0]])
tnx = daily("TNX").resample("MS").first()
tnx.index = tnx.index.normalize()
gs10 = pd.concat([sh["GS10"][sh.index < pd.Timestamp("1970-01-01")], tnx[tnx.index >= pd.Timestamp("1970-01-01")]])
fvx = daily("FVX")
idx = tr.index.intersection(cpi.index).intersection(gs10.index)
tr, cpi, gs10 = tr[idx], cpi[idx], gs10[idx]
AS_OF = str(tr.index[-1].date())

# ---------------- yields: where are we ----------------
def pct(s, v):
    s = s.dropna()
    return float((s < v).mean() * 100)

real10 = gs10 - (cpi / cpi.shift(12) - 1) * 100
S = {"as_of": AS_OF, "yields_now": Y_NOW, "cpi_yoy_now": CPI_YOY_NOW, "real_10y_now": Y_NOW["10y"] - CPI_YOY_NOW}
S["yield_pct"] = {
    "10y_since_1871": pct(gs10, Y_NOW["10y"]), "10y_since_1962": pct(gs10["1962":], Y_NOW["10y"]), "10y_since_1980": pct(gs10["1980":], Y_NOW["10y"]),
    "10y_since_2009": pct(gs10["2009":], Y_NOW["10y"]), "5y_since_1970": pct(fvx, Y_NOW["5y"]), "5y_since_1980": pct(fvx["1980":], Y_NOW["5y"]),
    "real10_since_1871": pct(real10, S["real_10y_now"]), "real10_since_1980": pct(real10["1980":], S["real_10y_now"]),
    "gs10_median_1871": float(gs10.median()), "gs10_median_1980": float(gs10["1980":].median()), "gs10_median_1990_2007": float(gs10["1990":"2007"].median()),
    "real10_median_1871": float(real10.median()), "real10_median_1980": float(real10["1980":].median()),
}

# ---------------- rolling windows: stocks vs locked yield ----------------
def windows(tr, cpi, gs10, years):
    n = years * 12
    out = []
    for i in range(len(tr) - n):
        t0, t1 = tr.index[i], tr.index[i + n]
        nom = (tr.iloc[i + n] / tr.iloc[i]) ** (1 / years) - 1
        real = ((tr.iloc[i + n] / tr.iloc[i]) / (cpi.iloc[i + n] / cpi.iloc[i])) ** (1 / years) - 1
        y0 = gs10.iloc[i] / 100
        out.append(dict(start=t0, end=t1, stock_nom=nom * 100, stock_real=real * 100, bond_lock=y0 * 100,
                        bond_real=((1 + y0) / (cpi.iloc[i + n] / cpi.iloc[i]) ** (1 / years) - 1) * 100,
                        stock_minus_bond=(nom - y0) * 100, stock_mult=tr.iloc[i + n] / tr.iloc[i], bond_mult=(1 + y0) ** years))
    return pd.DataFrame(out).set_index("start")

W = {}
for yrs in (5, 10, 20):
    w = windows(tr, cpi, gs10, yrs)
    W[yrs] = w
    S[f"spx_{yrs}y"] = dict(n=int(len(w)), first=str(w.index[0].date()), last=str(w.index[-1].date()),
                            nom_min=float(w.stock_nom.min()), nom_min_start=str(w.stock_nom.idxmin().date()), nom_p5=float(w.stock_nom.quantile(.05)),
                            nom_p25=float(w.stock_nom.quantile(.25)), nom_median=float(w.stock_nom.median()), nom_p75=float(w.stock_nom.quantile(.75)), nom_max=float(w.stock_nom.max()),
                            real_min=float(w.stock_real.min()), real_min_start=str(w.stock_real.idxmin().date()), real_median=float(w.stock_real.median()),
                            share_negative_nom=float((w.stock_nom < 0).mean() * 100), share_negative_real=float((w.stock_real < 0).mean() * 100),
                            share_below_bond=float((w.stock_minus_bond < 0).mean() * 100), share_below_bond_since_1950=float((w["1950":].stock_minus_bond < 0).mean() * 100),
                            share_below_bond_since_1980=float((w["1980":].stock_minus_bond < 0).mean() * 100) if len(w["1980":]) else None,
                            worst_vs_bond=float(w.stock_minus_bond.min()), worst_vs_bond_start=str(w.stock_minus_bond.idxmin().date()),
                            bond_real_median=float(w.bond_real.median()), bond_real_min=float(w.bond_real.min()))
W[20].to_csv(HERE / "windows_20y.csv", float_format="%.2f", encoding="utf-8-sig")
# windows where stocks lost to the locked bond, 20y
lose = W[20][W[20].stock_minus_bond < 0]
S["spx_20y_lose_episodes"] = [dict(start=str(a.date()), stock=float(r.stock_nom), bond=float(r.bond_lock)) for a, r in lose.iterrows()][::12]
# decade-ish table for 20y windows at round starts
S["spx_20y_named"] = {}
for d in ("1929-09-01", "1965-01-01", "1972-12-01", "1981-09-01", "1989-01-01", "1999-12-01", "2000-03-01", "2006-10-01"):
    d = pd.Timestamp(d)
    if d in W[20].index:
        r = W[20].loc[d]
        S["spx_20y_named"][str(d.date())] = dict(stock_nom=float(r.stock_nom), stock_real=float(r.stock_real), bond_lock=float(r.bond_lock), stock_mult=float(r.stock_mult), bond_mult=float(r.bond_mult))

# ---------------- NDX / QQQ windows ----------------
ndx = daily("NDX").resample("MS").first()
qqq = daily("QQQ", "adj_close").resample("MS").first()

def simple_windows(s, years):
    n = years * 12
    r = (s.shift(-n) / s) ** (1 / years) - 1
    r = r.dropna() * 100
    return dict(n=int(len(r)), first=str(r.index[0].date()), last=str(r.index[-1].date()), min=float(r.min()), min_start=str(r.idxmin().date()),
                p5=float(r.quantile(.05)), p25=float(r.quantile(.25)), median=float(r.median()), max=float(r.max()), max_start=str(r.idxmax().date()),
                share_negative=float((r < 0).mean() * 100), share_below_5pct=float((r < 5).mean() * 100), series=r)

S["ndx_windows"] = {}
S["qqq_windows"] = {}
for yrs in (5, 10, 15, 20):
    a = simple_windows(ndx, yrs)
    S["ndx_windows"][str(yrs)] = {k: v for k, v in a.items() if k != "series"}
    if len(qqq) > yrs * 12 + 12:
        b = simple_windows(qqq, yrs)
        S["qqq_windows"][str(yrs)] = {k: v for k, v in b.items() if k != "series"}
ndx20 = simple_windows(ndx, 20)["series"]
ndx_named = {}
for d in ("1985-11-01", "1990-01-01", "1995-01-01", "2000-03-01", "2002-10-01", "2006-10-01"):
    d = pd.Timestamp(d)
    if d in ndx20.index:
        ndx_named[str(d.date())] = float(ndx20[d])
S["ndx_20y_named"] = ndx_named

# ---------------- protection structure vs horizon ----------------
def bond_share(y, h):
    return 1 / (1 + y / 100) ** h

S["bond_share_table"] = {}
for h, y in ((5, Y_NOW["5y"]), (10, Y_NOW["10y"]), (15, (Y_NOW["10y"] + Y_NOW["30y"]) / 2), (20, (Y_NOW["10y"] + Y_NOW["30y"]) / 2), (30, Y_NOW["30y"])):
    S["bond_share_table"][str(h)] = dict(yield_used=y, bond_share=bond_share(y, h) * 100, equity_share=(1 - bond_share(y, h)) * 100)
# 20y structure outcomes on 52,548 USD using NDX 20y window distribution (price-only; dividends ~0.5-1%/yr would add)
P = 52548.0
y20 = (Y_NOW["10y"] + Y_NOW["30y"]) / 2
b20 = bond_share(y20, 20)
eq = P * (1 - b20)
nd = S["ndx_windows"]["20"]
S["structure_20y"] = dict(principal_usd=P, yield_used=y20, bond_share=b20 * 100, bond_usd=P * b20, equity_usd=eq,
                          outcomes={k: dict(cagr=v, total=P * b20 * (1 + y20 / 100) ** 20 + eq * (1 + v / 100) ** 20) for k, v in
                                    (("纳指 20 年最差（起点 " + nd["min_start"] + "）", nd["min"]), ("纳指 20 年 5 分位", nd["p5"]), ("纳指 20 年中位", nd["median"]), ("纳指 20 年最好", nd["max"]))},
                          all_bond_total=P * (1 + y20 / 100) ** 20, all_equity={k: P * (1 + v / 100) ** 20 for k, v in (("最差", nd["min"]), ("中位", nd["median"]))})
# 5y structure for comparison
b5 = bond_share(Y_NOW["5y"], 5)
S["structure_5y"] = dict(bond_share=b5 * 100, bond_usd=P * b5, equity_usd=P * (1 - b5))
# equal-weight stock/bond over 20y (no guarantee): 60/40 locked
S["mix_20y"] = {}
for eqw in (1.0, 0.8, 0.6, 0.4, 0.0):
    S["mix_20y"][f"{round(eqw*100)}/{round((1-eqw)*100)}"] = {k: P * ((1 - eqw) * (1 + y20 / 100) ** 20 + eqw * (1 + v / 100) ** 20) for k, v in (("最差", nd["min"]), ("5分位", nd["p5"]), ("中位", nd["median"]))}

# ---------------- figures ----------------
w = W[20]
fig, ax = plt.subplots(figsize=(11, 5))
ax.plot(w.index, w.stock_nom, color=NAVY, lw=1, label="标普500 之后 20 年年化（含分红，名义）")
ax.plot(w.index, w.stock_real, color=TEAL, lw=.8, ls="--", label="同上，扣 CPI（实际）")
ax.plot(w.index, w.bond_lock, color=ORANGE, lw=1, label="起点 10 年国债收益率（= 锁定国债 20 年的名义年化）")
ax.fill_between(w.index, w.stock_nom, w.bond_lock, where=w.stock_nom < w.bond_lock, color=RED, alpha=.35, label="股票输给锁定国债的起点")
ax.axhline(Y_NOW["10y"], color=GRAY, lw=.8, ls=":", label=f"今天 10 年国债 {Y_NOW['10y']:.2f}%")
ax.set_ylabel("%/年")
ax.set_title(f"图 1 · 从每个月起算的 20 年：标普500 年化 vs 起点锁定的国债收益率（1871–{w.index[-1].year} 起点）")
ax.legend(loc="upper left", ncol=2)
fig.tight_layout()
fig.savefig(F / "01_20y_windows.png")
plt.close(fig)

fig, ax = plt.subplots(figsize=(7.5, 4.5))
hs = np.arange(1, 31)
for y, c, lab in ((Y_NOW["5y"], NAVY, f"按 5 年期 {Y_NOW['5y']:.2f}%"), (y20, ORANGE, f"按 10–30 年均值 {y20:.2f}%"), (1.5, GRAY, "2010–2021 常见的 1.5%")):
    ax.plot(hs, [bond_share(y, h) * 100 for h in hs], color=c, lw=1.3, label=lab)
for h in (5, 10, 20):
    ax.axvline(h, color=GRAY, lw=.6, ls=":")
ax.set_xlabel("投资期限（年）")
ax.set_ylabel("锁住 100% 本金所需的零息国债占比 %")
ax.set_title("图 2 · 期限越长，保本需要的国债越少：占比 = 1/(1+y)^期限")
ax.legend()
fig.tight_layout()
fig.savefig(F / "02_bond_share_vs_horizon.png")
plt.close(fig)

fig, ax = plt.subplots(figsize=(11, 4.2))
ax.plot(gs10.index, gs10.values, color=ORANGE, lw=.9, label="10 年国债收益率（Shiller GS10 → ^TNX）")
ax.plot(real10.index, real10.values, color=GRAY, lw=.7, label="减去 CPI 同比后的实际收益率")
ax.axhline(Y_NOW["10y"], color=NAVY, lw=.8, ls="--", label=f"今天 {Y_NOW['10y']:.2f}%（1871 起 {S['yield_pct']['10y_since_1871']:.0f} 分位，1980 起 {S['yield_pct']['10y_since_1980']:.0f} 分位）")
ax.axhline(0, color="black", lw=.5)
ax.set_ylim(-15, 16)
ax.set_title("图 3 · 10 年国债收益率 1871 年以来：现在高不高")
ax.legend(loc="upper left")
fig.tight_layout()
fig.savefig(F / "03_yield_history.png")
plt.close(fig)

json.dump(S, open(HERE / "stats.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False, default=float)
print(json.dumps({k: S[k] for k in ("yield_pct", "spx_20y", "spx_20y_named", "ndx_windows", "qqq_windows", "ndx_20y_named", "bond_share_table", "structure_20y", "mix_20y")}, indent=1, ensure_ascii=False, default=float))
