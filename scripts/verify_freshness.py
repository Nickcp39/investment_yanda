#!/usr/bin/env python3
"""verify_freshness.py -mechanical data-freshness gate for a research dossier.

WHY THIS EXISTS (incident INC-001):
  companies/nvda/ (as_of 2026-06-19) shipped current price $145.48 -actually ~the
  52-week LOW ($142.03). The real last close was $210.69. The 45% error flipped the
  verdict (base 5y IRR +13% -> +4.8%, STARTER -> WATCH) yet the human Checker stamped
  CLEAN, because the freshness check was a JUDGMENT CHECKBOX that only confirmed the
  price's DATE (<= as_of) and that the (wrong) value was copied consistently across files.

WHAT THIS DOES (the guarantee):
  A dossier may be marked CLEAN only if this validator exits 0 and a committed
  freshness_check.json with "status":"PASS" exists for that (ticker, as_of). It:
    1. RE-FETCHES the price independently (last close <= as_of) via the repo's proven
       fetch_yahoo (scripts/market_data_download.py) -> compares to the dossier value.
       This is an INDEPENDENT pull, not a re-derivation of the card's own numbers, so it
       cannot reproduce the Checker's mistake (everything internally consistent w/ a bad input).
    2. CROSS-CHECKS price across >=2 independent sources declared in freshness.json.
    3. Runs structural TRIPWIRES T1-T6 (incl. "current ~= 52wk low/high" -the exact tell).
    4. Hard-BLOCKS on any failure or if it cannot reach >=2 sources (never a silent pass).

Decay axis (orthogonal to source tier A1-E1): LIVE data (price, market cap, 52wk band,
shares, plus export-control/litigation/guidance) decays fast and is re-verified every run;
FILED data (10-K/10-Q line items) rides the dated-source claim_ledger discipline.

EXIT CODES: 0 = PASS | 1 = BLOCK (itemized failures) | 2 = usage/internal error (no interpreter,
pandas missing, dossier unreadable) -also blocking, distinguished so a wrapper can tell
"validator broke" from "dossier failed".

Usage:
  python scripts/verify_freshness.py --dossier companies/nvda/2026-06-20
  python scripts/verify_freshness.py --dossier companies/nvda/2026-06-19   # -> BLOCK (the bad run)
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

# Import the repo's proven Yahoo fetcher (sibling module in scripts/). Adding the script's
# own dir to sys.path makes `import market_data_download` work whether this is run as
# `python scripts/verify_freshness.py` or from elsewhere.
_SCRIPT_DIR = Path(__file__).resolve().parent
if str(_SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_DIR))

VALIDATOR_VERSION = "verify_freshness-v1"


def _load_fetcher():
    """Return (fetch_yahoo, _retry, err). err is set (and funcs None) if pandas/module missing."""
    try:
        from market_data_download import fetch_yahoo, _retry  # noqa: WPS433 (intentional sibling import)
        return fetch_yahoo, _retry, None
    except Exception as e:  # pandas missing, module moved, etc.
        return None, None, e


# --------------------------------------------------------------------------- helpers
def _rel(a: float, b: float) -> float:
    """Relative difference |a-b|/|b| (the denominator is the 'truth' side)."""
    return abs(a - b) / abs(b) if b else float("inf")


def _read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def _read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except Exception:
        return ""


def _find_claim_value(rows, *needles):
    """First claim_ledger row whose 'claim' contains ALL needles (case-insensitive) -> float value."""
    for r in rows:
        claim = (r.get("claim") or "").lower()
        if all(n.lower() in claim for n in needles):
            try:
                return float(str(r.get("value")).replace(",", ""))
            except (TypeError, ValueError):
                return None
    return None


def _fmt_price(p: float) -> str:
    """Canonical price string used for the single-value-of-truth scan, e.g. 210.69."""
    s = f"{p:.2f}"
    return s


# --------------------------------------------------------------------------- inputs
def load_dossier(dossier: Path):
    card_path = dossier / "decision_card.json"
    if not card_path.exists():
        raise FileNotFoundError(f"no decision_card.json in {dossier}")
    card = _read_json(card_path)

    manifest = None
    man_path = dossier / "freshness.json"
    if man_path.exists():
        manifest = _read_json(man_path)

    ledger_rows = []
    ledger_path = dossier / "claim_ledger.csv"
    if ledger_path.exists():
        with ledger_path.open(encoding="utf-8") as f:
            ledger_rows = list(csv.DictReader(f))

    # Backtests carry sources_used.csv (not claim_ledger.csv); used by T7 no-lookahead.
    sources_rows = []
    src_path = dossier / "sources_used.csv"
    if src_path.exists():
        with src_path.open(encoding="utf-8") as f:
            sources_rows = list(csv.DictReader(f))

    return card, manifest, ledger_rows, sources_rows


def live_field(manifest, field):
    """Return the manifest live_fields entry for `field`, or None."""
    if not manifest:
        return None
    for lf in manifest.get("live_fields", []):
        if lf.get("field") == field:
            return lf
    return None


def get_live_value(manifest, field, ledger_rows, *ledger_needles, default=None):
    """Prefer the manifest value for a LIVE field; fall back to claim_ledger keyword match."""
    lf = live_field(manifest, field)
    if lf is not None and lf.get("value") is not None:
        try:
            return float(lf["value"])
        except (TypeError, ValueError):
            return lf["value"]
    if ledger_needles:
        v = _find_claim_value(ledger_rows, *ledger_needles)
        if v is not None:
            return v
    return default


# --------------------------------------------------------------------------- price re-fetch
def refetch_last_close(ticker, as_of, fetch_yahoo, _retry):
    """Independently pull the LAST close <= as_of from Yahoo. Returns (price, date) or raises."""
    asof_d = dt.date.fromisoformat(as_of)
    start = (asof_d - dt.timedelta(days=14)).isoformat()
    end = (asof_d + dt.timedelta(days=4)).isoformat()  # wide end; we filter <= as_of below
    s = _retry(fetch_yahoo, ticker, start, end)
    pairs = [(d, float(v)) for d, v in zip(list(s.index), list(s.values)) if d <= as_of]
    if not pairs:
        raise ValueError(f"no close <= {as_of} in fetched window {start}..{end}")
    last_date, last_close = pairs[-1]
    return last_close, last_date


def _fetch_raw_and_splits(ticker, start, end):
    """BACKTEST helper -direct Yahoo v8 pull. Returns (rows, splits):
      rows   = [(YYYY-MM-DD, raw_close_float), ...]  (raw `quote.close`)
      splits = {YYYY-MM-DD: ratio_float}             (e.g. a 10:1 split -> 10.0)
    Yahoo split-adjusts the raw close too, so to recover the CONTEMPORANEOUS nominal price
    we multiply the raw close by the product of split ratios dated AFTER the as_of (see
    refetch_nominal). Uses urllib directly (no pandas) so backtest mode has no extra deps.
    """
    def _epoch(d):
        return int(dt.datetime.strptime(d, "%Y-%m-%d").timestamp())

    url = (f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}"
           f"?period1={_epoch(start)}&period2={_epoch(end)}&interval=1d&events=div%2Csplits")
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        payload = json.loads(resp.read().decode("utf-8"))
    res = payload["chart"]["result"][0]
    ts = res.get("timestamp") or []
    raw = (res.get("indicators", {}).get("quote") or [{}])[0].get("close") or []
    rows = []
    for i, t in enumerate(ts):
        if i < len(raw) and raw[i] is not None:
            d = dt.datetime.fromtimestamp(t, dt.timezone.utc).strftime("%Y-%m-%d")
            rows.append((d, float(raw[i])))
    splits = {}
    for s in (res.get("events", {}).get("splits", {}) or {}).values():
        sd = dt.datetime.fromtimestamp(s["date"], dt.timezone.utc).strftime("%Y-%m-%d")
        denom = s.get("denominator") or 1
        splits[sd] = (s.get("numerator") or 1) / denom
    return rows, splits


def refetch_nominal(ticker, as_of):
    """BACKTEST: independently re-derive the contemporaneous NOMINAL price for a frozen as_of.
    nominal = raw_close(last trading day <= as_of) x product(split ratios dated > as_of).
    Returns (nominal_price, date, split_factor) or raises. Example: NVDA 2023-05-25 raw close
    today reads $37.98 (Yahoo split-adjusted for the 2024 10:1); x10 -> $379.80 nominal.
    """
    asof_d = dt.date.fromisoformat(as_of)
    start = (asof_d - dt.timedelta(days=18)).isoformat()
    end = dt.date.today().isoformat()
    rows, splits = _fetch_raw_and_splits(ticker, start, end)
    le = [(d, v) for d, v in rows if d <= as_of]
    if not le:
        raise ValueError(f"no raw close <= {as_of} in window {start}..{end}")
    last_date, raw_close = le[-1]
    factor = 1.0
    for sdate, ratio in splits.items():
        if sdate > as_of:
            factor *= ratio
    return raw_close * factor, last_date, factor


# --------------------------------------------------------------------------- tripwires
def tw(idn, name, status, detail):
    return {"id": idn, "name": name, "status": status, "detail": detail}


def run_tripwires(card, manifest, ledger_rows, dossier, low_high_band, qual_days, mode="live", sources_rows=None):
    price = float(card.get("as_of_price"))
    mcap = card.get("as_of_market_cap")
    as_of = card.get("as_of")
    hi = get_live_value(manifest, "52wk_high", ledger_rows, "52-week high")
    lo = get_live_value(manifest, "52wk_low", ledger_rows, "52-week low")
    shares_m = get_live_value(manifest, "shares_out", ledger_rows, "diluted weighted shares")
    out = []

    # T1 -52wk band containment
    if hi and lo:
        ok = lo <= price <= hi
        out.append(tw("T1", "52wk band containment",
                      "PASS" if ok else "FAIL",
                      f"{lo} <= {price} <= {hi}" if ok else f"{price} outside [{lo}, {hi}]"))
    else:
        out.append(tw("T1", "52wk band containment", "SKIP", "no 52wk high/low found"))

    # T2 -low/high hug (the exact NVDA tell: 145.48 ~= 52wk low 142.03)
    if hi and lo:
        d_lo = _rel(price, lo)
        d_hi = _rel(price, hi)
        justified = bool((live_field(manifest, "price") or {}).get("low_high_hug_justified"))
        if (d_lo <= low_high_band or d_hi <= low_high_band) and not justified:
            which = "52wk low" if d_lo <= d_hi else "52wk high"
            out.append(tw("T2", "low/high hug", "FAIL",
                          f"price is {min(d_lo, d_hi) * 100:.2f}% off {which} "
                          f"(<= {low_high_band * 100:.0f}% band) and not justified -> likely grabbed an "
                          f"extreme of the series instead of the last close"))
        else:
            out.append(tw("T2", "low/high hug", "PASS",
                          f"+{d_lo * 100:.1f}% off low, -{d_hi * 100:.1f}% off high"))
    else:
        out.append(tw("T2", "low/high hug", "SKIP", "no 52wk high/low found"))

    # T3 -market-cap identity (price x shares ~= reported mcap)
    if mcap and shares_m:
        implied = price * shares_m * 1e6
        d = _rel(implied, float(mcap))
        out.append(tw("T3", "market-cap identity",
                      "PASS" if d <= 0.01 else "FAIL",
                      f"{shares_m:.0f}M x {price} = {implied/1e12:.3f}T vs card {float(mcap)/1e12:.3f}T ({d*100:.2f}%)"))
    else:
        out.append(tw("T3", "market-cap identity", "SKIP", "missing market_cap or shares"))

    # T4 -distance-from-high narrative reconciles with the CARD price (internal consistency)
    if hi:
        text = _read_text(dossier / "valuation.md") + "\n" + _read_text(dossier / "facts.md")
        m = re.search(r"[-−]\s?(\d{1,2}(?:\.\d)?)\s?%[^\n]{0,18}(?:off\s+high|高点|52)", text)
        if not m:
            m = re.search(r"(?:off\s+high|距.{0,3}高点)[^\n]{0,12}[-−]\s?(\d{1,2}(?:\.\d)?)\s?%", text)
        if m:
            stated = float(m.group(1))
            actual = abs(price / hi - 1) * 100
            d = abs(stated - actual)
            out.append(tw("T4", "distance-from-high reconciliation",
                          "PASS" if d <= 1.0 else "FAIL",
                          f"narrative -{stated}% vs card-implied -{actual:.1f}% (gap {d:.1f}pt)"))
        else:
            out.append(tw("T4", "distance-from-high reconciliation", "SKIP", "no distance claim found"))
    else:
        out.append(tw("T4", "distance-from-high reconciliation", "SKIP", "no 52wk high"))

    # T5 -single value of truth: canonical as_of_price appears verbatim in every price-bearing file
    pstr = _fmt_price(price)
    targets = ["facts.md", "valuation.md", "model/scenario_model.csv", "decision_card.md"]
    missing = []
    for rel_path in targets:
        p = dossier / rel_path
        if p.exists():
            if pstr not in _read_text(p):
                missing.append(rel_path)
    out.append(tw("T5", "single value of truth",
                  "PASS" if not missing else "FAIL",
                  f"as_of_price {pstr} present in all price-bearing files"
                  if not missing else f"as_of_price {pstr} MISSING from: {', '.join(missing)}"))

    # T6 -LIVE-qualitative freshness (export-control / litigation / guidance). WARN-level, never
    # the sole BLOCK cause, EXCEPT a declared qualitative field with zero sources is a FAIL.
    qual_fields = ["export_control_status", "active_litigation", "guidance"]
    if manifest:
        asof_d = dt.date.fromisoformat(as_of)
        for fld in qual_fields:
            lf = live_field(manifest, fld)
            if lf is None:
                continue
            srcs = lf.get("sources") or []
            if not srcs:
                out.append(tw("T6", f"LIVE-qualitative freshness [{fld}]", "FAIL", "declared but has 0 sources"))
                continue
            newest = None
            for sdate in [s.get("public_date") or s.get("fetched_at") for s in srcs]:
                if not sdate:
                    continue
                try:
                    d = dt.date.fromisoformat((sdate + "-01")[:10] if len(sdate) == 7 else sdate[:10])
                    newest = d if newest is None or d > newest else newest
                except ValueError:
                    continue
            if newest is None:
                out.append(tw("T6", f"LIVE-qualitative freshness [{fld}]", "WARN", "no parseable source date"))
            else:
                age = (asof_d - newest).days
                if age > qual_days:
                    out.append(tw("T6", f"LIVE-qualitative freshness [{fld}]", "WARN",
                                  f"newest source {newest} is {age}d before as_of (> {qual_days}d) -confirm it is still the latest authoritative event"))
                else:
                    out.append(tw("T6", f"LIVE-qualitative freshness [{fld}]", "PASS", f"newest source {newest} ({age}d)"))
    else:
        out.append(tw("T6", "LIVE-qualitative freshness", "WARN", "no freshness.json manifest -cannot verify LIVE-qualitative items"))

    # T7 (BACKTEST only) -no-lookahead: every source public_date <= as_of. Mechanizes the
    # source-date dimension of LOOKAHEAD_CHECKER.md (hindsight-language scan stays there).
    if mode == "backtest":
        asof_d = dt.date.fromisoformat(as_of)
        # Prefer sources_used.csv (complete list); fall back to decision_card.json sources_used[].
        pairs = []
        for r in (sources_rows or []):
            pairs.append((r.get("source_id") or "?", r.get("public_date")))
        if not pairs:
            for s in card.get("sources_used", []):
                pairs.append((s.get("source_id") or "?", s.get("public_date")))
        offenders, checked = [], 0
        for sid, pd_ in pairs:
            if not pd_:
                continue
            try:
                d = dt.date.fromisoformat((pd_ + "-01")[:10] if len(pd_) == 7 else pd_[:10])
            except ValueError:
                continue
            checked += 1
            if d > asof_d:
                offenders.append(f"{sid}:{pd_}")
        if not checked:
            out.append(tw("T7", "no-lookahead (source<=as_of)", "SKIP", "no parseable source dates found"))
        elif offenders:
            out.append(tw("T7", "no-lookahead (source<=as_of)", "FAIL",
                          f"{len(offenders)} source(s) dated AFTER as_of {as_of}: {', '.join(offenders[:6])}"))
        else:
            out.append(tw("T7", "no-lookahead (source<=as_of)", "PASS", f"all {checked} source dates <= {as_of}"))

    return out


# --------------------------------------------------------------------------- price cross-check
def cross_check_price(card_price, refetched, refetch_err, manifest, tol):
    """Compare card price vs independent Yahoo re-fetch vs >=2 manifest sources."""
    result = {"card_value": card_price, "tolerance_pct": tol * 100}
    deltas = []
    source_names = set()

    if refetched is not None:
        result["refetched_yahoo"] = refetched
        deltas.append(("card_vs_yahoo_refetch", _rel(card_price, refetched)))
        source_names.add("yahoo")
    else:
        result["refetched_yahoo"] = None
        result["refetch_error"] = str(refetch_err)[:160] if refetch_err else "fetch returned nothing"

    man_sources = []
    pf = live_field(manifest, "price")
    if pf:
        for s in pf.get("sources", []):
            name, val = s.get("source_name"), s.get("value")
            if name and val is not None:
                man_sources.append({"source_name": name, "value": float(val)})
                deltas.append((f"card_vs_{name}", _rel(card_price, float(val))))
                source_names.add(name.split("/")[0].lower())
    result["manifest_sources"] = man_sources

    max_delta = max((d for _, d in deltas), default=None)
    result["max_pairwise_delta_pct"] = round(max_delta * 100, 3) if max_delta is not None else None
    result["independent_sources"] = sorted(source_names)

    # Decision order: a value mismatch is a hard FAIL even with one source; otherwise require >=2.
    if max_delta is not None and max_delta > tol:
        worst = max(deltas, key=lambda kv: kv[1])
        result["result"] = "FAIL"
        result["detail"] = f"{worst[0]} delta {worst[1]*100:.1f}% exceeds tolerance {tol*100:.0f}%"
    elif len(source_names) < 2:
        result["result"] = "UNVERIFIABLE"
        result["detail"] = (f"only {len(source_names)} independent price source(s) reachable/declared; "
                            f"need >=2 -refusing to authorize")
    else:
        result["result"] = "PASS"
        result["detail"] = f"{len(source_names)} independent sources agree within {tol*100:.0f}%"
    return result


# --------------------------------------------------------------------------- main
def main() -> int:
    ap = argparse.ArgumentParser(description="Mechanical data-freshness gate for a research dossier.")
    ap.add_argument("--dossier", required=True, help="path to the date-keyed dossier folder")
    ap.add_argument("--tolerance", type=float, default=0.01, help="price/mcap cross-check tolerance (default 0.01 = 1%%)")
    ap.add_argument("--low-high-band", type=float, default=0.03, help="T2 low/high-hug threshold (default 0.03)")
    ap.add_argument("--qual-days", type=int, default=45, help="T6 LIVE-qualitative recency window vs as_of (default 45)")
    ap.add_argument("--out", default=None, help="output json path (default <dossier>/freshness_check.json)")
    ap.add_argument("--mode", choices=["auto", "live", "backtest"], default="auto",
                    help="live = adjusted last-close (default); backtest = nominal raw x split-factor + T7 no-lookahead; "
                         "auto detects 'backtest' from a dossier path under backtests/ or cases/")
    ap.add_argument("--offline", action="store_true", help="skip the network re-fetch (tripwires only; never authorizes)")
    args = ap.parse_args()

    # Make console output robust on Windows (cp1252) consoles: never crash on a non-ASCII char.
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass

    dossier = Path(args.dossier).resolve()
    out_path = Path(args.out) if args.out else dossier / "freshness_check.json"

    try:
        card, manifest, ledger_rows, sources_rows = load_dossier(dossier)
    except Exception as e:
        print(f"USAGE/INTERNAL ERROR: {e}")
        return 2

    mode = args.mode
    if mode == "auto":
        parts = set(dossier.parts)
        mode = "backtest" if ("backtests" in parts or "cases" in parts) else "live"

    ticker = card.get("ticker")
    as_of = card.get("as_of")
    card_price = card.get("as_of_price")
    if card_price is None or not as_of or not ticker:
        print("USAGE/INTERNAL ERROR: decision_card.json missing ticker / as_of / as_of_price")
        return 2
    card_price = float(card_price)

    # ---- independent price re-fetch (LIVE = adjusted last-close; BACKTEST = nominal raw x split)
    refetched = refetched_date = refetch_err = None
    split_factor = None
    price_basis = "yahoo_adjclose"
    if not args.offline:
        if mode == "backtest":
            price_basis = "yahoo_raw_x_split"
            try:
                refetched, refetched_date, split_factor = refetch_nominal(ticker, as_of)
            except Exception as e:
                refetch_err = e
        else:
            fetch_yahoo, _retry, ferr = _load_fetcher()
            if ferr is not None:
                print(f"USAGE/INTERNAL ERROR: cannot import fetcher (pandas missing?): {ferr}")
                return 2
            try:
                refetched, refetched_date = refetch_last_close(ticker, as_of, fetch_yahoo, _retry)
            except Exception as e:
                refetch_err = e

    price_block = cross_check_price(card_price, refetched, refetch_err, manifest, args.tolerance)
    if refetched_date:
        price_block["refetched_date"] = refetched_date
    if split_factor is not None:
        price_block["split_factor"] = split_factor

    tripwires = run_tripwires(card, manifest, ledger_rows, dossier, args.low_high_band, args.qual_days,
                              mode=mode, sources_rows=sources_rows)

    # ---- verdict
    failures = []
    if price_block["result"] in ("FAIL", "UNVERIFIABLE"):
        failures.append(f"price:{price_block['result']} -{price_block['detail']}")
    for t in tripwires:
        if t["status"] == "FAIL":
            failures.append(f"{t['id']}:{t['name']} -{t['detail']}")

    status = "PASS" if not failures else ("UNVERIFIABLE" if price_block["result"] == "UNVERIFIABLE" and len(failures) == 1 else "BLOCK")
    exit_code = 0 if status == "PASS" else 1

    result = {
        "ticker": ticker,
        "as_of": as_of,
        "validator_version": VALIDATOR_VERSION,
        "pipeline_version": card.get("pipeline_version"),
        "mode": mode,
        "status": status,
        "exit_code": exit_code,
        "price_basis": price_basis,
        "price": price_block,
        "tripwires": tripwires,
        "warnings": [f"{t['id']}:{t['name']} -{t['detail']}" for t in tripwires if t["status"] == "WARN"],
        "failures": failures,
    }

    out_path.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    # human-readable transcript alongside
    txt = [
        f"FRESHNESS CHECK -{ticker} as_of {as_of}  [{VALIDATOR_VERSION}]",
        f"STATUS: {status}  (exit {exit_code})",
        f"price: card={card_price} refetched_yahoo={price_block.get('refetched_yahoo')} "
        f"({price_block.get('refetched_date','-')}) -> {price_block['result']} :: {price_block['detail']}",
        "tripwires:",
    ]
    for t in tripwires:
        txt.append(f"  [{t['status']:4s}] {t['id']} {t['name']}: {t['detail']}")
    if failures:
        txt.append("FAILURES:")
        txt.extend(f"  - {f}" for f in failures)
    transcript = "\n".join(txt)
    (out_path.with_suffix(".txt")).write_text(transcript + "\n", encoding="utf-8")

    print(transcript)
    print(f"\nwrote {out_path.name} + {out_path.with_suffix('.txt').name}")
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
