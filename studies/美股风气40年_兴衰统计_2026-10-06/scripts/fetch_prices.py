#!/usr/bin/env python3
"""fetch_prices.py — 美股风气40年：抓取指数 / 主题 ETF / 个股价格 + FRED 宏观序列（只补缺，不覆盖）。

价格源：Yahoo chart API（period1=0 拿完整历史），全部用日线（周线会漏掉妖股的单日尖峰，
如 BlackBerry 2021-01-27 收盘 $25.10，而当周周五收盘约 $14 —— 2026-10-06 实测后改为日线）。
每个序列存成紧凑的 data/raw/prices/<ticker>.csv.gz（date, close, adjclose），原始响应的 sha256、
抓取时间、Yahoo meta（币种、上市日、证券类型、名称）写入 data/raw/prices/manifest.json。
FRED：fredgraph.csv 原文保存到 data/raw/fred/<id>.csv。

已存在的文件不重抓（避免把本快照悄悄变成另一天的数据）。要研究新的截止日，请另建日期目录。
用法：
    python scripts/fetch_prices.py               # 指数 + ETF + FRED
    python scripts/fetch_prices.py --companies   # 另外抓 data/research/*.json 里所有 yahoo_ticker
"""
from __future__ import annotations

import csv
import datetime as dt
import gzip
import hashlib
import io
import json
import subprocess
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
PX = BASE / "data/raw/prices"
FRED = BASE / "data/raw/fred"
AS_OF = "2026-10-05"  # 最后一个完整交易日（研究日 2026-10-06）
PERIOD2 = int(dt.datetime(2026, 10, 6, tzinfo=dt.timezone.utc).timestamp())
UA = {"User-Agent": "Mozilla/5.0"}

INDICES = {"^IXIC": "纳斯达克综合指数", "^GSPC": "标普500（价格指数）", "^NDX": "纳斯达克100"}
ETFS = {  # 主题代理 ETF（注意：大多晚于主题本身才发行）
    "QQQ": "纳指100 ETF", "SPY": "标普500 ETF", "ARKK": "ARK 颠覆创新", "ICLN": "全球清洁能源",
    "TAN": "太阳能", "MJ": "大麻", "XBI": "生物科技（等权）", "IBB": "生物科技（市值）", "SOXX": "半导体",
    "IGV": "软件", "FDN": "互联网", "SKYY": "云计算", "WCLD": "云计算（等权）", "XHB": "住宅建筑",
    "KBE": "银行", "XME": "金属与采矿", "URA": "铀/核能", "LIT": "锂电", "KWEB": "中概互联网",
    "BLOK": "区块链", "IPO": "新股 IPO", "ROBO": "机器人", "HACK": "网络安全", "XLE": "能源", "GDX": "金矿",
}
FRED_IDS = {"FEDFUNDS": "联邦基金有效利率（月）", "ECOMPCTSA": "美国电商占零售比（季，季调）",
            "M2SL": "M2 货币供应（月）", "DGS10": "10 年期美债收益率（日）"}


def get(url: str) -> bytes:
    err = None
    for i in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
                return r.read()
        except Exception as e:  # noqa: BLE001
            err = e
            time.sleep(2 * (i + 1))
    raise RuntimeError(f"{url}: {err}")


def load_manifest() -> dict:
    p = PX / "manifest.json"
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}


def save_manifest(m: dict) -> None:
    # 先写临时文件再替换；Windows 上文件偶尔被其他进程占用（2026-10-06 实测 Errno 22），重试
    tmp = PX / "manifest.json.tmp"
    tmp.write_text(json.dumps(m, ensure_ascii=False, indent=1, sort_keys=True), encoding="utf-8")
    for i in range(10):
        try:
            tmp.replace(PX / "manifest.json")
            return
        except OSError:
            time.sleep(1 + i)
    raise RuntimeError("manifest.json 无法写入")


def fname(tk: str) -> Path:
    return PX / (tk.replace("^", "IDX_").replace("/", "_").replace("=", "_") + ".csv.gz")


def fetch_yahoo(tk: str, interval: str, manifest: dict) -> str:
    out = fname(tk)
    if out.exists() and manifest.get(tk, {}).get("interval") == interval:
        return "cached"
    url = (f"https://query1.finance.yahoo.com/v8/finance/chart/{urllib.parse.quote(tk)}"
           f"?period1=0&period2={PERIOD2}&interval={interval}&events=div%7Csplit&includeAdjustedClose=true")
    try:
        raw = get(url)
        res = json.loads(raw)["chart"]
        if res.get("error") or not res.get("result"):
            manifest[tk] = {"status": "error", "url": url, "error": str(res.get("error"))[:300],
                            "fetched_utc": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")}
            return "error"
        r = res["result"][0]
        meta = r["meta"]
        off = meta.get("gmtoffset", 0) or 0  # 用交易所本地日期（memory: Yahoo 时间戳为本地午夜）
        q = r["indicators"]["quote"][0]
        adj = (r["indicators"].get("adjclose") or [{}])[0].get("adjclose") or q["close"]
        rows = []
        for t, c, a in zip(r.get("timestamp") or [], q["close"], adj):
            if c is None:
                continue
            d = dt.datetime.fromtimestamp(t + off, dt.timezone.utc).date()
            if d > dt.date.fromisoformat(AS_OF):
                continue
            rows.append((d.isoformat(), round(c, 6), round(a if a is not None else c, 6)))
        buf = io.StringIO()
        w = csv.writer(buf)
        w.writerow(["date", "close", "adjclose"])
        w.writerows(rows)
        out.write_bytes(gzip.compress(buf.getvalue().encode()))
        manifest[tk] = {
            "status": "ok" if rows else "empty", "url": url, "interval": interval, "rows": len(rows),
            "first": rows[0][0] if rows else None, "last": rows[-1][0] if rows else None,
            "sha256_raw": hashlib.sha256(raw).hexdigest(),
            "fetched_utc": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
            "currency": meta.get("currency"), "instrumentType": meta.get("instrumentType"),
            "longName": meta.get("longName") or meta.get("shortName"), "exchange": meta.get("fullExchangeName"),
            "firstTradeDate": meta.get("firstTradeDate"),
            "splits": sorted((dt.datetime.utcfromtimestamp(int(k)).date().isoformat(),
                              f'{v["numerator"]}:{v["denominator"]}')
                             for k, v in ((r.get("events") or {}).get("splits") or {}).items()),
        }
        return manifest[tk]["status"]
    except Exception as e:  # noqa: BLE001
        manifest[tk] = {"status": "error", "url": url, "error": str(e)[:300],
                        "fetched_utc": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")}
        return "error"


def fetch_fred(sid: str) -> str:
    out = FRED / f"{sid}.csv"
    if out.exists():
        return "cached"
    # FRED 对 Python urllib 会挂起（2026-10-06 实测），curl 正常 → 用 curl
    raw = subprocess.run(["curl", "-s", "-m", "60", f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={sid}"],
                         capture_output=True, check=True).stdout
    if not raw.startswith(b"observation_date") and not raw.startswith(b"DATE"):
        return "error"
    out.write_bytes(raw)
    return "ok"


def company_tickers() -> list[str]:
    tks = set()
    for p in sorted((BASE / "data/research").glob("e*.json")):
        d = json.loads(p.read_text(encoding="utf-8"))
        for th in d.get("themes", []):
            tks.update(t for t in th.get("proxy_tickers") or [] if t)
            tks.update(c["yahoo_ticker"] for c in th.get("companies", []) if c.get("yahoo_ticker"))
    return sorted(tks)


def main() -> None:
    PX.mkdir(parents=True, exist_ok=True)
    FRED.mkdir(parents=True, exist_ok=True)
    m = load_manifest()
    jobs = [(t, "1d") for t in INDICES] + [(t, "1d") for t in ETFS]
    if "--companies" in sys.argv:
        jobs += [(t, "1d") for t in company_tickers() if t not in INDICES and t not in ETFS]
    for tk, iv in jobs:
        st = fetch_yahoo(tk, iv, m)
        print(f"{tk:12s} {iv:4s} {st:7s} {m.get(tk, {}).get('first')} → {m.get(tk, {}).get('last')}  {m.get(tk, {}).get('longName') or ''}")
        save_manifest(m)
        if st != "cached":
            time.sleep(0.4)
    for sid in FRED_IDS:
        print(sid, fetch_fred(sid))


if __name__ == "__main__":
    main()
