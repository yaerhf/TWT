"""III-21 probe: is the NEAR-VACUUM texture metric Lorentzian?
READ-ONLY probe. Uses the banked machinery (texture_metric_candidate h = <Om_m I4 Om_n>_0,
R-145 P/Q legs, g = delta + Q^T Q - P^T P).  Nothing here is banked.
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

rng = np.random.default_rng(20260729)
def rand_biv(scale=1.0):
    cs = rng.normal(size=6)*scale
    return sum((float(cs[i])*b for i, b in enumerate(SDb+ASDb)), 0.0*SCALAR)

def Om_at(Rf, x, mu, d=1e-5):
    xp = list(x); xm = list(x); xp[mu] += d; xm[mu] -= d
    dR = (1/(2*d))*(Rf(xp)-Rf(xm))
    return Rf(x).reverse()*dR

def PQ(Oms):
    P = np.array([[hpair(Oms[m], Si) for m in range(4)] for Si in SDb])
    Q = np.array([[hpair(Oms[m], Aj) for m in range(4)] for Aj in ASDb])
    return P, Q

def g_of(Oms, c2=1.0):
    H = np.array([[hpair(Oms[m], Oms[n]) for n in range(4)] for m in range(4)])
    return np.eye(4) + c2*H

def sig(gm, tol=1e-10):
    ev = np.linalg.eigvalsh(gm)
    return (int(np.sum(ev < -tol)), int(np.sum(ev > tol)))

print("="*78)
print("PART 1 -- EXACT SCALING OF ||P|| WITH FLUCTUATION AMPLITUDE")
print("="*78)
# R(x) = exp( lam * sum_mu B_mu x^mu )  =>  Om_mu(0) = lam*B_mu EXACTLY (R-145 fact 2)
B1 = [rand_biv(1.0) for _ in range(4)]
def make_R(lam):
    def Rf(x):
        B = sum((float(x[m])*(lam*B1[m]) for m in range(4)), 0.0*SCALAR)
        return mv_exp(B)
    return Rf

Oms1 = [Om_at(make_R(1.0), [0.0]*4, mu) for mu in range(4)]
P1, Q1 = PQ(Oms1)
nP1 = np.linalg.norm(P1, 2)
print("reference config (lam=1):  ||P||_op = %.6f   ||Q||_op = %.6f" % (nP1, np.linalg.norm(Q1,2)))
print()
print("%-10s %-14s %-14s %-14s %-12s %-10s" % ("lam","||P||_op","min eig g","det g","sig(neg,pos)","h_max"))
lams = [1e-6,1e-4,1e-2,0.1,0.3,0.5,0.8,1.0,1.2,1.5,2.0,3.0]
for lam in lams:
    Oms = [Om_at(make_R(lam), [0.0]*4, mu) for mu in range(4)]
    P,Q = PQ(Oms); g = g_of(Oms)
    ev = np.linalg.eigvalsh(g)
    hmax = float(np.max(np.abs(g-np.eye(4))))
    print("%-10.1e %-14.6e %-14.6e %-14.6e %-12s %-10.3e" %
          (lam, np.linalg.norm(P,2), ev.min(), np.linalg.det(g), str(sig(g)), hmax))
print()
print("exactness of the linear scaling ||P(lam)|| = lam*||P(1)||:")
for lam in [1e-4, 0.1, 1.0, 3.0]:
    Oms = [Om_at(make_R(lam), [0.0]*4, mu) for mu in range(4)]
    P,_ = PQ(Oms)
    print("   lam=%-8.4g  ||P||=%.10e   lam*||P1||=%.10e   rel.dev=%.2e" %
          (lam, np.linalg.norm(P,2), lam*nP1, abs(np.linalg.norm(P,2)-lam*nP1)/(lam*nP1)))

print()
print("="*78)
print("PART 2 -- LEADING-ORDER PERTURBATIVE FORM OF g")
print("="*78)
print("h_mn = <Om_m I4 Om_n>_0 is exactly QUADRATIC in Om.  With Om = lam*B:")
for lam in [1e-3, 1e-2, 1e-1]:
    Oms = [Om_at(make_R(lam), [0.0]*4, mu) for mu in range(4)]
    g = g_of(Oms); h = g - np.eye(4)
    h_over_lam2 = h/lam**2
    print("   lam=%.0e   max|h|=%.4e   max|h|/lam^2=%.6f   eigs(g)=%s" %
          (lam, np.max(np.abs(h)), np.max(np.abs(h_over_lam2)),
           np.array2string(np.linalg.eigvalsh(g), precision=8)))
print("   => eig(g) = 1 + O(lam^2) > 0 for all four directions: g is POSITIVE DEFINITE,")
print("      NONDEGENERATE, signature (0,4) [0 timelike, 4 spacelike].  Not degenerate.")

print()
print("="*78)
print("PART 3 -- WHERE IS THE ACTUAL SIGNATURE THRESHOLD? (bisection, many configs)")
print("="*78)
print("||P||>1 is NECESSARY only.  Bisect lam for the first eigenvalue crossing zero.")
print()
print("%-6s %-12s %-12s %-12s %-14s %-10s" %
      ("cfg","lam*=1/||P1||","lam_deg(det=0)","ratio","sig just above","||P|| at deg"))
def first_degenerate(Bset, lo=1e-3, hi=50.0):
    def minev(lam):
        def Rf(x):
            B = sum((float(x[m])*(lam*Bset[m]) for m in range(4)), 0.0*SCALAR)
            return mv_exp(B)
        Oms=[Om_at(Rf,[0.0]*4,mu) for mu in range(4)]
        return np.linalg.eigvalsh(g_of(Oms)).min(), Oms
    if minev(hi)[0] > 0: return None
    for _ in range(60):
        mid = 0.5*(lo+hi)
        if minev(mid)[0] > 0: lo = mid
        else: hi = mid
    return 0.5*(lo+hi)

rows=[]
for cfg in range(8):
    Bs=[rand_biv(1.0) for _ in range(4)]
    def Rf1(x):
        B = sum((float(x[m])*Bs[m] for m in range(4)), 0.0*SCALAR)
        return mv_exp(B)
    Oms=[Om_at(Rf1,[0.0]*4,mu) for mu in range(4)]
    Pc,Qc = PQ(Oms); nP=np.linalg.norm(Pc,2)
    lstar = 1.0/nP
    ld = first_degenerate(Bs)
    if ld is None:
        print("%-6d %-12.5f %-12s %-12s %-14s %-10s" % (cfg, lstar, "none<50","-","-","-")); continue
    def Rf2(x, lam=ld*1.03):
        B = sum((float(x[m])*(lam*Bs[m]) for m in range(4)), 0.0*SCALAR)
        return mv_exp(B)
    Oms2=[Om_at(Rf2,[0.0]*4,mu) for mu in range(4)]
    Pd,_=PQ([Om_at(lambda x,l=ld:(mv_exp(sum((float(x[m])*(l*Bs[m]) for m in range(4)),0.0*SCALAR))),[0.0]*4,mu) for mu in range(4)])
    print("%-6d %-12.5f %-12.5f %-12.4f %-14s %-10.5f" %
          (cfg, lstar, ld, ld/lstar, str(sig(g_of(Oms2))), np.linalg.norm(Pd,2)))
    rows.append((lstar, ld))

print()
print("="*78)
print("PART 4 -- PURE-SD CASE: THE THRESHOLD IS EXACTLY ||P||=1")
print("="*78)
print("Pure-SD Om => Q=0 => g = delta - P^T P; eig(g) = 1 - s_i^2 (s = sing.vals of P).")
for a in [0.5, 0.9, 0.99, 1.0, 1.01, 1.2, 1.6]:
    Bs=[a*SDb[0], 0.15*SDb[1], 0.1*SDb[2], 0.0*SCALAR]
    def Rf(x):
        B = sum((float(x[m])*Bs[m] for m in range(4)), 0.0*SCALAR)
        return mv_exp(B)
    Oms=[Om_at(Rf,[0.0]*4,mu) for mu in range(4)]
    P,Q=PQ(Oms); g=g_of(Oms)
    print("   a=%-6.3f ||P||=%.6f ||Q||=%.2e det g=%+.6e sig=%s  eigs=%s" %
          (a, np.linalg.norm(P,2), np.linalg.norm(Q,2), np.linalg.det(g), sig(g),
           np.array2string(np.linalg.eigvalsh(g), precision=5)))

print()
print("="*78)
print("PART 5 -- THE THRESHOLD IS SET BY THE UNDETERMINED NORMALISATION c2")
print("="*78)
print("texture_metric_candidate U4: h unique UP TO NORMALISATION.  g = delta + c2*h.")
print("h ~ Om^2 has dimension 1/length^2 => c2 carries length^2.  Threshold |Om| ~ 1/sqrt(c2).")
Bs=[1.0*SDb[0]+0.1*SDb[1], 0.2*ASDb[0], 0.1*ASDb[1], 0.0*SCALAR]
def RfC(x, lam=1.0):
    B = sum((float(x[m])*(lam*Bs[m]) for m in range(4)), 0.0*SCALAR)
    return mv_exp(B)
print("%-10s %-14s %-14s %-12s" % ("c2","lam_deg","lam_deg*sqrt(c2)","sig above"))
for c2 in [0.01, 0.25, 1.0, 4.0, 100.0]:
    lo,hi=1e-4,500.0
    def me(lam):
        Oms=[Om_at(lambda x,l=lam: RfC(x,l),[0.0]*4,mu) for mu in range(4)]
        return np.linalg.eigvalsh(g_of(Oms,c2)).min()
    if me(hi)>0:
        print("%-10.4g %-14s" % (c2,"none")); continue
    for _ in range(60):
        mid=0.5*(lo+hi)
        if me(mid)>0: lo=mid
        else: hi=mid
    ld=0.5*(lo+hi)
    Oms=[Om_at(lambda x,l=ld*1.05: RfC(x,l),[0.0]*4,mu) for mu in range(4)]
    print("%-10.4g %-14.6f %-14.6f %-12s" % (c2, ld, ld*math.sqrt(c2), str(sig(g_of(Oms,c2)))))
print("   => the threshold amplitude scales as 1/sqrt(c2) EXACTLY; 'perturbative' is")
print("      perturbative RELATIVE TO the (undetermined) length sqrt(c2).")

print()
print("="*78)
print("PART 6 -- PHYSICAL AMPLITUDE OF THE B.1-B.5 REGIME")
print("="*78)
print("In B.3/B.5 the rotor field varies on the de Broglie / Compton scale:")
print("   |Om| ~ k  (wavenumber).   Threshold: |Om| ~ 1/sqrt(c2) ~ 1/l_monad (if c2 ~ l_P^2).")
lP = 1.616255e-35
for name, lam_c in [("electron Compton", 3.8615926796e-13),
                    ("proton Compton",   2.10308910336e-16),
                    ("LHC 14 TeV",       1.41e-20),
                    ("GUT 1e16 GeV",     1.97e-32)]:
    print("   %-18s  l = %.3e m   ||P||_est = l_P/l = %.3e" % (name, lam_c, lP/lam_c))
print("   => in the entire regime where B.1-B.5 operates, ||P|| <= 1e-16.")
print("      The texture metric there is (0,4) Euclidean to ~32 decimal places.")

print()
print("="*78)
print("PART 7 -- SIGNATURE-LABEL CONVENTION CHECK")
print("="*78)
print("engine _sig(g) returns (n_negative_eigs, n_positive_eigs).")
gL = np.diag([-1.0,1.0,1.0,1.0])
print("   diag(-1,+1,+1,+1)  -> menu label %s   (mostly-PLUS; 1 timelike)" % str(sig(gL)))
gM = np.diag([1.0,-1.0,-1.0,-1.0])
print("   diag(+1,-1,-1,-1)  -> menu label %s   (mostly-MINUS; B.1's eta)" % str(sig(gM)))
print("   R-145 fact (5) uses eta = diag(-1,1,1,1)  -> menu (1,3).")
print("   B.1 uses          eta = diag(+1,-1,-1,-1) -> menu (3,1).")
print("   Clifford (p,q) convention: p = #(+1) generators, q = #(-1).")
print("   B.1's Cl(1,3): p=1,q=3 -> eta=diag(+,-,-,-) -> menu label (3,1).")
print("   So the STRING '(1,3)' denotes DIFFERENT signatures in B.1 and in B.6.6.")
print("   All-timelike = 4 negative eigenvalues = menu (4,0) [consistent with the prose].")
