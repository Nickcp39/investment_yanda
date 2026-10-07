#!/usr/bin/env python3
"""make_figures.py — 美股风气40年 全部图表（只读本地 data/，不联网）。"""
from __future__ import annotations

import csv
import datetime as dt
import gzip
import io
import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.dates as mdates  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.font_manager import FontProperties  # noqa: E402

BASE = Path(__file__).resolve().parents[1]
FIG = BASE
font = FontProperties(fname="C:/Windows/Fonts/msyh.ttc")
plt.rcParams.update({"font.family": font.get_name(), "axes.unicode_minus": False, "font.size": 9.5,
                     "axes.spines.top": False, "axes.spines.right": False, "savefig.dpi": 170})
INK, MUTED, GRID = "#1a1d24", "#6b7380", "#e3e7ee"
C = {"dead": "#b9484a", "acquired": "#d28a36", "survived_below_peak": "#8c929d",
     "survived_new_high": "#2f7d6d", "in_progress": "#4a78b0"}
FATE_CN = {"dead": "死亡（破产/清算/退市归零）", "acquired": "被收购", "survived_below_peak": "活着但没回到当年高点",
           "survived_new_high": "活着且曾收复当年高点", "in_progress": "进行中（2023 后主题）"}
VERDICT_C = {"真实且巨大": "#2f7d6d", "真实但比股价预期慢得多": "#d28a36", "真实但利润没留给当年的股东": "#8c698d",
             "基本是炒作": "#b9484a", "进行中": "#4a78b0"}


def load_px(tk):
    fn = BASE / "data/raw/prices" / (tk.replace("^", "IDX_") + ".csv.gz")
    rows = list(csv.DictReader(io.StringIO(gzip.decompress(fn.read_bytes()).decode())))
    return [(dt.date.fromisoformat(r["date"]), float(r["close"])) for r in rows]


def load_fred(sid):
    rows = list(csv.reader((BASE / f"data/raw/fred/{sid}.csv").read_text().splitlines()))[1:]
    return [(dt.date.fromisoformat(a), float(b)) for a, b in rows if b not in ("", ".")]


def title(ax, t, sub=None):
    ax.set_title(t, loc="left", fontweight="bold", fontsize=11.5, color=INK, pad=22 if sub else 8)
    if sub:
        ax.text(0, 1.015, sub, transform=ax.transAxes, fontsize=8.3, color=MUTED, va="bottom")


def fig_market(themes=None):
    nas = [x for x in load_px("^IXIC") if x[0] >= dt.date(1985, 1, 1)]
    ff = [x for x in load_fred("FEDFUNDS") if x[0] >= dt.date(1985, 1, 1)]
    dd = json.loads((BASE / "data/market_drawdowns.json").read_text(encoding="utf-8"))["^IXIC"]["drawdowns_ge20"]
    fig, (ax, ax2) = plt.subplots(2, 1, figsize=(10.5, 6.6), sharex=True, gridspec_kw={"height_ratios": [3, 1.15], "hspace": 0.08})
    ax.plot([d for d, _ in nas], [c for _, c in nas], color="#235e7c", lw=1.1)
    ax.set_yscale("log")
    for e in dd:
        p, r = dt.date.fromisoformat(e["peak"]), dt.date.fromisoformat(e["recovered"]) if e["recovered"] else nas[-1][0]
        ax.axvspan(p, r, color="#b9484a", alpha=0.08 if e["drawdown"] > -0.5 else 0.16, lw=0)
        if e["drawdown"] <= -0.3:
            yrs = e["years_peak_to_recover"]
            ax.annotate(f'{e["drawdown"]:.0%}\n收复 {yrs:.1f} 年' if yrs else f'{e["drawdown"]:.0%}',
                        xy=(p, e["peak_close"]), xytext=(0, 10), textcoords="offset points", fontsize=7.6,
                        color="#8a2f31", ha="center")
    if themes:
        for t in themes:
            pk = t.get("peak_date_parsed")
            if pk and t.get("label_on_market"):
                y = min(nas, key=lambda x: abs((x[0] - pk).days))[1]
                ax.plot([pk], [y], marker="v", color="#d28a36", ms=5)
                ax.annotate(t["short"], xy=(pk, y), xytext=(0, -14), textcoords="offset points", fontsize=7,
                            color="#7a4f16", ha="center", va="top")
    ax.set_ylabel("纳斯达克综合指数（对数）")
    ax.grid(alpha=0.25, color=GRID)
    title(ax, "图 1｜四十年纳指：每一轮风气的顶点都伴随一次深回撤",
          "红色区间 = 从前高回撤 ≥20% 到收复前高；日线价格指数，不含股息。来源：Yahoo Finance ^IXIC；FRED FEDFUNDS")
    ax2.plot([d for d, _ in ff], [v for _, v in ff], color="#8c698d", lw=1.2)
    ax2.fill_between([d for d, _ in ff], [v for _, v in ff], color="#8c698d", alpha=0.12)
    ax2.set_ylabel("联邦基金利率 %")
    ax2.grid(alpha=0.25, color=GRID)
    ax2.xaxis.set_major_locator(mdates.YearLocator(5))
    ax2.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    fig.savefig(FIG / "fig1_nasdaq_rates_1985_2026.png", bbox_inches="tight")
    plt.close(fig)


def fig_industry():
    d = json.loads((BASE / "data/industry_fads.json").read_text(encoding="utf-8"))
    from analyze_industry_market import CN
    rows = d["annual"]
    fig, ax = plt.subplots(figsize=(10.5, 5.0))
    xs = [r["year"] for r in rows if "hot5_fwd_rel" in r]
    ys = [(r["hot5_fwd_rel"] - 1) * 100 for r in rows if "hot5_fwd_rel" in r]
    full = [r["fwd_months"] == 60 for r in rows if "hot5_fwd_rel" in r]
    cols = [("#2f7d6d" if y >= 0 else "#b9484a") if f else "#c5cad3" for y, f in zip(ys, full)]
    ax.bar(xs, ys, color=cols, width=0.75)
    for x, y, r in zip(xs, ys, [r for r in rows if "hot5_fwd_rel" in r]):
        ax.text(x, y + (3 if y >= 0 else -3), CN[r["hot5"]], rotation=90, fontsize=6.8, ha="center",
                va="bottom" if y >= 0 else "top", color=INK)
    ax.axhline(0, color=INK, lw=0.8)
    s = d["a1_summary"]
    ax.set_ylabel("之后 5 年相对市场 %（行业财富/市场财富 − 1）")
    ax.set_ylim(-150, max(ys) + 60)
    ax.grid(axis="y", alpha=0.3, color=GRID)
    title(ax, "图 3｜每年年末“过去 5 年最热的行业”，之后 5 年怎样？",
          f"1985–2020 年共 {s['n']} 个起点：{s['hot_underperformed_next5y']} 次跑输市场，中位数相对 {(s['hot_median_fwd_rel']-1)*100:+.0f}%；"
          f"灰色 = 未满 5 年。来源：Kenneth French 49 行业（市值加权，月度，至 {d['end'][:4]}-{d['end'][4:]}）")
    fig.savefig(FIG / "fig3_hot_industry_next5y.png", bbox_inches="tight")
    plt.close(fig)

    ev = d["bubble_events"]
    fig, ax = plt.subplots(figsize=(10.5, 6.4))
    ev = sorted(ev, key=lambda e: e["peak"])
    for i, e in enumerate(ev):
        lab = f'{e["industry_cn"]} {e["peak"][:4]}-{e["peak"][4:]}'
        dd5 = e["maxdd"] * 100  # 本轮崩盘：顶点 → 收复前的最大回撤
        ax.barh(i, dd5, color="#b9484a" if dd5 <= -50 else ("#d28a36" if dd5 <= -30 else "#c5cad3"), height=0.65)
        later = e["maxdd_5y_after_peak"] * 100
        if later < dd5 - 10:  # 先创新高、5 年内又深跌
            ax.plot([later], [i], marker="D", mfc="white", mec="#b9484a", ms=4.5)
            ax.text(later - 1.5, i, f'{later:.0f}%', va="center", ha="right", fontsize=6.8, color="#8a2f31")
        if e["recovered"]:
            txt = f'{e["months_to_recover"] / 12:.1f} 年收复'
        elif e["months_after_peak_available"] < 24:
            txt = "顶点太近，未定"
        else:
            txt = f'至今未收复（{e["months_since_peak_unrecovered"] / 12:.0f} 年）'
        ax.text(1, i, f'  36 月涨 {e["abs36_max"]:.1f} 倍 · {txt}', va="center", fontsize=7.6, color=INK)
        if dd5 > -1:
            pass
        elif dd5 < -90:
            ax.text(dd5 + 2, i, f'{dd5:.0f}%', va="center", ha="left", fontsize=7.4, color="white", fontweight="bold")
        elif not later < dd5 - 10:
            ax.text(dd5 - 1, i, f'{dd5:.0f}%', va="center", ha="right", fontsize=7.4, color=INK)
        else:
            ax.text(dd5 + 1, i, f'{dd5:.0f}%', va="center", ha="left", fontsize=7.0, color=INK)
        ax.text(-101, i, lab, va="center", ha="right", fontsize=8, color=INK)
    ax.set_yticks([])
    ax.set_xlim(-100, 75)
    ax.invert_yaxis()
    ax.axvline(0, color=INK, lw=0.8)
    ax.set_xlabel("顶点后最大回撤，至收复前（月末总回报指数）；◇ = 先小幅创新高、5 年内又跌到的最低点")
    ax.spines["left"].set_visible(False)
    title(ax, "图 4｜行业暴涨时代：36 个月涨 ≥2.5 倍且跑赢市场 1 倍以上之后",
          f"{d['a2_summary']['n_events']} 个时代（1985–2026），规则见附录。来源：Kenneth French 49 行业，自行计算")
    fig.subplots_adjust(left=0.2)
    fig.savefig(FIG / "fig4_industry_booms.png", bbox_inches="tight")
    plt.close(fig)


def pd_(s):
    if not s:
        return None
    import re
    m = re.search(r"\d{4}(-\d{2}(-\d{2})?)?", str(s))
    if not m:
        return None
    s = m.group(0)
    try:
        if len(s) == 4:
            return dt.date(int(s), 7, 1)
        if len(s) == 7:
            return dt.date(int(s[:4]), int(s[5:7]), 15)
        return dt.date.fromisoformat(s)
    except ValueError:
        return None


def short_theme(n):
    """图中标签：过长的主题名截到第一个括号前。"""
    return n.split("（")[0].strip() if len(n) > 18 and "（" in n else n


def verdict_key(v):
    for k in VERDICT_C:
        if v and v.startswith(k[:4]):
            return k
    return v or "?"


def fig_timeline(T):
    th = [t for t in T["themes"] if pd_((t.get("hype_start") or {}).get("date")) and pd_((t.get("peak") or {}).get("date"))]
    th.sort(key=lambda t: pd_(t["hype_start"]["date"]))
    fig, ax = plt.subplots(figsize=(10.5, 0.27 * len(th) + 1.6))
    end = dt.date(2026, 10, 5)
    for i, t in enumerate(th):
        a, p = pd_(t["hype_start"]["date"]), pd_(t["peak"]["date"])
        z = pd_((t.get("trough") or {}).get("date"))
        col = VERDICT_C.get(verdict_key(t.get("reality_verdict")), "#8c929d")
        ax.plot([a, p], [i, i], color=col, lw=5.5, solid_capstyle="butt", alpha=0.9)
        if z and z > p:
            ax.plot([p, z], [i, i], color="#b9484a", lw=2.2, alpha=0.75)
            ax.plot([z], [i], marker="|", color="#b9484a", ms=7)
        elif verdict_key(t.get("reality_verdict")) == "进行中":
            ax.plot([p, end], [i, i], color=col, lw=1.2, ls=":", alpha=0.8)
        ax.text(a - dt.timedelta(days=60), i, short_theme(t["name_cn"]), ha="right", va="center", fontsize=7.8, color=INK)
    ax.set_yticks([])
    ax.invert_yaxis()
    ax.set_xlim(dt.date(1979, 1, 1), dt.date(2027, 6, 1))
    ax.xaxis.set_major_locator(mdates.YearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    ax.grid(axis="x", alpha=0.3, color=GRID)
    ax.spines["left"].set_visible(False)
    from matplotlib.lines import Line2D
    hs = [Line2D([0], [0], color=c, lw=5) for c in VERDICT_C.values()] + [Line2D([0], [0], color="#b9484a", lw=2)]
    ax.legend(hs, [f"兴起→顶点：{k}" for k in VERDICT_C] + ["顶点→谷底"], fontsize=7.2, loc="lower left", frameon=False, ncol=2)
    title(ax, "图 2｜四十年风气时间轴：粗线 = 从兴起到顶点（颜色 = 主题后来是否兑现），细红线 = 从顶点到谷底",
          "日期为研究员按当时事件标注（见各章来源）；“进行中”主题的虚线延伸到今天")
    fig.savefig(FIG / "fig2_theme_timeline.png", bbox_inches="tight")
    plt.close(fig)


def fig_fates(T):
    th = sorted(T["themes"], key=lambda t: pd_((t.get("hype_start") or {}).get("date")) or dt.date(2100, 1, 1))
    order = ["dead", "acquired", "survived_below_peak", "survived_new_high", "in_progress"]
    fig, ax = plt.subplots(figsize=(10.5, 0.27 * len(th) + 1.6))
    for i, t in enumerate(th):
        left = 0
        for f in order:
            n = t["fate_counts"].get(f, 0)
            if n:
                ax.barh(i, n, left=left, color=C[f], height=0.68)
                ax.text(left + n / 2, i, str(n), ha="center", va="center", fontsize=7, color="white")
                left += n
        ax.text(-0.3, i, short_theme(t["name_cn"]), ha="right", va="center", fontsize=7.8, color=INK)
    ax.set_yticks([])
    ax.invert_yaxis()
    ax.spines["left"].set_visible(False)
    ax.set_xlabel("当年明星股数量")
    from matplotlib.patches import Patch
    ax.legend([Patch(color=C[f]) for f in order], [FATE_CN[f] for f in order], fontsize=7.4, loc="lower right", frameon=False)
    a = T["aggregate"]
    title(ax, "图 5｜当年明星股的结局（按主题）",
          f"{a['n_companies']} 家公司：死亡 {a['dead']}、被收购 {a['acquired']}、活着未回高点 {a['survived_below_peak']}、"
          f"曾收复高点 {a['survived_new_high']}、进行中 {a['in_progress']}。有价格的按 Yahoo 重算，其余按研究来源")
    fig.savefig(FIG / "fig5_fates_by_theme.png", bbox_inches="tight")
    plt.close(fig)


def fig_durations(T):
    import statistics as stt
    th = [t for t in T["themes"] if not t["era_id"].startswith("e6")]  # 进行中主题不计用时
    cs = [c for c in T["companies"] if c.get("listed", True) and not c["era_id"].startswith("e6")]
    groups = [
        ("主题：兴起→顶点", [t["months_rise"] / 12 for t in th if t.get("months_rise")], "#d28a36"),
        ("主题：顶点→谷底", [t["months_bust"] / 12 for t in th if t.get("months_bust")], "#b9484a"),
        ("明星股：顶点→死亡", [c["months_peak_to_fate"] / 12 for c in cs if c["fate_computed"] == "dead" and c.get("months_peak_to_fate")], "#7a2e30"),
        ("明星股：顶点→被收购", [c["months_peak_to_fate"] / 12 for c in cs if c["fate_computed"] == "acquired" and c.get("months_peak_to_fate")], "#d28a36"),
        ("明星股：顶点→收复（已收复者）", [(c["price"] or {}).get("months_to_recover") / 12 for c in cs
                                     if c.get("price") and (c["price"] or {}).get("months_to_recover") and c["fate_computed"] != "in_progress"], "#2f7d6d"),
        ("明星股：顶点至今仍未收复", [(c["price"] or {}).get("years_since_peak") for c in cs
                                if c["fate_computed"] == "survived_below_peak" and (c.get("price") or {}).get("years_since_peak")], "#8c929d"),
    ]
    import random
    random.seed(7)
    fig, ax = plt.subplots(figsize=(10.5, 4.6))
    for i, (lab, xs, col) in enumerate(groups):
        ax.scatter(xs, [i + random.uniform(-0.18, 0.18) for _ in xs], s=13, color=col, alpha=0.65, lw=0)
        if xs:
            m = stt.median(xs)
            ax.plot([m, m], [i - 0.32, i + 0.32], color=INK, lw=1.6)
            ax.text(m, i - 0.36, f"中位 {m:.1f} 年（n={len(xs)}）", ha="center", va="bottom", fontsize=7.4, color=INK)
        ax.text(-0.6, i, lab, ha="right", va="center", fontsize=8.2, color=INK)
    ax.set_yticks([])
    ax.invert_yaxis()
    ax.set_xlim(0, 36)
    ax.set_xlabel("年")
    ax.grid(axis="x", alpha=0.3, color=GRID)
    ax.spines["left"].set_visible(False)
    title(ax, "图 6｜各阶段用了多久", "每个点是一个主题或一家公司；竖线为中位数")
    fig.subplots_adjust(left=0.25)
    fig.savefig(FIG / "fig6_durations.png", bbox_inches="tight")
    plt.close(fig)


def short_name(n):
    n = n.split("（")[0].split("(")[0].strip()
    return n[:16]


def fig_scatter(T):
    cs = [c for c in T["companies"] if c.get("listed", True) and c.get("price") and "maxdd" in (c["price"] or {})
          and not c["price"].get("conflict") and c["fate_computed"] in ("survived_new_high", "survived_below_peak")
          and not c["era_id"].startswith("e6")]
    seen, uniq = set(), []
    for c in sorted(cs, key=lambda c: c["price"]["peak_date"]):  # 同一家公司同一峰值只画一次
        k = (c.get("yahoo_ticker"), c["price"]["peak_date"][:7])
        if k not in seen:
            seen.add(k)
            uniq.append(c)
    rec = [c for c in uniq if c["price"].get("months_to_recover")]
    unr = [c for c in uniq if not c["price"].get("months_to_recover")]
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(11, 5.0), sharex=True, gridspec_kw={"wspace": 0.18})
    for c in rec:
        p = c["price"]
        y = p["months_to_recover"] / 12
        a1.scatter(p["maxdd"] * 100, y, s=22, color=C["survived_new_high"], alpha=0.8, lw=0)
        if y > 12:
            a1.annotate(short_name(c["name"]), (p["maxdd"] * 100, y), fontsize=6.6, color=MUTED, xytext=(3, 1), textcoords="offset points")
    for c in unr:
        p = c["price"]
        y = p["years_since_peak"]
        a2.scatter(p["maxdd"] * 100, y, s=22, color=C["survived_below_peak"], alpha=0.8, lw=0)
    for ax, yl, t in ((a1, "收复前高用了几年", f"已收复（{len(rec)} 家）"),
                      (a2, "顶点至今已等了几年（仍未收复）", f"仍未收复（{len(unr)} 家；等待 15 年以上的名单见正文表）")):
        ax.set_xlim(-101, 0)
        ax.set_ylim(0, 28)
        ax.set_ylabel(yl)
        ax.grid(alpha=0.3, color=GRID)
        ax.set_title(t, fontsize=9.5, loc="left", color=INK)
    fig.supxlabel("顶点后最大回撤 %（拆股复权日收盘）", fontsize=9)
    fig.suptitle("图 7｜跌得越深，回来越难：活下来的当年明星股", x=0.06, ha="left", fontweight="bold", fontsize=11.5, y=1.02)
    fig.text(0.06, 0.955, "只含已结束的时代（2023 年后主题除外）；同一公司同一峰值只计一次；死亡与被收购的公司不在图中",
             fontsize=8.3, color=MUTED)
    fig.savefig(FIG / "fig7_drawdown_vs_recovery.png", bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    import sys
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    fig_industry()
    tp = BASE / "data/themes_computed.json"
    T = json.loads(tp.read_text(encoding="utf-8")) if tp.exists() else None
    marks = []
    if T:
        for t in T["themes"]:
            if t.get("market_label"):
                marks.append({"peak_date_parsed": pd_((t.get("peak") or {}).get("date")), "short": t["market_label"], "label_on_market": True})
        fig_timeline(T)
        fig_fates(T)
        fig_durations(T)
        fig_scatter(T)
    fig_market(marks)
    print("ok")
