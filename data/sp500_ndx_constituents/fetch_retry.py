#!/usr/bin/env python
"""高效补救：按失败原因分类处理，不做无意义的 404 重试。
- Errno/No such file (临时网络错误) / timestamp 异常 -> 直接重试（最多 2 次）
- 404 (退市/不存在) -> 仅查映射表用 new_symbol 重试，否则直接 missing
"""
import csv, json, sys, time, urllib.parse, urllib.request, datetime as dt
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

HERE = Path(__file__).resolve().parent
PRICES = HERE / "prices"
UA = {"User-Agent": "Mozilla/5.0 (research-lab retry3)"}
P1 = int(dt.datetime(1989, 1, 1).timestamp())


def load_mapping():
    m = {}
    with open(HERE / "ticker_changes_us.csv", encoding="utf-8-sig") as f:
        r = csv.DictReader(f)
        for row in r:
            old = (row.get("old_symbol") or "").strip()
            new = (row.get("new_symbol") or "").strip()
            if old and new and new != old:
                m[old] = new
    return m


def fetch(ticker):
    p2 = int(dt.datetime.utcnow().timestamp()) + 86400 * 2
    url = (
        f"https://query1.finance.yahoo.com/v8/finance/chart/{urllib.parse.quote(ticker)}"
        f"?period1={P1}&period2={p2}&interval=1d&events=div%2Csplits&includeAdjustedClose=true"
    )
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=25) as r:
        js = json.load(r)
    res = js["chart"]["result"][0]
    ts = res["timestamp"]
    adj = res["indicators"]["adjclose"][0]["adjclose"]
    return [(dt.datetime.utcfromtimestamp(t).date().isoformat(), round(float(a), 6))
            for t, a in zip(ts, adj) if a is not None]


def save(ticker, rows):
    safe = ticker.replace("/", "_").replace("\\", "_")
    with open(PRICES / f"{safe}.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["date", "adj_close"])
        w.writerows(rows)


def try_fetch(ticker, tries=2):
    for i in range(tries):
        try:
            rows = fetch(ticker)
            if rows:
                return rows
        except Exception:
            if i < tries - 1:
                time.sleep(0.5)
    return None


def main():
    mapping = load_mapping()
    failed = []
    with open(HERE / "fetch_failed.txt", encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if not line:
                continue
            p = line.split("\t")
            failed.append((p[0], p[1] if len(p) > 1 else ""))

    direct, mapped, missing = [], [], []
    for t, err in failed:
        is_404 = "404" in err
        if not is_404:
            # 临时网络错误 / timestamp 异常 -> 直接重试
            rows = try_fetch(t)
            if rows:
                save(t, rows)
                direct.append((t, len(rows)))
                continue
        # 404 -> 仅映射补救；非404重试失败也走映射
        target = mapping.get(t)
        if target:
            rows2 = try_fetch(target)
            if rows2:
                save(t, rows2)
                mapped.append((t, target, len(rows2)))
                continue
        missing.append((t, err))

    with open(HERE / "fetch_retried.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["type", "old_symbol", "used_symbol", "rows"])
        for t, n in direct:
            w.writerow(["direct", t, t, n])
        for t, target, n in mapped:
            w.writerow(["mapped", t, target, n])
    with open(HERE / "fetch_missing.txt", "w", encoding="utf-8") as f:
        for t, e in missing:
            f.write(f"{t}\t{e}\n")

    print("直接重试成功:", len(direct), "| 映射补救:", len(mapped), "| 仍缺失:", len(missing))
    for t, target, n in mapped:
        print("MAP", t, "->", target, n, "rows")


if __name__ == "__main__":
    main()
