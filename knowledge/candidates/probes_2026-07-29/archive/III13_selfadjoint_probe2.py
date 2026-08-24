"""III-13 probe, part 2: general linear operators, and the grade-3 'spectral structure' claim."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/../../corpus")
import sympy as sp
from twt import MV, e

ONE = MV.from_dict({(): 1.0})
B = e(1, 2)

EVEN = [("1", ONE), ("e12", e(1,2)), ("e13", e(1,3)), ("e14", e(1,4)),
        ("e23", e(2,3)), ("e24", e(2,4)), ("e34", e(3,4)), ("I4", e(1,2,3,4))]
ODD  = [("e1", e(1)), ("e2", e(2)), ("e3", e(3)), ("e4", e(4)),
        ("e123", e(1,2,3)), ("e124", e(1,2,4)), ("e134", e(1,3,4)), ("e234", e(2,3,4))]
FULL = EVEN[:1] + ODD[:4] + EVEN[1:7] + ODD[4:] + EVEN[7:]

def comp(X, blade):
    return sp.Rational(round(X.coeff(blade) * 10**6), 10**6)

# ------------------------------------------------------------------ 1. general REAL-LINEAR operators
def general_linear_kernel(basis, label):
    """L: V -> V arbitrary real-linear, dim V = n, so n^2 parameters L[j] = sum_i A_ij b_i.
       Condition: B-component of  psi~ L[psi]  vanishes for all psi."""
    n = len(basis)
    A = sp.symbols(f"a0:{n*n}")
    # q(psi) = sum_{j,k} x_j x_k * Bcomp( b_k~ * L[b_j] )   with L[b_j] = sum_i A[i,j] b_i
    rows = []
    for k in range(n):
        for j in range(k, n):
            row = [0]*(n*n)
            for i in range(n):
                # psi = x_j b_j + ... ; term x_k x_j from b_k~ L[b_j] and b_j~ L[b_k]
                c1 = comp(basis[k][1].reverse() * basis[i][1], (1, 2))
                row[i*n + j] += c1
                if j != k:
                    c2 = comp(basis[j][1].reverse() * basis[i][1], (1, 2))
                    row[i*n + k] += c2
            rows.append(row)
    M = sp.Matrix(rows)
    ns = M.nullspace()
    print(f"\n=== {label} ===")
    print(f"  dim V = {n}, real-linear operator space dim = {n*n}")
    print(f"  constraint rank = {M.rank()};  SOLUTION SPACE DIM = {len(ns)}")
    return len(ns)

general_linear_kernel(EVEN, "E. states V = Cl+(4,0); L = ARBITRARY real-linear map on V")

# ------------------------------------------------------------------ 2. left-mult ops, states = FULL Cl(4,0)
def kernel_leftmult(state_basis, op_basis, target_blade, label):
    n = len(state_basis)
    rows = []
    for i in range(n):
        for j in range(i, n):
            row = []
            for _, M in op_basis:
                v = comp(state_basis[i][1].reverse() * M * state_basis[j][1], target_blade)
                if i != j:
                    v += comp(state_basis[j][1].reverse() * M * state_basis[i][1], target_blade)
                row.append(v)
            rows.append(row)
    A = sp.Matrix(rows)
    ns = A.nullspace()
    names = [nm for nm, _ in op_basis]
    print(f"\n=== {label} ===")
    print(f"  SOLUTION SPACE DIM = {len(ns)}  (op space dim {len(op_basis)}, rank {A.rank()})")
    out = []
    for v in ns:
        v = v / max([abs(x) for x in v if x != 0])
        terms = " + ".join(f"({x}){nm}" for x, nm in zip(v, names) if x != 0)
        out.append(terms)
        print("    basis vector:", terms)
    return out

kernel_leftmult(FULL, FULL, (1,2), "F. states = FULL Cl(4,0); ops = FULL Cl(4,0); B-component condition")

# ------------------------------------------------------------------ 3. grade-3 'spectral structure'
print("\n\n### G. the four grade-3 blades T_a")
T = {"e123": e(1,2,3), "e124": e(1,2,4), "e134": e(1,3,4), "e234": e(2,3,4)}
print("  orthonormality  <T_a T_b~>_0 :")
for a, Ta in T.items():
    row = []
    for b, Tb in T.items():
        row.append(f"{b}:{comp(Ta*Tb.reverse(), ()) }")
    print(f"    {a:5s} -> " + "  ".join(row))
print("\n  reversion behaviour of the T_a (grade 3 -> sign (-1)^(3*2/2) = -1):")
for a, Ta in T.items():
    print(f"    {a}~ = {Ta.reverse()}   self-adjoint (T~=T)? {Ta.reverse()==Ta}   anti (T~=-T)? {Ta.reverse()==(-1.0)*Ta}")
print("\n  squares (would-be eigenvalue structure):")
for a, Ta in T.items():
    print(f"    {a}^2 = {Ta*Ta}")
print("\n  do the T_a commute pairwise? (simultaneous eigenbasis would need it)")
for a, Ta in T.items():
    for b, Tb in T.items():
        if a < b:
            print(f"    [{a},{b}] = {Ta*Tb - Tb*Ta}")
print("\n  is T_a an eigenvector of left-multiplication by T_b?  T_b * T_a =")
for b, Tb in T.items():
    print("    " + f"{b}: " + ", ".join(f"{b}*{a} = {Tb*Ta}" for a, Ta in T.items()))
