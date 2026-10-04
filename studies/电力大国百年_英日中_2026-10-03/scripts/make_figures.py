#!/usr/bin/env python3
"""make_figures.py — 《电力大国百年：英 / 日 / 中》历史回顾的图（风格对齐 2026-09-16 电力报告与 2026-09-30 石油报告）。

配色：青绿 #008C7E（主角 / 好结果）· 焦橙 #C2410C（对照 / 冲击）· 石板灰 #5B6475（大盘等背景参照）
      电源结构用固定的燃料色（煤 = 深灰，油 = 暖灰，气 = 琥珀，核 = 紫灰，水 / 风 / 光 = 青绿），并直接标注，不靠图例猜颜色。
数据：data/ 下的 DUKES《Electricity since 1920》、OWID 能源数据、Yahoo 月线与分红（fetch_history.py），
      回报口径与 analyze_history.py 相同（close + 逐笔分红自建含息指数）。
用法: python studies/电力大国百年_英日中_2026-10-03/scripts/make_figures.py [uk|jp|cn|all]
"""
from __future__ import annotations

import csv
import datetime as dt
import json
import sys
import warnings
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.dates as mdates  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402
import openpyxl  # noqa: E402
from matplotlib.ticker import FuncFormatter  # noqa: E402

warnings.filterwarnings("ignore", category=UserWarning, module="openpyxl")

HERE = Path(__file__).resolve().parents[1]
DATA = HERE / "data"
sys.path.insert(0, str(Path(__file__).resolve().parent))
from analyze_history import M, annual_div, tr_series  # noqa: E402

TEAL, ORANGE, SLATE = "#008C7E", "#C2410C", "#5B6475"
TEAL_D, TEAL_L = "#005F56", "#5FB3AA"
INK, MUTED, GRID = "#1F2328", "#6B7280", "#E5E7EB"
FUEL = {"煤": "#4B5563", "油": "#A8A29E", "天然气": "#E0A43A", "核电": "#8B78B0", "水 / 风 / 光": "#008C7E",
        "其他": "#CBD5E1"}
SHOCK = "#F3E8DC"

plt.rcParams.update({
    "font.family": "Microsoft YaHei", "axes.unicode_minus": False, "figure.dpi": 150, "savefig.dpi": 150,
    "axes.spines.top": False, "axes.spines.right": False, "axes.edgecolor": "#9CA3AF",
    "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.8, "axes.axisbelow": True,
    "axes.titlesize": 13, "axes.titleweight": "regular", "axes.titlelocation": "left",
    "axes.labelcolor": MUTED, "xtick.color": MUTED, "ytick.color": MUTED, "font.size": 10,
    "legend.frameon": False, "lines.linewidth": 2.0, "text.parse_math": False,
})


def d(ym):
    return dt.date(int(ym[:4]), int(ym[5:7]), 15)


def note(fig, text):
    fig.text(0.01, 0.01, text, fontsize=8, color=MUTED, ha="left", va="bottom")


def save(fig, name):
    fig.savefig(HERE / name, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("->", name)


def rebase(s, start, level=1.0):
    ks = [k for k in s if k >= start]
    b = s[ks[0]]
    return {k: s[k] / b * level for k in ks}


def logfmt(ax):
    ax.set_yscale("log")
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:g}"))


def end_label(ax, s, text, color, dy=0):
    k = max(s)
    ax.annotate(text, (d(k), s[k]), xytext=(6, dy), textcoords="offset points", color=color, fontsize=9.5,
                va="center", fontweight="bold")


# ------------------------------------------------------------------ data
def uk_generation():
    wb = openpyxl.load_workbook(DATA / "uk_electricity_since_1920.xlsx", read_only=True, data_only=True)
    rows = list(wb["Estimated Historical Generation"].iter_rows(values_only=True))
    out = {}
    for r in rows[5:]:
        if not isinstance(r[0], int):
            continue
        v = [x if isinstance(x, (int, float)) else 0 for x in r[1:10]]
        out[r[0]] = {"煤": v[1] + v[6], "油": v[2], "天然气": v[3], "核电": v[4], "水 / 风 / 光": v[5],
                     "其他": v[7] + v[8], "total": v[0]}
    price = {}
    for r in list(wb["Electricity Prices"].iter_rows(values_only=True))[6:]:
        if isinstance(r[0], int) and isinstance(r[4], (int, float)):
            price[r[0]] = r[4]
    return out, price


def owid(country):
    rows = [r for r in csv.DictReader((DATA / "owid-energy-data.csv").open(encoding="utf-8")) if r["country"] == country]
    out = {}
    for r in rows:
        y = int(r["year"])

        def f(c):
            return float(r[c]) if r[c] else None
        out[y] = {"煤": f("coal_electricity"), "油": f("oil_electricity"), "天然气": f("gas_electricity"),
                  "核电": f("nuclear_electricity"),
                  "水 / 风 / 光": sum(x for x in (f("hydro_electricity"), f("wind_electricity"), f("solar_electricity")) if x),
                  "其他": sum(x for x in (f("biofuel_electricity"), f("other_renewable_exc_biofuel_electricity")) if x),
                  "total": f("electricity_generation"), "primary": f("primary_energy_consumption")}
    return out


# ------------------------------------------------------------------ UK
def fig_uk_generation():
    gen, price = uk_generation()
    ys = sorted(gen)
    fig, (ax, ax2) = plt.subplots(2, 1, figsize=(10, 7.4), height_ratios=[2.2, 1], sharex=True)
    keys = ["煤", "油", "天然气", "核电", "水 / 风 / 光", "其他"]
    ax.stackplot(ys, *[[gen[y][k] / 1000 for y in ys] for k in keys], colors=[FUEL[k] for k in keys], linewidth=0)
    for x0, x1 in ((1948, 1990),):
        ax.axvspan(x0, x1, color="#F1F5F9", zorder=0)
    ax.text(1969, 405, "国有化（1948–1990）", ha="center", color=MUTED, fontsize=9)
    peak = max(ys, key=lambda y: gen[y]["total"])
    ax.annotate(f"{peak} 年见顶 {gen[peak]['total']/1000:.0f} TWh", (peak, gen[peak]["total"] / 1000), xytext=(-150, 10),
                textcoords="offset points", fontsize=9.5, color=INK, arrowprops=dict(arrowstyle="-", color=MUTED))
    ax.annotate(f"2025 年 {gen[2025]['total']/1000:.0f} TWh\n≈ 1980 年代水平", (2025, gen[2025]["total"] / 1000),
                xytext=(-120, -55), textcoords="offset points", fontsize=9.5, color=INK,
                arrowprops=dict(arrowstyle="-", color=MUTED))
    for k, (x, yv) in {"煤": (1965, 70), "天然气": (2003, 200), "核电": (1990, 250), "水 / 风 / 光": (2019, 150)}.items():
        ax.text(x, yv, k, color="white" if k in ("煤", "核电", "水 / 风 / 光") else INK, fontsize=10, fontweight="bold",
                ha="center")
    ax.set_ylabel("发电量（TWh）")
    ax.set_ylim(0, 430)
    ax.set_title("英国发电量 1920–2025：涨了 90 年，然后掉了 20 年；煤从 99% 到 0")
    py = sorted(price)
    ax2.plot(py, [price[y] for y in py], color=ORANGE)
    ax2.axhline(100, color=GRID, lw=1)
    ax2.set_ylabel("实际电价指数\n（CPI 电力分项，2010=100）")
    ax2.annotate("私有化后十年\n实际电价 −47%", (2000, price[2000]), xytext=(-150, 18), textcoords="offset points",
                 fontsize=9, color=INK, arrowprops=dict(arrowstyle="-", color=MUTED))
    ax2.annotate(f"2023 能源危机 {price[2023]:.0f}", (2023, price[2023]), xytext=(-130, 0), textcoords="offset points",
                 fontsize=9, color=INK, arrowprops=dict(arrowstyle="-", color=MUTED))
    ax2.set_xlim(1920, 2027)
    note(fig, "来源：英国 DESNZ《DUKES: Electricity since 1920》（2026-07-30 版）'Estimated Historical Generation' 与 'Electricity Prices' 表；"
              "煤含焦炭，'其他' 含其他燃料与抽水蓄能。")
    fig.tight_layout(rect=(0, 0.03, 1, 1))
    save(fig, "fig1_uk_generation_price_1920_2025.png")


def fig_uk_shareholders():
    start = "1995-12"
    ng, sse = rebase(tr_series("NG.L"), start), rebase(tr_series("SSE.L"), start)
    idx = rebase({k: v["close"] for k, v in M["^FTAS"]["series"].items()}, start)
    etf = tr_series("ISF.L")
    etf = rebase(etf, "2009-01", idx[min(k for k in idx if k >= "2009-01")])
    fig, ax = plt.subplots(figsize=(10, 5.6))
    for x0, x1, lab in (("2008-09", "2009-03", "金融危机"), ("2021-09", "2023-03", "能源危机")):
        ax.axvspan(d(x0), d(x1), color=SHOCK, zorder=0)
        ax.text(d(x0), 40, lab, color=MUTED, fontsize=8.5)
    ax.plot([d(k) for k in idx], list(idx.values()), color=SLATE, lw=1.6)
    ax.plot([d(k) for k in etf], list(etf.values()), color=SLATE, lw=1.4, ls="--")
    ax.plot([d(k) for k in ng], list(ng.values()), color=TEAL)
    ax.plot([d(k) for k in sse], list(sse.values()), color=ORANGE)
    logfmt(ax)
    end_label(ax, sse, f"SSE ×{sse[max(sse)]:.1f}", ORANGE, 6)
    end_label(ax, ng, f"National Grid ×{ng[max(ng)]:.1f}", TEAL, -6)
    end_label(ax, idx, f"富时全股（价格）×{idx[max(idx)]:.1f}", SLATE, -4)
    end_label(ax, etf, "富时 100 含息（2009 起接续）", SLATE, 8)
    for ym, txt, yv in (("2002-10", "NG 并 Lattice", 6.0), ("2013-04", "RIIO 监管期", 16.0), ("2024-06", "NG 配股 £7bn", 1.05)):
        ax.axvline(d(ym), color=GRID, lw=1)
        ax.text(d(ym), yv, txt, rotation=90, color=MUTED, fontsize=8, va="bottom", ha="right")
    ax.set_ylabel("含息总回报（1995-12 = 1，对数）")
    ax.set_title("英国：用电量 2005 年见顶后一路下降，电网股的股东却继续赚钱")
    ax.set_xlim(d("1995-06"), d("2031-06"))
    note(fig, "来源：Yahoo 月线收盘 + 逐笔分红自建含息指数（未用 Yahoo adjclose，见 analyze_history.py）。富时全股为价格指数、不含息；"
              "按 3–3.5% 年股息粗估，其含息约 ×8–9 —— 两家电网股仍明显跑赢。")
    fig.tight_layout(rect=(0, 0.03, 1, 1))
    save(fig, "fig2_uk_shareholders_1995_2026.png")


# ------------------------------------------------------------------ Japan
def fig_jp_generation():
    o = owid("Japan")
    ys = [y for y in sorted(o) if y >= 1985 and o[y]["total"]]
    fig, (ax, ax2) = plt.subplots(1, 2, figsize=(11, 4.8), width_ratios=[2, 1])
    keys = ["煤", "油", "天然气", "核电", "水 / 风 / 光", "其他"]
    ax.stackplot(ys, *[[o[y][k] or 0 for y in ys] for k in keys], colors=[FUEL[k] for k in keys], linewidth=0)
    ax.axvline(2011, color=ORANGE, lw=1.4)
    ax.text(2011.3, 1140, "2011-03 福岛", color=ORANGE, fontsize=9)
    for k, (x, yv) in {"煤": (2000, 100), "天然气": (2003, 380), "油": (1990, 330), "核电": (1998, 720),
                      "水 / 风 / 光": (2020, 840)}.items():
        ax.text(x, yv, k, color="white" if k in ("煤", "核电", "水 / 风 / 光") else INK, fontsize=10,
                fontweight="bold", ha="center")
    ax.set_ylim(0, 1250)
    ax.set_ylabel("发电量（TWh）")
    ax.set_title("日本发电量 1985–2025：2008 年见顶，核电 2011 后归零又回来")
    py = [y for y in sorted(o) if o[y]["primary"]]
    ax2.plot(py, [o[y]["primary"] / 1000 for y in py], color=SLATE)
    ax2.set_title("一次能源消费（千 TWh）", fontsize=11)
    pk = max(py, key=lambda y: o[y]["primary"])
    ax2.annotate(f"{pk} 峰值", (pk, o[pk]["primary"] / 1000), xytext=(-60, -40), textcoords="offset points", fontsize=9,
                 arrowprops=dict(arrowstyle="-", color=MUTED))
    ax2.annotate("1965–1973\n高速增长期\n能源消费 ×2", (1969, o[1969]["primary"] / 1000), xytext=(10, -10),
                 textcoords="offset points", fontsize=8.5, color=INK)
    note(fig, "来源：Our World in Data 能源数据集（Ember / Energy Institute）；1985 年前的分电源发电量本批未取得，用一次能源消费代替。")
    fig.tight_layout(rect=(0, 0.04, 1, 1))
    save(fig, "fig3_jp_generation_1985_2025.png")


def fig_jp_shareholders():
    start = "2000-01"
    idx = rebase({k: v["close"] for k, v in M["^N225"]["series"].items()}, start)
    etf = rebase(tr_series("1321.T"), "2009-01", idx[min(k for k in idx if k >= "2009-01")])
    fig, ax = plt.subplots(figsize=(10, 5.8))
    ax.axvspan(d("2011-03"), d("2012-09"), color=SHOCK, zorder=0)
    ax.text(d("2011-04"), 0.062, "福岛冲击", color=MUTED, fontsize=8.5)
    ax.plot([d(k) for k in idx], list(idx.values()), color=SLATE, lw=1.6)
    ax.plot([d(k) for k in etf], list(etf.values()), color=SLATE, lw=1.4, ls="--")
    lines = {"9503.T": ("关西电力", TEAL), "9508.T": ("九州电力", TEAL_L), "9513.T": ("J-POWER", TEAL_D),
             "9501.T": ("东京电力", ORANGE)}
    ends = {}
    mult = {}
    for tk, (nm, c) in lines.items():
        s = tr_series(tk)
        first = max(min(s), start)
        mult[tk] = s[max(s)] / s[first]          # 自身起点以来的含息倍数（标签用）
        # 晚上市的（九州 2001-01、J-POWER 2004-10）在起点对齐到日经当时的位置，使与日经的视觉比较不失真
        s = rebase(s, first, 1.0 if first <= start else idx[min(k for k in idx if k >= first)])
        ax.plot([d(k) for k in s], list(s.values()), color=c, lw=2.0 if tk in ("9501.T", "9503.T") else 1.6)
        ends[tk] = s
    logfmt(ax)
    end_label(ax, idx, f"日经 225（价格）×{idx[max(idx)]:.1f}", SLATE, 10)
    end_label(ax, etf, "日经含息（2009 起接续）", SLATE, 22)
    end_label(ax, ends["9503.T"], f"关西 ×{mult['9503.T']:.2f}", TEAL, 4)
    end_label(ax, ends["9513.T"], f"J-POWER ×{mult['9513.T']:.2f}（2004 上市起；同期日经价格 ×6.3）", TEAL_D, -8)
    end_label(ax, ends["9508.T"], f"九州 ×{mult['9508.T']:.2f}（2001 起；同期日经价格 ×4.9）", TEAL_L, -14)
    end_label(ax, ends["9501.T"], f"东电 ×{mult['9501.T']:.2f}", ORANGE, 0)
    ax.set_ylabel("含息总回报（2000-01 = 1，对数）")
    ax.set_title("日本：26 年里没有一家电力公司跑赢日经，东电股东亏掉约四分之三")
    ax.set_xlim(d("1999-06"), d("2031-06"))
    note(fig, "来源：Yahoo 月线收盘 + 逐笔分红自建含息指数；晚上市的两家在起点对齐日经当时位置，标签倍数为各自起点以来。"
              "日经 225 为价格指数（不含息），2009 起虚线为日经 225 ETF（1321.T）含息。")
    fig.tight_layout(rect=(0, 0.03, 1, 1))
    save(fig, "fig4_jp_shareholders_2000_2026.png")


def fig_jp_dividends():
    tks = {"9501.T": "东京电力", "9503.T": "关西电力", "9508.T": "九州电力", "9513.T": "J-POWER"}
    fig, axs = plt.subplots(2, 2, figsize=(10, 5.6), sharex=True)
    for ax, (tk, nm) in zip(axs.flat, tks.items()):
        dv = annual_div(tk)
        ys = list(range(2000, 2027))
        vals = [dv.get(str(y), 0) for y in ys]
        first = min(int(k) for k in dv)
        zeros = [y for y, v in zip(ys, vals) if v == 0 and y >= first]
        for y in zeros:
            ax.axvspan(y - 0.5, y + 0.5, color=SHOCK, zorder=0)
        ax.bar(ys, vals, color=TEAL, width=0.75)
        ax.axvline(2011.2, color=ORANGE, lw=1)
        ax.set_title(f"{nm} · 零分红 {len(zeros)} 年" if zeros else f"{nm} · 上市以来未断", fontsize=11)
    for ax in axs[:, 0]:
        ax.set_ylabel("每股分红（日元，日历年）")
    fig.suptitle("日本四家：福岛之后的分红断档（浅橙底 = 当年分红为零；橙线 = 2011-03）", x=0.01, ha="left", fontsize=13)
    note(fig, "来源：Yahoo 分红记录（按除息日所在日历年加总，2026 年为截至 10 月）；J-POWER 2004 年 10 月上市。")
    fig.tight_layout(rect=(0, 0.04, 1, 0.95))
    save(fig, "fig5_jp_dividends_2000_2026.png")


# ------------------------------------------------------------------ China
def wb_coal():
    wb = openpyxl.load_workbook(DATA / "wb_cmo_monthly.xlsx", read_only=True, data_only=True)
    rows = list(wb["Monthly Prices"].iter_rows(values_only=True))
    j = [k for k, h in enumerate(rows[4]) if h == "Coal, Australian"][0]
    return {f"{r[0][:4]}-{r[0][5:7]}": r[j] for r in rows[6:] if r[0] and isinstance(r[j], (int, float))}


def fig_cn_generation():
    o = owid("China")
    ys = [y for y in sorted(o) if y >= 1985 and o[y]["total"]]
    fig, ax = plt.subplots(figsize=(10, 5.2))
    keys = ["煤", "油", "天然气", "核电", "水 / 风 / 光", "其他"]
    ax.stackplot(ys, *[[(o[y][k] or 0) / 1000 for y in ys] for k in keys], colors=[FUEL[k] for k in keys], linewidth=0)
    for k, (x, yv) in {"煤": (2012, 2.0), "水 / 风 / 光": (2021, 6.9)}.items():
        ax.text(x, yv, k, color="white", fontsize=10, fontweight="bold", ha="center")
    y24 = sum((o[2024][k] or 0) for k in ("煤", "油", "天然气")) / 1000 + (o[2024]["核电"] or 0) / 2000
    ax.annotate(f"核电（2025 年约 {o[2025]['核电'] / o[2025]['total']:.0%}）", (2024, y24), xytext=(-170, 25),
                textcoords="offset points", fontsize=9, color=INK, arrowprops=dict(arrowstyle="-", color=MUTED))
    ax.annotate(f"2000 年 {o[2000]['total']/1000:.2f} 千 TWh", (2000, o[2000]["total"] / 1000), xytext=(-20, 40),
                textcoords="offset points", fontsize=9.5, arrowprops=dict(arrowstyle="-", color=MUTED))
    ax.annotate(f"2025 年 {o[2025]['total']/1000:.1f} 千 TWh\n= 2000 年 ×{o[2025]['total']/o[2000]['total']:.1f}",
                (2025, o[2025]["total"] / 1000), xytext=(-150, 0), textcoords="offset points", fontsize=9.5,
                arrowprops=dict(arrowstyle="-", color=MUTED))
    ax.set_ylabel("发电量（千 TWh）")
    ax.set_title("中国发电量 1985–2025：25 年涨了 7.8 倍，煤电至今仍占一半以上")
    note(fig, "来源：Our World in Data 能源数据集（Ember / Energy Institute）。对照：英国 2025 年约 0.29 千 TWh，日本约 1.03 千 TWh。")
    fig.tight_layout(rect=(0, 0.03, 1, 1))
    save(fig, "fig6_cn_generation_1985_2025.png")


def fig_cn_shareholders():
    start = "2004-01"
    sh = rebase({k: v["close"] for k, v in M["000001.SS"]["series"].items()}, start)
    hsi = rebase({k: v["close"] for k, v in M["^HSI"]["series"].items()}, start)
    lines = {"600900.SS": ("长江电力（A，水电）", TEAL), "0836.HK": ("华润电力（H）", "#E0A43A"),
             "0902.HK": ("华能国际（H，煤电）", ORANGE), "1816.HK": ("中广核电力（H，核电）", "#8B78B0")}
    fig, (ax, ax2) = plt.subplots(2, 1, figsize=(10, 7.6), height_ratios=[2.3, 1], sharex=True)
    for x0, x1 in (("2016-01", "2018-10"), ("2021-01", "2022-10")):
        for a in (ax, ax2):
            a.axvspan(d(x0), d(x1), color=SHOCK, zorder=0)
    ax.set_ylim(0.6, 22)
    ax.text(d("2016-02"), 17, "煤价上行", color=MUTED, fontsize=8.5)
    ax.text(d("2021-02"), 17, "煤价暴涨", color=MUTED, fontsize=8.5)
    ax.plot([d(k) for k in sh], list(sh.values()), color=SLATE, lw=1.5)
    ax.plot([d(k) for k in hsi], list(hsi.values()), color=SLATE, lw=1.3, ls="--")
    mult = {}
    for tk, (nm, c) in lines.items():
        s = tr_series(tk)
        first = max(min(s), start)
        mult[tk] = s[max(s)] / s[first]
        lvl = 1.0 if first <= start else hsi[min(k for k in hsi if k >= first)]
        s = rebase(s, first, lvl)
        ax.plot([d(k) for k in s], list(s.values()), color=c, lw=2.0 if tk in ("600900.SS", "0902.HK") else 1.6)
        end_label(ax, s, f"{nm} ×{mult[tk]:.1f}" + ("（2014 上市起）" if tk == "1816.HK" else ""), c,
                  {"600900.SS": 0, "0836.HK": 4, "0902.HK": 12, "1816.HK": -12}[tk])
    end_label(ax, sh, f"上证综指（价格）×{sh[max(sh)]:.1f}", SLATE, 0)
    end_label(ax, hsi, f"恒生指数（价格）×{hsi[max(hsi)]:.1f}", SLATE, -6)
    logfmt(ax)
    ax.set_ylabel("含息总回报（2004-01 = 1，对数）")
    ax.set_title(f"中国：水电一路复利（×{mult['600900.SS']:.1f}），煤电股东的回报取决于起点和煤价")
    coal = {k: v for k, v in wb_coal().items() if k >= start}
    ax2.plot([d(k) for k in coal], list(coal.values()), color=ORANGE, lw=1.6)
    ax2.set_ylabel("澳大利亚动力煤\n（美元 / 吨）")
    pk = max(coal, key=coal.get)
    ax2.annotate(f"{pk} ${coal[pk]:.0f}", (d(pk), coal[pk]), xytext=(-110, -8), textcoords="offset points", fontsize=9,
                 arrowprops=dict(arrowstyle="-", color=MUTED))
    ax.set_xlim(d("2003-06"), d("2031-06"))
    note(fig, "来源：Yahoo 月线 + 逐笔分红自建含息指数（每条线 2004-01 = 1；中广核 2014-12 上市时对齐恒指位置，标签倍数为上市以来）；"
              "煤价：世界银行 Pink Sheet 月度（澳大利亚纽卡斯尔动力煤，国际基准，非中国国内价）。")
    fig.tight_layout(rect=(0, 0.03, 1, 1))
    save(fig, "fig7_cn_shareholders_coal_2004_2026.png")


# ------------------------------------------------------------------ summary
SUMMARY = [  # (国家, 名称, 股票, 含息代理, 模式)
    ("英国", "SSE", "SSE.L", "ISF.L", "net"), ("英国", "National Grid", "NG.L", "ISF.L", "net"),
    ("日本", "J-POWER", "9513.T", "1321.T", "mix"), ("日本", "关西电力", "9503.T", "1321.T", "mix"),
    ("日本", "九州电力", "9508.T", "1321.T", "mix"), ("日本", "东京电力", "9501.T", "1321.T", "acc"),
    ("中国", "长江电力（A）", "600900.SS", "510300.SS", "net"), ("中国", "华润电力（H）", "0836.HK", "2800.HK", "coal"),
    ("中国", "华能国际（H）", "0902.HK", "2800.HK", "coal"), ("中国", "华能国际（A）", "600011.SS", "510300.SS", "coal"),
    ("中国", "中广核电力（H）", "1816.HK", "2800.HK", "mix"),
]
MODE = {"net": (TEAL, "受监管电网 / 水电（稀缺资产、无燃料价差）"), "mix": (SLATE, "核电 / 综合发电"),
        "coal": ("#E0A43A", "煤电主导（受管控电价 − 市场煤价）"), "acc": (ORANGE, "核事故")}


def fig_summary():
    from analyze_history import ratio, cagr
    rows = []
    for ctry, nm, tk, ix, mode in SUMMARY:
        s, it = tr_series(tk), tr_series(ix)
        a = max(min(s), min(it))
        r, a2, b2 = ratio(s, a, "2026-10")
        ri, _, _ = ratio(it, a2, b2)
        rows.append((ctry, nm, cagr(r, a2, b2), cagr(ri, a2, b2), a2, mode))
    fig, ax = plt.subplots(figsize=(10, 6.4))
    ys = list(range(len(rows)))[::-1]
    for y, (ctry, nm, sc, ic, a2, mode) in zip(ys, rows):
        ax.barh(y, sc * 100, color=MODE[mode][0], height=0.62)
        ax.plot([ic * 100], [y], marker="|", markersize=16, mew=2.4, color=INK)
        if sc >= 0:
            x = (max(sc, ic) if abs(sc - ic) < 0.012 else sc) * 100 + 0.5   # 与指数竖线太近时放到竖线右侧
            ax.text(x, y, f"{sc:+.1%}", va="center", ha="left", fontsize=9, color=INK)
        else:
            ax.text(sc * 100 - 0.3, y, f"{sc:+.1%}", va="center", ha="right", fontsize=9, color=INK)
    ax.axvline(0, color="#9CA3AF", lw=1)
    ax.set_xlim(-11.5, 17)
    ax.set_yticks(ys)
    ax.set_yticklabels([f"{c} · {n}（{a[:4]} 起）" for c, n, _, _, a, _ in rows], fontsize=9.5, color=INK)
    ax.tick_params(axis="y", length=0)
    ax.grid(axis="y", visible=False)
    ax.set_xlabel("含息总回报年化（%）；黑色竖线 = 同期本国指数 ETF 含息年化")
    for i, (k, (c, lab)) in enumerate(MODE.items()):
        ax.text(1.0, 0.30 - i * 0.055, f"■ {lab}", color=c, transform=ax.transAxes, ha="right", fontsize=9)
    ax.set_title("三国电力股：股东回报由制度和资产决定，不由用电量决定")
    note(fig, "窗口 = 本国指数 ETF 含息数据起点（英 / 日 2009-01，港 2008-01，A 股 2012-05；中广核 H 2014-12）至 2026-10。"
              "发电量：英国 2005 年见顶后 −26%，日本 2008 年见顶后 −13%，中国 2000–2025 年 ×7.8。")
    fig.tight_layout(rect=(0, 0.03, 1, 1))
    save(fig, "fig8_summary_shareholder_returns.png")


# ------------------------------------------------------------------ history extras
def uk_real_price():
    """名义平均售电价（DUKES，便士/kWh）÷ 英格兰银行 CPI → 2016 年价格；2017–2025 用 DUKES 的 CPI 电力分项实际指数接续。"""
    boe = {int(r["year"]): r for r in csv.DictReader((DATA / "boe_uk_macro_1900_2016.csv").open(encoding="utf-8"))}
    wb = openpyxl.load_workbook(DATA / "uk_electricity_since_1920.xlsx", read_only=True, data_only=True)
    pr = {r[0]: (r[2], r[4]) for r in list(wb["Electricity Prices"].iter_rows(values_only=True))[6:] if isinstance(r[0], int)}
    real = {}
    for y, (nom, _) in pr.items():
        if isinstance(nom, (int, float)) and y in boe and boe[y]["cpi"]:
            real[y] = nom / float(boe[y]["cpi"]) * float(boe[2016]["cpi"])
    for y in range(2017, 2026):
        if isinstance(pr.get(y, (0, None))[1], (int, float)):
            real[y] = real[2016] * pr[y][1] / pr[2016][1]
    cust = {r[0]: r[2] for r in list(wb["Capacity"].iter_rows(values_only=True))[6:]
            if isinstance(r[0], int) and isinstance(r[2], (int, float))}
    load = {r[0]: r[10] / 1000 for r in list(wb["Capacity"].iter_rows(values_only=True))[6:]
            if isinstance(r[0], int) and isinstance(r[10], (int, float))}
    return dict(sorted(real.items())), dict(sorted(cust.items())), dict(sorted(load.items()))


def fig_uk_real_price():
    real, cust, load = uk_real_price()
    fig, (ax, ax2) = plt.subplots(2, 1, figsize=(10, 7.2), height_ratios=[1.6, 1], sharex=True)
    ys = sorted(real)
    ax.plot(ys, [real[y] for y in ys], color=ORANGE, marker="o", markersize=2.5, lw=1.8)
    ax.axvspan(1948, 1990, color="#F1F5F9", zorder=0)
    ax.text(1969, 31, "国有化（1948–1990）", ha="center", color=MUTED, fontsize=9)
    for y, txt, dx, dy in ((1921, "1921 年 {v:.1f}p", 10, 0), (1970, "1970 年 {v:.1f}p\n（比 1921 年 −77%）", -10, 55),
                           (2000, "2000 年 {v:.1f}p\n私有化后的历史最低", -150, -20), (2023, "2023 年 {v:.1f}p\n能源危机", -130, 10)):
        ax.annotate(txt.format(v=real[y]), (y, real[y]), xytext=(dx, dy), textcoords="offset points", fontsize=9,
                    color=INK, arrowprops=dict(arrowstyle="-", color=MUTED))
    ax.set_ylabel("实际平均电价\n（2016 年价格，便士 / kWh）")
    ax.set_ylim(0, 37)
    ax.set_title("英国百年实际电价：电气化让电便宜了 77%，私有化再降一截，此后去碳化与能源危机把它推到 3.5 倍")
    cy = sorted(cust)
    ax2.bar(cy, [cust[y] for y in cy], color=TEAL, width=0.8, label="用户数（百万户）")
    ax3 = ax2.twinx()
    ly = sorted(load)
    ax3.plot(ly, [load[y] for y in ly], color=SLATE, lw=1.6)
    ax3.set_ylabel("最大负荷（GW）", color=SLATE)
    ax3.spines["right"].set_visible(True)
    ax3.grid(False)
    ax2.set_ylabel("电力用户（百万户）", color=TEAL)
    ax2.text(1926, 17, "用户：1925 年 170 万 → 1980 年 2,030 万", color=TEAL, fontsize=9)
    pk = max(load, key=load.get)
    ax3.annotate(f"{pk} 年峰值 {load[pk]:.1f} GW", (pk, load[pk]), xytext=(-140, -6), textcoords="offset points",
                 fontsize=9, color=SLATE, arrowprops=dict(arrowstyle="-", color=MUTED))
    ax2.set_xlim(1918, 2027)
    note(fig, "来源：DUKES《Electricity since 1920》（平均售电价、用户数、同时最大负荷）；英格兰银行《A millennium of macroeconomic data》CPI；"
              "2017–2025 用 DUKES 的 CPI 电力分项实际指数接续。")
    fig.tight_layout(rect=(0, 0.03, 1, 1))
    save(fig, "fig1b_uk_real_price_customers_1921_2025.png")


def fig_decade_growth():
    wb = openpyxl.load_workbook(DATA / "uk_electricity_since_1920.xlsx", read_only=True, data_only=True)
    uk = {r[0]: r[1] for r in list(wb["Estimated Historical Generation"].iter_rows(values_only=True))[5:] if isinstance(r[0], int)}
    jp, cn = owid("Japan"), owid("China")

    def cg(d, a, b, key=None):
        x = d[a] if key is None else d[a][key]
        y = d[b] if key is None else d[b][key]
        return ((y / x) ** (1 / (b - a)) - 1) * 100

    panels = [
        ("英国（发电量，DUKES）", [(f"{a}s", cg(uk, a, min(a + 10, 2025)), "gen") for a in range(1920, 2030, 10)]),
        ("日本（1965–1985 用一次能源代替；1985 起发电量）",
         [("1965–73", cg(jp, 1965, 1973, "primary"), "pri"), ("1973–80", cg(jp, 1973, 1980, "primary"), "pri"),
          ("1980–85", cg(jp, 1980, 1985, "primary"), "pri"), ("1985–90", cg(jp, 1985, 1990, "total"), "gen"),
          ("1990s", cg(jp, 1990, 2000, "total"), "gen"), ("2000s", cg(jp, 2000, 2010, "total"), "gen"),
          ("2010s", cg(jp, 2010, 2020, "total"), "gen"), ("2020–25", cg(jp, 2020, 2025, "total"), "gen")]),
        ("中国（1965–1985 用一次能源代替；1985 起发电量）",
         [("1965–73", cg(cn, 1965, 1973, "primary"), "pri"), ("1973–80", cg(cn, 1973, 1980, "primary"), "pri"),
          ("1980–85", cg(cn, 1980, 1985, "primary"), "pri"), ("1985–90", cg(cn, 1985, 1990, "total"), "gen"),
          ("1990s", cg(cn, 1990, 2000, "total"), "gen"), ("2000s", cg(cn, 2000, 2010, "total"), "gen"),
          ("2010s", cg(cn, 2010, 2020, "total"), "gen"), ("2020–25", cg(cn, 2020, 2025, "total"), "gen")]),
    ]
    fig, axs = plt.subplots(3, 1, figsize=(10, 8.4), sharey=True)
    for ax, (title, bars) in zip(axs, panels):
        xs = range(len(bars))
        ax.bar(xs, [b[1] for b in bars], color=[TEAL if b[2] == "gen" else "#9FB7C9" for b in bars], width=0.7)
        for x, b in zip(xs, bars):
            ax.text(x, b[1] + (0.4 if b[1] >= 0 else -0.4), f"{b[1]:+.1f}%", ha="center",
                    va="bottom" if b[1] >= 0 else "top", fontsize=8.5, color=INK)
        ax.set_xticks(list(xs))
        ax.set_xticklabels([b[0] for b in bars], fontsize=9)
        ax.axhline(0, color="#9CA3AF", lw=1)
        ax.set_title(title, fontsize=11)
        ax.set_ylabel("年均增速（%）")
    axs[0].set_ylim(-4, 14.5)
    fig.suptitle("三国用电增速：英国的高增长在 1920–1960 年代，日本在 1960 年代，中国在 2000 年代 —— 之后都会放慢",
                 x=0.01, ha="left", fontsize=12.5)
    note(fig, "来源：英国 DUKES；日本、中国 Our World in Data（浅色柱 = 一次能源消费，深色柱 = 发电量）。")
    fig.tight_layout(rect=(0, 0.03, 1, 0.96))
    save(fig, "fig9_decade_growth_three_countries.png")


def main():
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    if which in ("uk", "all"):
        fig_uk_generation()
        fig_uk_shareholders()
    if which in ("jp", "all"):
        fig_jp_generation()
        fig_jp_shareholders()
        fig_jp_dividends()
    if which in ("cn", "all"):
        fig_cn_generation()
        fig_cn_shareholders()
    if which in ("summary", "all"):
        fig_summary()
    if which in ("hist", "all"):
        fig_uk_real_price()
        fig_decade_growth()


if __name__ == "__main__":
    main()
