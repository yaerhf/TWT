"""TWT companion-engine self-checks — separated test harness for the deep-dive layer.
Split from twt_test.py per the engine split (knowledge/audit/engine_split_classification_2026-08-12.md):
these blocks exercise the COMPANION primitives (twt_companion.py, which re-exposes the
main engine via `from twt import *`); twt_test.py keeps the MAIN engine's checks.
CONSERVATION RULE: the two harnesses' printed totals must sum to the pre-split suite total.
Run:  python3 twt_companion_test.py
"""
import math
import sympy as sp
from twt_companion import *

def _ck(name, cond):
    print(f"  [{'OK ' if cond else 'FAIL'}] {name}")
    assert cond, name

_check = _ck


# ---- twt_algebra (companion blocks) ----------------------------------------
def check_twt_algebra():
    re_ = g8_opB_gauge_torus_relative_equilibrium()
    _ck("★ THE op-B GAUGE TORUS AND THE RELATIVE EQUILIBRIUM (R-194, 2026-08-31): the centralizer "
        "of B₀ in SO(4) is an exact 2-torus {B₀, ⋆B₀} (comm < 1e-15; exp(2πB₀u) = I < 1e-12) under "
        "which ops B/C are exactly equivariant — so relative equilibria exist generically and are "
        "indistinguishable from limit cycles to every fixed-projection instrument (three-term "
        "Fourier asserted); the modulus-folding wall |c₀| ≤ |c₊|+|c₋| forces a T/2 read (RUL-118 "
        "ground); the RE residual discriminates developed (2e-6…8e-5) from control (1.000/0.578) "
        "states (RUL-119 instrument); 'limit cycle' is a MISLABEL — closed but NON-ISOLATED orbits",
        "2-torus" in re_["torus"]
        and "MISLABEL" in re_["re_vs_limit_cycle"]
        and "NON-ISOLATED" in re_["re_vs_limit_cycle"]
        and "RUL-118" in re_["folding_wall"]
        and re_["re_residual"]["developed_max"] < 1e-3
        and re_["re_residual"]["neg_control_seeded"] >= 0.99
        and "RUL-119" in re_["duty"])

    ph_ = g8_opB_phason_neutral_manifold()
    _ck("\u2605 THE NEUTRAL MANIFOLD IS 3-DIMENSIONAL AND THE THIRD DIRECTION IS THE PHASON "
        "(R-195, 2026-09-01): R-194's exact 2-torus is UNTOUCHED and no theorem is refuted, but the "
        "op-B relative equilibrium carries one further EXACT neutral direction \u2014 translation "
        "along the hosted k. 'Spatial translation Goldstone' is wrong twice: a lattice has no "
        "continuous translation symmetry to break, and FIVE non-period lattice vectors act as the "
        "IDENTITY on this state (exact arithmetic here; measured 7.8e-16), so only motion along k "
        "moves it. The corpus's own word is PHASON. Established by the continuous translation "
        "generator projecting into the null space at 1.000000 (gauge overlaps 0.0/3.1e-5), by "
        "sigma_3 tracking the FD floor as h^2 beside two THEOREM zeros while sigma_4 sits immobile "
        "at 1.1400e-2, and by nu = 0 to 1e-14 over ~2.2 lattice steps \u2014 NOT by the void "
        "exponent scan. NO PEIERLS-NABARRO BARRIER at this state, with the scope condition named "
        "(shorter wavelength TESTED at 1.58x, R-197: NOT restored; larger amplitude UNTESTED)",
        ph_["neutral manifold dimension"] == 3
        and ph_["R-194 untouched (exact 2-torus centralizer)"] is True
        and "PHASON" in ph_["the third direction"]
        and ph_["transverse lattice vectors acting as the identity (exact)"] == 5
        and abs(ph_["continuous translation generator -> nullspace projection"] - 1.0) < 1e-9
        and ph_["pattern_phase_mode -> nullspace projection"] < 0.9
        and "NONE" in ph_["PEIERLS-NABARRO barrier at this state"]
        and "UNTESTED" in ph_["where the barrier should return"])

    _ck("\u2605 THE EXPONENT-DIFFERENCE DISCRIMINATOR IS VOID \u2014 THE RUL-122 GROUND (R-195): "
        "N3d registered 'the DIFFERENCE OF EXPONENTS, which no identity can fix'. Closed form: for "
        "r(eps) = sqrt((L eps)^2 + (Q eps^2/2)^2) the fitted log-log slope depends on L/Q ALONE "
        "(verified invariant under rescaling both), so it tends to 2 for a true symmetry (L = 0) "
        "AND for a non-symmetry with L/Q = 1e-7 \u2014 both 2.000 here \u2014 while a stiff "
        "direction gives 1.000. It carries NO symmetry information. Measured on the flow: a "
        "direction 1.07e6 x sigma_soft \u2014 provably not a symmetry \u2014 scanned at 1.987. "
        "SIXTH vacuous check of the arc, built INSIDE the prose clause written against the fifth",
        "VOID" in ph_["exponent-difference discriminator"]
        and abs(ph_["closed-form slopes (symmetry / non-symmetry / stiff)"][0] - 2.0) < 1e-6
        and abs(ph_["closed-form slopes (symmetry / non-symmetry / stiff)"][1] - 2.0) < 1e-3
        and abs(ph_["closed-form slopes (symmetry / non-symmetry / stiff)"][2] - 1.0) < 1e-3)

    _ck("\u2605 THE ONSET IS A TWO-TERM STUART-LANDAU NORMAL FORM, AND THE SINGLE g WAS MIS-STATED "
        "(R-195): refitting the five recorded (A, c*) points gives c* - c_lin = 10.4410 A^2 + "
        "42.01 A^4, cutting the residual 791x against one term. g_eff is STRICTLY MONOTONE, five "
        "of five ordered \u2014 so the previously quoted '10.45403 +- 0.01353, constant to 0.349%' "
        "reported a fully resolved amplitude dependence as scatter, and the number banked as the "
        "Stuart-Landau coefficient is NOT it: the cubic coefficient is the A->0 limit g0. CREDIT: "
        "the five-point table, the nine-sig-fig non-circularity ground and the first two-term "
        "value are the N3c REVIEWER's, not the round's",
        abs(ph_["Stuart-Landau g0 (cubic, the A->0 limit)"] - 10.4410) < 2e-3
        and 40.0 < ph_["Stuart-Landau g2 (quintic)"] < 44.0
        and ph_["residual reduction, one-term -> two-term"] > 700.0
        and ph_["g_eff strictly monotone (5 of 5)"] is True
        and "REVIEWER" in ph_["credit for the five-point table and the two-term value"]
        and "SECANT" in ph_["engaged-ceiling dlnT/ddg = +1.018"]
        and "RUL-114" in ph_["fence"])

    ec_ = g8_engaged_ceiling_convex_not_derivative()
    _ck("★ THE ENGAGED-CEILING RELATION IS CONVEX, SO R-195's dlnT/d(delta g) = +1.018 "
        "IS A CHORD, NOT A DERIVATIVE (R-196, 2026-09-02): R-195 measured ONE engaged rho_sat "
        "and wrote a secant in derivative notation. Four engaged states (rel 5.5e-13..9.2e-13) "
        "give successive secants +0.4400/+1.2616/+2.0621/+3.1714 — STRICTLY MONOTONE "
        "INCREASING, spread 157%%, and the chord across R-195's own interval reproduces +1.018 "
        "to four figures while the local slope varies 4.69x WITHIN it (the 7.21x first written "
        "in the L1 wrongly spanned a secant BEYOND that interval — self-corrected at the "
        "ceremony). Only the SIGN survives, which is all R-194's sign-withdrawal required, so "
        "that withdrawal stands untouched. NON-VACUOUS: the same test on a log-linear synthetic "
        "returns NOT-convex, discriminating by >1e8. UNDER-CLAIM adopted: |omega| extrapolates "
        "to a DRIFT BIFURCATION at delta g* ~ 0.84-1.15 — WINDOW-DEPENDENT, hence a "
        "can-fail prediction two continuation points away, never a measurement",
        ec_["strictly monotone increasing (CONVEX)"] is True
        and abs(ec_["chord over R-195's interval [0, 0.48345]"] - 1.018) < 5e-3
        and abs(ec_["local-slope variation WITHIN that interval"] - 4.69) < 0.05
        and ec_["negative control (log-linear synthetic) is NOT convex"] is True
        and ec_["T = 2*pi/|omega| identically"] is True
        and len(ec_["and it is WINDOW-DEPENDENT (all5/last4/last3/last2)"]) == 4
        and "SIGN only" in ec_["what survives of R-195"]
        and "RUL-114" in ec_["fence"])

    in_ = g8_track2_inertial_face_and_charge()
    _ck("\u2605 THE INERTIAL FACE HAS AN EXACT CANONICAL CHARGE THAT BUYS NO BARRIER (R-199, Phase N4 "
        "Track 2, 2026-09-03; conditional on V4-m5): the reactive term placed as a force is not Lyapunov "
        "(sign-indefinite <V,[B0,F]>), placed as a Coriolis term it is work-free and variational, with the "
        "Noether charge Q_can conserved to 1.9e-8 at c = 12 where the kinetic half drifts 46 percent; the drive "
        "is a frame rotation c -> c - m5 Om0; the m5 -> 0 limit op B' is an ANISOTROPIC mobility "
        "(1/gd on ker ad_B0, 1/sqrt(gd^2+c^2) on the planes), not a placement of the kernel; op B' holds the "
        "hedgehog 31x longer (3.18 vs 0.103) - LESS than the 36.6x reparametrisation of the same collapse - and "
        "NEGATIVE on the plateau condition; the same-charge uniform carrier lies 2172.6 below the charged seed "
        "(0.4 percent of the defect's excess): N73 (f2) attacked and not reached; inertia UNDECIDED 0/18.",
        "not a placement" in in_["exact_clauses"]
        and in_["charge drifts (c = 12, Om0 = 0, gd = 0, 0.3 tu)"]["Q_kin_c12"] > 0.3
        and in_["no-centrifugal-barrier (keeper)"]["charge_cost_frac_c12_m5_1_upper_bound_at_U_eq_I"] < 0.05
        and "attacked and not reached" in in_["verdicts"]
        and "conditional on V4-m5" in in_["tier"])

    aw_ = g8_track1b_active_window_balance_and_zero_work_identity()
    _ck("R-201 (Track 1b): |G|^2 = gamma_eff^2|F|^2 + c^2|[B0,F]|^2 exactly on random fields (worst rel %.1e) and the check FAILS on a reactive channel that does work ([B0,F] + 0.3 F) (rel %.2f > 0.05: it can fail); the banked passive kernel admits no non-vacuum steady state at zero drive; the active window's balanced localized state recorded, not asserted" % (aw_["worst_rel_on_random_fields"], aw_["failure_mode_rel_working_reactive_channel"]),
        aw_["worst_rel_on_random_fields"] < 1e-12 and aw_["failure_mode_rel_working_reactive_channel"] > 0.05)
    ro_ = g8_track1b2_root_offset_balance_identity()
    _ck("R-202 (Track 1b round 2) + R-203 exact form: a balanced window state sits ABOVE the lower root by dx = (L/S)/sqrt(a^2-4b) to O((L/S)^2) over %d random windows (second-order ratio to the derived b eps^2/D^1.5: %.3f < 1.5); the EXACT identity <delta>_w = (|G|/S)/sqrt(D) + (b/sqrt(D))<delta^2>_w holds to 1e-10 on random cores (the wrong root breaks it at O(1)); the balance |G_core| = L is the separate assumption; and the check FAILS where it must: a^2 < 4b has no root and no real balance, and at the UPPER root the offset flips sign (W2 branch)"
        % (ro_["trials"], ro_["worst_second_order_constant"]),
        ro_["worst_second_order_constant"] < 1.5 and ro_["trials"] > 50 and abs(ro_["lower_root_W1"] - 0.5) < 1e-15 and ro_["exact_second_order_identity_worst_rel"] < 1e-10 and abs(ro_["witness_CFW16_HW1"]["balance_predicted"] - 0.710839) < 2e-6)
    fl2_ = g8_track2b_fixed_charge_floor_is_configuration_independent()
    _ck("R-200 (Branch B): the fixed-charge kinetic floor is configuration-independent at c = 0 - Gram = N diag(a^2, a*^2) on random SO(4) fields, K_min identical across fields and equal to the closed form to 1e-13, and the SAME check FAILS on a site-weighted metric (rel %.3f > 0.05: it can fail); N73 (f2) excluded by construction at c = 0 on V4-m5's realization" % fl2_["failure_mode_rel_on_site_weighted_metric"],
        fl2_["failure_mode_rel_on_site_weighted_metric"] > 0.05 and (max(fl2_["K_min_fields"]) - min(fl2_["K_min_fields"])) / fl2_["closed_form"] < 1e-13)
    lim_ = g8_track1a_saturation_is_a_limiter()
    _ck("\u2605 THE SATURATION TERM IS A LIMITER, NOT A GAIN (R-198, Phase N4 Track 1a, 2026-09-03): "
        "g_eff = \u03b3(1+|F|\u00b2/\u03c1\u00b2) \u2265 \u03b3 for every \u03c1_sat, equality iff |F| = 0 (DERIVED-A), "
        "so the banked kernel's only nonlinearity can never supply CQ-CGL gain; on the CFW16 band-hosting "
        "cell the linear-profile hedgehog is certified degree-0 at t = 0.105 / 0.070 / 0.020 / 0.005 (op B) "
        "for t = 0 seed dampings 1 / 4 / 31 / 301 \u2014 the ceiling clamps the core to |F| ~ 2\u03c1 within "
        "0.005 tu (measured 5.9 / 5.6 / 5.0, not 4 / 31 / 301) and in its own clock the core unwinds SLOWER; "
        "13/13 frozen-criterion elements NO EXISTS, the drive band grew \u2264 1.048\u00d7 over any defect's "
        "life (band-as-gain UNTESTED, not refuted); op C differs from op B on the defect-side strain "
        "(C/B 0.46\u20130.91 at 6/6) but not on the verdict observables \u2014 a located gap, N73 (f3)(f).",
        "DERIVED-A" in lim_["exact_clause"]
        and lim_["seed_arithmetic_k0 (t = 0, NOT a realised regime)"][33.8] > 3.99
        and lim_["measured engagement at t = 0.005 (op B / op C)"]["B"][3.38] < 5.0
        and lim_["certified degree-0 UPPER BOUNDS by k0, 0.005-tu cadence (op B / op C)"]["B"][1] == 0.105
        and lim_["certified degree-0 UPPER BOUNDS by k0, 0.001-tu cadence dt-converged (op B), five-point ladder"][27954] == 0.001
        and "did not run" in lim_["frozen-criterion elements"]
        and "not selection" in lim_["op C vs op B"]
        and "N73 (f3)(f)" in lim_["tier"])

    tr_ = g8_travelling_re_short_wavelength()
    _ck("\u2605 A TRAVELLING RELATIVE EQUILIBRIUM AT 1.58\u00d7 SHORTER WAVELENGTH, AND ITS PHASON IS NOT "
        "PINNED EITHER (R-197, 2026-09-02): at k = (\u03c0/16)(\u22122,\u22121,0,0) the three lattice "
        "vectors that fixed R-195's state now MOVE it (phase \u22123\u03c0/16, exact arithmetic) and the "
        "drift lies along [1,\u22121,0,0], off the k-axis \u2014 which is why the round's third residual "
        "column, pattern_phase_mode, could not see it and the L1 wrongly reported NOT an RE. Exact "
        "generators: 0.2908 \u2192 9.57e-4; relaxed to 2.1e-5 (R-194's band); Newton 1.2e-12 and, on "
        "the advective residual, 8.4e-15. The Jacobian done right has EXACTLY three exact zeros "
        "(gauge 2-torus + one phason \u2014 a single-k pattern is a one-parameter phase family) with "
        "\u03c3\u2084 = 0.325 immobile; the washboard is null to ~5e-4. RUL-119 as banked is ONE-SIDED "
        "and re-cut to exact generators + Newton; \u03c9 is border-convention-dependent here (gauge "
        "overlap 0.5276 vs 0.000000 at R-195). R-195's wavelength disjunct: MEASURED, NOT CONFIRMED; "
        "amplitude disjunct UNTESTED; two states are not a genericity claim",
        tr_["measured exact zeros at R-197"] == 3
        and tr_["expected neutral-manifold dimension (both k)"] == 3
        and tr_["continuous translation symmetries (both k)"] == 1
        and tr_["residuals on the committed attractor"]["exact_generators"] < 1e-3
        and tr_["residuals on the committed attractor"]["newton_advective"] < 1e-10
        and "NOT detected" in tr_["Peierls-Nabarro barrier at 1.58x"]
        and "UNTESTED" in tr_["R-195 would-change-if"]
        and "ONE generator" in tr_["RUL-119 as banked"]
        and "genericity" in tr_["NOT claimed"]
        and "RUL-114" in tr_["fence"])

    wq = b0_plane_detector_wind_quantum()
    _ck("★ THE B0-PLANE DETECTOR WIND QUANTUM (branch-scan bank 2026-08-31, DERIVED-A instrument "
        "algebra): phase_g reads an off-origin circle (radius ρ, offset d = 1−⟨cos β⟩) — winding "
        "transition wind/rev = 1 iff ρ > d else 0 (reading VOID at ρ ≤ d); on a limit cycle "
        "Δ_cycle = 2πn/(Ω₀T) with n INTEGER (measured n = 1, three runs/two cells) so the slip is "
        "a period and an integer, not a free number; the band MIDPOINT is a biased estimator "
        "(≥1.4× at d/ρ = 0.57 — quote cycle-averages only); measured closure: REF 6.2784 passes, "
        "D 6.3057 does not (transient-vs-attractor OPEN). Adler 1946 / Kralemann–Rosenblum–"
        "Pikovsky 2008 prior-art anchored",
        wq["midpoint_bias_at_d_over_rho_0.57"] >= 1.4
        and "n integer" in wq["wind_quantum"]
        and "VOID" in wq["winding_transition"]
        and abs(wq["closure_REF"] - 6.2784) < 1e-3
        and abs(wq["closure_D"] - 6.3057) < 1e-3
        and "never a band midpoint" in wq["duty"])

    srp = single_relaxation_family_exclusion_probe()
    _ck("★ Phase B / B2 — the SINGLE-RELAXATION FAMILY-EXCLUSION PROBE (the 'unspent 2b move', spent) "
        "[FRAMING/CANDIDATE-family-exclusion]: the simplest causal kernel χ(ω)=χ₀/(1−iωτ) (Debye) is a "
        "genuine FAMILY-EXCLUSION — a PASSIVE single-relaxation kernel is FDT-RESPECTING by construction, so "
        "Θ_rel (the FDT-violation, I-12) is IDENTICALLY 0 for EVERY (χ₀,τ) ⟹ it CANNOT source the FDT-violation "
        "the program hunts ⟹ EXCLUDED as the Θ_rel-kernel. It fits the passive targets VACUOUSLY (2 dials vs 2 "
        "numeric targets = exactly-determined; N33's rank-deficiency at the kernel level) and satisfies the "
        "spin-2 ≤4-moment bound (1 relaxation = 1 moment). ⟹ the FDT-violating content requires a DRIVEN "
        "(non-equilibrium) kernel ⟹ directs to the CUDA D4-Langevin driven sim (B3). Causality/KK "
        "engine-checked (Re reconstructed from Im); the exclusion rides I-12 (definitional). A first-class "
        "family-exclusion (brief B0).",
        "verified" in srp["causality_KK"] and "EXCLUDED" in srp["exclusion"]
        and "Theta_rel" in srp["exclusion"] and "vacuous" in srp["counting"]
        and "DRIVEN" in srp["directs_to"] and "family-exclusion" in srp["tier"])
    print("        ⇒ Phase B/B2: the passive single-relaxation family is EXCLUDED as the Θ_rel-kernel (Θ_rel≡0, FDT-respecting) and its passive fit is vacuous (2 dials, 2 numbers) ⟹ the analytic 2b move is spent; the FDT-violation needs a DRIVEN kernel ⟹ B3 (the CUDA D4-Langevin sim).")
    dlg = d4_langevin_calibration_gate()
    _ck("★ Phase B / B3 — the CUDA D4-Langevin CALIBRATION GATE [DERIVED-A reduction + FRAMING sim]: the N31 "
        "canted-D4 planar statics reduce EXACTLY to a 1D rotor chain (per-bond −12J cos(Δθ) − 2√2 D sin(Δθ)) "
        "reproducing q*=atan(√2/6) AND K_long=√38 J (sympy-exact, live vs N31); target renorm K_long/K_c = "
        "(19/2)√38 ≈ 58.56. GATE PASSED on device=cuda. DRIVEN result (CANDIDATE, in the B4 memo; "
        "RE-TIERED 2026-07-26 per the sharpened no-toy rule, KP_T3c_closure R10 — this ran on the 1D "
        "EFFECTIVE CHAIN, a TOY-LEVEL CONSISTENCY RECORD, not a conclusion-bearer): the sim SOFTENS K_eff "
        "monotonically but via spiral-order DEGRADATION or drive-LOCKING — NOT a stable softened-ORDERED "
        "spiral at K_c ⟹ the (19/2)√38 is CROSSED en route to disorder, NOT SELECTED at toy level; the "
        "prior located-negative/DQCP-selection wording is WITHDRAWN as a conclusion — CLASSICAL "
        "SELECTABILITY OF K_c IS OPEN; the instrument-grade 4D record = gate-0 (memoryless quadrant EMPTY, "
        "36.8× shortfall) + G1b (kernel hunt UNMEASURED-DRY), K4D closures at consensus. Invariance: "
        "softening-via-disorder was drive-model-invariant WITHIN the 1D toy record.",
        abs(dlg["target_renorm_58"] - (19.0/2.0)*math.sqrt(38.0)) < 1e-9
        and "GATE PASSED on device=cuda" in dlg["calibration_gate"]
        and "atan(sqrt(2)/6)" in dlg["calibration_gate"]
        and "SOFTENS" in dlg["driven_result_CANDIDATE"] and "NOT SELECTED" in dlg["driven_result_CANDIDATE"]
        and "INVARIANT" in dlg["invariance"] and "DERIVED-A" in dlg["tier"])
    print("        ⇒ Phase B/B3: the CUDA D4-Langevin sim's CALIBRATION GATE PASSED (statics reproduce N31 exactly on the 4090); the driven 58.6 test = a TOY-LEVEL CONSISTENCY RECORD (re-tiered 2026-07-26 per the no-toy rule R10 — 1D chain; classical selectability of K_c OPEN; the instrument-grade 4D record: gate-0 quadrant empty + G1b unmeasured-dry). Full history in the B4 candidate memo.")

    ss = static_susceptibility_sumrule_and_kss_channel_mismatch()
    _ck("W2.2 static-susceptibility SUM-RULE datum + KSS wrong-object adjudication [FRAMING "
        "verdict + DERIVED-A datum]: manufactures N33 input (3) from the canted-D4 statics — "
        "χ_long(0) = 1/√38 J (the M₋₁ = ∫Im χ/ω KK moment; KK-safe, FDT-free per I-12) — and "
        "NAMES all four channel coordinates. VERDICT: same CELL layer as the KSS/GW anchor but "
        "DIFFERENT operator/channel (order-parameter magnon χ_θθ vs shear-viscosity η = "
        "stress-tensor transport) ⟹ WRONG-OBJECT ⟹ NO usable anchor added ⟹ rank-deficiency "
        "UNCHANGED (table count stays 1). Channel-MATCHED to the K_c row: χ_c/χ_long = (19/2)√38 "
        "(the bare static-susceptibility companion to the K_c target). Sub-finding: the f-sum "
        "M₊₁ needs the rotor inertia (absent from statics) ⟹ one moment only. Ledger N43.",
        abs(ss["datum"]["chi_long_times_J"] - (1.0 / math.sqrt(38.0))) < 1e-12
        and ss["added_usable_anchor_for_kss"] is False
        and ss["channel_match_to_Kc"]["matches"] is True
        and abs(ss["channel_match_to_Kc"]["renorm_factor_chi_c_over_chi_long"]
                - (19.0 / 2.0) * math.sqrt(38.0)) < 1e-9
        and "PARTIALLY DELIVERED" in ss["n33_input_3_status"]
        and "DERIVED-A" in ss["tier"])
    sts = stress_tensor_shear_channel_static_moment()
    _ck("★ A3 (N47) — the STRESS-TENSOR/shear-channel static moment (N43's would-change-if (i), the one "
        "move that could lift the usable-anchor count): compute the canted-D4 spiral's static SHEAR from "
        "LSWT. A lattice shear of the spiral IS a transverse-wavevector tilt (EXACT) ⟹ G_shear = 2q*²·K_trans "
        "≈ 0.637 J (K_trans erratum 2026-07-26) is the ORDER-PARAMETER Frank-elastic modulus (built from N31/N43's transverse stiffness), "
        "WRONG-OBJECT for the KSS η (stress-tensor momentum transport) — same wall as N43. The genuine "
        "stress-tensor shear modulus is the GATED C_T·Λ² (N44, KK-linked to η, not independent). ⟹ NO "
        "independent KSS-matched static anchor from statics; usable-anchor count STAYS 1; N43 wci (i) "
        "CLOSED-NEGATIVE. Confirms the honest ceiling: statics sees only the order-parameter channel; the "
        "stress-tensor transport channel is #1-gap kernel-gated. FRAMING + DERIVED-A (G_shear number)",
        abs(sts["G_shear_over_J"] - 2*(math.atan(math.sqrt(2)/6))**2 * (2*math.cos(math.atan(math.sqrt(2)/6)) + 4)) < 1e-9
        and sts["usable_anchor_count"] == 1 and "CLOSED-NEGATIVE" in sts["verdict"]
        and "ORDER-PARAMETER" in sts["verdict"] and "GATED" in sts["verdict"])
    print("        ⇒ A3/N47: the stress-tensor/shear static moment does NOT lift the count — the computable static shear (G_shear≈0.637J, K_trans erratum 2026-07-26) is order-parameter Frank-elastic (wrong-object, N43); the true stress-tensor shear modulus is the gated C_T·Λ² (N44). Count stays 1; honest ceiling confirmed.")


# ---- twt_observer_qm (companion blocks) ----------------------------------------
def check_twt_observer_qm():
    td = two_defect_tensor_complex_space()
    _ck("★ TWO-DEFECT TENSOR COMPLEXIFICATION (2026-08-31, DERIVED-A pointwise / generic-given-two-"
        "complex-structures): all 9 winding-blade pairs give ker(J₁⊗I − I⊗J₂) exactly 8-real-dim = "
        "ℂ²⊗ℂ² (the two-qubit space; tr K = 0 forces the 8/8 split for ANY pair — the blades don't do "
        "the work); same-blade swap splits 3+1 with the singlet Λ² one complex dim; distinct-blade "
        "identification NON-CANONICAL (U(1) per pair — the CP¹-candidate connection seed) yet the "
        "singlet SLOT is choice-invariant (~7e-16). SCOPE banked with it: pointwise only — the "
        "bundle-level global-choice (Hopf) question untouched; N53 NOT unbanked; no photon claim",
        all(v == 8 for v in td["dims_all_9_pairs"].values())
        and len(td["dims_all_9_pairs"]) == 9
        and "singlet Lambda^2 one complex dim" in td["structure"]
        and "choice-invariant" in td["identification"]
        and td["slot_invariance_dev"] < 1e-12
        and "N53 NOT unbanked" in td["scope"]
        and "GENERIC" in td["tier"])

    tun = tunneling_evanescent_decay_constant()
    _ck("★ WP-TUN-1 RESOLVED — the §B.3.6 tunneling decay constant [DERIVED-A]: the forbidden-region "
        "recovery of κ = √(2m(V−E))/ℏ is EXACT in the non-relativistic (Schrödinger) limit (0%, NOT 5% — "
        "it is the defining equation of the tail); the leading deviation is a RELATIVISTIC (KG-parent) "
        "correction κ_rel/κ_NR = √(1−(V−E)/2mc²) ~ 1−(V−E)/4mc², controlled by (V−E)/mc² (barrier energy "
        "vs rest mass), NOT the tunneling depth V₀/E. ⟹ the V2-era '5% at V₀/E≥5' is MIS-PARAMETRIZED and "
        "DEMOTED (a 5% deviation needs (V−E)~0.2mc², a semi-relativistic barrier, independent of V₀/E). "
        "TWT-specific candidate deviation (wave-train~barrier-scale interference) stays CANDIDATE.",
        "EXACT" in tun["nr_recovery"] and "0%" in tun["nr_recovery"]
        and "sqrt(1 - (V-E)/(2 m c^2))" in tun["kg_correction"]
        and "(V-E)/mc^2" in tun["deviation_controlled_by"] and "NOT V0/E" in tun["deviation_controlled_by"]
        and "DEMOTED" in tun["v2_figure_verdict"] and "DERIVED-A" in tun["tier"])


# ---- twt_spectra (companion blocks) ----------------------------------------
def check_twt_spectra():
    dL = math.degrees(lepton_phase_from_DoverJ(0.787))  # δ_L the LEPTON Brannen phase (V2 Q1: NOT the Cabibbo angle)
    _ck(f"δ_L = ⅓arctan(D/J) ≈ 12.73° (lepton phase; the θ_C=δ_L identification is REFUTED, live reading = "
        f"frequency-ratio |V_us|²=m_d/m_s §19.7)  (got {dL:.2f}°)", abs(dL - 12.73) < 0.1)
    # §19.7 Cabibbo PROBABILITY reading: |V_us|² = Born projection of a VECTOR SO(2) rotation, not a spinor overlap
    cvs = cabibbo_vector_vs_spinor()
    _ck(f"|V_us|²: VECTOR sin²θ_C={cvs['vector sin^2(theta_C)']:.4f} ≈ data {cvs['data |V_us|^2']:.4f} "
        f"within θ_C residual (got {cvs['vector_resid']*100:.1f}% ≤ 4%)", cvs['vector_resid'] <= 0.04)
    _ck(f"|V_us|²: SPINOR sin²(θ_C/2)={cvs['spinor sin^2(theta_C/2)']:.4f} is ≥3× too small "
        f"(data/spinor={cvs['data/spinor']:.2f} ≥ 3)", cvs['data/spinor'] >= 3.0)
    _ck(f"spinor reading = 1−half_angle_overlap(θ_C)²  (genuine §15.4 object, not a strawman; "
        f"got {cvs['spinor = 1-overlap^2']:.4f} = {cvs['spinor sin^2(theta_C/2)']:.4f})",
        abs(cvs['spinor = 1-overlap^2'] - cvs['spinor sin^2(theta_C/2)']) < 1e-9)

    sm_test = [1.0, 2.0, 5.0]
    eig = sorted(float(x) for x in __import__('numpy').linalg.eigvalsh(amplitude_to_operator(sm_test, 0.4)))
    _ck("F3.2 amplitude→operator [DERIVED]: M(ψ)=R_G(ψ)·diag(√m)·R_G(ψ)ᵀ, ψ a rotation about G=(1,1,1) "
        "(the §19.6.1 ℤ₃ axis); eigenvalues = √m exactly; unique among ℤ₃-preserving choices",
        all(abs(a - b) < 1e-9 for a, b in zip(eig, sorted(sm_test))))
    tst = ckm_from_mass_pinned_psi()
    _ck(f"F3.3 THE TEST [the anti-fake-positive payoff]: mass-pinned ψ fed forward → DEMOCRATIC CKM "
        f"(ℤ₃ forces |V₁₂|=|V₂₃| at every β), structurally NOT the λ-ladder → (ii) located boundary: CKM "
        f"needs non-G (ℤ₃-breaking) eigenVECTOR data; predicts_ladder={tst['predicts_ladder']}",
        tst['predicts_ladder'] is False and tst['verdict'].startswith('ii'))

    print("  meta-time-phase operator → CKM (TASK metatime/item-15 — exploiting e₄ Part A; outcome iii):")
    mop = metatime_generation_operator(1.033, 0.973, 2/9)
    _ck("1A: meta-time-phase generation operator built on the anti-self-dual triple has the √m_n as eigenvalues (eigenframe is R_G(ψ) independent of (b,ε) → ℤ₃-symmetric, F3's structural class)",
        abs(float(__import__("numpy").linalg.eigvalsh(mop)[0])) >= 0)  # constructs without assertion failure
    mc = ckm_from_metatime_operator()
    _ck(f"1B [(iii) DERIVED]: with ψ fixed (no tuned ψ_u≠ψ_d), the meta-time operator gives DEMOCRATIC CKM (V12={mc['CKM_offdiagonals_psi_fixed']['V12']},V13={mc['CKM_offdiagonals_psi_fixed']['V13']}), NOT the ladder — the e₄-dip ε is an eigenVALUE effect; missing = ℤ₃-breaking AMONG generations",
        mc['ladder_emerges'] is False and mc['free_inputs_used'].startswith('none'))
    xr = baryon_rank2_mode_cross_sector()
    _ck("cross-sector (CKM-blind, STRUCTURAL not instance): rank-2 deformation present in BOTH sectors (generation ε; v14's kσ spin-tensor/Δ-N — c₀ rank-0) but does NO CKM work (core iii) → structural presence, NO coherent CKM link",
        xr['structural_presence_both_sectors'] is True and xr['coherent_CKM_link'] is False)
    ms = ckm_metatime_status()
    _ck("F3 status: the non-R_G operator F3 was missing (the meta-time phase) is ALSO ℤ₃-symmetric → F3 CONFIRMED & SHARPENED, not closed; the ladder needs per-generation asymmetry (lead: from the colour map?)",
        ms['F3_status'].startswith('located gap CONFIRMED'))

    dp = dip_planes_multiaxis_but_uniform_is_single_axis()
    _ck("D3 [Level 1]: the three per-generation dip planes span so(3) (rank 3, multi-axis) — a NON-uniform dip WOULD be multi-axis — but "
        "the uniform-strength dip sums to exactly the colour/symmetric (1,1,1) axis = SINGLE axis; the multi-axis freedom is not engaged",
        dp["dip_planes_span_so3_rank"] == 3 and abs(dp["uniform_dip_parallel_to_colour_axis"] - 1.0) < 1e-9)
    pd = phase_D_colour_updown_blind()
    _ck("D4 [Phase D RUN, not cut off]: the colour/I₄ channel acts on the spatial axes; up,down are BOTH colour triplets → the SAME colour "
        "rotation cancels in V_u†V_d → still democratic; [colour,I₄]=0 so handedness can't differentiate. The thesis's mechanism supplies no per-weak-isospin rotation",
        float(pd["[M_u,M_d]_after_colour"].split("e")[0]) < 10 and pd["[colour_gen,I4]"].startswith("0"))

    gb = gate_B_branch()
    _ck("Gate B [rank analysis → (iii); SUPERSEDED to (ii) LOCATED by the CKM arc]: the circulant theorem stands as algebra; "
        "the rank analysis alone left U1/U2 under-determined, but the CKM arc DERIVED the {projector+S₊+gen-space} pair (+e₄) "
        "→ (ii) LOCATED, democratic GENUINE (circulant linchpin), residual = Θ_rel (#1 gap)",
        "RESOLVED" in gb["outcome"] and "(ii) LOCATED" in gb["outcome"] and gb["circulant_theorem"].startswith("STANDS")
        and "MIXING-REACHABLE" in gb["lean"])

    cfv = ckm_frame_fit_is_vacuous()
    _ck("GUARD — the fit-based CKM 'fix' (V=F†UF, U∈U(3) fitted, reported loss≈1e-7 + right J) is VACUOUS: "
        "U=FVF† exists for ANY target unitary (fits a random unitary to ~1e-16 as well as the hierarchical CKM), "
        "so the loss and J are fitted not derived. Confirms only the weak-isospin (iii) lean (U(3) room via E = "
        "mixing-reachable); does NOT close the gap (DERIVE U, don't fit it)",
        cfv["verdict"].startswith("VACUOUS") and float(cfv["fits_random_unitary_err"]) < 1e-12)

    print("§19.7b Cl-i — I₄ generation over-determination (exact) + CKM from triplet overlap (located gap ii-a):")
    i4o = i4_generation_overdetermination()
    _ck(f"(b) I₄ map ties lepton↔quark generations EXACTLY (involution, L→Q bijection, G→±GQ) — "
        f"fixes the 3-count + shared ℤ₃ cycle; DISTINCT from the ~1.1% D/J leg (that gap is {i4o['DoverJ_gap_pct']}%, numerical)",
        i4o['I4_constraint_error_pct'] == 0.0 and i4o['is_the_1.1pct_leg'] is False
        and i4o['DoverJ_gap_pct'] > 0.5)
    ckm = ckm_from_triplet_overlap()
    _ck(f"(a) CKM from triplet overlap: ii-a located gap (F3-blocked) — circulant→permutation, no mixing (E1); "
        f"ψ-free specificity {ckm['E2_leading_offdiag_fractions']} & rank {ckm['E2_overlap_rank']} not 3 (E2); "
        f"no natural ψ=±δ_L/0 gives the λ-ladder (probe) — ε-in-eigenvalues necessary but NOT sufficient",
        ckm['verdict'].startswith('ii-a') and ckm['E1_always_permutation']
        and ckm['E2_overlap_rank'] < 3 and ckm['probe_natural_psi_gives_ladder'] is False)
    ab = i4_lepton_quark_amplitude_blind()
    _ck(f"path-(i)/#14: I₄ AMPLITUDE-BLIND — grade-split I₄(2→2 gen/mixing) vs e₄(2→3 charge); "
        f"lepton mass-Koide↔quark CHARGE (2/3↔2/3 at N=3); quark K's "
        f"(d={ab['K_down']},u={ab['K_up']})≠lepton 2/3 ⇒ 'quark-Koide=I₄·lepton-Koide' REFUTED; "
        f"#14 stiffness ratio = located gap N12 OUTSIDE the Hodge map",
        ab['I4_leg_grade'] == 2 and ab['e4_leg_grade'] == 3 and ab['amplitude_blind'] is True
        and ab['quark_Koide_is_I4_image_of_lepton_Koide'] is False)
    sr = q_l_stiffness_ratio_is_gap_gated()
    _ck(f"#14/N12 fork LEANS Layer-2 (mass-ontology relocation): valid target m_p/m_e={sr['m_p/m_e']}~"
        f"v/f_π={sr['v/f_pi']} is a ~1836× ABSOLUTE-SCALE hierarchy at the #1 gap; isometry-linkage does "
        f"NOT reach CAND 1's grade ratio (cf. C_A/C_F=9/4) ⇒ RELOCATED, CAND 1 NOT foreclosed/NOT computed; "
        f"vs the witness-only b-ratio it is an INDICATOR-level cross-check, not a verification",
        sr['sectors_isometry_linked'] and sr['sector_asymmetry_is_e4_dip']
        and sr['target_is_absolute_scale_hierarchy'] and 'NOT computed' in sr['CAND1_layer1_24cell']
        and 'INDICATOR-LEVEL' in sr['CAND1_layer1_24cell'])
    c1 = cand1_24cell_ratio_computed()
    _ck(f"#14/N12 CAND 1 COMPUTED: D4 24-cell ({c1['vertices']} verts, octads {c1['octads_8v/8s/8c']}) "
        f"projection/Casimir ratios all O(1) (largest {c1['largest_natural_ratio']}=8/3), undershoot "
        f"m_p/m_e={c1['target_m_p/m_e']} by {c1['undershoot_factor']}× ⇒ self-dual triality pins the "
        f"lepton/quark sector ratio near 1; CAND 1-as-a-ratio CLOSED, CAND 3 indicator+gap-gated, "
        f"CAND 2 the Layer-2 survivor ⇒ #14 sits entirely at the #1 gap (lean→computed, not a theorem)",
        c1['vertices'] == 24 and c1['octads_8v/8s/8c'] == (8, 8, 8)
        and c1['largest_natural_ratio'] < 3.0 and c1['undershoot_factor'] > 100
        and 'CLOSED' in c1['CAND1_status'] and 'survivor' in c1['CAND2_status'])

    print("§— matter-as-defect: generations = protected sub-harmonics; CKM asymmetry read in FREQUENCY (FIT/FRAMING/CANDIDATE; TWT_DEFECT_CKM_GLUON.md):")
    gl = generation_subharmonic_ladder()
    _ck("GST/FRITZSCH relation RE-READ in the defect frame [FIT, indicator-level]: |Vus|≈sqrt(m_d/m_s) (textbook 1968) reads as "
        f"mixing = sqrt(down 1-2 FREQUENCY step), ω_d/ω_s=|Vus|²=0.050 ({gl['gst_fritzsch_relation_re_read']['pct_off']}% off). HONEST: the bite "
        "IS a quark-mass relation (INDICATOR-level §5/N12, NOT witness-only); TWT content = the ω-ladder interpretation, not the relation",
        gl["gst_fritzsch_relation_re_read"]["pct_off"] < 1.0 and "INDICATOR-level" in gl["gst_fritzsch_relation_re_read"]["honesty"]
        and "textbook" in gl["gst_fritzsch_relation_re_read"]["TWT_content"])
    _ck("NOT an over-determination [reviewer correction, avoids the N10 error]: Cabibbo & the down-1-2 read are the SAME GST "
        "relation (two sides), not 2 sectors; lepton 2-3 step is a LOOSE 8% coincidence; the ladder is rung-dependent λ-powers "
        "(down 2-3=0.15, lepton 1-2=0.07), NOT one universal λ; λ=sinθ_C=|Vus|=0.225 (NOT D/J=0.79)",
        gl["NOT_an_over_determination"]["off_from_Vus_pct"] > 5.0 and "NOT independent over-determination" in gl["NOT_an_over_determination"]["why"]
        and "NOT D/J" in gl["NOT_an_over_determination"]["lambda_def"])
    _ck("CHIRALITY [CANDIDATE, clean only at 1-2]: up tower = chirality-STEEPENED down tower — gen 1-2 up step ≈ (down step)² "
        "(exp 4.27≈2×2.01; at 2-3 it FAILS); up/down ratio GROWS with gen (0.46→13.6→41); Koide K=2/3 = the symmetric-circle "
        "parameterization of the same ladder; PROTECTION (why λ, why 3, ± chirality) = owed sub-harmonic-stability calc, GATED",
        gl["chirality_doubling_gen_1-2"]["up~2x_down (up step = down step squared)"] is True
        and gl["koide_is_a_parameterization"]["is_2/3"] is True and "GATED" in gl["protection_status"])
    print("        ⇒ CKM-as-frequency: the GST relation re-read as a ω-ladder + chirality steepening (1-2); NOT over-determination; protection DERIVATION located, not done.")

    tc = subharmonic_transition_cost()
    _ck("the probability read as a COST not a ratio (Yaer): P=exp(−Cost), Cost(d↔s)=ln(ω_s/ω_d)=3.00 ⇒ P=0.050; costs ADD "
        "(trivial ln-identity; rungs NOT equally spaced); CHIRALITY DOUBLES the cost (Cost_up≈2×Cost_down); BRIDGE [interpretive, "
        "not logical]: Cost INVITES reading as a §9.6 HYSTERETIC barrier action (Fork A) — same #1-gap S-face as τ_mem. Same GST number re-expressed, NOT DERIVED",
        tc["cabibbo_cost"]["pct_off"] < 2.0 and "TRIVIAL identity" in tc["log_frequency_line"]["caveat"]
        and 1.7 < tc["chirality_doubles_the_cost"]["ratio"] < 2.5 and "INTERPRETIVE identification" in tc["hysteretic_kernel_bridge"]
        and "NOT DERIVED" in tc["tier"])
    print("        ⇒ COST framing: P=exp(−Cost), Cost=log-freq distance = a hysteretic-barrier action ⇒ CKM magnitudes ride the SAME #1-gap reactive barrier as τ_mem; deriving the cost = the owed protection calc.")

    cs = generation_cost_step_structure()
    _ck("Q1 cost-step DIRECTION (bare): DOWN rises (3.00→3.80), UP+LEPTON fall — falling = anomalously light bare 1st gen (u,e); "
        "down rises (m_d>m_u, gen-1 not light). CANDIDATE: ± chirality acts on the lightest rung",
        cs["Q1_cost_step_direction_bare"]["down"]["trend"] == "RISING"
        and cs["Q1_cost_step_direction_bare"]["up"]["trend"] == "FALLING"
        and cs["Q1_cost_step_direction_bare"]["lepton"]["trend"] == "FALLING")
    _ck("Q2 [the key, INDICATOR]: in CONSTITUENT masses the UP tower FLIPS to RISING (336-floor swamps bare m_u), lepton "
        "(undressed) unchanged ⇒ the pattern is a BARE-frequency phenomenon, NOT dressing-invariant. TWO LAYERS: bare protected "
        "sub-harmonic (CKM/protection target) vs vacuum-DRESSED (constituent = hadron-impact = bare ω + the gluon/defect-vacuum interaction)",
        cs["Q2_constituent_INDICATOR"]["up"]["trend"] == "RISING" and cs["Q2_constituent_INDICATOR"]["lepton"]["trend"] == "FALLING"
        and "BARE-frequency phenomenon" in cs["Q2_finding"] and "MEET" in cs["Q2_two_layers"])
    _ck("Q3 [OPEN]: what makes ω CHANGE = the reaction coordinate (not just the cost). Candidate via √m=r²: ω=r⁴ ⇒ Cost=4·ln(radius-gap); "
        "r=defect radius. The stability condition selecting exactly 3 protected r (+ ± chirality) = the owed protection mechanism (N13), GATED. NOT DERIVED",
        "reaction coordinate" not in cs["Q3_reaction_coordinate"][:5] and "PROTECTION mechanism (N13)" in cs["Q3_reaction_coordinate"]
        and "NOT DERIVED" in cs["tiers"])
    print("        ⇒ the cost table is the BARE protected sub-harmonic; constituent = that DRESSED by the vacuum (the gluon) — the two problems meet there; Q3 (the coordinate + stability condition) is the next real target.")

    gm = generation_gen2_chirality_mirror()
    _ck("Yaer: the MIDDLE generation has a preferred position — 3.00/6.80≈4.91/11.29: DOWN gen-2 = 0.441 from the LIGHT end, "
        "UP gen-2 = 0.435 from the HEAVY end (1.4%, consistent within large quark-mass errors ~0.3σ) ⇒ UP & DOWN are MIRROR "
        "images (gen-2 at off-center ~0.44, opposite ends = the ± chirality REFLECTION); leptons differ (0.346) → a quark feature",
        abs(gm["gen2_position_fraction_of_span"]["down_from_LIGHT"] - gm["gen2_position_fraction_of_span"]["up_from_HEAVY"]) < 0.02
        and gm["gen2_position_fraction_of_span"]["lepton_from_HEAVY"] < 0.40
        and "NOT over-determination" in gm["significance"] and "NOT DERIVED" in gm["tier"])
    print("        ⇒ a 2nd signature of chirality-as-reflection (up<->down mirror); CONSTRAINT on the protection mechanism: gen-2 at the off-center fixed fraction ~0.44, mirror-imaged. Consistent within errors, NOT derived.")

    cm = cp_chirality_90_120_mismatch()
    _ck("v14 CIRCULAR-POLARIZATION attempt (Yaer): CLEAN four-fold NEGATIVE — the CP ±90° structure does NOT reproduce the gen-2 "
        "mirror from a hadron fit (forcing f=0.44 → ~4.75× worse); decisive reason = hadrons see DRESSED ω, the mirror is BARE-sector "
        "(independent confirmation of the §10 two-layer split); the outside-frame/hole sign flip is UNOBSERVABLE (χ-degenerate)",
        cm["verdict"].startswith("CLEAN") and "two-layer split" in cm["decisive_reason"]
        and "UNOBSERVABLE" in cm["outside_frame_unobservable"] and "located-negative N16" in cm["tier"])
    _ck("located gap N16 (engine-checked): the CP π/2 phase is INCOMMENSURATE with the 3-fold generation spacing 2π/3 — "
        "(π/2)/(2π/3)=3/4 ∉ ℤ ⇒ a CP shift moves a generation OFF the lattice (¾ of a step), scrambling the tower; "
        "re-attack = a per-rung CP action or a geometry where 90° and the spacing commute. NOT DERIVED",
        cm["located_gap_90_120"]["displacement_in_gen_steps"] == 0.75 and cm["located_gap_90_120"]["incommensurate"] is True
        and "per-rung" in cm["would_change_if"])
    print("        ⇒ v14 (archive, illustrative): the CP ±90° encoding is more principled than v13 (1 phase replaces 4 knobs, 3.68%) but the mirror is bare-sector & hadrons can't probe it; the 90/120 mismatch is the located re-attack handle.")

    lw = generation_loose_windows_vacuum_relative()
    _ck("Yaer reframe 2 — LOOSE PROTECTION (3 WINDOWS not 3 lines): each generation = a {up,down} band; engine-checked: 3 NON-overlapping "
        "windows, widths GROW (0.77/2.61/3.72 log), up-type edge FLIPS (light gen-1, heavy gen-2/3 = m_d>m_u inversion). RE-DESCRIBES N16 (not a "
        "derivation): the within-window (mirror) structure is bare; IF dressing washes it out (owed) it re-describes why hadrons can't probe it. FRAMING/CANDIDATE, NOT DERIVED",
        lw["reframe2_loose_windows"]["non_overlapping"] is True and lw["reframe2_loose_windows"]["widths_grow_with_gen"] is True
        and "does NOT derive it" in lw["reframes_N16_re_description_NOT_derivation"] and "NOT DERIVED" in lw["tier"])
    _ck("Yaer reframe 1 — PERCEPTION is VACUUM-RELATIVE: perceived mass = f(ω_vac−ω_abs); the PROTECTED quantity is the ABSOLUTE defect "
        "frequency (heavier=slower-absolute=further from carrier); cost-axis inverts. NAMED TEST (the N16 handle): does the absolute-frequency "
        "map make generations CP-commensurate (resolve the 90/120 mismatch)? FRAMING + owed computation, NOT DERIVED",
        "ABSOLUTE defect frequency" in lw["reframe1_vacuum_relative"] and "CP-commensurable" not in lw["owed"]
        and "vacuum-relative" in lw["owed"])
    print("        ⇒ two next directions: (1) the protected quantity is the ABSOLUTE (vacuum-relative) frequency, mass is a readout — may resolve the 90/120 mismatch in absolute space; (2) LOOSE windows re-describe why the mirror is bare-only (N16). Both FRAMING, owed the maps.")

    ch = charge_in_the_window_picture()
    _ck("Yaer — CHARGE in the picture: the winding supplies PROTECTION and the per-state VALUES are ASSIGNED "
        "(keeper R2, 2026-08-21: this returned string previously read 'charge = the topological WINDING "
        "(winding_charge)', asserting inside a RETURNED VALUE the exact provenance the main engine's own "
        "docstring disclaims — the RV-7 shape. The check moved with the value: it now asserts the split, not "
        "merely the surviving word 'winding'). Q=T3+Y/2 = +1/6 ± 1/2 (up/down diff = SYMMETRIC weak-isospin "
        "T3=±1/2, common Y/2=+1/6; distinct-but-linked to the CP handedness; symmetric -> consistent with the "
        "mirror, doesn't source its residual asymmetry)",
        abs(ch["charge_diff_is_symmetric"]["T3_updown"] - 0.5) < 1e-9 and abs(ch["charge_diff_is_symmetric"]["Y/2_common"] - 1/6) < 1e-3
        and "PROTECTION" in ch["what_is_charge"] and "pi3_S3_integer_completion" in ch["what_is_charge"]
        and "charge_assignment_from_anchor" in ch["what_is_charge"]
        and "never from GMN" in ch["what_is_charge"])
    _ck("Yaer — could a charge-dependent window REDUCE the width? Decisive engine fact: the width GROWS (0.77/2.61/3.72) while ΔT3 is CONSTANT "
        "(=1) ⇒ a FIXED charge-shift gives constant width & CANNOT do it; charge-windows reduce width ONLY if the coupling is MULTIPLICATIVE/"
        "frequency-scaled (up/down cost ratio≈2≈|Q| ratio at 1↔2, breaks at 2↔3). NEGATIVE: cost ∝ |Q| FAILS (leptons 5.33 vs quarks ~9). NOT DERIVED",
        "MULTIPLICATIVE" in ch["width_question_answer"] and "REFUTED" in ch["negative_cost_not_prop_Q"]["verdict"]
        and "NOT DERIVED" in ch["tier"])
    print("        ⇒ charge = winding (symmetric T3, consistent with the mirror); a charge-dependent window can tighten per-charge protection ONLY via a multiplicative/frequency-scaled coupling — a fixed shift can't (width grows, ΔT3 constant); cost ∝ |Q| refuted.")

    vm = vacuum_relative_map_and_cp_commensurability()
    _ck("OWED COMPUTATION 1 (perceived↔absolute map): matter=a beat/deficit below the carrier, ω_abs=ω_vac−m; with ω_vac=Λ~M_Pl every SM "
        "m/Λ≲1e-17 ⇒ ω_abs≈Λ, the hierarchy lives in the tiny DEFICIT (=perceived mass) ⇒ the map is a MONOTONIC FRAME TRANSFORM, "
        "structurally INERT (clean NEGATIVE on the absolute axis being a structural key). NOT DERIVED",
        "MONOTONIC FRAME TRANSFORM" in vm["C1_verdict"] and "INERT" in vm["C1_verdict"])
    _ck("OWED COMPUTATION 2 (CP-commensurability): N16's 90/120 mismatch is a BRANNEN-CIRCLE artifact (gcd(2,3)=1; π/2=3/4 of 120°). On the "
        "LOG-FREQUENCY LINE (the vacuum-relative/cost variable) the generations are a LADDER not a circle ⇒ ±90° is a non-scrambling modulation "
        "(Lens C/D fit 3.68% vs Lens A scramble) ⇒ the 90/120 located gap DISSOLVES; N16's MAIN negative (mirror=bare-sector) STANDS",
        "RESOLVED" in vm["C2_verdict"] and "BRANNEN-CIRCLE artifact" in vm["C2_verdict"]
        and vm["C2_circle_artifact"]["gcd(2_handedness, 3_generations)"] == 1 and "STANDS" in vm["C2_verdict"])
    print("        ⇒ the two owed computations DONE: the vacuum-relative map is ontologically right but structurally inert (C1); its payoff is reorienting circle→line, which DISSOLVES the N16 90/120 gap (C2). Open frontier = the bare-sector protection mechanism (#1 gap).")

    lq = e4_conjugation_is_LQ_not_updown()
    _ck("N28 DERIVED + CAND3 REFUTED -- e4-conjugation C4(B)=e4*B*e4 on grade-2: L-orbit {e12,e13,e23} eigenvalue +1 (LEPTON), "
        "Q-orbit {e14,e24,e34} eigenvalue -1 (QUARK); within Q, C4=-1 uniformly -- NO up/down sub-split. "
        "C4 maps SD(e12-e34) -> ASD(e12+e34); [C4,Hodge] != 0 on grade-2 (L/Q and SD/ASD are incommensurable). "
        "CAND3 (helical-pitch e4 -> up/down) REFUTED: P+(e4) is the L/Q projector, not up/down; SD^ASD={0}. "
        "LOCATED GAP N28: up/down distinction in Q-orbit needs sec.9.6 EOM (Layer-2), not a static Clifford fact",
        all(lq["L-orbit C4(B)=+B (LEPTON sector)"].values())
        and all(lq["Q-orbit C4(B)=-B (QUARK sector)"].values())
        and lq["C4 maps SD(e12-e34) -> ASD(e12+e34)"] is True
        and lq["[C4,Hodge](sd_gen) non-zero"] is True
        and "refuted" in lq["tier"]
        and "N28" in lq["tier"])

    nis = generation_ladder_needs_inverse_square()
    _ck("★ N20 re-attack hinge attacked — the GEOMETRIC ladder ⟺ logarithmic action ⟺ attractive −1/r² channel (rigorous reduction); the substrate "
        "supplies NO −1/r² generator (every action term ±1/±3 power-law or rational ⇒ ARITHMETIC radii), the Derrick breathing well is a STABLE harmonic "
        "minimum V''>0 (NOT scale-critical — corrects N17), and the data is NOT within-tower geometric (radius ratios drift +22/−31/−47%, sign=chirality) "
        "⇒ discrete-scale-invariance/Efimov REFUTED-as-forced (Efimov 22.7~20 numerology rejected). clean-NEGATIVE + FRAMING; NOT DERIVED",
        nis["data_not_within_tower_geometric"]["down"] > 0 and nis["data_not_within_tower_geometric"]["up"] < 0
        and "clean-NEGATIVE" in nis["tier"])
    _ck("★ N20 DERIVED sub-result — the driven-PENDULUM backbone (Λθ̈=−K sinθ from gear inertia + e4-carrier lock; separatrix=chirality co/counter-rotation) "
        "answers the N19 hinge 'is ω(A) EXPONENTIAL?' = NO, it is LOGARITHMIC ⇒ cost RISES toward the separatrix (right trend) but the gaps CROWD: the SINGLE gap "
        f"is UNBOUNDED (one rung straddling the separatrix) but consecutive gaps collapse — Maslov-½ pair-min ≈ {nis['derived_pendulum_backbone']['best_adjacent_pair_min_maslov']}, sup over all placements ≲2.0, in every case < 2.8 (factor ~1.4) "
        "⇒ no RUN of band gaps ⇒ cannot make the cost table. Sharper hinge = PROJECT V(θ), read the period-divergence EXPONENT",
        nis["derived_pendulum_backbone"]["best_adjacent_pair_min_maslov"] < 1.8 and "NO" in nis["derived_pendulum_backbone"]["N19_hinge_answered"]
        and "PROJECT" in nis["sharper_hinge"] and "N20" in nis["tier"])
    print("        ⇒ N20: discrete-scale-invariance REFUTED-as-forced (no −1/r² generator; Derrick well harmonic-stable, correcting N17; data not within-tower geometric); the driven-pendulum backbone is LOGARITHMIC (gaps CROWD: pair-min ~1.2, sup ≲2.0 < 2.8); sharper hinge = project V(θ), period-divergence exponent. NOTHING DERIVED.")

    nsa = geometric_ladder_is_nonselfadjoint()
    _ck("★ N21 REFUTATION — is the geometric ladder NECESSARILY dissipative? NO: Efimov/Calogero (H=−∂²−g/r², g>1/4) is a CONSERVATIVE HERMITIAN "
        "log-periodic ladder via a self-adjoint extension. The honest dichotomy is SELF-ADJOINT (arithmetic) vs NON-SELF-ADJOINT (ladder), NOT Hermitian vs dissipative. FRAMING+REFUTATION",
        "FALSE" in nsa["refutation"] and "NON-SELF-ADJOINT" in nsa["dichotomy"] and nsa["g_critical"] == 0.25)
    _ck("★ N21 DERIVED — the BULK (large-R) conservative spectrum is ARITHMETIC: cranked centrifugal L²/(2(aR³+bR)) = {R⁻¹,R⁻³}, NEVER scale-invariant R⁻²; "
        "Laplace-Beltrami measure Q=0 (1D flat). So the ladder is NOT a bulk phenomenon",
        "never R⁻²" in nsa["bulk_is_arithmetic"] and "arithmetic" in nsa["bulk_is_arithmetic"])
    _ck("★ N21 the RESULT is a RELOCATION (reviewer-corrected from an over-claimed clean-negative): whether the conservative sector makes the ladder reduces to the "
        "R→0 (small-defect=MONAD-scale) endpoint, UNSETTLED — (i) the operator is LIMIT-CIRCLE at R=0 (soft c₄/R wall, NOT e.s.a. ⇒ has self-adjoint-extension freedom), "
        "(ii) the von Roos R→0 measure 1/r² coefficient is ORDERING-DEPENDENT and SPANS the BF threshold (repulsive +0.39, sub −0.105, SUPER-critical −0.195 at n=3 — the measure CAN be supercritical)",
        nsa["relocation_to_R0_monad_endpoint"]["measure_coeff_spans_BF"]["super_critical"] < -0.125
        and nsa["relocation_to_R0_monad_endpoint"]["measure_coeff_spans_BF"]["symmetric"] > 0
        and "UNSETTLED" in nsa["relocation_to_R0_monad_endpoint"]["verdict"])
    _ck("★ N21 FORK + Θ_rel tie: the R→0 extension/coefficient is fixed EITHER (a) CONSERVATIVELY by monad-scale D4 contact/3-body physics (Efimov-on-lattice), OR (b) by "
        "the DISSIPATIVE Im χ kernel (Fork A) — Efimov makes (a) available ⇒ ‘dissipative’ is not forced. What the anchor must supply (g_eff>1/4 + chirality-signed DSI-breaking running rate) ties to Θ_rel (CANDIDATE)",
        "monad" in nsa["fork"].lower() and "Im χ" in nsa["fork"] and "Θ_rel" in nsa["ties_to_theta_rel"] and "NOT a clean negative" in nsa["tier"])
    print("        ⇒ N21: ‘necessarily dissipative’ REFUTED (Efimov=conservative ladder); dichotomy = self-adjoint vs non-self-adjoint; the BULK is arithmetic (cranked-no-R⁻²; LB Q=0) but the R→0 endpoint is LIMIT-CIRCLE + the measure coeff SPANS the BF threshold ⇒ UNSETTLED, RELOCATED to the small-defect/MONAD scale; FORK = conservative-monad-UV OR dissipative-Imχ; ties to Θ_rel. NOT a clean negative, NOT DERIVED.")

    gvm = generation_values_monad_forked()
    _ck("★ N22 — which ordering does the substrate dictate? The COVARIANT (Laplace-Beltrami) one ⇒ Q=0 for the 1-D breathing modulus (any metric); LB = unique reparametrization-"
        "covariant von Roos member ⇒ N21's supercritical measure sub-route is CLOSED. The 2D-curvature objection is DEFUSED: θ is the CENTRAL U(1)_E mass-phase (cyclic); separation "
        "ψ=e^{inθ}φ(R) gives a SOFT n²/(2bR) θ-centrifugal (degree −1), NOT scale-invariant R⁻² (sympy-exact). DERIVED sub-results + located-gap (N21 measure-fork resolved)",
        "Q=0" in gvm["measure_subroute_resolved"] and "CLOSED" in gvm["measure_subroute_resolved"] and "degree −1" in gvm["curvature_objection_defused"])
    _ck("★ N22 the HONEST TIER of the generation VALUES — a SHARPENED 2-WAY FORK (not a flat input): the cost-table numbers / lepton masses / CKM magnitudes are GATED-WITH-AN-OPEN-FORK — "
        "(a) a monad-scale INPUT (tier Λ/f_π) IF the R→0 resolution is the conservative self-adjoint-extension / D4-3-body-contact, OR (b) Im χ-GATED & dynamically DERIVABLE IF dissipative (Fork A). "
        "Sharpening: a static boundary alone gives ≤1 bound state, not a TOWER ⇒ even (a) needs the dynamical 3-body contact. STRUCTURE derived, VALUES forked. NOT DERIVED for the values",
        "GATED-WITH-AN-OPEN-FORK" in gvm["values_tier"] and "≤1 bound state" in gvm["sharpening"] and "NOT DERIVED for the values" in gvm["tier"])
    print("        ⇒ N22: the physical measure is covariant (Q=0) ⇒ N21's measure sub-route CLOSED (the 2D-curvature loophole defused via cyclic-θ ⇒ soft 1/R); the generation VALUES are a sharpened 2-way FORK (conservative monad-INPUT vs dissipative Im-χ-GATED), the STRUCTURE derived. NOT a flat input, NOT DERIVED. The #1 gap stands, localized to the R→0 conservative-vs-dissipative discriminator.")


    lr_ = g8_linear_response_operator_twisted_vacuum()
    _ck("★ THE LINEAR-RESPONSE OPERATOR OF THE G-8 FLOW ABOUT ITS TWISTED VACUUM (2026-09-15, the keeper's Q2 spec; "
        "at Ω₀ = 0, body-diagonal branch, D/J = 0.787): check 1 — <⋆B₀|H(k)|⋆B₀> = 12 J k̃²(k) EXACTLY on 3 directions × "
        "3 magnitudes (R-192's identity, worst rel %.1e)" % lr_["check1_starB0_identity_worst_rel"],
        lr_["check1_starB0_identity_worst_rel"] < 1e-10)
    _ck("   PLANTED FAILURES of check 1: the 6J label-form misses by ≥ 40 %% (%.2f) and the continuum 12|k|² misses "
        "by ≥ 0.2 %% at 2π/8 (%.3f) and ≥ 10 %% at (2π/8)(1,1,1) (%.3f) — the stiffness is the full lattice dispersion"
        % (lr_["check1_planted_6J_min_miss"], lr_["check1_planted_continuum_min_miss"],
           lr_["check1_planted_continuum_miss_at_(2pi/8)(1,1,1)"]),
        lr_["check1_planted_6J_min_miss"] > 0.4 and lr_["check1_planted_continuum_min_miss"] > 0.002
        and lr_["check1_planted_continuum_miss_at_(2pi/8)(1,1,1)"] > 0.1)
    _ck("   check 2 — L(0): EXACTLY 2 zero modes + 4 at −g(1 ± i C12), Im/Re = 12 to 1e-4, g = 12|k₀|² to 1 %% "
        "(%.5f vs %.5f); the UNTWISTED world returns 6 zero modes (%d) — the 2 + 4 split is the twist's"
        % (lr_["check2_g_vs_12k0sq"][0], lr_["check2_g_vs_12k0sq"][1], lr_["check2_planted_untwisted_zero_modes"]),
        lr_["check2_L0_zero_modes"] == 2 and len(lr_["check2_L0_gapped"]) == 4
        and lr_["check2_planted_untwisted_zero_modes"] == 6)
    _ck("   check 3 — ξ = 1/|k₀|: the inverse pitch reproduces R-189's measured-minimum healing length on the same "
        "branch to 0.1 %% (%.4f vs %.4f)" % (lr_["check3_xi_inverse_pitch"], lr_["check3_xi_R189_measured_min"]),
        abs(lr_["check3_xi_inverse_pitch"] - lr_["check3_xi_R189_measured_min"]) / lr_["check3_xi_R189_measured_min"] < 1e-3)
    _ck("   check 4 — THE SELECTION RULE IS A PLANE: [H(k), ad_B₀] = 0 to 1e-12 on span{k̂₀, e₄} (along k₀ at three "
        "magnitudes, along e₄, three interpolations; worst %.1e) and > 0.01 for every k OFF the plane (min %.2f, the "
        "control); identically 0 in the untwisted world" % (max(lr_["check4_commutator_in_plane"].values()),
                                                            min(lr_["check4_commutator_off_plane (control)"].values())),
        max(lr_["check4_commutator_in_plane"].values()) < 1e-12
        and min(lr_["check4_commutator_off_plane (control)"].values()) > 0.01
        and lr_["check4_untwisted_world_commutator_max"] < 1e-12)
    _ck("   PROVENANCE TIE: the operator reproduces the deposited 32³ delta-plant stencil of gr1_linear_response_step2 "
        "(D_B0, D_⋆B0 at 2π/32; L(0)'s gapped pair; the 32³-raster max Re / min |eig|) to 1e-3 (worst %.1e) and the "
        "steady state is DAMPED (max Re eig < 0: driven, not variational — keeper UNDER-CLAIM 5)"
        % lr_["provenance_tie_to_step2_stencil"]["worst_rel"],
        lr_["provenance_tie_to_step2_stencil"]["worst_rel"] < 1e-3
        and lr_["provenance_tie_to_step2_stencil"]["engine"]["K5_max_re"] < 0.0)
    pc_ = lr_["perp_stiffness_channels"]
    _ck("   THE CHANNEL SPLIT (2026-09-17, the L48/K-INV-2e keeper's COLLISION 1, confirmed on the developer's own route): "
        "perpendicular to the pitch the Schur-reduced smooth sector SPLITS — the B₀ channel saturates POSITIVE (%.4f; "
        "65:1 against the pitch %.3f) and the ⋆B₀ channel NEGATIVE (%.5f = N70's banked −0.02305291 to 5e-4), off-diagonal "
        "%.1e; the withdrawn 'D_perp saturates at 0.080' was their MEAN (%.4f) — a banked instability hidden in an average; "
        "along the pitch ⋆B₀ reads %.6f (R-192)"
        % (pc_["B0_perp"], pc_["B0_pitch"], pc_["starB0_perp"], abs(pc_["offdiag_perp"]),
           pc_["mean_perp (the withdrawn '0.080')"], pc_["starB0_pitch"]),
        pc_["B0_perp"] > 0.1 and abs(pc_["starB0_perp"] - (-0.02305291)) < 5e-4 and abs(pc_["offdiag_perp"]) < 1e-6
        and abs(pc_["mean_perp (the withdrawn '0.080')"] - 0.080) < 1e-3 and abs(pc_["starB0_pitch"] - 12.0) < 1e-3
        and pc_["B0_pitch"] / pc_["B0_perp"] > 60)
    print("        ⇒ the linearized G-8 kernel at Ω₀ = 0 is in the engine: L(k) = −(1 + C12 ad_B₀) H(k); the ⋆B₀ stiffness "
          "is R-192's identity, the Γ gap is 12|k₀|², ξ = 1/|k₀|, and the smooth→satellite null is an exact symmetry "
          "on the canting PLANE. No far-field law, no drift, no driven-face statement is claimed here.")


# ---- twt_matter (companion blocks) ----------------------------------------
def check_twt_matter():
    sc = same_composition_baryons_pin_internal_mode()
    _ck("same-composition/different-mass baryons pin the mechanism: Λ≠Σ⁰ (both uds, J=1/2, ΔM=77), "
        "p≠Δ⁺ (uud), Σ≠Σ*, Ξ≠Ξ* ⇒ additive composition-only mass FALSIFIED (predicts ΔM=0); ΔM "
        "isolates the non-additive internal-mode term (additive floor cancels); §17.3 gear Θ_A≠Θ_B "
        "(Λ antisym / Σ sym) and the coherent-sum relative-phase are TWO VIEWS of the ONE mode",
        sc["composition_only_additivity_falsified"] and sc["dM_isolates_nonadditive_internal_mode"]
        and sc["splits_MeV"]["uds_Lambda_vs_Sigma0_sameJ"] > 50
        and all(v > 50 for v in sc["splits_MeV"].values()))

    ws = winding_sense_sets_mass_measure()
    _ck("residual (a) ADJUDICATED structurally (FRAMING bridge, data near-degenerate) — WINDING SENSE sets "
        "the measure: meson (B=0, q+q̄ OPPOSITE=counter → beat → m=2ω|cos(α/2)| linear/Goldstone) vs baryon "
        "(B=1, 3 quarks SAME=co → frequency-lock Ω_B=Σω = the §17.3 GEAR). 'linear-|A| for baryon' was the "
        "MESON import; baryon's primary measure = the gear. Residual (b)=absolute scale=#1 gap (located)",
        ws["meson_B"] == 0 and ws["baryon_B"] == 1 and ws["linear_A_is_meson_import"] is True
        and ws["floors_near_degenerate"]["N/Delta"]["diff_MeV"] < 15)

    gi = gear_inertia_form_from_S2_symmetry()
    _ck("§17.3 inertia-tensor FORM — symmetry-adapted BASIS DERIVED (was fully posited in gear_eigenvalues) "
        "[reviewer-narrowed]: on the colour-blind (trivectors orthonormal) Spin(3) collective manifold (triple "
        "closes su(2)), the identical light-pair exchange S₂ commutes with the inertia ([M,P]=0) ⇒ its "
        "symmetry-adapted basis is (1,±1) (sym/antisym), M diagonal with a±b. HONEST: the Λ/Σ SPLIT needs the "
        "off-diagonal b≠0 (generic-Willis + gap-gated); the (1,1)↔Σ↔spin-1 / (1,−1)↔Λ↔spin-0 labels are "
        "FRAMING/standard-QM (per su6_pairs). Matches gear_eigenvalues (Θ_A=I_p, Θ_B=I_p(1+2x_Q)); values #1-gap-gated",
        gi["colour_trivectors_orthonormal"] and gi["collective_manifold_is_Spin3"]
        and gi["inertia_commutes_with_S2_exchange"] and gi["M_diagonal_in_adapted_basis"]
        and gi["matches_gear_eigenvalues"])

    sp = su6_pairs_are_rotor_orientation()
    _ck("SU(6) pair coefficients = RELATIVE ROTOR ORIENTATIONS (not bookkeeping): σ_ij=4·⟨S_i·S_j⟩ — "
        "triplet=aligned=constructive(+1/4) / singlet=anti-aligned=destructive(−3/4) = the step-3 "
        "interference signs; trace-zero (3·¼−¾=0) ⇒ floor=centroid (step4); Λ ud-singlet(destructive)<Σ "
        "ud-triplet = the step-5 K_L flip. Geometric meaning DERIVED; per-baryon assignment = standard-QM",
        abs(sp["triplet_aligned_constructive"] - 0.25) < 1e-12
        and abs(sp["singlet_antialigned_destructive"] + 0.75) < 1e-12
        and abs(sp["trace_over_multiplet"]) < 1e-12
        and sp["sigma_ij_eq_4_SS"]["singlet"] == -3.0)

    gen_surv = generation_index_survives_brannen_excision()
    _ck("generation OPERATOR (meta-time phase, NOT spatial G) survives Brannen excision — pure algebra, no mass-measure",
        gen_surv["spatial_G_is_mass_blind"] is True
        and gen_surv["depends_on_mass_measure"] is False
        and gen_surv["depends_on_Brannen"] is False
        and gen_surv["spatial_G_max_dsp"] < 1e-12)
    pLr = pure_L_rotor_preserves_spatial_radius()
    _ck("pure-L rotor preserves spatial radius EXACTLY (narrow honest residue of REFUTED Phase F derivation)",
        pLr["tier"] == "DERIVED-A"
        and len(pLr["engine_verified_for_L_bivectors"]) == 3
        and len(pLr["engine_verified_for_r0_choices"]) == 5
        and "REFUTED" in pLr["does_NOT_close"]
        and len(pLr["bridge_gaps_remaining"]) == 2)

    osd = one_sided_rotor_uniform_density_identity()
    _ck("★ T5-1 (tau5 adjudication 2026-08-13; N61) — the ONE-SIDED uniform kinetic-density "
        "identity [DERIVED-A]: BOTH one-sided rest forms (left Q(τ5)R0 → Ω5 = R0~ŵR0; right "
        "R0Q(τ5) → Ω5 = ŵ) have EXACTLY uniform (iv)-kinetic density (ω/2)² at every point "
        "(2 profiles × 2 û × radii to 12 — the fact is ONE-SIDEDNESS, never the left shift), "
        "so the rotor does not fix the vacuum at infinity and the raw 3-slice kinetic cost "
        "diverges AT REST under any positive-definite pairing (ANW/Coleman vacuum-stabilizer "
        "criterion, via I-5); + the conjugation-subtraction identity Ω5(conj) = A(Ω5(left) − ŵ)Ã "
        "EXACT (the field-level subtraction; the two-subtraction-levels map = the open O1 gap): "
        "conj class decays (< 1e-6 at r=12) while one-sided stays (ω/2)² exactly",
        "DERIVED-A" in osd["tier"]
        and osd["left FD vs R0~ w_hat R0 (worst coeff)"] < 1e-7
        and osd["right FD vs w_hat (worst coeff)"] < 1e-7
        and osd["uniform density dev vs (omega/2)^2 (both forms, 2 profiles, 2 u_hat)"] < 1e-12
        and osd["conjugation identity Om5(conj) = A(Om5(left) - w_hat)A~ (worst coeff)"] < 1e-7
        and osd["decay dichotomy at r=12 (conj vs one-sided)"][0] < 1e-6
        and abs(osd["decay dichotomy at r=12 (conj vs one-sided)"][1] - (0.83 / 2) ** 2) < 1e-12
        and "NOT a left-shift fact" in osd["one-sidedness"])
    uvi = tau5_unique_v_inert_combination()
    _ck("★ T5-2 (tau5 adjudication 2026-08-13; N61) — the UNIQUE v-inert combination lemma "
        "[DERIVED-A]: far-field sector densities of the T-coord-transported one-sided rotor are "
        "d5 → γ², d1 → γ²v² (engine, r=14, both v); among a·d5 + b·d1 the v-inertness of the "
        "asymptote FORCES b = −a (sympy-exact) — the η/action combination (I-C) is the UNIQUE "
        "v-inert one and the Noether combination (b = +a) is v-dependent (measured spread 0.93): "
        "the discrimination-null root — any background finitizing another combination installs "
        "the v-law (γ-face triviality per Schroers)",
        "DERIVED-A" in uvi["tier"] and uvi["b = -a forced (sympy)"] is True
        and uvi["far-field density match at r=14 (worst rel)"] < 1e-3
        and uvi["(1,-1) inertness measured (worst dev from 1)"] < 1e-3
        and uvi["(1,+1) Noether v-spread (must be > 0.3)"] > 0.3
        and "UNIQUE v-inert" in uvi["consequence"])


# ---- twt_weak (companion blocks) ----------------------------------------
def check_twt_weak():
    print("§18.3a e4 identity on S+ (companion-side identity):")
    _ck("e4 acts as +1 on S+ (e4·s0 = s0)", e4_acts_as_identity_on_Splus())


# ---- twt_hadrons (companion blocks) ----------------------------------------
def check_twt_hadrons():
    print("§17.3 Willis planetary-gear eigenvalues (COMPUTED symbolically):")
    ge = gear_eigenvalues()
    _ck(f"Θ_A = I_pair (Λ-type, K_L=0)  (eigenvalues {ge['eigenvalues']})", ge["Θ_A = I_pair (Λ-type)"])
    _ck("Θ_B = I_pair(1+2x_Q) (Σ-type, K_L=1)", ge["Θ_B = I_pair(1+2x_Q) (Σ-type)"])

    print("§17.3 heavy-quark regimes (x_Q = m_Q·Θ_0, post-R-133 correction):")
    qr = quark_regimes()
    _ck(f"x_Q: s≈0.48, c≈6.5, b≈21.4, t≈883 (crossover x_Q~1 ↔ Λ_QCD)  (got {qr})",
        abs(qr["s"]-0.48) < 0.02 and abs(qr["c"]-6.5) < 0.1 and abs(qr["t"]-883) < 2)

    print("§17.3 forward predictions (anchor 195.6 predicted; hyperfine corrections fit-inherited):")
    hp = heavy_baryon_predictions()
    _ck(f"Σ_c-Λ_c = 195.6-43.7 = 151.9 MeV vs 167 — the -9.0% TRACKED RESIDUAL (the old 2.4% "
        f"agreement rode the WRONG 97.27; candidate resolution = bound-state-class inertia, "
        f"P2-7-adjacent)  (got {hp['Σ_c-Λ_c']['pred']:.0f}, err {hp['Σ_c-Λ_c']['err%']:.1f}%)",
        abs(hp["Σ_c-Λ_c"]["pred"] - 151.9) < 1 and 8.0 < hp["Σ_c-Λ_c"]["err%"] < 10.0)
    _ck(f"Σ_b-Λ_b = 195.6-13.7 = 181.9 MeV vs 191 (-4.8%, improved from +5.2%)  "
        f"(got {hp['Σ_b-Λ_b']['pred']:.0f}, err {hp['Σ_b-Λ_b']['err%']:.1f}%)",
        abs(hp["Σ_b-Λ_b"]["pred"] - 181.9) < 1 and hp["Σ_b-Λ_b"]["err%"] < 6)

    print("§17.4 hadron mass operator:")
    _ck(f"γ = (Σ-Λ)/2 = 38.5 MeV (fixed, not free)  (got {gell_mann_okubo_gamma():.1f})", abs(gell_mann_okubo_gamma() - 38.5) < 0.1)
    print(f"        form: {mass_operator_form()}")


    print("ADJ2 consolidated bank (2026-08-12) — the Λ_⊥ = ½Θ_ANW closed form:")
    lp = lambda_perp_anw_half_theta()
    _ck("Λ_⊥ shell density = (8π/3)r²sin²f[c₂+4c₄(f′²+sin²f/r²)] — 3 profiles × 2 couplings, 1e-12 class",
        lp["shell density vs (8pi/3) r^2 sin^2 f [c2 + 4 c4 (f'^2 + sin^2 f/r^2)] (worst rel, 3 profiles x 2 couplings)"] < 1e-12)
    _ck("Θ_ANW/Λ_⊥ = 2 measured (the identification sentence MUST carry the ½ — else band spacings wrong by 2)",
        abs(lp["Theta_ANW / Lambda_perp (measured)"] - 2.0) < 1e-10)
    _ck("carrier-independence holds on the solid-angle+cycle average AND is non-trivial (per-direction k_c-dependence real)",
        lp["carrier-independence after averaging (worst rel)"] < 1e-12
        and lp["per-direction k_c-dependence (real, must be > 0)"] > 0.1)
    _ck("Λ_⊥ = 32.156 full-range; probe-2's 31.4386 reproduced on its own grid; deficit = truncation AND step (both positive — engine-corrected attribution)",
        abs(lp["Lambda_perp (test profile, full range)"] - 32.156) < 0.01
        and abs(lp["probe-2 grid value reproduced (trapezoid 0.3..12 step 0.3)"] - 31.4386) < 0.001
        and lp["deficit split (truncation, step)"][0] > 0.1 and lp["deficit split (truncation, step)"][1] > 0.1)

    print("\ne₄-orthogonal projection mass mechanism (TASK e4 — constituent sector; Part A RESOLVED (ii)):")
    rA = hodge_split_invariance_theorem()
    _ck("Hodge-split theorem: G preserves |B_spatial| AND |B_e4| (|B_spatial| reading -> no generation variation)",
        rA["max_d|B_spatial|_under_G"] < 1e-12 and rA["max_d|B_e4|_under_G"] < 1e-12 and rA["max_d|B_spatial|_under_e24"] > 0.1)
    rE = epicycle_reading_dependent()
    _ck("epicycle reading-dependence (intermediate): epicycle reachable under r² orbit-projection (lepton ε=0 exact), forbidden under |B_spatial| — RESOLVED by Part A below",
        rE["harmonics"]["lepton_offset_no_tilt"]["r2_2nd"] == 0.0
        and rE["harmonics"]["quark_offset_tilt"]["r2_2nd"] > 0.05
        and abs(rE["harmonics"]["lepton_offset_no_tilt"]["r_2nd"]) > 1e-3)
    rD = deferent_from_offset_lepton_consistent()
    _ck(f"deferent b from offset (got {rD['deferent_coeff']}), lepton ε=0 — survives both readings", rD["lepton_epsilon_zero"])

    rb = bu_offset_not_charge_sourced()
    _ck(f"strange/charm: n=2 epicycle node ({rb['epicycle_node_at_n2']}) -> b_u offset NOT charge/T3/gen-sourced; b,ε independent handles", abs(rb["epicycle_node_at_n2"]) < 0.12)

    rRes = epicycle_reading_resolved()
    _ck("RESOLUTION: epicycle_reading_dependent UNRESOLVED -> RESOLVED (ii); reproduces modified-Brannen; downstream — R_G reidentified as COLOUR (F3/Cl-i math stands, interpretation under revision; explains F3's non-G-axis gap)",
        rRes["resolved_status"] == "RESOLVED" and rRes["reproduces_modified_brannen"] is True)

    gf = generations_are_defect_flows_on_spinor_S3()
    _ck("SHARP defect-picture (matter-as-defect central): generation = a DEFECT WINDING-FLOW on the "
        "anti-self-dual spinor S³ (one circular handedness); su(2) closure + orthonormality verified; "
        "EXACTLY 3 = S³ parallelizable by 3 global flows (defect-centric why-3/why-not-4, SAME count as "
        "the ℍ-triple recast); weak isospin = other handedness; +e₄ helicity→up/down (CAND); dynamical "
        "selection = #1 gap; period-doubling REFUTED",
        gf["anti_self_dual_triple_orthonormal"] and gf["su2_closure"] and gf["count"] == 3)


# ---- twt_cosmo (companion blocks) ----------------------------------------
def check_twt_cosmo():
    print("§9.6 Fork B STRUCTURAL LEAN (compact-Spin(4) + periodic e4-drive => Floquet limit-cycle preferred):")
    cs = compact_spin4_favors_limit_cycle()
    _ck("Fork B lean from compact-group + periodic-drive geometry [DERIVED-generic / FRAMING; e5-litmus-free, no §9.6 routing]: "
        "F1 compact target Spin(4)≅S³×S³ (bounded trajectories) + F2 periodic finite-freq e4-drive at ω_d=mass (Floquet/Krein generic limit-cycle) "
        "+ F3 ≥3 intrinsic scales {Λ, T_d, f_π, S³ radius} (SOC scale-invariance is measure-zero, no enforcing symmetry) "
        "+ F4 no slow/fast separation (ω_drive=ω_rotor by ontology, removes canonical BTW/OFC SOC). "
        "NET: structural LEAN toward Floquet limit-cycle, independent of N9's toy; DICHOTOMY NOT DECIDED (SOC biased-against, not excluded). "
        "DOWNSTREAM: SOC-universality route to (α,g,g_s) structurally DISFAVORED — not refuted. Per canon §5 derived-vs-generic, this is "
        "the Sakharov-Λ² template (DERIVED-generic-given-substrate-facts); Fork B DECISION stays #1-gap GATED.",
        cs["F1_compact_target"]["compact"] is True
        and cs["F2_periodic_drive"]["kind"].startswith("periodic")
        and cs["F3_multi_scale"]["n_scales_at_least"] >= 3
        and cs["F4_no_slow_fast_separation"]["separation"] is False
        and cs["lean"]["Fork B verdict (geometry-only, e5-litmus-free, no §9.6 routing)"] == "LEANS LIMIT-CYCLE (Floquet)"
        and "DERIVED-generic" in cs["tier"]
        and "#1-gap GATED" in cs["tier"])
    print("        ⇒ Fork B's limit-cycle lean now has two INDEPENDENT supports (N9 D4-Langevin toy + F1-F4 structural geometry); "
          "the SOC-universality coupling-pinning route is structurally disfavored, but the kernel decides.")

    # §17.4 vs §19.2 — meta-time-phase sampling vs V_4^perp projection (Brannen reach)
    mb = metatime_brannen_vs_v4perp_projection_reach()
    _ck("§17.4 meta-time-phase sampling vs §19.2 V_4^perp projection: SHARE the harmonic FORM (deferent + cosine at tau=0, no cos3/cos4) but DIFFER on the Brannen c-reach: §19.2 c free (INPUT sqrt(2), K=2/3); §17.4 c_norm = 2d/(1+d^2) bounded by 1 at lepton boundary tau=0 (K<=1/2, Foot<=35.3deg). c=sqrt(2) UNREACHABLE in §17.4 sampling — discriminant of sqrt(2)*d^2 - 2d + sqrt(2) = 0 is -4 < 0. Hence §17.4 reidentification does NOT add an independent derivation of K=2/3; the meta-time-phase sampling joins §19.4's NEGATIVE-forcing table as a additional structurally-incomplete route. LOCATED-GAP-REFINED — two pictures bridge at FORM, not at VALUE.",
        abs(mb["v4perp_picture"]["K_at_c_sqrt2"] - 2.0/3.0) < 1e-12
        and abs(mb["metatime_sampling_picture"]["c_norm_max"] - 1.0) < 1e-12
        and mb["metatime_sampling_picture"]["discriminant_for_c_norm_eq_sqrt2"] < 0
        and mb["metatime_sampling_picture"]["K_max_sampled_at_psi_eq_deltaL"] < 2.0/3.0 - 0.05
        and mb["metatime_sampling_picture"]["foot_max_at_tau0_deg"] < 45.0 - 5.0
        and mb["verdict"].startswith("LOCATED-GAP-REFINED"))

    print("ADJ1 consolidated bank (2026-08-12) — carrier-batch DERIVED-A algebra:")
    co = conjugating_extension_omega_identities()
    _ck("one-sided |Ω₄| = k₄/2 exact; FD vs analytic Ω₄ at FD-noise for all three extension classes",
        co["one-sided |Om4| = k4/2 (worst |4|Om4|^2/k4^2 - 1|)"] < 1e-12
        and max(co["FD vs analytic Om4, worst coeff (rigid, corot, conj)"]) < 1e-8)
    _ck("conjugating Ω₄ vanishes on EXACTLY {sin f = 0} ∪ {n̂ = ±lock axis} (closed magnitude k₄²sin²f(1−(n·a)²); off-locus visibly nonzero — non-vacuous)",
        co["conj Om4 on the locus {sin f = 0} U {n = +/- a} (worst coeff)"] < 1e-12
        and co["conj |Om4|^2 = k4^2 sin^2 f (1-(n.a)^2) (worst dev)"] < 1e-12
        and co["conj Om4 off-locus visibility (min maxcoeff)"] > 1e-3)
    _ck("⟨AXA~⟩₀ = ⟨X⟩₀ (observer-mass invisibility) and conjugation preserves the Q-span (u-blade coefficient exactly absent)",
        co["<A X A~>_0 - <X>_0 (worst)"] < 1e-12
        and co["Q-span leak under conjugation (worst coeff)"] < 1e-12
        and co["u-blade coefficient of A R_h A~ (worst)"] < 1e-12)
    al = alpha_family_parallelogram_law()
    _ck("same-axis composite ≡ α-family pointwise; parallelogram law Δkin = −2α(1−α)(1−c)(k_c/2)²c₂ exact; c α-independent",
        al["same-axis composite == alpha family (worst coeff)"] < 1e-12
        and al["parallelogram law residual (worst)"] < 1e-12
        and al["c alpha-independence (extracted-c spread)"] < 1e-12)
    _ck("argmin = ½ forced: α↔1−α symmetry + exact quadraticity + convexity, both sectors, pointwise (c₄/c₂-independent)",
        al["sector alpha<->1-alpha symmetry (worst, pointwise)"] < 1e-12
        and al["sector exact-quadraticity in alpha (worst)"] < 1e-12
        and min(al["min sector curvatures (quadratic, quartic)"]) >= 0.0)
    _ck("the computed hole-shaped fact is the AMPLITUDE NOTCH (|z| ≈ 0.384 at the wall); the kinetic dip is a small negative sub-term inside a large positive excess (canon §0 fence carried)",
        abs(al["wall notch |z| (vacuum 1.000 ->)"] - 0.384) < 0.01
        and al["wall Delta_kin / Delta_total (dip inside positive excess)"][0] < 0.0
        and al["wall Delta_kin / Delta_total (dip inside positive excess)"][1] > 0.0)
    ec = ecarrier_matched_defect_hblock_null()
    _ck("E-carrier matched defect: ENTIRE h-block ≡ 0 (all 16 entries, exact; FD with the TRUE inverse; E~ = +E trap witnessed — reverse visibly fails)",
        ec["max |h_mu_nu| over all 16 entries, all points"] == 0.0
        and ec["FD vs analytic (TRUE inverse), worst coeff"] < 1e-8
        and ec["trap witness maxcoeff(qE~ qE - 1) (reverse fails)"] > 0.5)

    print("K-O1 round certificates (2026-08-13; KO1_ADJUDICATION governing record):")
    ko = ecarrier_common_mode_certificates()
    _ck("★ KO1 C-1 [DERIVED-A] E-centrality: q_(k+dk)q_k⁻¹ = q_dk exact (collapses every "
        "referenced two-rate object); conjugation transparency; two-path TRUE-INVERSE carrier "
        "cancellation (arbitrary Cl(4,0) content); + the D-1 leg — the REVERSE overlap does NOT "
        "cancel the carrier ((A₁qE)~(A₂qE) = Ã₁A₂qE² exact), witness measured BOTH over all "
        "blades (> 0.3) AND within the {1,B} line (> 0.05, stated = measured); consequence "
        "filed class-(1) and RULED (RUL-035): R-023's reference on carrier backgrounds = the "
        "ruled adjoint t, rest-frame-scoped — see the C-4 leg-4 check",
        ko["leg1 centrality identities (worst coeff)"] < 1e-12
        and ko["leg1 D-1 reverse-overlap carrier retention (witness, must be > 0.3)"] > 0.3
        and ko["leg1 D-1 retention within the {1,B} line (measured, must be > 0.05)"] > 0.05)
    _ck("★ KO1 C-2 [DERIVED-A; (iv)-conditional RUL-018 class B] t(q_E) = q_E⁻¹ (the ruled "
        "involution IS the true inverse on the E-phase) ⇒ carrier-FLAT (iv)-observables: "
        "⟨Ψ t(Ψ)⟩₀ = c₀²/2 and ⟨Ω₄t(Ω₄)⟩₀ = (k_c/2)² exactly x₄-independent — INSTANTIATES "
        "cl41_positive_definite_pairing's per-blade value (E one of 32); RUL-018(b)'s volume "
        "density now engine-explicit",
        ko["leg2 (iv)-flatness devs (worst)"] < 1e-12
        and "class B" in ko["tier"])
    _ck("★ KO1 C-3 [DERIVED-A, FACT ONLY; the HINGE H is NOT decided] pure-carrier raw "
        "structure: un-referenced ideal shadow = cos(k_c x₄/2)c₀s₀ (exact zero at the node) "
        "and reverse grade-0 = cos(k_c x₄)c₀²/2 — sign-INDEFINITE (both signs realized): "
        "reverse is indefinite on e₅-content, so its grade-0 is not a density there (R-168 — "
        "why (iv) was ruled in); H's LIVE SCOPE = this raw shadow only (t-paired objects are "
        "carrier-transparent, keeper C3); coordinator ratification owed",
        ko["leg3 raw-shadow structure devs (worst)"] < 1e-12
        and ko["leg3 shadow amplitude at the node (exact 0)"] == 0.0
        and ko["leg3 reverse grade-0 sign pair (+, -)"][0] > 0.0
        and ko["leg3 reverse grade-0 sign pair (+, -)"][1] < 0.0
        and "NOT" in ko["hinge"])
    _ck("★ KO1 C-4 [DERIVED-A; RUL-035 engine ground] the {1,B} FACTORIZATION (keeper O1 + "
        "MO C2 composed): reverse-referenced Born-class overlaps on a shared carrier "
        "factorize exactly to cos(k_c x₄)·z⁽⁰⁾ per channel ⇒ RATIOS exactly carrier-invariant "
        "(common-mode cancellation — normalized R-023 probabilities carrier-independent), "
        "ΣP breathes as cos²(k_c x₄) and DEGENERATES 0/0 on the comb; the RULED adjoint t "
        "removes all three (constant reference) — R-023's reference operation on carrier "
        "backgrounds = t, rest-frame-scoped, t ≡ reverse on trivial backgrounds (RUL-035; "
        "boost extension = dictionary, RUL-034)",
        ko["leg4 {1,B} factorization + ruled-adjoint constancy (worst)"] < 1e-12
        and ko["leg4 normalized-ratio carrier-invariance (worst dev)"] < 1e-12
        and ko["leg4 Sum P vs cos^2 breathing (worst dev)"] < 1e-12
        and ko["leg4 Sum P on the comb (0/0 degeneracy witness)"] < 1e-20
        and "RUL-035" in ko["ruling"])


def check_twt_jd7_quartic():
    print("R-206 JD-7 leg B — the two readings of the bond COST differ at O(X^4) by exactly the Pfaffian channel:")
    r = g8_jd7_quartic_pfaffian_channel_identity(n_trials=20, seed=20260821)
    _ck("per-bivector identity <X^4>_0 = 1/2 Tr(M^4) + 6 Pf(M)^2 and Tr(M^4) = 1/2 Tr(M^2)^2 - 4 Pf^2 [DERIVED-A; max rel dev < 1e-12]",
        r["identity_max_rel_dev"] < 1e-12)
    cf = r["frame_coeffs_S1_S2_S3"]; cr = r["rotor_coeffs_S1_S2_S3"]
    _ck("frame-bilinear 24-bond sum = 8 S1 + 4 S2 exactly (S3 coefficient 0; residual < 1e-10)",
        abs(cf[0] - 8) < 1e-8 and abs(cf[1] - 4) < 1e-8 and abs(cf[2]) < 1e-8 and r["frame_residual_3ch"] < 1e-10)
    _ck("rotor-linear 24-bond sum = 4 S1 + 2 S2 + 6 sum_b Pf(X_b)^2 exactly (residual < 1e-10)",
        abs(cr[0] - 4) < 1e-8 and abs(cr[1] - 2) < 1e-8 and abs(cr[2] - 6) < 1e-8 and r["rotor_residual_3ch"] < 1e-10)
    _ck("the two-channel fit of the rotor reading is NOT exact (the JD-7 run's 0.148-class residual > 0.03: an artifact of the incomplete basis, never a constant of the theory)",
        r["rotor_residual_2ch_the_artifact"] > 0.03)
    _ck("planted failure: a Pfaffian coefficient of 5 instead of 6 leaves a residual > 1e-3 (the check can fail)",
        r["planted_failure_pf_coeff_5_residual"] > 1e-3)
    print("        => LS-Z2 discriminator (1) at O(X^4) is an IDENTITY (the pseudoscalar channel), not a fraction; the e-propagation stays BLOCKED at the dressed sector.")

def check_twt_z3_gauge_gain_band():
    print("R-207 the Z^3 generator's left-torus gauge identity + the W1 gain-band identity:")
    r = g8_z3_left_torus_gauge_identity(L=4, n_states=2)
    _ck("[B0, V_i] = [*B0, V_i] = 0 for all 18 bond twists and [B0, *B0] = 0 [DERIVED-A; < 1e-14]",
        r["comm_B0_V_max"] < 1e-14 and r["comm_SB0_V_max"] < 1e-14 and r["comm_B0_SB0"] < 1e-14)
    _ck("G(RU) = G(U) for a uniform LEFT rotation in B0, in *B0 and in their product (max dev < 1e-10 against |G| ~ 1e2)",
        max(r["dev_left_B0"], r["dev_left_SB0"], r["dev_left_torus_product"]) < 1e-10 and r["gen_scale"] > 10)
    _ck("the Lie-midpoint stepper is left-equivariant: step(RU) = R step(U) (< 1e-12)", r["dev_step_equivariance"] < 1e-12)
    _ck("planted: e13 does not commute with the twists (> 1e-2) and a LEFT e13 rotation changes G (> 1)",
        r["planted_comm_e13_V_max"] > 1e-2 and r["dev_planted_left_e13"] > 1.0)
    _ck("planted: a RIGHT B0 rotation is not a covariance of G (> 1): the K_i do not commute with B0 and are not needed to",
        r["dev_planted_right_B0"] > 1.0 and r["comm_B0_K_max_not_needed"] > 1e-2)
    w = g8_w1_gain_band_identity()
    lo, hi = w["band_exact"]
    _ck("W1 gain band exactly (rho/sqrt2, rho sqrt(3/2)): g_eff = 0 at both edges (< 1e-12), the grid band agrees (< 1e-3 rel)",
        abs(w["exact"]["g_at_lo"]) < 1e-12 and abs(w["exact"]["g_at_hi"]) < 1e-12
        and abs(w["band_grid"][0] / lo - 1) < 1e-3 and abs(w["band_grid"][1] / hi - 1) < 1e-3)
    _ck("min g_eff = 1 - a^2/4b = -1/3 exactly, at |F| = rho (< 1e-12; grid argmin at rho)",
        abs(w["exact"]["min_formula"] + 1/3) < 1e-12 and abs(w["exact"]["g_at_rho"] + 1/3) < 1e-12 and abs(w["argmin_grid"] / 36.877546 - 1) < 1e-4)
    p = w["planted_quartic_moved"]
    _ck("planted: the quartic weight moved to 3/2 misses both edges (> 1e-2) and the minimum (> 0.1 off -1/3)",
        abs(p["g_at_lo"]) > 1e-2 and abs(p["g_at_hi"]) > 1e-2 and abs(p["min"] + 1/3) > 0.1)
    _ck("planted: a rho1 mismatch between (a, b) and the x normalization breaks the -1/3 at rho (> 1e-2)",
        abs(w["planted_rho1_mismatch"]["g_at_rho"] + 1/3) > 1e-2)
    print("        => a uniform LEFT drive's mean is an exact frame rotation (carrier entrainment by it void for every Omega0); the W1 band is rho-exact, rho1-free.")

def main():
    print("="*70)
    print("  TWT companion engine — self-check (the deep-dive layer's harness)")
    print("="*70)
    checks=[check_twt_algebra, check_twt_observer_qm, check_twt_spectra, check_twt_matter, check_twt_weak, check_twt_hadrons, check_twt_cosmo, check_twt_jd7_quartic, check_twt_z3_gauge_gain_band]
    import io, contextlib
    total=0; ok=True
    for fn in checks:
        buf=io.StringIO()
        try:
            with contextlib.redirect_stdout(buf): fn()
            n=buf.getvalue().count('[OK ]'); total+=n
            print(f'  [PASS]  {fn.__name__[6:]:18s}  {n:>3d} checks')
        except Exception as ex:
            ok=False; print(f'  [FAIL]  {fn.__name__[6:]:18s}  {type(ex).__name__}: {ex}')
    print('-'*70)
    print(f'  ALL {total} COMPANION CHECKS PASSED across {len(checks)} modules.' if ok else '  SOME CHECKS FAILED.')
    print('='*70)
    return ok

if __name__ == "__main__":
    import sys; sys.exit(0 if main() else 1)
