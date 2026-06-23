#!/usr/bin/env python
"""Log-linear trend channel ("fair-value growth channel") for SPY / QQQ.

Idea (what the user asked for):
  On a LOG scale, constant compound growth = a STRAIGHT LINE. Fit
      ln(price) = a + b * t      (OLS over time)
  -> slope b is the index's "stable speed" (annualized CAGR = exp(b*365.25)-1).
  Residual sigma gives deviation bands. Where price sits vs the line:
      |dev| < 1 sigma   -> 合理 / normal speed
      +1..+2 sigma      -> 偏热 / running hot
      > +2 sigma        -> 超速 / overheated (historically mean-reverts)
      -1..-2 sigma      -> 偏冷 / below trend
      < -2 sigma        -> 降速 / broken-down or cheap

Honesty caveat baked in: the fitted "fair value" depends entirely on the window.
2010->today is an almost-uninterrupted bull (post-GFC + ZIRP + AI), so the trend
slope is steep and "fair value" is biased HIGH. The script therefore reports the
fit over THREE windows (full / 10y / 5y) so you can see how much the answer moves.

Inputs : macro/market_panel/data/{SPY,QQQ}.csv  (date,value ; dividend-adj close)
Outputs: macro/market_panel/log_trend/<IDX>_channel.csv  (full-fit channel)
         macro/market_panel/log_trend/<IDX>_log_trend.png (if matplotlib present)
         macro/market_panel/log_trend/summary.md
"""
from __future__ import annotations
import math
import sys
from pathlib import Path

import numpy as np
import pandas as pd

# Windows consoles default to cp1252, which can't encode σ / Chinese verdicts.
try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

ROOT = Path(__file__).resolve().parents[1]
PANEL = ROOT / "macro" / "market_panel" / "data"
OUT = ROOT / "macro" / "market_panel" / "log_trend"
OUT.mkdir(parents=True, exist_ok=True)

INDICES = ["SPY", "QQQ"]
WINDOWS = {"full": None, "10y": 10, "5y": 5}  # years lookback (None = all)


def load(label: str) -> pd.DataFrame:
    df = pd.read_csv(PANEL / f"{label}.csv")
    cols = list(df.columns)
    df = df.rename(columns={cols[0]: "date", cols[1]: "value"})
    df["date"] = pd.to_datetime(df["date"])
    df = df.dropna(subset=["value"]).sort_values("date").reset_index(drop=True)
    df = df[df["value"] > 0]
    return df.reset_index(drop=True)


def fit_window(df: pd.DataFrame, years):
    """OLS of ln(price) on days; return slope/intercept/sigma over the window
    plus the CURRENT (last-row) deviation. Time origin = first row of FULL df."""
    t_all = (df["date"] - df["date"].iloc[0]).dt.days.values.astype(float)
    y_all = np.log(df["value"].values)
    if years is None:
        mask = np.ones(len(df), bool)
    else:
        cutoff = df["date"].iloc[-1] - pd.DateOffset(years=years)
        mask = (df["date"] >= cutoff).values
    t, y = t_all[mask], y_all[mask]
    b, a = np.polyfit(t, y, 1)                 # slope (per day), intercept
    resid = y - (a + b * t)
    sigma = float(resid.std(ddof=1))
    cur_dev = float(y_all[-1] - (a + b * t_all[-1]))
    return {
        "a": a, "b": b, "sigma": sigma,
        "cagr": math.exp(b * 365.25) - 1.0,
        "cur_dev_log": cur_dev,
        "cur_dev_pct": math.exp(cur_dev) - 1.0,   # % above/below the trend line
        "cur_sigma": cur_dev / sigma if sigma else float("nan"),
        "n": int(mask.sum()),
        "t_all": t_all, "y_all": y_all,
    }


def verdict(sig: float) -> str:
    if sig > 2:   return "超速 OVERHEATED (>+2σ)"
    if sig > 1:   return "偏热 hot (+1..+2σ)"
    if sig < -2:  return "降速/破位 BROKEN-DOWN (<-2σ)"
    if sig < -1:  return "偏冷 cheap (-1..-2σ)"
    return "合理 normal (±1σ)"


def trailing_growth(df: pd.DataFrame, win: int = 252) -> float:
    if len(df) <= win:
        return float("nan")
    return df["value"].iloc[-1] / df["value"].iloc[-1 - win] - 1.0


def main() -> None:
    lines = ["# Log-Linear Trend Channel — SPY / QQQ", ""]
    last_date = None
    for idx in INDICES:
        df = load(idx)
        last_date = df["date"].iloc[-1].date()
        price = float(df["value"].iloc[-1])
        fits = {name: fit_window(df, yrs) for name, yrs in WINDOWS.items()}
        full = fits["full"]
        g1y = trailing_growth(df)

        # ---- console + summary ----
        print(f"\n=== {idx}  (through {last_date}, ${price:,.2f}) ===")
        hdr = f"{'window':>6} {'n':>6} {'CAGR':>7} {'cur vs trend':>13} {'σ':>6}  verdict"
        print(hdr)
        lines += [f"## {idx} — through {last_date}, **${price:,.2f}**", "",
                  "| window | n | trend CAGR | current vs trend | σ | verdict |",
                  "|---|---:|---:|---:|---:|---|"]
        for name in WINDOWS:
            f = fits[name]
            print(f"{name:>6} {f['n']:>6} {f['cagr']*100:>6.1f}% "
                  f"{f['cur_dev_pct']*100:>+11.1f}% {f['cur_sigma']:>+6.2f}  {verdict(f['cur_sigma'])}")
            lines.append(f"| {name} | {f['n']} | {f['cagr']*100:.1f}% | "
                         f"{f['cur_dev_pct']*100:+.1f}% | {f['cur_sigma']:+.2f} | {verdict(f['cur_sigma'])} |")
        speed = (f"trailing-1y growth {g1y*100:+.1f}% vs full-history CAGR "
                 f"{full['cagr']*100:.1f}% -> "
                 + ("超速 accelerating" if g1y > full['cagr']*1.25 else
                    "降速 decelerating" if g1y < full['cagr']*0.5 else "≈ normal speed"))
        print("  speed:", speed)
        lines += ["", f"**Speed:** {speed}", ""]

        # ---- channel CSV (full-history fit) ----
        a, b, sigma = full["a"], full["b"], full["sigma"]
        t_all, y_all = full["t_all"], full["y_all"]
        trend = a + b * t_all
        chan = pd.DataFrame({
            "date": df["date"].dt.date, "price": df["value"].values,
            "trend": np.exp(trend),
            "minus1sd": np.exp(trend - sigma), "plus1sd": np.exp(trend + sigma),
            "minus2sd": np.exp(trend - 2 * sigma), "plus2sd": np.exp(trend + 2 * sigma),
            "dev_sigma": (y_all - trend) / sigma,
        })
        chan.to_csv(OUT / f"{idx}_channel.csv", index=False)

        # ---- figure (optional) ----
        try:
            import matplotlib
            matplotlib.use("Agg")
            import matplotlib.pyplot as plt
            fig, ax = plt.subplots(figsize=(11, 6))
            ax.semilogy(df["date"], df["value"], lw=1.1, color="#1a1d21", label=idx)
            ax.semilogy(df["date"], np.exp(trend), lw=1.4, color="#1f6feb",
                        label=f"log trend ({full['cagr']*100:.1f}%/yr)")
            for k, c in [(1, "#b7791f"), (2, "#c0392b")]:
                ax.semilogy(df["date"], np.exp(trend + k * sigma), lw=.8, ls="--", color=c, alpha=.8)
                ax.semilogy(df["date"], np.exp(trend - k * sigma), lw=.8, ls="--", color=c, alpha=.8)
            ax.scatter([df["date"].iloc[-1]], [price], color="#c0392b", zorder=5, s=40)
            ax.annotate(f"  {full['cur_dev_pct']*100:+.0f}% / {full['cur_sigma']:+.2f}σ",
                        (df["date"].iloc[-1], price), color="#c0392b", va="center")
            ax.set_title(f"{idx} — log-linear fair-value channel (2010→{last_date})")
            ax.legend(loc="upper left", fontsize=9)
            ax.grid(True, which="both", alpha=.15)
            fig.tight_layout()
            fig.savefig(OUT / f"{idx}_log_trend.png", dpi=120)
            plt.close(fig)
            print(f"  figure -> {OUT / f'{idx}_log_trend.png'}")
        except Exception as e:  # noqa: BLE001
            print(f"  (no figure: {e})")

    lines += ["---", "",
              "Caveat: the 2010→ window is an almost-uninterrupted bull (post-GFC + ZIRP + AI),",
              "so the full-history trend slope is steep and 'fair value' is biased high.",
              "Read the 10y/5y rows as sensitivity. This is a temperature/mean-reversion gauge,",
              "not a timing signal; the trend itself can re-rate.",
              "", f"Built by `scripts/log_trend_channel.py` from `macro/market_panel/data/`. Data through {last_date}."]
    (OUT / "summary.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"\nsummary -> {OUT / 'summary.md'}")


if __name__ == "__main__":
    main()
