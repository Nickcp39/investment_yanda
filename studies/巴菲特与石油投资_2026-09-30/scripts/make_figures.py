#!/usr/bin/env python3
"""make_figures.py — 《巴菲特与石油投资》报告的 7 张历史图（风格对齐 2026-09-16 电力报告）。

配色（经 dataviz validate_palette.js 校验，light 模式全部 PASS）：
  青绿 #008C7E（主体 / 买入）· 焦橙 #C2410C（对照 / 卖出 / 现在）· 石板灰 #5B6475（大盘等背景参照，非分类色）
数据全部来自本目录 data/ 与仓库已有文件；SPY/CVX/OXY 月线从 Yahoo 拉取并缓存。
用法: python studies/巴菲特与石油投资_2026-09-30/scripts/make_figures.py
"""
from __future__ import annotations

import csv
import datetime as dt
import json
import urllib.request
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.dates as mdates  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.ticker import FuncFormatter, LogLocator, NullFormatter  # noqa: E402

HERE = Path(__file__).resolve().parents[1]
DATA = HERE / "data"
REPO = HERE.parents[1]
FFDIR = HERE.parent / "电力需求与电力公司盈利_百年实证_2026-09-16" / "data"

TEAL, ORANGE, SLATE = "#008C7E", "#C2410C", "#5B6475"
INK, MUTED, GRID = "#1F2328", "#6B7280", "#E5E7EB"
SPIKE, GLUT = "#F3E8DC", "#E6EEF3"   # 冲击期 / 供给放开期的底色

plt.rcParams.update({
    "font.family": "Microsoft YaHei", "axes.unicode_minus": False, "figure.dpi": 150, "savefig.dpi": 150,
    "axes.spines.top": False, "axes.spines.right": False, "axes.edgecolor": "#9CA3AF",
    "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.8, "axes.axisbelow": True,
    "axes.titlesize": 13, "axes.titleweight": "regular", "axes.titlelocation": "left",
    "axes.labelcolor": MUTED, "xtick.color": MUTED, "ytick.color": MUTED, "font.size": 10,
    "legend.frameon": False, "lines.linewidth": 2.0,
    "text.parse_math": False,   # 文本里的 $ 是美元符号，不是公式
})


def d(ym):
    return dt.date(int(ym[:4]), int(ym[5:7]), 15)


def ym_add(ym, n):
    t = int(ym[:4]) * 12 + int(ym[5:7]) - 1 + n
    return f"{t // 12}-{t % 12 + 1:02d}"


# ------------------------------------------------------------------ data loaders
def oil_monthly():
    """1949–1973 年度首购价（放在每年 7 月），1974–1985 月度首购价，1986 起 WTI 现货。"""
    annual, monthly = {}, {}
    with (DATA / "eia_mer_T09.01.csv").open(encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r["MSN"] != "CODPUUS" or r["Value"] in ("", "Not Available"):
                continue
            ym = r["YYYYMM"]
            if ym.endswith("13"):
                annual[ym[:4]] = float(r["Value"])
            else:
                monthly[f"{ym[:4]}-{ym[4:]}"] = float(r["Value"])
    wti = json.loads((DATA / "eia_monthly_spot.json").read_text(encoding="utf-8"))["WTI_spot"]
    out = {f"{y}-07": v for y, v in annual.items() if int(y) <= 1973}
    out.update({k: v for k, v in monthly.items() if k < "1986-01"})
    out.update(wti)
    return dict(sorted(out.items()))


def ff():
    def section(path, key):
        raw = path.read_bytes().decode("utf-8", errors="replace")
        lines = raw.replace("\r\r\n", "\n").replace("\r\n", "\n").split("\n")
        start = next(i for i, l in enumerate(lines) if key in l)
        hdr, data = None, {}
        for l in lines[start + 1:]:
            if l.startswith(","):
                hdr = [h.strip() for h in l.split(",")]
                continue
            if hdr and not l.strip() and data:
                break
            p = [x.strip() for x in l.split(",")]
            if hdr and len(p) == len(hdr) and len(p[0]) == 6 and p[0].isdigit():
                data[f"{p[0][:4]}-{p[0][4:]}"] = dict(zip(hdr[1:], map(float, p[1:])))
        return data
    ind = section(FFDIR / "ff12.csv", "Average Value Weighted Returns -- Monthly")
    fac = section(FFDIR / "ff_factors.csv", "")
    months = sorted(set(ind) & set(fac))
    return {m: (ind[m]["Enrgy"] / 100, (fac[m]["Mkt-RF"] + fac[m]["RF"]) / 100) for m in months}


def yahoo_monthly(tickers, start="2022-03-01"):
    cache = DATA / "yahoo_monthend_2022.json"   # 由日线取每月最后一个交易日（截至 2026-09-29），避免月线末根陈旧
    if cache.exists():
        return json.loads(cache.read_text(encoding="utf-8"))
    out = {}
    p1 = int(dt.datetime.fromisoformat(start).timestamp())
    p2 = int(dt.datetime(2026, 9, 30).timestamp())
    for tk in tickers:
        url = (f"https://query1.finance.yahoo.com/v8/finance/chart/{tk}?period1={p1}&period2={p2}"
               f"&interval=1d&events=div")
        j = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})))
        r = j["chart"]["result"][0]
        adj = r["indicators"]["adjclose"][0]["adjclose"]
        me = {}
        for t, a in zip(r["timestamp"], adj):
            day = dt.datetime.utcfromtimestamp(t).date()
            if a and day <= dt.date(2026, 9, 29):
                me[day.strftime("%Y-%m")] = a   # 按时间顺序覆盖 → 留下每月最后一个交易日
        out[tk] = me
    cache.write_text(json.dumps(out), encoding="utf-8")
    return out


def finish(fig, name, note=None):
    if note:
        fig.text(0.01, -0.01, note, fontsize=8, color=MUTED, ha="left", va="top")
    out = HERE / name
    fig.savefig(out, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("wrote", out.name)


# ------------------------------------------------------------------ figures
def fig1_oil_history(oil):
    fig, ax = plt.subplots(figsize=(11, 5))
    xs = [d(k) for k in oil]
    ax.plot(xs, list(oil.values()), color=INK, lw=1.4)
    ax.set_yscale("log")
    ax.yaxis.set_major_locator(LogLocator(base=10, subs=(1, 2, 5)))
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"${v:g}"))
    ax.yaxis.set_minor_formatter(NullFormatter())
    spikes = [("1973-10", "1975-01", "1973 禁运"), ("1979-01", "1981-03", "1979 伊朗革命"),
              ("1990-08", "1991-01", "1990 海湾战争"), ("2007-01", "2008-07", "2008 需求高峰"),
              ("2022-03", "2022-07", "2022 俄乌"), ("2026-03", "2026-08", "2026 霍尔木兹")]
    gluts = [("1985-12", "1986-07", "1986 沙特价格战"), ("2014-07", "2016-02", "2014 页岩过剩"),
             ("2020-02", "2020-05", "2020 疫情")]
    for i, (a, b, lab) in enumerate(spikes):
        ax.axvspan(d(a), d(b), color=SPIKE, lw=0)
        ax.text(d(a), 230 if i % 2 == 0 else 165, lab, color=ORANGE, fontsize=9, ha="left")
    for i, (a, b, lab) in enumerate(gluts):
        ax.axvspan(d(a), d(b), color=GLUT, lw=0)
        ax.text(d(a), 1.45 if i % 2 == 0 else 1.15, lab, color=SLATE, fontsize=9, ha="left")
    ax.hlines(63.8, d("2016-01"), d("2026-08"), colors=TEAL, linestyles="--", lw=1.2)
    ax.text(d("2027-01"), 63.8, "← 2016–25 均价 $64", color=TEAL, fontsize=9, ha="left", va="center")
    last = list(oil)[-1]
    ax.text(d("2027-01"), oil[last] * 1.08, f"← {last}：${oil[last]:.0f}", color=INK, fontsize=9, ha="left", va="center")
    ax.set_ylim(1, 320)
    ax.set_xlim(d("1949-01"), d("2034-12"))
    ax.set_title("1949–2026：美国原油价格（名义，对数轴）—— 冲击来得快，去得也快")
    ax.set_ylabel("美元 / 桶")
    finish(fig, "fig1_oil_price_1949_2026.png",
           "数据：EIA《月度能源评论》表 9.1 国内首购价（1949–73 年度、1974–85 月度）+ EIA WTI 现货（1986–2026-08）。米色 = 价格冲击，蓝灰 = 供给过剩 / 需求崩塌。")


def fig2_energy_vs_market(ffd):
    fig, ax = plt.subplots(figsize=(11, 5))
    months = sorted(ffd)
    e = m = 1.0
    xs, ev, mv = [], [], []
    for k in months:
        re_, rm = ffd[k]
        e *= 1 + re_
        m *= 1 + rm
        xs.append(d(k)); ev.append(e); mv.append(m)
    for a, b, lab, col, tcol in [("1973-01", "1980-12", "供给受约束\n能源 +11.5pp/年", SPIKE, ORANGE),
                                 ("1999-01", "2008-12", "供给受约束\n+12.3pp/年", SPIKE, ORANGE),
                                 ("1981-01", "1998-12", "供给放开\n−5.7pp/年", GLUT, SLATE),
                                 ("2009-01", "2019-12", "页岩：供给放开\n−11.1pp/年", GLUT, SLATE)]:
        ax.axvspan(d(a), d(b), color=col, lw=0)
        mid = d(a) + (d(b) - d(a)) / 2
        ax.text(mid, 2.0, lab, color=tcol, fontsize=8.5, ha="center", va="center")
    ax.plot(xs, mv, color=SLATE, lw=1.6, label="美国股市（CRSP 全市场）")
    ax.plot(xs, ev, color=TEAL, lw=1.8, label="能源行业组合（Ken French 12 行业 Enrgy）")
    ax.set_yscale("log")
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"${v:,.0f}" if v >= 1 else f"${v:g}"))
    ax.text(xs[-1] + dt.timedelta(days=150), ev[-1] * 1.45, f"能源 ${ev[-1]:,.0f}", color=TEAL, fontsize=9, va="center")
    ax.text(xs[-1] + dt.timedelta(days=150), mv[-1] * 0.62, f"市场 ${mv[-1]:,.0f}", color=SLATE, fontsize=9, va="center")
    ax.set_xlim(d("1926-01"), d("2036-12"))
    ax.legend(loc="upper left")
    ax.set_title(f"1926–{months[-1][:4]}：$1 投入的累计价值（含股息，对数轴）—— 能源只在供给被卡住时跑赢")
    finish(fig, "fig2_energy_vs_market_1926_2026.png",
           f"数据：Ken French Data Library（CRSP {months[-1].replace('-', '')}），12 行业市值加权月收益与 Mkt-RF + RF。时代超额收益引自 2026-09-16 电力报告 §11。")


def fig3_event_study(ffd, oil_peaks):
    fig, ax = plt.subplots(figsize=(11, 5.2))
    rel = list(range(-12, 37))
    paths = {}
    for name, pk in oil_peaks:
        r, ratio = {}, 1.0
        base_k = ym_add(pk, -12)
        series = {}
        for k in rel:
            mk = ym_add(pk, k)
            if mk not in ffd:
                break
            re_, rm = ffd[mk]
            ratio *= (1 + re_) / (1 + rm)
            series[k] = ratio
        if 0 in series:
            p0 = series[0]
            paths[name] = {k: v / p0 - 1 for k, v in series.items()}
    hist = [n for n in paths if not n.startswith("2026")]
    for n in hist:
        ks = sorted(paths[n])
        ax.plot(ks, [paths[n][k] * 100 for k in ks], color=SLATE, lw=1.1, alpha=0.75)
    avg = {k: sum(paths[n][k] for n in hist) / len(hist) for k in rel if all(k in paths[n] for n in hist)}
    ax.plot(sorted(avg), [avg[k] * 100 for k in sorted(avg)], color=TEAL, lw=2.6)
    # 右端标签去重叠：按值排序，最小间距 3.6pp
    ends = [(paths[n][36] * 100, f"{n} {paths[n][36]*100:+.0f}%", SLATE, "normal") for n in hist]
    ends.append((avg[36] * 100, f"五次平均 {avg[36]*100:+.0f}%", TEAL, "bold"))
    ends.sort()
    placed = []
    for y, lab, col, w in ends:
        yy = max(y, placed[-1] + 3.6) if placed else y
        placed.append(yy)
        ax.plot([36, 37.2], [y, yy], color=col, lw=0.6)
        ax.text(37.4, yy, lab, color=col, fontsize=8.5, va="center", fontweight=w)
    if "2026 霍尔木兹" in paths:
        p = paths["2026 霍尔木兹"]
        ks = sorted(p)
        ax.plot(ks, [p[k] * 100 for k in ks], color=ORANGE, lw=2.4)
        ax.text(ks[-1] + 0.6, p[ks[-1]] * 100 - 4, "2026（数据到 2026-07）", color=ORANGE, fontsize=9)
    ax.axvline(0, color=INK, lw=1, ls="--")
    ax.text(0.4, ax.get_ylim()[1] * 0.9 if ax.get_ylim()[1] > 0 else 5, "油价见顶的月份", fontsize=9, color=INK)
    ax.axhline(0, color=MUTED, lw=0.8)
    ax.axvspan(0, 12, color=SPIKE, lw=0, alpha=0.6)
    ax.text(1, -42, f"见顶后 12 个月：5 次全部跑输（平均 {avg[12]*100:+.0f}%）", color=ORANGE, fontsize=9.5)
    ax.set_xlim(-12, 47)
    ax.set_xlabel("距油价见顶的月数")
    ax.set_ylabel("相对大盘的累计超额（见顶月 = 0）")
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:+.0f}%"))
    ax.set_title("油价见顶前后：能源股相对大盘 —— 高峰之前一路跑赢，高峰之后一路跑输")
    finish(fig, "fig3_energy_after_oil_peaks.png",
           "数据：Ken French 12 行业 Enrgy vs 市场（Mkt-RF + RF）；见顶月取各次冲击窗口内月度油价最高点（见 data/oil_shocks.md）。超额 = 能源累计 ÷ 市场累计 − 1。")
    return avg


def fig4_buffett_actions(oil):
    fig, (ax, bx) = plt.subplots(2, 1, figsize=(11, 8.2), sharex=True,
                                 gridspec_kw={"height_ratios": [1.35, 1], "hspace": 0.12})
    ks = [k for k in oil if k >= "2000-01"]
    ax.plot([d(k) for k in ks], [oil[k] for k in ks], color=INK, lw=1.3)
    acts = [  # (月份, 买/卖, 标签, 文字偏移 x, y)
        ("2003-01", "buy", "买中石油 $4.9 亿\n（约估值的 1/3）", -10, 55),
        ("2007-09", "sell", "卖中石油 $40 亿", -95, 40),
        ("2008-06", "buy", "重仓康菲 $70 亿\n——自认\"重大错误\"", 18, -8),
        ("2009-06", "sell", "大幅卖出康菲", 12, -42),
        ("2013-09", "buy", "买埃克森", 14, 26),
        ("2014-12", "sell", "油价崩盘时\n清仓埃克森", -115, -62),
        ("2019-08", "buy", "OXY 8% 优先股\n+ 认股权证 $100 亿", -70, 78),
        ("2020-12", "buy", "疫情低点\n买雪佛龙", 22, -55),
        ("2022-03", "buy", "大举买入\nCVX + OXY", -95, 18),
        ("2026-03", "sell", "冲击中减持\nCVX 35%", -78, 48),
    ]
    for k, kind, lab, dx, dy in acts:
        col, mk = (TEAL, "^") if kind == "buy" else (ORANGE, "v")
        ax.scatter([d(k)], [oil[k]], s=70, marker=mk, color=col, zorder=5, edgecolor="white", linewidth=1.2)
        ax.annotate(lab, (d(k), oil[k]), xytext=(dx, dy), textcoords="offset points", fontsize=8.5, color=col,
                    arrowprops=dict(arrowstyle="-", color=col, lw=0.7))
    ax.set_ylim(0, 155)
    ax.set_ylabel("WTI 美元 / 桶")
    ax.scatter([], [], marker="^", color=TEAL, label="买入")
    ax.scatter([], [], marker="v", color=ORANGE, label="卖出")
    ax.legend(loc="upper left", ncol=2)
    ax.set_title("巴菲特 / 伯克希尔的每一笔石油操作，落在油价曲线的哪里（2000–2026）")

    rows = list(csv.DictReader((DATA / "brk_13f_oil.csv").open(encoding="utf-8")))
    qs = sorted({r["report_date"] for r in rows})
    val = {q: {"CVX": 0.0, "OXY": 0.0, "其他": 0.0} for q in qs}
    for r in rows:
        key = r["ticker"] if r["ticker"] in ("CVX", "OXY") else "其他"
        val[r["report_date"]][key] += float(r["value_usd"]) / 1e9
    xq = [dt.date.fromisoformat(q) for q in qs]
    bx.stackplot(xq, [val[q]["CVX"] for q in qs], [val[q]["OXY"] for q in qs], [val[q]["其他"] for q in qs],
                 colors=[TEAL, ORANGE, "#B8BEC8"], labels=["雪佛龙 CVX", "西方石油 OXY（普通股）", "其他：埃克森 / 康菲 / Phillips 66 / Suncor"],
                 edgecolor="white", linewidth=0.6)
    bx.set_ylabel("13F 市值（$B）")
    bx.legend(loc="upper left", fontsize=8.5)
    bx.text(dt.date(2001, 1, 1), 18, "另：2019 起持 OXY 8% 优先股（面值 $100 亿，现余 $85 亿）与认股权证，\n2026 年买下 OxyChem（约 $94 亿）—— 均不在 13F 中", fontsize=8.5, color=MUTED)
    bx.xaxis.set_major_locator(mdates.YearLocator(2))
    bx.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    bx.set_xlim(dt.date(2000, 1, 1), dt.date(2026, 12, 31))
    finish(fig, "fig4_buffett_oil_actions.png",
           "数据：油价 EIA WTI 月均；操作来自伯克希尔致股东信（2003–2025）与 13F。上图标记为操作所在季度/年份的近似月份；下图为 13F 季末市值（2013Q3 起有 XML 数据）。")


def fig5_since_2022(prices):
    fig, ax = plt.subplots(figsize=(11, 4.8))
    base = "2022-03"
    for tk, col, lab in [("SPY", SLATE, "标普 500（SPY）"), ("CVX", TEAL, "雪佛龙 CVX"), ("OXY", ORANGE, "西方石油 OXY")]:
        s = prices[tk]
        ks = [k for k in sorted(s) if k >= base]
        ys = [s[k] / s[base] * 100 for k in ks]
        ax.plot([d(k) for k in ks], ys, color=col, lw=2.0 if tk != "SPY" else 1.8, label=lab)
        ax.text(d(ks[-1]) + dt.timedelta(days=12), ys[-1], f"{lab} {ys[-1]-100:+.0f}%", color=col, fontsize=9, va="center")
    ax.axhline(100, color=MUTED, lw=0.8)
    ax.set_xlim(d(base), d("2027-08"))
    ax.set_ylabel("含股息总回报指数（2022-03 = 100）")
    ax.legend(loc="upper left")
    ax.set_title("伯克希尔 2022 年在高油价期大举加仓之后：两只石油股 vs 大盘")
    finish(fig, "fig5_since_2022_buys.png", "数据：Yahoo Finance 月度复权价（含股息再投资），2022-03 至 2026-09。")


def fig6_implied_oil():
    v = json.loads((REPO / "companies" / "_oil_2026-09-30" / "data" / "valuation_2026-09-30.json").read_text(encoding="utf-8"))
    spot = json.loads((DATA / "eia_monthly_spot.json").read_text(encoding="utf-8"))
    avg = {b: sum(x for k, x in spot[s].items() if "2016" <= k[:4] <= "2025") / 120
           for b, s in (("Brent", "Brent_spot"), ("WTI", "WTI_spot"))}
    last = {b: spot[s][max(spot[s])] for b, s in (("Brent", "Brent_spot"), ("WTI", "WTI_spot"))}
    rows = [("埃克森美孚 XOM", "XOM", "Brent"), ("雪佛龙 CVX", "CVX", "Brent"),
            ("西方石油 OXY", "OXY", "WTI"), ("康菲 COP", "COP", "WTI")]
    fig, ax = plt.subplots(figsize=(10, 4.4))
    for i, (lab, tk, bench) in enumerate(rows):
        y = len(rows) - 1 - i
        imp = v["tickers"][tk]["implied_oil_price_for_8pct"]
        a = avg[bench]
        ax.plot([a, imp], [y, y], color="#C9CED6", lw=4, solid_capstyle="round", zorder=1)
        ax.scatter([a], [y], s=90, color=SLATE, zorder=3, edgecolor="white", linewidth=1.5)
        ax.scatter([imp], [y], s=110, color=ORANGE, zorder=3, edgecolor="white", linewidth=1.5)
        ax.scatter([last[bench]], [y], s=60, marker="|", color=INK, zorder=4, linewidth=2)
        ax.text(imp, y + 0.22, f"${imp:.0f}（比十年均价高 ${imp - a:.0f}）", ha="center", va="bottom", fontsize=9.5, color=INK)
        ax.text(a - 1.5, y, f"{bench} 均价 ${a:.0f}", va="center", ha="right", fontsize=8.5, color=SLATE)
    ax.set_yticks(range(len(rows)))
    ax.set_yticklabels([r[0] for r in rows][::-1])
    ax.set_xlim(40, 125)
    ax.xaxis.set_major_formatter(FuncFormatter(lambda x, _: f"${x:.0f}"))
    ax.grid(axis="y", visible=False)
    ax.scatter([], [], s=70, color=SLATE, label="2016–25 年均价")
    ax.scatter([], [], s=80, color=ORANGE, label="现价要拿到 8% 所需的长期油价")
    ax.scatter([], [], marker="|", color=INK, s=60, label=f"2026-08 现货（WTI ${last['WTI']:.0f} / Brent ${last['Brent']:.0f}）")
    ax.set_ylim(-0.5, len(rows) - 0.35)
    ax.legend(loc="lower right", fontsize=8.5)
    ax.set_title("今天的股价在押多高的油价？—— 四家油气公司都要求长期油价高于过去十年")
    finish(fig, "fig6_implied_oil_price.png",
           "数据：companies/_oil_2026-09-30/valuation_model.py（base 情景：g、退出倍数、返还比例不变，只让油价变动）；EIA 现货月均。XOM、CVX 以 Brent 计，OXY、COP 以 WTI 计。")


def fig7_oxy_structure():
    debt, pref, common = 11.8, 8.5, 54.9
    brk_common = common * 0.267
    fig, ax = plt.subplots(figsize=(10.5, 3.2))
    segs = [("债务（本金）\n$11.8B", debt, SLATE, "white"),
            ("伯克希尔\n8% 优先股\n$8.5B", pref, ORANGE, "white"),
            ("普通股：伯克希尔 26.7%\n≈ $14.7B", brk_common, TEAL, "white"),
            ("普通股：其他股东（含你）\n≈ $40.2B", common - brk_common, "#9ED3CC", INK)]
    left = 0.0
    for lab, w, col, tc in segs:
        ax.barh([0], [w], left=left, color=col, edgecolor="white", linewidth=2.5, height=0.6)
        ax.text(left + w / 2, 0, lab, ha="center", va="center", fontsize=9, color=tc)
        left += w
    ax.annotate("", xy=(0, -0.48), xytext=(debt + pref, -0.48), arrowprops=dict(arrowstyle="<->", color=INK, lw=1))
    ax.text((debt + pref) / 2, -0.62, "先拿钱：油价跌时先受保护", ha="center", va="top", fontsize=9, color=INK)
    ax.annotate("", xy=(debt + pref, -0.48), xytext=(left, -0.48), arrowprops=dict(arrowstyle="<->", color=TEAL, lw=1))
    ax.text(debt + pref + common / 2, -0.62, "最后拿钱、杠杆最高：散户只能买到这一层", ha="center", va="top", fontsize=9, color=TEAL)
    ax.set_xlim(0, left * 1.01)
    ax.set_ylim(-0.95, 0.45)
    ax.set_yticks([])
    ax.grid(False)
    ax.spines["left"].set_visible(False)
    ax.xaxis.set_major_formatter(FuncFormatter(lambda x, _: f"${x:.0f}B"))
    ax.set_title("西方石油（OXY）的资本结构：伯克希尔拿的和你能买的不是同一层")
    finish(fig, "fig7_oxy_capital_structure.png",
           "数据：OXY 2026Q2 8-K（本金债务）、伯克希尔 2026Q2 10-Q（优先股 $8.5B、持股 26.7%；认股权证 8,390 万股 @ $59.59 未画出）；普通股市值按 2026-09-29 收盘 $54.94。")


def main():
    oil = oil_monthly()
    ffd = ff()
    fig1_oil_history(oil)
    fig2_energy_vs_market(ffd)
    peaks = [("1973 禁运", "1975-01"), ("1979 伊朗", "1981-03"), ("1990 海湾", "1990-10"),
             ("2008 高峰", "2008-06"), ("2022 俄乌", "2022-06"), ("2026 霍尔木兹", "2026-05")]
    avg = fig3_event_study(ffd, peaks)
    print("event-study avg excess: +12m %.1f%%, +36m %.1f%%" % (avg[12] * 100, avg[36] * 100))
    fig4_buffett_actions(oil)
    fig5_since_2022(yahoo_monthly(["SPY", "CVX", "OXY"]))
    fig6_implied_oil()
    fig7_oxy_structure()


if __name__ == "__main__":
    main()
