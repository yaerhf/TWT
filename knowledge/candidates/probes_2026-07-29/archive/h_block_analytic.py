"""ANALYTIC-ROUTE PROBE (read-only w.r.t. the corpus): which blocks of
h_{mu nu} = <Om_mu I4 Om_nu>_0 are settled by IDENTITY?

Steps:
 A. polarized form of the R-146 cross-term identity (off-diagonal, not just B,B)
 B. L closes / Q does not close  -> sector consequence for hedgehog MC forms
 C. sector assignment: R-127 (lepton) and R-128 (quark) mass-phase axes are BOTH L-orbit
 D. h_00 forced zero; h_0k closed form; h_kl for the Q-hedgehog
 E. is the banked "Q-orbit hedgehog gives h=0" a generic fact or an on-axis witness?
"""
import sys, math, random, itertools
sys.path.insert(0, r"C:/Users/hfyae/Claude/Projects/Deepseek/knowledge/corpus")
import numpy as np
from twt import MV, e, SCALAR, I4

def g0(mv): return dict(mv.terms).get((), 0.0)
def h(A, B): return g0(A * I4 * B)
def ip(A, B): return -g0(A * B)          # positive-definite on grade-2 in Cl(4,0)
def nrm(mv): return max((abs(c) for _, c in mv.terms), default=0.0)

L = [e(1, 2), e(1, 3), e(2, 3)]
Q = [e(1, 4), e(2, 4), e(3, 4)]
rng = random.Random(20260729)

def rand_span(basis):
    out = 0.0 * SCALAR
    for b in basis:
        out = out + rng.uniform(-1, 1) * b
    return out

print("=" * 72)
print("A. POLARIZED CROSS-TERM IDENTITY (R-146 off the diagonal)")
print("=" * 72)
maxLL = maxQQ = maxid = maxsym = 0.0
for _ in range(400):
    XL, XQ, YL, YQ = rand_span(L), rand_span(Q), rand_span(L), rand_span(Q)
    X, Y = XL + XQ, YL + YQ
    maxLL = max(maxLL, abs(h(XL, YL)))
    maxQQ = max(maxQQ, abs(h(XQ, YQ)))
    maxid = max(maxid, abs(h(X, Y) - (h(XL, YQ) + h(XQ, YL))))
    maxsym = max(maxsym, abs(h(X, Y) - h(Y, X)))
print("  sup |h(X_L,Y_L)|                              = %.3e" % maxLL)
print("  sup |h(X_Q,Y_Q)|                              = %.3e" % maxQQ)
print("  sup |h(X,Y) - [h(X_L,Y_Q)+h(X_Q,Y_L)]|        = %.3e" % maxid)
print("  sup |h(X,Y) - h(Y,X)|  (symmetry)             = %.3e" % maxsym)

# the mechanism: I4 maps L<->Q (Hodge), and L _|_ Q under the grade-2 inner product
print("  I4 * L -> Q ? ", all(nrm((I4 * b).grade(2)) > 0 and
                              all(abs(ip(I4 * b, l)) < 1e-12 for l in L) for b in L))
print("  I4 * Q -> L ? ", all(all(abs(ip(I4 * b, q)) < 1e-12 for q in Q) for b in Q))
print("  L _|_ Q       ? ", max(abs(ip(a, b)) for a in L for b in Q) < 1e-12)

print()
print("=" * 72)
print("B. L CLOSES UNDER COMMUTATOR; Q DOES NOT ( [Q,Q] c L )")
print("=" * 72)
def comm(a, b): return a * b - b * a
LL_leak = max(max(abs(ip(comm(a, b), q)) for q in Q) for a in L for b in L)
QQ_inL = max(max(abs(ip(comm(a, b), l)) for l in L) for a in Q for b in Q)
QQ_leak = max(max(abs(ip(comm(a, b), q)) for q in Q) for a in Q for b in Q)
print("  sup |<[L,L], Q>| (L closure leak)   = %.3e" % LL_leak)
print("  sup |<[Q,Q], Q>| (Q closure leak)   = %.3e" % QQ_leak)
print("  sup |<[Q,Q], L>| (Q -> L transfer)  = %.3e   <- nonzero: Q is NOT a subalgebra" % QQ_inL)
print("  [e14,e24] =", comm(e(1, 4), e(2, 4)).terms)

print()
print("=" * 72)
print("C. SECTOR ASSIGNMENT OF THE MASS-PHASE AXIS (R-127 lepton / R-128 quark)")
print("=" * 72)
print("  lepton  R-127: u = +-B_a,  B_a in L-orbit          -> u in span(L):",
      all(all(abs(ip(b, q)) < 1e-12 for q in Q) for b in L))
for Bq in Q:
    dual = I4 * Bq
    inL = all(abs(ip(dual, q)) < 1e-12 for q in Q)
    print("  quark   R-128: B_q=%-22s u = I4*B_q = %-24s in span(L): %s"
          % (Bq.terms, dual.terms, inL))
print("  ==> in BOTH sectors the mass-phase (meta-time rotor) axis is L-ORBIT valued.")

print()
print("=" * 72)
print("D. CONSEQUENCE: h_00 = 0 IDENTICALLY (Om_0 pure L in both sectors)")
print("=" * 72)
worst = 0.0
for _ in range(500):
    u = rand_span(L)                       # any L-orbit mass axis, any amplitude
    worst = max(worst, abs(h(u, u)))
print("  sup over 500 random L-orbit Om_0 of |h(Om_0,Om_0)| = %.3e" % worst)
print("  reason: I4*Om_0 in span(Q) and span(L) _|_ span(Q).")
