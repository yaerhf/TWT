"""Three-coupling unification: solve alpha_1(M_X)=alpha_2(M_X)=alpha_3(M_X) for
(sin^2 theta_W(M_Z), M_X) with alpha_em(M_Z) and alpha_s(M_Z) as inputs.
This is the classic non-SUSY SU(5) computation; the paper's row quotes 6.8e14 / 0.208.
Also: how good is the 'unification' really (spread of the three couplings)?
"""
import numpy as np
from scipy.optimize import fsolve
import rg_lib as R

PI = np.pi

def eqs(x, loops):
    s, lnMX = x
    g = R.run(s, lnMX, loops=loops)
    if g is None or not np.all(np.isfinite(g)):
        return [1e3, 1e3]
    return [g[0]-g[1], g[1]-g[2]]

print("Three-coupling unification (impose g1=g2=g3 at one scale M_X)")
print("inputs held fixed: alpha_em(M_Z)=1/127.951, alpha_s(M_Z)=0.1179, y_t(M_Z)=0.95")
print()
for loops in (1, 2):
    sol, info, ier, msg = fsolve(eqs, [0.21, np.log(7e14)], args=(loops,),
                                 full_output=True, xtol=1e-13)
    s, lnMX = sol
    g = R.run(s, lnMX, loops=loops)
    resid = np.max(np.abs(eqs(sol, loops)))
    print(f"  loops = {loops}:  sin^2 theta_W(M_Z) = {s:.5f},  M_X = {np.exp(lnMX):.4e} GeV")
    print(f"                  g1=g2=g3 = {g[0]:.6f} {g[1]:.6f} {g[2]:.6f}"
          f"   (alpha_X = {g[0]**2/(4*PI):.5f}, 1/alpha_X = {4*PI/g[0]**2:.2f})")
    print(f"                  residual = {resid:.2e}, converged = {ier==1}")
print()
print("  [paper's row: 'three-coupling unification (minimal-SU(5)-style)' -> 6.8e14, 0.208]")
print()

# How badly do the couplings actually fail to unify at the MEASURED sin^2?
print("Reality check: at the MEASURED sin^2(M_Z)=0.23122 the three SM couplings do NOT meet.")
for loops in (1, 2):
    print(f"  loops = {loops}:")
    for mu in (1e13, 1e14, 1e15, 1e16, 1e17):
        g = R.run(R.S2W_MEAS, np.log(mu), loops=loops)
        a = g[:3]**2/(4*PI)
        print(f"    mu = {mu:.0e}: 1/a1={1/a[0]:7.2f}  1/a2={1/a[1]:7.2f}  1/a3={1/a[2]:7.2f}"
              f"   spread = {max(1/a)-min(1/a):6.2f}")
print()
print("  => the non-SUSY SM has no common crossing; the 'three-coupling unification' row")
print("     is a two-of-three construct, which is why it is flagged as NOT a TWT claim.")
