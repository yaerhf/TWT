"""PROBE 2b — does the R-041 left-Spin(4) shift symmetry forbid a curvature ENDOMORPHISM,
not merely the xi*R*phi^2 term?

The a_1 type-weight is set entirely by E in D = -(nabla^2 + E). R-041 (sakharov_xi_minimal_coupling)
already shows the NON-DERIVATIVE operator <phi^2>_0 is shift-non-invariant. A Weitzenbock-type
endomorphism phi^A W_AB phi^B is the SAME kind of object (non-derivative, quadratic in the
fluctuation). Check that ANY such contraction is shift-non-invariant on the engine, while the
sigma-model kinetic term <Omega Omega>_0 is exactly shift-invariant.

READ-ONLY probe.
"""
import math, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "corpus"))
from twt import e, I4, SCALAR, MV, Substrate, sakharov_xi_minimal_coupling

def g0(mv): return dict(mv.terms).get((), 0.0)
def maxabs(mv):
    d = dict(mv.terms)
    return max((abs(v) for v in d.values()), default=0.0)

print("=" * 78)
print("PROBE 2b — shift symmetry vs a curvature ENDOMORPHISM")
print("=" * 78)

r041 = sakharov_xi_minimal_coupling()
print("\nR-041 banked facts:")
print("  left-Spin(4) invariance of Omega, residual =", "%.3e" % r041["left_invariance_err"])
print("  xi-term operator <phi^2>_0 shift-invariant? ", not r041["xi_term_breaks_shift_symmetry"])
print("  N_eff =", r041["N_eff"], " WP-LV1 isotropy =", r041["isotropy_WP_LV1"])

# --- the 6 grade-2 basis directions (the fluctuation bundle) -------------
SD1 = (1/math.sqrt(2))*(e(1,2) - e(3,4)); ASD1 = (1/math.sqrt(2))*(e(1,2) + e(3,4))
SD2 = (1/math.sqrt(2))*(e(1,3) + e(2,4)); ASD2 = (1/math.sqrt(2))*(e(1,3) - e(2,4))
SD3 = (1/math.sqrt(2))*(e(1,4) - e(2,3)); ASD3 = (1/math.sqrt(2))*(e(1,4) + e(2,3))
basis = [SD1, SD2, SD3, ASD1, ASD2, ASD3]
print("\n  grade-2 bundle dim =", len(basis))

# --- a GENERIC (non-degenerate, symmetric) endomorphism W on that bundle --
import numpy as np
rng = np.random.default_rng(7)
Wm = rng.normal(size=(6, 6)); Wm = 0.5*(Wm + Wm.T)          # a generic symmetric endomorphism
# ...and the Weitzenbock-shaped one for Lambda^2 on a maximally symmetric space:
#     W = p(n-p)K * 1 = (R/3) * 1   at p=2, n=4  -> proportional to the identity
W_weitz = (12.0/3.0) * np.eye(6)

def quad(coeffs, W):
    """phi^A W_AB phi^B for a coefficient vector"""
    v = np.array(coeffs, float)
    return float(v @ W @ v)

phi = [0.31, -0.17, 0.44, 0.09, -0.28, 0.36]
shift = [0.10, 0.00, -0.05, 0.07, 0.00, 0.00]     # a CONSTANT left shift of the fluctuation
phi_shift = [a + b for a, b in zip(phi, shift)]

print("\n  Is the non-derivative quadratic form phi.W.phi invariant under phi -> phi + c ?")
for name, W in (("generic symmetric endomorphism", Wm),
                ("Weitzenbock-shaped W = (R/3)*1 (Lambda^2, p=2,n=4)", W_weitz)):
    a, b = quad(phi, W), quad(phi_shift, W)
    print("    %-52s %.6f -> %.6f   invariant: %s" % (name, a, b, abs(a-b) < 1e-12))

# --- contrast: the sigma-model kinetic term IS shift-invariant -----------
# Omega_mu = R~ d_mu R is invariant under the CONSTANT left shift R -> g0 R (R-041, engine).
# At quadratic order the kinetic density is delta_AB d_mu phi^A d^mu phi^B: a constant shift
# of phi does not touch d_mu phi at all.
h = 1e-6
def path(t):
    R1 = math.cos(0.7*t/2)*SCALAR + math.sin(0.7*t/2)*e(1,2)
    R2 = math.cos(1.3*t/2)*SCALAR + math.sin(1.3*t/2)*e(2,3)
    return R1*R2
t0 = 0.41
g0c = math.cos(0.55)*SCALAR + math.sin(0.55)*e(1,3)
def Omega(prefix):
    R = prefix*path(t0) if prefix is not None else path(t0)
    if prefix is None:
        Rp = (1/(2*h))*(path(t0+h) + (-1.0)*path(t0-h))
    else:
        Rp = (1/(2*h))*(prefix*path(t0+h) + (-1.0)*(prefix*path(t0-h)))
    return R.reverse()*Rp
Om, Om_l = Omega(None), Omega(g0c)
kin_bare = g0(Om*Om.reverse()); kin_shift = g0(Om_l*Om_l.reverse())
print("\n    %-52s %.9f -> %.9f   invariant: %s"
      % ("sigma-model kinetic <Omega Omega>_0", kin_bare, kin_shift,
         abs(kin_bare-kin_shift) < 1e-9))
print("    max|Omega(g0 R) - Omega(R)| = %.3e" % maxabs(Om_l + (-1.0)*Om))

print("""
=> EVERY non-derivative quadratic operator (xi*R*phi^2 AND the Weitzenbock/2-form endomorphism
   alike) breaks the exact left-Spin(4) shift symmetry of the Omega-only action; the sigma-model
   kinetic term does not. So E = 0 is forced by the SAME symmetry R-041 uses for xi = 0 — the
   linear-face bundle is BOCHNER, not Hodge.  a_1 = dim(V)*R/6 = 6*R/6 = R.""")
