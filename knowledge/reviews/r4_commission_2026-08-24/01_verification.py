"""01_verification.py — standalone recomputation backing 01_REVIEW_LEDGER_C4.5_C3.md.

Every assert here is a V-row of the ledger. No TWT engine import: the point is
independence. Requires numpy + scipy only. Run: python 01_verification.py
"""
import numpy as np
from scipy.optimize import brentq, least_squares

# ---------- Part 1: C.4.5 one-loop descent (V-1 .. V-4) ----------
AEM_INV, MZ, MPL = 127.951, 91.1876, 1.220890e19   # full Planck mass (convention check: V-2)
B1, B2 = 41/10, -19/6                               # SM one-loop, GUT-normalized U(1)

def sin2_MZ(MX):
    """sin^2 theta_W(MZ) given g1=g2 at MX, matched to measured alpha_em(MZ)."""
    ell = np.log(MX/MZ)/(2*np.pi)
    x = (3/8)*(AEM_INV - (11/3)*ell)                # alpha_U^{-1}; (5/3)B1+B2 = 11/3
    return (x + B2*ell)/AEM_INV

# V-1: analytic coefficient 3/8 - c*t with c = (109/24)/alpha_em^{-1}
c_analytic = (109/24)/AEM_INV
assert abs(c_analytic - 0.035497) < 5e-6, c_analytic
# numerical slope check
d = (sin2_MZ(np.e*1e13) - sin2_MZ(1e13))/(1/(2*np.pi))
assert abs(-d - c_analytic) < 1e-6, d

# V-2: ruled band [0.39, 0.73] M_Pl -> 0.154-0.158 (requires FULL Planck mass)
lo, hi = sin2_MZ(0.73*MPL), sin2_MZ(0.39*MPL)
assert 0.1535 < lo < 0.1545 and 0.1570 < hi < 0.1580, (lo, hi)

# V-3: three-coupling crossing ~6.8e14 -> ~0.208
A3_INV = 1/0.1181; B3 = -7
M23 = brentq(lambda M: (3/8)*(AEM_INV-(11/3)*np.log(M/MZ)/(2*np.pi))
                        - (A3_INV - B3*np.log(M/MZ)/(2*np.pi)), 1e12, 1e17)
assert 6.5e14 < M23 < 7.1e14 and abs(sin2_MZ(M23) - 0.2076) < 5e-4, (M23, sin2_MZ(M23))

# V-4: required crossing for 0.23122 is ~1.0e13 GeV (one loop)
MX_req = brentq(lambda M: sin2_MZ(M) - 0.23122, 1e10, 1e16)
assert 0.95e13 < MX_req < 1.10e13, MX_req

# V-5: 3/8 = (Sum T3^2)/(Sum Q^2) over one 15-Weyl generation
T3sq = 4*2*(1/4)                      # 4 doublets x 2 states x 1/4 (color-counted: 3+1 doublets) ...
T3sq = (3+1)*2*0.25                   # quark doublet x3 colors + lepton doublet
Qsq  = 3*(2*(2/3)**2 + 2*(1/3)**2) + 2*1**2   # quarks LH+RH x3 colors + e_L,e_R
assert abs(T3sq - 2) < 1e-12 and abs(Qsq - 16/3) < 1e-12 and abs(T3sq/Qsq - 3/8) < 1e-12

# ---------- Part 2: C.3 lepton sector (V-7 .. V-14) ----------
ME, MMU, MTAU = 0.51099895, 105.6583755, 1776.93   # PDG pole masses, MeV
m = np.array([MTAU, MMU, ME]); s = np.sqrt(m)

K = m.sum()/s.sum()**2
assert abs(K - 2/3)/(2/3) < 4e-6                                   # V-7
foot = np.degrees(np.arccos(s.sum()/np.sqrt(3*m.sum())))
assert abs(foot - 45.0) < 2e-3                                     # V-8

def resid(delta):
    A = 1 + np.sqrt(2)*np.cos(delta - 2*np.pi*np.arange(3)/3)
    mu = s.sum()/A.sum()
    return s - mu*A
fit = least_squares(resid, 0.2); dL = fit.x[0]
assert abs(np.degrees(dL) - 12.7325) < 2e-3                        # V-9
assert abs(dL - 2/9)/(2/9) < 2e-5                                  # V-10: 2/9 rad to 1.4e-5
A = 1 + np.sqrt(2)*np.cos(dL - 2*np.pi*np.arange(3)/3); mu = s.sum()/A.sum()
res_sqrtm = np.max(np.abs(s - mu*A)/s); res_mass = np.max(np.abs((mu*A)**2 - m)/m)
assert res_sqrtm < 1e-4 and 1.4e-4 < res_mass < 1.8e-4             # F-5: measure matters
assert abs(np.tan(3*dL) - 0.7866) < 1e-3                           # V-11 (fitted D/J)
assert abs(np.tan(2/3) - 0.786843) < 1e-6                          # V-11 (arc-ratio D/J)
assert abs(np.sqrt(18)/np.tan(2/3) - 5.391979) < 1e-6              # V-12 (demanded e)

mu_lep = s.sum()/3                                                  # V-13: R-134
mN3 = (938.2720813 + 939.5654205)/2/3
assert abs(mu_lep**2 - 313.85) < 0.02
assert abs((mu_lep**2 - mN3)/mN3 - 0.0028) < 4e-4

assert abs(4.67/93.4 - 0.0500) < 1e-4 and abs(0.2243**2 - 0.0503) < 1e-4   # V-14: GST

print("01_verification: ALL CHECKS PASSED")
print(f"  descent coefficient  = {c_analytic:.6f}  (= (109/24)/alpha_em^-1)")
print(f"  ruled-band window    = [{lo:.4f}, {hi:.4f}]")
print(f"  required M_X (1loop) = {MX_req:.3e} GeV")
print(f"  delta_L              = {np.degrees(dL):.4f} deg = {dL:.6f} rad  (2/9 = {2/9:.6f})")
print(f"  fit residual         = {res_sqrtm:.2e} (sqrt-m) / {res_mass:.2e} (mass)")
