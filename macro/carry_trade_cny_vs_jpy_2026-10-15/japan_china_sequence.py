"""日本 1980–2000 vs 中国 2003–2026：本币升值、利率、房价、股市的先后顺序（回答“错位”问题）。

数据：FRED（DEXJPUS、DEXCHUS 美联储 H.10；INTDSRJPM193N 日本贴现率；IR3TIB01CNM156N 中国 3 个月银行间；
QJPN628BIS、QCNN628BIS 为 BIS 名义住宅价格），Yahoo（^N225 日经、000001.SS 上证综指）。
下载到 data/（已有文件不重下）。运行：python japan_china_sequence.py
"""
import csv
import datetime as dt
import io
import json
import subprocess
import urllib.request
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.dates as mdates  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.font_manager import FontProperties  # noqa: E402

HERE = Path(__file__).resolve().parent
D = HERE / "data"


def fred(sid):
    f = D / f"{sid}.csv"
    if not f.exists() or f.stat().st_size < 200:
        f.write_bytes(subprocess.run(["curl", "-s", "-m", "90", f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={sid}"],
                                     capture_output=True).stdout)
    out = []
    for r in csv.reader(io.StringIO(f.read_text(errors="replace"))):
        if len(r) == 2 and r[0][:1].isdigit() and r[1] not in ("", "."):
            out.append((dt.date.fromisoformat(r[0]), float(r[1])))
    return out


def yahoo(tk):
    f = D / f"yahoo_{tk.replace('^', 'IDX_').replace('=', '_')}.json"
    if not f.exists():
        url = f"https://query1.finance.yahoo.com/v8/finance/chart/{tk.replace('^', '%5E')}?period1=0&period2=9999999999&interval=1d"
        f.write_bytes(urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=60).read())
    r = json.loads(f.read_text())["chart"]["result"][0]
    off = r["meta"].get("gmtoffset", 0) or 0
    return [(dt.datetime.utcfromtimestamp(t + off).date(), c) for t, c in zip(r["timestamp"], r["indicators"]["quote"][0]["close"]) if c]


def ext(s, a, b, f=max):
    w = [x for x in s if a <= x[0].isoformat() <= b]
    return f(w, key=lambda x: x[1])


def at(s, d):
    return [x for x in s if x[0] <= dt.date.fromisoformat(d)][-1]


jpy, cny = fred("DEXJPUS"), fred("DEXCHUS")
jp_disc, cn_3m = fred("INTDSRJPM193N"), fred("IR3TIB01CNM156N")
jp_house, cn_house = fred("QJPN628BIS"), fred("QCNN628BIS")
n225, ssec = yahoo("^N225"), yahoo("000001.SS")

print("== 日本 ==")
a = ext(jpy, "1985-01-01", "1985-09-20")
p = at(jpy, "1985-09-20")
b = ext(jpy, "1986-01-01", "1988-12-31", min)
print(f"日元：1985 年最弱 {a[0]} {a[1]:.2f}；广场协议前一天 {p[0]} {p[1]:.2f} → {b[0]} {b[1]:.2f}，日元对美元升值 {(a[1] / b[1] - 1) * 100:.0f}%（从广场协议起 {(p[1] / b[1] - 1) * 100:.0f}%）")
c = ext(jpy, "1989-06-01", "1990-12-31")
e = ext(jpy, "1993-01-01", "1995-12-31", min)
print(f"泡沫破裂后：{c[0]} {c[1]:.2f} → {e[0]} {e[1]:.2f}，日元再升值 {(c[1] / e[1] - 1) * 100:.0f}%")
f_ = ext(jpy, "1995-05-01", "1998-12-31")
print(f"1995 年后转弱：{e[0]} {e[1]:.2f} → {f_[0]} {f_[1]:.2f}，日元贬值 {(1 - e[1] / f_[1]) * 100:.0f}%（套息交易时期）")
print("日本贴现率：", [(f"{d:%Y-%m}", v) for d, v in jp_disc if dt.date(1985, 1, 1) <= d <= dt.date(1996, 1, 1) and
                      (d.month in (1, 7) or v != [x for x in jp_disc if x[0] < d][-1][1])])
pk = ext(n225, "1985-01-01", "1995-12-31")
lo = ext(n225, "1990-01-01", "1995-12-31", min)
s85 = at(n225, "1985-09-20")
print(f"日经：广场协议时 {s85[1]:,.0f} → {pk[0]} {pk[1]:,.2f}（{pk[1] / s85[1]:.1f} 倍）→ {lo[0]} {lo[1]:,.0f}（{(lo[1] / pk[1] - 1) * 100:.0f}%）")
hp = ext(jp_house, "1980-01-01", "2000-12-31")
h85 = at(jp_house, "1985-07-01")
h95 = at(jp_house, "1995-07-01")
print(f"日本住宅价格（BIS 名义）：1985Q3 {h85[1]:.1f} → 峰值 {hp[0]} {hp[1]:.1f}（{(hp[1] / h85[1] - 1) * 100:+.0f}%）；1995 年 {h95[1]:.1f}（较峰值 {(h95[1] / hp[1] - 1) * 100:+.0f}%）")

print("\n== 中国 ==")
r0 = at(cny, "2005-07-20")
r1 = ext(cny, "2013-01-01", "2014-12-31", min)
print(f"人民币：汇改前 {r0[0]} {r0[1]:.4f} → {r1[0]} {r1[1]:.4f}，对美元升值 {(r0[1] / r1[1] - 1) * 100:.0f}%，用时 {(r1[0] - r0[0]).days / 365.25:.1f} 年")
r2 = ext(cny, "2015-01-01", "2016-12-31")
r3 = ext(cny, "2022-01-01", "2025-12-31")
r4 = cny[-1]
print(f"之后转弱：{r2[0]} {r2[1]:.4f}；{r3[0]} {r3[1]:.4f}（较 2014 年最强贬值 {(1 - r1[1] / r3[1]) * 100:.0f}%）；现在 {r4[0]} {r4[1]:.4f}（较 2025-04 升值 {(r3[1] / r4[1] - 1) * 100:.1f}%）")
s0 = at(ssec, "2005-07-20")
sp = ext(ssec, "2005-01-01", "2008-12-31")
sl = ext(ssec, "2008-01-01", "2008-12-31", min)
sp2 = ext(ssec, "2015-01-01", "2015-12-31")
print(f"上证：汇改时 {s0[1]:,.0f} → {sp[0]} {sp[1]:,.0f}（{sp[1] / s0[1]:.1f} 倍）→ {sl[0]} {sl[1]:,.0f}（{(sl[1] / sp[1] - 1) * 100:.0f}%）；2015 年高点 {sp2[0]} {sp2[1]:,.0f}；最新 {ssec[-1][0]} {ssec[-1][1]:,.0f}")
cp = ext(cn_house, "2005-01-01", "2026-12-31")
print(f"中国住宅价格（BIS 名义）：{cn_house[0][0]} {cn_house[0][1]:.1f} → 峰值 {cp[0]} {cp[1]:.1f} → 最新 {cn_house[-1][0]} {cn_house[-1][1]:.1f}（较峰值 {(cn_house[-1][1] / cp[1] - 1) * 100:+.0f}%）")
print("中国 3 个月银行间利率：", [(f"{d:%Y-%m}", v) for d, v in cn_3m if d.month == 7 and d.year in (2007, 2011, 2014, 2017, 2019, 2021, 2023, 2024, 2025, 2026)])

# ---------- 图：左日本 1980–2000，右中国 2003–2026；上本币强弱，中房价/股市，下利率
font = FontProperties(fname="C:/Windows/Fonts/msyh.ttc")
plt.rcParams.update({"font.family": font.get_name(), "axes.unicode_minus": False, "font.size": 8.5,
                     "axes.spines.top": False, "axes.spines.right": False, "savefig.dpi": 160})
fig, ax = plt.subplots(3, 2, figsize=(11.5, 9.2), sharex="col")
J0, J1 = dt.date(1980, 1, 1), dt.date(2000, 12, 31)
C0, C1 = dt.date(2003, 1, 1), dt.date(2026, 12, 31)


def sub(s, a, b):
    return [x for x in s if a <= x[0] <= b]


# 本币强弱：取倒数（每单位本币值多少美分），越高本币越强
for col, (s, a_, b_, unit, title) in enumerate(((jpy, J0, J1, 100, "日元：每 100 日元值多少美元（越高日元越强）"),
                                                 (cny, C0, C1, 1, "人民币：每 1 元值多少美元（越高人民币越强）"))):
    w = sub(s, a_, b_)
    ax[0][col].plot([d for d, _ in w], [unit / v for _, v in w], color="#b9484a" if col == 0 else "#235e7c", lw=1.1)
    ax[0][col].set_title(title, loc="left", fontweight="bold", fontsize=9.5)
# 房价 + 股市（各自以区间首值=100）
for col, (house, stock, a_, b_, sname) in enumerate(((jp_house, n225, J0, J1, "日经 225"), (cn_house, ssec, C0, C1, "上证综指"))):
    h = sub(house, a_, b_)
    st = sub(stock, a_, b_)
    ax[1][col].plot([d for d, _ in h], [v / h[0][1] * 100 for _, v in h], color="#d28a36", lw=1.6, label="住宅价格（BIS 名义）")
    ax[1][col].plot([d for d, _ in st], [v / st[0][1] * 100 for _, v in st], color="#8c698d", lw=0.9, label=sname)
    ax[1][col].set_yscale("log")
    ax[1][col].legend(fontsize=7.5, frameon=False, loc="upper left")
    ax[1][col].set_title("房价与股市（区间起点 = 100，对数）", loc="left", fontweight="bold", fontsize=9.5)
w = sub(jp_disc, J0, J1)
ax[2][0].step([d for d, _ in w], [v for _, v in w], where="post", color="#555", lw=1.3)
ax[2][0].set_title("日本央行贴现率 %", loc="left", fontweight="bold", fontsize=9.5)
w = sub(cn_3m, C0, C1)
ax[2][1].plot([d for d, _ in w], [v for _, v in w], color="#555", lw=1.3)
ax[2][1].set_title("中国 3 个月银行间利率 %（OECD 月度）", loc="left", fontweight="bold", fontsize=9.5)
# 阶段标注
for x in ax[:, 0]:
    for s_, e_, c in (("1985-09-22", "1988-11-30", "#b9484a"), ("1990-04-01", "1995-04-19", "#b9484a"), ("1995-04-19", "1998-08-11", "#235e7c")):
        x.axvspan(dt.date.fromisoformat(s_), dt.date.fromisoformat(e_), color=c, alpha=0.08, lw=0)
    x.axvline(dt.date(1989, 12, 29), color="#999", lw=0.8, ls="--")
for x in ax[:, 1]:
    for s_, e_, c in (("2005-07-21", "2014-01-14", "#b9484a"), ("2025-04-09", "2026-10-09", "#b9484a"), ("2022-01-01", "2025-04-09", "#235e7c")):
        x.axvspan(dt.date.fromisoformat(s_), dt.date.fromisoformat(e_), color=c, alpha=0.08, lw=0)
    x.axvline(cp[0], color="#999", lw=0.8, ls="--")
ax[0][0].text(dt.date(1986, 1, 1), ax[0][0].get_ylim()[1] * 0.97, "广场协议后升值", fontsize=7.5, color="#8a2f31", va="top")
ax[0][0].text(dt.date(1991, 1, 1), ax[0][0].get_ylim()[1] * 0.97, "泡沫破裂后再升值", fontsize=7.5, color="#8a2f31", va="top")
ax[0][0].text(dt.date(1995, 9, 1), ax[0][0].get_ylim()[1] * 0.97, "转贬：套息期", fontsize=7.5, color="#235e7c", va="top")
ax[0][1].text(dt.date(2006, 1, 1), ax[0][1].get_ylim()[1] * 0.99, "汇改后缓慢升值", fontsize=7.5, color="#8a2f31", va="top")
ax[0][1].text(dt.date(2022, 2, 1), ax[0][1].get_ylim()[1] * 0.99, "贬值", fontsize=7.5, color="#235e7c", va="top")
ax[0][1].text(dt.date(2025, 5, 1), ax[0][1].get_ylim()[1] * 0.93, "再升值", fontsize=7.5, color="#8a2f31", va="top")
for x in ax.flat:
    x.grid(alpha=0.25)
ax[2][0].xaxis.set_major_locator(mdates.YearLocator(2))
ax[2][1].xaxis.set_major_locator(mdates.YearLocator(2))
for x in (ax[2][0], ax[2][1]):
    x.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
fig.suptitle("日本 1980–2000 vs 中国 2003–2026：本币升值、利率、房价、股市的先后（虚线 = 日经顶点 / 中国房价顶点）",
             x=0.01, ha="left", fontweight="bold", fontsize=11)
fig.text(0.01, 0.004, "来源：FRED（DEXJPUS、DEXCHUS、INTDSRJPM193N、IR3TIB01CNM156N、BIS 住宅价格 QJPN628BIS / QCNN628BIS），Yahoo（^N225、000001.SS）。红色底 = 本币升值期，蓝色底 = 贬值期。",
         fontsize=7, color="#666")
fig.tight_layout(rect=(0, 0.015, 1, 0.97))
out = HERE / "japan_vs_china_sequence.png"
fig.savefig(out)
print("\n图：", out)
