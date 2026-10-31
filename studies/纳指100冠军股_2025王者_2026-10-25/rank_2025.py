"""纳指100（QQQ）2025 全年涨幅前十：point-in-time 候选池 = 2025 年初成分股。

数据：data/sp500_ndx_constituents/（ndx100_yearly_constituents.csv + annual_returns.csv，Yahoo 复权价，含分红拆股）。
补缺：WBD、EA 在 Yahoo 的 2025 历史已被删（两者 2026 年被收购/私有化退市），用 companiesmarketcap 年度涨幅补，单独标注。
GOOG / GOOGL 同一家公司，按公司只算一次（取 GOOGL）。
运行：python rank_2025.py → 打印，写 ndx_2025_ranking.csv
"""
import csv
import json
import subprocess
import datetime as dt
from pathlib import Path

HERE = Path(__file__).resolve().parent
D = HERE.parents[1] / "data" / "sp500_ndx_constituents"
AS_OF = dt.date(2026, 10, 22)  # 成分股数据集价格的最后一天

yl = {int(r[0]): [t for t in r[1].split(",") if t] for r in list(csv.reader((D / "ndx100_yearly_constituents.csv").open(encoding="utf-8")))[1:]}
ret = {r["ticker"]: r for r in csv.DictReader((D / "annual_returns.csv").open(encoding="utf-8"))}
m25, m26 = yl[2025], yl[2026]

# 补缺（价格涨幅；WBD 不派息，EA 股息约 0.5%/年，可忽略）
MANUAL = {
    "WBD": {"2025": 1.7036, "2026": 0.0739, "note": "companiesmarketcap 年度涨幅（2026 为至 10-05 退市：被 Paramount Skydance 收购）；Motley Fool 12-15 年内读数 +173% 佐证"},
    "EA": {"2025": 0.4059, "2026": 0.0263, "note": "companiesmarketcap 年度涨幅（2026 为至 08-04 退市：PIF 等财团私有化）"},
}
NAMES = {"MU": "美光", "WBD": "华纳兄弟探索", "LRCX": "泛林", "PLTR": "Palantir", "APP": "AppLovin", "KLAC": "科磊",
         "INTC": "英特尔", "MDB": "MongoDB", "AMD": "AMD", "GOOGL": "Alphabet", "IDXX": "爱德士", "AMAT": "应用材料",
         "CEG": "Constellation Energy", "ASML": "阿斯麦", "AVGO": "博通", "WDC": "西部数据", "STX": "希捷", "INSM": "Insmed"}


def r_of(t, y):
    if t in MANUAL:
        return MANUAL[t][str(y)]
    v = ret.get(t, {}).get(str(y), "")
    return float(v) if v not in ("", None) else None


rows, missing = [], []
for t in m25:
    if t == "GOOG":
        continue
    v = r_of(t, 2025)
    if v is None:
        missing.append(t)
        continue
    rows.append({"ticker": t, "name": NAMES.get(t, ""), "ret_2025": v, "ret_2026_ytd": r_of(t, 2026),
                 "in_ndx_2026": t in m26, "source": "manual: " + MANUAL[t]["note"] if t in MANUAL else "Yahoo adj close（数据集）"})
rows.sort(key=lambda r: -r["ret_2025"])
for i, r in enumerate(rows, 1):
    r["rank"] = i


def qqq(y0, y1):
    url = ("https://query1.finance.yahoo.com/v8/finance/chart/QQQ?period1=1735084800&period2=1793664000"
           "&interval=1d&includeAdjustedClose=true&events=div")
    r = json.loads(subprocess.run(["curl", "-s", "-m", "40", "-A", "Mozilla/5.0", url], capture_output=True).stdout)["chart"]["result"][0]
    off = r["meta"]["gmtoffset"]
    s = {dt.datetime.utcfromtimestamp(ts + off).date(): a for ts, a in zip(r["timestamp"], r["indicators"]["adjclose"][0]["adjclose"]) if a}
    pick = lambda d: s[max(x for x in s if x <= d)]
    return pick(y1) / pick(y0) - 1


q25 = qqq(dt.date(2024, 12, 31), dt.date(2025, 12, 31))
q26 = qqq(dt.date(2025, 12, 31), AS_OF)
print(f"候选池：2025 年初纳指100 成分股 {len(m25)} 只（GOOG 并入 GOOGL）；无法取得 2025 全年数据：{missing}（ANSS 2025-07 被 Synopsys 收购）")
print(f"QQQ 复权总回报：2025 年 {q25:+.1%}；2026 年至 {AS_OF} {q26:+.1%}\n")
print("名次 代码   公司                   2025 全年   2026 至今   2026 年初仍在 NDX")
for r in rows[:15]:
    y26 = f"{r['ret_2026_ytd']:+8.1%}" if r["ret_2026_ytd"] is not None else "     n/a"
    flag = " *" if r["ticker"] in MANUAL else ""
    print(f"{r['rank']:3d}  {r['ticker']:6s} {r['name']:20s} {r['ret_2025']:+9.1%}  {y26}   {'是' if r['in_ndx_2026'] else '否（2025-12 调出）'}{flag}")
top10 = rows[:10]
avg25 = sum(r["ret_2025"] for r in top10) / 10
avg26 = sum(r["ret_2026_ytd"] for r in top10) / 10
beat = sum(r["ret_2026_ytd"] > q26 for r in top10)
print(f"\n前十等权：2025 年 {avg25:+.1%}（QQQ {q25:+.1%}）；2026 年至今 {avg26:+.1%}（QQQ {q26:+.1%}），10 只里 {beat} 只跑赢 QQQ")
print("* 手工补的数据（Yahoo 历史已删），来源见 CSV")

added = sorted(set(m26) - set(m25))
print("\n对照：2025 年内才加入纳指100 的（年初不在 QQQ 里，不进排名）：")
for t in added:
    v = r_of(t, 2025)
    if v is not None and v > rows[9]["ret_2025"]:
        print(f"   {t:5s} {NAMES.get(t, ''):8s} 2025 全年 {v:+.1%}")

with (HERE / "ndx_2025_ranking.csv").open("w", newline="", encoding="utf-8-sig") as fh:
    w = csv.DictWriter(fh, fieldnames=["rank", "ticker", "name", "ret_2025", "ret_2026_ytd", "in_ndx_2026", "source"])
    w.writeheader()
    for r in rows:
        w.writerow({**r, "ret_2025": round(r["ret_2025"], 4),
                    "ret_2026_ytd": round(r["ret_2026_ytd"], 4) if r["ret_2026_ytd"] is not None else ""})
print("\n写出：", HERE / "ndx_2025_ranking.csv")
