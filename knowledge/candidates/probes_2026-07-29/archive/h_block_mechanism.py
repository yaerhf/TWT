"""Mechanism + stress tests.

H1. the triple-product identity  <(a b) I4 c>_0 = -det[a,b,c]  for a,b,c in span(Q)
    -> h_kl = 0 for ANY exp(n(x) f(x)) with n in span(Q), by det antisymmetry
H2. does it survive leaving the exp-class (product of two Q-exponentials)?
H3. is the surviving h_4k block PURE GAUGE (curl-free / removable)?
H4. F1 non-generic-witness check: a MOVING defect (uniform velocity) -- is h_44 still 0?
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
rng = random.Random(7)

print("="*76); print("H1. TRIPLE-PRODUCT IDENTITY on span(Q)"); print("="*76)
worst = 0.0
for _ in range(400):
    av, bv, cv = (np.array([rng.uniform(-1,1) for _ in range(3)]) for _ in range(3))
    a = sum((av[i]*Q[i] for i in range(3)), ZERO)
    b = sum((bv[i]*Q[i] for i in range(3)), ZERO)
    c = sum((cv[i]*Q[i] for i in range(3)), ZERO)
    lhs = h(a*b, c)
    rhs = -float(np.dot(np.cross(av, bv), cv))
    worst = max(worst, abs(lhs-rhs))
print("  sup | <(ab) I4 c>_0  +  det[a,b,c] |  = %.3e   (a,b,c in span Q)" % worst)
print("  => for Om_k = f_k n + sc d_k n - s^2 (n d_k n):")
print("     h_kl = s^3 c ( det[n,d_k n,d_l n] + det[n,d_l n,d_k n] ) = 0  IDENTICALLY.")

print(); print("="*76)
print("H2. h_kl = 0 for ARBITRARY span(Q)-exponential rotor fields (not just hedgehog)")
print("="*76)

def rand_smooth(seed):
    """random smooth map R^3 -> S^2 and random profile"""
    r_ = random.Random(seed)
    A = [[r_.uniform(-1,1) for _ in range(4)] for _ in range(3)]
    P = [r_.uniform(-1,1) for _ in range(4)]
    def n_of(x):
        v = np.array([A[i][0] + A[i][1]*math.sin(1.3*x[0]) + A[i][2]*math.cos(0.9*x[1])
                      + A[i][3]*math.sin(1.7*x[2]) for i in range(3)])
        return v/np.linalg.norm(v)
    def f_of(x):
        return P[0] + P[1]*math.sin(x[0]) + P[2]*x[1]*0.3 + P[3]*math.cos(1.1*x[2])
    return n_of, f_of

def Rexp(x, n_of, f_of, orbit=Q):
    nv = n_of(x); f = f_of(x)
    n = sum((nv[i]*orbit[i] for i in range(3)), ZERO)
    return math.cos(f)*SCALAR + math.sin(f)*n

def Hspatial(x, Rfun, d=1e-6):
    R = Rfun(x); Rr = R.reverse(); Om = []
    for mu in range(3):
        xp=list(x); xm=list(x); xp[mu]+=d; xm[mu]-=d
        Om.append(Rr*((1/(2*d))*(Rfun(xp)-Rfun(xm))))
    return np.array([[h(Om[m],Om[n]) for n in range(3)] for m in range(3)]), Om

mx = 0.0
for s in range(12):
    n_of, f_of = rand_smooth(s)
    for x in ([0.3,-0.7,1.1],[1.4,0.2,-0.6]):
        H,_ = Hspatial(x, lambda y: Rexp(y, n_of, f_of))
        mx = max(mx, np.abs(H).max())
print("  sup |h_kl| over 12 random smooth Q-valued exp fields x 2 points = %.3e" % mx)

# leave the exp class: product of two independent Q-exponentials
mx2 = 0.0
for s in range(12):
    n1,f1 = rand_smooth(100+s); n2,f2 = rand_smooth(200+s)
    Rf = lambda y: Rexp(y,n1,f1)*Rexp(y,n2,f2)
    for x in ([0.3,-0.7,1.1],[1.4,0.2,-0.6]):
        H,Om = Hspatial(x, Rf); mx2 = max(mx2, np.abs(H).max())
print("  sup |h_kl| for PRODUCTS of two Q-exponentials              = %.3e" % mx2)
print("  (nonzero => the vanishing is a property of the single-exponential class,")
print("   not of 'Q-orbit' as such)")

print(); print("="*76)
print("H3. IS THE SURVIVING h_4k BLOCK PURE GAUGE?")
print("="*76)
OMEGA, CMETA = 0.8317, 1.0; ALPHA = OMEGA/(2*CMETA)
def f_prof(r): return math.pi*math.exp(-r)
def nhat(x):
    r = math.sqrt(sum(t*t for t in x)); return [x[i]/r for i in range(3)]
def build(x, x4, lock):
    nv = nhat(x); r = math.sqrt(sum(t*t for t in x)); f = f_prof(r)
    n = sum((nv[i]*Q[i] for i in range(3)), ZERO)
    Rw = math.cos(f)*SCALAR + math.sin(f)*n
    u = I4*Q[0] if lock=='fixed' else I4*n
    th = OMEGA*x4/CMETA
    return Rw*(math.cos(th/2)*SCALAR + math.sin(th/2)*u)

def h4k(x, lock, d=1e-6):
    R = build(x,0.31,lock); Rr = R.reverse()
    Om=[]
    for mu in range(4):
        if mu<3:
            xp=list(x); xm=list(x); xp[mu]+=d; xm[mu]-=d
            Om.append(Rr*((1/(2*d))*(build(xp,0.31,lock)-build(xm,0.31,lock))))
        else:
            Om.append(Rr*((1/(2*d))*(build(x,0.31+d,lock)-build(x,0.31-d,lock))))
    return np.array([h(Om[3],Om[k]) for k in range(3)])

for lock in ('local','fixed'):
    x0=[0.63,-0.41,0.82]; d=1e-4
    curl = np.zeros((3,3))
    for j in range(3):
        xp=list(x0); xm=list(x0); xp[j]+=d; xm[j]-=d
        dj = (h4k(xp,lock)-h4k(xm,lock))/(2*d)
        curl[j,:] = dj
    anti = curl - curl.T
    print("  lock=%-6s  max |d_j h_4k - d_k h_4j| = %.3e  %s"
          % (lock, np.abs(anti).max(),
             "-> CURL-FREE: h_4k = d_k chi, PURE GAUGE" if np.abs(anti).max()<1e-5
             else "-> NOT a gradient: genuinely non-gauge"))

print(); print("="*76)
print("H4. F1 CHECK -- A MOVING DEFECT (uniform velocity). Is h_44 still forced 0?")
print("="*76)
def build_mov(x, x4, v, lock='local'):
    xs = [x[i]-v[i]*x4 for i in range(3)]
    nv = nhat(xs); r = math.sqrt(sum(t*t for t in xs)); f = f_prof(r)
    n = sum((nv[i]*Q[i] for i in range(3)), ZERO)
    Rw = math.cos(f)*SCALAR + math.sin(f)*n
    u = I4*Q[0] if lock=='fixed' else I4*n
    th = OMEGA*x4/CMETA
    return Rw*(math.cos(th/2)*SCALAR + math.sin(th/2)*u)

for lock in ('fixed','local'):
    for v in ([0,0,0],[0.15,0,0],[0.11,-0.07,0.19]):
        x0=[0.63,-0.41,0.82]; d=1e-6
        R=build_mov(x0,0.0,v,lock); Rr=R.reverse(); Om=[]
        for mu in range(4):
            if mu<3:
                xp=list(x0); xm=list(x0); xp[mu]+=d; xm[mu]-=d
                Om.append(Rr*((1/(2*d))*(build_mov(xp,0.0,v,lock)-build_mov(xm,0.0,v,lock))))
            else:
                Om.append(Rr*((1/(2*d))*(build_mov(x0,d,v,lock)-build_mov(x0,-d,v,lock))))
        Om4 = Om[3].grade(2)
        QL = math.sqrt(sum(ip(Om4,b)**2 for b in Q))
        print("  lock=%-6s v=%-22s h_44 = %+.6e   (Q-part of Om_4 = %.4f)"
              % (lock, str(v), h(Om[3],Om[3]), QL))
