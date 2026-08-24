"""Block structure of h_{mu nu} for a defect, WITH the meta-time rotor restored.

Index convention: mu = 0,1,2 -> x1,x2,x3 spatial ; mu = 3 -> x4 (the wavefront/e4 axis).
On the R-123 lock x4 = c_meta*tau5, so the meta-time rotor exp(u*omega*tau5/2)
reads as an x4-rotor and contributes Om_4 = (omega/2c) * u  EXACTLY.

The engine's texture_metric_candidate (U6 / caveat (d)) sets Om_4 = 0 ("if mu>=3: return 0")
i.e. a STATIC rotor -- by canon section 0 that is a MASSLESS defect.
"""
import sys, math, random
sys.path.insert(0, r"C:/Users/hfyae/Claude/Projects/Deepseek/knowledge/corpus")
import numpy as np
from twt import MV, e, SCALAR, I4

def g0(mv): return dict(mv.terms).get((), 0.0)
def h(A, B): return g0(A * I4 * B)
def ip(A, B): return -g0(A * B)
ZERO = 0.0 * SCALAR

L = [e(1, 2), e(1, 3), e(2, 3)]
Q = [e(1, 4), e(2, 4), e(3, 4)]

def split(mv):
    m2 = mv.grade(2)
    XL = sum((ip(m2, b) * b for b in L), ZERO)
    XQ = sum((ip(m2, b) * b for b in Q), ZERO)
    return XL, XQ

def offgrade(mv):
    return max(math.sqrt(sum(c*c for _, c in mv.grade(k).terms)) for k in (0,1,3,4,5))

# ------------------------------------------------------------------ profiles
def f_prof(r):  return math.pi * math.exp(-r)
def fp_prof(r): return -math.pi * math.exp(-r)

def nhat(x, orbit):
    r = math.sqrt(sum(t*t for t in x))
    return sum((orbit[i] * (x[i]/r) for i in range(3)), ZERO)

def R_wind(x, orbit):
    r = math.sqrt(sum(t*t for t in x))
    f = f_prof(r)
    return math.cos(f)*SCALAR + math.sin(f)*nhat(x, orbit)

def rotor(u, th):
    return math.cos(th/2)*SCALAR + math.sin(th/2)*u

OMEGA, CMETA = 0.8317, 1.0
ALPHA = OMEGA/(2*CMETA)

def build_R(x, x4, orbit, lock):
    """lock: None (static, = the engine's caveat-(d) config)
             'fixed' (u = I4*B_q for a FIXED B_q -- R-128 as banked)
             'local' (u = I4*nhat(x)  -- CANDIDATE pointwise extension)
             'lepton'(u = nhat(x) itself, R-127 identity lock)"""
    Rw = R_wind(x, orbit)
    if lock is None:
        return Rw
    if lock == 'fixed':
        u = I4 * orbit[0]
    elif lock == 'local':
        u = I4 * nhat(x, orbit)
    else:
        u = nhat(x, orbit)
    return Rw * rotor(u, OMEGA*x4/CMETA)

def Hmat(x, x4, orbit, lock, d=1e-6):
    R = build_R(x, x4, orbit, lock)
    Rr = R.reverse()
    Om = []
    for mu in range(4):
        if mu < 3:
            xp = list(x); xm = list(x); xp[mu] += d; xm[mu] -= d
            dR = (1/(2*d))*(build_R(xp, x4, orbit, lock) - build_R(xm, x4, orbit, lock))
        else:
            dR = (1/(2*d))*(build_R(x, x4+d, orbit, lock) - build_R(x, x4-d, orbit, lock))
        Om.append(Rr*dR)
    H = np.array([[h(Om[m], Om[n]) for n in range(4)] for m in range(4)])
    return H, Om

GEN = [0.63, -0.41, 0.82]      # a GENERIC point, not on any axis
AXIS = [1.0, 0.0, 0.0]         # the engine's on-axis witness

def show(tag, H):
    print("  %-46s" % tag)
    for row in H:
        print("      [" + "  ".join("%+10.6f" % v for v in row) + "]")

print("="*76)
print("E. IS THE BANKED 'Q-ORBIT SKYRMION -> h = 0' GENERIC OR ON-AXIS?")
print("   (static rotor, Om_4 = 0 -- exactly the engine's caveat-(d) configuration)")
print("="*76)
for tag, x in (("on-axis  x=(1,0,0)", AXIS), ("GENERIC  x=(.63,-.41,.82)", GEN)):
    H, Om = Hmat(x, 0.0, Q, None)
    print("  %-28s  max|h| = %.3e" % (tag, np.abs(H).max()))
    XL, XQ = split(Om[1])
    print("      (Om_2 has L-part norm %.4f and Q-part norm %.4f -- Om is NOT pure Q)"
          % (math.sqrt(max(ip(XL,XL),0)), math.sqrt(max(ip(XQ,XQ),0))))

print()
print("="*76)
print("F. THE SAME DEFECT WITH THE META-TIME ROTOR RESTORED (mass = omega)")
print("="*76)
for lockname in ('fixed', 'local'):
    for tag, x in (("on-axis", AXIS), ("GENERIC", GEN)):
        H, Om = Hmat(x, 0.37, Q, lockname)
        r = math.sqrt(sum(t*t for t in x))
        print("\n  Q-orbit hedgehog, lock=%s, %s point x=%s" % (lockname, tag, x))
        show("h_{mu nu} (indices 1,2,3,4=e4):", H)
        print("      h_44                      = %+.3e   (forced 0?)" % H[3,3])
        print("      max |h_kl| (spatial 3x3)  = %.3e" % np.abs(H[:3,:3]).max())
        print("      h_4k                      = [%s]"
              % ", ".join("%+.6f" % H[3,k] for k in range(3)))
        pred = [-ALPHA*fp_prof(r)*(x[k]/r) for k in range(3)]
        print("      -(omega/2c) d_k f  predict = [%s]" % ", ".join("%+.6f" % p for p in pred))
        print("      grade-content of Om_4: off-grade %.2e ; L-norm %.4f ; Q-norm %.4f"
              % (offgrade(Om[3]),
                 math.sqrt(max(ip(*(2*(split(Om[3])[0],))),0)),
                 math.sqrt(max(ip(*(2*(split(Om[3])[1],))),0))))

print()
print("="*76)
print("G. LEPTON-SECTOR ANALOG: L-orbit winding + R-127 identity lock")
print("="*76)
for tag, x in (("on-axis", AXIS), ("GENERIC", GEN)):
    H, Om = Hmat(x, 0.37, L, 'lepton')
    leak = max(math.sqrt(max(ip(*(2*(split(O)[1],))),0)) for O in Om)
    print("  %-8s max|h| = %.3e ;  max Q-part of any Om_mu = %.3e"
          % (tag, np.abs(H).max(), leak))
