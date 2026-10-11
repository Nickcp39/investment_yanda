#!/usr/bin/env python
"""Post-crisis-era view: every gauge re-based on the sample that starts after a crisis trough.
Eras: A = 2002-10-07 (dot-com trough) ->, B = 2009-03-09 (GFC trough) ->.  Reference: full 1985 sample.
Trend lines, medians and percentiles are recomputed inside each era only.
Reads data/, writes fig/*.png + stats_era.json."""
import json, sys, numpy as np, pandas as pd
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass
from pathlib import Path
HERE = Path(__file__).resolve().parent; D = HERE/"data"; F = HERE/"fig"; F.mkdir(exist_ok=True)
plt.rcParams.update({"font.family": ["Microsoft YaHei", "SimHei", "DejaVu Sans"], "axes.unicode_minus": False, "figure.dpi": 150,
                     "axes.grid": True, "grid.alpha": .3, "axes.spines.top": False, "axes.spines.right": False, "font.size": 9, "legend.fontsize": 8, "axes.titlesize": 11})
NAVY, ORANGE, RED, GREEN, GRAY, PURPLE, TEAL = "#1f4e79", "#e36c09", "#c00000", "#2e7d32", "#7f7f7f", "#6a3d9a", "#0b7285"
ERAS = {"A": ("2002-10-07", "2002-10 起（互联网泡沫底之后）", TEAL), "B": ("2009-03-09", "2009-03 起（金融危机底之后）", ORANGE)}
FULL = "1985-10-01"
S = {"eras": {k: {"start": v[0], "label": v[1]} for k, v in ERAS.items()}}


def pr(s, v):
    s = s.dropna(); return float((s < v).mean()*100)


def load(l):
    return pd.read_csv(D/f"{l}_daily.csv", parse_dates=["date"]).set_index("date")


qqq, ndx, spy = load("QQQ"), load("NDX"), load("SPY")
n, a, p = ndx.close, qqq.adj_close, qqq.close
AS_OF = str(p.index[-1].date()); S["as_of"] = AS_OF; S["qqq_close"] = float(p.iloc[-1]); S["ndx_close"] = float(n.iloc[-1])
X0 = pd.Timestamp("2002-01-01")  # charts start here so both eras are visible


def mark_now(ax, x, y, fmt="{:+.0f}%", color=RED, dy=0):
    ax.plot([x], [y], "o", color=color, ms=5, zorder=5)
    ax.annotate(fmt.format(y), (x, y), xytext=(6, 4+dy), textcoords="offset points", color=color, fontsize=8, fontweight="bold")


def save(fig, name):
    fig.tight_layout(); fig.savefig(F/name, dpi=150); plt.close(fig); print("fig", name)


def trend(series, start):
    s = series[series.index >= start].dropna(); x = np.arange(len(s)); b, c = np.polyfit(x, np.log(s.values), 1)
    fit = pd.Series(np.exp(c+b*x), index=s.index); dev = (s/fit-1)*100
    per_year = 252 if len(s) > 2000 else 12
    return fit, dev, (np.exp(b*per_year)-1)*100


def era_stats(series, start):
    """percentile/median/p10/p90/extremes of a series inside [start, now]"""
    s = series[series.index >= start].dropna(); v = float(s.iloc[-1])
    return dict(now=v, pct=pr(s, v), median=float(s.median()), p10=float(s.quantile(.1)), p90=float(s.quantile(.9)),
                max=float(s.max()), max_date=str(s.idxmax().date()), min=float(s.min()), min_date=str(s.idxmin().date()), n=int(len(s)))


def era_lines(ax, series, key, x_end, label_prefix="", show_p10=True):
    """draw era median / p90 / p10 as segments from era start to now"""
    start, label, col = ERAS[key]; s = series[series.index >= start].dropna(); x0 = pd.Timestamp(start)
    ax.hlines(s.median(), x0, x_end, colors=col, linestyles="--", lw=1, label=f"{label_prefix}{label[:8]} 中位 {s.median():+.0f}%")
    ax.hlines(s.quantile(.9), x0, x_end, colors=col, linestyles=":", lw=1.2, label=f"{label[:8]} 90 分位 {s.quantile(.9):+.0f}%")
    if show_p10:
        ax.hlines(s.quantile(.1), x0, x_end, colors=col, linestyles=":", lw=.8)


# ===== 1. price vs era trend lines =====
S["trend"] = {}
fits = {}
for key, (start, label, col) in ERAS.items():
    fit, dev, cagr = trend(n, start); fits[key] = (fit, dev, cagr)
    st = era_stats(dev, start); st.update(cagr=cagr, peak2021=float(dev["2021"].max()) if dev.index[0] < pd.Timestamp("2021-01-01") else None,
                                          trough2022=float(dev["2022":"2023"].min()), peak2007=float(dev["2007"].max()) if dev.index[0] < pd.Timestamp("2007-01-01") else None)
    S["trend"][key] = st
fit85, dev85, cagr85 = trend(n, FULL); S["trend"]["FULL"] = dict(era_stats(dev85, FULL), cagr=cagr85)
# sensitivity of start date
sens = []
for key, (start, label, col) in ERAS.items():
    t0 = pd.Timestamp(start)
    pre_high = n[:t0].max()
    regain = n[t0:][n[t0:] >= pre_high].index[0]
    for name, s0 in [("危机底", t0), ("底后 1 年", t0 + pd.DateOffset(years=1)), ("底后 2 年", t0 + pd.DateOffset(years=2)), ("收复危机前高点", regain)]:
        fit, dev, cagr = trend(n, str(s0.date())); st = era_stats(dev, str(s0.date()))
        sens.append(dict(era=label[:8], start_name=name, start=str(s0.date()), cagr=cagr, dev=st["now"], pct=st["pct"], p90=st["p90"]))
S["sensitivity"] = sens

fig, axes = plt.subplots(3, 1, figsize=(10, 9.2), gridspec_kw={"height_ratios": [1.5, 1, 1]})
ax = axes[0]; s = n[n.index >= X0]
ax.semilogy(s.index, s.values, lw=.9, color=NAVY, label="纳指100 价格")
for key, (start, label, col) in ERAS.items():
    fit, dev, cagr = fits[key]; ax.semilogy(fit.index, fit.values, "--", lw=1.3, color=col, label=f"{label} 趋势线，年化 {cagr:.1f}%")
f85 = fit85[fit85.index >= X0]; ax.semilogy(f85.index, f85.values, ":", lw=1, color=GRAY, label=f"参照：1985 起趋势线，年化 {cagr85:.1f}%")
for d, t in [("2007-10-31", "2007 顶"), ("2009-03-09", "2009 底"), ("2021-11-19", "2021-11 顶"), ("2022-12-28", "2022 底")]:
    d = pd.Timestamp(d); ax.annotate(t, (d, n[:d].iloc[-1]), xytext=(0, 8 if "顶" in t else -14), textcoords="offset points", ha="center", fontsize=7.5, color=GRAY)
ax.plot([n.index[-1]], [n.iloc[-1]], "o", color=RED, ms=5); ax.annotate(f"{n.iloc[-1]:,.0f}", (n.index[-1], n.iloc[-1]), xytext=(6, -2), textcoords="offset points", color=RED, fontsize=8, fontweight="bold")
ax.set_title(f"维度 1 · 价格与危机后趋势线：纳指100 2002–{AS_OF[:4]}（对数坐标）"); ax.legend(loc="upper left")
for ax, key in zip(axes[1:], ERAS):
    start, label, col = ERAS[key]; fit, dev, cagr = fits[key]; st = S["trend"][key]
    ax.plot(dev.index, dev.values, lw=.9, color=col, label=f"偏离 {label} 趋势线")
    ax.axhline(0, color="k", lw=.7); ax.axhline(st["p90"], color=RED, ls=":", lw=1, label=f"本时代 90 分位 {st['p90']:+.0f}%"); ax.axhline(st["p10"], color=GREEN, ls=":", lw=1, label=f"10 分位 {st['p10']:+.0f}%")
    mark_now(ax, dev.index[-1], dev.iloc[-1]); ax.set_ylabel("%"); ax.legend(loc="upper left", ncol=3); ax.set_xlim(X0, n.index[-1] + pd.DateOffset(months=8))
save(fig, "01_era_trend.png")

# ===== 2. drawdowns & corrections inside each era =====
dd = (p/p.cummax()-1)*100
S["dd"] = {}
for key, (start, label, col) in ERAS.items():
    s = p[p.index >= start]; d = (s/s.cummax()-1)*100  # drawdown measured from era-internal highs
    # corrections: episodes with depth <= -10%
    below = d <= -10; eps = []; cur = None
    for dt_, flag in below.items():
        if flag and cur is None: cur = [dt_, dt_]
        elif flag: cur[1] = dt_
        elif cur is not None and (dt_ - cur[1]).days > 60: eps.append(cur); cur = None
    if cur is not None: eps.append(cur)
    corr = [dict(start=str(e[0].date()), end=str(e[1].date()), depth=float(d[e[0]:e[1]].min())) for e in eps]
    S["dd"][key] = dict(now=float(d.iloc[-1]), corrections=corr, n_corr=len(corr), max=float(d.min()), max_date=str(d.idxmin().date()),
                        share_within_5=float((d > -5).mean()*100), share_within_10=float((d > -10).mean()*100))
fig, ax = plt.subplots(figsize=(10, 3.8)); dds = dd[dd.index >= X0]
ax.fill_between(dds.index, dds.values, 0, color=NAVY, alpha=.3); ax.plot(dds.index, dds.values, lw=.6, color=NAVY)
for c in S["dd"]["A"]["corrections"]:
    if c["depth"] <= -15: ax.annotate(f"{c['depth']:.0f}%", (pd.Timestamp(c["start"]) + (pd.Timestamp(c["end"]) - pd.Timestamp(c["start"]))/2, c["depth"]), xytext=(0, -12), textcoords="offset points", ha="center", fontsize=7.5, color=RED)
for key, (start, label, col) in ERAS.items(): ax.axvline(pd.Timestamp(start), color=col, lw=1, ls="--", label=f"{label[:8]} 起算")
mark_now(ax, dds.index[-1], dds.iloc[-1], fmt="{:.1f}%"); ax.set_ylim(-60, 6); ax.set_ylabel("距前高 %"); ax.legend(loc="lower left")
ax.set_title(f"维度 2 · 回撤与调整：QQQ 2002–{AS_OF[:4]}（2009 起 ≥10% 的调整共 {S['dd']['B']['n_corr']} 次，最深 {S['dd']['B']['max']:.0f}%）")
save(fig, "02_era_drawdown.png")

# ===== 3. 200DMA inside eras =====
d200 = (n/n.rolling(200).mean()-1)*100
S["ma"] = {k: era_stats(d200, ERAS[k][0]) for k in ERAS}; S["ma"]["FULL"] = era_stats(d200, FULL)
fig, ax = plt.subplots(figsize=(10, 3.8)); s = d200[d200.index >= X0]
ax.plot(s.index, s.values, lw=.7, color=NAVY, label="纳指100 相对 200 日均线"); ax.axhline(0, color="k", lw=.7)
for k in ERAS: era_lines(ax, d200, k, n.index[-1])
mark_now(ax, s.index[-1], s.iloc[-1]); ax.set_ylabel("%"); ax.legend(loc="upper left", ncol=3); ax.set_title("维度 3 · 相对 200 日均线：参考线按时代分别计算")
save(fig, "03_era_ma200.png")

# ===== 4. rolling returns inside eras =====
S["roll"] = {}
fig, axes = plt.subplots(3, 1, figsize=(10, 7.4), sharex=True)
for ax, yrs in zip(axes, (1, 3, 5)):
    tr = ((a/a.shift(252*yrs)-1)*100).dropna(); S["roll"][yrs] = {}
    for k in ERAS:
        start = pd.Timestamp(ERAS[k][0]) + pd.DateOffset(years=yrs)  # windows that START after the trough
        st = era_stats(tr, str(start.date())); st["neg_share"] = float((tr[tr.index >= start] < 0).mean()*100); st["window_start"] = str(start.date()); S["roll"][yrs][k] = st
    S["roll"][yrs]["FULL"] = dict(era_stats(tr, "1999-01-01"), neg_share=float((tr < 0).mean()*100))
    s = tr[tr.index >= X0]; ax.plot(s.index, s.values, lw=.8, color=NAVY, label=f"QQQ 过去 {yrs} 年总回报（含分红）"); ax.axhline(0, color="k", lw=.7)
    for k in ERAS:
        start = pd.Timestamp(ERAS[k][0]) + pd.DateOffset(years=yrs); ss = tr[tr.index >= start]; col = ERAS[k][2]
        ax.hlines(ss.median(), start, tr.index[-1], colors=col, linestyles="--", lw=1, label=f"{ERAS[k][1][:8]} 中位 {ss.median():+.0f}%")
        ax.hlines(ss.quantile(.9), start, tr.index[-1], colors=col, linestyles=":", lw=1.2, label=f"90 分位 {ss.quantile(.9):+.0f}%")
    mark_now(ax, s.index[-1], s.iloc[-1]); ax.legend(loc="upper left", ncol=5); ax.set_ylabel("%")
axes[0].set_title("维度 4 · 滚动总回报：只统计危机底之后才开始的窗口")
save(fig, "04_era_rolling.png")

# ===== 5. forward PE inside eras =====
fpe = pd.read_csv(D/"ndx_forward_pe_weekly.csv", parse_dates=["date"]).set_index("date").value
j = json.load(open(D/"hom_ndx_forward_pe.json", encoding="utf-8"))
fown = pd.DataFrame(j["forwardOwn"]); fown["date"] = pd.to_datetime(fown["date"]); fown = fown.set_index("date").value
tpe = pd.read_csv(D/"ndx_trailing_pe_daily.csv", parse_dates=["date"]).set_index("date").value
fnow = float(fown.iloc[-1])
S["fpe"] = {k: dict(era_stats(fpe, ERAS[k][0]), now=fnow, pct=pr(fpe[fpe.index >= ERAS[k][0]], fnow)) for k in ERAS}
S["fpe"]["meta"] = dict(now_daily=fnow, now_daily_date=str(fown.index[-1].date()), now_weekly=float(fpe.iloc[-1]), trailing=float(tpe.iloc[-1]), implied=float((tpe.iloc[-1]/fnow-1)*100),
                        peak2020=float(fpe["2020":"2021"].max()), peak2020_date=str(fpe["2020":"2021"].idxmax().date()), trough2022=float(fpe["2022":"2023"].min()), trough2008=float(fpe["2008":"2009"].min()),
                        ye2021=float(fpe["2021-12"].iloc[-1]), peak2007=float(fpe["2007"].max()), min2011=float(fpe["2011":"2012"].min()))
fig, ax = plt.subplots(figsize=(10, 4.2)); s = fpe[fpe.index >= X0]
ax.plot(s.index, s.values, lw=.9, color=NAVY, label="纳指100 前瞻 12 个月 PE（周频）"); ax.plot(fown.index, fown.values, lw=1.2, color=NAVY, alpha=.6)
for k in ERAS:
    start, label, col = ERAS[k]; ss = fpe[fpe.index >= start]
    ax.hlines(ss.median(), pd.Timestamp(start), fown.index[-1], colors=col, linestyles="--", lw=1, label=f"{label[:8]} 中位 {ss.median():.1f}x")
    ax.hlines(ss.quantile(.9), pd.Timestamp(start), fown.index[-1], colors=col, linestyles=":", lw=1.2, label=f"90 分位 {ss.quantile(.9):.1f}x")
for d, t, dy in [("2020-08-28", "2020-08 高 29.6x", 8), ("2022-10-14", "2022-10 低 18.6x", -14), ("2008-11-21", "2008-11 低 12.0x", -14), ("2007-10-31", "2007 高 23.5x", 8)]:
    d = pd.Timestamp(d); ax.annotate(t, (d, fpe[:d].iloc[-1]), xytext=(0, dy), textcoords="offset points", ha="center", fontsize=7.5, color=GRAY)
mark_now(ax, fown.index[-1], fnow, fmt="{:.1f}x"); ax.set_ylim(8, 36); ax.set_ylabel("倍"); ax.legend(loc="upper left", ncol=2)
ax.set_title(f"维度 5 · 估值：纳指100 前瞻 PE，参考线按时代分别计算（2002–{AS_OF[:4]}）")
save(fig, "05_era_forward_pe.png")

# ===== 6. CAPE inside eras =====
cape = pd.read_csv(D/"multpl_shiller_pe.csv", parse_dates=["date"]).set_index("date").value
S["cape"] = {k: era_stats(cape, ERAS[k][0]) for k in ERAS}; S["cape"]["FULL"] = era_stats(cape, "1871-01-01"); S["cape"]["since1990"] = era_stats(cape, "1990-01-01")
fig, ax = plt.subplots(figsize=(10, 3.8)); s = cape[cape.index >= X0]
ax.plot(s.index, s.values, lw=1, color=NAVY, label="标普500 席勒 CAPE")
for k in ERAS:
    start, label, col = ERAS[k]; ss = cape[cape.index >= start]
    ax.hlines(ss.median(), pd.Timestamp(start), cape.index[-1], colors=col, linestyles="--", lw=1, label=f"{label[:8]} 中位 {ss.median():.1f}")
    ax.hlines(ss.quantile(.9), pd.Timestamp(start), cape.index[-1], colors=col, linestyles=":", lw=1.2, label=f"90 分位 {ss.quantile(.9):.1f}")
ax.axhline(cape.median(), color=GRAY, ls="--", lw=.8, label=f"参照：1881 起中位 {cape.median():.1f}")
mark_now(ax, s.index[-1], s.iloc[-1], fmt="{:.1f}"); ax.set_ylim(10, 46); ax.legend(loc="upper left", ncol=2); ax.set_title(f"维度 6 · 大盘估值背景：CAPE 2002–{AS_OF[:4]}")
save(fig, "06_era_cape.png")

# ===== 7. QQQ/SPY inside eras =====
rel = (qqq.adj_close/spy.adj_close).dropna(); S["rel"] = {}
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 5.8), sharex=True); s = rel[rel.index >= X0]
ax1.plot(s.index, s.values, lw=.9, color=NAVY, label="QQQ / SPY（含分红复权价之比）")
for k in ERAS:
    start, label, col = ERAS[k]; fit, dev, cagr = trend(rel, start); st = era_stats(dev, start); st["cagr"] = cagr; st["ratio_now"] = float(rel.iloc[-1]); S["rel"][k] = st
    ax1.plot(fit.index, fit.values, "--", lw=1.2, color=col, label=f"{label[:8]} 趋势，年化 {cagr:+.1f}%")
    ax2.plot(dev.index, dev.values, lw=.9, color=col, label=f"偏离 {label[:8]} 趋势"); ax2.hlines(st["p90"], pd.Timestamp(start), rel.index[-1], colors=col, linestyles=":", lw=1.2)
    mark_now(ax2, dev.index[-1], dev.iloc[-1], color=col, dy=(-14 if k == "B" else 0))
mark_now(ax1, s.index[-1], s.iloc[-1], fmt="{:.2f}"); ax1.legend(loc="upper left"); ax1.set_title(f"维度 7 · 科技相对大盘：QQQ/SPY 2002–{AS_OF[:4]}")
ax2.axhline(0, color="k", lw=.7); ax2.legend(loc="upper left"); ax2.set_ylabel("%（点线 = 各时代 90 分位）")
save(fig, "07_era_qqq_spy.png")

# ===== 8. NDX / M2 inside eras =====
m2 = pd.read_csv(D/"us_m2_monthly.csv"); m2["dt"] = pd.to_datetime(m2.month); m2 = m2.set_index("dt").m2_sa_usd_bn
nm = n.resample("MS").last(); nm.index = nm.index.normalize(); ratio = (nm/m2).dropna(); S["liq"] = {}
fig, ax = plt.subplots(figsize=(10, 3.8)); s = ratio[ratio.index >= X0]*1000
ax.semilogy(s.index, s.values, lw=1, color=NAVY, label="纳指100 ÷ M2（×1000）")
for k in ERAS:
    start, label, col = ERAS[k]; fit, dev, cagr = trend(ratio, start); st = era_stats(dev, start); st["cagr"] = cagr; S["liq"][k] = st
    ax.semilogy(fit.index, fit.values*1000, "--", lw=1.2, color=col, label=f"{label[:8]} 趋势，年化 {cagr:.1f}%；当前偏离 {dev.iloc[-1]:+.0f}%（{st['pct']:.0f} 分位）")
S["liq"]["m2_asof"] = str(m2.index[-1].date())
mark_now(ax, s.index[-1], s.iloc[-1], fmt="{:.0f}"); ax.legend(loc="upper left"); ax.set_title(f"维度 8 · 按货币存量缩放：纳指100 ÷ M2（M2 至 {m2.index[-1].strftime('%Y-%m')}）")
save(fig, "08_era_ndx_m2.png")

# ===== 9. vol inside eras =====
vol = (np.log(a).diff().rolling(60).std()*np.sqrt(252)*100).dropna(); S["vol"] = {k: era_stats(vol, ERAS[k][0]) for k in ERAS}
fig, ax = plt.subplots(figsize=(10, 3.2)); s = vol[vol.index >= X0]
ax.plot(s.index, s.values, lw=.7, color=NAVY, label="QQQ 60 日实现波动率（年化）")
for k in ERAS:
    start, label, col = ERAS[k]; ss = vol[vol.index >= start]; ax.hlines(ss.median(), pd.Timestamp(start), vol.index[-1], colors=col, linestyles="--", lw=1, label=f"{label[:8]} 中位 {ss.median():.0f}%")
mark_now(ax, s.index[-1], s.iloc[-1], fmt="{:.0f}%"); ax.legend(loc="upper left", ncol=3); ax.set_ylabel("%"); ax.set_title("维度 9 · 实现波动率")
save(fig, "09_era_vol.png")


# ===== episodes inside era B (2009-) : what followed similar readings =====
def episodes(flag, gap=365):
    dates = flag[flag].index; eps = []
    for d in dates:
        if not eps or (d - eps[-1][-1]).days > gap: eps.append([d, d])
        else: eps[-1][-1] = d
    return eps


def fwd(series, d, yrs):
    i = series.index.get_indexer([d], method="nearest")[0]; jj = i + 252*yrs
    return float((series.iloc[jj]/series.iloc[i]-1)*100) if jj < len(series) else None


def mdd_after(series, d, yrs):
    i = series.index.get_indexer([d], method="nearest")[0]; s = series.iloc[i:i+252*yrs]
    return float((s/s.cummax()-1).min()*100)


tbl = []
for key in ERAS:
    start, label, col = ERAS[key]; fit, dev, cagr = fits[key]; tr3 = ((a/a.shift(756)-1)*100).dropna(); tr3 = tr3[tr3.index >= pd.Timestamp(start) + pd.DateOffset(years=3)]
    fe = fpe[fpe.index >= start]; d2 = d200[d200.index >= start]
    conds = [("价格高出本时代趋势线 > 90 分位", dev > dev.quantile(.9), 365), ("3 年回报 > 本时代 90 分位", tr3 > tr3.quantile(.9), 365),
             ("前瞻 PE > 本时代 90 分位", fe > fe.quantile(.9), 180), ("高出 200 日线 > 本时代 90 分位", d2 > d2.quantile(.9), 180)]
    for name, flag, gap in conds:
        for s_, e_ in episodes(flag, gap):
            tbl.append(dict(era=label[:8], cond=name, start=str(s_.date()), end=str(e_.date()), r1=fwd(a, s_, 1), r3=fwd(a, s_, 3), r5=fwd(a, s_, 5), mdd2=mdd_after(a, s_, 2)))
S["episodes"] = tbl; pd.DataFrame(tbl).to_csv(HERE/"similar_episodes_by_era.csv", index=False, encoding="utf-8-sig")

# ===== era summary: CAGR, max dd, corrections =====
S["era_summary"] = {}
for key in ERAS:
    start = ERAS[key][0]; s = a[a.index >= start]; yrs = (s.index[-1]-s.index[0]).days/365.25
    S["era_summary"][key] = dict(years=yrs, qqq_total=float((s.iloc[-1]/s.iloc[0]-1)*100), qqq_cagr=float(((s.iloc[-1]/s.iloc[0])**(1/yrs)-1)*100),
                                 ndx_trend_cagr=S["trend"][key]["cagr"], max_dd=S["dd"][key]["max"], n_corr=S["dd"][key]["n_corr"])

# ===== dashboard: value | 1985 pct | era A pct | era B pct =====
def row(k, v, full, A, B, ref):
    return dict(k=k, v=v, full=full, A=A, B=B, ref=ref)


S["dashboard"] = [
    row("偏离趋势线（各自样本拟合）", f"1985 起 {S['trend']['FULL']['now']:+.0f}% / 2002 起 {S['trend']['A']['now']:+.0f}% / 2009 起 {S['trend']['B']['now']:+.0f}%", S["trend"]["FULL"]["pct"], S["trend"]["A"]["pct"], S["trend"]["B"]["pct"],
        f"2009 起趋势年化 {S['trend']['B']['cagr']:.1f}%，2021 顶 {S['trend']['B']['peak2021']:+.0f}%"),
    row("相对 200 日均线", f"{S['ma']['A']['now']:+.0f}%", S["ma"]["FULL"]["pct"], S["ma"]["A"]["pct"], S["ma"]["B"]["pct"], f"2009 起中位 {S['ma']['B']['median']:+.0f}% / 90 分位 {S['ma']['B']['p90']:+.0f}%"),
    row("过去 1 年总回报", f"{S['roll'][1]['FULL']['now']:+.0f}%", S["roll"][1]["FULL"]["pct"], S["roll"][1]["A"]["pct"], S["roll"][1]["B"]["pct"], f"2009 起中位 {S['roll'][1]['B']['median']:+.0f}%"),
    row("过去 3 年总回报", f"{S['roll'][3]['FULL']['now']:+.0f}%", S["roll"][3]["FULL"]["pct"], S["roll"][3]["A"]["pct"], S["roll"][3]["B"]["pct"], f"2009 起中位 {S['roll'][3]['B']['median']:+.0f}% / 90 分位 {S['roll'][3]['B']['p90']:+.0f}%"),
    row("过去 5 年总回报", f"{S['roll'][5]['FULL']['now']:+.0f}%", S["roll"][5]["FULL"]["pct"], S["roll"][5]["A"]["pct"], S["roll"][5]["B"]["pct"], f"2009 起中位 {S['roll'][5]['B']['median']:+.0f}%，负窗口 {S['roll'][5]['B']['neg_share']:.0f}%"),
    row("纳指100 前瞻 PE", f"{fnow:.1f}x", pr(fpe, fnow), S["fpe"]["A"]["pct"], S["fpe"]["B"]["pct"], f"2009 起中位 {S['fpe']['B']['median']:.1f}x / 90 分位 {S['fpe']['B']['p90']:.1f}x"),
    row("标普500 CAPE", f"{S['cape']['A']['now']:.1f}", S["cape"]["FULL"]["pct"], S["cape"]["A"]["pct"], S["cape"]["B"]["pct"], f"2009 起中位 {S['cape']['B']['median']:.1f} / 90 分位 {S['cape']['B']['p90']:.1f}"),
    row("QQQ/SPY 偏离趋势（各自拟合）", f"2002 起 {S['rel']['A']['now']:+.0f}% / 2009 起 {S['rel']['B']['now']:+.0f}%", None, S["rel"]["A"]["pct"], S["rel"]["B"]["pct"], f"2009 起趋势年化 {S['rel']['B']['cagr']:+.1f}%"),
    row("纳指100 ÷ M2 偏离趋势（各自拟合）", f"2002 起 {S['liq']['A']['now']:+.0f}% / 2009 起 {S['liq']['B']['now']:+.0f}%", None, S["liq"]["A"]["pct"], S["liq"]["B"]["pct"], f"2009 起趋势年化 {S['liq']['B']['cagr']:.1f}%"),
    row("60 日实现波动率", f"{S['vol']['A']['now']:.0f}%", None, S["vol"]["A"]["pct"], S["vol"]["B"]["pct"], f"2009 起中位 {S['vol']['B']['median']:.0f}%"),
]
json.dump(S, open(HERE/"stats_era.json", "w", encoding="utf-8"), indent=2, ensure_ascii=False, default=float)
print(json.dumps({k: S[k] for k in ("trend", "era_summary", "sensitivity", "dd")}, indent=1, ensure_ascii=False, default=float)[:6000])
print(pd.DataFrame(S["dashboard"]).to_string()); print(pd.DataFrame(tbl).to_string())
