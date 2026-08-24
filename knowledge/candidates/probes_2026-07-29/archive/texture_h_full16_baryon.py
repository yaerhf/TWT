"""PROBE (read-only, scratch): full 16-component texture metric h_mn on the standard
B=1 Q-orbit hedgehog baryon, with the meta-time mass rotor INCLUDED.

h_mn = <Om_m I4 Om_n>_0,  Om_m = R~ d_m R,  m in {t=x4, 1, 2, 3}

Uses the corpus engine (twt.MV / twt.e / twt.I4) directly.
"""
import sys, os, math, itertools, random
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "corpus"))
import numpy as np
import twt
from twt import MV, e, I4, SCALAR

Q = [e(1, 4), e(2, 4), e(3, 4)]          # Q-orbit (baryon winding sector)
L = [e(1, 2), e(1, 3), e(2, 3)]          # L-orbit
E5 = e(1, 2, 3, 4, 5)                    # central E = I4*e5


def g0(mv):
    return dict(mv.terms).get((), 0.0)


def h(A, B):
    return g0(A * I4 * B)


# ----------------------------------------------------------------- profiles
PROFILES = {
    "pi*exp(-r)":        lambda r: math.pi * math.exp(-r),
    "2*atan(1/r^2)":     lambda r: 2.0 * math.atan(1.0 / (r * r)),
    "pi/(1+r^2)":        lambda r: math.pi / (1.0 + r * r),
    "pi*exp(-r^2)":      lambda r: math.pi * math.exp(-r * r),
    "pi*sech(r)":        lambda r: math.pi / math.cosh(r),
    "pi*(1-tanh(r-1))/2":lambda r: math.pi * (1.0 - math.tanh(r - 1.0)) / 2.0,
}


def Qhat(rhat):
    return rhat[0] * Q[0] + rhat[1] * Q[1] + rhat[2] * Q[2]


def rotor_hedgehog(x3, prof, Ospat=None, Aright=None):
    """R_h(x) = cos f + sin f * Qhat(rhat).  Ospat: SO(3) applied to the *field*
    (a spatially rotated hedgehog).  Aright: constant right-multiplying rotor."""
    v = np.array(x3, dtype=float)
    if Ospat is not None:
        v = Ospat @ v
    r = float(np.linalg.norm(v))
    if r < 1e-12:
        R = math.cos(math.pi) * SCALAR
    else:
        f = prof(r)
        R = math.cos(f) * SCALAR + math.sin(f) * Qhat(v / r)
    if Aright is not None:
        R = R * Aright
    return R


def uhat_of(case, x3, prof, Ospat=None):
    """The mass-phase axis u_hat (u^2 = -1) for each case."""
    v = np.array(x3, dtype=float)
    if Ospat is not None:
        v = Ospat @ v
    r = float(np.linalg.norm(v))
    rh = v / r if r > 1e-12 else np.array([0.0, 0.0, 1.0])
    if case == "A_I4Qhat":      return I4 * Qhat(rh)          # R-128 lock, co-rotating
    if case == "A_minus":       return (-1.0) * (I4 * Qhat(rh))
    if case == "B_fixedL":      return e(1, 2)                # global L blade
    if case == "B_fixedL2":     return e(2, 3)
    if case == "C_Qhat":        return Qhat(rh)               # lepton-type rule (R-128: leaks)
    if case == "C_fixedQ":      return e(3, 4)
    if case == "D_E":           return E5                     # central E (R-127: exits ideal)
    if case == "Z_static":      return None                   # Om_t = 0  (corpus assumption)
    raise ValueError(case)


def rotor_full(x4vec, prof, case, k4, Ospat=None, Aright=None):
    """R(x1,x2,x3,x4) = R_h(x) * q(x,x4), q = cos(th/2) + u sin(th/2), th = k4*x4."""
    x3 = x4vec[:3]
    Rh = rotor_hedgehog(x3, prof, Ospat, Aright)
    u = uhat_of(case, x3, prof, Ospat)
    if u is None:
        return Rh
    th = k4 * x4vec[3]
    q = math.cos(th / 2.0) * SCALAR + math.sin(th / 2.0) * u
    return Rh * q


def Hmat(x4vec, prof, case, k4, delta=1e-5, Ospat=None, Aright=None):
    """4x4 h_mn in the ORDER (t=x4, x1, x2, x3)."""
    R = rotor_full(x4vec, prof, case, k4, Ospat, Aright)
    Rr = R.reverse()
    Om = []
    for mu in (3, 0, 1, 2):           # t first, then spatial
        xp = list(x4vec); xm = list(x4vec)
        xp[mu] += delta; xm[mu] -= delta
        dR = (1.0 / (2 * delta)) * (rotor_full(xp, prof, case, k4, Ospat, Aright)
                                    - rotor_full(xm, prof, case, k4, Ospat, Aright))
        Om.append(Rr * dR)
    return np.array([[h(Om[a], Om[b]) for b in range(4)] for a in range(4)]), Om


# ------------------------------------------------------------------ grids
def grid_points(n, box=2.5, seed=None):
    """Cartesian grid avoiding the origin, or random points if seed given."""
    if seed is not None:
        rng = random.Random(seed)
        return [[rng.uniform(-box, box) for _ in range(3)] for _ in range(n)]
    xs = np.linspace(-box, box, n)
    pts = []
    for a in xs:
        for b in xs:
            for c in xs:
                if a * a + b * b + c * c > 1e-4:
                    pts.append([a, b, c])
    return pts


def rand_SO3(rng):
    A = np.array([[rng.gauss(0, 1) for _ in range(3)] for _ in range(3)])
    Qm, Rm = np.linalg.qr(A)
    Qm = Qm * np.sign(np.diag(Rm))
    if np.linalg.det(Qm) < 0:
        Qm[:, 0] *= -1
    return Qm


def rand_rotor(rng):
    """random even unit rotor in Cl(4,0) (product of two blade rotations)"""
    bl = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
    R = SCALAR
    for _ in range(3):
        b = bl[rng.randrange(6)]
        a = rng.uniform(0, 2 * math.pi)
        R = R * (math.cos(a / 2) * SCALAR + math.sin(a / 2) * e(*b))
    return R


LBL = ["t", "1", "2", "3"]


def report_case(case, prof_name="pi*exp(-r)", k4=0.83, x4=0.0, n=7,
                Ospat=None, Aright=None, quiet=False):
    prof = PROFILES[prof_name]
    pts = grid_points(n)
    Hs = [Hmat(p + [x4], prof, case, k4, Ospat=Ospat, Aright=Aright)[0] for p in pts]
    Hs = np.array(Hs)
    mx = np.max(np.abs(Hs), axis=0)
    if not quiet:
        print(f"\n=== case {case}   profile {prof_name}   k4={k4}  x4={x4}  "
              f"grid {n}^3 ({len(pts)} pts) ===")
        print("max |h_mn| over grid:")
        print("        " + "".join(f"{l:>14}" for l in LBL))
        for i in range(4):
            print(f"   {LBL[i]:>3} " + "".join(f"{mx[i, j]:14.3e}" for j in range(4)))
    return mx, Hs, pts


if __name__ == "__main__":
    np.set_printoptions(precision=6, suppress=False)
    print("engine:", twt.__file__)
    print("I4*e14 =", I4 * e(1, 4), " I4*e24 =", I4 * e(2, 4), " I4*e34 =", I4 * e(3, 4))
    for case in ["Z_static", "A_I4Qhat", "A_minus", "B_fixedL", "B_fixedL2",
                 "C_Qhat", "C_fixedQ", "D_E"]:
        report_case(case)
