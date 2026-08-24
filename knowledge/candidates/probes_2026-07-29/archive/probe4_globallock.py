"""PROBE 4: the GLOBAL (rigid) lock reading of R-128, u = I4*B0 with B0 a fixed
Q-orbit blade -- the genuinely stationary configuration -- plus exact-identity checks
and the gauge/flatness question."""
import sys, os, math, random
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "corpus"))
import numpy as np
import twt
from twt import MV, e, I4, SCALAR
from texture_h_full16_baryon import (PROFILES, Qhat, g0, h, grid_points,
                                     rotor_hedgehog, rand_SO3, rand_rotor)

rng = random.Random(31415)
Q = [e(1, 4), e(2, 4), e(3, 4)]


def rotor_global(x4v, prof, nhat, k4, Ospat=None, Aright=None):
    """R = R_h(x) * q(x4), q = cos + I4*Qhat(nhat) sin  -- ONE fixed axis for the soliton."""
    Rh = rotor_hedgehog(x4v[:3], prof, Ospat, Aright)
    u = I4 * Qhat(np.asarray(nhat, dtype=float))
    th = k4 * x4v[3]
    return Rh * (math.cos(th / 2) * SCALAR + math.sin(th / 2) * u)


def Hg(x4v, prof, nhat, k4, delta=1e-5, Ospat=None, Aright=None):
    R = rotor_global(x4v, prof, nhat, k4, Ospat, Aright)
    Rr = R.reverse(); Om = []
    for mu in (3, 0, 1, 2):
        xp = list(x4v); xm = list(x4v); xp[mu] += delta; xm[mu] -= delta
        dR = (1 / (2 * delta)) * (rotor_global(xp, prof, nhat, k4, Ospat, Aright)
                                  - rotor_global(xm, prof, nhat, k4, Ospat, Aright))
        Om.append(Rr * dR)
    return np.array([[h(Om[a], Om[b]) for b in range(4)] for a in range(4)])


prof = PROFILES["pi*exp(-r)"]
nz = [0.0, 0.0, 1.0]

print("=== (A) GLOBAL lock: full 16 components, max over a 9^3 grid ===")
for pn in PROFILES:
    pts = grid_points(9, box=3.0)
    M = np.zeros((4, 4))
    for p in pts:
        M = np.maximum(M, np.abs(Hg(p + [0.0], PROFILES[pn], nz, 0.83)))
    print(f"  profile {pn:>22}:  h_tt={M[0,0]:.2e}  max|h_tk|={np.max(M[0,1:]):.3e} "
          f" max|h_kl|={np.max(M[1:,1:]):.2e}")

print("\n=== (B) GLOBAL lock: x4-independence (genuinely stationary) ===")
x = [0.7, -0.4, 1.1]
H0 = Hg(x + [0.0], prof, nz, 0.83)
for x4 in (0.0, 0.4, 1.3, 2.9, -1.7):
    H = Hg(x + [x4], prof, nz, 0.83)
    print(f"  x4={x4:+5.2f}  max|H(x4)-H(0)| = {np.max(np.abs(H-H0)):.3e}   "
          f"h_t=({H[0,1]:+.6f},{H[0,2]:+.6f},{H[0,3]:+.6f})  h_tt={H[0,0]:+.2e}"
          f"  max|h_kl|={np.max(np.abs(H[1:,1:])):.2e}")

print("\n=== (C) GLOBAL lock: analytic form ===")
print("  claim: h_tk = -(k4/2)[ f'(r) rhat_k rhat_a + (sin f cos f / r)(delta_ka - rhat_k rhat_a) ]")
print("         with a = the fixed axis direction (here a = 3)")
worst = 0.0
for _ in range(120):
    p = [rng.uniform(-3, 3) for _ in range(3)]
    r = np.linalg.norm(p)
    if r < 0.2: continue
    k4 = rng.uniform(0.2, 2.0)
    pn = list(PROFILES)[rng.randrange(len(PROFILES))]
    pf = PROFILES[pn]
    nvec = np.array([rng.gauss(0, 1) for _ in range(3)]); nvec /= np.linalg.norm(nvec)
    H = Hg(p + [0.0], pf, nvec, k4)
    rh = np.array(p) / r
    d = 1e-6; fp = (pf(r + d) - pf(r - d)) / (2 * d); f = pf(r)
    sc = math.sin(f) * math.cos(f) / r
    pred = np.array([-(k4 / 2) * (fp * rh[k] * float(nvec @ rh)
                                  + sc * (nvec[k] - rh[k] * float(nvec @ rh)))
                     for k in range(3)])
    worst = max(worst, np.max(np.abs(np.array(H[0, 1:]) - pred)))
print(f"  max abs deviation over 120 random (point, profile, k4, axis) = {worst:.3e}")

print("\n=== (D) GLOBAL lock: robustness, 200 independent trials ===")
tot = surv = 0; lo = 1e30; hi = 0.0; mtt = mkl = 0.0
names = list(PROFILES)
for _ in range(200):
    O = rand_SO3(rng); A0 = rand_rotor(rng)
    pf = PROFILES[names[rng.randrange(len(names))]]
    k4 = rng.uniform(0.2, 2.0)
    p = [rng.uniform(-2.5, 2.5) for _ in range(3)]
    if np.linalg.norm(p) < 0.2: continue
    x4 = rng.uniform(-2, 2)
    nvec = np.array([rng.gauss(0, 1) for _ in range(3)]); nvec /= np.linalg.norm(nvec)
    H = Hg(p + [x4], pf, nvec, k4, Ospat=O, Aright=A0)
    tot += 1
    tk = np.max(np.abs(H[0, 1:]))
    if tk > 1e-6: surv += 1
    lo = min(lo, tk); hi = max(hi, tk)
    mtt = max(mtt, abs(H[0, 0])); mkl = max(mkl, np.max(np.abs(H[1:, 1:])))
print(f"  h_tk nonzero in {surv}/{tot};  |h_tk| in [{lo:.3e},{hi:.3e}]")
print(f"  max|h_tt| = {mtt:.3e}   max|h_kl| = {mkl:.3e}   (both exact-zero blocks)")

print("\n=== (E) exact-identity ingredients (engine) ===")
print("  <Qhat Qhat>_0 for 50 random unit nhat:",
      max(abs(g0(Qhat(v/np.linalg.norm(v))*Qhat(v/np.linalg.norm(v))) + 1)
          for v in [np.array([rng.gauss(0,1) for _ in range(3)]) for _ in range(50)]),
      "(deviation from -1)")
mx = 0.0
for _ in range(50):
    v = np.array([rng.gauss(0,1) for _ in range(3)]); v /= np.linalg.norm(v)
    w = np.array([rng.gauss(0,1) for _ in range(3)]); w -= (w@v)*v   # tangent => dQhat
    mx = max(mx, abs(g0(Qhat(v)*Qhat(w))))
print("  <Qhat(n) Qhat(t)>_0 for t tangent (i.e. <Qhat d_kQhat>_0):", mx)
mx = 0.0
for Qi in Q:
    for Lj in [e(1,2), e(1,3), e(2,3)]:
        mx = max(mx, abs(g0(Qi*Lj)))
print("  <Q_i L_j>_0 (all 9):", mx)
mx = 0.0
for Li in [e(1,2), e(1,3), e(2,3)]:
    for Lj in [e(1,2), e(1,3), e(2,3)]:
        mx = max(mx, abs(g0(Li*I4*Lj)))
print("  <L_i I4 L_j>_0 (all 9) -> this is why h_tt = 0 exactly:", mx)

print("\n=== (F) is the resulting g = delta + c2*h flat?  (case A radial form) ===")
import sympy as sp
r, c2, k4s = sp.symbols('r c2 k4', positive=True)
f = sp.Function('f')
A = 1 - c2**2 * (k4s/2)**2 * sp.Derivative(f(r), r)**2
print("  After completing the square t -> T = t + int c2 h_tr dr (h_tr depends on r only):")
print("     ds^2 = dT^2 + A(r) dr^2 + r^2 dOmega^2,   A(r) = 1 - c2^2 (k4/2)^2 f'(r)^2")
# Ricci scalar of the 3-metric A dr^2 + r^2 dOmega^2 (the T direction is flat/product)
Af = sp.Function('A')
Rs = (2/r**2)*(1 - 1/Af(r)) + (2*sp.Derivative(Af(r), r))/(r*Af(r)**2)
print("  Ricci scalar of that 3-geometry:  R3 = 2/r^2 (1 - 1/A) + 2 A'/(r A^2)")
Ae = 1 - sp.Rational(1,1)*sp.Symbol('a')*sp.exp(-2*r)          # a>0 test profile stand-in
R3 = (2/r**2)*(1 - 1/Ae) + 2*sp.diff(Ae, r)/(r*Ae**2)
print("  With A = 1 - a e^{-2r} (the pi*exp(-r) case up to constants):")
print("     R3 =", sp.simplify(R3))
print("     -> nonzero for a != 0  =>  the metric is NOT flat; h_tk is not pure gauge.")
