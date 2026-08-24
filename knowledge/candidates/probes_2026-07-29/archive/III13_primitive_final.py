"""FINAL draft of the proposed twt.py primitive (self-contained; nested helper)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/../../corpus")
from twt import MV, e


def self_adjointness_from_one_B_projection() -> dict:
    """[DERIVED-A] §B.3.2: self-adjointness is forced by the {1,B} projection, NOT by
    "requiring reality" of the grade-0 expectation.

    THE DEFECT REPAIRED. §B.3.2 as written derived `M~ = M` from "requiring reality" of
    <phi~ M psi>_0. In a REAL Clifford algebra every grade-0 coefficient is a real number
    by construction, so that requirement imposes NOTHING. Worse, the grade-0 expectation is
    identically BLIND to the anti-self-adjoint part of M:
        <psi~ M psi>_0 = <(psi~ M psi)~>_0 = <psi~ M~ psi>_0   for every psi,
    hence <psi~ (M - M~) psi>_0 = 0 identically -- the scalar part cannot even see the
    violation it was supposed to forbid.

    THE CORRECT CONDITION is the one the Born-rule section (R-023) already uses: the
    expectation lives in the derived {1, B} subalgebra (R-021 / born_subspace_one_B_forced),
    where `1` is the real axis and `B` the imaginary axis (i := B). "Real expectation value"
    therefore means THE B-COMPONENT VANISHES:  <psi~ M psi>_B = 0 for all psi.
    That condition is not vacuous; this primitive computes exactly which M satisfy it.

    THE PAIRING. On Cl+(4,0) (real dim 8) write h(phi,psi) = <phi~ psi>_{1,B}, with
    components g(phi,psi) = <phi~ psi>_0 and b(phi,psi) = <phi~ psi>_B. Engine-exact: g is
    symmetric and unimodular, b is ANTISYMMETRIC and nondegenerate (a symplectic form), and
    J := right-multiplication by B satisfies J^2 = -1. So h = g + B*b is the Hermitian form
    of C^4 and "vanishing B-part" is the standard "<psi, M psi> is real".

    RESULTS (exact kernel computations over the rationals):
      (1) states = Cl+(4,0), operators = left multiplication by Cl+(4,0) [8 real dims]:
          {M : <psi~ M psi>_B = 0 for all psi} = span{1, I4}, DIMENSION 2 -- EXACTLY the
          reversion-fixed subspace {M in Cl+(4,0) : M~ = M}.
      (2) states = Cl(4,0), operators = left multiplication by Cl(4,0) [16 real dims]:
          the solution space is span{1, e1, e2, e3, e4, I4}, DIMENSION 6 -- again EXACTLY
          the reversion-fixed subspace (grades 0,1,4 reversion-even; grades 2,3 odd).
      (3) THE PHASE SECTOR ALONE IS NOT ENOUGH. With states restricted to span{1,B} the
          condition kills only the B-component of M: 7 of 8 dimensions survive. It becomes
          exactly right only once the operators are also required to preserve the phase
          sector (M in span{1,B}), where the solution is span{1}, DIMENSION 1 -- the
          reversion-fixed part of {1,B}, i.e. the reals inside C. The forcing therefore
          needs the state space to be the full even subalgebra (or full Cl(4,0)).
      (4) OPERATOR CLASS IS A NAMED PREMISE. Over ARBITRARY real-linear maps on Cl+(4,0)
          [64 real dims] the condition leaves 28 dimensions -- too loose, because it admits
          C-ANTIlinear pieces. Restricted to C-linear maps (commuting with J; left
          multiplication is automatically of this kind) the solution space is 16-dimensional
          = dim_R of the self-adjoint operators on C^4. (The 28/16 counts are recorded in
          the returned dict as documented companion computations, not re-derived here.)

    CONCLUSION. R-022's CONCLUSION (`M~ = M`, Clifford reversion self-adjointness) is
    CONFIRMED as an exact algebraic identity; only its stated DERIVATION was vacuous.
    Restated on the {1,B} projection with the C-linearity premise named, it is DERIVED-A.

    GRADE-3 LOOSE END (§B.3.2 "spectral structure"). The four grade-3 blades ARE orthonormal
    (<T_a T_b~>_0 = delta_ab, engine-exact), but they are reversion-ODD (T~ = -T), hence
    ANTI-self-adjoint under R-022's own criterion; they square to -1 (no real eigenvalues)
    and do not commute pairwise (no simultaneous eigenbasis). The gloss "each blade an
    eigenvector of the corresponding observable" names no observable and is WITHDRAWN. The
    four blades also split 3+1 by e4-content (the three colour slots e124/e134/e234 vs the
    spatial pseudoscalar e123), so they are not a uniform quadruplet.

    TIER. DERIVED-A for the kernel computation and the reversion-fixed identification and
    for the grade-3 orthonormality/anti-self-adjointness; the C-linearity of observables is
    a NAMED PREMISE, not derived here.
    """
    from fractions import Fraction

    def _nullspace(rows, ncols):
        """[nested helper] exact Fraction Gauss-Jordan -> (rank, nullspace basis)."""
        A = [[Fraction(x) for x in r] for r in rows]
        m = len(A)
        piv = []
        r = 0
        for c in range(ncols):
            p = None
            for i in range(r, m):
                if A[i][c] != 0:
                    p = i
                    break
            if p is None:
                continue
            A[r], A[p] = A[p], A[r]
            pv = A[r][c]
            A[r] = [x / pv for x in A[r]]
            for i in range(m):
                if i != r and A[i][c] != 0:
                    f = A[i][c]
                    A[i] = [a - f * b for a, b in zip(A[i], A[r])]
            piv.append(c)
            r += 1
            if r == m:
                break
        basis = []
        for fc in [c for c in range(ncols) if c not in piv]:
            v = [Fraction(0)] * ncols
            v[fc] = Fraction(1)
            for i, pc in enumerate(piv):
                v[pc] = -A[i][fc]
            basis.append(v)
        return len(piv), basis

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
        return ONE if not t else e(*t)

    # ---- (0) vacuity witness: the grade-0 expectation is blind to the anti-self-adjoint part
    grade0_blind = True
    for k, tb in enumerate(EVEN_BLADES):
        M_anti = 0.5 * (bl(tb) - bl(tb).reverse())
        for j, sb in enumerate(EVEN_BLADES):
            psi = bl(sb) + 0.5 * bl(EVEN_BLADES[(j + 3) % 8]) + 0.25 * bl(EVEN_BLADES[(j + 5) % 8])
            if abs((psi.reverse() * M_anti * psi).coeff(())) > 1e-12:
                grade0_blind = False
    assert grade0_blind, "grade-0 expectation must be blind to the anti-self-adjoint part of M"

    # ---- (1) the {1,B} pairing: g symmetric, b symplectic, J^2 = -1
    n = 8
    g = [[(bl(EVEN_BLADES[i]).reverse() * bl(EVEN_BLADES[j])).coeff(()) for j in range(n)]
         for i in range(n)]
    bmat = [[(bl(EVEN_BLADES[i]).reverse() * bl(EVEN_BLADES[j])).coeff((1, 2)) for j in range(n)]
            for i in range(n)]
    g_symmetric = all(abs(g[i][j] - g[j][i]) < 1e-12 for i in range(n) for j in range(n))
    b_antisymmetric = all(abs(bmat[i][j] + bmat[j][i]) < 1e-12 for i in range(n) for j in range(n))
    b_rank, _ = _nullspace([[round(x) for x in row] for row in bmat], n)
    J = [[(bl(EVEN_BLADES[j]) * B).coeff(EVEN_BLADES[i]) for j in range(n)] for i in range(n)]
    JJ = [[sum(J[i][k] * J[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    J_sq_minus1 = all(abs(JJ[i][j] - (-1 if i == j else 0)) < 1e-12
                      for i in range(n) for j in range(n))
    assert g_symmetric and b_antisymmetric and b_rank == n and J_sq_minus1, (
        "the {1,B} pairing must be (symmetric g) + (nondegenerate symplectic b) with J^2 = -1")

    # ---- kernel of  psi -> <psi~ M psi>_B  over left-multiplication operators
    def kernel(state_blades, op_blades, target=(1, 2)):
        rows = []
        for i in range(len(state_blades)):
            for j in range(i, len(state_blades)):
                row = []
                for ob in op_blades:
                    v = (bl(state_blades[i]).reverse() * bl(ob) * bl(state_blades[j])).coeff(target)
                    if i != j:
                        v += (bl(state_blades[j]).reverse() * bl(ob)
                              * bl(state_blades[i])).coeff(target)
                    row.append(round(v))
                rows.append(row)
        _, basis = _nullspace(rows, len(op_blades))
        return len(basis), basis

    def support(basis, names):
        s = set()
        for v in basis:
            for k, x in enumerate(v):
                if x != 0:
                    s.add(names[k])
        return sorted(s)

    dim_even, basis_even = kernel(EVEN_BLADES, EVEN_BLADES)
    dim_full, basis_full = kernel(FULL_BLADES, FULL_BLADES)
    dim_phase_ops_even, _ = kernel([(), (1, 2)], EVEN_BLADES)
    dim_phase_ops_phase, _ = kernel([(), (1, 2)], [(), (1, 2)])

    rev_fixed_even = sorted(nm for nm, t in zip(EVEN_NAMES, EVEN_BLADES) if bl(t).reverse() == bl(t))
    rev_fixed_full = sorted(nm for nm, t in zip(FULL_NAMES, FULL_BLADES) if bl(t).reverse() == bl(t))

    assert dim_even == 2 and support(basis_even, EVEN_NAMES) == rev_fixed_even, (
        f"even-subalgebra solution must be the reversion-fixed span{{1,I4}}: dim={dim_even}, "
        f"support={support(basis_even, EVEN_NAMES)}")
    assert dim_full == 6 and support(basis_full, FULL_NAMES) == rev_fixed_full, (
        f"full-algebra solution must be reversion-fixed span{{1,e1,e2,e3,e4,I4}}: dim={dim_full}, "
        f"support={support(basis_full, FULL_NAMES)}")
    assert dim_phase_ops_even == 7 and dim_phase_ops_phase == 1, (
        "the phase sector alone must UNDER-determine self-adjointness (7 of 8), becoming exactly "
        "span{1} only when the operators are also required to preserve it")

    # ---- the grade-3 "spectral structure" loose end
    T = {"e123": e(1, 2, 3), "e124": e(1, 2, 4), "e134": e(1, 3, 4), "e234": e(2, 3, 4)}
    gram3 = {a: {b2: round((Ta * T[b2].reverse()).coeff(()), 9) for b2 in T} for a, Ta in T.items()}
    orthonormal3 = all(gram3[a][b2] == (1 if a == b2 else 0) for a in T for b2 in T)
    T_anti = {a: (Ta.reverse() == (-1.0) * Ta) for a, Ta in T.items()}
    T_sq = {a: (Ta * Ta == (-1.0) * ONE) for a, Ta in T.items()}
    T_noncomm = {f"[{a},{b2}]": ((T[a] * T[b2] - T[b2] * T[a]) != ZERO)
                 for a in T for b2 in T if a < b2}
    orbit_split = {a: ("Q-orbit (contains e4)" if 4 in list(T[a].terms)[0][0]
                       else "L-orbit (no e4)") for a in T}
    assert orthonormal3, "the four grade-3 blades must be orthonormal under <T_a T_b~>_0"
    assert all(T_anti.values()), "grade-3 blades are reversion-ODD (T~ = -T): ANTI-self-adjoint"
    assert all(T_sq.values()), "T_a^2 = -1 (no real eigenvalues)"
    assert all(T_noncomm.values()), "the T_a do not commute pairwise (no simultaneous eigenbasis)"

    return {
        "grade0_reality_requirement_is_vacuous": True,
        "grade0_blind_to_anti_self_adjoint_part": grade0_blind,
        "pairing_g_symmetric": g_symmetric,
        "pairing_b_antisymmetric_symplectic": b_antisymmetric,
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
        "companion_counts_general_linear": {
            "all_real_linear_on_Cl_plus": 28, "C_linear_on_Cl_plus": 16,
            "note": "documented companion computation (probes_2026-07-29); the engine assertion "
                    "above covers the left-multiplication statement, which is the one the paper uses",
        },
        "grade3_gram": gram3,
        "grade3_orthonormal": orthonormal3,
        "grade3_anti_self_adjoint": T_anti,
        "grade3_square_minus_one": T_sq,
        "grade3_pairwise_noncommuting": T_noncomm,
        "grade3_orbit_split_3plus1": orbit_split,
        "DERIVED": (
            "<psi~ M psi>_B = 0 for all psi (M acting by left multiplication) holds EXACTLY on the "
            "reversion-fixed subspace: dim 2 = span{1, I4} on Cl+(4,0); dim 6 = "
            "span{1,e1,e2,e3,e4,I4} on Cl(4,0). R-022's conclusion M~ = M is CONFIRMED; its "
            "'requiring reality of <..>_0' derivation is VACUOUS and is replaced by the "
            "{1,B}-projection condition."
        ),
        "named_premise": (
            "Observables act C-LINEARLY (commute with J = right-multiplication by B). Without it, "
            "arbitrary real-linear maps satisfying the condition span 28 dimensions, not 16."
        ),
        "grade3_loose_end": (
            "The four grade-3 blades are orthonormal but reversion-ODD, hence ANTI-self-adjoint "
            "under R-022's own criterion; T_a^2 = -1 and the T_a do not commute pairwise. 'Each "
            "blade an eigenvector of the corresponding observable' names no observable and is "
            "WITHDRAWN; the four also split 3+1 by e4-content (colour slots e124/e134/e234 vs the "
            "spatial pseudoscalar e123), so they are not a uniform quadruplet."
        ),
        "tier": (
            "DERIVED-A for the kernel computation, the reversion-fixed identification, and the "
            "grade-3 orthonormality/anti-self-adjointness. The C-linearity of observables is a "
            "NAMED PREMISE, not derived here. The 'eigenvector of the corresponding observable' "
            "gloss is WITHDRAWN (unsupported)."
        ),
    }


if __name__ == "__main__":
    r = self_adjointness_from_one_B_projection()
    for k, v in r.items():
        print(f"{k}: {v}")
