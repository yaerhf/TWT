"""SECOND-PASS INDEPENDENT RE-DERIVATION of the 2026-07-29 c_reg claim.
Written WITHOUT reading the first pass's probes. Own degeneracies, own numerics,
own symbolic algebra. Methods deliberately DIFFERENT from the engine primitive's.
"""
import math
import numpy as np
import sympy as sp
from mpmath import mp, mpf, exp as mexp

mp.dps = 40

print("=" * 78)
print("PART A -- HEAT-KERNEL a_1 TYPE SUM ON S^4, INDEPENDENT DERIVATION")
print("=" * 78)

# unit S^4: sectional curvature K = 1, R = n(n-1)K = 12, Vol = 8 pi^2 / 3
n = 4
K = mpf(1)
Rs = mpf(n * (n - 1)) * K
Vol = 8 * mp.pi ** 2 / 3
print("R = %s   Vol = %s" % (Rs, mp.nstr(Vol, 12)))


# ---- MY OWN degeneracy formulas (derived, then cross-checked against known counts) ----
def deg_scalar(l):
    """S^n scalar harmonics: (2l+n-1)(l+n-2)!/(l!(n-1)!) ; n=4 -> (2l+3)(l+1)(l+2)/6"""
    return sp.Rational((2 * l + 3) * (l + 1) * (l + 2), 6)


def lam_scalar(l):
    return l * (l + 3)


def deg_coexact(l, p):
    """coexact p-forms on S^4, l>=1:
       (2l+n-1) (l+n-1)! / [ (l+p)(l+n-p-1) p! (n-p-1)! (l-1)! ]"""
    num = (2 * l + n - 1) * sp.factorial(l + n - 1)
    den = ((l + p) * (l + n - p - 1) * sp.factorial(p)
           * sp.factorial(n - p - 1) * sp.factorial(l - 1))
    return sp.Rational(num, den)


def lam_coexact(l, p):
    return (l + p) * (l + n - p - 1)


# --- sanity anchors that do NOT come from the engine ---
assert deg_scalar(0) == 1 and deg_scalar(1) == 5, "S^4 scalar l=0,1 -> 1,5"
assert deg_coexact(1, 1) == 10, "coexact 1-forms level 1 = Killing fields = dim so(5) = 10"
assert lam_coexact(1, 1) == 6
# * maps coexact p-forms to EXACT (n-p)-forms: coexact 3 <-> exact 1 = d(scalars)
assert deg_coexact(1, 3) == deg_scalar(1) == 5, "Hodge duality coexact 3 <-> d(scalar)"
assert deg_coexact(1, 2) == 10 and lam_coexact(1, 2) == 6
print("degeneracy anchors OK: scalar(0,1)=(1,5); Killing=10; *-duality coexact3<->d(scalar)")


def heat_trace(levels, s):
    return sum(mpf(int(d)) * mexp(-mpf(int(lam)) * s) for lam, d in levels)


def a01_fit(levels_fn, lmax_of_s, npts=6, degree=4, smin=mpf("0.004"), ratio=mpf("1.35")):
    """Extract a_0, a_1 by a HIGH-PRECISION POLYNOMIAL LEAST-SQUARES FIT in s
    (NOT the engine's 2-point Richardson) of x(s) = Theta(s)(4 pi s)^2 / Vol."""
    ss, xs = [], []
    s = smin
    for _ in range(npts):
        lm = lmax_of_s(s)
        th = heat_trace(levels_fn(lm), s)
        xs.append(th * (4 * mp.pi * s) ** 2 / Vol)
        ss.append(s)
        s = s * ratio
    A = mp.matrix(npts, degree + 1)
    for i, sv in enumerate(ss):
        for j in range(degree + 1):
            A[i, j] = sv ** j
    y = mp.matrix(xs)
    # normal equations in mp precision
    AT = A.T
    coef = mp.lu_solve(AT * A, AT * y)
    return coef[0], coef[1]


def lmax_of(s):
    return int(math.sqrt(300.0 / float(s))) + 80


scal = lambda m: lambda L: [(lam_scalar(l), m * deg_scalar(l)) for l in range(L + 1)]
lam2 = lambda L: ([(lam_coexact(l, 2), deg_coexact(l, 2)) for l in range(1, L + 1)]
                  + [(lam_coexact(l, 1), deg_coexact(l, 1)) for l in range(1, L + 1)])
lam1 = lambda L: ([(lam_coexact(l, 1), deg_coexact(l, 1)) for l in range(1, L + 1)]
                  + [(lam_scalar(l), deg_scalar(l)) for l in range(1, L + 1)])

cases = {}
for name, fn, dimV in (("1 minimal scalar", scal(1), 1),
                       ("6 minimal scalars", scal(6), 6),
                       ("Hodge Lambda^2", lam2, 6),
                       ("Hodge Lambda^1", lam1, 4)):
    a0, a1 = a01_fit(fn, lmax_of)
    cases[name] = (float(a0), float(a1))
    print("  %-20s a_0 = %+10.6f (expect %2d)   a_1 = %+10.6f  = %+7.4f R"
          % (name, float(a0), dimV, float(a1), float(a1) / float(Rs)))

# ---- ANALYTIC cross-route: Gilkey a_1 = tr(E) + (R/6) dim V, with Weitzenbock ----
# For a space form of curvature K, Weitzenbock on p-forms: Delta_H = nabla*nabla + p(n-p)K.
# Hodge => E = -p(n-p)K * 1  => a_1 = -C(n,p) p(n-p) K + C(n,p) R/6.
def a1_analytic_hodge(p):
    C = sp.binomial(n, p)
    W = p * (n - p) * 1  # K = 1
    return sp.nsimplify(-C * W + C * sp.Rational(12, 6))


print("\n  ANALYTIC (Gilkey + Weitzenbock, K=1, R=12):")
for p in (1, 2):
    print("    Hodge Lambda^%d : a_1 = %s   (= %s R)" % (p, a1_analytic_hodge(p),
                                                         sp.nsimplify(a1_analytic_hodge(p) / 12)))
print("    Bochner (rough) Lambda^2 / 6 scalars : a_1 = 6*(R/6) = R = 12")

# ---- consistency cross-check that validates my degeneracies independently ----
# Delta_Hodge = nabla*nabla + W_2 with W_2 = p(n-p)K = 4.  Adding constant c to D
# shifts a_1 by -c*dimV.  So a_1(rough Lambda^2) = a_1(Hodge Lambda^2) + 4*6.
lhs = cases["Hodge Lambda^2"][1] + 4 * 6
print("\n  CROSS-CHECK  a_1(Hodge L^2) + W_2*dimV = %.6f   must equal 6*(R/6) = %.1f"
      % (lhs, float(Rs)))
assert abs(lhs - float(Rs)) < 2e-3, lhs
# same for 1-forms: W_1 = 1*3*K = 3
lhs1 = cases["Hodge Lambda^1"][1] + 3 * 4
print("  CROSS-CHECK  a_1(Hodge L^1) + W_1*dimV = %.6f   must equal 4*(R/6) = %.1f"
      % (lhs1, 4 * float(Rs) / 6))
assert abs(lhs1 - 4 * float(Rs) / 6) < 2e-3, lhs1

for nm, (a0e, a1e) in (("1 minimal scalar", (1, 2.0)), ("6 minimal scalars", (6, 12.0)),
                       ("Hodge Lambda^2", (6, -12.0)), ("Hodge Lambda^1", (4, -4.0))):
    a0g, a1g = cases[nm]
    assert abs(a0g - a0e) < 2e-3 and abs(a1g - a1e) < 3e-3, (nm, a0g, a1g)
print("\n  ==> CLAIM (ii)/(iv) a_1 VALUES CONFIRMED by two independent routes.")

print()
print("=" * 78)
print("PART B -- c_reg NORMALIZATION, DERIVED FROM SCRATCH")
print("=" * 78)
# Euclidean one-loop:  Gamma = (1/2) Tr ln D = -(1/2) int_0^inf ds/s Tr e^{-sD}
# Tr e^{-sD} = (4 pi s)^{-2} int sqrt(g) (a_0 + s a_1 + ...)
# R-linear piece: -(1/2)(1/(16 pi^2)) int sqrt(g) a_1 * int_{1/Lambda^2}^inf ds s^{-2}
s_, L_, R_, a1_, Neff_, creg_ = sp.symbols('s Lambda R a_1 N_eff c_reg', positive=True)
propertime = sp.integrate(s_ ** -2, (s_, 1 / L_ ** 2, sp.oo))
print("  int_{1/L^2}^inf ds s^-2 = %s" % propertime)
coef_EH = sp.simplify(sp.Rational(1, 2) * a1_ / (16 * sp.pi ** 2) * propertime)
print("  => 1/(16 pi G) = %s" % coef_EH)
# paper parametrization 1/(16 pi G) = c_reg * N_eff * Lambda^2 / (16 pi^2)
creg_sol = sp.solve(sp.Eq(coef_EH, creg_ * Neff_ * L_ ** 2 / (16 * sp.pi ** 2)), creg_)[0]
print("  => c_reg = %s   [i.e. (1/2)(a_1/R)/N_eff after a_1 -> (a_1/R) R]" % creg_sol)
creg_of = lambda a1v, N: sp.simplify(creg_sol.subs({a1_: a1v * R_, Neff_: N}) / R_)
for nm, a1v in (("TWT 6 minimal (a_1 = +R)", 1), ("conformal xi=1/6 (a_1 = 0)", 0),
                ("Hodge Lambda^2 (a_1 = -R)", -1)):
    print("    %-28s c_reg = %s" % (nm, creg_of(a1v, 6)))
# independent tie to the textbook Sakharov formula
Gm1 = sp.simplify(16 * sp.pi * sp.Rational(1, 12) * 6 * L_ ** 2 / (16 * sp.pi ** 2))
print("  textbook tie:  G^-1 = 16 pi * (1/12) N L^2/(16 pi^2) = %s   (expect N L^2/(12 pi) = %s)"
      % (Gm1, sp.simplify(6 * L_ ** 2 / (12 * sp.pi))))
assert sp.simplify(Gm1 - 6 * L_ ** 2 / (12 * sp.pi)) == 0
print("  ==> c_reg = 1/12 <=> G^-1 = N_eff Lambda^2/(12 pi).  CONFIRMED.")

print()
print("=" * 78)
print("PART C -- CLAIM (iii): IS THE RATIO *EXACTLY* c_lat?  SYMBOLIC.")
print("=" * 78)
clat, a_, N_ = sp.symbols('c_lat a N_eff', positive=True)
# R-163 Step 5 assembly (banked):
assembly = N_ * clat / (192 * sp.pi ** 2 * a_ ** 2)
print("  R-163 Step 5:   1/(16 pi G) = %s" % assembly)
# paper parametrization with a CHOICE of Lambda-variable
def creg_at(Lam):
    return sp.simplify(sp.solve(sp.Eq(assembly, creg_ * N_ * Lam ** 2 / (16 * sp.pi ** 2)), creg_)[0])

c_at_inv_a = creg_at(1 / a_)
c_at_Leff = creg_at(sp.sqrt(clat) / a_)
print("  Lambda := 1/a          ->  c_reg = %s" % c_at_inv_a)
print("  Lambda := sqrt(c_lat)/a ->  c_reg = %s" % c_at_Leff)
ratio = sp.simplify(c_at_inv_a / c_at_Leff)
print("  RATIO = %s      simplify(ratio - c_lat) = %s" % (ratio, sp.simplify(ratio - clat)))
assert sp.simplify(ratio - clat) == 0

# the general statement: for ANY two Lambda-variables the ratio is the inverse square ratio
L1, L2 = sp.symbols('Lambda_1 Lambda_2', positive=True)
gen = sp.simplify(creg_at(L1) / creg_at(L2))
print("\n  GENERAL: c_reg(L1)/c_reg(L2) = %s   -- i.e. (L2/L1)^2, INDEPENDENT of the assembly."
      % gen)
print("  => the 'ratio = c_lat' statement is (Lambda_eff * a)^2 by DEFINITION of Lambda_eff.")

# what the engine's own assert actually tests
A_eng = (16 * sp.pi ** 2) / (192 * sp.pi ** 2)
B_eng = (16 * sp.pi ** 2) * clat / (192 * sp.pi ** 2)
print("\n  ENGINE's assert reduces to:  (A*c_lat)/A - c_lat = %s   <-- TAUTOLOGY"
      % sp.simplify(B_eng / A_eng - clat))

# numerical: does the recorded '~21.6' equal c_lat?
print("\n  NUMBERS: c_lat(banked) = 21.83 ; c_lat/12 = %.5f ; (c_lat/12)/(1/12) = %.4f"
      % (21.8285 / 12, (21.8285 / 12) / (1 / 12)))
print("  the record in sakharov_induced_gravity says the factor is '~21.6'.")
print("  1.82/(1/12) = %.3f ; 1.819/(1/12) = %.3f  -> the '21.6' is a rounding artefact, not c_lat"
      % (1.82 * 12, 1.819 * 12))

print()
print("=" * 78)
print("PART D -- INDEPENDENT RECOMPUTE OF c_lat (own quadrature)")
print("=" * 78)
prs = []
for i in range(4):
    for j in range(i + 1, 4):
        for sg in (+1, -1):
            b = [0, 0, 0, 0]; b[i] = 1; b[j] = sg
            prs.append(tuple(b))
assert len(prs) == 12
M2 = sum(2.0 * np.outer(np.array(b, float), np.array(b, float)) for b in prs)
assert np.allclose(M2, 12 * np.eye(4))


def c_lat_grid(N, offset=0.5):
    x = 2 * math.pi * (np.arange(N) + offset) / N
    ax = [x.reshape([N if k == m else 1 for k in range(4)]) for m in range(4)]
    om2 = np.zeros((N,) * 4)
    for b in prs:
        om2 += 2.0 * (1.0 - np.cos(sum(bi * a for bi, a in zip(b, ax) if bi != 0)))
    return 16 * math.pi ** 2 * 0.5 * float((6.0 / om2).mean())


g = {N: c_lat_grid(N) for N in (12, 18, 24, 30)}
for N, v in g.items():
    print("   N=%2d  c_lat = %.5f" % (N, v))
rich = lambda a, b, ra, rb: b + (b - a) / ((rb / ra) ** 2 - 1.0)
r1 = rich(g[12], g[18], 12, 18)
r2 = rich(g[18], g[24], 18, 24)
r3 = rich(g[24], g[30], 24, 30)
print("   h^2-Richardson limits: %.5f  %.5f  %.5f" % (r1, r2, r3))
print("   ==> c_lat ~ %.3f   (banked 21.83)" % r3)
assert abs(r3 - 21.83) < 0.1

# Monte-Carlo, entirely different quadrature
rng = np.random.default_rng(31337)
M = 4_000_000
kk = rng.uniform(0, 2 * math.pi, size=(M, 4))
om2 = np.zeros(M)
for b in prs:
    om2 += 2.0 * (1.0 - np.cos(kk @ np.array(b, float)))
mc = 16 * math.pi ** 2 * 0.5 * float((6.0 / om2).mean())
print("   MC (%d pts) c_lat = %.3f  +- (heavy-tail, IR-dominated estimator)" % (M, mc))

print()
print("=" * 78)
print("PART E -- CLAIM (i): STRESS THE E = 0 ARGUMENT")
print("=" * 78)
# The engine 'check' for E=0: a quadratic form phi.W.phi is not shift invariant.
_rng = np.random.default_rng(7)
Wg = _rng.normal(size=(6, 6)); Wg = 0.5 * (Wg + Wg.T)
phi = np.array([0.31, -0.17, 0.44, 0.09, -0.28, 0.36])
sh = np.array([0.10, 0.0, -0.05, 0.07, 0.0, 0.0])
print("  engine's test: |(phi+sh)W(phi+sh) - phiWphi| = %.4f  (nonzero)"
      % abs((phi + sh) @ Wg @ (phi + sh) - phi @ Wg @ phi))
print("  BUT this holds for ANY W != 0 and ANY sh with W.sh != 0 -- it is the statement")
print("  'a nondegenerate quadratic form is not translation invariant'. Content = 0.")
print("  The DERIVATIVE term is shift-invariant for the same trivial reason:")
d1 = np.array([0.2, 0.1, -0.3, 0.05, 0.0, 0.4])   # d_mu phi
print("    |d(phi+sh) - d(phi)| = %.1e   (sh constant)"
      % np.abs(d1 - d1).max())
print("  => the real load is the PHYSICS premise 'the 6 fields are shift/Goldstone directions',")
print("     which is R-041 (FRAMING + CONDITIONAL), not an engine computation.")

# Is the Hodge corner reachable from the BANKED kinetic term?
print("\n  Hodge-vs-Bochner: the sigma-model term g^{mu nu} delta_AB Grad_mu phi^A Grad_nu phi^B")
print("  yields the ROUGH (Bochner) Laplacian regardless of whether A is a target index or a")
print("  spacetime 2-form index.  The Hodge Laplacian needs |d phi|^2 + |delta phi|^2, a")
print("  DIFFERENT kinetic term.  So the Hodge corner is excluded by R-112's kinetic term,")
print("  not by the index-type sentence the docstring gives.")
print("\nDONE.")
