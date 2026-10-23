#!/usr/bin/env python
"""Shared paths, HTTP helper and logging for the market-temperature pipeline (scripts/market_temp/).

Layout (all paths relative to the repo root):
  scripts/market_temp/        code (this package)
  data/market_temp/           rolling cache of every fetched series + manifest.json (small CSVs, committed)
  output/market_temp/<as_of>/ one dated run: temp.md, temp.json, gauges.csv, dashboard.png, needs_ai.json, ai_notes.md
  output/market_temp/history.csv   append-only log of the key readings, one row per as_of
  output/market_temp/LATEST.txt    name of the newest dated folder (read by run_market_temp.bat)
"""
import datetime as dt
import json
import sys
import time
import urllib.request
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
DATA = REPO / "data" / "market_temp"
OUT = REPO / "output" / "market_temp"
DATA.mkdir(parents=True, exist_ok=True)
OUT.mkdir(parents=True, exist_ok=True)

UA = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}

_LOG_LINES = []


def log(*parts):
    msg = " ".join(str(p) for p in parts)
    stamp = dt.datetime.now().strftime("%H:%M:%S")
    line = f"[{stamp}] {msg}"
    _LOG_LINES.append(line)
    print(line, flush=True)


def flush_log(path: Path):
    path.write_text("\n".join(_LOG_LINES) + "\n", encoding="utf-8")


def http_get(url, timeout=60, headers=None, data=None, retries=2, backoff=2.0) -> bytes:
    """GET (or POST when data is given) with browser headers, small retry, raises on final failure."""
    h = dict(UA)
    if headers:
        h.update(headers)
    last = None
    for i in range(retries + 1):
        try:
            req = urllib.request.Request(url, data=data, headers=h)
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read()
        except Exception as e:  # noqa: BLE001 - we want any network error to fall through to cache
            last = e
            if i < retries:
                time.sleep(backoff * (i + 1))
    raise last


def today_str() -> str:
    return dt.date.today().isoformat()


def utc_now() -> str:
    return dt.datetime.utcnow().isoformat(timespec="seconds")


def read_json(path: Path, default=None):
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, obj):
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False, default=_json_default), encoding="utf-8")


def _json_default(o):
    try:
        import numpy as np
        if isinstance(o, (np.integer,)):
            return int(o)
        if isinstance(o, (np.floating,)):
            return None if np.isnan(o) else float(o)
        if isinstance(o, (np.ndarray,)):
            return o.tolist()
    except Exception:
        pass
    if isinstance(o, (dt.date, dt.datetime)):
        return o.isoformat()
    if hasattr(o, "isoformat"):
        return o.isoformat()
    return str(o)
