#!/usr/bin/env python
"""Lump sum vs DCA into QQQ, conditioned on how 'high' the start was (2009-era trend-deviation percentile).
Data: ../QQQ_现在高不高_危机后视角_2026-10-09/data (QQQ adj_close, NDX close). Cash earns 0%.
Outputs: results.csv, worst_starts.csv, lump_vs_dca.png"""
import sys, numpy as np, pandas as pd
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass
from pathlib import Path
HERE = Path(__file__).resolve().parent; D = HERE.parent/"QQQ_现在高不高_危机后视角_2026-10-09"/"data"
plt.rcParams.update({"font.family": ["Microsoft YaHei", "SimHei"], "axes.unicode_minus": False, "figure.dpi": 150, "axes.grid": True, "grid.alpha": .3, "font.size": 9})
q = pd.read_csv(D/"QQQ_daily.csv", parse_dates=["date"]).set_index("date").adj_close
n = pd.read_csv(D/"NDX_daily.csv", parse_dates=["date"]).set_index("date").close
# 2009-era trend deviation (same method as the 10-09 report)
s = n[n.index >= "2009-03-09"]; x = np.arange(len(s)); b, c = np.polyfit(x, np.log(s.values), 1); dev = pd.Series((s.values/np.exp(c+b*x)-1)*100, index=s.index)
pct = dev.rank(pct=True)*100  # percentile of each day within the era (in-sample, same as report)
NOW_PCT = float(pct.iloc[-1]); print("current era percentile", round(NOW_PCT, 1))
idx = q.index; pos = {d: i for i, d in enumerate(idx)}
month_starts = [pd.Timestamp(d) for d in q.groupby([idx.year, idx.month]).apply(lambda g: g.index[0]).values]  # first trading day of each month


def simulate(t, months, horizon_days):
    """invest 1 unit total: lump (months=0) or equal monthly tranches over `months` months starting at t. Return value path / capital."""
    i0 = pos[t]; end = i0 + horizon_days
    if end >= len(idx): return None
    path = q.iloc[i0:end+1].values
    if months == 0:
        v = path/path[0]
    else:
        ms = [d for d in month_starts if d >= t][:months]
        if len(ms) < months or pos[ms[-1]] > end: return None
        shares = np.zeros(len(path)); cash = np.ones(len(path))
        for k, d in enumerate(ms):
            j = pos[d]-i0; shares[j:] += (1/months)/path[j]; cash[j:] -= 1/months
        v = shares*path + cash
    return v


rows = []
H = {"3y": 756, "5y": 1260}
starts = [d for d in idx if d >= pd.Timestamp("2009-03-09") and d in pct.index]
for t in starts[::5]:  # weekly-ish sampling to keep it fast
    r = dict(start=t, pct=float(pct[t]))
    for hname, hd in H.items():
        for m in (0, 6, 12, 24):
            v = simulate(t, m, hd)
            if v is None: r[f"{hname}_m{m}"] = np.nan; r[f"{hname}_m{m}_mdd"] = np.nan; r[f"{hname}_m{m}_under1y"] = np.nan; continue
            r[f"{hname}_m{m}"] = (v[-1]-1)*100; r[f"{hname}_m{m}_mdd"] = (v.min()-1)*100; r[f"{hname}_m{m}_under1y"] = v[252] < 1 if len(v) > 252 else np.nan
    rows.append(r)
df = pd.DataFrame(rows); df.to_csv(HERE/"results.csv", index=False)


def summ(sub, label):
    out = []
    for hname in H:
        for m in (0, 6, 12, 24):
            col = f"{hname}_m{m}"; s_ = sub[col].dropna()
            if len(s_) == 0: continue
            out.append(dict(样本=label, 期限=hname, 方式=("一次性" if m == 0 else f"分 {m} 个月"), 起点数=len(s_), 中位回报=s_.median(), 最差=s_.min(), 最好=s_.max(),
                            亏损概率=(s_ < 0).mean()*100, 期间最深浮亏中位=sub[col+"_mdd"].dropna().median(), 期间最深浮亏最差=sub[col+"_mdd"].dropna().min(),
                            一年后仍亏概率=sub[col+"_under1y"].dropna().astype(float).mean()*100))
    return out


tab = []
tab += summ(df, "2009 起全部起点")
tab += summ(df[df.pct >= 80], "起点 ≥ 80 分位（偏高）")
tab += summ(df[df.pct >= 90], "起点 ≥ 90 分位（和现在一样）")
T = pd.DataFrame(tab); T.to_csv(HERE/"summary.csv", index=False, encoding="utf-8-sig", float_format="%.1f")
print(T.round(1).to_string())
# lump beats DCA-12m share
for label, sub in [("全部", df), ("≥80", df[df.pct >= 80]), ("≥90", df[df.pct >= 90])]:
    for h in H:
        d_ = sub[[f"{h}_m0", f"{h}_m12"]].dropna(); print(label, h, "一次性赢过分12个月的比例", round((d_[f"{h}_m0"] > d_[f"{h}_m12"]).mean()*100), "%", "n=", len(d_))
# named worst starts
worst = []
for t in ["2021-11-19", "2020-02-19", "2018-08-29", "2025-02-19", "2024-07-10", "2010-04-23", "2015-07-20"]:
    t = idx[idx.get_indexer([pd.Timestamp(t)], method="nearest")[0]]; r = dict(起点=str(t.date()), 起点分位=round(float(pct.get(t, np.nan)), 0))
    for m in (0, 12, 24):
        v3 = simulate(t, m, 756); v1 = simulate(t, m, 252)
        r[f"{'一次性' if m==0 else f'分{m}月'}_1年"] = None if v1 is None else round((v1[-1]-1)*100); r[f"{'一次性' if m==0 else f'分{m}月'}_3年"] = None if v3 is None else round((v3[-1]-1)*100)
        r[f"{'一次性' if m==0 else f'分{m}月'}_最深浮亏"] = None if v3 is None else round((v3.min()-1)*100)
    worst.append(r)
W = pd.DataFrame(worst); W.to_csv(HERE/"named_starts.csv", index=False, encoding="utf-8-sig"); print(W.to_string())

# chart: 3y outcome distribution, lump vs DCA12, high starts
fig, axes = plt.subplots(1, 2, figsize=(10, 3.8))
for ax, (label, sub) in zip(axes, [("2009 起全部起点", df), ("起点 ≥ 90 分位（和现在一样）", df[df.pct >= 90])]):
    for m, col, name in [(0, "#1f4e79", "一次性"), (12, "#e36c09", "分 12 个月"), (24, "#2e7d32", "分 24 个月")]:
        s_ = sub[f"3y_m{m}"].dropna(); ax.hist(s_, bins=30, alpha=.45, color=col, label=f"{name}：中位 {s_.median():+.0f}%，最差 {s_.min():+.0f}%")
    ax.axvline(0, color="k", lw=.8); ax.set_title(f"3 年后总回报分布 · {label}（n={len(sub)}）"); ax.legend(fontsize=7.5); ax.set_xlabel("%")
fig.tight_layout(); fig.savefig(HERE/"lump_vs_dca.png"); print("chart saved")
