#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Four side-by-side panels per asset, one cycle trough per panel (2000 / 2008 / 2015 / 2021 cycles).
Each panel has its OWN calendar x-axis: from that trough to today (+3y dashed extension of the fitted line).
y = actual price (log). Each panel fits ln P = c + b*t on its own era and prints the formula + implied levels.
Writes fig/03_ndx_four_panels.png, 01b_spx_four_panels.png, 04b_gold_four_panels.png, panel_fits.json"""
import json, sys, numpy as np, pandas as pd
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt, matplotlib.dates as mdates
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass
from pathlib import Path
HERE = Path(__file__).resolve().parent; D = HERE/"data"; F = HERE/"fig"
plt.rcParams.update({"font.family": ["Microsoft YaHei", "SimHei"], "axes.unicode_minus": False, "figure.dpi": 150,
                     "axes.grid": True, "grid.alpha": .3, "axes.spines.top": False, "axes.spines.right": False, "font.size": 9, "legend.fontsize": 8})
NAVY, ORANGE, RED, GREEN, GRAY, PURPLE, TEAL, BROWN = "#1f4e79", "#e36c09", "#c00000", "#2e7d32", "#7f7f7f", "#6a3d9a", "#0b7285", "#8c564b"
S = json.load(open(HERE/"stats_temp.json", encoding="utf-8")); AS_OF = S["as_of"]; EXT = 3.0
OUT = {}


def yh(l):
    return pd.read_csv(D/f"{l}_daily.csv", parse_dates=["date"]).set_index("date")["close"].dropna()


def fit_era(series, d):
    seg = series[series.index >= d].dropna(); t = np.asarray((seg.index - d).days/365.25)
    b, c = np.polyfit(t, np.log(seg.values), 1)  # ln P = c + b t, t in years since trough
    fit = np.exp(c + b*t); dev = pd.Series((seg.values/fit - 1)*100, index=seg.index)
    return seg, t, b, c, fit, dev


COLS = {"2000": BROWN, "2008": ORANGE, "2015": TEAL, "2021": PURPLE}


def panels(series, troughs, title, fname, label, unit="", figw=None):
    n = len(troughs); fig, axes = plt.subplots(2, n, figsize=(figw or 3.6*n + 0.1, 7.4), gridspec_kw={"height_ratios": [1.7, 1]}, squeeze=False)
    cols = [COLS[e] for e in troughs]; OUT.setdefault(label, {}); devs = []
    for j, ((era, d), col) in enumerate(zip(troughs.items(), cols)):
        d = pd.Timestamp(d); seg, t, b, c, fit, dev = fit_era(series, d); p0 = float(seg.iloc[0]); g = (np.exp(b)-1)*100
        t_now = float(t[-1]); pct = float((dev < dev.iloc[-1]).mean()*100)
        lvl = {k: float(np.exp(c + b*(t_now + k))) for k in (1, 3, 5)}
        tx = np.linspace(t_now, t_now + EXT, 60); dx = [d + pd.Timedelta(days=float(v*365.25)) for v in tx]
        OUT[label][era] = dict(start=str(d.date()), p0=p0, a=float(np.exp(c)), g=float(g), b=float(b), c=float(c), years=t_now, now=float(seg.iloc[-1]),
                               dev=float(dev.iloc[-1]), pct=pct, p90=float(dev.quantile(.9)), p10=float(dev.quantile(.1)), implied=lvl)
        ax = axes[0, j]
        ax.semilogy(seg.index, seg.values, lw=.9, color=NAVY)
        ax.semilogy(seg.index, fit, "--", lw=1.4, color=col)
        ax.semilogy(dx, np.exp(c + b*tx), ":", lw=1.3, color=col)
        ax.plot([seg.index[-1]], [seg.iloc[-1]], "o", color=RED, ms=4)
        ax.annotate(f"{seg.iloc[-1]:,.0f}", (seg.index[-1], seg.iloc[-1]), xytext=(4, -12), textcoords="offset points", fontsize=8, color=RED, fontweight="bold")
        ax.annotate(f"若延续\n3 年后 {lvl[3]:,.0f}", (dx[-1], np.exp(c + b*tx[-1])), xytext=(-4, 6), textcoords="offset points", fontsize=7.5, color=col, ha="right")
        ax.set_title(f"{era} 周期底起 · {d.date()} · {label} {p0:,.0f}{unit}", fontsize=9.3, color=col)
        txt = (f"P = {np.exp(c):,.0f} × {1+g/100:.3f}^t\nln P = {c:.3f} + {b:.4f}·t\nt = 自 {d.date()} 起的年数（现 {t_now:.1f}）\n"
               f"年化 {g:.1f}%\n当前偏离 {dev.iloc[-1]:+.0f}%，本时代 {pct:.0f} 分位\n若延续：1 年 {lvl[1]:,.0f} · 5 年 {lvl[5]:,.0f}")
        ax.text(0.03, 0.97, txt, transform=ax.transAxes, va="top", ha="left", fontsize=7.6, color=col, bbox=dict(boxstyle="round,pad=0.35", fc="white", ec=col, alpha=.92))
        x0 = d - pd.Timedelta(days=90); x1 = dx[-1] + pd.Timedelta(days=120); ax.set_xlim(x0, x1)
        ylo = seg.min()*0.85; yhi = max(seg.max(), float(np.exp(c + b*tx[-1])))*1.9; ax.set_ylim(ylo, yhi)
        ax.xaxis.set_major_locator(mdates.YearLocator(base=(4 if t_now > 15 else (2 if t_now > 6 else 1)))); ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
        if j == 0: ax.set_ylabel(f"{label}{unit}（对数）")
        ax2 = axes[1, j]; ax2.plot(dev.index, dev.values, lw=.8, color=col); ax2.axhline(0, color="k", lw=.7)
        ax2.axhline(dev.quantile(.9), color=RED, ls=":", lw=1); ax2.axhline(dev.quantile(.1), color=GREEN, ls=":", lw=1)
        ax2.annotate(f"90 分位 {dev.quantile(.9):+.0f}%", (d, dev.quantile(.9)), xytext=(3, 3), textcoords="offset points", fontsize=7.3, color=RED)
        ax2.annotate(f"10 分位 {dev.quantile(.1):+.0f}%", (d, dev.quantile(.1)), xytext=(3, -10), textcoords="offset points", fontsize=7.3, color=GREEN)
        ax2.plot([dev.index[-1]], [dev.iloc[-1]], "o", color=RED, ms=4)
        ax2.annotate(f"{dev.iloc[-1]:+.0f}%", (dev.index[-1], dev.iloc[-1]), xytext=(4, 3), textcoords="offset points", fontsize=8, color=RED, fontweight="bold")
        ax2.set_xlim(x0, x1); ax2.xaxis.set_major_locator(ax.xaxis.get_major_locator()); ax2.xaxis.set_major_formatter(mdates.DateFormatter("%Y")); devs.append(dev)
        if j == 0: ax2.set_ylabel("实际价格偏离趋势线 %")
    lo = min(v.min() for v in devs) - 5; hi = max(v.max() for v in devs) + 5
    for j in range(n): axes[1, j].set_ylim(lo, hi)
    fig.suptitle(title, fontsize=11, y=.995); fig.tight_layout(); fig.savefig(F/fname, dpi=150); plt.close(fig); print("fig", fname)


ndx, spx = yh("NDX"), yh("GSPC")
gold = pd.read_csv(D/"gold_lbma_pm_daily.csv", parse_dates=[0]); gold = gold.set_index(gold.columns[0]).iloc[:, 0].astype(float).dropna()
gcf = yh("GCF"); gold = pd.concat([gold, gcf[gcf.index > gold.index[-1]]])


def troughs(s, windows):
    return {era: str(s[a:b].idxmin().date()) for era, (a, b) in windows.items()}


EQ_WIN = {"2000": ("2002-07-01", "2003-03-31"), "2008": ("2008-09-01", "2009-06-30"), "2015": ("2015-08-01", "2016-03-31"), "2021": ("2022-06-01", "2022-12-31")}
GD_WIN = {"2000": ("1999-01-01", "2001-12-31"), "2008": ("2008-09-01", "2009-06-30"), "2015": ("2015-08-01", "2016-03-31"), "2021": ("2022-06-01", "2022-12-31")}
NT, ST, GT = troughs(ndx, EQ_WIN), troughs(spx, EQ_WIN), troughs(gold, GD_WIN)
sub = f"每张图的横轴是各自的日历时间，从该周期底部到 {AS_OF}，点线为趋势线按公式再延长 3 年；纵轴为实际价格（对数）"
panels(ndx, NT, f"图 3 · 纳指100：四个周期底部各自起算的趋势线与公式（{sub}）", "03_ndx_four_panels.png", "纳指100")
panels(spx, ST, f"图 1b · 标普500：四个周期底部各自起算的趋势线与公式（{sub}）", "01b_spx_four_panels.png", "标普500")
panels(gold, GT, f"图 4b · 黄金：四个周期底部各自起算的趋势线与公式（{sub}）", "04b_gold_four_panels.png", "黄金", unit=" 美元")
def pairs(series, tr, label, fname, unit=""):
    for tag, eras in (("A", ("2000", "2008")), ("B", ("2015", "2021"))):
        sub_t = {e: tr[e] for e in eras}
        panels(series, sub_t, f"{label}：{eras[0]} 与 {eras[1]} 周期底部各自起算（横轴为各自日历时间，纵轴为实际价格，对数；点线为按公式延长 3 年）", f"{fname}_pair{tag}.png", label, unit=unit, figw=10)


pairs(ndx, NT, "纳指100", "03_ndx"); pairs(spx, ST, "标普500", "01b_spx"); pairs(gold, GT, "黄金", "04b_gold", unit=" 美元")
OUT["troughs"] = {"纳指100": NT, "标普500": ST, "黄金": GT}
json.dump(OUT, open(HERE/"panel_fits.json", "w", encoding="utf-8"), indent=2, ensure_ascii=False)
for lab in ("纳指100", "标普500", "黄金"):
    for era, r in OUT[lab].items():
        print(f"{lab} {era}: start {r['start']} P0 {r['p0']:,.0f}  P = {r['a']:,.0f} x {1+r['g']/100:.3f}^t  g={r['g']:.1f}%  dev {r['dev']:+.0f}% pct {r['pct']:.0f}  implied 3y {r['implied'][3]:,.0f} 5y {r['implied'][5]:,.0f}")
