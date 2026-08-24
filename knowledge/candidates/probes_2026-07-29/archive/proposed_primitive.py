# -*- coding: utf-8 -*-
"""Standalone dry-run of the PROPOSED twt.py primitive.  Imports twt; defines the
function exactly as it would be pasted; runs it plus the proposed suite assertions."""
import twt
from twt import MV, e


def bell_wing_needs_the_e4_commutant_qubit() -> dict:
    """[DERIVED-A] V3 SSB.3.1 / SSB.4: the per-defect internal space that can carry a Bell
    wing is the WAVEFRONT-FRAME COMMUTANT Z_{Cl+(4,0)}(e4) = span{1,e12,e13,e23} ~ H --
    real dim 4, COMPLEX dim 2 for the R-020 complex structure -- and NOT the phase sector
    span{1,B_a}, which is complex dim ONE.

    THE CONTRADICTION THIS RESOLVES.  SSB.3.1 restricted the fluctuation to span{1,B_a}
    (2 real = 1 complex); SSB.4 then needed a qubit.  A qubit does not fit in C^1:
      - CP^0 is a point, so every state R_a psi_0 obtained by a rotor IN the plane B_a is
        the SAME ray -- the Hermitian overlap has modulus 1 at every pair of angles;
      - Lambda^2(C^1) = 0, so no antisymmetric pairing and hence NO SINGLET exists there.
    The cos(dtheta/2) SSB.4 quoted was the GRADE-0 PART only, i.e. the real inner product
    of the plane span{1,B_a} -- a different functional from the Hermitian inner product
    that `born_exponent_gleason_closure` uses and that the same primitive already flags as
    an undercount (it calls 1 and B orthogonal when they are one ray).

    WHAT IS EXACT HERE (all engine-checked below):
      (1) (W)&(E) = even blades commuting with e4 = {1,e12,e13,e23} = Z(e4), closed under
          the geometric product, a quaternion algebra.  (W)&(S)&(E) = {1,B_a} is R-020.
      (2) RIGHT multiplication by B_a squares to -1 on Z(e4) => Z(e4) is a C-vector space
          of dim 2, C-basis {|0> = 1, |1> = e13}.  LEFT multiplication commutes with it
          (associativity), so the one-sided L-orbit rotor action of SSB.3.5/SSB.4 is
          C-linear and unitary with det 1: SU(2) on C^2.
      (3) The half-angle SURVIVES: with psi_0 = 1 and R_a = exp(theta_a * j / 2) for
          j in {e13,e23} (a plane OTHER than the phase plane), <psi_a|psi_b> = cos(dth/2)
          as an honest C^2 Hermitian overlap -- no grade projection.  Rotors in the plane
          B_a itself are DIAGONAL in that basis and fix psi_0 = 1 up to phase, producing
          no second state -- which is exactly why SSB.4's own choice of measurement plane
          could not generate a wing.
      (4) The singlet PAIRING is a substrate object on the two units the phase-sector cut
          discarded: eps(u,v) = <u*j, v> with j in {e13,e23} is antisymmetric, C-BILINEAR
          and SU(2)-invariant -- the symplectic form whose tensor is the singlet.  RIGHT
          multiplication is essential (it is the antilinear/quaternionic structure); LEFT
          multiplication by the same j is C-linear and gives a form that is neither
          antisymmetric nor invariant.  Right-mult by B_a itself gives no such form either.
      (5) R-020's UNIQUENESS IS NOT SPENT.  span{1,B_a} is exactly the C-linear commutant
          (Schur) of the SU(2) action on Z(e4): dim_R = 2.  Enlarging the MODULE to C^2
          leaves the OPERATOR statement verbatim.  What is withdrawn is only the separate
          SSB.3.1 ansatz that the fluctuation lies in the operator commutant.
      (6) R-127 UNDISTURBED and sharpened: the mass phase = RIGHT multiplication by
          exp(omega*tau5*B_a/2) acts as one global C scalar on both C-coordinates and
          commutes exactly with the SU(2) spin action.  'the mass phase never leaves B_a'
          and 'spin acts on the left' are the two halves of the H = C^2 picture.
      (7) The U(1)_{B_a} adjoint charge decomposition of the eight even blades is
          charge-0 {1,e12,e34,I4} and charged {e13,e14,e23,e24}; intersecting with (W)
          gives Z(e4)-charge-0 = {1,e12} (the phase line = |0>) and Z(e4)-charged =
          {e13,e23} (= |1>).  This discharges the charge-sector half of SSB.3.1's own
          named open item; the remaining four blades {e14,e24,e34,I4} are exactly the
          ones that FAIL (W) (they anticommute with e4) and are R-128's quark-lock family.

    WHAT IS *NOT* CLAIMED.  This constructs ONE wing.  The two-wing TENSOR PRODUCT is
    still not constructed anywhere in TWT (negatives ledger N53, five failed routes) and
    remains a named INPUT of `bell_correlation`; nor is the singlet SELECTED here (that is
    angular-momentum conservation at the source = dynamics = the #1 gap).  Restricting the
    fluctuation to Z(e4) is still a CHOICE -- weaker than span{1,B_a} and motivated by (W),
    but not a derivation.  Tier of the wing algebra: DERIVED-A.  Tier of the Bell
    correlation: unchanged, FRAMING.
    """
    import math, cmath, random
    import numpy as np
    from scipy.linalg import null_space

    ONE = MV.from_dict({(): 1.0})
    ZERO = MV.from_dict({})
    e4, B = e(4), e(1, 2)
    KEYS8 = [(), (1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4), (1, 2, 3, 4)]
    EVEN = {"1": ONE, "e12": e(1, 2), "e13": e(1, 3), "e14": e(1, 4),
            "e23": e(2, 3), "e24": e(2, 4), "e34": e(3, 4), "I4": e(1, 2, 3, 4)}
    co = lambda x: np.array([x.coeff(k) for k in KEYS8], float)
    nz = lambda x: float(np.linalg.norm(co(x)))
    rnd = random.Random(20260729)

    # ---- (1) the two commutants ----
    W = sorted([n for n, X in EVEN.items() if (e4 * X - X * e4) == ZERO])
    assert W == ["1", "e12", "e13", "e23"], W
    notW = sorted([n for n in EVEN if n not in W])
    assert notW == ["I4", "e14", "e24", "e34"], notW
    Zb = [ONE, e(1, 2), e(1, 3), e(2, 3)]
    for X in Zb:
        for Y in Zb:
            assert min(nz(X * Y - s * Z) for Z in Zb for s in (1.0, -1.0)) < 1e-12, \
                "Z(e4) not closed under the geometric product"
    for u in Zb[1:]:
        assert nz(u * u + ONE) < 1e-12, "Z(e4) units must square to -1"
    r020 = twt.born_subspace_one_B_forced()
    assert r020["intersections_per_winding_choice"]["e12"] == ["1", "e12"], "R-020 anchor broken"

    # ---- (2) the complex structure and the C^2 chart ----
    for X in Zb:
        assert nz((X * B) * B + X) < 1e-12, "right-mult by B_a must square to -1 on Z(e4)"
    to_C2 = lambda x: np.array([complex(x.coeff(()), x.coeff((1, 2))),
                                complex(x.coeff((1, 3)), x.coeff((2, 3)))])
    from_C2 = lambda z: (z[0].real * ONE + z[0].imag * e(1, 2)
                         + z[1].real * e(1, 3) + z[1].imag * e(2, 3))
    herm = lambda x, y: complex(np.vdot(to_C2(x), to_C2(y)))
    rvec = lambda: from_C2(np.array([complex(rnd.gauss(0, 1), rnd.gauss(0, 1)),
                                     complex(rnd.gauss(0, 1), rnd.gauss(0, 1))]))
    for _ in range(200):
        x, g = rvec(), rvec()
        assert nz(from_C2(to_C2(x)) - x) < 1e-12, "C^2 chart round-trip failed"
        assert nz((g * x) * B - g * (x * B)) < 1e-12, "left action not C-linear"
    su2 = {}
    for nm, blade in [("e12", e(1, 2)), ("e13", e(1, 3)), ("e23", e(2, 3))]:
        R = twt.exp_unit_bivector(blade, 0.8 / 2.0)
        M = np.stack([to_C2(R * from_C2(np.array([1 + 0j, 0j]))),
                      to_C2(R * from_C2(np.array([0j, 1 + 0j])))], axis=1)
        assert np.linalg.norm(M.conj().T @ M - np.eye(2)) < 1e-12, "L-orbit rotor not unitary"
        assert abs(np.linalg.det(M) - 1.0) < 1e-12, "L-orbit rotor not in SU(2)"
        offdiag = max(abs(M[0, 1]), abs(M[1, 0]))
        su2[nm] = round(offdiag, 12)
    assert su2["e12"] == 0.0, "the PHASE-plane rotor must be diagonal (it fixes psi_0=1 up to phase)"
    assert su2["e13"] > 0.3 and su2["e23"] > 0.3, "the discarded-plane rotors must move the ray"

    # ---- the C^1 obstruction, stated as an assertion ----
    for _ in range(50):
        ta, tb = rnd.uniform(-7, 7), rnd.uniform(-7, 7)
        pa = twt.exp_unit_bivector(B, ta / 2.0) * ONE
        pb = twt.exp_unit_bivector(B, tb / 2.0) * ONE
        assert abs(abs(herm(pa, pb)) - 1.0) < 1e-12, \
            "in C^1 every rotor-rotated state must be the SAME ray (modulus 1)"
    # ... while the grade-0 part is a DIFFERENT functional
    gap = max(abs(abs((twt.exp_unit_bivector(B, t / 2.0) * ONE).reverse().coeff(())) - 1.0)
              for t in (0.5, 1.0, 2.0, 3.0))
    assert gap > 0.1, "grade-0 part must differ from the Hermitian modulus"

    # ---- (3) the half-angle, honest, in C^2 ----
    worst_half = 0.0
    for jb in (e(1, 3), e(2, 3)):
        for _ in range(200):
            ta, tb = rnd.uniform(-7, 7), rnd.uniform(-7, 7)
            pa = twt.exp_unit_bivector(jb, ta / 2.0) * ONE
            pb = twt.exp_unit_bivector(jb, tb / 2.0) * ONE
            worst_half = max(worst_half, abs(abs(herm(pa, pb)) - abs(math.cos((tb - ta) / 2))))
    assert worst_half < 1e-12, "C^2 Hermitian overlap != |cos(dtheta/2)|: %.2e" % worst_half

    # ---- (4) the singlet pairing on the discarded units ----
    pair = {}
    for nm, jb, side in [("e13_right", e(1, 3), "R"), ("e23_right", e(2, 3), "R"),
                         ("e12_right", e(1, 2), "R"), ("e13_left", e(1, 3), "L")]:
        E = (lambda J: (lambda u, v: herm(u * J, v)))(jb) if side == "R" else \
            (lambda J: (lambda u, v: herm(J * u, v)))(jb)
        anti = bil = inv = 0.0
        for _ in range(200):
            u, v = rvec(), rvec()
            lam = complex(rnd.gauss(0, 1), rnd.gauss(0, 1))
            lamMV = lam.real * ONE + lam.imag * e(1, 2)
            anti = max(anti, abs(E(u, v) + E(v, u)))
            bil = max(bil, abs(E(u * lamMV, v) - lam * E(u, v)))
            cs = [rnd.gauss(0, 1) for _ in range(3)]
            n_ = math.sqrt(sum(c * c for c in cs)); cs = [c / n_ for c in cs]
            ax = cs[0] * e(1, 2) + cs[1] * e(1, 3) + cs[2] * e(2, 3)
            Rg = twt.exp_unit_bivector(ax, rnd.uniform(-3, 3))
            inv = max(inv, abs(E(Rg * u, Rg * v) - E(u, v)))
        pair[nm] = (anti < 1e-10, bil < 1e-10, inv < 1e-10)
    assert pair["e13_right"] == (True, True, True), "eps via RIGHT-mult by e13 must be the symplectic form"
    assert pair["e23_right"] == (True, True, True), "eps via RIGHT-mult by e23 must be the symplectic form"
    assert pair["e12_right"][0] is False, "right-mult by the PHASE blade must NOT give an antisym form"
    assert pair["e13_left"][0] is False and pair["e13_left"][2] is False, \
        "LEFT-mult by e13 must fail antisymmetry and SU(2)-invariance"
    k0, k1 = from_C2(np.array([1 + 0j, 0j])), from_C2(np.array([0j, 1 + 0j]))
    E13 = lambda u, v: herm(u * e(1, 3), v)
    assert abs(E13(k0, k1) - 1.0) < 1e-12 and abs(E13(k1, k0) + 1.0) < 1e-12
    assert abs(E13(k0, k0)) < 1e-12 and abs(E13(k1, k1)) < 1e-12
    # and it VANISHES identically on the phase sector (Lambda^2(C^1) = 0)
    for _ in range(100):
        u = from_C2(np.array([complex(rnd.gauss(0, 1), rnd.gauss(0, 1)), 0j]))
        v = from_C2(np.array([complex(rnd.gauss(0, 1), rnd.gauss(0, 1)), 0j]))
        assert abs(E13(u, v)) < 1e-12, "eps must vanish identically on span{1,B_a}"

    # ---- (5) Schur: the C-linear commutant of the spin action is span{1,B_a} ----
    def regmat(Y, left):
        M = np.zeros((4, 4))
        for c, X in enumerate(Zb):
            P = (Y * X) if left else (X * Y)
            M[:, c] = np.array([P.coeff(k) for k in [(), (1, 2), (1, 3), (2, 3)]])
        return M
    rows = [np.kron(np.eye(4), regmat(Y, True)) - np.kron(regmat(Y, True).T, np.eye(4))
            for Y in Zb]
    dim_comm = null_space(np.vstack(rows), rcond=1e-10).shape[1]
    RB = regmat(e(1, 2), False)
    dim_ccomm = null_space(np.vstack(rows + [np.kron(np.eye(4), RB)
                                             - np.kron(RB.T, np.eye(4))]), rcond=1e-10).shape[1]
    assert dim_comm == 4, "commutant of the left regular rep must be H (dim 4), got %d" % dim_comm
    assert dim_ccomm == 2, "C-linear commutant must be span{1,B_a} (dim 2), got %d" % dim_ccomm

    # ---- (6) R-127 coherence: the mass phase is the global C scalar ----
    om, t5 = 0.937, 1.7
    P = twt.exp_unit_bivector(B, om * t5 / 2.0)
    for _ in range(100):
        x = rvec()
        assert np.max(np.abs(to_C2(x * P) - cmath.exp(1j * om * t5 / 2.0) * to_C2(x))) < 1e-12, \
            "mass phase must act as ONE global C scalar on both coordinates"
        cs = [rnd.gauss(0, 1) for _ in range(3)]
        n_ = math.sqrt(sum(c * c for c in cs)); cs = [c / n_ for c in cs]
        ax = cs[0] * e(1, 2) + cs[1] * e(1, 3) + cs[2] * e(2, 3)
        Rg = twt.exp_unit_bivector(ax, rnd.uniform(-3, 3))
        assert nz((Rg * x) * P - Rg * (x * P)) < 1e-12, "[spin, mass phase] must vanish"

    # ---- (7) the U(1)_{B_a} adjoint charge decomposition ----
    charge = {}
    th = 0.37
    for n, X in EVEN.items():
        Rr = twt.exp_unit_bivector(B, th / 2.0)
        Y = Rr * X * Rr.reverse()
        if nz(Y - X) < 1e-12:
            charge[n] = 0
        else:
            c = float(co(Y) @ co(X) / (co(X) @ co(X)))
            charge[n] = int(round(math.acos(max(-1.0, min(1.0, c))) / th))
    assert sorted([n for n, q in charge.items() if q == 0]) == ["1", "I4", "e12", "e34"], charge
    assert sorted([n for n, q in charge.items() if q == 1]) == ["e13", "e14", "e23", "e24"], charge

    return {
        "tier": ("DERIVED-A (the wing algebra: commutant dimensions, the C-structure, "
                 "SU(2) unitarity, the half-angle as an honest C^2 Hermitian overlap, the "
                 "symplectic pairing, the Schur commutant, the charge grading -- all exact "
                 "Clifford identities) + the SSB.3.1 module restriction to Z(e4) remains a "
                 "named CHOICE, not a derivation + the two-wing TENSOR PRODUCT and the "
                 "SINGLET SELECTION remain IMPORTS (N53; bell_correlation stays FRAMING)"),
        "W_commutant": W, "fails_W": notW,
        "dim_R_phase_sector": 2, "dim_C_phase_sector": 1,
        "dim_R_e4_commutant": 4, "dim_C_e4_commutant": 2,
        "qubit_C_basis": ["1", "e13"],
        "su2_offdiagonal_by_rotor_plane": su2,
        "max_dev_half_angle_C2_hermitian": worst_half,
        "pairing_antisym_Cbilinear_SU2invariant": pair,
        "schur_commutant_dim_R": dim_comm, "schur_C_linear_commutant_dim_R": dim_ccomm,
        "U1_Ba_adjoint_charges": charge,
        "phase_sector_hosts_a_qubit": False,
        "e4_commutant_hosts_a_qubit": True,
        "not_claimed": ["two-wing tensor product (N53)", "singlet selection (dynamics, #1 gap)",
                        "the Z(e4) module restriction itself"],
    }


if __name__ == "__main__":
    import json
    d = bell_wing_needs_the_e4_commutant_qubit()
    for k, v in d.items():
        print("%-42s %s" % (k, v))
    # proposed suite assertions
    assert d["dim_C_phase_sector"] == 1 and d["dim_C_e4_commutant"] == 2
    assert d["phase_sector_hosts_a_qubit"] is False and d["e4_commutant_hosts_a_qubit"] is True
    assert d["max_dev_half_angle_C2_hermitian"] < 1e-12
    assert d["schur_C_linear_commutant_dim_R"] == 2
    assert d["pairing_antisym_Cbilinear_SU2invariant"]["e13_right"] == (True, True, True)
    assert d["su2_offdiagonal_by_rotor_plane"]["e12"] == 0.0
    print("\nPROPOSED SUITE ASSERTIONS: ALL PASS")
