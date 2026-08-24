"""PROBE 3 — SENSITIVITY of R-163's c_lat (=> c_reg ~ 1.82, => a, => 1/a) to OA-LF-ii.

OA-LF-ii = "the continuum a_1 = R/6 curvature weight extends down to proper times s ~ a^2 up to
O(1)". R-163 reports ~93% of I_lat sits at s < a^2. Quantify HOW MUCH c_lat moves as that clause
is relaxed.

The R-linear proper-time integral is, per channel,
    I_lat = int_BZ d^4k/(2pi)^4  int_0^inf ds  w(s) exp(-s ktil^2(k)) ,   w = R/6 in the continuum.
OA-LF-ii is the assumption w(s) = R/6 for ALL s down to 0. Relax it as w(s) = (R/6) f(s/a^2) with
f -> 1 for s >> a^2. Three deformation families, all with f(inf) = 1:
    (F1) hard proper-time floor  f = theta(s - s0)          [curvature invisible below s0]
    (F2) smooth turn-on          f = s/(s + s0)             [same, analytic]
    (F3) short-time rescale      f = kappa for s < 1, else 1 [monad-scale weight is kappa, not 1]
Lattice units a = 1 throughout, so s is in units of a^2.

READ-ONLY probe. Same D4 band + midpoint-grid quadrature R-163 uses.
"""
import math
import numpy as np
from scipy.special import exp1

# --- the D4 nearest-neighbour band (identical construction to R-163) ------
pairs = []
for i in range(4):
    for j in range(i + 1, 4):
        for sg in (+1, -1):
            b = [0, 0, 0, 0]; b[i] = 1; b[j] = sg
            pairs.append(tuple(b))
assert len(pairs) == 12
M2 = np.zeros((4, 4))
for b in pairs:
    bb = np.array(b, float); M2 += 2.0 * np.outer(bb, bb)
assert np.allclose(M2, 12 * np.eye(4))

def ktil2(N):
    x = 2 * math.pi * (np.arange(N) + 0.5) / N
    axes = [x.reshape([N if k == m else 1 for k in range(4)]) for m in range(4)]
    om2 = np.zeros((N,) * 4)
    for b in pairs:
        ph = sum(bi * ax for bi, ax in zip(b, axes) if bi != 0)
        om2 += 2.0 * (1.0 - np.cos(ph))
    return om2 / 6.0

def c_of(kt, weight):
    """c_lat = 16 pi^2 * (1/2) * < int_0^inf ds f(s) e^{-s ktil^2} >_BZ"""
    return 16 * math.pi ** 2 * 0.5 * float(weight(kt).mean())

N = 32
kt = ktil2(N)
band_max = float(kt.max())

# baseline (OA-LF-ii fully assumed): int ds e^{-s q} = 1/q
c_base = c_of(kt, lambda q: 1.0 / q)
print("=" * 78)
print("PROBE 3 — OA-LF-ii sensitivity of c_lat (D4 NN band, midpoint grid N=%d)" % N)
print("=" * 78)
print("baseline c_lat (OA-LF-ii fully assumed) = %.4f   [R-163 banked 21.83]" % c_base)
print("band max ktil^2 = %.4f    c_Debye(generic guess) = 4pi = %.4f" % (band_max, 4*math.pi))

# support localization reproduction
tot = float((1.0/kt).sum())
frac_k = float((1.0/kt)[kt > 1.0].sum() / tot)
uv = float(((1.0 - np.exp(-kt)) / kt).mean()); ir = float((np.exp(-kt) / kt).mean())
print("support: frac(ktil^2 > 1) = %.4f ; frac(proper time s < a^2) = %.4f  [R-163: 0.95 / 0.93]"
      % (frac_k, uv / (uv + ir)))

def report(label, cval):
    print("   %-34s c_lat = %8.4f  (x%.3f)  c_reg=c_lat/12 = %7.4f  a = %.3f l_Pl  1/a = %.4f M_Pl"
          % (label, cval, cval / c_base, cval / 12.0,
             math.sqrt(6 * cval / (12 * math.pi)), 1.0 / math.sqrt(6 * cval / (12 * math.pi))))

# ---- F1: hard proper-time floor  int_{s0}^inf ds e^{-sq} = e^{-s0 q}/q ---
print("\n(F1) HARD PROPER-TIME FLOOR  f = theta(s - s0)  [curvature invisible below s0]")
for s0 in (0.0, 0.25, 0.5, 1.0, 2.0, 4.0):
    report("s0 = %.2f a^2" % s0, c_of(kt, lambda q, s0=s0: np.exp(-s0 * q) / q))

# ---- F2: smooth turn-on  int_0^inf s/(s+s0) e^{-sq} ds = (1/q)(1 - s0 q e^{s0 q} E1(s0 q))
print("\n(F2) SMOOTH TURN-ON  f = s/(s + s0)")
def f2(q, s0):
    x = s0 * q
    # (1/q)*(1 - x * e^{x} E1(x)) ; scipy exp1 is E1
    return (1.0 - x * np.exp(x) * exp1(x)) / q
for s0 in (0.0625, 0.25, 1.0, 4.0):
    report("s0 = %.4f a^2" % s0, c_of(kt, lambda q, s0=s0: f2(q, s0)) if s0 > 0 else c_base)

# ---- F3: short-time rescale  f = kappa for s<1, 1 for s>1 ---------------
print("\n(F3) SHORT-TIME RESCALE  f = kappa for s < a^2, f = 1 for s > a^2")
def f3(q, kap):
    return kap * (1.0 - np.exp(-q)) / q + np.exp(-q) / q
for kap in (0.0, 0.25, 0.5, 1.0, 2.0, 4.0):
    report("kappa = %.2f" % kap, c_of(kt, lambda q, k=kap: f3(q, k)))

# ---- the linearity statement -------------------------------------------
print("\nLINEARITY CHECK — c_lat(kappa) should be affine with slope = the s<a^2 support fraction:")
c0 = c_of(kt, lambda q: f3(q, 0.0)); c1 = c_base
print("   c_lat(kappa) = %.4f + %.4f * kappa   ; slope/c_base = %.4f  (= the 93%% support figure)"
      % (c0, c1 - c0, (c1 - c0) / c1))
for kap in (0.5, 2.0, 4.0):
    pred = c0 + (c1 - c0) * kap
    act = c_of(kt, lambda q, k=kap: f3(q, k))
    print("      kappa=%.2f  predicted %.4f  actual %.4f  |diff| %.2e" % (kap, pred, act, abs(pred-act)))

# ---- what does NOT move -------------------------------------------------
print("\nWHAT DOES NOT MOVE — Lambda_eff = sqrt(c_lat)/a with a = sqrt(N c_lat/(12 pi)) l_Pl:")
for cval in (c0, 5.0, c_base, 60.0):
    a = math.sqrt(6 * cval / (12 * math.pi))
    print("   c_lat = %7.3f -> Lambda_eff = %.9f M_Pl   (sqrt(2pi) = %.9f)"
          % (cval, math.sqrt(cval) / a, math.sqrt(2 * math.pi)))

# ---- honest range summary ----------------------------------------------
print("\nRANGE SUMMARY over the deformations above (excluding the pathological kappa=0):")
cands = []
for s0 in (0.25, 0.5, 1.0, 2.0):
    cands.append(c_of(kt, lambda q, s0=s0: np.exp(-s0 * q) / q))
for s0 in (0.0625, 0.25, 1.0, 4.0):
    cands.append(c_of(kt, lambda q, s0=s0: f2(q, s0)))
for kap in (0.25, 0.5, 2.0, 4.0):
    cands.append(c_of(kt, lambda q, k=kap: f3(q, k)))
cands.append(c_base)
lo, hi = min(cands), max(cands)
print("   c_lat in [%.3f, %.3f]  => c_reg = c_lat/12 in [%.4f, %.4f]" % (lo, hi, lo/12, hi/12))
print("   => a in [%.3f, %.3f] l_Pl ; 1/a in [%.4f, %.4f] M_Pl"
      % (math.sqrt(6*lo/(12*math.pi)), math.sqrt(6*hi/(12*math.pi)),
         1/math.sqrt(6*hi/(12*math.pi)), 1/math.sqrt(6*lo/(12*math.pi))))
print("   spread in c_lat: factor %.1f    (R-163's own quoted gap refinement window: -5%%..-25%%)"
      % (hi/lo))
