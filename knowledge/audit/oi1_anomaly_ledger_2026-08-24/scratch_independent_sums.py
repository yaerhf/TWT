"""Independent re-derivation of the SM one-generation anomaly ledger, from the
textbook table typed by hand — NOT read from the engine."""
from fractions import Fraction as F

# (label, T3, Q, colour mult, chirality)  -- textbook SM, one generation
tbl = [("nu_L", F(1,2), F(0),      1, "L"),
       ("e_L",  F(-1,2), F(-1),    1, "L"),
       ("u_L",  F(1,2), F(2,3),    3, "L"),
       ("d_L",  F(-1,2), F(-1,3),  3, "L"),
       ("e_R",  F(0),   F(-1),     1, "R"),
       ("u_R",  F(0),   F(2,3),    3, "R"),
       ("d_R",  F(0),   F(-1,3),   3, "R")]

# LH Weyl convention: RH entries conjugated -> Y -> -Y (and colour 3 -> 3bar,
# which does not change |Y| bookkeeping but DOES change the SU(3) index sign
# convention: for [SU(3)]^2 U(1) the conjugate of a 3 with Y is a 3bar with -Y,
# and T(3bar)=T(3), so the contribution is (-Y) as written.)
states = []
for lbl, t3, q, m, ch in tbl:
    Y = 2*(q - t3)
    if ch == "R":
        states.append((lbl+"^c", -Y, m, "colour" if m == 3 else "singlet"))
    else:
        states.append((lbl, Y, m, "colour" if m == 3 else "singlet"))
for s in states: print(s)

A1 = 3*F(1,3) + 1*F(-1)                      # [SU(2)]^2 U(1): sum over doublets
A2 = sum(m*Y**3 for _, Y, m, _ in states)     # [U(1)]^3
A3 = sum(m*Y   for _, Y, m, _ in states)      # grav^2 U(1)
A_SU3 = sum(Y for _, Y, m, c in states if c == "colour" for _ in range(1))
# careful: [SU(3)]^2 U(1) sums Y over colour-triplet WEYL states counting the
# SU(2) doublet members separately, colour index traced once (T=1/2 each):
A_SU3 = (F(1,3) + F(1,3))  + (-F(4,3)) + (F(2,3))   # u_L,d_L, u_R^c, d_R^c
print("A1", A1, "A2", A2, "A3", A3, "[SU(3)]^2U(1)", A_SU3)
print("doublets:", 3+1, "gauged states:", sum(m for _,_,m,_ in tbl and [(0,0,m,0) for _,_,_,m,_ in tbl]))
print("n gauged =", sum(m for _,_,_,m,_ in tbl))

# counterfactual A1 values, computed by MUTATING the table rather than typing
def A1_of(yq, yl, colour):
    return colour*yq + 1*yl
print("cf no_over_3 :", A1_of(F(1), F(-1), 3))
print("cf sign_flip :", A1_of(F(1,3), F(1), 3))
print("cf colour 2  :", A1_of(F(1,3), F(-1), 2))

# counterfactual A2/A3 for u_R entered unconjugated
def sums(flip_uR):
    a2 = a3 = F(0)
    for lbl, Y, m, _ in states:
        if lbl == "u_R^c" and flip_uR:
            Y = -Y
        a2 += m*Y**3; a3 += m*Y
    return a2, a3
print("cf uR unconj (A2,A3):", sums(True), " baseline:", sums(False))
