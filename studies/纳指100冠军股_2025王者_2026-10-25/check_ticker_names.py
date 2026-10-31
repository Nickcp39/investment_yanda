"""查 ticker 复用：每只入选过前十的代码，比对「成分股名单里的历史公司名」和「Yahoo 现在这个代码对应的公司名」。
名字对不上的，Yahoo 的价格历史可能是另一家公司的。输出 ticker_name_check.csv 供人工复核。
"""
import csv
import json
import subprocess
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).resolve().parent
D = HERE.parents[1] / "data" / "sp500_ndx_constituents"

picks = {}
for r in csv.DictReader((HERE / "backtest_yearly.csv").open(encoding="utf-8-sig")):
    for p in r["picks"].split(";"):
        t = p.split(":")[0]
        picks.setdefault(t, set()).add((r["universe"], int(r["year"]) - 1))  # 记的是"选股年"

hist = {}
for f in ("sp500_historical_components_v2.csv", "ndx100_historical_components.csv"):
    for r in csv.DictReader((D / f).open(encoding="utf-8-sig")):
        hist.setdefault(r["symbol"], []).append(f"{r['name']} [{r['opt-in']}→{r['opt-out'] or '今'}]")


def yname(t):
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{t.replace('.', '-')}?range=5d&interval=1d"
    try:
        m = json.loads(subprocess.run(["curl", "-s", "-m", "30", "-A", "Mozilla/5.0", url], capture_output=True).stdout)["chart"]["result"][0]["meta"]
        return m.get("longName") or m.get("shortName") or "", m.get("firstTradeDate")
    except Exception:
        return "?", None


with ThreadPoolExecutor(8) as ex:
    names = dict(zip(picks, ex.map(yname, picks)))

rows = []
for t in sorted(picks):
    first = names[t][1]
    first_year = subprocess.run(["python", "-c", f"import datetime;print(datetime.datetime.utcfromtimestamp({first}).year)"],
                                capture_output=True, text=True).stdout.strip() if first else ""
    rows.append({"ticker": t, "pick_years": " ".join(f"{u}:{y}" for u, y in sorted(picks[t])),
                 "hist_name": " | ".join(hist.get(t, ["(名单里无名字)"])), "yahoo_name": names[t][0], "yahoo_first_trade_year": first_year})
with (HERE / "ticker_name_check.csv").open("w", newline="", encoding="utf-8-sig") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0]))
    w.writeheader()
    w.writerows(rows)
for r in rows:
    print(f"{r['ticker']:6s} 选股年 {r['pick_years']:28s} 名单：{r['hist_name'][:70]:70s} Yahoo：{r['yahoo_name'][:40]:40s} 首交易 {r['yahoo_first_trade_year']}")
