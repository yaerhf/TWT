"""Two-loop SM RG library for the sin^2(theta_W) escape-route probe (2026-07-29).
GUT normalization g1^2 = (5/3) g'^2.  Read-only probe support code."""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

PI = np.pi
MZ        = 91.1876
ALPHA_EM  = 1.0 / 127.951
ALPHA_S   = 0.1179
S2W_MEAS  = 0.23122
YT_MZ     = 0.95
MPL       = 1.220890e19

b1, b2, b3 = 41.0/10.0, -19.0/6.0, -7.0
B = np.array([
    [199.0/50.0, 27.0/10.0, 44.0/5.0],
    [  9.0/10.0, 35.0/ 6.0, 12.0    ],
    [ 11.0/10.0,  9.0/ 2.0, -26.0   ],
])
C_u = np.array([17.0/10.0, 3.0/2.0, 2.0])


def s2w_1loop_analytic(MX, alpha_em=ALPHA_EM, db1=0.0, db2=0.0, Mthr=None):
    t = np.log(MX / MZ) / (2 * PI)
    shift = (b1 - b2) * t
    if Mthr is not None:
        shift += (db1 - db2) * np.log(MX / Mthr) / (2 * PI)
    return 3.0/8.0 - (5.0/8.0) * alpha_em * shift


def MX_for_target_1loop(target, alpha_em=ALPHA_EM):
    t = (3.0/8.0 - target) / ((5.0/8.0) * alpha_em * (b1 - b2))
    return MZ * np.exp(2 * PI * t)


def _rhs(loops):
    k = 1.0 / (16 * PI**2)
    bvec = np.array([b1, b2, b3])
    def f(lnmu, y):
        g = y[:3]
        yt = y[3]
        dg = k * bvec * g**3
        if loops >= 2:
            dg = dg + k**2 * g**3 * ((B @ (g**2)) - C_u * yt**2)
        dyt = k * yt * (4.5*yt**2 - 8*g[2]**2 - 2.25*g[1]**2 - (17.0/20.0)*g[0]**2)
        return np.concatenate([dg, [dyt]])
    return f


def run(s2w_MZ, lnmu_end, loops=2, alpha_s=ALPHA_S, yt=YT_MZ, alpha_em=ALPHA_EM):
    a2 = alpha_em / s2w_MZ
    aY = alpha_em / (1.0 - s2w_MZ)
    a1 = (5.0/3.0) * aY          # g1^2 = (5/3) g'^2  =>  alpha_1 = (5/3) alpha_Y
    y0 = [np.sqrt(4*PI*a1), np.sqrt(4*PI*a2), np.sqrt(4*PI*alpha_s), yt]
    sol = solve_ivp(_rhs(loops), [np.log(MZ), lnmu_end], y0,
                    rtol=1e-11, atol=1e-13, method="DOP853")
    if not sol.success:
        return None
    return sol.y[:, -1]


def s2w_from_MX(MX, loops=2, lo=0.02, hi=0.45, **kw):
    def mismatch(s):
        r = run(s, np.log(MX), loops=loops, **kw)
        return np.nan if r is None else r[0] - r[1]
    return brentq(mismatch, lo, hi, xtol=1e-14, rtol=1e-15)


def couplings_at(s2w_MZ, mu, loops=2, **kw):
    r = run(s2w_MZ, np.log(mu), loops=loops, **kw)
    return None if r is None else r[:3]


def crossing(s2w_MZ, i, j, loops=2, lo=1e2, hi=1e20, **kw):
    def f(L):
        g = couplings_at(s2w_MZ, np.exp(L), loops=loops, **kw)
        return np.nan if g is None else g[i] - g[j]
    try:
        return np.exp(brentq(f, np.log(lo), np.log(hi), xtol=1e-11))
    except Exception:
        return None
