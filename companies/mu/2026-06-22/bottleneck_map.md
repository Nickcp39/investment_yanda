# MU Bottleneck Map — as_of 2026-06-22

## The bottleneck thesis

The AI buildout has created a **memory bottleneck**: high-end AI accelerators are constrained by HBM supply
(bandwidth + capacity), and leading-node data-center DRAM is scarce. Micron is one of three suppliers of this
scarce input → it sits *adjacent to* the AI compute bottleneck and captures economics from it.

## Is it a real bottleneck? (evidence)

- **YES, currently.** HBM is sold out for 2026 across the industry; Micron's entire 2026 HBM output is
  contracted under multi-year agreements (S3). Pricing has moved from quarterly commodity negotiation to
  multi-year contracts — the market behavior of a genuine shortage, not a manufactured one.
- Gross margins (74%) and the velocity of the up-leg (GM 36.8% → 74.4% in a year) corroborate a real
  supply/demand squeeze, not just sentiment.
- HBM demand growth +77% (2026) / +68% (2027) per TrendForce (S10) — the demand curve is steep.

## But — who OWNS the bottleneck vs who is a supplier into it?

- **NVIDIA owns the AI-compute bottleneck** (the accelerator + CUDA). Micron is a *critical supplier* into it.
  A supplier into a bottleneck captures real economics while the shortage lasts, but is more replaceable and
  more cyclical than the bottleneck owner: there are 3 HBM suppliers, and the customer (NVIDIA) actively
  multi-sources to avoid dependence.
- **The memory bottleneck is more competible than the compute bottleneck.** All three suppliers are racing
  to add HBM capacity (DRAM→HBM mix shift + new fabs). Memory bottlenecks have *always* resolved via supply
  response → the open question is timing, not whether.

## Bottleneck durability / resolution risk

- **Self-correcting by design:** the cure for high memory prices is high memory prices — the three suppliers'
  capacity additions (and China's long-run entry) will eventually ease the shortage. The historical memory
  cycle is exactly this: shortage → price spike → capacity flood → glut → price collapse.
- **The AI-specific question:** can demand grow fast enough, for long enough, that supply never catches up
  within the investment horizon? The bull case is that AI memory demand is a multi-year secular step-change
  that outruns supply for years. The bear case is that this is the same cycle with a bigger amplitude, and
  the glut comes in 2026–2027 as HBM4 capacity floods in.

## Verdict

A **real, currently-acute memory bottleneck** that Micron genuinely participates in — but as a *supplier into*
the bottleneck (not its owner), in a product the customer multi-sources, in an industry whose bottlenecks
have always resolved via supply response. The bottleneck is real and the economics are real; the *durability*
of the bottleneck (and Micron's share of it) is the unresolved variable that the price is fully pricing as
permanent. Strong M2 signal on the dislocation being real; tempered by the supplier-not-owner + supply-
response dynamics.
