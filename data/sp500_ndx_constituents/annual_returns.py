#!/usr/bin/env python
"""计算每只成分股的逐年总回报（adj_close 年末/上年末 - 1），
并识别每年「涨幅冠军」（该年年初成分股中涨幅第一的有价格股票）。
用于验证数据完整性 + 作为冠军股回测的核心中间数据。
"""
import csv
from pathlib import Path
from collections import defaultdict

HERE = Path(__file__).resolve().parent
PRICES = HERE / "prices"

def load_price(ticker):
    p = PRICES / f"{ticker}.csv"
    if not p.exists():
        return None
    d = {}
    with open(p, encoding="utf-8") as f:
        r = csv.reader(f)
        next(r)
        for row in r:
            if len(row) < 2:
                continue
            d[row[0]] = float(row[1])
    return d

def year_end(prices):
    """prices: {date: adj_close} -> {year: (last_date, last_price)}"""
    ye = {}
    for date, px in prices.items():
        y = int(date[:4])
        if y not in ye or date > ye[y][0]:
            ye[y] = (date, px)
    return {y: v[1] for y, v in ye.items()}

def annual_returns(prices):
    """-> {year: total_return} 用年末/上年末 - 1"""
    ye = year_end(prices)
    years = sorted(ye)
    ret = {}
    for i in range(1, len(years)):
        y = years[i]
        prev = years[i-1]
        if prev != y - 1:
            continue  # 中间缺年份则跳过
        if ye[prev] == 0 or ye[y] == 0:
            continue  # 价格异常(0)则跳过
        ret[y] = ye[y] / ye[prev] - 1.0
    return ret

def main():
    # 读取逐年名单
    sp_yearly = {}
    with open(HERE / "sp500_yearly_constituents.csv", encoding="utf-8") as f:
        r = csv.reader(f); next(r)
        for row in r:
            sp_yearly[int(row[0])] = [t for t in row[1].split(',') if t]

    ndx_yearly = {}
    with open(HERE / "ndx100_yearly_constituents.csv", encoding="utf-8") as f:
        r = csv.reader(f); next(r)
        for row in r:
            ndx_yearly[int(row[0])] = [t for t in row[1].split(',') if t]

    # 加载所有价格，算逐年回报
    tickers = sorted(p.stem for p in PRICES.glob("*.csv"))
    print("加载", len(tickers), "只股票价格...")
    all_ret = {}
    for t in tickers:
        px = load_price(t)
        if not px:
            continue
        all_ret[t] = annual_returns(px)

    # 输出逐年回报矩阵
    with open(HERE / "annual_returns.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        years = sorted(set(y for r in all_ret.values() for y in r))
        w.writerow(["ticker"] + years)
        for t in sorted(all_ret):
            w.writerow([t] + [round(all_ret[t].get(y, ""), 4) if y in all_ret[t] else "" for y in years])
    print("annual_returns.csv 已生成, 覆盖年份:", years[0], "->", years[-1])

    # 识别每年冠军
    print()
    print("=== 标普500 每年涨幅冠军 (有价格部分) ===")
    for y in sorted(sp_yearly):
        members = sp_yearly[y]
        # 该年冠军 = 该年年初成分股中，该年 return 最大者
        best_t, best_r = None, None
        for t in members:
            r = all_ret.get(t, {}).get(y)
            if r is not None and (best_r is None or r > best_r):
                best_t, best_r = t, r
        miss = len([t for t in members if t not in all_ret or y not in all_ret[t]])
        if best_t:
            print(f"  {y}: {best_t:6s}  +{best_r*100:7.1f}%   (缺失{miss}只)")
        else:
            print(f"  {y}: 无数据  (缺失{miss}只)")

    print()
    print("=== 纳指100 每年涨幅冠军 (有价格部分) ===")
    for y in sorted(ndx_yearly):
        members = ndx_yearly[y]
        best_t, best_r = None, None
        for t in members:
            r = all_ret.get(t, {}).get(y)
            if r is not None and (best_r is None or r > best_r):
                best_t, best_r = t, r
        miss = len([t for t in members if t not in all_ret or y not in all_ret[t]])
        if best_t:
            print(f"  {y}: {best_t:6s}  +{best_r*100:7.1f}%   (缺失{miss}只)")
        else:
            print(f"  {y}: 无数据  (缺失{miss}只)")

if __name__ == "__main__":
    main()
