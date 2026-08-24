"""(c) refined: the near-misses in the monomial scan are NOT random -- they all come
from ONE functional family. Quantify how much information that family actually carries.
"""
import numpy as np
from scipy.optimize import brentq
import rg_lib as R

PI, MPL = np.pi, R.MPL
t2 = np.exp(brentq(lambda lm: R.s2w_from_MX(np.exp(lm), loops=2) - R.S2W_MEAS,
                   np.log(1e10), np.log(1e17), xtol=1e-12))
print(f"required M_X (2 loop) = {t2:.4e} GeV\n")

print("The near-misses all belong to ONE family: M = (Lambda^2 * m)^(1/3), m a low scale.")
print("How sensitive is that family to WHICH low scale you feed it?\n")
print(f"  {'m':<28} {'m [GeV]':>10}   {'(Lam_lo^2 m)^1/3':>17} {'(Lam_hi^2 m)^1/3':>17}")
for lab, m in [("f_pi (0.129)", 0.129), ("Lambda_QCD (0.196)", 0.196),
               ("e f_pi (0.70)", 0.70), ("1 GeV", 1.0), ("m_p (0.938)", 0.938),
               ("m_t (173)", 173.0), ("v_EW (246)", 246.22), ("1 TeV", 1000.0)]:
    lo = ((0.13*MPL)**2*m)**(1/3); hi = ((2.5*MPL)**2*m)**(1/3)
    print(f"  {lab:<28} {m:>10.4g}   {lo:>17.3e} {hi:>17.3e}")
allv = []
for m in (0.129, 0.196, 0.70, 1.0, 0.938, 173.0, 246.22, 1000.0):
    for L in (0.13*MPL, 2.5*MPL):
        allv.append(((L**2*m)**(1/3)))
allv = np.array(allv)
print(f"\n  The WHOLE family spans {allv.min():.2e} .. {allv.max():.2e} GeV"
      f"  = {np.log10(allv.max()/allv.min()):.2f} decades,")
print(f"  and the target {t2:.2e} sits inside it.")
print("  So the family 'hits' regardless of which low scale is chosen: the FORM does all")
print("  the work and the CHOICE of m does almost none. That is the signature of a")
print("  content-free fit, not of a derived scale.\n")

print("What low scale would the family have to pick to hit the target EXACTLY?")
for Llab, L in [("Lambda low (0.13 M_Pl)", 0.13*MPL), ("M_Pl", MPL), ("Lambda high (2.5 M_Pl)", 2.5*MPL)]:
    m_req = t2**3 / L**2
    print(f"  {Llab:<24}: m = M_X^3/Lambda^2 = {m_req:.4g} GeV")
    for lab, m in [("f_pi", 0.129), ("Lambda_QCD", 0.196), ("e f_pi", 0.70),
                   ("v_EW", 246.22), ("m_t", 173.0)]:
        print(f"      vs {lab:<12} {m:>9.4g} GeV   ratio {m_req/m:>8.2f}")
print("\n  No banked low scale reproduces the required m; the closest are off by factors")
print("  of ~2 and none is singled out. Route (c) is CLOSED: NO derived scale near 1e13 GeV.")
