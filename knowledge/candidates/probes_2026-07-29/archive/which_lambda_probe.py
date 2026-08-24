"""WHICH-LAMBDA probe (2026-07-29). READ-ONLY analysis; nothing here is banked.

Question: Lambda_eff = sqrt(2 pi) M_Pl (Sakharov coefficient) vs 1/a ~ 0.537 M_Pl
(lattice dispersion). Same object in two conventions, or two different quantities?
"""
import math, itertools
import numpy as np
import sympy as sp

MPL = 1.220910e19  # GeV, non-reduced
N_EFF = 6

print("=" * 78)
print("(A) THE TWO OBJECTS, DEFINED FROM THEIR OWN DEFINING EQUATIONS")
print("=" * 78)

# --- Lambda_eff: defined by DEMANDING the textbook Sakharov form reproduce measured G.
#     1/(16 pi G) = N_eff * Lambda_eff^2 / (192 pi^2)   [sakharov: G^-1 = N_eff L^2/(12 pi)]
#     with 1/G = M_Pl^2 (non-reduced).
L, Mpl, clat, a, Neff = sp.symbols('Lambda_eff M_Pl c_lat a N_eff', positive=True)
eq_sak = sp.Eq(Mpl**2 / (16 * sp.pi), Neff * L**2 / (192 * sp.pi**2))
sol_L = sp.solve(eq_sak, L)[0]
print("  Lambda_eff solved from the Sakharov identity :", sp.simplify(sol_L))
print("  at N_eff = 6                                 :",
      sp.simplify(sol_L.subs(Neff, 6)), "=", float(sol_L.subs({Neff: 6, Mpl: 1})))
assert abs(float(sol_L.subs({Neff: 6, Mpl: 1})) - math.sqrt(2 * math.pi)) < 1e-12

# --- a: defined by DEMANDING the DERIVED D4 band integral reproduce measured G.
#     1/(16 pi G) = N_eff * c_lat / (192 pi^2 a^2)      [R-163 step 5]
eq_band = sp.Eq(Mpl**2 / (16 * sp.pi), Neff * clat / (192 * sp.pi**2 * a**2))
sol_a = sp.solve(eq_band, a)[0]
print("  a solved from the R-163 band identity        :", sp.simplify(sol_a))
inv_a = sp.simplify(1 / sol_a)
print("  => 1/a                                       :", inv_a)

ratio = sp.simplify(sol_L / inv_a)
print("  => Lambda_eff / (1/a)                        :", ratio, "  <-- EXACT, symbolic")
assert sp.simplify(ratio - sp.sqrt(clat)) == 0
print("  VERIFIED: Lambda_eff = sqrt(c_lat) * (1/a) IDENTICALLY, all N_eff, all M_Pl.")

# --- c_lat-(in)dependence
print()
print("  Lambda_eff depends on c_lat? ", sp.simplify(sp.diff(sol_L, clat)) != 0)
print("  1/a        depends on c_lat? ", sp.simplify(sp.diff(inv_a, clat)) != 0)
print("  Lambda_eff/M_Pl (N=6) is the pure number sqrt(2 pi) = %.6f" %
      math.sqrt(2 * math.pi))
f_inv_a = sp.lambdify((clat,), inv_a.subs({Neff: 6, Mpl: 1}))
for cl in (1.0, 11.65, 21.83, 42.06, 100.0):
    print("    c_lat = %7.2f  ->  1/a = %.4f M_Pl   (Lambda_eff stays %.4f M_Pl)"
          % (cl, f_inv_a(cl), math.sqrt(2 * math.pi)))

print()
print("=" * 78)
print("(B) WHAT KIND OF OBJECT IS EACH? -- the informational test")
print("=" * 78)
print("  Lambda_eff = sqrt(12 pi / N_eff) * M_Pl.")
print("    Inputs: measured G, N_eff, and the CHOICE of the textbook proper-time a_1 scheme.")
print("    Substrate lattice inputs: NONE. It cannot move when the lattice moves.")
print("  1/a        = sqrt(12 pi / (N_eff c_lat)) * M_Pl.")
print("    Inputs: measured G, N_eff, AND c_lat = 16 pi^2 * int_BZ d^4k/(2pi)^4 / ktil^2(k).")
print("    Substrate lattice input: c_lat -- a Brillouin-zone integral of the DERIVED band.")

print()
print("=" * 78)
print("(C) ARE THEY FUNCTIONALLY INDEPENDENT? -- deform the kernel and watch")
print("=" * 78)
# D4 nearest-neighbour bonds (24 roots)
bonds = []
for i, j in itertools.combinations(range(4), 2):
    for si in (1, -1):
        for sj in (1, -1):
            v = [0, 0, 0, 0]; v[i], v[j] = si, sj
            bonds.append(tuple(v))
assert len(bonds) == 24
shell2 = [tuple(2 if k == i else 0 for k in range(4)) for i in range(4) for _ in (0,)]
shell2 = [tuple(s * (2 if k == i else 0) for k in range(4)) for i in range(4) for s in (1, -1)]

Ng = 24
xs = 2 * math.pi * (np.arange(Ng) + 0.5) / Ng
ax = [xs.reshape([Ng if k == m else 1 for k in range(4)]) for m in range(4)]


def band(bs, weights):
    """ktil^2(k) normalized so ktil^2 -> k^2 as k->0 (2nd moment = 12 delta convention)."""
    tot = np.zeros((Ng,) * 4)
    m2 = 0.0
    for b, w in zip(bs, weights):
        tot += w * (1.0 - np.cos(sum(bi * a_ for bi, a_ in zip(b, ax) if bi != 0)))
        m2 += w * b[0] ** 2          # 2nd moment along axis 0 (isotropic sets)
    return tot / (m2 / 2.0)          # (1-cos) ~ x^2/2  =>  divide by m2/2


def c_lat_of(bs, weights):
    q = band(bs, weights)
    return 16 * math.pi ** 2 * 0.5 * float((1.0 / q).mean())


def quartic_coeff(bs, weights):
    """Coefficient c in ktil^2(k) = k^2 + c*(k^2)^2 + ..., EXACT via sympy along a
    generic direction (isotropy of the quartic is R-165's degree-4 invariant result)."""
    t = sp.symbols('t')
    n = sp.Matrix([1, 2, 3, 5]); n = n / sp.sqrt((n.T * n)[0])   # generic direction
    m2 = sum(w * b[0] ** 2 for b, w in zip(bs, weights))
    expr = sum(w * (1 - sp.cos(t * sum(sp.Integer(bi) * n[i] for i, bi in enumerate(b))))
               for b, w in zip(bs, weights)) / (sp.Rational(1, 2) * m2)
    ser = sp.series(sp.expand(expr), t, 0, 7).removeO()
    p = sp.Poly(sp.expand(ser), t)
    c2 = sp.simplify(p.coeff_monomial(t ** 2))    # = 1 by construction
    c4 = sp.simplify(p.coeff_monomial(t ** 4))    # = c  (since (k^2)^2 -> t^4)
    return sp.nsimplify(c2), sp.nsimplify(c4)


w_nn = [1.0] * 24
c2, c4 = quartic_coeff(bonds, w_nn)
print("  PURE NN D4 band:  ktil^2 = %s*k^2 + (%s)*(k^2)^2 + ...   [a = 1 units]" % (c2, c4))
print("     -> c_lat = %.4f ;  quartic coefficient c = %s = %.6f"
      % (c_lat_of(bonds, w_nn), c4, float(c4)))

print()
print("  Now add a SECOND-SHELL coupling with weight w (same D4 point group, still")
print("  degree-4 isotropic by R-165). Watch the two numbers move independently:")
print("   %8s | %10s | %14s | %12s" % ("w(2nd)", "c_lat", "quartic c", "sqrt(c_lat)"))
rows = []
for w2 in (0.0, 0.05, 0.15, 0.30, 0.60):
    bs = bonds + shell2
    ws = [1.0] * 24 + [w2] * len(shell2)
    cl = c_lat_of(bs, ws)
    _, cq = quartic_coeff(bs, ws)
    rows.append((w2, cl, float(cq)))
    print("   %8.2f | %10.4f | %14.6f | %12.4f" % (w2, cl, float(cq), math.sqrt(cl)))
r0, r1 = rows[0], rows[-1]
print("  ratio moves:  c_lat x%.3f   vs   |quartic c| x%.3f   -- NOT a common rescaling"
      % (r1[1] / r0[1], abs(r1[2] / r0[2])))

print()
print("=" * 78)
print("(D) WHICH SCALE SITS IN THE dim-6 LV OPERATOR? -- read it off the dispersion")
print("=" * 78)
print("  Restore the spacing a: k -> a*k, omega^2 = ktil^2(a k)/a^2 gives")
print("      E^2 = p^2 + c * a^2 * p^4 + O(a^4 p^6),   c = %s (pure NN)" % c4)
print("  i.e.  E^2 = p^2 + c * p^4 / (1/a)^2 .")
print("  The denominator is (1/a)^2 -- the INVERSE MONAD SPACING -- because the ONLY")
print("  length in a finite-difference kernel's Taylor expansion is the bond length.")
print("  c_lat never appears: it is a BZ *integral*, the k->0 expansion cannot see it.")
print("  Consequence (arithmetic):  eta4 = c * (M_Pl / (1/a))^2 = c * (a M_Pl)^2 .")

print()
print("=" * 78)
print("(E) THE NUMBERS THAT MOVE")
print("=" * 78)
KAP = (11.65, 42.06)                      # OA-LF-ii O(1) band on c_lat, from the engine
c_lat_c = 21.8285
inv_a_c = f_inv_a(c_lat_c)
inv_a_lo, inv_a_hi = f_inv_a(KAP[1]), f_inv_a(KAP[0])   # bigger c_lat -> smaller 1/a
print("  central   1/a = %.4f M_Pl  (c_lat = %.2f)" % (inv_a_c, c_lat_c))
print("  OA-LF-ii  1/a in [%.4f, %.4f] M_Pl" % (inv_a_lo, inv_a_hi))
print()


def orders(eta_lo, eta_hi):
    bounds = {"photon 1e-8": 1e-8, "electron 1e-6": 1e-6, "proton(sub) 1e-3": 1e-3}
    out = {}
    for nm, b in bounds.items():
        out[nm] = (math.log10(eta_lo / b), math.log10(eta_hi / b))
    return out


for label, lo, hi in (("CURRENT bracket Lambda in [0.13,2.5]", 0.13, 2.5),
                      ("PROPOSED 1/a band [%.3f,%.3f]" % (inv_a_lo, inv_a_hi), inv_a_lo, inv_a_hi)):
    e_lo, e_hi = (1.0 / hi) ** 2, (1.0 / lo) ** 2
    o = orders(e_lo, e_hi)
    allo = [v for pair in o.values() for v in pair]
    print("  %s" % label)
    print("     eta4 at c=1 : [%.3g, %.3g]" % (e_lo, e_hi))
    for nm, (a1, b1) in o.items():
        print("        vs %-18s : %.1f .. %.1f orders" % (nm, a1, b1))
    print("     => headline span: %.1f to %.1f orders  (rounded: %d to %d)"
          % (min(allo), max(allo), math.floor(min(allo)), math.ceil(max(allo))))
    print()

# dim-8 anisotropy row
E = 1.0e11
print("  dim-8 anisotropy (E/Lambda)^4 at E = 1e11 GeV:")
for label, lo, hi in (("current [0.13,2.5]", 0.13, 2.5),
                      ("1/a band", inv_a_lo, inv_a_hi)):
    print("     %-20s : %.2e (loose) ... %.2e (tight)"
          % (label, (E / (lo * MPL)) ** 4, (E / (hi * MPL)) ** 4))

# the NN-model value of c, as an aside
print()
print("  ASIDE (MODEL-DEPENDENT, canon SS3 -- the true c is #1-gap GATED):")
cnn = float(c4)
print("     pure-NN kernel gives c = %.6f (= %s), sign NEGATIVE (subluminal at high p)."
      % (cnn, c4))
print("     eta4 = c*(a M_Pl)^2 in [%.4f, %.4f]" % (cnn / inv_a_lo ** 2, cnn / inv_a_hi ** 2))
print("     |eta4| in [%.4f, %.4f]" % (abs(cnn / inv_a_hi ** 2), abs(cnn / inv_a_lo ** 2)))

print()
print("=" * 78)
print("(F) SIDE FINDING -- induced_G_bracket_mode_count normalization")
print("=" * 78)
print("  sakharov / R-163 / paper all use   1/(16 pi G) = N_eff Lambda^2/(192 pi^2)")
print("  induced_G_bracket_mode_count uses  1/(16 pi G) = N_eff Lambda^2/( 96 pi^2)")
print("  -> its back-fit Lambda/M_Pl = sqrt(6 pi/N_eff);  correct is sqrt(12 pi/N_eff).")
for nm, coef in (("bracket primitive (96 pi^2)", 6.0), ("sakharov/R-163/paper (192 pi^2)", 12.0)):
    ne = lambda r: coef * math.pi / r ** 2
    print("     %-34s: Lambda/M_Pl at N_eff=6 -> %.4f ; [0.13,2.5] -> N_eff [%d, %d]"
          % (nm, math.sqrt(coef * math.pi / 6), round(ne(2.5)), round(ne(0.13))))
print("  TELL: only the 192 pi^2 convention sends the sakharov branch Lambda=sqrt(2 pi) M_Pl")
print("        back to N_eff = 6 EXACTLY (%.6f). The 96 pi^2 one returns 3."
      % (12 * math.pi / (2 * math.pi)))
