#!/usr/bin/env python
"""Multi-dimension 'is QQQ high' charts. Reads data/, writes fig/*.png + stats.json.
Every chart = full history line + reference (trend / median / percentile band) + current point."""
import json, sys, numpy as np, pandas as pd
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass
from pathlib import Path
HERE = Path(__file__).resolve().parent; D = HERE/"data"; F = HERE/"fig"; F.mkdir(exist_ok=True)
plt.rcParams.update({"font.family": ["Microsoft YaHei", "SimHei", "DejaVu Sans"], "axes.unicode_minus": False,
                     "figure.dpi": 150, "axes.grid": True, "grid.alpha": .3, "axes.spines.top": False, "axes.spines.right": False,
                     "font.size": 9, "legend.fontsize": 8, "axes.titlesize": 11})
NAVY, ORANGE, RED, GREEN, GRAY, PURPLE = "#1f4e79", "#e36c09", "#c00000", "#2e7d32", "#7f7f7f", "#6a3d9a"
S = {}  # stats


def pr(s, v):
    s = s.dropna(); return float((s < v).mean()*100)


def load(l):
    return pd.read_csv(D/f"{l}_daily.csv", parse_dates=["date"]).set_index("date")


qqq, ndx, spy, gspc = load("QQQ"), load("NDX"), load("SPY"), load("GSPC")
n, a, p = ndx.close, qqq.adj_close, qqq.close
AS_OF = str(p.index[-1].date()); S["as_of"] = AS_OF; S["qqq_close"] = float(p.iloc[-1]); S["ndx_close"] = float(n.iloc[-1])


def mark_now(ax, x, y, fmt="{:+.0f}%", color=RED, dx=0, dy=0):
    ax.plot([x], [y], "o", color=color, ms=5, zorder=5)
    ax.annotate(fmt.format(y), (x, y), xytext=(6+dx, 4+dy), textcoords="offset points", color=color, fontsize=8, fontweight="bold")


def save(fig, name):
    fig.tight_layout(); fig.savefig(F/name, dpi=150); plt.close(fig); print("fig", name)


def trend(series, start):
    s = series[series.index >= start].dropna(); x = np.arange(len(s)); b, c = np.polyfit(x, np.log(s.values), 1)
    fit = pd.Series(np.exp(c+b*x), index=s.index); dev = (s/fit-1)*100; cagr = (np.exp(b*252)-1)*100
    return fit, dev, cagr


# ---------- Fig 1: NDX log price + trend lines ----------
fit85, dev85, cagr85 = trend(n, "1985-10-01"); fit09, dev09, cagr09 = trend(n, "2009-03-09")
fig, ax = plt.subplots(figsize=(10, 4.4))
ax.semilogy(n.index, n.values, lw=.9, color=NAVY, label="纳指100 (NDX) 价格")
ax.semilogy(fit85.index, fit85.values, "--", lw=1.2, color=RED, label=f"1985 起对数趋势线，年化 {cagr85:.1f}%")
ax.semilogy(fit09.index, fit09.values, "--", lw=1.2, color=ORANGE, label=f"2009 起对数趋势线，年化 {cagr09:.1f}%")
for d, t in [("2000-03-27", "2000-03 顶"), ("2002-10-07", "2002 底"), ("2009-03-09", "2009 底"), ("2021-11-19", "2021-11 顶"), ("2022-12-28", "2022 底")]:
    d = pd.Timestamp(d); ax.annotate(t, (d, n[:d].iloc[-1]), xytext=(0, 8 if "顶" in t else -14), textcoords="offset points", ha="center", fontsize=7.5, color=GRAY)
ax.plot([n.index[-1]], [n.iloc[-1]], "o", color=RED, ms=5)
ax.annotate(f"{n.iloc[-1]:,.0f}", (n.index[-1], n.iloc[-1]), xytext=(6, -2), textcoords="offset points", color=RED, fontsize=8, fontweight="bold")
ax.set_title(f"维度 1 · 价格与长期趋势：纳指100 1985–{AS_OF[:4]}（对数坐标）"); ax.legend(loc="upper left"); ax.set_ylabel("指数点位（对数）")
save(fig, "01_ndx_log_trend.png")
S["trend85"] = dict(dev=float(dev85.iloc[-1]), pct=pr(dev85, dev85.iloc[-1]), p90=float(dev85.quantile(.9)), median=float(dev85.median()), cagr=cagr85,
                    peak2000=float(dev85.max()), peak2000_date=str(dev85.idxmax().date()), peak2021=float(dev85["2021"].max()))
S["trend09"] = dict(dev=float(dev09.iloc[-1]), pct=pr(dev09, dev09.iloc[-1]), p90=float(dev09.quantile(.9)), median=float(dev09.median()), cagr=cagr09,
                    peak2021=float(dev09.max()), peak2021_date=str(dev09.idxmax().date()), trough2022=float(dev09["2022":"2023"].min()))

# ---------- Fig 2: deviation from trend ----------
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 5.6))
ax1.plot(dev85.index, dev85.values, lw=.9, color=NAVY, label="偏离 1985 起趋势线")
ax1.axhline(0, color="k", lw=.7)
ax1.axhline(dev85.quantile(.9), color=RED, ls=":", lw=1, label=f"90 分位 {dev85.quantile(.9):+.0f}%")
ax1.axhline(dev85.quantile(.1), color=GREEN, ls=":", lw=1, label=f"10 分位 {dev85.quantile(.1):+.0f}%")
mark_now(ax1, dev85.index[-1], dev85.iloc[-1]); ax1.set_ylabel("%"); ax1.set_title("维度 1 · 偏离趋势线的幅度（%）"); ax1.legend(loc="upper left")
ax2.plot(dev09.index, dev09.values, lw=.9, color=ORANGE, label="偏离 2009 起趋势线")
ax2.axhline(0, color="k", lw=.7)
ax2.axhline(dev09.quantile(.9), color=RED, ls=":", lw=1, label=f"90 分位 {dev09.quantile(.9):+.0f}%")
ax2.axhline(dev09.quantile(.1), color=GREEN, ls=":", lw=1, label=f"10 分位 {dev09.quantile(.1):+.0f}%")
mark_now(ax2, dev09.index[-1], dev09.iloc[-1]); ax2.set_ylabel("%"); ax2.legend(loc="upper left")
save(fig, "02_trend_deviation.png")

# ---------- Fig 3: drawdown ----------
dd = (p/p.cummax()-1)*100
EPIS = [("2000-03-01", "2002-12-31", "2000-02"), ("2007-10-01", "2009-06-30", "2008-09"), ("2020-02-01", "2020-04-30", "2020"), ("2021-11-01", "2023-01-31", "2022")]
fig, ax = plt.subplots(figsize=(10, 3.8))
ax.fill_between(dd.index, dd.values, 0, color=NAVY, alpha=.35); ax.plot(dd.index, dd.values, lw=.6, color=NAVY)
for a_, b_, t in EPIS:
    seg = dd[a_:b_]; ax.annotate(f"{t}\n{seg.min():.0f}%", (seg.idxmin(), seg.min()), xytext=(0, -16), textcoords="offset points", ha="center", fontsize=7.5, color=RED)
mark_now(ax, dd.index[-1], dd.iloc[-1], fmt="{:.1f}%"); ax.set_ylim(-90, 8); ax.set_ylabel("距前高 %")
ax.set_title(f"维度 2 · 距历史最高点的回撤：QQQ 1999–{AS_OF[:4]}（当前 {dd.iloc[-1]:.1f}%，前高 {p.max():.2f} @ {p.idxmax().date()}）")
save(fig, "03_drawdown.png")
S["drawdown"] = dict(now=float(dd.iloc[-1]), ath=float(p.max()), ath_date=str(p.idxmax().date()),
                     episodes={t: float(dd[a_:b_].min()) for a_, b_, t in EPIS},
                     days_within_5pct_of_ath_share=float((dd > -5).mean()*100))

# ---------- Fig 4: 200DMA ----------
d200 = (n/n.rolling(200).mean()-1)*100; d50 = (n/n.rolling(50).mean()-1)*100
fig, ax = plt.subplots(figsize=(10, 3.8))
ax.plot(d200.index, d200.values, lw=.7, color=NAVY, label="NDX 相对 200 日均线")
ax.axhline(0, color="k", lw=.7)
ax.axhline(d200.quantile(.9), color=RED, ls=":", lw=1, label=f"90 分位 {d200.quantile(.9):+.0f}%")
ax.axhline(d200.quantile(.1), color=GREEN, ls=":", lw=1, label=f"10 分位 {d200.quantile(.1):+.0f}%")
ax.axhline(d200.median(), color=GRAY, ls="--", lw=.8, label=f"中位 {d200.median():+.0f}%")
mark_now(ax, d200.index[-1], d200.iloc[-1]); ax.set_ylabel("%"); ax.set_title("维度 3 · 短中期动能：纳指100 相对 200 日均线（1986–）"); ax.legend(loc="upper left", ncol=4)
save(fig, "04_ma200.png")
S["ma"] = dict(d200=float(d200.iloc[-1]), d200_pct=pr(d200, d200.iloc[-1]), d200_median=float(d200.median()), d200_p90=float(d200.quantile(.9)), d200_max=float(d200.max()),
               d50=float(d50.iloc[-1]), d50_pct=pr(d50, d50.iloc[-1]))

# ---------- Fig 5: rolling returns ----------
fig, axes = plt.subplots(3, 1, figsize=(10, 7.2), sharex=True); S["roll"] = {}
for ax, yrs, col in zip(axes, (1, 3, 5), (NAVY, ORANGE, PURPLE)):
    tr = (a/a.shift(252*yrs)-1)*100; trd = tr.dropna()
    ax.plot(trd.index, trd.values, lw=.8, color=col, label=f"QQQ 过去 {yrs} 年总回报（含分红）")
    ax.axhline(0, color="k", lw=.7)
    ax.axhline(trd.median(), color=GRAY, ls="--", lw=.8, label=f"中位 {trd.median():+.0f}%")
    ax.axhline(trd.quantile(.9), color=RED, ls=":", lw=1, label=f"90 分位 {trd.quantile(.9):+.0f}%")
    mark_now(ax, trd.index[-1], trd.iloc[-1]); ax.legend(loc="upper left", ncol=3); ax.set_ylabel("%")
    S["roll"][yrs] = dict(now=float(trd.iloc[-1]), pct=pr(trd, trd.iloc[-1]), pct09=pr(trd["2009-03-09":], trd.iloc[-1]), median=float(trd.median()), p90=float(trd.quantile(.9)),
                          max=float(trd.max()), max_date=str(trd.idxmax().date()), min=float(trd.min()), min_date=str(trd.idxmin().date()))
axes[0].set_title(f"维度 4 · 滚动总回报：QQQ 1 / 3 / 5 年窗口（2000–{AS_OF[:4]}）")
save(fig, "05_rolling_returns.png")

# ---------- Fig 6: NDX forward P/E ----------
fpe = pd.read_csv(D/"ndx_forward_pe_weekly.csv", parse_dates=["date"]).set_index("date").value
j = json.load(open(D/"hom_ndx_forward_pe.json", encoding="utf-8"))
fown = pd.DataFrame(j["forwardOwn"]); fown["date"] = pd.to_datetime(fown["date"]); fown = fown.set_index("date").value
tpe = pd.read_csv(D/"ndx_trailing_pe_daily.csv", parse_dates=["date"]).set_index("date").value
siblis = pd.Series({pd.Timestamp("2016-12-31"): 23.08, pd.Timestamp("2017-12-31"): 25.84, pd.Timestamp("2018-12-31"): 20.75, pd.Timestamp("2019-12-31"): 26.47,
                    pd.Timestamp("2020-12-31"): 39.72, pd.Timestamp("2021-12-31"): 38.00, pd.Timestamp("2022-12-31"): 23.72, pd.Timestamp("2023-12-31"): 30.25,
                    pd.Timestamp("2024-12-31"): 32.36, pd.Timestamp("2025-12-31"): 32.32, pd.Timestamp("2026-08-31"): 34.24})
fpe_plot = fpe[fpe.index >= "2002-01-01"]  # 2001 earnings-collapse spike (82x) distorts the axis; stated in text
fig, ax = plt.subplots(figsize=(10, 4.2))
ax.plot(fpe_plot.index, fpe_plot.values, lw=.9, color=NAVY, label="纳指100 前瞻 12 个月 PE（周频，一致预期）")
ax.plot(fown.index, fown.values, lw=1.2, color=NAVY, alpha=.6)
ax.plot(siblis.index, siblis.values, "s", ms=4, color=ORANGE, label="滚动 PE 年末值（Siblis Research）")
ax.plot(tpe.index, tpe.values, lw=1, color=ORANGE, alpha=.8, label="滚动 PE 日频（2026-05 起）")
m_all = fpe.median(); m10 = fpe["2016-10":].mean()
ax.axhline(m_all, color=GRAY, ls="--", lw=.8, label=f"2001 起中位 {m_all:.1f}x"); ax.axhline(m10, color=RED, ls=":", lw=1, label=f"近 10 年均值 {m10:.1f}x")
for d, t, dy in [("2020-08-28", "2020-08 高 29.6x", 8), ("2022-10-14", "2022-10 低 18.6x", -14), ("2008-11-21", "2008-11 低 12.0x", -14), ("2007-10-31", "2007 高 23.5x", 8)]:
    d = pd.Timestamp(d); v = fpe[:d].iloc[-1]; ax.annotate(t, (d, v), xytext=(0, dy), textcoords="offset points", ha="center", fontsize=7.5, color=GRAY)
mark_now(ax, fown.index[-1], fown.iloc[-1], fmt="{:.1f}x"); mark_now(ax, tpe.index[-1], tpe.iloc[-1], fmt="{:.1f}x", color=ORANGE, dy=-12)
ax.set_ylim(8, 45); ax.set_ylabel("倍"); ax.set_title(f"维度 5 · 估值：纳指100 前瞻 PE 2002–{AS_OF[:4]}（2001 年盈利塌陷期峰值 82x 未画）"); ax.legend(loc="upper left", ncol=2)
save(fig, "06_ndx_forward_pe.png")
S["fpe"] = dict(now_weekly=float(fpe.iloc[-1]), now_weekly_date=str(fpe.index[-1].date()), now_daily=float(fown.iloc[-1]), now_daily_date=str(fown.index[-1].date()),
                trailing_now=float(tpe.iloc[-1]), trailing_date=str(tpe.index[-1].date()), median=float(m_all), mean10=float(m10), mean5=float(fpe["2021-10":].mean()),
                median_since2010=float(fpe["2010":].median()), pct_since2001=pr(fpe, fpe.iloc[-1]), pct_since2010=pr(fpe["2010":], fpe.iloc[-1]),
                peak2020=float(fpe["2020":"2021"].max()), peak2020_date=str(fpe["2020":"2021"].idxmax().date()),
                trough2022=float(fpe["2022":"2023"].min()), trough2008=float(fpe["2008":"2009"].min()), peak2001=float(fpe.max()), ye2021=float(fpe["2021-12"].iloc[-1]),
                implied_eps_growth=float((tpe.iloc[-1]/fown.iloc[-1]-1)*100), siblis_ye={str(k.date()): float(v) for k, v in siblis.items()})

# ---------- Fig 7: CAPE + S&P PE ----------
cape = pd.read_csv(D/"multpl_shiller_pe.csv", parse_dates=["date"]).set_index("date").value
spe = pd.read_csv(D/"multpl_sp500_pe.csv", parse_dates=["date"]).set_index("date").value
fig, ax = plt.subplots(figsize=(10, 4.2))
ax.plot(cape.index, cape.values, lw=.9, color=NAVY, label="标普500 席勒 CAPE（10 年通胀调整盈利）")
ax.plot(spe.index, spe.values, lw=.7, color=ORANGE, alpha=.7, label="标普500 滚动 PE（2009 年因盈利塌陷冲到 120x，已截断）")
ax.axhline(cape.median(), color=GRAY, ls="--", lw=.8, label=f"CAPE 1881 起中位 {cape.median():.1f}")
ax.axhline(cape["1990":].median(), color=RED, ls=":", lw=1, label=f"CAPE 1990 起中位 {cape['1990':].median():.1f}")
for d, t, dy in [("1929-09-01", "1929 高 32.6", 8), ("1999-12-01", "1999-12 高 44.2", 8), ("2021-11-01", "2021-11 高 38.6", 8), ("2009-03-01", "2009 低 13.3", -14), ("1982-07-01", "1982 低 6.6", -14)]:
    d = pd.Timestamp(d); ax.annotate(t, (d, cape[:d].iloc[-1]), xytext=(0, dy), textcoords="offset points", ha="center", fontsize=7.5, color=GRAY)
mark_now(ax, cape.index[-1], cape.iloc[-1], fmt="{:.1f}"); ax.set_ylim(0, 50); ax.set_ylabel("倍")
ax.set_title(f"维度 6 · 大盘估值背景：标普500 CAPE 1881–{AS_OF[:4]}（multpl.com，基于 Shiller 数据）"); ax.legend(loc="upper left")
save(fig, "07_cape.png")
S["cape"] = dict(now=float(cape.iloc[-1]), date=str(cape.index[-1].date()), pct=pr(cape, cape.iloc[-1]), median=float(cape.median()), median1990=float(cape["1990":].median()),
                 peak2000=float(cape["1999":"2000"].max()), peak2000_date=str(cape["1999":"2000"].idxmax().date()), peak2021=float(cape["2021":"2022"].max()), peak1929=float(cape["1929"].max()),
                 sp_pe_now=float(spe.iloc[-1]), sp_pe_date=str(spe.index[-1].date()), sp_pe_median=float(spe.median()), sp_pe_pct=pr(spe, spe.iloc[-1]))

# ---------- Fig 8: QQQ / SPY ratio ----------
rel = (qqq.adj_close/spy.adj_close).dropna(); rfit, rdev, rcagr = trend(rel, "1999-03-10")
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 5.6), sharex=True)
ax1.plot(rel.index, rel.values, lw=.9, color=NAVY, label="QQQ / SPY（含分红复权价之比）")
ax1.plot(rfit.index, rfit.values, "--", lw=1, color=RED, label=f"1999 起对数趋势，年化 {rcagr:+.1f}%")
mark_now(ax1, rel.index[-1], rel.iloc[-1], fmt="{:.2f}"); ax1.legend(loc="upper left"); ax1.set_title(f"维度 7 · 科技相对大盘：QQQ/SPY 1999–{AS_OF[:4]}")
ax2.plot(rdev.index, rdev.values, lw=.9, color=ORANGE, label="比值偏离趋势线 %"); ax2.axhline(0, color="k", lw=.7)
ax2.axhline(rdev.quantile(.9), color=RED, ls=":", lw=1, label=f"90 分位 {rdev.quantile(.9):+.0f}%")
ax2.axhline(rdev.quantile(.1), color=GREEN, ls=":", lw=1, label=f"10 分位 {rdev.quantile(.1):+.0f}%")
mark_now(ax2, rdev.index[-1], rdev.iloc[-1]); ax2.set_ylim(-60, 80); ax2.legend(loc="upper left"); ax2.set_ylabel("%")
save(fig, "08_qqq_spy_ratio.png")
S["rel"] = dict(now=float(rel.iloc[-1]), dev=float(rdev.iloc[-1]), pct=pr(rdev, rdev.iloc[-1]), p90=float(rdev.quantile(.9)), cagr=rcagr,
                peak2000=float(rel[:"2000-12-31"].max()), peak2000_date=str(rel[:"2000-12-31"].idxmax().date()),
                trough2002=float(rel["2001":"2009"].min()), trough2002_date=str(rel["2001":"2009"].idxmin().date()), dev_peak2000=float(rdev.max()))

# ---------- Fig 9: liquidity & inflation ----------
m2 = pd.read_csv(D/"us_m2_monthly.csv"); m2["dt"] = pd.to_datetime(m2.month); m2 = m2.set_index("dt").m2_sa_usd_bn
cpi = pd.read_csv(D/"us_cpi_monthly.csv"); cpi["dt"] = pd.to_datetime(cpi.month); cpi = cpi.set_index("dt").cpi_u_nsa
nm = n.resample("MS").last(); nm.index = nm.index.normalize()
base = pd.Timestamp("2008-01-01")


def idx(s):
    return s/s[base]*100


real = (nm/cpi).dropna()
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6))
ax1.semilogy(nm[base:].index, idx(nm)[base:], lw=1, color=NAVY, label="纳指100 名义")
ax1.semilogy(m2[base:].index, idx(m2)[base:], lw=1, color=ORANGE, label="M2 货币供应")
ax1.semilogy(cpi[base:].index, idx(cpi)[base:], lw=1, color=GREEN, label="CPI")
ax1.semilogy(real[base:].index, idx(real)[base:], lw=1, color=PURPLE, ls="--", label="纳指100 实际（÷CPI）")
ax1.set_title(f"维度 8 · 流动性与通胀背景：2008-01 = 100（对数坐标，M2/CPI 至 {m2.index[-1].strftime('%Y-%m')}）"); ax1.legend(loc="upper left", ncol=2)
ratio = (nm/m2).dropna(); ratio = ratio["1985-10":]
x = np.arange(len(ratio)); b, c = np.polyfit(x, np.log(ratio.values), 1); rf = np.exp(c+b*x); rdv = pd.Series((ratio.values/rf-1)*100, index=ratio.index)
ax2.plot(ratio.index, ratio.values*1000, lw=.9, color=NAVY, label="纳指100 ÷ M2（点位 / 十亿美元 ×1000）")
ax2.plot(ratio.index, rf*1000, "--", lw=1, color=RED, label=f"1985 起对数趋势，年化 {(np.exp(b*12)-1)*100:.1f}%")
ax2.set_yscale("log"); mark_now(ax2, ratio.index[-1], ratio.iloc[-1]*1000, fmt="{:.2f}"); ax2.legend(loc="upper left")
ax2.set_title("按货币存量缩放后的纳指100（扣掉水位之后还剩多少）")
save(fig, "09_liquidity.png")
S["liq"] = dict(ndx_since2008=float(idx(nm).iloc[-1]-100), m2_since2008=float(idx(m2).iloc[-1]-100), cpi_since2008=float(idx(cpi).iloc[-1]-100), real_ndx_since2008=float(idx(real).iloc[-1]-100),
                m2_asof=str(m2.index[-1].date()), ndx_m2_dev=float(rdv.iloc[-1]), ndx_m2_dev_pct=pr(rdv, rdv.iloc[-1]), ndx_m2_dev_2000=float(rdv["2000"].max()),
                ndx_m2_dev_2021=float(rdv["2021"].max()), ndx_m2_cagr=float((np.exp(b*12)-1)*100))

# ---------- Fig 10: realized vol ----------
vol = np.log(a).diff().rolling(60).std()*np.sqrt(252)*100
fig, ax = plt.subplots(figsize=(10, 3.4))
ax.plot(vol.index, vol.values, lw=.7, color=NAVY, label="QQQ 60 日实现波动率（年化）"); ax.axhline(vol.median(), color=GRAY, ls="--", lw=.8, label=f"中位 {vol.median():.0f}%")
mark_now(ax, vol.index[-1], vol.iloc[-1], fmt="{:.0f}%"); ax.set_ylabel("%"); ax.set_title("维度 9 · 市场情绪代理：实现波动率（顶部往往伴随波动率抬升）"); ax.legend(loc="upper left")
save(fig, "10_vol.png")
S["vol"] = dict(now=float(vol.iloc[-1]), pct=pr(vol, vol.iloc[-1]), median=float(vol.median()))


# ---------- table: what happened after similar positions ----------
def episodes(flag, min_gap_days=365):
    dates = flag[flag].index; eps = []
    for d in dates:
        if not eps or (d - eps[-1][-1]).days > min_gap_days:
            eps.append([d, d])
        else:
            eps[-1][-1] = d
    return eps


def fwd(series, d, yrs):
    i = series.index.get_indexer([d])[0]; j = i + 252*yrs
    return float((series.iloc[j]/series.iloc[i]-1)*100) if j < len(series) else np.nan


tr3 = (a/a.shift(756)-1)*100
cond = [("价格高出 1985 趋势线 > 90 分位", dev85 > dev85.quantile(.9), 365), ("3 年回报 > 90 分位", tr3 > tr3.quantile(.9), 365), ("前瞻 PE > 24x（高于 5 年均值）", fpe > 24, 180)]
tbl = []
for name, flag, gap in cond:
    for s_, e_ in episodes(flag.dropna(), gap):
        use_qqq = s_ >= a.index[0]; r = a if use_qqq else n
        d = r.index[r.index.get_indexer([s_], method="nearest")[0]]
        tbl.append(dict(cond=name, start=str(s_.date()), end=str(e_.date()), r1=fwd(r, d, 1), r3=fwd(r, d, 3), r5=fwd(r, d, 5), src="QQQ含息" if use_qqq else "NDX价格"))
S["episodes"] = tbl
pd.DataFrame(tbl).to_csv(HERE/"similar_episodes.csv", index=False, encoding="utf-8-sig")

# ---------- dashboard ----------
S["dashboard"] = [
    dict(k="偏离 1985 起趋势线", v=f"{S['trend85']['dev']:+.0f}%", p=S['trend85']['pct'], ref=f"中位 {S['trend85']['median']:+.0f}% / 2000 顶 {S['trend85']['peak2000']:+.0f}%"),
    dict(k="偏离 2009 起趋势线", v=f"{S['trend09']['dev']:+.0f}%", p=S['trend09']['pct'], ref=f"中位 {S['trend09']['median']:+.0f}% / 2021 顶 {S['trend09']['peak2021']:+.0f}%"),
    dict(k="距历史最高", v=f"{S['drawdown']['now']:.1f}%", p=None, ref=f"前高 {S['drawdown']['ath']:.2f} @ {S['drawdown']['ath_date']}"),
    dict(k="相对 200 日均线", v=f"{S['ma']['d200']:+.0f}%", p=S['ma']['d200_pct'], ref=f"中位 {S['ma']['d200_median']:+.0f}% / 90 分位 {S['ma']['d200_p90']:+.0f}%"),
    dict(k="过去 1 年总回报", v=f"{S['roll'][1]['now']:+.0f}%", p=S['roll'][1]['pct'], ref=f"中位 {S['roll'][1]['median']:+.0f}%"),
    dict(k="过去 3 年总回报", v=f"{S['roll'][3]['now']:+.0f}%", p=S['roll'][3]['pct'], ref=f"中位 {S['roll'][3]['median']:+.0f}%"),
    dict(k="过去 5 年总回报", v=f"{S['roll'][5]['now']:+.0f}%", p=S['roll'][5]['pct'], ref=f"中位 {S['roll'][5]['median']:+.0f}%"),
    dict(k="纳指100 前瞻 PE", v=f"{S['fpe']['now_daily']:.1f}x", p=S['fpe']['pct_since2001'], ref=f"2001 起中位 {S['fpe']['median']:.1f}x / 近 10 年均 {S['fpe']['mean10']:.1f}x / 2020 顶 {S['fpe']['peak2020']:.1f}x"),
    dict(k="纳指100 滚动 PE", v=f"{S['fpe']['trailing_now']:.1f}x", p=None, ref="年末值：2021 38.0x / 2022 23.7x / 2025 32.3x（Siblis）"),
    dict(k="标普500 CAPE", v=f"{S['cape']['now']:.1f}", p=S['cape']['pct'], ref=f"1881 起中位 {S['cape']['median']:.1f} / 2000 顶 {S['cape']['peak2000']:.1f} / 2021 顶 {S['cape']['peak2021']:.1f}"),
    dict(k="QQQ/SPY 偏离趋势", v=f"{S['rel']['dev']:+.0f}%", p=S['rel']['pct'], ref=f"90 分位 {S['rel']['p90']:+.0f}% / 2000 顶 {S['rel']['dev_peak2000']:+.0f}%"),
    dict(k="纳指100 ÷ M2 偏离趋势", v=f"{S['liq']['ndx_m2_dev']:+.0f}%", p=S['liq']['ndx_m2_dev_pct'], ref=f"2000 顶 {S['liq']['ndx_m2_dev_2000']:+.0f}% / 2021 顶 {S['liq']['ndx_m2_dev_2021']:+.0f}%"),
    dict(k="60 日实现波动率", v=f"{S['vol']['now']:.0f}%", p=S['vol']['pct'], ref=f"中位 {S['vol']['median']:.0f}%"),
]
json.dump(S, open(HERE/"stats.json", "w", encoding="utf-8"), indent=2, ensure_ascii=False, default=float)
print(json.dumps({k: S[k] for k in ("trend85", "trend09", "fpe", "cape", "liq", "vol", "rel", "roll")}, indent=1, ensure_ascii=False, default=float))
print(pd.DataFrame(tbl).to_string())
