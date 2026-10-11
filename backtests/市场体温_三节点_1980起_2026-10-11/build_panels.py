#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Three side-by-side panels per index: one node trough -> now per panel, its own trend line,
shared x/y axes so the slopes are directly comparable. Writes fig/03_ndx_three_panels.png, fig/01b_spx_three_panels.png"""
import json, sys, numpy as np, pandas as pd
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass
from pathlib import Path
HERE = Path(__file__).resolve().parent; D = HERE/"data"; F = HERE/"fig"
plt.rcParams.update({"font.family": ["Microsoft YaHei", "SimHei"], "axes.unicode_minus": False, "figure.dpi": 150,
                     "axes.grid": True, "grid.alpha": .3, "axes.spines.top": False, "axes.spines.right": False, "font.size": 9, "legend.fontsize": 8})
NAVY, ORANGE, RED, GREEN, GRAY, PURPLE, TEAL = "#1f4e79", "#e36c09", "#c00000", "#2e7d32", "#7f7f7f", "#6a3d9a", "#0b7285"
S = json.load(open(HERE/"stats_temp.json", encoding="utf-8")); AS_OF = S["as_of"]


def yh(l):
    return pd.read_csv(D/f"{l}_daily.csv", parse_dates=["date"]).set_index("date")["close"].dropna()


def trend(series, start):
    s = series[series.index >= start].dropna(); x = np.arange(len(s)); b, c = np.polyfit(x, np.log(s.values), 1)
    fit = pd.Series(np.exp(c+b*x), index=s.index); return fit, (s/fit-1)*100, (np.exp(b*252)-1)*100


def panels(series, troughs, title, fname, label):
    """troughs: dict era_name -> trough date (str). 2x3 grid, shared x (2008-> now) and shared y per row."""
    x0 = pd.Timestamp("2008-01-01"); x1 = series.index[-1] + pd.DateOffset(months=9)
    full = series[series.index >= x0]
    fig, axes = plt.subplots(2, 3, figsize=(12.5, 6.8), sharex=True, gridspec_kw={"height_ratios": [1.6, 1]})
    cols = [ORANGE, TEAL, PURPLE]
    ymin, ymax = full.min()*0.9, full.max()*1.25
    dev_all = []
    for j, ((era, d), col) in enumerate(zip(troughs.items(), cols)):
        d = pd.Timestamp(d); fit, dev, cagr = trend(series, d); seg = series[series.index >= d]
        ax = axes[0, j]
        ax.semilogy(full.index, full.values, lw=.7, color=GRAY, alpha=.6)
        ax.semilogy(seg.index, seg.values, lw=.9, color=NAVY)
        ax.semilogy(fit.index, fit.values, "--", lw=1.4, color=col)
        ax.axvline(d, color=GREEN, lw=.8, ls=":")
        ax.set_ylim(ymin, ymax); ax.set_xlim(x0, x1)
        pct = float((dev < dev.iloc[-1]).mean()*100)
        ax.set_title(f"{era} 底起（{d.date()}）\n趋势年化 {cagr:.1f}%  ·  当前偏离 {dev.iloc[-1]:+.0f}%  ·  本时代 {pct:.0f} 分位", fontsize=9.5, color=col)
        ax.plot([seg.index[-1]], [seg.iloc[-1]], "o", color=RED, ms=4)
        ax2 = axes[1, j]
        ax2.plot(dev.index, dev.values, lw=.8, color=col)
        ax2.axhline(0, color="k", lw=.7)
        ax2.axhline(dev.quantile(.9), color=RED, ls=":", lw=1); ax2.axhline(dev.quantile(.1), color=GREEN, ls=":", lw=1)
        ax2.annotate(f"90 分位 {dev.quantile(.9):+.0f}%", (x0, dev.quantile(.9)), xytext=(4, 3), textcoords="offset points", fontsize=7.5, color=RED)
        ax2.annotate(f"10 分位 {dev.quantile(.1):+.0f}%", (x0, dev.quantile(.1)), xytext=(4, -10), textcoords="offset points", fontsize=7.5, color=GREEN)
        ax2.plot([dev.index[-1]], [dev.iloc[-1]], "o", color=RED, ms=4)
        ax2.annotate(f"{dev.iloc[-1]:+.0f}%", (dev.index[-1], dev.iloc[-1]), xytext=(5, 3), textcoords="offset points", fontsize=8, color=RED, fontweight="bold")
        ax2.set_xlim(x0, x1); dev_all.append(dev)
        if j == 0: ax.set_ylabel(f"{label}（对数）"); ax2.set_ylabel("偏离趋势线 %")
    lo = min(d.min() for d in dev_all) - 5; hi = max(d.max() for d in dev_all) + 5
    for j in range(3): axes[1, j].set_ylim(lo, hi)
    fig.suptitle(title, fontsize=11, y=.995); fig.tight_layout(); fig.savefig(F/fname, dpi=150); plt.close(fig); print("fig", fname)


ndx, spx = yh("NDX"), yh("GSPC")
NT = S["nodes"]["ndx_troughs"]; ST = S["nodes"]["spx_troughs"]
panels(ndx, NT, f"图 3 · 纳指100：同一价格，三把尺子并列（灰线 = 2008 起全程，蓝线 = 该节点底部之后，虚线 = 从该底部拟合的趋势线；截至 {AS_OF}）", "03_ndx_three_panels.png", "纳指100")
panels(spx, ST, f"图 1b · 标普500：同一价格，三把尺子并列（灰线 = 2008 起全程，蓝线 = 该节点底部之后，虚线 = 从该底部拟合的趋势线；截至 {AS_OF}）", "01b_spx_three_panels.png", "标普500")
