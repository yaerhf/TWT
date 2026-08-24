"""PROBE 6: is the surviving h_tk cross term removable by a time shift?
curl of the 1-form h_t = h_tk dx^k, for the local (A) and global (B) lock readings."""
import sys, os, math, random
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "corpus"))
import numpy as np
import twt
from twt import e, I4, SCALAR
from texture_h_full16_baryon import Hmat, PROFILES, grid_points
from probe4_globallock import Hg

rng = random.Random(2718)
prof = PROFILES["pi*exp(-r)"]


def curl_local(p, k4=0.83, d=1e-4):
    """curl of h_t for case A (co-rotating I4*Qhat)."""
    def ht(q):
        H, _ = Hmat(list(q) + [0.0], prof, "A_I4Qhat", k4)
        return np.array(H[0, 1:])
    J = np.zeros((3, 3))
    for j in range(3):
        pp = list(p); pm = list(p); pp[j] += d; pm[j] -= d
        J[:, j] = (ht(pp) - ht(pm)) / (2 * d)
    return J - J.T


def curl_global(p, nhat, k4=0.83, d=1e-4):
    def ht(q):
        H = Hg(list(q) + [0.0], prof, nhat, k4)
        return np.array(H[0, 1:])
    J = np.zeros((3, 3))
    for j in range(3):
        pp = list(p); pm = list(p); pp[j] += d; pm[j] -= d
        J[:, j] = (ht(pp) - ht(pm)) / (2 * d)
    return J - J.T


print("=== curl(h_t):  zero => the cross term is a pure time-shift (removable) ===")
mxA = 0.0; mxB = 0.0; scaleA = 0.0; scaleB = 0.0
nz = np.array([0.0, 0.0, 1.0])
for _ in range(60):
    p = [rng.uniform(-2.5, 2.5) for _ in range(3)]
    if np.linalg.norm(p) < 0.3: continue
    cA = curl_local(p); cB = curl_global(p, nz)
    HA, _ = Hmat(p + [0.0], prof, "A_I4Qhat", 0.83)
    HB = Hg(p + [0.0], prof, nz, 0.83)
    mxA = max(mxA, np.max(np.abs(cA))); mxB = max(mxB, np.max(np.abs(cB)))
    scaleA = max(scaleA, np.max(np.abs(HA[0, 1:]))); scaleB = max(scaleB, np.max(np.abs(HB[0, 1:])))
print(f"  case A (local  lock, u = I4*Qhat(rhat)): max|curl h_t| = {mxA:.3e}   (|h_t| scale {scaleA:.3e})")
print(f"  case B (global lock, u = I4*Qhat(n)   ): max|curl h_t| = {mxB:.3e}   (|h_t| scale {scaleB:.3e})")
print()
print("  case A: h_t = -(k4/2) f'(r) rhat  =  d[ -(k4/2) f(r) ]  -> EXACT 1-form,")
print("          removable by T = t - c2*(k4/2)*f(r).  Residual invariant:")
print("          ds^2 = dT^2 + [1 - c2^2 (k4/2)^2 f'(r)^2] dr^2 + r^2 dOmega^2   (NOT flat)")
print("  case B: curl != 0  -> a genuine stationary (gravitomagnetic-type) cross term,")
print("          NOT removable by any time redefinition.")

print()
print("=== residual invariant magnitude, case A, at the ANW-like profile ===")
for pn in ["pi*exp(-r)", "2*atan(1/r^2)"]:
    pf = PROFILES[pn]
    worst = 0.0; rworst = 0.0
    for rr in np.linspace(0.05, 6, 400):
        d = 1e-6
        fp = (pf(rr + d) - pf(rr - d)) / (2 * d)
        v = (0.5 * fp) ** 2                      # (k4/2)^2 f'^2 at k4=1, c2=1
        if v > worst: worst, rworst = v, rr
    print(f"  {pn}: max (k4/2)^2 f'^2 = {worst:.4f} (at r={rworst:.2f})  "
          f"-> A_min = 1 - c2^2*k4^2*{worst:.4f}")
print("  (k4 = omega = the defect mass in substrate units; c2 = the undetermined R-042 scale)")
