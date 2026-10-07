#!/usr/bin/env python3
"""make_figures.py — 生命周期时间轴、分阶段股价小图、回撤与回本年数。

阶段划分（开始 / 爬升 / 顶点 / 衰落·沉默 / 转身·复苏 / 未定）是本研究按舆论与经营事实做的判断，
依据见 report.md 各公司表格；股价全部来自 data/prices_monthly.json（Yahoo 月末收盘，仅拆股调整）。
"""
from __future__ import annotations

import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Patch  # noqa: E402
from matplotlib.ticker import FuncFormatter, LogLocator, NullFormatter  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
P = json.loads((ROOT / "data" / "prices_monthly.json").read_text(encoding="utf-8"))

plt.rcParams.update({
    "font.sans-serif": ["Microsoft YaHei", "SimHei"], "axes.unicode_minus": False, "text.parse_math": False,
    "font.size": 9, "axes.spines.top": False, "axes.spines.right": False,
})
TEAL, ORANGE, SLATE, SHOCK = "#008C7E", "#C2410C", "#5B6475", "#F3E8DC"
PH = {  # 阶段 -> (颜色, 图例名, 填充纹理)
    "S": ("#A9B4C2", "开始", None),
    "C": (TEAL, "爬升", None),
    "P": (ORANGE, "顶点", None),
    "D": ("#C9CDD4", "衰落 / 沉默", None),
    "R": ("#8CCFC6", "转身 / 复苏", "//"),
    "U": ("#F2B48F", "未定（今天）", "xx"),
}
NOW = 2026.8

# 名称, 段列表 [(起, 止, 阶段)]
ROWS = [
    ("阿克莱特 · 水力纺纱机（英）", [(1764, 1771, "S"), (1771, 1781, "C"), (1781, 1785, "P"), (1785, 1792, "D")]),
    ("Boulton & Watt · 蒸汽机（英）", [(1769, 1776, "S"), (1776, 1790, "C"), (1790, 1800, "P"), (1800, 1895, "D")]),
    ("Platt Brothers · 纺织机械（英）", [(1821, 1844, "S"), (1844, 1890, "C"), (1890, 1926, "P"), (1927, 1982, "D")]),
    ("Robert Stephenson & Co · 机车（英）", [(1823, 1829, "S"), (1829, 1844, "C"), (1844, 1847, "P"), (1847, 1937, "D")]),
    ("Krupp · 无缝轮箍 / 钢（德）", [(1826, 1851, "S"), (1851, 1871, "C"), (1871, 1918, "P"), (1918, 1967, "D")]),
    ("Baldwin · 蒸汽机车（美）", [(1831, 1835, "S"), (1835, 1900, "C"), (1900, 1923, "P"), (1924, 1956, "D")]),
    ("西门子 · 电报 / 电气（德）", [(1847, 1866, "S"), (1866, 1914, "C"), (1998, 2000.2, "P"), (2000.2, 2008.9, "D"),
                                  (2008.9, NOW, "R")]),
    ("Harland & Wolff · 造船（英）", [(1861, 1870, "S"), (1870, 1900, "C"), (1900, 1918, "P"), (1956, 2024.7, "D")]),
    ("通用电气 GE · 电气（美）", [(1878, 1892, "S"), (1892, 1925, "C"), (1925, 1929.8, "P"), (1929.8, 1945, "D"),
                                (1981, 1998, "C"), (1998, 2000.7, "P"), (2000.7, 2024.3, "D")]),
    ("Marconi · 无线电（英）", [(1896, 1901, "S"), (1901, 1912, "C"), (1912, 1913.5, "P"), (1913.5, 1929, "D"),
                              (1999, 2000.7, "P"), (2000.7, 2006, "D")]),
    ("RCA · 无线电（美）", [(1919, 1922, "S"), (1922, 1928, "C"), (1928, 1929.8, "P"), (1929.8, 1937, "D")]),
    ("丰田自动织机 · 织机（日）", [(1924, 1926, "S"), (1926, 1929, "C"), (1929, 1937, "P"), (1937, 2026.4, "R")]),
    ("IBM · 大型机（美）", [(1914, 1952, "S"), (1952, 1964, "C"), (1964, 1987.6, "P"), (1987.6, 1993.7, "D"),
                           (1993.7, NOW, "R")]),
    ("三菱重工 · 造船（日）", [(1884, 1950, "S"), (1950, 1965, "C"), (1965, 1974, "P"), (1974, 2020.8, "D"),
                             (2020.8, NOW, "R")]),
    ("Intel · PC 芯片（美）", [(1968, 1981, "S"), (1981, 1996, "C"), (1996, 2000.7, "P"), (2000.7, 2025.1, "D"),
                              (2025.1, NOW, "R")]),
    ("NEC · 半导体（日）", [(1970, 1977, "S"), (1977, 1985, "C"), (1985, 1992, "P"), (1992, 2012.6, "D")]),
    ("思科 · 路由器（美，参照）", [(1984, 1990, "S"), (1990, 1999, "C"), (1999, 2000.25, "P"), (2000.25, 2025.95, "D")]),
    ("爱立信 · 移动通信（瑞典）", [(1981, 1991, "S"), (1991, 1998, "C"), (1998, 2000.2, "P"), (2000.2, NOW, "D")]),
    ("英伟达 · GPU（美，参照）", [(1993, 2006, "S"), (2006, 2023, "C"), (2023, NOW, "U")]),
    ("无锡尚德 · 光伏（中）", [(2001, 2005.9, "S"), (2005.9, 2007, "C"), (2007, 2008.6, "P"), (2008.6, 2013.3, "D")]),
    ("中国船舶 · 造船（中）", [(1998, 2006, "S"), (2006, 2007.5, "C"), (2007.5, 2007.8, "P"), (2007.8, NOW, "D")]),
    ("中国南车 / 中车 · 高铁（中）", [(2004, 2008.6, "S"), (2008.6, 2014.9, "C"), (2014.9, 2015.5, "P"),
                                   (2015.5, NOW, "D")]),
]


def first_peak(segs):
    ps = [a for a, b, k in segs if k in ("P", "U")]
    return ps[0] if ps else 9999


ROWS.sort(key=lambda r: first_peak(r[1]))


def legend(ax, keys="SCPDRU", **kw):
    hs = [Patch(facecolor=PH[k][0], hatch=PH[k][2], edgecolor="white", label=PH[k][1]) for k in keys]
    ax.legend(handles=hs, frameon=False, **kw)


def fig_timeline():
    fig, ax = plt.subplots(figsize=(11, 7.6))
    n = len(ROWS)
    for i, (name, segs) in enumerate(ROWS):
        y = n - 1 - i
        x0, x1 = segs[0][0], segs[-1][1]
        ax.plot([x0, x1], [y, y], color="#E3E6EA", lw=1, zorder=1)
        for a, b, k in segs:
            c, _, h = PH[k]
            ax.barh(y, max(b - a, 0.8), left=a, height=0.62, color=c, hatch=h, edgecolor="white", lw=0.3, zorder=2)
        ax.text(1758, y, name, ha="right", va="center", fontsize=8.6)
    for x, lab, ha in [(1776, "1776 瓦特机", "center"), (1846, "1846 铁路狂热", "center"), (1929, "1929", "center"),
                       (2000, "2000 ", "right"), (2007.8, "2007", "center"), (2015.4, " 2015", "left")]:
        ax.axvline(x, color=ORANGE, lw=0.6, ls=":", zorder=0)
        ax.text(x, n - 0.2 + (0.45 if lab.strip() == "2007" else 0), lab, color=ORANGE, fontsize=7.5, ha=ha,
                va="bottom")
    ax.set_xlim(1758, 2030)
    ax.set_ylim(-0.7, n + 0.8)
    ax.set_yticks([])
    ax.spines["left"].set_visible(False)
    ax.set_xticks(range(1760, 2031, 20))
    ax.set_title("图 1  22 家\"卖铲子的人\"的生命周期：开始 → 爬升 → 顶点 → 衰落 / 沉默（1764–2026）", loc="left",
                 fontsize=11)
    legend(ax, loc="lower left", ncol=6, fontsize=8.5, bbox_to_anchor=(0.0, -0.11))
    fig.text(0.01, 0.005, "注：阶段边界按本报告各公司表格中的舆论与经营事实划定；按第一次顶点的年份从上到下排列。"
             "西门子、GE、Marconi 有两轮周期；细灰线 = 未做阶段划分的中间年代。", fontsize=7.5, color=SLATE)
    fig.subplots_adjust(left=0.25, right=0.985, top=0.95, bottom=0.1)
    fig.savefig(ROOT / "fig1_lifecycle_timeline.png", dpi=170)
    plt.close(fig)


def series(tk, end=None):
    s = P[tk]["series"]
    ks = [k for k in sorted(s) if end is None or k <= end]
    return [int(k[:4]) + (int(k[5:]) - 0.5) / 12 for k in ks], [s[k]["close"] for k in ks], ks


ANN = {  # 标注的（顶点月, 其后最低点月）
    "CSCO": [("2000-03", "2002-09")], "INTC": [("2000-08", "2009-02")],
    "NVDA": [("2007-09", "2008-11"), ("2021-11", "2022-09")], "IBM": [("1987-08", "1993-09")],
    "GE": [("2000-08", "2020-07")], "ERIC": [("2000-02", "2002-09")], "SIE.DE": [("2000-02", "2002-09")],
    "6701.T": [("2000-06", "2012-07")], "7011.T": [("2007-07", "2020-10")], "600150.SS": [("2007-09", "2018-06")],
    "601766.SS": [("2015-04", "2022-09")], "^IXIC": [("2000-02", "2002-09")],
}

PANELS = [  # ticker, 标题, 阴影段, 截止月
    ("CSCO", "思科（参照）", [(1990, 1999, "C"), (1999, 2000.25, "P"), (2000.25, 2025.95, "D")], None),
    ("INTC", "英特尔", [(1985, 1996, "C"), (1996, 2000.7, "P"), (2000.7, 2025.1, "D"), (2025.1, NOW, "R")], None),
    ("NVDA", "英伟达（参照）", [(1999, 2006, "S"), (2006, 2023, "C"), (2023, NOW, "U")], None),
    ("IBM", "IBM", [(1970, 1987.6, "P"), (1987.6, 1993.7, "D"), (1993.7, NOW, "R")], None),
    ("GE", "通用电气（至 2023 年底）", [(1981, 1998, "C"), (1998, 2000.7, "P"), (2000.7, 2023.99, "D")], "2023-12"),
    ("ERIC", "爱立信（ADR）", [(1991, 1998, "C"), (1998, 2000.2, "P"), (2000.2, NOW, "D")], None),
    ("SIE.DE", "西门子", [(1998, 2000.2, "P"), (2000.2, 2008.9, "D"), (2008.9, NOW, "R")], None),
    ("6701.T", "NEC（数据 2000 起）", [(2000, 2012.6, "D")], None),
    ("7011.T", "三菱重工（数据 2000 起）", [(2000, 2020.8, "D"), (2020.8, NOW, "R")], None),
    ("600150.SS", "中国船舶（复权）", [(2006, 2007.5, "C"), (2007.5, 2007.8, "P"), (2007.8, NOW, "D")], None),
    ("601766.SS", "中国南车 / 中车", [(2008.6, 2014.9, "C"), (2014.9, 2015.5, "P"), (2015.5, NOW, "D")], None),
    ("^IXIC", "纳斯达克综指（背景）", [(1995, 1999, "C"), (1999, 2000.2, "P"), (2000.2, 2015, "D")], None),
]


def fig_prices():
    fig, axs = plt.subplots(4, 3, figsize=(11, 12))
    for ax, (tk, title, segs, end) in zip(axs.flat, PANELS):
        x, y, ks = series(tk, end)
        for a, b, k in segs:
            ax.axvspan(max(a, x[0]), b, color=PH[k][0], alpha=0.35, hatch=PH[k][2], lw=0)
        ax.plot(x, y, color="#1F2933", lw=0.9)
        ax.set_yscale("log")
        idx = {k: n for n, k in enumerate(ks)}
        for pk, tr in ANN[tk]:
            i, j = idx[pk], idx[tr]
            ax.annotate(pk, (x[i], y[i]), fontsize=7, color=ORANGE, xytext=(3, 2), textcoords="offset points")
            ax.annotate(f"{tr} {y[j] / y[i] - 1:+.0%}", (x[j], y[j]), fontsize=7, color=SLATE, xytext=(3, -9),
                        textcoords="offset points")
        ax.yaxis.set_major_locator(LogLocator(base=10, subs=(1.0, 3.0)))
        ax.yaxis.set_minor_formatter(NullFormatter())
        ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:g}"))
        ax.set_title(f"{title}  {tk}", loc="left", fontsize=9)
        ax.tick_params(labelsize=7)
        ax.set_xlim(x[0], 2027)
        ax.set_ylim(min(y) * 0.6, max(y) * 1.5)
        ax.xaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:.0f}"))
    legend(fig, loc="lower center", fontsize=8.5, ncol=6, bbox_to_anchor=(0.5, 0.012))
    fig.suptitle("图 2  有月线数据的 11 家公司 + 纳指：股价（对数轴）与舆论阶段", x=0.01, ha="left", fontsize=11)
    fig.text(0.01, 0.005, "数据：Yahoo 月末收盘（仅拆股调整；A 股为复权价，中国船舶 2007 年名义高点约 300 元）。"
             "橙字 = 顶点月份；灰字 = 其后最低点的月份与跌幅。",
             fontsize=7.5, color=SLATE)
    fig.tight_layout(rect=(0, 0.04, 1, 0.97))
    fig.savefig(ROOT / "fig2_prices_by_phase.png", dpi=160)
    plt.close(fig)


def recover(tk, peak):
    s = P[tk]["series"]
    ks = sorted(s)
    p = s[peak]["close"]
    after = [k for k in ks if k > peak]
    trough = min(after, key=lambda k: s[k]["close"])
    rec = next((k for k in after if s[k]["close"] >= p), None)
    yrs = None if rec is None else (int(rec[:4]) - int(peak[:4])) + (int(rec[5:]) - int(peak[5:])) / 12
    now = s[ks[-1]]["close"] / p - 1
    return s[trough]["close"] / p - 1, trough, rec, yrs, now


def fig_recovery():
    rows = []
    for tk, name, peak in [("CSCO", "思科", "2000-03"), ("INTC", "英特尔", "2000-08"), ("IBM", "IBM", "1987-08"),
                           ("SIE.DE", "西门子", "2000-02"), ("7011.T", "三菱重工", "2007-07"),
                           ("NVDA", "英伟达 ①", "2007-09"), ("NVDA", "英伟达 ②", "2021-11"),
                           ("ERIC", "爱立信", "2000-02"), ("6701.T", "NEC", "2000-06"),
                           ("600150.SS", "中国船舶", "2007-09"), ("601766.SS", "中国南车/中车", "2015-04"),
                           ("GE", "通用电气", "2000-08")]:
        dd, tr, rec, yrs, now = recover(tk, peak)
        if tk == "GE":  # 2024 拆分后不可比：只看拆分前的最低点
            s = P["GE"]["series"]
            ks = [k for k in sorted(s) if peak < k <= "2023-12"]
            tr = min(ks, key=lambda k: s[k]["close"])
            dd, rec, yrs, now = s[tr]["close"] / s[peak]["close"] - 1, None, None, None
        rows.append((name, peak, dd, tr, rec, yrs, now, "data"))
    lit = [("RCA", "1929-09", -0.98, "1932", None, None, None, "lit"),
           ("Marconi plc", "2000", -0.986, "2002", None, None, None, "lit"),
           ("英国铁路股（平均）", "1845–46", -0.85, "1850", None, None, None, "lit")]
    rows += lit
    (ROOT / "data" / "recovery_stats.json").write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(11, 6.2), gridspec_kw={"width_ratios": [1, 1.25]})
    n = len(rows)
    for i, (name, peak, dd, tr, rec, yrs, now, src) in enumerate(rows):
        y = n - 1 - i
        a1.barh(y, -dd * 100, color=SLATE if src == "data" else "#A9B4C2", hatch=None if src == "data" else "..",
                edgecolor="white")
        a1.text(-dd * 100 + 1, y, f"{dd * 100:.1f}%", va="center", fontsize=8)
        if yrs is not None:
            a2.barh(y, yrs, color=TEAL)
            a2.text(yrs + 0.3, y, f"{yrs:.1f} 年（{rec}）", va="center", fontsize=8)
        elif src == "data" and now is not None:
            span = NOW - (int(peak[:4]) + int(peak[5:7]) / 12)
            a2.barh(y, span, color="#F2B48F", hatch="//", edgecolor="white")
            a2.text(span + 0.3, y, f"未收复：今天仍 {now:+.0%}", va="center", fontsize=8, color=ORANGE)
        elif name == "通用电气":
            a2.text(0.3, y, "2024 年拆成三家，回本口径不可比", va="center", fontsize=8, color=SLATE)
        else:
            a2.text(0.3, y, {"RCA": "1937 年才首次给普通股派息", "Marconi plc": "2003 年债转股，原股东只剩 0.5%",
                             "英国铁路股（平均）": "Hudson 1849 年身败名裂"}[name], va="center", fontsize=8,
                    color=SLATE)
    for a in (a1, a2):
        a.set_ylim(-0.6, n - 0.4)
    a1.set_yticks([n - 1 - i for i in range(n)])
    a1.set_yticklabels([f"{r[0]}（{r[1]}）" for r in rows], fontsize=8.5)
    a2.set_yticks([])
    a1.set_xlim(0, 115)
    a1.set_xlabel("顶点到最低点的跌幅（%，月末收盘）")
    a2.set_xlabel("回到顶点所用年数")
    a2.set_xlim(0, 38)
    a1.set_title("图 3  顶点之后：跌多少、多久回本", loc="left", fontsize=11, x=-0.45)
    fig.text(0.01, 0.01, "实心 = 本目录 Yahoo 月线计算；点状 = 文献数字（RCA：Finaeon；Marconi：CNN / The Register；"
             "铁路股：Railway Mania 词条）。三菱重工以 2007 年为顶（造船时代的 1970 年代无数据）。", fontsize=7.5,
             color=SLATE)
    fig.subplots_adjust(left=0.19, right=0.98, wspace=0.12, top=0.93, bottom=0.12)
    fig.savefig(ROOT / "fig3_drawdown_recovery.png", dpi=170)
    plt.close(fig)
    for r in rows:
        print(r)


if __name__ == "__main__":
    fig_timeline()
    fig_prices()
    fig_recovery()
