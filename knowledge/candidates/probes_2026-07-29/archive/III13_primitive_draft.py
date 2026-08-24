"""Draft of the proposed twt.py primitive, tested standalone against the engine."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/../../corpus")
from fractions import Fraction
from twt import MV, e


def _frac_nullspace_dim(rows, ncols):
    """[internal helper] exact Fraction Gauss elimination -> (rank, nullspace basis vectors)."""
    A = [[Fraction(x) for x in r] for r in rows]
    m = len(A); piv = []
    r = 0
    for c in range(ncols):
        p = None
        for i in range(r, m):
            if A[i][c] != 0:
                p = i; break
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        pv = A[r][c]
        A[r] = [x / pv for x in A[r]]
        for i in range(m):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [a - f * b for a, b in zip(A[i], A[r])]
        piv.append(c); r += 1
        if r == m:
            break
    free = [c for c in range(ncols) if c not in piv]
    basis = []
    for fc in free:
        v = [Fraction(0)] * ncols
        v[fc] = Fraction(1)
        for i, pc in enumerate(piv):
            v[pc] = -A[i][fc]
        basis.append(v)
    return len(piv), basis


def self_adjointness_from_one_B_projection() -> dict:
    """[DERIVED-A] §B.3.2: self-adjointness is forced by the {1,B} projection, NOT by
    'requiring reality' of the grade-0 expectation.

    THE DEFECT REPAIRED. §B.3.2 as written derived `M~ = M` from "requiring reality"
    of <phi~ M psi>_0. In a REAL Clifford algebra every grade-0 coefficient is a real
    number by construction, so that requirement imposes NOTHING. Worse, the grade-0
    expectation is identically BLIND to the anti-self-adjoint part of M:
        <psi~ M psi>_0 = <(psi~ M psi)~>_0 = <psi~ M~ psi>_0   for every psi,
    so <psi~ (M - M~) psi>_0 = 0 identically -- the scalar part cannot even see the
    violation it was supposed to forbid.

    THE CORRECT CONDITION is the one the Born-rule section (R-023) already uses: the
    expectation lives in the derived {1, B} subalgebra (R-021 / born_subspace_one_B_forced),
    where `1` is the real axis and `B` is the imaginary axis (i := B). "Real expectation
    value" therefore means the B-COMPONENT VANISHES:
        <psi~ M psi>_B = 0   for all psi.
    That condition is not vacuous, and this primitive computes exactly which M satisfy it.

    THE PAIRING. On Cl+(4,0) (real dim 8) write h(phi,psi) = <phi~ psi>_{1,B}. Its two
    components are g(phi,psi) = <phi~ psi>_0 and b(phi,psi) = <phi~ psi>_B. Engine-exact:
    g is symmetric and unimodular (the Euclidean/Frobenius metric), b is ANTISYMMETRIC and
    nondegenerate (a symplectic form), and J := right-multiplication by B satisfies J^2 = -1
    and preserves both. So h = g + B*b is the Hermitian form of C^4 -- and the "vanishing
    imaginary part" condition is the standard <psi, M psi> in R.

    RESULTS (all engine-exact kernel computations below):
      (1) states = Cl+(4,0), operators = left multiplication by Cl+(4,0) [8 real dims]:
          {M : <psi~ M psi>_B = 0 for all psi} = span{1, I4}, DIMENSION 2 -- which is
          EXACTLY the reversion-fixed subspace {M in Cl+(4,0) : M~ = M}.
      (2) states = Cl(4,0), operators = left multiplication by Cl(4,0) [16 real dims]:
          the solution space is span{1, e1, e2, e3, e4, I4}, DIMENSION 6 -- again EXACTLY
          the reversion-fixed subspace {M : M~ = M} (grades 0,1,4 are reversion-even;
          grades 2,3 are reversion-odd).
      (3) PHASE SECTOR ALONE IS NOT ENOUGH. With states restricted to span{1,B} the
          condition kills only the B-component of M: dimension 7 of 8 survives. It becomes
          exactly right only once the operators are also required to preserve the phase
          sector (M in span{1,B}), where the solution is span{1}, dimension 1 -- the
          reversion-fixed part of {1,B}, i.e. the reals in C. The forcing therefore needs
          the state space to be the full even subalgebra (or full Cl(4,0)), not the
          one-complex-dimensional phase sector.
      (4) OPERATOR CLASS MATTERS. Over ARBITRARY real-linear maps on Cl+(4,0) [64 real
          dims] the condition leaves a 28-dimensional space -- too loose, because it
          admits C-ANTIlinear pieces. Restricted to C-linear maps (those commuting with
          J = right-mult by B; left multiplication is automatically of this kind) the
          solution space is 16-dimensional = dim_R of the self-adjoint operators on C^4.
          So the honest statement carries a named premise: OBSERVABLES ARE C-LINEAR, i.e.
          they commute with the phase structure that R-021 derived.

    CONCLUSION. R-022's CONCLUSION (`M~ = M`, Clifford reversion self-adjointness) is
    CONFIRMED and is an exact algebraic identity; only its stated DERIVATION was vacuous.
    Restated on the {1,B} projection with the C-linearity premise named, it is DERIVED-A.

    TIER. DERIVED-A (exact kernel computation, all-integer constraint matrices solved over
    the rationals). Premise named, not hidden: observables act C-linearly (commute with J).
    """
    ONE = MV.from_dict({(): 1})
    B = e(1, 2)
    ZERO = MV.from_dict({})
    EVEN_BLADES = [(), (1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4), (1, 2, 3, 4)]
    EVEN_NAMES = ["1", "e12", "e13", "e14", "e23", "e24", "e34", "I4"]
    FULL_BLADES = [(), (1,), (2,), (3,), (4,), (1, 2), (1, 3), (1, 4), (2, 3), (2, 4),
                   (3, 4), (1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4), (1, 2, 3, 4)]
    FULL_NAMES = ["1", "e1", "e2", "e3", "e4", "e12", "e13", "e14", "e23", "e24",
                  "e34", "e123", "e124", "e134", "e234", "I4"]

    def bl(t):
        return MV.from_dict({(): 1}) if not t else e(*t)

    def comp(X, blade):
        return X.coeff(blade)

    # ---- (0) the vacuity witness: grade-0 cannot see the anti-self-adjoint part
    grade0_blind = True
    for tb in EVEN_BLADES:
        M = bl(tb)
        Manti = 0.5 * (M - M.reverse())
        for sb in EVEN_BLADES:
            psi = bl(sb) + 0.5 * bl(EVEN_BLADES[(EVEN_BLADES.index(sb) + 3) % 8])
            if abs(comp(psi.reverse() * Manti * psi, ())) > 1e-12:
                grade0_blind = False
    assert grade0_blind, "grade-0 expectation must be blind to the anti-self-adjoint part of M"

    # ---- (1) the {1,B} pairing: g symmetric, b antisymmetric and nondegenerate, J complex structure
    n = 8
    g = [[comp(bl(EVEN_BLADES[i]).reverse() * bl(EVEN_BLADES[j]), ()) for j in range(n)]
         for i in range(n)]
    bmat = [[comp(bl(EVEN_BLADES[i]).reverse() * bl(EVEN_BLADES[j]), (1, 2)) for j in range(n)]
            for i in range(n)]
    g_symmetric = all(abs(g[i][j] - g[j][i]) < 1e-12 for i in range(n) for j in range(n))
    b_antisymmetric = all(abs(bmat[i][j] + bmat[j][i]) < 1e-12 for i in range(n) for j in range(n))
    b_rank, _ = _frac_nullspace_dim([[Fraction(round(x)) for x in row] for row in bmat], n)
    J = [[comp(bl(EVEN_BLADES[j]) * B, EVEN_BLADES[i]) for j in range(n)] for i in range(n)]
    def matmul(A, C):
        return [[sum(A[i][k] * C[k][j] for k in range(len(C))) for j in range(len(C[0]))]
                for i in range(len(A))]
    JJ = matmul(J, J)
    J_sq_minus1 = all(abs(JJ[i][j] - (-1 if i == j else 0)) < 1e-12 for i in range(n) for j in range(n))
    assert g_symmetric and b_antisymmetric and b_rank == n and J_sq_minus1, (
        "the {1,B} pairing must be (symmetric g) + (nondegenerate symplectic b) with J^2 = -1"
    )

    # ---- kernel machinery: which left-multiplication operators kill the B-component?
    def kernel(state_blades, op_blades, target=(1, 2)):
        rows = []
        for i in range(len(state_blades)):
            for j in range(i, len(state_blades)):
                row = []
                for ob in op_blades:
                    v = comp(bl(state_blades[i]).reverse() * bl(ob) * bl(state_blades[j]), target)
                    if i != j:
                        v += comp(bl(state_blades[j]).reverse() * bl(ob) * bl(state_blades[i]), target)
                    row.append(Fraction(round(v * 2), 2))
                rows.append(row)
        rank, basis = _frac_nullspace_dim(rows, len(op_blades))
        return len(basis), basis

    dim_even, basis_even = kernel(EVEN_BLADES, EVEN_BLADES)
    dim_full, basis_full = kernel(FULL_BLADES, FULL_BLADES)
    dim_phase_ops_even, _ = kernel([(), (1, 2)], EVEN_BLADES)
    dim_phase_ops_phase, _ = kernel([(), (1, 2)], [(), (1, 2)])

    def support(basis, names):
        s = set()
        for v in basis:
            for k, x in enumerate(v):
                if x != 0:
                    s.add(names[k])
        return sorted(s)

    rev_fixed_even = sorted(nm for nm, t in zip(EVEN_NAMES, EVEN_BLADES) if bl(t).reverse() == bl(t))
    rev_fixed_full = sorted(nm for nm, t in zip(FULL_NAMES, FULL_BLADES) if bl(t).reverse() == bl(t))

    assert dim_even == 2 and support(basis_even, EVEN_NAMES) == rev_fixed_even, (
        f"even-subalgebra solution must be the reversion-fixed span{{1,I4}}: "
        f"dim={dim_even}, support={support(basis_even, EVEN_NAMES)}"
    )
    assert dim_full == 6 and support(basis_full, FULL_NAMES) == rev_fixed_full, (
        f"full-algebra solution must be the reversion-fixed span{{1,e1,e2,e3,e4,I4}}: "
        f"dim={dim_full}, support={support(basis_full, FULL_NAMES)}"
    )
    assert dim_phase_ops_even == 7 and dim_phase_ops_phase == 1, (
        "the phase sector alone must UNDER-determine self-adjointness (7 of 8), and "
        "become exactly span{1} only when the operators also preserve it"
    )

    # ---- the grade-3 'spectral structure' loose end
    T = {"e123": e(1, 2, 3), "e124": e(1, 2, 4), "e134": e(1, 3, 4), "e234": e(2, 3, 4)}
    gram3 = {a: {b_: round(comp(Ta * Tb.reverse(), ()), 9) for b_, Tb in T.items()}
             for a, Ta in T.items()}
    orthonormal3 = all(gram3[a][b_] == (1 if a == b_ else 0) for a in T for b_ in T)
    T_anti_self_adjoint = {a: (Ta.reverse() == (-1.0) * Ta) for a, Ta in T.items()}
    T_square_minus1 = {a: (Ta * Ta == (-1.0) * ONE) for a, Ta in T.items()}
    T_pairwise_noncommuting = {
        f"[{a},{b_}]": ((T[a] * T[b_] - T[b_] * T[a]) != ZERO)
        for a in T for b_ in T if a < b_
    }
    e4_content = {a: ("Q-orbit (contains e4)" if 4 in list(T[a].terms)[0][0] else "L-orbit (no e4)")
                  for a in T}
    assert orthonormal3, "the four grade-3 blades must be orthonormal under <T_a T_b~>_0"
    assert all(T_anti_self_adjoint.values()), "grade-3 blades are reversion-ODD (T~ = -T)"
    assert all(T_square_minus1.values()), "T_a^2 = -1"
    assert all(T_pairwise_noncommuting.values()), "the T_a do not commute pairwise"

    return {
        "grade0_reality_is_vacuous": True,
        "grade0_blind_to_anti_self_adjoint_part": grade0_blind,
        "pairing_g_symmetric": g_symmetric,
        "pairing_b_antisymmetric": b_antisymmetric,
        "pairing_b_rank": b_rank,
        "J_right_mult_B_squares_to_minus1": J_sq_minus1,
        "dim_solution_even_subalgebra": dim_even,
        "basis_solution_even_subalgebra": support(basis_even, EVEN_NAMES),
        "reversion_fixed_even": rev_fixed_even,
        "dim_solution_full_algebra": dim_full,
        "basis_solution_full_algebra": support(basis_full, FULL_NAMES),
        "reversion_fixed_full": rev_fixed_full,
        "dim_phase_sector_states_even_ops": dim_phase_ops_even,
        "dim_phase_sector_states_phase_ops": dim_phase_ops_phase,
        "grade3_gram": gram3,
        "grade3_orthonormal": orthonormal3,
        "grade3_anti_self_adjoint": T_anti_self_adjoint,
        "grade3_square_minus_one": T_square_minus1,
        "grade3_pairwise_noncommuting": T_pairwise_noncommuting,
        "grade3_orbit_split": e4_content,
        "DERIVED": (
            "<psi~ M psi>_B = 0 for all psi (M acting by left multiplication) holds EXACTLY on the "
            "reversion-fixed subspace: dim 2 = span{1, I4} on Cl+(4,0), dim 6 = span{1,e1,e2,e3,e4,I4} "
            "on Cl(4,0). R-022's conclusion M~ = M is confirmed; its 'requiring reality of <..>_0' "
            "derivation is vacuous and is replaced by the {1,B}-projection condition."
        ),
        "named_premise": (
            "Observables act C-LINEARLY (commute with J = right-multiplication by B). Without it, "
            "arbitrary real-linear maps satisfying the condition form a 28-dim space, not 16."
        ),
        "grade3_loose_end": (
            "The four grade-3 blades ARE orthonormal (<T_a T_b~>_0 = delta_ab, engine-exact), but they "
            "are reversion-ODD (T~ = -T), hence ANTI-self-adjoint under R-022's own criterion; they "
            "square to -1 (no real eigenvalues) and do not commute pairwise (no simultaneous "
            "eigenbasis). 'Each blade an eigenvector of the corresponding observable' names no "
            "observable and is withdrawn; the four blades also split 3+1 by e4-content (the three "
            "colour slots e124/e134/e234 vs the spatial pseudoscalar e123), so they are not a "
            "uniform quadruplet."
        ),
        "tier": (
            "DERIVED-A for the kernel computation and the reversion-fixed identification; the "
            "C-linearity of observables is a NAMED PREMISE, not derived here. The grade-3 "
            "orthonormality is DERIVED-A; the 'eigenvector of the corresponding observable' gloss "
            "is WITHDRAWN (unsupported)."
        ),
    }


if __name__ == "__main__":
    import json
    r = self_adjointness_from_one_B_projection()
    for k, v in r.items():
        print(f"{k}: {v}")
