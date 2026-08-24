"""PROBE 2: identify the nonzero component analytically + check E-axis case."""
import sys, os, math, random
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "corpus"))
import numpy as np
import twt
from twt import MV, e, I4, SCALAR
from texture_h_full16_baryon import (Hmat, PROFILES, Qhat, g0, h, grid_points,
                                     rand_SO3, rand_rotor, LBL, rotor_full)

E5 = e(1, 2, 3, 4, 5)
print("--- E-axis algebra (case D) ---")
print("e5*e5 =", e(5) * e(5))
print("E*E   =", E5 * E5)
print("<E I4 E>_0 =", g0(E5 * I4 * E5))
print("E is grade-5 (odd) -> q=cos+E sin is NOT even; R-127 rules it out anyway.")
print("I4*E =", I4 * E5, "  (grade-1: e5) -> <E I4 E>_0 = <e5 E>_0 = 0")

print()
print("--- analytic identity check for case A (u = I4*Qhat) ---")
print("claim: h_tk = -(k4/2) * df/dr * rhat_k ,  h_tt = 0, h_kl = 0")

rng = random.Random(7)
for prof_name in PROFILES:
    prof = PROFILES[prof_name]
    worst = 0.0
    worst_rel = 0.0
    for _ in range(60):
        x = [rng.uniform(-3, 3) for _ in range(3)]
        r = math.sqrt(sum(t * t for t in x))
        if r < 0.15:
            continue
        k4 = rng.uniform(0.2, 2.0)
        H, Om = Hmat(x + [0.0], prof, "A_I4Qhat", k4)
        d = 1e-6
        fp = (prof(r + d) - prof(r - d)) / (2 * d)
        pred = np.array([-(k4 / 2.0) * fp * (x[i] / r) for i in range(3)])
        got = np.array([H[0, 1], H[0, 2], H[0, 3]])
        err = np.max(np.abs(got - pred))
        scale = max(np.max(np.abs(pred)), 1e-30)
        worst = max(worst, err)
        worst_rel = max(worst_rel, err / scale)
    print(f"  {prof_name:>22}:  max abs err = {worst:.3e}   max rel err = {worst_rel:.3e}")

print()
print("--- exact zeros: h_tt and h_kl over a dense grid, case A ---")
for prof_name in PROFILES:
    prof = PROFILES[prof_name]
    pts = grid_points(9, box=3.0)
    m_tt = 0.0; m_kl = 0.0; m_tk = 0.0
    for p in pts:
        H, _ = Hmat(p + [0.0], prof, "A_I4Qhat", 0.83)
        m_tt = max(m_tt, abs(H[0, 0]))
        m_kl = max(m_kl, np.max(np.abs(H[1:, 1:])))
        m_tk = max(m_tk, np.max(np.abs(H[0, 1:])))
    print(f"  {prof_name:>22}: max|h_tt|={m_tt:.3e}  max|h_kl|={m_kl:.3e}  max|h_tk|={m_tk:.3e}")

print()
print("--- symmetry h_mn = h_nm ---")
prof = PROFILES["pi*exp(-r)"]
ms = 0.0
for p in grid_points(7, box=2.5):
    H, _ = Hmat(p + [0.0], prof, "A_I4Qhat", 0.83)
    ms = max(ms, np.max(np.abs(H - H.T)))
print("  max |h - h^T| =", ms)

print()
print("--- k4 (mass) linearity of h_tk, case A ---")
x = [0.7, -0.4, 1.1]
for k4 in (0.1, 0.5, 1.0, 2.0, 5.0):
    H, _ = Hmat(x + [0.0], prof, "A_I4Qhat", k4)
    print(f"  k4={k4:5.2f}   h_t = ({H[0,1]:+.6f}, {H[0,2]:+.6f}, {H[0,3]:+.6f})"
          f"   |h_t|/k4 = {np.linalg.norm(H[0,1:])/k4:.6f}")

print()
print("--- radiality: is h_t parallel to rhat? ---")
mx = 0.0
for p in grid_points(7, box=2.5):
    H, _ = Hmat(p + [0.0], prof, "A_I4Qhat", 0.83)
    v = np.array(H[0, 1:]); rr = np.array(p) / np.linalg.norm(p)
    perp = v - np.dot(v, rr) * rr
    mx = max(mx, np.linalg.norm(perp))
print("  max |h_t - (h_t.rhat) rhat| =", mx)

print()
print("--- eigenvalues / rank of the full h at a sample point (case A) ---")
H, _ = Hmat([1.0, 0.0, 0.0, 0.0], prof, "A_I4Qhat", 0.83)
print(H)
print("  eigs =", np.linalg.eigvalsh(H), " rank =", np.linalg.matrix_rank(H, tol=1e-9))
