"""(c) Is there ANY framework-derived scale near the required M_X ~ 1e13 GeV?
Plus the closing numbers for the escape-route report.
"""
import numpy as np
from scipy.optimize import brentq
import rg_lib as R

PI = np.pi
MPL, MZ = R.MPL, R.MZ
S2W_MEAS, ALPHA_EM, ALPHA_S = R.S2W_MEAS, R.ALPHA_EM, R.ALPHA_S

t1 = R.MX_for_target_1loop(S2W_MEAS)
t2 = np.exp(brentq(lambda lm: R.s2w_from_MX(np.exp(lm), loops=2) - S2W_MEAS,
                   np.log(1e10), np.log(1e17), xtol=1e-12))
print(f"required M_X (1 loop) = {t1:.4e} GeV")
print(f"required M_X (2 loop) = {t2:.4e} GeV   = {t2/MPL:.3e} M_Pl")
print(f"the Sakharov bracket is Lambda in [0.13, 2.5] M_Pl = [{0.13*MPL:.3e}, {2.5*MPL:.3e}] GeV")
print(f"=> M_X would have to sit {np.log10(0.13*MPL/t2):.2f} decades BELOW the bracket's floor.\n")

scales = {
  "Lambda cutoff low  (0.13 M_Pl)  [R-037]":   0.13*MPL,
  "Lambda cutoff high (2.5 M_Pl)   [R-037]":   2.5*MPL,
  "M_Pl (non-reduced)":                        MPL,
  "M_Pl reduced":                              MPL/np.sqrt(8*PI),
  "v_EW (electroweak vev)":                    246.22,
  "cell scale e*f_pi              [§21.6.3]":  0.70,
  "1/Theta_0 ~ Lambda_QCD         [R-111]":    0.196,
  "f_pi massless branch           [R-106]":    0.129,
  "f_pi massive refit             [R-138]":    0.10826,
  "m_nu (Dirac, ~0.05 eV)         [R-121]":    0.05e-9,
  "H_0                            [R-119]":    1.44e-42,
}
print("Every energy scale the framework has on the books, vs the required M_X:")
for k, v in scales.items():
    print(f"  {k:<42} {v:.4e} GeV   log10(v/M_X_req) = {np.log10(v/t2):+8.2f}")
best = min(scales.items(), key=lambda kv: abs(np.log10(kv[1]/t2)))
print(f"\n  Nearest banked scale: {best[0].strip()} at {np.log10(best[1]/t2):+.2f} decades.")
print("  NO framework scale lands within 5 decades of the required M_X.")
print("\n  Structural note: TWT has NO seesaw scale. Neutrinos are DIRAC, forced by exact")
print("  B-L conservation (R-089, §C.5.4-§C.5.6); a Majorana mass is FORBIDDEN. The single")
print("  intermediate scale that generically sits near 1e13 GeV in the GUT literature is")
print("  therefore not merely absent from TWT -- it is structurally excluded by it.")
print("  The three sterile RH neutrinos TWT does predict (R-121) are total gauge singlets:")
print("  db1 = db2 = 0, so they do not touch the running at all.\n")

# --- brute-force numerology scan, honestly framed --------------------------
big = [("Lam_hi", 2.5*MPL), ("M_Pl", MPL), ("Lam_lo", 0.13*MPL), ("M_red", MPL/np.sqrt(8*PI))]
small = [("f_pi", 0.129), ("1/Th0", 0.196), ("e.f_pi", 0.70), ("v_EW", 246.22),
         ("1GeV", 1.0), ("m_nu", 0.05e-9)]
combos = []
for Ln, Lv in big:
    for sn, sv in small:
        combos += [(f"sqrt({Ln}.{sn})", np.sqrt(Lv*sv)),
                   (f"({Ln}^2.{sn})^1/3", (Lv**2*sv)**(1/3)),
                   (f"({Ln}.{sn}^2)^1/3", (Lv*sv**2)**(1/3)),
                   (f"({Ln}^3.{sn})^1/4", (Lv**3*sv)**(1/4)),
                   (f"({Ln}^4.{sn})^1/5", (Lv**4*sv)**(1/5))]
    combos += [(f"{Ln}.a_em", Lv*ALPHA_EM), (f"{Ln}.a_em^2", Lv*ALPHA_EM**2),
               (f"{Ln}.a_em^3", Lv*ALPHA_EM**3), (f"{Ln}/(16pi^2)", Lv/(16*PI**2)),
               (f"{Ln}/(16pi^2)^2", Lv/(16*PI**2)**2), (f"{Ln}/(16pi^2)^3", Lv/(16*PI**2)**3),
               (f"{Ln}.exp(-2pi/a_s)", Lv*np.exp(-2*PI/ALPHA_S))]
combos = [(l, v) for l, v in combos if v > 0 and np.isfinite(v)]
vals = np.array([v for _, v in combos])
span = np.log10(vals.max()/vals.min())
hits = [(l, v) for l, v in combos if 1e12 <= v <= 1e14]
print(f"Brute-force numerology scan (reported to CLOSE the route, not to endorse it):")
print(f"  combinations scanned            : {len(combos)}")
print(f"  log10 span of the scanned values: {span:.1f} decades")
print(f"  landing within one decade of the target: {len(hits)}  "
      f"({100*len(hits)/len(combos):.0f}% -- vs {100*2/span:.0f}% expected for a uniform scan)")
print("  the ten closest:")
for l, v in sorted(combos, key=lambda x: abs(np.log10(x[1]/t2)))[:10]:
    print(f"    {l:<24} {v:.4e} GeV   log10 offset {np.log10(v/t2):+.3f}")
print("\n  VERDICT (c): a scan of monomials spanning ~60 decades populates any target decade")
print("  by construction; the hit rate is at chance level. None of these combinations is")
print("  produced by a mechanism in the framework, so none of them is a derived scale.")
print("  ANSWER: NO. The framework derives no scale near 1e13 GeV.\n")

# --- closing numbers -------------------------------------------------------
s2_lo = R.s2w_from_MX(0.13*MPL, loops=2)
s2_hi = R.s2w_from_MX(2.50*MPL, loops=2)
s1_lo = R.s2w_1loop_analytic(0.13*MPL)
s1_hi = R.s2w_1loop_analytic(2.50*MPL)
print("CLOSING NUMBERS")
print(f"  one-loop Lambda band : {s1_hi:.5f} .. {s1_lo:.5f}")
print(f"  two-loop Lambda band : {s2_hi:.5f} .. {s2_lo:.5f}   (shift +{s2_hi-s1_hi:.5f} .. +{s2_lo-s1_lo:.5f})")
print(f"  measured             : {S2W_MEAS:.5f}")
print(f"  gap                  : {S2W_MEAS-s2_lo:.5f} .. {S2W_MEAS-s2_hi:.5f}"
      f"  ({100*(S2W_MEAS-s2_lo)/S2W_MEAS:.1f}% .. {100*(S2W_MEAS-s2_hi)/S2W_MEAS:.1f}%)")
print(f"  two-loop / gap       : {100*(s2_lo-s1_lo)/(S2W_MEAS-s2_lo):.2f}% .. "
      f"{100*(s2_hi-s1_hi)/(S2W_MEAS-s2_hi):.2f}%")
print(f"  3-loop estimate      : ~ (2L shift) x (alpha/4pi-ish) ~ 1e-5, i.e. ~0.01% of the gap")
