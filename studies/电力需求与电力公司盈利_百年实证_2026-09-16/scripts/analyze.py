#!/usr/bin/env python
"""Reproduce the core tables of the study from data/. Run from the study folder."""
import csv, io, json, math, re, collections, os, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")

def french():
    raw = open(f"{D}/ff12.csv", "rb").read().decode("utf8", "ignore").replace("\r", "")
    L = raw.split("\n"); i0 = next(i for i, l in enumerate(L) if l.strip().startswith(",NoDur"))
    hdr = [h.strip() for h in L[i0].split(",")]; rows = {}
    for l in L[i0 + 1:]:
        s = l.strip(); m = re.match(r"^(\d{6}),", s)
        if not m:
            if rows: break
            continue
        v = [float(x) for x in s.split(",")[1:]]
        if len(v) == len(hdr) - 1: rows[int(m.group(1))] = dict(zip(hdr[1:], v))
    raw2 = open(f"{D}/ff_factors.csv", "rb").read().decode("utf8", "ignore").replace("\r", "")
    F = raw2.split("\n"); j0 = next(i for i, l in enumerate(F) if l.strip().startswith(",Mkt-RF"))
    cols = [c.strip() for c in F[j0].split(",")]; fac = {}
    for l in F[j0 + 1:]:
        s = l.strip(); m = re.match(r"^(\d{6}),", s)
        if not m:
            if fac: break
            continue
        a = s.split(","); fac[int(m.group(1))] = {c: float(a[i]) for i, c in enumerate(cols) if i}
    U = {k: v["Utils"] for k, v in rows.items()}
    M = {k: fac[k]["Mkt-RF"] + fac[k]["RF"] for k in fac if k in rows}
    RF = {k: fac[k]["RF"] for k in fac}
    return rows, U, M, RF

def cum(s, a, b):
    g, n = 1.0, 0
    for k in sorted(s):
        if a * 100 + 1 <= k <= b * 100 + 12: g *= 1 + s[k] / 100; n += 1
    return g, n

def ann(g, n): return g ** (12 / n) - 1

def eia(t):
    d = collections.defaultdict(dict)
    for r in csv.DictReader(io.open(f"{D}/eia_{t}.csv", encoding="utf8")):
        if r["YYYYMM"][-2:] != "13": continue
        try: d[r["MSN"]][int(r["YYYYMM"][:4])] = float(r["Value"])
        except ValueError: pass
    return d

ERAS = [(1926, 1929), (1930, 1934), (1935, 1949), (1950, 1969), (1970, 1981), (1982, 1999),
        (2000, 2002), (2003, 2007), (2008, 2019), (2020, 2022), (2023, 2026)]

if __name__ == "__main__":
    rows, U, M, RF = french()
    print("== Utils vs Market by era ==")
    for a, b in ERAS:
        gu, n = cum(U, a, b); gm, _ = cum(M, a, b)
        print(f"{a}-{b}  utils {ann(gu,n):+.1%}  mkt {ann(gm,n):+.1%}  excess {ann(gu,n)-ann(gm,n):+.1%}")
    gu, n = cum(U, 1926, 2026); gm, _ = cum(M, 1926, 2026)
    print(f"full  utils {ann(gu,n):.2%}  mkt {ann(gm,n):.2%}  $1-> {gu:,.0f} vs {gm:,.0f}")
    gen = eia("T07.01")["ELETPUS"]
    print("\n== Demand CAGR vs excess return ==")
    pairs = []
    for a, b in ERAS:
        a2, b2 = max(a, 1949), min(b, 2025)
        if b2 <= a2: continue
        g = (gen[b2] / gen[a2]) ** (1 / (b2 - a2)) - 1
        gu, n = cum(U, a, b); gm, _ = cum(M, a, b); pairs.append((g, ann(gu, n) - ann(gm, n)))
        print(f"{a}-{b}  gen CAGR {g:+.2%}  excess {pairs[-1][1]:+.1%}")
    xs, ys = [p[0] for p in pairs], [p[1] for p in pairs]
    mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
    r = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / math.sqrt(sum((x - mx) ** 2 for x in xs) * sum((y - my) ** 2 for y in ys))
    print(f"r = {r:+.2f}")
