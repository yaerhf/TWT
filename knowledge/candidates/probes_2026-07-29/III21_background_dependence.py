"""III-21 probe part 2: is the R-145 signature menu a property of h, or of the DELTA background?
Compare g_delta = delta_4 + h   (R-145 / B.6.6 as banked)
   with g_eta   = eta   + h,  eta = diag(-1,1,1,1)  (B.6.1's linearised Newtonian background).
READ-ONLY probe.
"""
import math, sys, os
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "corpus"))
from twt import e, SCALAR, I4

def g0(mv): return dict(mv.terms).get((), 0.0)
def hpair(A, B): return g0(A * I4 * B)
s2 = 1/math.sqrt(2)
SDb  = [s2*(e(1,2)-e(3,4)), s2*(e(1,3)+e(2,4)), s2*(e(1,4)-e(2,3))]
ASDb = [s2*(e(1,2)+e(3,4)), s2*(e(1,3)-e(2,4)), s2*(e(1,4)+e(2,3))]
def mv_exp(B, n=60):
    out = SCALAR; term = SCALAR
    for k in range(1, n):
        term = (1.0/k)*(term*B); out = out + term
    return out
rng = np.random.default_rng(11)
def rand_biv(scale=1.0):
    cs = rng.normal(size=6)*scale
    return sum((float(cs[i])*b for i, b in enumerate(SDb+ASDb)), 0.0*SCALAR)
def Om_at(Rf, x, mu, d=1e-5):
    xp=list(x); xm=list(x); xp[mu]+=d; xm[mu]-=d
    return Rf(x).reverse()*((1/(2*d))*(Rf(xp)-Rf(xm)))
def PQ(Oms):
    P = np.array([[hpair(Oms[m], Si) for m in range(4)] for Si in SDb])
    Q = np.array([[hpair(Oms[m], Aj) for m in range(4)] for Aj in ASDb])
    return P, Q
def H_of(Oms):
    return np.array([[hpair(Oms[m], Oms[n]) for n in range(4)] for m in range(4)])
def sig(gm, tol=1e-10):
    ev=np.linalg.eigvalsh(gm); return (int(np.sum(ev<-tol)), int(np.sum(ev>tol)))

delta = np.eye(4); eta = np.diag([-1.,1.,1.,1.])

print("="*78)
print("PART A -- SAME h, TWO BACKGROUNDS, OPPOSITE VERDICTS")
print("="*78)
Bs=[rand_biv(1.0) for _ in range(4)]
def make_R(lam):
    def Rf(x):
        B=sum((float(x[m])*(lam*Bs[m]) for m in range(4)),0.0*SCALAR)
        return mv_exp(B)
    return Rf
print("%-9s %-10s %-16s %-16s" % ("lam","||P||","sig(delta + h)","sig(eta + h)"))
for lam in [1e-6,1e-3,1e-2,0.1,0.3,0.5,0.7,1.0,1.5,2.0,4.0,8.0]:
    Oms=[Om_at(make_R(lam),[0.]*4,mu) for mu in range(4)]
    H=H_of(Oms); P,_=PQ(Oms)
    print("%-9.1e %-10.4f %-16s %-16s" % (lam, np.linalg.norm(P,2),
          str(sig(delta+H)), str(sig(eta+H))))
print()
print("READING: on the delta background the vacuum (lam->0) is (0,4) EUCLIDEAN and")
print("         Lorentzian needs finite amplitude.  On the eta background the vacuum is")
print("         (1,3) LORENTZIAN and finite amplitude DESTROYS it.  The R-145 threshold")
print("         statement is a property of the BACKGROUND CHOICE, not of h.")

print()
print("="*78)
print("PART B -- WHICH R-145 FACTS SURVIVE AN eta BACKGROUND?")
print("="*78)
print("R-145 fact (3a): lambda_max(g) >= 1 ALWAYS  [derived from the delta legs]")
print("R-145 fact (3c): all-timelike (4,0) STRUCTURALLY EXCLUDED")
print("Re-run both on eta + Q^T Q - P^T P over a random-frame sweep (same form as the")
print("engine's own 2000-sample sweep, only delta -> eta):")
rng2=np.random.default_rng(20260729)
maxneg_d=maxneg_e=0; lam_min_d=1e9; lam_min_e=1e9; n40_e=0; n40_d=0
seen_e={}; seen_d={}
for _ in range(20000):
    P=rng2.normal(size=(3,4))*rng2.uniform(0.2,3.0)
    Q=rng2.normal(size=(3,4))*rng2.uniform(0.2,3.0)
    M=Q.T@Q-P.T@P
    gd=delta+M; ge=eta+M
    sd=sig(gd); se=sig(ge)
    seen_d[sd]=seen_d.get(sd,0)+1; seen_e[se]=seen_e.get(se,0)+1
    maxneg_d=max(maxneg_d,sd[0]); maxneg_e=max(maxneg_e,se[0])
    lam_min_d=min(lam_min_d,float(np.max(np.linalg.eigvalsh(gd))))
    lam_min_e=min(lam_min_e,float(np.max(np.linalg.eigvalsh(ge))))
    if sd==(4,0): n40_d+=1
    if se==(4,0): n40_e+=1
print("  delta background: max negative index = %d ; min over samples of lambda_max = %.6f ; (4,0) hits = %d"
      % (maxneg_d, lam_min_d, n40_d))
print("  eta   background: max negative index = %d ; min over samples of lambda_max = %.6f ; (4,0) hits = %d"
      % (maxneg_e, lam_min_e, n40_e))
print("  signature census, delta background: %s" % sorted(seen_d.items()))
print("  signature census, eta   background: %s" % sorted(seen_e.items()))
print()
print("  => on the eta background BOTH banked structural facts FAIL: lambda_max >= 1 is")
print("     violated, and all-timelike (4,0) is REALISED.  An explicit (4,0) witness:")
# explicit (4,0) witness on eta: kill P on the timelike direction, keep Q small
Pw=np.zeros((3,4)); Pw[0,1]=1.4; Pw[1,2]=1.4; Pw[2,3]=1.4
Qw=np.zeros((3,4))
gw=eta+Qw.T@Qw-Pw.T@Pw
print("     P = 1.4*[e1,e2,e3 rows], Q = 0 :  eig(eta+M) = %s  sig = %s"
      % (np.array2string(np.linalg.eigvalsh(gw),precision=4), sig(gw)))
print("     (on the delta background the same P gives eig = %s sig = %s)"
      % (np.array2string(np.linalg.eigvalsh(delta+Qw.T@Qw-Pw.T@Pw),precision=4),
         sig(delta+Qw.T@Qw-Pw.T@Pw)))

print()
print("="*78)
print("PART C -- THE NEWTONIAN LIMIT IS ON THE eta BACKGROUND, NOT delta")
print("="*78)
print("B.6.1 (paper):  g_00 = -1 + 2GM/r ,  g_ij = (1 + 2GM/r) delta_ij")
print("  -> the 00 component sits at -1 in vacuum, i.e. background eta = diag(-1,1,1,1).")
print("R-145 / B.6.6:  g = delta_4 + h  -> g_00 = +1 + h_00 in vacuum.")
print("For the two to name the same tensor one needs h_00 = -2 + 2GM/r AT THE VACUUM,")
print("i.e. an O(1) texture at every point of empty space -- not a perturbation.")
print("Check the size of h_00 required:  h_00(needed) = %+.1f ; h_00 available at" % (-2.0))
for lam in [1e-3,1e-2,1e-1]:
    Oms=[Om_at(make_R(lam),[0.]*4,mu) for mu in range(4)]
    print("   lam=%-6.0e :  h_00 = %+.4e" % (lam, H_of(Oms)[0,0]))

print()
print("="*78)
print("PART D -- IS THE B.1 OBSERVER FRAME EVEN THE SAME 4-SPACE AS THE TEXTURE INDEX?")
print("="*78)
print("B.1.1/B.1.4: the observer's spacetime basis inside Cl(4,0) is")
print("   gamma^0 = e_4 (GRADE 1),  gamma^j = e_4 e_j (GRADE 2, the Q-orbit).")
gam=[e(4), e(4)*e(1), e(4)*e(2), e(4)*e(3)]
names=["g0=e4","g1=e4e1","g2=e4e2","g3=e4e3"]
M=np.array([[g0(gam[i]*gam[j]+gam[j]*gam[i])/2.0 for j in range(4)] for i in range(4)])
print("   induced form  <{gamma^a,gamma^b}>_0 / 2 =")
for i in range(4):
    print("      %-8s %s" % (names[i], np.array2string(M[i],precision=3,suppress_small=True)))
print("   signature of that form (n_neg,n_pos) = %s   [= eta = diag(+1,-1,-1,-1)]" % str(sig(M)))
print()
print("   The texture metric's index mu is the COORDINATE index of Om_mu = R~ d_mu R,")
print("   i.e. the four SUBSTRATE axes {x1,x2,x3,x4} whose background form is delta_4.")
print("   B.1's Lorentzian form lives on span{e4, e4e1, e4e2, e4e3} -- a MIXED-GRADE")
print("   4-space, not the substrate coordinate tangent space.  No map between the two")
print("   is constructed anywhere in the corpus (grep below).")
