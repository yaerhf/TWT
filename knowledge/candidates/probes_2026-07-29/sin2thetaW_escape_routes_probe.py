"""
sin^2(theta_W) ESCAPE-ROUTE PROBE  (review item II-1)  -- 2026-07-29
READ-ONLY probe. No project file is modified.

TWT gets sin^2(theta_W) = 3/8 at the scale M_X where g_1 = g_2 (R-082, paper §C.4.5).
Running down with TWT's OWN spectrum (15 Weyl/gen x 3, 1 Higgs, NO superpartners)
lands at ~0.15 if M_X = Lambda (the substrate cutoff), vs measured 0.23122.
Which standard escape routes can close a ~33% gap?

  (a) TWO-LOOP running with real two-loop SM beta functions
  (b) THRESHOLD corrections -- plausible magnitude
  (c) any INDEPENDENTLY DERIVED framework scale near 1e13 GeV
  (d) how large a new-states threshold would have to be

Conventions: GUT normalization g1^2 = (5/3) g'^2, alpha_1 = (5/3) alpha_Y,
alpha_em^-1 = alpha_2^-1 + (5/3) alpha_1^-1, sin^2 = alpha_em/alpha_2.
Two-loop SM gauge betas (Machacek-Vaughn), top Yukawa at one loop.
"""
import numpy as np
from scipy.optimize import brentq
import rg_lib as R

PI = np.pi
MZ, MPL = R.MZ, R.MPL
ALPHA_EM, ALPHA_S, S2W_MEAS = R.ALPHA_EM, R.ALPHA_S, R.S2W_MEAS
b1, b2 = R.b1, R.b2


def sec(t):
    print("\n" + "=" * 84)
    print(t)
    print("=" * 84)


# ======================================================================
sec("0. SANITY -- reproduce the paper's one-loop coefficient 0.0355 and its table")
coef = (5.0/8.0) * ALPHA_EM * (b1 - b2)
print(f"  b1, b2                      = {b1}, {b2}   (SM: 41/10, -19/6)")
print(f"  b1 - b2                     = {b1-b2:.6f}   (= 109/15)")
print(f"  (5/8)*alpha_em*(b1-b2)      = {coef:.6f}    [paper: 0.0355]")
print(f"  d sin^2 / d ln M_X          = {-coef/(2*PI):.8f} per e-fold")
print(f"  M_X reproducing 0.23122     = {R.MX_for_target_1loop(S2W_MEAS):.4e} GeV  [paper: 1.0e13]")
print(f"  sin^2 at M_X = 0.13 M_Pl    = {R.s2w_1loop_analytic(0.13*MPL):.5f}")
print(f"  sin^2 at M_X = 1.00 M_Pl    = {R.s2w_1loop_analytic(MPL):.5f}")
print(f"  sin^2 at M_X = 2.50 M_Pl    = {R.s2w_1loop_analytic(2.5*MPL):.5f}  [paper band 0.147-0.164]")
g = R.run(S2W_MEAS, np.log(MZ), loops=2)
print(f"  boundary check at M_Z: g1,g2,g3 = {g[0]:.5f}, {g[1]:.5f}, {g[2]:.5f}"
      f"  (PDG ~ 0.4614, 0.6517, 1.2172)")
print(f"  numeric 1-loop shoot at M_X=M_Pl = {R.s2w_from_MX(MPL, loops=1):.14f}")
print(f"  analytic 1-loop                  = {R.s2w_1loop_analytic(MPL):.14f}   <-- agree to 1e-15")


# ======================================================================
sec("(a) TWO-LOOP RUNNING with TWT's own spectrum")
rows = []
for lab, MX in [
    ("Lambda low  (0.13 M_Pl)",  0.13*MPL),
    ("M_Pl",                     1.00*MPL),
    ("Lambda high (2.50 M_Pl)",  2.50*MPL),
    ("6.8e14  (3-coupling row)", 6.8e14),
    ("1.0e13  (fit-to-data row)",1.0e13),
]:
    s1a = R.s2w_1loop_analytic(MX)
    s1n = R.s2w_from_MX(MX, loops=1)
    s2n = R.s2w_from_MX(MX, loops=2)
    rows.append((lab, MX, s1a, s1n, s2n))
print(f"  {'M_X reading':<26} {'M_X [GeV]':>11}  {'1L analytic':>11} {'1L numeric':>11} {'2L numeric':>11} {'2L - 1L':>9}")
for lab, MX, s1a, s1n, s2n in rows:
    print(f"  {lab:<26} {MX:>11.3e}  {s1a:>11.5f} {s1n:>11.5f} {s2n:>11.5f} {s2n-s1n:>+9.5f}")

s2_lo = R.s2w_from_MX(0.13*MPL, loops=2)
s2_hi = R.s2w_from_MX(2.50*MPL, loops=2)
print(f"\n  TWO-LOOP Lambda band: sin^2(M_Z) = {s2_hi:.5f} .. {s2_lo:.5f}"
      f"   (one-loop band was {R.s2w_1loop_analytic(2.5*MPL):.5f} .. {R.s2w_1loop_analytic(0.13*MPL):.5f})")
gap_lo = S2W_MEAS - s2_lo
gap_hi = S2W_MEAS - s2_hi
print(f"  Gap to the measurement: {gap_lo:+.5f} (Lambda low) .. {gap_hi:+.5f} (Lambda high)")
print(f"                        = {100*gap_lo/S2W_MEAS:.1f}% .. {100*gap_hi/S2W_MEAS:.1f}% of 0.23122")
d2 = [r[4]-r[3] for r in rows[:3]]
print(f"\n  TWO-LOOP SHIFT over the Lambda bracket: {min(d2):+.5f} .. {max(d2):+.5f}")
print(f"  Fraction of the required shift covered by two loops: "
      f"{100*max(d2)/gap_hi:.2f}% (vs the Lambda-high gap {gap_hi:.5f})")

print("\n  Sensitivity of the two-loop shift to y_t(M_Z) (+-10%):")
for yt in (0.85, 0.95, 1.05):
    s1n = R.s2w_from_MX(MPL, loops=1, yt=yt)
    s2n = R.s2w_from_MX(MPL, loops=2, yt=yt)
    print(f"    y_t = {yt:.2f}:  1L = {s1n:.5f}   2L = {s2n:.5f}   2L-1L = {s2n-s1n:+.5f}")
print("  Sensitivity to alpha_s(M_Z) (enters sin^2 only at two loops):")
for a in (0.1150, 0.1179, 0.1210):
    s2n = R.s2w_from_MX(MPL, loops=2, alpha_s=a)
    print(f"    alpha_s = {a:.4f}:  2L = {s2n:.5f}")
print("  Sensitivity to alpha_em(M_Z) input (1/128.0 vs 1/127.951 vs 1/127.90):")
for inv in (128.0, 127.951, 127.90):
    s2n = R.s2w_from_MX(MPL, loops=2, alpha_em=1.0/inv)
    print(f"    1/alpha_em = {inv:.3f}:  2L = {s2n:.5f}")


# ======================================================================
sec("(a') Does anything actually unify? pairwise crossings at one and two loops")
for loops in (1, 2):
    print(f"  loops = {loops}, starting from the MEASURED sin^2(M_Z) = {S2W_MEAS}:")
    for (i, j, lab) in [(0, 1, "g1 = g2"), (1, 2, "g2 = g3"), (0, 2, "g1 = g3")]:
        v = R.crossing(S2W_MEAS, i, j, loops=loops)
        print(f"     {lab}: {v:.4e} GeV" if v else f"     {lab}: no crossing below 1e20 GeV")

print("\n  Self-consistent 3-coupling unification (impose g1=g2 and g2=g3 at ONE scale;")
print("  alpha_s(M_Z) and alpha_em(M_Z) held at their measured values, sin^2(M_Z) free):")
for loops in (1, 2):
    def mm(s):
        a = R.crossing(s, 0, 1, loops=loops)
        b = R.crossing(s, 1, 2, loops=loops)
        if a is None or b is None:
            return np.nan
        return np.log(a) - np.log(b)
    try:
        s_star = brentq(mm, 0.15, 0.30, xtol=1e-11)
        Mx = R.crossing(s_star, 0, 1, loops=loops)
        print(f"    loops={loops}: requires sin^2(M_Z) = {s_star:.5f} at M_X = {Mx:.4e} GeV"
              f"   [paper's 3-coupling row: 0.208 at 6.8e14]")
    except Exception as e:
        print(f"    loops={loops}: no solution ({e})")


# ======================================================================
sec("(b) THRESHOLD CORRECTIONS -- plausible magnitude")
print("  One-loop leading-log shift from extra states with (db1,db2) live above M_T:")
print("    delta sin^2 = -(5/8) alpha_em (db1-db2) ln(M_X/M_T) / (2 pi)")
print(f"    coefficient  -(5/8) alpha_em /(2pi) = {-(5.0/8.0)*ALPHA_EM/(2*PI):.3e}"
      f"   per unit of (db1-db2)*ln(M_X/M_T)\n")

def db_weyl(n_c, T2, Ys):
    return (2.0/3.0)*(3.0/5.0)*n_c*sum(y*y for y in Ys), (2.0/3.0)*n_c*T2
def db_scalar(n_c, T2, Ys):
    return (1.0/3.0)*(3.0/5.0)*n_c*sum(y*y for y in Ys), (1.0/3.0)*n_c*T2

sumY2_gen = (2*0.25 + 1.0 + 3*2*(1.0/6.0)**2 + 3*(2.0/3.0)**2 + 3*(1.0/3.0)**2)
states = {
  "extra Higgs doublet (cplx scalar, Y=1/2)": db_scalar(1, 0.5, [0.5, 0.5]),
  "extra lepton doublet (Weyl, Y=-1/2)":      db_weyl(1, 0.5, [-0.5, -0.5]),
  "SU(2) triplet Weyl fermion, Y=0 (wino)":   db_weyl(1, 2.0, [0, 0, 0]),
  "SU(2) triplet cplx scalar, Y=0":           db_scalar(1, 2.0, [0, 0, 0]),
  "singlet Weyl, Y=-1 (bino-like)":           db_weyl(1, 0.0, [-1.0]),
  "colour-triplet Weyl, Y=-1/3":              db_weyl(3, 0.0, [-1.0/3.0]),
  "one full SM generation (15 Weyl)":         ((2.0/3.0)*(3.0/5.0)*sumY2_gen, (2.0/3.0)*0.5*4),
  "full MSSM shift (SM -> MSSM b's)":         (33.0/5.0 - b1, 1.0 - b2),
}
print(f"  {'state':<44} {'db1':>8} {'db2':>8} {'db1-db2':>9}  {'d sin^2 (M_T=1 TeV, M_X=M_Pl)':>30}")
for k, (d1, d2v) in states.items():
    dd = d1 - d2v
    ds = -(5.0/8.0)*ALPHA_EM*dd*np.log(MPL/1000.0)/(2*PI)
    print(f"  {k:<44} {d1:>8.4f} {d2v:>8.4f} {dd:>+9.4f}  {ds:>+30.5f}")

print("\n  GUT-style threshold corrections proper -- heavy multiplets SPLIT around M_X.")
print("  |db1-db2| ~ O(1) acting over ln(spread) of 1-2 decades:")
for dd in (0.5, 1.0, 3.0, 10.0):
    for L, tag in ((2.3, "1 decade"), (4.6, "2 decades"), (9.2, "4 decades")):
        ds = abs((5.0/8.0)*ALPHA_EM*dd*L/(2*PI))
        print(f"    |db1-db2| = {dd:>5.1f}, ln(spread) = {L:.1f} ({tag:<9}) -> |d sin^2| = {ds:.5f}")
print(f"\n  Needed: {gap_hi:.5f} (Lambda high) / {gap_lo:.5f} (Lambda low).")
print("  MS-bar <-> DR-bar scheme conversion: d(alpha_i^-1) = -C_2(G_i)/(12 pi), i.e.")
for lab, C2 in (("U(1)_Y", 0.0), ("SU(2)", 2.0)):
    print(f"    {lab}: d alpha^-1 = {-C2/(12*PI):+.5f}")
ds_scheme = abs(-(5.0/8.0)*(2.0/(12*PI))*ALPHA_EM/1.0)
print(f"    net effect on sin^2 ~ (5/8)*alpha_em*(2/(12 pi)) = {ds_scheme:.6f}  (negligible)")


# ======================================================================
sec("(d) HOW LARGE A NEW-STATES THRESHOLD WOULD HAVE TO BE")
K = (5.0/8.0)*ALPHA_EM/(2*PI)
for MXlab, MX in [("Lambda high (2.5 M_Pl)", 2.5*MPL), ("M_Pl", MPL), ("Lambda low (0.13 M_Pl)", 0.13*MPL)]:
    LX = np.log(MX/MZ)
    total_needed = (3.0/8.0 - S2W_MEAS)/K
    resid = total_needed - (b1-b2)*LX
    print(f"\n  M_X = {MX:.3e} GeV  ({MXlab}),  ln(M_X/M_Z) = {LX:.2f}")
    print(f"    SM content supplies (b1-b2)*ln(M_X/M_Z) = {(b1-b2)*LX:8.2f}")
    print(f"    the measurement needs                     {total_needed:8.2f}")
    print(f"    => required  (db1-db2) * ln(M_X/M_T)    = {resid:+8.2f}   (must be NEGATIVE:")
    print(f"       new states must feed SU(2) MORE than U(1)_Y)")
    dlep = states["extra lepton doublet (Weyl, Y=-1/2)"]
    dtri = states["SU(2) triplet Weyl fermion, Y=0 (wino)"]
    dhig = states["extra Higgs doublet (cplx scalar, Y=1/2)"]
    for MT, tag in [(MZ, "M_Z"), (1e3, "1 TeV"), (1e6, "1e6 GeV"), (1e10, "1e10 GeV"),
                    (1e16, "1e16 GeV"), (0.1*MX, "M_X/10")]:
        LT = np.log(MX/MT)
        dd = resid/LT
        n_tri = dd/(dtri[0]-dtri[1]); n_lep = dd/(dlep[0]-dlep[1]); n_hig = dd/(dhig[0]-dhig[1])
        print(f"    M_T = {tag:<9} ln(M_X/M_T) = {LT:6.2f} -> db1-db2 = {dd:+8.3f}"
              f"  = {n_tri:6.1f} SU(2)-triplet Weyl | {n_lep:6.1f} lepton doublets | {n_hig:6.1f} Higgs doublets")

print("\n  Consequence for SU(2) asymptotic freedom (cheapest route: pure db2):")
for dd in (2.0, 2.6, 5.0, 10.0):
    newb2 = b2 + dd
    print(f"    to get db1-db2 = {-dd:+6.1f} via db2 alone: b2 = {b2:+.3f} -> {newb2:+.3f}"
          f"   ({'still asymptotically free' if newb2 < 0 else 'SU(2) LOSES asymptotic freedom'})")

print("\n  CROSS-CHECK: the historical V1 route (MSSM content).")
b1M, b2M = 33.0/5.0, 1.0
cM = (5.0/8.0)*ALPHA_EM*(b1M-b2M)
MXm = MZ*np.exp(2*PI*(3.0/8.0 - S2W_MEAS)/cM)
print(f"    MSSM b1={b1M}, b2={b2M}: coefficient (5/8)a(b1-b2) = {cM:.6f}")
print(f"    sin^2 = 3/8 - {cM:.4f} t  ->  0.23122 at M_X = {MXm:.3e} GeV   (the classic 2e16)")
print(f"    at M_X = M_Pl this MSSM formula would give {3.0/8.0 - cM*np.log(MPL/MZ)/(2*PI):.5f}"
      f"  -- so even MSSM content does NOT work at Lambda; it works at 2e16 only.")


# ======================================================================
sec("(c) IS THERE ANY FRAMEWORK-DERIVED SCALE NEAR 1.0e13 GeV?")
t1 = R.MX_for_target_1loop(S2W_MEAS)
t2 = np.exp(brentq(lambda lm: R.s2w_from_MX(np.exp(lm), loops=2) - S2W_MEAS,
                   np.log(1e10), np.log(1e17), xtol=1e-11))
print(f"  required M_X (1-loop) = {t1:.4e} GeV")
print(f"  required M_X (2-loop) = {t2:.4e} GeV      <-- the number a derived scale would have to hit")

scales = {
  "Lambda substrate cutoff, low  (0.13 M_Pl)": 0.13*MPL,
  "Lambda substrate cutoff, high (2.5 M_Pl)":  2.5*MPL,
  "M_Pl (non-reduced)":                        MPL,
  "M_Pl reduced":                              MPL/np.sqrt(8*PI),
  "v_EW":                                      246.22,
  "cell scale e*f_pi (~0.70 GeV)":             0.70,
  "1/Theta_0 ~ Lambda_QCD (196 MeV, R-111)":   0.196,
  "f_pi massless branch (129 MeV)":            0.129,
  "f_pi massive refit (108.26 MeV, R-138)":    0.10826,
  "m_nu scale (0.05 eV)":                      0.05e-9,
  "H_0":                                       1.44e-42,
}
print("\n  Every energy scale the framework has on the books:")
for k, v in scales.items():
    print(f"    {k:<44} {v:.4e} GeV     log10(v/target) = {np.log10(v/t2):+8.2f}")
print("\n  NOTE: TWT has NO seesaw scale -- neutrinos are DIRAC by exact B-L conservation")
print("  (§C.5.4-§C.5.6, R-089), so the one intermediate scale that generically sits near")
print("  1e13 GeV in the GUT literature is structurally FORBIDDEN here.")

print("\n  Brute-force scan of two-scale combinations (pure numerology, reported to close")
print("  the route, not to endorse it):")
combos = []
big = [("Lam_hi", 2.5*MPL), ("M_Pl", MPL), ("Lam_lo", 0.13*MPL), ("M_red", MPL/np.sqrt(8*PI))]
small = [("f_pi", 0.129), ("1/Theta0", 0.196), ("e_f_pi", 0.70), ("v_EW", 246.22),
         ("1GeV", 1.0), ("m_nu", 0.05e-9)]
for Ln, Lv in big:
    for sn, sv in small:
        combos.append((f"sqrt({Ln}*{sn})",           np.sqrt(Lv*sv)))
        combos.append((f"({Ln}^2*{sn})^(1/3)",       (Lv**2*sv)**(1/3)))
        combos.append((f"({Ln}*{sn}^2)^(1/3)",       (Lv*sv**2)**(1/3)))
        combos.append((f"({Ln}^3*{sn})^(1/4)",       (Lv**3*sv)**(1/4)))
for Ln, Lv in big:
    combos.append((f"{Ln}*alpha_em",          Lv*ALPHA_EM))
    combos.append((f"{Ln}*alpha_em^2",        Lv*ALPHA_EM**2))
    combos.append((f"{Ln}*alpha_em^3",        Lv*ALPHA_EM**3))
    combos.append((f"{Ln}/(16 pi^2)",         Lv/(16*PI**2)))
    combos.append((f"{Ln}/(16 pi^2)^2",       Lv/(16*PI**2)**2))
    combos.append((f"{Ln}*exp(-2pi/alpha_em)",Lv*np.exp(-2*PI/ALPHA_EM)))
    combos.append((f"{Ln}*exp(-2pi/alpha_s)", Lv*np.exp(-2*PI/ALPHA_S)))
hits = [(l, v) for l, v in combos if 1e12 <= v <= 1e14]
print(f"    combinations scanned: {len(combos)}")
print(f"    landing inside ONE DECADE of the target (1e12..1e14 GeV): {len(hits)}")
for l, v in sorted(hits, key=lambda x: abs(np.log10(x[1]/t2))):
    print(f"      {l:<28} {v:.4e} GeV   log10 offset {np.log10(v/t2):+.3f}")
print("    nearest six overall:")
for l, v in sorted(combos, key=lambda x: abs(np.log10(x[1]/t2)))[:6]:
    print(f"      {l:<28} {v:.4e} GeV   log10 offset {np.log10(v/t2):+.3f}")
print(f"\n    A blind scan of {len(combos)} two-scale monomials spanning ~60 decades will")
print( "    populate any given decade by construction; a hit here carries NO evidential weight")
print( "    unless a MECHANISM selects the combination. None of the hits has one.")

sec("SUMMARY")
print(f"  (a) two loops move sin^2 by {min(d2):+.5f} .. {max(d2):+.5f}; the gap is {gap_hi:+.5f}"
      f" -> {100*max(d2)/gap_hi:.2f}% of it.")
print(f"  (b) realistic thresholds give |d sin^2| ~ 1e-4 .. 1e-2; the gap is {gap_hi:.3f}.")
print(f"  (c) no framework-derived scale sits near {t2:.2e} GeV; the nearest banked scale is"
      f" {min(scales.values(), key=lambda v: abs(np.log10(v/t2))):.2e} GeV.")
print( "  (d) closing it needs db1-db2 ~ -2.6 from M_Z, or ~ -5 from 1e10 GeV, or ~ -15 from 1e16 GeV.")
