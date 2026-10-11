#!/usr/bin/env python
"""Is QQQ 'high' right now?  Price-based gauges, each with its historical percentile.
Inputs: data/*_daily.csv  (from fetch_prices.py).  Outputs: snapshot.json, gauges.csv, chart png.
"""
import json, sys, numpy as np, pandas as pd
from pathlib import Path
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass
HERE = Path(__file__).resolve().parent
def load(l):
    df = pd.read_csv(HERE/"data"/f"{l}_daily.csv", parse_dates=["date"]).set_index("date")
    return df
qqq, ndx, spy = load("QQQ"), load("NDX"), load("SPY")
out = {"as_of": str(qqq.index[-1].date()), "qqq_close": float(qqq.close.iloc[-1])}
gauges = []
def pct_rank(series, value):
    s = series.dropna(); return float((s < value).mean()*100)

# ---- 1. distance from all-time high / 52w high (price, QQQ) ----
p = qqq.close
ath = p.cummax(); dd = p/ath - 1
out["ath"] = float(ath.iloc[-1]); out["ath_date"] = str(p.idxmax().date())
out["drawdown_from_ath_pct"] = float(dd.iloc[-1]*100)
hi52 = p.rolling(252).max(); out["pct_from_52w_high"] = float((p.iloc[-1]/hi52.iloc[-1]-1)*100)
days_since_ath = (p.index[-1]-p.idxmax()).days; out["days_since_ath"] = int(days_since_ath)

# ---- 2. % above 200-day & 50-day MA (NDX since 1985 for a long base) ----
n = ndx.close
for w in (50, 200):
    ma = n.rolling(w).mean(); dev = (n/ma-1)*100
    v = float(dev.iloc[-1]); r = pct_rank(dev, v)
    gauges.append({"gauge": f"NDX vs {w}日均线 (%)", "value": round(v,1), "pctile_since_1985": round(r,0),
                   "hist_median": round(float(dev.median()),1), "hist_p90": round(float(dev.quantile(.9)),1),
                   "hist_max": round(float(dev.max()),1)})
    out[f"ndx_vs_{w}dma_pct"] = v; out[f"ndx_vs_{w}dma_pctile"] = r

# ---- 3. trailing total returns (QQQ adj_close) and percentile vs all windows ----
a = qqq.adj_close
for yrs in (1, 3, 5, 10):
    k = 252*yrs
    tr = a/a.shift(k)-1
    v = float(tr.iloc[-1]*100); r = pct_rank(tr*100, v)
    gauges.append({"gauge": f"QQQ 过去{yrs}年总回报 (%)", "value": round(v,1), "pctile_since_1999": round(r,0),
                   "hist_median": round(float(tr.median()*100),1), "hist_p90": round(float(tr.quantile(.9)*100),1),
                   "hist_max": round(float(tr.max()*100),1)})
    out[f"qqq_trailing_{yrs}y_pct"] = v; out[f"qqq_trailing_{yrs}y_pctile"] = r
    # since 2009 base too
    tr09 = tr[tr.index >= "2009-03-09"]
    out[f"qqq_trailing_{yrs}y_pctile_since2009"] = pct_rank(tr09*100, v)

# ---- 4. deviation from long-run log-linear trend ----
def trend_dev(series, start):
    s = series[series.index >= start].dropna()
    x = np.arange(len(s)); y = np.log(s.values)
    b, c = np.polyfit(x, y, 1)
    fit = np.exp(c + b*x); dev = (s.values/fit-1)*100
    cagr = (np.exp(b*252)-1)*100
    return pd.Series(dev, index=s.index), cagr
for label, ser, start in (("NDX 1985起", n, "1985-10-01"), ("NDX 2009起", n, "2009-03-09"), ("QQQ(含息) 1999起", a, "1999-03-10")):
    dev, cagr = trend_dev(ser, start)
    v = float(dev.iloc[-1]); r = pct_rank(dev, v)
    gauges.append({"gauge": f"偏离对数趋势线 {label} (%)", "value": round(v,1), "pctile": round(r,0),
                   "hist_median": round(float(dev.median()),1), "hist_p90": round(float(dev.quantile(.9)),1),
                   "hist_max": round(float(dev.max()),1), "trend_cagr_pct": round(cagr,1)})
    out[f"trend_dev_{label}"] = {"dev_pct": v, "pctile": r, "trend_cagr": cagr, "max_dev": float(dev.max()),
                                 "max_dev_date": str(dev.idxmax().date())}
    if label == "NDX 1985起": dev_long = dev
    if label == "NDX 2009起": dev_09 = dev

# ---- 5. QQQ vs SPY relative strength: ratio of adj prices vs its own trend ----
rel = (qqq.adj_close/spy.adj_close).dropna()
rel_dev, rel_cagr = trend_dev(rel, "1999-03-10")
v = float(rel_dev.iloc[-1]); r = pct_rank(rel_dev, v)
gauges.append({"gauge": "QQQ/SPY 比值偏离趋势 (%)", "value": round(v,1), "pctile": round(r,0),
               "hist_median": round(float(rel_dev.median()),1), "hist_p90": round(float(rel_dev.quantile(.9)),1),
               "hist_max": round(float(rel_dev.max()),1), "trend_cagr_pct": round(rel_cagr,1)})
out["qqq_spy_ratio"] = {"now": float(rel.iloc[-1]), "dev_pct": v, "pctile": r,
                        "peak_2000": float(rel[:"2000-12-31"].max()), "peak_2000_date": str(rel[:"2000-12-31"].idxmax().date())}

# ---- 6. YTD and from 2025 close ----
y25 = a[a.index <= "2025-12-31"].iloc[-1]; out["qqq_ytd_total_pct"] = float((a.iloc[-1]/y25-1)*100)

# ---- 7. realized vol last 60d vs history ----
lr = np.log(a).diff(); vol60 = lr.rolling(60).std()*np.sqrt(252)*100
out["vol60_pct"] = float(vol60.iloc[-1]); out["vol60_pctile"] = pct_rank(vol60, vol60.iloc[-1])

pd.DataFrame(gauges).to_csv(HERE/"gauges.csv", index=False, encoding="utf-8-sig")
json.dump(out, open(HERE/"snapshot.json","w",encoding="utf-8"), indent=2, ensure_ascii=False, default=float)
print(json.dumps(out, indent=2, ensure_ascii=False, default=float))
print(pd.DataFrame(gauges).to_string())

# ---- chart ----
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
plt.rcParams["font.family"] = ["Microsoft YaHei", "SimHei", "DejaVu Sans"]; plt.rcParams["axes.unicode_minus"] = False
fig, axes = plt.subplots(3, 1, figsize=(12, 12), sharex=False)
ax = axes[0]; s = n[n.index >= "1985-10-01"]
x = np.arange(len(s)); b, c = np.polyfit(x, np.log(s.values), 1)
ax.semilogy(s.index, s.values, lw=1, color="#1f4e79", label="纳指100 (NDX)")
ax.semilogy(s.index, np.exp(c+b*x), lw=1.2, ls="--", color="#c00000", label=f"1985起对数趋势线 (年化 {(np.exp(b*252)-1)*100:.1f}%)")
ax.set_title(f"纳指100 价格 vs 长期趋势线  (截至 {out['as_of']})"); ax.legend(); ax.grid(alpha=.3)
ax = axes[1]
ax.plot(dev_long.index, dev_long.values, lw=1, color="#1f4e79", label="偏离 1985 起趋势线 (%)")
ax.plot(dev_09.index, dev_09.values, lw=1, color="#e36c09", label="偏离 2009 起趋势线 (%)")
ax.axhline(0, color="k", lw=.8); ax.axhline(dev_long.quantile(.9), color="#c00000", ls=":", lw=1, label="1985起 90 分位")
ax.set_title("偏离趋势线的百分比"); ax.legend(); ax.grid(alpha=.3)
ax = axes[2]
dev200 = (n/n.rolling(200).mean()-1)*100
ax.plot(dev200.index, dev200.values, lw=.8, color="#1f4e79", label="NDX 相对 200 日均线 (%)")
ax.axhline(0, color="k", lw=.8); ax.axhline(dev200.quantile(.9), color="#c00000", ls=":", lw=1, label="90 分位")
ax.axhline(dev200.quantile(.1), color="#2e7d32", ls=":", lw=1, label="10 分位")
ax.set_title("NDX 相对 200 日均线"); ax.legend(); ax.grid(alpha=.3)
plt.tight_layout(); plt.savefig(HERE/"qqq_level_check_2026-10-08.png", dpi=130)
print("chart saved")
