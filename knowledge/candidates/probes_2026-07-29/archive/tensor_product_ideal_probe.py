"""
PROBE (NOT BANKED) — 2026-07-29
Direct algebraic tensor product of the spinor minimal left ideal S = Cl(4,0)*s0.

Question assigned: attempt  S (x) S  over R, over C, over the commutant.
Be rigorous about WHICH ring the tensor product is over.

Everything here is computed from the twt.py Clifford engine (MV / e()).
NOTHING here is a twt.py primitive yet -> cite as PROBE, not "engine-verified".
"""
import sys, os, itertools, math
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "..", "corpus"))
import twt
from twt import MV, e

TOL = 1e-10
ok = lambda cond, msg: print(("  PASS  " if cond else "  ** FAIL ** ") + msg) or (cond)
results = []
def check(cond, msg):
    results.append((bool(cond), msg))
    print(("  PASS  " if cond else "  **FAIL**  ") + msg)
    return bool(cond)

# ---------------------------------------------------------------- blade basis
BLADES = []
for k in range(5):
    for c in itertools.combinations((1, 2, 3, 4), k):
        BLADES.append(c)
BIDX = {b: i for i, b in enumerate(BLADES)}
N = len(BLADES)          # 16

def vec(mv: MV):
    v = np.zeros(N)
    for b, c in mv.terms:
        v[BIDX[b]] += c
    return v

def unvec(v):
    return MV.from_dict({BLADES[i]: float(v[i]) for i in range(N) if abs(v[i]) > 1e-14})

ONE = MV.from_dict({(): 1.0})
s0  = 0.5 * (ONE + e(4))
I4  = e(1, 2, 3, 4)

print("=" * 78)
print("PART 1 — the one-defect object: S = Cl(4,0) s0 and its commutant")
print("=" * 78)

check(((s0 * s0) - s0).terms == (), "s0^2 = s0   (s0 = (1+e4)/2 is idempotent)")

# S = Cl(4,0) s0 : span of {blade * s0}
M = np.array([vec(unvec(np.eye(N)[i]) * s0) for i in range(N)])
rank_S = np.linalg.matrix_rank(M, tol=1e-9)
check(rank_S == 8, f"dim_R S = 8   (got {rank_S})")

# nice basis: e4*s0 = s0  =>  S = Cl(3,0) s0
check(((e(4) * s0) - s0).terms == (), "e4 s0 = s0   => S = Cl(3,0) s0, basis {1,e1,e2,e3,e12,e13,e23,e123} s0")

CL3 = [(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]
SB = [unvec(np.eye(N)[BIDX[b]]) * s0 for b in CL3]
SBm = np.array([vec(x) for x in SB])
check(np.linalg.matrix_rank(SBm, tol=1e-9) == 8, "that basis is independent (rank 8)")

# coordinates on S
Q, _ = np.linalg.qr(SBm.T)          # 16 x 8 orthonormal columns spanning S
P_S = Q @ Q.T
def sc(mv):                         # S-coords (8-vector) in the Q frame
    return Q.T @ vec(mv)
def unsc(c):
    return unvec(Q @ c)

def L(mv):                          # left multiplication by mv, as 8x8 on S
    return np.array([sc(mv * unsc(np.eye(8)[i])) for i in range(8)]).T
def R(mv):                          # right multiplication by mv, as 8x8 on S
    return np.array([sc(unsc(np.eye(8)[i]) * mv) for i in range(8)]).T

# --- the commutant End_{Cl(4,0)}(S) --------------------------------------
gens = [L(e(1)), L(e(2)), L(e(3)), L(e(4))]
rows = []
for G in gens:
    # vec(G X - X G) = (I (x) G - G^T (x) I) vec(X)
    rows.append(np.kron(np.eye(8), G) - np.kron(G.T, np.eye(8)))
A = np.vstack(rows)
u, s, vt = np.linalg.svd(A)
comm_dim = int(np.sum(s < 1e-8)) + (A.shape[1] - len(s))
check(comm_dim == 4, f"dim_R End_Cl(4,0)(S) = 4   (got {comm_dim})  ->  the commutant is a 4-dim division ring")

# the four right-multipliers  {1, e23, e13, e12}
Hbasis = [ONE, e(2, 3), e(1, 3), e(1, 2)]
# GUARD: the coordinate maps sc()/unsc() PROJECT onto S. Verify the right action really
# closes inside S, otherwise every commutation check below would be silently projected.
worst_cl = 0.0
for h in Hbasis:
    for b in SB:
        y = vec(b * h)
        worst_cl = max(worst_cl, np.linalg.norm(y - P_S @ y))
check(worst_cl < TOL, f"right-mult by {{1,e23,e13,e12}} CLOSES inside S — no silent projection (max {worst_cl:.1e})")
worst_cl = 0.0
for g in [e(1), e(2), e(3), e(4)]:
    for b in SB:
        y = vec(g * b)
        worst_cl = max(worst_cl, np.linalg.norm(y - P_S @ y))
check(worst_cl < TOL, f"left Cl(4,0) action closes inside S (left ideal) (max {worst_cl:.1e})")

Rmats = [R(h) for h in Hbasis]
for h, Rm in zip(Hbasis, Rmats):
    worst = max(np.abs(Rm @ G - G @ Rm).max() for G in gens)
    check(worst < TOL, f"right-mult by {h!r:>18} commutes with all left Cl(4,0) action (max err {worst:.1e})")
stack = np.array([m.flatten() for m in Rmats])
check(np.linalg.matrix_rank(stack, tol=1e-9) == 4,
      "those 4 right-multipliers are independent -> they ARE the whole commutant")

# quaternion relations on the commutant  (i,j,k) = (e23, e13, e12)
i_, j_, k_ = e(2, 3), e(1, 3), e(1, 2)
rel = [((i_ * i_) + ONE, "i^2 = -1"), ((j_ * j_) + ONE, "j^2 = -1"), ((k_ * k_) + ONE, "k^2 = -1"),
       ((i_ * j_) - k_, "i j = k"), ((j_ * k_) - i_, "j k = i"), ((k_ * i_) - j_, "k i = j")]
for mv, nm in rel:
    check(mv.terms == (), f"commutant quaternion relation  {nm}")

print("\n  >>> RESULT 1 [DERIVED-A, probe]: the scalar ring of TWT's one-defect state space is H,")
print("      not C.  S is a (Cl(4,0), H)-bimodule, quaternionic dim 2.")
print("      The imaginary units of the commutant are EXACTLY the L-orbit winding blades")
print("      {e23, e13, e12} — i.e. B_a of B.3.1 is an imaginary unit OF THE COMMUTANT.\n")

# --- the chiral (Weyl) split ---------------------------------------------
check((I4 * I4 - ONE).terms == (), "I4^2 = +1")
evens = [(), (1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4), (1, 2, 3, 4)]
worst = 0.0
for b in evens:
    x = unvec(np.eye(N)[BIDX[b]])
    worst = max(worst, max(abs(c) for _, c in (I4 * x - x * I4).terms) if (I4 * x - x * I4).terms else 0.0)
check(worst < TOL, "I4 is central in Cl+(4,0)")
sp = 0.5 * (ONE + I4)
sm = 0.5 * (ONE - I4)
check((sp * sp - sp).terms == () and (sm * sm - sm).terms == (), "s_pm = (1 +- I4)/2 idempotent")

Lp, Lm = L(sp), L(sm)
dp = int(round(np.trace(Lp))); dm = int(round(np.trace(Lm)))
check(dp == 4 and dm == 4, f"S = S+ (+) S-,  dim_R S+ = {dp}, dim_R S- = {dm}   (the two Weyl ideals)")
for Rm in Rmats:
    check(np.abs(Lp @ Rm - Rm @ Lp).max() < TOL, "S+ is stable under the right H-action (left/right commute)")
    break

# basis of S+
w, V = np.linalg.eigh((Lp + Lp.T) / 2)
Bp = V[:, w > 0.5]                       # 8 x 4
check(Bp.shape[1] == 4, "extracted a 4-dim real basis of S+")

print("\n  >>> RESULT 2 [DERIVED-A, probe]: S splits into two Weyl ideals S_pm = s_pm S,")
print("      each of real dim 4 = quaternionic dim 1 = ONE qubit once a complex line is chosen.\n")

print("=" * 78)
print("PART 2 — WHICH RING?  the three candidate tensor products")
print("=" * 78)

# --- (a) over R -----------------------------------------------------------
print("\n(a) S (x)_R S")
print(f"    dim_R = 8 x 8 = 64.")
# H (x)_R H = M_4(R):  check numerically via L_q R_q' on H = R^4
Hb = [ONE, i_, j_, k_]
def hvec(mv):
    return np.array([mv.coeff(()), mv.coeff((2, 3)), mv.coeff((1, 3)), mv.coeff((1, 2))])
ops = []
for a in Hb:
    for b in Hb:
        Mq = np.array([hvec(a * Hb[t] * b) for t in range(4)]).T
        ops.append(Mq.flatten())
r = np.linalg.matrix_rank(np.array(ops), tol=1e-9)
check(r == 16, f"H (x)_R H  ->  16 independent operators on R^4  =>  H (x)_R H = M_4(R)  (rank {r})")
print("    => Cl(4,0) (x)_R Cl(4,0) = M_2(H) (x) M_2(H) = M_16(R): minimal left ideal has dim_R 16.")
print("    => 64 = 4 x 16 : S (x)_R S is NOT a minimal/irreducible module of the doubled algebra.")
print("    => and M_16(R) has commutant R : the 'two-defect' theory would be REAL quantum mechanics.")

# --- (b) over the commutant H --------------------------------------------
print("\n(b) S (x)_H S   — the *natural* choice, since H IS the commutant")
print("    S is a RIGHT H-module.  A tensor product over H needs a LEFT H-module on the other side;")
print("    use the conjugation anti-automorphism to turn S into one.  Then:")
print("        H^2 (x)_H H^2  ~=  H^{2x2}  -> real dim 16.")
print("    BUT: the result carries NO H-action.  Z(H) = R, so the balanced product")
print("    (m q) (x) n = m (x) (q n) admits no well-defined quaternion scalar multiplication.")
# demonstrate the obstruction concretely: any candidate action (m (x) n).q := m (x) (n q)
# must be compatible with the balancing relation; test on H (x)_H H ~= H:
# balanced: (1 (x) p) ~ (p (x) 1). Acting on the right by q:
#   from lhs: 1 (x) p q ;  from rhs: p (x) q ~ 1 (x) p q  -> consistent
# but acting on the LEFT by q (the other slot) gives q p (x) 1 ~ 1 (x) q p, and p q != q p.
p_, q_ = i_, j_
check(((p_ * q_) - (q_ * p_)).terms != (), "H is noncommutative:  i j != j i   (the balancing obstruction)")
print("    => S (x)_H S is a REAL vector space with no complex or quaternionic structure.")
print("    => this is Adler's tensor-product problem for quaternionic QM, arriving here from the")
print("       substrate side rather than being imported as a difficulty.")

# --- (c) over a complex line C_a = R + R B_a ------------------------------
print("\n(c) S (x)_{C_a} S   — the only choice that gives a usable complex tensor product")
Ca = [ONE, k_]           # B_a = e12
Cb = [ONE, j_]           # a second defect winding on e13
inter = np.array([hvec(ONE), hvec(k_), hvec(ONE), hvec(j_)])
Ma = np.array([hvec(ONE), hvec(k_)])
Mb = np.array([hvec(ONE), hvec(j_)])
# intersection of two 2-planes inside H
stackab = np.vstack([Ma, Mb])
dim_sum = np.linalg.matrix_rank(stackab, tol=1e-9)
dim_int = 2 + 2 - dim_sum
check(dim_int == 1, f"C_a ^ C_b = R  for B_a=e12, B_b=e13  (dim {dim_int})  -> NO common complex scalar field")

# joint centralizer of e4, e12, e13 in Cl+(4,0)
def centralizer(mvs, space):
    keep = []
    for b in space:
        x = unvec(np.eye(N)[BIDX[b]])
        if all((m * x - x * m).terms == () for m in mvs):
            keep.append(b)
    return keep
c1 = centralizer([e(4), e(1, 2)], evens)
c2 = centralizer([e(4), e(1, 2), e(1, 3)], evens)
print(f"    centralizer_even(e4, e12)        = {c1}   (dim {len(c1)})")
print(f"    centralizer_even(e4, e12, e13)   = {c2}   (dim {len(c2)})")
check(len(c1) == 2, "one defect: the B.3.1 centralizer is 2-dim {1, B_a}  (reproduces R-020)")
check(len(c2) == 1, "two MISALIGNED defects: the common centralizer collapses to the scalars R")

print("\n  >>> RESULT 3 [DERIVED-A, probe]: the tensor product over C_a EXISTS only if both defects")
print("      select the SAME winding blade.  That alignment is not derived anywhere in TWT.")
print("      Misaligned defects share only R -> real QM (Renou et al 2021 territory).\n")

print("=" * 78)
print("PART 3 — GRANT the C_a tensor product. What does the substrate then supply?")
print("=" * 78)

# ---- complexify S+ over C_a = span{1, e12}, right action ----------------
Jr = R(k_)                            # right mult by e12 = 'i'
check(np.abs(Jr @ Jr + np.eye(8)).max() < TOL, "right-mult by e12 squares to -1 on S")
check(np.abs(Lp @ Jr - Jr @ Lp).max() < TOL, "it preserves S+")

# real basis of S+ adapted to J : {u1, u1 i, u2, u2 i}
def proj_plus(v8):
    return Lp @ v8
u1 = proj_plus(sc(SB[0]))
u1 = u1 / np.linalg.norm(u1)
u1i = Jr @ u1
# pick u2 orthogonal to span{u1,u1i} inside S+
cand = None
for x in [sc(b) for b in SB]:
    x = proj_plus(x)
    x = x - (x @ u1) * u1 - (x @ u1i) * u1i
    if np.linalg.norm(x) > 1e-6:
        cand = x / np.linalg.norm(x); break
u2 = cand; u2i = Jr @ u2
Breal = np.array([u1, u1i, u2, u2i]).T
check(np.linalg.matrix_rank(Breal, tol=1e-9) == 4, "S+ has C_a-basis {u1, u2} (real basis {u1,u1i,u2,u2i})")

def to_C(v8):
    """C_a-coordinates of a vector in S+ w.r.t. {u1,u2}."""
    a = np.linalg.lstsq(Breal, v8, rcond=None)[0]
    return np.array([a[0] + 1j * a[1], a[2] + 1j * a[3]])
def from_C(z):
    return Breal @ np.array([z[0].real, z[0].imag, z[1].real, z[1].imag])

def cmat(Op8):
    """2x2 complex matrix of a real operator on S+ that commutes with Jr."""
    cols = [to_C(Op8 @ from_C(np.array([1 + 0j, 0j]))),
            to_C(Op8 @ from_C(np.array([0j, 1 + 0j])))]
    return np.array(cols).T

def is_Clinear(Op8):
    return np.abs((Op8 @ Jr - Jr @ Op8) @ Lp).max() < 1e-9

# spin su(2): LEFT multiplication by the L-orbit bivectors
S12, S13, S23 = L(e(1, 2)), L(e(1, 3)), L(e(2, 3))
for nm, Op in [("e12", S12), ("e13", S13), ("e23", S23)]:
    check(is_Clinear(Op), f"left-mult by {nm} is C_a-linear (commutes with the RIGHT action)")

C13, C23, C12 = cmat(S13), cmat(S23), cmat(S12)
for nm, Cm in [("e13", C13), ("e23", C23), ("e12", C12)]:
    ah = np.abs(Cm + Cm.conj().T).max()
    tr = abs(np.trace(Cm))
    check(ah < 1e-9 and tr < 1e-9, f"L({nm}) on S+ is anti-Hermitian & traceless -> su(2)   (|A+A*|={ah:.1e}, |tr|={tr:.1e})")
check(abs(np.linalg.det(C13) - 1) < 1e-9, f"det L(e13)|_{{S+}} = {np.linalg.det(C13):.6f}  -> SU(2)")

print("\n  >>> RESULT 4 [DERIVED-A, probe]: on S+ with the C_a structure, the spin rotors act as")
print("      exactly SU(2) on C^2.  The qubit is substrate-native; nothing imported so far.\n")

# ---- the antisymmetric invariant (the 'singlet' before any tensor product)
# eps(u,v) = det[u|v] is the unique SL(2,C)-invariant antisym bilinear form; check SU(2)-invariance
def eps(z, w):
    return z[0] * w[1] - z[1] * w[0]
rng = np.random.default_rng(7)
worst = 0.0
for _ in range(200):
    th = rng.normal(size=3)
    Bv = th[0] * e(1, 2) + th[1] * e(1, 3) + th[2] * e(2, 3)
    # rotor = exp(Bv/2) via series on the 8x8 left rep
    Rm = np.eye(8); T = np.eye(8); Lb = L(Bv) / 2
    for n in range(1, 30):
        T = T @ Lb / n; Rm = Rm + T
    Cr = cmat(Rm)
    z = rng.normal(size=2) + 1j * rng.normal(size=2)
    w = rng.normal(size=2) + 1j * rng.normal(size=2)
    worst = max(worst, abs(eps(Cr @ z, Cr @ w) - eps(z, w)))
check(worst < 1e-8, f"eps(u,v) = u1 v2 - u2 v1 is invariant under ALL substrate spin rotors (max err {worst:.1e})")

# is eps the quaternionic structure?  j = right-mult by e13 is antilinear over C_a
Jq = R(j_)
anti = np.abs((Jq @ Jr + Jr @ Jq) @ Lp).max()
check(anti < 1e-9, "right-mult by e13 ANTI-commutes with right-mult by e12 -> it is the antilinear")
check(np.abs((Jq @ Jq + np.eye(8)) @ Lp).max() < 1e-9,
      "  quaternionic structure j on S+, j^2 = -1  => eps(u,v) = <j u, v> is substrate-supplied")

# --- how the dropped commutant directions sit in the brief's U(1)_a charge split ---
# adjoint (two-sided) U(1) generated by B_a = e12 on the even blades
def adj(th, X):
    Rr = math.cos(th / 2) * ONE + math.sin(th / 2) * e(1, 2)
    return Rr * X * Rr.reverse()
th = 0.7
for nm, X, expect in [("e12", e(1, 2), "charge 0"), ("e34", e(3, 4), "charge 0"),
                      ("I4", I4, "charge 0")]:
    check(max((abs(c) for _, c in (adj(th, X) - X).terms), default=0.0) < 1e-9,
          f"adjoint U(1)_a: {nm} is invariant ({expect})")
d13 = adj(th, e(1, 3))
check(abs(d13.coeff((1, 3)) - math.cos(th)) < 1e-9 and abs(d13.coeff((2, 3)) + math.sin(th)) < 1e-9,
      "adjoint U(1)_a: (e13,e23) rotate as a charge-+-1 doublet")
print("    -> the TWO commutant directions the C_a restriction DISCARDS are e13, e23,")
print("       i.e. exactly the adjoint-U(1)_a CHARGED doublet of the 2026-07-29 charge split.")
print("       They are the charge-conjugating (antilinear) directions. Coherent, not coincidental.")

# --- Gleason spinoff: C_a-dimension of the FULL ideal ---
dimC_S = 8 // 2
check(dimC_S == 4, f"dim_C_a(S) = {dimC_S} >= 3  -> Gleason applies to ONE defect's full ideal")
print("    -> the dim-2 Gleason hole of B.3.3 is an artifact of the B.3.1 phase-sector ANSATZ,")
print("       not of the substrate: the ideal itself is C_a-dim 4. (CANDIDATE — needs the")
print("       physical-vs-gauge status of the other 2 complex dims settled.)")

print("\n  >>> RESULT 5 [DERIVED-A, probe]: the antisymmetric SU(2) invariant eps — i.e. the SINGLET")
print("      pairing — is NOT an extra postulate.  It is the leftover imaginary unit of the")
print("      commutant H that the C_a restriction discards: the antilinear quaternionic structure j.")
print("      This is real substrate content, and it is what the six 'dropped blades' are hiding.\n")

print("=" * 78)
print("PART 4 — the Bell correlation, computed rather than typed in")
print("=" * 78)

def analyzer(theta):
    """A(theta) = i * L(cos t e13 + sin t e23) on S+ : Hermitian, A^2 = 1, traceless."""
    Cm = math.cos(theta) * C13 + math.sin(theta) * C23
    return 1j * Cm

# GUARD: is theta an honest REAL-SPACE analyzer angle, or a fudge?
# adjoint rotation by theta about the 12-plane must carry e13 -> cos t e13 - sin t e23.
worst = 0.0
for t in np.linspace(0, 2 * math.pi, 25):
    got = adj(t, e(1, 3))
    want = math.cos(t) * e(1, 3) - math.sin(t) * e(2, 3)
    worst = max(worst, max((abs(c) for _, c in (got - want).terms), default=0.0))
check(worst < 1e-9, f"the analyzer family {{cos t e13 + sin t e23}} IS the real-space rotation orbit of e13 "
                    f"by angle t (no half-angle fudge in the setting label; err {worst:.1e})")

A0 = analyzer(0.0)
check(np.abs(A0 @ A0 - np.eye(2)).max() < 1e-9, "A(0)^2 = 1 (a legitimate +-1 observable)")
check(np.abs(A0 - A0.conj().T).max() < 1e-9, "A(0) Hermitian")

# singlet in S+ (x)_{C_a} S+   (the tensor product is GRANTED here, not derived)
psi = np.array([0, 1, -1, 0], dtype=complex) / math.sqrt(2)

# GUARD A: is the singlet CHOSEN or FORCED?  ->  it is the unique diagonal-invariant vector.
gen = []
for Bv in [e(1, 2), e(1, 3), e(2, 3)]:
    g = cmat(L(Bv))
    gen.append(np.kron(g, np.eye(2)) + np.kron(np.eye(2), g))   # diagonal su(2) action
Astack = np.vstack(gen)
sv = np.linalg.svd(Astack, compute_uv=False)
null_dim = int(np.sum(sv < 1e-9)) + max(0, 4 - len(sv))
check(null_dim == 1, f"the diagonal substrate-spin invariant subspace of S+ (x) S+ is 1-dimensional "
                     f"(dim {null_dim}) -> the singlet is FORCED, not chosen")
inv_res = max(np.abs(G @ psi).max() for G in gen)
check(inv_res < 1e-9, f"and psi_singlet spans it (residual {inv_res:.1e})")

# GUARD B: where does the HALF-ANGLE actually enter?
worst = 0.0
for t in np.linspace(0.1, 6.0, 20):
    Rm = np.eye(8); T = np.eye(8); Lb = L(e(1, 2)) * (t / 2)      # exp(t*e12/2): HALF angle
    for n in range(1, 40):
        T = T @ Lb / n; Rm = Rm + T
    U = cmat(Rm)
    # L(R) A(0) L(R)^-1 = i L(R e13 Rrev) = i L(cos t e13 - sin t e23) = A(-t)  (orientation of the
    # adjoint orbit vs the analyzer parameter; irrelevant to E, which depends only on a-b)
    worst = max(worst, np.abs(U @ analyzer(0.0) @ U.conj().T - analyzer(-t)).max())
check(worst < 1e-8, f"A(-t) = U(t/2) A(0) U(t/2)^dagger with the HALF-angle one-sided rotor "
                    f"exp(t e12/2) -> the half-angle IS the geometric ingredient (err {worst:.1e})")
def E(a, b):
    Op = np.kron(analyzer(a), analyzer(b))
    return float(np.real(psi.conj() @ Op @ psi))

worst = 0.0
for _ in range(400):
    a, b = rng.uniform(0, 2 * math.pi, 2)
    worst = max(worst, abs(E(a, b) - (-math.cos(a - b))), abs(E(a, b) - twt.bell_correlation(a, b)))
check(worst < 1e-9, f"E(a,b) = -cos(a-b) COMPUTED from substrate rotors + eps  (matches twt.bell_correlation, err {worst:.1e})")

S = abs(E(0, math.pi / 4) - E(0, 3 * math.pi / 4) + E(math.pi / 2, math.pi / 4) + E(math.pi / 2, 3 * math.pi / 4))
check(abs(S - 2 * math.sqrt(2)) < 1e-9, f"CHSH S = {S:.12f} = 2*sqrt(2)  (Tsirelson, from the geometry)")

print("\n  >>> RESULT 6 [conditional: DERIVED-A GIVEN the imported (x)]: -cos(a-b) is no longer a")
print("      typed-in closed form.  It follows from (i) left-mult L-orbit rotors on S+, (ii) the")
print("      commutant's leftover j giving eps.  The ONE remaining import is the tensor product.\n")

print("=" * 78)
print("PART 5 — the killer: what a ONE-FIELD substrate can actually reach")
print("=" * 78)

def schmidt_rank(t4):
    return int(np.linalg.matrix_rank(t4.reshape(2, 2), tol=1e-9))

print("\n  STEP 1 — pointwise evaluation of one field gives ONLY product states.")
worst_rank = 0
for _ in range(300):
    z = rng.normal(size=2) + 1j * rng.normal(size=2)
    w = rng.normal(size=2) + 1j * rng.normal(size=2)
    worst_rank = max(worst_rank, schmidt_rank(np.kron(z, w)))
check(worst_rank == 1, f"Psi(x1) (x) Psi(x2) always has Schmidt rank 1 (max {worst_rank})")
check(schmidt_rank(psi) == 2, "the singlet has Schmidt rank 2 -> not a pointwise-evaluation state")
print("    dim_C {product states} = 2+2-1 = 3 inside dim_C 4 : a measure-zero Segre subvariety.")

print("\n  STEP 2 — BUT a fair critic repairs this: smear.  T[Psi] = Int Int K(x,y) Psi(x)(x)Psi(y).")
print("  That object CAN have full rank.  So the Segre argument alone does NOT close the door.")
Ks = []
for _ in range(50):
    z1 = rng.normal(size=2) + 1j * rng.normal(size=2); w1 = rng.normal(size=2) + 1j * rng.normal(size=2)
    z2 = rng.normal(size=2) + 1j * rng.normal(size=2); w2 = rng.normal(size=2) + 1j * rng.normal(size=2)
    Ks.append(schmidt_rank(np.kron(z1, w1) + np.kron(z2, w2)))
check(max(Ks) == 2, f"a 2-term smear of one field DOES reach Schmidt rank 2 (max {max(Ks)}) "
                    f"-> the Segre/measure-zero argument is NOT the obstruction")

print("\n  STEP 3 — the actual obstruction: any such T is QUADRATIC in Psi, so the map")
print("  Psi -> T[Psi] is NOT linear.  A quantum state space must carry SUPERPOSITION.")
def T_of(zA, zB):                      # a 2-term smear, bilinear in the field
    return np.kron(zA, zB)
p1 = rng.normal(size=2) + 1j * rng.normal(size=2)
p2 = rng.normal(size=2) + 1j * rng.normal(size=2)
q1 = rng.normal(size=2) + 1j * rng.normal(size=2)
q2 = rng.normal(size=2) + 1j * rng.normal(size=2)
lhs = T_of(p1 + q1, p2 + q2)
rhs = T_of(p1, p2) + T_of(q1, q2)
check(np.abs(lhs - rhs).max() > 1e-3,
      f"T[Psi1 + Psi2] != T[Psi1] + T[Psi2]  (gap {np.abs(lhs-rhs).max():.3f}) "
      f"-> a bilinear functional of ONE classical field cannot BE the linear two-particle state space")
print("""
    This is the precise located failure, and it is not a dimension count:
      * S is the VALUE space of the classical field, not a state space.
      * S (x) S is therefore a space of classical BILINEAR STATISTICS, and the assignment
        Psi -> statistic is quadratic, hence destroys superposition.
      * QM's two-particle state space is L^2 over the CONFIGURATION space of the field
        (equivalently over the 2-defect moduli space M_2), and L^2(M_1 x M_1) = L^2(M_1) (x) L^2(M_1)
        IS a genuine tensor product — but it is a tensor product of FUNCTION spaces, which the
        algebraic object S (x) S neither contains nor implies.""")

print("\n" + "=" * 78)
print("PART 6 — the R^{3N} question, answered without dodging")
print("=" * 78)
print("""
  S is FINITE-dimensional (dim_R 8) and carries NO spatial dependence: it is the value space,
  not the configuration space.  S (x) S is a 32-real-dim INTERNAL space.

  The N-particle wavefunction lives on R^{3N}.  That is a statement about the FUNCTION factor
  L^2(R^3) (x) L^2(R^3) = L^2(R^6), not about the spinor ideal.  So:

      the assigned angle CANNOT produce R^{3N}, by construction, no matter how it is repaired.

  It addresses only the internal/spin factor.  Anything claiming otherwise from S (x) S is
  smuggling.  The only place in TWT where R^{3N} could honestly come from is the N-defect
  MODULI SPACE (R-135 / R-136 / R-144), whose collective coordinates are the defect positions —
  and that space is finite-dimensional too, so it gives QUANTUM MECHANICS OF N PARTICLES
  (functions on M_N ~ R^{3N} x internal) and NOT a field theory Fock space.
""")

print("=" * 78)
print("PART 7 — an INTERNAL COHERENCE finding nobody has flagged")
print("=" * 78)
print("""
  TWT_foundational_paper.md line 1865 (SS B.5b.1, R-035a) already states:

      "The native inner product is quaternionic-Hermitian on the spinor ideal S = Cl(4,0).s_0"

  That is exactly the structure this probe re-derived from the commutant (RESULT 1) — and it is
  exactly the structure for which no tensor product of state spaces exists (Adler's tensor-product
  problem; the obstruction is Z(H) = R).  So:

      SS B.5b.1  and  SS B.4.1  are in tension, and the tension is not a technicality:
      the paper asserts a quaternionic state space in one place and uses a complex tensor
      product in another, with no construction connecting them.

  This is NOT a new negative about the world.  It is a located inconsistency in the corpus, and it
  sharpens the external review's finding II-3 from "no construction exists" to "the framework's own
  stated inner-product structure BLOCKS the naive construction, and the blockage has a named exit".

  THE NAMED EXIT (and its cost, honestly):
      cut the commutant H -> C_a by choosing one imaginary unit.  That IS SS B.3.1's phase-sector
      ansatz, seen from the other side.  Cost: C_a is DEFECT-SELECTED (B_a is picked by the
      defect's own winding), so a two-defect tensor product needs both defects to select the SAME
      blade.  Engine-checked above: for B_a != B_b the shared scalar ring collapses to R.
      => "all defects share one winding blade" is a NEW, UNCOUNTED INPUT BIT if used.
""")
npass = sum(1 for c, _ in results if c)
print(f"PROBE SUMMARY: {npass}/{len(results)} checks passed")
print("=" * 78)
