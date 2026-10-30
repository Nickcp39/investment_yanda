# -*- coding: utf-8 -*-
"""HWM 2026-10-30 — independent Checker calculations (reproducible, no network).

Run:  python companies/hwm/2026-10-30/checker_calc.py
Sections:
  phase_a()  — blind estimate. Logic identical to scratchpad phaseA_calc.py (sha256 e290c5e7...),
               written and run BEFORE any Runner judgement file was opened (locked 2026-10-30 09:39:44 EDT).
  phase_b()  — independent re-run of the Runner's buy_below ladder + method grid (a)(b)(c) + break-evens.
  phase_c()  — Checker buy_below grid used for the ruling.
All inputs are from raw/ primary text (10-K FY25, 10-Qs, EX-99.1s, price JSON) unless marked JUDGEMENT/ESTIMATE.
"""

P0 = 205.94          # 2026-10-29 close (raw/price_nasdaq_historical, raw/price_yahoo_v8_1y)
S0 = 397.660490      # M shares, Q3'26 10-Q cover, as of 2026-10-26

# ------------------------------------------------------------------ Phase A
ocf = 654 + 1745               # Q4'25 EX-99.1 FCF recon 654; Q3'26 EX-99.1 9M 1,745
capx = 124 + 345
fcf = ocf - capx
sbc = (73 - 59) + 80           # FY25 CF 73; 9M25 59; 9M26 80
da = (283 - 210) + 251
adj_ni = 426 + 1612            # Q4'25 NI ex special items; 9M26 adj NI
gaap_ni = 372 + 1681
adj_eps_ttm = 1.05 + 4.01
rev_ttm = (8252 - 6084) + 7563
# other-customer-receivable sales outstanding: 9/30/25 = 231 (Q3'25 10-Q); 9/30/26 NOT disclosed. ESTIMATE:
fact_lo, fact_hi = 257 - 231, 372 - 231
fact_mid = (fact_lo + fact_hi) / 2
acq_cash_costs = 30            # JUDGEMENT: cash part of $36M 9M26 acquisition-related costs
oe0_ttm = fcf - sbc - fact_mid + acq_cash_costs
sbc26 = 80 / 0.75
oe0_fy26 = 2000 - sbc26 - fact_mid + acq_cash_costs
adj_ni_26 = 1612 + 1.50 * 399  # 9M adj NI + Q4 guide baseline x ~399M diluted
rev26 = 10300
m26 = adj_ni_26 / rev26


def path(g, m_end, buyback, conv_path=None):
    rev, out, S = rev26, [], S0
    for t in range(1, 6):
        rev *= (1 + g[t - 1])
        m = m26 + (m_end - m26) * t / 5
        ni = rev * m
        S *= (1 - buyback)
        conv = conv_path[t - 1] if conv_path else None
        out.append(dict(yr=2026 + t, rev=rev, m=m, ni=ni, S=S, eps=ni / S,
                        oe_ps=(ni * conv) / S if conv else None))
    return out


def irr(cfs):
    lo, hi = -0.9, 1.0
    for _ in range(200):
        mid = (lo + hi) / 2
        v = sum(cf / (1 + mid) ** t for t, cf in enumerate(cfs))
        lo, hi = (mid, hi) if v > 0 else (lo, mid)
    return mid


def scen_irr(p, price, mult, payout=0.10, use='eps', divs=True):
    cfs = [-price]
    for i, y in enumerate(p):
        d = payout * y['eps'] if divs else 0.0
        cfs.append(d + (mult * (y['eps'] if use == 'eps' else y['oe_ps']) if i == 4 else 0))
    return irr(cfs)


def threshold(p, mult, hurdle=0.08, payout=0.10, use='eps', divs=True):
    pv = 0.0
    for i, y in enumerate(p):
        d = payout * y['eps'] if divs else 0.0
        cf = d + (mult * (y['eps'] if use == 'eps' else y['oe_ps']) if i == 4 else 0)
        pv += cf / (1 + hurdle) ** (i + 1)
    return pv


conv_base = [0.86, 0.86, 0.88, 0.90, 0.91]   # JUDGEMENT: (FCF-SBC)/adjNI while capex elevated
conv_bear = [0.84, 0.84, 0.86, 0.88, 0.88]
conv_bull = [0.88, 0.89, 0.91, 0.92, 0.93]
SCEN = {   # JUDGEMENT
    'bear': dict(g=[0.08, 0.02, -0.04, 0.04, 0.05], m=0.19, bb=0.010, pe=20, poe=20, conv=conv_bear),
    'base': dict(g=[0.11, 0.10, 0.09, 0.08, 0.07], m=0.225, bb=0.015, pe=27, poe=25, conv=conv_base),
    'bull': dict(g=[0.13, 0.13, 0.12, 0.11, 0.10], m=0.245, bb=0.015, pe=34, poe=30, conv=conv_bull),
}


def phase_a():
    print('== Phase A (blind)')
    print(f"TTM rev {rev_ttm} OCF {ocf} capex {capx} FCF {fcf} SBC {sbc} D&A {da} capex/D&A {capx/da:.2f}")
    print(f"TTM adjNI {adj_ni} GAAP NI {gaap_ni} adjEPS {adj_eps_ttm:.2f} FCF-SBC {fcf-sbc} ({(fcf-sbc)/adj_ni:.0%} of adjNI); "
          f"factoring-adjusted {(fcf-sbc-fact_mid)/adj_ni:.0%}")
    print(f"factoring tailwind est {fact_lo}..{fact_hi} mid {fact_mid:.0f}")
    print(f"OE0 TTM {oe0_ttm:.0f} (/sh {oe0_ttm/S0:.2f}); OE0 FY26E {oe0_fy26:.0f} (/sh {oe0_fy26/S0:.2f})")
    print(f"mkt cap {P0*S0/1000:.1f}B  P/FY26 adjEPS {P0/5.50:.1f}x  P/TTM {P0/adj_eps_ttm:.1f}x  P/OE0(FY26E) {P0/(oe0_fy26/S0):.1f}x")
    for k, s in SCEN.items():
        p = path(s['g'], s['m'], s['bb'], s['conv'])
        y = p[-1]
        print(f"{k}: EPS31 {y['eps']:.2f} (CAGR {(y['eps']/5.5)**0.2-1:.1%}) | IRR eps@{s['pe']}x {scen_irr(p, P0, s['pe']):.1%} "
              f"| IRR oe@{s['poe']}x {scen_irr(p, P0, s['poe'], use='oe'):.1%} | 8% px eps {threshold(p, s['pe']):.0f} "
              f"(no div {threshold(p, s['pe'], divs=False):.0f}) oe {threshold(p, s['poe'], use='oe'):.0f}")
    pb = path(SCEN['base']['g'], SCEN['base']['m'], SCEN['base']['bb'], SCEN['base']['conv'])
    print('base 8% line vs exit P/E:', {m: round(threshold(pb, m)) for m in (20, 24, 27, 30, 32, 35)})
    lo, hi = 10, 60
    for _ in range(100):
        mid = (lo + hi) / 2
        lo, hi = (lo, mid) if scen_irr(pb, P0, mid) > 0.08 else (mid, hi)
    print(f"base: exit P/E (FY2031 EPS) needed for 8% at {P0} = {mid:.1f}x")


# ------------------------------------------------------------------ Phase B
H = 1.08 ** 5


def runner_eps30(anchor, g27, g_rest, m0, m1=34.0, bb=0.01):
    # Runner's reconstructed structure (valuation.md §2); Runner computes buyback as 1/(1-1%)^4
    return anchor * (1 + g27) * (1 + g_rest) ** 3 * (m1 / m0) / (1 - bb) ** 4


def phase_b():
    print('\n== Phase B: Runner ladder re-run')
    print('Step0', round(8.0 * 32 / H, 2))
    e1 = runner_eps30(5.50, 0.10, 0.10, 32.0)
    e2 = runner_eps30(5.50, 0.10, 0.10, 32.3)
    e3 = runner_eps30(5.50, 0.12, 0.10, 32.3)
    cagr = (e3 / 5.50) ** 0.25 - 1
    e4 = e3 * (1 + cagr) ** (129 / 365)
    for n, e in (('Step1', e1), ('Step2', e2), ('Step3', e3), ('Step4 roll', e4)):
        print(f"{n}: EPS {e:.3f} line {e*32/H:.2f}")
    print(f"roll factor {(1+cagr)**(129/365):.4f} (EPS CAGR {cagr:.2%})")
    print(f"base IRR Runner formula: {(e4*32/P0)**0.2-1+0.0027:.2%} (price-only {(e4*32/P0)**0.2-1:.2%})")
    print('-- method grid: (a) 2027 guide  x  (b) roll B/A/C  x  (c) dividends (exact PV of $0.56/yr growing)')
    vals = []
    for use_guide in (True, False):
        for roll in ('B', 'A', 'C'):
            for div in (False, True):
                e = runner_eps30(5.50, 0.12 if use_guide else 0.10, 0.10, 32.3)
                c = (e / 5.5) ** .25 - 1
                ee, yrs = {'B': (e * (1 + c) ** (129 / 365), 5.0), 'A': (e, 5 - 129 / 365), 'C': (e, 5.0)}[roll]
                v = ee * 32 / 1.08 ** yrs
                if div:
                    v += sum(0.56 * (1 + c) ** t / 1.08 ** t for t in range(1, 6))
                vals.append(v)
                print(f"  guide={use_guide!s:5} roll={roll} div={div!s:5} -> {v:.1f}")
    print(f"method range {min(vals):.1f} .. {max(vals):.1f}")
    fy31 = e3 * (1 + cagr)
    print(f"Runner exit EPS = {e4/fy31:.3f} x FY2031 EPS -> Runner 32x = {32*e4/fy31:.1f}x on FY2031 EPS (Checker basis)")
    for conv in (0.86, 0.90, 0.95):
        poe = 32 / conv
        print(f"  conv {conv:.2f}: 32x P/E = {poe:.1f}x P/OE -> implied perpetual g at 8% = {(0.08*poe-1)/(poe+1):.2%}")
    print(f"Runner structure: exit P/E needed at {P0}: price-only {P0*H/e4:.2f}x; incl. 0.27% yield {P0*(1.08-0.0027)**5/e4:.2f}x")
    for pe in (25, 27, 28, 30, 32):
        print(f"  Runner EPS {e4:.2f} x {pe}x -> line {e4*pe/H:.1f}")
    # HWM own P/E history: adj EPS from Q4 EX-99.1s (FY21 8-K 0001157523-22-000133; FY23 0001157523-24-000226;
    # FY24 0001104659-25-012529; FY25/26 raw/), avg monthly close from Yahoo v8 range=10y interval=1mo (fetched 2026-10-30)
    hist = {2021: (31.0, 1.01), 2022: (35.0, 1.40), 2023: (46.6, 1.84), 2024: (86.7, 2.69), 2025: (171.1, 3.77), 2026: (239.5, 5.50)}
    print('HWM avg price / same-year adj EPS:', {y: f"{p/e:.1f}x" for y, (p, e) in hist.items()})


# ------------------------------------------------------------------ Phase C
def phase_c():
    print('\n== Phase C: Checker buy_below grid (8%, price-only = dividends excluded in both IRR and line)')
    grids = {'checker_g': [0.11, 0.10, 0.09, 0.08, 0.07],
             'guide_then_taper': [0.12, 0.10, 0.09, 0.08, 0.07],
             'runner_like_g': [0.12, 0.10, 0.10, 0.10, 0.10]}
    for gname, g in grids.items():
        p = path(g, 0.225, 0.015, conv_base)
        print(f"{gname:17} EPS31 {p[-1]['eps']:.2f} " + ' '.join(
            f"{pe}x:{threshold(p, pe, divs=False):.0f}" for pe in (25, 27, 28, 29.6, 32)))
    p = path(grids['guide_then_taper'], 0.225, 0.015, conv_base)
    print(f"POINT (guide_then_taper, 27x FY2031, no div): {threshold(p, 27, divs=False):.0f}")
    print(f"OE lens (same path, 25x P/OE, no div): {threshold(p, 25, use='oe', divs=False):.0f}")


if __name__ == '__main__':
    phase_a()
    phase_b()
    phase_c()
