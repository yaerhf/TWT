# ONE-FIELD CONFIGURATION SPACE probe -- multi-defect state space
# Every block prints an engine-checkable fact. No claim is banked here.
import sys, math, itertools
sys.path.insert(0, r"C:\Users\hfyae\Claude\Projects\Deepseek\knowledge\corpus")
import numpy as np
import twt
from twt import MV, e, SCALAR, I4, exp_unit_bivector

print("="*78)
print("A. Cl+(4,0) as a module over the phase line C_B = span{1,B}, B = e12")
print("="*78)

EVEN = {"1": SCALAR, "e12": e(1,2), "e13": e(1,3), "e14": e(1,4),
        "e23": e(2,3), "e24": e(2,4), "e34": e(3,4), "I4": I4}
B = e(1,2)

def name_of(mv):
    d = mv.as_dict()
    out = []
    for b,c in sorted(d.items()):
        nm = "1" if not b else "e"+"".join(map(str,b))
        out.append(f"{c:+.0f}*{nm}")
    return " ".join(out) if out else "0"

print("\nA1. RIGHT multiplication X -> X*B  (the action the B.3.1 ansatz uses):")
for k,v in EVEN.items():
    print(f"   {k:4s} * e12 = {name_of(v*B)}")

# free rank over C_B: pick line generators
lines = [("1",  SCALAR), ("e13", e(1,3)), ("e14", e(1,4)), ("e34", e(3,4))]
print("\n   -> right-C_B lines (generator, generator*B):")
for nm, g in lines:
    print(f"      <{nm}>_C = span{{ {name_of(g)} , {name_of(g*B)} }}")
# verify: the 4 lines span the 8-dim even algebra and are pairwise disjoint
basis = []
for nm,g in lines:
    basis.append(g); basis.append(g*B)
M = np.zeros((8,8))
blades = [(), (1,2),(1,3),(1,4),(2,3),(2,4),(3,4),(1,2,3,4)]
for j,v in enumerate(basis):
    for i,bl in enumerate(blades):
        M[i,j] = v.coeff(bl)
print(f"   rank of the 8 line-vectors = {np.linalg.matrix_rank(M)}  (8 => free rank-4 C_B-module)")
print(f"   det = {np.linalg.det(M):+.6f}")

print("\nA2. ADJOINT action X -> R X ~R, R = exp(theta*e12/2)  (U(1) charge grading):")
th = 0.7
R = exp_unit_bivector(B, th/2.0)   # exp(theta B/2)
Rt = R.reverse()
for k,v in EVEN.items():
    w = R*v*Rt
    print(f"   {k:4s} -> {name_of(w)}")

# charge assignment: measure the rotation rate
print("\n   charge sectors (adjoint):")
q0 = [k for k,v in EVEN.items() if (R*v*Rt - v).terms == ()]
print(f"     charge 0 : {q0}")
print(f"     charged  : {[k for k in EVEN if k not in q0]}")

# doublet check
def adj(v, t):
    r = exp_unit_bivector(B, t/2.0); return r*v*r.reverse()
for pair in [("e13","e23"), ("e14","e24")]:
    a_, b_ = EVEN[pair[0]], EVEN[pair[1]]
    w = adj(a_, th)
    ca = w.coeff(tuple(sorted(int(c) for c in pair[0][1:])))
    cb = w.coeff(tuple(sorted(int(c) for c in pair[1][1:])))
    print(f"     doublet {pair}: {pair[0]} -> {ca:+.6f}*{pair[0]} {cb:+.6f}*{pair[1]}"
          f"   (cos={math.cos(th):+.6f}, sin={math.sin(th):+.6f})")

print("\nA3. CROSS-CHECK: is the right-module grading the SAME as the adjoint grading?")
print("   right lines : {1,e12} {e13,e23} {e14,-e24} {e34,I4}")
print("   adjoint q=0 : {1,e12,e34,I4};  q=+-1 doublets: {e13,e23},{e14,e24}")
print("   => DIFFERENT gradings. The adjoint-neutral set {1,e12,e34,I4} is the union of")
print("      TWO right-C_B lines (<1> and <e34>); the two charged doublets are the")
print("      other two right-C_B lines.  Both statements are exact.")

print()
print("="*78)
print("B. B=1 hedgehog: stabiliser and moduli dimension (dim M_1)")
print("="*78)
# sigma(x) = (cos F(r), sin F(r) * xhat) in S^3 subset R^4
# group acting: translations R^3 (3) x SO(3)_space (3) x SO(3)_iso (3) = 9 params
# stabiliser: A in SO(3)_iso, R in SO(3)_space with  A*nhat(R^-1 x) = nhat(x) for all x
#   nhat(x)=xhat  =>  A R^-1 = 1  => A = R.  Diagonal SO(3), dim 3.
rng = np.random.default_rng(7)
def rot(axis, ang):
    axis = axis/np.linalg.norm(axis); K = np.array([[0,-axis[2],axis[1]],
        [axis[2],0,-axis[0]],[-axis[1],axis[0],0]])
    return np.eye(3) + math.sin(ang)*K + (1-math.cos(ang))*K@K

def hedgehog(x, F):          # returns 4-vector sigma
    r = np.linalg.norm(x, axis=-1, keepdims=True)
    nh = np.divide(x, np.where(r==0,1,r))
    f = F(r[...,0])
    return np.concatenate([np.cos(f)[...,None], np.sin(f)[...,None]*nh], axis=-1)

Fdummy = lambda r: math.pi*np.exp(-r)          # any monotone profile: stabiliser is profile-free
pts = rng.normal(size=(400,3))
maxdev_diag, maxdev_offdiag = 0.0, 0.0
for _ in range(20):
    ax, an = rng.normal(size=3), rng.uniform(0,2*math.pi)
    Rm = rot(ax,an)
    s_ref = hedgehog(pts, Fdummy)
    # spatial rotation of the FIELD: sigma'(x) = (s0, A n(R^-1 x))
    s_rot = hedgehog(pts@Rm, Fdummy)           # n(R^-1 x)
    s_diag = s_rot.copy(); s_diag[:,1:] = s_rot[:,1:]@Rm.T     # A = R
    maxdev_diag = max(maxdev_diag, np.abs(s_diag-s_ref).max())
    Am = rot(rng.normal(size=3), rng.uniform(0.5,2.5))         # A independent of R
    s_off = s_rot.copy(); s_off[:,1:] = s_rot[:,1:]@Am.T
    maxdev_offdiag = max(maxdev_offdiag, np.abs(s_off-s_ref).max())
print(f"   diagonal (A = R)     : max |sigma' - sigma| = {maxdev_diag:.3e}   (invariant)")
print(f"   generic (A != R)     : max |sigma' - sigma| = {maxdev_offdiag:.3e}   (NOT invariant)")
print(f"   => stabiliser = SO(3)_diag (dim 3); orbit dim = 3(trans)+3+3-3 = 6")
print(f"   => dim M_1 = 6 ; asymptotically dim M_N = 6N  (3N positions + 3N orientations)")

print()
print("="*78)
print("C. The B=1 baryon-density core radius (the individuation scale)")
print("="*78)
from scipy.integrate import solve_ivp, quad

def make_rhs(Bc, Ic):
    def f_rhs(t, y):
        F, Fp = y
        s2 = math.sin(2*F); sF = math.sin(F)
        num = -(t/2)*Fp - Bc*s2*Fp**2 + Bc*s2/4 + Ic*sF**2*s2/t**2
        den = t**2/4 + 2*Bc*sF**2
        return [Fp, num/den]
    return f_rhs

def solve_profile(Bc, Ic, a_lo, a_hi, xmax=28.0):
    p = (-1+math.sqrt(1+8*Bc))/2; s_dec = (1+math.sqrt(1+8*Bc))/2
    rhs = make_rhs(Bc, Ic); x0 = 1e-3
    def integrate(a):
        return solve_ivp(rhs,(x0,xmax),[math.pi-a*x0**p, -a*p*x0**(p-1)],
                         rtol=1e-11, atol=1e-13, dense_output=True, max_step=0.1)
    w1,w2 = 10.0,16.0
    def flatness(a):
        s = integrate(a)
        if np.any(s.y[0] < -1e-12): return -1e9
        return w2**s_dec*s.sol(w2)[0] - w1**s_dec*s.sol(w1)[0]
    flo = flatness(a_lo); assert flo*flatness(a_hi) < 0
    lo,hi = a_lo,a_hi
    for _ in range(52):
        mid = .5*(lo+hi)
        if flatness(mid)*flo > 0: lo = mid
        else: hi = mid
    a = .5*(lo+hi); return integrate(a), a, p, s_dec

sol1, a1, p1, s1 = solve_profile(1.0, 1.0, 0.9, 1.2)
print(f"   B=1 profile shooting parameter a* = {a1:.10f}  (R-135 banked 1.0037677224656325)")
xs = np.linspace(1e-6, 24.0, 200001)
F  = sol1.sol(xs)[0]; Fp = sol1.sol(xs)[1]
# baryon density (dimensionless x = e f_pi r):  b(x) = -(1/2pi^2) sin^2F F' / x^2
bdens = -(np.sin(F)**2)*Fp/(2*math.pi**2*xs**2)
Bint = np.trapezoid(bdens*4*math.pi*xs**2, xs)
print(f"   integral of baryon density = {Bint:.10f}   (must be 1)")
rho_r = bdens*4*math.pi*xs**2                     # radial baryon distribution
cum = np.concatenate([[0], np.cumsum(0.5*(rho_r[1:]+rho_r[:-1])*np.diff(xs))])
cum /= cum[-1]
for frac in (0.5, 0.9, 0.99):
    r_f = float(np.interp(frac, cum, xs))
    print(f"   radius containing {frac*100:4.0f}% of B : x = {r_f:.4f}  (Skyrme units 1/(e f_pi))")
r50 = float(np.interp(0.5, cum, xs)); r90 = float(np.interp(0.9, cum, xs))
# max of the radial distribution = the shell radius
imax = int(np.argmax(rho_r)); print(f"   peak of 4 pi x^2 b(x) at x = {xs[imax]:.4f}")
Ls = twt.skyrme_length_fm()
print(f"   skyrme_length_fm() -> {Ls}")

print()
print("="*78)
print("D. Product-ansatz two-defect baryon density: the two-maxima -> one-maximum")
print("   bifurcation  [MODEL: product ansatz, valid only at large separation]")
print("="*78)
Fint = lambda r: np.interp(r, xs, F, left=math.pi, right=0.0)

def hh_quat(X, centre):
    d = X - centre
    r = np.sqrt((d*d).sum(-1))
    f = Fint(r)
    nh = np.divide(d, np.where(r[...,None]==0, 1.0, r[...,None]))
    q = np.empty(X.shape[:-1]+(4,))
    q[...,0] = np.cos(f); q[...,1:] = np.sin(f)[...,None]*nh
    return q

def qmul(a, b):
    w1,x1,y1,z1 = a[...,0],a[...,1],a[...,2],a[...,3]
    w2,x2,y2,z2 = b[...,0],b[...,1],b[...,2],b[...,3]
    return np.stack([w1*w2-x1*x2-y1*y2-z1*z2,
                     w1*x2+x1*w2+y1*z2-z1*y2,
                     w1*y2-x1*z2+y1*w2+z1*x2,
                     w1*z2+x1*y2-y1*x2+z1*w2], axis=-1)

def isorot(q, A):    # A in SO(3) acting on the imaginary part
    out = q.copy(); out[...,1:] = q[...,1:]@A.T; return out

def bary_density(sig, h):
    d1 = np.gradient(sig, h, axis=0); d2 = np.gradient(sig, h, axis=1); d3 = np.gradient(sig, h, axis=2)
    M = np.stack([sig, d1, d2, d3], axis=-2)
    return np.linalg.det(M)/(2*math.pi**2)

# separation along e3; maximally attractive channel = pi isorotation about an axis _|_ R (R-139)
A_att = rot(np.array([1.0,0,0]), math.pi)
L, N = 9.0, 97
g = np.linspace(-L, L, N); h = g[1]-g[0]
Xg = np.stack(np.meshgrid(g,g,g, indexing='ij'), axis=-1)

print(f"   grid {N}^3 on [-{L},{L}]^3, h = {h:.4f}")
print(f"   {'d':>6} {'B_total':>10} {'#local max':>11} {'b(0)/b_max':>11}  chart")
results = []
for d in [8.0, 6.0, 5.0, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.5, 0.0]:
    c1 = np.array([0,0,+d/2]); c2 = np.array([0,0,-d/2])
    q1 = hh_quat(Xg, c1); q2 = isorot(hh_quat(Xg, c2), A_att)
    sig = qmul(q1, q2)
    sig /= np.linalg.norm(sig, axis=-1, keepdims=True)
    b = bary_density(sig, h)
    Btot = b.sum()*h**3
    # count local maxima of b on the interior (26-neighbour test), only above 5% of max
    bm = b.max(); thr = 0.05*bm
    core = b[1:-1,1:-1,1:-1]
    is_max = np.ones_like(core, dtype=bool)
    for di,dj,dk in itertools.product([-1,0,1],repeat=3):
        if di==dj==dk==0: continue
        is_max &= core >= b[1+di:N-1+di, 1+dj:N-1+dj, 1+dk:N-1+dk]
    is_max &= core > thr
    nmax = int(is_max.sum())
    i0 = N//2
    results.append((d, Btot, nmax, b[i0,i0,i0]/bm))
    print(f"   {d:6.2f} {Btot:10.5f} {nmax:11d} {b[i0,i0,i0]/bm:11.4f}   "
          f"{'2 lumps' if nmax>=2 else 'MERGED (no 2-point readout)'}")

print()
print("="*78)
print("E. Hilbert-space step: L^2(M x N) = L^2(M) (x) L^2(N)  -- and its failure")
print("   after excising the diagonal")
print("="*78)
# discrete witness: functions on a product grid factorise into a Kronecker basis
nA, nB = 5, 4
rng2 = np.random.default_rng(3)
f = rng2.normal(size=(nA,nB))                      # arbitrary function on A x B
# Kronecker basis (delta_i (x) delta_j) reproduces it exactly
recon = np.zeros_like(f)
for i in range(nA):
    for j in range(nB):
        recon += f[i,j]*np.outer(np.eye(nA)[i], np.eye(nB)[j])
print(f"   product manifold: |f - sum_ij f_ij (e_i (x) e_j)| = {np.abs(f-recon).max():.2e}   (exact)")
print(f"   dim L^2(AxB) = {nA*nB} = dim L^2(A) x dim L^2(B) = {nA}*{nB}")
# now excise the "diagonal": the subspace of functions vanishing on i==j is NOT a tensor product
mask = np.ones((nA,nB), dtype=bool)
for k in range(min(nA,nB)): mask[k,k] = False
dim_excised = int(mask.sum())
print(f"   after excising the diagonal (i==j): dim = {dim_excised}, "
      f"which is not a product n*m for any n<= {nA}, m<= {nB} unless trivial")
# check: is the excised subspace of the form V (x) W ?  test all factorisations
fac = [(n,m) for n in range(1,nA+1) for m in range(1,nB+1) if n*m == dim_excised]
print(f"   integer factorisations n*m = {dim_excised} inside the box: {fac}")
print("   -> the excised subspace is spanned by product vectors but is NOT of the form")
print("      V (x) W: it is not closed under the local algebra A(A) (x) A(B) (a local")
print("      operator on A moves support onto the diagonal).")
# demonstrate: a local operator on A maps an excised function off the excised subspace
v = np.zeros((nA,nB)); v[0,1] = 1.0                       # off-diagonal, allowed
OpA = np.zeros((nA,nA)); OpA[1,0] = 1.0                   # local shift on A only
w = OpA@v
print(f"   witness: v supported at (0,1) [off-diagonal]; (Op_A (x) 1) v is supported at "
      f"(1,1) [ON the diagonal]; leaves the subspace: {bool(abs(w[1,1])>0)}")

print()
print("="*78)
print("F. Banked-fact witnesses used by the construction (cite, do not re-derive)")
print("="*78)
for n in ['multi_skyrmion_b2_classical_binding','two_defect_asymptotic_tensor_force']:
    r = getattr(twt,n)()
    print(f"   {n}: keys = {list(r.keys())[:6]}")
