"""READ-ONLY probe: which index range of h_mn is actually verified zero on the baryon?

No project file is modified. Scratch only.
"""
import sys, math, random
sys.path.insert(0, r"C:/Users/hfyae/Claude/Projects/Deepseek/knowledge/corpus")
import numpy as np
import twt
from twt import MV, e, I4

def g0(mv): return dict(mv.terms).get((), 0.0)
def h(A, B): return g0(A * I4 * B)

L = [e(1,2), e(1,3), e(2,3)]
Q = [e(1,4), e(2,4), e(3,4)]

print("=== 1. orbit definitions / Hodge duals (verify canon summary) ===")
for B in Q:
    print("  I4 *", B, "=", I4*B)
for B in L:
    print("  I4 *", B, "=", I4*B)

print("\n=== 2. L x L and Q x Q I4-bilinear blocks ===")
print("  LL =", np.array([[h(a,b) for b in L] for a in L]).tolist())
print("  QQ =", np.array([[h(a,b) for b in Q] for a in Q]).tolist())
print("  LQ =", np.array([[h(a,b) for b in Q] for a in L]).tolist())

# --- exact hedgehog Maurer-Cartan, same construction as the engine primitive ---
def hedgehog_Omega(rhat, f, fp, r):
    """Om_k = R~ d_k R for R = cos f + sin f * Qhat, k = 1,2,3 (spatial)."""
    sf, cf = math.sin(f), math.cos(f)
    R = MV.from_dict({(): cf, (1,4): sf*rhat[0], (2,4): sf*rhat[1], (3,4): sf*rhat[2]})
    Rrev = MV.from_dict({(): cf, (1,4): -sf*rhat[0], (2,4): -sf*rhat[1], (3,4): -sf*rhat[2]})
    Oms = []
    for k in range(3):
        # d_k rhat_i = (delta_ik - rhat_i rhat_k)/r ;  d_k f = fp * rhat_k
        drk = [((1.0 if i == k else 0.0) - rhat[i]*rhat[k]) / r for i in range(3)]
        dkf = fp * rhat[k]
        d = {(): -dkf*sf}
        for i, bl in enumerate([(1,4), (2,4), (3,4)]):
            v = dkf*cf*rhat[i] + sf*drk[i]
            if abs(v) > 1e-16:
                d[bl] = d.get(bl, 0.0) + v
        Oms.append(Rrev * MV.from_dict(d))
    return Oms

rng = random.Random(7)

print("\n=== 3. spatial block h_kl on the hedgehog (the banked exact result) ===")
mx = 0.0
for _ in range(50):
    v = [rng.gauss(0,1) for _ in range(3)]
    n = math.sqrt(sum(x*x for x in v)); rhat = [x/n for x in v]
    f = 0.2 + 2.5*rng.random(); fp = -2.0*rng.random(); r = 0.5 + rng.random()
    Om = hedgehog_Omega(rhat, f, fp, r)
    mx = max(mx, max(abs(h(Om[k], Om[l])) for k in range(3) for l in range(3)))
print("  max |h_kl| over 50 random hedgehog configs =", mx)

print("\n=== 4. what the engine ACTUALLY asserts for the 0-row ===")
print("  check 8 uses a PURE Q-orbit representative Om_0 = e14:  h_00 =", h(e(1,4), e(1,4)))
print("  (i.e. h_00 = 0 is asserted only for Om_0 in the Q-orbit, or Om_0 = 0)")

print("\n=== 5. mass = omega: give the defect a meta-time rotor phase, Om_0 != 0 ===")
# R-127: lepton mass phase rides u = +-B_a   (L-orbit winding blade)
# R-128: quark/baryon mass phase rides u = +-I4*B_q (Hodge dual of the Q-orbit winding blade)
print("  R-128 lock axis for B_q = e14:  I4*e14 =", I4*e(1,4), " (grade-2, L-orbit)")

omega = 1.0
for label, u in [("lepton-type lock u = e12 (L-orbit)", e(1,2)),
                 ("baryon-type lock u = I4*e34 (R-128)", I4*e(3,4)),
                 ("hypothetical Q-orbit Om_0 = e14",     e(1,4))]:
    Om0 = omega * u
    print("\n  --", label)
    print("     h_00 = <Om_0 I4 Om_0>_0 =", h(Om0, Om0))
    # h_0k against the SAME hedgehog spatial MC forms, north-pole-ish config
    rhat = [0.0, 0.0, 1.0]; f = math.pi/4; fp = -1.0; r = 1.0
    Om = hedgehog_Omega(rhat, f, fp, r)
    h0k = [h(Om0, Om[k]) for k in range(3)]
    print("     h_0k =", [round(x, 6) for x in h0k])

print("\n=== 6. sweep: is h_0k generically nonzero for a meta-time-rotating baryon? ===")
worst = 0.0
for _ in range(200):
    v = [rng.gauss(0,1) for _ in range(3)]
    n = math.sqrt(sum(x*x for x in v)); rhat = [x/n for x in v]
    f = 0.2 + 2.5*rng.random(); fp = -2.0*rng.random(); r = 0.5 + rng.random()
    Om = hedgehog_Omega(rhat, f, fp, r)
    # lock axis = I4 * (Qhat), the R-128 dual of the local winding blade
    Qhat = MV.from_dict({(1,4): rhat[0], (2,4): rhat[1], (3,4): rhat[2]})
    Om0 = I4 * Qhat
    worst = max(worst, max(abs(h(Om0, Om[k])) for k in range(3)))
print("  max |h_0k| with Om_0 = omega * I4*Qhat over 200 configs =", worst)

print("\n=== 7. and h_00 for that same lock axis ===")
Qhat = MV.from_dict({(1,4): 0.0, (2,4): 0.0, (3,4): 1.0})
Om0 = I4 * Qhat
print("  Om_0 =", Om0, "  h_00 =", h(Om0, Om0))
