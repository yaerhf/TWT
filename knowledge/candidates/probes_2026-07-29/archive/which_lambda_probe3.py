"""WHICH-LAMBDA probe 3: the remaining Lambda consumers + anchor uniqueness. READ-ONLY."""
import math, io, os

MPL = 1.220910e19
MZ = 91.1876
f_inv_a = lambda cl: math.sqrt(12 * math.pi / (6 * cl))
CUR = (0.13, 2.5)
LAT = (f_inv_a(42.06), f_inv_a(11.65))
print("1/a band  = [%.4f, %.4f] M_Pl ; central %.4f (c_lat=21.8285)"
      % (LAT[0], LAT[1], f_inv_a(21.8285)))
print("Lambda_eff = %.4f M_Pl (exact sqrt(2 pi), c_lat-independent)" % math.sqrt(2 * math.pi))
print()

print("--- SC.4.5 sin^2 theta_W row: sin^2 = 3/8 - 0.0355*ln(M_X/M_Z)/(2 pi)")
s2 = lambda x: 0.375 - 0.0355 * math.log(x * MPL / MZ) / (2 * math.pi)
print("   current  Lambda in [0.13,2.5]      -> sin^2 in [%.4f, %.4f]  (paper prints 0.147-0.164)"
      % (s2(CUR[1]), s2(CUR[0])))
print("   if 1/a   in [%.3f,%.3f]            -> sin^2 in [%.4f, %.4f]"
      % (LAT[0], LAT[1], s2(LAT[1]), s2(LAT[0])))
print()

print("--- SC.4.5 'decades below the floor' (M_X required = 1.09e13 GeV)")
for nm, lo in (("current floor 0.13", 0.13), ("1/a floor %.3f" % LAT[0], LAT[0])):
    print("   %-22s -> %.2f decades" % (nm, math.log10(lo * MPL / 1.09e13)))
print()

print("--- SB.6.5 / sakharov_xi: (f_pi/Lambda)^2 with f_pi = 0.129 GeV")
for nm, l in (("Lambda_eff 2.507", math.sqrt(2 * math.pi)), ("1/a 0.5365", f_inv_a(21.8285))):
    print("   %-20s -> %.2e   (both ~1e-40; the sqrt(c_lat)=4.67 shift is irrelevant here)"
          % (nm, (0.129 / (l * MPL)) ** 2))
print()

print("--- implied_substrate_c_ceiling  (|c| <= eta4_bound * (Lambda/M_Pl)^2)")
for nm, (lo, hi) in (("current [0.13,2.5]", CUR), ("1/a band", LAT)):
    lo_c = min(1e-8 * lo ** 2, 1e-8 * hi ** 2, 1e-6 * lo ** 2, 1e-6 * hi ** 2)
    hi_c = max(1e-8 * lo ** 2, 1e-8 * hi ** 2, 1e-6 * lo ** 2, 1e-6 * hi ** 2)
    print("   %-20s -> |c| in [%.2e, %.2e]  (%.0f-to-%.0f-order suppression of an O(1) c)"
          % (nm, lo_c, hi_c, -math.log10(hi_c), -math.log10(lo_c)))
print()

print("--- N52 handle (b): 'Lambda_LV >~ 1e3 M_Pl, decoupled from the Sakharov cutoff'")
print("   the decoupling EXISTS and is computable: Lambda_LV/Lambda_S = 1/sqrt(c_lat) = %.4f"
      % (1 / math.sqrt(21.8285)))
print("   direction: DOWNWARD. It costs %.2f orders in eta4, it does not buy any."
      % math.log10(21.8285))
print()

# ---------- anchor uniqueness ----------
ROOT = r"C:\Users\hfyae\Claude\Projects\Deepseek"
anchors = {
    "companion_symbol_row": (
        os.path.join(ROOT, "knowledge", "corpus", "TWT_foundational_paper_companion.md"),
        "| `\u039b` | Planckian within O(1) | Substrate cutoff; \u00a7B.6 bracket `[0.13, 2.5] M_Pl`"),
    "paper_two_normalizations": (
        os.path.join(ROOT, "knowledge", "corpus", "TWT_foundational_paper.md"),
        "**Two normalizations, kept apart.**"),
    "engine_bracket_docline": (
        os.path.join(ROOT, "knowledge", "corpus", "twt.py"),
        "Back-fitting empirical G to 1/(16\u03c0G) = N_eff\u00b7\u039b\u00b2/(96\u03c0\u00b2) gives"),
    "paper_LV_table_row": (
        os.path.join(ROOT, "knowledge", "corpus", "TWT_foundational_paper.md"),
        "| dim-6 **isotropic** `c \u00b7 p\u2074/\u039b\u00b2`"),
}
print("--- ANCHOR OCCURRENCE COUNTS")
for k, (path, s) in anchors.items():
    txt = io.open(path, encoding="utf-8").read()
    print("   %-26s : %d   (%s)" % (k, txt.count(s), os.path.basename(path)))
