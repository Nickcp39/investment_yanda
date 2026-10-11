#!/usr/bin/env python
"""Mandate: ~USD 42-45k, 5-year lock, principal guaranteed by the manager, ETF only, no leverage.
Compare candidate assets and mixes on the metrics a guarantor cares about (worst 5y, shortfall) and the
metrics the owner cares about (median 5y). Common window = GLD inception 2004-11-18 -> last close.
Also: historical test of a principal-protection structure (5y Treasury held to maturity + QQQ remainder).
Outputs: fig/*.png, metrics.csv, metrics_2009.csv, stats_alloc.json"""
import json, sys, numpy as np, pandas as pd
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass
from pathlib import Path
HERE = Path(__file__).resolve().parent; D = HERE/"data"; F = HERE/"fig"; F.mkdir(exist_ok=True)
plt.rcParams.update({"font.family": ["Microsoft YaHei", "SimHei"], "axes.unicode_minus": False, "figure.dpi": 150, "axes.grid": True, "grid.alpha": .3,
                     "axes.spines.top": False, "axes.spines.right": False, "font.size": 9, "legend.fontsize": 8, "axes.titlesize": 11})
S = {}


def load(l, col="adj_close"):
    return pd.read_csv(D/f"{l}_daily.csv", parse_dates=["date"]).set_index("date")[col]


px = pd.DataFrame({k: load(k) for k in ["QQQ", "SPY", "RSP", "EFA", "EEM", "GLD", "IEF", "TLT", "BRKB"]})
irx = load("IRX", "close"); fvx = load("FVX", "close"); tnx = load("TNX", "close"); cny = load("CNY", "close")
START = px.dropna().index[0]; px = px[px.index >= START].ffill().dropna(); END = px.index[-1]
# cash index from 13-week T-bill yield (daily accrual)
cash = (1 + (irx.reindex(px.index).ffill()/100)/252).cumprod(); px["CASH"] = cash/cash.iloc[0]
S["window"] = dict(start=str(START.date()), end=str(END.date()), years=(END-START).days/365.25)
print("window", S["window"])
ret = px.pct_change().fillna(0)
NAMES = {"QQQ": "QQQ 纳指100", "SPY": "SPY 标普500", "RSP": "RSP 标普等权", "EFA": "EFA 发达市场(非美)", "EEM": "EEM 新兴市场", "GLD": "GLD 黄金",
         "IEF": "IEF 美债7-10年", "TLT": "TLT 美债20年+", "BRKB": "BRK.B 伯克希尔", "CASH": "现金(T-bill)"}
MIXES = {"QQQ50/SPY50": {"QQQ": .5, "SPY": .5}, "SPY60/IEF40": {"SPY": .6, "IEF": .4}, "QQQ60/IEF40": {"QQQ": .6, "IEF": .4},
         "QQQ50/GLD25/IEF25": {"QQQ": .5, "GLD": .25, "IEF": .25}, "SPY40/QQQ20/GLD20/IEF20": {"SPY": .4, "QQQ": .2, "GLD": .2, "IEF": .2},
         "QQQ40/SPY30/BRK30": {"QQQ": .4, "SPY": .3, "BRKB": .3}, "QQQ70/CASH30": {"QQQ": .7, "CASH": .3}, "QQQ50/GLD50": {"QQQ": .5, "GLD": .5}}


def mix_index(w):
    """monthly-rebalanced portfolio value, start 1"""
    months = px.index.to_period("M"); V = []; v = 1.0
    for m, g in ret.groupby(months):
        hold = {k: v*w_ for k, w_ in w.items()}
        for d, r in g.iterrows():
            for k in hold: hold[k] *= (1 + r[k])
            v = sum(hold.values()); V.append((d, v))
    return pd.Series(dict(V))


idx = {k: px[k]/px[k].iloc[0] for k in px.columns}
for name, w in MIXES.items(): idx[name] = mix_index(w)
# principal-protection structure: f = 1/(1+y5)^5 in a 5y Treasury held to maturity, 1-f in QQQ, buy-and-hold per start date
H = 1260
f5 = fvx.reindex(px.index).ffill()/100


def five_year(series):
    return (series.shift(-H)/series - 1).dropna()


def metrics(s, label, start=None):
    s = s[s.index >= start] if start else s
    r5 = five_year(s)*100; r1 = (s.shift(-252)/s - 1).dropna()*100; dd = (s/s.cummax()-1)*100
    yrs = (s.index[-1]-s.index[0]).days/365.25; lr = np.log(s).diff().dropna()
    return dict(组合=label, 年化=((s.iloc[-1]/s.iloc[0])**(1/yrs)-1)*100, 年化波动=lr.std()*np.sqrt(252)*100, 最大回撤=dd.min(), 最差1年=r1.min(),
                五年中位=r5.median(), 五年5分位=r5.quantile(.05), 五年最差=r5.min(), 五年最差起点=str(r5.idxmin().date()) if len(r5) else "",
                五年为负比例=(r5 < 0).mean()*100, 担保人期望赔付=np.maximum(0, -r5).mean(), 担保人最大赔付=max(0, -r5.min()), n5=len(r5))


rows, rows09 = [], []
for k, s in idx.items():
    rows.append(metrics(s, NAMES.get(k, k))); rows09.append(metrics(s, NAMES.get(k, k), "2009-03-09"))
# protection structure (historical, with the 5y yield at each start)
q = px["QQQ"]; Q = (q.shift(-H)/q).dropna(); f = (1/(1+f5.reindex(Q.index))**5)
prot = ((1-f)*Q)*100  # return on principal, floor 0 by construction
prot_s = pd.Series(prot.values, index=Q.index)
rows.append(dict(组合="保本结构: 5年国债到期 + 其余QQQ", 年化=np.nan, 年化波动=np.nan, 最大回撤=np.nan, 最差1年=np.nan, 五年中位=prot_s.median(), 五年5分位=prot_s.quantile(.05),
                 五年最差=prot_s.min(), 五年最差起点=str(prot_s.idxmin().date()), 五年为负比例=0.0, 担保人期望赔付=0.0, 担保人最大赔付=0.0, n5=len(prot_s)))
p09 = prot_s[prot_s.index >= "2009-03-09"]
rows09.append(dict(组合="保本结构: 5年国债到期 + 其余QQQ", 年化=np.nan, 年化波动=np.nan, 最大回撤=np.nan, 最差1年=np.nan, 五年中位=p09.median(), 五年5分位=p09.quantile(.05),
                   五年最差=p09.min(), 五年最差起点=str(p09.idxmin().date()), 五年为负比例=0.0, 担保人期望赔付=0.0, 担保人最大赔付=0.0, n5=len(p09)))
y5 = float(fvx.dropna().iloc[-1]); fnow = 1/(1+y5/100)**5
prot_today = pd.Series(((1-fnow)*Q).values*100, index=Q.index); pt09 = prot_today[prot_today.index >= "2009-03-09"]
LBL_T = f"保本结构@当前{y5:.2f}%: {fnow*100:.0f}%国债+{(1-fnow)*100:.0f}%QQQ"
for R, ser in ((rows, prot_today), (rows09, pt09)):
    R.append(dict(组合=LBL_T, 年化=np.nan, 年化波动=np.nan, 最大回撤=np.nan, 最差1年=np.nan, 五年中位=ser.median(), 五年5分位=ser.quantile(.05), 五年最差=ser.min(),
                  五年最差起点=str(ser.idxmin().date()), 五年为负比例=0.0, 担保人期望赔付=0.0, 担保人最大赔付=0.0, n5=len(ser)))
M = pd.DataFrame(rows); M09 = pd.DataFrame(rows09)
M.to_csv(HERE/"metrics.csv", index=False, encoding="utf-8-sig", float_format="%.1f"); M09.to_csv(HERE/"metrics_2009.csv", index=False, encoding="utf-8-sig", float_format="%.1f")
print(M.round(1).to_string()); print(M09.round(1).to_string())
# current protection structure numbers
y5 = float(fvx.dropna().iloc[-1]); fnow = 1/(1+y5/100)**5
S["protect"] = dict(y5_now=y5, y5_date=str(fvx.dropna().index[-1].date()), bond_share=fnow*100, equity_share=(1-fnow)*100,
                    y5_median_2010_2021=float(fvx["2010":"2021"].median()), f_at_1pct=100/(1.01**5), f_at_2pct=100/(1.02**5),
                    upside_at_qqq_median=(1-fnow)*(1+M.loc[M.组合 == "QQQ 纳指100", "五年中位"].iloc[0]/100)*100,
                    upside_at_qqq_worst09=(1-fnow)*(1+M09.loc[M09.组合 == "QQQ 纳指100", "五年最差"].iloc[0]/100)*100,
                    upside_at_qqq_worst02=(1-fnow)*(1-0.28)*100, upside_at_qqq_worst99=(1-fnow)*(1-0.69)*100,
                    tbill_now=float(irx.dropna().iloc[-1]), tnx_now=float(tnx.dropna().iloc[-1]))
S["protect"].update(label_today=LBL_T, today_median=float(prot_today.median()), today_p5=float(prot_today.quantile(.05)), today_worst=float(prot_today.min()),
                    today_worst09=float(pt09.min()), today_median09=float(pt09.median()), hist_median=float(prot_s.median()), hist_worst=float(prot_s.min()))
# correlations (monthly)
mret = px.resample("ME").last().pct_change().dropna(); C = mret[["QQQ", "SPY", "EFA", "EEM", "GLD", "IEF", "TLT", "BRKB"]].corr(); C.to_csv(HERE/"corr_monthly.csv", float_format="%.2f")
S["corr_qqq"] = {k: float(v) for k, v in C["QQQ"].round(2).items()}
# FX
cnym = cny.resample("ME").last().dropna(); fx5 = (cnym.shift(-60)/cnym - 1).dropna()*100
S["fx"] = dict(now=float(cny.dropna().iloc[-1]), date=str(cny.dropna().index[-1].date()), max5y=float(fx5.max()), min5y=float(fx5.min()), median5y=float(fx5.median()),
               max5y_date=str(fx5.idxmax().date()), min5y_date=str(fx5.idxmin().date()), hi=float(cnym.max()), hi_date=str(cnym.idxmax().date()), lo=float(cnym.min()), lo_date=str(cnym.idxmin().date()))
S["metrics"] = M.round(2).to_dict("records"); S["metrics_2009"] = M09.round(2).to_dict("records")
json.dump(S, open(HERE/"stats_alloc.json", "w", encoding="utf-8"), indent=2, ensure_ascii=False, default=float)
print(json.dumps({k: S[k] for k in ("protect", "fx", "corr_qqq")}, indent=1, ensure_ascii=False, default=float))

# ---------- charts ----------
NAVY, ORANGE, RED, GREEN, GRAY, PURPLE, TEAL, GOLD = "#1f4e79", "#e36c09", "#c00000", "#2e7d32", "#7f7f7f", "#6a3d9a", "#0b7285", "#b8860b"
# F1 growth
fig, ax = plt.subplots(figsize=(10, 4.6))
for k, col, lw in [("QQQ", NAVY, 1.2), ("SPY", ORANGE, 1), ("BRKB", PURPLE, .9), ("GLD", GOLD, .9), ("IEF", GREEN, .9), ("EFA", GRAY, .8), ("SPY60/IEF40", TEAL, 1), ("QQQ50/GLD25/IEF25", RED, 1.1)]:
    s = idx[k]; ax.semilogy(s.index, s.values, lw=lw, color=col, label=f"{NAMES.get(k, k)}  ×{s.iloc[-1]:.1f}")
ax.set_title(f"图 1 · 候选资产与组合：{START.year}-{START.month:02d} 投入 1 元的增长（对数坐标，含分红，月度再平衡）"); ax.legend(loc="upper left", ncol=2); ax.set_ylabel("倍")
fig.tight_layout(); fig.savefig(F/"01_growth.png"); plt.close(fig)
# F2 scatter worst5y vs median5y
fig, ax = plt.subplots(figsize=(10, 5.2))
for _, r in M.iterrows():
    is_mix = "/" in r.组合 or "保本" in r.组合; col = RED if "保本" in r.组合 else (TEAL if is_mix else NAVY)
    ax.scatter(r.五年最差, r.五年中位, s=40, color=col, zorder=3); ax.annotate(r.组合, (r.五年最差, r.五年中位), xytext=(5, 4), textcoords="offset points", fontsize=7.5)
ax.axvline(0, color="k", lw=.8); ax.set_xlabel("最差 5 年窗口回报 %（担保人的尾部，越右越好）"); ax.set_ylabel("5 年窗口中位回报 %（委托人的期望，越上越好）")
ax.set_title(f"图 2 · 担保人视角的取舍：{START.year} 年以来所有 5 年窗口（蓝=单资产，青=混合，红=保本结构）")
fig.tight_layout(); fig.savefig(F/"02_frontier.png"); plt.close(fig)
# F3 rolling 5y
fig, ax = plt.subplots(figsize=(10, 4.4))
for k, col in [("QQQ", NAVY), ("SPY", ORANGE), ("SPY60/IEF40", TEAL), ("QQQ50/GLD25/IEF25", RED)]:
    r5 = five_year(idx[k])*100; ax.plot(r5.index, r5.values, lw=1, color=col, label=NAMES.get(k, k))
ax.plot(prot_s.index, prot_s.values, lw=1.2, color=GREEN, ls="--", label="保本结构（按各起点当时的 5 年国债收益率）")
ax.plot(prot_today.index, prot_today.values, lw=1.2, color=PURPLE, ls="--", label=f"保本结构按当前收益率 {y5:.2f}%（{(1-fnow)*100:.0f}% QQQ）")
ax.axhline(0, color="k", lw=.8); ax.set_ylabel("%"); ax.set_xlabel("5 年窗口起点"); ax.legend(loc="upper left", ncol=2)
ax.set_title("图 3 · 每个起点往后 5 年的总回报：谁跌破过零线")
fig.tight_layout(); fig.savefig(F/"03_rolling5y.png"); plt.close(fig)
# F4 drawdowns
fig, ax = plt.subplots(figsize=(10, 3.8))
for k, col in [("QQQ", NAVY), ("QQQ50/GLD25/IEF25", RED), ("SPY60/IEF40", TEAL), ("GLD", GOLD)]:
    s = idx[k]; dd = (s/s.cummax()-1)*100; ax.plot(dd.index, dd.values, lw=.8, color=col, label=f"{NAMES.get(k, k)} 最深 {dd.min():.0f}%")
ax.set_ylabel("距前高 %"); ax.legend(loc="lower left", ncol=2); ax.set_title("图 4 · 回撤：期中浮亏有多深（保本只在到期日兑现，中途要能拿住）")
fig.tight_layout(); fig.savefig(F/"04_drawdown.png"); plt.close(fig)
# F5 5y treasury yield and bond share needed
fig, ax = plt.subplots(figsize=(10, 3.8)); fv = fvx.dropna()["2000":]
ax.plot(fv.index, fv.values, lw=.9, color=NAVY, label="美国 5 年期国债收益率 %"); ax.set_ylabel("%")
ax2 = ax.twinx(); fshare = 100/(1+fv/100)**5; ax2.plot(fshare.index, fshare.values, lw=.9, color=RED, ls="--", label="保本所需国债占比 %"); ax2.set_ylabel("保本所需国债占比 %"); ax2.set_ylim(70, 100); ax2.grid(False)
ax.plot([fv.index[-1]], [fv.iloc[-1]], "o", color=NAVY); ax.annotate(f"{fv.iloc[-1]:.2f}%", (fv.index[-1], fv.iloc[-1]), xytext=(6, 4), textcoords="offset points", color=NAVY, fontsize=8, fontweight="bold")
ax2.annotate(f"{fshare.iloc[-1]:.0f}%", (fshare.index[-1], fshare.iloc[-1]), xytext=(6, -10), textcoords="offset points", color=RED, fontsize=8, fontweight="bold")
h1, l1 = ax.get_legend_handles_labels(); h2, l2 = ax2.get_legend_handles_labels(); ax.legend(h1+h2, l1+l2, loc="upper right")
ax.set_title("图 5 · 保本结构的成本：5 年国债收益率越高，锁住本金所需的债券越少，留给 QQQ 的越多")
fig.tight_layout(); fig.savefig(F/"05_fvx_bondshare.png"); plt.close(fig)
# F6 FX
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 3.6), gridspec_kw={"width_ratios": [2, 1]})
ax1.plot(cnym.index, cnym.values, lw=1, color=NAVY); ax1.set_title(f"图 6 · 美元兑人民币 2001–{END.year}（现 {S['fx']['now']:.2f}）"); ax1.set_ylabel("USD/CNY")
ax2.hist(fx5, bins=25, color=NAVY, alpha=.6); ax2.axvline(0, color="k", lw=.8); ax2.set_title("任意 5 年里美元对人民币的变动 %"); ax2.set_xlabel("%（负 = 美元贬值）")
fig.tight_layout(); fig.savefig(F/"06_fx.png"); plt.close(fig)
print("charts saved")
