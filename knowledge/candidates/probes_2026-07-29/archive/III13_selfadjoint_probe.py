"""III-13 probe: which M satisfy <psi~ M psi>_B = 0 for all psi?

Read-only probe. Uses the engine's own MV / e() Clifford primitives.
Exact rational arithmetic via sympy on top of the engine's blade products.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/../../corpus")
import sympy as sp
from twt import MV, e

ONE = MV.from_dict({(): 1.0})
B = e(1, 2)                      # the chosen winding blade / complex unit i := B

EVEN = [("1", ONE), ("e12", e(1,2)), ("e13", e(1,3)), ("e14", e(1,4)),
        ("e23", e(2,3)), ("e24", e(2,4)), ("e34", e(3,4)), ("I4", e(1,2,3,4))]
FULL = [("1", ONE),
        ("e1", e(1)), ("e2", e(2)), ("e3", e(3)), ("e4", e(4)),
        ("e12", e(1,2)), ("e13", e(1,3)), ("e14", e(1,4)),
        ("e23", e(2,3)), ("e24", e(2,4)), ("e34", e(3,4)),
        ("e123", e(1,2,3)), ("e124", e(1,2,4)), ("e134", e(1,3,4)), ("e234", e(2,3,4)),
        ("I4", e(1,2,3,4))]

def comp(X, blade):
    return sp.Rational(round(X.coeff(blade) * 10**6), 10**6)

def gradek_comp(X, k_blades):
    return [comp(X, b) for b in k_blades]

def kernel_of_condition(state_basis, op_basis, target_blade, label, extra_blades=None):
    """dim/basis of {M in span(op_basis) : component of psi~ M psi along target_blade
       vanishes identically for all psi in span(state_basis)}."""
    n = len(state_basis)
    rows = []          # one row per (i<=j) monomial coefficient, columns = ops
    targets = [target_blade] if extra_blades is None else [target_blade] + extra_blades
    for tb in targets:
        for i in range(n):
            for j in range(i, n):
                _, bi = state_basis[i]
                _, bj = state_basis[j]
                row = []
                for _, M in op_basis:
                    v = comp(bi.reverse() * M * bj, tb)
                    if i != j:
                        v += comp(bj.reverse() * M * bi, tb)
                    row.append(v)
                rows.append(row)
    A = sp.Matrix(rows)
    ns = A.nullspace()
    names = [nm for nm, _ in op_basis]
    print(f"\n=== {label} ===")
    print(f"  states: {[nm for nm,_ in state_basis]}")
    print(f"  ops   : {names}")
    print(f"  condition blades: {targets}")
    print(f"  constraint matrix rank = {A.rank()}  (of {A.rows}x{A.cols})")
    print(f"  SOLUTION SPACE DIMENSION = {len(ns)}")
    for v in ns:
        v = v / max([abs(x) for x in v if x != 0])
        terms = " + ".join(f"({x}){nm}" for x, nm in zip(v, names) if x != 0)
        print(f"    basis vector: {terms}")
    return ns

# ---------------------------------------------------------------- reference sets
print("REFERENCE: reversion-fixed elements of Cl+(4,0)  (M~ = M)")
rev_fixed = [nm for nm, X in EVEN if X.reverse() == X]
rev_odd   = [nm for nm, X in EVEN if X.reverse() == (-1.0) * X]
print("  M~ = +M :", rev_fixed)
print("  M~ = -M :", rev_odd)

print("\nREFERENCE: is <X>_0 automatically real? (the review's point)")
print("  MV coefficients are real floats by construction; grade(0) of any X in Cl(4,0)")
print("  is a single real number. Demonstration with a deliberately 'non-self-adjoint' M:")
Mbad = e(1, 2)
psi = ONE + 0.5 * e(1, 3) + 0.25 * e(2, 4)
val = psi.reverse() * Mbad * psi
print("   psi        =", psi)
print("   M          =", Mbad, "   (M~ = ", Mbad.reverse(), " != M )")
print("   psi~ M psi =", val)
print("   <psi~ M psi>_0 =", val.grade(0), "  <- a real number: NO constraint imposed")
print("   <psi~ M psi>_B =", comp(val, (1, 2)), " <- nonzero: THIS is the constraint")

# ---------------------------------------------------------------- case A: phase sector
PHASE = [("1", ONE), ("B=e12", B)]
kernel_of_condition(PHASE, EVEN, (1, 2), "A. phase sector states {1,B}; operators = Cl+(4,0)")
kernel_of_condition(PHASE, PHASE, (1, 2), "A'. phase sector states {1,B}; operators = {1,B}")
kernel_of_condition(PHASE, FULL, (1, 2), "A''. phase sector states {1,B}; operators = full Cl(4,0)")

# ---------------------------------------------------------------- case B: full even subalgebra
kernel_of_condition(EVEN, EVEN, (1, 2), "B. states = Cl+(4,0); operators = Cl+(4,0)")
kernel_of_condition(EVEN, FULL, (1, 2), "B'. states = Cl+(4,0); operators = full Cl(4,0)")

# ---------------------------------------------------------------- case C: L-orbit even (quaternions)
LEVEN = [("1", ONE), ("e12", e(1,2)), ("e13", e(1,3)), ("e23", e(2,3))]
kernel_of_condition(LEVEN, EVEN, (1, 2), "C. states = L-orbit even span{1,e12,e13,e23} = H; ops = Cl+(4,0)")

# ---------------------------------------------------------------- case D: ALL bivector components
print("\n\n### D. stronger variant: require EVERY grade-2 component of psi~ M psi to vanish")
biv = [(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)]
kernel_of_condition(EVEN, EVEN, biv[0], "D. states=Cl+(4,0), ops=Cl+(4,0), all 6 bivector comps",
                    extra_blades=biv[1:])
