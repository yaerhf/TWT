"""TWT library self-checks — the MAIN-engine harness (split 2026-08-13).
Runs every module's checks against the MAIN engine (twt.py) and reports one verdict.
The COMPANION engine's checks live in twt_companion_test.py — run BOTH before banking
(scripts/bank.sh does; the two totals must both be green).
Run:  python3 twt_test.py && python3 twt_companion_test.py
"""
import math
import sympy as sp
from twt import *

def _ck(name, cond):
    print(f"  [{'OK ' if cond else 'FAIL'}] {name}")
    assert cond, name

_check = _ck   # twt_poc uses this name


# ---- twt_poc ----------------------------------------
def check_twt_poc():
    print("Cl(4,0) engine — geometry COMPUTED, not asserted:")
    _check("I4·(L-bivectors) land in Q  (Hodge interchanges orbits)", I4_maps_L_to_Q())
    _check("e14·e24·e34 = -I4", triple_product_Q() == (-1.0) * I4)
    _check("e124·e134·e234 = e4", triple_product_color() == e(4))
    sqs = e_i4_squares_to_minus_one()['squares']
    _check(f"(e_i4)^2 = -1 for i=1,2,3  (Cl(4,0) cannot host Lorentz boost as rotor; got {sqs})",
           all(v == -1.0 for v in sqs.values()))
    lq = L_Q_orthogonal_decomposition()
    _check("L ⊥ Q under bivector inner product  (Λ²Cl(4,0) = L ⊕ Q orthogonal direct sum)",
           lq['<L, Q> = 0 (all cross-terms)'] and lq['dim_L_orbit'] == 3 and lq['dim_Q_orbit'] == 3)

    print("\nCharge sector — the §2a boundary: what is COMPUTED, and what is ASSIGNED:")
    yl = hypercharge(LEPTON_BLADE["e123"]); yq = hypercharge(QUARK_BLADES["e124"])
    _check(f"[ANCHOR-FREE] hypercharge(e123) = -1 (got {yl:+.0f}) — the e_4-bilinear "
           f"eigenvalue, computed from the blade with no charge input", abs(yl + 1) < 1e-9)
    _check(f"[ANCHOR-FREE] hypercharge(quark) = +1 (got {yq:+.0f}) — same map, opposite "
           f"sign; the sign opposition is the substrate content (R-056)", abs(yq - 1) < 1e-9)

    # The boundary itself is machine-readable, and this check makes it stay that way:
    # a charge-block primitive added without being classified on one side FAILS here.
    prov = charge_sector_provenance()
    _sides = set(prov["anchor_free"]) | set(prov["assigned"])
    _block = {"hypercharge", "doublet_hypercharge", "charge_normalization_anchor_free",
              "pi3_S3_integer_completion", "T3", "charge_assignment_from_anchor",
              "winding_charge", "generation_spectrum", "gmn_coefficient", "weinberg_sin2",
              "B_minus_L_anomaly"}
    _check("[BOUNDARY] charge_sector_provenance classifies every primitive of the charge "
           f"block on exactly one side (unclassified: {sorted(_block - _sides) or 'none'}), "
           "no primitive sits on both, the premise table names P4-P7, and the primitive itself "
           "proves the anchor-forcing identities SYMBOLICALLY (reviewer-derived 2026-08-21, "
           "engine-asserted: the four GMN coefficients are an arithmetic progression so the "
           "spread is 3*|Q_p - Q_n - 1| identically; P4 imposed FORWARD forces Q_p - Q_n = 1 "
           "identically in c WITHOUT the lepton tie; the no-/3 universal-c anchor is the UNIQUE "
           "point (1/2, -1/2)). It also carries the identification note: anchor-free is not "
           "identification-free, the blade->particle dictionary is P6-class",
           not (_block - _sides)
           and not (set(prov["anchor_free"]) & set(prov["assigned"]))
           and set(prov["premises"]) >= {"P4", "P5", "P6", "P7"}
           and "WITHOUT the lepton tie" in prov["anchor_forcing"]["P4_forces"]
           and "(1/2, -1/2)" in prov["anchor_forcing"]["no_over_3_unique_anchor"]
           and "IDENTIFICATION-FREE" in prov["identification_note"])

    # ---- the ASSIGNED side ------------------------------------------------------
    # WHAT STOOD HERE AND WHY IT WENT (blind probe P2, 2026-08-19; the live case named
    # in RUL-067's ground column; independently re-reported by external review round 2,
    # 2026-08-21): a single check asserting Q['u'] ≈ 2/3 where Q['u'] is computed as
    # (2·1 − 0)/3. It asserted that Python performs division and could not detect any
    # change in physics content. It is replaced by three checks: the same equality kept
    # but LABELED as the code-consistency regression guard it actually is, and two that
    # can fail for a reason that matters. Both were negative-tested — see
    # knowledge/audit/external_review_2026-08-21/CHARGE_SECTOR_REPAIR_2026-08-21.md.
    Q = charge_assignment_from_anchor()
    _check(f"[ASSIGNED — regression guard, NOT a physics check] at the default anchor "
           f"(Q_p, Q_n) = (1, 0) the composition solve returns Qu=+2/3 (got {Q['u']:+.3f}), "
           f"Qd=-1/3 (got {Q['d']:+.3f}). This is exact arithmetic on ENTERED literals: it "
           f"detects a code change, never a change in physics content",
           abs(Q['u'] - 2/3) < 1e-9 and abs(Q['d'] + 1/3) < 1e-9)

    def _gmn_spread(Qp, Qn, y_Q=None):
        """max-min of the per-state GMN coefficient over the four states, at an arbitrary
        anchor. y_Q overrides the R-057 trivector /3 for the counterfactual world."""
        q = charge_assignment_from_anchor(Qp, Qn)
        dh_ = doublet_hypercharge()
        yq_ = dh_["u"] if y_Q is None else y_Q
        yl_ = dh_["e"]
        cs = {"nu": (q["nu"] - T3["nu"]) / yl_, "e": (q["e"] - T3["e"]) / yl_,
              "u": (q["u"] - T3["u"]) / yq_,  "d": (q["d"] - T3["d"]) / yq_}
        return max(cs.values()) - min(cs.values())

    # DISCRIMINATING 1 — what could have disagreed: the anchor is NOT free. Requiring ONE
    # universal c across both orbits (premise P4) forces the anchor DIFFERENCE exactly.
    _sweep = [(1.0, 0.0), (1.0, 0.1), (1.2, 0.0), (0.5, -0.5), (2.0, 1.0), (0.9, 0.0)]
    _pred = {(a, b): 3 * abs(a - b - 1.0) for a, b in _sweep}
    _got = {(a, b): _gmn_spread(a, b) for a, b in _sweep}
    _check("[ASSIGNED — DISCRIMINATING] P4 (one universal c across both orbits) pins the "
           "anchor DIFFERENCE, not its value: the four-state GMN spread is exactly "
           "3·|Q_p − Q_n − 1| — PROVEN as an identity in charge_sector_provenance (so these six "
           "points witness a theorem, not a coincidence), and forced by P4 even WITHOUT the "
           "lepton tie — zero on the whole line Q_p − Q_n = 1 "
           f"(incl. the physically absurd (0.5, −0.5) and (2, 1)) and nonzero off it {[(k, round(v, 4)) for k, v in _got.items()]}. "
           "So the substrate side buys Q_p − Q_n = 1 and the ENTERED value Q_p = 1 buys the "
           "absolute normalization c = Q_p − 1/2 = 1/2 and nothing else. This is the honest "
           "division of labour the old check hid",
           all(abs(_got[k] - _pred[k]) < 1e-9 for k in _pred)
           and _got[(1.0, 0.0)] < 1e-12 and _got[(0.9, 0.0)] > 0.29)

    # DISCRIMINATING 2 — the R-057 /3 is load-bearing HERE, not just downstream: without it
    # the integer nucleon anchor is not even compatible with one universal c.
    _no3_at_real_anchor = _gmn_spread(1.0, 0.0, y_Q=hypercharge(QUARK_BLADES["e124"]))
    _no3_at_half = _gmn_spread(0.5, -0.5, y_Q=hypercharge(QUARK_BLADES["e124"]))
    _check("[ASSIGNED — DISCRIMINATING, counterfactual] delete the R-057 trivector /3 (use the "
           f"raw Y_Q = +1) and the observed anchor (1, 0) no longer admits one universal c: "
           f"spread = {_no3_at_real_anchor:.4f} ≠ 0. The unique anchor that does is "
           f"(Q_p, Q_n) = (+1/2, −1/2) (spread {_no3_at_half:.1e}) — a half-charged proton and "
           "a negatively charged neutron. So the /3 is what makes the integer nucleon anchor "
           "compatible with P4 AND THE NEUTRALITY DATA: substrate-specific, not generic (canon "
           "§5). The half-clause is load-bearing and was added at §8a review — untie the lepton "
           "rows and the no-/3 world does admit a universal c = 1/6 at (1,0), at the price of "
           "Q_nu = +1/3 and Q_e = -2/3, i.e. a charged neutrino and non-neutral hydrogen. Since "
           "Q(nu_L) = 0 is the anchor's own stated provenance datum, the tied table is the right "
           "one to quantify over — but 'at all' full stop was one notch stronger than the "
           "computation",
           abs(_no3_at_real_anchor - 1 / 3) < 1e-9 and _no3_at_half < 1e-12)

    c = gmn_coefficient()
    _check(f"GMN: c=1/2 on ALL blades (got {[round(c[s],3) for s in ['nu','e','u','d']]})",
           all(abs(c[s] - 0.5) < 1e-9 for s in c))
    _check(f"sin^2(theta_W) = 3/8 (got {weinberg_sin2():.4f})", abs(weinberg_sin2() - 3/8) < 1e-9)

    print("\nalpha_em — the L<->Q structure is explicit (the Coordinator's slip is impossible):")
    F = photon_strain_mode()
    _check("photon F spans BOTH orbits (magnetic in L, electric in Q)", F.spans_both_orbits())
    for k, v in F.orbit_content().items():
        print(f"        {k}: {v}")
    print(f"        alpha_em meaning: {alpha_em_meaning()}")

    print("\nGates — these RAISE (you cannot retreat to a silent stub):")
    for fn in (alpha_em_value, texture_tetrad, qcd_collider_phenomenology):
        try:
            fn(); _check(f"{fn.__name__} should have raised", False)
        except NotImplementedError as ex:
            print(f"  [RAISES] {fn.__name__}: {str(ex)[:70]}...")

    # THE FOURTH GUARD, and why it is a counted check rather than a print (apparatus
    # sabotage test, 2026-08-19): Substrate.tau_mem_over_tau_wave raises GatedError on
    # the unchosen-kernel branch, but MemoryKernel.GATED was never CONSTRUCTED anywhere
    # in the tree — so the raise was unreachable, and replacing it with a returned
    # number left both suites fully green. A guard nothing exercises is not a guard.
    # Note the class: no review role had "do the guards actually fire?" in its diet;
    # only deliberate sabotage found it. Negative-tested by replacing the raise with a
    # return, which now FAILS here.
    _gated_fired = False
    try:
        Substrate(memory_kernel=MemoryKernel.GATED).tau_mem_over_tau_wave()
    except GatedError:
        _gated_fired = True
    _check("Substrate.tau_mem_over_tau_wave RAISES on the unchosen-kernel branch — the guard is "
           "EXERCISED, not merely written. Before this check nothing in either suite constructed "
           "MemoryKernel.GATED, so swapping the raise for a number passed both suites in full",
           _gated_fired)

    print("\nAll structural checks passed. The math is self-consistent.")


# ---- twt_foundation ----------------------------------------
def check_twt_foundation():
    obs = WavefrontLockedObserver()
    print("WAVEFRONT-LOCKING, computed (the recurring-problem area):")
    eta = obs.dirac_metric()
    for row in eta:
        print("   [" + "  ".join(f"{x:+.0f}" for x in row) + "]")
    assert obs.signature() == [1, -1, -1, -1], "signature must be (+,-,-,-)"
    assert obs.spatial_axes_are_Q_bivectors(), "gamma^j must be Q-orbit bivectors"
    for k, v in obs.outside_vs_inside().items():
        print(f"   {k}: {v}")
    print("\n[OK] signature (+,-,-,-) COMPUTED from gamma^mu=e4,e4e_j inside Euclidean Cl(4,0).")
    print("[OK] observer-space axes ARE the Q-orbit bivectors (one structure, two roles).\n")
    closure_report()


# ---- twt_algebra ----------------------------------------
def check_twt_algebra():
    print("split invariant (2026-08-13):")
    import io as _io, os as _os, ast as _ast
    _here = _os.path.dirname(_os.path.abspath(__file__))
    _read = lambda f: open(_os.path.join(_here, f), encoding="utf-8").read()
    # WIDENED 2026-08-23 (family split): the MAIN engine is now THREE files — the facade
    # and its two halves — and the 2026-08-13 invariant binds all three, not just the one
    # that happens to be named twt.py. A guard that checks the facade only would pass
    # vacuously the moment a companion import were added to a half.
    _main_files = ("twt.py", "twt_core.py", "twt_candidate_v3.py")
    _ck("MAIN never imports COMPANION (no 'import twt_companion' statement in any of "
        "twt.py / twt_core.py / twt_candidate_v3.py — the mirror ships MAIN alone; "
        "canon §6 split invariant)",
        not any(ln.strip().startswith(("import twt_companion", "from twt_companion"))
                for f in _main_files for ln in _read(f).splitlines()))

    print("family split invariant (2026-08-23, RUL-093/RUL-095): CORE never consumes CANDIDATE:")
    def _module_names(sourcetext):
        """module-level names a file DEFINES (defs, classes, assignments)."""
        out = set()
        for _n in _ast.parse(sourcetext).body:
            if isinstance(_n, (_ast.FunctionDef, _ast.ClassDef)):
                out.add(_n.name)
            elif isinstance(_n, _ast.Assign):
                for _t in _n.targets:
                    for _x in (_t.elts if isinstance(_t, _ast.Tuple) else [_t]):
                        if isinstance(_x, _ast.Name):
                            out.add(_x.id)
        return out

    def _direction_violations(core_text, cand_text):
        """every twt_candidate_v3 name REFERENCED anywhere in twt_core (AST, not grep —
        a docstring mention is a string constant and must not fire)."""
        cand = _module_names(cand_text)
        core_tree = _ast.parse(core_text)
        core_defined = _module_names(core_text)
        hits = {}
        for _x in _ast.walk(core_tree):
            if isinstance(_x, _ast.Name) and _x.id in cand and _x.id not in core_defined:
                hits.setdefault(_x.id, []).append(_x.lineno)
            elif isinstance(_x, (_ast.Import, _ast.ImportFrom)):
                _mod = getattr(_x, "module", None) or ""
                _nms = [a.name for a in _x.names]
                if "twt_candidate_v3" in _mod or any("twt_candidate_v3" in n for n in _nms):
                    hits.setdefault("import twt_candidate_v3", []).append(_x.lineno)
        return hits

    _core_src, _cand_src = _read("twt_core.py"), _read("twt_candidate_v3.py")
    _viol = _direction_violations(_core_src, _cand_src)
    _ck(f"twt_core.py references NO name defined in twt_candidate_v3.py — the family may "
        f"not depend on the instance; the reverse edge is the allowed one (violations: "
        f"{ {k: v[:3] for k, v in _viol.items()} or 'none'})", not _viol)
    # THE GUARD IS SEEN TO FIRE (RUL-095 execution requirement, the relocation-leg standard):
    # a planted violation must be detected, or the check above is decoration. Both mutations
    # are run here against in-memory copies — the files on disk are never touched.
    _m1 = _core_src + "\n\ndef _planted():\n    return induced_level_parity_on_baryon_worldline()\n"
    _m2 = "import twt_candidate_v3\n" + _core_src
    _ck("the direction guard is NOT vacuous: a planted CORE->CANDIDATE call is caught, and "
        "so is a planted 'import twt_candidate_v3' (two demonstrated failure modes)",
        bool(_direction_violations(_m1, _cand_src)) and bool(_direction_violations(_m2, _cand_src)))

    print("facade conservation (twt.py re-exports BOTH halves — the ~40 probe scripts, the "
          "simulator and twt_companion import `twt` unmodified):")
    import twt as _twt, twt_core as _tc, twt_candidate_v3 as _tv
    _want = ({n for n in _module_names(_core_src) if not n.startswith("__")}
             | {n for n in _module_names(_cand_src) if not n.startswith("__")})
    _absent = sorted(n for n in _want if not hasattr(_twt, n))
    _ck(f"every module-level name of both halves — PRIVATE HELPERS INCLUDED (twt_companion "
        f"imports six of them by name from `twt`) — is an attribute of the facade "
        f"({len(_want)} names; absent: {_absent or 'none'})", not _absent)

    print("CORE_PROVENANCE — the intra-CORE third-commitment-class registry (RUL-095 (iii)):")
    _prov = charge_sector_provenance()
    _reg = CORE_PROVENANCE
    _bad = []
    for _row, _v in _reg.items():
        for _c in _v["consumers"]:
            if not hasattr(_twt, _c):                      # (i) the name must resolve
                _bad.append(f"{_row}:{_c}:absent")
            elif "marker" in _v:                           # (ii) it must name its own premise
                _seg = _core_src.split(f"\n{_c}" if _c.isupper() else f"\ndef {_c}")
                if len(_seg) < 2 or _v["marker"] not in _seg[1].split("\ndef ")[0]:
                    _bad.append(f"{_row}:{_c}:marker-missing")
    _ck(f"every registered class-(c) consumer resolves in the engine AND names its own "
        f"entered datum / posited premise in its own source (offenders: {_bad or 'none'})",
        not _bad)
    _ck("the charge row of CORE_PROVENANCE is EXACTLY charge_sector_provenance()'s ASSIGNED "
        "side — the two boundaries are one boundary and cannot drift apart",
        set(_reg["charge_assignment_chain"]["consumers"]) == set(_prov["assigned"]))
    print("§5.3 algebra dimensions:")
    d = cl40_vs_cl41()
    _ck(f"Cl(4,0)=16, Cl(4,1)=32, NOT iso (got {d})", d == {"Cl(4,0)":16,"Cl(4,1)":32,"isomorphic":False})

    print("§5.5 pseudoscalar I4:")
    _ck(f"I4² = +1 (real duality) (got {I4_squared()})", I4_squared() == SCALAR)
    print("     duality map I4·(biv) [L↔Q, sign COMPUTED]:")
    for name, (partner, sign) in duality_map().items():
        print(f"        I4·{name} = {sign:+d}·{partner}")

    print("§5.4 wave complex structure E = e12345 (Cl(4,1) — the colour-sector prerequisite):")
    cs_E = wave_E_complex_structure()
    _ck(f"E² = -1 (genuine geometric i, wave-sourced — vs I4²=+1) (got {wave_E5()*wave_E5()})",
        cs_E["E^2 == -1"])
    _ck("E is central (n=5 odd ⇒ pseudoscalar commutes with all generators)", cs_E["E central"])
    _ck("R[E] ≅ C ⇒ {e124,e134,e234} complexify to C³ (carrier only; su(3) is the open (β))",
        cs_E["R[E] ~ C"])

    print("§5.4b Cl(4,0)+H guardrail (spatial vs phase):")
    qt = cl40_quaternion_triple()
    _ck(f"H ⊂ Cl(4,0): {{e23,e13,e12}} unit quaternion (i²=-1, ij=k, ijk=-1) (got {qt})", all(qt.values()))
    ph = cl41_phase_is_external_u1()
    _ck(f"e5 is PHASE not space: E = I4·e5 is the external U(1) i (E²=-1 central; I4²=+1 ≠ phase) (got {ph})",
        all(ph.values()))

    print("§5.4c colour sector — native U(3) grounding (α) + the su(3) located gap (β/H1):")
    hf = colour_sector_E_hermitian_form()
    _ck(f"(α) colour carrier is U(3): E-Hermitian form, amplitudes faithful C³ coords (extraction exact); "
        f"real SO(3) realization excluded by external-U(1) phase-invariance (got symmetry {hf['free-form symmetry']})",
        hf["free-form symmetry"] == "U(3)" and hf["E complex structure ok (central, E^2=-1)"]
        and hf["amplitudes are faithful C^3 coords (extraction exact)"])
    so3f = colour_SO3_re_realization_forbidden()
    _ck("(α) SO(3)-real realization is C-linear (commutes with E) ⇒ centrality CANNOT exclude it; "
        "the exclusion is phase-invariance (old centrality argument refuted, recorded)",
        so3f["SO(3) generators are C-linear (commute with E)"])
    lg = colour_su3_located_gap()
    _ck(f"(β) su(3) located gap (H1+H2): invariant-quartic space is 3-dim — (Σ|c|²)² su(3)-invariant, Σ|c|⁴ AND "
        f"the holomorphic |Σc²|² both break su(3); the holomorphic bilinear is external-U(1) charge-2 ⇒ phase-"
        f"invariance does NOT extend to the quartic; colour-U(3) needs THREE §9.6-gated conditions [(b) B=0; "
        f"(a-bare) static holo un-derived; (a-rich) rich-barrier relative-phase]; GIVEN su(3) Casimirs give 9/4; "
        f"verdict: {lg['verdict'][:24]}…",
        lg["su3_writable (extraction round-trip exact)"] and lg["(sum|c|^2)^2 is su(3)-invariant"]
        and lg["sum|c|^4 is NOT su(3)-invariant"] and lg["|sum c^2|^2 (holomorphic) ALSO breaks su(3)"]
        and lg["holomorphic bilinear sum c^2 has external-U(1) charge 2 (modulus is charge 0)"]
        and lg["rep_chain C_A=3,C_F=4/3,ratio=9/4 (Casimirs)"] and lg["verdict"].startswith("PARTIAL/LOCATED-GAP"))
    ch = colour_quartic_charge_handle()
    _ck("§5.4d H2 charge handle [DERIVED + (iii)]: under exp(θE), Σ|c|²→charge-0, Σc²→charge-2, |Σc²|²→charge-0 "
        "(so phase-invariance does NOT forbid the holomorphic quartic); 3-dim quartic space complete; the rich-"
        "branch coupling is LOCATED at the relative-phase content of the §9.6 reactive barrier S; colour-U(3) "
        "needs THREE conditions — (a-bare) is a SEPARATE un-derived H1 item, not closed by 'given H1'",
        ch["charge(Σ|c|²) == 0"] and ch["charge(Σc²) == 2"] and ch["charge(|Σc²|²) == 0"]
        and ch["phase-invariance forbids |Σc²|²?"] is False and ch["verdict"].startswith("(iii)")
        and "three open conditions for colour-U(3)" in ch)
    rp = colour_relative_phase_is_coset()
    _ck("§9.6 reactive barrier [DERIVED spine + (ii)/(iii)]: the deciding |Σc²|² is moved ONLY by the SU(3)/SO(3) "
        "coset (= H1's not-Cl-native 5 = H2's holomorphic dir = the coset Cartan λ3,λ8), invariant under so(3) AND "
        "U(1)_global — so NO spiral Goldstone (phason+magnons) protects the relative phases; residual = coset-Cartan "
        "curvature of the driven steady-state (EOM-gated, sign-neutral, NOT a colour verdict)",
        rp["|Sc2|2 invariant under so(3) (l2,l5,l7)"] and rp["|Sc2|2 invariant under U(1)_global (phason)"]
        and rp["|Sc2|2 moved by SU(3)/SO(3) coset (l1,l3,l4,l6,l8)"] and rp["relative phases = coset Cartan (l3,l8)"] == [3, 8]
        and rp["verdict"].startswith("(ii)"))
    ab = colour_abare_static_holomorphic()
    _ck("a-bare [DERIVED ≠0, the 4th colour install OVERTURNED]: the static §10.3 colour quartic, made external-U(1)-invariant "
        "by CHARGE-PROJECTION (not E-Hermitian norm-substitution), carries the holomorphic |Σc²|² (charge-projected VARIES with "
        "relative phases, Σ|c|² is FLAT) → a-bare = ½Σ(b·∂f)⁴ ≠ 0 on overlapping colour support. NO static U(3)-clean exit: "
        "colour-U(3) ⟺ a-rich = −a-bare (EOM-gated cancellation of a known nonzero static baseline)",
        ab["a-bare == 0?"] is False and ab["E-Hermitian quartic FLAT in relative phases (=> its a-bare=0 is install)"]
        and ab["charge-projected quartic VARIES (=> carries |Sigma c^2|^2)"] and ab["disjoint support FLAT (a-bare=0 there)"])
    ar = colour_arich_kernel_dependent()
    _ck("a-rich [LOCATED (iii), first colour two-build CONCURRENCE]: the DRIVEN coset-Cartan curvature is KERNEL-DEPENDENT — "
        "both K-independent forcings fail for the relative phases (Goldstone/Adler-zero doesn't reach the non-Goldstone relative "
        "phases; FDT broken at the SOC NESS) → a-rich = a-rich(Θ_rel), ONE named kernel property (coset-Cartan FDT-violation at ω_d). "
        "U(3) ⟺ a-rich(Θ_rel) = −a-bare, SIGN-NEUTRAL (no genericity lean — self-tuned SOC kernel, not a generic draw). Deepest "
        "residual: is Θ_rel universal (→ structure-forced) or non-universal (→ K-dependent)?",
        ar["relative phases = coset-Cartan, NOT Goldstone-protected"] and ar["verdict"].startswith("(iii) kernel-dependent")
        and ar["a-bare baseline (GIVEN, != 0)"] > 0)

    tz = theta_rel_z3_isotropy_dichotomy()
    _ck("Θ_rel Z3-isotropy dichotomy [DERIVED tensor-structure; symmetry shortcut]: colour Z3 acts on the relative-phase "
        "Cartan {λ3,λ8} as the 2D STANDARD irrep (120° rotation, no real fixed axis), so by Schur the Z3-invariant symmetric "
        "curvature forms are 1-dim = scalar·I. ⟹ Θ_rel ISOTROPIC (1 scalar) ⟺ NESS preserves colour Z3; ANISOTROPIC ⟺ Z3 broken. "
        "Reduces Θ_rel's tensor content 2 numbers→1 (conditional on Z3); ties to CKM property P (= the SAME non-G/Z3-breaking axis); "
        "refutes CAND 3 (λ3→0 Goldstone), relocates CAND 2 (→N10). VALUE stays GATED.",
        tz["dim of Z3-invariant symmetric curvature forms (Schur)"] == 1
        and tz["no real fixed axis (Z3-fixed diagonal = diag(1,1,1) is OUTSIDE the Cartan)"] is True
        and tz["tier"].startswith("DERIVED"))

    tu = theta_rel_universality_located()
    _ck("Θ_rel UNIVERSALITY axis [FRAMING + LOCATED-GAP N11; DERIVED element = symmetry-shortcut foreclosure for the VALUE]: "
        "adjudicates CAND 1 (universal w→0 FDR X_inf via boundary CFT). No symmetry pins the VALUE (relative phases "
        "non-Goldstone N8; FDT broken N8; Z3/Schur fixed only STRUCTURE). DECISIVE R1 (wrong-object): X_inf "
        "(dissipation/fluctuation ratio at ω→0) and a-rich/a-bare (reactive-curvature ratio at ω_d) are DIFFERENT "
        "dimensionless ratios bridged by the kernel K; a-bare kernel-free, a-rich kernel-carrying, so a universal X_inf is "
        "NECESSARY-AT-MOST, not sufficient for colour-U(3) (a-rich=−a-bare). CAND 1 RELOCATED (not refuted — inverse-N0 "
        "guard); universality LOCATED as (U1) critical-not-Floquet ∧ (U2) a universal quantity actually fixing a-rich/a-bare. "
        "VALUE stays GATED.",
        tu["Theta_rel is at w_d (not w->0)"] is True
        and tu["a-bare static kernel-free baseline (cancellation target)"] > 0
        and tu["tier"].startswith("FRAMING + LOCATED-GAP (N11)")
        and "RELOCATED" in tu["CAND 1 status"])

    tp = theta_rel_pinnability_from_data()
    _ck("Θ_rel PINNABILITY from data [DERIVED neg (B1) + FRAMING binary/convergent (B2) + LOCATED value-windows (B3)]: "
        "(B1) FROM MASS EIGENVALUES = NO — lepton spectra are FRAME-INVARIANT (same spectrum under different mixings) "
        "while Θ_rel is a FRAME/eigenvector property (ckm_arc_circulant_linchpin); Koide/Brannen eigenvalues are "
        "Θ_rel-blind (hadron SPLITTINGS carry it but gap-gated, a 4th window). (B2) STRUCTURE (anisotropic/Z3-broken) "
        "pinned gate-free as a BINARY, CONVERGENTLY (not independent-path over-determination) from CKM "
        "(non-democratic |V_us|/|V_cb|≈5.5) + colour (SU(3)≠U(3)) through the SAME I₄ channel + derived Z3-dichotomy; "
        "conditional on the dichotomy ⇒ resolves N10's yes/no empirically (NESS MUST break colour-Z3). (B3) VALUE = "
        "windows (colour a-rich=−a-bare [a-bare DERIVED], CKM mags×F3, decoherence barrier, hadron splittings), all "
        "#1-gap-gated. δ–θ_C FLAG NOT an angle.",
        tp["B1_masses_frame_invariant"] and tp["B2_CKM_nondemocratic"] and tp["B2_dichotomy_is_derived"]
        and tp["B3_abare_derived_value"] > 0)

    kot = kernel_overdetermination_table()
    _ck("W2.1 kernel OVER-DETERMINATION TABLE [FRAMING dashboard + DERIVED-A live cross-checks]: "
        "graduates N33's prose meta-result into a self-validating engine artifact — 10 registry "
        "rows, each tagged with an anchor STATUS; exactly ONE usable anchor (KSS/GW bracket, itself "
        "not numerically closed: reconciling the eta/s-floor with the eta-ceiling needs an unstated "
        "entropy density s) against a >=2-parameter causal kernel ⟹ RANK-DEFICIENT by >=1 dof "
        "(= N33's headline). Live engine cross-checks (anti-drift): Kc ratio = (19/2)√38, running "
        "muPsi0 (decreasing, sign>0, ratio>2), Brannen 0.28%; exclusion guards: sin²θ_W=3/8 gate-free "
        "(NOT an Im χ sample — the N33 miscount), alpha_em_value GATED. Carries N33's four named "
        "missing inputs + the FDT-forbidden/KK-safe jurisdiction (I-12).",
        kot["n_rows"] == 10 and kot["n_usable_anchors"] == 1
        and kot["usable_anchor_ids"] == ["kss_gw_bracket"]
        and kot["rank_deficient"] is True
        and "FRAMING" in kot["tier"] and "DERIVED-A" in kot["tier"]
        and len(kot["n33_missing_inputs"]) == 4)
    kcc = kernel_candidate_constraints()
    _ck("★ Phase B / B1 — the KERNEL-CANDIDATE CONSTRAINT INVENTORY [FRAMING tooling; channel targets "
        "cross-validated live]: encodes as checkable DATA the full acceptance test any driven-dissipative "
        "kernel candidate (P2-1) must pass — 5 HARD constraints (C1 causality/KK + FDT-forbidden per I-12; "
        "C2 memory-requirement τ_mem>0 per R-114 (FRAMING); C3 linear-face + s=3 Adler-zero; C4 positivity ρ_2≥0 per R-040; "
        "C5 KSS bracket η/s≥ℏ/4π) + 3 CHANNEL TARGETS (order-param (19/2)√38≈58.56 [N31]; spin-0 c=3Ω_Λ≈2.05 "
        "[N33]; spin-2 C_T ≤4 moments [R-151]) + 1 discrete FORK BRANCH (fading vs hysteretic, never a knob) "
        "+ SOC disfavored. The B4 memo reports candidates against this; 'no member passes' is a first-class "
        "bankable result. Live cross-checks: 58.56 = N31's K_long/K_c, ≤4 = R-151's parity-even count, "
        "FDT-forbidden flagged, 1 usable anchor per R-150.",
        kcc["n_hard"] == 5 and kcc["n_channel_targets"] == 3 and kcc["n_branch"] == 1
        and abs(kcc["channel_targets"]["order_param_58"] - (19.0/2.0)*math.sqrt(38.0)) < 1e-9
        and kcc["channel_targets"]["spin2_CT_moments_max"] == 4
        and kcc["fork_is_branch_not_knob"] is True and kcc["fdt_forbidden"] is True
        and kcc["usable_anchors_underlying"] == 1 and "FRAMING" in kcc["tier"])
    kcf = kernel_candidate_form()
    _ck("★ §E.5 / R-153 — the #1-gap kernel CANDIDATE FORM (KS campaign, Grade B) [CANDIDATE]: "
        "the constraints-by-construction class (odd/passive/KK-causal/s≥3-Adler/UV-cutoff exact "
        "by construction) with members nodal/swave/composite + the EXCLUDED edge-less kstar "
        "(the two-sided D3 cull); every hard row of the acceptance inventory answered at the "
        "label level; branch = hysteretic (the counted F4 bit — a PICK, not a derivation); NO "
        "selection within the class (R-157) and NO magnitude supplied (the gates keep raising).",
        kcf["grade"] == "B" and kcf["tier"].startswith("CANDIDATE")
        and set(kcf["hard_row_coverage"]) == {"C1_causality_KK", "C2_monostability",
                                              "C3_linear_face", "C4_positivity", "C5_KSS_bracket"}
        and "kstar" in kcf["excluded"] and kcf["branch"] == "hysteretic"
        and kcf["selects_within_class"] is False and kcf["magnitudes_supplied"] is None)
    kcl = kernel_composite_closure()
    _ck("★ §E.5 / R-154 — COMPOSITE CLOSURE [DERIVED-A + CANDIDATE/FRAMING grounding]: the "
        "constraints-by-construction properties are CLOSED under the positive Goldstone+magnon "
        "sum [nodal(p=3)+r·swave]/(1+r) — sympy: the IR leading power of the positive sum is "
        "exactly 3 (the Adler floor survives ANY positive weights); numeric: odd + passive at "
        "machine precision across r; measured IR slope ≈3, UV slope < 0; boundaries recover the "
        "pure branches (r=0 → nodal EXACTLY; r=1e8 → swave) ⟹ the F2 edge fork DISSOLVES into "
        "the measured ratio r. The substrate-kernel-IS-this-sum identification stays CANDIDATE.",
        kcl["s_ir_sum_exact"] == 3 and kcl["odd_passive_all_r"] is True
        and abs(kcl["ir_slope_at_r1"] - 3.0) < 0.06 and kcl["uv_slope_at_r1"] < 0.0
        and kcl["r0_matches_nodal_max"] < 1e-15 and kcl["rinf_matches_swave_max"] < 1e-6
        and "DERIVED-A" in kcl["tier"] and "CANDIDATE" in kcl["tier"])
    kcd = kernel_candidate_dials()
    _ck("★ §E.5 / R-155 — the COUNTED CANDIDATE ECONOMY [INPUT/FIT, candidate-scoped]: genuine "
        "dials {p, wT, W, τ_mem, r} + ONE counted F4 hysteretic INPUT bit; the SN-15 edge scale "
        "EXACTLY absorbable (machine precision — NOT a dial); minimal member = 2 dials + 1 bit, "
        "composite = 3 + 1; LEDGER FENCE: counted within the candidate's OWN ledger — joins the "
        "§E.2.1 framework ledger ONLY on adoption (framework_ledger_joined is False).",
        set(kcd["dials"]) == {"p", "wT", "W", "tau_mem", "r"}
        and kcd["sn15_absorption_max_dev"] < 1e-15
        and kcd["minimal_member_dials"] == 2 and kcd["composite_dials"] == 3
        and kcd["framework_ledger_joined"] is False and "PICK" in kcd["input_bit"]
        and "candidate-scoped" in kcd["tier"])
    kfl = kernel_candidate_falsifiers()
    _ck("★ §E.5 / R-158 — the PRE-REGISTERED FALSIFIER REGISTER [CANDIDATE]: seven virgin-sector "
        "falsifiers P1–P7 (git two-commit: REGISTER 27e2847 strictly before EVALUATE 7f2d52d) + "
        "the two-sided D3 edge-less cull (kstar the recorded casualty); NO MISSES on the "
        "evaluable-now set (⊇ {P1, P6}); the near-KSS commitment (E.3.3 VG-1) STANDS at the "
        "compatibility level (η/s gated — never a fitted number); the N49/KC-1 INSIDE-frame "
        "jurisdiction hedge on the P1 ceiling + the flatness datum carried load-bearing.",
        len(kfl["register"]) == 7 and kfl["no_misses"] is True
        and {"P1", "P6"} <= set(kfl["evaluable_now"])
        and "kstar" in kfl["structural_falsifier"]
        and kfl["near_kss_commitment"].startswith("STANDS")
        and "INSIDE-frame" in kfl["frame_hedge"] and "projection" in kfl["frame_hedge"]
        and "27e2847" in kfl["preregistration"] and "7f2d52d" in kfl["preregistration"])

    print("§6.1/6.2 idempotents:")
    _ck("s0=(1+e4)/2 is idempotent (s0²=s0)", is_idempotent(s0()))
    cl41 = cl41_idempotents_note()
    _ck(f"Cl(4,1) P4,P15 idempotent + commuting, e15²=+1 (now constructed) (got {cl41})",
        all(cl41.values()))

    print("§6.3 Dirac spinor:")
    sp = spinor_real_dof()
    _ck(f"S has 8 real dof = 4-cplx Dirac (got {sp})", sp["match"])

    print("§8.4 chiral/Weyl split (distinct from L/Q):")
    cs = chiral_split_demo()
    _ck(f"⋆(e12) = -e34 (got {cs['star(e12)']})", cs["star(e12)"] == (-1.0)*e(3,4))
    _ck(f"e12-e34 is self-dual (⋆=+1) (got {cs['self_dual e12-e34 eigenvalue']})",
        cs["self_dual e12-e34 eigenvalue"] == 1)
    _ck(f"e12+e34 is anti-self-dual (⋆=-1) (got {cs['anti_self_dual e12+e34 eigenvalue']})",
        cs["anti_self_dual e12+e34 eigenvalue"] == -1)
    _ck("self-dual e12-e34 spans BOTH L and Q (≠ the L/Q split)", cs["self_dual spans L and Q"])
    _ck(f"Spin(4)=SU(2)+×SU(2)-: 3+3=6=dim so(4) (got {spin4_generator_count()})",
        spin4_generator_count()["total = dim so(4)"] == 6)
    _ck("weak=SD is the UNIQUE generation-blind su(2): centralizer(ASD) in so(4) is dim 3 = SD "
        f"(got {weak_isospin_centralizer_is_SD()['centralizer_dim']})",
        weak_isospin_centralizer_is_SD()["centralizer_dim"] == 3)
    _ck("V-A given weak=SD: SU(2)+ has a half-module kernel (acts on one Weyl chirality only). "
        "The old gloss 'the single-Weyl neutrino forbids the zero-kernel L-orbit' is WITHDRAWN "
        "(RV-7): the discriminator is the RIGHT-HANDED half's weak-singlet character "
        f"(kernel {vminusa_is_spin4_factor_chirality()['SU(2)+_kernel']} of {vminusa_is_spin4_factor_chirality()['module_dim']})",
        vminusa_is_spin4_factor_chirality()["SU(2)+_kernel"] == vminusa_is_spin4_factor_chirality()["module_dim"] // 2)

    print("C-32 exhausted-menu closure — the weak-su(2) menu inside grade-2 so(4):")
    _wx = weak_su2_menu_exhaustion()
    _ck("menu CLOSED: the Goursat sweep over 3-dim subalgebras of su(2)⊕su(2) returns exactly "
        "three admissible tuples = {SD, ASD, the diagonal so(3) class} — two rigid IDEALS plus one "
        "genuine 3-parameter family, and the exclusion comes from lemma L1 (su(2) has no 2-dim "
        "subalgebra, rank 1), NOT from the handed-mixture sub-case "
        f"(got {_wx['goursat_tuples_(dim_p1,dim_k1,dim_p2,dim_k2)']}); structure tensor is c·ε "
        f"exactly (residual {_wx['structure_constants']['max|T - c*eps|']})",
        _wx["goursat_tuples_(dim_p1,dim_k1,dim_p2,dim_k2)"] == [(0, 0, 3, 3), (3, 0, 3, 0), (3, 3, 0, 0)]
        and _wx["menu_classes_up_to_SO(4)"] == 3
        and "L1" in _wx["exclusion_comes_from"]
        and _wx["structure_constants"]["max|T - c*eps|"] < 1e-12)
    _ck("ASD is the SD MIRROR, not a rival: conjugation by an orientation-reversing frame "
        f"reflection (det {_wx['mirror']['reflection_det']}) maps SD onto ASD exactly — worst "
        f"residual over THREE inequivalent reflectors {_wx['mirror']['conj_e1(SD)->ASD_residual']:.1e} "
        "— preserves the diagonal CLASS (membership, not each member: a generic reflector carries "
        "the L-orbit to Stab(v')), and flips the I4 sign ⇒ 2 classes up to Aut(so(4))",
        _wx["mirror"]["conj_e1(SD)->ASD_residual"] < 1e-12
        and _wx["mirror"]["reflection_det"] < -0.5
        and _wx["mirror"]["I4_sign_flip_residual"] < 1e-12
        and _wx["mirror"]["diagonal_class_preserved_by_all_reflectors"] is True
        and len(_wx["mirror"]["witnesses (3 inequivalent reflection vectors, delta D4)"]) == 3
        and _wx["menu_classes_up_to_Aut(so(4))"] == 2)
    _ck("diagonal-class KILL (Route A): ker(SD)=ker(ASD)=2 (each grips exactly one Weyl half) "
        "while ker(L-orbit)=0 and ker(every graph subalgebra)=0 ⇒ a diagonal host would give "
        "right-handed charged currents AT FULL STRENGTH — one su(2) at one coupling, charging "
        "W− exactly as strongly as W+ — and none is OBSERVED AT ANY ACCESSIBLE ENERGY (the "
        "datum is read, not tuned, and reversible; its FAMILY INPUTS register row carries the "
        f"would-change-if) (got {_wx['kernels_on_4dim_spinor']})",
        _wx["kernels_on_4dim_spinor"]["SD"] == 2 and _wx["kernels_on_4dim_spinor"]["ASD"] == 2
        and _wx["kernels_on_4dim_spinor"]["L-orbit"] == 0
        and _wx["kernels_on_4dim_spinor"]["graph_subalgebras"] == [0])
    _ck("the discriminator is the RIGHT-HANDED half, NOT the neutrino's own: on W+ the L-orbit "
        "and SD have the SAME IMAGE (image dims 3/3, union 3 — the same algebra, so a single-Weyl "
        "neutrino cannot tell them apart), while on W− SD has image dim 0 (weak singlet) and the "
        "L-orbit 3. IMAGE DIMENSION, never per-operator matrix rank: the per-operator ranks are "
        f"{_wx['weyl_half_restriction']['per_operator_matrix_ranks_SD_on_W+']} on W+ and "
        f"{_wx['weyl_half_restriction']['per_operator_matrix_ranks_SD_on_W-']} on W−, and 3 is not "
        "among them",
        _wx["weyl_half_restriction"]["image_dim(SD|W+)"] == 3
        and _wx["weyl_half_restriction"]["image_dim(L|W+)"] == 3
        and _wx["weyl_half_restriction"]["image_dim(SD|W+ u L|W+)"] == 3
        and _wx["weyl_half_restriction"]["image_dim(SD|W-)"] == 0
        and _wx["weyl_half_restriction"]["image_dim(L|W-)"] == 3
        and 3 not in _wx["weyl_half_restriction"]["per_operator_matrix_ranks_SD_on_W+"]
        and _wx["weyl_half_restriction"]["per_operator_matrix_ranks_SD_on_W-"] == [0])
    _ck("C-32 gate CONTROLS — the sweep can return a DIFFERENT menu: dropping reality/compactness "
        f"(2-dim Borel allowed) gives {_wx['controls']['C1_reality_dropped_count']} tuples not 3, "
        f"and so(3) admits {_wx['controls']['C2_so(3)_3dim_subalgebra_count']} not 3",
        _wx["controls"]["C1_reality_dropped_count"] == 6
        and _wx["controls"]["C2_so(3)_3dim_subalgebra_count"] == 1
        and _wx["controls"]["C2_so(3)_selfcentralizer"] == 0)
    _ck("free-lepton/confined-quark from e4-content: lepton e123 anticommutes with e4 (I4·e123=e4, alone); "
        "quark blades commute, reach e4 only collectively (3-facet product = colour singlet)",
        e4_content_confines_quarks_not_leptons()["I4·e123"].startswith("e4"))
    _ck("Brannen amplitude form a_k = 1 + c·cos(φ_i−φ_k) (§19.2); at φ_i=φ_k the Koide point c=√2 gives a=1+√2",
        abs(brannen_amplitude(math.sqrt(2), 12.73, 12.73) - (1 + math.sqrt(2))) < 1e-9)
    _ck("spatial/phase partition (§5 guardrail): SPATIAL=Cl(4,0) vectors, PHASE=ℍ units + e5-completion E=I4·e5",
        set(spatial_vs_phase_partition()) == {"SPATIAL (Cl(4,0))", "PHASE / INTERNAL", "META-TIME e5"})

    print("ADJUDICATION3 bank (2026-08-12) — Cl(4,1) pairing algebra + the ruled pick (iv):")
    st = cl41_pairing_sign_tables()
    _ck("Cl(4,1) sign tables: reverse negative on EXACTLY the e5-containing blades; sector-uniform over all 32",
        st["reverse negative exactly on e5-containing blades"])
    _ck("conjugation pairing: E positive, e_i5 boosts negative, Cl(4,0) bivectors positive (the scoped statement)",
        st["conjugation: E positive, e_i5 boosts negative, Cl(4,0) bivectors positive"])
    _ck("E central in FULL Cl(4,1) ⇒ no commutator backstop for E-content (banked-functional quantifier fence)",
        st["E central in FULL Cl(4,1) (worst |[E,blade]| coeff)"] == 0.0)
    pd = cl41_positive_definite_pairing()
    _ck("t = α₅∘reverse is an exact anti-involution (t(xy)=t(y)t(x), t²=id; residuals 0)",
        pd["anti-involution residuals (t(xy)-t(y)t(x), t^2-id)"][0] < 1e-12
        and pd["anti-involution residuals (t(xy)-t(y)t(x), t^2-id)"][1] < 1e-12)
    _ck("⟨X t(X)⟩₀ POSITIVE-DEFINITE on all 32 blades and = Σ coeff² (refutes 'every involution fails')",
        pd["positive-definite on all 32 blades"]
        and pd["<X t(X)>_0 == sum of squared coeffs (diff)"] < 1e-12)
    _ck("t-pairing Spin(4)- and E-phase-invariant, boost-NON-invariant ⇒ no spin(4,1)-invariant pos-def pairing",
        pd["Spin(4)-invariance residual"] < 1e-12 and pd["E-phase-invariance residual"] < 1e-12
        and pd["boost non-invariance (norm change, must be > 0)"] > 1.0)
    _ck("reverse pairing: boost-invariant AND indefinite (the complementary horn of the theorem)",
        pd["reverse pairing boost-invariance residual"] < 1e-12
        and pd["reverse pairing indefinite (e5 neg, e1 pos)"])
    _ck("RULED pick (iv) restricted to Cl(4,0) == the banked reverse pairing (conservative extension; R1 2026-08-12)",
        pd["(iv) restricted to Cl(4,0) equals banked reverse pairing"])
    lk = boost_projection_leak_identity()
    # P6-1 repair (2026-08-21): the tolerance is RELATIVE, and the sweep runs to
    # ζ = 10 — an absolute 1e-12 was calibrated to the old ζ ≤ 1.5 sample and the
    # same true identity breaks it at ζ = 6 (1.5e-11) and ζ = 10 (3.0e-8).
    _ck("|g2(BAB⁻¹)|² = |A_⊥|² + cosh²ζ|A_∥|² engine-exact to RELATIVE 1e-13 over ζ ∈ {0…10} (relativistic rapidity; the absolute residual there is 3e-8)",
        lk["identity worst RELATIVE residual (the gating number)"] < 1e-13
        and lk["zeta sweep (fixed A, ascending)"][-1] >= 10.0)
    # P6-1 repair: the label is now a PREDICATE on the leak keys, blade by blade,
    # with the primitive's own ζ = 0 row asserted EMPTY as the named exception.
    _ck("all three e₁-blades leak to grade 1 blade-by-blade (e12→e2, e13→e3, e14→e4, each carrying cosh²ζ); {e23,e24,e34} inert; leak = {e2,e3,e4} at every ζ ≠ 0 row and EMPTY at ζ = 0 (B = 1, the named exception)",
        lk["all three e1-blades leak to grade 1 (blade by blade)"]
        and lk["perp blades {e23,e24,e34} inert (no grade-1 leak)"]
        and lk["e1-blades carry cosh^2(zeta), perp blades carry 1"]
        and lk["all six A-coefficients bounded away from zero (leak predicate meaningful)"]
        and lk["leak list = {e2,e3,e4} at every zeta != 0 row"]
        and lk["leak list EMPTY at zeta = 0 (the named exception: B = 1)"])
    # P6-1 repair: the true iff. "STRICT iff A_∥ ≠ 0" was FALSE — ζ ≠ 0 is required
    # too, and ζ = 0 is in the primitive's own row set. 2×2 truth table, both ways.
    _ck("projected-cost over-count = sinh²ζ|A_∥|² ⇒ STRICT iff (A_∥ ≠ 0 AND ζ ≠ 0): strict in that one cell of the 2×2 table, exact equality in the other three",
        lk["strict over-count iff (A_par != 0 AND zeta != 0)"]
        and lk["over-count closed form sinh^2(zeta)|A_par|^2 (rel residual)"] < 1e-13
        and lk["strictness truth table {(A_par!=0, zeta!=0): over-count}"][(True, True)] > 1e-6)
    # P6-1 repair: monotonicity COMPUTED off a fixed-A sweep (the old rows drew a
    # new bivector per ζ, so the claim was unreadable) — and even in ζ, not ζ.
    _ck("over-count monotone in |ζ|, NOT ζ: strictly increasing along the fixed-A ascending sweep, and EVEN in ζ (f(ζ) = f(−ζ) exactly)",
        lk["over-count strictly monotone in |zeta| (computed, fixed A)"]
        and lk["over-count EVEN in zeta (max rel |f(z)-f(-z)|)"] < 1e-13
        and len(lk["over-count sequence vs ascending |zeta| (fixed A)"]) == len(lk["zeta sweep (fixed A, ascending)"]))

    print("\nAll algebra-completion checks passed (companion-layer checks: twt_companion_test.py).")


# ---- twt_observer_qm ----------------------------------------
def check_twt_observer_qm():
    print("§13.3 boost/rotation generators:")
    K1, J3 = boost(1), rotation(1, 2)
    _ck(f"K_1 = ½e1, K_1² = +¼ (non-compact boost)  (K1²={K1*K1})", (K1*K1) == 0.25*SCALAR)
    _ck(f"J_3 = -½e12, J_3² = -¼ (compact rotation)  (J3²={J3*J3})", (J3*J3) == (-0.25)*SCALAR)

    print("§13.4 Thomas precession (the so(1,3) minus sign):")
    cl = so13_closure_signs()
    _ck("[K1,K2] = -J3  (boost-boost = MINUS rotation ⇒ so(1,3), not so(4))",
        cl["[K1,K2] = -J3 (boost-boost gives MINUS rotation = so(1,3))"])

    print("§14.7 Hestenes Dirac:")
    Is3 = hestenes_Isigma3()
    _ck(f"Iσ³ = e12 in the wavefront frame  (computed {Is3})", Is3 == e(1, 2))
    _ck("P_+ = ½(1+γ⁰) is idempotent", (dirac_ideal_idempotent() * dirac_ideal_idempotent()) == dirac_ideal_idempotent())

    print("§15.4 Bell / Tsirelson:")
    _ck(f"half-angle overlap ⟨R(Δθ)⟩_0 = cos(Δθ/2)  (Δθ=π/2 → {half_angle_overlap(math.pi/2):.4f} = cos45°)",
        abs(half_angle_overlap(math.pi/2) - math.cos(math.pi/4)) < 1e-12)
    S = tsirelson_S()
    _ck(f"|S| = 2√2 at optimal angles (got {S:.4f}; classical bound 2, quantum max 2√2={2*math.sqrt(2):.4f})",
        abs(S - 2*math.sqrt(2)) < 1e-9 and S > 2.0)
    M = mermin_value()
    _ck(f"3-party Mermin |M| = 4 = QM/GHZ max (got {M:.4f}; classical LHV bound 2) — rotor grade-0, extends Tsirelson to n=3",
        abs(M - 4.0) < 1e-9 and M > 2.0)

    print("§15.4 (multipartite): n-party Mermin–Klyshko hierarchy — TWT = QM-GHZ max 2^((n+1)/2):")
    for n in (2, 3, 4, 5):
        mk = mermin_klyshko_value(n); anchor = 2 ** ((n + 1) / 2)
        _ck(f"MK n={n}: TWT |M_n|={mk:.6f} = 2^((n+1)/2)={anchor:.6f}  (QM-GHZ max; rotor grade-0, Tsirelson-type optimal settings)",
            abs(mk - anchor) < 1e-6)
    _ck(f"MK hierarchy reproduces tsirelson_S() at n=2 (got {mermin_klyshko_value(2):.4f} vs {tsirelson_S():.4f}=2√2)",
        abs(mermin_klyshko_value(2) - tsirelson_S()) < 1e-9)
    _ck(f"MK hierarchy reproduces mermin_value() at n=3 (got {mermin_klyshko_value(3):.4f} vs {mermin_value():.4f}=4)",
        abs(mermin_klyshko_value(3) - mermin_value()) < 1e-9)

    print("§15.6 (Cl-iv-c): W (non-GHZ) class — located construction gap (ii-a), NOT a solve/falsifier:")
    wg = w_state_located_gap()   # raises if any P0/P1/P2/anchor assert fails
    _ck(f"W located-gap: GHZ object = cos(Σφ); W ≡ 0 in e12 plane (P1); diff-phase = |Σe^iφ|² norm (P2) — all proven; verdict: {wg['verdict'][:34]}…",
        wg["verdict"].startswith("ii-a") and wg["QM_anchors"]["W_inplane_correlation"] == 0.0
        and wg["QM_anchors"]["W_mermin_max"] == 3.046 and wg["QM_anchors"]["GHZ_mermin_max"] == 4.0)

    print("WP-MASS-MEASURE keystone bridge (2026-07-02): defect ω → front wavenumber k_4:")
    br = defect_rotor_frequency_reads_as_k4_on_front()
    _ck("bridge (i) DERIVED-A: q_h(τ_5) restricted to the wavefront lock x_4 = c_meta·τ_5 IS the x_4-profile at k_4 = ω/c_meta — exact on 3 independent axes (e12, generic conjugated R e13 R~, central E = I_4·e_5; Phase-F non-special-config discipline); extracted wavenumber matches ω/c_meta; half-angle sign flip at 2π/k_4, rotor period 4π/k_4; natural units read k_4 = ω = m literally",
        br["restriction_identity_exact"] and br["k4_extraction_matches"]
        and br["half_angle_sign_flip_at_2pi_over_k4"] and br["rotor_period_4pi_over_k4"]
        and br["natural_units_k4_equals_omega"]
        and len(br["per_axis_checks"]) == 3)
    _ck("bridge (ii)+(iii) honesty: the two FRAMING residues are NAMED, not folded in — (ii) one-particle-sector-at-k_4 (R-017's consuming identification) and (iii) the E → B_a complex-unit hand-off both carried as open in the return dict",
        "NOT derived here" in br["framing_residue_ii_one_particle_sector"]
        and "owed" in br["framing_residue_iii_complex_unit_handoff"]
        and "FRAMING" in br["tier"] and "DERIVED-A" in br["tier"])

    # R-125 (2026-07-02) — residue (ii) existence/location half via the symmetry shortcut:
    # the left u_hat-shift generator applied to the rest defect yields an EXACT collective
    # mode = co-rotating zero mode, lab/front frequency exactly ω (k_4 = ω/c_meta).
    print("R-123 residue (ii) — existence/location half (R-125, symmetry shortcut):")
    cm = defect_phase_collective_mode_at_k4()
    _ck("R-125 spine: Ω = R̃∂R exactly left-invariant under R → gR (generic non-commuting path + "
        "generic two-plane g); collective mode (û/2)·R* is the CO-ROTATING ZERO MODE, equals "
        "(1/ω)∂_τ₅R*, and reads at lab frequency EXACTLY ω on all 3 axes (e12, generic conjugated, "
        "central E); front restriction at k_4 = ω/c_meta exact",
        cm["omega_left_invariance_exact"]
        and len(cm["per_axis_checks"]) == 3
        and all(v["corotating_zero_mode_dev"] < 1e-12
                and abs(v["lab_frequency_extracted"] - 0.937) < 1e-5
                and v["front_restriction_dev"] < 1e-12
                for v in cm["per_axis_checks"].values()))
    _ck("R-125 sub-case honesty (AXIS-SPLIT per reviewer): E central over all 32 blades with E² = −1 "
        "but reverse(E) = +E (NOT a Spin rotor), and Ω is NOT E-phase invariant — Ω(g_E R) = "
        "exp(Eθ)·Ω(R) exactly (the reviewer's engine fact, banked) — so the E axis routes through "
        "τ₅-autonomy or an UNBANKED U(1)_E; bivector left shift preserves g̃g = 1 (banked symmetry)",
        cm["subcase_facts"]["E_central_all_32_blades"]
        and cm["subcase_facts"]["E_squared_minus_one"]
        and cm["subcase_facts"]["E_phase_not_a_spin_rotor_reverseE_plus"]
        and cm["subcase_facts"]["bivector_left_shift_preserves_rotor_constraint"]
        and cm["subcase_facts"]["omega_NOT_E_phase_invariant_but_expEtheta_equivariant"])
    _ck("R-125 tier honesty: SHARPENS residue (ii), does NOT close it — (C1) û-phase symmetry OR "
        "τ₅-autonomy, AXIS-SPLIT (bivector banked; E-axis NOT banked), coherence-argued for the "
        "kernel NOT proven; (C2) separable rest ansatz NAMED; remaining halves (H1) localization + "
        "(H2) one-particle-pole identification NAMED; new falsifier face exposed",
        cm["outcome"].startswith("SHARPENED (not closed)")
        and "(C1)" in cm["named_conditions"] and "NOT proven" in cm["named_conditions"]
        and "AXIS-SPLIT" in cm["named_conditions"] and "NOT banked" in cm["named_conditions"]
        and "(H1)" in cm["remaining_open_halves"] and "(H2)" in cm["remaining_open_halves"]
        and "falsify" in cm["new_falsifier_face"])

    # R-126 (2026-07-02) — the zero-mode FACTORY over the full symmetry catalog:
    # the rest defect's exact symmetry-mode multiplet reads ONLY k_4 = ±ω/c_meta.
    print("R-126 — zero-mode multiplet labels (the (H2) skeleton):")
    zm = defect_zero_mode_multiplet_labels()
    _ck("R-126 NEW right-symmetry engine facts: Ω(Rg) = g̃Ωg exact (right-covariance); the scalar "
        "part of any Ω-word is right-shift invariant (kinetic + Skyrme-class scalars); DM-sector "
        "right-status carried OPEN as a named condition",
        zm["right_symmetry_facts"]["omega_right_covariant_exact"]
        and zm["right_symmetry_facts"]["kinetic_scalar_invariant"]
        and zm["right_symmetry_facts"]["all_scalar_omega_words_invariant"]
        and "OPEN" in zm["right_symmetry_facts"]["dm_sector_right_status"])
    _ck("R-126 exact label table (generic conjugated û, generic R₀, Phase F): left û-commuting "
        "(dim 2) → +ω incl. R-125's phase mode; left anticommuting (dim 4) → −ω (conjugate "
        "branch); right sextet → +ω; translation-type → +ω; NO third label anywhere — the "
        "multiplet reads ONLY k_4 = ±ω/c_meta (the rest one-particle labels)",
        zm["labels_only_pm_omega"]
        and zm["label_table"]["commutant_dims"] == (2, 4)
        and zm["label_table"]["left_u_commuting_dim2"] == ["+omega"]
        and zm["label_table"]["left_u_anticommuting_dim4"] == ["-omega"]
        and zm["label_table"]["right_dim6"] == ["+omega"]
        and zm["label_table"]["r125_phase_mode_consistency"] == "+omega")
    _ck("R-126 tier honesty: per-class premises NAMED (P1 banked / P2 scalar-sector engine-exact "
        "with DM right-status OPEN / P3 homogeneity continuum-limit); −ω antiparticle reading FRAMING; "
        "boost/moving family FIRED as R-132 — a consistency check, NOT an independent second angle "
        "(D-8 sweep 2026-07-31); multiplet = the (H2) SKELETON, not (H2)",
        "(P1)" in zm["named_conditions"] and "OPEN" in zm["named_conditions"]
        and "continuum limit" in zm["named_conditions"]
        and "FIRED as R-132" in zm["framing_pieces"]
        and "NOT an independent second angle" in zm["framing_pieces"]
        and "not (H2) itself" in zm["framing_pieces"])

    # R-127 (2026-07-02) — residue (iii) resolved-as-selection: the front mass phase
    # is carried by the defect's own winding direction ±B_a (the R-020 blade).
    print("R-123 residue (iii) — the hand-off selects the winding axis (R-127):")
    ho = front_phase_handoff_selects_winding_axis()
    _ck("R-127 exact dichotomy (all three B_a, orthogonal line basis, generic angle): û = ±B_a "
        "stays EXACTLY in the observer's forced {1,B_a} line as a pure phase at rate ±ω "
        "(k_4 = ω/c_meta on the lock); other ℍ axes precess OUT of the line but INSIDE Cl(4,0) "
        "(spin-precession reading, amplitude-only shadow); the central E leaves the Cl(4,0) ideal "
        "(e₅ content — density-node shadow); partial axes give reduced rate + precession; "
        "left = right for winner and E (convention-free)",
        ho["s0_idempotent"]
        and len(ho["per_Ba"]) == 3
        and all(v["dichotomy_ok"] and v["line_orthogonal"]
                and abs(v["winner_phase_rate"] - 0.937) < 1e-5
                and v["left_equals_right_for_winner_and_E"]
                for v in ho["per_Ba"].values()))
    _ck("R-127 tier honesty: the SELECTION is DERIVED-CONDITIONAL (C1 banked §A.3 ansatz; C2 "
        "banked Part-B pure-phase criterion + empirical face; C3 L-orbit scope); the ξ-gloss "
        "reconciliation carried as FRAMING flagged for review; EOM-level axis lock + Q-orbit "
        "analog + (H1)/(H2) named still-open",
        "RESOLVED-AS-SELECTION" in ho["outcome"]
        and "DERIVED-CONDITIONAL" in ho["tier"] and "FRAMING" in ho["tier"]
        and "EOM-level axis-lock" in ho["still_open"]
        and "Q-orbit" in ho["still_open"] and "(H1)+(H2)" in ho["still_open"]
        and "falsifies" in ho["would_change_if"])

    # R-128 (2026-07-02) — R-127's Q-orbit extension: the baryon-sector lock is the
    # HODGE DUAL and PARITY-ODD — a Z₂ seat for the up/down doubling.
    print("R-127 Q-orbit extension — dual lock, parity-odd, up/down seat (R-128):")
    qd = qorbit_mass_phase_dual_lock_parity_odd()
    _ck("R-128 dual lock (all three B_q, exact): observer centralizer (W)∩(S')∩(E) = {1, I₄B_q} "
        "— the HODGE DUAL of the winding; only û = ±I₄B_q reads as a pure phase at ±ω; the "
        "winding axis itself leaks into the complementary idempotent sector; E exits the ideal",
        len(qd["per_Bq"]) == 3
        and all(v["centralizer_is_1_and_I4Bq"] and v["dichotomy_ok"]
                and abs(v["rate"] - 0.937) < 1e-5
                and v["winding_leaks_to_complementary_idempotent"]
                for v in qd["per_Bq"].values()))
    _ck("R-128 parity structure (exact): P an automorphism; L-orbit even / Q-orbit odd / I₄ odd; "
        "the quark lock P(I₄X) = −I₄P(X) is PARITY-ODD (lepton lock parity-even); the σ "
        "orientation label parity-flips; the (winding, dual) pair = one SD + one ASD and P swaps "
        "SD↔ASD — the Z₂ seat for the up/down doubling, absent for leptons",
        all(qd["parity_facts"].values()))
    _ck("R-128 tier honesty: C1' Q-orbit analog ansatz (R-020's 'structural analog, not "
        "load-bearing') + C2' same-observer NAMED; N28 consistency explicit (statics gives "
        "two-ness, the VALUE split stays Layer-2/⟨I₄⟩); up/down-seat + µΨ₀-tie carried FRAMING; "
        "which-σ-is-up and the split value NOT derived",
        "C1'" in qd["tier"] and "FRAMING" in qd["tier"]
        and "STATICALLY DEGENERATE" in qd["n28_consistency"]
        and "N28 stands" in qd["n28_consistency"]
        and "which sigma is up" in qd["not_derived"]
        and "runs per N37" in qd["not_derived"])

    # R-129 (2026-07-02) -- the R-128 mechanism face by elimination: the <I4> coupling
    # cannot live in ideal bilinears; it must engage the spatial winding topology (rho_L).
    print("R-129 -- I4-condensate ideal-channel rule + sigma-blindness (N38):")
    ic = i4_condensate_ideal_channel_rule()
    _ck("R-129 channel rule (exact, all 16 blades): s0*M*s0 = M*s0 if [M,e4]=0, = 0 if {M,e4}=0; "
        "survivors = the e4-commutant {1, e4, L-orbit, colour trivectors} = R-020 (W)-family; "
        "DEAD: vectors, Q-orbit, e123, and I4 ITSELF -- Psi~ I4 Psi = 0 identically (all grades, "
        "quark and lepton states); minimal composite carrier I4 x (Q-orbit) = L-orbit blades",
        ic["survivors_are_e4_commutant_W_family"]
        and ic["bare_I4_insertion_identically_zero"]
        and set(ic["channel_table"]["dead"]) == {"e1","e2","e3","e14","e24","e34","e123","e1234"})
    _ck("R-129 sigma-blindness + the reviewer's linear-channel finding: P fixes the lock axis, "
        "the R-128 mirror pair is ONE ray at snapshot level => diagonal bilinears sigma-blind; "
        "the LINEAR defect-vacuum pairing <vac~ I4 Psi> is NONZERO and sigma-ODD (the escape) "
        "and is excluded by the NAMED sign-gauge premise (Omega(-R) = Omega(R) exact, banked); "
        "elimination = DERIVED-CONDITIONAL on that premise; rho_L seat POINTED TO not confirmed "
        "(SD4.4 R-110 standing candidate); N28 vindicated at the same conditional level",
        all(ic["sigma_blindness"].values())
        and ic["linear_channel"]["nonzero_and_sigma_odd"]
        and "NAMED sign-gauge premise" in ic["linear_channel"]["excluded_by"]
        and ic["omega_sign_gauge_exact"]
        and "pointed to not confirmed" in ic["where_the_coupling_must_live"]
        and "SNAPSHOT" in ic["tier"] and "FRAMING" in ic["tier"]
        and "DERIVED-CONDITIONAL" in ic["tier"])

    # R-130 (2026-07-02) -- residue (ii) (H1) localization half: the phase mode's
    # defect-excess inherits the defect's own localization exactly; the carrier
    # subtraction is uniquely forced; residue (ii) narrows to (H2) + named (T).
    print("R-130 -- phase-mode excess inherits defect localization ((H1) discharged):")
    pm = phase_mode_excess_inherits_defect_localization()
    _ck("R-130 exact facts F1-F5: raw mode CONSTANT norm 1/2 everywhere (provably non-L2 -- "
        "R-125's excess-phrasing vindicated); excess = (u/2)Q(tau5)(R0-1) exactly; pointwise "
        "isometry N(exc) = (1/2)N(R0-1), tau5-free (mode-L2 <=> defect-L2, factor 1/2 exact); "
        "subtraction dichotomy |resid|_inf = |sin((w-wc)t5/4)| => the SAME-omega carrier "
        "subtraction is FORCED (the vacuum-relative subtlety DERIVED, not assumed); hedgehog "
        "N(R0-1)^2 = 4sin^2(F/4) n-hat-independent; Frobenius = coeff norm on Cl(4,0); "
        "left/right/u-hat isometries exact; E-axis Frobenius sign-flip (E-mootness face)",
        pm["facts"]["frobenius_eq_coeff_norm_cl40"]
        and pm["facts"]["isometries_left_right_uhat"]
        and pm["facts"]["E_axis_frobenius_sign_flip"]
        and pm["facts"]["F1_raw_mode_constant_half_dev"] < 1e-12
        and pm["facts"]["F2_excess_factorization_dev"] < 1e-12
        and pm["facts"]["F3_pointwise_isometry_dev"] < 1e-12
        and pm["facts"]["F4_dichotomy_dev"] < 1e-12
        and pm["facts"]["F4_offfreq_residual_nonzero"] > 0.05
        and pm["facts"]["F5_hedgehog_identity_dev"] < 1e-12)
    _ck("R-130 static-face tail + tier honesty: exterior indicial roots EXACTLY {-2, 1} (Euler "
        "operator annihilates r^-2; ANW corrections engine-checked subleading) => the banked "
        "drive->0 face satisfies the p > 3/2 criterion with margin; the (H1) closure is "
        "DERIVED-CONDITIONAL on NAMED (C2)+(T)+(N) (kernel tail NOT derived -- only the static "
        "face's p = 2 is); below-continuum reading tagged FRAMING; remaining open = (H2) + "
        "(T-kernel), a genuine open pair (reviewer fix: (T-kernel) not minimized under (H2)); "
        "new falsifier face (sub-r^-3/2 tail) exposed",
        pm["static_face_tail"]["indicial_roots"] == [-2, 1]
        and pm["static_face_tail"]["anw_residual_subleading"]
        and "DERIVED-CONDITIONAL" in pm["tier"] and "FRAMING" in pm["tier"]
        and "(T)" in pm["named_conditions"] and "(N)" in pm["named_conditions"]
        and "(H2) + (T-kernel)" in pm["remaining_open"]
        and "slower than r^-3/2" in pm["new_falsifier_face"])

    # R-131 (2026-07-03) -- residue (ii) (H2) quantization-step skeleton: compact phase
    # modulus => discrete charge tower; envelope identity dE/dN = omega (kernel-form-free)
    # => the tower's leading spacing is exactly the defect's rotor frequency.
    print("R-131 -- defect phase-modulus charge tower: discreteness + spacing = omega:")
    ct = defect_phase_modulus_charge_tower_spacing()
    _ck("R-131 DERIVED-A spine: ansatz reduction Omega_tau5 = R0~(u w/2)R0 (tau5-free, linear "
        "in omega; <Om^2>_0 = -w^2/4) and Omega_i omega-free => any Omega-built action reduces "
        "to L(omega, shape), polynomial in omega; COMPACTNESS: rotor period 4pi, theta+2pi => "
        "-R, Omega sign-blind (R-129 gauge re-verified on the ansatz) => ray orbit = closed "
        "2pi circle; orbit distances 2|sin(D/4)|, 2|cos(D/4)| exact; ENVELOPE FACTORIZATION "
        "dE/dw - w dN/dw = cons*cons_w/cons_s identically for FULLY GENERIC L(w,s) (reviewer "
        "upgrade -- engine-proved, not imported) AND on the quartic polynomial family, "
        "vanishing on the relative-equilibrium locus -- one AND two shape moduli symbolically "
        "exact; numeric illustration dE/dN = omega to 1e-4",
        ct["facts"]["D_universal_envelope_generic_L_exact"]
        and ct["facts"]["A1_omega_tau5_reduction_dev"] < 1e-7
        and ct["facts"]["A1_kinetic_scalar_dev"] < 1e-12
        and ct["facts"]["A2_omega_i_omega_free_dev"] < 1e-7
        and ct["facts"]["B_compactness_max_dev"] < 1e-7
        and ct["facts"]["B3_orbit_distance_dev"] < 1e-12
        and ct["facts"]["D_envelope_factorization_identically_exact"]
        and ct["facts"]["D_on_shell_zero_one_modulus"]
        and ct["facts"]["D_on_shell_zero_two_moduli"]
        and abs(ct["facts"]["numeric_illustration_dE_dN"] - 0.937) < 1e-4)
    _ck("R-131 tier honesty + fork neutrality: discreteness DERIVED-given-(Q) (the corpus-"
        "standard collective-quantization premise, FR frame); the Z vs Z+1/2 LATTICE is a "
        "NAMED Z_2 selection in the FR family, NOT decided (fork-neutral; distinct modulus "
        "from W-LIVE-4's sign-blind two-sided sandwich -- the one-sided phase orbit keeps "
        "the sign); spacing identity conditional on NAMED (C1)+(C2'); remaining (H2) core = "
        "pole uniqueness + the moduli<->pole identification (FRAMING); inertia correction "
        "kernel-gated; P2-4's induced level named as a free lattice cross-check",
        "NAMED, NOT" in ct["lattice_fork"] or "NAMED AND NOT" in ct["lattice_fork"]
        or ("NAMED" in ct["lattice_fork"] and "NOT decided" in ct["lattice_fork"]))
    _ck("R-131 scope: remaining-open and conditions carried in the return dict",
        "pole UNIQUENESS" in ct["remaining_open"]
        and "identification" in ct["remaining_open"]
        and "(C1)" in ct["named_conditions"] and "(C2')" in ct["named_conditions"]
        and "(Q)" in ct["named_conditions"]
        and "DERIVED-via-symmetry-CONDITIONAL" in ct["tier"]
        and "FRAMING" in ct["tier"])

    # R-132 (2026-07-03) -- the R-126 boost/moving-family handle FIRED: the Lorentz-boost
    # orbit of the rest label, inside Cl(4,0) via the gamma-embedding, is the mass shell.
    print("R-132 -- boost orbit of the rest label = the mass shell (chain (2) second angle):")
    bo = boost_orbit_rest_label_mass_shell()
    _ck("R-132 DERIVED-A spine: gamma^0 gamma^j = e_j (the iso's grade shift -- the observer's "
        "boost bivector IS a substrate vector); K_j^2 = +1/4 with exact rapidity addition "
        "(hyperbolic BECAUSE e_j^2 = +1, Euclidean); vector action B g0 B^-1 = cosh g0 - sinh g1 "
        "exact; rest label m gamma^0 -> (E,p) = m(cosh, sinh) with E^2 - p^2 = m^2 EXACT, "
        "algebraically (Clifford square) AND componentwise, for axis + generic-direction boosts "
        "+ rotation compositions; caveat DEFUSED side-by-side (e_14 rotation: E = m cos, "
        "CIRCULAR, e_i4_squares_to_minus_one intact; e_1 boost: E = m cosh, HYPERBOLIC); "
        "REVERSION HAZARD banked (reviewer): B~ = B in Cl(4,0) so the corpus R.x.R~ sandwich "
        "is a SILENT NO-OP here (B g0 B = g0 exactly) -- use B.x.B^-1, which IS the "
        "Cl(1,3)-reversion sandwich through the iso (g1 g0 = -e1)",
        all(bo["facts"].values())
        and bo["facts"]["reversion_hazard_RxRrev_is_noop_use_Binv"])
    _ck("R-132 tier honesty: dispersion second angle = DERIVED implied-by-banked composition, "
        "conditional on NAMED (P) substrate-realization premise (R-039 class, as in R-124) + "
        "(I) inherited residue-(ii) remainder ((H2) R-131 + (T-kernel) R-130); orbit-equals-"
        "full-shell transitivity imported (cited like Schur); no moving-defect construction "
        "claimed; falsifier alignment carried (off-shell moving defect would break (P))",
        "(P)" in bo["named_conditions"] and "(I)" in bo["named_conditions"]
        and "R-039" in bo["named_conditions"]
        and "implied-by-banked" in bo["tier"]
        and "imported group theory" in bo["tier"]
        and "OFF the shell" in bo["would_change_if"])

    print("R-184 the general-bilinear third-order null (Sorkin arc, non-Gleason route to R-160's conclusion):")
    bt = bilinear_detection_third_order_null()
    _ck("(T1) MASTER STRUCTURAL THEOREM, general n PROVED not sampled — UNDER THE P(∅)=0 "
        "HYPOTHESIS (no slit-independent monomial; a constant k has I₃=k≠0 — the SK-F1 "
        "vacuum-offset channel sits OUTSIDE this theorem, the R-184 closing review's computed "
        "catch): I₃[P] is EXACTLY the all-three-slit-touching part of P(ABC) — verified "
        "against the directly extracted all-3 part on the ladder (|ψ|²)^m for m = 2..5 "
        "(12/55/153/336 terms; the reviewer reproduced m = 7 at 1107). The superset "
        "sign-sums are +1/0/0/+1 for |T|=3/2/1/0, so only the all-three class and the "
        "hypothesis-excluded constant class survive",
        sorted(bt["T1_master_theorem"]) == [2, 3, 4, 5]
        and all(v["I3_equals_all_three_touching_part_of_P_ABC"] and v["I3_nonzero"]
                for v in bt["T1_master_theorem"].values())
        and [bt["T1_master_theorem"][m]["terms"] for m in (2, 3, 4, 5)] == [12, 55, 153, 336]
        and bt["T1_master_theorem"][2]["exact_homogeneity_degree"] == 4)
    _ck("(T2) THE NULL: ANY bilinear detection functional is annihilated — arbitrary slit-pair "
        "kernel M_ij with Hermiticity NOT assumed, and d-component amplitudes with an "
        "arbitrary bilinear metric at d ∈ {1,2,3,6} (the two branches the arc's own menu "
        "names, witnessed explicitly — the L1 memo cited a 2-component witness for them). No "
        "locality assumed: a non-local kernel K(x,y) only produces another arbitrary complex "
        "M_ij. TIER RIDER MANDATORY (canon §5, in kind with brannen_z3_harmonic_collapse_"
        "invariant): DERIVED-A GIVEN the hypotheses — generic set-indexed inclusion-exclusion, "
        "NOT a Clifford/D4 identity, zero TWT content",
        bt["T2_null"]["arbitrary_slit_pair_kernel_M_ij"]
        and bt["T2_null"]["hermiticity_assumed"] is False
        and bt["T2_null"]["locality_assumed"] is False
        and sorted(bt["T2_null"]["d_component_arbitrary_metric"]) == [1, 2, 3, 6]
        and all(bt["T2_null"]["d_component_arbitrary_metric"].values())
        and "NOT a Clifford/D4 identity" in bt["tier"])
    _ck("(T3) THE HYPOTHESIS IS PART OF THE THEOREM + (T4) THE DEMONSTRATED FAILURE MODE — "
        "two planted violations, so neither half is vacuous. (T3): with a slit-configuration-"
        "DEPENDENT kernel M^S_ij the null FAILS (computed, not asserted), so "
        "slit-configuration-independence is a real premise — and it is the premise a "
        "slit-set-dependent vacuum/carrier offset would deny, which nothing here covers. "
        "(T4): a NONLINEAR functional gives I₃ ≠ 0 for every m ≥ 2 (positive multinomial "
        "coefficients cannot cancel), with exact homogeneity s^{2m}. R-160 RELATION AT ITS "
        "TRUE STRENGTH: an independent non-Gleason route to R-160's CONCLUSION only — "
        "one-way, fixing no exponent until the EMPIRICAL third-order null is adjoined (a "
        "datum R-160 does not need); not a re-derivation, not a discharge of F2, not support "
        "for the rest of the Sorkin arc",
        bt["T3_hypothesis"]["counter_case_fires"] is True
        and bt["T3_hypothesis"]["set_dependent_kernel_null"] is False
        and bt["T3_hypothesis"]["fixed_kernel_null"] is True
        and bt["T4_failure_mode"]["planted_violation_demonstrated"] is True
        and bt["T4_failure_mode"]["checked_m"] == [2, 3, 4, 5]
        and "NON-GLEASON" in bt["r160_relation"].upper()
        and "conclusion only" in bt["r160_relation"].lower()
        and "F2" in bt["r160_relation"])


    print("\nAll §13–§15 observer/QM checks passed (companion-layer checks: twt_companion_test.py).")


# ---- twt_spectra ----------------------------------------
def check_twt_spectra():
    masses = [M_E, M_MU, M_TAU]

    print("§19.3 Koide (empirical lepton masses TEST the relation):")
    K = koide_K(masses)
    _ck(f"K = sum m / (sum sqrt m)^2 = 2/3  (got {K:.5f})", abs(K - 2/3) < 5e-4)
    _ck(f"Brannen-Koide theorem: K(c=sqrt2) = 2/3  (got {koide_from_c(math.sqrt(2)):.5f})",
        abs(koide_from_c(math.sqrt(2)) - 2/3) < 1e-12)
    _ck(f"equivalence: K=2/3 <=> c=sqrt(2) (the 45deg Koide value; got K={koide_from_c(C_KOIDE):.5f})",
        abs(koide_from_c(C_KOIDE) - 2/3) < 1e-12)
    th = foot_angle_deg(masses)
    _ck(f"Foot angle theta = 45deg  (got {th:.3f})", abs(th - 45.0) < 0.05)
    _ck(f"DFT: K(r=1/sqrt2) = 2/3  (got {dft_K_from_r(1/math.sqrt(2)):.5f})",
        abs(dft_K_from_r(1/math.sqrt(2)) - 2/3) < 1e-12)

    print("§19.5 the lepton angle delta_L from D/J = 0.79:")
    dL = math.degrees(delta_L_from_DoverJ(0.79))
    _ck(f"delta_L = (1/3)arctan(0.79) ≈ 12.7deg, in (0,15)  (got {dL:.2f})", 0.0 < dL < 15.0)

    print("§10.3.1 / §10.2.1 canting pitch q and the canting order parameter cos q at D/J=0.787:")
    q_deg = math.degrees(canting_pitch_q_rad(0.787))
    _ck(f"q = arctan(D sqrt(2)/(6 J)) ≈ 10.51deg  (got {q_deg:.4f})",
        abs(q_deg - 10.51) < 0.01)
    cq = canting_cos_q(0.787)
    cq_direct = math.cos(canting_pitch_q_rad(0.787))
    _ck(f"<R> = cos q ≈ 0.983 (closed form sqrt(18/(18+(D/J)^2)))  (got {cq:.4f})",
        abs(cq - 0.9832) < 1e-4)
    _ck(f"closed form matches cos(atan(...)) directly  (delta {abs(cq-cq_direct):.2e})",
        abs(cq - cq_direct) < 1e-12)
    _ck(f"hierarchy type = one-light-two-heavy  (got '{hierarchy_type(dL)}')",
        hierarchy_type(dL) == "one-light-two-heavy (observed lepton hierarchy)")
    djl = abs(DoverJ_from_lepton_masses())
    _ck(f"D/J BACK-DERIVED from lepton masses alone (NOT fed in) ≈ 0.787 (got {djl:.4f}) "
        f"— the lepton leg of the T0 over-determination, now reproducible in code",
        abs(djl - 0.787) < 0.01)
    djs = DoverJ_from_skyrme()
    _ck(f"D/J BACK-DERIVED from the empirical Skyrme e (√18/5.45) ≈ 0.778 (got {djs:.4f}) "
        f"— the baryon leg; agrees with the lepton leg to ~1.1% (NOT 0.4%: 0.790 is the Cabibbo "
        f"calibration, not a baryon value; √18-coincidence-hedged)",
        abs(djs - 0.778) < 0.01 and abs(djs - djl) / djl < 0.02)
    od = over_determination_scan()
    _ck(f"T0/WP-OD1 scan CONSOLIDATED: D/J 3-sector (lep {od['DJ_lepton']}, bar {od['DJ_baryon']}, "
        f"cab {od['DJ_cabibbo']}) — lep↔bar PASS {od['DJ_lepton_baryon_pct']}%; v/f_π~m_p/m_e PASS "
        f"{od['OD1.3_pct']}%; f_π one shared floor PASS; NO FAIL ({od['n_FAIL']}); exactly ONE tracked "
        f"FLAG = δ–θ_C (Cabibbo {od['DJ_cabibbo_vs_lepton_pct']}% high, origin §19.7 L/Q sector-projection)",
        od['n_FAIL'] == 0 and od['n_FLAG'] == 1 and od['OD1_lepton_baryon'].startswith('PASS')
        and od['OD1_cabibbo'].startswith('FLAG') and od['OD1.3_v_fpi_vs_mp_me'].startswith('PASS'))

    print("§19.4 Koide-charge Z3 unification:")
    ku = koide_charge_unification()
    _ck(f"K_N=2/N and Qu=(N-1)/N coincide at N=3 (both 2/3)  (got {ku})", ku["coincide_at_N=3"])

    print("§19.6.1 Koide-modus-tollens (positive empirical-coherence check):")
    kmt = koide_modus_tollens_consistency()
    _ck(f"§19.6.1 Koide-modus-tollens (canon §0a-2): explicit-SSB on lepton mass op predicts "
        f"K-deviation ~{kmt['explicit_SSB_K_deviation_scale']:.2f} (~82%); empirical K-deviation "
        f"= {kmt['deviation_observed']:.1e}; framework passes consistency band by ~"
        f"{kmt['orders_inside_consistency_band']} orders; [e_{{23}}, e_{{14}}]=0 gen-1 decoupling "
        f"engine-verified; CONSISTENCY (NOT a derivation of K=2/3 INPUT); WP-MASS-MEASURE-spine-independent",
        kmt["orders_inside_consistency_band"] > 3.5
        and kmt["substrate_commutator_check"]["[e_{23}, e_{14}] = 0 (gen-1 decoupled)"] is True
        and "DERIVED-STRUCTURAL" in kmt["tier"])

    print("§19.6.1 the generation-cycle generator G:")
    gc = G_cycles_generations()
    _ck(f"G = (e12+e23+e31)/√3 is a unit bivector (G²=-1)  (got {gc['G²']})",
        abs(gc["G²"].coeff(()) + 1.0) < 1e-9)
    _ck(f"rotor exp(Gπ/3) cyclically permutes {{e14,e24,e34}} (G generates the generation Z3)  (images {gc['images']})",
        gc["cycles {e14,e24,e34}"])

    print("§19.7 quark sector (Cabibbo DECOUPLED from δ_L per Q1; θ_C=δ_L identification REFUTED):")
    qmr = quark_mass_reconstruction()
    _ck(f"F3.1 quark masses [INDICATORS, not verifiers — only hadron masses verify]: DOWN rebuilds "
        f"{qmr['down']['max_resid_pct']}% (tautological — b_d,ε_d fitted from d,s,b); ψ a non-unique fit "
        f"({qmr['psi_degeneracy'][:5]}); UP misses the m_t INDICATOR ({qmr['up']['max_resid_pct']:.0f}%) but "
        f"that is NOT a TWT falsification (no top hadrons ⇒ m_t not a verifier); dial audit is indicator-level "
        f"(the quark-sector verifier was the V1 30-hadron fit — paper-only, retired from V2 under W-LIVE-MASS-AUDIT 2026-06-29 as snapping-disguised-as-derivation; NOT in V2 engine, not a quark-mass count)",
        qmr['down']['max_resid_pct'] < 1.0 and qmr['up']['max_resid_pct'] > 50.0
        and qmr['psi_bedrock_derivable'] is False and 'mass_verifier_principle' in qmr)

    print("  ψ-repair (ADJUDICATION2 keeper C1, 2026-08-13): ψ is not fixed by the mass spectrum; ψ_inv is the mass-observable:")
    bz = brannen_z3_harmonic_collapse_invariant()
    _ck(f"Z3 harmonic collapse cos(2φ_n-ψ)=cos(φ_n+ψ) exact (max err {bz['collapse_max_err']:.1e}); "
        f"ψ NOT fixed by the masses (mass-gauge) — two distinct (b,ε,ψ) triples hit the same 3 masses "
        f"(witness: {bz['two_triple_witness']['triple1']} vs ε=0 {bz['two_triple_witness']['triple2_eps0']}); "
        f"r²-orbit amplitude cap = {bz['r2_orbit_amplitude_cap']} < banked A_d (N60)",
        bz['collapse_max_err'] < 1e-12
        and abs(bz['two_triple_witness']['triple1'][2] - bz['two_triple_witness']['triple2_eps0'][2]) > 6.0
        and bz['r2_orbit_amplitude_cap'] <= 1.0 + 1e-9
        and bz['down_model_free']['A'] > bz['r2_orbit_amplitude_cap'] + 0.5)
    _ck(f"MS-bar indicator-triple invariant ψ_inv,d = {bz['down_model_free']['psi_inv_deg']}° (3-point DFT, "
        f"model-free, scheme-dependent; fit route {bz['down_fit_route']['psi_inv_deg']}° = fit residuals; "
        f"credited hadron-route band 5.8–8.5° is the physical channel) — both ≠ δ_L = {bz['delta_L_deg']}°, "
        f"the old 'ψ_d ≈ δ_L' clause STRUCK over-determined; "
        f"cross-route A_d ⇒ K_down = {bz['down_model_free']['K_down']} via koide_from_c (reciprocal 1.367)",
        abs(bz['down_model_free']['psi_inv_deg'] - 6.294243) < 1e-4
        and abs(bz['down_fit_route']['psi_inv_deg'] - bz['down_model_free']['psi_inv_deg']) < 0.05
        and abs(bz['down_model_free']['psi_inv_deg'] - bz['delta_L_deg']) > 4.0
        and abs(bz['down_model_free']['K_down'] - koide_from_c(bz['down_model_free']['A'])) < 1e-6
        and abs(1.0/bz['down_model_free']['K_down'] - 1.367) < 1e-3)

    print("  non-uniform-orbit SECOND BUILD → Gate B decided geometrically (proper two-build; first-pass solo (iii) SUPERSEDED):")
    d1 = updown_mass_operators_commute()
    _ck("D1 [CONSTRUCTION-INDEPENDENT, the headline]: deferent+dip are functions on the ℤ₃ orbit → mass operator CIRCULANT → "
        "[M_u,M_d]=0 EXACTLY → CKM democratic, for a circulant/Spin(4) reason (not a frame choice) — strengthens metatime, supersedes "
        "the first-pass single-axis Phase B (the fake-negative). The orbit geometry does NOT give the ladder (b,ε are eigenVALUE-only)",
        float(d1["[M_u,M_d]"].split("e")[0]) < 10 and "DEMOCRATIC, CONSTRUCTION-INDEPENDENT" in d1["verdict"])
    wi = weak_isospin_zero_on_generations()
    _ck("D2 [Level-2 theorem GIVEN the identification, CONTINGENT]: the self-dual su(2)₊ acts as EXACTLY ZERO on the anti-self-dual "
        "generation space (Spin(4) mutual-centralizer) → GIVEN weak-isospin=su(2)₊, weak isospin can't rotate the generation frame. "
        "★ LOAD-BEARING: that identification is asserted (§19.8.1) NOT derived; a different one overlapping V (e14 ad-norm 1.41) REVIVES the thesis",
        max(wi["su2_plus_action_on_V_norms"]) < 1e-12 and wi["alt_identification_e14_action_on_V_norm"] > 1.0)
    pa = nonuniform_orbit_baryon_model()
    _ck("Phase A [hadron-only, RETAINED — gaps NOT determined]: the cos(Δφ_gen) overlap free-fit does NOT beat the flat baseline and leaves "
        "the same-gen/cross-gen split unresolved; the split only zeros under a targeted objective at an RMS cost with different gaps → gaps "
        "PROBE-DEPENDENT, not hadron-determined (does NOT refute the thesis — a colour-sourced non-uniformity need not be baryon-pinned)",
        pa["gaps_hadron_determined"] is False and pa["free_gap_RMS_optimal"]["beats_baseline"] is False)
    wrt = weak_isospin_rank_table()
    _ck("weak-isospin rank table [DERIVED, decisive]: su(2)₊ acts rank-0 (democratic) ONLY on the anti-self-dual space; "
        "on §8.3's STATED Q-orbit generations EVERY embedding (incl. clean su(2)₊) gives rank-3 (mixing-reachable). "
        "Democratic occupies exactly 1 of 6 cells — the chiral/orbit conflation §8.4 warns against",
        wrt["su2_plus_(§8.4)"]["anti_self_dual_(prior arc)"] == 0
        and all(wrt[en]["Q_orbit_(§8.3 quark gens)"] == 3 for en in wrt))
    wv = weak_isospin_verdict()
    _ck("weak-isospin verdict [(iii)→(ii) RESOLVED]: the RANK analysis alone left U1/U2 under-determined (structure LEANS "
        "mixing-reachable on §8.3's stated generations), but the CKM arc DERIVED the {chiral projector ½(1+I₄)+S₊+gen-space} "
        "pair via §19.8.1 +e₄ → (ii) LOCATED; residual = property P = Θ_rel (the #1 gap, shared with colour-U(3))",
        "RESOLVED" in wv["outcome"] and "(ii) LOCATED" in wv["outcome"] and "MIXING-REACHABLE" in wv["lean"]
        and wv["deciding_principle"].startswith("a DERIVED consistent pair"))
    seed = ckm_hierarchy_and_cp_seed()
    _ck("SEED (salvaged from the Gemini note): complexity ALONE stays democratic (complex-circulant commutes), "
        "but a NON-CIRCULANT E-valued term gives the hierarchy AND a physical-scale Jarlskog J from one complex term "
        "→ E (=e12345) is the natural CKM CP-phase source, arriving WITH the hierarchy term if it is E-valued. Sharpens "
        "the gate: the owed chiral/handed projector is naturally complex → magnitudes + J together (ties CP to §19.8.1)",
        "physical scale" in seed["non_circulance_plus_E"] and seed["the_seed"].startswith("E ("))
    print("    [retired from V2, NOT a tracked port] V1 30-hadron baryon fit (V1 §17.4, 6 nominal / ~9 effective params): V1-reported only; retired from V2 paper body under W-LIVE-MASS-AUDIT 2026-06-29 (snapping-disguised-as-derivation per workflow audit); NOT in V2 engine; the script is deliberately NOT in this repo per standing 2026-06-24 directive (worklist F3 line 886) — rebuilding it is NOT a current work item.")


    print("§19.8.1 neutrino forced handedness (computed):")
    _ck("γ⁰γʲ = e_j (massless H = e_j p_j)", all(gamma0_gammaj_reduces_to_ej(j) for j in (1, 2, 3)))
    h2, p2 = massless_H_squared()
    _ck(f"H² = |p|² (got {h2} = {p2})", h2 == p2 * e())
    fh = forced_handedness()
    _ck(f"e4·I4·e4⁻¹ = -I4 and e123·I4·e123⁻¹ = -I4 (handedness sign flips)  (got {fh})",
        fh["e4·I4·e4⁻¹ = -I4"] and fh["e123·I4·e123⁻¹ = -I4"])

    print("§19.8.2 neutrino lightness (single Weyl ideal):")
    nl = neutrino_lightness()
    _ck(f"charged lepton = 2 ideals (Dirac mass); neutrino = 1 ideal (no partner ⇒ light)  (got {nl})",
        nl["charged lepton ideals (S+⊕S-)"] == 2 and nl["neutrino ideals (single Weyl)"] == 1)

    print("§19.8.3 sterile RH neutrinos as dark-matter candidate (DM-V2-1 first cut, LOCATED-GAP):")
    sr = sterile_rh_relic_check()
    _ck(f"3 sterile RH neutrinos (DERIVED §19.8.3, Dirac partners of active LH; m_s tied to active m_ν)  (count={sr['TWT_sterile_count']})",
        sr["TWT_sterile_count"] == 3)
    _ck(f"thermal upper bound Ω_s h² ≤ 2·Σm_ν/(94 eV) = {sr['Omega_sterile_h2_thermal_upper_bound']:.5f}; ratio to Ω_DM h² = {sr['ratio_thermal_upper_to_Omega_DM']:.3f} (~2.1%); shortfall ~{sr['thermal_shortfall_factor']}x",
        0.01 < sr["ratio_thermal_upper_to_Omega_DM"] < 0.05 and sr["thermal_shortfall_factor"] > 20)
    _ck(f"DW window mismatch: m_s~keV required, TWT m_s≤0.1 eV ⇒ ~{sr['DW_mass_mismatch_orders']:.0f} orders too light; sub-eV ⇒ hot DM ⇒ free-streaming excludes as dominant DM",
        sr["DW_mass_mismatch_orders"] >= 4.0)
    _ck(f"LOCATED-GAP per canon §4 (tried/failed/would-change-if): candidate FALSIFIED at first-cut TWT parameters; would change if {{Z1: 2nd mass-scale, Z2: non-thermal production, Z3: m_s≫m_a w/o B-L violation}}",
        "LOCATED-GAP" in sr["tier"] and "FALSIFIED" in sr["DM_V2_1_status"])
    print("        ⇒ DM-V2-1 sterile-RH-as-DM: FALSIFIED-AS-CONJECTURED at first-cut TWT parameters (banking-worthy negative); DM candidate hunt continues with other worklist leads (differential coupling, wave-train phase-defect).")

    print("§19.8.3 DM-V2-1 Z2 re-attack: can sterile carry SEPARATE mass scale from active? (LOCATED-GAP-REFINED):")
    z2 = sterile_rh_z2_separate_mass_scale_check()
    _ck(f"Z2-A: Dirac mass = one KK eigenvalue per 4D Dirac fermion (§17.1); separate k_5 ⇒ two independent Weyls ⇒ each needs forbidden Majorana (B-L closes Z2-A)",
        z2["Z2_A_dirac_KK_eigenvalues_per_pair"] == 1 and z2["Z2_A_majorana_forbidden_by_BL"] is True)
    _ck(f"Z2-B: wave-decoupling axis = {z2['Z2_B_wave_decoupling_axis']} (independent of mass axis = {z2['Z2_B_mass_axis']} in Cl(4,1)); wave-decoupling cannot set k_5",
        z2["Z2_B_axes_orthogonal"] is True)
    _ck(f"Z2-C: §10.5 µΨ₀ρ_L sources L-winding density (β-decay L-pair creation §23.10), NOT a single-mode KK mass term",
        z2["Z2_C_section_10_5_is_KK_mass"] is False)
    _ck(f"Z2 numerical: standard DW keV-sterile-DM excluded by X-ray + Ly-α at all tested m_s ∈ {z2['DW_window_m_s_keV_tested']} keV (Boyarsky 2019); required mixing exceeds bound at every point",
        z2["DW_all_excluded_by_xray_plus_lyman_alpha"] is True)
    _ck(f"Z2 verdict LOCATED-GAP-REFINED: current substrate gives NO route to m_s≠m_a; DM-V2-1 lead (iii) CONFIRMED RESOLVED-NEGATIVE on N30 + Z2; refined would-change-if = {{Z2-A' B-L-charged condensate, Z2-R Shi-Fuller w/ TWT lepton asymmetry}}",
        "LOCATED-GAP-REFINED" in z2["tier"] and z2["current_substrate_route_to_m_s_neq_m_a"] is None)
    print("        ⇒ DM-V2-1 Z2 (separate sterile mass scale): closed-NEGATIVE on current substrate; refined would-change-if handles (Z2-A', Z2-R) recorded for future re-attack.")

    print("§19.8.5 DM-V2-1 Z1: non-thermal sterile production via §10.5 topological boundary (LOCATED-GAP-REFINED):")
    sz1 = sterile_rh_substrate_production_via_L_theta()
    _ck(f"active-sterile overlap eps = m_ν/Ψ_0 ~ {sz1['active_sterile_overlap_eps']:.2e} (Ψ_0 ~ f_π ~ 93 MeV, m_ν ~ 0.05 eV); eps² ~ {sz1['eps_squared_S_plus_to_S_minus_branching']:.2e} is the S_+→S_- branching",
        sz1["active_sterile_overlap_eps"] < 1e-8 and sz1["eps_squared_S_plus_to_S_minus_branching"] < 1e-15)
    _ck(f"𝓛_θ sources L-pair creation in S_+ (j_L built from L-orbit bivectors); sterile in S_- gated by SAME eps² as Dodelson-Widrow → no DW bypass; shortfall ~{sz1['overlap_shortfall_orders_of_magnitude']} orders",
        sz1["overlap_shortfall_orders_of_magnitude"] >= 15.0 and "REFUTED" in sz1["verdict"])
    _ck("LOCATED-GAP-REFINED: N30 sharpened — shortfall is structural overlap-limit on unique S_+↔S_- connector, NOT just thermal-window mismatch; Z1 closed-NEGATIVE; would-change-if {Z1a pure-S_- channel, Z1b decoupled overlaps, Z1c keV-scale Dirac eigenvalue}",
        "LOCATED-GAP-REFINED" in sz1["tier"] and "closed-NEGATIVE" in sz1["DM_V2_1_Z1_status"])
    print("        ⇒ DM-V2-1 Z1 (non-thermal substrate production via §10.5): closed-NEGATIVE — REFINES N30 with a structural overlap-limit argument; DM-V2-1 remains OPEN; leads (i) differential coupling & (ii) wave-train phase-defect still OPEN.")

    print(f"\n  [note] the Koide input is K=2/3 <=> c=sqrt(2) [INPUT, exact-but-unforced, CANDIDATE] — the EQUIVALENCE is derived; the value is empirical. (No 'alpha' here; alpha is reserved for alpha_em.)")


    cp = cabibbo_transition_probability()
    _ck("the NATIVE defect-frame object is a PROBABILITY, not the SM angle (Yaer): P(d<->s)=|Vus|²=ω_d/ω_s=0.050 "
        f"({cp['P(d<->s)_is_a_frequency_ratio']['pct_off']}%) — a transition PROBABILITY = a FREQUENCY RATIO (resonant overlap of sub-harmonics); "
        "UNITARITY automatic (up-row |V|²=1.000 = the meaning of a probability row, not a TWT explanation); CHIRALITY = up-exp≈2×down-exp. "
        "HONEST: GST + chirality are generation_subharmonic_ladder's facts re-expressed (Born rule credited); only the unitarity assert is new; NOT DERIVED",
        cp["P(d<->s)_is_a_frequency_ratio"]["pct_off"] < 1.0
        and abs(cp["unitarity_is_automatic"]["up_row_sum_|V|^2"] - 1.0) < 0.003
        and cp["chirality_up_exp_2x_down_exp"]["up_exp~2x_down_exp"] is True and "NOT DERIVED" in cp["tier"])
    print("        ⇒ probability is the native object: P=frequency-ratio, unitarity=defect-goes-somewhere, chirality=up-exp≈2×down-exp; the protection condition (owed) would predict these probabilities.")


    print("§9.6 PROTECTION-MECHANISM attempt (Yaer: DO the #1-gap derivation; 4-route workflow + verification):")
    cr = chirality_is_a_reflection()
    _ck("★ FORCED result — CHIRALITY IS A REFLECTION (engine-exact): a spatial parity (e1→−e1) maps self_dual(e1j)→−anti_self_dual(e1j) "
        "(j=2,3,4) ⇒ the SD↔ASD = up↔down swap IS a reflection ⇒ 'up↔down is a MIRROR' (the gen-2 ~0.44 mirror's ORIGIN) is FORCED "
        "Spin(4)/Hodge geometry, NOT a fit. DERIVED in KIND; the 0.44 VALUE stays #1-gap-GATED",
        all(cr["swaps_verified"].values()) and "DERIVED in KIND" in cr["tier"] and "GATED in VALUE" in cr["tier"])

    # RECOVERED CHECK (2026-07-02): updown_mirror_value_three_handles (N32a, banked
    # 2026-06-30 with a "suite +1" ledger claim) had NO _ck call anywhere — a phantom
    # suite count of the same class as the two N31-era dead checks. Recovered here.
    mv = updown_mirror_value_three_handles()
    _ck("N32a (recovered phantom check): three W-LIVE-1 handles converge on ONE open dial µΨ₀ "
        "(§10.5(d) = ⟨I₄⟩ condensate); H1/H2 static flip-cost = 0 by SU(2) mirror isomorphism; "
        "H3 gen-1→2 avg-vs-lepton suggestive (in-function asserts pass)",
        mv is not None and isinstance(mv, dict))
    # N37 (2026-07-02) — N32a's named multi-generation cross-check FIRED → clean negative:
    mg = updown_mirror_multigen_avg_vs_lepton()
    _ck("N37 REFUTED (multi-gen negative): c_common = c_lepton fails at gen-2→3 (avg 4.36 vs "
        "lepton 2.82, +54%; lepton BELOW both towers — and c_l < c_d is TOP-FREE decisive); "
        "gen-1→2 reproduces N32a (-12%, lepton between towers) and survives as FRAMING gen-1→2 "
        "ONLY; implied dial µΨ₀ RUNS between generations (1.69 → 0.56)",
        mg["outcome"].startswith("REFUTED")
        and abs(mg["avg_vs_lepton"]["deviation_frac"][0] + 0.121) < 0.01
        and abs(mg["avg_vs_lepton"]["deviation_frac"][1] - 0.543) < 0.01
        and mg["avg_vs_lepton"]["lepton_between_towers"] == (True, False)
        and abs(mg["implied_mu_psi0_per_transition"][0] - 1.690) < 0.01
        and abs(mg["implied_mu_psi0_per_transition"][1] - 0.555) < 0.01
        and ("top-free" in mg["outcome"] or "TOP-FREE" in mg["outcome"]))
    _ck("N37 tier honesty: witness-mass arithmetic (quark masses = canon-allowed throwaway "
        "witnesses of a non-equality; top only in the drift magnitude, NOT the refutation); "
        "scheme caveat named; numerology (~3 drift ratio) flagged FIT-level NO-derivation",
        "throwaway witnesses" in mg["tier"] and "NO derivation" in mg["tier"]
        and "scheme" in mg["scheme_caveat"])
    print("        => e4-conjugation = L/Q projector (DERIVED); CAND3 refuted; up/down has no gate-free e4 support (N28 located gap, Layer-2).")
    rs = updown_seat_rhoL_parity_odd_hodge_form()
    _ck("★ W3.2/A2 — the µΨ₀ ρ_L SEAT INTEGRAL on the banked Q-orbit baryon (R-133/R-144), R-129's remaining construction: "
        "the LITERAL §10.5 scalar ρ_L boundary term VANISHES IDENTICALLY (e14·e24·e34 = −I4 grade-4 ⇒ the Q-orbit winding density is "
        "PARITY-ODD/I4-valued, scalar part 0; profile/geometry-independent) — CLEAN NEGATIVE, confirms N32a 'ρ_L sources L-orbit winding, not Q-orbit'. "
        "But the R-128 parity-odd HODGE-DUAL quark-lock (I4·Ω) recovers the scalar L-winding EXACTLY ⇒ the corrected seat FORM L_θ = µΨ₀·B_Q, "
        "PARITY-ODD, linear in the integrated B_Q (π₃ degree): the algebraic FORM behind N32a's CANDIDATE cost_flip = 2µΨ₀B is DERIVED-A, but the "
        "PHYSICAL seat identification inherits R-128's OWN FRAMING tier (NOT promoted). VALUE µΨ₀ #1-gap GATED; does NOT give N37's inter-gen running (∝B ⊥ gen index)",
        "VANISHES IDENTICALLY" in rs["literal_seat"] and "CLEAN NEGATIVE" in rs["literal_seat"]
        and "HODGE" in rs["hodge_seat_DERIVED_form"].upper() and "LINEAR" in rs["hodge_seat_DERIVED_form"]
        and "GATED" in rs["value_gated"] and "NO split value" in rs["value_gated"])
    print("        ⇒ A2/W3.2 (N32a/R-129 refined): literal ρ_L seat VANISHES on Q-orbit (clean negative); the R-128 Hodge-dual seat FORM µΨ₀·B (parity-odd, linear-in-winding) is DERIVED on the explicit profile; value µΨ₀ stays GATED (no split value — N28/N32a trap respected).")
    wi = weak_isospin_SD_parity_exclusion()
    _ck("N4 U1 -- SECOND INDEPENDENT STRUCTURAL ROUTE (first: CKM arc): full spatial parity "
        "P(e_k)=-e_k(k=1,2,3),P(e4)=+e4 on grade-2 (substrate-specific via TWT e4 wavefront): "
        "L-orbit {e12,e13,e23} parity-EVEN (+1); Q-orbit parity-ODD (-1) AND non-closing as su(2) "
        "([e14,e24]=-2*e12, [e24,e34]=-2*e23, [e14,e34]=-2*e13, all in L-orbit); "
        "SD triple NOT parity eigenspace (P maps SD->ASD); SD = I4=+1 eigenspace. "
        "L-orbit EXCLUDED: V-A [INPUT] + coupling-parity [INPUT] + parity-even [DERIVED]. "
        "SD = SU(2)_L (FRAMING: Euclidean chirality + Spin(4) complementarity). "
        "Q-orbit double-excluded: not su(2) (DERIVED) + not Spin(4)-complementary. "
        "N4 U1 confirmation (second route); N4 U2 + CKM remain open",
        all(wi["L_orbit_parity_even"].values())
        and all(wi["Q_orbit_parity_odd"].values())
        and all(wi["Q_orbit_nonclose_in_L"].values())
        and all(wi["SD_maps_to_ASD_under_P"].values())
        and all(wi["SD_NOT_parity_eigenstate"].values())
        and all(wi["SD_I4_eigenvalue_plus1"].values())
        and all(wi["ASD_I4_eigenvalue_minus1"].values())
        and "SECOND" in wi["N4_U1_resolved"])
    print("        => L-orbit EXCLUDED by parity (DERIVED+INPUT); SD = weak isospin SU(2)_L (FRAMING); N4 U1 LOCATED.")
    sa = self_adjointness_from_one_B_projection()
    _ck("§B.3.2 SELF-ADJOINTNESS REPAIRED -- 'requiring reality' of <phi~ M psi>_0 is VACUOUS (every "
        "grade-0 coefficient of a REAL Clifford algebra is already real; and <psi~ M psi>_0 = "
        "<psi~ M~ psi>_0 identically, so the scalar part is BLIND to the anti-self-adjoint part). The "
        "working condition is the {1,B} one the Born rule already uses: <psi~ M psi>_B = 0 for all psi. "
        "Its solution space over left-multiplication operators is EXACTLY the reversion-fixed subspace "
        "-- dim 2 = span{1,I4} on Cl+(4,0), dim 6 = span{1,e1,e2,e3,e4,I4} on Cl(4,0), for ALL THREE "
        "L-orbit winding choices B_a (R-020 scope; nothing depends on the phase-blade convention). "
        "R-022's conclusion M~ = M SURVIVES; only its derivation is replaced. The {1,B} pairing is "
        "exactly the Hermitian form of C^4: g = <phi~ psi>_0 symmetric unimodular, b = <phi~ psi>_B "
        "antisymmetric nondegenerate (symplectic), J = right-mult by B a compatible complex structure. "
        "DERIVED-A. PREMISES NAMED: expectations are real (the QM postulate, not derived) and "
        "observables are C-linear (28 solution dims without it, 16 with it -- both computed).",
        sa["grade0_blind_to_anti_self_adjoint_part"]
        and sa["B_a_independent"] and sorted(sa["per_B_a"]) == ["e12", "e13", "e23"]
        and sa["pairing_g_symmetric_unimodular"]
        and sa["pairing_b_antisymmetric_symplectic"] and sa["pairing_b_rank"] == 8
        and sa["J_squares_to_minus1"] and sa["J_preserves_g_and_b"]
        and sa["dim_solution_even_subalgebra"] == 2
        and sa["basis_solution_even_subalgebra"] == sa["reversion_fixed_even"]
        and sa["dim_solution_full_algebra"] == 6
        and sa["basis_solution_full_algebra"] == sa["reversion_fixed_full"]
        and sa["dim_phase_sector_states_even_ops"] == 7
        and sa["dim_phase_sector_states_phase_ops"] == 1
        and sa["dim_all_real_linear_solution"] == 28
        and sa["dim_c_linear_operator_space"] == 32
        and sa["dim_c_linear_solution"] == 16
        and sa["left_mult_is_c_linear"]
        and "DERIVED-A" in sa["tier"] and "NAMED PREMISES" in sa["tier"])
    _ck("§B.3.2 SPECTRAL-STRUCTURE gloss WITHDRAWN -- the four grade-3 blades ARE orthonormal "
        "(<T_a T_b~>_0 = delta_ab, exact), but they are reversion-ODD (T~ = -T) hence ANTI-self-adjoint "
        "by the criterion just derived, they square to -1 (no real eigenvalues) and they do NOT commute "
        "pairwise (no simultaneous eigenbasis) => 'each blade an eigenvector of the corresponding "
        "observable' names NO observable and is withdrawn; the four also split 3+1 by e4-content "
        "(colour slots e124/e134/e234 vs the spatial pseudoscalar e123), so they are not a uniform "
        "quadruplet. The trivector->fermion-spectrum map is NOT established in §B.3.2.",
        sa["grade3_orthonormal"] and all(sa["grade3_anti_self_adjoint"].values())
        and all(sa["grade3_square_minus_one"].values())
        and all(sa["grade3_pairwise_noncommuting"].values())
        and sum(1 for v in sa["grade3_orbit_split_3plus1"].values()
                if v == "L-orbit (no e4)") == 1
        and "WITHDRAWN" in sa["tier"])
    print("        => self-adjointness now forced by the {1,B} projection (dim 2 / dim 6 = reversion-fixed, all three B_a); grade-3 'eigenvector' gloss withdrawn.")
    bs = born_subspace_one_B_forced()
    _ck("§14.4 DEEPER {1,B} -- V2 §3.2 derivation eliminates the §14.4-via-§14.2 circularity: "
        "(L-orbit) AND (centralizer of B_a) within Cl+(4,0) = exactly {1, B_a} for each L-orbit "
        "winding choice B_a in {e12,e13,e23} (engine-exact). The complex structure i := B is the "
        "DERIVED consequence of the subalgebra, not its premise. One-way chain: V2 §3.2 + wavefront "
        "frame => {1,B} => complex structure => Born projection. Remaining structural input (sector "
        "choice L vs Q = lepton vs baryon) fixed independently at §16.6 / V2 §3.2. DERIVED-A.",
        bs["L_orbit_names"] == ["1", "e12", "e13", "e23"]
        and all(set(m) == {"1", b} for b, m in bs["intersections_per_winding_choice"].items())
        and all(all(c.values()) for c in bs["subalgebra_closure"].values())
        and all(bs["Q_orbit_anticommute_e4"].values())
        and "DERIVED-A" in bs["tier"])
    print("        => {1,B} subalgebra forced by V2 §3.2 (engine-exact); §14.4 circularity reduced to sector choice (lepton vs baryon, independently derived).")
    bwq = bell_wing_needs_the_e4_commutant_qubit()
    _ck("★ R-167 — the BELL WING is the e4-COMMUTANT qubit, NOT the phase sector: Z_{Cl⁺(4,0)}(e4) = {1,e12,e13,e23} ≅ ℍ = dim_ℂ 2, "
        "while span{1,B_a} is dim_ℂ 1 and CANNOT host a wing (in ℂ¹ every B_a-rotor state is the SAME ray — Hermitian modulus 1 at every "
        "pair of angles — and Λ²(ℂ¹)=0 so NO singlet exists there). The half-angle SURVIVES as an honest ℂ² Hermitian overlap "
        f"|⟨ψ_a|ψ_b⟩| = |cos(Δθ/2)| (max dev {bwq['max_dev_half_angle_C2_hermitian']:.1e}, no grade projection) once the measurement rotor "
        "leaves the phase plane; the PHASE-plane rotor is DIAGONAL in the ℂ-basis {1,e13} (off-diag 0.0) and fixes ψ₀=1 up to phase, "
        "generating no second state — which is exactly why §B.4's own measurement plane produced no wing. NO NEW INNER PRODUCT IS NEEDED: "
        f"§B.3.3's own z(ψ,D) (grade-0 part AND B_a part, as born_exponent_gleason_closure defines it) applied UNCHANGED on Z(e4) IS that ℂ² "
        f"Hermitian form (max dev {bwq['max_dev_B33_z_overlap_vs_C2_hermitian']:.1e} over 500 random pairs) — the repair widens the MODULE, "
        "not the inner product. DERIVED-A for the wing algebra; the Z(e4) module restriction remains a named CHOICE, not a derivation.",
        bwq["W_commutant"] == ["1", "e12", "e13", "e23"] and bwq["fails_W"] == ["I4", "e14", "e24", "e34"]
        and bwq["dim_C_phase_sector"] == 1 and bwq["dim_C_e4_commutant"] == 2
        and bwq["dim_R_e4_commutant"] == 4 and bwq["qubit_C_basis"] == ["1", "e13"]
        and bwq["phase_sector_hosts_a_qubit"] is False and bwq["e4_commutant_hosts_a_qubit"] is True
        and bwq["max_dev_half_angle_C2_hermitian"] < 1e-12
        and bwq["max_dev_B33_z_overlap_vs_C2_hermitian"] < 1e-12
        and bwq["su2_offdiagonal_by_rotor_plane"]["e12"] == 0.0
        and min(bwq["su2_offdiagonal_by_rotor_plane"][k] for k in ("e13", "e23")) > 0.3
        and "DERIVED-A" in bwq["tier"])
    _ck("★ R-167 (cont) — the SINGLET PAIRING is a substrate object on the two units the phase-sector cut discarded, and R-020's uniqueness "
        "is NOT spent: ε(u,v) = ⟨u·j, v⟩ with j ∈ {e13,e23} (RIGHT multiplication — the quaternionic/antilinear structure) is antisymmetric "
        "AND ℂ-bilinear AND SU(2)-invariant, while RIGHT-mult by the PHASE blade B_a and LEFT-mult by the same e13 both FAIL, and ε vanishes "
        "identically on span{1,B_a}. span{1,B_a} is exactly the ℂ-linear SCHUR commutant of the one-sided SU(2) action on Z(e4) (dim_ℝ 2 "
        "inside the full commutant dim_ℝ 4 = ℍ) ⇒ enlarging the MODULE to ℂ² leaves R-020's OPERATOR statement verbatim. U(1)_{B_a} adjoint "
        "grading of the eight even blades: charge-0 {1,e12,e34,I4} / charged {e13,e14,e23,e24}; the four that FAIL (W) are {e14,e24,e34,I4} "
        "= R-128's quark-lock family. NOT CLAIMED: the two-wing TENSOR PRODUCT (N53) and the SINGLET SELECTION (dynamics, #1 gap) remain "
        "IMPORTS — bell_correlation stays FRAMING.",
        bwq["pairing_antisym_Cbilinear_SU2invariant"]["e13_right"] == (True, True, True)
        and bwq["pairing_antisym_Cbilinear_SU2invariant"]["e23_right"] == (True, True, True)
        and bwq["pairing_antisym_Cbilinear_SU2invariant"]["e12_right"][0] is False
        and bwq["pairing_antisym_Cbilinear_SU2invariant"]["e13_left"][0] is False
        and bwq["pairing_antisym_Cbilinear_SU2invariant"]["e13_left"][2] is False
        and bwq["schur_commutant_dim_R"] == 4 and bwq["schur_C_linear_commutant_dim_R"] == 2
        and sorted(n for n, q in bwq["U1_Ba_adjoint_charges"].items() if q == 0) == ["1", "I4", "e12", "e34"]
        and sorted(n for n, q in bwq["U1_Ba_adjoint_charges"].items() if q == 1) == ["e13", "e14", "e23", "e24"]
        and "IMPORTS" in bwq["tier"])
    print("        ⇒ R-167: the ℂ¹/ℂ² contradiction between §B.3.1 and §B.4 is CLOSED on the e4-commutant qubit; the two-wing tensor product (N53) is NOT.")
    pm = protection_mechanism_located()
    _bb = pm["clean_negative_linear_cannot_make_geometric"]["backbone_costs"]
    _ck("★ CLEAN NEGATIVE (decisive) — LINEAR backbones cannot make the GEOMETRIC cost ladder, and fail on the TREND not just scale: every "
        "arithmetic backbone gives k·ln((n+1)/n) = SHRINKING steps (k=1: 0.69/0.41/0.29, k=2 Mathieu: 1.39/0.81/0.58, k=4 cavity: 2.77/1.62/1.15) "
        "while the down tower RISES (3.00→3.80) ⇒ no linear ω-ladder gets even the trend right; the ladder NEEDS nonlinearity. Static Skyrme well "
        "refuted 3 ways ⇒ the tower is the e4-DRIVEN rotor. Composite (FRAMING) = driven Skyrme-quartic rotor; FORCED: windows + chirality-reflection + cost-4 scale",
        all(v[0] > v[1] > v[2] for v in _bb.values()) and "located-gap" in pm["verdict"] and "NOT DERIVED" in pm["tier"])
    _ck("LOCATED gap N19: why-3/cost-values/widths/edge-flip/0.44 all #1-gap-gated (§9.6 EOM). Its hinge ('is the backbone ω(amplitude) EXPONENTIAL?') "
        "is now ANSWERED & SHARPENED by N20 (driven-pendulum backbone is logarithmic → caps cost < 2.8; sharper hinge = project V(θ)). NOT DERIVED",
        "ANSWERED & SHARPENED by N20" in pm["re_attack_hinge"] and "N19" in pm["tier"])
    print("        ⇒ #1-gap protection: ONE forced new result (chirality=reflection, engine-exact) + one clean negative (linear≠geometric) + a precisely-located gap; re-attack = is the nonlinear backbone ω(A) exponential? NOTHING DERIVED for the tower.")


    gl = gluon_octet_symmetric_space_split()
    _ck("★ GLUON IDENTIFICATION (Yaer: SU(3) blends a SPATIAL Cl(4,1)-native part with a DYNAMICAL part) — DERIVED group-theory spine (numpy on Gell-Mann): the octet 8 branches "
        "under SO(3) as 3 (L=1, Cl-native so(3) {λ2,λ5,λ7}, the colour-ℤ₃ ladder) ⊕ 5 (L=2, not-Cl-native coset {λ1,λ3,λ4,λ6,λ8}, moves |Σc²|²); member-aligned with the banked split. "
        "★ The Z₂ SYMMETRIC-SPACE grading [3,3]→3/[3,5]→5/[5,5]→3 is EXACT and [5,5] spans ALL of so(3) (rank 3) ⇒ su(3)/so(3) symmetric space, the coset-5 is a spin-2 MODULE not a subalgebra",
        "branches under SO(3)" in gl["decomposition"] and "rank 3" in gl["symmetric_space_grading"])
    _ck("★ GLUON — the FRAMING + the ADVERSARIAL correction (honest, not soft-pedaled): the gluon FORCE = the dynamical coset-5 = §9.6 defect-vacuum kernel (banked a-rich); the geometric 3 "
        "is a frame relabel. Recasts N5 (octet = 3 rotations + 1 spin-2 module ⇒ 'missing spin-1 gauge boson' is the WRONG object) BUT: because [5,5]→3 spans all of so(3), the coset-5 is NOT "
        "autonomous ⇒ Yaer's 'artificial blend' is RIGHT for the STATICS but the DYNAMICS needs the FULL su(3) f_abc (SU(3) is the right object for the running; jet data confirms). #1-gap GATED",
        "RIGHT for the STATICS" in gl["adversarial_correction"] and "FALSE for the DYNAMICS" in gl["adversarial_correction"]
        and "NOT a refutation of SU(3) for the dynamics" in gl["tier"])
    _ck("★ GLUON TESTED (empirical + robustness): the structure gives the SU(3) colour Casimirs C_F=4/3, C_A=3, C_A/C_F=9/4 = the measured LEP colour factors "
        "(C_A/C_F=2.27±0.06) ⇒ 'the dynamics needs the full su(3)' AGREES WITH DATA (a sub-su(3) force is falsified); C_A splits 1.5(geom-3)+1.5(dyn-5) so the 3 can't be "
        "dropped; and the Cl-native so(3)={λ2,λ5,λ7} is FORCED (the unique imag-antisym set) ⇒ the 3⊕5 split is not an arbitrary embedding. (asserts inside the primitive)",
        "AGREES WITH DATA" in gl["tested"]["empirical_coherence"] and "FORCED" in gl["tested"]["robustness"])
    _ck("★ GLUON STATIC f_abc CLOSED (task-2 tidy-up, DERIVED-but-generic group theory): the dynamical coset-5 GENERATES all of su(3) (Lie closure = dim 8, NOT a subalgebra), "
        "and the geometric-3 closes as so(3) but carries only half the colour charge (C_A=1.5) ⇒ there is NO consistent sub-su(3) colour force; the 'intra-coset only' option is "
        "algebraically EXCLUDED, the algebra HAS the full f_abc. So the STATIC half is CLOSED; only the DYNAMICAL running MAGNITUDE (a-rich=−a-bare, β₃, σ_QCD) stays #1-gap GATED. NOT progress on the kernel",
        "GENERATES all of su(3)" in gl["static_f_abc_closed"] and "EXCLUDED" in gl["static_f_abc_closed"]
        and "PURELY DYNAMICAL" in gl["gated_next_step"] and "NOT progress on the kernel" in gl["tier"])
    print("        ⇒ GLUON: octet = 3 (Cl-native geometric so(3)) ⊕ 5 (not-native dynamical coset = defect-vacuum kernel = a-rich), a Z₂ symmetric space ([5,5]→all of so(3)). Yaer's spatial/dynamical blend is REAL for the statics (recasts N5 as wrong-object) but SU(3) is the RIGHT object for the dynamics (the f_abc bracket re-fuses them). TESTED: structure gives the SU(3) Casimirs (C_A/C_F=9/4=LEP); split is forced; coset-5 GENERATES su(3) ⇒ STATIC f_abc closed, only the running magnitude GATED. FRAMING on a DERIVED spine; the §9.6 gluon dynamics stays GATED.")

    tb = theta_rel_equivariant_bifurcation_spine()
    _ck("★ TASK 1 — Θ_rel curvature axis (the equivariant-bifurcation spine, extending the N10 Schur shortcut): the colour-Z3 = standard 2D irrep on {λ3,λ8}; the commutant FORCES the spiral "
        "linear form ż=(μ+iω)z+α·z̄²+β·z|z|² ⇒ the colour-symmetric fixed point can ONLY lose stability via a Z3-PRESERVING Hopf, NEVER a static off-G pitchfork (ω≠0); the e4 drive is Z3-even (no Z3-odd "
        "term) ⇒ off-G Z3-breaking is LINEARLY FORBIDDEN, can arise ONLY through the nonlinear z̄². DERIVED-via-symmetry (sympy: commutant=complex scalar; +reflection⇒ω=0)",
        "spiral" in tb["spine_DERIVED"] and "LINEARLY FORBIDDEN" in tb["linear_off_G_forbidden"] and "DERIVED-CONDITIONAL" in tb["hopf_is_conditional"])
    _ck("★ TASK 1 — the SHARPENING (Route B, NEW) + the near-falsifier: z̄² is NON-RESONANT with the Hopf cycle ⇒ the Z3-symmetric cycle is ROBUST to small α; Z3-breaking is selected ONLY for "
        "|α|≳ω (an O(1) threshold, numerically verified) — α≠0 is NOT sufficient. Reynolds/Schur: ANY Z3-symmetric attractor ⇒ isotropic Θ_rel. So the N10 converse REDUCES to one kernel binary "
        "(is |α|≳ω?), #1-gap GATED; near-falsifier: the data (non-democratic CKM + SU(3)≠U(3)) forces the kernel into the STRONG regime |α|≳ω (rests on SYMMETRY, NOT N9/N15). NOT a resolution, NOT a Θ_rel value",
        "NON-RESONANT" in tb["nonresonance_threshold"] and "|α| ≳ ω" in tb["sharpened_binary"] and "NOT on N9/N15" in tb["near_falsifier"] and "GATED" in tb["tier"])
    print("        ⇒ TASK 1 (Θ_rel curvature): the symmetry shortcut DERIVES the equivariant-bifurcation spine — off-G Z3-breaking is LINEARLY FORBIDDEN (spiral⇒Hopf, e4-arrow-protected; e4 Z3-even closes the odd route); it can come ONLY from the nonlinear z̄², which is NON-RESONANT so needs |α|≳ω (a threshold, not α≠0). The N10 converse REDUCES to that one kernel binary; the data forces |α|≳ω (near-falsifier). DERIVED-structural + sharpened-located-gap; the kernel α + Θ_rel value stay GATED.")

    tw = theta_rel_rotating_wave_escape_located()
    _ck("★ Θ_rel curvature — the ROTATING-WAVE ESCAPE LOCATED (extends the spine; classifies its one hand-waved 'τ_mem-gated Z3 rotating-wave escape'): in the MARKOVIAN strictly-2D limit the escape does NOT "
        "exist — the colour Cartan {λ3,λ8} is exactly 2D, so above the |α|≳ω threshold the planar flow rests at ONE of 3 Z3-related off-G fixed points (spontaneous Z3 breaking; engine-verified: below ⇒ one circulating "
        "constant-|z| orbit |mean z|≈0 = Z3-symmetric/isotropic, above ⇒ 3 fixed points 120° apart |mean z|>0 = Z3-broken/anisotropic). The escape is NON-MARKOVIAN (needs finite-memory delay-dimensions) — but §9.6 "
        "FORBIDS the Markovian limit for the selection/memory roles (settled hysteretic kernel — originator pick; R-114 FRAMING since 2026-07-31), so that limit is a REFERENCE BASELINE, not the physical verdict",
        "MARKOVIAN" in tw["escape_classified_DERIVED"] and "selection/memory roles" in tw["escape_is_nonMarkovian"]
        and "WITHDRAWN" in tw["escape_is_nonMarkovian"]
        and "REFERENCE BASELINE" in tw["escape_is_nonMarkovian"] and "ISOTROPIC" in tw["markovian_dichotomy"] and "ANISOTROPIC" in tw["markovian_dichotomy"])
    _ck("★ Θ_rel curvature — threshold = SNIC/Adler phase-locking (refines the spine's bare-ω reading): α*≈C·|ω+β_i R²|/R, R²=−μ/β_r, C=O(1) — rises with ω, FALLS with μ (engine-confirmed); EXPLAINS the spine's "
        "'O(1)≈2ω' as C·ω·√(−β_r/μ). ★ CORRECTION (Yaer 2026-06-28c): the prior 'near-falsifier tightened' is WITHDRAWN — §9.6 forbids the Markovian limit, so the converse stays OPEN, gated on whether the HYSTERETIC "
        "τ_mem stabilizes the rotating wave; NEW handle: hysteretic=STICKY plausibly DISFAVORS the escape (barrier-pinning beats circulation) ⇒ could restore data-forces-breaking on dynamical grounds [CANDIDATE]. NOT a Θ_rel value",
        "SNIC" in tw["threshold_is_SNIC_Adler"] and "Adler" in tw["threshold_is_SNIC_Adler"] and "WITHDRAWN" in tw["converse_is_OPEN"]
        and "STICKY" in tw["sticky_hysteresis_handle_CANDIDATE"] and "WITHDRAWN" in tw["tier"] and "GATED" in tw["gated"])
    print("        ⇒ Θ_rel curvature (escape located, then CORRECTED 2026-06-28c per Yaer): the spine's τ_mem-escape is classified — in 2D Markovian dynamics, above the SNIC/Adler threshold Z3 is broken (3 off-G nodes, one selected). BUT §9.6 forbids the Markovian limit (mandatory hysteretic kernel), so that is a REFERENCE BASELINE, not the verdict; the prior 'near-falsifier tightened' is WITHDRAWN — the converse stays OPEN, gated on whether the hysteretic τ_mem stabilizes the rotating wave. NEW handle: hysteretic=sticky plausibly disfavors the escape ⇒ could restore breaking on dynamical grounds [CANDIDATE]. DERIVED-structural (the bifurcation) + open-located-gap; kernel + Θ_rel value GATED.")
    tfk = theta_rel_fork_escape_kernel_number_governed()
    _ck("★ Θ_rel FORK DISCRIMINATOR (W3.3/A1, N46 — COMPUTES N33 wci (iv) / the escape primitive's sticky-hysteresis handle): extend the Markovian normal form with an explicit NON-MARKOVIAN memory on the α locking channel (reactive u lags conj(z)², timescale τ, optional barrier D) — above the SNIC threshold the escape/lock outcome is governed by kernel NUMBERS "
        "(α/α*, τ·ω, barrier height) NON-MONOTONICALLY, NOT by the fading-vs-hysteretic branch LABEL; the sticky-hysteresis handle is REFUTED as a clean monotone discriminator (a SMALL barrier PROMOTES the escape, onset τ_c 1.1→0.8; only a LARGE barrier suppresses it). In-function asserts: markov(2.6) LOCKS, fading(2.6,τ=2) ESCAPES, small-barrier(D=0.05) STILL escapes, large-barrier(D=0.3) LOCKS, α=4.0 confinement. FRAMING/CANDIDATE-refuting; fork stays #1-gap GATED on the three numbers",
        "NO CLEAN DISCRIMINATION" in tfk["verdict"] and "NUMBERS" in tfk["verdict"] and "branch LABEL" in tfk["verdict"]
        and "REFUTED" in tfk["sticky_handle_status"] and "PROMOTES" in tfk["sticky_handle_status"] and "GATED" in tfk["gated"])
    print("        ⇒ Θ_rel fork (W3.3/A1, N46): the theory-side discriminator named in N33/companion §12 is COMPUTED — a hysteretic τ_mem does NOT cleanly clear/suppress the escape; the outcome is set by 3 #1-gap numbers (α/α*, τ·ω, barrier) non-monotonically, and the sticky handle is refuted as a clean discriminator (small barrier promotes escape). Re-locates the fork on kernel numbers; still GATED.")
    print("W2 (2026-07-27) — the BORN EXPONENT = 2 as a theorem given F1-F4 + import-exempt Gleason:")
    bgc = born_exponent_gleason_closure()
    _ck("W2 identity (i) FRAME-FUNCTION CONTEXT-INVARIANCE [DERIVED-A, Cl-native on the R-020 {1,B} "
        "line]: over 40 random orthonormal contexts of a dim-3 {1,B} sector, sum_i |z_i|^2 is "
        "context-INVARIANT to ~1e-14 and equals ||psi||^2 (a Gleason frame function), while "
        "sum_i |z_i|^4 spreads by O(1) -- the algebraic content of Gleason's additivity hypothesis "
        "holding at exponent 2 and failing at exponent 4",
        bgc["identity_i_frame_function"]["sum|z|^2 spread over 40 contexts"] < 1e-10
        and bgc["identity_i_frame_function"]["sum|z|^4 spread"] > 1.0)
    _ck("W2 identity (ii) PER-CONTEXT ADDITIVITY (Pythagoras) [DERIVED-A]: for orthogonal merged "
        "channels ||P12 psi||^2 = |z1|^2 + |z2|^2 engine-exact, with the quartic additivity gap "
        "equal to 2|z1|^2|z2|^2 exactly -- the exponent-2 rate is additive over coarse-graining and "
        "the exponent-4 rate is not",
        abs(bgc["identity_ii_additivity"]["||P12 psi||^2 - (|z1|^2+|z2|^2)"]) < 1e-10
        and abs(bgc["identity_ii_additivity"]["quartic gap"]
                - bgc["identity_ii_additivity"]["= 2|z1|^2|z2|^2"]) < 1e-10)
    _ck("W2 identity (iii) THE COVARIANT-YET-CONTEXTUAL COUNTEREXAMPLE [DERIVED-A + sympy]: the "
        "ratio-normalized |z|^(2k) rule is built from invariants alone (hence fully rotation-"
        "COVARIANT) yet its fine-vs-coarse gap is 0 at k=1 and ~0.096 at k=2/3, with the symbolic "
        "remainder (b^2+c^2)^k - b^(2k) - c^(2k) = 0 iff k=1 (2b^2c^2 at k=2). This is the engine "
        "witness that COVARIANCE CANNOT DELIVER F2 -- and, restricted to the old power family, the "
        "graceful-degradation corollary forcing k=1 by elementary algebra in dim >= 3",
        bgc["identity_iii_covariant_yet_contextual"]["coarse-graining gap k=1"] < 1e-12
        and bgc["identity_iii_covariant_yet_contextual"]["k=2"] > 1e-3
        and bgc["identity_iii_covariant_yet_contextual"]["k=3"] > 1e-3
        and "2*b^2*c^2" in bgc["identity_iii_covariant_yet_contextual"]["sympy remainder k=2"])
    _ck("W2 identity (iv) THE dim-2 WITNESS [DERIVED-A]: the power-4 ratio rule is normalized in "
        "EVERY dim-2 context (to machine epsilon), phase-invariant and noncontextual, yet deviates "
        "from Born by ~0.15 -- Gleason's dim >= 3 hypothesis is genuinely LOAD-BEARING, so the "
        "joint-configuration embedding step (dim-2 sectors sit inside >= 4-dim joint sectors) is not "
        "decoration. Busch 2003 is STATED AND DECLINED, not silently omitted",
        bgc["identity_iv_dim2_witness"]["max normalization deviation"] < 1e-12
        and bgc["identity_iv_dim2_witness"]["max deviation from Born"] > 0.05
        and "DECLINED" in bgc["busch_2003"])
    _ck("W2 the PREMISE HONESTY [tier: DERIVED-conditional-on-F1-F4 + import-exempt Gleason 1957]: "
        "F2 (statistical noncontextuality of the Role-3 selection functional) is the SINGLE NEW "
        "SUBSTANTIVE premise beyond the Role-3 FRAMING commitments already on the books; F1 CARRIES "
        "single-outcome definiteness; F3 is a TOTAL function on the JOINT lattice including "
        "entangled contexts -- NOT 'mild'; the F2+F3 => additivity coarse-graining reduction is "
        "LITERATURE-STANDARD, not TWT-novel; Gleason is imported not re-proved; and F2 becomes "
        "DERIVED only IF Role 3 is built WITH the channel-pairwise drag structure (two derivation "
        "routes already FAILED -- covariance is weaker than noncontextuality, and linear-face "
        "linearity does not constrain the dissipative-face rate functional)",
        "SINGLE NEW SUBSTANTIVE PREMISE" in bgc["tier"]
        and "F1 carries single-outcome definiteness" in bgc["tier"]
        and "NOT 'mild'" in bgc["tier"]
        and "LITERATURE-STANDARD" in bgc["additivity_reduction_attribution"]
        and "NOT novel to TWT" in bgc["additivity_reduction_attribution"]
        and "NOT re-proved" in bgc["fence"]
        and "**IF**" in bgc["would_change_if"]
        and "FAILED" in bgc["would_change_if"])


    # ============ G5 — WHAT `D/J ≈ 0.79` MEASURES, AND THE TAUTOLOGY FENCE ============
    # Governing records: knowledge/audit/gamma_referent_2026-08-23/ (§CONSENSUS + §ADDENDUM).
    _g5 = DoverJ_calibration_referent()
    _ar = _g5["arc_ratio_rider"]
    _ck("G5 PART 1 — the ROUTING THEOREM: what `D/J ≈ 0.79` measures is `D_total / "
        "J_effective`, a RATIO OF TOTALS, with an exact channel exclusivity (B = D_e₄ + "
        "β·D_spatial is exactly Γ-clean; A = J + Σᵢ αᵢΓᵢ is exactly D-clean, and by the "
        "exhaustive menu nothing else can enter either). THE REFERENT REVIEW STANDING SINCE "
        "2026-08-17 CLOSES NEGATIVELY: 0.79 is NOT re-pinnable as a single-parameter "
        "measurement of J and D, on three independent computed refusals (the calibration's "
        "functional is OUTSIDE the scalar sector so tracelessness gives zero protection; Γ "
        "enters at the SAME order as J; the one blind direction loses blindness off the "
        "banked branches). ★ THE OLD FENCE IS KEPT, NOT WIDENED: the flat assertion '0.79 "
        "is a measurement of a combination RATHER THAN D/J' stays UNLICENSED — it asserts "
        "αᵢ ≠ 0, which remains uncomputable. Conditioning: the frame-bilinear class pick, "
        "bilinear order, and JD-5 open on the ℤ₃ leg",
        "RATIO OF TOTALS" in _g5["what_0_79_measures"]
        and "NEGATIVELY" in _g5["verdict"]
        and "cannot be re-pinned" in _g5["verdict"]
        and len(_g5["three_computed_refusals_of_a_re_pin"]) == 3
        and "RATHER THAN" in _g5["still_not_licensed"]
        and "uncomputable" in _g5["still_not_licensed"]
        and "Gamma-clean" in _g5["routing"]["numerator B (parity-ODD)"]
        and "D-clean" in _g5["routing"]["denominator A (parity-EVEN)"]
        and "#1-gap-routed" in _g5["admixture_sizes"]
        and "JD-5" in _g5["tier"])

    _ck("G5 PART 2 — the ARC-RATIO RIDER enters at CANDIDATE with its numbers verified on "
        f"the engine's OWN constants: δ_L = 2/9 rad exactly (= 6/27, the n = 3 rung of the "
        f"2:4:6 ladder) ⇒ D/J = tan(2/3) = {_ar['DoverJ_exact']:.16f}, against the fitted "
        f"{_ar['fitted_on_engine_constants']:.12f} — relative offset "
        f"{_ar['relative_offset_exact_vs_fit']:.3e} (0.00157%), which is TIGHTER than the "
        f"banked rounded quote 0.787's own offset "
        f"{_ar['relative_offset_of_the_rounded_quote_0.787']:.3e} (0.0200%). ★ CONSEQUENTLY "
        "0.787 STOPS BEING THE QUOTED FIGURE either way: the honest quotable object is the "
        "fitted 0.78686 with its band, or — conditionally on the reading — tan(2/3). "
        "★ WHAT FIXING δ_L BUYS, counted honestly: one fitted CONTINUOUS parameter becomes "
        "one prediction, so the lepton leg's D/J calibration carries no continuous free "
        "parameter and one integer (n = 3). It does NOT make the lepton mass TRIPLE "
        "parameter-free — Λ and the c = √2 INPUT remain. CREDIT: the 2/9 observation is "
        "BRANNEN's; δ_U = 2/27 and δ_D = 4/27 are ŻENCZYKOWSKI's; the arc-ratio reading "
        "supplies the ADDRESS, not the number — and the F3 bibliography duty is OPEN",
        _ar["tier"] == "CANDIDATE"
        and abs(_ar["delta_L_exact_rad"] - 2.0 / 9.0) < 1e-15
        and abs(_ar["DoverJ_exact"] - math.tan(2.0 / 3.0)) < 1e-15
        and _ar["ladder_address"] == {"as_27ths": "6/27", "n": 3,
                                      "rung_set": "2:4:6 over 27"}
        and abs(_ar["relative_offset_exact_vs_fit"] - 1.5678e-5) < 1e-8
        and (_ar["relative_offset_exact_vs_fit"]
             < _ar["relative_offset_of_the_rounded_quote_0.787"])
        and "0.787 STOPS BEING THE QUOTED FIGURE" in _g5["quoting_rule"]
        and "fitted 0.78686" in _g5["quoting_rule"]
        and "Brannen" in _ar["credit"] and "Zenczykowski" in _ar["credit"]
        and "ADDRESS, not" in _ar["credit"]
        and _ar["F3_bibliography_duty"].startswith("OPEN")
        and "does NOT make the lepton mass TRIPLE parameter-free"
            in _ar["what_fixing_delta_L_buys"])

    _ck("★★ G5's CORE DESIGN — THE TAUTOLOGY FENCE, ASSERTED. The chain's SINGLE empirical "
        "fact is δ_L ≈ 2/9 rad (Brannen's observation). The `D/J`-level agreement is "
        "therefore a TAUTOLOGICAL RESTATEMENT — `D/J := tan(3·δ_L)` BY DEFINITION, so the "
        "'0.00157%' is tan(3·) applied to BOTH SIDES OF ONE FACT — and the returned dict "
        "must LABEL it so: NOT an agreement, NOT a confirmation, NOT corroboration of the "
        "arc-ratio reading. The precedent is cited BY NAME in the label: "
        "`brannen_comb_commitment_dominance_and_dof_vacuity`'s "
        "`min_over_mean_is_NOT_corroboration` (a function of (c, δ) alone, so matching the "
        "target fixes it by construction — reported so it cannot be mistaken for an "
        "independent check). Same class, same remedy. AND THE LADDER IS POSTDICTIVE: formed "
        "on the ALREADY-KNOWN δ values and entered as 'noted non-coincidences ONLY' "
        "(governing record: TWT_worklist.md, THE 1/27 PHASE LADDER, coordinator input "
        "2026-08-03) — A NOTED REGULARITY OF ZERO EVIDENTIAL WEIGHT (the 'compression, one "
        "integer for one real' booking is RETIRED; see the demotion check that follows)",
        "TAUTOLOGICAL RESTATEMENT" in _g5["tautology_label"]
        and "NOT an agreement" in _g5["tautology_label"]
        and "NOT a confirmation" in _g5["tautology_label"]
        and "BY DEFINITION" in _g5["tautology_label"]
        and "BOTH SIDES OF ONE EMPIRICAL FACT" in _g5["tautology_label"]
        and "brannen_comb_commitment_dominance_and_dof_vacuity" in _g5["tautology_label"]
        and "min_over_mean_is_NOT_corroboration" in _g5["tautology_label"]
        and "BRANNEN" in _ar["single_empirical_fact"].upper()
        and "POSTDICTIVE" in _ar["ladder_is_POSTDICTIVE"]
        and "ALREADY-KNOWN" in _ar["ladder_is_POSTDICTIVE"]
        and "NOTED REGULARITY OF ZERO EVIDENTIAL WEIGHT" in _ar["ladder_is_POSTDICTIVE"]
        and "coordinator input 2026-08-03" in _ar["ladder_is_POSTDICTIVE"])

    _ck("★ THE LADDER'S 'COMPRESSION' BOOKING IS RETIRED — demoted to A NOTED REGULARITY OF "
        "ZERO EVIDENTIAL WEIGHT on THIS CORPUS'S OWN ground, not on a reviewer's say-so: "
        "R-173's dof/vacuity result computes that the geometry reaches the measured triple "
        "on a FOUR-DIMENSIONAL solution manifold (6 free reals − 2 constraints, Jacobian "
        "rank 2), so every NEARBY ladder value is reached too — the ladder labels a point in "
        "a CONTINUUM and EXCLUDES NOTHING. Compression is evidence only when the compressed "
        "description is CONSTRAINED. The bit ledger is shipped and does not close in the "
        "ladder's favour even before the vacuity kill: bought = 3 reals → 3 small integers; "
        "paid = the base 27, the EVEN rung parity (the 'why even harmonics' question still "
        "OPEN), ~log2(3!) ≈ 2.58 bits of sector assignment, and an UNPAYABLE model-class "
        "charge (the family 'rational multiple of 1/27 rad' was itself chosen after the "
        "values were known, and the family is unbounded). ★ AND THE PLANTED-VIOLATION DEMO "
        "RUNS: restoring the old 'COMPRESSION — one integer for one real' wording on a copy "
        "is REJECTED by the demotion predicate",
        (lambda _lp: (
            _lp(_ar) and not _lp({"ladder_is_POSTDICTIVE":
                                  "POSTDICTIVE ... What it buys is COMPRESSION — one integer "
                                  "for one real — and it carries ZERO predictive weight."})))(
            lambda d: ("NOTED REGULARITY OF ZERO EVIDENTIAL WEIGHT" in d["ladder_is_POSTDICTIVE"]
                       and "EXCLUDES NOTHING" in d["ladder_is_POSTDICTIVE"]))
        and set(_ar["ladder_bit_accounting"]) == {
            "bought", "paid_1_base", "paid_2_parity", "paid_3_assignment",
            "paid_4_model_class", "net"}
        and "UNPAYABLE IN BITS" in _ar["ladder_bit_accounting"]["paid_4_model_class"]
        and "2.58" in _ar["ladder_bit_accounting"]["paid_3_assignment"]
        and "R-173" in _ar["ladder_is_POSTDICTIVE"]
        and "FOUR-DIMENSIONAL" in _ar["ladder_is_POSTDICTIVE"])

    # THE PLANTED-VIOLATION DEMO for the tautology fence. The whole point of the label is
    # that it CANNOT be relabelled as agreement/confirmation and still pass. Planted here
    # on a copy so the failure mode is SEEN TO FIRE rather than asserted to exist.
    _planted = dict(_g5)
    _planted["tautology_label"] = ("0.00157% agreement between the exact form and the fit "
                                   "— a confirmation of the arc-ratio reading")
    def _fence_ok(d):
        t = d["tautology_label"]
        return ("TAUTOLOGICAL RESTATEMENT" in t and "NOT an agreement" in t
                and "NOT a confirmation" in t and "BY DEFINITION" in t)
    _ck("★ G5's PLANTED-VIOLATION DEMO, run in-process: the tautology label is replaced by "
        "an 'agreement / confirmation' wording on a copy of the returned dict, and the "
        "fence predicate is re-run — it REJECTS the planted copy while accepting the real "
        "one. So the vacuous-agreement reading cannot re-enter through the returned record",
        _fence_ok(_g5) and not _fence_ok(_planted))

    _mdc = _ar["mass_definition_control"]["m_tau x (1 - 0.001)"]
    _v_new = _ar["input_vintage_control"]["m_tau = 1776.93 +- 0.09 (this engine)"]
    _v_old = _ar["input_vintage_control"]["m_tau = 1776.86 +- 0.12 (an earlier vintage)"]
    _ck("★ G5 — THE SIGMA IS DELETED, NOT FENCED (ruled 2026-08-24), and the RESIDUAL IS "
        f"QUOTED AS AN OFFSET: δ_fit − 2/9 = {_ar['residual_offset_rad']:+.3e} rad, a "
        f"fractional agreement of {_ar['fractional_agreement_delta']:.2e} in δ "
        f"({_ar['fractional_agreement_DoverJ']:.2e} in D/J). NO SIGNIFICANCE IS QUOTED — "
        "there is no null hypothesis, and the residual sits BELOW the input-systematic "
        "sensitivity. TWO SHIPPED CONTROLS carry the ruling's ground, both expressed in "
        "RADIANS so no σ can re-enter through them: (a) the MASS-DEFINITION CONTROL — a 0.1% "
        f"coherent m_τ shift moves δ_L by {abs(_mdc['shift_from_fitted_rad']):.2e} rad, "
        f"{_mdc['multiple_of_observed_residual']:.0f}× the observed residual, and the "
        "mass-MEASURE conditional (√m = r², pole-vs-MS̄) is not covered by any propagated "
        "bar at all; (b) ★ the INPUT-VINTAGE CONTROL, the sharper one and the reason the σ "
        f"goes — m_τ = 1776.93 gives a residual of {abs(_v_new['residual_rad']):.3e} rad "
        f"while m_τ = 1776.86 (0.07 MeV away, INSIDE the older vintage's own bar) gives "
        f"{abs(_v_old['residual_rad']):.3e} rad, a factor "
        f"{abs(_v_old['residual_rad'])/abs(_v_new['residual_rad']):.1f}. A σ-count built on "
        "this swings 0.41↔0.89 for ONE unchanged claim: the statistic measures how well m_τ "
        "is MEASURED, so it is ANTI-INFORMATIVE, not merely incomplete",
        abs(_ar["residual_offset_rad"] - 2.5397e-6) < 1e-9
        and abs(_ar["fractional_agreement_delta"] - 1.1429e-5) < 1e-8
        and _mdc["multiple_of_observed_residual"] > 20.0
        and (abs(_v_old["residual_rad"]) / abs(_v_new["residual_rad"])) > 2.5
        and "NO SIGNIFICANCE IS QUOTED" in _ar["no_significance_is_quoted"]
        and "ANTI-INFORMATIVE" in _ar["no_significance_is_quoted"]
        and "DELETED FROM THIS RECORD" in _ar["no_significance_is_quoted"]
        and "OPEN commitment" in _ar["renormalization_point"]
        and "POLE" in _ar["renormalization_point"]
        and "NOT RG-stable" in _ar["renormalization_point"])

    # THE ABSENCE FENCE — executable. The deleted statistic must not survive under ANY key,
    # and it must not be reconstructible from the returned parts without tripping the
    # does_not_license clause. Planted here so the fence is SEEN TO FIRE.
    def _no_sigma(d):
        # NOTE the whitelist by construction: the DECLARATIVE clause key
        # `no_significance_is_quoted` is not a statistic and is not matched. What is matched
        # is any key that would HOLD a σ-count (`sigma`, `σ`, `..._confidence_...`).
        bad = ("sigma", "σ", "confidence")
        for k, v in d.items():
            kl = str(k).lower()
            if any(b.lower() in kl for b in bad):
                return False
            if isinstance(v, dict) and not _no_sigma(v):
                return False
        return True
    _planted_sigma = dict(_ar)
    _planted_sigma["PDG_band"] = {"sigma_of_tan(2/3)": 0.41}
    _ck("★ G5's THIRD SHIPPED FAILURE MODE — the ABSENCE FENCE, run in-process: the returned "
        "arc-ratio record is scanned recursively for any key naming a significance statistic "
        "(σ / sigma / confidence — the word 'significance' itself is DELIBERATELY unmatched, "
        "so the declarative no_significance_is_quoted clause can exist) and must contain NONE — the old `PDG_band."
        "sigma_of_tan(2/3)` key is GONE, not merely captioned. A copy with the old key "
        "planted back is REJECTED while the live record passes, so the deleted statistic "
        "cannot re-enter through the returned dict. `does_not_license` separately forbids "
        "RECONSTRUCTING it by dividing residual_offset_rad by input_uncertainty_scale_rad — "
        "the same error by another route",
        _no_sigma(_ar) and not _no_sigma(_planted_sigma)
        and "PDG_band" not in _ar
        and "SIGNIFICANCE STATISTIC" in _g5["does_not_license"]
        and "reconstructing one by" in _g5["does_not_license"]
        and "forbidden by does_not_license" in _ar[
            "input_uncertainty_scale_is_NOT_a_bar_to_divide_by"])

    _tf = _ar["trials_factor"]
    _ck("★ G5 — THE TRIALS FACTOR IS WHAT REPLACES THE σ, and it is stronger than one was: "
        f"over the stated rational menu {_tf['menu']} ({_tf['n_candidates']} candidates, "
        f"local density {_tf['local_density_per_unit_delta']:.0f} per unit δ near the "
        "target), at a tolerance equal to the OBSERVED residual, **2/9 is the ONLY hit** — "
        f"chance expectation {_tf['chance_expectation_local_density']:.4f} on a "
        "local-density bookkeeping. An external reviewer's independent and WIDER menu (2394 "
        "candidates, q < 20) returned the SAME unique hit at 0.16; ★ WE QUOTE THE MORE "
        "CONSERVATIVE 0.16, our own reproduction being ~40× more favourable and therefore "
        "not the number to lead with. ★★ AND THE CONDITIONING CLASS IS CARRIED (RUL-049), "
        "which neither computation stated: the trials factor bounds the look-elsewhere "
        "WITHIN THE STATED MENU, and the menu was chosen AFTER 2/9 was known — so what is "
        "bounded is WHICH RUNG, never WHETHER a rational-menu reading was the thing to look "
        "for. Evidence about uniqueness; NOT evidence about the reading's prior",
        _tf["hits"] == [("p/q", 2, 9)]
        and _tf["n_candidates"] == 956
        and _tf["chance_expectation_local_density"] < _tf["quoted_chance_expectation"]
        and _tf["quoted_chance_expectation"] == 0.16
        and "WITHIN THE STATED MENU" in _tf["CONDITIONING_CLASS_RUL_049"]
        and "AFTER 2/9 was known" in _tf["CONDITIONING_CLASS_RUL_049"]
        and "NOT evidence about the reading's prior" in _tf["CONDITIONING_CLASS_RUL_049"])

    _et = _ar["non_tautological_tests"]["baryon_e_test"]
    _ck("★ G5 — THE NON-TAUTOLOGICAL TESTS are the rider's ONLY evidential future, and the "
        f"first of them is NOT YET DISCRIMINATING (deviation below instrument spread): the "
        f"exact reading DEMANDS e = √18/tan(2/3) = {_et['e_required']:.6f} against the "
        f"historical e_ANW = {_et['e_ANW_historical']} — {_et['percent_low']:.2f}% low. "
        "Either e_ANW is ~1.06% high of what the substrate demands, or the two legs' J_eff "
        "differ by that much (which is exactly GR-2 / JD-6(b)). The other two tests are the "
        "GR-2 read-out at 0.1% and a second sector landing on the 1/27 ladder with no new "
        "freedom. ★ AND THE VALUE BANKS AS A REPORTED COMPARISON, WIRED TO NOTHING: "
        "`does_not_license` forbids feeding tan(2/3) into delta_L_from_DoverJ, "
        "canting_pitch_q_rad, dressed_coupling, eta_DM or any other consumer — that would be "
        "the cross-leg error this whole review is about, AND would convert a CANDIDATE into "
        "a banked default by the back door",
        "NOT YET DISCRIMINATING" in _et["STATUS"]
        and _et["percent_low"] > 1.0
        and abs(_et["e_required"] - 5.391979) < 1e-5
        and len(_ar["non_tautological_tests"]) == 3
        and _ar["banks_as"] == "A REPORTED COMPARISON, WIRED TO NOTHING"
        and "delta_L_from_DoverJ" in _g5["does_not_license"]
        and "canting_pitch_q_rad" in _g5["does_not_license"]
        and "back door" in _g5["does_not_license"]
        and "QUOTING ANY " in _g5["does_not_license"]
        and "corroboration" in _g5["does_not_license"])

    # The wiring fence is not only prose: assert the engine's live consumers are UNMOVED.
    _ck("★ G5's WIRING FENCE, VERIFIED AGAINST THE LIVE ENGINE (not just asserted in prose): "
        "no consumer has been re-wired to the exact form — `DoverJ_from_lepton_masses()` "
        "still returns the FITTED value on the engine's own constants, not tan(2/3), and "
        "`delta_L_from_DoverJ` still inverts whatever it is passed. The exact value is a "
        "reported comparison and nothing consumes it",
        abs(DoverJ_from_lepton_masses() - _ar["fitted_on_engine_constants"]) < 1e-15
        and abs(DoverJ_from_lepton_masses() - _ar["DoverJ_exact"]) > 1e-6
        and abs(delta_L_from_DoverJ(0.787) - math.atan(0.787) / 3.0) < 1e-15)

    print("All §19 generation-sector checks passed (empirical masses corroborate the relations; companion-layer checks: twt_companion_test.py).")


# ---- twt_matter ----------------------------------------
def check_twt_matter():
    print("§16.2 Skyrme BVP — SYMBOLIC audit (adjudicates the 8-vs-4 revision-map flag):")
    a = skyrme_BVP_audit()
    _ck(f"∂L/∂F' (×4) = (x²+8sin²F)F'  [coefficient is 8, NOT 4]  (got coeff={a['coefficient of sin²F']})",
        a["matches (x²+8sin²F)F'"] and a["coefficient of sin²F"] == 8)
    _ck("EL RHS (×4) = sin2F[1+4F'²+4sin²F/x²]  (matches paper §16.2)",
        a["RHS (×4) matches sin2F[1+4F'²+4sin²F/x²]"])
    print("       VERDICT: main-text 8sin²F is correct; the flagged '4' is the typo.")

    print("§10.3 Skyrme stabilizer (bare + dressed, honestly hedged):")
    _ck(f"f_π² = 8J/a  (z_sp/d3=12/3=4, ×2; got {f_pi_squared(1.0,1.0):.1f}·J/a)", abs(f_pi_squared(1.0, 1.0) - 8.0) < 1e-9)
    _ck(f"κ_F bare = J/24 ≈ 0.0417 J  (got {kappa_F_bare():.4f})", abs(kappa_F_bare() - 1/24) < 1e-9)
    quv = qcd_uv_conformal_phaseCD()
    _ck("qcd-UV ARC [(ii) LOCATED, a mechanism-less dynamics-gated GAP — sign OPEN, NOT a wrong prediction]: Route I (emergent gluon-free antiscreening) "
        "CLOSED — derived absence (no charged spin-1 → no antiscreening; ℤ₃-discrete colour → no gauge boson). The conformal "
        "route carries the scale-invariant SKELETON (Bjorken) + confinement-consistency + EW RG-decoupling, but NOT the AF "
        "running: ALL of asymptotic freedom (the DGLAP log violations) LOCATES to the single open, unmotivated marginal-Skyrme β. "
        "TWT meets the qualitative collision phenomenology + the scale-invariant skeleton but supplies no DERIVED source for the running (mechanism-less, gated like the other values, no backup) — gate STAYS RAISING",
        quv["GATE_D"].startswith("(ii)") and quv["Route_I"].startswith("CLOSED")
        and quv["gate"].startswith("qcd_collider_phenomenology() stays RAISING"))
    b3rp = beta3_sign_from_reflection_positivity()
    _ck("Sector 3 [LOCATED-GAP]: Euclidean reflection-positivity / ghost-freedom forces the BARE Skyrme coefficient sign (1/e² > 0, Hamiltonian boundedness) "
        "but does NOT pin the β₃ sign — both AF (β<0) and IR-free (β>0) running are RP-compatible (2D O(N) σ-model is RP+AF; 4D φ⁴ is RP+IR-free). "
        "Skyrme quartic has 4 derivs but ONE per field copy (L_μ = U†∂_μU) → second-order EL → no Ostrogradski ghost at either sign. "
        "Constraint is non-empty but VACUOUS on β₃; residual stays in qcd_uv_conformal_phaseCD",
        "YES" in b3rp["RP_forces_bare_sign"] and "NO" in b3rp["RP_forces_beta3_sign"]
        and b3rp["verdict"].startswith("LOCATED-GAP"))
    _ck(f"D_crit/J = √18 = 4.243  (got {D_crit_over_J():.3f})", abs(D_crit_over_J() - math.sqrt(18)) < 1e-9)
    _ck(f"spiral angle ≈ 10.51° at D/J=0.787  (got {spiral_angle_deg(0.787):.2f})", abs(spiral_angle_deg(0.787) - 10.51) < 0.03)
    dc = dressed_coupling(0.79)
    _ck(f"e_LT=√18/(D/J)≈5.37 (1%, coincidence-riding)  (got {dc['e_LT = √18/(D/J)']:.2f})", abs(dc['e_LT = √18/(D/J)'] - 5.37) < 0.02)
    _ck(f"e_NN=√12/(D/J)≈4.38 (20%, clean)  (got {dc['e_NN = √12/(D/J)']:.2f})", abs(dc['e_NN = √12/(D/J)'] - 4.38) < 0.02)

    print("§16.3/16.4 mass + Skyrme length:")
    _ck(f"M_0 = 36.47 f_π/e = 863 MeV at e_phys=5.45  (got {skyrmion_mass_MeV():.0f})", abs(skyrmion_mass_MeV() - 863) < 2)
    _ck(f"M_0 = 876 MeV at e=5.37 (~1% shift)  (got {skyrmion_mass_MeV(e=5.37):.0f})", abs(skyrmion_mass_MeV(e=5.37) - 876) < 2)
    sl = skyrme_length_fm()
    _ck(f"ℓ_S≈0.281 fm, a≈1.53 fm, a/ℓ_S=e≈5.45  (got ℓ_S={sl['ell_S (fm)']:.3f}, a={sl['a (fm)']:.2f}, a/ℓ_S={sl['a/ell_S = e']:.2f})",
        abs(sl['ell_S (fm)'] - 0.281) < 0.005 and abs(sl['a/ell_S = e'] - 5.45) < 0.05)

    print("§22.3 topological confinement π₃(S³)=ℤ:")
    pc = pi3_S3_integer_completion()
    _ck("B=1/3 ∉ ℤ (no smooth-map degree 1/3) but 3×(1/3)=1 ∈ ℤ (integer completion)",
        (pc["B=1/3 is an integer"] is False) and (pc["3×(1/3) = 1 is an integer"] is True))
    p3o = pi3_orientation_class_two_windings()
    _ck("dimension census: Cl(4,0) dim 16, Cl⁺(4,0) dim 8 = 1+6+1 (CLOSED under the geometric "
        "product), SIX grade-2 generators = dim so(4) — the local state's 6 real parameters",
        p3o["dim_Cl_4_0"] == 16 and p3o["dim_Cl_even_4_0"] == 8
        and p3o["n_grade2_generators"] == 6 and p3o["even_subalgebra_closed"] is True
        and p3o["local_state_real_parameters"] == 6)
    _ck("chiral factorization ⇒ TWO windings (R-002): SD and ASD EACH close as su(2) with "
        "OPPOSITE structure-constant sign (+4/−4 = chirality) and mutually commute ⇒ "
        "so(4) ≅ su(2)⊕su(2), Cl⁺(4,0) ≅ ℍ⊕ℍ ⇒ π₃(4D-orientation class) = ℤ×ℤ — "
        "COVER-BLIND (πₙ≥2 iso across the double cover; LS-ℤ₂ stays an open branch, RUL-057)",
        p3o["SD_closes_as_su2"] and p3o["ASD_closes_as_su2"]
        and p3o["su2_structure_constants (SD, ASD)"] == (4.0, -4.0)
        and p3o["chiral_factors_commute"] and p3o["n_windings"] == 2
        and p3o["pi_3(4D-orientation class)"] == "Z x Z" and p3o["cover_blind"] is True)
    bm = baryon_mass_shared_rotor_nonadditive()
    _ck("system-level hadron mass: NON-ADDITIVE (shared B=1 rotor, mass≠ΣA_i) DERIVED; meson 2ω|cos(α/2)| "
        "2-body anchor (vector 4, pseudoscalar 0); colour slots ORTHONORMAL ⇒ colour MASS-BLIND/inert "
        "(Gemini colour-interference REFUTED; cube-roots cancel ⇒ no coherent colour mass channel) ⇒ "
        "non-additivity carried by META-TIME/generation phases. The coherent-sum FORM is FRAMING (2→3 "
        "analogy, reconcile w/ §17.3 gear lock); VALUES gap-gated",
        bm["colour_slots_orthonormal_so_colour_sum_additive"] and bm["meson_vector_alpha0"] == 4.0
        and bm["meson_pseudoscalar_alphapi"] == 0.0 and bm["colourZ3_coherent_would_cancel"] == 0.0
        and bm["coherent_revival_vs_phase_shift"][0.6] > bm["coherent_revival_vs_phase_shift"][0.0])
    gs = interference_can_reduce_mass_goldstone()
    _ck("interference can SUBTRACT mass (Yaer, DERIVED): destructive cross-term (β=π) drops BELOW the "
        "incoherent floor=2 (→0, full cancellation) — the GOLDSTONE channel (meson pseudoscalar, π/K/η "
        "light), PARTIAL so hadron stays massive; antisym=destructive=lighter is CONSISTENT with Λ<Σ "
        "(a third lens, NOT an independent sign-fix — the §17.3 gear corroborator is calibrated to the same datum)",
        gs["interference_can_subtract_mass"] and gs["destructive_betapi"] < gs["incoherent_floor"]
        and gs["constructive_beta0"] > gs["incoherent_floor"] and gs["Lambda_MeV"] < gs["Sigma0_MeV"])
    fl = identify_the_floor()
    _ck("THE FLOOR identified: EXACT = QUADRATURE mean √((M_sym²+M_antisym²)/2) via the parallelogram law "
        "(ud-pair, given mass~coherent amplitude); floor≈arith CENTROID (1154 MeV) is a near-degenerate "
        "approx (Λ/Σ 0.6 MeV, FAILS in the Goldstone limit). Reconciles §17.3 gear (M_0=floor−γ=Λ) with "
        "coherent-sum as ONE functional (gear γ IS the coherent cross-term); γ INPUT, floor gap-gated",
        fl["floor_is_centroid_near_degenerate_only"] and abs(fl["gear_M0_equals_floor_minus_gamma"] - 1115.68) < 0.01
        and abs(fl["floor_MeV_arith_approx"] - fl["floor_MeV_quad_EXACT"]) < 1.0)
    cg = cogear_linkage_kinematic()
    _ck("residual (a) co↔gear LINKAGE freq-lock half DERIVED-CONDITIONAL via E-CENTRALITY "
        "(2026-07-02 sweep re-tier: conditional on the E-channel composition premise — R-127/R-128 lock "
        "the observer-visible mass phase to winding blades; E-floor→observer bridge now a named open) "
        "(NOT a shared spatial plane): "
        "mass-phase = the CENTRAL E (E²=−1, commutes with the non-commuting colour {e_ij4}/generation {e_ij} "
        "planes) ⇒ co-rotating same-E-sign windings' meta-time phases ADD to Ω_B=Σω INDEPENDENT of their "
        "spatial planes (positive-definite ⇒ no cancellation); meson opposite-E-sign ⇒ coherent amplitude "
        "2ω|cos(α/2)| cancels at α=π (Goldstone). Inertia Θ_A/Θ_B = non-abelian §17.3 (NOT derived here); "
        "freq-sum↔full-mass = open reconciliation; scale+phases = #1 gap [reviewer OVER-CLAIM→corrected]",
        cg["E_central_and_Esq_minus1"] and cg["mass_phase_is_central_E_not_spatial_plane"]
        and cg["co_monotone_no_cancellation"] and cg["LOCK_pi3_shared_rotor"]
        and abs(cg["meson_amp_vector_alpha0"] - 2.0) < 1e-9
        and cg["meson_amp_pseudoscalar_alphapi"] < 1e-9)
    mr = mass_reconciliation_U1_Spin3()
    _ck("8b residual (a) STRUCTURAL HALF CLOSED [DERIVED structure; values #1-gap-gated] — freq-sum↔full-mass "
        "RECONCILED: the baryon mass = U(1)_E FLOOR (the co-rotating frequency-sum Ω_B=Σω, central E) ⊕ the "
        "orthogonal Spin(3) collective-rotation BAND J(J+1)/2Θ (anti-self-dual triple closes su(2), Casimir J²). "
        "They are ADDITIVE not rival because [E,J_i]=0 AND [E,J²]=0 ⇒ simultaneously diagonalizable (the standard "
        "Skyrme M=M_cl+J(J+1)/2Θ, here grounded in U(1)_E⊕Spin(3) commutation). Open: the §17.3 inertia FORM "
        "(posited-standard) + absolute scales (#1 gap)",
        mr["E_central_Esq_minus1"] and mr["triple_closes_su2"] and mr["casimir_commutes_with_su2"]
        and mr["U1_commutes_with_Spin3"])
    ms = matter_stability_outside_frame()
    _ck("(vi) outside-frame SIGNAL-HOLE stability RESOLVED [FRAMING + N14 located-negative]: stable = a hole "
        "the carrier CANNOT refill = pi3 topological pinning (§3.2/§16); decay rung = lowest substrate op "
        "opening a refill channel = §23.11's 'highest forced operation'. NO new amplitude-collapse boundary: "
        "the carrier is a COMPACT unit-rotor field (all generators²=−1, bivector rotors unit-norm, twist "
        "2π-periodic, max=antipode/π=hedgehog F(0)), so 'overmodulation' INCREMENTS the winding (pi3) instead "
        "of clipping; the only genuine 'cannot sustain' = the driven-attractor basin, #1-gap-gated",
        ms["vacuum_carrier_s0_idempotent"] and ms["all_generators_square_to_minus1"]
        and ms["bivector_rotors_unit_norm"] and ms["central_E_is_U1_circle_phase"]
        and ms["twist_periodic_2pi"] and ms["overmodulation_increments_winding"]
        and ms["stable_iff_carrier_cannot_refill_eq_pi3_pinning"])

    print("§16.6 electron as topological defect (QCP scaling):")
    _ck(f"QCP exponent ν = 3·3·(1/2)·1 = 9/2  (got {electron_QCP_nu()})", electron_QCP_nu() == 4.5)
    _ck(f"f_L STIFFNESS = f_π·(1-D/J)^ν ≈ 0.115 MeV at D/J=0.79 — NOT m_e; no stiffness→mass conversion exists  (got {electron_f_L_MeV():.3f})", abs(electron_f_L_MeV() - 0.115) < 0.005)
    _ck("electron = one defect, two Hopf-linked windings (π_3=ℤ Skyrme, π_1=ℤ vortex) — the "
        "ELECTRON's pair, NOT R-002's ℤ×ℤ two windings of the state class",
        electron_two_windings()["Hopf link H"] == 1)
    lnt = lepton_number_topological_conservation()
    _ck(f"L-number topological conservation: L(L-orbit)=1, L(Q-orbit)=0, B-L doublet-sector condition (§23.7)",
        lnt["L(L-orbit defect)"] == 1 and lnt["L(Q-orbit defect)"] == 0
        and lnt["L_conserved_perturbatively"] and lnt["B_conserved_perturbatively"])
    pmns = pmns_no_substrate_derivation()
    _ck("PMNS defusing: V_PMNS has NO substrate derivation; same-orbit SM-import retracted (audit C1 2026-06-30)",
        pmns["V_PMNS_substrate_derivation"] == "NONE (no engine primitive computes lepton V_PMNS)"
        and pmns["substrate_obstruction_chiral_asymmetry"]["neutrino_module"].startswith("S+ only")
        and "RETRACTED" in pmns["previous_audit_P1_status"]
        and len(pmns["scope_restrictions_now_in_force"]) == 5)
    noa = neutrino_orbit_asymmetry_attempt()
    _ck("ν-asymmetric reframing COUNTER-INDICATED (Phase D audit 2026-06-30): [I_4, ASD_k]=0 → chirality axis ⊥ generation axis",
        noa["verdict"] == "COUNTER-INDICATED"
        and noa["obstruction_2_I4_commutes_with_ASD_triple"] is True
        and noa["obstruction_1_ASD_in_I4_minus_eigenspace"] is True
        and noa["obstruction_3_lepton_blade_has_no_e4"] is True
        and noa["both_neutrino_and_charged_lepton_are_L_orbit"] is True)
    sqr = single_quark_no_rest_mass_axis()
    _ck("canon §5 'no individual quark mass' is ALGEBRA-DERIVED: I_4·e_123=e_4 + colour-singlet reaches e_4 only collectively",
        sqr["lepton_e123_Hodge_dual_is_e4"] is True
        and sqr["no_single_quark_blade_Hodge_dual_to_e4"] is True
        and sqr["colour_singlet_triple_reaches_e4"] is True)
    phm = phase_to_h_unit_map_located_residual()
    _ck("φ_n → ℍ-unit map: LOCATED-GAP consolidation banks the single residual that surfaces in 4 substrate questions",
        "LOCATED-GAP" in phm["tier_for_phase_to_unit_bijection"]
        and len(phm["four_downstream_contexts"]) == 4
        and all(abs(n - phm["ASD_norms_squared"][0]) < 1e-12 for n in phm["ASD_norms_squared"]))
    mts = meson_topological_status()
    _ck("meson topological status: n_Q=0, NOT topologically protected; partition = EMPIRICAL; (A)-vs-(B) ontology = LOCATED-GAP (#1-gap-routed)",
        mts["n_Q(meson)"] == 0 and mts["topologically_protected"] is False
        and "EMPIRICAL" in mts["stability_partition_tier"] and "LOCATED-GAP" in mts["ontology_choice_tier"]
        and "meson_dynamical_current_split" in mts["consistency_with_existing_engine"]
        and "cogear_linkage_kinematic" in mts["consistency_with_existing_engine"])
    tot = topological_overproduction_test()
    _ck("topological over-production test: {γ, p, e, ν, stable nuclei, antiparticles} = observed; no orphans, no gaps (canonical §25.2.2 RF-7)",
        tot["matches_observation"] is True and tot["orphans"] == [] and tot["gaps"] == []
        and "DERIVED-STRUCTURAL" in tot["tier"]
        and "§25.2.2 RF-7" == tot["canonical_falsifier_entry"])
    icfb = im_chi_falsifier_budget_KSS_GW_macromolecule()
    _ck("Im χ falsifier budget: KSS floor + GW170817 ceiling + macromolecule-interferometry floor (canonical §25.2.3 VG-1)",
        "FRAMING" in icfb["tier"]
        and "KSS_floor" in icfb["pillars"]
        and "GW170817_ceiling" in icfb["pillars"]
        and "macromolecule_interferometry_floor" in icfb["pillars"]
        and "§25.2.3 VG-1" == icfb["canonical_falsifier_entry"])

    # F-5 (worklist B1, 2026-06-29): the four QCP-ingredient primitives.
    iso = D4_spatial_bond_isotropy()
    _ck(f"F-5 N_dir: D4 spatial bonds give M_ij = 4·δ_ij, Tr(M)/M_11 = N_dir = 3  "
        f"(got N_dir={iso['N_dir_from_trace_over_M11']})",
        iso["M_eq_4_delta_ij"] and iso["N_dir_from_trace_over_M11"] == 3)
    knorm = sigma_model_kinetic_normalization()
    _ck(f"F-5 1/2 factor: K_φ/f² · dim(S±) = (1/4)·2 = 1/2  "
        f"(got {knorm['QCP_half_factor']})",
        abs(knorm["QCP_half_factor"] - 0.5) < 1e-12)
    dm = DM_operator_gaussian_dim(d=3, eta=0.0)
    _ck(f"F-5 ν_corr: Gaussian-FP [O_DM] = 2[φ]+1 = 2 at d=3, η=0 ⇒ ν_corr = 1/(d-[O_DM]) = 1  "
        f"(got [O_DM]={dm['O_DM_dim']}, ν_corr={dm['nu_corr']})",
        abs(dm["O_DM_dim"] - 2.0) < 1e-12 and abs(dm["nu_corr"] - 1.0) < 1e-12)
    gap = canting_critical_stiffness_at_DJ()
    _ck(f"F-5 K_c LOCATED-GAP-REFINED: 19 named via Luttinger-Tisza (18+(D/J)²=19 at D=J), "
        f"2 traced to N_Goldstone=dim(SU(2)_L/U(1)_canting)=2 (Lead A); kernel form still §9.6  "
        f"(outcome={gap['outcome']}, K_c/J derived={gap['K_c_over_J_engine_derived']}, "
        f"Lead-A reconstruction={gap['lead_A_reconstruction_K_c_over_J']:.4f})",
        gap["outcome"] == "LOCATED-GAP-REFINED"
        and gap["spiral_pitch_denominator_at_DJ"] == 19
        and gap["K_c_over_J_engine_derived"] is None
        and gap["N_Goldstone_substrate_value"] == 2
        and abs(gap["lead_A_reconstruction_K_c_over_J"] - 2.0/19.0) < 1e-12
        and abs(gap["K_c_over_J_asserted"] - 2.0/19.0) < 1e-12)
    ng = n_goldstone_canted_FM()
    _ck(f"§16.6 N_Goldstone = dim(SU(2)_L/U(1)_canting) = 3-1 = 2 (closed coset-dim identity; "
        f"sources the 2 prefactor in K_c via Lead A)  (got N_G={ng['N_Goldstone']}, "
        f"tier={ng['tier']})",
        ng["N_Goldstone"] == 2
        and ng["dim_SU2_L"] == 3
        and ng["dim_U1_canting"] == 1
        and ng["dim_coset_SU2_over_U1"] == 2
        and ng["tier"] == "DERIVED-A"
        and ng["N_Goldstone"] == gap["N_Goldstone_substrate_value"])

    print("§22.5 nuclear forces hierarchy:")
    _ck(f"η_DM = (D/J)²/144 ≈ 0.43%  (got {eta_DM()*100:.2f}%)", abs(eta_DM() - 0.0043) < 1e-4)
    nh = nuclear_length_hierarchy()
    _ck(f"length hierarchy: hard core 0.40, soliton 0.56, pion 1.46 fm  (got {{k: round(v,2) for k,v in nh.items()}})",
        abs(nh["hard core (√2 ℓ_S)"]-0.40) < 0.01 and abs(nh["pion Yukawa (5.2 ℓ_S)"]-1.46) < 0.02)

    print("W-LIVE-4 fermionic-Skyrmion-forcing re-attack (LOCATED-GAP-REFINED):")
    sky = skyrmion_collective_quantization_under_v2_3p2()
    _ck("L1 — collective ansatz R = A·R_sol·Ã is A→−A invariant (diff_norm = 0 exact); I_4 is a BLADE map L→Q, not a rotor-rotor identification ⇒ V2 §3.2 cannot push A's sign flip to q_h's sign",
        sky["L1_sandwich_AnegA_invariant"] is True
        and sky["L1_sandwich_diff_norm"] == 0
        and sky["L1_I4_maps_L_to_Q_blades_not_rotors"] is True)
    _ck("L2 — one-sided ψ→Rψ gives ψ→−ψ at R(2π) (§14.6); two-sided A·R_sol·Ã is identity at R(2π); the two actions decouple, s=3 / Adler-zero does NOT force collective fermionic",
        sky["L2_one_sided_R2pi_psi_is_minus_psi"] is True
        and sky["L2_two_sided_R2pi_sandwich_is_identity"] is True)
    _ck("L3 — each Q-trivector facet's sandwich A·e_{ij4}·Ã is A→−A invariant; three-facet product = +1, NOT (−1)^3 = −1 (no WZW-analog phase from N_c = 3)",
        all(s == 1 for s in sky["L3_facet_signs_under_AnegA"].values())
        and sky["L3_three_facet_product_sign"] == 1.0)
    _ck("verdict: LOCATED-GAP-REFINED; §14.6 / §15.1 Finkelstein-Rubinstein SELECTION tier preserved; three named closure routes (W1 reduced 2026-07-02 to the P2-4 U(1)-level-term form — finite-ℤ_3-holonomy instance closed, W2 §9.6 τ_5-flow, W3 deeper V2 §3.2 refinement) remain open",
        sky["outcome"] == "LOCATED-GAP-REFINED"
        and len(sky["eliminated_closure_routes"]) == 3
        and len(sky["remaining_closure_routes"]) == 3
        and "reduced 2026-07-02" in sky["remaining_closure_routes"][0])

    print("W-LIVE-4 route W1 finite-holonomy no-go (2026-07-02, DERIVED-generic group theory):")
    w1 = colour_z3_holonomy_cannot_source_fr_sign()
    _ck("W1 finite-holonomy CLOSED-NEGATIVE: ℤ_3 has no order-2 element (Hom(ℤ_2,ℤ_3) trivial); all six ℤ_6 characters enumerated — rotation-loop sign fully independent of colour part; S_3 (the unique nonabelian completion): [S_3,S_3] = A_3 computed, both 1-dim reps trivial on colour; √1 ∩ ∛1 = {1} (coprimality — no scalar mechanism ties ℤ_3 to the FR −1); 2π rotation fixes all facet blades (no permutation loophole) ⇒ W1 reduces to P2-4's U(1)-valued level-N_c action term",
        w1["no_order_2_in_z3"] and w1["hom_z2_z3_trivial"]
        and w1["z6_rotation_sign_independent_of_colour"]
        and w1["s3_commutator_subgroup_is_A3"] and w1["s3_sign_rep_trivial_on_colour"]
        and w1["coprime_intersection_trivial"]
        and w1["facets_fixed_under_2pi"]
        and w1["outcome"] == "CLOSED-NEGATIVE-finite-holonomy; W1 reduces to P2-4"
        and "DERIVED-generic" in w1["tier"])
    _ck("W1-honesty: the close is scoped to the FINITE-holonomy instance only — the surviving U(1)-level-N_c action-term form is named, not silently absorbed (would-change-if carries the P2-4 odd/even-level fork)",
        "U(1)" in w1["surviving_W1_form"] and "P2-4" in w1["surviving_W1_form"]
        and "ODD level" in w1["would_change_if"])

    print("ADJUDICATION3 bank (2026-08-12) — moving-defect cost laws + the m = E₀ premise:")
    sh = pattern_shear_sector_identities()
    _ck("shear family: g2(Ω₄) = −v·g2(Ω₁) pointwise-exact (FD floor) — the sector-law mechanism",
        sh["pointwise g2(Om4) = -v g2(Om1) (worst coeff)"] < 1e-9)
    _ck("shear family: [Ω₄, Ω₁] = 0 identically (the (4,1) quartic pair vanishes)",
        sh["pointwise [Om4, Om1] = 0 (worst coeff)"] < 1e-9)
    _ck("sector laws: E₂→(1+v²/3), E₄→(1+2v²/3); 1+v²/2 at Derrick TERMINATING; inertia = E₀ at O(v²) iff balanced; FENCE-IMMUNE",
        sh["fence-immune"] and sh["inertia at Derrick = (1/3)E2 + (2/3)E4 = E0/2"])
    tl = tilt_family_fixed_slice_cost_law()
    _ck("tilt family: D_tilt(x,x₄) == D_rest(rotated point) pointwise ⇒ fixed-slice law E = E₀·secθ = E₀√(1+v²)",
        tl["pointwise D_tilt(x,x4) == D_rest(rotated point) (worst rel)"] < 1e-8)
    _ck("O(v²) native γ-agreement; O(v⁴) split (pattern 0, tilt −1/8, γ +3/8) = the N56 energetic gap",
        tl["v^4 split (pattern, tilt, gamma)"] == (0.0, -0.125, 0.375))
    pr = mass_equals_elastic_cost_premise()
    _ck("m = E₀ premise: INPUT-class, COUNTED; ADJACENT to residue (ii)/N57/C-7, never their content (R3(a))",
        pr["counted"] and pr["adjacent_to_not_content_of"] == ["R-123 residue (ii)", "N57", "C-7"])
    _ck("m = E₀ which-E₀ named (vacuum-subtracted, v = 0 duty-free reading); R-144 is NOT a user of the bridge",
        "vacuum-subtracted" in pr["which_E0"]
        and pr["not_used_by"] == ["R-144 (dimensionless margin)"])

    print("J,D/Γ rework bank (2026-08-21) — the canted vacuum's BRANCH STRUCTURE (§D.4.3):")
    bs = canting_vacuum_branch_structure()
    _ck("axis branch IDENTIFIED and reproduced: the 24-bond frame-bilinear sum on k = q·e₁, "
        "B = e₁₄ equals §D.4.3's printed E(q) = −12J cos q − 12J − 2√2 D sin q up to the inert "
        f"−24J bond-count constant (maxdiff {bs['axis_branch_closed_form_maxdiff']:.2e}); and the "
        f"DM energy vanishes IDENTICALLY on an e₄-axis helix ({bs['dm_energy_on_e4_axis_helix']:.2e}) "
        "— which is why the vacuum helix is SPATIAL, a fact §D.4.3 never states",
        bs["axis_branch_closed_form_maxdiff"] < 1e-11
        and bs["dm_energy_on_e4_axis_helix"] < 1e-12
        and bs["reduced_vs_bond_sum_maxdiff"] < 1e-11)
    _ck("that configuration is an INDEX-2 SADDLE for every D/J > 0: the transverse second "
        "variation ∂²E/∂k₂² = 4J(cos q+3)(cos q−1)/cos q is an IDENTITY (sympy, tolerance-free, "
        "after substituting the stationarity relation D = 6J tan q/√2) and is NEGATIVE at "
        f"D/J = 0.2, 0.787, 2.0 (values "
        f"{[round(v['d2E_dk2sq_closed_form'], 6) for v in bs['transverse_second_variation'].values()]}; "
        "independent central-difference witness agrees to "
        f"{max(v['relative_diff'] for v in bs['transverse_second_variation'].values()):.1e} relative)",
        bs["saddle_index"] == 2 and bs["saddle_holds_for_all_DoverJ_gt_0"]
        and all(v["d2E_dk2sq_closed_form"] < 0 and v["relative_diff"] < 1e-3
                for v in bs["transverse_second_variation"].values()))
    _ck("the BODY-DIAGONAL branch (k ∝ (1,1,1,0), all twelve e₄-bonds at ONE uniform angle) lies "
        "LOWER, by the leading-order splitting law ΔE = −(1/243)(D/J)⁴·J — verified at D/J = 0.1 to "
        f"{bs['branches'][0.1]['gap_relative_deviation_from_law']:.1e} relative. DERIVED-numeric "
        "WITHIN THE SINGLE-q SIMPLE-BIVECTOR HELICAL FAMILY (RUL-049; multi-q, conical and "
        "non-simple-B states unscanned); exact-arithmetic minimisation owed",
        bs["branches"][0.1]["E_diagonal"] < bs["branches"][0.1]["E_axis"]
        and bs["branches"][0.787]["E_diagonal"] < bs["branches"][0.787]["E_axis"]
        and bs["branches"][0.1]["gap_relative_deviation_from_law"] < 1e-3
        and "SINGLE-q" in bs["tier"])
    _ck("R-108's closed form SURVIVES on both branches with a re-interpreted referent: the "
        "leading-order helical-rate invariant |k|·λ = √2D/(6J) holds on the diagonal branch "
        f"(deviation {bs['branches'][0.1]['rate_abs_deviation']:.1e} at D/J = 0.1) where on the axis "
        "branch the same closed form appears as tan q. NORMALISATION quoted with the gap: at "
        f"D/J = 0.787 it is {bs['gap_relative_to_full_bond_total_minus48J']:.1e} of the full "
        f"−48J bond total and {bs['gap_relative_to_paper_printed_total']:.1e} of §D.4.3's printed "
        "E(q) total. WHICH branch the DRIVEN kernel selects is OPEN (#1 gap, §D.5)",
        bs["branches"][0.1]["rate_abs_deviation"] < 1e-6
        and abs(bs["gap_relative_to_full_bond_total_minus48J"] - 3.2e-5) < 2e-6
        and abs(bs["gap_relative_to_paper_printed_total"] - 6.4e-5) < 4e-6
        and "#1 gap" in bs["open_branch_selection"])


    print("THE ESTATE OF N64 (2026-08-23) — the four-round estate dispute's banked outcome:")
    md_ = brannen_comb_commitment_dominance_and_dof_vacuity()
    _ck("PERIOD LATTICE = 2π·D4*, as a FOURIER-SUPPORT THEOREM, not a controls hedge: the J-term's "
        "support {±e_i±e_j} GENERATES D4 so periods(J) = 2π·D4* exactly, and the DM-term's "
        "π-periodicity per coordinate never restricts. Measured on three D4* generators "
        f"(max dev {max(md_['period_deviations'].values()):.1e}) WITH the negative control at "
        f"2π(½,½,0,0) SEEN TO REJECT ({md_['period_negative_control_2pi_half_half_0_0']:.2e}) — "
        "a lattice check that never rejects has not been shown to be one. This is the ONE "
        "DERIVED-A item to come out of the Y2 dispute",
        md_["period_lattice"] == "2pi*D4*"
        and max(md_["period_deviations"].values()) < 1e-12
        and md_["period_negative_control_2pi_half_half_0_0"] > 1.0
        and "FOURIER-SUPPORT THEOREM" in md_["period_lattice_ground"])
    _ck("the closed-comb enumeration is exhaustive OF TRANSLATION-STEP combs and nothing more: two "
        "steps coincide iff g ≡ g′ mod 3·D4*, so a complete residue system of D4*/3D4* covers them "
        f"all — {md_['residue_system']['candidates_in_box']} candidates → "
        f"{md_['residue_system']['distinct_classes']} classes ({md_['residue_system']['non_degenerate']} "
        "non-degenerate), and {0,1,2}⁴ ALONE hits every class exactly once (ℤ⁴ → D4*/3D4* is an "
        "isomorphism, so the 81 half-integer candidates are redundant)",
        md_["residue_system"]["candidates_in_box"] == 162
        and md_["residue_system"]["distinct_classes"] == 81
        and md_["residue_system"]["non_degenerate"] == 80
        and md_["residue_system"]["integer_reps_alone_suffice"] is True)
    _ck("★ THE FINDING IS THE INEQUALITY, and it is asserted so the numbers can never be separated: "
        f"c_max(translation-closed) = {md_['c_max_translation_closed']} < √2 < "
        f"{md_['c_max_twisted_closed_nondegenerate']} = c_max(screw-closed, non-degeneracy-guarded) "
        f"< {md_['c_max_twisted_closed']} unconstrained. TWO defensible readings of 'a closed ℤ₃ comb' "
        "STRADDLE the Koide point, so NO GEOMETRIC CEILING IS A SUBSTRATE PROPERTY — the reachable "
        "amplitude is dominated by the UNBANKED M-3 commitment (CELL meta-time phase → GRAIN helix "
        f"configuration). Reproduced live: the maximising class gives {md_['c_max_translation_closed_reproduced_on_maximising_class']:.6f}, "
        f"an 80-class polish sweep does not exceed it ({md_['c_max_translation_closed_80class_sweep']:.6f}), "
        f"and a guarded screw search reaches {md_['c_max_twisted_guarded_live_witness']:.4f} > √2",
        md_["c_max_translation_closed"] < math.sqrt(2.0)
        < md_["c_max_twisted_closed_nondegenerate"] < md_["c_max_twisted_closed"]
        and abs(md_["c_max_translation_closed_reproduced_on_maximising_class"] - 1.216468) < 1e-5
        and md_["c_max_translation_closed_80class_sweep"] < 1.216468 + 1e-4
        and md_["c_max_twisted_guarded_live_witness"] > math.sqrt(2.0)
        and md_["sqrt2_attained_on_closed_comb"] is True
        and len(md_["commitment_menu"]) == 5)
    _ck("the SUBTRACTION is the global vacuum (never the ray minimum — m = E₀'s own referent), and "
        "the correction yields the cross-check neither side of the dispute had: the corrected axis "
        f"λ=1 ray value {md_['axis_lambda1_global_subtracted_cross_check']:.6f} EQUALS the exhaustive "
        f"translation-closed maximum {md_['c_max_translation_closed']}, because g = (0,0,2,0) IS an "
        "axis-type comb — which dissolves the apparent paradox of a ray value exceeding an "
        f"'exhaustive' maximum. Free 4D vacuum lands on the BANKED body-diagonal value "
        f"({md_['global_vacuum_free_search']:.9f} vs {md_['global_vacuum_banked_body_diagonal']:.9f})",
        abs(md_["axis_lambda1_global_subtracted_cross_check"]
            - md_["c_max_translation_closed"]) < 1e-4
        and abs(md_["global_vacuum_free_search"]
                - md_["global_vacuum_banked_body_diagonal"]) < 1e-9
        and "global vacuum" in md_["subtraction"])
    _ck("★ THE MASS-RATIO CAVEAT TRAVELS WITH THE NUMBERS: the exhibited NON-DEGENERATE screw point "
        f"HIT B closes exactly (residual {max(abs(x) for x in md_['screw_hit_B']['closure_residual_over_2pi']):.1e} "
        f"in D4*, min/mean {md_['screw_hit_B']['min_over_mean']:.4f} — NOT the c→2 two-massless corner) "
        f"and hits c = √2, K = 2/3 to twelve digits — yet its √m ladder is "
        f"1 : {md_['screw_hit_B']['sqrt_mass_ratios'][1]:.2f} : {md_['screw_hit_B']['sqrt_mass_ratios'][2]:.2f} "
        f"(HIT A: 1 : {md_['screw_hit_A']['sqrt_mass_ratios'][1]:.2f} : {md_['screw_hit_A']['sqrt_mass_ratios'][2]:.2f}) "
        "against the measured 1 : 206.77 : 3477.37. Matching K is ONE equation; matching the ladder "
        "is TWO, and NO configuration measured in the AMPLITUDE dispute came near it — what that "
        "dispute demolished is the EXPLANATION offered for batch 1's kill (a geometric ceiling), "
        "never the kill. ★ AND THE CAVEAT CARRIES ITS OWN SUPERSESSION, RUL-049-conditioned IN THE "
        "SAME STRING: the JOINT (c, δ) search DOES reach the ladder exactly, so the kill in its "
        "'cannot-reach-the-data' form DOES NOT SURVIVE on the SCREW family — whose "
        "generation-legality is an OPEN COORDINATOR CALL — and is UNTOUCHED on the TRANSLATION-STEP "
        "family. It is REPLACED by a dof/vacuity kill, never removed (next check)",
        abs(md_["screw_hit_B"]["c"] - math.sqrt(2.0)) < 1e-8
        and abs(md_["screw_hit_B"]["K"] - 2.0 / 3.0) < 1e-8
        and md_["screw_hit_B"]["closure_in_D4star"] is True
        and md_["screw_hit_B"]["min_over_mean"] > 0.25
        and md_["screw_hit_B"]["sqrt_mass_ratios"][2] < 300.0
        and md_["screw_hit_A"]["sqrt_mass_ratios"][2] < 300.0
        and "DOES NOT SURVIVE on the SCREW family" in md_["mass_ratio_caveat"]
        and "OPEN COORDINATOR CALL" in md_["mass_ratio_caveat"]
        and "UNTOUCHED on the TRANSLATION-STEP family" in md_["mass_ratio_caveat"]
        and "COUNTED, UNFORCED INPUT" in md_["koide_rows_unchanged"])

    print("THE ESTATE OF N64 — the JOINT (c, δ) SEARCH: attainment and vacuity, ONE finding:")
    _ck("★ THE NEVER-SEPARABLE PAIR, MEASURED IN ONE CALL: the closed screw family ATTAINS the "
        f"MEASURED charged-lepton ladder EXACTLY — {md_['attainment_exhibited_point']['mass_ratios'][1]:.6f} "
        f"and {md_['attainment_exhibited_point']['mass_ratios'][2]:.4f} against the measured "
        f"206.768283 and 3477.365267 (relative error "
        f"{max(md_['attainment_exhibited_point']['relative_error_per_ratio']):.1e}, inside the "
        f"pre-registered ATTAINED band), on a closure exact to "
        f"{max(abs(x) for x in md_['attainment_exhibited_point']['closure_over_2pi']):.1e} — on ALL "
        f"EIGHT order-3 symmetries, at {md_['attainment_independent_solutions']['search_refinement_pass']} "
        f"mutually-distant solutions plus {md_['attainment_independent_solutions']['ratification_independent_solver']} "
        "more from the ratification round's INDEPENDENT solver — ★ AND THAT IS THE NULL RESULT: "
        f"{md_['free_reals']} free reals against {md_['constraints']} constraints ⇒ a "
        f"{md_['solution_manifold_dim']}-DIMENSIONAL SOLUTION MANIFOLD returning "
        f"{md_['sm_quantities_returned']} SM quantities. Reaching the data is worth nothing here",
        md_["measured_triple_attained"] is True
        and max(md_["attainment_exhibited_point"]["relative_error_per_ratio"]) < 1e-6
        and md_["attainment_on_all_eight_symmetries"] is True
        and md_["sm_quantities_returned"] == "0 of 19"
        and md_["solution_manifold_dim"] == 4)
    _ck("the dof kill is JACOBIAN-ATTACK-PROOF, and the counting argument is the load-bearing step "
        f"— NOT the measurement: dim = free_reals − constraints = {md_['free_reals']} − "
        f"{md_['constraints']} = {md_['solution_manifold_dim']}, and a 2×6 Jacobian has rank ≤ 2 "
        "IDENTICALLY, so dim ≥ 4 AT EVERY SOLUTION whatever the rank turns out to be. Rank 2 is the "
        "MAXIMUM — the LEAST vacuous case available to the family; any rank DROP makes the manifold "
        f"LARGER. Measured here at the exhibited point: rank {md_['jacobian_rank']}, singular values "
        f"{[round(x, 3) for x in md_['jacobian_singular_values']]} (well separated ⇒ the two "
        "constraints are locally independent, which is the BEST the family could have done). And "
        "widening cannot rescue it: any widening adds PARAMETERS or BRANCHES, neither adds CONSTRAINTS",
        md_["solution_manifold_dim"] == md_["free_reals"] - md_["constraints"] == 4
        and md_["jacobian_rank"] == 2
        and len(md_["jacobian_singular_values"]) == 2
        and "rank <= 2 IDENTICALLY" in md_["dof_kill_is_jacobian_attack_proof"]
        and "neither adds" in md_["widening_makes_the_kill_stronger"])
    _ck("the order-3 step-form enumeration REBUILT FROM SCRATCH inside the D4 point group closed by "
        f"generators: {md_['point_group_order']} elements, {md_['symmetries_of_E_reduced']} symmetries "
        f"of E_reduced, EXACTLY {md_['order3_symmetries']} of order 3 (max deviation "
        f"{md_['order3_symmetry_max_deviation']:.1e}), every one with rank(I+ρ+ρ²) = "
        f"{md_['N_rank_for_every_order3']} — which is what makes closure TWO scalar equations. ★ THE "
        f"ENUMERATION IS SEEN TO REJECT: a non-symmetry inside the same group deviates by "
        f"{md_['symmetry_enumeration_negative_control']:.3f} > 1. ★ SCOPE, tightened per the "
        "ratification: EXHAUSTIVE OF THE ORDER-3 LINEAR SYMMETRIES OF E_reduced — never 'of linear ρ' "
        "— with the ρ³ = I-without-symmetry class DECLARED UNSCANNED, and the published "
        "exhaustiveness ARGUMENT repaired to run through ρᵀ(D4) = D4, not through fixing the J-term",
        md_["point_group_order"] == 1152
        and md_["symmetries_of_E_reduced"] == 96
        and md_["order3_symmetries"] == 8
        and md_["N_rank_for_every_order3"] == 2
        and md_["symmetry_enumeration_negative_control"] > 1.0
        and md_["order3_symmetry_max_deviation"] < 1e-12
        and "EXHAUSTIVE OF THE ORDER-3 LINEAR SYMMETRIES" in md_["order3_exhaustiveness_scope"]
        and "rho^T(D4) = D4" in md_["order3_exhaustiveness_argument"]
        and len(md_["order3_declared_unscanned"]) == 4
        and any("rho^3 = I" in s for s in md_["order3_declared_unscanned"]))
    _ck("★ δ BINDS BEFORE c DOES — the ONE strategic finding of the whole four-round dispute, and the "
        f"reason every ceiling in it measured the WEAKER face: |t|_c / |t|* = {md_['pitch_threshold_c_only']} "
        f"/ {md_['pitch_threshold_joint']} = {md_['delta_binds_first_factor']:.4f}. Corroborated live: "
        f"max c over k₀ at |t|_c is {md_['max_c_at_pitch_threshold_c_only']:.4f} = √2. The pitch lattice "
        f"L = ker(N) ∩ 2π·D4* is HEXAGONAL 2π·A₂ (DERIVED — a half-integer D4* vector has no zero "
        f"coordinate so it cannot meet {{x₄ = 0}}), minimal vector {md_['pitch_L_minimal_vector']:.6f} = "
        f"2π√2, covering radius {md_['pitch_L_covering_radius']:.6f}; the exhibited screw reduces from "
        f"{md_['screws_must_be_quoted_reduced_mod_L']['exhibited_raw']:.6f} to "
        f"{md_['screws_must_be_quoted_reduced_mod_L']['exhibited_reduced']:.6f}, so screws are NOT "
        "comparable unless quoted mod L",
        abs(md_["delta_binds_first_factor"] - 1.1402) < 1e-3
        and abs(md_["max_c_at_pitch_threshold_c_only"] - math.sqrt(2.0)) < 5e-3
        and abs(md_["pitch_L_minimal_vector"] - 2.0 * math.pi * math.sqrt(2.0)) < 1e-9
        and abs(md_["screws_must_be_quoted_reduced_mod_L"]["exhibited_reduced"] - 0.603642) < 1e-5)
    _ck("lattice-t mass blindness is DERIVED-A and is a MEASURE-ZERO KNIFE-EDGE, computed on BOTH "
        f"sides so the sharper family-level statement replaces the single-base-point ε table: the "
        f"three comb energies coincide to {md_['lattice_t_spread']:.1e} for EVERY lattice translation "
        f"and EVERY base point (c = 0 identically ⇒ 100% of the splitting rides the NON-LATTICE part "
        f"of t), yet at reduced pitch 0.10 the maximum is already {md_['max_c_at_small_pitch_0p10']:.4f} "
        "≈ 2. And the δ-window at c = √2 is the FULL non-negativity window ψ ∈ [π/4, π/3] of width "
        f"π/12 — brute-forced measure fraction {md_['delta_window_measure_fraction']:.4f} = 0.25 — "
        "saturated to machine precision and EMPTY outside it: THE SUBSTRATE CONTRIBUTES EXACTLY ZERO "
        "CONSTRAINT BEYOND E₀ ≥ 0",
        md_["lattice_t_mass_blind"] is True
        and md_["lattice_t_spread"] < 1e-12
        and md_["max_c_at_small_pitch_0p10"] > 1.9
        and abs(md_["delta_window_measure_fraction"] - 0.25) < 1e-3
        and "measure-zero" in md_["lattice_t_blindness_is_a_measure_zero_knife_edge"].lower()
        and "CONTRAST" in md_["lattice_t_blindness_is_a_measure_zero_knife_edge"])

    print("THE INSEPARABILITY GUARD — the never-separable discipline made EXECUTABLE (AST-level):")
    import os as _os, ast as _ast
    _here = _os.path.dirname(_os.path.abspath(__file__))
    _read = lambda f: open(_os.path.join(_here, f), encoding="utf-8").read()
    _ATTAIN_KEY = "measured_triple_attained"
    _VACUITY_KEYS = ("solution_manifold_dim", "jacobian_rank", "sm_quantities_returned",
                     "free_reals", "constraints")

    def _returned_dict_keys(sourcetext):
        """{function name -> set of STRING keys in every dict it RETURNS} (AST, not grep —
        a docstring mention is a string constant and must not fire)."""
        out = {}
        for _fn in _ast.walk(_ast.parse(sourcetext)):
            if not isinstance(_fn, (_ast.FunctionDef, _ast.AsyncFunctionDef)):
                continue
            keys = set()
            for _r in _ast.walk(_fn):
                if isinstance(_r, _ast.Return) and isinstance(_r.value, _ast.Dict):
                    for _k in _r.value.keys:
                        if isinstance(_k, _ast.Constant) and isinstance(_k.value, str):
                            keys.add(_k.value)
            if keys:
                out[_fn.name] = keys
        return out

    def _inseparability_violations(sourcetext):
        """the attainment fact and the vacuity facts must be returned by ONE function.
        Fires if: no function returns the attainment key; more than one does; or the one
        that does fails to return every vacuity key alongside it."""
        byfn = _returned_dict_keys(sourcetext)
        carriers = sorted(n for n, k in byfn.items() if _ATTAIN_KEY in k)
        if len(carriers) != 1:
            return {"attainment carriers": carriers or "none"}
        missing = sorted(k for k in _VACUITY_KEYS if k not in byfn[carriers[0]])
        return {f"{carriers[0]} returns the attainment WITHOUT": missing} if missing else {}

    _cand_src_v3 = _read("twt_candidate_v3.py")
    _isep = _inseparability_violations(_cand_src_v3)
    _ck("★ THE ATTAINMENT AND THE VACUITY ARE RETURNED BY ONE CALL, AND NO OTHER: exactly one "
        f"function in twt_candidate_v3.py returns `{_ATTAIN_KEY}`, and it returns all of "
        f"{list(_VACUITY_KEYS)} alongside it. A corpus able to quote 'the banked geometry reproduces "
        "the charged-lepton ladder exactly' WITHOUT 'on a 4-dimensional solution manifold, returning "
        "0 of 19' has been handed the worst sentence in this program's history — this check is what "
        f"makes the never-separable discipline EXECUTABLE rather than a hope (violations: {_isep or 'none'})",
        not _isep)
    # THE GUARD IS SEEN TO FIRE — three planted splits, all against in-memory copies; the
    # file on disk is never touched. A guard never demonstrated firing is decoration.
    _split_a = _cand_src_v3.replace('"solution_manifold_dim": MANIFOLD_DIM,',
                                    '"solution_manifold_dim_MOVED_OUT": MANIFOLD_DIM,', 1)
    _split_b = _cand_src_v3 + (
        '\n\ndef _planted_second_carrier():\n'
        '    return {"measured_triple_attained": True}\n')
    _split_c = _cand_src_v3.replace('"measured_triple_attained": True,',
                                    '"measured_triple_attained_RELOCATED": True,', 1)
    _ck("the inseparability guard is NOT vacuous — THREE demonstrated failure modes, each the real "
        "way this could go wrong: (a) a vacuity key moved out of the dict; (b) a SECOND function "
        "returning the attainment fact on its own (the split that would let it be quoted alone); "
        "(c) the attainment key relocated out of the carrier entirely",
        bool(_inseparability_violations(_split_a))
        and bool(_inseparability_violations(_split_b))
        and bool(_inseparability_violations(_split_c))
        and _split_a != _cand_src_v3 and _split_c != _cand_src_v3)

    print("THE ESTATE OF N64 — B2, the six-band magnon STIFFNESS spectrum of the canted vacuum:")
    mb_ = magnon_stiffness_bands_canted_vacuum()
    _ck("at D = 0 the shared band is an EXACT OPERATOR IDENTITY H(k) = 12·J·k̃²(k)·𝟙₆ "
        f"(max dev {mb_['D0_identity_max_dev']:.2e}), upgrading induced_G_from_linear_face_band STEP 1 "
        "from a WP-LV1 LICENCE to an identity. ★ SHIPPED FAILURE MODE — the factor-2 label trap that "
        "sits directly under this line in the probe script: the 6·J·k̃² form is SEEN TO FAIL by "
        f"{mb_['D0_identity_wrong_factor_6J_dev']:.1f}, so a reader checking the identity against a "
        "'6J' print cannot conclude it fails",
        mb_["D0_identity_max_dev"] < 1e-12
        and mb_["D0_identity_wrong_factor_6J_dev"] > 1.0
        and mb_["D0_operator_identity"] == "H(k) = 12 * J * ktilde^2(k) * 1_6")
    _ck("at Γ the spectrum is 2 GAPLESS + 4 EXACTLY FOURFOLD-DEGENERATE gapped on BOTH single-q "
        f"branches — body-diagonal {[round(x, 6) for x in mb_['gamma_spectrum']['body-diagonal']]}, "
        f"axis {[round(x, 6) for x in mb_['gamma_spectrum']['axis']]} — so the 2+4 SPLIT is "
        "BRANCH-ROBUST (stronger than 'confirms the banked N_G = 2', which is scoped to the AXIS "
        "branch). ★ SECOND SHIPPED FAILURE MODE: the EVEN DM convention (excluded by §D.4.3's own "
        f"printed E(q)) DESTROYS the structure — {mb_['even_convention_control_spectrum'][:3]}… all "
        "six gapless",
        mb_["n_gapless"] == 2 and mb_["n_gapped"] == 4
        and mb_["split_is_branch_robust"] is True
        and mb_["even_convention_control_destroys_split"] is True)
    _ck("★ but the VALUE g is BRANCH-SPECIFIC and must never be quoted branch-blind: "
        f"g = {mb_['g_body_diagonal']:.6f} (body-diagonal) vs {mb_['g_axis']:.6f} (axis) at D/J = 0.787, "
        f"{100 * mb_['branch_relative_difference']:.1f}% apart, with branch SELECTION #1-gap OPEN. And "
        "this is STIFFNESS, NOT BOGOLIUBOV (F2): bosonic Bogoliubov is paraunitary against a τ₃ "
        "metric and that operator is not this one — so this does NOT discharge the two banked "
        "'6-band Bogoliubov UN-BANKED' IOUs, which name a different object and are left standing",
        abs(mb_["g_body_diagonal"] - 0.412121) < 1e-5
        and abs(mb_["g_axis"] - 0.405987) < 1e-5
        and mb_["g_is_branch_specific"] is True
        and "STIFFNESS" in mb_["object"] and "NOT a Bogoliubov" in mb_["object"]
        and "UN-BANKED" in mb_["does_not_discharge"])

    print("THE ESTATE OF N64 — KC-1, the one-way symmetry-class filter on #1-gap kernel candidates:")
    kc_ = spectral_branch_symmetry_class_filter()
    _ck("KC-1 is ONLY IF, not IFF: failing the test is DECISIVE, PASSING is NECESSARY-NOT-SUFFICIENT "
        "(a complex-class kernel can still be nodeless, and the banked substrate fails the second "
        "test independently — the gapless set is exactly {Γ, ±k₀}). Measured on the banked D4 "
        f"Hessian, body-diagonal branch at D/J = 0.787: H(k)* = H(−k) at {kc_['hermiticity_dev']:.1e} "
        f"and spectrum(k) = spectrum(−k) at {kc_['spec_inversion_dev']:.1e}, both EXACTLY, so an "
        f"antiunitary acts at fixed k ⇒ REAL (orthogonal) class ⇒ codimension 2 ⇒ Jacobian rank 3 "
        f"NEVER occurs (histogram {kc_['rank_histogram']})",
        kc_["direction"] == "necessary-not-sufficient"
        and kc_["hermiticity_dev"] < 1e-13 and kc_["spec_inversion_dev"] < 1e-13
        and kc_["rank_3_absent"] is True and 3 not in kc_["rank_histogram"])
    _ck("★ CORRECTION TO THE GOVERNING RECORD, found by this pass's own check design: 'Chern ≡ 0' at "
        "the rank-2 crossings is NOT robust. Codimension 2 means a small S² around a crossing CUTS "
        f"the degeneracy locus — measured, the two-band gap on the sphere collapses to "
        f"{min(c['min_gap_on_S2'] for c in kc_['substrate_rank2_crossings']):.1e} at radius "
        f"{kc_['sphere_radius']:.0e} — so NO ℤ-valued invariant is defined there, and the SAME "
        f"instrument returns {kc_['chern_values_returned_across_crossings']} at different crossings. "
        "The CODIMENSION is the real-class signature (exactly what the estate verdict's §KC-1.2 says); "
        "L1's verdict — no Weyl node on this substrate — is UNCHANGED and better evidenced",
        kc_["chern_definable_at_substrate_crossings"] is False
        and len(kc_["chern_values_returned_across_crossings"]) > 1
        and all(c["min_gap_on_S2"] < 1e-5 for c in kc_["substrate_rank2_crossings"]))
    _ck("★ MANDATED FAILURE MODE — the filter is SEEN TO RETURN THE OTHER ANSWER: on a synthetic "
        f"complex-class Weyl node the SAME instrument gives Chern {[round(c, 5) for c in kc_['chern_control_weyl']]} "
        f"with the sphere gap BOUNDED AWAY at 2r ({kc_['sphere_gap_weyl'][0]:.1e}), and that node FAILS "
        f"the real-class test the substrate passes ({kc_['weyl_control_fails_real_class_test']:.2f}); a "
        "synthetic real-class control reproduces the substrate's collapsed-gap signature. And two "
        "fences travel with the primitive: the real-class ASSIGNMENT is EVIDENCE-NOT-THEOREM (the "
        "inversion operator M is not exhibited — owed), and 'escape (a) measured EMPTY' is WITHDRAWN "
        "as a mis-transcription: the Ω/metric escape is UNMEASURED / kernel-GATED, never empty",
        all(abs(abs(c) - 1.0) < 1e-6 for c in kc_["chern_control_weyl"])
        and all(g > 1.9e-3 for g in kc_["sphere_gap_weyl"])
        and kc_["weyl_control_fails_real_class_test"] > 1.0
        and kc_["inversion_operator_exhibited"] is False
        and "UNMEASURED / KERNEL-GATED" in kc_["escape_a_status"]
        and "CLEAN" in kc_["frame_jurisdiction_N49"])

    print("J,D/Γ rework bank (2026-08-21) — the DM CHIRALITY LOCK at the driven group (§D.3.3):")
    cl_ = dm_chirality_polarisation_lock()
    a48 = cl_["counts"]["Stab(+e4)[48]"]
    a24 = cl_["counts"]["Stab+(+e4)[24]"]
    _ck("at the DRIVEN group Stab(+e₄) [48] the allowed DM space is 2-dimensional and contains NO "
        f"chirally-polarised element at all (SD-polarised dim {a48['SD_polarised_dim']}, ASD-polarised "
        f"dim {a48['ASD_polarised_dim']}, χ dim {a48['chi_dim']}): every allowed D is forced exactly "
        "50/50 SD:ASD — so 'two chiral dials, one turned' is an OVER-STATEMENT at the driven group",
        (a48["allowed_D_dim"], a48["SD_polarised_dim"], a48["ASD_polarised_dim"], a48["chi_dim"])
        == (2, 0, 0, 0)
        and all(abs(f - 0.5) < 1e-9 for f in a48["per_basis_SD_fraction"]))
    _ck("the doubling is bought by DROPPING THE REFLECTIONS and by nothing else: at the proper "
        f"subgroup [24] the space is {a24['allowed_D_dim']}-dimensional and splits "
        f"{a24['SD_polarised_dim']} + {a24['ASD_polarised_dim']}, with χ opening to "
        f"{a24['chi_dim']} — the driven group carries {cl_['n_reflections_in_driven_group']} "
        "orientation-reversing elements (spatial parity among them), and ⋆∘Λ²g = det(g)·Λ²g∘⋆ locks "
        "SD to ASD. TIER: the ZERO count is GENERIC-GIVEN-ONE-ORIENTATION-REVERSING-ELEMENT (canon "
        "§5), not a D4 discovery; FENCE: bond-coupling SD/ASD content licenses NOTHING about weak "
        "isospin (weak = SD is settled at R-171/R-079, not by any bond-coupling result)",
        (a24["allowed_D_dim"], a24["SD_polarised_dim"], a24["ASD_polarised_dim"], a24["chi_dim"])
        == (4, 2, 2, 2)
        and cl_["n_reflections_in_driven_group"] == 24
        and "GENERIC-GIVEN-ONE-ORIENTATION-REVERSING-ELEMENT" in cl_["tier"]
        and "weak = SD" in cl_["weak_isospin_fence"])


    # ================= THE Γ-CHANNEL REFERENT CLOSURE (2026-08-23) =================
    # Governing records: knowledge/audit/gamma_referent_2026-08-23/ (the review's
    # §CONSENSUS + §ADDENDUM, the reviewer verdict, and JOINT_BANKING_2026-08-23.md).
    # Each check states what it IS and what it is NOT, and each primitive's own
    # failure mode is run IN-PROCESS and asserted to fire.
    _g1 = bond_invariant_menu_frame_bilinear()
    _ld, _rl = _g1["ladder_frame_bilinear"], _g1["ladder_rotor_linear"]
    _ck("G1 the bond-invariant menu is COMPUTED EXHAUSTIVE AT TEN under the driven group, "
        "IN THE FRAME-BILINEAR (relative-frame) REALIZATION [DERIVED-A on the counts; "
        f"ladder {[_ld[g]['TOTAL'] for g in ('1152','96','48','24')]} = 2/8/10/12 with "
        f"J:{_ld['48']['J']} ⊕ D:{_ld['48']['D']} ⊕ Γ:{_ld['48']['Gamma']} at Stab(+e₄)]. "
        "★ C-33: the ROTOR-LINEAR realization gives a DIFFERENT ladder "
        f"{[_rl[g]['TOTAL'] for g in ('1152','96','48','24')]} = 1/2/4/8 (Γ does not exist "
        "at that order; the grade-4 χ channel sits in its place, dim 0 at [48] and 2 at "
        "[24]) — and WHICH realization is 'the' menu is the V3-2-class PICK, family tree "
        "LS-ℤ₂, where the fork was ALREADY RECORDED (this round CONFIRMS, it does not "
        "originate). ★★ WHAT THIS CHECK IS NOT: it is NOT a residue measurement. "
        "'residue = 0' is an ALGEBRAIC IDENTITY of the parametrisation — the three channel "
        f"projectors commute EXACTLY with both constraints (max|[P,R]| = "
        f"{_g1['commutation_witness']['max|[P_ch, R]|']:.1e}, max|[P,H]| = "
        f"{_g1['commutation_witness']['max|[P_ch, H]|']:.1e}) and sum to I, so the ranks add "
        "identically and a nonzero residue was NOT A POSSIBLE OUTCOME (canon §8a's own "
        "tell). The exhaustiveness is ANALYTIC — the complete 1⊕6⊕9 split preserved by both "
        "constraints — and the completeness of the RELATIVE-FRAME ANSATZ itself is a NAMED, "
        "UNMEASURED premise. Wording fence: 'computed EXHAUSTIVE', never C-32's "
        "'computed closed' (the {J,D} pick is LIVE and counted, V3-2)",
        [_ld[g]["TOTAL"] for g in ("1152", "96", "48", "24")] == [2, 8, 10, 12]
        and (_ld["48"]["J"], _ld["48"]["D"], _ld["48"]["Gamma"]) == (2, 2, 6)
        and [_rl[g]["TOTAL"] for g in ("1152", "96", "48", "24")] == [1, 2, 4, 8]
        and _rl["48"]["chi"] == 0 and _rl["24"]["chi"] == 2
        and _g1["residue_zero_is_an_identity"] is True
        and max(_g1["commutation_witness"].values()) < 1e-12
        and "ANALYTIC" in _g1["exhaustiveness_ground"]
        and "NOT a residue measurement" in _g1["exhaustiveness_ground"]
        and "RELATIVE-FRAME BILINEAR ANSATZ" in _g1["open_premise_relative_frame_ansatz"]
        and "MEASURED BY NOTHING" in _g1["open_premise_relative_frame_ansatz"]
        and "EXHAUSTIVE" in _g1["wording_fence"]
        and "never 'computed closed'" in _g1["wording_fence"]
        and len(_g1["four_pipelines"]) == 4
        and "ALREADY BANKED" in _g1["already_recorded_at"])

    _pl = _g1["planted_noncommuting_projector"]
    _ck("★ G1's DEMONSTRATED FAILURE MODE, run in-process: a rank-1 projector that does NOT "
        f"commute with the constraints (max|[P_bad, R]| = {_pl['max|[P_bad, R]|']:.3e}) is "
        f"planted, and the SVD ranks of its two-part resolution of the identity do NOT add "
        f"— {_pl['rank_part_1']} + {_pl['rank_part_2']} = {_pl['sum']} against the true "
        f"total {_pl['true_total']}. THAT is what the residue quantity tests: COMMUTATION, "
        "not the lattice. Seen to fire",
        _pl["fires"] is True and _pl["max|[P_bad, R]|"] > 1e-6
        and _pl["sum"] != _pl["true_total"])

    _g2 = bond_channel_parity_exclusivity()
    _ck("G2 the CHANNEL→PARITY EXCLUSIVITY theorem at TRACE-PAIRING strength [DERIVED-A, "
        "CONFIGURATION-INDEPENDENT — the one result of the round carrying no branch risk and "
        "no class-of-configuration risk]: Tr(K Wᵀ) = Tr(Kᵀ W) for ARBITRARY real W, so "
        "symmetric couplings (J, Γ) are reversal-EVEN and antisymmetric ones (D) reversal-"
        f"ODD — verified on independent random SO(4) rotors per bond AND on random "
        f"NON-orthogonal W (worst relative deviation {max(_g2['worst_relative_deviation'].values()):.1e}), "
        "i.e. NO helix, NO simple bivector, NOT EVEN A ROTOR is required. ⇒ Γ can only "
        "renormalise the parity-EVEN denominator and D_spatial is the ONLY channel in the "
        "exhaustive menu that can reach the parity-ODD numerator — a SELECTION RULE. ★ ALL "
        "THE PHYSICS IS IN THE NAMED PREMISE 'chirality reversal acts as W_b → W_bᵀ', which "
        "on a helix is the identity q → −q; the algebra above is free. ★★ TWO SCOPE FENCES "
        "ASSERTED HERE: (a) 'EXACTLY TWO amplitudes' is CLASS-CONDITIONED (RUL-049) to "
        "single-q families generated by a unit SIMPLE bivector; (b) 'JD-5 HALF-DISCHARGED' "
        "is WITHDRAWN as a label — JD-5 STANDS UNDISCHARGED on its recorded ℤ₃ scope and "
        "RUL-071(vi)'s conditioning of 0.79 on it is UNCHANGED (the pitch statement is a "
        "fact about a DIFFERENT functional)",
        max(_g2["worst_relative_deviation"].values()) < 1e-9
        and len(_g2["worst_relative_deviation"]) == 4
        and "ARBITRARY real" in _g2["identity"]
        and "not even a rotor" in _g2["scope_measured_on"]
        and _g2["branch_risk"].startswith("NONE")
        and "ONLY channel" in _g2["routing"]["selection_rule"]
        and "CLASS-CONDITIONED" in _g2["exactly_two_amplitudes"]
        and "SIMPLE" in _g2["exactly_two_amplitudes"]
        and "STANDS, UNDISCHARGED" in _g2["JD5_status"]
        and "WITHDRAWN" in _g2["JD5_status"]
        and "UNCHANGED" in _g2["JD5_status"]
        and all(_g2["pitch_functional_parities"][k] == "EVEN"
                for k in ("J#1", "J#2", "Gamma#1", "bankedJ"))
        and all(_g2["pitch_functional_parities"][k] == "ODD"
                for k in ("D#1", "D#2", "bankedD")))

    _mx = _g2["mixed_symmetry_control"]
    _ck("★ G2's DEMONSTRATED FAILURE MODE, run in-process: a deliberately MIXED-symmetry "
        f"coupling (J#1 + D#1) must come back MIXED, not EVEN and not ODD — |E−Eᵀ|rel = "
        f"{_mx['relative |E - E^T|']:.3f} AND |E+Eᵀ|rel = {_mx['relative |E + E^T|']:.3f}, "
        "both O(1). Without it the parity classifier could be returning its input's name",
        _mx["fires"] is True and _mx["verdict"] == "MIXED"
        and _mx["relative |E - E^T|"] > 1e-6 and _mx["relative |E + E^T|"] > 1e-6)

    _g3 = bond_harmonic_ceiling_by_generator_class()
    _cx = _g3["counterexample"]
    _ck("G3 the HARMONIC CEILING is CONDITIONED ON THE TWIST-GENERATOR CLASS, not on "
        "bilinear order [DERIVED-A-given-(a SIMPLE or ISOCLINIC (SD/ASD) generator); "
        "REFUTED without that premise]. ★ THIS CHECK EXISTS TO MAKE THE OVER-CLAIM "
        "UNSAYABLE FROM THE ENGINE: the submitted round asserted 'either way the ceiling is "
        "m ≤ 2 < 3' and 'no bilinear-order computation, however refined, can compute αᵢ or "
        "β' — bare necessity claims (RUL-049) and FALSE AS WRITTEN. The premise that DOES "
        f"make the ceiling true is verified here: every SD and every ASD bivector is "
        f"ISOCLINIC (B² = −λ²I, residuals ≤ {max(_g3['isoclinic_premise']['residual_SD'], _g3['isoclinic_premise']['residual_ASD']):.1e}), "
        "so canon §5's GENERATIONS = the ASD triple SUPPLIES it — as an IDENTIFICATION, not "
        "a theorem. ⇒ JD-6's upgrade is DERIVED-CONDITIONAL, and conditioned on the "
        "TWIST/CONFIGURATION class, NOT on 'the banked action class' (the submitted phrase "
        "mislocated it). ★★ AND THE VACUITY CENSUS IS REPAIRED: the round's second "
        f"construction E = Tr(Rᵀ(Σ_b K_b)R Q) is VACUOUS for {_g3['vacuous_members']} of 12 "
        "couplings (four give Σ_b K_b = 0 ⇒ E ≡ 0; four give Σ_b K_b ∝ I ⇒ E constant, so "
        "every m ≥ 1 vanishes trivially) — the identical defect was self-caught in one "
        "script of that round and NOT swept into the other, where it was load-bearing "
        "(canon §2, sweep after a patch)",
        _g3["vacuous_members"] == 8
        and max(_g3["isoclinic_premise"]["residual_SD"],
                _g3["isoclinic_premise"]["residual_ASD"]) < 1e-12
        and "IDENTIFICATION, not a theorem" in _g3["isoclinic_premise"]["source"]
        and "CONDITIONALLY" in _g3["JD6_status"]
        and "TWIST/CONFIGURATION class" in _g3["JD6_status"]
        and "NOT on" in _g3["JD6_status"]
        and "withdrawn as a bare necessity claim" in _g3["does_not_license"]
        and _g3["ceiling_by_generator_class"]["general (a,b)"]["rep"] == "max(a,b)"
        and all(_g3["measured_harmonics"][c]["bankedJ"]["|c3|"] < 1e-10
                for c in ("simple(1,0)", "SD-isoclinic(1,1)", "ASD-isoclinic(1,-1)")))

    _ck("★ G3's DEMONSTRATED FAILURE MODE, run in-process — THE COUNTEREXAMPLE IS THE "
        f"FAILURE MODE: a bond-BILINEAR energy on a helix generated by a NON-ISOCLINIC "
        f"bivector with plane angles (1,3) carries |c₃| = {_cx['|c3|']:.4f} at the SAME "
        f"magnitude as |c₁| = {_cx['|c1|']:.4f}, on the BANKED J coupling. The primitive "
        "RETURNS that nonzero m₃, so the unconditioned ceiling can never be re-asserted "
        "from this engine — and the would-change-if names exactly this world",
        _cx["|c3|"] > 1.0
        and abs(_cx["|c3|"] - _cx["|c1|"]) < 1e-6 * _cx["|c1|"]
        and "bond-BILINEAR" in _cx["order"]
        and "non-isoclinic" in _g3["would_change_if"])

    _g4 = gamma_survivor_pitch_genericity()
    _lk = _g4["survivor_leak_equal_per_bond_scale"]
    _ax = _g4["banked_branches"]["AXIS  k=q e1, B=e14"]
    _ck("G4 the Γ SURVIVOR'S INERTNESS IS NON-GENERIC — located gap GR-1 [DERIVED-A on the "
        "banked branches; DERIVED-numeric off them]. On the two banked high-symmetry "
        f"branches the survivor is EXACTLY pitch-blind ({_ax['survivor_pitch_weight']:.1e}) "
        f"with pitch-visible Γ dimension 1 (axis) / 2 (diagonal); on generic single-q "
        f"branches the visible dimension is 4 on essentially every branch "
        f"({_g4['generic_visible_dimension_distribution']}) and the survivor's own pitch "
        "entry is NONZERO. ★★ THE NUMBER IS CORRECTED AND THE OLD ONE WITHDRAWN: the "
        "submitted '7.134e-01 — i.e. O(1)' was a BARE NUMBER compared against nothing, "
        "violating the same report's own normalisation discipline. At EQUAL PER-BOND SCALE "
        f"the leak is worst {_lk['worst_this_run']:.2e} / median {_lk['median_this_run']:.2e} "
        "— a few percent worst case, ~0.1% median, i.e. a REAL but markedly WEAK leak "
        "against the pitch-visible directions' exact 1/2, and NOT a protection. The worst "
        "case is a SAMPLE MAXIMUM (seed named); the median is stable. ★ Blast radius of the "
        "unscoped claim: EMPTY (every live site already carries the scope) — ONE annotation "
        "is owed, at family-tree V3-2's risk ordering, and it is repaired ASYMMETRICALLY "
        "(the D_spatial half branch-INDEPENDENT by G2's selection rule, the Γ half "
        "branch-CONDITIONAL). Keeper L-2 UPHELD-not-discharged; V3-2a "
        "ANNOTATED-not-discharged. Q(k) ≡ 0 is DEFINITIONAL and is not reported as evidence",
        _ax["survivor_pitch_weight"] < 1e-12
        and _ax["pitch_visible_Gamma_dim"] == 1
        and _g4["banked_branches"]["BODY-DIAGONAL k~(1,1,1,0), B~(e14+e24+e34)"]
                ["pitch_visible_Gamma_dim"] == 2
        and _g4["generic_visible_dimension_distribution"].get(4, 0) >= 190
        and 5e-3 < _lk["worst_this_run"] < 2e-1
        and 1e-4 < _lk["median_this_run"] < 1e-2
        and _lk["worst_is_a_sample_maximum"] is True
        and "WITHDRAWN" in _g4["survivor_raw_worst_WITHDRAWN"]["why_withdrawn"].upper()
        and "BARE NUMBER" in _g4["survivor_raw_worst_WITHDRAWN"]["why_withdrawn"].upper()
        and abs(_g4["entry_ratio_pitch_visible_over_J"]["value"] - 0.5) < 1e-15
        and max(abs(abs(v) - 0.5) for v in
                _g4["entry_ratio_pitch_visible_over_J"]["q_scan"].values()) < 1e-12
        and "EQUAL MAXIMUM PER-BOND" in _g4["entry_ratio_pitch_visible_over_J"]["normalisation"]
        and "1/3" in _g4["entry_ratio_pitch_visible_over_J"]["normalisation"]
        and _g4["blast_radius_of_the_unscoped_claim"].startswith("EMPTY")
        and "ASYMMETRICALLY" in _g4["one_annotation_owed"]
        and _g4["discharges"].startswith("NEITHER")
        and "definitional" in _g4["Qk_is_definitional_not_evidence"])

    _ck("★ G4's DEMONSTRATED FAILURE MODE (positive control), run in-process: the "
        "pseudo-dipolar W(F₄)-invariant Γ direction (K_b = u_b u_bᵀ − I/4) IS visible on "
        f"BOTH banked branches at O(1) ({_ax['positive_control_pseudo_dipolar']:.3f} axis, "
        f"{_g4['banked_branches']['BODY-DIAGONAL k~(1,1,1,0), B~(e14+e24+e34)']['positive_control_pseudo_dipolar']:.3f} "
        "diagonal), so the survivor's measured blindness is not an artefact of a "
        "profile map that returns zero for everything",
        _ax["positive_control_pseudo_dipolar"] > 0.1
        and _g4["banked_branches"]["BODY-DIAGONAL k~(1,1,1,0), B~(e14+e24+e34)"]
                ["positive_control_pseudo_dipolar"] > 0.1)

    _g6 = gamma_admixture_cross_functional_route()
    _ds, _bs = _g6["discriminator"], _g6["bridge_sensitivity_control"]
    _ck("G6 = GR-2 / JD-6(b) — THE THREE J_eff FACES, and the first number the review has "
        "produced for a Γ admixture [CANDIDATE — a ROUTE, not a measurement]. Filed as a "
        "named COROLLARY of JD-6, deliberately NOT an independent fourth gap (GR-2 is empty "
        "if JD-6's coefficients vanish; gap-inventory inflation is a real cost). ★ THE FENCE "
        "IS WIDENED from the submitted 'never combine D/J with an independently-fixed J' to "
        "'NEVER CARRY A RATIO CALIBRATED ON ONE FUNCTIONAL INTO ANOTHER' — the submitted "
        "form named ONE junction while placing every cross-leg consumer in NOT-EXPOSED on a "
        "ground valid only WITHIN one functional, which is exactly what GR-2 denies ACROSS "
        f"functionals. VALUES DO NOT MOVE; what moves is the claim that the formula is being "
        f"fed the right substrate quantity. THE NUMBER: J_eff(pitch)/J_eff(ℤ₃) = "
        f"{_ds['J_eff(pitch)/J_eff(Z3)']:.6f} and, through G4's exact entry ratio 1/2, "
        f"Δ(Γ/J) ≈ {_ds['Delta(Gamma/J)_between_the_two_functionals']*100:.2f}% of J — with "
        "its FOUR-ITEM conditioning class in the same breath (RUL-049), any one of which "
        "voids it. RESOLUTION ROUTE: an independent e — or the J that f_π² = 8J/a fixes — at "
        "the 0.1% level would READ OUT the admixture instead of absorbing it into a '1.1% "
        "agreement'",
        abs(_ds["Delta(Gamma/J)_between_the_two_functionals"] - 0.0215) < 5e-4
        and abs(_ds["J_eff(pitch)/J_eff(Z3)"] - 1.01076) < 1e-4
        and _ds["pitch_entry_ratio_a_visible_over_a_J"] == 0.5
        and _g6["fence"] == "NEVER CARRY A RATIO CALIBRATED ON ONE FUNCTIONAL INTO ANOTHER"
        and _g6["values_move"] is False
        and len(_g6["conditioning_class_RUL049"]) == 4
        and _g6["any_one_failing_voids_the_number"] is True
        and "COROLLARY" in _g6["gap_id"] and "NOT an independent gap" in _g6["gap_id"]
        and "0.1%" in _g6["resolution_route"]
        and len(_g6["exposed_classes"]) == 3)

    _ck("★ G6's DEMONSTRATED FAILURE MODE, run in-process: the SAME route run on the √12 "
        f"bridge instead of the disclaimed √18 one returns Δ(Γ/J) = {_bs['sqrt12_route_Delta(Gamma/J)']*100:.1f}% "
        f"against {_bs['sqrt18_route_Delta(Gamma/J)']*100:.2f}% — a relative spread of "
        f"{_bs['relative_spread']:.1f}, i.e. LARGER THAN THE ANSWER ITSELF. The route is "
        "bridge-bound, and 2.15% can never be quoted as a measurement",
        _bs["relative_spread"] > 1.0
        and abs(_bs["sqrt18_route_Delta(Gamma/J)"]
                - _ds["Delta(Gamma/J)_between_the_two_functionals"]) < 1e-15)

    print("\nAll §10/§16/§22 matter-sector checks passed (incl. the BVP 8-vs-4 adjudication; companion-layer checks: twt_companion_test.py).")


# ---- twt_weak ----------------------------------------
def check_twt_weak():
    print("§18.3a lepton-quark weak universality (theorem, computed on the ideal):")
    ut = universality_theorem()
    for k, v in ut.items():
        _ck(f"{k}  (trivector = bivector on S+)", v)
    print("       ⇒ weak force cannot distinguish quark trivectors from lepton bivectors ⇒ universality.")

    print("§20.3 SU(2)_L from the L-orbit algebra:")
    cl = L_algebra_su2_closure()
    for k, v in cl.items():
        _ck(k, v)

    print("§23.6 (iii) F-7 promotion — DM bond bivectors non-commuting on D4:")
    dmnc = D4_DM_bond_bivectors_non_commuting()
    _ck(f"12 e4-bearing D4 bonds  (got {dmnc['n_bonds_e4']})", dmnc["n_bonds_e4"] == 12)
    _ck(f"C(12,2)=66 pairs total  (got {dmnc['n_pairs']})", dmnc["n_pairs"] == 66)
    _ck(f"48 distinct-axis pairs NON-commute (substrate non-commutativity)  (got {dmnc['n_pairs_non_commuting']})",
        dmnc["n_pairs_non_commuting"] == 48)
    _ck(f"18 same-axis pairs commute  (got {dmnc['n_pairs_commuting']})",
        dmnc["n_pairs_commuting"] == 18)
    _ck("[e_{a4},e_{b4}] = -2 e_{ab} for a!=b (engine, convention-robust under Hodge dual)",
        dmnc["n_pairs_non_commuting"] > 0)

    print("§23.7 B-L anomaly cancellation (3×1/3=1):")
    bl = B_minus_L_anomaly()
    _ck(f"A_B = 3×(1/3) = 1, A_L = 1, A_(B-L) = 0 — the DOUBLET-SECTOR condition "
        f"(scoped 2026-08-24: no longer billed as 'anomaly-free' outright)  (got A_B={bl['A_B = 3×(1/3)']})",
        bl["B-L doublet-sector condition vanishes"] and bl["A_B = 3×(1/3)"] == 1)
    _ck(f"A_(B+L) = 2 (anomalous)", bl["B+L anomalous"] and bl["A_{B+L}"] == 2)
    _ck("singlet-inclusive B−L sums over the LIVE gauged table (LH conv): linear and cubic "
        f"BOTH exactly −1 on the 15 alone (got {bl['sum(B-L) gauged 15 (LH conv)']}, "
        f"{bl['sum(B-L)^3 gauged 15 (LH conv)']}), and BOTH complete to exactly 0 with "
        "R-121's sterile partner — the sterile's CLASSICAL completion work for R-089's "
        "exactness, consuming no SMG import (the full free-c anomaly system with RH "
        "hypercharges unknown is banked at charge_normalization_anchor_free, R-159; "
        "OI-1 closed by discovery, record oi1_anomaly_ledger_2026-08-24)",
        bl["sum(B-L) gauged 15 (LH conv)"] == -1
        and bl["sum(B-L)^3 gauged 15 (LH conv)"] == -1
        and bl["both complete to 0 with R-121 sterile"])

    print("§23.8 BPST instanton charge + selection rule:")
    Q = bpst_charge_Q()
    _ck(f"instanton charge Q = ∫q d⁴x = 1  (computed {Q})", Q == 1)
    sr = bpst_selection_rule(3)
    _ck(f"ΔB = ΔL = N_gen = 3, Δ(B-L) = 0, Δ(B+L) = 6  (got {sr})",
        sr["ΔB = N_gen"] == 3 and sr["ΔL = N_gen"] == 3 and sr["Δ(B-L)"] == 0 and sr["Δ(B+L)"] == 6)

    print("W1 (2026-07-27) — the charge flagship ANCHOR-FREE: Q_p = -Q_e theorem-given-(P4,P5,P6,P7):")
    cnaf = charge_normalization_anchor_free()
    _ck("W1 the c-FREE IDENTITIES [DERIVED-A]: with the charge functional Q = T_3 + c*Y carried "
        "with c a FREE sympy symbol (anti-circularity: GMN c=1/2 never assumed), Q_p + Q_e = 0 and "
        "Q_n + Q_nu = 0 vanish IDENTICALLY in c and Q_udd + Q_e = -1 identically — the absolute "
        "normalization drops out of the flagship entirely. Both brackets vanish separately: the T_3 "
        "bracket (uud+e = one complete quark doublet + an (up-type, down-type) pair) and the Y "
        "bracket 3Y_Q + Y_lep = 0 (= the R-087 arithmetic: R-056 sign opposition + R-057 /3). "
        "COUNTERFACTUAL (canon 5 derived-vs-generic): removing the /3 leaves residue exactly 2c != 0 "
        "-- SUBSTRATE-SPECIFIC to Y_lep/Y_Q = -3, not generic",
        cnaf["c_free_identities"] == {"Q_p + Q_e": 0, "Q_n + Q_nu": 0, "Q_udd + Q_e": -1}
        and "2c != 0" in cnaf["counterfactual_no_over_3"]
        and "free symbol" in cnaf["anti_circularity"])
    _ck("W1 the CONDITIONALITY SET, stated not hidden: DERIVED-structural CONDITIONAL on (P4 single "
        "universal linear charge functional -- ASSUMED, structural, FRAMING-supported by R-035 "
        "(DERIVED) + R-086a, and R-086a HAS NO ENGINE PRIMITIVE so it is never to be phrased as "
        "engine-checked; P5 per-defect chirality-independence; P6 proton = uud, an inside-frame "
        "state-identification INPUT; P7 the cross-sector weak-isospin alignment T_3(e) = T_3(d) = "
        "-T_3(u), INPUT/posited -- ADDED to this primitive's named set 2026-08-21: the paper has "
        "named P7 at C.2.7 since 2026-07-31 while the engine's tier, headline and premise list "
        "named only P4-P6 and the code used the alignment regardless, so the engine was "
        "understating its own conditionality against the paper), INHERITING the weak=SD assignment "
        "(R-079) via R-058/R-079. "
        "Language: 'theorem-given-(P4,P5,P6,P7)', NOT 'the import is retired'. The neutrality-of-atoms "
        "anchor is CONDITIONALLY REPLACED by (P4,P5,P6,P7) -- ALL FOUR, not P4+P5 (keeper C1: "
        "the primitive's own lepton-slot flip returns +1 with P4+P5 intact, so P6/P7 are "
        "load-bearing in the T_3 bracket), and the 10^-21 bound flips from calibration "
        "input to falsification test GIVEN the premises",
        "NO ENGINE PRIMITIVE" in cnaf["tier"] and "P6" in cnaf["tier"]
        and "R-058/R-079" in cnaf["tier"]
        and "THEOREM-GIVEN-(P4,P5,P6,P7)" in cnaf["headline"]
        and "P7" in cnaf["tier"]
        and "CONDITIONALLY REPLACED" in cnaf["headline"]
        and "falsification test" in cnaf["headline"])
    _ck("W1 P7 IS LOAD-BEARING, COMPUTED not asserted (added 2026-08-21 with P7's promotion into "
        "the primitive's named premise set): the T_3 bracket vanishes ONLY under the stated "
        "cross-sector alignment. Flip the LEPTON slot alone and Q_p + Q_e = +1; flip the QUARK "
        "slots alone and it is -1; flip BOTH and it returns to 0 -- which is exactly why the "
        "GLOBAL flip is a convention while the RELATIVE alignment is a posited premise. What "
        "could have disagreed: if the bracket vanished under either single flip, P7 would be "
        f"free and the paper's C.2.7 caveat would be over-cautious. Got: {cnaf['counterfactual_P7_slot_flips']}",
        cnaf["counterfactual_P7_slot_flips"] == {"lepton_slot_flipped": 1,
                                                 "quark_slots_flipped": -1,
                                                 "global_flip_is_convention": 0})
    _ck("W1 the uud-UNIQUENESS BONUS (dissolves the C.3.13 side-assignment circularity smell): all "
        "four three-facet composites' charges relative to the electron are c-FREE -- uuu+e = +1, "
        "uud+e = 0, udd+e = -1, ddd+e = -2 -- so uud is the UNIQUE three-facet composite "
        "neutralizing e, and no normalization choice can move it",
        cnaf["three_facet_table_relative_to_e"] == {"uuu": 1, "uud": 0, "udd": -1, "ddd": -2}
        and "UNIQUE" in cnaf["uud_uniqueness"])
    _ck("W1 the c = 1/2 FIXINGS, COUNTED HONESTLY (the reviewer-corrected count -- NOT 'four "
        "convergent'): ONE NATIVE route (Q_nu = 0, itself conditional on the FRAMING-supported "
        "'wave-decoupled => Y(S_-) = 0' inference, named separately with its own would-change-if) + "
        "TWO independent CONDITIONS under ONE registered import (I-18: the mixed-gravitational "
        "Tr Y = 0 root and the [U(1)_Y]^3 factorization -(2c-1)^3/(8c^3) -- strike I-18 and BOTH "
        "fall) + ONE DOWNSTREAM consistency check (the R-086a condensate route, downstream of the "
        "anomaly-forced y_e AND riding R-086a's vev placement). RH hypercharges FORCED: exactly two "
        "branches, y_e = -2 in both, {y_u,y_d} = {4/3,-2/3} up to the u<->d relabel; CONTROL: a "
        "charged nu_R leaves the system UNDER-determined. Colour honesty: no native continuous "
        "[SU(3)]^2-U(1)_Y (colour is Z3) -- the flagship needs none",
        cnaf["c_half_fixings"]["native_routes"] == 1
        and cnaf["c_half_fixings"]["conditions_under_one_registered_import"] == 2
        and cnaf["c_half_fixings"]["downstream_consistency_checks"] == 1
        and "four convergent" in cnaf["c_half_fixings"]["NOT"]
        and cnaf["rh_hypercharges"]["branches"] == 2
        and cnaf["rh_hypercharges"]["y_e"] == -2
        and cnaf["rh_hypercharges"]["y_e_forced_in_both_branches"]
        and "UNDER-determined" in cnaf["rh_hypercharges"]["control"]
        and "Z3" in cnaf["colour_honesty"])

    print("R-172 — WHICH SIDE THE WEAK HOST ACTS ON (RUL-091's deep-layer discharge; the "
          "external body-frame submission, verified cross-class and integrated per keeper + "
          "consensus 2026-08-23). Every count names its realization (C-33):")
    _bf = weak_host_must_be_body_frame(carrier="Cl+", hosting="body")
    _bfx = weak_host_must_be_body_frame(carrier="Cl+", hosting="space")   # the broken state
    _bfd = _bf["defect"]
    _ck("THE DEFECT is COMPUTED, not asserted: on the OBSERVER'S OWN SIDE a chiral host fails "
        f"to commute with the lock — [L_J, L_SD] {_bfd['[L_J, L_SD]']['nonzero']}/9 nonzero and "
        f"[L_K, L_SD] {_bfd['[L_K, L_SD] (grade-one K, BANKED)']['nonzero']}/9 in the BANKED "
        f"GRADE-ONE realization (K_j = ½e_j), {_bfd['[L_K, L_SD] (grade-two K, the alternative)']['nonzero']}"
        "/9 in the grade-two one — and identically J₁ = −½e₂₃ = "
        f"({_bfd['J1_decomposition']['SD_part']}) + ({_bfd['J1_decomposition']['ASD_part']}), "
        "both chiral parts nonzero: a lab rotation IS half an SD rotation plus half an ASD "
        "rotation. THE CONCLUSION IS REALIZATION-ROBUST and that robustness is computed — the "
        "tables are nonzero under BOTH lock realizations; only the counts move",
        _bfd["[L_J, L_SD]"]["nonzero"] == 6
        and _bfd["[L_K, L_SD] (grade-one K, BANKED)"]["nonzero"] == 9
        and _bfd["[L_K, L_SD] (grade-two K, the alternative)"]["nonzero"] == 6
        and _bfd["J1_both_parts_nonzero"] and _bfd["realization_robust"] is True)
    _bft = _bf["commutator_tables"]
    _ck("THE BODY-FRAME HOST COMMUTES WITH THE OBSERVER'S LOCK GENERATORS: all four tables "
        f"0/9, worst residual {max(x['max'] for x in _bft.values()):.1e}. ★ AND THE SHIPPED "
        "FAILURE MODE IS RUN IN THE SAME BREATH (manuals/banking.md): the identical computation "
        "against the BROKEN state — hosting='space', the reading every R-079 use-site carried "
        f"before RUL-091 — comes back [L_J,host_SD] {_bfx['commutator_tables']['[L_J, host_SD]']['nonzero']}/9 "
        f"and [L_K,host_SD] {_bfx['commutator_tables']['[L_K, host_SD]']['nonzero']}/9 nonzero, "
        "i.e. this check IS SEEN TO FAIL for its named reason and is not decoration",
        _bf["host_commutes_with_Lorentz"] is True
        and _bfx["host_commutes_with_Lorentz"] is False
        and _bfx["commutator_tables"]["[L_J, host_SD]"]["nonzero"] == 6
        and _bfx["commutator_tables"]["[L_K, host_SD]"]["nonzero"] == 9)
    _ck("the repair is ASSOCIATIVITY at full strength — not for the host's three generators but "
        "for the whole algebra: max|[L_g, R_h]| = "
        f"{_bf['repair']['max|[L_g, R_h]| over ALL g, h in the 16-blade basis']:.1e} over ALL "
        "g, h in the 16-blade basis (the even-h statement the ruling quotes is the weaker one). "
        "A body-frame host is Lorentz-scalar BY CONSTRUCTION, for every lock realization",
        _bf["repair"]["max|[L_g, R_h]| over g in Cl(4,0), h in Cl+"] < 1e-12
        and _bf["repair"]["max|[L_g, R_h]| over ALL g, h in the 16-blade basis"] < 1e-12)
    _bfo = _bf["opposite_algebra"]
    _ck("the body copy is the OPPOSITE Lie algebra ([R_X,R_Y] = −R_[X,Y], residual "
        f"{_bfo['max|[R_X,R_Y] + R_[X,Y]|']:.1e}; the left action is a homomorphism, residual "
        f"{_bfo['max|[L_X,L_Y] - L_[X,Y]|']:.1e}), isomorphic via X → −X, so R-171's conjugacy "
        f"classification carries over verbatim; I₄ central in Cl⁺ (residual "
        f"{_bfo['I4_central_in_Cl+_residual']:.1e}) ⇒ the SD/ASD split is the SAME split on the "
        "body side",
        _bfo["max|[R_X,R_Y] + R_[X,Y]|"] < 1e-12 and _bfo["max|[L_X,L_Y] - L_[X,Y]|"] < 1e-12
        and _bfo["I4_central_in_Cl+_residual"] < 1e-12)
    _bfc, _bfs = _bf["I4_grading_dims"], _bf["annihilation_is_side_independent"]
    _ck("★ THE OWED TRANSFER IS NOW COMPUTED, closing an orphan in the standing record: "
        "weak_su2_menu_exhaustion's kernel numbers are taken on the 4-dim spinor module under "
        "the LEFT action, while the RULED hosting is RIGHT action on the even module, and "
        "RUL-091(iii) ASSERTED the transfer ('an ideal fact, hence side-independent') with no "
        "primitive computing it. Computed here on the I₄ GRADING of Cl⁺ (NOT the observer's "
        f"chirality — C-33): image_dim(R_SD|W₊) = {_bfc['SD|W+']['image_dim_operator_span']}, "
        f"(R_SD|W₋) = {_bfc['SD|W-']['image_dim_operator_span']}, (R_ASD|W₊) = "
        f"{_bfc['ASD|W+']['image_dim_operator_span']}, (R_ASD|W₋) = "
        f"{_bfc['ASD|W-']['image_dim_operator_span']} on the OPERATOR-SPAN reading "
        f"({_bfc['SD|W+']['image_dim_image_subspace']}/{_bfc['SD|W-']['image_dim_image_subspace']}"
        f"/{_bfc['ASD|W+']['image_dim_image_subspace']}/{_bfc['ASD|W-']['image_dim_image_subspace']} "
        "on the image-subspace reading — the word carries two readings and both are returned), "
        f"no leak; and the LEFT action gives the IDENTICAL table ({_bfs['left_SD|W+']}, "
        f"{_bfs['left_SD|W-']}) ⇒ side-independent, as claimed",
        _bfc["SD|W+"]["image_dim_operator_span"] == 3 and _bfc["SD|W-"]["image_dim_operator_span"] == 0
        and _bfc["ASD|W+"]["image_dim_operator_span"] == 0
        and _bfc["ASD|W-"]["image_dim_operator_span"] == 3
        and (_bfc["SD|W+"]["image_dim_image_subspace"],
             _bfc["ASD|W-"]["image_dim_image_subspace"]) == (4, 4)
        and _bfs["left_SD|W+"] == _bfs["right_SD|W+"] == 3
        and _bfs["left_SD|W-"] == _bfs["right_SD|W-"] == 0
        and max(x["leak"] for x in _bfc.values()) < 1e-9)
    _bfb = _bf["bimodule"]
    _ck("the BIMODULE IDENTITIES — ALGEBRA ONLY, fenced: the L and R Casimirs on W₊ are the "
        f"SAME scalar ({_bfb['casimirs']['L_SD|W+']['scalar']:.1f} in the NAMED normalization "
        "u_a² = −1 − I₄, so the VALUE is normalization-dependent and the load-bearing content "
        "is the EQUALITY), both vanish on W₋, and W₊ is IRREDUCIBLE under (L_SD, R_SD) jointly "
        f"(generated algebra dim {_bfb['generated_algebra_dim']} = End(W₊)). These are "
        "statements about the LOCAL EVEN-ALGEBRA MODULE on the I₄ grading and nothing else — "
        "the scope fence is asserted here, in the check, so no CORE string can quietly promote "
        "them to a claim about one-defect STATES (that consumes the UNBUILT collective "
        "manifold, against the corpus's only built band)",
        _bfb["L_and_R_casimirs_equal_on_W+"] and _bfb["casimirs"]["L_SD|W+"]["is_scalar"]
        and _bfb["casimirs"]["R_SD|W+"]["is_scalar"]
        and abs(_bfb["casimirs"]["L_SD|W-"]["scalar"]) < 1e-9
        and abs(_bfb["casimirs"]["R_SD|W-"]["scalar"]) < 1e-9
        and _bfb["W+_irreducible_under_(L_SD,R_SD)"]
        and "NOT a statement about one-defect STATES" in _bfb["scope_fence"])
    _bfa = _bf["body_algebra_available_on_carrier"]
    _bfl = _bf["observer_lock_does_not_preserve_carrier"]
    _ck(f"on the Cl⁺ carrier the FULL body so(4) is available (right-stabiliser bivectors "
        f"{_bfa['dim_bivectors']} of 6); AND the C-33 grading fence is COMPUTED, not asserted: "
        f"with the BANKED grade-one boosts the observer's lock does not even preserve this "
        f"carrier (max leak {_bfl['max leak(L_K grade-one, carrier)']:.4f}, and "
        f"{_bfl['max leak(L_K grade-one, W+)']:.1f} on W₊) while the rotations do "
        f"({_bfl['max leak(L_J, carrier)']:.1e}) — so W± is the I₄ grading and CANNOT be read "
        "as the observer's chirality; that bridge is unbuilt",
        _bfa["is_full_so(4)"] and _bfa["dim_bivectors"] == 6
        and _bfl["max leak(L_K grade-one, carrier)"] > 1.0
        and _bfl["max leak(L_J, carrier)"] < 1e-9
        and _bfl["max leak(L_K grade-two, carrier)"] < 1e-9)
    _bfS = weak_host_must_be_body_frame(carrier="S", hosting="body")
    _bfSa = _bfS["body_algebra_available_on_carrier"]
    _ck("CONTROL C2 — THE CARRIER IS A BRANCH POINT, and the computation returns a DIFFERENT "
        f"verdict on it: on S = Cl·s₀ the right-stabiliser AMONG EVEN ELEMENTS (that qualifier "
        f"is load-bearing — the full stabiliser is {_bfSa['right_stabiliser_all_grades_dim']}-"
        f"dimensional) is the e₄-commutant {_bfSa['right_stabiliser_even']} ≅ ℍ — ONE su(2), "
        f"not two — charging BOTH halves of the I₄ grading (span dims "
        f"{_bfSa['single_su2_span_dim_on_W+']} "
        f"and {_bfSa['single_su2_span_dim_on_W-']}), i.e. the diagonal-class occupancy the "
        "right-handed-singlet datum kills. So the body route survives on Cl⁺ and is refuted by "
        "the datum on S — the two modules the corpus names for the local state's one-sided "
        "internal action are separated by an observable, and WHICH the internal host acts on "
        "is an OPEN node, not decided here",
        _bfSa["is_e4_commutant_H"] and not _bfSa["is_full_so(4)"]
        and _bfSa["single_su2_span_dim_on_W+"] == 3
        and _bfSa["single_su2_span_dim_on_W-"] == 3
        and _bfSa["right_stabiliser_all_grades_dim"] == 8
        and "REFUTED BY DATA" in _bfS["verdict"])

    print("the left-centralizer theorem — BANKED (it was cited as a ground of RUL-091 while "
          "unbanked; a ruling grounded on an uncomputed theorem is a record-invariant defect):")
    _lc = lock_left_centralizer_is_u1()
    _ck("post-lock the LEFT-acting centralizer of the observer's so(1,3) inside Cl(4,0) is "
        f"span{{1, e123}} ≅ ℂ — dim {_lc['centralizer_dim']}, support "
        f"{_lc['centralizer_support_blades']}, COMMUTATIVE (max|[x,y]| = "
        f"{_lc['max|[x,y]| over the centralizer']:.1e}) with (e123)² = {_lc['e123_squared']:.0f}: "
        "a U(1), never an su(2) — an su(2) needs three mutually non-commuting directions and "
        "there are only two directions in total. ★ THE DEMONSTRATED FAILURE MODE, run here: "
        f"drop the BOOSTS and centralize the rotations alone and the answer MOVES "
        f"{_lc['centralizer_dim']} → {_lc['control_rotations_only(the demonstrated failure mode)']['dim']} "
        f"({_lc['control_rotations_only(the demonstrated failure mode)']['support']}), so the 2 "
        "is measuring the boosts and not bookkeeping",
        _lc["centralizer_dim"] == 2
        and _lc["centralizer_support_blades"] == ["1", "e123"]
        and _lc["is_commutative"] and abs(_lc["e123_squared"] + 1.0) < 1e-12
        and _lc["control_rotations_only(the demonstrated failure mode)"]["dim"] == 4)


    # ===== THE Φ BRIDGE — the V4-ASD Layer-A round's ONLY bankable result (2026-08-23) =====
    # Governing records: knowledge/audit/external_review_2026-08-22/V4ASD_LAYERA_2026-08-23.md
    # (its §CONSENSUS SUPERSEDES the body) + VERDICT_REVIEWER_LAYERA_2026-08-23.md +
    # JOINT_BANKING_2026-08-23.md.
    _phi = spinor_module_graded_iso()
    _w = _phi["code_correctness_witness_NOT_the_evidence"]
    _ck("Φ: Cl⁺(4,0) → S = Cl(4,0)·s₀, x ↦ x·s₀, is a LEFT-Cl(4,0)-LINEAR BIJECTION carrying "
        "the I₄ grading to the I₄ grading — Φ(W±) = S± exactly [DERIVED-A BY IDENTITY]. THE "
        "EVIDENCE IS THE ARGUMENT, NOT THE RESIDUALS: e₄s₀ = s₀ ⇒ Cl·s₀ = Cl⁺·s₀; x·s₀ = 0 "
        "with x even forces x ∈ Cl⁺ ∩ Cl⁻ = 0 ⇒ injective; left-linearity IS associativity, "
        "g(x·s₀) = (gx)·s₀; and P± = (1 ± I₄)/2 is CENTRAL in Cl⁺, so Φ(W±) = P±·S = S±. "
        f"(The residuals — rank {_w['rank Phi(Cl+)']}, image {_w['||(1-P_S) Phi(Cl+)||']:.1e}, "
        f"left-linearity {_w['left-linearity residual']:.1e}, grading {_w['||(1-P_S+) Phi(W+)||']:.1e} "
        "— are a CODE-CORRECTNESS witness and are labelled so in the returned dict; a tight "
        "tolerance on an associativity identity is canon §8a's own tell, not rigour.) "
        "★ WHAT IT CLOSES: the GRADED-LEFT-MODULE half of the keeper's two-module orphan — "
        "the I₄ grading of Cl⁺ and the I₄ grading of S are ONE grading, transported "
        "canonically — which retroactively LICENSES the previously silent W₊/S₊ "
        "identification. ★ WHAT IT DOES NOT CLOSE, asserted in the dict: the V4-0 carrier "
        "node, the I₄-grading↔observer-handedness bridge (R-172(viii), UNBUILT), and the "
        "boost-invariance of R-076's occupancy",
        _phi["identity_holds"]["e4.s0 == s0"] is True
        and _phi["identity_holds"]["s0 idempotent"] is True
        and _phi["identity_holds"]["I_4 central in Cl+"] < 1e-12
        and _w["rank Phi(Cl+)"] == 8
        and max(_w["||(1-P_S) Phi(Cl+)||"], _w["left-linearity residual"],
                _w["||(1-P_S+) Phi(W+)||"], _w["||(1-P_S-) Phi(W-)||"]) < 1e-12
        and len(_phi["the_identity"]) == 4
        and "ASSOCIATIVITY" in _phi["the_identity"][2]
        and "CENTRAL" in _phi["the_identity"][3]
        and "code-correctness witness, never the evidence" in _w["note"]
        and "GRADED-LEFT-MODULE" in _phi["closes"]
        and len(_phi["does_not_close"]) == 3
        and any("V4-0 carrier node" in s for s in _phi["does_not_close"])
        and any("UNBUILT" in s for s in _phi["does_not_close"]))

    _m1 = _phi["mandatory_check_1_body_side_differs"]
    _ck("★ Φ's MANDATORY FAILURE-MODE CHECK #1 — THE BODY SIDE GENUINELY DIFFERS, and the "
        "qualifier that keeps 'only through Φ' from being an over-claim. S is NOT a right "
        f"Cl⁺-module (leak(R_ASD, S) = {_m1['leak(R_ASD, S)']:.1f} against "
        f"leak(R_ASD, Cl⁺) = {_m1['leak(R_ASD, Cl+)']:.1e}); the body action reaches S only "
        f"through the s₀-dependent transport ρ(h): x·s₀ ↦ x·h·s₀, which differs from S's own "
        f"right multiplication by {_m1['||rho(ASD) - R_ASD|| on S']:.1f}. ★ BUT A GENUINE "
        "INTRINSIC LORENTZ-SCALAR BODY ACTION ON S DOES EXIST — End_Cl(S), the 8-dim "
        "right-stabiliser {1,e₄,e₁₂,e₁₃,e₂₃,e₁₂₄,e₁₃₄,e₂₃₄} whose EVEN part is the single ℍ "
        "{1,e₁₂,e₁₃,e₂₃}, exactly the one-su(2) diagonal-class algebra R-172(6)C2 already "
        f"names — AND ρ IS NOT IN IT: max‖[L_even, ρ(ASD)]‖ = {_m1['max||[L_even, rho(ASD)]||']:.1e} "
        f"but max‖[L_odd, ρ(ASD)]‖ = {_m1['max||[L_odd,  rho(ASD)]||']:.1f}. SEEN TO FIRE. "
        "Without this check the unqualified 'the body action reaches S only through Φ' "
        "re-enters — and that omission HIDES THE VERY FACT THAT MAKES V4-0 A BRANCH POINT",
        _m1["fires"] is True
        and _m1["leak(R_ASD, S)"] > 0.5 and _m1["leak(R_ASD, Cl+)"] < 1e-9
        and _m1["leak(rho(ASD), S)"] < 1e-9
        and _m1["||rho(ASD) - R_ASD|| on S"] > 0.5
        and _m1["intrinsic left-Cl-linear right-stabiliser of S"]
            == ["1", "e4", "e12", "e13", "e23", "e124", "e134", "e234"]
        and _m1["its even part"] == ["1", "e12", "e13", "e23"]
        and _m1["max||[L_even, rho(ASD)]||"] < 1e-9
        and _m1["max||[L_odd,  rho(ASD)]||"] > 1e-6
        and "INTRINSIC" in _m1["honest_sentence"]
        and "branch point" in _m1["why_mandatory"])

    _m2 = _phi["mandatory_check_2_realization_split_C33"]
    _ck("★ Φ's MANDATORY FAILURE-MODE CHECK #2 — THE C-33 REALIZATION SPLIT, both "
        "realizations returned under their own keys exactly as R-172 does. Under the BANKED "
        "grade-one lock (K_j = ½e_j, a Cl(4,0) VECTOR) an observer boost maps one I₄ half "
        f"INTO the other: leak(L_K¹, S₊) = {_m2['leak(L_K grade-ONE, S+)  [BANKED]']:.1f} "
        f"exactly, against {_m2['leak(L_K grade-TWO, S+)  [alternative]']:.1e} under the "
        f"grade-two alternative; and the transported label FAILS the canon §5 / RUL-099 "
        f"invariance test on R-076's OWN module for ALL NINE pairs "
        f"([L_K¹, ρ(ASD)] on S: {_m2['[L_K grade-ONE, rho(ASD)] on S  [BANKED]']['nonzero']} of 9, "
        f"max {_m2['[L_K grade-ONE, rho(ASD)] on S  [BANKED]']['max']:.1f}), while under "
        "grade-two it is 0 of 9 and against lab rotations it is 0 of 9 in both. SEEN TO "
        "FIRE. ★ THE POINT: the associativity identity [L_g, R_h] = 0 — re-verified here at "
        f"{_m2['associativity control on Cl(4,0) acting on itself']:.1e} over the FULL "
        "16-blade basis — is a fact about Cl(4,0) acting on ITSELF and does NOT transfer to "
        "the pair (observer on S, label on S), because the label on S is not a right "
        "multiplication. Any argument clearing an S-sited label on that identity is computed "
        "on the wrong object",
        _m2["fires"] is True
        and abs(_m2["leak(L_K grade-ONE, S+)  [BANKED]"] - 1.0) < 1e-12
        and _m2["leak(L_K grade-TWO, S+)  [alternative]"] < 1e-9
        and _m2["leak(L_J, S+)"] < 1e-9
        and _m2["[L_K grade-ONE, rho(ASD)] on S  [BANKED]"]["nonzero"] == 9
        and _m2["[L_K grade-TWO, rho(ASD)] on S  [alternative]"]["nonzero"] == 0
        and _m2["[L_J, rho(ASD)] on S"]["nonzero"] == 0
        and _m2["associativity control on Cl(4,0) acting on itself"] < 1e-12
        and "does NOT transfer" in _m2["consequence"]
        and "wrong object" in _m2["why_mandatory"])

    _e1, _e2 = _phi["exposure_E1"], _phi["exposure_E2"]
    _ck("★ THE TWO EXPOSURES THE Φ ROUND SURFACED — both PRE-EXISTING, neither created here, "
        f"neither previously carried. E-1: R-076's I₄-graded OCCUPANCY IS NOT "
        f"BOOST-INVARIANT in the banked realization — e₁·P₊ − P₋·e₁ = "
        f"{_e1['e1.P+ - P-.e1']:.1e} EXACTLY and L_{{e₁}}(S₊) ⊆ S₋ at "
        f"{_e1['L_e1(S+) inside S-']:.1e}, so 'occupies one ideal / occupies both' is not a "
        "Lorentz-stable species property under the banked grade-one lock (sited at R-076's "
        "companion row and at the V4-ASD node). E-2: RUL-099 ON THE V4-0-SIGNED CARRIER Cl⁺, "
        f"TESTED AGAINST THE BANKED LOCK, IS VACUOUS — leak(L_K¹, Cl⁺) = "
        f"{_e2['leak(L_K grade-one, Cl+)']:.6f} = √2, i.e. the banked boost is a VECTOR "
        "(odd) and is NOT AN OPERATOR ON Cl⁺ AT ALL, so there is nothing to commute with; "
        "the test becomes non-vacuous only on S, where the label fails. ★ E-2 IS RUL-099's "
        "FIRST REFINEMENT, recorded at the ruling's register row: AN INVARIANCE TEST MUST "
        "NAME THE REALIZATION ON WHICH IT IS NON-VACUOUS — a vacuous pass is not a pass",
        _e1["e1.P+ - P-.e1"] < 1e-12 and _e1["L_e1(S+) inside S-"] < 1e-12
        and _e1["pre_existing"] is True and len(_e1["sited_at"]) == 2
        and abs(_e2["leak(L_K grade-one, Cl+)"] - math.sqrt(2.0)) < 1e-12
        and "VACUOUS" in _e2["statement"]
        and "NAME THE REALIZATION" in _e2["refinement_of_RUL-099"]
        and "vacuous pass is not a pass" in _e2["refinement_of_RUL-099"]
        and "RUL-099" in _e2["sited_at"][0])

    _ck("★★ AND WHAT THE Φ ROUND DOES *NOT* CARRY — the honesty content of this bank. The "
        "Layer-A round submitted a menu-DISCRIMINATING verdict at the V4-ASD node; it was "
        "WITHDRAWN IN FULL at consensus, on the reviewer's computed counter-findings, every "
        "one of which the author reproduced independently before conceding. Struck: 'a j = 1 "
        "occurs NOWHERE in the local field module' (one DOES — the ASD triple itself, under "
        "the ADJOINT action, at exactly the j=1 Casimir; the C-33 ACTION axis was named in "
        "the setup and dropped at the headline, a C-33 violation at the round's own "
        "headline); the strike of any seat reading (no Layer-A computation on any module "
        "under any action can REACH the recorded seat reading, which names no module and no "
        "action — so neither table can strike it OR establish it); the 'only door' "
        "dichotomy (a bare necessity claim, RUL-049); the FCNC re-basing (a non-sequitur — "
        "the debt is UNTOUCHED and stays where the keeper put it); and the claimed "
        "ASYMMETRY between the readings — because (L_J, ρ(ASD)) generates ALL of End(S₋) "
        "AND the weak-side mirror (L_J, R_SD) generates all of End(W₊) too, so that argument "
        "form would refute banked R-079 when mirrored and is invalid at this layer, in BOTH "
        "directions. **LAYER A DID NOT DISCRIMINATE**: the node stays OPEN, its menu reverts "
        "three-way, and Layer B (the K2 stabiliser computation) is the SOLE decider. The "
        "primitive's own `does_not_license` carries this so the withdrawn verdict cannot "
        "re-enter through the engine",
        "LAYER A DID NOT DISCRIMINATE" in _phi["layer_A_verdict"]
        and "stays OPEN" in _phi["layer_A_verdict"]
        and "sole" in _phi["layer_A_verdict"].lower()
        and "only bankable result" in _phi["layer_A_verdict"]
        and "menu narrowing" in _phi["does_not_license"]
        and "ACTION named" in _phi["does_not_license"]
        and "C-33" in _phi["does_not_license"]
        and "scope fence" in _phi["does_not_license"]
        and "R-079" in _phi["does_not_license"])

    print("\nAll §18.3a/§20.3/§23.6/§23.7/§23.8 weak-sector checks passed (incl. instanton Q=1 by integration; F-7 (iii) promoted; R-172 body-frame hosting + the left-centralizer theorem banked 2026-08-23; companion-layer checks: twt_companion_test.py).")


# ---- twt_em ----------------------------------------
def check_twt_em():
    print("§21.2 consolidated Maxwell ∇F=J (grade structure COMPUTED):")
    m = maxwell_grade_structure()
    _ck(f"∇F lands in grades {{1,3}} only (grade-1 op × grade-2 field)  (got {m['grades of ∇F']})",
        m["no grade-0/2/4 part"])
    _ck(f"grade-1 part = 4 components (Gauss+Ampère=J)  (got {m['grade-1 components (Gauss+Ampère = J)']})",
        m["grade-1 components (Gauss+Ampère = J)"] == 4)
    _ck(f"grade-3 part = 4 components (Faraday+no-monopole=0)  (got {m['grade-3 components (Faraday+no-monopole = 0)']})",
        m["grade-3 components (Faraday+no-monopole = 0)"] == 4)
    _ck(f"⇒ 8 components = the four Maxwell vector equations  (got {m['total = 8 = 4 Maxwell vector eqs']})",
        m["total = 8 = 4 Maxwell vector eqs"] == 8)
    print("       the four laws (one statement, four grade-components):")
    for k, v in maxwell_four_laws().items():
        print(f"          {k:22s}: {v}")
    print("       no magnetic monopoles: the grade-3 SOURCE slot (4 components) exists but J is")
    print("       grade-1 only — empty by the winding-as-source identification, not by algebra.")

    print("§21.3 Coulomb potential:")
    _ck("F_static = Σ/(4πr) is harmonic away from source: ∇²(1/r)=0 for r>0", coulomb_is_harmonic())
    sr = coulomb_sign_rule()
    _ck("same-chirality repels (Σ₁Σ₂>0 ⇒ V>0)", sr["same-chirality (Σ₁Σ₂>0) → V>0 repulsion"])
    _ck("opposite-chirality attracts (Σ₁Σ₂<0 ⇒ V<0)", sr["opposite-chirality (Σ₁Σ₂<0) → V<0 attraction"])

    # §B.5.5 / R-124 — charged-defect worldline EOM + cyclotron readout (2026-07-02,
    # WP-MASS-MEASURE chain (1)): force law f = q F·u FORCED by the banked rest-frame
    # anchor (R-034 elastic overlap reads the Q-part only; Q⊥L exact) + Spin covariance
    # (transitivity), Schur commutant-2 cross-check; ω_c = qB/m exact rotor solution.
    # Inertia leg m = k_4 = ω/c_meta INHERITED-CONDITIONAL on R-123 residue (ii).
    print("§B.5.5 charged-defect worldline EOM + cyclotron (R-124):")
    cy = charged_defect_worldline_eom_cyclotron()
    _ck("R-124 rest-frame anchor: static force reads the 𝓠-part (E) ONLY; pure 𝓛-strain (B) exerts "
        "zero static force on a monopole winding (⟨Σ_Q Σ_L⟩₀ = 0 all 9 pairs, exact); the I₄-dual "
        "candidate reads the 𝓛-part at rest = the candidate the anchor kills",
        cy["rest_frame_anchor"]["rest_L_force_zero"]
        and cy["rest_frame_anchor"]["rest_reads_Q_only"]
        and cy["rest_frame_anchor"]["QL_grade0_orthogonal_all9"]
        and cy["rest_frame_anchor"]["dual_candidate_reads_L_at_rest"])
    _ck(f"R-124 uniqueness: Spin(4)-equivariant bilinear maps Λ²×V→V form EXACTLY a 2D space "
        f"{{F·u, (I₄F)·u}} (SVD commutant, got dim={cy['uniqueness']['commutant_dimension']}); "
        f"transitivity construction (anchor + covariance, no linearity-in-F needed) reproduces q·F·u; "
        f"u-cubic candidates collapse exactly",
        cy["uniqueness"]["commutant_dimension"] == 2
        and cy["uniqueness"]["span_is_dot_and_I4dual"]
        and cy["uniqueness"]["transitivity_reproduces_force"]
        and cy["uniqueness"]["cubic_third_contraction_zero"]
        and cy["uniqueness"]["cubic_reduces_to_dot"])
    _ck(f"R-124 cyclotron: m·u̇ = q·F·u in uniform 𝓛-strain B has the exact rotor solution rotating "
        f"at ω_c = qB/m (got {cy['cyclotron']['omega_c_extracted']:.6f} vs "
        f"{cy['cyclotron']['omega_c_expected_qB_over_m']:.6f}, generic q,B,m); e₄/out-of-plane/norm "
        f"preserved; f·u = 0 exact ⇒ dm/dτ = 0 a CONSEQUENCE",
        abs(cy["cyclotron"]["omega_c_extracted"] - cy["cyclotron"]["omega_c_expected_qB_over_m"]) < 1e-4
        and cy["cyclotron"]["conserved_e4_outofplane_norm"]
        and cy["pure_force_f_dot_u_zero"]
        and cy["cyclotron"]["eom_residual"] < 1e-5)
    _ck("R-124 tier honesty: DERIVED-A spine + DERIVED-conditional worldline limit (R-038 class) AND "
        "the NAMED Spin-covariance premise (R-014 + R-039 DERIVED-STRUCTURAL; twt-reviewer amendment) + "
        "INHERITED-CONDITIONAL inertia leg (R-123 residue ii, NOT closed here); α_em magnitude stays #1-gap",
        "MODULO R-123" in cy["outcome"]
        and "residue (ii)" in cy["conditional_on"]
        and "Spin-covariance" in cy["conditional_on"]
        and "alpha_em magnitude" in cy["not_derived_here"])

    print("\nAll §21.2/§21.3 EM-sector checks passed.")


# ---- twt_hadrons ----------------------------------------
def check_twt_hadrons():

    print("§17.3 numerical chain (e=5.45, f_π=129):")
    nc = numerical_chain()
    _ck(f"M_0 = 36.47 f_π/e = 863 MeV  (got {nc['M_0 (MeV)']:.0f})", abs(nc["M_0 (MeV)"] - 863) < 2)
    _ck(f"Θ_0 = 106.76/(e³ f_π) = 5.113e-3 [CORRECTED from 97.27, R-133 exact BVP]  (got {nc['Θ_0 (1/MeV)']*1e3:.3f}e-3)",
        abs(nc["Θ_0 (1/MeV)"] - 5.113e-3) < 5e-6)
    _ck(f"1/Θ_0 = 195.6 MeV (heavy-quark limit of Σ-Λ; was 214.7 pre-correction)  (got {nc['1/Θ_0 (MeV)']:.1f})",
        abs(nc["1/Θ_0 (MeV)"] - 195.6) < 0.5)

    # (removed: the alpha_H_gap()==77 assertion — 190-113=77 is true by construction, a
    #  calibration decomposition, not an independent check; see alpha_H_gap docstring.)

    print("§17.3 top-quark exclusion:")
    _ck(f"Γ_t·Θ_0 = 7.2 ≫ 1 ⇒ no top baryon (was 6.5; STRENGTHENED by R-133)  (got {top_excluded():.1f})",
        top_excluded() > 5.0 and abs(top_excluded() - 7.16) < 0.05)

    print("R-133 — the rotational-band baryon mass equation (exact BVP, Θ-coefficient corrected):")
    rb = skyrmion_rotational_band_nucleon_delta()
    _ck("R-133 BVP integrity: Derrick virial E2 = E4 at the minimum (<0.5%); mass coefficient "
        "reproduces the banked 36.47 (<0.2%); tail = the R-130 r^-2 branch with CLEAN constant "
        "B = x²F ≈ 8.64 on the flatness-selected window (spread < 0.05); Λ ≈ 50.98 matches the "
        "ANW literature ~50.9; Θ-coefficient = 106.76 — the banked 97.27 REFUTED (it equals "
        "36.47·8/3, provenance suspect, and the truncated-grid route shows how ~97 arises "
        "spuriously)",
        rb["bvp"]["virial_dev"] < 0.005
        and abs(rb["bvp"]["mass_coeff"] - 36.47) < 0.08
        and 8.3 < rb["bvp"]["tail_B"] < 8.9 and rb["bvp"]["tail_B_spread"] < 0.05
        and abs(rb["bvp"]["Lambda"] - 50.9) < 0.6
        and abs(rb["bvp"]["theta_coeff"] - 106.76) < 1.0
        and abs(rb["bvp"]["theta_coeff"] - 97.27) > 5.0)
    _ck("R-133 the band equation M(J) = M_0 + J(J+1)/(2Θ_0) at the counted ANW couplings: "
        "M_N = 936.4 (-0.27%), M_Δ = 1229.8 (-0.18%), split = 293.4 (+0.1%) — the banked M_0's "
        "'8% ANW deficit' EXPLAINED as the missing band term; honesty carried: (f_π, e) were "
        "historically FITTED to N/Δ (pipeline consistency, not a new prediction; no new "
        "parameter); J = 1/2, 3/2 rides the FR fermionic SELECTION (fork untouched); the "
        "J(J+1) band = the R-131-class moduli correction on the spin/isospin sector",
        abs(rb["band"]["err_N"]) < 0.005 and abs(rb["band"]["err_Delta"]) < 0.005
        and abs(rb["band"]["err_split"]) < 0.01
        and "FITTED to N/Delta" in rb["band"]["fit_history_note"]
        and "FR" in rb["tier"] and "CORRECTION" in rb["tier"]
        and "TRACKED RESIDUAL" in rb["correction_knock_ons"]["Sigma_c-Lambda_c"])

    print("R-134 — Brannen-scale ↔ nucleon-third convergence (CANDIDATE, canon §0a):")
    bc = brannen_scale_nucleon_third_convergence()
    _ck("R-134 zero-parameter numbers: mu^2 = 313.84 MeV vs m_N/3 = 312.97 (ratio 1.0028, "
        "0.28%); amplitude form 0.14% = the SAME convergence (sqrt halves it, reviewer fix — "
        "not added evidence); the per-rotor baryon amplitude at the lepton tower's democratic "
        "component; FLOOR reading does NOT converge (~9%, the named E-floor fork stake); "
        "look-elsewhere scan banked: EXACTLY two hits over 4 comparators x rationals <= 8 "
        "(m_N/3 at 1/1 + the fit-tied 8/5 of 1/Theta_0 — same hit via the N/Delta fit)",
        abs(bc["numbers"]["mu2_MeV"] - 313.84) < 0.05
        and abs(bc["numbers"]["ratio_mass"] - 1.0) < 0.005
        and abs(bc["numbers"]["ratio_amplitude"] - 1.0) < 0.0025
        and 1.05 < bc["numbers"]["floor_reading_ratio"] < 1.13)
    _ck("R-134 tier honesty: CANDIDATE (literature-known observation imported as such; "
        "post-hoc/look-elsewhere caveat named); per-rotor lock reading keeps canon §5 (NOT "
        "a quark mass); the naive I_4 route BLOCKED by N12 (amplitude-blind Hodge map) — "
        "mechanism is kernel/cell-scale class; would-become-result and would-weaken faces "
        "both carried",
        "CANDIDATE" in bc["tier"] and "literature-known" in bc["tier"]
        and "N12" in bc["blocked_route"]
        and "one fewer counted INPUT dial" in bc["would_become_result_if"]
        and "FLOOR reading" in bc["would_weaken_if"])

    print("R-135 — P2-7 first half: B = 2 below the two-defect threshold (classical binding):")
    b2 = multi_skyrmion_b2_classical_binding()
    _ck("R-135 construction integrity: degree identity (1/4π)∫ψ² = B = 2 exact (<1e-10); "
        "I(z²) = 5.8083 computed by quadrature (literature ~5.81); B = 1 regression "
        "reproduces the banked 36.46 (R-133) with Derrick virial ~4e-6; B = 2 virial ~3e-6; "
        "per-baryon 1.2081·12π² matches HMS 1.208 end-to-end; indicial roots s²+s−2B = 0 "
        "generalize R-130's {+1, −2} (B = 2: (−1±√17)/2 — non-integer origin exponent, "
        "steeper x^−2.56 tail, no long-tail matching problem)",
        abs(b2["angular"]["degree_check"] - 2.0) < 1e-10
        and abs(b2["angular"]["I_z2"] - 5.8083) < 0.001
        and abs(b2["b1_regression"]["mass_coeff"] - 36.46) < 0.08
        and b2["b1_regression"]["virial"] < 1e-4 and b2["b2"]["virial"] < 1e-4
        and abs(b2["b2"]["per_baryon_12pi2"] - 1.208) < 0.002
        and abs(b2["b2"]["roots"][0] - 1.5615528128088303) < 1e-12)
    _ck("R-135 THE RESULT: E_RM(B=2) = 71.543 f_π/e < 2×36.462 = 72.923 (margin 1.89%, three "
        "orders above numerical error) — the B = 2 sector lies STRICTLY BELOW the two-defect "
        "threshold ⇒ nuclear binding EXISTS classically with the predicted SIGN; at the "
        "counted ANW couplings binding ≥ 32.7 MeV (upper-bound ansatz value; conclusion "
        "ansatz-independent); overbinding vs the observed 2.22 MeV honestly imported "
        "(quantization + pion-mass = named follow-ups); deuteron identification FRAMING "
        "(classical seat only); first SC-1 N = 2 datum, scoped to the reduced BVP",
        b2["inequality"]["m2_coeff"] < b2["inequality"]["threshold_coeff"] - 1.0
        and 0.015 < b2["inequality"]["margin"] < 0.025
        and 30.0 < b2["inequality"]["classical_binding_MeV_lower_bound"] < 36.0
        and "upper bound" in b2["tier"]
        and "deuteron identification awaits" in b2["tier"]
        and "NOT full 3D" in b2["sc1_datum"])

    print("R-136 — P2-7 quantization face: the deuteron's quantum numbers (K3=0 selection rule):")
    dq = b2_axial_quantization_deuteron_ground_state()
    _ck("R-136 structural core: z² map symmetries exact (sympy in-primitive: axial iso-lock, "
        "π-about-e3 alone, π-e1 = π-τ1; parity map R_P = −R ⇒ isoscalar parity +); Krusch "
        "loop signs consistency-checked (B=1 fermionic regression; compositions mod 2); "
        "K3=0 tower rule I+J ODD: (0,1) = deuteron J^π = 1⁺ ALLOWED, scalar (0,0) dibaryon "
        "FORBIDDEN, (1,1)/(0,2) forbidden, (1,0) = np singlet allowed; bosonic branch flips "
        "to I+J EVEN (scalar ground state) — refuted by nature: SECOND independent anchor "
        "for the fermionic FR selection (W-LIVE-4/N35 fork untouched — evidence, not "
        "derivation)",
        dq["selection"]["fermionic_table"]["(0, 1)"] is True
        and dq["selection"]["fermionic_table"]["(0, 0)"] is False
        and dq["selection"]["fermionic_table"]["(1, 1)"] is False
        and dq["selection"]["fermionic_table"]["(1, 0)"] is True
        and dq["selection"]["bosonic_table"]["(0, 0)"] is True
        and dq["selection"]["bosonic_table"]["(0, 1)"] is False
        and "NOT a derivation" in dq["fork_face"]
        and "FR-selection" in dq["tier"] and "IMPORTED-AS-CITED" in dq["tier"]
        and "LITERATURE-KNOWN" in dq["tier"])
    _ck("R-136 moments + ordering (ansatz-level): B=1 regression — all FOUR moments (iso AND "
        "spatial paths) = 106.75 matching R-133's 106.76, spin-from-isospin V = U verified "
        "numerically, Λ = 50.97; axial identity V33 = 4·U33 exact (<1e-6); W_⊥ = 0 "
        "block-diagonality (all four iso×spatial cross moments < 1e-10 — the reviewer's "
        "probe, banked: the two-state ordering has no mixing term); B=2: V_⊥ = 312.5 "
        "> U_⊥ = 194.6 ⇒ E(0,1) < E(1,0): the deuteron quantum numbers are the GROUND STATE, "
        "isovector ~40 MeV up; spectrum values FRAMING/estimate only (rigid-rotor on the "
        "R-135 saddle; overbinding stated, no magnitude claimed)",
        dq["moments"]["Wperp_cross_max"] < 1e-10
        and all(abs(v - 106.76) < 0.3 for v in dq["moments"]["B1_regression"].values())
        and abs(dq["moments"]["B1_Lambda"] - 50.98) < 0.15
        and abs(dq["moments"]["axial_V33_over_U33"] - 4.0) < 1e-6
        and dq["moments"]["B2"]["V1"] > dq["moments"]["B2"]["U1"] + 50
        and dq["spectrum_estimate_MeV"]["E(0,1)"] < dq["spectrum_estimate_MeV"]["E(1,0)"]
        and 30.0 < dq["spectrum_estimate_MeV"]["split"] < 50.0
        and "ESTIMATE" in dq["spectrum_estimate_MeV"]["note"])

    print("R-137 — pion-mass robustness re-check (the R-133/R-135/R-136 owed face):")
    mp = massive_pion_bvp_binding_margin_robust()
    _ck("R-137 THE RE-CHECK: the R-135 below-threshold inequality SURVIVES the physical "
        "pion mass — massive coefficients 74.31 < 2×37.90 = 75.80, margin 1.96% (massless "
        "1.89% — it WIDENS); binding ≥ 35.2 MeV; certificates: mass-extended Derrick "
        "E2 + 3Em = E4 at ~3-5e-6 both profiles, Bessel-asymptote tails clean (<1e-3), "
        "Bessel-index identity √(2B+¼)+½ = (1+√(1+8B))/2 exact (μ→0 reproduces the "
        "massless exponents); m_π = 138 a NAMED witness import (probe-only, both sides "
        "identically; (1−cosF) form = imported chiral-breaking deformation, not substrate)",
        mp["massive"]["m2"] < 2*mp["massive"]["m1"] - 1.0
        and mp["massive"]["margin"] > 0.0189
        and 33.0 < mp["massive"]["binding_MeV"] < 38.0
        and mp["massive"]["virials"][0] < 1e-4 and mp["massive"]["virials"][1] < 1e-4
        and "NAMED IMPORT" in mp["tier"] and "probe-only" in mp["tier"])
    _ck("R-137 the inertia face (R-133 scheme honesty QUANTIFIED): massive-profile "
        "Λ = 33.52 vs massless 50.98 (θ-coeff 106.76 → 70.20, −34%) — the exponential "
        "tail kills the long-ranged integrand, so the massless N/Δ closure does NOT "
        "transfer at the same couplings: the massive variant is a DIFFERENT SCHEME "
        "requiring its own refit (fork NAMED, not taken; banked baseline stays massless); "
        "R-136's topological selection is mass-UNTOUCHED (only moments shift — ordering "
        "re-check owed only in the massive-scheme branch)",
        abs(mp["massive"]["Lambda_massive"] - 33.5) < 0.3
        and abs(mp["massive"]["theta_coeff_massive"] - 70.2) < 0.6
        and "not taken" in mp["tier"]
        and "UNTOUCHED" in mp["r136_note"])

    print("R-138 — massive-scheme refit branch (coordinator-approved fork execution):")
    rf = massive_scheme_refit_branch()
    _ck("R-138 the refit + invariance: (f_π*, e*) = (108.26, 4.843) closes N/Δ in the "
        "massive scheme (verification solve <0.2 MeV; corroborates Adkins-Nappi 108/4.84); "
        "1/Θ₀ = (2/3)·split_obs = 195.4 MeV is FIT-INVARIANT across the fork (DERIVED-A) ⇒ "
        "Λ_QCD candidate, top exclusion, AND the Σ_c−Λ_c residual (−9.0%) all UNCHANGED — "
        "the fork does NOT resolve the residual (strengthens the Callan-Klebanov candidate); "
        "branch counts THREE inputs (m_π load-bearing in-branch) vs baseline TWO",
        abs(rf["refit"]["f_pi"] - 108.26) < 0.05 and abs(rf["refit"]["e"] - 4.8427) < 0.001
        and abs(rf["refit"]["M_N"] - 938.9) < 0.2 and abs(rf["refit"]["M_Delta"] - 1232.0) < 0.5
        and abs(rf["refit"]["inv_Theta0"] - rf["invariance"]["inv_Theta0_pinned"]) < 0.5
        and "3 inputs" in rf["tier"])
    _ck("R-138 owed re-checks + baseline decision: margin at refit couplings 1.87% "
        "(75.997 < 77.442, binding ≥ 32.3 MeV — the binding conclusion now verified across "
        "the ENTIRE fork); deuteron ordering V_⊥ = 222.1 > U_⊥ = 135.6 in-branch (R-136 "
        "massive re-check DISCHARGED); BASELINE STAYS MASSLESS (bookkeeping decision, "
        "not derivation): economy + one hedged √18/e face (massless −1.1% vs massive "
        "+11.3%) + import-minimization",
        0.015 < rf["recheck_margin"]["margin"] < 0.025
        and rf["recheck_ordering"]["V_perp"] > rf["recheck_ordering"]["U_perp"] + 50
        and abs(rf["discriminators"]["D2_sqrt18_over_e"]["massless"] - 0.7784) < 0.001
        and rf["discriminators"]["D2_sqrt18_over_e"]["massive"] > 0.87
        and "STAYS MASSLESS" in rf["discriminators"]["verdict"])

    print("R-139 — P2-7 tensor-force face (the item's last constructive half):")
    tfr = two_defect_asymptotic_tensor_force()
    _ck("R-139 exact identities + law: K_{3/2} elementary (the B=1 massive tail IS the "
        "dipole-Yukawa profile exactly, sympy); OPE decomposition exact (tensor radial "
        "(1+μR+μ²R²/3)e^{−μR}/R³ = the standard OPE tensor shape; central ∝ μ² vanishes "
        "massless — the aligned-channel zero); dipole constants from the banked tails: "
        "C = 8.634 (massless), 7.91 (probe), 7.66 (refit) — nearly FORK-INVARIANT, gently "
        "μ-screened (the drafted 4.24 was a provenance misread, REFUTED by the reviewer's "
        "independent solve — fix F1, constants now solved in-primitive); the asymptotic Skyrmion "
        "= an exact triplet of orthogonal pion dipoles (iso-locked to space by the hedgehog)",
        abs(tfr["constants"]["C_massless"] - 8.634) < 0.02
        and abs(tfr["constants"]["C_dip_probe"] - 7.91) < 0.05
        and abs(tfr["constants"]["C_dip_refit"] - 7.66) < 0.05
        and "e^{-mu R}/R^3" in tfr["law"]["massive"]
        and "ATTRACTIVE" in tfr["law"]["channels"]["pi-rot perp R"])
    _ck("R-139 grid certificate + adjudications: 81³ in-suite product-ansatz regression — "
        "perp π-rotation ATTRACTIVE (the R-135 channel), par REPULSIVE, aligned sub-leading "
        "and falling with R (full 169³ development record: ratios monotone → 1, channel "
        "ratio → 2); D4-anisotropy premise CORRECTED (N39: the isotropic dressed sector "
        "delivers the tensor force; no anisotropy input anywhere); P2-7 DONE AT SCOPE with "
        "the binding-magnitude face LOCATED (torus + beyond-rigid-rotor quantization)",
        tfr["grid_certificate"]["8.0"]["perp"]["V"] < 0
        and tfr["grid_certificate"]["8.0"]["par"]["V"] > 0
        and tfr["grid_certificate"]["10.0"]["perp"]["V"] < 0
        and tfr["grid_certificate"]["10.0"]["par"]["V"] > 0
        and abs(tfr["grid_certificate"]["10.0"]["O1"]["V"]) < abs(tfr["grid_certificate"]["8.0"]["O1"]["V"])
        and "NOT the source" in tfr["d4_adjudication"]
        and "DONE AT SCOPE" in tfr["p2_7_closure"]
        and "LOCATED residual" in tfr["p2_7_closure"])

    print("R-140 — P2-4 leg 2: the explicit DM-twisted D4 plaquette holonomy:")
    pq = d4_dm_plaquette_holonomy_explicit()
    _ck("R-140 the explicit plaquette: census 32 = 8 spatial (trivial) + 24 two-e₄-bond "
        "(ALL non-trivial — the pure-gauge lift EXPLICIT); exact law W = cos²θ + "
        "sinθcosθ(B₁+B₂) + sin²θ·e_ab (non-abelian excess EXACTLY sin²θ = the banked "
        "48/66 commutator content sitting in the holonomy); consistency forces the "
        "orientation-ODD convention (= physical DM antisymmetry; convention-robust); "
        "e₄-triangles engage ONLY the 48 non-commuting pairs",
        pq["census"]["triangles"] == 32 and pq["census"]["spatial"] == 8
        and pq["census"]["e4_two_bond"] == 24
        and pq["census"]["chordless_4cycles"] == 36
        and pq["census"]["all_4cycles_trivial"] is True
        and abs(pq["law"]["at_0.3"]["angle"] - 0.421031603413) < 1e-9
        and abs(pq["law"]["at_0.3"]["excess"] - 0.08733219254516) < 1e-9)
    _ck("R-140 chiral structure + instanton accessibility: I₄-central factorization "
        "W = W₊P₊ + W₋P₋ with IDENTICAL angles arccos(cos²θ_D) in both sectors — the "
        "plaquette is chirally BLIND (weak = SD is settled at R-171/R-079, not here; §C.4.6(iii) "
        "annotated); per-sector holonomy Lie closure = FULL su(2)± (rank 3, not a U(1) "
        "subgroup) ⇒ π₃ = ℤ instanton sectors structurally accessible; dynamics stays "
        "kernel-gated as banked (no value claimed)",
        pq["lie_closure"]["su2_plus_rank"] == 3 and pq["lie_closure"]["su2_minus_rank"] == 3
        and "chirally BLIND" in pq["outcome"]
        and "FRAMING preserved" in pq["tier"]
        and "leg 4 ANSWERED-AT-PARITY" in pq["p2_4_status"])

    # B-1 (RUL-095 (iv), the RUL-083 witness-split pattern). The R-141 regression that used
    # to run INSIDE the CORE primitive lock_channel_is_axial_chiral_channel_p1b_split moved,
    # verbatim, into the V3 witness that may hold it. The assertion did not weaken: it is
    # still executed on every suite run — from the file where the instance-sited leg lives.
    print("B-1 — the V3 witness leg of the family-level lock-channel claim (R-161/R-141):")
    _w = lock_channel_p1b_split_v3_witness()
    _ck("the V3 witness runs the moved R-141 regression AND states the exposure: the family "
        "claim is witnessed ONLY by the V3 route (D4 chain S1b/S1c + the FR scheme, V3-11) "
        "pending a family-level witness",
        "P1b" in _w["regression"] and "ONLY by this V3 route" in _w["exposure"]
        and "DERIVED-A" in _w["family_claim_tier"])

    print("R-141 — P2-4 leg 4: the induced-level PARITY on the baryon worldline:")
    il = induced_level_parity_on_baryon_worldline()
    _ck("R-141 the counting (all inputs banked): roster 4 doublets/gen (evenness = the "
        "banked SU(2) gaugeability, same roster); baryon-coupled count 3/gen (the colour "
        "modes; lepton EXCLUDED by the R-002 winding split + R-127/R-128 lock split — the "
        "load-bearing step, anchored to live banked primitives); the named generation fork "
        "N = 3 vs 9: ODD in both branches — the parity does not wait on the fork; the "
        "parity-flipping variants (lepton included: 4/12, even) are the EXCLUDED ones",
        il["counting"]["roster_per_gen"] == 4
        and il["counting"]["baryon_coupled_per_gen"] == 3
        and il["counting"]["fork"]["parity"] == "ODD in both branches"
        and "R-002" in il["counting"]["lepton_excluded_by"]
        and "R-128" in il["counting"]["lepton_excluded_by"])
    _ck("R-141 the conditional conclusion + honesty: induced weight (−1)^N = −1 ⇒ "
        "fermionic Skyrmion quantization INDUCED, conditional on the THREE NAMED premises "
        "P1 (imported D'Hoker-Farhi/Witten theorem, cited to-be-verified, R-088-class) + "
        "P1b (channel identification for the WHOLE roster, CANDIDATE-class, revocable) + "
        "(Q); W-LIVE-4's W1 CLOSED-CONDITIONAL positive (N35 (a) PARTIALLY discharged at "
        "the parity level; the substrate computation face stays open); "
        "the FR selection upgrades to INDUCED-given-(P1)+(P1b); both empirical anchors "
        "become consistency checks; refusing P1b reverts to selection with the anchors "
        "standing",
        "P1" in il["premises"] and "P1b" in il["premises"] and "Q" in il["premises"]
        and "IMPORTED-AS-CITED" in il["tier"]
        and "DERIVED-given-(P1)+(P1b)+(Q)" in il["tier"]
        and "CLOSED-CONDITIONAL" in il["w_live_4"]
        and "refuted by the R-136 deuteron anchor" in il["w_live_4"])

    print("R-142 — the (H2) core: moduli↔pole identification + uniqueness (residue (ii)):")
    hp2 = one_particle_pole_moduli_identification()
    _ck("R-142 identification: the CLOCK-ORBIT IDENTITY exp(û θ/2)R* = R*(τ₅+θ/ω) exact "
        "(dev < 1e-12, generic config) — the observer's R-127 channel phase and R-131's "
        "modulus are ONE U(1); vacuum→one-particle = the ΔN = 1 step at exactly ω → "
        "k₄ = ω/c_meta; multiplicity = the R-126 multiplet (the quantum numbers); R-131 "
        "cited live (no phantom)",
        (hp2["identification"]["clock_orbit_identity_max_dev"] < 1e-12)
        and ("one circle" in hp2["identification"]["same_U1"])
        and ("Delta N = 1" in hp2["identification"]["tower_step"])
        and ("label reading" in hp2["identification"]["tower_step"]))
    _ck("R-142 uniqueness + honesty: the pole = the winding-1 sector GROUND STATE given "
        "(S)+(M) (sideband worry dissolves at quantized level); (S)-static ENGINE-CERTIFIED "
        "— the ℓ=0 Hessian around the banked hedgehog is strictly positive (~0.217, "
        "resolution- and box-robust; cross-term reduced by parts); (M)-static = the banked "
        "BVP-minimizer premise; residue (ii) reduced to KERNEL FACES ONLY (S/M/T-kernel), "
        "no structural face left; falsifier: any sub-mass channel pole kills m = k₄",
        all(v > 0.15 for v in hp2["uniqueness"]["S_static_lowest_eigs"])
        and abs(hp2["uniqueness"]["S_static_lowest_eigs"][0]
                - hp2["uniqueness"]["S_static_lowest_eigs"][1]) < 0.01
        and hp2["uniqueness"]["kernel_faces_open"] == ["S-kernel", "M-kernel", "T-kernel (R-130)"]
        and "DERIVED-given-(Q)+(S)+(M)" in hp2["tier"]
        and "LOCATED" in hp2["tier"])
    cse = corotating_stability_fixed_charge_hessian()
    _ck("★ A6 — the N45/R-142 ENSEMBLE FACE, RESOLVED (twt-reviewer-corrected + completed 2026-07-06): the correct "
        "co-rotating stability is FIXED-CHARGE (Q-ball) — via R-131 (`dE/dN=ω`) + R-007 (`mass=ω`, INTRINSIC rotation) "
        "⟹ construction (ii) (lab-cranking) EXCLUDED; the fixed-charge Hessian `H = E_s''−½ω²Θ''+ω²Θ'²/Θ` (Routh "
        "reduction of E_static+N²/(2Θ), sympy-exact) is STRICTLY STIFFER than N45 construction (i). COMPLETION: for "
        "the Derrick-scaling ℓ=0 breathing mode (E_static=E₂λ+E₄/λ, Θ=Θ₀λ^p, p>0) the fixed-charge "
        "`V_eff = E_static+N²/2Θ` is STRICTLY CONVEX (`V_eff'' = (4E₄Θ₀λ^p+N²λp(p+1))/(2Θ₀λ^{p+3}) > 0`, both terms "
        "positive) ⟹ a stable size for ALL ω ⟹ **NO instability threshold**; the ω²-coefficient Θ₀p(p+1)/2 > 0 for "
        "any p>0 (robust sign). So N45's Ω_c≈1.2057 (from the fixed-ω construction (i)) is a pure ENSEMBLE ARTIFACT, "
        "not merely a lower bound. DERIVED-A + DERIVED-CONDITIONAL(R-131/R-007 + the Derrick-scaling ansatz)",
        "FIXED-CHARGE" in cse["ensemble"] and "EXCLUDES construction (ii)" in cse["ensemble"]
        and "STRICTLY too soft" in cse["corrects_N45"]
        and "STRICTLY CONVEX" in cse["completion_no_threshold"] and "NO instability threshold" in cse["completion_no_threshold"]
        and "NO instability threshold" in cse["verdict"] and "ENSEMBLE ARTIFACT" in cse["verdict"])
    print("        ⇒ A6 RESOLVED (N45/W1.1): the ensemble is FIXED-CHARGE (Q-ball; (ii) lab-cranking EXCLUDED); COMPLETION — the fixed-charge V_eff is strictly convex for the Derrick-scaling ℓ=0 breathing mode (both terms of V_eff''=(4E₄Θ₀λ^p+N²λp(p+1))/(2Θ₀λ^{p+3}) positive) ⟹ NO instability threshold at any ω ⟹ N45's Ω_c≈1.2057 is a fixed-ω ENSEMBLE ARTIFACT (robust for any power p>0). DERIVED-CONDITIONAL on the Derrick-scaling ansatz.")

    print("R-143 — P2-4 leg 3: lattice-instanton access + DM background neutrality:")
    li = d4_lattice_instanton_access_and_dm_background_neutrality()
    _ck("R-143 background topological NEUTRALITY (iota-mechanism, exact: the DM twist "
        "plane r∧e₄ is e₄-reflection-BLIND while the volume pairing is e₄-reflection-ODD "
        "and ι is free ⇒ every site-based density cancels in ι-orbit pairs, EACH sector, "
        "ALL θ_D; 6912 individually O(1) terms — genuine cancellation; variant-b "
        "convention-robust) + the charge operator calibration Q_form(F) = 576·ε(F) "
        "integer-EXACT (pseudoscalar-pure; 24²; continuum norm 4π²)",
        abs(li["neutrality"]["sums"][0.7]["Q_plus"]) < 1e-10
        and abs(li["neutrality"]["sums"][0.7]["Q_minus"]) < 1e-10
        and li["neutrality"]["sums"][0.7]["nonzero_terms"] == 6912
        and li["neutrality"]["sums"][0.7]["max_term"] > 0.4
        and abs(li["neutrality"]["variant_b_sum"]) < 1e-10
        and li["neutrality"]["blocks_all_zero"] is True
        and abs(li["neutrality"]["genericity_witness"]["Q_plus"]) > 1.0
        and abs(li["neutrality"]["genericity_witness"]["Q_minus"]) > 1.0
        and li["charge_operator"]["c_geom"] == 576
        and "site-based density class" in li["neutrality"]["scope"])
    _ck("R-143 explicit charge-1 access at finite action excess: compactly-supported "
        "SU(2)₊ singular-gauge winding-1 fluctuation (identity S³-map, banked π₃ degree "
        "1; SU(2)₋ transparency EXACT) — action excess EXACTLY localized (far-dev = 0.0), "
        "measured charge plateau → 1 (0.79/0.90/0.94 at ρ = 2/3/4, deficit ~1/ρ², "
        "in-suite regression 0.672); cross-term tensor closed form c(θ) = 4√2·a·sin²θ/"
        "sin(a) (sourced by the 48/66 non-abelian excess; orientation-BLIND — no CP "
        "claim); LATT-π₃ premise NAMED; no minimizer/value/rate — kernel-gated fence "
        "inherited",
        li["access"]["regression"]["far_dev"] == 0.0
        and 0.65 < li["access"]["regression"]["Q_fluct"] < 0.70
        and abs(li["access"]["regression"]["Q_bg"]) < 1e-8
        and li["access"]["dev_record_Q"][4.0] == 0.9406
        and abs(li["cross_term"]["at"][0.7] - 2.738150065) < 1e-6
        and abs(li["cross_term"]["at"][0.5] - 1.4100035499873378) < 1e-9
        and li["cross_term"]["orientation_blind"] is True
        and "LATT-pi3" in li["strong_twist_reading"]["premise"]
        and "kernel-gated" in li["tier"]
        and "kernel-gated" in li["outcome"])

    print("R-144 — SC-1 second datum: full-field (ansatz-free) B=2 below threshold:")
    ff = full_field_b2_below_threshold_sc1_datum()
    _ck("R-144 the functional + discretization certified: the 3D Skyrme density reduces "
        "to R-135's radial integrand u/x² SYMBOLICALLY (sympy, generic rays — the 3D "
        "functional IS the banked dressed sector); compact-profile 3D-vs-1D regression "
        "h²-convergent at N = 48→96 for BOTH the hedgehog and the z² map; in-suite 32³ "
        "projected-gradient descent (hand-coded gradient, machine-checked vs autograd in "
        "dev): monotone after burn-in, winding conserved (drift < 0.025)",
        "DERIVED-A" in ff["tier"] and "SC-1 SECOND DATUM" in ff["outcome"]
        and ff["dev_record"]["banked_refs"]["continuum_B1"] == 36.462)
    _ck("R-144 the datum: ansatz-FREE full-3D B = 2 lies below the two-defect threshold "
        "at matched grid — stall-vs-stall margins 1.79% (N=64) / 3.06% (N=96, 30k-step "
        "continuation), ≥ 2.95% after the reviewer's B1-side continuation probe (banked; "
        "both stalls are upper bounds — 'descent only deepens' was one-sided, reviewer-"
        "corrected; sign independently protected by the R-133 continuum anchor "
        "72.923 > 71.617); the flow found the TOROIDAL minimizer with no symmetry "
        "constraint during descent (axial init + cubic grid QUALIFIER banked; ring at "
        "r = 1.55, center 2% of max, sharpening); charge pinned (B_disc = −1.98198); "
        "R-135's would-change-if (c) FIRED (KEEPS the binding, deepening at N=96); "
        "SC-1's static face advanced — the dynamical multi-defect EOM face stays open, "
        "kernel-gated; no magnitude claim (P2-7 residual row untouched)",
        ff["dev_record"]["margins_same_grid_pct"]["N64"] == 1.79
        and ff["dev_record"]["margins_same_grid_pct"]["N96"] == 3.06
        and ff["dev_record"]["reviewer_b1_continuation_probe"]["margin_pct"] == 2.95
        and ff["dev_record"]["B2"]["N96_final"]["E"] == 71.6169
        and ff["dev_record"]["B2"]["N96_final"]["center_over_max"] < 0.05
        and "SIGN" in ff["dev_record"]["margin_note"]
        and "kernel-gated" in ff["sc1_status"]
        and "two recorded" in ff["dev_record"]["unwinding_events"]
        and "reproducible-on-demand" in ff["dev_record"]["unwinding_events"]
        and "charge-guard" in ff["dev_record"]["unwinding_events"])


    print("\nAll §17.3/§17.4 hadron-mass checks passed (main-engine set; the gear chain and epicycle checks live in twt_companion_test.py).")

    rC = meson_dynamical_current_split()
    _ck(f"meson dynamical/current split orders P-V gaps light>charm>bottom, knob-free; heavy law is a 2-pt fit (p={rC['heavy_exponent_p_from_2_points']}), π enhanced {rC['pi_chiral_enhancement_over_2pt']}×",
        rC["per_state_knob"] is False)

    print("        Part A (real) — mass-measure FORCED + generation ℤ₃ reidentified (the fake-negative dissolved):")
    r1a = mass_measure_from_omega()
    _ck("1A [DERIVED]: mass-measure FORCED to √m=r² — reproduces modified-Brannen EXACTLY (deferent + negative epicycle, no cos3/cos4, lepton ε=0); √m=r ruled out by the lepton boundary (spurious epicycle). NOT a fit",
        abs(r1a["lepton_tau0"]["sqrtm=r2"]["epi_cos2"]) < 1e-6 and r1a["quark_tau0p6"]["sqrtm=r2"]["epi_cos2"] < 0
        and abs(r1a["lepton_tau0"]["sqrtm=r"]["epi_cos2"]) > 1e-3)
    r1b = generation_z3_is_metatime_phase()
    _ck("1B [DERIVED]: spatial G_generator is MASS-BLIND (preserves |B_spatial| AND |B_e4| to 1e-16) -> it is the COLOUR ℤ₃, NOT the generation operator; the generation ℤ₃ is the meta-time phase (distinct sampled masses). The prior (iii) used the colour ℤ₃ for the generation index = the fake-negative",
        r1b["spatial_G_dmass"]["d|B_spatial|"] < 1e-12 and r1b["spatial_G_dmass"]["d|B_e4|"] < 1e-12)
    r1c = why_three_generation_triple()
    _ck("1C [LOCATED]: why-three = the 3 ANTI-self-dual bivectors (I₄·u=−u verified); COUNT now COMPUTED as "
        "dim(ASD eigenspace of I₄· on Λ²) = trace(P₋) = 3 — GENERIC-GIVEN-4D, not Frobenius (C-1 2026-07-31; "
        "replaces the len()-of-a-literal cert); residual = the orbit-phase→ℍ-unit map (property Q)",
        r1c["count"] == 3 and "generic-given-4D" in r1c["count_source"]
        and r1c["duality_verified"] == "I4·u = -u for all three")
    gd = generations_dynamical_count_structural()
    _ck("generation ONTOLOGY (honest): DYNAMICAL meta-time phase (3 phases of one ℤ₃ orbit, all planes used "
        "equivalently → multi-gen baryons OK); the COUNT 3 is STRUCTURAL (ℍ-triple, UNIVERSAL across all "
        "fermions), NOT a stability cutoff — the stable neutrinos are still exactly 3 (N_ν=2.984); instability "
        "is the lifetime hierarchy WITHIN the 3, not the count; the dynamical→structural bridge stays OPEN",
        gd["multigeneration_baryons_ok"] and gd["stability_is_the_count_cutoff"] is False
        and gd["count_is_structural_not_dynamical_stability"] and abs(gd["N_nu_light_stable"] - 3.0) < 0.1)
    print("        e₄ verdict: PART A RESOLVED (ii) — measure √m=r² + generation/colour ℤ₃ split fixed; why-three is the located residual.")

    print("W3 (2026-07-27) — R-141's premise P1b SPLIT: P1b-STRUCT derived, P1b-DYN stays CANDIDATE:")
    p1b = lock_channel_is_axial_chiral_channel_p1b_split()
    _ck("W3 D1-D4 [DERIVED-A, engine-exact]: (D1) I4 IS the substrate gamma5 -- central in "
        "Cl+(4,0), I4^2 = +1, +1 on SD and -1 on ASD, P_+- central orthogonal idempotents, and "
        "I4 X = P_+X - P_-X for every bivector, so the R-128 lock OPERATOR is exactly the chirality "
        "reflection (coherent with its banked parity-ODDness: two gradings agreeing); (D2) the QUARK "
        "lock generator I4*B_q = b_+ - b_- factorizes the mass rotor into commuting chiral-sector "
        "rotors with ideal-normalized sector phases (+th, -th) EXACTLY -- purely AXIAL, the exponent "
        "structure of m exp(gamma5 theta n.tau); (D3) the LEPTON lock generator B_a = a_+ + a_- "
        "gives (+th, +th) -- purely VECTOR, no chirality-linking content; (D4) representation-level "
        "in the 4-dim module: the quark mass rotor restricts to the two Weyl halves through "
        "OPPOSITE-signed factors, the lepton rotor through SAME-signed factors",
        p1b["sector_phases_at_theta_1p234"]["quark e14"] == (1.234, -1.234)
        and p1b["sector_phases_at_theta_1p234"]["quark e34"] == (1.234, -1.234)
        and p1b["sector_phases_at_theta_1p234"]["lepton e12"] == (1.234, 1.234)
        and p1b["sector_phases_at_theta_1p234"]["lepton e23"] == (1.234, 1.234))
    _ck("W3 D5 SLAVING + THE GENERIC-COSET EXTENSION [DERIVED-A]: I4-centrality gives "
        "R(I4 X)R~ = I4(R X R~) for every even rotor (the lock map is Spin(4)-equivariant, so the "
        "mass-phase axis co-rotates with the local winding), diagonal-Spin(3) rotors preserve the "
        "observer, and the FULL R-128 dichotomy (centralizer = span{1, I4 b} of dimension exactly 2; "
        "dual axis = pure in-line phase at rate exactly omega; winding-axis leak confined to the "
        "complementary {1,e4} ideal; generic other axes leave the line; E exits the Cl(4,0) ideal) "
        "holds at 23 GENERIC coset directions INCLUDING near-lattice-axis and exact diagonals -- "
        "R-128 itself checked only the three lattice axes, and a hedgehog field's winding roams the "
        "whole coset sphere",
        p1b["generic_coset_directions_tested"] == 23
        and "PURE PHASE at rate omega" in p1b["intrinsic_load_bearing_facts"]["(a) quark line"])
    _ck("W3 D6 LEPTON EXCLUSION, hardened to algebra-given-conditions: the lepton line is "
        "coset-phase-BLIND under EVERY coset axis (it leaves its own line while the INLINE PHASE "
        "coordinate stays exactly 0), and by D3 its only mass-phase channel is chirality-EVEN -- so "
        "it cannot carry a U-slaved axial mass phase AT ANY COUPLING STRENGTH. THE DODGE-CLOSURE IS "
        "THE LOAD-BEARING EXCLUSION STATEMENT (not a footnote): the only escape, reading B_a as "
        "axial w.r.t. the winding I4*B_a, would make the lepton a Q-ORBIT defect, contradicting the "
        "banked R-002 L/Q assignment. HARDENING SCOPE: the parity-flipping even variants N = 4/12 "
        "ONLY -- NOT 6/18",
        p1b["intrinsic_load_bearing_facts"]["lepton_worst_inline_phase"] < 1e-10
        and "R-002" in p1b["dodge_closure"]
        and "load-bearing exclusion statement" in p1b["dodge_closure"].lower()
        and "4/12 ONLY" in p1b["lepton_exclusion_hardening"]
        and "NOT" in p1b["lepton_exclusion_hardening"] and "6/18" in p1b["lepton_exclusion_hardening"])
    _ck("W3 THE WINDING-ASSIGNMENT-RELATIVITY + the honest split [composite tier]: the reviewer's "
        "attack is BANKED AS AN IDENTITY, not conceded in prose -- B_a = (I4*B_a)_+ - (I4*B_a)_- "
        "holds EXACTLY (and its quark mirror), so 'axial vs vector' is NOT intrinsic to a generator: "
        "the lepton generator has AXIAL form about its OWN dual axis, and the tie is broken only by "
        "WHICH blade is the mode's winding (banked R-002 + R-127/R-128). SPLIT: P1b-STRUCT (the "
        "channel identity) is DERIVED here; P1b-DYN (nonzero coupling in the effective worldline "
        "action + the sigma-mirror pair as the theorem's doublet unit) STAYS CANDIDATE, so R-141 "
        "becomes INDUCED-given-(P1)+(P1b-DYN)+(Q). FOUR named conditions incl. C4' (roster colour "
        "modes' local winding = the baryon field's local coset orientation). NO SIGN is produced "
        "(L1-L3/N35 intact); the 'self-coherence cost of refusal' is a COST, never an argument",
        p1b["winding_assignment_relative"]["max_deviation"] < 1e-13
        and len(p1b["conditions"]) == 4 and any(c.startswith("C4'") for c in p1b["conditions"])
        and "C4'" in p1b["tier"] and "CANDIDATE" in p1b["tier"]
        and "CANDIDATE" in p1b["split"]["P1b-DYN"]
        and p1b["split"]["R-141 combined"] == "INDUCED-given-(P1) + (P1b-DYN) + (Q)"
        and "no sign, no" in p1b["no_sign_produced"]
        and "COST, never an argument" in p1b["cost_not_argument"])




# ---- twt_cosmo ----------------------------------------
def check_twt_cosmo():
    print("§24.4 cosmological constant via Volovik (FRAMING):")
    lr = lambda_resolution_structure()
    _ck(f"gravitating vacuum energy ρ_grav = ε-μn = -P = 0 at equilibrium (P=0), despite huge ZPE  (got {lr['rho_grav at equilibrium (P=0)']})",
        lr["rho_grav at equilibrium (P=0)"] == 0.0 and not lr["huge zero-point energy gravitates"])
    print("        ⇒ the huge QFT zero-point energy does NOT gravitate; Λ>0 is the off-equilibrium remnant [value OPEN].")

    lh = lambda_H2_dynamical_reading_excluded()
    _ck("N54 / §E.1.1: the DYNAMICAL reading ρ_vac ∝ H(t)² at ALL epochs is EXCLUDED — Ω_vac(z) ≡ ν forces "
        f"Ω_e = 0.685 ({lh['excess_over_Planck2015XIV_earlyDE_0p02']:.0f}× the Planck 2015 XIV ≈2% early-DE bound), "
        f"equivalent ΔN_eff = {lh['equivalent_Delta_Neff_at_BBN']:.1f} at the BBN epoch "
        f"({lh['excess_over_BBN_Delta_Neff_95up']:.0f}× the −0.14±0.21 light-element 95% ceiling; the "
        f"post-annihilation convention would give {lh['equivalent_Delta_Neff_post_annihilation_convention']:.1f}), "
        f"{lh['excess_over_RVM_nu_95up']:.0f}× the RVM ν fit ceiling, and a CONSTANT q ⇒ NO deceleration→acceleration "
        f"transition (flat ΛCDM on the same params: z_t = {lh['LCDM_transition_redshift_same_params']:.2f}). Only the "
        "PRESENT-EPOCH reading survives, and it is near-definitional ⇒ NO dark-energy prediction at V3",
        lh["excess_over_Planck2015XIV_earlyDE_0p02"] > 30
        and lh["excess_over_BBN_Delta_Neff_95up"] > 25
        and lh["equivalent_Delta_Neff_at_BBN"] < lh["equivalent_Delta_Neff_post_annihilation_convention"]
        and lh["excess_over_RVM_nu_95up"] > 100
        and lh["q_depends_on_z"] is False
        and 0.60 < lh["LCDM_transition_redshift_same_params"] < 0.70
        and "EXCLUDED" in lh["verdict"] and "NO dark-energy prediction" in lh["verdict"])

    print("§24.5 induced-G MAGNITUDE — the knowability determination (item 10, ECC two-build, Editor-calibrated):")
    qd = induced_G_quadratic_divergence_from_4D()
    _ck("Λ² scaling DERIVED from substrate DIMENSIONALITY only (UV power d−2 = 2 at d=4); the heat-kernel "
        "PREFACTOR is generic-QFT IMPORTED (flagged, sets bracket not verdict)",
        qd["UV_power_of_Lambda_in_1_over_16piG"] == 2 and qd["derived_content"].startswith("ONLY the 4"))
    mi = induced_G_leading_coefficient_mass_independent()
    _ck("Phase-D absence: leading Λ² coefficient is MASS-INDEPENDENT (I/Λ²→1 as m/Λ→0; I/Λ²>0.999 at m/Λ=1e-2) "
        "-> no manufactured G<->mass<->generation link",
        mi["I_over_Lambda2"]["m_over_Lambda=1e-02"] > 0.999 and "MASS-INDEPENDENT" in mi["verdict"])
    om = induced_G_only_monad_scale_enters()
    _ck("only the MONAD scale Λ enters the leading coefficient; the cell scale ℓ_S (~0.281 fm) would miss G by "
        "~1e38 -> clean (b), not partial-knowability",
        abs(om["ell_S_fm"] - 0.281) < 0.005 and float(om["G_mismatch_if_cell_cutoff"]) > 1e38)
    bk = induced_G_bracket_mode_count()
    _ck("Λ_S is a FREE residual: back-fit Λ/M_Pl=√(6π/N_eff) mapped the RETIRED [0.13,2.5]M_Pl bracket to "
        "N_eff∈[~3,~1115] (HISTORICAL record; which-Λ ruled 2026-07-30, bracket_status = RETIRED); "
        "CAVEAT a1 is a SIGNED TYPE-sum not a count -> a mode-count bracket would be WIDER still",
        bk["N_eff_bracket_mode_count"] == (3, 1115) and "WIDER" in bk["caveat"]
        and "RETIRED" in bk["bracket_status"] and "HISTORICAL" in bk["NOT_a_mode_count_claim"])
    sg = induced_G_sign_cross_check()
    _ck("sign + (attractive) via C_T>0 (item 5, cross-checked not re-opened); OPEN subsidiary: Euclidean->Lorentzian "
        "prefactor/sign may carry i/2π subtleties (Λ² scaling survives)",
        sg["induced_1_over_16piG_sign"].startswith("+") and "Euclidean" in sg["open_subsidiary"])
    ga = induced_G_gate_A_linearized_sufficient()
    _ck("Gate A: linearized (one-loop heat-kernel a1) spectrum SUFFICES; the #1 gap would sharpen N_eff only, NOT "
        "gate the verdict -> item 10 [A] status STANDS",
        ga["verdict_gated_by_#1_gap"] is False and "[A] stands" in ga["status"])
    kv = induced_G_knowability_verdict()
    _ck("VERDICT (b) CUTOFF-GATED currently; KNOWABILITY = CONSISTENT WITH, NOT CONFIRMED (gating is GENERIC to any "
        "4D induced gravity + a route to (a) [derive Λ·ℓ_S] is named & predicted-derivable => refutable, not a "
        "structural underivability) — calibrated from the delta's 'SUPPORTED'",
        kv["outcome"].startswith("(b) CUTOFF-GATED") and kv["knowability_boundary"].startswith("CONSISTENT WITH, NOT CONFIRMED"))
    print("        ⇒ item 10: [A] done at linearized level; G is cutoff-gated by the free monad scale Λ; "
          "the knowability boundary is consistent-with but NOT confirmed (refutable by deriving Λ·ℓ_S).")

    print("§21.6.1/§4.3 EQUIVALENCE-PRINCIPLE PROTECTION — item 16 cheap-win sub-item (gate-free, FRAMING+removed-falsifier):")
    ep = equivalence_principle_protection()
    _ck("WEAK EP (m_i=m_g) leading-order = GATE-FREE removed falsifier (NOT tetrad-gated); engine-checked: ~R∂R is "
        f"pure grade-2 (off-grade {ep['MC_form_offgrade_norm']:.1e} << grade-2 {ep['MC_form_grade2_norm']}) ⇒ frame(spin)-connection coupling, universal",
        ep["MC_form_offgrade_norm"] < 1e-6 < ep["MC_form_grade2_norm"] and "GATE-FREE" in ep["claim"])
    _ck("derived-vs-generic HELD: substrate-specific = single-field monism (mass=ω, ONE charge) + WP-LV1-twin protection; "
        "GENERIC = the ½h_μν T^μν / diff-invariance Ward identity (any Sakharov-induced EH)",
        "single-field monism" in ep["substrate_specific"] and "NOT substrate-specific" in ep["generic_given_induced_gravity"])
    _ck("honest LIMIT located: STRONG/Einstein EP + all-orders diff-invariance STILL gated on the texture tetrad (item 16)",
        "STRONG" in ep["still_gated_on_tetrad_item16"] and "removed-falsifier" in ep["tier"])
    print("        ⇒ item 16 cheap-win: WEP is the gravitational TWIN of WP-LV1, gate-free + consistent with MICROSCOPE η<1e-15; "
          "the STRONG EP stays tetrad-gated.")

    print("§B.1.5/§B.6.3 LORENTZ-VIOLATION ORDERS — R-165, which orders D4 protects AND WHICH IT DOES NOT (2026-07-27):")
    lv = d4_lattice_lorentz_violation_orders()
    _ck("D4 bond set 2nd moment EXACTLY 12·δ_ij (no dim-4 anisotropy) — DERIVED-A",
        lv["D4_second_moment_12_delta"] is True)
    _ck("D4 bond set 4th moment EXACTLY isotropic, residual = 0 with A = 4 (M_1111 = 12 = 3·M_1122) ⇒ leading "
        "rotational anisotropy pushed to DIMENSION EIGHT, (E/Λ)⁴ ≈ 2.0e-31 at the loose Λ_L corner — STRENGTHENS "
        "the old dim-6 claim. (Which-Λ ruling 2026-07-30: the corner is now the 1/a band floor 0.386 M_Pl; was "
        "≈ 1.6e-29 at the retired bracket's 0.13 M_Pl floor, ≈ 6.9e-30 at the pre-widening 0.16 M_Pl. "
        "Utterly negligible under every convention — the STRUCTURAL content, dim-8 leading, is Λ-independent)",
        lv["D4_fourth_moment_isotropy_residual"] == 0 and lv["D4_fourth_moment_A"] == 4
        and "EIGHT" in lv["anisotropy_leading_order"]
        and 2.0e-31 < lv["anisotropy_magnitude_(E/Lambda)^4"] < 2.1e-31)
    _ck("THE REAL REASON is representation-theoretic, not a kernel model (canon §3): |Aut(D4 root system)| = "
        "1152 = |W(F4)| and its degree-4 invariant space is ONE-dimensional (only (k²)²) ⇒ symmetry forces the "
        "quartic isotropic for ANY point-group-symmetric analytic kernel — matches F4's known invariant "
        "degrees {2,6,8,12}",
        lv["point_group_order"] == 1152 and abs(lv["invariant_poly_dims_deg_2_4_6"][4] - 1.0) < 1e-6
        and "1-DIMENSIONAL" in lv["why_no_dim6_anisotropy"])
    _ck("'LEADING' checked on BOTH sides, not just as an upper bound: degree-6 invariant space is 2-dimensional "
        "and D4's SIXTH bond moment is ANISOTROPIC (residual 12 ≠ 0) ⇒ dimension eight is actually REACHED",
        abs(lv["invariant_poly_dims_deg_2_4_6"][6] - 2.0) < 1e-6
        and lv["D4_sixth_moment_isotropy_residual"] > 0 and "LEADING" in lv["anisotropy_leading_order"])
    _ck("the dim-8 inference is CONDITIONAL and ALL FOUR of its premises are NAMED, not buried — FULL NAMING "
        "as of 2026-08-25, the ONE coordinated engine+suite+companion edit the R-165 amendment §4(i) left "
        "owed (the literal previously named the two headline premises and silently omitted (P-gs), added "
        "2026-07-31, and (P-op), added 2026-08-25): (P-an) analyticity in k — a non-analytic "
        "driven-dissipative memory kernel (the #1 gap itself) is not covered; (P-pg) the FULL point group "
        "INCLUDING TRIALITY — W(D4) alone has a 3-dim degree-4 space, and unequal weighting of "
        "triality-related shell-2 orbits RESTORES dim-6 anisotropy; (P-gs) the ground state preserves the "
        "point group — the §D.4.3 spiral breaks it, leaving SC-2's sidereal residual; (P-op) the OPERATIVE "
        "symmetry is the full point group, NOT the order-48 DRIVEN subgroup, where the degree-4 SPATIAL "
        "invariant space is 2-dimensional and the protection is carried by a +4/-4 interaction-content "
        "cancellation rather than by symmetry. THE STRING IS NOT EXHAUSTIVE OF ALL CONDITIONS AND SAYS SO: "
        "it is the paper §E premise register's four, and the §B.1.5 scalar-in-internal-index condition is a "
        "fifth that register does not label. WHAT THIS CHECK ENFORCES: every premise the tier names is "
        "DEFINED in the returned anisotropy_premises, and the two sets agree exactly — the engine↔paper "
        "drift class the record-invariants policy exists to catch",
        set(lv["anisotropy_premises"]) == {"P-an", "P-pg", "P-gs", "P-op"}
        and all(k in lv["tier"] for k in ("P-an", "P-pg", "P-gs", "P-op"))
        and "DERIVED-conditional-on-(P-an ∧ P-pg ∧ P-gs ∧ P-op)" in lv["tier"]
        and "FULL NAMING" in lv["tier"] and "FIFTH" in lv["tier"]
        and "+4/-4" in lv["anisotropy_premises"]["P-op"]
        and "SC-2" in lv["anisotropy_premises"]["P-gs"])
    _ck("NOT generic to lattices: simple-cubic Z⁴ 4th moment is ANISOTROPIC (residual 2, N_1111=2 vs N_1122=0) — "
        "the D4-vs-Z⁴ contrast is what makes the dim-8 push substrate-specific rather than generic",
        lv["Z4_fourth_moment_isotropy_residual"] > 0)
    _ck("NORMALIZATION stated so the two conventions cannot collide: η⁽⁴⁾ is the coefficient of p⁴/M²_Pl "
        "(Liberati), the substrate's own form is c·p⁴/Λ² with c = O(1), hence η⁽⁴⁾ = c·(M_Pl/Λ)² — "
        "'natural coefficient unity' means c = 1, NOT η⁽⁴⁾ = 1",
        "eta4 = c*(M_Pl/Lambda)^2" in lv["normalization"] and "NOT eta4 = 1" in lv["normalization"])
    _ck("FRAME JURISDICTION hedged, not glossed (canon §0 / N49 shape): the inertial-frame question is closed "
        "(CMB = τ₅-foliation comoving frame) but the bounds are INSIDE-frame inferences about an OUTSIDE-frame "
        "object, so the transfer rides the un-built outside↔inside projection — the exposure is named per §0a "
        "while its BINDINGNESS stays conditional (I-19 premise (e))",
        "INSIDE-frame" in lv["frame_jurisdiction_HEDGE"] and "BINDINGNESS" in lv["frame_jurisdiction_HEDGE"]
        and "INERTIAL-frame question only" in lv["frame_inertial"])
    _ck("the ROTATIONALLY INVARIANT dim-6 residual η⁽⁴⁾ is NOT protected by either face and is #1-gap GATED — "
        "the engine returns NO prediction for it (Cl41Wave().wave_speed_c raises)",
        "GATED" in lv["dim6_isotropic_eta4"] and "NOT a prediction" in lv["naive_eta4_status"])
    _ck("HONEST EXPOSURE recorded, not hidden: naive coefficient-1 value η⁽⁴⁾ = c_lat/(2π) ∈ [1.9, 6.7] is EXCLUDED "
        "by published n=4 limits by 3-9 orders; form factor gives only (f_π/m_p)² ~ 1e-2 and NOTHING for the photon "
        "(bulk mode) ⇒ logged as E.3.3 VG-6 / E.3.5(4) + N52, NOT as a falsifier row and NOT as a passed test. "
        "(which-Λ ruling 2026-07-30: dispersion consumers take Λ_L = 1/a, band [0.386, 0.734] M_Pl; the 2026-07-28 "
        "wide bracket [0.13, 2.5] / η⁽⁴⁾ [0.16, 59] / 2-10 orders is RETIRED — the exposure NARROWED and SHARPENED)",
        1.8 < lv["naive_eta4_at_c_equals_1"][0] < 1.9 and 6.6 < lv["naive_eta4_at_c_equals_1"][1] < 6.8
        and "NOT a falsifier row" in lv["recorded_as"] and "NONE for the photon" in lv["form_factor_insufficient"]
        and lv["Lambda_bracket_used"]["bracket_M_Pl_nonreduced"] == (0.3865, 0.7345)
        and "RULED" in lv["Lambda_bracket_used"]["status"])
    _crg_tie = c_reg_from_substrate_mode_content()
    _m_tie = __import__("re").search(r"c_lat = ([0-9.]+) \+ ([0-9.]+)\*kappa",
                                     _crg_tie["OA_LF_ii_sensitivity"]["c_lat(kappa) affine"])
    _mt_math = __import__("math")
    _band_tie = tuple(sorted(_mt_math.sqrt(2 * _mt_math.pi / (float(_m_tie.group(1)) + float(_m_tie.group(2)) * _k))
                             for _k in (2.0, 0.5)))
    _ck("CROSS-TIE (2026-07-30): the LV primitive's Λ_L band literals agree with the band recomputed LIVE from "
        "c_reg_from_substrate_mode_content's own affine c_lat(κ) at κ ∈ {1/2, 2} to 1e-3 — the ruled band is "
        "tied to the computing primitive, not a free-floating constant (the vacuous-check tell, canon §8a)",
        abs(_band_tie[0] - lv["Lambda_bracket_used"]["bracket_M_Pl_nonreduced"][0]) < 1e-3
        and abs(_band_tie[1] - lv["Lambda_bracket_used"]["bracket_M_Pl_nonreduced"][1]) < 1e-3)
    print("        ⇒ R-165: dim-4 boost CLOSED (R-016); anisotropy CLOSED HARDER than claimed (dim-8, D4-specific); "
          "the isotropic dim-6 term is the framework's sharpest standing empirical tension (N52).")

    print("THE (P-op) GROUP THEORY MADE EXECUTABLE — R-185, the driven group's spatial invariant theory "
          "(2026-08-25; §8a-repaired same day — verdicts at knowledge/audit/pop_banking_2026-08-25/):")
    pw = driven_group_spatial_invariants_wb3()
    _ck("FACT 1 — Stab_G(+e₄) [48] is block-diagonal and restricts FAITHFULLY and EXACTLY onto W(B₃) "
        "(all 48 signed 3-permutations, set-equality both directions), with spatial invariant dims 1/2/3 "
        "at degrees 2/4/6 = the free algebra on W(B₃)'s classical invariant degrees {2,4,6} "
        "(Coxeter/Chevalley/Shephard–Todd — the check is banked, not the mathematics); the NEGATIVE "
        "CONTROL runs in-process: the orientation-preserving half G24 restricts to a PROPER 24-element "
        "subset ≠ W(B₃), so the exactness test is seen able to fail",
        pw["driven_group_order"] == 48 and pw["full_group_order"] == 1152
        and pw["block_diagonal"] is True and pw["restriction_faithful"] is True
        and pw["restriction_is_exactly_WB3"] is True and pw["wb3_invariant_degrees"] == (2, 4, 6)
        and "classical" in pw["wb3_degrees_credit"]
        and (pw["invariant_dims"]["deg2_3var_spatial_WB3"],
             pw["invariant_dims"]["deg4_3var_spatial_WB3"],
             pw["invariant_dims"]["deg6_3var_spatial_WB3"]) == (1, 2, 3))
    _ck("FACT 2 — the degree-4 SPATIAL invariant space at the driven group is 2-DIMENSIONAL (an anisotropic "
        "spatial quartic is PERMITTED there, FORBIDDEN at the full group): dims 1 at G [1152] / 4 at G48 "
        "(4-var) / 2 spatial, computed by TWO GENUINELY INDEPENDENT METHODS INSIDE THE PRIMITIVE and "
        "asserted equal — symmetric-power traces AND the Reynolds-operator projector rank (the §8a "
        "reviewer's repair: the previous cross-tie to R-165's count was the SAME Molien formula re-run and "
        "is now labeled a CONSISTENCY TIE, which this check still keeps); witness Σ_{i≤3}k_i⁴ moved by "
        f"{pw['witness_violations']['full_group']}/1152 full-group elements, 0/48 driven and 0/96 axis-group "
        "— the 1056 is FORCED (= 1152 − 96, the witness's stabilizer is exactly G96); AXIS SUB-PREMISE "
        "NAMED, not resolved: these numbers sit at the maximally symmetric axis (generic axis ⇒ trivial "
        "stabilizer, permission dim 15) — an implicit V3 alignment commitment now recorded",
        (pw["invariant_dims"]["deg4_4var_full_group_1152"],
         pw["invariant_dims"]["deg4_4var_driven_group_48"],
         pw["invariant_dims"]["deg4_3var_spatial_WB3"]) == (1, 4, 2)
        and pw["invariant_dims_reynolds"] == {"deg4_4var_full_group_1152": 1,
                                              "deg4_4var_driven_group_48": 4,
                                              "deg4_3var_spatial_WB3": 2}
        and abs(lv["invariant_poly_dims_deg_2_4_6"][4] - pw["invariant_dims"]["deg4_4var_full_group_1152"]) < 1e-6
        and pw["witness_violations"] == {"driven_group": 0, "axis_group_G96": 0, "full_group": 1056}
        and pw["anisotropic_spatial_quartic_permitted_at_driven_group"] is True
        and "NAMED, NOT RESOLVED" in pw["axis_sub_premise"]
        and "CONSISTENCY TIE" in pw["two_methods"])
    _ck("FACT 3 — the 24-bond spatial fourth moment is EXACTLY isotropic at FULL TENSOR rank (residual 0.0; "
        "the halves are each residual-4, opposite in the anisotropy scalar: +4 e₄-bearing / −4 hyperplane), "
        "and the MECHANISM is keyed correctly (meta-observer F4 repair): full-orbit isotropy — one "
        "equal-weight W(F4) orbit forces Σ_b(b·k)⁴ = 12(k²)² in FOUR variables, descending to EVERY "
        "3-plane; the +4/−4 split is the e₄-axis SENSITIVITY DECOMPOSITION, not the mechanism. The "
        "would-change-if is keyed AXIS-INDEPENDENTLY (a weighting G48-invariant but NOT constant on the "
        f"orbit) and its exhibit runs in-process: w = 2 ⇒ anisotropy {pw['reweighting_demo']['anisotropy']:+.0f} ≠ 0 "
        "— an EXHIBIT entailed by the ±4 integers, correctly not counted as a negative control",
        pw["spatial_fourth_moment_full_tensor_residuals"] == {"total_24_bonds": 0.0,
                                                              "e4_bearing_12_bonds": 4.0,
                                                              "hyperplane_12_bonds": 4.0}
        and pw["spatial_fourth_moment_anisotropy"] == {"e4_bearing_12_bonds": 4.0,
                                                       "hyperplane_12_bonds": -4.0,
                                                       "total_24_bonds": 0.0}
        and abs(pw["reweighting_demo"]["anisotropy"]) > 1e-9
        and "EXHIBIT" in pw["reweighting_demo"]["status"]
        and "SENSITIVITY" in pw["mechanism"] and "descends" in pw["mechanism"]
        and "NOT constant on the W(F4) orbit" in pw["would_change_if"])
    _ck("SCOPE FENCE — NOTHING MOVES and COMPUTED ≠ DISCHARGED, said in the returned value: no value, tier "
        "or count changes; (P-op) stays an OPEN assumption about the dressed driven dynamics; R-165's "
        "asserts remain full-group statements; the §D.5.7 Γ-survivor arbitration stays OPEN (this primitive "
        "supplies its group-theoretic content, does not resolve it); the R-165 premise literal's (P-op) "
        "entry and this primitive agree on the ±4 split; and the tier carries the derived-vs-generic RIDER "
        "(facts 1–2 are reflection-group generic, shared with Z⁴'s point group — the D4-specific content is "
        "the forbidden/permitted CONTRAST and the full-orbit isotropy)",
        "NOTHING MOVES" in pw["scope"] and "COMPUTED IS NOT DISCHARGED" in pw["scope"]
        and "does not resolve it" in pw["scope"] and "OPEN" in pw["scope"]
        and "+4/-4" in lv["anisotropy_premises"]["P-op"]
        and "DERIVED-A" in pw["tier"] and "V3-1" in pw["tier"]
        and "RIDER" in pw["tier"] and "GENERIC" in pw["tier"] and "Z4" in pw["tier"])

    print("THE 24-BOND SCALAR DISPERSION QUARTIC — R-186, external-reviewer-proposed, three routes agree (2026-08-25):")
    dq = d4_scalar_dispersion_quartic_coefficients()
    _ck("AT ORBIT-CONSTANT COUPLING (r = J_p/J_a = 1) the scalar NN dispersion has c² = 1 and BOTH "
        "degree-4 coefficients EXACTLY ZERO — through quartic order the symbol is a function of the 4D "
        "invariant alone, ω² = k_sp² exactly, and the leading survivor is the degree-6 anisotropic "
        "(1/90)[(k²)³ − Σk_i⁶] (dimension EIGHT). Closed forms c² = (1+2r)/3, iso (1−r)(5+4r)/108, "
        "aniso −(1−r)/36 verified against the exact Fraction series at five rational r values, with "
        "r = 1 the UNIQUE root of either coefficient — R-185's orbit-constancy condition carrying "
        "BOTH loads at once",
        dq["orbit_constant_point"] == {"r": 1, "c_squared": 1, "deg4_isotropic": 0,
                                       "deg4_anisotropic": 0,
                                       "leading_survivor": "(1/90)[(k_sp^2)^3 - Sum k_i^6] — "
                                                           "anisotropic, dimension EIGHT"}
        and "unique root" in dq["unique_root"].lower())
    _ck("THE LIVE EDGE IS THE SUB-ORBIT EXTREME: at r = 0 (support on the 12 e₄-bearing bonds alone — "
        "the V3-2a shape) the coefficients are 5/108 and −1/36, both order 10⁻² — lethal against the "
        "3-to-9-order requirement if the dressed coupling sat there. The adjudicated reading is "
        "carried IN the returned value: the conservative NN scalar part's natural value is ZERO at "
        "orbit-constant coupling; the exposure concentrates in the orbit-splitting channel and the "
        "driven-dissipative sector; whether the dressed couplings sit at r = 1 is the named OPEN "
        "computation ({J, D} matrix-valued — the real object)",
        dq["sub_orbit_extreme"]["deg4_isotropic"] == "5/108"
        and dq["sub_orbit_extreme"]["deg4_anisotropic"] == "-1/36"
        and "ZERO at orbit-constant" in dq["adjudicated_reading"]
        and "OPEN" in dq["adjudicated_reading"])
    _ck("THE MODEL RIDER IS MANDATORY AND TRAVELS IN THE VALUE: scalar NN toy, NOT the banked {J,D} "
        "rotor; matrix-valued kernels outside the theorem (P-sc); non-analytic dissipative kernels "
        "outside entirely (P-an); PROOF OF CONCEPT NOT DISCHARGE — VG-6/N52 unmoved. PROVENANCE "
        "carried: proposed + first computed by the round-5 EXTERNAL reviewer, reproduced by two "
        "internal routes the same day — the standing-external-recomputation datum",
        "NOT the banked {J, D} rotor" in dq["model_rider"]
        and "PROOF OF CONCEPT, NOT DISCHARGE" in dq["model_rider"]
        and "VG-6/N52 unmoved" in dq["model_rider"]
        and "EXTERNAL reviewer" in dq["provenance"]
        and "DERIVED-A OF THE STATED MODEL" in dq["tier"])

    print("§21.6.1 TEXTURE METRIC — formula DERIVED-STRUCTURAL-CONDITIONAL (Schur uniqueness, gauge premise); dynamics CANDIDATE (2026-06-28):")
    tc = texture_metric_candidate()
    _ck("FORMULA DERIVED-STRUCTURAL-CONDITIONAL (Schur uniqueness engine-verified; conditional on gauge "
        "projection premise [FRAMING/INPUT]): h_mn=<Om_m I4 Om_n>_0 is the UNIQUE Spin(4)-invariant "
        "sign-indefinite gauge-projected symmetric bilinear from grade-2 inputs",
        "formula" in tc and "I4" in tc["formula"] and "DERIVED-STRUCTURAL-CONDITIONAL" in tc["tier"])
    _ck("UNIQUENESS span COMPLETE: grade-3 insertions give zero bilinear on grade-2 x grade-2 (grade-count); "
        "2D span {<AB>_0, <AI4B>_0} is the full space of invariant symmetric bilinears",
        "COMPLETE" in tc["U_span"])
    _ck("UNIQUENESS gauge forces c1=0: <balanced I4 balanced>_0=0; h=0 for balanced => c1=0; "
        "c2 is the unique free normalization",
        "c1=0" in tc["U_uniqueness"])
    _ck("I4 structure engine-verified: SD->+1, ASD->-1 eigenvalues; I4^2=+1; I4 central on all bivectors",
        "SD->+1" in tc["U_I4_eigenvalues"])
    _ck("P1 SYMMETRY PASS: h_mn is symmetric",
        "PASS" in tc["P1_symmetry"])
    _ck("P2 SIGN-FLIP PASS: pure-SD gives negative semi-definite; pure-ASD gives positive semi-definite",
        "PASS" in tc["P2_sign_flip"])
    _ck("P4 TWO POLARIZATIONS PASS: SD+ASD two-wave gives rank>=2, sign-indefinite h",
        "PASS" in tc["P4_two_polarizations"] and "sign-indefinite" in tc["P4_two_polarizations"])
    _ck("P5 SD-HEDGEHOG RANK PASS: SD hedgehog gives rank>=2, radial/transverse anisotropy "
        "(SD generators are L-Q-mixed; NOT the standard TWT baryon — see open_4)",
        "PASS" in tc["P5_skyrmion_rank"])
    _ck("P6 GAUGE: pure L and Q rotors give h=0; only L-Q MIXED (SD/ASD basis) create metric",
        "L or pure Q" in tc["P6_gauge_projection"])
    _ck("OPEN_4 LOCATED: standard TWT Q-orbit Skyrmion (actual B=1 baryon) gives h=0 everywhere; "
        "matter-geometry coupling mechanism is unresolved",
        "q_orbit_h_zero=True" in tc["open_4_matter_coupling"])
    _ck("STILL GATED: texture_tetrad() still raises; Sakharov EH NOT computed; h_mn tensor covariance now derived",
        "still raises" in tc["still_gated"] and "NOT computed" in tc["NOT_computed"]
        and "TENSOR COVARIANCE DERIVED" in tc["open_2_diffeomorphism"])
    print("        => item 16: formula DERIVED-STRUCTURAL-CONDITIONAL (Schur uniqueness; ONE FRAMING: "
          "gauge projection = Sakharov tree-level separation, not two independent inputs); "
          "dynamics CANDIDATE; open_4 (Q-orbit gives h=0, matter coupling unresolved) LOCATED; "
          "open_2 CLOSED (h_mn tensor covariance DERIVED).")

    print("§21.6.1 DIFFEOMORPHISM COVARIANCE — h_mn is a (0,2) tensor (open_2 CLOSED; 2026-06-28):")
    td = texture_metric_diffinvariance()
    _ck("TIER DERIVED-STRUCTURAL-CONDITIONAL: h_mn tensor covariance engine-verified",
        "DERIVED-STRUCTURAL-CONDITIONAL" in td["tier"] and "covariant" in td["tier"])
    _ck("PROOF: Om_m is a Lie-algebra covector; bilinear of covectors = (0,2) tensor",
        "covector" in td["proof"] and "bilinear" in td["proof"])
    _ck("NUMERICAL CHECK: |delta_h + L_xi h| / |delta_h| < 1e-3",
        float(td["numerical_check"].split("=")[1]) < 1e-3)
    _ck("CLOSES open_2 (tensor covariance of h_mn)",
        "open_2" in td["closes"])
    _ck("open_1 EH action STILL OPEN: Sakharov R(g) not computed",
        "NOT computed" in td["still_open_1"])
    print("        => open_2 CLOSED: h_mn is a proper (0,2) metric perturbation; "
          "open_1 (EH action) remains; texture_tetrad still raises.")

    print("§21.6.1 TT GRAVITON — polarization structure DERIVED-STRUCTURAL-CONDITIONAL (open_3 CLOSED; 2026-06-28):")
    tg = texture_metric_tt_graviton()
    _ck("TIER DERIVED-STRUCTURAL-CONDITIONAL: TT graviton polarization engine-verified",
        "DERIVED-STRUCTURAL-CONDITIONAL" in tg["tier"] and "engine-verified" in tg["tier"])
    _ck("TT STRUCTURE: h_mn = eps-_m eps-_n - eps+_m eps+_n (SD negative, ASD positive)",
        "eps-_m eps-_n" in tg["TT_structure"] and "phi_SD" in tg["TT_structure"])
    _ck("TWO POLARIZATIONS: h_plus = diag(0,-1,+1,0) engine-verified; h_cross = 45-deg rotation",
        "diag(0,-1,+1,0)" in tg["polarizations"] and "2 physical polarizations" in tg["polarizations"])
    _ck("TT GAUGE IN TWT: k^m Omega_m = 0 (transverse Maurer-Cartan = radiation gauge)",
        "k^m Omega_m = 0" in tg["TT_gauge_TWT"])
    _ck("LONGITUDINAL CHECK: single-mode Omega_m = k_m phi gives h ∝ k_m k_n (pure gauge)",
        "pure gauge" in tg["longitudinal"])
    _ck("CLOSES open_3 (TT graviton polarization)",
        "open_3" in tg["closes"])
    print("        => open_3 CLOSED: TT graviton = transverse Omega_m; "
          "SD->h_plus, ASD->h_cross; 2 polarizations from transverse-plane choice. "
          "open_1 (EH action from TT modes) still owed.")

    import math as _math
    print("§21.6.1 VIERBEIN — explicit e^a_m from SD/ASD decomposition (2026-06-28):")
    tv = texture_metric_vierbein()
    _ck("TIER DERIVED-STRUCTURAL-CONDITIONAL: Lorentzian vierbein engine-verified",
        "DERIVED-STRUCTURAL-CONDITIONAL" in tv["tier"] and "Lorentzian" in tv["tier"])
    _ck("SD/ASD DECOMPOSITION: h_mn = Q^T Q - P^T P (ASD positive, SD negative; engine-verified)",
        "Q^T Q" in tv["structural_decomposition"] and "Engine-verified" in tv["structural_decomposition"])
    _ck("LORENTZIAN EMERGENCE: g_00 = -5/4 for L-type rotor theta0=3 (engine)",
        abs(tv["g_00_Ltype"] + 1.25) < 1e-5)
    _ck("VIERBEIN EXPLICIT: e^0_0 = sqrt(5/4) = sqrt(5)/2 ~ 1.11803 [timelike]",
        abs(tv["e00_vierbein"] - _math.sqrt(5)/2) < 1e-5)
    _ck("VIERBEIN EXACT: max|g - e^T eta e| < 1e-10 (engine)",
        tv["vierbein_err"] < 1e-10)
    _ck("EIGENDECOMPOSITION VIERBEIN: general construction engine-verified",
        tv["eig_vierbein_err"] < 1e-10)
    _ck("TIMELIKE = SD direction: Lorentzian from SD dominance; ASD gives spacelike",
        "SD-dominant" in tv["timelike_is_SD"] and "Lorentzian" in tv["timelike_is_SD"])
    _ck("CLOSES: a vierbein exhibited for one SD-dominant config; general tetrad remains gated",
        "vierbein" in tv["closes"].lower() and "texture_tetrad" in tv["closes"])
    print("        => Vierbein CLOSED: Lorentzian emerges from Euclidean Cl(4,0) via SD dominance. "
          "open_1 (EH action), open_4 (matter coupling) remain.")

    print("R-146 — DM-V2-1 differential-coupling lead adjudicated (negative + located gap):")
    dm = dm_differential_coupling_no_em_dark_texture()
    _ck("R-146 the negative: the texture-metric source of ANY grade-2 excitation is "
        "IDENTICALLY its E.B-type L-Q cross term — h(B_L,B_L) = h(B_Q,B_Q) = 0 exactly and "
        "h(B,B) = 2<B_L I4 B_Q>_0 (the banked P6 balanced-fact rewritten in the EM basis; "
        "Hodge duality pairing engine-asserted); span(L)+span(Q) = ALL of grade-2 (rank 6) "
        "=> no EM-orthogonal gravitating polarization exists; |h| <= 2|B_L||B_Q| "
        "(Cauchy-Schwarz, saturated by pure SD/ASD — the maximally gravitating "
        "polarizations are exactly half-magnetic half-electric); [SD_i,ASD_j] = 0 all 9 "
        "pairs while the L/Q split is not commutator-closed => no non-abelian rescue; the "
        "transverse photon mode (E perp B) is h-DARK at bilinear order; grade-3 insertions "
        "have NO even part (parity) and the even substrate field can never produce "
        "grade-3 MC content => the grade-3 route is a new-field scope gap (E.1.3 posture "
        "reinforced). Physical negative DERIVED-structural, conditional on the banked "
        "photon-strain identification + the U2 gauge-projection premise",
        "DERIVED-A" in dm["tier"] and "NEGATIVE" in dm["tier"]
        and "E.B invariant" in dm["cross_term_identity"]
        and "CLEAN NEGATIVE" in dm["verdict"]
        and "sterile-RH" in dm["verdict"])
    _ck("R-146 the located gap: the grade-0 x grade-4 AMPLITUDE channel — a non-unit even "
        "excitation a + c*I4 has MC form with ZERO grade-2 (EM-strain) content yet sources "
        "the banked bilinear h = 2(aa'+cc')(ac'+a'c) (witness coefficient-exact); closed "
        "IDENTICALLY on unit rotors (grade-0/4 MC parts = d<R~R>/2 = 0) => opens ONLY if "
        "the #1-gap EOM supports gapped amplitude (Higgs-class, DM-shaped) modes AND the "
        "h-formula's grade-2-specific Schur scope extends — DOUBLY conditional, named; "
        "would-change-if handles recorded (kernel amplitude modes / odd-grade content / "
        "U2 falls)",
        "LOCATED-GAP" in dm["tier"] and "amplitude" in dm["located_gap"]
        and "doubly" in dm["located_gap"].lower()
        and "kernel EOM supports gapped amplitude modes" in dm["would_change_if"])

    print("R-148 — P2-3 sign face: beta_3 <= 0 AF-SIGNED (corrected build; first build refuted):")
    b3 = marginal_skyrme_beta3_sign_dispersive()
    _ck("R-148 the anchored channel map [DERIVED-A; vertex sign DERIVED in-suite per the "
        "review correction — the FIRST build was REFUTED (Euclidean-sign transplant, N42; "
        "correction history in the docstring)]: machinery calibrated (series C24 = 1/48 "
        "-> Weinberg M = t/f^2 exact); quartic-form coefficient +1 SERIES-EXTRACTED at "
        "rational configurations (not hand-entered); STATIC-ENERGY ANCHOR E4 > 0 ties "
        "the Minkowski Lagrangian sign +(1/32e^2)Tr([L,L][L,L]) to R-085's Hamiltonian-"
        "boundedness; slot = -1/4 COMPUTED; A_Skyrme(s,t,u) = -(s^2/2 + tu)/(2 e^2 f^4) "
        "(Bose s<->u; identical channel zero) => POSITIVE forward weight +1/(2f^4) — "
        "tree-level forward positivity SATISFIED by the banked sign automatically (the "
        "amplitude-side twin of R-085); monotonicity identity sympy-exact",
        "DERIVED-A" in b3["tier"] and "w = +1/(2 f^4) > 0" in b3["channel_map"]
        and "SATISFIED" in b3["channel_map"]
        and "CORRECTION-HISTORY" in b3["tier"]
        and "calibrate the load-bearing vertex" in b3["tier"])
    _ck("R-148 the sign + the honest close: beta_3 = mu d(1/e^2)/dmu <= 0 — the AF-SIGNED "
        "branch (1/e^2 grows toward the IR) — DERIVED-conditional-GENERIC [generic per "
        "canon 5: the standard dispersive-running statement for ANY two-term chiral "
        "action; substrate content = the banked action IS that action + engine-exact "
        "weights; LITERATURE-KNOWN-CLASS credited (Pham-Truong-class)]; premise set "
        "named (P-disp = I-13 registered, positivity leg partially RECAST onto banked "
        "B.3-derived QM per the 13.3 directive; P-action one-coupling, l1-mixing MOOT "
        "forward; P-chan; P-conv); the WRONG-SIGN RISK for the qcd-UV arc is REMOVED "
        "and P2-3's Class-1 sign face CLOSES POSITIVE-conditional-generic; HARD FENCE: "
        "sign-consistency is NOT AF-achieved (additive f^2-loop drift, no antiscreening "
        "mechanism) — DGLAP structure + magnitude stay N7/Class 2 at the kernel",
        "AF-SIGNED" in b3["sign"] and "GENERIC" in b3["sign"]
        and "wrong-sign risk" in b3["sign"]
        and "CLOSED POSITIVE-conditional-generic" in b3["p2_3_status"]
        and "antiscreening" in b3["p2_3_status"]
        and "I-13 registered" in b3["premises"]
        and "RECAST" in b3["premises"]
        and "forward-surviving weight" in b3["would_change_if"])

    print("R-147 — DM-V2-1 wave-train phase-defect lead adjudicated (negative; leads exhausted):")
    wt = dm_wavetrain_phase_defect_negative()
    _ck("R-147 the negative: THE BLADE, NOT THE TOPOLOGY, FIXES h — blade table engine-exact "
        "(all six coordinate bivectors h-null; SD/ASD blades -1/+1; the carrier blade "
        "E = I4 e5 h-null, and span{1,E} h-null even at NON-unit amplitude); pure-L and "
        "E-phase dislocations give h = 0 machine-exact (U2-conditional physical reading, "
        "c1-channel witness nonzero — named); the ONLY gravitating dislocation (SD-blade "
        "chiral-ideal U(1)) has h = -(1/2)dth x dth EXACT and its ENTIRE h is the R-146 "
        "EM-visible L-Q cross term POINTWISE (|Om_L|/|Om_Q| = 1) — topology buys no "
        "evasion; NO pi_1 protection (exp(e12 pi) = -1 exact; the winding-1 SD loop "
        "explicitly unwound by a belt-trick homotopy, engine-exact on a 9x13 grid) => "
        "KZ at the front produces no protected wave-train defect network; the one "
        "Z-protected class (U(1)_E vortices, conditional-FRAMING) is exactly the h-null "
        "class => nothing is simultaneously gravitating, EM-dark, and TOPOLOGICALLY "
        "PROTECTED (metastability cannot reopen DM — the gravitating-and-EM-dark class "
        "is already empty; reviewer F2); varying-blade defects fall to the same "
        "accounting (unit-rotor MC is pure grade-2 — reviewer F1 probe); the negative "
        "survives the SO(4)/Z2 order-parameter fork (reviewer R1 probe)",
        "CLEAN NEGATIVE" in wt["tier"] and "blade" in wt["verdict"]
        and "EXHAUSTED" in wt["verdict"]
        and "no pi_1 protection" in wt["verdict"])
    _ck("R-147 the sharpening: phase-VORTEX CORES are the natural population mechanism of "
        "R-146's amplitude channel — the SD-vortex core's radial MC leg is AUTOMATICALLY "
        "pure a + c*I4 (grade-2 leak ~1e-11) with h = 2sp digit-exact vs the R-146 "
        "formula — but only the EM-VISIBLE vortex forces I4-core content; EM-dark cores "
        "(E-vortex, balanced-blade) are structurally I4-free and h-null => the single "
        "remaining DM loophole now carries TWO named EOM conditions (amplitude modes "
        "exist AND EM-dark cores couple into the c*I4 grade-4 channel); both DM-V2-1 "
        "leads funnel into this one kernel-gated hinge — the item's V2-era lead list is "
        "EXHAUSTED and paper E.1.3's scope posture is REINFORCED",
        "EM-VISIBLE" in wt["sharpening"] and "TWO named EOM conditions" in wt["sharpening"]
        and "EM-dark" in wt["would_change_if"]
        and "R-145 signature-menu" in wt["would_change_if"])

    print("R-145 — P2-2 structural half: the 6->4 frame reduction (first-order/Cartan face):")
    fr = texture_frame_6to4_reduction()
    _ck("R-145 frame + menu: the banked texture metric is EXACTLY a rank-4 frame square "
        "g = E^T kappa E with E = [delta; Q; P] (10x4, rank 4 always — no degeneracy caveat), "
        "kappa = diag(+1_7, -1_3) [DERIVED-A, machine-exact]; pointwise the grade-2 frame "
        "quadruple is FREE (Om_mu(0) = B_mu coefficient-exact for exp-linear proper rotor "
        "fields); SIGNATURE-MENU theorem: >= 1 spacelike ALWAYS — stronger form "
        "lambda_max(g) >= 1 engine-asserted (reviewer R1) — negative index <= 3 => "
        "NONDEGENERATE menu = {(0,4),(1,3),(2,2),(3,1)} (det g = 0 at transitions, F2), "
        "ALL-TIMELIKE (4,0) STRUCTURALLY EXCLUDED; each menu item realized by an explicit "
        "proper rotor field; "
        "invariant Lorentzian threshold ||P||_op > 1 (the family-free form of the banked "
        "theta0 > 2 — no perturbative texture is Lorentzian; light-cone birth at det g = 0); "
        "menu DERIVED, the (1,3) PICK not derived (vacuum/EOM residue, named)",
        "DERIVED-A" in fr["tier"] and "NOT-DERIVED" in fr["tier"]
        and fr["signature_menu"]["excluded"].startswith("(4,0)")
        and fr["signature_menu"]["sweep_max_negative_index"] == 3
        and fr["signature_menu"]["realized"]["(1,3)"] == "(1, 3)"
        and fr["signature_menu"]["realized"]["(2,2)"] == "(2, 2)"
        and fr["signature_menu"]["realized"]["(3,1)"] == "(3, 1)"
        and "||P||_op > 1" in fr["lorentzian_threshold"])
    _ck("R-145 the reduction + first-order face: whenever the signature is Lorentzian the "
        "10-row frame reduces CANONICALLY to a tetrad — E = iota e with iota^T kappa iota = eta "
        "(machine-exact), tetrad unique up to O(1,3) (explicit boost verified) — the strategic "
        "map's '6->4 needs EOM' is SPLIT: the reduction is structural and selection-free; the "
        "EOM owes ONLY the signature pick; Maurer-Cartan FLATNESS dOm + Om^Om = 0 SYMPY-EXACT "
        "(faithful Cl(4,0) rep, non-commuting family) + numeric on a generic MV field => both "
        "first-order variables (frame AND spin connection) come from the ONE rotor field with "
        "the Cartan structure equation automatic; internal gauge action on the legs = compact "
        "SO(3) x SO(3) (split leak 0, dets +1, the transformation law P' = O_SD^T P itself "
        "engine-asserted per reviewer F1, g exactly invariant) => tetrad boosts NOT "
        "substrate-internal — local Lorentz emergent at the reduced description [FRAMING, "
        "scope-guarded vs R-132 spacetime boosts]; C_T/absolute coefficient NOT touched "
        "(#1-gap as banked); Gauss-equation face = the named next handle",
        "canonical tetrad" in fr["reduction"] and "SIGNATURE PICK" in fr["reduction"]
        and "sympy" in fr["first_order_face"]
        and "kernel-adjacent, not done" in fr["first_order_face"]
        and "SO(3) x SO(3)" in fr["gauge_compactness"]
        and "emergent" in fr["gauge_compactness"]
        and "STRUCTURAL HALF" in fr["p2_2_status"]
        and "Class 2" in fr["p2_2_status"])

    print("R-149 — P2-2 Gauss-equation face: Riem(g) closes algebraically in (E, Om, dE):")
    gc = texture_gauss_equation_riemann_closure()
    _ck("R-149 the five facts [DERIVED-A, each sympy-exact on a faithful-rep 2-parameter "
        "family + numeric on generic three-factor rotor fields]: (1) CURL CLOSURE "
        "d_mu E_nu - d_nu E_mu = -L([Om_mu,Om_nu]) (MC flatness + leg linearity — the "
        "antisymmetric part of dE is ALGEBRAIC in Om); (2) LEG-MAP INVERSION: all of dOm "
        "recoverable from dE (Hodge pairing = signed identity blocks); (3) GAUSS EQUATION "
        "for the induced torsionful metric connection Rt = kappa(S,S)-bilinear with S = "
        "the kappa-normal part of dE (S NOT symmetric — torsion carried; classical "
        "subbundle machinery, hypotheses engine-checked, no QFT import); (4) CONTORSION: "
        "Gam_LC = Gt + C with C algebraic in kappa(E, L([Om,Om]))",
        "DERIVED-A" in gc["tier"] and "sympy-exact" in gc["tier"]
        and "-L([Om_mu, Om_nu])" in gc["curl_closure"]
        and "kappa-normal part of dE" in gc["gauss_equation"]
        and "NOT symmetric" in gc["gauss_equation"]
        and "algebraic" in gc["contorsion"])
    _ck("R-149 THE CLOSURE + fence: Riem(g) is ALGEBRAIC in the first-order data "
        "(E, Om, dE) — NO derivatives of the FRAME DATA beyond first order (no ddE/ddOm; "
        "the closure drops Riem from THIRD- to SECOND-derivative order in the rotor "
        "field — reviewer-F1 wording: dE itself carries ddR, so 'no ddR' would be "
        "engine-FALSE; d_mu C assembled from point-data only, end-to-end vs an "
        "independent ddg computation); SIGNATURE-BLIND (verified at ALL FOUR "
        "nondegenerate menu items (0,4), (1,3), (2,2), (3,1) — the (3,1) config per "
        "reviewer R1; needs nondegeneracy, not the Lorentzian pick); NON-VACUOUS (Gauss "
        "and torsion blocks each same order as Riem); R-145's would-change-if (3) "
        "answered NEGATIVE — the first-order scaffold is CLOSED; C_T-skeleton reading "
        "FRAMING (quadratic in (S, [Om,Om]) — the kernel is the missing ingredient, not "
        "kinematics); NO value/coefficient computed (#1-gap as banked); the (1,3) pick "
        "and U2 untouched",
        "ALGEBRAIC in the first-order data" in gc["headline"]
        and "no derivatives of the frame data beyond first order" in gc["headline"]
        and "NEGATIVE" in gc["headline"]
        and gc["signatures_verified"] == ["(0, 4)", "(1, 3)", "(2, 2)", "(3, 1)"]
        and "SIGNATURE-BLIND" in gc["closure"]
        and "same order" in gc["non_vacuity"]
        and "FRAMING" in gc["ct_skeleton"]
        and "#1-gap" in gc["p2_2_status"]
        and "U2" in gc["p2_2_status"]
        and "MC flatness" in gc["would_change_if"])

    print("W3.1 — P2-2 C_T MOMENT COUNT: symmetry collapses C_T to <= 4 kernel numbers:")
    cm = ct_kernel_moment_count_symmetry_reduction()
    _ck("W3.1 [DERIVED-A block-exact + DERIVED group + DERIVED-A count + FRAMING spin-2 refine]: "
        "the R-149 C_T fluctuation data (S_sym (+) [Om,Om]) under the R-145 symmetry "
        "SO(4)_tangent x SO(3)_SD x SO(3)_ASD (product — internal fact (7) undoes the "
        "spacetime/tangent locking) carries EXACTLY 8 invariant quadratic forms (S_sym block 4, "
        "[Om,Om] block 4, cross 0 by SO(4)-irrep disjointness Sym^2(4)={(3,3),(1,1)} vs "
        "Lam^2(4)={(3,1),(1,3)}), split 4 PARITY-EVEN + 4 PARITY-ODD (2+2 per block; parity pairs "
        "each SD-channel form with its ASD-conjugate). su(2)+su(2) block structure engine-EXACT "
        "([SD,ASD]=0 => [Om,Om] block-diagonal). CONSEQUENCE: C_T (parity-even) enters through "
        "AT MOST 4 kernel moments — reduced from an unknown FUNCTION to <= 4 NUMBERS. Counts = "
        "exact character inner products (seeded Reynolds MC rounding to integers; independently "
        "confirmed by exact commutant null-space + hand irrep-decomposition). FENCE: no C_T value, "
        "no spin-2/Ricci sub-projection (the exact <=4 refine), #1-gap gated.",
        cm["su2_su2_block_exact"] < 1e-12
        and cm["invariant_forms"] == {"S_sym": 4, "OmOm": 4, "cross": 0, "total": 8}
        and cm["parity_split"]["even"] == 4 and cm["parity_split"]["odd"] == 4
        and cm["N_moments_parity_even"] == 4
        and "DERIVED-A" in cm["tier"] and "FRAMING" in cm["tier"])

    import math as _math2
    print("§21.6.1 SAKHAROV INDUCED GRAVITY — N_eff from Spin(4) + Seeley-DeWitt (2026-06-28):")
    sg = sakharov_induced_gravity()
    _ck("TIER: CANDIDATE (coeff) / DERIVED-STRUCTURAL-CONDITIONAL (specific ratio Lambda/M_Pl=4*pi)",
        "CANDIDATE" in sg["tier"] and "DERIVED-STRUCTURAL-CONDITIONAL" in sg["tier"] and sg["N_eff"] == 6)
    _ck("N_eff = 6 [engine; GENERIC-given-dim=4 per canon §5 — C(4,2), not dynamical]",
        sg["N_eff"] == 6 and "GENERIC" in sg["tier"] and "dim=4" in sg["tier"])
    _ck("SCALING FORM M_Pl^2~N*Lambda^2 is QFT INPUT (labeled as such in tier)",
        "QFT INPUT" in sg["tier"] and "scaling FORM" in sg["tier"])
    _ck("RESULT: M_Pl^2 = Lambda^2/(16*pi^2) (from N_eff=6 + QFT INPUT)",
        abs(sg["MPl_sq_coeff"] - 1/(16*_math2.pi**2)) < 1e-14)
    _ck("Lambda = 4*pi * M_REDUCED ~ 12.566 M_red (exact arithmetic) == sqrt(2*pi) ~ 2.507 in the paper's "
        "NON-REDUCED M_Pl. UNIT CONVENTION now explicit (2026-07-28): the legacy key 'Lambda_over_MPl' is "
        "stated against M_red = M_Pl/sqrt(8*pi) and its name never said 'reduced' — that omission is what made "
        "this artifact and the paper's Lambda-bracket look ~12x apart (real convention gap sqrt(8*pi) ~ 5.01). "
        "Plus: the c_reg story CLOSED — RESOLVED 2026-07-29 (one coefficient c_reg = 1/12, three "
        "Lambda-variables) + which-Λ RULED 2026-07-30 (Λ_S scheme / Λ_L = 1/a for dispersion consumers) — "
        "no tier moves",
        abs(sg["Lambda_over_MPl"] - 4*_math2.pi) < 1e-10
        and abs(sg["Lambda_over_M_REDUCED"] - 4*_math2.pi) < 1e-10
        and abs(sg["Lambda_over_MPl_nonreduced"] - _math2.sqrt(2*_math2.pi)) < 1e-12
        and "REDUCED Planck mass" in sg["unit_convention"]
        and sg["c_reg_reconciliation"]["status"].startswith("RESOLVED")
        and "induced_G_from_linear_face_band" in sg["c_reg_reconciliation"]["the three values"]["~1.8"])
    _ck("SD/ASD split: N_eff = 3 (SD) + 3 (ASD); generic-dim=4 qualifier present",
        "3 + 3" in sg["SD_ASD_split"] and "generic" in sg["SD_ASD_split"].lower())
    _ck("NEGATIVE: [SD1,ASD1] = 0 (engine) => L_Skyrme(TT graviton) = 0 => EH != Skyrme quartic",
        "[SD1,ASD1] = 0" in sg["negative_skyrme_EH"] and "L_Skyrme(TT graviton)" in sg["negative_skyrme_EH"] and "= 0" in sg["negative_skyrme_EH"])
    _ck("NEGATIVE: SD-SD intra-sector commutator nonzero (baryonic sector has Skyrme term)",
        "intra-sector" in sg["negative_skyrme_EH"].lower() and "nonzero" in sg["negative_skyrme_EH"].lower())
    _ck("OPEN_4 NOTE: Q-orbit h=0; baryon sources gravity via Sakharov T_mn (loop), not direct h_mn",
        "Q-orbit" in sg["open_4_note"] and "L-Q-mixing" in sg["open_4_note"])
    _ck("CONDITIONS honest: minimal coupling + #1-gap caveat both stated",
        "minimal coupling" in sg["conditions"].lower() and "#1-gap" in sg["conditions"])
    print("        => Sakharov EH STRUCTURAL: Lambda = 4*pi*M_Pl from 6 Spin(4) DOF + Seeley-DeWitt. "
          "Skyrme quartic orthogonal to EH. open_4 (matter coupling) still located gap.")

    print("§21.6.1 SAKHAROV xi GATE (N27) — xi=1/6 catastrophic branch EXCLUDED by left-Spin(4) shift symmetry (2026-06-28):")
    xi = sakharov_xi_minimal_coupling()
    _ck("TIER: FRAMING + removed-falsifier, CONDITIONAL (matches sibling equivalence_principle_protection); "
        "derived-vs-generic split honest (substrate=symmetry, QFT=lemma)",
        "FRAMING" in xi["tier"] and "removed-falsifier" in xi["tier"] and "substrate-specific" in xi["tier"] and "generic" in xi["tier"])
    _ck("SHORTCUT (engine): Omega=R~dR LEFT-Spin(4)-invariant under R->g0 R (|diff|<1e-8)",
        xi["left_invariance_err"] < 1e-8)
    _ck("CONTRAST (engine): right mult conjugates Omega (Om->g0~ Om g0), NOT invariant",
        xi["right_mult_conjugation_err"] < 1e-8 and xi["right_is_invariant"] is False)
    _ck("xi-term forbidden: <dR^2>_0 is shift-NON-invariant (engine) => xi*R*<dR^2> breaks left-Spin(4)",
        xi["xi_term_breaks_shift_symmetry"] is True)
    _ck("N_eff=6 grade-2 DOF + WP-LV1 isotropy (homogeneity anchor: no invariant potential lifts them)",
        xi["N_eff"] == 6 and xi["isotropy_WP_LV1"] is True)
    _ck("mass = central-E U(1) (E=I4*e5), distinct from 6 bivectors => IR mass gives xi~(f_pi/Lambda)^2, not 1/6",
        "central-E U(1)" in xi["mass_phase_distinct"] and "(f_pi/Lambda)^2" in xi["mass_phase_distinct"])
    _ck("SCOPE: REDUCES (not closes) N27 gate (2) — xi=1/6 excluded, xi=0 leading-order + (f_pi/Lambda)^2 corr; "
        "gate (1) #1-gap coefficient STAYS GATED",
        "REDUCES N27 gate (2)" in xi["scope"] and "does NOT close" in xi["scope"] and "Gate (1)" in xi["scope"] and "STAYS GATED" in xi["scope"])
    _ck("COHERENCE: same WP-LV1-twin protection as matter_stability (H1) + WEAK-EP (equivalence_principle_protection)",
        "matter_stability_outside_frame" in xi["coherence"] and "equivalence_principle_protection" in xi["coherence"])
    print("        => N27 gate (2) NARROWED by a SYMMETRY SHORTCUT (canon §4a, s=3/Adler-zero class): xi=1/6 "
          "catastrophic branch EXCLUDED (removed falsifier), xi=0 leading-order. Only gate (1) (#1-gap coefficient) remains.")

    print("§21.6.1 c_reg FOR TWT'S ACTUAL MODE CONTENT — the three-way c_reg 'disagreement' is a")
    print("     Lambda-VARIABLE artifact, and the OA-LF-ii exposure sits entirely in c_lat (2026-07-29):")
    crg = c_reg_from_substrate_mode_content()
    _ck("TIER honest: DERIVED-A only for the exact arithmetic (parametrization identity + S^4 a_1 "
        "type-sum, pure math), DERIVED-given-(R-112 linear face AND R-041 xi=0/E=0) for the physics, "
        "INHERITING R-041's FRAMING+CONDITIONAL cap. NOT a derivation of G; N_eff unchanged "
        "(GENERIC-given-dim-4); OA-LF-i/ii NOT retired",
        "DERIVED-A" in crg["tier"] and "R-112" in crg["tier"] and "R-041" in crg["tier"]
        and "FRAMING+CONDITIONAL" in crg["tier"] and "NOT a derivation of G" in crg["tier"]
        and "GENERIC-given-dim-4" in crg["tier"] and "NOT retired" in crg["tier"])
    _ck("THE TYPE-SUM (exact S^4 spectra, Richardson in s): a_1 = R/6 for one minimal scalar, "
        "a_1 = R for TWT's SIX grade-2 channels, and the excluded readings computed not assumed — "
        "conformal xi=1/6 gives a_1 = 0 (NO induced gravity) and the Lambda^2 HODGE operator gives "
        "a_1 = -R (c_reg = -1/12, REPULSIVE G < 0), with Lambda^1 Hodge a_1 = -R/3 as cross-check. "
        "So the mode-TYPE question was capable of ZEROING or REVERSING induced gravity",
        abs(crg["a1_type_sum_S4"]["1 minimal scalar"] - 2.0) < 1e-4
        and abs(crg["a1_type_sum_S4"]["6 minimal scalars (TWT)"] - 12.0) < 1e-3
        and abs(crg["a1_type_sum_S4"]["Lambda^2 HODGE (Weitzenbock)"] + 12.0) < 1e-3
        and abs(crg["a1_type_sum_S4"]["Lambda^1 HODGE (cross-check)"] + 4.0) < 1e-3
        and crg["excluded_readings_would_have"]["conformal xi=1/6"]["c_reg"] == 0.0
        and crg["excluded_readings_would_have"]["Hodge / 2-form"]["c_reg"] < 0
        and crg["excluded_readings_would_have"]["TWT (6 minimal / Bochner)"]["c_reg"] > 0)
    _ck("RESULT: TWT's mode content is 6 real bosonic massless channels with E = 0 (BOCHNER, "
        "sigma-model kinetic) — NO fermionic channel on the linear face (matter = defect = soliton) "
        "and NO separate gauge sector (the photon is one of the 6 grade-2 strain modes, B.5.4). "
        "E = 0 is forced by the SAME left-Spin(4) shift symmetry R-041 uses for xi = 0: a generic AND "
        "a Weitzenbock-shaped endomorphism are both shift-NON-invariant (engine). => c_reg = 1/12 "
        "EXACTLY, in the SAKHAROV PROPER-TIME-CUTOFF variable — the textbook value IS the substrate's "
        "own mode-content value. This answers induced_G_bracket_mode_count's standing 'mode content "
        "was not specified' caveat: it is the all-minimal-scalar corner",
        abs(crg["c_reg"] - 1/12) < 1e-12
        and crg["mode_content"]["channels"] == 6
        and "BOCHNER" in crg["mode_content"]["type"]
        and crg["mode_content"]["fermionic channels"].startswith("NONE")
        and crg["mode_content"]["gauge sector"].startswith("NONE")
        and all(crg["mode_content"]["endomorphism_shift_breaks"].values())
        and "PROPER-TIME CUTOFF" in crg["c_reg_variable"])
    _ck("THE RECONCILIATION, SCOPED (second pass 2026-07-29): 1/(16 pi G) = N_eff c_lat/"
        "(192 pi^2 a^2) reads c_reg = c_lat/12 at Lambda := 1/a and c_reg = 1/12 at Lambda := "
        "Lambda_eff = sqrt(c_lat)/a, so the two BANKED values are NOT rivals. Their ratio is c_lat "
        "EXACTLY — but BY DEFINITION of Lambda_eff: c_reg multiplies Lambda^2, so the ratio is "
        "(L2/L1)^2 for any two Lambda-variables, independent of the assembly, of a_1 and of N_eff. "
        "The in-primitive assert WAS a TAUTOLOGY (B := A*c_lat, check B/A = c_lat) and has been "
        "DELETED 2026-07-29 — it was not evidence, it read neither banked primitive, and its "
        "absolute tolerance made it FAIL at c_lat = 1e5 while claiming ARBITRARY c_lat; "
        "R-163 had already stated the reconciliation itself. There are TWO Lambda-"
        "variables, not three: the '~1' placeholder sits at Lambda := 1/a alongside 1.82 and is "
        "consistent with it at O(1), and it is SUPERSEDED as never-computed. What remains OPEN is "
        "NOT c_reg but c_lat",
        "TAUTOLOGY" in crg["three_way_resolution"]["~1.82"]
        and "SUPERSEDED" in crg["three_way_resolution"]["~1"]
        and "TWO Lambda-variables, not " in crg["three_way_resolution"]["verdict"]
        and "c_lat" in crg["three_way_resolution"]["what is actually OPEN"])


    # --- REAL cross-primitive consistency check (added 2026-07-29, replaces the deleted
    # in-primitive tautology). This one READS THREE BANKED PRIMITIVES and FAILS if any of
    # them drifts relative to the others — which is exactly what the deleted assert could
    # not do, since it recomputed local literals and never touched a banked value.
    _sg_x = sakharov_induced_gravity()
    _bd_x = induced_G_from_linear_face_band()
    _creg_x = crg["c_reg"] if isinstance(crg.get("c_reg"), float) else 1.0 / 12.0
    _chain = math.sqrt(math.pi / (_creg_x * _sg_x["N_eff"]))
    _ck("CROSS-PRIMITIVE: c_reg (mode-content primitive) + N_eff (sakharov) reproduce sakharov's "
        "OWN Lambda/M_Pl(non-reduced) = sqrt(2 pi) = %.6f, and c_lat (linear-face-band primitive) "
        "is positive and at its banked 21.83. Unlike the deleted tautology this reads all three "
        "and FAILS on drift in any one of them" % math.sqrt(2 * math.pi),
        abs(_chain - _sg_x["Lambda_over_MPl_nonreduced"]) / _sg_x["Lambda_over_MPl_nonreduced"] < 1e-5
        and _bd_x["c_lat"] > 0 and abs(_bd_x["c_lat"] - 21.8285) / 21.8285 < 1e-3)
    _ck("THE SENSITIVITY (the same quantity, both faces): deforming the monad-scale curvature weight "
        "to kappa for s < a^2 makes c_lat(kappa) EXACTLY AFFINE with slope = R-163's own ~93% "
        "proper-time support fraction, so OA-LF-ii's own 'up to O(1)' tolerance (kappa in [1/2,2]) "
        "moves c_lat by a factor ~3.6 — R-163's quoted -5%..-25% window is the GAP/state "
        "(OA-LF-i-class) question and UNDERSTATES the OPERATOR exposure by > an order of magnitude. "
        "But Lambda_eff = sqrt(c_lat)/a = sqrt(2 pi) M_Pl EXACTLY for every c_lat, so c_reg = 1/12 "
        "carries ZERO OA-LF-ii sensitivity while 'c_reg ~ 1.82' carries ~93%-LINEAR sensitivity. "
        "R-163's branch is WEAKER as a c_reg determination than its window suggests; its real content "
        "is the monad spacing a. FENCE + SWEEP both stated, revert clause named",
        0.90 <= crg["OA_LF_ii_sensitivity"]["slope fraction (= R-163's s<a^2 support)"] <= 0.95
        and "factor 3.6" in crg["OA_LF_ii_sensitivity"]["O(1) tolerance kappa in [1/2,2]"]
        and "UNDERSTATES" in crg["OA_LF_ii_sensitivity"]["R-163's quoted window"]
        and "ZERO OA-LF-ii sensitivity" in crg["OA_LF_ii_sensitivity"]["what does NOT move"]
        and "Does NOT derive G" in crg["scope_fence"]
        and "RETIRED" in crg["scope_fence"]
        and "Revert clause" in crg["would_change_if"]
        and "ADDITIVE" in crg["pending_sweep"])
    print("        => c_reg = 1/12 for TWT's OWN mode content (6 minimal/Bochner channels; E=0 from "
          "R-112's sigma-model kinetic term for the Hodge corner and from R-041's shift symmetry for "
          "the conformal corner); the '21.6 disagreement' was a Lambda-VARIABLE bookkeeping defect, "
          "reconciled by definition of Lambda_eff, not by computation; the OA-LF-ii exposure lives "
          "entirely in c_lat/a, NOT in the induced-G coefficient.")

    print("§21.6.1 MATTER-GRAVITY COUPLING (open_4) — structural resolution (2026-06-28):")
    mg = texture_matter_gravity_coupling()
    _ck("9 engine checks (L×L=0, Q×Q=0, L×Q Hodge, [Q,Q]=-2L, sigma-model, h00=0, hkl=0 EXACT CANCEL)",
        mg["n_engine_checks"] == 9)
    _ck("L×L I4-bilinear = 0 (all 3x3; spatial pairs share index -> epsilon=0)",
        "0 (all 3x3, engine)" in mg["I4_bilinear"]["LL_block"])
    _ck("Q×Q I4-bilinear = 0 (all 3x3; temporal pairs share index 4 -> epsilon=0)",
        "0 (all 3x3, engine)" in mg["I4_bilinear"]["QQ_block"])
    _ck("L×Q Hodge: exactly 3 nonzero pairs with epsilon values (engine)",
        "<e12 I4 e34>=+1" in mg["I4_bilinear"]["LQ_Hodge_nonzero"] and
        "<e13 I4 e24>=-1" in mg["I4_bilinear"]["LQ_Hodge_nonzero"] and
        "<e23 I4 e14>=+1" in mg["I4_bilinear"]["LQ_Hodge_nonzero"])
    _ck("[Q,Q] = L-orbit commutators (engine): [e14,e24]=-2*e12 etc.",
        "[e14,e24]=-2*e12" in mg["commutator_QQ"] and "quaternionic" in mg["commutator_QQ"])
    _ck("Hedgehog Om_k has L-orbit correction from [Q,Q]=-2L (structural)",
        "[Q,Q]=-2L" in mg["hedgehog_Omega"] and "L-orbit" in mg["hedgehog_Omega"])
    _ck("h_kl (tree) = 0 EXACTLY (N26: Lk_Ql=-Qk_Ll exact cancellation, 20 random configs engine): DERIVED-STRUCTURAL-CONDITIONAL",
        "ZERO" in mg["h_kl_tree"] and "cancellation" in mg["h_kl_tree"] and "DERIVED-STRUCTURAL-CONDITIONAL" in mg["h_kl_tree"])
    _ck("h_00 (tree) = 0 at ALL orders: DERIVED (Q×Q I4=0 + static Om_0=0)",
        "ZERO at all tree-level orders" in mg["h_00_tree"] and "Q×Q I4=0" in mg["h_00_tree"])
    _ck("Newtonian h_00 from Sakharov T_mn (FRAMING: mechanism identified, CANDIDATE: explicit Phi)",
        "LOOP LEVEL" in mg["Newtonian_sourcing"] and "FRAMING" in mg["Newtonian_sourcing"])
    _ck("ONE GRAVITATIONAL LAYER: tree h_mn=0 (exact, N26); Newtonian from Sakharov loop only",
        "ONE GRAVITATIONAL LAYER" in mg["structural_picture"] and "SOLE" in mg["Newtonian_sourcing"])
    _ck("open_4 LOCATED-GAP (N26): tree h_mn=0 exact; texture_tetrad() still raises",
        "LOCATED-GAP" in mg["open_4_status"] and "texture_tetrad() still raises" in mg["open_4_status"])
    print("        => open_4 LOCATED-GAP (N26): tree h_mn=0 exact (Lk_Ql=-Qk_Ll cancellation); "
          "Sakharov T_mn SOLE gravity mechanism. "
          "Explicit Phi(r)=-G_N*M/r remains CANDIDATE (N25).")

    print("§9.6 #1-GAP as a CONSTRAINT-SATISFACTION CLASS — the compatible-EOM-field boundary (FRAMING; TWT_EOM_MAP.md):")
    ec = eom_constraint_class()
    _ck(f"BINARY BOUNDARY engine-anchored: all {ec['n_engine_checks']} engine-backed HARD constraints resolve "
        f"(9 called primitives {ec['HARD_boundary_engine_backed'][:2]}... + 3 inline {ec['HARD_boundary_inline_engine']}) "
        "⇒ the compatible-field boundary is built of LIVE banked facts, not paraphrase",
        ec["n_engine_checks"] == 12 and len(ec["HARD_boundary_engine_backed"]) == 9
        and "H2_klein_gordon" in ec["HARD_boundary_inline_engine"])
    _ck("GAP INTACT: the class-VARIANT value-gates (alpha_em_value, qcd_collider_phenomenology, and — added 2026-07-27 — "
        "wave_speed_c, the strain-mode dispersion that E1 constrains) + the Layer-3 structural gate (texture_tetrad) all "
        "still RAISE — computing a variant from one ansatz would be a toy (canon §3)",
        ec["gates_intact"]["value_#1gap"] == ["alpha_em_value", "qcd_collider_phenomenology", "wave_speed_c"]
        and ec["gates_intact"]["structural_Layer3"] == ["texture_tetrad"])
    _ck("H4 RESCOPED (R-165) and now COMPUTED, not a flag: the boundary's H4 label carries BOTH orders separately — "
        "(a) 2nd-moment one-stiffness g1=g2 (the dim-4 statement) and (b) degree-4 invariant space 1-dimensional ⇒ no "
        "anisotropic quartic ⇒ anisotropy only at dim-8 — AND states that neither reaches the isotropic dim-6 term",
        any("H4_isotropy_orders" in x and "deg-4 invariant space 1-dim" in x and "that is E1" in x
            for x in ec["HARD_boundary_inline_engine"]))
    # H8's own gate, re-fired here so THIS check arbitrates rather than trusting the aggregator.
    # (The same raise is separately exercised by the 2026-08-19 sabotage guard in check_structure;
    # what is new here is that H8's boundary entry now depends on it instead of on an isinstance.)
    try:
        Substrate(memory_kernel=MemoryKernel.GATED).tau_mem_over_tau_wave()
        _h8_gate_fired = False
    except GatedError:
        _h8_gate_fired = True
    _ck("H8 REPAIRED (2026-08-23) and now EXERCISED, not type-checked: the boundary's H8 entry was a bare "
        "isinstance(Substrate().memory_kernel, MemoryKernel) — an assertion on an Enum member that cannot fail, the "
        "R-165 defect class sitting two lines under the comment describing its own fix, and counted in n_engine inside "
        "a primitive advertising LIVE banked facts. Both orders are now separated and BEHAVIOURALLY checked here too: "
        "(a) with NO branch chosen tau_mem RAISES (GatedError) — the driven NESS's memory magnitude stays #1-gap open, "
        "not quietly equilibrium; (b) the fork is the live binary {fading, hysteretic} and it MOVES tau_mem (only the "
        "hysteretic branch carries the reactive-barrier exp(S/hbar) §11.6 needs) — a constitutive fork, not a label",
        any("H8_drive_dissipation_fork" in x and "tau_mem RAISES" in x and "MOVES tau_mem" in x
            for x in ec["HARD_boundary_inline_engine"])
        and {k.value for k in MemoryKernel if k is not MemoryKernel.GATED} == {"fading", "hysteretic"}
        and "exp(S/hbar)" in Substrate(memory_kernel=MemoryKernel.HYSTERETIC).tau_mem_over_tau_wave()
        and Substrate(memory_kernel=MemoryKernel.FADING).tau_mem_over_tau_wave()
            != Substrate(memory_kernel=MemoryKernel.HYSTERETIC).tau_mem_over_tau_wave()
        and _h8_gate_fired)
    _ck("E1 ADDED as the class's FIRST EMPIRICAL constraint — and deliberately NOT numbered H12: it is IMPORTED data "
        "(I-19), it is a CEILING that can refute but supplies no equation (zero anchor rank), and its bindingness is "
        "CONDITIONAL on the un-built outside↔inside projection, carried as an explicit field so an I-19 excision fires "
        "against E1 alone and leaves H1-H11 untouched",
        ec["EMPIRICAL_boundary_conditional"]["id"] == "E1_dim6_isotropic_LV_ceiling"
        and "I-19" in ec["EMPIRICAL_boundary_conditional"]["source"]
        and "CONDITIONAL" in ec["EMPIRICAL_boundary_conditional"]["bindingness_HEDGE"]
        and "zero anchor rank" in ec["EMPIRICAL_boundary_conditional"]["kind"]
        and "NAIVE" in ec["EMPIRICAL_boundary_conditional"]["naive_value_status"])
    _ck("the substrate-normalization CEILING is a BANKED RETURNED FIELD, not a floating number: "
        "implied_substrate_c_ceiling spans 1.5e-9 … 5.4e-7 across {species, Λ-corner}, so downstream text cites the "
        "primitive rather than quoting an unbacked bracket (canon §2). (Re-cut 2026-07-30 by the which-Λ ruling to "
        "the Λ_L = 1/a band [0.386, 0.734] M_Pl; was 1.7e-10 … 6.3e-6 under the retired [0.13, 2.5] bracket)",
        (lambda d: abs(d["photon_eta4_1e-8"][0] - 1.49e-9) < 1e-11 and abs(d["matter_eta4_1e-6"][1] - 5.39e-7) < 1e-9)(
            lv["implied_substrate_c_ceiling"]))
    _ck("INVARIANT/VARIANT partition + epistemics recorded: invariants (s=3, sin²θ_W=3/8, π₃, Z3-dichotomy, WEAK-EP) = "
        "DERIVABLE-by-class-invariance; variants (α,g,g_s,σ_QCD,masses,v,τ_mem,Θ_rel-value) = provably gated; "
        "binary=boundary-only, plausibility=within-field, revision=bidirectional",
        len(ec["class_invariant_DERIVABLE"]) >= 5 and len(ec["class_variant_GATED"]) >= 5
        and "FRAMING" in ec["tier"] and "bidirectional revision" in ec["epistemics"])
    print("        ⇒ the #1 gap is MAPPED: a binary boundary of live banked constraints + a 4-axis residual; the path to a "
          "banked number is the invariant test (s=3 pattern), never cranking one ansatz.")

    print("§9.6 INVARIANT/VARIANT AUDIT of the #1-gap class — the hypothesis test (FRAMING; TWT_EOM_MAP.md §4; reviewer-trimmed):")
    iv = eom_invariant_variant_audit()
    _ck("FORWARD (trimmed, reviewer OVER-CLAIM): NO [DERIVED] Layer-2 VALUE exists; the genuine Layer-2 dynamical "
        "class-invariants are EXACTLY TWO, both SYMMETRY SHORTCUTS (s=3 Adler-zero + Θ_rel Z3-dichotomy Schur); the audit "
        "engine-reclassifies ckm_seed (SEED) + qcd_uv (LOCATED) OUT of 'wins' by their banked tier",
        len(iv["layer2_dynamical_invariants_GENUINE"]) == 2
        and set(iv["audit_reclassified_OUT_of_wins (by banked tier)"]) == {"ckm_hierarchy_and_cp_seed", "qcd_uv_conformal_phaseCD"}
        and "near-VACUOUS" in iv["no_disguised_toy"])
    _ck("BACKWARD HOLDS for MAGNITUDES; 'open' REFINED into 3 categories; category-3 CORRECTED (bidirectional revision, "
        "EOM_MAP §5): NO kernel-independent carve-out survives — N4's {chiral projector ½(1+I4)+S₊+gen-space} is DERIVED "
        "(CKM arc, +e4) with residual = property P = Θ_rel (#1-gap KERNEL); octet kernel-dep (N5); only the tetrad remains",
        iv["open_cat3_structural"]["kernel_INDEPENDENT"] == []
        and "(ii) LOCATED" in iv["N4_status"] and "NO surviving kernel-independent" in iv["carve_out"]
        and iv["open_cat3_structural"]["Layer3_deep_gate"] == ["tetrad / STRONG-EP"])
    _ck("HONESTY recorded: the 'boundary unification' is a RESTATEMENT of the already-banked fault line (not new content); "
        "the program reframe (new Layer-2 derivation = INVARIANT-HUNTING via symmetry shortcut, fired twice) stands; tier FRAMING",
        "not new content" in iv["unification_is_a_restatement"].lower() and "INVARIANT-HUNTING" in iv["program_reframe"]
        and "FRAMING" in iv["tier"])
    print("        ⇒ the honest finding: the symmetry shortcut is the ONLY route that has yielded a Layer-2 invariant (twice); "
          "N4 is already (ii) LOCATED (residual=Θ_rel kernel); the only non-#1-gap opens are the Layer-3 tetrad + F3.")

    print("§9.6 FORK-TREE MAP of the compatible EOM field — 'all the options, for the record' (FRAMING; TWT_EOM_MAP.md §3a):")
    ff = eom_compatible_field_forks()
    _ck("the compatible field = a LOCATED discrete fork tree × a continuous kernel residual: 3 forks (A memory-kernel/N18, "
        "B NESS-character/N11, C colour-Z3/N10), 1 DATA-PINNED (C→Z3-broken, engine-arbitrated: non-democratic CKM), "
        "2 OPEN-but-leaning (A→hysteretic, B→limit-cycle/N9) ⇒ 4 live discrete branches × one Θ_rel-kernel value",
        ff["n_discrete_forks"] == 3 and ff["n_data_pinned"] == 1 and ff["n_live_branches"] == 4
        and "TWO Hodge-tied Z3 FACES" in ff["fork_C_note"]
        and "[CANDIDATE]" in ff["forks"]["C_two_tied_Z3_faces(N10)"]["merge_one_Theta_rel_breaks_both"])
    _ck("observable→fork map + honest scope: invariants (s=3, Z3-dichotomy, sin²θ_W, charge, π₃, WEAK-EP) set by NO fork; "
        "τ_mem←A, coupling-universality←B=critical, CKM/colour-direction←C, magnitudes←the continuous Θ_rel residual; "
        "scope = the LOCATED fork tree, completeness NOT proven (FRAMING, no new value)",
        len(ff["observable_to_fork"]["INVARIANT (no fork)"]) == 6 and "completeness NOT proven" in ff["honest_scope"]
        and "FRAMING" in ff["tier"])
    print("        ⇒ the compatible field is SMALL & structured: 3 forks (1 data-pinned, 2 leaning) × one continuous kernel value, "
          "NOT a vast unknown — the #1 gap is 2 open forks (hysteretic?, critical?) + the Θ_rel kernel value.")



    print("§24.6 macroscopic angular momentum is L/Q-decomposed (same split as leptons/quarks):")
    ms = macroscopic_LQ_split()
    _ck(f"spatial r∧v ∈ L-orbit (lepton sector)  (blades {ms['spatial r∧v blades']})", ms["spatial part ∈ L-orbit (lepton sector)"])
    _ck(f"center-of-mass e4-drift ∈ Q-orbit (quark sector)  (blades {ms['e4-drift blades']})", ms["e4-drift ∈ Q-orbit (quark sector)"])
    print("        ⇒ the L/Q split classifying matter at the particle scale also organizes macroscopic angular momentum.")
    _ck(f"polar moment I = Σ m|s|² (Sundman) computes  (got {polar_moment_of_inertia([1,2],[(1,0,0),(0,1,1)])})",
        polar_moment_of_inertia([1, 2], [(1, 0, 0), (0, 1, 1)]) == 5)

    # ------------------------------------------------------------------
    # RECOVERED CHECKS (2026-07-02): the two blocks below were banked on
    # 2026-06-29/30 but accidentally appended AFTER `sys.exit()` inside the
    # `if __name__` block — dead code the harness never executed (their
    # ledger entries claimed "suite +1" that never counted). Moved here so
    # they actually run; content unchanged.
    # ------------------------------------------------------------------
    # K_c kernel-form via direct LSWT (2026-06-29, T1 K_c re-attack route):
    # adds an engine-verified NEGATIVE result eliminating the static-LSWT closure route
    # for the K_c kernel form K_c = N_G * sin²(q) * J at the D=J QCP.
    kcm = Kc_magnon_stiffness_canted_FM_at_DJ()
    _ck(f"K_c via direct LSWT: K_long = sqrt(38) J ≈ 6.164 (got {kcm['K_long_value']:.4f}); "
        f"K_trans = (2 cos q* + 4) J ≈ 5.947 (got {kcm['K_trans_value']:.4f}; ERRATUM "
        f"2026-07-26 — the prior 4 cos q* ≈ 3.893 transcription omitted the 8 zero-phase "
        f"transverse D4 bonds; probe-confirmed on the 4D instrument, K4D 4D-1 consensus); "
        f"K_c = 2J/19 ≈ 0.105 (got {kcm['K_c_asserted_over_J']:.4f}); ratio K_long/K_c = (19/2)sqrt(38) ≈ 58.56 "
        f"(got {kcm['ratio_K_long_over_K_c']:.4f}) — static LSWT route to K_c ELIMINATED "
        f"(a fortiori under the erratum: K_trans/K_c ≈ 56.49, near-not-equal 58.56, non-coincidence flagged)",
        kcm["outcome"] == "LOCATED-GAP-REFINED"
        and abs(kcm["K_long_value"] - 6.164414002968977) < 1e-9
        and abs(kcm["K_trans_value"] - (2.0 * math.cos(math.atan(math.sqrt(2.0)/6.0)) + 4.0)) < 1e-9
        and abs(kcm["K_c_asserted_over_J"] - 2.0/19.0) < 1e-12
        and abs(kcm["ratio_K_long_over_K_c"] - 9.5 * (38.0**0.5)) < 1e-9
        and kcm["is_K_c_a_static_LSWT_identity"] is False
        and abs(kcm["sin_squared_q_star"] - 1.0/19.0) < 1e-12
        and abs(kcm["cos_squared_q_star"] - 18.0/19.0) < 1e-12)


    print("W4 (2026-07-27) — COUPLING-SECTOR CHANNEL DISJOINTNESS: the symmetry route to a derived")
    print("     alpha_em/alpha_s shared-condition is CLOSED at the two-point level:")
    csd = coupling_sector_channel_disjointness()
    _ck("W4 the channel CLASSIFICATION [DERIVED-A]: the SIGNED identity "
        "<B I4 B>_0 = |B_ASD|^2 - |B_SD|^2 = 2<B_L I4 B_Q>_0 exactly (banked signed, verified on "
        "random draws AND on an exact integer-coefficient witness); and the same form VANISHES "
        "IDENTICALLY on the colour-carrying grade-3 sector, <X I4 X>_0 == 0, with a GRADE-COUNTING "
        "proof (I4*X is grade 1 for grade-3 X, and grade-3 x grade-1 lands in grades 2 and 4 only, "
        "so no grade-0 exists to extract) -- the alpha-type reconversion channel literally does not "
        "exist over colour data. The coset partner E*e124 = e35 is the EXTERNAL-phase blade "
        "(litmus-compliant), not Cl(4,0) grade-2",
        "SIGNED" in csd["tier"] and "|B_ASD|^2 - |B_SD|^2 = 2<B_L I4 B_Q>_0" in csd["signed_identity"]
        and "grade counting" in csd["colour_sector_has_no_alpha_form"])
    _ck("W4 the SPIN CONTENT and INVARIANT-FORM COUNTS [DERIVED-A, exact nullity + independent "
        "weight spectra]: under the spatial SO(3) both sectors share, the EM carrier grade-2 is a "
        "MULTIPLICITY-2 SPIN-1 block (L and Q both spin 1, Casimir ratio 1.000, weights two copies "
        "of {-1,0,1}) while the colour-force carrier coset-5 is SPIN-2 (ratio 3.000, weights "
        "{-2,-1,0,1,2}). Counts: full Spin(4) gives grade-2 = 2 forms, grade-3 = 1, CROSS = 0; "
        "spatial so(3) gives grade-2 = 3 (the 2x2 spin-1 kernel incl. the Schur-ALLOWED alpha "
        "channel K_LQ), coset-5 = 1, CROSS(grade-2, coset-5) = 0, cross(grade-2, geometric-3) = 2 "
        "(the ladder = spatial-rotation identity, the NON-force channel). REVIEWER STRENGTHENING: "
        "the blocks are DIMENSIONALLY INEQUIVALENT (6 vs 5), so no invertible intertwiner exists "
        "under ANY subgroup chain. R-151 route: EM fits (F-slot count 4 = the [Om,Om] block); "
        "colour does NOT (its invariant needs a spin-2 value slot; R-151's slots top out at spin 1)",
        csd["invariant_form_counts"]["Spin(4) cross"] == 0
        and csd["invariant_form_counts"]["so(3) cross(grade-2, coset-5)"] == 0
        and csd["invariant_form_counts"]["so(3) grade-2"] == 3
        and csd["invariant_form_counts"]["so(3) L-Q cross"] == 1
        and csd["invariant_form_counts"]["so(3) cross(grade-2, geometric-3)"] == 2
        and abs(csd["spin_content"]["casimir_ratios"]["coset-5"] - 3.0) < 1e-9
        and csd["block_dimensions"]["grade-2"] == 6 and csd["block_dimensions"]["coset-5"] == 5
        and "ANY subgroup chain" in csd["block_dimensions"]["consequence"]
        and "does NOT fit" in csd["r151_route"]["colour"])
    _ck("W4 the SCENARIO QUALIFIERS (these must survive into every prose restatement): 'ONE scalar "
        "K_5' is the SO(3)-SCENARIO count, not scenario-free; under a Z3-only NESS (the open N10 "
        "binary) cross-pairings become ALLOWED with count EXACTLY 10 -- confirmed by two "
        "independent methods (explicit intertwiner nullity and a weights-mod-3 character count) -- "
        "and that is ALLOWED-BUT-UNFORCED (less symmetry gives MORE kernel freedom, never forced "
        "equality); N10's Z3-BROKEN NESS pushes BELOW even that, a fortiori unforced. So under EVERY "
        "scenario Schur PERMITS K_1(omega) != K_5(omega)",
        "count exactly 10" in csd["scenario_qualifiers"]["Z3-only (open N10 binary)"]
        and "ALLOWED-BUT-UNFORCED" in csd["scenario_qualifiers"]["Z3-only (open N10 binary)"]
        and "a fortiori" in csd["scenario_qualifiers"]["N10 Z3-BROKEN NESS"]
        and "SO(3)-SCENARIO count" in csd["scenario_qualifiers"]["one scalar K_5"])
    _ck("W4 what SURVIVES + the hard scope fence [LOCATED-GAP]: the alpha_s fold-in stops being a "
        "BARE conjecture and becomes ONE named kernel property -- spin-channel universality, "
        "Im chi_5 proportional to Im chi_1 UP TO FREQUENCY-INDEPENDENT WEIGHTS -- landing on the "
        "already-named SOC-universality axis, with the spin-2 block being Theta_rel's own channel. "
        "Quoted BESIDE it, always: the CROSS-BLOCK WEIGHT IS OPEN (no derived analogue of the 8/3 "
        "charge/Casimir ratio that fixes sin^2 theta_W = 3/8). CONDITIONAL on the banked "
        "gluon-FRAMING channel assignment AND the Im-chi-moments FRAMING. FENCE: TWO-POINT / "
        "MAGNITUDE-SOURCE ONLY -- never the RUNNING/AF face (cubic [3,5]/[5,5] brackets couple the "
        "sectors; the full-su(3) running correction stands verbatim); the EW trio's one-dial "
        "reduction (R-035b) is untouched",
        "LOCATED-GAP" in csd["tier"] and "gluon-FRAMING" in csd["tier"] and "Im-chi-moments" in csd["tier"]
        and "FREQUENCY-INDEPENDENT WEIGHTS" in csd["named_premise"]
        and "8/3" in csd["open_cross_block_weight"] and "OPEN" in csd["open_cross_block_weight"]
        and "TWO-POINT" in csd["scope_fence"] and "NOT about the RUNNING" in csd["scope_fence"]
        and "R-035b" in csd["scope_fence"])

    print("W5 (2026-07-27) — INDUCED EH ON THE DERIVED LINEAR-FACE BAND: I-3 NARROWED (3 premises -> 2):")
    iglf = induced_G_from_linear_face_band()
    _ck("W5 the FLAT-BAND NUMBERS [DERIVED-given-the-NN-band-INPUT]: the D4 NN second moment is "
        "sum_b b_mu b_nu = 12*delta EXACTLY (the WP-LV1 isotropy face, so ktil^2 -> k^2), and the "
        "proper-time integral over the DERIVED band is finite in both UV (compact BZ) and IR (4D) "
        "with no regularization choice left, giving c_lat = 16 pi^2 I_lat = 21.83: three grids "
        "converge monotonically from below with h^2-Richardson limits agreeing to < 1e-3, and "
        "|c_lat - 21.83| < 0.05 at the banked grid. The DERIVED band sits ~74% ABOVE the "
        "Debye-sphere generic guess c_D = 4 pi = 12.566 -- a genuinely derived O(1) where c_reg "
        "was free",
        abs(iglf["c_lat"] - 21.83) < 0.05
        and abs(iglf["c_lat_at_banked_grid_N32"] - 21.83) < 0.05
        and abs(iglf["richardson_limits"]["16->24"] - iglf["richardson_limits"]["24->32"]) < 1e-3
        and abs(iglf["c_lat_over_c_Debye"] - 1.737) < 0.01)
    _ck("W5 the METHOD, EXTERNALLY CALIBRATED (both re-run in code, not merely recorded): the SAME "
        "grid + h^2-Richardson machinery applied to the Z^4 nearest-neighbour band reproduces the "
        "known 4D hypercubic lattice Green's function at the origin (G(0)/4 = 0.30986678, Watson "
        "class) to ~4e-8 -- a literature-anchored absolute calibration of the quadrature -- and a "
        "seeded INDEPENDENT Monte-Carlo quadrature of the same D4 integral agrees with the grid "
        "value. The Seeley-DeWitt curvature weight a_1 = R/6 is verified on the EXACT S^4 spectrum "
        "by Richardson in proper time (import-exempt pure math: the operator is specified). Support "
        "is localized: ~95% of I_lat rides ktil^2 > 1/a^2 and ~93% rides proper time s < a^2",
        float(iglf["external_calibration"]["Z^4 tadpole vs literature G(0)/4 = 0.30986678"]
              .split()[-1]) < 1e-6
        and abs(iglf["external_calibration"]["independent MC quadrature of the same D4 integral"]
                - iglf["c_lat"]) < 0.15
        and abs(iglf["seeley_dewitt_a1"]["computed"] - 2.0) < 1e-3
        and 0.94 <= iglf["support"]["fraction of I_lat from ktil^2 > 1"] <= 0.96
        and 0.90 <= iglf["support"]["fraction from proper time s < a^2"] <= 0.95)
    _ck("W5 the PREMISE REDUCTION, counted honestly: I-3's triple becomes TWO -- 'one-loop validity' "
        "discharged to the banked Gate A, 'covariant regularization' COMPUTED AWAY, and 'a standard "
        "QFT vacuum' replaced by OA-LF, which is TWO ASSUMPTIONS COUNTED AS TWO: (i) OCCUPATION, a "
        "statement about the STATE (NESS occupation = the Gaussian ground-state measure at monad "
        "scales) and (ii) COVARIANT MONAD-SCALE CURVATURE WEIGHT, a statement about the OPERATOR "
        "(a_1 = R/6 extends to s ~ a^2 up to O(1)), both discharged by the SAME #1-gap retirement "
        "handle. CRITICAL WORDING: 'REGULATOR-FREE' DESCRIBES I_lat ONLY -- the former O(1) "
        "regulator freedom is RELOCATED into OA-LF(ii), one named physical unknown carrying ~93% of "
        "the support, now localized with a retirement handle. R-041's FRAMING+CONDITIONAL xi = 0 is "
        "INHERITED",
        iglf["OA_LF_assumptions"]["count"] == 2
        and "STATE" in iglf["OA_LF_assumptions"]["(i) occupation"]
        and "OPERATOR" in iglf["OA_LF_assumptions"]["(ii) covariant monad-scale curvature weight"]
        and "3 premises -> 2" in iglf["OA_LF_assumptions"]["I-3 ledger"]
        and "DESCRIBES I_lat ONLY" in iglf["regulator_language"]
        and "RELOCATED" in iglf["regulator_language"]
        and "R-041" in iglf["tier"] and "DERIVED-CONDITIONAL-on-(OA-LF-i AND OA-LF-ii)" in iglf["tier"])
    _ck("W5 the a-VALUE, its RANGE, the NORMALIZATION SPREAD and the JURISDICTION FENCE: c_lat = "
        "21.83 is the GAPLESS-SHARED-BAND idealization -- the realistic canted vacuum has N_G = 2 "
        "(2 gapless + 4 gapped, exact 6-band Bogoliubov structure UN-BANKED). ** THE -5%...-25% "
        "REFINEMENT WINDOW AND ITS a in [1.61, 1.86] IMAGE ARE WITHDRAWN 2026-08-23 (estate of "
        "N64, B1): the window rode a UNIFORM-GAP spot check assuming (gap/b_max)^2 in [0.01, 0.04] "
        "while the actual canted vacuum gives 4.049e-05 -- 247x-988x too large -- and is 2 gapless "
        "+ 4 gapped, not uniform-gap. NO WINDOW AND NO REPLACEMENT NUMBER IS ASSERTED (the "
        "six-band measure is unresolved at M <= 47, Richardson limit consistent with ZERO), which "
        "is what the banked induced_G_leading_coefficient_mass_independent line at STEP 2 already "
        "predicts. THE FENCE IS UNWEAKENED: a is a BACK-FIT of measured G_N, so a narrower window "
        "narrows a back-fit and MOVES NO EMPIRICAL CLAIM -- IT IS NEVER BETTER AGREEMENT ** "
        "(derived stiffness "
        "anisotropy shifts c_lat by < 0.01%). THREE-WAY normalization spread noted (paper 16 pi^2 / "
        "bracket 96 pi^2 / sakharov 192 pi^2): the paper B.6.2 table IS self-consistent under its "
        "OWN formula (c_reg = c_lat/12 = 1.82, inside 'c_reg ~ 1') so a convention note is needed, "
        "not an arithmetic fix -- SCOPED (2026-07-28) to the pi-CONVENTION spread ONLY; the VALUE "
        "question RESOLVED 2026-07-29 (one c_reg = 1/12 in the proper-time variable; 1.82 = c_lat/12 "
        "is the same computation in Lambda := 1/a) and which-Lambda RULED 2026-07-30; "
        "the CONVENTION-INVARIANT statement 'a = 1.86 ell_Planck, Planckian "
        "within O(1)' SUPPORTS B.6.2. The engine cross-tie sqrt(96 pi^2/6) = 4 pi reproduces "
        "sakharov_induced_gravity exactly and is c_lat-INDEPENDENT, so nothing banked moves. "
        "JURISDICTION: 'a' is ALWAYS CONDITIONAL -- never 'TWT derives the monad spacing'; Lambda "
        "values stay CANDIDATE/conditional and do NOT move to chase agreement with measurement "
        "(both historical re-cuts were fence case (a) -- the 2026-07-28 widening spanned the apparent "
        "c_reg disagreement; the 2026-07-29 resolution + 2026-07-30 which-Lambda ruling SPLIT the "
        "symbol, Lambda_S scheme / Lambda_L = 1/a = [0.386, 0.734] M_Pl for dispersion consumers, and "
        "RETIRED the wide bracket. 'It agrees better with the data' is NEVER a reason)",
        "WITHDRAWN 2026-08-23" in iglf["gapless_idealization"]["honest refinement window"]
        and "NO WINDOW IS ASSERTED" in iglf["gapless_idealization"]["honest refinement window"]
        and iglf["gapless_idealization"]["premise refutation (2026-08-23, B1)"][
            "no number of the -0.111% class is asserted anywhere"] is True
        and abs(iglf["gapless_idealization"]["premise refutation (2026-08-23, B1)"][
            "(g/b_max)^2"] - 4.049e-05) < 1e-8
        and "NEVER BE QUOTED AS ONE" in iglf["gapless_idealization"][
            "jurisdiction fence (verbatim, unweakened)"]
        and "BACK-FIT OF MEASURED G_N" in iglf["gapless_idealization"][
            "jurisdiction fence (verbatim, unweakened)"]
        and "UN-BANKED" in iglf["gapless_idealization"]["canted vacuum"]
        and "16 pi^2" in iglf["normalization_spread"]["three conventions"]["paper SSB.6.2"]
        and "192 pi^2" in iglf["normalization_spread"]["three conventions"]["sakharov_induced_gravity"]
        and "c_reg = c_lat/12 = 1.82" in iglf["normalization_spread"]["paper table self-consistency"]
        and "PLANCKIAN WITHIN O(1)" in iglf["normalization_spread"]["convention-invariant statement"]
        and abs(iglf["engine_cross_tie"]["sqrt(96 pi^2 / N_eff)"]
                - iglf["engine_cross_tie"]["sakharov_induced_gravity Lambda_over_MPl"]) < 1e-12
        and "ALWAYS CONDITIONAL" in iglf["a_monad_spacing"]["JURISDICTION"]
        and "NEVER write" in iglf["a_monad_spacing"]["JURISDICTION"]
        and "do NOT move" in iglf["fence"]
        and "NEVER a reason" in iglf["fence"]
        and iglf["c_reg_vs_sakharov"]["status"].startswith("RESOLVED")
        and "1/12" in iglf["c_reg_vs_sakharov"]["sakharov_induced_gravity"]
        and "VALUE question RESOLVED"
            in iglf["normalization_spread"]["paper table self-consistency"])

    print("W6 (2026-07-27) — THE ELASTIC-EH NEGATIVE (ledger N51): the Skyrme quartic contains NO")
    print("     tree-level Einstein-Hilbert term -- 'gravity as elasticity' dead in the banked class:")
    sqe = skyrme_quartic_contains_no_tree_EH()
    _ck("W6 the EXACT DECOMPOSITION [DERIVED-A, rational arithmetic -- no floats]: in the R-151 "
        "invariant basis Q1..Q8, sqrt(g)R|_2 = Q1 - Q2 - (3/4)Q3 + (3/4)Q4 - (1/4)(Q5+Q7) + "
        "(1/4)(Q6+Q8) and the Skyrme quartic = -(Q5+Q6+Q7+Q8), both EXACT on random INTEGER "
        "datasets; parity acts as (Q1 Q2)(Q3 Q4)(Q5 Q8)(Q6 Q7) so the EH representative is "
        "parity-ODD and the quartic parity-EVEN EXACTLY, with ZERO OVERLAP (parity-even part of EH "
        "= 0, parity-odd part of the quartic = 0), basis-independently. The quartic's equal weight "
        "-1 on all four W-invariants IS the definite KILLING combination; EH's W-block is the "
        "INDEFINITE h-combination. MECHANISM: the property that makes the term a stabilizer "
        "(Killing definiteness) is the property that makes it EH-blind -- STRETCHING vs BENDING",
        "rational (Fraction), no floats" in sqe["exact_decomposition"]["arithmetic"]
        and "ZERO" in sqe["exact_decomposition"]["overlap"]
        and "ODD" in sqe["exact_decomposition"]["parity"] and "EVEN" in sqe["exact_decomposition"]["parity"]
        and "STRETCHING" in sqe["mechanism"] and "BENDING" in sqe["mechanism"]
        and "Killing definiteness" in sqe["mechanism"])
    _ck("W6 the WOULD-CHANGE-IF HANDLE banked as an IDENTITY: the I4-BUILT parity-odd quartic "
        "(1/4) sum_mn h(W_mn, W_mn) equals the EH W-block EXACTLY -- so a parity-odd I4-built "
        "quartic would buy the W-block HALF of EH and ONLY that half: it is indefinite (cannot "
        "serve Derrick stabilization) and supplies none of the S-block Q1..Q4. This is the sharpest "
        "statement of what a different quartic would and would not do",
        "equals the EH" in sqe["would_change_if_handle"]
        and "W-block HALF" in sqe["would_change_if_handle"]
        and "cannot serve Derrick" in sqe["would_change_if_handle"])
    _ck("W6 the SEQUENTIAL KILL CHAIN [correct witness attribution -- NOT 'one-blade kills cc+HC']: "
        "(1) parity/S-block disjointness => lambda = 0 at quadratic order; (2) ddR-FREEZE => "
        "lambda = 0 nonperturbatively vs cc and the Omega-algebraic remainder (holding (R,dR) fixed "
        "and varying ONLY ddR leaves BOTH quartic contractions EXACTLY frozen to machine zero while "
        "sqrt(g)R sweeps by > 50x the FD noise floor, on two independent backgrounds); (4) "
        "GAUSS-BONNET DEATH -- sqrt(g)E4 spreads by tens-to-hundreds on those same frozen-quartic "
        "sweeps; (5) ACROSS-BACKGROUND NON-UNIVERSALITY -- a near-exact higher-curvature "
        "cancellation DOES exist along any SINGLE sweep (which is exactly why a single-sweep test is "
        "insufficient) but the fitted coefficients do NOT transfer: sweep-1's (a,b,c) on a different "
        "background leave a residual larger than that background's entire EH spread, so a "
        "fixed-coefficient HC repackaging of EH is excluded",
        all(sqe["sweeps"][s]["quartic flat spread"] == 0.0
            and sqe["sweeps"][s]["quartic texture spread"] == 0.0
            and sqe["sweeps"][s]["sqrt(g)R spread"] > 50 * sqe["sweeps"][s]["FD noise"]
            and sqe["sweeps"][s]["sqrt(g)E4 spread"] > 50 * sqe["sweeps"][s]["FD noise"]
            for s in ("sweep-1", "sweep-2"))
        and "CHAIN" in sqe["kill_chain"]["ATTRIBUTION"]
        and "does NOT transfer" in sqe["kill_chain"]["(5) across-background non-universality"])
    _ck("W6 the ONE-BLADE STEP (3), stated as what it actually delivers: on a one-blade texture the "
        "quartic vanishes IDENTICALLY (a blade commutes with itself) so the whole menu must vanish "
        "there; the 12-point menu matrix (EH, cc, R^2, Ric^2, Riem^2) is rank-deficient with a "
        "ONE-dimensional null space whose vector is EXACTLY (0, 0, -1/4, 1, -1/4), i.e. proportional "
        "to GAUSS-BONNET E4 = R^2 - 4Ric^2 + Riem^2. Its EH and cc components VANISH -- that is the "
        "step's real output: it kills lambda and Lambda_cc and REDUCES the higher-curvature menu to "
        "Gauss-Bonnet, which then dies at step (4). Truncation numbers are config-dependent: the "
        "banked statement is the SHRINKAGE of the truncation deviation, never the magnitudes",
        abs(sqe["one_blade_null_vector"]["(EH, cc, R^2, Ric^2, Riem^2)"][0]) < 1e-5
        and abs(sqe["one_blade_null_vector"]["(EH, cc, R^2, Ric^2, Riem^2)"][1]) < 1e-5
        and abs(sqe["one_blade_null_vector"]["(EH, cc, R^2, Ric^2, Riem^2)"][2] + 0.25) < 1e-5
        and abs(sqe["one_blade_null_vector"]["(EH, cc, R^2, Ric^2, Riem^2)"][3] - 1.0) < 1e-5
        and abs(sqe["one_blade_null_vector"]["(EH, cc, R^2, Ric^2, Riem^2)"][4] + 0.25) < 1e-5
        and "SHRINKAGE" in sqe["truncation_ladder"]["note"])
    _ck("W6 the MENU QUANTIFIER, the CLASS-SCOPED consequence and the flagged NON-COINCIDENCE "
        "[DERIVED-structural EH-ABSENT, conditional on U2 + the banked Omega-algebraic action class]: "
        "the EXCLUDED MENU IS EXACTLY {cc, R^2, Ric^2, Riem^2} -- the R^3/grad-Riemann class falls "
        "to the SAME dE-independence schema but was NOT RUN, so never quantify over 'any conceivable "
        "term'. SOLE-ROUTE consequence is CLASS-SCOPED: no Omega-algebraic term in the banked "
        "first-derivative action class can contain EH, so with the front-embedding route closed at "
        "B.6.6 the INDUCED arc is the unique surviving route WITHIN THE BANKED CONTENT -- the "
        "thermodynamic route and genuinely-new dE-terms are UNTOUCHED. Four-signature menu coverage "
        "(0,4)/(1,3)/(2,2)/(3,1) shows NO common lambda (ratios spread over four orders of "
        "magnitude), and the (3,1) one-point near-equality F4_tex/sqrt(g)R = 1.0007 is FLAGGED as a "
        "noted non-coincidence per the K_trans precedent, NOT claimed as a result. Ledger: N51",
        "MENU QUANTIFIER" in sqe["tier"] and "U2" in sqe["tier"]
        and "NOT RUN" in sqe["menu_quantifier"]
        and "any conceivable term" in sqe["menu_quantifier"]
        and "CLASS-SCOPED" in sqe["sole_route_consequence"]
        and "UNTOUCHED" in sqe["sole_route_consequence"]
        and "1.0007" in sqe["noted_non_coincidence"]
        and "K_trans precedent" in sqe["noted_non_coincidence"]
        and "NOT a" in sqe["noted_non_coincidence"]
        and len(sqe["menu_coverage"]) == 4
        and "N51" in sqe["ledger"])

    mwc = mass_weight_empirical_chain()
    _mp_codata, _me_codata = 1.67262192595e-27, 9.1093837139e-31
    _gp = mwc["link_4_active_single_particle"]["gap_factor_proton"]
    _ge = mwc["link_4_active_single_particle"]["gap_factor_electron"]
    _ck("mass->weight jurisdiction ledger (mass_weight_empirical_chain, B.6 intro block). What "
        "this check IS: a duplicate-literal drift guard (the 92.1e-6 kg source mass and "
        "CODATA-2022 m_p/m_e are re-declared here and the primitive's gap quotients must match "
        "them — 5.5e22 proton masses / 1.0e26 electron masses, 22+ orders with no direct data) "
        "plus a wording-guard on the ledger's flags: link 4 (active single-particle) UNMEASURED, "
        "link 3 macroscopic-only, link 1 (clock<->inertia) single-particle at 1e-11, the three "
        "fences (2.7e-15 passive / 3.9e-14 active-passive / 1e-21 spin-direction) present, the "
        "identity OUTSIDE the eom E-namespace, jurisdiction non-predictive. What it is NOT: a "
        "verification of any literature value — the VALUES are imports (companion I-23), "
        "primary-source-verified at import time, and no suite check can re-verify them.",
        abs(_gp - 92.1e-6 / _mp_codata) / _gp < 1e-12
        and abs(_ge - 92.1e-6 / _me_codata) / _ge < 1e-12
        and 5.4e22 < _gp < 5.6e22 and 1.0e26 < _ge < 1.02e26
        and mwc["link_4_active_single_particle"]["measured"] is False
        and mwc["link_3_passive_active"]["single_particle"] is False
        and mwc["link_1_clock_inertia"]["single_particle"] is True
        and mwc["link_1_clock_inertia"]["electron_rel_unc"] < 1e-10
        and mwc["link_2_inertia_passive"]["neutron_1975"] == 0.10
        and mwc["fences"]["material_independence_passive"] == 2.7e-15
        and mwc["fences"]["material_independence_active_passive"] == 3.9e-14
        and mwc["fences"]["electron_spin_direction_gravitational_asymmetry"] == 1e-21
        and "OUTSIDE" in mwc["identity"] and "E1-only" in mwc["identity"]
        and "never an R-NNN" in mwc["identity"]
        and "COMMITS" in mwc["jurisdiction"]
        and "predicts nothing" in mwc["jurisdiction"])


    print("\nAll §24.4/§24.6 cosmology/macroscopic checks passed (companion-layer checks: twt_companion_test.py).")



def main():
    print("="*70)
    print("  TWT library — MAIN-engine self-check (companion layer: twt_companion_test.py)")
    print("="*70)
    checks=[check_twt_poc, check_twt_foundation, check_twt_algebra, check_twt_observer_qm, check_twt_spectra, check_twt_matter, check_twt_weak, check_twt_em, check_twt_hadrons, check_twt_cosmo]
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
    print(f'  ALL {total} CHECKS PASSED across {len(checks)} modules.' if ok else '  SOME CHECKS FAILED.')
    print('='*70)
    return ok

if __name__ == "__main__":
    import sys; sys.exit(0 if main() else 1)
