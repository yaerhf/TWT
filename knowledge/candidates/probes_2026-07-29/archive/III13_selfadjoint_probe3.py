"""III-13 probe, part 3: the {1,B} pairing as a symplectic form, and the C-linear operator count."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/../../corpus")
import sympy as sp
from twt import MV, e

ONE = MV.from_dict({(): 1.0})
B = e(1, 2)
EVEN = [("1", ONE), ("e12", e(1,2)), ("e13", e(1,3)), ("e14", e(1,4)),
        ("e23", e(2,3)), ("e24", e(2,4)), ("e34", e(3,4)), ("I4", e(1,2,3,4))]
n = len(EVEN)
def comp(X, blade): return sp.Rational(round(X.coeff(blade)*10**6), 10**6)

# --- the two components of the {1,B} pairing
g = sp.Matrix(n, n, lambda i, j: comp(EVEN[i][1].reverse()*EVEN[j][1], ()))       # <phi~ psi>_0
b = sp.Matrix(n, n, lambda i, j: comp(EVEN[i][1].reverse()*EVEN[j][1], (1, 2)))   # <phi~ psi>_B
print("g = <phi~ psi>_0 :  symmetric?", g.T == g, "   det =", g.det())
print("b = <phi~ psi>_B :  antisymmetric?", b.T == -b, "  rank =", b.rank(), " det =", b.det())

# --- J = right multiplication by B is the complex structure
J = sp.zeros(n, n)
for j, (_, bj) in enumerate(EVEN):
    prod = bj * B
    for i, (_, bi) in enumerate(EVEN):
        J[i, j] = comp(prod, bi[1].terms[0][0] if False else tuple(sorted(_blade := [])) ) if False else 0
# (build J properly)
BLADES = [(), (1,2), (1,3), (1,4), (2,3), (2,4), (3,4), (1,2,3,4)]
J = sp.Matrix(n, n, lambda i, j: comp(EVEN[j][1]*B, BLADES[i]))
print("\nJ = right-mult by B :  J^2 = -1 ?", J*J == -sp.eye(n))
print("  g(J.,J.) = g ?", (J.T*g*J) == g, "    b(J.,J.) = b ?", (J.T*b*J) == b)

# --- left multiplication commutes with J (so left-mult ops are C-linear)
def Lmat(M):
    return sp.Matrix(n, n, lambda i, j: comp(M*EVEN[j][1], BLADES[i]))
print("  every left-mult operator commutes with J ?",
      all(Lmat(X)*J == J*Lmat(X) for _, X in EVEN))

# --- C-linear operators: L with L J = J L  (32 real dims); impose b(psi, L psi)=0
A = sp.symbols(f"x0:{n*n}")
Lg = sp.Matrix(n, n, lambda i, j: A[i*n+j])
eqs = list((Lg*J - J*Lg))                       # C-linearity
S = (b*Lg)                                      # quadratic form matrix: q(psi)=psi^T b L psi
eqs += [sp.expand(S[i, j] + S[j, i]) for i in range(n) for j in range(i, n)]
sol = sp.linsolve(eqs, A)
free = len(set().union(*[expr.free_symbols for expr in list(sol)[0]]))
print("\nC-LINEAR operators on Cl+(4,0) (32 real dims) with <psi~ L psi>_B = 0 for all psi:")
print("   SOLUTION SPACE DIM =", free, "   (expected 16 = dim_R of self-adjoint ops on C^4)")

# same without the C-linearity constraint
eqs2 = [sp.expand(S[i, j] + S[j, i]) for i in range(n) for j in range(i, n)]
sol2 = sp.linsolve(eqs2, A)
free2 = len(set().union(*[expr.free_symbols for expr in list(sol2)[0]]))
print("   (all real-linear, no C-linearity:  DIM =", free2, ")")

# --- and the intersection with left-multiplication operators, recomputed as a cross-check
Msym = sp.symbols("m0:8")
Mgen = sp.zeros(n, n)
for k, (_, X) in enumerate(EVEN):
    Mgen += Msym[k]*Lmat(X)
S2 = b*Mgen
eqs3 = [sp.expand(S2[i, j] + S2[j, i]) for i in range(n) for j in range(i, n)]
sol3 = list(sp.linsolve(eqs3, Msym))[0]
print("\nleft-mult operators M in Cl+(4,0) with <psi~ M psi>_B = 0 for all psi:")
print("   general solution (m0..m7 <-> 1,e12,e13,e14,e23,e24,e34,I4):", sol3)
