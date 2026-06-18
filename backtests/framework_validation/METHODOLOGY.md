# Position & Cash Management Methodology

Date: 2026-06-17
Status: canonical methodology (v1). Consolidates and supersedes the "one-page card" sections of
`notes/2026-06-17_position_cash_management_source_notes.md` and `notes/2026-06-17_simple_position_rules_draft.md`
(those remain as sourced background). The pipeline's Portfolio Controller and scorer implement this.

---

## 速记卡 (TL;DR)

- **一条原则**:仓位跟着"已兑现的信念"走,不跟着故事走。小仓试 → 确认才加 → 证伪砍回现金。
- **盘形**:集中 3–5 个真仓;BTC 算核心仓。
- **阶梯**:跟踪 0.5–1% → 起步 3–5% → 确认 8–12% → 核心 15–25%(罕见 ~30%)。天花板由"耐久性"定,不只由"确认"定。
- **现金**:默认接近满仓,**留 ~5% 机会仓**;新/加仓主要靠换仓(卖弱买强);没好标的时现金可自然漂高,但不设目标。
- **卖出**:只 4 个理由(看错 / 贵到离谱 / 有更好的要用钱 / 论点证伪砍回现金)。不为"仓位大了"削赢家。
- **铁律**:不借钱、不裸期权、不做空、不天天择时;3–5 个名字不能都押同一件事。

---

## Core principle

**Size follows earned conviction, not the story.** Enter small to test, add only when the thesis is
confirmed, cut back to cash/tracking when it is disproven. Cash is a residual, not a target.

Why this is the spine: Duan Yongping (value) and the USIC champions — Minervini / D. Ryan / S. Ryan /
J Law / Clement Ang (momentum) — run opposite styles, yet both do exactly this. That cross-style
convergence is the evidence it is robust. Momentum confirms via price; we confirm via fundamentals.

## 1. Book shape (Decisions A + B)

- Concentrated: **3–5 real positions** (Decision A: more concentrated → high ceiling).
- **BTC is a core position** (occupies a slot, eligible for the full core ceiling) (Decision B).
- A name is "real" only at Starter or above. **Tracking does not count toward the 3–5.**

## 2. Position ladder — size by earned conviction

| Tier | Weight | Unlocks when |
|---|---:|---|
| Tracking | 0.5–1% | Not yet understood; buy a sliver to force attention (Duan). Not a bet, not a slot. |
| Starter | 3–5% | Thesis is sound; real money, still testing. |
| Confirmed | 8–12% | First confirmation in (fundamentals delivering). |
| Core conviction | 15–25% | Understood + cheap/fair + **durable**. (BTC, GOOGL belong here.) |
| Rare max | ~30% | Let a proven winner run. Exceptional only. |

**The ceiling is set by DURABILITY, not just by confirmation.** A confirmed *cyclical* (e.g. a NAND
recovery) caps around Confirmed (~10–15%); the 15–25% Core tier is reserved for businesses you would
hold 5–10 years. Durability also includes the **founder / core-team life-arc** grade
(see `../../companies/_operator_underwriting_template.md` → *Founder & Core Team Life-Arc*): a proven,
cohesive, values-consistent long-arc team raises the ceiling; a fragile / one-person / misaligned team
lowers it. (N/A for BTC — no operator; map to protocol governance instead.)

## 3. Cash (Decision C: ~5% opportunity reserve — NOT a 25% band)

- **No cash target. Default ≈ fully invested.** (Duan: cash loses to inflation over the long run; his
  own scale calls 50% cash "empty," and reaching meaningful cash was a once-in-a-career event.)
- Keep **~5% as an opportunity reserve** — to average into a conviction or grab a dislocation fast
  without first having to sell.
- **Primary funding for new / larger ideas = rotation:** sell the weakest-conviction holding to fund a
  better one ("sell weak, buy strong").
- Cash may **drift above ~5% only as a residual** when genuinely nothing clears the bar. Do not
  force-deploy; do not target a high level either.
- Accepted trade-off: at ~5% cash you fund by rotation and **hold convictions through drawdowns**
  (you are concentrated and never forced to sell), rather than holding dry powder to trade dips.

> Note: this replaces the earlier draft `target_cash = 25%, band 20–30%`. The 25% band was a
> war-chest / progressive-exposure choice, not Duan's actual behaviour; Decisions A+C move us to the
> Duan "near-full, cash is residual" model with a small opportunistic buffer.

## 4. Sell / trim — only four triggers

1. The thesis is **wrong** (you misjudged the business).
2. Price is **absurd** vs. value.
3. A **clearly better idea** needs the capital (rotation).
4. The thesis is **disconfirmed → cut back to cash/tracking immediately** (the discipline Duan is weak
   on, borrowed from the champions — do not死扛 a broken thesis).

Do **not** trim a winner just because its weight got large. High weight is not a sell reason (Duan let
Apple run to ~60%; Buffett's Apple trims were structure / tax driven, which do not apply to us).

## 5. Hard constraints

- No leverage, no naked options, no shorting, no constant market-timing.
- **Your 3–5 names must not all depend on one factor.** (Today BTC / GOOGL / NBIS all ride
  "AI + liquidity" — that is a hidden single bet. New names should diversify the factor, not double it.)
  One-line judgement check, no covariance math.
- Define risk as **"loss if the thesis is wrong / drawdown to fair value" + "can it go bankrupt"** —
  not stop-distance (we are value, not momentum).
- Optional waiting tool: cash-secured puts / limit orders at your buy price — only at prices where
  assignment is welcome, fully cash-covered, and **never on a true fat pitch** (just buy that).

## 6. Worked example — SNDK (2025-06-16)

The old pipeline said BUY but capped it at 1.5%. Direction right, size wrong. Under this methodology:

```
2025-06-16   M2 +2, M6 +2, no veto, survivable balance sheet
             -> conviction not yet earned (spin-off + cyclical + unconfirmed)
             -> Starter 3-4%
Q4 FY25      gross margin / revenue confirm
             -> add to Confirmed 8-10%
later        enterprise / cloud demand + pricing confirm
             -> max ~12-15% (cyclical -> capped below Core)
disproven    margins roll over / demand was just restocking
             -> cut back to cash
```

## 7. Pipeline changes this methodology requires (the 3 fixes)

1. **M6 outputs raw attractiveness + asymmetry + stage + risk — it does NOT set final size.**
   Remove the "uncertainty haircut as a hard ceiling" that pinned SNDK to 1.5%.
2. **Add a Portfolio Controller** that combines M6 output with: the ladder, the ~5% reserve + rotation
   funding rule, the durability ceiling, and the one-factor check → outputs `target_weight`,
   `funding_source`, and `add/trim trigger`.
3. **Split the score:** grade `initial_size` and `post-confirmation add discipline` separately. A winner
   identified only as a tiny STARTER is **not** full marks — "right direction, too small" must lose points.

---

Sources: see the two 2026-06-17 notes files in `notes/` for the verifiable primary sources behind each
borrowed mechanism (Duan Yongping, Munger, Buffett partnership era, Druckenmiller/Soros, Greenblatt,
Cboe PutWrite, USIC champions).
