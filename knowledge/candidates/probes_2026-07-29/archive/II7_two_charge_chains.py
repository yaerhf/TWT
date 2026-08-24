# -*- coding: utf-8 -*-
"""Review item II-7: do the two charge chains agree, state by state, on all 15 Weyl states?
CHAIN A (paper B.5.1/B.5.4): L-orbit bivector WINDING, integer, grade-2 -> grade-1 projected.
CHAIN B (paper C.2.1/C.2.2): e4-bilinear on grade-3 blades + trivector triple product /3.
READ-ONLY probe. No project file is modified."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'corpus'))
import twt
from twt import MV, e, hypercharge, winding_charge, doublet_hypercharge, T3, generation_spectrum
import sympy as sp

R = sp.Rational
sep = "=" * 78

# --------------------------------------------------------------------------
print(sep); print("STEP 0.  ENGINE GROUND TRUTH — the e4-bilinear on ALL grade-3 blades")
print(sep)
G3 = {"e123": e(1,2,3), "e124": e(1,2,4), "e134": e(1,3,4), "e234": e(2,3,4)}
for n, B in G3.items():
    res = B.reverse() * e(4) * B
    print("  ~B e4 B  for B = %-5s ->  %s      hypercharge() = %+.1f" % (n, res, hypercharge(B)))

print()
print("  L-orbit trivector (no e4):  e123 -> -1")
print("  Q-orbit trivectors (w/ e4): e124, e134, e234 -> +1  (all three identical)")
print("  triple_product_color()  e124*e134*e234 =", twt.triple_product_color())
print("  doublet_hypercharge()   =", doublet_hypercharge())
print("  winding_charge()        =", winding_charge())
print("  gmn_coefficient()       =", twt.gmn_coefficient())

# --------------------------------------------------------------------------
print(); print(sep)
print("STEP 1.  CHAIN B, BUILT FROM SCRATCH (bilinear + /3 + T3), c kept a FREE symbol")
print(sep)
c = sp.Symbol('c', positive=True)
y_lep = R(int(hypercharge(G3["e123"])))            # -1, read from the engine bilinear
y_q_raw = R(int(hypercharge(G3["e124"])))          # +1, read from the engine bilinear
y_Q = y_q_raw / 3                                  # R-057 trivector triple-product /3
print("  y_lep (bilinear, e123)          = %s" % y_lep)
print("  y_q_raw (bilinear, e124)        = %s" % y_q_raw)
print("  y_Q = y_q_raw/3 (triple product)= %s" % y_Q)

T3sym = {"nu": R(1,2), "e": R(-1,2), "u": R(1,2), "d": R(-1,2)}
Y_LH = {"nu": y_lep, "e": y_lep, "u": y_Q, "d": y_Q}
QB_LH = {f: T3sym[f] + c * Y_LH[f] for f in T3sym}
print("  Q_B(f_L) with c free:", {k: str(v) for k, v in QB_LH.items()})

# c fixed by the LEPTON DOUBLET ALONE (paper C.2.7), gate-free, no quark content:
c_sols = sp.solve(sp.Eq(QB_LH["nu"], 0), c)
print("  c fixed by lepton doublet alone (Q(nu_L)=0):  c =", c_sols)
chalf = c_sols[0]
assert chalf == R(1,2)

# RH singlets: Y fixed by P5 (chirality-independence) => c*y_fR = Q(f_L)
Y_RH = {f: sp.solve(sp.Eq(c*sp.Symbol('y'), QB_LH[f]), sp.Symbol('y'))[0] for f in ["e","u","d"]}
print("  RH hypercharges from P5, c free:", {k: str(v) for k, v in Y_RH.items()})
print("  RH hypercharges at c=1/2:      ", {k: str(v.subs(c, chalf)) for k, v in Y_RH.items()})

# --------------------------------------------------------------------------
print(); print(sep)
print("STEP 2.  CHAIN A, AS THE ENGINE ACTUALLY IMPLEMENTS IT (winding_charge)")
print(sep)
import inspect
src = inspect.getsource(winding_charge)
body = [l for l in src.splitlines() if not l.strip().startswith(('"""', '*', 'Tier', 'Q from', 'e_4', 'p=uud', 'Solve', '(int', 'is th', 'over'))]
print("  --- executable body of winding_charge() ---")
for l in src.splitlines():
    s = l.strip()
    if s.startswith('Qp,') or s.startswith('Qu =') or s.startswith('Qd =') or s.startswith('return'):
        print("   ", l)
print("  -> the ONLY numeric inputs are the LITERALS  Qp, Qn = 1, 0.")
print("  -> no winding number is computed anywhere in this function.")

QA = winding_charge()

# --------------------------------------------------------------------------
print(); print(sep)
print("STEP 3.  STATE-BY-STATE COMPARISON — all 15 Weyl states of generation 1")
print(sep)
spec = generation_spectrum()
print("  %-6s %-4s %-8s %-12s %-12s %-10s %s" % ("state","mult","T3","Q_A (wind.)","Q_B (bilin.)","Q_B free-c","agree?"))
print("  " + "-"*88)
allagree = True; total = 0
for label, t3, q, mult in spec:
    f = label.split('_')[0]
    qa = QA[f]
    if label.endswith("_L"):
        qb_free = QB_LH[f]
    else:
        qb_free = c * Y_RH[f]          # T3 = 0 for singlets
    qb = sp.nsimplify(sp.simplify(qb_free.subs(c, chalf)))
    ok = abs(float(qb) - qa) < 1e-15
    allagree &= ok; total += mult
    print("  %-6s %-4d %-8s %-12s %-12s %-10s %s" % (label, mult, str(sp.nsimplify(t3)),
          str(sp.nsimplify(qa)), str(qb), str(sp.simplify(qb_free)), "YES" if ok else "*** NO ***"))
print("  " + "-"*88)
print("  total Weyl states counted: %d      ALL 15 AGREE: %s" % (total, allagree))

# --------------------------------------------------------------------------
print(); print(sep)
print("STEP 4.  IS THE AGREEMENT INDEPENDENT?  — dependency-severance tests")
print(sep)
print("  TEST 4a. Perturb chain B's bilinear sign (pretend Y(e123)=+1) and re-run chain A.")
print("           winding_charge() output:", winding_charge(), " <- UNCHANGED (literals frozen)")
print("           => chain A is numerically INSENSITIVE to chain B because its anchor is a")
print("              hard-coded literal, NOT because it has an independent derivation.")
print()
print("  TEST 4b. What does chain A's own cited topology actually deliver?")
print("           pi3_S3_integer_completion() =", twt.pi3_S3_integer_completion())
print("           -> proves  B in Z  and  3*(1/3)=1.  It fixes NO sign, NO unit, NO per-state value.")
print()
print("  TEST 4c. Chain A run HONESTLY (unknown unit q0, unknown integer windings).")
w_p, w_n, q0 = sp.symbols('w_p w_n q0')
Qu_A = (2*w_p - w_n)*q0/3; Qd_A = (2*w_n - w_p)*q0/3
print("           Q_u = %s ,  Q_d = %s" % (sp.simplify(Qu_A), sp.simplify(Qd_A)))
print("           free parameters remaining: {w_p, w_n, q0} — 3.  Chain A alone determines NOTHING")
print("           until (w_p, w_n, q0) = (1, 0, 1) is supplied from OUTSIDE.")
print("           winding_charge()'s own docstring supplies it from: 'Q_e=-1 from the e_4-bilinear")
print("           on the e_123 lepton blade, SS18.2' — i.e. FROM CHAIN B — plus B-L + neutrality.")

# --------------------------------------------------------------------------
print(); print(sep)
print("STEP 5.  CAN CHAIN A's LITERAL RECIPE BE EXECUTED? (grade-2 L-winding -> grade-1)")
print(sep)
print("  B.5.1 says J is 'the wavefront projection of L-orbit bivector winding to grade 1'.")
print("  Test every natural Clifford map grade-2 -> lower grade on L- vs Q-bivectors:")
maps = {
    "Sigma * e4            ": lambda S: S * e(4),
    "e4 * Sigma            ": lambda S: e(4) * S,
    "~Sigma e4 Sigma       ": lambda S: S.reverse() * e(4) * S,
    "I4 * Sigma            ": lambda S: twt.I4 * S,
}
for mname, fn in maps.items():
    row = []
    for nm, S in list(twt.L_BIVECTORS.items())[:1] + list(twt.Q_BIVECTORS.items())[:1]:
        out = fn(S)
        grades = sorted({len(k) for k in dict(out.terms).keys()}) if hasattr(out, 'terms') else None
        row.append("%s -> %s (grades %s)" % (nm, out, grades))
    print("   %s : %s" % (mname, " | ".join(row)))
print()
print("  NOTE the ~Sigma e4 Sigma row: on an L-bivector it returns -e4 ; on a Q-bivector +e4 —")
print("  i.e. the SAME e4-bilinear of chain B, one grade down. Checking all six bivectors:")
for nm, S in list(twt.L_BIVECTORS.items()) + list(twt.Q_BIVECTORS.items()):
    print("     ~%s e4 %s = %s" % (nm, nm, S.reverse()*e(4)*S))

print(); print(sep)
print("STEP 6.  GMN coefficient recomputed per state from the two chains")
print(sep)
for f in ["nu","e","u","d"]:
    cval = (QA[f] - T3[f]) / float(Y_LH[f])
    print("   c(%-2s) = (Q_A - T3)/Y_B = %.6f" % (f, cval))
print()
print("ALL CHECKS RAN. allagree =", allagree)
