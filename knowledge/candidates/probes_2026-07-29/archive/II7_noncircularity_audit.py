# -*- coding: utf-8 -*-
"""II-7 part 2: does SSC.2.7's non-circularity argument survive?
Tests the claim '**Q** is fixed independently of GMN by the topological-winding chain'.
READ-ONLY."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'corpus'))
import twt
from twt import e, hypercharge, MV
import sympy as sp
R = sp.Rational
sep = "=" * 78

print(sep); print("TEST 1.  Can the e4-bilinear SEPARATE the two members of a doublet?")
print(sep)
print("  nu_L and e_L are BOTH carried on the single lepton blade:")
print("    twt.LEPTON_BLADE =", {k: str(v) for k, v in twt.LEPTON_BLADE.items()})
print("  so the per-blade bilinear returns ONE number for both:")
for f in ["nu", "e"]:
    print("    hypercharge(blade of %-3s) = %+.1f" % (f, hypercharge(twt.LEPTON_BLADE["e123"])))
print("  independent corroboration (banked primitive e4_conjugation_is_LQ_not_updown):")
d = twt.e4_conjugation_is_LQ_not_updown()
print("    'Q-orbit: no sub-splitting (all C4=-1)':", d["Q-orbit: no sub-splitting (all C4=-1)"])
print("    DERIVED:", d["DERIVED"][:120], "...")
print()
print("  => CONSEQUENCE: the sentence in winding_charge()'s docstring —")
print("     'Q_p=+1 anchored via Q_e=-1 from the e_4-bilinear on the e_123 lepton blade' —")
print("     CANNOT be executed. The bilinear on e123 returns -1 for nu_L and e_L ALIKE.")
print("     Getting Q(e_L)=-1 while Q(nu_L)=0 requires T3 = -+1/2 AND the functional form")
print("     Q = T3 + c*Y with c already = 1/2.  That IS the GMN relation.")

print(); print(sep)
print("TEST 2.  Parameter count: what do the two chains each DETERMINE?")
print(sep)
c = sp.Symbol('c', positive=True); q0, wp, wn = sp.symbols('q0 w_p w_n')
print("  CHAIN A (topology only: pi_3(S^3)=Z + 3-facet composition):")
print("     Q_u = q0*(2*w_p - w_n)/3, Q_d = q0*(2*w_n - w_p)/3, w_p,w_n in Z, q0 free")
print("     free parameters = 3  (w_p, w_n, q0).  Determines: a LATTICE, no value.")
print("  CHAIN B (bilinear Y + rotor T3 + functional form Q = T3 + c*Y):")
yL, yQ = R(-1), R(1,3)
QB = {"nu": R(1,2)+c*yL, "e": R(-1,2)+c*yL, "u": R(1,2)+c*yQ, "d": R(-1,2)+c*yQ}
print("     Q =", {k: str(v) for k, v in QB.items()})
print("     free parameters = 1  (c).  Determines everything up to ONE normalization.")
print()
print("  So the two chains are NOT two determinations of the same 15 numbers.")
print("  Chain A determines 0 of the 15; chain B determines all 15 up to a single scalar c.")

print(); print(sep)
print("TEST 3.  Where does c=1/2 actually come from? (three candidate anchors, each tested)")
print(sep)
print("  (a) EMPIRICAL neutrality of the neutrino  Q(nu_L)=0 :  c =", sp.solve(sp.Eq(QB["nu"],0), c))
print("      -> an INPUT datum, not a derivation.")
print("  (b) NATIVE route (S_- wave-decoupled => Y(S_-)=0, plus P5): same equation, c =",
      sp.solve(sp.Eq(QB["nu"],0), c))
print("      -> engine: charge_normalization_anchor_free tiers the 'wave-decoupled =>")
print("         gauge-decoupled => Y(S_-)=0' step as a FRAMING-SUPPORTED INFERENCE, not a closed identity.")
ye, yu, yd = sp.symbols('y_e y_u y_d')
ye_c = sp.solve(sp.Eq(c*ye, QB["e"]), ye)[0]; yu_c = sp.solve(sp.Eq(c*yu, QB["u"]), yu)[0]
yd_c = sp.solve(sp.Eq(c*yd, QB["d"]), yd)[0]
A_grav = (6*yQ + 2*yL - 3*yu - 3*yd - ye).subs({ye: ye_c, yu: yu_c, yd: yd_c})
A_cub  = (6*yQ**3 + 2*yL**3 - 3*yu**3 - 3*yd**3 - ye**3).subs({ye: ye_c}).subs({yu: yu_c}).subs({yd: yd_c})
print("  (c) ANOMALY route [registered import I-18]:")
print("      grav condition  -> c =", sp.solve(sp.Eq(A_grav, 0), c))
print("      cubic condition -> factors as", sp.factor(sp.simplify(A_cub)), "-> c =", sp.solve(sp.Eq(A_cub,0), c))
print("      -> rides ONE registered external import; both legs fall together if I-18 is struck.")
print()
print("  NOT ON THIS LIST: the topological winding chain. It supplies NO equation for c.")

print(); print(sep)
print("TEST 4.  Does the GMN tautology-circularity (Y := 2(Q - T3)) actually occur?")
print(sep)
print("  Y is computed from the e4-bilinear, with NO reference to Q anywhere:")
import inspect
for l in inspect.getsource(twt.hypercharge).splitlines():
    if 'res =' in l or 'y =' in l or 'return' in l: print("   ", l.strip())
print("  -> Y is genuinely Q-independent. The *tautology* form of circularity is ABSENT.")
print("  What is NOT independent is Q itself: the engine's Q (winding_charge) is a pair of")
print("  frozen literals whose stated justification routes back through the SAME chain B.")

print(); print(sep)
print("TEST 5.  The engine's own honest statement (already banked) — quoted verbatim")
print(sep)
doc = inspect.getdoc(twt.charge_normalization_anchor_free)
i = doc.find("The topological face")
print("   ...", doc[i:i+230].replace("\n", "\n    "))
print()
print("   -> the corpus ALREADY records the correct division of labour:")
print("      winding = PROTECTION (discreteness / drift), functional structure = NORMALIZATION.")
print("      SSC.2.7 bullet 1 ('Q is fixed independently ... by the topological-winding chain')")
print("      is inconsistent with this banked statement.")
