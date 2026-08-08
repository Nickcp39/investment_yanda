#!/usr/bin/env python
"""Pull the three raw series needed for the gold-vs-money valuation test.

Sources (all free, no API key):
  1. LBMA Gold Price PM fix, daily USD/oz, from 1968-04-01
     https://prices.lbma.org.uk/json/gold_pm.json
  2. US M2 money stock, monthly, seasonally adjusted, USD billions, from 1959-01
     Federal Reserve H.6 statistical release, Data Download Program
  3. US CPI-U (all items, US city average, NSA), monthly, from 1968
     BLS public API v1 (10-year chunks, no key required)

Outputs (data/):
  gold_lbma_pm_daily.csv   date,gold_usd_per_oz
  us_m2_monthly.csv        month,m2_sa_usd_bn,m2_nsa_usd_bn
  us_cpi_monthly.csv       month,cpi_u_nsa
  source_manifest.json     URLs, row counts, coverage, fetch timestamp

Re-run: python fetch_data.py
"""
from __future__ import annotations

import csv
import datetime as dt
import io
import json
import sys
import urllib.request
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
DATA.mkdir(parents=True, exist_ok=True)

UA = {"User-Agent": "Mozilla/5.0 (research-lab gold-vs-money)"}

LBMA_URL = "https://prices.lbma.org.uk/json/gold_pm.json"
H6_URL = (
    "https://www.federalreserve.gov/datadownload/Output.aspx"
    "?rel=H6&series=798e2796917702a5f8423426ba7e6b42"
    "&from=&to=&filetype=csv&label=include&layout=seriescolumn"
)
BLS_URL = "https://api.bls.gov/publicAPI/v1/timeseries/data/"
CPI_SERIES = "CUUR0000SA0"  # CPI-U, all items, US city average, not seasonally adjusted


def get(url: str, data: bytes | None = None, headers: dict | None = None) -> bytes:
    req = urllib.request.Request(url, data=data, headers={**UA, **(headers or {})})
    with urllib.request.urlopen(req, timeout=90) as resp:
        return resp.read()


# --------------------------------------------------------------------------- gold
def fetch_gold() -> list[tuple[str, float]]:
    raw = json.loads(get(LBMA_URL).decode("utf-8"))
    rows: list[tuple[str, float]] = []
    for item in raw:
        values = item.get("v") or []
        usd = values[0] if values else None
        if usd is None:
            continue
        rows.append((item["d"], float(usd)))
    rows.sort()
    return rows


# ----------------------------------------------------------------------------- m2
def fetch_m2() -> list[tuple[str, float, float]]:
    text = get(H6_URL).decode("utf-8-sig")
    reader = list(csv.reader(io.StringIO(text)))
    header_idx = next(i for i, r in enumerate(reader) if r and r[0] == "Time Period")
    header = reader[header_idx]
    i_sa = header.index("M2.M")       # seasonally adjusted
    i_nsa = header.index("M2_N.M")    # not seasonally adjusted

    rows: list[tuple[str, float, float]] = []
    for r in reader[header_idx + 1:]:
        if not r or not r[0] or len(r[0]) != 7:
            continue
        sa, nsa = r[i_sa].strip(), r[i_nsa].strip()
        if not sa:
            continue
        rows.append((r[0], float(sa), float(nsa) if nsa else float("nan")))
    rows.sort()
    return rows


# ---------------------------------------------------------------------------- cpi
def fetch_cpi(start_year: int, end_year: int) -> list[tuple[str, float]]:
    """BLS v1 allows at most 10 calendar years per request and no API key."""
    out: dict[str, float] = {}
    year = start_year
    while year <= end_year:
        chunk_end = min(year + 9, end_year)
        payload = json.dumps({
            "seriesid": [CPI_SERIES],
            "startyear": str(year),
            "endyear": str(chunk_end),
        }).encode("utf-8")
        body = json.loads(get(BLS_URL, data=payload,
                              headers={"Content-Type": "application/json"}).decode("utf-8"))
        if body.get("status") != "REQUEST_SUCCEEDED":
            raise RuntimeError(f"BLS {year}-{chunk_end} failed: {body.get('message')}")
        for series in body["Results"]["series"]:
            for obs in series["data"]:
                if not obs["period"].startswith("M") or obs["period"] == "M13":
                    continue
                try:
                    value = float(obs["value"])
                except ValueError:
                    continue  # BLS returns "-" for months not yet published
                out[f"{obs['year']}-{obs['period'][1:]}"] = value
        print(f"  CPI {year}-{chunk_end}: {len(out)} months cumulative")
        year = chunk_end + 1
    return sorted(out.items())


def write_csv(path: Path, header: list[str], rows) -> None:
    with path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(header)
        w.writerows(rows)


def main() -> int:
    print("1/3 LBMA gold PM fix ...")
    gold = fetch_gold()
    write_csv(DATA / "gold_lbma_pm_daily.csv", ["date", "gold_usd_per_oz"], gold)
    print(f"    {len(gold):,} daily fixes, {gold[0][0]} -> {gold[-1][0]}")

    print("2/3 Federal Reserve H.6 M2 ...")
    m2 = fetch_m2()
    write_csv(DATA / "us_m2_monthly.csv",
              ["month", "m2_sa_usd_bn", "m2_nsa_usd_bn"], m2)
    print(f"    {len(m2):,} months, {m2[0][0]} -> {m2[-1][0]}, latest SA = ${m2[-1][1]:,.1f}bn")

    print("3/3 BLS CPI-U ...")
    cpi = fetch_cpi(1968, dt.date.today().year)
    write_csv(DATA / "us_cpi_monthly.csv", ["month", "cpi_u_nsa"], cpi)
    print(f"    {len(cpi):,} months, {cpi[0][0]} -> {cpi[-1][0]}")

    manifest = {
        "fetched_at": dt.datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %z"),
        "series": [
            {
                "file": "data/gold_lbma_pm_daily.csv",
                "name": "LBMA Gold Price PM (USD/oz)",
                "url": LBMA_URL,
                "rows": len(gold), "first": gold[0][0], "last": gold[-1][0],
                "note": "London afternoon benchmark. Pre-1968-04 there is no market price: "
                        "gold was pegged at USD 35/oz.",
            },
            {
                "file": "data/us_m2_monthly.csv",
                "name": "US M2 money stock, seasonally adjusted (USD bn)",
                "url": H6_URL,
                "rows": len(m2), "first": m2[0][0], "last": m2[-1][0],
                "note": "Federal Reserve H.6. The M2 definition was revised in Feb 2021 "
                        "(savings deposits reclassified); levels before/after May 2020 are "
                        "not a perfectly clean series.",
            },
            {
                "file": "data/us_cpi_monthly.csv",
                "name": "CPI-U, all items, US city average, NSA (1982-84=100)",
                "url": BLS_URL + f" (series {CPI_SERIES})",
                "rows": len(cpi), "first": cpi[0][0], "last": cpi[-1][0],
                "note": "BLS public API v1, 10-year chunks, no key.",
            },
        ],
    }
    (HERE / "data" / "source_manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    print("\nwrote data/source_manifest.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
