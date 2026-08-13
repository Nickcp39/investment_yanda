#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""NVDA 暴涨期小盘热点股 2022→2026-08 轨迹图。

数据内嵌于本文件（单一事实源），运行时同步导出 data.csv。
置信度: S=本轮网络检索 R=仓库档案 D=由S数据推算 M=模型知识(高置信) L=模型知识(近似,±)
图中: 实心点=S/R/D/M · 空心点=L · 点线=含L段 · 虚线=年度缺口直连 · ▲=波段峰值
"""
import csv
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from pathlib import Path

plt.rcParams["font.sans-serif"] = ["WenQuanYi Zen Hei", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["text.parse_math"] = False

HERE = Path(__file__).resolve().parent

# ---- 调色板（dataviz 默认分类色，已过验证器；见报告§5） ----
INK, INK2, MUTED = "#0b0b0b", "#52514e", "#898781"
SURFACE, GRID, BASE = "#fcfcfb", "#e1e0d9", "#c3c2b7"
GROUP_COLORS = {
    "AI软件叙事": "#2a78d6",
    "NVDA持仓概念": "#eb6834",
    "卖铲人": "#1baf7a",
    "矿工转AI": "#eda100",
    "量子番外": "#e87ba4",
    "基准": INK,
}

# ---- 数据 ----
# series: (x, price, conf)  x: 0=2021末 1=2022末 2=2023末 3=2024末 4=2025末 4.62=2026-08
# peak: (price, x, 标签, conf) 或 None（日期不明→仅文字）
T = [
    dict(t="NVDA", n="英伟达(基准)", g="基准",
         s=[(0, 29.41, "M"), (1, 14.61, "M"), (2, 49.52, "M"), (3, 134.29, "M"), (4, 185.70, "D"), (4.62, 223.40, "S")],
         peak=None, peak_note="现价≈周期高位", src="s22"),
    dict(t="AI", n="C3.ai", g="AI软件叙事",
         s=[(0, 31.45, "M"), (1, 11.21, "M"), (2, 28.68, "M"), (3, 34.45, "M"), (4, 15.50, "L"), (4.62, 10.63, "S")],
         peak=(48.87, 1.42, "$48.9 · 23-06", "M"), src="s1,s8"),
    dict(t="BBAI", n="BigBear.ai", g="AI软件叙事",
         s=[(0, 5.80, "M"), (1, 0.67, "S"), (2, 2.11, "M"), (3, 4.43, "M"), (4, 4.31, "D"), (4.62, 3.33, "S")],
         peak=(10.36, 3.12, "$10.4 · 25-02", "S"), src="s1,s7"),
    dict(t="SOUN", n="SoundHound", g="AI软件叙事",
         s=[(1, 1.42, "M"), (2, 2.12, "M"), (3, 20.66, "S"), (4, 14.00, "L"), (4.62, 6.45, "S")],
         peak=(24.98, 2.99, "$25.0 · 24-12", "S"), note="22-04 SPAC上市", src="s1,s3,s5"),
    dict(t="NNOX", n="Nano-X 影像", g="NVDA持仓概念",
         s=[(0, 17.2, "L"), (1, 10.72, "M"), (2, 6.16, "M"), (3, 7.20, "D"), (4.62, 1.80, "S")],
         peak=None, peak_note="24-02 13F日 +49%", src="s3,s9"),
    dict(t="RXRX", n="Recursion", g="NVDA持仓概念",
         s=[(0, 16.36, "M"), (1, 5.50, "M"), (2, 9.81, "M"), (3, 6.55, "M"), (4, 4.70, "L"), (4.62, 3.22, "S")],
         peak=None, peak_note="23-07 NVDA注资 +78%", src="s3,s10"),
    dict(t="SERV", n="Serve Robotics", g="NVDA持仓概念",
         s=[(3, 13.50, "L"), (4.62, 4.92, "S")],
         peak=(18.64, 3.6, "$18.6 · 52周高", "S"), note="24-04 上市", src="s11"),
    dict(t="SMCI", n="超微电脑", g="卖铲人",
         s=[(0, 4.39, "M"), (1, 8.21, "S"), (2, 28.43, "S"), (3, 30.49, "S"), (4, 30.0, "L"), (4.62, 35.96, "S")],
         peak=(118.81, 2.20, "$118.8 · 24-03", "S"), src="s2,s6"),
    dict(t="VRT", n="Vertiv", g="卖铲人",
         s=[(0, 24.96, "M"), (1, 13.66, "M"), (2, 48.02, "M"), (3, 114.34, "M"), (4, 140.60, "D"), (4.62, 292.96, "S")],
         peak=(379.94, 4.45, "$379.9 · 52周高", "S"), src="s12"),
    dict(t="MOD", n="Modine 散热", g="卖铲人",
         s=[(0, 10.09, "M"), (1, 19.34, "M"), (2, 59.74, "M"), (3, 116.10, "M"), (4, 131.0, "L"), (4.62, 205.0, "S")],
         peak=(323.25, 4.45, "$323.3 · 52周高", "S"), src="s13"),
    dict(t="POWL", n="Powell 电力设备", g="卖铲人",
         s=[(0, 29.2, "L"), (1, 35.8, "L"), (2, 91.4, "M"), (3, 243.0, "L"), (4.62, 208.63, "S")],
         peak=(364.98, 2.87, "$365.0 · 24-11", "M"), src="s14"),
    dict(t="INOD", n="Innodata 数据工程", g="卖铲人",
         s=[(0, 3.87, "L"), (1, 3.43, "M"), (2, 8.79, "M"), (3, 39.40, "M"), (4.62, 69.76, "S")],
         peak=(125.14, 4.4, "$125.1 · 52周高", "S"), src="s15"),
    dict(t="AEHR", n="Aehr 晶圆测试", g="卖铲人",
         s=[(1, 27.1, "L"), (2, 25.2, "L"), (3, 14.0, "L"), (4.62, 131.72, "S")],
         peak=(54.10, 1.55, "$54.1 · 23-07", "M"), note="26年AI烧机订单第二春", src="s16"),
    dict(t="APLD", n="Applied Digital", g="矿工转AI",
         s=[(1, 1.91, "M"), (2, 6.72, "M"), (3, 7.71, "M"), (4.62, 29.69, "S")],
         peak=(50.73, 4.4, "$50.7 · 52周高", "S"), note="CoreWeave $7B 租约", src="s17"),
    dict(t="WULF", n="TeraWulf", g="矿工转AI",
         s=[(0, 11.0, "L"), (1, 0.40, "M"), (2, 2.33, "M"), (3, 5.66, "M"), (4.62, 18.46, "S")],
         peak=None, peak_note="Anthropic $19B 租约", src="s18"),
    dict(t="IREN", n="Iris Energy", g="矿工转AI",
         s=[(0, 18.0, "L"), (1, 1.06, "M"), (2, 6.87, "L"), (3, 9.90, "L"), (4.62, 34.83, "R")],
         peak=None, peak_note="距6/22市值峰 -34%", src="s19"),
    dict(t="IONQ", n="IonQ", g="量子番外",
         s=[(0, 16.65, "M"), (1, 3.43, "M"), (2, 12.36, "M"), (3, 41.85, "M"), (4.62, 41.72, "S")],
         peak=(69.28, 4.42, "$69.3 · 26-06", "S"), src="s20,s21"),
    dict(t="RGTI", n="Rigetti", g="量子番外",
         s=[(0, 9.46, "L"), (1, 0.58, "M"), (2, 0.94, "M"), (3, 15.34, "M"), (4.62, 17.45, "S")],
         peak=(25.63, 4.42, "$25.6 · 26-06", "S"), src="s20,s21"),
]

SOLID = {"S", "R", "D", "M"}
XT = [0, 1, 2, 3, 4, 4.62]
XL = ["21末", "22", "23", "24", "25", "今"]


def fmt(p):
    return f"${p:,.2f}" if p < 10 else (f"${p:,.1f}" if p < 1000 else f"${p:,.0f}")


def export_csv():
    xdate = {0: "2021-12-31", 1: "2022-12-30", 2: "2023-12-29", 3: "2024-12-31", 4: "2025-12-31", 4.62: "2026-08-12"}
    with open(HERE / "data.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["ticker", "name_cn", "group", "point", "date", "price_usd", "confidence", "sources", "note"])
        for d in T:
            for x, p, c in d["s"]:
                w.writerow([d["t"], d["n"], d["g"], "close", xdate[x], p, c, d["src"], d.get("note", "")])
            if d["peak"]:
                w.writerow([d["t"], d["n"], d["g"], "cycle_peak", d["peak"][2].split("·")[-1].strip(), d["peak"][0], d["peak"][3], d["src"], ""])


def chart1():
    fig, axes = plt.subplots(6, 3, figsize=(12.5, 17.5))
    fig.patch.set_facecolor(SURFACE)
    for ax, d in zip(axes.flat, T):
        c = GROUP_COLORS[d["g"]]
        ax.set_facecolor(SURFACE)
        pts = d["s"]
        # 分段画线：段样式由端点置信度与是否跨缺口决定
        for (x0, p0, c0), (x1, p1, c1) in zip(pts, pts[1:]):
            gap = (x1 - x0) > 1.01  # 跳过了某个年末
            ls = "--" if gap else (":" if (c0 == "L" or c1 == "L") else "-")
            ax.plot([x0, x1], [p0, p1], ls=ls, lw=2, color=c, solid_capstyle="round", zorder=3)
        for x, p, cf in pts:
            if cf == "L":
                ax.plot(x, p, "o", ms=5.5, mfc=SURFACE, mec=c, mew=1.6, zorder=4)
            else:
                ax.plot(x, p, "o", ms=5 if x < 4.6 else 7, mfc=c, mec=c, zorder=4)
        if d["peak"]:
            pp, px, pl, _ = d["peak"]
            ax.plot(px, pp, "^", ms=7, mfc=SURFACE, mec=c, mew=1.6, zorder=5)
            ax.annotate(pl, (px, pp), textcoords="offset points", xytext=(0, 7),
                        ha="center", fontsize=7, color=MUTED)
        # 标题与现价/回撤
        last = pts[-1][1]
        peakv = d["peak"][0] if d["peak"] else max(p for _, p, _ in pts)
        dd = last / peakv - 1
        ax.text(0.02, 1.14, f"{d['t']} · {d['n']}", transform=ax.transAxes,
                fontsize=10.5, fontweight="bold", color=INK, va="top")
        sub = f"现 {fmt(last)}" + (f" · 距峰 {dd:+.0%}" if dd < -0.005 else " · 高位区")
        if d.get("peak_note"):
            sub += f" · {d['peak_note']}"
        elif d.get("note"):
            sub += f" · {d['note']}"
        ax.text(0.02, 1.045, sub, transform=ax.transAxes, fontsize=7.8, color=INK2, va="top")
        ax.set_yscale("log")
        ax.grid(axis="y", color=GRID, lw=0.7)
        ax.set_axisbelow(True)
        for sp in ax.spines.values():
            sp.set_visible(False)
        ax.spines["bottom"].set_visible(True)
        ax.spines["bottom"].set_color(BASE)
        ax.tick_params(axis="both", length=0, labelsize=7.5, colors=MUTED)
        ax.set_xlim(-0.25, 4.87)
        ax.set_xticks(XT)
        ax.set_xticklabels(XL if d in T[-3:] else [""] * 6)
        from matplotlib.ticker import LogLocator, NullFormatter, FuncFormatter
        ax.yaxis.set_major_locator(LogLocator(base=10, numticks=4))
        ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"${v:g}"))
        ax.yaxis.set_minor_formatter(NullFormatter())
        lo = min(p for _, p, _ in pts)
        hi = max(peakv, max(p for _, p, _ in pts))
        ax.set_ylim(lo * 0.42, hi * 2.6)
    handles = [Line2D([], [], color=GROUP_COLORS[g], lw=2.5, label=g) for g in
               ["AI软件叙事", "NVDA持仓概念", "卖铲人", "矿工转AI", "量子番外", "基准"]]
    handles += [Line2D([], [], color=INK2, lw=1.6, ls=":", label="段含近似点(空心)"),
                Line2D([], [], color=INK2, lw=1.6, ls="--", label="年度数据缺口直连"),
                Line2D([], [], color=INK2, marker="^", ls="", mfc=SURFACE, label="波段峰值")]
    fig.legend(handles=handles, loc="lower center", fontsize=8.8, frameon=False, ncol=5,
               labelcolor=INK2, handlelength=1.7, columnspacing=1.4, bbox_to_anchor=(0.5, 0.002))
    fig.suptitle("NVDA 暴涨期的小盘热点股：2022 → 2026-08 股价轨迹（对数轴）",
                 fontsize=15, fontweight="bold", color=INK, x=0.055, ha="left", y=0.988)
    fig.text(0.055, 0.9715, "年末收盘 + 2026-08 现价 · 空心点=近似值(±) · 虚线=缺口 · ▲=波段峰 · 数据置信度逐点见 data.csv",
             fontsize=9, color=INK2)
    fig.subplots_adjust(left=0.055, right=0.975, top=0.925, bottom=0.052, hspace=0.62, wspace=0.24)
    fig.savefig(HERE / "chart1_trajectories.png", dpi=150, facecolor=SURFACE)
    plt.close(fig)


def chart2():
    rows = [  # (ticker, group, 22末→峰值倍数, 峰值→今回撤, 备注)
        ("RGTI", "量子番外", 25.63 / 0.58, 17.45 / 25.63 - 1, ""),
        ("INOD", "卖铲人", 125.14 / 3.43, 69.76 / 125.14 - 1, ""),
        ("VRT", "卖铲人", 379.94 / 13.66, 292.96 / 379.94 - 1, ""),
        ("APLD", "矿工转AI", 50.73 / 1.91, 29.69 / 50.73 - 1, ""),
        ("IONQ", "量子番外", 69.28 / 3.43, 41.72 / 69.28 - 1, ""),
        ("SOUN", "AI软件叙事", 24.98 / 1.42, 6.45 / 24.98 - 1, ""),
        ("MOD", "卖铲人", 323.25 / 19.34, 205.0 / 323.25 - 1, ""),
        ("BBAI", "AI软件叙事", 10.36 / 0.67, 3.33 / 10.36 - 1, ""),
        ("NVDA", "基准", 223.40 / 14.61, 0.0, "现价≈峰"),
        ("SMCI", "卖铲人", 118.81 / 8.21, 35.96 / 118.81 - 1, ""),
        ("POWL", "卖铲人", 364.98 / 35.8, 208.63 / 364.98 - 1, ""),
        ("AEHR", "卖铲人", 132.99 / 27.1, 131.72 / 132.99 - 1, "现价≈峰"),
        ("AI", "AI软件叙事", 48.87 / 11.21, 10.63 / 48.87 - 1, ""),
    ]
    rows.sort(key=lambda r: r[2], reverse=True)
    ys = range(len(rows) - 1, -1, -1)
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(12.5, 7.2), sharey=True)
    fig.patch.set_facecolor(SURFACE)
    for ax in (a1, a2):
        ax.set_facecolor(SURFACE)
        for sp in ax.spines.values():
            sp.set_visible(False)
        ax.tick_params(length=0, labelsize=9, colors=MUTED)
        ax.set_axisbelow(True)
    for y, (t, g, mult, dd, note) in zip(ys, rows):
        c = GROUP_COLORS[g]
        a1.barh(y, mult, height=0.62, color=c, zorder=3)
        a1.text(mult * 1.07, y, f"×{mult:,.1f}", va="center", fontsize=9,
                color=INK, fontweight="bold")
        if dd < -0.005:
            a2.barh(y, dd * 100, height=0.62, color=c, alpha=0.55, zorder=3)
            a2.text(dd * 100 - 1.2, y, f"{dd:+.0%}", va="center", ha="right",
                    fontsize=9, color=INK, fontweight="bold")
        else:
            a2.text(-1.2, y, "≈周期高位", va="center", ha="right", fontsize=8.5, color="#006300")
        lbl = f"{t}"
        a1.text(-0.12, y, lbl, va="center", ha="right", transform=a1.get_yaxis_transform(),
                fontsize=9.5, color=INK, fontweight="bold")
        a1.text(-0.015, y, {"AI软件叙事": "软件", "NVDA持仓概念": "持仓", "卖铲人": "铲子",
                            "矿工转AI": "矿工", "量子番外": "量子", "基准": "基准"}[g],
                va="center", ha="right", transform=a1.get_yaxis_transform(), fontsize=8, color=MUTED)
    a1.set_xscale("log")
    a1.set_xlim(1, 130)
    a1.set_xticks([1, 3, 10, 30, 100])
    a1.set_xticklabels(["×1", "×3", "×10", "×30", "×100"])
    a1.grid(axis="x", color=GRID, lw=0.7)
    a1.set_title("2022年末 → 周期峰值（倍数，对数轴）", fontsize=11, color=INK, loc="left", pad=10)
    a2.set_xlim(-88, 2)
    a2.set_xticks([0, -25, -50, -75])
    a2.set_xticklabels(["0", "-25%", "-50%", "-75%"])
    a2.grid(axis="x", color=GRID, lw=0.7)
    a2.axvline(0, color=BASE, lw=1)
    a2.set_title("周期峰值 → 现在（回撤）", fontsize=11, color=INK, loc="left", pad=10)
    a1.set_yticks([])
    fig.suptitle("涨了多少 · 吐回了多少 —— 同一批热点股的往返", fontsize=14.5,
                 fontweight="bold", color=INK, x=0.055, ha="left", y=0.975)
    fig.text(0.055, 0.918, "峰值取本轮周期高点或52周高（见data.csv）· IONQ/RGTI 峰值为 2026-06-01 读数 · MOD 现价为 8 月上旬读数",
             fontsize=8.5, color=INK2)
    fig.subplots_adjust(left=0.13, right=0.965, top=0.86, bottom=0.06, wspace=0.10)
    fig.savefig(HERE / "chart2_roundtrip.png", dpi=150, facecolor=SURFACE)
    plt.close(fig)


if __name__ == "__main__":
    export_csv()
    chart1()
    chart2()
    print("done:", *[p.name for p in HERE.glob("*.png")], "data.csv")
