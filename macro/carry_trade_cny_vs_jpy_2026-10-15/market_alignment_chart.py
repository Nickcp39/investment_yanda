"""按房价顶点对齐的市场指标图：读 markets/aligned_table.csv（日本 T0=1991，中国 T0=2021，年末值）。"""
import csv
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.font_manager import FontProperties  # noqa: E402

HERE = Path(__file__).resolve().parent
rows = list(csv.DictReader((HERE / "markets" / "aligned_table.csv").open(encoding="utf-8-sig")))


def num(s):
    s = (s or "").replace("*", "").split("(")[0].strip()
    try:
        return float(s)
    except ValueError:
        return None


T = [int(r["T"]) for r in rows]
series = [
    ("10 年期国债收益率 %", "日10Y年末%", "中10Y年末%"),
    ("住宅价格 / 顶点（BIS 名义）", "日本住宅价(BIS Q4)/顶", "中国住宅价(BIS Q4)/顶"),
    ("股市 / 顶点（日经对 1989 顶；中国为沪深 300 对 2021 顶）", "日经年末/1989顶", "沪深300年末/2021顶"),
    ("CPI 涨幅 %", "日本CPI%", "中国CPI%"),
]
font = FontProperties(fname="C:/Windows/Fonts/msyh.ttc")
plt.rcParams.update({"font.family": font.get_name(), "axes.unicode_minus": False, "font.size": 8.5,
                     "axes.spines.top": False, "axes.spines.right": False, "savefig.dpi": 160})
fig, axs = plt.subplots(2, 2, figsize=(10.5, 6.4))
for ax, (title, jk, ck) in zip(axs.flat, series):
    jx = [(t, num(r[jk])) for t, r in zip(T, rows) if num(r[jk]) is not None]
    cx = [(t, num(r[ck])) for t, r in zip(T, rows) if num(r.get(ck)) is not None]
    ax.plot([t for t, _ in jx], [v for _, v in jx], "-o", ms=3, color="#b9484a", lw=1.6, label="日本（T0 = 1991）")
    ax.plot([t for t, _ in cx], [v for _, v in cx], "-o", ms=3, color="#235e7c", lw=1.6, label="中国（T0 = 2021）")
    if "CPI" in title:
        ax.axhline(0, color="#555", lw=0.7)
    ax.set_title(title, loc="left", fontweight="bold", fontsize=9.5)
    ax.set_xlabel("距房价顶点的年数（年末值）")
    ax.grid(alpha=0.25)
axs[0][0].legend(fontsize=8, frameon=False)
fig.suptitle("以房价顶点对齐的市场指标：中国的利率比日本当年降得更快", x=0.01, ha="left", fontweight="bold", fontsize=11)
fig.text(0.01, 0.004, "数据：markets/aligned_table.csv（FRED/OECD、BIS、Yahoo、中国债券信息网、国家统计局，见 markets/japan_post_bubble_markets.md）。中国 2026 年为最新值，非年末。",
         fontsize=7, color="#666")
fig.tight_layout(rect=(0, 0.02, 1, 0.95))
fig.savefig(HERE / "market_alignment.png")
print(HERE / "market_alignment.png")
