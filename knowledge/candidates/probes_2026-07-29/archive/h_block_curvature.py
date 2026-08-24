"""Final: exact closed forms + gauge-invariant test (linearized Riemann) + boost relation.

Uses the CORPUS's OWN analytic hedgehog Maurer-Cartan decomposition
(texture_matter_gravity_coupling, "hedgehog_Omega"):
    Om_k = (d_k f) n  +  s c (d_k n)  -  s^2 n (d_k n)     [s=sin f, c=cos f]
plus the R-123 lock bridge  Om_4 = (omega/2c_meta) u   with u the R-127/R-128 mass axis.
All h entries are then EXACT analytic functions of x -- no finite differences in h itself.
"""
import sys, math
sys.path.insert(0, r"C:/Users/hfyae/Claude/Projects/Deepseek/knowledge/corpus")
import numpy as np
from twt import MV, e, SCALAR, I4

def g0(mv): return dict(mv.terms).get((), 0.0)
def hb(A, B): return g0(A * I4 * B)
ZERO = 0.0 * SCALAR
Q = [e(1, 4), e(2, 4), e(3, 4)]
OMEGA, CMETA = 0.8317, 1.0
ALPHA = OMEGA / (2 * CMETA)

def f_(r):  return math.pi * math.exp(-r)
def fp_(r): return -math.pi * math.exp(-r)

def geom(x):
    r = math.sqrt(sum(t*t for t in x))
    n = [x[i]/r for i in range(3)]
    f, fp = f_(r), fp_(r)
    dkf = [fp*n[k] for k in range(3)]
    dkn = [[(1.0 if i == k else 0.0)/r - n[i]*n[k]/r for i in range(3)] for k in range(3)]
    return r, n, f, dkf, dkn

def Omegas(x, lock):
    r, n, f, dkf, dkn = geom(x)
    s, c = math.sin(f), math.cos(f)
    nmv = sum((n[i]*Q[i] for i in range(3)), ZERO)
    Om = []
    for k in range(3):
        dn = sum((dkn[k][i]*Q[i] for i in range(3)), ZERO)
        Om.append(dkf[k]*nmv + (s*c)*dn - (s*s)*(nmv*dn))
    u = I4*Q[0] if lock == 'fixed' else I4*nmv
    Om.append(ALPHA*u)
    return Om

def Hfull(x, lock):
    Om = Omegas(x, lock)
    return np.array([[hb(Om[m], Om[n]) for n in range(4)] for m in range(4)])

X0 = [0.63, -0.41, 0.82]
print("="*76)
print("EXACT ANALYTIC h  (corpus's own hedgehog MC form + R-123/R-128 Om_4)")
print("="*76)
for lock in ('fixed', 'local'):
    H = Hfull(X0, lock)
    r, n, f, dkf, dkn = geom(X0)
    s, c = math.sin(f), math.cos(f)
    print("\n lock = %s   at x = %s" % (lock, X0))
    for row in H:
        print("     [" + "  ".join("%+11.7f" % v for v in row) + "]")
    print("     h_44                 = %+.3e   (EXACT 0? %s)" % (H[3,3], abs(H[3,3]) < 1e-15))
    print("     max|h_kl| (spatial)  = %.3e" % np.abs(H[:3,:3]).max())
    if lock == 'local':
        pred = [-ALPHA*dkf[k] for k in range(3)]
    else:
        pred = [-ALPHA*(n[0]*dkf[k] + s*c*dkn[k][0]) for k in range(3)]
    print("     h_4k                 = [%s]" % ", ".join("%+.8f" % H[3,k] for k in range(3)))
    print("     closed-form predict  = [%s]" % ", ".join("%+.8f" % p for p in pred))
    print("     closed-form residual = %.3e"
          % max(abs(H[3,k]-pred[k]) for k in range(3)))

print()
print("="*76)
print("GAUGE-INVARIANT TEST: LINEARIZED RIEMANN OF THE SURVIVING h")
print("   R_{mnrs} = 1/2 (d_n d_r h_ms + d_m d_s h_nr - d_n d_s h_mr - d_m d_r h_ns)")
print("   (static config: d_4 h = 0)")
print("="*76)
def d2H(x, a, b, lock, d=2e-3):
    # second derivative of the 4x4 h w.r.t. spatial a,b (indices 0..2); index 3 -> 0
    if a == 3 or b == 3:
        return np.zeros((4,4))
    if a == b:
        xp=list(x); xm=list(x); xp[a]+=d; xm[a]-=d
        return (Hfull(xp,lock) - 2*Hfull(x,lock) + Hfull(xm,lock))/d**2
    xpp=list(x); xpm=list(x); xmp=list(x); xmm=list(x)
    xpp[a]+=d; xpp[b]+=d; xpm[a]+=d; xpm[b]-=d
    xmp[a]-=d; xmp[b]+=d; xmm[a]-=d; xmm[b]-=d
    return (Hfull(xpp,lock)-Hfull(xpm,lock)-Hfull(xmp,lock)+Hfull(xmm,lock))/(4*d**2)

for lock in ('fixed', 'local'):
    D2 = {(a,b): d2H(X0,a,b,lock) for a in range(4) for b in range(4)}
    worst = 0.0; where = None
    for m in range(4):
        for nn in range(4):
            for rr in range(4):
                for ss in range(4):
                    val = 0.5*(D2[(nn,rr)][m,ss] + D2[(m,ss)][nn,rr]
                               - D2[(nn,ss)][m,rr] - D2[(m,rr)][nn,ss])
                    if abs(val) > worst:
                        worst, where = abs(val), (m,nn,rr,ss)
    print("  lock=%-6s  max |R^lin_{mnrs}| = %.6f  at indices %s   -> %s"
          % (lock, worst, where,
             "GENUINE CURVATURE (not pure gauge)" if worst > 1e-4 else "flat / pure gauge"))

print()
print("="*76)
print("BOOST RELATION:  h_44 = -2 v^k h_4k   (uniform motion; fixed lock, where h_kl=0)")
print("="*76)
def Om_moving(x, v, lock):
    Om = Omegas(x, lock)
    Om4 = Om[3] - sum((v[k]*Om[k] for k in range(3)), ZERO)   # profile translated at velocity v
    return Om[:3] + [Om4]
for v in ([0.15,0,0], [0.11,-0.07,0.19], [-0.05,0.22,0.03]):
    Om = Om_moving(X0, v, 'fixed')
    H0 = Hfull(X0, 'fixed')
    h44 = hb(Om[3], Om[3])
    pred = -2*sum(v[k]*H0[3,k] for k in range(3))
    print("  v=%-24s h_44 = %+.8f   -2 v.h_4 = %+.8f   diff %.2e"
          % (str(v), h44, pred, abs(h44-pred)))
print("  (exact because h_kl = 0 kills the O(v^2) term -- the boost drag of the 4k block IS h_44)")
