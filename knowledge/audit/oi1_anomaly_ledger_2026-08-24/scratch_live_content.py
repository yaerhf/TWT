"""How much of the ledger is LIVE, given the primitive's own doublet_hypercharge assert?"""
import sympy as sp, twt_core as tc

orig = tc.generation_spectrum
print("doublet_hypercharge (anchor-free, blade-derived constants):", tc.doublet_hypercharge())

# (a) Can A1 or the parity ever be nonzero?  Perturb the LH doublet charges.
def perturbed(qnu=0.1):
    out=[]
    for lbl,t3,q,m in orig():
        if lbl=="nu_L": q=qnu
        out.append((lbl,t3,q,m))
    return out
tc.generation_spectrum = perturbed
try:
    tc.continuous_anomaly_ledger(); print("Q_nu perturbed -> LEDGER RETURNED (bad)")
except AssertionError as e:
    print("Q_nu = 0.1 -> the dh cross-check assert fires BEFORE any sum is formed:", e)
tc.generation_spectrum = orig

# (b) symbolic: with the four doublet asserts satisfied, y_q = 1/3 and y_l = -1 are
#     FORCED constants, so A1 and the doublet parity are identities of the code.
yq, yl = sp.Rational(1,3), sp.Integer(-1)
print("A1 given the assert  = 3*(1/3) + (-1) =", 3*yq + yl, "  <- cannot be nonzero")
print("doublet parity given the table shape = 3 + 1 =", 4, " <- cannot be odd without the colour mult changing")

# (c) the LIVE content: two equations on the three RIGHT-handed charges
Qu,Qd,Qe = sp.symbols('Qu Qd Qe', real=True)
yuc,ydc,yec = -2*Qu, -2*Qd, -2*Qe
A3 = 6*yq + 2*yl + 3*yuc + 3*ydc + yec
A2 = 6*yq**3 + 2*yl**3 + 3*yuc**3 + 3*ydc**3 + yec**3
print("\nA3 =", sp.simplify(A3), " ; A2 =", sp.expand(A2))
SM = {Qu: sp.Rational(2,3), Qd: sp.Rational(-1,3), Qe: sp.Integer(-1)}
print("at the SM point: A3 =", A3.subs(SM), " A2 =", A2.subs(SM))
sol = sp.solve([A3], [Qe])[0]
red = sp.simplify(A2.subs(Qe, sol))
print("eliminating Qe:", sp.factor(red), "= 0  -> ONE equation in TWO unknowns => a CURVE")
# rational points on that curve
pts=[]
for a in range(-9,10):
  for b in (1,2,3,6,9):
    Quv = sp.Rational(a,b)
    for r in sp.solve(sp.Eq(red.subs(Qu,Quv),0), Qd):
        if r.is_rational and r.q<=9:
            pts.append((Quv, r, sol.subs({Qu:Quv, Qd:r})))
seen=set(); print("\nRATIONAL solutions (Q_uR, Q_dR, Q_eR) of the FULL ledger, denom<=9:")
for p in pts:
    if p in seen: continue
    seen.add(p); print("   ", p, "   <-- SM" if p==(sp.Rational(2,3),sp.Rational(-1,3),-1) else "")
