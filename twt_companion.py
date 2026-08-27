"""TWT COMPANION ENGINE — the deep-dive layer (split from twt.py, 2026-08-13).

WHAT THIS FILE IS. The engine was split in two (coordinator directive, 2026-08-12,
per knowledge/audit/engine_split_classification_2026-08-12.md): `twt.py` is the
MAIN engine — the primitives a reader of the foundational paper needs (paper-cited
rows of the companion Section 3 View A, core MV/e Clifford machinery, all classes,
the GATED raisers). THIS file is the COMPANION engine — the deep-dive layer:
exploration arcs (CKM/metatime, TASK-e4 epicycles, the matter-as-defect CKM-ladder
series), V2-era fine demonstrations, audit-record primitives, kernel-campaign
Phase-B probes, and probe-layer algebra cited only in the paper's companion or the
ledgers. Every def here was MOVED VERBATIM from twt.py — docstrings, tier tags and
claim wording are canon-protected and unchanged.

DEPENDENCY RULE (binding): the companion may call the main engine; the MAIN engine
NEVER calls the companion. `from twt import *` re-exposes the whole main namespace
here, so `import twt_companion` gives the full merged surface; the reverse import
does not exist.

THE FAMILY SPLIT, COMPANION SIDE (RUL-093/RUL-095, 2026-08-23). A SECOND cut now runs
across the engine, on a different axis: family-level (CORE) vs V3-instance (CANDIDATE).
On the MAIN side it is a FILE split (`twt_core.py` / `twt_candidate_v3.py`, with
`twt.py` as the import facade). HERE it is an in-file SECTION split — two banner-
delimited blocks below, ruled Option C because a fourth module would buy a small
direction guard on a small file and cost a third harness. The defs were REORDERED
ONLY: no docstring, body or tier tag changed, and the original relative order survives
inside each section. Per-section censuses are pinned in scripts/check_records.py.

Suite: twt_companion_test.py (this layer) + twt_test.py (main); scripts/bank.sh
runs BOTH and refuses to bank unless both pass.
"""
from __future__ import annotations
import math
import itertools
from itertools import combinations
import sympy as sp

from twt import *
# `import *` skips underscore names — every MAIN-engine helper a companion def
# actually calls (AST-derived list) is imported explicitly:
from twt import _Mcirc, _adV, _biv, _blade_mul, _cl40, _mixing


# ######################################################################
# ######################################################################
# ##                                                                  ##
# ##   SECTION CORE — FAMILY-LEVEL COMPANION PRIMITIVES               ##
# ##                                                                  ##
# ######################################################################
# ######################################################################
# THE FAMILY SPLIT, COMPANION SIDE (RUL-093/RUL-095, 2026-08-23). The MAIN engine
# split into two FILES on the family axis (twt_core.py / twt_candidate_v3.py). The
# companion is 18 CORE / 43 CANDIDATE and is already the deep-dive layer, so it
# carries the same cut as an in-file SECTION split instead — ruled Option C: a
# fourth module would buy a small direction guard on a small file and cost a third
# harness. Every def below was REORDERED ONLY; not one character of any docstring,
# body or tier tag changed, and the relative order inside each section is the
# file's original order.
#
# WHAT THIS SECTION HOLDS: companion primitives that consume NO V3 pick — exact
# Clifford / homotopy algebra, the ASD-triple generation structure, the Koide /
# Brannen structural face, the S5-generic NESS lean, the cost-pairing MENU algebra
# (Q-2, ruled CORE: the menu is family-level, the picks V3-7/V3-8 are not in these
# primitives), and the engine-internal audit record.
#
# DIRECTION NOTE: the file-level invariant that is AST-checked lives on the MAIN
# side (twt_core.py must never reference twt_candidate_v3). Here the cut is
# READABILITY-level by ruling — a section boundary is not a module boundary and the
# gate does not pretend otherwise. What IS pinned is the per-section census
# (scripts/check_records.py), so the sections cannot silently drift out of balance.
# ######################################################################



def single_relaxation_family_exclusion_probe():
    """[FRAMING / CANDIDATE-family-exclusion — Phase B / B2 of the Class-2 campaign (2026-07-05); the
    'unspent 2b move', spent] The analytic single-relaxation probe: take the SIMPLEST causal kernel family
    (Debye, amplitude chi0 + relaxation tau) and ask whether ANY member can be THE driven-dissipative
    kernel (source Theta_rel + land the channel targets). RESULT: a genuine FAMILY-EXCLUSION with a
    definite reason -- a PASSIVE single-relaxation kernel is FDT-RESPECTING by construction, so its
    FDT-violation residual (which IS Theta_rel, I-12) is IDENTICALLY ZERO for EVERY (chi0, tau). It can fit
    the passive channel numbers VACUOUSLY (2 dials, 2 numeric targets) and it satisfies the <=4-moment
    spin-2 bound (a single relaxation is ONE moment), but it CANNOT source the FDT-violation that is the
    whole point => EXCLUDED as the Theta_rel-kernel. The driven/FDT-violating content requires a
    NON-EQUILIBRIUM (driven) kernel => the CUDA D4-Langevin driven sim (B3) is the necessary next probe.

    THE FAMILY. chi(omega) = chi0 / (1 - i omega tau)  (Debye / single-pole). Then
        Re chi(omega) = chi0 / (1 + (omega tau)^2) ,   Im chi(omega) = chi0 omega tau / (1 + (omega tau)^2).
    CAUSAL: the only pole is at omega = -i/tau (LOWER half-plane) => chi analytic in the upper half-plane =>
    Kramers-Kronig holds (verified numerically below: Re from Im via the KK principal-value integral). This
    is the C1-safe part (causality/KK, NO FDT invoked).

    THE COUNTING (why 'survival' is vacuous). Dials = 2 (chi0, tau). NUMERIC channel targets = 2 (order-param
    (19/2)sqrt(38)~58.56; spin-0 c~2.05). The spin-2 target is STRUCTURAL (<=4 moments, R-151) and a single
    relaxation is ONE moment => AUTOMATICALLY satisfied. So 2 dials vs 2 numeric targets => EXACTLY-DETERMINED
    (generically one solution, zero residual) => the family 'survives' but the fit is a TAUTOLOGY, NOT an
    over-determination test (exactly N33's rank-deficiency, now at the analytic-kernel level: with only 2
    usable numeric anchors a 2-dial kernel is never tested).

    THE EXCLUSION (the real content). Theta_rel is DEFINED as the FDT-violation residual (I-12). A passive
    single-relaxation kernel is an EQUILIBRIUM linear response: its fluctuation spectrum and its dissipation
    Im chi are tied by the fluctuation-dissipation theorem, so the FDT-violation is IDENTICALLY ZERO --
    Theta_rel[passive Debye] = 0 for EVERY (chi0, tau), independent of the fit. Therefore NO member of the
    passive single-relaxation family can be the Theta_rel-kernel: the object the whole program hunts
    (Theta_rel != 0) is structurally ABSENT from any passive form. To get Theta_rel != 0 one needs a DRIVEN
    (non-equilibrium steady-state) kernel, where the fluctuation spectrum is NOT tied to Im chi by FDT --
    which is exactly what the B3 driven D4-Langevin sim measures (Theta_rel as a direct FDT-violation
    readout, R-114's mandatory non-Markovian/hysteretic drive).

    NAMED BRIDGES (all CANDIDATE-tier, carried for B4): (i) order-param 58.56 via |Im chi|/|Re chi|^2 at the
    QCP (N31 would-change-if); (ii) spin-2 via Maxwell eta = C_T Lambda^2 tau + the KSS near-floor (pins
    tau); (iii) spin-0 2.05 via the Volovik off-equilibrium deviation (N33 input 2). These bridges are the
    revert clauses: the exclusion is jointly conditional on 'Theta_rel = FDT-violation' (I-12, definitional,
    robust) -- the bridges only affect the vacuous-fit half, not the exclusion.

    VERDICT: the passive single-relaxation family is EXCLUDED as the Theta_rel-kernel (Theta_rel identically
    0), and its passive-target fit is vacuous (un-over-determined) => it is NOT a validated candidate. This
    SPENDS the analytic 2b move: the simplest family fails for a STRUCTURAL reason (no FDT-violation without
    drive), directing the program to the DRIVEN sim (B3). A family-exclusion is a first-class Phase-B result
    (brief B0). Tier FRAMING/CANDIDATE-family-exclusion; the causality/KK + counting are engine-checked, the
    exclusion rides I-12 (definitional).
    self-check: the single-relaxation Re/Im forms; KK (Re reconstructed from Im) holds to grid tolerance;
    1 relaxation = 1 moment <= 4; dials 2 == numeric targets 2 (exactly-determined, vacuous)."""
    import math
    import numpy as np
    tau = 1.0
    w = np.linspace(-60, 60, 240001)
    chi0 = 1.0
    Re = chi0 / (1 + (w * tau)**2)
    Im = chi0 * w * tau / (1 + (w * tau)**2)
    # Kramers-Kronig: Re(w0) = (1/pi) P int Im(w)/(w - w0) dw  -- reconstruct Re from Im at a few points
    def kk_re(w0):
        dw = w[1] - w[0]
        mask = np.abs(w - w0) > dw / 2      # principal value: drop the singular cell
        return (1 / math.pi) * np.sum(Im[mask] / (w[mask] - w0)) * dw
    test_pts = [-3.0, -0.7, 0.5, 2.0]
    kk_ok = all(abs(kk_re(w0) - chi0 / (1 + (w0 * tau)**2)) < 0.02 for w0 in test_pts)

    n_dials = 2                    # chi0, tau
    n_relaxation_moments = 1       # single pole
    ct_moment_bound = 4            # R-151
    n_numeric_targets = 2          # 58.56 (order-param), 2.05 (spin-0); spin-2 <=4 is structural
    satisfies_ct_bound = n_relaxation_moments <= ct_moment_bound
    exactly_determined = (n_dials == n_numeric_targets)   # vacuous fit, no over-determination
    theta_rel_passive = 0.0        # FDT-respecting passive kernel => FDT-violation residual = 0 (I-12)
    excluded_as_kernel = (theta_rel_passive == 0.0)       # cannot source Theta_rel != 0

    assert kk_ok, "single-relaxation kernel must satisfy Kramers-Kronig (Re reconstructed from Im)"
    assert satisfies_ct_bound, "a single relaxation is 1 moment <= 4 (R-151 spin-2 bound satisfied)"
    assert exactly_determined, "2 dials vs 2 numeric targets => exactly-determined (vacuous survival)"
    assert excluded_as_kernel, "passive single-relaxation is FDT-respecting => Theta_rel=0 => EXCLUDED as the kernel"

    return {
        "tier": "FRAMING / CANDIDATE-family-exclusion (causality/KK + counting engine-checked; the exclusion rides I-12, definitional)",
        "family": "chi(omega) = chi0/(1 - i omega tau) (Debye single-relaxation); Re=chi0/(1+(wt)^2), Im=chi0 wt/(1+(wt)^2)",
        "causality_KK": "verified: analytic in the upper half-plane (pole at -i/tau); Re reconstructed from Im via KK to grid tolerance",
        "counting": "2 dials (chi0, tau) vs 2 NUMERIC targets (58.56, 2.05) => exactly-determined (vacuous fit); spin-2 <=4 satisfied (1 relaxation = 1 moment)",
        "exclusion": "a PASSIVE single-relaxation kernel is FDT-RESPECTING => Theta_rel (the FDT-violation, I-12) = 0 for EVERY (chi0, tau) => EXCLUDED as the Theta_rel-kernel; the FDT-violating content requires a DRIVEN (non-equilibrium) kernel",
        "directs_to": "the CUDA D4-Langevin DRIVEN sim (B3): Theta_rel as a direct FDT-violation readout; the passive analytic family cannot host it",
        "bridges_named_CANDIDATE": "CANDIDATE-tier: (i) 58.56 via |Im chi|/|Re chi|^2 at the QCP (N31); (ii) spin-2 via Maxwell eta=C_T Lambda^2 tau + KSS floor; (iii) 2.05 via Volovik off-eq deviation (N33) -- revert clauses for the vacuous-fit half only",
        "verdict": "the analytic 2b move is SPENT: the passive single-relaxation family is EXCLUDED (Theta_rel identically 0) and its passive fit is vacuous (un-over-determined) => NOT a validated candidate; a family-exclusion (first-class, brief B0) directing to the driven sim B3",
    }


def dip_planes_multiaxis_but_uniform_is_single_axis():
    """[DERIVED — Level 1] §19.7: (D3) The three per-generation dip planes {(1,4),(2,4),(3,4)} induce so(3)
    generators on V that SPAN so(3) (rank 3 = multi-axis), so a NON-uniform dip WOULD be multi-axis — but the
    uniform-strength dip (one eps per sector) is their SUM, which is exactly the G-generator/colour symmetric
    (1,1,1) axis = SINGLE axis. The multi-axis freedom exists but the uniform dip engages only the one axis."""
    import math
    np, e, I4 = _cl40()
    D = [_adV(np, e, _biv(e, i, 4)) for i in (1, 2, 3)]
    rank = int(np.linalg.matrix_rank(np.array([d.flatten() for d in D]), tol=1e-9))
    assert rank == 3, rank
    def axial(M): return np.array([M[2, 1], M[0, 2], M[1, 0]])
    colour = _adV(np, e, (_biv(e, 1, 2) + _biv(e, 2, 3) - _biv(e, 1, 3)) / math.sqrt(3))
    uniform = axial(D[0] + D[1] + D[2]); col_ax = axial(colour)
    cosang = abs(uniform @ col_ax) / (np.linalg.norm(uniform) * np.linalg.norm(col_ax))
    assert abs(cosang - 1.0) < 1e-9, cosang
    return {"dip_planes_span_so3_rank": rank, "uniform_dip_parallel_to_colour_axis": round(float(cosang), 12),
            "meaning": "multi-axis freedom exists but the uniform dip engages only the single symmetric axis"}


def phase_D_colour_updown_blind():
    """[DERIVED — PHASE D run, not cut off; Level 2, shares D2's contingency] (D4) The colour/I4 channel acts
    as SO(3) on the spatial axes {e1,e2,e3} (I4-duals of the colour trivectors). up,down are BOTH colour
    triplets => the SAME colour rotation hits both frames => CANCELS in V_u†V_d => still democratic. And
    [colour-gen, I4]=0 => the up/down e4-orientation (handedness, §19.8.1) CANNOT make the colour rotation
    differ. The thesis's own colour/chirality mechanism supplies no per-weak-isospin rotation (contingent, as
    D2, on the weak-isospin identification — the only door that could differentiate up/down via colour)."""
    import math
    np, e, I4 = _cl40()
    Mu, Md = _Mcirc(np, 1.033, 0.973, 2/9), _Mcirc(np, 1.172, 0.344, 2/9)
    a = np.array([1.0, 1, 1]); a = a / np.linalg.norm(a)
    K = np.array([[0, -a[2], a[1]], [a[2], 0, -a[0]], [-a[1], a[0], 0]])
    Rcol = np.eye(3) + math.sin(0.7) * K + (1 - math.cos(0.7)) * K @ K
    Mu2, Md2 = Rcol @ Mu @ Rcol.T, Rcol @ Md @ Rcol.T
    cUD = np.linalg.norm(Mu2 @ Md2 - Md2 @ Mu2)
    Vu, Vd = np.linalg.eigh(Mu2)[1], np.linalg.eigh(Md2)[1]
    mixing = _mixing(np, Vu.conj().T @ Vd)
    col_gen = (_biv(e, 1, 2) + _biv(e, 2, 3) - _biv(e, 1, 3))
    cI4 = np.linalg.norm(col_gen @ I4 - I4 @ col_gen)
    assert cUD < 1e-12 and mixing < 1e-9 and cI4 < 1e-12, (cUD, mixing, cI4)
    return {"[M_u,M_d]_after_colour": f"{cUD:.1e}", "CKM_mixing_dist_from_permutation": f"{mixing:.1e}",
            "[colour_gen,I4]": f"{cI4:.1e}",
            "verdict": "colour is up/down-BLIND => no per-weak-isospin rotation => still DEMOCRATIC"}


def hodge_split_invariance_theorem():
    """[TASK-e4 PART A, theorem — VERIFIED] rest mass = |B_spatial| of a fixed generator
    bivector B cycled by G (the §19.6.1 120°-about-(1,1,1) rotation). G is a SPATIAL bivector
    (G in span{e12,e13,e23}); its adjoint preserves the spatial/e4 Hodge decomposition as a
    direct sum of so(3) reps -> BOTH |B_spatial| AND |B_e4| are invariant along the whole
    generation orbit (the build asserted only the first; the second is forced). A sector-MIXING
    rotation (e24, a Q-bivector) DOES modulate |B_spatial| (contrast).
    CONSEQUENCE: the literal '|B_spatial| of the G-cycled rotor' gives NO generation variation
    -- not even the deferent. So THIS reading is dead; see epicycle_reading_dependent() for why
    that does NOT settle the central claim."""
    np = __import__("numpy")
    G = G_generator()
    assert all(bl in [(1, 2), (1, 3), (2, 3)] for bl, _ in G.terms), "G must be a SPATIAL bivector"
    def sp(mv): return math.sqrt(sum(c*c for bl, c in mv.terms if bl in [(1, 2), (1, 3), (2, 3)]))
    def e4f(mv): return math.sqrt(sum(c*c for bl, c in mv.terms if bl in [(1, 4), (2, 4), (3, 4)]))
    B0 = 1.0*e(1, 2) + 0.7*e(1, 4) + 0.4*e(2, 3) + 0.5*e(3, 4)
    sp0, e40 = sp(B0), e4f(B0)
    dG_sp = dG_e4 = dmix = 0.0
    for phi in np.linspace(0, 2*math.pi, 400):
        RG = exp_unit_bivector(G, phi); BG = RG*B0*RG.reverse()
        dG_sp = max(dG_sp, abs(sp(BG) - sp0)); dG_e4 = max(dG_e4, abs(e4f(BG) - e40))
        RM = exp_unit_bivector(e(2, 4), phi); BM = RM*B0*RM.reverse()
        dmix = max(dmix, abs(sp(BM) - sp0))
    assert dG_sp < 1e-12, "G must preserve |B_spatial| exactly (Hodge-split invariance)"
    assert dG_e4 < 1e-12, "G must preserve |B_e4| exactly too (the forced strengthening)"
    assert dmix > 0.1, "a sector-mixing rotation (e24) must modulate |B_spatial| (contrast)"
    return {"G_is_spatial": True, "max_d|B_spatial|_under_G": float(dG_sp),
            "max_d|B_e4|_under_G": float(dG_e4), "max_d|B_spatial|_under_e24": round(float(dmix), 3),
            "consequence": "|B_spatial|-of-G-cycled-rotor gives NO generation variation (not even deferent)"}


def generations_are_defect_flows_on_spinor_S3() -> dict:
    """[DERIVED geometry + FRAMING picture + CANDIDATE up/down + LOCATED dynamical residual]
    The SHARP matter-as-defect image of the generation sector (replacing the fuzzy phase reading),
    Yaer 2026-06-25. A generation is a DEFECT WINDING-FLOW on the spinor 3-sphere.

    DERIVED (geometry, engine-checked): the anti-self-dual triple {e12+e34, e13-e24, e14+e23} are the
    3 generators of ONE SU(2) factor of Spin(4) -- they are mutually ORTHOGONAL, EQUAL-NORM (norm^2=2),
    and close as su(2) EXACTLY ([J_i,J_j] = -4 J_k, verified) = the 3 imaginary units of H. That SU(2) is the 3-sphere S^3 = unit-H,
    which is PARALLELIZABLE by EXACTLY 3 global vector fields (the H units). So:
      * generation = a defect's meta-time WINDING-FLOW along one of the 3 globally-consistent
        invariant directions of the anti-self-dual spinor S^3;
      * WHY EXACTLY 3 / WHY NOT 4 is now TOPOLOGICAL (defect-centric), not just 'su(2) is 3-dim':
        S^3 admits exactly 3 combable global flows (dim S^3 = 3, and it is parallelizable so the flows
        are GLOBALLY stable); a 4th generation would need a 4th independent global flow on S^3, which
        does not exist. (Same count as the banked H-triple, RECAST as defect winding-flows -- this is
        the sharp picture, NOT a new number.)

    FRAMING (the picture, circular-polarization mapping): Spin(4) = SU(2)xSU(2) = the two CIRCULAR
    handednesses (self-dual / anti-self-dual = left/right isoclinic). Generations live in ONE handedness
    (anti-self-dual S^3, the 3 flows above); the OTHER handedness (self-dual S^3) is weak isospin su(2)+
    [SETTLED SINCE (2026-06-29, N29; RE-SETTLED 2026-08-21, R-171/RUL-082 — the menu is THREE
    classes and it CLOSED, so weak = SD su(2)+ is DERIVED-given-{A-P2 + RH-singlet datum}, not a
    counted free bit): weak = SD su(2)+ is the framework's weak-host assignment
    (§C.4.2) — one bit, with V−A/generation-blindness/up=SD derived-given-it; the historical
    N4-era hedge formerly here is superseded.]
    BASIS NOTE (wavefront, §12.5/§7): SPIN = the L-orbit {e12,e13,e23} (e4-FREE planes = the observer's
    spatial rotations gamma^i gamma^j = -e_ij), and it is exactly the SPATIAL part of each anti-self-dual
    generation flow (e12 in e12+e34, etc.). NOT {e_i4}: the Q-orbit {e14,e24,e34} is the observer's spatial
    direction-VECTORS (gamma^j=e4 e_j) AND the §8.3 quark-CKM-orbit -- a DISTINCT role from the H-triple
    generations (§8.4 warns against conflating them). So {e_ij}=spin is the right basis here, {e_i4} is not.
    The vacuum is an ACTIVE carrier (s0=(1+e4)/2): it FILLS any defect WITHOUT topological winding
    (pi_3(S^3)=Z); a generation survives only by winding (inverse of a radio signal, which survives by
    frequency-separation on a passive carrier). So 'must span an amplitude reversal' = the nonzero-winding
    condition = why the carrier does not fill these 3.

    CANDIDATE (up/down, Gemini CAND 3, post-hoc + substrate-testable): the +e4 chirality sets the helicity
    of the winding relative to the wave -- up-type CO-rotating (rides +e4: lighter gen-1, steeper scaling),
    down-type COUNTER-rotating (m_d>m_u, slower). Matches the gross pattern (m_d>m_u; up-tower steeper);
    the exact P+ = (1+e4)/2 projection test is owed; NOT derived.

    LOCATED RESIDUAL (the #1 gap, unchanged but sharpened): the DYNAMICAL SELECTION -- the EOM by which a
    defect locks onto these 3 flows and intermediate windings RADIATE/fill (Gemini CAND 1's radiative
    limit-cycle is the candidate but UNPROVEN -- needs the driven-dissipative EOM; its D4-Langevin sim is
    the N9 forbidden toy, NOT run) -- and the phase->mass map (which flow carries which generation mass /
    the hierarchy). REFUTED en route: Gemini CAND 2 (period-doubling -> 3) -- period-doubling gives a 2^n
    cascade (->inf before chaos), not 3, and omega/2^n != the mass ratios.

    derived-vs-generic: substrate-specific = the anti-self-dual su(2) closure + S^3=unit-H being the rotor
    target; the S^3-parallelizability '3 global flows' is the defect-picture form of dim su(2)=3 (a
    sharpening, same count). NO new number is claimed derived; the dynamical selection stays the #1 gap."""
    out = {}
    J = [e(1, 2) + e(3, 4), e(1, 3) + (-1.0) * e(2, 4), e(1, 4) + e(2, 3)]
    def norm2(x): return sum(c * c for _, c in x.terms)
    out["anti_self_dual_triple_orthonormal"] = all(abs(norm2(j) - 2.0) < 1e-12 for j in J)  # equal-norm (=2)
    # su(2) closure EXACTLY: [J_i, J_j] = -4 J_k (cyclic) -- tightened from blade-membership to proportionality
    def approx_eq(a, b):
        d = a - b
        return all(abs(c) < 1e-9 for _, c in d.terms)
    closes = []
    for i, j in [(0, 1), (1, 2), (2, 0)]:
        k = ({0, 1, 2} - {i, j}).pop()
        closes.append(approx_eq(comm(J[i], J[j]), (-4.0) * J[k]))
    out["su2_closure"] = all(closes)   # exact [J_i,J_j] = -4 J_k
    assert out["anti_self_dual_triple_orthonormal"] and out["su2_closure"], \
        "anti-self-dual triple must be an orthogonal equal-norm su(2) ([J_i,J_j]=-4J_k) = 3 H units = SU(2)=S^3 generators"
    out["count"] = 3
    out["why_3"] = "S^3 = SU(2) = unit-H is parallelizable by EXACTLY 3 global flows; a defect winds along one => 3 generations"
    out["why_not_4"] = "no 4th independent global flow on S^3 (dim S^3 = 3); a 4th generation has nowhere to wind"
    out["generations_handedness"] = "anti-self-dual S^3 (one circular polarization); self-dual S^3 = weak isospin su(2)+ [CANDIDATE §8.4; vs §10.5 L-orbit; embedding UNDETERMINED, N4]"
    out["spin_basis"] = "SPIN = L-orbit {e12,e13,e23} (e4-free; = observer rotations gamma^i gamma^j = -e_ij, §12.5); = the spatial part of each anti-self-dual generation flow. NOT {e_i4} (Q-orbit = observer spatial AXES + §8.3 CKM-orbit, a distinct role)"
    out["survival"] = "active vacuum carrier fills non-wound defects (pi_3=Z); generations survive by winding (NOT frequency-separation)"
    out["up_down"] = "CANDIDATE (Gemini CAND3): +e4 helicity -- up co-rotating (steeper), down counter (m_d>m_u); P+ test owed"
    out["dynamical_selection"] = "OPEN (#1 gap): the EOM picking 3 flows + radiating intermediates (CAND1 unproven); phase->mass map open"
    out["period_doubling_why3"] = "REFUTED (CAND2): period-doubling is 2^n->inf, not 3; omega/2^n != mass ratios"
    out["verdict"] = ("SHARP defect-picture: a generation = a defect WINDING-FLOW on the anti-self-dual spinor "
                      "S^3 (one circular handedness); EXACTLY 3 because S^3 is parallelizable by exactly 3 global "
                      "flows (defect-centric why-3/why-not-4, the SAME count as the H-triple recast); weak isospin "
                      "= the other handedness; +e4 helicity = up/down (CANDIDATE). The DYNAMICAL selection (lock to "
                      "3 + radiate the rest, and the mass hierarchy) stays the #1-gap residual; period-doubling REFUTED.")
    return out


# item 8b, step 5 (2026-06-24, Yaer: "do the residuals"). Residual (a): WHICH mass-measure governs the
# multi-quark coherent sum -- the meson's linear-in-amplitude m=2w|cos(a/2)|, or the gear's frequency
# lock? Resolved by the WINDING SENSE. Residual (b): the absolute omega scale = the #1 gap (located).
def winding_sense_sets_mass_measure() -> dict:
    """[DERIVED (winding sense) + FRAMING (the measure consequence)] item 8b step 5 -- RESIDUAL (a)
    ADJUDICATED (structurally, by a FRAMING bridge; empirically undiscriminated): the meson and baryon
    have DIFFERENT mass-measures because their constituents have OPPOSITE vs SAME winding sense -- one
    ontology, mass=omega of the locked config, two regimes. NOTE this is a structural ADJUDICATION (the
    deciding co<->gear link is FRAMING, not derived) NOT a closure: the two candidate floors are near-
    degenerate so DATA cannot yet force the choice, and the gear's VALUES stay gap-gated (residual b).

    DERIVED (topological winding):
      * MESON = q + qbar: windings +1/3 and -1/3 -> net B=0 -> OPPOSITE sense = COUNTER-rotating pair.
      * BARYON = 3 quarks: 3 x (+1/3) -> net B=1 (pi3_S3_integer_completion) -> SAME sense = CO-rotating.

    FRAMING (why the measures differ -- the resolution of residual (a)):
      * COUNTER-rotating (meson, opposite omega) -> the pair BEATS; the interference enters the mass
        DIRECTLY: m = 2 omega |cos(alpha/2)| (meson_dynamical_current_split) -- mass LINEAR in the
        coherent amplitude. This is the regime where the GOLDSTONE subtraction lives (alpha=pi cancels).
      * CO-rotating (baryon, same omega) -> the frequencies LOCK and ADD: the colour-singlet constraint
        omega1+omega2+omega3 = Omega_B (gear_eigenvalues) + an internal-mode INERTIA (Theta_A/Theta_B).
        This is the §17.3 GEAR -- NOT a linear-in-amplitude coherent sum.
      => The 'linear-|A| meson->baryon assumption' that underpinned steps 3-4 (the parallelogram floor,
         the Goldstone subtraction) is the MESON (counter-rotating) measure IMPORTED. The BARYON's OWN
         primary measure is the gear (co-rotating frequency lock), which is already DERIVED STRUCTURE.
         They are ONE ontology (mass = omega of the locked configuration) under opposite vs same winding,
         and they reconcile on the internal mode (step 2). So the baryon mass functional's BACKBONE is
         the gear; the Goldstone-subtraction is the meson-sector sibling, consistent-on-the-mode but not
         the baryon's fundamental measure.

    EMPIRICAL (the two floors are near-degenerate, so data can't yet force the choice): the gear/arith
    floor (S+L)/2 and the meson/quadrature floor sqrt((S^2+L^2)/2) differ by only 0.6 MeV at Lambda/Sigma
    and ~9.9 MeV even at the wide N/Delta pair -- consistent with either; not a discriminator yet.

    RESIDUAL (b) -- the ABSOLUTE omega/Omega_B scale -- is the #1 GAP (NOT a separate gate): it is the
    SAME absolute-scale gate that sets f_pi / the soliton normalization (canon §2 'f_pi the one fitted
    mass scale'; cf. q_l_stiffness_ratio_is_gap_gated). The gear gives the STRUCTURE (Omega_B=Sum omega,
    Theta eigenvalues) gate-free; the absolute MeV waits on the driven-dissipative dynamics. Nothing
    gate-free remains in (b) -- it is located, not open-ended.

    NET (item 8b closeout): the non-additive baryon mass functional = the §17.3 GEAR (co-rotating
    frequency-lock Omega_B=Sum omega + internal-mode inertia, DERIVED structure); colour mass-blind
    (step 1); same-composition splits isolate the internal mode (step 2); the meson Goldstone
    subtraction is the counter-rotating sibling (steps 3-4); residual (a) resolved (winding sense picks
    the gear for baryons); residual (b) = the #1 gap (absolute scale). derived-vs-generic: substrate-
    specific = the B=0(opposite)/B=1(same) winding topology and the engine's two measures; the
    counter->beat / co->frequency-lock consequence is a FRAMING identification (physical, consistent
    with both engine primitives), NOT a fresh derivation of either measure."""
    out = {}
    # DERIVED: winding sense (B numbers)
    pc = pi3_S3_integer_completion()
    assert pc["3×(1/3) = 1 is an integer"], "baryon B=1 (3 co-rotating 1/3 windings)"
    out["meson_B"], out["baryon_B"] = 0, 1
    out["meson_sense"] = "OPPOSITE (q + qbar) = counter-rotating"
    out["baryon_sense"] = "SAME (3 quarks) = co-rotating"
    # the two engine measures
    out["meson_measure"] = "m = 2*omega*|cos(alpha/2)| (counter beat; LINEAR in coherent amplitude; Goldstone subtraction)"
    out["baryon_measure"] = "gear: Omega_B = omega1+omega2+omega3 lock + inertia (§17.3 eigenvalues are DERIVED; the co-rotating<->gear LINKAGE is FRAMING)"
    out["linear_A_is_meson_import"] = True   # steps 3-4's 'linear-|A| for baryon' = the meson measure
    out["baryon_primary_measure"] = "the §17.3 gear (co-rotating frequency lock), NOT the linear coherent amplitude -- adjudicated via the FRAMING bridge"
    # UPDATE: the linkage's FREQUENCY-LOCK half is no longer FRAMING -- it is DERIVED via E-centrality
    out["cogear_linkage_freqlock_now_derived"] = ("cogear_linkage_kinematic: Omega_B=Sum omega is "
        "DERIVED-CONDITIONAL (2026-07-02 sweep re-tier: central-E additivity holds ONLY in the E channel; "
        "R-127/R-128 lock the observer-visible mass phase to winding blades whose axes do not commute) -- "
        "the E-channel composition premise + the E-floor->observer bridge + the §17.3 INERTIA tensor + "
        "whether freq-sum IS the mass are the open residual")
    # EMPIRICAL: floors near-degenerate (can't yet discriminate)
    floors = {}
    for nm, m1, m2 in [("Lambda/Sigma", 1115.68, 1192.64), ("N/Delta", 938.27, 1232.0)]:
        ar = (m1+m2)/2.0; qu = math.sqrt((m1*m1+m2*m2)/2.0)
        floors[nm] = {"arith_gear": round(ar, 1), "quad_meson": round(qu, 1), "diff_MeV": round(qu-ar, 1)}
    out["floors_near_degenerate"] = floors
    out["empirically_undiscriminated"] = "floors agree to 0.6 (Lambda/Sigma) / 9.9 (N/Delta) MeV => DATA cannot force gear-vs-meson; the adjudication rests on the FRAMING winding bridge ALONE"
    assert floors["N/Delta"]["diff_MeV"] < 15, "arith(gear) and quad(meson) floors must be near-degenerate (data can't force the choice)"
    # RESIDUAL (b): the #1 gap
    out["residual_b_absolute_scale"] = "the absolute omega/Omega_B scale = the #1 GAP (same gate as f_pi/soliton normalization); STRUCTURE gate-free, VALUE gap-gated; located, not open-ended"
    out["verdict"] = ("RESIDUAL (a) ADJUDICATED structurally (FRAMING bridge, empirically undiscriminated): "
                      "winding sense sets the measure -- meson (B=0, OPPOSITE/counter -> beat -> mass linear in "
                      "amplitude, Goldstone) vs baryon (B=1, SAME/co -> frequency lock Omega_B=Sum omega -> the "
                      "§17.3 GEAR, whose eigenvalues are DERIVED though the co<->gear LINKAGE is FRAMING). The "
                      "linear-|A| of steps 3-4 is the MESON import; the baryon's primary measure is the gear; one "
                      "ontology under opposite/same winding, reconciled on the internal mode. The two floors are "
                      "near-degenerate so DATA can't yet force the choice (rests on the framing bridge). RESIDUAL "
                      "(b) = the #1 gap (absolute scale, located, NOT separate).")
    return out


def generation_index_survives_brannen_excision():
    """[DERIVED-STRUCTURAL — assembly synthesis B3, Workers 1+4 convergence]

    The IDENTIFICATION of the generation operator with the meta-time phase advance (per
    `generation_z3_is_metatime_phase`) does NOT depend on the √m=r² mass-measure choice or
    the modified-Brannen empirical fit. The core derivation runs:

      (i)  Spatial G_generator preserves |B_spatial| and |B_e_4| under conjugation to 1e-12
           ⇒ spatial G is MASS-BLIND ⇒ cannot source any mass hierarchy
      (ii) Therefore spatial G is the COLOUR Z3 (3 colours mass-degenerate)
      (iii) The GENERATION operator must be a DIFFERENT Z3 action that DOES source a hierarchy
      (iv) The meta-time phase advance is the natural candidate (acts on the e_5/τ_5 channel,
           which is the mass channel per `mass_measure_from_omega` ontology)

    Step (i) is pure Cl(4,0) algebra (commutator of G with bivector content, no mass measure
    involved). Step (ii) is identification. Step (iii) is logical. Step (iv) identifies meta-time
    phase as the operator — but does NOT bank what the operator's eigenvalues are at each phase.

    What DOES depend on Brannen / √m=r² (and is THEREFORE under WP-MASS-MEASURE suspicion):
    the SPECIFIC mass values at each meta-time phase sample. That's the spectrum-at-each-phase,
    not the existence of the operator.

    Consequence: if WP-MASS-MEASURE excises the unified-Brannen framework, the generation
    OPERATOR identification survives. What gets demoted is the per-phase mass prediction.

    This banks the engine-checkable separation between (a) the generation operator
    (DERIVED, survives) and (b) the mass-at-each-phase prediction (CANDIDATE-strong,
    conditional on the WP-MASS-MEASURE rebuild)."""
    # Engine check: spatial G mass-blindness is purely algebraic (no mass measure invoked)
    G = G_generator()
    B0 = 1.0 * e(1, 2) + 0.7 * e(1, 4) + 0.4 * e(2, 3) + 0.5 * e(3, 4)
    np = __import__("numpy")

    def split(mv):
        sp = math.sqrt(sum(c * c for b, c in mv.terms if b in [(1, 2), (1, 3), (2, 3)]))
        ep = math.sqrt(sum(c * c for b, c in mv.terms if b in [(1, 4), (2, 4), (3, 4)]))
        return sp, ep

    sp0, ep0 = split(B0)
    dsp_max = dep_max = 0.0
    for phi in np.linspace(0, 2 * math.pi, 200):
        R = exp_unit_bivector(G, phi)
        sp, ep = split(R * B0 * R.reverse())
        dsp_max = max(dsp_max, abs(sp - sp0))
        dep_max = max(dep_max, abs(ep - ep0))
    assert dsp_max < 1e-12 and dep_max < 1e-12, (
        "spatial G mass-blindness must hold (pure algebra, no mass measure invoked)")
    return {
        "tier": "DERIVED-STRUCTURAL",
        "spatial_G_max_dsp": dsp_max,
        "spatial_G_max_dep": dep_max,
        "spatial_G_is_mass_blind": True,
        "implication_1_spatial_G_is_colour_Z3": True,
        "implication_2_generation_operator_is_metatime_phase": True,
        "depends_on_mass_measure": False,
        "depends_on_Brannen": False,
        "what_DOES_depend_on_mass_measure": (
            "the per-phase mass eigenvalue spectrum (CANDIDATE-strong, conditional on WP-MASS-MEASURE rebuild)"
        ),
        "what_survives_Brannen_excision": (
            "the OPERATOR identification: generation = meta-time phase advance, NOT spatial G"
        ),
    }


def pure_L_rotor_preserves_spatial_radius():
    """[DERIVED-A — Phase F audit residue, 2026-06-30]

    Clean substrate-pure fact (the narrow result that survives the REFUTED forward-derivation
    attempt of lepton ε=0 from L-orbit e_4-freeness, Phase F audit):

      For any unit bivector B ∈ span(L_BIVECTORS) (with B²=−1) and any spatial vector r_0
      ∈ span{e_1, e_2, e_3}, the rotor orbit r(φ) = exp(½φB)·r_0·exp(−½φB) has CONSTANT
      spatial radius:
        |r(φ)|_spatial² := Σ_{i=1,2,3} ⟨r(φ), e_i⟩² = |r_0|²   for all φ.

    Underlying algebra: L_BIVECTORS commute with e_4 ⇒ L-rotors preserve the e_4-component
    of any vector ⇒ the spatial component evolves as a rotation in the spatial 3-volume,
    preserving its norm.

    Honest scope (from Phase F audit REFUTED verdict):
      - This DOES bank a clean substrate fact about L-rotor geometry.
      - This does NOT by itself close the lepton ε=0 forward derivation. The Phase F
        attempt (Worker 4 §8.2) tried to leverage this fact to derive ε=0 in the
        modified-Brannen cos(2φ) channel, but the bridge fails on two counts:
          (1) GRADE CONFLATION: lepton BLADE = e_123 (grade-3 trivector); lepton orbit
              GENERATOR is a bivector (grade-2). No banked primitive maps lepton-blade
              to L-bivector-as-rotor-generator. Different objects.
          (2) PARAMETER CONFLATION: Brannen's τ = e_4-dip of OFFSET AXIS (deferent tilt);
              the L↔Q-mixing-angle of the rotor GENERATOR is a different object. The
              "cos(2φ) coefficient = sin²(τ)/2" claim depended on r_0 = e_1 (special
              choice); for generic r_0 the ratio is 0.59-0.84, not 1.

    Filed as the narrow honest residue of N-LEPTON-EPS-FROM-L-ORBIT (negatives ledger,
    2026-06-30). The fact itself is real and could be a building block for future
    substrate-derivations bridging lepton-blade to lepton-orbit-generator (gap 1)."""
    np = __import__("numpy")
    # Engine-verify for all three L-bivectors and several non-trivial r_0
    for name, B in L_BIVECTORS.items():
        # Confirm B²=−1
        bb = (B * B).coeff(())
        assert abs(bb - (-1.0)) < 1e-12, f"{name} must have B²=−1"
        # Confirm B commutes with e_4
        assert B * e(4) == e(4) * B, f"{name} must commute with e_4"
    # For each L-bivector, check several r_0 and confirm spatial radius is constant
    r0_choices = [e(1), e(2), e(3), 0.7 * e(1) + 0.4 * e(2), 0.5 * e(1) + 0.6 * e(2) + 0.3 * e(3)]
    spatial_norm = lambda v: math.sqrt(sum(v.coeff((i,)) ** 2 for i in (1, 2, 3)))
    for name, B in L_BIVECTORS.items():
        for r0 in r0_choices:
            target = spatial_norm(r0)
            for phi in np.linspace(0, 2 * math.pi, 50):
                R = exp_unit_bivector(B, phi / 2)
                rphi = R * r0 * R.reverse()
                got = spatial_norm(rphi)
                assert abs(got - target) < 1e-10, (
                    f"pure-L rotor under {name} must preserve spatial radius for r_0={r0}; "
                    f"got {got} vs target {target} at phi={phi}")
    return {
        "tier": "DERIVED-A",
        "claim": "pure-L rotor preserves spatial radius exactly (any L-bivector, any spatial r_0)",
        "underlying_algebra": "L_BIVECTORS commute with e_4 ⇒ L-rotors preserve e_4 component ⇒ spatial radius preserved",
        "engine_verified_for_L_bivectors": list(L_BIVECTORS.keys()),
        "engine_verified_for_r0_choices": ["e_1", "e_2", "e_3", "0.7e_1+0.4e_2", "0.5e_1+0.6e_2+0.3e_3"],
        "tolerance": "1e-10 absolute on spatial-radius difference",
        "does_NOT_close": "lepton ε=0 forward derivation (Phase F audit REFUTED Worker 4 §8.2 chain)",
        "bridge_gaps_remaining": [
            "(1) GRADE: lepton blade e_123 (grade-3) ≠ L-bivector (grade-2); no banked map",
            "(2) PARAMETER: Brannen τ (offset-axis e_4-dip) ≠ L↔Q-mixing of rotor generator",
        ],
        "filed_as": "narrow honest residue of N-LEPTON-EPS-FROM-L-ORBIT (negatives ledger)",
    }


def e4_acts_as_identity_on_Splus() -> bool:
    """[DERIVED] §18.3a: e4·s0 = s0 (e4 = +1 on the e4=+1 ideal)."""
    return (e(4) * s0()) == s0()


def compact_spin4_favors_limit_cycle() -> dict:
    """[DERIVED-generic / FRAMING — substrate facts produce a STRUCTURAL LEAN
    toward Floquet limit-cycle NESS over self-organized-critical NESS, but do NOT
    DECIDE the dichotomy (SOC is biased-against, not excluded). Sector-2 of the
    2026-06-28 symmetry-shortcut hunt; supplies independent structural support
    for Fork B in `eom_compatible_field_forks` and the N11-U1 / N15 lean.
    Canon-§2 tier: DERIVED-generic (the unqualified/-generic variant — real but
    generic-given-coarse-substrate-facts, the Sakharov-Λ² template of canon §5),
    NOT DERIVED-A and NOT DERIVED-P. /FRAMING because the dichotomy stays open.]

    Pin a SINGLE fork-lean from compact-group + periodic-drive geometry —
    e5-litmus-free (no e5 spatial) and not §9.6-routed (no kernel import; §9.6
    is the kernel that Fork B is ABOUT, so routing through it would beg the
    question). Four substrate facts conjoin:

    F1 — COMPACT TARGET. The rotor field lives on Spin(4) = SU(2)_+ × SU(2)_-
      = S^3 × S^3, compact without boundary (the two chiral Spin(4) factors of
      the substrate). Dissipative trajectories on a compact manifold are
      uniformly bounded; no unbounded target-space scale develops. Caveat:
      compactness alone does NOT kill SOC (SOC's correlation length is a
      SPATIAL field-correlator property, not target-space).

    F2 — PERIODIC FINITE-FREQUENCY DRIVE. The advancing e4 wave is a periodic
      drive at the rotor frequency ω_d = mass (canon §0: mass = the meta-time
      rotor frequency). Periodic + dissipative + compact ⇒ Floquet theory
      applies and generically yields a T_d=2π/ω_d-periodic (or rationally
      mode-locked p:q) attractor — a limit cycle. This is GENERIC dynamical-
      systems theory (Floquet/Krein; Pikovsky–Rosenblum–Kurths synchronization),
      DERIVED-generic-given-(compact + periodic-drive), NOT a TWT theorem.

    F3 — MULTIPLE INTRINSIC SCALES. The substrate has ≥3 banked scales:
      Λ (UV cutoff = grain spacing), T_d=2π/ω_d (drive period), f_π (hadronic-
      cell scale) — and additionally the Spin(4) group radius from F1. SOC
      requires SCALE INVARIANCE — a fine cancellation that no substrate
      symmetry enforces (contrast: s=3 decoherence is symmetry-pinned, not
      scale-tuned). Multi-scale ⇒ SOC is measure-zero — a LEAN, not a proof.

    F4 — NO SLOW/FAST SEPARATION. Canonical SOC (BTW/OFC/sandpile) needs
      slow drive + fast relaxation (drive ≪ relaxation rate). The e4-drive
      is at the substrate's PRIMARY timescale (ω_d = ω_rotor, by ontology);
      no slow-driving limit. Removes the canonical SOC mechanism; does not
      exclude non-canonical continuum-SOC at finite drive.

    NET — FORK B LEAN. F1+F2 furnish a generic Floquet attractor; F3+F4
      remove canonical SOC routes. STRUCTURAL LEAN toward Floquet limit-cycle
      NESS, substrate-grounded (none of F1-F4 imports the kernel, runs §9.6,
      or uses e5 spatially) and INDEPENDENT of N9's D4-Langevin toy hint —
      two independent supports converge on the same lean. NOT a decision: the
      dichotomy is biased-against SOC, not exclusive (topological criticality
      on compact targets, or continuum-SOC at finite drive, are not refuted).
      The kernel decides; the geometry only leans. Note: the substance of F2
      already lives in `theta_rel_universality_located` R2 (Floquet lean + N9
      numerical hint); the genuinely NEW content here is F3 (multi-scale ⇒ SOC
      measure-zero) and F4 (no slow/fast separation removes BTW/OFC SOC).

    TIER (canon §2 + §5 derived-vs-generic). DERIVED-generic: each Fi is a
    banked substrate fact (compactness, periodicity, multi-scale, timescale
    identity); the CONJUNCTION is generic dynamical-systems theory, so the lean
    is DERIVED-generic-given-(F1-F4), the Sakharov-Λ² template (canon §5) —
    real but generic, NOT a substrate-specific theorem and NOT a closed Clifford
    identity (so NOT DERIVED-A) and NOT a clean physical forcing (NOT DERIVED-P).
    The DICHOTOMY remains OPEN (Fork B decision stays #1-gap GATED). Downstream:
    the SOC-universality route to (α,g,g_s) is structurally DISFAVORED (not
    refuted) — the gauge couplings likely require a more bespoke mechanism than
    NESS universality.

    NEGATIVES-DISCIPLINE (canon §4). Tried whether substrate GEOMETRY ALONE
    decides Fork B → succeeded at the LEAN level (F1-F4) → would change if the
    built §9.6 kernel flows to a genuine scale-invariant fixed point despite
    F1-F4 (topological criticality on compact target / continuum-SOC at finite
    drive). Then the kernel verdict overrides the geometric lean. Not a §1
    SM-retreat (no e5-spatial, no §9.6 routing, no imported QFT theorem in the
    forcing step).

    self-check: F1 compact + boundary-free; F2 periodic finite-frequency drive
    (ω_d = mass, canon §0); F3 substrate scales ≥3; F4 no slow/fast separation
    (drive timescale = system timescale by ontology); cross-references
    (theta_rel_universality_located N11/U1, eom_compatible_field_forks Fork B)
    resolve and lean limit-cycle the same way."""
    # F1 — Compact target.
    F1 = {
        "manifold": "Spin(4) = SU(2)_+ x SU(2)_- = S^3 x S^3",
        "compact": True, "boundary": False,
        "bites": "uniformly bounded dissipative trajectories; no target-space scale-divergence",
        "caveat": "compactness alone does NOT kill SOC (correlation length is a SPATIAL "
                  "field-correlator, not a target-space property)",
    }
    # F2 — Periodic finite-frequency drive (canon §0: mass = ω_d).
    F2 = {
        "drive": "advancing e4 wave at omega_d = mass (meta-time rotor freq; canon §0)",
        "kind": "periodic, finite-frequency, continuous (NOT slow-driven)",
        "period": "T_d = 2pi/omega_d",
        "bites": "Floquet/Krein + Pikovsky synchronization => generic T_d-periodic (or p:q mode-locked) attractor",
        "tier": "DERIVED-generic-given-(compact+periodic-drive), NOT a TWT theorem",
    }
    # F3 — Multiple intrinsic scales (SOC requires scale invariance).
    F3 = {
        "intrinsic_scales": ["Lambda (UV cutoff = monad spacing)",
                              "T_d = 2pi/omega_d (drive period)",
                              "f_pi (hadronic-cell scale)",
                              "Spin(4) group radius (from F1)"],
        "n_scales_at_least": 3,
        "SOC_requirement": "scale-invariant attractor (no characteristic scale)",
        "bites": ">=3 intrinsic scales => scale-invariance is measure-zero with no symmetry to enforce it",
        "caveat": "SOC AT one of these scales is not strictly excluded — a LEAN, not a proof",
    }
    # F4 — No slow/fast separation.
    F4 = {
        "canonical_SOC_needs": "slow drive << fast relaxation (BTW/OFC/sandpile)",
        "substrate_reality": "omega_drive = omega_rotor = omega_system (ontology: drive IS the substrate's primary timescale)",
        "separation": False,
        "bites": "removes canonical SOC mechanism by construction",
        "caveat": "does NOT exclude non-canonical (continuum-SOC at finite drive) classes",
    }
    # Cross-references must resolve and the existing Fork B lean must agree.
    tu = theta_rel_universality_located()
    assert "FRAMING + LOCATED-GAP (N11)" in tu["tier"], "N11-U1 lean must resolve"
    ff = eom_compatible_field_forks()
    assert "limit-cycle" in ff["forks"]["B_NESS_character(N11)"]["status"], "Fork B lean must agree"
    # Self-check assertions on the four substrate facts.
    assert F1["compact"] and not F1["boundary"]
    assert F2["kind"].startswith("periodic")
    assert F3["n_scales_at_least"] >= 3
    assert not F4["separation"]
    lean = {
        "Fork B verdict (geometry-only, e5-litmus-free, no §9.6 routing)": "LEANS LIMIT-CYCLE (Floquet)",
        "support": "F1+F2 => generic Floquet attractor; F3+F4 => canonical SOC routes removed",
        "vs N9": "N9 (D4-Langevin toy) and F1-F4 (structural) lean limit-cycle for INDEPENDENT reasons — "
                 "convergent support, NOT a tighter derivation",
        "decision_status": "DICHOTOMY NOT DECIDED — SOC biased-against, not excluded; the §9.6 kernel decides",
    }
    return {
        "question": "does compact-Spin(4) + periodic e4-drive STRUCTURALLY prefer Floquet limit-cycle NESS "
                    "over SOC-critical NESS, e5-litmus-free and not §9.6-routed?",
        "answer": "STRUCTURAL LEAN yes (4 substrate facts F1-F4); DECISION no (geometry leans, kernel decides)",
        "F1_compact_target": F1, "F2_periodic_drive": F2,
        "F3_multi_scale": F3, "F4_no_slow_fast_separation": F4,
        "lean": lean,
        "fork_B_status_update": "OPEN, leans limit-cycle: was '(N9 D4-Langevin toy)' alone; now also "
                                "'(F1-F4 structural, geometry-grounded)' — two independent supports converge",
        "downstream_implication": "SOC-universality route to (alpha,g,g_s) (the §9.6 coupling-universality hope, "
                                  "N11/N15) is STRUCTURALLY DISFAVORED — not refuted; gauge couplings "
                                  "likely require a more bespoke mechanism than NESS universality",
        "would_change_if": "the built §9.6 kernel is shown to flow to a genuine scale-invariant fixed point "
                           "despite F1-F4 (e.g. topological criticality on compact targets, continuum-SOC at "
                           "finite drive). Then the kernel verdict overrides the geometric lean.",
        "scope_honesty": "DERIVED-generic-given-(F1-F4), NOT DERIVED-A/-P. Per canon §5 derived-vs-generic, "
                         "this is the Sakharov-Λ² template: real, but generic-given-coarse-substrate-facts.",
        "tier": "DERIVED-generic / FRAMING: structural lean derived from F1-F4 substrate facts; "
                "dichotomy NOT decided (SOC biased-against, not excluded); Fork B DECISION stays #1-gap GATED. "
                "Negatives-discipline (canon §4): tried→succeeded at LEAN level→would-change-if kernel shows SOC. "
                "Not §1 SM-retreat (no e5-spatial, no §9.6 routing, no imported QFT theorem in the forcing).",
    }


def generation_values_monad_forked():
    """[located-gap (N21 measure-fork RESOLVED) + DERIVED sub-results + FRAMING (the structure/value tiering) — N22;
    TWT_DEFECT_CKM_GLUON.md §19] A 3-route workflow + developer verification (sympy-exact) asking which quantization
    ordering the substrate dictates for the collective coordinate, and what TIER that makes the generation VALUES.
    (The fork's small-size endpoint is the GRAIN — this primitive's name retains the older word 'monad'.)

    ── RESOLVES the N21 measure sub-fork: the physical ordering is COVARIANT (Laplace-Beltrami), Q=0 ───────
    The von Roos ordering ambiguity is PHYSICAL, so it must be fixed by the substrate. Collective-coordinate
    quantization on a moduli space has a canonical answer — the COVARIANT (Laplace-Beltrami / Gervais-Jevicki)
    operator, hermitian w.r.t. the invariant moduli measure. For the 1-D breathing modulus R it gives an induced
    potential of EXACTLY ZERO for ANY metric g(R) (1-D moduli is flat; in arc-length s=∫√g dR, LB = −d²/ds², no
    potential). LB is the UNIQUE reparametrization-covariant von Roos member — every non-LB ordering adds a +c/R²
    that is NOT a coordinate scalar (it changes under R→u), hence unphysical. **So the covariant ordering supplies
    NO induced −1/r²; the N21 "von Roos measure spans the BF threshold ⇒ could be supercritical" sub-route is CLOSED**
    — the supercritical orderings are non-covariant artifacts. (One POSITED hinge: that the TWT rotor inner product
    is the coordinate-free moduli L²-norm that selects LB — standard collective quantization, §17-grounded, not a
    separately-built Clifford identity.)

    ── the 2D-curvature objection, DEFUSED (the decisive push-past) ────────────────────────────────────
    The physical collective manifold is really 2-D — (R, θ) with θ the meta-time mass-phase — and its Ricci scalar
    is NONZERO (~R⁻³ at R→0), so a covariant DeWitt curvature term Q=ξ·R_scalar seems to survive. BUT θ is the
    CENTRAL U(1)_E mass-phase (a CYCLIC, commuting coordinate). Separating ψ=e^{inθ}φ(R) collapses the 2-D operator
    to a 1-D radial problem whose θ-centrifugal term n²/(2Λ(R)) with Λ=aR³+bR is **n²/(2bR) near R→0 — a SOFT 1/R
    (degree −1), NOT a scale-invariant R⁻²** (sympy-exact). So the R⁻³ curvature is a coordinate artifact of the
    un-separated operator; after separation there is no forced supercritical −g/r² from curvature.

    ── ★ THE HONEST TIER OF THE GENERATION VALUES — a SHARPENED 2-WAY FORK (not a flat input) ───────────
    With the measure sub-route dead, the cost-table VALUES (the 6 numbers; the lepton masses + CKM magnitudes that
    are physical per §5) are GATED-WITH-AN-OPEN-FORK at the R→0 grain endpoint:
      (a) a grain-scale INPUT — same tier as Λ/f_π (canon §2), the knowability shape of `induced_G_only_grain_scale_enters`
          (cutoff-gated, consistent-with-not-confirming underivability) — IF the resolution is the conservative
          self-adjoint-extension parameter fixed by grain-scale D4-lattice 3-body CONTACT (Efimov-on-the-lattice); OR
      (b) Im χ-GATED and dynamically DERIVABLE — IF the resolution is the DISSIPATIVE hysteretic kernel (Fork A,
          Θ_rel-kind coset-Cartan/FDT-violation); calling its output "input" would smuggle a gated quantity into the
          input tier.
    SHARPENING (tilts toward dynamical): a static boundary parameter alone gives at most ONE bound state, NOT a
    geometric TOWER — log-periodicity still needs a genuine attractive −1/4 1/s² channel, so even branch (a) needs
    the dynamical 3-body contact to SOURCE the channel. Both live routes are grain-scale and essentially DYNAMICAL;
    the measure was a red herring for the values. Only the Im χ branch can supply the chirality-signed DSI-breaking
    RUNNING rate the data demands (a single Λ/f_π ratio gives ONE universal log-period, but the data is 6 numbers =
    3 distinct tower scales + within-tower drift of OPPOSITE signs, sign = the up↔down mirror).

    ── the STRUCTURE/VALUE line (branch-independent SCAFFOLD vs FORKED VALUES) — tier-honest, mixed tiers ──
    The branch-independent SCAFFOLD is NOT uniformly DERIVED — only two members are unconditionally DERIVED; the rest
    are weaker and carry their true tier: (1) [DERIVED, sympy-exact] the 1-D-moduli covariant-Q=0 fact + the cyclic-θ
    soft-1/R defusal; (2) [DERIVED, sympy-exact] the bulk-arithmetic negative (cranked no R⁻²); (3) [STRUCTURAL,
    dynamical selection OPEN] the 3 windows (N13 topological, contingent on generation=ℍ-triple); (4) [DERIVED-in-KIND,
    CONDITIONAL on up=SD/down=ASD — per V3 R-077 given the weak=SD assignment R-079
    (DERIVED-given-{A-P2 + RH-singlet datum} since RUL-082, not an INPUT bit); label updated 2026-07-02 from the
    stale 'N4-CANDIDATE' (N4 resolved (ii) LOCATED, see weak_isospin_verdict)] the up↔down MIRROR
    (`chirality_is_a_reflection`); (5) [FRAMING — the
    UNSETTLED channel] the NON-SELF-ADJOINT character (N21); (6) [TAUTOLOGY, not a prediction] the O(few) cost SCALE
    (the r⁴ map, N20); (7) [FRAMING] the RELOCATION to R→0. So TWT derives THAT there are 3 (structural) non-self-adjoint
    (framing) mirror-paired (conditional) O(few)-cost (tautology) windows needing a chirality-signed running rate; it
    does NOT derive WHICH costs. NOT a derivation of the values; NOT a flat deflation to input. The #1 gap stands,
    localized to: is the R→0 datum a conservative D4-3-body contact (values=INPUT) or the Im χ kernel (values=GATED)?

    ── COORDINATE DISAMBIGUATION (the −1/r² channel's r/R) — to keep the arc unambiguous ────────────────
    The radial coordinate r/R of the −1/r² channel is the **soliton-SIZE = breathing-mode collective MODULUS**
    throughout N20–N22 (the dynamical coordinate whose closed-orbit action is S(r)); R→0 is its small-size = grain
    limit. It is NOT the *static* soliton radius of the √m=r²⇒ω=r⁴ mass map (that enters only the cost=4·ln(r-gap)
    TAUTOLOGY), and NOT the phase θ (the central U(1)_E mass-phase, cyclic, → the soft 1/R, not the −1/r²).

    Tier: located-gap (N21 measure-fork resolved) + DERIVED sub-results (covariant LB ⇒ Q=0; cyclic-θ ⇒ soft 1/R) +
    FRAMING (structure-DERIVED / values-FORKED). NOT DERIVED for the values.
    self-check: the cyclic-θ centrifugal is degree −1 (soft 1/R), not R⁻²; Λ=aR³+bR has no R⁻² in n²/(2Λ)."""
    import sympy as sp
    R, a, b, nph = sp.symbols('R a b n_phase', positive=True)
    # the decisive defusal: cyclic-theta separation gives a SOFT 1/R, not a scale-invariant R^-2
    Lam = a * R**3 + b * R
    cent = sp.series(nph**2 / (2 * Lam), R, 0, 2).removeO()
    assert cent.coeff(R, -2) == 0                                    # NO scale-invariant R^-2
    assert cent.coeff(R, -1) == nph**2 / (2 * b)                     # leading term is the SOFT 1/R (degree -1)
    # the covariant (LB) member: induced potential identically 0 for ANY 1D metric. PROOF (Liouville normal form):
    # LB as Sturm-Liouville -(p f')'=λ w f has p=√g·g⁻¹=g^{-1/2}, w=√g (the invariant measure); the induced potential
    # is Q=m''(s)/m with m=(p·w)^{1/4}. For LB, p·w = g^{-1/2}·g^{1/2} = 1 ⇒ m=1 ⇒ Q=0, for any g. (non-LB orderings
    # have p·w ≠ 1 ⇒ Q≠0, and that Q is not a coordinate scalar.)
    m = sp.Symbol('m', positive=True)
    g_pow = R**m                                                    # arbitrary power-law 1D moduli metric
    p_lb, w_lb = g_pow**sp.Rational(-1, 2), sp.sqrt(g_pow)          # LB Sturm-Liouville weights
    assert sp.simplify(p_lb * w_lb) == 1                            # ⇒ Liouville m=(pw)^{1/4}=1 ⇒ induced Q=0 (covariant ordering, any metric)
    return {
        "measure_subroute_resolved": "the physical (covariant Laplace-Beltrami) ordering gives Q=0 for the 1-D breathing modulus (any metric); LB is the unique "
                                      "reparametrization-covariant von Roos member; non-covariant orderings add a +c/R² that is not a coordinate scalar ⇒ N21's supercritical measure sub-route is CLOSED",
        "curvature_objection_defused": "the 2-D (R,θ) Ricci is ~R⁻³ at R→0, but θ is CYCLIC (central U(1)_E mass-phase); separation ψ=e^{inθ}φ(R) gives a θ-centrifugal "
                                       "n²/(2(aR³+bR)) = soft n²/(2bR) (degree −1), NOT R⁻² ⇒ the curvature singularity is a coordinate artifact, no forced supercritical channel",
        "values_tier": "GATED-WITH-AN-OPEN-FORK (NOT a flat input, NOT a derivation): the cost-table numbers / lepton masses / CKM magnitudes are EITHER (a) a monad-scale "
                       "INPUT (tier Λ/f_π) if the R→0 resolution is the conservative self-adjoint-extension / D4-3-body-contact parameter, OR (b) Im χ-GATED and dynamically DERIVABLE if dissipative (Fork A)",
        "sharpening": "a static boundary parameter alone gives ≤1 bound state, not a geometric TOWER; log-periodicity needs a genuine −1/4 1/s² channel, so even the conservative "
                      "branch needs the dynamical 3-body contact to source it. Only the Im χ branch can supply the chirality-signed DSI-breaking RUNNING rate the 3 drifting towers demand",
        "structural_scaffold_mixed_tiers": {
            "DERIVED (sympy-exact)": ["1-D-moduli covariant Q=0 (+ cyclic-θ soft-1/R)", "the bulk-arithmetic negative (cranked no R⁻², N21)"],
            "STRUCTURAL (dyn. selection open)": "3 windows (N13 topological, contingent on generation=ℍ-triple)",
            "DERIVED-in-KIND (conditional on up=SD/down=ASD, per R-077 given weak=SD INPUT R-079; ex-N4-CANDIDATE, N4 resolved (ii) LOCATED)": "the up↔down mirror (chirality_is_a_reflection)",
            "FRAMING": ["the NON-SELF-ADJOINT character (N21, the UNSETTLED channel)", "the relocation to R→0"],
            "TAUTOLOGY (not a prediction)": "the O(few) cost scale (the r⁴ map, N20)"},
        "coordinate_disambiguation": "the −1/r² channel's r/R is the soliton-SIZE = breathing-mode collective MODULUS (S(r) = its closed-orbit action; R→0 = monad limit), "
                                     "NOT the static √m=r²⇒ω=r⁴ radius (that enters only the cost=4·ln(r-gap) tautology), NOT the phase θ (cyclic, → the soft 1/R)",
        "next_step": "the SMALL-DEFECT discriminator: construct the TWT rotor inner product on the breathing moduli to FIX the R→0 extension, then test whether monad-scale "
                     "D4-lattice 3-body CONTACT (Efimov-on-lattice) supplies a supercritical g_eff>1/4 channel AND the chirality-signed running rate — conservative (values=INPUT) vs Im χ (values=GATED)",
        "tier": "located-gap (N21 measure-fork resolved) + DERIVED sub-results (covariant LB ⇒ Q=0; cyclic-θ ⇒ soft 1/R defusing the 2D curvature) + FRAMING (structure-DERIVED / "
                "values-FORKED tiering); the VALUES tier is GATED-with-an-open-fork (conservative-INPUT vs dissipative-Im χ-GATED), NOT a flat input, NOT DERIVED for the values",
    }


def tunneling_evanescent_decay_constant():
    """[DERIVED-A (both the exact NR recovery and the KG correction, sympy-exact); WP-TUN-1 RESOLVED
    2026-07-06] Reproduces the SSB.3.6 evanescent-tail tunneling check with an engine primitive, and
    CORRECTS the V2-era claim. RESULT: the recovery of the standard decay constant is EXACT in the
    non-relativistic (Schrodinger) limit (0%, not 5%); the leading deviation is a RELATIVISTIC (KG-parent)
    correction controlled by (V-E)/mc^2 -- NOT the tunneling depth V0/E. So the V2-era '5% in the
    deep-tunneling regime V0/E >= 5' figure is MIS-PARAMETRIZED and is DEMOTED, replaced by the derived
    correction formula.

    (1) NON-RELATIVISTIC RECOVERY [DERIVED-A, EXACT]. The linearized wave equation in the classically-
        forbidden region V > E is the time-independent Schrodinger form  psi'' = (2m(V-E)/hbar^2) psi,
        with the decaying solution psi ~ exp(-kappa_NR x) and
            kappa_NR = sqrt(2 m (V-E)) / hbar   -- the STANDARD QM decay constant, recovered EXACTLY
        (0% deviation; it is the defining equation of the forbidden-region tail, not a 5% approximation).

    (2) RELATIVISTIC (KG-PARENT) CORRECTION [DERIVED-A, sympy-exact]. TWT's actual substrate wave equation
        is the hyperbolic KG parent (SSB.3.7); a static potential gives, in the forbidden region,
            -hbar^2 c^2 psi'' + m^2 c^4 psi = (E - V)^2 psi   =>   kappa_rel = sqrt(m^2 c^4 - (E-V)^2)/(hbar c),
        with E the TOTAL relativistic energy (E = mc^2 + W, W the non-rel energy). Then
            kappa_rel / kappa_NR = sqrt(1 - (V-E)/(2 m c^2))  ~  1 - (V-E)/(4 m c^2),
        where (V-E) is the non-rel barrier-minus-energy. The deviation from standard QM is thus
        (V-E)/(4 m c^2) at leading order -- a RELATIVISTIC ratio (barrier energy vs rest mass), which
        reaches 5% at (V-E)/mc^2 ~ 0.195.

    (3) THE V2 FIGURE, CORRECTED [DEMOTE]. '5% in the deep-tunneling regime V0/E >= 5' conflates two
        different ratios: the deviation is set by (V-E)/mc^2 (relativistic), NOT by V0/E (tunneling depth).
        For a deep barrier that is still non-relativistic ((V-E) << mc^2) the deviation is << 5% no matter
        how large V0/E is; a 5% deviation needs (V-E) ~ 0.2 mc^2, a semi-relativistic barrier. So the V2
        '5% at V0/E>=5' is MIS-PARAMETRIZED. Correct statement (now in SSB.3.6): EXACT NR recovery + a
        relativistic correction (V-E)/(4mc^2) controlled by the barrier-to-rest-mass ratio.

    TWT-specific candidate prediction (UNCHANGED, CANDIDATE): a further small deviation when the wave-train
    extent and the barrier scale are comparable (leading-edge/barrier interference) -- not quantified.

    self-check: the NR forbidden-region equation gives kappa_NR = sqrt(2m(V-E))/hbar exactly; the KG
    forbidden-region decay gives kappa_rel/kappa_NR = sqrt(1 - (V-E)/(2mc^2)) (sympy-exact); the deviation
    is controlled by (V-E)/mc^2 (relativistic), NOT V0/E; 5% deviation at (V-E)/mc^2 ~ 0.195."""
    import sympy as sp
    m, c, hbar, W, Vpot = sp.symbols('m c hbar W V_pot', positive=True)
    DeltaV = Vpot - W                                   # (V - E), non-rel barrier minus energy (>0)

    # (1) NR: the forbidden-region Schrodinger solution's decay constant (exact)
    kappa_NR = sp.sqrt(2 * m * DeltaV) / hbar
    x = sp.symbols('x', real=True)
    psi = sp.exp(-kappa_NR * x)
    nr_residual = sp.simplify(sp.diff(psi, x, 2) - (2 * m * DeltaV / hbar**2) * psi)
    nr_exact = (nr_residual == 0)                        # exact solution => 0% deviation

    # (2) KG: forbidden-region relativistic decay constant + the correction ratio
    E_tot = m * c**2 + W
    kappa_rel = sp.sqrt(m**2 * c**4 - (E_tot - Vpot)**2) / (hbar * c)
    ratio_sq = sp.simplify(kappa_rel**2 / kappa_NR**2)
    correction_form = 1 - DeltaV / (2 * m * c**2)
    kg_matches = (sp.simplify(ratio_sq - correction_form) == 0)
    leading = sp.series(sp.sqrt(correction_form), DeltaV, 0, 2).removeO()   # 1 - (V-E)/(4mc^2)
    leading_ok = (sp.simplify(leading - (1 - DeltaV / (4 * m * c**2))) == 0)

    # (3) the deviation is relativistic ((V-E)/mc^2), NOT V0/E; 5% at ~0.195
    dev5_ratio = float(sp.nsolve(sp.sqrt(1 - sp.Symbol('r') / 2) - sp.Rational(95, 100), sp.Symbol('r'), 0.2))

    assert nr_exact, "NR forbidden-region recovery of kappa_NR = sqrt(2m(V-E))/hbar must be EXACT (0%)"
    assert kg_matches, "KG correction kappa_rel/kappa_NR must be sqrt(1 - (V-E)/(2mc^2))"
    assert leading_ok, "leading deviation must be (V-E)/(4 m c^2)"
    assert abs(dev5_ratio - 0.195) < 0.01, "5% deviation occurs at (V-E)/mc^2 ~ 0.195 (relativistic, not V0/E)"

    return {
        "tier": "DERIVED-A (exact NR recovery + sympy-exact KG correction) -- WP-TUN-1 resolved",
        "nr_recovery": "EXACT: the forbidden-region Schrodinger equation gives kappa_NR = sqrt(2m(V-E))/hbar with 0% deviation (it is the defining equation, not a 5% approximation)",
        "kg_correction": "kappa_rel/kappa_NR = sqrt(1 - (V-E)/(2 m c^2)) ~ 1 - (V-E)/(4 m c^2) -- the RELATIVISTIC correction; this is STANDARD relativistic QM (any KG particle gets it), recovered here from the substrate's KG parent (SSB.3.7), NOT a TWT-specific prediction. The TWT-specific deviation remains the (unquantified) wave-train/barrier-scale interference",
        "deviation_controlled_by": "(V-E)/mc^2 (barrier energy vs rest mass), NOT V0/E (tunneling depth); 5% at (V-E)/mc^2 ~ 0.195",
        "v2_figure_verdict": "DEMOTED: '5% in the deep-tunneling regime V0/E >= 5' is MIS-PARAMETRIZED (conflates the relativistic ratio with the tunneling depth); replaced by the derived correction",
        "twt_candidate_deviation": "UNCHANGED (CANDIDATE): a further deviation when wave-train extent ~ barrier scale (leading-edge/barrier interference), not quantified",
    }


# ---- e4-conjugation is the L/Q projector, not the up/down projector (CAND 3 refutation / N28) ----
def e4_conjugation_is_LQ_not_updown() -> dict:
    """[DERIVED — exact Clifford, no toy] §19.9: (N28 / CAND 3 refutation, 2026-06-28)
    The e4-conjugation C4(B) = e4·B·e4 on all 6 grade-2 bivectors:
      L-orbit {e12,e13,e23} (no e4 index): C4(B) = +B  (eigenvalue +1)
      Q-orbit {e14,e24,e34} (one e4 index): C4(B) = -B  (eigenvalue -1)
    So P+(e4) = ½(1+C4) projects onto L-orbit = LEPTON sector;
       P-(e4) = ½(1-C4) projects onto Q-orbit = QUARK sector.
    Within Q-orbit, ALL THREE bivectors share eigenvalue -1 — NO sub-splitting into up/down.

    INCOMMUTABILITY: C4 and the Hodge star (I4·) are INCOMMENSURABLE on grade-2.
    C4 maps the SD generator (e12-e34) to the ASD generator (e12+e34); [C4,Hodge](sd)=2*asd != 0.
    The L/Q splitting (C4) and the SD/ASD splitting (I4) are orthogonal projections of grade-2 -- no
    basis simultaneously diagonalizes both.

    CAND 3 REFUTED (2026-06-24 candidate file, helical-pitch-asymmetry): the claim is that
    P+(e4) = ½(1+e4) acting on the intersection of SD and ASD bivector spaces algebraically fixes
    the up/down mass-scaling exponent ratio. This fails on two independent counts:
      1. P+(e4) is the L/Q projector: C4=+1 ↔ LEPTON; C4=-1 ↔ QUARK. Within the Q-orbit C4=-1
         uniformly on {e14,e24,e34} — there is no e4-based sub-splitting into up vs down.
      2. SD∩ASD = {0}: the SD and ASD subspaces are complementary; their intersection is trivial,
         so there is no non-zero element for P+(e4) to act on differentially.

    LOCATED GAP -- N28: tried e4-helicity P+/-(e4) as up/down projector within Q-orbit ->
    REFUTED: P+/-(e4) is the L/Q (lepton/quark sector) projector; within Q, C4 = -1 uniformly;
    SD/ASD and L/Q are incommensurable. Would change if: sec.9.6 EOM distinguishes SD vs ASD
    dynamics of Q-orbit bivectors (a Layer-2 driven-dissipative distinction, not a static Clifford fact).

    DERIVED-VS-GENERIC (sec.5 guardrail): the algebraic eigenvalue formula C4(B)=+/-B depending on
    e4-index count is GENERIC for any Euclidean Clifford algebra with a distinguished e4. What is
    SUBSTRATE-SPECIFIC is the CONCLUSION -- "C4 is the L/Q projector" -- because that requires the
    Cl(4,0) orbit identification L-orbit=lepton sector, Q-orbit=quark sector (banked via I4_maps_L_to_Q,
    not generic across dimensions). The DERIVED tag attaches to the conclusion, not the formula.

    Consistent with: chirality_does_not_source_P (I4:Q->L => chirality blind on Q-orbit);
    chiral_split_demo (SD/ASD mixes L and Q); chirality_is_a_reflection (parity<->SD/ASD, FRAMING)."""
    e4 = e(4)
    L_bivs = {"e12": e(1)*e(2), "e13": e(1)*e(3), "e23": e(2)*e(3)}
    Q_bivs = {"e14": e(1)*e(4), "e24": e(2)*e(4), "e34": e(3)*e(4)}

    def c4(B): return e4 * B * e4

    L_eigs_ok = {name: (c4(B) == B) for name, B in L_bivs.items()}
    Q_eigs_ok = {name: (c4(B) == (-1.0) * B) for name, B in Q_bivs.items()}

    # Incommutability: C4 maps SD generator to ASD (they are not C4 eigenstates)
    sd_gen  = e(1)*e(2) - e(3)*e(4)   # self-dual (I4 eigenvalue +1)
    asd_gen = e(1)*e(2) + e(3)*e(4)   # anti-self-dual (I4 eigenvalue -1)
    c4_sd_is_asd = (c4(sd_gen) == asd_gen)

    I4 = e(1)*e(2)*e(3)*e(4)
    comm = c4(I4 * sd_gen) - (I4 * c4(sd_gen))   # [C4, Hodge](sd_gen) = 2·asd_gen
    comm_nonzero = (comm.terms != ())

    assert all(L_eigs_ok.values()),   f"L-orbit C4 eigenvalue +1 check failed: {L_eigs_ok}"
    assert all(Q_eigs_ok.values()),   f"Q-orbit C4 eigenvalue -1 check failed: {Q_eigs_ok}"
    assert c4_sd_is_asd,              "C4 must map SD(e12-e34) -> ASD(e12+e34)"
    assert comm_nonzero,              "[C4,Hodge] must be non-zero on grade-2 bivectors"

    return {
        "L-orbit C4(B)=+B (LEPTON sector)": L_eigs_ok,
        "Q-orbit C4(B)=-B (QUARK sector)": Q_eigs_ok,
        "C4 maps SD(e12-e34) -> ASD(e12+e34)": c4_sd_is_asd,
        "[C4,Hodge](sd_gen) non-zero": comm_nonzero,
        "Q-orbit: no sub-splitting (all C4=-1)": all(Q_eigs_ok.values()),
        "DERIVED": (
            "P+(e4)=L-projector (lepton sector); P-(e4)=Q-projector (quark sector); "
            "within Q-orbit C4=-1 uniformly -- no up/down sub-split exists. "
            "SD/ASD and L/Q are incommensurable on grade-2 (C4 maps SD<->ASD; [C4,Hodge]!=0)."
        ),
        "CAND3_REFUTED": (
            "P+(e4) acting on SD^ASD cannot algebraically fix up/down scaling: "
            "(1) P+(e4) is the L/Q splitter, not up/down; C4=-1 uniformly on Q. "
            "(2) SD^ASD={0}; no non-zero element to act on."
        ),
        "N28_located_gap": (
            "Tried e4-helicity P+/-(e4) as up/down projector within Q-orbit -> REFUTED. "
            "Would change if: sec.9.6 EOM distinguishes SD vs ASD dynamics on Q-orbit (Layer-2)."
        ),
        "tier": "DERIVED (exact Clifford, all asserts pass) + LOCATED-GAP N28 (CAND 3 refuted)",
    }


# ======================================================================
# §19/§17.4 BRIDGE: META-TIME-PHASE SAMPLING vs V_4^perp PROJECTION READING
# (Brannen formula consequences under the §17.4 reidentification)
# ======================================================================

def metatime_brannen_vs_v4perp_projection_reach():
    """[DERIVED + LOCATED-GAP] §17.4 (ii) vs §19.2 — the two Brannen-amplitude
    readings AGREE on the harmonic FORM but DIFFER on the Brannen-coefficient
    REACH at the empirical Koide value.

    §19.2 V_4^perp projection picture: A_{ki} = sqrt(3)*(v_k, e_{i4}) with
    v_k = d + (c/sqrt(2))*e_hat_k, giving a_k = 1 + c*cos(phi_i - phi_k).
    Here c is FREE (the V_4^perp tilt magnitude); K = (2+c^2)/6 reaches the
    empirical K = 2/3 at c = sqrt(2) (INPUT, exact-but-unforced, §19.4).

    §17.4 meta-time-phase sampling picture: sqrt(m_n) = r^2(phi_n, tau=0) where
    r is the position-orbit spatial radius. At the lepton boundary tau=0
    (eps_l = 0):
        r^2(phi, 0) = (d + cos(phi-psi))^2 + sin^2(phi-psi)
                    = (1+d^2) + 2*d*cos(phi-psi),
    so the normalized Brannen amplitude is a_n = (1+d^2)*(1 + c_norm*cos(phi_n-psi))
    with c_norm = 2*d/(1+d^2). By AM-GM, |c_norm| <= 1 for all real d (equality
    at d=1), so K <= (2+1)/6 = 1/2. Solving 2*d/(1+d^2) = sqrt(2) gives the
    quadratic sqrt(2)*d^2 - 2*d + sqrt(2) = 0 with discriminant 4 - 8 = -4 < 0:
    NO REAL d delivers c = sqrt(2). Hence the empirical K = 2/3 <=> c = sqrt(2)
    is UNREACHABLE under this literal position-orbit sampling at tau = 0.

    Q1 (projection-forced sqrt(2)): NO — §17.4 has no sqrt(2) projection factor
    (d is the orbit-offset magnitude, c_norm = 2*d/(1+d^2) is a different
    geometric ratio); the §19.2 sqrt(2) (the V_4^perp transverse/longitudinal
    projection ratio |e_{i4}^perp|/(e_{i4}, d) = sqrt(2/3)/(1/sqrt(3)) = sqrt(2))
    has no counterpart here.

    Q2 (Foot 45°): NO at tau = 0 — Foot 45° requires K = 2/3 (cos^2(theta) =
    1/(3K) = 1/2). The §17.4 sampling caps K at 1/2 (at d=1, c_norm=1), giving
    max Foot angle acos(sqrt(2/3)) ≈ 35.26°, NOT 45°.

    Q3 (new structural constraint): YES — the bound c_norm <= 1 from
    c_norm = 2*d/(1+d^2) is a structural constraint absent in §19.2. But it
    DISAGREES with empirical c = sqrt(2), so it does NOT bank as a new
    derivation; it functions as evidence that the literal §17.4 sampling reading
    is INCOMPLETE as a route to the Brannen value (it captures the form but not
    the magnitude).

    Status:
    - The two pictures SHARE the modified-Brannen harmonic FORM at tau=0
      (deferent + cosine; no cos3/cos4) — engine-checked by
      mass_measure_from_omega.
    - The two pictures DIFFER on the Brannen c-reach: §19.2 free (INPUT
      sqrt(2)); §17.4 bounded by 1 at lepton boundary.
    - The §17.4 meta-time-phase reidentification (the *which* operator is the
      generation operator) is DERIVED, engine-verified by
      generation_z3_is_metatime_phase. The reading does NOT supply an
      INDEPENDENT geometric derivation of c = sqrt(2); the V_4^perp picture's
      INPUT status of c = sqrt(2) survives the reidentification.

    This sharpens §19.4: the meta-time-phase sampling route is a additional closed
    forcing-route for c = sqrt(2) (after the six listed in §19.4's table); the
    §17.4 reidentification does NOT add a fresh derivation of K = 2/3. The
    'would-change-if' handle: if the sampled amplitude were embedded in a larger
    geometric construction (e.g., adding the e_4-dip even at the lepton
    boundary, or rescaling by an additional V_4^perp factor) that restores the
    c-reach to include sqrt(2), the bridge §17.4 <-> §19.2 at the Koide value
    could close. Until then, the two pictures are bridged at the FORM level
    only.

    OUTCOME: LOCATED-GAP-REFINED.
    """
    import numpy as np

    # The V_4^perp picture: c free, K = (2+c^2)/6 hits 2/3 at c = sqrt(2).
    c_target = math.sqrt(2.0)
    K_v4perp_at_c_sqrt2 = (2.0 + c_target * c_target) / 6.0
    assert abs(K_v4perp_at_c_sqrt2 - 2.0/3.0) < 1e-12, \
        "V_4^perp picture must give K=2/3 at c=sqrt(2)"

    # The §17.4 sampling picture: c_norm = 2d/(1+d^2), max 1 at d=1.
    ds = np.linspace(-5.0, 5.0, 4001)
    c_norms = 2.0 * ds / (1.0 + ds * ds)
    c_norm_max = float(np.max(np.abs(c_norms)))
    assert abs(c_norm_max - 1.0) < 1e-12, \
        "c_norm = 2d/(1+d^2) max must be 1 at d=1"

    # No real d gives c_norm = sqrt(2): discriminant of sqrt(2)*d^2 - 2d + sqrt(2) = 0 is -4.
    disc = 4.0 - 4.0 * math.sqrt(2.0) * math.sqrt(2.0)
    assert disc < 0, "no real d yields c_norm = sqrt(2)"

    # Numerical K-reach: sample tau=0 at several d and psi=delta_L=0.2222.
    psi = 0.2222
    Ks = []
    for d in [0.3, 0.5, 0.7, 0.9, 1.0, 1.1, 1.3, 1.5, 2.0]:
        a = [(d + math.cos(2.0 * math.pi * n / 3.0 - psi)) ** 2
             + math.sin(2.0 * math.pi * n / 3.0 - psi) ** 2
             for n in range(3)]
        m = [ak * ak for ak in a]
        K = sum(m) / (sum(math.sqrt(mk) for mk in m)) ** 2
        Ks.append(K)
    K_max_sampled = max(Ks)
    assert K_max_sampled <= 0.5 + 1e-9, \
        f"§17.4 K-reach must be <= 1/2 at tau=0 (got {K_max_sampled})"
    assert K_max_sampled < 2.0 / 3.0 - 0.05, \
        "K=2/3 must NOT be reached by §17.4 sampling at tau=0"

    # Max Foot angle at K=1/2: cos^2(theta) = 1/(3K) = 2/3, theta = acos(sqrt(2/3)).
    foot_max_at_K_half_deg = math.degrees(math.acos(math.sqrt(2.0 / 3.0)))

    return {
        "v4perp_picture": {
            "formula": "a_k = 1 + c*cos(phi_i - phi_k); c FREE",
            "K_at_c_sqrt2": K_v4perp_at_c_sqrt2,
            "projection_factor": "sqrt(2) = |e_i4^perp|/(e_i4,d) = sqrt(2/3)/(1/sqrt(3))",
            "projection_factor_role": "v_k = d + (c/sqrt(2))*e_hat_k -- makes the Brannen cos-coefficient be c (not c/sqrt(2) or c*sqrt(2))",
        },
        "metatime_sampling_picture": {
            "formula": "a_n = (1+d^2) + 2d*cos(phi_n - psi) at tau=0",
            "c_norm": "c_norm = 2d/(1+d^2)",
            "c_norm_max": c_norm_max,
            "K_cap_at_tau0": 0.5,
            "K_max_sampled_at_psi_eq_deltaL": round(K_max_sampled, 6),
            "discriminant_for_c_norm_eq_sqrt2": disc,
            "foot_max_at_tau0_deg": round(foot_max_at_K_half_deg, 4),
        },
        "shared_structure": (
            "the harmonic FORM at tau=0 (deferent + cosine, no cos3/cos4) -- the modified-Brannen form"
        ),
        "different_structure": (
            "Brannen c-reach: V_4^perp free (INPUT to sqrt(2)); metatime bounded by 1 at tau=0"
        ),
        "Q1_projection_forced_sqrt2_in_metatime": (
            "NO -- §17.4 has no sqrt(2) projection factor; d is the orbit-offset, "
            "c_norm = 2d/(1+d^2) is the orbit-offset ratio bounded by 1"
        ),
        "Q2_foot_45deg_in_metatime_at_tau0": (
            "NO -- max Foot at K=1/2 is acos(sqrt(2/3)) ~ 35.26deg, NOT 45deg"
        ),
        "Q3_new_constraint": (
            "c_norm <= 1 at tau=0 is a structural BOUND not present in §19.2, but it "
            "DISAGREES with empirical c=sqrt(2); functions as evidence the literal §17.4 "
            "sampling reading is INCOMPLETE as a route to the Brannen value"
        ),
        "role_in_§19.4_forcing_table": (
            "a STRUCTURAL INCOMPLETENESS at the lepton boundary tau=0 (c_norm capped at 1, c=sqrt(2) unreachable) — meta-time-phase sampling at "
            "lepton boundary tau=0 caps K at 1/2; c=sqrt(2) is structurally unreachable. "
            "The six §19.4 routes (parametric drive, generic dynamics, BPS, chiral standing-"
            "wave, wavefront-null, topological/Hopf) plus this seventh remain all NEGATIVE"
        ),
        "would_change_if": (
            "the §17.4 sampling were embedded in a larger geometric construction (extra "
            "V_4^perp rescaling, or e_4-dip even at the lepton boundary) that restored the "
            "c-reach to include sqrt(2)"
        ),
        "verdict": (
            "LOCATED-GAP-REFINED -- two pictures bridge at the harmonic FORM, diverge at "
            "the Brannen VALUE; the §17.4 reidentification does NOT add a fresh derivation "
            "of K=2/3; INPUT status of c=sqrt(2) survives."
        ),
        "remaining_closure_route": (
            "§9.6 driven-dissipative kernel + vortex-worldsheet "
            "convolution producing the (19/2)sqrt(38) ratio."
        ),
    }


# =============================================================================
# V2 §3.2 systematic application audit — §26.4 path (vi) sweep (2026-06-30)
# =============================================================================
# Bank the audit OUTCOME as an engine-checkable primitive (canon §10): a
# confirmed 'still FRAMING after V2 §3.2 audit' is a banking-worthy result per
# canon §4; an audit-record primitive lets the harness self-detect drift if
# any of these residuals are later promoted (the counts will need to update).

def v2_section_3_2_audit_log() -> dict:
    """[FRAMING — audit-record primitive; banking-worthy per canon §4]
    §26.4 path (vi): V2 §3.2 SYSTEMATIC AUDIT sweep across engine FRAMING/CANDIDATE
    primitives, asking whether the matter-as-defect + spatial<->meta-time-rotor I_4
    Hodge coupling now FORCES any previously-asserted result.

    PRECEDENT (5 V2 §3.2 unblockings explicitly named in §26.4):
      * M-4              — Q_u/Q_d charge-split coherence under the SD<->ASD mirror
      * W-LIVE-2 / M-6'  — up=SD chirality identification (V1 FRAMING -> V2 DERIVED)
      * W-LIVE-3         — rich-branch memory kernel chosen (engine fork OPEN, leans hysteretic)
      * W-LIVE-5         — baryon = one circular winding with three orthogonal facets
      * W-LIVE-6         — Willis planetary-gear apparatus removed; V2 §3.2 ontology stands alone

    AUDIT OUTCOME (this pass, 2026-06-30) — TWO BANKED FINDINGS:

    *** FINDING 1 — A SIXTH V2 §3.2 UNBLOCKING HAS ALREADY LANDED (audit recognizes,
    does not derive). ***  The Born projection subspace §14.4 was previously tagged
    in V1 as 'the complex structure of the wavefront-Schrödinger sector' — partially
    CIRCULAR with §14.2. V2 §3.2's soliton-background ansatz `Psi_def = F(chi) B_a
    s_0 q_h(tau_5)` with a single chosen winding direction `B_a` from the L-orbit
    triplet REPLACES the circular identification with a one-way derivation chain:
        V2 §3.2  ==>  centralizer({e_4, B_a}) within Cl+(4,0) = {1, B}
                 ==>  complex structure (i := B with B^2 = -1)
                 ==>  Born projection
    The engine primitive `born_subspace_one_B_forced` is now DERIVED-A (engine-exact
    centralizer computation; all three L-orbit choices B_a in {e_12, e_13, e_23}
    give the same closed {1, B} subalgebra). V2 paper §14.4 explicitly carries the
    new 'forced by V2 §3.2, not stipulated' framing.
    §26.4 path (vi) currently says 'Five V2 §3.2 unblockings have been banked';
    the correct count is now SIX. W-REVIEW-P10 in the worklist still flags the
    §14.4 deeper derivation as 'a sixth potential V2 unblocking candidate beyond
    W-LIVE-5'; that flag is now ALREADY-LANDED.

    *** FINDING 2 — NO SEVENTH UNBLOCKING THIS PASS (LOCATED-GAP-REFINED). ***
    The 20 FRAMING/CANDIDATE engine primitives (this pass's sweep) categorize as:

      (a) ALREADY-CONSISTENT with V2 §3.2 at current tier:
          matter_stability_outside_frame, equivalence_principle_protection,
          sakharov_xi_minimal_coupling.
      (b) #1-gap-gated (§9.6 dynamics):
          theta_rel_universality_located, eom_constraint_class,
          eom_invariant_variant_audit, eom_compatible_field_forks (additionally
            carries an inline [ASSERTED] for Z3-merge exhaustiveness — labeled),
          protection_mechanism_located, subharmonic_transition_cost,
          cp_chirality_90_120_mismatch, generation_loose_windows_vacuum_relative,
          charge_in_the_window_picture, vacuum_relative_map_and_cp_commensurability,
          gluon_octet_symmetric_space_split.
      (c) L3 deep-gate (texture tetrad):
          texture_metric_candidate, sakharov_induced_gravity,
          gravitating_vacuum_energy, lambda_resolution_structure.
      (d) Ontological consolidation; open residual independent of V2 §3.2:
          generations_dynamical_count_structural,
          baryon_mass_shared_rotor_nonadditive.
    Each was checked under V2 §3.2 + I_4 Hodge coupling; none promote on this pass.

    NAMED BRIEF CANDIDATES (per §26.4 path (vi)):
      * §14.6 spin-statistics (W-LIVE-4): previously audited; the collective coord
        A(t) and meta-time rotor q_h(tau_5) are independent SU(2) actions on the
        same defect, coupling NOT directly forced. Stays 'compatible with, not
        forced in pure SU(2)'.
      * §16.6 L2 mechanism (nu_L2 = 3pi/2; Delta_nu_K = pi - 3 ~ 0.14 anomalous
        vortex dimension): CS at Hopf k=1 gives eta_v^CS = 19/(8 pi) ~ 0.756 — a
        ~5x overshoot of the required 0.14 (engine-verified: 0.7560/0.1416 = 5.34).
        V2 §3.2 supplies the spatial<->meta-time-rotor coupling STRUCTURALLY (the
        two-faces identification) but does NOT supply a reducing factor that scales
        0.756 -> 0.14. Mechanism STAYS unidentified; tag CANDIDATE (paper §16.6
        already).
      * Colour / weak-isospin sector FRAMING: all located-gap or #1-gap-gated;
        no V2 §3.2 forcing.
      * 'ASSERTED' inline tags in substrate dynamics: single instance in
        eom_compatible_field_forks (Z3-merge exhaustiveness); already documented.

    WOULD CHANGE IF: (i) closure of the #1 gap §9.6 driven-dissipative kernel
    reveals a structural coupling beyond §3.2 that promotes a category-(b) item;
    (ii) the texture tetrad (item 16) supplies the L3-deep spin-connection that
    promotes category-(c) items; (iii) a new ontology extension beyond V2 §3.2
    (e.g. a §3.4 wave-drive refinement) supplies forcing for category-(d).

    NET. Six V2 §3.2 unblockings now banked (including the §14.4 sixth recognized
    here); the seventh is not §3.2-reachable on the current substrate map.

    Tier: FRAMING (audit record). The audit OUTCOME is banking-worthy per canon §4.
    This primitive does NOT derive anything new; it RECORDS the sweep outcome and
    the recognized sixth unblocking, neither of which the engine harness can
    self-detect without an explicit primitive.

    self-check: 20 engine FRAMING/CANDIDATE primitives swept, 4 categories cover
    them exhaustively; 5 prior + 1 newly-recognized sixth = 6 total banked."""
    n_audited = 20
    n_promotions_this_pass = 0
    n_recognized_already_landed = 1
    n_prior_unblockings = 5
    n_total_unblockings = n_prior_unblockings + n_recognized_already_landed
    out = {
        "n_engine_framings_swept": n_audited,
        "n_promotions_derived_this_pass": n_promotions_this_pass,
        "n_unblockings_recognized_already_landed_this_pass": n_recognized_already_landed,
        "n_prior_named_unblockings": n_prior_unblockings,
        "n_total_banked_unblockings": n_total_unblockings,
        "named_unblockings": [
            "M-4 (Q_u/Q_d charge-split coherence under SD<->ASD mirror)",
            "W-LIVE-2 / M-6' (up=SD chirality identification)",
            "W-LIVE-3 (rich-branch memory kernel)",
            "W-LIVE-5 (baryon = one circular winding with three orthogonal facets)",
            "W-LIVE-6 (Willis gear retired; V2 §3.2 ontology stands alone)",
            "RECOGNIZED-HERE: §14.4 Born subspace = centralizer({e_4, B_a}) within Cl+(4,0); "
            "engine `born_subspace_one_B_forced` DERIVED-A; W-REVIEW-P10 'sixth candidate' "
            "is ALREADY-LANDED in V2 paper + engine, not a future task",
        ],
        "category_a_already_consistent": [
            "matter_stability_outside_frame",
            "equivalence_principle_protection",
            "sakharov_xi_minimal_coupling",
        ],
        "category_b_one_gap_gated": [
            "theta_rel_universality_located",
            "eom_constraint_class",
            "eom_invariant_variant_audit",
            "eom_compatible_field_forks",
            "protection_mechanism_located",
            "subharmonic_transition_cost",
            "cp_chirality_90_120_mismatch",
            "generation_loose_windows_vacuum_relative",
            "charge_in_the_window_picture",
            "vacuum_relative_map_and_cp_commensurability",
            "gluon_octet_symmetric_space_split",
        ],
        "category_c_L3_deep_gate": [
            "texture_metric_candidate",
            "sakharov_induced_gravity",
            "gravitating_vacuum_energy",
            "lambda_resolution_structure",
        ],
        "category_d_ontology_consolidation": [
            "generations_dynamical_count_structural",
            "baryon_mass_shared_rotor_nonadditive",
        ],
        "named_brief_candidates_outcome": {
            "section_14_6_spin_statistics_W_LIVE_4":
                "previously audited (W-LIVE-4); stays 'compatible-with-not-forced'",
            "section_16_6_L2_mechanism":
                "CS overshoot ~5.34x (eta_v^CS = 0.756 vs required Delta_nu_K = pi-3 = 0.142); "
                "V2 §3.2 supplies no reducing factor; mechanism stays CANDIDATE",
            "colour_weak_isospin_FRAMING":
                "all located-gap or #1-gap-gated; no V2 §3.2 forcing",
            "ASSERTED_substrate_dynamics_inline":
                "single inline [ASSERTED] in eom_compatible_field_forks (Z3-merge "
                "exhaustiveness); already labeled honestly",
        },
        "would_change_if":
            "(i) #1-gap closure (§9.6 kernel) supplies a category-(b) coupling beyond §3.2; "
            "(ii) texture tetrad (item 16) supplies the L3-deep coupling for category-(c); "
            "(iii) a §3.x ontology extension supplies forcing for (d).",
        "owed_documentation_updates": [
            "V2 paper §26.4 path (vi): 'Five V2 §3.2 unblockings' -> 'Six', name §14.4",
            "V2 paper §26.5: 'five structural unblockings' -> 'six structural unblockings'",
            "Worklist W-REVIEW-P10: mark ALREADY-LANDED (engine-banked + paper-installed)",
        ],
        "verdict":
            "LOCATED-GAP-REFINED per canon §4: sweep produced (a) RECOGNITION that the "
            "§14.4 Born-subspace unblocking is the sixth V2 §3.2 unblocking, already "
            "landed in engine + paper but uncounted in §26.4; (b) NO seventh promotion "
            "this pass — the remaining FRAMING/CANDIDATE residuals are dynamics- or "
            "deep-gate-gated.",
        "tier": "FRAMING (audit record); banking-worthy per canon §4",
    }
    n_categorized = (len(out["category_a_already_consistent"])
                     + len(out["category_b_one_gap_gated"])
                     + len(out["category_c_L3_deep_gate"])
                     + len(out["category_d_ontology_consolidation"]))
    assert n_categorized == n_audited, f"category coverage mismatch: {n_categorized} != {n_audited}"
    assert n_total_unblockings == 6
    assert n_promotions_this_pass == 0
    assert n_recognized_already_landed == 1
    assert len(out["named_unblockings"]) == n_total_unblockings
    return out


# ======================================================================
# ADJUDICATION CONSOLIDATED BANK — chunk 2 (2026-08-12)
# ======================================================================
# Source: knowledge/candidates/probes_2026-08-02/ADJUDICATION_2026-08-03.md
# (governing record of probes 1/2/2b/3/3b; "Bankable now as DERIVED-A" items
# 1-5 and 8) and ADJUDICATION2_2026-08-03.md ("What SURVIVES" item 1).
# Four primitives (+ helpers _a1_*):
#   A12-1 conjugating_extension_omega_identities — probe-1 Omega-identities
#         (items 1-3: |Om4| = k4/2 one-sided; conjugating Om4 closed form +
#         the CORRECTED vanishing locus; <AXA~>_0 = <X>_0; Q-span preservation)
#   A12-2 alpha_family_parallelogram_law        — items 3-4 (same-axis composite
#         == alpha family; Delta_kin closed form; argmin = 1/2; retractions carried)
#   A12-3 ecarrier_matched_defect_hblock_null   — item 8 (E-carrier h == 0 exact;
#         the reverse-is-not-inverse trap; ruling-R1 h-null consonance leg)
#   A12-4 lambda_perp_anw_half_theta            — ADJUDICATION2 item 1 (Lambda_perp
#         density closed form; Lambda_perp = (1/2) Theta_ANW; Lambda = 32.1561;
#         ANW-reproduction certificate)
# Probe provenance (documentation only; every check is self-contained):
# h0k_variational_probe1.py, carrier_probe2.py, carrier_probe2b_Ecarrier.py,
# probe4_two_ladders.py.
# ======================================================================


def _a1_g0(X):
    """Helper: scalar-grade coefficient of an MV, as a float."""
    return float(dict(X.terms).get((), 0.0))


def _a1_maxcoeff(X):
    """Helper: coefficient-level magnitude max|c| over the blades of X.
    NOT nrm2 of a difference: MV.from_dict prunes coefficients below 1e-12,
    so the norm of a small difference multivector can collapse to exactly 0
    — a vacuous metric (the probe-1 live catch)."""
    return max((abs(c) for c in dict(X.terms).values()), default=0.0)


def _a1_coeffdiff(A, B):
    """Helper: float-level per-blade max |a - b| over the union of blades of
    A and B (the subtraction happens in Python floats, never inside MV
    arithmetic, so MV pruning cannot mask a real disagreement)."""
    da, db = dict(A.terms), dict(B.terms)
    return max((abs(da.get(k, 0.0) - db.get(k, 0.0))
                for k in set(da) | set(db)), default=0.0)


def _a1_nrm2(X):
    """Helper: <X X~>_0 (use only on O(1) objects, never on small differences)."""
    return _a1_g0(X * X.reverse())


def _a1_comm(A, B):
    return A * B - B * A


def _a1_qhat(v):
    """Helper: the Q-blade unit direction v -> v1*e14 + v2*e24 + v3*e34."""
    return float(v[0]) * e(1, 4) + float(v[1]) * e(2, 4) + float(v[2]) * e(3, 4)


def _a1_expu(u, half):
    """Helper: exp(u*half) for u^2 = -1."""
    import math as _m
    return _m.cos(half) * SCALAR + _m.sin(half) * u


def _a1_hedgehog(x, f, fp):
    """Helper: B=1 Q-orbit hedgehog at the point x (3-seq) with profile VALUE f
    and derivative fp at r = |x|. Returns (R_h, [o_1, o_2, o_3]) with the
    corpus's analytic MC decomposition o_k = (d_k f) n + s c (d_k n) - s^2 n (d_k n)
    (texture_matter_gravity_coupling form; FD-verified in probes 1/2/4)."""
    import math as _m
    r = _m.sqrt(x[0] ** 2 + x[1] ** 2 + x[2] ** 2)
    n = (x[0] / r, x[1] / r, x[2] / r)
    s, c = _m.sin(f), _m.cos(f)
    nmv = _a1_qhat(n)
    Rh = c * SCALAR + s * nmv
    o = []
    for k in range(3):
        dkn = [((1.0 if i == k else 0.0) - n[i] * n[k]) / r for i in range(3)]
        dmv = _a1_qhat(dkn)
        o.append((fp * n[k]) * nmv + (s * c) * dmv - (s * s) * (nmv * dmv))
    return Rh, o


def conjugating_extension_omega_identities():
    """[DERIVED-A] The Omega-identities of the R-128 mass-lock extensions over
    the B=1 Q-orbit hedgehog — probe 1's exact algebra, banked per
    ADJUDICATION_2026-08-03 items 1-3 with the corrected vanishing locus.
    Lock axis u = I4*Qhat(a), k4 = omega/c_meta.

    FACTS (all engine-checked here, coefficient-level):
      (1) ONE-SIDED extensions (rigid R_h(x)*exp(u k4 x4/2) and co-rotating
          R_h(x)*exp(u(x) k4 x4/2), u(x) = I4*Qhat(rhat)): |Omega_4| = k4/2
          everywhere, exactly (Omega_4 = (k4/2)u resp. (k4/2)u(x); FD-verified).
      (2) CONJUGATING extension R = A(x4) R_h A(x4)~, A = exp(u k4 x4/2):
          Omega_4 = (k4/2)(R^-1 u R - u), FD-verified, with the closed magnitude
          |Omega_4|^2 = k4^2 sin^2 f (1 - (n.a)^2) — hence the VANISHING LOCUS is
          {sin f = 0} UNION {n = +/- a, the whole lock-axis ray}. THE CORRECTION
          BANKED (reviewer P1-1): the probe memo's 'core and infinity' gloss was
          INCOMPLETE — the lock-axis ray vanishes at every radius too.
      (3) <A X A~>_0 = <X>_0 for ANY rotor A (cyclic scalar-grade identity):
          the conjugating class is invisible to the observer's scalar
          (mass-line) quadrature identically — R-127's mass phase cannot live on
          a purely conjugating extension.
      (4) Conjugation by exp(u theta/2), u = I4*Qhat(a), preserves the Q-blade
          span: A Qhat(n) A~ has NO coefficient outside {e14, e24, e34}, so the
          conjugated hedgehog rotor A R_h A~ stays in span{1, Q-blades} and its
          u-blade (L-orbit) coefficient is exactly absent.
    FENCES: kinematic identities of the named extension families only — no cost
    hierarchy, no vacuum-branch selection here (probe 1's cost table F-2/F-3 is
    conditional on the static-vacuum premise and is NOT banked by this entry);
    uniqueness of the conjugating class is banked ONLY within the global
    two-sided family L(x4) R_h M(x4) up to a constant rotor (item 2 scope — the
    'unique finite-cost family' headline was over-broad and is not asserted).
    Zero-checks sit below the MV pruning floor (1e-12): certified jointly by the
    float-level per-blade metric and the closed-form magnitude in (2)."""
    # runtime: ~0.1s
    import math as _m
    import random as _rd

    K4 = 0.8317                      # probe value; identities are k4-independent
    AXIS = (0.0, 0.0, 1.0)
    U = I4 * _a1_qhat(AXIS)
    rng = _rd.Random(20260812)

    def _prof(r):
        return _m.pi * _m.exp(-r), -_m.pi * _m.exp(-r)

    def _Rfull(ext, x, x4):
        r = _m.sqrt(x[0] ** 2 + x[1] ** 2 + x[2] ** 2)
        f, _ = _prof(r)
        Rh, _o = _a1_hedgehog(x, f, 0.0)
        if ext == "rigid":
            return Rh * _a1_expu(U, K4 * x4 / 2)
        if ext == "corot":
            n = (x[0] / r, x[1] / r, x[2] / r)
            return Rh * _a1_expu(I4 * _a1_qhat(n), K4 * x4 / 2)
        A = _a1_expu(U, K4 * x4 / 2)
        return A * Rh * A.reverse()

    def _Om4_fd(ext, x, x4, d=1e-6):
        R = _Rfull(ext, x, x4)
        return R.reverse() * ((1.0 / (2 * d)) * (_Rfull(ext, x, x4 + d)
                                                 - _Rfull(ext, x, x4 - d)))

    # --- (1) + (2): FD vs closed forms at seeded generic points
    worst_fd = {"rigid": 0.0, "corot": 0.0, "conj": 0.0}
    worst_norm = 0.0
    for _ in range(8):
        x = tuple(rng.uniform(-2.2, 2.2) for _ in range(3))
        r = _m.sqrt(sum(c * c for c in x))
        if r < 0.35:
            continue
        x4 = rng.uniform(-3.0, 3.0)
        n = (x[0] / r, x[1] / r, x[2] / r)
        # rigid / corot analytic Omega_4
        for ext, uax in (("rigid", U), ("corot", I4 * _a1_qhat(n))):
            ana = (K4 / 2) * uax
            worst_fd[ext] = max(worst_fd[ext],
                                _a1_coeffdiff(_Om4_fd(ext, x, x4), ana))
            worst_norm = max(worst_norm,
                             abs(_a1_nrm2(ana) * 4.0 / K4 ** 2 - 1.0))
        # conjugating closed form (k4/2)(R^-1 u R - u), R the full configuration
        R = _Rfull("conj", x, x4)
        ana = (K4 / 2) * (R.reverse() * U * R - U)
        worst_fd["conj"] = max(worst_fd["conj"],
                               _a1_coeffdiff(_Om4_fd("conj", x, x4), ana))
    assert all(1e-13 < v < 5e-8 for v in worst_fd.values()), \
        "analytic Omega_4 must match FD at FD-noise level (0.0 would be vacuous)"
    assert worst_norm < 1e-14, "one-sided |Omega_4| = k4/2 must be exact"

    # --- (2) locus certificate, parametric in (f, n) at x4 = 0 (A = 1 there;
    #     the FD check above already covers x4 != 0)
    def _Om4_conj_param(f, n):
        Rh = _m.cos(f) * SCALAR + _m.sin(f) * _a1_qhat(n)
        return (K4 / 2) * (Rh.reverse() * U * Rh - U)

    NGEN = [(0.6, 0.0, 0.8), (0.0, 1.0, 0.0),
            (0.5345224838248488, 0.2672612419124244, 0.8017837257372732),
            (0.1, 0.0, 0.99498743710662)]          # incl. a near-axis direction
    FGEN = (0.4, 1.2, 2.7)
    on_locus = 0.0
    for f in (0.0, _m.pi):                          # sin f = 0
        for n in NGEN:
            on_locus = max(on_locus, _a1_maxcoeff(_Om4_conj_param(f, n)))
    for f in FGEN:                                  # the whole lock-axis ray
        for n in ((0.0, 0.0, 1.0), (0.0, 0.0, -1.0)):
            on_locus = max(on_locus, _a1_maxcoeff(_Om4_conj_param(f, n)))
    off_locus_min, mag_dev = float("inf"), 0.0
    for f in FGEN:
        for n in NGEN:
            O = _Om4_conj_param(f, n)
            d = n[2]                                # n . a with a = e_z
            mag_dev = max(mag_dev, abs(_a1_nrm2(O)
                          - K4 ** 2 * _m.sin(f) ** 2 * (1 - d * d)))
            off_locus_min = min(off_locus_min, _a1_maxcoeff(O))
    assert on_locus < 1e-14, "Omega_4 must vanish on {sin f = 0} U {n = +/- a}"
    assert mag_dev < 1e-13, "|Omega_4|^2 = k4^2 sin^2 f (1 - (n.a)^2) exact"
    assert off_locus_min > 1e-3, "Omega_4 must be visibly nonzero off the locus"

    # --- (3) <A X A~>_0 = <X>_0 for rotors A, X random over all 16 Cl(4,0) blades
    import itertools as _it
    blades = [e(*idx) if idx else SCALAR
              for g in range(5) for idx in _it.combinations(range(1, 5), g)]
    worst_scalar = 0.0
    for _ in range(6):
        A = (_a1_expu(e(1, 2), rng.uniform(-2, 2))
             * _a1_expu(e(1, 4), rng.uniform(-2, 2))
             * _a1_expu(e(2, 3), rng.uniform(-2, 2)))
        X = 0.0 * SCALAR
        for B in blades:
            X = X + rng.uniform(-1, 1) * B
        worst_scalar = max(worst_scalar,
                           abs(_a1_g0(A * X * A.reverse()) - _a1_g0(X)))
    assert worst_scalar < 1e-12, "<A X A~>_0 = <X>_0 for rotors"

    # --- (4) Q-span preservation + u-blade coefficient exactly absent
    QKEYS = {(1, 4), (2, 4), (3, 4)}
    worst_leak = 0.0
    worst_ublade = 0.0
    for _ in range(6):
        a = [rng.gauss(0, 1) for _ in range(3)]
        na = _m.sqrt(sum(c * c for c in a)); a = [c / na for c in a]
        nn = [rng.gauss(0, 1) for _ in range(3)]
        nb = _m.sqrt(sum(c * c for c in nn)); nn = [c / nb for c in nn]
        ua = I4 * _a1_qhat(a)
        A = _a1_expu(ua, rng.uniform(-2, 2))
        img = A * _a1_qhat(nn) * A.reverse()
        worst_leak = max(worst_leak,
                         max((abs(c) for k, c in dict(img.terms).items()
                              if k not in QKEYS), default=0.0))
        f = rng.uniform(0.3, 2.8)
        Rc = A * (_m.cos(f) * SCALAR + _m.sin(f) * _a1_qhat(nn)) * A.reverse()
        dr = dict(Rc.terms)
        worst_ublade = max(worst_ublade,
                           max((abs(dr.get(k, 0.0)) for k in dict(ua.terms)),
                               default=0.0))
        worst_leak = max(worst_leak,
                         max((abs(c) for k, c in dr.items()
                              if k not in QKEYS and k != ()), default=0.0))
    assert worst_leak < 1e-14, "conjugation must preserve the Q-blade span"
    assert worst_ublade < 1e-14, "u-blade coefficient of A R_h A~ exactly absent"

    return {
        "tier": "DERIVED-A",
        "one-sided |Om4| = k4/2 (worst |4|Om4|^2/k4^2 - 1|)": worst_norm,
        "FD vs analytic Om4, worst coeff (rigid, corot, conj)": (
            worst_fd["rigid"], worst_fd["corot"], worst_fd["conj"]),
        "conj Om4 on the locus {sin f = 0} U {n = +/- a} (worst coeff)": on_locus,
        "conj |Om4|^2 = k4^2 sin^2 f (1-(n.a)^2) (worst dev)": mag_dev,
        "conj Om4 off-locus visibility (min maxcoeff)": off_locus_min,
        "<A X A~>_0 - <X>_0 (worst)": worst_scalar,
        "Q-span leak under conjugation (worst coeff)": worst_leak,
        "u-blade coefficient of A R_h A~ (worst)": worst_ublade,
        "locus correction": ("'core and infinity' gloss INCOMPLETE — the whole "
                             "lock-axis ray n = +/- a vanishes too (ADJUDICATION_"
                             "2026-08-03 item 1, reviewer P1-1)"),
        "fence": ("kinematic identities only; cost table / vacuum-branch NOT "
                  "banked; two-sided uniqueness only within L(x4) R_h M(x4) up "
                  "to a constant rotor"),
    }


def alpha_family_parallelogram_law():
    """[DERIVED-A] The alpha-family (carrier-phase split) cost algebra — probe 2's
    corrected claim set, banked per ADJUDICATION_2026-08-03 items 3-4. Family:
    R_alpha = L(x4) R_h(x) M(x4), L = exp(u_c a th/2), M = exp(u_c (1-a) th/2),
    th = k_c x4, on the carrier R_vac = exp(u_c k_c x4/2), u_c = I4*Qhat(a_c).

    FACTS (all engine-checked here, coefficient-level / pointwise):
      (1) SAME-AXIS COMPOSITE IS NOT A NEW FAMILY: A R_h A~ q_c with
          A = exp(u_c dk x4/2) equals the alpha family at a = dk/k_c POINTWISE
          exactly — the same-axis internal rotation is a REPARAMETRIZATION of
          the carrier-phase split, not a mass-differentiation dial.
      (2) THE PARALLELOGRAM LAW (closed form, pointwise exact):
              Delta_kin = -2 a (1-a) (1-c) (k_c/2)^2 c_2,
          c = <R_h~ u_c R_h u_c~>_0, with c ALPHA-INDEPENDENT (extracted-c
          spread across alpha ~1e-15 here; the adjudication's check: 1e-16).
          Cross-link: 1 - c =
          2 sin^2 f (1 - (n.a_c)^2) — the SAME object as the conjugating
          Omega_4 magnitude (conjugating_extension_omega_identities fact 2).
      (3) ARGMIN = 1/2, FORCED: both cost sectors are pointwise x4-independent,
          pointwise QUADRATIC in alpha with non-negative curvature (convex),
          and pointwise SYMMETRIC under alpha <-> 1-alpha; symmetry + convexity
          force argmin = 1/2, and sector-wise minimization makes the argmin
          c4/c2-INDEPENDENT (both sectors minimized at 1/2 — any non-negative
          coupling pair inherits it).
    RETRACTIONS CARRIED (ADJUDICATION_2026-08-03 item 4 — the corrected record):
      * The 'wall kinetic deficit drives it' attribution was WRONG — at the
        probe couplings (c2, c4) = (1, 0.25) the QUARTIC sector supplies 53.5%
        of the alpha-dependence; the kinetic dip is not the driver.
      * The probe-2 script line asserting 'matter as a hole ... computed' is
        RETRACTED. The total carrier-relative density is a LARGE POSITIVE
        EXCESS; the Om_4-kinetic sub-term dips only ~0.1% below the carrier in
        probe 2's P1 table (wall-point witness here: dip = 2% of the local
        excess, sign facts asserted).
        The genuinely hole-shaped computed fact is the AMPLITUDE NOTCH: the
        observer-line projection |z| drops from 1.000 (vacuum) to 0.384 at the
        wall AT THE CARRIER'S OWN PHASE. Canon sec. 0's fence applies: the
        hole is an image, never a load-bearing premise.
    FENCE: the carrier premise itself stays H8-licensed / sec. 9.6-GATED in
    value (axis, omega_c, scale); these are exact algebraic facts OF the named
    family, not a carrier-value claim."""
    # runtime: ~0.15s
    import math as _m
    import random as _rd

    K_C = 0.8317
    C2 = 1.0
    U_C = I4 * _a1_qhat((0.0, 0.0, 1.0))
    rng = _rd.Random(20260803)

    def _prof(r):
        return _m.pi * _m.exp(-r), -_m.pi * _m.exp(-r)

    def _rh_o(x):
        r = _m.sqrt(sum(c * c for c in x))
        f, fp = _prof(r)
        return _a1_hedgehog(x, f, fp)

    def _R_alpha(x, x4, a):
        Rh, _ = _rh_o(x)
        th = K_C * x4
        return _a1_expu(U_C, a * th / 2) * Rh * _a1_expu(U_C, (1 - a) * th / 2)

    def _Om_alpha(x, x4, a):
        Rh, o = _rh_o(x)
        th = K_C * x4
        M = _a1_expu(U_C, (1 - a) * th / 2)
        Mr = M.reverse()
        X = Mr * (Rh.reverse() * U_C * Rh) * M
        return ([Mr * ok * M for ok in o]
                + [(a * K_C / 2) * X + ((1 - a) * K_C / 2) * U_C])

    def _sectors(Om):
        e2 = sum(_a1_nrm2(ok) for ok in Om)
        e4 = sum(_a1_nrm2(_a1_comm(Om[i], Om[j]))
                 for i in range(4) for j in range(i + 1, 4))
        return e2, e4

    def _rand_pt():
        while True:
            x = tuple(rng.uniform(-2.2, 2.2) for _ in range(3))
            if _m.sqrt(sum(c * c for c in x)) > 0.4:
                return x

    # --- P0 discipline: one FD spot-check of the analytic Omegas
    x0, x40, a0 = _rand_pt(), 0.83, 0.35
    R0 = _R_alpha(x0, x40, a0)
    worst_p0 = 0.0
    d = 1e-6
    for mu in range(4):
        if mu < 3:
            xp = list(x0); xm = list(x0)
            xp[mu] += d; xm[mu] -= d
            dR = (1.0 / (2 * d)) * (_R_alpha(tuple(xp), x40, a0)
                                    - _R_alpha(tuple(xm), x40, a0))
        else:
            dR = (1.0 / (2 * d)) * (_R_alpha(x0, x40 + d, a0)
                                    - _R_alpha(x0, x40 - d, a0))
        worst_p0 = max(worst_p0,
                       _a1_coeffdiff(R0.reverse() * dR, _Om_alpha(x0, x40, a0)[mu]))
    assert 1e-13 < worst_p0 < 5e-8, "alpha-family analytic Omegas vs FD"

    # --- (1) same-axis composite == alpha family, pointwise
    worst_comp = 0.0
    for _ in range(10):
        x = _rand_pt()
        x4 = rng.uniform(-3.0, 3.0)
        dk = rng.uniform(0.1, 0.7)
        Rh, _ = _rh_o(x)
        A = _a1_expu(U_C, dk * x4 / 2)
        Rcomp = A * Rh * A.reverse() * _a1_expu(U_C, K_C * x4 / 2)
        worst_comp = max(worst_comp,
                         _a1_coeffdiff(Rcomp, _R_alpha(x, x4, dk / K_C)))
    assert worst_comp < 1e-13, "same-axis composite must equal the alpha family"

    # --- (2) the parallelogram law + alpha-independence of c + cross-link
    worst_law = 0.0
    worst_cspread = 0.0
    worst_cx = 0.0
    for _ in range(6):
        x = _rand_pt()
        x4 = rng.uniform(-3.0, 3.0)
        Rh, _ = _rh_o(x)
        c = _a1_g0(Rh.reverse() * U_C * Rh * U_C.reverse())
        r = _m.sqrt(sum(v * v for v in x))
        f, _fp = _prof(r)
        nz = x[2] / r
        worst_cx = max(worst_cx,
                       abs((1 - c) - 2 * _m.sin(f) ** 2 * (1 - nz * nz)))
        cs = []
        for a in (0.2, 0.35, 0.5, 0.65, 0.8):
            Om = _Om_alpha(x, x4, a)
            dkin = C2 * (_a1_nrm2(Om[3]) - (K_C / 2) ** 2)
            worst_law = max(worst_law, abs(
                dkin - (-2 * a * (1 - a) * (1 - c) * (K_C / 2) ** 2 * C2)))
            cs.append(1 + dkin / (2 * a * (1 - a) * (K_C / 2) ** 2 * C2))
        worst_cspread = max(worst_cspread, max(cs) - min(cs))
    assert worst_law < 1e-14, "Delta_kin = -2a(1-a)(1-c)(k_c/2)^2 c2 pointwise"
    assert worst_cspread < 1e-13, "c must be alpha-independent"
    assert worst_cx < 1e-13, "1 - c = 2 sin^2 f (1 - (n.a_c)^2) cross-link"

    # --- (3) sector structure: x4-independence, quadraticity, symmetry, convexity
    AGRID = (0.2, 0.35, 0.5, 0.65, 0.8)
    worst_x4 = worst_sym = worst_quad = 0.0
    min_curv2 = min_curv4 = float("inf")
    for _ in range(3):
        x = _rand_pt()
        s1 = [_sectors(_Om_alpha(x, 0.7, a)) for a in AGRID]
        s2 = [_sectors(_Om_alpha(x, 1.9, a)) for a in AGRID]
        for p, q in zip(s1, s2):
            worst_x4 = max(worst_x4, abs(p[0] - q[0]), abs(p[1] - q[1]))
        for sec in (0, 1):
            v = [p[sec] for p in s1]
            worst_sym = max(worst_sym, abs(v[0] - v[4]), abs(v[1] - v[3]))
            # exact quadratic through a = 0.2, 0.5, 0.8 -> predict 0.35, 0.65
            A2 = (v[0] + v[4] - 2 * v[2]) / (2 * 0.3 ** 2)
            A1 = (v[4] - v[0]) / 0.6
            for a, vv in ((0.35, v[1]), (0.65, v[3])):
                pred = v[2] + A1 * (a - 0.5) + A2 * (a - 0.5) ** 2
                worst_quad = max(worst_quad, abs(pred - vv))
            if sec == 0:
                min_curv2 = min(min_curv2, A2)
            else:
                min_curv4 = min(min_curv4, A2)
    assert worst_x4 < 1e-13, "alpha-family sector densities must be x4-independent"
    assert worst_sym < 1e-12, "sectors must be symmetric under alpha <-> 1-alpha"
    assert worst_quad < 1e-12, "sectors must be exactly quadratic in alpha"
    assert min_curv2 >= -1e-12 and min_curv4 >= -1e-12, \
        "sector curvatures must be non-negative (convexity)"

    # --- wall-point witness of the corrected reading (retraction support)
    xw = (0.8, 0.45, 0.35)
    rw = _m.sqrt(sum(v * v for v in xw))
    fw, _ = _prof(rw)
    Rh, _ = _rh_o(xw)
    zs = []
    for i in range(16):
        t = i / 16 * (4 * _m.pi / K_C)
        R = Rh * _a1_expu(U_C, K_C * t / 2)
        zs.append(_m.hypot(_a1_g0(R), _a1_g0(R * U_C.reverse())))
    notch = sum(zs) / len(zs)
    assert max(zs) - min(zs) < 1e-12, "|z| must be cycle-constant"
    assert abs(notch - abs(_m.cos(fw))) < 1e-12, "notch |z| = |cos f| at the wall"
    assert abs(notch - 0.3843) < 5e-4, "the banked 1.000 -> 0.384 notch value"
    Om = _Om_alpha(xw, 0.9, 0.5)
    e2, e4 = _sectors(Om)
    dkin_w = C2 * (_a1_nrm2(Om[3]) - (K_C / 2) ** 2)
    dtot_w = C2 * e2 + 0.25 * e4 - C2 * (K_C / 2) ** 2
    assert dkin_w < 0.0 < dtot_w and abs(dkin_w) < 0.05 * dtot_w, \
        "kinetic dip must be a small negative sub-term inside a positive excess"

    return {
        "tier": "DERIVED-A",
        "alpha-family FD spot-check (worst coeff)": worst_p0,
        "same-axis composite == alpha family (worst coeff)": worst_comp,
        "parallelogram law residual (worst)": worst_law,
        "c alpha-independence (extracted-c spread)": worst_cspread,
        "1-c = 2 sin^2 f (1-(n.a_c)^2) cross-link (worst)": worst_cx,
        "sector x4-independence (worst)": worst_x4,
        "sector alpha<->1-alpha symmetry (worst, pointwise)": worst_sym,
        "sector exact-quadraticity in alpha (worst)": worst_quad,
        "min sector curvatures (quadratic, quartic)": (min_curv2, min_curv4),
        "argmin": "1/2, both sectors, c4/c2-independent (symmetry + convexity)",
        "wall notch |z| (vacuum 1.000 ->)": notch,
        "wall Delta_kin / Delta_total (dip inside positive excess)": (
            dkin_w, dtot_w),
        "retractions": ("'wall kinetic deficit drives it' WRONG (quartic 53.5% "
                        "at probe couplings); 'matter as a hole ... computed' "
                        "RETRACTED — the computed fact is the amplitude notch; "
                        "canon sec. 0 hole-image fence applies"),
    }


def ecarrier_matched_defect_hblock_null():
    """[DERIVED-A] E-carrier h-block null (probe 2b, banked per
    ADJUDICATION_2026-08-03 item 8): under the corpus's own carrier blade
    E = I4*e5 (canon sec. 5; R-147 banks it h-null), the matched defect
    R = R_h(x) * exp(E k_c x4/2) has its ENTIRE 16-entry texture h-block
    h_mu_nu = <Omega_mu I4 Omega_nu>_0 IDENTICALLY ZERO — exact, FD-verified
    with the TRUE inverse. Blade arithmetic: Omega_k = Omega_k^hedgehog (E is
    central, the carrier factor cancels), Omega_4 = (k_c/2)E; then
    h_44 ~ <I4 E^2>_0 = -<I4>_0 = 0, h_4k ~ <(E I4) Omega_k>_0 = 0 (E*I4 is
    grade-1, the product carries grades 1 and 3 only), h_kl = the static
    hedgehog's 0.

    THE TRAP, DOCUMENTED (this probe's own first run failed on it):
    E~ = +E (grade 5), so .reverse() is NOT the inverse for E-content — every
    FD check against an E-carrier must build the true inverse
    (R_h q_E)^-1 = q_E^-1 R_h~ explicitly (engine-witnessed below: q_E~ q_E
    != 1 at O(1), q_E^-1 q_E = 1). Related energetics (banked in
    cl41_pairing_sign_tables): the E-direction has NEGATIVE norm under the
    reverse pairing, <Om_4 Om_4~>_0 = -(k_c/2)^2 (reported below) — the
    REVERSE pairing is INDEFINITE on e5-content, hence its grade-0 is not a
    density there; that is why the positive-definite pairing (iv) was ruled in
    (R-168/RUL-018; under t the same object reads +(k_c/2)^2). [Gloss
    re-worded 2026-08-13 per the K-O1 keeper C2: the earlier "R-127's 'E
    leaves the ideal', as energetics" reading is retired — the exclusion's
    instrument is the pairing-independent e5-content fact; site on RUL-018's
    class-B revert list.]

    RULING-R1 CONSONANCE LEG (2026-08-12): under the ruled positive-definite
    pairing (iv) (cl41_positive_definite_pairing) the carrier is COSTED —
    uniform volume density (k_c/2)^2 — while THIS entry certifies that the
    E-carrier content is TEXTURE-INVISIBLE (h == 0 exactly, R-147 consonant):
    the carrier's volume energy under pairing (iv) carries no h-block, so
    banked texture results are untouched by costing the carrier.
    SUPERSEDED CONTEXT: with R1 adopting pairing (iv), the 2026-08-03 'the
    fork closes the other way and Sakharov stays sole route' sentence is the
    superseded (iii)-branch reading; the h == 0 fact itself is pairing-
    independent and is what this entry banks."""
    # runtime: ~0.1s
    import math as _m
    import random as _rd

    K_C = 0.8317
    E5 = I4 * e(5)                     # E = I4 e5 = e12345, the carrier blade
    rng = _rd.Random(20260812)

    # blade algebra: E^2 = -1, E~ = +E, E central (sample incl. odd blades)
    assert _a1_maxcoeff(E5 * E5 + SCALAR) < 1e-14, "E^2 = -1"
    assert _a1_maxcoeff(E5.reverse() - E5) < 1e-14, "E~ = +E (grade 5)"
    for b in (e(1), e(1, 2), e(1, 4), e(3, 4), e(1, 2, 3), e(2, 5), e(1, 5)):
        assert _a1_maxcoeff(E5 * b - b * E5) < 1e-14, "E central"

    def _qE(x4):
        return _m.cos(K_C * x4 / 2) * SCALAR + _m.sin(K_C * x4 / 2) * E5

    def _qE_inv(x4):
        return _m.cos(K_C * x4 / 2) * SCALAR - _m.sin(K_C * x4 / 2) * E5

    # the trap, engine-witnessed
    trap = _a1_maxcoeff(_qE(1.7).reverse() * _qE(1.7) - SCALAR)
    assert trap > 0.5, "reverse must visibly FAIL as the inverse for E-content"
    assert _a1_maxcoeff(_qE_inv(1.7) * _qE(1.7) - SCALAR) < 1e-14, "true inverse"

    def _prof(r):
        return _m.pi * _m.exp(-r), -_m.pi * _m.exp(-r)

    def _Om_analytic(x):
        r = _m.sqrt(sum(c * c for c in x))
        f, fp = _prof(r)
        _Rh, o = _a1_hedgehog(x, f, fp)
        return o + [(K_C / 2) * E5]

    def _R(x, x4):
        r = _m.sqrt(sum(c * c for c in x))
        f, _ = _prof(r)
        Rh, _o = _a1_hedgehog(x, f, 0.0)
        return Rh * _qE(x4)

    worst_fd = 0.0
    worst_h = 0.0
    pair_dev = 0.0
    d = 1e-6
    for _ in range(10):
        x = tuple(rng.uniform(-2.2, 2.2) for _ in range(3))
        if _m.sqrt(sum(c * c for c in x)) < 0.35:
            continue
        x4 = rng.uniform(-3.0, 3.0)
        Om = _Om_analytic(x)
        # FD with the TRUE inverse
        r = _m.sqrt(sum(c * c for c in x))
        f, _ = _prof(r)
        Rh, _o = _a1_hedgehog(x, f, 0.0)
        Rinv = _qE_inv(x4) * Rh.reverse()
        for mu in range(4):
            if mu < 3:
                xp = list(x); xm = list(x)
                xp[mu] += d; xm[mu] -= d
                dR = (1.0 / (2 * d)) * (_R(tuple(xp), x4) - _R(tuple(xm), x4))
            else:
                dR = (1.0 / (2 * d)) * (_R(x, x4 + d) - _R(x, x4 - d))
            worst_fd = max(worst_fd, _a1_coeffdiff(Rinv * dR, Om[mu]))
        # the h-block: all 16 entries
        for i in range(4):
            for j in range(4):
                worst_h = max(worst_h, abs(_a1_g0(Om[i] * I4 * Om[j])))
        # reverse-pairing negative norm on the carrier direction (cross-ref)
        pair_dev = max(pair_dev, abs(_a1_g0(Om[3] * Om[3].reverse())
                                     + (K_C / 2) ** 2))
    assert 1e-13 < worst_fd < 5e-8, "analytic Omegas vs FD (true inverse)"
    assert worst_h < 1e-15, "the ENTIRE h-block must vanish identically"
    assert pair_dev < 1e-14, "<Om_4 Om_4~>_0 = -(k_c/2)^2 (reverse pairing)"

    return {
        "tier": "DERIVED-A",
        "max |h_mu_nu| over all 16 entries, all points": worst_h,
        "FD vs analytic (TRUE inverse), worst coeff": worst_fd,
        "trap witness maxcoeff(qE~ qE - 1) (reverse fails)": trap,
        "<Om_4 Om_4~>_0 + (k_c/2)^2 (negative norm, cross-ref)": pair_dev,
        "ruling_R1_consonance": ("h-null leg of the 2026-08-12 R1 package: "
                                 "carrier volume energy under pairing (iv) is "
                                 "texture-invisible (E-content h == 0, R-147)"),
        "trap": "E~ = +E (grade 5): reverse is NOT the inverse for E-content",
    }


# ======================================================================
# TAU5 ADJUDICATION BANK (2026-08-13)
# ======================================================================
# Source: knowledge/candidates/probes_2026-08-13/TAU5_ADJUDICATION_2026-08-13.md
# (GOVERNING record of the tau5-hyperbolic collective-coordinate round; banking
# triage feed item (b)). Two primitives, reusing the _a1_* helpers above:
#   T5-1 one_sided_rotor_uniform_density_identity — the one-sided uniform
#        kinetic-density identity (BOTH one-sided forms) + the conjugation-
#        subtraction identity (the field-level subtraction, keeper fact 2)
#   T5-2 tau5_unique_v_inert_combination — the b = -a lemma (I-C is the unique
#        v-inert far-field combination; reviewer N-5)
# Ledger descendant: N61 (the discrimination-null negative). Round scripts:
# tau5_probe1_collective_coordinate.py (probe dir; every check below is
# self-contained and does not import them).
# ======================================================================


def one_sided_rotor_uniform_density_identity():
    """[DERIVED-A] THE ONE-SIDED UNIFORM KINETIC-DENSITY IDENTITY (tau5
    adjudication 2026-08-13, three-way convergent root; N61). For the banked
    one-sided mass-rotor rest form (R-125 class) with w_hat = u_hat*omega/2:

      LEFT  form R = Q(tau5) R0(x):  Omega_5 = R0~ w_hat R0   (the A1 identity)
      RIGHT form R = R0(x) Q(tau5):  Omega_5 = w_hat           (identically)

    and in BOTH cases the kinetic density <Omega_5 t(Omega_5)>_0 equals
    (omega/2)^2 |u_hat|^2 at EVERY point — exactly uniform, profile-independent
    (checked on two distinct profiles), u_hat-independent in value. On this
    Cl+(4,0) grade-2 content the ruled pairing (iv) coincides with the reverse
    pairing (alpha_5 trivial without e5), so this IS the ruled-cost kinetic
    density. THE FACT IS ONE-SIDEDNESS, NOT THE LEFT SHIFT (keeper engine fact
    1: the right-multiplication form gives the same uniform density) — the
    one-sided rotor does not tend to the static vacuum at infinity (Omega_5 ->
    w_hat != 0), so ANY positive-definite pairing yields a positive limit
    density and the raw 3-slice kinetic cost diverges AT REST: the standard
    vacuum-stabilizer obstruction to treating a broken-symmetry direction as a
    collective coordinate (Adkins-Nappi-Witten 1983; Coleman 1985 — credit via
    import I-5 context). Spin(4)-invariance of the pairing buys the exact
    UNIFORMITY (left form); positivity + the boundary condition buy the
    divergence.

    THE CONJUGATION-SUBTRACTION IDENTITY (keeper engine fact 2, exact): for the
    two-sided (conjugation / spin-class) rotation R = A(tau5) R0 A~(tau5),

        Omega_5(conj) = A (Omega_5(left) - w_hat) A~     EXACTLY,

    so the conjugation class is the left-shift class MINUS ITS OWN ASYMPTOTE,
    conjugated — i.e. the FIELD-LEVEL version of the subtraction the ruled cost
    convention performs at the density level (R-130's F2 excess factorization
    is the same move on the mode; the map between the two subtraction LEVELS is
    the open O1 gap of the adjudication). Its density decays iff R0 -> 1
    (checked: ~1e-10 by r = 12 on the witness profile, vs the one-sided form's
    exact (omega/2)^2 there).

    Checks below are non-vacuous: FD-vs-analytic at coefficient level (never
    nrm2 of a small difference), uniformity across radii x directions x u_hat
    x profiles, the omega^2 value, the conjugation identity at three radii,
    and the decay dichotomy."""
    import math as _m
    w = 0.83
    profiles = [
        (lambda r: _m.pi * _m.exp(-r), lambda r: -_m.pi * _m.exp(-r)),
        (lambda r: _m.pi / (1.0 + r * r), lambda r: -2 * _m.pi * r / (1 + r * r) ** 2),
    ]
    # FD step 1e-4, NOT smaller: at r = 12 the profile components are ~2e-5 and a
    # 1e-6 step pushes their FD differences below the MV ~1e-12 prune floor,
    # which silently zeroes them and corrupts the quotient (the canon's
    # prune-vs-FD trap, caught live on this primitive's first run).
    d = 1e-4
    worst_left = worst_right = worst_unif = worst_conj = 0.0
    for u in (e(1, 2), e(3, 4)):
        what = (w / 2.0) * u
        for (f, fp) in profiles:
            for x in ((0.3, 0.2, 0.25), (0.9, -0.6, 0.4), (2.5, 2.0, 2.4),
                      (12.0, 0.3, 0.2)):
                r = _m.sqrt(x[0] ** 2 + x[1] ** 2 + x[2] ** 2)
                R0, _o = _a1_hedgehog(x, f(r), fp(r))
                # LEFT: FD on Q(t5) R0 vs the analytic R0~ w_hat R0
                Q = lambda t5: _a1_expu(u, w * t5 / 2.0)
                Om5L_fd = (Q(0.1) * R0).reverse() * (
                    (1 / (2 * d)) * (Q(0.1 + d) * R0 - Q(0.1 - d) * R0))
                Om5L = R0.reverse() * what * R0
                worst_left = max(worst_left, _a1_coeffdiff(Om5L_fd, Om5L))
                # RIGHT: FD on R0 Q(t5) vs w_hat identically
                Om5R_fd = (R0 * Q(0.1)).reverse() * (
                    (1 / (2 * d)) * (R0 * Q(0.1 + d) - R0 * Q(0.1 - d)))
                worst_right = max(worst_right, _a1_coeffdiff(Om5R_fd, what))
                # UNIFORMITY + VALUE, both forms (nrm2 on O(1) objects only)
                for Om in (Om5L, what):
                    worst_unif = max(worst_unif,
                                     abs(_a1_nrm2(Om) - (w / 2.0) ** 2))
    # conjugation-subtraction identity + decay dichotomy (witness profile)
    f, fp = profiles[0]
    u = e(1, 2)
    what = (w / 2.0) * u
    for x in ((0.5, 0.2, 0.1), (2.0, 0.5, 0.4), (6.0, 0.3, 0.2)):
        r = _m.sqrt(x[0] ** 2 + x[1] ** 2 + x[2] ** 2)
        R0, _o = _a1_hedgehog(x, f(r), fp(r))
        A = lambda t5: _a1_expu(u, w * t5 / 2.0)
        Rc = lambda t5: A(t5) * R0 * A(t5).reverse()
        Om5c_fd = Rc(0.0).reverse() * ((1 / (2 * d)) * (Rc(d) - Rc(-d)))
        Om5c = A(0.0) * (R0.reverse() * what * R0 + (-1.0) * what) * A(0.0).reverse()
        worst_conj = max(worst_conj, _a1_coeffdiff(Om5c_fd, Om5c))
    x12 = (12.0, 0.3, 0.2)
    r12 = _m.sqrt(x12[0] ** 2 + x12[1] ** 2 + x12[2] ** 2)
    R0, _o = _a1_hedgehog(x12, f(r12), fp(r12))
    dens_conj_12 = _a1_nrm2(R0.reverse() * what * R0 + (-1.0) * what)
    dens_left_12 = _a1_nrm2(R0.reverse() * what * R0)
    assert worst_left < 1e-7 and worst_right < 1e-7, "one-sided FD identities"
    assert worst_unif < 1e-12, "uniform density (omega/2)^2 both one-sided forms"
    assert worst_conj < 1e-7, "conjugation-subtraction identity"
    assert dens_conj_12 < 1e-6, "conjugation class must DECAY (vacuum fixed)"
    assert abs(dens_left_12 - (w / 2.0) ** 2) < 1e-12, "one-sided must NOT decay"
    return {
        "tier": "DERIVED-A",
        "left FD vs R0~ w_hat R0 (worst coeff)": worst_left,
        "right FD vs w_hat (worst coeff)": worst_right,
        "uniform density dev vs (omega/2)^2 (both forms, 2 profiles, 2 u_hat)":
            worst_unif,
        "one-sidedness": "left AND right forms uniform -- NOT a left-shift fact",
        "conjugation identity Om5(conj) = A(Om5(left) - w_hat)A~ (worst coeff)":
            worst_conj,
        "decay dichotomy at r=12 (conj vs one-sided)": (dens_conj_12,
                                                        dens_left_12),
        "pairing note": "(iv) == reverse on this Cl+(4,0) content (alpha5 trivial)",
        "credit": "ANW 1983 / Coleman 1985 (vacuum-stabilizer criterion), via I-5",
        "governing record": "TAU5_ADJUDICATION_2026-08-13.md; ledger N61; "
                            "subtraction-level map = the open O1 gap",
    }


def tau5_unique_v_inert_combination():
    """[DERIVED-A lemma] THE UNIQUE v-INERT FAR-FIELD COMBINATION (tau5
    adjudication 2026-08-13, reviewer N-5 adopted; N61). For the
    T-coord-transported one-sided rotor (phase w*gamma*(tau5 - v*x1), the
    coordinate-boosted rest form), the far-field sector densities are, in units
    of (omega/2)^2:  d5 -> gamma^2  and  d1 -> gamma^2 v^2  (both engine-checked
    below at large r). Among quadratic combinations a*d5 + b*d1, v-INERTNESS of
    the asymptote for all v FORCES b = -a (sympy-exact below):
        a*gamma^2 + b*gamma^2 v^2 = const in v  <=>  b = -a  (value = a).
    CONSEQUENCE: the eta/action combination (the I-C object, b = -a) is the
    UNIQUE v-inert one — every other combination (in particular the Noether
    b = +a) has a v-DEPENDENT asymptote, so any FIXED background renders it
    finite at one v only, and any background that renders it finite at every v
    must itself carry the v-law: the DISCRIMINATION-NULL root of the tau5 route
    (any background that makes a cost finite is the one that installs the
    v-law). The action face's sqrt(1-v^2) is the change-of-variables triviality
    (Schroers 1994: boosting a static soliton is 'merely a complicated way of
    deriving something trivial'; credit carried). This lemma converts the probe
    round's 'only I-C was finite' from observation to result."""
    import math as _m
    a, b, v = sp.symbols("a b v", real=True)
    gamma2 = 1 / (1 - v ** 2)
    expr = a * gamma2 + b * gamma2 * v ** 2
    # v-inertness: expr - expr|_{v=0} == 0 identically in v
    resid = sp.simplify(expr - expr.subs(v, 0))
    num, _den = sp.fraction(sp.together(resid))
    conds = sp.Poly(num, v).coeffs()
    sols = sp.solve(conds, b)
    forced = sp.simplify(sols[b] - (-a)) == 0 if isinstance(sols, dict) else \
        all(sp.simplify(s - (-a)) == 0 for s in (sols if isinstance(sols, list) else [sols]))
    inert_val = sp.simplify(expr.subs(b, -a))
    # numeric far-field face (could fail): FD densities on the transported form
    w = 0.83
    u = e(1, 2)
    d = 1e-6

    def _f(r):
        return _m.pi * _m.exp(-r)

    def _fp(r):
        return -_m.pi * _m.exp(-r)

    def _dens(vv, x):
        g = 1.0 / _m.sqrt(1 - vv * vv)

        def R(x1, t5):
            r = _m.sqrt((g * (x1 - vv * t5)) ** 2 + x[1] ** 2 + x[2] ** 2)
            Rh, _o = _a1_hedgehog((g * (x1 - vv * t5), x[1], x[2]), _f(r), _fp(r))
            return _a1_expu(u, w * g * (t5 - vv * x1) / 2.0) * Rh

        Ri = R(x[0], 0.0).reverse()
        d5 = _a1_nrm2(Ri * ((1 / (2 * d)) * (R(x[0], d) - R(x[0], -d))))
        d1 = _a1_nrm2(Ri * ((1 / (2 * d)) * (R(x[0] + d, 0.0) - R(x[0] - d, 0.0))))
        return d5 / (w / 2.0) ** 2, d1 / (w / 2.0) ** 2

    worst = 0.0
    combos = {}
    for vv in (0.3, 0.6):
        g2 = 1.0 / (1 - vv * vv)
        d5, d1 = _dens(vv, (14.0, 0.3, 0.2))
        worst = max(worst, abs(d5 - g2) / g2, abs(d1 - g2 * vv * vv) / (g2 * vv * vv))
        combos[vv] = (d5 - d1, d5 + d1)
    inert_meas = max(abs(combos[vv][0] - 1.0) for vv in combos)
    noether_spread = abs(combos[0.6][1] - combos[0.3][1])
    assert forced, "v-inertness must FORCE b = -a"
    assert sp.simplify(inert_val - a) == 0, "inert value must equal a"
    assert worst < 1e-3, "far-field densities must match gamma^2 / gamma^2 v^2"
    assert inert_meas < 1e-3, "(1,-1) combination must be v-inert (measured)"
    assert noether_spread > 0.3, "(1,+1) Noether combination must be v-DEPENDENT"
    return {
        "tier": "DERIVED-A (lemma; sympy-exact + far-field engine face)",
        "b = -a forced (sympy)": bool(forced),
        "inert value == a (sympy)": True,
        "far-field density match at r=14 (worst rel)": worst,
        "(1,-1) inertness measured (worst dev from 1)": inert_meas,
        "(1,+1) Noether v-spread (must be > 0.3)": noether_spread,
        "consequence": "I-C is the UNIQUE v-inert combination; any background "
                       "finitizing another combination installs the v-law "
                       "(discrimination-null root)",
        "credit": "Schroers 1994 (gamma-face triviality); reviewer N-5 lemma",
        "governing record": "TAU5_ADJUDICATION_2026-08-13.md; ledger N61",
    }


def ecarrier_common_mode_certificates():
    """[DERIVED-A] K-O1 ROUND CERTIFICATES (governing record:
    knowledge/candidates/probes_2026-08-13/KO1_ADJUDICATION_2026-08-13.md;
    N56 K-O1 sub-item, RUL-022 booking; the round CLOSED WITHOUT EXECUTION —
    every identity here was decided twice over at design time, and these three
    legs are banked as the round's PROVEN BUG-CATCHERS (design-review bug
    injection: reverse-as-inverse, alpha5-sign-drop, broken-e5-filter each
    caught by exactly these checks). k_c is an ARBITRARY convention constant
    (RUL-017: no carrier scale is named). Everything at rest (RUL-034/RUL-015).

    LEG 1 (CL-1, E-centrality): q_{k+dk} q_k^-1 = q_dk EXACTLY (the identity
    that collapses every referenced two-rate object); conjugation transparency
    q_E X q_E^-1 = X; two-path TRUE-INVERSE carrier cancellation
    (A1 qE) t(A2 qE) = A1 t(A2) for arbitrary Cl(4,0) branch content; and the
    D-1 leg — the REVERSE overlap does NOT cancel the carrier:
    (A1 qE)~ (A2 qE) = A1~ A2 qE^2 exactly (E central, qE~ = qE), with the
    nonzero witness MEASURED both over all 32 blades AND within the {1, B}
    line separately (stated = measured; MO sweep-integrity fix 2026-08-13).

    LEG 2 (CL-2; pairing-(iv)-conditional — RUL-018 class B): t = alpha5 o
    reverse satisfies t(q_E) = q_E^-1 — on the E-phase the ruled involution IS
    the true inverse (alpha5 flips E, exactly compensating E~ = +E) — hence
    <Psi_vac t(Psi_vac)>_0 = c0^2/2 and <Om_4 t(Om_4)>_0 = (k_c/2)^2, both
    exactly x4-independent: every (iv)-class observable is carrier-FLAT.
    CREDIT (corrected TWICE — K-O1 re-review, then keeper round-record
    hygiene): this INSTANTIATES the banked per-blade positivity of
    cl41_positive_definite_pairing (E is one of the 32 blades) — not new
    content; and the (k_c/2)^2 MAGNITUDE was already engine-explicit under the
    reverse pairing (opposite sign) in ecarrier_matched_defect_hblock_null's
    return — the (iv)-SIGN version is what is new here.

    LEG 3 (CL-3 — FACT ONLY; no observability claim in either direction): the
    pure carrier Psi_vac = c0 s0 q_E(x4) has un-referenced Cl(4,0)-ideal
    shadow cos(k_c x4/2) c0 s0 (amplitude modulation with zeros on the grid)
    and reverse grade-0 <Psi~ Psi>_0 = cos(k_c x4) c0^2/2 — oscillating and
    SIGN-INDEFINITE. Whether the un-referenced shadow is OBSERVABLE on a
    carrier background is the round's HINGE H ('the ideal-shadow projection is
    observable iff applied to a carrier-referenced object') — NOT
    engine-decidable, banked domain EMPTY — filed at the
    renormalization-dictionary assembly for coordinator ratification. H's LIVE
    SCOPE (keeper C3 simplification): exactly the NON-t-paired residue — this
    raw shadow — since E-centrality + t(q_E) = q_E^-1 make every t-paired
    object carrier-transparent (the stronger, H-independent ground).

    LEG 4 (keeper O1 — the {1,B} FACTORIZATION, the fact that decided C1's
    true cost; K-O1 keeper verdict + MO C2, composed): for any detector/state
    contents D, psi with a SHARED carrier, the reverse-referenced Born-class
    overlap projected to the observer's {1, B} line factorizes EXACTLY:
        <(D qE)~ (psi qE)>_{1,B} = cos(k_c x4) * <D~ psi>_{1,B},
    a REAL COMMON SCALAR for every channel. Hence: probability RATIOS exactly
    x4-invariant (common-mode cancellation — R-023's normalized probabilities
    are carrier-independent); TOTAL probability breathes as cos^2(k_c x4) and
    DEGENERATES 0/0 on the comb x4 = (2n+1)pi/(2 k_c); under the RULED adjoint
    t the reference is exactly carrier-free (constant Sum P). This is the
    engine ground of RUL-035 (class-(1), coordinator-enacted 2026-08-13):
    R-023's observer-side reference operation on non-trivial (carrier)
    backgrounds is the ruled adjoint t = alpha5 o reverse, REST-FRAME-scoped;
    on Cl(4,0)/trivial backgrounds t == reverse so nothing recomputes; the
    boost extension belongs to the dictionary (RUL-034 fence). Scope of the
    fact: every reverse-referenced observer-side overlap (R-023 and, on
    carrier backgrounds, the R-160 F3 total-function premise and the R-027
    half-angle overlap — inherit-notes at their rows)."""
    import math as _m
    import random as _rd

    K_C = 0.8317
    C0 = 1.0
    E5 = I4 * e(5)
    s0 = 0.5 * SCALAR + 0.5 * e(4)
    rng = _rd.Random(20260813)

    def _t(X):
        out = 0.0 * SCALAR
        for idx, c in dict(X.reverse().terms).items():
            sgn = -1.0 if 5 in idx else 1.0
            B = e(*idx) if idx else SCALAR
            out = out + c * sgn * B
        return out

    def _qE(x4, kc=K_C):
        return _m.cos(kc * x4 / 2) * SCALAR + _m.sin(kc * x4 / 2) * E5

    def _qEi(x4, kc=K_C):
        return _m.cos(kc * x4 / 2) * SCALAR - _m.sin(kc * x4 / 2) * E5

    def _shadow(X):
        out = 0.0 * SCALAR
        for idx, c in dict(X.terms).items():
            if 5 not in idx:
                B = e(*idx) if idx else SCALAR
                out = out + c * B
        return out

    # generating facts (non-vacuous anchors: the reverse-trap witness must FAIL
    # visibly as an inverse, so the checks below cannot pass under bug A)
    assert _a1_maxcoeff(E5 * E5 + SCALAR) < 1e-12
    assert _a1_maxcoeff(E5.reverse() - E5) < 1e-12
    assert _a1_maxcoeff(_qE(1.7).reverse() * _qE(1.7) - SCALAR) > 0.5, \
        "reverse must visibly FAIL as the inverse for E-content"
    assert _a1_maxcoeff(_t(_qE(1.7)) - _qEi(1.7)) < 1e-12, "t(qE) = qE^-1"

    def _line12(X):
        """{1, B}-line projection coefficients (B = e12): (grade-0, B-coeff)."""
        d = dict(X.terms)
        return (float(d.get((), 0.0)), float(d.get((1, 2), 0.0)))

    n_grid = 48
    period = 2 * (4 * _m.pi / K_C)          # >= 2 carrier periods incl. the node
    leg1 = leg1_wit = leg1_wit_line = leg2 = leg3 = leg4 = 0.0
    ratio_dev = 0.0
    breathe_dev = 0.0
    for i in range(n_grid):
        x4 = (i + 0.5) / n_grid * period
        dk = rng.uniform(-2.0, 2.0)
        # LEG 1 -- relative-phase collapse, transparency, two-path, D-1
        leg1 = max(leg1, _a1_maxcoeff(_qE(x4, K_C + dk) * _qEi(x4) - _qE(x4, dk)))
        A1 = (rng.uniform(-1, 1) * SCALAR + rng.uniform(-1, 1) * e(1, 2)
              + rng.uniform(-1, 1) * e(1, 4) + rng.uniform(-1, 1) * e(1, 2, 3))
        A2 = (rng.uniform(-1, 1) * SCALAR + rng.uniform(-1, 1) * e(2, 3)
              + rng.uniform(-1, 1) * e(1) + rng.uniform(-1, 1) * e(1, 2, 3, 4))
        leg1 = max(leg1, _a1_maxcoeff(
            (A1 * _qE(x4)) * _t(A2 * _qE(x4)) - A1 * _t(A2)))
        X = rng.uniform(-1, 1) * e(1, 3) + rng.uniform(-1, 1) * e(1, 2, 3)
        leg1 = max(leg1, _a1_maxcoeff(_qE(x4) * X * _qEi(x4) - X))
        rev_ov = (A1 * _qE(x4)).reverse() * (A2 * _qE(x4))
        leg1 = max(leg1, _a1_maxcoeff(rev_ov - A1.reverse() * A2 * _qE(x4, 2 * K_C)))
        resid = rev_ov - A1.reverse() * A2
        leg1_wit = max(leg1_wit, _a1_maxcoeff(resid))
        g0r, gBr = _line12(resid)
        leg1_wit_line = max(leg1_wit_line, abs(g0r), abs(gBr))
        # LEG 2 -- carrier-flat (iv)-observables
        psi = C0 * s0 * _qE(x4)
        leg2 = max(leg2, abs(_a1_g0(psi * _t(psi)) - C0 * C0 / 2))
        Om4 = (K_C / 2) * E5
        leg2 = max(leg2, abs(_a1_g0(Om4 * _t(Om4)) - (K_C / 2) ** 2))
        # LEG 3 -- raw-shadow structure (fact only)
        leg3 = max(leg3, _a1_maxcoeff(_shadow(psi) - _m.cos(K_C * x4 / 2) * C0 * s0))
        leg3 = max(leg3, abs(_a1_g0(psi.reverse() * psi)
                             - _m.cos(K_C * x4) * C0 * C0 / 2))
    # LEG 4 -- the {1,B} factorization + common-mode facts (keeper O1 / MO C2)
    Dets = []
    for _ in range(3):
        Dets.append(rng.uniform(-1, 1) * SCALAR + rng.uniform(-1, 1) * e(1, 2)
                    + rng.uniform(-1, 1) * e(1, 3))
    psi_b = 0.6 * SCALAR + 0.3 * e(1, 2) + 0.2 * e(2, 3)
    z0 = [complex(*_line12(D.reverse() * psi_b)) for D in Dets]
    P0 = [abs(z) ** 2 for z in z0]
    S0n = sum(P0)
    x4_samples = [0.0, 1.1, 2.5, 3.7773, _m.pi / (2 * K_C)]   # incl. the comb point
    for x4 in x4_samples:
        c = _m.cos(K_C * x4)
        zs = [complex(*_line12((D * _qE(x4)).reverse() * (psi_b * _qE(x4))))
              for D in Dets]
        # factorization: z(x4) = cos(kc x4) * z0, per channel, exact
        leg4 = max(leg4, max(abs(zs[j] - c * z0[j]) for j in range(3)))
        Ps = [abs(z) ** 2 for z in zs]
        Ss = sum(Ps)
        # total probability breathes as cos^2 (degenerate 0/0 on the comb)
        breathe_dev = max(breathe_dev, abs(Ss - c * c * S0n))
        # ratios exactly invariant wherever defined
        if Ss > 1e-20:
            ratio_dev = max(ratio_dev,
                            max(abs(Ps[j] / Ss - P0[j] / S0n) for j in range(3)))
        # under the RULED adjoint the reference is exactly carrier-free
        zt = [complex(*_line12(_t(D * _qE(x4)) * (psi_b * _qE(x4))))
              for D in Dets]
        zt0 = [complex(*_line12(_t(D) * psi_b)) for D in Dets]
        leg4 = max(leg4, max(abs(zt[j] - zt0[j]) for j in range(3)))
    comb_S = sum(abs(complex(*_line12(
        (D * _qE(_m.pi / (2 * K_C))).reverse()
        * (psi_b * _qE(_m.pi / (2 * K_C)))))) ** 2 for D in Dets)
    # sign-indefiniteness of the reverse grade-0 (LEG 3, non-vacuous: both signs
    # realized on the grid) and the shadow zero at the node
    g0s = [_a1_g0((C0 * s0 * _qE(x4)).reverse() * (C0 * s0 * _qE(x4)))
           for x4 in (0.1, _m.pi / K_C)]
    assert g0s[0] > 0.0 and g0s[1] < 0.0, "reverse grade-0 must be sign-indefinite"
    node_amp = _a1_maxcoeff(_shadow(C0 * s0 * _qE(_m.pi / K_C)))
    assert leg1 < 1e-12 and leg2 < 1e-12 and leg3 < 1e-12
    assert leg1_wit > 0.3, "the reverse overlap must visibly RETAIN the carrier"
    assert leg1_wit_line > 0.05, \
        "the retention must be visible WITHIN the {1,B} line (stated = measured)"
    assert node_amp < 1e-12, "the raw shadow amplitude must vanish at the node"
    assert leg4 < 1e-12, "{1,B} factorization + ruled-adjoint constancy must be exact"
    assert ratio_dev < 1e-12, "normalized ratios must be exactly carrier-invariant"
    assert breathe_dev < 1e-12, "Sum P must breathe as cos^2(k_c x4) exactly"
    assert comb_S < 1e-20, "Sum P must vanish on the comb (the 0/0 degeneracy)"
    return {
        "tier": "DERIVED-A (legs 1/3/4 pairing-independent facts; leg 2 "
                "pairing-(iv)-conditional, RUL-018 class B; leg 4's "
                "reference-operation consequence is RUL-035)",
        "leg1 centrality identities (worst coeff)": leg1,
        "leg1 D-1 reverse-overlap carrier retention (witness, must be > 0.3)":
            leg1_wit,
        "leg1 D-1 retention within the {1,B} line (measured, must be > 0.05)":
            leg1_wit_line,
        "leg2 (iv)-flatness devs (worst)": leg2,
        "leg3 raw-shadow structure devs (worst)": leg3,
        "leg3 reverse grade-0 sign pair (+, -)": tuple(g0s),
        "leg3 shadow amplitude at the node (exact 0)": node_amp,
        "leg4 {1,B} factorization + ruled-adjoint constancy (worst)": leg4,
        "leg4 normalized-ratio carrier-invariance (worst dev)": ratio_dev,
        "leg4 Sum P vs cos^2 breathing (worst dev)": breathe_dev,
        "leg4 Sum P on the comb (0/0 degeneracy witness)": comb_S,
        "hinge": "H = 'ideal-shadow observable iff carrier-referenced' — NOT "
                 "decided here; live scope = the raw un-referenced shadow "
                 "(t-paired objects are carrier-transparent); filed for "
                 "coordinator ratification",
        "ruling": "RUL-035 (2026-08-13): R-023's observer-side reference on "
                  "carrier backgrounds = the ruled adjoint t, rest-frame-scoped; "
                  "t == reverse on Cl(4,0)/trivial backgrounds (nothing "
                  "recomputes); boost extension = dictionary (RUL-034)",
        "credits": "cl41_positive_definite_pairing (per-blade value, leg 2); "
                   "ecarrier_matched_defect_hblock_null (matched-defect face + "
                   "the reverse-pairing magnitude, opposite sign); "
                   "R-147 blade table (texture faces, K-O3 caveat)",
        "governing record": "KO1_ADJUDICATION_2026-08-13.md; N56 K-O1 sub-item",
    }


# ######################################################################
# ######################################################################
# ##                                                                  ##
# ##   SECTION CANDIDATE — V3-INSTANCE COMPANION PRIMITIVES           ##
# ##                                                                  ##
# ######################################################################
# ######################################################################
# WHAT THIS SECTION HOLDS: companion primitives that consume a V3 PICK — the whole
# CKM / meta-time exploration arc, the TASK-e4 epicycle series, the matter-as-defect
# CKM/gluon ladder, the SU(6)/gear hadron-band toolbox, the D4-sited 24-cell
# geometry, the Langevin calibration gate and the KSS channel probes, and everything
# consuming lepton/quark mass VALUES or D/J numerics.
#
# MEMBERSHIP HERE IS NOT A TIER. It says: a different family member — same axioms,
# different pick — would compute something else here. The tiers are unchanged by the
# split and live where they always lived, in each primitive's own docstring.
# ######################################################################



def d4_langevin_calibration_gate():
    """[DERIVED-A (the 1D-effective reduction reproduces N31 exactly) + FRAMING (the GPU driven-sim model);
    Phase B / B3 of the Class-2 campaign (2026-07-05)] The CALIBRATION GATE for the CUDA D4-Langevin
    driven-dissipative sim (RTX 4090): the N31 canted-D4 planar statics reduce EXACTLY to a 1D planar-rotor
    chain with per-bond energy
        e(dtheta) = -A cos(dtheta) - B sin(dtheta),   A = 12 J,  B = 2*sqrt(2)*D,
    whose ordered-state spiral tan q* = B/A = sqrt(2) D/(6 J) reproduces (at D=J) q* = atan(sqrt(2)/6) AND
    the longitudinal stiffness K_long = (1/2) d2E/dq2 = sqrt(38) J -- BOTH of N31's banked statics. This is
    the model the driven sim runs (drive along the DM/e4 channel; overdamped Langevin with damping gamma +
    noise Tn NOT tied by FDT, per C1/I-12). No dynamics is believed until this gate passes (R-143/R-144
    lattice discipline). The GATE PASSED on device=cuda (statics reproduced to machine precision).

    PROVENANCE RE-TIER (2026-07-26 corpus pass; the coordinator's sharpened no-toy
    rule, 2026-07-23): the DRIVEN MEASUREMENT paragraph below ran on the 1D
    EFFECTIVE CHAIN — under the no-toy rule (conclusions only from the dynamic
    4D-wave-in-4D-substrate model; a toy shows only known/demonstrated/predictable
    results) it is a TOY-LEVEL CONSISTENCY RECORD, not a conclusion-bearer
    (simulator KP_T3c_closure.md R10). The INSTRUMENT-GRADE record now exists on
    the 4D substrate sim (simulator substrate4d [2z32], reviewed to consensus):
    GATE-0 — the memoryless ordered-softened quadrant is EMPTY on the hunted grid
    (best ratio 1.06 vs the 39 bar, a 36.8x shortfall; K4D_gate0_closure.md);
    G1b — the kernel-injected calibration hunt is UNMEASURED-DRY (3 of 4 corners
    never converge at the protocol windows; the readable corner shows NO
    renormalization above 0.4%/0.04% floors; K4D_g1b_closure.md, all three
    readings carried unadjudicated). CLASSICAL SELECTABILITY OF K_c IS OPEN —
    neither confirmed nor excluded; the paragraph below stays as history with its
    1D scope now explicit.

    THE DRIVEN MEASUREMENT (documented in the B4 candidate memo, CANDIDATE-tier -- NOT a suite claim;
    1D-toy-scoped per the re-tier above). The
    headline test: does drive+dissipation renormalize K_long DOWN to K_c = 2J/19 (the (19/2)sqrt(38) ~ 58.56
    factor, N31)? RESULT (GPU, equipartition-calibrated, order-parameter-tracked, invariance-checked across
    2 drive models): the drive SOFTENS the effective stiffness K_eff monotonically (the RIGHT DIRECTION --
    toward K_c), BUT it does so by DEGRADING the spiral order (a classical order->disorder crossover: the
    spiral coherence OP drops from ~0.98 to <0.4 as K_eff softens) or by drive-LOCKING the rotors uniformly
    (K_eff -> 0, no spiral) -- NOT by selecting a STABLE softened-but-ORDERED spiral at K_c. So the specific
    (19/2)sqrt(38) renormalization is CROSSED en route to disorder, NOT SELECTED as a stable driven fixed
    point. HONEST READ: the softening DIRECTION is confirmed on the substrate lattice, but the specific N31
    value is a QUANTUM-CRITICAL (DQCP) effect that the CLASSICAL effective-model Langevin sim does not
    select -- a LOCATED NEGATIVE, consistent with the honest ceiling (the kernel FORM / the DQCP quantum
    dynamics is the #1 gap). Invariance-across-choices (B0): the qualitative softening-via-disorder is the
    SAME for the bulk-e4 and traveling-wave drive models => it is a drive-model-INVARIANT feature (a
    candidate substrate fact); the specific K_eff values are model-dependent (labeled).

    self-check: the 1D-effective reduction reproduces N31's q* = atan(sqrt(2)/6) and K_long = sqrt(38) J
    (sympy-exact), and the target renormalization K_long/K_c = (19/2)sqrt(38) (live vs N31)."""
    import sympy as sp
    J = sp.Integer(1); D = sp.Integer(1)                 # D = J (the QCP)
    A = 12 * J; B = 2 * sp.sqrt(2) * D
    q = sp.symbols('q', real=True)
    # ordered-state pitch of the per-bond energy e(q) = -A cos q - B sin q:
    q_star = sp.atan(B / A)                              # tan q* = B/A = sqrt(2)/6
    K_long = sp.simplify((A * sp.cos(q_star) + B * sp.sin(q_star)) / 2)   # (1/2) d2e/dq2 at q*
    K_c = sp.Rational(2, 19) * J
    renorm = sp.simplify(K_long / K_c)

    # cross-check vs N31 (banked)
    kc = Kc_magnon_stiffness_canted_FM_at_DJ()
    q_star_N31 = sp.atan(sp.sqrt(2) / 6)
    K_long_N31 = sp.sqrt(38) * J

    q_ok = sp.simplify(q_star - q_star_N31) == 0
    K_ok = sp.simplify(K_long - K_long_N31) == 0
    renorm_ok = sp.simplify(renorm - sp.Rational(19, 2) * sp.sqrt(38)) == 0
    renorm_live_ok = abs(float(renorm) - kc["ratio_K_long_over_K_c"]) < 1e-9

    assert q_ok, "1D-effective reduction must reproduce N31's q* = atan(sqrt(2)/6)"
    assert K_ok, "1D-effective reduction must reproduce N31's K_long = sqrt(38) J"
    assert renorm_ok and renorm_live_ok, "target renormalization must be (19/2)sqrt(38) ~ 58.56 (N31 live)"

    return {
        "tier": "DERIVED-A (the 1D-effective reduction reproduces N31's q*, K_long exactly, sympy) + FRAMING (the GPU driven-sim model + the CANDIDATE driven measurement)",
        "effective_model": "1D planar-rotor chain, per-bond e = -12J cos(dtheta) - 2 sqrt(2) D sin(dtheta); tan q* = sqrt(2) D/(6 J)",
        "calibration_gate": "reproduces N31 EXACTLY: q* = atan(sqrt(2)/6), K_long = sqrt(38) J; target renorm K_long/K_c = (19/2)sqrt(38) ~ 58.56 -- GATE PASSED on device=cuda",
        "driven_result_CANDIDATE": "the drive SOFTENS K_eff monotonically (right direction toward K_c) but via spiral-order DEGRADATION or drive-LOCKING, NOT a stable softened-ORDERED spiral => the (19/2)sqrt(38) is CROSSED en route to disorder, NOT SELECTED. [RE-TIERED 2026-07-26 per the sharpened no-toy rule (KP_T3c_closure R10): this ran on the 1D EFFECTIVE CHAIN — a TOY-LEVEL CONSISTENCY RECORD, not a conclusion-bearer; the prior located-negative/DQCP-selection wording is WITHDRAWN as a conclusion. CLASSICAL SELECTABILITY OF K_c IS OPEN. The instrument-grade 4D record: gate-0 memoryless quadrant EMPTY (36.8x shortfall); G1b kernel hunt UNMEASURED-DRY (K4D closures, consensus)]",
        "invariance": "the qualitative softening-via-disorder is INVARIANT across the bulk-e4 and traveling-wave drive models (a candidate substrate fact, B0); the specific K_eff values are model-dependent (labeled)",
        "target_renorm_58": float(renorm),
    }


def static_susceptibility_sumrule_and_kss_channel_mismatch():
    """[FRAMING (channel adjudication + wrong-object verdict) + DERIVED-A (the static
    susceptibilities, live from N31)] — W2.2 of the Class-2 campaign (2026-07-05). Manufactures
    N33 input (3) — a genuine Kramers-Kronig-safe / FDT-free static-susceptibility datum — from
    the canted-D4 statics, then adjudicates its CHANNEL against the registry. RESULT: the datum
    is real, but it is WRONG-OBJECT for the one usable anchor (KSS/GW) — so it does NOT lift the
    rank-deficiency; it is channel-MATCHED to the K_c structural-target row instead. A precise
    located gap (ledger N43), with the datum computed.

    THE MOVE (brief W2.2). N33's would-change-if (iii) asks for "a genuine sum-rule /
    Kramers-Kronig input with a real number (a static-susceptibility value or a short-distance
    equal-time correlator)" — currently absent from the corpus "with real numeric content, only
    as named categories." The canted-D4 LSWT machinery (Kc_magnon_stiffness_canted_FM_at_DJ,
    N31) computes exactly this class of quantity sympy-exactly. This primitive instantiates the
    datum and, critically, NAMES ITS CHANNEL so the wrong-object trap (the campaign's most likely
    failure, N11-R1/N33/N34) is confronted head-on.

    THE DATUM [DERIVED-A, live from N31]. The static susceptibility of the L-orbit magnon phase
    is the inverse of the LSWT gradient stiffness (the standard stiffness<->susceptibility
    inverse; the prefactor is conjugate-field-normalization-dependent, but the KK-safe/FDT-free
    provenance and the (19/2)sqrt(38) renormalization ratio below are convention-INDEPENDENT):
        chi_long(0) = 1/K_long = 1/(sqrt(38) J)  ~ 0.16222 / J
        chi_trans(0)= 1/K_trans = 1/((2 cos q* + 4) J) ~ 0.16816 / J
        (K_trans erratum 2026-07-26 — see Kc_magnon_stiffness_canted_FM_at_DJ;
        the prior 0.25685/J rode the 4 cos q* transcription error)
    This is the M_{-1} moment `chi(0) = (2/pi) INT dω Im chi(ω)/ω` (Kramers-Kronig; the ω->0
    static limit of Re chi) — a real (moment, value) pair. It rides ONLY causality/KK (holds for
    ANY causal response, driven or not — SAFE) and the ground-state energy curvature (a
    mechanical/thermodynamic response). It does NOT use the fluctuation-dissipation theorem —
    whose violation residual IS Θ_rel (Import Registry I-12, definitional). Stating this
    discrimination is load-bearing: the moment one invokes FDT one has assumed away the object
    the program hunts.

    NAME ALL FOUR (the wrong-object discipline — canon menu-vs-pick; N33):
      - OPERATOR : the L-orbit magnon PHASE θ (the canted order-parameter twist / spin-wave).
      - CHANNEL  : order-parameter (longitudinal/transverse magnon) static response.
      - LAYER    : CELL-layer QCP phenomenology (the LSWT is computed on D4 bonds, but the
                   chirality-balance / canted ordered state is cell-scale collective, NOT a
                   Planckian-grain excitation — §D.3.2 naming note, §D.4.3).
      - FREQUENCY: ω -> 0 static (KK-safe; NOT a finite-drive reactive ratio).

    THE VERDICT — WRONG-OBJECT FOR THE ONE USABLE ANCHOR [the located gap, N43]. The registry's
    single usable anchor (kss_gw_bracket) constrains the SHEAR VISCOSITY η — a STRESS-ENERGY-
    TENSOR transport coefficient, `η = lim_{ω->0} Im G_{T_xy,T_xy}(ω)/ω` (KSS floor η/s ≥ ℏ/4π;
    GW170817 via Γ ~ 16πGη/c²), also at the CELL layer. So the LAYER matches, but the OPERATOR
    and CHANNEL do NOT: an order-parameter susceptibility (chi_θθ) is a different response
    function from a momentum-transport / stress-tensor transport coefficient (η). They are
    bridged only by the unbuilt kernel — exactly the N11-R1 "two dimensionless objects bridged
    only by the kernel" pattern. CONSEQUENCE: this datum does NOT match kss_gw_bracket ⟹ it does
    NOT add a usable anchor ⟹ the registry's rank-deficiency is UNCHANGED (the over-determination
    table's usable-anchor count stays 1, asserted live below). N33 input (3) is thus PARTIALLY
    delivered: a KK-safe static datum with a real number DOES exist from statics — but in the
    magnon channel, not the transport channel the one anchor lives in.

    THE CONSTRUCTIVE HALF — CHANNEL-MATCH TO THE K_c ROW. The same datum IS in the K_c row's
    channel (the L-orbit QCP magnon). K_c = 2J/19 is the corpus's asserted RENORMALIZED stiffness
    in this channel; the kernel must take K_long -> K_c, i.e. renormalize the static
    susceptibility chi(0) UP by exactly `chi_c/chi_long = (1/K_c)/(1/K_long) = (19/2)sqrt(38)
    ~ 58.56` (cross-checked live vs N31). So this primitive gives the K_c structural-target row a
    genuine KK-safe, FDT-free static-susceptibility COMPANION on its bare side: chi_long = 1/sqrt(38) J
    is the un-renormalized static susceptibility the kernel must soften into chi_c = 19/2 J.

    THE SECOND-MOMENT SUB-FINDING (why statics gives only ONE moment). The f-sum M_{+1} =
    `INT dω ω Im chi(ω)` = the equal-time double commutator ⟨[[θ,H],θ]⟩. For the planar rotor it
    equals 1/(2 I) with I the rotor MOMENT OF INERTIA (ω_k^2 = K(k)/I) — a substrate-DYNAMICS
    input absent from the statics (the Skyrme Θ_0 is the BARYON rotational inertia, not this
    L-orbit magnon inertia). So statics alone yields the M_{-1} static susceptibility but NOT the
    M_{+1} f-sum ⟹ NOT a two-moment shape constraint on the kernel. This is a precise sub-gap.

    FENCE: does NOT lift the rank-deficiency; does NOT compute any kernel value; does NOT add a
    usable anchor. The CANDIDATE beyond this (FLAGGED, NOT banked): IF a moment of Im chi in this
    channel is kernel-invariant (e.g. the f-sum, were the inertia available AND the kernel purely
    dissipative), the (19/2)sqrt(38) softening of chi(0) at fixed f-sum would force spectral
    weight to lower ω — a critical-slowing/soft-mode statement. Both premises (inertia; the
    kernel-invariance of a moment) are the #1 gap — so this stays a candidate for a future move,
    not a result.

    WOULD CHANGE IF: (i) a static moment in the STRESS-TENSOR / shear channel is computed from
    the substrate (that WOULD be channel-matched to kss_gw_bracket and could lift the count);
    (ii) the L-orbit magnon rotor inertia I is derived (enables the f-sum M_{+1} ⟹ a two-moment
    constraint on the K_c renormalization); (iii) a grain↔cell transport bridge relates chi_θθ to
    η (would make this an indirect anchor).

    self-checks: chi_long*J == 1/sqrt(38) and chi_trans*J == 1/K_trans (live vs N31); the renorm
    ratio chi_c/chi_long == (19/2)sqrt(38) (live vs N31); the over-determination table's
    usable-anchor count is UNCHANGED at 1 (this datum added no usable anchor — live vs R-150);
    the KSS anchor operator is the shear viscosity η (stress-tensor), confirmed distinct."""
    import math

    kc = Kc_magnon_stiffness_canted_FM_at_DJ()
    K_long = kc["K_long_value"]            # sqrt(38) J
    K_trans = kc["K_trans_value"]          # (2 cos q* + 4) J (erratum 2026-07-26)
    K_c = kc["K_c_asserted_over_J"]        # 2/19 J
    ratio_engine = kc["ratio_K_long_over_K_c"]   # (19/2) sqrt(38)

    chi_long = 1.0 / K_long                # = 1/sqrt(38) per J
    chi_trans = 1.0 / K_trans
    chi_c = 1.0 / K_c                      # = 19/2 per J  (target renormalized)
    renorm = chi_c / chi_long             # = (19/2) sqrt(38)

    # ---- DERIVED-A: the static-susceptibility datum, live from N31 ----
    assert abs(chi_long - 1.0 / math.sqrt(38.0)) < 1e-12, "chi_long must be 1/sqrt(38) per J"
    assert abs(chi_trans - 1.0 / K_trans) < 1e-12, "chi_trans must be 1/K_trans"
    assert abs(renorm - (19.0 / 2.0) * math.sqrt(38.0)) < 1e-9, \
        "the kernel renormalization of chi(0) must be (19/2)sqrt(38)"
    assert abs(renorm - ratio_engine) < 1e-9, \
        "renorm ratio must equal N31's K_long/K_c (same object, inverse)"

    # ---- the wrong-object verdict: NO usable anchor added (rank-deficiency unchanged) ----
    added_usable_anchor_for_kss = False   # order-parameter chi != stress-tensor transport η
    channel_matches_kc = True             # same L-orbit magnon channel
    table = kernel_overdetermination_table()
    assert table["n_usable_anchors"] == 1, \
        "W2.2 must NOT change the usable-anchor count (wrong-object for KSS/GW)"

    return {
        "tier": "FRAMING (channel adjudication + wrong-object verdict) + "
                "DERIVED-A (the static susceptibilities, live from N31)",
        "datum": {
            "chi_long_times_J": chi_long,          # 1/sqrt(38) ~ 0.16222
            "chi_long_symbolic": "1/sqrt(38)",
            "chi_trans_times_J": chi_trans,        # ~ 0.16816 (K_trans erratum 2026-07-26)
            "moment": "M_{-1} = chi(0) = (2/pi) INT Im chi(ω)/ω dω  (Kramers-Kronig; ω->0 static)",
            "provenance": "KK-safe (causality, any causal response) + ground-state energy "
                          "curvature; FDT NOT used (I-12: FDT violation IS Θ_rel)",
        },
        "channel": {
            "operator": "L-orbit magnon phase θ (canted order-parameter twist / spin-wave)",
            "channel": "order-parameter (longitudinal/transverse) static response",
            "layer": "CELL-layer QCP phenomenology (LSWT on D4 bonds; cell-scale collective, "
                     "NOT a Planckian-monad excitation — §D.3.2/§D.4.3)",
            "frequency": "ω -> 0 static",
        },
        "kss_anchor_object": "shear viscosity η = lim Im G_{T_xy,T_xy}/ω (stress-tensor "
                             "transport; KSS η/s ≥ ℏ/4π; GW Γ ~ 16πGη/c²); CELL layer",
        "wrong_object_verdict": ("SAME layer (cell), DIFFERENT operator/channel: an "
                                 "order-parameter susceptibility chi_θθ is not the stress-tensor "
                                 "transport coefficient η — bridged only by the unbuilt kernel "
                                 "(N11-R1 pattern) ⟹ does NOT match kss_gw_bracket ⟹ NO usable "
                                 "anchor added ⟹ rank-deficiency UNCHANGED (count stays 1)"),
        "added_usable_anchor_for_kss": added_usable_anchor_for_kss,   # False
        "n33_input_3_status": "PARTIALLY DELIVERED — a KK-safe/FDT-free static datum with a real "
                              "number DOES exist from statics, but in the magnon channel, not the "
                              "transport channel the one usable anchor lives in",
        "channel_match_to_Kc": {
            "matches": channel_matches_kc,        # True
            "chi_c_times_J": chi_c,               # 19/2 = 9.5 (target renormalized)
            "renorm_factor_chi_c_over_chi_long": renorm,   # (19/2)sqrt(38) ~ 58.56
            "meaning": "chi_long = 1/sqrt(38) J is the bare KK-safe static-susceptibility "
                       "companion to the K_c target; the kernel must soften K_long -> K_c "
                       "(chi(0) up by (19/2)sqrt(38))",
        },
        "second_moment_subfinding": ("the f-sum M_{+1} = INT ω Im chi dω = ⟨[[θ,H],θ]⟩ = 1/(2I) "
                                     "needs the rotor MOMENT OF INERTIA I (ω^2 = K/I), a "
                                     "substrate-dynamics input absent from statics ⟹ statics "
                                     "gives ONE moment (M_{-1}), NOT a two-moment shape constraint"),
        "candidate_not_banked": ("IF a channel moment is kernel-invariant AND the inertia is "
                                 "known, the (19/2)sqrt(38) softening of chi(0) at fixed f-sum "
                                 "forces spectral weight to lower ω (critical-slowing/soft-mode) "
                                 "— both premises are the #1 gap; FLAGGED, not banked"),
        "fence": "NOT a rank-deficiency resolution, NOT a kernel value, NOT a new usable anchor "
                 "— a channel adjudication with the datum computed (ledger N43)",
        "would_change_if": ("(i) a static moment in the STRESS-TENSOR/shear channel (channel-"
                            "matched to kss_gw_bracket); (ii) the L-orbit magnon inertia I "
                            "derived (enables the f-sum); (iii) a monad↔cell transport bridge "
                            "relating chi_θθ to η"),
        "verdict": ("N33 input (3) is manufacturable from statics (chi_long = 1/sqrt(38) J, "
                    "KK-safe/FDT-free) but is WRONG-OBJECT for the one usable anchor (KSS/GW = "
                    "shear viscosity); it is channel-matched to the K_c structural-target row, "
                    "giving that row a bare static-susceptibility companion. The rank-deficiency "
                    "is unchanged — a precise located gap, not an anchor."),
    }


def stress_tensor_shear_channel_static_moment():
    """[FRAMING (channel adjudication) + DERIVED-A (the shear modulus number) — A3 of the Class-2
    campaign, N47; addresses N43's would-change-if (i)] Computes the canted-D4 spiral's STATIC SHEAR
    response and adjudicates its channel against the one usable anchor (KSS/GW eta). RESULT: the
    computable static shear is ORDER-PARAMETER Frank-elastic (wrong-object for eta, same as N43); the
    genuine stress-tensor shear modulus is the GATED induced-EH rigidity C_T*Lambda^2 (N44). So NO
    independent KSS-matched static anchor emerges from statics ==> the usable-anchor count STAYS 1.
    N43's would-change-if (i) is CLOSED-NEGATIVE. The honest ceiling is confirmed with a precise reason:
    the substrate STATICS sees only the order-parameter channel; the stress-tensor transport channel is
    kernel-gated.

    THE MOVE (brief A3 / N43 wci (i)): compute 'a static moment in the STRESS-TENSOR / shear channel'
    on the canted-D4 ordered state -- which WOULD be channel-matched to kss_gw_bracket and could lift the
    count from 1 to 2. The N31/N43 LSWT machinery is the tool.

    THE COMPUTATION (DERIVED-A). A medium shear strain u^1 = eps*x^2 carries the spiral theta = q*X^1
    with the material points (X^1 = x^1 - eps*x^2), so the sheared spiral is theta = q*(x^1 - eps*x^2)
    = a spiral with a TRANSVERSE wavevector tilt (q*, -eps*q*). This is an EXACT kinematic identity:
    a lattice shear of a spiral IS a transverse-wavevector tilt. Hence the static shear-elastic energy is
        G_shear = d2E/deps^2|_0 = q*^2 * d2E/dq_perp^2 = 2 * q*^2 * K_trans  ~ 0.637 J
    with K_trans = (2 cos q* + 4) J the N31/N43 TRANSVERSE (order-parameter) magnon stiffness
    (K_trans ERRATUM 2026-07-26 — see Kc_magnon_stiffness_canted_FM_at_DJ; the prior 0.417 J rode
    the 4 cos q* transcription error; the VERDICT below is value-independent and unchanged). So
    G_shear is built from the ORDER-PARAMETER transverse stiffness -- it is the spin-texture's
    Frank-elastic modulus.
    (PREFACTOR CAVEAT, per N31/N43: the ABSOLUTE number 0.637 J inherits K_trans's conjugate-field-
    normalization dependence -- it is NOT a convention-independent prediction and nothing downstream
    consumes it as one; its whole role is to be wrong-object. The load-bearing content is the STRUCTURE
    G_shear proportional-to q*^2 * K_trans = ORDER-PARAMETER, which is exact and convention-independent.)

    NAME ALL FOUR (wrong-object discipline, N43):
      - OPERATOR : the spiral order-parameter texture (spin-wave phase tilt), NOT the momentum current T_xy.
      - CHANNEL  : ORDER-PARAMETER Frank-elastic (a magnon gradient modulus) -- the SAME channel as N43's
                   chi_theta, NOT the stress-tensor momentum-transport channel.
      - LAYER    : cell-scale QCP.
      - FREQUENCY: omega->0 static.

    THE VERDICT (the located gap, N47). The KSS anchor eta = lim Im G_{T_xy,T_xy}(w)/w is a STRESS-TENSOR
    momentum-TRANSPORT coefficient. Its reactive static partner (the TRUE shear modulus G_inf) is, per
    N44, the induced-EH rigidity C_T*Lambda^2 -- #1-gap GATED and KK-linked to eta (ONE anchor source,
    NOT independent). The computable order-parameter Frank modulus G_shear ~ 0.637 J (K_trans erratum 2026-07-26) is a DIFFERENT object
    (order-parameter, not momentum-transport) ==> wrong-object for eta, exactly N43's pattern. So the
    substrate statics offers no stress-tensor-channel static moment that is simultaneously COMPUTABLE,
    INDEPENDENT, and KSS-MATCHED: the computable static shear is order-parameter (wrong-object); the
    genuine stress-tensor shear modulus is gated (N44). The usable-anchor count STAYS 1.

    WHY THIS IS THE HONEST CEILING (not a fixable gap): a shear of a spin texture on a rigid lattice is
    an order-parameter deformation; the momentum-current T_xy transport (eta) is a driven-dissipative
    kernel object. Statics cannot cross that channel boundary -- exactly the N11-R1/N43 wrong-object wall.

    WOULD CHANGE IF: (i) a substrate momentum-current / Noether stress tensor is constructed whose static
    correlator is BOTH computable from statics AND distinct from the gated C_T*Lambda^2 (none is currently
    constructed -- the two shear moduli in hand are the order-parameter Frank one (computable, wrong-object)
    and the graviton one (gated)); (ii) a grain<->cell transport bridge relates the Frank modulus to eta
    (that bridge is the #1-gap kernel, N43 wci (iii)).
    self-checks: G_shear = 2 q*^2 K_trans > 0 (order-parameter Frank modulus, live from N31 K_trans);
    the over-determination table's usable-anchor count is UNCHANGED at 1 (no KSS-matched anchor added,
    live vs R-150)."""
    import math
    kc = Kc_magnon_stiffness_canted_FM_at_DJ()
    K_trans = kc["K_trans_value"]                 # (2 cos q* + 4) J (order-parameter transverse stiffness; erratum 2026-07-26)
    q_star = math.atan(math.sqrt(2)/6)
    G_shear = 2.0 * q_star**2 * K_trans           # spiral-texture Frank-elastic shear modulus (order-param)
    G_shear_check = 2.0 * q_star**2 * (2.0 * math.cos(q_star) + 4.0)  # per J (K_trans erratum 2026-07-26)

    # channel adjudication: order-parameter Frank (computable) vs stress-tensor transport eta (gated, N44)
    computable_static_shear_is_order_parameter = True    # built from K_trans (order-parameter stiffness)
    true_stress_tensor_shear_modulus_is_gated = True     # = C_T*Lambda^2 (N44), #1-gap
    added_usable_anchor_for_kss = False

    table = kernel_overdetermination_table()
    assert table["n_usable_anchors"] == 1, \
        "A3 must NOT change the usable-anchor count (order-parameter Frank modulus is wrong-object for KSS eta)"
    assert G_shear > 0 and abs(G_shear - G_shear_check) < 1e-12, \
        "G_shear = 2 q*^2 K_trans (order-parameter Frank-elastic shear modulus)"

    return {
        "tier": "FRAMING (channel adjudication + wrong-object verdict) + DERIVED-A (G_shear number, live from N31 K_trans)",
        "G_shear_over_J": G_shear,                # ~ 0.637 (K_trans erratum 2026-07-26)
        "G_shear_formula": "2 q*^2 K_trans (K_trans = (2 cos q* + 4) J, the N31/N43 order-parameter transverse stiffness; erratum 2026-07-26)",
        "kinematic_identity": "a lattice shear of the spiral IS a transverse-wavevector tilt (theta = q*(x^1 - eps x^2)) -- EXACT; so the static shear-elastic response is the ORDER-PARAMETER Frank modulus, NOT the stress-tensor T_xy transport",
        "verdict": "the computable static shear is ORDER-PARAMETER Frank-elastic (wrong-object for KSS eta, same as N43); the genuine stress-tensor shear modulus is the GATED C_T*Lambda^2 (N44, KK-linked to eta, not independent) => NO independent KSS-matched static anchor from statics; N43 wci (i) CLOSED-NEGATIVE",
        "usable_anchor_count": table["n_usable_anchors"],   # stays 1
        "ceiling": "confirms the honest ceiling with a precise reason: substrate statics sees only the order-parameter channel; the stress-tensor transport channel (eta) is #1-gap kernel-gated",
    }


# DEPRECATED ALIAS (V2 Q1, 2026-06-29): the canonical name for the lepton Brannen phase
# δ_L = ⅓arctan(D/J) is `delta_L_from_DoverJ` (above, §19.5). The V1 reading "the Cabibbo angle
# IS the lepton phase, θ_C = δ_L" is REFUTED — the Cabibbo angle gives a MIXING PROBABILITY
# (|V_us|², §19.7 frequency-ratio = m_d/m_s ≈ 0.05), a different mechanism from the Brannen
# generation phase-shift. D/J is now calibrated to the LEPTON sector alone, NOT to Cabibbo.
# The alias is retained for backwards compatibility ONLY; new code should use
# `delta_L_from_DoverJ` (or its synonym `lepton_phase_from_DoverJ` below).
lepton_phase_from_DoverJ = delta_L_from_DoverJ

def cabibbo_angle_rad(D_over_J: float = 0.787) -> float:
    """[DEPRECATED, REFUTED V1 identification — emits DeprecationWarning]
    Alias preserved for back-compat only. The V1 "θ_C = δ_L" reading is REFUTED
    (V2 Q1, 2026-06-29) — use lepton_phase_from_DoverJ for the lepton Brannen
    phase, and the §19.7 frequency-ratio for the Cabibbo PROBABILITY."""
    import warnings
    warnings.warn(
        "cabibbo_angle_rad is DEPRECATED — V1 identification REFUTED (2026-06-29). "
        "Use lepton_phase_from_DoverJ for the lepton Brannen phase, or §19.7 for the "
        "Cabibbo probability. This alias returns δ_L (the lepton phase), NOT a Cabibbo angle.",
        DeprecationWarning, stacklevel=2)
    return delta_L_from_DoverJ(D_over_J)

def cabibbo_vector_vs_spinor(D_over_J: float = 0.787, V_us: float = 0.2243):
    """[DERIVED, inherits D/J input] §19.7: the Cabibbo PROBABILITY reading (magnitude half
    of Path-(i)(d)). |V_us|² is the Born projection (§14.4) of a VECTOR (full-angle) SO(2)
    rotation by δ_L = θ_C on the V₄⊥ generation plane — generations mixing as orbit-phases
    — NOT a §15.4 Spin(3) spinor half-angle overlap.
        vector  sin²(θ_C)   ≈ 0.0486  — matches |V_us|²=0.0503 within the θ_C residual
        spinor  sin²(θ_C/2) ≈ 0.0123  — ~4× too small (data/spinor ≈ 4.1)
    TIER, layered: the STRUCTURE (vector projection on V₄⊥) is [DERIVED] — the §19.1–19.5
    chain sets up generations as V₄⊥ orbit-phases with the full-angle δ_L throughout (no
    half-angle anywhere in that chain), so the vector reading is structurally implied a
    priori; the 4.09× separation from the spinor reading is empirical CONFIRMATION, not the
    source of the choice. The VALUE 0.0486 is [DERIVED, modulo D/J]: it inherits θ_C =
    ⅓arctan(D/J) with D/J=0.787, one of the four §25.1 fitted dials (itself over-determined,
    lepton↔skyrme), so it is NOT parameter-free. The spinor value equals
    1−half_angle_overlap(θ_C)², so it is the genuine §15.4 object (not a strawman) and is
    still ruled out. Internal-consistency win: the mixing geometry (vector) matches what
    generations ARE (V₄⊥ orbit-phases, not Spin(3) spinors).
    SCOPE: magnitude/geometry only. The CKM hierarchy and the ⟨up-triplet|down-triplet⟩
    specificity (why s) are OUT — a held construction (Medium Cl-i), not settled here."""
    theta  = lepton_phase_from_DoverJ(D_over_J)  # the lepton Brannen phase δ_L (V2 Q1: NOT the Cabibbo angle)
    vector = math.sin(theta) ** 2
    spinor = math.sin(theta / 2) ** 2
    data   = V_us ** 2
    return {
        "theta_C":                 theta,
        "vector sin^2(theta_C)":   vector,
        "spinor sin^2(theta_C/2)": spinor,
        "data |V_us|^2":           data,
        "vector_resid":            abs(vector - data) / data,        # ≈ 0.034 (θ_C residual)
        "data/spinor":             data / spinor,                    # ≈ 4.09 (spinor too small)
        "spinor = 1-overlap^2":    1.0 - half_angle_overlap(theta) ** 2,  # ties spinor to §15.4
    }


def _R_axis(axis, ang):
    np = __import__("numpy")
    n = np.array(axis, float); n = n/np.linalg.norm(n)
    K = np.array([[0,-n[2],n[1]],[n[2],0,-n[0]],[-n[1],n[0],0]])
    return np.eye(3) + math.sin(ang)*K + (1-math.cos(ang))*(K @ K)


def amplitude_to_operator(sqrt_m, psi):
    """[F3.2, operator rule] The bedrock-motivated amplitude->operator promotion.

    ⚠ FRAME LABEL (re-identification, see `G_generator`): R_G here rotates about the
    spatial (1,1,1) diagonal cycling {e14,e24,e34}. Per e4 Part A this spatial-G orbit is
    the COLOUR ℤ₃ (mass-blind), NOT the generation operator (generation = the meta-time
    PHASE advance = anti-self-dual triple). This F3 computation is mathematically CORRECT —
    R_G is used only as the §19.7 Brannen mass-phase frame about G — and its conclusion
    (democratic, "needs a NON-G axis") is frame-LABEL-independent; do NOT re-read R_G as a
    spatial generation frame (that conflation is the retired N0 fake-negative).

    Bedrock: the §19.6.1 generator G cycles the orbit = the 120-deg rotation about the
    (1,1,1) diagonal. The Brannen phase psi orients the sector's frame about THIS SAME G
    axis (psi = position along the orbit). The masses are the eigenVALUES sqrt(m_n); psi
    sets the eigenVECTOR orientation about G:  M(psi) = R_G(psi) diag(sqrt_m) R_G(psi)^T.

    This is the rule the §19.7/§19.4 phase geometry actually supplies -- psi is a phase
    along the Z3 orbit, i.e. a rotation about G. It is NOT reverse-engineered to a ladder."""
    np = __import__("numpy")
    RG = _R_axis([1, 1, 1], psi)
    return RG @ np.diag(sqrt_m) @ RG.T


def ckm_from_mass_pinned_psi():
    """[F3.3, THE TEST] Does the mass-orientation psi predict the CKM ladder?  NO.

    Feeding psi through amplitude_to_operator, CKM = U_u^T U_d = R_G(psi_d - psi_u):
    a rotation about G=(1,1,1). [NOTE 2026-08-13, ADJUDICATION2 keeper C1: per-sector psi
    is NOT mass-observable (N=3 harmonic collapse; MAIN brannen_z3_harmonic_collapse_invariant),
    so psi_d - psi_u is convention-pinned MODEL data (the psi->eigenvector promotion), not
    mass-derived; the mass-observable phases are the invariants psi_inv,d/psi_inv,u. The
    conclusion below is UNAFFECTED -- it holds for ANY psi assignment.] Z3 forces
    |V_12| = |V_23| at EVERY beta (one orbit of
    off-diagonals), so the pattern is at most 'two equal + one different' -- DEMOCRATIC
    (all ~ equal, |V_ij| ~ beta/sqrt(3)) at small beta, and approaching a PERMUTATION
    near beta=120deg (Cl-i's no-mixing-modulo-relabeling) -- but STRUCTURALLY NEVER the
    three-DISTINCT graded ladder |V_us|>>|V_cb|>>|V_ub|. The G-axis is the symmetric
    (1,1,1) mode that the Z3-orbit mass data respects, so psi can only rotate ABOUT it.
    A hierarchy needs rotation about a NON-G (Z3-breaking) axis, whose direction is
    eigenVECTOR data NOT contained in the Brannen eigenVALUES.

    Located boundary (deliverable form):
      CKM hierarchy needs the TWT object to have property P = { the relative orientation
      of the up vs down generation frames about a NON-G (Z3-breaking) axis on the 3D
      Q-orbit -- i.e. eigenVECTOR (frame-misalignment) data }, sourced from [bedrock:
      an independent Z3-breaking orientation of the up/down frames, which §19.7's
      Brannen mass structure (a function on the Z3 orbit = G-symmetric/circulant) does
      NOT provide]. The mass phase psi orients only ABOUT G (-> democratic mixing), so
      the mass-pinned psi cannot predict the ladder; CKM needs property P beyond it.

    NOT a falsifier (the rule makes no sharp wrong number -- it gives the wrong STRUCTURE,
    democratic vs hierarchical); NOT a solve. A located gap, sharp enough to build:
    supply the non-G frame-orientation (its bedrock source is the open construction)."""
    np = __import__("numpy")
    def ckm(psd, psu):
        return np.abs(_R_axis([1,1,1], psd).T @ _R_axis([1,1,1], psu))

    # democratic structure for small angle: off-diagonals ~ equal
    rows = {}
    for beta in (math.radians(5), math.radians(10), math.radians(20)):
        A = ckm(beta, 0.0)
        o = [A[0,1], A[0,2], A[1,2]]
        rows[round(math.degrees(beta))] = [round(x,4) for x in o]
        spread = max(o)/max(min(o), 1e-12)
        assert spread < 1.3, "G-rotation must give ~democratic (near-equal) off-diagonals at small beta"
        assert abs(np.mean(o) - beta/math.sqrt(3)) < 0.02, "off-diagonals ~ beta/sqrt(3)"
    # STRUCTURAL (the rigorous claim): Z3 forces |V_12| = |V_23| at EVERY beta ->
    # at most 'two equal + one different', never the three-DISTINCT graded ladder.
    for bd in range(1, 180):
        A = ckm(math.radians(bd), 0.0)
        assert abs(A[0,1] - A[1,2]) < 1e-9, "Z3 forces |V_12| == |V_23| at every beta (one orbit)"
    # a NON-G axis CAN give a hierarchy (but its axis is not in the mass data)
    A_nonG = ckm  # placeholder; demonstrate via _R_axis directly
    Ah = np.abs(_R_axis([1, 0.2, 0.0], 0.23))
    hierarchical_spread = max(Ah[0,1], Ah[0,2], Ah[1,2]) / max(min(Ah[0,1], Ah[0,2], Ah[1,2]), 1e-12)
    assert hierarchical_spread > 5.0, "a NON-G axis yields unequal (hierarchical) off-diagonals"

    return {
        "test_result": "mass-orientation psi gives DEMOCRATIC mixing, NOT the lambda-ladder",
        "G_rotation_offdiagonals_by_beta_deg": rows,
        "Z3_forces_V12_eq_V23": "at every beta (one orbit) -> at most two-equal-one-different, never a 3-distinct graded ladder",
        "predicts_ladder": False,
        "needs_property_P": "relative up/down frame orientation about a NON-G (Z3-breaking) axis (eigenVECTOR data)",
        "P_bedrock_source": "an independent Z3-breaking frame orientation; the Z3-orbit Brannen masses do not supply it",
        "metatime_test_2026_06_21": "the meta-time-phase operator (e4 Part A's reidentified non-R_G generation operator) "
            "is ALSO Z3-SYMMETRIC -> democratic CKM, NOT the ladder (ckm_from_metatime_operator). The e4-dip eps is an "
            "eigenVALUE effect. F3 CONFIRMED and SHARPENED (not closed): the missing ingredient is Z3-breaking AMONG the "
            "three generations (per-generation asymmetry / non-uniform orbit), which no per-sector (b,eps,psi) supplies.",
        "verdict": "ii located boundary: mass-pinned psi cannot predict CKM (NOT a falsifier, NOT a solve); sharpened by the meta-time test",
    }


# ---- meta-time-phase generation operator -> CKM (TASK metatime/item-15; outcome iii) -------
# Exploits e4 Part A's reidentification (generation operator = meta-time phase, NOT spatial R_G).
# RESULT (iii): the operator is ALSO Z3-symmetric -> democratic CKM, NOT the ladder. The e4-dip
# eps is an eigenVALUE effect. F3 sharpened, not closed. Cross-sector: rank-2 present in BOTH
# sectors but does no CKM work (structural presence, no coherent link). Current sector EXTENDED.
def _metatime_sqrt_m(b, eps, psi):
    """Modified-Brannen sqrt-masses on the Z3 orbit (the generation eigenvalues).
    CONVENTION (2026-08-13, ADJUDICATION2 keeper C1): this uses the 2psi-form second
    harmonic cos(2(phi-psi)) with amplitude -sqrt(eps) -- one of FOUR epicycle variants in
    the corpus (the 2psi-form PHASE STRUCTURE is what MAIN mass_measure_from_omega derives,
    FORM only). The quark table's psi-form cos(2phi-psi) with amplitude +eps*b
    inter-converts with this form on the Z3 orbit ONLY UNDER A RE-FIT of (b, eps) -- the
    SAME (b, eps) may NOT be carried across forms (doing so distorts the down sqrt-mass
    ratios by x4.6). (b, eps) fed to this function are values in THIS parametrization; psi
    itself is not fixed by the mass spectrum -- see MAIN
    brannen_z3_harmonic_collapse_invariant."""
    return [1 + b*math.cos(2*math.pi*n/3 - psi)
            - math.sqrt(max(eps, 0))*math.cos(2*(2*math.pi*n/3 - psi)) for n in range(3)]


def _axis_rotation(axis, ang):
    np = __import__("numpy")
    n = np.array(axis, float); n = n/np.linalg.norm(n)
    K = np.array([[0, -n[2], n[1]], [n[2], 0, -n[0]], [-n[1], n[0], 0]])
    return np.eye(3) + math.sin(ang)*K + (1 - math.cos(ang))*(K @ K)


def metatime_generation_operator(b, eps, psi):
    """[TASK metatime 1A] §19.6.1: The concrete 3x3 meta-time-phase generation operator on the
    anti-self-dual triple (e4 Part A 'property Q'). The meta-time phase advances at phi_n=2*pi*n/3
    with the sector's (b,eps,psi) setting the deferent (offset) and the e4-dip (epicycle = tilt);
    eigenvalues are the sqrt(m_n). Built uniformly on the Z3 orbit (same b,eps,psi for all three
    generations, sampled at 120deg) -> Z3-SYMMETRIC; its eigenframe is the meta-time-phase
    orientation R_G(psi), the SAME structural class as F3's R_G (verified independent of (b,eps)).

    SCOPE (defused 2026-06-30 per audit C1): applies to ONE chiral module per call (one Z3 orbit
    on one S±-ideal). The ν (S+ only, neutrino_lightness) and charged-ℓ (S+⊕S−, vminusa_is_spin4_factor_chirality)
    sectors require SEPARATE operators on DIFFERENT modules — not automatically tied to a shared
    basis. Substrate does NOT supply a ν-vs-ℓ basis identification; see pmns_no_substrate_derivation().
    [NOTE 2026-08-13, keeper C1: callers feed the table's ψ-form (b,eps) into _metatime_sqrt_m's
    2ψ/−√ε form — those are ILLUSTRATIVE values in this construction's own parametrization, NOT the
    table's fitted pair re-used (spectra differ across forms). All conclusions here are
    value-independent (the eigenframe is R_G(psi) REGARDLESS of (b,eps)) and stand.]"""
    np = __import__("numpy")
    D = np.diag(_metatime_sqrt_m(b, eps, psi)); R = _axis_rotation([1, 1, 1], psi)
    M = R @ D @ R.T
    assert np.allclose(np.sort(np.linalg.eigvalsh(M)), np.sort(_metatime_sqrt_m(b, eps, psi)), atol=1e-9), \
        "meta-time operator eigenvalues must be the sqrt-masses"
    return M


def ckm_from_metatime_operator():
    """[TASK metatime 1B, outcome (iii) — DERIVED]

    SCOPE (defused 2026-06-30 per audit C1): this construction applies to the QUARK u/d weak
    doublet (both sectors live on the SAME chiral module S+⊕S−, paired by SU(2)_weak). The
    analogous ν-vs-charged-ℓ construction (for V_PMNS) LACKS substrate basis: ν is single-Weyl
    in S+ only (neutrino_lightness), so the weak-isospin doublet structure that grounds the
    "shared metatime basis" assumption is structurally absent on the matter side. See
    pmns_no_substrate_derivation().

    §19.7: CKM = misalignment of the up/down meta-time
    mass-eigenbases, built from the CURRENT-sector (b,eps) of quark_brannen_table with psi FIXED
    by prescription (~delta_L), IDENTICAL for both sectors (no tuned psi_u != psi_d — F3's free
    function held out). [NOTE 2026-08-13, ADJUDICATION2 keeper C1: psi is not fixed by the mass
    spectrum (N=3 collapse; MAIN brannen_z3_harmonic_collapse_invariant), so the prescription pin
    is a convention choice; and the (b,eps) pulled from quark_brannen_table are ψ-form numbers fed
    into the 2ψ/−√ε form here — ILLUSTRATIVE values in this construction's own parametrization,
    not the table's spectra. The conclusion is value-independent: it holds for ANY shared psi and
    ANY (b,eps).] Because each operator's eigenframe is R_G(psi) REGARDLESS of (b,eps), the
    up/down eigenbases differ only by a rotation about the symmetric (1,1,1) axis -> CKM is
    DEMOCRATIC/permutation (V12=V13=0, V23=1), NOT the 3-tier ladder. The one construction giving a
    large 'spread' did so via a FREE axis choice with the WRONG ordering. So the e4-dip mismatch
    sets the MASSES and nothing in the MIXING. MISSING INGREDIENT (sharpened): Z3-breaking AMONG
    the three generations (a per-generation asymmetry / non-uniform orbit), absent from the
    per-sector (b,eps,psi). FIXED: b_u,eps_u,b_d,eps_d (mass-set), psi (prescription, same u&d);
    FREE: none."""
    np = __import__("numpy")
    t = quark_brannen_table()
    b_d, eps_d, _ = t["down (b,ε,K)"]; b_u, eps_u, _ = t["up (b,ε,K)"]
    psi = 2.0/9.0
    def basis(b, eps):
        M = metatime_generation_operator(b, eps, psi)
        w, V = np.linalg.eigh(M); return V[:, np.argsort(w)]
    C = np.abs(basis(b_u, eps_u).T @ basis(b_d, eps_d))
    ladder = (C[0, 1] > C[1, 2] > C[0, 2]) and C[0, 1] > 0.15 and C[0, 2] < 0.01
    assert not ladder, "the measured ladder (V12>>V23>>V13) must NOT emerge with psi fixed"
    Vu, Vd = basis(b_u, eps_u), basis(b_d, eps_d)
    sym = np.array([1, 1, 1.])/math.sqrt(3)
    symmetric_axis_preserved = abs(abs(float(sym @ (Vu.T @ Vd @ sym))) - 1.0) < 1e-6
    assert symmetric_axis_preserved, "Z3-symmetry forces a symmetric-axis (democratic) misalignment"
    return {
        "fixed_inputs": "b_u,eps_u,b_d,eps_d (mass-set); psi=2/9 (prescription, same u&d)",
        "free_inputs_used": "none (no tuned psi_u != psi_d)",
        "CKM_offdiagonals_psi_fixed": {"V12": round(float(C[0, 1]), 4), "V13": round(float(C[0, 2]), 4),
                                       "V23": round(float(C[1, 2]), 4)},
        "ladder_emerges": False,
        "eigenbasis_misalignment": "rotation about the symmetric (1,1,1) axis -> DEMOCRATIC",
        "missing_ingredient": "Z3-breaking AMONG the three generations (per-generation asymmetry); "
                              "b,eps,psi are per-sector (Z3-symmetric) and cannot supply it",
        "verdict": "iii: meta-time phase fixes the MASSES but not the MIXING; e4-dip is NOT the CKM source",
    }


def baryon_rank2_mode_cross_sector():
    """[TASK metatime cross-sector, CKM-blind] §19.7: The rank-2 (l=2, quadrupole) deformation in v14's
    baryon sector vs the rank-0 part, from baryon physics ALONE: c0*sum 1/(A_iA_j) is
    spin-independent -> rank-0 (geometric monopole/overlap); k*sum sigma/(A_iA_j) is the spin-tensor
    term (sigma: spin-1 pairs +1 vs the spin-0 good diquark -3; drives the decuplet-octet/Delta-N
    splitting) -> the rank-2 (spin-tensor) deformation. The generation epicycle eps (cos2phi tilt)
    is ALSO rank-2 -> the rank-2 e4-orthogonal deformation is STRUCTURALLY PRESENT in both sectors
    (same geometric category). BUT the core (iii) shows this mode does NOT generate the CKM ladder,
    so 'one mode does coherent work in BOTH the CKM ladder and the baryon spectrum' does NOT hold:
    there is no CKM-ladder work for it to do. STRUCTURAL PRESENCE, NO COHERENT CKM LINK. The test is
    STRUCTURAL (same operator type), not instance (numbers differ: constituent vs current)."""
    return {
        "rank0_monopole_term": "c0 * sum 1/(A_i A_j)  (spin-independent geometric overlap)",
        "rank2_tensor_term": "k * sum sigma/(A_i A_j)  (spin-tensor; decuplet-octet / Delta-N splitting)",
        "generation_rank2": "the epicycle eps (cos2phi tilt) -- same rank-2 e4-orthogonal category",
        "structural_presence_both_sectors": True, "coherent_CKM_link": False,
        "reason": "core (iii): the rank-2 e4-dip does NOT produce the CKM ladder, so there is no "
                  "CKM-ladder work for a shared mode to do (structural match only, no coherent link)",
        "verdict": "rank-2 mode present in both sectors; NO coherent cross-sector CKM link (core is (iii))",
    }


def ckm_metatime_status():
    """[F3 status update] F3 is NOT closed by the meta-time operator: it (the 'non-R_G' operator F3
    was missing) is ALSO Z3-symmetric, so it inherits the democratic result. The gap is SHARPENED:
    the CKM ladder needs Z3-breaking AMONG the three generations (per-generation asymmetry /
    non-uniform orbit), which no per-sector parameter (b,eps,psi) -- including the e4-dip eps --
    supplies. (Lead: whether that per-generation angular asymmetry is determined by the colour map.)"""
    return {
        "F3_status": "located gap CONFIRMED and SHARPENED (not closed)",
        "tested": "meta-time-phase operator with e4-dip; current-sector (b,eps); psi fixed",
        "result": "democratic (Z3-symmetric eigenbasis); e4-dip is an eigenVALUE effect",
        "sharpened_missing_ingredient": "Z3-breaking AMONG the three generations (per-generation "
                                        "asymmetry / non-uniform 120deg orbit), not a per-sector (b,eps,psi)",
        "secondbuild_2026_06_23": "the non-uniform-orbit thesis is REFUTED as the CKM source. Level 1 "
            "(CONSTRUCTION-INDEPENDENT, banks): the orbit operators are circulant -> [M_u,M_d]=0 -> democratic, so the "
            "metatime result is strengthened from an R_G-dependent argument to a circulant/Spin(4) one "
            "(updown_mass_operators_commute). Level 2 (CONTINGENT on weak-isospin = su(2)+, asserted not derived): weak "
            "isospin is zero on the generation space and colour is up/down-blind, so the thesis's mechanism supplies no "
            "per-weak-isospin rotation — but a different weak-isospin identification overlapping V revives it. The located "
            "gap: a per-weak-isospin, NON-orbit, MULTI-AXIS frame rotation. LOAD-BEARING open item: derive weak-isospin = su(2)+.",
        "thirdbuild_2026_06_23_CORRECTION": "TASK weak-isospin → (iii) UNDER-DETERMINED; the Level-1 PHYSICAL "
            "democratic conclusion above is CORRECTED (held, not banked). The circulant THEOREM stands as algebra, but "
            "physical democratic CKM also needed the anti-self-dual gen-space — which CONTRADICTS §8.3's stated quark "
            "generations 𝔔={e14,e24,e34}. weak_isospin_rank_table: su(2)+ is rank-0 (democratic) ONLY on anti-self-dual; "
            "on §8.3's stated Q-orbit EVERY embedding is rank-3 (mixing-reachable). So on the paper's own generations the "
            "structure LEANS toward mixing (away from the democratic tension) — but rank room is NOT the ladder. The CKM "
            "gate is now the derived {chiral projector + quark gen-space} pair (weak_isospin_verdict).",
        "fourthbuild_2026_06_23_RESOLVED": "the CKM arc closes the (iii) to (ii) LOCATED: the meta-time E-phase IS the generation label [2026-07-02 sweep: now CONDITIONAL on the E-channel reading — R-127/R-128 lock the observer-visible mass phase to winding blades; the democratic NEGATIVE itself is carried by the lock-independent exact I₄:Q→L scalar fact, formalization (A) of chirality_does_not_source_P] and is SHARED up/down (E central ⇒ blind to T₃) ⇒ Y_u,Y_d circulant ⇒ democratic — derived, not fit. CP ARROW derived (+e₄). The hierarchy AND the CP magnitude reduce to property P = a NON-CIRCULANT up/down difference (SHARPENED: a different *circulant* phase still gives democratic), sourced by the Θ_rel channel SHARED with colour-U(3). F3 (√(mᵢ/mⱼ)/Λ) additionally gates the magnitudes. See ckm_arc_channel_identity_and_verdict.",
    }


def gate_B_branch():
    """[rank analysis → (iii); SUPERSEDED to (ii) LOCATED by the CKM arc (see RESOLVED_ below); the prior
    (a)/democratic bank is HELD, NOT banked.] The circulant THEOREM stands as algebra (orbit-function operators are
    simultaneously diagonalizable). But the PHYSICAL conclusion 'CKM is democratic' also required (i)
    weak isospin acting as rank-0 on the generation space AND (ii) the generation space being the chiral
    anti-self-dual triple — and (ii) was used WITHOUT checking §8.3's stated quark generations 𝔔=
    {e14,e24,e34}. The rank table (rank_table) is decisive: weak-isospin = su(2)+ is rank-0 (democratic)
    ONLY on the anti-self-dual space; on §8.3's STATED Q-orbit generations EVERY embedding (including clean
    su(2)+) is rank 3 (mixing-reachable). Democratic occupies 1 of 6 cells — the (su(2)+, anti-self-dual)
    pairing §8.4 explicitly warns against (conflating the chiral and orbit splits). So the physical
    democratic conclusion does NOT bank; on the paper's own stated generation space the structure LEANS
    toward mixing-reachable — but 'reachable' is rank room, NOT the ladder (§19.7 derives one calibrated
    Cabibbo angle; the V_us≫V_cb≫V_ub magnitudes are open). Outcome (iii): under-determined, decided only
    by a derived {chiral projector + quark gen-space} pair."""
    return {
        "outcome": "(iii)→(ii) RESOLVED — the RANK analysis alone gave (iii); SUPERSEDED by the CKM arc "
                   "(2026-06-23) → (ii) LOCATED; democratic is GENUINE (circulant linchpin), residual = Θ_rel (#1 gap)",
        "circulant_theorem": "STANDS as algebra (orbit-function operators commute) — but this alone does "
                             "NOT give physical democratic CKM",
        "why_democratic_does_not_bank": "it needed BOTH weak-isospin rank-0 AND the anti-self-dual gen-space; "
                                        "the latter contradicts §8.3's stated Q-orbit; rank table shows su(2)+ "
                                        "is rank-0 ONLY on anti-self-dual, rank-3 on §8.3's stated Q-orbit",
        "rank0_cells": "1 of 6 — (su(2)+, anti-self-dual), the §8.4-warned chiral/orbit conflation",
        "lean": "on §8.3's stated generations, EVERY embedding is rank-3 → structure leans MIXING-REACHABLE "
                "(away from the democratic tension) — but room is NOT the ladder (§19.7: one calibrated angle)",
        "two_under_determinations": "U1 SU(2)_L embedding (su(2)+ §8.4 vs 𝔏 §10.5; chiral projector [CANDIDATE]/"
                                    "Paper 2) + U2 quark gen-space (𝔔 §8.3 vs anti-self-dual; §8.4 different splits)",
        "located_CKM_gate": "a DERIVED consistent pair {chiral projector (§18.3b), quark gen-space (§8.3 vs §8.4)} "
                            "that together fix the rank — then the framework predicts democratic (tension) or "
                            "hierarchical (consistent): a sharp data-facing near-falsifier",
        "RESOLVED_2026_06_23": "the CKM arc DERIVED the pair {sector S₊ via +e₄, co-rotation-matched gen-space} → "
                               "(ii) LOCATED. The democratic is the GENUINE result (NOT the trivial (su(2)+,anti-self-dual) "
                               "cell — that is unreachable by co-rotation; it is the circulant/shared-phase mechanism), "
                               "and it locates ALL observable content in the Θ_rel residual SHARED with colour-U(3). See "
                               "ckm_arc_sector_and_corotation / ckm_arc_circulant_linchpin / ckm_arc_channel_identity_and_verdict.",
    }


def ckm_frame_fit_is_vacuous():
    """[GUARD — refutes a recurring fake-positive] §19.7: A 'fix' that writes V_CKM = F† U F with U ∈ U(3)
    FITTED to the data (reporting a tiny loss + the right Jarlskog J) carries ZERO predictive content:
    F is a fixed unitary (the circulant DFT eigenframe), so U = F V F† exists for ANY target unitary V
    — the parameterization is a surjection onto U(3) and fits anything (a random unitary as well as the
    empirical CKM) to machine precision. The fitted J is fitted along with the complex entries, not
    'automatically generated'. Such a fit confirms only what weak_isospin_verdict (iii) already
    established — TWT's complex structure (E=e12345) leaves U(3) ROOM for a hierarchical, CP-violating
    CKM (mixing-REACHABLE) — and does NOT close the located gap, which is to DERIVE U (the chiral
    projector + quark gen-space), not fit it. self-check: F†(F V F†)F = V to 1e-12 for a random V and a
    hierarchical CKM."""
    np = __import__("numpy"); import math
    w = np.exp(2j*np.pi/3)
    F = np.array([[w**(j*k) for k in range(3)] for j in range(3)], complex)/np.sqrt(3)
    def reconstructs(V):
        U = F @ V @ F.conj().T
        return float(np.max(np.abs(F.conj().T @ U @ F - V))), bool(np.allclose(U.conj().T @ U, np.eye(3)))
    q, _ = np.linalg.qr(np.random.randn(3, 3) + 1j*np.random.randn(3, 3))
    errR, uR = reconstructs(q)
    s12, s23, s13, d = 0.225, 0.0408, 0.00369, 1.2
    c12, c23, c13 = math.sqrt(1-s12**2), math.sqrt(1-s23**2), math.sqrt(1-s13**2)
    V = np.array([[c12*c13, s12*c13, s13*np.exp(-1j*d)],
                  [-s12*c23-c12*s23*s13*np.exp(1j*d), c12*c23-s12*s23*s13*np.exp(1j*d), s23*c13],
                  [s12*s23-c12*c23*s13*np.exp(1j*d), -c12*s23-s12*c23*s13*np.exp(1j*d), c23*c13]], complex)
    errC, uC = reconstructs(V)
    assert errR < 1e-12 and errC < 1e-12 and uR and uC
    return {
        "claim_tested": "V_CKM = F† U F with U∈U(3) fitted (reported loss≈1e-7, J≈3e-5)",
        "fits_random_unitary_err": f"{errR:.1e}", "fits_hierarchical_CKM_err": f"{errC:.1e}",
        "verdict": "VACUOUS — U=FVF† exists for ANY V; the parameterization is a surjection onto U(3), "
                   "fits anything to machine precision; the loss and J are fitted, not derived",
        "what_it_confirms": "only the weak-isospin (iii) lean — U(3) ROOM (mixing-reachable) via the "
                            "complex structure E; NOT a derivation",
        "located_gap_unchanged": "DERIVE U (the chiral projector + quark gen-space) — not fit it "
                                 "(gate_B_branch, weak_isospin_verdict)",
    }


def ckm_arc_circulant_linchpin():
    """[DERIVED — CKM arc Phase B, Editor clean-room verified] Why CKM comes out democratic: the complex
    structure E (=e12345, central) commutes with the weak isospin ⇒ E is blind to T₃ ⇒ the meta-time
    GENERATION phase is SHARED between up and down ⇒ Y_u, Y_d are circulant in the SAME basis ⇒ they commute
    ([Y_u,Y_d]≈0) ⇒ V_CKM = identity (democratic). A DERIVED negative (the absence of non-circulance), NOT a
    fit. ★ SHARPENING (Editor): breaking democratic requires property P that is genuinely NON-CIRCULANT
    (breaks the ℤ₃ orbit symmetry). An up/down-different *circulant* phase STILL commutes and STILL gives
    democratic — so the consolidation's 'up/down-different phase' is insufficient as stated; Θ_rel must supply
    NON-CIRCULANCE, a stronger and more specific requirement. self-check: shared & different-circulant phases
    both commute (<1e-9); only a non-circulant term mixes (>0.1).
    NOTE (2026-06-28): the circulant theorem is algebra on a UNIFORM ℤ₃ orbit — which holds for LEPTONS,
    where ε=0 (the symmetric circle) is DERIVED-structural-conditional (√m=r² measure + lepton τ=0,
    `epicycle_reading_dependent`) while the Koide value K=2/3⟺c=√2 is INPUT (unforced). For QUARKS the
    protected sub-harmonic windows are asymmetrically placed
    (ε≠0, `quark_brannen_table`), so the orbit is non-uniform and need not give democratic CKM; the
    meta-time-phase-Z3 and protected-sub-harmonic readings are COMPATIBLE, not in conflict (the
    asymmetry is the quark-only deviation). See TWT_DEFECT_CKM_GLUON.md §2/§21.

    SCOPE (defused 2026-06-30 per audit C1): "E central blind to T₃ ⇒ shared phase" was DERIVED
    for a weak-isospin DOUBLET PAIR on the SAME chiral module (u/d, both S+⊕S−). It does NOT lift
    to ν vs charged-ℓ as the basis for V_PMNS: the substrate places ν in S+ only
    (neutrino_lightness) while charged-ℓ occupies S+⊕S−. The doublet partner of ν on the matter
    side is the wave-decoupled sterile RH (§19.8.3), NOT the charged lepton. The shared-Z3-basis
    premise across S+ and S+⊕S− chirally-asymmetric modules is NOT substrate-derived; see
    pmns_no_substrate_derivation()."""
    np = __import__("numpy"); w = np.exp(2j*np.pi/3)
    def circ(c): return np.array([[c[(i-j) % 3] for j in range(3)] for i in range(3)], complex)
    base = [1.0, 0.3*np.exp(1j*0.7), 0.2*np.exp(-1j*0.4)]
    Yu = circ(base)
    same = float(np.linalg.norm(Yu @ circ(base) - circ(base) @ Yu))
    diff = circ([1.1, 0.4*np.exp(1j*1.3), 0.15*np.exp(1j*0.9)]); diffn = float(np.linalg.norm(Yu @ diff - diff @ Yu))
    P = np.array([[0, 0.18j, 0], [-0.18j, 0, 0.05j], [0, -0.05j, 0]], complex)
    ncn = float(np.linalg.norm(Yu @ (diff + P) - (diff + P) @ Yu))
    assert same < 1e-9 and diffn < 1e-9 and ncn > 0.1
    return {
        "why_democratic": "E (central) blind to T₃ ⇒ meta-time generation phase shared up/down ⇒ Y_u,Y_d "
                          "circulant in one basis ⇒ commute ⇒ V=identity",
        "derived_not_fit": "the ABSENCE of non-circulance was derived, not back-solved from CKM",
        "sharpening_property_P": "must be genuinely NON-CIRCULANT (break the ℤ₃ orbit symmetry); an up/down-"
                                 "different *circulant* phase still commutes → still democratic",
        "commutators": {"shared_phase": f"{same:.0e}", "different_circulant": f"{diffn:.0e}", "non_circulant": f"{ncn:.1e}"},
    }

def ckm_arc_channel_identity_and_verdict():
    """[CKM arc Phase C/D — the verdict, Editor clean-room verified] Outcome (ii) LOCATED — TWT does NOT
    close CKM. DERIVED scaffolding: the sector S₊ + projector ½(1+I₄) (Phase A); the E-valuedness; the
    circulant/democratic structure (Phase B); the CP ARROW = the +e₄ substrate parity; and the
    colour↔generation CHANNEL CORRESPONDENCE — colour=e₄·L, generation=I₄·L with I₄=e₁₂₃·e₄: the
    lepton↔quark SECTOR + Z3-CYCLE + Cartan CORRESPOND under the exact I₄ Hodge tie [DERIVED-STRUCTURAL,
    i4_generation_overdetermination]. ⚠ NOT "literally the same channel derived": that CKM property-P
    BREAKS in that same {λ₃,λ₈} Cartan (i.e. the CKM non-circulance invariant = the Hodge-image of colour's
    |Σc²|²) is NOT computed to colour's standard — it is ASSERTED/CANDIDATE, a convergent-consistency BINARY,
    NOT a second derivation (cf. theta_rel_pinnability_from_data: "materially weaker than over-determination;
    pins a binary, not a value"; the gate-free closer is the owed ckm_P_cartan_direction, worklist).
    LOCATED: the entire observable content (mixing angles, λ-hierarchy, J magnitude) reduces to property P =
    a NON-CIRCULANT up/down difference, sourced by the I₄/§9.6 coset-Cartan Θ_rel channel — the SAME residual
    as colour-U(3) (CKM is the SECOND arc to terminate on Θ_rel). NOT closed: Θ_rel has no forward model
    [UNDEFINED]; the dynamical merge (one Θ_rel sources BOTH colour-breaking and CKM property P) is
    [CANDIDATE]; the exhaustiveness (Θ_rel the unique source of P) is [ASSERTED]; the magnitudes additionally
    need F3 (the √(mᵢ/mⱼ)/Λ suppression). The derived structure predicts the WRONG CKM — |V_us|/|V_cb|≈1
    (democratic) vs ≈5.49 (data) — the near-falsifying tension at FULL WEIGHT.

    ★★ THE EXHAUSTIVENESS CLAIM IS WEAKENED, 2026-08-27 (RUL-110 / family-tree node V3-1b —
    M-3a GRANTED, the drive-referenced two-rate defect rotor). "Θ_rel is the unique source of P"
    was already recorded [ASSERTED], never computed. Under the adopted two-rate form a SECOND
    CANDIDATE SOURCE-SLOT now exists: the blast radius (UNLOCK-4) computes that the ONLY
    directions which both break ℤ₃-equivariance (property P's defining requirement) and stay
    BLIND to weak isospin (leaving the weak-sector arc intact) are the ASD directions OFF the
    (1,1,1) generation axis — the banked central carrier E is provably not one of them (central
    ⇒ ℤ₃-equivariant ⇒ circulant ⇒ democratic). This is a WEAKENING of the exhaustiveness claim
    and is recorded as such, NOT a win: it shows WHERE such a source could live, not that the
    two-rate form SUPPLIES one, and the magnitude remains Θ_rel / #1-gap. ★ THE AXIS PICK IS
    NOT GRANTED — putting the second rotation on a pure-ASD off-(1,1,1) direction is a FURTHER
    choice (recorded CANDIDATE at node V3-1b, not picked); nothing here licenses it. Reverting
    V3-1b evaporates the slot and restores the single-candidate reading. Record:
    knowledge/audit/generations_arc_2026-08-23/M3_BLAST_RADIUS_2026-08-26.md.

    self-check: I₄=e₁₂₃·e₄; data ratio ≈5.49 vs democratic O(1)."""
    assert _blade_mul((1, 2, 3), (4,)) == (1, (1, 2, 3, 4))
    ratio = 0.2252 / 0.0410
    assert 5.0 < ratio < 6.0
    return {
        "outcome": "(ii) LOCATED — TWT does NOT close CKM",
        "derived_scaffolding": "sector S₊ + projector ½(1+I₄); E-valuedness; circulant/democratic; CP arrow=+e₄; "
                               "colour↔generation CHANNEL correspondence (I₄=e₁₂₃·e₄ ⇒ Cartan {λ₃,λ₈} CORRESPONDS; "
                               "breaking-in-that-channel ASSERTED, not computed to colour's standard)",
        "located_residual": "ALL observable content (angles, λ-hierarchy, J) → property P = a NON-CIRCULANT "
                            "up/down difference, sourced by the I₄/§9.6 Θ_rel channel",
        "shared_with_colour": "the SAME Θ_rel residual as colour-U(3) — CKM is the SECOND arc to terminate there "
                              "(channel identity DERIVED; dynamical merge [CANDIDATE]; exhaustiveness [ASSERTED])",
        "exhaustiveness_weakened_2026_08_27": (
            "RUL-110 / family-tree V3-1b (M-3a GRANTED — the drive-referenced two-rate defect rotor). "
            "'Θ_rel is the UNIQUE source of P' was always [ASSERTED], never computed, and it is now "
            "WEAKER: under the adopted two-rate form a SECOND CANDIDATE SOURCE-SLOT exists — the ASD "
            "directions OFF the (1,1,1) generation axis, the only ones that both break ℤ₃-equivariance "
            "(property P's requirement) and stay blind to weak isospin (blast radius UNLOCK-4). The "
            "banked central E is provably not one of them (central ⇒ ℤ₃-equivariant ⇒ circulant ⇒ "
            "democratic). Recorded as a WEAKENING, not a win: it locates where such a source COULD "
            "live, not that the two-rate form supplies one, and the magnitude stays Θ_rel / #1-gap. "
            "★ THE AXIS PICK IS NOT GRANTED — a pure-ASD off-(1,1,1) second rotation is a FURTHER "
            "choice, recorded CANDIDATE at node V3-1b and NOT picked. Reverting V3-1b evaporates the "
            "slot. Record: generations_arc_2026-08-23/M3_BLAST_RADIUS_2026-08-26.md"),
        "magnitude_gate": "additionally needs F3 (√(mᵢ/mⱼ)/Λ suppression)",
        "tension": f"predicts WRONG CKM: |V_us|/|V_cb|≈1 (democratic) vs {ratio:.2f} (data) — FULL WEIGHT",
        "does_not": "close CKM / predict any observable / fit (democratic found, not patched) / un-gate the "
                    "collider gate / close colour-U(3)",
    }


# ---- §19.7b  Cl-i: the I4 generation over-determination + CKM-from-triplet-overlap (located gap) ----
# TASK Cl-i (Hard/careful two-build). (b) the I4 Hodge map ties lepton<->quark generations EXACTLY;
# (a) the CKM hierarchy is a LOCATED GAP (ii-a) blocked on worklist F3 (the unexposed §19.7 ψ/Λ).
def i4_generation_overdetermination():
    """[DERIVED, exact] §8.2/§19.6: the I4 Hodge map ties the lepton and quark
    GENERATION structures together exactly (they are NOT independent).

    What it fixes (all verified, exact):
      * I4^2 = +1  (Cl(4,0) pseudoscalar) -> the map is an involution.
      * I4·{e12,e13,e23} is a bijection onto the quark Q-bivectors {e34,e24,e14}
        (and e4·{e12,e13,e23} = the quark trivectors {e124,e134,e234}).
      * I4 sends the spatial cycle generator G=(e12+e23+e31)/sqrt3 (the COLOUR Z3
        generator per R-072; historically read as a generation cycle) to
        ±(the Q-orbit diagonal (e14+e24+e34)/sqrt3) -> the L-orbit Z3 cycle and the
        Q-orbit Z3 cycle are the SAME cycle under Hodge.
    Consistency: EXACT (0% -- an algebraic identity). It CONFIRMS count-3 CONSISTENCY
    across leptons and quarks (the Hodge bijection is one-to-one between L_BIVECTORS
    and Q_BIVECTORS) GIVEN the lepton-side ASD identification; it does NOT independently
    derive the count itself — the count-3 derivation residual lives in
    `why_three_generation_triple` (LOCATED). What is locked here is the shared cyclic
    Z3 structure (lepton Z3 ↔ quark Z3 same cycle); it does NOT fix the Brannen
    amplitudes/phases.

    Is this the ~1.1% over-determination? NO -- DISTINCT. The ~1.1% is the NUMERICAL
    agreement DoverJ_from_lepton_masses (0.787) vs DoverJ_from_skyrme (0.778) across the
    unrelated lepton-mass and baryon-Skyrme sectors. This I4 constraint is an EXACT BLADE
    identity, a different (structural) leg. It supplies the COMMON SPACE that makes the
    overlap in ckm_from_triplet_overlap well-defined (rules out FAIL there)."""
    out = {}
    out["I4^2"] = I4_squared()
    assert I4_squared() == (1.0 * e()), "I4^2 must be +1 (exact)"
    imgsQ = {nm: I4 * b for nm, b in L_BIVECTORS.items()}
    assert all(is_Q_bivector(v) for v in imgsQ.values())
    assert all((I4 * (I4 * b)) == b for b in L_BIVECTORS.values())
    tri = {nm: e(4) * b for nm, b in L_BIVECTORS.items()}
    assert {tuple(sorted(next(iter(v.as_dict())))) for v in tri.values()} == {(1,2,4),(1,3,4),(2,3,4)}
    G = G_generator(); GQ = (e(1,4)+e(2,4)+e(3,4)) * (1.0/math.sqrt(3.0))
    assert (I4 * G) == GQ or (I4 * G) == (-1.0)*GQ
    out["maps_lepton_cycle_to_quark_cycle"] = True
    djl, djs = DoverJ_from_lepton_masses(), DoverJ_from_skyrme()
    out["DoverJ_lepton"], out["DoverJ_skyrme"] = round(djl,5), round(djs,5)
    out["DoverJ_gap_pct"] = round(abs(djl-djs)/djs*100, 2)
    assert out["DoverJ_gap_pct"] > 0.5
    out["I4_constraint_error_pct"] = 0.0
    out["is_the_1.1pct_leg"] = False
    out["verdict"] = "exact structural over-determination (generation count + shared Z3 cycle); DISTINCT from the ~1.1% D/J leg"
    return out


# TASK path-(i)/#14 (gate-free Layer-1, 2026-06-24). The I4 Hodge map is AMPLITUDE-BLIND:
# it refutes 'quark-Koide = I4·(lepton-Koide)' as a value relation, and the grade-split
# DERIVES why (the lepton mass-Koide's Hodge content routes to quark CHARGE, not mass).
def i4_lepton_quark_amplitude_blind() -> dict:
    """[DERIVED] §8.2/§19.4/§19.6 — item #14 / exploration path (i).
    DERIVED CORE (substrate-specific, exact): the grade-2 lepton mass-structure has its
    Hodge image SPLIT ACROSS TWO GRADES, and the K=2/3 coincidence lands on the grade-3
    CHARGE leg, NOT on a quark mass-Koide. CONSEQUENCE (generic-given-that-split): I4 is
    amplitude-blind, so the path-(i) conjecture 'quark-Koide-analog = I4·(lepton-Koide)'
    is FALSE as a VALUE relation. (The amplitude-blindness alone is generic — any blade
    isometry can't fix scalar amplitudes; what is substrate-specific is the two-grade split
    that ROUTES the lepton mass-Koide's image onto quark CHARGE, which is why no quark
    mass-Koide is in the I4-image to begin with.)

    Engine facts (exact):
      * Hodge grade-split of the grade-2 L-bivectors (the lepton generation/mass space):
          I4· : grade-2 L-biv -> grade-2 Q-biv   (the GENERATION/mixing space; CKM/PMNS)
          e4· : grade-2 L-biv -> grade-3 trivector (the CHARGE/colour slots)
        => the lepton mass-structure (grade 2) has TWO Hodge images at DIFFERENT grades.
      * The grade-3 (charge) leg carries the K=2/3 <-> Q_u=2/3 coincidence
        (koide_charge_unification): the '2/3' that is a lepton mass-Koide at grade 2 is an
        up-quark CHARGE at grade 3 (both = 2/N = (N-1)/N at N=3). The Hodge dual of the
        lepton MASS-Koide is quark CHARGE, NOT a quark mass-Koide.
      * Amplitude-blindness: the I4/e4 maps are blade isometries -- they carry the Z3
        cycle, count, and charge-grade, NOT the Brannen scalar amplitudes (Lambda,b,eps,psi).

    Data confirmation that I4 does NOT carry the Koide VALUE (would force quark K = 2/3):
      lepton K=2/3 (b=sqrt2);  down K=0.732 (b=1.172);  up K=0.85/0.99 (b=1.033).
      Quark K's != 2/3 and quark b's != sqrt2 => no isometry maps them => the path-(i)
      conjecture 'quark-Koide = I4·lepton-Koide' is FALSE as a value relation. (Quark K's
      are scheme/scale-dependent INDICATORS, top-contaminated -- NOT TWT verifiers; used
      here only to witness the non-equality, which holds for any reading.)

    Consequence (LOCATED-GAP N12): the amplitude-sector input item #14 needs
    (v/f_pi ~ m_p/m_e; the 'single D4 Q/L stiffness ratio') lives OUTSIDE the Hodge map.
    Its TIER is itself open (forked): a Layer-1 D4 24-cell triality ratio [gate-free; the
    re-attack: compute it, test vs b_d/b_l=0.829, b_u/b_l=0.730 parameter-free] vs a
    Layer-2 driven-NESS elastic-modulus ratio [gap-gated]. The path-(i) STRUCTURAL legs
    (cycle tie + charge-grade coincidence) are gate-free and DONE; the AMPLITUDE leg is a
    located gap, NOT a free Layer-1 win (corrects the strategic map).

    FRAMING — DEFUSED 2026-06-30 per audit C1 (replaces prior amplitude-blindness PMNS≠CKM
    reconciliation, which is internally contradicted by ckm_arc_circulant_linchpin's 2026-06-28
    sharpening): **PMNS is OUTSIDE the I4-Hodge map's scope.** I4· ties L-orbit (charged-ℓ-orbit)
    ↔ Q-orbit (quark-orbit) — a cross-sector tie. It does NOT identify a basis between ν and
    charged-ℓ within the L-orbit. The ν-vs-charged-ℓ shared-basis identification needed for
    V_PMNS to be well-defined is NOT substrate-derived: ν is single-Weyl in S+ only
    (neutrino_lightness, paper §19.8.2) while charged-ℓ occupies S+⊕S− (8-dof Dirac), so the
    weak-isospin doublet structure that grounds ckm_arc_circulant_linchpin's "E central blind
    to T₃ ⇒ shared phase" is ABSENT on the matter side for PMNS. See pmns_no_substrate_derivation().

    derived-vs-generic: substrate-specific = the exact I4/e4 grade-split + the N=3
    coincidence; the 'isometry can't fix scalar amplitudes' step is GENERIC (true of any
    blade isometry) -- which is exactly WHY the amplitude leg needs a non-Hodge input."""
    out = {}
    # (1) exact Hodge grade-split: I4 stays grade 2 (Q-biv), e4 raises to grade 3 (trivector)
    assert I4_squared() == (1.0 * e()), "I4^2 must be +1"
    for nm, b in L_BIVECTORS.items():
        img_I4 = I4 * b
        img_e4 = e(4) * b
        assert is_Q_bivector(img_I4), f"I4·{nm} must be a Q-bivector (grade 2)"
        assert all(len(bl) == 3 for bl, _ in img_e4.terms), f"e4·{nm} must be a trivector (grade 3)"
    out["I4_leg_grade"] = 2          # generation/mixing space (CKM/PMNS) -- amplitude-blind
    out["e4_leg_grade"] = 3          # charge/colour slots -- carries the 2/3 coincidence
    # (2) the grade-3 charge leg: K=2/3 <-> Q_u=2/3 at N=3 (the real lepton-mass<->quark-charge tie)
    ku = koide_charge_unification()
    assert ku["coincide_at_N=3"], "K=2/3 must coincide with Q_u=2/3 at N=3"
    out["lepton_massKoide_to_quark_charge"] = (ku["K_N=2/N"], ku["Qu_N=(N-1)/N"])
    # (3) amplitude-blindness witnessed by data: quark K != lepton K=2/3
    KL = koide_K((M_E, M_MU, M_TAU))
    Kd = koide_K(PDG_QUARK_MASSES["down"])
    Ku = koide_K(PDG_QUARK_MASSES["up"])
    assert abs(KL - 2.0/3.0) < 2e-3, "lepton Koide must be 2/3"
    assert abs(Kd - 2.0/3.0) > 0.02 and abs(Ku - 2.0/3.0) > 0.02, \
        "quark Koide K's must NOT equal 2/3 (amplitude-blindness: I4 does not carry the value)"
    out["K_lepton"], out["K_down"], out["K_up"] = round(KL, 4), round(Kd, 4), round(Ku, 4)
    out["quark_Koide_is_I4_image_of_lepton_Koide"] = False
    out["amplitude_blind"] = True
    out["located_gap"] = "N12: Q/L stiffness ratio is non-Hodge; tier forked (Layer-1 24-cell vs Layer-2 NESS)"
    out["verdict"] = ("DERIVED core: the two-grade Hodge split routes the lepton mass-Koide's "
                      "image onto the grade-3 quark-CHARGE leg (K=2/3<->Q_u=2/3), so no quark "
                      "mass-Koide is in the I4-image; consequence (generic-given-the-split): I4 "
                      "amplitude-blind => 'quark-Koide = I4·lepton-Koide' REFUTED; #14 stiffness "
                      "ratio is a located gap (N12) OUTSIDE the Hodge map")
    return out


# TASK #14/N12-fork (gate-free, 2026-06-24, symmetry shortcut). Resolves the N12 tier-fork:
# is the Q/L "stiffness ratio" a Layer-1 D4 24-cell geometric constant, or a Layer-2 gap-gated
# quantity? -> Layer-2 (gap-gated); CAND 1 (pure-geometric 24-cell) FORECLOSED.
def q_l_stiffness_ratio_is_gap_gated() -> dict:
    """[DERIVED isometry facts + FRAMING fork-resolution] item #14 / N12: the lepton/quark
    'stiffness ratio' that #14 needs (the valid target v/f_pi ~ m_p/m_e) **LEANS Layer-2
    (gap-gated)** -- it is RELOCATED to the #1 gap, NOT foreclosed-by-geometry. Gemini CAND 1
    (the 24-cell triality projection ratio) is NOT computed here and stays an open re-attack
    handle; what this primitive does is RELOCATE the valid target, not kill CAND 1.
    [Post-review correction: an earlier draft over-claimed "CAND 1 FORECLOSED" -- the isometry
    argument (leg 1) does NOT reach CAND 1's actual object; see leg 1.]

    The two legs:
      (1) ISOMETRY-LINKAGE (exact, but does NOT foreclose CAND 1): I4· : grade-2 L-biv ->
          grade-2 Q-biv and e4· : grade-2 L-biv -> grade-3 trivector PRESERVE BLADE NORM (=1),
          so the cycle/count/charge-grade STRUCTURE transfers between sectors. ⚠ This kills only
          SAME-TYPE (blade-norm) asymmetries; it says NOTHING about a grade-distinguishing
          VOLUME / Casimir ratio between different-dimensional objects (CAND 1's actual object,
          e.g. grade-2 2-faces vs grade-3 octahedral cells of the self-dual 24-cell). Such
          ratios CAN be O(1)!=1 and are NOT killed by any isometry -- the engine's own
          C_A/C_F = 9/4 (colour_quartic_charge_handle) is exactly such a grade-distinguishing
          O(1) ratio. So the genuine sector asymmetry must come EITHER from amplitude data (the
          e4-DIP eps: lepton eps=0, quarks eps!=0 -- value GATED) OR from a 24-cell combinatorial
          ratio that has NOT been computed. Leg 1 does NOT decide CAND 1.
      (2) MASS-ONTOLOGY RELOCATION (the load-bearing leg): per the mass ontology (canon §5:
          quarks have no individual mass), the b_quark/b_lepton ratio (O(1), ~0.73-0.83) is
          quark-mass-DERIVED -> WITNESS-ONLY, NOT a valid physical target. The valid #14 target
          is the physical hierarchy m_p/m_e (=1836) ~ v/f_pi (~1909): a ratio of ABSOLUTE SCALES
          (EW VEV vs the chiral/hadron scale), which the framework already places at the #1 gap
          (f_pi = 'the one fitted mass scale'; absolute mass scales gap-gated). A ~1836 hierarchy
          runs through the soliton mass mechanism (the Q-orbit action, #7) + absolute scales =
          the #1 gap. So the VALID target LEANS Layer-2 / gap-gated.

    => the N12 fork LEANS Layer-2 (the valid target RELOCATED to the #1 gap, leg 2). CAND 1's
    Layer-1 route is NOT foreclosed-by-isometry and NOT computed. Its stated comparison target,
    the b_q/b_l ratio, is quark-mass-derived => WITNESS-ONLY (canon §5: quark masses INDICATE,
    only hadron masses VERIFY), so 'match the 24-cell ratio to the b-ratio' is a permissible
    INDICATOR-LEVEL cross-check but NOT a valid VERIFICATION (agreement can't graduate CAND 1 to
    DERIVED). The VERIFICATION-grade open handle is narrower: a 24-cell route is admissible only
    if it predicts a PHYSICAL observable (hadron/lepton); there it meets the ABSOLUTE-SCALE
    character of the valid target (v vs f_pi ~ m_p/m_e), which is gap-gated at the #1 gap. A
    pure-combinatorial 24-cell ratio is GENERICALLY O(1) and so LEANS toward undershooting a
    ~1836x hierarchy -- a LEAN, NOT a theorem (a determinant/exponential/power of a geometric
    quantity is not excluded). Surviving lean = CAND 2 (driven-NESS / absolute-scale dynamics).

    derived-vs-generic: the load-bearing conclusion is GENERIC-given-the-mass-ontology ('absolute
    scales are gap-gated', 'O(1) geometry can't make a 1000x hierarchy' -- true of any scale-
    separated theory) + the substrate-specific mass-ontology target choice. Leg 1's isometry facts
    are substrate-specific but do NOT bear on CAND 1 (the honest limit of the symmetry shortcut)."""
    out = {}
    # leg (1): the linking maps are norm-preserving isometries
    def _norm(mv): return math.sqrt(sum(c * c for _, c in mv.terms))
    iso_ok = all(abs(_norm(b) - 1.0) < 1e-12 and abs(_norm(I4 * b) - 1.0) < 1e-12
                 and abs(_norm(e(4) * b) - 1.0) < 1e-12 for b in L_BIVECTORS.values())
    assert iso_ok, "I4· and e4· must be norm-preserving (sectors isometry-linked)"
    out["sectors_isometry_linked"] = True
    # the sector asymmetry IS the e4-dip eps (lepton 0, quark !=0)
    qt = quark_brannen_table()
    eps_l, eps_d, eps_u = qt["lepton (b,ε,K)"][1], qt["down (b,ε,K)"][1], qt["up (b,ε,K)"][1]
    assert eps_l == 0.0 and eps_d != 0.0 and eps_u != 0.0, \
        "sector asymmetry must be the e4-dip eps (lepton 0, quarks nonzero)"
    out["sector_asymmetry_is_e4_dip"] = True
    # leg (2): the valid target is a LARGE absolute-scale hierarchy, not O(1)
    mp, me = 938.272, M_E
    v_ew, f_pi = 246220.0, 129.0
    mp_me, v_fpi = mp / me, v_ew / f_pi
    assert mp_me > 1000 and v_fpi > 1000, "the #14 target is a ~1000x hierarchy, not O(1)"
    assert abs(v_fpi / mp_me - 1.0) < 0.06, "the v/f_pi ~ m_p/m_e lead holds to <6% (the empirical coincidence)"
    out["m_p/m_e"], out["v/f_pi"] = round(mp_me, 1), round(v_fpi, 1)
    out["target_is_absolute_scale_hierarchy"] = True
    out["valid_target_leans"] = "Layer-2 (gap-gated): m_p/m_e ~ v/f_pi is an ABSOLUTE-SCALE hierarchy at the #1 gap"
    # NOTE: leg-1 isometry does NOT foreclose a grade-distinguishing volume/Casimir ratio --
    # the engine's own C_A/C_F=9/4 is exactly such an O(1)!=1 grade ratio, not killed by isometry.
    out["grade_distinguishing_O(1)_ratios_exist"] = {"C_A/C_F": 9/4}
    out["b_ratio_is_quark_mass_derived_witness_only"] = {"b_d/b_l": round(qt["down (b,ε,K)"][0]/math.sqrt(2), 3),
                                                         "b_u/b_l": round(qt["up (b,ε,K)"][0]/math.sqrt(2), 3)}
    out["CAND1_layer1_24cell"] = ("NOT foreclosed-by-isometry (cf. C_A/C_F=9/4) & NOT computed; vs the "
                                  "witness-only b-ratio it is an INDICATOR-LEVEL cross-check, NOT a "
                                  "verification; verification-grade handle = a 24-cell route to a PHYSICAL "
                                  "target (then meets the absolute-scale #1 gap; O(1) lean, not a theorem)")
    out["surviving_lean"] = "CAND2 = Layer-2 driven-NESS / absolute-scale dynamics (gap-gated)"
    # forward pointer: the 'NOT computed' clause above is now SUPERSEDED -- CAND 1 (as a projection/
    # Casimir ratio) WAS subsequently computed and CLOSED (all O(1), ~690x short of 1836).
    out["CAND1_now_computed"] = "SUPERSEDED -> cand1_24cell_ratio_computed(): CAND1-as-a-ratio CLOSED (O(1))"
    out["verdict"] = ("symmetry shortcut (honest limit): isometry-linkage transfers the cycle/count/"
                      "charge-grade structure but does NOT reach CAND 1's grade-distinguishing 24-cell "
                      "ratio (cf. engine C_A/C_F=9/4); the LOAD-BEARING leg is the mass-ontology "
                      "relocation -- the valid target m_p/m_e~v/f_pi is a ~1836x ABSOLUTE-SCALE hierarchy "
                      "at the #1 gap => #14 LEANS Layer-2 (RELOCATED, not foreclosed). CAND 1's 24-cell "
                      "ratio is NOT computed and stays an INDICATOR-level cross-check vs the witness-only "
                      "b-ratio; a verification-grade route must target a PHYSICAL observable (O(1) lean, not a theorem)")
    return out


# item #14 / N12 -- COMPUTE Gemini CAND 1 (the open gate-free handle that q_l_stiffness_ratio_is_gap_gated
# left "NOT computed"): the D4 Voronoi-cell (24-cell) projection/Casimir ratio. Turns the prior LEAN
# ("O(1) geometry can't make a 1000x hierarchy") into a COMPUTED result on the substrate polytope.
def cand1_24cell_ratio_computed() -> dict:
    """[DERIVED (the ratios are O(1)) + GENERIC-given-self-duality (the conclusion)] item #14 / N12:
    Gemini CAND 1 -- the Layer-1 D4 24-cell triality projection/Casimir ratio as the lepton/quark
    'stiffness ratio' source for v/f_pi ~ m_p/m_e ~ 1836 -- is now COMPUTED (it was the one open
    gate-free handle left explicitly NOT-computed by q_l_stiffness_ratio_is_gap_gated). RESULT: every
    natural scale-free ratio is O(1) (largest = 8/3 ~ 2.67), undershooting the ~1836x target by ~690x.
    => CAND 1, in the FORM it proposes (a projection-volume / quadratic-Casimir ratio -- its own
    'Claude substrate computation' steps 3-4), is CLOSED. The last gate-free Layer-1 handle on #14 is
    spent; #14's valid target sits ENTIRELY at the #1 gap (no surviving gate-free remnant).

    THE COMPUTATION (the SO(8)-triality / Hurwitz-unit form CAND 1 specifies): the D4 Voronoi cell is
    the regular 24-cell = the 24 unit Hurwitz quaternions = 8 vertices +-e_a (the 8_v 'vector' octad,
    norm 1) + 16 half-spinors (1/2)(+-e1+-e2+-e3+-e4) split by sign-parity into the 8_s and 8_c octads.
      * Each octad is a 16-cell (cross-polytope), and the 24-cell is SELF-DUAL with F4/D4 TRIALITY
        permuting the three octads => the three sectors are CONGRUENT. The lepton sector (grade-2
        anti-self-dual triple) and the quark sector (grade-3 colour trivectors) are triality-equivalent
        octads, so any multiplicity/volume ratio between them is PINNED to 1 -- the structural OPPOSITE
        of a 1836x hierarchy. (This is the decisive reason, independent of the exact identification:
        a ratio of two triality-equivalent sectors of ONE self-dual polytope cannot be large.)
      * The non-trivial natural ratios are small algebraic numbers (the engine's own C_A/C_F=9/4 class):
        - triality octad multiplicity / volume ratio           = 1
        - lepton/quark blade norm^2 ratio (ASD=2 vs trivec=1)  = 2
        - SU(2) adjoint(spin-1)/fundamental(spin-1/2) Casimir   = 8/3
        - (engine precedent grade ratio C_A/C_F, su(3))         = 9/4
      Largest = 8/3 ~ 2.67; m_p/m_e / 2.67 ~ 689x short. Even the largest combinatorial COUNTS of the
      24-cell (|W(F4)|=1152, V*E=2304) are O(10^3) but are COUNTS, not stiffness RATIOS, and none = 1836.

    SCOPE / honesty (preserves 'lean, not theorem'): this forecloses CAND 1 AS STATED -- a projection
    or Casimir RATIO. It does NOT foreclose an exotic non-combinatorial FUNCTIONAL (determinant /
    exponential / high power) of a 24-cell quantity; but CAND 1 proposes none and there is no
    motivation for one, so that remnant stays logically-open-but-unmotivated. derived-vs-generic: the
    individual ratios are substrate-specific DERIVED numbers; the load-bearing conclusion ('a self-dual
    triality-symmetric polytope yields O(1) sector ratios, not a 1000x hierarchy') is GENERIC-given-
    self-duality -- exactly the q_l_stiffness_ratio mass-ontology relocation, now backed by computed
    numbers rather than asserted.

    SIBLING CANDIDATES in the same #14 file, adjudicated (this closes the file):
      * CAND 3 (charge-winding strain E ~ Q^2 -> the quark Koide amplitudes b_d=1.17, b_u=1.03): its
        falsifiable handle TARGETS standalone quark Koide amplitudes, which canon §5 / N12
        (i4_lepton_quark_amplitude_blind) make WITNESS-ONLY (quark masses INDICATE, only hadrons
        VERIFY) -> INDICATOR-level at most, cannot graduate to DERIVED; AND its strain modulus
        E ~ integral (d phi)^2 IS the gap-gated elastic 'stiffness' (same object as CAND 2). Not a
        gate-free Layer-1 win -> folds into the #1 gap.
      * CAND 2 (NESS longitudinal/transverse viscosity ratio, runs with omega_d, D/J, tau_mem): an
        explicit Layer-2 driven-dissipative quantity = the gap-gated SURVIVOR, exactly where
        q_l_stiffness_ratio_is_gap_gated already places #14's lean.

    NET: #14's three candidate routes resolve -- CAND 1 (gate-free) COMPUTED & closed (O(1)); CAND 3
    indicator-only + gap-gated; CAND 2 the gap-gated survivor. #14 now sits entirely at the #1 gap."""
    out = {}
    # build the 24 unit-Hurwitz vertices, partitioned into the three triality octads
    oct_v = [tuple(s if k == a else 0 for k in range(4)) for a in range(4) for s in (1, -1)]
    half = [tuple(0.5 * s for s in sg) for sg in itertools.product((1, -1), repeat=4)]
    oct_s = [h for h in half if sum(x < 0 for x in h) % 2 == 0]
    oct_c = [h for h in half if sum(x < 0 for x in h) % 2 == 1]
    verts = oct_v + oct_s + oct_c
    assert len(verts) == 24 and len(oct_v) == len(oct_s) == len(oct_c) == 8, "the 24-cell = three 8-octads"
    assert all(abs(sum(x * x for x in v) - 1.0) < 1e-12 for v in verts), "all 24 vertices are unit (Hurwitz)"
    out["vertices"], out["octads_8v/8s/8c"] = 24, (8, 8, 8)
    # the lepton (anti-self-dual bivector) and quark (colour trivector) sector blade norms^2
    def _n2(mv): return sum(c * c for _, c in mv.terms)
    ASD = [e(1, 2) + e(3, 4), e(1, 3) - e(2, 4), e(1, 4) + e(2, 3)]
    COL = [QUARK_BLADES["e124"], QUARK_BLADES["e134"], QUARK_BLADES["e234"]]
    assert all(abs(_n2(b) - 2.0) < 1e-12 for b in ASD), "ASD lepton triple norm^2 = 2"
    assert all(abs(_n2(t) - 1.0) < 1e-12 for t in COL), "colour trivector norm^2 = 1"
    # the panel of natural scale-free ratios
    ratios = {
        "triality_octad_mult": 8 / 8,
        "triality_octad_volume": 1.0,                          # congruent 16-cells (self-dual triality)
        "blade_norm2_lep/quark": _n2(ASD[0]) / _n2(COL[0]),    # 2
        "Casimir_su2_adj/fund": (1 * 2) / (0.5 * 1.5),         # 8/3
        "engine_C_A/C_F_su3": 3 / (4 / 3),                     # 9/4 (the grade-ratio precedent)
    }
    out["natural_ratios"] = {k: round(v, 4) for k, v in ratios.items()}
    out["largest_natural_ratio"] = round(max(ratios.values()), 4)   # 8/3
    mp_me = 938.272 / M_E
    out["target_m_p/m_e"] = round(mp_me, 1)
    out["undershoot_factor"] = round(mp_me / max(ratios.values()), 0)   # ~689x
    assert max(ratios.values()) < 3.0, "every natural 24-cell ratio is O(1) (largest = 8/3)"
    assert mp_me / max(ratios.values()) > 100, "O(1) ratios undershoot the ~1836x hierarchy by >100x"
    out["CAND1_status"] = ("CLOSED as a projection/Casimir RATIO: O(1) (largest 8/3), ~690x short of "
                           "m_p/m_e; self-dual triality pins the lepton/quark sector ratio near 1. "
                           "Exotic non-combinatorial functional logically-open-but-unmotivated.")
    out["CAND3_status"] = ("INDICATOR-only (targets witness-only quark Koide amplitudes, canon §5/N12) "
                           "+ strain modulus is gap-gated -> not a gate-free Layer-1 win")
    out["CAND2_status"] = "Layer-2 NESS viscosity ratio = the gap-gated survivor (where #14 already sits)"
    out["verdict"] = ("Gemini CAND 1 COMPUTED: the D4 24-cell projection/Casimir ratios are all O(1) "
                      "(largest 8/3 ~ 2.67, ~690x short of m_p/m_e ~ 1836); the self-dual triality makes "
                      "the lepton/quark sectors congruent octads so the ratio is pinned near 1. The last "
                      "gate-free Layer-1 handle on #14 is CLOSED (CAND 1 as a ratio); CAND 3 is "
                      "indicator-only + gap-gated, CAND 2 is the Layer-2 survivor => #14 sits ENTIRELY at "
                      "the #1 gap with no surviving gate-free remnant. (lean -> computed; an exotic "
                      "functional stays unmotivated-open, so not a theorem.)")
    return out


def _orbit_vectors(b, eps, psi, delta):
    """The 3 V4perp orbit-phase vectors = 1st harmonic + eps*(2nd harmonic), the 2nd
    harmonic ORIENTED by psi (the §19.7 phase that worklist F3 does NOT expose)."""
    V = []
    for n in range(3):
        phi = delta + 2*math.pi*n/3
        x = math.cos(phi)+eps*math.cos(2*phi-psi)
        y = math.sin(phi)+eps*math.sin(2*phi-psi)
        nrm = math.hypot(x, y)
        V.append((x/nrm, y/nrm))
    return V


def ckm_from_triplet_overlap():
    """[LOCATED-GAP, outcome ii-a] §19.7 (proposed): CKM from <up-triplet|down-triplet>.

    SCOPE (defused 2026-06-30 per audit C1): applies to the QUARK u/d weak doublet (both Brannen
    triplets share the Hodge-dual V4perp/Q-orbit per i4_generation_overdetermination — same chiral
    module S+⊕S−). The analogous V_PMNS construction (ν-vs-charged-ℓ) is NON-APPLICABLE: the
    shared-basis identification across S+ (neutrino_lightness) and S+⊕S− (charged-ℓ) modules is
    NOT substrate-supplied. See pmns_no_substrate_derivation().

    The two §19.7 Brannen triplets share a common space (the Hodge-dual V4perp/Q-orbit,
    per i4_generation_overdetermination) so the overlap <up_i|down_j> is WELL-DEFINED (not
    a FAIL). But the CKM hierarchy does NOT fall out of the EXPOSED data (b, eps, delta_L);
    it is blocked on worklist F3 (the unexposed phases psi_u,psi_d and scale Lambda).
    [NOTE 2026-08-13, ADJUDICATION2 keeper C1: 'unexposed' is now STRONGER -- per-sector psi
    is not mass-observable even in principle (N=3 harmonic collapse; MAIN
    brannen_z3_harmonic_collapse_invariant): the masses expose only the invariant phases
    psi_inv per sector. Any F3 psi-prescription must therefore be pinned by structure BEYOND
    the masses (eigenvector data), consistent with this function's own conclusion.]

      E1 (rigorous): a Z3-SYMMETRIC (circulant) orbit -> CKM is a PERMUTATION matrix
         (no genuine mixing) at ANY phase, regardless of b, eps, psi — identity when the
         up/down spectra sort-align, a non-identity generation RELABELING otherwise
         (verified: 100% permutation, ~20% identity over random phases). All circulant
         matrices share the DFT eigenbasis, so up/down circulant mass operators commute.
         => the 2nd-harmonic eps in the EIGENVALUES generates NO mixing; the hierarchy
         needs explicit Z3-BREAKING in the eigenVECTORS (a SHARPENING of the brief's crux:
         eps in the mass amplitudes is necessary but NOT sufficient).
      E2 (demonstrated): once Z3 is broken by the eps-distortion, the overlap's specificity
         (which off-diagonal leads) and ladder are a FREE FUNCTION of the unexposed
         psi_u,psi_d. Over random phases the leading off-diagonal is V_12:V_23:V_13 ~
         48:23:29 % (a plurality hint, NOT forced); lambda-ladder shapes occur in ~0% of
         phase space; magnitudes are O(0.1-1), NOT the lambda-suppressed 0.22/0.04/0.004
         (that suppression is mass-ratio sqrt(m_i/m_j) physics, needing the scale Lambda --
         also F3). The literal phase-overlap matrix is rank 2, not a rank-3 unitary.
      PROBE (the decisive negative): no NATURAL psi-tied-to-delta_L identification closes
         the gap. Across every sensible identification of psi_u,psi_d with ±delta_L or 0,
         NONE reproduces the lambda-ladder — the best V_12-leading case is still ~4x/12x/130x
         too large in V_12/V_23/V_13, and specificity is ~half CKM-correct, half wrong. So
         the simple psi=delta_L ("Cabibbo = lepton phase") shortcut is DEAD; the F3
         ψ-prescription must be NON-TRIVIAL. (This is why the fake-positive is avoided by
         structural necessity, not by avoiding a working choice — no natural choice works.)

    What DOES emerge (partial, honest): the LEADING off-diagonal can be the Cabibbo angle
    theta_C = delta_L (TASK-3 consistent) as a single relative rotation; plus the E1
    dichotomy. Neither supplies the specificity or the ladder.

    Located missing construction (deliverable form):
      CKM hierarchy needs the TWT object to have property P = { an explicit Z3-BREAKING
      3x3 generation operator on V4perp for EACH of up/down -- the Brannen amplitudes
      promoted to ORIENTED eigenVECTORS (not just eigenvalues) via the §19.7 triplet phases
      psi_u,psi_d and scale Lambda -- so the up/down mass bases are genuinely MISALIGNED
      (non-circulant) }, sourced from [bedrock: the V4perp generation plane + the Brannen
      Z3 orbit-phase structure, with the §19.7 ψ/Λ prescription currently UNEXPOSED
      (worklist F3)]. The overlap captures the leading Cabibbo angle (a single delta_L
      rotation); the specificity (why s) and |V_us|>>|V_cb|>>|V_ub| ladder need the F3
      orientation psi (selects the leading off-diagonal) and scale Lambda (sets the
      lambda-suppression via mass ratios).

    => F3 is pinned as CKM's PREREQUISITE, with three precise dependencies: (1) ψ_u,ψ_d
       (specificity), (2) Λ / absolute masses (lambda-magnitude), (3) the amplitude->operator
       rule (eigenvectors, not eigenvalues). NOT a falsifier (output is psi-free, no definite
       prediction), NOT a solve. A located gap, sharp enough to build."""
    import numpy as np
    tab = quark_brannen_table()
    (b_d, eps_d, _) = tab["down (b,ε,K)"]; (b_u, eps_u, _) = tab["up (b,ε,K)"]
    dL = delta_L_from_DoverJ(DoverJ_from_lepton_masses())
    out = {"inputs": {"b_d": b_d, "eps_d": eps_d, "b_u": b_u, "eps_u": eps_u,
                      "delta_L_deg": round(math.degrees(dL), 2)}}

    # --- E1: circulant -> PERMUTATION matrix (no genuine mixing) at any phase ---
    w = np.exp(2j*np.pi/3)
    DFT = np.array([[w**(j*k) for j in range(3)] for k in range(3)])/np.sqrt(3)
    def circ(b, eps, psi):
        sm = np.array([1+b*math.cos(2*math.pi*n/3-psi)+eps*b*math.cos(2*(2*math.pi*n/3)-psi)
                       for n in range(3)])
        return DFT @ np.diag(sm) @ DFT.conj().T
    def _is_perm(P, tol=1e-7):
        return (bool(np.all((np.abs(P) < tol) | (np.abs(P-1) < tol)))
                and bool(np.all(np.abs(P.sum(0)-1) < tol)) and bool(np.all(np.abs(P.sum(1)-1) < tol)))
    _, Vu = np.linalg.eigh(circ(b_u, eps_u, 0.3)); _, Vd = np.linalg.eigh(circ(b_d, eps_d, dL))
    P0 = np.abs(Vu.conj().T @ Vd)
    out["E1_aligned_max_offdiag"] = float(np.max(P0 - np.diag(np.diag(P0))))   # ~0 (identity at aligned phase)
    rngp = np.random.default_rng(11); all_perm = True; any_nonid = False
    for _ in range(300):
        pu, pd = rngp.uniform(0, 2*math.pi, 2)
        _, Vu = np.linalg.eigh(circ(b_u, eps_u, pu)); _, Vd = np.linalg.eigh(circ(b_d, eps_d, pd))
        Pp = np.abs(Vu.conj().T @ Vd)
        all_perm &= _is_perm(Pp); any_nonid |= (np.max(Pp - np.diag(np.diag(Pp))) > 1e-7)
    assert all_perm, "circulant orbits MUST give a permutation matrix (no genuine mixing) at any phase"
    out["E1_always_permutation"] = bool(all_perm)        # True; identity only a subset
    out["E1_some_nonidentity"] = bool(any_nonid)         # True (permutation, not always identity)

    # --- E2: psi-dependence of the broken overlap ---
    def offdiags(pu, pd, du, dd):
        Vu = _orbit_vectors(b_u, eps_u, pu, du); Vd = _orbit_vectors(b_d, eps_d, pd, dd)
        O = np.array([[abs(np.dot(Vu[i], Vd[j])) for j in range(3)] for i in range(3)])
        return O[0,1], O[1,2], O[0,2], O
    rng = np.random.default_rng(7); lead = {"12":0,"23":0,"13":0}; N = 4000
    for _ in range(N):
        du, dd, pu, pd = rng.uniform(0, 2*math.pi, 4)
        o12, o23, o13, _ = offdiags(pu, pd, du, dd)
        lead[max([("12",o12),("23",o23),("13",o13)], key=lambda t:t[1])[0]] += 1
    fr = {k: v/N for k, v in lead.items()}
    out["E2_leading_offdiag_fractions"] = {k: round(v, 3) for k, v in fr.items()}
    assert max(fr.values()) < 0.7, "specificity must NOT be forced (else it would be ~1.0)"
    *_ , O = offdiags(0.3, dL, 0.0, dL)
    out["E2_overlap_rank"] = int(np.linalg.matrix_rank(O, tol=1e-9))
    assert out["E2_overlap_rank"] < 3, "phase overlap is rank-deficient (not a unitary CKM)"

    # --- PROBE: no natural psi-tied-to-delta_L identification gives the lambda-ladder ---
    ladder_hit = False; max_o12 = 0.0; v12_leads = 0; total = 0
    for pu_id in (0.0, dL, -dL):
        for pd_id in (0.0, dL, -dL):
            for (du_id, dd_id) in ((dL, dL), (0.0, dL)):
                total += 1
                o12, o23, o13, _ = offdiags(pu_id, pd_id, du_id, dd_id)
                max_o12 = max(max_o12, o12)
                if o12 >= o23 and o12 >= o13:
                    v12_leads += 1
                if (o12 > o23 > o13 and o12 < 0.4
                        and o23/max(o12, 1e-9) < 0.4 and o13/max(o23, 1e-9) < 0.4):
                    ladder_hit = True
    assert not ladder_hit, "no natural psi=±delta_L/0 identification gives the lambda-ladder (the simple route is dead)"
    out["probe_natural_psi_gives_ladder"] = ladder_hit            # False
    out["probe_max_V12_over_natural"] = round(max_o12, 3)         # ~0.9 (≈4x too large vs |V_us|≈0.225)
    out["probe_V12_leads_fraction"] = round(v12_leads/total, 2)   # ~0.5 (specificity not robust)

    out["emerges_partial"] = "leading off-diagonal = Cabibbo theta_C = delta_L (TASK-3 consistent); E1 dichotomy"
    out["needs_property_P"] = ("explicit Z3-BREAKING 3x3 generation operator on V4perp per sector "
                               "(Brannen amplitudes -> oriented eigenVECTORS) via §19.7 psi_u,psi_d & Lambda")
    out["F3_dependencies"] = ["orientation psi_u,psi_d (specificity)", "scale Lambda (lambda-suppression)",
                              "amplitude->operator rule (eigenvectors, not just eigenvalues)"]
    out["verdict"] = "ii-a located gap; F3 is CKM's prerequisite (NOT a falsifier, NOT a solve)"
    return out


def epicycle_reading_dependent():
    """[TASK-e4 PART A, RECONCILED central finding] §17.4: The obstruction is READING-DEPENDENT. The §0
    ellipse construction is NOT 'cycle a bivector by G and take |B_spatial|'; it is 'project a
    tilted, offset circular ORBIT onto the spatial plane and sample at the three generation
    angles.' Projecting a unit circle tilted by tau (a dip toward e4) with spatial offset d gives
        r^2(phi) = C + 2 d cos(phi) + (sin^2(tau)/2) cos(2 phi),
    so offset -> 1st harmonic (DEFERENT b), tilt -> 2nd harmonic (EPICYCLE eps). Under the
    RADIUS-SQUARED measure the lepton boundary is EXACT (tau=0 -> 2nd harmonic = 0 -> eps=0);
    under the RADIUS measure a sqrt cross-term gives a SPURIOUS nonzero lepton 2nd harmonic (the
    only case the build's 'fails to vanish for leptons' dismissal actually describes).
    => the epicycle IS reproducible (geometry half) under the radius^2 orbit-projection, and is
    forbidden only under the |B_spatial|-of-cycled-bivector reading. The central claim is
    UNRESOLVED: it turns on the under-specified bedrock mass-measure and on connecting the
    orbit-projection (gives the FORMULA) to the G/Z3 action (gives 'why three'). NOT a clean
    outcome-(iii); a re-located gap, sharper than 'G preserves the Hodge split'."""
    np = __import__("numpy")
    phis = np.linspace(0, 2*math.pi, 4000, endpoint=False)
    def h(f): return 2*np.mean(f*np.cos(phis)), 2*np.mean(f*np.cos(2*phis))
    def proj_r2(d, tau):
        x = np.cos(phis) + d; y = np.sin(phis)*math.cos(tau)   # spatial projection drops the e4 component
        return x*x + y*y
    out = {}
    for tag, (d, tau) in {"quark_offset_tilt": (0.3, 0.5), "lepton_offset_no_tilt": (0.3, 0.0)}.items():
        r2 = proj_r2(d, tau); r = np.sqrt(r2)
        a1_2, a2_2 = h(r2); a1_r, a2_r = h(r)
        out[tag] = {"r2_1st": round(float(a1_2), 4), "r2_2nd": round(float(a2_2), 4),
                    "r_1st": round(float(a1_r), 4), "r_2nd": round(float(a2_r), 4)}
    assert abs(out["lepton_offset_no_tilt"]["r2_2nd"]) < 1e-6, "radius^2: untilted lepton MUST have zero epicycle"
    assert abs(out["quark_offset_tilt"]["r2_2nd"]) > 0.05, "radius^2: tilt MUST produce a nonzero epicycle"
    assert abs(out["lepton_offset_no_tilt"]["r_2nd"]) > 1e-3, "radius: untilted lepton has a SPURIOUS epicycle (cross-term)"
    return {"harmonics": out, "epicycle_reachable_under_radius_squared_orbit_projection": True,
            "epicycle_forbidden_under_|B_spatial|_of_cycled_bivector": True,
            "build_dismissal_holds_only_for": "the radius measure (NOT radius^2)",
            "open_step": "pin the bedrock mass-measure; reconcile orbit-projection (formula) with |B_spatial| "
                         "(no hierarchy); connect orbit-projection to the G/Z3 generation action",
            "verdict": "RESOLVED by epicycle_reading_resolved (e4 Part A): the reading-dependence is settled — "
                       "mass-measure √m=r² forced, generation ℤ₃ = meta-time phase (spatial G = colour); prior (iii) was a fake-negative"}


def deferent_from_offset_lepton_consistent():
    """[TASK-e4 PART A, the half that survives BOTH readings] §17.4: The DEFERENT b·cos(phi-psi) is a
    clean 1st harmonic with zero 2nd harmonic. SCOPE: this verifies the TRIG IDENTITY / lepton
    boundary (no 2nd harmonic at no e4-dip), NOT the full geometric claim that a linear
    e4-orthogonal projection of a phasor yields rest mass (asserted in text). The offset->b map +
    lepton eps=0 hold; the epicycle is the reading-dependent piece (epicycle_reading_dependent)."""
    np = __import__("numpy")
    b, psi = 1.7, 0.3
    phis = np.linspace(0, 2*math.pi, 2000, endpoint=False)
    sqrt_m = 1 + b*np.cos(phis - psi)
    a1 = 2*np.mean(sqrt_m*np.cos(phis - psi)); a2 = 2*np.mean(sqrt_m*np.cos(2*(phis - psi)))
    assert abs(a1 - b) < 1e-6, "deferent 1st-harmonic coefficient must equal b"
    assert abs(a2) < 1e-6, "linear projection of the deferent phasor has ZERO 2nd harmonic"
    return {"deferent_coeff": round(float(a1), 4), "epicycle_coeff_at_no_dip": round(float(a2), 8),
            "lepton_epsilon_zero": True, "check_scope": "trig identity / lepton boundary, not full projection geometry"}


def bu_offset_not_charge_sourced():
    """[TASK-e4 PART D, located gap] §17.4: s (down, n=2, q=-1/3) and c (up, n=2, q=+2/3) sit at
    phi2=4pi/3 = the EPICYCLE NODE (cos2(phi2-psi)~-0.08 at psi=2/9), so eps is nearly invisible
    for both -> the s/c gap is driven by the DEFERENT offset b. b_d=pi clean; optimum b_u~4.333.
    [CONVENTION 2026-08-13, keeper C2: this function computes the node in the 2PSI-FORM
    (cos(2*(phi2 - psi))); psi = 2/9 is a PRESCRIPTION PIN (a convention choice), not 'the quark
    phase = delta_L' -- psi is not fixed by the mass spectrum (MAIN
    brannen_z3_harmonic_collapse_invariant). The node VALUE is convention-dependent: -0.079 in
    the 2psi-form vs -0.297 in the table's psi-form cos(2*phi2 - psi). The located-gap
    conclusion (b and eps independent handles; b_u not charge-sourced) is unchanged.]
    Tested CKM-/charge-blind: charge guess pi*sqrt2~4.443 FAILS; T3 gives no such ratio; gen-count
    gives 4.712 or 3.848 -- none hits 4.333. So eps (charge tilt) and b (offset) are TWO
    INDEPENDENT handles; b_u is NOT charge-determined. FUTURE-SEARCH FLAG: 13/3=4.33333 hits b_u to
    0.008% (pi*11/8=4.320 at 0.31%) but NEITHER has a bedrock source. NOT DELIVERED (owed): the
    n=1/n=3 up/down splitting cross-checks + the phi-vs-J/psi deficit (downstream of Part A)."""
    psi = 2/9
    node = math.cos(2*(4*math.pi/3 - psi))
    b_d, b_u_opt = math.pi, 4.333
    preds = {"charge_pi*sqrt2": math.pi*math.sqrt(2), "gen_3over2": b_d*1.5, "gen_sqrt_3over2": b_d*math.sqrt(1.5)}
    near = {"13/3": 13/3, "pi*11/8": math.pi*11/8}
    assert abs(node) < 0.12, "n=2 must be the epicycle node (cos2 ~ -0.08)"
    assert all(abs(v - b_u_opt)/b_u_opt > 0.02 for v in preds.values()), \
        "no charge/T3/gen-count prediction may reproduce b_u within 2% (it is a separate handle)"
    assert abs(near["13/3"] - b_u_opt)/b_u_opt < 0.001, "13/3 is a near-exact (bedrock-unmotivated) hit on b_u_opt"
    return {"epicycle_node_at_n2": round(node, 3), "b_d_clean": round(b_d, 4), "b_u_optimum": b_u_opt,
            "failed_predictions": {k: round(v, 3) for k, v in preds.items()},
            "unmotivated_near_hits": {k: round(v, 4) for k, v in near.items()},
            "not_delivered": "n=1/n=3 splitting cross-checks + phi-vs-Jpsi deficit (downstream of Part A)",
            "verdict": "located gap: b_u offset NOT sourced by charge/T3/gen-count; b and eps independent"}


def epicycle_reading_resolved():
    """[e4 PART A — RESOLUTION of epicycle_reading_dependent] §17.4: Status UNRESOLVED -> RESOLVED.
    The |B_spatial| reading (FACT 1) and the orbit-projection reading (FACT 2) are NOT both the
    mass-measure. Adjudicated from 'mass = ω': the measure is √m = r² (1A, forced by the lepton
    boundary); the generation ℤ₃ is the meta-time phase, NOT spatial G (1B — spatial G is
    mass-blind = colour). Under THAT pairing the modified-Brannen form is reproduced EXACTLY with
    ε=0 at no tilt. The prior (iii) ('e4-projection cannot make the epicycle') was a FAKE-NEGATIVE:
    it applied the COLOUR ℤ₃ (spatial G) to the generation index. Remaining gap: 'why exactly
    three' (1C), now sharply located."""
    mass_measure_from_omega(); generation_z3_is_metatime_phase(); why_three_generation_triple()
    return {
        "prior_status": "UNRESOLVED (reading-dependent)", "resolved_status": "RESOLVED",
        "mass_measure": "sqrt(m) = r^2 (squared spatial amplitude); m=r^2 ruled out by lepton boundary",
        "generation_Z3": "meta-time phase advance; spatial G_generator = COLOUR (mass-blind)",
        "prior_iii_was": "a FAKE-NEGATIVE (it used the colour ℤ₃ for the generation index)",
        "reproduces_modified_brannen": True,
        "remaining_gap": "why exactly three (1C) — located: a map orbit-phase->ℍ-unit (property Q) is owed",
        "downstream_reinterpretation": "spatial G / R_G was used as the GENERATION operator in Cl-i and F3; it "
            "is mass-blind = the COLOUR ℤ₃. Those tasks' MATH stands, but their INTERPRETATION of R_G is under "
            "revision (a CONCEPTUAL re-identification, not a parameter remap) — a separate worklist item.",
        "outcome": "(ii) measure + ℤ₃ fixed; hierarchy + exact lepton boundary reproduced; why-three is the located step",
    }


# item 8b, step 2 (2026-06-24, Yaer's hint). SAME quark composition, DIFFERENT mass = the cleanest
# pointer to the mechanism: the additive floor cancels in the difference, so dM is a direct readout
# of the NON-ADDITIVE internal-mode term. Reconciles the coherent-sum and §17.3 gear pictures.
def same_composition_baryons_pin_internal_mode() -> dict:
    """[DERIVED falsifier + FRAMING reconciliation] item 8b step 2: baryons with the SAME quark
    composition but DIFFERENT mass are the cleanest evidence for the non-additive system-level
    functional, and the bridge that reconciles the coherent-sum picture with the §17.3 gear lock.

    DATA (HADRON masses = the legitimate verifiers, canon §C; quark masses NOT used):
      uds:  Lambda 1115.68  vs  Sigma0 1192.64  -> dM = +76.96   (BOTH J=1/2: differ ONLY by the
            ud-pair symmetry, I=0 antisymmetric vs I=1 symmetric -- the cleanest, J held fixed too)
      uud:  p      938.27   vs  Delta+ 1232.0   -> dM = +293.73  (differ by total spin J)
      uus:  Sigma+ 1189.37  vs  Sigma*+ 1382.8  -> dM = +193.43  (J)
      uss:  Xi0    1314.86  vs  Xi*0   1531.8   -> dM = +216.94  (J)

    THE FALSIFIER (DERIVED, logic + hadron data): an ADDITIVE composition-only functional
    M = sum_i A_i (+ composition-only corrections) assigns ONE mass per composition, so it predicts
    dM = 0 for EVERY same-composition pair. All four pairs have dM >> 0. ⇒ ADDITIVITY IS FALSIFIED;
    the mass MUST depend on the INTERNAL CONFIGURATION (the shared-rotor relative-phase / symmetry
    mode), not on which quarks are present. This is the cleanest empirical case FOR the non-additive
    system-level ontology (item 8b) -- and it ISOLATES the non-additive term: in the difference the
    additive floor (same composition) CANCELS, so dM is a direct, absolute-scale-free readout of the
    internal-mode (non-additive) contribution alone.

    THE RECONCILIATION (coherent-sum <-> §17.3 gear, on the Lambda/Sigma case where J is also fixed):
      * §17.3 gear_eigenvalues ALREADY derives this split as the internal-MODE eigenvalue:
        Lambda-type = antisymmetric light pair, mode (1,-1), Theta_A = I_pair         (K_L=0);
        Sigma-type  = symmetric  light pair, mode (1, 1), Theta_B = I_pair(1+2 x_Q)   (K_L=1).
        Same composition (uds), DIFFERENT internal mode -> different eigenvalue -> different mass.
      * In the coherent-sum picture (baryon_mass_shared_rotor_nonadditive) the SAME internal mode is
        the light pair's RELATIVE META-TIME PHASE (antisymmetric = pi, symmetric = 0) -> its cross-
        term flips sign with the mode. So the §17.3 gear-INERTIA eigenvalue and the coherent-sum
        INTERFERENCE cross-term are TWO VIEWS of the ONE internal mode. They reconcile ON the
        discriminator: both make the mass a function of the internal mode, and same-composition
        splits are exactly where that dependence is isolated (composition fixed, only the mode varies).

    SCOPE (what the falsifier does and does NOT show): it rules out mass = f(composition) ALONE, so
    the internal MODE is load-bearing -- DERIVED. It does NOT by itself select the TWT shared-rotor
    picture over a 'constituent sum + internal-mode-dependent corrections' model (e.g. v13's SU(6) pair
    term sigma already depends on the internal state, so v13 is itself NOT composition-only). Both
    encode internal-mode dependence; the same-composition splits prove that dependence is real and
    isolate it, but the claim that the mode IS the shared-rotor relative-phase/§17.3-gear structure
    (primary, not a perturbative correction) is the FRAMING part below.

    TIER: the FALSIFIER (composition-only ruled out, mass depends on the internal mode) is DERIVED. The
    coherent-sum<->gear identification is FRAMING (both encode the mode; the EXACT map -- including
    the sign/ordering Lambda<Sigma and the J-sector, and which functional is fundamental -- is the
    open reconciliation work). GAP-GATED: the absolute dM VALUES (need I_pair, x_Q / the omega scale
    + the Theta_rel phases). derived-vs-generic: substrate-specific = the §17.3 mode eigenvalues +
    the colour/meta-time split; generic = 'same input, different output rules out a function of the
    input alone'. NO fit (hadron masses used only as the verifier-level witnesses of dM != 0)."""
    out = {}
    pairs = {
        "uds_Lambda_vs_Sigma0_sameJ": (1115.68, 1192.64, "1/2 both; ud-pair symmetry mode (cleanest)"),
        "uud_p_vs_Delta":             (938.27, 1232.0, "spin J 1/2 vs 3/2"),
        "uus_Sigma_vs_Sigmastar":     (1189.37, 1382.80, "spin J"),
        "uss_Xi_vs_Xistar":           (1314.86, 1531.80, "spin J"),
    }
    out["splits_MeV"] = {k: round(m2 - m1, 2) for k, (m1, m2, _note) in pairs.items()}
    out["notes"] = {k: note for k, (_a, _b, note) in pairs.items()}
    # FALSIFIER: additive composition-only predicts dM=0; all observed dM are large
    assert all(m2 - m1 > 50.0 for (m1, m2, _n) in pairs.values()), \
        "every same-composition pair must split (additive composition-only mass is FALSIFIED)"
    out["additive_composition_only_predicts_dM"] = 0.0
    out["composition_only_additivity_falsified"] = True   # NB: composition-ONLY; an additive sum WITH
    #   internal-mode terms (e.g. v13's K_L term) still splits these pairs -- see SCOPE in the docstring
    # the difference cancels the additive floor -> dM is the pure non-additive internal-mode term
    out["dM_isolates_nonadditive_internal_mode"] = True
    # the §17.3 gear already realizes the Lambda/Sigma (same-J) internal-mode split
    ge = gear_eigenvalues()
    assert ge["Θ_A = I_pair (Λ-type)"] and ge["Θ_B = I_pair(1+2x_Q) (Σ-type)"], \
        "§17.3 gear eigenvalues must give the Lambda(antisym)/Sigma(sym) internal-mode split"
    out["gear_lambda_sigma_modes"] = "Theta_A=I_pair (Lambda, antisym (1,-1), K_L=0) != Theta_B=I_pair(1+2x_Q) (Sigma, sym (1,1), K_L=1)"
    out["coherent_sum_view_of_same_mode"] = "light-pair RELATIVE PHASE (antisym=pi, sym=0); cross-term flips sign with the mode"
    out["reconciliation"] = "gear-inertia eigenvalue and coherent-sum interference are TWO VIEWS of the ONE internal mode (FRAMING; exact map = open)"
    out["gap_gated"] = "absolute dM values (I_pair, x_Q / omega scale + Theta_rel phases) at the #1 gap"
    out["verdict"] = ("same-composition/different-mass baryons (Lambda!=Sigma0 same J, p!=Delta, etc.) "
                      "FALSIFY additive composition-only mass (DERIVED) and ISOLATE the non-additive "
                      "internal-mode term (additive floor cancels in dM); §17.3 gear eigenvalues realize "
                      "the Lambda/Sigma mode split, the coherent-sum is its amplitude-view -> the two "
                      "pictures reconcile on the ONE internal mode; absolute dM values gap-gated")
    return out


# item 8b, step 8 (2026-06-24, Yaer: "what ARE the SU(6) pairs? geometric/dynamic meaning?").
# The hyperfine pair coefficients sigma_ij are NOT just practical bookkeeping -- they are the discrete
# RELATIVE ROTOR ORIENTATIONS of the quark pairs = the step-3 constructive/destructive interference signs.
def su6_pairs_are_rotor_orientation() -> dict:
    """[DERIVED geometric meaning + FRAMING (per-baryon assignment = standard-QM TWT reconstructs)] §19.7:
    item 8b: the SU(6) hyperfine pair coefficients sigma_ij (the mass fit's internal-mode term) are
    the discrete RELATIVE ROTOR ORIENTATIONS of the quark pairs -- the constructive/destructive
    interference signs of the step-3 coherent sum -- NOT imported black-box bookkeeping.

    In TWT spin = the Spin(4) rotor orientation (the even subalgebra; half-angle, fermionic). A quark
    PAIR's spin-spin S_i.S_j IS the relative orientation of their two rotors:
      * TRIPLET (S=1, rotors ALIGNED / same sense):     S_i.S_j = +1/4 -> CONSTRUCTIVE cross-term (+)
      * SINGLET (S=0, rotors ANTI-aligned / opposite):  S_i.S_j = -3/4 -> DESTRUCTIVE (Goldstone-like, -)
    These ARE the step-3 signs (interference_can_reduce_mass_goldstone): aligned rotors add (mass up),
    anti-aligned subtract (mass down). The fit's integer sigma_ij = 4*<S_i.S_j> (decuplet all-aligned = +1).

    Two consequences tie the whole item-8b picture into ONE object (the pair's rotor sense):
      (1) TRACE-ZERO over the spin multiplet: 3*(+1/4) + 1*(-3/4) = 0 -> the cross-terms average to zero,
          so the interference-free FLOOR is the spin-averaged CENTROID (= step 4, the floor).
      (2) Lambda<Sigma (same uds): the ud pair flips SINGLET(anti-aligned,-3) -> TRIPLET(aligned,+1) --
          the step-5 K_L=0/1 gear mode IS the pair's rotor reorientation. So same-composition split (step2),
          the gear K_L mode (step5), and the destructive Goldstone channel (step3) are ONE thing: pair rotor sense.

    DERIVED (TWT-geometric INTERPRETATION, not the numbers): spin = Spin(4) rotor; S_i.S_j = relative rotor
    orientation; trace-zero = centroid; aligned/anti = constructive/destructive (step 3). So sigma_ij is the
    rotor-interference coefficient -- a geometric meaning, not a black box. (The numeric +1/4 / -3/4 themselves
    are GENERIC spin-1/2 Casimir algebra -- see the derived-vs-generic note; what is TWT is their rotor READING.)
    FRAMING / standard-QM (NOT novel to TWT): WHICH pair is singlet vs triplet in a given baryon (the SU(6)
    56-plet wavefunction) follows from colour-ANTISYMMETRY (TWT: the 3 distinct colour trivectors) + Fermi
    statistics (TWT: the Spin(4) half-angle). TWT HAS these ingredients and reconstructs the assignment, but
    the Young-tableaux machinery itself is shared with the standard quark model -- imported as group theory.
    derived-vs-generic: the numerical +1/4,-3/4 are GENERIC spin-1/2 algebra; the INTERPRETATION (rotor
    orientation / coherent-sum interference) is the TWT-specific content."""
    out = {}
    def SiSj(Spair): return 0.5 * (Spair * (Spair + 1) - 2 * 0.75)   # two spin-1/2 quarks
    trip, sing = SiSj(1), SiSj(0)
    assert abs(trip - 0.25) < 1e-12 and abs(sing + 0.75) < 1e-12, "spin-1/2 pair: triplet +1/4, singlet -3/4"
    out["triplet_aligned_constructive"] = trip          # +1/4
    out["singlet_antialigned_destructive"] = sing       # -3/4
    out["trace_over_multiplet"] = round(3 * trip + 1 * sing, 12)   # 0 -> centroid floor (step 4)
    assert abs(3 * trip + 1 * sing) < 1e-12, "spin cross-terms must trace to zero (floor = centroid, step 4)"
    out["sigma_ij_eq_4_SS"] = {"triplet": 4 * trip, "singlet": 4 * sing}   # +1, -3 (the fit's integers)
    out["lambda_ud"] = "ud SINGLET (anti-aligned, sigma=-3) [FRAMING: the assignment is standard-QM; the Lambda<Sigma ORDERING is calibrated-to-data per step-3, NOT derived]"
    out["sigma_ud"] = "ud TRIPLET (aligned, sigma=+1) [FRAMING, as above]"
    out["meaning"] = "sigma_ij = the relative ROTOR ORIENTATION of the pair = the step-3 interference sign (NOT just practical)"
    out["per_baryon_assignment"] = "SU(6) 56 wavefunction = colour-antisym (trivectors) + Fermi (Spin4); TWT reconstructs, standard group theory (not novel); the resulting Lambda<Sigma ordering is FRAMING/calibrated (step-3), not derived"
    out["verdict"] = ("DERIVED (geometric MEANING only): sigma_ij = the discrete RELATIVE ROTOR ORIENTATION of "
                      "the quark pair = the step-3 interference sign -- triplet=aligned=constructive, "
                      "singlet=anti-aligned=destructive (the rotor READING of the generic spin-1/2 values "
                      "+1/4,-3/4); trace-zero = the centroid floor (step4). So sigma_ij is NOT just practical "
                      "bookkeeping -- it has a rotor-orientation meaning. FRAMING / standard-QM (NOT derived): "
                      "WHICH pair is singlet/triplet (the SU(6) 56 wavefunction, from colour-antisym + Fermi, TWT "
                      "reconstructs) AND the resulting Lambda<Sigma ORDERING (calibrated to the Sigma-Lambda datum, "
                      "step-3) -- neither is independently derived. Only the rotor-interpretation of sigma_ij is DERIVED-as-meaning.")
    return out


# ---- §17.3  the same-composition-split eigenvalues (three-facet S2-symmetry inertia; "gear"=legacy label) ----
def gear_eigenvalues():
    """[DERIVED] §17.3: colour-singlet (ω1+ω2+ω3=Ω_B) removes one rotor dof; for a
    symmetric light pair (I_pair) + heavy quark (I3 = x_Q·I_pair) the effective 2×2
    inertia M = [[I_p+I3, I3],[I3, I_p+I3]] has eigenvalues
        Θ_A = I_pair                 (Λ-type, K_L=0, mode (1,-1)),
        Θ_B = I_pair + 2 I3 = I_pair(1+2 x_Q)   (Σ-type, K_L=1, mode (1,1)).
    COMPUTED symbolically."""
    Ip, x = sp.symbols('I_pair x_Q', positive=True)
    I3 = x * Ip
    M = sp.Matrix([[Ip + I3, I3], [I3, Ip + I3]])
    eig = M.eigenvals()                       # {eigenvalue: multiplicity}
    vals = set(sp.simplify(e) for e in eig)
    return {
        "eigenvalues": vals,
        "Θ_A = I_pair (Λ-type)": Ip in vals,
        "Θ_B = I_pair(1+2x_Q) (Σ-type)": sp.simplify(Ip * (1 + 2*x)) in vals,
    }


def gear_inertia_form_from_S2_symmetry() -> dict:
    """[DERIVED symmetry-adapted BASIS (gate-free) + GENERIC split/entries + FRAMING spin labels +
    GAP-GATED values] item 8b residual (a), last gate-free handle: the §17.3 gear inertia tensor FORM,
    previously only POSITED (gear_eigenvalues computes eigenvalues of a hand-written 2x2 M=[[I_p+I3,I3],
    [I3,I_p+I3]]). Here the FORM's symmetry-adapted BASIS is DERIVED; the two-mode SPLIT, the entry
    parametrization, and the spin/Lambda-Sigma identification stay generic/FRAMING/gated. [Scope set after
    a twt-reviewer MISLABELED/OVER-CLAIM catch: an earlier draft said S_2 'forces the eigenmodes for ANY
    a,b' -- vacuous at b=0 where the matrix is a*I and every vector is an eigenvector -- and folded the
    imported K_L<->spin<->Lambda/Sigma identification under DERIVED. Both corrected below.]

    THE DERIVATION CHAIN:
      (1) [DERIVED, §17.2 + mass_reconciliation_U1_Spin3] the collective rotation is A(t) in SPIN(3)
          (the anti-self-dual triple closes su(2)); the inertia is a symmetric form on this manifold.
      (2) [DERIVED facts, leaning on baryon_mass_shared_rotor_nonadditive] colour contributes NO inertia
          cross-channel: the colour trivectors {e124,e134,e234} are ORTHONORMAL (engine-verified below),
          so a quadratic inertia form has no colour bilinear cross-term => the collective inertia lives in
          the Spin(3)(x)light-pair sector. (This is the no-bilinear-cross-term consequence of the DERIVED
          orthonormality; the broader colour mass-blindness is the FRAMING+DERIVED-facts dependency.)
      (3) [DERIVED basis (by symmetry); generic split] for the §17.3 case (a symmetric LIGHT PAIR + one
          distinct heavy/strange quark) the two identical light quarks carry an exchange symmetry S_2,
          i.e. the inertia 2x2 COMMUTES with the exchange P=[[0,1],[1,0]]. Therefore M is DIAGONAL in the
          symmetry-ADAPTED basis -- the eigenvectors of P -- which are (1,1) and (1,-1) ALWAYS:
             symmetric  (1, 1)  -> eigenvalue a+b,
             antisym    (1,-1)  -> eigenvalue a-b.
          So the BASIS is symmetry-forced (gate-free). BUT the two modes are DISTINCT (a non-trivial
          Lambda/Sigma SPLIT, and a UNIQUE physical basis) ONLY when the off-diagonal b != 0: at b=0,
          M=a*I is degenerate and (1,+-1) is merely one admissible choice. And b -- the coupling of the
          distinct quark to the light diquark -- is exactly the GENERIC-Willis / gap-gated piece. So the
          SPLIT and the basis-SELECTION ride on the un-derived off-diagonal; only the symmetry-adapted
          basis itself is derived.

    => UPGRADE (honestly scoped): the gear inertia FORM is no longer a bare posit -- its symmetry-adapted
       BASIS (the sym/antisym modes (1,+-1) of the light-pair S_2 on the colour-blind Spin(3) manifold)
       is DERIVED, gate-free. What stays NOT-derived:
         * GENERIC (Willis/Callan-Klebanov): the SPLIT and the entry parametrization a=I_p+I3, b=I3
           (off-diagonal = the heavy-to-diquark coupling, LINEAR in I3=x_Q*I_p) -- standard chiral-soliton
           heavy-baryon model; the Lambda/Sigma degeneracy-lifting lives here.
         * FRAMING / standard-QM (per su6_pairs_are_rotor_orientation, which tags it so): the physical
           identification (1,1)<->K_L=1<->Sigma<->diquark SPIN-1 and (1,-1)<->K_L=0<->Lambda<->SPIN-0.
           TWT reconstructs but does not DERIVE this; it is imported SU(6)/chiral-soliton phenomenology.
         * GAP-GATED (#1 gap): the VALUES I_pair, I3, x_Q = m_Q*Theta_0 (soliton profile / f_pi scale).

    derived-vs-generic: substrate-specific = (i) Spin(3) collective manifold, (ii) colour no-inertia-
    cross-channel (from orthonormality), (iii) the residual symmetry of the light-pair sector is S_2 ->
    the symmetry-adapted basis is (1,+-1); GENERIC = 'S_2 has sym+antisym irreps' + the Willis linear
    entries + the b!=0 split; FRAMING = the K_L<->spin<->Lambda/Sigma identification. No value, no fit.
    This derives the BASIS half of the inertia-FORM question; the split, the spin labels, and the scale
    remain (generic + FRAMING + #1 gap)."""
    out = {}

    # (2) colour is inertia-blind: the colour trivectors are orthonormal (no cross-term inertia channel)
    col = [e(1, 2, 4), e(1, 3, 4), e(2, 3, 4)]
    def ip(a, b):                                   # Clifford scalar inner product <a~ b>_0
        return (a.reverse() * b).coeff(())
    gram = [[ip(a, b) for b in col] for a in col]
    out["colour_trivectors_orthonormal"] = all(
        abs(gram[i][j] - (1.0 if i == j else 0.0)) < 1e-12 for i in range(3) for j in range(3))
    assert out["colour_trivectors_orthonormal"], "colour trivectors must be orthonormal (inertia-blind, no colour channel)"

    # (1) collective manifold is Spin(3): the anti-self-dual triple closes su(2)
    J = [e(1, 2) + e(3, 4), e(1, 3) - e(2, 4), e(1, 4) + e(2, 3)]
    def comm(a, b):
        return a * b - b * a
    def zero(x):
        return all(abs(c) < 1e-12 for _, c in x.terms)
    out["collective_manifold_is_Spin3"] = zero(comm(J[0], J[1]) - (-4) * J[2])
    assert out["collective_manifold_is_Spin3"], "collective rotation must be Spin(3) (triple closes su(2))"

    # (3) THE DERIVATION: M commutes with the exchange P -> the symmetry-ADAPTED basis is P's
    #     eigenvectors (1,+-1) (ALWAYS); M is diagonal in it with eigenvalues a+-b.
    a, b = sp.symbols('a b', real=True)
    M = sp.Matrix([[a, b], [b, a]])
    P = sp.Matrix([[0, 1], [1, 0]])                 # the S_2 light-pair exchange
    out["inertia_commutes_with_S2_exchange"] = (sp.simplify(M * P - P * M) == sp.zeros(2, 2))
    assert out["inertia_commutes_with_S2_exchange"], "S_2-invariance: [M, P] = 0"
    # P's eigenvectors are (1,+-1) (the symmetry-adapted basis), and M is diagonal there
    sym, anti = sp.Matrix([1, 1]), sp.Matrix([1, -1])
    out["sym_adapted_basis_is_P_eigenvecs"] = (sp.simplify(P * sym - sym) == sp.zeros(2, 1)
                                               and sp.simplify(P * anti + anti) == sp.zeros(2, 1))
    out["M_diagonal_in_adapted_basis"] = (sp.simplify(M * sym - (a + b) * sym) == sp.zeros(2, 1)
                                          and sp.simplify(M * anti - (a - b) * anti) == sp.zeros(2, 1))
    assert out["sym_adapted_basis_is_P_eigenvecs"] and out["M_diagonal_in_adapted_basis"], \
        "the symmetry-adapted basis (1,+-1) must diagonalize M with eigenvalues a+-b"
    # HONEST: the SPLIT (distinct eigenvalues) and the unique basis require b != 0 (else M=a*I, degenerate)
    out["split_requires_offdiagonal_b"] = (sp.simplify((a + b) - (a - b)) != 0)   # = 2b, nonzero iff b!=0
    out["sym_mode_eigenvalue"] = "a+b  (K_L=1, Sigma-type) [K_L/spin/Lambda-Sigma label = FRAMING/standard-QM]"
    out["antisym_mode_eigenvalue"] = "a-b  (K_L=0, Lambda-type) [label FRAMING; split needs b!=0 = generic/gated]"

    # identify with gear_eigenvalues: a=I_p+I3, b=I3 -> Theta_B=a+b=I_p+2I3, Theta_A=a-b=I_p (cross-check)
    Ip, x = sp.symbols('I_pair x_Q', positive=True)
    I3 = x * Ip
    aa, bb = Ip + I3, I3
    out["matches_gear_eigenvalues"] = (sp.simplify((aa + bb) - Ip * (1 + 2 * x)) == 0
                                       and sp.simplify((aa - bb) - Ip) == 0)
    assert out["matches_gear_eigenvalues"], "the S_2 form must reproduce gear_eigenvalues Theta_A=I_p, Theta_B=I_p(1+2x_Q)"

    # FRAMING link to su6_pairs_are_rotor_orientation: the spin/Lambda-Sigma identification of the modes
    # (NOT derived here -- su6_pairs itself tags the per-baryon assignment FRAMING/standard-QM)
    sp6 = su6_pairs_are_rotor_orientation()
    out["FRAMING_modes_id_with_diquark_spin"] = (abs(sp6["triplet_aligned_constructive"] - 0.25) < 1e-12
                                                 and abs(sp6["singlet_antialigned_destructive"] + 0.75) < 1e-12)

    out["DERIVED_symmetry_adapted_basis"] = ("the inertia 2x2 commutes with the light-pair exchange S_2 -> its "
                                             "symmetry-adapted basis is (1,+-1) (sym/antisym) on the colour-blind "
                                             "Spin(3) collective manifold. Gate-free. (BASIS only.)")
    out["GENERIC_split_and_entries"] = ("the Lambda/Sigma SPLIT needs b!=0; the entries a=I_p+I3, b=I3 "
                                        "(linear-in-heavy-moment Willis/Callan-Klebanov reduction) are the standard "
                                        "chiral-soliton model, not derived -- the split lives HERE")
    out["FRAMING_spin_labels"] = ("(1,1)<->K_L=1<->Sigma<->spin-1 / (1,-1)<->K_L=0<->Lambda<->spin-0 = imported "
                                  "SU(6)/chiral-soliton phenomenology (su6_pairs tags it FRAMING/standard-QM), not derived")
    out["GAP_GATED_values"] = "I_pair, I3, x_Q=m_Q*Theta_0 (soliton profile / f_pi scale) = #1 gap"
    out["verdict"] = ("§17.3 inertia FORM: the symmetry-adapted BASIS (sym/antisym (1,+-1) of the light-pair S_2 "
                      "on the colour-blind Spin(3) manifold) is DERIVED gate-free -- upgrades gear_eigenvalues from "
                      "fully-posited to basis-grounded. The two-mode SPLIT (needs b!=0) + entries are generic-Willis, "
                      "the K_L/spin/Lambda-Sigma labels are FRAMING/standard-QM, and the VALUES are #1-gap-gated. "
                      "8b residual (a): freq-lock + reconciliation + inertia-BASIS now derived; the split magnitude, "
                      "spin labels, entry model, and scale remain (generic + FRAMING + #1 gap).")
    return out


def quark_regimes():
    """[DERIVED] §17.3: x_Q classifies the regime. Crossover x_Q~1 ↔ m_Q~1/Θ_0≈196 MeV≈Λ_QCD
    (was ≈215 before the R-133 Θ-coefficient correction; the Λ_QCD proximity IMPROVED)."""
    masses = {"u/d": 3.5, "s": 93, "c": 1275, "b": 4180, "t": 172760}
    return {q: round(x_Q(m), 2) for q, m in masses.items()}


# ---- §17.3  forward predictions (one anchor + fit-inherited hyperfine corrections) ----
def heavy_baryon_predictions():
    """[anchor PREDICTED; hf fit-inherited — read precisely, NOT a clean VALIDATED] §17.3:
    Σ_Q-Λ_Q = 1/Θ_0 - hf_Q. The PREDICTED part is the anchor 1/Θ_0 = 195.6 (from f_π/e, no
    heavy-sector input; CORRECTED from 214.7 by R-133 — the old Θ-coefficient was wrong).
    hf_c=43.7, hf_b=13.7 are NOT computed here — they are fit-inherited
    constants from the disclosed global fit's B_0 (typed in, not re-derived from the light
    sector via the CMI ∝ 1/(m_i m_j) law). So 'no further fitting' = 'no fitting BEYOND the
    disclosed 6-parameter hadron fit', not parameter-free.
    POST-CORRECTION NUMBERS (R-133, 2026-07-03): Σ_c-Λ_c = 195.6-43.7 = 151.9 vs 167
    (-9.0%) — a TRACKED RESIDUAL (the old 2.4% agreement rode the WRONG constant; it was
    accidental); Σ_b-Λ_b = 195.6-13.7 = 181.9 vs 191 (-4.8%, slightly improved from 5.2%).
    CANDIDATE resolution of the c-leg residual (named, not decided): the heavy-baryon Σ-Λ
    inertia may be a bound-state-class object distinct from the rigid-rotor B=1 Θ_0
    (P2-7-adjacent). Promoting hf to a prediction needs B_0 fixed by the light sector +
    the CMI law in code (OPEN)."""
    inv_T0 = numerical_chain()["1/Θ_0 (MeV)"]
    hf_c, hf_b = 43.7, 13.7
    pred_c, data_c = inv_T0 - hf_c, 167.0
    pred_b, data_b = inv_T0 - hf_b, 191.0
    return {
        "Σ_c-Λ_c": {"pred": pred_c, "data": data_c, "err%": abs(pred_c-data_c)/data_c*100},
        "Σ_b-Λ_b": {"pred": pred_b, "data": data_b, "err%": abs(pred_b-data_b)/data_b*100},
    }


# ---- §17.4  the hadron mass operator (structure; V1 30-hadron fit retired from V2 paper body) ----------
def mass_operator_form():
    """[DERIVED structure; FIT RESULT paper-reported, not computed here] §17.4:
    M = M_0 + K_L(K_L+1)/(2Θ_eff) + m_Q^eff + n_s·δm_s + E_CMI.
    V1 paper §17.4 reported: 30-hadron fit (octet+decuplet+heavy+light vectors) → 0.74% RMS, 6 nominal /
    ~9 effective parameters (audit-found undercount: 3 of 7 optimizer dims silently overridden by snapped
    values ε_u=2, ε_d=1, b_d=π, ψ=2/9 — W-LIVE-MASS-AUDIT 2026-06-29) — (δm_s, m_c^eff, m_b^eff, α_{H1},
    B_0, g_ρ) plus the snapped ghost dims, with five constraints from the gear (M_0, Θ_0; γ=(Σ-Λ)/2=38.5;
    η_dec=δm_s-x_s/Θ_0; α_{H0}=α_{H1}+77; c_M=0).
    ⚠️ V1-ONLY RESIDUAL (worklist F3, NOT a tracked port): the FORMULA STRUCTURE is verified; the FIT itself
    (the 0.74% RMS and the 'five free constraints' claim) is NOT performed here — the string below
    reports the V1 paper's result, it does not compute it. NOTE (standing 2026-06-24 directive, Yaer +
    W-LIVE-MASS-AUDIT 2026-06-29): the historical twt_baryon_rho30.py and mass_formula_v14.py are
    deliberately NOT in this repo and are NOT to be ported (snapping-disguised-as-derivation per
    workflow audit; the V2 paper body has removed the 30-hadron-fit claim accordingly)."""
    return ("M = M_0 + K_L(K_L+1)/(2Θ_eff) + m_Q^eff + n_s·δm_s + E_CMI  "
            "[V1 paper-reported: 6 nominal / ~9 effective params (audit), 0.74% RMS, 30 hadrons — "
            "NOT computed in this library; retired from V2 paper body]")

def gell_mann_okubo_gamma(Sigma_minus_Lambda: float = 77.0) -> float:
    """[INPUT, calibrated] §17.4: γ = (Σ-Λ)/2 = 38.5 MeV — FIXED BY the one Σ-Λ calibration (it is the
    half of an input datum, not a derived number; the structure that γ has this ROLE is what §17.4
    derives). Tier corrected from a prior mislabel: a quantity calibrated to a datum is INPUT, not DERIVED."""
    return Sigma_minus_Lambda / 2.0


def generation_subharmonic_ladder():
    """[FIT (cross-checked) + FRAMING + CANDIDATE — matter-as-defect generation frequencies; TWT_DEFECT_CKM_GLUON.md]
    Yaer's directive (2026-06-26): read the generations as the 3 PROTECTED SUB-HARMONICS of the defect
    (mass = the meta-time rotor frequency ω; the defect spins SLOWER than the vacuum, only at protected
    frequencies), and use the CKM ASYMMETRY to find what it means IN TERMS OF FREQUENCY. Work from OUTSIDE
    the wavefront. **CKM + lepton masses are LOAD-BEARING (physical/measured).** Quark masses: per canon §5
    they may not VERIFY, but the one place they enter (the GST relation |V_us|²=m_d/m_s) they carry the
    content, so they are INDICATOR-level there (cf. N12) — NOT witness-only, NOT a verification; the real
    object remains impact-on-hadron. NOT a toy: these are EMPIRICAL data
    (predictions-vs-data, canon §3 rule 2), and FITTING is allowed + labeled (Yaer; canon §0a).

    ── CKM ASYMMETRY → FREQUENCY (the read) ───────────────────────────────────────────────────────────
    • **The established GATTO-SARTORI-TONIN / FRITZSCH relation, RE-READ in the defect frame** [the relation
      is TEXTBOOK (1968); the TWT content is the INTERPRETATION, not the relation]: |V_us| ≈ sqrt(m_d/m_s)
      (0.3%: 0.2243 vs 0.2236). In the matter-as-defect frame (mass = ω) this READS as: the mixing = sqrt(down
      1-2 FREQUENCY step), ω_d/ω_s = |V_us|² = 0.050. **HONESTY (reviewer-enforced): this leg's empirical bite
      IS a quark-mass relation (|V_us|² = m_d/m_s) — per canon §5 it is an INDICATOR-level cross-check (cf.
      N12), NOT a verification, and the quark masses are NOT 'witness-only' here, they carry the content.** The
      TWT contribution is the ω-ladder reading + the protected-sub-harmonic hypothesis.
    • **NOT an over-determination** [reviewer correction — avoids the N10 error]: the Cabibbo read and the
      "down 1-2 mass-step" read are the SAME GST relation (its two sides), NOT two independent sectors. The
      lepton 2-3 sqrt-step sqrt(m_μ/m_τ)=0.244 lands near the same value but is 8% off — a LOOSE coincidence,
      not a tight third leg. So this is ONE relation + ONE loose coincidence, **not** D/J-style independent-path
      over-determination. The ladder is also NOT one universal λ per rung: the down 2-3 step is 0.15 and the
      lepton 1-2 step is 0.07 (rung-dependent λ-powers = the Wolfenstein/Froggatt-Nielsen texture, as expected).
      λ = sin θ_C = |V_us| = 0.225 (NOT D/J = 0.79; θ_C = ⅓·arctan(D/J), the banked Cabibbo).

    ── CHIRALITY (the up/down asymmetry Yaer flagged) ─────────────────────────────────────────────────
    • the UP tower is the chirality-STEEPENED down tower: at gen 1-2 the up frequency step is ≈ the SQUARE
      of the down step, ω_u/ω_c ≈ (ω_d/ω_s)² (exponents in λ: down 2.01, up 4.27 ≈ 2×). [CANDIDATE — WITNESS
      masses; not cleanly CKM-derivable on the up side, Fritzsch up-relation is poor]
    • the within-generation up/down ratio GROWS with generation (m_u/m_d=0.46, m_c/m_s=13.6, m_t/m_b=41) →
      the chirality effect INCREASES with frequency/generation (the gen-2,3 difference). The clean ×2 doubling
      holds best at 1-2 (4.27 vs 4.02); at 2-3 the up is steeper but not exactly double (3.29 vs 2.55). [CANDIDATE]

    ── LEPTONS as a parameterization ─────────────────────────────────────────────────────────────────
    Koide K=2/3 EXACT (the symmetric sqrt2-circle, Brannen). In the defect frame this is a RE-PARAMETERIZATION
    of the SAME geometric frequency ladder (the lepton steps ride λ: sqrt(m_μ/m_τ)≈λ, sqrt(m_e/m_μ)≈λ²). The
    circle is one chart; the sub-harmonic LADDER is the defect-frame picture (Yaer: "Brannen is probably just
    a parameterization, not the real picture"). [FRAMING]

    ── PROTECTION (the owed piece) ───────────────────────────────────────────────────────────────────
    The data is CONSISTENT with a PROTECTED geometric ladder (ONE ratio λ governs masses AND mixing across ALL
    towers — strong evidence FOR the sub-harmonic picture) with a CHIRALITY exponent-split for up vs down. But
    DERIVING the protection — why λ, why exactly 3 rungs, the precise ± chirality law — is the owed
    SUB-HARMONIC-STABILITY calculation (the driven defect-in-vacuum resonance), GATED at the #1 gap. So: the
    FREQUENCY READING is done (CKM → a λ-ladder + chirality steepening); the PROTECTION DERIVATION is LOCATED,
    not done. NOT DERIVED anywhere here.

    self-check: the GST relation |V_us|≈sqrt(m_d/m_s) holds to <1%; the lepton 2-3 step is a LOOSE coincidence
    (8% off, NOT a 3rd over-determination leg); up 1-2 exponent ≈ 2× down 1-2; Koide K=2/3."""
    import math
    # LOAD-BEARING: lepton masses (physical, MeV) + measured CKM
    m_e, m_mu, m_tau = 0.5109989, 105.6584, 1776.93
    Vus = 0.2243
    lam = 0.225
    # quark masses: INDICATOR-level in the GST leg (m_d,m_s carry |V_us|²=m_d/m_s); the heavy ones are
    # CANDIDATE-level witnesses for the chirality steepening (up-side not CKM-clean) — never a verification (§5/N12)
    m_u, m_c, m_t = 2.16, 1270.0, 172500.0
    m_d, m_s, m_b = 4.67, 93.4, 4180.0
    cabibbo_freq = math.sqrt(m_d / m_s)
    assert abs(Vus - cabibbo_freq) / Vus < 0.01                       # GST relation |Vus|≈sqrt(m_d/m_s), 0.3%
    lep_23 = math.sqrt(m_mu / m_tau)
    assert abs(lep_23 - Vus) / Vus < 0.10                            # lepton 2-3 near Cabibbo — LOOSE (8%), a coincidence not a 3rd leg
    exp_down12 = math.log(m_d / m_s) / math.log(lam)
    exp_up12 = math.log(m_u / m_c) / math.log(lam)
    assert abs(exp_up12 - 2 * exp_down12) / (2 * exp_down12) < 0.15   # up 1-2 ≈ (down 1-2)²  (chirality doubling)
    K = (m_e + m_mu + m_tau) / (math.sqrt(m_e) + math.sqrt(m_mu) + math.sqrt(m_tau)) ** 2
    assert abs(K - 2.0 / 3.0) < 1e-3                                  # Koide exact
    return {
        "frame": "matter-as-defect, mass=ω (meta-time freq), from OUTSIDE the wavefront; CKM+leptons LOAD-BEARING",
        "gst_fritzsch_relation_re_read": {
            "relation": "|V_us| ≈ sqrt(m_d/m_s) — the TEXTBOOK Gatto-Sartori-Tonin/Fritzsch relation (1968)",
            "|Vus|": Vus, "sqrt(m_d/m_s)": round(cabibbo_freq, 4), "pct_off": round(100 * abs(Vus - cabibbo_freq) / Vus, 2),
            "defect-frame reading": "mixing = sqrt(down 1-2 FREQUENCY step); omega_d/omega_s = |Vus|^2 = " + str(round(Vus ** 2, 4)),
            "honesty": "the bite IS a quark-mass relation (|Vus|^2=m_d/m_s) — INDICATOR-level (canon §5/N12), NOT 'witness-only', NOT a verification",
            "TWT_content": "the INTERPRETATION (omega-ladder + sub-harmonic hypothesis), NOT the relation (textbook)"},
        "NOT_an_over_determination": {
            "lepton_2-3_sqrt_step": round(lep_23, 4), "off_from_Vus_pct": round(100 * abs(lep_23 - Vus) / Vus, 1),
            "why": "Cabibbo and the down-1-2 read are the SAME GST relation (two sides), not 2 sectors; + 1 loose lepton "
                   "coincidence (8%) = NOT independent over-determination (avoids the N10 error)",
            "ladder_not_one_lambda": {"down_2-3_step": round(math.sqrt(m_s / m_b), 3), "lepton_1-2_step": round(math.sqrt(m_e / m_mu), 3),
                                      "note": "rung-dependent lambda-powers (Wolfenstein/Froggatt-Nielsen), not one universal lambda"},
            "lambda_def": "lambda = sin(theta_C) = |Vus| = 0.225 (NOT D/J=0.79; theta_C = 1/3 arctan(D/J), the banked Cabibbo)"},
        "chirality_doubling_gen_1-2": {"down_exp_in_lambda": round(exp_down12, 2),
                                       "up_exp_in_lambda": round(exp_up12, 2),
                                       "up~2x_down (up step = down step squared)": True,
                                       "tier": "CANDIDATE (witness masses; up-side not CKM-clean)"},
        "up_down_ratio_grows_with_gen": {"g1_mu/md": round(m_u / m_d, 2), "g2_mc/ms": round(m_c / m_s, 1),
                                         "g3_mt/mb": round(m_t / m_b, 1), "meaning": "chirality effect grows with generation"},
        "koide_is_a_parameterization": {"K": round(K, 5), "is_2/3": True,
                                        "reading": "the sqrt2-circle is a re-parameterization of the SAME λ-ladder (defect-frame = the ladder)"},
        "protection_status": "CONSISTENT with a protected λ-ladder + chirality split (one λ governs masses AND "
                             "mixing across all towers); DERIVING protection (why λ, why 3, the ± chirality law) = "
                             "the owed sub-harmonic-stability calc (driven defect-in-vacuum), GATED at the #1 gap",
        "tiers": "FIT (the GST/Fritzsch relation re-read, INDICATOR-level per §5); FRAMING (the ω-ladder reading + "
                 "Koide-as-parameterization + the loose lepton coincidence); CANDIDATE (chirality doubling, clean only "
                 "at 1-2); LOCATED/GATED (protection). NOT DERIVED — the relation is textbook, the TWT content is the interpretation.",
        "discipline": "CKM load-bearing; the GST quark-mass leg is INDICATOR-level (not witness-only, not a verification, §5/N12); "
                      "mass=ω; work-from-outside; no toy (empirical data); GST credited; NOT over-determination (N10 error avoided)",
    }


def subharmonic_transition_cost():
    """[FRAMING + CANDIDATE — the transition PROBABILITY read as a COST (barrier action), not a ratio; Yaer 2026-06-26]
    Yaer: "a transition probability is better interpreted in TWT as a transition COST between the frequencies
    than a frequency ratio." This is the SAME Cabibbo/GST number as `cabibbo_transition_probability`
    (P(d↔s)=ω_d/ω_s), RE-EXPRESSED: **P = exp(−Cost)**, Cost = ln(ω_higher/ω_lower) = the log-frequency GAP.
    The NEW content is the cost/barrier INTERPRETATION + the log-frequency-line geometry + the bridge to the
    HYSTERETIC kernel — NOT a new empirical fact (the underlying number is the textbook GST relation).

    • **Cost(d↔s) = ln(ω_s/ω_d) = ln(20.0) = 3.00 ⇒ P = exp(−3.00) = 0.050** (0.6% vs |V_us|²). A "cost"
      (= −ln P) is an ACTION/BARRIER, not a bare ratio — what a defect must "pay" to transition between two
      protected sub-harmonics. [the GST relation, re-expressed]
    • **The protected sub-harmonics sit on a LOG-FREQUENCY LINE; the transition cost = the DISTANCE between
      them.** Costs are ADDITIVE (Cost(d-s)+Cost(s-b) = Cost(d-b), 3.00+3.80=6.80), probabilities multiply —
      the natural geometry of a geometric (sub-harmonic) ladder. [FRAMING]
    • **CHIRALITY DOUBLES the cost** [CANDIDATE]: Cost_up(u↔c) = ln(ω_c/ω_u) = 6.38 ≈ 2×Cost_down(d↔s) = 5.99
      (ratio 2.13). The up/down asymmetry, in cost language, is that the +e₄ handedness DOUBLES the barrier
      action for the up-sector — the cleanest name for the steepening (= the λ-exponent-doubling re-expressed;
      clean at 1-2, degrades at 2-3).
    • **BRIDGE to the hysteretic kernel** [FRAMING — the reason 'cost' is the right TWT object]: P = exp(−Cost)
      is a tunneling/instanton amplitude — Cost is a REACTIVE-BARRIER ACTION of the §9.6 HYSTERETIC type
      (τ_mem ~ exp(S/ħ); Fork A, Yaer-settled hysteretic). So the CKM transition cost = a barrier action of the
      SAME #1-gap S-face that gives τ_mem (item 18). This CONNECTS the CKM magnitudes to the reactive barrier
      (complementary to the Θ_rel curvature-face); it does NOT derive the value — deriving Cost(d↔s)=ln(20)
      (why those protected frequencies) is the owed PROTECTION calc, GATED at the #1 gap.

    Tiers: FRAMING (cost reading + log-freq-line geometry + the hysteretic-kernel bridge); CANDIDATE (chirality
    cost-doubling); the GST relation re-expressed (indicator-level, §5/N12). NOT DERIVED — exp(−Cost) is the
    standard Boltzmann/tunneling form; the TWT content is the barrier interpretation + the kernel bridge.
    self-check: P=exp(−Cost) matches |V_us|² to <2%; costs additive on the log-freq line; chirality cost ≈ 2× down."""
    import math
    Vus = 0.2243
    m_u, m_c = 2.16, 1270.0
    m_d, m_s, m_b = 4.67, 93.4, 4180.0
    cost_ds = math.log(m_s / m_d)                          # log-frequency gap = barrier action
    P_from_cost = math.exp(-cost_ds)
    assert abs(P_from_cost - Vus ** 2) / Vus ** 2 < 0.02   # P = exp(-Cost) = |Vus|^2 (the GST relation)
    cost_sb = math.log(m_b / m_s)
    cost_db = math.log(m_b / m_d)
    assert abs((cost_ds + cost_sb) - cost_db) < 1e-9       # ADDITIVE: costs = distances on the log-freq line
    cost_up = math.log(m_c / m_u)
    assert abs(cost_up - 2 * cost_ds) / (2 * cost_ds) < 0.15   # chirality DOUBLES the cost
    return {
        "reframing": "transition PROBABILITY = exp(-Cost); Cost = ln(omega_higher/omega_lower) = the log-frequency GAP (a barrier action), NOT a bare ratio — Yaer 2026-06-26",
        "cabibbo_cost": {"Cost(d<->s)=ln(omega_s/omega_d)": round(cost_ds, 3), "P=exp(-Cost)": round(P_from_cost, 4),
                         "|Vus|^2": round(Vus ** 2, 4), "pct_off": round(100 * abs(P_from_cost - Vus ** 2) / Vus ** 2, 2)},
        "log_frequency_line": {"additive": "Cost(d-s)+Cost(s-b) = Cost(d-b)", "values": f"{cost_ds:.2f}+{cost_sb:.2f}={cost_ds+cost_sb:.2f} = {cost_db:.2f}",
                               "meaning": "protected sub-harmonics ORDERED on a log-freq axis; cost = DISTANCE; probabilities multiply, costs add",
                               "caveat": "the additivity is the TRIVIAL identity ln(a)+ln(b)=ln(ab) (true for any 3 numbers); the rungs are NOT "
                                         "equally spaced (gap d-s=3.00 != s-b=3.80) — 'line' means ordered-on-a-log-axis, NOT an evenly-spaced lattice"},
        "chirality_doubles_the_cost": {"Cost_up(u<->c)": round(cost_up, 2), "2x_Cost_down": round(2 * cost_ds, 2),
                                       "ratio": round(cost_up / cost_ds, 2), "tier": "CANDIDATE (= the exponent-doubling re-expressed; clean 1-2)"},
        "hysteretic_kernel_bridge": "P=exp(-Cost) INVITES THE READING that Cost is a REACTIVE-BARRIER action of the §9.6 HYSTERETIC type "
                                    "(tau_mem~exp(S/hbar); Fork A Yaer-settled) — any P in (0,1) can be written exp(-something), so this is an "
                                    "INTERPRETIVE identification, not a logical implication. IF so, CKM transition cost = a barrier action of the SAME "
                                    "#1-gap S-face that gives tau_mem (item 18; consistent with ckm_arc B3c, the barrier-height window); complementary to "
                                    "the Theta_rel curvature-face. FRAMING bridge, value GATED, NOT a derivation.",
        "honesty": "SAME number as cabibbo_transition_probability (the GST relation) re-expressed as a cost; exp(-Cost) is the standard Boltzmann/tunneling form; NOT DERIVED",
        "opens": "deriving Cost(d<->s)=ln(20) (why those protected frequencies + the barrier between them) = the owed PROTECTION calc, GATED at the #1 gap",
        "tier": "FRAMING (cost/barrier reading + log-freq-line geometry + hysteretic-kernel bridge) + CANDIDATE (chirality cost-doubling); NOT DERIVED",
    }


def generation_cost_step_structure():
    """[FIT + INDICATOR + FRAMING + CANDIDATE — why the cost climbs vs falls; the bare/dressed split; TWT_DEFECT_CKM_GLUON.md §10]
    Yaer's 3 questions (2026-06-26) for getting the protection mechanism right:
      (Q1) why does the transition cost CLIMB (1->2->3) in DOWN quarks but FALL in UP quarks + leptons?
      (Q2) does this follow constituent-mass logic? (constituent/bare masses as INDICATOR, not derivation)
      (Q3) what makes a frequency CHANGE — not just the cost of the change?

    ── Q1 — the cost-step DIRECTION (bare/current masses) [FIT, masses re-expressed] ──────────────────
    DOWN: Cost12=3.00, Cost23=3.80 -> RISING (+0.81). UP: 6.38, 4.91 -> FALLING (-1.47). LEPTON: 5.33, 2.82
    -> FALLING (-2.51). "Falling" = an anomalously ISOLATED (light) bare FIRST generation (u, e). DOWN rises
    because its gen-1 (d) is NOT anomalously light — the m_d > m_u inversion (the only generation where the
    down-type exceeds the up-type). **CANDIDATE reading:** the ± medium chirality acts on the FIRST (lightest)
    rung — pushing the up-type gen-1 frequency far DOWN (tiny m_u -> isolated -> falling) and the down-type
    gen-1 UP (m_d normal -> less isolated -> rising), relative to the lepton "base" (electron-light -> falling).
    This is WHY the 1<->2 step showed the cleanest chirality-doubling: the chirality is concentrated at the bottom.

    ── Q2 — constituent re-read: the pattern is NOT dressing-invariant [INDICATOR + FRAMING — the key point] ─
    Re-read in CONSTITUENT masses (INDICATOR only, model-dependent, Yaer-sanctioned; u≈d≈336, s≈540, c≈1550,
    b≈4730 MeV): the **UP tower FLIPS falling -> RISING** (+3.18) — the ~336 MeV constituent floor SWAMPS the
    tiny bare m_u (2.16). DOWN stays rising; LEPTONS (undressed) stay falling, unchanged. ⇒ the climbing/falling
    pattern is a **BARE-frequency (weak-eigenstate) phenomenon**, NOT the constituent/hadron pattern. **TWO
    LAYERS:** the protected BARE sub-harmonic (the CKM cost-table, what the protection mechanism must produce)
    vs the vacuum-DRESSED frequency (constituent = impact-on-hadron = the bare ω + the **defect-vacuum
    interaction**, Yaer's gluon §4). The light quarks' hadron-impact is mostly vacuum-dressing, NOT their bare
    sub-harmonic (canon §5: only hadron-impact is physical). **The constituent quark mass is where the
    generation problem and the gluon problem MEET** — bare sub-harmonic + vacuum dressing.

    ── Q3 — what makes ω CHANGE (the reaction coordinate) [OPEN + CANDIDATE] ──────────────────────────
    The cost is the BARRIER; the open question is the COORDINATE the frequency is a function of. Engine-grounded
    candidate: √m = r² (banked mass-geometry) ⇒ ω = m = r⁴ ⇒ **Cost = 4·ln(radius-gap)**. So a candidate
    reaction coordinate is the defect's geometric RADIUS r (its size / winding-density in the rotor field);
    "what makes ω change" = what changes r. The radius-gaps are O(1) (0.7–1.6). **The deeper question — what
    STABILITY condition selects exactly 3 protected r (and the ± chirality split) — is the owed PROTECTION
    mechanism (N13, the why-3), GATED at the #1 gap.** Q3 is the right next question: identify the coordinate +
    the stability functional, not just the barrier heights.

    Tiers: FIT (bare cost-steps) + INDICATOR (constituent flip, model-dependent) + FRAMING (the bare/dressed
    two-layer split; the constituent = generation⊕gluon meeting point) + CANDIDATE (chirality-on-gen-1; r as
    coordinate) + OPEN (Q3 the stability condition). NOT DERIVED. Quark masses INDICATOR-level only (§5/Yaer).
    self-check: down rises, up+lepton fall (bare); up FLIPS to rising in constituent, lepton unchanged; Cost=4·ln(r-gap)."""
    import math
    def steps(m): c12 = math.log(m[1] / m[0]); c23 = math.log(m[2] / m[1]); return c12, c23, c23 - c12
    bare = {"down": [4.67, 93.4, 4180.0], "up": [2.16, 1270.0, 172500.0], "lepton": [0.5109989, 105.6584, 1776.93]}
    con = {"down": [336., 540., 4730.], "up": [336., 1550., 172500.], "lepton": [0.5109989, 105.6584, 1776.93]}  # INDICATOR
    bsteps = {t: steps(m) for t, m in bare.items()}
    csteps = {t: steps(m) for t, m in con.items()}
    # Q1: down rises, up & lepton fall (bare)
    assert bsteps["down"][2] > 0 and bsteps["up"][2] < 0 and bsteps["lepton"][2] < 0
    # Q2: up FLIPS to rising in constituent; lepton (undressed) unchanged
    assert csteps["up"][2] > 0 and abs(csteps["lepton"][2] - bsteps["lepton"][2]) < 1e-9
    # Q3: Cost = 4 ln(radius-gap)  via sqrt(m)=r^2
    r_gap_ds = math.log(math.sqrt(math.sqrt(93.4)) / math.sqrt(math.sqrt(4.67)))  # ln(r_s/r_d), r=m^(1/4)
    assert abs(4 * r_gap_ds - bsteps["down"][0]) < 1e-9
    return {
        "Q1_cost_step_direction_bare": {t: {"Cost12": round(v[0], 2), "Cost23": round(v[1], 2),
                                            "trend": "RISING" if v[2] > 0 else "FALLING"} for t, v in bsteps.items()},
        "Q1_reading": "down RISES, up+lepton FALL; falling = anomalously light bare 1st gen (u,e); down's gen-1 (d) NOT "
                      "anomalously light (m_d>m_u). CANDIDATE: ± chirality acts on the lightest rung (up gen-1 pushed down, down gen-1 up)",
        "Q2_constituent_INDICATOR": {t: {"Cost12": round(v[0], 2), "Cost23": round(v[1], 2),
                                         "trend": "RISING" if v[2] > 0 else "FALLING"} for t, v in csteps.items()},
        "Q2_finding": "UP FLIPS falling->rising (constituent ~336 swamps bare m_u=2.16); lepton (undressed) unchanged => the "
                      "climbing/falling pattern is a BARE-frequency phenomenon, NOT dressing-invariant. The flip is a 1->2 EFFECT "
                      "(the top has no constituent value, so the 2->3 step is ~unchanged 4.91->4.71); robust to the floor value (reviewer-scanned)",
        "Q2_two_layers": "BARE protected sub-harmonic (CKM cost-table; the protection target) vs vacuum-DRESSED (constituent = "
                         "impact-on-hadron = bare ω + the defect-vacuum interaction = Yaer's gluon §4). The constituent quark mass "
                         "is where the generation problem and the gluon problem MEET. Light quarks' hadron-impact is mostly dressing.",
        "Q3_reaction_coordinate": "the cost is the BARRIER; the open question is the COORDINATE. Candidate via √m=r²: ω=r⁴ ⇒ "
                                  "Cost=4·ln(radius-gap); r (defect radius/winding-density) is a candidate. The stability condition "
                                  "selecting exactly 3 protected r (+ the ± chirality split) = the owed PROTECTION mechanism (N13), GATED",
        "tiers": "FIT (bare steps) + INDICATOR (constituent flip, model-dependent) + FRAMING (bare/dressed two-layer; "
                 "constituent = generation⊕gluon meeting point) + CANDIDATE (chirality-on-gen-1; r-coordinate) + OPEN (Q3); NOT DERIVED",
        "discipline": "quark masses INDICATOR-level only (§5/Yaer-sanctioned); CKM/lepton-derived bare costs are the load-bearing object",
    }


def generation_gen2_chirality_mirror():
    """[FIT/observation + CANDIDATE — the middle generation's preferred position; up<->down mirror; TWT_DEFECT_CKM_GLUON.md §11]
    Yaer's observation (2026-06-26): 3.00/6.80 ≈ 4.91/11.29 — "while the direction of the cost is opposite, the
    MIDDLE generation seems to have a preferred position." Worked out: read gen-2's position as a FRACTION of
    the full span on the cost (log-frequency) axis.

    • **DOWN** gen-2 = 0.441 of the span from the LIGHT end (gen-1); **UP** gen-2 = 0.435 from the HEAVY end
      (gen-3). These match to 1.4% ⇒ **up and down are MIRROR IMAGES**: gen-2 sits at the SAME off-center
      fraction (~0.44) but measured from OPPOSITE ends. Equivalently, gen-2's position is invariant under the
      combined reflection {up↔down} ∘ {light↔heavy} — exactly the **± chirality acting as a reflection**.
    • **OFF-CENTER:** ~0.44 ≠ 0.5 (equal-spacing would be 0.5) — a specific preferred fraction, not the midpoint.
    • **ROBUST to the (large) quark-mass uncertainties:** down-from-light = 0.440±0.015, up-from-heavy =
      0.434±0.010 (MC over PDG-ish errors) — CONSISTENT (Δ=0.006, ~0.3σ). **HONEST: this is a 6-number
      observation consistent WITHIN errors, NOT a tight/derived relation; resist numerology on 0.44.**
    • **LEPTONS do NOT share it:** lepton gen-2 = 0.346 from the heavy end (more off-center) — so the mirror is a
      **QUARK (up↔down, a weak-doublet) feature**; the charged-lepton's mirror partner would be the NEUTRINO
      (the open 4th tower — data too poor, PMNS anarchic). [observation]

    SIGNIFICANCE: a SECOND signature of the chirality-as-REFLECTION (up & down = the two chirality images),
    consistent with the cost-doubling (`generation_cost_step_structure`) — but BOTH are readings of the same
    cost table, NOT independent data (do NOT call it over-determination). CONSTRAINT on the owed protection
    mechanism: it must place the protected frequencies so gen-2 sits at the off-center fixed fraction ~0.44,
    mirror-imaged between up and down. Tier: FIT/observation (masses re-expressed) + CANDIDATE (chirality-mirror);
    consistent within large quark-mass errors; NOT DERIVED.
    self-check: down-from-light ≈ up-from-heavy (<2%); both ~0.44 & off-center (<0.5); leptons differ (<0.40)."""
    import math
    def frac_light(m): return math.log(m[1] / m[0]) / math.log(m[2] / m[0])   # gen-2 from the light end
    def frac_heavy(m): return math.log(m[2] / m[1]) / math.log(m[2] / m[0])   # gen-2 from the heavy end
    down = [4.67, 93.4, 4180.0]; up = [2.16, 1270.0, 172500.0]; lep = [0.5109989, 105.6584, 1776.93]
    fd = frac_light(down)        # down gen-2 from light = 0.441
    fu = frac_heavy(up)          # up gen-2 from heavy = 0.435
    fl = frac_heavy(lep)         # lepton gen-2 from heavy = 0.346
    assert abs(fd - fu) < 0.02                      # the mirror match (1.4%)
    assert 0.42 < fd < 0.46 and fd < 0.5            # off-center ~0.44, not the midpoint
    assert fl < 0.40                                # leptons do NOT match -> quark feature
    return {
        "yaer_observation": "3.00/6.80 ≈ 4.91/11.29 (0.441 vs 0.435, 1.4%): the middle generation has a preferred position",
        "gen2_position_fraction_of_span": {"down_from_LIGHT": round(fd, 3), "up_from_HEAVY": round(fu, 3),
                                           "lepton_from_HEAVY": round(fl, 3)},
        "reading": "UP & DOWN are MIRROR images: gen-2 at the SAME off-center fraction ~0.44, measured from OPPOSITE ends "
                   "(invariant under {up<->down}∘{light<->heavy} = the ± chirality REFLECTION). Off-center (~0.44 != 0.5).",
        "robustness": "down-from-light 0.440±0.015, up-from-heavy 0.434±0.010 (MC over PDG-ish errors) — CONSISTENT (~0.3σ), "
                      "NOT a tight relation; a 6-number observation; resist numerology on 0.44",
        "leptons": "lepton gen-2 = 0.346 (more off-center) — the mirror is a QUARK up<->down (weak-doublet) feature; the "
                   "charged-lepton's mirror partner = the NEUTRINO (open 4th tower, data too poor)",
        "significance": "a 2nd signature of chirality-as-REFLECTION (up & down = chirality images), consistent with the "
                        "cost-doubling — but BOTH read the same cost table, NOT independent data (NOT over-determination)",
        "constraint_on_protection": "the owed mechanism must place gen-2 at the off-center fixed fraction ~0.44, mirror-imaged up<->down",
        "tier": "FIT/observation (masses re-expressed) + CANDIDATE (chirality-mirror; gen-2 preferred position); consistent within large quark-mass errors; NOT DERIVED",
    }


def cp_chirality_90_120_mismatch():
    """[FRAMING + located-negative N16 — the v14 circular-polarization attempt; TWT_DEFECT_CKM_GLUON.md §12]
    Yaer's directive (2026-06-26): try circular polarization (up/down = the two ±90° handedness, Jones (1,±i))
    in 4D+meta-time as the up/down chirality, and build a v14 mass formula (knowledge/archive/mass_formula_v14.py,
    the CP encoding replacing v13's four up/down amplitude knobs with ONE fixed ±π/2 phase). A 4-lens design
    workflow + developer verification returned a CLEAN, FOUR-FOLD NEGATIVE on the headline hypothesis, with real
    structural learning. This primitive records the engine-checkable STRUCTURAL CORE; the fit numbers live in the
    archive (illustrative).

    ── THE NEGATIVE (verified) ────────────────────────────────────────────────────────────────────────
    The CP ±90° structure does NOT reproduce the gen-2 ~0.44 mirror (or the bare cost table) from a HADRON-mass
    fit. Forcing the mirror toward 0.44 multiplies the hadron RMS ~5× (banked v14 FORM-B: 3.68%→~20%, reviewer-
    reproduced; the original Lens-D scratch read 2.6%→12.3%, ~4.75×, but that scratch is deleted — use the banked
    number). REASON (decisive, structural): hadron masses see only the vacuum-DRESSED/constituent ω (the fitted
    cost gaps come out ~5-10× smaller than the bare table; the free fit lands on the constituent fraction ~0.19,
    not 0.44), while the mirror is a BARE protected-sub-harmonic feature. So this is a CONVERGENT/consistency
    confirmation of the bare-vs-dressed two-layer split (`generation_cost_step_structure` §10) — NOT independent
    over-determination (hadron data + the §10 dressing premise route through the SAME dressed layer; cf. the
    N10/N12 distinction). The mirror lives in the bare/CKM cost table, which a hadron fit cannot probe — it is
    IMPOSED whenever present, never emergent.

    ── THE LOCATED GAP (engine-checkable core) ────────────────────────────────────────────────────────
    A π/2 (90°) circular-polarization phase is INCOMMENSURATE with the 3-fold generation spacing 2π/3 (120°):
    (π/2)/(2π/3) = 3/4 ∉ ℤ. So a CP phase-shift displaces a generation by ¾ of an inter-generation step — it maps
    a generation OFF the generation lattice (toward an adjacent rung), SCRAMBLING the tower rather than steepening
    it. This is WHY the CP-phase-on-the-circle (Lens A) fails: the free fit drives the CP phase → 0. RE-ATTACK
    (would change if): a per-rung CP action, or a sub-harmonic geometry where 90° and the generation spacing
    COMMUTE (this is the N16 handle).

    ── THE LEARNINGS (tiered) ─────────────────────────────────────────────────────────────────────────
    • [FRAMING — the legitimate advance] up/down = the two circular-polarization handedness = Spin(4)'s
      SU(2)₊/SU(2)₋ (self-dual/anti-self-dual), encoded as ONE fixed ±π/2 phase, REPLACES v13's four ad-hoc
      amplitude knobs (b_u,b_d,ε_u,ε_d) at v13's param count (7), fitting hadrons at ~3.68%. More principled,
      but the economy buys no new physics (the mirror still doesn't emerge).
    • [located-negative] the OUTSIDE-FRAME / HOLE sign flip (matter = a circularly-polarized hole) is
      UNOBSERVABLE in the hadron fit — flipping χ exactly swaps up↔down phases (χ=+1 RMS 3.677% vs χ=-1 3.689%,
      degenerate). Answers Yaer's check: matter-as-defect/outside-frame changes NOTHING in hadron masses (a
      relabeling); it would only bite with a top-tower or a CP-odd observable.
    • [modest positive] the down-RISING / up-FALLING cost trend emerges spontaneously from the free fit.

    Tier: FRAMING + located-negative (N16). The fit is FIT/ILLUSTRATIVE (archive). NOT DERIVED.
    self-check: the 90°/120° incommensurability (π/2)/(2π/3) = 3/4 ∉ ℤ (the geometric mismatch)."""
    import math
    cp_phase = math.pi / 2.0              # the circular-polarization ±90° handedness phase
    gen_spacing = 2.0 * math.pi / 3.0     # the 3-fold generation spacing (120°)
    displacement_in_steps = cp_phase / gen_spacing
    assert abs(displacement_in_steps - 0.75) < 1e-12          # = 3/4 of an inter-generation step
    assert abs(displacement_in_steps - round(displacement_in_steps)) > 0.2  # NOT an integer => off-lattice (scrambles)
    return {
        "verdict": "CLEAN four-fold NEGATIVE: the CP ±90° structure does NOT reproduce the gen-2 ~0.44 mirror from a hadron fit",
        "decisive_reason": "hadron masses see only DRESSED/constituent ω (free fit lands on the constituent fraction ~0.19, cost gaps "
                           "~5-10× smaller than bare); the mirror is a BARE-sector feature -> CONVERGENT/consistency confirmation of the §10 "
                           "bare-vs-dressed two-layer split (NOT independent over-determination; forcing the mirror toward 0.44 -> ~5× worse fit, 3.68%->~20%)",
        "located_gap_90_120": {"cp_phase_deg": 90, "gen_spacing_deg": 120, "displacement_in_gen_steps": round(displacement_in_steps, 3),
                               "incommensurate": True, "why": "(π/2)/(2π/3)=3/4 ∉ ℤ -> a CP shift moves a generation OFF the lattice, scrambling the tower (free fit drives CP phase->0)"},
        "would_change_if": "a per-rung CP action, OR a sub-harmonic geometry where 90° and the generation spacing 2π/3 commute (the N16 re-attack handle)",
        "framing_advance": "up/down = SU(2)+/SU(2)- circular-polarization handedness (Spin(4)), encoded as ONE fixed ±π/2 phase, "
                           "replaces v13's 4 amplitude knobs at v13's param count (~3.68% fit) — more principled, but no new physics (mirror still absent)",
        "outside_frame_unobservable": "the hole/outside-frame χ sign flip exactly swaps up<->down phases (χ=+1 3.677% vs χ=-1 3.689%, degenerate) "
                                      "-> UNOBSERVABLE in hadron masses; Yaer's check answered (NOTHING changes; relabeling only)",
        "emergent_positive": "down-RISING / up-FALLING cost trend falls out of the free fit (partly generic)",
        "tier": "FRAMING + located-negative N16; the fit is FIT/ILLUSTRATIVE (archive mass_formula_v14.py); NOT DERIVED",
    }


def generation_loose_windows_vacuum_relative():
    """[FRAMING + CANDIDATE + INDICATOR — two reframes for the protection mechanism; TWT_DEFECT_CKM_GLUON.md §13]
    Yaer's two reorientations (2026-06-26) for getting the protected-frequency mechanism right:

    ── REFRAME 1: PERCEPTION IS VACUUM-RELATIVE (perceived mass inverts absolute frequency) [FRAMING + named test] ─
    What we call ω (mass) is perceived RELATIVE to the vacuum carrier ω_vac. The defect spins SLOWER than the
    vacuum; "the slower the ABSOLUTE defect frequency, the further from ω_vac, the HIGHER we perceive its mass."
    So perceived mass = f(ω_vac − ω_abs) — a vacuum-relative READOUT — and the PROTECTED quantity is the
    **absolute** defect frequency, NOT the perceived mass. Consequence: heavier generation = SLOWER absolute =
    further below the carrier; the cost-axis (perceived) is INVERTED vs the absolute-frequency axis. **NAMED TEST
    (the hopeful handle on N16):** the 90°/120° mismatch (`cp_chirality_90_120_mismatch`) was measured in
    PERCEIVED-mass space (masses at 2πn/3 on the Brannen circle); in ABSOLUTE-frequency space the generation
    spacing may differ and become commensurate with the CP π/2 — find the perceived↔absolute map and check
    CP-commensurability. (Coheres with matter-as-defect = a HOLE: a bigger deficit below the carrier reads as more mass.)

    ── REFRAME 2: 3 WINDOWS, NOT 3 LINES — LOOSE PROTECTION [FRAMING; the window structure engine-checked] ──────
    The 3 generations may be 3 protected frequency WINDOWS (bands of finite width, like resonance/Arnold tongues)
    rather than 3 sharp lines — "loose protection." Engine-checked structure (each window = the {up-type,down-type}
    band of a generation; quark masses INDICATOR-level §5):
      gen1 [2.2, 4.7]    width(log)=0.77   up-type u at the LIGHT edge
      gen2 [93, 1270]    width(log)=2.61   up-type c at the HEAVY edge
      gen3 [4180, 172500] width(log)=3.72  up-type t at the HEAVY edge
    The windows are NON-OVERLAPPING (3 distinct bands survive), their WIDTH GROWS with generation, and the
    up-type EDGE FLIPS — at the LIGHT edge in gen-1, the HEAVY edge in gen-2,3 = the m_d>m_u inversion read as an
    edge-flip. So within each window the chirality places up/down at OPPOSITE edges (the ± reflection), and the
    edge-assignment flips at gen-1.

    ★ WHY THIS MATTERS — it RE-DESCRIBES N16 (a re-description, NOT a derivation): the within-window placement
    (up/down at the band edges; the mirror) is a BARE-band feature; IF vacuum DRESSING shifts the dressed ω into
    the window/band region (the WASH-OUT step — OWED, not shown here) it would wash out the within-band structure,
    re-describing in window language why a hadron-mass fit (dressed ω) could NOT recover the gen-2 mirror (N16/§10).
    So loose-windows COHERES WITH / re-describes the v14 negative; it does NOT derive it (the wash-out is the owed
    computation). Protection target = the bare WINDOWS + the within-window chirality edges; seek it in the bare/CKM
    cost table, not in hadron masses.

    Tiers: FRAMING (both reframes); INDICATOR (the window widths/edges = masses re-expressed §5); CANDIDATE (loose
    protection; vacuum-relative perception); NOT DERIVED. The vacuum-relative map + the CP-commensurability test are
    the OWED next computations.
    self-check: 3 non-overlapping windows; widths grow with generation; the up-type edge flips (gen-1 light, gen-2/3 heavy)."""
    import math
    UP = {"u", "c", "t"}
    # each generation's window = its {up-type, down-type} band; masses INDICATOR-level (§5)
    win = {1: {"u": 2.16, "d": 4.67}, 2: {"s": 93.4, "c": 1270.0}, 3: {"b": 4180.0, "t": 172500.0}}
    bands, up_at_light = [], []
    for g in (1, 2, 3):
        pair = win[g]; lo, hi = min(pair.values()), max(pair.values())
        up_f = [f for f in pair if f in UP][0]; dn_f = [f for f in pair if f not in UP][0]
        bands.append((lo, hi, math.log(hi / lo)))
        up_at_light.append(pair[up_f] < pair[dn_f])
    non_overlap = bands[0][1] < bands[1][0] and bands[1][1] < bands[2][0]
    widths = [b[2] for b in bands]
    widths_grow = widths[0] < widths[1] < widths[2]
    edge_flip = up_at_light == [True, False, False]              # gen-1 up light, gen-2/3 up heavy = m_d>m_u inversion
    assert non_overlap and widths_grow and edge_flip
    return {
        "reframe1_vacuum_relative": "perceived mass = vacuum-RELATIVE readout f(ω_vac−ω_abs); the PROTECTED quantity is the "
                                    "ABSOLUTE defect frequency (heavier=slower-absolute=further from carrier); cost-axis inverts. "
                                    "NAMED TEST: does the absolute-frequency map make generations CP-commensurate (resolve the N16 90/120 mismatch)?",
        "reframe2_loose_windows": {"windows": {f"gen{g}": [round(b[0], 1), round(b[1], 1)] for g, b in zip((1, 2, 3), bands)},
                                   "widths_log": [round(w, 2) for w in widths], "non_overlapping": non_overlap,
                                   "widths_grow_with_gen": widths_grow,
                                   "up_edge_flip": "up-type at LIGHT edge gen-1, HEAVY edge gen-2/3 (= the m_d>m_u inversion as an edge-flip)"},
        "reframes_N16_re_description_NOT_derivation": "the within-window up/down EDGE placement (the mirror) is a BARE-band feature; IF "
                        "vacuum DRESSING shifts the dressed ω into the band region (the wash-out step — OWED, not shown), it would wash out the "
                        "within-band structure -> RE-DESCRIBES in window language why a hadron fit (dressed ω) cannot recover the mirror (N16/§10). "
                        "Coheres with / re-describes N16; does NOT derive it.",
        "protection_target": "the bare WINDOWS (loose protection) + the within-window chirality EDGES; seek in the bare/CKM cost table, NOT hadron masses",
        "owed": "(1) the perceived<->absolute (vacuum-relative) map; (2) check CP-commensurability of the ABSOLUTE frequencies (the N16 re-attack)",
        "tier": "FRAMING (both reframes) + INDICATOR (window widths/edges = masses re-expressed §5) + CANDIDATE (loose protection; vacuum-relative); NOT DERIVED",
    }


def charge_in_the_window_picture():
    """[FRAMING + CANDIDATE + a small engine-checked NEGATIVE — Yaer's charge question; TWT_DEFECT_CKM_GLUON.md §14]
    Yaer (2026-06-26): what is CHARGE in the defect/circular-polarization/windows picture, and could a
    CHARGE-DEPENDENT generation window REDUCE the band width?

    ── WHAT CHARGE IS ─────────────────────────────────────────────────────────────────────────────────
    Charge: the topological winding supplies PROTECTION (`pi3_S3_integer_completion` — B ∈ ℤ, a discrete
    lattice and its drift protection); the per-state VALUES come from `charge_assignment_from_anchor`
    (entered anchor + composition, riding P4–P7) — never from GMN. Structurally Q = T₃ + Y/2.
    For the quarks Q_u=+2/3, Q_d=−1/3 = **+1/6 ± 1/2**: the up/down DIFFERENCE is the weak-isospin **T₃ = ±1/2
    (SYMMETRIC)** — *posited as* the self-dual SU(2)₊ doublet (N4, CANDIDATE) — and the **+1/6 hypercharge (Y/2)
    is COMMON** to both.
    So charge is DISTINCT from the ±90° circular-polarization handedness (the central E/U(1) where charge lives
    is chirality-blind), though LINKED (weak isospin = self-dual SU(2)₊). KEY: the up/down charge difference is
    SYMMETRIC (±T₃), consistent with the symmetric gen-2 mirror — and therefore it does NOT source the mirror's
    tiny residual asymmetry (0.441 vs 0.435).

    ── COULD A CHARGE-DEPENDENT WINDOW REDUCE THE WIDTH? — the decisive engine fact ─────────────────────
    The band WIDTH (the within-generation up/down split) GROWS with generation: 0.77, 2.61, 3.72 (log). But the
    charge DIFFERENCE (T₃ = ±1/2, so ΔT₃ = 1) is CONSTANT across generations. ⇒ a FIXED charge-shift CANNOT be
    the band width (a constant shift would give a CONSTANT width). So: **charge-dependent windows CAN reduce the
    per-window width — reattributing the up/down split to a charge-SEPARATION, leaving narrow per-charge bands
    (tighter protection) — BUT ONLY IF the charge coupling is MULTIPLICATIVE / frequency-scaled** (it must grow
    with the generation frequency). A multiplicative form is suggestive (up/down cost RATIO ≈ 2 ≈ |Q_u/Q_d| at
    gen 1↔2 = the cost-doubling) but BREAKS at 2↔3 (ratio 1.29). [CANDIDATE]

    ── A CLEAN SMALL NEGATIVE (engine-checked) ─────────────────────────────────────────────────────────
    The inter-generation cost is NOT proportional to |Q| (additive charge-scaling): cost(1↔2)/|Q| = lepton 5.33
    (|Q|=1), up 9.57 (|Q|=2/3), down 9.00 (|Q|=1/3) — leptons sit far below the quarks. So a simple cost∝|Q| is
    refuted; if charge sets the width it is not via this scaling.

    Tier: FRAMING (charge = winding/T₃, distinct-but-linked to chirality; charge-window reduces width only if
    multiplicative) + CANDIDATE (the frequency-scaled charge coupling) + a checked NEGATIVE (cost ∝ |Q| fails).
    Quark masses INDICATOR-level (§5). NOT DERIVED.
    self-check: Q=T₃+Y/2 decomposition (±1/2 symmetric, +1/6 common); width grows while ΔT₃ constant; cost not ∝ |Q|."""
    import math
    Qu, Qd = 2.0 / 3.0, -1.0 / 3.0
    Y_half = (Qu + Qd) / 2.0          # common hypercharge/2 = +1/6
    T3 = (Qu - Qd) / 2.0              # up/down weak isospin = +1/2 (symmetric)
    assert abs(Y_half - 1.0 / 6.0) < 1e-12 and abs(T3 - 0.5) < 1e-12
    widths = [math.log(4.67 / 2.16), math.log(1270.0 / 93.4), math.log(172500.0 / 4180.0)]  # 0.77, 2.61, 3.72
    width_grows = widths[0] < widths[1] < widths[2]
    dT3_constant = True              # ΔT3 = 1 for every generation (up-type T3=+1/2, down-type T3=-1/2)
    assert width_grows and dT3_constant   # growing width + constant charge-diff => no FIXED charge-shift can set it
    # cost ∝ |Q| test (additive scaling): leptons (|Q|=1) vs quarks
    cQ = {"lepton": (5.33, 1.0), "up": (6.38, 2.0 / 3.0), "down": (3.00, 1.0 / 3.0)}
    per_Q = {t: c / q for t, (c, q) in cQ.items()}
    cost_prop_Q_fails = per_Q["lepton"] < 0.75 * min(per_Q["up"], per_Q["down"])   # leptons far below quarks
    assert cost_prop_Q_fails
    return {
        "what_is_charge": "the topological winding supplies PROTECTION (pi3_S3_integer_completion: B in Z, no unit, no sign, no value); the per-state VALUES are ASSIGNED (charge_assignment_from_anchor: entered anchor + composition, riding P4-P7) — never from GMN. Corrected 2026-08-21 (keeper R2, the RV-7 shape): this string asserted a provenance the main engine disclaims. Q = T3 + Y/2 = +1/6 ± 1/2 for the quarks — up/down differ by the "
                          "SYMMETRIC weak-isospin T3=±1/2 (self-dual SU(2)+, N4 U1 LOCATED: CKM arc 2026-06-23 + parity exclusion 2026-06-28), common Y/2=+1/6; distinct from (but linked to) the CP handedness",
        "charge_diff_is_symmetric": {"Y/2_common": round(Y_half, 4), "T3_updown": round(T3, 4),
                                     "implication": "symmetric (±T3) -> consistent with the symmetric mirror; does NOT source the mirror's residual asymmetry"},
        "width_question_answer": "charge-dependent windows CAN reduce the per-window width (split -> charge-separation, narrow per-charge bands) "
                                 "BUT ONLY IF the charge coupling is MULTIPLICATIVE/frequency-scaled: the width GROWS (0.77/2.61/3.72) while ΔT3 is "
                                 "CONSTANT (=1), so a FIXED charge-shift gives constant width and cannot do it",
        "multiplicative_hint": "up/down cost RATIO ≈ 2 ≈ |Q_u/Q_d| at gen 1↔2 (the cost-doubling); BREAKS at 2↔3 (ratio 1.29) — CANDIDATE",
        "negative_cost_not_prop_Q": {"cost(1-2)/|Q|": {t: round(v, 2) for t, v in per_Q.items()},
                                     "verdict": "cost ∝ |Q| (additive) REFUTED — leptons (|Q|=1) give 5.33 vs quarks ~9"},
        "tier": "FRAMING (charge=winding/T3, distinct-but-linked to chirality) + CANDIDATE (multiplicative/frequency-scaled charge coupling) + "
                "checked NEGATIVE (cost ∝ |Q| fails); quark masses INDICATOR §5; NOT DERIVED",
    }


def vacuum_relative_map_and_cp_commensurability():
    """[FRAMING + clean NEGATIVE + a RESOLVED located-gap — the two owed computations of §13; TWT_DEFECT_CKM_GLUON.md §15]
    Yaer asked to DO the two computations owed from the vacuum-relative reframe (§13):
      (C1) the perceived↔absolute map; (C2) the CP-commensurability check in absolute-frequency space (the N16 handle).

    ── C1: the perceived↔absolute map = a MONOTONIC FRAME TRANSFORM (clean NEGATIVE on it being a structural key) ──
    Matter = a HOLE/beat below the carrier ω_vac (the radio/heterodyne picture Yaer used): perceived mass = the
    deficit/beat = ω_vac − ω_abs, so ω_abs = ω_vac − m. The physical carrier scale is the grain cutoff Λ ~ M_Pl.
    Then for EVERY SM defect m/Λ ≲ 1e-16 (top ~1.4e-17) down to ~1e-23 (electron) ⇒ **ω_abs ≈ Λ for all** (the
    absolute frequencies are all the carrier minus a part-in-1e17 deficit). The entire generation HIERARCHY (~1e5 in
    mass) lives ENTIRELY in the tiny DEFICIT (= the perceived mass), NOT in ω_abs. So the perceived↔absolute map is a
    **monotonic frame transform that adds NO new generation structure** (the ratio map ω_abs=Λ/(1+m/Λ) gives the
    same). **Scope (reviewer):** the INERTNESS (no new structure) is CARRIER-INDEPENDENT — ω_abs=ω_vac−m is strictly
    monotonic in m for ANY carrier, and a monotonic relabeling cannot manufacture ordinal/clustering structure; the
    ω_abs≈Λ COMPRESSION is the Planckian-carrier statement (Λ substrate-mandated, canon §0, not a fit). The reframe
    is ONTOLOGICALLY correct (mass = the beat/deficit below the carrier, matter-as-hole) but **structurally inert**.

    ── C2: the 90°/120° mismatch is a BRANNEN-CIRCLE ARTIFACT — N16's located gap RESOLVED ─────────────────────
    A monotonic map preserves the 3-fold (generations) vs 2-fold (CP handedness) count — gcd(2,3)=1 — so the map
    CANNOT fix the incommensurability. BUT the mismatch is an ARTIFACT of the BRANNEN CIRCLE: on a 3-fold circle
    the generations are forced to 2π/3 (120°) spacing, and a CP π/2 shift is 3/4 of a step → scrambles (Lens A;
    the free fit drove the CP phase→0). On the **LOG-FREQUENCY LINE** (the cost axis — the natural variable in the
    vacuum-relative/cost picture), the generations sit on a geometric LADDER (s·(n−1)), NOT a circle, and the ±90°
    chirality is a SMALL non-scrambling modulation — which is exactly why **Lens C/D (ladder-based, FIXED ±π/2) fit
    at 3.68% while only Lens A (circle-based) scrambled** (archive mass_formula_v14.py). ⇒ **abandoning the Brannen
    circle — which Yaer's reframes (Brannen-is-a-parameterization §7; windows §11; cost-line §9a) already mandate —
    DISSOLVES N16's 90°/120° located gap.** The CP π/2 then just labels the two towers (up/down handedness) on the
    line; no commensurability with a generation-circle spacing is required. (N16's MAIN negative — the mirror is
    bare-sector, hadrons can't probe it — is UNTOUCHED and stands.)
    ★ CONFIRMED (reviewer-reproduced): on the ladder the ±π/2 is genuinely LOAD-BEARING (NOT inert) — removing the
    chirality (χ→0, up=down) collapses the FORM-B fit 3.68%→26.5%; the ±π/2 supplies the ENTIRE within-generation
    up/down split (ln-freq splits 0.06/1.18/−1.24 across the 3 gens). So the CP π/2 WORKS on the line (it labels the
    towers); the "free fit drove the CP phase→0" was the CIRCLE (Lens A) diagnostic only, not the line. (NB: the
    archive implements two FORMS — A=circle, B=ladder; "Lens C/D" are the ladder-side twists folded into FORM-B.)

    Tier: FRAMING (the map = a frame transform; the circle-artifact resolution, grounded in the v14 fits) + clean
    NEGATIVE (the absolute axis reveals no new structure) + RESOLVED located-gap (N16 90/120, downgraded to a
    Brannen-circle artifact). The fit evidence is FIT/ILLUSTRATIVE (archive). NOT DERIVED.
    self-check: m/Λ ≪ 1 for all SM (ω_abs≈Λ, map inert); the 90/120 = 3/4 lives on the CIRCLE; gcd(2,3)=1."""
    import math
    Lam = 1.22e19 * 1e3                                  # M_Pl in MeV (~1.22e22)
    m_max, m_min = 172500.0, 0.5109989                  # top, electron
    assert m_max / Lam < 1e-10 and m_min / Lam < 1e-10  # C1: deficits tiny -> omega_abs ≈ Lambda -> map inert
    circle_mismatch = (math.pi / 2.0) / (2.0 * math.pi / 3.0)
    assert abs(circle_mismatch - 0.75) < 1e-12          # the 90/120 = 3/4 mismatch lives on the CIRCLE
    assert math.gcd(2, 3) == 1                          # 3 generations vs 2 CP handedness are coprime (monotonic map can't fix)
    return {
        "C1_map": "perceived mass = the beat/deficit below the carrier: ω_abs = ω_vac − m (matter-as-hole/heterodyne). With ω_vac = Λ~M_Pl, "
                  "m/Λ ≲ 1e-17 for ALL SM defects ⇒ ω_abs ≈ Λ; the whole hierarchy is in the tiny DEFICIT (= perceived mass), not in ω_abs",
        "C1_verdict": "the perceived↔absolute map is a MONOTONIC FRAME TRANSFORM — ontologically correct (mass = deficit below the carrier) "
                      "but STRUCTURALLY INERT: it adds NO new generation structure (clean NEGATIVE on the absolute axis being a structural key)",
        "C2_circle_artifact": {"on_BRANNEN_CIRCLE": "generations forced to 120° (2π/3); CP π/2 = 3/4 of a step -> scrambles (Lens A, fit drove CP phase->0)",
                               "on_LOG_FREQUENCY_LINE": "generations on a geometric LADDER s·(n−1); ±90° chirality = a small non-scrambling modulation -> "
                                                        "Lens C/D fit 3.68% with FIXED ±π/2 (archive mass_formula_v14.py)",
                               "gcd(2_handedness, 3_generations)": math.gcd(2, 3)},
        "C2_verdict": "N16's 90°/120° located gap is RESOLVED — it is a BRANNEN-CIRCLE artifact; on the log-frequency LINE (the vacuum-relative/cost "
                      "variable the reframes already mandate) it DISSOLVES (the CP π/2 just labels the up/down towers; no circle-commensurability needed). "
                      "N16's MAIN negative (mirror = bare-sector, hadrons can't probe it) STANDS.",
        "net": "the vacuum-relative reframe is ontologically right but structurally inert as a MAP (C1); its real payoff is reorienting from the "
               "Brannen CIRCLE to the cost LINE, which DISSOLVES the 90/120 gap (C2). Owed-no-more: the 90/120 handle is closed; the open frontier is "
               "the bare-sector protection mechanism (the windows + chirality edges on the cost line) — the #1 gap.",
        "tier": "FRAMING + clean NEGATIVE (map inert) + RESOLVED located-gap (N16 90/120 = Brannen-circle artifact); fit evidence FIT/ILLUSTRATIVE; NOT DERIVED",
    }


def generation_ladder_needs_inverse_square():
    """[clean-NEGATIVE + DERIVED sub-result + FRAMING — N20, the re-attack-hinge attack; TWT_DEFECT_CKM_GLUON.md §17]
    Pursuing the N19 hinge ("is the backbone ω(amplitude) exponential, making the geometric cost ladder?") via 4
    substrate routes (discrete-scale-invariance / Hopf-closing action / driven-pendulum backbone / adversarial) +
    independent developer verification. Outcome: a clean NEGATIVE on the discrete-scale-invariance prime hypothesis,
    ONE new DERIVED sub-result, and a strictly sharper hinge. NOTHING DERIVED for the cost table.

    NOTE (coordinate, N20–N22): the radial coordinate r/R of the −1/r² channel is the soliton-SIZE = breathing-mode
    collective MODULUS (whose closed-orbit action is S(r); R→0 = its small-size = grain limit) — NOT the *static*
    soliton radius of the √m=r²⇒ω=r⁴ mass map (that enters only the cost=4·ln(r-gap) tautology), and NOT the phase θ.

    ── ★ THE RIGOROUS REDUCTION (FRAMING, the sharper WHERE) ───────────────────────────────────────────
    A GEOMETRIC radius ladder r_n = r₀·qⁿ (which the cost table needs — N19) requires a LOGARITHMIC closed-orbit
    action S(r) ∝ ln(r) (then Bohr-Sommerfeld S=2πn ⇒ r_n geometric), EQUIVALENTLY an attractive scale-invariant
    **−1/r² effective radial potential** with coefficient below the Efimov/Breitenlohner-Freedman critical −1/4
    (complex index ±i·s₀, log-periodic spectrum, ratio e^{π/s₀}). This sharpens N19's "is ω(A) exponential?" to the
    fundamental "does the defect's radial action carry a −1/r² scale-invariant channel?".

    ── ★ THE CLEAN NEGATIVE (4-route + independent convergence — over-determined) ───────────────────────
    The substrate does NOT force the geometric ladder; the −1/r² generator is ABSENT:
      • every single-soliton action term is degree ±1/±3 power-law or rational (Derrick breathing c₂r+c₄/r;
        rotational L²/2Θ ∼ 1/r or 1/r³; Hopf-closing rᵏ=p/q; Arnold/Farey staircase) — NEVER degree −2. Power-law
        action ⇒ Bohr-Sommerfeld r_n ∼ n^{1/k} = ARITHMETIC, ratios → 1 (engine: S∼r⁵ → 1.15/1.08/1.06, shrinking).
      • the Derrick breathing well is a STABLE HARMONIC minimum: V=c₂r+c₄/r ⇒ V''(r*) = 2c₂^{3/2}/√c₄ > 0
        (sympy-exact) — **NOT scale-critical**. (This CORRECTS N17's imprecise "Derrick marginal point": the static
        breathing mode is a fixed-scale harmonic minimum; the only scale-critical Derrick regime is the chiral-limit
        CONTINUUM = N17's no-discrete-tower. The Skyrme quartic IS d=4-scale-marginal, but its static fluctuation
        index is REAL — the σ 2-derivative term pins the 1/r² coefficient above −1/4, no Efimov.)
      • a single discrete-scale-invariant tower has a CONSTANT ratio (self-similar = constant cost/rung); the DATA is
        NOT within-tower self-similar — radius ratios DRIFT down +22% / up −31% / lepton −47% (the drift SIGN = the
        up↔down chirality mirror). So a constant-q ladder is excluded by the data itself, before any mechanism.
      • the Efimov 3-boson s₀=1.006 (ratio 22.7, cost 3.12) is a one-rung 4%-off coincidence at down 1→2 that FAILS
        all 5 other rungs (per-rung s₀ spans 0.49–1.11); REJECTED as numerology.

    ── ★ THE DERIVED SUB-RESULT — the driven-pendulum backbone (answers the N19 hinge) ──────────────────
    The meta-time collective backbone IS the driven pendulum: Λθ̈ = −K sinθ (Λ from `gear_eigenvalues`; the −K cosθ
    carrier lock = the lowest e4-harmonic), ω(A) exact. The SEPARATRIX (E=K) = the chirality boundary (libration =
    co-rotating bound defect, rotation = counter-rotation over the top = SD↔ASD, ties to `chirality_is_a_reflection`).
    The separatrix divergence is **LOGARITHMIC** (ω ∼ π/ln(32/ε)) ⇒ the cost ladder RISES toward it (the right
    trend-sign, unlike every arithmetic ladder of N19 which shrinks) but the gaps **CROWD**: a SINGLE gap is
    UNBOUNDED (one rung tuned to straddle the separatrix can exceed any value), but consecutive gaps collapse — the
    best min-of-two-adjacent-gaps at Maslov-½ quantization is **≈1.2** (grid-sampling-sensitive ~1.0–1.25 — it
    samples a near-singular structure); the SUPREMUM over all level placements (scanning ℏ and the phase offset) is
    **≲2.0**, in every case **< 2.8** (the band floor, factor ~1.4). The cost table needs a RUN of consecutive band
    gaps (down 3.00 THEN 3.80; up 6.38 THEN 4.91), which the logarithmic backbone structurally cannot supply. So
    "is ω(A) exponential?" = clean NO (logarithmic crowds; cannot make a run of [2.8,6.4] gaps).

    ── O(2-5) RADIUS-RATIO "NATURALNESS" = TAUTOLOGY (down-tier of the N16/N19 framing) ─────────────────
    cost = 4·ln(r-gap) is the INVERSE r⁴ of the banked √m=r²⇒ω=r⁴, so ANY cost in the empirical [2.8,6.4] maps to
    r∈[2,5] BY CONSTRUCTION. The tameness is a property of the log-r coordinate, NOT a substrate prediction that the
    radii sit there. Real only once the substrate SETS r (#1-gap GATED).

    ── ★ THE SHARPENED HINGE (the new single sharpest computation) ─────────────────────────────────────
    PROJECT the e4-driven Skyrme quartic onto the meta-time collective coordinate to get V(θ), Λ(θ) — do **NOT**
    assume the single-harmonic pendulum — and read the **EXPONENT of the period (action) divergence** at the lock
    boundary: LOGARITHMIC (cosine barrier) ⇒ crowds ⇒ caps at ~2.2 ⇒ geometric ladder dead; POWER-LAW (a steeper
    non-cosine barrier the quartic could supply) ⇒ S(r) ∝ ln(r) = the missing −1/r² channel ⇒ SPREADS into [2.8,6.4].
    And constant-q is drift-excluded, so the within-tower drift (+22/−31/−47%, sign=chirality) needs a RUNNING rate
    (a controlled discrete-scale-invariance-BREAKING relevant operator). #1-gap §9.6-EOM-gated, same dynamics as Θ_rel/τ_mem.

    Tier: clean-NEGATIVE (DSI/geometric-ladder refuted-as-forced; generator absent; Derrick well harmonic-stable;
    pendulum cap ~2.2<2.8; data not within-tower geometric) + DERIVED sub-result (the driven-pendulum backbone,
    ω(A) exact) + FRAMING (the geometric⟺log-action⟺1/r² reduction; the N17 correction). NOT DERIVED.
    self-check: pendulum cost cap < 2.8; Derrick V''>0; within-tower drift signs +/−/−; power-law action ⇒ shrinking radii."""
    import numpy as np, sympy as sp, math
    from scipy.special import ellipk
    # (1) DERIVED sub-result: the forced driven-pendulum backbone — the gaps CROWD (logarithmic divergence).
    #     The SINGLE gap is UNBOUNDED (one rung tuned to straddle the separatrix can exceed any value), but
    #     consecutive gaps COLLAPSE: the best min-of-two-adjacent-gaps at Maslov-½ is ≈1.2; the supremum over all
    #     level placements (ℏ + phase offset) is ≲2.0 — in every case < 2.8, so NO RUN of band gaps (the cost table
    #     needs down 3.00 THEN 3.80, up 6.38 THEN 4.91) is possible. NOTE the value is grid-sampling-sensitive
    #     (~1.0–1.25 across resolutions; near-singular structure) — but the conclusion (< 2.8, factor ~1.4 below the
    #     band floor) is insensitive to it. ω floored (WKB invalid below) to keep the near-separatrix interpolation
    #     well-conditioned (else careless grids artifact); floor is hygiene only (value identical where ω is defined).
    wfl = 0.08
    El = np.sort(np.concatenate([np.linspace(-0.999, 0.9, 30000), 1 - np.logspace(-1, -12, 30000)])); El = El[(El > -1) & (El < 1)]
    Er = 1 + np.logspace(-12, 2.0, 30000)
    wl = np.maximum(np.pi / (2 * ellipk((El + 1) / 2)), wfl)
    wr = np.maximum(np.pi * np.sqrt((Er + 1) / 2) / ellipk(2 / (Er + 1)), wfl)
    Il = np.concatenate([[0], np.cumsum(np.diff(El) / ((wl[1:] + wl[:-1]) / 2))]); Isep = Il[-1]
    Ir = Isep + np.concatenate([[0], np.cumsum(np.diff(Er) / ((wr[1:] + wr[:-1]) / 2))])
    Ia = np.concatenate([Il, Ir]); wa = np.concatenate([wl, wr])
    pair_min = 0.0
    for hb in np.linspace(0.02, 3.0, 600):
        N = int(Ia[-1] / hb)
        if N < 3: continue
        Ilv = (np.arange(N) + 0.5) * hb; Ilv = Ilv[(Ilv > 0) & (Ilv <= Ia[-1])]
        if len(Ilv) < 3: continue
        c = np.abs(np.diff(np.log(np.interp(Ilv, Ia, wa))))    # consecutive cost-gaps
        pm = np.minimum(c[:-1], c[1:])                         # min of each ADJACENT pair
        pair_min = max(pair_min, float(pm.max()))
    assert pair_min < 1.8                                     # CROWDS: Maslov-½ pair-min ~1.2 (sup over placements ≲2.0) < 2.8, no run of band gaps
    # (2) Derrick breathing well is a STABLE harmonic minimum (V''>0), not scale-critical — corrects N17
    r, c2, c4 = sp.symbols('r c2 c4', positive=True)
    Vpp = sp.simplify(sp.diff(c2 * r + c4 / r, r, 2).subs(r, sp.sqrt(c4) / sp.sqrt(c2)))
    assert Vpp == 2 * c2**sp.Rational(3, 2) / sp.sqrt(c4)   # = 2 c2^{3/2}/sqrt(c4) > 0
    # (3) within-tower radius-ratio drift: sign = chirality (down +, up −, lepton −) ⇒ not within-tower geometric
    tw = {'down': [3.00, 3.80], 'up': [6.38, 4.91], 'lepton': [5.33, 2.82]}
    drift = {t: (math.exp(cs[1] / 4) - math.exp(cs[0] / 4)) / math.exp(cs[0] / 4) for t, cs in tw.items()}
    assert drift['down'] > 0 and drift['up'] < 0 and drift['lepton'] < 0   # NOT self-similar; sign = up↔down mirror
    # (4) power-law action S~r^k ⇒ Bohr-Sommerfeld r_n ~ n^{1/k} ⇒ shrinking (arithmetic), not geometric
    rn = [n**(1 / 5) for n in (1, 2, 3, 4)]; ratios = [rn[i + 1] / rn[i] for i in range(3)]
    assert ratios[0] > ratios[1] > ratios[2] > 1.0 and ratios[0] < 1.3   # shrink toward 1
    return {
        "verdict": "clean-NEGATIVE on discrete-scale-invariance/geometric-ladder-as-forced (4-route + independent convergence); "
                   "ONE DERIVED sub-result (driven-pendulum backbone); a sharper hinge. NOT DERIVED for the cost table.",
        "reduction_FRAMING": "geometric radius ladder ⟺ logarithmic closed-orbit action S(r)∝ln(r) ⟺ attractive scale-invariant −1/r² radial channel (coeff < −1/4)",
        "generator_absent": "no single-soliton action term is degree −2; every term is ±1/±3 power-law or rational ⇒ Bohr-Sommerfeld radii ARITHMETIC (S~r⁵ → 1.15/1.08/1.06, shrinking)",
        "N17_correction": "the Derrick breathing well is a STABLE HARMONIC minimum (V''(r*)=2c₂^{3/2}/√c₄ > 0), NOT scale-critical — corrects N17's imprecise 'marginal point'; the only critical Derrick regime is the chiral-limit CONTINUUM",
        "derived_pendulum_backbone": {"eom": "Λθ̈=−K sinθ (gear inertia + lowest e4-harmonic lock)",
                                      "separatrix_is_chirality": "libration=co-rotating vs rotation=counter-rotation = SD/ASD",
                                      "divergence": "LOGARITHMIC ⇒ cost RISES toward separatrix (right trend) but gaps CROWD",
                                      "single_gap": "UNBOUNDED (one rung straddling the separatrix)",
                                      "best_adjacent_pair_min_maslov": round(pair_min, 2), "sup_over_placements": "≲2.0", "band_floor": 2.8,
                                      "pair_min_note": "Maslov-½ value grid-sampling-sensitive ~1.0–1.25 (near-singular structure); sup over all level placements ≲2.0; in every case < 2.8 (factor ~1.4), conclusion insensitive to the value",
                                      "N19_hinge_answered": "'is ω(A) exponential?' = NO, it is logarithmic ⇒ gaps CROWD (pair-min ~1.2, sup ≲2.0, < 2.8) ⇒ cannot make a RUN of band gaps"},
        "data_not_within_tower_geometric": {t: round(d, 2) for t, d in drift.items()},
        "naturalness_is_tautology": "O(2-5) radius ratios = the data re-expressed through the banked r⁴ map (cost=4 ln r is the inverse of ω=r⁴), NOT a substrate prediction; real only once the substrate sets r (gated)",
        "efimov_numerology_rejected": "s₀=1.006 (ratio 22.7, cost 3.12) is a one-rung 4%-off coincidence; fails 5/6 rungs (per-rung s₀ 0.49–1.11) and within-tower self-similarity",
        "sharper_hinge": "PROJECT the e4-driven Skyrme quartic → V(θ),Λ(θ) (do NOT assume the pendulum); read the period-divergence EXPONENT: "
                         "log=crowds=dead, power-law=the missing 1/r² channel=spreads into [2.8,6.4]; constant-q drift-excluded ⇒ needs a RUNNING rate (a DSI-breaking relevant operator)",
        "tier": "clean-NEGATIVE + DERIVED sub-result (pendulum backbone: gaps CROWD, pair-min ~%.1f, sup over placements ≲2.0 < 2.8) + FRAMING (the 1/r² reduction; N17 correction); located-gap N20; NOT DERIVED" % pair_min,
    }


def geometric_ladder_is_nonselfadjoint():
    """[REFUTATION + RELOCATION + CONDITIONAL + DERIVED sub-results + FRAMING — N21; TWT_DEFECT_CKM_GLUON.md §18]
    Testing whether the geometric cost ladder is NECESSARILY non-Hermitian/dissipative (a 3-route workflow +
    independent developer verification + twt-reviewer, sympy/Weyl-exact). Outcome: the strong "necessarily DISSIPATIVE"
    claim is REFUTED; and (reviewer-corrected from an over-claimed clean-negative) the conservative-sector question
    RELOCATES to the R→0 (grain-scale) endpoint — UNSETTLED, not a clean negative. NOT DERIVED for the cost table.

    ── ★ THE REFUTATION (do not over-claim "dissipative") ──────────────────────────────────────────────
    Efimov / Calogero physics is a CONSERVATIVE, HERMITIAN geometric ladder: H = −∂² − g/r² with g>1/4 is real and
    time-reversal-even (no Im χ), yet log-periodic (ratio e^{π/s₀}, s₀=√(g−1/4)), via a self-adjoint EXTENSION / a
    3-body UV anchor. So the geometric ladder is NOT intrinsically dissipative. (Russian-doll cyclic RG is NOT a
    counterexample — it needs an explicit non-Hermitian coupling g+ih.)

    ── ★ THE AIRTIGHT REPLACEMENT (the dichotomy is self-adjoint, not Hermitian-vs-dissipative) ─────────
    geometric radius ladder ⟺ attractive scale-invariant **−g/r² with g>1/4** (Breitenlohner-Freedman / fall-to-the-
    center) ⟺ a **NON-SELF-ADJOINT** radial channel (complex index ±i·s₀, log-periodic). [The honest dichotomy is
    SELF-ADJOINT (arithmetic, no ladder) vs NON-SELF-ADJOINT (ladder) — NOT Hermitian vs dissipative.]

    ── DERIVED sub-results — the BULK (large-R) conservative spectrum is arithmetic (engine/sympy-exact) ─
    (a) CRANKED no R⁻²: conservative cranking at fixed L adds L²/(2Λ(R)) with the inertia's mixed Derrick scaling
        Λ=aR³+bR (σ-term volume R³, Skyrme-term length R¹; the meta-time/e5 global-phase generator gives R³, not R²),
        expanding as {R⁻¹, R⁻³} — NEVER scale-invariant R⁻² in the bulk, always + (repulsive).
    (b) the LAPLACE-BELTRAMI (geometrically-natural) kinetic measure induces NO quantum potential (1D is flat), Q=0.
        So the bulk/large-R collective spectrum is arithmetic — the ladder is NOT a bulk phenomenon.

    ── ★ THE RESULT IS A RELOCATION TO THE R→0 (small-defect = GRAIN-scale) ENDPOINT, NOT a clean negative ─
    Whether the conservative collective sector CAN make the ladder is UNSETTLED and reduces entirely to the R→0
    endpoint, via two facts (both reviewer-forced, sympy/Weyl-verified — they CORRECT an earlier over-claim that the
    sector "cannot, class-wide"):
      • LIMIT-CIRCLE at R=0: the bare PDM operator (even with the Skyrme c₄/R wall) is LIMIT-CIRCLE at R=0 — the
        wall (degree −1) is too SOFT to dominate the 3/(4R²) essential-self-adjointness threshold — so the operator
        is **NOT essentially self-adjoint**; it carries a Calogero-like 1-parameter boundary/self-adjoint-EXTENSION
        freedom at R→0 (exactly the freedom a conservative Efimov ladder uses). "Bounded-below ⇒ e.s.a. ⇒ arithmetic"
        is therefore NOT a theorem here.
      • The R→0 1/r² coefficient is ORDERING-DEPENDENT (von Roos) and SPANS the BF threshold: +α(α−1) REPULSIVE
        (symmetric, +0.19→+0.39), −n(n+4)/(8(n+2)²) SUB-critical (one attractive ordering, →1/8), and
        −n(3n+4)/(8(n+2)²) SUPER-critical (divergence/Zhu-Kroemer form, s<−1/8 for n≥2). So the measure CAN be
        supercritical — the sector's ladder question is genuinely open, fixed by (i) which ordering is physical and
        (ii) the self-adjoint-extension parameter at R→0.
    Both (i) and (ii) are R→0 = small-defect = the Planckian GRAIN-scale UV (where the coarse soliton description
    fails) — so the whole cost-table question RELOCATES to the grain-scale endpoint.

    ── THE FORK (the open resolution of "dissipative?") ────────────────────────────────────────────────
    The R→0 self-adjoint-extension / net-coefficient is fixed EITHER (a) CONSERVATIVELY by grain-scale D4-lattice
    contact / 3-body physics (Efimov-on-the-lattice — a conservative geometric ladder, the extension parameter = the
    grain UV input), OR (b) by the DISSIPATIVE Im χ kernel (Fork A). Efimov shows (a) is logically available, so
    "necessarily dissipative" is FALSE; discriminating (a) vs (b) is the open question. CONDITIONAL (the honest
    headline): *given the physical ordering+extension supply no supercritical −g/r² at R→0, the ladder must be
    dissipative; otherwise it is a conservative grain-scale phenomenon.*

    ── TIE to Θ_rel (CANDIDATE) ────────────────────────────────────────────────────────────────────────
    What the R→0 anchor (conservative-UV or Im χ) must supply — the supercritical g_eff>1/4 AND a chirality-signed
    discrete-scale-invariance-BREAKING running rate ds₀/drung (the N20 within-tower drift +22/−31/−47%, sign = the
    up↔down SD/ASD mirror) — are coset-Cartan / FDT-violation objects of Θ_rel's kind. A possible 5th face of the
    Θ_rel merge (the shared DSI-breaking DIRECTION = chirality is derived; the single kernel value is gated).

    ── ★ THE SHARPER HINGE ─────────────────────────────────────────────────────────────────────────────
    Compute the net R→0 (grain-scale) 1/r² coefficient for the PHYSICAL collective-coordinate ordering, and the
    self-adjoint-extension parameter — is it supercritical (g>1/4)? and is the extension fixed conservatively (D4
    grain-scale contact) or by Im χ? This is now a SMALL-DEFECT/grain-scale endpoint computation, not a bulk one.

    Tier: REFUTATION ("necessarily dissipative" is FALSE — Efimov is a conservative ladder; correct word =
    non-self-adjoint) + DERIVED (the BULK is arithmetic: cranked-no-R⁻²; LB measure Q=0) + FRAMING (the non-self-
    adjoint dichotomy; the RELOCATION to the R→0/grain endpoint) + located-gap N21 (the UNSETTLED R→0 coefficient +
    extension parameter; the conservative-grain vs dissipative-Imχ fork). NOT a clean negative; NOT DERIVED.
    self-check: cranked centrifugal has no R⁻² (bulk); the von Roos R→0 measure coefficient SPANS the BF threshold
    (repulsive symmetric > 0; divergence-form supercritical < −1/8 at n=3); the c₄/R wall is sub-threshold (soft)."""
    import sympy as sp
    R, L, a, b, n = sp.symbols('R L a b n', positive=True)
    # (a) BULK: cranked centrifugal has no scale-invariant R^-2 term (large-R spectrum arithmetic)
    cent_small = sp.series(L**2 / (2 * (a * R**3 + b * R)), R, 0, 4).removeO()
    assert cent_small.coeff(R, -2) == 0                                  # never R^-2 in the bulk
    assert cent_small.coeff(R, -1) != 0                                  # has R^-1 (repulsive), and R^-3 at large R
    # (b) R->0 ENDPOINT: the von Roos measure 1/r^2 coefficient is ORDERING-DEPENDENT and SPANS the BF threshold (g>1/4
    #     <=> the H=-d^2-g/r^2 convention s<-1/8). NOT "never supercritical" (reviewer-corrected): a divergence-form
    #     ordering IS supercritical for n>=2 -> the conservative-sector ladder question is UNSETTLED, fixed at R->0.
    s_symmetric   = (lambda k: float((-k/(2*(k+2)))*((-k/(2*(k+2)))-1)))   # +REPULSIVE (symmetric ordering)
    s_subcrit     = (lambda k: -float(k*(k+4)/(8*(k+2)**2)))               # attractive, sub-critical (sup -> -1/8)
    s_supercrit   = (lambda k: -float(k*(3*k+4)/(8*(k+2)**2)))             # attractive, SUPER-critical (divergence form)
    assert s_symmetric(3) > 0                                            # repulsive ordering exists
    assert -0.125 < s_subcrit(3) < 0                                     # a sub-critical attractive ordering exists
    assert s_supercrit(3) < -0.125                                       # a SUPER-critical attractive ordering exists (n=3): the span crosses BF
    # (c) LIMIT-CIRCLE at R->0: the Skyrme wall c4/R (degree -1) is sub-threshold vs the 3/(4R^2) e.s.a. criterion
    R0 = sp.Symbol('R0', positive=True)
    assert sp.limit((1/R0) / (sp.Rational(3, 4) / R0**2), R0, 0) == 0    # c4/R  <<  (3/4)/R^2  -> wall too soft -> limit-circle, NOT e.s.a.
    g_crit = sp.Rational(1, 4)
    return {
        "refutation": "‘geometric ladder ⇒ necessarily DISSIPATIVE’ is FALSE — Efimov/Calogero (H=−∂²−g/r², g>1/4) is a CONSERVATIVE, "
                      "HERMITIAN, log-periodic ladder via a self-adjoint extension / 3-body UV anchor; no Im χ needed",
        "dichotomy": "geometric ladder ⟺ attractive −g/r² (g>1/4, BF/fall-to-center) ⟺ a NON-SELF-ADJOINT radial channel "
                     "(the honest dichotomy is self-adjoint vs non-self-adjoint, NOT Hermitian vs dissipative)",
        "g_critical": float(g_crit),
        "bulk_is_arithmetic": "cranked centrifugal L²/(2(aR³+bR)) = {R⁻¹,R⁻³}, never R⁻² (meta-time/e5 generator gives R³); Laplace-Beltrami measure Q=0 (1D flat) "
                              "⇒ the large-R collective spectrum is arithmetic; the ladder is NOT a bulk phenomenon",
        "relocation_to_R0_monad_endpoint": {
            "limit_circle": "the bare PDM operator (even with the soft c₄/R wall) is LIMIT-CIRCLE at R=0 ⇒ NOT essentially self-adjoint ⇒ "
                            "it carries a Calogero-like self-adjoint-EXTENSION (boundary) freedom at R→0 — so ‘bounded-below ⇒ e.s.a. ⇒ arithmetic’ is NOT a theorem here",
            "measure_coeff_spans_BF": {"symmetric": round(s_symmetric(3), 3), "sub_critical": round(s_subcrit(3), 3), "super_critical": round(s_supercrit(3), 3),
                                        "note": "von Roos ORDERING-DEPENDENT, SPANS the BF threshold s=−1/8 (repulsive +0.39, sub −0.105, SUPER −0.195 at n=3) — the measure CAN be supercritical"},
            "verdict": "UNSETTLED, not a clean negative: whether the conservative collective sector makes the ladder reduces to the R→0 (small-defect=MONAD-scale) "
                       "endpoint — (i) the physical ordering's net 1/r² coefficient (spans sub/super) and (ii) the self-adjoint-extension parameter"},
        "fork": "the R→0 extension/coefficient is fixed EITHER (a) CONSERVATIVELY by monad-scale D4-lattice contact/3-body physics (Efimov-on-lattice — the Planckian "
                "MONAD scale), OR (b) by the DISSIPATIVE Im χ kernel (Fork A). Efimov makes (a) logically available ⇒ ‘necessarily dissipative’ is FALSE; the fork is open",
        "conditional": "GIVEN the physical ordering+extension supply no supercritical −g/r² at R→0 ⇒ the ladder must be dissipative; OTHERWISE it is a conservative monad-scale phenomenon",
        "ties_to_theta_rel": "CANDIDATE: the R→0 anchor must supply g_eff>1/4 + a chirality-signed DSI-breaking running rate (the N20 within-tower drift, sign=SD/ASD mirror) "
                             "— coset-Cartan/FDT-violation objects of Θ_rel's kind; a possible 5th face (shared DSI-breaking DIRECTION derived; kernel value gated)",
        "sharper_hinge": "compute the net R→0 (monad-scale) 1/r² coefficient for the PHYSICAL collective-coordinate ordering + the self-adjoint-extension parameter — "
                         "supercritical (g>1/4)? and is the extension fixed conservatively (D4 monad contact) or by Im χ? a SMALL-DEFECT endpoint computation",
        "tier": "REFUTATION (‘necessarily dissipative’ is false) + DERIVED (the BULK is arithmetic: cranked-no-R⁻²; LB measure Q=0) + FRAMING (non-self-adjoint dichotomy; "
                "the RELOCATION to the R→0/monad endpoint) + located-gap N21 (the UNSETTLED R→0 coefficient + extension; conservative-monad vs dissipative-Imχ fork); NOT a clean negative, NOT DERIVED",
    }


def _a1_dirs():
    """Helper: the probes' 14-direction unit set (6 axes + 8 cube diagonals)."""
    import math as _m
    out = []
    for v in ([1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1],
              [1, 1, 1], [1, 1, -1], [1, -1, 1], [-1, 1, 1],
              [-1, -1, 1], [-1, 1, -1], [1, -1, -1], [-1, -1, -1]):
        nn = _m.sqrt(v[0] ** 2 + v[1] ** 2 + v[2] ** 2)
        out.append((v[0] / nn, v[1] / nn, v[2] / nn))
    return out


def lambda_perp_anw_half_theta():
    """[DERIVED-A given the frozen-profile (rigid-rotor) ansatz] The
    perpendicular internal-rotation response Lambda_perp of a carrier-matched
    hedgehog IS the ANW isorotation moment — banked per ADJUDICATION2_2026-08-03
    item 1 (P4-A, stronger than claimed). Configuration: R = A(x4) R_h A(x4)~ q_c,
    A = exp(u_p dk x4/2) with u_p PERPENDICULAR to the carrier axis u_c;
    E_extra = Lambda_perp * dk^2 (exact quadraticity: ADJUDICATION_2026-08-03
    item 5, licence re-checked here at two dk a decade apart).

    FACTS (engine-checked here):
      (1) ZERO-PARAMETER CLOSED FORM: the direction+cycle-averaged shell
          density of Lambda_perp is
              (8 pi/3) r^2 sin^2 f [c2 + 4 c4 (f'^2 + sin^2 f / r^2)]
          pointwise (per radius) at the 1e-12 class (measured ~1e-15), across
          THREE profiles x TWO coupling pairs, NO FIT — both coefficients
          analytic (the probe-4 memo's least-squares was unnecessary). The
          bracket is EXACTLY the banked R-133 Theta_0 integrand structure
          (x^2 sin^2 F [1 + 4 F'^2 + 4 sin^2 F / x^2]), ANW factor-4 included.
      (2) CARRIER-INDEPENDENCE, NON-TRIVIAL: per-direction the coefficient IS
          k_c-dependent (witnessed below); it cancels ONLY on the solid-angle +
          cycle average (k_c vs 2.1 k_c agree at ~1e-15 after averaging).
      (3) Lambda_perp = (1/2) * Theta_ANW — ratio Theta_ANW/Lambda_perp =
          2.0000000000 measured, where Theta_ANW is the isorotation moment in
          the BAND CONVENTION E_rot = (1/2) Theta omega^2 that R-133's
          M(J) = M_0 + J(J+1)/(2 Theta_0) uses. The measurement chain, each
          link engine-checked: E_extra is EXACTLY quadratic in dk (licence
          below); the physical isorotation rate is omega = dk (the adjoint
          rotation angle of A(x4) = exp(u_p dk x4/2) is MEASURED on a rotated
          bivector: phi(x4) = dk*x4 to 1e-15 — the rotor half-angle doubles);
          hence Theta = 2 E/omega^2 = 2 Lambda_perp.
          THE IDENTIFICATION SENTENCE MUST CARRY THE 1/2: plugging Lambda_perp
          in as Theta makes every R-133 band spacing WRONG BY 2.
      (4) ACCURATE VALUE for the test profile pi*exp(-r), (c2, c4) = (1, 0.25):
          Lambda_perp = 32.1561 (closed-form Simpson, full range). Probe-2's
          31.4386 is REPRODUCED as the closed form on probe-2's own grid
          (trapezoid, r in [0.3, 12], step 0.3) — 31.438617, certifying that
          number was the grid's, not an engine error. ENGINE CORRECTION to the
          adjudication's parenthetical '(not step size)': the 0.7175 deficit
          decomposes as ~0.3656 truncation (r < 0.3; fine-grid [0.3, 12] gives
          31.7904) + ~0.3518 trapezoid step error — truncation AND step size
          contribute comparably (canon sec. 6: the engine wins).
    FRAME — ANW-REPRODUCTION CERTIFICATE: this certifies the Clifford
    machinery reproduces the Adkins-Nappi-Witten isorotation moment structure;
    the ansatz IS ANW's by construction (conjugation at frozen profile) —
    DEFINITIONAL, not discovered. It is a rigid-rotor IDENTITY, NOT a measured
    moment of inertia: profile back-reaction (Battye-Krusch-Sutcliffe 2005)
    is UNTESTED here. Generation-ladder use stays dead (N17; ADJUDICATION2
    item 2): all three charged leptons are J = 1/2 — this moment quantizes
    MULTIPLET splittings (R-133), never generations."""
    # runtime: ~1.7s
    import math as _m
    import numpy as _np

    K_C, DK = 0.8317, 0.3
    U_C = I4 * _a1_qhat((0.0, 0.0, 1.0))
    U_P = I4 * _a1_qhat((1.0, 0.0, 0.0))
    DIRS = _a1_dirs()

    PROFILES = [
        ("pi*exp(-r)", lambda r: _m.pi * _m.exp(-r),
         lambda r: -_m.pi * _m.exp(-r)),
        ("pi*exp(-r^2/2)", lambda r: _m.pi * _m.exp(-r * r / 2),
         lambda r: -_m.pi * r * _m.exp(-r * r / 2)),
        ("pi/(1+r^2)", lambda r: _m.pi / (1 + r * r),
         lambda r: -2 * _m.pi * r / (1 + r * r) ** 2),
    ]
    COUPLINGS = [(1.0, 0.25), (0.7, 0.6)]
    RADII = (0.7, 1.6)

    def _pieces(r, ffun, fpfun, k_c, dk, dirs=DIRS, nx4=8):
        """(kinP, commP): the dk^2-response of the c2- and c4-sector extra
        density, direction+cycle averaged. Spatial norms and spatial-spatial
        commutators cancel exactly under the conjugations (certified below)
        and are omitted; the dk = 0 baseline is the CR class analytically."""
        x4s = [(i + 0.5) / nx4 * (4 * _m.pi / k_c) for i in range(nx4)]
        kin = cq = 0.0
        for dvec in dirs:
            x = (r * dvec[0], r * dvec[1], r * dvec[2])
            Rh, o = _a1_hedgehog(x, ffun(r), fpfun(r))
            Y = Rh.reverse() * U_P * Rh
            base = [(k_c / 2) ** 2 * _a1_nrm2(_a1_comm(ok, U_C)) for ok in o]
            for x4 in x4s:
                A = _a1_expu(U_P, dk * x4 / 2)
                Ar = A.reverse()
                qc = _a1_expu(U_C, k_c * x4 / 2)
                qr = qc.reverse()
                Omk = [qr * (A * ok * Ar) * qc for ok in o]
                extra = qr * (A * Y * Ar - U_P) * qc
                Om4 = (dk / 2) * extra + (k_c / 2) * U_C
                kin += _a1_nrm2(Om4) - (k_c / 2) ** 2
                cq += sum(_a1_nrm2(_a1_comm(Omk[j], Om4)) - base[j]
                          for j in range(3))
        m = len(dirs) * nx4
        return kin / m / dk ** 2, cq / m / dk ** 2

    # --- omission licence: spatial norms / spatial-spatial commutators cancel
    xs = (0.7 * DIRS[6][0], 0.7 * DIRS[6][1], 0.7 * DIRS[6][2])
    f1, fp1 = PROFILES[0][1], PROFILES[0][2]
    Rh, o = _a1_hedgehog(xs, f1(0.7), fp1(0.7))
    A = _a1_expu(U_P, DK * 0.9 / 2); Ar = A.reverse()
    qc = _a1_expu(U_C, K_C * 0.9 / 2); qr = qc.reverse()
    Omk = [qr * (A * ok * Ar) * qc for ok in o]
    lic = max(abs(_a1_nrm2(Omk[j]) - _a1_nrm2(o[j])) for j in range(3))
    lic = max(lic, max(abs(_a1_nrm2(_a1_comm(Omk[i], Omk[j]))
                           - _a1_nrm2(_a1_comm(o[i], o[j])))
                       for i in range(3) for j in range(i + 1, 3)))
    assert lic < 1e-12, "spatial-sector cancellation licence"

    # --- P0 discipline: one FD spot-check of the comp-perp analytic Omegas
    def _Rcp(x, x4):
        r = _m.sqrt(sum(c * c for c in x))
        Rh_, _o = _a1_hedgehog(x, f1(r), 0.0)
        A_ = _a1_expu(U_P, DK * x4 / 2)
        return A_ * Rh_ * A_.reverse() * _a1_expu(U_C, K_C * x4 / 2)

    x0, x40 = (0.8, -0.5, 0.6), 0.7
    r0 = _m.sqrt(sum(c * c for c in x0))
    Rh0, o0 = _a1_hedgehog(x0, f1(r0), fp1(r0))
    A0 = _a1_expu(U_P, DK * x40 / 2); A0r = A0.reverse()
    q0 = _a1_expu(U_C, K_C * x40 / 2); q0r = q0.reverse()
    Om_ana = [q0r * (A0 * ok * A0r) * q0 for ok in o0]
    Om_ana.append((DK / 2) * (q0r * (A0 * (Rh0.reverse() * U_P * Rh0) * A0r
                                     - U_P) * q0) + (K_C / 2) * U_C)
    R0 = _Rcp(x0, x40)
    worst_p0 = 0.0
    d = 1e-6
    for mu in range(4):
        if mu < 3:
            xp = list(x0); xm = list(x0)
            xp[mu] += d; xm[mu] -= d
            dR = (1.0 / (2 * d)) * (_Rcp(tuple(xp), x40) - _Rcp(tuple(xm), x40))
        else:
            dR = (1.0 / (2 * d)) * (_Rcp(x0, x40 + d) - _Rcp(x0, x40 - d))
        worst_p0 = max(worst_p0, _a1_coeffdiff(R0.reverse() * dR, Om_ana[mu]))
    assert 1e-13 < worst_p0 < 5e-8, "comp-perp analytic Omegas vs FD"

    # --- (1) closed form: three profiles x two coupling pairs, per radius
    worst_rel = 0.0
    for _name, ffun, fpfun in PROFILES:
        for r in RADII:
            kinP, commP = _pieces(r, ffun, fpfun, K_C, DK)
            f, fp = ffun(r), fpfun(r)
            s2 = _m.sin(f) ** 2
            for c2, c4 in COUPLINGS:
                meas = (c2 * kinP + c4 * commP) * 4 * _m.pi * r * r
                closed = (8 * _m.pi / 3) * r * r * s2 * (
                    c2 + 4 * c4 * (fp ** 2 + s2 / (r * r)))
                worst_rel = max(worst_rel, abs(meas - closed) / closed)
    assert worst_rel < 5e-12, \
        "Lambda_perp shell density must equal the ANW closed form (1e-12 class)"

    # --- (2) carrier-independence: real per-direction, cancels on the average
    kin1, comm1 = _pieces(1.6, f1, fp1, K_C, DK)
    kin2, comm2 = _pieces(1.6, f1, fp1, 2.1 * K_C, DK)
    kc_avg = max(abs(kin2 - kin1) / abs(kin1), abs(comm2 - comm1) / abs(comm1))
    d1 = _pieces(1.6, f1, fp1, K_C, DK, dirs=[DIRS[6]])       # generic (1,1,1)
    d2 = _pieces(1.6, f1, fp1, 2.1 * K_C, DK, dirs=[DIRS[6]])
    kc_dir = max(abs(d2[0] - d1[0]), abs(d2[1] - d1[1]))
    assert kc_avg < 1e-12, "averaged coefficient must be carrier-independent"
    assert kc_dir > 1e-3, "per-direction k_c-dependence must be REAL (non-trivial)"

    # --- quadraticity licence (two dk a decade apart)
    ka, ca = _pieces(0.7, f1, fp1, K_C, 0.3)
    kb, cb = _pieces(0.7, f1, fp1, K_C, 0.03)
    quad = max(abs(ka - kb) / abs(ka), abs(ca - cb) / abs(ca))
    assert quad < 1e-9, "E_extra must be exactly quadratic in dk"

    # --- (3) the 1/2: E = Lambda dk^2 vs the band convention E = (1/2)Theta omega^2.
    # Measure the physical isorotation rate omega: the adjoint rotation angle of
    # A(x4) = exp(u_p dk x4/2) read off a rotated bivector (u_c is in u_p's
    # rotation plane): cos phi = <A u_c A~ u_c~>_0 / |u_c|^2, so phi = dk*x4.
    x4t = 0.9
    At = _a1_expu(U_P, DK * x4t / 2)
    cphi = _a1_g0(At * U_C * At.reverse() * U_C.reverse()) / _a1_nrm2(U_C)
    omega_dev = abs(cphi - _m.cos(DK * x4t))
    assert omega_dev < 1e-14, "adjoint rotation angle phi = dk*x4 (omega = dk)"
    phi = _m.acos(cphi)
    # Theta = 2 E/omega^2, Lambda = E/dk^2  =>  ratio = 2 (dk*x4t/phi)^2, with
    # phi engine-measured (NOT assumed): the whole factor is the 1/2 convention.
    ratio = 2.0 * (DK * x4t / phi) ** 2
    assert abs(ratio - 2.0) < 1e-9, "Theta_ANW / Lambda_perp = 2"

    # --- (4) the integrals (closed form, Simpson; numpy)
    def _lam_closed(rgrid, c2, c4):
        f = _np.pi * _np.exp(-rgrid)
        s2 = _np.sin(f) ** 2
        fp = -_np.pi * _np.exp(-rgrid)
        y = (8 * _np.pi / 3) * rgrid ** 2 * s2 * (
            c2 + 4 * c4 * (fp ** 2 + s2 / _np.maximum(rgrid ** 2, 1e-300)))
        h = rgrid[1] - rgrid[0]
        return float(h / 3 * (y[0] + y[-1] + 4 * _np.sum(y[1:-1:2])
                              + 2 * _np.sum(y[2:-1:2])))

    lam_full = _lam_closed(_np.linspace(1e-9, 30.0, 60001), 1.0, 0.25)
    lam_trunc_fine = _lam_closed(_np.linspace(0.3, 12.0, 60001), 1.0, 0.25)
    rg = _np.arange(0.3, 12.0 + 1e-9, 0.3)       # probe-2's exact grid
    fg = _np.pi * _np.exp(-rg)
    fpg = -_np.pi * _np.exp(-rg)
    s2g = _np.sin(fg) ** 2
    yg = (8 * _np.pi / 3) * rg ** 2 * s2g * (
        1.0 + 4 * 0.25 * (fpg ** 2 + s2g / rg ** 2))
    lam_probe2_grid = float(_np.trapezoid(yg, rg))
    assert abs(lam_full - 32.1561) < 1e-3, "accurate Lambda_perp = 32.1561"
    assert abs(lam_probe2_grid - 31.43862) < 1e-4, \
        "probe-2's 31.4386 reproduced as the closed form on probe-2's own grid"

    return {
        "tier": "DERIVED-A given the frozen-profile (rigid-rotor) ansatz",
        "shell density vs (8pi/3) r^2 sin^2 f [c2 + 4 c4 (f'^2 + sin^2 f/r^2)]"
        " (worst rel, 3 profiles x 2 couplings)": worst_rel,
        "comp-perp FD spot-check (worst coeff)": worst_p0,
        "spatial-sector cancellation licence (worst)": lic,
        "carrier-independence after averaging (worst rel)": kc_avg,
        "per-direction k_c-dependence (real, must be > 0)": kc_dir,
        "dk-quadraticity licence (0.3 vs 0.03, worst rel)": quad,
        "adjoint-rate certificate |cos phi - cos(dk x4)| (omega = dk)": omega_dev,
        "Theta_ANW / Lambda_perp (measured)": ratio,
        "half_theta": ("Lambda_perp = (1/2) Theta_ANW — the identification "
                       "sentence MUST carry the 1/2 or every R-133 band "
                       "spacing computed with it is wrong by 2"),
        "Lambda_perp (test profile, full range)": lam_full,
        "probe-2 grid value reproduced (trapezoid 0.3..12 step 0.3)":
            lam_probe2_grid,
        "fine [0.3, 12] (truncation-only)": lam_trunc_fine,
        "deficit split (truncation, step)": (32.15607 - lam_trunc_fine,
                                             lam_trunc_fine - lam_probe2_grid),
        "frame": ("ANW-reproduction certificate; ansatz is ANW's by "
                  "construction (definitional, not discovered); rigid-rotor "
                  "identity, NOT a measured moment of inertia (BKS "
                  "back-reaction untested)"),
    }
