"""套息交易：利差、汇率走势、日元历次平仓、人民币套息近一年的实际损益。"""
import csv
import datetime as dt
import io
import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.dates as mdates  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.font_manager import FontProperties  # noqa: E402

D = Path(__file__).resolve().parent / "data"  # 由 fetch_carry_data.py 下载
OUT = Path(__file__).resolve().parent / "carry_trade_cny_vs_jpy.png"


def fred(sid):
    rows = list(csv.reader(io.StringIO((D / f"{sid}.csv").read_text(errors="replace"))))[1:]
    out = []
    for r in rows:
        if len(r) == 2 and r[0][:1].isdigit() and r[1] not in ("", "."):
            out.append((dt.date.fromisoformat(r[0]), float(r[1])))
    return out


def yahoo(tk):
    r = json.loads((D / f"yahoo_{tk.replace('^', 'IDX_').replace('=', '_')}.json").read_text())["chart"]["result"][0]
    off = r["meta"].get("gmtoffset", 0) or 0
    return [(dt.datetime.utcfromtimestamp(t + off).date(), c) for t, c in zip(r["timestamp"], r["indicators"]["quote"][0]["close"]) if c]


def at(series, d):
    """d 当天或之前最近的值。"""
    xs = [x for x in series if x[0] <= d]
    return xs[-1] if xs else None


jpy, cny = fred("DEXJPUS"), fred("DEXCHUS")
ff_m, ff_d = fred("FEDFUNDS"), fred("DFF")
jp_call, cn_3m, us_3m = fred("IRSTCI01JPM156N"), fred("IR3TIB01CNM156N"), fred("IR3TIB01USM156N")
jp10, us10, us2 = fred("IRLTLT01JPM156N"), fred("DGS10"), fred("DGS2")
n225 = yahoo("^N225")

print("== 最新 ==")
for name, s in (("美元/日元", jpy), ("美元/人民币", cny), ("联邦基金(日)", ff_d), ("美 2 年", us2), ("美 10 年", us10),
                ("日本隔夜(月)", jp_call), ("日本 10 年(月)", jp10), ("中国 3 月银行间(月)", cn_3m), ("美 3 月银行间(月)", us_3m)):
    print(f"{name:14s} {s[-1][0]} {s[-1][1]}")

print("\n== 人民币：近一年和近两年 ==")
last = cny[-1]
for lab, days in (("一年前", 365), ("两年前", 730), ("年初", None)):
    d0 = dt.date(last[0].year, 1, 1) if days is None else last[0] - dt.timedelta(days=days)
    p0 = at(cny, d0)
    print(f"{lab} {p0[0]} {p0[1]:.4f} → {last[0]} {last[1]:.4f}：人民币对美元 {(p0[1] / last[1] - 1) * 100:+.1f}%")
pk = max((x for x in cny if x[0] >= dt.date(2022, 1, 1)), key=lambda x: x[1])
print(f"2022 年以来人民币最弱：{pk[0]} {pk[1]:.4f}；之后升值 {(pk[1] / last[1] - 1) * 100:+.1f}%")

print("\n== 中美、日美短端利差（月度：联邦基金 − 对方短端）==")
def spread(a, b):
    mb = {(d.year, d.month): v for d, v in b}
    return [(d, v - mb[(d.year, d.month)]) for d, v in a if (d.year, d.month) in mb]
sp_cn = spread(ff_m, cn_3m)
sp_jp = spread(ff_m, jp_call)
turn = next((d for d, v in sp_cn if d >= dt.date(2015, 1, 1) and v > 0 and all(x > 0 for dd, x in sp_cn if d <= dd <= d + dt.timedelta(days=180))), None)
print("美国减中国 3 月利差：最新", sp_cn[-1], "；2015 年以来首次持续转正：", turn)
print("  年度样本：", [(f"{d:%Y-%m}", round(v, 2)) for d, v in sp_cn if d.month == 7 and d.year >= 2014])
print("美国减日本隔夜利差：最新", sp_jp[-1])
print("  年度样本：", [(f"{d:%Y-%m}", round(v, 2)) for d, v in sp_jp if d.month == 7 and d.year >= 1995])

print("\n== 近一年人民币套息的实际损益（借人民币 → 换美元 → 持有美元现金 1 年 → 换回还款）==")
d1 = last[0]
d0 = d1 - dt.timedelta(days=365)
s0, s1 = at(cny, d0)[1], last[1]
usd_r = sum(v for d, v in ff_d if d0 < d <= d1) / max(1, sum(1 for d, v in ff_d if d0 < d <= d1)) / 100
cny_r = sum(v for d, v in cn_3m if d0 <= d <= d1) / max(1, sum(1 for d, v in cn_3m if d0 <= d <= d1)) / 100
pnl = (1 + usd_r) * s1 / s0 - (1 + cny_r)
print(f"美元利息平均 {usd_r * 100:.2f}%，人民币融资（3 月银行间）平均 {cny_r * 100:.2f}%，利差 {(usd_r - cny_r) * 100:.2f} 个百分点")
print(f"汇率 {s0:.4f} → {s1:.4f}，汇兑 {(s1 / s0 - 1) * 100:+.2f}%；合计损益约 {pnl * 100:+.2f}%（按借入本金计，未计杠杆和交易成本）")

print("\n== 日元历次平仓（美联储 H.10 日度；日元升值 = 美元/日元下跌）==")
eps = [("1998 LTCM/俄罗斯", "1998-06-01", "1998-12-31"), ("2007–08 次贷/金融危机", "2007-01-01", "2009-03-31"),
       ("2024 年 8 月", "2024-06-01", "2024-09-30")]
for name, a, b in eps:
    w = [x for x in jpy if a <= x[0].isoformat() <= b]
    hi = max(w, key=lambda x: x[1])
    lo = min((x for x in w if x[0] > hi[0]), key=lambda x: x[1])
    print(f"{name}：{hi[0]} {hi[1]:.2f} → {lo[0]} {lo[1]:.2f}，日元升值 {(hi[1] / lo[1] - 1) * 100:.1f}%，用时 {(lo[0] - hi[0]).days} 天")
# 1998 年 10 月最快的一周
w = [x for x in jpy if "1998-10-01" <= x[0].isoformat() <= "1998-10-15"]
print("  1998-10 上旬逐日：", [(f"{d:%m-%d}", v) for d, v in w])
w = [x for x in n225 if "2024-07-31" <= x[0].isoformat() <= "2024-08-07"]
print("  日经 2024-07-31 至 08-07：", [(f"{d:%m-%d}", round(v)) for d, v in w])
prev = [x for x in n225 if x[0] < dt.date(2024, 8, 5)][-1]
day = [x for x in n225 if x[0] == dt.date(2024, 8, 5)][0]
print(f"  日经 2024-08-05 单日 {(day[1] / prev[1] - 1) * 100:+.1f}%")

# ---------- 图
font = FontProperties(fname="C:/Windows/Fonts/msyh.ttc")
plt.rcParams.update({"font.family": font.get_name(), "axes.unicode_minus": False, "font.size": 9,
                     "axes.spines.top": False, "axes.spines.right": False, "savefig.dpi": 160})
fig, ax = plt.subplots(3, 1, figsize=(10.5, 10), gridspec_kw={"height_ratios": [1, 1.1, 1]})
a = ax[0]
s1_ = [x for x in sp_jp if x[0] >= dt.date(1995, 1, 1)]
s2_ = [x for x in sp_cn if x[0] >= dt.date(1997, 6, 1)]
a.plot([d for d, _ in s1_], [v for _, v in s1_], color="#b9484a", lw=1.5, label="美国 − 日本（联邦基金 − 日本隔夜利率）")
a.plot([d for d, _ in s2_], [v for _, v in s2_], color="#235e7c", lw=1.5, label="美国 − 中国（联邦基金 − 中国 3 个月银行间）")
a.axhline(0, color="#555", lw=0.8)
a.set_ylabel("百分点")
a.set_title("① 借低息货币、买美元的利差：大于 0 才有套息的动机", loc="left", fontweight="bold", fontsize=10)
a.legend(fontsize=8, frameon=False, loc="lower left")
a = ax[1]
j = [x for x in jpy if x[0] >= dt.date(1995, 1, 1)]
a.plot([d for d, _ in j], [v for _, v in j], color="#b9484a", lw=1.0)
for name, s, e in (("1998", "1998-08-11", "1998-10-08"), ("2007–08", "2007-06-22", "2008-12-17"), ("2024", "2024-07-10", "2024-08-05")):
    a.axvspan(dt.date.fromisoformat(s), dt.date.fromisoformat(e), color="#b9484a", alpha=0.15, lw=0)
a.set_ylabel("日元/美元（越高日元越弱）")
a.set_title("② 日元套息：日元一路走弱时赚钱，平仓时日元急升（阴影 = 三次平仓）", loc="left", fontweight="bold", fontsize=10)
a = ax[2]
c = [x for x in cny if x[0] >= dt.date(2015, 1, 1)]
a.plot([d for d, _ in c], [v for _, v in c], color="#235e7c", lw=1.0)
a.set_ylabel("人民币/美元（越高人民币越弱）")
a.annotate(f"{last[0]:%Y-%m-%d} {last[1]:.2f}", (last[0], last[1]), xytext=(-110, -18), textcoords="offset points", fontsize=8)
a.annotate(f"{pk[0]:%Y-%m} {pk[1]:.2f}", (pk[0], pk[1]), xytext=(-60, 8), textcoords="offset points", fontsize=8)
a.set_title("③ 人民币：2022 年后利差转正，但人民币近一年在升值，借人民币换美元是亏的", loc="left", fontweight="bold", fontsize=10)
for x in ax:
    x.grid(alpha=0.25)
    x.xaxis.set_major_locator(mdates.YearLocator(5 if x is not ax[2] else 1))
    x.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
fig.suptitle("套息交易：日元当年 vs 人民币现在", x=0.01, ha="left", fontweight="bold", fontsize=12)
fig.text(0.01, 0.005, "来源：FRED（DEXJPUS、DEXCHUS、FEDFUNDS，OECD IRSTCI01JPM156N、IR3TIB01CNM156N），截至 2026-10。OECD 月度利率有 2–3 个月滞后。",
         fontsize=7, color="#666")
fig.tight_layout(rect=(0, 0.015, 1, 0.97))
fig.savefig(OUT)
print("\n图：", OUT)

