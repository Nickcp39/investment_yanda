"""画回测图：上排 $100 增长（对数轴），下排每年超额收益（策略 − 基准 ETF）。读 backtest_yearly.csv。"""
import csv
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.font_manager import FontProperties  # noqa: E402
from matplotlib.ticker import FuncFormatter  # noqa: E402

HERE = Path(__file__).resolve().parent
BLUE, ORANGE, AQUA, RED = "#2a78d6", "#eb6834", "#1baf7a", "#e34948"   # dataviz 默认分类色 1–3；发散对 蓝/红
INK, INK2, GRID, SURF = "#0b0b0b", "#52514e", "#e6e5e1", "#fcfcfb"
PARTIAL_X = 2025 + 295 / 365   # 2026 只到 10-22

rows = list(csv.DictReader((HERE / "backtest_yearly.csv").open(encoding="utf-8-sig")))
font = FontProperties(fname="C:/Windows/Fonts/msyh.ttc")
plt.rcParams.update({"font.family": font.get_name(), "axes.unicode_minus": False, "font.size": 9, "text.parse_math": False,
                     "axes.spines.top": False, "axes.spines.right": False, "axes.edgecolor": INK2, "axes.labelcolor": INK2,
                     "xtick.color": INK2, "ytick.color": INK2, "figure.facecolor": SURF, "axes.facecolor": SURF, "savefig.dpi": 170})
fig, axs = plt.subplots(2, 2, figsize=(13, 8.6), gridspec_kw={"height_ratios": [1.55, 1]})

for col, (uni, bn, title) in enumerate([("NDX100", "QQQ", "纳指100：每年买上一年前十（2007–2026，20 年）"),
                                        ("SP500", "SPY", "标普500：每年买上一年前十（1997–2026，30 年）")]):
    rs = [r for r in rows if r["universe"] == uni]
    years = [int(r["year"]) for r in rs]
    x = [years[0] - 1] + [PARTIAL_X if r["partial"] == "True" else int(r["year"]) for r in rs]
    ax = axs[0][col]
    low = [int(r["year"]) for r in rs if float(r["coverage_pick_year"]) < 0.8]
    if low:
        ax.axvspan(low[0] - 1, low[-1], color="#f0efec", zorder=0)
        cv = [float(r["coverage_pick_year"]) for r in rs if float(r["coverage_pick_year"]) < 0.8]
        ax.text(low[0] - 0.7, 0.97, f"早期：选股年只有 {min(cv):.0%}–{max(cv):.0%} 的成分股有数据\n（缺的多是后来破产/被收购的）→ 结果偏乐观",
                transform=ax.get_xaxis_transform(), va="top", fontsize=7.5, color=INK2)
    series = [("v_strategy", "前十策略", BLUE, "-"), ("v_bench", bn, ORANGE, "-"), ("v_ew", "同口径等权对照", AQUA, (0, (4, 2)))]
    finals = []
    for key, lab, c, ls in series:
        v = [100.0] + [float(r[key]) for r in rs]
        ax.plot(x, v, color=c, lw=2, ls=ls, label=lab, solid_capstyle="round")
        finals.append((v[-1], lab, c))
    # 直接标注终值（按数值排开，避免重叠）
    finals.sort()
    ypos = []
    for i, (fv, lab, c) in enumerate(finals):
        y = fv
        if ypos and y / ypos[-1] < 1.22:
            y = ypos[-1] * 1.22
        ypos.append(y)
        ax.annotate(f"{lab}  ${fv:,.0f}", (x[-1], fv), xytext=(x[-1] + 0.4, y), textcoords="data", fontsize=8.5,
                    color=INK, va="center", arrowprops=dict(arrowstyle="-", color=c, lw=0.8))
        ax.plot([x[-1]], [fv], "o", color=c, ms=4.5, mec=SURF, mew=1.2, zorder=3)
    ax.set_yscale("log")
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"${v:,.0f}"))
    ax.set_xlim(x[0] - 0.5, x[-1] + 7.5)
    ax.grid(axis="y", color=GRID, lw=0.8)
    ax.set_title(title, loc="left", fontweight="bold", fontsize=10.5, color=INK, pad=17)
    ticks = list(range((years[0] // 5) * 5 + 5, 2026, 5))
    ax.set_xticks(ticks)
    ax.text(0, 1.005, "起始 $100，每只 10%，每年年底换仓；纵轴为对数刻度", transform=ax.transAxes, fontsize=7.5, color=INK2, va="bottom")
    ax.legend(loc="upper left", bbox_to_anchor=(0.0, 0.84), frameon=False, fontsize=8)

    ax = axs[1][col]
    ex = [(float(r["strategy"]) - float(r["bench"])) * 100 for r in rs]
    xb = years
    ax.bar(xb, ex, width=0.72, color=[BLUE if e >= 0 else RED for e in ex], edgecolor=SURF, linewidth=1)
    ax.axhline(0, color="#9a9994", lw=0.8)
    lo_i, hi_i = ex.index(min(ex)), ex.index(max(ex))
    for i in {lo_i, hi_i}:
        ax.annotate(f"{xb[i]}{'*' if rs[i]['partial'] == 'True' else ''}\n{ex[i]:+.0f}", (xb[i], ex[i]),
                    xytext=(0, 4 if ex[i] >= 0 else -4), textcoords="offset points", ha="center",
                    va="bottom" if ex[i] >= 0 else "top", fontsize=7.5, color=INK)
    beat = sum(e > 0 for e in ex)
    ax.set_title(f"每年超额收益（策略 − {bn}，百分点）：跑赢 {beat}/{len(ex)} 年", loc="left", fontweight="bold", fontsize=9.5, color=INK)
    ax.grid(axis="y", color=GRID, lw=0.8)
    ax.set_xlim(axs[0][col].get_xlim()[0], years[-1] + 1)
    ax.set_xticks(ticks)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:+.0f}"))
    ylim = max(abs(min(ex)), abs(max(ex))) * 1.3
    ax.set_ylim(-ylim, ylim)

fig.suptitle("每年买上一年涨幅前十：纳指100 输给 QQQ，标普500 跑赢 SPY（主要靠 2019 年以后）", x=0.01, ha="left",
             fontweight="bold", fontsize=12.5, color=INK)
fig.text(0.01, 0.008, "数据：point-in-time 年初成分股（标普 1996 起、纳指 2006 起）+ Yahoo 复权价（含分红拆股）；基准 SPY/QQQ 总回报。"
         "不计交易成本和税。2026* 只到 10-22。对照线 = 同年所有有数据成分股等权，和策略带同样的幸存者偏差。已剔除 7 处 ticker 复用/复权错误。",
         fontsize=7.2, color=INK2)
fig.tight_layout(rect=(0, 0.025, 1, 0.955))
fig.savefig(HERE / "backtest_top10.png")
print(HERE / "backtest_top10.png")
