#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Benchmark = nominal GDP (≈ real GDP + CPI). From anchors 2010-01 and 2020-01, draw the GDP line from the asset's
level at the anchor and measure how far QQQ / SPY / the whole market have run ahead of it. Decompose the excess into
earnings-beyond-GDP and multiple expansion. Buffett ratio (Wilshire 5000 / nominal GDP) for context.
Outputs fig/*.png, stats_gdp.json, table_*.csv"""
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


def yh(l, col="close"):
    return pd.read_csv(D/f"{l}_daily.csv", parse_dates=["date"]).set_index("date")[col].dropna()


A = {"QQQ 含分红": yh("QQQ", "adj_close"), "SPY 含分红": yh("SPY", "adj_close"), "纳指100 价格": yh("NDX"), "标普500 价格": yh("GSPC"), "全市场 Wilshire 5000": yh("W5000"),
     "标普等权 RSP": yh("RSP", "adj_close"), "罗素2000 IWM": yh("IWM", "adj_close"), "全球 VT": yh("VT", "adj_close")}
AS_OF = str(A["QQQ 含分红"].index[-1].date()); S["as_of"] = AS_OF
# ---- GDP: BEA quarterly (SAAR, $bn) to 2025Q1, then extrapolated at trailing 4-quarter growth ----
Q = pd.read_csv(D/"bea_gdp_quarterly.csv", parse_dates=["date"]).set_index("date"); last_q = Q.index[-1]
g_nom = Q.gdp_nominal_bn.iloc[-1]/Q.gdp_nominal_bn.iloc[-5]; g_real = Q.gdp_real_bn.iloc[-1]/Q.gdp_real_bn.iloc[-5]  # 4-quarter growth factors
ext_idx = pd.date_range(last_q + pd.offsets.QuarterEnd(), AS_OF, freq="QE") if hasattr(pd.offsets, "QuarterEnd") else []
ext_idx = pd.date_range(last_q, pd.Timestamp(AS_OF) + pd.offsets.QuarterEnd(), freq="QE")[1:]
ext = pd.DataFrame({"gdp_nominal_bn": [Q.gdp_nominal_bn.iloc[-1]*g_nom**((i+1)/4) for i in range(len(ext_idx))],
                    "gdp_real_bn": [Q.gdp_real_bn.iloc[-1]*g_real**((i+1)/4) for i in range(len(ext_idx))]}, index=ext_idx)
QX = pd.concat([Q[["gdp_nominal_bn", "gdp_real_bn"]], ext]); QX["extrapolated"] = QX.index > last_q
S["gdp"] = dict(bea_last_quarter=str(last_q.date()), trailing_nominal_yoy=(g_nom-1)*100, trailing_real_yoy=(g_real-1)*100, extrapolated_quarters=int(len(ext_idx)),
                nominal_2024_bn=float(Q.gdp_nominal_bn["2024-12-31"]), wb_2025_usd=float(pd.read_csv(D/"wb_gdp_nominal.csv").set_index("year").usd[2025]))
# daily interpolation in log space
days = pd.date_range("1990-01-01", AS_OF, freq="D")
ngdp = np.exp(np.log(QX.gdp_nominal_bn).reindex(days.union(QX.index)).interpolate(method="time").reindex(days))
rgdp = np.exp(np.log(QX.gdp_real_bn).reindex(days.union(QX.index)).interpolate(method="time").reindex(days))
bls = pd.read_csv(D/"bls_cpi_unrate_monthly.csv"); bls["dt"] = pd.to_datetime(bls.month); cpi = bls.set_index("dt").cpi_u_nsa.dropna()
cpi_d = cpi.reindex(days.union(cpi.index)).interpolate(method="time").reindex(days).ffill()
S["gdp"]["cpi_last"] = str(cpi.index[-1].date())
# ---- head-company premium: S&P EPS growth minus nominal GDP growth, long windows ----
spe = pd.read_csv(D/"multpl_sp500_pe.csv", parse_dates=["date"]).set_index("date").value
gm = A["标普500 价格"].resample("MS").first(); gm.index = gm.index.normalize()
eps = (gm.reindex(spe.index, method="nearest")/spe).dropna()  # nominal trailing EPS = price / trailing PE (multpl earnings table is inflation-adjusted)
AN = pd.read_csv(D/"bea_gdp_annual.csv").set_index("year")
eps_y = eps.groupby(eps.index.year).last()
prem = {}
for a, b in ((1970, 2024), (1990, 2024), (2010, 2024)):
    ce = (eps_y[b]/eps_y[a])**(1/(b-a))-1; cg = (AN.gdp_nominal_bn[b]/AN.gdp_nominal_bn[a])**(1/(b-a))-1
    prem[f"{a}-{b}"] = dict(eps_cagr=ce*100, ngdp_cagr=cg*100, premium=(ce-cg)*100)
S["premium"] = prem; PREM = prem["1990-2024"]["premium"]/100  # modern window (buybacks, margins); 1960 window reported alongside
print("premium", json.dumps(prem, indent=1))

# ---- anchors ----
ANCH = {"2010": pd.Timestamp("2010-01-04"), "2020": pd.Timestamp("2020-01-02")}
S["anchors"] = {k: str(v.date()) for k, v in ANCH.items()}


def lines(series, a):
    s = series[series.index >= a]; p0 = float(s.iloc[0]); idx = s.index
    L1 = p0*ngdp.reindex(idx)/ngdp[a]; L2 = p0*(rgdp.reindex(idx)/rgdp[a])*(cpi_d.reindex(idx)/cpi_d[a])
    t = (idx - a).days/365.25; L3 = L1*(1+PREM)**t
    return s, L1, L2, L3


def cagr(x0, x1, yrs): return ((x1/x0)**(1/yrs)-1)*100


tables = {}
for k, a in ANCH.items():
    rows = []
    yrs = (pd.Timestamp(AS_OF)-a).days/365.25
    gn = cagr(ngdp[a], ngdp.iloc[-1], yrs); gr = cagr(rgdp[a], rgdp.iloc[-1], yrs); gc = cagr(cpi_d[a], cpi_d.iloc[-1], yrs)
    for name, ser in A.items():
        if ser.index[0] > a: continue
        s, L1, L2, L3 = lines(ser, a); ga = cagr(s.iloc[0], s.iloc[-1], yrs)
        gap1 = (s.iloc[-1]/L1.iloc[-1]-1)*100; gap3 = (s.iloc[-1]/L3.iloc[-1]-1)*100
        years_borrowed = np.log(s.iloc[-1]/L1.iloc[-1])/np.log(1+gn/100)
        rows.append(dict(资产=name, 年化=ga, 名义GDP年化=gn, 超出GDP=ga-gn, 累计超出GDP线=gap1, 超出GDP加头部溢价线=gap3, 相当于透支GDP年数=years_borrowed, 总涨幅=(s.iloc[-1]/s.iloc[0]-1)*100, GDP线涨幅=(L1.iloc[-1]/L1.iloc[0]-1)*100))
    T = pd.DataFrame(rows); T.to_csv(HERE/f"table_anchor_{k}.csv", index=False, encoding="utf-8-sig", float_format="%.1f"); tables[k] = T
    S[f"anchor_{k}"] = dict(years=yrs, ngdp_cagr=gn, rgdp_cagr=gr, cpi_cagr=gc, real_plus_cpi=gr+gc, rows=T.round(2).to_dict("records"))
    print(f"anchor {k}: {yrs:.1f}y  nominal GDP {gn:.1f}%/yr  real {gr:.1f}%  CPI {gc:.1f}%"); print(T.round(1).to_string())
# sensitivity: COVID trough anchor
a = pd.Timestamp("2020-03-23"); yrs = (pd.Timestamp(AS_OF)-a).days/365.25; gn = cagr(ngdp[a], ngdp.iloc[-1], yrs)
S["anchor_2020_trough"] = {name: dict(年化=cagr(ser[a:].iloc[0], ser.iloc[-1], yrs), 名义GDP年化=gn, 累计超出GDP线=(ser.iloc[-1]/(ser[a:].iloc[0]*ngdp.iloc[-1]/ngdp[a])-1)*100) for name, ser in A.items() if name in ("QQQ 含分红", "SPY 含分红")}

# ---- decomposition: price = GDP x (EPS/GDP) x PE ----
spx = A["标普500 价格"]; fpe = pd.read_csv(D/"ndx_forward_pe_weekly.csv", parse_dates=["date"]).set_index("date").value; ndx = A["纳指100 价格"]
ndx_eps = (ndx.reindex(fpe.index, method="nearest")/fpe).dropna()  # forward EPS implied
dec = {}
for k, a in ANCH.items():
    g0, g1 = ngdp[a], ngdp.iloc[-1]; p0, p1 = spx[a:].iloc[0], spx.iloc[-1]
    pe0, pe1 = float(spe[:a].iloc[-1]), float(spe.iloc[-1]); e0, e1 = p0/pe0, p1/pe1
    ne0, ne1 = ndx_eps[:a].iloc[-1], ndx_eps.iloc[-1]; np0, np1 = ndx[a:].iloc[0], ndx.iloc[-1]; fpe0, fpe1 = fpe[:a].iloc[-1], 21.83
    dec[k] = dict(spx=dict(price=p1/p0, gdp=g1/g0, eps_over_gdp=(e1/e0)/(g1/g0), pe=pe1/pe0, pe0=pe0, pe1=pe1, eps=e1/e0),
                  ndx=dict(price=np1/np0, gdp=g1/g0, eps_over_gdp=(ne1/ne0)/(g1/g0), pe=fpe1/fpe0, pe0=fpe0, pe1=fpe1, eps=ne1/ne0))
S["decomp"] = dec; print(json.dumps(dec, indent=1))
# ---- Buffett ratio ----
w = A["全市场 Wilshire 5000"]; br = (w/ngdp.reindex(w.index)).dropna()["1990":]
S["buffett"] = dict(now=float(br.iloc[-1]), pct_since1990=float((br < br.iloc[-1]).mean()*100), at2010=float(br[ANCH["2010"]:].iloc[0]), at2020=float(br[ANCH["2020"]:].iloc[0]),
                    peak2000=float(br["2000"].max()), peak2021=float(br["2021"].max()), low2009=float(br["2009"].min()), ratio_vs2010=float(br.iloc[-1]/br[ANCH["2010"]:].iloc[0]), ratio_vs2020=float(br.iloc[-1]/br[ANCH["2020"]:].iloc[0]))

# gap extremes for the text
GE = {}
for k, a in ANCH.items():
    for name in ("QQQ 含分红", "SPY 含分红", "全市场 Wilshire 5000", "标普等权 RSP"):
        s_, L1, L2, L3 = lines(A[name], a); gap = (s_/L1-1)*100
        GE[f"{k}|{name}"] = dict(max2021=float(gap["2021"].max()), max2021_date=str(gap["2021"].idxmax().date()), min2022=float(gap["2022"].min()), min2022_date=str(gap["2022"].idxmin().date()), now=float(gap.iloc[-1]))
S["gap_extremes"] = GE
json.dump(S, open(HERE/"stats_gdp.json", "w", encoding="utf-8"), indent=2, ensure_ascii=False, default=float)
print("buffett", S["buffett"])

# ================= charts =================
def save(fig, name): fig.tight_layout(); fig.savefig(F/name, dpi=150); plt.close(fig); print("fig", name)


COL = {"QQQ 含分红": NAVY, "SPY 含分红": ORANGE, "标普500 价格": "#f4a261", "全市场 Wilshire 5000": PURPLE, "标普等权 RSP": TEAL, "罗素2000 IWM": GRAY, "全球 VT": BROWN}
for k, a in ANCH.items():
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 7.4), gridspec_kw={"height_ratios": [1.8, 1]}, sharex=True)
    base = {}
    for name in ("QQQ 含分红", "SPY 含分红", "全市场 Wilshire 5000", "标普等权 RSP", "罗素2000 IWM", "全球 VT"):
        s, L1, L2, L3 = lines(A[name], a); r = s/s.iloc[0]*100; ax1.semilogy(r.index, r.values, lw=1 if name in ("QQQ 含分红", "SPY 含分红") else .8, color=COL[name], label=f"{name} ×{r.iloc[-1]/100:.2f}")
        base[name] = (s, L1, L3)
    s, L1, L2, L3 = lines(A["SPY 含分红"], a)
    ax1.semilogy(L1.index, (L1/L1.iloc[0]*100).values, "--", lw=1.6, color=RED, label=f"名义 GDP 线 ×{L1.iloc[-1]/L1.iloc[0]:.2f}（年化 {S[f'anchor_{k}']['ngdp_cagr']:.1f}%）")
    ax1.semilogy(L2.index, (L2/L2.iloc[0]*100).values, ":", lw=1.4, color=RED, label=f"实际 GDP × CPI 线 ×{L2.iloc[-1]/L2.iloc[0]:.2f}")
    ax1.semilogy(L3.index, (L3/L3.iloc[0]*100).values, "--", lw=1.2, color=GREEN, label=f"名义 GDP + 头部溢价 {PREM*100:.1f}pp 线 ×{L3.iloc[-1]/L3.iloc[0]:.2f}")
    ext_start = last_q
    ax1.axvspan(ext_start, pd.Timestamp(AS_OF), color=GRAY, alpha=.12, lw=0); ax1.annotate("GDP 外推区", (ext_start, 100), xytext=(3, 3), textcoords="offset points", fontsize=7.5, color=GRAY)
    ax1.set_title(f"图 {k} · 从 {a.date()} 出发：资产 vs 名义 GDP 线（锚点 = 100，对数；含分红）"); ax1.legend(loc="upper left", ncol=2, fontsize=7.5)
    for name in ("QQQ 含分红", "SPY 含分红", "全市场 Wilshire 5000", "标普等权 RSP"):
        s, L1, L3 = base[name]; gap = (s/L1-1)*100; ax2.plot(gap.index, gap.values, lw=.9, color=COL[name], label=f"{name} 超出名义 GDP 线 {gap.iloc[-1]:+.0f}%")
    ax2.axhline(0, color="k", lw=.8); ax2.axvspan(ext_start, pd.Timestamp(AS_OF), color=GRAY, alpha=.12, lw=0); ax2.legend(loc="upper left", ncol=2, fontsize=7.5); ax2.set_ylabel("%")
    save(fig, f"0{1 if k == '2010' else 2}_anchor_{k}.png")
# earnings vs GDP
fig, ax = plt.subplots(figsize=(10, 4.4)); a = ANCH["2010"]
for ser, col, lab in [(ngdp[a:], RED, "名义 GDP"), (eps[a:], ORANGE, "标普500 每股盈利（滚动 12 个月，名义 = 价格 ÷ PE）"), (ndx_eps[a:], NAVY, "纳指100 前瞻每股盈利（价格 ÷ 前瞻 PE）"), (spx[a:], "#f4a261", "标普500 价格"), (ndx[a:], TEAL, "纳指100 价格")]:
    r = ser/ser.iloc[0]*100; ax.semilogy(r.index, r.values, lw=1, color=col, ls="-" if "价格" not in lab else "--", label=f"{lab} ×{r.iloc[-1]/100:.2f}")
ax.axvline(ANCH["2020"], color=GRAY, lw=.8, ls=":"); ax.set_title("图 3 · 2010 年起：盈利跑赢 GDP 多少，价格又跑赢盈利多少（2010-01 = 100，对数）"); ax.legend(loc="upper left", fontsize=7.5)
save(fig, "03_eps_vs_gdp.png")
# Buffett
fig, ax = plt.subplots(figsize=(10, 3.8)); ax.plot(br.index, br.values, lw=.9, color=PURPLE, label="Wilshire 5000 指数 ÷ 名义 GDP（十亿美元），相对值")
for k, a in ANCH.items(): ax.axvline(a, color=GRAY, lw=.8, ls=":"); ax.annotate(f"{k}: {br[a:].iloc[0]:.2f}", (a, br[a:].iloc[0]), xytext=(4, 6), textcoords="offset points", fontsize=8, color=GRAY)
ax.plot([br.index[-1]], [br.iloc[-1]], "o", color=RED, ms=5); ax.annotate(f"{br.iloc[-1]:.2f}（2010 的 {S['buffett']['ratio_vs2010']:.1f} 倍，2020 的 {S['buffett']['ratio_vs2020']:.1f} 倍）", (br.index[-1], br.iloc[-1]), xytext=(-6, 8), textcoords="offset points", fontsize=8, color=RED, ha="right", fontweight="bold")
ax.set_title("图 4 · 全市场市值 ÷ 名义 GDP（巴菲特指标，1990 起）"); ax.legend(loc="upper left")
save(fig, "04_buffett.png")
# EPS premium over GDP, long history
fig, ax = plt.subplots(figsize=(10, 3.8)); r1 = eps_y.loc[1970:]/eps_y[1970]*100; r2 = AN.gdp_nominal_bn.loc[1970:2024]/AN.gdp_nominal_bn[1970]*100
ax.semilogy(r1.index, r1.values, lw=1, color=ORANGE, label=f"标普500 每股盈利（年末）×{r1.iloc[-1]/100:.0f}"); ax.semilogy(r2.index, r2.values, lw=1, color=RED, label=f"名义 GDP ×{r2.iloc[-1]/100:.0f}")
ax.set_title(f"图 5 · 1970 年起：头部公司盈利比 GDP 快多少（1990–2024 年化差 {PREM*100:.1f} 个百分点，用作「头部溢价」）"); ax.legend(loc="upper left")
save(fig, "05_eps_premium.png")
