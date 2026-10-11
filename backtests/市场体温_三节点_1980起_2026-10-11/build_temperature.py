#!/usr/bin/env python
"""Market temperature since 1980 with three nodes (2008 / 2015 / 2021 cycles).
Each gauge: current value, percentile within four bases (1980-, post-2009 trough, post-2016 trough, post-2022 trough),
and its reading at the three peaks and three troughs. Groups: price, valuation, economy, liquidity, gold.
Outputs fig/*.png, gauges.csv, stats_temp.json"""
import json, sys, numpy as np, pandas as pd
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass
from pathlib import Path
HERE = Path(__file__).resolve().parent; D = HERE/"data"; F = HERE/"fig"; F.mkdir(exist_ok=True)
plt.rcParams.update({"font.family": ["Microsoft YaHei", "SimHei"], "axes.unicode_minus": False, "figure.dpi": 150, "axes.grid": True, "grid.alpha": .3,
                     "axes.spines.top": False, "axes.spines.right": False, "font.size": 9, "legend.fontsize": 8, "axes.titlesize": 11})
NAVY, ORANGE, RED, GREEN, GRAY, PURPLE, TEAL, GOLD = "#1f4e79", "#e36c09", "#c00000", "#2e7d32", "#7f7f7f", "#6a3d9a", "#0b7285", "#b8860b"
REC = [("1980-01-01", "1980-07-31"), ("1981-07-01", "1982-11-30"), ("1990-07-01", "1991-03-31"), ("2001-03-01", "2001-11-30"), ("2007-12-01", "2009-06-30"), ("2020-02-01", "2020-04-30")]
S = {}


def yh(l, col="close"):
    return pd.read_csv(D/f"{l}_daily.csv", parse_dates=["date"]).set_index("date")[col].dropna()


gspc, tr, ndx, qqq = yh("GSPC"), yh("SP500TR"), yh("NDX"), yh("QQQ", "adj_close")
tnx, irx, fvx, vix, dxy = yh("TNX"), yh("IRX"), yh("FVX"), yh("VIX"), yh("DXY")
bls = pd.read_csv(D/"bls_cpi_unrate_monthly.csv"); bls["dt"] = pd.to_datetime(bls.month); bls = bls.set_index("dt"); cpi, unr = bls.cpi_u_nsa.dropna(), bls.unrate_sa.dropna()
m2 = pd.read_csv(D/"us_m2_monthly.csv"); m2["dt"] = pd.to_datetime(m2.month); m2 = m2.set_index("dt").m2_sa_usd_bn
gold = pd.read_csv(D/"gold_lbma_pm_daily.csv", parse_dates=[0]); gold = gold.set_index(gold.columns[0]).iloc[:, 0].astype(float).dropna()
gcf = yh("GCF"); gold_lbma_last = gold.index[-1]; gold = pd.concat([gold, gcf[gcf.index > gold_lbma_last]])  # splice COMEX front-month after LBMA cache ends
cape = pd.read_csv(D/"multpl_shiller_pe.csv", parse_dates=["date"]).set_index("date").value
spe = pd.read_csv(D/"multpl_sp500_pe.csv", parse_dates=["date"]).set_index("date").value
fpe = pd.read_csv(D/"ndx_forward_pe_weekly.csv", parse_dates=["date"]).set_index("date").value
AS_OF = str(gspc.index[-1].date()); S["as_of"] = AS_OF
S["gold_splice"] = dict(lbma_last=str(gold_lbma_last.date()), gcf_last=str(gcf.index[-1].date()), gcf_last_value=float(gcf.iloc[-1]), lbma_last_value=float(gold[gold_lbma_last]))
S["levels"] = dict(spx=float(gspc.iloc[-1]), ndx=float(ndx.iloc[-1]), gold=float(gold.iloc[-1]), gold_date=str(gold.index[-1].date()), tnx=float(tnx.iloc[-1]), irx=float(irx.iloc[-1]),
                   fvx=float(fvx.iloc[-1]), vix=float(vix.iloc[-1]), dxy=float(dxy.iloc[-1]), cpi_date=str(cpi.index[-1].date()), unrate=float(unr.iloc[-1]), unrate_date=str(unr.index[-1].date()), m2_date=str(m2.index[-1].date()))

# ---- nodes (computed from data) ----
def argmax(s, a, b): return s[a:b].idxmax()
def argmin(s, a, b): return s[a:b].idxmin()
PK = {"2007": argmax(gspc, "2007-01-01", "2007-12-31"), "2015": argmax(gspc, "2015-01-01", "2015-12-31"), "2021": argmax(gspc, "2021-10-01", "2022-01-31")}
TR = {"2009": argmin(gspc, "2008-09-01", "2009-06-30"), "2016": argmin(gspc, "2015-08-01", "2016-03-31"), "2022": argmin(gspc, "2022-06-01", "2022-12-31")}
PKN = {"2007": argmax(ndx, "2007-01-01", "2007-12-31"), "2015": argmax(ndx, "2015-01-01", "2015-12-31"), "2021": argmax(ndx, "2021-10-01", "2022-01-31")}
TRN = {"2009": argmin(ndx, "2008-09-01", "2009-06-30"), "2016": argmin(ndx, "2015-08-01", "2016-03-31"), "2022": argmin(ndx, "2022-06-01", "2022-12-31")}
S["nodes"] = {"spx_peaks": {k: str(v.date()) for k, v in PK.items()}, "spx_troughs": {k: str(v.date()) for k, v in TR.items()}, "ndx_peaks": {k: str(v.date()) for k, v in PKN.items()}, "ndx_troughs": {k: str(v.date()) for k, v in TRN.items()},
              "spx_drawdowns": {k: float((gspc[TR[k]]/gspc[PK[p]]-1)*100) for k, p in zip(TR, PK)}, "ndx_drawdowns": {k: float((ndx[TRN[k]]/ndx[PKN[p]]-1)*100) for k, p in zip(TRN, PKN)}}
print("nodes", S["nodes"])
BASES = {"1980 起": pd.Timestamp("1980-01-01"), "2009 起": TR["2009"], "2016 起": TR["2016"], "2022 起": TR["2022"]}
GAUGES = []


def asof(s, d):
    s2 = s[:d]; return float(s2.iloc[-1]) if len(s2) else np.nan


def gauge(name, group, s, hot="high", fmt="{:+.0f}%", note=""):
    """register gauge: percentile within each base; readings at peaks/troughs"""
    s = s.dropna(); now = float(s.iloc[-1]); rec = dict(指标=name, 组=group, 现值=now, fmt=fmt, hot=hot, note=note, start=str(s.index[0].date()))
    for b, d in BASES.items():
        sub = s[s.index >= d]; rec[f"分位 {b}"] = float((sub < now).mean()*100) if len(sub) > 20 else np.nan
    for k, d in PK.items(): rec[f"{k} 顶"] = asof(s, d)
    for k, d in TR.items(): rec[f"{k} 底"] = asof(s, d)
    p = rec["分位 1980 起"]; rec["热度"] = p if hot == "high" else (100 - p if hot == "low" else np.nan)
    GAUGES.append(rec); return rec


def trend(series, start):
    s = series[series.index >= start].dropna(); x = np.arange(len(s)); b, c = np.polyfit(x, np.log(s.values), 1)
    fit = pd.Series(np.exp(c+b*x), index=s.index); per = 252 if (s.index[1:] - s.index[:-1]).median().days <= 3 else 12
    return fit, (s/fit-1)*100, (np.exp(b*per)-1)*100


def shade(ax):
    for a, b in REC: ax.axvspan(pd.Timestamp(a), pd.Timestamp(b), color=GRAY, alpha=.15, lw=0)


def nodes(ax, y=None):
    for k, d in PK.items(): ax.axvline(d, color=RED, lw=.7, ls=":")
    for k, d in TR.items(): ax.axvline(d, color=GREEN, lw=.7, ls=":")


# ================= PRICE: S&P since 1980 =================
spx = gspc["1980":]; fit80, dev80, cagr80 = trend(gspc, "1980-01-01")
gauge("标普500 偏离 1980 起趋势线", "价格", dev80, note=f"趋势年化 {cagr80:.1f}%")
d200 = (gspc/gspc.rolling(200).mean()-1)*100; gauge("标普500 相对 200 日均线", "价格", d200["1980":])
r3 = (gspc/gspc.shift(756)-1)*100; gauge("标普500 过去 3 年价格回报", "价格", r3["1980":])
tr5 = (tr/tr.shift(1260)-1)*100; gauge("标普500 过去 5 年总回报（1993 起）", "价格", tr5["1993":])
dd = (gspc/gspc.cummax()-1)*100; gauge("标普500 距历史最高", "价格", dd["1980":], hot="high", fmt="{:.1f}%")
fitN, devN, cagrN = trend(ndx, "1985-10-01"); gauge("纳指100 偏离 1985 起趋势线", "价格", devN, note=f"趋势年化 {cagrN:.1f}%")
d200n = (ndx/ndx.rolling(200).mean()-1)*100; gauge("纳指100 相对 200 日均线", "价格", d200n)
q3 = (qqq/qqq.shift(756)-1)*100; gauge("QQQ 过去 3 年总回报", "价格", q3)
# NDX trend lines from each node trough
S["ndx_eras"] = {}
for k, d in TRN.items():
    f_, dv, cg = trend(ndx, str(d.date())); sub = dv; S["ndx_eras"][k] = dict(start=str(d.date()), cagr=cg, dev=float(dv.iloc[-1]), pct=float((dv < dv.iloc[-1]).mean()*100), p90=float(dv.quantile(.9)), max=float(dv.max()), max_date=str(dv.idxmax().date()))
S["spx_eras"] = {}
for k, d in TR.items():
    f_, dv, cg = trend(gspc, str(d.date())); S["spx_eras"][k] = dict(start=str(d.date()), cagr=cg, dev=float(dv.iloc[-1]), pct=float((dv < dv.iloc[-1]).mean()*100), p90=float(dv.quantile(.9)), max=float(dv.max()), max_date=str(dv.idxmax().date()))

# ================= VALUATION =================
gauge("标普500 CAPE", "估值", cape["1980":], fmt="{:.1f}")
gauge("标普500 滚动 PE", "估值", spe["1980":], fmt="{:.1f}")
ey = (100/spe).rename("ey"); gap = (ey - tnx.resample("MS").first().reindex(ey.index, method="nearest"))["1980":]
gauge("标普500 盈利收益率 − 10 年国债（Fed 模型）", "估值", gap, hot="low", fmt="{:+.1f}pp")
gauge("纳指100 前瞻 PE（2001 起）", "估值", fpe, fmt="{:.1f}")
# ================= ECONOMY =================
unr80 = unr["1980":]; gauge("失业率", "经济", unr80, hot="low", fmt="{:.1f}%")
sahm = (unr.rolling(3).mean() - unr.rolling(12).min())["1980":]; gauge("Sahm 指标（3 月均值 − 12 月最低）", "经济", sahm, hot="low", fmt="{:+.2f}pp", note="≥0.5 历史上对应衰退开始")
cpiy = (cpi/cpi.shift(12)-1)*100; gauge("CPI 同比", "经济", cpiy["1980":], fmt="{:.1f}%")
curve = (tnx - irx)["1980":]; gauge("收益率曲线 10 年 − 3 月", "经济", curve, hot="low", fmt="{:+.2f}pp", note="倒挂后 6–18 个月常见衰退")
realtb = (irx.resample("MS").first() - cpiy.reindex(irx.resample("MS").first().index, method="nearest"))["1980":]; gauge("实际短期利率（3 月国库券 − CPI 同比）", "经济", realtb, hot="high", fmt="{:+.1f}pp", note="高 = 政策紧")
gauge("10 年国债收益率", "经济", tnx["1980":], hot="high", fmt="{:.2f}%")
# ================= LIQUIDITY =================
m2y = (m2/m2.shift(12)-1)*100; gauge("M2 同比", "流动性", m2y["1980":], fmt="{:.1f}%")
gauge("VIX（1990 起）", "流动性", vix, hot="low", fmt="{:.1f}")
gauge("美元指数 DXY", "流动性", dxy["1980":], hot="high", fmt="{:.1f}")
# ================= GOLD =================
gm = gold.resample("MS").first(); cpi_m = cpi.reindex(gm.index, method="ffill"); real_gold = (gm/cpi_m*cpi.iloc[-1])["1980":]
gauge("黄金实际价格（按今日 CPI 折算）", "黄金", real_gold, fmt="${:,.0f}")
g_spx = (gm/gspc.resample("MS").first().reindex(gm.index, method="nearest"))["1980":]; gauge("黄金 / 标普500 比值", "黄金", g_spx, fmt="{:.2f}")
g3 = (gold/gold.shift(756)-1)*100; gauge("黄金过去 3 年回报", "黄金", g3["1980":])
g_m2 = (gm/m2.reindex(gm.index, method="ffill")*1000)["1980":].dropna(); gauge("黄金 / M2（美元每十亿美元 ×1000）", "黄金", g_m2, fmt="{:.3f}")
S["gold_levels"] = dict(peak1980=float(gold["1979":"1981"].max()), peak1980_date=str(gold["1979":"1981"].idxmax().date()), peak2011=float(gold["2011"].max()), peak2011_date=str(gold["2011"].idxmax().date()),
                        now=float(gold.iloc[-1]), real_peak1980=float(real_gold["1980":"1981"].max()), real_peak2011=float(real_gold["2011"].max()), real_now=float(real_gold.iloc[-1]))

G = pd.DataFrame(GAUGES); G.to_csv(HERE/"gauges.csv", index=False, encoding="utf-8-sig", float_format="%.2f")
S["gauges"] = G.round(2).to_dict("records")
S["heat_by_group"] = G.groupby("组")["热度"].mean().round(0).to_dict()
# heat at the nodes: percentile of each node reading within the 1980 base (for a "then vs now" comparison)
def pct_at(s, d, base=pd.Timestamp("1980-01-01")):
    s = s.dropna(); sub = s[(s.index >= base) & (s.index <= d)]; v = asof(s, d); return float((sub < v).mean()*100) if len(sub) else np.nan
json.dump(S, open(HERE/"stats_temp.json", "w", encoding="utf-8"), indent=2, ensure_ascii=False, default=float)
cols = ["指标", "组", "现值", "分位 1980 起", "分位 2009 起", "分位 2016 起", "分位 2022 起", "2007 顶", "2015 顶", "2021 顶", "2009 底", "2016 底", "2022 底", "热度"]
print(G[cols].round(1).to_string()); print(S["heat_by_group"]); print(json.dumps(S["ndx_eras"], indent=1)); print(json.dumps(S["spx_eras"], indent=1)); print(S["gold_levels"])

# ================= CHARTS =================
def save(fig, name): fig.tight_layout(); fig.savefig(F/name, dpi=150); plt.close(fig); print("fig", name)
# F1 S&P 1980- log + trend + nodes; deviation
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6.4), gridspec_kw={"height_ratios": [1.5, 1]})
ax1.semilogy(spx.index, spx.values, lw=.9, color=NAVY, label="标普500（价格指数）"); ax1.semilogy(fit80.index, fit80.values, "--", lw=1.1, color=RED, label=f"1980 起对数趋势线，年化 {cagr80:.1f}%")
shade(ax1); nodes(ax1)
for k, d in PK.items(): ax1.annotate(f"{k} 顶", (d, gspc[d]), xytext=(0, 8), textcoords="offset points", ha="center", fontsize=7.5, color=RED)
for k, d in TR.items(): ax1.annotate(f"{k} 底", (d, gspc[d]), xytext=(0, -14), textcoords="offset points", ha="center", fontsize=7.5, color=GREEN)
ax1.plot([spx.index[-1]], [spx.iloc[-1]], "o", color=RED, ms=5); ax1.annotate(f"{spx.iloc[-1]:,.0f}", (spx.index[-1], spx.iloc[-1]), xytext=(6, -2), textcoords="offset points", color=RED, fontsize=8, fontweight="bold")
ax1.set_title(f"图 1 · 标普500 1980–{AS_OF[:4]}：价格、趋势线、三个节点（灰 = NBER 衰退）"); ax1.legend(loc="upper left")
ax2.plot(dev80.index, dev80.values, lw=.8, color=NAVY, label="偏离 1980 起趋势线 %"); ax2.axhline(0, color="k", lw=.7)
ax2.axhline(dev80.quantile(.9), color=RED, ls=":", lw=1, label=f"90 分位 {dev80.quantile(.9):+.0f}%"); ax2.axhline(dev80.quantile(.1), color=GREEN, ls=":", lw=1, label=f"10 分位 {dev80.quantile(.1):+.0f}%")
shade(ax2); nodes(ax2); ax2.plot([dev80.index[-1]], [dev80.iloc[-1]], "o", color=RED, ms=5); ax2.annotate(f"{dev80.iloc[-1]:+.0f}%", (dev80.index[-1], dev80.iloc[-1]), xytext=(6, 4), textcoords="offset points", color=RED, fontsize=8, fontweight="bold")
ax2.legend(loc="upper left", ncol=3); ax2.set_ylabel("%")
save(fig, "01_spx_1980.png")
# F2 valuation
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6), sharex=True)
c80 = cape["1980":]; ax1.plot(c80.index, c80.values, lw=1, color=NAVY, label="标普500 CAPE"); ax1.axhline(c80.median(), color=GRAY, ls="--", lw=.8, label=f"1980 起中位 {c80.median():.1f}")
shade(ax1); nodes(ax1); ax1.plot([c80.index[-1]], [c80.iloc[-1]], "o", color=RED, ms=5); ax1.annotate(f"{c80.iloc[-1]:.1f}", (c80.index[-1], c80.iloc[-1]), xytext=(6, 2), textcoords="offset points", color=RED, fontsize=8, fontweight="bold")
ax1.set_title("图 2 · 估值：CAPE 与「盈利收益率 − 10 年国债」（Fed 模型，负 = 股票相对债券无溢价）"); ax1.legend(loc="upper left")
ax2.plot(gap.index, gap.values, lw=1, color=ORANGE, label="标普500 盈利收益率 − 10 年国债收益率（百分点）"); ax2.axhline(0, color="k", lw=.8); shade(ax2); nodes(ax2)
ax2.plot([gap.index[-1]], [gap.iloc[-1]], "o", color=RED, ms=5); ax2.annotate(f"{gap.iloc[-1]:+.1f}", (gap.index[-1], gap.iloc[-1]), xytext=(6, 2), textcoords="offset points", color=RED, fontsize=8, fontweight="bold")
ax2.legend(loc="upper left"); ax2.set_ylabel("pp")
save(fig, "02_valuation.png")
# F3 NDX with node trend lines
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6.4), gridspec_kw={"height_ratios": [1.5, 1]})
n85 = ndx["2005":]; ax1.semilogy(n85.index, n85.values, lw=.9, color=NAVY, label="纳指100")
cols = {"2009": ORANGE, "2016": TEAL, "2022": PURPLE}
for k, d in TRN.items():
    f_, dv, cg = trend(ndx, str(d.date())); ax1.semilogy(f_.index, f_.values, "--", lw=1.1, color=cols[k], label=f"{k} 底起趋势线，年化 {cg:.1f}%，当前偏离 {dv.iloc[-1]:+.0f}%（{S['ndx_eras'][k]['pct']:.0f} 分位）")
    ax2.plot(dv.index, dv.values, lw=.9, color=cols[k], label=f"偏离 {k} 底起趋势线")
shade(ax1); nodes(ax1); ax1.set_xlim(pd.Timestamp("2005-01-01"), ndx.index[-1] + pd.DateOffset(months=8)); ax1.set_title(f"图 3 · 纳指100 2005–{AS_OF[:4]}：从三个底部分别拟合的趋势线"); ax1.legend(loc="upper left")
ax2.axhline(0, color="k", lw=.7); shade(ax2); nodes(ax2); ax2.set_xlim(pd.Timestamp("2005-01-01"), ndx.index[-1] + pd.DateOffset(months=8)); ax2.legend(loc="upper left", ncol=3); ax2.set_ylabel("%")
save(fig, "03_ndx_three_nodes.png")
# F4 gold
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6), sharex=True)
g80 = gm["1980":]; ax1.semilogy(g80.index, g80.values, lw=1, color=GOLD, label="黄金名义 USD/oz（LBMA PM）"); ax1.semilogy(real_gold.index, real_gold.values, lw=1, color=NAVY, ls="--", label="黄金实际价格（按今日 CPI）")
shade(ax1); nodes(ax1); ax1.plot([g80.index[-1]], [g80.iloc[-1]], "o", color=RED, ms=5); ax1.annotate(f"{g80.iloc[-1]:,.0f}", (g80.index[-1], g80.iloc[-1]), xytext=(6, 2), textcoords="offset points", color=RED, fontsize=8, fontweight="bold")
ax1.set_title("图 4 · 黄金：名义与实际价格，黄金 / 标普500 比值（1980 起）"); ax1.legend(loc="upper left")
ax2.plot(g_spx.index, g_spx.values, lw=1, color=GOLD, label="黄金 / 标普500"); ax2.axhline(g_spx.median(), color=GRAY, ls="--", lw=.8, label=f"中位 {g_spx.median():.2f}"); shade(ax2); nodes(ax2)
ax2.plot([g_spx.index[-1]], [g_spx.iloc[-1]], "o", color=RED, ms=5); ax2.annotate(f"{g_spx.iloc[-1]:.2f}", (g_spx.index[-1], g_spx.iloc[-1]), xytext=(6, 2), textcoords="offset points", color=RED, fontsize=8, fontweight="bold")
ax2.set_yscale("log"); ax2.legend(loc="upper left")
save(fig, "04_gold.png")
# F5 inflation & liquidity
fig, axes = plt.subplots(3, 1, figsize=(10, 7.5), sharex=True)
for ax, s, col, lab in [(axes[0], cpiy["1980":], RED, "CPI 同比 %"), (axes[1], realtb, NAVY, "实际短期利率：3 月国库券 − CPI 同比（百分点）"), (axes[2], m2y["1980":], ORANGE, "M2 同比 %")]:
    ax.plot(s.index, s.values, lw=1, color=col, label=lab); ax.axhline(0, color="k", lw=.7); shade(ax); nodes(ax); ax.legend(loc="upper left")
    ax.plot([s.index[-1]], [s.iloc[-1]], "o", color=RED, ms=5); ax.annotate(f"{s.iloc[-1]:+.1f}", (s.index[-1], s.iloc[-1]), xytext=(6, 2), textcoords="offset points", color=RED, fontsize=8, fontweight="bold")
axes[0].set_title("图 5 · 通胀与流动性：CPI、实际利率、M2（1980 起）")
save(fig, "05_inflation_liquidity.png")
# F6 economy
fig, axes = plt.subplots(2, 1, figsize=(10, 6), sharex=True)
ax = axes[0]; ax.plot(curve.index, curve.values, lw=.8, color=NAVY, label="收益率曲线：10 年 − 3 月（百分点）"); ax.axhline(0, color="k", lw=.8); shade(ax); nodes(ax); ax.legend(loc="upper left")
ax.plot([curve.index[-1]], [curve.iloc[-1]], "o", color=RED, ms=5); ax.annotate(f"{curve.iloc[-1]:+.2f}", (curve.index[-1], curve.iloc[-1]), xytext=(6, 2), textcoords="offset points", color=RED, fontsize=8, fontweight="bold")
ax.set_title("图 6 · 经济温度：收益率曲线、失业率与 Sahm 指标（1980 起，灰 = 衰退）")
ax = axes[1]; ax.plot(unr80.index, unr80.values, lw=1, color=NAVY, label="失业率 %"); shade(ax); nodes(ax)
ax2 = ax.twinx(); ax2.plot(sahm.index, sahm.values, lw=.9, color=RED, label="Sahm 指标（右轴）"); ax2.axhline(.5, color=RED, ls=":", lw=1); ax2.set_ylim(-1, 5); ax2.grid(False)
ax.plot([unr80.index[-1]], [unr80.iloc[-1]], "o", color=RED, ms=5); ax.annotate(f"{unr80.iloc[-1]:.1f}%", (unr80.index[-1], unr80.iloc[-1]), xytext=(6, 2), textcoords="offset points", color=RED, fontsize=8, fontweight="bold")
h1, l1 = ax.get_legend_handles_labels(); h2, l2 = ax2.get_legend_handles_labels(); ax.legend(h1+h2, l1+l2, loc="upper left")
save(fig, "06_economy.png")
# F7 heat bars: current percentile since 1980 by gauge
fig, ax = plt.subplots(figsize=(10, 6.2)); Gp = G.dropna(subset=["热度"]).sort_values(["组", "热度"])
colors = [RED if h >= 80 else (ORANGE if h >= 60 else (GREEN if h <= 20 else NAVY)) for h in Gp["热度"]]
ax.barh(Gp["指标"] + "  [" + Gp["组"] + "]", Gp["热度"], color=colors); ax.axvline(50, color="k", lw=.8); ax.axvline(80, color=RED, ls=":", lw=1); ax.axvline(20, color=GREEN, ls=":", lw=1)
ax.set_xlim(0, 100); ax.set_xlabel("热度 = 1980 年以来的分位（已按方向统一：越右越热）"); ax.set_title(f"图 7 · 体温计：每个指标的当前热度（截至 {AS_OF}）"); ax.grid(axis="y", alpha=0)
save(fig, "07_heat_bars.png")
