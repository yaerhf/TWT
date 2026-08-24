# CROSS-CLASS VERIFICATION probe A (independent re-derivation, 2026-07-29)
# Independent representation: Cl(4,0) via 4x4 complex Euclidean gamma matrices.
#   gamma_k = [[0, i sig_k], [-i sig_k, 0]] (k=1,2,3), gamma_4 = [[0, I], [I, 0]]
#   All Hermitian, gamma_a gamma_b + gamma_b gamma_a = 2 delta_ab.
#   Clifford reversal = matrix dagger (for real-coefficient elements).
#   Grade-0 projection <M>_0 = Re Tr(M) / 4.
# The MV engine is used ONLY for cross-checking the basic bilinear table.
import numpy as np, sys, math
sys.path.insert(0, r"C:\Users\hfyae\Claude\Projects\Deepseek\knowledge\corpus")

I2 = np.eye(2, dtype=complex)
sx = np.array([[0, 1], [1, 0]], dtype=complex)
sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
sz = np.array([[1, 0], [0, -1]], dtype=complex)
Z2 = np.zeros((2, 2), dtype=complex)

def blk(a, b, c, d):
    return np.block([[a, b], [c, d]])

g = {}
for k, s in [(1, sx), (2, sy), (3, sz)]:
    g[k] = blk(Z2, 1j * s, -1j * s, Z2)
g[4] = blk(Z2, I2, I2, Z2)
ID = np.eye(4, dtype=complex)

# --- rep sanity ---
for a in range(1, 5):
    for b in range(1, 5):
        anti = g[a] @ g[b] + g[b] @ g[a]
        target = 2 * ID if a == b else np.zeros((4, 4))
        assert np.allclose(anti, target), (a, b)
print("[rep] anticommutation OK: gamma_a gamma_b + gamma_b gamma_a = 2 delta")

def G(*idx):
    m = ID.copy()
    for i in idx:
        m = m @ g[i]
    return m

I4m = G(1, 2, 3, 4)
def g0(M):  # grade-0 projection
    return float(np.real(np.trace(M)) / 4.0)

# all non-scalar blades traceless (faithfulness of g0)
from itertools import combinations
for r in range(1, 5):
    for c in combinations(range(1, 5), r):
        assert abs(np.trace(G(*c))) < 1e-12, c
print("[rep] all 15 non-scalar blades traceless -> <.>_0 = Tr/4 faithful")

def h_bil(A, B):
    return g0(A @ I4m @ B)

# --- basic bilinear table, cross-checked against the MV engine ---
import twt
def g0_mv(mv): return dict(mv.terms).get((), 0.0)
def h_mv(A, B): return g0_mv(A * twt.I4 * B)
e = twt.e

L_idx = [(1, 2), (1, 3), (2, 3)]
Q_idx = [(1, 4), (2, 4), (3, 4)]
print("\n[table] L x L, Q x Q, L x Q blocks (my rep | MV engine):")
maxdiff = 0.0
for a in L_idx + Q_idx:
    for b in L_idx + Q_idx:
        mine = h_bil(G(*a), G(*b))
        theirs = h_mv(e(*a), e(*b))
        maxdiff = max(maxdiff, abs(mine - theirs))
print("  max |mine - engine| over all 36 pairs =", maxdiff)
assert maxdiff < 1e-12
LL = [[h_bil(G(*a), G(*b)) for b in L_idx] for a in L_idx]
QQ = [[h_bil(G(*a), G(*b)) for b in Q_idx] for a in Q_idx]
LQ = [[h_bil(G(*a), G(*b)) for b in Q_idx] for a in L_idx]
print("  LxL block max|.| =", np.max(np.abs(LL)))
print("  QxQ block max|.| =", np.max(np.abs(QQ)))
print("  LxQ block:\n", np.round(np.array(LQ), 12))

# --- Hodge duals: I4 * e_{i4} (sector assignment for the R-128 lock axis) ---
print("\n[hodge] I4 * Q-blades (should be L-orbit blades):")
Lnames = {(1, 2): "e12", (1, 3): "e13", (2, 3): "e23"}
for qi in Q_idx:
    M = I4m @ G(*qi)
    # decompose in blade basis
    comps = {}
    for r in range(0, 5):
        for c in combinations(range(1, 5), r):
            coef = np.trace(G(*c).conj().T @ M) / 4.0
            if abs(coef) > 1e-12:
                comps[c] = np.real_if_close(coef)
    print("  I4*e%d%d =" % qi, comps)

# ============ THE HEDGEHOG + MASS-PHASE ROTOR, FULL 4x4 h ============
def hedgehog_R(x3, prof):
    r = math.sqrt(sum(v * v for v in x3))
    if r < 1e-12:
        f = prof(1e-12)
        return math.cos(f) * ID  # n_hat ill-defined at 0; avoided in sampling
    f = prof(r)
    n = [v / r for v in x3]
    Qh = n[0] * G(1, 4) + n[1] * G(2, 4) + n[2] * G(3, 4)
    return math.cos(f) * ID + math.sin(f) * Qh

def Qhat_at(x3):
    r = math.sqrt(sum(v * v for v in x3))
    n = [v / r for v in x3]
    return n[0] * G(1, 4) + n[1] * G(2, 4) + n[2] * G(3, 4)

def phase_rotor(u, k4, x4):
    th = 0.5 * k4 * x4
    return math.cos(th) * ID + math.sin(th) * u

def R_full(x4v, x3, prof, k4, mode, uglob=None):
    """mode: 'none', 'local' (u = I4 Qhat(x)), 'global' (u = uglob),
       'winding' (u = Qhat(x)), 'E' -> handled elsewhere (needs e5)."""
    Rh = hedgehog_R(x3, prof)
    if mode == "none":
        return Rh
    if mode == "local":
        u = I4m @ Qhat_at(x3)
    elif mode == "global":
        u = uglob
    elif mode == "winding":
        u = Qhat_at(x3)
    else:
        raise ValueError(mode)
    return Rh @ phase_rotor(u, k4, x4v)

def full_h(x4v, x3, prof, k4, mode, uglob=None, d=1e-5):
    """h_{mu nu}, index order (t=x4, 1, 2, 3). FD in all four coords."""
    Om = []
    R0 = R_full(x4v, x3, prof, k4, mode, uglob)
    Rd = R0.conj().T  # reversal = dagger
    # t-derivative
    Rp = R_full(x4v + d, x3, prof, k4, mode, uglob)
    Rm = R_full(x4v - d, x3, prof, k4, mode, uglob)
    Om.append(Rd @ ((Rp - Rm) / (2 * d)))
    # spatial
    for k in range(3):
        xp = list(x3); xm = list(x3)
        xp[k] += d; xm[k] -= d
        Rp = R_full(x4v, xp, prof, k4, mode, uglob)
        Rm = R_full(x4v, xm, prof, k4, mode, uglob)
        Om.append(Rd @ ((Rp - Rm) / (2 * d)))
    H = np.array([[h_bil(Om[m], Om[n]) for n in range(4)] for m in range(4)])
    return H

profiles = {
    "pi*exp(-r)":      lambda r: math.pi * math.exp(-r),
    "2atan(1/r^2)":    lambda r: 2 * math.atan(1.0 / (r * r)),
    "pi/(1+r^2)":      lambda r: math.pi / (1 + r * r),
    "pi*sech(r)":      lambda r: math.pi / math.cosh(r),
}
dprof = {   # analytic derivatives for formula checks
    "pi*exp(-r)":      lambda r: -math.pi * math.exp(-r),
    "2atan(1/r^2)":    lambda r: -4 * r / (1 + r ** 4),
    "pi/(1+r^2)":      lambda r: -2 * math.pi * r / (1 + r * r) ** 2,
    "pi*sech(r)":      lambda r: -math.pi * math.sinh(r) / math.cosh(r) ** 2,
}

rng = np.random.default_rng(20260729)

print("\n============ CASE 1: Omega_0 = 0 (corpus static ansatz) ============")
mx = 0.0
for pname, prof in profiles.items():
    for _ in range(10):
        x3 = list(rng.normal(0, 1, 3))
        H = full_h(0.0, x3, prof, 0.0, "none")
        mx = max(mx, np.max(np.abs(H)))
print("  max |h_mu_nu| over 4 profiles x 10 random points =", mx)

print("\n============ CASE 2a: LOCAL lock u = I4*Qhat(x), x4=0 slice ============")
worst_dev = 0.0; mx_tt = 0.0; mx_kl = 0.0; nonzero_count = 0; total = 0
for pname, prof in profiles.items():
    for _ in range(15):
        x3 = list(rng.normal(0, 1, 3))
        r = math.sqrt(sum(v * v for v in x3))
        if r < 0.15: continue
        k4 = float(rng.uniform(0.1, 5.0))
        H = full_h(0.0, x3, prof, k4, "local")
        mx_tt = max(mx_tt, abs(H[0, 0]))
        mx_kl = max(mx_kl, np.max(np.abs(H[1:, 1:])))
        # analytic prediction h_tk = -(k4/2) f'(r) x_k / r
        fp = dprof[pname](r)
        pred = [-(k4 / 2) * fp * x3[k] / r for k in range(3)]
        dev = max(abs(H[0, k + 1] - pred[k]) for k in range(3))
        worst_dev = max(worst_dev, dev)
        sym = np.max(np.abs(H - H.T))
        assert sym < 1e-9, sym
        total += 1
        if max(abs(H[0, k + 1]) for k in range(3)) > 1e-6:
            nonzero_count += 1
print("  h_tt max |.| =", mx_tt, " (claimed exactly 0)")
print("  h_kl max |.| =", mx_kl, " (claimed exactly 0 on slice)")
print("  h_tk vs analytic -(k4/2) f'(r) x_k/r : worst |dev| =", worst_dev)
print("  nonzero h_tk in %d / %d trials" % (nonzero_count, total))

print("\n  -- identity behind h_tt = 0: <u I4 u>_0 for ALL 6 coordinate bivectors --")
for a in L_idx + Q_idx:
    print("    <e%d%d I4 e%d%d>_0 =" % (a + a), h_bil(G(*a), G(*a)))
print("    mixed Hodge-pair axis 0.6*e12+0.8*e34: <u I4 u>_0 =",
      h_bil(0.6 * G(1, 2) + 0.8 * G(3, 4), 0.6 * G(1, 2) + 0.8 * G(3, 4)))

print("\n============ CASE 2a off-slice: x4 != 0 (is h_kl still 0?) ============")
prof = profiles["pi*exp(-r)"]
for x4v in [0.3, 0.9, 1.7]:
    mxkl = 0.0
    for _ in range(30):
        x3 = list(rng.normal(0, 1, 3))
        if math.sqrt(sum(v*v for v in x3)) < 0.15: continue
        H = full_h(x4v, x3, prof, 1.7, "local")
        mxkl = max(mxkl, np.max(np.abs(H[1:, 1:])))
    print("  x4 = %.1f : max |h_kl| = %.4f" % (x4v, mxkl))

print("\n============ CASE 2b: GLOBAL lock u = I4*e34 (fixed), any x4 ============")
uglob = I4m @ G(3, 4)
mx_tt = 0.0; mx_kl = 0.0; worst_dev = 0.0; nz = 0; tot = 0; mx_stat = 0.0
H_ref = None
for pname, prof in profiles.items():
    for _ in range(15):
        x3 = list(rng.normal(0, 1, 3))
        r = math.sqrt(sum(v * v for v in x3))
        if r < 0.15: continue
        k4 = float(rng.uniform(0.1, 5.0))
        x4v = float(rng.uniform(-2, 3))
        H = full_h(x4v, x3, prof, k4, "global", uglob)
        H0 = full_h(0.0, x3, prof, k4, "global", uglob)
        mx_stat = max(mx_stat, np.max(np.abs(H - H0)))   # stationarity
        mx_tt = max(mx_tt, abs(H[0, 0]))
        mx_kl = max(mx_kl, np.max(np.abs(H[1:, 1:])))
        # analytic: h_tk = -(k4/2)[ f' n3 x_k/r + (sin f cos f) d_k n3 ],  n3 = x3[2]/r
        fp = dprof[pname](r); f = prof(r)
        n3 = x3[2] / r
        for k in range(3):
            dkn3 = ((1.0 if k == 2 else 0.0) - (x3[k] / r) * n3) / r
            pred = -(k4 / 2) * (fp * (x3[k] / r) * n3 + math.sin(f) * math.cos(f) * dkn3)
            worst_dev = max(worst_dev, abs(H[0, k + 1] - pred))
        tot += 1
        if max(abs(H[0, k + 1]) for k in range(3)) > 1e-6: nz += 1
print("  stationarity max |H(x4)-H(0)| =", mx_stat)
print("  h_tt max =", mx_tt, "  h_kl max =", mx_kl)
print("  h_tk vs analytic global-lock formula: worst |dev| =", worst_dev)
print("  nonzero h_tk in %d/%d trials" % (nz, tot))

print("\n============ CASE 4: u = Qhat(x) (winding blade, R-128-EXCLUDED) ============")
mx = 0.0
for pname, prof in profiles.items():
    for _ in range(8):
        x3 = list(rng.normal(0, 1, 3))
        if math.sqrt(sum(v*v for v in x3)) < 0.15: continue
        for x4v in [0.0, 0.8]:
            H = full_h(x4v, x3, prof, 2.3, "winding")
            mx = max(mx, np.max(np.abs(H)))
print("  max |h_mu_nu| (all blocks, incl. off-slice) =", mx)

print("\n============ LEPTON: L-orbit hedgehog, full h ============")
def lepton_R(x3, prof):
    r = math.sqrt(sum(v * v for v in x3))
    f = prof(r)
    n = [v / r for v in x3]
    Lh = n[0] * G(2, 3) + n[1] * G(1, 3) + n[2] * G(1, 2)
    return math.cos(f) * ID + math.sin(f) * Lh
mx = 0.0
prof = profiles["pi*exp(-r)"]
for _ in range(20):
    x3 = list(rng.normal(0, 1, 3))
    if math.sqrt(sum(v*v for v in x3)) < 0.15: continue
    d = 1e-5
    R0 = lepton_R(x3, prof); Rd = R0.conj().T
    Om = [np.zeros((4,4), complex)]
    # give it the R-127 mass phase too: u = winding blade itself (local)
    r = math.sqrt(sum(v*v for v in x3)); n = [v/r for v in x3]
    u = n[0]*G(2,3) + n[1]*G(1,3) + n[2]*G(1,2)
    k4 = 1.3
    def RL(x4v, x3_):
        return lepton_R(x3_, prof) @ phase_rotor(u, k4, x4v)   # frozen u (at eval pt)
    Om[0] = RL(0,x3).conj().T @ ((RL(d,x3)-RL(-d,x3))/(2*d))
    for k in range(3):
        xp=list(x3); xm=list(x3); xp[k]+=d; xm[k]-=d
        Om.append(RL(0,x3).conj().T @ ((RL(0,xp)-RL(0,xm))/(2*d)))
    H = np.array([[h_bil(Om[m],Om[n]) for n in range(4)] for m in range(4)])
    mx = max(mx, np.max(np.abs(H)))
print("  max |h_mu_nu| lepton hedgehog + R-127 mass phase =", mx)

print("\n============ TRIPLE-PRODUCT IDENTITY on span(Q) ============")
# claim (worker 2): <(ab) I4 c>_0 = -det[a,b,c] for a,b,c in span(Q)
worst = 0.0
for _ in range(200):
    av, bv, cv = rng.normal(0, 1, (3, 3))
    A = sum(av[i] * G(i + 1, 4) for i in range(3))
    B = sum(bv[i] * G(i + 1, 4) for i in range(3))
    C = sum(cv[i] * G(i + 1, 4) for i in range(3))
    lhs = g0(A @ B @ I4m @ C)
    rhs = -np.linalg.det(np.array([av, bv, cv]))
    worst = max(worst, abs(lhs - rhs))
print("  max |<(ab) I4 c>_0 + det[a,b,c]| over 200 random =", worst)

print("\n============ EXACTNESS: analytic MC form, no FD ============")
# Om_k = f' rk Qhat + sin f cos f dQhat_k - sin^2 f Qhat dQhat_k  (exact)
def exact_Om(x3, f, fp):
    r = math.sqrt(sum(v * v for v in x3)); n = np.array(x3) / r
    Qh = sum(n[i] * G(i + 1, 4) for i in range(3))
    s, c = math.sin(f), math.cos(f)
    Oms = []
    for k in range(3):
        dn = np.array([((1.0 if i == k else 0.0) - n[k] * n[i]) / r for i in range(3)])
        dQ = sum(dn[i] * G(i + 1, 4) for i in range(3))
        Oms.append(fp * n[k] * Qh + s * c * dQ - s * s * (Qh @ dQ))
    return Oms
mx_exact = 0.0
for _ in range(50):
    x3 = list(rng.normal(0, 1, 3))
    r = math.sqrt(sum(v*v for v in x3))
    if r < 0.15: continue
    f = float(rng.uniform(0.2, 3.0)); fp = float(rng.normal(0, 1.5))
    Oms = exact_Om(x3, f, fp)
    for k in range(3):
        for l in range(3):
            mx_exact = max(mx_exact, abs(h_bil(Oms[k], Oms[l])))
print("  max |h_kl| from EXACT analytic Om (50 random configs, generic f, f') =", mx_exact)

print("\nDONE A")
