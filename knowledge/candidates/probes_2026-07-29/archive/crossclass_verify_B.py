# CROSS-CLASS VERIFICATION probe B: gauge status, Riemann, conjugating case,
# E-axis case, R-128 centralizer, moving defect. 2026-07-29
import numpy as np, sys, math
sys.path.insert(0, r"C:\Users\hfyae\Claude\Projects\Deepseek\knowledge\corpus")
from itertools import combinations

I2 = np.eye(2, dtype=complex)
sx = np.array([[0, 1], [1, 0]], dtype=complex)
sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
sz = np.array([[1, 0], [0, -1]], dtype=complex)
Z2 = np.zeros((2, 2), dtype=complex)
def blk(a, b, c, d): return np.block([[a, b], [c, d]])
g = {1: blk(Z2, 1j*sx, -1j*sx, Z2), 2: blk(Z2, 1j*sy, -1j*sy, Z2),
     3: blk(Z2, 1j*sz, -1j*sz, Z2), 4: blk(Z2, I2, I2, Z2)}
ID = np.eye(4, dtype=complex)
def G(*idx):
    m = ID.copy()
    for i in idx: m = m @ g[i]
    return m
I4m = G(1, 2, 3, 4)
def g0(M): return float(np.real(np.trace(M)) / 4.0)
def h_bil(A, B): return g0(A @ I4m @ B)

rng = np.random.default_rng(77)

# ---------- closed-form h_0k fields (verified in probe A) ----------
def f_exp(r): return math.pi * math.exp(-r)
def fp_exp(r): return -math.pi * math.exp(-r)

def h0k_local(x3, k4):
    r = math.sqrt(sum(v*v for v in x3))
    return np.array([-(k4/2) * fp_exp(r) * x3[k] / r for k in range(3)])

def h0k_global(x3, k4, nhat=np.array([0., 0., 1.])):
    r = math.sqrt(sum(v*v for v in x3)); n = np.array(x3)/r
    f = f_exp(r); fp = fp_exp(r)
    nr = float(nhat @ n)
    return np.array([-(k4/2) * (fp * n[k] * nr
                    + math.sin(f)*math.cos(f) * (nhat[k] - n[k]*nr) / r)
                    for k in range(3)])

k4 = 1.0
print("======== CURL of h_0k (removability by t -> t + psi(x)) ========")
d = 1e-5
for name, fld in [("local", h0k_local), ("global", h0k_global)]:
    mxcurl = 0.0; mxval = 0.0
    for _ in range(40):
        x3 = rng.normal(0, 1, 3)
        if np.linalg.norm(x3) < 0.3: continue
        J = np.zeros((3, 3))
        for j in range(3):
            xp = x3.copy(); xm = x3.copy(); xp[j] += d; xm[j] -= d
            J[:, j] = (fld(list(xp), k4) - fld(list(xm), k4)) / (2*d)
        curl = np.array([J[2,1]-J[1,2], J[0,2]-J[2,0], J[1,0]-J[0,1]])
        mxcurl = max(mxcurl, np.max(np.abs(curl)))
        mxval = max(mxval, np.max(np.abs(fld(list(x3), k4))))
    print("  %s lock: max|curl| = %.3e   (max|h_0k| = %.3f)" % (name, mxcurl, mxval))

print("\n======== LINEARIZED RIEMANN (static, only h_0k nonzero) ========")
# R_{mnrs} = 1/2 (h_{ms,nr} + h_{nr,ms} - h_{mr,ns} - h_{ns,mr}); static => d_t = 0
def h_full(x3, k4, fld):
    H = np.zeros((4, 4))
    v = fld(list(x3), k4)
    H[0, 1:] = v; H[1:, 0] = v
    return H
def d2h(x3, k4, fld, i, j):  # second spatial derivative d_i d_j of full H
    dd = 1e-4
    xi = np.zeros(3); xi[i-1] = dd
    xj = np.zeros(3); xj[j-1] = dd
    return (h_full(x3+xi+xj, k4, fld) - h_full(x3+xi-xj, k4, fld)
            - h_full(x3-xi+xj, k4, fld) + h_full(x3-xi-xj, k4, fld)) / (4*dd*dd)
for name, fld in [("local", h0k_local), ("global", h0k_global)]:
    mxR = 0.0
    for _ in range(15):
        x3 = rng.normal(0, 1, 3)
        if np.linalg.norm(x3) < 0.4 or np.linalg.norm(x3) > 2.0: continue
        # precompute d2 H for spatial pairs
        D2 = {}
        for i in range(1, 4):
            for j in range(1, 4):
                D2[(i, j)] = d2h(x3, k4, fld, i, j)
        def hd(m, s, n, r):  # h_{ms, nr}: derivative indices n,r must be spatial (static)
            if n == 0 or r == 0: return 0.0
            return D2[(n, r)][m, s]
        for m in range(4):
            for n in range(4):
                for r_ in range(4):
                    for s in range(4):
                        Rc = 0.5*(hd(m, s, n, r_) + hd(n, r_, m, s)
                                  - hd(m, r_, n, s) - hd(n, s, m, r_))
                        mxR = max(mxR, abs(Rc))
    print("  %s lock: max |R^lin_{mnrs}| = %.4f" % (name, mxR))

print("\n======== CASE 3: conjugating rotor R = A(t) R_h A(t)~ ========")
def hedgehog_R(x3, k4=None):
    r = math.sqrt(sum(v*v for v in x3)); f = f_exp(r); n = [v/r for v in x3]
    Qh = n[0]*G(1,4) + n[1]*G(2,4) + n[2]*G(3,4)
    return math.cos(f)*ID + math.sin(f)*Qh
u_conj = I4m @ G(3, 4)
def R_conj(x4v, x3, k4):
    th = 0.5*k4*x4v
    A = math.cos(th)*ID + math.sin(th)*u_conj
    Ad = math.cos(th)*ID - math.sin(th)*u_conj
    return A @ hedgehog_R(x3) @ Ad
mx = 0.0; mxOm0 = 0.0
for _ in range(30):
    x3 = list(rng.normal(0, 1, 3))
    if math.sqrt(sum(v*v for v in x3)) < 0.3: continue
    k4c = float(rng.uniform(0.3, 3.0)); x4v = float(rng.uniform(-1, 2))
    dd = 1e-5
    R0 = R_conj(x4v, x3, k4c); Rd = R0.conj().T
    Om = [Rd @ ((R_conj(x4v+dd, x3, k4c) - R_conj(x4v-dd, x3, k4c))/(2*dd))]
    mxOm0 = max(mxOm0, np.max(np.abs(Om[0])))
    for k in range(3):
        xp = list(x3); xm = list(x3); xp[k] += dd; xm[k] -= dd
        Om.append(Rd @ ((R_conj(x4v, xp, k4c) - R_conj(x4v, xm, k4c))/(2*dd)))
    H = np.array([[h_bil(Om[m], Om[n]) for n in range(4)] for m in range(4)])
    mx = max(mx, np.max(np.abs(H)))
print("  max|Om_0| entries = %.3f (nonzero) ; max |h_mu_nu| = %.3e" % (mxOm0, mx))

print("\n======== CASE 5: u = E = I4 e5 (MV engine; both e5 signatures moot) ========")
import twt
def g0mv(mv): return dict(mv.terms).get((), 0.0)
E = twt.e(1,2,3,4,5)
# h_00 = <E I4 E>_0 ; h_0k = <E I4 Om_k>_0 with Om_k grade-2 in Cl(4,0)
print("  <E I4 E>_0 =", g0mv(E * twt.I4 * E))
mvrng = np.random.default_rng(5)
mx = 0.0
for _ in range(20):
    c = mvrng.normal(0, 1, 6)
    Om = (c[0]*twt.e(1,2) + c[1]*twt.e(1,3) + c[2]*twt.e(2,3)
          + c[3]*twt.e(1,4) + c[4]*twt.e(2,4) + c[5]*twt.e(3,4))
    mx = max(mx, abs(g0mv(E * twt.I4 * Om)))
print("  max |<E I4 Om_k>_0| over random grade-2 Om =", mx)

print("\n======== R-128 CENTRALIZER (independent check in my rep) ========")
# claim: even elements commuting with BOTH e4 and B_q=e14 span exactly {1, I4*B_q=~e23}
even_basis = [((), ID)] + [(c, G(*c)) for c in combinations(range(1,5), 2)] + [((1,2,3,4), I4m)]
e4m = G(4); B_q = G(1, 4)
commuting = []
for name, M in even_basis:
    c1 = np.max(np.abs(M @ e4m - e4m @ M))
    c2 = np.max(np.abs(M @ B_q - B_q @ M))
    if c1 < 1e-12 and c2 < 1e-12: commuting.append(name)
print("  even basis elements commuting with {e4, e14}:", commuting)

print("\n======== MOVING DEFECT (Galilean model): h_tt = -2 v.h_tk ? ========")
def R_mov(x4v, x3, k4, v):
    x3s = [x3[i] - v[i]*x4v for i in range(3)]
    r = math.sqrt(sum(q*q for q in x3s))
    u = I4m @ (sum((x3s[i]/r)*G(i+1,4) for i in range(3)))
    Rh = hedgehog_R(x3s)
    th = 0.5*k4*x4v
    return Rh @ (math.cos(th)*ID + math.sin(th)*u)
worst = 0.0
for _ in range(15):
    x3 = list(rng.normal(0, 1, 3))
    if math.sqrt(sum(q*q for q in x3)) < 0.4: continue
    v = list(rng.normal(0, 0.3, 3)); k4c = 1.3
    dd = 1e-5
    R0 = R_mov(0.0, x3, k4c, v); Rd = R0.conj().T
    Om = [Rd @ ((R_mov(dd, x3, k4c, v) - R_mov(-dd, x3, k4c, v))/(2*dd))]
    for k in range(3):
        xp = list(x3); xm = list(x3); xp[k] += dd; xm[k] -= dd
        Om.append(Rd @ ((R_mov(0.0, xp, k4c, v) - R_mov(0.0, xm, k4c, v))/(2*dd)))
    H = np.array([[h_bil(Om[m], Om[n]) for n in range(4)] for m in range(4)])
    pred = -2*sum(v[k]*H[0, k+1] for k in range(3))
    worst = max(worst, abs(H[0, 0] - pred))
print("  max |h_tt - (-2 v.h_tk)| over 15 random (v up to ~0.9) =", worst)

print("\n======== worker-3 style probes: constant u = e12 ; mixed axis h_00 ========")
# constant lepton-type axis against the Q-hedgehog: h_0k nonzero?
u = G(1, 2)
x3 = [0.3, -0.5, 0.8]; k4c = 2.0
dd = 1e-5
def R_c(x4v, x3_):
    th = 0.5*k4c*x4v
    return hedgehog_R(x3_) @ (math.cos(th)*ID + math.sin(th)*u)
R0 = R_c(0.0, x3); Rd = R0.conj().T
Om = [Rd @ ((R_c(dd, x3) - R_c(-dd, x3))/(2*dd))]
for k in range(3):
    xp = list(x3); xm = list(x3); xp[k] += dd; xm[k] -= dd
    Om.append(Rd @ ((R_c(0.0, xp) - R_c(0.0, xm))/(2*dd)))
H = np.array([[h_bil(Om[m], Om[n]) for n in range(4)] for m in range(4)])
print("  u=e12 const: h_tt = %.3e, max|h_tk| = %.3f, max|h_kl| = %.3e"
      % (H[0,0], np.max(np.abs(H[0,1:])), np.max(np.abs(H[1:,1:]))))

print("\nDONE B")
