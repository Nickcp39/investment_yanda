"""回测前的数据盘点：逐年成分股名单覆盖多少年、每年有多少成分股有回报数据、基准 ETF 从哪年开始。"""
import csv
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
D = ROOT / "data" / "sp500_ndx_constituents"
MT = ROOT / "data" / "market_temp"

ret = {r["ticker"]: r for r in csv.DictReader((D / "annual_returns.csv").open(encoding="utf-8"))}
for name, f in [("标普500", "sp500_yearly_constituents.csv"), ("纳指100", "ndx100_yearly_constituents.csv")]:
    yl = {int(r[0]): [t for t in r[1].split(",") if t] for r in list(csv.reader((D / f).open(encoding="utf-8")))[1:]}
    print(f"\n=== {name} 逐年名单：{min(yl)}–{max(yl)}，共 {len(yl)} 年 ===")
    print("年份  成分股  当年有回报  覆盖率   |  下一年有回报（持有年）")
    for y in sorted(yl):
        m = yl[y]
        have = sum(1 for t in m if ret.get(t, {}).get(str(y), "") != "")
        nxt = sum(1 for t in m if ret.get(t, {}).get(str(y + 1), "") != "")
        print(f"{y}  {len(m):5d}  {have:8d}  {have / len(m):6.0%}   |  {nxt:5d}")

print("\n=== 基准数据 ===")
for f in sorted(MT.glob("*_daily.csv")):
    lines = f.read_text(encoding="utf-8").strip().splitlines()
    print(f"{f.name:22s} {lines[0][:60]:60s} {lines[1].split(',')[0]} → {lines[-1].split(',')[0]}  ({len(lines) - 1} 行)")
