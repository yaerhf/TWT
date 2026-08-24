"""PROBE 2 — c_reg for TWT's ACTUAL mode content.

The a_1 heat-kernel coefficient is a SIGNED weighted TYPE-sum, not a count. For a Laplace-type
operator D = -(nabla^2 + E) on a bundle V,
    a_1 = tr_V( E + (R/6) 1_V ),
and the induced EH coefficient from N real bosonic channels with proper-time cutoff Lambda is
    1/(16 pi G) = (1/2) * (Lambda^2/(16 pi^2)) * [a_1 / R]     (per unit volume, coefficient of R)
so in the paper's parametrization 1/(16 pi G) = c_reg * N_eff * Lambda^2/(16 pi^2),
    c_reg = (1/2) * (a_1/R) / N_eff.
For N_eff minimal scalars a_1/R = N_eff/6 => c_reg = 1/12. That is branch A's value.

QUESTION: is TWT's linear-face bundle E = 0 (scalar-like, a_1 = N R/6), or does it carry a
curvature endomorphism (2-form / so(4)-adjoint Weitzenbock)? We compute BOTH exactly on S^4 from
the exact spectra, with the same Richardson-in-s extraction the engine already uses.

READ-ONLY probe.
"""
import math
import numpy as np

Vol = 8 * math.pi**2 / 3.0     # unit S^4
Rcurv = 12.0                   # unit S^4 scalar curvature

def a1_from_spectrum(levels, svals=(1e-3, 5e-4), a0_expect=None):
    """levels: callable(lmax) -> list of (eigenvalue, degeneracy).
    Extract a_0 and a_1 from K(s) = (4 pi s)^-2 Vol (a_0 + s a_1 + ...) by Richardson in s."""
    F, A0 = [], []
    for s in svals:
        lmax = int(math.sqrt(200.0 / s)) + 60
        K = sum(d * math.exp(-s * lam) for lam, d in levels(lmax))
        x = K * (4 * math.pi * s)**2 / Vol          # = a_0 + s a_1 + O(s^2)
        A0.append(x)
        F.append((x - a0_expect) / s)
    a1 = 2 * F[1] - F[0]                            # Richardson in s
    a0 = 2 * A0[1] - A0[0]
    return a0, a1

print("=" * 78)
print("PROBE 2 — heat-kernel a_1 by MODE TYPE, exact S^4 spectra (R = 12, Vol = 8pi^2/3)")
print("=" * 78)

# ---------------------------------------------------------------- scalars
def scalars(lmax, n=1):
    return [(l * (l + 3), n * (l + 1) * (l + 2) * (2 * l + 3) / 6.0) for l in range(lmax + 1)]

a0, a1 = a1_from_spectrum(lambda L: scalars(L, 1), a0_expect=1.0)
print("\n[1] ONE real minimal scalar (E = 0), Delta = -nabla^2")
print("    a_0 = %.6f  (expect 1)" % a0)
print("    a_1 = %.6f  (expect R/6 = %.6f)" % (a1, Rcurv / 6))

a0, a1_6s = a1_from_spectrum(lambda L: scalars(L, 6), a0_expect=6.0)
print("\n[2] SIX real minimal scalars  (= 6 grade-2 so(4) coefficient fields, E = 0)")
print("    a_0 = %.6f  (expect 6)" % a0)
print("    a_1 = %.6f  (expect 6*R/6 = R = %.1f)" % (a1_6s, Rcurv))

# --------------------------------------------- 2-forms (Hodge / de Rham)
# S^4, unit radius. Coexact p-forms: lam = (l+p)(l+n-p-1), l>=1,
#   d_l = (2l+n-1)(l+n-1)! / [ (l+p)(l+n-p-1) p! (n-p-1)! (l-1)! ]
def coexact(lmax, p, n=4):
    out = []
    for l in range(1, lmax + 1):
        lam = (l + p) * (l + n - p - 1)
        d = ((2 * l + n - 1) * math.factorial(l + n - 1)
             / (lam * math.factorial(p) * math.factorial(n - p - 1) * math.factorial(l - 1)))
        out.append((lam, d))
    return out

# sanity: p=0 coexact reproduces the scalar tower (l>=1)
chk = coexact(6, 0)
print("\n    [sanity] coexact p=0 on S^4, first 3 levels:", [(int(a), int(b)) for a, b in chk[:3]],
      " vs scalars:", [(int(l*(l+3)), int((l+1)*(l+2)*(2*l+3)/6)) for l in (1, 2, 3)])
print("    [sanity] coexact p=1 lowest level (Killing vectors, expect 10):",
      int(coexact(3, 1)[0][1]), " lam =", int(coexact(3, 1)[0][0]))
print("    [sanity] coexact p=2 lowest level (expect 10):",
      int(coexact(3, 2)[0][1]), " lam =", int(coexact(3, 2)[0][0]))

# Full Lambda^2(S^4) = coexact 2-forms  +  d(coexact 1-forms)  (b_2 = 0, no harmonics)
def two_forms(lmax):
    return coexact(lmax, 2) + coexact(lmax, 1)

a0, a1_2f = a1_from_spectrum(two_forms, a0_expect=6.0)
print("\n[3] Lambda^2(S^4) with the HODGE-de Rham Laplacian (dd*+d*d), dim V = 6")
print("    a_0 = %.6f  (expect 6 = dim Lambda^2)" % a0)
print("    a_1 = %.6f" % a1_2f)
# analytic: Weitzenbock W_p = p(n-p)K, K = R/(n(n-1)) = R/12; p=2,n=4 -> W = 4K = R/3
W2 = 2 * 2 * Rcurv / 12.0
a1_2f_analytic = 6 * Rcurv / 6 - 6 * W2
print("    analytic: E = -W_2 = -p(n-p)K = -R/3 = %.4f per channel" % (-W2))
print("              a_1 = 6*R/6 - 6*(R/3) = R - 2R = -R = %.4f" % a1_2f_analytic)
print("    agreement: |numeric - analytic| = %.2e" % abs(a1_2f - a1_2f_analytic))

# 1-forms as a cross-check of the same machinery (Delta_1 = nabla*nabla + Ric)
a0, a1_1f = a1_from_spectrum(lambda L: coexact(L, 1) + coexact(L, 0), a0_expect=4.0)
print("\n    [cross-check] Lambda^1(S^4) Hodge: a_0 = %.4f (expect 4), a_1 = %.6f "
      "(expect 4R/6 - R = %.4f)" % (a0, a1_1f, 4 * Rcurv / 6 - Rcurv))

# ------------------------------------------------ conformal & Dirac weights
print("\n[4] TYPE WEIGHTS in the paper's parametrization  c_reg = (1/2)*(a_1/R)/N_eff  at N_eff = 6")
def creg_of(a1, Neff=6):
    return 0.5 * (a1 / Rcurv) / Neff
rows = [
    ("6 real MINIMAL scalars (E = 0)",                a1_6s),
    ("6 real CONFORMAL scalars (xi = 1/6)",           6 * (Rcurv/6 - Rcurv/6)),
    ("Lambda^2 with HODGE (Weitzenbock E = -R/3)",    a1_2f),
    ("6 channels, BOCHNER nabla*nabla on any bundle", 6 * Rcurv / 6),
]
for name, a1v in rows:
    c = creg_of(a1v)
    lam = (math.sqrt(math.pi / (c * 6)) if c > 0 else float('nan'))
    print("    %-46s a_1 = %8.4f  c_reg = %+8.5f  Lambda/M_Pl = %s"
          % (name, a1v, c, ("%.4f" % lam) if c > 0 else "NO SOLUTION (G < 0, repulsive)"))

print("\n    1/12 = %.6f" % (1/12))
print("\nNOTE: a Dirac fermion would enter with the opposite overall sign (-Tr ln) and the")
print("      spinor Weitzenbock (Lichnerowicz E = -R/4): a_1(Dirac,4 cx = 8 real) = -[4*R/6 - 4*(R/4)]")
print("      per 2-component... TWT's LINEAR FACE CARRIES NO FERMIONIC MODE (matter = defect =")
print("      soliton, not a linear-face field), so no fermion term is present. Recorded, not used.")
