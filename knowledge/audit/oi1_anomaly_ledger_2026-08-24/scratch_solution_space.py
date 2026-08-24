"""How constraining is the ledger, with colour UNGAUGED (TWT's own framing, dossier
3(A))? Unknowns: y1 quark doublet, y2 lepton doublet, y3 = Y(u_R^c), y4 = Y(d_R^c),
y5 = Y(e_R^c).  Conditions: A1 = 3y1 + y2 = 0 ; A3 = 6y1+2y2+3y3+3y4+y5 = 0 ;
A2 = 6y1^3+2y2^3+3y3^3+3y4^3+y5^3 = 0."""
import sympy as sp
y1,y2,y3,y4,y5 = sp.symbols('y1 y2 y3 y4 y5', rational=True)
A1 = 3*y1 + y2
A3 = 6*y1 + 2*y2 + 3*y3 + 3*y4 + y5
A2 = 6*y1**3 + 2*y2**3 + 3*y3**3 + 3*y4**3 + y5**3
sol = sp.solve([A1, A3], [y2, y5], dict=True)[0]
print("A1,A3 =>", sol)
res = sp.simplify(A2.subs(sol))
print("A2 reduces to:", sp.factor(res))
SM = {y1: sp.Rational(1,3), y3: sp.Rational(-4,3), y4: sp.Rational(2,3)}
print("SM point residual:", res.subs(SM))
# the SM solution as one point on a surface: scan y3 with y1 fixed to SM, solve for y4
print("\nOther exact solutions with y1 = 1/3 (SM quark doublet kept):")
for y3v in [sp.Rational(-4,3), sp.Rational(-1), sp.Rational(-2), sp.Rational(0), sp.Rational(1)]:
    r = sp.solve(sp.Eq(res.subs({y1: sp.Rational(1,3), y3: y3v}), 0), y4)
    print(f"  y3={y3v}: y4 in {[sp.nsimplify(s) for s in r if s.is_real]}")
# an explicit non-SM RATIONAL solution?
print("\nsearch for rational non-SM solutions, y1=1/3, small denominators:")
found=[]
for a in range(-12,13):
  for b in range(1,13):
    y3v = sp.Rational(a,b)
    rr = sp.solve(sp.Eq(res.subs({y1: sp.Rational(1,3), y3: y3v}),0), y4)
    for s in rr:
        if s.is_rational and s.q<=12:
            pt=(sp.Rational(1,3), y3v, s)
            if pt not in found: found.append(pt)
for p in found[:40]:
    y1v,y3v,y4v = p
    y2v=-3*y1v; y5v=-(6*y1v+2*y2v+3*y3v+3*y4v)
    chk=(6*y1v**3+2*y2v**3+3*y3v**3+3*y4v**3+y5v**3)
    print(f"  Yq={y1v} Yl={y2v} Yuc={y3v} Ydc={y4v} Yec={y5v}  A2={chk}"
          f"   [SU(3)^2U(1)={2*y1v+y3v+y4v}]")
