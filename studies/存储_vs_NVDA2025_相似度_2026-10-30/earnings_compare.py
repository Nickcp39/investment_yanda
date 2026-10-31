"""逐季财报对比：把各家「同一时刻」对齐到 T0，看 T0 前后几个季度的轨迹像不像。

T0 = 股价高点后第 88 个交易日（MU/SNDK 的今天）之前最近一次财报：
- NVDA 2025：Q4 FY25（2025-02-26）      - MU 2018：FQ4 FY18（2018-09-20）
- MU 2022：FQ2 FY22（2022-03-29）       - MU 2026：FQ4 FY26（2026-09-30）
- SNDK 2026：FQ4 FY26（2026-08-05；FQ1 FY27 若已发布就是 T+1）
读 data/{nvda,mu,sndk}_quarters.csv（研究子代理整理，一手来源为主）。
运行：python earnings_compare.py → 打印对齐表，写 data/earnings_aligned.csv、earnings_compare.png
"""
import csv
from pathlib import Path

HERE = Path(__file__).resolve().parent
D = HERE / "data"


def load(f):
    p = D / f
    if not p.exists():
        return []
    rows = list(csv.DictReader(p.open(encoding="utf-8-sig")))
    for r in rows:
        for k in list(r):
            if k not in ("company", "fiscal_quarter", "period_end", "report_date", "source"):
                try:
                    r[k] = float(str(r[k]).replace("%", "").replace(",", "")) if r[k] not in ("", None, "n/a", "NA") else None
                except ValueError:
                    r[k] = None
    return sorted(rows, key=lambda r: r["report_date"] or "")


SERIES = [  # (标签, 文件, 公司筛选, T0 报告日)
    ("NVDA 2025", "nvda_quarters.csv", "NVDA", "2025-02-26"),
    ("MU 2018 周期顶", "mu_quarters.csv", "MU", "2018-09-20"),
    ("MU 2022 周期顶", "mu_quarters.csv", "MU", "2022-03-29"),
    ("MU 2026（现在）", "mu_quarters.csv", "MU", "2026-09-30"),
    ("SNDK 2026（现在）", "sndk_quarters.csv", "SNDK", "2026-08-05"),
]
aligned = []
for label, f, co, t0 in SERIES:
    rows = [r for r in load(f) if (r.get("company") or "").upper().startswith(co)
            and (r.get("report_date") or "")[:4].isdigit()]   # 只有指引、还没发布的行不参与对齐
    _t0 = __import__("datetime").date.fromisoformat(t0)
    rows = [r for r in rows if abs((__import__("datetime").date.fromisoformat(r["report_date"][:10]) - _t0).days) <= 460]  # 同一轮周期内，约 ±15 个月
    if not rows:
        print(f"{label}: 无数据（{f}）")
        continue
    # T0 = 报告日最接近给定日期的那一行
    i0 = min(range(len(rows)), key=lambda i: abs((__import__("datetime").date.fromisoformat(rows[i]["report_date"][:10])
                                                  - __import__("datetime").date.fromisoformat(t0)).days))
    for i, r in enumerate(rows):
        k = i - i0
        if -5 <= k <= 4:
            guide_growth = (r["next_q_guide_rev_mid_usd_m"] / r["revenue_usd_m"] - 1) * 100 if r.get("next_q_guide_rev_mid_usd_m") and r.get("revenue_usd_m") else None
            aligned.append({"series": label, "k": k, "fq": r["fiscal_quarter"], "report_date": r["report_date"],
                            "revenue": r.get("revenue_usd_m"), "qoq": r.get("qoq_pct"), "yoy": r.get("yoy_pct"),
                            "gm": r.get("gm_nongaap_pct"), "beat": r.get("beat_vs_mid_pct"), "guide_qoq": guide_growth,
                            "guide_gm": r.get("next_q_guide_gm_mid_pct"), "reaction": r.get("stock_reaction_next_day_pct")})

fmt = lambda v, s="{:+.0f}": "—" if v is None else s.format(v)
print("对齐表（k = 相对 T0 的季度序号；T0 = 高点后第 88 个交易日之前最近一次财报）")
print(f"{'系列':16s} {'k':>3s} {'季度':10s} {'报告日':11s} {'收入$M':>9s} {'环比%':>6s} {'同比%':>6s} {'毛利率%':>7s} {'超指引%':>7s} {'下季指引环比%':>12s} {'次日涨跌%':>9s}")
for a in aligned:
    print(f"{a['series']:16s} {a['k']:>3d} {a['fq']:10s} {a['report_date'][:10]:11s} {fmt(a['revenue'], '{:,.0f}'):>9s} {fmt(a['qoq']):>6s} {fmt(a['yoy']):>6s} "
          f"{fmt(a['gm'], '{:.1f}'):>7s} {fmt(a['beat'], '{:+.1f}'):>7s} {fmt(a['guide_qoq']):>12s} {fmt(a['reaction'], '{:+.1f}'):>9s}")
if aligned:
    with (D / "earnings_aligned.csv").open("w", newline="", encoding="utf-8-sig") as fh:
        w = csv.DictWriter(fh, fieldnames=list(aligned[0]))
        w.writeheader()
        w.writerows(aligned)

# ---- 图：环比增速、毛利率、下季指引环比 三个小图
import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.font_manager import FontProperties  # noqa: E402

font = FontProperties(fname="C:/Windows/Fonts/msyh.ttc")
INK, INK2, GRID, SURF = "#0b0b0b", "#52514e", "#e6e5e1", "#fcfcfb"
plt.rcParams.update({"font.family": font.get_name(), "axes.unicode_minus": False, "font.size": 9, "text.parse_math": False,
                     "axes.spines.top": False, "axes.spines.right": False, "axes.edgecolor": INK2, "xtick.color": INK2,
                     "ytick.color": INK2, "figure.facecolor": SURF, "axes.facecolor": SURF, "savefig.dpi": 170})
STYLE = {"NVDA 2025": ("#2a78d6", "-", 2.2, "o"), "MU 2026（现在）": ("#eb6834", "-", 2.2, "o"), "SNDK 2026（现在）": ("#1baf7a", "-", 2.2, "o"),
         "MU 2018 周期顶": ("#6250d6", (0, (4, 2)), 1.5, "s"), "MU 2022 周期顶": ("#e87ba4", (0, (4, 2)), 1.5, "s")}
panels = [("qoq", "① 收入环比增速 %"), ("guide_qoq", "② 下季收入指引中值 / 本季收入 − 1，%"), ("beat", "③ 实际收入超出指引中值 %"), ("gm", "④ non-GAAP 毛利率 %")]
fig, axs = plt.subplots(2, 2, figsize=(13, 8.4))
axs = axs.flatten()
for ax, (key, title) in zip(axs, panels):
    for label, (c, ls, lw, mk) in STYLE.items():
        pts = [(a["k"], a[key]) for a in aligned if a["series"] == label and a[key] is not None]
        if pts:
            ax.plot([p[0] for p in pts], [p[1] for p in pts], color=c, ls=ls, lw=lw, marker=mk, ms=4.5, mec=SURF, label=label)
    ax.axvline(0, color="#9a9994", lw=0.8, ls=":")
    ax.axhline(0, color="#9a9994", lw=0.6)
    ax.set_title(title, loc="left", fontweight="bold", fontsize=10, color=INK)
    ax.set_xlabel("相对 T0 的季度（T0 = 高点后约 4 个月内最近一次财报）", color=INK2, fontsize=8)
    ax.grid(axis="y", color=GRID, lw=0.8)
    ax.set_xticks(range(-4, 5))
axs[0].legend(frameon=False, fontsize=8, loc="upper left")
fig.suptitle("逐季财报对齐：MU、SNDK 现在 vs NVDA 2025、MU 2018/2022 周期顶", x=0.01, ha="left", fontweight="bold", fontsize=11.5, color=INK)
fig.text(0.01, 0.01, "数据：各公司财报新闻稿 / 8-K（见 research/*.md 来源表）。虚线 = MU 过去两次周期顶。", fontsize=7.2, color=INK2)
fig.tight_layout(rect=(0, 0.03, 1, 0.95))
fig.savefig(HERE / "earnings_compare.png")
print("\n图：", HERE / "earnings_compare.png")
