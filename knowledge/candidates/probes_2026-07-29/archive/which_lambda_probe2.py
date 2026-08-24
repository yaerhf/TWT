"""WHICH-LAMBDA probe, part 2 (2026-07-29): the functional-independence test done
with the FULL second D4 shell (both triality-related orbits at equal weight, so
(P-pg) holds and the quartic stays isotropic -- probe 1 used only {+-2e_i}, a single
W(D4) orbit, which breaks degree-4 isotropy).  READ-ONLY.
"""
import math, itertools
import numpy as np
import sympy as sp

nn = []
for i, j in itertools.combinations(range(4), 2):
    for si in (1, -1):
        for sj in (1, -1):
            v = [0, 0, 0, 0]; v[i], v[j] = si, sj
            nn.append(tuple(v))
sh2_a = [tuple((s * 2 if k == i else 0) for k in range(4)) for i in range(4) for s in (1, -1)]
sh2_b = [t for t in itertools.product((1, -1), repeat=4)]
sh2 = sh2_a + sh2_b
assert len(nn) == 24 and len(sh2_a) == 8 and len(sh2_b) == 16 and len(sh2) == 24

Ng = 24
xs = 2 * math.pi * (np.arange(Ng) + 0.5) / Ng
ax = [xs.reshape([Ng if k == m else 1 for k in range(4)]) for m in range(4)]


def c_lat_of(bs, ws):
    tot = np.zeros((Ng,) * 4); m2 = 0.0
    for b, w in zip(bs, ws):
        tot += w * (1.0 - np.cos(sum(bi * a_ for bi, a_ in zip(b, ax) if bi != 0)))
        m2 += w * b[0] ** 2
    q = tot / (m2 / 2.0)
    return 16 * math.pi ** 2 * 0.5 * float((1.0 / q).mean())


def quartic(bs, ws, direction):
    t = sp.symbols('t')
    n = sp.Matrix(direction); n = n / sp.sqrt((n.T * n)[0])
    m2 = sum(w * b[0] ** 2 for b, w in zip(bs, ws))
    expr = sum(w * (1 - sp.cos(t * sum(sp.Integer(bi) * n[i] for i, bi in enumerate(b))))
               for b, w in zip(bs, ws)) / (sp.Rational(1, 2) * m2)
    p = sp.Poly(sp.expand(sp.series(sp.expand(expr), t, 0, 7).removeO()), t)
    return sp.nsimplify(p.coeff_monomial(t ** 2)), sp.nsimplify(p.coeff_monomial(t ** 4))

D1, D2 = [1, 0, 0, 0], [1, 2, 3, 5]
print("FULL-SHELL DEFORMATION (P-pg respected: both triality orbits at equal weight)")
print(" %7s | %9s | %11s | %11s | %9s | %9s"
      % ("w(2nd)", "c_lat", "c4 (axis)", "c4 (generic)", "ratio c_lat", "ratio c4"))
base = None
for w2 in (0.0, 0.05, 0.15, 0.30, 0.60, 1.00):
    bs = nn + sh2
    ws = [1.0] * 24 + [w2] * 24
    cl = c_lat_of(bs, ws)
    _, c4a = quartic(bs, ws, D1)
    _, c4g = quartic(bs, ws, D2)
    assert sp.simplify(c4a - c4g) == 0, "quartic must be ISOTROPIC with the full shell"
    if base is None:
        base = (cl, float(c4a))
    print(" %7.2f | %9.4f | %11s | %11s | %9.4f | %9.4f"
          % (w2, cl, c4a, c4g, cl / base[0], float(c4a) / base[1]))

print()
print("VERDICT: with (P-pg) intact the quartic is isotropic at every weight (asserted),")
print("and c_lat and the quartic coefficient scale by DIFFERENT factors -- so they are")
print("two independent functionals of the same band, not one number in two conventions.")

print()
print("Direction check on the PURE-NN band (probe-1 value, isotropy of the quartic):")
for d in ([1, 0, 0, 0], [1, 1, 0, 0], [1, 1, 1, 1], [1, 2, 3, 5]):
    print("   direction %-12s -> c2=%s, c4=%s" % (d, *quartic(nn, [1.0] * 24, d)))

print()
print("Single-orbit (P-pg VIOLATED) contrast, {+-2e_i} only at w=0.6:")
bs = nn + sh2_a; ws = [1.0] * 24 + [0.6] * 8
for d in ([1, 0, 0, 0], [1, 1, 1, 1]):
    print("   direction %-12s -> c2=%s, c4=%s" % (d, *quartic(bs, ws, d)))
print("   (direction-dependent c4 == the restored dim-6 ANISOTROPY N52 warns about)")
