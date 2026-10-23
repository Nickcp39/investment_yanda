#!/usr/bin/env python
"""One-click market-temperature pipeline.

    python scripts/market_temp/run.py                 # fetch -> compute -> render into output/market_temp/<as_of>/
    python scripts/market_temp/run.py --no-fetch      # reuse the cache in data/market_temp/
    python scripts/market_temp/run.py --as-of 2026-10-09   # reproduce an earlier reading (writes to output/market_temp/_backfill/<date>/)
    python scripts/market_temp/run.py --pdf           # also render temp.md -> output/pdf/市场体温_<as_of>.pdf
    python scripts/market_temp/run.py --ai            # after rendering, call `claude -p` headless to write ai_notes.md (see ai_update.py)

Double-click run_market_temp.bat (or run_market_temp_ai.bat) at the repo root for the same thing.
"""
import argparse
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import OUT, REPO, flush_log, log  # noqa: E402


def main():
    ap = argparse.ArgumentParser(description="market temperature pipeline")
    ap.add_argument("--no-fetch", action="store_true", help="skip network, use data/market_temp cache")
    ap.add_argument("--as-of", default=None, help="YYYY-MM-DD: truncate every series to reproduce an earlier reading")
    ap.add_argument("--pdf", action="store_true", help="also build a PDF via scripts/md_to_pdf.py")
    ap.add_argument("--ai", action="store_true", help="run the headless Claude step (ai_update.py)")
    ap.add_argument("--model", default="sonnet", help="model for --ai (default sonnet)")
    ap.add_argument("--budget", type=float, default=3.0, help="max USD for --ai (default 3)")
    args = ap.parse_args()
    t0 = time.time()

    import fetch
    import compute
    import render

    man = fetch.fetch_all(skip_network=args.no_fetch)
    S, G = compute.compute(args.as_of)
    needs = fetch.staleness(man, S["as_of"])
    man.save()
    S["needs_ai"] = needs
    S["freshness"] = {k: dict(status=v.get("status"), last=v.get("last"), stale_days=v.get("stale_days"), stale=v.get("stale"), error=v.get("error"))
                      for k, v in man.m["series"].items()}
    backfill = bool(args.as_of)
    folder = (OUT / "_backfill" / S["as_of"]) if backfill else (OUT / S["as_of"])
    D = compute.load(args.as_of)
    render.write_outputs(S, G, D, folder, backfill=backfill)

    if args.pdf:
        pdf = REPO / "output" / "pdf" / f"市场体温_{S['as_of']}.pdf"
        cmd = [sys.executable, str(REPO / "scripts" / "md_to_pdf.py"), str(folder / "temp.md"), str(pdf), f"市场体温 · 截至 {S['as_of']}"]
        r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
        log("pdf", "ok" if r.returncode == 0 else f"FAILED rc={r.returncode} {r.stderr[-400:]}", pdf.relative_to(REPO))

    if args.ai:
        import ai_update
        ai_update.run_ai(folder, S, needs, model=args.model, budget=args.budget)

    Q, NE, L = S["qqq"], S["ndx_eras"], S["levels"]
    log("-" * 72)
    log(f"as_of {S['as_of']} | QQQ {Q['close']:.2f} ({Q['chg_1d_pct']:+.1f}% d/d) | 距最高 {Q['drawdown_pct']:+.1f}% | vs200dma {Q['vs_200dma_pct']:+.1f}%")
    log("纳指四把尺子 偏离/分位: " + " | ".join(f"{k}: {NE[k]['dev']:+.0f}% / {NE[k]['pct']:.0f}" for k in ("2000", "2008", "2015", "2021")))
    log(f"前瞻PE {L['fwd_pe']:.1f} ({L['fwd_pe_date']}) | CAPE {L['cape']:.1f} | 10y {L['tnx']:.2f}% | VIX {L['vix']:.1f} | 金 {L['gold']:,.0f}")
    log("热度: " + " | ".join(f"{k} {v:.0f}" for k, v in S["heat_by_group"].items()) + f" | 总 {S['heat_overall']:.0f}")
    c = S["dca_channel"]["QQQ"]
    log(f"QQQ σ 通道(2010起): {c['cur_sigma']:+.2f}σ | −1σ 翻倍线 {c['minus1sd']:.0f} (需 {c['to_minus1sd_pct']:+.0f}%)")
    log(f"AI 待补 {len(needs)} 项 | 输出 {folder.relative_to(REPO)} | {time.time() - t0:.0f}s")
    flush_log(folder / "run_log.txt")
    return 0


if __name__ == "__main__":
    sys.exit(main())
