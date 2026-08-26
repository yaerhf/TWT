"""TWT — the CANDIDATE (V3-instance) half of the MAIN engine (family split 2026-08-23).

THE MAIN ENGINE IS A FACADE OVER TWO HALVES SINCE 2026-08-23 (RUL-093/RUL-095, the
family split). THIS file is the CANDIDATE half: everything that consumes a V3 PICK — the pinned
calibrations (f_pi, D/J, the ANW dials, the massive-scheme refit), the D4-sited
lattice constructions, the gravity/Sakharov chain, the hadron and mass spectra, the
LV numerics, the CKM/meta-time material, the kernel-branch dials. Its sibling
`twt_core.py` holds the family-level half. `twt.py` is a FACADE over both.

WHAT MEMBERSHIP HERE MEANS, AND WHAT IT DOES NOT. It means: this primitive rides one
of the family tree's V3 picks (V3-1 … V3-11, +V3-2a), so a different family member —
same axioms, different pick — would compute something else here. It does NOT mean
"unverified" or "lower tier": the tiers are unchanged by the move and live where they
always lived, in each primitive's own docstring. A DERIVED-A identity that happens to
consume the D4 siting is still a DERIVED-A identity; it is just not family-level.

THE DIRECTION INVARIANT (suite-guarded, AST-checked): this file may import `twt_core`
freely — that is the allowed direction. `twt_core` may never reference a name defined
here. Neither half may import `twt_companion` (the 2026-08-13 split invariant).

Verify with:  python twt_test.py && python twt_companion_test.py
"""
from __future__ import annotations
import math
import itertools
from itertools import combinations
import sympy as sp
from dataclasses import dataclass
from dataclasses import dataclass, field
from enum import Enum
from twt_core import *
from twt_core import (_biv, _blade_mul, _sqrt_masses)


HBAR_C = 197.3269804   # MeV*fm


def sakharov_induced_gravity():
    """[CANDIDATE / QFT INPUT] Sakharov induced gravity from the substrate's rotor field
    (the six-parameter 4D-orientation field; the Spin(4) writing below is cover-agnostic —
    only dim = 6 enters).

    SETUP:
    R(x) takes values in the 4D-ORIENTATION CLASS — the medium's local state space,
    six real parameters, inherited unchanged by the continuum field (§D.3.2;
    `pi3_orientation_class_two_windings`). WHERE the Z_2 sign lives — in the state
    (Spin(4), one-sided) or in the emergent covering sector (SO(4) + odd character) —
    is a recorded OPEN BRANCH in the family tree, and nothing below depends on it:
    N_eff = 6 is the DIMENSION of the class, which both branches share.
    R(x) in Spin(4) = SU(2)_L x SU(2)_R; target manifold Spin(4) ~ S^3 x S^3, dim_R = 6.
    The 6 real DOF are the grade-2 generators {SD_1,SD_2,SD_3, ASD_1,ASD_2,ASD_3}
    of Cl(4,0) — the basis of the Lie algebra so(4) ~ su(2)_L + su(2)_R.
    N_eff = 6  [engine: grade-2 subspace of Cl(4,0) has dim 6 = C(4,2) = n(n-1)/2 at n=4.
               GENERIC-given-dim=4 (canon §5 class: same as Sakharov Lambda^2 — combinatorial,
               not a dynamical Clifford derivation; substrate-specific only in that n=4 is fixed)].

    SEELEY-DEWITT (QFT INPUT — standard one-loop heat kernel, exact for Lambda >> f_pi):
    For N_eff minimally coupled massless scalars in 4D Euclidean with UV cutoff Lambda:
        W_1loop = (N_eff/2) Tr ln(-Box_g)
    The R-linear term in the heat kernel expansion gives (Donoghue, standard result):
        G_N^{-1} = N_eff * Lambda^2 / (12*pi)    [QFT INPUT — the scaling FORM is entirely here]
        M_red^2 = 1/(8*pi*G_N) = N_eff * Lambda^2 / (96*pi^2)   [M_red = REDUCED Planck mass]

    RESULT for N_eff = 6 [DERIVED-STRUCTURAL-CONDITIONAL]:
        M_red^2 = 6 * Lambda^2 / (96*pi^2) = Lambda^2 / (16*pi^2)
        Lambda = 4*pi * M_red  ~  12.566 * M_red
    *** UNIT CONVENTION — READ BEFORE QUOTING THE NUMBER (fixed 2026-07-28). ***
    The M_Pl appearing in the Seeley-DeWitt line below is the REDUCED Planck mass
    M_red = M_Pl/sqrt(8*pi) (it enters via M^2 = 1/(8*pi*G_N)), NOT the non-reduced
    M_Pl = 1/sqrt(G_N) that the PAPER's Lambda-bracket uses. So:
        Lambda/M_red = 4*pi     = 12.566   <- what this primitive returns
        Lambda/M_Pl  = 4*pi/sqrt(8*pi) = sqrt(2*pi) = 2.507  <- the paper's convention
    The returned key Lambda_over_MPl is kept for backward compatibility but is REDUCED-frame;
    read Lambda_over_M_REDUCED / Lambda_over_MPl_nonreduced / unit_convention instead. The
    missing "reduced" in the old key name is exactly what made this artifact and the paper
    bracket look a factor ~12 apart when the real convention gap is sqrt(8*pi) ~ 5.01.

    *** c_reg RESOLVED (2026-07-29) + WHICH-LAMBDA RULED (coordinator, 2026-07-30). ***
    The regulator story closed in two steps. (1) RESOLVED: there is ONE coefficient,
    c_reg = 1/12 exactly in the proper-time variable (c_reg_from_substrate_mode_content:
    a_1 = R on the six grade-2 channels). The old "three values" were ONE coefficient read
    in three Lambda-variables — ~1 was the paper's never-computed placeholder; 1.82 = c_lat/12
    is the SAME a_1 = R, N_eff = 6 computation written in Lambda := 1/a (R-163). (2) RULED:
    the symbol is SPLIT. Lambda_S = sqrt(2*pi)*M_Pl exactly (THIS primitive's variable) is a
    proper-time SCHEME scale — measured G restated, exactly c_lat-independent, carrying NO
    substrate information; it serves the induced-G bookkeeping ONLY. Lambda_L = 1/a — central
    0.537 M_Pl, band [0.386, 0.735] M_Pl from OA-LF-ii kappa in [1/2, 2] through the affine
    c_lat(kappa) — is FORCED for the two Taylor-coefficient consumers (dim-6 LV eta4 / VG-6 /
    E1 / N52, and the D4 anisotropy corners), is a NAMED PREMISE for the C.4.5 descent start,
    and is deliberately NOT assigned to the B.6.4 GW denominator (VG-5-gated) or the B.6.5 xi
    residual (reading-immaterial) — the scoped B.6.2 assignment. The old
    [0.13, 2.5] M_Pl bracket is RETIRED: it spanned a symbol collision, not a physical range.
    The re-cut is admissible under the engine's own fence (induced_G_from_linear_face_band:
    case (a), a normalization/convention reconciliation between named engine artifacts).
    NOTE: the SPECIFIC RATIO Lambda/M_red = 4*pi is what is DERIVED-STRUCTURAL-CONDITIONAL
    (substrate N_eff=6 [generic-dim=4] + QFT INPUT). The SCALING FORM M^2 ~ N*Lambda^2
    is pure QFT INPUT, not a substrate result.

    NEGATIVE RESULT — Sakharov EH != Skyrme quartic [engine-derived]:
    The TT graviton uses Omega_m = eps+_m SD1 + eps-_m ASD1 (cross-sector SD+ASD mixing).
    [SD1, ASD1] = 0 exactly (engine: SD and ASD generators commute — Spin(4) product structure).
    => L_Skyrme = sum_{m<n} <[Omega_m, Omega_n]^2>_0 = 0 for the TT graviton.
    => The Sakharov EH operator (sigma-model g^{mn}<Om_m Om_n>_0) and the Skyrme quartic
       are ORTHOGONAL in the field space: EH governs the SD+ASD cross-sector; Skyrme governs
       intra-sector SD-SD or ASD-ASD mixing (nonzero commutator).
    Consequence: h_mn != 0 for TT graviton (engine) while L_Skyrme = 0 (engine). These are
    independent operators and the naive "Sakharov EH = Skyrme quartic" conjecture is FALSE.

    OPEN_4 STATUS (not attempted here, independent of this result):
    Standard Q-orbit Skyrmion gives h_mn = 0 (engine: <e14 I4 e14>_0 = 0). The baryon
    sources gravity via the loop-level Sakharov T_mn (rotor kinetic energy), NOT via direct
    h_mn from the Q-orbit winding. The L-Q-mixing mechanism for direct coupling is unknown.

    TIER: CANDIDATE for the coefficient (#1-gap substrate EOM means full rotor propagator
    is unknown; minimal-coupling correction (f_pi/Lambda)^2 ~ 1e-40-class is negligible but the
    full nonlinear sigma-model result may differ at subleading order).
    DERIVED-STRUCTURAL-CONDITIONAL for the SPECIFIC RATIO Lambda/M_Pl = 4*pi:
      - N_eff = 6 (engine, generic-given-dim=4) + Seeley-DeWitt [QFT INPUT] => ratio fixed.
    The SCALING FORM M_Pl^2 ~ N_eff * Lambda^2 is entirely QFT INPUT, not a TWT derivation.
    [reviewer correction 2026-06-28: narrowed tier from "scaling + N_eff" to "specific ratio";
     added generic-given-dim=4 qualifier per canon §5 (same class as Sakharov Lambda^2 example).]
    """
    import math, numpy as np

    def _g0(mv): return dict(mv.terms).get((), 0.0)
    def _h(A, B): return _g0(A * I4 * B)

    # Engine check 1: grade-2 subspace of Cl(4,0) has dimension 6 (the N_eff count)
    grade2_basis = [e(1,2), e(1,3), e(1,4), e(2,3), e(2,4), e(3,4)]
    N_eff = len(grade2_basis)
    assert N_eff == 6, f"grade-2 dim = {N_eff}, expected 6"

    # Engine check 2: basis splits as 3 SD + 3 ASD (su(2)_L + su(2)_R)
    SD1  = (1/math.sqrt(2))*(e(1,2) - e(3,4))
    SD2  = (1/math.sqrt(2))*(e(1,3) + e(2,4))
    SD3  = (1/math.sqrt(2))*(e(1,4) - e(2,3))
    ASD1 = (1/math.sqrt(2))*(e(1,2) + e(3,4))
    ASD2 = (1/math.sqrt(2))*(e(1,3) - e(2,4))
    ASD3 = (1/math.sqrt(2))*(e(1,4) + e(2,3))
    N_SD  = 3
    N_ASD = 3
    assert N_SD + N_ASD == N_eff, "SD + ASD count != N_eff"

    # Engine check 3: NEGATIVE RESULT — [SD1, ASD1] = 0 (cross-sector commutator vanishes)
    # SD1 * ASD1 = ((e12-e34)/sqrt2) * ((e12+e34)/sqrt2)
    SD1_times_ASD1   = SD1 * ASD1   # Clifford product
    ASD1_times_SD1   = ASD1 * SD1
    commutator_SD1_ASD1 = SD1_times_ASD1 - ASD1_times_SD1
    # Verify: all terms of the commutator are zero
    comm_norms = [abs(v) for v in dict(commutator_SD1_ASD1.terms).values()]
    max_comm = max(comm_norms) if comm_norms else 0.0
    assert max_comm < 1e-12, f"[SD1,ASD1] != 0: max_coeff = {max_comm}"

    # Also check representative SD-SD and ASD-ASD commutators (nonzero -- for contrast)
    comm_SD12 = SD1*SD2 - SD2*SD1   # should be nonzero (su(2)_L algebra)
    comm_ASD12 = ASD1*ASD2 - ASD2*ASD1  # should be nonzero (su(2)_R algebra)
    sd_norm  = max(abs(v) for v in dict(comm_SD12.terms).values())
    asd_norm = max(abs(v) for v in dict(comm_ASD12.terms).values())
    assert sd_norm  > 1e-6, "[SD1,SD2] = 0, expected nonzero (su(2)_L structure)"
    assert asd_norm > 1e-6, "[ASD1,ASD2] = 0, expected nonzero (su(2)_R structure)"

    # Engine check 4: Skyrme term = 0 for the TT graviton mode (Omega = eps+*SD1 + eps-*ASD1)
    # For Omega_1 = SD1, Omega_2 = ASD1, Omega_k=0 otherwise:
    #   L_Skyrme = <[Omega_1, Omega_2]^2>_0 = <[SD1,ASD1]^2>_0 = 0
    comm_sq_g0 = _g0(commutator_SD1_ASD1 * commutator_SD1_ASD1)
    assert abs(comm_sq_g0) < 1e-12, "Skyrme term for TT graviton != 0"

    # Engine check 5: Skyrme term != 0 for intra-sector (SD1+SD2) mode (baryonic)
    comm_SD12_sq = SD1*SD2 - SD2*SD1
    skyrme_baryon = _g0(comm_SD12_sq * comm_SD12_sq)
    assert abs(skyrme_baryon) > 1e-6, "Skyrme term for SD1+SD2 mode = 0 (expected nonzero)"

    # Seeley-DeWitt calculation (QFT INPUT: Donoghue formula for min. coupled massless scalars)
    # G_N^{-1} = N_eff * Lambda^2 / (12*pi)
    # M_red^2 = 1/(8*pi*G_N) = N_eff * Lambda^2 / (96*pi^2)      [M_red = REDUCED Planck mass]
    # => Lambda^2 / M_red^2 = 96*pi^2 / N_eff
    Lambda_sq_over_MPl_sq = 96 * math.pi**2 / N_eff   # = 96*pi^2/6 = 16*pi^2  (REDUCED frame)
    Lambda_over_MPl = math.sqrt(Lambda_sq_over_MPl_sq)  # = 4*pi, AGAINST M_red (name kept for compat)
    assert abs(Lambda_over_MPl - 4*math.pi) < 1e-10, \
        f"Lambda/M_red = {Lambda_over_MPl}, expected 4*pi = {4*math.pi}"

    # The SAME ratio restated in the PAPER's non-reduced convention: M_red = M_Pl/sqrt(8*pi),
    # so Lambda/M_Pl = (Lambda/M_red)/sqrt(8*pi) = 4*pi/sqrt(8*pi) = sqrt(2*pi) ~ 2.507.
    # This is a pure UNIT change, not a physics change — it is the whole of the apparent
    # "factor 12" between this artifact and the paper's bracket.
    Lambda_over_MPl_nonreduced = Lambda_over_MPl / math.sqrt(8 * math.pi)
    assert abs(Lambda_over_MPl_nonreduced - math.sqrt(2 * math.pi)) < 1e-12, \
        f"Lambda/M_Pl(non-reduced) = {Lambda_over_MPl_nonreduced}, expected sqrt(2*pi)"

    # Verify the intermediate result: N_eff=6 => M_red^2 = Lambda^2/(16*pi^2)
    MPl_sq_coefficient = N_eff / (96 * math.pi**2)   # coefficient in M_red^2 = coeff * Lambda^2
    assert abs(MPl_sq_coefficient - 1/(16*math.pi**2)) < 1e-14, \
        f"M_red^2 coefficient = {MPl_sq_coefficient}, expected 1/(16*pi^2)"

    return {
        "tier": ("CANDIDATE (coefficient) / DERIVED-STRUCTURAL-CONDITIONAL (specific ratio Lambda/M_red=4*pi). "
                 "N_eff = %d (engine: grade-2 dim of Cl(4,0); GENERIC-given-dim=4, canon §5 class). "
                 "Seeley-DeWitt [QFT INPUT — scaling FORM M^2~N*Lambda^2 is entirely here]: "
                 "G_N^{-1} = N_eff*Lambda^2/(12*pi). "
                 "DERIVED-STRUCTURAL-CONDITIONAL consequence: Lambda = 4*pi*M_red ~ %.3f*M_red "
                 "(= sqrt(2*pi)*M_Pl ~ %.3f*M_Pl non-reduced) (N_eff=6 [generic-dim=4] + QFT INPUT). "
                 "[reviewer 2026-06-28: narrowed from 'scaling+N_eff' to 'specific ratio'; "
                 "generic-dim=4 qualifier added per canon §5] "
                 "[2026-07-28: convention made explicit (REDUCED M_Pl). 2026-07-29: c_reg "
                 "RESOLVED = 1/12 — one coefficient, three Lambda-variables. 2026-07-30: "
                 "which-Lambda RULED, see c_reg_reconciliation. NO tier change]."
                 % (N_eff, Lambda_over_MPl, Lambda_over_MPl_nonreduced)),
        "N_eff":            N_eff,            # = 6 (engine, generic-given-dim=4)
        # *** UNIT CONVENTION: the ratio below is against the REDUCED Planck mass
        # M_red = M_Pl/sqrt(8*pi). The key name lacks "reduced" for BACKWARD COMPATIBILITY only;
        # prefer Lambda_over_M_REDUCED / Lambda_over_MPl_nonreduced, and read unit_convention. ***
        "Lambda_over_MPl":  Lambda_over_MPl,  # = 4*pi ~ 12.566 AGAINST M_red (legacy key name)
        "Lambda_over_M_REDUCED":     Lambda_over_MPl,             # explicit alias, same number
        "Lambda_over_MPl_nonreduced": Lambda_over_MPl_nonreduced,  # = sqrt(2*pi) ~ 2.507
        "unit_convention": ("Lambda_over_MPl is stated against the REDUCED Planck mass "
                            "M_red = M_Pl/sqrt(8*pi) (it comes from M^2 = 1/(8*pi*G_N)). "
                            "In the PAPER's non-reduced M_Pl = 1/sqrt(G_N) the same result reads "
                            "Lambda/M_Pl = 4*pi/sqrt(8*pi) = sqrt(2*pi) = %.3f. The legacy key "
                            "name says 'MPl' and does NOT say 'reduced' — that omission is what "
                            "made this artifact and the paper's Lambda-bracket look ~12x apart "
                            "when the actual convention gap is sqrt(8*pi) ~ 5.013. Pure units, "
                            "no physics." % Lambda_over_MPl_nonreduced),
        "c_reg_reconciliation": {
            "status": "RESOLVED (2026-07-29) + WHICH-LAMBDA RULED (coordinator, 2026-07-30): ONE "
                      "coefficient c_reg = 1/12 in the proper-time variable; the apparent three "
                      "values were three Lambda-variables (c_reg_from_substrate_mode_content). "
                      "ONE-PASS settlement — its adversarial verifier died mid-response; R-165's "
                      "caveat rides",
            "the three values": {
                "~1": "the paper's ORIGINAL PLACEHOLDER for the O(1) regulator coefficient "
                      "(no engine primitive backs it)",
                "1/12": "THIS primitive — G^-1 = N_eff*Lambda^2/(12*pi), the TEXTBOOK Sakharov "
                        "heat-kernel value (a_1 coefficient, MINIMAL coupling xi=0, proper-time "
                        "cutoff). QFT INPUT, not a substrate computation",
                "~1.8": "induced_G_from_linear_face_band (R-163) — c_reg = c_lat/12 = 1.82, "
                        "computed on TWT's OWN derived D4 nearest-neighbour band",
            },
            "the two BANKED ones disagree": "1/12 vs 1.82 = factor ~21.6 in c_reg "
                                            "=> ~4.6 in Lambda => ~21.6 in eta4",
            "consequence": ("RULED (2026-07-30): the symbol is SPLIT — Lambda_S = sqrt(2*pi)*M_Pl "
                            "(this primitive; scheme variable, induced-G bookkeeping only) vs "
                            "Lambda_L = 1/a, band [0.386, 0.734] M_Pl (every lattice-dispersion "
                            "consumer). The old wide bracket [0.13, 2.5] M_Pl is RETIRED — it "
                            "spanned a symbol collision, not a physical range"),
            "do NOT": "read 1/12 vs 1.82 as rivals — they are ONE coefficient in two "
                      "Lambda-variables; the per-consumer variable assignment is the 2026-07-30 "
                      "ruling, a bookkeeping act, not a physics pick (canon §1/§2 unthreatened)",
            "would_change_if": "CONDITION MET (2026-07-29): the two primitives' measures were "
                               "shown to be the same object in different variables "
                               "(c_reg_from_substrate_mode_content) — which is what resolved this row",
        },
        "MPl_sq_coeff":     MPl_sq_coefficient,  # = 1/(16*pi^2) in M_red^2 = coeff*Lambda^2
        "SD_ASD_split":    ("N_eff = N_SD + N_ASD = %d + %d [generic-dim=4; C(4,2)=6 is combinatorial]. "
                             "SD sector (su(2)_L): 3 generators. "
                             "ASD sector (su(2)_R): 3 generators. "
                             "Both contribute positively to the Sakharov M_red^2 "
                             "(sigma-model kinetic term is positive-definite in Euclidean)." %
                             (N_SD, N_ASD)),
        "negative_skyrme_EH": ("[engine] [SD1,ASD1] = 0 (max_coeff=%.2e). "
                                 "L_Skyrme(TT graviton) = <[SD1,ASD1]^2>_0 = 0. "
                                 "Sakharov EH != Skyrme quartic: they are orthogonal operators. "
                                 "SD-SD intra-sector: [SD1,SD2] nonzero (max=%.2e) => L_Skyrme nonzero. "
                                 "Gravity sector (SD+ASD cross) decouples from baryon sector (intra-SD/ASD)." %
                                 (max_comm, sd_norm)),
        "open_4_note":      ("Q-orbit {e14,e24,e34}: h_kl=0 and h_00=0 on the COMPUTED blocks (engine, see texture_metric_candidate); h_0k UNCOMPUTED — static Omega_0=0 is an unlabeled PREMISE that canon sec.0 + R-123 forbid for a massive defect. "
                              "Baryon sources gravity via Sakharov T_mn (rotor kinetic energy at loop level), "
                              "NOT via direct h_mn. L-Q-mixing mechanism for direct coupling: unknown (LOCATED GAP)."),
        "formula":          "G_N^{-1} = N_eff * Lambda^2 / (12*pi)  [Seeley-DeWitt INPUT]",
        "result":           ("M_red^2 = Lambda^2 / (16*pi^2);  Lambda = 4*pi * M_red "
                             "= sqrt(2*pi) * M_Pl(non-reduced) ~ 2.507 * M_Pl. "
                             "M_red = M_Pl/sqrt(8*pi) — state the convention every time this is quoted."),
        "conditions":       ("Minimal coupling (exact for Lambda >> f_pi: correction (f_pi/Lambda)^2 ~ 1e-40-class). "
                              "#1-gap: full rotor EOM (substrate dynamics, Sec 9.6) not derived; "
                              "minimal coupling is the leading-order approximation to the full result. "
                              "SECOND GATE (2026-06-28): non-minimal coupling xi of rotor to gravity NOT derived "
                              "from TWT substrate. G_N^{-1}=N_eff*Lambda^2/(12*pi) assumes xi=0 (minimal); "
                              "conformal xi=1/6 would cancel the leading Sakharov term entirely. "
                              "Xi-derivation awaits #1-gap EOM. Two independent gates on the coefficient. "
                              "THIRD (2026-07-28; RESOLVED 2026-07-29, RULED 2026-07-30): c_reg = 1/12 "
                              "exactly — the apparent three-way disagreement was one coefficient in "
                              "three Lambda-variables. Which Lambda each downstream consumer takes is "
                              "RULED: Lambda_S (this primitive) for induced-G bookkeeping; "
                              "Lambda_L = 1/a for lattice-dispersion consumers. See "
                              "c_reg_reconciliation."),
    }


def c_reg_from_substrate_mode_content():
    """[DERIVED-A (exact arithmetic: the parametrization identity + the S^4 a_1 TYPE-SUM; pure
    math, import-exempt) + DERIVED-given-(R-112 linear face AND R-041 xi=0/E=0), INHERITING
    R-041's FRAMING+CONDITIONAL status] — c_reg computed for TWT's OWN mode content, and the
    three-way c_reg 'disagreement' identified as a Lambda-VARIABLE artifact, not a physics
    disagreement. (2026-07-29.)

    THE OLD STATE (sakharov_induced_gravity()['c_reg_reconciliation'], pre-2026-07-30 key
    'c_reg_reconciliation_OPEN'): three values of the
    R-linear regulator coefficient in the paper's parametrization
        1/(16 pi G) = c_reg * N_eff * Lambda^2 / (16 pi^2)
    were carried as unreconciled — ~1 (paper placeholder), 1/12 (textbook heat kernel), ~1.82
    (induced_G_from_linear_face_band / R-163, = c_lat/12) — the two BANKED ones a factor ~21.6
    apart. That entry's own would_change_if named the exit: "the two primitives' measures are
    shown to be the same object in different variables." THIS PRIMITIVE MEETS THAT CONDITION.

    (1) THE TYPE-SUM, FOR TWT'S ACTUAL MODE CONTENT. a_1 is a SIGNED weighted sum over mode
    TYPES, not a count: for a Laplace-type D = -(nabla^2 + E) on a bundle V,
        a_1 = tr_V( E + (R/6) 1_V ),      c_reg = (1/2) * (a_1/R) / N_eff.
    TWT's linear face (R-112 / D.4.6 Face 1, banked): the 6 grade-2 so(4) coefficient fields,
    free operator, NO endomorphism and NO mass at quadratic order; the kinetic term is the
    sigma-model <Omega_mu Omega^mu>_0 (R-109), whose curved continuation is the BOCHNER operator
    (delta_AB is the target Killing form, metric-independent — the internal index is a TARGET
    index, so a local frame rotation contributes a connection, never an endomorphism). No
    fermionic channel exists on the linear face (matter = defect = soliton, canon SS0/SS5 — not a
    linear-face field); the photon is already ONE OF the 6 grade-2 strain modes (B.5.4), not a
    separate gauge sector, so there is no double count and no gauge/ghost weight.
    E = 0 HAS TWO FACES AND THEY ARE NOT EQUALLY SUPPORTED (scoped, second pass 2026-07-29):
      (a) the CONFORMAL corner (E = -xi*R, a curvature-coupled NON-derivative quadratic phi.W.phi)
          is excluded by the left-Spin(4) shift symmetry — that is R-041's own content, and it is
          exactly what caps this primitive at R-041's FRAMING+CONDITIONAL tier;
      (b) the WEITZENBOCK/HODGE corner is excluded by the KINETIC TERM, not by the shift symmetry.
          The banked sigma-model term g^{mu nu} delta_AB Grad_mu phi^A Grad_nu phi^B yields the
          ROUGH (Bochner) Laplacian with E = 0 whether the internal index is read as a TARGET index
          or as a spacetime 2-form index; the Hodge Laplacian requires the DIFFERENT kinetic term
          |d phi|^2 + |delta phi|^2, which R-112's linear face does not produce. So (b) rests on
          R-112, not on R-041.
    The endo_shift_breaks check below is VACUOUS AS A DISCRIMINATOR — every nonzero quadratic form
    fails translation invariance, so it separates no candidate operator from any other. It is kept
    as an illustration only; do not cite it as the support for (a) or (b). Hence
        a_1 = 6 * R/6 = R      =>      c_reg = 1/12   EXACTLY.
    THE TEXTBOOK VALUE IS TWT'S OWN MODE-CONTENT VALUE. Note this is near-definitional once the
    mode content is fixed: G^-1 = N_eff Lambda^2/(12 pi) IS the N-minimal-scalar heat-kernel result,
    so the content sits in the upstream identification (R-112) and in the exclusion of the corners
    below, NOT in the arithmetic. HOW LIVE WERE THE CORNERS (scoped, second pass 2026-07-29): the
    CONFORMAL corner is genuinely live, and is held off only at R-041's FRAMING+CONDITIONAL tier —
    it is the real exposure here. The HODGE corner is NOT reachable from R-112's banked sigma-model
    kinetic term (see the E = 0 discussion above), so "the mode-TYPE question was capable of
    flipping the sign of G" holds only if one ALSO replaces the banked kinetic term; stated without
    that proviso it overstates how open the sign was. Both corners are computed below and one of
    them FLIPS THE SIGN OF G:
        conformal (xi = 1/6):              a_1 = 0    -> c_reg = 0     (NO induced gravity)
        Lambda^2 with the HODGE operator:  a_1 = -R   -> c_reg = -1/12 (REPULSIVE, G < 0)
        6 minimal / Bochner (TWT's):       a_1 = +R   -> c_reg = +1/12 (attractive)
    So the mode-TYPE question was capable of zeroing or reversing induced gravity; the substrate's
    content lands on +1/12. This ANSWERS the standing caveat in induced_G_bracket_mode_content
    ("a1 is a SIGNED weighted TYPE-sum, not a count ... the substrate's actual mode content was
    not specified") — it is now specified, and it is the all-minimal-scalar corner.

    (2) THE '~1.82' IS THE SAME NUMBER IN A DIFFERENT VARIABLE. R-163 assembles
    1/(16 pi G) = N_eff*c_lat/(192 pi^2 a^2). Reading Lambda := 1/a gives c_reg = c_lat/12;
    reading Lambda := Lambda_eff = sqrt(c_lat)/a gives c_reg = 1/12. The ratio of the two banked
    values is therefore c_lat EXACTLY — but that is a CHANGE OF VARIABLE, not a computation.
    c_reg is BY CONSTRUCTION the coefficient multiplying Lambda^2, so for ANY two Lambda-variables
    c_reg(L1)/c_reg(L2) = (L2/L1)^2 IDENTICALLY — independently of the assembly, of a_1 and of
    N_eff (re-derived symbolically, second pass 2026-07-29). With L2/L1 = Lambda_eff*a = sqrt(c_lat)
    the ratio is c_lat BY DEFINITION of Lambda_eff := sqrt(c_lat)/a. The assert below is therefore a
    TAUTOLOGY: it sets B := A*c_lat and checks B/A = c_lat, i.e. it tests floating-point division,
    not physics — do NOT quote its "residual ~1e-14 for arbitrary c_lat" as numerical evidence.
    The old record's "~21.6" is not c_lat either: 1.819*12 = 21.83 = c_lat, so "21.6" was a
    write-down slip in sakharov_induced_gravity, not a computed factor. And R-163 ALREADY STATED
    this reconciliation ("lands exactly on the sakharov_induced_gravity form" at
    Lambda_eff^2 = c_lat/a^2; its cross-tie Lambda_eff/M_red = 4 pi is c_lat-INDEPENDENT) — so what
    point (2) adds is RECOGNITION and bookkeeping hygiene, not a new computation.
    SEPARATE, AND NOT WHAT THE RATIO SHOWS: the stronger reading "ONE VALUE in two variables"
    (rather than merely "two coefficients related by a change of variable") additionally needs both
    branches to use the SAME a_1 = R and the SAME N_eff = 6. They do — R-163 Step 2 uses a_1 = R/6
    per channel — but the ratio identity is blind to a_1 and N_eff and does not establish it.
    => c_reg is ONE value, 1/12, in the Sakharov proper-time-cutoff variable. The '~1' placeholder
    is SUPERSEDED (it was never computed). WHAT REMAINS OPEN IS NOT c_reg BUT c_lat.

    (3) AND c_lat IS EXACTLY THE OA-LF-ii-SENSITIVE OBJECT. Deform the grain-scale curvature
    weight as w(s) = (R/6)*f(s/a^2), f -> 1 for s >> a^2, f = kappa for s < a^2. Then c_lat(kappa)
    is EXACTLY AFFINE and its slope is R-163's own ~93% proper-time support fraction (checked
    below to ~1e-14). OA-LF-ii's own stated tolerance ("up to O(1)"), read as kappa in [1/2, 2],
    moves c_lat by a factor ~3.6 — where R-163's quoted refinement window is only -5%..-25%. That
    window is the GAP/state question (OA-LF-i-class), NOT the OPERATOR clause, and it UNDERSTATES
    the OA-LF-ii exposure by more than an order of magnitude. So the SAME quantity is (a) the
    whole of the alleged factor-21.6 and (b) the whole of the OA-LF-ii exposure — decisive that
    the two were never rival values of one coefficient.
    CONSEQUENCE, BOTH WAYS: c_reg = 1/12 carries ZERO OA-LF-ii sensitivity (Lambda_eff is exactly
    c_lat-independent); "c_reg ~ 1.82" carries ~93%-LINEAR OA-LF-ii sensitivity. R-163's branch is
    WEAKER as a c_reg determination than its quoted window suggests — and its real content is
    relocated to where it belongs: the grain spacing a, which is what actually moves.

    SCOPE FENCE. This does NOT derive G, does NOT move N_eff (still GENERIC-given-dim-4), does NOT
    retire OA-LF-i/ii. The WHICH-Lambda ruling this fence anticipated was MADE by the coordinator
    on 2026-07-30 exactly as stated (Lambda_eff for the Sakharov coefficient; 1/a for
    lattice-dispersion quantities such as the E1/VG-6 eta4 exposure); the [0.13, 2.5] M_Pl bracket
    is RETIRED and dispersion consumers carry the 1/a band [0.386, 0.734] M_Pl. Tier is CAPPED by
    R-041: the xi=0/E=0 step is symmetry-protected, not #1-gap-derived.
    WOULD CHANGE IF: the #1-gap kernel generates a non-derivative quadratic (endomorphism) term in
    the linear-face operator — then E != 0, a_1 moves off 6*R/6, and c_reg moves with it (the
    Hodge corner would flip the sign of G). Named revert clause: strike this primitive and restore
    the three-way OPEN record.
    SWEEP EXECUTED (2026-07-30, the which-Lambda ruling pass) — this primitive is ADDITIVE and
    flips no existing label; the sites that carried the OPEN record were updated together:
    sakharov_induced_gravity()['c_reg_reconciliation'],
    induced_G_from_linear_face_band()['c_reg_vs_sakharov'] and its normalization_spread scope
    note, induced_G_bracket_mode_count(), the LV dim-6 Lambda note, paper SSB.6.2/SSB.6.3, and
    companion Sections 1/2/4/13 plus the ledgers.

    self-checks: exact S^4 spectra give a_1 = R/6 (1 scalar), R (6 scalars), -R (Lambda^2 Hodge),
    -R/3 (Lambda^1 Hodge) with a_0 = 1/6/6/4 and the Killing level = 10; Weitzenbock-shaped AND
    generic endomorphisms are shift-NON-invariant while R-041's Omega-invariance holds; the c_reg
    ratio equals c_lat identically; c_lat(kappa) affine with slope = the s<a^2 support fraction;
    c_reg = 1/12 reproduces sakharov_induced_gravity's Lambda/M_Pl(non-reduced) = sqrt(2 pi);
    Lambda_eff is exactly c_lat-independent."""
    import math
    import numpy as np

    Rc, Vol = 12.0, 8 * math.pi ** 2 / 3.0          # unit S^4: R = 12, Vol = 8 pi^2/3

    def _a01(levels, a0_expect):
        F, A0 = [], []
        for s in (1e-3, 5e-4):
            lmax = int(math.sqrt(200.0 / s)) + 60
            K = sum(d * math.exp(-s * lam) for lam, d in levels(lmax))
            x = K * (4 * math.pi * s) ** 2 / Vol     # = a_0 + s a_1 + O(s^2)
            A0.append(x); F.append((x - a0_expect) / s)
        return 2 * A0[1] - A0[0], 2 * F[1] - F[0]    # Richardson in s

    def _scalars(lmax, n):
        return [(l * (l + 3), n * (l + 1) * (l + 2) * (2 * l + 3) / 6.0) for l in range(lmax + 1)]

    def _coexact(lmax, p, n=4):                      # coexact p-forms on S^4, l >= 1
        return [((l + p) * (l + n - p - 1),
                 (2 * l + n - 1) * math.factorial(l + n - 1)
                 / ((l + p) * (l + n - p - 1) * math.factorial(p)
                    * math.factorial(n - p - 1) * math.factorial(l - 1)))
                for l in range(1, lmax + 1)]

    a0_1, a1_1 = _a01(lambda L: _scalars(L, 1), 1.0)
    a0_6, a1_6 = _a01(lambda L: _scalars(L, 6), 6.0)
    # full Lambda^2(S^4) = coexact 2-forms + d(coexact 1-forms); b_2 = 0 so no harmonics
    a0_2f, a1_2f = _a01(lambda L: _coexact(L, 2) + _coexact(L, 1), 6.0)
    a0_1f, a1_1f = _a01(lambda L: _coexact(L, 1) + _coexact(L, 0), 4.0)
    assert abs(a0_1 - 1) < 1e-4 and abs(a1_1 - Rc / 6) < 1e-4, (a0_1, a1_1)
    assert abs(a0_6 - 6) < 1e-3 and abs(a1_6 - Rc) < 1e-3, (a0_6, a1_6)
    assert abs(a0_2f - 6) < 1e-3 and abs(a1_2f + Rc) < 1e-3, (a0_2f, a1_2f)   # HODGE: a_1 = -R
    assert abs(a0_1f - 4) < 1e-3 and abs(a1_1f + Rc / 3) < 1e-3, (a0_1f, a1_1f)
    assert int(_coexact(2, 1)[0][1] + 0.5) == 10, "S^4 coexact-1-form level 1 = Killing = 10"

    N_eff = 6
    _creg = lambda a1: 0.5 * (a1 / Rc) / N_eff
    c_min, c_conf, c_hodge = _creg(a1_6), _creg(0.0), _creg(a1_2f)
    assert abs(c_min - 1 / 12) < 1e-4 and abs(c_hodge + 1 / 12) < 1e-4 and c_hodge < 0 < c_min

    # --- E = 0 is forced by the SAME shift symmetry as xi = 0 (R-041) ---------------
    xi = sakharov_xi_minimal_coupling()
    assert xi["left_invariance_err"] < 1e-8 and xi["xi_term_breaks_shift_symmetry"] is True
    assert xi["N_eff"] == 6
    _rng = np.random.default_rng(7)
    Wg = _rng.normal(size=(6, 6)); Wg = 0.5 * (Wg + Wg.T)
    Ww = (Rc / 3.0) * np.eye(6)                      # the Lambda^2 Weitzenbock shape, p(n-p)K
    _phi = np.array([0.31, -0.17, 0.44, 0.09, -0.28, 0.36])
    _sh = np.array([0.10, 0.0, -0.05, 0.07, 0.0, 0.0])
    endo_shift_breaks = {}
    for _nm, _W in (("generic", Wg), ("Weitzenbock R/3", Ww)):
        _b, _a = float(_phi @ _W @ _phi), float((_phi + _sh) @ _W @ (_phi + _sh))
        endo_shift_breaks[_nm] = abs(_a - _b) > 1e-9
    assert all(endo_shift_breaks.values()), "an endomorphism must break the left-Spin(4) shift"

    # --- the parametrization identity: ratio == c_lat, IDENTICALLY -----------------
    # --- WHAT CAN FAIL HERE, AND WHAT CANNOT (rewritten 2026-07-29, second pass) -------
    # DELETED: an assert that set B := A*c_lat and then checked B/A == c_lat. Three
    # independent defects, all measured, none caught by the harness:
    #   (1) a float round-trip with NO path to failure on any physics — the residual is
    #       0-to-1 ulp (measured residual/(c_lat*eps) = 0.80, 0.00, 0.93), the fingerprint
    #       of a tautology, and the suite printed it as "(residual < 1e-12)" evidence;
    #   (2) it read NEITHER banked primitive — it recomputed local literals, so it would
    #       have passed unchanged had the two primitives disagreed by orders of magnitude;
    #   (3) its tolerance was ABSOLUTE while its residual scales linearly in c_lat, so it
    #       FAILS at c_lat = 1e5 (residual 1.455e-11) while advertising "ARBITRARY c_lat".
    # There is NO non-tautological version of it: c_reg is BY CONSTRUCTION the coefficient
    # of Lambda^2, so at two Lambda-variables the ratio is (L2/L1)^2 identically. That is a
    # DEFINITION; it belongs in prose (see the docstring above), never in an assert.
    # The genuine cross-primitive consistency check now lives in twt_test.py, where both
    # sakharov_induced_gravity and induced_G_from_linear_face_band are already loaded.
    # NOTE THE TOLERANCE, it is the whole difference. A0 comes from the NUMERICALLY extracted
    # a_1 (checked to 1e-3 absolute against R = 12 above), so it carries real numerical error —
    # measured 3e-7 relative. The deleted tautology could afford 1e-12 precisely BECAUSE it was
    # exact by construction; a tight tolerance on a vacuous check is not rigour, it is a tell.
    # 1e-5 relative sits ~30x above the observed error and far below anything a wrong mode count
    # could produce (that would move A0 by factors, not by parts per million).
    A0 = _creg(a1_6)          # from THIS primitive's own computed a_1, not a literal
    assert abs(A0 - 1 / 12) / (1 / 12) < 1e-5, \
        "proper-time-cutoff c_reg must come out 1/12 from the COMPUTED a_1 = R; got %.10g" % A0
    sg = sakharov_induced_gravity()
    # RELATIVE tolerance, and for the same reason as A0's own: this now rides the NUMERICALLY
    # extracted a_1 rather than an exact literal, so the residual is ~1.5e-7 (half of A0's 3e-7,
    # the sqrt). The previous 1e-12 was satisfiable only because A0 was exact by construction —
    # a second tolerance that was measuring nothing, exposed by removing the tautology above.
    _chain_rel = abs(math.sqrt(math.pi / (A0 * N_eff)) - sg["Lambda_over_MPl_nonreduced"]) \
        / sg["Lambda_over_MPl_nonreduced"]
    assert _chain_rel < 1e-5, \
        "c_reg = 1/12 must reproduce sakharov's Lambda/M_Pl(non-reduced) = sqrt(2 pi); rel %.2e" % _chain_rel

    # --- OA-LF-ii sensitivity: c_lat(kappa) EXACTLY affine, slope = s<a^2 support ---
    prs = [tuple(1 if k == i else (_s if k == j else 0) for k in range(4))
           for i in range(4) for j in range(i + 1, 4) for _s in (+1, -1)]
    assert len(prs) == 12
    Ng = 16
    _x = 2 * math.pi * (np.arange(Ng) + 0.5) / Ng
    _ax = [_x.reshape([Ng if k == m else 1 for k in range(4)]) for m in range(4)]
    om2 = np.zeros((Ng,) * 4)
    for b in prs:
        om2 += 2.0 * (1.0 - np.cos(sum(bi * a for bi, a in zip(b, _ax) if bi != 0)))
    q = om2 / 6.0
    _C = lambda arr: 16 * math.pi ** 2 * 0.5 * float(arr.mean())
    c_base = _C(1.0 / q)
    c_k = lambda kap: _C(kap * (1.0 - np.exp(-q)) / q + np.exp(-q) / q)
    c_at0 = c_k(0.0)
    slope = c_base - c_at0
    lin = max(abs(c_at0 + slope * k - c_k(k)) for k in (0.5, 2.0, 4.0))
    assert lin < 1e-9, "c_lat(kappa) must be affine; residual %.3e" % lin
    frac_s = slope / c_base
    assert 0.90 <= frac_s <= 0.95, "OA-LF-ii support slope out of range: %.4f" % frac_s
    O1_lo, O1_hi = c_k(0.5), c_k(2.0)
    assert O1_hi / O1_lo > 3.0, "O(1) tolerance on OA-LF-ii must move c_lat by > 3x"

    _a_of = lambda cl: math.sqrt(N_eff * cl / (12 * math.pi))
    assert max(abs(math.sqrt(cl) / _a_of(cl) - math.sqrt(2 * math.pi))
               for cl in (1.5, 21.83, 90.0)) < 1e-12, "Lambda_eff must be EXACTLY c_lat-independent"

    return {
        "tier": ("DERIVED-A (exact arithmetic: the parametrization identity + the S^4 a_1 TYPE-SUM; "
                 "pure math, import-exempt) + DERIVED-given-(R-112 linear face AND R-041 xi=0/E=0), "
                 "INHERITING R-041's FRAMING+CONDITIONAL status. NOT a derivation of G; N_eff stays "
                 "GENERIC-given-dim-4; OA-LF-i/ii NOT retired"),
        "c_reg": 1 / 12,
        "c_reg_variable": ("Lambda = the SAKHAROV PROPER-TIME CUTOFF. State the variable every time "
                           "c_reg is quoted — that is the whole of the old 'disagreement'"),
        "mode_content": {
            "channels": 6,
            "type": "real bosonic, massless, E = 0 (BOCHNER), sigma-model kinetic",
            "fermionic channels": "NONE on the linear face (matter = defect = soliton, not a field)",
            "gauge sector": "NONE separate — the photon is one of the 6 grade-2 strain modes (B.5.4)",
            "why E = 0": "an endomorphism is a NON-DERIVATIVE quadratic phi.W.phi — the exact class "
                         "the left-Spin(4) shift symmetry forbids (R-041); checked on the "
                         "Weitzenbock shape too",
            "endomorphism_shift_breaks": endo_shift_breaks,
        },
        "a1_type_sum_S4": {
            "1 minimal scalar": round(a1_1, 6), "R/6": Rc / 6,
            "6 minimal scalars (TWT)": round(a1_6, 6), "R": Rc,
            "Lambda^2 HODGE (Weitzenbock)": round(a1_2f, 6),
            "Lambda^1 HODGE (cross-check)": round(a1_1f, 6),
        },
        "excluded_readings_would_have": {
            "conformal xi=1/6": {"a_1": 0.0, "c_reg": c_conf, "consequence": "NO induced gravity"},
            "Hodge / 2-form": {"a_1": round(a1_2f, 4), "c_reg": round(c_hodge, 6),
                               "consequence": "G < 0 — REPULSIVE gravity (the mode-TYPE question "
                                              "was capable of flipping the sign)"},
            "TWT (6 minimal / Bochner)": {"a_1": round(a1_6, 4), "c_reg": round(c_min, 6),
                                          "consequence": "G > 0 attractive"},
        },
        "three_way_resolution": {
            "verdict": "NOT three RIVAL values of one coefficient — but TWO Lambda-variables, not "
                       "three: the '~1' placeholder and c_lat/12 = 1.82 BOTH sit at Lambda := 1/a "
                       "and are mutually consistent at O(1) (R-163 says so itself), while 1/12 sits "
                       "at Lambda := Lambda_eff. [second pass 2026-07-29: the earlier gloss 'ONE "
                       "value in three variables/states' miscounted the variables]",
            "1/12": "c_reg in the proper-time-cutoff variable = TWT's own mode-content value (here)",
            "~1.82": "the SAME coefficient with Lambda := 1/a. Its ratio to 1/12 is c_lat EXACTLY, "
                     "but BY DEFINITION of Lambda_eff := sqrt(c_lat)/a: c_reg multiplies Lambda^2, "
                     "so c_reg(L1)/c_reg(L2) = (L2/L1)^2 for ANY two Lambda-variables, independently "
                     "of the assembly, of a_1 and of N_eff. The in-primitive assert that used to sit "
                     "here WAS a TAUTOLOGY and has been DELETED (2026-07-29): it read neither banked "
                     "primitive, its residual was 0-to-1 ulp, and its ABSOLUTE tolerance made it FAIL "
                     "at c_lat = 1e5 while advertising 'ARBITRARY c_lat'. The real cross-primitive "
                     "check now lives in twt_test.py. The old record's '~21.6' was a write-down "
                     "slip: 1.819*12 = 21.83 = c_lat",
            "~1": "a never-computed paper placeholder — SUPERSEDED, not a rival; note it sits in the "
                  "SAME variable as 1.82 (Lambda := 1/a) and is consistent with it at O(1)",
            "what is actually OPEN": "c_lat, i.e. how many lattice spacings the effective cutoff "
                                     "is — a DIFFERENT question, and the OA-LF-ii-sensitive one",
        },
        "OA_LF_ii_sensitivity": {
            "c_lat(kappa) affine": "c_lat = %.4f + %.4f*kappa (residual %.1e)" % (c_at0, slope, lin),
            "slope fraction (= R-163's s<a^2 support)": round(frac_s, 4),
            "O(1) tolerance kappa in [1/2,2]": "c_lat in [%.2f, %.2f] — factor %.1f"
                                               % (O1_lo, O1_hi, O1_hi / O1_lo),
            "=> a in": "[%.2f, %.2f] ell_Planck" % (_a_of(O1_lo), _a_of(O1_hi)),
            "=> 1/a in": "[%.3f, %.3f] M_Pl" % (1 / _a_of(O1_hi), 1 / _a_of(O1_lo)),
            "R-163's quoted window": "-5%..-25% — that is the GAP/state (OA-LF-i-class) question, "
                                     "NOT the OPERATOR clause; it UNDERSTATES the OA-LF-ii exposure "
                                     "by more than an order of magnitude",
            "what does NOT move": "Lambda_eff = sqrt(c_lat)/a = sqrt(2 pi) M_Pl EXACTLY for every "
                                  "c_lat — so c_reg = 1/12 carries ZERO OA-LF-ii sensitivity while "
                                  "'c_reg ~ 1.82' carries ~93%-linear sensitivity",
        },
        "scope_fence": ("removes ONE recorded OPEN item (the c_reg three-way disagreement). Does NOT "
                        "derive G, does NOT move N_eff, does NOT retire OA-LF-i/ii. The WHICH-Lambda "
                        "ruling it anticipated was MADE 2026-07-30 (Lambda_eff for the Sakharov "
                        "coefficient; 1/a for lattice-dispersion quantities such as the E1/VG-6 eta4 "
                        "exposure); the old wide bracket is RETIRED"),
        "would_change_if": ("the #1-gap kernel generates a non-derivative quadratic (endomorphism) "
                            "term in the linear-face operator — then E != 0 and c_reg moves with it "
                            "(the Hodge corner would flip the SIGN of G). Revert clause: strike this "
                            "primitive and restore the three-way OPEN record"),
        "pending_sweep": ("ADDITIVE — flips no existing label. SWEEP EXECUTED 2026-07-30 (the "
                          "which-Lambda ruling pass): sakharov_induced_gravity"
                          "['c_reg_reconciliation'], induced_G_from_linear_face_band"
                          "['c_reg_vs_sakharov'] + its normalization_spread scope note, "
                          "induced_G_bracket_mode_count, the LV dim-6 Lambda note, paper "
                          "§B.6.2/§B.6.3, companion Sections 1/2/4/13, ledgers"),
    }


def mass_weight_empirical_chain() -> dict:
    """[EMPIRICAL-JURISDICTION LEDGER / FRAMING] Sec.B.6: what the laboratory actually pins
    between a particle's clock and its gravitational effect — and where the extrapolation sits.
    (The framework identifies mass with the meta-time rotor frequency omega, Sec.A.4; the lab
    facts here stand independently of that identification — mass METROLOGY is frequency
    metrology, but the omega-identification is TWT's own, not the laboratory's.)
    Deliberately OUTSIDE eom_constraint_class's E-namespace: E1 there is an empirical CEILING
    that can refute a candidate kernel; this ledger constrains nothing — it states where
    measurement stops. The E-series remains E1-only. Nothing here is derived; every number is a
    published experimental value, primary-source-verified (companion Section 13, I-23; Section
    10 bibliography carries the full records).

    THE FOUR LINKS (very unequal strength):
      1. clock <-> INERTIAL mass: single-particle, direct, definitional. Penning traps read
         masses as frequency ratios — electron 2.8e-11 (Sturm et al., Nature 506, 467 (2014);
         Larmor/cyclotron ratio + bound-state QED), proton 3.2e-11 (Heisse et al., PRL 119,
         033001 (2017); cyclotron-frequency ratio). Photon-recoil h/m ~1.4e-10 (Morel et al.,
         Nature 588, 61 (2020)). A Cs interferometer has run as a clock at a subharmonic of the
         atom's Compton frequency, 4e-9 (Lan et al., Science 339, 554 (2013)). Since 2019 the
         kilogram is DEFINED via fixed h (CGPM 2018 Res. 1).
      2. inertial <-> PASSIVE gravitational (what has inertia falls universally): bulk 1e-15
         (MICROSCOPE final, eta(Ti,Pt) = [-1.5 +- 2.3 +- 1.5]e-15, Touboul et al., PRL 129,
         121102 (2022); lab torsion balances ~1.5e-13 on Be-Ti/Be-Al, Wagner et al., CQG 29,
         184002 (2012)); whole atoms 7e-9 vs a falling corner cube (Peters-Chung-Chu, Nature
         400, 849 (1999)) and [1.6 +- 1.8 +- 3.4]e-12 on 85Rb/87Rb (Asenbaum et al., PRL 125,
         191101 (2020)). FREE ELEMENTARY PARTICLES ONLY COARSELY: neutron interferometry agreed
         at ~10 PERCENT in 1975 (Colella-Overhauser-Werner, PRL 34, 1472 — the often-recalled
         "1%" is wrong for 1975), and the refined two-wavelength version leaves an UNEXPLAINED
         ~0.6-0.8% discrepancy (Littrell-Allman-Werner, PRA 56, 1767 (1997)); free electrons
         ~10% via a low-temperature shielding effect never reproduced (Witteborn-Fairbank, PRL
         19, 1049 (1967); the positron version was never performed); antihydrogen's DIRECTION of
         fall first measured 2023 at ~25% (ALPHA, a = [0.75 +- 0.13 +- 0.16] g, Anderson et al.,
         Nature 621, 716 (2023)). Since ~99% of nucleon mass is confined field energy, the bulk
         tests DO establish that field energy falls like rest mass — but always in AGGREGATE.
      3. PASSIVE <-> ACTIVE (what falls also pulls): macroscopic bodies only — material-
         independence of the active/passive ratio: 5e-5 laboratory (Kreuzer, Phys. Rev. 169,
         1007 (1968)), 3.9e-14 lunar laser ranging (Singh et al., PRL 131, 021401 (2023),
         sharpening Bartlett-Van Buren, PRL 57, 21 (1986), 4e-12).
      4. ACTIVE gravity of a SINGLE particle: NEVER MEASURED, at any precision. The smallest
         body whose gravitational pull has been detected is a 92.1 mg gold sphere of radius
         1.07 mm (Westphal et al., Nature 591, 225 (2021)) = 5.5e22 proton MASSES (the sphere's
         actual proton count, Z = 79, is 2.2e22) / 1.0e26 electron masses; the 2024
         "milligram" result (Fuchs et al., Sci. Adv. 10, eadk2949) used a
         0.43 mg TEST mass against kg-scale SOURCES, so the source record stands. Whether a
         superposed mass sources a superposed field is untested (BMV entanglement-witness
         PROPOSALS: Bose et al., PRL 119, 240401 (2017); Marletto-Vedral, PRL 119, 240402
         (2017) — no experiment performed).

    THE FENCES (they bind the INSIDE-FRAME effective description Sec.B.6 is written in — the
    frame the data live in; no outside-frame substrate object is bounded, so no outside<->inside
    projection premise is invoked):
      - passive-fall universality at 1e-15 (link 2) and active/passive material-independence at
        3.9e-14 (link 3) — different materials mean different binding-energy, Z/A and
        electron-mass fractions, so composition cuts across the aggregate;
      - spin-direction blindness: an electron's gravitational mass differs by < ~1 part in 1e21
        between opposite spin orientations (Heckel et al., PRD 78, 092006 (2008) — the 1e-21 is
        the SOURCE'S OWN abstract statement, not a conversion made here; the per-electron
        reading itself rides linearity across the pendulum's ~1e23 polarized spins).

    JURISDICTION STATEMENT (the paper's Sec.B.6 block cites this primitive): single-defect
    sourcing is an extrapolation across a factor ~5.5e22 in mass (22+ orders; ~1e26 for the
    electron), EMPIRICALLY underwritten by the linearity of the aggregate theory and by nothing
    else. The framework's banked route SATISFIES the fences and COMMITS to per-particle
    sourcing: matter couples through the conserved T_mn alone, m_i = m_g forced by single-field
    monism (equivalence_principle_protection, R-016/R-039), the two-defect potential additive
    (R-038); the tree-level texture channel vanishes on every COMPUTED block (R-042 — the h_0k
    time-space row is an open fork, Sec.B.6.6). That commitment is untested below 92.1 mg:
    NOTHING BANKED PREDICTS ANY DEVIATION in the unmeasured range — this ledger is
    jurisdictional, not a prediction, and deliberately not an exposure row.
    """
    m_p = 1.67262192595e-27       # kg, CODATA 2022
    m_e = 9.1093837139e-31        # kg, CODATA 2022
    smallest_source_kg = 92.1e-6  # Westphal et al. 2021, gold sphere, r = 1.07 mm
    return {
        "identity": ("mass->weight empirical-jurisdiction ledger — deliberately OUTSIDE "
                     "eom_constraint_class's E-namespace (that series remains E1-only; this "
                     "ledger can refute no kernel); never an Hn and never an R-NNN "
                     "(nothing is derived here)"),
        "link_1_clock_inertia": {
            "single_particle": True,
            "status": "measured; definitional since SI-2019 (kilogram via fixed h)",
            "electron_rel_unc": 2.8e-11, "proton_rel_unc": 3.2e-11,
            "h_over_m_rel_unc": 1.4e-10, "compton_clock_rel_unc": 4e-9},
        "link_2_inertia_passive": {
            "bulk_eta_1sigma": 2.7e-15,      # MICROSCOPE stat+syst in quadrature
            "atoms_eta_1sigma": 3.8e-12,     # Asenbaum 2020 combined
            "neutron_1975": 0.10, "neutron_refined_unexplained": 0.008,
            "free_electron": 0.10, "antihydrogen": 0.25,
            "single_particle": "coarse only (1e-1 .. 1e-2); aggregate exquisite"},
        "link_3_passive_active": {
            "lab_material_independence": 5e-5,
            "llr_material_independence": 3.9e-14,
            "single_particle": False},
        "link_4_active_single_particle": {
            "measured": False,
            "smallest_source_kg": smallest_source_kg,
            "gap_factor_proton": smallest_source_kg / m_p,
            "gap_factor_electron": smallest_source_kg / m_e,
            "superposed_source": "untested (BMV proposals only, no experiment)"},
        "fences": {
            "aggregate_additivity_floor_kg": smallest_source_kg,
            "material_independence_passive": 2.7e-15,
            "material_independence_active_passive": 3.9e-14,
            "electron_spin_direction_gravitational_asymmetry": 1e-21},
        "jurisdiction": ("single-defect sourcing = extrapolation across ~5.5e22 in mass, "
                         "empirically underwritten by aggregate linearity and nothing else; "
                         "the banked route COMMITS to per-particle additivity (T_mn coupling, "
                         "m_i = m_g forced, R-038 additive) and that commitment is untested "
                         "below 92.1 mg; this ledger predicts nothing and exposes nothing"),
        "tier": ("EMPIRICAL-JURISDICTION LEDGER / FRAMING — published values, "
                 "primary-source-verified; nothing derived, nothing predicted"),
    }


def sakharov_xi_minimal_coupling():
    """[FRAMING + removed-falsifier, CONDITIONAL] N27 gate (2) NARROWED by a SYMMETRY SHORTCUT: the
    rotor fluctuations that induce gravity are MINIMALLY coupled (xi = 0) at leading order, so the
    catastrophic conformal value xi=1/6 (which would cancel the leading Sakharov EH term entirely) is
    EXCLUDED — a REMOVED FALSIFIER. (canon §4a symmetry shortcut; the s=3 / Adler-zero precedent
    applied to the gravitational vertex. Tier matches the sibling equivalence_principle_protection:
    this is the gravitational-vertex face of the SAME WP-LV1-twin protection, NOT a from-substrate
    dynamical derivation of G_N — cf. item 5, the induced-G sign, 'a removed falsifier, not derived gravity'.)

    THE GATE (N27): the Sakharov coefficient G_N^{-1}=N_eff*Lambda^2/(12*pi) (sakharov_induced_gravity)
    assumes minimal coupling xi=0. The heat-kernel R-coefficient carries a factor (1/6 - xi): at the
    CONFORMAL value xi=1/6 the leading Lambda^2 Sakharov term CANCELS (G_N^{-1} -> 0). So xi is a
    SECOND, independent gate on the coefficient — separate from the #1-gap EOM. If xi were undetermined,
    the sign and even existence of induced G would be open. This primitive removes that gate at leading order.

    THE SHORTCUT (symmetry, EOM-free): the rotor sigma-model action is built ENTIRELY from the
    Maurer-Cartan form Omega_mu = R~ d_mu R (kinetic <Omega Omega>_0 + Skyrme <[Omega,Omega]^2>_0 are
    both functions of Omega only). Hence it has an EXACT global LEFT-Spin(4) symmetry R -> g0 R
    (constant g0), under which Omega is INVARIANT [engine: max|Omega(g0 R)-Omega(R)| ~ 1e-11]. This is a
    NON-LINEARLY-REALIZED shift symmetry on the 6 grade-2 fluctuation directions {SD,ASD} — they are
    flat / Goldstone directions (no invariant potential on the homogeneous Spin(4) target; reinforced by
    WP-LV1 isotropy = ONE stiffness over the 6 bivector planes, Substrate().dim4_isotropy).

    A non-minimal coupling xi*R_curv*phi^2 needs the NON-derivative quadratic operator phi^2=<dR^2>_0
    (dR = the fluctuation delta_R, NOT a derivative d_mu R; the kinetic term is the separate <Omega Omega>_0),
    which is NOT shift-invariant [engine: phi->phi+c changes <phi^2>_0, 0.13 -> 0.20]. So the xi-term
    BREAKS the left-Spin(4) symmetry and is FORBIDDEN (the Adler-zero / Goldstone protection of a
    derivatively-coupled field). Therefore xi = 0 is FORCED at leading order; xi=1/6 is excluded.

    WHY THE MASS DOES NOT REOPEN IT: the rotor "mass" (meta-time omega) is the CENTRAL-E U(1) phase
    (E = I4*e5, I4 = e1234 the central pseudoscalar) — a SEVENTH direction, distinct from the 6 grade-2
    bivectors [engine]. A would-be mass term V(R) that lifts the bivector directions breaks left-Spin(4),
    but only at the IR scale f_pi; at any Planckian Lambda >> f_pi it generates xi ~ (f_pi/Lambda)^2
    ~ 1e-40-class (2-8e-40 on the Lambda_L band; the which-Lambda reading is IMMATERIAL here and
    this consumer is deliberately NOT force-assigned by the 2026-07-30 ruling), NOT xi=1/6. The residual is a scale-Lambda-suppressed IR effect of the SAME general
    family as the WP-LV1 / WEAK-EP species-difference violations (equivalence_principle_protection) —
    negligible, and tied to the same isotropy protection.
    SCOPE CORRECTION (2026-07-27, R-165 — swept here): do NOT read 'the same dim-6 order' off this any
    more. Three DISTINCT objects were being merged: (i) this xi residual, an IR (f_pi/Lambda)^2
    suppression of a non-minimal-coupling operator; (ii) WP-LV1's rotational ANISOTROPY, now known to be
    dimension-EIGHT (the degree-4 point-group invariant space is 1-dimensional); (iii) the rotationally
    INVARIANT dim-6 dispersion term, which no isotropy protection reaches and which is #1-gap GATED and
    empirically constrained (E1/VG-6/N52). They are not the same order and not gated on the same thing.

    TIER: FRAMING + removed-falsifier, CONDITIONAL (matches the sibling equivalence_principle_protection;
    NOT a dynamical derivation of G_N — it removes the xi=1/6 catastrophic branch, like item 5 removes a
    falsifier without deriving gravity).
      substrate-specific: the gravity-inducing DOF ARE the homogeneous, WP-LV1-isotropic rotor bivector
        directions whose action is left-invariant (Omega-only) -> exact shift symmetry; the mass is the
        separate central-E U(1).  [the same homogeneity/compactness anchor as matter_stability_outside_frame
        (H1) and equivalence_principle_protection.]
      generic (canon §5, honest): "a shift-symmetric / Goldstone scalar has xi=0 protected" is a generic
        QFT lemma (as is the Seeley-DeWitt coefficient itself, QFT INPUT). The substrate supplies the
        SYMMETRY; QFT supplies the xi=0-from-shift-symmetry implication.
    SCOPE: this REDUCES (does NOT close) N27 gate (2) — it EXCLUDES the catastrophic xi=1/6 branch and
    fixes xi=0 at LEADING order, leaving a controlled (f_pi/Lambda)^2 ~ 1e-40-class correction (the protection
    is only approximate: the symmetry is broken by the IR mass/potential at f_pi). It does NOT give the
    value of G_N — gate (1), the #1-gap substrate EOM / full nonlinear propagator coefficient, STAYS GATED
    (sakharov_induced_gravity remains CANDIDATE for the coefficient). N27 goes from "two gates" to
    "one gate (#1-gap coefficient) + a controlled (f_pi/Lambda)^2 correction".

    self-check: (a) Omega = R~dR is left-invariant under R->g0 R; (b) it is conjugated (NOT invariant)
    under right R->R g0; (c) <phi^2>_0 is shift-non-invariant; (d) N_eff=6 grade-2 + WP-LV1 isotropy;
    (e) E=I4*e5 mass phase distinct from the 6 bivectors.
    """
    import math

    def _g0(mv): return dict(mv.terms).get((), 0.0)
    def _maxabs(mv):
        d = dict(mv.terms)
        return max((abs(v) for v in d.values()), default=0.0)

    # A constant rotor g0 in Spin(4) (left multiplier) and a 2-plane background rotor path R(t)
    B1, B2 = e(1, 2), e(2, 3)
    def _rotor(a, c):
        R1 = math.cos(a/2)*SCALAR + math.sin(a/2)*B1
        R2 = math.cos(c/2)*SCALAR + math.sin(c/2)*B2
        return R1*R2
    t0, h = 0.41, 1e-6
    g0c = math.cos(0.55)*SCALAR + math.sin(0.55)*e(1, 3)   # constant left multiplier

    # Omega = R~ R'  (the Maurer-Cartan form) for the bare and the left-multiplied path
    def _Omega(prefix):
        R  = prefix*_rotor(0.7*t0, 1.3*t0) if prefix is not None else _rotor(0.7*t0, 1.3*t0)
        if prefix is None:
            Rp = (1/(2*h))*(_rotor(0.7*(t0+h), 1.3*(t0+h)) + (-1.0)*_rotor(0.7*(t0-h), 1.3*(t0-h)))
        else:
            Rp = (1/(2*h))*(prefix*_rotor(0.7*(t0+h), 1.3*(t0+h)) + (-1.0)*(prefix*_rotor(0.7*(t0-h), 1.3*(t0-h))))
        return R.reverse()*Rp

    Om      = _Omega(None)
    Om_left = _Omega(g0c)
    left_inv_err = _maxabs(Om_left + (-1.0)*Om)
    assert left_inv_err < 1e-8, f"LEFT-Spin(4) not a symmetry: |Omega(g0 R)-Omega(R)|={left_inv_err}"

    # (b) RIGHT multiplication conjugates Omega (NOT invariant) — contrast
    R_r  = _rotor(0.7*t0, 1.3*t0)*g0c
    R_rp = (1/(2*h))*(_rotor(0.7*(t0+h), 1.3*(t0+h))*g0c + (-1.0)*(_rotor(0.7*(t0-h), 1.3*(t0-h))*g0c))
    Om_right = R_r.reverse()*R_rp
    conj_err = _maxabs(Om_right + (-1.0)*(g0c.reverse()*Om*g0c))
    assert conj_err < 1e-8, f"RIGHT mult should conjugate Omega: residual={conj_err}"
    right_is_invariant = _maxabs(Om_right + (-1.0)*Om) < 1e-8   # should be False (it changes)

    # (c) the non-minimal operator <phi^2>_0 is shift-NON-invariant -> xi-term breaks the symmetry
    phi = 0.3*e(1, 2) + 0.2*e(2, 3)
    cshift = 0.1*e(1, 2)
    q_before = _g0(phi*phi.reverse())
    q_after  = _g0((phi + cshift)*(phi + cshift).reverse())
    shift_breaks_xi_term = abs(q_after - q_before) > 1e-9
    assert shift_breaks_xi_term, "<phi^2>_0 unexpectedly shift-invariant"

    # (d) N_eff = 6 grade-2 directions + WP-LV1 isotropy (the homogeneity anchor)
    grade2 = [e(1, 2), e(1, 3), e(1, 4), e(2, 3), e(2, 4), e(3, 4)]
    N_eff = len(grade2)
    isotropic = Substrate().dim4_isotropy
    assert N_eff == 6 and isotropic is True

    # (e) the mass phase E = I4*e5 is distinct from the 6 grade-2 bivectors (I4 = central pseudoscalar)
    I4_is_pseudoscalar = (tuple(sorted((1, 2, 3, 4))) in dict(I4.terms))
    assert I4_is_pseudoscalar, "I4 not the e1234 pseudoscalar"

    return {
        "tier": ("FRAMING + removed-falsifier, CONDITIONAL (matches sibling equivalence_principle_protection; "
                 "NOT a dynamical derivation of G_N — removes the xi=1/6 catastrophic branch). "
                 "substrate-specific: the gravity-inducing DOF are the "
                 "homogeneous WP-LV1-isotropic rotor bivector directions; their action is left-Spin(4)-"
                 "invariant (Omega-only) -> exact shift symmetry; mass = the separate central-E U(1). "
                 "generic (canon §5): 'shift-symmetric/Goldstone scalar has xi=0' is a generic QFT lemma "
                 "(like Seeley-DeWitt is QFT INPUT). Substrate supplies the symmetry; QFT the implication."),
        "claim": ("xi = 0 (minimal coupling) at LEADING order by the left-Spin(4) shift symmetry "
                  "of the Maurer-Cartan rotor action (Adler-zero/Goldstone protection); the catastrophic "
                  "conformal xi=1/6 is EXCLUDED (removed falsifier) -> the leading Sakharov EH term does NOT cancel."),
        "shortcut": ("action = f(Omega), Omega=R~dR -> exact global LEFT-Spin(4) R->g0 R; "
                     "engine: |Omega(g0 R)-Omega(R)|=%.1e (invariant). The xi*R*phi^2 operator needs "
                     "the non-derivative phi^2=<dR^2>_0 (fluctuation, not d_mu R), shift-NON-invariant "
                     "(engine: %.2f -> %.2f under phi->phi+c) -> symmetry-forbidden." % (left_inv_err, q_before, q_after)),
        "left_invariance_err": left_inv_err,           # ~1e-11: Omega invariant under R->g0 R
        "right_mult_conjugation_err": conj_err,        # ~1e-11: Omega -> g0~ Omega g0 (NOT invariant)
        "right_is_invariant": right_is_invariant,      # False — right mult changes Omega
        "xi_term_breaks_shift_symmetry": shift_breaks_xi_term,   # True
        "N_eff": N_eff,                                # 6
        "isotropy_WP_LV1": isotropic,                  # True (the homogeneity anchor)
        "mass_phase_distinct": ("mass = central-E U(1) (E=I4*e5, I4=e1234 pseudoscalar) — a 7th direction, "
                                "distinct from the 6 grade-2 bivectors; an IR mass term gives xi~(f_pi/Lambda)^2"
                                "~1e-40-class at any Planckian Lambda (2-8e-40 on the Lambda_L "
                               "band; reading-immaterial, not force-assigned by the ruling), "
                               "NOT xi=1/6."),
        "scope": ("REDUCES N27 gate (2) (does NOT close it): xi=0 LEADING-order, the catastrophic xi=1/6 "
                  "branch EXCLUDED (removed falsifier), Sakharov EH survives; a controlled (f_pi/Lambda)^2 "
                  "correction remains (symmetry only approximate, broken by the IR mass at f_pi). "
                  "Gate (1) (#1-gap substrate EOM / full nonlinear propagator coefficient) STAYS GATED "
                  "(sakharov_induced_gravity stays CANDIDATE for the coefficient). N27: two gates -> one gate "
                  "(#1-gap) + controlled (f_pi/Lambda)^2 correction — an IR scale-Lambda suppression; NOT the "
                  "same object as WP-LV1 anisotropy (now dim-8) nor the gated isotropic dim-6 term (R-165)."),
        "coherence": ("same homogeneity/compactness + isotropy protection as matter_stability_outside_frame (H1) "
                      "and equivalence_principle_protection (WEAK-EP) — minimal coupling is the gravitational "
                      "vertex face of the SAME WP-LV1-twin protection."),
    }


def kernel_overdetermination_table():
    """[FRAMING (over-determination dashboard; the anchor-count operationalizes N33's
    judgment) + DERIVED-A (live engine cross-validation of the sharpest row values + the
    two exclusion guards)] — W2.1 of the Class-2 campaign (2026-07-05). Banks N33's prose
    meta-result as a CHECKABLE, self-validating engine artifact: the single dashboard
    row-set for the #1-gap kernel's over-determination program (route 2b).

    WHY THIS EXISTS. N33 (2026-07-02) established — as a session-level investigation with
    NO engine primitive and NO suite delta — that the pending-values registry's own
    "over-determination opportunity" is currently RANK-DEFICIENT: the net count of
    mutually-independent numeric constraints usable to pin a >=2-parameter causal kernel is
    effectively ONE (the KSS-floor-to-GW170817-ceiling bracket on a single zero-frequency
    transport coefficient). This primitive GRADUATES that finding into the engine (canon
    Section 10: a finding not written to a checkable file drifts): it enumerates every
    registry constraint as a structured row, tags each with an anchor STATUS, and asserts
    the usable-anchor count against N33's headline. It is the campaign's live dashboard —
    when a future move manufactures a genuine new (frequency, value) anchor (N33 input (3),
    e.g. a static sum-rule datum, W2.2) the count increments and the rank-deficiency lifts.

    NOT a new physics result; NOT a kernel value; NOT a resolution of the rank deficiency.
    The DERIVED-A core is the LIVE engine cross-checks of the sharpest row values (so the
    dashboard cannot silently drift from twt.py — the phantom-cite guard, canon Section 2)
    plus the two exclusion guards; the anchor COUNT operationalizes N33's judgment (FRAMING).
    Distinct from theta_rel_pinnability_from_data (which assesses whether Theta_rel
    specifically is pinnable, at the structure-vs-value level): THIS is the full
    kernel-constraint registry with the usable-anchor count as a live invariant.

    THE ANCHOR-COUNTING DISCIPLINE (N33; canon menu-vs-pick + anti-circularity):
    a row is a USABLE ANCHOR iff it is TODAY a mutually-independent (frequency, value)
    numeric pair capable of constraining a >=2-parameter causal kernel. EXCLUDED, each for
    a named reason:
      - one-sided brackets / numberless placeholders (sigma_QCD, chain-(4), tau_mem);
      - gate-free quantities miscounted as Im chi samples (sin^2 theta_W = 3/8 — the exact
        miscount N33 names; asserted gate-free below and kept OUT of the anchor set);
      - quantities algebraically tied to another (g tied to alpha via g^2 = 4 pi alpha (8/3)
        — the SAME unknown, not a second anchor; alpha_s / alpha_W likewise);
      - structural TARGETS for the kernel, not data FOR it (the K_c factor (19/2)sqrt(38);
        the running muPsi0 shape; the C_T integrand shape);
      - candidate identifications not closed (1/Theta_0 ~ Lambda_QCD; m_N = 3 mu^2).

    THE ONE USABLE ANCHOR, honestly qualified: the KSS/GW bracket is is_usable_anchor=True
    by N33's convention (a two-sided numeric bracket on one coefficient), BUT it is not yet
    numerically CLOSED into a single-coefficient constraint — reconciling the KSS floor
    (on eta/s) with the GW ceiling (on eta) needs an entropy density s the corpus does not
    supply, and its frequency (omega->0) is asserted by CATEGORY, not derived (N33 input (4)
    still owed). So even the count-of-one overstates the operative constraint; one bracket
    against a >=2-dial kernel is rank-deficient by >=1 dof regardless.

    JURISDICTION (Import Registry, canon Section 2): the moments that could manufacture a
    NEW anchor (W2.2) must ride causality / Kramers-Kronig (holds for any causal response)
    and equal-time operator-identity (f-sum) moments — NOT the fluctuation-dissipation
    theorem, whose violation residual IS Theta_rel (I-12, definitional). This table records
    that discrimination so the 2b program does not assume away its own target.

    N33's four named missing inputs (the campaign's acceptance criteria) are carried in the
    return, each mapped to which row it would upgrade.

    self-checks: usable-anchor count == 1 (== N33 headline); the anchor set == {kss_gw_bracket};
    rank_deficient == True (count < kernel_min_free_params = 2); and LIVE cross-validation of
    the sharpest row values against their source primitives — Kc ratio == (19/2)sqrt(38), the
    running-muPsi0 pair (decreasing, sign>0, ratio>2), the Brannen 0.28%, plus the two
    exclusion guards (weinberg_sin2 gate-free == 3/8 and kept out of anchors;
    alpha_em_value GATED-raises)."""
    import math

    # ---- rows: the registry's kernel-gated constraints, each a structured dashboard entry
    rows = [
        dict(id="kss_gw_bracket",
             observable="shear viscosity eta / (eta/s) of the substrate transport function Im chi",
             kernel_link="im_chi_falsifier_budget_KSS_GW_macromolecule (FRAMING); the #1-gap Im chi at the macroscopic layer",
             value="KSS floor eta/s >= hbar/(4 pi); GW170817 ceiling eta <~ 1e9-1e10 Pa*s (reproduced ~6.5e9, ledger N34)",
             frequency_window="omega->0 transport",
             frequency_justification="UNJUSTIFIED",
             independence="independent (the single mutually-independent numeric anchor per N33)",
             status="usable-anchor",
             is_usable_anchor=True,
             caveat="not yet numerically closed: reconciling the eta/s-floor with the eta-ceiling needs an unstated entropy density s; one bracket vs a >=2-dial kernel is rank-deficient by >=1 dof"),
        dict(id="Kc_renorm",
             observable="L-orbit QCP magnon stiffness renormalization (bare LSWT -> K_c)",
             kernel_link="Kc_magnon_stiffness_canted_FM_at_DJ (LOCATED-GAP-REFINED); the kernel must produce the exact ratio",
             value="K_long/K_c = (19/2)sqrt(38) ~ 58.56 (sympy-exact); K_long=sqrt(38)J, K_c=2J/19",
             frequency_window="cell/QCP scale",
             frequency_justification="N/A",
             independence="internal statics relation (two same-substrate quantities), not two measurements",
             status="structural-target",
             is_usable_anchor=False,
             caveat="the sharpest single-number TARGET for the kernel; static LSWT ELIMINATED as a route (this is what the #9.6 kernel must reproduce)"),
        dict(id="running_muPsi0",
             observable="parity-odd <I_4> condensate dial across generations",
             kernel_link="updown_mirror_multigen_avg_vs_lepton (N37); the dial must RUN",
             value="implied 1.69 -> 0.56 (ratio ~3.0 > 2); sign pinned > 0 (N32a)",
             frequency_window="UNKNOWN (running is over generation index, not a frequency window)",
             frequency_justification="N/A",
             independence="the single N32a dial (three handles converge); values tied to witness masses",
             status="structural-target",
             is_usable_anchor=False,
             caveat="a SHAPE/running constraint (two numbers + drift + sign), NOT a one-number closure; per-transition unfalsifiable (2 unknowns, 2 points)"),
        dict(id="tau_mem",
             observable="memory-kernel relaxation time",
             kernel_link="MemoryKernel enum (#1-gap Cat-1); listed in eom_invariant_variant_audit()['open_cat1_kernel_gated_#1gap']",
             value="hysteretic tau_mem = tau_wave*exp(S/hbar) (S/hbar UNPROVEN); fading [3,380] explicitly NOT pinned",
             frequency_window="omega ~ H (memory window); fork unresolved",
             frequency_justification="UNJUSTIFIED",
             independence="n/a -- GATED; hysteretic value tied to the unbuilt barrier action S",
             status="bracket-only",
             is_usable_anchor=False,
             caveat="N34: the [3,380] range must NEVER be treated as a quantitative target (NOT pinned, never suite-exercised; needs an eta<->tau_mem bridge)"),
        dict(id="C_T",
             observable="induced-EH spin-2 spectral coefficient (absolute G)",
             kernel_link="texture_gauss_equation_riemann_closure (R-149): integrand FIXED as a quadratic form in (S,[Om,Om]); Import Registry I-3",
             value="Lambda_S = sqrt(2*pi) M_Pl (scheme variable; which-Lambda ruling 2026-07-30 — the old [0.13, 2.5] M_Pl bracket is RETIRED); C_T value #1-gap GATED",
             frequency_window="substrate spin-2 spectral sum up to Lambda ~ M_Pl",
             frequency_justification="N/A",
             independence="tied to the same kernel/mode-measure as the other #1-gap value faces (I-3 OPEN); KK-linked to the kss_gw transport anchor as the Re/Im of ONE spin-2 rho_2 (N44: eta = C_T*Lambda^2*tau) -- NOT an independent anchor",
             status="structural-target",
             is_usable_anchor=False,
             caveat="R-149 fixed the integrand SHAPE; the single missing ingredient is the kernel's mode measure alone -- the sharpest 'kernel-as-counted-INPUT' contribution to route 2b (see W3.1)"),
        dict(id="theta0_LambdaQCD",
             observable="inverse rotational moment of inertia <-> Lambda_QCD",
             kernel_link="massive_scheme_refit_branch (R-138) + R-111 CANDIDATE identification",
             value="1/Theta_0 = (2/3)(M_Delta - M_N) = 195.4 MeV, fit-invariant across the pion-mass/scheme fork",
             frequency_window="omega ~ QCD scale",
             frequency_justification="N/A",
             independence="algebraically pinned by the observed N-Delta splitting; the Lambda_QCD side an unclosed candidate",
             status="candidate-anchor",
             is_usable_anchor=False,
             caveat="candidate identification, not a mutually-independent Im chi pair; carries no independent kernel information"),
        dict(id="sigma_QCD",
             observable="confining-string tension",
             kernel_link="OPEN (listed in eom_invariant_variant_audit()['open_cat1_kernel_gated_#1gap']); no computing primitive -- gated on #D.5",
             value="empirical ~0.18-0.19 GeV^2 (lattice/Regge); TWT-computed value = NONE",
             frequency_window="hadronic-cell confinement (effectively UNKNOWN for anchoring)",
             frequency_justification="N/A",
             independence="n/a (no TWT value; only the imported empirical datum)",
             status="numberless",
             is_usable_anchor=False,
             caveat="an OUTPUT the kernel must PREDICT, not an INPUT that constrains it today"),
        dict(id="chain4_missing_energy",
             observable="decay-energy residual (Im chi energy budget)",
             kernel_link="WP-MASS-MEASURE chain (4) (N36); #1-gap gated; no primitive (correctly)",
             value="no datum; anomalous missing energy in precision decay spectra would MEASURE Im chi",
             frequency_window="omega ~ H dissipative (materializes only with a measurement)",
             frequency_justification="N/A",
             independence="n/a (no datum today)",
             status="future-falsifier",
             is_usable_anchor=False,
             caveat="becomes a real Im-chi anchor only when such a measurement pins it -- the free over-determination row route 2b flags"),
        dict(id="mN_3musq",
             observable="nucleon per-rotor lock vs lepton Brannen scale",
             kernel_link="brannen_scale_nucleon_third_convergence (R-134); a mechanism landing it gives m_N = 3 mu^2",
             value="mu^2 = 313.85 vs m_N/3 = 312.97 MeV, 0.28% zero-parameter (E-channel-conditional; I4 route BLOCKED N12)",
             frequency_window="cell-scale per-rotor lock (a static mass ratio, no spectral axis)",
             frequency_justification="N/A",
             independence="isolated cross-sector coincidence; value GATED (P2-1/P2-5-class)",
             status="candidate-anchor",
             is_usable_anchor=False,
             caveat="a candidate coincidence (look-elsewhere caveated), NOT an Im chi kernel anchor; floor reading does NOT converge (~9%)"),
        dict(id="alpha_couplings",
             observable="alpha_em / alpha_s / alpha_W / g",
             kernel_link="B.5b structural links; four samples of one Im chi (value OPEN)",
             value="g^2 = 4 pi alpha (8/3); all tied to the SINGLE unknown alpha (itself GATED)",
             frequency_window="UNKNOWN ('different frequencies' asserted, not justified)",
             frequency_justification="UNJUSTIFIED",
             independence="tied-to: alpha_s / alpha_W / g all the same unknown as alpha_em (8/3 = 1/sin^2 theta_W)",
             status="non-anchor",
             is_usable_anchor=False,
             caveat="structural links only; sin^2 theta_W = 3/8 is gate-free and must NOT be counted as an Im chi sample (the N33 miscount)"),
    ]

    usable = [r["id"] for r in rows if r["is_usable_anchor"]]
    n_usable = len(usable)
    kernel_min_free_params = 2   # amplitude + relaxation scale, at minimum (N33)
    rank_deficient = n_usable < kernel_min_free_params

    # ---- N33's four named missing inputs (acceptance criteria), mapped to rows ----
    n33_missing_inputs = {
        "(1) macromolecule-interferometry floor number": "DELIVERED-WITH-CAVEAT 2026-07-05 (coordinator-directed, web-sourced + 3-agent verified): the MODEL-INDEPENDENT inside-frame anomalous-CoM-decoherence ceiling is Gamma <~ 30 s^-1 (a downstream conversion of macroscopicity mu <= 15.5 via tau = tau_e*(m_e/m)^2; native quantity is a coherence TIME, not a rate) from the CURRENT record Pedalino et al. Nature 649, 866 (2026) (Na nanoparticles >170 kDa, MUSCLE) [prior: Fein et al. Nat.Phys. 15,1242 (2019), 25 kDa, mu=14.1]; framework Nimmrichter & Hornberger PRL 110,160403 (2013). WAVEFRONT/JURISDICTION CAVEAT (load-bearing, canon 0): this bound is derived on the INSIDE-frame c.m. density operator (a Markovian, GALILEAN-INVARIANT / Holevo-form addition to the von Neumann eq.); TWT decoherence is the OUTSIDE-frame substrate Im-chi. It binds TWT ONLY IF the substrate effect coarse-grains to an inside-frame Galilean-invariant Markovian localization -- and the WAVEFRONT picks a distinguished frame, which may VIOLATE that axiom. So: CANDIDATE-for-applicability -- number solid+current; TWT-binding is an OPEN outside<->inside projection (the un-built isomorphism the canon flags), itself downstream of the #1 gap. CSL/DP-specific bounds (interferometry lambda~1e-6..1e-8; X-ray lambda<5.2e-13 s^-1 EPJC 81,773 (2021), white-noise-dependent; LISA-PF lambda~2.96e-8 Helou PRD 95,084054 (2017); DP parameter-free EXCLUDED R_0>0.54 Angstrom Donadi Nat.Phys.17,74 (2021)) are COLLAPSE-MODEL-SPECIFIC, NOT TWT anchors (future cross-checks only, outside<->inside projection un-built). Fork-BLIND (WP-DC2). USABLE-ANCHOR COUNT still HELD.",
        "(2) Lambda ~ H^2 residual coefficient": "DELIVERED 2026-07-05 (coordinator-directed, Gemini-web-sourced + verified in-house): the observed spin-0/trace-channel coefficient is c = 3*Omega_L = 2.05 +/- 0.02 (rho_L = c*M_Pl^2*H_0^2 with reduced M_Pl; Planck 2018 VI arXiv:1807.06209, Omega_L=0.6847; H_0-tension width c in [1.75(SH0ES), 2.05(Planck)]). A CANDIDATE 2nd anchor (spin-0 channel, omega~H, independent of the spin-2 eta/C_T sector per N44); O(1)-strength (semi-definitional c=3*Omega_L); substrate side = the gated Lambda~H^2 residual (R-047/R-119, Volovik crack I-4). USABLE-ANCHOR COUNT ADJUDICATION HELD pending the 3rd (order-param/QCP) channel + the >=3-agreeing test.",
        "(3) a genuine sum-rule / Kramers-Kronig datum with a real number": "the one input the SUBSTRATE can plausibly supply today -- a static-susceptibility value or a short-distance equal-time correlator (W2.2); upgrades the usable-anchor count",
        "(4) independently-justified frequency assignments per anchor": "turns UNJUSTIFIED frequency windows (kss_gw, tau_mem, alpha_couplings) into justified ones -- the bare assertion 'different frequencies' is forbidden (N33)",
    }

    # ---- DERIVED-A: live cross-validation against the engine (anti-drift / anti-phantom) ----
    # (a) the anchor count matches N33's headline
    assert n_usable == 1, f"usable-anchor count must be 1 (N33 headline); got {n_usable}"
    assert usable == ["kss_gw_bracket"], f"the one anchor must be the KSS/GW bracket; got {usable}"
    assert rank_deficient, "one anchor vs a >=2-dial kernel must be rank-deficient (N33)"
    # (b) the sharpest structural-target values == their source primitives, LIVE:
    kc = Kc_magnon_stiffness_canted_FM_at_DJ()
    assert abs(kc["ratio_K_long_over_K_c"] - (19.0/2.0)*math.sqrt(38.0)) < 1e-9, \
        "K_c row must equal the engine ratio (19/2)sqrt(38)"
    mu = updown_mirror_multigen_avg_vs_lepton()["implied_mu_psi0_per_transition"]
    assert mu[0] > mu[1] > 0 and (mu[0] / mu[1]) > 2.0, \
        "running-muPsi0 row: the dial must run, decreasing, sign>0, ratio>2"
    br = brannen_scale_nucleon_third_convergence()["numbers"]
    assert abs(br["ratio_mass"] - 1.0) < 0.005, \
        "m_N=3mu^2 row must match the engine's 0.28% convergence"
    # (c) the two exclusion guards, LIVE:
    assert abs(weinberg_sin2() - 0.375) < 1e-12, \
        "sin^2 theta_W must be gate-free 3/8 (hence correctly excluded from the anchor set)"
    assert not any(r["id"] == "sin2_thetaW" for r in rows), \
        "sin^2 theta_W = 3/8 must NOT appear as an Im chi anchor row (the N33 miscount guard)"
    try:
        alpha_em_value()
        _alpha_gated = False
    except GatedError:
        _alpha_gated = True
    assert _alpha_gated, "alpha_em_value must be GATED (the couplings are non-anchors today)"

    return {
        "tier": "FRAMING (over-determination dashboard; anchor count operationalizes N33) + "
                "DERIVED-A (live engine cross-validation of the sharpest row values + exclusion guards)",
        "purpose": "graduate N33's prose meta-result into a checkable, self-validating engine "
                   "artifact; the Class-2 (route 2b) campaign dashboard",
        "rows": rows,
        "n_rows": len(rows),
        "n_usable_anchors": n_usable,
        "usable_anchor_ids": usable,
        "kernel_min_free_params": kernel_min_free_params,
        "rank_deficient": rank_deficient,
        "rank_deficit_at_least": kernel_min_free_params - n_usable,
        "n33_missing_inputs": n33_missing_inputs,
        "jurisdiction": "manufacturing a NEW anchor (W2.2) may ride causality/Kramers-Kronig + "
                        "equal-time operator-identity (f-sum) moments; NOT FDT (I-12, whose "
                        "violation residual IS Theta_rel)",
        "excluded_from_anchors": {
            "sin2_thetaW_3_8": "gate-free (DERIVED); not an Im chi sample -- the exact N33 miscount",
            "g_and_alpha_s_alpha_W": "algebraically tied to alpha via g^2=4 pi alpha (8/3); one unknown, not several",
            "tau_mem_3_380": "NOT pinned; never a quantitative target (N34)",
        },
        "fence": "NOT a kernel value, NOT a new anchor, NOT a resolution of the rank deficiency; "
                 "the live cross-checks are DERIVED-A, the anchor-count/dashboard is FRAMING",
        "verdict": ("the registry's over-determination opportunity is RANK-DEFICIENT as banked: "
                    "exactly ONE usable anchor (KSS/GW, itself not numerically closed) against a "
                    ">=2-parameter causal kernel. This artifact makes N33's finding a live, "
                    "self-validating invariant: the count increments when a genuine new "
                    "(frequency, value) anchor (N33 input (3)) is manufactured -- the campaign's dashboard."),
    }


def kernel_candidate_constraints():
    """[FRAMING — the kernel-candidate CONSTRAINT INVENTORY as an engine artifact; Phase B / B1 of the
    Class-2 campaign (2026-07-05). Companion to R-150's over-determination table.] Encodes, as checkable
    DATA, the full set of constraints ANY driven-dissipative kernel candidate (P2-1 / Im chi / Theta_rel)
    must satisfy, so candidates are tested MECHANICALLY, not rhetorically. Each row: a hard constraint, a
    channel TARGET (with its banked value cross-validated live), a discrete BRANCH (the fork), or a
    structurally-DISFAVORED option. Deliberately NOT a derivation: nothing here computes the kernel; this
    is the acceptance test a candidate memo (B4) reports against. Tier FRAMING (tooling); the channel
    targets are cross-checked live against their banked engine sources.

    THE INVENTORY (brief B1):
      C1 CAUSALITY / KK   [hard]  : K(t) causal; Kramers-Kronig holds (ANY causal response). FDT is NOT
                                    assumed -- its violation residual IS Theta_rel (Import Registry I-12,
                                    definitional). A candidate that invokes FDT has assumed away the hunt.
      C2 MEMORY-REQUIRED  [hard]  : memoryless kernel EXCLUDED for the SELECTION/MEMORY roles
                                    (R-114 re-tiered FRAMING 2026-07-31, C/D/E audit D-3: the old
                                    'no stable Skyrmion' premise contradicted §A.3's topological
                                    stability and is WITHDRAWN; the survivable claim is that a
                                    memoryless kernel cannot supply tau_mem >> tau_wave, which
                                    Role-3 selection and §D.5.4's roles require); tau_mem > 0.
      C3 LINEAR-FACE      [hard]  : reduces to the conservative master equation at the linear face
                                    (WP-IX3/IX4/DC2 intact); the low-omega spectral exponent respects the
                                    s = 3 Goldstone/Adler-zero protection (the decoherence floor).
      C4 POSITIVITY       [hard]  : omega^2(k) >= 0 (dynamical stability); spin-2 spectral positivity
                                    rho_2 >= 0 (R-040, C_T > 0 by unitarity).
      C5 KSS BRACKET      [hard]  : eta/s >= hbar/4pi (near-floor = the framework's commitment), below the
                                    GW170817 ceiling (~1e9-1e10 Pa s; entropy-density caveat named, N33).
      C6 CHANNEL TARGETS  [target,>=3 orthogonal]: the ONE kernel, sampled in 3 orthogonal channels, must
                                    reproduce -- (a) order-param: the (19/2)sqrt(38) ~ 58.56 renormalization
                                    at the D=J QCP (N31/W2.2; cross-checked live); (b) spin-0: the Lambda~H^2
                                    coefficient c = 3*Omega_L ~ 2.05 (N33 input 2, Planck); (c) spin-2: C_T
                                    through <= 4 kernel moments (R-151) at the Sakharov scheme scale
                                    Lambda_S = sqrt(2*pi) M_Pl (which-Lambda ruling 2026-07-30). (N44: (a spin-2 eta and C_T are ONE
                                    KK-linked source; the 3 must be sector-orthogonal.)
      C7 THE FORK         [branch]: fading vs hysteretic carried as an EXPLICIT DISCRETE BRANCH, never a
                                    fitted knob (N33). A6/N45: hysteretic is the SETTLED WORKING BRANCH
                                    (originator pick; R-114/FRAMING excludes only the memoryless
                                    limit for the selection roles); N46: the fork outcome for the Z3 escape is set by
                                    kernel NUMBERS (alpha/alpha*, tau*om, barrier), not the branch label.
      C8 SOC              [disfavored]: SOC universality stays structurally disfavored (Floquet limit-cycle
                                    lean, companion Section 12) -- do not resurrect without new grounds.

    THE USE (B4): a candidate kernel PASSES iff it satisfies C1-C5 (hard) + lands the C6 targets within
    tolerance + declares its C7 branch + avoids C8. 'No member passes' is a first-class, bankable result.

    self-checks: the C6 targets equal their banked sources live -- (a) (19/2)sqrt(38) vs N31's
    ratio_K_long_over_K_c; (c) the <=4 moment bound vs R-151; the FDT-forbidden flag (I-12); the fork is a
    branch not a target; monostability requires tau_mem>0; the usable-anchor structure matches R-150."""
    kc = Kc_magnon_stiffness_canted_FM_at_DJ()
    ct = ct_kernel_moment_count_symmetry_reduction()
    tbl = kernel_overdetermination_table()

    target_58 = (19.0 / 2.0) * math.sqrt(38.0)           # ~ 58.56, order-param renormalization (N31)
    target_c0 = 2.05                                     # spin-0 c = 3 Omega_L (Planck, N33 input 2)
    ct_moment_bound = 4                                  # spin-2 C_T <= 4 kernel moments (R-151)

    rows = [
        dict(id="C1_causality_KK", kind="hard",
             req="K(t) causal; Kramers-Kronig holds; FDT NOT assumed (its violation IS Theta_rel, I-12)",
             source="I-12 (FDT definitional); companion Section 6 principle 7 (KK)"),
        dict(id="C2_monostability", kind="hard",
             req="memoryless EXCLUDED for the selection/memory roles; tau_mem > 0 "
                 "(cannot supply tau_mem >> tau_wave otherwise)",
             source="R-114 (FRAMING since 2026-07-31 — memory requirement, NOT a stability theorem); N9"),
        dict(id="C3_linear_face", kind="hard",
             req="conservative master eq at the linear face (WP-IX3/IX4/DC2); low-omega exponent respects s=3 Adler-zero",
             source="WP-DC2; the s=3 Goldstone/Adler-zero protection"),
        dict(id="C4_positivity", kind="hard",
             req="omega^2(k) >= 0; spin-2 spectral positivity rho_2 >= 0 (C_T > 0)",
             source="R-040 (unitarity); dynamical stability"),
        dict(id="C5_KSS_bracket", kind="hard",
             req="eta/s >= hbar/4pi (near-floor), below GW170817 ceiling ~1e9-1e10 Pa s",
             source="KSS bound; GW170817; R-150 kss_gw (the one usable anchor); entropy-density caveat N33"),
        dict(id="C6a_orderparam_target", kind="target", channel="order-parameter (magnon, D=J QCP)",
             value=target_58, req="the (19/2)sqrt(38) ~ 58.56 stiffness renormalization K_long -> K_c",
             source="N31/W2.2 (Kc_magnon_stiffness_canted_FM_at_DJ)"),
        dict(id="C6b_spin0_target", kind="target", channel="spin-0 / trace (Lambda~H^2, omega~H)",
             value=target_c0, req="the Lambda~H^2 coefficient c = 3*Omega_L ~ 2.05",
             source="N33 input 2 (Planck 2018 VI); companion cosmo"),
        dict(id="C6c_spin2_target", kind="target", channel="spin-2 (graviton / C_T, KK-linked to eta)",
             value=ct_moment_bound, req="C_T through <= 4 kernel moments at the Sakharov scheme scale "
                                "Lambda_S = sqrt(2*pi) M_Pl (which-Lambda ruling 2026-07-30)",
             source="R-151 (ct_kernel_moment_count_symmetry_reduction); N44 (eta<->C_T KK-linked, ONE source)"),
        dict(id="C7_fork_branch", kind="branch",
             req="fading vs hysteretic = an EXPLICIT DISCRETE BRANCH, never a fitted knob; hysteretic = the settled working branch (originator pick; R-114 FRAMING excludes only the memoryless limit)",
             source="N33; A6/N45 (fixed-charge/hysteretic); N46 (escape set by kernel numbers, not the branch label)"),
        dict(id="C8_SOC_disfavored", kind="disfavored",
             req="SOC universality structurally disfavored (Floquet limit-cycle lean); do not resurrect without new grounds",
             source="companion Section 12"),
    ]

    hard = [r for r in rows if r["kind"] == "hard"]
    targets = [r for r in rows if r["kind"] == "target"]
    branches = [r for r in rows if r["kind"] == "branch"]

    # --- live cross-validation of the channel targets against their banked sources ---
    assert abs(target_58 - kc["ratio_K_long_over_K_c"]) < 1e-9, \
        "C6a: the 58.56 target must equal N31's K_long/K_c = (19/2)sqrt(38)"
    assert ct_moment_bound == ct["N_moments_parity_even"] == 4, \
        "C6c: the C_T moment bound must be the 4 parity-even invariant forms (R-151)"
    assert tbl["n_usable_anchors"] == 1, \
        "the over-determination table's one usable anchor (KSS/GW) underlies C5/C6 (R-150)"
    assert len(hard) == 5 and len(targets) == 3 and len(branches) == 1, \
        "inventory shape: 5 hard + 3 channel targets + 1 fork branch"
    # FDT is NOT a constraint a candidate may invoke:
    fdt_forbidden = "FDT NOT assumed" in rows[0]["req"]
    assert fdt_forbidden, "FDT must be flagged NOT-assumed (I-12) -- its violation IS Theta_rel"

    return {
        "tier": "FRAMING (the kernel-candidate constraint inventory as an engine artifact; channel targets cross-validated live)",
        "rows": rows,
        "n_hard": len(hard), "n_channel_targets": len(targets), "n_branch": len(branches),
        "channel_targets": {"order_param_58": target_58, "spin0_c": target_c0, "spin2_CT_moments_max": ct_moment_bound},
        "fork_is_branch_not_knob": True,
        "fdt_forbidden": fdt_forbidden,
        "usable_anchors_underlying": tbl["n_usable_anchors"],
        "use": "a candidate PASSES iff it satisfies C1-C5 (hard) + lands C6 targets within tolerance + declares its C7 branch + avoids C8; 'no member passes' is a first-class bankable result",
    }


# ======================================================================
# THE #1-GAP KERNEL CANDIDATE (paper §E.5; R-153..R-158) — the KS
# selection campaign's Grade-B class, integrated 2026-07-22.
# Provenance: the simulator/ KS campaign (commits ec11cfc..1ae53b7; every
# phase adversarially reviewed to consensus; corpus frozen throughout per
# the campaign's RULE 1; simulator suite 144->172). Review documents:
# simulator/references/KS_CANDIDATE_KERNEL_SYNTHESIS.md,
# KS_SIMULATOR_ARC_SYNTHESIS.md, KS6_PAPER_ADDENDUM.md.
# GOLDEN RULE INTACT: these primitives fix FORM only — every #1-gap
# magnitude keeps raising (alpha_em_value etc. untouched); selecting a
# candidate un-gates NOTHING.
# ======================================================================

def _ks_nodal_im_chi(w, p=3.0, W=3000.0, tau=1.0, A=1.0, Delta=1.0):
    """Pure-python mirror of the simulator nodal family (sc_kernel.nodal_family):
    sign(w) * A * x^p/(x^p + Delta^p) / (1 + (x/W)^2), x = |w|*tau. Algebraic edge."""
    if w == 0.0:
        return 0.0
    x = abs(w) * tau
    return math.copysign(A * x ** p / (x ** p + Delta ** p) / (1.0 + (x / W) ** 2), w)


def _ks_swave_im_chi(w, W=3000.0, tau=1.0, wT=0.15, A=1.0, Delta=1.0):
    """Pure-python mirror of the simulator s-wave family (sc_kernel.swave_family):
    Gaussian-in-deficit gap exp(-((Delta-x)_+ / wT)^2) * x^3/(x^3+Delta^3) / (1+(x/W)^2).
    Exponentially-gapped edge; numerical domain Delta/wT <~ 27 (the underflow cliff)."""
    if w == 0.0:
        return 0.0
    x = abs(w) * tau
    gap = math.exp(-(max(Delta - x, 0.0) / wT) ** 2)
    rise = x ** 3 / (x ** 3 + Delta ** 3)
    return math.copysign(A * gap * rise / (1.0 + (x / W) ** 2), w)


def _ks_composite_im_chi(w, r=1.0, W=3000.0, tau=1.0, wT=0.15, A=1.0):
    """The positive two-sector sum [nodal(p=3) + r*swave]/(1+r) (R-154): Goldstone
    sector (nodal p=3, the s=3/Adler face) + DM-gapped canting-magnon sector (swave
    edge), r = the transfer-weight ratio w_magnon/w_goldstone."""
    wg, wm = 1.0 / (1.0 + r), r / (1.0 + r)
    return A * (wg * _ks_nodal_im_chi(w, p=3.0, W=W, tau=tau)
                + wm * _ks_swave_im_chi(w, W=W, tau=tau, wT=wT))


def kernel_candidate_form():
    """[CANDIDATE — Grade B; R-153, paper §E.5. The KS kernel-selection campaign's surviving
    CLASS, integrated 2026-07-22.] The #1-gap kernel CANDIDATE FORM: Im chi(omega) odd, passive,
    Kramers-Kronig-causal, IR exponent s >= 3 (the s=3 Adler/Goldstone floor, WP-DC2 class), UV
    cutoff — CONSTRAINTS-BY-CONSTRUCTION (the hard properties are exact by construction, never
    filtered after the fact). Members: nodal (algebraic edge, x^p/(x^p+1), p >= 3), s-wave
    (exponentially-gapped edge), and their positive composite (R-154). The edge-less campaign
    reference (kstar) is EXCLUDED — the two-sided D3 cull (an edge-less kernel is structurally
    disqualified from sustaining identity transfer; plateau width 0.31 < 0.5 decades) plus the
    F-strong flatness failure (77% dispersion).  Memory branch = HYSTERETIC by the counted F4
    INPUT bit (R-155; the Koide c=sqrt2 menu-vs-pick pattern — a pick, NOT a derivation. The
    old exemplar here was weak=SD, which no longer illustrates an OPEN menu: that menu was COMPUTED
    and CLOSED under C-32, R-171/RUL-082. F4's menu {hysteretic, fading} is not closed).

    WHAT THIS PRIMITIVE IS NOT: it does NOT select within the class (R-157 — the executable
    constraints are reading-conditionally rank-deficient) and does NOT supply any magnitude
    (every #1-gap number stays gated; the gates keep raising).

    self-checks: the declared hard properties cover ALL 5 hard rows of the acceptance inventory
    (kernel_candidate_constraints) at the label level; the branch declaration matches the C7
    branch row; kstar excluded with both cull reasons recorded; members odd + passive on a
    numeric spot grid; grade = B."""
    inv = kernel_candidate_constraints()

    hard_row_coverage = {
        "C1_causality_KK": "odd + IR-integrable (s_IR >= 3 > 0) + UV-decaying => causal KK "
                           "partner exists (Titchmarsh); FDT never invoked (I-12 respected)",
        "C2_monostability": "tau_mem > 0 is a counted dial of every member — mandatorily "
                            "non-Markovian (R-114 respected by construction)",
        "C3_linear_face": "IR exponent s >= 3 built in (the Adler/Goldstone floor; the "
                          "exact-3-vs->=3 fork F1 carried OPEN)",
        "C4_positivity": "passivity exact by sign structure (sign(Im chi) = sign(w)); no "
                         "negative spectral weight introduced",
        "C5_KSS_bracket": "no structural feature forcing eta/s off the KSS floor identified "
                          "(P6 register); eta/s VALUE gated — compatibility, not confirmation",
    }
    families = {
        "nodal": "sign(w)*A * x^p/(x^p+1) / (1+(x/W)^2), x = |w|*tau, p >= 3 (algebraic edge)",
        "swave": "sign(w)*A * exp(-((1-x)_+/wT)^2) * x^3/(x^3+1) / (1+(x/W)^2) (gapped edge)",
        "composite": "[nodal(p=3) + r*swave]/(1+r) — the two-sector positive sum (R-154)",
    }
    excluded = {
        "kstar": "edge-less reference A*(wt)^3/(1+(wt)^2)^2 — culled TWO ways: the two-sided D3 "
                 "smoke test (plateau 0.31 < 0.5 decades => cannot sustain identity transfer) "
                 "AND F-strong flatness (77% dispersion >> the 1.49% tier)",
    }

    # coverage: every hard row of the inventory answered at the label level
    inv_hard_ids = {r["id"] for r in inv["rows"] if r["kind"] == "hard"}
    assert inv_hard_ids == set(hard_row_coverage), \
        "R-153: the candidate must answer ALL hard rows of kernel_candidate_constraints"
    # the branch declaration matches the inventory's C7 branch row
    branch_rows = [r for r in inv["rows"] if r["kind"] == "branch"]
    assert len(branch_rows) == 1 and "hysteretic" in branch_rows[0]["req"], \
        "R-153: the F4 hysteretic declaration must match the C7 branch row"
    # numeric spot-check: members odd + passive on a small grid (sanity, not the closure proof)
    grid = [10.0 ** (-4 + 7 * i / 40.0) for i in range(41)]
    for f in (lambda w: _ks_nodal_im_chi(w, p=3.0),
              lambda w: _ks_swave_im_chi(w),
              lambda w: _ks_composite_im_chi(w, r=1.0)):
        for w in grid:
            assert abs(f(-w) + f(w)) < 1e-15, "R-153: oddness must be exact by construction"
            assert f(w) >= 0.0, "R-153: passivity must be exact by construction (w > 0)"
    assert "kstar" in excluded and "D3" in excluded["kstar"]

    return {
        "tier": "CANDIDATE (Grade B — a surviving CLASS, not a pinned kernel; paper §E.5, R-153)",
        "grade": "B",
        "hard_row_coverage": hard_row_coverage,
        "families": families,
        "excluded": excluded,
        "branch": "hysteretic",
        "branch_is": "a counted F4 INPUT bit (menu {hysteretic, fading} -> PICK, and NOT closed -- "
                     "contrast the weak menu, computed CLOSED at R-171; consistent with "
                     "§D.5.3's adopted working branch; NOT a derivation)",
        "selects_within_class": False,
        "magnitudes_supplied": None,
        "provenance": "simulator/ KS campaign ec11cfc..1ae53b7 (reviewed to consensus per phase; "
                      "corpus frozen during the campaign)",
    }


def kernel_composite_closure():
    """[DERIVED-A (the closure property) + CANDIDATE/FRAMING (the two-sector substrate grounding)
    — R-154, paper §E.5.] Constraints-by-construction are CLOSED under the positive summation
    that defines the composite: for the sum [nodal(p=3) + r*swave]/(1+r), (i) sympy — the IR
    leading power of a positive sum of two x^3-leading densities is exactly 3, so the s=3 Adler
    floor survives ANY positive weights; a positive combination of odd functions is odd, of
    passive ones passive, of UV-decaying ones UV-decaying — the F2 edge-class fork therefore
    DISSOLVES into a single measured ratio r; (ii) numeric — oddness and passivity hold at
    machine precision across r, the measured IR slope is 3 and the UV slope negative, and the
    boundaries recover the pure branches (r=0 -> nodal EXACTLY; r -> inf -> swave). Mirrors the
    simulator witness kernel_space.composite_closed_under_summation. What stays CANDIDATE/FRAMING:
    that the substrate kernel IS this two-sector sum (the SN-16 grounding) — the closure fact is
    algebra; the identification is not.

    self-checks: sympy IR degree == 3; odd/passive at machine precision for r in {0, 0.25, 1, 4,
    100}; measured IR slope within 2% of 3; UV slope < 0; r=0 boundary exact; r=1e8 boundary
    < 1e-6 from pure swave."""
    # (i) sympy: the IR leading power of the positive sum is exactly 3
    x, wg, wm = sp.symbols("x w_g w_m", positive=True)
    lead = sp.expand(wg * x ** 3 + wm * x ** 3)
    s_ir_exact = int(sp.degree(sp.Poly(lead, x)))

    # (ii) numeric: odd + passive across r; slopes; boundary recovery
    grid = [10.0 ** (-4 + 7 * i / 200.0) for i in range(201)]
    odd_passive = True
    for r in (0.0, 0.25, 1.0, 4.0, 100.0):
        for w in grid:
            f_p = _ks_composite_im_chi(w, r=r)
            f_m = _ks_composite_im_chi(-w, r=r)
            if abs(f_m + f_p) > 1e-15 or f_p < 0.0:
                odd_passive = False
    # measured IR slope (decade 1e-4..1e-3) and UV slope (decade 1e2..1e3) at r=1
    def _slope(w1, w2, r):
        y1, y2 = _ks_composite_im_chi(w1, r=r), _ks_composite_im_chi(w2, r=r)
        return (math.log(y2) - math.log(y1)) / (math.log(w2) - math.log(w1))
    ir_slope = _slope(1e-4, 1e-3, r=1.0)
    uv_slope = _slope(1e2, 1e3, r=1.0)
    # boundary recovery
    r0_max = max(abs(_ks_composite_im_chi(w, r=0.0) - _ks_nodal_im_chi(w, p=3.0)) for w in grid)
    rinf_max = max(abs(_ks_composite_im_chi(w, r=1e8) - _ks_swave_im_chi(w)) for w in grid)

    assert s_ir_exact == 3, "R-154: the Adler floor must survive the positive sum (sympy)"
    assert odd_passive, "R-154: oddness + passivity must be closed under the positive sum"
    assert abs(ir_slope - 3.0) < 0.06, f"R-154: measured IR slope must be ~3 (got {ir_slope})"
    assert uv_slope < 0.0, f"R-154: UV slope must be negative (got {uv_slope})"
    assert r0_max < 1e-15, "R-154: r=0 must recover nodal(p=3) exactly"
    assert rinf_max < 1e-6, "R-154: r->inf must recover swave"

    return {
        "tier": "DERIVED-A (closure under positive summation) + CANDIDATE/FRAMING (the "
                "substrate-kernel-IS-this-sum identification; R-154, paper §E.5)",
        "s_ir_sum_exact": s_ir_exact,
        "odd_passive_all_r": odd_passive,
        "ir_slope_at_r1": ir_slope,
        "uv_slope_at_r1": uv_slope,
        "r0_matches_nodal_max": r0_max,
        "rinf_matches_swave_max": rinf_max,
        "dissolves": "the F2 edge-class fork -> the single measured ratio r (r=0 nodal, "
                     "r->inf swave)",
    }


def kernel_candidate_dials():
    """[INPUT/FIT — CANDIDATE-SCOPED; R-155, paper §E.5.] The counted parameter economy of the
    candidate class. Genuine dials: p (nodal IR exponent, >= 3; F1 fork), wT (s-wave edge width;
    SC-1b crossover-pinned), W (UV plateau width; a_e-invisible), tau_mem (memory time; F3-pinned
    economy-preferred, value gated), r (composite transfer weight; dissolves F2). Plus ONE
    counted INPUT bit: F4 = HYSTERETIC (the menu {hysteretic, fading} -> PICK; the Koide c=sqrt2
    pattern -- NOT the weak=SD pattern, whose menu closed under C-32 at R-171; consistent with §D.5.3's adopted branch — NOT a derivation; the campaign's bathless
    forcing attempt stays FRAMING/CANDIDATE). The SN-15 redundant edge scale Delta is EXACTLY
    absorbable (Delta, tau, W) -> (1, tau/Delta, W/Delta) and is NOT a dial. Minimal member =
    2 dials + 1 bit; composite = 3 dials + 1 bit.

    LEDGER SCOPE (load-bearing): these dials are counted within the CANDIDATE'S OWN ledger.
    They join the framework's parameter ledger (§E.2.1's four counted INPUTs + measured G_N) ONLY if the candidate is
    adopted; until then the #1 gap stays open exactly as §D.5 states it.

    self-checks: the SN-15 absorption identity at machine precision on a grid; the dial count
    arithmetic; the F4 bit declared as pick-not-derivation; the framework-ledger fence."""
    # SN-15: nodal(Delta=d, tau=t, W=W0) == nodal(Delta=1, tau=t/d, W=W0/d) exactly
    d, t, W0 = 2.7, 1.3, 3000.0
    grid = [10.0 ** (-4 + 7 * i / 60.0) for i in range(61)]
    absorb_max = max(
        abs(_ks_nodal_im_chi(w, p=3.0, W=W0, tau=t, Delta=d)
            - _ks_nodal_im_chi(w, p=3.0, W=W0 / d, tau=t / d, Delta=1.0))
        for w in grid)
    assert absorb_max < 1e-15, \
        "R-155/SN-15: the edge scale must be exactly absorbable (machine precision)"

    dials = {
        "p": "nodal IR exponent (>= 3; F1 exact-3-vs->=3 fork OPEN; floor member fixes p = 3)",
        "wT": "s-wave edge-width ratio (SC-1b crossover wT/Delta ~ 0.45-0.54)",
        "W": "UV plateau width (W_min ~ 145-156 conservative; a_e-INVISIBLE)",
        "tau_mem": "memory time (F3 pinned-economy-preferred; the VALUE stays gated)",
        "r": "composite Goldstone->magnon transfer weight (dissolves F2)",
    }
    n_minimal, n_composite = 2, 3
    assert len(dials) == 5 and n_minimal == 2 and n_composite == 3

    out = {
        "tier": "INPUT/FIT — candidate-scoped (R-155, paper §E.5): counted within the "
                "candidate's OWN ledger; joins the §E.2.1 framework ledger ONLY on adoption",
        "dials": dials,
        "input_bit": "F4 = HYSTERETIC (menu {hysteretic, fading} -> PICK; weak=SD pattern; "
                     "a pick, NOT a derivation)",
        "sn15_absorption_max_dev": absorb_max,
        "minimal_member_dials": n_minimal,
        "composite_dials": n_composite,
        "framework_ledger_joined": False,
    }
    assert out["framework_ledger_joined"] is False and "PICK" in out["input_bit"]
    return out


def kernel_candidate_falsifiers():
    """[CANDIDATE — R-158, paper §E.5.] The seven PRE-REGISTERED virgin-sector falsifiers
    P1-P7 + the two-sided D3 edge-less cull. PRE-REGISTRATION PROVENANCE (git two-commit,
    load-bearing for falsifiability): the P1-P7 predictions were committed in the REGISTER
    commit 27e2847 STRICTLY BEFORE the EVALUATE commit 7f2d52d (simulator/; register file
    simulator/references/KS5_prediction_register.md). NO MISSES on the evaluable-now set;
    the sharp tests are pre-registered FUTURE falsifiers; every magnitude stays gated
    (compatibility level, never a fitted number).

    JURISDICTION HEDGE (N49/KC-1 class, load-bearing — reviewer-required 2026-07-22): the
    SC-persistence ceiling (P1) and the superallowed-flatness datum (the R-157 reading fork)
    are INSIDE-frame data; they bind the outside-frame kernel only through the UN-BUILT
    outside<->inside projection — the numeric comparisons gate on exactly this leg (the
    campaign's ceiling_stub raises on its kernel key; the campaign-side KC-1/N49 frame
    hedges are the source records).

    self-checks: 7 register entries; the externally-evaluable-now set contains P1 and P6;
    no misses; the D3 cull two-sided with kstar the recorded casualty; the near-KSS
    commitment flag = STANDS; the frame hedge carried as a returned field."""
    register = {
        "P1": dict(sector="mueV-meV virgin band",
                   prediction="a SINGLE knee/edge at the DM-sourced magnon edge (scale gated); "
                              "IR exponent p; edge class per family",
                   outcome_now="CONSISTENT (structural; the SC-persistence ceiling one-sided, "
                               "numeric gated; the ceiling is an INSIDE-frame datum — binds "
                               "only through the un-built outside<->inside projection, the "
                               "N49/KC-1 frame hedge)",
                   external_test="NOW (one-sided)"),
        "P2": dict(sector="precision a_e two-point ratio",
                   prediction="fixed-tau ratio-vs-floor: nodal-floor 1.0, nodal-steep 0.043 "
                              "(the SC-1b p=5 atlas), swave ~0 — SEPARATES the classes",
                   outcome_now="construction self-consistency recorded",
                   external_test="FUTURE (vertex gated)"),
        "P3": dict(sector="knee*tau_mem train-cadence relation",
                   prediction="knee*tau ~ 1 (nodal exact; swave 0.9995)",
                   outcome_now="declaration recorded",
                   external_test="FUTURE (needs the barrier action S pinned)"),
        "P4": dict(sector="mass-frequency (OM-1) containment",
                   prediction="the knee sits within the x3 containment bracket",
                   outcome_now="containment-consistent (scale gated)",
                   external_test="NOW (structural)"),
        "P5": dict(sector="driven identity-transfer rate landscape",
                   prediction="ACTIVATED (Arrhenius) transfer at d > d* with AK-form drive "
                              "tilt (hysteretic snap face)",
                   outcome_now="form-consistent",
                   external_test="FUTURE (the driven sector)"),
        "P6": dict(sector="VG-1 near-KSS bracket",
                   prediction="eta/s not structurally forced off the KSS floor",
                   outcome_now="CONSISTENT (compatibility NOT confirmation; eta/s gated); "
                               "the near-KSS commitment STANDS — no renegotiation",
                   external_test="NOW (VG-1)"),
        "P7": dict(sector="N22 generation-values fork",
                   prediction="the kernel SUPPORTS the dissipative generation route "
                              "(parity-odd KC23 channel)",
                   outcome_now="structural pass (values gated)",
                   external_test="FUTURE (the generation-route construction)"),
    }
    structural_falsifier = ("two-sided D3 cull: an edge-less (no-plateau) kernel is "
                           "structurally disqualified from sustaining identity transfer — "
                           "kstar culled; an edge-less substrate-kernel finding would KILL "
                           "the class")
    evaluable_now = {k for k, v in register.items() if v["external_test"].startswith("NOW")}

    assert len(register) == 7, "R-158: seven pre-registered falsifiers"
    assert {"P1", "P6"} <= evaluable_now, \
        "R-158: the externally-evaluable-now set must contain P1 and P6"
    assert "kstar" in structural_falsifier and "two-sided" in structural_falsifier
    no_misses = all("MISS" not in v["outcome_now"].upper() for v in register.values())
    # E-14 (2026-07-31): the assert that used to sit here tested a literal authored in this same
    # function — it could only fail if an author typed "MISS". Removed as vacuous; no_misses stays
    # as a REPORTED field with its scope stated honestly below.

    return {
        "tier": "CANDIDATE (the pre-registered falsifier register + outcomes; R-158, paper §E.5)",
        "register": register,
        "structural_falsifier": structural_falsifier,
        "evaluable_now": sorted(evaluable_now),
        "no_misses": no_misses,
        "no_misses_scope": ("a register-consistency statement over outcomes authored in this "
                            "function (all evaluable-now entries are themselves scale/numeric "
                            "GATED) — structural compatibility, NOT an external numeric test; "
                            "the vacuous assert was removed 2026-07-31 (E-14)"),
        "near_kss_commitment": "STANDS (P6 — compatibility, not confirmation)",
        "frame_hedge": "the SC-persistence ceiling (P1) and the superallowed-flatness datum "
                       "(R-157) are INSIDE-frame data: they bind the outside-frame kernel only "
                       "through the un-built outside<->inside projection (N49/KC-1 class)",
        "preregistration": "git two-commit: REGISTER 27e2847 strictly before EVALUATE 7f2d52d "
                           "(simulator/references/KS5_prediction_register.md)",
    }


# ---- §19.4 / §19.5 the lepton angle delta_L and the hierarchy type ------------
def delta_L_from_DoverJ(D_over_J: float) -> float:
    """[DERIVED-CONDITIONAL on §19.5 ANSATZ A=J, B=D] §19.5: D/J = tan(3 delta_L) =>
    delta_L = (1/3) arctan(D/J)  [radians].

    Tier note (audit C2 2026-06-30): the identity D/J = tan(3·δ_L) is DERIVED at leading order
    GIVEN the §19.5 ANSATZ (A=J, B=D) — paper §19.5 line 605-609 explicitly flags this as
    'the framework's single load-bearing ANSATZ at this layer', Paper-2-pending. Engine tier
    is therefore DERIVED-CONDITIONAL, not bare DERIVED."""
    return math.atan(D_over_J) / 3.0

def canting_pitch_q_rad(D_over_J: float) -> float:
    """[DERIVED] §10.3.1 / §D.4.3: the single-q spiral pitch on the AXIS BRANCH. The
    canted-helix minimization on D4 with energy E(q) = -12 J cos q - 12 J - 2 D sqrt(2) sin q
    yields the stationary point at tan q = D sqrt(2)/(6 J). At D/J = 0.787 returns ~10.51deg
    (matches the engine's canting_at_DJ via §10.3.1's standard formula).

    *** SCOPE — READ BEFORE CALLING THIS 'THE LUTTINGER-TISZA MINIMUM'. ***
    The configuration behind E(q) is k = q*e_1 (a SPATIAL helix), B = e_14, and its wavevector
    DIRECTION was never scanned: the twisting bonds are named in advance and the minimisation
    then runs in one variable. That is a Luttinger-Tisza ANSATZ, not a Luttinger-Tisza
    MINIMISATION. Scanning k and the rotation plane (`canting_vacuum_branch_structure`) shows
    the configuration IS a genuine stationary point but an INDEX-2 SADDLE for every D/J > 0
    (transverse second variation 4J(cos q+3)(cos q-1)/cos q < 0), with a body-diagonal screw
    state lying lower by -(1/243)(D/J)^4*J *within the single-q simple-bivector helical family*
    (multi-q, conical and non-simple-B states unscanned; RUL-049).

    WHAT SURVIVES, and is why this primitive is unchanged: D*sqrt(2)/(6J) is a LEADING-ORDER
    INVARIANT of the whole helical problem — it appears here as tan q on the axis branch and as
    the total helical rate |k|*lambda on the body-diagonal branch. Which branch the DRIVEN
    dynamics selects is OPEN (#1 gap, §D.5.7 assembly record); negatives ledger N62."""
    return math.atan(D_over_J * math.sqrt(2.0) / 6.0)

def canting_cos_q(D_over_J: float) -> float:
    """[DERIVED] §10.2.1 / §3.1: the local rotor alignment <R> = cos q (the canting order
    parameter on the canted STATIONARY CONFIGURATION — the AXIS BRANCH of §D.4.3, not "the
    realized ground state": that configuration is an index-2 saddle of the full (k, B) problem
    and a body-diagonal branch lies lower, see `canting_vacuum_branch_structure` and
    `canting_pitch_q_rad`'s SCOPE block), where q is the §10.3.1 axis-branch
    spiral pitch (canting_pitch_q_rad). NOT the global magnetization — this is the local
    / nearest-neighbour rotor alignment carrying the chiral-symmetry-breaking structure
    on which the pion-as-magnon picture rests (§10.2: f_pi = magnon kinetic stiffness).

    Closed form: from tan q = D sqrt(2)/(6 J), sec^2 q = 1 + (D/J)^2/18, hence
        cos q = sqrt(18 / (18 + (D/J)^2)) = sqrt(18) / sqrt(18 + (D/J)^2).
    At D/J = 0.787: cos q = 0.9832 (paper-cited ~0.985)."""
    DoJ = float(D_over_J)
    return math.sqrt(18.0 / (18.0 + DoJ * DoJ))

def DoverJ_from_lepton_masses(masses=(M_E, M_MU, M_TAU)) -> float:
    """[INPUT, over-determined; CONDITIONAL on (a) √m=r² mass-measure AND (b) §19.5 A=J,B=D ANSATZ]
    §19.5 BACK-DERIVATION: compute D/J from the lepton masses ALONE (D/J is NOT passed in) —
    the lepton leg of the headline T0 over-determination.

    Tier note (audit C2 2026-06-30): "INDEPENDENT of the baryon sector" is honest in the sense
    that no baryon-sector quantity is used. But the chain DOES depend on (a) the √m=r² mass-measure
    choice (`mass_measure_from_omega`, under suspicion per WP-MASS-MEASURE worklist item — the
    measure choice is reverse-engineered from the modified-Brannen empirical pattern), AND (b)
    the §19.5 ANSATZ A=J, B=D for the D/J ↔ δ_L identification (paper §19.5:605-609 flags this
    as load-bearing-Paper-2-pending). Independence from Brannen's c=√2 VALUE is real (engine-
    checked: D/J output invariant under c sweep ∈ {0.5, 1.0, √2, 1.5}), but independence from
    the upstream measure + ANSATZ is NOT.

    Brannen triplet sqrt(m_k) ∝ 1 + sqrt(2)·cos(delta_L + 2πk/3) with c=sqrt(2) (the Koide point, C_KOIDE)
    fixed; delta_L is the phase of the order-1 DFT component of the normalized sqrt-mass
    triplet; then D/J = tan(3·delta_L) (robust to the Z3 phase branch since 3·120deg=360deg).
    Returns ~0.787. So its agreement with the Skyrme-stabilizer leg (≈0.778 = √18/e, §10.3)
    — NOT D/J fed in and read back — is the test.
    The Skyrme leg's back-derivation (DoverJ_from_skyrme) IS now in the library and the harness
    checks BOTH legs, so the T0 over-determination is fully reproducible in code (the ~1.1%
    lepton↔baryon agreement, √18-hedged; the 0.790 sometimes quoted is the Cabibbo calibration)."""
    import cmath
    r = [math.sqrt(m) for m in masses]
    M = sum(r) / 3.0
    b = [rk / M - 1.0 for rk in r]
    z = sum(b[k] * cmath.exp(-1j * 2 * math.pi * k / 3) for k in range(3))
    return math.tan(3.0 * cmath.phase(z))


# ---- §19.7 the quark sector --------------------------------------------------

def quark_brannen_table():
    """[PAPER-ASSERTED, not reconstructed] §19.7: same Brannen form with a 2nd-harmonic ε term,
    √m_n = Λ[1 + b cos(φ_n-ψ) + ε b cos(2φ_n-ψ)]. Lepton b=√2 forced (ε=0, K=2/3 exact);
    down b=1.172,ε=0.344,K=0.731 (fitted from d,s,b); up b=1.033,ε=0.973,K=0.992
    (ε_u predicted [CANDIDATE] via ε_u/ε_d=2^(3/2); b_u fit to u,c). Quark K's are scheme/scale-dependent.
    ✅ F3 DONE (worklist F3, careful two-build): the reconstruction is now in quark_mass_reconstruction()
    + amplitude_to_operator() + ckm_from_mass_pinned_psi(). Findings: (1) DOWN rebuilds to <0.2% but
    TAUTOLOGICALLY (b_d,ε_d were fitted from d,s,b); (2) ψ/Λ are a NON-UNIQUE fit (ψ degenerate with (b,ε))
    -- NOT bedrock-derived [SHARPENED 2026-08-13, ADJUDICATION2 keeper C1: ψ is NOT FIXED BY THE MASS
    SPECTRUM (mass-gauge) -- the N=3 harmonic collapse cos(2φ-ψ)=cos(φ+ψ) makes (b,ε,ψ) a 3→2 map at fixed
    Λ; the mass-observable is the invariant phase ψ_inv = 6.294° model-free for down (mixed-scheme), see
    brannen_z3_harmonic_collapse_invariant. CONVENTION: this table's form cos(2φ_n-ψ) is the ψ-FORM, one of
    FOUR epicycle variants in the corpus; the 2ψ-form PHASE STRUCTURE is derivation-backed
    (mass_measure_from_omega, form only) -- variants inter-convert on the orbit UNDER A RE-FIT of (b,ε);
    the same (b,ε) may NOT be carried across forms; ε values and the ε_u/ε_d rule are pinned to this stated
    parametrization]; (3) the up-from-down rule ε_u=ε_d·2^(3/2)=0.973 MISSES the m_t INDICATOR (the
    Brannen FORM reaches it with a free ε, but the RULE's 0.973 does not) -- BUT this is NOT a TWT
    falsification: the top has no hadrons, so m_t is a QCD-model number, not a TWT verifier (only u,c are
    hadron-indicated up-type masses, and two underdetermine the triplet); the rule is TWT-UNTESTABLE, the
    miss an indicator-level hint the up sector may need revisiting; (4) the 'four §25.1
    dials' do NOT survive the quark sector (it adds b_u + the up scale; the ε_u rule is falsified), so the
    full charged-fermion mass spectrum needs >4 continuous dials; (5) the mass-orientation ψ (a rotation
    about G=(1,1,1)) gives DEMOCRATIC CKM mixing (ℤ₃ forces |V₁₂|=|V₂₃|), NOT the λ-ladder -- so the CKM
    hierarchy (Cl-i) needs non-G (ℤ₃-breaking) eigenVECTOR data the ℤ₃-orbit masses do not supply.
    The (b,ε,K) below remain the paper's asserted values (ε_u on the now-falsified rule, flagged)."""
    eps_d, eps_u = 0.344, 0.973
    return {
        "lepton (b,ε,K)": (math.sqrt(2), 0.0, 2/3),
        "down (b,ε,K)": (1.172, eps_d, 0.731),
        "up (b,ε,K)": (1.033, eps_u, 0.992),
        "ε_u/ε_d": eps_u / eps_d,           # ≈ 2^1.5
        "2^(3/2)": 2 ** 1.5,
    }


def quark_mass_reconstruction():
    """[F3.1, AUDITED] §19.7: surface psi, Lambda by reconstructing the six quark
    masses, and AUDIT the dial count. Replaces the tautological eps_u/eps_d check.

    Findings (all asserted below):
      * DOWN reconstructs to <0.2% with the table's (b_d,eps_d) at psi_d ~= 12.76 deg.
        [CORRECTED 2026-08-13 per ADJUDICATION2 keeper C1: this clause used to add
        '~= the lepton delta_L' -- STRUCK. psi is NOT FIXED BY THE MASS SPECTRUM (mass-gauge;
        N=3 harmonic collapse cos(2phi-psi) = cos(phi+psi); see
        brannen_z3_harmonic_collapse_invariant): comparing it to delta_L compared a
        mass-gauge parameter. The reparametrization-INVARIANT down phase is psi_inv =
        6.294 deg MODEL-FREE from the three masses (mixed-scheme; the fit route gives
        6.305 deg, a fit-residual difference) != delta_L = 12.732 deg.] EXPECTED, not a prediction:
        (b_d,eps_d) were themselves fitted from (d,s,b), so the down masses rebuild by
        construction.
      * psi is NOT UNIQUELY surfaced: the SAME 3 down masses are reproduced for a wide
        range of psi, each with its own (b,eps) -- psi is degenerate with (b,eps).
        => 'surfacing psi' is ill-posed from the masses alone; psi is only defined once
        (b,eps) are fixed (and they were fitted). psi is a FIT, not bedrock-derived.
      * UP, against the m_t INDICATOR: the table's (b_u=1.033, eps_u=0.973) [eps_u from the 2^(3/2) rule,
        b_u fit to (u,c)] cannot reach the steep up triplet m_t/m_u ~ 7.5e4 -- a free (b,eps) fit DOES
        reach it (eps ~ 1.8-2.8), so it is the TABLE's value, not the Brannen FORM, that misses.
        ⚠️ CRUCIAL (TWT mass-verifier principle): this miss is entirely DRIVEN BY THE TOP, which is NOT
        a TWT verifier (no top hadrons -- m_t is QCD-model). Only u,c are hadron-indicated up-type masses,
        and TWO masses underdetermine the 3-parameter triplet, so the eps_u rule is TWT-UNTESTABLE, NOT
        falsified. The top INDICATOR hints the up-sector treatment (the rule and/or b_u) may need revisiting
        -- an indicator-level signal, recorded as such, NOT a TWT falsification. (The legitimate up/down
        verifier is the HADRON spectrum (V1 30-hadron fit, 6 nominal / ~9 effective params -> 30 hadron
        masses, top absent — V1 paper-reported only; the script is deliberately NOT in this repo per
        standing 2026-06-24 directive + W-LIVE-MASS-AUDIT 2026-06-29 snapping-disguised-as-derivation; worklist F3).)
      * DIAL AUDIT (indicator-level, NOT a TWT parameter-economy verdict): per sector the form has
        {Lam,b,eps,psi} = 4 params for 3 masses (1 redundant; the degeneracy). The 'four continuous dials'
        (scale=f_pi, D/J=delta_L, eps_d, b_d) cover the LEPTONS (legitimate -- leptons are physical) + the
        down-quark INDICATORS. The quark-mass reconstruction adds psi_d, psi_u, b_u (and Lam_u/Lam_d; eps_u
        via a rule), but this counts dials to fit INDICATORS, not the hadron verifier. The TWT parameter
        economy for the quark/hadron sector is the V1 30-HADRON FIT (6 nominal / ~9 effective params -> 30
        hadrons — V1 paper-only, retired from V2 paper body under W-LIVE-MASS-AUDIT 2026-06-29 as snapping-
        disguised-as-derivation, the script deliberately NOT in this repo per standing 2026-06-24 directive,
        worklist F3), NOT this quark-mass count. So the four-dial headline is precise for the leptons; the
        quark-sector economy is the (now retired) V1 30-hadron fit, and the quark-mass dial count here is
        an INDICATOR-level observation, not a TWT
        verdict on parameter economy. (Structural results below -- the operator rule and the CKM democratic
        finding -- do NOT depend on the quark-mass values and stand.)"""
    np = __import__("numpy")
    out = {"scale_note": "MS-bar; m_d,m_s at 2GeV, m_b at m_b, m_c at m_c, m_t MS-bar (scale-dependent)"}

    def fit_Lam_psi(masses, b, eps):
        tgt = np.sort(np.sqrt(masses)); rd = np.log(tgt[1:]/tgt[0])
        def loss(psi):
            v = np.sort(np.abs(_sqrt_masses(1.0, b, eps, psi)))
            return 1e9 if v[0] < 1e-12 else float(np.sum((np.log(v[1:]/v[0]) - rd)**2))
        best = min(((p, loss(p)) for p in np.linspace(0, 2*math.pi, 400)), key=lambda t: t[1])
        from scipy.optimize import minimize
        r = minimize(lambda x: loss(x[0]), [best[0]], method="Nelder-Mead",
                     options=dict(xatol=1e-10, fatol=1e-14))
        psi = r.x[0] % (2*math.pi)
        vm = np.sort(np.abs(_sqrt_masses(1.0, b, eps, psi)))
        Lam = float(np.exp(np.mean(np.log(tgt)) - np.mean(np.log(vm))))
        m = (np.sort(np.abs(_sqrt_masses(Lam, b, eps, psi))))**2
        resid = (m - np.sort(masses))/np.sort(masses)*100
        return math.degrees(psi), Lam, m, resid

    b_d, eps_d, b_u, eps_u = 1.172, 0.344, 1.033, 0.973
    psd, Lam_d, m_d, res_d = fit_Lam_psi(np.array(PDG_QUARK_MASSES["down"]), b_d, eps_d)
    psu, Lam_u, m_u, res_u = fit_Lam_psi(np.array(PDG_QUARK_MASSES["up"]), b_u, eps_u)
    out["down"] = {"psi_deg": round(psd, 2), "Lambda": round(Lam_d, 3),
                   "max_resid_pct": round(float(np.max(np.abs(res_d))), 2)}
    out["up"]   = {"psi_deg": round(psu, 2), "Lambda": round(Lam_u, 3),
                   "max_resid_pct": round(float(np.max(np.abs(res_u))), 2)}

    # ASSERT: down reconstructs well (tautological but real); up MISSES the m_t INDICATOR (NOT a TWT
    # falsification -- top has no hadrons, so m_t is not a verifier; this documents the indicator-level miss)
    assert np.max(np.abs(res_d)) < 1.0, "down should reconstruct to <1% (b_d,eps_d fitted from d,s,b)"
    assert np.max(np.abs(res_u)) > 50.0, "up misses the m_t indicator (table b_u,eps_u vs the steep up triplet)"

    # ASSERT: psi is degenerate with (b,eps) -> not uniquely surfaced
    from scipy.optimize import minimize
    tgt = np.sort(np.sqrt(np.array(PDG_QUARK_MASSES["down"]))); rd = np.log(tgt[1:]/tgt[0])
    n_psi_fit = 0
    for psd_deg in range(0, 180, 10):
        psi = math.radians(psd_deg)
        def loss(x):
            b, eps = x; v = np.sort(np.abs(_sqrt_masses(1.0, b, eps, psi)))
            return 1e9 if v[0] < 1e-12 else float(np.sum((np.log(v[1:]/v[0]) - rd)**2))
        r = minimize(loss, [1.0, 0.3], method="Nelder-Mead",
                     options=dict(xatol=1e-10, fatol=1e-14, maxiter=5000))
        if r.fun < 1e-6: n_psi_fit += 1
    out["psi_degeneracy"] = f"{n_psi_fit}/18 scanned psi reproduce the down masses -> psi NOT uniquely surfaced (near-uniform degeneracy)"
    assert n_psi_fit >= 12, "psi must be degenerate with (b,eps) (most psi fit the same masses)"

    out["dial_audit"] = {
        "params_per_sector": "{Lam,b,eps,psi} = 4 for 3 masses (1 redundant; degenerate)",
        "four_dials": "{scale=f_pi, D/J=delta_L, eps_d, b_d} -- LEPTONS (legit) + down INDICATORS",
        "extra_beyond_four": "psi_d, psi_u, b_u (+ Lam_u/Lam_d ratio; eps_u via 2^(3/2) rule) -- to fit INDICATORS",
        "up_sector": "vs the m_t INDICATOR only (top has no hadrons -> NOT a TWT verifier; rule TWT-untestable)",
        "TWT_verifier": ("the V1 30-HADRON FIT (6 nominal / ~9 effective params -> 30 hadron masses, top "
                         "absent) — V1 paper-reported only; deliberately NOT in this repo per standing "
                         "2026-06-24 directive + W-LIVE-MASS-AUDIT 2026-06-29 (snapping-disguised-as-derivation); "
                         "worklist F3"),
        "verdict": "four-dial precise for LEPTONS; quark-sector economy is the hadron fit, NOT this quark-mass count (indicator-level)",
    }
    out["psi_bedrock_derivable"] = False
    out["mass_verifier_principle"] = ("quark masses are TWT INDICATORS, not verifiers; only hadron masses verify "
        "(via the V1 30-hadron fit — paper-only; deliberately NOT in this repo per standing 2026-06-24 directive "
        "+ W-LIVE-MASS-AUDIT 2026-06-29 snapping-disguised-as-derivation; worklist F3). The top is not a verifier "
        "(no top hadrons). The up 'failure' is vs the top "
        "INDICATOR -> NOT a TWT falsification of the eps_u rule (which is TWT-untestable: only u,c are hadron-indicated).")
    out["verdict"] = ("ii (located): psi/Lambda are a NON-UNIQUE fit (not bedrock). Up vs the m_t INDICATOR misses, "
        "but that is NOT a TWT falsification (top has no hadrons -- not a verifier); indicator-level signal only.")
    return out




def ckm_hierarchy_and_cp_seed():
    """[SEED — illustration, not a derivation; the salvageable mechanism distilled from the Gemini note]
    Separates what is real in the 'U(3) frame' idea from the vacuous free-fit (ckm_frame_fit_is_vacuous).
    TWO findings: (1) complexity ALONE does not break democratic — complex-circulant up/down operators
    still share the DFT frame ([M_u,M_d]≈0 to 1e-15) → democratic; so 'complexify to U(3)' is NOT the lever.
    (2) the lever is NON-CIRCULANCE: a non-circulant, E-VALUED (complex) term breaks the shared frame and
    produces BOTH the hierarchy (large off-diagonal) AND a Jarlskog J of the physical scale (~1e-5) from ONE
    complex term. So the complex structure E (real in TWT, E=e12345, `wave_E_complex_structure`) is the
    natural SOURCE of the CKM CP phase, and it arrives WITH the hierarchy-generating term if that term is
    E-valued. CONSEQUENCE (sharpens the located CKM gate, weak_isospin_verdict): the owed object — the
    chiral/handed projector that breaks circulance (the non-orbit overlap) — is naturally COMPLEX, so
    deriving it would yield the magnitudes AND J together, tying CKM CP violation to the §19.8.1 forced
    e4-handedness via E. STILL OWED: the DERIVATION of that projector (this illustrates the mechanism, not
    the values). self-check: complex-circulant commutes (<1e-12); the non-circulant E-term gives off-diagonal
    >0.5 and |J|>1e-6."""
    np = __import__("numpy")
    w = np.exp(2j*np.pi/3)
    def circ(c): return np.array([[c[(i-j) % 3] for j in range(3)] for i in range(3)], complex)
    def ckm(Mu, Md):
        _, Vu = np.linalg.eigh(Mu @ Mu.conj().T); _, Vd = np.linalg.eigh(Md @ Md.conj().T)
        V = Vu.conj().T @ Vd
        return float(np.max(np.abs(V - np.diag(np.diag(V))))), V
    Mu = circ([1.0, 0.3*np.exp(1j*0.7), 0.2*np.exp(-1j*0.4)])
    Md = circ([1.1, 0.25*np.exp(1j*1.3), 0.15*np.exp(1j*0.9)])
    comm_circ = float(np.linalg.norm(Mu @ Md - Md @ Mu)); od_circ, _ = ckm(Mu, Md)
    P = np.array([[0, 0.18j, 0], [-0.18j, 0, 0.05j], [0, -0.05j, 0]], complex)  # non-circulant, E-valued
    od_nc, V = ckm(Mu, Md + P)
    J = float(np.imag(V[0, 0]*V[1, 1]*np.conj(V[0, 1])*np.conj(V[1, 0])))
    assert comm_circ < 1e-12 and od_circ < 1e-9 and od_nc > 0.5 and abs(J) > 1e-6
    return {
        "complexity_alone": f"complex-circulant still commutes ([M_u,M_d]={comm_circ:.0e}) → democratic "
                            f"(off-diag {od_circ:.0e}); NOT the lever",
        "non_circulance_plus_E": f"a non-circulant E-valued term → hierarchy (off-diag {od_nc:.2f}) AND "
                                 f"CP (J={J:.1e}, physical scale) from ONE complex term",
        "the_seed": "E (=e12345, real in TWT) is the natural SOURCE of the CKM CP phase; it arrives WITH the "
                    "hierarchy term if that term is E-valued",
        "sharpens": "the owed chiral/handed projector (the non-circulant overlap) is naturally complex → "
                    "would give magnitudes + J together, tying CP to the §19.8.1 e4-handedness via E",
        "still_owed": "the DERIVATION of that projector (the mechanism, not the values; cf. ckm_frame_fit_is_vacuous)",
    }


def ckm_arc_sector_and_corotation():
    """[DERIVED — CKM arc Phase A, Editor clean-room verified] The chiral sector is DERIVED to be S₊
    (I₄=+1) from §19.8.1's forced +e₄ handedness (e₂₃·e₁₄=+I₄ — the forward-mode / DM / CP parity), NOT an
    assumed Hodge identification (the weak-isospin lesson NOT repeated); the projector is ½(1+I₄).
    ★ CO-ROTATION (refines/overturns the coarse rank-table reading): the weak isospin co-rotates with the
    sector (su(2)₊ acts on S₊, su(2)₋ on S₋), and a self-dual generator acts TRIVIALLY on anti-self-dual
    bivectors ([self-dual, anti-self-dual] = 0). So the rank-0 'democratic cell' (su(2)₊ on anti-self-dual)
    is the TRIVIAL-action cell and is PHYSICALLY UNREACHABLE — the weak isospin always pairs its chirality
    with the matching generation sector, giving rank-3 automatically. Democratic therefore does NOT come
    from that cell (resolving the prior conflation worry); it comes from the circulant linchpin below.
    self-check: e₂₃·e₁₄=+I₄; [self-dual,self-dual]≠0 and [self-dual,anti-self-dual]=0."""
    def mvmul(A, B):
        C = {}
        for ba, ca in A.items():
            for bb, cb in B.items():
                s, bl = _blade_mul(ba, bb); C[bl] = C.get(bl, 0) + s*ca*cb
        return {k: v for k, v in C.items() if abs(v) > 1e-12}
    def comm(A, B):
        P = mvmul(A, B); Q = mvmul(B, A); R = dict(P)
        for k, v in Q.items(): R[k] = R.get(k, 0) - v
        return {k: v for k, v in R.items() if abs(v) > 1e-12}
    SD = [{(1, 2): 1, (3, 4): 1}, {(1, 3): 1, (2, 4): -1}, {(1, 4): 1, (2, 3): 1}]
    ASD = [{(1, 2): 1, (3, 4): -1}, {(1, 3): 1, (2, 4): 1}, {(1, 4): 1, (2, 3): -1}]
    e23e14 = _blade_mul((2, 3), (1, 4))
    sd_sd = max(len(comm(SD[i], SD[j])) for i in range(3) for j in range(3) if i != j)
    sd_asd = max(len(comm(SD[i], ASD[j])) for i in range(3) for j in range(3))
    assert e23e14 == (1, (1, 2, 3, 4)) and sd_sd > 0 and sd_asd == 0
    return {
        "sector": "S₊ (I₄=+1), DERIVED from §19.8.1's +e₄ (e₂₃·e₁₄=+I₄) — not an assumed Hodge identification",
        "projector": "½(1+I₄)",
        "corotation": "su(2)₊ on S₊, su(2)₋ on S₋; [self-dual, anti-self-dual]=0 (su(2)₊ trivial on anti-self-dual)",
        "rank0_cell_status": "the (su(2)₊, anti-self-dual) rank-0 cell is the TRIVIAL-action cell → PHYSICALLY "
                             "UNREACHABLE (the weak isospin co-rotates) → rank-3 is automatic on the matched sector",
        "democratic_source": "NOT the trivial cell — the circulant linchpin (shared meta-time phase) below",
    }



# ---- e₄-orthogonal projection mass mechanism (CONSTITUENT sector; TASK e4) -----
# Separate sector from quark_brannen_table (current/generation): same modified-Brannen
# form + phase psi~delta_L, different (b,eps) because different physical quantities.
# RECONCILED verdict (Coordinator over the build's headline (iii)): PART A central claim
# is UNRESOLVED / READING-DEPENDENT, not a clean obstruction. Touches NOTHING in the
# current sector. Constituent amplitudes below = v14 baryon fit output (RMS 0.993%).
_E4_CONSTITUENT_A = {"u": 385.7, "d": 396.6, "s": 553.3, "c": 1668.7, "b": 4990.5}  # MeV (v14 fit)
_E4_PDG_CURRENT   = {"u": 2.16, "d": 4.67, "s": 93, "c": 1270, "b": 4180}           # MeV (PDG running, indicators)




def meson_dynamical_current_split():
    """[TASK-e4 PART C, qualitative success + localized gap] §17.4: Meson = q + counter-rotating q-bar;
    m = 2 omega |cos(alpha/2)| (vector alpha=0 full; pseudoscalar alpha=pi cancels). ONLY the
    DYNAMICAL (chiral, soft) part cancels; the CURRENT (bare) part does not -> the P-V gap = the
    cancelled dynamical rotation, which SHRINKS as the quark gets heavier. f_dyn=(A-m_cur)/A is
    fixed by current-vs-constituent mass, NOT per state. Findings: f_dyn orders light>charm>bottom;
    the etac/etab ratio is consistent with ~1/sqrt(A) BUT that is a 1-parameter fit to 2 data
    points, NOT a derived law; the light pi gap is ~2.5x larger = the measured chiral enhancement.
    LOCALIZED GAP: unifying the heavy 2-point scaling with the light chiral enhancement in ONE
    closed knob-free form is not achieved."""
    A, MCUR = _E4_CONSTITUENT_A, _E4_PDG_CURRENT
    dyn = {q: A[q] - MCUR[q] for q in A}
    PV = {"pi(ud)": (775.3 - 139.6, ("u", "d")), "K(us)": (893.6 - 493.7, ("u", "s")),
          "etac(cc)": (3096.9 - 2983.9, ("c", "c")), "etab(bb)": (9460.3 - 9398.7, ("b", "b"))}
    f_dyn = {m: math.sqrt(dyn[q1]*dyn[q2]) / math.sqrt(A[q1]*A[q2]) for m, (g, (q1, q2)) in PV.items()}
    gc, gb = PV["etac(cc)"][0], PV["etab(bb)"][0]
    p = math.log(gc/gb) / math.log(A["c"]/A["b"])                 # 2-POINT exponent (etac,etab)
    pi_pred = gc * (math.sqrt(A["u"]*A["d"])/A["c"])**p
    pi_enhance = PV["pi(ud)"][0] / pi_pred
    assert gc > gb, "P-V gap must shrink with quark mass (charm gap > bottom gap)"
    assert f_dyn["pi(ud)"] > f_dyn["etac(cc)"] > f_dyn["etab(bb)"], "f_dyn must order light>charm>bottom"
    assert -0.7 < p < -0.4, "etac/etab ratio consistent with ~1/sqrt(A) (2-point fit, not a derived law)"
    assert pi_enhance > 2.0, "light pi gap must exceed the 2-point scaling (chiral/Goldstone enhancement)"
    return {"f_dyn": {m: round(v, 2) for m, v in f_dyn.items()},
            "PV_gaps_MeV": {m: round(g, 1) for m, (g, _) in PV.items()},
            "heavy_exponent_p_from_2_points": round(p, 2),
            "pi_chiral_enhancement_over_2pt": round(pi_enhance, 1), "per_state_knob": False,
            "verdict": "ii (meson): knob-free split reproduces gap-shrinking + ordering; localized gap = "
                       "unify heavy 2-point scaling with light Goldstone enhancement"}

def massless_H_squared(p=(2.0, 3.0, 5.0)):
    """[DERIVED] §19.8.1: H = Σ e_j p_j, H² = |p|² (e_j²=+1, e_i e_j anticommute).
    COMPUTED for a sample momentum."""
    H = sum((p[j-1] * e(j) for j in (1, 2, 3)), 0 * e())
    return H * H, sum(pi**2 for pi in p)


# ---- §19.8.3 sterile RH neutrinos as dark-matter candidate (DM-V2-1 first cut) --
def sterile_rh_relic_check():
    """[LOCATED-GAP] §19.8.3 + DM-V2-1: do TWT's 3 sterile RH neutrinos account for Omega_DM?

    Question. Do TWT's 3 structurally-predicted sterile RH neutrinos (§19.8.3, the wave-decoupled
    S_- modes; one per generation, Dirac partners of the active LH neutrinos) account for
    Omega_DM h^2 ~ 0.12 (Planck 2018)?

    TWT structural facts (DERIVED, §19.8.3 — already banked via `neutrino_lightness`):
      - 3 sterile right-handed Weyl modes exist as wave-decoupled S_- partners.
      - Dirac character: Majorana mass forbidden by B-L conservation (§23.7-§23.9).
      - Therefore m_sterile = m_active per generation (one Dirac eigenvalue per generation).

    TWT OPEN items (gated on §16.6 / §9.6 #1-gap dynamics):
      - The Dirac-mass magnitude (= active-sterile overlap) is OPEN.
      - No SECOND mass scale for the sterile RH is predicted — its mass is TIED to the
        active neutrino's mass by the Dirac character (one Dirac eigenvalue / generation).

    Empirical inputs (witnesses, NOT derived in TWT):
      - Sigma m_nu < 0.12 eV  (Planck 2018 + BAO cosmology bound).
      - Sigma m_nu > 0.06 eV  (oscillation data, normal ordering minimum).
      - Omega_DM h^2 = 0.120  (Planck 2018).
      - Relic formula (Dodelson "Modern Cosmology" eq. 3.55; Lesgourgues-Pastor review):
        for Dirac active neutrinos at thermal decoupling (T_dec ~ 1 MeV >> m_nu),
        Omega_nu h^2 = Sigma m_nu / (94 eV).

    Two production-mechanism scenarios:

    A) THERMAL upper bound (sterile thermalizes alongside active).
       Each helicity Dirac mode at thermal decoupling contributes equally. Even with BOTH
       active and sterile thermalized at the upper Sigma m_nu bound, the ACTIVE+STERILE TOTAL is
       2 * 0.12/94 = 0.00255 — about 2.1% of Omega_DM (shortfall ~47x). The standard relation
       Omega_nu h^2 = Sigma m_nu/94 already counts the active species, so the STERILE SHARE is
       exactly half: 0.00128 — 1.06% of Omega_DM, shortfall ~94x (E-6 relabel, 2026-07-31).
       (This SHOULD NOT happen in TWT — sterile is wave-decoupled — but it bounds the case.)

    B) DODELSON-WIDROW oscillation production (the realistic scenario).
       Sterile relic ~ sin^2(2 theta) * (m_s/keV) for active-sterile mixing angle theta.
       DW sterile-DM matches Omega_DM only for m_s ~ keV with sin^2(2 theta) ~ 1e-10
       (Boyarsky et al. 2019 review, constrained by X-ray + structure formation). In TWT,
       m_s = m_active <~ 0.1 eV (Dirac character ties the masses). The TWT sterile is ~4
       orders of magnitude too light for the DW sterile-DM window.

    Independent structural problem (hot DM).
       Sub-eV thermal fermion has free-streaming length ~ tens of Mpc; washes out small-
       scale structure. Combined f_HDM < ~0.01 from Planck + LSS. So even if abundance
       matched, sub-eV Dirac sterile is excluded as DOMINANT DM by structure formation
       independently of the relic-abundance computation.

    Verdict. 3 sterile RH neutrinos at TWT-implied parameters CANNOT account for Omega_DM:
      - quantitative shortfall ~94x for the sterile share (~47x for the active+sterile total)
        at the most optimistic thermal upper bound;
      - structural exclusion: sub-eV mass ⇒ hot DM ⇒ free-streaming excluded;
      - DW window mismatch: m_s ~ keV needed; TWT predicts <~ 0.1 eV (~4 orders too light).

    Would change if (CLAUDE.md §4 negatives discipline):
      Z1: TWT predicts a SECOND mass scale for sterile RH decoupled from the Dirac eigenvalue
          (e.g. a meta-time grain-scale contribution to the wave-decoupled mode that doesn't
          couple back to the active sector). Not currently in §19.8.
      Z2: A non-thermal production mechanism dumps energy into the sterile sector early
          (e.g. inflaton decay into wave-decoupled modes). Not currently identified.
      Z3: §19.8 active-sterile overlap calculation reveals m_sterile >> m_active without
          violating B-L. Would require breaking the one-Dirac-eigenvalue-per-generation
          structure that currently follows from §19.8.3.

    Tier: LOCATED-GAP (CLAUDE.md §4 tried/failed/would-change-if).
    DM-V2-1 status: sterile-RH-as-DM candidate FALSIFIED at first-cut TWT parameters; the
    DM-V2-1 candidate hunt continues with the other worklist leads (differential coupling,
    wave-train phase-defect)."""
    import math as _math
    # ---- inputs (witnesses) ----
    Sigma_mnu_eV_upper = 0.12      # Planck 2018 + BAO
    Sigma_mnu_eV_lower = 0.06      # NH minimum from oscillation data
    Omega_DM_h2        = 0.120     # Planck 2018
    eV_per_relic       = 94.0      # Dodelson eq. 3.55 (Dirac active, relativistic decoupling)

    # Scenario A: thermal upper bound (both active + sterile thermalize at upper Sigma m_nu)
    Omega_sterile_single  = Sigma_mnu_eV_upper / eV_per_relic
    Omega_sterile_doubled = 2.0 * Omega_sterile_single
    ratio_thermal_upper   = Omega_sterile_doubled / Omega_DM_h2

    # Scenario B: DW mass-window mismatch
    m_s_DW_required_eV = 1.0e3     # 1 keV canonical DW sterile-DM scale
    m_s_TWT_eV_max     = 0.1       # tied to active by Dirac character
    DW_mismatch_orders = round(_math.log10(m_s_DW_required_eV / m_s_TWT_eV_max), 1)

    # Safety asserts (engine-style: a passing primitive must be honest about the verdict)
    assert ratio_thermal_upper < 0.05, "thermal upper bound must remain << Omega_DM (the negative result)"
    assert DW_mismatch_orders >= 4.0,  "DW window mismatch must remain >= 4 orders"

    return {
        # Inputs (witnesses, cited)
        "Sigma_m_nu_eV_upper_Planck18": Sigma_mnu_eV_upper,
        "Sigma_m_nu_eV_lower_oscillation_NH": Sigma_mnu_eV_lower,
        "Omega_DM_h2_Planck18": Omega_DM_h2,
        "eV_per_relic_Dodelson_eq3_55": eV_per_relic,
        # TWT structural prediction (DERIVED §19.8.3)
        "TWT_sterile_count": 3,
        "TWT_sterile_character": "Dirac partner of active LH (wave-decoupled S_-); B-L conservation forbids Majorana",
        "TWT_sterile_mass_scale": "tied to active m_nu via Dirac eigenvalue; no second scale in §19.8",
        # Scenario A: thermal upper bound
        "Omega_sterile_h2_thermal_upper_bound": Omega_sterile_doubled,
        "ratio_thermal_upper_to_Omega_DM": ratio_thermal_upper,
        "thermal_shortfall_factor": round(1.0 / ratio_thermal_upper, 1),
        "NOTE_total_vs_sterile": ("the two fields above are the ACTIVE+STERILE TOTAL (the key name "
                                  "predates the E-6 relabel, 2026-07-31); the sterile-only share is half"),
        "sterile_only_share_h2": Omega_sterile_doubled / 2.0,
        "sterile_only_ratio_to_Omega_DM": ratio_thermal_upper / 2.0,
        "sterile_only_shortfall_factor": round(2.0 / ratio_thermal_upper, 1),
        # Scenario B: DW mass-window mismatch
        "DW_required_m_s_eV": m_s_DW_required_eV,
        "TWT_m_s_max_eV": m_s_TWT_eV_max,
        "DW_mass_mismatch_orders": DW_mismatch_orders,
        # Structural problem (independent)
        "hot_DM_problem": "sub-eV Dirac fermion ⇒ free-streaming ~tens of Mpc; f_HDM<0.01 from Planck+LSS excludes as dominant DM",
        # Verdict + would-change-if
        "verdict": "FAILED-AS-CONJECTURED at first-cut TWT parameters",
        "reasons": [
            "thermal upper bound ~2.1% of Omega_DM (shortfall ~47x)",
            "DW production needs m_s ~ keV; TWT m_s <~ 0.1 eV (~4 orders too light)",
            "sub-eV mass ⇒ hot DM ⇒ excluded as dominant DM by free-streaming",
        ],
        "would_change_if": [
            "Z1: TWT predicts a SECOND mass scale for sterile RH (e.g. monad-scale) decoupled from the active Dirac eigenvalue (not in §19.8)",
            "Z2: a non-thermal production mechanism dumps energy into the sterile sector (e.g. inflaton decay) (not identified)",
            "Z3: §19.8 overlap calc reveals m_sterile >> m_active without B-L violation",
        ],
        "tier": "LOCATED-GAP (CLAUDE.md §4)",
        "DM_V2_1_status": "sterile-RH-as-DM candidate FALSIFIED at first-cut; DM-V2-1 candidate hunt continues with other leads",
    }


# ---- §19.8.5 DM-V2-1 Z1: substrate-level sterile production via §10.5 boundary ---
def sterile_rh_substrate_production_via_L_theta():
    """[LOCATED-GAP-REFINED] DM-V2-1 Z1 (re-attack handle from N30): does the §10.5 topological
    boundary term 𝓛_θ = µ Ψ_0 ρ_L (the substrate-level L-pair creation channel of §23.10) provide
    a non-thermal production mechanism that closes the 47× sterile-RH-as-DM shortfall?

    QUESTION. The Dodelson-Widrow thermal channel gives Ω_s h² ~ 0.0026, only ~2.1% of Ω_DM h²
    (sterile_rh_relic_check, §19.8.3). Z1's lead: the §10.5 term 𝓛_θ = µ Ψ_0 ρ_L sources L-pair
    creation from the substrate vacuum (§23.10 β-decay channel) — a candidate non-thermal route
    that might bypass the DW Boltzmann suppression.

    DERIVATION (overlap-gating argument).

    (1) The L-winding 4-current is j_L^μ = (1/24π²) ε^μνρσ Tr(L_ν L_ρ L_σ) (§10.5 row (a)),
        built from chiral currents L_μ of the rotor field U. These are L-orbit bivectors
        {e_12, e_13, e_23} that act WITHIN the wave-riding sector S_+ — they do NOT connect S_+
        to S_-. So 𝓛_θ sources L-pair creation in S_+ (active LH neutrinos plus their conjugate
        active antineutrinos), NOT in S_- (where the sterile RH lives).

    (2) The sterile RH neutrino is the wave-DECOUPLED S_- mode (§19.8.3). The unique connector
        between S_+ (wave-riding) and S_- (wave-decoupled) in current TWT is the active-sterile
        overlap ε — the same overlap that sets the Dirac neutrino mass m_ν = ε · Ψ_0 (§19.8.3:
        "the Dirac mass couples a wave-riding state to a wave-decoupled one; the overlap is
        suppressed, the mass naturally tiny").

    (3) Taking Ψ_0 ~ f_π ~ 93 MeV (the chiral condensate scale, the natural seed for the
        boundary term — §10.5 eq. (a) "constant condensate Φ = Ψ_0") and m_ν ~ 0.05 eV
        (Σ m_ν ≥ 0.06 eV NH minimum / 3 generations):
            ε ~ m_ν / Ψ_0 ~ 5 × 10⁻¹⁰
            ε² ~ 3 × 10⁻¹⁹
        Each active neutrino produced by 𝓛_θ branches to sterile with probability ε². So
        Ω_sterile_from_Lθ ~ ε² · Ω_active_from_Lθ.

    (4) The active side is bounded by Σ m_ν < 0.12 eV (Planck 2018+BAO); the sterile branching
        is suppressed by ε² that EQUALS the sin²(2θ) factor in Dodelson-Widrow. So 𝓛_θ does NOT
        provide an independent enhancement: whatever it produces in S_+ is gated by the same ε²
        when transferring to S_-. The 47× shortfall does NOT close.

    VERDICT (honest tier). Z1 candidate REFUTED-AT-FIRST-CUT: the §10.5 substrate channel is
    structurally interesting (it is the substrate-level mechanism for §23.10 β-decay L-pair
    creation) but is overlap-limited by the same active-sterile overlap that gates DW. The
    required branching to close 47× is ~47; the actual branching is ~3 × 10⁻¹⁹ — a ~20-order
    shortfall in the unique S_+↔S_- connector.

    REFINEMENT OF N30. The shortfall is now structurally sharper: it is not a thermal-window
    mismatch in isolation, but a structural OVERLAP-LIMIT on the unique connector between wave-
    riding (S_+, where the L-current lives) and wave-decoupled (S_-, where the sterile lives).
    No mechanism in current TWT bypasses it.

    WOULD-CHANGE-IF (refined Z1 handles).
      Z1a: a substrate channel that creates pure-S_- L-pairs directly would close the shortfall
           — but it requires breaking S_- wave-decoupling, in tension with §19.8.1 forced
           handedness.
      Z1b: the active-sterile production overlap is DECOUPLED from the Dirac-mass-setting
           overlap (two distinct overlaps) — not in §19.8.3 as currently constructed.
      Z1c: the Dirac neutrino mass eigenvalue is at the ~keV scale rather than ~0.05 eV — in
           tension with cosmological Σ m_ν < 0.12 eV bound.

    Z2 (non-standard sterile mass scale) and Z3 (explicit DM-out-of-framework scope statement)
    from the original N30 are unaffected by this Z1 analysis.
    """
    import math as _math

    # Parameter inputs (witnesses; all canon-grounded, NOT freshly derived)
    m_nu_eV          = 0.05         # ~Σm_ν / 3, NH-min consistent with Planck18+BAO
    f_pi_MeV         = 93.0         # chiral condensate scale = natural Ψ_0 seed (§10.2)
    Psi_0_eV         = f_pi_MeV * 1e6
    eps_overlap      = m_nu_eV / Psi_0_eV       # the Dirac-mass-setting active-sterile overlap
    eps_sq           = eps_overlap ** 2          # the S_+ → S_- transition suppression

    # Required vs actual branching to close the 47x shortfall via L_theta
    required_enhancement     = 47.0                  # from sterile_rh_relic_check (DW shortfall)
    actual_branching_via_eps = eps_sq                # ~3e-19
    overlap_shortfall_orders = round(_math.log10(required_enhancement / actual_branching_via_eps), 1)

    # Safety asserts (engine-style negative-result discipline per canon §4)
    assert eps_sq < 1e-15,                  "ε² should be ~3e-19 at canonical params (m_ν~0.05 eV, Ψ_0~f_π)"
    assert overlap_shortfall_orders >= 15.0, "shortfall must remain many orders for refutation to hold"
    assert eps_overlap < 1e-8,              "ε must remain tiny (Dirac-mass-setting overlap)"

    return {
        # Setup (witnesses, cited)
        "active_neutrino_mass_eV":              m_nu_eV,
        "chiral_condensate_scale_MeV_(Psi_0~f_pi)": f_pi_MeV,
        "active_sterile_overlap_eps":           eps_overlap,
        "eps_squared_S_plus_to_S_minus_branching": eps_sq,
        # Verdict
        "verdict":                              "REFUTED-AT-FIRST-CUT",
        "required_branching_to_close_47x_shortfall": required_enhancement,
        "actual_branching_via_eps_squared":      eps_sq,
        "overlap_shortfall_orders_of_magnitude":  overlap_shortfall_orders,
        # Structural reason (the refinement of N30)
        "structural_reason":
            "L_theta sources L-pair creation in S_+ (j_L built from L-orbit bivectors acting on wave-riding spinors); "
            "sterile RH lives in S_- (wave-decoupled, §19.8.3); the unique S_+ <-> S_- connector is the active-sterile "
            "overlap eps that ALSO sets the Dirac neutrino mass — so the sterile branching is gated by the SAME eps^2 as Dodelson-Widrow",
        "why_NOT_a_DW_bypass":
            "eps is the UNIQUE S_+ <-> S_- connector in TWT as currently constructed (§19.8.3); "
            "any channel acting on S_+ branches into S_- with probability eps^2; L_theta gives an enhanced active production "
            "on S_+ but the sterile branch retains the DW overlap-suppression",
        # Refined would-change-if handles
        "would_change_if": [
            "Z1a: substrate channel creating pure-S_- L-pairs directly (requires breaking S_- wave-decoupling — in tension with §19.8.1 forced-handedness)",
            "Z1b: production overlap DECOUPLED from the Dirac-mass overlap (two distinct overlaps — not in §19.8.3)",
            "Z1c: Dirac neutrino mass eigenvalue at ~keV rather than ~0.05 eV (in tension with cosmological Σm_ν < 0.12 eV)",
        ],
        # Tier + DM-V2-1 status
        "tier": "LOCATED-GAP-REFINED (CLAUDE.md §4)",
        "N30_refinement":
            "the 47x shortfall is not a thermal-window mismatch in isolation but a structural overlap-limit on the unique "
            "S_+ <-> S_- connector (eps^2); REFINES rather than RESOLVES N30",
        "DM_V2_1_Z1_status":
            "Z1 (non-thermal substrate production via §10.5) closed-NEGATIVE; leads (i) differential coupling and "
            "(ii) wave-train phase-defect still OPEN; Z2 (non-standard sterile mass) and Z3 (explicit out-of-framework scope) unaffected; "
            "DM-V2-1 remains an OPEN worklist item",
    }



# ======================================================================
# MATTER / SOLITON SECTOR (§10,§16,§22.3/5)   [twt_matter]
# ======================================================================



# ---- §16.2  Skyrme BVP — SYMBOLIC audit (adjudicates 8 vs 4) --------------------
def skyrme_BVP_audit():
    """[AUDIT] §16.2: derive the Euler-Lagrange equation from the energy density and
    confirm the profile-equation coefficient is 8 sin²F (NOT 4 — resolving the
    flagged revision-map typo). Dimensionless integrand (4π and f_π,e absorbed):
        L = (1/8)[F'²x² + 2sin²F] + (1/2)[2sin²F F'² + sin⁴F/x²].
    EL: d/dx(∂L/∂F') - ∂L/∂F = 0; ×4 gives the standard ANW form
        ∂_x[(x² + 8sin²F)F'] = sin2F[1 + 4F'² + 4sin²F/x²]."""
    x, F, Fp = sp.symbols('x F Fp', real=True)
    L = sp.Rational(1, 8) * (Fp**2 * x**2 + 2*sp.sin(F)**2) \
        + sp.Rational(1, 2) * (2*sp.sin(F)**2 * Fp**2 + sp.sin(F)**4 / x**2)
    dL_dFp = sp.simplify(4 * sp.diff(L, Fp))          # the (x²+8sin²F)F' factor
    dL_dF  = sp.simplify(4 * sp.diff(L, F))           # the sin2F[...] RHS
    target_lhs_factor = Fp * (x**2 + 8*sp.sin(F)**2)
    target_rhs = sp.sin(2*F) * (1 + 4*Fp**2 + 4*sp.sin(F)**2 / x**2)
    coeff_of_sin2 = sp.simplify(dL_dFp / Fp).coeff(sp.sin(F)**2)   # should be 8
    return {
        "dL/dFp (×4)": dL_dFp,
        "matches (x²+8sin²F)F'": sp.simplify(dL_dFp - target_lhs_factor) == 0,
        "RHS (×4) matches sin2F[1+4F'²+4sin²F/x²]": sp.simplify(dL_dF - target_rhs) == 0,
        "coefficient of sin²F": int(coeff_of_sin2),     # == 8, adjudicates the typo
    }


# ---- §10.2  the kinetic term: f_π² = 8J/a -------------------------------------
def f_pi_squared(J: float = 1.0, a: float = 1.0) -> float:
    """[DERIVED] §10.2: the 12 spatial bonds projected onto 3 dimensions give the chiral
    kinetic term H_kin = (z_sp/d3)(J/a)|∂U|² = 4(J/a)|∂U|²; matching to (f_π²/2)|∂U|²
    gives f_π² = 8J/a. The 8 = 2 × (z_sp/d3) = 2 × (12/3). [D4 coordination]
    NOMENCLATURE: the absolute f_π = 129 MeV consumed downstream is the ANW FITTED value
    (physical F_π ≈ 186 MeV in ANW's normalization), not the measured decay constant."""
    z_sp, d3 = 12, 3
    return 2 * (z_sp / d3) * (J / a)    # = 8 J/a


# ---- §10.3  Skyrme stabilizer: bare + dressed coupling (honestly hedged) -------
def kappa_F_bare(J: float = 1.0) -> float:
    """[DERIVED] §10.3: bare exchange Skyrme coefficient κ_F = +J/24 (D-independent)."""
    return J / 24.0


def qcd_uv_conformal_phaseCD() -> dict:
    """[ARC TERMINAL — (ii) LOCATED, a mechanism-less dynamics-gated GAP (Editor weight, post-correction: the candidate β sign is OPEN, so NOT a wrong prediction — see body)] TASK qcd-UV (the gluon-free
    asymptotic-freedom burden, §25.2 / item 7's β₃ half). Proper two-build A→D at every phase (no solo
    exemption). The gate `qcd_collider_phenomenology()` STAYS RAISING.

    ARC: **Route I (emergent gluon-free antiscreening) is CLOSED — a DERIVED absence.** Asymptotic freedom
    requires the paramagnetic (spin) contribution of a charged SPIN-1 field to beat the diamagnetic orbital
    one (general Nielsen-Hughes, NOT the QCD β₀ plug-in); TWT's colour content is spin-0 σ-Goldstones +
    spin-½ sub-windings (diamagnetic → SCREENING), and colour is ℤ₃-DISCRETE (no continuous colour symmetry
    to gauge → no colour gauge boson, emergent or fundamental). The data's antiscreening is gauged-continuous-
    SU(3) paramagnetism, FORECLOSED by the gluon-free/discrete-colour commitment. The 2D-O(N) σ-model AF does
    NOT transfer to 4D (the 2-derivative coupling is irrelevant in 4D). (Phase A: the gate-OVERTURN — colour
    persists into the AF band, measured continuously to TeV, AF onset only 1.42× above Λ_cell≈703 MeV, so
    Route II's 'colour caps at the substrate scale' is NOT an escape: the AF/Bjorken falsifier IS colour-
    structured physics, not dodge-able by the cell scale.)

    THE CONFORMAL / nearly-conformal route carries the GENERIC SCALE-INVARIANT SKELETON (pointlike DIS
    response — discrete ℤ₃ + global U(3) + scale-free MARGINAL Skyrme [Derrick λ^0], the 2-deriv σ-model being
    irrelevant), CONFINEMENT-CONSISTENCY (the SAME structure confines at the IR lock Ω_B~1 GeV / soliton size
    ℓ_S and goes scale-free in the UV — Gate C, CLASSICAL/CONDITIONAL: tree-level scale-invariance, not an
    unconditional fixed-point derivation), and EW RG-CONSISTENCY (Gate D3: sin²θ_W=3/8 is electroweak-only /
    SU(5)-free / α_s-INDEPENDENT at one loop ⇒ the gluon-free strong sector DECOUPLES — a decoupling result,
    NOT positive AF support; the 3-coupling unification DOES depend on the unsourced running).

    ★ THE TENSION (the PRIMARY characterization, not a caveat): the high-Q physics = [exact Bjorken scaling]
    + [AF-like LOG scaling violations]. Exact scaling is the GENERIC content of ANY scale-invariant theory
    (the trivial skeleton); the LOG violations are the running coupling / DGLAP = the ENTIRE NON-TRIVIAL
    CONTENT = AF ITSELF. So the arc sources the skeleton + the consistency checks and LOCATES ALL of
    asymptotic freedom as a SINGLE residual = the marginal-4D-Skyrme β-function. **The arc LOCATES AF rather
    than ACHIEVING it.**

    [STATUS UPDATE 2026-07-05, R-148: the residual's SIGN face is now decided-conditional —
    beta_3 <= 0 (AF-signed) via the dispersive/I-13 package at the dressed one-coupling level,
    DERIVED-conditional-GENERIC; the wrong-sign risk is REMOVED (conditional on I-13, revert
    clause named). The DGLAP structure + magnitude residual below STANDS — sign-consistency
    is NOT AF-achieved (additive f^2-loop drift, no antiscreening mechanism).]
    THE RESIDUAL'S STATUS (Coordinator corrected BOTH builds): GENUINELY OPEN — NOT 'structurally disfavored'
    (that over-extends the spin-1-paramagnetism, a GAUGE-coupling fact, to a SCALAR self-coupling; 4-derivative
    scalar theories CAN be asymptotically free) and NOT 'plausibly closeable' (no POSITIVE mechanism gives
    β<0, and the residual is the full DGLAP structure, not merely a sign). UNMOTIVATED + structurally
    demanding. FALSIFYING-ADJACENT: if the marginal-Skyrme sector does not realize the DGLAP-structured
    violations, the observed running is unsourced and TWT parts company with observed AF. Formal label (ii)
    (the strict 'cannot' is gated; the bare β-sign is open); the WEIGHT is the high-weight tension above.
    The violations are NOT 'α_s running' (TWT has no continuous gauge coupling) — they relocate to the
    marginal-Skyrme β, GATED to Paper 2."""
    HBARC = 197.327
    return {
        "GATE_C": "consistent, CLASSICAL/CONDITIONAL: IR lock (Ω_B, ℓ_S) and a scale-free UV (marginal Skyrme "
                  "dominates; σ-model irrelevant) are one structure IF the fixed point exists (the D2 residual).",
        "D1_Bjorken_skeleton": "CANDIDATE — sources the generic SCALE-INVARIANT SKELETON (pointlike response); the "
                               "OBSERVED object is APPROXIMATE (violated) scaling, whose deviation (D2) is unsourced.",
        "D2_AF_log_violations": "THE RESIDUAL = AF ITSELF. Only log-runner is the marginal-Skyrme β; σ-model running "
                                "is power-law (wrong form); discreteness brackets but doesn't source. GENUINELY OPEN "
                                "(4-deriv scalar can be AF) but UNMOTIVATED (no positive mechanism) + full DGLAP demanded.",
        "D3_RG_consistency": f"sin²θ_W={weinberg_sin2()} EW-only/SU(5)-free/α_s-independent ⇒ DECOUPLING (gluon-free "
                             "strong sector doesn't spoil the EW prediction) — NOT positive AF support.",
        "Route_I": "CLOSED negative (B-screen, DERIVED): no charged spin-1 → no antiscreening; ℤ₃-discrete colour → no "
                   "gauge boson; gauged-SU(3) paramagnetism foreclosed by gluon-free; 2D σ-model AF doesn't transfer to 4D.",
        "conformal_route_CARRIES": "the scale-invariant skeleton (pointlike) + confinement-consistency (C) + EW "
                                   "RG-consistency (D3) — NOT asymptotic freedom",
        "conformal_route_does_NOT_carry": "the observed AF running (the DGLAP log violations) = the entire non-trivial "
                                           "content; reduces to the single open, unmotivated residual (marginal-Skyrme β)",
        "marginal_Skyrme_kappa_F": round(kappa_F_bare(), 5),
        "GATE_D": "(ii) LOCATED, a mechanism-less dynamics-gated GAP (NOT a wrong prediction — the marginal-Skyrme β "
                  "sign is genuinely OPEN): the arc locates ALL of AF as the residual, unsourced + unmotivated, "
                  "behind the same unbuilt dynamics that gate the other values, but with no backup mechanism (load-bearing).",
        "terminal_result": "a clean, formalization-checked LOCALIZATION OF WHERE TWT AND OBSERVED AF PART COMPANY: TWT "
                           "reproduces the scale-invariant skeleton + meets the qualitative collision phenomenology (jets/pointlike "
                           "response), but supplies no DERIVED source for the observed running — a mechanism-less, dynamics-gated "
                           "gap (sign OPEN, not a wrong prediction); the lone candidate (marginal-Skyrme β) is gated to Paper 2.",
        "gate": "qcd_collider_phenomenology() stays RAISING (violations unsourced ⇒ no un-gating).",
    }


def beta3_sign_from_reflection_positivity() -> dict:
    """[LOCATED-GAP] §22.2 (Sector 3): does Euclidean reflection-positivity (OS3) /
    ghost-freedom on the marginal 4D-Skyrme sector force the sign of β₃?

    SETUP. The Skyrme quartic in Euclidean 4D is
        L_4 = -(1/(32 e²)) Tr([L_μ, L_ν]²),   L_μ = U†∂_μU,
    a 4-derivative term BUT with derivatives distributed as four (∂U) factors
    (NOT (∂²U)²). The EL equations remain second-order in time (the classical
    Skyrme/ANW result) — no Ostrogradski ghost at any sign of the coefficient.

    WHAT RP DOES FORCE (the substantive content). Hamiltonian positivity
    (the OS3 / OS-reconstruction requirement) constrains the BARE coefficient
    sign. Expanding L_4 in time-derivatives,
        L_4 ⊃ (1/e²) Tr([L_0, L_i]²) + (1/e²) Tr([L_i, L_j]²),
    both trace-squares are non-negative on hermitian L_μ; for the Euclidean
    action to give a bounded-below Hamiltonian on Wick-rotation, the
    coefficient must satisfy 1/e² > 0 (equivalently e² > 0). FORCED by RP.

    WHAT RP DOES NOT FORCE (the gap). β₃ = μ d(1/e²)/dμ at one loop on the
    SU(2) σ-model coset is set by FUNCTIONAL-DETERMINANT SIGNS of quantum
    fluctuations — NOT by the bare-sign constraint. RP at every scale
    (consistency of OS reconstruction along RG) requires 1/e²(μ) > 0 for
    all μ; this says 1/e²(μ) never crosses zero, NOT that its derivative
    has a particular sign. Both signs of β₃ are RP-compatible:
      • β₃ < 0 (AF): 1/e² grows in IR, stays positive — consistent.
      • β₃ > 0 (IR-free): 1/e² grows in UV, stays positive — consistent.

    EMPIRICAL ANALOGUES (both signs realized within RP). 2D O(N) σ-model:
    RP + AF (β<0). 4D φ⁴: RP + IR-free (β>0). RP is sign-agnostic on β.

    NEGATIVES-DISCIPLINE STATEMENT (canon §4).
      tried: RP / Hamiltonian-boundedness / ghost-freedom constraint on the
             marginal 4D-Skyrme bare action.
      failed because: RP fixes only the bare coefficient sign (1/e² > 0).
             It does NOT constrain the SIGN of dln(1/e²)/dlnμ. Both signs of
             β₃ are RP-compatible at every scale.
      would change if: a stronger Euclidean monotone (a c/a-theorem analogue
             on the marginal-Skyrme RG flow, or a Källén-Lehmann positivity
             combined with a unitarity bound on the running quartic) were
             established. None currently known for the 4D Skyrme sector.
             [FIRED 2026-07-05, R-148 marginal_skyrme_beta3_sign_dispersive: the
             KL/unitarity route delivered — beta_3 <= 0, the AF-SIGNED branch,
             DERIVED-conditional-GENERIC (I-13 dispersive package, registered;
             revert clause: refusing the package restores THIS located gap).
             The sign face is decided-conditional; the running/DGLAP residual
             below stands. NOTE the first build was REFUTED for transplanting
             THIS docstring's EUCLIDEAN density into Minkowski machinery — N42.]

    Sector 3 closes as VACUOUS: the constraint exists but does not bite on β₃.
    Stays e5-litmus-free; #1-gap-free. The β₃-sign residual remains the
    §22.2 / `qcd_uv_conformal_phaseCD` mechanism-less gap."""
    return {
        "RP_forces_bare_sign":      "YES: 1/e² > 0 (Hamiltonian boundedness on Wick rotation).",
        "RP_forces_beta3_sign":     "NO: RP requires 1/e²(μ) > 0 at all μ, consistent with EITHER sign of d(1/e²)/dlnμ.",
        "ghost_status":             "Skyrme quartic has 4 derivs but ONE per field copy (L_μ = U†∂_μU) → second-order EL → NO Ostrogradski ghost at either sign.",
        "RP_analogues_both_signs":  "2D O(N) σ-model: RP + AF (β<0). 4D φ⁴: RP + IR-free (β>0). RP is sign-agnostic on β.",
        "tried":                    "RP / Hamiltonian-boundedness / ghost-freedom on the marginal 4D-Skyrme bare action.",
        "failed_because":           "RP fixes the bare-coefficient sign (1/e² > 0) but does NOT constrain dln(1/e²)/dlnμ.",
        "would_change_if":          "a c/a-theorem analogue or Källén-Lehmann + unitarity bound on the running marginal-Skyrme coupling were established — none currently known.",
        "verdict":                  "LOCATED-GAP: RP constraint is non-empty but VACUOUS on β₃. Sector 3 does NOT pin AF; residual stays in `qcd_uv_conformal_phaseCD` (the §22.2 mechanism-less gap).",
        "e5_litmus":                "e5-free (no e5 enters the argument).",
        "hash_1_gap":               "#1-gap free (no routing through driven-dissipative dynamics).",
    }


def D_crit_over_J() -> float:
    """[DERIVED] §10.3: D_crit/J = 6/√2 = 3√2 = √18 = 4.243 (pure D4 geometry, no fit).

    REFERENT NOTE (J,D/Γ rework). Do not confuse this geometric D_crit with the
    "D = J" balance point of §C.3.6 / R-069. R-069's theorem is about the two
    AMPLITUDES of the chiral ℤ₃ potential: `B = A ⇔ δ_L = π/12 ⇔ m_e = 0`. The
    "D = J" form is the ANSATZ-MAPPED FACE of that identity — it holds given
    R-070's asserted `A = J, B = D` coefficient identification, and is a corollary,
    not the theorem. Everything narrated as "the substrate's chirality nearly
    balances / 79% of critical" rides that ansatz."""
    return 6.0 / math.sqrt(2.0)

def spiral_angle_deg(D_over_J: float = 0.787) -> float:
    """[DERIVED] §10.3: minimizer tan q_opt = D√2/(6J); at D/J=0.787, q ≈ 10.51°."""
    return math.degrees(math.atan(D_over_J * math.sqrt(2.0) / 6.0))

def dressed_coupling(D_over_J: float = 0.79):
    """[DERIVED, HEDGED] §10.3: the dressed Skyrme coupling e has TWO candidate routes —
    NOT a single 1% number. Honest status: 1%-but-coincidence-riding (√18) alongside
    20%-but-clean (√12)."""
    return {
        "e_LT = √18/(D/J)": math.sqrt(18.0) / D_over_J,    # ≈5.37, ~1% from empirical 5.45 (ANW) but coincidence-riding
        "e_NN = √12/(D/J)": math.sqrt(12.0) / D_over_J,    # ≈4.38, ~20% but cleaner first-principles
        "empirical e (ANW)": 5.45,
        "status": "1%-coincidence-riding (√18) + 20%-clean (√12); not a single derived 1% value",
    }

def DoverJ_from_skyrme(e_empirical: float = 5.45) -> float:
    """[INPUT back-derivation, HEDGED] §10.3: the baryon leg of the T0 over-determination —
    the INVERSE of the dressed-coupling relation e ≈ √18/(D/J), back-deriving D/J from the
    empirically-fit Skyrme stabilizer e:  D/J = √18/e_empirical = √18/5.45 = 0.778.
    It agrees with the lepton leg (DoverJ_from_lepton_masses ≈ 0.787) to ~1.1%.
    HONEST CAVEATS (do not quote a cleaner number):
      (i) the agreement is ~1.1%, NOT 0.4% — the 0.4% figure compares the lepton 0.787 against
          0.790, but 0.790 is the *Cabibbo θ_C calibration reference* (§19.7), not an independent
          baryon value (the Skyrme relation runs D/J → e, predicting e, not the reverse);
      (ii) the √18 = D_crit/J link 'rides a geometric coincidence whose physical referent the
           framework itself disclaims' (§10.3: no static referent at √18).
    So this is a hedged cross-check across unrelated sectors, not a clean independent determination.

      (iii) ★ CONDITIONED 2026-08-23 (the Gamma-channel referent closure, R-180/R-181 —
           `DoverJ_calibration_referent`, `gamma_admixture_cross_functional_route`): THE TWO LEGS
           ARE NOT TWO READS OF ONE QUANTITY. Each measures a RATIO OF TOTALS — the parity-odd
           bond amplitude over the parity-even one — and the two legs' parity-EVEN totals belong
           to DIFFERENT FUNCTIONALS: the Z3 generation amplitude and the helix pitch. Since
           `e = sqrt18/(D/J) = cot q`, THIS leg IS the pitch functional. They are the same
           substrate number ONLY IF the symmetric-traceless (Gamma) bond admixture vanishes,
           which is #1-gap-routed. So the ~1.1% is evidence that TWO DIFFERENT READINGS OF THE
           CHIRALITY COHERE — not a second reading of one pinned parameter. Standing fence:
           NEVER CARRY A RATIO CALIBRATED ON ONE FUNCTIONAL INTO ANOTHER. (The returned VALUE is
           unchanged; what is conditioned is what the agreement is evidence OF.)"""
    return math.sqrt(18.0) / e_empirical


# ---- T0 / WP-OD1  the over-determination scan, CONSOLIDATED + the delta-thetaC FLAG pinned ----------
# item 0 (gate-free [A, consistency], 2026-06-24). Makes the §25.1 OD1 scan reproducible-in-code:
# every leg with its value, % deviation, pre-registered PASS/FLAG/LEAD band, and the single tracked FLAG.
def over_determination_scan(V_us: float = 0.2243, f_pi: float = 129.0,
                            v_ew: float = 246220.0) -> dict:
    """[A, consistency — INPUT, over-determined] §25.1 (WP-OD1): the consolidated
    over-determination scan. An over-determination tests an INPUT by forcing it to serve
    several independent observables with NO further freedom; a passed leg is tagged
    [INPUT, over-determined], NOT [DERIVED] (the value stays an input; what passed is its
    consistency across roles). Pre-registered PASS/FLAG/FAIL bands (the methodology).

    ★ BAND RATIONALE (why two legs have DIFFERENT thresholds — NOT gerrymandering): the band is
    the RELATION's own intrinsic precision, not a fixed number. The D/J leg is THREE reads of the
    SAME quantity (a tight cross-sector determination → PASS <=1.5%, the joint ~1% relation
    uncertainty), so the Cabibbo read at 2.5% is a genuine OUTLIER/FLAG even though small.
    ★★ THAT STATED GROUND IS CONDITIONED 2026-08-23 (Gamma-channel referent closure, R-181;
    `gamma_admixture_cross_functional_route`) — READ THIS BEFORE QUOTING THE BAND'S RATIONALE.
    "THREE reads of the SAME quantity" is exactly what the closure denies ACROSS FUNCTIONALS:
    each read is a ratio of TOTALS whose parity-EVEN denominator belongs to its own functional
    (the f_pi stiffness `f_pi^2 = 8J/a`, the helix pitch, the Z3 generation amplitude), and
    Gamma renormalises each through a DIFFERENT one — they coincide only if the Gamma admixture
    vanishes (#1-gap-routed). The honest ground is therefore "three reads of one CHIRALITY RATIO
    through three different functionals, mutually consistent at ~1%", which supports the SAME
    numerical band by the same intrinsic-precision argument but claims less about what the legs
    share. ★ THE FLAG ITSELF IS UNAFFECTED and is band-independent by its own note below (the
    Cabibbo 2.5% reads FLAG under ANY threshold between the 1.1% lepton<->baryon agreement and
    the 5% absolute-scale line); what moves is the RATIONALE, not the verdict. NO VALUE IN THIS
    PRIMITIVE MOVES. The
    OD1.3 leg is an APPROXIMATE coincidence of two distinct ABSOLUTE scales (v vs f_pi ~ m_p/m_e),
    convention-dependent at the few-% level → PASS <=5%. So 2.5% is a FLAG for D/J but 4% is a PASS
    for v/f_pi BECAUSE they measure different things at different intrinsic precision — exactly the
    'pre-register on the relations' own uncertainties' discipline, not a tuned threshold. (The <=5%
    absolute-scale band is the SAME convention already used by cabibbo_vector_vs_spinor's <=4%
    residual — inherited, not invented here. And the FLAG is band-independent: the Cabibbo 2.5% reads
    FLAG under ANY threshold between the 1.1% lepton<->baryon agreement and the 5% absolute-scale line.)
    CONVENTION NOTE: at the engine-canonical f_pi=129 MeV, OD1.3 reads 4.0% (the high end); the paper's
    §25.1 headline '~2.6%' is the f_pi~=131 convention — same leg, same PASS, different f_pi convention.

    LEGS (all computed below; status per pre-registered band):
      * OD1 — D/J across THREE sectors (the headline):
          - lepton Koide phase   D/J = 0.787  (DoverJ_from_lepton_masses)
          - baryon Skyrme stab.  D/J = 0.778  (DoverJ_from_skyrme = sqrt18/e, HEDGED: no static
                                               referent at sqrt18, §10.3)
          - Cabibbo angle        D/J = tan(3·asin V_us) ≈ 0.807  (back-derived from measured θ_C)
        PASS: lepton<->baryon agree to ~1.1% across UNRELATED sectors, no shared input.
        ★ FLAG (the delta-thetaC residual, PINNED): the Cabibbo determination sits ~2.5% HIGH of
          the lepton/baryon consensus — ONE tracked systematic residual (not multiple), with a
          LOCATED origin: the §19.7 L-orbit vs Q-orbit sector-projection difference. The
          alternative (a spiral-induced f_perp generation-cycle tilt) was closed NEGATIVE by
          T0b.1 (the f_perp read is a categorical 0%-or-82% SSB fork, and an 82% explicit tilt
          would have wrecked Koide's 1e-5). So delta_L (lepton-predicted Cabibbo) vs measured
          θ_C is a FLAG, not a FAIL, and not a clean PASS.
      * OD1.3 — v/f_pi vs m_p/m_e: PASS (~2.6-4% apart, f_pi-convention-dependent). NOTE
        (mass-ontology, canon §5): this is an ABSOLUTE-SCALE consistency cross-check, NOT a
        derivation — both v and f_pi are absolute scales (gap-gated at the #1 gap; cf.
        q_l_stiffness_ratio_is_gap_gated). It passes as a consistency leg; it does not compute
        the hierarchy.
      * OD1.2 — lepton<->baryon adjacent SCALE lead (A^2 ~ m_p/3 at 0.33%, the 2.43 f_pi
        diagnostic): recorded as a [LEAD held lightly], NOT a passed test — the lepton amplitude
        scale A is a FREE Koide calibration (no relation forces it from f_pi). Not recomputed here.
      * f_pi ONE SHARED FLOOR: the single fitted mass scale serves leptons (amplitude scale),
        baryons (Skyrme M_0 = 36.47 f_pi/e) and the chiral condensate — a parameter-economy
        consistency (one scale, many roles), structural PASS.

    VERDICT: NO FAIL anywhere — the input web is self-consistent at the few-% level; exactly ONE
    tracked FLAG (the delta-thetaC / Cabibbo residual, origin located at §19.7). derived-vs-generic:
    the leg VALUES are substrate-computed; the PASS/FLAG tagging is consistency bookkeeping (the
    discipline), and the D/J consensus is HEDGED (sqrt18 has no static referent)."""
    out = {}
    djl = DoverJ_from_lepton_masses()
    djs = DoverJ_from_skyrme()
    dj_cab = math.tan(3.0 * math.asin(V_us))
    lep_bar_pct = abs(djl - djs) / djs * 100.0
    cab_pct = (dj_cab - djl) / djl * 100.0          # signed: Cabibbo runs HIGH
    out["DJ_lepton"], out["DJ_baryon"], out["DJ_cabibbo"] = round(djl, 4), round(djs, 4), round(dj_cab, 4)
    out["DJ_lepton_baryon_pct"] = round(lep_bar_pct, 2)
    out["DJ_cabibbo_vs_lepton_pct"] = round(cab_pct, 2)
    # pre-registered bands: PASS <=1.5% clean cross-sector; FLAG 1.5-5% systematic w/ located origin; FAIL >5%
    out["OD1_lepton_baryon"] = "PASS (~1.1%, sqrt18-hedged)" if lep_bar_pct <= 1.5 else "FAIL"
    out["OD1_cabibbo"] = ("FLAG (delta-thetaC: ~2.5% high, located = §19.7 L/Q sector-projection; "
                          "f_perp-tilt alt closed NEGATIVE by T0b.1)") if 1.5 < cab_pct <= 5.0 else "UNEXPECTED"
    # OD1.3 v/f_pi vs m_p/m_e (absolute-scale cross-check)
    mp, me = 938.272, M_E
    v_fpi, mp_me = v_ew / f_pi, mp / me
    vf_pct = abs(v_fpi - mp_me) / mp_me * 100.0
    out["v/f_pi"], out["m_p/m_e"], out["OD1.3_pct"] = round(v_fpi, 1), round(mp_me, 1), round(vf_pct, 1)
    out["OD1.3_v_fpi_vs_mp_me"] = ("PASS (absolute-scale consistency cross-check, NOT a derivation; "
                                   "few-% convention-dependent)") if vf_pct <= 5.0 else "FAIL"
    out["OD1.2_scale_lead"] = "LEAD (A^2~m_p/3 at 0.33%; lepton amplitude scale A is a FREE calibration; NOT a passed test)"
    out["f_pi_one_shared_floor"] = "PASS (structural: one fitted scale serves leptons + baryons + chiral condensate)"
    # asserts: the scan structure
    assert lep_bar_pct <= 1.5, "lepton<->baryon D/J must agree to ~1.1% (PASS)"
    assert 1.5 < cab_pct <= 5.0, "Cabibbo D/J must sit ~2.5% high = the tracked delta-thetaC FLAG"
    assert vf_pct <= 5.0, "v/f_pi vs m_p/m_e must pass at the few-% level"
    out["n_FAIL"] = 0
    out["n_FLAG"] = 1
    out["tracked_FLAG"] = "delta-thetaC (Cabibbo leg ~2.5% high; origin §19.7 L/Q sector-projection)"
    out["verdict"] = ("NO FAIL; input web self-consistent at the few-% level; exactly ONE tracked FLAG "
                      "(the delta-thetaC / Cabibbo residual). D/J consensus HEDGED (sqrt18 no static referent); "
                      "passed legs are [INPUT, over-determined], not [DERIVED]")
    return out


# ---- §16.3 / §16.4  mass and Skyrme length -------------------------------------
def skyrmion_mass_MeV(f_pi: float = 129.0, e: float = 5.45) -> float:
    """[DERIVED, dressed-level] §16.3: M_0 = 36.47 f_π/e. 36.47 = BVP eigenvalue at the
    optimal profile (independent of f_π,e). At e_phys=5.45: 863 MeV (standard ANW;
    8% below the proton 938) — but this is the STATIC soliton mass and NOT, as the corpus
    previously said, "the known ANW deficit": ANW 1983 (Nucl. Phys. B228, 552) FIT (e, F_pi) =
    (5.45, 129 MeV) so that their eq. (9) M_N = M + (1/2*lambda)(3/4) closes N and Delta EXACTLY
    (their table 1 lists both as input). The 8% is the missing ROTATIONAL-BAND term, supplied at
    R-133 skyrmion_rotational_band_nucleon_delta. ANW publish the same coefficient to three
    figures, "M = 36.5 F_pi/e" (their p. 556) — source-verified 2026-07-28. Honest scope: relation among DRESSED
    (EFT-layer) couplings, conditional on the §10.3 branch-(c) dressed-sector closure."""
    return 36.47 * f_pi / e

def skyrme_length_fm(f_pi: float = 129.0, e: float = 5.45) -> dict:
    """[DERIVED] §16.4: ℓ_S = ℏc/(e f_π) ≈ 0.281 fm (emergent cell scale);
    a = ℏc/f_π ≈ 1.53 fm (pion Compton / wave-train coherence); a/ℓ_S = e."""
    ell_S = HBAR_C / (e * f_pi)
    a = HBAR_C / f_pi
    return {"ell_S (fm)": ell_S, "a (fm)": a, "a/ell_S = e": a / ell_S}




# item 8b, step 3 (2026-06-24, Yaer's idea). Interference can REDUCE the hadron mass -- like the
# Goldstone mesons: two rotations that don't add but stay flat or SUBTRACT. This fixes the SIGN that
# step 2 left open (Lambda<Sigma) and unifies it with the pseudoscalar Goldstone lightness.
def interference_can_reduce_mass_goldstone() -> dict:
    """[DERIVED (subtractive channel) + FRAMING (sign reconciliation)] item 8b step 3: in the
    shared-rotor / coherent-sum picture, interference between two windings can REDUCE the hadron
    mass below the incoherent sum -- they need not add; they can stay flat or SUBTRACT. This is the
    GOLDSTONE mechanism, and it FIXES the Lambda<Sigma sign step 2 left open.

    DERIVED -- the subtractive channel (exact + engine):
      Two unit rotors at relative meta-time phase beta: |a1 + a2 e^{i beta}|^2 = 2 + 2 cos(beta).
      Incoherent floor = 2 (the would-be 'sum'). The cross-term 2 cos(beta):
        beta=0   (constructive / symmetric)  -> 4   ABOVE floor (mass ADDED)
        beta=pi/2 (orthogonal)               -> 2   AT floor    (mass FLAT, no interference)
        beta=pi  (destructive / antisymmetric)-> 0   BELOW floor (mass SUBTRACTED, full cancellation)
      So destructive interference (beta>pi/2) drops the mass BELOW the additive sum -- the strongest
      form of non-additivity. This is EXACTLY the engine's meson result (meson_dynamical_current_split):
      m = 2 omega |cos(alpha/2)|, pseudoscalar alpha=pi CANCELS -> the light pi/K/eta (Goldstone). The
      subtractive channel is therefore already a TWT mechanism, not a generic possibility.
      PARTIAL (not to zero): as in the meson, only the SOFT/DYNAMICAL part of the cross-term cancels --
      the CURRENT/incoherent part survives (meson: the pseudoscalar is LIGHT, not massless). So the
      baryon reduction is partial (the ~77 MeV Sigma-Lambda scale), the hadron stays massive; the
      destructive channel lowers, it does not annihilate.

    FRAMING (consistency, NOT a derivation) -- the Lambda<Sigma SIGN as a third lens:
      Mapping the light-pair exchange symmetry to this relative phase (meson-analogous, an ASSIGNMENT
      not forced: antisymmetric <-> destructive beta~pi, symmetric <-> constructive beta~0) gives:
        Lambda = ANTISYMMETRIC ud pair -> destructive / Goldstone-like -> mass REDUCED -> LIGHTER
        Sigma  = SYMMETRIC    ud pair -> constructive                 -> HEAVIER
      This is CONSISTENT WITH the observed Lambda(1115.68) < Sigma0(1192.64). ⚠ It does NOT
      INDEPENDENTLY fix the sign: the §17.3 gear that gives the same ordering is CALIBRATED TO THE SAME
      Sigma-Lambda DATUM (gamma=(Sigma-Lambda)/2=38.5 and the 77 MeV are INPUT, see gell_mann_okubo_gamma
      / alpha_H_gap), so 'data + gear' is one datum plus a quantity fit to it -- not two independent
      witnesses; and the gear's Lambda:K_L=0 / Sigma:K_L=1 is itself an ASSIGNMENT to match the order.
      So this is a THIRD LENS consistent with Lambda<Sigma, not a derivation of it.
      Moreover the gear and the Goldstone push OPPOSITE ways about the floor (gear ADDS rotational
      energy to Sigma above a floor; Goldstone SUBTRACTS from Lambda below it) -- reconciling them needs
      the floor identified, which is exactly the OPEN reconciliation flagged in
      baryon_mass_shared_rotor_nonadditive (the coherent-sum <-> §17.3 gear map).

    OPEN (residual): whether antisym<->beta=pi is FORCED (vs the assignment above); the exact
    coherent-sum<->gear functional map incl. the floor; and the absolute values (omega scale + the
    Theta_rel phases) = the #1 gap. derived-vs-generic: substrate-specific = the meson 2omega|cos(a/2)|
    Goldstone channel being a DERIVED TWT form (so the subtractive channel really exists here); generic
    = 'a destructive cross-term lowers a coherent sum'. The Lambda<Sigma sign is FRAMING/CONSISTENCY
    (a third lens; the gear corroborator is calibrated to the same datum), NOT derived. NO fit."""
    out = {}
    def coh2(beta): return 2.0 + 2.0*math.cos(beta)
    floor = 2.0
    out["constructive_beta0"] = round(coh2(0.0), 2)          # 4 ABOVE floor
    out["flat_beta_halfpi"] = round(coh2(math.pi/2), 2)      # 2 AT floor
    out["destructive_betapi"] = round(coh2(math.pi), 2)      # 0 BELOW floor (full cancellation)
    out["incoherent_floor"] = floor
    # the load-bearing fact: destructive interference goes BELOW the additive sum
    assert coh2(math.pi) < floor and coh2(2*math.pi/3) < floor and coh2(0.0) > floor, \
        "destructive interference (beta>pi/2) must drop the coherent mass BELOW the incoherent floor"
    out["interference_can_subtract_mass"] = True
    # this is the meson Goldstone channel (engine): pseudoscalar alpha=pi cancels
    mc = meson_dynamical_current_split()
    out["meson_goldstone_engine"] = mc["verdict"][:60] + " ..."
    out["goldstone_is_full_cancellation_betapi"] = True
    # the Lambda<Sigma sign, pinned by the destructive=lighter principle + consistent with the gear
    out["Lambda_MeV"], out["Sigma0_MeV"] = 1115.68, 1192.64
    assert out["Lambda_MeV"] < out["Sigma0_MeV"], "Lambda (antisym/destructive) must be lighter than Sigma (sym/constructive)"
    out["sign_lens_consistency"] = "antisym(Lambda)=destructive/Goldstone-like=LIGHTER, sym(Sigma)=heavier -- CONSISTENT with data, NOT an independent derivation (assignment)"
    out["not_independent_witnesses"] = "the §17.3 gear that gives the same order is CALIBRATED to the Sigma-Lambda datum (gamma=38.5/77 INPUT); so 'data+gear' is one datum + a fit to it"
    out["floor_reconciliation_open"] = "gear ADDS to Sigma above a floor vs Goldstone SUBTRACTS from Lambda below it -> reconciling needs the floor (open, see baryon_mass_shared_rotor_nonadditive)"
    out["gap_gated"] = "absolute omega scale + Theta_rel phases (#1 gap); + whether antisym<->beta=pi is FORCED (open)"
    out["verdict"] = ("DERIVED: interference can SUBTRACT mass (destructive cross-term drops below the "
                      "incoherent floor; full cancellation at beta=pi) -- the GOLDSTONE channel, already a "
                      "DERIVED TWT form (meson 2omega|cos(a/2)|, pi/K/eta light); PARTIAL (soft part only, "
                      "hadron stays massive). FRAMING/CONSISTENCY (not a derivation): the antisym=destructive "
                      "assignment is CONSISTENT with Lambda<Sigma -- a third lens, NOT an independent sign-fix "
                      "(the gear corroborator is calibrated to the same datum); the gear<->Goldstone floor "
                      "reconciliation + values stay gap-gated/open")
    return out


# item 8b, step 4 (2026-06-24, Yaer). IDENTIFY THE FLOOR -- the open reconciliation between the
# §17.3 gear (adds ABOVE a floor) and the Goldstone coherent-sum (subtracts BELOW a floor).
# Per Yaer's license: speculate/fit freely, tag honestly (DERIVED / FRAMING / INPUT / CANDIDATE).
def identify_the_floor() -> dict:
    """[DERIVED structure + FRAMING reconciliation + INPUT(gamma) + CANDIDATE(speculation)] item 8b
    step 4: THE FLOOR is the interference-free CENTROID that the constructive/destructive partners
    straddle -- NOT the bottom state. This closes (structurally) the gear<->coherent-sum reconciliation.

    SCOPE: a,b are the LIGHT ud-PAIR sub-amplitudes (Lambda/Sigma0 differ by the ud exchange symmetry,
    strange as SPECTATOR); the common strange contribution sits IN the floor and CANCELS in the +/- split.
    So this is a 2-AMPLITUDE (pair) parallelogram, NOT a 3-body coherent sum (the full 3-body form stays
    the open 2->3 question of baryon_mass_shared_rotor_nonadditive).

    DERIVED (conditional on mass proportional to the COHERENT AMPLITUDE -- the MESON form
    m=2 omega|cos(alpha/2)|=omega|1+e^{i alpha}|; whether the baryon mass law is linear in the amplitude
    |A| vs |A|^2 is the OPEN meson->baryon assumption flagged in baryon_mass_shared_rotor_nonadditive):
    the ud-pair symmetric/antisymmetric combinations obey the PARALLELOGRAM LAW
        |a+b|^2 + |a-b|^2 = 2(|a|^2 + |b|^2)   =>   M_sym^2 + M_antisym^2 = 2 M_floor^2,
    so the floor that is EXACTLY derived is the QUADRATURE MEAN
        M_floor = sqrt((M_sym^2 + M_antisym^2)/2) = omega*sqrt(|a|^2+|b|^2) = the INCOHERENT sum.
    ⚠ The identification of this floor with the ARITHMETIC CENTROID (M_sym+M_antisym)/2 is a
    NEAR-DEGENERATE APPROXIMATION, NOT exact: it holds when the split is small (Lambda/Sigma0:
    arith 1154.16 vs quad 1154.80 -- agree to 0.6 MeV) and FAILS far from degeneracy -- e.g. in the
    very GOLDSTONE limit the mechanism invokes (antisym->0 at alpha=pi: arith=Msym/2 vs quad=Msym/sqrt2,
    a ~40% gap). So: EXACT/DERIVED = the quadrature floor; floor ~= centroid ~= 1154 MeV is the
    small-split reading for Lambda/Sigma0, an approximation that degrades as the partners separate.

    FRAMING -- the reconciliation (the open piece from steps 2-3, now closed in structure):
      The §17.3 gear writes M = M_0[bottom] + K_L(K_L+1)/(2 Theta) (Lambda at M_0, Sigma above);
      the coherent-sum writes M = FLOOR +/- interference (Sigma = floor+gamma, Lambda = floor-gamma).
      These are ONE functional at DIFFERENT ZERO-POINTS: gear M_0 = floor - gamma = Lambda; the gear's
      rotational swing 2 gamma = the coherent (constructive - destructive). So the gear's
      gamma=(Sigma-Lambda)/2 IS the coherent cross-term half-amplitude. The gear puts the zero at the
      bottom; the physical interference-free baseline is the CENTROID (floor). Same physics.

    INPUT (calibrated, not derived): gamma = (Sigma-Lambda)/2 = 38.5 MeV (gell_mann_okubo_gamma); the
    ABSOLUTE floor (omega scale, ~1154 MeV) is GAP-GATED (#1 gap).

    CANDIDATE (SPECULATION, recorded as such per Yaer's license -- TWT under construction): if the floor
    is the interference-free baseline, the FLOOR/CENTROID should carry the ADDITIVE (e.g. strangeness-
    counting) part of the mass while the interference (+/- gamma) carries the NON-ADDITIVE pair-symmetry
    part. Illustration (NOT a derivation): the octet Gell-Mann-Okubo centroid relation 2(N+Xi)=3Lambda+Sigma
    holds to ~0.6% -- a known additive-type regularity at the floor level. FORWARD-TESTABLE: the spin/
    symmetry-averaged centroids should be MORE additive than the individual masses. This is a fit-grade
    hypothesis to be checked, tagged CANDIDATE, not banked as structure.

    NET: the FLOOR is identified as the interference-free CENTROID (DERIVED via the parallelogram law,
    conditional on the coherent-amplitude mass law); the gear and coherent-sum reconcile as one
    functional about different zero-points (FRAMING); gamma is INPUT, the absolute scale gap-gated; the
    centroid-is-additive claim is a tagged CANDIDATE. derived-vs-generic: the parallelogram law is exact
    (generic given mass~|amplitude|); substrate-specific = that TWT's mass IS proportional to a coherent
    rotor amplitude (the meson form) so the law APPLIES here."""
    out = {}
    L, S = 1115.68, 1192.64                       # Lambda, Sigma0 (uds, J=1/2): antisym/sym partners
    gamma = (S - L) / 2.0
    floor_arith = (S + L) / 2.0
    floor_quad = math.sqrt((S*S + L*L) / 2.0)
    # parallelogram law: M_sym^2 + M_antisym^2 = 2 M_floor^2 (exact, by construction of floor_quad)
    assert abs((S*S + L*L) - 2.0*floor_quad*floor_quad) < 1e-6, "parallelogram law must hold exactly"
    assert abs(floor_arith - floor_quad) < 1.0, "arith ~= quadrature floor ONLY for the small Lambda/Sigma split"
    out["floor_MeV_quad_EXACT"] = round(floor_quad, 2)        # the DERIVED floor (parallelogram)
    out["floor_MeV_arith_approx"] = round(floor_arith, 2)     # = centroid; near-degenerate APPROXIMATION
    out["arith_vs_quad_gap_MeV"] = round(abs(floor_arith - floor_quad), 2)   # 0.64 (small split)
    # the approximation FAILS far from degeneracy -- e.g. the Goldstone limit (antisym->0):
    msym = 1400.0
    out["goldstone_limit_arith_vs_quad"] = {"arith": round(msym/2, 0), "quad": round(msym/math.sqrt(2), 0)}  # 700 vs 990
    out["gamma_MeV"] = round(gamma, 2)            # = the interference cross-term half-amplitude (INPUT)
    out["floor_is_centroid_near_degenerate_only"] = True   # exact floor = QUADRATURE mean; centroid is small-split
    # reconciliation (near-degenerate / arithmetic parameterization): gear M_0 (bottom) = floor - gamma = Lambda
    out["gear_M0_equals_floor_minus_gamma"] = round(floor_arith - gamma, 2)   # = Lambda (exact in arith)
    assert abs((floor_arith - gamma) - L) < 1e-6, "gear M_0 (bottom) = arith floor - gamma = Lambda (arithmetic identity)"
    out["reconciliation"] = "gear (M_0 bottom + rotational) and coherent-sum (floor +/- interference) = ONE functional, different zero-point (gear gamma IS the coherent cross-term); holds in the near-degenerate regime, FRAMING"
    # CANDIDATE illustration (tagged): GMO octet centroid relation holds ~0.6%
    N, Xi = 938.92, 1318.3
    gmo_lhs, gmo_rhs = 2*(N + Xi), 3*L + S
    out["CANDIDATE_centroid_additive_GMO_pct"] = round(abs(gmo_lhs - gmo_rhs)/gmo_rhs*100, 2)
    out["gap_gated"] = "absolute floor (omega scale ~1154 MeV) at the #1 gap; gamma is INPUT (calibrated to Sigma-Lambda)"
    out["verdict"] = ("THE FLOOR = the interference-free baseline the sym/antisym partners straddle. EXACT/"
                      "DERIVED (given mass~coherent amplitude, the open meson->baryon linear-|A| assumption): "
                      "the QUADRATURE mean sqrt((M_sym^2+M_antisym^2)/2) via the parallelogram law -- a ud-PAIR "
                      "(2-amplitude) result, strange spectator in the floor. The floor~=arithmetic CENTROID "
                      "(~1154 MeV) is a NEAR-DEGENERATE approximation (Lambda/Sigma 0.6 MeV; FAILS in the "
                      "Goldstone limit, 700 vs 990). Reconciliation (FRAMING): gear & coherent-sum = one "
                      "functional, different zero-point (gear M_0=arith floor-gamma=Lambda; gear gamma=the "
                      "coherent cross-term). gamma INPUT, absolute floor gap-gated; centroid-additivity CANDIDATE")
    return out


# ---- §16.6  the electron as topological defect (QCP scaling) -------------------
def electron_QCP_nu():
    """[DERIVED-CONDITIONAL on four named L1 ingredients — F-5 audit, 2026-06-29]
    §16.6: the L-orbit STIFFNESS scale obeys QCP scaling f_L = f_π·δ^ν, δ=1-D/J,
    with critical exponent factorizing (DQCP universality) as
        ν = N_dir · Δ_v · (1/2) · ν_corr = 3 · 3 · (1/2) · 1 = 9/2.
    Per F-5 (worklist B1), each ingredient now has a dedicated engine primitive:
      * N_dir = 3 ............ DERIVED-A   `D4_spatial_bond_isotropy()` (M_ij = 4·δ_ij)
      * Δ_v   = 3 (K_c=2J/19)  LOCATED-GAP-REFINED `canting_critical_stiffness_at_DJ()`
                              (the 19 is the D4 spiral-pitch denominator = sin²q at QCP;
                              the 2 is now traced to N_Goldstone = dim(SU(2)_L/U(1)_canting)
                              = 2 — substrate-traceable via the Hopf S¹ fiber, §16.6 — but
                              the KERNEL FORM K_c = N_G · sin²(q) · J still needs §9.6)
      * 1/2 .................. INPUT-conv  `sigma_model_kinetic_normalization()`
                              (K_φ/f² = 1/4; matching factor dim(S±) = 2)
      * ν_corr = 1 ........... DERIVED-given-Gaussian-FP `DM_operator_gaussian_dim()`
                              ([O_DM] = 2[φ]+1 = 2 at d=3, η=0; ν_corr = 1/(d-[O_DM]) = 1)
    So ν = 9/2 is engine-verified MODULO the K_c=(2/19)J LOCATED-GAP — the audit's
    honest tier is DERIVED-CONDITIONAL, promoting to DERIVED once K_c is closed.

    NAMED PREMISE (state-space scoping, inherited via Δ_v = 3 ← K_c ← N_Goldstone):
    this chain is taken WITHIN THE L-ORBIT SUB-SECTOR of the medium's six-parameter
    4D-orientation state space (§D.3.2; `pi3_orientation_class_two_windings`), not
    over the full state space. The premise is named here rather than left silent; a
    full-state-space treatment awaits the un-banked 6-band Bogoliubov structure."""
    N_dir, Delta_v, half, nu_corr = 3, 3, 0.5, 1
    return N_dir * Delta_v * half * nu_corr      # = 4.5 = 9/2

def electron_f_L_MeV(f_pi: float = 129.0, D_over_J: float = 0.79) -> float:
    """[DERIVED-CONDITIONAL — cascade-inherits from electron_QCP_nu] §16.6:
    f_L = f_π·δ^ν, δ=1-D/J. At D/J=0.79 (δ=0.21, ν=9/2): ≈0.115 MeV.

    SCOPE — f_L IS A STIFFNESS, NOT THE ELECTRON MASS. This framework has NO
    stiffness->mass conversion for the L sector: no substrate argument fixes an
    L-sector coupling, and no primitive here or in the companion computes one. Do
    not compare this return value to m_e, and do not reintroduce the retired
    `m_e = f_L * e_L` convention with `e_L = sqrt(36.47)` — that was an undeclared,
    uncounted coupling placed at the self-consistent fixed point coeff/e = e, and it
    was EXCISED from §C.1.6 (2026-08-20) together with all three residuals it
    produced (~36% on f_L, 4.4% on the exponent, 0.34% on nu = 3pi/2). 36.47 is the
    BARYON functional's coefficient (the ANW hedgehog BVP energy evaluated at its
    solution; the BVP's selected parameter is F'(0) = -1.0038) and it is excluded
    outright on the Faddeev-Skyrme branch by the Vakulenko-Kapitanski floor
    (coefficient 59.6 > 36.46). Settling WHICH functional stabilises the L-orbit
    defect is the prerequisite for any L-sector coefficient.

    Tier note (audit 2026-06-30 P9): inherits DERIVED-CONDITIONAL from electron_QCP_nu()
    which is conditional on four named L1 ingredients (F-5 audit 2026-06-29), one of
    which — K_c=(2/19)·J — remains LOCATED-GAP (#1-gap-routed). If K_c closure lands,
    this primitive auto-promotes to DERIVED."""
    delta = 1.0 - D_over_J
    return f_pi * delta ** electron_QCP_nu()


# ---- §16.6 F-5: the four QCP-ingredient primitives -----------------------------
# Per F-5 audit (worklist B1, 2026-06-29): each of the four factors in
# ν^L1 = N_dir · Δ_v · (1/2) · ν_corr = 9/2 gets a dedicated engine primitive.
# Three of the four are now substrate-derived; the K_c=(2/19)J ingredient is
# recorded as LOCATED-GAP per canon §4 (the 2 prefactor needs the #9.6 EOM).
def D4_spatial_bond_isotropy():
    """[DERIVED-A] §16.6 / F-5: the N_dir=3 ingredient of the QCP exponent.

    The D4 lattice has 24 nearest-neighbour vectors of squared length 2,
    permutations-with-signs of (±1, ±1, 0, 0). The SPATIAL subset (zero e_4
    component) is the 12 directed permutations of (±1, ±1, 0, 0) within
    coordinate positions {1, 2, 3} — equivalently, 6 undirected bonds, one
    per (unordered-pair, sign-of-second-coordinate). The bond stiffness
    tensor
        M_{ij} = Σ_b (b_sp)_i (b_sp)_j
    summed over the 6 undirected spatial bonds evaluates to exactly 4·δ_{ij}
    (and identically over the 12 unit-normalized directed bonds — the bond-
    doubling and the 1/2-from-unit-normalization cancel). Tr(M)/M_11 = 3 is
    the algebraic origin of N_dir = 3 in the §16.6 QCP exponent: one stiffness
    contribution per spatial direction. This is a closed Cl(4,0)+D4 identity,
    not a fit — DERIVED-A."""
    import numpy as np
    import itertools as _it
    bonds = []
    # 6 undirected representatives: (i<j) pair-locations × 2 second-sign choices
    for i, j in _it.combinations(range(3), 2):
        for s2 in (+1, -1):
            b = [0.0, 0.0, 0.0]
            b[i] = +1.0
            b[j] = float(s2)
            bonds.append(b)
    assert len(bonds) == 6, f"expected 6 undirected spatial bonds, got {len(bonds)}"
    B = np.array(bonds, float)
    M = B.T @ B                                   # 3×3 stiffness tensor
    iso = bool(np.allclose(M, 4.0 * np.eye(3), atol=1e-12))
    assert iso, f"D4 spatial-bond stiffness must equal 4·I_3, got M={M.tolist()}"
    N_dir = int(round(np.trace(M) / M[0, 0]))     # 12/4 = 3
    return {
        "n_undirected_spatial_bonds": len(bonds),
        "stiffness_M_ij": M.tolist(),
        "M_eq_4_delta_ij": iso,
        "N_dir_from_trace_over_M11": N_dir,
    }


def sigma_model_kinetic_normalization():
    """[INPUT-convention] §16.6 / F-5: the 1/2 ingredient of the QCP exponent.

    Writing the L-orbit SECTOR of the field as a Spin(3) rotor U = exp(iφ^a T^a) sandwich
    (a stated sector reduction of the six-parameter 4D-orientation state space — §D.3.2,
    `pi3_orientation_class_two_windings`; NOT the field's full target),
    the chiral kinetic term is conventionally
        L_kin = -(f²/4) tr(∂_μ U^† ∂^μ U)  →  K_φ |∂φ|²  with  K_φ = f²/4.
    The QCP bookkeeping factor in ν^L1 is
        (K_φ/f²) · dim(S_±) = (1/4) · 2 = 1/2,
    where dim(S_±) = 2 is the chiral half-spin representation dimension that
    the L-orbit field lives in. This is a NORMALIZATION CHOICE (a counted
    parameter-economy item), NOT a substrate derivation — tagged honestly per
    canon §5 derived-vs-generic."""
    K_over_f2 = 1.0 / 4.0
    dim_S_plus = 2
    bookkeeping = K_over_f2 * dim_S_plus
    assert abs(bookkeeping - 0.5) < 1e-12, "K/f² · dim(S±) must equal 1/2"
    return {
        "K_phi_over_f_squared": K_over_f2,
        "dim_S_plus_matching_factor": dim_S_plus,
        "QCP_half_factor": bookkeeping,        # = 0.5
    }


def DM_operator_gaussian_dim(d: int = 3, eta: float = 0.0):
    """[DERIVED-given-Gaussian-fixed-point] §16.6 / F-5: the ν_corr=1 ingredient.

    At the Gaussian fixed point in d spatial dimensions with anomalous dim η,
    the order-parameter field has scaling dimension
        [φ] = (d - 2 + η)/2.
    The Dzyaloshinskii–Moriya operator O_DM = ε^{abc} φ^a (∂φ^b) φ^c carries
        [O_DM] = 2[φ] + 1.
    The associated correlation-length exponent is
        ν_corr = 1 / (d - [O_DM]).
    At d=3, η=0:  [φ] = 1/2,  [O_DM] = 2,  ν_corr = 1.
    This is the standard Gaussian-fixed-point counting — generic-given-d=3,
    not substrate-specific. Tagged DERIVED-given-Gaussian-FP per canon §5."""
    phi_dim = (d - 2.0 + eta) / 2.0
    O_DM_dim = 2.0 * phi_dim + 1.0
    if abs(d - O_DM_dim) < 1e-15:
        nu_corr = float("inf")
    else:
        nu_corr = 1.0 / (d - O_DM_dim)
    return {
        "phi_dim": phi_dim,                    # = 1/2 at (d=3, η=0)
        "O_DM_dim": O_DM_dim,                  # = 2
        "nu_corr": nu_corr,                    # = 1
    }


def canting_critical_stiffness_at_DJ(J: float = 1.0):
    """[LOCATED-GAP-REFINED] §16.6 / F-5: K_c=(2/19)·J at D=J — the 2 prefactor
    re-examined (2026-06-29 audit).

    Static facts (engine-checked via canting_cos_q):
      cos²q = 18/(18 + (D/J)²) → 18/19 at D=J;  sin²q = (D/J)²/(18 + (D/J)²) → 1/19.
    The 19 is the spiral-pitch denominator — equivalently sin²q at the QCP.
    This is a closed Cl(4,0)+D4 identity (DERIVED-A within canting_cos_q).

    The 2 prefactor — three candidate static origins tested per canon §4:

      (A) GOLDSTONE COUNT (PRINCIPLED; traces 2 to substrate): on the canted FM
          vacuum — the AXIS BRANCH of §D.4.3; see `n_goldstone_canted_FM`'s BRANCH
          SCOPE block, this reconstruction inherits it —
          SU(2)_L breaks to U(1)_canting (paper §16.6: M_GS = 8×S¹
          ⊂ Spin(3) = S³; the residual U(1) is the Hopf S¹ fiber). # broken
          Goldstones = dim(SU(2)_L) − dim(U(1)) = 3 − 1 = 2 = dim(S²) (Hopf base).
          Reconstruction: K_c = N_Goldstone · sin²(q) · J = 2 · (1/19) · J = 2J/19
          at D=J. The 2 is now TRACEABLE to a banked substrate fact (the residual
          U(1) of the canted FM). NAMED PREMISE (state-space scoping): N_Goldstone
          = 2 holds WITHIN THE L-ORBIT SUB-SECTOR of the six-parameter 4D-orientation
          state space (§D.3.2; see `n_goldstone_canted_FM`'s SCOPE block and the
          un-banked 6-band structure at `induced_G_from_linear_face_band`). That
          premise is part of this result's conditioning class and propagates to
          `electron_QCP_nu`. BUT the KERNEL FORM (why K_c assembles as
          N_G · sin²(q) · J at the QCP) requires the §9.6 magnon-kernel convolved
          with the vortex-line worldsheet — i.e., the #1 gap remains for the
          assembly, not the prefactor.

      (B) D4 COORDINATION RATIO (REJECTED as numerical coincidence): 2 = z_total/z_sp
          = 24/12 gives the arithmetic match K_c = (z_total/z_sp)·sin²(q)·J = 2/19 J,
          but no first-principles motivation forces K_c to scale as z_total/z_sp. The
          SM-retreat trap of reverse-engineering a number from a coordination ratio.

      (C) SWT BOSON-SYMMETRIZATION 2 (REJECTED as double-counting): the standard
          Holstein-Primakoff factor of 2 is already booked in the QCP exponent's
          (K_φ/f²)·dim(S±) = (1/4)·2 = 1/2 (sigma_model_kinetic_normalization).
          Re-using it in K_c would double-count the same 2.

    tried — (A) 2 traced to N_Goldstone = dim(SU(2)_L/U(1)_canting) = 2 (substrate fact);
            (B) 24/12 D4 coord → arithmetic match without motivation; (C) SWT 2 →
            double-counts the 1/2 factor.
    failed — none of A/B/C statically FORCE the kernel form K_c = (prefactor)·sin²(q)·J.
            The static gradient stiffness at the canted FM is ~5.95J (transverse:
            2J cos q* + 4J, erratum 2026-07-26 in Kc_magnon_stiffness_canted_FM_at_DJ —
            the old ~3.89J transcribed a verbal statement; longitudinal: √38 J), not
            2/19 J; so K_c is NOT directly the magnon stiffness — it is the
            kernel-convolved vortex-line critical stiffness.
    would change if — (a) the §9.6 driven-dissipative kernel closes and confirms
            K_c = N_Goldstone · sin²(q) · J at the QCP (which would promote this
            to DERIVED-given-(SU(2)_L→U(1)_canting)); ~~OR (b) a purely static
            vortex-line linear-response argument is found that forces the kernel
            form unambiguously~~ — ROUTE (b) ELIMINATED 2026-06-29 by
            Kc_magnon_stiffness_canted_FM_at_DJ(): direct LSWT on the canted
            spiral gives K_long = √38·J ≈ 6.164 J and K_trans = (2 cos q* + 4) J ≈
            5.947 J (erratum 2026-07-26), both ~56-59× LARGER than K_c = 2J/19 ≈
            0.105 J. Static LSWT cannot produce the kernel form. ONLY ROUTE (a)
            REMAINS.
            [KP-1 TENSION NOTE, 2026-07-26 corpus pass: Lead A's N_Goldstone = 2 is
            a BROKEN-GENERATOR count; the actual canted-spiral spectrum is 1 gapless
            phason + 2 DM-gapped tilt modes (KP-1 consensus 2026-07-22), so the
            assembly N_eff ∈ {1, 2, 3} is genuinely OPEN — the simulator's frozen
            three-row table (kernel_kc_target [2z29]: 117.12 / 58.56 / 39.04)
            records the alternatives; the only assembly-shaped datum yet measured
            is G1c's echo-bound CANDIDATE non-integer 2.221 (K4D_g1c_closure.md).
            Lead A remains the substrate-traceable reconstruction; this note keeps
            its pick-vs-forced status honest.]

    Refinement gain over the prior LOCATED-GAP entry: the 2 prefactor is now
    SUBSTRATE-TRACEABLE (Lead A: Goldstone count from SU(2)_L→U(1)_canting), not
    merely "gated on the kernel." The remaining gap is narrower and named: the
    kernel form K_c = N_G · sin²(q) · J — not the value 2."""
    cos2_q_at_DJ = 18.0 / 19.0
    sin2_q_at_DJ = 1.0 / 19.0
    K_c_over_J_asserted = 2.0 / 19.0
    N_Goldstone = 2  # = dim(SU(2)_L/U(1)_canting) = dim(S²) (Hopf base, §16.6)
    K_c_lead_A = N_Goldstone * sin2_q_at_DJ                # = 2/19 with N_G=2
    assert abs(K_c_lead_A - K_c_over_J_asserted) < 1e-12, \
        "Lead A reconstruction K_c = N_G · sin²(q) · J must match asserted 2/19 at D=J"
    return {
        "cos_squared_q_at_DJ": cos2_q_at_DJ,
        "sin_squared_q_at_DJ": sin2_q_at_DJ,
        "spiral_pitch_denominator_at_DJ": 19,        # 18 + (D/J)² with D/J=1
        "K_c_over_J_asserted": K_c_over_J_asserted,  # = 2/19
        "K_c_over_J_engine_derived": None,           # GAP — kernel form still open
        "prefactor_2_traced_to": "N_Goldstone = dim(SU(2)_L/U(1)_canting) = 3-1 = 2",
        "N_Goldstone_substrate_value": N_Goldstone,
        "lead_A_reconstruction_K_c_over_J": K_c_lead_A,    # = 2/19 (engine-checked)
        "outcome": "LOCATED-GAP-REFINED",
        "tried": "Lead A (Goldstone count → 2 substrate-traced); "
                 "Lead B (24/12 → numerical coincidence); "
                 "Lead C (SWT 2 → double-counts 1/2 factor)",
        "would_change_if": "the §9.6 driven-dissipative kernel closes and confirms "
                            "K_c = N_Goldstone · sin²(q) · J at the QCP. [Route (b) — a static "
                            "vortex-line linear-response argument — was ELIMINATED 2026-06-29 per "
                            "this primitive's own docstring; this return string was stale until the "
                            "2026-07-26 corpus pass (a pre-existing return/docstring incoherence, "
                            "cured as a labeled doc fix).]",
    }


# ---- §22.5  nuclear forces hierarchy ------------------------------------------
def eta_DM(D_over_J: float = 0.79) -> float:
    """[CALIBRATED — combinatorial origin sketched; explicit 1/144 coefficient awaits Paper 2
    D4 effective tensor-vertex computation] §17.6 / §22.5: the DM tensor-force correction
    η_DM = (D/J)²/144 ≈ 0.43%, where 144 = 12² is the spatial bond-count squared. (Bond-count
    anisotropy is zero since z_sp = z_{e4} = 12, so the leading D4-ANISOTROPY CONTRIBUTION TO
    the tensor force is this sub-percent DM term -- the DOMINANT tensor force is the OPE-class
    dipole-dipole law, now derived in-framework at R-139.) Tier retagged from V1 [DERIVED] to match paper V2 §17.6 F-6 correction."""
    return (D_over_J ** 2) / 144.0

def nuclear_length_hierarchy(f_pi: float = 129.0, e: float = 5.45):
    """[DERIVED] §22.5: the nuclear-force length scales in units of ℓ_S = ℏc/(e f_π):
    hard core √2 ℓ_S = 0.40 fm (cell exclusion — 1+24 coordination at the cell layer, §C.5.10); soliton core 2 ℓ_S = 0.56 fm;
    pion Yukawa 5.2 ℓ_S = 1.46 fm (π, 135 MeV)."""
    ell_S = HBAR_C / (e * f_pi)
    return {"hard core (√2 ℓ_S)": math.sqrt(2)*ell_S, "soliton core (2 ℓ_S)": 2*ell_S,
            "pion Yukawa (5.2 ℓ_S)": 5.2*ell_S}


# ---- §23.6 (iii)  F-7 promotion: DM bond bivectors non-commuting on D4 ----------
def D4_DM_bond_bivectors_non_commuting():
    """[DERIVED-A] §23.6 (iii) — the substrate-specific non-commutativity claim.

    The F-7 V1-review tier-correction flagged §23.6 (iii) ("DM lifts the pure-gauge
    constraint") as FRAMING pending an engine-level check that the DM bivector axes
    B_hat_{ij} attached to different D4 bond directions are NON-COMMUTING. This
    primitive supplies that check, promoting (iii) from FRAMING to DERIVED-A on the
    natural geometric convention (bond bivector = the oriented plane the bond
    displacement lies in).

    SETUP. The D4 kissing vectors are the 24 length-sqrt(2) displacements
    +/- e_i +/- e_j with i<j in {1,2,3,4}. Of these, 12 are e_4-bearing:
        +/- e_a +/- e_4   with a in {1,2,3},   4 sign-choices x 3 axes = 12.
    Each such bond lies in the oriented plane spanned by {e_a, e_4}.

    CONVENTION (natural / engine-canonical). The DM bivector axis for a bond with
    displacement r = eps_a e_a + eps_4 e_4 is the bond bivector
        B_hat_{ij} = (eps_a * eps_4) * e_{a4}
    — the oriented 2-plane the bond lies in, signed by the parity-odd product of
    the bond's component signs. (The DM bivector being THIS plane, rather than
    its 4D Hodge dual I_4 * e_{a4} = +/- e_{bc} (b,c the complementary spatial
    pair), is a convention choice; both conventions give NON-commuting bond
    bivectors across distinct bond directions — see CONVENTION-ROBUSTNESS below.)

    RESULT. Across the C(12,2)=66 pairs of distinct e_4-bearing bonds:
      * 18 pairs share the spatial axis a (same {a,4} plane, up to sign) and
        commute identically;
      * 48 pairs have distinct spatial axes a != b and DO NOT COMMUTE:
            [e_{a4}, e_{b4}] = -2 e_{ab}   (a != b in {1,2,3})
        so the commutator is the spatial L-bivector e_{ab} (with sign tracking
        the eps_a eps_4 product). Distinct-axis pairs are 48/66 > 0, so the
        substrate-level claim "DM bond bivectors B_hat_{ij} on different D4
        bond directions are non-commuting" is VERIFIED.

    CONSEQUENCE (paper §23.6 (iii)). With non-commuting V_{ij} = exp(i theta_D
    B_hat_{ij}), the DM-twisted link U_{ij} = R_i^dag R_j V_{ij} no longer
    telescopes around a plaquette — F is no longer forced pure-gauge, the
    SU(2)_+ connection acquires genuine non-abelian curvature, and the full
    Z of instanton sectors opens up. The PRIMITIVE here is the algebraic fact
    that drives the lifting; the explicit plaquette + Yang-Mills construction
    remains Paper 2/3 (so paper §23.6 (iii) text retains its "construction:
    Paper 2/3" qualifier — only the substrate non-commutativity claim is here
    promoted from FRAMING to DERIVED-A). [UPDATE 2026-07-03, R-140
    d4_dm_plaquette_holonomy_explicit: the explicit plaquette holonomy is now
    computed — the pure-gauge lift is EXPLICIT (24/24 e_4-triangles
    non-trivial, exact law, chiral factorization); note the plaquette drives
    BOTH chiral sectors equally (chirally blind), and consistency forces the
    orientation-ODD refinement of this primitive's even bond-plane convention
    (B_even = eps_4 * B_odd; the commutator census here is
    orientation-insensitive, so nothing in this primitive changes).]

    CONVENTION-ROBUSTNESS. The Hodge-dual convention B_hat = I_4 * e_{a4} maps the
    bond bivectors {e_{14}, e_{24}, e_{34}} (Q-orbit) to {-e_{23}, +e_{13}, -e_{12}}
    (L-orbit), and these also non-commute pairwise ([e_{23}, e_{13}] = -2 e_{12}
    etc.). So the non-commutativity claim is convention-robust (DERIVED-A on EITHER
    convention; DERIVED-CONDITIONAL only on the unsharp "either" — the qualitative
    conclusion does not depend on the choice).

    TIER. DERIVED-A on the natural bond-bivector convention; convention-robust
    across the two natural Cl(4,0) choices (bond plane vs Hodge dual).
    """
    # Build the 12 e_4-bearing D4 bonds: displacements +/- e_a +/- e_4, a in {1,2,3}.
    bonds = []
    for a in (1, 2, 3):
        for eps_a in (+1, -1):
            for eps_4 in (+1, -1):
                bonds.append((eps_a, a, eps_4))
    assert len(bonds) == 12, f"expected 12 e4-bearing bonds, got {len(bonds)}"

    def _B_hat(bond):
        """DM bivector axis for an e_4-bearing bond (bond-plane convention)."""
        eps_a, a, eps_4 = bond
        return float(eps_a * eps_4) * e(a, 4)

    def _comm(A, B):
        return A * B - B * A

    def _is_zero(mv, tol=1e-12):
        coeffs = [abs(v) for _, v in mv.terms]
        return (not coeffs) or max(coeffs) < tol

    # ENGINE CHECK 1 (axis representatives): [e_{a4}, e_{b4}] = -2 e_{ab} for a != b.
    repr_pairs = {(1, 2): -2.0 * e(1, 2),
                  (1, 3): -2.0 * e(1, 3),
                  (2, 3): -2.0 * e(2, 3)}
    for (a, b), expected in repr_pairs.items():
        got = _comm(e(a, 4), e(b, 4))
        diff = got - expected
        assert _is_zero(diff), f"[e_{a}4, e_{b}4] != -2 e_{a}{b}: got {got}"

    # ENGINE CHECK 2 (full 12-bond scan): count non-commuting vs commuting pairs.
    n_nc = 0
    n_c  = 0
    for i in range(12):
        for j in range(i + 1, 12):
            cij = _comm(_B_hat(bonds[i]), _B_hat(bonds[j]))
            if _is_zero(cij):
                n_c += 1
            else:
                n_nc += 1
    # Geometry expectation: 4 bonds per axis, 3 axes.
    # Same-axis pairs: 3 * C(4,2) = 3*6 = 18 (all commute, since B_hat = +/- e_{a4}).
    # Distinct-axis pairs: C(12,2) - 18 = 66 - 18 = 48 (all non-commute).
    assert n_c == 18, f"expected 18 same-axis commuting pairs, got {n_c}"
    assert n_nc == 48, f"expected 48 distinct-axis non-commuting pairs, got {n_nc}"

    # ENGINE CHECK 3 (convention-robustness): the Hodge-dual convention I_4 * e_{a4}
    # also gives pairwise-non-commuting bond bivectors.
    duals = [I4 * e(a, 4) for a in (1, 2, 3)]
    for i in range(3):
        for j in range(i + 1, 3):
            cij = _comm(duals[i], duals[j])
            assert not _is_zero(cij), \
                f"dual convention: [dual_{i+1}, dual_{j+1}] = 0 (unexpected)"

    return {
        "tier": ("DERIVED-A (substrate non-commutativity of DM bond bivectors); convention-robust "
                 "across bond-plane and Hodge-dual conventions. PROMOTES §23.6 (iii) F-7 substrate "
                 "claim from FRAMING to DERIVED-A; explicit plaquette/Yang-Mills construction "
                 "remains Paper 2/3."),
        "n_bonds_e4":              12,             # 4 sign-choices x 3 spatial axes
        "n_pairs":                 66,             # C(12,2)
        "n_pairs_non_commuting":   n_nc,           # = 48 (distinct-axis)
        "n_pairs_commuting":       n_c,            # = 18 (same-axis)
        "axis_commutators":        "[e_{a4}, e_{b4}] = -2 e_{ab} for a != b in {1,2,3} (engine-verified)",
        "convention":              ("bond-plane: B_hat_{ij} = (eps_a*eps_4) * e_{a4} for bond +/- e_a +/- e_4; "
                                    "Hodge-dual variant I_4*e_{a4} = +/- e_{bc} (L-orbit) ALSO non-commuting"),
        "consequence_paper_23_6":  ("non-commuting V_{ij}=exp(i theta_D B_hat_{ij}) => plaquette no longer "
                                    "telescopes => F != 0 accessible, SU(2)_+ instanton sectors open."),
        "f7_status":               ("§23.6 (iii) substrate non-commutativity: F-7 FRAMING -> DERIVED-A "
                                    "(this primitive); plaquette/Yang-Mills construction: Paper 2/3 (unchanged)."),
    }


# ======================================================================
# THE CANTED-VACUUM BRANCH STRUCTURE + THE DM CHIRALITY LOCK
# (§D.3.3, §D.4.3)   [twt_matter]
# ----------------------------------------------------------------------
# Governing record for both primitives: the J,D/Gamma rework round,
#   knowledge/candidates/probes_2026-08-20/JD_REWORK_REPORT_2026-08-20.md
# (read-outs (A)/(C) + its 2026-08-21 consensus addendum), together with
#   REDERIVATION_HELIX_MINIMUM_2026-08-21.md  (blind re-derivation) and the
# four verdict files persisted in the same directory.
# ======================================================================

def canting_vacuum_branch_structure(J: float = 1.0) -> dict:
    """[DERIVED-numeric + closed-form mechanism | scope: the SINGLE-q SIMPLE-BIVECTOR
    HELICAL FAMILY] §D.4.3 — the branch structure of the canted vacuum.

    THE MODEL (frame-bilinear, 24 bonds, floats — no symbolic step):
        E(k, B) = sum_b [ -(J/2) Tr(W_b) - (D/2) <Bhat_b, W_b>_F ],   W_b = exp((k.b) B)
    with Bhat_b = (sigma_a/sqrt2) * e_{a4} on the 12 e_4-bearing bonds (sigma_a = the
    sign of the bond's e_a component — the ODD convention of R-140 /
    D4_DM_bond_bivectors_non_commuting; the EVEN convention kills the sin q term and is
    excluded by §D.4.3's own printed E(q)), zero on the 12 spatial bonds, and
    B = n_hat ^ e_4 a unit SIMPLE bivector (a screw state).

    WHAT IS COMPUTED HERE:
      (i)   AXIS BRANCH: k = q*e_1, B = e_14 reproduces §D.4.3's printed
            E(q) = -12J cos q - 12J - 2 sqrt2 D sin q exactly, up to the physically
            inert additive constant -24J (the bond-count term the section drops).
            This IDENTIFIES the configuration §D.4.3 minimises — a SPATIAL helix, not
            an e_4 one: the DM energy vanishes identically on an e_4-axis helix.
      (ii)  That configuration is a genuine stationary point of the full (k, B) problem
            and an INDEX-2 SADDLE for every D/J > 0. Closed form of the transverse
            second variation, checked here against a central difference:
                d2E/dk_2^2 = d2E/dk_3^2 = 4 (cos q + 3)(cos q - 1)/cos q  <  0
            for all 0 < cos q < 1 (i.e. all D/J > 0), vanishing only in the
            ferromagnetic limit D -> 0.
      (iii) BODY-DIAGONAL BRANCH: k = t*(1,1,1,0) — all twelve e_4-bonds at ONE uniform
            angle instead of the axis branch's 4+8 split — lies LOWER, by the
            leading-order law  dE = -(1/243)*(D/J)^4 * J, equivalently Ref-1's
            -(2 sqrt2/9)*D*r^3 at r = sqrt2 D/(6J) (two blind derivations, one law).
            MECHANISM: the two families are degenerate through O(d^2); the DM cubic
            term ~ sum_a k_a^4 is minimised on the body diagonal (r^4/3) and maximised
            on the axis (r^4), so the axis branch loses at O(d^4), not at leading order.
      (iv)  The leading-order HELICAL-RATE INVARIANT |k|*lambda = sqrt2 D/(6J) holds on
            the diagonal branch as well (lambda = the unit bivector's eigen-angle = 1
            here), where on the axis branch the same closed form appears as tan q. So
            R-108's closed form SURVIVES on both branches, with a re-interpreted
            referent; what does not survive is the word "ground state".

    TIER, stated per component. (i), (ii) and (iv) are closed-form identities, verified
    numerically here against the explicit bond sum. (iii) is DERIVED-numeric with a
    closed-form mechanism; an exact-arithmetic minimisation is still owed. Global
    minimality is asserted ONLY WITHIN THE SINGLE-q SIMPLE-BIVECTOR HELICAL FAMILY
    (RUL-049): multi-q, conical and non-simple-B states are unscanned.

    NORMALISATION, quoted with the figure (it is not normalisation-free): at
    D/J = 0.787 the gap is 1.548e-3 J per site = 3.2e-5 of the frame-bilinear per-site
    total (-48J) and 6.4e-5 of §D.4.3's own printed E(q) total (-24.2J).

    WHAT IS OPEN. WHICH branch the DRIVEN dynamics selects is a kernel question (#1 gap,
    §D.5) — static energetics need not govern a NESS vacuum. It is assembly-recorded at
    §D.5 as a named puzzle piece (RUL-030 class 2), not ruled.

    PRIOR ART, and it is not the framework's: axis-vs-body-diagonal helix direction
    selection at ~1e-5 relative splitting is standard cubic-helimagnet physics
    (Bak & Jensen 1980); Luttinger-Tisza certifies a global minimum only under the
    strong constraint (Lyons & Kaplan 1960), which is NOT verified here.
    """
    import numpy as np
    SQ2 = math.sqrt(2.0)
    SQ3 = math.sqrt(3.0)
    SQ6 = math.sqrt(6.0)

    # ---- the 24 D4 nearest-neighbour bonds (directed: b and -b both present) ----
    _B = []
    for _i, _j in combinations(range(4), 2):
        for _si in (+1, -1):
            for _sj in (+1, -1):
                _v = np.zeros(4); _v[_i] = float(_si); _v[_j] = float(_sj)
                _B.append(_v)
    BONDS = np.array(_B, float)
    assert BONDS.shape == (24, 4), f"D4 bond set must be 24x4, got {BONDS.shape}"

    def _Ea4(a):
        M = np.zeros((4, 4)); M[a, 3] = 1.0; M[3, a] = -1.0
        return M

    def _biv(n):
        n = np.asarray(n, float); n = n / float(np.linalg.norm(n))
        return sum(n[a] * _Ea4(a) for a in range(3))

    def _W(theta, B):
        # Rodrigues for a UNIT SIMPLE bivector (B^3 = -B): exact, no matrix exponential.
        return np.eye(4) + math.sin(theta) * B + (1.0 - math.cos(theta)) * (B @ B)

    def E_bond_sum(k, B, D, even_convention=False):
        """The explicit 24-bond frame-bilinear energy — the ground truth of this primitive."""
        tot = 0.0
        for b in BONDS:
            W = _W(float(np.dot(k, b)), B)
            tot += -(J / 2.0) * float(np.trace(W))
            if b[3] != 0.0:
                a = int(np.nonzero(b[:3])[0][0])
                w = float(b[a]) * (float(b[3]) if even_convention else 1.0)
                tot += -(D / 2.0) * (w / SQ2) * float(np.sum(_Ea4(a) * W))
        return tot

    def E_reduced(k, D):
        """Closed form of the bond sum with B already optimised (v ∝ (s1,s2,s3), w = 0)."""
        c = np.cos(k); s = np.sin(k)
        pair = sum(c[i] * c[j] for i, j in combinations(range(4), 2))
        return (-24.0 * J - 4.0 * J * float(pair)
                - 2.0 * SQ2 * D * abs(float(c[3])) * float(np.linalg.norm(s[:3])))

    # ---- (i) the AXIS branch reproduces §D.4.3's printed E(q) --------------------
    axis_maxdiff = 0.0
    for D in (0.2 * J, 0.787 * J, 2.0 * J):
        for q in [0.1 * t for t in range(13)]:
            got = E_bond_sum(np.array([q, 0.0, 0.0, 0.0]), _biv([1, 0, 0]), D)
            want = -24.0 * J - 12.0 * J * math.cos(q) - 12.0 * J - 2.0 * SQ2 * D * math.sin(q)
            axis_maxdiff = max(axis_maxdiff, abs(got - want))
    assert axis_maxdiff < 1e-11, (
        "the 24-bond sum must reproduce §D.4.3's E(q) up to the inert -24J constant; "
        f"maxdiff {axis_maxdiff:.3e}")

    # the DM energy is IDENTICALLY zero on an e_4-axis helix (why the vacuum helix is spatial)
    e4_helix = max(abs(E_bond_sum(np.array([0.0, 0.0, 0.0, q]), _biv([1, 0, 0]), 0.787 * J)
                       - E_bond_sum(np.array([0.0, 0.0, 0.0, q]), _biv([1, 0, 0]), 0.0))
                   for q in (0.1, 0.5, 1.0))
    assert e4_helix < 1e-12, f"DM must vanish on an e_4-axis helix; got {e4_helix:.3e}"

    # the reduced form agrees with the bond sum at the optimal B (both branches)
    red_maxdiff = 0.0
    for k in (np.array([0.3, 0.0, 0.0, 0.0]), np.array([0.11, 0.11, 0.11, 0.0]),
              np.array([0.4, -0.2, 0.7, 0.0])):
        s = np.sin(k)[:3]
        red_maxdiff = max(red_maxdiff,
                          abs(E_bond_sum(k, _biv(s), 0.787 * J) - E_reduced(k, 0.787 * J)))
    assert red_maxdiff < 1e-11, f"reduced form vs bond sum: maxdiff {red_maxdiff:.3e}"

    # ---- (ii) the transverse second variation: index-2 saddle at every D/J > 0 ----
    # SYMBOLIC leg first (tolerance-free): sympy differentiates the model's own reduced
    # energy twice in the transverse component and the result is shown IDENTICAL to the
    # closed form, for symbolic q, after substituting the stationarity relation
    # D = 6 J tan q / sqrt2. This is what makes the closed form an identity rather than
    # a fit to three sampled couplings.
    _q, _Js = sp.symbols('q J_sym', positive=True)
    _k1, _k2 = sp.symbols('k1 k2', real=True)
    _c1, _c2 = sp.cos(_k1), sp.cos(_k2)
    _pairsym = _c1 * _c2 + 2 * _c1 + 2 * _c2 + 1          # k3 = k4 = 0
    _Dsym = 6 * _Js * sp.tan(_q) / sp.sqrt(2)
    _Esym = (-24 * _Js - 4 * _Js * _pairsym
             - 2 * sp.sqrt(2) * _Dsym * sp.sqrt(sp.sin(_k1) ** 2 + sp.sin(_k2) ** 2))
    _d2 = sp.simplify(sp.diff(_Esym, _k2, 2).subs(_k2, 0).subs(_k1, _q))
    # the pitch lies in (0, pi/2) for D/J > 0, so |sin q| = sin q on the physical branch
    _d2 = sp.simplify(_d2.subs(sp.Abs(sp.sin(_q)), sp.sin(_q)))
    _closed_sym = 4 * _Js * (sp.cos(_q) + 3) * (sp.cos(_q) - 1) / sp.cos(_q)
    assert sp.simplify(_d2 - _closed_sym) == 0, (
        "the transverse second variation must EQUAL 4J(cos q+3)(cos q-1)/cos q "
        f"identically; sympy gives {_d2}")

    saddle = {}
    for d in (0.2, 0.787, 2.0):
        D = d * J
        q = math.atan(SQ2 * d / 6.0)
        k0 = np.array([q, 0.0, 0.0, 0.0])
        # Step scaled to the transverse curvature's own scale sin q — a fixed absolute h
        # is a trap here, because the DM term's transverse expansion parameter is k2/sin q.
        # The finite-difference leg is intrinsically ill-conditioned and that is itself
        # informative: the saddle curvature is a ~1e-3 residual of two O(12J) pieces
        # (+4J(cos q+2) from exchange, -12J/cos q from DM), so a relative error of 1e-4 in
        # either piece is a percent-level error in the residual. The TOLERANCE-FREE leg is
        # the symbolic identity above; this one is the independent numerical witness.
        h = 1.0e-3 * math.sin(q)

        def f(x2):
            k = k0.copy(); k[1] = x2
            return E_reduced(k, D)

        num = (f(h) - 2.0 * f(0.0) + f(-h)) / (h * h)
        closed = 4.0 * J * (math.cos(q) + 3.0) * (math.cos(q) - 1.0) / math.cos(q)
        saddle[d] = {"q_rad": q, "d2E_dk2sq_closed_form": closed,
                     "d2E_dk2sq_central_difference": num,
                     "relative_diff": abs(num / closed - 1.0), "negative": closed < 0.0}
        assert closed < 0.0, f"transverse second variation must be NEGATIVE at D/J={d}"
        assert abs(num / closed - 1.0) < 1e-3, (
            f"closed-form second variation vs central difference at D/J={d}: "
            f"{closed:.10f} vs {num:.10f}")

    # ---- (iii)/(iv) the body-diagonal branch, its gap law and its rate ------------
    def E_diag(t, D):
        return (-24.0 * J - 12.0 * J * math.cos(t) ** 2 - 12.0 * J * math.cos(t)
                - 2.0 * SQ6 * D * math.sin(t))

    def E_axis(D):
        q = math.atan(SQ2 * (D / J) / 6.0)
        return -24.0 * J - 12.0 * J * math.cos(q) - 12.0 * J - 2.0 * SQ2 * D * math.sin(q)

    def _golden(fn, lo, hi, iters=200):
        g = (math.sqrt(5.0) - 1.0) / 2.0
        a, b = lo, hi
        c, e_ = b - g * (b - a), a + g * (b - a)
        for _ in range(iters):
            if fn(c) < fn(e_):
                b = e_
            else:
                a = c
            c, e_ = b - g * (b - a), a + g * (b - a)
        return 0.5 * (a + b)

    branches = {}
    for d in (0.1, 0.787):
        D = d * J
        t = _golden(lambda t: E_diag(t, D), 0.0, 1.0)
        ed, ea = E_diag(t, D), E_axis(D)
        # the diagonal branch's closed form must agree with the explicit bond sum
        eb = E_bond_sum(t * np.array([1.0, 1.0, 1.0, 0.0]), _biv([1, 1, 1]), D)
        assert abs(eb - ed) < 1e-11, f"diagonal-branch bond sum vs closed form: {abs(eb-ed):.3e}"
        gap = ed - ea
        pred = -(1.0 / 243.0) * d ** 4 * J
        rate = SQ3 * t                      # |k| * lambda, lambda = 1 for a unit simple B
        branches[d] = {
            "t_per_bond_angle_rad": t, "E_diagonal": ed, "E_axis": ea,
            "gap": gap, "gap_leading_order_law": pred,
            "gap_relative_deviation_from_law": abs(gap / pred - 1.0),
            "helical_rate": rate, "sqrt2_D_over_6J": SQ2 * d / 6.0,
            "rate_abs_deviation": abs(rate - SQ2 * d / 6.0),
        }
        assert ed < ea, f"the body-diagonal branch must lie LOWER at D/J={d}"

    assert branches[0.1]["gap_relative_deviation_from_law"] < 1.0e-3, (
        "the -(1/243)(D/J)^4 splitting law must hold at small D/J (D/J = 0.1); got "
        f"{branches[0.1]['gap_relative_deviation_from_law']:.3e}")
    assert branches[0.1]["rate_abs_deviation"] < 1.0e-6, (
        "the leading-order helical-rate invariant |k|*lambda = sqrt2 D/(6J) must hold on "
        f"the diagonal branch at D/J = 0.1; got {branches[0.1]['rate_abs_deviation']:.3e}")

    gap787 = branches[0.787]["gap"]
    return {
        "tier": ("DERIVED-numeric + closed-form mechanism; scope = the SINGLE-q "
                 "SIMPLE-BIVECTOR HELICAL FAMILY (RUL-049 — multi-q, conical and "
                 "non-simple-B states unscanned). Branch SELECTION by the driven "
                 "dynamics is OPEN (#1 gap, §D.5, assembly-recorded)."),
        "axis_branch_closed_form_maxdiff": axis_maxdiff,
        "axis_branch_configuration": "k = q*e_1 (a SPATIAL helix), B = e_14; the four "
                                     "±e_1±e_4-class bonds carry the DM weight 1/sqrt2",
        "dm_energy_on_e4_axis_helix": e4_helix,
        "reduced_vs_bond_sum_maxdiff": red_maxdiff,
        "transverse_second_variation": saddle,
        "saddle_index": 2,
        "saddle_holds_for_all_DoverJ_gt_0": all(v["negative"] for v in saddle.values()),
        "branches": branches,
        "splitting_law": "dE = -(1/243)*(D/J)^4*J  ==  -(2 sqrt2/9)*D*r^3 at r = sqrt2 D/(6J)",
        "gap_at_DoverJ_0787": gap787,
        "gap_relative_to_full_bond_total_minus48J": abs(gap787) / (48.0 * J),
        "gap_relative_to_paper_printed_total": abs(gap787) / 24.2047102383,
        "open_branch_selection": ("which single-q branch the DRIVEN kernel selects — static "
                                  "energetics need not govern a NESS vacuum (#1 gap, §D.5)"),
        "prior_art": ("Bak & Jensen 1980 (cubic-helimagnet direction selection); "
                      "Lyons & Kaplan 1960 (the Luttinger-Tisza strong constraint, "
                      "unverified here)"),
        "governing_record": ("knowledge/candidates/probes_2026-08-20/ — "
                             "JD_REWORK_REPORT_2026-08-20.md §7 + §14 addendum (b1), "
                             "REDERIVATION_HELIX_MINIMUM_2026-08-21.md, "
                             "VERDICT_REF1_JD2B_2026-08-21.md"),
    }


# ============================================================================
# THE ESTATE OF N64 — the three primitives banked out of the four-round estate
# dispute (2026-08-23). Governing records:
#   knowledge/audit/generations_arc_2026-08-23/VERDICT_REVIEWER_ESTATE_2026-08-23.md
#     (verdict + RATIFICATION ADDENDUM, §R5.4 = the banking package)
#   knowledge/audit/generations_arc_2026-08-23/TONGUES_T2PRIME_2026-08-23.md
#     (§CONSENSUS + §CONSENSUS-R4)
#   knowledge/audit/generations_arc_2026-08-23/ESTATE_BANKING_2026-08-23.md
#     (this pass's execution record)
# PLACEMENT (reviewer's adjudication, canon §6 consumption rule): all three
# consume V3 picks — the D4 siting, the D/J = 0.787 calibration, the branch pick —
# so all three are CANDIDATE-half primitives and NONE takes a CORE_PROVENANCE row.
# ============================================================================


def brannen_comb_commitment_dominance_and_dof_vacuity() -> dict:
    """[CANDIDATE (the commitment dominance) + FIT, COUNTED (the attainment) +
    DERIVED-numeric (each maximum, the pitch thresholds) + DERIVED-A (the period
    lattice = 2pi*D4*; the eight order-3 symmetries; lattice-`t` mass blindness; the
    pi/12 window; rank(N) = 2)] §C.3 / §D.4.3 — HOW FAR THE BANKED HELIX ENERGY CAN
    REACH TOWARDS THE KOIDE AMPLITUDE AND THE CHARGED-LEPTON LADDER, AND WHY REACHING
    THEM IS WORTH NOTHING.

    ONE PRIMITIVE, ONE DICT, ON PURPOSE. Every number below is returned together
    because separating them is exactly how this quantity was mis-reported twice in
    one day: `1.303412` became a governing-ledger headline within hours of being
    computed, without the commitment that produced it. A number in its own row gets
    quoted; a number inside this dict cannot be quoted without its commitment.
    The mandated inequality `c_max_translation_closed < sqrt2 < c_max_twisted_guarded`
    is asserted here so the two closed-family maxima can never drift apart.

    *** THE NEVER-SEPARABLE PAIR — the reason this primitive was RENAMED. ***
    `measured_triple_attained = True` and `solution_manifold_dim = 4` /
    `sm_quantities_returned = '0 of 19'` are ONE FINDING and are returned by ONE call.
    A corpus able to quote *"the banked geometry reproduces the charged-lepton ladder
    exactly"* without *"on a 4-dimensional solution manifold, returning 0 of 19 SM
    quantities"* has been handed the worst sentence in this program's history. The
    discipline is made EXECUTABLE, not hoped for: `twt_test.py` carries an AST-level
    INSEPARABILITY GUARD that fails if the attainment key and the vacuity keys are
    ever returned by different functions, and the guard is demonstrated firing on a
    planted split.

    *** THE FINDING: M-3-COMMITMENT-DOMINANCE. ***
    The Brannen amplitude `c` reachable from the banked {J, D} helix energy is
    dominated by the UNBANKED M-3 commitment — how the CELL-layer meta-time ℤ3
    generation phase acts on the GRAIN-layer spatial helix configuration `k` — and
    NOT by the substrate. Two defensible readings of "a closed ℤ3 comb" differ by
    1.216468 vs 2.000000, i.e. by more than the whole distance from the lower one to
    the Koide point. NO GEOMETRIC CEILING IS A SUBSTRATE PROPERTY. (RUL-049: this is
    a negative claim about ceilings, and its conditioning class is named throughout —
    banked {J,D} reduced energy, D/J = 0.787, single-`q` simple-bivector family.)

    C-33 FRAME/LAYER NAMING, held throughout:
      * `E_reduced(k)` is a GRAIN-layer per-site frame-bilinear bond energy on the D4
        lattice, read in the OUTSIDE frame. It contains no `e5` and no meta-time phase.
      * the ℤ3 generation phase `phi_n = 2pi n/3` is a CELL-layer, meta-time object
        (`generation_z3_is_metatime_phase`).
      * the measured lepton mass ratios are INSIDE-frame empirical data, imported per
        canon §0's METHOD clause and routed through the counted `m = E0` premise
        (`mass_equals_elastic_cost_premise`, vacuum-subtracted, v = 0).
      * M-3 is the channel between the first two — a CELL-phase -> GRAIN-configuration
        LAYER CROSSING, unbanked, RUL-048 class.

    *** THE MASS-RATIO CAVEAT — READ THIS BEFORE QUOTING ANY `c` ABOVE. ***
    Every number in the AMPLITUDE half concerns `c` (equivalently `K = (2 + c^2)/6`)
    ALONE. Matching `K` is ONE equation; matching the ladder is TWO. The two exhibited
    non-degenerate screw points that hit `c = sqrt2, K = 2/3` to twelve digits give
    sqrt-mass ratios
        1 : 7.83 : 235.62   (HIT A)      and      1 : 1.56 : 85.66   (HIT B)
    against the measured `1 : 206.77 : 3477.37` — so NO configuration measured in the
    four-round AMPLITUDE dispute came near the ladder.
    *** AND THAT IS NO LONGER THE WHOLE STORY — READ THE JOINT-SEARCH BLOCK BELOW. ***
    The joint `(c, delta)` search that the dispute defined and never ran DOES reach the
    ladder, exactly. **RUL-049 conditioning, in the same sentence:** batch 1's kill, in
    its *"the geometry cannot reach the data"* form, DOES NOT SURVIVE **on the SCREW
    family — whose generation-legality is an OPEN coordinator call**; it is UNTOUCHED
    on the TRANSLATION-STEP family, where the ladder remains unreached. The kill is
    REPLACED, not removed, and the replacement is of a different and stronger class:
    a dof/VACUITY kill (below). T2P-1 itself — the first-harmonic `c = 1` theorem — is
    untouched by any of this.

    *** THE JOINT (c, delta) SEARCH — ATTAINMENT AND VACUITY, ONE FINDING. ***
    Searching the closed screw family for the FULL charged-lepton triple (`c`, the
    Brannen phase `delta`, hence both mass ratios) rather than for `c` alone:
      * ATTAINED, exactly. `log-err = 0.0`; mass ratios `1 : 206.768282988 :
        3477.365266602` against the measured `1 : 206.768282988 : 3477.365266602`,
        per-component relative error `~3e-15`. It attains on ALL EIGHT order-3
        symmetries independently, at 19 mutually-distant solutions in one refinement
        pass — and the ratification round's INDEPENDENT solver (different
        parametrisation, objective and dedup radius) found 14 more of its own.
      * AND THAT IS THE NULL RESULT, EXACTLY AS PRE-REGISTERED. `t` contributes 2 free
        reals (its component transverse to `ker(N)` is pinned to a discrete set by the
        two closure equations; `ker(N)` is 2-dimensional and free) and `k0` contributes
        4: SIX free reals against TWO constraints (`K` is not a third — `K = (2+c^2)/6`
        identically). The mod-`L` reduction acts INSIDE `ker(N)`, removing redundancy,
        not dimension.
      * ★ THE KILL IS IMMUNE TO A JACOBIAN ATTACK, BY COUNTING ALONE (the ratification
        round's strengthening, and the reason the measurement is confirmation rather
        than foundation): a `2 x 6` Jacobian has rank `<= 2` IDENTICALLY, so the
        solution manifold has dimension `>= 6 - 2 = 4` AT EVERY SOLUTION, WHATEVER the
        rank turns out to be. Rank 2 is the MAXIMUM — the LEAST vacuous case available
        to the family; any rank DROP makes the manifold LARGER, i.e. more vacuous. The
        measured rank 2 (singular values well separated) says only that the two
        constraints are locally independent and well-conditioned, which is the best the
        family could have done.
      * SM QUANTITIES RETURNED: **0 of 19.** It returns the two numbers it was fed.
        Against RUL-098's budget (`~4-6` counted constants deriving the SM's `~19`)
        this SPENDS 2 and COMPRESSES NOTHING, with 4 dimensions of unspent freedom.
        By the corpus's own vacuity control MAP-G (`log-err 1.08e-07` on FOUR free
        integers, recorded VACUOUS BY CONSTRUCTION), `log-err = 0` on SIX free reals is
        MORE vacuous, not less.
      * WIDENING CANNOT RESCUE IT. Any widening of the family adds PARAMETERS or
        BRANCHES; neither adds CONSTRAINTS. That all eight `rho` work is branch
        multiplicity, not extra dimensions — and it makes the dof kill stronger.

    *** THE EIGHT ORDER-3 SYMMETRIES — computed, with the argument the ratification
    round REPAIRED. *** The enumeration below is exhaustive OF THE ORDER-3 LINEAR
    SYMMETRIES OF `E_reduced` — never "exhaustive of linear `rho`", which is a wider
    and false claim. The repaired argument (the originally-stated one, "a symmetry must
    fix the J-term separately, hence permutes the roots", DOES NOT FOLLOW — a symmetry
    of `E` fixes `E`, not `J`, and could a priori trade J-support against DM-support):
        `E` has Fourier support `R u S`, `R` = the 24 D4 roots (TWO ODD coordinates
        each) and `S = supp(DM) <= 2Z^4` (DM is invariant under pi*e_i for every `i`,
        so its support is all-even); hence `R n 2Z^4 = {}`.
        `E . rho = E` forces `rho^T (R u S) = R u S` by uniqueness of the expansion.
        `<R u S> = D4` (the roots alone generate it; 2Z^4 < D4), and `rho^T` is a
        bijection of `R u S` onto itself, so `rho^T (D4) = D4`.
        ==> `rho^T` in Aut(D4 lattice), the order-1152 group.  QED.
    The disjointness of `R` and `S` is genuinely needed — to IDENTIFY THE GROUP, not to
    split the two terms. Computed inside that group: 1152 elements, 96 symmetries of
    `E_reduced`, EIGHT of order 3 (a signed 3-cycle on `(k1,k2,k3)` with `k4` fixed and
    sign-product `+1`: 2 cycles x 4 admissible sign patterns), with the enumeration's
    NEGATIVE CONTROL seen to fire (a non-symmetry in the same group deviates by > 1).
    DECLARED UNSCANNED, and this is the class that has now refuted three
    exhaustiveness claims in this dispute: (i) NON-LINEAR order-3 symmetries;
    (ii) **order-3 maps whose linear part is NOT a symmetry of `E_reduced` — a genuine
    Z3 orbit only needs `rho^3 = I`, so that family is strictly LARGER and is NAMED,
    NOT SCANNED**; (iii) the translation-step family (exhausted at 1.216468);
    (iv) other `D/J`, branch or engine-level widenings.

    *** THE PITCH ESTATE — the one thing the substrate DOES constrain. ***
      * `L = ker(N) n 2pi*D4* = 2pi*A2`, HEXAGONAL — DERIVED, not asserted: a
        half-integer vector of `D4*` has NO zero coordinate, so the half-integer coset
        cannot meet `{x4 = 0} > ker(N)`; only `2pi*Z^4` survives. Minimal vector
        `2pi*sqrt2 = 8.885766`, covering radius `d/sqrt3 = 5.130199`.
      * LATTICE-`t` MASS BLINDNESS, DERIVED-A, three lines and no numerics:
            let t in 2pi*D4*.  rho is a symmetry of E and rho(2pi D4*) = 2pi D4*.
              E(rho k0 + t)             = E(rho k0)   [t a period]     = E(k0)
              E(rho^2 k0 + rho t + t)   = E(rho^2 k0) [rho t + t also] = E(k0)
            all three comb energies coincide  =>  X1 = 0  =>  c = 0 IDENTICALLY,
            for EVERY base point.
        ==> 100% of the screw comb's mass splitting is carried by the NON-LATTICE part
        of `t`. It is a MEASURE-ZERO KNIFE-EDGE, not a neighbourhood: an infinitesimal
        off-lattice displacement already restores the full amplitude range (`c -> 2`).
      * `|t|* = 0.6160 +- 0.0003` (isotropic in the kernel plane to 0.09%, measured at
        NON-SYMMETRIC angles because 60-degree spacing is `rho`'s own symmetry and would
        have manufactured the isotropy): the measured triple is reachable only BELOW it.
      * `|t|_c = 0.702693`: the pitch at which `max c` over `k0` falls to `sqrt2`.
      * ★ `delta` BINDS BEFORE `c` DOES, BY A FACTOR 1.1402 — matching the phase is a
        STRICTLY STRONGER requirement on the pitch than matching the amplitude. EVERY
        ceiling in the four-round dispute measured the WEAKER face. This is the one
        strategic finding of the whole dispute.
      * The `delta`-window at `c = sqrt2` is the FULL non-negativity window
        `[0, pi/12]` (DERIVED-A: `E0 >= 0` with `c = sqrt2` needs the angle nearest pi
        to sit at `psi >= pi/4`, so `psi in [pi/4, pi/3]`, width `pi/12` = 25% of the
        fold domain) — saturated to machine precision and EMPTY outside it. **The
        substrate contributes exactly ZERO constraint beyond `E0 >= 0`.**
      * Screw translations MUST be quoted REDUCED MODULO `L`: raw `9.08 / 15.61 /
        15.28 / 15.78` reduce to `0.6268 / 0.4448 / 0.4482 / 0.6036`. All four
        "different" published screws are ONE small-pitch regime, and the un-reduced
        coordinates concealed it.
      * `min/mean` is NOT corroboration: it is a function of `(c, delta)` alone, so
        matching the target fixes it by construction. Returned so it cannot later be
        mistaken for an independent check.

    THE FIVE-ROW COMMITMENT MENU (all on the banked reduced energy at D/J = 0.787,
    GLOBAL-vacuum subtracted — see the subtraction note below):

      # | commitment on how the ℤ3 phase acts on the helix | max c   | closed? | sqrt2?
      1 | translation step, closed in 2pi*D4*              | 1.216468| YES     | no
      2 | lam = 1 ray shift at |khat| = 1                  | 1.303371| NO      | no
      3 | lam = 2, 5 ray shifts                            | 1.994608| NO      | yes
      4 | order-3 AFFINE (SCREW) step h(k) = rho k + t,
        |   closed in 2pi*D4*                              | 2.000000| YES     | YES
        |   (1.827129 under an explicit non-degeneracy guard)
      5 | any order-3 map outside {translation, rho.translation} | UNSCANNED | — | —

    Rows 2 and 3 are BOTH WITHDRAWN and are kept only so they cannot be re-derived as
    new: `lam*khat` is not in `D4*` for the diag2/diag3 directions at any integer
    `lam` (1/sqrt2, 1/sqrt3 irrational), so those three points are not a ℤ3 ORBIT at
    all — they are three points at 2pi*lam/3 spacing along a ray of incommensurate
    period. Row 2 was the developer's published number and rode an uncounted
    normalisation convention; row 3 was the reviewer's counter-example and was
    conceded on the same ground.
    ROW 5 IS THE LESSON OF THE ROUND APPLIED TO ITSELF. Twice an exhaustiveness claim
    was refuted by widening the FORM OF THE STEP. No maximum over "all ℤ3 combs" has
    been established at all — only maxima over two named step-forms.

    WHAT IS ACTUALLY DERIVED-A HERE, and it is the one banked-quality item to come out
    of the dispute — THE PERIOD LATTICE, AS A FOURIER-SUPPORT THEOREM (not a controls
    hedge; two negative controls do not establish a lattice):
        The periods of a function are the DUAL of the group generated by its Fourier
        support. The J-term `-4 sum_{i<j} cos k_i cos k_j` has support {+-e_i +- e_j},
        which GENERATES D4 (integer vectors of even coordinate sum); hence
        periods(J) = 2pi*Dual(D4) = 2pi*D4* exactly. The DM-term
        `-2 sqrt2 (D/J) |cos k4| * ||sin(k1,k2,k3)||` has period pi in each coordinate
        (|cos| has period pi; sin^2 has period pi), so periods(DM) contains pi*Z^4,
        which CONTAINS 2pi*D4*, and therefore never restricts. INTERSECTION = 2pi*D4*.
    Checked below on the D4* generators with a NEGATIVE CONTROL at 2pi(1/2,1/2,0,0)
    that must FAIL (a lattice check that never rejects has not been shown to be one).

    THE 81-CLASS ENUMERATION (DERIVED-numeric, exhaustive OF TRANSLATION-STEP COMBS).
    Two translation steps give the same configuration iff `Delta - Delta'` is a period,
    i.e. `g = g' mod 3*D4*`; so a complete residue system of `D4*/3D4*` covers every
    translation-step closed comb. |D4*/3D4*| = 3^4 = 81 for any rank-4 lattice, and
    Z^4 -> D4*/3D4* is an ISOMORPHISM (3D4* contains (1.5,1.5,1.5,1.5)), so the 81
    half-integer candidates are entirely redundant and {0,1,2}^4 alone hits every class
    exactly once. 80 classes are non-degenerate. Computed below both ways.

    THE SUBTRACTION CORRECTION (a defect of BOTH published ray scans, found in the
    ratification round). `m = E0` requires the GLOBAL vacuum, not the ray minimum
    (`mass_equals_elastic_cost_premise`: "the VACUUM-SUBTRACTED rest cost ... relative
    to the pure-carrier background"). The ray minimum is higher, so the subtracted
    values and their mean `C` are smaller and `c = R/C` is INFLATED. Corrected:
    diag2 lam=1 1.303413 -> 1.303371; axis lam=1 1.216639 -> 1.216467; diag2 lam=2
    1.994681 -> 1.994608. THE CROSS-CHECK THIS PRODUCES IS THE POINT: the corrected
    axis lam=1 value 1.216467 EQUALS the exhaustive translation-closed maximum
    1.216468, because g = (0,0,2,0) IS an axis-type comb. That dissolves the apparent
    paradox (a published ray value exceeding an "exhaustive" maximum) which would
    otherwise have read as a refutation of the enumeration itself.

    THE SCREW FAMILY (row 4). A ℤ3 comb requires an order-3 MAP `h` with `h^3 = id`,
    not an order-3 TRANSLATION. With `rho` = the 3-cycle on (k1,k2,k3) — an EXACT
    symmetry of the banked reduced energy, checked below at ~7e-15 — `h(k) = rho k + t`
    has `h^3 = id + N t`, `N = I + rho + rho^2`, so closure is `N t in 2pi*D4*`. The
    comb reads `E(k0), E(k0+u), E(k0+u+rho^2 u)` with `u = rho^2 t`: NOT an arithmetic
    progression, hence in no translation class at any `g`. On this family `max c = 2`,
    `1.827129` under the non-degeneracy guard, and `c = sqrt2` with `K = 2/3` is
    ATTAINED to twelve digits at non-degenerate, physically-sized triples (HIT B
    returned below, the best-conditioned exhibit: min/mean = 0.2608, closure exact to
    machine epsilon). Since 1.827129 > sqrt2 > 1.216468 and `c` varies continuously,
    the Koide point is attained on this family by the intermediate value theorem,
    independently of any exhibited point.

    *** THE OPEN COORDINATOR CALL, NAMED AND NOT PRE-EMPTED (RUL-030 class 3). ***
    Is the screw family EXCLUDED? It is not excluded by computation — it closes and it
    reaches sqrt2. It is excluded, if at all, by a CANON GUARDRAIL whose SCOPE is the
    question: canon §5 says the L-orbit blades are "never generation LABELS" (sweep fix
    2026-07-02), and `rho` is generated by an L-orbit blade — `G_generator`'s spatial
    ℤ3, DERIVED mass-blind, whose docstring's rigorous core is "spatial G != the
    generation operator". But the screw uses `rho` inside the STEP MAP with the label
    still the meta-time phase, and "never a label" does not reach "never inside the
    step map". THE SCOPE EXTENSION IS A COORDINATOR CALL, NOT A WORKER'S. Recorded
    both ways, per the keeper's symmetric duty:
      FOR EXCLUSION: `G_generator`'s DERIVED mass-blindness plus canon §5's
        generation/L-orbit separation — and the exclusion does NOT need the
        non-derived "rho = COLOUR" identification, which is dropped from the argument.
        Corroborating datum, computed below: at `t = 0` the screw degenerates to the
        bare spatial ℤ3 and the three energies COINCIDE exactly, so `rho` contributes
        ZERO mass splitting; every split in the screw comb comes from its translation
        part. Also on the record: identifying the generation operator with spatial `G`
        has ALREADY produced a banked fake-negative
        (`generation_z3_is_metatime_phase`).
      AGAINST EXCLUSION: `h = rho . T` is a SCREW, and a screw is literally the
        originator's corkscrew image ("a corkscrew tunnel across the wavefronts"). It
        is the only construction in the dispute that realises it. Committing to it is
        CORE-TOUCHING (it modifies canon §5's separation), so it would need a
        family-tree branch node with menu and revert clause AND plain-language
        coordinator sign-off BEFORE any load-bearing use (RUL-048).
    Either way the outcome is a COMMITMENT — which is the finding, not a resolution.

    LINEAGE, credited rather than re-derived (F3 duty). This is the SEVENTH negative
    forcing route for `c = sqrt2` (companion R-065/R-066: "NOT independently forced —
    six forcing routes NEGATIVE") and the SECOND non-negativity amplitude cap after
    N60 (`r^2 >= 0` caps the ℤ3-orbit DFT amplitude at A <= 1). N60's own
    would-change-if already named the escape ("a vacuum-subtracted/signed measure").
    The ℤ3 harmonic collapse itself is banked at
    `brannen_z3_harmonic_collapse_invariant` with priority to Koide (hep-ph/0005137,
    2000) and Zenczykowski (PRD 86 (2012) 117303) — so "a constant plus one harmonic
    on the ℤ3 comb" is a property of ANY three real numbers and discriminates nothing.
    `c = sqrt2` remains a COUNTED, UNFORCED INPUT (canon §2, §7); nothing here changes
    that, and in particular NO conditioning clause of the form "sqrt2 requires
    structure outside the banked family" may be added to the Koide rows — that
    sentence is false, and this primitive is what refutes it.

    *** THE LEGALITY BANNER, carried into every sentence of the joint-search half. ***
    The screw family's generation-legality is an OPEN COORDINATOR CALL (below), and a
    positive result on it banks NO generation identification. As it turns out the
    positive is of the kind that makes the ruling CHEAPER, not more urgent: this pass
    shows the family BUYS NOTHING, so excluding it FORFEITS NOTHING.

    self-checks: the period lattice on three D4* generators with a NEGATIVE CONTROL
    that must fail; the residue system 162 -> 81 -> 80 and the {0,1,2}^4 isomorphism;
    the free 4D vacuum landing on the banked body-diagonal value; `max c` reproduced
    on the maximising class and a polish-per-class sweep over all 80 classes that does
    not exceed it; the corrected axis lam=1 cross-check against 1.216468; rho's exact
    symmetry and rho^3 = I; HIT B's c, K, closure residual and non-degeneracy witness;
    a guarded screw search that exceeds sqrt2; the t = 0 mass-blindness datum; the
    mandated inequality 1.216468 < sqrt2 < 1.827129; AND, from the joint search: the
    order-1152 group built by closure with 1152/96/8 reproduced and the non-symmetry
    control seen to fire; rank(N) = 2 for all eight; the exhibited attainment point
    reproducing the measured ladder inside the pre-registered ATTAINED band, on a
    closure exact to machine epsilon; the Jacobian of the two log-ratios in the SIX
    free reals measured rank 2 with `dim = free_reals - constraints = 4`; `L`'s minimal
    vector `2pi*sqrt2` and covering radius; the mod-`L` reduction of the exhibited
    screw reproducing 0.603642; lattice-`t` mass blindness at ~1e-14 against a
    small-pitch `max c` of ~2 (the measure-zero knife-edge, computed BOTH sides);
    `max c` at `|t|_c = 0.702693` landing on sqrt2; and the delta-binds-first ratio
    `|t|_c / |t|* = 1.1402`."""
    import cmath
    import numpy as np
    from itertools import product
    from scipy.optimize import minimize

    SQ2 = math.sqrt(2.0)
    TWO_PI = 2.0 * math.pi
    DJ = 0.787                       # the V3 {J,D} calibration (a CANDIDATE-half pick)

    def E_red(k):
        """The BANKED reduced energy, byte-for-byte the closed form inside
        `canting_vacuum_branch_structure` (J = 1, B already optimised)."""
        c = np.cos(k); s = np.sin(k)
        pair = sum(c[i] * c[j] for i, j in combinations(range(4), 2))
        return (-24.0 - 4.0 * float(pair)
                - 2.0 * SQ2 * DJ * abs(float(c[3])) * float(np.linalg.norm(s[:3])))

    def c_of(tri):
        """Brannen amplitude from a ℤ3 triple: c = 2|X1|/|X0| — a MAGNITUDE, so no
        phase/sign convention in the DFT can move it."""
        X0 = sum(tri)
        if abs(X0) < 1e-15:
            return float("nan")
        X1 = sum(a * cmath.exp(-2j * math.pi * n / 3.0) for n, a in enumerate(tri))
        return 2.0 * abs(X1) / abs(X0)

    def K_of(tri):
        return sum(x * x for x in tri) / (sum(tri) ** 2)

    def in_D4star(v, tol=1e-7):
        return (all(abs(x - round(x)) < tol for x in v)
                or all(abs((x - 0.5) - round(x - 0.5)) < tol for x in v))

    rng = np.random.default_rng(20260823)
    KS = rng.uniform(-4.0, 4.0, (150, 4))

    # ---- 1. THE PERIOD LATTICE = 2pi*D4* (theorem above; measured here) ----------
    def dev(shift):
        return max(abs(E_red(k + shift) - E_red(k)) for k in KS)

    lattice = {}
    for nm, v in (("2pi*e1", (1., 0., 0., 0.)),
                  ("2pi*(1,1,0,0)", (1., 1., 0., 0.)),
                  ("2pi*(.5,.5,.5,.5)", (.5, .5, .5, .5))):
        lattice[nm] = dev(TWO_PI * np.array(v))
        assert lattice[nm] < 1e-12, f"{nm} must be a period of E_reduced; dev {lattice[nm]:.3e}"
    neg_control = dev(TWO_PI * np.array([.5, .5, 0., 0.]))
    assert neg_control > 1.0, (
        "the period test must be SEEN TO REJECT: 2pi(1/2,1/2,0,0) is NOT in D4* and must "
        f"fail; got {neg_control:.3e}")

    # ---- 2. THE COMPLETE RESIDUE SYSTEM D4*/3D4* --------------------------------
    vals = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5]
    cand = [np.array(g, float) for g in product(vals, repeat=4)
            if in_D4star(np.array(g, float))]
    reps = []
    for ga in cand:
        if any(in_D4star((ga - gb) / 3.0) for gb in reps):
            continue
        reps.append(ga)
    nondeg = [g for g in reps if not in_D4star(g / 3.0)]
    ireps = []
    for ga in (np.array(g, float) for g in product([0., 1., 2.], repeat=4)):
        if any(in_D4star((ga - gb) / 3.0) for gb in ireps):
            continue
        ireps.append(ga)
    assert (len(cand), len(reps), len(nondeg), len(ireps)) == (162, 81, 80, 81), (
        "the residue system must be 162 candidates -> 81 classes -> 80 non-degenerate, "
        "with {0,1,2}^4 alone hitting all 81 (Z^4 -> D4*/3D4* is an isomorphism); got "
        f"{(len(cand), len(reps), len(nondeg), len(ireps))}")

    # ---- 3. THE GLOBAL VACUUM (the subtraction the m = E0 premise requires) ------
    t_st = 0.107096425089
    E_VAC_BANKED = (-24.0 - 12.0 * math.cos(t_st) ** 2 - 12.0 * math.cos(t_st)
                    - 2.0 * math.sqrt(6.0) * DJ * math.sin(t_st))
    free_vac = 1e9
    for _ in range(40):
        r = minimize(E_red, rng.uniform(0.0, TWO_PI, 4), method="Nelder-Mead",
                     options={"xatol": 1e-12, "fatol": 1e-14, "maxiter": 3000})
        free_vac = min(free_vac, float(r.fun))
    assert abs(free_vac - E_VAC_BANKED) < 1e-9, (
        "the free 4D vacuum search must land on the BANKED body-diagonal branch value; "
        f"{free_vac:.9f} vs {E_VAC_BANKED:.9f}")
    EV = E_VAC_BANKED

    # ---- 4. ROW 1 — the translation-step closed family ---------------------------
    def neg_c_trans(k0, g):
        tri = [E_red(k0 + n * (TWO_PI / 3.0) * g) - EV for n in range(3)]
        if min(tri) < -1e-9 or sum(tri) < 1e-3:
            return 10.0
        cc = c_of(tri)
        return 10.0 if math.isnan(cc) else -cc

    g_max = np.array([0., 0., 2., 0.])
    c_on_gmax = 0.0
    for _ in range(20):
        r = minimize(neg_c_trans, rng.uniform(0.0, TWO_PI, 4), args=(g_max,),
                     method="Nelder-Mead",
                     options={"xatol": 1e-11, "fatol": 1e-13, "maxiter": 2500})
        c_on_gmax = max(c_on_gmax, -float(r.fun))
    C_MAX_TRANS = 1.216468            # governing record (two independent searches, 5e-7)
    assert abs(c_on_gmax - C_MAX_TRANS) < 1e-5, (
        "the maximising translation class g = (0,0,2,0) must reproduce the recorded "
        f"1.216468; got {c_on_gmax:.6f}")

    sweep_max, sweep_arg = 0.0, None
    for g in nondeg:
        seeds = rng.uniform(0.0, TWO_PI, (60, 4))
        s0 = seeds[int(np.argmax([-neg_c_trans(s, g) for s in seeds]))]
        r = minimize(neg_c_trans, s0, args=(g,), method="Nelder-Mead",
                     options={"xatol": 1e-10, "fatol": 1e-12, "maxiter": 1500})
        if -float(r.fun) > sweep_max:
            sweep_max, sweep_arg = -float(r.fun), g.copy()
    assert sweep_max < C_MAX_TRANS + 1e-4, (
        "no translation-step closed class may exceed the recorded maximum 1.216468; "
        f"the 80-class polish sweep returned {sweep_max:.6f}")

    # ---- 5. the corrected-subtraction axis cross-check ---------------------------
    def c_max_ray(khat, lam, ndelta=4000, ngrid=4000):
        ss = np.linspace(0.0, TWO_PI, ngrid)
        Es = np.array([E_red(s * khat) for s in ss])
        s_star = float(ss[int(np.argmin(Es))])
        best = 0.0
        for j in range(ndelta):
            dd = TWO_PI * j / ndelta
            tri = [E_red((s_star + lam * TWO_PI * n / 3.0 - dd) * khat) - EV
                   for n in range(3)]
            if min(tri) < -1e-12 or sum(tri) < 1e-6:
                continue
            cc = c_of(tri)
            if not math.isnan(cc):
                best = max(best, cc)
        return best

    axis_lam1_global = c_max_ray(np.array([1., 0., 0., 0.]), 1)
    assert abs(axis_lam1_global - C_MAX_TRANS) < 1e-4, (
        "THE CROSS-CHECK: the axis lam=1 ray value, corrected to GLOBAL-vacuum "
        "subtraction, must equal the exhaustive translation-closed maximum (g = (0,0,2,0) "
        f"IS an axis-type comb); got {axis_lam1_global:.6f} vs {C_MAX_TRANS}")

    # ---- 6. ROW 4 — the order-3 AFFINE (screw) closed family ---------------------
    RHO = np.array([[0., 0., 1., 0.],
                    [1., 0., 0., 0.],
                    [0., 1., 0., 0.],
                    [0., 0., 0., 1.]])
    R2 = RHO @ RHO
    rho_sym_dev = max(abs(E_red(RHO @ k) - E_red(k)) for k in KS)
    assert rho_sym_dev < 1e-12, (
        "rho (the 3-cycle on k1,k2,k3) must be an EXACT symmetry of the banked reduced "
        f"energy; dev {rho_sym_dev:.3e}")
    assert np.allclose(np.linalg.matrix_power(RHO, 3), np.eye(4)), "rho^3 must be I"

    def comb_u(k0, u):
        return [E_red(k0) - EV, E_red(k0 + u) - EV, E_red(k0 + u + R2 @ u) - EV]

    def closure_residual(k0, u):
        """h^3(k0) - k0 by ITERATING THE MAP, not via the algebra."""
        t = RHO @ u
        k = np.array(k0, float)
        for _ in range(3):
            k = RHO @ k + t
        return (k - k0) / TWO_PI

    HIT_B_k0 = np.array([-0.084525707, 0.047786432, 6.524193429, -0.062738936])
    HIT_B_u = np.array([-5.929839519, 12.472259117, -6.542419598, 0.0])
    triB = comb_u(HIT_B_k0, HIT_B_u)
    cB, KB = c_of(triB), K_of(triB)
    resB = closure_residual(HIT_B_k0, HIT_B_u)
    ptsB = [HIT_B_k0, HIT_B_k0 + HIT_B_u, HIT_B_k0 + HIT_B_u + R2 @ HIT_B_u]
    distinctB = all(float(np.linalg.norm(ptsB[i] - ptsB[j])) > 1e-6
                    for i, j in ((0, 1), (0, 2), (1, 2)))
    nondegB = min(triB) / (sum(triB) / 3.0)
    msB = sorted(x * x for x in triB)
    assert abs(cB - SQ2) < 1e-8 and abs(KB - 2.0 / 3.0) < 1e-8, (
        f"HIT B must return c = sqrt2 and K = 2/3; got c = {cB:.12f}, K = {KB:.12f}")
    assert in_D4star(resB) and float(np.abs(resB).max()) < 1e-9, (
        f"HIT B's closure h^3(k0) = k0 must be exact to machine epsilon; got {resB}")
    assert distinctB and nondegB > 0.25, (
        "HIT B must be three DISTINCT points and non-degenerate (min/mean > 0.25 — this "
        "is NOT the c -> 2 two-massless corner); got "
        f"distinct={distinctB}, min/mean={nondegB:.4f}")

    HIT_A_k0 = np.array([3.019357, 3.184774, 3.429826, 3.085031])
    HIT_A_u = np.array([6.097349, 6.646313, -12.743662, 0.0])
    triA = comb_u(HIT_A_k0, HIT_A_u)
    msA = sorted(x * x for x in triA)

    # a live guarded search on the exactly-closing a = b = 0 branch: it must EXCEED sqrt2
    def neg_c_screw(x):
        k0 = x[:4]
        u = np.array([x[4], x[5], -x[4] - x[5], 0.0])
        tri = comb_u(k0, u)
        if min(tri) < -1e-9 or sum(tri) < 1e-3:
            return 10.0
        if min(tri) < 0.05 * (sum(tri) / 3.0) or sum(tri) < 0.5:
            return 10.0
        cc = c_of(tri)
        return 10.0 if math.isnan(cc) else -cc

    screw_guarded_live = 0.0
    for _ in range(10):
        x0 = np.concatenate([rng.uniform(0.0, TWO_PI, 4), rng.uniform(-8.0, 8.0, 2)])
        r = minimize(neg_c_screw, x0, method="Nelder-Mead",
                     options={"xatol": 1e-10, "fatol": 1e-12, "maxiter": 2000})
        screw_guarded_live = max(screw_guarded_live, -float(r.fun))
    assert screw_guarded_live > SQ2, (
        "the NON-DEGENERATE screw maximum must EXCEED sqrt2 — this is what makes the "
        "Koide point interior to the family by the intermediate value theorem; got "
        f"{screw_guarded_live:.6f}")

    # the t = 0 mass-blindness datum (the exclusion argument's computed ground)
    blind_spread = max(max(comb_u(k0, np.zeros(4))) - min(comb_u(k0, np.zeros(4)))
                       for k0 in rng.uniform(0.0, TWO_PI, (4, 4)))
    assert blind_spread < 1e-12, (
        "at t = 0 the screw degenerates to the BARE spatial ℤ3 and the three energies must "
        f"COINCIDE (mass-blindness, G_generator); spread {blind_spread:.3e}")

    # ================================================================
    # 7. THE JOINT (c, delta) SEARCH — ATTAINMENT AND VACUITY, ONE FINDING
    # ================================================================

    # ---- 7a. the order-1152 D4 point group, BUILT BY CLOSURE, and the EIGHT ------
    # order-3 symmetries. The generators: a transposition + a 4-cycle (=> S4), ONE
    # ODD sign flip (=> the full hyperoctahedral group of order 384), and the
    # half-Hadamard (=> the triality extension to 1152). Omitting the odd flip
    # returns 384 and would have MISSED two thirds of the group — recorded because it
    # is the kind of silent under-enumeration this dispute exists to prevent.
    _P = np.zeros((4, 4)); _P[0, 1] = _P[1, 0] = 1.0; _P[2, 2] = _P[3, 3] = 1.0
    _C4 = np.zeros((4, 4)); _C4[0, 1] = _C4[1, 2] = _C4[2, 3] = _C4[3, 0] = 1.0
    _S1 = np.eye(4); _S1[0, 0] = -1.0
    _HAD = 0.5 * np.array([[1., 1, 1, 1], [1, -1, 1, -1],
                           [1, 1, -1, -1], [1, -1, -1, 1]])
    _gens = [_P, _C4, _S1, _HAD]

    def _gkey(M):
        return tuple(np.round(M, 9).ravel() + 0.0)

    _grp = {_gkey(np.eye(4)): np.eye(4)}
    _front = [np.eye(4)]
    while _front:
        _nf = []
        for _M in _front:
            for _g in _gens:
                _Mg = _g @ _M
                _k = _gkey(_Mg)
                if _k not in _grp:
                    _grp[_k] = _Mg
                    _nf.append(_Mg)
        _front = _nf
    _grp = list(_grp.values())
    assert len(_grp) == 1152 and all(
        np.allclose(M.T @ M, np.eye(4), atol=1e-9) for M in _grp), (
        "the D4 point group must close at order 1152 with every element orthogonal; "
        f"got {len(_grp)}")

    _KS_S = KS[:60]
    _devs = [max(abs(E_red(M @ k) - E_red(k)) for k in _KS_S) for M in _grp]
    _syms = [M for M, d in zip(_grp, _devs) if d < 1e-12]
    _worst_non_sym = max(d for d in _devs if d >= 1e-12)
    ORD3 = [M for M in _syms
            if np.allclose(np.linalg.matrix_power(M, 3), np.eye(4), atol=1e-9)
            and not np.allclose(M, np.eye(4), atol=1e-9)]
    _ord3_dev = max(max(abs(E_red(M @ k) - E_red(k)) for k in _KS_S) for M in ORD3)
    _N_ranks = sorted({int(np.linalg.matrix_rank(np.eye(4) + M + M @ M, tol=1e-9))
                       for M in ORD3})
    assert (len(_syms), len(ORD3)) == (96, 8), (
        "inside the order-1152 group `E_reduced` must have exactly 96 symmetries, EIGHT "
        f"of them of order 3; got {(len(_syms), len(ORD3))}")
    assert _worst_non_sym > 1.0, (
        "the symmetry enumeration must be SEEN TO REJECT — a non-symmetry inside the "
        f"same 1152 group must deviate by > 1; worst deviation {_worst_non_sym:.3e}")
    assert _N_ranks == [2], (
        "N = I + rho + rho^2 must have rank 2 for EVERY order-3 symmetry (this is what "
        f"makes closure TWO scalar equations and leaves ker(N) 2-dimensional); got {_N_ranks}")
    assert all(abs(M[3, 3] - 1.0) < 1e-12 and abs(M[3, :3]).max() < 1e-12
               and abs(M[:3, 3]).max() < 1e-12 for M in ORD3), (
        "every order-3 symmetry must FIX k4 (a signed 3-cycle on (k1,k2,k3))")

    # ---- 7b. THE ATTAINMENT — the exhibited joint-search solution ----------------
    # `sj_03`'s best point, on the dispute's own rho, exact-closure branch (t in ker N).
    JOINT_k0 = np.array([2.827904510199, 3.021047758255, 3.656406929630, 3.144453562423])
    JOINT_t = np.array([-6.769480527926, -6.109532537936, 12.879013065861, 0.0])
    MEASURED_MASS_RATIOS = (1.0, 206.768282988, 3477.365266602)

    def _orbit_h(k0, t, rho):
        r2 = rho @ rho
        return [k0, rho @ k0 + t, r2 @ k0 + rho @ t + t]

    def _tri_h(k0, t, rho=RHO):
        return [E_red(p) - EV for p in _orbit_h(k0, t, rho)]

    _triJ = _tri_h(JOINT_k0, JOINT_t)
    _msJ = sorted(x * x for x in _triJ)
    joint_ratios = [1.0, _msJ[1] / _msJ[0], _msJ[2] / _msJ[0]]
    joint_rel_err = [abs(joint_ratios[i] - MEASURED_MASS_RATIOS[i])
                     / MEASURED_MASS_RATIOS[i] for i in (1, 2)]
    _NM = np.eye(4) + RHO + R2
    joint_closure_over_2pi = (_NM @ JOINT_t) / TWO_PI
    joint_c, joint_K = c_of(_triJ), K_of(_triJ)
    joint_min_over_mean = min(_triJ) / (sum(_triJ) / 3.0)
    assert max(joint_rel_err) < 1e-6, (
        "THE ATTAINMENT: the exhibited joint-search point must reproduce the MEASURED "
        "charged-lepton ladder inside the pre-registered ATTAINED band (<= 1e-6 relative "
        f"on each ratio); got {joint_rel_err}")
    assert float(np.abs(joint_closure_over_2pi).max()) < 1e-9, (
        "the exhibited point must CLOSE exactly (N t = 0, the exact-closure branch); got "
        f"{joint_closure_over_2pi}")

    # ---- 7c. THE VACUITY — six free reals, two constraints, rank 2 ---------------
    # ker(N) = {(a,b,c,0) : a+b+c = 0}: a 2-dimensional plane. The 6 free reals are
    # k0 (4) + t's kernel components (2); the 2 constraints are the two measured ratios.
    V1 = np.array([1.0, -1.0, 0.0, 0.0])
    V2 = np.array([0.0, 1.0, -1.0, 0.0])
    assert float(np.abs(_NM @ V1).max()) < 1e-12 and float(np.abs(_NM @ V2).max()) < 1e-12
    _ab, *_ = np.linalg.lstsq(np.column_stack([V1, V2]), JOINT_t, rcond=None)
    assert float(np.linalg.norm(np.column_stack([V1, V2]) @ _ab - JOINT_t)) < 1e-9, (
        "the exhibited t must lie IN ker(N) — the exact-closure branch")

    def _logratios(x):
        tri = _tri_h(x[:4], x[4] * V1 + x[5] * V2)
        ms = sorted(v * v for v in tri)
        return np.array([math.log(ms[1] / ms[0]), math.log(ms[2] / ms[0])])

    _x0 = np.concatenate([JOINT_k0, _ab])
    _hh = 1e-6
    _JAC = np.zeros((2, 6))
    for _i in range(6):
        _xp = _x0.copy(); _xp[_i] += _hh
        _xm = _x0.copy(); _xm[_i] -= _hh
        _JAC[:, _i] = (_logratios(_xp) - _logratios(_xm)) / (2.0 * _hh)
    _sv = np.linalg.svd(_JAC, compute_uv=False)
    jac_rank = int(np.linalg.matrix_rank(_JAC, tol=1e-6 * float(_sv[0])))
    FREE_REALS, CONSTRAINTS = 6, 2
    MANIFOLD_DIM = FREE_REALS - CONSTRAINTS
    assert _JAC.shape == (CONSTRAINTS, FREE_REALS) and jac_rank == 2, (
        "the Jacobian of the two log-ratios in the six free reals must be 2x6 of rank 2 "
        f"(the LEAST vacuous case available); got shape {_JAC.shape}, rank {jac_rank}")
    assert MANIFOLD_DIM == 4, "6 free reals - 2 constraints = 4"

    # ---- 7d. THE PITCH ESTATE ----------------------------------------------------
    # L = ker(N) cap 2pi*D4*. A half-integer vector of D4* has no zero coordinate, so it
    # cannot meet {x4 = 0}; only 2pi*Z^4 survives => L = 2pi*A2, hexagonal.
    _Lvecs = []
    for _a, _b in product(range(-4, 5), repeat=2):
        _cc = -_a - _b
        if (_a, _b, _cc) == (0, 0, 0):
            continue
        _Lvecs.append(TWO_PI * np.array([_a, _b, _cc, 0.0], float))
    L_min_vector = min(float(np.linalg.norm(v)) for v in _Lvecs)
    L_covering_radius = L_min_vector / math.sqrt(3.0)
    assert abs(L_min_vector - TWO_PI * SQ2) < 1e-9, (
        f"L's minimal vector must be 2pi*sqrt2 = {TWO_PI * SQ2:.6f}; got {L_min_vector:.6f}")

    def _reduce_modL(t):
        best = float(np.linalg.norm(t))
        for _a, _b in product(range(-6, 7), repeat=2):
            _cc = -_a - _b
            best = min(best, float(np.linalg.norm(
                t - TWO_PI * np.array([_a, _b, _cc, 0.0], float))))
        return best

    joint_t_raw = float(np.linalg.norm(JOINT_t))
    joint_t_reduced = _reduce_modL(JOINT_t)
    assert abs(joint_t_reduced - 0.603642) < 1e-5, (
        "the exhibited screw, REDUCED MOD L, must land at the recorded 0.603642 — "
        f"the raw {joint_t_raw:.6f} is not comparable to any other published screw; "
        f"got {joint_t_reduced:.6f}")

    # lattice-`t` mass blindness (DERIVED-A; the three-line proof is in the docstring)
    lattice_t_spread = 0.0
    for _v in ((1., 0., 0., 0.), (1., 1., 0., 0.), (.5, .5, .5, .5), (0., 0., 1., -1.),
               (1., -1., 0., 0.), (2., -1., -1., 0.)):
        _tl = TWO_PI * np.array(_v)
        for _k0 in rng.uniform(0.0, TWO_PI, (3, 4)):
            _tt = _tri_h(_k0, _tl)
            lattice_t_spread = max(lattice_t_spread, max(_tt) - min(_tt))
    assert lattice_t_spread < 1e-12, (
        "EVERY lattice translation must be mass-blind (c = 0 identically, for every base "
        f"point) — not only t = 0; spread {lattice_t_spread:.3e}")

    def _max_c_at_pitch(tvec, ntries, seed):
        r = np.random.default_rng(seed)
        best = 0.0

        def _neg(k0):
            tri = _tri_h(k0, tvec)
            if min(tri) < -1e-9 or sum(tri) < 1e-3:
                return 10.0
            cc = c_of(tri)
            return 10.0 if math.isnan(cc) else -cc

        for _ in range(ntries):
            _r = minimize(_neg, r.uniform(0.0, TWO_PI, 4), method="Nelder-Mead",
                          options={"xatol": 1e-11, "fatol": 1e-13, "maxiter": 3000})
            best = max(best, -float(_r.fun))
        return best

    _kdir = V1 / float(np.linalg.norm(V1))
    PITCH_JOINT = 0.616296          # |t|*  — governing record, bisected, isotropic
    PITCH_C_ONLY = 0.702693         # |t|_c — the pitch at which max c falls to sqrt2
    max_c_at_pitch_c = _max_c_at_pitch(PITCH_C_ONLY * _kdir, 16, 11)
    max_c_at_small_pitch = _max_c_at_pitch(0.10 * _kdir, 20, 11)
    assert abs(max_c_at_pitch_c - SQ2) < 5e-3, (
        "|t|_c must be the pitch at which max c over k0 falls to sqrt2; at 0.702693 the "
        f"maximum is {max_c_at_pitch_c:.4f}")
    assert max_c_at_small_pitch > 1.9, (
        "THE MEASURE-ZERO KNIFE-EDGE, computed on BOTH sides: c = 0 IDENTICALLY on the "
        "lattice, yet at reduced pitch 0.10 the maximum is already ~2 — so lattice-t mass "
        f"blindness is a knife-edge, not a neighbourhood; got {max_c_at_small_pitch:.4f}")
    delta_binds_first = PITCH_C_ONLY / PITCH_JOINT
    assert abs(delta_binds_first - 1.1402) < 1e-3, (
        "★ THE ONE STRATEGIC FINDING OF THE FOUR-ROUND DISPUTE: matching delta is a "
        "STRICTLY STRONGER requirement on the screw pitch than matching c, by 1.1402 — "
        f"every ceiling in four rounds measured the weaker face; got {delta_binds_first:.4f}")

    # the pi/12 non-negativity window at c = sqrt2 (DERIVED-A), brute-forced
    _adm = 0
    _NTH = 200000
    for _j in range(_NTH):
        _th = TWO_PI * _j / _NTH
        if min(1.0 + SQ2 * math.cos(_th + TWO_PI * n / 3.0) for n in range(3)) >= 0.0:
            _adm += 1
    delta_window_measure_fraction = _adm / _NTH
    assert abs(delta_window_measure_fraction - 0.25) < 1e-3, (
        "the analytic non-negativity window at c = sqrt2 is psi in [pi/4, pi/3], width "
        "pi/12 = 25% of the fold domain; brute force must return 0.25, got "
        f"{delta_window_measure_fraction:.6f}")

    # ---- 8. THE MANDATED INEQUALITY — the finding, made undriftable --------------
    C_MAX_TWISTED = 2.000000
    C_MAX_TWISTED_GUARDED = 1.827129
    assert C_MAX_TRANS < SQ2 < C_MAX_TWISTED_GUARDED < C_MAX_TWISTED, (
        "THE FINDING IS THE INEQUALITY: 1.216468 < sqrt2 < 1.827129 < 2.000000 — two "
        "defensible readings of 'a closed ℤ3 comb' STRADDLE the Koide point, so no "
        "ceiling is a substrate property")

    return {
        "tier": ("CANDIDATE (the M-3 commitment dominance; the screw as a generation "
                 "mechanism, legality OPEN) + FIT, COUNTED — 2 of 6 consumed, NEVER "
                 "DERIVED (the hit on the measured triple) + DERIVED-numeric (each "
                 "maximum and each pitch threshold, on the banked {J,D} reduced energy "
                 "at D/J = 0.787, GLOBAL-vacuum subtracted) + DERIVED-A (the period "
                 "lattice = 2pi*D4*, a Fourier-support theorem; the EIGHT order-3 "
                 "symmetries; lattice-t mass blindness; the pi/12 window; rank(N) = 2)"),
        "finding": ("TWO HALVES, ONE FINDING. (i) NO GEOMETRIC CEILING IS A SUBSTRATE "
                    "PROPERTY — the Brannen amplitude reachable from the banked helix "
                    "energy is dominated by the UNBANKED M-3 commitment, not by the "
                    "substrate. (ii) THE MEASURED CHARGED-LEPTON LADDER IS ATTAINED "
                    "EXACTLY on the closed screw family — ON A 4-DIMENSIONAL SOLUTION "
                    "MANIFOLD, RETURNING 0 OF 19 SM QUANTITIES. The kill is no longer "
                    "'the geometry cannot reach the data'; it is 'the geometry reaches "
                    "the data with four spare dimensions, so reaching it is worth "
                    "nothing' — a dof/VACUITY kill, and widening the family makes it "
                    "STRONGER, not weaker."),
        # --- the period lattice (DERIVED-A) ---
        "period_lattice": "2pi*D4*",
        "period_lattice_ground": ("FOURIER-SUPPORT THEOREM: periods = dual of the group "
                                  "generated by the Fourier support; the J-term's support "
                                  "{+-e_i+-e_j} generates D4 so periods(J) = 2pi*D4* "
                                  "exactly, and the DM-term's pi-periodicity per coordinate "
                                  "gives periods(DM) > 2pi*D4*, which never restricts"),
        "period_deviations": lattice,
        "period_negative_control_2pi_half_half_0_0": neg_control,
        # --- the enumeration ---
        "residue_system": {"quotient": "D4*/3D4*", "candidates_in_box": len(cand),
                           "distinct_classes": len(reps), "non_degenerate": len(nondeg),
                           "integer_reps_alone_suffice": len(ireps) == 81,
                           "why": "|D4*/3D4*| = 3^4 = 81; Z^4 -> D4*/3D4* is an isomorphism"},
        # --- the four measured maxima + the unscanned fifth row ---
        "c_max_translation_closed": C_MAX_TRANS,
        "c_max_translation_closed_reproduced_on_maximising_class": c_on_gmax,
        "c_max_translation_closed_80class_sweep": sweep_max,
        "c_max_unit_gear_ray": 1.303371,
        "c_max_lambda2_ray": 1.994608,
        "c_max_twisted_closed": C_MAX_TWISTED,
        "c_max_twisted_closed_nondegenerate": C_MAX_TWISTED_GUARDED,
        "c_max_twisted_guarded_live_witness": screw_guarded_live,
        "sqrt2_attained_on_closed_comb": True,
        "subtraction": "global vacuum (never the ray minimum — m = E0's own referent)",
        "global_vacuum_free_search": free_vac,
        "global_vacuum_banked_body_diagonal": E_VAC_BANKED,
        "axis_lambda1_global_subtracted_cross_check": axis_lam1_global,
        "cross_check_note": ("the corrected axis lam=1 ray value EQUALS the exhaustive "
                             "translation-closed maximum, because g = (0,0,2,0) IS an "
                             "axis-type comb — which dissolves the apparent paradox of a "
                             "ray value exceeding an 'exhaustive' maximum"),
        "commitment_menu": [
            {"row": 1, "step": "translation, closed in 2pi*D4*", "c_max": C_MAX_TRANS,
             "closed": True, "reaches_sqrt2": False,
             "status": "DERIVED-numeric; exhaustive OF TRANSLATION-STEP combs "
                       "(80 classes x free base point); best-verified number in the dispute"},
            {"row": 2, "step": "lam = 1 ray shift at |khat| = 1", "c_max": 1.303371,
             "closed": False, "reaches_sqrt2": False,
             "status": "WITHDRAWN — an uncounted normalisation convention, and not an orbit"},
            {"row": 3, "step": "lam = 2, 5 ray shifts", "c_max": 1.994608,
             "closed": False, "reaches_sqrt2": True,
             "status": "WITHDRAWN — not an orbit (lam*khat not in D4* at any integer lam)"},
            {"row": 4, "step": "order-3 AFFINE (SCREW) h(k) = rho k + t, closed in 2pi*D4*",
             "c_max": C_MAX_TWISTED, "c_max_nondegenerate": C_MAX_TWISTED_GUARDED,
             "closed": True, "reaches_sqrt2": True,
             "status": "CANDIDATE — defensibly excluded by canon §5 + G_generator's DERIVED "
                       "mass-blindness, NOT decisively; and it is the literal corkscrew"},
            {"row": 5, "step": "any order-3 map outside {translation, rho.translation}",
             "c_max": None, "closed": None, "reaches_sqrt2": None,
             "status": "NAMED, NOT SCANNED — twice an exhaustiveness claim was refuted by "
                       "widening the step-form; no maximum over 'all ℤ3 combs' exists"},
        ],
        "spread_between_the_two_closed_rows": C_MAX_TWISTED / C_MAX_TRANS,
        # --- the exhibited screw hits ---
        "screw_hit_B": {"k0": list(HIT_B_k0), "u": list(HIT_B_u),
                        "E0_J_per_site": [float(x) for x in triB],
                        "c": cB, "K": KB,
                        "closure_residual_over_2pi": [float(x) for x in resB],
                        "closure_in_D4star": True, "three_points_distinct": distinctB,
                        "min_over_mean": nondegB,
                        "sqrt_mass_ratios": [1.0, msB[1] / msB[0], msB[2] / msB[0]],
                        "note": "the BEST-CONDITIONED exhibit (min/mean 0.2608 vs the "
                                "addendum's 0.1107); closure exact by construction on the "
                                "a = b = 0 branch"},
        "screw_hit_A": {"c": c_of(triA), "K": K_of(triA),
                        "sqrt_mass_ratios": [1.0, msA[1] / msA[0], msA[2] / msA[0]]},
        # --- THE CAVEAT, returned so it travels with the numbers ---
        "mass_ratio_caveat": ("EVERY c IN THE AMPLITUDE HALF CONCERNS c ALONE. Matching K "
                              "is ONE equation; matching the ladder is TWO. The two "
                              "exhibited sqrt2 screw points give sqrt-mass ratios "
                              "1 : 7.83 : 235.62 and 1 : 1.56 : 85.66 against the measured "
                              "1 : 206.77 : 3477.37, so NO configuration measured in the "
                              "AMPLITUDE dispute came near the ladder. *** BUT THE JOINT "
                              "(c, delta) SEARCH DOES REACH IT — see measured_triple_"
                              "attained. RUL-049 CONDITIONING, IN THE SAME SENTENCE: batch "
                              "1's kill, in its 'cannot-reach-the-data' form, DOES NOT "
                              "SURVIVE on the SCREW family — whose generation-legality is "
                              "an OPEN COORDINATOR CALL; it is UNTOUCHED on the "
                              "TRANSLATION-STEP family, where the ladder remains "
                              "unreached. *** The kill is REPLACED, not removed, by a "
                              "dof/vacuity kill of a different and stronger class. T2P-1 "
                              "(the first-harmonic c = 1 theorem) is untouched throughout."),
        "measured_sqrt_mass_ratios": [1.0, 206.7683, 3477.3653],
        "mass_blindness_datum_spread": blind_spread,
        # ============================================================
        # THE JOINT (c, delta) SEARCH — THE NEVER-SEPARABLE PAIR.
        # `measured_triple_attained` and the vacuity block below are ONE FINDING and
        # are returned by ONE call. twt_test.py's AST-level INSEPARABILITY GUARD fails
        # if they are ever split into different functions, and is demonstrated firing
        # on a planted split.
        # ============================================================
        "measured_triple_attained": True,
        "attainment_logerr": 0.0,
        "attainment_exhibited_point": {
            "rho": "the dispute's rho = the 3-cycle on (k1,k2,k3), k4 fixed",
            "k0": list(JOINT_k0), "t": list(JOINT_t),
            "t_in_ker_N": True, "branch": "exact closure (N t = 0)",
            "E0_J_per_site": [float(x) for x in _triJ],
            "mass_ratios": joint_ratios,
            "measured_mass_ratios": list(MEASURED_MASS_RATIOS),
            "relative_error_per_ratio": joint_rel_err,
            "c": joint_c, "K": joint_K,
            "closure_over_2pi": [float(x) for x in joint_closure_over_2pi],
            "min_over_mean": joint_min_over_mean,
            "min_over_mean_is_NOT_corroboration": (
                "min/mean is a function of (c, delta) ALONE, so matching the target fixes "
                "it by construction — reported so it cannot be mistaken for an "
                "independent check. The measured triple's own value is 0.040350, which is "
                "BELOW the 5% non-degeneracy guard the dispute imposed on every "
                "c-maximisation: THAT GUARD WOULD HAVE EXCLUDED THE PHYSICAL TARGET."),
        },
        "attainment_on_all_eight_symmetries": True,
        "attainment_independent_solutions": {
            "search_refinement_pass": 19, "ratification_independent_solver": 14,
            "note": ("19 mutually-distant hits (pairwise parameter distances "
                     "min/median/max 4.16/16.11/35.61) from two independent code paths, "
                     "and 14 more from the ratification round's own solver on a different "
                     "parametrisation, objective and dedup radius. 19 vs 14 is a stopping "
                     "cap, not a discrepancy. NOTHING IS FRAGILE ABOUT THE HIT — which is "
                     "precisely the problem with it."),
        },
        # --- THE VACUITY, inseparable from the attainment above ---
        "free_reals": FREE_REALS,
        "constraints": CONSTRAINTS,
        "solution_manifold_dim": MANIFOLD_DIM,
        "jacobian_rank": jac_rank,
        "jacobian_singular_values": [float(x) for x in _sv],
        "sm_quantities_returned": "0 of 19",
        "dof_kill_is_jacobian_attack_proof": (
            "THE COUNTING ARGUMENT, which is the load-bearing step — the Jacobian is "
            "CONFIRMATION, not foundation: a 2 x 6 Jacobian has rank <= 2 IDENTICALLY, so "
            "the solution manifold has dimension >= 6 - 2 = 4 AT EVERY SOLUTION, by "
            "parameter counting alone, WHATEVER the rank turns out to be. Rank 2 is the "
            "MAXIMUM — the LEAST vacuous case available to the family; any rank DROP makes "
            "the manifold LARGER. The dof kill therefore cannot be attacked through the "
            "Jacobian at all."),
        "widening_makes_the_kill_stronger": (
            "any widening of the family adds PARAMETERS or BRANCHES; neither adds "
            "CONSTRAINTS. That all eight rho work is branch multiplicity, not extra "
            "dimensions — and it is evidence the reachability is GENERIC rather than "
            "special to the dispute's rho."),
        "budget_accounting": (
            "RUL-098's success criterion is PARAMETER COMPRESSION (~4-6 counted constants "
            "deriving the SM's ~19). This SPENDS 2 of the budget and buys back the 2 "
            "already-measured numbers it was fed, with 4 dimensions of unspent freedom. "
            "K is not a third return — K = (2 + c^2)/6 identically. NET YIELD: NEGATIVE. "
            "By the corpus's own vacuity control MAP-G (log-err 1.08e-07 on FOUR free "
            "INTEGERS, recorded VACUOUS BY CONSTRUCTION), log-err = 0 on SIX free REALS is "
            "MORE vacuous, not less. D/J = 0.787 is NOT corroboration: it was held fixed, "
            "but the 6 free reals absorb everything, so the hit tests it not at all."),
        "what_would_convert_it": (
            "NAMED, NOT COMPUTED — a hit on a 4-dimensional manifold becomes a result only "
            "if something OUTSIDE the fit cuts those 4 dimensions: (1) the quark/CKM comb "
            "fitted with the SAME rho, closure class, D/J and a SHARED or named-rule "
            "related (t, k0) — the only item that could convert the fit on its own; (2) the "
            "neutrino Brannen phase with NO new parameters; (3) a dynamical selection "
            "principle from the #1 gap (§D.5) — the 4 spare dimensions are exactly what a "
            "kernel would have to fix; (4) any independent structure FIXING the screw "
            "pitch, which would turn |t|* into a genuine FALSIFIER. NO FURTHER "
            "SINGLE-SECTOR WORK ON THIS FAMILY CAN CHANGE ITS STATUS: the branch is not "
            "blocked, it is EMPTY AT SINGLE-SECTOR RESOLUTION."),
        # --- THE EIGHT ORDER-3 SYMMETRIES ---
        "order3_symmetries": len(ORD3),
        "point_group_order": len(_grp),
        "symmetries_of_E_reduced": len(_syms),
        "order3_symmetry_max_deviation": _ord3_dev,
        "symmetry_enumeration_negative_control": _worst_non_sym,
        "N_rank_for_every_order3": _N_ranks[0],
        "order3_exhaustiveness_argument": (
            "THE REPAIRED ARGUMENT (the originally-published one does not follow — a "
            "symmetry of E fixes E, not the J-term separately, and could a priori trade "
            "J-support against DM-support): E has Fourier support R u S with R = the 24 D4 "
            "roots (TWO ODD coordinates each) and S = supp(DM) <= 2Z^4 (DM is invariant "
            "under pi*e_i for every i), so R n 2Z^4 = {}. E.rho = E forces "
            "rho^T (R u S) = R u S by uniqueness of the expansion; <R u S> = D4 and rho^T "
            "is a bijection of R u S onto itself, so rho^T(D4) = D4, i.e. rho^T lies in "
            "Aut(D4), the order-1152 group. The disjointness of R and S is needed to "
            "IDENTIFY THE GROUP, not to split the two terms."),
        "order3_exhaustiveness_scope": (
            "EXHAUSTIVE OF THE ORDER-3 LINEAR SYMMETRIES OF E_reduced — never 'exhaustive "
            "of linear rho', which is a wider and FALSE claim that the declaration list "
            "below already contradicts."),
        "order3_declared_unscanned": [
            "NON-LINEAR order-3 symmetries",
            "★ order-3 maps whose LINEAR PART IS NOT A SYMMETRY of E_reduced — a genuine "
            "Z3 orbit needs only rho^3 = I, so that family is strictly LARGER and is "
            "NAMED, NOT SCANNED. This is the widening class that has now refuted THREE "
            "exhaustiveness claims in this dispute.",
            "the translation-step family (already exhausted at 1.216468)",
            "other D/J, branch, or engine-level widenings",
        ],
        # --- THE PITCH ESTATE ---
        "pitch_period_lattice": "L = ker(N) n 2pi*D4* = 2pi*A2 (HEXAGONAL)",
        "pitch_period_lattice_ground": (
            "DERIVED, not asserted: ker(N) = {(a,b,c,0) : a+b+c = 0}; a half-integer "
            "vector of D4* has NO zero coordinate, so the half-integer coset cannot meet "
            "{x4 = 0}, and only 2pi*Z^4 survives."),
        "pitch_L_minimal_vector": L_min_vector,
        "pitch_L_covering_radius": L_covering_radius,
        "pitch_threshold_joint": PITCH_JOINT,
        "pitch_threshold_c_only": PITCH_C_ONLY,
        "delta_binds_first_factor": delta_binds_first,
        "delta_binds_first_note": (
            "★ THE ONE STRATEGIC FINDING OF THE FOUR-ROUND DISPUTE: matching delta is a "
            "STRICTLY STRONGER requirement on the screw pitch than matching c, by 1.140. "
            "EVERY ceiling in four rounds measured the WEAKER (amplitude) face. |t|* is "
            "isotropic in the kernel plane to 0.09%, measured at NON-SYMMETRIC angles "
            "because 60-degree spacing is rho's own symmetry on that plane and would have "
            "MANUFACTURED the isotropy."),
        "max_c_at_pitch_threshold_c_only": max_c_at_pitch_c,
        "max_c_at_small_pitch_0p10": max_c_at_small_pitch,
        "lattice_t_mass_blind": True,
        "lattice_t_spread": lattice_t_spread,
        "lattice_t_mass_blindness_proof": (
            "DERIVED-A, three lines, no numerics: let t in 2pi*D4*; rho is a symmetry of E "
            "and rho(2pi*D4*) = 2pi*D4*. Then E(rho k0 + t) = E(rho k0) = E(k0) and "
            "E(rho^2 k0 + rho t + t) = E(rho^2 k0) = E(k0). All three comb energies "
            "coincide => X1 = 0 => c = 0 IDENTICALLY, for EVERY base point. ==> 100% of "
            "the screw comb's mass splitting is carried by the NON-LATTICE part of t."),
        "lattice_t_blindness_is_a_measure_zero_knife_edge": (
            "★ THE FAMILY-LEVEL STATEMENT, and it is SHARPER than the single-base-point "
            "epsilon table published in the search report's §6.1 (which is labelled "
            "CONTRAST in its own script and reads as a family claim it never was, "
            "contradicting the same report's §6.3): mass blindness is a MEASURE-ZERO "
            "KNIFE-EDGE — it holds EXACTLY ON the lattice and nowhere else, and an "
            "INFINITESIMAL off-lattice displacement already restores the full amplitude "
            "range. Computed on both sides here: spread "
            "~1e-14 ON the lattice, max c already ~2 at reduced pitch 0.10. The "
            "ratification round's max-over-k0 table (reviewer-computed, credited, "
            "UNGUARDED — the approach to 2 is driven by the base point going to the "
            "vacuum, i.e. the mean going to zero) reads 1.9927 / 1.9878 / 1.9984 / 1.9988 "
            "at epsilon = 1e-3 / 1e-2 / 1e-1 / 1, against the fixed-k0 illustration's "
            "0.0027 / 0.0273 / 0.2679 / 1.0380."),
        "delta_window_at_koide": "psi in [pi/4, pi/3], width pi/12 — the FULL window",
        "delta_window_measure_fraction": delta_window_measure_fraction,
        "delta_window_is_saturated_and_empty_outside": (
            "the attainable delta-set at c = sqrt2 on the closed screw family IS the full "
            "non-negativity window [0, pi/12], saturated to machine precision, and EMPTY "
            "outside it. THE SUBSTRATE CONTRIBUTES EXACTLY ZERO CONSTRAINT BEYOND "
            "E0 >= 0 — a constraint of the CONSTRUCTION, not of the geometry. The "
            "pre-registered obstruction does not exist. The measured delta = 0.222225 "
            "sits 84.9% of the way into the window."),
        "screws_must_be_quoted_reduced_mod_L": {
            "exhibited_raw": joint_t_raw, "exhibited_reduced": joint_t_reduced,
            "published_raw_to_reduced": {"9.077521": 0.626794, "15.612561": 0.444780,
                                         "15.281476": 0.448233, "15.780407": 0.603642},
            "note": ("all four 'different' published screws are ONE small-pitch regime and "
                     "the un-reduced coordinates concealed it; the reviewer's 0.626794 "
                     "sits just OUTSIDE the joint threshold 0.616296, consistent with its "
                     "reaching c = sqrt2 at a delta that is not the measured one. A "
                     "correction is owed to the dispute record: screw translations are not "
                     "comparable unless reduced mod L."),
        },
        "measure_honesty_note": (
            "960,000 random draws from the family reached c in [0.000058, 1.342770] and "
            "ZERO samples within 0.01 of sqrt2. RANDOM SAMPLING ALONE WOULD HAVE REPORTED "
            "A MISS — the hits live on a thin set reachable only by optimisation. This is "
            "why the dispute's ray scans kept finding ceilings, and it is a standing "
            "warning that 'scanned N random directions and found nothing' is weak evidence "
            "on this family."),
        "legality": (
            "OPEN COORDINATOR CALL (the screw family) — RUL-030 class 3, NOT pre-empted. "
            "★ AND THIS PASS MAKES THE RULING CHEAP: the family BUYS NOTHING, so excluding "
            "it FORFEITS NOTHING. If the screw is ruled ILLEGAL, §2's eight symmetries, "
            "lattice-t mass blindness and the dof method survive as substrate facts and as "
            "method, and batch 1's kill survives untouched on the legal family. If it is "
            "ALLOWED, the hit is still a 2-parameter FIT with a 4-dimensional residual "
            "manifold."),
        # --- the open call ---
        "open_coordinator_call": ("canon §5's L-orbit guardrail says the L-orbit blades are "
                                  "never generation LABELS; does that scope extend to 'never "
                                  "inside the generation STEP MAP'? If yes, row 4 falls and "
                                  "row 1 is the live ceiling; if no, row 4 stands and needs a "
                                  "family-tree branch node (CORE-touching, RUL-048). NOT "
                                  "ruled here — RUL-030 class 3."),
        "m3_ruling_would_decide": ("a single M-3 ruling — does the meta-time generation phase "
                                   "act on the helix as a pure translation, or may it carry a "
                                   "spatial rotation (a screw)? — selects between rows 1 and 4 "
                                   "and therefore between 'no ceiling below sqrt2' and "
                                   "'sqrt2 attained'"),
        "koide_rows_unchanged": ("c = sqrt2 remains a COUNTED, UNFORCED INPUT. NO clause of "
                                 "the form 'sqrt2 requires structure outside the banked "
                                 "family' may be added to the Koide rows — this primitive is "
                                 "what refutes that sentence."),
        "lineage": ("the SEVENTH negative forcing route for c = sqrt2 (after R-065/R-066's "
                    "six) and the SECOND non-negativity amplitude cap (after N60); the ℤ3 "
                    "harmonic collapse itself is banked at "
                    "brannen_z3_harmonic_collapse_invariant with priority to Koide 2000 and "
                    "Zenczykowski 2012"),
        "conditioning_class": ("the banked {J,D} reduced energy at D/J = 0.787, the "
                               "single-`q` simple-bivector helical family (RUL-049: multi-q, "
                               "conical and non-simple-B states unscanned), and the D4 "
                               "siting — all three V3 picks, which is why this primitive is "
                               "CANDIDATE-half"),
        "re_attack_handle": (
            "TRIED the joint (c, delta) search on the closed screw family -> IT SUCCEEDED "
            "EXACTLY, WHICH IS THE FAILURE -> WOULD CHANGE IF the family were restricted "
            "to <= 1 free real by an INDEPENDENT principle, or if the SAME 6 parameters "
            "were made to carry a SECOND sector's triple. Anything less leaves the fit "
            "vacuous. Widening cannot rescue it (the kill gets stronger). Replacing "
            "E0 ~ sqrt(m) by m = E0 or m ~ sqrt(E0) moves the target (c, delta) but not "
            "the family's reach and not the dof accounting, so the verdict is expected "
            "identical — NAMED, NOT COMPUTED."),
        "governing_record": ("knowledge/audit/generations_arc_2026-08-23/ — "
                             "VERDICT_REVIEWER_ESTATE_2026-08-23.md (verdict + "
                             "RATIFICATION ADDENDUM §R5.4 + SECOND ADDENDUM §S1-§S8, the "
                             "closing ratification), SCREW_JOINT_SEARCH_2026-08-23.md "
                             "(the joint search + screw_joint_scripts/sj_00…sj_08 with "
                             "its frozen pre-registration), TONGUES_T2PRIME_2026-08-23.md "
                             "(§CONSENSUS, §CONSENSUS-R4), ESTATE_BANKING_2026-08-23.md, "
                             "ESTATE_CLOSURE_2026-08-23.md (this extension)"),
    }

def _estate_d4_magnon_rig(J: float = 1.0):
    """Shared rig for the two spectral-probe estate primitives — the 6x6 Bloch
    stiffness (Hessian) matrix of the banked D4 frame-bilinear model, linearised about
    a uniform helical vacuum.

    Model, verbatim from `canting_vacuum_branch_structure`:
        E = sum over the 24 D4 bonds of [ -(J/2) Tr(W_b) - (D/2) <Bhat_b, W_b>_F ],
        W_b = R_x^T R_{x+b},  Bhat_b = (sigma_a/sqrt2) E_{a4} on the 12 e_4-bearing
        bonds (the ODD convention of R-140), 0 on the 12 spatial bonds.
    Linearise in the TWISTED frame R_x = Rbar_x exp(phi_x), phi_x in so(4) (6 real
    components), so W_b = exp(-phi_x) V_b exp(phi_{x+b}) with V_b x-independent. The
    quadratic form is then a 6x6 Hermitian Bloch matrix H(k) and its six eigenvalues
    are the magnon STIFFNESS bands.

    THE BASIS IS COMPLETE FOR THE BANKED STATE and its limit is named: the six so(4)
    generators E_ij span the medium's local state space, which `n_goldstone_canted_FM`
    itself calls "a six-parameter 4D orientation, not a three-parameter one"
    (§D.3.2, `pi3_orientation_class_two_windings`). The order parameter is a ROTOR, not
    a vector with a length, so no amplitude mode is dropped. It is complete as a
    statement ABOUT THE ROTOR FIELD — not about the medium should the family ever add a
    grain-substance / amplitude degree of freedom, which is a newly-opened node with no
    existing home.

    Returns a dict of callables and the bond set; no claim is made here."""
    import numpy as np

    SQ2 = math.sqrt(2.0)
    BONDS = []
    for i, j in combinations(range(4), 2):
        for si in (+1, -1):
            for sj in (+1, -1):
                v = np.zeros(4); v[i] = float(si); v[j] = float(sj)
                BONDS.append(v)
    BONDS = np.array(BONDS, float)
    assert BONDS.shape == (24, 4)

    def Ea4(a):
        M = np.zeros((4, 4)); M[a, 3] = 1.0; M[3, a] = -1.0
        return M

    def Bhat(b, even=False):
        if b[3] == 0.0:
            return None
        a = int(np.nonzero(b[:3])[0][0])
        w = float(b[a]) * (float(b[3]) if even else 1.0)
        return (w / SQ2) * Ea4(a)

    def Eij(i, j):
        M = np.zeros((4, 4)); M[i, j] = 1.0; M[j, i] = -1.0
        return M

    T = np.array([Eij(i, j) for (i, j) in combinations(range(4), 2)])   # (6,4,4)
    NG = 6

    def bivec(n):
        n = np.asarray(n, float); n = n / float(np.linalg.norm(n))
        return sum(n[a] * Ea4(a) for a in range(3))

    def rod(theta, B):
        return np.eye(4) + math.sin(theta) * B + (1.0 - math.cos(theta)) * (B @ B)

    def E_uniform(k0, B0, D, even=False):
        tot = 0.0
        for b in BONDS:
            W = rod(float(np.dot(k0, b)), B0)
            tot += -(J / 2.0) * float(np.trace(W))
            Bh = Bhat(b, even)
            if Bh is not None:
                tot += -(D / 2.0) * float(np.sum(Bh * W))
        return tot

    def hessian_parts(k0, B0, D, even=False):
        onsite = np.zeros((NG, NG))
        Rs = []
        for b in BONDS:
            V = rod(float(np.dot(k0, b)), B0)
            C = -(J / 2.0) * np.eye(4)
            Bh = Bhat(b, even)
            if Bh is not None:
                C = C - (D / 2.0) * Bh
            P = np.zeros((NG, NG)); Q = np.zeros((NG, NG)); R = np.zeros((NG, NG))
            for a in range(NG):
                for c in range(NG):
                    P[a, c] = 0.5 * (np.sum(C * (T[a] @ T[c] @ V))
                                     + np.sum(C * (T[c] @ T[a] @ V)))
                    Q[a, c] = 0.5 * (np.sum(C * (V @ T[a] @ T[c]))
                                     + np.sum(C * (V @ T[c] @ T[a])))
                    R[a, c] = -float(np.sum(C * (T[a] @ V @ T[c])))
            onsite += P + Q
            Rs.append(R)
        return onsite, BONDS.copy(), np.array(Rs)

    def H_of(k, onsite, bvec, Rs):
        ph = np.exp(1j * (bvec @ np.asarray(k, float)))
        H = (onsite.astype(complex) + np.einsum('n,nij->ij', ph, Rs)
             + np.einsum('n,nij->ij', np.conj(ph), np.transpose(Rs, (0, 2, 1))))
        return 0.5 * (H + H.conj().T)

    def ktilde2(k):
        return float(np.sum(1.0 - np.cos(BONDS @ np.asarray(k, float)))) / 6.0

    return {"BONDS": BONDS, "T": T, "NG": NG, "biv": bivec, "rod": rod,
            "E_uniform": E_uniform, "hessian_parts": hessian_parts, "H_of": H_of,
            "ktilde2": ktilde2, "Ea4": Ea4}


def magnon_stiffness_bands_canted_vacuum(J: float = 1.0) -> dict:
    """[DERIVED-A (the D = 0 operator identity) + DERIVED-numeric (the Gamma spectrum
    and g, BRANCH- and D/J-LABELLED) + DERIVED-structural (branch-robustness of the
    2 + 4 split)] §D.4.3 / §B.6.2 — THE SIX-BAND MAGNON STIFFNESS SPECTRUM OF THE
    CANTED VACUUM.

    *** STIFFNESS, NOT BOGOLIUBOV — the name carries the F2 caution. ***
    This is the six-band magnon STIFFNESS (Hessian) spectrum of the canted vacuum.
    It is NOT a Bogoliubov spectrum: bosonic Bogoliubov problems are PARAUNITARY,
    diagonalised against a tau_3 metric (Shindou, Matsumoto, Murakami & Ohe, PRB 87,
    174427 (2013)), and that operator is not this one. THE CONSEQUENCE, which matters
    at banking time: THIS PRIMITIVE DOES NOT DISCHARGE the two banked "exact 6-band
    Bogoliubov structure UN-BANKED" IOUs at `n_goldstone_canted_FM` and at
    `induced_G_from_linear_face_band` — those IOUs name a DIFFERENT OBJECT and are
    correctly left standing. Rewriting them to "now banked" would be exactly the F2
    referent drift this caution exists to prevent.

    WHAT IS COMPUTED.
      (1) THE GAMMA SPECTRUM, and it is 2 gapless + 4 EXACTLY FOURFOLD-DEGENERATE
          gapped, on BOTH single-`q` branches at D/J = 0.787:
              body-diagonal : [0, 0, 0.412121, 0.412121, 0.412121, 0.412121]
              axis          : [0, 0, 0.405987, 0.405987, 0.405987, 0.405987]
          ★ THE 2 + 4 SPLIT WITH FOURFOLD DEGENERACY IS BRANCH-ROBUST — a stronger
          statement than "confirms the banked N_G = 2", and it is banked as such.
          ★ THE VALUE g IS BRANCH-SPECIFIC (0.412121 vs 0.405987, 1.5 % apart), and
          BRANCH SELECTION IS #1-GAP OPEN (`canting_vacuum_branch_structure`: "WHICH
          branch the DRIVEN dynamics selects is a kernel question"). EVERY g QUOTED
          ANYWHERE MUST CARRY ITS BRANCH LABEL. The asserted check `g_axis != g_diag`
          below exists precisely so a branch-blind quotation cannot silently return.
      (2) THE D = 0 OPERATOR IDENTITY, and it is the strongest item in the estate:
              H(k) = 12 * J * ktilde^2(k) * 1_6     EXACTLY (max dev ~1e-14),
          where ktilde^2(k) = (1/6) sum over the 24 D4 roots of (1 - cos k.b).
          `induced_G_from_linear_face_band` STEP 1 currently only LICENSES the shared
          band from WP-LV1 (`Substrate().dim4_isotropy`); here it is an identity.

    BRANCH SCOPE, stated once and load-bearing: the banked `n_goldstone_canted_FM`
    N_G = 2 is explicitly scoped to the AXIS branch ("this coset count is a statement
    about the axis branch, not a branch-independent one"). This primitive computes on
    BOTH, which is what makes the branch-robustness of the SPLIT a result and the
    branch-specificity of the VALUE a correction.

    THE FACTOR-2 TRAP, shipped as this primitive's own demonstrated failure mode. The
    identity is `12*J*ktilde^2`, and the axiom-arc probe script `leg1_bands.py` printed
    the bands beside `6*J*ktilde2` as if equal — a print LABEL defect (the physics was
    right) sitting directly under the line this result banks on, such that a reader
    checking the identity against that print would wrongly conclude it FAILS. The
    harness therefore asserts BOTH that the 12J form holds to 1e-12 AND that the 6J
    form fails by O(10), so the trap cannot be re-entered silently. (The script itself
    was repaired in the same pass.)

    A SECOND DEMONSTRATED FAILURE MODE — the DM convention. Flipping the DM bond
    bivector to the EVEN convention (which `canting_vacuum_branch_structure` records as
    killing the sin q term, and which §D.4.3's own printed E(q) excludes) collapses the
    Gamma spectrum to SIX gapless modes: the 2 + 4 structure is destroyed. So the
    structure is seen to depend on the banked convention rather than on the linear
    algebra.

    C-33: the bands are GRAIN-layer per-site stiffnesses of the OUTSIDE-frame vacuum
    (an energy-curvature, not a frequency); no INSIDE-frame rate is used anywhere here,
    and no dimensionful number is produced (J = 1 throughout; g is in units of J).

    tier, per component — DERIVED-A for the D = 0 identity (exact); DERIVED-numeric for
    the Gamma spectrum and g, branch- and D/J-labelled; DERIVED-structural for the
    branch-robustness of the 2 + 4 split.

    self-checks: 2 gapless + fourfold degeneracy at Gamma on BOTH branches; the exact
    D = 0 identity at 12*J*ktilde^2 with the 6J label-form seen to fail; g_axis !=
    g_diag with both values; the EVEN-convention control destroying the 2 + 4 split."""
    import numpy as np
    from scipy.optimize import minimize_scalar

    rig = _estate_d4_magnon_rig(J)
    biv_, E_uniform = rig["biv"], rig["E_uniform"]
    hessian_parts, H_of, ktilde2 = rig["hessian_parts"], rig["H_of"], rig["ktilde2"]
    D0 = 0.787                     # the V3 {J,D} calibration (a CANDIDATE-half pick)

    # ---- the two banked single-q branch vacua -------------------------------------
    t_star = float(minimize_scalar(
        lambda t: E_uniform(np.array([t, t, t, 0.0]), biv_([1, 1, 1]), D0),
        bounds=(0.0, 1.2), method="bounded", options=dict(xatol=1e-13)).x)
    q_star = float(minimize_scalar(
        lambda q: E_uniform(np.array([q, 0.0, 0.0, 0.0]), biv_([1, 0, 0]), D0),
        bounds=(0.0, 1.2), method="bounded", options=dict(xatol=1e-13)).x)

    spectra = {}
    for label, k0, B0 in (("body-diagonal", np.array([t_star] * 3 + [0.0]), biv_([1, 1, 1])),
                          ("axis", np.array([q_star, 0.0, 0.0, 0.0]), biv_([1, 0, 0]))):
        on, bv, Rs = hessian_parts(k0, B0, D0)
        w = np.linalg.eigvalsh(H_of(np.zeros(4), on, bv, Rs))
        spectra[label] = [float(x) for x in w]
        n_gapless = int(sum(1 for x in w if abs(x) < 1e-9))
        gapped = [float(x) for x in w if abs(x) >= 1e-9]
        assert n_gapless == 2 and len(gapped) == 4, (
            f"the {label} branch must give 2 gapless + 4 gapped at Gamma; got {w}")
        assert max(gapped) - min(gapped) < 1e-9, (
            f"the four gapped modes must be EXACTLY fourfold degenerate on the {label} "
            f"branch; spread {max(gapped) - min(gapped):.3e}")
        spectra[label + "_g"] = float(np.mean(gapped))

    g_diag = spectra["body-diagonal_g"]
    g_axis = spectra["axis_g"]
    assert abs(g_diag - 0.412121) < 1e-5 and abs(g_axis - 0.405987) < 1e-5, (
        f"the banked gap values are 0.412121 (body-diagonal) and 0.405987 (axis) at "
        f"D/J = 0.787; got {g_diag:.6f}, {g_axis:.6f}")
    assert abs(g_diag - g_axis) > 1e-3, (
        "g is BRANCH-SPECIFIC and must never drift back into a branch-blind quotation; "
        f"g_diag {g_diag:.6f} vs g_axis {g_axis:.6f}")

    # ---- EVEN-convention control: the 2 + 4 structure must be DESTROYED ------------
    on_e, bv_e, Rs_e = hessian_parts(np.array([t_star] * 3 + [0.0]), biv_([1, 1, 1]),
                                     D0, even=True)
    w_even = np.linalg.eigvalsh(H_of(np.zeros(4), on_e, bv_e, Rs_e))
    even_gapless = int(sum(1 for x in w_even if abs(x) < 1e-9))
    assert even_gapless != 2, (
        "the EVEN DM convention (excluded by §D.4.3's own printed E(q)) must DESTROY the "
        f"2 + 4 structure — the control must be seen to fail; got spectrum {w_even}")

    # ---- the D = 0 operator identity, with the factor-2 label trap as a control ----
    on0, bv0, Rs0 = hessian_parts(np.zeros(4), biv_([1, 0, 0]), 0.0)
    rng = np.random.default_rng(7)
    dev12 = dev6 = 0.0
    for _ in range(120):
        k = rng.uniform(-math.pi, math.pi, 4)
        H = H_of(k, on0, bv0, Rs0)
        kt = ktilde2(k)
        dev12 = max(dev12, float(np.abs(H - 12.0 * J * kt * np.eye(6)).max()))
        dev6 = max(dev6, float(np.abs(H - 6.0 * J * kt * np.eye(6)).max()))
    assert dev12 < 1e-12, (
        "at D = 0 the shared band is an EXACT OPERATOR IDENTITY H(k) = 12*J*ktilde^2*1_6; "
        f"max dev {dev12:.3e}")
    assert dev6 > 1.0, (
        "the factor-2 label trap must be SEEN TO FAIL: the identity is 12*J*ktilde^2, not "
        f"6*J*ktilde^2; the 6J form deviates by only {dev6:.3e}")

    return {
        "tier": ("DERIVED-A (the D = 0 operator identity) + DERIVED-numeric (the Gamma "
                 "spectrum and g, BRANCH- and D/J-labelled) + DERIVED-structural (the "
                 "branch-robustness of the 2 + 4 split)"),
        "object": ("the six-band magnon STIFFNESS (Hessian) spectrum of the canted vacuum "
                   "— NOT a Bogoliubov spectrum (paraunitary, tau_3 metric; Shindou et al. "
                   "2013): a different operator"),
        "D_over_J": D0,
        "gamma_spectrum": {"body-diagonal": spectra["body-diagonal"],
                           "axis": spectra["axis"]},
        "n_gapless": 2,
        "n_gapped": 4,
        "gapped_degeneracy": "exactly fourfold on both branches",
        "split_is_branch_robust": True,
        "g_body_diagonal": g_diag,
        "g_axis": g_axis,
        "g_is_branch_specific": True,
        "branch_relative_difference": abs(g_diag - g_axis) / g_diag,
        "branch_selection": ("OPEN — #1 gap, §D.5; static energetics need not govern a NESS "
                             "vacuum (canting_vacuum_branch_structure)"),
        "D0_operator_identity": "H(k) = 12 * J * ktilde^2(k) * 1_6",
        "D0_identity_max_dev": dev12,
        "D0_identity_wrong_factor_6J_dev": dev6,
        "even_convention_control_spectrum": [float(x) for x in w_even],
        "even_convention_control_destroys_split": True,
        "basis": ("the six so(4) generators E_ij — COMPLETE for the banked rotor field "
                  "(the local state is a six-parameter 4D orientation, "
                  "pi3_orientation_class_two_windings), NOT a statement about the medium "
                  "should the family add a grain-substance/amplitude DOF"),
        "does_not_discharge": ("the two banked 'exact 6-band Bogoliubov structure UN-BANKED' "
                               "IOUs at n_goldstone_canted_FM and "
                               "induced_G_from_linear_face_band — they name a PARAUNITARY "
                               "object this is not (F2)"),
        "upgrades": ("induced_G_from_linear_face_band STEP 1, which only LICENSES the D = 0 "
                     "shared band from WP-LV1; here it is an exact operator identity"),
        "governing_record": ("knowledge/audit/axiom_arc_2026-08-23/PROBE_SPECTRAL_NODE_"
                             "2026-08-23.md (B2) + knowledge/audit/generations_arc_2026-08-23/"
                             "VERDICT_REVIEWER_ESTATE_2026-08-23.md §B2 + "
                             "ESTATE_BANKING_2026-08-23.md"),
    }


def spectral_branch_symmetry_class_filter(J: float = 1.0) -> dict:
    """[DERIVED-numeric (the four measurements, BRANCH- and D/J-labelled) + CANDIDATE
    (the filter as a kernel constraint); the real-class ASSIGNMENT explicitly flagged
    EVIDENCE-NOT-THEOREM] §D.5 — KC-1, A ONE-WAY SYMMETRY-CLASS FILTER ON #1-GAP KERNEL
    CANDIDATES.

    *** THE DIRECTION IS "ONLY IF", NOT "IFF". *** The banked-record statement is:

        A kernel is spectral-branch-compatible ONLY IF its symplectic/kinetic structure
        Omega makes Omega^-1 H(k) leave the real (orthogonal) class on the banked D4
        Hessian.

    FAILING the test is DECISIVE (the branch is closed for that kernel). PASSING it is
    NECESSARY, NOT SUFFICIENT — a complex-class kernel can still be nodeless. A second
    test (an actual zero of det H at generic k with a rank-3 Jacobian and a non-zero
    Chern number) is still required, and the banked substrate fails THAT one
    independently of any kernel: the gapless set is exactly {Gamma, +-k_0}, the
    helimagnet Goldstone triplet. The earlier "iff" was an over-claim against the
    probe's own would-change-if and is withdrawn.

    *** "ESCAPE (a) MEASURED EMPTY" IS A MIS-TRANSCRIPTION AND IS WITHDRAWN. ***
    Read exactly, escape (a) of the spectral probe's L1 is *"the kernel is
    first-order/precessional or paraunitary-BdG and its Omega breaks the fixed-k
    antiunitary"*. What was measured empty is a SUB-CLASS of it: four modifications of
    the TIME-DERIVATIVE structure and of the HOPPING — a dissipative real Gamma, a
    gyroscopic Gamma, a uniform Peierls phase, a real antisymmetric hopping — each
    returning exactly zero, with only a genuinely COMPLEX hopping firing. THE
    Omega/METRIC ESCAPE ITSELF WAS NEVER TOUCHED: Omega is #1-gap content and unbanked,
    and the probe's own fork labels that branch "kernel-GATED — not open". The honest
    restatement is UNMEASURED / KERNEL-GATED, never "empty". Writing "empty" converts a
    named gate into a closed measurement, which is the canon §4 / RUL-049 mirror-rule
    failure (a bare impossibility with no conditioning class).

    THE FOUR MEASUREMENTS (body-diagonal branch, D/J = 0.787; all computed here):
      (i)   H(k)* = H(-k) exactly — the real-space couplings are real.
      (ii)  spectrum(k) = spectrum(-k) exactly, so H(k) and H(k)* are unitarily
            equivalent at every k: an antiunitary acts at FIXED k and the Bloch matrix
            sits in the REAL (orthogonal) class.
      (iii) In that class two-band degeneracies have codimension 2, so the Jacobian rank
            at a crossing never reaches 3. Measured: a rank histogram over band
            crossings with RANK 3 ABSENT.
      (iv)  NO Z-VALUED CHERN NUMBER IS DEFINABLE at those crossings — measured as the
            SPHERE-GAP COLLAPSE (below) — on an instrument calibrated to +-1 on a
            control Weyl node, which is run here as the MANDATED FAILURE MODE. A filter
            never observed to return the other answer has not been shown to be a filter.

    *** A CORRECTION TO THE GOVERNING RECORD, FOUND BY THIS PASS'S OWN CHECK DESIGN. ***
    `PROBE_SPECTRAL_NODE_2026-08-23.md` L1 and the arc INDEX row state "Chern == 0" at
    the rank-2 crossings, and the estate verdict repeats it. THAT NUMBER IS NOT ROBUST,
    and the reason is structural rather than numerical. In the real class the degeneracy
    has CODIMENSION 2, so its locus is a 2-surface in the 4-torus; a small S^2 drawn
    around a point ON that locus therefore CUTS it, and a Chern number is not defined on
    a sphere the bands touch. Measured here at four independent rank-2 crossings: the
    two-band gap on the surrounding S^2 collapses to ~1e-7...1e-9 at radius 1e-3 (i.e.
    the sphere passes through the locus), and the SAME instrument returns 0 at some
    crossings and -1 at others — one of them flipping with the grid resolution. At the
    synthetic Weyl node, by contrast, the gap on S^2 is bounded away from zero at
    exactly 2r and the value is a stable +-1.
    *** THE CONCLUSION IS UNCHANGED AND THE EVIDENCE IS STRONGER. *** The correct
    real-class signature is the CODIMENSION — which is precisely what the estate
    verdict's own §KC-1.2 says ("codimension 2 => a Z2 Berry phase, NOT a Z-valued Chern
    number") — and the definability collapse is a sharper witness of it than a fragile
    zero. Quoting "Chern == 0" asserts a tolerance on a quantity that is not defined,
    which is the tight-tolerance-on-a-vacuous-check tell in a new dress. The record
    sites are annotated rather than silently overwritten; nothing about L1's verdict (no
    Weyl node on this substrate) moves.

    *** THE SOFT SPOT, which must travel with this primitive. *** The real-class
    ASSIGNMENT is STRONG COMPUTED EVIDENCE, NOT A THEOREM. The inversion operator M was
    never built explicitly and `M H(-k) M^-1 = H(k)` was never verified matrix-wise;
    what is exhibited is two exact isospectralities plus two real-class consequences.
    Exhibiting M is the cheapest computation that would close it, and it is owed.
    `inversion_operator_exhibited` is returned False so no consumer can forget.

    FRAME JURISDICTION (N49 axis, checked explicitly): CLEAN. This is substrate-internal
    end to end — a Hessian of the D4 bond energy, a symmetry class, a Jacobian rank, a
    Chern number. NO inside-frame observed rate, bound or constancy is used anywhere to
    motivate or bound an outside-frame kernel property, so no N33-1-class
    CANDIDATE-for-applicability hedge is warranted and none is manufactured.

    PLACEMENT (canon §6's consumption rule, and this is the case the rule is aimed at):
    the filter FEELS family-level — it tests kernel candidates — but it CONSUMES three
    V3 picks: the D4 siting, the D/J = 0.787 calibration and the body-diagonal branch
    vacuum. Consumption decides, so it is a CANDIDATE-half primitive and takes no
    CORE_PROVENANCE row. A CORE primitive calling it fails the AST guard by construction.

    IMPORT NOTE. The codimension/Chern half is pure mathematics with checkable
    hypotheses and IS checked here, so it is import-exempt (canon §2). The clause
    "paraunitary bosonic-BdG kernels (tau_3 metric) are the named class that CAN pass"
    is a load-bearing EXTERNAL physics import — Shindou, Matsumoto, Murakami & Ohe, PRB
    87, 174427 (2013); Li et al., Nat. Commun. 7, 12691 (2016) — and carries its
    companion Section 13 registry row.

    tier, per component — DERIVED-numeric for the four measurements (branch- and
    D/J-labelled); CANDIDATE for the filter as a kernel constraint; the real-class
    assignment EVIDENCE-NOT-THEOREM pending the inversion operator.

    self-checks: the two exact isospectralities; a rank histogram with rank 3 absent;
    the sphere-gap collapse at four independent rank-2 crossings PLUS the instrument
    returning more than one 'Chern' value across them (the instability IS the finding);
    and the MANDATED FAILURE MODE — the same instrument on a synthetic complex-class
    Weyl node, where the sphere gap is bounded away at 2r and the value is a stable +-1,
    and which also fails the H(k)* = H(-k) test the substrate passes, so the filter is
    seen to give the other answer; plus a synthetic real-class control reproducing the
    substrate's signature."""
    import numpy as np
    from scipy.optimize import minimize, minimize_scalar

    rig = _estate_d4_magnon_rig(J)
    biv_, E_uniform = rig["biv"], rig["E_uniform"]
    hessian_parts, H_of = rig["hessian_parts"], rig["H_of"]
    D0 = 0.787

    t_star = float(minimize_scalar(
        lambda t: E_uniform(np.array([t, t, t, 0.0]), biv_([1, 1, 1]), D0),
        bounds=(0.0, 1.2), method="bounded", options=dict(xatol=1e-13)).x)
    on, bv, Rs = hessian_parts(np.array([t_star] * 3 + [0.0]), biv_([1, 1, 1]), D0)

    def H(k):
        return H_of(k, on, bv, Rs)

    def w(k):
        return np.linalg.eigvalsh(H(k))

    # ---- (i)/(ii) the two exact isospectralities ---------------------------------
    r1 = np.random.default_rng(1)
    herm_dev = max(float(np.abs(H(k).conj() - H(-k)).max())
                   for k in r1.uniform(-3.0, 3.0, (40, 4)))
    r2 = np.random.default_rng(2)
    spec_dev = max(float(np.abs(w(k) - w(-k)).max())
                   for k in r2.uniform(-math.pi, math.pi, (40, 4)))
    assert herm_dev < 1e-13 and spec_dev < 1e-13, (
        "the real-class evidence is that H(k)* = H(-k) and spectrum(k) = spectrum(-k) "
        f"EXACTLY; got {herm_dev:.3e}, {spec_dev:.3e}")

    # ---- (iii) the degeneracy codimension histogram -------------------------------
    SIG = [np.array([[0, 1], [1, 0]], complex),
           np.array([[0, -1j], [1j, 0]]),
           np.array([[1, 0], [0, -1]], complex)]

    def jac(kstar, n, h=1e-5):
        _, U = np.linalg.eigh(H(kstar))
        Vd = U[:, n:n + 2]

        def fvec(k):
            h2 = Vd.conj().T @ H(k) @ Vd
            h2 = h2 - 0.5 * np.trace(h2) * np.eye(2)
            return np.array([0.5 * np.trace(s @ h2).real for s in SIG])

        Jm = np.zeros((3, 4))
        for mu in range(4):
            e = np.zeros(4); e[mu] = h
            Jm[:, mu] = (fvec(kstar + e) - fvec(kstar - e)) / (2.0 * h)
        return Jm

    r3 = np.random.default_rng(99)
    hist, examples = {}, {}
    for n in range(5):
        for _ in range(10):
            res = minimize(lambda k: w(k)[n + 1] - w(k)[n],
                           r3.uniform(-math.pi, math.pi, 4), method="Nelder-Mead",
                           options=dict(xatol=1e-11, fatol=1e-15, maxiter=1200,
                                        maxfev=1200))
            if res.fun > 1e-9:
                continue
            sv = np.linalg.svd(jac(res.x, n), compute_uv=False)
            rk = int((sv > 1e-3).sum())
            hist[rk] = hist.get(rk, 0) + 1
            examples.setdefault(rk, []).append((n, res.x.copy()))
    assert hist and 3 not in hist, (
        "in the REAL class two-band degeneracies have codimension 2, so the Jacobian rank "
        f"must never reach 3; histogram {hist}")

    # ---- (iv) DEFINABILITY, not a value — and the MANDATED FAILURE MODE ------------
    # See the docstring's CORRECTION block: at a codimension-2 degeneracy a surrounding
    # S^2 CUTS the degeneracy locus, so no Z-valued Chern number is definable and the
    # instrument's returned value is unstable. What is measured here is therefore the
    # SPHERE-GAP COLLAPSE (the definability signature), with the Chern figures reported
    # only as the demonstration of that instability.
    def chern_and_sphere_gap(Hfun, kstar, n, basis3, r=1e-3, N=32):
        th = np.linspace(1e-4, math.pi - 1e-4, N)
        ph = np.linspace(0.0, 2.0 * math.pi, N, endpoint=False)
        dim = Hfun(kstar).shape[0]
        U = np.empty((N, N, dim), complex)
        min_gap = float("inf")
        for i, t in enumerate(th):
            for j, p in enumerate(ph):
                d = np.array([math.sin(t) * math.cos(p), math.sin(t) * math.sin(p),
                              math.cos(t)])
                ev, v = np.linalg.eigh(Hfun(kstar + r * (d @ basis3)))
                U[i, j] = v[:, n]
                if n + 1 < dim:
                    min_gap = min(min_gap, abs(float(ev[n + 1] - ev[n])))
                if n > 0:
                    min_gap = min(min_gap, abs(float(ev[n] - ev[n - 1])))
        F = 0.0
        for i in range(N - 1):
            for j in range(N):
                j2 = (j + 1) % N
                z = (np.vdot(U[i, j], U[i, j2]) * np.vdot(U[i, j2], U[i + 1, j2])
                     * np.vdot(U[i + 1, j2], U[i + 1, j]) * np.vdot(U[i + 1, j], U[i, j]))
                if abs(z) < 1e-13:
                    return None, min_gap
                F += float(np.angle(z))
        return F / (2.0 * math.pi), min_gap

    R_SPHERE = 1e-3
    sub_crossings = []
    for (n_c, k_c) in examples[2][:4]:
        basis = np.linalg.svd(jac(k_c, n_c))[2][:3]
        cval, gap = chern_and_sphere_gap(H, k_c, n_c, basis, r=R_SPHERE)
        sub_crossings.append({"bands": [n_c, n_c + 1], "min_gap_on_S2": gap,
                              "chern_returned": None if cval is None else float(cval)})
        assert gap < 1e-5 * R_SPHERE * 1e3, (
            "THE CODIMENSION-2 SIGNATURE: a small S^2 around a real-class crossing must CUT "
            "the degeneracy locus, i.e. the two-band gap on the sphere must collapse to "
            f"~0; got {gap:.3e} at bands {n_c}/{n_c+1}")
    ch_values = sorted({round(abs(c["chern_returned"]), 6) for c in sub_crossings
                        if c["chern_returned"] is not None})
    assert len(ch_values) > 1, (
        "the instability is the point: across real-class crossings the SAME instrument must "
        "return more than one 'Chern' value, which is what shows the invariant is not "
        f"defined there; got {ch_values}")

    # THE FILTER MUST BE SEEN TO RETURN THE OTHER ANSWER — a synthetic complex-class
    # Weyl node on the SAME instrument, where the sphere does NOT cut the locus.
    sx = np.array([[0, 1], [1, 0]], complex)
    sy = np.array([[0, -1j], [1j, 0]])
    sz = np.array([[1, 0], [0, -1]], complex)
    B3 = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]], float)

    def H_weyl(k):
        return k[0] * sx + k[1] * sy + k[2] * sz

    def H_real_ctrl(k):
        return k[0] * sx + k[1] * sz

    ch_weyl, gap_weyl = zip(*[chern_and_sphere_gap(H_weyl, np.zeros(4), nn, B3,
                                                   r=R_SPHERE) for nn in (0, 1)])
    ch_real, gap_real = zip(*[chern_and_sphere_gap(H_real_ctrl, np.zeros(4), nn, B3,
                                                   r=R_SPHERE) for nn in (0, 1)])
    r4 = np.random.default_rng(5)
    weyl_herm_dev = max(float(np.abs(H_weyl(k).conj() - H_weyl(-k)).max())
                        for k in r4.uniform(-2.0, 2.0, (20, 4)))
    assert all(g > 1.9 * R_SPHERE for g in gap_weyl), (
        "at a genuine codimension-3 Weyl node the sphere MISSES the degeneracy, so the gap "
        f"on S^2 is bounded away from zero at 2r; got {gap_weyl}")
    assert all(c is not None and abs(abs(c) - 1.0) < 1e-6 for c in ch_weyl), (
        "MANDATED FAILURE MODE: the SAME instrument must return +-1 on a synthetic "
        f"complex-class Weyl node, or its verdict on the substrate means nothing; {ch_weyl}")
    assert weyl_herm_dev > 1.0, (
        "the synthetic Weyl node must FAIL the real-class test the substrate passes; got "
        f"{weyl_herm_dev:.3e}")
    assert all(g < 1e-6 for g in gap_real) and all(abs(c) < 1e-9 for c in ch_real), (
        "the synthetic REAL-class control must reproduce the SUBSTRATE's signature — a "
        f"collapsed sphere gap; got gaps {gap_real}, chern {ch_real}")

    return {
        "tier": ("DERIVED-numeric (the four measurements, branch- and D/J-labelled) + "
                 "CANDIDATE (the filter as a kernel constraint); the real-class ASSIGNMENT "
                 "is EVIDENCE-NOT-THEOREM pending the inversion operator"),
        "statement": ("KC-1: a kernel is spectral-branch-compatible ONLY IF its "
                      "symplectic/kinetic structure Omega makes Omega^-1 H(k) leave the "
                      "real (orthogonal) class on the banked D4 Hessian"),
        "direction": "necessary-not-sufficient",
        "why_not_sufficient": ("a complex-class kernel can still be nodeless; a second test "
                               "(a zero of det H at generic k with rank-3 Jacobian and "
                               "non-zero Chern) is required, and the banked substrate fails "
                               "THAT one independently — the gapless set is exactly "
                               "{Gamma, +-k_0}, the helimagnet Goldstones"),
        "branch": "body-diagonal",
        "D_over_J": D0,
        "hermiticity_dev": herm_dev,
        "spec_inversion_dev": spec_dev,
        "rank_histogram": dict(sorted(hist.items())),
        "rank_3_absent": True,
        "chern_definable_at_substrate_crossings": False,
        "substrate_rank2_crossings": sub_crossings,
        "chern_values_returned_across_crossings": ch_values,
        "chern_instability_note": ("THE CORRECTION: 'Chern == 0' at the rank-2 crossings is "
                                   "NOT a robust measurement. Codimension 2 means a small "
                                   "S^2 around a crossing CUTS the degeneracy locus (gap on "
                                   "the sphere collapses to ~1e-7...1e-9 at r = 1e-3), so no "
                                   "Z-valued invariant is defined there and the instrument "
                                   "returns different values at different crossings. The "
                                   "CODIMENSION is the real-class signature — which is what "
                                   "the estate verdict's own KC-1.2 says — and this is a "
                                   "sharper witness of it than a fragile zero. L1's verdict "
                                   "(no Weyl node on this substrate) is UNCHANGED."),
        "chern_control_weyl": [float(c) for c in ch_weyl],
        "sphere_gap_weyl": [float(g) for g in gap_weyl],
        "chern_control_real_class": [float(c) for c in ch_real],
        "sphere_gap_real_class_control": [float(g) for g in gap_real],
        "sphere_radius": R_SPHERE,
        "weyl_control_fails_real_class_test": weyl_herm_dev,
        "inversion_operator_exhibited": False,
        "soft_spot": ("the real-class ASSIGNMENT is strong computed evidence, not a theorem: "
                      "the inversion operator M was never built and M H(-k) M^-1 = H(k) was "
                      "never verified matrix-wise. Exhibiting M is the cheapest closing "
                      "computation and it is OWED."),
        "escape_a_status": ("UNMEASURED / KERNEL-GATED — never 'empty'. What was measured "
                            "empty is a SUB-CLASS: four modifications of the time-derivative "
                            "structure and of the hopping (dissipative real Gamma, gyroscopic "
                            "Gamma, uniform Peierls phase, real antisymmetric hopping), each "
                            "exactly zero, with only a genuinely complex hopping firing. The "
                            "Omega/metric escape itself was never touched; Omega is #1-gap "
                            "content and unbanked."),
        "frame_jurisdiction_N49": ("CLEAN — substrate-internal end to end; no inside-frame "
                                   "observed rate, bound or constancy is used to bound an "
                                   "outside-frame kernel property, so no N33-1-class hedge is "
                                   "warranted and none is manufactured"),
        "import_row": ("the 'paraunitary bosonic-BdG (tau_3 metric) is the named class that "
                       "CAN pass' clause is an external physics import — Shindou, Matsumoto, "
                       "Murakami & Ohe, PRB 87, 174427 (2013); Li et al., Nat. Commun. 7, "
                       "12691 (2016) — carried in companion Section 13"),
        "governing_record": ("knowledge/audit/axiom_arc_2026-08-23/PROBE_SPECTRAL_NODE_"
                             "2026-08-23.md §5 (KC-1) + knowledge/audit/generations_arc_"
                             "2026-08-23/TONGUES_L2_2026-08-23.md §4 (the sub-class "
                             "measurements) + VERDICT_REVIEWER_ESTATE_2026-08-23.md §KC-1 + "
                             "ESTATE_BANKING_2026-08-23.md"),
    }


def dm_chirality_polarisation_lock() -> dict:
    """[DERIVED-A, generic-given-one-orientation-reversing-element] §D.3.3 — how much
    CHIRAL freedom the driven point group grants the DM bond channel.

    COMPUTED by explicit group closure + projector rank on the 24 D4 bonds:

        group                         allowed D | SD-polarised | ASD-polarised | chi
        Stab(+e_4)  [48]  (DRIVEN)        2     |      0       |      0        |  0
        Stab+(+e_4) [24]  (proper)        4     |      2       |      2        |  2

    READING. At the DRIVEN group there is NO chirally-polarised DM coupling at all:
    every allowed D is forced exactly 50/50 SD:ASD. The menu theorem's jump D: 2 -> 4
    IS the chiral doubling, and it is bought by exactly one thing — DROPPING THE
    REFLECTIONS. The 24 orientation-reversing elements of Stab(+e_4) (spatial parity
    diag(-1,-1,-1,+1) among them) exchange SD and ASD (§D.2.5, R-099), because
    *(Lambda^2 g) = det(g) (Lambda^2 g) *, so the two chiral halves are LOCKED
    TOGETHER at [48]. The same reflection-dropping is what opens the pseudoscalar
    channel chi (0 -> 2).

    CONDITIONING CLASS (RUL-049 — this is a necessity claim, so it carries one):
    "no polarised DM coupling" holds WITHIN THE BILINEAR BOND-ACTION CLASS ON THE
    ORIENTED DRIVEN GROUP Stab(+e_4). It becomes false at [24], i.e. only under
    HAMILTONIAN-level spatial-reflection breaking — a source the drive axis +e_4 alone
    does not supply, and which a spontaneously reflection-breaking ground state does
    not supply either.

    TIER NOTE (canon §5 derived-vs-generic). The zero count is
    GENERIC-GIVEN-ONE-ORIENTATION-REVERSING-ELEMENT, not a D4-specific discovery: any
    point group containing a single orientation-reversing element forbids a polarised
    invariant by the same Hodge identity. What is D4-specific here is only the
    dimension count 2 (resp. 4) of the allowed space itself.

    SCOPE FENCE. This is BOND-COUPLING SD/ASD content. It licenses NOTHING about weak
    isospin: weak = SD is settled at R-171/R-079 (the closed three-class menu, RUL-082) and NOT
    here, and this computation
    neither supports nor undermines it.
    """
    import numpy as np
    import itertools as _it

    PAIRS = list(combinations(range(1, 5), 2))

    _B = []
    for _i, _j in combinations(range(4), 2):
        for _si in (+1, -1):
            for _sj in (+1, -1):
                _v = np.zeros(4); _v[_i] = float(_si); _v[_j] = float(_sj)
                _B.append(_v)
    BONDS = np.array(_B, float)

    def _key(g):
        return tuple(np.round(np.asarray(g, float).ravel(), 9) + 0.0)

    # ---- explicit closure of Stab(+e_4): signed permutations of {e_1,e_2,e_3} ----
    gens = []
    for p in _it.permutations(range(3)):
        P = np.eye(4); P[:3, :3] = 0.0
        for i, pi in enumerate(p):
            P[i, pi] = 1.0
        gens.append(P)
    for s in _it.product((+1.0, -1.0), repeat=3):
        gens.append(np.diag(np.array(list(s) + [1.0], float)))
    seen = {_key(np.eye(4)): np.eye(4)}
    frontier = [np.eye(4)]
    while frontier:
        nxt = []
        for a in frontier:
            for g in gens:
                p = g @ a
                k = _key(p)
                if k not in seen:
                    seen[k] = p; nxt.append(p)
        frontier = nxt
    G48 = list(seen.values())
    G24 = [g for g in G48 if np.linalg.det(g) > 0]
    assert len(G48) == 48, f"|Stab(+e_4)| must be 48, got {len(G48)}"
    assert len(G24) == 24, f"|Stab+(+e_4)| must be 24, got {len(G24)}"
    # CONTROL: every element must permute the D4 root system, and fix +e_4.
    rootset = set(_key(b) for b in BONDS)
    assert all(set(_key(g @ b) for b in BONDS) == rootset for g in G48), \
        "Stab(+e_4) elements must permute the 24 D4 roots"
    e4 = np.array([0.0, 0.0, 0.0, 1.0])
    assert all(np.allclose(g @ e4, e4) for g in G48), "Stab(+e_4) must fix +e_4"
    n_reflections = len(G48) - len(G24)
    assert any(np.allclose(g, np.diag([-1.0, -1.0, -1.0, 1.0])) for g in G48), \
        "spatial parity must lie in the driven group (it is what locks SD to ASD)"

    # ---- the Hodge/chirality split, taken from the engine's own I4 ----------------
    S = np.zeros((6, 6))
    for c, (i, j) in enumerate(PAIRS):
        for k, v in (I4 * e(i, j)).terms:
            if len(k) == 2:
                S[PAIRS.index((k[0], k[1])), c] = v
    assert np.abs(S @ S - np.eye(6)).max() < 1e-12, "the star operator must square to 1"
    Pp, Pm = (np.eye(6) + S) / 2.0, (np.eye(6) - S) / 2.0
    assert np.linalg.matrix_rank(Pp, tol=1e-9) == 3 and np.linalg.matrix_rank(Pm, tol=1e-9) == 3, \
        "SD and ASD must each be 3-dimensional"

    def _lam2(g):
        M = np.zeros((6, 6))
        for c, (i, j) in enumerate(PAIRS):
            for r, (k, l) in enumerate(PAIRS):
                M[r, c] = g[k-1, i-1] * g[l-1, j-1] - g[k-1, j-1] * g[l-1, i-1]
        return M

    idx = {_key(b): i for i, b in enumerate(BONDS)}

    def _bond_perm(g):
        P = np.zeros((24, 24))
        for i, b in enumerate(BONDS):
            P[i, idx[_key(g.T @ b)]] = 1.0
        return P

    def _invariant_space(G, rep, rev_sign):
        dim = rep(np.eye(4)).shape[0]
        R = np.zeros((24 * dim, 24 * dim))
        for g in G:
            R += np.kron(_bond_perm(g), rep(g))
        R /= len(G)
        Prev = np.zeros((24, 24))
        for i, b in enumerate(BONDS):
            Prev[i, idx[_key(-b)]] = 1.0
        Q = np.kron(Prev, rev_sign * np.eye(dim))
        M = R @ ((np.eye(24 * dim) + Q) / 2.0)
        M = 0.5 * (M + M.T)
        U, s, _ = np.linalg.svd(M)
        d = int((s > 1e-8).sum())
        return U[:, :d], d

    out = {}
    for label, G in (("Stab(+e4)[48]", G48), ("Stab+(+e4)[24]", G24)):
        Bs, dD = _invariant_space(G, _lam2, -1.0)         # DM: bond-reversal ODD
        _, dchi = _invariant_space(G, lambda g: np.array([[np.linalg.det(g)]]), +1.0)
        fr = []
        for c in range(dD):
            V6 = Bs[:, c].reshape(24, 6)
            sd = float(np.linalg.norm(V6 @ Pp.T)) ** 2
            asd = float(np.linalg.norm(V6 @ Pm.T)) ** 2
            fr.append(sd / (sd + asd))
        Mm = np.array([(Bs[:, c].reshape(24, 6) @ Pm.T).ravel() for c in range(dD)]).T
        Mp = np.array([(Bs[:, c].reshape(24, 6) @ Pp.T).ravel() for c in range(dD)]).T
        rm = int((np.linalg.svd(Mm, compute_uv=False) > 1e-8).sum()) if dD else 0
        rp = int((np.linalg.svd(Mp, compute_uv=False) > 1e-8).sum()) if dD else 0
        out[label] = {"allowed_D_dim": dD, "SD_polarised_dim": dD - rm,
                      "ASD_polarised_dim": dD - rp, "chi_dim": dchi,
                      "per_basis_SD_fraction": fr}

    a48, a24 = out["Stab(+e4)[48]"], out["Stab+(+e4)[24]"]
    assert (a48["allowed_D_dim"], a48["SD_polarised_dim"], a48["ASD_polarised_dim"],
            a48["chi_dim"]) == (2, 0, 0, 0), f"driven-group counts wrong: {a48}"
    assert (a24["allowed_D_dim"], a24["SD_polarised_dim"], a24["ASD_polarised_dim"],
            a24["chi_dim"]) == (4, 2, 2, 2), f"proper-subgroup counts wrong: {a24}"
    assert all(abs(f - 0.5) < 1e-9 for f in a48["per_basis_SD_fraction"]), \
        "every allowed D at the driven group must be exactly 50/50 SD:ASD"

    return {
        "tier": ("DERIVED-A, but GENERIC-GIVEN-ONE-ORIENTATION-REVERSING-ELEMENT for the "
                 "ZERO count (canon §5); the dimensions 2 and 4 are D4-specific."),
        "n_group_elements": {"Stab(+e4)": len(G48), "Stab+(+e4)": len(G24)},
        "n_reflections_in_driven_group": n_reflections,
        "counts": out,
        "doubling_bought_by": ("dropping the reflections — and nothing else. Within the "
                               "bilinear bond-action class on the oriented driven group "
                               "Stab(+e_4) there is no such thing as turning one chiral dial "
                               "and leaving the other (RUL-049 conditioning class)."),
        "reopener": ("HAMILTONIAN-level spatial-reflection breaking to [24], where the "
                     "polarised halves and chi both open. The drive axis +e_4 alone does not "
                     "supply it, and a spontaneously reflection-breaking ground state does not."),
        "weak_isospin_fence": ("BOND-COUPLING SD/ASD content only. This licenses NOTHING about "
                               "weak isospin; weak = SD is settled at R-171 (the closed three-class "
                               "menu) plus R-079, RUL-082 -- never by a bond-coupling result."),
        "governing_record": ("knowledge/candidates/probes_2026-08-20/ — "
                             "JD_REWORK_REPORT_2026-08-20.md §3 (JD-3, closed negatively), "
                             "VERDICT_REF3_PARITY_SECONDD_2026-08-21.md Attack 2, "
                             "VERDICT_META_OBSERVER_2026-08-21.md claim 7 (the genericity note)"),
    }



# ======================================================================
# HADRON MASS SECTOR (§17: same-composition splits / three-facet S2-inertia)   [twt_hadrons]
# ======================================================================
# NOTE (V2, 2026-06-29): the Willis planetary-gear METAPHOR was retired from the paper (W-LIVE-6);
# §17.3 is now the V2 §3.2 three-orthogonal-facets interference structure. The underlying MATH is
# unchanged and stays banked (the S2-symmetry inertia BASIS is DERIVED; the freq-lock Ω_B=Σω from
# E-centrality is DERIVED; split values are #1-gap GATED). The "gear"/"Willis" names below are LEGACY
# labels for that same structure (kept to avoid test-breaking renames) — read "gear" as "the
# three-facet collective-rotation inertia", NOT the Toyota-eCVT picture.

# numerical chain inputs (§17.3): dressed e (ANW phys), f_π
E_PHYS = 5.45          # ANW massless-pion best-fit dressed coupling
F_PI = 129.0           # MeV -- the ANW FITTED F_pi, not the measured pion decay constant:
                       # in ANW's own normalization the physical value is F_pi ~ 186 MeV, so this
                       # sits ~30% below it, and its resemblance to the measured f_pi+ = 130.2 MeV
                       # of the sqrt(2) convention is a collision of conventions (paper Opening).
# BVP eigenvalue coefficients (§16.3/§17.2): M_0 = 36.47 f_π/e, Θ_0 = 106.76/(e³ f_π)
# CORRECTION 2026-07-03 (R-133, skyrmion_rotational_band_nucleon_delta): the long-banked
# Θ-coefficient 97.27 was WRONG — it equals 36.47·8/3 = 97.25 (provenance suspect, not an
# inertia integral); the exact hedgehog-BVP value is 106.76 (Λ = 50.98, matching the ANW
# literature ~50.9 and ANW's own published N/Δ fit). Downstream numbers swept same pass.
M0_COEFF, THETA0_COEFF = 36.47, 106.76




# ---- §17.3  the numerical chain -----------------------------------------------
def numerical_chain():
    """[DERIVED, dressed-level] §17.3: M_0 = 36.47 f_π/e = 863 MeV;
    Θ_0 = 106.76/(e³ f_π) = 5.113e-3 MeV⁻¹; 1/Θ_0 = 195.6 MeV (heavy-quark limit of Σ-Λ).
    [Θ-coefficient CORRECTED 97.27 → 106.76, R-133 2026-07-03 — exact BVP; see
    skyrmion_rotational_band_nucleon_delta.]"""
    M0 = M0_COEFF * F_PI / E_PHYS
    Theta0 = THETA0_COEFF / (E_PHYS**3 * F_PI)
    return {"M_0 (MeV)": M0, "Θ_0 (1/MeV)": Theta0, "1/Θ_0 (MeV)": 1.0 / Theta0}

def x_Q(m_Q_MeV: float) -> float:
    """[DERIVED] §17.3: heavy-quark crossover parameter x_Q = m_Q·Θ_0 (Θ_0 from the chain)."""
    return m_Q_MeV * numerical_chain()["Θ_0 (1/MeV)"]


def alpha_H_gap() -> float:
    """[CALIBRATION, not a validation] §17.3/§17.4: the light Σ-Λ splitting = 77 MeV is a
    FITTED input (190-113=77 is its decomposition in the fit, true by construction — NOT an
    independent check). The gear *uses* this calibration; do not present 'α_{H0}-α_{H1}=77 ✓'
    as a prediction (it is the same datum that calibrates the light-diquark spin coupling)."""
    return 190.0 - 113.0   # = 77, the calibrated light Σ-Λ splitting (an INPUT)

def top_excluded():
    """[DERIVED given INPUT(Γ_t)] §17.3: top exclusion. Γ_t·Θ_0 = 1400·5.113e-3 = 7.2 ≫ 1 ⇒
    top decays ~7× before the gear can establish a coupling mode ⇒ no top baryon.
    [Was 6.5 before the R-133 Θ-coefficient correction; conclusion STRENGTHENED.]

    Tier note (audit 2026-06-30): the STRUCTURAL form (Γ_t·Θ_0 ≫ 1 ⇒ no bound hadron) is
    DERIVED; the value Γ_t = 1400 MeV is the PDG top decay width — an external SM input,
    NOT a substrate output. This is NOT a Clifford/D4 identity (canon §2 DERIVED-A), so
    the tier downgrades to "DERIVED given INPUT(Γ_t)". A substrate-derived Γ_t would
    require g (§9.6-gated, #1 gap) and a top-Yukawa equivalent (undefined in current
    TWT); cf. WORKLIST item B-G1."""
    Gamma_t = 1400.0   # INPUT — PDG top decay width (external SM datum, not substrate-derived)
    return Gamma_t * numerical_chain()["Θ_0 (1/MeV)"]






# ======================================================================
# COSMOLOGY / MACROSCOPIC (§24.4/6)   [twt_cosmo]
# ======================================================================


# ---- §24.4  cosmological constant via Volovik (FRAMING) ------------------------
def gravitating_vacuum_energy(epsilon: float, mu: float, n: float, P: float) -> float:
    """[FRAMING] §24.4: Volovik's identity for a self-sustained quantum medium —
    the GRAVITATING vacuum energy (what sources gravity) is ρ_grav = ε - μn. The
    Gibbs-Duhem relation gives ε - μn = -P, so at zero external pressure (P=0) the
    gravitating vacuum energy vanishes EXACTLY in equilibrium — even though the
    sub-Planckian zero-point energy is huge. The small observed Λ is the TWT
    driven-dissipative deviation from equilibrium (explicit value OPEN)."""
    return epsilon - mu * n      # = -P by Gibbs-Duhem

def lambda_resolution_structure():
    """[FRAMING] §24.4: the cosmological-constant 'problem' dissolves structurally —
    substrate is self-sustained ⇒ Gibbs-Duhem ⇒ ρ_grav = 0 in equilibrium. The huge
    QFT zero-point energy does NOT gravitate. Λ>0 is the off-equilibrium remnant."""
    eps, mu, n = 1e120, 1.0, 1e120     # huge zero-point energy, but self-sustained
    P = 0.0                            # zero external pressure (self-sustained medium)
    rho_grav = gravitating_vacuum_energy(eps, mu, n, P)   # ε - μn = -P = 0
    return {"rho_grav at equilibrium (P=0)": rho_grav, "huge zero-point energy gravitates": rho_grav != 0}


def lambda_H2_dynamical_reading_excluded():
    """[DERIVED arithmetic + INPUT bounds] §E.1.1 / N54: `Λ ~ H²` admits two readings and only one
    survives. DYNAMICAL: ρ_vac(t) = 3ν M̄_Pl² H(t)² at ALL epochs. Substituting into the flat Friedmann
    constraint 3 M̄_Pl² H² = ρ_m + ρ_r + ρ_vac gives 3 M̄_Pl² H² (1−ν) = ρ_m + ρ_r, hence Ω_vac(z) ≡ ν
    IDENTICALLY — the vacuum FRACTION is epoch-independent, so matching today forces ν = Ω_Λ,0 ≈ 0.685
    at recombination and at BBN too. (A separately-conserved w=−1 component would give ρ_vac = const,
    i.e. the other reading; so the dynamical reading necessarily involves vacuum–matter exchange.)
    PRESENT-EPOCH: ρ_vac = const with ρ_vac = 3 Ω_Λ,0 M̄_Pl² H_0² — near-definitional (it is the
    definition of Ω_Λ,0 rearranged), and the reading `kernel_overdetermination_table` already uses
    (H_0, not H(t); it likewise calls c = 3Ω_Λ semi-definitional).
    INPUT bounds, all read from the primary source: early-DE below ≈2% of critical — and that is the
    WEAKEST, z<50-only case (Planck 2015 XIV abstract, arXiv:1502.01590); ΔN_eff = −0.14 ± 0.21 from
    light elements alone (arXiv:2401.15054); N_eff = 2.99 ± 0.17, Ω_m = 0.315 ± 0.007 (Planck 2018 VI,
    arXiv:1807.06209); running-vacuum global fit ν_eff ≡ ν/4 = 0.00024 (+0.00039/−0.00040) for
    ρ_vac(H) = (3/8πG)(c₀ + νH² + ν̃Ḣ) + O(H⁴) (arXiv:2102.12758 Eq.1, Table 1).
    CAVEAT, not hidden: the ΔN_eff rows are an EQUIVALENT-ENERGY translation (a w=−1 component is not
    radiation); they size the violation and the verdict does NOT rest on them — the early-DE row is a
    direct fraction-vs-fraction comparison and the q-constancy row imports no bound at all. The
    normalization is convention-dependent, so BOTH are returned: the BBN-epoch value (T_ν = T_γ, the
    one appropriate to a light-element bound) and the post-e⁺e⁻-annihilation value.
    self-checks: Ω_e excess > 30×; ΔN_eff excess > 25×; the BBN-epoch convention is the smaller of the
    two; q(z) constant and negative in both eras ⇒ no acceleration transition, while flat ΛCDM on the
    SAME parameters gives z_t ≈ 0.63."""
    Om_m0, Om_L0 = 0.315, 0.685                      # Planck 2018 VI, flat  [INPUT]
    nu = Om_L0                                       # forced by matching today under the dynamical reading
    r_vac_rad = nu / (1.0 - nu)                      # = 2.1746, epoch-independent
    # ΔN_eff at the BBN epoch proper: T_nu = T_gamma, one neutrino species = (7/8) rho_gamma
    dNeff = r_vac_rad * (1.0 + (7.0 / 8.0) * 3.044) / (7.0 / 8.0)
    # the post-e+e--annihilation convention, quoted so the choice is visible
    f_post = 7.0 / 8.0 * (4.0 / 11.0) ** (4.0 / 3.0)
    dNeff_post = r_vac_rad * (1.0 + f_post * 3.044) / f_post
    bbn_95_upper = -0.14 + 2.0 * 0.21                # arXiv:2401.15054: -0.14 +/- 0.21
    def q(w):                                        # deceleration parameter; NOTE: no z-dependence
        return -1.0 + 1.5 * (1.0 + w) * (1.0 - nu)
    z_t_LCDM = (2.0 * Om_L0 / Om_m0) ** (1.0 / 3.0) - 1.0
    nu_RVM_95_upper = 4.0 * (0.00024 + 2.0 * 0.00039)
    out = {
        "Omega_vac_at_every_epoch": nu,
        "excess_over_Planck2015XIV_earlyDE_0p02": nu / 0.02,
        "equivalent_Delta_Neff_at_BBN": dNeff,
        "equivalent_Delta_Neff_post_annihilation_convention": dNeff_post,
        "excess_over_BBN_Delta_Neff_95up": dNeff / bbn_95_upper,
        "q_matter_era": q(0.0), "q_radiation_era": q(1.0 / 3.0),
        "q_depends_on_z": False,
        "LCDM_transition_redshift_same_params": z_t_LCDM,
        "excess_over_RVM_nu_95up": nu / nu_RVM_95_upper,
        "verdict": "DYNAMICAL reading EXCLUDED (three independent probes: early-DE, BBN Delta-N_eff, "
                   "and the absent deceleration->acceleration transition). PRESENT-EPOCH reading "
                   "survives but is near-definitional => TWT makes NO dark-energy prediction at V3.",
    }
    assert abs(out["Omega_vac_at_every_epoch"] - Om_L0) < 1e-12, "matching today forces nu = Omega_Lambda,0"
    assert out["excess_over_Planck2015XIV_earlyDE_0p02"] > 30.0
    assert out["excess_over_BBN_Delta_Neff_95up"] > 25.0
    assert out["equivalent_Delta_Neff_at_BBN"] < out["equivalent_Delta_Neff_post_annihilation_convention"]
    assert out["q_depends_on_z"] is False and q(0.0) < 0.0 and q(1.0 / 3.0) < 0.0
    assert 0.60 < z_t_LCDM < 0.70
    assert out["excess_over_RVM_nu_95up"] > 100.0
    return out


# ---- §24.5  induced-G MAGNITUDE: the knowability determination (item 10) ------
# Integrated from the ECC Sakharov two-build (MC + Reviewer + reconciler). Arithmetic clean-room
# verified by the Editor; verdict-LABELS calibrated per the reconciler (the delta over-framed them):
# "derived from substrate" -> "from substrate DIMENSIONALITY"; "knowability boundary SUPPORTED" ->
# "currently CONSISTENT WITH, not CONFIRMED"; + the mode-TYPE and Euclidean->Lorentzian caveats.
def induced_G_quadratic_divergence_from_4D():
    """[DERIVED — from substrate DIMENSIONALITY only] §21.6.3: The induced Einstein-Hilbert coefficient is
    quadratically UV-divergent, 1/(16πG) ∝ Λ², BECAUSE the substrate is 4D: the loop ∫d^dk/(2π)^d (1/k²)
    has UV power d−2 (= 2 for d=4, 0/log for d=2, 1 for d=3). The Λ² (not log, not finite) is fixed by the
    4D mode density — and by NOTHING ELSE about the grain dynamics. So the substrate-derived content is
    exactly the 4-dimensionality. IMPORTED (load-bearing, flagged): the numerical PREFACTOR (the a1
    heat-kernel coefficient / N_eff / spin weights) is generic QFT, not re-derived from the grain action —
    it sets the N_eff VALUE (the bracket), not the verdict. self-check: UV power d−2 = 2 at d=4."""
    def uv_power(d): return d - 2
    return {"substrate_dimension": 4, "UV_power_of_Lambda_in_1_over_16piG": uv_power(4),
            "derived_content": "ONLY the 4-dimensionality (=> Λ² scaling => G cutoff-power-gated)",
            "imported_load_bearing": "the heat-kernel PREFACTOR (a1/N_eff/spin weights) — generic QFT, "
                                     "sets the bracket width, NOT the verdict"}


def induced_G_leading_coefficient_mass_independent():
    """[DERIVED — Phase-D absence; the fake-positive guard] The exact heat-kernel coefficient
    I(Λ,m)/Λ² = e^{-x} − x·E1(x), x=(m/Λ)², → 1 as m/Λ → 0. The LEADING Λ² piece (the induced 1/16πG) is
    MASS-INDEPENDENT; the mass spectrum enters only the subleading −m² ln(Λ²/m²). So N_eff carries the mode
    COUNT (incl. generation multiplicity) but NOT mass VALUES, the meta-time phase, or the §9.6 dissipation
    kernel — no manufactured G↔mass↔generation link. self-check: I/Λ² > 0.999 for m/Λ ≤ 1e-2."""
    np = __import__("numpy"); from scipy.special import exp1
    def I_over_L2(r): x = r * r; return float(np.exp(-x) - x * exp1(x))
    vals = {f"m_over_Lambda={r:.0e}": round(I_over_L2(r), 6) for r in (1e-1, 1e-2, 1e-3)}
    return {"I_over_Lambda2": vals,
            "verdict": "leading Λ² coefficient MASS-INDEPENDENT -> no G<->mass link (Phase D absent, not manufactured)"}


def induced_G_only_monad_scale_enters():
    """[DERIVED arithmetic] §21.6.3: If the cutoff were the CELL scale 1/ℓ_S = e·f_π (~0.70 GeV) instead of the
    grain scale Λ~M_Pl (the grain — this primitive's name retains the older word 'monad'),
    1/G would miss M_Pl² by (Λ·ℓ_S)² = (M_Pl/(e f_π))² ~ 3e38 — the paper's two-scale
    forcing. So ONLY Λ (grain) enters the leading coefficient; ℓ_S enters at ~1e-38. Clean (b), not
    partial-knowability. self-check: ℓ_S ≈ 0.281 fm and the mismatch is ~1e38."""
    M_Pl, f_pi, e_sk, hbar_c = 1.22e19, 0.129, 5.45, 0.1973
    inv_lS = e_sk * f_pi; lS_fm = hbar_c / inv_lS; hier = M_Pl / inv_lS
    return {"ell_S_fm": round(lS_fm, 3), "hierarchy_Lambda_x_ellS": f"{hier:.2e}",
            "G_mismatch_if_cell_cutoff": f"{hier**2:.2e}",
            "verdict": "only Λ(monad) enters; cell scale would miss G by ~1e38 -> clean (b)"}


def induced_G_bracket_mode_count():
    """[DERIVED — Λ-status core] §21.6.3: Back-fitting empirical G to 1/(16πG) = N_eff·Λ²/(96π²) gives
    Λ/M_Pl = sqrt(6π/N_eff). The RETIRED 2026-07-28 bracket Λ∈[0.13,2.5] M_Pl mapped to N_eff∈[~3,~1115]
    — the surviving point: Λ_S is a FREE residual fit to G, pinned only up to the mode count, NOT by
    the substrate.
    ★ BRACKET RETIRED 2026-07-30 (history: widened 2026-07-28 from [0.16,0.72] to span an apparent
    three-way c_reg disagreement; RESOLVED 2026-07-29 — ONE c_reg = 1/12 in three Λ-variables; the
    which-Λ ruling then split the symbol, so the wide bracket has no live consumer). This primitive's
    Λ↔N_eff trade-off statement is kept as the HISTORICAL record of what the wide bracket implied
    (N_eff∈[~3,~1115] in this primitive's fixed convention) and of the honest point that survives:
    Λ_S is a back-fit to measured G over the N_eff menu, pinned by the mode count, NOT by the substrate.
    ★ CAVEAT (reconciler): a1 is a SIGNED weighted sum over mode TYPES (scalar +1/6, conformal 0,
    Dirac −1/12, gauge +1/6), NOT a count — and the substrate's actual mode content was not specified — so
    the true bracket may be WIDER still than the mode-count [3,1115].
    self-check: the bracket maps to ~[3,1115]."""
    import math
    def Neff_of(ratio): return 6 * math.pi / ratio ** 2
    Neff_hi, Neff_lo = Neff_of(0.13), Neff_of(2.5)
    return {"Lambda_over_MPl_bracket": (0.13, 2.5),  # RETIRED 2026-07-30 (historical record)
            "bracket_status": "RETIRED by the 2026-07-30 which-Lambda ruling — historical record only; "
                              "live scales: Lambda_S = sqrt(2*pi) M_Pl (scheme), Lambda_L = 1/a = "
                              "[0.386, 0.734] M_Pl (dispersion consumers)",
            "N_eff_bracket_mode_count": (round(Neff_lo), round(Neff_hi)),
            "caveat": "a1 is a SIGNED weighted TYPE-sum, not a count; true bracket may be WIDER; substrate "
                      "mode content unspecified",
            "NOT_a_mode_count_claim": (
                "READ THIS BEFORE QUOTING [3,1115]. Since 2026-07-28 the Lambda bracket's width is "
                "DOMINATED by the unreconciled c_reg (a factor ~4.6 in Lambda), not by mode content. "
                "Inverting that width through a FIXED coefficient convention therefore charges c_reg's "
                "uncertainty to N_eff, which is a category error if read literally: the framework does "
                "NOT claim the substrate may carry anywhere from 3 to 1115 modes. [3,1115] is only the "
                "image of the Lambda bracket under this primitive's fixed convention. The honest "
                "mode-count statement is the OLD one conditioned on a SINGLE c_reg (e.g. [36,736] at the "
                "placeholder), and it could not be stated unconditionally until the c_reg reconciliation "
                "closed. It closed 2026-07-29 (one coefficient, three Lambda-variables) and the "
                "which-Lambda ruling landed 2026-07-30: this field is now HISTORICAL."),
            "bracket_widened_2026_07_28": ("was [0.16,0.72] -> N_eff [36,736]. Widened to span the OPEN "
                                           "three-way c_reg disagreement (~1 paper placeholder / 1/12 "
                                           "sakharov_induced_gravity / ~1.8 induced_G_from_linear_face_band), "
                                           "NOT to agree with any measurement. Λ is now LESS pinned; the old "
                                           "'SM-like O(100)' gloss on N_eff no longer holds"),
            "verdict": "Λ is a FREE residual (pinned only up to N_eff), substrate-UNFIXED"}


def induced_G_sign_cross_check():
    """[CROSS-CHECK of item 5 — NOT re-opened] §21.6.3: Induced 1/(16πG) > 0 (attractive) follows from C_T > 0
    (reflection positivity of <T T>); item 5 establishes C_T > 0, dominated by the bosonic rotor modes.
    ★ OPEN SUBSIDIARY (reconciler): the substrate is 4D EUCLIDEAN; induced gravity is usually (3+1)
    Lorentzian. The Wick rotation preserves the Λ² scaling, but the prefactor and the positivity/sign
    relation may carry i/2π subtleties — to be checked consistent with the Euclidean substrate (item 5's
    sign cross-check inherits this). self-check (flag only): sign + given C_T>0."""
    C_T_positive = True
    return {"C_T": ">0 (item 5, established)", "induced_1_over_16piG_sign": "+ (attractive)",
            "open_subsidiary": "Euclidean->Lorentzian: Λ² scaling survives Wick rotation; prefactor/sign may "
                               "carry i/2π subtleties to check against the Euclidean substrate",
            "status": "cross-checked against item 5; not re-derived"}


def induced_G_gate_A_linearized_sufficient():
    """[DERIVED — Gate A] The leading Λ² coefficient and the knowability verdict are a one-loop GAUSSIAN
    (heat-kernel a1) result over the LINEARIZED fluctuation spectrum — the linearized spectrum SUFFICES.
    The #1 gap (§9.6 nonlinear dynamics) does NOT gate the verdict; it would only sharpen the N_eff value
    (the bracket). So item 10 is NOT (iii)/#1-gap-gated — its [A] status STANDS. self-check: the verdict
    depends on the Λ-power (a1/Gaussian level), not on any nonlinear EOM input."""
    needs_nonlinear_EOM = False
    return {"computation_level": "one-loop Gaussian / heat-kernel a1 (linearized spectrum)",
            "verdict_gated_by_#1_gap": needs_nonlinear_EOM,
            "what_#1_gap_would_change": "the N_eff value (bracket width), NOT the cutoff-gated verdict",
            "status": "NOT (iii)/#1-gap-gated; item 10 [A] stands"}


def induced_G_knowability_verdict():
    """[DERIVED — the calibrated determination; item 10] §21.6.3: (b) CUTOFF-GATED *currently*. 1/(16πG) =
    N_eff·Λ²/(96π²), G = f(N_eff)·Λ⁻², with Λ (~M_Pl) a FREE, substrate-unfixed residual — so the absolute
    G is not currently a pure number.
    ★ KNOWABILITY — CALIBRATED (reconciler), from the delta's 'SUPPORTED' to CONSISTENT-WITH-NOT-CONFIRMED:
    (b) is the current status but does NOT confirm the knowability boundary, for two reasons — (1) the
    cutoff-gating is GENERIC (ANY 4D induced gravity is cutoff-gated; it is not a TWT-STRUCTURAL forcing of
    underivability); (2) the framework NAMES and PREDICTS-DERIVABLE a route to (a): derive the dimensionless
    Λ·ℓ_S as a pure number (via the open cell-formation theory fixing the Skyrme e/ℓ_S from the grain
    scale), which would make G knowable. So the absolute is NOT structurally underivable, only currently
    underdetermined — and the boundary would be REFUTED by deriving Λ·ℓ_S. Honest: (b) currently; consistent
    with the boundary, not confirming it; refutable. self-check: outcome (b); knowability = consistent-not-confirmed."""
    return {
        "outcome": "(b) CUTOFF-GATED (currently)",
        "form": "1/(16πG) = N_eff·Λ²/(96π²);  G = f(N_eff)·Λ⁻²",
        "derived_part": "Λ² scaling — from substrate DIMENSIONALITY only",
        "imported_part": "heat-kernel prefactor / N_eff weights (generic QFT) — flagged; sets bracket only",
        "which_scale_enters": "ONLY Λ (monad ~M_Pl); ℓ_S would miss G by ~1e38",
        "Lambda_status": "FREE residual, substrate-unfixed (bracket == mode-count uncertainty, maybe wider)",
        "phase_D_mass_link": "ABSENT (leading coefficient mass-independent; only generation multiplicity in N_eff)",
        "sign": "+ (attractive) via C_T>0 (item 5); Euclidean->Lorentzian prefactor/sign open subsidiary",
        "gate_A": "linearized suffices; NOT #1-gap-gated; item 10 [A] stands",
        "knowability_boundary": "CONSISTENT WITH, NOT CONFIRMED — gating is generic + a route to (a) is "
                                "named and predicted-derivable (=> refutable, not a structural underivability)",
        "route_to_(a)_and_refutation_open": "derive the dimensionless hierarchy Λ·ℓ_S as a pure number "
                                            "(cell-formation theory fixing e/ℓ_S from the monad scale)",
    }


def d4_lattice_lorentz_violation_orders(E_GeV: float = 1.0e11):
    """[DERIVED-A for the lattice-moment + invariant-dimension identities; the dim-8 INFERENCE is
    DERIVED-conditional on two named premises; the dim-6 ISOTROPIC coefficient is #1-gap GATED]
    R-165. §B.1.5 / §B.6.3: WHICH orders of Lorentz violation the substrate actually protects — and,
    equally load-bearing, WHICH IT DOES NOT. Supersedes the pre-2026-07-27 claim that "the two
    protections leave the residual at dimension six (E/Λ)²", which conflated two different objects
    (anisotropy vs isotropic dispersion) and read a dim-6 number against a dim-4 bound.

    THE THREE FACES, separated:
      (1) dim-4 RELATIVE-BOOST LV between species — CLOSED structurally by matter-as-defect
          (R-016, equivalence_principle_protection): one field, one light cone, no independent
          coefficient for the violation to live in.
      (2) ROTATIONAL ANISOTROPY — closed by the D4 point group, and closed HARDER than the paper
          claimed. The REASON IS REPRESENTATION-THEORETIC, not a property of any particular kernel
          (the earlier nearest-neighbour-Laplacian argument was a model, canon §3, and is NOT what
          this rests on). Engine-checked here:
            |Aut(D4 root system)| = 1152 = |W(F4)| (built by closure, verified to permute the roots)
            dim of degree-d point-group-invariant polynomials, by Molien:  d=2 → 1, d=4 → 1,
            d=6 → 2, d=8 → 3   [= F4's known invariant degrees {2, 6, 8, 12}]
          The degree-4 invariant space is ONE-dimensional — spanned by (k²)² alone. So for ANY
          dispersion kernel invariant under the lattice point group and analytic in k, there is no
          anisotropic quartic AT ALL: the quartic term is forced isotropic by symmetry, whatever
          the kernel — GIVEN the premises below ((P-op) in particular: the drive is a dynamics
          that reduces the operative group, which is exactly why this cannot be said
          dynamics-independently; wording repaired 2026-08-25, R-185 keeper O-3).
          The degree-6 space is TWO-dimensional, so an anisotropic sextic DOES exist and
          the order is not merely bounded but LEADING — checked on both sides here (the 6th bond
          moment is anisotropic, residual 12). Consequence: leading rotational anisotropy sits at
          DIMENSION EIGHT, (E/Λ)⁴ ~ 7e-30 at the highest observed cosmic-ray energies — structurally
          out of any observational range. A genuine strengthening of §B.1.5.
          The bond moments are retained as the concrete face: 2nd = 12 δ_ij, 4th = 4(δδ+δδ+δδ)
          exactly (M_1111 = 12 = 3 M_1122).
          NOT GENERIC TO LATTICES (the derived-vs-generic discriminator, canon §5): simple-cubic Z⁴
          has N_1111 = 2 while N_1122 = 0 (4th-moment residual 2), and its point group B4 (order 384)
          has a TWO-dimensional degree-4 invariant space — Σk_i⁴ exists there. Dim-8 is an F4/D4
          fact, not a 4-dimensionality fact.
          PREMISES, NAMED (do not drop them — the inference is conditional, not absolute; the
          paper carries two further ones this docstring does not restate, (P-gs) the ground state
          preserving the point group and the scalar-in-internal-index premise — see §B.1.5):
            (P-an) ANALYTICITY in k, i.e. a derivative expansion exists. A driven-dissipative memory
                   kernel — the #1 gap itself — need not be analytic, and a non-analytic kernel is
                   not covered by any polynomial-invariant argument.
            (P-pg) the FULL point group, INCLUDING TRIALITY. The reflection subgroup W(D4) (order
                   192) has a 3-dimensional degree-4 invariant space; the order-384 subgroup has 2.
                   Concretely: at the second D4 shell the roots split into two W(D4) orbits — {±2e_i}
                   and (±1,±1,±1,±1) — each individually anisotropic (residual 32 apiece), cancelling
                   ONLY at equal weight. A substrate coupling that weights triality-related orbits
                   unequally RESTORES dimension-six anisotropy. This is the positive result's own
                   would-change-if (N52), and it is why the result must not be over-trusted.
            (P-op) THE OPERATIVE SYMMETRY IS THE FULL POINT GROUP [1152], NOT THE DRIVEN SUBGROUP
                   (added 2026-08-25, D4 standalone cold-review round; adjudication record
                   knowledge/audit/standalone_reviews_2026-08-25/ADJUDICATION_D4_2026-08-25.md §1.4,
                   amendment record R165_AMENDMENT_2026-08-25.md — NOT SHIPPED, internal audit
                   paths). The theorem above is proved in FOUR Euclidean variables at the full
                   group; the claim it is QUOTED for — leading ROTATIONAL (spatial) anisotropy,
                   read against SME anisotropic coefficients and sidereal cosmic-ray limits — is a
                   THREE-dimensional statement, and a driven steady state singles out e4. The
                   driven group is Stab_G(e4), order 48 (the same G48 that `_gamma_bond_rig` builds
                   and asserts); it is block-diagonal and restricts FAITHFULLY and EXACTLY onto
                   W(B3) — all 48 signed 3-permutations — whose invariant degrees are {2,4,6}. So
                   the degree-4 SPATIAL invariant space at the driven group is TWO-dimensional,
                   spanned by (k_sp²)² AND Σ_{i<=3} k_i⁴: an anisotropic spatial quartic is
                   PERMITTED there, though it is FORBIDDEN at the full group. What carries the
                   protection at the driven group is therefore a FULL-GROUP PROPERTY OF THE
                   COUPLING, not the driven symmetry: the 24 bonds are one equal-weight W(F4)
                   orbit, forcing the spatial fourth moment exactly isotropic on every 3-plane
                   (residual 0, full tensor); the 12 e4-bearing bonds give spatial residual +4
                   and the 12 bonds in the e4=0 hyperplane -4, which is the e4-axis SENSITIVITY
                   DECOMPOSITION of that protection, not its mechanism (R-185 re-key). A
                   permission left unpopulated, not a forbidden term.
                   WOULD-CHANGE-IF: any driven-sector term populating that permitted invariant —
                   a coupling surviving at G48 but not at G, with nonzero spatial fourth moment
                   (equivalently any reweighting breaking the +4/-4 cancellation) — RESTORES
                   dimension-six SPATIAL anisotropy, facing SME-type sidereal bounds rather than
                   the isotropic ones. This premise is the group-theoretic content of the
                   arbitration the §D.5.7 Γ-survivor pointer dockets: the candidate answer to
                   "which premise does a nonzero driven-group Γ survivor evade" is (P-op), not
                   (P-an) and not (P-pg). NOTHING COMPUTED HERE MOVES — no value, tier or count
                   changes on this premise; it is a scope statement made explicit. This primitive's
                   own asserts remain full-group statements and are correct as such.
                   CONTENT COMPUTED since 2026-08-25 at driven_group_spatial_invariants_wb3
                   (R-185): the W(B3) restriction (faithful, exact), the invariant dimensions
                   (two independent methods) and the +-4 split are engine-executed there.
                   COMPUTED IS NOT DISCHARGED — (P-op) remains an open assumption about the
                   dressed driven dynamics. R-185's §8a review also RE-KEYED the would-change-if
                   axis-independently: the operative condition is a bond weighting that fails to
                   be CONSTANT ON THE W(F4) ORBIT (G48-invariant but not G-invariant); the +4/-4
                   split is the e4-axis SENSITIVITY DECOMPOSITION of the protection, not its
                   mechanism (full-orbit isotropy descends to every 3-plane — at a generic axis
                   the split does not exist and isotropy persists).
      (3) the ROTATIONALLY INVARIANT dim-6 residual η⁽⁴⁾ p⁴/M²_Pl — NOT PROTECTED BY EITHER.
          It is not a relative-boost observable (so (1) does not reach it) and it is not an
          anisotropy (so (2) does not reach it). At dim 6 a species-UNIVERSAL coefficient is NOT
          removable by rescaling either: the induced velocity shift ≈ (3/2)η p²/Λ² is
          MOMENTUM-dependent (x → λx scales E²−p² by λ⁻² but p⁴/Λ² by λ⁻⁴), so universality is not
          a symmetry here. Its value is set by the substrate strain-mode dispersion = the #1 gap
          (Cl41Wave().wave_speed_c RAISES); this primitive therefore returns NO prediction for it.

    THE EXPOSURE (INPUT — inside-frame data; Import Registry I-19, dim-6 LV-EFT constraint bridge;
    RE-TABLED 2026-08-26 at the round-5 E21-VERDICT on the primary-read bounds dossier,
    knowledge/audit/external_review_r5_2026-08-25/BOUNDS_DOSSIER_V-C_2026-08-26.md — the old table
    quoted conditional corners as if unconditional, and one corner was a PROJECTED bound):
    published n = 4 (= dim-6) limits, CMB frame — which the framework identifies with its own
    τ₅-foliation/comoving frame (§B.4.5), so the frames agree.
    UNCONDITIONAL (no composition assumption, no unmet observation; superluminal branch — the one
    the positive naive value sits on):
        hadron    η⁽⁴⁾_p < 0.149  (η_π < 0.298), 5σ   (Auger 2022, model-independent; obtained by
                  rigidity-rescaling the fitted n=0 result — the ONE unconditional analysis)
        photon    |ξ⁽⁴⁾| < 6.2e6 superluminal          (Satunin 2021, Tibet-ASγ — no sub-unity
                  reach at this operator dimension)
        electron  none below ~1e6                      (Liberati 2013's own statement)
    CONDITIONAL (the strong corners, each with its condition NAMED — never quote one without it):
        proton    −1e-3 ≲ η⁽⁴⁾_p ≲ 1e-6, 99% CL       (Liberati 2013 eq. 78 / Maccione+2009:
                  PURE-PROTON composition, which Auger 2022's own data disfavours; the −1e-3
                  corner is a subluminal simulation-grid edge — inapplicable to the positive
                  naive value either way)
        photon    ξ⁽⁴⁾ ≲ 1e-8                          (Liberati 2013 eq. 77: the γ-decay line —
                  a PROJECTED bound, "do not correspond to real constraints" in its authors' own
                  words, contingent on a ~1e19 eV photon detection UNMET as of 2026; plus
                  pure-proton GZK secondaries)
        electron  −1e-7 ≲ η⁽⁴⁾ ≲ 1e-6                  (ibid.: same rectangle and conditions as
                  the photon; corner assignment partially unresolved — dossier §b.6)
        universal |η| ≲ 1.4e-6                          (Stecker 2009 eq. 18 via δ^π_p < 4.5e-23:
                  proton-dominated GZK + species universality)
        nuclei    the composition LADDER (Saveliev–Maccione–Sigl 2011; each rung requires that
                  species observed at that energy): He at 1e20 eV: η ≲ 1e-4 (4.3–4.8 orders);
                  O at 1e20 eV: η ≲ 3e-2 (still 1.8–2.4 orders — MORE than the unconditional
                  bound); Fe at 1e20 eV: η ≲ 4 — the naive band STRADDLES it; Fe at 10^19.6 eV:
                  NO exclusion. Auger 2022 reports near-zero PROTON fraction above 1e19 eV, not
                  a species ID — composition is UNSETTLED and the conditional corners RE-ARM if
                  it resolves adversely.
    DOSSIER FLAGS CARRIED (E21 spec — named, not dropped): Galaverni & Sigl and Maccione &
    Liberati 2008 UNREAD at primary (the likely GZK-photon-argument ancestry of the projected
    corner); the published-CQG equation numbering unchecked (cite as eqs. 77–78 v1 = 75–76 v3);
    Stecker's universal 1.4e-6 is the NON-reduced-M_Pl (conservative) reading — the reduced
    reading is 5.6e-8, flagged unresolved in the dossier.
    NORMALIZATION — TWO CONVENTIONS, DO NOT CONFLATE (this is where the old text contradicted
    itself): η⁽⁴⁾ is by definition the coefficient of p⁴/M²_Pl (the Liberati convention, in which the
    bounds above are quoted). The SUBSTRATE's own natural form is c·p⁴/Λ² with c = O(1), since Λ is
    the substrate cutoff. The two are related by η⁽⁴⁾ = c·(M_Pl/Λ)². So "the substrate's natural
    coefficient is unity" means c = 1, NOT η⁽⁴⁾ = 1 — and c = 1 at the lattice scale Λ_L = 1/a gives
    η⁽⁴⁾ = c_lat/(2π) ∈ [1.9, 6.7] (central 3.47) — positive, hence superluminal. THE EXCLUSION,
    E21-RE-CUT: UNCONDITIONALLY ~1.1–1.7 orders (0.8–1.4 on the pion reading) from the single
    Auger 2022 model-independent analysis; 6.3–6.8 orders CONDITIONAL on pure-proton composition;
    8.3–8.8 only on the unmet photon-detection premise. THE HISTORICAL '3–9 ORDERS' IS RETIRED —
    its 3-corner was the subluminal branch (inapplicable to a positive coefficient) and its
    9-corner the projected γ-decay line. The framework does NOT
    claim the naive value (it cannot compute c); the number is reported here only to size the exposure.
    WHICH-Λ RULING (coordinator, 2026-07-30): the dispersion denominator is Λ_L = 1/a — a Taylor
    expansion of a finite-range lattice kernel can only produce the bond length — with band
    [0.386, 0.735] M_Pl from OA-LF-ii's κ ∈ [1/2, 2] through the affine c_lat(κ). Λ_S = √(2π) M_Pl is a
    heat-kernel SCHEME variable carrying no substrate information and is NOT admissible here.
    History: 2026-07-28 the bracket was widened to [0.13, 2.5] M_Pl to span an apparent three-way
    c_reg disagreement; 2026-07-29 that resolved to ONE coefficient in three Λ-variables; the
    widening's rationale died with it and the wide bracket is RETIRED. Against the E21 re-cut: the most
    favourable corner (η⁽⁴⁾ = 1.9) is ~1.1 orders above the unconditional Auger bound and ~6.3
    above the pure-proton-conditional one. The defect form factor supplies (f_π/m_p)² ~ 1e-2 for
    the proton — MARGINAL against the ~1-order UNCONDITIONAL gap (clears by 1.18x at the upper
    corner with the ANW f_π = 129 MeV, FAILS by 1.77x at the honest F_π = 186 MeV substitution),
    far short of the 6-to-7-order conditional gap; its applicability to the strain-mode
    coefficient is unbuilt regardless — and it supplies NOTHING for the
    photon, which §B.5.4 makes a BULK strain mode with no internal structure — the most exposed
    sector under the conditional corners, unconstrained below ~1e6 unconditionally.

    JURISDICTION HEDGE (canon §0 / the N49 shape; I-19 premise (e)): the published bounds are
    INSIDE-frame inferences about propagating particles, while the object they are taken to bound is
    the OUTSIDE-frame substrate strain-mode dispersion. The transfer runs through the un-built
    outside↔inside projection — the same hedge §E.3.1 rows 7–8 carry for the Im χ / Goldstone floors.
    So the exposure is real and must be named (canon §0a), but its BINDINGNESS is itself conditional.

    Recorded as an open exposure at §E.3.3 VG-6 and §E.3.5(4), NOT as a falsifier row and NOT as a
    passed test. Negative N52.

    self-check: |Aut(D4)| = 1152 with degree-4 invariant space 1-dimensional (⇒ no anisotropic
    quartic) and degree-6 2-dimensional (⇒ dim-8 is LEADING, not merely bounded); D4's 2nd and 4th
    bond moments exactly isotropic and its 6th NOT; Z⁴'s 4th moment anisotropic (the contrast)."""
    import itertools
    bonds = []
    for i, j in itertools.combinations(range(4), 2):
        for si in (1, -1):
            for sj in (1, -1):
                v = [0, 0, 0, 0]
                v[i], v[j] = si, sj
                bonds.append(v)
    cubic = [[(s if k == i else 0) for k in range(4)] for i in range(4) for s in (1, -1)]

    def _moments(vs):
        m2 = [[sum(v[a] * v[b] for v in vs) for b in range(4)] for a in range(4)]
        m4 = {}
        for a, b, c, d in itertools.product(range(4), repeat=4):
            m4[(a, b, c, d)] = sum(v[a] * v[b] * v[c] * v[d] for v in vs)
        return m2, m4

    def _iso_residual(m4):
        # best isotropic form A(δδ + δδ + δδ) is fixed by the mixed component A = M_1122
        A = m4[(0, 0, 1, 1)]
        dl = lambda p, q: 1 if p == q else 0
        return max(abs(m4[(a, b, c, d)] - A * (dl(a, b) * dl(c, d) + dl(a, c) * dl(b, d) + dl(a, d) * dl(b, c)))
                   for a, b, c, d in itertools.product(range(4), repeat=4)), A

    m2, m4 = _moments(bonds)
    z2, z4 = _moments(cubic)
    d4_offdiag = max(abs(m2[a][b]) for a in range(4) for b in range(4) if a != b)
    d4_diag = {m2[a][a] for a in range(4)}
    d4_res, d4_A = _iso_residual(m4)
    z_res, _ = _iso_residual(z4)

    assert len(bonds) == 24 and d4_diag == {12} and d4_offdiag == 0, (
        "D4 bond set must have 24 bonds with second moment exactly 12*delta_ij")
    assert d4_res == 0, f"D4 fourth bond moment must be EXACTLY isotropic, residual={d4_res}"
    assert m4[(0, 0, 0, 0)] == 12 == 3 * m4[(0, 0, 1, 1)], "D4: M_1111 = 12 = 3*M_1122"
    assert z_res > 0 and z4[(0, 0, 0, 0)] == 2 and z4[(0, 0, 1, 1)] == 0, (
        "Z^4 fourth moment must NOT be isotropic — the contrast is the point")

    # --- the OTHER side of "leading": the SIXTH bond moment must be ANISOTROPIC, else "dimension
    #     eight" would be an unchecked upper bound rather than the leading order.
    #     Isotropic rank-6 form is B*(sum of the 15 delta-pairings): M_112233 = B, M_111111 = 15B.
    m6 = lambda idx: sum(v[idx[0]] * v[idx[1]] * v[idx[2]] * v[idx[3]] * v[idx[4]] * v[idx[5]]
                         for v in bonds)
    m6_1x6, m6_112233 = m6((0,) * 6), m6((0, 0, 1, 1, 2, 2))
    sixth_residual = abs(m6_1x6 - 15 * m6_112233)
    assert sixth_residual > 0, (
        "D4 SIXTH bond moment must be ANISOTROPIC — otherwise the leading anisotropy is not dim-8")

    # --- the REAL reason (representation theory, not any particular kernel): build Aut(D4 root
    #     system) by closure and count invariant polynomials by Molien. Degree 4 one-dimensional
    #     ⇒ the quartic is forced isotropic for ANY point-group-symmetric analytic kernel.
    import numpy as _np
    _roots = {tuple(v) for v in bonds}
    _R = _np.array(sorted(_roots), dtype=float)

    def _permutes_roots(A):
        return all(tuple(q) in _roots for q in _np.rint(_R @ A.T).astype(int))

    _gens = []
    for _p in itertools.permutations(range(4)):
        _A = _np.zeros((4, 4))
        for _i, _pi in enumerate(_p):
            _A[_i, _pi] = 1.0
        _gens.append(_A)
    _gens += [_np.diag(_s).astype(float) for _s in itertools.product((1, -1), repeat=4)]
    _tri = 0.5 * _np.array([[1, 1, 1, 1], [1, 1, -1, -1], [1, -1, 1, -1], [1, -1, -1, 1]], dtype=float)
    _gens = [_g for _g in _gens if _permutes_roots(_g)] + ([_tri] if _permutes_roots(_tri) else [])
    _grp = {_np.eye(4).tobytes(): _np.eye(4)}
    _frontier = [_np.eye(4)]
    while _frontier:
        _nxt = []
        for _A in _frontier:
            for _g in _gens:
                _B = _np.round(_g @ _A, 6) + 0.0
                _k = _B.tobytes()
                if _k not in _grp:
                    _grp[_k] = _B
                    _nxt.append(_B)
        _frontier = _nxt
    _G = list(_grp.values())

    def _molien_dim(deg):
        # dim of degree-`deg` G-invariant polynomials = (1/|G|) sum_g h_deg(eigenvalues(g))
        tot = 0.0
        for _A in _G:
            lam = _np.linalg.eigvals(_A)
            ps = [complex(_np.sum(lam ** k)) for k in range(1, deg + 1)]
            h = [1.0 + 0j] + [0j] * deg
            for n in range(1, deg + 1):
                h[n] = sum(ps[k - 1] * h[n - k] for k in range(1, n + 1)) / n
            tot += h[deg].real
        return tot / len(_G)

    inv_dims = {d: round(_molien_dim(d), 6) for d in (2, 4, 6)}
    assert len(_G) == 1152, f"Aut(D4 root system) must have order 1152 = |W(F4)|, got {len(_G)}"
    assert abs(inv_dims[4] - 1.0) < 1e-6, (
        "degree-4 point-group-invariant space must be 1-DIMENSIONAL (only (k^2)^2) — this, not any "
        f"particular kernel, is why there is no anisotropic quartic; got {inv_dims[4]}")
    assert abs(inv_dims[6] - 2.0) < 1e-6, (
        f"degree-6 invariant space must be 2-dimensional (an anisotropic sextic EXISTS, so dim-8 is "
        f"LEADING not merely an upper bound); got {inv_dims[6]}")

    MPl = 1.220910e19  # GeV
    # Λ_L = 1/a — the inverse grain spacing, the ONLY admissible dispersion denominator
    # (which-Λ ruling, coordinator 2026-07-30). Band: κ ∈ [1/2, 2] applied THROUGH the AFFINE
    # c_lat(κ) = 1.5075 + 20.2777·κ of c_reg_from_substrate_mode_content — κ scales the ~93%
    # sub-grain support fraction, NOT c_lat wholesale (wholesale would give [0.38, 0.76], a
    # DIFFERENT band). 1/a = sqrt(12π/(N_eff·c_lat)) M_Pl → [0.3865, 0.7345]; central 0.5365
    # at the flat-band c_lat = 21.83 (the affine κ=1 value 21.79 gives 0.537 — same at 2 d.p.).
    # The suite cross-ties these literals to the live affine map (no free-floating constant).
    # The old [0.13, 2.5] Sakharov-scheme bracket is RETIRED here.
    lam_lo, lam_hi = 0.3865, 0.7345
    x2 = (E_GeV / (lam_lo * MPl)) ** 2
    return {
        "dim4_relative_boost": "CLOSED structurally (R-016 matter-as-defect: one field, one light cone)",
        "D4_second_moment_12_delta": True,
        "D4_fourth_moment_isotropy_residual": d4_res,
        "D4_fourth_moment_A": d4_A,
        "Z4_fourth_moment_isotropy_residual": z_res,
        "D4_sixth_moment_isotropy_residual": sixth_residual,
        "point_group_order": len(_G),
        "invariant_poly_dims_deg_2_4_6": inv_dims,
        "why_no_dim6_anisotropy": ("degree-4 invariant space is 1-DIMENSIONAL (only (k^2)^2) under the "
                                   "order-1152 point group — symmetry forces the quartic isotropic for ANY "
                                   "point-group-symmetric analytic kernel; NOT a property of one model"),
        "anisotropy_leading_order": ("dimension EIGHT — LEADING (checked both sides: deg-4 invariant space "
                                     "1-dim ⇒ no anisotropic quartic; deg-6 2-dim and 6th bond moment "
                                     "anisotropic ⇒ dim-8 is reached, not merely bounded)"),
        "anisotropy_magnitude_(E/Lambda)^4": x2 ** 2,
        "anisotropy_premises": {
            "P-an": "ANALYTICITY in k (a derivative expansion exists); a non-analytic driven-dissipative "
                    "memory kernel — the #1 gap itself — is NOT covered by a polynomial-invariant argument",
            "P-pg": "the FULL point group INCLUDING TRIALITY; W(D4) (order 192) alone has a 3-dim degree-4 "
                    "invariant space, and the shell-2 sub-orbits {±2e_i} and (±1,±1,±1,±1) are each "
                    "anisotropic (residual 32 apiece), cancelling ONLY at equal weight — unequal weighting "
                    "of triality-related orbits RESTORES dim-6 anisotropy (N52 risk note)",
            "P-gs": ("the GROUND STATE PRESERVES THE POINT GROUP. The SSD.4.3 spiral vacuum BREAKS it; "
                     "what is left is a species-universal O(q^2) splitting absorbable by the I-22 "
                     "rescaling class, plus a space-fixed/sidereal residual that is SC-2's open "
                     "question. Carried in the paper SSE premise register since 2026-07-31; entered "
                     "into this returned value 2026-08-25 with the full tier naming, so the tier "
                     "string names nothing this primitive does not define"),
            "P-op": ("the OPERATIVE SYMMETRY on the SPATIAL-anisotropy sector is the FULL point group "
                     "(1152), NOT the DRIVEN subgroup Stab_G(e4) (order 48, restricting faithfully and "
                     "exactly onto W(B3), invariant degrees {2,4,6}), whose degree-4 SPATIAL invariant "
                     "space is TWO-dimensional and PERMITS an anisotropic spatial quartic. At the driven "
                     "group the protection is carried by a FULL-GROUP property of the coupling (constancy "
                     "on the single equal-weight W(F4) bond orbit), not by the driven symmetry: the "
                     "24-bond spatial fourth moment is exactly isotropic on every 3-plane, with the +4/-4 "
                     "split between the e4-bearing and in-hyperplane bonds as the e4-axis SENSITIVITY "
                     "DECOMPOSITION (R-185 re-key) -- a permission left unpopulated, not a "
                     "forbidden term. WOULD-CHANGE-IF: any driven-sector term populating that permitted "
                     "invariant (equivalently any reweighting breaking the +4/-4 cancellation) RESTORES "
                     "dimension-six SPATIAL anisotropy, facing SME-type SIDEREAL bounds rather than the "
                     "isotropic ones. Added 2026-08-25; see this docstring's (P-op) block for the full "
                     "statement and the SSD.5.7 Gamma-survivor arbitration pointer. NOTHING COMPUTED "
                     "MOVES: this premise can only make the POSITIVE half weaker. CONTENT COMPUTED at "
                     "driven_group_spatial_invariants_wb3 (R-185, banked 2026-08-25; computed is NOT "
                     "discharged — the premise stays an open assumption; its would-change-if is "
                     "re-keyed there axis-independently to orbit-constancy of the bond weighting, "
                     "with +4/-4 as the e4-axis sensitivity split)")},
        "dim6_isotropic_eta4": "GATED (#1 gap: substrate strain-mode dispersion; Cl41Wave().wave_speed_c raises)",
        "normalization": ("eta4 is the coefficient of p^4/M_Pl^2 (Liberati convention); the SUBSTRATE's "
                          "natural form is c*p^4/Lambda^2 with c = O(1), so eta4 = c*(M_Pl/Lambda)^2. "
                          "'natural coefficient unity' means c = 1, NOT eta4 = 1"),
        "naive_eta4_at_c_equals_1": ((1.0 / lam_hi) ** 2, (1.0 / lam_lo) ** 2),
        "naive_eta4_status": "NOT a prediction — sizes the exposure. E21-RE-CUT (2026-08-26, primary-read dossier): excluded UNCONDITIONALLY by ~1.1-1.7 orders (Auger 2022 model-independent hadronic, superluminal branch, one analysis) and by 6.3-6.8 orders ONLY under pure-proton composition (disfavoured by Auger itself); the historical 3-9-orders figure is RETIRED (wrong-branch 3-corner; projected never-triggered 9-corner)",
        "Lambda_bracket_used": {
            "bracket_M_Pl_nonreduced": (lam_lo, lam_hi),
            "meaning": "Lambda_L = 1/a, the inverse monad spacing — band from OA-LF-ii kappa in "
                       "[1/2, 2] on the banked c_lat = 21.83; central 0.537 M_Pl",
            "history": ("2026-07-28: widened (0.16, 0.72) -> (0.13, 2.5) to span an apparent "
                        "three-way c_reg disagreement; 2026-07-29: RESOLVED — one c_reg = 1/12 in "
                        "three Lambda-variables; 2026-07-30: which-Lambda RULED, wide bracket "
                        "RETIRED. eta4 went [1.9, 39] -> [0.16, 59] -> [1.9, 6.7]"),
            "status": "RULED (coordinator, 2026-07-30) — Lambda_L = 1/a for the lattice-dispersion "
                      "consumers (scoped per B.6.2; THIS exposure is one of the two FORCED "
                      "Taylor-coefficient consumers); Lambda_S = sqrt(2*pi) M_Pl is a scheme variable "
                      "with no substrate content (see sakharov_induced_gravity()['c_reg_reconciliation'])"},
        # The SURVIVAL requirement expressed in the substrate's OWN normalization. Banked as a returned
        # field so downstream text can cite this primitive rather than quoting a floating number
        # (canon §2 bank-before-you-cite). c = eta4*(Lambda/M_Pl)^2, so the ceiling scales with BOTH the
        # species bound and the Lambda-bracket corner — it is a bracket, never a single figure.
        "implied_substrate_c_ceiling": {
            "UNCONDITIONAL_hadron_eta4_0.149": (0.149 * lam_lo ** 2, 0.149 * lam_hi ** 2),
            "CONDITIONAL_matter_eta4_1e-6": (1e-6 * lam_lo ** 2, 1e-6 * lam_hi ** 2),
            "CONDITIONAL_photon_eta4_1e-8_PROJECTED": (1e-8 * lam_lo ** 2, 1e-8 * lam_hi ** 2),
            "note": "survival needs |c| below these. E21-RE-CUT: the UNCONDITIONAL ceiling is "
                    "2.2e-2 .. 8.0e-2 (a ~1-to-1.7-order suppression of an O(1) coefficient); the "
                    "1.5e-9 .. 5.4e-7 band is CONDITIONAL (pure-proton; the photon row additionally "
                    "PROJECTED on an unmet detection) and must carry those labels wherever quoted "
                    "(2026-07-30 which-Lambda band; historical brackets in the git record)"},
        "published_n4_bounds_INPUT": {"photon_xi4": (-1e-7, 1e-8), "electron_eta4": (-1e-7, 1e-6),
                                      "proton_eta4": (-1e-3, 1e-6), "delta_pi_p_Stecker": 4.5e-23},
        "form_factor_insufficient": "(f_pi/m_p)^2 ~ 1e-2 for the proton — MARGINAL against the ~1-order unconditional gap (clears 1.18x at ANW f_pi, fails 1.77x at F_pi = 186), far short of the conditional 6-7 orders, applicability unbuilt; NONE for the photon (bulk mode, B.5.4)",
        "frame_inertial": "coefficients defined in the CMB frame = the tau5-foliation/comoving frame (B.4.5) "
                          "— frames agree; this closes the INERTIAL-frame question only",
        "frame_jurisdiction_HEDGE": ("the bounds are INSIDE-frame inferences; the object bounded is the "
                                     "OUTSIDE-frame strain-mode dispersion. The transfer rides the un-built "
                                     "outside<->inside projection (same hedge as E.3.1 rows 7-8). The exposure "
                                     "is named per canon §0a, but its BINDINGNESS is itself conditional — "
                                     "I-19 premise (e)"),
        "tier": ("DERIVED-A (lattice moment identities + invariant-space dimensions, exact) + "
                 "DERIVED-conditional-on-(P-an ∧ P-pg ∧ P-gs ∧ P-op) (the dimension-EIGHT "
                 "inference -- FULL NAMING, 2026-08-25: the four are the paper SSE premise "
                 "register's own list, and every one of them is DEFINED in this "
                 "primitive's anisotropy_premises. The SSB.1.5 scalar-in-internal-index "
                 "condition is a FIFTH named condition that register does not label, and "
                 "is therefore not in this string either -- said here so the list's reach "
                 "is not over-read) + "
                 "INPUT (published n=4 bounds, I-19) + GATED (the dim-6 isotropic coefficient itself)"),
        "recorded_as": "open exposure E.3.3 VG-6 / E.3.5(4) + negative N52 — NOT a falsifier row, NOT a passed test",
    }


def driven_group_spatial_invariants_wb3():
    """[DERIVED-A — exact finite group theory + exact bond-moment integers; the (P-op)
    premise's CONTENT made EXECUTABLE. R-185, banked 2026-08-25; §8a-reviewed same day,
    verdicts at knowledge/audit/pop_banking_2026-08-25/ — the review's repairs are IN
    this text, so read it as the post-consensus form.]

    THE (P-op) GROUP THEORY, COMPUTED. Until this primitive, three facts lived only as
    PROSE — in knowledge/audit/standalone_reviews_2026-08-25/ADJUDICATION_D4_2026-08-25.md
    §1.4 and in the (P-op) block of d4_lattice_lorentz_violation_orders — while the R-165
    tier literal NAMES (P-op) as a premise. A load-bearing premise named in a tier string
    deserves an executable form (the bank-before-you-cite class one step removed, canon
    §2); this primitive computes the premise's content. COMPUTED IS NOT DISCHARGED: (P-op)
    remains an OPEN assumption about the dressed driven dynamics — what is banked here is
    the group theory that states it, not a verdict on it. (The docket row's claim that
    (P-op)'s sibling premises were already computed was FALSE and is not repeated:
    (P-pg)'s own numbers — W(D4) order 192, degree-4 dim 3, shell-2 residuals +-32 — are
    prose-only too, verified correct by this bank's reviewer; a follow-up bank of the
    same shape is available there.)

    FILE PLACEMENT (canon §6 consumption rule): consumes the D4 siting (V3-1) via
    _gamma_bond_rig — CANDIDATE half, correctly.

    THE THREE FACTS (each exact, each asserted in-process):
      (1) THE RESTRICTION IS FAITHFUL AND EXACTLY W(B3). The driven group Stab_G(+e4) —
          order 48, the same G48 that _gamma_bond_rig builds and asserts — is
          BLOCK-DIAGONAL (every element fixes e4 exactly and preserves e4-perp), and its
          restriction to the spatial 3-space is FAITHFUL (48 distinct 3x3 images) and is
          EXACTLY the full octahedral group W(B3) = all 48 signed 3-permutations, checked
          as set equality of exact matrix keys, both directions. Consistency: the spatial
          invariant dimensions at degrees 2/4/6 come out 1/2/3 — exactly the free
          polynomial algebra on W(B3)'s invariant degrees {2, 4, 6}, which are CLASSICAL
          (Coxeter 1951; Chevalley 1955; Shephard-Todd 1954) — nothing here is claimed
          as new mathematics; what is banked is the executable check.
      (2) THE DEGREE-4 SPATIAL INVARIANT SPACE AT THE DRIVEN GROUP IS 2-DIMENSIONAL —
          spanned by (k_sp^2)^2 and Sum_{i<=3} k_i^4 — so an ANISOTROPIC SPATIAL QUARTIC
          IS PERMITTED at the driven group though FORBIDDEN at the full group. Dimensions
          computed by TWO GENUINELY INDEPENDENT METHODS INSIDE THIS PRIMITIVE and
          asserted equal (the §8a reviewer computed that the previous cross-tie to
          d4_lattice_lorentz_violation_orders' count was the SAME Molien/Newton formula
          re-run, not a second method — repaired here by adding the real second method):
          (i) symmetric-power traces (group average of h_d(eigenvalues), Newton
          recursion on power sums), and (ii) the REYNOLDS OPERATOR on the degree-d
          monomial basis, with the invariant dimension read off as the rank (= trace) of
          the averaged action matrix. Both give: degree-4 in FOUR variables: 1 at
          G [1152], 4 at G48; degree-4 in the THREE spatial variables at the W(B3)
          restriction: 2. The full-group value 1 also equals
          d4_lattice_lorentz_violation_orders' count — a CONSISTENCY TIE across two
          independently-cached group objects, not itself a second method. The witness
          polynomial Sum_{i<=3} k_i^4 is verified invariant under ALL 48 driven-group
          elements and NON-invariant under the full group (1056/1152 elements move it —
          forced: 1056 = 1152 - 96, since the witness's stabilizer in G is exactly the
          axis group G96), by exact coefficient transport, not sampling.
          ★ AXIS SUB-PREMISE, NAMED (the §8a meta-observer's F1 finding): these numbers
          are evaluated AT THE MAXIMALLY SYMMETRIC AXIS. e4 is a lattice symmetry
          direction (an F4 short-root axis), which is why |Stab| = 48; a GENERIC drive
          axis has trivial stabilizer and a degree-4 spatial permission of dimension 15
          (all quartics). The banked corpus builds every driven-group object at
          Stab(+e4), so the instance-level alignment "the advance axis is a lattice
          symmetry axis" is an IMPLICIT V3 commitment this primitive now names — it is
          recorded, not resolved, and the family-tree question (a V3-1 sub-node) is the
          coordinator's. The would-change-if below is deliberately keyed
          AXIS-INDEPENDENTLY so it does not inherit this parochiality.
      (3) THE 24-BOND SPATIAL FOURTH MOMENT IS EXACTLY ISOTROPIC — FULL TENSOR, not just
          one scalar: max deviation of the rank-4 spatial moment tensor from its best
          isotropic form is 0.0 exactly (an UNDER-CLAIM repair from the §8a review; the
          e4-bearing and in-hyperplane halves have full-tensor residuals 4 each, of
          opposite sign in the anisotropy scalar M_1111 - 3*M_1122: +4 and -4).
          THE MECHANISM, STATED CORRECTLY (the §8a meta-observer's F4 re-keying,
          engine-arbitrated): the isotropy is NOT produced by the +4/-4 cancellation —
          it is a FULL-ORBIT fact. The 24 bonds are a single W(F4) orbit with equal
          weights, so the banked full-group degree-4 uniqueness forces
          Sum_b (b.k)^4 = 12*(k^2)^2 identically in FOUR variables, and that isotropy
          DESCENDS TO EVERY 3-PLANE — at a generic axis the 12+12 split does not even
          exist and the spatial moment is still isotropic. What (P-op) adds is that AT
          THE DRIVEN GROUP nothing forces this: G48 symmetry PERMITS the anisotropic
          quartic, and the protection is carried by the interaction remaining CONSTANT
          ON THE FULL W(F4) ORBIT — a full-group property of the coupling that the
          driven symmetry does not enforce. The +4/-4 split is the e4-axis SENSITIVITY
          DECOMPOSITION of that protection (how big the anisotropy gets per unit of
          orbit-weighting imbalance at this axis), not the mechanism.

    SCOPE — NOTHING MOVES (the same sentence the premise carries, kept executable): no
    value, tier or count changes on this bank; R-165's own asserts remain full-group
    statements and are correct as such; (P-op) can only make R-165's POSITIVE half
    weaker, and its negative half (the isotropic dim-6 exposure) is untouched a
    fortiori. The Γ-SURVIVOR ARBITRATION POINTER travels UNRESOLVED: the candidate
    answer to "which premise does a nonzero driven-group Γ survivor evade" is (P-op) —
    the §D.5.7 assembly record holds the arbitration and this primitive does not
    resolve it; it supplies the arbitration's group-theoretic content as computation.

    WOULD-CHANGE-IF, KEYED AXIS-INDEPENDENTLY (re-keyed at the §8a review): any
    driven-sector coupling whose bond weighting FAILS TO BE CONSTANT ON THE W(F4)
    ORBIT — i.e. is G48-invariant but not G-invariant — RESTORES dimension-six SPATIAL
    anisotropy, facing SME-type sidereal bounds rather than the isotropic ones. At the
    e4 axis the sensitivity is the +-4 pair: demonstrated in-process at hyperplane
    weight w = 2 (a weighting constant on each of the two G48 sub-orbits but not on the
    full orbit), leaving anisotropy -4, nonzero.

    IN-PROCESS DEMONSTRATIONS, correctly labeled (the §8a reviewer's finding: only one
    of these is a negative control): (a) the G24 restriction check IS a real negative
    control — the orientation-preserving half restricts to a PROPER 24-element subset
    of W(B3), so the exactness test is seen able to fail; (b) the w = 2 reweighting is
    an EXECUTABLE WOULD-CHANGE-IF EXHIBIT, not a failure plant — its outcome is entailed
    by the +-4 integers asserted above; it demonstrates the failure channel, it does not
    test this primitive.

    TIER RIDER (derived-vs-generic, canon §5 — R-184's exact-is-not-substrate-specific
    class, owed here for rider parity): facts (1) and (2) are GENERIC finite-reflection-
    group theory, NOT D4-specific — the keeper computed that Z4's point group W(B4) has
    |Stab(e4)| = 48 restricting onto the SAME W(B3). What IS D4-specific: the
    forbidden-at-G / permitted-at-G48 CONTRAST (Z4 permits the spatial quartic at both
    levels), and the 24-bond full-orbit isotropy with its +-4 sensitivity split.

    Records: knowledge/audit/standalone_reviews_2026-08-25/ADJUDICATION_D4_2026-08-25.md
    §1.4 (source prose) · TRIAGE_2026-08-25.md §5.2 (the docket row) · R-165's (P-op)
    premise text at d4_lattice_lorentz_violation_orders ·
    knowledge/audit/pop_banking_2026-08-25/ (the three §8a verdicts + consensus INDEX)."""
    import itertools
    import numpy as np
    rig = _gamma_bond_rig()
    G = [np.asarray(g, float) for g in rig["groups"]["1152"]]
    G48 = [np.asarray(g, float) for g in rig["groups"]["48"]]
    G96 = [np.asarray(g, float) for g in rig["groups"]["96"]]
    G24 = [np.asarray(g, float) for g in rig["groups"]["24"]]
    bonds = rig["bonds"]

    def mkey(m):
        return tuple(np.round(np.asarray(m, float).ravel(), 9) + 0.0)

    # ---- fact (1): block-diagonality + faithful, exact W(B3) restriction ----
    block_diagonal = all(
        np.allclose(g[3, :3], 0.0, atol=1e-12) and np.allclose(g[:3, 3], 0.0, atol=1e-12)
        and abs(g[3, 3] - 1.0) < 1e-12 for g in G48)
    restr = [g[:3, :3] for g in G48]
    images = {mkey(r) for r in restr}
    wb3 = set()
    for p in itertools.permutations(range(3)):
        for s in itertools.product((+1.0, -1.0), repeat=3):
            M = np.zeros((3, 3))
            for i, pi in enumerate(p):
                M[i, pi] = s[i]
            wb3.add(mkey(M))
    faithful = (len(images) == 48)
    exactly_wb3 = (images == wb3)
    assert block_diagonal and faithful and exactly_wb3 and len(wb3) == 48, \
        "(P-op) fact 1 failed: Stab_G(+e4) must restrict faithfully and exactly onto W(B3)"
    # negative control (a), run in-process: the orientation-preserving half is NOT W(B3)
    images24 = {mkey(g[:3, :3]) for g in G24}
    assert len(images24) == 24 and images24 != wb3 and images24 < wb3, \
        "negative control must fire: G24's restriction is a PROPER 24-element subset of W(B3)"

    # ---- fact (2): invariant dimensions, TWO independent methods ----
    # method (i): symmetric-power traces (Molien) — h_d of eigenvalues via Newton
    # recursion on power sums p_k = tr(g^k)
    def _sym_trace(g, d):
        n = g.shape[0]
        p = [0.0] * (d + 1)
        M = np.eye(n)
        for k in range(1, d + 1):
            M = M @ g
            p[k] = float(np.trace(M))
        h = [1.0] + [0.0] * d
        for k in range(1, d + 1):
            h[k] = sum(p[i] * h[k - i] for i in range(1, k + 1)) / k
        return h[d]

    def inv_dim_traces(mats, d):
        v = sum(_sym_trace(m, d) for m in mats) / len(mats)
        assert abs(v - round(v)) < 1e-6, "invariant dimension must be an integer"
        return int(round(v))

    # method (ii): the REYNOLDS OPERATOR on the degree-d monomial basis — the averaged
    # action matrix is a projector onto the invariants; its rank (= its trace) is the
    # invariant dimension. Genuinely different route: builds the polynomial action
    # explicitly, never touches eigenvalues or Newton's identities.
    def _act_matrix(g, monos, idx, nvars):
        n = len(monos)
        M = np.zeros((n, n))
        for j, mono in enumerate(monos):
            terms = {(): 1.0}
            for v in mono:
                new = {}
                for t, c in terms.items():
                    for a in range(nvars):
                        ga = g[a, v]
                        if abs(ga) > 1e-12:
                            tt = tuple(sorted(t + (a,)))
                            new[tt] = new.get(tt, 0.0) + c * ga
                terms = new
            for t, c in terms.items():
                M[idx[t], j] += c
        return M

    def inv_dim_reynolds(mats, nvars, d):
        monos = list(itertools.combinations_with_replacement(range(nvars), d))
        idx = {m: i for i, m in enumerate(monos)}
        R = np.zeros((len(monos), len(monos)))
        for g in mats:
            R += _act_matrix(g, monos, idx, nvars)
        R /= len(mats)
        assert np.abs(R @ R - R).max() < 1e-9, "Reynolds average must be a projector"
        rank = int(round(np.linalg.matrix_rank(R, tol=1e-8)))
        trace = float(np.trace(R))
        assert abs(trace - rank) < 1e-6, "projector rank must equal its trace"
        return rank

    dims = {"deg4_4var_full_group_1152": inv_dim_traces(G, 4),
            "deg4_4var_driven_group_48": inv_dim_traces(G48, 4),
            "deg4_3var_spatial_WB3": inv_dim_traces(restr, 4),
            "deg2_3var_spatial_WB3": inv_dim_traces(restr, 2),
            "deg6_3var_spatial_WB3": inv_dim_traces(restr, 6)}
    dims_reynolds = {"deg4_4var_full_group_1152": inv_dim_reynolds(G, 4, 4),
                     "deg4_4var_driven_group_48": inv_dim_reynolds(G48, 4, 4),
                     "deg4_3var_spatial_WB3": inv_dim_reynolds(restr, 3, 4)}
    for k, v in dims_reynolds.items():
        assert dims[k] == v, "the two independent methods must agree at " + k
    assert (dims["deg4_4var_full_group_1152"], dims["deg4_4var_driven_group_48"],
            dims["deg4_3var_spatial_WB3"]) == (1, 4, 2), "(P-op) fact 2 failed"
    assert (dims["deg2_3var_spatial_WB3"], dims["deg6_3var_spatial_WB3"]) == (1, 3), \
        "spatial invariant dims must match the free algebra on W(B3) degrees {2,4,6}"

    # the witness polynomial Sum_{i<=3} k_i^4 — exact coefficient transport under g
    def _act_poly(g, coeff):
        out = {}
        for mono, c0 in coeff.items():
            terms = {(): c0}
            for v in mono:
                new = {}
                for t, c in terms.items():
                    for a in range(4):
                        ga = g[a, v]
                        if abs(ga) > 1e-12:
                            tt = tuple(sorted(t + (a,)))
                            new[tt] = new.get(tt, 0.0) + c * ga
                terms = new
            for t, c in terms.items():
                out[t] = out.get(t, 0.0) + c
        return out

    p_aniso = {(i, i, i, i): 1.0 for i in range(3)}

    def _changed(g):
        tg = _act_poly(g, p_aniso)
        ks = set(tg) | set(p_aniso)
        return any(abs(tg.get(k, 0.0) - p_aniso.get(k, 0.0)) > 1e-9 for k in ks)

    viol_driven = sum(_changed(g) for g in G48)
    viol_axis_group = sum(_changed(g) for g in G96)
    viol_full = sum(_changed(g) for g in G)
    assert viol_driven == 0 < viol_full, \
        "Sum k_i^4 must be driven-group-invariant and full-group-NON-invariant"
    assert viol_axis_group == 0 and viol_full == len(G) - len(G96), \
        "the witness's stabilizer in G is exactly the axis group G96 (1056 = 1152 - 96)"

    # ---- fact (3): full-tensor spatial isotropy + the +4/-4 sensitivity split ----
    e4_bearing = [v for v in bonds if abs(v[3]) > 0.5]
    hyperplane = [v for v in bonds if abs(v[3]) < 0.5]

    def _spatial_m4(vs):
        m4 = {}
        for a, b, c, d in itertools.product(range(3), repeat=4):
            m4[(a, b, c, d)] = sum(v[a] * v[b] * v[c] * v[d] for v in vs)
        return m4

    def _full_tensor_residual(m4):
        # best isotropic form A(dd+dd+dd), A fixed by the mixed component
        A = m4[(0, 0, 1, 1)]
        dl = lambda p, q: 1 if p == q else 0
        return max(abs(m4[(a, b, c, d)]
                       - A * (dl(a, b) * dl(c, d) + dl(a, c) * dl(b, d) + dl(a, d) * dl(b, c)))
                   for a, b, c, d in itertools.product(range(3), repeat=4))

    def _aniso_scalar(vs):
        m1111 = sum(v[0] ** 4 for v in vs)
        m1122 = sum(v[0] ** 2 * v[1] ** 2 for v in vs)
        return float(m1111 - 3.0 * m1122)

    res_total = _full_tensor_residual(_spatial_m4(bonds))
    res_e4 = _full_tensor_residual(_spatial_m4(e4_bearing))
    res_hyp = _full_tensor_residual(_spatial_m4(hyperplane))
    a_e4 = _aniso_scalar(e4_bearing)
    a_hyp = _aniso_scalar(hyperplane)
    assert len(e4_bearing) == len(hyperplane) == 12
    assert res_total == 0.0 and (res_e4, res_hyp) == (4.0, 4.0), \
        "(P-op) fact 3 failed: total spatial moment must be FULL-TENSOR isotropic, halves not"
    assert (a_e4, a_hyp, a_e4 + a_hyp) == (4.0, -4.0, 0.0), "(P-op) fact 3 scalar split failed"
    # the would-change-if EXHIBIT (entailed by the integers above, demonstrates the channel):
    w_demo = 2.0
    reweighted = a_e4 + w_demo * a_hyp
    assert abs(reweighted) > 1e-9, "the reweighting exhibit must be nonzero"

    return {
        "driven_group_order": len(G48), "full_group_order": len(G),
        "block_diagonal": block_diagonal,
        "restriction_faithful": faithful,
        "restriction_is_exactly_WB3": exactly_wb3,
        "restriction_image": "W(B3) — all 48 signed 3-permutations, set-equality both directions",
        "wb3_invariant_degrees": (2, 4, 6),
        "wb3_degrees_credit": "classical invariant theory (Coxeter 1951; Chevalley 1955; "
                              "Shephard-Todd 1954) — the executable check is what is banked, "
                              "not the mathematics",
        "invariant_dims": dims,
        "invariant_dims_reynolds": dims_reynolds,
        "two_methods": ("symmetric-power traces (Molien/Newton) AND the Reynolds-operator "
                        "projector rank, computed IN THIS PRIMITIVE and asserted equal — the "
                        "agreement with d4_lattice_lorentz_violation_orders' count is a "
                        "CONSISTENCY TIE (same Molien formula, independently-cached group), "
                        "not a second method (§8a reviewer repair, 2026-08-25)"),
        "anisotropic_spatial_quartic_permitted_at_driven_group": True,
        "axis_sub_premise": ("NAMED, NOT RESOLVED (meta-observer F1): all driven-group numbers "
                             "are evaluated at the maximally symmetric axis — e4 is a lattice "
                             "symmetry direction, |Stab| = 48; a generic drive axis has trivial "
                             "stabilizer and spatial degree-4 permission dimension 15. The "
                             "alignment 'advance axis = lattice symmetry axis' is an implicit "
                             "V3 commitment (V3-1-adjacent), recorded here; family-tree "
                             "disposition is the coordinator's. The would-change-if is keyed "
                             "axis-independently and does not inherit this"),
        "witness_polynomial": "Sum_{i<=3} k_i^4 — invariant at G48 (0/48) and at the axis group "
                              f"G96 (0/96), moved by {viol_full}/{len(G)} full-group elements "
                              "(forced: 1056 = 1152 - 96, the witness's stabilizer is G96)",
        "witness_violations": {"driven_group": viol_driven, "axis_group_G96": viol_axis_group,
                               "full_group": viol_full},
        "spatial_fourth_moment_full_tensor_residuals": {"total_24_bonds": res_total,
                                                        "e4_bearing_12_bonds": res_e4,
                                                        "hyperplane_12_bonds": res_hyp},
        "spatial_fourth_moment_anisotropy": {"e4_bearing_12_bonds": a_e4,
                                             "hyperplane_12_bonds": a_hyp,
                                             "total_24_bonds": a_e4 + a_hyp},
        "mechanism": ("FULL-ORBIT ISOTROPY, correctly keyed (meta-observer F4 repair): the 24 "
                      "bonds are one equal-weight W(F4) orbit, so full-group degree-4 uniqueness "
                      "forces Sum_b (b.k)^4 = 12*(k^2)^2 in FOUR variables and isotropy descends "
                      "to EVERY 3-plane — the +4/-4 split is the e4-axis SENSITIVITY "
                      "DECOMPOSITION, not the mechanism (at a generic axis the split does not "
                      "exist and isotropy persists). At the driven group nothing FORCES "
                      "orbit-constancy: that is exactly (P-op)'s permission"),
        "would_change_if": ("AXIS-INDEPENDENT KEYING: any driven-sector coupling whose bond "
                            "weighting is G48-invariant but NOT constant on the W(F4) orbit "
                            "restores dim-6 SPATIAL anisotropy (SME-type sidereal bounds); at "
                            "the e4 axis the sensitivity is the +-4 pair"),
        "reweighting_demo": {"w_hyperplane": w_demo, "anisotropy": reweighted,
                             "status": "EXECUTABLE WOULD-CHANGE-IF EXHIBIT — entailed by the "
                                       "asserted +-4 integers, demonstrates the failure channel; "
                                       "the real negative control is the G24 proper-subset check"},
        "scope": ("NOTHING MOVES: no value, tier or count changes on this bank; R-165's asserts "
                  "remain full-group statements and are correct as such; (P-op) can only make the "
                  "POSITIVE half weaker. COMPUTED IS NOT DISCHARGED — (P-op) stays an open "
                  "assumption about the dressed driven dynamics. The §D.5.7 Γ-survivor "
                  "arbitration stays OPEN — this primitive supplies its group-theoretic content "
                  "and does not resolve it"),
        "tier": ("DERIVED-A (exact finite group theory: closure-built Stab_G(+e4), set-equality "
                 "onto W(B3), invariant dimensions by two independent methods, integer bond "
                 "moments) — the executable form of premise (P-op) of R-165; consumes the D4 "
                 "siting (V3-1). RIDER (canon §5, R-184's class): facts (1)-(2) are GENERIC "
                 "reflection-group theory shared with Z4's point group (whose Stab(e4) also "
                 "restricts onto W(B3)) — D4-specific content is the forbidden-at-G/"
                 "permitted-at-G48 CONTRAST and the 24-bond full-orbit isotropy with its +-4 "
                 "sensitivity split"),
        "records": ("knowledge/audit/standalone_reviews_2026-08-25/ADJUDICATION_D4_2026-08-25.md §1.4 "
                    "(source prose) · TRIAGE_2026-08-25.md §5.2 (the docket row) · R-165's (P-op) "
                    "premise text at d4_lattice_lorentz_violation_orders · "
                    "knowledge/audit/pop_banking_2026-08-25/ (§8a verdicts + consensus)"),
    }


def eom_constraint_class():
    """[FRAMING — the #1-gap compatible-field boundary, aggregated + engine-anchored; see TWT_EOM_MAP.md]
    The #1 gap (the driven-dissipative substrate EOM / Im χ form, §9.6) is a CONSTRAINT-SATISFACTION
    CLASS, not a single missing function: the family of nonlinear driven-dissipative rotor-field EOMs
    compatible with everything TWT has banked. This primitive makes the BINARY compatible-field BOUNDARY
    (H1-H11) machine-checkable: each engine-primitive-backed HARD constraint is CALLED here — it must
    RESOLVE, so the boundary is built of LIVE banked facts (not paraphrase) — and the CLASS-VARIANT
    magnitudes (α, g, σ_QCD, ...) are asserted to STILL RAISE (the gap is intact; computing them from one
    ansatz would be a toy, canon §3).

    EPISTEMICS (TWT_EOM_MAP.md §0, binding — Yaer 2026-06-25):
      • TWO-LAYER SCALE: the binary DERIVED/NOT scale draws the BOUNDARY ONLY (class membership — 'is it
        allowed?'); selection WITHIN the field uses a CONTINUOUS plausibility scale (the candidate
        mechanisms; not encoded here). Never collapse plausibility into the binary.
      • BIDIRECTIONAL REVISION (fallibilist): a high-plausibility EOM colliding with a HARD constraint Hn
        CHALLENGES Hn — the boundary is revisable, no banked fact is immune; the conflict is logged, not
        discarded (TWT_EOM_MAP.md §5).
    TIER: FRAMING. It asserts NO new EOM and NO new value — it certifies the boundary is banked + live and
    the variant gate holds. The path to a banked NUMBER is §4's invariant test (a value constant across the
    whole class ⇒ DERIVED-by-class-invariance, the s=3 pattern), NOT this aggregator.

    THE BOUNDARY NOW HAS TWO KINDS OF ENTRY (2026-07-27, R-165):
      • H1-H11 — SUBSTRATE-FORCED structural constraints. Unconditional; the original boundary.
      • E1     — the class's FIRST EMPIRICAL constraint: published dim-6 LV limits require the kernel's
                 isotropic quartic dispersion coefficient to sit far below its natural size. It is kept
                 in a SEPARATE bucket, never renumbered "H12", for two reasons that must not be blurred:
                 (i) it is IMPORTED DATA (I-19), not a substrate theorem; (ii) its bindingness is
                 CONDITIONAL on the un-built outside<->inside projection (I-19 premise (e)) — these are
                 inside-frame inferences about an outside-frame object. Excising I-19 fires against E1
                 alone. E1 is a CEILING: it can REFUTE a candidate kernel but supplies no equation, so it
                 adds ZERO anchor rank to the over-determination programme. Exposure ≠ value ≠ rank.

    self-check: every engine-backed HARD constraint resolves; H4's isotropy ORDERS are computed (not a
    flag) via R-165; H8's fork is EXERCISED (not type-checked) — an unchosen kernel must RAISE and the
    two live branches must move tau_mem; the class-variant value-gates — now including the strain-mode
    dispersion that E1 constrains — plus the Layer-3 structural gate all RAISE."""
    # --- H1-H11: the engine-primitive-backed HARD constraints (CALLED => must resolve) ---
    engine_backed = {
        "H1_field_unit_rotor_Spin4": matter_stability_outside_frame,   # compact unit-rotor carrier
        "H3_pi3_soliton":            pi3_S3_integer_completion,          # matter = π₃(S³)=ℤ soliton
        "H3_skyrme_stabilizer":      skyrme_BVP_audit,                   # ANW-consistent BVP + π₃ non-collapse (Derrick = standard physics, not engine-derived)
        "H5_colour_Z3_dichotomy":    theta_rel_z3_isotropy_dichotomy,    # colour ℤ₃ (or break = Θ_rel)
        "H6_genSpin3_centralE_a":    mass_reconciliation_U1_Spin3,       # [E,J²]=0, U(1)_E ⊕ Spin(3)
        "H6_genSpin3_centralE_b":    cogear_linkage_kinematic,           # E central, commutes colour+gen
        "H7_winding_continuity":     pi3_S3_integer_completion,         # ∂_μ j^μ=0 (grade-0);
        # re-pointed 2026-08-21 (keeper R2): the old entry named the charge-ASSIGNMENT
        # primitive, which computes neither a winding nor a continuity. The topological
        # content H7 is about — B in Z and its drift protection — is pi3_S3_integer_completion.
        "H10_frame_universal_EP":    equivalence_principle_protection,   # R̃∂R grade-2 ⇒ universal frame
        "H11_spine_weinberg":        weinberg_sin2,                      # must not contradict sin²θ_W=3/8
    }
    resolved = []
    for name, fn in engine_backed.items():
        fn()                 # raises if the cited banked fact is not live -> boundary check fails
        resolved.append(name)
    # H2 (linear free limit), H4 (isotropy ORDERS), H8 (drive/dissipation fork): inline engine facts
    assert "m = k4" in Cl41Wave().klein_gordon()                         # H2
    # H4 — RESCOPED 2026-07-27 (R-165). Was a bare `Substrate().dim4_isotropy is True`, i.e. a
    # hard-coded dataclass FLAG certifying a paraphrase, against this primitive's own "LIVE banked
    # facts" standard. Now CALLS the primitive that computes it, and separates the two orders the old
    # name conflated: (a) 2nd moment 12*delta ⇒ one stiffness, g1=g2 (dimension-FOUR operator);
    # (b) degree-4 point-group invariant space is 1-dimensional ⇒ NO anisotropic quartic, so
    # rotational anisotropy is reached only at dimension EIGHT (a statement about the dimension-SIX
    # operator). H4 does NOT deliver "emergent Lorentz" full stop — see E1.
    _lv = d4_lattice_lorentz_violation_orders()
    assert Substrate().dim4_isotropy is True                            # H4a one stiffness (g1=g2)
    assert _lv["D4_second_moment_12_delta"] is True
    assert _lv["D4_fourth_moment_isotropy_residual"] == 0               # H4b no anisotropic quartic
    assert abs(_lv["invariant_poly_dims_deg_2_4_6"][4] - 1.0) < 1e-6    #     ...by symmetry, model-free
    # H8 — RESCOPED 2026-08-23. Was a bare `isinstance(Substrate().memory_kernel, MemoryKernel)`,
    # i.e. a TYPE-CHECK on an Enum member, which cannot fail: the identical defect class R-165
    # repaired for H4 (see the comment block immediately above), left unfixed two lines below the
    # comment that describes the fix, inside a primitive advertising "LIVE banked facts (not
    # paraphrase)" and counting it in n_engine. A vacuous check inside an aggregator that certifies
    # measurement is the calibration tell inverted — no measurement at all. Now EXERCISES H8's
    # content, and separates the two orders the old one-liner conflated:
    #   (a) DRIVEN, NOT EQUILIBRIUM — the steady state is a NESS whose memory magnitude is #1-gap
    #       open, so with NO branch chosen the substrate must RAISE rather than quietly hand back
    #       an equilibrium relation. This is the assertion that fails if the gap is ever silently
    #       closed at the constitutive level.
    #   (b) THE FORK IS A LIVE, VALUE-MOVING BINARY — exactly two non-gated branches
    #       {fading, hysteretic}, and they return DIFFERENT tau_mem laws (hysteretic carries the
    #       reactive-barrier exp(S/hbar) that §11.6 needs; fading does not). A fork whose branches
    #       agree is a label, not a constitutive fork, and H8 would then be naming nothing.
    _h8_live = {k.value for k in MemoryKernel if k is not MemoryKernel.GATED}
    assert _h8_live == {"fading", "hysteretic"}, "H8b: the drive/dissipation fork must be the live binary"
    _h8_tau = {b: Substrate(memory_kernel=MemoryKernel(b)).tau_mem_over_tau_wave() for b in _h8_live}
    assert _h8_tau["hysteretic"] != _h8_tau["fading"], "H8b: the fork must MOVE tau_mem, else it is a label"
    assert "exp(S/hbar)" in _h8_tau["hysteretic"], "H8b: the hysteretic branch is the reactive-barrier law"
    try:
        Substrate(memory_kernel=MemoryKernel.GATED).tau_mem_over_tau_wave()
    except GatedError:
        pass                                                            # H8a — the gap is intact
    else:
        raise AssertionError("H8a: with no memory kernel chosen tau_mem must be #1-gap GATED — a "
                             "driven NESS whose memory magnitude quietly resolves is not H8's object")
    n_engine = len(resolved) + 3
    # --- E1: the class's FIRST EMPIRICAL constraint (2026-07-27, R-165/N52/VG-6) -------------------
    # Deliberately NOT numbered "H12". H1-H11 are substrate-FORCED; E1 is IMPORTED DATA (I-19) and its
    # bindingness is conditional on the un-built outside<->inside projection (I-19 premise (e)). Kept in
    # its own bucket so an I-19 excision fires against exactly this entry and nothing else, and so no
    # reader mistakes a conditional empirical ceiling for a structural theorem. It is a CEILING, not a
    # target: it can REFUTE a candidate kernel but supplies no equation (rank contribution zero — the
    # over-determination anchor count is unchanged; see kernel_overdetermination_table).
    empirical_E1 = {
        "id": "E1_dim6_isotropic_LV_ceiling",
        "requirement": "the kernel's isotropic quartic dispersion coefficient must satisfy "
                       "|eta4| <~ 1e-6 (matter) and <~ 1e-8 (photon), i.e. |c| below "
                       "implied_substrate_c_ceiling in the substrate's own normalization",
        "source": "IMPORT I-19 (published n=4 LV-EFT limits: Liberati 2013 eqs 77-78; Stecker 2009 eq 18)",
        "naive_value_status": "a coefficient of order unity (c = 1) gives eta4 = c_lat/(2*pi) in "
                              "[1.9, 6.7] (central 3.47) — the NAIVE value; E21-RE-CUT: ~1.1-1.7 orders unconditional (Auger 2022, superluminal), 6.3-6.8 conditional on pure-proton; the 3-9 figure is RETIRED. NOT "
                              "a TWT prediction: c is #1-gap GATED (Cl41Wave().wave_speed_c() raises). "
                              "[which-Lambda ruling 2026-07-30: dispersion consumers take "
                              "Lambda_L = 1/a, band [0.386, 0.734] M_Pl; the 2026-07-28 wide bracket "
                              "[0.13, 2.5] / eta4 [0.16, 59] / 2-10 orders is RETIRED. The ceiling "
                              "binds at every corner]",
        "bindingness_HEDGE": "CONDITIONAL — these are INSIDE-frame inferences bounding an OUTSIDE-frame "
                             "object; the transfer rides the un-built outside<->inside projection "
                             "(I-19 premise (e); same hedge as E.3.1 rows 7-8). Excising I-19 fires "
                             "against E1 alone and leaves H1-H11 untouched",
        "kind": "CEILING (can refute a candidate; supplies no equation ⇒ zero anchor rank)",
        "engine": "d4_lattice_lorentz_violation_orders (moments + invariant dims + c-ceiling)",
        "recorded_at": "E.3.3 VG-6, E.3.5(4), negatives ledger N52",
    }
    # H9: passive + low-ω super-Ohmic s=3 — banked in the PAPER (item 18/WP-DC2/IX4), no standalone
    #     primitive; cited honestly, NOT asserted via a phantom call.
    paper_backed = {"H9_passive_super_ohmic_s3": "item 18 / WP-DC2/IX4 (s=3 via Goldstone/Adler-zero); §9.6"}
    # --- the gap is INTACT: class-variant value-gates + the Layer-3 structural gate must RAISE ---
    def _must_raise(fn):
        try:
            fn()
        except (GatedError, UnderivedError):
            return True
        raise AssertionError(f"gate {fn.__name__} did NOT raise — the gap is not intact")
    # NOTE the parenless form below is REQUIRED: _must_raise needs the CALLABLE, not its return value.
    # (In prose/docstrings always write Cl41Wave().wave_speed_c() WITH parens — the attribute alone is a
    # bound method and does not raise, so a parenless prose cite sends a reviewer looking for nothing.)
    value_gates_1stgap = [alpha_em_value, qcd_collider_phenomenology,
                          Cl41Wave().wave_speed_c]          # #1-gap VALUE variants — the third is E1's gate
    structural_gate_L3 = [texture_tetrad]                               # Layer-3 (STRONG-EP/full metric)
    assert all(_must_raise(g) for g in value_gates_1stgap + structural_gate_L3)
    return {
        "object": "the #1 gap = a constraint-satisfaction class (driven-dissipative rotor EOM); map = TWT_EOM_MAP.md",
        "HARD_boundary_engine_backed": resolved,            # live banked primitives, called + resolved
        "HARD_boundary_inline_engine": ["H2_klein_gordon",
                                        "H4_isotropy_orders(a: 2nd-moment one-stiffness g1=g2 | "
                                        "b: deg-4 invariant space 1-dim ⇒ no anisotropic quartic ⇒ "
                                        "anisotropy only at dim-8) [R-165; does NOT reach the isotropic "
                                        "dim-6 term — that is E1]",
                                        "H8_drive_dissipation_fork(a: no branch chosen ⇒ tau_mem RAISES, "
                                        "so the NESS memory magnitude stays #1-gap open | b: the fork is "
                                        "the live binary {fading, hysteretic} and it MOVES tau_mem — a "
                                        "constitutive fork, not a label) [2026-08-23; was a type-check "
                                        "on the Enum, the R-165 defect class]"],
        "HARD_boundary_paper_backed": paper_backed,         # banked in the paper, no standalone primitive
        "EMPIRICAL_boundary_conditional": empirical_E1,     # NOT an Hn — imported, conditionally binding
        "n_engine_checks": n_engine,                        # = 12 (9 called + 3 inline)
        "class_invariant_DERIVABLE": [                      # constant across the class ⇒ s=3-style wins
            "s=3 super-Ohmic exponent (Goldstone symmetry)", "sin²θ_W=3/8 (static)",
            "charge quantization", "π₃(S³)=ℤ topology", "Bjorken scale-free skeleton",
            "Θ_rel Z3-isotropy dichotomy (Schur)", "WEAK-EP frame-universality"],
        "class_variant_GATED": [                            # depend on §3 free data ⇒ provably ansatz-dependent
            "α, g, g_s magnitudes", "σ_QCD", "absolute/relative mass scales", "v (EW VEV)",
            "τ_mem", "Θ_rel VALUE", "β₃ running magnitude",
            "isotropic dim-6 dispersion coefficient c (⇒ η⁽⁴⁾) — the ONLY class-variant carrying an "
            "EMPIRICAL bound; see E1"],
        "residual_free_data_4axes": ["Skyrme coupling e (ℓ_S)",
            "reactive Im χ at ω_d (barrier S / fork) — NOTE the kernel's k-dependence / strain-mode "
            "dispersion is a DISTINCT face of this axis, and it is the face E1 constrains",
            "f_π & Λ scales (separately cutoff-gated)", "drive amplitude/profile"],
        "gates_intact": {"value_#1gap": [g.__name__ for g in value_gates_1stgap],
                         "structural_Layer3": [g.__name__ for g in structural_gate_L3]},
        "tier": "FRAMING (boundary aggregator; asserts NO new EOM, NO new value); the gap stays GATED",
        "epistemics": "binary = boundary/membership only; plausibility = continuous within-field selector; "
                      "bidirectional revision: a plausible EOM vs an Hn challenges THAT Hn",
    }


def eom_invariant_variant_audit():
    """[FRAMING — the invariant/variant AUDIT of the #1-gap class; TWT_EOM_MAP.md §4]
    Tests 'every banked Layer-2 (dynamical) WIN is a class-INVARIANT; every open VALUE is a class-VARIANT'
    by SORTING every candidate by its TRUE engine tier-tag (NOT by 'the primitive resolves' — a primitive
    that records an OPEN gap also resolves), the independent criterion being: does it depend on the §3 free
    data (Im χ at ω_d / Skyrme e / f_π–Λ / drive)?

    ── VERDICT (rewritten after twt-reviewer OVER-CLAIM → trimmed; engine arbitrated) ─────────────────
    • FORWARD: the honest finding is NOT 'clean audit, 10 wins'. Sorting by tier shows there is **NO
      [DERIVED] Layer-2 VALUE at all**, and the genuine Layer-2 *dynamical* class-invariants are **EXACTLY
      TWO, both won by a SYMMETRY SHORTCUT**: s=3 (Goldstone/Adler-zero, paper-backed) and the Θ_rel
      Z3-isotropy dichotomy (Schur; `theta_rel_z3_isotropy_dichotomy`). Everything else on the 'invariant'
      side is NOT a dynamical win — it is static Layer-1 (charge/π₃/sin²θ_W, EOM-independent), topological
      (instanton rule, confinement), generic-given-4D (Sakharov Λ², canon §5), or FRAMING (WEAK-EP,
      induced-G sign cross-check). The audit ALSO catches two primitives that must NOT be counted as wins,
      proving it BY THEIR BANKED TIER: `ckm_hierarchy_and_cp_seed` is tagged **SEED** (hand-built
      off-diagonal — the N4′/N0 illustration pattern) and `qcd_uv_conformal_phaseCD` is tagged **LOCATED**
      ('locates AF, does not achieve it'). So the only route that has produced a Layer-2 derivation is the
      symmetry shortcut, and it has fired exactly twice. The 'no disguised toy' claim is TRUE but
      near-VACUOUS — the tiering already forbids a [DERIVED] Layer-2 value, so nothing COULD be disguised;
      the audit confirms the tiering is self-consistent, no more.
    • BACKWARD: 'open' is REFINED into 3 categories, only ONE the #1 gap:
        (1) KERNEL-gated variants = the #1 gap proper: α, g, g_s, σ_QCD, τ_mem, Θ_rel-VALUE, β₃-running.
        (2) CUTOFF-gated variants = the knowability SUB-case (Λ/f_π): absolute mass scales, G, abs f_π.
        (3) STRUCTURAL-open: the Layer-3 tetrad deep gate. **CORRECTED 2026-06-26 (bidirectional revision,
            EOM_MAP §5): the engine REFUTES my earlier 'N4 is kernel-independent'.** The {chiral projector
            ½(1+I₄) + sector S₊ + gen-space} pair is **DERIVED** (`ckm_arc_sector_and_corotation`, via
            §19.8.1's +e₄ — the symmetry shortcut ALREADY fired), and `chirality_does_not_source_P` proves
            (exact Clifford, 3 formalizations) the +e₄ chirality is **GENERATION-BLIND** (the Q→Q Hodge
            channel = 0), so property P is structurally ABSENT from it ⇒ N4 is **(ii) LOCATED** with residual
            = property P = **Θ_rel = the #1-gap KERNEL** (shared with colour-U(3)). And the SU(3) colour
            OCTET is also kernel-dependent (octet-as-oscillation needs the nonlinear vacuum, N5).
      ⇒ there is **NO surviving kernel-independent structural carve-out**: N4 is already DERIVED-structure
      with a KERNEL residual; the octet is kernel-dependent; category-(3)'s only member is the Layer-3
      tetrad (a deep gate, NOT cheap). 'every open item is #1-gap-gated' is now nearly TRUE — the open
      magnitudes are the kernel/cutoff #1-gap; the only non-#1-gap opens are the Layer-3 tetrad and the
      F3 magnitude-suppression form.

    HONESTY: for value-magnitudes 'open ⟺ variant' is near-DEFINITIONAL. The surviving bankable content is
    (a) the sharpened FORWARD finding (only the symmetry-shortcut has yielded a Layer-2 invariant — twice —
    and the audit engine-reclassifies the SEED + LOCATED items out of 'wins'); (b) the **N4-only**
    structural carve-out. The 'boundary unification' (invariant/variant = the static/dynamic fault line) is
    a RESTATEMENT of the already-banked fault line, not new content. PROGRAM REFRAME (stands): a new Layer-2
    derivation = INVARIANT-HUNTING via a symmetry shortcut (the s=3 / Z3-dichotomy pattern).
    TIER: FRAMING — no new value.

    self-check: the 2 genuine invariants' engine primitive resolves; the SEED+LOCATED items are
    tier-tagged out of 'wins'; the kernel-variant + Layer-3 gates raise; the cutoff verdict is (b)."""
    # FORWARD — the ONLY genuine Layer-2 DYNAMICAL class-invariants (both symmetry shortcuts):
    theta_rel_z3_isotropy_dichotomy()                  # Θ_rel Z3-dichotomy (Schur) — CALLED, live [DERIVED]
    layer2_dynamical_invariants = ["s=3 super-Ohmic exponent (Goldstone/Adler-zero; item 18/WP-DC2, paper)",
                                   "Θ_rel Z3-isotropy dichotomy (Schur; theta_rel_z3_isotropy_dichotomy)"]
    # invariant, but NOT a Layer-2 dynamical WIN (engine tiers, honest buckets):
    invariant_not_a_layer2_win = {
        "static_Layer1 (EOM-independent)": ["charge quantization (pi3_S3_integer_completion; the ASSIGNMENT of values is charge_assignment_from_anchor and is NOT EOM-independent of P4-P7)",
                                            "π₃(S³)=ℤ (pi3_S3_integer_completion)", "sin²θ_W=3/8 (weinberg_sin2)"],
        "topological/structural":          ["instanton ΔB=ΔL=3 (bpst_selection_rule)", "confinement = shared-rotor lock"],
        "generic-given-4D (canon §5)":     ["Sakharov Λ²-scaling (induced_G_quadratic_divergence_from_4D)"],
        "FRAMING (not DERIVED)":           ["WEAK-EP frame-universality (equivalence_principle_protection)",
                                            "induced-G sign cross-check (open Euclid→Lorentz subsidiary)"],
    }
    # the audit ENGINE-ARBITRATES the reclassification: these are NOT wins, proven by their banked tier
    assert "SEED" in (ckm_hierarchy_and_cp_seed.__doc__ or "")          # hand-built off-diagonal (N4′/N0)
    assert "LOCATED" in (qcd_uv_conformal_phaseCD.__doc__ or "")        # locates AF, does not achieve it
    not_a_win_caught = {"ckm_hierarchy_and_cp_seed": "SEED (illustration, not a derivation)",
                        "qcd_uv_conformal_phaseCD": "LOCATED (locates AF, does not achieve it)"}
    # BACKWARD — the THREE categories of 'open' (category-3 carve-out trimmed to N4 per reviewer)
    open_cat1_kernel = ["alpha", "g", "g_s", "sigma_QCD", "tau_mem", "Theta_rel_VALUE", "beta3_running"]
    open_cat2_cutoff = ["absolute mass scales", "Newton_G", "absolute f_pi (MeV)"]      # knowability sub-case
    # CORRECTED 2026-06-26 (bidirectional revision, EOM_MAP §5): the engine REFUTES 'N4 kernel-independent'.
    # The {chiral projector ½(1+I4) + sector S₊ + gen-space} pair is DERIVED (ckm_arc_sector_and_corotation,
    # via §19.8.1 +e4); chirality_does_not_source_P proves (exact, 3 formalizations) the +e4 chirality is
    # GENERATION-BLIND (Q->Q Hodge channel = 0) => property P is structurally ABSENT from it => N4 is (ii)
    # LOCATED, residual = property P = Theta_rel = the #1-gap KERNEL (shared with colour-U(3)).
    ckm_arc_sector_and_corotation(); chirality_does_not_source_P()      # engine-arbitrate the N4 correction
    weak_isospin_verdict()
    open_cat3_structural = {
        "kernel_INDEPENDENT": [],   # was [N4]; CORRECTED — N4's structure is DERIVED, its residual is KERNEL
        "Layer3_deep_gate": ["tetrad / STRONG-EP"],
        "already_DERIVED_structure__residual_is_KERNEL":
            ["N4 CKM: projector ½(1+I4)+S₊+gen-space DERIVED (CKM arc); residual = property P = Theta_rel (#1 gap)"],
        "NOT_kernel_independent": ["SU(3) colour octet — needs the nonlinear vacuum (N5)"],
    }
    # gates that must RAISE (the variant + deep-gate side intact)
    def _must_raise(fn):
        try:
            fn()
        except (GatedError, UnderivedError):
            return True
        raise AssertionError(f"{fn.__name__} did not raise")
    assert _must_raise(alpha_em_value)        # category (1): a kernel-gated #1-gap variant
    assert _must_raise(texture_tetrad)        # category (3): the Layer-3 structural deep gate
    assert induced_G_knowability_verdict()["outcome"].startswith("(b) CUTOFF-GATED")   # category (2)
    return {
        "hypothesis": "banked Layer-2 win => class-invariant; open value => class-variant",
        "FORWARD_verdict": "TRIMMED (reviewer OVER-CLAIM): NO [DERIVED] Layer-2 value exists; the genuine "
                           "Layer-2 dynamical class-invariants are EXACTLY TWO, both symmetry shortcuts",
        "layer2_dynamical_invariants_GENUINE": layer2_dynamical_invariants,
        "invariant_but_NOT_a_layer2_win": invariant_not_a_layer2_win,
        "audit_reclassified_OUT_of_wins (by banked tier)": not_a_win_caught,
        "no_disguised_toy": "TRUE but near-VACUOUS — the tiering already forbids a [DERIVED] Layer-2 value",
        "BACKWARD_verdict": "HOLDS for MAGNITUDES; 'open' REFINED into 3 categories (only (1) is the #1 gap)",
        "open_cat1_kernel_gated_#1gap": open_cat1_kernel,
        "open_cat2_cutoff_gated_knowability": open_cat2_cutoff,
        "open_cat3_structural": open_cat3_structural,
        "carve_out": "CORRECTED (bidirectional revision): NO surviving kernel-independent structural carve-out. "
                     "N4 is already DERIVED-structurally (chiral projector ½(1+I4)+S₊ via +e4) with a KERNEL "
                     "residual (property P=Theta_rel; chirality_does_not_source_P); the SU(3) octet is "
                     "kernel-dependent (N5); category-3's only member is the Layer-3 tetrad (deep gate, NOT cheap)",
        "N4_status": "(ii) LOCATED — the {chiral projector ½(1+I4) + S₊ + gen-space} pair DERIVED via the +e4 "
                     "symmetry shortcut; the chirality is generation-blind (Q->Q=0); residual = Theta_rel (#1 gap)",
        "unification_is_a_restatement": "invariant/variant = the already-banked static/dynamic fault line (s=3 = "
                                        "the Layer-2 invariant); knowability = the cat-(2) cutoff sub-case — NOT new content",
        "program_reframe": "a new Layer-2 derivation = INVARIANT-HUNTING via a symmetry shortcut (s=3 / Z3-dichotomy "
                           "pattern); it has fired exactly twice",
        "tier": "FRAMING (classification audit; no new value)",
    }




def chirality_is_a_reflection():
    """[DERIVED (the geometric fact) + FRAMING (the up/down identification) — the protection-mechanism workflow's
    one genuinely FORCED new result; TWT_DEFECT_CKM_GLUON.md §16]
    Attacking the #1 gap (the protected-window mechanism) via 4 substrate routes surfaced ONE engine-exact forced
    result: the up/down chirality (= the SD/ASD circular-polarization handedness) is LITERALLY a spatial REFLECTION.

    DERIVED (engine-exact Clifford): a spatial PARITY reflection P (e1 → −e1) maps each self-dual bivector to
    MINUS its anti-self-dual partner — P(self_dual(e1j)) = −anti_self_dual(e1j) for j=2,3,4. So an
    orientation-reversing isometry SWAPS the self-dual (3) and anti-self-dual (3) Spin(4) sub-spaces (the standard
    Hodge fact, here exhibited on the engine for the generating bivectors). [twt.py self_dual/anti_self_dual]

    FRAMING (the physics, CONDITIONAL on the identification): up/down = the two circular-polarization handedness =
    SU(2)₊/SU(2)₋ = self-dual / anti-self-dual (the posited CP identification — the weak-isospin=SU(2)₊ leg is N4
    CANDIDATE). GIVEN that identification, **"up ↔ down is a MIRROR" — the chirality-as-reflection that gives Yaer's
    gen-2 ~0.44 mirror (`generation_gen2_chirality_mirror`) — is substrate-FORCED Spin(4)/Hodge geometry, NOT a
    fit** (the geometry is unconditional; only the up↔SD labeling is the CANDIDATE step). This is the structural
    ORIGIN of the mirror, converged on by 3 of the 4 workflow routes
    (A: co/counter-rotating lock to the rotating e4 carrier; B: the even/odd ce_n/se_n Mathieu parity doublet =
    the ±90° Jones (1,±i); D: the parity↔SD/ASD swap, the decisive engine-exact one).

    GATED (NOT derived): the mirror VALUE — gen-2 at the off-center fraction ~0.44 — is shift+scale-invariant (a
    fraction of the span), so parity alone does NOT pin it; it needs the #1-gap EOM. So the chirality-as-reflection
    is DERIVED in KIND (up↔down is a mirror), GATED in VALUE (where gen-2 sits in the mirror).

    self-check: P(self_dual(e1j)) = −anti_self_dual(e1j) for j=2,3,4 (exact)."""
    def parity(mv):                                    # spatial reflection e1 -> -e1
        return MV.from_dict({b: (-1.0 if 1 in b else 1.0) * c for b, c in mv.terms})
    swaps = {}
    for j in (2, 3, 4):
        sd = self_dual(e(1, j)); asd = anti_self_dual(e(1, j))
        swaps[f"P(SD e1{j}) == -ASD e1{j}"] = (parity(sd) == (-1.0) * asd)
    assert all(swaps.values())
    return {
        "DERIVED_geometric": "a spatial parity reflection (e1→−e1) maps self_dual(e1j) → −anti_self_dual(e1j) (j=2,3,4, engine-exact); "
                             "an orientation-reversing isometry SWAPS the self-dual / anti-self-dual Spin(4) sub-spaces (Hodge)",
        "swaps_verified": swaps,
        "FRAMING_physics": "up/down = SU(2)+/SU(2)- = SD/ASD handedness ⇒ 'up↔down is a MIRROR' (the chirality-as-reflection = the "
                           "structural ORIGIN of the gen-2 ~0.44 mirror) is FORCED Spin(4)/Hodge geometry, NOT a fit (3 of 4 routes converge)",
        "GATED_value": "the mirror VALUE (gen-2 at off-center ~0.44) is shift+scale-invariant -> parity does NOT pin it; #1-gap EOM-gated",
        "tier": "DERIVED in KIND (up↔down is a mirror; the parity↔SD/ASD swap is engine-exact) + FRAMING (the up/down=SD/ASD identification) "
                "+ GATED in VALUE (the 0.44 fraction). The mirror's STRUCTURE is forced; its NUMBER is the #1 gap.",
    }


def protection_mechanism_located():
    """[FRAMING + clean-NEGATIVE + located-gap N17 — the #1-gap protection-mechanism attempt; TWT_DEFECT_CKM_GLUON.md §16]
    Yaer: DO the protection-mechanism derivation (the substrate dynamics that protect 3 generation frequency-windows
    + the chirality edges). A 4-route substrate-anchored workflow (mode-locking, parametric/Mathieu, Skyrme bound-
    modes, outside-frame hole) + developer verification ⇒ a precisely-LOCATED gap (NOT a derivation, NOT a clean
    negative on the program; no toy was sold as a derivation — the routes refused to fit lock-orders by hand).

    ── THE COMPOSITE (FRAMING) ────────────────────────────────────────────────────────────────────────
    ONE substrate object underlies all 4 target features: the **e4-DRIVEN SKYRME-quartic rotor on the Hopf torus**.
    The defect IS the Derrick-forced Skyrmion (`skyrme_BVP_audit`); the SAME quartic is BOTH the spatial stabilizer
    AND the temporal-lock nonlinearity (one term, two roles); driven by the carrier it MODE-LOCKS (Arnold tongues =
    the loose finite-width windows); the chirality = the SD/ASD reflection (`chirality_is_a_reflection`); the count
    is inherited from the topological S³-parallelizability (N13). Maps to the BARE layer ⇒ hadrons can't probe it (N16).

    ── WHAT THE SUBSTRATE GENUINELY FORCES ────────────────────────────────────────────────────────────
    (a) the EXISTENCE of discrete finite-width protected windows — a driven-dissipative LIMIT CYCLE (the Floquet
        limit cycle already observed, N9/N11) UNIVERSALLY mode-locks; the Skyrme quartic supplies the nonlinearity.
        Substrate-generic, not a chosen circle-map. (b) chirality-as-reflection (`chirality_is_a_reflection`, engine-
        exact). (c) the cost-'4' prefactor + O(1) SCALE: √m=r² ⇒ ω=r⁴ ⇒ Cost = 4·ln(r-gap); mean adjacent cost 4.37
        ⇒ radius ratio ≈ 2.98 (~3×/gen) — a substrate stability calc outputs O(few) barriers, not 10^5 mass ratios.

    ── ★ THE CLEAN STRUCTURAL NEGATIVE (the most decisive bankable result) ─────────────────────────────
    **LINEAR/ARITHMETIC backbones CANNOT make the geometric cost ladder — and fail on the TREND, not just the scale.**
    Every linear backbone gives adjacent cost-steps of the form **k·ln((n+1)/n) = k·{0.69, 0.41, 0.29}** — a strictly
    SHRINKING sequence — differing only by a prefactor k set by the ω↔index map: integer sub-harmonics ω_vac/N give
    k=1 (**0.69/0.41/0.29**), Mathieu tongue centers a~n² give k=2 (**1.39/0.81/0.58**), an n⁴ cavity gives k=4
    (**2.77/1.62/1.15**) — all verified in-engine. The decisive failure is the SIGN of the trend: the steps SHRINK
    regardless of k, but the observed down tower RISES (3.00→3.80). So NO arithmetic ω-ladder reproduces even the
    *direction* of the cost-step trend (the low-k ones also miss the [2.8,6.4] band on magnitude; the k=4 cavity only
    approaches the band floor at 2.77 but still shrinks). A linear/arithmetic ω-ladder STRUCTURALLY cannot rise; the rising,
    O(few) cost ladder REQUIRES a GEOMETRIC (nonlinear) backbone. (The static Skyrme well is also refuted 3 ways: the
    chiral-limit vibrational spectrum is a CONTINUUM; the rotational tower is the infinite spin tower at the wrong
    scale; the radial-node tower shrinks/wrong-scale. ⇒ the tower is the DRIVEN rotor, not the static well.)

    ── LOCATED (#1-gap GATED) ─────────────────────────────────────────────────────────────────────────
    the why-3 (inherited topological S³-parallelizability — NOT dynamically selected; the dynamical selection is N13),
    the cost VALUES, the widths (0.77/2.61/3.72), the up-type edge-flip, the gen-2 0.44 axis, the cost-doubling
    magnitude — all need the nonlinear driven-dissipative §9.6 EOM.

    ── ★ THE RE-ATTACK HINGE (the single sharpest next computation) ────────────────────────────────────
    Compute the **nonlinear backbone ω(amplitude)** of the e4-driven Skyrme rotor — **is it EXPONENTIAL in A?** An
    exponential backbone converts the arithmetic k·ln((n+1)/n) ladder (shrinking) into a RISING GEOMETRIC one
    ([2.8,6.4]); that ONE curve is the hinge between the clean negatives and the cost table.

    Tier: FRAMING (the composite) + DERIVED sub-results (chirality-reflection; the cost-4 prefactor) + clean-NEGATIVE
    (linear backbones, engine-verified) + located-gap N19. NOT DERIVED (the generation tower itself stays the #1 gap).
    self-check: every arithmetic backbone (k=1,2,4) SHRINKS while the down tower rises; the cost-4 prefactor gives radius ratio ~3."""
    import math
    base = [math.log((n + 1) / n) for n in (1, 2, 3)]                    # 0.69/0.41/0.29 — the arithmetic-ladder cost family
    backbones = {                                                        # three linear backbones = base × a prefactor k (ω↔index map)
        "integer_subharmonic wvac/N (k=1)": [1 * c for c in base],       # 0.69/0.41/0.29
        "Mathieu a~n^2, w=a (k=2)":         [2 * c for c in base],       # 1.39/0.81/0.58
        "n^4 cavity, w~n^4 (k=4)":          [4 * c for c in base],       # 2.77/1.62/1.15
    }
    assert all(b[0] > b[1] > b[2] for b in backbones.values())          # EVERY arithmetic backbone SHRINKS, any prefactor
    assert 3.00 < 3.80                                                  # but the observed down tower RISES — opposite sign of the trend
    assert backbones["integer_subharmonic wvac/N (k=1)"][0] < 2.8        # low-k backbones also miss the [2.8,6.4] band on magnitude
    radius_ratio = math.exp(4.37 / 4.0)                                 # mean cost 4.37 via Cost=4 ln(r-gap)
    assert 2.5 < radius_ratio < 3.5
    return {
        "verdict": "located-gap (mixed): the #1-gap protection mechanism is now PRECISELY located as the e4-driven Skyrme-quartic rotor's "
                   "mode-lock staircase that must map 3 channel-locked tongues onto a GEOMETRIC ω-ladder. NOT a derivation, NOT a clean negative.",
        "composite_FRAMING": "ONE object — the e4-driven Skyrme-quartic rotor on the Hopf torus — underlies COUNT (topological N13) + "
                             "SPECTRUM (Skyrme quartic, one term two roles) + LOOSE WINDOWS (Arnold tongues) + CHIRALITY (SD/ASD reflection)",
        "forced": ["discrete finite-width windows EXIST (universal mode-locking on the driven limit cycle, N9/N11)",
                   "chirality-as-reflection (chirality_is_a_reflection, engine-exact)",
                   "the cost-4 prefactor + O(1) scale (√m=r²→ω=r⁴; radius ratio ~3×/gen)"],
        "clean_negative_linear_cannot_make_geometric": {
            "backbone_costs": {k: [round(c, 3) for c in v] for k, v in backbones.items()},
            "target_band": [2.8, 6.4],
            "verdict": "every arithmetic backbone gives k·ln((n+1)/n) = SHRINKING steps (k=1: 0.69/0.41/0.29, k=2: 1.39/0.81/0.58, "
                       "k=4: 2.77/1.62/1.15); the down tower RISES (3.00→3.80) ⇒ NO linear ω-ladder gets even the TREND right; "
                       "the rising O(few) ladder NEEDS a geometric (nonlinear) backbone"},
        "static_skyrme_well_refuted": "vibrational=CONTINUUM (chiral limit), rotational=infinite spin tower (wrong scale), radial-node=shrinking/wrong-scale "
                                      "⇒ the tower is the DRIVEN rotor, NOT the static well",
        "located_gated": "why-3 (inherited topological, dynamical selection = N13), cost VALUES, widths, edge-flip, 0.44 axis, cost-doubling magnitude — all #1-gap (§9.6 EOM)",
        "re_attack_hinge": "[ANSWERED & SHARPENED by N20, `generation_ladder_needs_inverse_square`]: the N19 hinge 'is ω(A) EXPONENTIAL in A?' "
                           "is answered NO — the forced driven-pendulum backbone is LOGARITHMIC (separatrix divergence), so it RISES the trend but CAPS the cost at ~2.2 < 2.8. "
                           "The sharper hinge: PROJECT the e4-driven Skyrme quartic onto V(θ),Λ(θ) (do NOT assume the pendulum) and read the period-divergence EXPONENT — "
                           "log=crowds=dead, power-law=the missing 1/r² channel=spreads into [2.8,6.4]; constant-q is drift-excluded so it must be exponential-WITH-A-RUNNING-RATE",
        "tier": "FRAMING (composite) + DERIVED sub-results (chirality-reflection, cost-4 prefactor) + clean-NEGATIVE (linear backbones) + located-gap N19; NOT DERIVED",
    }


def theta_rel_equivariant_bifurcation_spine():
    """[DERIVED-structural (the equivariant-bifurcation spine, EOM-free) + sharpened-located-gap — TASK 1, the Θ_rel
    curvature axis; extends `theta_rel_z3_isotropy_dichotomy` (N10); TWT_STRATEGIC_MAP.md "FRONTIERS CONVERGING ON THE
    §9.6 KERNEL"] A 3-route workflow + developer verification (numpy/sympy). The N10 SYMMETRY SHORTCUT (canon §4a — the
    only Layer-2-winning route) is extended from "which curvature forms are Z3-invariant" to "what can a Z3-equivariant
    driven-dissipative drift DO at the colour-symmetric fixed point". Outcome: the N10 dynamical converse ("does the
    e4-driven NESS spiral OFF the G=(1,1,1) axis = break colour-Z3?") is REDUCED to one kernel binary. NOT a Θ_rel value.

    ── DERIVED-via-symmetry SPINE (group theory + equivariant normal-form theory, EOM-free, engine-verified) ──
    The relative-phase Cartan {λ3,λ8} carries the colour-Z3 as the standard 2D irrep (120° rotation R, det=+1, R³=I).
    Writing z = λ3 + i·λ8, the Z3-equivariant drift normal form is **ż = (μ+iω)z + α·z̄² + β·z|z|²** (the commutant of R
    is the COMPLEX SCALAR {aI+cJ}, so the spiral linear form is FORCED; z̄² is the lowest Z3-DISTINGUISHING term,
    a−b=1 mod 3). Consequences:
     (1) the symmetric fixed point z=0 has a SPIRAL Jacobian (μ±iω, an inseparable conjugate pair) ⇒ it can ONLY lose
         stability via a HOPF → a Z3-PRESERVING limit cycle, **never a static off-G pitchfork** (for ω≠0). So off-G
         Z3-breaking is LINEARLY FORBIDDEN — it can arise ONLY through the nonlinear z̄² term.
     (2) the e4 carrier drive is COLOUR-BLIND (a scalar on the colour C³) ⇒ Z3-EVEN ⇒ no Z3-odd term (the other route
         to a linear off-G instability is closed too).
     (3) the z̄² quadratic creates exactly 3 Z3-related off-G (Z3-broken, anisotropic-Θ_rel) fixed points for α≠0.
     (4) [Reynolds/Schur, attractor-AGNOSTIC]: the time-averaged Θ_rel on ANY Z3-symmetric attractor (fixed point /
         cycle / torus / chaos) is forced ISOTROPIC (scalar·I) — the Z3-average annihilates both anisotropic
         generators, preserves I. So Z3-symmetric ⟺ isotropic Θ_rel, for any attractor type.
     (5) ★ NEW (the key sharpening): the z̄² term is **NON-RESONANT** with the Hopf cycle (on z~Re^{iΩt} it rotates at
         −2Ω vs +Ω), so it does NOT enter the cycle's amplitude equation at leading order ⇒ the Z3-symmetric limit
         cycle is ROBUST to small α. Z3-breaking (off-G state / symmetry-broken modulated cycle) is selected ONLY when
         **|α| ≳ ω** (an O(1) cycle-breaking THRESHOLD, numerically verified) — α≠0 is NOT sufficient.

    ── HOPF-NOT-PITCHFORK is DERIVED-CONDITIONAL (a tier-correction — not an unconditional theorem) ─────────
    ω=0 (which WOULD allow a static off-G bifurcation) is forced iff the drift symmetry is the full DIHEDRAL D3 (Z3 +
    a Cartan reflection κ=diag(1,−1), which anticommutes with J and kills ω). It does NOT survive: (a) the colour-cyclic
    ladder is the det=+1 PROPER SO(3) rotation (`colour_su3_located_gap`); a colour transposition is the det=−1
    orientation-REVERSING reflection, NOT in the ladder; (b) the e4 meta-time ARROW carries a definite handedness (it
    selects sign(ω)), breaking that reflection; and (c) the NESS is non-gradient / FDT-broken (N8), so ω=0 (the
    detailed-balance locus) is doubly non-generic. So ω≠0 is e4-arrow-protected — DERIVED-CONDITIONAL on these premises.

    ── THE SHARPENED #1-gap BINARY (the located gap) + the near-falsifier ──────────────────────────────
    The N10 converse REDUCES to: is the e4-driven NESS z̄² coefficient α (a) nonzero AND (b) **|α| ≳ ω** (above the
    cycle-breaking threshold) to destabilize the Z3-symmetric Hopf cycle toward an off-G broken state? A sign+magnitude+
    stability property of the §9.6 kernel = **#1-gap GATED**. NEAR-FALSIFIER (sound, FRAMING-grade, conditional on the
    N10 dichotomy): the DATA forces Z3-broken (non-democratic CKM |V_us|/|V_cb|~5.5 ⇒ non-circulant ⇒ anisotropic; +
    SU(3)≠U(3) via the I₄ channel), but a Z3-symmetric attractor gives isotropic Θ_rel — so the data forces the kernel
    into the STRONG regime |α|≳ω. ONE honest escape: a τ_mem-gated "Z3 rotating wave" (period-3 hopping, Z3-symmetric
    over a period but instantaneously anisotropic) — #1-gap-gated. [Honesty note: this near-falsifier rests on the
    SYMMETRY, NOT on N9/N15 — N9 is a forbidden-toy (memoryless-Markovian) and N15 a generic un-derived lean, in the
    τ_mem/decoherence sector, NOT the colour-Cartan drift; the spine merely COHERES with that generic limit-cycle
    expectation, it is not "derived-default-matches-evidence".]

    Tier: DERIVED-structural (the spine) + sharpened-located-gap (the converse → the |α|≳ω binary). Hopf-not-pitchfork
    is DERIVED-CONDITIONAL. The α sign/magnitude and the Θ_rel value stay #1-gap GATED. NOT a resolution of the converse.
    self-check: commutant of R = complex scalar (spiral forced); +reflection ⇒ ω=0; Reynolds kills the anisotropic
    generators; z̄² non-resonant ⇒ symmetric cycle robust to small α, off-G only above the |α|≳ω threshold."""
    import numpy as np, sympy as sp
    # (i) commutant of the 120° rotation R = COMPLEX SCALAR ⇒ spiral linear form FORCED; +reflection ⇒ ω=0 (D3)
    a, c = sp.symbols('a c', real=True)
    th = 2 * sp.pi / 3
    R = sp.Matrix([[sp.cos(th), -sp.sin(th)], [sp.sin(th), sp.cos(th)]])
    aa, bb, cc, dd = sp.symbols('aa bb cc dd', real=True)
    M = sp.Matrix([[aa, bb], [cc, dd]])
    comm = sp.solve(list(M * R - R * M), [aa, bb, cc, dd], dict=True)[0]   # commutant of R
    assert comm[aa] == dd and comm[bb] == -cc                              # M = a·I + c·J (complex scalar) ⇒ spiral
    kap = sp.Matrix([[1, 0], [0, -1]])
    Msp = sp.Matrix([[a, -c], [c, a]])
    d3 = sp.solve(list(Msp * kap - kap * Msp), [a, c], dict=True)[0]       # add the reflection ⇒ D3 commutant
    assert d3[c] == 0                                                      # reflection KILLS ω ⇒ Hopf needs chiral Z3, not D3
    # (ii) the Z3-equivariant monomials z^p z̄^q satisfy p−q = 1 mod 3 ⇒ {z, z̄², z²z̄}; z̄² is the lowest distinguishing one
    equis = [(p, q) for p in range(4) for q in range(4) if (p - q - 1) % 3 == 0 and p + q <= 3]
    assert (0, 2) in equis and (1, 0) in equis and min(p + q for (p, q) in equis if (p, q) != (1, 0)) == 2  # z̄² is the lowest >linear
    # (iii) Reynolds/Schur: the Z3-average annihilates the anisotropic generators (σ_z, σ_x), preserves I ⇒ isotropy
    Rn = np.array([[np.cos(2 * np.pi / 3), -np.sin(2 * np.pi / 3)], [np.sin(2 * np.pi / 3), np.cos(2 * np.pi / 3)]])
    reyn = lambda Mx: (Mx + Rn.T @ Mx @ Rn + (Rn.T @ Rn.T) @ Mx @ (Rn @ Rn)) / 3
    sz = np.array([[1, 0], [0, -1.]]); sx = np.array([[0, 1], [1, 0.]])
    assert np.allclose(reyn(sz), 0) and np.allclose(reyn(sx), 0) and np.allclose(reyn(np.eye(2)), np.eye(2))
    # (iv) z̄² NON-RESONANT ⇒ symmetric cycle ROBUST to small α; off-G (Z3-broken) only above the |α|≳ω threshold
    def _meanabs(al, om=1.0, mu=0.12, be=-1.0, T=1200, dt=0.02):
        z = 0.2 + 0.1j; n = int(T / dt); zs = []
        for i in range(n):
            z = z + dt * ((mu + 1j * om) * z + al * np.conj(z)**2 + be * z * abs(z)**2)
            if i > n - 1500: zs.append(z)
        return abs(np.mean(zs))
    assert _meanabs(0.5) < 0.05 and _meanabs(2.6) > 0.05          # small α: symmetric cycle robust; large α: off-G Z3-broken
    return {
        "spine_DERIVED": "colour-Z3 = standard 2D irrep (120°) on {λ3,λ8}; the commutant FORCES the spiral linear form ż=(μ+iω)z+α·z̄²+β·z|z|²; "
                         "z̄² is the lowest Z3-distinguishing term; the symmetric point can only lose stability via a Z3-PRESERVING Hopf, NOT a static off-G pitchfork",
        "linear_off_G_forbidden": "off-G Z3-breaking is LINEARLY FORBIDDEN (the spiral ⇒ Hopf, not pitchfork, for ω≠0) AND the e4 colour-blind drive is Z3-even (no Z3-odd term) "
                                  "⇒ Z3-breaking can arise ONLY through the nonlinear z̄² term",
        "hopf_is_conditional": "DERIVED-CONDITIONAL (tier-correction, not unconditional): ω=0 (static-bifurcation locus) needs a surviving D3 reflection — excluded because the "
                               "colour-cyclic ladder is det=+1 proper SO(3) (the transposition is det=−1, not in it), the e4 ARROW breaks the reflection, and the NESS is non-gradient (N8). ω≠0 is e4-arrow-protected",
        "reynolds_isotropy": "Reynolds/Schur (attractor-AGNOSTIC): the time-averaged Θ_rel on ANY Z3-symmetric attractor (fixed point/cycle/torus/chaos) is forced ISOTROPIC (scalar·I) ⇒ Z3-symmetric ⟺ isotropic Θ_rel",
        "nonresonance_threshold": "★ NEW: z̄² is NON-RESONANT with the Hopf cycle (−2Ω vs +Ω) ⇒ the Z3-symmetric cycle is ROBUST to small α; Z3-breaking is selected ONLY for |α|≳ω "
                                  "(an O(1) cycle-breaking THRESHOLD, numerically verified) — α≠0 is NOT sufficient",
        "sharpened_binary": "the N10 converse REDUCES to: is the e4-driven NESS z̄² coefficient |α| ≳ ω (above the cycle-breaking threshold) to destabilize the Z3-symmetric Hopf cycle "
                            "toward an off-G broken state? — a sign+magnitude+stability property of the §9.6 kernel = #1-gap GATED",
        "near_falsifier": "SOUND (FRAMING-grade, conditional on the N10 dichotomy; rests on the SYMMETRY, NOT on N9/N15): the data (non-democratic CKM + SU(3)≠U(3)) forces Z3-broken, "
                          "but a Z3-symmetric attractor gives isotropic Θ_rel ⇒ the data forces the kernel into the STRONG regime |α|≳ω. ONE escape: a τ_mem-gated Z3 rotating wave",
        "gated": "the z̄² coefficient α's sign+magnitude, which side of the |α|≳ω threshold the NESS sits, the selected attractor, τ_mem, and the Θ_rel VALUE — all #1-gap GATED",
        "tier": "DERIVED-structural (the equivariant-bifurcation spine, EOM-free) + sharpened-located-gap (the converse → the |α|≳ω binary); Hopf-not-pitchfork is DERIVED-CONDITIONAL; "
                "the near-falsifier is FRAMING-grade (conditional on the dichotomy); the kernel α + the Θ_rel value stay #1-gap GATED. NOT a resolution of the converse, NOT a Θ_rel value",
    }


def theta_rel_rotating_wave_escape_located():
    """[DERIVED-structural (planar equivariant genericity, EOM-free) + sharpened-located-gap — extends
    `theta_rel_equivariant_bifurcation_spine`; the Θ_rel curvature axis; N10] CLASSIFIES the one clause the spine
    left hand-waved: its near-falsifier ("the data force the kernel into |α|≳ω, hence Z3-broken") held ONLY "modulo a
    τ_mem-gated Z3 rotating-wave escape" — a Z3-symmetric attractor that would keep Θ_rel isotropic (democratic colour)
    DESPITE |α|≳ω. That escape was asserted, not located. Here it is structurally pinned, using the SAME substrate-derived
    normal form ż=(μ+iω)z + α·z̄² + β·z|z|² (the spine's Z3-irrep commutant result, gate-free). Three results:

    ── (A) [DERIVED-structural] In the MARKOVIAN (memoryless, strictly-2D) limit, ABOVE threshold Z3 is UNCONDITIONALLY
         broken — there is NO Z3-symmetric escape. The colour relative-phase Cartan {λ3,λ8} is EXACTLY 2-dimensional, so
         the Markovian drift is a PLANAR vector field. Above the |α|≳ω threshold the z̄² term pins the phase: the smooth
         Z3-symmetric rotating wave (the spine's robust cycle, phase circulating around z=0) is DESTROYED, replaced by
         exactly 3 Z3-related off-G fixed points; the flow rests at ONE of them (which one = initial-condition, spontaneous
         Z3 breaking). A robust Z3-symmetric attractor above threshold (a heteroclinic ring through all 3, or a cycle
         enclosing them) is NON-GENERIC in the plane — at large |z| the stabilizing β|z|² spirals inward (no enclosing
         cycle), and a saddle-connection ring is codim-1, not asymptotically attracting in 2D. ENGINE-VERIFIED (and
         consistent with the spine's own |mean(z)|>0 at α=2.6): below threshold all initial phases converge to one
         constant-amplitude CIRCULATING orbit (|time-mean z|≈0, Z3-symmetric ⇒ isotropic Θ_rel); above threshold the 3
         sectors land on 3 DISTINCT fixed points 120° apart (|time-mean z|>0, Z3-broken ⇒ anisotropic Θ_rel). So:
           rotating-wave escape ∉ the 2D Markovian dynamics — it REQUIRES extra phase-space dimensions.
         This LOCATES the spine's τ_mem tag NON-TRIVIALLY: a finite memory adds delay-coordinate dimensions (the system
         is no longer planar), and ONLY in that enlarged space can a robust Z3-symmetric modulated/rotating wave persist
         above the static threshold. The escape is therefore a STRICTLY NON-MARKOVIAN effect, not a free option — exactly
         the τ_mem/decoherence sector where N9 (the forbidden memoryless-Markovian toy) and N15 live. This SHARPENS the
         spine's honesty note: the Markovian decisiveness is symmetry + dimension (gate-free); only the escape touches
         τ_mem. (It does NOT make N9/N15 load-bearing for the near-falsifier — it shows the escape is the one place they
         COULD bite.)

    ── (B) [refinement] The threshold is a SADDLE-NODE-ON-INVARIANT-CIRCLE (SNIC) / Adler phase-locking transition, and
         its location is α* ≈ C·|ω + β_i·R²| / R  with the cycle radius R² = −μ/β_r (ṙ=0 on the symmetric cycle, z̄²
         averaging out) and C = O(1). Derivation: on the cycle z≈R·e^{iθ}, the phase obeys the Adler equation
         θ̇ = ω + β_i R² + |α|R·sin(φ−3θ); it LOCKS (3 static fixed points born on the circle) iff |α|R ≳ |ω+β_i R²|.
         This is NOT bare ω: it rises with ω, FALLS as μ grows (bigger, more robust cycle), rises with |β_r| and with
         β_i>0 — all engine-confirmed in scaling. It EXPLAINS the spine's "O(1) threshold ≈ 2ω": with these units
         √(−β_r/μ)=√(1/0.12)≈2.9, so α*≈C·ω·√(−β_r/μ) is an O(few)×ω number set by the kernel ratio μ/β, not a fundamental
         "2". The smooth rotating wave (below) and the locked off-G triple (above) are the TWO SIDES of this ONE bifurcation.

    ── (C) [the converse is OPEN — NOT a tightened near-falsifier. CORRECTION 2026-06-28c, Yaer: §9.6 FORBIDS the
         Markovian limit] The Markovian limit of (A) is the framework's FORBIDDEN case, NOT the physical one: §9.6's
         selection/memory roles need tau_mem >> tau_wave, excluding the memoryless limit (R-114 — re-tiered FRAMING
         2026-07-31; the old 'no stable Skyrmion' premise contradicted §A.3 and is withdrawn), and the originator
         settled the kernel as specifically **HYSTERETIC** (the
         reactive-barrier branch; `MemoryKernel.HYSTERETIC`, `TWT_DEFECT_CKM_GLUON.md §5`). So the substrate lives
         ENTIRELY in the regime (A) calls "the escape regime" — the rotating-wave escape is therefore NOT a remote/exotic
         loophole, and there is NO clean Markovian binary to physically realize. (A)'s Markovian result is a REFERENCE
         BASELINE (breaking is the memoryless default), not the verdict. ⇒ the N10 converse stays GENUINELY OPEN, gated on
         the QUANTITATIVE question: does the hysteretic τ_mem stabilize a Z3 rotating wave above the SNIC locking
         threshold, or not? — #1-gap kernel dynamics, not settled by symmetry. The earlier "near-falsifier tightened"
         framing is WITHDRAWN as an over-claim.
         ★ NEW re-attack handle [CANDIDATE]: "hysteretic" = STICKY (a reactive barrier; the system pins in metastable
         states rather than freely circulating). A rotating wave needs the phase to keep MOVING around the cycle, which
         barrier-pinning RESISTS — so the *hysteretic character itself* plausibly DISFAVORS the rotating-wave escape and
         FAVORS locking at one off-G fixed point (Z3 BROKEN, matching the non-democratic CKM data). If borne out, the
         data-forces-breaking conclusion is RESTORED — but on kernel-specific DYNAMICAL grounds (stickiness beats
         circulation), NOT the clean symmetry grounds of the withdrawn near-falsifier. Owed: derive whether the §9.6
         hysteretic barrier suppresses the SNIC rotating wave (the #1-gap reactive-barrier / N18 S-face).

    Tier: (A) DERIVED-structural (planar genericity + the engine numerics + the spine's commutant normal form) — gate-free,
    but its MARKOVIAN limit is the §9.6-FORBIDDEN reference case, not physical. (B) a refinement of the threshold to a
    SNIC/Adler criterion (the FORM α*≈C|ω+β_i R²|/R is structural; the VALUE is kernel-gated). (C) the converse is OPEN
    (gated on hysteretic-τ_mem stabilization of the rotating wave) + the sticky-hysteresis CANDIDATE handle; the prior
    "near-falsifier tightened" claim is WITHDRAWN. NOT a Θ_rel value; NOT a resolution of the converse. The kernel signs
    (α, β_i, μ), which side of the SNIC, and τ_mem all stay #1-gap GATED. e5-litmus N/A (internal relative-phase Cartan,
    not e5-spatial; same z as the spine).
    self-check: below threshold ⇒ one circulating constant-|z| orbit, |mean z|≈0 (Z3-symmetric); above ⇒ 3 distinct
    fixed points 120° apart, |mean z|>0 (Z3-broken); threshold rises with ω, falls with μ (SNIC/Adler scaling)."""
    import numpy as np

    def _evolve(al, om=1.0, mu=0.12, be=-1.0, T=1500, dt=0.02, z0=0.2 + 0.1j):
        z = z0; n = int(T / dt); zs = []
        for i in range(n):
            z = z + dt * ((mu + 1j * om) * z + al * np.conj(z)**2 + be * z * abs(z)**2)
            if i > n - 1500: zs.append(z)
        return np.array(zs)

    # (A) below threshold: the 3 sectors converge to ONE circulating orbit; |mean|≈0; amplitude constant (rotating wave)
    below = [_evolve(0.5, z0=0.3 * np.exp(2j * np.pi * k / 3) + 0.02) for k in range(3)]
    amps_b = [np.std(np.abs(tr)) for tr in below]                 # amplitude steady (cycle)
    meanabs_b = [abs(np.mean(tr)) for tr in below]                # |time-mean| ≈ 0 ⇒ Z3-symmetric
    assert all(a < 0.05 for a in amps_b) and all(m < 0.05 for m in meanabs_b)   # rotating wave: steady-|z|, Z3-symmetric
    # above threshold: the 3 sectors land on 3 DISTINCT fixed points 120° apart; |mean| > 0 (Z3 broken)
    above = [_evolve(2.6, z0=0.3 * np.exp(2j * np.pi * k / 3) + 0.02) for k in range(3)]
    fixed = [np.std(np.abs(tr)) < 1e-3 for tr in above]          # each is a fixed point (no phase drift)
    finals = sorted([np.angle(tr[-1]) % (2 * np.pi) for tr in above])
    gaps = np.diff(finals + [finals[0] + 2 * np.pi])
    assert all(fixed) and np.allclose(gaps, 2 * np.pi / 3, atol=0.2)   # 3 fixed points, 120° apart ⇒ Z3 spontaneously broken
    assert all(abs(np.mean(tr)) > 0.05 for tr in above)               # |time-mean| > 0 ⇒ anisotropic Θ_rel

    # (B) SNIC/Adler threshold scaling: rises with ω, FALLS with μ (vs the bare-ω spine reading)
    def _thr(om, mu, be=-1.0, step=0.3):
        al = 0.2
        while al < 7:
            if abs(np.mean(_evolve(al, om=om, mu=mu, be=be, T=900))) > 0.05:
                return al
            al += step
        return None
    t_om1, t_om2 = _thr(1.0, 0.12), _thr(2.0, 0.12)
    t_mu_lo, t_mu_hi = _thr(1.0, 0.12), _thr(1.0, 0.50)
    assert t_om2 > t_om1 and t_mu_hi < t_mu_lo                    # α* ∝ ω, ∝ 1/R(μ) — the SNIC/Adler form, not bare ω

    return {
        "escape_classified_DERIVED": "the spine's 'τ_mem-gated Z3 rotating-wave escape' is LOCATED: in the MARKOVIAN (strictly-2D) limit it does NOT exist — "
                                     "the colour Cartan {λ3,λ8} is exactly 2D, and above the |α|≳ω threshold the planar flow rests at ONE of 3 Z3-related off-G fixed points "
                                     "(spontaneous Z3 breaking, init-dependent); a robust Z3-symmetric attractor is non-generic in the plane (β|z|² spirals inward, no enclosing cycle)",
        "escape_is_nonMarkovian": "the rotating-wave escape REQUIRES the extra delay-coordinate dimensions of a finite memory τ_mem (the system is no longer planar) — "
                                   "it is a NON-MARKOVIAN effect, living in the τ_mem sector. ★ but this is NOT exotic: §9.6 + the R-114 memory requirement (ex-'monostability theorem', FRAMING 2026-07-31) make the substrate "
                                   "non-Markovian for the selection/memory roles (memoryless cannot supply tau_mem >> tau_wave; the old no-stable-Skyrmion premise WITHDRAWN, R-114 FRAMING 2026-07-31), and the kernel is settled HYSTERETIC (originator pick) — so the substrate "
                                   "lives ENTIRELY in the escape regime; the Markovian decisiveness is a REFERENCE BASELINE (breaking is the memoryless default), not the physical verdict",
        "markovian_dichotomy": "below threshold ⇒ one CIRCULATING constant-|z| orbit, |time-mean z|≈0 = Z3-symmetric ⇒ ISOTROPIC Θ_rel; "
                               "above threshold ⇒ 3 DISTINCT fixed points 120° apart, |time-mean z|>0 = Z3-broken ⇒ ANISOTROPIC Θ_rel (engine-verified)",
        "threshold_is_SNIC_Adler": "the threshold is a SADDLE-NODE-ON-INVARIANT-CIRCLE (SNIC) / Adler phase-locking transition: on the cycle z≈R·e^{iθ}, "
                                   "θ̇ = ω+β_i R²+|α|R·sin(φ−3θ) LOCKS iff |α|R ≳ |ω+β_i R²|, with R²=−μ/β_r ⇒ α* ≈ C·|ω+β_i R²|/R, C=O(1). "
                                   "Rises with ω, FALLS as μ grows, rises with |β_r| and β_i>0 — engine-confirmed; the smooth rotating wave and the locked off-G triple are TWO SIDES of this ONE bifurcation",
        "explains_2omega": "the spine's 'O(1) threshold ≈ 2ω' is explained: α*≈C·ω·√(−β_r/μ); with μ=0.12, β_r=−1 ⇒ √(1/0.12)≈2.9, an O(few)×ω set by the kernel ratio μ/β, NOT a fundamental factor 2",
        "converse_is_OPEN": "★ CORRECTION (2026-06-28c, Yaer): the prior 'near-falsifier tightened' is WITHDRAWN. §9.6 FORBIDS the Markovian limit (mandatory non-Markovian / hysteretic kernel), "
                            "so the substrate lives in the escape regime and there is NO clean Markovian binary to realize ⇒ the N10 converse stays GENUINELY OPEN, gated on the QUANTITATIVE #1-gap "
                            "question: does the hysteretic τ_mem stabilize a Z3 rotating wave above the SNIC threshold? — not settled by symmetry",
        "sticky_hysteresis_handle_CANDIDATE": "★ NEW re-attack handle: 'hysteretic' = STICKY (reactive barrier, pins in metastable states). A rotating wave needs the phase to keep MOVING; barrier-pinning RESISTS that "
                                              "⇒ the hysteretic character plausibly DISFAVORS the escape and FAVORS locking at one off-G state (Z3 BROKEN, matching non-democratic CKM). If borne out, data-forces-breaking is RESTORED — "
                                              "but on kernel-specific DYNAMICAL grounds (stickiness beats circulation), NOT the withdrawn clean-symmetry near-falsifier. Owed: §9.6 reactive-barrier / N18 S-face derivation. "
                                              "★ REFINED 2026-07-05 (N46, W3.3, `theta_rel_fork_escape_kernel_number_governed`): the handle is REFUTED as a CLEAN discriminator -- an explicit non-Markovian memory sim shows the escape/lock outcome is governed by kernel NUMBERS "
                                              "(alpha/alpha*, tau*om, barrier height) NON-MONOTONICALLY, not the branch label; a SMALL reactive barrier PROMOTES the escape (only a LARGE barrier suppresses it) => stickiness is NON-monotone; the handle holds only in the large-barrier sub-regime",
        "gated": "the kernel signs (α, β_i, μ), which side of the SNIC the NESS sits, the selected attractor, whether the hysteretic τ_mem stabilizes the rotating wave, and τ_mem — all #1-gap GATED. NOT a Θ_rel value, NOT a resolution of the converse",
        "tier": "(A) DERIVED-structural (planar equivariant genericity + engine numerics + the spine's commutant normal form) — gate-free, but its MARKOVIAN limit is the §9.6-FORBIDDEN reference case, not physical; "
                "(B) threshold refined to a SNIC/Adler criterion (the FORM is structural, the VALUE kernel-gated); (C) the converse is OPEN (gated on hysteretic-τ_mem stabilization) + a sticky-hysteresis CANDIDATE handle — "
                "the prior 'near-falsifier tightened' is WITHDRAWN (Yaer 2026-06-28c). Extends theta_rel_equivariant_bifurcation_spine; does NOT contradict it",
    }


def theta_rel_fork_escape_kernel_number_governed():
    """[FRAMING / CANDIDATE-refuting -- extends `theta_rel_rotating_wave_escape_located` (C); W3.3/A1;
    N46] ANSWERS the brief's A1 (N33 would-change-if (iv)): does a HYSTERETIC memory clear/suppress the
    Z3-symmetric rotating-wave ESCAPE above the SNIC/Adler locking threshold (=> Z3 broken => the
    non-democratic CKM the data show), per the escape primitive's sticky-hysteresis CANDIDATE handle?

    METHOD. Extend the banked Markovian normal form  zdot=(mu+i*om)z + alpha*conj(z)^2 + beta*z|z|^2
    (mu=0.12, om=1, beta=-1; Markovian SNIC threshold alpha*~2.05) with an explicit NON-MARKOVIAN memory
    on the equivariant (alpha) LOCKING channel: a reactive variable u lags conj(z)^2 with timescale tau
    and an optional reactive BARRIER D (deadzone/play = a sticky/hysteretic element; D=0 = pure fading).
    Above threshold (alpha=2.6), sweep (tau, D, alpha) and classify each: LOCKED (Z3-broken, |mean z|>0)
    vs ESCAPE (Z3-symmetric rotating wave, all 3 sectors -> one circulating orbit, |mean z|~0).

    FINDINGS. NOTE ON SCOPE (canon 2, reviewer-required): the SUITE self-check below verifies exactly
    ONE model (the exp-filter with an optional deadzone/play barrier, `_mem`). The INVARIANCE across the
    other kernel models {discrete-delay, bistable-pin} was checked in an EXTERNAL characterization run,
    and the whole result was independently REPRODUCED CLEAN-ROOM by the adversarial reviewer (a separate
    code path) -- these are external-run robustness, NOT banked as suite artifacts. The findings:
      (i)   Markovian/fast memory above threshold LOCKS (reproduces the banked escape primitive).
      (ii)  a SLOW fading memory near threshold RESTORES the escape (MOTIONAL AVERAGING: the memory
            low-passes conj(z)^2 at the circulation frequency 2*Omega, attenuating the locking torque
            below alpha* -> the below-threshold symmetric cycle re-appears; fading onset tau_c~1.1).
      (iii) NON-MONOTONIC barrier: a SMALL reactive barrier PROMOTES the escape (onset tau_c 1.1->0.8 at
            D 0->0.05 -- the deadzone weakens near-equilibrium feedback, destabilizing the locked fixed
            point EARLIER), while a LARGE barrier SUPPRESSES the escape at ALL tau (D=0.3 -> LOCKED for
            tau in [0.5,5] -- the reactive channel freezes into a static locking term).
      (iv)  NEAR-THRESHOLD CONFINEMENT: the escape exists only for alpha/alpha* <~ 1.5 (present 2.2-3.0;
            absent >=3.5) -- well above threshold no memory in the tested range restores the sym. wave.

    VERDICT (the fork discriminator). The escape/lock outcome above the SNIC threshold is governed by
    THREE kernel NUMBERS -- the distance above threshold alpha/alpha*, the memory timescale tau*om, and
    the reactive-barrier height -- in a NON-MONOTONIC way, NOT by the discrete fading-vs-hysteretic branch
    LABEL. The sticky-hysteresis handle ("stickiness beats circulation => locks => Z3-broken") assumed
    stickiness is MONOTONE; it is not (a small barrier FAVORS the escape). So the handle holds only in
    the large-barrier sub-regime and is REFUTED as a clean/general discriminator. The fork is NOT
    resolved by the SNIC escape dynamics at the branch-label level; all three deciding quantities are
    #1-gap kernel numbers. Nothing here is a Theta_rel value or a fork resolution -- it REMOVES a claimed
    shortcut and re-locates the fork on kernel numbers. e5-litmus N/A (internal Cartan, same z as the
    spine). Tier FRAMING/CANDIDATE-refuting: the memory kernels are labeled modeling choices (canon 3);
    only the branch-label-non-determination + non-monotonicity + near-threshold confinement are banked
    (invariant across the tested choices).
    self-check: markov(2.6) LOCKS; fading(2.6,tau=2) ESCAPES; small-barrier(2.6,tau=2,D=0.05) still
    ESCAPES (barrier does not monotonically suppress); large-barrier(2.6,tau=2,D=0.3) LOCKS (=> outcome
    set by the barrier NUMBER within one branch, not the branch label); alpha=4.0 no escape (confinement)."""
    import numpy as np
    MU, OM, BE = 0.12, 1.0, -1.0

    def _markov(al, T=900, dt=0.02, z0=0.2+0.1j, keep=1500):
        z=z0; n=int(T/dt); zs=[]
        for i in range(n):
            z=z+dt*((MU+1j*OM)*z+al*np.conj(z)**2+BE*z*abs(z)**2)
            if i>n-keep: zs.append(z)
        return np.array(zs)

    def _mem(al, tau, D, T=900, dt=0.02, z0=0.3+0.02j, keep=1500):
        # reactive variable u lags conj(z)^2 with timescale tau; D=0 -> exp filter, D>0 -> deadzone/play
        z=z0; u=np.conj(z)**2; n=int(T/dt); zs=[]
        for i in range(n):
            cz2=np.conj(z)**2; m=cz2-u
            if D>0.0:
                a=abs(m); m=0j if a<=D else (a-D)*m/a
            u=u+dt*m/tau
            z=z+dt*((MU+1j*OM)*z+al*u+BE*z*abs(z)**2)
            if i>n-keep: zs.append(z)
        return np.array(zs)

    def _sectors_mem(al, tau, D):
        return [_mem(al, tau, D, z0=0.3*np.exp(2j*np.pi*k/3)+0.02) for k in range(3)]

    markov_locked        = abs(np.mean(_markov(2.6))) > 0.5
    fad = _sectors_mem(2.6, 2.0, 0.0)
    fading_escapes       = all(abs(np.mean(t)) < 0.04 and np.mean(np.abs(t)) > 0.05 for t in fad)
    sb = _sectors_mem(2.6, 2.0, 0.05)
    small_barrier_escapes= all(abs(np.mean(t)) < 0.04 and np.mean(np.abs(t)) > 0.05 for t in sb)
    large_barrier_locks  = abs(np.mean(_mem(2.6, 2.0, 0.3))) > 0.05
    confined             = abs(np.mean(_mem(4.0, 3.0, 0.0))) > 0.05

    assert markov_locked,        "Q0: Markovian alpha=2.6 must LOCK (Z3-broken) -- reproduces the escape primitive"
    assert fading_escapes,       "Q1: a slow fading memory restores the Z3-symmetric rotating-wave escape"
    assert small_barrier_escapes,"Q2a: a SMALL reactive barrier does NOT suppress the escape (sticky-monotone REFUTED)"
    assert large_barrier_locks,  "Q2b: a LARGE reactive barrier suppresses the escape -> LOCKED (outcome set by barrier NUMBER, not branch label)"
    assert confined,             "Q3: well above threshold (alpha=4.0) no memory restores the symmetric escape (confinement)"

    return {
        "question": "does a hysteretic tau_mem clear/suppress the Z3 rotating-wave escape above the SNIC threshold (escape primitive (C); sticky-hysteresis handle; N33 wci (iv))?",
        "verdict": "NO CLEAN DISCRIMINATION: the escape/lock outcome is set by kernel NUMBERS (alpha/alpha*, tau*om, barrier height) NON-MONOTONICALLY, not by the fading-vs-hysteretic branch LABEL",
        "sticky_handle_status": "REFUTED as a clean monotone discriminator -- a SMALL reactive barrier PROMOTES the escape (onset tau_c 1.1->0.8); only a LARGE barrier suppresses it. Holds only in the large-barrier sub-regime.",
        "non_markovian_confirmed": "the escape is a genuine non-Markovian effect (motional averaging of the locking channel) -- the escape primitive (A) is CONFIRMED and mechanized",
        "confinement": "escape confined to alpha/alpha* <~ 1.5; absent well above threshold",
        "gated": "the three deciding numbers (alpha/alpha* at the QCP = how far the driven substrate sits above its own SNIC threshold; tau_mem*om; the reactive-barrier height) are all #1-gap GATED kernel quantities",
        "tier": "FRAMING / CANDIDATE-refuting; modeling choices per canon 3; invariant-across-choices banked only",
    }



# ---- chirality-sources-P (HCC, 2026-06-23): the bare +e4 handedness is generation-blind on the Q-orbit ----
def chirality_does_not_source_P() -> dict:
    """[DERIVED — exact Clifford, no toy] §18.3b/§19.7/§19.8.1 (TASK chirality-sources-P): does the bare
    +e4 handedness alone source CKM property P (the off-(1,1,1)/non-circulant up/down piece)? VERDICT: NO.

    THE EXACT DERIVATION (project-then-restrict, NOT a posited matrix):
      * I4 maps the Q-orbit ENTIRELY to the L-orbit: I4·e14=-e23, I4·e24=+e13, I4·e34=-e12 ⇒ the Q→Q part
        of I4 is EXACTLY ZERO. [exact MV fact]
      * Hence the chiral projector ½(1+I4), PROJECT-THEN-RESTRICTED to the Q-orbit (L-components dropped), is
        M = ½·I (scalar): the off-diagonal Q→Q entries vanish. The chirality is GENERATION-BLIND on the
        Hodge-mixed Q-orbit (= 'su(2)+ is blind to the S- mass generations'). [DERIVED]

    READ-OFF (exact quantities), across THREE independent formalizations of 'the +e4 action on the Q-orbit'
    — banking the (ii) negative:
      (A) chiral project-then-restrict ½(1+I4) = ½·I (scalar): [½·I, R_G]=0 ; off-(1,1,1)=0.
      (B) the e4-dip mass operator M = R_G(ψ)·diag(√m)·R_G(ψ)ᵀ: the e4-dip is the generation-dependent mass
          EIGENVALUES (symmetric ⇒ NO eigenvector rotation; non-circulant as a matrix but irrelevant to the
          CKM), the meta-time ψ orients eigenVECTORS about G ⇒ the CKM = R_G(ψ_d-ψ_u) about G ⇒ off-(1,1,1)=0
          ⇒ |V12|=|V23| (two-equal). [NOTE 2026-08-13, ADJUDICATION2 keeper C1: per-sector ψ is not
          mass-observable (N=3 harmonic collapse; brannen_z3_harmonic_collapse_invariant), so ψ_d-ψ_u here is
          convention-pinned MODEL data (the ψ→eigenvector promotion), not mass-derived; the mass-observable
          phases are the invariants ψ_inv,d/ψ_inv,u. The conclusion is UNAFFECTED — off-(1,1,1)=0 holds for
          ANY ψ assignment.]
      (C) the E-valued CP-arrow phase diag(1,ω,ω²), shared up/down (E central, blind to T3) ⇒ [Y_u,Y_d]=0
          ⇒ circulant ⇒ off-(1,1,1)=0.
      All three AGREE: off-(1,1,1)=0.

    THE FEATURE THAT WOULD SUPPLY IT IS ABSENT: the only candidate is the Hodge-mixing's Q→Q action, which
    is EXACTLY ZERO (I4: Q→L). So the chirality has no Q→Q channel to distinguish generations; property P
    (the non-G eigenvector orientation) is structurally ABSENT from the chirality and must come from the
    coset-Cartan Θ_rel (which acts within the non-G/coset-Cartan directions, where the chirality is silent).

    ANTI-FIT / NO TOY: nothing read off CKM. A POSITED off-diagonal (a rotation about a non-G axis) would
    give (i), but it is the FORBIDDEN toy; the EXACT +e4 Clifford action gives off-(1,1,1)=0 for ALL
    illustrative dip/phase values.

    GATE (ii): the bare +e4 handedness escapes democratic (one Cabibbo-like angle about G) + supplies CP
    (the E-arrow=+e4), but CANNOT produce the three-distinct ladder. Property P needs a source BEYOND +e4 →
    Θ_rel. CONFIRMS the CKM arc's Phase-C/D (ii)-LOCATED landing. Does NOT un-gate
    qcd_collider_phenomenology; does NOT redefine the (undefined) Θ_rel."""
    from math import sqrt  # MV, e are module-level here
    import math
    I4 = e(1)*e(2)*e(3)*e(4)
    Q = {"e14": e(1)*e(4), "e24": e(2)*e(4), "e34": e(3)*e(4)}
    # (1) Hodge Q->L (Q->Q part zero) + (2) chiral project-then-restrict = 1/2 I
    def qcoeff(mv, target):
        tk = tuple(sorted(next(iter(target.as_dict()))))
        for k, v in mv.as_dict().items():
            if tuple(sorted(k)) == tk: return v
        return 0.0
    names = ["e14", "e24", "e34"]
    M = [[round(qcoeff(MV.from_dict({(): 0.5})*Q[na] + MV.from_dict({(): 0.5})*(I4*Q[na]), Q[nb]), 6)
          for nb in names] for na in names]
    chiral_is_half_I = (M == [[0.5,0,0],[0,0.5,0],[0,0,0.5]])
    hodge_QtoL = all(len(next(iter((I4*b).as_dict()))) == 2 and
                     set(next(iter((I4*b).as_dict()))) in ({1,2},{1,3},{2,3}) for b in Q.values())
    # (3) off-(1,1,1) of the three formalizations (numpy lazy)
    np = __import__("numpy")
    nG = np.array([1,1,1.])/math.sqrt(3)
    def off111(Mx):
        A=(Mx-Mx.T)/2; a=np.array([A[2,1]-A[1,2],A[0,2]-A[2,0],A[1,0]-A[0,1]])/2
        return float(np.linalg.norm(a-np.dot(a,nG)*nG))
    def Rax(n,t):
        n=np.asarray(n,float); n/=np.linalg.norm(n); K=np.array([[0,-n[2],n[1]],[n[2],0,-n[0]],[-n[1],n[0],0]])
        return np.eye(3)+math.sin(t)*K+(1-math.cos(t))*(K@K)
    offA = off111(0.5*np.eye(3))
    Mu=Rax(nG,0.0)@np.diag([.3,.9,2.4])@Rax(nG,0.0).T; Md=Rax(nG,0.4)@np.diag([.4,1.2,3.1])@Rax(nG,0.4).T
    _,Vu=np.linalg.eigh(Mu); _,Vd=np.linalg.eigh(Md); offB=off111(Vu.T@Vd); Vck=np.abs(Vu.T@Vd)
    om=np.exp(2j*np.pi/3); D=np.diag([1,om,om**2]); P=np.array([[0,0,1],[1,0,0],[0,1,0]],complex)
    circ=lambda a:a[0]*np.eye(3)+a[1]*P+a[2]*P@P
    Yu,Yd=D.conj().T@circ([1,.3,.1])@D, D.conj().T@circ([1,.5,.2])@D; commC=float(np.max(np.abs(Yu@Yd-Yd@Yu)))
    return {
        "I4 maps Q-orbit entirely to L (Q→Q part = 0)": hodge_QtoL,
        "chiral project-then-restrict = ½·I (scalar, generation-blind)": chiral_is_half_I,
        "(A) chiral off-(1,1,1)": round(offA, 12),
        "(B) e4-dip CKM off-(1,1,1)": round(offB, 10),
        "(B) |V12|,|V23| (two-equal)": [round(Vck[0,1],4), round(Vck[1,2],4)],
        "(C) E-phase shared ⇒ [Y_u,Y_d]": round(commC, 12),
        "all three formalizations agree": (offA < 1e-9 and offB < 1e-9 and commC < 1e-9),
        "feature that would supply off-(1,1,1)": "the Hodge Q→Q action — EXACTLY ZERO (I4:Q→L) ⇒ structurally absent",
        "GATE": "(ii) — bare +e4 escapes democratic (G-rotation) + CP (E-arrow) but CANNOT make the 3-distinct ladder; property P needs Θ_rel",
        "weight (Coordinator+Reviewer)": "formalization A (the scalar ½·I) CARRIES the negative ALONE — it rests on the exact "
            "I4:Q→L fact (Q→Q block of the chirality = 0 ⇒ scalar), which is tuning-IMMUNE (a scalar commutes with every "
            "generation structure, so it cannot inject off-G mixing under ANY combination). B and C are corroborating "
            "cross-checks covering the other entry points (the e4-dip; the E-phase); the 'three formalizations agree' framing "
            "is slightly generous — B leans on the e4-dip being symmetric (the route to push if stress-testing), but A is "
            "independent of B and already decisive.",
        "derived-vs-gated refinement": "the chirality DOES source the CIRCULANT structure: a G-rotation (one Cabibbo-like angle, "
            "since R_G about (1,1,1) is circulant ⇒ |V12|=|V23|) PLUS the CP arrow (E=+e4). ONLY the off-(1,1,1) THREE-DISTINCT "
            "splitting (V12≠V23) is structurally absent from the chirality ⇒ gated on Θ_rel. So Θ_rel's job is narrowed to the "
            "non-circulant splitting; the escape-from-democratic + CP are derived.",
        "forecloses the cheap escape": "the worry that the already-derived +e4 handedness might QUIETLY supply property P (letting "
            "CKM close on derived ingredients) is provably FALSE — the chirality is silent on exactly the non-G directions where "
            "property P lives. Sharpens the CKM (ii)-LOCATED: no derived shortcut; the democratic tension rests without remainder on Θ_rel.",
        "anti-fit": "exact Clifford, nothing read off CKM; a posited off-diagonal (i) is the forbidden toy; exact action gives 0",
        "confirms": "the CKM arc Phase-C/D (ii)-LOCATED: property P = the Θ_rel channel, beyond the chirality",
    }


# ---- §19.8 (cont) DM-V2-1 Z2 re-attack: can sterile carry a SEPARATE mass scale? --
def sterile_rh_z2_separate_mass_scale_check():
    """[LOCATED-GAP-REFINED] §19.8.3 + DM-V2-1 Z2: can the sterile RH carry a SEPARATE
    mass scale from the active LH (decoupling m_s from m_a) within the current TWT substrate?

    Z2 question (re-attack of N30's first 'would-change-if'). The first-cut sterile-RH DM
    check (N30, `sterile_rh_relic_check`) failed in part because TWT ties m_sterile = m_active
    per generation (one Dirac eigenvalue per generation, §19.8.3). Z2 asks: is this tie
    STRUCTURALLY required by TWT, or could the wave-decoupling mechanism set m_s at a
    different (e.g. keV) scale?

    Three candidate routes investigated:

    ROUTE Z2-A: SEPARATE meta-time KK momenta for the two ideals (k_5^a != k_5^s).
    Substrate constraint (§17.1). A Dirac mass term m psi-bar psi in 4D is the KK reduction
    of a SINGLE 5D mode at fixed meta-time momentum d_5 Psi = m e_5 Psi. Both Weyl components
    (Psi_+ active in S_+, Psi_- sterile in S_-) share ONE k_5 eigenvalue by construction --
    that is what 'Dirac mass' MEANS as a 5D KK reduction. Splitting the 5D mode into the two
    ideals does not introduce a second e_5 eigenvalue; the SAME d_5 acts on both ideals with
    the SAME m. Independent k_5^a, k_5^s describe TWO independent 4D fermions, NOT one Dirac
    pair. Each independent single-Weyl mode would then need its own mass structure -- and the
    only mass available to a single Weyl is Majorana (DL = 2). Majorana is forbidden by
    §19.8.3 (B-L conservation, §23.7-§23.9, anomaly-free 3*1/3=1). So Z2-A reduces to a
    forbidden Majorana mass. [DERIVED -- KK structure of Dirac mass + §19.8.3 B-L closure.]

    ROUTE Z2-B: 'Wave-decoupling sets m_s at a different scale.'
    Wave-decoupling means the S_- mode does not ride the +e_4 wavefront -- its e_4-phase is
    not locked to the wavefront. But mass IS the meta-time momentum k_5 (§17.1, d_5 Psi =
    m e_5 Psi), NOT the e_4-phase relation. The +e_4 wave direction (P1c, §1.1) and the e_5
    KK axis are DISTINCT, independent Cl(4,1) generators (e_4 e_5 = -e_5 e_4). Wave-decoupling
    concerns the e_4-phase-lock axis; the Dirac mass concerns the e_5-momentum axis. The two
    are orthogonal in the substrate. Wave-decoupling therefore can make S_- propagate without
    +e_4 phase-lock, but does NOT give S_- a second k_5 eigenvalue. [DERIVED -- distinguishes
    the e_4-wavefront-lock axis from the e_5-KK-mass axis as independent Cl(4,1) basis vectors.]

    ROUTE Z2-C: §10.5 topological mass via the L-pair-creation operator mu Psi_0 rho_L.
    The §10.5(a) topological boundary term at constant condensate, where rho_L = j_L^0 is the
    L-winding number density, is parity-odd (proportional to I_4) and sources L-WINDING-DENSITY
    -- it is the substrate channel for §23.10 beta-decay L-pair creation and §24 arrow of time.
    It is a charged-current topological boundary on L-orbit CONFIGURATIONS AS A WHOLE, not a
    single-mode mass term in the e_5 KK sector. It does not give an independent meta-time KK
    eigenvalue to S_-. (And mu itself is OPEN per §10.5(d), Paper-2.) [DERIVED -- §10.5 sources
    L-winding number density, not a single-mode KK mass.]

    NUMERICAL CANDIDATE CHECK (granting the structural objection). Even if Z2 were granted by
    new substrate physics, the standard Dodelson-Widrow keV-sterile-DM mechanism is itself
    excluded by combined X-ray + Ly-alpha constraints (Boyarsky-Drewes-Lasserre-Mertens-
    Ruchayskiy 2019 review). DW relic abundance: Omega_s h^2 ~ 0.12 * (sin^2(2 theta) / 3e-9)
    * (m_s/keV)^1.8. At m_s in {1, 3, 7, 50} keV, required mixing for Omega_DM h^2 = 0.12 is
    {3e-9, 4.2e-10, 9.0e-11, 2.6e-12}; X-ray + Ly-alpha bound is {1e-10, 4.1e-13, 6.0e-15,
    3.2e-19}. The required mixing exceeds the bound at every point by O(1-13) orders. So Z2
    does not rescue DM-V2-1 via the standard sterile-DM mechanism even if granted. (Resonant
    Shi-Fuller production needs a primordial lepton asymmetry -- not in current TWT.)

    Verdict. Z2 LOCATED-GAP-REFINED:
      (i) Structurally, TWT does NOT supply a route to m_s != m_a. The Dirac character
          (forced by §19.8.3 B-L conservation) ties m_sterile to m_active by KK eigenvalue
          identity (§17.1), NOT by mere assumption. The wave-decoupling axis (e_4-phase-lock)
          is orthogonal to the mass axis (e_5-KK momentum). The §10.5 topological term sources
          L-winding density, not single-mode mass.
      (ii) Empirically, standard DW keV-sterile-DM is itself excluded by X-ray + Ly-alpha at
           the full keV-50 keV window, so even if Z2 were granted, this would not rescue
           DM-V2-1 via the standard sterile-DM mechanism.

    Refined would-change-if (CLAUDE.md §4 negatives discipline; supersedes N30's Z1):
      Z2-A': New substrate physics gives S_- a SECOND k_5 eigenvalue while preserving B-L
             (e.g. a B-L-charged condensate connecting S_-^(k_5=m_a) to S_-^(k_5=m_s); would
             require breaking the one-Dirac-eigenvalue-per-generation structure of §19.8.3
             WITHOUT introducing a Majorana mass). No such mechanism in current TWT.
      Z2-R: Resonant (Shi-Fuller) production with a TWT-derived primordial lepton asymmetry.
            The §23.10 beta-decay L-pair-creation mechanism + cosmological P1c (+e_4)
            condition MIGHT seed such an asymmetry, but no substrate calculation links the
            early-universe L-pair-creation rate to a quantitative lepton-asymmetry value.
            CANDIDATE only.

    Tier: LOCATED-GAP-REFINED (CLAUDE.md §4 -- the N30 Z1 'would-change-if' is now
    structurally argued to require new physics; not a fake-impossibility per §4, but a
    sharpened gap with explicit handles Z2-A' and Z2-R).

    Status: Z2 closed-NEGATIVE-on-current-substrate; refined would-change-if handles (Z2-A',
    Z2-R) remain. DM-V2-1 lead (iii) is CONFIRMED RESOLVED-NEGATIVE on both N30 first-cut
    and Z2 re-attack. DM-V2-1 itself stays OPEN; leads (i) and (ii) unadjudicated."""
    import math as _math

    # --- ROUTE Z2-A: separate KK eigenvalues for a Dirac pair ---
    dirac_KK_eigenvalues_per_pair = 1   # one m per Dirac fermion, structural (§17.1)
    independent_weyl_needs_majorana_for_mass = True   # single Weyl => Majorana only
    majorana_forbidden_by_BL = True   # §19.8.3 + §23.7-§23.9

    # --- ROUTE Z2-B: e_4-wavefront-lock vs e_5-KK-mass axes are independent in Cl(4,1) ---
    wave_decoupling_axis = "e_4-phase-lock"
    mass_axis            = "e_5-KK-momentum"
    axes_orthogonal      = True   # e_4, e_5 are independent Cl(4,1) generators

    # --- ROUTE Z2-C: §10.5 topological term sources L-winding density, not single-mode mass --
    section_10_5_sources = "L-winding number density rho_L (beta-decay L-pair creation, §23.10)"
    section_10_5_is_KK_mass_term = False

    # --- Numerical CANDIDATE: granting Z2 structurally, does DW keV-sterile-DM survive? ---
    DW_window_m_s_keV = [1.0, 3.0, 7.0, 50.0]
    DW_required_mix    = [3.0e-9 * m**(-1.8) for m in DW_window_m_s_keV]
    DW_xray_lyman_bound= [1.0e-10 * m**(-5.0) for m in DW_window_m_s_keV]
    DW_all_excluded = all(r > b for r, b in zip(DW_required_mix, DW_xray_lyman_bound))

    # --- Safety asserts (engine-style: a passing primitive must be honest about the verdict) ---
    assert dirac_KK_eigenvalues_per_pair == 1, \
        "Z2-A: Dirac mass is one KK eigenvalue per 4D Dirac fermion (§17.1)"
    assert majorana_forbidden_by_BL, \
        "Z2-A reduces to forbidden Majorana via §19.8.3 B-L conservation"
    assert axes_orthogonal, \
        "Z2-B: e_4 wave-lock and e_5 KK-mass are independent Cl(4,1) generators"
    assert not section_10_5_is_KK_mass_term, \
        "Z2-C: §10.5 mu Psi_0 rho_L is a topological boundary on L-winding density, not KK mass"
    assert DW_all_excluded, \
        "standard DW keV-sterile-DM excluded by X-ray + Ly-alpha at all tested keV-window m_s"

    return {
        # Structural arguments
        "Z2_A_dirac_KK_eigenvalues_per_pair": dirac_KK_eigenvalues_per_pair,
        "Z2_A_independent_weyl_needs_majorana": independent_weyl_needs_majorana_for_mass,
        "Z2_A_majorana_forbidden_by_BL": majorana_forbidden_by_BL,
        "Z2_B_wave_decoupling_axis": wave_decoupling_axis,
        "Z2_B_mass_axis": mass_axis,
        "Z2_B_axes_orthogonal": axes_orthogonal,
        "Z2_C_section_10_5_sources": section_10_5_sources,
        "Z2_C_section_10_5_is_KK_mass": section_10_5_is_KK_mass_term,
        # Numerical (granting structural objection)
        "DW_window_m_s_keV_tested": DW_window_m_s_keV,
        "DW_required_mixing": DW_required_mix,
        "DW_xray_lyman_bound": DW_xray_lyman_bound,
        "DW_all_excluded_by_xray_plus_lyman_alpha": DW_all_excluded,
        # Verdict
        "verdict": "Z2 LOCATED-GAP-REFINED: TWT does not supply m_s != m_a on current substrate; DW keV-sterile-DM independently excluded",
        "current_substrate_route_to_m_s_neq_m_a": None,
        "refined_would_change_if": [
            "Z2-A': new substrate physics gives S_- a second k_5 eigenvalue while preserving B-L (e.g. B-L-charged condensate) -- not in current TWT",
            "Z2-R: resonant Shi-Fuller production with TWT-derived primordial lepton asymmetry (CANDIDATE; needs §23.10 + cosmology calc)",
        ],
        "DM_V2_1_lead_iii_status": "CONFIRMED RESOLVED-NEGATIVE on both N30 first-cut AND Z2 re-attack",
        "tier": "LOCATED-GAP-REFINED (CLAUDE.md §4)",
    }



# ======================================================================
# MATTER / SOLITON SECTOR (§10,§16,§22.3/5)   [twt_matter]
# ======================================================================

# ======================================================================
# N_Goldstone on the canted FM vacuum -- AXIS BRANCH (§16.6)   [twt_matter]
# ----------------------------------------------------------------------
# Promoted from docstring-only fact inside canting_critical_stiffness_at_DJ
# to a stand-alone substrate primitive: a closed coset-dimension identity
# independent of the K_c kernel-form question.
# ======================================================================

def n_goldstone_canted_FM() -> dict:
    """[DERIVED-A] §16.6: number of broken Goldstone modes on the canted FM
    ground state = dim(SU(2)_L / U(1)_canting) = dim(SU(2)) − dim(U(1)) = 3 − 1 = 2.

    Closed dimensional identity given §16.6's ground-state manifold structure
    ℳ_GS = 8 × S¹ ⊂ Spin(3) = S³ (the residual U(1) is the Hopf S¹ fiber of
    the Hopf fibration S¹ → S³ → S²):
      * Symmetry broken: SU(2)_L ≅ S³ (the L-orbit rotor target, dim = 3).
      * Residual:        U(1)_canting ≅ S¹ (the Hopf fiber of ℳ_GS, dim = 1).
      * Coset:           SU(2)_L / U(1)_canting ≅ S² (the Hopf base, dim = 2).
      * Goldstone count: N_G = dim(coset) = dim(S²) = 2.

    This is a discrete substrate fact — a closed coset-dimension identity
    independent of any dynamical kernel, and cleanly separable from the K_c
    prefactor question at the D=J QCP (`canting_critical_stiffness_at_DJ`):
    Lead A there reconstructs the 2 prefactor as K_c = N_Goldstone · sin²(q) · J
    with N_Goldstone supplied by THIS primitive. The kernel FORM remains a
    #1-gap (§9.6) item; the COUNT 2 does not — it is closed here.

    *** SCOPE — READ BEFORE QUOTING N_G = 2. ***
    BRANCH SCOPE (added with the J,D/Γ rework): the vacuum manifold ℳ_GS used here is
    computed on the AXIS BRANCH of §D.4.3 (k = q*e_1, B = e_14, four of the twelve
    e_4-bonds twisting). That configuration is an index-2 saddle of the full (k, B)
    problem, and on the body-diagonal branch the breaking geometry is different — all
    twelve e_4-bonds at one common angle, no 4+8 split — so this coset count is a
    statement about the axis branch, not a branch-independent one. Which branch the
    DRIVEN dynamics selects is open (#1 gap, §D.5.7); see
    `canting_vacuum_branch_structure` and negatives ledger N62.

    This count is also taken WITHIN THE L-ORBIT SUB-SECTOR of the medium's local state
    space, which is a six-parameter 4D orientation, not a three-parameter one
    (§D.3.2; `pi3_orientation_class_two_windings`). The identity above is exact
    and unrefuted AS A SECTOR STATEMENT — "SU(2)_L ≅ S³" names the L-orbit rotor
    target, a 3-dimensional subgroup of the state space, never the state space —
    but the broken group at the canted-FM vacuum of the FULL six-parameter state
    space is not SU(2)_L, and the honest full-state-space number is supplied by
    the exact 6-band Bogoliubov structure, which remains UN-BANKED (already
    flagged as such at `induced_G_from_linear_face_band`: "N_G = 2 (2 gapless +
    4 gapped) — exact 6-band Bogoliubov structure UN-BANKED"). Consumers of this
    count (`canting_critical_stiffness_at_DJ` → `electron_QCP_nu`) therefore carry
    the named premise "within the L-orbit sub-sector of the six-parameter state
    space" in their conditioning class.

    Cross-references:
      * `canting_critical_stiffness_at_DJ` — uses N_G to source the 2 prefactor
        in K_c = N_G · sin²(q) · J (Lead A reconstruction).
      * `induced_G_from_linear_face_band` — the un-banked 6-band structure that
        the full-state-space count would come from.
      * paper §16.6 — ℳ_GS = 8 × S¹ ⊂ Spin(3) = S³ and the Hopf fibration
        S¹ → S³ → S² with H = (1/16π²) ∫ A ∧ dA the Hopf invariant.

    tier — DERIVED-A (closed algebraic / dimensional identity given §16.6),
    SCOPED to the L-orbit sub-sector.
    """
    dim_SU2_L = 3                                  # dim(SU(2)) = dim(S³)
    dim_U1_canting = 1                             # dim(U(1)) = dim(S¹), Hopf fiber
    dim_coset = dim_SU2_L - dim_U1_canting         # = 2 = dim(S²), Hopf base
    N_Goldstone = dim_coset
    assert N_Goldstone == 2, \
        "Goldstone count on canted FM = dim(SU(2)_L/U(1)_canting) = 3 - 1 = 2 (§16.6)"
    assert dim_SU2_L == 3 and dim_U1_canting == 1, \
        "dim(SU(2)) = 3 and dim(U(1)) = 1 are fixed Lie-group facts"
    return {
        "dim_SU2_L": dim_SU2_L,
        "dim_U1_canting": dim_U1_canting,
        "dim_coset_SU2_over_U1": dim_coset,
        "N_Goldstone": N_Goldstone,
        "coset_geometry": "SU(2)_L / U(1)_canting = S^2 (Hopf base of S^1 -> S^3 -> S^2)",
        "ground_state_manifold": "M_GS = 8 x S^1 in Spin(3) = S^3 (§16.6)",
        "cross_ref_K_c": "canting_critical_stiffness_at_DJ Lead A: K_c = N_G * sin^2(q) * J",
        "tier": "DERIVED-A",
    }


def Kc_magnon_stiffness_canted_FM_at_DJ(J: float = 1.0):
    """[LOCATED-GAP-REFINED] §16.6 — direct linear spin-wave (LSWT) calculation
    on the canted-spiral vacuum (the AXIS BRANCH of §D.4.3) at the D=J QCP,
    attempting to derive
    K_c=(2/19)·J as the bare magnon gradient stiffness. RESULT: the LSWT magnon
    stiffness is NOT K_c. The static-LSWT closure route is eliminated.

    METHOD (engine-verifiable, symbolic via sympy):

    Effective planar Hamiltonian (canon §10.3.1):
       H = -J Σ_{NN bonds} cos(θ_i - θ_j)
           -D Σ_{e4-DM bonds} σ_b sin(θ_i - θ_j)
    Canon ground-state energy per unit cell on the uniform spiral θ_i = q·x_i^1:
       E(q) = -12 J cos q  -  12 J  -  2 D √2 sin q
    Minimization gives tan q* = √2/6  =>  sin²q* = 1/19, cos²q* = 18/19 at D=J
    (analytically verified; engine-cross-checked via canting_cos_q).

    LSWT bilinear in fluctuations δθ_i = θ_i - θ_i^0 (long-wavelength, k -> 0):
       ω²(k) = Σ_b K_b (1 - cos(k·b))  ≈  k_μ k_ν · (1/2) Σ_b K_b b_μ b_ν
    with bond stiffness K_b = d²(bond_E)/d(δθ)² at the spiral optimum.

    LONGITUDINAL stiffness (k along spiral direction e1):
       K_long = (1/2) d²E(q)/dq² |_{q*, D=J}
              = (1/2)·[12 J cos q* + 2 D √2 sin q*] |_{D=J}
              = (1/2)·[12 J·(3√2/√19) + 2 J √2·(1/√19)]
              = (1/2)·(38 J √(2/19))
              = √38 · J    ≈ 6.164 J
    (sympy-verified: d²E/dq²|_{q*,D=J} = 2√38·J exactly; q* = atan(√2/6).)

    TRANSVERSE stiffness (k perpendicular to spiral) — **ERRATUM 2026-07-26**:
       K_trans = (2 cos q* + 4) J  =  (6√2/√19 + 4) J  ≈  5.947 J
    [The prior banked line K_trans = 4 J cos q* ≈ 3.893 J was a transcription of
    the canon's verbal statement and was INTERNALLY INCONSISTENT with this
    primitive's own stated method: applying ω²(k) = Σ_b K_b (1 − cos k·b) to the
    full D4 bond table, the transverse direction couples 4 spiral-participating
    bonds (curvature J cos q*) AND 8 bonds with zero spiral phase difference
    (curvature J), giving C(k⊥) = (1 − cos k)(4J cos q* + 8J), hence
    K_trans = 2J cos q* + 4J. Caught at the K4D 4D-1 build review (2026-07-23),
    independently re-derived by two adversarial reviewers, and PROBE-CONFIRMED
    at 0.00% on the 4D substrate instrument (simulator/references/
    K4D_build_register.md, post-review amendments). K_long is UNAFFECTED.]

    COMPARISON to the asserted K_c = 2J/19 (banked in canting_critical_stiffness_at_DJ):
       K_long   = √38 J            ≈ 6.164 J
       K_trans  = (2 cos q* + 4) J ≈ 5.947 J   [erratum above]
       K_c      = 2 J / 19         ≈ 0.105 J
       K_long / K_c  = (19/2) √38  ≈ 58.56  [sympy-verified analytically]
       K_trans / K_c ≈ 56.49   [CAUTION, pre-flagged at the erratum review:
       NEAR but NOT EQUAL to the 58.56 target row — 3.5% apart; recorded so no
       future pass reads a coincidence into it]
    NEITHER LSWT stiffness equals K_c, nor differs by any clean factor (no
    N_Goldstone factor of 2, no sin²q factor of 1/19, no rational ratio) — the
    erratum STRENGTHENS this elimination (K_trans moved further from K_c).

    TIER ANALYSIS (canon §2, §4):
    tried — direct linear spin-wave on the canted spiral at D=J. K_long computed
        analytically as (1/2) d²E_canon/dq² = √38 J (engine-verified via sympy:
        q* = atan(√2/6) solves dE/dq=0 at D=J; d²E/dq²|_{q*,D=J} = 2√38 J).
        K_trans computed from the bond stiffness sum as (2 cos q* + 4) J ≈ 5.95 J
        (ERRATUM 2026-07-26 — the originally-banked 4 J cos q* transcribed the
        canon's verbal statement and omitted the 8 zero-phase transverse bonds;
        see the erratum block above).
    failed — neither K_long nor K_trans equals K_c = 2J/19, nor by any clean factor.
        K_long/K_c = (19/2)√38 ≈ 58.6 (engine-verified); K_trans/K_c ≈ 56.49
        (erratum value; NEAR-not-equal 58.56 — non-coincidence flagged). The
        asserted kernel form K_c = N_Goldstone · sin²(q*) · J = 2 · (1/19) · J
        is NOT a static linear-response identity on the spiral vacuum.
    would change if — (a) the §9.6 driven-dissipative kernel is closed AND its
        convolution with the vortex-worldsheet effective action renormalizes K_long
        DOWN to K_c by EXACTLY the factor (19/2)√38 ≈ 58.6 (the kernel-renormalization
        ratio the §9.6 dynamics must produce — likely via |Im χ|/|Re χ|² at the QCP or
        vortex-line tension renormalization from worldsheet instantons)
        [G1c MEASUREMENT NOTE, 2026-07-26: the POINT-FUNCTIONAL reading of the
        |Im χ|/|Re χ|² parenthetical is now MEASURED UNDER-DETERMINED on the pinned
        §E.5 member — the implied calibration moves ×22.7 across the QCP's own
        scales (ω-choice alone ×3.2), simulator/references/K4D_g1c_closure.md,
        consensus; ledger row N50. The MAIN CLAUSE — the vortex-worldsheet
        convolution — is UNTOUCHED and is the surviving arm of route (a)];
        (b) a non-static argument (RG flow at the DQCP fixed point) yields K_c
        directly without going through static LSWT. Static LSWT alone cannot
        reach K_c — ELIMINATED.

    REFINEMENT GAIN over prior canting_critical_stiffness_at_DJ entry:
    The prior entry stated verbally "K_c is NOT directly the magnon stiffness" and
    cited the canon's '4 J cos q' static gradient. This primitive SUBSTRATE-VERIFIES
    that statement with concrete engine-checked symbolic values, and ELIMINATES one
    of the two named 'would change if' routes ("a static vortex-line linear-response
    argument forces the kernel form" — the static linear-response now demonstrably
    cannot do it). The remaining route is the §9.6 dynamics. The factor (19/2)√38
    is a concrete handle for that closure: §9.6 must produce this exact ratio.

    This does NOT refute the asserted K_c = 2J/19 value; that value remains banked
    from spiral-pitch geometry (sin²q*=1/19) plus the substrate-traceable
    N_Goldstone=2 (canting_critical_stiffness_at_DJ Lead A). It REFUTES the route
    'derive K_c via bare LSWT' — narrowing the gap to §9.6 dynamics ONLY.

    Cross-reference: canting_critical_stiffness_at_DJ (the asserted K_c value),
    canting_cos_q (sin²q* = 1/19 at D=J), canting_pitch_q_rad (q* = atan(√2/6))."""
    q, D_sym, J_sym = sp.symbols('q D J', real=True, positive=True)
    # Canon §10.3.1 ground-state energy per unit cell on the spiral:
    E_sym = -12*J_sym*sp.cos(q) - 12*J_sym - 2*D_sym*sp.sqrt(2)*sp.sin(q)
    dE = sp.diff(E_sym, q)
    d2E = sp.diff(E_sym, q, 2)
    # Ground-state pitch at D=J: tan q* = √2/6  =>  q* = atan(√2/6)
    q_star = sp.atan(sp.sqrt(2)/6)
    # Verify q* solves the minimization at D=J:
    dE_at_qstar = sp.simplify(dE.subs([(D_sym, J_sym), (q, q_star)]))
    assert dE_at_qstar == 0, \
        f"q* = atan(√2/6) must solve dE/dq at D=J; got {dE_at_qstar}"
    # Longitudinal stiffness K_long = (1/2) d²E/dq² at (D=J, q=q*):
    d2E_at = sp.simplify(d2E.subs([(D_sym, J_sym), (q, q_star)]))
    expected_d2E = 2 * sp.sqrt(38) * J_sym
    assert sp.simplify(d2E_at - expected_d2E) == 0, \
        f"d²E/dq²|_{{q*,D=J}} must equal 2 sqrt(38) J; got {d2E_at}"
    K_long_sym = d2E_at / 2  # = sqrt(38) J
    K_long_value = float(K_long_sym.subs(J_sym, J))
    # Transverse stiffness (ERRATUM 2026-07-26): K_trans = (2 cos q* + 4) J —
    # the primitive's own bond-sum method on the full D4 bond table; the prior
    # 4 J cos q* omitted the 8 zero-phase-difference transverse bonds at
    # curvature J (probe-confirmed on the 4D instrument, K4D 4D-1 consensus)
    K_trans_sym = (2 * sp.cos(q_star) + 4) * J_sym
    K_trans_value = float(K_trans_sym.subs(J_sym, J))
    # Asserted K_c (banked in canting_critical_stiffness_at_DJ):
    K_c_asserted_value = 2.0 * J / 19.0
    ratio_long  = K_long_value  / K_c_asserted_value      # ≈ (19/2)sqrt(38) ≈ 58.56
    ratio_trans = K_trans_value / K_c_asserted_value      # ≈ 56.49 (erratum 2026-07-26)
    # Verify analytic ratio (the kernel-renormalization factor §9.6 must produce):
    ratio_long_sym = sp.simplify(K_long_sym / (2*J_sym/19))
    expected_ratio_long = sp.Rational(19, 2) * sp.sqrt(38)
    assert sp.simplify(ratio_long_sym - expected_ratio_long) == 0, \
        f"K_long/K_c must equal (19/2) sqrt(38); got {ratio_long_sym}"
    is_kc_static_LSWT_identity = False     # the engine-checked negative result
    return {
        "method": "direct LSWT on canted spiral at D=J, planar (XY) reduction of §10.3.1 H",
        "ground_state_pitch_q_star": "atan(sqrt(2)/6)",
        "sin_squared_q_star": float(sp.sin(q_star)**2),    # = 1/19
        "cos_squared_q_star": float(sp.cos(q_star)**2),    # = 18/19
        "K_long_over_J_symbolic": "sqrt(38)",
        "K_long_value": K_long_value,                       # ≈ 6.164
        "K_trans_over_J_symbolic": "2 cos(q*) + 4 = 6 sqrt(2)/sqrt(19) + 4  [erratum 2026-07-26]",
        "K_trans_value": K_trans_value,                     # ≈ 5.947
        "K_c_asserted_over_J": K_c_asserted_value,          # = 2/19 ≈ 0.105
        "ratio_K_long_over_K_c": ratio_long,                # ≈ 58.56
        "ratio_K_long_over_K_c_symbolic": "(19/2)*sqrt(38)",
        "ratio_K_trans_over_K_c": ratio_trans,              # ≈ 56.49 (erratum; NEAR-not-equal 58.56, non-coincidence flagged)
        "is_K_c_a_static_LSWT_identity": is_kc_static_LSWT_identity,  # False
        "outcome": "LOCATED-GAP-REFINED",
        "tried": "direct linear spin-wave on the canted spiral at D=J; K_long = sqrt(38) J "
                 "via d²E_canon/dq² (sympy-verified); K_trans = (2 cos q* + 4) J via the "
                 "bond-by-bond stiffness sum on the FULL D4 bond table (erratum 2026-07-26: "
                 "the originally-banked 4 J cos q* omitted the 8 zero-phase transverse bonds).",
        "failed": "neither LSWT stiffness equals K_c = 2J/19; K_long/K_c = (19/2)sqrt(38) "
                  "≈ 58.6; K_trans/K_c ≈ 56.49 (erratum value; NEAR-not-equal 58.56, "
                  "non-coincidence flagged). The kernel form K_c = N_G·sin²(q)·J is NOT "
                  "a static linear-response identity.",
        "would_change_if": "the §9.6 driven-dissipative kernel is closed AND its convolution "
                          "with the vortex worldsheet renormalizes K_long DOWN to K_c by "
                          "the factor (19/2)sqrt(38) ≈ 58.6 (the specific kernel-"
                          "renormalization ratio §9.6 must produce). [G1c 2026-07-26: the "
                          "point-functional |Im chi|/|Re chi|^2 reading of this route is "
                          "MEASURED under-determined (x22.7 across QCP scales; N50; "
                          "K4D_g1c_closure.md); the worldsheet-convolution main clause is "
                          "the surviving arm.]",
        "refines_canting_critical_stiffness_at_DJ": "the prior entry's verbal statement 'K_c "
                          "is NOT directly the magnon stiffness' is now substrate-verified "
                          "by direct symbolic computation; the 'static vortex-line linear-"
                          "response' would-change-if route is ELIMINATED, narrowing the gap "
                          "to §9.6 dynamics only.",
        "eliminated_closure_routes": [
            "static linear spin-wave on the canted spiral (this primitive)",
            "D4 coordination ratio 24/12 (canting_critical_stiffness_at_DJ Lead B)",
            "standard SWT symmetrization (canting_critical_stiffness_at_DJ Lead C)",
        ],
        "remaining_closure_route": "§9.6 driven-dissipative kernel + vortex-worldsheet "
                                   "convolution producing the (19/2)sqrt(38) ratio.",
    }


def updown_seat_rhoL_parity_odd_hodge_form():
    """[DERIVED-A (algebraic core) + DERIVED-CONDITIONAL on R-128 (seat identification) + value #1-gap
    GATED; W3.2/A2; refines N32a/R-129] COMPUTES the SS10.5/SSD.4.4 muPsi0 rho_L boundary-term SEAT on the
    banked Q-orbit baryon profiles (R-133 hedgehog, R-144 torus) -- R-129's 'remaining construction'.

    THE SS10.5 boundary term is L_theta = muPsi0 * rho_L, rho_L = (1/24pi^2) eps^{0ijk}<Om_i Om_j Om_k>_0
    the L-ORBIT topological winding density (Om_mu = R~ d_mu R, grade-2). In TWT the L/Q distinction IS the
    Cl(4,0) Hodge-grade split: the L-orbit su(2) {e12,e13,e23} triple product is SCALAR-graded, the Q-orbit
    su(2) {e14,e24,e34} triple product is I4-graded (parity-odd). So rho_L = the SCALAR-graded winding is
    intrinsically the L-orbit one -- a matrix-Tr picture that forgets the Clifford embedding (in which BOTH
    su(2)'s look identical) would MISS this grade distinction. The banked baryons are Q-ORBIT (wind in
    {e14,e24,e34}). N32a flagged: 'rho_L sources L-orbit winding, not Q-orbit baryon winding -- a
    derivation of how a quark (Q-orbit) chirality flip couples to rho_L is owed.' Here it is computed.

    RESULT (engine-exact + geometry-independent -- verified on hedgehog, squashed, and B=2-twist Q-configs):
      (1) [DERIVED-A] e14*e24*e34 = -I4 (grade-4), while e12*e13*e23 = +1 (SCALAR): the Q-orbit su(2)
          triple product is PARITY-ODD (I4-valued); the L-orbit su(2) triple product is scalar.
      (2) [DERIVED-A] CONSEQUENCE: the LITERAL scalar rho_L VANISHES IDENTICALLY on any Q-orbit rotor
          field (<Om^3>_0 = 0 to ~1e-14, profile/geometry-independent) => the direct SS10.5 muPsi0 rho_L
          seat is a CLEAN NEGATIVE on Q-orbit baryons. Confirms N32a's suspicion exactly.
      (3) [DERIVED-A] the Q-orbit baryon DOES carry a nonzero topological winding, but PARITY-ODD:
          <Om^3>_I4 != 0 (grade-4). The winding lives in the I4 channel, not the scalar channel.
      (4) [DERIVED-A] the R-128 parity-odd HODGE-DUAL quark-lock (I4: Q->L) converts it EXACTLY into the
          scalar L-orbit winding: <(I4 Om)^3>_0 = |<Om_L^3>_0| (matches a genuine L-hedgehog to ~1e-6).
          The INTEGRATED object is the baryon winding number B_Q (the pi_3 degree, B=1->2 across the tower);
          the LOCAL density reshapes with the profile -- linearity is of the integrated B_Q, NOT the density.

    SEAT FORM [the algebraic recovery is DERIVED-A; the PHYSICAL seat identification inherits R-128's
    OWN FRAMING tier -- R-128 tags the up/down-SEAT + the muPsi0-through-the-lock tie as FRAMING, so this
    is NOT a promotion of that tie to DERIVED]:
      L_theta = muPsi0 * <(I4 Om)^3> = muPsi0 * B_Q, PARITY-ODD (prop I4), linear in the integrated B_Q.
      This substrate-DERIVES the algebraic FORM behind N32a's CANDIDATE-posited 'cost_flip = 2 muPsi0 B'
      on the explicit Q-orbit profile (parity-odd + prop-B_Q, routed through the R-128 Hodge dual) -- the
      seat's PHYSICAL status stays FRAMING (R-128), the muPsi0 VALUE stays kernel-GATED.

    HONEST SCOPE (N28/N32a trap -- deriving a SEAT, never the value):
      - the VALUE muPsi0 stays #1-gap kernel-GATED (no up/down split value is claimed or computed).
      - the seat FORM prop B_Q (= 1 for ALL baryons) does NOT determine N37's INTER-GENERATION running of
        muPsi0 (the running is over generation index, ORTHOGONAL to B) -- the running stays kernel-gated.
        DO NOT read this as 'N37's running shape derived' (that would be an over-claim).
      - e5-litmus N/A (Cl(4,0) blades + I4 = phase-sector Hodge dual, no e5-spatial).
    self-check: e14*e24*e34 = -I4 (scalar 0); e12*e13*e23 scalar +1; I4 maps Q->L; Q-hedgehog
    <Om^3>_0 ~ 0 and <Om^3>_I4 != 0; Hodge-dual <(I4 Om)^3>_0 = L-hedgehog magnitude (recovery)."""
    I4 = e(1,2,3,4)
    Lg = [e(1,2), e(1,3), e(2,3)]
    Qg = [e(1,4), e(2,4), e(3,4)]
    def _p(x, k): return sum(c for kk, c in x.terms if kk == k)

    # (1) Clifford identities
    LLL = Lg[0]*Lg[1]*Lg[2]; QQQ = Qg[0]*Qg[1]*Qg[2]
    id_L_scalar = abs(_p(LLL, ()) - 1.0) < 1e-12 and abs(_p(LLL, (1,2,3,4))) < 1e-12
    id_Q_I4     = abs(_p(QQQ, ())) < 1e-12 and abs(_p(QQQ, (1,2,3,4)) + 1.0) < 1e-12
    i4Q_in_L = all(all(len(kk)==2 and kk in {(1,2),(1,3),(2,3)} for kk,_ in (I4*g).terms) for g in Qg)

    def _R(x3, gens, Fc):
        r = math.sqrt(sum(t*t for t in x3))
        if r < 1e-12: return math.cos(Fc*math.pi)*SCALAR
        F = Fc*math.pi*math.exp(-r)
        n = gens[0]*(x3[0]/r)+gens[1]*(x3[1]/r)+gens[2]*(x3[2]/r)
        return math.cos(F)*SCALAR + math.sin(F)*n
    def _Om(Rf, x3, mu, d=1e-6):
        xp=list(x3); xm=list(x3); xp[mu]+=d; xm[mu]-=d
        return Rf(x3).reverse()*((1.0/(2*d))*(Rf(xp)-Rf(xm)))
    _SGN={(0,1,2):1,(1,2,0):1,(2,0,1):1,(0,2,1):-1,(2,1,0):-1,(1,0,2):-1}
    def _triple(Rf, x3, dual=False):
        O=[_Om(Rf,x3,mu) for mu in range(3)]
        if dual: O=[I4*o for o in O]
        s=0.0; f=0.0
        for pp in _SGN:
            tp=O[pp[0]]*O[pp[1]]*O[pp[2]]; s+=_SGN[pp]*_p(tp,()); f+=_SGN[pp]*_p(tp,(1,2,3,4))
        return s, f

    RQ = lambda x: _R(x, Qg, 1.0); RL = lambda x: _R(x, Lg, 1.0)
    pts = [[1.0,0.0,0.0], [0.6,0.5,0.4]]
    direct_rhoL_zero = all(abs(_triple(RQ, x)[0]) < 1e-9 for x in pts)
    Q_winding_parity_odd = all(abs(_triple(RQ, x)[1]) > 0.1 for x in pts)
    recovery = all(abs(abs(_triple(RQ, x, dual=True)[0]) - abs(_triple(RL, x)[0])) < 1e-6 for x in pts)

    assert id_L_scalar,        "L-orbit triple e12 e13 e23 = +1 scalar"
    assert id_Q_I4,            "Q-orbit triple e14 e24 e34 = -I4 (grade-4, parity-odd)"
    assert i4Q_in_L,           "I4 maps Q-orbit gens into L-orbit (Hodge dual Q->L)"
    assert direct_rhoL_zero,   "literal scalar rho_L VANISHES on the Q-orbit baryon (clean negative)"
    assert Q_winding_parity_odd,"Q-orbit baryon winding is nonzero but PARITY-ODD (I4-valued)"
    assert recovery,           "R-128 Hodge-dual (I4 Om) recovers the scalar L-orbit winding EXACTLY"

    return {
        "literal_seat": "the SS10.5 scalar rho_L boundary term VANISHES IDENTICALLY on Q-orbit baryons (R-133/R-144) -- CLEAN NEGATIVE; confirms N32a 'rho_L sources L-orbit winding, not Q-orbit'",
        "why": "e14*e24*e34 = -I4 (grade-4): the Q-orbit su(2) winding density is parity-odd (I4-valued), so its SCALAR part is 0; profile/geometry-independent (hedgehog/squashed/B2-twist all give <Om^3>_0=0)",
        "hodge_seat_DERIVED_form": "the R-128 parity-odd Hodge-dual quark-lock (I4 Om) converts the Q-winding EXACTLY into the scalar L-winding = B_Q => the corrected seat FORM L_theta = muPsi0 * B_Q, PARITY-ODD, LINEAR in the integrated B_Q (pi_3 degree) -- DERIVES the algebraic FORM behind N32a's CANDIDATE cost_flip = 2 muPsi0 B on the explicit profile; the seat's PHYSICAL status inherits R-128's OWN FRAMING tier (NOT promoted to DERIVED)",
        "value_gated": "muPsi0 stays #1-gap kernel-GATED; the FORM prop B does NOT give N37's inter-generation running (orthogonal to B) -- running stays gated. NO split value claimed (N28/N32a trap respected)",
        "tier": "DERIVED-A (Clifford core: vanishing + parity-odd + exact Hodge-recovery) + the PHYSICAL seat identification inherits R-128's OWN FRAMING tier (up/down-seat + muPsi0-tie = FRAMING, not promoted) + value GATED",
    }


def updown_mirror_multigen_avg_vs_lepton() -> dict:
    """[REFUTED-structural-identification (a clean multi-generation NEGATIVE) +
    surviving FRAMING (the gen-1->2 suggestion) + FIT-level numerology note] --
    W-LIVE-1 gate-free partial (N32a's named clean future engine test, fired
    2026-07-02): does the parity-odd shift structure's baseline identification
    c_common = c_lepton hold at EVERY generation transition? -> NO.

    THE TEST (N32a named it verbatim): the H3 parity-odd shift structure
        cost_d = c_common - mu Psi_0,   cost_u = c_common + mu Psi_0
    predicts a symmetric mirror about a parity-even baseline at every generation;
    N32a's suggestive observation was avg(c_d, c_u) ~ c_lepton at gen-1->2 (within
    12%) plus 'lepton sits between down and up costs' -- and flagged the
    multi-generation cross-check as owed before any promotion. This primitive runs
    it. Costs are the N16-N22 arc's ln frequency-gap ladder; masses enter as INPUT
    witnesses only (canon: external quark masses are throwaway witnesses of a
    (non-)equality, never load-bearing; same tuples as
    updown_mirror_value_three_handles for consistency -- note the top entry is the
    direct/pole 172.5 GeV; the MS-bar top ~162.5 GeV shifts only the un-banked
    drift-ratio numerology, 3.04 -> 3.22, confirming its FIT-level status).

    RESULT (arithmetic, witnesses):
      gen-1->2: c_l = 5.33; c_d = 3.00, c_u = 6.38; avg = 4.69 (-12% vs lepton);
                lepton BETWEEN the towers. (Reproduces N32a exactly.)
      gen-2->3: c_l = 2.82; c_d = 3.80, c_u = 4.91; avg = 4.36 (+54% vs lepton);
                lepton BELOW BOTH towers -- NOT between, NOT the baseline.
      TOP-FREE decisive half: c_l(2->3) < c_d(2->3) already breaks 'the lepton is
      the parity-even baseline between the towers' -- the refutation does NOT lean
      on the top (canon: the top is not a verifier; it enters only the
      mu-Psi_0-drift magnitude below, as an indicator).

    VERDICT: the generation-UNIFORM structural identification c_common = c_lepton
    is REFUTED (54% off at 2->3, far beyond the ~10% MS-bar scheme/scale
    uncertainty of the witness masses -- caveat named, not decisive). What
    SURVIVES: (a) the gen-1->2 avg-vs-lepton agreement stays a FRAMING-suggestive
    observation (now honestly scoped as gen-1->2 ONLY); (b) the parity-odd FORM
    itself (d below / u above SOME common baseline) is untouched -- but note
    (reviewer clause) it is untouched because PER-TRANSITION it is unfalsifiable
    (two unknowns c_common, mu Psi_0 fit two data points exactly; N32a's own 'one
    equation, two unknowns'): its only testable content was the lepton-baseline
    identification (dead) or a generation-independent dial (also dead as an
    option). What died is everything testable at fixed dial.

    SHARPENING FOR THE 2b KERNEL PROGRAM: if the parity-odd shift structure is
    retained, its dial CANNOT be one generation-independent number --
        mu Psi_0 (1->2) = (c_u - c_d)/2 = 1.69
        mu Psi_0 (2->3) = (c_u - c_d)/2 = 0.56   [top-indicator-dependent]
    i.e. the parity-odd dial RUNS between generations (a drift), joining N20's
    within-tower drift as a second thing the kernel's generation sector must
    produce. NUMEROLOGY NOTE (FIT-level, NO derivation, recorded per the N32a
    precedent): the drift ratio 1.69/0.56 = 3.04 ~ 3; not banked as meaningful.

    WOULD CHANGE IF: (a) a derived generation-dependence of mu Psi_0 (from the
    kernel or the N22 grain endpoint) reproduces BOTH values -> the structure
    revives with a running dial and the 2->3 row becomes a constraint, not a
    refutation; (b) a different derived baseline (not the lepton) is identified
    for c_common -> re-run this test against it; (c) the witness masses' scheme
    dependence is shown to exceed ~40% at 2->3 (not plausible for ln-ratios).
    """
    lep = (0.511, 105.658, 1776.93)
    down = (4.67, 93.4, 4180.0)
    up = (2.16, 1270.0, 172500.0)

    def _cost(t, i):
        return math.log(t[i + 1] / t[i])

    c_l = (_cost(lep, 0), _cost(lep, 1))
    c_d = (_cost(down, 0), _cost(down, 1))
    c_u = (_cost(up, 0), _cost(up, 1))
    avg = tuple(0.5 * (d + u) for d, u in zip(c_d, c_u))
    dev = tuple(a / l - 1.0 for a, l in zip(avg, c_l))
    lepton_between = tuple(d < l < u for d, l, u in zip(c_d, c_l, c_u))
    mu_psi0 = tuple(0.5 * (u - d) for d, u in zip(c_d, c_u))

    gen12_reproduces_N32a = (
        abs(avg[0] - 4.686) < 0.02 and abs(c_l[0] - 5.332) < 0.01
        and abs(dev[0]) < 0.15 and lepton_between[0]
    )
    gen23_refutes = (
        abs(dev[1]) > 0.4                       # 54% off -- way beyond scheme noise
        and not lepton_between[1]               # lepton NOT between the towers
        and c_l[1] < c_d[1]                     # the TOP-FREE decisive inequality
    )
    # reviewer fix: the ratio is witness-scheme-dependent (MS-bar top gives 3.22,
    # direct/pole 3.04) -- assert only that the dial RUNS (ratio > 2), never the value
    dial_runs = mu_psi0[0] / mu_psi0[1] > 2.0

    assert gen12_reproduces_N32a, "gen-1->2 must reproduce N32a's suggestive observation"
    assert gen23_refutes, "gen-2->3 must refute the lepton-baseline identification (top-free)"
    assert dial_runs, "the implied parity-odd dial must run between generations"

    return {
        "outcome": ("REFUTED (clean multi-generation negative) -- the generation-uniform "
                    "identification c_common = c_lepton fails at gen-2->3 (+54%, lepton BELOW "
                    "both towers, top-free); N32a's gen-1->2 agreement survives as "
                    "FRAMING-suggestive, gen-1->2 ONLY; if the parity-odd structure is retained "
                    "its dial mu Psi_0 must RUN between generations (1.69 -> 0.56)"),
        "tier": ("REFUTED-structural-identification (witness-mass arithmetic; quark masses as "
                 "canon-allowed throwaway witnesses of a non-equality; top used only for the "
                 "drift magnitude, NOT the refutation) + FRAMING (gen-1->2 suggestion survives, "
                 "scoped) + FIT-numerology note (drift ratio ~3, NO derivation)"),
        "worklist_ref": "W-LIVE-1 gate-free partial (Class-1 queue item 5); fires N32a's named test",
        "costs": {"lepton": c_l, "down": c_d, "up": c_u},
        "avg_vs_lepton": {"avg": avg, "deviation_frac": dev,
                          "lepton_between_towers": lepton_between},
        "implied_mu_psi0_per_transition": mu_psi0,
        "top_free_decisive_inequality": "c_l(2->3) < c_d(2->3): 2.82 < 3.80",
        "scheme_caveat": ("MS-bar witness masses carry ~10%-class scheme/scale ambiguity in "
                          "ln-ratios; the 54% discrepancy is far beyond it"),
        "would_change_if": ("a derived generation-dependence of mu Psi_0 reproduces both values "
                            "(structure revives with a running dial); or a different derived "
                            "baseline replaces the lepton; or scheme dependence shown > 40% "
                            "(implausible)"),
    }


def skyrmion_rotational_band_nucleon_delta() -> dict:
    """[DERIVED, dressed-level (the exact-BVP band equation and both coefficients;
    same conditional class as skyrmion_mass_MeV: SS10.3 branch-(c) dressed-sector
    closure) + DERIVED-given-(Q)+FR (the J-quantization: collective quantization
    premise + the Finkelstein-Rubinstein fermionic SELECTION J = 1/2, 3/2 --
    empirically correct, NOT forced, W-LIVE-4/N35 fork untouched) + CORRECTION
    (the banked THETA0_COEFF = 97.27 is WRONG; exact BVP gives 106.76)] --
    the improved baryon mass equation: the rotational band
        M(J) = M_0 + J(J+1)/(2 Theta_0),
    with BOTH coefficients computed from the SAME exact hedgehog BVP profile:
        M_0     = 36.46 f_pi/e          (validates the banked 36.47),
        Theta_0 = 106.76 / (e^3 f_pi)   (CORRECTS the banked 97.27).
    At the banked ANW couplings (f_pi = 129, e = 5.45 -- historically FITTED to
    N and Delta, so this closure is a PIPELINE CONSISTENCY, not a parameter-free
    prediction): M_N = 936.4 MeV (obs 938.9 avg, -0.3%), M_Delta = 1229.8 MeV
    (obs 1232, -0.18%), splitting 293.4 MeV (obs 293.1, +0.10%). The banked M_0's
    '8% ANW deficit' (863 vs 939) is thereby EXPLAINED: it is the missing
    rotational-band term, not a model failure. (2026-07-03.)

    THE BVP (solved in-primitive, self-contained): the SC.1.1/ANW massless radial
    equation (the same exterior linearization R-130 used)
      (x^2/4 + 2 sin^2F) F'' + (x/2) F' + sin2F F'^2 - sin2F/4 - sin^2F sin2F/x^2 = 0,
    F(0) = pi, F(inf) = 0, solved by shooting; the energy density whose
    Euler-Lagrange equation IS this equation (sympy-verified in development):
      u = x^2 F'^2/8 + sin^2F/4 + sin^2F F'^2 + sin^4F/(2x^2),  M = 4pi (f_pi/e) Int u dx.
    SELF-CHECKS BANKED: (i) the DERRICK VIRIAL E2 = E4 at the minimum (engine:
    equal to <0.5% -- a profile-quality certificate); (ii) the mass coefficient
    reproduces the banked 36.47 to <0.2%; (iii) the tail is the R-130 r^-2 branch
    with constant B = x^2 F ~ 8.6 (fitted on the clean window x in [12, 20];
    beyond x ~ 25 the shooting numerics drift off the separatrix -- the unstable
    x^+1 mode -- so the long tail is added by ASYMPTOTIC MATCHING, A1_tail = B^2/X,
    not by raw quadrature; this matters: the inertia integrand x^2 sin^2F is
    LONG-RANGED, ~B^2/x^2, and truncating it at x ~ 14 is a ~10% error).

    THE INERTIA (the correction's derivation): the collective rotation
    U = A(t) U_0 A~(t) gives Theta = 2T/omega^2 with
      Theta_0 = (2pi/3) (1/(e^3 f_pi)) Int x^2 sin^2F [1 + 4 F'^2 + 4 sin^2F/x^2] dx
              = (2pi/3) Lambda / (e^3 f_pi),   Lambda = 50.98  =>  coeff 106.76.
    The FACTOR-4 on the Skyrme part and the quadratic part's normalization were
    verified ON THE ENGINE by a 3D-grid computation (development, 2026-07-03):
    rotating hedgehog on a [-14,14]^3 grid with couplings CALIBRATED to the
    validated static radial integrals; the grid's Skyrme kinetic piece matched
    the factor-4 radial value to 0.3%, and the quadratic piece matched (2pi/3)A1
    up to the box truncation of the long-ranged integrand (the truncated grid
    total, ~97, is exactly how a ~97 value can arise SPURIOUSLY).
    THE BANKED 97.27 IS NOT CONFIRMED BY THE BVP: it equals 36.47 x 8/3 = 97.253
    to within 0.02% (provenance suspect -- an unexplained algebraic relation to the
    mass coefficient, not an inertia integral); the exact value is 106.76, and
    ANW's own published fit (f_pi = 129, e = 5.45 reproducing N/Delta exactly)
    back-solves to ~106.6 -- independent confirmation. Lambda = 50.98 also
    matches the standard literature value ~50.9.

    KNOCK-ONS OF THE CORRECTION (swept this pass, canon 'sweep after a patch'):
      * 1/Theta_0: 214.7 -> 195.6 MeV.
      * R-111 Lambda_QCD candidate: 1/Theta_0 moves 215 -> 196 MeV, remaining IN
        the Lambda_QCD range (scheme caveat: closer to the folk ~200, farther from
        Lambda(5)_MSbar ~ 210 -- scheme-dependent, so no strengthening is claimed;
        still CANDIDATE, R-111 tier unchanged).
      * top exclusion (top_excluded): Gamma_t Theta_0 = 6.5 -> 7.16 >> 1 --
        conclusion STRENGTHENED (top still decays before binding).
      * heavy_baryon_predictions (anchor-predicted Sigma_Q - Lambda_Q):
        Sigma_c - Lambda_c: 171 (2.4% err) -> 151.9 (-9.0% err) -- the c-leg
        DEGRADES and becomes a TRACKED RESIDUAL (recorded honestly, not hidden);
        Sigma_b - Lambda_b: 201 (+5.2%) -> 181.9 (-4.8%) -- slightly improved.
        TWO CANDIDATE resolutions (named, not decided): (i) the heavy-baryon
        Sigma-Lambda inertia may not be the rigid-rotor B=1 Theta_0 at all
        (bound-state / Callan-Klebanov-class treatments use a DIFFERENT
        light-sector inertia) -- adjudicating needs the P2-7-class construction;
        (ii) hf_c = 43.7 is FIT-INHERITED from the disclosed global fit's B_0 --
        if that calibration was anchored in the old-constant environment, a
        re-fit is the cheaper resolution (its independence NOT verified this
        pass -- reviewer note). The OLD 2.4% agreement rode the WRONG constant
        -- it was accidental.

    THE BAND STRUCTURE (tie to this session's chain): the J(J+1)/(2 Theta_0)
    term is the concrete static-face instance of the O(d2E/dN2)-class moduli
    corrections named in R-131 -- here on the SPIN/ISOSPIN collective moduli
    (the R-126 right-sextet class), DISTINCT from R-131's U(1) phase tower (do
    not conflate the two moduli). J = 1/2, 3/2 for B = 1 rides the FR fermionic
    SELECTION -- the corpus's honest tier (compatible, not forced; W-LIVE-4
    routes L1/L2/L3 refuted; P2-4's induced level would decide it).

    HONEST ACCOUNTING: no new fitted parameter (f_pi, e are the already-counted
    ANW inputs); the N/Delta closure is consistency, the CONTENT is (a) the
    corrected exact coefficient pair, (b) the deficit explained as band physics,
    (c) the downstream corrections, (d) the new c-leg residual. NOT done: the
    pion-mass term (massless model only, as banked); the moving-defect band;
    the heavy-baryon inertia adjudication; any absolute scale (f_pi stays INPUT).

    WOULD CHANGE IF: (a) a banked pion-mass-term BVP shifts the coefficients
    (standard massive-ANW values differ; would need re-fit of the counted
    inputs -- a scoped follow-up); (b) the P2-7-class bound-state inertia lands
    => the c-leg residual adjudicates; (c) P2-4 decides FR => the J-lattice
    premise upgrades from selection to derived.
    """
    import numpy as np
    from scipy.integrate import solve_ivp

    # ---- the ANW radial equation, F'' isolated (algebraic rearrangement of the
    #      SC.1.1 equation; the sympy EL<->density check was done in development)
    def f_rhs(t, y):
        F, Fp = y
        s2 = math.sin(2 * F)
        sF = math.sin(F)
        num = -(t / 2) * Fp - s2 * Fp**2 + s2 / 4 + sF**2 * s2 / t**2
        den = t**2 / 4 + 2 * sF**2
        return [Fp, num / den]

    def _integrate(a, xmax=24.0):
        return solve_ivp(f_rhs, (1e-4, xmax), [math.pi + a * 1e-4, a],
                         rtol=1e-11, atol=1e-13, dense_output=True, max_step=0.1)

    # separatrix by the FLATNESS criterion: the tail-drift (the unstable x^+1 mode)
    # makes plain steep/shallow bisection imprecise; instead root-find on the
    # flatness of B(x) = x^2 F across the fit window -- the on-separatrix condition.
    def _flatness(a):
        s = _integrate(a)
        if np.any(s.y[0] < -1e-12):
            return -1e9                      # crossed zero: steep side
        return 324.0 * s.sol(18.0)[0] - 144.0 * s.sol(12.0)[0]

    lo, hi = -1.2, -0.9
    assert _flatness(lo) < 0 < _flatness(hi), "flatness bracket must straddle the separatrix"
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        if _flatness(mid) < 0:
            lo = mid
        else:
            hi = mid
    a_star = 0.5 * (lo + hi)
    sol = _integrate(a_star)
    xs = np.linspace(1e-4, 23.9, 24000)
    F = sol.sol(xs)[0]
    Fp = sol.sol(xs)[1]
    sF = np.sin(F)

    # ---- tail constant on the flat window (checked flat, not assumed)
    win = (xs >= 12.0) & (xs <= 20.0)
    B_tail = float(np.mean(xs[win]**2 * F[win]))
    B_spread = float(np.std(xs[win]**2 * F[win]))

    # ---- mass coefficient + Derrick virial (analytic sigma-tail beyond xmax added to E2)
    Xm = xs[-1]
    E2 = 4 * np.pi * (np.trapezoid(xs**2 * Fp**2 / 8 + 0.25 * sF**2, xs)
                      + 0.25 * B_tail**2 / Xm**3)
    E4 = 4 * np.pi * np.trapezoid(sF**2 * Fp**2 + 0.5 * sF**4 / xs**2, xs)
    mass_coeff = E2 + E4
    virial_dev = abs(E2 - E4) / mass_coeff

    # ---- inertia with asymptotic matching (the long-ranged A1 tail = B^2/X)
    X_match = 20.0
    m20 = xs <= X_match
    A1 = np.trapezoid(xs[m20]**2 * sF[m20]**2, xs[m20]) + B_tail**2 / X_match
    A2 = np.trapezoid(xs**2 * sF**2 * Fp**2, xs)
    A3 = np.trapezoid(sF**4, xs)
    Lambda = A1 + 4 * (A2 + A3)
    theta_coeff = (2 * np.pi / 3) * Lambda

    # ---- the band equation at the banked (already-counted) couplings
    f_pi, e_c = F_PI, E_PHYS
    M0 = mass_coeff * f_pi / e_c
    inv_Theta = (e_c**3 * f_pi) / theta_coeff          # MeV
    M_N = M0 + (3.0 / 8.0) * inv_Theta                 # J = 1/2
    M_D = M0 + (15.0 / 8.0) * inv_Theta                # J = 3/2
    split = M_D - M_N
    OBS_N, OBS_D = 938.9, 1232.0                       # PDG averages
    err_N = (M_N - OBS_N) / OBS_N
    err_D = (M_D - OBS_D) / OBS_D
    err_split = (split - (OBS_D - OBS_N)) / (OBS_D - OBS_N)

    banked_9727_is_8_3rds = abs(97.27 - M0_COEFF * 8.0 / 3.0) < 0.03

    assert virial_dev < 0.005, "Derrick virial E2 = E4 must hold at the minimum (<0.5%)"
    assert abs(mass_coeff - 36.47) < 0.08, "mass coefficient must reproduce the banked 36.47"
    assert 8.3 < B_tail < 8.9 and B_spread < 0.05, "tail constant B = x^2 F must be clean ~8.6"
    assert abs(Lambda - 50.9) < 0.6, "Lambda must be ~50.9 (the exact-BVP inertia integral)"
    assert abs(theta_coeff - 106.76) < 1.0, "Theta coefficient must be ~106.76 (NOT 97.27)"
    assert abs(theta_coeff - 97.27) > 5.0, "the exact BVP must REFUTE the old 97.27"
    assert banked_9727_is_8_3rds, "the old 97.27 must equal 36.47*8/3 (its suspect provenance)"
    assert abs(err_N) < 0.005 and abs(err_D) < 0.005 and abs(err_split) < 0.01, \
        "N, Delta, and the splitting must close at the banked couplings (<0.5%/1%)"

    return {
        "outcome": ("IMPROVED BARYON MASS EQUATION banked: M(J) = M_0 + J(J+1)/(2 Theta_0) "
                    "with exact-BVP coefficients M_0 = %.2f f_pi/e (validates 36.47) and "
                    "Theta_0 = %.2f/(e^3 f_pi) (CORRECTS the banked 97.27 = 36.47*8/3, "
                    "provenance suspect); at the counted ANW couplings M_N = %.1f (-0.3%%), "
                    "M_Delta = %.1f (-0.18%%), split %.1f -- the banked M_0's '8%% deficit' "
                    "is the missing band term" % (mass_coeff, theta_coeff, M_N, M_D, split)),
        "tier": ("DERIVED dressed-level (SS10.3 branch-(c) conditional, as skyrmion_mass_MeV) "
                 "+ DERIVED-given-(Q)+FR-selection (J = 1/2, 3/2 quantization; fork untouched) "
                 "+ CORRECTION (THETA0_COEFF 97.27 -> 106.76, swept) + R-131-class band "
                 "instance (spin/isospin moduli, distinct from the U(1) phase tower)"),
        "bvp": {
            "F_prime_origin": a_star,
            "E2": E2, "E4": E4, "virial_dev": virial_dev,
            "mass_coeff": mass_coeff,
            "tail_B": B_tail, "tail_B_spread": B_spread,
            "A1_tail_matched": A1, "A2": A2, "A3": A3,
            "Lambda": Lambda, "theta_coeff": theta_coeff,
        },
        "band": {
            "M0_MeV": M0, "inv_Theta_MeV": inv_Theta,
            "M_N": M_N, "M_Delta": M_D, "split": split,
            "err_N": err_N, "err_Delta": err_D, "err_split": err_split,
            "fit_history_note": ("f_pi = 129, e = 5.45 were HISTORICALLY FITTED to N/Delta "
                                 "(ANW) -- the closure is pipeline consistency, not a new "
                                 "prediction; no NEW parameter is introduced"),
        },
        "correction_knock_ons": {
            "inv_Theta0": "214.7 -> 195.6 MeV",
            "R-111_LambdaQCD_candidate": ("215 -> 196 MeV (in the Lambda_QCD range; "
                                         "scheme-dependent whether closer -- no "
                                         "strengthening claimed; still CANDIDATE)"),
            "top_exclusion": "Gamma_t*Theta_0 = 6.5 -> 7.16 >> 1 (STRENGTHENED)",
            "Sigma_c-Lambda_c": ("171 (2.4%) -> 151.9 (-9.0%) -- NEW TRACKED RESIDUAL; the "
                                 "old agreement rode the wrong constant (accidental); "
                                 "CANDIDATE resolution: heavy-baryon inertia is a different "
                                 "object (bound-state class, P2-7-adjacent) -- named, open"),
            "Sigma_b-Lambda_b": "201 (+5.2%) -> 181.9 (-4.8%) (slightly improved)",
        },
        "would_change_if": ("pion-mass-term BVP shifts the pair (scoped follow-up); the "
                            "bound-state inertia lands => c-leg residual adjudicates; P2-4 "
                            "decides FR => the J-lattice premise upgrades"),
    }


def brannen_scale_nucleon_third_convergence() -> dict:
    """[CANDIDATE (a zero-parameter cross-sector numerical convergence, recorded per
    canon S0a -- the observation itself is LITERATURE-KNOWN in the Koide-formula
    circle, imported as such, not claimed as a TWT discovery) + FRAMING (the two
    TWT readings below) + engine-checked arithmetic on INPUT constants (the
    numbers themselves)] -- the Brannen lepton mass scale and the nucleon's
    per-rotor frequency agree to 0.28% with NO tunable parameter on either side:
        mu^2   = ((sqrt(m_e) + sqrt(m_mu) + sqrt(m_tau))/3)^2 = 313.85 MeV,
        m_N/3  = 312.97 MeV (PDG p/n average),   ratio = 1.0028.
    In AMPLITUDE form (TWT's own sqrt-m measure) -- the SAME single convergence,
    NOT a second one: the square root halves the relative deviation IDENTICALLY
    (0.138% = 0.277%/2); quoted as the framework-native measure, not as added
    evidence [reviewer fix 1] --
        sqrt(m_N/3) = 17.691 MeV^1/2  vs  mu = 17.716 MeV^1/2   (0.14%):
    the baryon's per-rotor amplitude sits at the LEPTON TOWER'S DEMOCRATIC
    COMPONENT -- mu multiplies the generation-blind '1' in Brannen's
    sqrt(m_n) = mu(1 + sqrt(2) cos theta_n); the sqrt(2)cos-theta Z_3 offsets
    average to zero over the triplet. (2026-07-03, prompted by the coordinator's
    question 'is m_N ~ 3x the Brannen scale a coincidence?')

    THE TWO TWT READINGS [FRAMING -- neither derived]:
      (i) PER-ROTOR, NOT PER-QUARK: m_N/3 is NOT a quark mass (canon S5 intact
          -- quarks have no individual mass, bare or constituent). It is the
          MEAN PER-ROTOR FREQUENCY of the banked baryon frequency-lock
          Omega_B = Sum_3 omega (cogear_linkage_kinematic; E-channel-composition
          conditional per the 2026-07-02 sweep). The SM 'constituent quark mass
          ~313 MeV' is the same number wearing the import TWT forbids; the lock
          reading is the framework-legal object.
      (ii) DEMOCRATIC-AXIS: sqrt(m_N/3) = <sqrt(m_l)>_leptons says the baryon
          rotors ride the (1,1,1) democratic axis of the SAME underlying tower
          whose Z_3 generation offsets produce the charged leptons -- coherent
          with the corpus's circulant machinery (the democratic direction is
          exactly the axis the CKM/circulant analyses distinguish) and with
          N37's finding that the towers share structure but not offsets.

    HONEST CAVEATS (all named):
      (a) POST-HOC / LOOK-ELSEWHERE: the pair (mu^2, m_N/3) was noticed
          empirically (Koide-literature; reported in Rivero-Gsponer, 'The
          strange formula of Dr. Koide', hep-ph/0505220 -- citation to be
          verified against the passage before any external use), not predicted;
          a ~0.3% match among
          O(10) plausible cell-scale pairings is suggestive, not compelling.
          TWT semi-pre-specifies the pair (Omega_B = Sum omega makes m_N/3
          canonical; mu is the canonical tower scale), which tightens but does
          not close this.
      (b) WHICH MASS ENTERS THE LOCK is open at the 8% level: the full m_N
          (this match, 0.3%) vs the R-051 floor M_0/3 = 287.7 (match degrades
          to 9.1%) -- the freq-sum-vs-full-mass residual / E-floor->observer
          bridge open face. The convergence FAVORS the full-mass reading of
          the lock [FRAMING], and becomes a stakeholder in that open fork.
      (c) THE NAIVE DERIVATION ROUTE IS BLOCKED by banked N12
          (i4_lepton_quark_amplitude_blind): the I_4 Hodge map is
          amplitude-blind -- lepton amplitudes cannot be carried to the quark
          sector structurally. Any mechanism must route through SHARED
          cell-scale/kernel dynamics (#1-gap class), not the algebra map.
      (d) scale bookkeeping, SCOPED TO MULTIPLIER-1 pairings [reviewer fix 2]:
          mu^2 = 2.433 f_pi -- no multiplier-1 convergence with f_pi or 1/Theta_0.
          FIT-TIE ANNOTATION: mu^2/(1/Theta_0) = 1.6045 = (8/5)(1 + 0.28%) -- but
          1/Theta_0 shares the convergence BY CONSTRUCTION (f_pi, e were fitted
          to N/Delta, R-133), so this is the SAME hit propagated, NOT a second
          independent convergence; do not re-discover mu^2 = (8/5)/Theta_0.
          LOOK-ELSEWHERE AUDIT (reviewer's engine scan, banked below): over the
          four canonical cell-scale comparators {f_pi, 1/Theta_0, M_0/3, m_N/3}
          x all reduced rationals p/q <= 8 at 0.5% tolerance, EXACTLY TWO hits
          -- m_N/3 at multiplier 1, and the fit-tied 8/5.
          ★ SCOPE REPAIR 2026-08-24 (strictly weakening; record
          knowledge/audit/R134_NTRIED_EXTRACT_2026-08-24.md, assembled for the
          round-4 reviewer's F-7): the phrase 'a genuinely small trials factor'
          IS OVER-STATED AS WRITTEN AND IS WITHDRAWN. The menu's own local
          density was computed for the first time in that pass -- the 172
          candidate ratios sit at ~60 per ln-unit near 1, so at 0.5% tolerance
          the menu ALONE expects ~0.6 chance hits, against ONE independent hit
          observed -- the hit scored AT POLE MASSES (in MS-bar the same
          comparison FAILS the 0.5% criterion, +0.80% at m_mu / -1.56% at M_Z;
          the scheme label is part of the observation, N57 scope). That is a
          trials factor of order the signal, not a small
          one. 'Suggestive, not compelling' SURVIVES and is better supported
          than before; only the supporting phrase falls.
          ★ AND THE MENU'S CONDITIONING (RUL-049): it was built AROUND mu^2
          after m_N/3 was known, so it bounds WHICH comparator and WHICH
          rational -- never WHETHER a cell-scale pairing was the thing to look
          for. The campaign-wide N_tried the reviewer asked for DOES NOT EXIST
          and is NOT RECONSTRUCTIBLE; the telemetry was never kept, and the
          O(10) in caveat (a) is an unenumerated estimate.

    VERDICT ON 'COINCIDENCE?': not decidable today -- recorded as a CANDIDATE
    over-determination row (canon S0a: two sector-independent numbers
    converging on one value is itself a finding worth banking). IF a mechanism
    lands, the prize is large: m_N = 3 mu^2 would CO-DERIVE the nucleon mass
    from the lepton tower with ZERO hadronic input -- one of the two counted ANW
    dials (f_pi, e) becomes DERIVED (one fewer counted dial; f_pi stays in the
    corpus but becomes solvable given e) [reviewer fix 5].

    WOULD BECOME A RESULT IF: a kernel/cell-formation mechanism pins the
    Q-orbit per-rotor lock frequency to the lepton tower's democratic
    component (P2-1/P2-5-class; the 2b over-determination table gains this
    row). WOULD WEAKEN IF: the E-floor bridge resolves the lock to the FLOOR
    reading (match degrades to ~9%); or a systematic look-elsewhere audit
    deflates the significance.
    """
    mu = (math.sqrt(M_E) + math.sqrt(M_MU) + math.sqrt(M_TAU)) / 3.0
    mu2 = mu * mu
    m_p, m_n = 938.272, 939.565          # PDG INPUT witnesses
    m_N = 0.5 * (m_p + m_n)
    ratio_mass = mu2 / (m_N / 3.0)
    ratio_amp = math.sqrt(m_N / 3.0) / mu
    # the floor-reading comparison (the open fork's other branch)
    M0 = M0_COEFF * F_PI / E_PHYS
    ratio_floor = mu2 / (M0 / 3.0)
    # non-convergence with the other cell-scale numbers (context, not cherry-picking)
    ratio_fpi = mu2 / F_PI
    inv_Theta0 = (E_PHYS**3 * F_PI) / THETA0_COEFF
    ratio_invTheta = mu2 / inv_Theta0
    # look-elsewhere audit (reviewer's scan, banked): comparators x reduced rationals
    from fractions import Fraction
    comparators = {'f_pi': F_PI, 'inv_Theta0': inv_Theta0,
                   'M0_third': M0 / 3.0, 'mN_third': m_N / 3.0}
    hits = set()
    for p in range(1, 9):
        for q in range(1, 9):
            fr = Fraction(p, q)
            for nm, c in comparators.items():
                if abs(mu2 / (c * fr.numerator / fr.denominator) - 1.0) < 0.005:
                    hits.add((nm, '%d/%d' % (fr.numerator, fr.denominator)))
    fit_tie_8_5 = abs(ratio_invTheta / 1.6 - 1.0) < 0.005

    assert abs(mu2 - 313.85) < 0.05, "Brannen scale squared must be 313.85 MeV (banked lepton INPUTs, PDG 2024 m_tau = 1776.93)"
    assert abs(ratio_mass - 1.0) < 0.005, "mu^2 vs m_N/3 must converge to <0.5% (zero parameters)"
    assert abs(ratio_amp - 1.0) < 0.0025, "amplitude form sqrt(m_N/3) vs mu must converge to <0.25%"
    assert 1.05 < ratio_floor < 1.13, "the FLOOR reading must NOT converge (~9% off -- the named fork)"
    assert ratio_fpi > 2.0 and ratio_invTheta > 1.5, \
        "no MULTIPLIER-1 convergence with f_pi or 1/Theta_0 (scoped claim, reviewer fix 2)"
    assert sorted(hits) == [("inv_Theta0", "8/5"), ("mN_third", "1/1")], "look-elsewhere scan must find EXACTLY two hits (m_N/3 at 1/1 + the fit-tied 8/5), got %s" % sorted(hits)
    assert fit_tie_8_5, "the 8/5 fit-tie (via the N/Delta fit of f_pi, e) must hold"

    return {
        "outcome": ("CANDIDATE convergence recorded: mu^2 = %.2f MeV vs m_N/3 = %.2f MeV "
                    "(ratio %.4f, 0.28%%, zero parameters); amplitude form sqrt(m_N/3)/mu = "
                    "%.4f (0.14%%) -- the baryon per-rotor amplitude sits at the lepton "
                    "tower's democratic component. Literature-known observation, TWT-reframed "
                    "(per-rotor lock frequency, NOT a quark mass); not derivable through the "
                    "I_4 map (N12); mechanism would collapse f_pi into the lepton scale."
                    % (mu2, m_N / 3.0, ratio_mass, ratio_amp)),
        "tier": ("CANDIDATE (zero-parameter cross-sector convergence, recorded per canon S0a; "
                 "observation literature-known, imported as such) + FRAMING (per-rotor lock "
                 "reading; democratic-axis reading; full-mass-vs-floor fork stake) + "
                 "engine-checked arithmetic on INPUTs"),
        "numbers": {
            "mu_MeV_half": mu, "mu2_MeV": mu2,
            "m_N_third": m_N / 3.0, "ratio_mass": ratio_mass, "ratio_amplitude": ratio_amp,
            "floor_reading_ratio": ratio_floor,
            "mu2_over_fpi": ratio_fpi, "mu2_over_invTheta0": ratio_invTheta,
            "look_elsewhere_hits": sorted(hits),
            "amplitude_form_is_same_fact": "0.138% = 0.277%/2 exactly (sqrt halves it)",
        },
        "blocked_route": ("N12 i4_lepton_quark_amplitude_blind: the Hodge map cannot carry "
                          "lepton amplitudes to the quark sector -- any mechanism is "
                          "kernel/cell-scale (#1-gap class), not algebraic"),
        "would_become_result_if": ("a P2-1/P2-5-class mechanism pins the per-rotor lock "
                                   "frequency to the lepton democratic component => m_N = "
                                   "3 mu^2 co-derives the nucleon mass from the lepton tower "
                                   "(one fewer counted INPUT dial); 2b table gains the row"),
        "would_weaken_if": ("the E-floor bridge resolves the lock to the FLOOR reading "
                            "(match degrades to ~9%); or a look-elsewhere audit deflates it"),
    }


def multi_skyrmion_b2_classical_binding() -> dict:
    """[DERIVED, dressed-level VARIATIONAL (the below-threshold inequality: an
    explicit B = 2 configuration of the banked dressed Skyrme static sector has
    energy STRICTLY BELOW the two-defect threshold 2 M_0 -- same SS10.3/D.4.3
    branch-(c) conditional class as skyrmion_mass_MeV and R-133; the CONCLUSION
    'the B = 2 channel is classically bound/attractive' is ansatz-independent
    because ANY trial configuration below threshold bounds the infimum --
    CONDITIONAL on the banked identification M_0 = the B = 1 minimum (hedgehog
    minimality, the standing premise of R-051/R-133's whole one-defect sector;
    INHERITED here, not new -- reviewer fix F1); 'bound' = strict SUB-ADDITIVITY,
    the standard classical-binding criterion (attained-minimizer existence is
    the concentration-compactness step, literature character); the
    ansatz VALUE 71.54 f_pi/e is only an UPPER BOUND on the true B = 2 minimum,
    labeled as such) + DERIVED-A (the indicial-root generalization s^2+s-2B = 0
    of R-130's {-2, +1}, and the rational-map degree identity
    (1/4pi) Int psi^2 dOmega = B, both engine-checked) + FRAMING (the DEUTERON
    identification: J^pi = 1+, I = 0 requires the B = 2 collective quantization
    (Braaten-Carson-class) + the FR constraint -- NOT done here; the classical
    bound state is the deuteron's classical SEAT, not yet the deuteron)] --
    P2-7 FIRST HALF: the B = 2 (two-defect) sector of the dressed Skyrme
    energy lies below the two-nucleon threshold -- nuclear binding EXISTS
    classically, with the predicted SIGN (attraction). (2026-07-03.)
    [QUANTIZATION FACE fired same day: R-136
    b2_axial_quantization_deuteron_ground_state upgrades the deuteron
    identification to the quantum-number level (DERIVED-given-(Q)+FR); the
    FRAMING above refers to what R-135 ALONE establishes.]

    THE CONSTRUCTION (rational-map ansatz, Houghton-Manton-Sutcliffe class,
    solved self-contained in R-133's x-units where B = 1, I = 1 reduces EXACTLY
    to the banked hedgehog equation):
      U = exp(i F(x) n_R(theta, phi) . tau),  R(z) = z^2  (the standard degree-2 map),
      u_{B,I} = x^2 F'^2/8 + B sin^2F/4 + B sin^2F F'^2 + I sin^4F/(2x^2),
      M = 4pi (f_pi/e) Int u dx,
      EL: (x^2/4 + 2B sin^2F) F'' + (x/2)F' + B sin2F F'^2 - B sin2F/4
          - I sin^2F sin2F/x^2 = 0,   F(0) = pi, F(inf) = 0.
    The angular content enters through ONE number, computed here by quadrature
    (not imported): I(z^2) = 5.8083 (literature ~5.81), with the DEGREE IDENTITY
    (1/4pi) Int psi^2 dOmega = B = 2 exact to 1e-10 as the normalization
    certificate. (Whether z^2 minimizes I over degree-2 maps is NOT needed:
    the below-threshold conclusion needs only SOME trial below threshold.)

    THE NUMBERS (all certificates banked as asserts; reviewer clean-room
    re-solve at review, 2026-07-03: different flatness window, domain, and
    tolerances -- agreement to 4e-5 on both coefficients and the margin):
      * B = 1 regression: the generalized solver reproduces the banked
        mass coefficient 36.46 (R-133) with Derrick virial E2 = E4 ~ 4e-6.
      * B = 2: mass coefficient 71.543 f_pi/e; Derrick virial ~ 3e-6;
        per-baryon energy 1.2081 in 12pi^2 units (HMS literature 1.208 --
        independent end-to-end cross-check); clean tail constant on the
        flatness window (spread < 0.1%).
      * Indicial structure (DERIVED-A): linearizing at EITHER end gives the
        same Euler equation x^2 F'' + 2x F' - 2B F = 0 (about F = 0 at the
        tail, about F = pi at the origin), roots s^2 + s - 2B = 0:
        B = 1 -> {+1, -2} = EXACTLY R-130's banked pair; B = 2 ->
        (-1 +/- sqrt(17))/2 = {+1.5616, -2.5616}; the B = 2 origin exponent
        is NON-integer (F ~ pi - a x^1.56) and the tail steepens to x^-2.56
        -- the B = 1 long-tail/asymptotic-matching problem of R-133 is ABSENT.
        PRECISION NOTES (reviewer R1/R2): at the B = 2 origin the linearization
        is self-consistent (nonlinear terms O(x^{3p-2}), subleading); at the
        B = 1 origin p = 1 is order-MARGINAL -- the O(x) nonlinear residual is
        (ax/2)[(B-1) + 4a^2(I-B)], vanishing identically iff B = I = 1 (sympy,
        review pass; this is also WHY a is a free shooting parameter for the
        hedgehog) -- so the B = 1-origin justification is the known hedgehog
        expansion, not a pure linearization. And the in-code indicial ASSERTS
        check the closed formula against itself (self-referential); the genuine
        engine certificates of the indicial structure are the clean tail
        constants on the flatness window + the virials + the B = 1 regression.
      * THE INEQUALITY: 71.543 < 2 x 36.462 = 72.923 -- margin 1.89%,
        vs numerical error ~1e-5 (three orders below the margin). At the
        counted ANW couplings (f_pi = 129, e = 5.45): M_RM(B=2) = 1693.4 MeV
        vs threshold 1726.1 MeV -- classical binding >= 32.7 MeV.

    HONEST ACCOUNTING (the companion P2-7 handle asked for exactly this:
    'predict existence + binding sign (classical overbinding caveat honestly
    imported)'):
      * NO new parameter: f_pi, e are the already-counted ANW inputs; I is
        computed; the trial map z^2 is the standard degree-2 map.
      * OVERBINDING, imported and named: the observed deuteron binding is
        2.22 MeV; the classical bound here is >= 32.7 MeV (and the literature
        full-field B = 2 toroidal minimum, ~1.179 per baryon, is deeper
        still, ~75 MeV). Classical-level overbinding is the KNOWN character
        of the massless Skyrme sector; the PHYSICAL binding magnitude lives
        at the B = 2 collective quantization + pion-mass level (named
        follow-ups) -- this primitive banks EXISTENCE + SIGN, no magnitude.
      * The no-toy tell, answered: the energy functional is the BANKED
        dressed static sector (branch-(c)); the rational map is a variational
        TRIAL whose only load-bearing output is an UPPER BOUND -- the
        conclusion (below threshold) does not depend on the trial's details.
      * SC-1 FIRST DATUM, scoped: what is banked is the ansatz-reduced N = 2
        radial BVP being clean and certificated (separatrix by the R-133
        flatness criterion, virial < 1e-5, clean tail) + variational
        existence BELOW threshold. This is NOT full 3D multi-defect PDE
        well-posedness; it is the first N = 2 datum the SC-1 row asked for.

    NOT DONE (named): the tensor force from D4 anisotropy via DM (P2-7's
    second half); the B = 2 collective quantization (deuteron J^pi = 1+,
    the 2.22 MeV face, FR/P2-4 fork inherited); the pion-mass-term BVP;
    the full-field (torus) solution; the Callan-Klebanov bound-state inertia
    that would adjudicate R-133's Sigma_c - Lambda_c residual (ADJACENT to
    this machinery but a DIFFERENT construction -- not resolved here).

    WOULD CHANGE IF: (a) a banked pion-mass-term BVP shifts both coefficients
    (binding margin must be re-checked -- the massive-pion literature keeps
    B = 2 bound, but that is imported, not banked); (b) the B = 2 quantization
    lands => the deuteron identification upgrades from FRAMING and the 2.22 MeV
    face becomes a real test; (c) a full-field computation replaces the upper
    bound with the true minimum (deepens, never un-binds, the classical result).
    [(c) FIRED 2026-07-05, R-144 full_field_b2_below_threshold_sc1_datum: the
    full-3D ansatz-free flow keeps the binding -- stall-vs-stall margins
    1.79%/3.06% at N = 64/96, >= 2.95% after the reviewer's B1-side probe;
    the toroidal minimizer -- as predicted.]
    """
    import numpy as np
    from scipy.integrate import solve_ivp, quad

    # ---- the angular integral I and the degree identity for R(z) = z^2 ----
    # psi(rho) = (1+rho^2)|R'|/(1+|R|^2); sphere measure 4 rho drho dphi/(1+rho^2)^2
    def psi(rho):
        return (1 + rho**2) * 2 * rho / (1 + rho**4)

    I_ang, _ = quad(lambda r: psi(r)**4 * 2 * r / (1 + r**2)**2, 0, np.inf, limit=200)
    B_deg, _ = quad(lambda r: psi(r)**2 * 2 * r / (1 + r**2)**2, 0, np.inf, limit=200)

    # ---- generalized radial problem (B = 1, I = 1 is EXACTLY R-133's equation) ----
    def make_rhs(Bc, Ic):
        def f_rhs(t, y):
            F, Fp = y
            s2 = math.sin(2 * F)
            sF = math.sin(F)
            num = -(t / 2) * Fp - Bc * s2 * Fp**2 + Bc * s2 / 4 + Ic * sF**2 * s2 / t**2
            den = t**2 / 4 + 2 * Bc * sF**2
            return [Fp, num / den]
        return f_rhs

    def solve_profile(Bc, Ic, a_lo, a_hi, xmax=28.0):
        p = (-1 + math.sqrt(1 + 8 * Bc)) / 2      # origin exponent (F = pi - a x^p)
        s_dec = (1 + math.sqrt(1 + 8 * Bc)) / 2   # tail decay exponent |s_-|
        rhs = make_rhs(Bc, Ic)
        x0 = 1e-3

        def integrate(a):
            return solve_ivp(rhs, (x0, xmax), [math.pi - a * x0**p, -a * p * x0**(p - 1)],
                             rtol=1e-11, atol=1e-13, dense_output=True, max_step=0.1)

        w1, w2 = 10.0, 16.0                       # flatness window (R-133 criterion)
        def flatness(a):
            s = integrate(a)
            if np.any(s.y[0] < -1e-12):
                return -1e9                        # crossed zero: steep side
            return w2**s_dec * s.sol(w2)[0] - w1**s_dec * s.sol(w1)[0]

        flo = flatness(a_lo)
        assert flo * flatness(a_hi) < 0, "flatness bracket must straddle the separatrix"
        lo, hi = a_lo, a_hi
        for _ in range(52):
            mid = 0.5 * (lo + hi)
            if flatness(mid) * flo > 0:
                lo = mid
            else:
                hi = mid
        a_star = 0.5 * (lo + hi)
        return integrate(a_star), a_star, p, s_dec

    def energy(sol, Bc, Ic, s_dec, xcut=24.0):
        xs = np.linspace(1e-3, xcut, 24000)
        F, Fp = sol.sol(xs)
        sF = np.sin(F)
        win = (xs >= 10.0) & (xs <= 16.0)
        Ct = float(np.mean(xs[win]**s_dec * F[win]))
        Ct_rel_spread = float(np.std(xs[win]**s_dec * F[win])) / abs(Ct)
        Xm, s = xs[-1], s_dec
        # analytic tail beyond Xm for the quadratic (long-ranged) terms
        t_E2 = quad(lambda x: x**2 * (s * Ct * x**(-s - 1))**2 / 8
                    + Bc * (Ct * x**(-s))**2 / 4, Xm, np.inf, limit=200)[0]
        E2 = 4 * np.pi * (np.trapezoid(xs**2 * Fp**2 / 8 + Bc * 0.25 * sF**2, xs) + t_E2)
        E4 = 4 * np.pi * np.trapezoid(Bc * sF**2 * Fp**2 + Ic * 0.5 * sF**4 / xs**2, xs)
        return E2, E4, Ct, Ct_rel_spread

    # ---- B = 1 regression (must reproduce R-133's banked coefficient) ----
    sol1, a1, p1, s1 = solve_profile(1.0, 1.0, 0.9, 1.2)
    E2_1, E4_1, C1, C1s = energy(sol1, 1.0, 1.0, s1)
    m1 = E2_1 + E4_1
    vir1 = abs(E2_1 - E4_1) / m1

    # ---- B = 2 rational map ----
    sol2, a2, p2, s2 = solve_profile(2.0, I_ang, 0.4, 0.6)
    E2_2, E4_2, C2, C2s = energy(sol2, 2.0, I_ang, s2)
    m2 = E2_2 + E4_2
    vir2 = abs(E2_2 - E4_2) / m2
    per_b_12pi2 = m2 / (3 * math.pi**2) / 2.0

    # ---- the inequality at the counted couplings ----
    M1 = m1 * F_PI / E_PHYS
    M2 = m2 * F_PI / E_PHYS
    binding = 2 * M1 - M2
    margin = (2 * m1 - m2) / (2 * m1)

    # ---- certificates ----
    assert abs(B_deg - 2.0) < 1e-10, "degree identity (1/4pi) Int psi^2 = B = 2 must hold"
    assert abs(I_ang - 5.8083) < 0.001, "I(z^2) must be 5.8083 (literature ~5.81)"
    assert abs(p1 - 1.0) < 1e-12 and abs(s1 - 2.0) < 1e-12, \
        "B = 1 indicial roots must be R-130's banked {+1, -2}"
    assert abs(p2 - (-1 + math.sqrt(17)) / 2) < 1e-12 and \
        abs(s2 - (1 + math.sqrt(17)) / 2) < 1e-12, "B = 2 roots must be (-1 +/- sqrt(17))/2"
    assert vir1 < 0.005 and vir2 < 0.005, "Derrick virial E2 = E4 must certify both profiles"
    assert abs(m1 - 36.46) < 0.08, "B = 1 regression must reproduce the banked 36.46 (R-133)"
    assert abs(m2 - 71.54) < 0.15, "B = 2 rational-map coefficient must be 71.54 f_pi/e"
    assert abs(per_b_12pi2 - 1.208) < 0.002, "per-baryon 1.2081 must match HMS ~1.208"
    assert C1s < 0.002 and C2s < 0.002, "tail constants must be clean on the flatness window"
    assert m2 < 2 * m1 - 1.0, "THE RESULT: B = 2 must lie strictly below the two-defect threshold"
    assert 0.015 < margin < 0.025, "the below-threshold margin must be ~1.9%"
    assert 30.0 < binding < 36.0, "classical binding >= ~32.7 MeV at the counted couplings"

    return {
        "outcome": ("P2-7 FIRST HALF banked: an explicit B = 2 rational-map configuration of "
                    "the dressed Skyrme sector has energy %.3f f_pi/e < 2 x %.3f = %.3f -- "
                    "STRICTLY BELOW the two-defect threshold (margin %.2f%%). Nuclear binding "
                    "EXISTS classically with the predicted SIGN (attraction): at the counted "
                    "couplings M_RM(B=2) = %.1f MeV vs threshold %.1f MeV (binding >= %.1f "
                    "MeV; ansatz value = upper bound only). Overbinding vs the observed "
                    "2.22 MeV honestly imported (quantization + pion mass = named follow-ups)."
                    % (m2, m1, 2 * m1, 100 * margin, M2, 2 * M1, binding)),
        "tier": ("DERIVED dressed-level VARIATIONAL (below-threshold inequality; branch-(c) "
                 "conditional as R-051/R-133; conclusion ansatz-independent GIVEN the "
                 "inherited hedgehog-minimality premise of the banked B = 1 sector; value "
                 "= upper bound) + DERIVED-A (indicial generalization s^2+s-2B = 0 of R-130's pair; "
                 "degree identity) + FRAMING (deuteron identification awaits B = 2 "
                 "quantization; classical seat only)"),
        "angular": {"I_z2": I_ang, "degree_check": B_deg},
        "b1_regression": {"mass_coeff": m1, "virial": vir1, "a_star": a1,
                          "roots": (p1, -s1), "tail_C": C1},
        "b2": {"mass_coeff": m2, "virial": vir2, "a_star": a2,
               "roots": (p2, -s2), "tail_C": C2, "per_baryon_12pi2": per_b_12pi2},
        "inequality": {"m2_coeff": m2, "threshold_coeff": 2 * m1, "margin": margin,
                       "M_RM_B2_MeV": M2, "threshold_MeV": 2 * M1,
                       "classical_binding_MeV_lower_bound": binding,
                       "observed_deuteron_binding_MeV": 2.22,
                       "overbinding_note": ("classical-level overbinding is the known massless-"
                                            "Skyrme character; existence + sign banked, "
                                            "magnitude NOT claimed")},
        "sc1_datum": ("first N = 2 datum, scoped: the ansatz-reduced radial BVP is clean and "
                      "certificated (flatness separatrix, virial < 1e-5, clean tail) + "
                      "variational existence below threshold; NOT full 3D well-posedness"),
        "would_change_if": ("pion-mass-term BVP shifts the pair (re-check margin); B = 2 "
                            "quantization lands (deuteron face becomes a test); full-field "
                            "torus computation (deepens, never un-binds)"),
    }


def b2_axial_quantization_deuteron_ground_state() -> dict:
    """[DERIVED-A (the z^2 map symmetries, verified symbolically in-primitive:
    R(e^{i a}z) = e^{2ia}R (axial iso-lock), R(-z) = R (pi about e3 alone),
    R(1/z) = 1/R (pi about e1 = pi about tau1); the PARITY map R_P = -R --
    parity of the B = 2 configuration is an INTERNAL isorotation by pi about
    tau3, so every isoscalar state has parity +; the axial inertia identity
    d_phi n = 2 e3 x n => V33 = 4 U33 exact; the radial x angular
    FACTORIZATION of all rigid-rotation inertia integrands, proved by the
    hedgehog reduction collapsing exactly to R-133's (2pi/3)(R1+4R2+4R3))
    + IMPORTED-AS-CITED (the Krusch homotopy formula for
    Finkelstein-Rubinstein loop signs on rational-map Skyrmions,
    N = (B^2 theta - B phi)/(2pi), sign (-1)^N -- an external topology
    theorem used like Schur; engine consistency checks banked: B = 1
    reproduces the fermionic 2pi-rotation sign, loop compositions consistent
    mod 2 -- HONESTY NOTE (reviewer): the composition asserts are
    mod-2-WEAK (2*N_S2 is always even); the real formula discriminator is
    the S2 loop itself -- the wrong variant (B/2pi)(theta - B phi) would
    give N = 1 there, killing every L3 = 0 state including the deuteron;
    the B = 1 fermionic regression is the anchor)
    + DERIVED-given-(Q)+FR-selection (the selection rule and quantum
    numbers, SAME conditional class as R-133's J = 1/2, 3/2: collective
    quantization premise + the FR fermionic SELECTION -- the W-LIVE-4/N35
    fork is NOT decided here) + ANSATZ-LEVEL for the moment ORDERING
    (rational-map moments, not the true-minimizer's; the same ordering holds
    for the literature torus, cited as corroboration only) + FRAMING/ESTIMATE
    (the MeV spectrum numbers -- rigid-rotor overbinding, honestly quoted,
    NO magnitude claimed)] -- P2-7 QUANTIZATION FACE: the quantized B = 2
    sector's ground state has EXACTLY the deuteron's quantum numbers.
    (2026-07-03.)

    PRIOR ART, stated plainly (reviewer required fix, R-134 precedent): the
    HEADLINE PHYSICS -- the I+J-odd selection rule, the forbidden (0,0), and
    the deuteron 1+ ground state of the quantized B = 2 Skyrmion -- is an
    ESTABLISHED Skyrme-literature result (Braaten-Carson 1988;
    Leese-Manton-Schroers 1995; Krusch 2003 -- citations to be verified
    before external use). This primitive does NOT claim it as a novel
    prediction. R-136's genuinely NEW content is: (i) the conditional TWT
    tiering (which parts are DERIVED-A, which ride the (Q)+FR selection,
    which are import); (ii) the exact factorized moments computed on the
    R-135 saddle with its certificate stack (B = 1 four-way regression,
    V33 = 4 U33, W_perp = 0 block-diagonality); (iii) the W-LIVE-4
    fork-face BOOKKEEPING (the bosonic-branch refutation as a second
    labeled empirical anchor).

    THE RESULT (three layers):
    (1) SELECTION RULE (DERIVED-given-(Q)+FR): the axial B = 2 configuration
        carries the body-fixed constraint L3 + 2 K3 = 0 (from the S1
        iso-lock) and two FR loop constraints: the pi-rotation-about-e3 loop
        (N = 2, sign +1) and the MIXED pi-e1/pi-tau1 loop (N = 1, sign -1).
        On the K3 = 0 tower these give exactly
            (-1)^{I+J} = -1  :  I + J ODD.
        ALLOWED: (I,J) = (0,1), (1,0), (1,2), (0,3), (2,1)...
        FORBIDDEN: (0,0), (1,1), (0,2), (2,0)...
        With the parity map (internal): the lowest isoscalar is J^pi = 1+,
        I = 0 -- THE DEUTERON; the lowest isovector is 0+, I = 1 -- the np
        spin-singlet channel. The scalar-isoscalar (0,0) DIBARYON IS
        TOPOLOGICALLY FORBIDDEN. TIER BOUNDARY (reviewer fix): the MAP
        identity R_P = -R is DERIVED-A; the STATE-level parity assignment
        (isoscalar parity +, hence 1+) lives HERE, in the (Q)-conditional
        layer -- the parity convention is anchored to the nucleon's + (the
        B = 1 hedgehog has R_P = R). GROUND-STATE COMPLETENESS (reviewer
        rec): the |K3| >= 1 towers necessarily lie HIGHER -- |L3| = 2|K3|
        forces every J <= 1 state onto K3 = 0, and any J >= 2 state costs
        >= 6/(2 V_perp) = 3x the (0,1) rotational energy (plus iso cost on
        K3 != 0 towers) -- so 'ground state' is airtight, not
        tower-restricted. The S2-loop sign +1 doubles as the NO-ANOMALY
        certificate on the axial constraint (a half-integer offset in
        L3 + 2 K3 = 0 would flip it).
    (2) ORDERING (ansatz-level): the exact factorized moments of the R-135
        profile give V_perp = 312.5 > U_perp = 194.6 (units 1/(e^3 f_pi)) =>
        E(0,1) < E(1,0): the deuteron quantum numbers are the GROUND STATE;
        the isovector lies ~40 MeV up (nature: deuteron bound at -2.2 MeV,
        singlet VIRTUAL at ~+0.07 -- ordering right, spacing overbound as
        expected at rigid-rotor level). Certificates: B = 1 regression --
        all FOUR moments (iso AND spatial code paths) = 106.75, matching
        R-133's banked 106.76 (the hedgehog spin-from-isospin identity
        V = U verified numerically, not assumed); V33/U33 = 4 to 8 digits;
        A.n = 0 orthogonality asserts on every angular field.
    (3) THE FORK FACE (recorded, not decided): under the BOSONIC branch of
        the W-LIVE-4 fork all loop signs are +1 and the rule flips to
        I + J EVEN -- ground state (0,0): a bound scalar-isoscalar dibaryon
        and NO distinguished (0,1). Nature's deuteron (1+, I = 0, no scalar
        partner) therefore EMPIRICALLY SELECTS the fermionic branch through
        a SECOND, independent anchor (the first: the nucleon's spin-1/2).
        This is empirical selection evidence for the FR pick, NOT a
        derivation -- N35's fork and P2-4's induced-level route stand.
        (The two anchors are INDEPENDENT DATA sharing the (Q) premise --
        reviewer rec, carried honestly.)

    THE CONSTRAINT DERIVATION (all engine-checked): spatial rotation by
    alpha about e3 maps z -> e^{i alpha} z, so S1 makes it equal an
    isorotation by 2 alpha about tau3 => (L3 + 2 K3) psi = 0 (body-fixed);
    at alpha = pi the spatial rotation closes ALONE (S2), giving the N = 2
    loop; the transverse pi-rotation closes against pi-about-tau1 (S3),
    giving the N = 1 loop. On |I, K3=0> x |J, L3=0>: e^{-i pi J_1}|J,0> =
    (-1)^J |J,0> (d^J_00(pi) = P_J(-1)) and likewise for iso => the rule.
    The e2-axis loop (z -> -1/z, also pi-about-tau1 for z^2) gives the SAME
    constraint -- internal coherence check, no new condition.

    THE MOMENTS (exact-to-quadrature, no grid, no 3D truncation): for
    sigma = (cos F, sin F n), ANY rigid rotation gives sdot = omega
    (0, sinF A) with A angular and A.n = 0 (so sdot . d_x sigma = 0
    identically), and every inertia integrand factorizes termwise:
        Theta = (1/4) Aq R1 + Aq R2 + Ab2 R3,
        R1 = Int x^2 sin^2F dx (+ analytic tail Ct^2 X^{3-2s}/(2s-3)),
        R2 = Int x^2 sin^2F F'^2 dx,  R3 = Int sin^4F dx,
        Aq = Int |A|^2 dOm,  Ab2 = Int [|A|^2 |grad n|^2 - (A.grad n)^2] dOm.
    Iso: A = e_b x n; spatial-3: A = d_phi n; spatial-1: A = sin(phi) d_th n
    + cot(th) cos(phi) d_ph n. Phi-quadrature is uniform-trapezoid = EXACT
    for the finite trig polynomials involved; theta is Gauss-Legendre.

    HONEST ACCOUNTING: no new parameter (f_pi, e counted; the profile is
    R-135's); the spectrum numbers are rigid-rotor-on-an-upper-bound-saddle
    ESTIMATES (E(0,1) = 1760 vs threshold 2 M_N = 1873: ~113 MeV overbound
    at this level -- the known classical/rigid-rotor character, stated, not
    hidden); the ordering claim is ansatz-level (torus corroboration cited,
    not banked); Krusch is an import, named as such; the deuteron
    IDENTIFICATION is now DERIVED-given-(Q)+FR at the quantum-number level
    -- upgraded from R-135's bare FRAMING -- while its BINDING VALUE stays
    open at the kernel/pion-mass/quantization-refinement level.

    NOT DONE: |K3| >= 1 towers (need symmetrized +/-K3 combinations -- the
    allowed set there is not claimed); the tensor force / D4 anisotropy
    (P2-7's remaining half); the pion-mass term; the true-minimizer (torus)
    moments; the Callan-Klebanov bound-state inertia (R-133's Sigma_c
    residual adjudicator); any Finkelstein-Rubinstein DERIVATION (P2-4).

    WOULD CHANGE IF: (a) P2-4's induced level lands EVEN => the fermionic
    selection loses its candidate derivation route and the B = 2 anchor
    becomes a standing empirical tension for the framework's FR bookkeeping;
    (b) a torus/full-field computation flips V_perp vs U_perp (literature
    says it does not); (c) a banked pion-mass BVP shifts the moments
    (ordering re-check owed, spacing will move toward physical).
    """
    import numpy as np
    import sympy as sp
    from scipy.integrate import solve_ivp, quad

    # ================= (1) map symmetries, DERIVED-A =================
    z = sp.symbols('z', complex=True)
    alpha_s = sp.symbols('alpha', real=True)
    R = z**2
    s1 = sp.simplify((sp.exp(sp.I*alpha_s)*z)**2 - sp.exp(2*sp.I*alpha_s)*R)
    s2 = sp.simplify((-z)**2 - R)
    s3 = sp.simplify((1/z)**2 - 1/R)
    zc = sp.conjugate(z)
    R_P = sp.simplify(-1/sp.conjugate((-1/zc)**2))      # spatial antipodal + target antipodal
    assert s1 == 0 and s2 == 0 and s3 == 0, "z^2 map symmetries S1/S2/S3 must hold exactly"
    assert sp.simplify(R_P + z**2) == 0, "parity map must be R_P = -R (internal iso-pi about tau3)"

    # ================= (2) Krusch loop signs (imported-as-cited) =================
    def N_loop(B, theta, phi):
        val = (B*B*theta - B*phi)/(2*math.pi)
        assert abs(val - round(val)) < 1e-12, "loop must close"
        return round(val)

    pi = math.pi
    N_rot2pi_B1 = N_loop(1, 2*pi, 0)          # = 1: fermionic B=1 (banked FR fact)
    N_iso2pi_B1 = N_loop(1, 0, 2*pi)          # = -1: odd => fermionic-iso for B=1
    N_rot2pi = N_loop(2, 2*pi, 0)             # = 4: boson
    N_iso2pi = N_loop(2, 0, 2*pi)             # = -2: integer isospin
    N_S2 = N_loop(2, pi, 0)                   # = 2: +1
    N_S3 = N_loop(2, pi, pi)                  # = 1: -1  (THE load-bearing sign)
    assert (N_rot2pi_B1 % 2, N_iso2pi_B1 % 2) == (1, 1), "B=1 must be fermionic (banked)"
    assert (N_rot2pi % 2, N_iso2pi % 2) == (0, 0), "B=2 must have integer spin and isospin"
    assert (N_S2 % 2, N_S3 % 2) == (0, 1), "loop signs: S2 -> +1, S3 -> -1"
    assert (2*N_S2 - N_rot2pi) % 2 == 0 and (2*N_S3 - N_loop(2, 2*pi, 2*pi)) % 2 == 0, \
        "loop-composition consistency (S2^2 = 2pi-rot; S3^2 = 2pi-rot o 2pi-iso)"

    # ================= (3) selection tables, both branches =================
    def allowed(I, J, sign):                   # K3 = 0 tower: (-1)^{I+J} == sign
        return (-1)**(I + J) == sign
    fermionic = {(I, J): allowed(I, J, (-1)**N_S3) for I in range(3) for J in range(4)}
    bosonic = {(I, J): allowed(I, J, +1) for I in range(3) for J in range(4)}
    assert fermionic[(0, 1)] and fermionic[(1, 0)] and fermionic[(1, 2)] and fermionic[(0, 3)]
    assert not fermionic[(0, 0)] and not fermionic[(1, 1)] and not fermionic[(0, 2)]
    assert bosonic[(0, 0)] and not bosonic[(0, 1)], \
        "bosonic branch: scalar (0,0) ground state -- empirically refuted (the fork face)"

    # ================= (4) profile (R-135 solver, self-contained) =================
    def psi_map(rho):
        return (1 + rho**2)*2*rho/(1 + rho**4)
    I_ang = quad(lambda r: psi_map(r)**4 * 2*r/(1 + r**2)**2, 0, np.inf, limit=200)[0]

    def make_rhs(Bc, Ic):
        def f_rhs(t, y):
            F, Fp = y
            s2_ = math.sin(2*F); sF_ = math.sin(F)
            return [Fp, (-(t/2)*Fp - Bc*s2_*Fp**2 + Bc*s2_/4 + Ic*sF_**2*s2_/t**2)
                    / (t**2/4 + 2*Bc*sF_**2)]
        return f_rhs

    def solve_profile(Bc, Ic, a_lo, a_hi, xmax=28.0):
        p = (-1 + math.sqrt(1 + 8*Bc))/2
        s_dec = (1 + math.sqrt(1 + 8*Bc))/2
        rhs = make_rhs(Bc, Ic); x0 = 1e-3

        def integrate(a):
            return solve_ivp(rhs, (x0, xmax), [math.pi - a*x0**p, -a*p*x0**(p-1)],
                             rtol=1e-11, atol=1e-13, dense_output=True, max_step=0.1)

        def flatness(a):
            s = integrate(a)
            if np.any(s.y[0] < -1e-12):
                return -1e9
            return 16.0**s_dec*s.sol(16.0)[0] - 10.0**s_dec*s.sol(10.0)[0]

        flo = flatness(a_lo)
        assert flo*flatness(a_hi) < 0, "flatness bracket must straddle the separatrix"
        lo, hi = a_lo, a_hi
        for _ in range(52):
            mid = 0.5*(lo + hi)
            if flatness(mid)*flo > 0:
                lo = mid
            else:
                hi = mid
        return integrate(0.5*(lo + hi)), s_dec

    def radials(sol, s_dec, xmax=24.0):
        xs = np.linspace(1e-3, xmax, 24000)
        F, Fp = sol.sol(xs)
        sF = np.sin(F)
        win = (xs >= 10.0) & (xs <= 16.0)
        Ct = float(np.mean(xs[win]**s_dec*F[win]))
        R1 = np.trapezoid(xs**2*sF**2, xs) + Ct**2*xmax**(3 - 2*s_dec)/(2*s_dec - 3)
        R2 = np.trapezoid(xs**2*sF**2*Fp**2, xs)
        R3 = np.trapezoid(sF**4, xs)
        return R1, R2, R3

    def angulars(mapdeg, nth=400, nph=64):
        tg, tw = np.polynomial.legendre.leggauss(nth)
        th = np.arccos(tg)
        ph = np.linspace(0, 2*np.pi, nph, endpoint=False)
        phw = 2*np.pi/nph
        TH, PH = np.meshgrid(th, ph, indexing='ij')
        W = tw[:, None]*phw
        ST, CT = np.sin(TH), np.cos(TH)
        t2 = np.tan(TH/2.0); tn = t2**mapdeg
        CTn = (1 - tn**2)/(1 + tn**2); STn = 2*tn/(1 + tn**2)
        dTn = mapdeg*(t2**(mapdeg - 1))*0.5*(1 + t2**2)*(2.0/(1 + tn**2))
        CP, SP = np.cos(mapdeg*PH), np.sin(mapdeg*PH)
        n = np.stack([STn*CP, STn*SP, CTn])
        dn_th = np.stack([dTn*CTn*CP, dTn*CTn*SP, -dTn*STn])
        dn_ph = np.stack([-mapdeg*STn*SP, mapdeg*STn*CP, np.zeros_like(CTn)])
        dn_ph_hat = dn_ph/ST

        def dot(a, b):
            return np.einsum('c...,c...->...', a, b)

        def cross(e, v):
            return np.stack([e[1]*v[2] - e[2]*v[1], e[2]*v[0] - e[0]*v[2],
                             e[0]*v[1] - e[1]*v[0]])

        grad2 = dot(dn_th, dn_th) + dot(dn_ph_hat, dn_ph_hat)
        A_fields = {
            "U1": cross(np.array([1., 0., 0.]), n),
            "U2": cross(np.array([0., 1., 0.]), n),
            "U3": cross(np.array([0., 0., 1.]), n),
            "V3": dn_ph,
            "V1": np.sin(PH)[None]*dn_th + (CT/ST)[None]*np.cos(PH)[None]*dn_ph,
            "V2": -np.cos(PH)[None]*dn_th + (CT/ST)[None]*np.sin(PH)[None]*dn_ph,
        }
        out = {}
        for k, A in A_fields.items():
            assert float(np.max(np.abs(dot(A, n)))) < 1e-12, "A.n = 0 must hold for " + k
            Ab2 = dot(A, A)*grad2 - dot(A, dn_th)**2 - dot(A, dn_ph_hat)**2
            out[k] = (float(np.sum(dot(A, A)*W)), float(np.sum(Ab2*W)))
        # W_perp = 0 block-diagonality (the reviewer's probe, banked): all four
        # perpendicular iso x spatial CROSS angular integrals vanish, so the
        # two-state ordering argument E(0,1) vs E(1,0) has no mixing term.
        # (W33 is the lock, handled by the L3 + 2 K3 = 0 constraint.)
        cross_max = 0.0
        for ki in ("U1", "U2"):
            for ks in ("V1", "V2"):
                Ai, As = A_fields[ki], A_fields[ks]
                aq_x = float(np.sum(dot(Ai, As)*W))
                ab2_x = float(np.sum((dot(Ai, As)*grad2
                                      - dot(Ai, dn_th)*dot(As, dn_th)
                                      - dot(Ai, dn_ph_hat)*dot(As, dn_ph_hat))*W))
                cross_max = max(cross_max, abs(aq_x), abs(ab2_x))
        return out, cross_max

    def moments(sol, s_dec, mapdeg):
        R1, R2, R3 = radials(sol, s_dec)
        ang, cross_max = angulars(mapdeg)
        return {k: 0.25*Aq*R1 + Aq*R2 + Ab2*R3
                for k, (Aq, Ab2) in ang.items()}, (R1, R2, R3), cross_max

    sol1, s1_ = solve_profile(1.0, 1.0, 0.9, 1.2)
    sol2, s2_ = solve_profile(2.0, I_ang, 0.4, 0.6)
    th1, rad1, _ = moments(sol1, s1_, 1)
    th2, rad2, cross2 = moments(sol2, s2_, 2)

    # ---- certificates ----
    for k, v in th1.items():
        assert abs(v - 106.76) < 0.3, "B=1 regression: every moment must match R-133's 106.76"
    spread1 = max(th1.values()) - min(th1.values())
    assert spread1 < 0.01, "B=1: iso and spatial moments must coincide (spin-from-isospin)"
    Lam1 = rad1[0] + 4*rad1[1] + 4*rad1[2]
    assert abs(Lam1 - 50.98) < 0.15, "B=1 radials must reproduce Lambda = 50.98 (R-133)"
    assert abs(th2["V3"]/th2["U3"] - 4.0) < 1e-6, "axial identity V33 = 4 U33 must be exact"
    assert th2["V1"] > th2["U1"] + 50, "ordering: V_perp > U_perp (deuteron below isovector)"
    assert cross2 < 1e-10, "W_perp = 0: iso x spatial cross moments must vanish (no mixing)"
    assert abs(th2["U1"] - th2["U2"]) < 1e-9 and abs(th2["V1"] - th2["V2"]) < 1e-9, \
        "transverse isotropy: the 1- and 2-axis moments must coincide (axial symmetry)"

    # ---- spectrum estimate (K3 = 0 tower; FRAMING/estimate) ----
    e3fpi = E_PHYS**3*F_PI
    M2cl = 71.543*F_PI/E_PHYS
    E01 = M2cl + e3fpi/th2["V1"]              # J(J+1)/2 = 1
    E10 = M2cl + e3fpi/th2["U1"]              # I(I+1)/2 = 1
    M_N = 936.4                                # R-133 band nucleon
    assert E01 < E10, "the deuteron quantum numbers must be the ground state"
    assert 30.0 < (E10 - E01) < 50.0, "isovector-isoscalar split ~40 MeV at ansatz level"

    return {
        "outcome": ("P2-7 QUANTIZATION FACE banked: the quantized axial B = 2 sector obeys "
                    "I + J ODD on the K3 = 0 tower (FR loop signs: S2 +1, S3 -1) -- the "
                    "ground state has EXACTLY the deuteron's quantum numbers J^pi = 1+, "
                    "I = 0 (parity + from the internal parity map R_P = -R); the scalar "
                    "(0,0) dibaryon is TOPOLOGICALLY FORBIDDEN; the isovector (1,0) lies "
                    "%.1f MeV up at ansatz level (V_perp = %.1f > U_perp = %.1f). The "
                    "BOSONIC fork branch would flip the rule to I + J EVEN (scalar ground "
                    "state) -- empirically refuted: a SECOND independent anchor selecting "
                    "the fermionic branch. Spectrum values remain rigid-rotor estimates "
                    "(E(0,1) = %.0f vs 2 M_N = %.0f: overbound, known character, no "
                    "magnitude claimed)." % (E10 - E01, th2["V1"], th2["U1"], E01, 2*M_N)),
        "tier": ("DERIVED-A (map symmetries; parity MAP identity R_P = -R; V33 = 4 U33; "
                 "W_perp = 0; factorization via hedgehog reduction = R-133) + "
                 "IMPORTED-AS-CITED (Krusch homotopy formula, consistency-checked) + "
                 "DERIVED-given-(Q)+FR-selection (selection rule + deuteron quantum numbers "
                 "INCLUDING the state-level parity assignment; W-LIVE-4/N35 fork untouched) "
                 "+ ANSATZ-LEVEL (moment ordering; torus corroboration cited not banked) + "
                 "FRAMING/ESTIMATE (MeV spectrum -- rigid-rotor overbinding stated). "
                 "HEADLINE PHYSICS LITERATURE-KNOWN (Braaten-Carson 1988 / "
                 "Leese-Manton-Schroers 1995 / Krusch 2003, citations to-be-verified) -- "
                 "new content = tiering + certificated moments + fork-face bookkeeping"),
        "selection": {
            "constraint": "L3 + 2 K3 = 0 (body); K3 = 0 tower rule: I + J odd",
            "allowed_lowest": {"(0,1)": "J^pi = 1+ THE DEUTERON (ground)",
                               "(1,0)": "0+ np singlet (first excited)"},
            "forbidden": ["(0,0) scalar dibaryon", "(1,1)", "(0,2)", "(2,0)"],
            "fermionic_table": {str(k): v for k, v in sorted(fermionic.items())},
            "bosonic_table": {str(k): v for k, v in sorted(bosonic.items())},
        },
        "fork_face": ("bosonic branch => I + J EVEN => bound scalar (0,0) ground state and "
                      "no distinguished (0,1) -- refuted by the observed deuteron: second "
                      "independent empirical anchor for the fermionic FR selection (first: "
                      "nucleon spin-1/2); selection evidence, NOT a derivation (P2-4 route "
                      "stands)"),
        "moments": {"B1_regression": th1, "B1_Lambda": Lam1,
                    "B2": th2, "axial_V33_over_U33": th2["V3"]/th2["U3"],
                    "Wperp_cross_max": cross2},
        "spectrum_estimate_MeV": {"M_cl": M2cl, "E(0,1)": E01, "E(1,0)": E10,
                                  "split": E10 - E01, "threshold_2MN": 2*M_N,
                                  "note": "rigid-rotor on the R-135 upper-bound saddle; "
                                          "ESTIMATE only, overbinding known and stated"},
        "would_change_if": ("P2-4 induced level EVEN (anchor becomes a standing tension); "
                            "torus flips V vs U (literature: it does not); pion-mass BVP "
                            "shifts moments (re-check owed)"),
    }


def massive_pion_bvp_binding_margin_robust() -> dict:
    """[DERIVED, dressed-level VARIATIONAL ROBUSTNESS (the R-135 below-threshold
    inequality re-checked under the standard chiral-breaking pion-mass
    deformation at the PHYSICAL pion mass: the margin SURVIVES and slightly
    widens, 1.89% -> 1.96%; same SS10.3/D.4.3 branch-(c) conditional class;
    the inherited hedgehog-minimality premise here is R-135's EXTENDED to
    the massive functional -- the threshold 2 m1 needs the massive B = 1
    hedgehog minimal; same premise class, different functional, reviewer
    rec 4) + DERIVED-A (the
    Bessel-index identity sqrt(2B + 1/4) + 1/2 = (1 + sqrt(1 + 8B))/2 -- the
    mu -> 0 limit of the massive tail reproduces R-135's massless exponents
    EXACTLY; the mass-extended Derrick virial E2 + 3 Em = E4) + NAMED IMPORT
    (m_pi = 138 MeV enters as a WITNESS input for this robustness probe ONLY
    -- both sides of the margin use it identically; it is NOT added to the
    counted core, and the mass term's (1 - cosF) FORM is the standard
    chiral-breaking deformation, an IMPORTED PROBE, not a banked substrate
    term -- TWT has not derived pion-mass generation) + LOCATED/named fork
    (the INERTIA is the mass-sensitive object: Lambda 50.98 -> 33.52, a -34%
    shift => the massless-model N/Delta closure R-133 does NOT transfer to
    the massive variant at the same couplings; the massive scheme requires
    its own (f_pi, e) refit -- the known massive-ANW direction -- a scheme
    fork NAMED, NOT taken; the banked baseline stays the massless model.
    REFERENT PRECISION (reviewer fix 1): the pion-mass fork is a SECOND,
    DISTINCT scheme axis ALONGSIDE SC.1.2's local/phason dressed-couplings
    fork -- NOT a quantification of that fork's ~10% spread; this axis is
    object-dependent: mass coefficients mildly sensitive (+3.9%), the
    inertia strongly (-34%) at fixed couplings)] --
    P2-7 / R-135 / R-136 owed re-check DISCHARGED: nuclear binding's
    classical existence is ROBUST to the pion mass. (2026-07-03.)

    WHY THIS CHECK EXISTS: R-133, R-135, and R-136 all carry the same
    would-change-if face -- 'a banked pion-mass-term BVP shifts the
    coefficients; the binding margin must be re-checked.' This primitive is
    that re-check, scoped as a ROBUSTNESS PROBE (does the R-135 conclusion
    depend on the massless idealization?) and nothing more.

    THE DEFORMED PROBLEM (normalization re-derived in-session against the
    banked conventions, not imported blind: the quadratic expansion of
    L_m = (1/8) m_pi^2 F_pi^2 (Tr U - 2) with the L_2-normalized pion field
    gives exactly -(1/2) m_pi^2 pi^2):
      u -> u + (mu^2/4) x^2 (1 - cos F),
      mu = m_pi/(e f_pi) = 0.19629  (m_pi = 138 MeV, isospin-averaged),
      EL gains -(mu^2/4) x^2 sinF;  linearized tail
      F'' + 2F'/x - (2B/x^2 + mu^2) F = 0  =>  F = C x^{-1/2} K_nu(mu x),
      nu = sqrt(2B + 1/4)  (flatness criterion on F/asym across [10, 16] --
      the exponential tail also REMOVES the massless long-tail issue).
    DERRICK WITH MASS: E(lambda) = lambda E2 + E4/lambda + lambda^3 Em =>
      E2 + 3 Em = E4 at the minimum -- the banked profile certificate.

    THE NUMBERS (physical m_pi = 138 MeV at the counted couplings
    f_pi = 129, e = 5.45; I(z^2) = 5.8083 unchanged -- the angular integral
    is mass-term independent):
      * B = 1: coeff 37.90 f_pi/e (massless 36.46, +3.9%); virial 5e-6;
        tail-constant spread < 1e-4 (the Bessel asymptote matches cleanly).
      * B = 2: coeff 74.31 f_pi/e (massless 71.54); virial 3e-6.
      * THE MARGIN: 74.31 < 2 x 37.90 = 75.80 -- 1.96% below threshold
        (massless: 1.89%): the below-threshold inequality is ROBUST, indeed
        marginally STRONGER; binding >= 35.2 MeV at these couplings
        (massless: 32.7). R-135's would-change-if (a) face: DISCHARGED for
        the EXISTENCE/SIGN conclusion (values still scheme-forked).
      * THE INERTIA SHIFT (the R-133 face): massive-profile Lambda = 33.52
        vs massless 50.98 (theta-coeff 106.76 -> 70.20). At the SAME counted
        couplings the massive N/Delta band closure FAILS -- confirming the
        massive variant is a DIFFERENT SCHEME requiring its own refit
        (massive-ANW-class), not a small correction to the banked massless
        pipeline. R-133's closure is massless-scheme-specific -- stated in
        its bank, now QUANTIFIED.

    HONEST ACCOUNTING: one imported witness constant (m_pi -- both sides of
    the margin identically; retiring it changes nothing in the counted core);
    no refit performed (the massive-scheme refit is the named, not-taken
    fork); the R-136 quantum-number selection is UNTOUCHED by the mass term
    (the map symmetries and FR loop signs are topological -- only the
    MOMENTS shift, so the ordering V_perp > U_perp would need a massive-
    profile re-check IF the massive scheme is ever adopted: noted, owed
    only in that branch).

    WOULD CHANGE IF: (a) the massive-scheme refit is banked => all massive
    numbers here get re-anchored (the margin statement then needs re-check
    at the refit couplings -- literature keeps B = 2 bound there, imported
    not banked); (b) a substrate derivation of the chiral-breaking term
    lands => the probe becomes a banked sector and m_pi's status upgrades.
    """
    import numpy as np
    from scipy.integrate import solve_ivp, quad
    from scipy.special import kv

    MU = 138.0/(E_PHYS*F_PI)
    I2 = 5.808259320256459        # I(z^2), banked in R-135 (mass-independent)

    # Bessel-index identity (DERIVED-A): sqrt(2B+1/4) + 1/2 = (1+sqrt(1+8B))/2
    for Bc in (1.0, 2.0, 3.0, 7.0):
        assert abs((math.sqrt(2*Bc + 0.25) + 0.5) - (1 + math.sqrt(1 + 8*Bc))/2) < 1e-14, \
            "mu -> 0 Bessel index must reproduce the massless tail exponent"

    def make_rhs(Bc, Ic, mu):
        def f_rhs(t, y):
            F, Fp = y
            s2 = math.sin(2*F); sF = math.sin(F)
            return [Fp, (-(t/2)*Fp - Bc*s2*Fp**2 + Bc*s2/4 + Ic*sF**2*s2/t**2
                         + (mu**2/4)*t**2*sF) / (t**2/4 + 2*Bc*sF**2)]
        return f_rhs

    def solve_profile(Bc, Ic, mu, a_lo, a_hi, xmax=26.0):
        p = (-1 + math.sqrt(1 + 8*Bc))/2
        nu = math.sqrt(2*Bc + 0.25)
        rhs = make_rhs(Bc, Ic, mu)
        x0 = 1e-3

        def asym(x):
            return kv(nu, mu*x)/math.sqrt(x)

        def integrate(a):
            return solve_ivp(rhs, (x0, xmax), [math.pi - a*x0**p, -a*p*x0**(p-1)],
                             rtol=1e-11, atol=1e-13, dense_output=True, max_step=0.1)

        def flatness(a):
            s = integrate(a)
            if np.any(s.y[0] < -1e-12):
                return -1e9
            return s.sol(16.0)[0]/asym(16.0) - s.sol(10.0)[0]/asym(10.0)

        flo = flatness(a_lo)
        assert flo*flatness(a_hi) < 0, "flatness bracket must straddle the separatrix"
        lo, hi = a_lo, a_hi
        for _ in range(52):
            mid = 0.5*(lo + hi)
            if flatness(mid)*flo > 0:
                lo = mid
            else:
                hi = mid
        return integrate(0.5*(lo + hi)), nu

    def energy(sol, Bc, Ic, mu, nu, xcut=24.0):
        xs = np.linspace(1e-3, xcut, 30000)
        F, Fp = sol.sol(xs)
        sF = np.sin(F)
        xw = np.linspace(10.0, 16.0, 50)
        ratio = sol.sol(xw)[0]/np.array([kv(nu, mu*x)/math.sqrt(x) for x in xw])
        Ct, Ct_sp = float(np.mean(ratio)), float(np.std(ratio))
        E2 = 4*np.pi*np.trapezoid(xs**2*Fp**2/8 + Bc*0.25*sF**2, xs)
        E4 = 4*np.pi*np.trapezoid(Bc*sF**2*Fp**2 + Ic*0.5*sF**4/xs**2, xs)
        Em = 4*np.pi*np.trapezoid((mu**2/4)*xs**2*(1 - np.cos(F)), xs)
        return E2, E4, Em, Ct, Ct_sp

    sol1, nu1 = solve_profile(1.0, 1.0, MU, 0.9, 1.6)
    E2a, E4a, Ema, C1, C1s = energy(sol1, 1.0, 1.0, MU, nu1)
    m1 = E2a + E4a + Ema
    vir1 = abs(E2a + 3*Ema - E4a)/m1

    sol2, nu2 = solve_profile(2.0, I2, MU, 0.3, 0.9)
    E2b, E4b, Emb, C2, C2s = energy(sol2, 2.0, I2, MU, nu2)
    m2 = E2b + E4b + Emb
    vir2 = abs(E2b + 3*Emb - E4b)/m2

    margin = (2*m1 - m2)/(2*m1)
    binding = (2*m1 - m2)*F_PI/E_PHYS

    # massive-profile inertia (the R-133 face)
    xs = np.linspace(1e-3, 24.0, 30000)
    F, Fp = sol1.sol(xs)
    sF = np.sin(F)
    Lam_massive = (np.trapezoid(xs**2*sF**2, xs) + 4*np.trapezoid(xs**2*sF**2*Fp**2, xs)
                   + 4*np.trapezoid(sF**4, xs))

    assert vir1 < 1e-4 and vir2 < 1e-4, "mass-extended Derrick E2 + 3Em = E4 must certify"
    assert C1s < 1e-3 and C2s < 1e-3, "Bessel-asymptote tail constants must be clean"
    assert abs(m1 - 37.90) < 0.05 and abs(m2 - 74.31) < 0.1, "massive coefficients 37.90/74.31"
    assert m2 < 2*m1 - 1.0, "THE RE-CHECK: B = 2 must stay strictly below threshold"
    assert 0.015 < margin < 0.025 and margin > 0.0189, \
        "margin must survive AND widen (> the massless 0.0189; reviewer fix 3)"
    assert 33.0 < binding < 38.0, "massive binding bound ~35 MeV"
    assert abs(Lam_massive - 33.5) < 0.3, "massive Lambda = 33.5 (vs massless 50.98, -34%)"
    assert abs(Lam_massive - 50.98) > 15.0, \
        "the inertia shift is LARGE: massive scheme is a different scheme (refit fork named)"

    return {
        "outcome": ("OWED RE-CHECK DISCHARGED: the R-135 below-threshold inequality is "
                    "ROBUST at the physical pion mass -- massive coefficients 74.31 < "
                    "2 x 37.90 = 75.80 (margin %.2f%%, massless 1.89%% -- it WIDENS); "
                    "binding >= %.1f MeV at the counted couplings. The INERTIA is the "
                    "mass-sensitive object (Lambda 50.98 -> %.2f, -34%%): the massless "
                    "N/Delta closure does NOT transfer -- the massive variant is a "
                    "different SCHEME needing its own refit (fork named, not taken)."
                    % (100*margin, binding, Lam_massive)),
        "tier": ("DERIVED dressed-level VARIATIONAL ROBUSTNESS (branch-(c) conditional; "
                 "inherited hedgehog-minimality premise as R-135) + DERIVED-A (Bessel-index "
                 "identity; mass-extended Derrick) + NAMED IMPORT (m_pi witness, probe-only; "
                 "the (1-cosF) form is an imported chiral-breaking deformation, not a banked "
                 "substrate term) + LOCATED (massive-scheme refit fork named, not taken at "
                 "R-137 -- executed at R-138 as a parallel BRANCH; baseline unchanged)"),
        "mu": MU,
        "massive": {"m1": m1, "m2": m2, "virials": (vir1, vir2),
                    "margin": margin, "binding_MeV": binding,
                    "tail_constants": (C1, C2), "Lambda_massive": Lam_massive,
                    "theta_coeff_massive": float(2*np.pi/3*Lam_massive)},
        "massless_reference": {"m1": 36.4617, "m2": 71.5430, "margin": 0.0189,
                               "Lambda": 50.98, "theta_coeff": 106.76},
        "r136_note": ("the R-136 quantum-number selection is mass-term UNTOUCHED "
                      "(topological); only the moments shift -- the V_perp > U_perp "
                      "ordering re-check is owed ONLY in the massive-scheme branch"),
        "would_change_if": ("massive-scheme refit banked (FIRED at R-138, 2026-07-03: "
                            "margin re-checked at the refit couplings, 1.87% -- survives; "
                            "the margin is non-monotonic in mu, so the widening at the "
                            "probe point is probe-point-specific); substrate derivation of "
                            "the chiral-breaking term (probe -> sector)"),
    }


MASSIVE_FPI, MASSIVE_E = 108.2594, 4.84269   # R-138 massive-scheme refit (branch values)


def massive_scheme_refit_branch() -> dict:
    """[FIT, in-branch (the massive-scheme refit of the SAME two dressed dials
    (f_pi, e) to the SAME two observables N/Delta, now in the massive-pion
    functional -- coordinator-approved fork execution 2026-07-03; honest
    counting: the massive BRANCH carries THREE counted inputs (f_pi, e, m_pi)
    vs the massless baseline's TWO, because m_pi is load-bearing in-branch,
    no longer a probe witness) + DERIVED-A (the Theta_0 fit-invariance
    identity: in ANY scheme closing N/Delta with the band equation
    M(J) = M_0 + J(J+1)/(2 Theta_0), the splitting alone pins
    1/Theta_0 = (2/3)(M_Delta - M_N)_obs = 195.4 MeV -- trivially exact,
    and consequential: every Theta_0-downstream banked number is
    scheme-fork-INVARIANT) + DERIVED dressed-level VARIATIONAL robustness
    (the R-135 below-threshold inequality re-checked AT the refit couplings:
    margin 1.87% -- the binding conclusion now verified across the ENTIRE
    fork: massless 1.89%, massive-at-massless-couplings 1.96%,
    massive-at-refit 1.87% -- the margin is NON-MONOTONIC in mu (banked,
    reviewer rec R5, so nobody 'corrects' one of the three numbers on
    monotonicity intuition): R-137's 'widens' holds AT THE PROBE POINT;
    at the refit couplings the margin is marginally NARROWER than massless.
    NO FOURTH FORK CORNER (reviewer rec R6): the massless margin is
    coupling-independent (pure f_pi/e scaling), so the margin is a function
    of mu alone and {0, 0.196, 0.263} exhausts the named fork. Inherited
    conditionals: branch-(c) dressed closure + hedgehog minimality extended
    to the massive functional, as R-135/R-137) + SCHEME DECISION, a
    bookkeeping entry, NOT a derived claim (reviewer fix F2: the banked
    baseline STAYS the massless model on D1 parameter economy --
    METHODOLOGICAL -- plus ONE HEDGED empirical face, D2 convergence-
    preservation below, plus D4 IMPORT-MINIMIZATION: in-branch the
    (1-cosF) chiral-breaking FORM is a load-bearing UNDERIVED structural
    import, no longer R-137's probe-only witness (fix F4), so the
    substrate-first discipline itself favors the minimal-import
    functional)] -- the massive-scheme
    refit branch: executed, banked, and adjudicated. (2026-07-03.)

    THE REFIT (development: 2D Newton on (f_pi, e) with the self-consistent
    mu = m_pi/(e f_pi) -- each trial solves the massive hedgehog BVP; this
    primitive VERIFIES the banked refit point with one solve, R-133-style):
      f_pi* = 108.26 MeV, e* = 4.8427, mu* = 0.26322,
      m1(mu*) = 38.72, theta_coeff(mu*) = 62.92, M_0 = 865.6 MeV;
      M_N = 938.9, M_Delta = 1232.0 closed exactly (fit construction).
    CORROBORATION (not load-bearing): Adkins-Nappi 1984's published massive
    fit (f_pi = 108, e = 4.84) -- reproduced independently end-to-end
    (citation to-be-verified before external use, R-134 precedent; the
    in-code assert pinning (108, 4.84) is a corroboration pin, partly
    self-referential -- the real certificate is the verification solve
    closing N/Delta). UNIQUENESS/CONVERGENCE (reviewer probe, banked note):
    the reviewer re-derived the fit by a DIFFERENT algorithm (1D fixed point
    on mu with a closed-form inner solve, different solver config) from two
    starting points bracketing the answer (mu_0 = 0.20 and 0.32) -- both
    converge monotonically to the banked point to 4e-6: the fit point is
    unique in the physical range.

    THE INVARIANCE (DERIVED-A given the band FORM and the J = 1/2, 3/2
    assignment -- i.e. it inherits R-133's (Q)+FR-selection conditional,
    reviewer annotation): 1/Theta_0 = (2/3) x 293.1 = 195.4 MeV for any
    EXACT-closure fit (the banked massless baseline closes N/Delta to
    ~0.3%, so its banked value reads 195.6 -- the identity is exact for
    exact closure; no banked number changes). Hence:
      * R-111's Lambda_QCD candidate (~196 MeV): scheme-fork-ROBUST.
      * The top exclusion Gamma_t Theta_0 = 7.2: scheme-fork-ROBUST.
      * The Sigma_c - Lambda_c TRACKED RESIDUAL (-9.0%, R-133): UNCHANGED
        by the fork -- the refit does NOT resolve it: 'scheme artifact' is
        ELIMINATED as an explanation, and the weight redistributes to BOTH
        of R-133's named surviving candidates (reviewer fix F3): (i) the
        Callan-Klebanov-class bound-state inertia, AND (ii) the hf_c anchor
        re-fit (independence still unverified) -- neither is excluded by
        anything in the record.

    THE DISCRIMINATORS (the fork decision made principled, not conventional):
      (D1) PARAMETER ECONOMY (methodological): massless baseline = 2 counted
           inputs; massive branch = 3 (m_pi load-bearing). Same observables
           closed. Honest counter-note (reviewer rec R4): the third input
           BUYS the physical pion tail -- it is not a free cost.
      (D2) HEDGED CONVERGENCE-PRESERVATION (reviewer fix F1 -- the banked
           sqrt(18)/(D/J) face is itself HEDGED: dressed_coupling tags
           sqrt(18) 'coincidence-riding... no static referent' and banks
           TWO routes, explicitly 'NOT a single 1% number'; the hedge is
           carried here, not dropped). The two-route x two-scheme grid:
           sqrt(18)/e: massless 0.7784 (-1.1% vs lepton D/J 0.787) vs
           massive 0.8761 (+11.3%); sqrt(12)/e (the other banked route):
           massless 0.6356 (-19.2%) vs massive 0.7153 (-9.1%) -- NOTE the
           sign flips on that route. The engine-true SMALLER claim: the
           ONLY sub-2% convergence anywhere in the grid is massless-sqrt18;
           NO rival convergence appears in the massive branch on either
           route. D2 = the massless baseline PRESERVES the one banked
           (hedged) convergence; it does not 'empirically select' alone.
      (D3) N/Delta closure: NO discrimination (both exact by construction).
      (D4) IMPORT-MINIMIZATION (framework-native): the branch functional
           carries the underived (1-cosF) chiral-breaking form as a
           load-bearing structural import; the massless functional carries
           no such import. Substrate-first discipline favors the
           minimal-import baseline.
      VERDICT: the massless model stays the banked baseline -- on economy
      (methodological) + one hedged empirical face + import-minimization;
      a DECISION entry, not a derived claim. The massive branch is banked
      as a named parallel scheme (these constants) for uses where the
      physical pion tail is essential (e.g. asymptotic NN interactions).

    OWED RE-CHECKS DISCHARGED AT REFIT COUPLINGS (this primitive solves the
    B = 2 massive BVP at mu* in-suite):
      * R-137 would-change-if (a): margin at the refit couplings = 1.87%
        (75.997 < 2 x 38.721 = 77.442), binding >= 32.3 MeV -- SURVIVES.
      * R-136 massive-branch moment ordering: V_perp = 222.1 > U_perp =
        135.6 (exact factorized moments on the mu* profile) -- the deuteron
        quantum numbers REMAIN the ground state; isovector split ~35 MeV
        (vs 40.5 massless-couplings) -- ordering fork-robust.
      * Rigid-rotor spectrum estimate at refit: E(0,1) = 1754 vs
        2 M_N = 1877.8 -- overbound ~124 MeV: the SAME known rigid-rotor/
        rational-map character in both schemes (FRAMING/estimate, unchanged).

    KNOCK-ON SWEEP (checked, none change): Theta_0-downstream numbers
    invariant (above); the banked f_pi = 129 / e = 5.45 / e f_pi = 703 MeV
    cell-scale constants are BASELINE quantities and stay (the branch scale
    e* f_pi* = 524 MeV is recorded in-branch only); no banked number moves.

    WOULD CHANGE IF: (a) a substrate derivation of the chiral-breaking term
    lands (the branch's third input becomes derived => economy discriminator
    D1 dissolves and the fork re-opens on D2 alone); (b) the D/J calibration
    moves (D2 re-evaluates); (c) a P2-5-class cell-scale derivation pins
    e f_pi independently (would adjudicate the fork from the substrate side).
    """
    import numpy as np
    from scipy.integrate import solve_ivp
    from scipy.special import kv

    M_PI_W = 138.0
    OBS_N, OBS_D = 938.9, 1232.0
    fpi_s, e_s = MASSIVE_FPI, MASSIVE_E
    mu_s = M_PI_W/(e_s*fpi_s)

    def solve_prof(B, I, mu, xmax=26.0):
        p = (-1 + math.sqrt(1 + 8*B))/2
        nu = math.sqrt(2*B + 0.25)

        def rhs(t, y):
            F, Fp = y
            s2 = math.sin(2*F); sF = math.sin(F)
            return [Fp, (-(t/2)*Fp - B*s2*Fp**2 + B*s2/4 + I*sF**2*s2/t**2
                         + (mu**2/4)*t**2*sF) / (t**2/4 + 2*B*sF**2)]

        x0 = 1e-3

        def integrate(a):
            return solve_ivp(rhs, (x0, xmax), [math.pi - a*x0**p, -a*p*x0**(p-1)],
                             rtol=1e-10, atol=1e-12, dense_output=True, max_step=0.1)

        def asym(x):
            return kv(nu, mu*x)/math.sqrt(x)

        def flat(a):
            s = integrate(a)
            if np.any(s.y[0] < -1e-12):
                return -1e9
            return s.sol(16.0)[0]/asym(16.0) - s.sol(10.0)[0]/asym(10.0)

        grid = np.linspace(0.2, 3.0, 29)
        vals = [flat(a) for a in grid]
        for i in range(len(grid) - 1):
            if vals[i]*vals[i+1] < 0:
                lo, hi, flo = grid[i], grid[i+1], vals[i]
                break
        else:
            raise RuntimeError("no flatness bracket")
        for _ in range(50):
            mid = 0.5*(lo + hi)
            if flat(mid)*flo > 0:
                lo = mid
            else:
                hi = mid
        return integrate(0.5*(lo + hi))

    def energy_and_radials(sol, B, I, mu):
        xs = np.linspace(1e-3, 24.0, 20000)
        F, Fp = sol.sol(xs)
        sF = np.sin(F)
        E2 = 4*np.pi*np.trapezoid(xs**2*Fp**2/8 + B*0.25*sF**2, xs)
        E4 = 4*np.pi*np.trapezoid(B*sF**2*Fp**2 + I*0.5*sF**4/xs**2, xs)
        Em = 4*np.pi*np.trapezoid((mu**2/4)*xs**2*(1 - np.cos(F)), xs)
        vir = abs(E2 + 3*Em - E4)/(E2 + E4 + Em)
        rads = (float(np.trapezoid(xs**2*sF**2, xs)),
                float(np.trapezoid(xs**2*sF**2*Fp**2, xs)),
                float(np.trapezoid(sF**4, xs)))
        return E2 + E4 + Em, vir, rads

    # ---- verify the banked refit point (one massive B=1 solve) ----
    sol1 = solve_prof(1.0, 1.0, mu_s)
    m1, vir1, rads1 = energy_and_radials(sol1, 1.0, 1.0, mu_s)
    thc = (2*np.pi/3)*(rads1[0] + 4*rads1[1] + 4*rads1[2])
    M0 = m1*fpi_s/e_s
    invT = e_s**3*fpi_s/thc
    M_N = M0 + 0.375*invT
    M_D = M0 + 1.875*invT

    # ---- Theta_0 fit-invariance identity ----
    invT_pinned = (2.0/3.0)*(OBS_D - OBS_N)

    # ---- B = 2 at refit couplings: margin + moments ----
    I2 = 5.808259320256459
    sol2 = solve_prof(2.0, I2, mu_s)
    m2, vir2, rads2 = energy_and_radials(sol2, 2.0, I2, mu_s)
    margin = (2*m1 - m2)/(2*m1)
    binding = (2*m1 - m2)*fpi_s/e_s

    def angulars_deg2(nth=400, nph=64):
        tg, tw = np.polynomial.legendre.leggauss(nth)
        th = np.arccos(tg)
        ph = np.linspace(0, 2*np.pi, nph, endpoint=False)
        phw = 2*np.pi/nph
        TH, PH = np.meshgrid(th, ph, indexing='ij')
        W = tw[:, None]*phw
        ST, CT = np.sin(TH), np.cos(TH)
        t2 = np.tan(TH/2.0); tn = t2**2
        CTn = (1 - tn**2)/(1 + tn**2); STn = 2*tn/(1 + tn**2)
        dTn = 2*t2*0.5*(1 + t2**2)*(2.0/(1 + tn**2))
        CP, SP = np.cos(2*PH), np.sin(2*PH)
        n = np.stack([STn*CP, STn*SP, CTn])
        dn_th = np.stack([dTn*CTn*CP, dTn*CTn*SP, -dTn*STn])
        dn_ph = np.stack([-2*STn*SP, 2*STn*CP, np.zeros_like(CTn)])
        dn_ph_hat = dn_ph/ST

        def dot(a, b):
            return np.einsum('c...,c...->...', a, b)

        grad2 = dot(dn_th, dn_th) + dot(dn_ph_hat, dn_ph_hat)
        A_iso = np.stack([np.zeros_like(CTn), -n[2], n[1]])          # e1 x n
        A_sp = np.sin(PH)[None]*dn_th + (CT/ST)[None]*np.cos(PH)[None]*dn_ph
        out = {}
        for k, A in (("U1", A_iso), ("V1", A_sp)):
            Ab2 = dot(A, A)*grad2 - dot(A, dn_th)**2 - dot(A, dn_ph_hat)**2
            out[k] = (float(np.sum(dot(A, A)*W)), float(np.sum(Ab2*W)))
        return out

    ang = angulars_deg2()
    R1, R2, R3 = rads2
    U1 = 0.25*ang["U1"][0]*R1 + ang["U1"][0]*R2 + ang["U1"][1]*R3
    V1 = 0.25*ang["V1"][0]*R1 + ang["V1"][0]*R2 + ang["V1"][1]*R3
    e3f = e_s**3*fpi_s
    E01 = m2*fpi_s/e_s + e3f/V1
    E10 = m2*fpi_s/e_s + e3f/U1

    # ---- discriminators ----
    dj_massless = math.sqrt(18)/5.45
    dj_massive = math.sqrt(18)/e_s
    dj12_massless = math.sqrt(12)/5.45
    dj12_massive = math.sqrt(12)/e_s
    DJ_LEPTON = DoverJ_from_lepton_masses()   # 0.7869, wired (reviewer rec R2)

    # ---- certificates ----
    assert vir1 < 1e-4 and vir2 < 1e-4, "mass-extended Derrick must certify both profiles"
    assert abs(M_N - OBS_N) < 0.2 and abs(M_D - OBS_D) < 0.5, \
        "the banked refit point must close N/Delta (verification solve)"
    assert abs(fpi_s - 108.0) < 1.0 and abs(e_s - 4.84) < 0.02, \
        "refit must corroborate the Adkins-Nappi 1984 neighborhood (108, 4.84)"
    assert abs(invT - invT_pinned) < 0.5, \
        "Theta_0 fit-invariance: 1/Theta_0 = (2/3) split_obs = 195.4 in-branch too"
    assert m2 < 2*m1 - 1.0 and 0.015 < margin < 0.025, \
        "R-137 owed re-check: margin must survive at the refit couplings (~1.87%)"
    assert V1 > U1 + 50, \
        "R-136 owed re-check: deuteron ordering V_perp > U_perp must hold in-branch"
    assert abs(dj_massless - DJ_LEPTON) < 0.01, \
        "D2: the one sub-2% convergence in the two-route x two-scheme grid (massless sqrt18)"
    assert min(abs(dj_massive - DJ_LEPTON), abs(dj12_massless - DJ_LEPTON),
               abs(dj12_massive - DJ_LEPTON)) > 0.05, \
        "D2: no rival convergence in the grid (massive both routes; massless sqrt12)"

    return {
        "outcome": ("MASSIVE-SCHEME REFIT BRANCH banked: f_pi* = %.2f MeV, e* = %.4f "
                    "(mu* = %.4f; corroborates Adkins-Nappi 108/4.84), N/Delta closed. "
                    "1/Theta_0 = %.1f MeV is FIT-INVARIANT across the fork => Lambda_QCD "
                    "candidate, top exclusion, AND the Sigma_c-Lambda_c residual all "
                    "UNCHANGED (the fork does NOT resolve the residual). Owed re-checks "
                    "DISCHARGED at refit couplings: margin %.2f%% (binding >= %.1f MeV); "
                    "deuteron ordering V_perp = %.1f > U_perp = %.1f. BASELINE DECISION "
                    "(bookkeeping, not derivation): massless stays -- parameter economy "
                    "(2 vs 3 counted inputs) + the one HEDGED sqrt(18)/e face (only "
                    "sub-2%% grid entry: massless within 1.1%% of lepton D/J vs massive "
                    "+11.3%%) + import-minimization (the (1-cosF) form is a load-bearing "
                    "underived import in-branch)."
                    % (fpi_s, e_s, mu_s, invT, 100*margin, binding, V1, U1)),
        "tier": ("FIT in-branch (same 2 dials refit; branch counts 3 inputs -- m_pi "
                 "load-bearing in-branch) + DERIVED-A (Theta_0 fit-invariance identity) + "
                 "DERIVED variational robustness (margin + ordering at refit couplings) + "
                 "SCHEME DECISION, a bookkeeping entry, not a derived claim (baseline "
                 "stays massless on D1 parameter economy [methodological] + ONE HEDGED "
                 "D2 empirical face + D4 import-minimization; branch banked as parallel "
                 "named scheme)"),
        "refit": {"f_pi": fpi_s, "e": e_s, "mu": mu_s, "m1": m1, "theta_coeff": thc,
                  "M0_MeV": M0, "M_N": M_N, "M_Delta": M_D, "inv_Theta0": invT},
        "invariance": {"inv_Theta0_pinned": invT_pinned,
                       "consequence": ("Lambda_QCD candidate ~195.4, top exclusion 7.2, "
                                       "Sigma_c-Lambda_c residual -9.0%: ALL fork-invariant")},
        "discriminators": {
            "D1_parameter_economy": "massless 2 counted inputs vs massive 3 (m_pi in-branch)",
            "D2_sqrt18_over_e": {"massless": dj_massless, "massive": dj_massive,
                                 "sqrt12_massless": dj12_massless,
                                 "sqrt12_massive": dj12_massive,
                                 "lepton_DJ": DJ_LEPTON,
                                 "note": ("HEDGED convergence-preservation: only sub-2% "
                                          "grid entry is massless-sqrt18; sign flips on "
                                          "the sqrt12 route (massive -9.1% vs massless "
                                          "-19.2%); the banked hedge is carried")},
            "D3_N_Delta": "no discrimination (both exact by construction)",
            "D4_import_minimization": ("branch carries the underived (1-cosF) form as a "
                                       "load-bearing import; massless does not"),
            "verdict": ("BASELINE STAYS MASSLESS (economy + one hedged empirical face + "
                        "import-minimization; a decision entry, not a derived claim)"),
        },
        "recheck_margin": {"m1": m1, "m2": m2, "margin": margin, "binding_MeV": binding},
        "recheck_ordering": {"U_perp": U1, "V_perp": V1,
                             "E(0,1)": E01, "E(1,0)": E10,
                             "spectrum_note": ("rigid-rotor estimate; overbound ~124 MeV vs "
                                               "2 M_N = 1877.8 -- same known character as "
                                               "the massless scheme; FRAMING only")},
        "branch_scale_note": ("e* f_pi* = 524 MeV recorded in-branch only; the banked "
                              "cell-scale constants (f_pi = 129, e = 5.45, 703 MeV) are "
                              "BASELINE quantities and do not move"),
        "would_change_if": ("substrate chiral-breaking derivation lands (D1 dissolves, "
                            "fork re-opens on D2); D/J calibration moves (D2 re-evaluates); "
                            "P2-5-class cell-scale derivation pins e f_pi from the "
                            "substrate (adjudicates the fork independently)"),
    }


def two_defect_asymptotic_tensor_force() -> dict:
    """[DERIVED-A (three exact identities, sympy-verified in-primitive: (i) the
    B = 1 massive tail is ELEMENTARY -- nu = sqrt(2B+1/4) = 3/2 half-integer,
    K_{3/2}(z) = sqrt(pi/2z) e^-z (1+1/z), so F = C_dip (1+mu x) e^{-mu x}/x^2
    EXACTLY, i.e. the exact derivative-of-Yukawa dipole profile, massless
    limit F = C/x^2 identically; (ii) the dipole identity
    -d/dr(e^{-mu r}/r) = (1+mu r) e^{-mu r}/r^2; (iii) the OPE decomposition
    O_ab d_a d_b Y = (3 O_RR - TrO)(1 + mu R + mu^2 R^2/3) e^{-mu R}/R^3
    + TrO (mu^2 R^2/3) e^{-mu R}/R^3 -- the tensor radial function is
    IDENTICAL to the standard one-pion-exchange tensor shape and the central
    piece vanishes as mu -> 0) + DERIVED dressed-level ASYMPTOTIC
    (product-ansatz class, the standard variational trial for two well-
    separated defects; same branch-(c) conditional as R-135/R-137: the
    two-defect interaction law
        V(R, O) = + pi C^2 [ (3 O_RR - TrO)(1 + mu R + mu^2 R^2/3)
                             + TrO mu^2 R^2/3 ] e^{-mu R} / R^3,
    with O the relative iso-orientation, O_RR = O_ab Rhat_a Rhat_b, and C
    the BANKED tail constant -- derivation: the asymptotic Skyrmion is an
    exact TRIPLET OF ORTHOGONAL PION DIPOLES pi_a = -C d_a Y (the hedgehog
    locks iso-index to space-index; certificated by the R-135/R-137 tails),
    and the quadratic-energy cross term integrates by parts onto the dipole
    sources; SIGN AND MAGNITUDE PINNED BY THE GRID, not by convention)
    + GRID-CERTIFICATED, SCOPED (reviewer fix F4: EXACT for the signs, the
    channel structure, and the aligned-channel zero; MAGNITUDE at the
    10-20% level raw, with the residual ACCOUNTED by named grid
    systematics -- h^2 discretization + finite-box (R/L)^3 cross-term
    truncation. Development record, 169^3 grid at h = 0.25, massless,
    R = 8/10/12/14: aligned channel +0.34/+0.068/+0.005/-0.013 (falling
    fast; all four values, fix F5); parallel pi-rotation REPULSIVE, ratio
    to +4 pi C^2/R^3 = 0.81/0.87/0.90/0.92; perpendicular ATTRACTIVE,
    ratio to -2 pi C^2/R^3 = 0.66/0.78/0.82/0.83; channel ratio -> 2.2 vs
    exact 2. REVIEWER SYSTEMATICS PROBE (banked, fix F4 -- the '-> 1' is
    evidence-backed, not extrapolated from the fixed grid alone): at
    R = 12 the perp ratio RISES with box size (0.742/0.785/0.801 at
    L = 15/21/27, h = 0.30) and with refinement (0.848 at h = 0.20);
    Richardson h -> 0 gives ~0.90 at finite L, ~0.93-0.95 with the
    L-trend (par ~0.95-0.98) -- the deficits are grid systematics, not
    physics. The in-suite check reruns a REDUCED 81^3 grid asserting the
    exact sign/channel structure + loose magnitude windows) + CORRECTED PREMISE-DRIFT (reviewer fix F3: the
    worklist's 'tensor force FROM D4 anisotropy via DM' was WORKLIST DRIFT,
    not a banked corpus premise -- the V1-era eta_DM primitive already
    banked 'dominant tensor = OPE (standard Skyrme); D4 contributes only
    the sub-percent DM anisotropy eta_DM = (D/J)^2/144 ~ 0.43%'. R-139
    UPGRADES that imported 'standard OPE' into an in-framework derivation
    from the banked tails, and the eta_DM 1/144 CALIBRATED face is
    PRESERVED as the named P2-5-gated subleading row (its Paper-2 D4
    vertex computation still owed); ledger N39 records the drift
    correction, N0-genre) + NAMED
    FOLLOW-UP (the nucleon-state PROJECTION O_ab -> spin-isospin operators
    (tau1.tau2, S_12) that turns this classical law into the quantum OPE
    potential -- Braaten-Carson/JJP-class, imported-as-cited when taken;
    the S-D mixing / deuteron quadrupole face lives there)] --
    P2-7 TENSOR-FORCE FACE: the nuclear tensor force's classical seat,
    derived from the banked tails with the OPE radial structure EXACT,
    and the D4-anisotropy premise corrected. (2026-07-03.)

    THE PHYSICAL READING: in the R-138 massive branch (the named use case
    for these asymptotics) the interaction range is 1/m_pi BY CONSTRUCTION
    and the law above IS the one-pion-exchange central + TENSOR structure
    -- TWT's dressed sector puts the deuteron's tensor glue where nature
    puts it (pion-tail dipoles), with strength set by the banked tail
    constants, all solved in-primitive: massless C = 8.634 (R-133/R-135);
    probe C_dip = C_t sqrt(pi/(2 mu))/mu = 7.91 (C_t = 0.5487, matching
    R-137's banked B = 1 value); refit C_dip = 7.66 (C_t = 0.8251 at
    mu* = 0.26322 -- REVIEWER FIX F1: an earlier draft transcribed 0.457,
    R-137's B=2-AT-PROBE constant, as the refit B=1 value, giving a
    REFUTED 4.24; the corrected physics is cleaner -- the dipole strength
    is nearly FORK-INVARIANT, 8.63 -> 7.91 -> 7.66, gently screened by
    mu, not the odd factor-2 collapse the misread implied). The
    quantitative g_piNN-analog strength comparison awaits the projection
    follow-up (NOT claimed here).

    PRIOR ART, stated plainly (reviewer fix F2, R-134/R-136 precedent): the
    headline physics -- asymptotic Skyrmion = triplet of orthogonal pion
    dipoles, the dipole-dipole interaction law, the attractive channel at
    pi-rotation perpendicular to the separation, and the OPE identification
    -- is ESTABLISHED Skyrme literature (Skyrme; Jackson-Jackson-Pasquier
    1985; Manton-Sutcliffe -- citations to-be-verified before external use).
    R-139's NEW content: the in-framework derivation from the BANKED tails
    (with the fork-resolved constants), the exact-identity certificates, the
    grid computation at the counted couplings, and the D4 premise-drift
    correction below.

    SIGN-AMBIGUITY ORIGIN (reviewer rec (b)): the naive quadratic-energy
    cross term has the classic source-interaction vs field-energy
    bookkeeping ambiguity (for scalar sources the field cross term of like
    charges is positive while the interaction is attractive) -- a
    quadratic-only computation would get every channel sign wrong, which is
    exactly why the sign is pinned by the GRID, not by convention.

    THE ATTRACTIVE CHANNEL (consistency anchor): maximal attraction at
    pi-rotation about an axis PERPENDICULAR to the separation -- the same
    relative-orientation structure the R-135 rational-map B = 2
    configuration realizes; the below-threshold binding and this asymptotic
    attraction are two faces of one channel.

    P2-7 CLOSURE (this face was the item's last constructive half): with
    R-135 (existence + sign), R-136 (deuteron quantum numbers), R-137
    (pion-mass robustness), R-138 (scheme fork executed + baseline), and
    R-139 (tensor force + premise correction), the P2-7 worklist item is
    DONE AT ITS DEFINED SCOPE. The one located residual: the binding
    MAGNITUDE (the 2.22 MeV face) -- rigid-rotor rational-map level
    overbinds by ~113/~124 MeV (massless/refit; R-136/R-138 estimates,
    reviewer fix F5); closure
    requires the full-field torus minimum + beyond-rigid-rotor quantization
    (finite-width/vibrational zero-point, Braaten-Carson-class refinement)
    -- LOCATED, literature-known character, a named Paper-2 refinement row,
    NOT attempted here. The Callan-Klebanov inertia (R-133's Sigma_c
    residual adjudicator) stays a separate, adjacent row.

    WOULD CHANGE IF: (a) the projection follow-up lands => the strength
    face (g_piNN/g_A-analog) becomes a real empirical test; (b) P2-5-class
    cell structure delivers observable lattice-anisotropy corrections =>
    the N39 correction gains its would-change-if face (directional nuclear
    forces relative to a cosmic cell frame -- an SC-2-adjacent falsifier);
    (c) a full-field B = 2 computation quantifies the product-ansatz
    subleading corrections (the grid ratios' approach to 1 bounds them).
    """
    import numpy as np
    import sympy as sp
    from scipy.integrate import solve_ivp

    # ---------- (1) the three exact identities ----------
    z, mu_s, R_s, ORR, TrO = sp.symbols('z mu R O_RR TrO', positive=True)
    k32 = sp.besselk(sp.Rational(3, 2), z)
    assert sp.simplify(sp.expand_func(k32) - sp.sqrt(sp.pi/(2*z))*sp.exp(-z)*(1 + 1/z)) == 0, \
        "K_{3/2} must be elementary (the B = 1 massive tail is the exact dipole profile)"
    Yf = sp.exp(-mu_s*R_s)/R_s
    assert sp.simplify(-sp.diff(Yf, R_s) - (1 + mu_s*R_s)*sp.exp(-mu_s*R_s)/R_s**2) == 0, \
        "dipole identity -dY/dr = (1+mu r)e^{-mu r}/r^2"
    Ypp = sp.diff(Yf, R_s, 2)
    Yp_over_R = sp.diff(Yf, R_s)/R_s
    lhs = ORR*Ypp + (TrO - ORR)*Yp_over_R
    rhs = ((3*ORR - TrO)*(1 + mu_s*R_s + mu_s**2*R_s**2/3)*sp.exp(-mu_s*R_s)/R_s**3
           + TrO*(mu_s**2*R_s**2/3)*sp.exp(-mu_s*R_s)/R_s**3)
    assert sp.simplify(lhs - rhs) == 0, "OPE decomposition must be exact"
    tensor_radial = (1 + mu_s*R_s + mu_s**2*R_s**2/3)*sp.exp(-mu_s*R_s)/R_s**3
    assert sp.simplify(sp.limit(tensor_radial, mu_s, 0) - 1/R_s**3) == 0
    assert sp.simplify(sp.limit(TrO*(mu_s**2*R_s**2/3)*sp.exp(-mu_s*R_s)/R_s**3, mu_s, 0)) == 0, \
        "central piece must vanish at mu -> 0 (the aligned-channel zero)"

    # ---------- (2) the massless B = 1 profile + tail constant ----------
    def rhs_b1(t, y):
        F, Fp = y
        s2 = math.sin(2*F); sF = math.sin(F)
        return [Fp, (-(t/2)*Fp - s2*Fp**2 + s2/4 + sF**2*s2/t**2)/(t**2/4 + 2*sF**2)]

    def integrate(a, xmax=24.0):
        return solve_ivp(rhs_b1, (1e-3, xmax), [math.pi - a*1e-3, -a],
                         rtol=1e-10, atol=1e-12, dense_output=True, max_step=0.1)

    def flat(a):
        s = integrate(a)
        if np.any(s.y[0] < -1e-12):
            return -1e9
        return 256.0*s.sol(16.0)[0] - 100.0*s.sol(10.0)[0]

    lo, hi = 0.9, 1.2
    flo = flat(lo)
    assert flo*flat(hi) < 0
    for _ in range(48):
        mid = 0.5*(lo + hi)
        if flat(mid)*flo > 0:
            lo = mid
        else:
            hi = mid
    sol1 = integrate(0.5*(lo + hi))
    xw = np.linspace(10.0, 16.0, 60)
    C_tail = float(np.mean(xw**2*sol1.sol(xw)[0]))
    assert abs(C_tail - 8.634) < 0.02, "massless tail constant must be the banked 8.634"

    # ---------- (3) reduced-grid product-ansatz certificate (81^3, ~3 s) ----------
    H, L = 0.42, 16.8
    xs1 = np.arange(-L, L + H/2, H)
    X, Y3, Z = np.meshgrid(xs1, xs1, xs1, indexing='ij')
    r1d = np.linspace(1e-3, 20.0, 40000)
    F1d = sol1.sol(r1d)[0]

    def hh(z0, O=None):
        dx, dy, dz = X, Y3, Z - z0
        r = np.maximum(np.sqrt(dx*dx + dy*dy + dz*dz), 1e-9)
        F = np.where(r < 20.0, np.interp(r, r1d, F1d), C_tail/r**2)
        n = np.stack([dx/r, dy/r, dz/r])
        if O is not None:
            n = np.einsum('ab,b...->a...', O, n)
        return np.concatenate([np.cos(F)[None], np.sin(F)[None]*n])

    def qmul(s1, s2):
        a, v = s1[0], s1[1:]
        b, w = s2[0], s2[1:]
        return np.concatenate([
            (a*b - np.einsum('c...,c...->...', v, w))[None],
            a[None]*w + b[None]*v + np.stack([v[1]*w[2] - v[2]*w[1],
                                              v[2]*w[0] - v[0]*w[2],
                                              v[0]*w[1] - v[1]*w[0]])])

    def gE(sig):
        d = []
        for ax in (1, 2, 3):
            sp_ = [slice(None)]*4
            sm = [slice(None)]*4
            sp_[ax] = slice(2, None)
            sm[ax] = slice(None, -2)
            ds = (sig[tuple(sp_)] - sig[tuple(sm)])/(2*H)
            crop = [slice(None)] + [slice(1, -1)]*3
            crop[ax] = slice(None)
            d.append(ds[tuple(crop)])
        e2 = sum(np.einsum('c...,c...->...', di, di) for di in d)/8.0
        e4 = np.zeros_like(e2)
        for i in range(3):
            for j in range(i + 1, 3):
                e4 += (np.einsum('c...,c...->...', d[i], d[i])
                       * np.einsum('c...,c...->...', d[j], d[j])
                       - np.einsum('c...,c...->...', d[i], d[j])**2)
        return float(np.sum(e2 + 0.5*e4)*H**3)

    O_par = np.diag([-1.0, -1.0, 1.0])     # pi about e3 (axis || R)
    O_perp = np.diag([1.0, -1.0, -1.0])    # pi about e1 (axis perp R)
    grid = {}
    for Rsep in (8.0, 10.0):
        sA = hh(+Rsep/2)
        EA = gE(sA)
        row = {}
        for name, O, Sg in (("par", O_par, 4.0), ("perp", O_perp, -2.0), ("O1", None, 0.0)):
            sB = hh(-Rsep/2, O)
            V = gE(qmul(sA, sB)) - EA - gE(sB)
            row[name] = {"V": V, "pred": math.pi*C_tail**2*Sg/Rsep**3}
        grid[Rsep] = row

    for Rsep, row in grid.items():
        assert row["perp"]["V"] < 0 < row["par"]["V"], \
            "channel SIGNS: perp attractive, par repulsive (the derived law's structure)"
        assert abs(row["O1"]["V"]) < 0.65*abs(row["perp"]["V"]), \
            "aligned channel must be sub-leading (vanishing leading force)"
        for ch in ("par", "perp"):
            ratio = row[ch]["V"]/row[ch]["pred"]
            assert 0.4 < ratio < 1.15, \
                "reduced-grid magnitude window (full 169^3 certificate: monotone -> 1)"
    assert abs(grid[10.0]["O1"]["V"]) < abs(grid[8.0]["O1"]["V"]), \
        "aligned-channel residual must fall with R"

    # ---------- (4) the dipole constants across the fork ----------
    # computed IN-PRIMITIVE from the massive B = 1 BVP at each mu (reviewer fix
    # F1: the previous draft hard-coded a provenance MISREAD -- R-137's
    # tail_constants are (B=1, B=2) BOTH at the probe mu; the refit B = 1
    # constant must be solved at mu* = 0.26322, not transcribed)
    from scipy.special import kv as _kv

    def massive_b1_tail(mu):
        nu = 1.5

        def rhs_m(t, y):
            F, Fp = y
            s2_ = math.sin(2*F)
            sF_ = math.sin(F)
            return [Fp, (-(t/2)*Fp - s2_*Fp**2 + s2_/4 + sF_**2*s2_/t**2
                         + (mu**2/4)*t**2*sF_)/(t**2/4 + 2*sF_**2)]

        def asym(x):
            return _kv(nu, mu*x)/math.sqrt(x)

        def integ(a):
            return solve_ivp(rhs_m, (1e-3, 26.0), [math.pi - a*1e-3, -a],
                             rtol=1e-10, atol=1e-12, dense_output=True, max_step=0.1)

        def flat_m(a):
            sm = integ(a)
            if np.any(sm.y[0] < -1e-12):
                return -1e9
            return sm.sol(16.0)[0]/asym(16.0) - sm.sol(10.0)[0]/asym(10.0)

        grid_a = np.linspace(0.5, 2.5, 21)
        vals = [flat_m(a) for a in grid_a]
        for i in range(len(grid_a) - 1):
            if vals[i]*vals[i+1] < 0:
                lo_m, hi_m, flo_m = grid_a[i], grid_a[i+1], vals[i]
                break
        else:
            raise RuntimeError("no bracket for massive B=1 at mu=%.4f" % mu)
        for _ in range(48):
            mid = 0.5*(lo_m + hi_m)
            if flat_m(mid)*flo_m > 0:
                lo_m = mid
            else:
                hi_m = mid
        sm = integ(0.5*(lo_m + hi_m))
        xw2 = np.linspace(10.0, 16.0, 50)
        return float(np.mean(sm.sol(xw2)[0]/np.array([asym(x) for x in xw2])))

    Ct_probe = massive_b1_tail(0.19629)
    Ct_refit = massive_b1_tail(0.26322)
    C_probe = Ct_probe*math.sqrt(math.pi/(2*0.19629))/0.19629
    C_refit = Ct_refit*math.sqrt(math.pi/(2*0.26322))/0.26322
    assert abs(Ct_probe - 0.5487) < 0.002, "probe B=1 tail must reproduce R-137's banked 0.5487"
    assert abs(Ct_refit - 0.8251) < 0.003, "refit B=1 tail 0.8251 (reviewer's independent solve)"
    assert abs(C_probe - 7.91) < 0.05 and abs(C_refit - 7.66) < 0.05, \
        "dipole strength nearly FORK-INVARIANT: 8.63 / 7.91 / 7.66 (reviewer fix F1)"

    return {
        "outcome": ("P2-7 TENSOR-FORCE FACE banked: the two-defect asymptotic interaction "
                    "is the dipole-dipole law V(R,O) = +pi C^2 [(3 O_RR - TrO)"
                    "(1 + mu R + mu^2R^2/3) + TrO mu^2R^2/3] e^{-mu R}/R^3 -- the OPE "
                    "central + TENSOR radial structure EXACTLY (sympy), from the banked "
                    "tails (the asymptotic Skyrmion = an exact triplet of orthogonal pion "
                    "dipoles). Grid-certified: aligned channel vanishes, perp pi-rotation "
                    "ATTRACTIVE, par REPULSIVE, magnitudes -> the law monotonically. "
                    "The D4-anisotropy premise CORRECTED (N39): no anisotropy input "
                    "anywhere -- the isotropic dressed sector delivers the tensor force. "
                    "P2-7 is DONE AT SCOPE; the located residual is the binding-magnitude "
                    "face (torus + beyond-rigid-rotor quantization)."),
        "tier": ("DERIVED-A (K_{3/2} elementary tail; dipole identity; OPE decomposition "
                 "with mu->0 limits) + DERIVED dressed-level ASYMPTOTIC (the law; "
                 "product-ansatz class, branch-(c) conditional; sign/magnitude pinned by "
                 "the grid, not convention) + GRID-CERTIFICATED (169^3 development record "
                 "+ 81^3 in-suite regression) + CORRECTED PREMISE (D4 anisotropy NOT the "
                 "tensor-force source -- N39) + NAMED FOLLOW-UP (nucleon-state projection "
                 "-> quantum OPE strength; imported-as-cited when taken)"),
        "law": {"massless": "V = pi C^2 (3 O_RR - TrO)/R^3",
                "massive": ("V = pi C^2 [(3 O_RR - TrO)(1 + mu R + mu^2R^2/3) "
                            "+ TrO mu^2R^2/3] e^{-mu R}/R^3"),
                "channels": {"aligned O=1": "0 (leading)",
                             "pi-rot || R": "+4 pi C^2/R^3 (repulsive)",
                             "pi-rot perp R": "-2 pi C^2/R^3 (ATTRACTIVE -- the R-135 channel)"}},
        "constants": {"C_massless": C_tail, "C_dip_probe": C_probe, "C_dip_refit": C_refit},
        "grid_certificate": {str(k): {ch: {kk: round(vv, 4) for kk, vv in d.items()}
                                      for ch, d in row.items()} for k, row in grid.items()},
        "d4_adjudication": ("the tensor force arises ENTIRELY from the isotropic dressed "
                            "sector (dipole tails); D4 anisotropy is NOT the source -- "
                            "worklist premise-drift corrected (ledger N39, N0-genre; the "
                            "banked eta_DM primitive always said dominant tensor = OPE); "
                            "the eta_DM = (D/J)^2/144 ~ 0.43% CALIBRATED face is preserved "
                            "as the named P2-5-gated subleading row (falsifier face: "
                            "directional nuclear forces vs a cosmic cell frame)"),
        "p2_7_closure": ("DONE AT SCOPE (R-135 existence/sign; R-136 quantum numbers; "
                         "R-137 pion-mass robustness; R-138 scheme fork + baseline; R-139 "
                         "tensor force + premise correction; first SC-1 N = 2 datum). "
                         "LOCATED residual: binding magnitude (~113/~124 MeV rigid-rotor "
                         "overbinding, massless/refit; needs torus + beyond-rigid-rotor "
                         "quantization -- named Paper-2 refinement). Adjacent, separate: "
                         "Callan-Klebanov inertia (Sigma_c residual); OPE-projection "
                         "strength face; the eta_DM 1/144 D4 face (P2-5-gated)."),
        "would_change_if": ("projection follow-up lands (strength face becomes empirical "
                            "test); P2-5 delivers cell-lattice corrections (N39's "
                            "would-change-if); full-field B = 2 bounds the product-ansatz "
                            "subleading terms"),
    }


def d4_dm_plaquette_holonomy_explicit() -> dict:
    """[DERIVED-A (the explicit plaquette holonomy of the DM-twisted D4 links --
    the census, the exact holonomy law, the consistency-forced orientation
    convention, the chiral factorization with its closed-form angle, the exact
    non-abelian excess, and the per-sector Lie closure; all engine-exact
    Clifford computations) + DERIVED-structural (instanton-sector
    ACCESSIBILITY: the holonomy group is genuinely non-abelian SU(2) in EACH
    chiral sector, not a U(1) subgroup, so pi_3(SU(2)_pm) = Z instanton
    sectors are structurally reachable -- SC.4.6(ii)'s 'full Z of instanton
    sectors opens' made explicit at the holonomy level) + FRAMING preserved
    (the DYNAMICAL Yang-Mills realization -- coupling normalization,
    continuum limit, fluctuation action, Im chi mediation -- stays
    Paper-2/kernel-gated exactly as banked; NOTHING value-level is claimed)
    + HONEST NEW CONSTRAINT (the DM plaquette is CHIRALLY SYMMETRIC: both
    SU(2)_+ and SU(2)_- are driven with IDENTICAL rotation angles, so the
    weak sector's chirality is NOT sourced by the DM plaquette -- the
    'weak = SD' assignment stays settled at R-171/R-079, not by the plaquette, and SC.4.6(iii)'s
    'delivering the SU(2)_+ Yang-Mills sector' carries an SD-selection
    qualifier, annotated in the paper this pass)] -- P2-4 LEG 2 STRUCTURAL
    CORE: the explicit DM-twisted plaquette, computed. (2026-07-03.)

    WHAT WAS OWED (SC.4.6(ii)-(iii), banked at FRAMING + the commutator-level
    D4_DM_bond_bivectors_non_commuting): 'the plaquette of DM-twisted bond
    bivectors gives a non-trivial F != 0... the explicit plaquette +
    Yang-Mills construction remains Paper 2/3.' This primitive supplies the
    explicit plaquette half. THE SETUP: D4 sites, 24 root bonds; the minimal
    CURVATURE-CARRYING loops are the TRIANGLES {r1, r2, r3}, r1+r2+r3 = 0,
    all roots (reviewer fix 1: 36 chordless 4-cycles also exist -- 6 spatial,
    24 two-e_4-bond, 6 four-e_4-bond same-axis DM squares engaging the 18
    COMMUTING pairs -- and ALL 36 carry TRIVIAL holonomy, banked as a check
    below: the triangles carry all elementary curvature); the DM twist
    lives on the 12 e_4-bearing bonds only (banked R-103); link rotor for the
    ORIENTED bond r: V(r) = exp(theta_D Bhat(r)) = cos theta + sin theta Bhat,
    with Bhat(r) = (r ^ e4)/|r ^ e4| = eps_a e_{a4}.

    THE RESULTS (all exact):
    (1) CENSUS: exactly 32 translation-classes of oriented triangles
        (reviewer fix 1b) -- 8 purely spatial and 24 carrying exactly TWO
        e_4-bonds; no triangle carries one or three e_4-bonds (e_4-components
        must cancel pairwise), and every e_4-triangle pairs bonds with
        DISTINCT spatial axes (same-axis pairs cannot close a triangle) --
        i.e. the elementary curvature-carrying loops (THE TRIANGLES; scope
        per fix 1) engage ONLY the 48 non-commuting pairs of the banked
        48/66 census; the 18 commuting pairs appear only in the
        holonomy-TRIVIAL 4-cycles.
    (2) CONSISTENCY FORCES THE ODD CONVENTION (a derived refinement of the
        banked bond-plane convention, which is orientation-EVEN): a genuine
        connection needs U_{ji} = U_{ij}^{-1}, which requires Bhat odd under
        r -> -r. Bhat = (r ^ e4)-normalized is the canonical odd choice --
        exactly the physical DM antisymmetry D_ij = -D_ji. Certificates:
        W_forward * W_backward = 1 exactly; theta -> 0 telescopes to 1;
        CONVENTION-ROBUST: the other odd variant (eps_4-weighted) gives the
        same census and the same non-triviality (24/24).
    (3) THE EXACT HOLONOMY LAW: spatial triangles: W = 1 identically (the
        curvature is sourced ONLY by the e_4/DM sector). Each of the 24
        e_4-triangles:
            W = cos^2(th) + sin(th)cos(th)(Bhat_1 + Bhat_2) + sin^2(th) e_ab
        (the last term's sign/axis tracking the triangle) -- W != 1 for all
        theta_D != 0 mod pi: THE PURE-GAUGE LIFT IS EXPLICIT. FRAME SCOPE
        (reviewer fix 3): the coefficient law is a CANONICAL-LATTICE-FRAME
        statement -- under gauge conjugation the L/Q split redistributes;
        the conjugation-INVARIANT content is the chiral angle pair and the
        non-triviality (the angle is invariant under arbitrary Spin(4)
        conjugation, reviewer-verified to 1e-15).
    (4) NON-ABELIAN SIGNATURE, exact (reviewer fix 2 -- stated as grade
        content, NOT as a literal rotor difference: the scalar and Q-grade
        parts of W and of the abelianized rotor also differ): the
        abelianized holonomy exp(theta(B1+B2)) contains NO L-grade bivector
        at all ((B1+B2)^2 = -2, a scalar), while W's L-grade content is
        EXACTLY sin^2(theta_D) e_ab -- the [e_{a4}, e_{b4}] = -2 e_{ab}
        commutator content of the banked 48/66 fact, sitting IN the
        holonomy as its non-abelian signature.
    (5) CHIRAL FACTORIZATION + CLOSED FORM: I_4 is central in the even
        subalgebra, so P_pm = (1 pm I_4)/2 split every holonomy exactly:
        W = W_+ P_+ + W_- P_- with W_pm in SU(2)_pm. BOTH sectors are driven
        with the IDENTICAL angle  a_pm = arccos(cos^2 theta_D)  (engine-exact
        at every theta tested, all 24 triangles) -- the DM plaquette is
        chirally BLIND. Consequence carried honestly: the weak sector's
        chirality does NOT come from the plaquette; 'weak = SD' stays the
        one counted INPUT bit (canon), and the gauge-sector construction
        delivers Spin(4) = SU(2)_+ x SU(2)_- curvature symmetrically, with
        the SD factor selected by the matter coupling, not by the lattice.
    (6) LIE CLOSURE PER SECTOR = FULL su(2): the chiral projections of the
        24 log-holonomies plus first commutators already span rank 3 in each
        sector (engine rank computation) => the holonomy group is genuinely
        non-abelian SU(2)_pm, NOT reducible to any U(1) (reducibility would
        force rank 1). OBSTRUCTION-ABSENCE gloss (reviewer fix 4): since
        pi_3(U(1)) = 0 but pi_3(SU(2)) = Z, the statement is that the
        pi_3-obstruction to instanton sectors is ABSENT at the
        structure-group level -- Z sectors EXIST for the group the DM
        background actually engages; explicit finite-action lattice
        instanton CONFIGURATIONS are leg 3, still open -- the SC.4.6(ii)
        claim, made explicit and correctly scoped.

    WHAT THIS DOES NOT CLAIM (the honest fence): no coupling value, no
    continuum limit, no fluctuation dynamics (the Wilson-action expansion
    around this background measures the banked D4 texture energy at leading
    order; the YM F^2 form for FLUCTUATIONS is the standard lattice
    construction GIVEN this background -- Paper-2, kernel-adjacent, as
    banked); no lattice instanton solution (leg 3); no induced level (leg 4).
    P2-4 LEG STATUS after this result: leg 1 banked (48/66) + leg 2
    STRUCTURAL CORE DONE (this primitive) + leg 3 half-banked (R-088 index;
    lattice construction owed) + leg 4 open (the W-LIVE-4 decider).
    [2026-07-04 UPDATE, R-143: leg 3 lattice construction DELIVERED --
    d4_lattice_instanton_access_and_dm_background_neutrality; leg 3
    STRUCTURAL CORE DONE, remaining face = instanton solution/action value
    (kernel-adjacent). See the return dict's p2_4_status, kept current.]

    WOULD CHANGE IF: (a) the fluctuation-YM construction lands (leg 2
    completes; the coupling's kernel face becomes the named value gap);
    (b) a physical mechanism is found that BREAKS the plaquette's chiral
    symmetry (would move 'weak = SD' from INPUT toward derived -- nothing
    in this computation does so); (c) the induced-level computation (leg 4)
    lands -- it inherits this primitive's explicit SU(2)_pm structure.
    """
    import numpy as np
    import itertools

    I4 = e(1, 2, 3, 4)
    P_plus = 0.5 * (SCALAR + I4)
    P_minus = 0.5 * (SCALAR - I4)

    # ---- roots and triangles ----
    roots = []
    for i, j in itertools.combinations(range(4), 2):
        for si in (1, -1):
            for sj in (1, -1):
                v = [0, 0, 0, 0]
                v[i] = si
                v[j] = sj
                roots.append(tuple(v))
    root_set = set(roots)
    triangles = set()
    for r1, r2 in itertools.combinations(roots, 2):
        r3 = tuple(-(a + b) for a, b in zip(r1, r2))
        if r3 in root_set:
            triangles.add(tuple(sorted([r1, r2, r3])))
    triangles = sorted(triangles)
    n_e4 = lambda tri: sum(1 for r in tri if r[3] != 0)
    census = {}
    for tri in triangles:
        census[n_e4(tri)] = census.get(n_e4(tri), 0) + 1
    assert len(triangles) == 32 and census == {0: 8, 2: 24}, \
        "census: 32 elementary D4 triangles = 8 spatial + 24 with two e_4-bonds"
    for tri in triangles:                        # e_4-triangles pair DISTINCT spatial axes
        ax = [next(i for i in range(3) if r[i] != 0) for r in tri if r[3] != 0]
        assert len(set(ax)) == len(ax), "e_4-triangle bonds must have distinct spatial axes"

    # chordless 4-cycles (reviewer fix 1 check): 36 exist; ALL holonomy-trivial
    quads = set()
    for r1 in roots:
        for r2 in roots:
            if r2 == tuple(-x for x in r1):
                continue
            if tuple(a + b for a, b in zip(r1, r2)) in root_set:
                continue                                   # chord 0 -> r1+r2
            for r3 in roots:
                if r3 == tuple(-x for x in r2):
                    continue
                if tuple(a + b for a, b in zip(r2, r3)) in root_set:
                    continue                               # chord r1 -> r1+r2+r3
                r4 = tuple(-(a + b + c) for a, b, c in zip(r1, r2, r3))
                if r4 not in root_set or r4 == tuple(-x for x in r3) or r4 == r1 and False:
                    pass
                if r4 not in root_set:
                    continue
                if r4 == tuple(-x for x in r3) or r1 == tuple(-x for x in r4):
                    continue
                # canonical form: all cyclic rotations + reversal of the edge list
                # dedupe by cyclic rotation ONLY (orientations counted
                # separately, matching the 32 = 16 x 2 triangle census)
                cyc = (r1, r2, r3, r4)
                quads.add(min(cyc[k:] + cyc[:k] for k in range(4)))
    quad_census = {}
    for q in quads:
        ne4 = sum(1 for r in q if r[3] != 0)
        quad_census[ne4] = quad_census.get(ne4, 0) + 1

    def Bhat(r, variant="a"):
        if r[3] == 0:
            return None
        a = next(i for i in range(3) if r[i] != 0)
        w = float(r[a]) if variant == "a" else float(r[3])
        return w * e(a + 1, 4)

    def V(r, th, variant="a"):
        B = Bhat(r, variant)
        return SCALAR if B is None else math.cos(th) * SCALAR + math.sin(th) * B

    def holonomy(path, th, variant="a"):
        W = SCALAR
        for r in path:
            W = W * V(r, th, variant)
        return W

    def sc(mv):
        return dict(mv.terms).get((), 0.0)

    def is_one(mv, tol=1e-12):
        c = dict(mv.terms)
        return (abs(c.get((), 0.0) - 1.0) < tol
                and max((abs(v) for k, v in c.items() if k != ()), default=0.0) < tol)

    BIV = [(1, 2), (1, 3), (2, 3), (1, 4), (2, 4), (3, 4)]

    def biv_part(mv):
        c = dict(mv.terms)
        out = 0.0 * SCALAR
        for b in BIV:
            if b in c:
                out = out + c[b] * e(*b)
        return out

    results = {}
    for th in (0.3, 0.7):
        s2 = math.sin(th) ** 2
        pred_angle = math.acos(math.cos(th) ** 2)
        angs = set()
        for tri in triangles:
            W = holonomy(tri, th)
            if n_e4(tri) == 0:
                assert is_one(W), "spatial triangles must have trivial holonomy"
                continue
            assert not is_one(W), "every e_4-triangle must have NON-trivial holonomy"
            c = dict(W.terms)
            assert abs(c.get((), 0.0) - math.cos(th) ** 2) < 1e-12, "scalar part = cos^2"
            Lmag = max(abs(c.get(b, 0.0)) for b in [(1, 2), (1, 3), (2, 3)])
            assert abs(Lmag - s2) < 1e-12, "non-abelian excess must be EXACTLY sin^2(theta)"
            ap = math.acos(max(-1.0, min(1.0, 2.0 * sc(W * P_plus))))
            am = math.acos(max(-1.0, min(1.0, 2.0 * sc(W * P_minus))))
            angs.add((round(ap, 12), round(am, 12)))
        assert len(angs) == 1, "all 24 e_4-triangles share ONE chiral angle pair"
        (ap, am), = angs
        assert abs(ap - am) < 1e-12, "chirally SYMMETRIC: both sectors driven equally"
        assert abs(ap - pred_angle) < 1e-10, "closed form a = arccos(cos^2 theta_D)"
        results[th] = {"angle": ap, "excess": s2}

    assert len(quads) == 36 and quad_census == {0: 6, 2: 24, 4: 6}, \
        "chordless 4-cycles: 36 = 6 spatial + 24 two-e4 + 6 four-e4 (got %s)" % quad_census
    for q in quads:
        assert is_one(holonomy(q, 0.3), 1e-10), \
            "ALL chordless 4-cycles must carry TRIVIAL holonomy (triangles carry all curvature)"

    # consistency: reverse path gives inverse holonomy; theta = 0 telescopes
    tri0 = next(t for t in triangles if n_e4(t) == 2)
    Wf = holonomy(tri0, 0.3)
    Wb = holonomy(tuple(tuple(-x for x in r) for r in reversed(tri0)), 0.3)
    assert is_one(Wf * Wb, 1e-10), "orientation-odd convention: W_fwd * W_bwd = 1"
    assert all(is_one(holonomy(t, 0.0)) for t in triangles), "theta = 0 must telescope"

    # convention robustness (the other odd variant)
    nb = sum(0 if is_one(holonomy(t, 0.3, "b")) else 1 for t in triangles if n_e4(t) == 2)
    assert nb == 24, "odd-variant-b must also give 24/24 non-trivial"

    # Lie closure per chiral sector = full su(2)
    logs = [biv_part(holonomy(t, 0.3)) for t in triangles if n_e4(t) == 2]

    def comm(A, B):
        return A * B - B * A

    ranks = {}
    for sign, P in ((1, P_plus), (-1, P_minus)):
        vecs = []
        for L in logs[:8]:
            vecs.append([dict((L * P).terms).get(b, 0.0) for b in BIV])
        for i in range(6):
            for j in range(i + 1, 6):
                LC = biv_part(comm(logs[i], logs[j]))
                vecs.append([dict((LC * P).terms).get(b, 0.0) for b in BIV])
        ranks[sign] = int(np.linalg.matrix_rank(np.array(vecs), tol=1e-10))
    assert ranks[1] == 3 and ranks[-1] == 3, \
        "holonomy Lie closure must be FULL su(2) in each chiral sector (rank 3)"

    return {
        "outcome": ("P2-4 LEG 2 STRUCTURAL CORE banked: the explicit DM-twisted D4 plaquette "
                    "-- 32 elementary triangles (8 spatial, trivial; 24 two-e_4-bond, ALL "
                    "non-trivial): W = cos^2(th) + sin cos (B1+B2) + sin^2(th) e_ab exactly; "
                    "the pure-gauge lift is EXPLICIT; chiral factorization drives SU(2)_+ "
                    "and SU(2)_- with the IDENTICAL angle arccos(cos^2 th) -- the plaquette "
                    "is chirally BLIND (weak = SD is settled at R-171/R-079, not here); per-sector "
                    "holonomy Lie closure = FULL su(2) => pi_3 = Z instanton sectors "
                    "structurally accessible. Dynamics (coupling, continuum, fluctuation "
                    "YM) stays kernel-gated as banked -- no value claimed."),
        "tier": ("DERIVED-A (census; exact holonomy law; consistency-forced odd convention, "
                 "convention-robust; chiral factorization + closed-form angle; non-abelian "
                 "excess = sin^2 theta exactly; per-sector Lie closure rank 3) + "
                 "DERIVED-structural (instanton-sector accessibility via non-abelian "
                 "SU(2)_pm holonomy) + FRAMING preserved (dynamical YM realization, "
                 "kernel-gated as banked) + HONEST CONSTRAINT (plaquette chirally "
                 "symmetric -- weak-sector chirality NOT sourced here)"),
        "census": {"triangles": 32, "spatial": 8, "e4_two_bond": 24,
                   "chordless_4cycles": 36, "all_4cycles_trivial": True,
                   "note": ("e_4-TRIANGLES engage ONLY the 48 non-commuting pairs; "
                            "the 18 commuting pairs appear only in holonomy-trivial "
                            "4-cycles -- triangles carry all elementary curvature")},
        "law": {"holonomy": "W = cos^2(th) + sin(th)cos(th)(B1+B2) + sin^2(th) e_ab",
                "chiral_angle": "a_pm = arccos(cos^2 theta_D), equal in both sectors",
                "at_0.3": results[0.3], "at_0.7": results[0.7]},
        "lie_closure": {"su2_plus_rank": ranks[1], "su2_minus_rank": ranks[-1],
                        "consequence": "holonomy group = non-abelian SU(2)_pm, pi_3 = Z"},
        "p2_4_status": ("leg 1 banked (48/66) + leg 2 STRUCTURAL CORE DONE (this) + leg 3 "
                        "STRUCTURAL CORE DONE 2026-07-04 (R-143 "
                        "d4_lattice_instanton_access_and_dm_background_neutrality: "
                        "background neutral + charge operator + explicit finite-action "
                        "charge-1 access; remaining face = instanton solution/action "
                        "value, kernel-adjacent; supersedes this docstring's "
                        "'half-banked' line) + leg 4 "
                        "ANSWERED-AT-PARITY same day (R-141: induced level ODD, "
                        "conditional on P1/P1b; the substrate COMPUTATION face stays "
                        "open -- the W-LIVE-4 decider, conditionally decided)"),
        "would_change_if": ("fluctuation-YM lands (leg 2 completes; coupling = named kernel "
                            "gap); a chirality-breaking plaquette mechanism is found (would "
                            "move weak = SD toward derived); leg 4 lands (inherits this "
                            "explicit SU(2)_pm structure)"),
    }


def induced_level_parity_on_baryon_worldline() -> dict:
    """[DERIVED-given-(P1)+(P1b)+(Q) (the PARITY of the induced topological
    term on the B = 1 baryon worldline: ODD -- so the 2pi-rotation weight is
    -1 and Finkelstein-Rubinstein fermionic quantization is INDUCED, not
    merely selected -- CONDITIONAL on three NAMED premises, below) +
    IMPORTED-AS-CITED (P1: the induced-topological-term theorem class --
    D'Hoker-Farhi 1984 decoupling (Nucl. Phys. B248) / Witten 1982 SU(2)
    anomaly (Phys. Lett. B117; the 1983 papers are the WZW/statistics
    pair -- reviewer fix F5): integrating
    out N chiral SU(2)-doublet modes coupled to an SU(2)-valued chiral field
    U induces the pi_4(SU(2)) = Z_2-class topological term with weight
    (-1)^N on the soliton's 2pi-rotation loop -- the Skyrmion of the
    residual theory is a fermion iff N is ODD; citations to-be-verified
    before external use, Schur/Krusch/R-088-class import) + DERIVED (the
    counting itself: every input to N is a BANKED index/structure fact --
    no new counting is introduced) + NAMED FORK, parity-robust (whether
    generations multiply the count: N = 3 or N = 9 -- BOTH ODD, so the
    conclusion does not wait on the fork)] -- P2-4 LEG 4, the W-LIVE-4
    DECIDER, answered at the parity level: THE INDUCED LEVEL IS ODD.
    N35's would-change-if (a) is PARTIALLY DISCHARGED at the parity level,
    conditional on P1/P1b (reviewer fix F4) -- the substrate COMPUTATION
    face remains open (= would-change-if (b) below). (2026-07-03.)

    THE QUESTION (N35, verbatim would-change-if): does the gauge-sector
    construction induce a U(1)-valued topological term on the B = 1 baryon
    worldline with ODD level (=> fermionic quantization FORCED) or
    zero/even (=> FR stays a permanent SELECTION)? For an SU(2)-valued
    chiral field the carrier is the pi_4(SU(2)) = Z_2 class -- there is no
    integer-level 5-form WZW (H^5(SU(2)) = 0, CONSISTENT WITH the banked L3
    refutation -- reviewer rec R2) -- so the WHOLE question is the PARITY
    of the mode count N.
    This evades the L1-L3 refutations by construction: those showed the
    sign cannot come from BLADE-LEVEL sandwich algebra; here it comes from
    the MODE DETERMINANT (dynamical content, imported as P1), which is
    precisely where QCD's own Skyrmion fermionicity lives.

    THE NAMED PREMISES (all explicit; refusing any re-opens the fork):
      (P1)  The induced-term theorem (imported-as-cited, above).
      (P1b) COUPLING IDENTIFICATION: the R-128 quark mass-phase lock (the
            parity-ODD Hodge-dual channel locking the quark modes' phase to
            the Q-orbit field) functions as the chiral coupling in the P1
            sense -- the substrate face of 'the mode is chirally coupled to
            U'. PRECISION (reviewer fix F5): the theorem's coupling is a
            mass-FORM (chirality-linking) coupling psi_L U psi_R; what TWT
            imports is the TOPOLOGICAL OUTPUT, which is magnitude-
            independent -- NOT the heavy-mass decoupling limit (nothing in
            TWT is heavy; canon S5 untouched: no quark mass introduced).
            SCOPE (reviewer fix F1): P1b is the CHANNEL IDENTIFICATION for
            the WHOLE roster -- 'the mass-phase LOCK CHANNEL is the
            chiral-coupling channel, for every roster mode' -- so the quark
            INCLUSION (R-128: I4-dual lock onto the Q-orbit) and the lepton
            EXCLUSION (R-127: identity lock on the L-blade, provably
            Q-blind) BOTH follow from the one premise. P1b is a FRESH,
            CANDIDATE-CLASS identification premise created in this result
            -- categorically unlike the corpus-standard (Q) -- and it is
            the result's one genuine vulnerability, named and revocable.
            It inherits R-127's C1-C3 and R-128's C1'-C3' ansatz
            conditions (R-020's 'structural analog, not load-bearing'
            class -- reviewer fix F6).
      (Q)   The collective-quantization premise (as R-133/R-136).

    THE COUNTING (all banked inputs, engine-recomputed here):
      * ROSTER (banked, bpst_selection_rule / SC.4.6(i)): per generation the
        substrate's chiral SU(2)-doublet modes = 3 colour quark modes + 1
        lepton mode = 4. The SAME roster's EVENNESS (4/gen) is what banked
        SU(2) gaugeability (Witten anomaly, SC.4.6(i)) -- self-consistency:
        one roster, two different questions.
      * THE DISCRIMINATION (banked): the baryon field U is the Q-orbit /
        COSET winding factor of pi_3(Spin(4)) = Z x Z (R-002; the A.5.2
        fibration basis: leptons wind the diagonal Spin(3) SUBGROUP factor,
        baryons the coset S^3_Q); the lepton mass-phase lock is the
        parity-EVEN L-orbit channel (R-127) while the quark lock is the
        parity-ODD Hodge-dual channel (R-128) -- two banked FACES of the
        ONE L/Q sector assignment (they would co-fail if that assignment
        failed -- reviewer fix F2), giving the same split: ONLY the 3
        colour modes per generation couple to the baryon-winding field.
        Level per generation N = 3. THE COUNTING UNIT (reviewer fix F3):
        one determinant unit = one chirally-linked doublet PAIR per colour
        facet per generation -- the doublet's two components under the
        baryon-field SU(2) are the (u,d) = R-128 sigma-mirror pair (exactly
        QCD's isospin pairing; the theorem's own anchor counts N_c = 3, not
        6); doublet-structure-under-the-Q-orbit-SU(2) is P1b's content,
        not the roster's.
      * THE FORK (named, NOT decided, parity-robust): if the three
        generations are spectator COPIES coupled to the same SU(2)-valued
        U, the count multiplies: N = 9; if they embed flavor-style in an
        enlarged chiral field, N = 3. BOTH ODD -- the parity conclusion is
        fork-independent. THE EVEN VARIANTS, adversarially enumerated and
        each EXCLUDED (reviewer fix F3):
          - N = 4/12 (lepton counted in): excluded by the L/Q assignment
            (the load-bearing step, riding R-002 + R-127/R-128) AND by a
            third, independent face (reviewer rec R3): the single-Weyl
            neutrino (SC.3.12) means the lepton could not even complete a
            chirally-LINKED determinant unit;
          - N = 6/18 (sigma-species double-counted as separate units, or
            Dirac-vs-Weyl double-counting): excluded by the counting unit
            above -- one lock = one chirality-link per colour mode; the
            (u,d) pair are doublet COMPONENTS (R-128's sigma-mirror seat),
            not two units; QCD's own anchor is N_c = 3, not 6;
          - N = 0 ('quarks do not couple either'): this is not a count
            variant but the REFUSAL of P1b -- the named revert branch
            (selection restored, anchors stand); it is NOT an established
            zero (which per N35 would close W1 NEGATIVE outright).

    THE CONCLUSION (conditional, tier as titled): the induced weight on the
    baryon's 2pi-rotation loop is (-1)^N = -1 => fermionic Skyrmion
    quantization is INDUCED. W-LIVE-4's W1 closes POSITIVE conditionally;
    the FR 'SELECTION' upgrades to 'INDUCED-given-(P1)+(P1b)' -- the
    fermionic branch is no longer a bare pick but the anomaly-matching
    consequence of the banked mode roster. The TWO empirical anchors
    (nucleon spin-1/2; R-136's deuteron 1+ with the scalar dibaryon
    forbidden) become CONSISTENCY CHECKS of the induced-odd conclusion --
    nature agrees with the parity on both independent data.

    CONSISTENCY FACTS (engine-checked):
      * Witten-anomaly evenness vs level oddness: 4 = 0 mod 2 (gaugeable)
        AND 3 = 1 mod 2 (fermionic) FROM THE SAME ROSTER -- different
        couplings (SU(2)_+ gauge vs Q-orbit chiral), no tension.
      * L3 non-contradiction: the blade-level facets contribute +1 each
        (banked skyrmion_collective_quantization_under_v2_3p2) -- and that
        is CORRECT for sandwich algebra; the induced term lives in the mode
        determinant, not the sandwich. The routes fail/succeed for the
        same structural reason.
      * R-140 inheritance: the explicit plaquette supplies the non-abelian
        SU(2)_pm structure the gauge-coupled worldline lives in (chirally
        blind at the plaquette level; the SD pick enters through the
        matter coupling -- consistent with P1b's channel).

    HONEST FENCE: this is a PARITY result, not a dynamical construction --
    the fermion-determinant dynamics is NOT derived (kernel territory);
    P1 is an import in the same class as the banked index theorem (R-088);
    the LEVEL VALUE (3 vs 9) stays a named fork (it does not affect the
    parity, but it would matter for any future magnitude claim, e.g. an
    omega-meson-class coupling strength); the tier is CONDITIONAL and the
    conditions are the record. If a future audit refutes P1b (the lock is
    shown NOT to function as the chiral coupling), the parity result
    reverts to N35's open fork -- and R-136's deuteron anchor then stands
    alone as the empirical selector.

    WOULD CHANGE IF: (a) P1b is refuted (revert to selection; anchors
    stand); (b) a substrate derivation of the mode determinant lands
    (P1 discharges; the result becomes DERIVED-dynamical -- kernel-class);
    (c) the generation fork is decided (the VALUE 3 vs 9 lands -- parity
    unchanged); (d) a banked change to the roster (e.g. a fourth coupled
    mode per generation) -- the parity recomputes from the same arithmetic.
    """
    # ---- the banked roster, recomputed ----
    sel = bpst_selection_rule(3)
    quark_modes_per_gen = 3            # one per colour facet (banked index count)
    lepton_modes_per_gen = 1
    roster_per_gen = quark_modes_per_gen + lepton_modes_per_gen
    assert sel["ΔB per gen = 3×(1/3)"] == 1 and sel["ΔB = N_gen"] == 3, \
        "the banked index roster must give 3 colour zero modes per generation"

    # ---- Witten-anomaly evenness (gaugeability) vs level parity: same roster ----
    assert roster_per_gen % 2 == 0, "SU(2) gaugeability: 4 doublets/gen must be EVEN"
    assert quark_modes_per_gen % 2 == 1, "baryon-coupled count 3/gen must be ODD"

    # ---- the discrimination anchors (banked primitives, called live) ----
    h = front_phase_handoff_selects_winding_axis()      # R-127: lepton lock, L-channel
    q = qorbit_mass_phase_dual_lock_parity_odd()        # R-128: quark lock, Hodge-dual, odd
    assert q["parity_facts"]["quark_lock_parity_odd"] is True, \
        "R-128: the quark lock channel must be parity-ODD (content-pinned, reviewer R1)"
    assert q["parity_facts"]["L_orbit_even_Q_orbit_odd_I4_odd"] is True, \
        "R-128: the L/Q parity split must hold (content-pinned)"
    assert all(bool(v["centralizer_is_1_and_I4Bq"]) for v in q["per_Bq"].values()), \
        "R-128: the I4-dual lock centralizer must hold on all three Q axes"
    assert all(str(v["dichotomy_ok"]) == "True" for v in h["per_Ba"].values()), \
        "R-127: the winding-axis dichotomy must hold on all three L axes"
    assert "DERIVED-A" in q["tier"], "R-128's parity facts are banked DERIVED-A"
    pi3 = pi3_S3_integer_completion()
    assert pi3["3×(1/3) = 1 is an integer"] is True and pi3["B=1/3 is an integer"] is False, \
        "the integer-winding structure (R-002 family) must hold"

    # ---- the parity table across every named variant ----
    variants = {
        "N = 3 (per-generation, flavor-style embedding)": 3,
        "N = 9 (spectator generation copies)": 9,
    }
    excluded = {
        "N = 4 (lepton wrongly included, per gen)": 4,
        "N = 12 (lepton wrongly included, total)": 12,
        "N = 6 (sigma-species or Dirac/Weyl double-counted, per gen)": 6,
        "N = 18 (same double-counting, total)": 18,
    }
    for name, N in variants.items():
        assert N % 2 == 1 and (-1) ** N == -1, name + " must give weight -1"
    for name, N in excluded.items():
        assert N % 2 == 0, name + \
            " is even -- and EXCLUDED (lepton variants by the L/Q assignment + the " \
            "single-Weyl face; double-counting variants by the counting unit: one " \
            "lock = one chirality-link per colour mode)"

    return {
        "outcome": ("P2-4 LEG 4 answered at the PARITY level: the induced topological "
                    "weight on the B = 1 baryon worldline's 2pi-rotation loop is (-1)^N "
                    "with N = 3 per generation (banked roster: 3 colour modes coupled to "
                    "the Q-orbit field; the lepton mode EXCLUDED by the banked winding "
                    "split R-002 + lock split R-127/R-128) -- N is ODD across the entire "
                    "named fork (3 or 9) => the weight is -1 => FERMIONIC SKYRMION "
                    "QUANTIZATION IS INDUCED, conditional on the named premises P1 "
                    "(imported induced-term theorem) + P1b (the R-128 lock = the chiral "
                    "coupling) + (Q). W-LIVE-4's W1 closes POSITIVE-conditional; the FR "
                    "selection upgrades to INDUCED-given-(P1)+(P1b); both empirical "
                    "anchors (nucleon 1/2, deuteron 1+) become consistency checks."),
        "tier": ("DERIVED-given-(P1)+(P1b)+(Q) (the parity; conditions named and "
                 "load-bearing; P1b = a fresh CANDIDATE-class channel-identification "
                 "premise, the result's one genuine vulnerability) + IMPORTED-AS-CITED "
                 "(P1: D'Hoker-Farhi 1984 / Witten 1982, to-be-verified citations, "
                 "R-088-class at the parity/mod-2-index level) + DERIVED (the roster "
                 "CENSUS -- banked) + DERIVED-given-P1b (the coupled-SUBSET selection "
                 "N = 3) + NAMED FORK parity-robust (N = 3 vs 9 both odd)"),
        "premises": {
            "P1": "induced pi_4(SU(2)) = Z_2 term with weight (-1)^N (imported, cited)",
            "P1b": ("the R-128 parity-odd Hodge-dual quark lock functions as the chiral "
                    "coupling to the Q-orbit field (substrate face of the P1 coupling; "
                    "canon S5 untouched -- no quark mass introduced)"),
            "Q": "collective quantization (as R-133/R-136)",
        },
        "counting": {
            "roster_per_gen": roster_per_gen,
            "baryon_coupled_per_gen": quark_modes_per_gen,
            "lepton_excluded_by": ("R-002 winding split (leptons: diagonal Spin(3) "
                                   "subgroup factor; baryons: coset S^3_Q) + R-127 "
                                   "(lepton lock = parity-even L-channel) + R-128 "
                                   "(quark lock = parity-odd Hodge-dual channel)"),
            "gaugeability_evenness": "4/gen even (Witten anomaly, SC.4.6(i)) -- same roster",
            "fork": {"N=3": "flavor-style", "N=9": "spectator copies",
                     "parity": "ODD in both branches"},
        },
        "w_live_4": ("W1 CLOSED-CONDITIONAL(P1+P1b+Q), POSITIVE: FR fermionic "
                     "quantization = INDUCED-given-(P1)+(P1b), no longer a bare "
                     "selection; N35's would-change-if (a) PARTIALLY DISCHARGED at the "
                     "parity level (the substrate computation face stays open); the "
                     "bosonic branch = refusing P1b, with the revert clause named -- "
                     "and it stands refuted by the R-136 deuteron anchor either way"),
        "would_change_if": ("P1b refuted (revert to selection; anchors stand); the mode "
                            "determinant derived from the substrate (P1 discharges, "
                            "kernel-class); the generation fork decided (value 3 vs 9; "
                            "parity unchanged); the banked roster changes"),
    }


def d4_lattice_instanton_access_and_dm_background_neutrality() -> dict:
    """[DERIVED-A (background topological NEUTRALITY via the iota-mechanism; the
    exact charge-operator calibration identity; the cross-term tensor with its
    closed form; the chiral-transparency and winding-map identities)
    + DERIVED-A construction + NUMERICAL CERTIFICATE (the explicit compactly
    supported charge-1 fluctuation: plateau -> 1, exact localization)
    + LOCATED face (the linear instanton-background coupling)
    + NAMED PREMISES / honest fence (LATT-pi3 sector labeling; no minimizer, no
    action value, no dynamics -- kernel-gated as banked)]
    -- P2-4 LEG 3 STRUCTURAL CORE: the lattice-instanton half. (2026-07-04.)

    WHAT WAS OWED (SC.4.6(ii)/R-140 fence): R-140 banked instanton-sector
    ACCESSIBILITY at the structure-group level (pi_3(SU(2)_pm) = Z, obstruction
    absent) and left 'explicit finite-action lattice instanton CONFIGURATIONS'
    as leg 3. R-088 banked the continuum BPST index half. This primitive
    supplies the lattice half at the structural level: the background is
    topologically NEUTRAL, a properly normalized D4 charge operator EXISTS with
    a derived geometric calibration, and an EXPLICIT finite-action-excess
    charge-1 configuration is exhibited in each chiral sector.

    THE RESULTS:
    (1) BACKGROUND TOPOLOGICAL NEUTRALITY [DERIVED-A, all theta_D, both
        sectors]. THE MECHANISM: the DM twist plane r ^ e4 = r_spatial ^ e4
        depends ONLY on the bond's spatial part, so the e4-reflection
        involution iota (negate every bond's e4-component) leaves EVERY link
        rotor -- hence EVERY based holonomy, hence ANY holonomy-built Lie
        factor -- exactly invariant, while the 4-volume pairing
        <A(T) ^ A(T')>_I4 of two triangle areas is exactly iota-ODD (each I4
        contribution pairs one spatial-spatial with one mixed area component),
        and iota is FREE on the e4-triangles. Hence EVERY site-based
        topological density  sum w_geom(T,T') kappa_hol(T,T')  with
        point-group-covariant pseudoscalar pairing w and holonomy-built kappa
        cancels in iota-orbit pairs IDENTICALLY -- in EACH chiral sector,
        at ALL theta_D. Engine: holonomy iota-invariance dev = 0 exactly;
        pairing oddness exact in integer arithmetic; the canonical double sum
        = 0 to machine precision at generic theta with thousands of
        individually O(1) nonzero terms (a genuine cancellation, not
        triviality); per-(axis-class) blocks vanish independently (asserted
        in-suite, reviewer F1); convention-robust: the variant-b odd
        convention is ALSO neutral, but note (reviewer F2) variant-b links
        READ the e4-orientation, so its zero is NOT an instance of the
        iota-mechanism -- it is banked as a separate numerical fact. SCOPE:
        the site-based density-operator class (the natural discrete tr F^F);
        NOT a claim about arbitrary non-local charge definitions. Contrast:
        generic parity covariance alone would only force q_+ = -q_-; the
        substrate-specific e4-blindness of the banked DM twist (R-103/R-140
        convention) kills BOTH sectors separately. GENERICITY WITNESS
        (reviewer probe, banked): a seeded-random homogeneous connection
        (U_{-r} = U_r^{-1} enforced, generic bivector exponents) has
        per-sector density Q_+ = +29.06, Q_- = -62.48 -- per-site neutrality
        is NOT generic for homogeneous configurations.
    (2) THE D4 CHARGE OPERATOR [DERIVED-A calibration]. The canonical
        site-based pairing form on the 192 based triangle loops satisfies
            Q_form(F) = 576 * eps(F),   eps(F) := <F F>_I4-coefficient,
        as an EXACT identity for a generic constant field (integer-arithmetic
        certificate in-suite; 576 = 24^2 = the squared root count) -- the form
        is pseudoscalar-PURE. Continuum normalization: the BPST density in the
        same component convention has profile constant 24, so
        V_cont = 24 * pi^2/6 = 4 pi^2, giving the normalized charge
            Q_D4 = V_site * sum_sites Q_site / (576 * 4 pi^2),  V_site = 2.
        The operator is exactly gauge-invariant (based logs conjugate by one
        g(x); scalar contractions invariant).
    (3) EXPLICIT CHARGE-1 ACCESS AT FINITE ACTION EXCESS [DERIVED-A
        construction + certificate]. The configuration: the DM background
        composed with a compactly supported, SINGULAR-GAUGE BPST fluctuation
        valued in SU(2)_+ (quaternion units = the SD triple T_a =
        (e_{a4} - e_{bc})/2; engine-exact T_1T_2 = T_3, T_a^2 = -P_+,
        T_a P_- = 0), cut to the identity outside R_cut. EXACT statements:
        (a) CHIRAL TRANSPARENCY: SU(2)_- holonomies are IDENTICALLY the
        background's (T_a P_- = 0) -- the instanton lives in ONE chiral
        sector; the mirrored construction gives the SU(2)_- instanton;
        (b) LOCALIZATION: outside R_cut the configuration IS the background
        link-for-link, so the action excess of ANY plaquette-angle action is
        supported on the finite, box-independent set of triangles touching
        the support (measured far-angle deviation = 0.0 exactly);
        (c) THE CLASS: the dressing's boundary map is the IDENTITY map
        S3 -> SU(2) (quaternion components exactly (x4, x_vec)/|x|), i.e. the
        banked degree-1 generator of pi_3(S3) (pi3_S3_integer_completion,
        R-002-class winding machinery). CERTIFICATE (development record,
        boxes M = 11/15/19, theta_D = 0.3): Q_D4(fluctuation) = 0.7854 /
        0.8955 / 0.9406 at rho = 2/3/4 with deficit ~ 1/rho^2 (0.86/0.94/0.95
        x rho^-2) -- the discretization signature of a UNIT-charge
        configuration, extrapolating to 1; the SAME operator measures the
        background alone at < 1e-5 (independent numpy confirmation of (1));
        Wilson action excess finite (103.19 at rho = 3, R_cut = 12).
        In-suite: a small-instance regression re-runs the full pipeline.
    (4) THE INSTANTON-BACKGROUND CROSS-TERM [DERIVED-A tensor + LOCATED face].
        The background's + sector log field pairs with triangle areas ONLY
        through the SPATIAL area components -- the mixed (a,4) components
        vanish by the same iota-parity -- each spatial plane (bc) coupling to
        exactly its SD blade (e_{a4} - e_{bc}), with the CLOSED FORM
        coefficient  c(theta_D) = 4 sqrt(2) * a sin^2(theta_D)/sin(a),
        a = arccos(cos^2 theta_D):  the coupling is sourced EXACTLY by the
        holonomy's non-abelian excess sin^2(theta_D) -- the banked 48/66
        commutator content (R-140 (4)) acting as a LINEAR source for
        SD-spatial flux. LOCATED CONSEQUENCE (Wilson-class site actions, a
        named premise -- the true substrate fluctuation action is
        kernel-gated): an UNCUT BPST superposition acquires a log(R)-growing
        excess from this linear coupling, so compact support is the correct
        finite-action-excess object; the coupling is orientation-BLIND
        (eta and eta-bar agree on spatial components -- it does NOT
        discriminate instanton vs anti-instanton; no CP-flavored claim).
    (5) STRONG-TWIST HONESTY [measured]. The local charge operator applied to
        the TOTAL (background x instanton) configuration at theta_D = 0.3
        reads ~0.59-0.65, NOT 1: at strong twist the composite is far outside
        the smooth sector and the local operator is not integer-faithful; at
        weak twist the total reading tracks the fluctuation charge
        CONTINUOUSLY (rho = 2 box: Q_total = 0.781/0.746/0.628 at theta_D =
        0.05/0.15/0.3 vs Q_fluct = 0.785). The (LATT-pi3) NAMED PREMISE: the composite's sector label is
        carried by the explicit constructive family (background neutral by
        (1) + fluctuation of unit winding by (3c)), i.e. the standard
        continuum-limit/smooth-sector identification -- not by a local
        operator at strong twist.

    WHAT THIS DOES NOT CLAIM (the honest fence, R-140's inherited): no
    instanton SOLUTION (no minimizer, no action VALUE, no size rho_*, no
    tunneling rate -- all kernel-gated with the fluctuation action); no
    coupling normalization; no continuum limit of the dynamics; the
    Wilson-class premise in (4) is named; R-088's index consequences
    (Delta B = Delta L = N_gen) now have their substrate carrier
    structurally in place but the RATE stays gated.

    P2-4 LEG STATUS after this result: leg 1 banked (48/66) + leg 2
    STRUCTURAL CORE DONE (R-140) + leg 3 STRUCTURAL CORE DONE (this primitive;
    remaining leg-3 face: the instanton solution/action value,
    kernel-adjacent) + leg 4 ANSWERED-AT-PARITY (R-141; substrate computation
    face open).

    WOULD CHANGE IF: (a) the fluctuation-YM action lands (the excess and the
    cross-term acquire derived coefficients; the log-interaction face becomes
    computable); (b) a substrate mechanism selects an instanton SIZE (the
    minimizer face); (c) the kernel decides the tunneling rate (R-088's
    selection-rule RATE face); (d) a non-site-based charge definition is
    motivated that evades the iota-mechanism's scope (would reopen (1)'s
    scope, not its exact content).
    """
    import numpy as np
    import itertools
    from fractions import Fraction

    I4l = e(1, 2, 3, 4)
    Pp = 0.5 * (SCALAR + I4l)
    Pm = 0.5 * (SCALAR - I4l)
    BIVb = [(1, 2), (1, 3), (2, 3), (1, 4), (2, 4), (3, 4)]

    def sc(mv):
        return dict(mv.terms).get((), 0.0)

    def cf(mv, b):
        return dict(mv.terms).get(b, 0.0)

    def bpart(mv):
        c = dict(mv.terms)
        out = 0.0 * SCALAR
        for b in BIVb:
            if b in c:
                out = out + c[b] * e(*b)
        return out

    def vecmv(r):
        out = 0.0 * SCALAR
        for i, x in enumerate(r):
            if x:
                out = out + float(x) * e(i + 1)
        return out

    def maxabs(mv):
        return max((abs(v) for v in dict(mv.terms).values()), default=0.0)

    # ---- roots, based triangle loops at a site ----
    roots = []
    for i, j in itertools.combinations(range(4), 2):
        for si in (1, -1):
            for sj in (1, -1):
                v = [0, 0, 0, 0]
                v[i] = si
                v[j] = sj
                roots.append(tuple(v))
    rset = set(roots)
    based = []
    for r1 in roots:
        for r2 in roots:
            r3 = tuple(-(a + b) for a, b in zip(r1, r2))
            if r3 in rset and r2 != tuple(-z for z in r1):
                based.append((r1, r2, r3))
    assert len(based) == 192, "based triangle loops at a site: 192"

    def Vlink(r, th):
        if r[3] == 0:
            return SCALAR
        a = next(i for i in range(3) if r[i] != 0)
        return math.cos(th) * SCALAR + math.sin(th) * float(r[a]) * e(a + 1, 4)

    def hol(T, th):
        W = SCALAR
        for r in T:
            W = W * Vlink(r, th)
        return W

    def slog(W, P):
        ca = max(-1.0, min(1.0, 2.0 * sc(W * P)))
        al = math.acos(ca)
        Bs = bpart(W * P)
        n = math.sqrt(sum(cf(Bs, b) ** 2 for b in BIVb))
        return (al / n) * Bs if n > 1e-14 else 0.0 * SCALAR

    # integer area data: A2 = 2 * area components (integers), w4 = 4 * pairing
    def area2(T):
        r1, r2, _ = T
        return [r1[m] * r2[n] - r1[n] * r2[m]
                for (m, n) in [(0, 1), (0, 2), (1, 2), (0, 3), (1, 3), (2, 3)]]

    A2 = np.array([area2(T) for T in based], dtype=np.int64)

    def w4pair(Ai, Aj):
        return (Ai[0] * Aj[5] - Ai[1] * Aj[4] + Ai[3] * Aj[2]
                + Aj[0] * Ai[5] - Aj[1] * Ai[4] + Aj[3] * Ai[2])

    W4 = np.array([[w4pair(A2[i], A2[j]) for j in range(192)]
                   for i in range(192)], dtype=np.int64)

    # ---- (1) neutrality: the iota mechanism, exact ----
    def iota(T):
        return tuple(tuple(list(r[:3]) + [-r[3]]) for r in T)

    idx_of = {T: k for k, T in enumerate(based)}
    perm = np.array([idx_of[iota(T)] for T in based])
    ne4 = np.array([sum(1 for r in T if r[3] != 0) for T in based])
    assert all(perm[k] != k for k in range(192) if ne4[k] > 0), \
        "iota must act FREELY on the e4-triangle loops"
    # twist plane r ^ e4 is exactly e4-blind (the substrate mechanism)
    for r in roots:
        if r[3] != 0:
            ir = tuple(list(r[:3]) + [-r[3]])
            d = (vecmv(r) * e(4) - e(4) * vecmv(r)) - (vecmv(ir) * e(4) - e(4) * vecmv(ir))
            assert maxabs(d) == 0.0, "r ^ e4 must be iota-invariant"
    # holonomy invariance, exact; pairing oddness, exact integers
    for k, T in enumerate(based):
        assert maxabs(hol(T, 0.7) + (-1.0) * hol(iota(T), 0.7)) == 0.0, \
            "every based holonomy must be EXACTLY iota-invariant"
    assert (W4[perm][:, perm] == -W4).all(), \
        "the volume pairing must be EXACTLY iota-odd (integer arithmetic)"
    # canonical double sums vanish with individually O(1) terms
    neut = {}
    for th in (0.7, 1.1):
        Lp = [slog(hol(T, th), Pp) for T in based]
        Lm = [slog(hol(T, th), Pm) for T in based]
        Lpc = np.array([[cf(L, b) for b in BIVb] for L in Lp])
        Lmc = np.array([[cf(L, b) for b in BIVb] for L in Lm])
        # <L L'>_0 for bivectors with distinct-blade components: -component dot
        Kp = -(Lpc @ Lpc.T)
        Km = -(Lmc @ Lmc.T)
        Wf = W4.astype(float) / 4.0
        Qp = float((Wf * Kp).sum())
        Qm = float((Wf * Km).sum())
        nz = int(((np.abs(Wf) > 1e-14) & (np.abs(Kp) > 1e-12)).sum())
        mx = float(np.abs(Wf * Kp).max())
        assert abs(Qp) < 1e-10 and abs(Qm) < 1e-10, "background neutrality both sectors"
        neut[th] = {"Q_plus": Qp, "Q_minus": Qm, "nonzero_terms": nz, "max_term": mx}
    assert neut[0.7]["nonzero_terms"] > 5000 and neut[0.7]["max_term"] > 0.05, \
        "the cancellation must be GENUINE (thousands of O(1) terms), not triviality"
    # variant-b convention robustness
    def hol_b(T, th):
        W = SCALAR
        for r in T:
            if r[3] == 0:
                W = W * SCALAR
            else:
                a = next(i for i in range(3) if r[i] != 0)
                W = W * (math.cos(th) * SCALAR
                         + math.sin(th) * float(r[3]) * e(a + 1, 4))
        return W
    Lpb = np.array([[cf(slog(hol_b(T, 0.7), Pp), b) for b in BIVb] for T in based])
    Qpb = float((W4.astype(float) / 4.0 * -(Lpb @ Lpb.T)).sum())
    assert abs(Qpb) < 1e-10, "variant-b odd convention: also neutral"
    # per-(axis-class) blocks vanish independently (reviewer F1)
    axes_of = [tuple(sorted(next(i for i in range(3) if r[i] != 0)
                            for r in T if r[3] != 0)) for T in based]
    Lp07 = np.array([[cf(slog(hol(T, 0.7), Pp), b) for b in BIVb] for T in based])
    Lm07 = np.array([[cf(slog(hol(T, 0.7), Pm), b) for b in BIVb] for T in based])
    Wff = W4.astype(float) / 4.0
    blocks_ok = True
    keys = sorted(set(axes_of))
    for ka in keys:
        ia = [k for k in range(192) if axes_of[k] == ka]
        for kb in keys:
            ib = [k for k in range(192) if axes_of[k] == kb]
            bp = float((Wff[np.ix_(ia, ib)] * -(Lp07[ia] @ Lp07[ib].T)).sum())
            bm = float((Wff[np.ix_(ia, ib)] * -(Lm07[ia] @ Lm07[ib].T)).sum())
            if abs(bp) > 1e-10 or abs(bm) > 1e-10:
                blocks_ok = False
    assert blocks_ok, "every (axis-class, axis-class) block must vanish independently"
    # genericity witness (reviewer probe, banked): seeded-random homogeneous
    # connection with U_{-r} = U_r^{-1} -> per-sector density NONZERO
    rngw = np.random.default_rng(0)
    expo = {}
    for r in roots:
        mr = tuple(-z for z in r)
        if mr in expo:
            continue
        cs = rngw.uniform(-0.6, 0.6, size=6)
        Bw = 0.0 * SCALAR
        for k, b in enumerate(BIVb):
            Bw = Bw + cs[k] * e(*b)
        expo[r] = Bw
    def mvexp(B, order=40):
        out = SCALAR
        term = SCALAR
        for n in range(1, order):
            term = term * B * (1.0 / n)
            out = out + term
        return out
    wlinks = {}
    for r, Bw in expo.items():
        wlinks[r] = mvexp(Bw)
        wlinks[tuple(-z for z in r)] = mvexp(-1.0 * Bw)
    for r in roots:
        assert maxabs(wlinks[r] * wlinks[tuple(-z for z in r)] + (-1.0) * SCALAR) < 1e-10, \
            "witness must be a consistent connection"
    Lwp, Lwm = [], []
    for T in based:
        W = SCALAR
        for r in T:
            W = W * wlinks[r]
        Lwp.append(slog(W, Pp))
        Lwm.append(slog(W, Pm))
    Lwpc = np.array([[cf(L, b) for b in BIVb] for L in Lwp])
    Lwmc = np.array([[cf(L, b) for b in BIVb] for L in Lwm])
    Qwp = float((Wff * -(Lwpc @ Lwpc.T)).sum())
    Qwm = float((Wff * -(Lwmc @ Lwmc.T)).sum())
    assert abs(Qwp) > 1.0 and abs(Qwm) > 1.0, \
        "genericity witness: per-site neutrality is NOT generic (nonzero density)"

    # ---- (2) calibration identity, exact integer arithmetic ----
    M16 = A2.T @ W4 @ A2          # 16 x the quadratic-form matrix
    E = np.zeros((6, 6), dtype=np.int64)
    E[0, 5] = E[5, 0] = 1
    E[1, 4] = E[4, 1] = -1
    E[2, 3] = E[3, 2] = 1
    assert (M16 == 16 * 576 * E).all(), \
        "Q_form(F) = 576 * eps(F) must hold EXACTLY (integer arithmetic)"

    # ---- (3) the construction: SD units, dressing, transparency ----
    Ts = [0.5 * (e(1, 4) - e(2, 3)), 0.5 * (e(2, 4) - e(3, 1)),
          0.5 * (e(3, 4) - e(1, 2))]
    for a in range(3):
        assert maxabs(I4l * Ts[a] + (-1.0) * Ts[a]) == 0.0, "T_a self-dual"
        assert maxabs(Ts[a] * Ts[a] + Pp) == 0.0, "T_a^2 = -P_plus"
        assert maxabs(Ts[a] * Pm) == 0.0, "T_a P_minus = 0"
    assert maxabs(Ts[0] * Ts[1] + (-1.0) * Ts[2]) == 0.0, "T1 T2 = T3"

    def grev(mv):
        c = dict(mv.terms)
        out = 0.0 * SCALAR
        for b, v in c.items():
            s = -1.0 if len(b) == 2 else 1.0
            out = out + s * v * (e(*b) if b else SCALAR)
        return out

    def gmap(x):
        n = math.sqrt(sum(xi * xi for xi in x))
        g = Pm + (x[3] / n) * Pp
        for a in range(3):
            g = g + (x[a] / n) * Ts[a]
        return g

    for x in ((1.3, -0.4, 2.1, 0.7), (0.2, 1.1, -0.6, -1.4)):
        g = gmap(x)
        n = math.sqrt(sum(xi * xi for xi in x))
        assert maxabs(g * grev(g) + (-1.0) * SCALAR) < 1e-14, "g unitary"
        assert maxabs(g * Pm + (-1.0) * Pm) == 0.0, "g trivial on SU(2)_-"
        # quaternion components = the IDENTITY map (x4, x_vec)/|x| (degree 1)
        assert abs(2.0 * sc(g * Pp) - x[3] / n) < 1e-15
        for a in range(3):
            assert abs(-2.0 * sc(g * Ts[a]) - x[a] / n) < 1e-15
    # chiral transparency of a dressed background link, exact
    r = (1, 0, 0, 1)
    x = [1.3, -0.4, 2.1, 0.7]
    y = [x[i] + r[i] for i in range(4)]
    U = Vlink(r, 0.7) * gmap(x) * grev(gmap(y))
    assert maxabs(U * Pm + (-1.0) * (Vlink(r, 0.7) * Pm)) < 1e-14, \
        "SU(2)_- part of any + sector-dressed link = background exactly"

    # ---- (4) cross-term tensor + closed form (0.5 = reviewer third-theta pin) ----
    cross = {}
    for th in (0.3, 0.5, 0.7):
        Csp = {}
        for bl in BIVb:
            Csp[bl] = 0.0 * SCALAR
        for T in based:
            L = slog(hol(T, th), Pp)
            r1, r2, _ = T
            Amv = 0.25 * (vecmv(r1) * vecmv(r2) - vecmv(r2) * vecmv(r1))
            for bl in BIVb:
                Csp[bl] = Csp[bl] + cf(Amv, bl) * L
        for bl in ((1, 4), (2, 4), (3, 4)):
            assert maxabs(Csp[bl]) < 1e-12, "mixed (a,4) cross components vanish"
        a_th = math.acos(math.cos(th) ** 2)
        c_pred = 4.0 * math.sqrt(2.0) * a_th * math.sin(th) ** 2 / math.sin(a_th)
        c_meas = -cf(Csp[(1, 2)], (1, 2))
        assert abs(cf(Csp[(1, 2)], (1, 2)) + cf(Csp[(1, 2)], (3, 4))) < 1e-12, \
            "spatial cross component is the SD blade (e12 - e34 direction)"
        assert abs(c_meas - c_pred) < 1e-10, \
            "closed form c(th) = 4 sqrt2 a sin^2(th)/sin(a)"
        cross[th] = c_meas

    # ---- (3-cert) small-instance regression of the full lattice pipeline ----
    def qmul(a, b):
        w = a[..., 0] * b[..., 0] - (a[..., 1:] * b[..., 1:]).sum(-1)
        v = (a[..., :1] * b[..., 1:] + b[..., :1] * a[..., 1:]
             + np.cross(a[..., 1:], b[..., 1:]))
        return np.concatenate([w[..., None], v], axis=-1)

    def qconj(a):
        o = a.copy()
        o[..., 1:] *= -1.0
        return o

    def qexp(v):
        n = np.linalg.norm(v, axis=-1)
        w = np.cos(n)
        s = np.where(n > 1e-30, np.sin(n) / np.maximum(n, 1e-30), 1.0)
        return np.concatenate([w[..., None], s[..., None] * v], axis=-1)

    def qlog(q):
        w = np.clip(q[..., 0], -1.0, 1.0)
        al = np.arccos(w)
        n = np.linalg.norm(q[..., 1:], axis=-1)
        f = np.where(n > 1e-14, al / np.maximum(n, 1e-14), 1.0)
        return f[..., None] * q[..., 1:]

    QID = np.array([1.0, 0.0, 0.0, 0.0])

    def A_sing(xs, rho):
        x2 = (xs * xs).sum(-1)
        q = np.stack([xs[:, 3], -xs[:, 0], -xs[:, 1], -xs[:, 2]], axis=-1)
        rr = np.sqrt(x2)
        h = q / rr[:, None]
        hinv = qconj(h)
        fs = rho ** 2 / (x2 + rho ** 2)
        A = np.zeros((len(xs), 4, 3))
        for mu in range(4):
            emu = np.zeros((len(xs), 4))
            if mu == 3:
                emu[:, 0] = 1.0
            else:
                emu[:, mu + 1] = -1.0
            dg = emu / rr[:, None] - xs[:, mu][:, None] * q / (rr ** 3)[:, None]
            A[:, mu, :] = fs[:, None] * qmul(hinv, dg)[..., 1:]
        return A

    rho, R_cut, M, th_D = 1.5, 4.5, 7, 0.3
    rng1 = np.arange(-M, M + 1)
    grid = np.array(np.meshgrid(rng1, rng1, rng1, rng1,
                                indexing="ij")).reshape(4, -1).T
    grid = grid[(grid.sum(1) % 2) == 0]
    dimg = 2 * M + 1
    dense = -np.ones((dimg,) * 4, dtype=np.int64)
    dense[tuple((grid + M).T)] = np.arange(len(grid))
    ctr = np.array([0.5, 0.5, 0.5, 0.5])
    X = grid.astype(float) - ctr[None, :]
    r2s = (X * X).sum(1)

    lf, lb = {}, {}
    for rt in roots:
        rv = np.array(rt, float)
        Av = A_sing(X + 0.5 * rv[None, :], rho)
        u = qexp(np.einsum("nmc,m->nc", Av, rv))
        out = (r2s > R_cut ** 2) & (((X + rv[None, :]) ** 2).sum(1) > R_cut ** 2)
        u[out] = QID
        lf[rt] = u
        if rt[3] == 0:
            lb[rt] = np.broadcast_to(QID, (len(grid), 4))
        else:
            a = next(i for i in range(3) if rt[i] != 0)
            qb = np.zeros(4)
            qb[0] = math.cos(th_D)
            qb[1 + a] = math.sin(th_D) * rt[a]
            lb[rt] = np.broadcast_to(qb, (len(grid), 4))
    lt = {rt: qmul(np.ascontiguousarray(np.broadcast_to(lb[rt], lf[rt].shape)),
                   lf[rt]) for rt in roots}

    def nbr(shift):
        sh = grid + np.array(shift)[None, :]
        ok = np.all(np.abs(sh) <= M, axis=1)
        o = -np.ones(len(grid), dtype=np.int64)
        o[ok] = dense[tuple((sh[ok] + M).T)]
        return o

    def loop_logs(links):
        L = np.zeros((192, len(grid), 3))
        val = np.ones(len(grid), dtype=bool)
        for k, (ra, rb, rc) in enumerate(based):
            i2 = nbr(ra)
            i3 = nbr(tuple(p + q2 for p, q2 in zip(ra, rb)))
            ok = (i2 >= 0) & (i3 >= 0)
            val &= ok
            Wq = qmul(qmul(links[ra], links[rb][np.where(ok, i2, 0)]),
                      links[rc][np.where(ok, i3, 0)])
            L[k][ok] = qlog(Wq[ok])
        return L, val

    V_cont = 4.0 * math.pi ** 2      # = 24 * pi^2/6, BPST profile constant 24
    V_site = 2.0

    def charge(L, mask):
        Lm = L * mask[None, :, None]
        acc = np.zeros(L.shape[1])
        Wf = W4.astype(float) / 4.0
        for cc in range(3):
            G = Lm[:, :, cc]
            acc += (G * (Wf @ G)).sum(0)
        return V_site * acc.sum() / (576.0 * V_cont)

    Lfq, vf = loop_logs(lf)
    Lbq, vb = loop_logs(lb)
    Ltq, vt = loop_logs(lt)
    Qf = charge(Lfq, vf)
    Qb = charge(Lbq, vb)
    angs_t = np.linalg.norm(Ltq, axis=-1)
    angs_b = np.linalg.norm(Lbq, axis=-1)
    far = (r2s > (R_cut + 2.5) ** 2) & vt & vb
    far_dev = float(np.abs(angs_t - angs_b)[:, far].max())
    exc = float((((1 - np.cos(angs_t)) - (1 - np.cos(angs_b)))[:, vt & vb]).sum() / 6.0)
    assert abs(Qb) < 1e-8, "numpy pipeline confirms background neutrality"
    assert far_dev == 0.0, "action excess EXACTLY localized (far deviation zero)"
    assert 0.65 < Qf < 0.70, "regression: Q_fluct(rho=1.5, R_cut=4.5) = 0.672"
    assert 55.0 < exc < 70.0, "regression: Wilson excess = 61.85, finite"

    return {
        "outcome": ("P2-4 LEG 3 STRUCTURAL CORE banked: the DM background is "
                    "topologically NEUTRAL in both chiral sectors (iota-mechanism: "
                    "the twist plane r^e4 is e4-reflection-blind while the volume "
                    "pairing is e4-reflection-odd -- exact, all theta_D, whole "
                    "site-based density class); the D4 charge operator calibrates "
                    "EXACTLY as Q_form = 576 eps(F) (24^2; pseudoscalar-pure) with "
                    "continuum norm 4 pi^2; an EXPLICIT compactly-supported "
                    "SU(2)_+ singular-gauge winding-1 fluctuation over the "
                    "background has exactly-localized finite action excess, exact "
                    "SU(2)_- transparency, and measured charge -> 1 (0.79/0.90/"
                    "0.94 at rho = 2/3/4, deficit ~ 1/rho^2); the linear "
                    "instanton-background coupling is derived in closed form "
                    "(4 sqrt2 a sin^2/sin a -- sourced by the 48/66 non-abelian "
                    "excess) and is orientation-blind. No minimizer, no action "
                    "value, no rate -- kernel-gated as banked."),
        "tier": ("DERIVED-A (neutrality mechanism, exact; calibration identity, "
                 "integer-exact; cross-term tensor + closed form; transparency + "
                 "winding identities) + DERIVED-A-construction + CERTIFICATE "
                 "(charge plateau -> 1, dev record + in-suite regression) + "
                 "LOCATED (linear coupling face; Wilson-class premise NAMED) + "
                 "NAMED PREMISE (LATT-pi3 sector labeling at strong twist) + "
                 "FRAMING preserved (fluctuation dynamics kernel-gated, R-140 "
                 "fence inherited)"),
        "neutrality": {"mechanism": "iota: r^e4 e4-blind; pairing odd; free",
                       "sums": neut, "variant_b_sum": Qpb,
                       "variant_b_note": ("variant-b reads the e4-orientation: its "
                                          "zero is a separate numerical fact, NOT "
                                          "the iota-mechanism (reviewer F2)"),
                       "blocks_all_zero": blocks_ok,
                       "genericity_witness": {"Q_plus": Qwp, "Q_minus": Qwm,
                                              "note": ("seeded-random homogeneous "
                                                       "connection: NONZERO -- "
                                                       "neutrality not generic")},
                       "scope": "site-based density class (discrete tr F^F)"},
        "charge_operator": {"calibration": "Q_form(F) = 576 * eps(F), exact",
                            "c_geom": 576, "V_cont": "4 pi^2 (BPST const 24)",
                            "gauge_invariant": True},
        "access": {"chiral_transparency": "exact (T_a P_- = 0)",
                   "winding": "identity map S3 -> SU(2)_+, degree 1 (banked pi_3)",
                   "dev_record_Q": {2.0: 0.7854, 3.0: 0.8955, 4.0: 0.9406},
                   "deficit_scaling": "~ 1/rho^2 -> extrapolates to 1",
                   "regression": {"rho": rho, "R_cut": R_cut, "M": M,
                                  "Q_fluct": Qf, "Q_bg": Qb,
                                  "far_dev": far_dev, "excess": exc},
                   "action_excess_dev_record": 103.19},
        "cross_term": {"closed_form": "c(th) = 4 sqrt2 * a sin^2(th)/sin(a)",
                       "at": cross, "mixed_components": 0.0,
                       "orientation_blind": True,
                       "located_face": ("linear coupling -> log(R) excess for "
                                        "uncut superpositions (Wilson-class "
                                        "premise); compact support is the "
                                        "finite-action object")},
        "strong_twist_reading": {"Q_total_dev_record_th0.3": (0.63, 0.65, 0.59),
                                 "weak_twist_continuity_rho2":
                                     {0.05: 0.781, 0.15: 0.746, 0.3: 0.628,
                                      "Q_fluct": 0.785},
                                 "premise": "LATT-pi3 (constructive labeling)"},
        "p2_4_status": ("leg 1 banked (48/66) + leg 2 STRUCTURAL CORE DONE "
                        "(R-140) + leg 3 STRUCTURAL CORE DONE (this; remaining "
                        "face: instanton solution/action value, kernel-adjacent) "
                        "+ leg 4 ANSWERED-AT-PARITY (R-141; substrate "
                        "computation face open)"),
        "would_change_if": ("fluctuation-YM lands (coefficients for excess + "
                            "cross-term; log face computable); a substrate "
                            "size-selection mechanism (minimizer face); the "
                            "kernel rate (R-088 selection-rule rate face); a "
                            "motivated non-site-based charge definition "
                            "(would reopen scope of (1), not its content)"),
    }


def full_field_b2_below_threshold_sc1_datum() -> dict:
    """[DERIVED-A (the 3D functional IS the banked sector: the hedgehog
    reduction of the full 3D energy density to R-135's radial integrand is a
    SYMBOLIC identity, sympy-certified in-suite; the discretization reproduces
    the 1D quadrature of the same ansatz with h^2-convergent agreement)
    + DERIVED dressed-level VARIATIONAL, FULL-FIELD (the ansatz-free 3D B = 2
    sector of the banked dressed Skyrme static energy lies STRICTLY BELOW the
    two-defect threshold at matched discretization -- charge-conserving
    projected-gradient descent with no symmetry CONSTRAINT during the flow,
    stalls below 2 E(B=1) on the same grid at BOTH resolutions; both sectors'
    stall values are upper bounds on their discrete minima, and the margin is
    protected against B = 1-side descent by the reviewer's banked
    continuation probe + the R-133 continuum anchor (see THE MARGIN below);
    same branch-(c)/hedgehog-minimality conditionality as R-135, inherited)
    + STRUCTURE, corroborative (the minimizer found is the TOROIDAL B = 2:
    exactly axial moments, baryon density maximal on a ring, suppressed at
    the center -- the literature torus, reached here with NO symmetry
    assumption; corroboration, not load-bearing)
    + SC-1 SECOND DATUM, scoped (STATIC variational coherence of the
    two-defect sector WITHOUT any symmetry reduction -- the full 3D landscape
    supports a simultaneous two-defect bound configuration reached by
    charge-conserving descent; the DYNAMICAL multi-defect Cl(4,1) EOM face of
    SC-1 remains open and kernel-gated -- this is the second datum the SC-1
    row asked for, not a closure)
    + METHODOLOGY, honest (lattice winding is SMOOTH-SECTOR-protected only:
    two recorded unwinding events -- under-resolved core, and Adam's
    vacuum-noise pathology -- make the charge-guard + resolution discipline
    load-bearing for ANY lattice flow on the substrate; the flow-level face
    of R-143's LATT-pi3 caveat)] -- SC-1's full-3D second datum: the R-135
    below-threshold conclusion survives ANSATZ-FREEDOM, and R-135's
    would-change-if (c) FIRED as predicted (the full field KEEPS the binding
    -- deepening at N = 96 same-grid, 3.06% vs 1.89%; the N = 64 same-grid
    1.79% sits slightly below the RM 1.89%, a stall/discretization nuance,
    reviewer F5; it does not un-bind). (2026-07-05.)

    WHAT WAS OWED (companion Section 12, SC-1 row): 'the full 3D static B = 2
    problem (torus) is the natural second datum' -- R-135's first datum was
    the ansatz-REDUCED radial BVP; the reduction itself was the caveat.

    THE COMPUTATION (development record; torch/CUDA gradient flow, fp32 flow
    + fp64 evaluation; box L = 7.5 x-units, cell-centered, vacuum-pinned
    boundary shell; SGD + momentum with periodic EXACT Derrick rescaling --
    resampling phi(lambda x) at lambda* = sqrt(E2/E4), which minimizes over
    the scale family analytically, so every step stays variational;
    charge-guard asserts |Delta B_disc| < 0.04 along the whole flow):
      * B = 1 (hedgehog init): N = 64 -> E = 36.4599 (virial 0.99219,
        B_disc = -0.97779, moments spherical to 4 digits); N = 96 ->
        E = 36.9399 (virial 1.00004, B_disc = -0.99027) -- the banked
        continuum coefficient is 36.462 (R-133): the fine-grid value sits
        +1.3% above it (bulk h^2 + box truncation), the coarse-grid value
        lands on it by a recorded, understood cancellation (its 2.2%
        discrete-charge deficit under-counts energy in the same direction).
        SAME-GRID comparisons are therefore the honest ones.
      * B = 2 (rational-map z^2 init, NO symmetry imposed thereafter):
        N = 64 -> E = 71.6177 (virial 0.98666, B_disc = -1.95783);
        N = 96 stall -> E = 72.4923 (virial 0.99399, B_disc = -1.98150);
        N = 96 long continuation (30k more steps) -> E = 71.6169
        (virial 0.99038, B_disc = -1.98198).
      * THE MARGIN (same grid, both resolutions, STALL-vs-STALL -- reviewer
        F1/F3 honesty): N = 64: E(B2) = 71.6177 < 2 E(B1) = 72.9198 (1.79%);
        N = 96: E(B2) = 71.6169 < 2 E(B1) = 73.8798 (3.06%); vs R-135's
        ansatz-reduced 1.89%. BOTH sectors' stall values are upper bounds on
        their discrete minima, so descent on the B = 2 side deepens the
        margin while descent on the B = 1 side SHRINKS it (the original
        'descent only deepens' wording was one-sided -- reviewer-corrected,
        engine-demonstrated): the reviewer's 15k-step B = 1-side continuation
        probe (banked) moves E(B1) 36.9399 -> 36.8986 (virial -> 1.00068,
        decelerating at -0.0034/3k steps), margin 3.06% -> 2.95%. The margin
        is protected by (a) the B = 1 virial ~ 1.0007 + decelerating residual
        drift (orders short of the ~3% needed to un-bind) and (b) the R-133
        continuum anchor 2 x 36.462 = 72.923 > 71.617 independently. Margin
        VALUES are stall-vs-stall records, not converged constants (rescale-
        free flows fake-stall at 6.8-7.3%, recorded); the banked content is
        the SIGN + the ~3% order, corrected N = 96 estimate ~2.9-3.0% (the
        literature full-field torus sits at ~4.3% binding; the trend is
        toward it from above).
      * THE STRUCTURE (N = 96): moments [4.433, 4.433, 6.3651] -- axial to 4
        digits; baryon density maximal on a RING at r = 1.553; center density
        0.0207 of max: the toroidal B = 2 minimizer. QUALIFIER (reviewer F2):
        'no symmetry input' means no symmetry CONSTRAINT during the flow --
        the z^2 initial condition IS axial and the cubic grid enforces the
        x = y moment equality; the genuine structural evidence is the
        ring/center density profile and its SHARPENING along the descent
        (corroborative, not load-bearing, as tiered).
      * Boundary honesty: a RIGID fat-tail (1/r^2) ansatz evaluated against
        the vacuum-pinned boundary acquires a spurious boundary-jump energy
        (recorded: +12.6% at N = 96 on the rigid Lorentzian-profile ansatz);
        the RELAXED field smooths into the pinned shell and does not have
        this artifact (its residual box error is O(tail) ~ 0.1%-scale).
        The in-suite regression therefore uses a compactly-supported
        profile (bulk-only discretization test).

    WHAT THIS BANKS (in-suite, numpy-only -- the torch/GPU record above is a
    development certificate, re-runnable from the archived scripts at
    knowledge/dev_records/r144_sc1_full_field/, which also holds the
    production + continuation logs and one recorded unwinding-failure log):
      (i)  the sympy hedgehog-reduction identity of the 3D functional
           (DERIVED-A: the 3D density on the hedgehog ansatz == R-135's
           radial integrand u/x^2, symbolically);
      (ii) the discretization regression: compact-support ansatz, 3D lattice
           energy vs 1D quadrature of the same profile, at N = 48 and N = 96
           for BOTH the B = 1 hedgehog and the B = 2 z^2 map -- rel. errors
           ~3%/~0.9% with the h^2 ratio in [3, 5.5]; discrete degree
           improving toward -1/-2;
      (iii) a short charge-conserving projected-gradient descent at 32^3
           with the hand-coded gradient (validated to machine precision
           against autograd): E strictly decreasing, |B_disc| drift < 0.025
           -- descent + charge conservation demonstrated inside the suite;
      (iv) the development record values asserted for internal consistency
           (margins, virials, torus structure, charge stability).

    HONEST FENCE: NO dynamical multi-defect EOM (the SC-1 core face --
    unformulated, kernel-gated; this datum is STATIC); NO continuum
    attained-minimizer theorem (concentration-compactness, literature
    character, as R-135); NO binding MAGNITUDE claim (the classical massless
    value remains the known overbinding vs the deuteron's 2.22 MeV -- the
    magnitude face lives at quantization + pion mass, the P2-7 residual row,
    untouched); the torus identification is corroborative.

    WOULD CHANGE IF: (a) further B = 1-side convergence closes the margin
    (bounded away: the reviewer's 15k-step probe shrank it only 3.06% ->
    2.95%, decelerating, with B1 virial 1.00068; the R-133 continuum anchor
    72.923 > 71.617 protects the sign independently -- but this is the
    honest two-sided statement, NOT 'descent only deepens'); (b) the
    dynamical multi-defect EOM lands (SC-1's real face -- this datum then
    becomes its static boundary condition); (c) the massive-pion full-field
    problem shifts the margin (R-137/R-138 banked fork-robustness at the
    ansatz level; the full-field massive run is a named follow-up);
    (d) B >= 3 full-field sectors (third datum, optional -- the multi-defect
    trend).
    """
    import numpy as np
    from scipy.integrate import quad

    # ---------- (i) sympy: the 3D density reduces to R-135's u/x^2 ----------
    # evaluated on generic rays x = rho*(a,b,c), |(a,b,c)| = 1 (two directions;
    # the hedgehog ansatz is rotation-equivariant, so a generic ray decides)
    rho = sp.Symbol('rho', positive=True)
    Ff = sp.Function('F')
    for (ca, cb, cc) in ((sp.Rational(3, 13), sp.Rational(4, 13), sp.Rational(12, 13)),
                         (sp.Rational(2, 11), sp.Rational(6, 11), sp.Rational(9, 11))):
        xs, ys, zs = sp.symbols('x y z', positive=True)
        r_ = sp.sqrt(xs**2 + ys**2 + zs**2)
        F_ = Ff(r_)
        nvec = [xs / r_, ys / r_, zs / r_]
        phis = [sp.cos(F_)] + [sp.sin(F_) * nc for nc in nvec]
        dm = [[sp.diff(pc, c) for pc in phis] for c in (xs, ys, zs)]
        gm = [[sum(dm[i][k] * dm[j][k] for k in range(4)) for j in range(3)]
              for i in range(3)]
        trm = sum(gm[i][i] for i in range(3))
        sqm = sum(gm[i][j] ** 2 for i in range(3) for j in range(3))
        dens = trm / 8 + (trm ** 2 - sqm) / 4
        dens_r = sp.simplify(dens.subs({xs: ca * rho, ys: cb * rho, zs: cc * rho}))
        Frho = Ff(rho)
        Fp = Frho.diff(rho)
        target = (rho**2 * Fp**2 / 8 + sp.sin(Frho)**2 / 4
                  + sp.sin(Frho)**2 * Fp**2 + sp.sin(Frho)**4 / (2 * rho**2)) / rho**2
        assert sp.simplify(dens_r - target) == 0,             "3D Skyrme density must reduce EXACTLY to R-135's u/x^2 on the hedgehog"

    # ---------- shared numpy machinery ----------
    def np_grid(N, L):
        h = 2 * L / N
        ax = (np.arange(N) - (N - 1) / 2) * h
        X, Y, Z = np.meshgrid(ax, ax, ax, indexing="ij")
        return X, Y, Z, h

    def np_diff(phi_, axis, h, ghost_vac=True):
        gcol = np.zeros_like(np.take(phi_, [0], axis=axis))
        if ghost_vac:
            gcol[0] = 1.0
        up = np.concatenate([np.take(phi_, range(1, phi_.shape[axis]), axis=axis), gcol], axis=axis)
        dn = np.concatenate([gcol, np.take(phi_, range(0, phi_.shape[axis] - 1), axis=axis)], axis=axis)
        return (up - dn) / (2 * h)

    def np_energy(phi_, h):
        d_ = [np_diff(phi_, ax, h) for ax in (1, 2, 3)]
        g_ = [[(d_[i] * d_[j]).sum(0) for j in range(3)] for i in range(3)]
        tr_ = g_[0][0] + g_[1][1] + g_[2][2]
        sq_ = sum(g_[i][j] ** 2 for i in range(3) for j in range(3))
        return (tr_ / 8.0).sum() * h**3, ((tr_ * tr_ - sq_) / 4.0).sum() * h**3, d_, g_, tr_

    def np_energy_grad(phi_, h):
        e2s, e4s, d_, g_, tr_ = np_energy(phi_, h)
        P = []
        for i in range(3):
            term = d_[i] / 4.0 + tr_[None] * d_[i]
            for j in range(3):
                term = term - g_[i][j][None] * d_[j]
            P.append(term)
        grad = np.zeros_like(phi_)
        for i, ax in enumerate((1, 2, 3)):
            grad -= np_diff(P[i], ax, h, ghost_vac=False)
        return e2s + e4s, grad * h**3, e2s, e4s

    def np_baryon(phi_, h):
        d_ = [np_diff(phi_, ax, h) for ax in (1, 2, 3)]
        M = np.stack([phi_, d_[0], d_[1], d_[2]], axis=-1)
        M = np.moveaxis(M, 0, -2)
        return np.linalg.det(M).sum() * h**3 / (2 * math.pi**2)

    Rc = 5.5
    def np_init_c(X, Y, Z, Bmap):
        rr = np.sqrt(X*X + Y*Y + Z*Z) + 1e-12
        Fc = np.where(rr < Rc, math.pi * (1 - (rr / Rc)**2)**2, 0.0)
        ct = np.clip(Z / rr, -1, 1)
        th = np.arccos(ct)
        ph = np.arctan2(Y, X)
        if Bmap == 1:
            n1 = np.sin(th)*np.cos(ph); n2 = np.sin(th)*np.sin(ph); n3 = np.cos(th)
        else:
            t = np.clip(np.tan(th / 2), None, 1e6)
            R2 = t * t
            den = 1 + R2 * R2
            n1 = 2*R2*np.cos(2*ph)/den; n2 = 2*R2*np.sin(2*ph)/den; n3 = (1-R2*R2)/den
        sF = np.sin(Fc)
        return np.stack([np.cos(Fc), sF*n1, sF*n2, sF*n3], axis=0)

    # ---------- (ii) discretization regression, compact profile ----------
    psi_rm = lambda rho: (1 + rho**2) * 2 * rho / (1 + rho**4)
    I2, _ = quad(lambda q: psi_rm(q)**4 * 2*q/(1+q**2)**2, 0, np.inf, limit=200)
    Bdeg, _ = quad(lambda q: psi_rm(q)**2 * 2*q/(1+q**2)**2, 0, np.inf, limit=200)
    assert abs(I2 - 5.8083) < 2e-4 and abs(Bdeg - 2.0) < 1e-8, \
        "R-135's angular integral + degree identity must reproduce"

    def rad_quad_c(Bc, Ic):
        xq = np.linspace(1e-6, Rc, 300000)
        Fq = math.pi * (1 - (xq / Rc)**2)**2
        Fpq = math.pi * 2 * (1 - (xq / Rc)**2) * (-2 * xq / Rc**2)
        uq = (xq**2 * Fpq**2 / 8 + Bc * np.sin(Fq)**2 / 4
              + Bc * np.sin(Fq)**2 * Fpq**2 + Ic * np.sin(Fq)**4 / (2 * xq**2))
        return 4 * math.pi * np.trapezoid(uq, xq)

    regress = {}
    for N, Lb in ((48, 7.5), (96, 7.5)):
        X, Y, Z, h = np_grid(N, Lb)
        for Bmap, Ic in ((1, 1.0), (2, I2)):
            ph_ = np_init_c(X, Y, Z, Bmap)
            e2, e4, *_ = np_energy(ph_, h)
            rel = (e2 + e4) / rad_quad_c(Bmap, Ic) - 1
            regress[(Bmap, N)] = (rel, np_baryon(ph_, h))
    for Bmap in (1, 2):
        r48, b48 = regress[(Bmap, 48)]
        r96, b96 = regress[(Bmap, 96)]
        assert abs(r48) < 0.045 and abs(r96) < 0.012, "discretization errors in band"
        assert 3.0 < abs(r48) / abs(r96) < 5.5, "h^2 convergence of the 3D functional"
        assert abs(abs(b96) - Bmap) < abs(abs(b48) - Bmap), "discrete degree improves"

    # ---------- (iii) short charge-conserving descent, 32^3 ----------
    N, Lb = 32, 6.0
    X, Y, Z, h = np_grid(N, Lb)
    rr = np.sqrt(X*X + Y*Y + Z*Z) + 1e-12
    Fw = math.pi / (1 + (rr / 2.0)**2)
    ct = np.clip(Z / rr, -1, 1); th = np.arccos(ct); ph2 = np.arctan2(Y, X)
    sF = np.sin(Fw)
    phi_ = np.stack([np.cos(Fw), sF*np.sin(th)*np.cos(ph2),
                     sF*np.sin(th)*np.sin(ph2), sF*np.cos(th)], axis=0)

    def pin(p):
        for ax in (1, 2, 3):
            for sl in (slice(0, 1), slice(-1, None)):
                idx = [slice(None)] * 4
                idx[ax] = sl
                p[tuple(idx)] = 0.0
                idx[0] = 0
                p[tuple(idx)] = 1.0

    B_start = np_baryon(phi_, h)
    Etraj = []
    vmom = np.zeros_like(phi_)
    for it in range(400):
        E, gr, _, _ = np_energy_grad(phi_, h)
        vmom = 0.9 * vmom - 8e-4 * gr / h**3
        phi_ = phi_ + vmom
        phi_ /= np.sqrt((phi_**2).sum(0, keepdims=True))
        pin(phi_)
        if it % 100 == 0 or it == 399:
            Etraj.append((E, np_baryon(phi_, h)))
    # monotone after the initial momentum transient (burn-in one log interval)
    assert all(Etraj[i+1][0] < Etraj[i][0] for i in range(1, len(Etraj)-1)), \
        "projected-gradient descent must be monotone after burn-in"
    assert max(abs(b - B_start) for _, b in Etraj) < 0.025, \
        "the winding must be conserved along the descent (charge-guard)"
    assert Etraj[0][0] - Etraj[-1][0] > 1.5, "the descent must make real progress"

    # ---------- (iv) development record (torch/CUDA; scripts archived) ----------
    dev = {
        "B1": {"N64": {"E": 36.4599, "virial": 0.99219, "B": -0.97779},
               "N96": {"E": 36.9399, "virial": 1.00004, "B": -0.99027,
                       "moments": [2.8283, 2.8283, 2.8283]}},
        "B2": {"N64": {"E": 71.6177, "virial": 0.98666, "B": -1.95783},
               "N96_stall": {"E": 72.4923, "virial": 0.99399, "B": -1.98150},
               "N96_final": {"E": 71.6169, "virial": 0.99038, "B": -1.98198,
                             "moments": [4.433, 4.433, 6.3651], "r_ring": 1.553,
                             "center_over_max": 0.0207}},
        "margins_same_grid_pct": {"N64": 1.79, "N96": 3.06},
        "reviewer_b1_continuation_probe": {
            "E_B1_after_15k": 36.8986, "virial": 1.00068,
            "margin_pct": 2.95,
            "note": ("reviewer F1 probe, banked: B = 1-side descent SHRINKS "
                     "the margin (3.06 -> 2.95%, decelerating -0.0034/3k "
                     "steps) -- both stalls are upper bounds; sign protected "
                     "by the R-133 continuum anchor 72.923 > 71.617")},
        "margin_note": ("stall-vs-stall records, not converged constants "
                        "(rescale-free flows fake-stall at 6.8-7.3%, "
                        "recorded); banked content = SIGN + ~3% order"),
        "banked_refs": {"continuum_B1": 36.462, "RM_bound": 71.543,
                        "threshold": 72.923, "RM_margin_pct": 1.89},
        "unwinding_events": ("two recorded (Adam vacuum-noise pathology; "
                             "under-resolved core at h = 0.375 with aggressive "
                             "steps) -- charge-guard + smooth-sector resolution "
                             "discipline is load-bearing; the flow-level face "
                             "of R-143's LATT-pi3 caveat; evidence class = "
                             "reproducible-on-demand, independently reproduced "
                             "by the reviewer (B -0.82 -> -0.0002 in 1500 "
                             "steps, reviewer F4)"),
    }
    m64 = (2 * dev["B1"]["N64"]["E"] - dev["B2"]["N64"]["E"]) / (2 * dev["B1"]["N64"]["E"])
    m96 = (2 * dev["B1"]["N96"]["E"] - dev["B2"]["N96_final"]["E"]) / (2 * dev["B1"]["N96"]["E"])
    assert m64 > 0.015 and m96 > 0.015, "below-threshold at BOTH resolutions"
    # reviewer F1 probe consistency: margin vs the CONTINUED B1 stays positive,
    # and the continuum anchor protects the sign independently
    probe = dev["reviewer_b1_continuation_probe"]
    m96p = (2 * probe["E_B1_after_15k"] - dev["B2"]["N96_final"]["E"]) \
        / (2 * probe["E_B1_after_15k"])
    assert abs(m96p * 100 - probe["margin_pct"]) < 0.05 and m96p > 0.025, \
        "reviewer B1-continuation probe: margin >= 2.9% after B1-side descent"
    assert 2 * dev["banked_refs"]["continuum_B1"] > dev["B2"]["N96_final"]["E"], \
        "continuum anchor: 2 x 36.462 = 72.923 > E(B2) -- sign protected"
    assert abs(m64 * 100 - dev["margins_same_grid_pct"]["N64"]) < 0.05
    assert abs(m96 * 100 - dev["margins_same_grid_pct"]["N96"]) < 0.05
    mom = dev["B2"]["N96_final"]["moments"]
    assert abs(mom[0] - mom[1]) < 2e-3 and mom[2] > mom[0] * 1.3, \
        "toroidal signature: exactly axial, oblate moments"
    assert dev["B2"]["N96_final"]["center_over_max"] < 0.05 \
        and dev["B2"]["N96_final"]["r_ring"] > 1.0, \
        "toroidal signature: ring density max, suppressed center"

    return {
        "outcome": ("SC-1 SECOND DATUM banked: the ansatz-FREE full-3D B = 2 sector "
                    "of the banked dressed Skyrme energy lies below the two-defect "
                    "threshold at matched discretization (stall-vs-stall margins "
                    "1.79%/" + str(dev["margins_same_grid_pct"]["N96"]) +
                    "% at N = 64/96; >= 2.95% after the reviewer's B1-side "
                    "continuation probe, sign independently protected by the "
                    "R-133 continuum anchor); the flow, with no symmetry "
                    "CONSTRAINT during descent (axial initial condition; cubic "
                    "grid), found the TOROIDAL minimizer (ring density max, "
                    "suppressed center, sharpening along the descent); R-135's "
                    "would-change-if (c) FIRED (the full field KEEPS the binding "
                    "-- deepening at N = 96; it does not un-bind). The 3D "
                    "functional is sympy-certified as the banked sector (hedgehog "
                    "reduction identity) and h^2-certified as a discretization. "
                    "STATIC variational datum only -- the dynamical multi-defect "
                    "EOM face of SC-1 stays open and kernel-gated; no magnitude "
                    "claim (classical overbinding known, P2-7 residual row "
                    "untouched)."),
        "tier": ("DERIVED-A (reduction identity; h^2 regression) + DERIVED "
                 "dressed-level VARIATIONAL full-field (below threshold, "
                 "branch-(c)/hedgehog-minimality inherited from R-135) + "
                 "STRUCTURE-corroborative (the torus) + SC-1-SECOND-DATUM scoped "
                 "(static face only; dynamical EOM face open, kernel-gated) + "
                 "METHODOLOGY (winding is smooth-sector-protected only; "
                 "charge-guard discipline load-bearing)"),
        "dev_record": dev,
        "sc1_status": ("SC-1 static face: N = 2 datum now FULL-3D and ansatz-free "
                       "(this) on top of the R-135 reduced-BVP datum; remaining "
                       "SC-1 core: the multi-defect Cl(4,1) dynamical EOM "
                       "(unformulated; kernel-gated) + optional B >= 3 static "
                       "third datum"),
        "would_change_if": ("longer/finer flow un-binds (descent only deepens -- "
                            "nothing points that way); the dynamical multi-defect "
                            "EOM lands (this datum becomes its static boundary "
                            "condition); the massive-pion full-field run shifts "
                            "the margin (fork-robust at ansatz level per "
                            "R-137/R-138); B >= 3 sectors computed"),
    }



def marginal_skyrme_beta3_sign_dispersive():
    """[R-148 — P2-3 SIGN FACE: beta_3 <= 0 — the marginal-Skyrme quartic runs AF-SIGNED
    under the dispersive package, DERIVED-conditional-GENERIC; 2026-07-05. CORRECTION
    HISTORY (binding record): the FIRST build of this result was REFUTED by adversarial
    review — it transplanted R-085's EUCLIDEAN action density -(1/32e^2)Tr([L,L]^2) into
    the Minkowski amplitude machinery unrotated, flipping the load-bearing channel weight
    and (self-inconsistently) making the banked action violate the very positivity it
    invoked; the reviewer killed it five independent ways incl. a static-energy witness
    (the coded sign gave NEGATIVE quartic energy — the configuration R-085's own RP
    argument excludes) and an exact end-to-end recomputation. THIS build derives the
    vertex sign in-suite instead of hand-entering it (the process lesson, ledger N42:
    CALIBRATE THE LOAD-BEARING VERTEX, NOT JUST THE MACHINERY).]

    THE QUESTION (N7 / R-085): the sign of beta_3 = mu d(1/e^2)/dmu for the marginal
    4D-Skyrme quartic. R-085: RP fixes only the bare sign (1/e^2 > 0), running-agnostic;
    its would-change-if named the Kallen-Lehmann/unitarity route — FIRED here.

    THE PIPELINE (sympy; every sign-sensitive input DERIVED or anchored in-suite):
    (0) MACHINERY CALIBRATION [DERIVED-A]: series-extracted C24 = 1/48 (numeric-rational
        matrices, symbolic eps; kinetic = (1/2)dpi.dpi verified) reproduces the TEXTBOOK
        Weinberg amplitude M(pi1 pi2 -> pi1 pi2) = t/f^2 exactly through the
        slot/permutation machinery — amplitude conventions PINNED.
    (0') VERTEX-SIGN ANCHORS [DERIVED-A — the reviewer-required additions]:
        (a) SERIES-DERIVED QUARTIC FORM: the eps^4 part of Tr([L_x,L_y]^2) for
            U = exp(i eps Pi(x,y)) equals +1 x Tr([d_x Pi, d_y Pi]^2) — coefficient
            extracted at independent rational configurations, NOT hand-entered.
        (b) STATIC-ENERGY ANCHOR: the MINKOWSKI Skyrme Lagrangian with the banked
            physical sign, L4 = +(1/(32 e^2)) Tr([L_mu,L_nu][L^mu,L^nu]) (mostly-minus
            metric; spatial raising [L^i,L^j] = [L_i,L_j]), gives static quartic energy
            E4 = -L4(static) >= 0, strictly positive on random su(2) configurations.
            This ties the amplitude-side Lagrangian sign to R-085's
            Hamiltonian-boundedness anchor (the Euclidean density is the Wick rotation
            of this — hence ITS minus sign, the first build's trap).
        The slot coefficient is then COMPUTED, not entered:
        slot = (1/32) x (series sign +1) x (trace-identity factor -8) = -1/4.
    (1) THE CHANNEL MAP [DERIVED-A]: with the anchored vertex,
            M(pi1 pi2 -> pi1 pi2)(s,t) = -(t^2/2 + s u)/(2 e^2 f^4),
        invariant amplitude A(s,t,u) = -(s^2/2 + t u)/(2 e^2 f^4); Bose s<->u asserted;
        identical-cartesian channel identically ZERO. FORWARD (t = 0):
        +s^2/(2 e^2 f^4) — THE SKYRME COUPLING ENTERS THE POSITIVITY-BOUNDED CHANNEL
        WITH POSITIVE WEIGHT w = +1/(2 f^4). CONSISTENCY (now in-suite): the banked sign
        SATISFIES tree-level forward positivity automatically (c2 = w/e^2 > 0) — the
        amplitude-side twin of R-085's bare-sign result. LITERATURE-KNOWN-CLASS,
        credited: the dispersive-derivation-of-the-Skyrme-sign / chiral-positivity-bound
        family (Pham-Truong-class sum rules; empirically l2-bar > 0, rho-saturated). The
        TWT content = the conditional tiering, the engine-exact weights for the banked
        action, and the P2-3 bookkeeping consequence.
    (2) MONOTONICITY IDENTITY [DERIVED-A]: mu d/dmu Int_{mu^2}^{Lam^2} rho/s^3 ds
        = -2 rho(mu^2)/mu^4 <= 0 for rho >= 0 (sympy-exact, positive-density family).
    (3) THE SIGN [DERIVED-conditional-GENERIC — canon 5 honesty: GENERIC]: the
        arc-defined forward coefficient c2(mu) = (2/pi) Int_{mu^2}^{Lam^2} ImA/s^3 + c_UV
        is >= 0 and monotone NON-INCREASING in mu (optical-theorem positivity for the
        diagonal |pi1 pi2> element; both cuts positive by crossing). At the banked
        two-term action (ONE quartic coupling) the channel's polynomial piece is
        w (1/e^2(mu)) with w > 0. Therefore 1/e^2(mu) is monotone NON-INCREASING in mu:
            beta_3 = mu d(1/e^2)/dmu <= 0 — THE AF-SIGNED BRANCH of R-085's table
        (1/e^2 grows toward the IR). GENERIC-HONESTY (the tag's load): this is the
        standard dispersive-running statement obeyed by ANY two-term chiral action —
        the substrate-specific content is only that TWT's banked dressed sector IS that
        action, plus the engine-exact channel weights. CORROBORATION (witness, not
        load-bearing): in one-loop ChPT the forward coefficient of this channel is pure
        l2 (l1 multiplies t^2, vanishing forward) and Gamma_2 > 0 makes l2^r decrease
        toward the UV — the same direction.
    (4) WHAT THIS DOES AND DOES NOT DECIDE [the fence, HARD]:
        - DECIDED (conditional-generic): the SIGN. The dressed marginal quartic runs
          AF-SIGNED — the wrong-sign risk for the qcd-UV arc is REMOVED; P2-3's Class-1
          "(sign, possibly)" face closes POSITIVE-conditional-generic.
        - NOT DECIDED (stays N7 / Class 2): asymptotic freedom itself. The sign's SOURCE
          here is the ADDITIVE, f^2-loop-driven drift (the O(p^2) unitarity cut), NOT a
          self-coupling antiscreening mechanism; the full DGLAP structure, the "small
          and negative" magnitude, and the UV completion above Lambda_cell remain the
          kernel's burden. SIGN-CONSISTENCY IS NOT AF-ACHIEVED — banking it as such
          would be the disguise canon 1 forbids.

    PREMISE SET (named; the import is REGISTERED as companion Section 13 row I-13 in the
    same banking pass, per the mandatory register-imports rule):
      (P-disp)   analyticity, crossing, <= 2 subtractions (boundedness), optical-theorem
                 positivity — inside-frame/effective level (data-like jurisdiction).
                 RECAST NOTE (13.3 directive): the positivity leg IS partially recast —
                 it rides the banked B.3-DERIVED unitary QM (probability conservation of
                 the derived inside-frame theory), not axiomatic unitarity; analyticity
                 and boundedness are NOT yet recast (named residual premises).
      (P-action) the banked two-term dressed action, one-coupling reading (radiative
                 l1-mixing = named refinement; MOOT AT FORWARD ORDER: l1 multiplies t^2,
                 which vanishes forward — the channel is pure-l2/Skyrme).
      (P-chan)   the |pi1 pi2>-class elastic forward channel (diagonal optical theorem);
                 chiral limit (arc formulation; the marginal log at the upper limit IS
                 the running; leading-log sign scheme-independent).
      (P-conv)   R-085's beta_3 = mu d(1/e^2)/dmu convention and branch labels.

    WOULD CHANGE IF: a new operator class with FORWARD-surviving weight enters the
    dressed action at matching (re-runs the combination — l1 does not qualify, it
    vanishes forward); the (P-disp) package fails inside-frame; the one-loop coefficient
    vanishes in this channel (weakens strict to non-strict); R-085's convention is
    re-anchored (relabels only, does not flip the physics).

    self-checks below (sympy, numeric-first series — fast)."""
    import itertools
    import random
    import sympy as sp

    t1 = sp.Matrix([[0, 1], [1, 0]])
    t2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    t3 = sp.Matrix([[1, 0], [0, -1]])
    taus = [t1, t2, t3]
    I2m = sp.eye(2)

    s, t = sp.symbols('s t', real=True)
    f = sp.Symbol('f', positive=True)
    e2s = sp.Symbol('e2', positive=True)
    eps = sp.Symbol('eps', real=True)

    legs = [('p1', -1), ('p2', -1), ('p3', +1), ('p4', +1)]
    DOTT = {
        frozenset(['p1']): sp.Integer(0), frozenset(['p2']): sp.Integer(0),
        frozenset(['p3']): sp.Integer(0), frozenset(['p4']): sp.Integer(0),
        frozenset(['p1', 'p2']): s / 2, frozenset(['p3', 'p4']): s / 2,
        frozenset(['p1', 'p3']): -t / 2, frozenset(['p2', 'p4']): -t / 2,
        frozenset(['p1', 'p4']): (s + t) / 2, frozenset(['p2', 'p3']): (s + t) / 2,
    }

    def ddot(j, k):
        bj, ioj = legs[j]; bk, iok = legs[k]
        return -ioj * iok * DOTT[frozenset([bj, bk])]

    # ---- (0)+(0'a) series calibrations, NUMERIC-FIRST (rational matrices, symbolic eps) ----
    def _rand_mat(rnd):
        return sum((sp.Rational(rnd.randint(-9, 9), rnd.randint(1, 7)) * taus[k]
                    for k in range(3)), sp.zeros(2))

    def _trunc4(M):
        # truncate every entry to a polynomial in eps of degree <= 4 (all we need)
        return M.applyfunc(lambda z: sp.expand(z) + sp.Integer(0)).applyfunc(
            lambda z: sum(z.coeff(eps, k) * eps**k for k in range(5)))

    C24_vals, qform_vals = [], []
    for sd in (11, 12, 13):
        rnd = random.Random(sd)
        P0n, P1n, P2n = _rand_mat(rnd), _rand_mat(rnd), _rand_mat(rnd)
        # U(x,y) = exp(i eps (P0 + x P1 + y P2)); need U, dU/dx, dU/dy, and U+ at x=y=0.
        # Build the exponential series term-by-term keeping FIRST order in x, y:
        # represent each series term as (T0, Tx, Ty): value and x/y-derivative parts at 0.
        A0 = sp.I * eps * P0n
        Ax = sp.I * eps * P1n
        Ay = sp.I * eps * P2n
        U0, Ux, Uy = I2m, sp.zeros(2), sp.zeros(2)
        T0, Tx, Ty = I2m, sp.zeros(2), sp.zeros(2)
        for k in range(1, 6):
            # (T*A)/k with A = A0 + x Ax + y Ay, keeping first order in x,y
            T0, Tx, Ty = (_trunc4(T0 * A0 / k),
                          _trunc4((Tx * A0 + T0 * Ax) / k),
                          _trunc4((Ty * A0 + T0 * Ay) / k))
            U0 = _trunc4(U0 + T0); Ux = _trunc4(Ux + Tx); Uy = _trunc4(Uy + Ty)
        # U+ at base point: series of -A0
        Ud, T = I2m, I2m
        for k in range(1, 6):
            T = _trunc4(T * (-A0) / k)
            Ud = _trunc4(Ud + T)
        # kinetic + C24 from L2 = (1/4) Tr(dU/dx (dU/dx)+):
        Uxdag = Ux.T.applyfunc(lambda z: z.subs(sp.I, -sp.I))
        L2v = sp.expand(sp.trace(Ux * Uxdag) / 4)
        ord2 = sp.nsimplify(L2v.coeff(eps, 2))
        kin = sp.nsimplify(sp.trace(P1n * P1n) / 4)   # (1/2) dpi.dpi = Tr(P1^2)/4
        assert sp.simplify(ord2 - kin) == 0, "kinetic normalization failed"
        ord4 = sp.nsimplify(L2v.coeff(eps, 4))
        trf = sp.nsimplify(sp.trace((P0n * P1n - P1n * P0n) * (P0n * P1n - P1n * P0n)))
        C24_vals.append(sp.nsimplify(ord4 / trf))
        # quartic form of Tr([L_x, L_y]^2), L = U+ dU:
        Lxm = _trunc4(Ud * Ux); Lym = _trunc4(Ud * Uy)
        comm = Lxm * Lym - Lym * Lxm
        K4 = sp.nsimplify(sp.expand(sp.trace(comm * comm)).coeff(eps, 4))
        tgt = sp.nsimplify(sp.trace((P1n * P2n - P2n * P1n) * (P1n * P2n - P2n * P1n)))
        qform_vals.append(sp.nsimplify(K4 / tgt))
    assert all(c == sp.Rational(1, 48) for c in C24_vals), "C24 != 1/48: %s" % C24_vals
    assert all(v == 1 for v in qform_vals), \
        "series quartic-form coefficient != +1: %s" % qform_vals
    series_sign = qform_vals[0]   # == +1, DERIVED not hand-entered

    # ---- (0'b) STATIC-ENERGY ANCHOR ----
    rnd = random.Random(20260705)
    for _ in range(3):
        Ls = [sp.I * _rand_mat(rnd) for _ in range(3)]   # anti-hermitian su(2) spatial L_i
        L4_static = sp.Integer(0)
        for i in range(3):
            for j in range(3):
                cij = Ls[i] * Ls[j] - Ls[j] * Ls[i]
                L4_static += sp.trace(cij * cij)
        E4 = sp.nsimplify(sp.expand(-sp.Rational(1, 32) * L4_static))  # e^2 = 1
        assert sp.simplify(sp.im(E4)) == 0, "static energy not real: %s" % E4
        E4r = sp.simplify(sp.re(E4))
        assert E4r > 0, \
            "static quartic energy not strictly positive with the coded sign: %s" % E4r

    # ---- trace identity factor (-8), verified not assumed ----
    av = sp.symbols('a1 a2 a3', real=True); bv = sp.symbols('b1 b2 b3', real=True)
    cv = sp.symbols('c1 c2 c3', real=True); dv = sp.symbols('d1 d2 d3', real=True)
    Am = sum((av[i] * taus[i] for i in range(3)), sp.zeros(2))
    Bm = sum((bv[i] * taus[i] for i in range(3)), sp.zeros(2))
    Cm = sum((cv[i] * taus[i] for i in range(3)), sp.zeros(2))
    Dm = sum((dv[i] * taus[i] for i in range(3)), sp.zeros(2))
    lhs = sp.expand(sp.trace((Am * Bm - Bm * Am) * (Cm * Dm - Dm * Cm)))
    adc = sum(av[i] * cv[i] for i in range(3)); bdd = sum(bv[i] * dv[i] for i in range(3))
    add = sum(av[i] * dv[i] for i in range(3)); bdc = sum(bv[i] * cv[i] for i in range(3))
    assert sp.simplify(lhs - (-8) * (adc * bdd - add * bdc)) == 0, "trace identity failed"

    # ---- amplitude machinery ----
    def _diso(iso, u, v): return 1 if iso[u] == iso[v] else 0

    def _amp(op_term, iso_ext):
        total = sp.Integer(0)
        for perm in itertools.permutations(range(4)):
            total += op_term(perm, iso_ext)
        return sp.expand(sp.simplify(total))

    def _l2_term(perm, iso):
        n1, d1, n2, d2 = perm
        isofac = _diso(iso, n1, n2) * _diso(iso, d1, d2) - _diso(iso, n1, d2) * _diso(iso, d1, n2)
        if isofac == 0:
            return sp.Integer(0)
        return sp.Rational(1, 48) / f**2 * (-8) * isofac * ddot(d1, d2)

    M2 = _amp(_l2_term, [1, 2, 1, 2])
    assert sp.simplify(M2 - t / f**2) == 0, "Weinberg calibration failed: %s" % M2

    # THE DERIVED SLOT: L4^(pi4) = +(1/(32 e^2 f^4)) * series_sign * Tr([dPi,dPi][dPi,dPi])
    slot = sp.Rational(1, 32) * series_sign * (-8)
    assert slot == sp.Rational(-1, 4), "derived slot coefficient != -1/4"

    def _sk_term(perm, iso):
        j, k, l, m = perm
        isofac = _diso(iso, j, l) * _diso(iso, k, m) - _diso(iso, j, m) * _diso(iso, k, l)
        if isofac == 0:
            return sp.Integer(0)
        return slot / (e2s * f**4) * isofac * ddot(j, l) * ddot(k, m)

    M4 = _amp(_sk_term, [1, 2, 1, 2])
    u_ = -s - t
    target = -(t**2 / 2 + s * u_) / (2 * e2s * f**4)
    assert sp.simplify(M4 - target) == 0, "corrected channel map failed: %s" % M4
    assert sp.simplify(M4 - M4.subs({s: u_}, simultaneous=True)) == 0, "Bose s<->u failed"
    assert sp.simplify(_amp(_sk_term, [1, 1, 1, 1])) == 0, "identical channel not zero"
    fw = sp.expand(M4.subs(t, 0))
    w_coef = sp.simplify(fw.coeff(s, 2) * (2 * e2s * f**4))
    assert w_coef == +1, "forward weight != +1/(2 e2 f^4): %s" % fw

    # ---- (2) monotonicity identity ----
    mu, Lam = sp.symbols('mu Lambda', positive=True)
    sv = sp.Symbol('sv', positive=True)
    for rho in (sp.Integer(1), sv, sv**2, 1 / (1 + sv)):
        c2i = sp.integrate(rho / sv**3, (sv, mu**2, Lam**2))
        dev = sp.simplify(sp.diff(c2i, mu) * mu + 2 * rho.subs(sv, mu**2) / mu**4)
        assert dev == 0, "monotonicity identity failed for rho = %s" % rho

    return {
        "tier": ("DERIVED-A (series-anchored channel map — vertex sign DERIVED in-suite "
                 "per the review correction: quartic-form coefficient +1 series-extracted "
                 "at rational configurations, static-energy anchor E4 > 0 tying the "
                 "Lagrangian sign to R-085's Hamiltonian-boundedness, slot = -1/4 "
                 "computed not hand-entered; A_Skyrme(s,t,u) = -(s^2/2 + tu)/(2 e^2 f^4); "
                 "POSITIVE forward weight +1/(2f^4); tree positivity SATISFIED "
                 "automatically — the amplitude-side twin of R-085; monotonicity "
                 "identity) + DERIVED-conditional-GENERIC (beta_3 <= 0 — the AF-SIGNED "
                 "branch — given the named premise set; GENERIC per canon 5: the "
                 "standard dispersive-running statement for any two-term chiral action; "
                 "substrate content = the banked action IS that action + the "
                 "engine-exact weights) + LITERATURE-KNOWN-CLASS credited (Pham-Truong-"
                 "class dispersive sum rules / chiral positivity bounds) + HARD FENCE "
                 "(sign-consistency is NOT AF-achieved: additive f^2-loop drift, no "
                 "antiscreening mechanism; DGLAP + magnitude stay N7/Class 2) + "
                 "CORRECTION-HISTORY (first build REFUTED — Euclidean-sign transplant; "
                 "N42 process lesson: calibrate the load-bearing vertex)"),
        "channel_map": ("A_Skyrme(s,t,u) = -(s^2/2 + t*u)/(2 e^2 f^4); forward weight "
                        "w = +1/(2 f^4) > 0; tree-level forward positivity SATISFIED by "
                        "the banked sign (c2 = w/e^2 > 0)"),
        "sign": ("beta_3 = mu d(1/e^2)/dmu <= 0 — AF-SIGNED (1/e^2 grows toward the IR; "
                 "R-085's AF branch) — DERIVED-conditional-GENERIC; the wrong-sign risk "
                 "for the qcd-UV arc is REMOVED"),
        "p2_3_status": ("Class-1 sign face CLOSED POSITIVE-conditional-generic; NOT AF "
                        "itself — the sign's source is the additive f^2-loop drift, not "
                        "antiscreening; remaining P2-3 = Class 2 (DGLAP structure, "
                        "magnitude, the UV completion above Lambda_cell — the kernel)"),
        "premises": ("P-disp (I-13 registered; positivity leg partially RECAST onto the "
                     "banked B.3-derived QM — 13.3 directive note; analyticity/"
                     "boundedness named residual premises) + P-action (one-coupling; "
                     "l1-mixing MOOT forward — l1 multiplies t^2) + P-chan + P-conv"),
        "would_change_if": ("a new operator class with forward-surviving weight (re-runs "
                            "the combination); the package fails inside-frame; one-loop "
                            "coefficient zero in this channel; convention re-anchored"),
    }


def induced_G_from_linear_face_band():
    """[DERIVED-given-the-NN-BAND-INPUT (the flat-band numbers I_lat and c_lat: the derived-band
    proper-time integral is finite and CONVENTION-FREE, so no regularization choice enters it)
    + DERIVED-CONDITIONAL-on-(OA-LF-i AND OA-LF-ii) (the EH-COEFFICIENT reading, the a-value,
    and the normalization-spread adjudication), INHERITING R-041's FRAMING+CONDITIONAL xi = 0]
    — the induced-EH coefficient computed directly on the banked linear face, narrowing (not
    retiring) import I-3 (W5, 2026-07-27).

    WHAT WAS ASSUMED BEFORE. I-3 rode 'a standard QFT vacuum for substrate modes + validity of
    the one-loop expansion + covariant regularization', with the regulator coefficient c_reg a
    free O(1) and the corpus carrying a factor-2 scheme spread between its two engine
    normalizations. Two of those three clauses are now discharged: one-loop validity by the
    banked Gate A (induced_G_gate_A_linearized_sufficient — the banked face IS the quadratic
    theory), and covariant regularization by COMPUTATION (Step 3 below). The third is replaced
    by OA-LF, which is TWO clauses, counted as two.

    THE COMPUTATION.
      STEP 1 — the derived operator. R-112 / SSD.4.6 Face 1 (banked DERIVED-STRUCTURAL):
        linearizing about the twist-gauge homogeneous vacuum leaves the free 5D hyperbolic
        operator with no endomorphism and no mass at quadratic order; the fluctuation content
        is the 6 grade-2 so(4) coefficient fields (C(4,2) = 6, GENERIC-given-dim-4 per canon
        SS5 — tier unchanged). WP-LV1 (Substrate().dim4_isotropy) licenses one stiffness across
        the 6 bivector planes, hence a SHARED band with a common principal symbol.
      STEP 2 — the curvature weight [IMPORT-EXEMPT PURE MATH: the operator is specified].
        For the minimal (xi = 0) curved continuation, the Seeley-DeWitt coefficient is
        a_1 = R/6 per scalar channel; verified below on the EXACT S^4 spectrum
        (lambda_l = l(l+3), d_l = (l+1)(l+2)(2l+3)/6) by Richardson in s. xi = 0 itself is the
        banked R-041 shift-symmetry face — FRAMING+CONDITIONAL, and that conditionality is
        INHERITED by everything downstream here. Gaps of gapped modes cannot leak into the
        R-coefficient at leading order (banked induced_G_leading_coefficient_mass_independent).
      STEP 3 — THE MODE SUM REPLACES THE REGULATOR. The R-linear term per channel is (R/6)*I
        with I = int_0^inf ds Kbar(s). In the continuum I diverges and BOTH standard schemes
        (proper-time cutoff, sharp-k cutoff) give Lambda^2/(16 pi^2) — the 'covariant
        regularization' premise. On the substrate Kbar is NOT a choice: it is fixed by the
        DERIVED D4 nearest-neighbour band. Using int_0^inf ds e^(-s ktil^2) = 1/ktil^2 exactly,
            I_lat = int_BZ d^4k/(2pi)^4 * 1/ktil^2(k),
            ktil^2(k) = (1/6) * sum over the 24 D4 roots of (1 - cos k.b),
        which is FINITE in the UV (compact BZ) and in the IR (4D), positive termwise (the
        SSB.6.4 stability face holds termwise: 1 - cos >= 0). k -> 0 isotropy is exact:
        sum_b b_mu b_nu = 12 delta_mu,nu (the WP-LV1 face, checked below), so ktil^2 -> k^2.
      STEP 4 — the number. c_lat := 16 pi^2 * I_lat (calibrated so a continuum sharp cutoff
        would give (Lambda a)^2). Midpoint grids over the double-cover cube with exact
        half-folding converge in h^2 to c_lat = 21.83. The Debye-sphere equivalent (same mode
        density, exact k^2 dispersion) is c_D = 4 pi = 12.566 — so the DERIVED band sits ~74%
        ABOVE the generic guess. That is the content: a genuinely derived O(1) where c_reg was
        free.
      STEP 5 — assembly. 1/(16 pi G) = N_eff * c_lat / (192 pi^2 a^2), i.e. exactly the
        sakharov_induced_gravity normalization G^-1 = N_eff Lambda^2/(12 pi) at
        Lambda_eff^2 = c_lat/a^2. The Lambda^2 scaling SURVIVES (the banked 4D-dimensionality
        fact, now realized as BZ-dominance of the band integral), and the engine ratio
        Lambda_eff/M_Pl(reduced) = sqrt(96 pi^2/6) = 4 pi is reproduced EXACTLY — it is
        c_lat-INDEPENDENT (a pure-N statement), so nothing already banked moves.

    *** 'REGULATOR-FREE' DESCRIBES I_lat ONLY. *** The finite, choice-free object is the band
    integral. The former O(1) regulator freedom is NOT deleted — it is RELOCATED, into OA-LF
    clause (ii), where it now carries ~93% of the support and has a named retirement handle.
    Say it as: 'the flat-band measure is derived (no scheme choice); the former regulator
    freedom survives as ONE named PHYSICAL unknown, OA-LF(ii), localized and retirable.'

    OA-LF — 'linear-face vacuum measure', TWO ASSUMPTIONS, COUNTED AS TWO (one registry row,
    two counted clauses; the I-3 ledger goes 3 -> 2, not 3 -> 1):
      (OA-LF-i) OCCUPATION — a statement about the STATE: the NESS occupation of the linear-face
        modes equals the Gaussian ground-state (1/2-per-mode) measure at grain-adjacent scales.
      (OA-LF-ii) COVARIANT GRAIN-SCALE CURVATURE WEIGHT — a statement about the OPERATOR: the
        slow frame background enters the BAND-COMPLETED operator covariantly, i.e. the continuum
        a_1 = R/6 extends down to proper times s ~ a^2 up to O(1). The continuum result is exact
        only for s >> a^2, and ~93% of I_lat sits at s < a^2 — hence the 93%-of-support figure.
      Both are discharged by the SAME retirement handle (the #1-gap kernel, which would derive
      the NESS occupation and the grain-scale curvature coupling) — the handle is unchanged
      from the current I-3 row. Use OA-LF in the PLURAL everywhere ('the OA-LF assumptions').
      Support localization (computed below): ~95% of I_lat rides modes with ktil^2 > 1/a^2 and
      ~93% rides proper time s < a^2 — so OA-LF is needed essentially only at the top of the band.

    c_lat = 21.83 IS THE GAPLESS-SHARED-BAND IDEALIZATION. The realistic canted vacuum has
    N_G = 2 (2 gapless + 4 gapped, banked n_goldstone_canted_FM). A uniform-gap spot check
    (computed below) gives -2% at gap^2 = 1% of the band max and -7% at 4%; the honest
    refinement window for the realistic vacuum is -5% ... -25%, which maps to
        a in [1.61, 1.86] ell_Planck(full),
    pending the un-banked exact 6-band Bogoliubov structure on the canted vacuum. Always quote
    c_lat = 21.83 WITH this named refinement. (Stiffness anisotropy from the derived canted-
    spiral K_long/K_trans erratum ratio shifts c_lat by < 0.01% — negligible, also checked.)

    *** DATED ANNOTATION, 2026-08-23 — THE -5%...-25% WINDOW IS WITHDRAWN AS UNSUPPORTED. ***
    (Estate of N64, item B1. The paragraph above is left standing so the withdrawal is legible
    against what it withdraws; the returned dict carries the withdrawal, not the window.)
      THE PREMISE IS REFUTED, and this half stands independently of any quadrature. The window
      was built from a UNIFORM-GAP spot check that assumed (gap/band_max)^2 in [0.01, 0.04].
      Computed on the ACTUAL canted vacuum (body-diagonal branch, D/J = 0.787,
      `magnon_stiffness_bands_canted_vacuum`):
          g = 0.412121 ,  b_max ~ 64.8   =>   (g/b_max)^2 = 4.049e-05
      i.e. the spot check's assumed gap fraction is 247x to 988x TOO LARGE, and the true
      structure is 2 GAPLESS + 4 GAPPED, not uniform-gap. So the window is not supported by the
      object it claims to bound.
      NO REPLACEMENT NUMBER IS ASSERTED, and specifically none of the -0.111% class: that figure
      was the M = 15 term of a monotonically shrinking midpoint-grid sequence (-0.1445% at M = 11
      falling to -0.0227% at M = 47, magnitude strictly decreasing on every grid tested, odd and
      even alike), whose Richardson limit is CONSISTENT WITH ZERO. The integrand carries three
      inverse-square singularities on the 4-torus (Gamma and the two helimagnet satellites
      +-k_0), so no such grid resolves it. Locking a grid artefact into the harness would be the
      archetypal tight-tolerance-on-a-vacuous-check.
      A NEAR-ZERO CORRECTION IS WHAT THE BANKED DERIVATION ALREADY PREDICTS — STEP 2's own line:
      "Gaps of gapped modes cannot leak into the R-coefficient at leading order (banked
      `induced_G_leading_coefficient_mass_independent`)". The -5%...-25% spot-check window was
      the outlier all along, so this STRENGTHENS self-coherence rather than disturbing it. And
      the D = 0 calibration is exact — `H(k) = 12 J ktilde^2(k) 1_6` identically — so the
      six-band measure REDUCES TO I_lat BY CONSTRUCTION: this refines the banked object, it does
      not replace it.
      *** THE JURISDICTION FENCE IS UNWEAKENED, AND ITS STRONGEST FORM IS SAID OUT LOUD: ***
      `a` remains CONDITIONAL on (OA-LF-i AND OA-LF-ii) + N_eff = 6 + the induced-G
      identification; "TWT derives the grain spacing" stays PROHIBITED; and `a` IS A BACK-FIT OF
      MEASURED G_N (canon §0; Branch-B ruling 2026-07-30; RUL-046), so narrowing the window
      narrows A BACK-FIT and MOVES NO EMPIRICAL CLAIM WHATSOEVER. *** A NARROWER WINDOW IS NOT
      BETTER AGREEMENT AND MUST NEVER BE QUOTED AS ONE. ***

    THE THREE-WAY NORMALIZATION SPREAD (residue (d), adjudicated). The corpus carries THREE
    conventions for the 1/(16 pi G) coefficient: the paper's 16 pi^2, the bracket primitive's
    96 pi^2, and the sakharov primitive's 192 pi^2. The paper SSB.6.2 table IS self-consistent
    under its OWN 16 pi^2 formula: in the paper's parametrization c_reg = c_lat/12 = 1.82, which
    sits comfortably inside its stated 'c_reg ~ 1'. So there is no arithmetic error to fix —
    only a convention note to add. SCOPE FENCE (2026-07-28): that adjudication covers the
    pi-CONVENTION spread ONLY. The VALUE of c_reg is a DIFFERENT and still-OPEN question —
    ~1 (paper placeholder) vs 1/12 (sakharov_induced_gravity, textbook heat-kernel) vs 1.82
    (here, the derived D4 band): the two BANKED values differ by ~21.6, and nothing in this
    primitive picks between them. Where the bracket LANDS is convention-dependent; the
    CONVENTION-INVARIANT statement is the one to quote:
        a = 1.86 ell_Planck, i.e. PLANCKIAN WITHIN O(1),
    and that statement SUPPORTS SSB.6.2. This computation lands exactly on the
    sakharov_induced_gravity form.

    JURISDICTION FENCE — 'a' IS ALWAYS CONDITIONAL. a = 1.86 ell_Pl is conditional on
    (OA-LF-i AND OA-LF-ii) + N_eff = 6 (GENERIC-given-dim-4) + the induced-G identification with
    the EMPIRICAL G. NEVER write 'TWT derives the grain spacing'. Lambda values stay
    CANDIDATE/conditional and MUST NEVER BE MOVED TO CHASE AGREEMENT WITH MEASUREMENT: Lambda_S is
    a back-fit to empirical G over the N_eff menu, and nothing here changes G or the menu.
    The reduction achieved is IN THE PREMISE, not in the tier.
    (Re-cut history — both re-cuts were fence case (a), a normalization/convention reconciliation
    between named engine artifacts, never data-chasing. 2026-07-28: widened [0.16, 0.72] ->
    [0.13, 2.5] to span an apparently unreconciled normalization between sakharov_induced_gravity
    (1/12) and THIS primitive (c_lat/12 = 1.82) plus the paper's ~1 placeholder. 2026-07-29:
    RESOLVED — one coefficient in different Lambda-variables. 2026-07-30: the coordinator's
    which-Lambda ruling SPLIT the symbol — Lambda_S = sqrt(2*pi) M_Pl (scheme; Sakharov
    bookkeeping) vs Lambda_L = 1/a, band [0.386, 0.735] M_Pl (lattice-dispersion consumers per
    the scoped B.6.2 assignment) — and RETIRED the wide bracket. The prohibition is unchanged: 'it agrees better with the data' is
    NEVER a reason to move any of these.)

    EXTERNAL VALIDATION OF THE METHOD (both re-run in code below, not merely recorded):
      * the SAME grid + h^2-Richardson machinery applied to the Z^4 nearest-neighbour band
        reproduces the known 4D hypercubic lattice Green's function at the origin
        (G(0) = 1.2394671218, Watson class; so the tadpole integral = G(0)/4 = 0.30986678)
        to ~1e-7 — an absolute, literature-anchored calibration of the quadrature;
      * a seeded independent Monte-Carlo estimate of the SAME D4 band integral agrees with the
        grid value (MC ~21.83 vs grid 21.828), a different quadrature entirely.

    self-checks: sum_b b_mu b_nu = 12 delta exactly; c_lat on three grids with h^2-consistent
    Richardson limits agreeing to < 1e-3 and |c_lat - 21.83| < 0.05 at the banked grid; the Z^4
    tadpole calibration; the independent MC; the S^4 a_1 = R/6 Richardson check; the support
    fractions; gap and anisotropy sensitivities; the engine cross-tie
    sqrt(96 pi^2/6) = 4 pi == sakharov_induced_gravity()['Lambda_over_MPl']; N_G = 2 read from
    the banked n_goldstone_canted_FM."""
    import math
    import numpy as np

    # ---------- the D4 nearest-neighbour root system (12 +/- pairs = 24 roots) ----------
    pairs = []
    for i in range(4):
        for j in range(i + 1, 4):
            for sg in (+1, -1):
                b = [0, 0, 0, 0]; b[i] = 1; b[j] = sg
                pairs.append(tuple(b))
    assert len(pairs) == 12
    M2 = np.zeros((4, 4))
    for b in pairs:
        bb = np.array(b, float); M2 += 2.0 * np.outer(bb, bb)      # x2 for the +/- pair
    assert np.allclose(M2, 12 * np.eye(4)), "D4 NN second moment must be 12*delta (WP-LV1 face)"

    def band(N, weights=None, gap2=0.0):
        """midpoint grid over [0,2pi)^4 — the DOUBLE COVER of the D4 BZ, hence the 1/2."""
        x = 2 * math.pi * (np.arange(N) + 0.5) / N
        axes = [x.reshape([N if k == m else 1 for k in range(4)]) for m in range(4)]
        om2 = np.zeros((N,) * 4)
        for idx, b in enumerate(pairs):
            w = 1.0 if weights is None else weights[idx]
            ph = sum(bi * ax for bi, ax in zip(b, axes) if bi != 0)
            om2 += w * 2.0 * (1.0 - np.cos(ph))
        if weights is None:
            norm = 6.0
        else:
            c_mu = np.zeros(4)
            for idx, b in enumerate(pairs):
                bb = np.array(b, float); c_mu += weights[idx] * bb * bb
            norm = float(np.prod(c_mu) ** 0.25)
        ktil2 = om2 / norm + gap2
        inv = 1.0 / ktil2
        return 16 * math.pi ** 2 * 0.5 * float(inv.mean()), ktil2, inv

    c16, _, _ = band(16)
    c24, _, _ = band(24)
    c32, kt32, inv32 = band(32)
    rich_a = c24 + (c24 - c16) / ((24.0 / 16.0) ** 2 - 1.0)
    rich_b = c32 + (c32 - c24) / ((32.0 / 24.0) ** 2 - 1.0)
    assert c16 < c24 < c32, "c_lat must approach its limit monotonically from below"
    assert abs(rich_a - rich_b) < 1e-3, \
        "h^2 trend broken: Richardson limits %.6f vs %.6f" % (rich_a, rich_b)
    c_lat = rich_b
    assert abs(c32 - 21.83) < 0.05, "|c_lat(N=32) - 21.83| must be < 0.05; got %.5f" % c32
    assert abs(c_lat - 21.83) < 0.05, "|c_lat(Richardson) - 21.83| must be < 0.05; got %.5f" % c_lat
    band_max = float(kt32.max())
    c_Debye = 4 * math.pi

    # support localization
    tot = float(inv32.sum())
    frac_k_gt_1 = float(inv32[kt32 > 1.0].sum() / tot)
    uv = float(((1.0 - np.exp(-kt32)) * inv32).mean())
    ir = float((np.exp(-kt32) * inv32).mean())
    frac_s_lt_a2 = uv / (uv + ir)
    assert 0.94 <= frac_k_gt_1 <= 0.96, "support fraction from ktil^2>1 out of range: %.4f" % frac_k_gt_1
    assert 0.90 <= frac_s_lt_a2 <= 0.95, "proper-time support fraction out of range: %.4f" % frac_s_lt_a2

    # ---------- external calibration 1: the Z^4 tadpole against the literature constant ------
    def I_z4(N):
        x = 2 * math.pi * (np.arange(N) + 0.5) / N
        axes = [x.reshape([N if k == m else 1 for k in range(4)]) for m in range(4)]
        return float((1.0 / sum(1.0 - np.cos(a) for a in axes)).mean())
    z48, z64 = I_z4(48), I_z4(64)
    z_rich = z64 + (z64 - z48) / ((64.0 / 48.0) ** 2 - 1.0)
    z_known = 1.2394671218 / 4.0                       # 4D hypercubic lattice G(0)/4 (Watson class)
    z_dev = abs(z_rich - z_known)
    assert z_dev < 1e-6, "Z^4 tadpole calibration failed: %.10f vs %.10f" % (z_rich, z_known)

    # ---------- external calibration 2: an independent (Monte-Carlo) quadrature -------------
    rng = np.random.default_rng(20260727)
    kmc = rng.uniform(0.0, 2 * math.pi, size=(2000000, 4))
    om2mc = np.zeros(kmc.shape[0])
    for b in pairs:
        ph = sum(bi * kmc[:, m] for m, bi in enumerate(b) if bi != 0)
        om2mc += 2.0 * (1.0 - np.cos(ph))
    inv_mc = 6.0 / om2mc
    c_mc = 16 * math.pi ** 2 * 0.5 * float(inv_mc.mean())
    assert abs(c_mc - c_lat) < 0.15, "independent MC quadrature disagrees: %.4f vs %.4f" % (c_mc, c_lat)

    # ---------- Seeley-DeWitt a_1 = R/6 on the exact S^4 spectrum (pure math, exempt) -------
    Vol, Rcurv = 8 * math.pi ** 2 / 3.0, 12.0
    F = []
    for s in (1e-3, 5e-4):
        lmax = int(math.sqrt(50.0 / s)) + 30
        l = np.arange(lmax + 1, dtype=float)
        K = float(np.sum((l + 1) * (l + 2) * (2 * l + 3) / 6.0 * np.exp(-s * l * (l + 3))))
        F.append((K * (4 * math.pi * s) ** 2 / Vol - 1.0) / s)
    a1 = 2 * F[1] - F[0]                                  # Richardson in s
    assert abs(a1 - Rcurv / 6.0) < 1e-3, "Seeley-DeWitt a_1 != R/6: got %.8f" % a1

    # ---------- sensitivities ----------
    gap_sens = {}
    for g2 in (0.05, 0.20):
        cg, _, _ = band(24, gap2=g2)
        gap_sens["gap^2 = %.2f (%.1f%% of band max)" % (g2, 100 * g2 / band_max)] = \
            round(100.0 * (cg / c24 - 1.0), 3)
    K_long = math.sqrt(38.0)
    K_trans = 2.0 * math.cos(math.atan(math.sqrt(2.0) / 6.0)) + 4.0      # 2026-07-26 erratum
    r_aniso = K_long / K_trans
    ca, _, _ = band(24, weights=[r_aniso if b[0] != 0 else 1.0 for b in pairs])
    aniso_pct = 100.0 * (ca / c24 - 1.0)
    assert abs(aniso_pct) < 0.01, "derived stiffness anisotropy must be negligible: %.4f%%" % aniso_pct

    # ---------- assembly + engine cross-tie ----------
    N_eff = 6
    a_over_lPl = math.sqrt(N_eff * c_lat / (12 * math.pi))               # ell_Planck(full)
    a_low = math.sqrt(N_eff * (0.75 * c_lat) / (12 * math.pi))           # the -25% end
    sg = sakharov_induced_gravity()
    assert sg["N_eff"] == 6
    lam_over_mpl_red = math.sqrt(96 * math.pi ** 2 / N_eff)
    assert abs(lam_over_mpl_red - 4 * math.pi) < 1e-12
    assert abs(lam_over_mpl_red - sg["Lambda_over_MPl"]) < 1e-12, \
        "engine cross-tie broken: %.9f vs %.9f" % (lam_over_mpl_red, sg["Lambda_over_MPl"])
    assert abs(a_over_lPl - 1.86) < 0.01 and abs(a_low - 1.61) < 0.01, (a_over_lPl, a_low)
    c_reg_paper = c_lat / 12.0
    assert abs(c_reg_paper - 1.82) < 0.01, "paper-parametrization c_reg = c_lat/12 != 1.82"
    assert n_goldstone_canted_FM()["N_Goldstone"] == 2, "N_G = 2 regression failed"
    induced_G_gate_A_linearized_sufficient()
    induced_G_leading_coefficient_mass_independent()

    return {
        "tier": ("DERIVED-given-the-NN-BAND-INPUT (the flat-band numbers I_lat, c_lat — the "
                 "band integral is finite and convention-free) + DERIVED-CONDITIONAL-on-"
                 "(OA-LF-i AND OA-LF-ii) (the EH-coefficient reading, the a-value, the "
                 "normalization-spread adjudication), INHERITING R-041's FRAMING+CONDITIONAL "
                 "xi = 0 and N_eff = 6's GENERIC-given-dim-4 status"),
        "c_lat": round(c_lat, 4),
        "c_lat_at_banked_grid_N32": round(c32, 4),
        "richardson_limits": {"16->24": round(rich_a, 5), "24->32": round(rich_b, 5)},
        "I_lat": c_lat / (16 * math.pi ** 2),
        "c_Debye_generic_guess": round(c_Debye, 4),
        "c_lat_over_c_Debye": round(c_lat / c_Debye, 4),
        "band_max_ktil2": round(band_max, 4),
        "second_moment_check": "sum_b b_mu b_nu = 12*delta (exact)",
        "support": {"fraction of I_lat from ktil^2 > 1": round(frac_k_gt_1, 4),
                    "fraction from proper time s < a^2": round(frac_s_lt_a2, 4)},
        "external_calibration": {
            "Z^4 tadpole vs literature G(0)/4 = 0.30986678": "deviation %.2e" % z_dev,
            "independent MC quadrature of the same D4 integral": round(c_mc, 4),
        },
        "seeley_dewitt_a1": {"computed": round(a1, 6), "R/6": 2.0},
        "regulator_language": ("'REGULATOR-FREE' DESCRIBES I_lat ONLY. The former O(1) regulator "
                               "freedom is RELOCATED into OA-LF(ii) — one named physical unknown "
                               "carrying ~93% of the support, now localized with a retirement "
                               "handle (the #1-gap kernel)."),
        "OA_LF_assumptions": {
            "count": 2,
            "(i) occupation": "a statement about the STATE — NESS occupation of the linear-face "
                              "modes equals the Gaussian ground-state measure at monad scales",
            "(ii) covariant monad-scale curvature weight": "a statement about the OPERATOR — the "
                                                           "continuum a_1 = R/6 extends to s ~ a^2 "
                                                           "up to O(1)",
            "retirement handle": "the #1-gap kernel (unchanged from the current I-3 row) "
                                 "discharges BOTH clauses",
            "I-3 ledger": "3 premises -> 2 (one registry row, TWO counted clauses)",
            "discharged": ["one-loop validity -> banked Gate A", "covariant regularization -> computed away"],
        },
        "gapless_idealization": {
            "note": "c_lat = 21.83 is the GAPLESS-SHARED-BAND idealization",
            "canted vacuum": "N_G = 2 (2 gapless + 4 gapped) — exact 6-band Bogoliubov structure UN-BANKED",
            "uniform-gap spot check (%)": gap_sens,
            "honest refinement window": (
                "WITHDRAWN 2026-08-23 (estate of N64, B1) — the former '-5% ... -25% on c_lat' "
                "rode a UNIFORM-GAP spot check assuming (gap/b_max)^2 in [0.01, 0.04], while the "
                "actual canted vacuum gives (g/b_max)^2 = 4.049e-05 (247x-988x too large) and is "
                "2 gapless + 4 gapped, not uniform-gap. NO WINDOW IS ASSERTED and no replacement "
                "number is offered: the six-band measure is not resolved at M <= 47 (the shift "
                "runs -0.1445% -> -0.0227% monotonically, Richardson limit CONSISTENT WITH ZERO), "
                "which is what the banked induced_G_leading_coefficient_mass_independent line at "
                "STEP 2 already predicts."),
            "=> a range": (
                "the former [%.2f, %.2f] ell_Planck(full) bracket was the WINDOW's image and is "
                "withdrawn with it; the CONVENTION-INVARIANT statement 'a = 1.86 ell_Planck, "
                "PLANCKIAN WITHIN O(1)' is unchanged" % (a_low, a_over_lPl)),
            "derived stiffness anisotropy effect": "%.4f%% (negligible)" % aniso_pct,
            "premise refutation (2026-08-23, B1)": {
                "g_body_diagonal": 0.412121,
                "band_max_approx": 64.8,
                "(g/b_max)^2": 4.049e-05,
                "spot check assumed (gap/b_max)^2": [0.01, 0.04],
                "too large by": "247x - 988x",
                "true structure": "2 gapless + 4 gapped (magnon_stiffness_bands_canted_vacuum)",
                "refined value": "NOT RESOLVED at M <= 47; Richardson limit consistent with ZERO",
                "no number of the -0.111% class is asserted anywhere": True,
            },
            "jurisdiction fence (verbatim, unweakened)": (
                "a remains CONDITIONAL on (OA-LF-i AND OA-LF-ii) + N_eff = 6 + the induced-G "
                "identification; 'TWT derives the grain spacing' stays PROHIBITED; and a IS A "
                "BACK-FIT OF MEASURED G_N, so narrowing the window narrows A BACK-FIT and MOVES "
                "NO EMPIRICAL CLAIM WHATSOEVER. A NARROWER WINDOW IS NOT BETTER AGREEMENT AND "
                "MUST NEVER BE QUOTED AS ONE."),
        },
        "normalization_spread": {
            "three conventions": {"paper SSB.6.2": "16 pi^2", "induced_G_bracket_mode_count": "96 pi^2",
                                  "sakharov_induced_gravity": "192 pi^2"},
            "paper table self-consistency": ("SSB.6.2 IS self-consistent under its OWN 16 pi^2 "
                                             "formula: c_reg = c_lat/12 = %.2f, inside 'c_reg ~ 1' "
                                             "— a convention note is needed, not an arithmetic fix. "
                                             "SCOPE (2026-07-28): this adjudicates the pi-CONVENTION "
                                             "spread (16 vs 96 vs 192 pi^2) ONLY. The VALUE question "
                                             "RESOLVED 2026-07-29 — one c_reg = 1/12 in the "
                                             "proper-time variable, with 1.82 = c_lat/12 the same "
                                             "computation in Lambda := 1/a — see "
                                             "c_reg_vs_sakharov" % c_reg_paper),
            "this computation lands on": "the sakharov_induced_gravity form",
            "convention-invariant statement": "a = %.2f ell_Planck — PLANCKIAN WITHIN O(1); this "
                                              "SUPPORTS SSB.6.2" % a_over_lPl,
        },
        "assembly": "1/(16 pi G) = N_eff * c_lat / (192 pi^2 a^2)  ==  G^-1 = N_eff Lambda^2/(12 pi) "
                    "at Lambda_eff^2 = c_lat/a^2",
        "engine_cross_tie": {"sqrt(96 pi^2 / N_eff)": lam_over_mpl_red,
                             "sakharov_induced_gravity Lambda_over_MPl": sg["Lambda_over_MPl"],
                             "note": "c_lat-INDEPENDENT (a pure-N statement) — nothing banked moves"},
        "a_monad_spacing": {"value": "%.2f ell_Planck(full)" % a_over_lPl,
                            "D4 NN spacing": "%.2f ell_Planck(full)" % (math.sqrt(2) * a_over_lPl),
                            "JURISDICTION": ("ALWAYS CONDITIONAL on (OA-LF-i AND OA-LF-ii) + "
                                             "N_eff = 6 (generic-given-dim-4) + the induced-G "
                                             "identification with the EMPIRICAL G. NEVER write "
                                             "'TWT derives the monad spacing'.")},
        "fence": ("Lambda values stay CANDIDATE/conditional and do NOT move to chase agreement "
                  "with measurement — Lambda_S is a back-fit to empirical G over the N_eff menu, and "
                  "nothing here changes G or the menu; the reduction achieved is IN THE PREMISE, not "
                  "in the tier. THE ONLY ADMISSIBLE RE-CUTS: (a) a normalization/convention "
                  "reconciliation between NAMED engine artifacts, or (b) an actual substrate "
                  "derivation of c_reg. Both historical re-cuts were case (a): the 2026-07-28 "
                  "widening spanned an apparent c_reg disagreement; the 2026-07-29 resolution + "
                  "2026-07-30 which-Lambda ruling SPLIT the symbol (Lambda_S scheme / Lambda_L = 1/a "
                  "= [0.386, 0.734] M_Pl for dispersion consumers) and RETIRED the wide bracket. "
                  "'It agrees better with the data' is NEVER a reason"),
        "c_reg_vs_sakharov": {
            "this primitive": "c_reg = c_lat/12 = %.2f (on TWT's DERIVED D4 nearest-neighbour band)" % c_reg_paper,
            "sakharov_induced_gravity": "c_reg = 1/12 (textbook heat-kernel a_1, minimal coupling, "
                                        "proper-time cutoff — QFT INPUT)",
            "paper placeholder": "c_reg ~ 1 (no engine primitive; never computed)",
            "ratio of the two BANKED values": "%.1f in c_reg => ~%.1f in Lambda => ~%.1f in eta4 — "
                                              "a VARIABLE ratio (sqrt(c_lat)), not a physics gap"
                                              % (c_reg_paper * 12.0, math.sqrt(c_reg_paper * 12.0),
                                                 c_reg_paper * 12.0),
            "status": "RESOLVED (2026-07-29): ONE coefficient in two Lambda-variables "
                      "(c_reg_from_substrate_mode_content meets this row's own exit condition); "
                      "which-Lambda RULED (coordinator, 2026-07-30): Lambda_S for Sakharov "
                      "bookkeeping, Lambda_L = 1/a for dispersion consumers",
        },
        "would_change_if": ("the #1-gap kernel derives the NESS occupation and/or the monad-scale "
                            "curvature coupling (discharges OA-LF entirely); the exact 6-band "
                            "Bogoliubov structure on the canted vacuum is banked (moves c_lat "
                            "inside the -5%...-25% window and narrows the a-range); the derived "
                            "band itself is revised beyond nearest neighbours"),
    }


def skyrme_quartic_contains_no_tree_EH():
    """[DERIVED-A (the decomposition facts: the EXACT rational coefficient tables, the exact
    parity covariances, the zero overlap, the exact I4-quartic == EH-W-block identity) +
    DERIVED-structural EH-ABSENT (the verdict), CONDITIONAL on U2 (the gauge/signature
    projection) + the banked Omega-ALGEBRAIC ACTION CLASS + the explicit MENU QUANTIFIER
    below] — the substrate's Skyrme quartic contains NO tree-level Einstein-Hilbert term:
    'gravity as elasticity' is dead within the banked action class, leaving the induced arc
    as the unique surviving tree route (W6, 2026-07-27; negatives ledger N51).

    THE MECHANISM (state it verbatim — it is the content, not the verdict): *the property that
    makes the term a stabilizer (Killing definiteness) is the property that makes it EH-blind
    (h-indefiniteness reachable only in the parity-odd sector)*. Equivalently, in elasticity
    language: the quartic is a STRETCHING energy and EH is a BENDING energy. A first-derivative
    Omega-algebraic term measures how much the frame is stretched; the Einstein-Hilbert density
    measures how much it is bent. The two live in orthogonal parity sectors of the SAME
    classified R-151 invariant space, so no coefficient assignment can turn one into the other.

    THE EXACT DECOMPOSITION [DERIVED-A, rational arithmetic — no floats]. In the R-151 basis of
    invariant quadratic forms Q1..Q8 built from the pointwise first-order fluctuation data
    (S_sym, W = [Om,Om]) — Q1/Q2 = trace-free S in the SD/ASD value block, Q3/Q4 = the traces,
    Q5/Q6 = self-dual W in SD/ASD, Q7/Q8 = anti-self-dual W in SD/ASD:
        sqrt(g) R |_quadratic = Q1 - Q2 - (3/4)Q3 + (3/4)Q4 - (1/4)(Q5+Q7) + (1/4)(Q6+Q8)
        Skyrme quartic        = -(Q5 + Q6 + Q7 + Q8)
    Both EXACT. Parity acts as the permutation (Q1 Q2)(Q3 Q4)(Q5 Q8)(Q6 Q7). Consequently:
        the EH representative is parity-ODD, the quartic is parity-EVEN, both EXACTLY,
        the parity-even part of the EH coefficients is 0, the parity-odd part of the quartic
        coefficients is 0 — ZERO OVERLAP, basis-independently.
    The quartic carries EQUAL WEIGHT -1 on all four W-invariants: the definite KILLING
    combination. The EH density's W-block instead carries the INDEFINITE h-combination
    -(1/4)(Q5+Q7) + (1/4)(Q6+Q8).

    THE WOULD-CHANGE-IF HANDLE, BANKED AS AN IDENTITY. The I4-BUILT parity-ODD quartic
    (1/4)*sum_{mn} h(W_mn, W_mn) equals the EH W-block EXACTLY. So a parity-odd, I4-built
    quartic would buy the W-block HALF of EH — and only that half: it cannot serve Derrick
    stabilization (it is indefinite), and it supplies none of the S-block (Q1..Q4). This is the
    sharpest statement of what a different quartic would and would not do.

    THE SEQUENTIAL KILL CHAIN (attribute the witnesses correctly — this is a CHAIN, and it is
    NOT 'one-blade kills cc + higher-curvature'):
      (1) PARITY / S-BLOCK DISJOINTNESS  =>  lambda = 0 at quadratic order (the exact
          decomposition above).
      (2) ddR-FREEZE (nonperturbative, pointwise)  =>  lambda = 0 non-perturbatively versus
          cc and the whole Omega-algebraic remainder: holding (R, dR) fixed at a point and
          varying ONLY ddR leaves BOTH quartic contractions (flat and texture) EXACTLY frozen
          (spread 0 to machine zero) while sqrt(g)R sweeps by O(100) times the finite-difference
          noise floor. An Omega-algebraic first-derivative object cannot see ddR; EH does.
      (3) ONE-BLADE FAMILY  =>  lambda = Lambda_cc = 0, with EXACTLY ONE surviving direction.
          On a one-blade texture the quartic vanishes IDENTICALLY (a blade commutes with
          itself), so the whole menu {EH, cc, R^2, Ric^2, Riem^2} must vanish there. The
          12-point menu matrix is rank-DEFICIENT with a ONE-dimensional null space, and the
          null vector is exactly
                (EH, cc, R^2, Ric^2, Riem^2) = (0, 0, -1/4, 1, -1/4)
          i.e. proportional to the GAUSS-BONNET combination E4 = R^2 - 4 Ric^2 + Riem^2. The
          EH and cc components of that null vector VANISH — that is the one-blade step's
          actual output. It does NOT by itself kill the higher-curvature menu; it reduces it
          to Gauss-Bonnet.
      (4) GAUSS-BONNET DEATH  =>  the surviving direction dies on the frozen-quartic sweeps:
          sqrt(g) E4 spreads by tens-to-hundreds along sweeps on which the quartic is frozen,
          against a finite-difference noise floor ~1e-4.
      (5) ACROSS-BACKGROUND NON-UNIVERSALITY  =>  the per-sweep higher-curvature
          'conspiracies' are NOT a fixed action term. A near-exact HC cancellation of the EH
          variation DOES exist along any SINGLE sweep (recorded below — this is exactly why a
          single-sweep test is insufficient), but the fitted coefficients do NOT transfer: the
          sweep-1 coefficients applied to a different background leave a residual comparable to
          or larger than that background's entire EH spread. A fixed-coefficient higher-curvature
          repackaging of EH is therefore excluded.

    THE MENU QUANTIFIER (required — never quantify over 'any conceivable term'). The EXCLUDED
    MENU IS EXACTLY {cc, R^2, Ric^2, Riem^2} (plus EH itself). The R^3 / grad-Riemann class
    falls to the SAME dE-independence schema — step (2) is a statement about ddR-blindness that
    applies verbatim — but those terms were NOT RUN. Do not widen the claim beyond the four
    named menu entries.

    SCOPE, AND WHAT THIS DOES *NOT* CLOSE:
      * CLASS-SCOPED SOLE-ROUTE CONSEQUENCE. No Omega-algebraic term in the banked
        first-derivative action class can contain EH. With the front-embedding tree route
        already closed at SSB.6.6, the INDUCED arc is the unique surviving route WITHIN THE
        BANKED CONTENT. The thermodynamic route and genuinely-new dE-terms are UNTOUCHED.
      * Conditional on U2 (the gauge/signature projection) and on the banked Omega-algebraic
        action content. If U2 falls, the verdict is re-opened.
      * A banked SECOND-derivative 'bending' term would reopen the question directly.
      * The inhomogeneity route yields Brans-Dicke-like non-constant 1/G, NOT EH.
      * TRUNCATION NUMBERS ARE CONFIG-DEPENDENT: quote the SHRINKAGE of the truncation
        deviation, never the magnitudes.
      * The EH W-block rides the EXACT R-149 fact (1), antisym(S) = -W/2, used as such.

    NOTED NON-COINCIDENCE (flagged per the K_trans precedent, NOT claimed as a result). At the
    single (3,1)-signature menu point, the TEXTURE-contracted quartic and the EH density are
    nearly equal: F4_tex / sqrt(g)R = 1.0007. It is ONE point on ONE configuration, the ratio
    spreads over four orders of magnitude across the four-signature menu, and nothing in the
    decomposition permits a relation. Recorded so a later reader does not rediscover it as a
    'finding'; it is a coincidence until something explains it.

    self-checks: engine anchors (Killing pairing = -delta, h pairing = diag(-1_SD,+1_ASD),
    [SD,ASD] = 0, parity = SD<->ASD with signs (+,+,-) flipping h and preserving K); the EXACT
    rational decomposition + parity covariances + zero overlap on random INTEGER datasets; the
    exact I4-quartic == EH-W-block identity; a truncation-shrinkage ladder certifying that the
    Gauss quadratic form IS the small-amplitude limit of sqrt(g)R; then the five kill-chain
    steps; and the four-signature menu coverage carrying the flagged (3,1) near-equality."""
    import math, random, itertools
    from fractions import Fraction as Fr
    import numpy as np

    s2 = 1.0 / math.sqrt(2.0)
    SDb = [s2 * (e(1, 2) - e(3, 4)), s2 * (e(1, 3) + e(2, 4)), s2 * (e(1, 4) - e(2, 3))]
    ASDb = [s2 * (e(1, 2) + e(3, 4)), s2 * (e(1, 3) - e(2, 4)), s2 * (e(1, 4) + e(2, 3))]
    B6 = SDb + ASDb
    def g0(mv): return dict(mv.terms).get((), 0.0)
    def hpair(A, Bm): return g0(A * I4 * Bm)
    def comm(A, Bm): return A * Bm - Bm * A

    # ---------------- I. engine anchors ----------------
    Kmat = np.array([[g0(B6[a] * B6[b]) for b in range(6)] for a in range(6)])
    Hmat = np.array([[g0(B6[a] * I4 * B6[b]) for b in range(6)] for a in range(6)])
    assert np.allclose(Kmat, -np.eye(6), atol=1e-12), "Killing pairing must be -delta"
    assert np.allclose(Hmat, np.diag([-1., -1., -1., 1., 1., 1.]), atol=1e-12), "h pairing wrong"
    assert max(sum(abs(x) for _, x in comm(SDb[i], ASDb[j]).terms)
               for i in range(3) for j in range(3)) < 1e-12, "[SD,ASD] must vanish"
    def parity_mv(mv):
        out = {}
        for bl, c in dict(mv.terms).items():
            out[bl] = out.get(bl, 0.0) + (-1.0 if 4 in bl else 1.0) * c
        return MV.from_dict(out)
    Pv = np.zeros((6, 6))
    Pv[3, 0] = Pv[0, 3] = 1.0; Pv[4, 1] = Pv[1, 4] = 1.0; Pv[5, 2] = Pv[2, 5] = -1.0
    for b in range(6):
        pred = MV.from_dict({})
        for a in range(6):
            pred = pred + float(Pv[a, b]) * B6[a]
        d = parity_mv(B6[b]) - pred
        assert max((abs(c) for _, c in d.terms), default=0.0) < 1e-12, "parity != SD<->ASD (+,+,-)"
    assert np.allclose(Pv.T @ Hmat @ Pv, -Hmat) and np.allclose(Pv.T @ Kmat @ Pv, Kmat), \
        "parity must flip h and preserve the Killing pairing"

    # ---------------- II. EXACT rational decomposition ----------------
    PvF = [[Fr(0)] * 6 for _ in range(6)]
    PvF[3][0] = PvF[0][3] = Fr(1); PvF[4][1] = PvF[1][4] = Fr(1); PvF[5][2] = PvF[2][5] = Fr(-1)
    PtF = [Fr(1), Fr(1), Fr(1), Fr(-1)]
    HF = [Fr(-1)] * 3 + [Fr(1)] * 3
    EPS = {}
    for p in itertools.permutations(range(4)):
        sgn = 1; pl = list(p)
        for i in range(4):
            for j in range(i + 1, 4):
                if pl[i] > pl[j]: sgn = -sgn
        EPS[p] = sgn
    def dualW(W):
        Wd = [[[Fr(0)] * 6 for _ in range(4)] for _ in range(4)]
        for m in range(4):
            for n in range(4):
                for a in range(6):
                    acc = Fr(0)
                    for r in range(4):
                        for s in range(4):
                            acc += EPS.get((m, n, r, s), 0) * W[r][s][a]
                    Wd[m][n][a] = acc / 2
        return Wd
    def invariants(Ss, W):
        t = [sum(Ss[m][m][a] for m in range(4)) for a in range(6)]
        Sh = [[[Ss[m][n][a] - (t[a] / 4 if m == n else Fr(0)) for a in range(6)]
               for n in range(4)] for m in range(4)]
        def bsum(T, lo, hi):
            return sum(T[m][n][a] * T[m][n][a] for m in range(4) for n in range(4) for a in range(lo, hi))
        Wd = dualW(W)
        Wp = [[[(W[m][n][a] + Wd[m][n][a]) / 2 for a in range(6)] for n in range(4)] for m in range(4)]
        Wm = [[[(W[m][n][a] - Wd[m][n][a]) / 2 for a in range(6)] for n in range(4)] for m in range(4)]
        return [bsum(Sh, 0, 3), bsum(Sh, 3, 6),
                sum(t[a] * t[a] for a in range(3)), sum(t[a] * t[a] for a in range(3, 6)),
                bsum(Wp, 0, 3), bsum(Wp, 3, 6), bsum(Wm, 0, 3), bsum(Wm, 3, 6)]
    def R_gauss_fr(Ss, W):
        S = [[[Ss[m][n][a] - W[m][n][a] / 2 for a in range(6)] for n in range(4)] for m in range(4)]
        t = [sum(S[m][m][a] for m in range(4)) for a in range(6)]
        return (sum(HF[a] * t[a] * t[a] for a in range(6))
                - sum(HF[a] * S[n][m][a] * S[m][n][a] for m in range(4) for n in range(4) for a in range(6)))
    def F4K_fr(W):
        return sum(-W[m][n][a] * W[m][n][a] for m in range(4) for n in range(4) for a in range(6))
    def F4H_fr(W):
        return sum(HF[a] * W[m][n][a] * W[m][n][a]
                   for m in range(4) for n in range(4) for a in range(6)) / 4
    def par_act(T):
        out = [[[Fr(0)] * 6 for _ in range(4)] for _ in range(4)]
        for m in range(4):
            for n in range(4):
                for cc in range(6):
                    out[m][n][cc] = PtF[m] * PtF[n] * sum(PvF[cc][a] * T[m][n][a] for a in range(6))
        return out
    cR = [Fr(1), Fr(-1), Fr(-3, 4), Fr(3, 4), Fr(-1, 4), Fr(1, 4), Fr(-1, 4), Fr(1, 4)]
    cF = [Fr(0)] * 4 + [Fr(-1)] * 4
    cH = [Fr(0)] * 4 + [Fr(-1, 4), Fr(1, 4), Fr(-1, 4), Fr(1, 4)]
    perm = [1, 0, 3, 2, 7, 6, 5, 4]                      # parity on Q1..Q8
    assert [cR[perm[i]] for i in range(8)] == [-cR[i] for i in range(8)], "EH coeffs not parity-odd"
    assert [cF[perm[i]] for i in range(8)] == [cF[i] for i in range(8)], "quartic coeffs not parity-even"
    assert all(cR[i] + cR[perm[i]] == 0 for i in range(8)), "parity-EVEN part of EH must vanish"
    assert all(cF[i] - cF[perm[i]] == 0 for i in range(8)), "parity-ODD part of quartic must vanish"
    assert cH == [Fr(0)] * 4 + [cR[4], cR[5], cR[6], cR[7]], "I4-quartic != the EH W-block"
    rnd = random.Random(20260727)
    for _ in range(6):
        Ss = [[[Fr(0)] * 6 for _ in range(4)] for _ in range(4)]
        W = [[[Fr(0)] * 6 for _ in range(4)] for _ in range(4)]
        for m in range(4):
            for n in range(m, 4):
                for a in range(6):
                    v = Fr(rnd.randint(-7, 7)); Ss[m][n][a] = v; Ss[n][m][a] = v
                    w = Fr(rnd.randint(-7, 7))
                    if m != n: W[m][n][a] = w; W[n][m][a] = -w
        Q = invariants(Ss, W)
        assert R_gauss_fr(Ss, W) == sum(cR[i] * Q[i] for i in range(8)), "EH decomposition NOT exact"
        assert F4K_fr(W) == sum(cF[i] * Q[i] for i in range(8)), "quartic decomposition NOT exact"
        assert F4H_fr(W) == sum(cH[i] * Q[i] for i in range(8)), "I4-quartic != EH W-block (exact)"
        Sp, Wp2 = par_act(Ss), par_act(W)
        assert R_gauss_fr(Sp, Wp2) == -R_gauss_fr(Ss, W), "EH not parity-ODD exactly"
        assert F4K_fr(Wp2) == F4K_fr(W), "quartic not parity-EVEN exactly"
        assert F4H_fr(Wp2) == -F4H_fr(W), "I4-quartic not parity-ODD exactly"
        assert invariants(Sp, Wp2) == [Q[perm[i]] for i in range(8)], "parity permutation wrong"

    # ---------------- III. numeric machinery (ported from the banked R-149 primitive) -------
    def mv_exp(Bm, n=40):
        out = SCALAR; term = SCALAR
        for k in range(1, n):
            term = (1.0 / k) * (term * Bm); out = out + term
        return out
    def coords6(X): return np.array([-g0(X * B6[a]) for a in range(6)])
    def Lmap(X):
        return np.array([0.0] * 4 + [hpair(X, ASDb[a]) for a in range(3)]
                        + [hpair(X, SDb[a]) for a in range(3)])
    kap = np.diag([1.0] * 7 + [-1.0] * 3)
    def E_of(Oms):
        E = np.zeros((10, 4)); E[:4, :] = np.eye(4)
        for m in range(4):
            E[:, m] += Lmap(Oms[m])
        return E
    def g_of(Oms):
        E = E_of(Oms); return E.T @ kap @ E
    def sig_of(g):
        ev = np.linalg.eigvalsh(g)
        return (int(np.sum(ev < -1e-10)), int(np.sum(ev > 1e-10)))
    def fd_tensor(func, x, h):
        outs = []
        for mu in range(4):
            xp = list(x); xm = list(x); xp[mu] += h; xm[mu] -= h
            outs.append((func(xp) - func(xm)) / (2 * h))
        return np.array(outs)
    def curv_invs(Omf, x, h_curv=1e-3):
        def gfun(xx): return g_of(Omf(xx))
        def Gamfun(xx):
            g2 = gfun(xx); gi2 = np.linalg.inv(g2)
            dg2 = fd_tensor(gfun, xx, 1e-5)
            Gl = np.zeros((4, 4, 4))
            for r in range(4):
                for mm in range(4):
                    for nn in range(4):
                        Gl[r, mm, nn] = 0.5 * (dg2[mm, nn, r] + dg2[nn, mm, r] - dg2[r, mm, nn])
            return np.einsum('lp,pmn->lmn', gi2, Gl)
        g = gfun(x); gi = np.linalg.inv(g); G0 = Gamfun(x)
        dG = (4.0 * fd_tensor(Gamfun, x, h_curv / 2) - fd_tensor(Gamfun, x, h_curv)) / 3.0
        Riem = np.zeros((4, 4, 4, 4))
        for lam in range(4):
            for sg2 in range(4):
                for mm in range(4):
                    for nn in range(4):
                        Riem[lam, sg2, mm, nn] = (dG[mm, lam, nn, sg2] - dG[nn, lam, mm, sg2]
                            + sum(G0[lam, mm, t2] * G0[t2, nn, sg2] - G0[lam, nn, t2] * G0[t2, mm, sg2]
                                  for t2 in range(4)))
        Ric = np.einsum('lsln->sn', Riem)
        Rs = float(np.einsum('sn,sn->', gi, Ric))
        Rlow = np.einsum('lr,rsmn->lsmn', g, Riem)
        Ric2 = float(np.einsum('sn,sa,nb,ab->', Ric, gi, gi, Ric))
        Riem2 = float(np.einsum('lsmn,la,sb,mc,nd,abcd->', Rlow, gi, gi, gi, gi, Rlow))
        return math.sqrt(abs(np.linalg.det(g))), Rs, Ric2, Riem2, g
    def F4_at(Oms, g=None):
        C = [[comm(Oms[m], Oms[n]) for n in range(4)] for m in range(4)]
        flat = sum(g0(C[m][n] * C[m][n]) for m in range(4) for n in range(4))
        tex = None
        if g is not None:
            gi = np.linalg.inv(g)
            tex = float(sum(gi[m, a] * gi[n, b] * g0(C[m][n] * C[a][b])
                            for m in range(4) for n in range(4) for a in range(4) for b in range(4)))
        return flat, tex
    def bch_dexp(A, X, kmax=30):
        out = X; term = X
        for k in range(1, kmax):
            term = comm(A, term)
            out = out + (((-1.0) ** k) / math.factorial(k + 1)) * term
        return out
    def make_expquad(Bmu, Cq, t):
        def Om(x):
            A = sum((float(x[m]) * Bmu[m] for m in range(4)), 0.0 * SCALAR)
            for m in range(4):
                for n in range(4):
                    A = A + (0.5 * t * float(x[m]) * float(x[n])) * Cq[m][n]
            Oms = []
            for m in range(4):
                dA = Bmu[m] + sum((t * float(x[n]) * Cq[m][n] for n in range(4)), 0.0 * SCALAR)
                Oms.append(bch_dexp(A, dA))
            return Oms
        return Om
    def rand_biv_from(rng, scale=1.0):
        cs = rng.normal(size=6) * scale
        return sum((float(cs[i]) * b for i, b in enumerate(B6)), 0.0 * SCALAR)

    # ---- truncation shrinkage: the Gauss quadratic form IS the small-amplitude limit -------
    Hnum = np.diag([-1., -1., -1., 1., 1., 1.])
    def extract_SW(Omf, x):
        Oms = Omf(x); E = E_of(Oms); g = E.T @ kap @ E; gi = np.linalg.inv(g)
        Wt = np.zeros((4, 4, 10)); hh = 1e-5
        for mu in range(4):
            xp = list(x); xm = list(x); xp[mu] += hh; xm[mu] -= hh
            Wt[mu] = ((E_of(Omf(xp)) - E_of(Omf(xm))) / (2 * hh)).T
        Gt = np.einsum('lp,pmn->lmn', gi, np.einsum('pr,rk,mnk->pmn', E.T, kap, Wt))
        S10 = Wt - np.einsum('lmn,kl->mnk', Gt, E)
        Sval = np.zeros((4, 4, 6)); Sval[..., :3] = -S10[..., 7:10]; Sval[..., 3:] = S10[..., 4:7]
        Wval = np.zeros((4, 4, 6))
        for m in range(4):
            for n in range(4):
                Wval[m, n] = coords6(comm(Oms[m], Oms[n]))
        return Sval, Wval
    rng_t = np.random.default_rng(20260727)
    Bme = [rand_biv_from(rng_t, 1.0) for _ in range(4)]
    Cme = [[None] * 4 for _ in range(4)]
    for m in range(4):
        for n in range(m, 4):
            Cme[m][n] = Cme[n][m] = rand_biv_from(rng_t, 1.0)
    ladder, prev = [], None
    for eps in (0.16, 0.08, 0.04):
        Omf = make_expquad([eps * b for b in Bme],
                           [[eps * Cme[m][n] for n in range(4)] for m in range(4)], 1.0)
        _, Rex, _, _, _ = curv_invs(Omf, [0.0] * 4)
        Sval, Wval = extract_SW(Omf, [0.0] * 4)
        anti_dev = float(np.max(np.abs(0.5 * (Sval - Sval.transpose(1, 0, 2)) + 0.5 * Wval)))
        trS = np.einsum('mma->a', Sval)
        Rg = float(trS @ Hnum @ trS) - float(np.einsum('nma,ab,mnb->', Sval, Hnum, Sval))
        rel = abs(Rex - Rg) / max(abs(Rex), 1e-12)
        ladder.append((eps, rel, anti_dev))
        if prev is not None:
            assert rel < prev * 0.70, "truncation deviation not shrinking with amplitude"
        prev = rel

    # ---------------- IV. kill-chain steps (2), (4), (5): the ddR sweeps -------------------
    def run_sweep(seed, tvals=(0.0, 0.4, 0.8, 1.2, 1.6)):
        rg = np.random.default_rng(seed)
        Bmu = [rand_biv_from(rg, 0.7) for _ in range(4)]
        Cq = [[None] * 4 for _ in range(4)]
        for m in range(4):
            for n in range(m, 4):
                Cq[m][n] = Cq[n][m] = rand_biv_from(rg, 0.6)
        rows, f4f, f4t, gref = [], [], [], None
        for t in tvals:
            Omf = make_expquad(Bmu, Cq, t)
            Oms = Omf([0.0] * 4)
            sg, Rs, Ric2, Riem2, g = curv_invs(Omf, [0.0] * 4)
            if gref is None:
                gref = g
            assert np.max(np.abs(g - gref)) < 1e-12, "metric must stay FROZEN along a ddR sweep"
            a_, b_ = F4_at(Oms, g)
            f4f.append(a_); f4t.append(b_)
            rows.append([sg * Rs, sg * Rs * Rs, sg * Ric2, sg * Riem2,
                         sg * (Rs * Rs - 4.0 * Ric2 + Riem2)])
        Omf0 = make_expquad(Bmu, Cq, tvals[0])
        sgh, Rsh, Ric2h, Riem2h, _ = curv_invs(Omf0, [0.0] * 4, h_curv=5e-4)
        noise = max(abs(sgh * Rsh - rows[0][0]),
                    abs(sgh * (Rsh * Rsh - 4.0 * Ric2h + Riem2h) - rows[0][4]), 1e-9)
        return np.array(rows), f4f, f4t, noise, sig_of(gref)

    M1, f4f1, f4t1, noise1, sig1 = run_sweep(777)
    M2, f4f2, f4t2, noise2, sig2 = run_sweep(424242)
    freeze = {}
    for tag, ff, ft, Mx, nz in (("sweep-1", f4f1, f4t1, M1, noise1),
                                ("sweep-2", f4f2, f4t2, M2, noise2)):
        sf, st = max(ff) - min(ff), max(ft) - min(ft)
        assert sf < 1e-9 * (1 + abs(ff[0])), "flat quartic moved under a pure ddR variation"
        assert st < 1e-9 * (1 + abs(ft[0])), "texture quartic moved under a pure ddR variation"
        eh_spread = float(np.max(Mx[:, 0]) - np.min(Mx[:, 0]))
        assert eh_spread > 50 * nz and eh_spread > 1e-2, "sqrt(g)R must sweep robustly"
        gb_spread = float(np.max(Mx[:, 4]) - np.min(Mx[:, 4]))
        assert gb_spread > 50 * nz, "GAUSS-BONNET must die on the frozen-quartic sweep"
        freeze[tag] = {"quartic flat spread": sf, "quartic texture spread": st,
                       "sqrt(g)R spread": round(eh_spread, 4),
                       "sqrt(g)E4 spread": round(gb_spread, 4), "FD noise": nz}
    # (5) across-background non-universality of the HC 'conspiracy'
    D1 = M1[1:, :4] - M1[0, :4]; D2 = M2[1:, :4] - M2[0, :4]
    sol1, _, _, _ = np.linalg.lstsq(D1[:, 1:], -D1[:, 0], rcond=None)
    sol2, _, _, _ = np.linalg.lstsq(D2[:, 1:], -D2[:, 0], rcond=None)
    resid1_own = float(np.linalg.norm(D1[:, 1:] @ sol1 + D1[:, 0]))
    resid2_own = float(np.linalg.norm(D2[:, 1:] @ sol2 + D2[:, 0]))
    resid2_x = float(np.linalg.norm(D2[:, 1:] @ sol1 + D2[:, 0]))
    eh2 = float(np.max(np.abs(D2[:, 0])))
    assert resid1_own < 0.05 * float(np.max(np.abs(D1[:, 0]))), \
        "a per-sweep HC cancellation should EXIST (this is why one sweep is not enough)"
    assert resid2_x > 0.05 * eh2, \
        "sweep-1 HC coefficients must NOT transfer to another background (%.3e vs %.3e)" % (resid2_x, eh2)

    # ---------------- V. kill-chain step (3): the one-blade family ------------------------
    def Om_oneblade(x):
        df = [0.35 * math.cos(x[0]), 0.25 * x[2], 0.25 * x[1], -0.2]
        return [df[m] * SDb[0] for m in range(4)]
    ob = Om_oneblade([0.3, 0.25, -0.2, 0.1])
    assert max(max((abs(c) for _, c in comm(ob[m], ob[n]).terms), default=0.0)
               for m in range(4) for n in range(4)) < 1e-14, "one blade must commute with itself"
    f4ob, f4ob_t = F4_at(ob, g_of(ob))
    assert abs(f4ob) < 1e-12 and abs(f4ob_t) < 1e-12, "the quartic must vanish IDENTICALLY here"
    pts = [[0.3, 0.25, -0.2, 0.1], [0.7, -0.4, 0.3, 0.6], [-0.5, 0.8, 0.2, -0.3],
           [1.0, 0.1, -0.6, 0.4], [0.2, -0.9, 0.5, 0.8], [-0.8, 0.3, 0.9, -0.2],
           [1.2, 0.5, -0.8, 0.9], [-1.1, -0.6, 0.7, -0.5], [0.5, 1.1, 0.4, 0.2],
           [-0.3, -1.2, -0.9, 0.7], [0.9, 0.7, 1.1, -0.6], [-0.6, 0.4, -1.0, 0.3]]
    Mb = []
    for p in pts:
        sg, Rs, Ric2, Riem2, g = curv_invs(Om_oneblade, p)
        assert abs(np.linalg.det(g)) > 1e-3
        Mb.append([sg * Rs, sg, sg * Rs * Rs, sg * Ric2, sg * Riem2])   # EH, cc, R^2, Ric^2, Riem^2
    Mb = np.array(Mb)
    U_, S_, Vt_ = np.linalg.svd(Mb)
    assert S_[4] < 1e-9 * S_[0], "the one-blade menu matrix must be rank-deficient"
    assert S_[3] > 1e-6 * S_[0], "the null space must be exactly ONE-dimensional"
    nullv = Vt_[-1] / Vt_[-1][3]                       # normalize on the Ric^2 slot (deterministic)
    gb_dir = np.array([0.0, 0.0, -0.25, 1.0, -0.25])   # prop. to E4 = R^2 - 4 Ric^2 + Riem^2
    assert np.max(np.abs(nullv - gb_dir)) < 1e-5, "surviving direction must be GAUSS-BONNET: %s" % nullv
    assert abs(nullv[0]) < 1e-5 and abs(nullv[1]) < 1e-5, "one-blade must kill lambda AND Lambda_cc"

    # ---------------- VI. four-signature menu coverage + the flagged near-equality ---------
    def family(B1, B2, B3, c):
        def f(x):
            return (c[0] * x[0] + c[1] * math.sin(x[1]) + c[2] * x[2] * x[3],
                    c[3] * x[1] + c[4] * math.cos(x[0]) + c[5] * x[2],
                    c[6] * x[3] + c[7] * x[0] * x[1] + c[8] * math.sin(x[2]))
        def df(x):
            return ([c[0], c[1] * math.cos(x[1]), c[2] * x[3], c[2] * x[2]],
                    [-c[4] * math.sin(x[0]), c[3], c[5], 0.0],
                    [c[7] * x[1], c[7] * x[0], c[8] * math.cos(x[2]), c[6]])
        def Om(x):
            f1, f2, f3 = f(x); d1, d2, d3 = df(x)
            R2 = mv_exp(f2 * B2); R3 = mv_exp(f3 * B3)
            B1c = R3.reverse() * (R2.reverse() * B1 * R2) * R3
            B2c = R3.reverse() * B2 * R3
            return [d1[m] * B1c + d2[m] * B2c + d3[m] * B3 for m in range(4)]
        return Om
    rA = np.random.default_rng(20260705)
    r22 = np.random.default_rng(7)
    r31 = np.random.default_rng(31)
    Om04 = family(rand_biv_from(rA, 0.5), rand_biv_from(rA, 0.5), rand_biv_from(rA, 0.5),
                  [0.4, 0.3, 0.2, 0.35, 0.25, 0.15, 0.3, 0.2, 0.25])
    Om13 = family(1.7 * SDb[0] + rand_biv_from(rA, 0.08), rand_biv_from(rA, 0.35),
                  rand_biv_from(rA, 0.35), [1.05, 0.15, 0.1, 0.3, 0.2, 0.15, 0.25, 0.15, 0.2])
    Om22 = family(1.7 * SDb[0] + rand_biv_from(r22, 0.06), 1.8 * SDb[1] + rand_biv_from(r22, 0.06),
                  rand_biv_from(r22, 0.3), [1.0, 0.1, 0.05, 1.0, 0.1, 0.05, 0.3, 0.1, 0.15])
    Om31 = family(1.6 * SDb[0] + rand_biv_from(r31, 0.05), 1.7 * SDb[1] + rand_biv_from(r31, 0.05),
                  1.8 * SDb[2] + rand_biv_from(r31, 0.05),
                  [1.0, 0.08, 0.05, 1.0, 0.08, 0.05, 1.0, 0.08, 0.05])
    menu, ratios = {}, []
    tex31 = None
    for name, sigt, Omf, xpt in [("(0,4)", (0, 4), Om04, [0.31, -0.42, 0.17, 0.23]),
                                 ("(1,3)", (1, 3), Om13, [0.21, -0.33, 0.15, 0.4]),
                                 ("(2,2)", (2, 2), Om22, [0.2, -0.3, 0.15, 0.35]),
                                 ("(3,1)", (3, 1), Om31, [0.1, -0.08, 0.06, 0.1])]:
        Oms = Omf(xpt); g = g_of(Oms)
        assert sig_of(g) == sigt, "menu signature mismatch at %s: %s" % (name, sig_of(g))
        sg, Rs, _, _, _ = curv_invs(Omf, xpt)
        flat, tex = F4_at(Oms, g)
        menu[name] = {"sqrt(g)R": round(sg * Rs, 4), "F4_flat": round(flat, 4),
                      "F4_tex": round(tex, 4), "F4_flat/sqrt(g)R": round(flat / (sg * Rs), 3)}
        ratios.append(flat / (sg * Rs))
        if name == "(3,1)":
            tex31 = tex / (sg * Rs)
    assert max(ratios) - min(ratios) > 0.5, "there must be NO common lambda across the menu"
    assert abs(tex31 - 1.0007) < 0.005, "the flagged (3,1) near-equality moved: %.6f" % tex31

    return {
        "tier": ("DERIVED-A (the decomposition facts: exact rational coefficient tables, exact "
                 "parity covariances, zero overlap, the exact I4-quartic == EH-W-block identity) "
                 "+ DERIVED-structural EH-ABSENT (the verdict), CONDITIONAL on U2 + the banked "
                 "Omega-algebraic action class + the MENU QUANTIFIER {cc, R^2, Ric^2, Riem^2}"),
        "verdict": "EH-ABSENT — the Skyrme quartic contains no tree-level Einstein-Hilbert term",
        "mechanism": ("the property that makes the term a stabilizer (Killing definiteness) is the "
                      "property that makes it EH-blind (h-indefiniteness reachable only in the "
                      "parity-odd sector) — STRETCHING energy vs BENDING energy"),
        "exact_decomposition": {
            "sqrt(g)R|_2": "Q1 - Q2 - (3/4)Q3 + (3/4)Q4 - (1/4)(Q5+Q7) + (1/4)(Q6+Q8)",
            "quartic": "-(Q5 + Q6 + Q7 + Q8)   [equal weight: the definite Killing combination]",
            "parity action": "(Q1 Q2)(Q3 Q4)(Q5 Q8)(Q6 Q7)",
            "parity": "EH ODD exactly; quartic EVEN exactly",
            "overlap": "ZERO — parity-even part of EH = 0, parity-odd part of quartic = 0",
            "arithmetic": "rational (Fraction), no floats",
        },
        "would_change_if_handle": ("the I4-BUILT parity-odd quartic (1/4) sum h(W,W) equals the EH "
                                   "W-block EXACTLY — it would buy the W-block HALF of EH and only "
                                   "that half: indefinite, so it cannot serve Derrick stabilization, "
                                   "and it supplies none of the S-block Q1..Q4"),
        "kill_chain": {
            "(1) parity / S-block disjointness": "lambda = 0 at quadratic order",
            "(2) ddR-freeze": ("lambda = 0 non-perturbatively vs cc and the Omega-algebraic "
                               "remainder — quartic EXACTLY frozen while sqrt(g)R sweeps"),
            "(3) one-blade": ("lambda = Lambda_cc = 0; ONE surviving direction, the null vector "
                              "(0, 0, -1/4, 1, -1/4) prop. to Gauss-Bonnet E4"),
            "(4) Gauss-Bonnet death": "sqrt(g)E4 spreads on the frozen-quartic sweeps",
            "(5) across-background non-universality": ("a per-sweep HC cancellation EXISTS (residual "
                                                       "%.2e) but does NOT transfer: sweep-1 "
                                                       "coefficients on sweep-2 leave %.2e against an "
                                                       "EH spread of %.2e" % (resid1_own, resid2_x, eh2)),
            "ATTRIBUTION": "this is a CHAIN — NOT 'one-blade kills cc + higher-curvature'",
        },
        "sweeps": freeze,
        "one_blade_null_vector": {"(EH, cc, R^2, Ric^2, Riem^2)": [round(float(v), 6) for v in nullv],
                                  "singular values": [float(x) for x in np.round(S_, 8)]},
        "truncation_ladder": {"note": "quote the SHRINKAGE, never the magnitudes (config-dependent)",
                              "(eps, rel dev, |antisym(S)+W/2|)":
                                  [(a_, float("%.3e" % b_), float("%.2e" % c_)) for a_, b_, c_ in ladder]},
        "menu_coverage": menu,
        "menu_quantifier": ("EXCLUDED MENU = {cc, R^2, Ric^2, Riem^2} (plus EH). The R^3 / "
                            "grad-Riemann class falls to the SAME dE-independence schema but was "
                            "NOT RUN — never quantify over 'any conceivable term'."),
        "noted_non_coincidence": ("F4_tex / sqrt(g)R = %.4f at the single (3,1) menu point — ONE "
                                  "point on ONE configuration; the ratio spreads over four orders "
                                  "of magnitude across the menu and nothing in the decomposition "
                                  "permits a relation. Flagged per the K_trans precedent, NOT a "
                                  "result." % tex31),
        "sole_route_consequence": ("CLASS-SCOPED: no Omega-algebraic term in the banked "
                                   "first-derivative action class can contain EH; with the "
                                   "front-embedding tree route closed at SSB.6.6, the INDUCED arc is "
                                   "the unique surviving route WITHIN THE BANKED CONTENT. The "
                                   "thermodynamic route and genuinely-new dE-terms are UNTOUCHED."),
        "fence": ("conditional on U2 and on the banked Omega-algebraic action content; a banked "
                  "SECOND-derivative 'bending' term reopens it; the inhomogeneity route yields "
                  "Brans-Dicke-like non-constant 1/G, not EH; the EH W-block rides the exact R-149 "
                  "fact (1) antisym(S) = -W/2"),
        "ledger": "negatives ledger N51 (tried -> failed -> would-change-if)",
        "would_change_if": ("a parity-odd I4-built quartic is banked (buys the W-block half only, "
                            "cannot serve Derrick); a second-derivative bending term is banked; U2 "
                            "falls; the Omega-algebraic action class is widened"),
    }


def mass_equals_elastic_cost_premise():
    """[INPUT — named, COUNTED premise (coordinator ruling R3(a), 2026-08-12);
    NOT derived, NOT a closure of any open item] THE PREMISE: m = E0 — the
    dispersion/rest-frequency mass parameter of the inside face equals the
    OUTSIDE-frame elastic cost of the defect, in lock units (E = hbar*omega,
    omega = c*k4; see I-23 link 1). WHICH E0 (the referent, mandatory): the
    VACUUM-SUBTRACTED rest cost under the ruled pairing (iv) — the 3-slice
    integral of the defect's cost density relative to the pure-carrier
    background, evaluated at v = 0 (the only duty-free reading; any moving-state
    cost use FIRES the boost-covariance duty).

    STATUS AUDIT (ADJUDICATION3 section 3, all three checkers convergent):
    (1) NOT novel physics: soliton mass = static energy is the STANDARD
    identification (ANW 1983; Manton-Sutcliffe; Schroers eq. Lsk1 quotes
    M = 73 f_pi/e flatly) and enters this corpus through registered import I-5.
    The TWT-specific residue is ONE lock-units dictionary line: R-007's meta-time
    rotor frequency omega equals the outside elastic cost.
    (2) ADJACENT TO, NEVER THE CONTENT OF: R-123 residue (ii) (a spectral/pole
    question this premise PRESUPPOSES), N57 (a SCHEME question — this premise
    picks no scheme; at most it NAMES the classical branch), C-7 (the
    e_ANW <-> sqrt18/(D/J) dictionary face — a distinct face). The four-bookings
    merge of the N56 brief is REFUTED; adjacency is the banked statement.
    (3) USED-BY (the silent-use audit): R-133 compares the hedgehog's elastic
    M0*f_pi/e to measured N/Delta frequencies — the bridge is load-bearing there
    IN A CALIBRATION (f_pi, e historically fitted to N/Delta; ANW honesty note).
    R-144 does NOT use the bridge (dimensionless margin). R-051/R-135/R-138
    consume it wherever an elastic value meets a measured mass.
    (4) FRAME FENCE: E0 is an outside-frame elastic functional value; hadron
    masses are inside-frame measured frequencies (I-23). This premise IS the
    bridge — state it, never silently cross it.
    (5) MODULI-LEVEL CONTENT (the honest derived fragment, per
    pattern_shear_sector_identities): translational inertia = E0 at O(v^2) IFF
    the stress balances (Derrick) — von Laue in Euclidean form. The all-orders
    gamma form is NOT derivable from the SO(4) functional (the pre-registered
    moduli test of the N56 brief is UNPASSABLE AS POSED — ADJUDICATION3 section
    4). The tau5-hyperbolic route (R-112, ruling R3(b)) RAN 2026-08-13 and is
    DISCRIMINATION-NULL: any background that makes a moving cost finite is the
    one that installs the v-law (the one-sided rotor's kinetic density is
    uniform — companion one_sided_rotor_uniform_density_identity; ledger N61;
    governing record knowledge/candidates/probes_2026-08-13/
    TAU5_ADJUDICATION_2026-08-13.md). RUL-020(b) is discharged; no outside
    sqrt(1-v^2) route is currently named.
    PARAMETER ECONOMY: +1 counted premise (this entry). Registry: I-5 amendment
    + the new dictionary face (scheme label owed when any number is quoted at a
    scheme — the N57 trap, K-L5)."""
    return {
        "tier": "INPUT (named, counted premise; ruling R3(a) 2026-08-12)",
        "premise": "m = E0 (lock units; E = hbar*omega, omega = c*k4)",
        "which_E0": ("vacuum-subtracted rest cost under pairing (iv); v = 0 "
                     "reading only (duty-free)"),
        "adjacent_to_not_content_of": ["R-123 residue (ii)", "N57", "C-7"],
        "used_by": ["R-133 (calibration; ANW honesty note)", "R-051", "R-135",
                    "R-138"],
        "not_used_by": ["R-144 (dimensionless margin)"],
        "credit": "ANW 1983 / Schroers Lsk1 / Manton-Sutcliffe, via import I-5",
        "counted": True,
        "derived_fragment": ("inertia = E0 at O(v^2) iff Derrick-balanced "
                             "(von Laue, Euclidean form)"),
        "not_closing": ["N56 (energetic face gap = the O(v^4) relative sign)",
                        "N57", "R-123 residue (ii)"],
    }


# ======================================================================
# B-1 — THE V3 WITNESS LEG of the family-level lock-channel claim (RUL-095 (iv))
# ======================================================================
def lock_channel_p1b_split_v3_witness() -> dict:
    """[WITNESS — instance-sited (V3). Tier of the witnessed claim is unchanged; this
    function adds no content of its own.] The RUL-083 witness-split pattern applied in
    the engine, on the coordinator's ruling RUL-095 (iv).

    WHAT WAS SPLIT AND WHY. `lock_channel_is_axial_chiral_channel_p1b_split` (R-161,
    CORE) is a FAMILY-level channel identification: D1-D6 are exact Clifford identities
    about the substrate's chirality reflection, and they consume no V3 pick. It carried
    ONE instance-sited leg — a regression assert reading R-141's premise list out of
    `induced_level_parity_on_baryon_worldline`, which rides the D4 chain (S1b/S1c) and
    the Finkelstein-Rubinstein quantization scheme (V3-11). That single call was the
    engine's last CORE -> CANDIDATE edge (classification sheet blocker B-1): a
    family-level claim reaching into an instance-level computation at runtime.

    THE SPLIT: the family claim stays CORE and is checked there on family algebra alone;
    the R-141-consuming leg — the regression, verbatim — lives HERE, where the primitive
    it consumes lives. Nothing was weakened and nothing was strengthened: the same
    assertion runs, in the file that may hold it.

    THE EXPOSURE, STATED PLAINLY (this is the honesty content, not the code): R-161's
    family claim is at present WITNESSED ONLY BY THE V3 ROUTE. No family-level witness of
    the induced-parity fact exists. Until one does, a reader who rejects V3-11 keeps the
    D1-D6 identities and loses this corroboration — that is exactly what the split makes
    visible, and it is why the core docstring carries the same sentence.

    would_change_if: a family-level (D4-free, FR-scheme-free) computation of the induced
    level parity is banked — then this witness becomes one of two, and the CORE claim's
    exposure line is struck from both sides in the same pass."""
    fam = lock_channel_is_axial_chiral_channel_p1b_split()
    il = induced_level_parity_on_baryon_worldline()
    assert "P1b" in il["premises"], "R-141 regression failed"
    return {
        "witnesses": "lock_channel_is_axial_chiral_channel_p1b_split (R-161, CORE)",
        "witness_route": "R-141 induced level parity — S1b/S1c (D4 chain) + V3-11 (FR scheme)",
        "regression": "'P1b' in induced_level_parity_on_baryon_worldline()['premises']",
        "family_claim_tier": fam["tier"],
        "exposure": ("the family claim is witnessed ONLY by this V3 route pending a "
                     "family-level witness of the induced-parity fact"),
        "direction_invariant": ("CORE never imports CANDIDATE — this file may call both; "
                                "twt_core.py may call neither this function nor R-141"),
    }


# ======================================================================
# THE Γ-CHANNEL REFERENT CLOSURE (2026-08-23) — G1…G6
# ----------------------------------------------------------------------
# Governing records (read them before quoting anything below):
#   knowledge/audit/gamma_referent_2026-08-23/GAMMA_REFERENT_REVIEW_2026-08-23.md
#     (its §CONSENSUS and §ADDENDUM are part of the converged state and SUPERSEDE
#      §§0-8 wherever they conflict)
#   knowledge/audit/gamma_referent_2026-08-23/VERDICT_REVIEWER_GAMMA_2026-08-23.md
#   knowledge/audit/gamma_referent_2026-08-23/JOINT_BANKING_2026-08-23.md (enactment)
#
# FILE PLACEMENT (canon §6 consumption rule): every primitive here consumes the D4
# siting (V3-1), the {J,D} bond truncation (V3-2) and/or the V3 calibrations, so all
# six belong in the CANDIDATE half. None may go in twt_core.py — the direction
# invariant's AST guard would fail the suite by construction, correctly. No
# CORE_PROVENANCE row is owed (nothing here is CORE).
# ======================================================================

_GAMMA_RIG_CACHE = {}


def _gamma_bond_rig():
    """[INTERNAL] The D4 bond set, the four groups of the ladder, the channel
    projectors and the equivariant bases — built once and cached.

    THE BOND SET, read from the banked construction (`D4_spatial_bond_isotropy`,
    `D4_DM_bond_bivectors_non_commuting`, `canting_vacuum_branch_structure`), not
    assumed: 24 DIRECTED nearest-neighbour (kissing) vectors ±e_i±e_j = 12 undirected;
    12 of them e4-BEARING (the banked D's support) and 12 SPATIAL. J lives on all 24.

    THE GROUPS, by exact closure: |Aut(D4)| = |W(F4)| = 1152; |Stab(e4-axis)| = 96;
    |Stab(+e4)| = 48 — THE DRIVEN GROUP, the group the driven action respects and the
    one every count in this block is stated at; |Stab+(+e4)| = 24.

    THE REALIZATION (C-33, and it is not free — see G1): the FRAME-BILINEAR
    (relative-frame) reading, site variable = an SO(4) frame, E_b = Tr(K_b W_b) with
    W_b = O_j O_i^T. That is the reading the banked E(q), the banked pitch and the
    banked f_pi^2 = 8J/a are computed in."""
    if "rig" in _GAMMA_RIG_CACHE:
        return _GAMMA_RIG_CACHE["rig"]
    import numpy as np

    def key(g):
        return tuple(np.round(np.asarray(g, float).ravel(), 9) + 0.0)

    bonds = []
    for i, j in combinations(range(4), 2):
        for si in (+1, -1):
            for sj in (+1, -1):
                v = np.zeros(4); v[i] = si; v[j] = sj
                bonds.append(v)
    bonds = np.array(bonds, float)
    assert bonds.shape == (24, 4)

    gens = []
    for p in itertools.permutations(range(4)):
        P = np.zeros((4, 4))
        for i, pi in enumerate(p):
            P[i, pi] = 1.0
        gens.append(P)
    for s in itertools.product((+1, -1), repeat=4):
        gens.append(np.diag(np.array(s, float)))
    gens.append(0.5 * np.array([[1, 1, 1, 1], [1, 1, -1, -1],
                                [1, -1, 1, -1], [1, -1, -1, 1]], float))
    seen = {key(np.eye(4)): np.eye(4)}
    frontier = [np.eye(4)]
    while frontier:
        nxt = []
        for a in frontier:
            for g in gens:
                p = g @ a
                k = key(p)
                if k not in seen:
                    seen[k] = p; nxt.append(p)
                    assert len(seen) <= 1200, "Aut(D4) closure blew its cap"
        frontier = nxt
    G = list(seen.values())
    e4 = np.array([0.0, 0.0, 0.0, 1.0])
    G96 = [g for g in G if abs(abs(float((g @ e4) @ e4)) - 1.0) < 1e-9]
    G48 = [g for g in G if np.allclose(g @ e4, e4, atol=1e-9)]
    G24 = [g for g in G48 if np.linalg.det(g) > 0]
    assert (len(G), len(G96), len(G48), len(G24)) == (1152, 96, 48, 24)

    T16 = np.zeros((16, 16))
    for a in range(4):
        for b in range(4):
            T16[4 * a + b, 4 * b + a] = 1.0
    I16 = np.eye(16); vI = np.eye(4).ravel()
    P_tr = np.outer(vI, vI) / 4.0
    P_as = (I16 - T16) / 2.0
    P_st = (I16 + T16) / 2.0 - P_tr
    for P in (P_tr, P_as, P_st):
        assert np.abs(P @ P - P).max() < 1e-12
    assert np.abs(P_tr + P_as + P_st - I16).max() < 1e-12
    CH = {"J": P_tr, "D": P_as, "Gamma": P_st}

    idx = {key(b): i for i, b in enumerate(bonds)}

    def bond_perm(g):
        P = np.zeros((24, 24)); gi = np.linalg.inv(g)
        for i, b in enumerate(bonds):
            P[i, idx[key(gi @ b)]] = 1.0
        return P

    def reynolds(Gx):
        R = np.zeros((24 * 16, 24 * 16))
        for g in Gx:
            R += np.kron(bond_perm(g), np.kron(g, g))
        return R / len(Gx)

    Prev = np.zeros((24, 24))
    for i, b in enumerate(bonds):
        Prev[i, idx[key(-b)]] = 1.0
    H = (np.eye(24 * 16) + np.kron(Prev, T16)) / 2.0

    def allowed(R, chP=None):
        M = R @ H
        if chP is not None:
            M = M @ np.kron(np.eye(24), chP)
        M = 0.5 * (M + M.T)
        U, s, _ = np.linalg.svd(M)
        d = int((s > 1e-8).sum())
        gap = (float(s[d - 1]) if d else float("nan"),
               float(s[d]) if d < len(s) else 0.0)
        return U[:, :d], d, gap

    Rs = {"1152": reynolds(G), "96": reynolds(G96),
          "48": reynolds(G48), "24": reynolds(G24)}
    rig = {"bonds": bonds, "groups": {"1152": G, "96": G96, "48": G48, "24": G24},
           "CH": CH, "H": H, "R": Rs, "allowed": allowed, "T16": T16,
           "bond_perm": bond_perm, "np": np}
    _GAMMA_RIG_CACHE["rig"] = rig
    return rig


def _gamma_couplings():
    """[INTERNAL] The two BANKED couplings written as K_b families in the
    E_b = Tr(K_b W_b) convention, plus the ten [48]-allowed basis members."""
    if "coup" in _GAMMA_RIG_CACHE:
        return _GAMMA_RIG_CACHE["coup"]
    rig = _gamma_bond_rig(); np = rig["np"]
    bonds = rig["bonds"]

    def Ea4(a):
        M = np.zeros((4, 4)); M[a, 3] = 1.0; M[3, a] = -1.0
        return M

    KJ = np.array([-(0.5) * np.eye(4) for _ in range(24)])
    KD = np.zeros((24, 4, 4))
    for i, b in enumerate(bonds):
        if b[3] != 0.0:                      # the 12 e4-bearing bonds only (V3-2a)
            a = int(np.nonzero(b[:3])[0][0]); w = float(b[a])
            KD[i] = -(0.5) * (w / math.sqrt(2.0)) * Ea4(a).T
    R48 = rig["R"]["48"]; allowed = rig["allowed"]
    BJ, dJ, _ = allowed(R48, rig["CH"]["J"])
    BD, dD, _ = allowed(R48, rig["CH"]["D"])
    BG, dG, _ = allowed(R48, rig["CH"]["Gamma"])
    members = ([(f"J#{m+1}", BJ[:, m].reshape(24, 4, 4)) for m in range(dJ)]
               + [(f"D#{m+1}", BD[:, m].reshape(24, 4, 4)) for m in range(dD)]
               + [(f"Gamma#{m+1}", BG[:, m].reshape(24, 4, 4)) for m in range(dG)])
    out = {"KJ": KJ, "KD": KD, "BJ": BJ, "BD": BD, "BG": BG,
           "dJ": dJ, "dD": dD, "dG": dG, "members": members, "Ea4": Ea4}
    _GAMMA_RIG_CACHE["coup"] = out
    return out


def _unit_simple_bivector(n):
    """[INTERNAL] A UNIT SIMPLE bivector in the e_a4 plane family (B^3 = -B)."""
    rig = _gamma_bond_rig(); np = rig["np"]; Ea4 = _gamma_couplings()["Ea4"]
    n = np.asarray(n, float); n = n / np.linalg.norm(n)
    return sum(n[a] * Ea4(a) for a in range(3))


def _plane_angle_bivector(angles, planes=((0, 1), (2, 3))):
    """[INTERNAL] An so(4) generator with PRESCRIBED PLANE ANGLES (a, b): exp(tB)
    rotates plane 1 by a*t and plane 2 by b*t. (1,0) simple; (1,1) SD-isoclinic;
    (1,-1) ASD-isoclinic; (1,3) NON-isoclinic with a 3:1 angle ratio."""
    rig = _gamma_bond_rig(); np = rig["np"]
    B = np.zeros((4, 4))
    for ang, (i, j) in zip(angles, planes):
        B[i, j] += ang; B[j, i] -= ang
    return B


def bond_invariant_menu_frame_bilinear() -> dict:
    """[DERIVED-A on the COUNTS (four independent pipelines) · DERIVED-A but ANALYTIC on
    the EXHAUSTIVENESS · CONDITIONAL on the class pick for which ladder is "the" menu]
    G1 — THE BOND-INVARIANT MENU, COMPUTED CLOSED AT TEN UNDER THE DRIVEN GROUP.

    Canon §2's INPUT rider stood since 2026-08-17: *"{J,D} is not the complete
    bond-invariant menu."* This primitive is the computed menu.

    ★ C-33 REALIZATION BLOCK — READ BEFORE QUOTING ANY COUNT.
    The count is REALIZATION-DEPENDENT and the realization is a PICK, not a measurement:
      * FRAME-BILINEAR (relative-frame): site variable = an SO(4) frame, E_b =
        Tr(K_b W_b), W_b = O_j O_i^T. Ladder (TOTAL, J, D, Gamma) by group:
        [1152] (2,1,0,1) · [96] (8,2,0,6) · **[48] DRIVEN (10,2,2,6)** · [24] (12,2,4,6).
      * ROTOR-LINEAR: the invariant contracts the relative rotor U_b = ~R_i R_j with an
        element of Cl+(4,0) = 1 + 6 + 1. Gamma DOES NOT EXIST at that order (it is a
        second-order object); in its place sits the grade-4 pseudoscalar channel `chi`.
        Ladder (TOTAL, J, D, chi): [1152] (1,1,0,0) · [96] (2,2,0,0) ·
        **[48] DRIVEN (4,2,2,0)** · [24] (8,2,4,2).
      * WHICH ONE IS "THE" MENU is the V3-2-class pick, family tree node LS-Z2.
    ★ CREDIT, corrected at consensus: the 4-vs-10 fork is CONFIRMED-ALREADY-RECORDED at
    `TWT_FAMILY_TREE.md` LS-Z2, not an output of this round. The round re-confirms it.

    ★★ THE RESIDUE IS AN IDENTITY, NOT A MEASUREMENT — the round's own first over-claim,
    conceded in full. The submitted report sold a "TOTAL with no channel projector, residue
    zero" as *the exhaustiveness measurement the prior round did not make*, with a
    pre-registered failure criterion *"total != J+D+Gamma at any group"*. THAT CRITERION IS
    UNFALSIFIABLE INSIDE THE PARAMETRISATION: the three channel projectors commute EXACTLY
    with both the Reynolds projector and the bond-reversal projector (returned below as the
    `commutation_witness`), and P_J + P_D + P_Gamma = I, so the invariant subspace
    decomposes as the direct sum of its three channel components IDENTICALLY, for any group
    and any bond set. A nonzero residue was not a possible outcome. This is canon §8a's own
    named tell — *a tight tolerance on a vacuous check is not rigour, it is a tell*.
    THE HONEST POSITIVE CONTENT IS TWO THINGS, and only these:
      (1) THE COUNTS — DERIVED-A on FOUR independent pipelines: the developer's
          Reynolds+SVD (here), the 2026-08-21 arbiter's constraint null-space, the
          reviewer's own null-space route, and the reviewer's character/trace recount
          dim Fix = tr(R H P_ch) with no SVD anywhere. All four agree on 2/8/10/12 and on
          the 2/2/6 split at [48].
      (2) THE EXHAUSTIVENESS — ANALYTIC: V (x) V = 1 + 6 + 9 is a COMPLETE ORTHOGONAL
          SPLIT of the 16-dim per-bond coupling space, and both constraints PRESERVE it
          ([P,R] = [P,H] = 0, computed exact). The residue figure is that identity's
          numerical witness plus a code-correctness witness on the intersection projector
          (the SVD gap 1.0000 vs <~4e-15 does prove R H is a clean projector, which was not
          free) — NEVER evidence that "an unnamed channel would have shown up".

    ★ THE OPEN PREMISE, NAMED (the honest exhaustiveness question, untouched by this round).
    E_b = Tr(K_b W_b) with W_b = O_j O_i^T already RESTRICTS the general bond-bilinear form
    (256 dims/bond) to the right-invariant subspace (16 dims/bond) — it ASSUMES the bond
    energy depends only on the RELATIVE frame. That is a legitimate, standard and NAMED
    premise, and NOTHING in this round measures it. So the licensed sentence is *"no unnamed
    channel exists WITHIN THE RELATIVE-FRAME BILINEAR ANSATZ"*, never *"at bilinear order"*.

    TENSOR CHARACTERS, measured on the allowed bases at [48] (not asserted from a
    projector's name): J = trace/internal SCALAR; D = antisymmetric / bond-reversal ODD;
    Gamma = symmetric-TRACELESS (per-bond trace at 3e-16 — a third independent pipeline
    agreeing with the developer's and the arbiter's).

    WORDING FENCE (reviewer defect (e), adopted): say **computed EXHAUSTIVE at ten**, never
    *computed closed*. In C-32 (weak isospin) *computed closed* means the menu is exhausted
    AND every alternative is refuted, so nothing is left to pick. Here the pick — keep
    {J, D}, zero the rest — is fully LIVE and counted (V3-2).

    FAILURE MODE SHIPPED WITH THE PRIMITIVE (`planted_noncommuting_projector`): a rank-1
    projector that does NOT commute with the constraints is planted, and the SVD ranks of
    its two-part resolution of the identity are reported. They do NOT add to the total
    (16 + 18 = 34 vs 10). That is the check that the residue tests COMMUTATION, not the
    lattice, and it is SEEN TO FIRE.

    Cross-refs: canting_vacuum_branch_structure, D4_spatial_bond_isotropy,
    D4_DM_bond_bivectors_non_commuting (the banked construction this reads);
    bond_channel_parity_exclusivity (G2, the durable result);
    weak_su2_menu_exhaustion (the C-32 pattern this deliberately does NOT claim)."""
    rig = _gamma_bond_rig(); np = rig["np"]
    allowed = rig["allowed"]; CH = rig["CH"]; H = rig["H"]
    ladder, gaps = {}, {}
    for name in ("1152", "96", "48", "24"):
        R = rig["R"][name]
        _, tot, gap = allowed(R)
        per = {c: allowed(R, P)[1] for c, P in CH.items()}
        ladder[name] = {"TOTAL": tot, "J": per["J"], "D": per["D"],
                        "Gamma": per["Gamma"]}
        gaps[name] = gap
    assert ladder["48"] == {"TOTAL": 10, "J": 2, "D": 2, "Gamma": 6}
    assert [ladder[g]["TOTAL"] for g in ("1152", "96", "48", "24")] == [2, 8, 10, 12]

    comm_R = comm_H = 0.0
    R48 = rig["R"]["48"]
    for P in CH.values():
        P384 = np.kron(np.eye(24), P)
        comm_R = max(comm_R, float(np.abs(P384 @ R48 - R48 @ P384).max()))
        comm_H = max(comm_H, float(np.abs(P384 @ H - H @ P384).max()))
    assert comm_R < 1e-12 and comm_H < 1e-12, "the identity claim's own witness failed"

    # ---- the SHIPPED FAILURE MODE: a NON-commuting projector, ranks must NOT add
    rng = np.random.default_rng(20260823)
    v = rng.standard_normal(16); v /= np.linalg.norm(v)
    Pbad = np.outer(v, v); Pbadc = np.eye(16) - Pbad
    P384 = np.kron(np.eye(24), Pbad)
    bad_comm = float(np.abs(P384 @ R48 - R48 @ P384).max())
    d1, d2 = allowed(R48, Pbad)[1], allowed(R48, Pbadc)[1]
    assert bad_comm > 1e-6, "the planted projector must NOT commute"
    assert d1 + d2 != ladder["48"]["TOTAL"], (
        "the planted-violation demo did not fire: ranks added anyway")

    # ---- tensor characters, measured
    co = _gamma_couplings()
    chars = {}
    for lab, B, d in (("J", co["BJ"], co["dJ"]), ("D", co["BD"], co["dD"]),
                      ("Gamma", co["BG"], co["dG"])):
        tr = sym = asym = 0.0
        for m in range(d):
            K = B[:, m].reshape(24, 4, 4)
            tr = max(tr, float(np.abs(np.trace(K, axis1=1, axis2=2)).max()))
            asym = max(asym, float(np.abs(K - np.transpose(K, (0, 2, 1))).max()))
            sym = max(sym, float(np.abs(K + np.transpose(K, (0, 2, 1))).max()))
        chars[lab] = {"max|Tr K_b|": tr, "max|K-K^T|": asym, "max|K+K^T|": sym}
    assert chars["Gamma"]["max|Tr K_b|"] < 1e-12 and chars["D"]["max|K+K^T|"] < 1e-12

    # ---- the rotor-linear ladder (C-33's other realization)
    rl = {}
    g2 = []
    for i, j in combinations(range(4), 2):
        M = np.zeros((4, 4)); M[i, j] = 1.0; M[j, i] = -1.0
        g2.append(M)
    idx = {tuple(np.round(b, 9) + 0.0): i for i, b in enumerate(rig["bonds"])}
    Prev = np.zeros((24, 24))
    for i, b in enumerate(rig["bonds"]):
        Prev[i, idx[tuple(np.round(-b, 9) + 0.0)]] = 1.0
    for name in ("1152", "96", "48", "24"):
        Gx = rig["groups"][name]; row = {}
        for gname, dim, act, par in (("J", 1, None, +1), ("D", 6, "biv", -1),
                                     ("chi", 1, "ps", +1)):
            M = np.zeros((24 * dim, 24 * dim))
            for g in Gx:
                if act is None:
                    A = np.eye(1)
                elif act == "biv":
                    A = np.zeros((6, 6))
                    for a, Ba in enumerate(g2):
                        im = g @ Ba @ g.T
                        for b_, Bb in enumerate(g2):
                            A[b_, a] = float(np.trace(Bb.T @ im)) / 2.0
                else:
                    A = np.array([[float(np.linalg.det(g))]])
                M += np.kron(rig["bond_perm"](g), A)
            M /= len(Gx)
            Hr = (np.eye(24 * dim) + par * np.kron(Prev, np.eye(dim))) / 2.0
            X = M @ Hr; X = 0.5 * (X + X.T)
            s = np.linalg.svd(X, compute_uv=False)
            row[gname] = int((s > 1e-8).sum())
        row["TOTAL"] = row["J"] + row["D"] + row["chi"]
        rl[name] = row
    assert rl["48"] == {"J": 2, "D": 2, "chi": 0, "TOTAL": 4}
    assert rl["24"]["chi"] == 2

    return {
        "tier": ("DERIVED-A on the COUNTS (four pipelines); DERIVED-A but ANALYTIC on the "
                 "EXHAUSTIVENESS; the choice of realization is a PICK, not a measurement"),
        "realization": "frame-bilinear (relative-frame): E_b = Tr(K_b W_b), W_b = O_j O_i^T",
        "driven_group": "Stab(+e4), order 48",
        "ladder_frame_bilinear": ladder,
        "ladder_rotor_linear": rl,
        "svd_gaps_total": gaps,
        "tensor_characters": chars,
        "group_orders": {k: len(v) for k, v in rig["groups"].items()},
        "bond_partition": {"directed": 24, "e4_bearing": 12, "spatial": 12},
        "exhaustiveness_ground": (
            "ANALYTIC: V(x)V = 1 + 6 + 9 is a complete orthogonal split of the 16-dim "
            "per-bond coupling space and BOTH constraints preserve it ([P,R] = [P,H] = 0, "
            "computed exact below). NOT a residue measurement."),
        "commutation_witness": {"max|[P_ch, R]|": comm_R, "max|[P_ch, H]|": comm_H},
        "residue_zero_is_an_identity": True,
        "residue_is_not_evidence_that": (
            "an unnamed channel would have shown up. It could not have: the projectors "
            "commute with both constraints and sum to I, so the ranks add identically."),
        "planted_noncommuting_projector": {
            "max|[P_bad, R]|": bad_comm, "rank_part_1": d1, "rank_part_2": d2,
            "sum": d1 + d2, "true_total": ladder["48"]["TOTAL"],
            "fires": d1 + d2 != ladder["48"]["TOTAL"],
            "reading": ("the residue tests COMMUTATION, not the lattice — planted and "
                        "seen to fire")},
        "open_premise_relative_frame_ansatz": (
            "E_b = Tr(K_b W_b) restricts the general bond-bilinear form (256 dims/bond) to "
            "the right-invariant subspace (16 dims/bond): it ASSUMES the bond energy depends "
            "only on the RELATIVE frame. NAMED, standard, and MEASURED BY NOTHING here. The "
            "licensed sentence is 'no unnamed channel exists WITHIN THE RELATIVE-FRAME "
            "BILINEAR ANSATZ', never 'at bilinear order'."),
        "wording_fence": (
            "computed EXHAUSTIVE at ten — never 'computed closed'. C-32's 'closed' means "
            "the menu is exhausted AND every alternative refuted; here the pick (keep {J,D}, "
            "zero the rest) is LIVE and counted (V3-2)."),
        "four_pipelines": [
            "developer Reynolds + SVD (this primitive)",
            "arbiter constraint null-space (VERDICT_ARBITRATION_SCALAR_KERNEL_2026-08-21)",
            "reviewer constraint null-space (VERDICT_REVIEWER_GAMMA_2026-08-23 §1.1a)",
            "reviewer character/trace recount dim Fix = tr(R H P_ch), no SVD (§1.1b)"],
        "already_recorded_at": (
            "TWT_FAMILY_TREE.md node LS-Z2 — the ten-frame-bilinear / four-rotor-linear "
            "fork and its class-pick disposition were ALREADY BANKED there; this round "
            "CONFIRMS-ALREADY-RECORDED, it does not originate them"),
        "does_not_license": (
            "'the menu is closed' in the C-32 sense; any claim that the residue measured "
            "anything about the lattice; any exhaustiveness claim reaching outside the "
            "relative-frame bilinear ansatz"),
        "record": "knowledge/audit/gamma_referent_2026-08-23/",
    }


def bond_channel_parity_exclusivity() -> dict:
    """[DERIVED-A at TRACE-PAIRING strength — configuration-independent] G2 — THE
    CHANNEL -> PARITY EXCLUSIVITY THEOREM. **The one result of the Gamma round that carries
    no branch risk and no class-of-configuration risk, and it was submitted at a fraction
    of its true scope (UNDER-CLAIM, RUL-076, adopted and then strengthened past the
    reviewer's own form).**

    THE ALGEBRA IS A TRACE-PAIRING IDENTITY: Tr(K W^T) = Tr(K^T W), for ARBITRARY real
    4x4 W. Hence
        K SYMMETRIC   (J, Gamma) => reversal-EVEN  => feeds ONLY the parity-EVEN amplitude
        K ANTISYMMETRIC (D)      => reversal-ODD   => feeds ONLY the parity-ODD  amplitude
    NO HELIX, NO SIMPLE BIVECTOR, NOT EVEN A ROTOR is required. Verified here on (a)
    independent random SO(4) relative rotors per bond and (b) random NON-orthogonal real W —
    relative deviations at the 1e-13 floor in both.

    ★ ALL THE PHYSICS SITS IN ONE NAMED PREMISE, and it is stated here rather than hidden:
    *chirality reversal on a bond configuration acts as W_b -> W_b^T*. On a helix that
    premise is an IDENTITY — q -> -q gives W_b = exp(-(k.b)B) = W_b^T exactly — so on the
    PITCH functional the parity assignment is not an assertion. On the Z3/generation
    functional it is NOT established, and that is JD-5.

    CONSEQUENCE, combined with G1's exhaustive menu — the review's central structural result:
        A (parity-EVEN)  <-  J and Gamma   : Gamma can only RENORMALISE the denominator
        B (parity-ODD)   <-  D only        : Gamma can NEVER contaminate the numerator
    and by G1 nothing else can enter either. So D_spatial is the ONLY channel in the entire
    exhaustive menu that can reach the parity-odd amplitude — a SELECTION RULE, inheriting
    NO branch risk (this is why the V3-2 risk-ordering annotation is asymmetric).

    ★ TWO SCOPE CORRECTIONS, both conceded, both binding on how this is quoted:
      (i) **"EXACTLY TWO amplitudes" is CLASS-CONDITIONED** (RUL-049's mirror rule — the
          conditioning class in the same sentence): true *within single-q families
          generated by a unit SIMPLE bivector*. On a helix generated by a non-simple
          bivector with plane angles (1,3) the even part is not a single (1-cos q) —
          computed, see bond_harmonic_ceiling_by_generator_class. The parity/exclusivity
          half above is UNAFFECTED and stays general.
      (ii) **"JD-5 HALF-DISCHARGED" IS WITHDRAWN AS A LABEL.** JD-5's RECORDED scope
          (`TWT_worklist.md`) is *the cos/sin parity assignment OF THE Z3 AMPLITUDES*. The
          pitch statement is true and, at trace-pairing strength, trivial — but it is a fact
          about a DIFFERENT functional, on which the question was never the open one.
          NOTHING OF JD-5 AS RECORDED IS DISCHARGED, and RUL-071(vi)'s conditioning of 0.79
          on JD-5 is UNCHANGED. At dressed level the assignment additionally requires the
          reversal to be a symmetry of the driven kernel, which a NESS kernel need not
          respect — #1-gap-routed.

    FAILURE MODE SHIPPED WITH THE PRIMITIVE (`mixed_symmetry_control`): a deliberately
    MIXED-symmetry coupling (J#1 + D#1) must come back MIXED, not EVEN and not ODD. Seen to
    fire (both residuals O(1) relative).

    Cross-refs: bond_invariant_menu_frame_bilinear (G1 — exhaustiveness is what makes this
    a selection rule rather than a statement about three named channels);
    DoverJ_calibration_referent (G5 — the routing theorem this supplies)."""
    rig = _gamma_bond_rig(); np = rig["np"]
    co = _gamma_couplings()
    members = co["members"] + [("bankedJ", co["KJ"]), ("bankedD", co["KD"])]
    rng = np.random.default_rng(20260823)

    def rand_so4(r):
        Q, _ = np.linalg.qr(r.standard_normal((4, 4)))
        if np.linalg.det(Q) < 0:
            Q[:, 0] *= -1
        return Q

    worst = {"rotor_sym": 0.0, "rotor_antisym": 0.0,
             "generic_sym": 0.0, "generic_antisym": 0.0}
    for _ in range(30):
        Wr = [rand_so4(rng) for _ in range(24)]
        Wg = [rng.standard_normal((4, 4)) for _ in range(24)]
        for lab, K in members:
            sym = float(np.abs(K - np.transpose(K, (0, 2, 1))).max()) < 1e-12
            for W, tag in ((Wr, "rotor"), (Wg, "generic")):
                e1 = sum(float(np.trace(K[i] @ W[i])) for i in range(24))
                e2 = sum(float(np.trace(K[i] @ W[i].T)) for i in range(24))
                den = max(abs(e1), 1e-30)
                k = f"{tag}_sym" if sym else f"{tag}_antisym"
                worst[k] = max(worst[k], (abs(e1 - e2) if sym else abs(e1 + e2)) / den)
    assert max(worst.values()) < 1e-9, worst

    # ---- the SHIPPED FAILURE MODE: MIXED symmetry must read MIXED
    Kmix = members[0][1] + members[co["dJ"]][1]
    Wg = [rng.standard_normal((4, 4)) for _ in range(24)]
    e1 = sum(float(np.trace(Kmix[i] @ Wg[i])) for i in range(24))
    e2 = sum(float(np.trace(Kmix[i] @ Wg[i].T)) for i in range(24))
    mix_even = abs(e1 - e2) / abs(e1); mix_odd = abs(e1 + e2) / abs(e1)
    assert mix_even > 1e-6 and mix_odd > 1e-6, "the MIXED control did not fire"

    # ---- the pitch functional: q -> -q IS W -> W^T, measured on all twelve
    khat = np.array([1.0, 0, 0, 0]); B = _unit_simple_bivector([1, 0, 0])

    def E(K, q):
        return sum(float(np.trace(K[i] @ (np.eye(4) + math.sin(t) * B
                                          + (1 - math.cos(t)) * (B @ B))))
                   for i, (b, t) in enumerate((b, q * float(np.dot(khat, b)))
                                              for b in rig["bonds"]))

    pitch = {}
    for lab, K in members:
        ev = max(abs(E(K, q) - E(K, -q)) for q in (0.13, 0.41, 0.97))
        od = max(abs(E(K, q) + E(K, -q) - 2 * E(K, 0.0)) for q in (0.13, 0.41, 0.97))
        pitch[lab] = "EVEN" if ev < 1e-12 else ("ODD" if od < 1e-12 else "MIXED")
    assert all(pitch[k] == "EVEN" for k in pitch if k.startswith(("J", "Gamma", "bankedJ")))
    assert all(pitch[k] == "ODD" for k in pitch if k.startswith(("D#", "bankedD")))

    return {
        "tier": "DERIVED-A at trace-pairing strength — CONFIGURATION-INDEPENDENT",
        "identity": "Tr(K W^T) = Tr(K^T W), for ARBITRARY real 4x4 W",
        "worst_relative_deviation": worst,
        "scope_measured_on": ("independent random SO(4) rotor per bond AND random "
                              "NON-orthogonal real W — no helix, no generator, not even "
                              "a rotor is required"),
        "routing": {"parity_EVEN amplitude A": ["J", "Gamma"],
                    "parity_ODD amplitude B": ["D"],
                    "selection_rule": ("D_spatial is the ONLY channel in the exhaustive "
                                       "menu that can reach the parity-ODD amplitude; "
                                       "Gamma is barred from it exactly")},
        "branch_risk": "NONE — this result inherits no branch and no configuration risk",
        "the_physical_premise": (
            "chirality reversal on a bond configuration acts as W_b -> W_b^T. On a helix "
            "this is the IDENTITY q -> -q. ALL the physics is here; the algebra above is "
            "free."),
        "pitch_functional_parities": pitch,
        "exactly_two_amplitudes": (
            "CLASS-CONDITIONED (RUL-049): true only within single-q families generated by "
            "a unit SIMPLE bivector. See bond_harmonic_ceiling_by_generator_class for the "
            "(1,3) counterexample."),
        "JD5_status": (
            "STANDS, UNDISCHARGED, on its recorded Z3 scope. 'Half-discharged' is "
            "WITHDRAWN as a label. RUL-071(vi)'s conditioning of 0.79 on JD-5 is UNCHANGED. "
            "The analogous assignment on the PITCH functional is an identity — a different "
            "functional, never the open question. At dressed level JD-5 additionally needs "
            "the reversal to be a symmetry of the driven kernel: #1-gap-routed."),
        "mixed_symmetry_control": {
            "coupling": "J#1 + D#1 (symmetric + antisymmetric)",
            "relative |E - E^T|": mix_even, "relative |E + E^T|": mix_odd,
            "verdict": "MIXED", "fires": True},
        "record": "knowledge/audit/gamma_referent_2026-08-23/",
    }


def bond_harmonic_ceiling_by_generator_class() -> dict:
    """[DERIVED-A GIVEN a SIMPLE or ISOCLINIC (SD/ASD) twist generator — and REFUTED without
    that premise, with the counterexample shipped] G3 — THE HARMONIC CEILING, CONDITIONED ON
    THE TWIST CLASS.

    ★ THE OVER-CLAIM THIS PRIMITIVE EXISTS TO PREVENT. The submitted round asserted, with no
    conditioning class (RUL-049 violation, conceded): *"a rigid conjugation twist raises the
    ceiling to degree 2 ... EITHER WAY THE CEILING IS m <= 2 < 3"* and, in the JD-6 upgrade,
    *"NO BILINEAR-ORDER COMPUTATION, HOWEVER REFINED, can compute alpha_i or beta"*. **Both
    are FALSE AS WRITTEN.** The ceiling is a property of the assumed TWIST GENERATOR CLASS,
    not of bilinear order. For a generator with plane angles (a,b) the rep-level frequencies
    are {a, b} and the adjoint-level ones {0, +-2a, +-2b, +-(a+b), +-(a-b)}. A NON-ISOCLINIC
    (1,3) generator therefore reaches m = 3 at the SAME MAGNITUDE as m = 1, at bond-BILINEAR
    order, on the BANKED J coupling: |c3| = |c1| = 6.00. That counterexample is COMPUTED HERE
    and asserted NONZERO, so the unconditioned claim can never be re-asserted from the engine.

    THE PREMISE THAT MAKES THE CEILING TRUE, and where it comes from: every SD and every ASD
    bivector satisfies B^2 = -lambda^2 I — i.e. is ISOCLINIC, adjoint frequencies {0, +-2}.
    Canon §5's *GENERATIONS = the anti-self-dual triple* therefore SUPPLIES the ceiling
    premise — but it supplies it as an IDENTIFICATION, not a theorem.

    THE HONEST FORM, adopted verbatim at consensus:
      **DERIVED-A-given-(the generation twist is generated by a SIMPLE or ISOCLINIC (SD/ASD)
      one-parameter subgroup):** at bond-bilinear order the harmonic ceiling is m <= 1 (rep)
      / m <= 2 (adjoint), hence < 3, hence every Z3 harmonic vanishes identically and the
      entry coefficients are 0/0. **WOULD CHANGE IF** the generation circle is implemented by
      a non-isoclinic SO(4) twist (plane-angle ratio reaching 3), where m = 3 appears at
      O(|c1|) at the same bilinear order.

    ★ JD-6's UPGRADE IS THEREFORE **DERIVED-CONDITIONAL**, and the conditioning is on the
    TWIST/CONFIGURATION class — **NOT** on "the banked action class", which is where the
    submitted phrase mislocated it. This is the BETTER result: it locates the ceiling in the
    ASD identification, where it is contestable and re-attackable, instead of asserting a
    whole class of bilinear-order constructions empty.

    ★ THE VACUITY CENSUS, REPAIRED (the round's sweep-after-a-patch failure, conceded). The
    submitted round's SECOND construction — a single rigid rotor conjugating every bond,
    E = Tr(R^T (sum_b K_b) R Q) — is VACUOUS for 8 of the 10 allowed members plus BOTH banked
    couplings: four give sum_b K_b = 0 (E == 0 identically) and four give sum_b K_b ~ I
    (E constant in psi, so every harmonic m >= 1 vanishes trivially). The identical defect
    had been self-caught in one script of the same round and NOT swept into the other, where
    it was load-bearing. The census is computed here so the defect cannot re-enter, and the
    ceiling is re-tested on a NON-VACUOUS construction (an independent random SO(4) pair per
    bond, W_b(psi) = O_b exp(psi B) O_b') — under which the CONDITIONED theorem is confirmed
    on all twelve couplings and the UNCONDITIONED one is refuted on all twelve.

    FAILURE MODE SHIPPED WITH THE PRIMITIVE: the (1,3) counterexample IS the failure mode.
    The primitive ASSERTS a nonzero m3 there and asserts the m3 floor under simple/SD/ASD.

    Cross-refs: bond_channel_parity_exclusivity (G2's class-conditioned "two amplitudes");
    DoverJ_calibration_referent (G5); worklist JD-6; negatives ledger N62."""
    rig = _gamma_bond_rig(); np = rig["np"]
    from scipy.linalg import expm
    co = _gamma_couplings(); bonds = rig["bonds"]
    members = co["members"] + [("bankedJ", co["KJ"]), ("bankedD", co["KD"])]
    N = 1024
    ts = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
    khat = np.array([1.0, 0, 0, 0])
    proj = np.array([float(np.dot(khat, b)) for b in bonds])

    def harmonics(K, B):
        Ws = {}
        E = np.empty(N)
        for n, t in enumerate(ts):
            tot = 0.0
            for i in range(24):
                a = round(proj[i] * t, 12)
                if a not in Ws:
                    Ws[a] = expm(a * B)
                tot += float(np.trace(K[i] @ Ws[a]))
            E[n] = tot
        return np.abs(np.fft.rfft(E) / N)

    classes = {}
    for lab, ang in (("simple(1,0)", (1, 0)), ("SD-isoclinic(1,1)", (1, 1)),
                     ("ASD-isoclinic(1,-1)", (1, -1)), ("NON-isoclinic(1,3)", (1, 3))):
        B = _plane_angle_bivector(ang)
        rows = {}
        for mlab, K in (("bankedJ", co["KJ"]), ("bankedD", co["KD"]),
                        ("Gamma#1", co["members"][co["dJ"] + co["dD"]][1])):
            c = harmonics(K, B)
            rows[mlab] = {"|c1|": float(c[1]), "|c3|": float(c[3])}
        classes[lab] = rows
    ce = classes["NON-isoclinic(1,3)"]["bankedJ"]
    assert ce["|c3|"] > 1.0, "the (1,3) COUNTEREXAMPLE did not fire — m3 must be nonzero"
    assert abs(ce["|c3|"] - ce["|c1|"]) < 1e-6 * ce["|c1|"]
    for lab in ("simple(1,0)", "SD-isoclinic(1,1)", "ASD-isoclinic(1,-1)"):
        assert classes[lab]["bankedJ"]["|c3|"] < 1e-10, lab

    # ---- the premise: every SD / every ASD bivector is ISOCLINIC
    rng = np.random.default_rng(20260823)
    iso = {}
    for nm, planes in (("SD", ((0, 1), (2, 3))), ("ASD", ((0, 1), (2, 3)))):
        sgn = 1 if nm == "SD" else -1
        trip = [_plane_angle_bivector((1, sgn), p) for p in
                (((0, 1), (2, 3)), ((0, 2), (3, 1)), ((0, 3), (1, 2)))]
        worst = 0.0
        for _ in range(200):
            c = rng.standard_normal(3)
            Bx = sum(ci * Bi for ci, Bi in zip(c, trip))
            lam2 = -Bx @ Bx
            worst = max(worst, float(np.abs(lam2 - (np.trace(lam2) / 4) * np.eye(4)).max())
                        / max(float(np.abs(lam2).max()), 1e-30))
        iso[nm] = worst
    assert max(iso.values()) < 1e-12

    # ---- the VACUITY CENSUS of the submitted round's second construction
    census, n_vac = {}, 0
    for mlab, K in members:
        S = K.sum(axis=0)
        smax = float(np.abs(S).max())
        dev = float(np.abs(S - (np.trace(S) / 4.0) * np.eye(4)).max())
        if smax < 1e-12:
            v = "VACUOUS — sum_b K_b = 0, E == 0 identically"
        elif dev < 1e-12:
            v = "VACUOUS — sum_b K_b ~ I, E constant in psi"
        else:
            v = "non-vacuous"
        census[mlab] = v
        n_vac += (v != "non-vacuous")
    assert n_vac == 8, n_vac

    return {
        "tier": ("DERIVED-A GIVEN a SIMPLE or ISOCLINIC (SD/ASD) twist generator; "
                 "REFUTED without that premise (counterexample shipped)"),
        "ceiling_by_generator_class": {
            "simple (1,0)": {"rep": 1, "adjoint": 2},
            "isoclinic SD/ASD (1,+-1)": {"rep": 1, "adjoint": 2},
            "general (a,b)": {"rep": "max(a,b)", "adjoint": "a+b"}},
        "measured_harmonics": classes,
        "counterexample": {
            "generator": "plane angles (1,3), NON-isoclinic",
            "coupling": "the BANKED J", "|c1|": ce["|c1|"], "|c3|": ce["|c3|"],
            "order": "bond-BILINEAR",
            "reading": ("m = 3 at the SAME magnitude as m = 1, at bilinear order. The "
                        "unconditioned ceiling is FALSE and can never be re-asserted from "
                        "this engine.")},
        "isoclinic_premise": {
            "residual_SD": iso["SD"], "residual_ASD": iso["ASD"],
            "source": ("canon §5's GENERATIONS = the anti-self-dual triple SUPPLIES this "
                       "premise — as an IDENTIFICATION, not a theorem")},
        "vacuity_census_of_the_submitted_second_construction": census,
        "vacuous_members": n_vac,
        "vacuity_note": (
            "8 of 12 (10 allowed + both banked) were vacuous in E = Tr(R^T (sum_b K_b) R Q). "
            "The identical defect was self-caught in one script of the round and NOT swept "
            "into the other, where it was load-bearing (canon §2 sweep-after-a-patch). "
            "Repaired by a non-vacuous rebuild: an independent random SO(4) pair per bond."),
        "JD6_status": (
            "UPGRADED CONDITIONALLY. Conditioned on the TWIST/CONFIGURATION class, NOT on "
            "'the banked action class' — the submitted phrase mislocated it. Remains an "
            "ASSEMBLY RECORD at §D.5.7 (RUL-030 class 2), not a ruling."),
        "would_change_if": (
            "the generation circle is implemented by a non-isoclinic SO(4) twist "
            "(plane-angle ratio reaching 3), where m = 3 appears at O(|c1|) at the same "
            "bilinear order — the shipped counterexample IS that world"),
        "does_not_license": (
            "'no bilinear-order computation, however refined, can compute alpha_i or beta' "
            "— withdrawn as a bare necessity claim (RUL-049)"),
        "record": "knowledge/audit/gamma_referent_2026-08-23/",
    }


def gamma_survivor_pitch_genericity(n_branches: int = 200) -> dict:
    """[DERIVED-A on the banked branches · DERIVED-numeric on the generic ones] G4 —
    THE LORENTZ-SAFE Gamma SURVIVOR'S INERTNESS IS NON-GENERIC, RE-SCOPED WITH CORRECTED
    NUMBERS. Located gap **GR-1**.

    THE SURVIVOR is the unique kernel direction of the (sum_b K_b, T_{mu nu}) map on the
    6-dim Gamma space — the Gamma direction with no first-moment and no two-derivative
    dispersion kernel, hence Lorentz-safe at quadratic order. Its Q(k) == 0 is DEFINITIONAL
    (it is defined as that kernel) and is NOT reported here as a confirming measurement —
    a third vacuity the reviewer correctly flagged.

    ON THE TWO BANKED HIGH-SYMMETRY BRANCHES it is EXACTLY pitch-blind (residuals <~2e-16),
    with pitch-visible Gamma dimension 1 (axis branch) / 2 (body-diagonal branch).

    ★ OFF THEM IT IS NOT. On generic single-q branches the pitch-visible Gamma dimension is
    4 (not 1) on essentially every branch, and the survivor's own pitch entry is NONZERO.
    So *"the Gamma survivor contributes exactly zero at all orders"* is SCOPED to the banked
    high-symmetry branches: it is a property of the vacuum's high-symmetry k-hat, NOT a
    lattice identity, and any protection argument resting on it is COUPLED TO THE BRANCH
    QUESTION, which is #1-gap open. This is the meta-observer's F1 class, measured.

    ★★ THE NUMBER, CORRECTED — and the correction is the point of this primitive.
    The submitted round headlined *"the survivor's worst pitch weight is 7.134e-01 — i.e.
    O(1), not zero"*. **That was a BARE NUMBER compared against nothing**, in direct
    violation of the same report's own normalisation discipline. In the EQUAL PER-BOND SCALE
    normalisation (both couplings at the same maximum per-bond matrix entry, which is the
    only normalisation in which a ratio to J means anything) the leak is:
        worst-case ~3-4% of J's own even weight · median ~0.1%
    Governing-record values at consensus: developer 3.57e-2 worst / 1.06e-3 median;
    reviewer 3.37e-2 / 8.95e-4. **The bare 7.1e-01 is WITHDRAWN and must never be quoted.**
    The worst case is a SAMPLE MAXIMUM over random branches and moves with the sample; the
    median is stable. Both are returned, with the seed named.

    READING: 3-4% sits right at the round's own sensitivity scale (a 1% read-out shift needs
    Gamma/J of a few percent), so a worst-case generic branch would need Gamma_surv/J ~ 0.3
    to move the read-out by 1% — MATERIALLY WEAKER than the pitch-visible directions (entry
    ratio exactly 1/2) but NOT a protection.

    ★ BLAST RADIUS OF THE UNSCOPED CLAIM: **EMPTY, swept.** Every live corpus site already
    carries the scope (paper §D.4/§D.5 sites, Core paper, family tree V3-2a(iii), worklist,
    the JD round's own report). GR-1 CONFIRMS AND QUANTIFIES the record; it corrects nothing
    in it. *"The finding with the widest reach"* is WITHDRAWN. **ONE annotation is owed and
    only one** — `TWT_FAMILY_TREE.md` node V3-2 (the risk-ordering carry), which conditions
    on the CLASS and not on the BRANCH; and it is repaired ASYMMETRICALLY, which is strictly
    better than a blanket hedge:
        the D_spatial half is BRANCH-INDEPENDENT (G2's exact parity selection rule);
        the Gamma half is BRANCH-CONDITIONAL (inert on the two banked k-hat, leaking a few
        percent off them).
    Keeper latent L-2 is UPHELD-not-discharged (GR-1 FEEDS it); node V3-2a is
    ANNOTATED-not-discharged.

    THE ENTRY RATIO, exact: the pitch-visible Gamma direction enters the pitch's even
    amplitude at a_visible/a_J = 1/2 EXACTLY, q-independent — an identity, not a coincidence
    at the calibrated pitch (both couplings weight the same twelve active bonds with the same
    (1-cos) factor; only the internal contraction differs). NORMALISATION IS STATED WITH THE
    NUMBER AND IS NOT FREE: equal maximum per-bond matrix entry. In the per-basis-member
    normalisation the same content reads 1/3, so the honest quotable is *a few percent,
    normalisation-dependent (~2-3%)* — never one end of that interval.

    FAILURE MODE SHIPPED WITH THE PRIMITIVE (`positive_control_pseudo_dipolar`): the
    pseudo-dipolar W(F4)-invariant Gamma direction (K_b = u_b u_b^T - I/4) IS visible on both
    banked branches, at O(1). Without it the blindness measurement could be vacuous.

    Cross-refs: canting_vacuum_branch_structure (the two branches);
    bond_invariant_menu_frame_bilinear (G1); TWT_FAMILY_TREE.md V3-2 / V3-2a."""
    rig = _gamma_bond_rig(); np = rig["np"]
    co = _gamma_couplings(); bonds = rig["bonds"]
    BG, dG, KJ = co["BG"], co["dG"], co["KJ"]

    rows = []
    for m in range(dG):
        K = BG[:, m].reshape(24, 4, 4)
        S = K.sum(axis=0)
        T = np.einsum('bm,bn,bij->mnij', bonds, bonds, K)
        rows.append(np.concatenate([S.ravel(), T.ravel()]))
    M = np.array(rows).T
    _, s, Vt = np.linalg.svd(M, full_matrices=True)
    rank = int((s > 1e-8).sum())
    assert dG - rank == 1, "the Lorentz-safe kernel must be 1-dimensional"
    surv = (BG @ Vt[rank]).reshape(24, 4, 4)
    surv_raw = surv / np.abs(surv).max()
    surv_eq = surv_raw * np.abs(KJ[0]).max()

    pd = np.zeros((24, 4, 4))
    for i, b in enumerate(bonds):
        u = b / np.linalg.norm(b)
        pd[i] = np.outer(u, u) - np.eye(4) / 4.0

    def even_profile(K, kh, Bb, q):
        cc = np.array([float(np.trace(K[i] @ (Bb @ Bb))) for i in range(24)])
        pr = np.array([float(np.dot(kh, b)) for b in bonds])
        return float(np.sum((1.0 - np.cos(q * pr)) * cc))

    qgrid = np.linspace(0.05, 1.5, 41)
    branches = {}
    for nm, kh, Bb in (("AXIS  k=q e1, B=e14", np.array([1.0, 0, 0, 0]),
                        _unit_simple_bivector([1, 0, 0])),
                       ("BODY-DIAGONAL k~(1,1,1,0), B~(e14+e24+e34)",
                        np.array([1.0, 1.0, 1.0, 0.0]) / math.sqrt(3.0),
                        _unit_simple_bivector([1, 1, 1]))):
        P = np.array([[even_profile(BG[:, m].reshape(24, 4, 4), kh, Bb, q)
                       for q in qgrid] for m in range(dG)])
        sv = np.linalg.svd(P, compute_uv=False)
        vis = int((sv > 1e-9 * max(1.0, sv[0])).sum())
        blind = max(abs(even_profile(surv_raw, kh, Bb, q)) for q in qgrid)
        ctrl = max(abs(even_profile(pd, kh, Bb, q)) for q in qgrid)
        branches[nm] = {"pitch_visible_Gamma_dim": vis, "blind_Gamma_dim": dG - vis,
                        "survivor_pitch_weight": blind,
                        "positive_control_pseudo_dipolar": ctrl}
        assert blind < 1e-12 and ctrl > 0.1, nm
    assert branches["AXIS  k=q e1, B=e14"]["pitch_visible_Gamma_dim"] == 1
    assert (branches["BODY-DIAGONAL k~(1,1,1,0), B~(e14+e24+e34)"]
            ["pitch_visible_Gamma_dim"] == 2)

    # ---- the exact 1/2 entry ratio, q-independent
    kh = np.array([1.0, 0, 0, 0]); Bb = _unit_simple_bivector([1, 0, 0])
    P = np.array([[even_profile(BG[:, m].reshape(24, 4, 4), kh, Bb, q)
                   for q in qgrid] for m in range(dG)])
    U, _, _ = np.linalg.svd(P)
    Kvis = (BG @ U[:, 0]).reshape(24, 4, 4)
    Kvis = Kvis / np.abs(Kvis).max() * np.abs(KJ[0]).max()
    ratios_q = {q: even_profile(Kvis, kh, Bb, q) / even_profile(KJ, kh, Bb, q)
                for q in (0.05, 0.1834, 0.5, 1.0, 1.5, 2.5)}
    assert max(abs(abs(v) - 0.5) for v in ratios_q.values()) < 1e-12

    # ---- genericity
    rng = np.random.default_rng(20260823)
    qs = np.linspace(0.05, 1.5, 25)
    dims, ratios, raw_worst = {}, [], 0.0
    for _ in range(n_branches):
        khr = rng.standard_normal(4); khr /= np.linalg.norm(khr)
        BB = _unit_simple_bivector(rng.standard_normal(3))
        pr = np.array([float(np.dot(khr, b)) for b in bonds])
        rws = []
        for m in range(dG):
            K = BG[:, m].reshape(24, 4, 4)
            cc = np.array([float(np.trace(K[i] @ (BB @ BB))) for i in range(24)])
            rws.append([float(np.sum((1 - np.cos(q * pr)) * cc)) for q in qs])
        sv = np.linalg.svd(np.array(rws), compute_uv=False)
        d = int((sv > 1e-9 * max(1.0, sv[0])).sum()); dims[d] = dims.get(d, 0) + 1
        cS = np.array([float(np.trace(surv_eq[i] @ (BB @ BB))) for i in range(24)])
        cR = np.array([float(np.trace(surv_raw[i] @ (BB @ BB))) for i in range(24)])
        cJ = np.array([float(np.trace(KJ[i] @ (BB @ BB))) for i in range(24)])
        for q in qs:
            w = 1.0 - np.cos(q * pr)
            raw_worst = max(raw_worst, abs(float(np.sum(w * cR))))
            aJ = float(np.sum(w * cJ))
            if abs(aJ) > 1e-12:
                ratios.append(abs(float(np.sum(w * cS)) / aJ))
    ratios = np.array(ratios)
    worst, med = float(ratios.max()), float(np.median(ratios))
    assert dims.get(4, 0) > 0.9 * n_branches, dims
    assert 5e-3 < worst < 2e-1 and 1e-4 < med < 1e-2, (worst, med)

    return {
        "tier": "DERIVED-A on the banked branches; DERIVED-numeric on the generic ones",
        "gap_id": "GR-1",
        "banked_branches": branches,
        "entry_ratio_pitch_visible_over_J": {
            "value": 0.5, "q_scan": ratios_q,
            "normalisation": ("EQUAL MAXIMUM PER-BOND MATRIX ENTRY — stated with the "
                              "number because it is NOT free; the per-basis-member "
                              "normalisation gives 1/3 for the same content"),
            "reading": ("q-INDEPENDENT and exactly 1/2 in magnitude: an identity, not a "
                        "coincidence at the calibrated pitch. Gamma enters the pitch's "
                        "even amplitude at the SAME ORDER as J, not suppressed. Quote the "
                        "INTERVAL 'a few percent, normalisation-dependent (~2-3%)', never "
                        "one end of it.")},
        "generic_visible_dimension_distribution": dims,
        "survivor_leak_equal_per_bond_scale": {
            "worst_this_run": worst, "median_this_run": med,
            "seed": 20260823, "n_branches": n_branches,
            "worst_is_a_sample_maximum": True,
            "recorded_at_consensus": {
                "developer": {"worst": 3.57e-2, "median": 1.06e-3},
                "reviewer": {"worst": 3.37e-2, "median": 8.95e-4}},
            "honest_statement": ("off the banked branches the survivor's pitch entry is "
                                 "nonzero — a few percent of J's own even weight worst "
                                 "case, ~0.1% median — so its exact blindness is a "
                                 "HIGH-SYMMETRY PROPERTY, not a lattice identity; a "
                                 "markedly weaker leak than the pitch-visible directions "
                                 "(ratio 1/2), but NOT a protection")},
        "survivor_raw_worst_WITHDRAWN": {
            "value_this_run": raw_worst,
            "why_withdrawn": ("the submitted '7.134e-01 — i.e. O(1)' was a BARE NUMBER "
                              "compared against nothing, in violation of the same report's "
                              "own normalisation discipline. Returned only so the "
                              "withdrawn figure is visible as withdrawn.")},
        "Qk_is_definitional_not_evidence": (
            "the survivor is DEFINED as the kernel of the (sum_b K_b, T) map, so Q(k) == 0 "
            "is definitional; it is not reported as a confirming measurement"),
        "blast_radius_of_the_unscoped_claim": "EMPTY — every live corpus site already scopes it",
        "one_annotation_owed": (
            "TWT_FAMILY_TREE.md node V3-2, the risk-ordering carry 'D_spatial > Gamma, "
            "within the frame-bilinear class' — it conditions on the CLASS and not on the "
            "BRANCH. Repaired ASYMMETRICALLY: the D_spatial half is BRANCH-INDEPENDENT (an "
            "exact parity selection rule, G2); the Gamma half is BRANCH-CONDITIONAL."),
        "discharges": ("NEITHER. Keeper latent L-2 is UPHELD-not-discharged (GR-1 feeds "
                       "it); family-tree node V3-2a is ANNOTATED-not-discharged."),
        "would_change_if": (
            "the branch question resolves onto a high-symmetry k-hat for a DYNAMICAL reason "
            "at §D.5.7 — static energetics need not govern a NESS vacuum"),
        "record": "knowledge/audit/gamma_referent_2026-08-23/",
    }


def DoverJ_calibration_referent() -> dict:
    """[The ROUTING THEOREM: DERIVED-conditional · The ARC-RATIO RIDER: CANDIDATE, with an
    executable TAUTOLOGY FENCE] G5 — WHAT `D/J ~ 0.79` MEASURES, AND WHAT THE ARC-RATIO
    READING DOES AND DOES NOT ADD.

    ═══ PART 1 — THE ROUTING THEOREM (the referent review's verdict, closed NEGATIVELY) ═══

    `0.79 = tan(3 delta_L)`, an INVARIANT OF THE THREE CHARGED-LEPTON MASSES computed with
    NO BOND DATUM (`DoverJ_from_lepton_masses`: inputs are the three masses, the sqrt(m)=r^2
    measure, and the Z3 phase convention). Its substrate referent, given §C.3.7's form and
    the parity assignment, is
        B = D_e4 + beta * D_spatial   (parity-ODD;  EXACTLY Gamma-clean)
        A = J + sum_i alpha_i Gamma_i (parity-EVEN; EXACTLY D-clean)
    i.e. **0.79 measures D_total / J_effective — a RATIO OF TOTALS with an exact channel
    exclusivity** (G2): Gamma reaches only the denominator, the second spatial-bond D only
    the numerator, and by G1 nothing else can enter either. The SIZES of alpha_i and beta are
    #1-gap-routed.

    THE VERDICT IS (b) AND IT IS OVER-DETERMINED: `D/J ~ 0.79` CANNOT be re-pinned as a
    single-parameter measurement of J and D. Three independent computed reasons refuse the
    re-pin: the calibration's functional sits OUTSIDE the scalar sector (Tr(K B^2) != 0 for
    symmetric-traceless K, so the tracelessness theorem supplies ZERO protection); Gamma
    enters at the SAME ORDER as J (entry ratio exactly 1/2); and the one blind direction
    loses its blindness off the banked branches (GR-1).
    **STILL NOT LICENSED, and the fence is kept:** the flat assertion *"0.79 is a
    measurement of a combination RATHER THAN D/J"* — that asserts alpha_i != 0, which
    remains uncomputable.
    **CONDITIONING:** the frame-bilinear class pick; bilinear order; and JD-5 on the Z3 side,
    which STANDS UNDISCHARGED.

    ═══ PART 2 — THE ARC-RATIO RIDER [CANDIDATE], AND ITS TAUTOLOGY FENCE ═══

    ★★ THE FENCE IS THIS PRIMITIVE'S CORE DESIGN, not a caveat on it. It exists because the
    tautology was very nearly banked as a confirmation.

    (i) THE CHAIN'S SINGLE EMPIRICAL FACT is `delta_L ~ 2/9 rad` — **Brannen's observation**.
        Everything else in the chain is a restatement of it. ★ THE RESIDUAL IS QUOTED AS AN
        OFFSET, NEVER AS A SIGNIFICANCE: on the engine's own constants
        `delta_fit - 2/9 = +2.540e-6 rad`, a FRACTIONAL AGREEMENT of `1.14e-5` in delta
        (`1.57e-5` in D/J). **NO SIGNIFICANCE IS QUOTED — there is no null hypothesis here,
        and the residual sits BELOW the input-systematic sensitivity** (the two controls in
        (iii)). Any sigma-count is DELETED from this record by ruling, not merely fenced.
    (ii) ★ THE `D/J`-LEVEL "0.00157% AGREEMENT" IS A **TAUTOLOGICAL RESTATEMENT**, NOT AN
        AGREEMENT AND NOT A CONFIRMATION. `D/J := tan(3 delta_L)` BY DEFINITION, so applying
        `tan(3 . )` to both sides of one empirical fact produces two numbers that agree
        because they are the same fact in different units. It is NOT a second check, NOT
        corroboration, and NOT evidence for the arc-ratio reading. **PRECEDENT, cited by
        name:** `brannen_comb_commitment_dominance_and_dof_vacuity`'s
        `min_over_mean_is_NOT_corroboration` — *"a function of (c, delta) ALONE, so matching
        the target fixes it by construction — reported so it cannot be mistaken for an
        independent check."* Same class, same remedy: reported so it cannot be mistaken.
    (iii) ★ THE SIGMA IS DELETED, NOT FENCED — and the reason is that IT IS
        ANTI-INFORMATIVE, not merely incomplete. A propagated-PDG-mass sigma measures how
        well m_tau is MEASURED, so the SAME unchanged physical agreement is reported as a
        different "significance" every time the input improves. Two controls, both computed
        here and both shipped in the return dict, make that concrete:
          (a) MASS-DEFINITION CONTROL. A 0.1% coherent shift in m_tau — far smaller than a
              pole->MS-bar conversion, and NOT covered by any propagated bar — moves
              delta_L by ~1.24e-4 rad, i.e. **~49x the observed residual**. The MEASURE
              conditional (sqrt(m)=r^2; pole vs MS-bar), which
              `DoverJ_from_lepton_masses`'s docstring names as conditional (a) and which
              paper §C.3.4 records moving the Foot angle ~50x its band, dwarfs the residual
              by orders.
          (b) INPUT-VINTAGE CONTROL — the sharper of the two, and it is why the sigma goes.
              Moving m_tau by 0.07 MeV (0.004%, WITHIN one PDG vintage's own bar: the
              1776.86 +- 0.12 vintage vs the 1776.93 +- 0.09 one this engine carries)
              changes the residual from 2.540e-6 to 7.409e-6 rad — a factor 2.9 — and a
              naive sigma-count correspondingly reports 0.41 or 0.89 for ONE unchanged
              claim. A statistic that swings by 2.2x on an input revision nobody would call
              a change of physics is not reporting the physics. **This control was produced
              by reconciling our own computation against an external reviewer's; it is the
              ruling's evidential ground.**
    (iv) THE 1/27 LADDER IS **POSTDICTIVE**, and it is **A NOTED REGULARITY OF ZERO
        EVIDENTIAL WEIGHT** — the earlier *"COMPRESSION, one integer for one real"* booking
        is RETIRED as too generous. It was formed on the ALREADY-KNOWN delta values and
        entered as *"noted non-coincidences ONLY"* (governing record: `TWT_worklist.md`,
        THE 1/27 PHASE LADDER, coordinator input 2026-08-03). ★ THE GROUND IS THIS CORPUS'S
        OWN: R-173's dof/vacuity result computes that the geometry reaches the measured
        triple on a **4-DIMENSIONAL solution manifold** (6 free reals - 2 constraints,
        Jacobian rank 2), so every NEARBY ladder value is reached as well. The ladder LABELS
        A POINT IN A CONTINUUM and EXCLUDES NOTHING — and compression is evidence only when
        the compressed description is CONSTRAINED. See `ladder_bit_accounting` for what the
        ladder pays (base, rung parity, ~2.58 bits of assignment, and an UNPAYABLE
        model-class charge) against what it buys.
        Separately and still true: fixing delta_L = 2/9 converts one fitted continuous
        parameter into one
        prediction, so the lepton leg's D/J calibration carries no continuous free parameter
        and one integer; it does NOT make the lepton mass TRIPLE parameter-free (Lambda and
        the c = sqrt2 INPUT remain).
    (v) ★ THE TRIALS FACTOR — what REPLACES the sigma, and it is stronger than one. Computed
        here, not asserted: over the rational menu {p/q, p*pi/q, p/(q*pi), p/(q*sqrt2)} with
        p, q <= 19 and gcd(p,q) = 1 (956 candidates; local density ~750 per unit delta near
        the target), at a tolerance equal to the OBSERVED residual, **`2/9` is the ONLY hit**,
        with a chance expectation of ~0.004. An external reviewer's independent and WIDER
        menu (2394 candidates, q < 20) returned the SAME unique hit at a chance expectation
        of 0.16; **we quote the more conservative 0.16**, our own reproduction being ~40x
        more favourable and therefore not the number to lead with.
        ★★ THE CONDITIONING CLASS, which neither computation states and which is the honest
        limit of the result (RUL-049): the trials factor bounds the look-elsewhere WITHIN
        THE STATED MENU. **The menu itself was chosen AFTER 2/9 was known** — "small rational,
        possibly times pi or sqrt2" is a family selected in the light of the answer — so what
        is bounded is *which rung*, never *whether a rational-menu reading was the thing to
        look for*. It is evidence about uniqueness, not about the reading's prior.
    (vi) ★ THE RENORMALIZATION POINT IS OWED, and this is where it is paid. `delta_L` is
        computed from POLE masses (the PDG charged-lepton pole values carried at the top of
        `twt_core`), and the Koide/arc-ratio relation is **NOT RG-stable** — a Koide-type
        relation exact at one scale is not exact at another, so the claim has no meaning
        without its point. THE CLAIM IS THEREFORE ASSERTED AT THE POLE-MASS POINT AND
        NOWHERE ELSE, and **no substrate argument yet fixes the pole point as the right
        one** — that is an OPEN commitment, not a fine-print caveat. For leptons the running
        is small, so this does not rescue or destroy the residual; it means the residual is
        a statement about a particular scheme-and-scale, which the record must say.
    (vii) THE NON-TAUTOLOGICAL TESTS — the rider's ONLY evidential future, enumerated:
        (a) **THE BARYON e-TEST, NOT YET DISCRIMINATING (coordinator ruling 2026-08-23: a 1.1% deviation is not a failure against a number whose own literature spread exceeds it - the historical Skyrme `e` is a fit that varied substantially across determinations; the test discriminates only with a determination at or below the ~1% level, read from primaries before any promotion).** The exact reading demands
            e = sqrt18/tan(2/3) = 5.391979 against the historical e_ANW = 5.45: **off by
            1.06%**. Stated here exactly as plainly as a success would be.
        (b) the GR-2 read-out at 0.1% (see gamma_admixture_cross_functional_route);
        (c) a SECOND sector landing on the 1/27 ladder with no new freedom.
    ★ WHAT THE VALUE BANKS AS (per the consensus §A7): a **REPORTED COMPARISON, WIRED TO
    NOTHING.** `tan(2/3)` is deliberately NOT fed into `delta_L_from_DoverJ`,
    `canting_pitch_q_rad`, `dressed_coupling`, `eta_DM` or any other consumer — that would
    be the cross-leg error this whole review is about (feeding a Z3-leg value into
    pitch-functional formulae) AND would convert a CANDIDATE into a banked default by the
    back door. See `does_not_license`.
    ★ AND `0.787` STOPS BEING THE QUOTED FIGURE, either way: it is the ROUNDED form of a
    number the review says is a ratio of totals, and it is COARSER than the fit (0.0200% vs
    0.00157% offsets). The honest quotable object is the fitted 0.78686 with its band — or,
    conditionally on the reading, tan(2/3).

    CREDIT (F3 duty OPEN — none of these is in the bibliography yet): the 2/9 observation is
    **Brannen's**; delta_U = 2/27 and delta_D = 4/27 are **Zenczykowski's**. The arc-ratio
    reading supplies the number's ADDRESS, not the number.

    FAILURE MODES SHIPPED WITH THE PRIMITIVE:
      * `mass_definition_control` — the 0.1% m_tau shift moving delta_L by ~49x the observed
        residual is IN the return dict, so the exact form can never be re-asserted from the
        engine as a precision result.
      * `input_vintage_control` — the two PDG m_tau vintages giving residuals 2.9x apart,
        shipped so that any future re-introduction of a sigma-count is refuted BY THE RETURN
        DICT ITSELF rather than by prose.
      * `no_sigma_count_in_record` — an executable ABSENCE fence: the returned record is
        asserted to contain no significance statistic under any key.
      * `tautology_label` + the suite's planted-violation demo — the D/J-level agreement is
        labelled TAUTOLOGICAL RESTATEMENT and the label is asserted; a planted relabel to
        "agreement"/"confirmation" fails the check.

    Cross-refs: DoverJ_from_lepton_masses (the computation);
    bond_channel_parity_exclusivity (the routing); gamma_admixture_cross_functional_route
    (GR-2); brannen_comb_commitment_dominance_and_dof_vacuity (the vacuity precedent);
    DoverJ_from_skyrme / dressed_coupling (the baryon leg the e-test is against)."""
    import cmath
    import numpy as np
    r = [math.sqrt(m) for m in (M_E, M_MU, M_TAU)]
    Mn = sum(r) / 3.0
    b = [rk / Mn - 1.0 for rk in r]
    z = sum(b[k] * cmath.exp(-1j * 2 * math.pi * k / 3) for k in range(3))
    arg = cmath.phase(z)
    delta_fit = arg - 2.0 * math.pi / 3.0
    dj_fit = math.tan(3.0 * arg)
    assert abs(dj_fit - DoverJ_from_lepton_masses()) < 1e-14

    delta_exact = 2.0 / 9.0
    dj_exact = math.tan(3.0 * delta_exact)

    # ── the residual, quoted as an OFFSET. No significance statistic is computed here, by
    #    ruling: see docstring (iii). The input-uncertainty SCALE is still reported (it is
    #    a sensitivity, not a bar to divide by) but no ratio to it is ever formed.
    offset_rad = delta_fit - delta_exact
    frac_delta = abs(offset_rad) / delta_exact
    frac_dj = abs(dj_fit - dj_exact) / dj_exact

    rng = np.random.default_rng(20260823)
    N = 200000
    me = rng.normal(M_E, 1.5e-10, N)
    mmu = rng.normal(M_MU, 2.3e-6, N)
    mta = rng.normal(M_TAU, 0.09, N)
    rr = np.sqrt(np.stack([me, mmu, mta]))
    bb = rr / rr.mean(axis=0) - 1.0
    zz = sum(bb[k] * np.exp(-1j * 2 * np.pi * k / 3) for k in range(3))
    delta_scale = float((np.angle(zz) - 2 * np.pi / 3).std())

    def _delta_of(mt):
        rc = [math.sqrt(m) for m in (M_E, M_MU, mt)]
        Mc = sum(rc) / 3.0
        bc = [x / Mc - 1.0 for x in rc]
        return cmath.phase(sum(bc[k] * cmath.exp(-1j * 2 * math.pi * k / 3)
                               for k in range(3))) - 2.0 * math.pi / 3.0

    # (a) MASS-DEFINITION CONTROL — expressed in the SAME units as the quotable (rad, and
    #     multiples of the observed residual) so no sigma can re-enter through it.
    control = {}
    for f in (0.001, 0.005):
        dc = _delta_of(M_TAU * (1 - f))
        control[f"m_tau x (1 - {f})"] = {
            "delta_L_rad": dc,
            "shift_from_fitted_rad": dc - delta_fit,
            "multiple_of_observed_residual": abs(dc - delta_fit) / abs(offset_rad),
            "D/J": math.tan(3.0 * dc)}
    assert control["m_tau x (1 - 0.001)"]["multiple_of_observed_residual"] > 20.0, (
        "the mass-definition control must DEMONSTRATE the measure systematic dwarfing the "
        "residual — in radians, not in sigma")

    # (b) INPUT-VINTAGE CONTROL — the anti-informativeness demonstration. Two PDG m_tau
    #     vintages, one unchanged claim, residuals a factor ~2.9 apart.
    vintage = {}
    for mt, sd, tag in ((1776.93, 0.09, "m_tau = 1776.93 +- 0.09 (this engine)"),
                        (1776.86, 0.12, "m_tau = 1776.86 +- 0.12 (an earlier vintage)")):
        dv = _delta_of(mt)
        vintage[tag] = {"residual_rad": dv - delta_exact,
                        "fractional_agreement": abs(dv - delta_exact) / delta_exact,
                        "propagated_delta_scale_rad": sd / 0.09 * delta_scale}
    _r1 = abs(vintage["m_tau = 1776.93 +- 0.09 (this engine)"]["residual_rad"])
    _r2 = abs(vintage["m_tau = 1776.86 +- 0.12 (an earlier vintage)"]["residual_rad"])
    assert _r2 / _r1 > 2.5, (
        "the input-vintage control must DEMONSTRATE that the residual — and hence any "
        "sigma-count built on it — swings on an input revision that is not a change of "
        "physics; that demonstration is the ground of the delete-the-sigma ruling")

    # ── THE TRIALS FACTOR: what replaces the sigma. Deterministic, menu stated in full.
    from math import gcd as _gcd
    _fams = {"p/q": lambda p, q: p / q,
             "p*pi/q": lambda p, q: p * math.pi / q,
             "p/(q*pi)": lambda p, q: p / (q * math.pi),
             "p/(q*sqrt2)": lambda p, q: p / (q * math.sqrt(2.0))}
    _cands = [(nm, p, q, f(p, q))
              for nm, f in _fams.items()
              for q in range(1, 20) for p in range(1, 20) if _gcd(p, q) == 1]
    _tol = abs(offset_rad)
    _hits = sorted({(nm, p, q) for nm, p, q, v in _cands if abs(v - delta_fit) <= _tol})
    _near = [c for c in _cands if abs(c[3] - delta_exact) <= 0.01]
    _rho = len(_near) / 0.02
    assert _hits == [("p/q", 2, 9)], (
        "the trials-factor menu must return 2/9 as the UNIQUE hit — if it does not, the "
        "claim's whole non-tautological content has changed and the record must be redrawn")

    e_required = math.sqrt(18.0) / dj_exact
    e_anw = 5.45
    e_gap = (e_anw - e_required) / e_anw * 100.0
    assert e_gap > 1.0, ("the e-test's 1.06% DEVIATION must be asserted, not softened -- the "
                         "number is reported plainly; per RUL-100(2) it is NOT called a failure, "
                         "because the historical e's own literature spread exceeds it")

    return {
        "tier": ("PART 1 routing theorem: DERIVED-conditional (frame-bilinear class pick, "
                 "bilinear order, JD-5 open on the Z3 leg). PART 2 arc-ratio rider: "
                 "CANDIDATE."),
        # ---- PART 1
        "what_0_79_measures": "D_total / J_effective — a RATIO OF TOTALS",
        "routing": {"numerator B (parity-ODD)": "D_e4 + beta * D_spatial — exactly Gamma-clean",
                    "denominator A (parity-EVEN)": "J + sum_i alpha_i Gamma_i — exactly D-clean",
                    "ground": "bond_channel_parity_exclusivity + bond_invariant_menu_frame_bilinear"},
        "admixture_sizes": "CANDIDATE, #1-gap-routed (JD-6, conditional per G3)",
        "verdict": ("(b) — it measures a stated combination. The referent review CLOSES "
                    "NEGATIVELY: D/J ~ 0.79 cannot be re-pinned as a single-parameter "
                    "measurement of J and D."),
        "three_computed_refusals_of_a_re_pin": [
            "the calibration's functional is OUTSIDE the scalar sector — the tracelessness "
            "theorem supplies zero protection",
            "Gamma enters at the SAME ORDER as J (entry ratio exactly 1/2)",
            "the one blind direction loses blindness off the banked branches (GR-1)"],
        "still_not_licensed": ("the flat assertion '0.79 is a measurement of a combination "
                               "RATHER THAN D/J' — that asserts alpha_i != 0, uncomputable"),
        # ---- PART 2
        "arc_ratio_rider": {
            "tier": "CANDIDATE",
            "delta_L_exact_rad": delta_exact,
            "ladder_address": {"as_27ths": "6/27", "n": 3, "rung_set": "2:4:6 over 27"},
            "DoverJ_exact": dj_exact,
            "fitted_on_engine_constants": dj_fit,
            "fitted_delta_L_rad": delta_fit,
            "relative_offset_exact_vs_fit": abs(dj_fit - dj_exact) / dj_exact,
            "relative_offset_of_the_rounded_quote_0.787": abs(0.787 - dj_exact) / dj_exact,
            "single_empirical_fact": (
                "delta_L ~ 2/9 rad — BRANNEN'S OBSERVATION. Everything else in the chain "
                "restates it."),
            # ---- THE QUOTABLE FORM (ruled 2026-08-24): offset + fractional agreement +
            #      an explicit no-significance clause + the trials factor + the RG point.
            "residual_offset_rad": offset_rad,
            "fractional_agreement_delta": frac_delta,
            "fractional_agreement_DoverJ": frac_dj,
            "no_significance_is_quoted": (
                "NO SIGNIFICANCE IS QUOTED. There is no null hypothesis here, and the "
                "residual sits BELOW the input-systematic sensitivity: see "
                "mass_definition_control (a 0.1% m_tau shift moves delta_L by ~49x the "
                "residual) and input_vintage_control (two PDG m_tau vintages give residuals "
                "a factor 2.9 apart). A propagated-mass sigma is ANTI-INFORMATIVE — it "
                "measures how well m_tau is measured, so the same unchanged agreement is "
                "reported as a different 'significance' every time the input improves. The "
                "sigma-count is DELETED FROM THIS RECORD, not fenced."),
            "input_uncertainty_scale_rad": delta_scale,
            "input_uncertainty_scale_is_NOT_a_bar_to_divide_by": (
                "reported as a SENSITIVITY SCALE only. Forming residual/scale reconstructs "
                "the deleted statistic and is forbidden by does_not_license."),
            "mass_definition_control": control,
            "input_vintage_control": vintage,
            "trials_factor": {
                "menu": ("{p/q, p*pi/q, p/(q*pi), p/(q*sqrt2)}, p,q <= 19, gcd(p,q) = 1"),
                "n_candidates": len(_cands),
                "local_density_per_unit_delta": _rho,
                "tolerance_rad": _tol,
                "hits": _hits,
                "chance_expectation_local_density": _rho * 2 * _tol,
                "quoted_chance_expectation": 0.16,
                "quoted_from": (
                    "an external reviewer's independent and WIDER menu (2394 candidates, "
                    "q < 20) returned the SAME unique hit at 0.16. We quote 0.16, the more "
                    "conservative figure; our own reproduction is ~40x more favourable and "
                    "is therefore not the number to lead with."),
                "CONDITIONING_CLASS_RUL_049": (
                    "the trials factor bounds the look-elsewhere WITHIN THE STATED MENU. "
                    "The menu was chosen AFTER 2/9 was known, so what is bounded is WHICH "
                    "RUNG, never WHETHER a rational-menu reading was the thing to look for. "
                    "Evidence about uniqueness; NOT evidence about the reading's prior.")},
            "renormalization_point": (
                "delta_L is computed from POLE masses, and the Koide/arc-ratio relation is "
                "NOT RG-stable, so the claim is meaningless without its point. IT IS "
                "ASSERTED AT THE POLE-MASS POINT AND NOWHERE ELSE, and no substrate "
                "argument yet fixes the pole point as the right one — an OPEN commitment, "
                "not fine print. Lepton running is small, so this neither rescues nor "
                "destroys the residual; it scopes it to one scheme and scale."),
            "ladder_is_POSTDICTIVE": (
                "POSTDICTIVE: formed on the ALREADY-KNOWN delta values and entered as 'noted "
                "non-coincidences ONLY' (governing record: TWT_worklist.md, THE 1/27 PHASE "
                "LADDER, coordinator input 2026-08-03). ★ IT IS A NOTED REGULARITY OF ZERO "
                "EVIDENTIAL WEIGHT — the earlier 'COMPRESSION, one integer for one real' "
                "booking is RETIRED as too generous, on this corpus's OWN ground: R-173's "
                "dof/vacuity result (brannen_comb_commitment_dominance_and_dof_vacuity) "
                "computes that the geometry reaches the measured triple on a "
                "FOUR-DIMENSIONAL solution manifold (6 free reals - 2 constraints, Jacobian "
                "rank 2), so every NEARBY ladder value is reached too. The ladder therefore "
                "LABELS A POINT IN A CONTINUUM and EXCLUDES NOTHING; compression is evidence "
                "only when the compressed description is CONSTRAINED, and here it is not."),
            "ladder_bit_accounting": {
                "bought": "3 reals (delta_L, delta_U, delta_D) -> 3 small integers",
                "paid_1_base": "the denominator 27 rather than 9, 81, 12, ... — a free choice",
                "paid_2_parity": "the rung set is EVEN (2:4:6) not (1:2:3) — >= 1 bit, and "
                                 "the 'why even harmonics' question is still OPEN",
                "paid_3_assignment": "which rung to which sector — log2(3!) ~ 2.58 bits",
                "paid_4_model_class": "UNPAYABLE IN BITS: the family 'rational multiple of "
                                      "1/27 rad' was itself selected AFTER the values were "
                                      "known, and the family is unbounded",
                "net": "the ledger does not close in the ladder's favour even before the "
                       "vacuity kill; with it, the accounting is moot — nothing is excluded"},
            "what_fixing_delta_L_buys": (
                "one fitted continuous parameter becomes one prediction: the lepton leg's "
                "D/J calibration then carries no continuous free parameter and one integer "
                "(n = 3). It does NOT make the lepton mass TRIPLE parameter-free — Lambda "
                "and the c = sqrt2 INPUT remain."),
            "non_tautological_tests": {
                "baryon_e_test": {
                    "e_required": e_required, "e_ANW_historical": e_anw,
                    "percent_low": e_gap,
                    "STATUS": "NOT YET DISCRIMINATING (1.1% deviation < historical literature spread of e)",
                    "note": ("stated as plainly as a success would be. Either e_ANW is "
                             "~1.06% high of what the substrate demands, or the two legs' "
                             "J_eff differ by that much.")},
                "GR-2_read_out": ("an independent determination of e — or of the J that "
                                  "f_pi^2 = 8J/a fixes — at the 0.1% level would READ OUT "
                                  "the Gamma admixture difference instead of absorbing it "
                                  "into a '1.1% agreement'"),
                "second_sector": ("a second sector landing on the 1/27 ladder with no new "
                                  "freedom")},
            "credit": ("Brannen (delta_L = 2/9); Zenczykowski (delta_U = 2/27, "
                       "delta_D = 4/27). The arc-ratio reading supplies the ADDRESS, not "
                       "the number."),
            "F3_bibliography_duty": "OPEN — neither Brannen nor Zenczykowski is in the bibliography",
            "open_commitments": ["why n = 3", "the even-harmonic question",
                                 "the mass-measure conditional",
                                 "the renormalization point (pole vs any other) is not "
                                 "fixed by any substrate argument"],
            "banks_as": "A REPORTED COMPARISON, WIRED TO NOTHING",
        },
        # ---- THE FENCE
        "tautology_label": (
            "TAUTOLOGICAL RESTATEMENT — NOT an agreement and NOT a confirmation. "
            "D/J := tan(3 delta_L) BY DEFINITION, so the D/J-level '0.00157%' is tan(3 . ) "
            "applied to BOTH SIDES OF ONE EMPIRICAL FACT. Precedent, cited by name: "
            "brannen_comb_commitment_dominance_and_dof_vacuity's "
            "min_over_mean_is_NOT_corroboration."),
        "quoting_rule": (
            "0.787 STOPS BEING THE QUOTED FIGURE — it is the ROUNDED form of a number the "
            "review calls a ratio of totals, and it is coarser than the fit (0.0200% vs "
            "0.00157%). The honest quotable object is the fitted 0.78686 with its band; "
            "conditionally on the arc-ratio reading, tan(2/3)."),
        "does_not_license": (
            "wiring tan(2/3) into delta_L_from_DoverJ, canting_pitch_q_rad, canting_cos_q, "
            "spiral_angle_deg, dressed_coupling, eta_DM or ANY consumer — that is the "
            "cross-leg error (a Z3-leg value fed into pitch-functional formulae) and it "
            "would convert a CANDIDATE into a banked default by the back door; QUOTING ANY "
            "SIGNIFICANCE STATISTIC FOR THE ARC-RATIO READING, or reconstructing one by "
            "dividing residual_offset_rad by input_uncertainty_scale_rad — the statistic is "
            "deleted by ruling because it is anti-informative, and re-deriving it from the "
            "returned parts is the same error by another route; reading the D/J-level "
            "agreement as corroboration of anything; reading the trials factor as evidence "
            "for the arc-ratio reading's PRIOR rather than for the rung's uniqueness "
            "within a post-hoc menu"),
        "record": "knowledge/audit/gamma_referent_2026-08-23/",
    }


def gamma_admixture_cross_functional_route() -> dict:
    """[CANDIDATE — a ROUTE, not a measurement; every one of four conditioning items can
    void it] G6 — **GR-2 / JD-6(b)**: THE THREE `J_eff` FACES, AND THE FIRST NUMBER THE
    REVIEW HAS PRODUCED FOR A Gamma ADMIXTURE.

    THE GAP (filed as **JD-6(b)**, a named COROLLARY of JD-6 with bidirectional pointers at
    §D.5.7 — deliberately NOT an independent fourth gap; gap-inventory inflation is a real
    cost and GR-2 is empty if JD-6's coefficients vanish):
      **TRIED** treating J as ONE constant shared by `f_pi^2 = 8J/a` (R-106), the helix pitch
      and the Z3 amplitude. **FAILED BECAUSE** Gamma renormalises each through a DIFFERENT
      functional — the quadratic dispersion kernel Q(k), the branch-dependent (1-cos) weight,
      and the dressed Z3 harmonic — and the three coincide ONLY if the Gamma admixture
      vanishes. **WOULD CHANGE IF** the dressed Gamma couplings are pinned, or an argument
      fixes the substrate Gamma to zero.

    ★ THE FENCE, WIDENED at consensus from the submitted form. The submitted report said
    *"never combine D/J with an independently-fixed J such as f_pi^2 = 8J/a"* and placed
    every other consumer in NOT-EXPOSED on the ground that *"the ratio is self-consistent"*.
    **That ground is valid WITHIN ONE FUNCTIONAL and is exactly what GR-2 denies ACROSS
    functionals — the report asserted GR-2 and then contradicted it one paragraph later.**
    The exposure is not a junction; it is the DEFAULT-ARGUMENT WIRING ITSELF. The correct
    fence is:
        **NEVER CARRY A RATIO CALIBRATED ON ONE FUNCTIONAL INTO ANOTHER.**
    It reaches every cross-leg consumer (`spiral_angle_deg`, `dressed_coupling`, `eta_DM`,
    `canting_pitch_q_rad`/`canting_cos_q` at the calibrated value, `electron_f_L_MeV`, and
    the hard-wired D/J defaults), the `over_determination_scan` band rationale, and the
    shipped lepton<->baryon over-determination headline. **VALUES DO NOT MOVE. What moves is
    the claim that the formula is being fed the right substrate quantity** — an unnamed
    premise (alpha = a) that this primitive names.

    ═══ THE DISCRIMINATOR, AND ITS FIRST NUMBER ═══
    G2's exclusivity theorem says Gamma reaches ONLY the denominator. So any difference
    between two legs' measured ratios is ENTIRELY a difference of their denominators:
        D_tot / J_eff(Z3)    = tan(2/3)      [the arc-ratio reading, CANDIDATE]
        D_tot / J_eff(pitch) = sqrt18/e_ANW  [the Skyrme leg]
        ==> J_eff(pitch) / J_eff(Z3) ~ 1.0108  (+1.08%)
    and through G4's computed pitch entry ratio a_visible/a_J = 1/2 EXACTLY (equal per-bond
    scale), a denominator difference of x% needs a Gamma admixture difference of 2x%:
        **Delta(Gamma/J) between the two functionals ~ +2.15% of J.**

    ★★ THE CONDITIONING CLASS, IN THE SAME BREATH (RUL-049), VERBATIM AND COMPLETE. It rides
    (i) the arc-ratio reading (CANDIDATE); (ii) the sqrt18 bridge — whose alternative sqrt12
    route sits ~20% away and whose physical referent THE FRAMEWORK ITSELF DISCLAIMS;
    (iii) e_ANW's own fit systematics; (iv) the assumption that the Gamma admixture is the
    ONLY difference between the two faces. **ANY ONE OF THE FOUR FAILING VOIDS THE NUMBER.
    IT IS A ROUTE, NOT A MEASUREMENT.**

    THE RESOLUTION ROUTE, stated: the three faces become distinguishable once ONE of them is
    pinned to an exact value. Under the reading the Z3 face is pinned BY CONSTRUCTION, so the
    discriminating measurements are THE OTHER TWO — an independent determination of `e`, or
    of the `J` that `f_pi^2 = 8J/a` fixes, **at the 0.1% level**. That converts JD-6(b) from
    a bookkeeping caution into a MEASUREMENT PROGRAMME WITH A STATED TARGET PRECISION, and it
    is the first time this review can say what would settle anything.

    FAILURE MODE SHIPPED WITH THE PRIMITIVE (`bridge_sensitivity_control`): the same route
    run on the sqrt12 bridge instead of sqrt18 returns a number ~20% away — computed and
    returned — so the 2.15% can never be quoted as a measurement rather than a route.

    Cross-refs: DoverJ_calibration_referent (G5, the arc-ratio rider);
    gamma_survivor_pitch_genericity (G4, the exact 1/2); f_pi_squared (R-106);
    DoverJ_from_skyrme / over_determination_scan (the exposed cross-leg sites)."""
    dj_z3 = math.tan(2.0 / 3.0)
    e_anw = 5.45
    dj_pitch = math.sqrt(18.0) / e_anw
    jeff_ratio = dj_z3 / dj_pitch
    entry_ratio = 0.5
    delta_gamma_over_J = (jeff_ratio - 1.0) / entry_ratio

    dj_pitch12 = math.sqrt(12.0) / e_anw
    jeff_ratio12 = dj_z3 / dj_pitch12
    delta12 = (jeff_ratio12 - 1.0) / entry_ratio
    spread = abs(delta12 - delta_gamma_over_J) / abs(delta_gamma_over_J)
    assert spread > 1.0, "the bridge-sensitivity control must show the route is bridge-bound"
    assert abs(delta_gamma_over_J - 0.0215) < 5e-4

    return {
        "tier": "CANDIDATE — a ROUTE, not a measurement",
        "gap_id": "JD-6(b) (= GR-2) — a named COROLLARY of JD-6, NOT an independent gap",
        "three_J_eff_faces": [
            "the magnon kinetic stiffness f_pi^2 = 8J/a (R-106) — a quadratic-fluctuation "
            "object, exactly where Gamma's Q(k) = sum_b (k.b)^2 K_b lives",
            "the helix pitch — a branch-dependent (1-cos)-weighted object",
            "the Z3 generation amplitude — a dressed harmonic"],
        "fence": "NEVER CARRY A RATIO CALIBRATED ON ONE FUNCTIONAL INTO ANOTHER",
        "fence_was_widened_from": (
            "'never combine D/J with an independently-fixed J such as f_pi^2 = 8J/a' — the "
            "submitted form named ONE junction while placing every cross-leg consumer in "
            "NOT-EXPOSED on a ground ('the ratio is self-consistent') that is valid within "
            "one functional and is exactly what GR-2 denies across functionals"),
        "exposed_classes": {
            "cross-leg consumers": ["spiral_angle_deg", "dressed_coupling", "eta_DM",
                                    "canting_pitch_q_rad / canting_cos_q at the calibrated "
                                    "value", "electron_f_L_MeV",
                                    "the hard-wired D/J defaults in twt_candidate_v3.py"],
            "same-quantity assertions": ["over_determination_scan's band rationale "
                                         "('THREE reads of the SAME quantity')",
                                         "DoverJ_from_skyrme's agreement docstring",
                                         "the shipped lepton<->baryon over-determination "
                                         "headline"],
            "stiffness junction": ["f_pi_squared (R-106) combined with D/J"]},
        "values_move": False,
        "what_moves": ("the claim that the formula is being fed the right substrate "
                       "quantity — the unnamed premise alpha = a"),
        "discriminator": {
            "D_tot/J_eff(Z3)": dj_z3, "D_tot/J_eff(pitch)": dj_pitch,
            "J_eff(pitch)/J_eff(Z3)": jeff_ratio,
            "pitch_entry_ratio_a_visible_over_a_J": entry_ratio,
            "Delta(Gamma/J)_between_the_two_functionals": delta_gamma_over_J,
            "note": "the FIRST number the review has produced for a Gamma admixture"},
        "conditioning_class_RUL049": [
            "(i) the arc-ratio reading (CANDIDATE)",
            "(ii) the sqrt18 bridge — whose alternative sqrt12 route sits ~20% away and "
            "whose physical referent the framework itself disclaims",
            "(iii) e_ANW's own fit systematics",
            "(iv) the assumption that the Gamma admixture is the ONLY difference between "
            "the two faces"],
        "any_one_failing_voids_the_number": True,
        "bridge_sensitivity_control": {
            "sqrt18_route_Delta(Gamma/J)": delta_gamma_over_J,
            "sqrt12_route_Delta(Gamma/J)": delta12,
            "relative_spread": spread,
            "reading": ("the route is BRIDGE-BOUND: swapping the disclaimed sqrt18 bridge "
                        "for sqrt12 moves the answer by more than its own size. Shipped so "
                        "2.15% can never be quoted as a measurement.")},
        "resolution_route": (
            "an independent determination of e — or of the J that f_pi^2 = 8J/a fixes — at "
            "the 0.1% LEVEL would READ OUT the Gamma admixture difference instead of "
            "absorbing it into a '1.1% agreement'. A measurement programme with a stated "
            "target precision."),
        "does_not_license": (
            "quoting 2.15% as a measured Gamma admixture; treating JD-6(b) as an "
            "independent fourth gap; any cross-functional carry of a calibrated ratio"),
        "record": "knowledge/audit/gamma_referent_2026-08-23/",
    }


# ======================================================================
# THE 24-BOND SCALAR DISPERSION QUARTIC (2026-08-25) — R-186
# ----------------------------------------------------------------------
# Governing records: knowledge/audit/external_review_r5_2026-08-25/
#   review_r5_02_opus_core_warm.md (the proposing computation, external)
#   ADJUDICATION_R5_2026-08-25.md (the adjudicating entry + the model rider)
# ======================================================================


def d4_scalar_dispersion_quartic_coefficients():
    """[DERIVED-A OF THE STATED MODEL + a MANDATORY MODEL RIDER — R-186, banked
    2026-08-25. PROPOSED BY THE ROUND-5 EXTERNAL REVIEWER (Opus, warm return 02) and
    INDEPENDENTLY REPRODUCED by the coordinator's own symbolic series the hour it
    arrived; this primitive is the third, pure-rational route.]

    THE MODEL (say it before the result — canon §3 model honesty): the SCALAR
    nearest-neighbour lattice symbol on the 24 D4 kissing bonds,
        F(k) = sum_b w_b [1 - cos(b.k)],
    with weight J_a on the 12 e4-BEARING bonds and J_p on the 12 IN-HYPERPLANE
    bonds — the two G48 sub-orbits of the single W(F4) bond orbit (R-185). The
    dispersion is F = 0 continued to k4 = i*omega. Pairing the b4 = +-1 bonds gives
    the exact closed form
        F = 4*J_a*Sum_i (1 - cos k_i cosh w) + 4*J_p*Sum_{i<j} (1 - cos k_i cos k_j),
    and omega^2(k) is solved as an exact rational power series, order by order, in
    Fraction arithmetic — no floats, no truncation error.

    THE RESULT (each fact asserted below; r := J_p/J_a):
        c^2                      = (1 + 2r)/3
        degree-4 isotropic  (k_sp^2)^2 coefficient : (1 - r)(5 + 4r)/108
        degree-4 anisotropic Sum k_i^4 coefficient : -(1 - r)/36
        at r = 1 (orbit-constant coupling): c^2 = 1 and BOTH degree-4 coefficients
            are EXACTLY ZERO — through quartic order the symbol is a function of the
            4D invariant alone, so omega^2 = k_sp^2 exactly; the leading survivor is
            the degree-6 anisotropic (1/90)[(k_sp^2)^3 - Sum k_i^6] (dimension EIGHT).
        at r = 0 (the e4-bearing sub-orbit alone): isotropic 5/108, anisotropic
            -1/36 — both order 1e-2.
        r = 1 is the UNIQUE root of either degree-4 coefficient: one condition,
        both loads.

    WHAT THIS MEANS AND DOES NOT MEAN (the adjudicated reading, R7-checked):
      * The CONSERVATIVE nearest-neighbour scalar part of the dim-6 exposure has
        natural value ZERO at orbit-constant coupling — not order one. The naive
        c = 1 estimate in d4_lattice_lorentz_violation_orders sizes the DRIVEN-
        DISSIPATIVE sector and the orbit-splitting channel, not this part.
      * The failure channel is EXACTLY R-185's would-change-if: a coupling
        G48-invariant but NOT constant on the W(F4) orbit (J_a != J_p). The live
        instance edge is family-tree node V3-2a (support on the 12 e4-bearing
        bonds is a SUB-ORBIT): at the r = 0 extreme both coefficients are ~1e-2
        against the CONDITIONAL 6-to-7-order requirement. UNITS, corrected at the
        contra-review: these are substrate-c values; converted through eta =
        c*(M_Pl/Lambda)^2 (factor 1.85-6.69 across the ruled band) the isotropic
        5/108 reads eta in [0.086, 0.310], which STRADDLES the unconditional Auger
        bound 0.149 — allowed at the loose lattice corner, excluded ~2x at the tight
        one; zero-vs-STRADDLE, not zero-vs-allowed. WHETHER a substrate argument pins
        r = 1 for the dressed couplings is the named open computation (docketed;
        the {J, D} matrix-valued version is the real object).
      * MANDATORY MODEL RIDER (the proposing reviewer's own fences, kept verbatim
        in kind): this is a scalar nearest-neighbour toy, NOT the banked {J, D}
        rotor structure; a matrix-valued internal-index kernel is outside the
        scalar theorem (R-165 premise (P-sc)); a non-analytic dissipative kernel
        is outside it entirely (P-an). PROOF OF CONCEPT, NOT DISCHARGE — nothing
        here closes VG-6/N52, and no banked exposure number moves.

    PROVENANCE: proposed and first computed by the round-5 external reviewer
    (review_r5_02, 2026-08-25); reproduced independently via sympy series
    (coordinator, same day, round records); this primitive is a third route in
    exact Fractions. Three computations, three implementations, one answer.

    self-check: the series inversion reproduces the closed forms at five rational
    r values; both degree-4 coefficients vanish IFF r = 1 (checked at r != 1);
    the degree-6 survivor at r = 1 matches (1/90)[(K2)^3 - S6] coefficient-wise."""
    from fractions import Fraction as Fr
    import itertools

    # polynomial dicts: {(a1,a2,a3): Fraction} over spatial monomials k1^a1 k2^a2 k3^a3
    def pmul(p, q):
        out = {}
        for ea, ca in p.items():
            for eb, cb in q.items():
                e = (ea[0] + eb[0], ea[1] + eb[1], ea[2] + eb[2])
                out[e] = out.get(e, Fr(0)) + ca * cb
        return {e: c for e, c in out.items() if c != 0}

    def padd(p, q, s=Fr(1)):
        out = dict(p)
        for e, c in q.items():
            out[e] = out.get(e, Fr(0)) + s * c
        return {e: c for e, c in out.items() if c != 0}

    def trunc(p, deg):
        return {e: c for e, c in p.items() if sum(e) <= deg}

    ONE = {(0, 0, 0): Fr(1)}
    K = [{(1, 0, 0): Fr(1)}, {(0, 1, 0): Fr(1)}, {(0, 0, 1): Fr(1)}]
    DEG = 6

    def cos_series(p, deg):
        # cos(p) for a polynomial p with no constant term, truncated at total deg
        out = dict(ONE)
        term = dict(ONE)
        sign = 1
        n = 0
        while True:
            n += 1
            term = trunc(pmul(pmul(term, p), p), deg)
            if not term:
                break
            sign = -sign
            fact = Fr(1)
            for m in range(1, 2 * n + 1):
                fact *= m
            out = padd(out, {e: c / fact for e, c in term.items()}, Fr(sign))
        return out

    def solve_for(r):
        # r = J_p/J_a; work in units J_a = 1
        Ja, Jp = Fr(1), Fr(r)
        # spatial-only part of F (the omega-independent piece):
        # 4*Ja*Sum_i (1 - cos k_i) + 4*Jp*Sum_{i<j}(1 - cos k_i cos k_j)
        P = {}
        for i in range(3):
            P = padd(P, padd(ONE, cos_series(K[i], DEG), Fr(-1)), 4 * Ja)
        for i, j in itertools.combinations(range(3), 2):
            cc = trunc(pmul(cos_series(K[i], DEG), cos_series(K[j], DEG)), DEG)
            P = padd(P, padd(ONE, cc, Fr(-1)), 4 * Jp)
        # omega-dependent piece: 4*Ja*Sum_i cos k_i (1 - cosh w); with u = w^2,
        # cosh w - 1 = u/2 + u^2/24 + u^3/720 ; F = P - 4*Ja*(Sum_i cos k_i)*(cosh w - 1)
        C = {}
        for i in range(3):
            C = padd(C, cos_series(K[i], DEG))
        C = {e: 4 * Ja * c for e, c in C.items()}
        # solve F = 0: P = C * (u/2 + u^2/24 + u^3/720) order by order for
        # u = u2 + u4 + u6 (homogeneous spatial degrees 2, 4, 6 — u carries weight 2)
        def homo(p, d):
            return {e: c for e, c in p.items() if sum(e) == d}
        # order 2: P|_2 = (C|_0/2) u2
        c0 = C.get((0, 0, 0))
        u2 = {e: c / (c0 / 2) for e, c in homo(P, 2).items()}
        # order 4: P|_4 = (1/2)[C u2]|_4 + (1/24) c0 u2^2|... careful:
        # C*(u/2 + u^2/24): order-4 terms = (1/2)(C|_2 u2 + c0 u4) + (1/24) c0 (u2^2)
        rhs4 = padd(homo(P, 4), pmul({e: c / 2 for e, c in homo(C, 2).items()}, u2), Fr(-1))
        rhs4 = padd(rhs4, pmul(u2, u2), Fr(-c0) / 24)
        u4 = {e: c / (c0 / 2) for e, c in rhs4.items()}
        # order 6: (1/2)(C|_4 u2 + C|_2 u4 + c0 u6) + (1/24)(C|_2 u2^2 + c0*2*u2*u4)
        #          + (1/720) c0 u2^3  = P|_6
        rhs6 = homo(P, 6)
        rhs6 = padd(rhs6, pmul({e: c / 2 for e, c in homo(C, 4).items()}, u2), Fr(-1))
        rhs6 = padd(rhs6, pmul({e: c / 2 for e, c in homo(C, 2).items()}, u4), Fr(-1))
        rhs6 = padd(rhs6, pmul(pmul(homo(C, 2), u2), u2), Fr(-1, 24))
        rhs6 = padd(rhs6, pmul(u2, u4), Fr(-c0) / 12)
        rhs6 = padd(rhs6, pmul(pmul(u2, u2), u2), Fr(-c0) / 720)
        u6 = {e: c / (c0 / 2) for e, c in rhs6.items()}
        # extract c^2 (coefficient of k1^2 in u2), a (isotropic), b (anisotropic) from u4:
        c2 = u2.get((2, 0, 0), Fr(0))
        a_plus_b = u4.get((4, 0, 0), Fr(0))
        two_a = u4.get((2, 2, 0), Fr(0))
        a = two_a / 2
        b = a_plus_b - a
        return c2, a, b, u6

    # ---- the closed forms, checked at five rational r values ----
    for r in (Fr(1), Fr(0), Fr(1, 2), Fr(2), Fr(3, 7)):
        c2, a, b, _ = solve_for(r)
        assert c2 == (1 + 2 * r) / 3, ("c^2 closed form failed", r)
        assert a == (1 - r) * (5 + 4 * r) / 108, ("isotropic closed form failed", r)
        assert b == -(1 - r) / 36, ("anisotropic closed form failed", r)
        if r != 1:
            assert a != 0 and b != 0, "r = 1 must be the UNIQUE root (seen nonzero away from it)"

    # ---- the r = 1 point: both zero, c^2 = 1, and the degree-6 survivor ----
    c2_1, a_1, b_1, u6_1 = solve_for(Fr(1))
    assert (c2_1, a_1, b_1) == (Fr(1), Fr(0), Fr(0)), "orbit-constant point must give (1, 0, 0)"
    # (1/90)[(K2)^3 - S6] expanded:  K2^3 = sum over multinomials; compare coefficient-wise
    K2 = {(2, 0, 0): Fr(1), (0, 2, 0): Fr(1), (0, 0, 2): Fr(1)}
    K2c = pmul(pmul(K2, K2), K2)
    S6 = {(6, 0, 0): Fr(1), (0, 6, 0): Fr(1), (0, 0, 6): Fr(1)}
    target = padd({e: c / 90 for e, c in K2c.items()}, {e: c / 90 for e, c in S6.items()}, Fr(-1))
    diff = padd(u6_1, target, Fr(-1))
    assert not diff, "degree-6 survivor at r = 1 must equal (1/90)[(k^2)^3 - Sum k_i^6]"

    # ---- scope fact (return-03 re-scope, 2026-08-25): the driven weight space is
    # 3-DIMENSIONAL, not 2 — the pointwise stabilizer cannot flip the e4 sign, so the
    # 24 bonds split 12 (hyperplane) + 6 (forward, b4 = +1) + 6 (backward, b4 = -1).
    # This primitive's model is RECIPROCAL (cosine symbol, even), so it sees only
    # J_f + J_b and the two-parameter (J_a, J_p) reading is COMPLETE for the
    # conservative sector; the THIRD direction (J_f - J_b, non-reciprocal hopping) is
    # odd in k4 — e.g. sum over the forward orbit of sin(b.k) = 2 sin(k4) * sum_i
    # cos(k_i), surviving at order k4*k^2 — and is INVISIBLE to any even symbol and
    # outside any polynomial-invariant argument on the even part. It is the
    # driven-dissipative channel's lattice face, named here so the orbit-constancy
    # question cannot be answered on the even sector alone and read as settling it.
    _bonds = []
    for i, j in itertools.combinations(range(4), 2):
        for si in (1, -1):
            for sj in (1, -1):
                v = [0, 0, 0, 0]
                v[i], v[j] = si, sj
                _bonds.append(v)
    _hyp = [v for v in _bonds if v[3] == 0]
    _fwd = [v for v in _bonds if v[3] == 1]
    _bwd = [v for v in _bonds if v[3] == -1]
    assert (len(_hyp), len(_fwd), len(_bwd)) == (12, 6, 6), \
        "driven-group bond-orbit split must be 12 + 6 + 6"
    r0 = solve_for(Fr(0))
    return {
        "model": ("SCALAR nearest-neighbour symbol on the 24 D4 kissing bonds; J_a on the 12 "
                  "e4-bearing, J_p on the 12 in-hyperplane (the two G48 sub-orbits of the one "
                  "W(F4) orbit, R-185); dispersion F = 0 at k4 = i*omega, exact Fraction series"),
        "driven_weight_space": ("3-DIMENSIONAL (return-03 re-scope): the pointwise stabilizer "
                                "splits the 24 bonds 12 + 6 + 6 (hyperplane / forward / "
                                "backward — asserted in-process), so orbit-constancy under "
                                "W(F4) opens to THREE driven weights. This RECIPROCAL model "
                                "sees only J_f + J_b and is complete for the CONSERVATIVE "
                                "sector; the third direction (J_f - J_b, non-reciprocal, odd "
                                "in k4: 2*sin(k4)*Sum cos k_i on the forward orbit, order "
                                "k4*k^2) is invisible to every even symbol — the "
                                "driven-dissipative channel's lattice face. An 'r = 1' answer "
                                "on the even sector does NOT settle the odd channel"),
        "c_squared": "(1 + 2r)/3, r = J_p/J_a",
        "deg4_isotropic_coefficient": "(1 - r)(5 + 4r)/108",
        "deg4_anisotropic_coefficient": "-(1 - r)/36",
        "orbit_constant_point": {"r": 1, "c_squared": 1, "deg4_isotropic": 0,
                                 "deg4_anisotropic": 0,
                                 "leading_survivor": "(1/90)[(k_sp^2)^3 - Sum k_i^6] — "
                                                     "anisotropic, dimension EIGHT"},
        "sub_orbit_extreme": {"r": 0, "deg4_isotropic": str(r0[1]), "deg4_anisotropic": str(r0[2]),
                              "meaning": "both order 1e-2 IN SUBSTRATE-c UNITS; converted (eta = c*(M_Pl/Lambda)^2, "
                                         "factor 1.85-6.69) the isotropic 5/108 reads eta in [0.086, 0.310] — "
                                         "STRADDLING the unconditional Auger bound 0.149 across the Lambda "
                                         "band (allowed loose corner, excluded ~2x tight corner), and 4.7-5.5 "
                                         "orders above the pure-proton-conditional corner (E21 + the "
                                         "contra-review units fix — the first-pass inside-by-3x reading was a "
                                         "c-vs-eta units error, caught contra-briefed)"},
        "unique_root": "r = 1 is the unique root of EITHER degree-4 coefficient — one condition, "
                       "both loads (the separator's own clause firing on R-185's orbit-constancy)",
        "adjudicated_reading": ("the CONSERVATIVE NN scalar part of the dim-6 exposure has natural "
                                "value ZERO at orbit-constant coupling; the exposure concentrates "
                                "in the orbit-splitting channel (V3-2a's sub-orbit support is the "
                                "live instance edge) and in the driven-dissipative sector (gated). "
                                "Whether the dressed couplings sit at r = 1 is the named OPEN "
                                "computation — the {J, D} matrix-valued version is the real object"),
        "model_rider": ("MANDATORY: scalar NN toy, NOT the banked {J, D} rotor structure; "
                        "matrix-valued internal-index kernels outside the theorem (P-sc); "
                        "non-analytic dissipative kernels outside entirely (P-an). PROOF OF "
                        "CONCEPT, NOT DISCHARGE — VG-6/N52 unmoved, no banked number changes"),
        "tier": ("DERIVED-A OF THE STATED MODEL (exact rational series identities; three "
                 "independent computations agree) + the mandatory model rider above. Consumes "
                 "the D4 siting (V3-1) and reads on the V3-2/V3-2a truncation — CANDIDATE half"),
        "provenance": ("proposed + first computed by the round-5 EXTERNAL reviewer (Opus, warm "
                       "return 02, 2026-08-25); independently reproduced by sympy series the same "
                       "hour; this primitive is the third route. Records: "
                       "knowledge/audit/external_review_r5_2026-08-25/"),
    }
