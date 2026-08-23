# Time-Wave Theory — Foundational Paper V3, Companion File

*Companion to `TWT_foundational_paper.md` (V3). This file consolidates all annexes, the
back-of-book bookkeeping (Result Index, Dependency Graph, Engine ↔ Paper Map, Pending-Values
Registry), the geometric-reinterpretation catalog, the methodology principles, the development
log, the stable-spectrum enumeration, the wave-phase stability ladder, and the bibliography.
Unconventional but practical: everything a reader might want beyond the main narrative is here.*

*Yaer Aharon Haddad Fennech · Independent Researcher · hfyaer@gmail.com*
*Engine, verification suite, and all three documents: https://github.com/yaerhf/TWT —*
*every engine cite in the Result Index and the Engine ↔ Paper Map below resolves to a primitive*
*in `twt.py` there, and `python twt_test.py` runs the checks those cites refer to.*

> **Which document a reference resolves in.** Every `§A`–`§E` reference in this file, and every
> `(R-NNN)` marker, resolves in **`TWT_foundational_paper.md` — the V3 instance dossier**, whose
> Part A–E structure and section numbering are unchanged. The family-level entry document is the
> **Core paper**, `TWT_core_paper.md`; it carries no result numbers and no inline tiers, and it
> cites the dossier by section. This file stays authoritative for tiers, dependencies, engine
> cites and premise rows wherever any of the three differ.

---

# Contents

- [Diff of intent (V2 → V3)](#diff-of-intent-v2--v3) — what V3 changed and why.
- [Section 1 — Result Index](#section-1--result-index) — every R-NNN result with tier, engine primitive, target section, dependencies.
- [Section 2 — Dependency Graph](#section-2--dependency-graph) — layered picture of axioms → algebraic → dynamical → deep gates.
- [Section 3 — Engine ↔ Paper Map](#section-3--engine--paper-map) — cross-reference between `twt.py` primitives and paper sections.
- [Section 4 — Pending-Values Registry](#section-4--pending-values-registry) — open items by kernel object.
- [Section 5 — Geometric reinterpretation catalog](#section-5--geometric-reinterpretation-catalog-nine-items) — nine items.
- [Section 6 — Methodology principles](#section-6--methodology-principles-seven) — seven principles with canon-successor notes.
- [Section 7 — Development log](#section-7--development-log-v1--v2--v3) — V1 → V2 → V3 history + review-round catches.
- [Section 8 — Stable-spectrum enumeration](#section-8--stable-spectrum-enumeration-the-over-production-test) — the over-production test (B, L) table.
- [Section 9 — Wave-phase stability ladder](#section-9--wave-phase-stability-ladder-20-states-across-9-orders-of-magnitude) — 20 states, Rungs 0–3, π⁰/π± discriminator.
- [Section 10 — Bibliography](#section-10--bibliography) — consolidated citations.
- [Section 11 — Paper 2 agenda](#section-11--paper-2-agenda) — what the next paper would derive (moved from paper §E.4.4).
- [Section 12 — Closability classification](#section-12--closability-classification-2026-07-02) — which open items can close, how, and what is walled off; per-item closure leads (2026-07-02 assessment).
- [Section 13 — Import Registry](#section-13--import-registry-2026-07-05) — every load-bearing external theorem: premises, level applied (substrate vs inside-frame), ontology status, retirement handle. **Maintenance mandatory on import** (methodology principle 8; canon §2).
- [Section 14 — Core / Instance bookkeeping](#section-14--core--instance-bookkeeping-the-family-split) — which results are family-side and which belong to Instance V3; the falsifier levels; the family-tree pointer; the dated history of the split (the paper body is history-blind, so it lives here).

---

# Diff of intent (V2 → V3)

For any future editor or fresh-context agent reading this file: the structural moves V3 makes
that V2 did not.

| | V2 | V3 |
|---|---|---|
| **Reading order** | Ontology → Cl-algebra → Substrate → Observer → Matter → Gauge → Cosmology | Ontology → **Spine results** → Matter/gauge → Substrate → Cosmology/frontier |
| **Hook position** | Lorentzian signature at line 950; QM postulates at line 1100; gravity sign at line 2629; α at line 2720 | All four in Part B (the second part the reader sees); α and the α-sibling g promoted to §B.5b as a parameter-economy hook |
| **Tier tags** | ~152 inline `[DERIVED]`/`[FRAMING]`/`[CANDIDATE]` tags scattered through prose | Removed from body; live in Result Index (Section 1 of this file) |
| **Result numbering** | Implicit (cited by §number + verbal handle) | Explicit `(R-NNN)` markers; equation-style |
| **V1→V2 history** | 5 "V2 re-audit findings" blocks in body + ~186 inline editor's notes | Consolidated into Section 7 (Development log) |
| **Cl-algebra machinery** | Part II (lines 246–490), forced on the reader before any payoff | A.5 carries the minimum; full algebra at Part D |
| **§24 cosmology** | All at the back as "Part VII" | Hook-worthy pieces (arrow of time, three asymmetries, Volovik, macroscopic L/Q split) in Part B; frontier pieces (Λ residual, dark matter) in Part E |
| **Falsifiers** | §25.2 (V2 Phase M consolidation) | §E.3 (same consolidation, same content) |
| **Epistemic gradient** | Mixed: solid results late, open frontier scattered | Monotonic: SOLID early → SPECULATIVE late |
| **Companion bookkeeping** | None; V2 had `TWT_V2_*` standalone files but the paper stood alone | This companion file consolidates all Result Index / Dep Graph / Engine Map / Pending-Values content into one out-of-paper location for reader convenience |

V3 is not a re-derivation. **All V2 physics is preserved.** What changes is the order, the inline
editorial weight, and how tier discipline is enforced (Index, not tags).

---


# Section 1 — Result Index

*Flat lookup: every R-NNN result with tier, engine primitive, target section, dependencies, what depends on it.*


*Version 3 · Phase α draft · 2026-06-30.*
*Flat lookup table for every numbered result in `TWT_foundational_paper.md`. The body of V3
carries `(R-NNN)` markers; this file resolves each marker to its tier, engine primitive, source
section, and dependency edges. The Dependency Graph (Section 2 below) renders the
same content as a structural picture.*

---

## How to read this file

Each row is one numbered result. Columns:

- **ID** — `R-NNN`. Cited in the V3 body as `(R-NNN)`.
- **Statement** — one-line summary of what the result asserts.
- **Tier** — DERIVED-A (algebraic / exact identity, engine-verified), DERIVED-P (physically forced
  by an explicit substrate argument), DERIVED (computed from the substrate, qualifier inline),
  DERIVED-STRUCTURAL (general substrate structure, no single closed identity), FORCED (algebra /
  substrate leaves no alternative), INPUT (counted empirical constant), FIT (parameter tuned to
  data), CALIBRATED (single-input fit with downstream consequences), CANDIDATE (proposed
  mechanism, not derived), FRAMING (structural identification, value open), GATED (magnitude
  blocked on an open gap; engine raises).
- **Engine** — primitive name in `twt.py`. Multiple primitives separated by `+`. `—` if no direct
  engine cite (paper-only / kinematic).
- **§** — target V3 section (`A.1` ... `E.6`). `Annex` if the result lives in an annex.
- **Deps** — other R-NNN this result depends on. Order is logical, not strict.
- **Used by** — other R-NNN that build on this one.
- **Notes** — tier qualifications, scope, open gates.

**Axioms** carry IDs `A-1a`, `A-1b`, `A-1c`, `A-2`, `A-3`, `A-1*`, `A-2*`. They are not
derived; they are listed in the *Axioms* table at the top.

---

## Axioms

| ID | Statement | Tier | § | Notes |
|---|---|---|---|---|
| A-1a | 4D Euclidean substrate `(ℝ⁴, g)`, positive-definite metric | AXIOM | Opening | True ontological premise. |
| A-1b | D4 cell lattice realization | INPUT-promoted-to-structural | Opening, D.3 | Empirically motivated by D4 being the densest 4D packing (kissing 24); not derived inside the framework. |
| A-1c | J + D coupling structure on D4 NN bonds | FRAMING (structure) + INPUT (ratio) | Opening, D.3 | Coupling structure = symmetric exchange on all 24 bonds + chiral DM on the 12 `e_4`-bonds. **This is a TRUNCATION PICK from the ten-constant driven-group menu (J:2 + D:2 + Γ:6 at `Stab(+e₄)`, frame-bilinear class; the pseudoscalar χ has allowed dimension 0 there) — family-tree S1c / V3-2, with the DM support pick at V3-2a. Parity does NOT exclude Γ (it is parity-EVEN), and the `e₄`-only DM restriction is a pick, not forced: the second (spatial-bond) `D` is symmetry-allowed at the same group, and its exclusion candidate is the drive-origin story (#1-gap-routed). The old "the unique pair allowed by parity" wording is struck as known-false** (menu theorem 2026-08-17; J,D/Γ rework 2026-08-20/21). Ratio `D/J ≈ 0.79` is INPUT, calibrated to leptons, conditional on (a) the `√m = r²` mass-measure choice and (b) the `A = J, B = D` ansatz. The `cos`/`sin` **parity assignment** of the ℤ₃ amplitudes (J, Γ → even; D, χ → odd) remains ASSERTED — the rework's own test of it was vacuous and is reported as such (negatives ledger N62, sub-note JD-5). |
| A-2 | Driven dynamics premise — the substrate is driven; EOM is the #1-gap placeholder | AXIOM-with-#1-gap | Opening, D.5 | Not on par with A-1a / A-3 in solidity. Gates absolute coupling magnitudes, masses, Θ_rel. |
| A-3 | Wavefront / signature locking — observers read `e_4` as time | AXIOM | Opening, A.2 | The Lorentzian signature follows (R-014, R-015). |
| A-1* | Matter = defect (canon §0) | AXIOM | Opening, A.3 | Matter is topologically protected pattern; mass is meta-time rotor frequency. Inside-positive / outside-hole are frame images. |
| A-2* | Working frame is outside the wavefront (canon §0) | AXIOM (method) | Opening, A.2 | Inside-frame for data, outside-frame for derivation. |

---

## Part A — The Picture

| ID | Statement | Tier | Engine | § | Deps | Used by | Notes |
|---|---|---|---|---|---|---|---|
| R-001 | Wave-train as succession of S³ wavefronts advancing along `e_4` | DERIVED-STRUCTURAL | — | A.1 | A-1a, A-3 | R-002, R-043 | The wave is `e_4`-propagating; observers are mechanically locked to a primary resonant wavelet. |
| R-002 | S³ wavefront topology; π_3 of the 4D-orientation class = ℤ × ℤ classifies matter | DERIVED-A | pi3_orientation_class_two_windings (the ℤ×ℤ; chiral factorization + the dim-6 census) + pi3_S3_integer_completion (the lepton-sector π_3(S³) = ℤ and the baryon integer-completion facts) | A.2 | R-001, R-102 | R-006, R-009, R-052 | **Target = the medium's local state space** (R-102): the 4D-orientation class, six real parameters, inherited unchanged by the continuum field. **COVER-BLIND** — the two windings do not depend on where the ℤ₂ sign lives (family tree node LS-ℤ₂, open), since covering maps are isomorphisms on π_n for n ≥ 2. The lepton subgroup `exp(𝓛)` and the baryon coset `Spin(4)/Spin(3)` are WINDING targets *inside* that state space, not the state space itself (A.2 aligned to C.1.3). Two ℤ factors come most directly from the chiral factorization Spin(4) = SU(2)_+ × SU(2)_−. The framework's working basis is the L-orbit / Q-orbit decomposition (by e_4-content), which is DIFFERENT — `𝓛 ⊕ 𝓠 ≠ SU(2)_+ × SU(2)_−` as decompositions of so(4). The relabeling from chiral basis (n_+, n_−) to orbit basis (n_𝓛, n_𝓠) is justified by the symmetric-pair / fibration bridge of A.5.2: `Spin(3) ↪ Spin(4) ↠ S³_𝓠 = Spin(4)/Spin(3)` with π_2(Spin(3))=0 gives `0 → ℤ → ℤ × ℤ → ℤ → 0`, so (n_𝓛, n_𝓠) is a change of basis of π_3(Spin(4)). Leptons wind into the diagonal Spin(3) (subgroup); baryons wind into the coset S³_𝓠 (coset). Coset-respecting relabeling of a chiral counting, not identification of the two splits. |
| R-003 | Working-frame discipline: outside-frame for derivation | METHOD | matter_stability_outside_frame | A.2 | A-2* | (all derivations) | Inside view used only to import data. |
| R-004 | Matter as defect — topological winding in rotor field, not piece of stuff | DERIVED-STRUCTURAL | matter_stability_outside_frame | A.3 | A-1*, R-001 | R-005, R-006, R-016, R-039 | Load-bearing throughout. Canon §0 statement. |
| R-005 | Defect's two faces (spatial winding + meta-time rotor) coupled by I_4 Hodge duality | DERIVED-STRUCTURAL | I4_maps_L_to_Q | A.3 | R-004, R-010 | R-007, R-053 | The two faces are not independent observables.  Sector-split (2026-07-02 sweep, R-127/R-128): the observer-visible winding↔mass-phase-axis relation is identity in L (lepton), I₄-dual in Q (quark); R-005's coupling is substrate-level. |
| R-006 | Topological stability of winding integer (cannot deform to vacuum) | DERIVED-A | pi3_S3_integer_completion | A.3 | R-002, R-004 | R-054, R-084, R-089 | π_3(S³) = ℤ for baryons; Hopf invariant for leptons. |
| R-007 | Mass = meta-time rotor frequency `m = ω` | DERIVED-STRUCTURAL | wave_E_complex_structure + wave_E5 | A.4 | R-005, **A-2 (because the rotor frequency is SUSTAINED BY THE DRIVE — the Section-2 gloss's own content, which is drivenness = Core S5/A-2, not A-1c's coupling content)** | R-008, R-017, R-038 | Half-angle convention forced by spinor inheritance. **A-1c edge STRUCK (J,D/Γ rework; keeper CONFIRMED, `VERDICT_KEEPER_2026-08-21.md` collision 2).** §A.4 contains no occurrence of J, D, DM, bond or canting; both engine cites are bond-free; the row's own Section-2 gloss named drivenness, not the couplings. Re-typed rather than bare-struck (meta-observer claim 9): the true parent is A-2. Consequence: the mass ontology is Core-side, free of the S1c truncation pick. |
| R-008 | Quarks are decomposition-components of one baryon defect (NOT independent objects that happen to be bound); the mass-bearing object is the baryon | DERIVED-STRUCTURAL | single_quark_no_rest_mass_axis | A.4 | R-007, R-004, R-053 | R-051, R-085, R-091a | V2 §3.2 ontology. Per-flavour MS-bar "quark masses" remain *indicators* of facet structure, never *verifiers* of standalone-quark predictions (canon §5). Reframed in V3 from V2's "quarks have no mass" — the cleaner statement is that quarks are not the kind of object that has mass, because they are not independent objects in the first place. |
| R-009 | L-orbit `{e_{12}, e_{13}, e_{23}}` and Q-orbit `{e_{14}, e_{24}, e_{34}}` orthogonally decompose grade-2; the pair `so(4) = 𝓛 ⊕ 𝓠` carries a symmetric-pair Cartan structure `[𝓛,𝓛] ⊆ 𝓛, [𝓛,𝓠] ⊆ 𝓠, [𝓠,𝓠] ⊆ 𝓛` (𝓛 = isotropy of e_4, exp = diagonal Spin(3); 𝓠 = coset complement, exp not a subgroup, hosts S³_𝓠 = Spin(4)/Spin(3)); fibration `Spin(3) ↪ Spin(4) ↠ S³_𝓠` bridges chiral and orbit bases of π_3(Spin(4)) = ℤ × ℤ | DERIVED-A | L_Q_orthogonal_decomposition + is_L_bivector + is_Q_bivector + L_algebra_su2_closure + pi3_orientation_class_two_windings (the `ℤ × ℤ` the fibration bridges the two bases of — this row computes the decomposition, not the count) | A.5.2 | A-1a | R-002, R-052, (many downstream) | Both 3-dim bivector triples; both square to −1. Engine-banked decomposition; the symmetric-pair Cartan relations and the fibration framing are stated explicitly in V3 prose (V2 left the relabeling implicit). |
| R-010 | Pseudoscalar `I_4 = e_1 e_2 e_3 e_4`; `I_4² = +1`; Hodge map L ↔ Q | DERIVED-A | I4_squared + I4_maps_L_to_Q + duality_map + hodge_star | A.5 | R-009 | R-005, R-019, R-080, R-090 | A real duality, not a complex unit. |
| R-011 | Rotor sandwich half-angle: `R = exp(θ B/2)`, `R(2π) = −1` on spinors | DERIVED-A | exp_unit_bivector + half_angle_overlap | A.5.5 | R-009 | R-025, R-027 | One-sided action on spinors gives half-angle; two-sided on vectors gives ordinary angle. |
| R-012 | Spinor minimal left ideal `𝒮 = Cl(4,0) · s_0`, `s_0 = (1+e_4)/2` idempotent | DERIVED-A | s0 + is_idempotent + spinor_real_dof | A.5.4 | A-1a | R-024, R-026, R-095 | Real dim 8, quaternionic dim 2. |
| R-012a | Cl(4,1) extension: `e_5² = −1`, central `E = I_4 · e_5` with `E² = −1` supplies the global geometric complex unit (external U(1) phase); native formalism is `Cl(4,0) + ℍ`; `e_5` grounding rule | DERIVED-A | wave_E5 + wave_E_complex_structure + spatial_vs_phase_partition + cl41_grounding_litmus + cl41_phase_is_external_u1 + cl41_idempotents_note | A.5.6 | R-010, R-012 | R-007, R-035a, R-094, R-095 | A Cl(4,1) construction is grounded iff its `e_5`-content reduces to PHASE in the Cl(4,0)+ℍ picture (canon §5 guardrail). Introduced in A.5.6; full at §D.1. |

---

## Part B — Spine results

| ID | Statement | Tier | Engine | § | Deps | Used by | Notes |
|---|---|---|---|---|---|---|---|
| R-013 | `γ⁰ := e_4, γʲ := e_4 e_j` satisfy Cl(1,3) Dirac relations `{γ^μ, γ^ν} = 2η^{μν}` | DERIVED-A | gammas + gamma0_gammaj_reduces_to_ej | B.1 | A-3, R-009 | R-014, R-017, R-026 | Engine-verified directly. |
| R-014 | Cl(4,0) ≅ Cl(1,3) ≅ M₂(ℍ) — the wavefront isomorphism lands on a nondegenerate Lorentzian partner, not the split (2,2) | DERIVED-A for the algebra identity and the (2,2) exclusion | cl_dimension | B.1 | R-013 | R-015, R-038 | **Scope corrected 2026-07-30.** The old cell read "The Lorentzian signature is forced" — flatly, without the conditioning canon actually carries: the signature is an INPUT *placement* on `e_5`, and the observer's reading is forced only *given* that placement. What is DERIVED-A is the substrate identity `Cl(4,0) ≅ M₂(ℍ)` (Bott) and that `φ` lands on a nondegenerate Lorentzian partner rather than the split one — the one-plus-three pattern of generator squares is convention-independent. Which real algebra names "observed spacetime" is NOT: `(+,−,−,−)` presents it as `M₂(ℍ)`, `(−,+,+,+)` as `M₄(ℝ)`, **with `Spin(1,3) = SL(2,ℂ)` acting identically in either** (V1 §12.4's concession, restored to §B.1.2 in the same pass; the glossary row and N56 already recorded the convention-sensitivity). Menu of presentations derived, presentation conventional, no pick for nature to make — and this presentation menu is a distinct object from R-145's texture-metric signature menu (N56: no map between the two Lorentzian faces). Still one of the two cleanest spine results at its corrected scope — the correction removes an over-claim, not the result. |
| R-015 | Lorentzian signature of observed spacetime is algebraic shadow of wavefront-locked observer in Euclidean substrate | DERIVED-A | gammas + cl_dimension | B.1 | A-3, R-013, R-014 | (paper headline) | Engine-verified. Two inputs: algebra fact + observer stipulation; both labeled. |
| R-016 | Matter-as-defect Lorentz protection: one substrate, one light-cone | FRAMING + removed-falsifier + structural identification (**cooled 2026-07-27** from DERIVED-STRUCTURAL to match the engine's own self-tag on `equivalence_principle_protection`: "NOT a dynamical EP derivation") | equivalence_principle_protection + matter_stability_outside_frame + d4_lattice_lorentz_violation_orders | B.1, B.6 | R-004 | R-039, R-040, R-165 | Defuses Collins-2004 radiative naturalness obstacle. Offensive win, not defensive tuning. **SCOPE, named 2026-07-27 (R-165):** covers **dimension-four relative-boost** LV only. It does NOT reach rotational anisotropy (that is D4's job — and D4 closes it to dim-8) and it does NOT reach the rotationally invariant **dimension-six** residual `η⁽⁴⁾ p⁴/M²_Pl` (equivalently `c·p⁴/Λ²`), which is neither a relative-boost observable nor an anisotropy and is #1-gap GATED. The pre-2026-07-27 gloss "the two protections leave the residual at dimension six" conflated those two objects; see VG-6, §E.3.5(4), N52. |
| R-017 | Klein–Gordon from 5D hyperbolic master by Fourier reduction at `k_4 = m` | DERIVED | wave_E_complex_structure | B.2 | R-007, R-013, R-123 | R-024, R-026 | Identifies rest mass with `e_4`-Fourier label. Engine support hardened 2026-07-02 by R-123: the consuming identification = R-123's derived restriction identity ∧ its named residue (ii) (one-particle sector at k_4) — previously the "m = k_4" identification existed in the engine only as a docstring string. |
| R-018 | Lorentz generators K_j = (1/2)e_j (non-compact), J_i = −(1/2)e_{jk} (compact); so(1,3) closure | DERIVED-A | boost + rotation + so13_closure_signs | B.2 | R-013 | R-019 | Bulk's compact so(4) becomes observer's non-compact so(1,3) via φ. |
| R-019 | Thomas precession from algebra: `[K_i, K_j] = −ε_{ijk} J_k` | DERIVED-A | thomas_KK | B.2 | R-018 | — | The minus sign is the signature of so(1,3) vs so(4). |
| R-020 | Born subspace `{1, B}` forced by centralizer intersection in Cl⁺(4,0), not stipulated | DERIVED-A | born_subspace_one_B_forced | B.3 | R-009, R-012 | R-021, R-023 | (W) ∩ (S) ∩ (E) = `{1, B_a}` — engine-exact intersection. |
| R-021 | QM Postulate 1: complex Hilbert space from transverse bivector plane | DERIVED | born_subspace_one_B_forced | B.3 | R-020 | R-022, R-023, R-024, R-166 | `i = B`; standard L² inner product from grade-0 part of Cl product. |
| R-022 | QM Postulate 2: self-adjointness as `M̃ = M` (Clifford reversion) | DERIVED-A given (i) expectations real + (ii) ℂ-linear observables | self_adjointness_from_one_B_projection | B.3.2 | R-021, R-166 | R-023 | Conclusion CONFIRMED, derivation REPLACED (review item III-13, 2026-07-29): "requiring reality" of `⟨φ̃ M̂ ψ⟩_0` is vacuous in a real Clifford algebra, and the grade-0 part is identically blind to the anti-self-adjoint part of `M̂`. The forcing condition is R-166 `⟨ψ̃ M̂ ψ⟩_B = 0`, whose solution space is exactly the reversion-fixed subspace. |
| R-023 | QM Postulate 3 (Born rule): squaring forced even-power by chirality symmetry | DERIVED structurally (even-power); the EXPONENT is upgraded by R-160 from plausibility-modulo-degree to a theorem given (F1–F4) + import-exempt Gleason | `ecarrier_common_mode_certificates` (leg 4 — the carrier-background reference face) | B.3 | R-020, R-021 | R-027, R-160 | Not a Gleason re-derivation: the framework supplies Gleason's hypotheses (R-160), it does not re-prove the theorem. **CARRIER-BACKGROUND REFERENCE NOTE (RUL-035, K-O1 keeper C1 precision wording):** on the ruled costed carrier the reverse-referenced overlap factorizes exactly to `cos(k_c x₄)·z⁽⁰⁾` per channel — amplitudes and ΣP scale by cos/cos² while probability RATIOS are exactly invariant (common-mode cancellation), with a 0/0 degeneracy on the comb `x₄ = (2n+1)π/(2k_c)`; the RULED adjoint `t = α₅∘reverse` removes all three (constant reference). RULED: the observer-side reference operation on carrier backgrounds is `t`, rest-frame-scoped; `t ≡ reverse` on Cl(4,0)/trivial backgrounds so nothing here recomputes; boost extension = the dictionary (RUL-034). Scope: EVERY reverse-referenced observer-side overlap (this row; R-160's F3 premise; R-027's half-angle overlap — inherit-notes at those rows). |
| R-024 | QM Postulate 4: **free** Schrödinger from the KG envelope, exact `mc²` cancellation — the `V ψ` term is ASSERTED, not derived | DERIVED (the free envelope reduction + the exact `mc²` cancellation) + NOT-DERIVED (the potential term: a modelling assumption about the fluctuation operator — scope added 2026-07-30, review item III-14) | — | B.3 | R-017, R-021 | — | Correct sign of kinetic term and of first relativistic correction. **Scope note (§B.3.4, §D.4.6):** the second variation about a soliton background is matrix-valued with symmetry zero modes (R-125/R-126) and is nowhere shown to reduce to a scalar `V(x)` on a one-component `ψ`; §D.4.6 does not construct that reduction — it declares the defect-linearization "not the route taken" and defers the soliton-fluctuation spectrum to Paper 2, treating `V` as a c-number background. §B.3.1(iii) records the matching state-space exposure (`ψ` is two-component; component-wise reduction needs the linearized operator to be `ℂ`-scalar at leading order — a named added premise). The hyperbolic parent is load-bearing, not a presentation choice: the Euclidean `□_4 Φ = 0` fails three ways — Hadamard-ill-posed elliptic Cauchy problem in `x_4`, complex energy `ℰ = mc² ± icp`, wrong-sign first relativistic correction. |
| R-025 | QM Postulate 5: spin-statistics from Spin(4) half-angle; fermionic Skyrmion quantization is SELECTION (not forced in bare SU(2)) | DERIVED + SELECTION | dirac_ideal_idempotent + skyrmion_collective_quantization_under_v2_3p2 + colour_z3_holonomy_cannot_source_fr_sign | B.3 | R-011, R-012 | — | Honest tier per V2 §14.6 W-LIVE-4 re-attack: three substrate routes all FAIL. 2026-07-02 (N35): closure route W1's finite-ℤ_3-holonomy instance closed-negative (DERIVED-generic group theory); W1 reduced to P2-4's induced-level question — SELECTION now protected by four engine-checked negatives. 2026-07-03 (R-141): the induced level answered at the PARITY level — ODD ⇒ the selection upgrades to INDUCED-given-(P1)+(P1b), conditional and revocable; the four negatives still protect all substrate-internal routes. 2026-07-03 (R-136): the selection gains a SECOND independent empirical anchor — the bosonic branch predicts a bound scalar `(0,0)` dibaryon ground state at `B = 2`, refuted by the observed deuteron (evidence for the pick, not a derivation; shared (Q) premise). |
| R-026 | Dirac equation from KG factorization `𝒟 ψ = ±m ψ B` with right-acting `B`; equivalent to Hestenes form on the minimal left ideal | DERIVED | hestenes_Isigma3 + dirac_ideal_idempotent | B.3 | R-013, R-017, R-012 | — | Right-acting `B` is mandatory for `□ + m²`. |
| R-027 | Tsirelson bound `S = 2√2` from the ONE-SIDED rotor half-angle on the `Cl(4,0)` wavefront commutant | DERIVED-A (the half-angle identity `⟨ψ_a\|ψ_b⟩ = cos(Δθ/2)`, now carried on the `ℂ²` commutant wing — R-167) + **FRAMING** (the CHSH value itself: `bell_correlation` was retiered FRAMING 2026-07-29 on two named imports — the two-particle tensor product and the singlet) | tsirelson_S + chsh_S + half_angle_overlap + bell_correlation (itself FRAMING) | B.4 | R-011, R-023, R-167 | R-028, R-031 | **Row corrected 2026-07-29.** Two stale facts fixed: (a) the engine retiered `bell_correlation` to FRAMING in the N53 pass while this row still read a flat DERIVED-A citing it — engine↔companion drift of the phantom-cite class; (b) the title read "rotor-sandwich half-angle", but §B.4 states explicitly that the sandwich is the identity here and the half-angle comes from the ONE-SIDED action. Setting corrected in the same pass: the wing is `Z_{Cl⁺(4,0)}(e_4) ≅ ℂ²`, not the `ℂ¹` phase sector (R-167). Dimensional fingerprint of `S³ → S²` projection. **CARRIER-BACKGROUND INHERIT-NOTE (RUL-035):** the half-angle overlap is a reverse-referenced observer-side overlap — on the ruled carrier background it inherits R-023's reference face (factorization by `cos(k_c x₄)`, comb degeneracy; the ruled adjoint `t` removes it; → R-028, R-031 inherit through this row). Trivial-background content unchanged (`t ≡ reverse` there). |
| R-028 | Multipartite MK bound `\|M_n\| = 2^{(n+1)/2}`, engine-checked n=2-5 | DERIVED-A (the rotor-composition identity `E_n = ⟨∏_j exp(φ_j B)⟩_0 = cos(Σ_j φ_j)`, exact at every `n`) + **FRAMING** (its reading as an `n`-party MK value: the same two imports named on R-027 — the multi-particle tensor product and the GHZ state, neither constructed anywhere in TWT, N53) | mermin_klyshko_value + mermin_value | B.4 | R-027, R-167 | — | **Row corrected 2026-07-29 (rhetoric-residue sweep).** The row read a flat DERIVED-structural while §B.4.2 states the accurate reading is the engine's own *"a consistency confirmation, not a falsifier"*, scoped to *"n = 3, GHZ/symmetric class, optimal settings"*: all `n` rotors lie in the SAME plane `B`, so they commute and the correlation collapses to a one-line trigonometric identity — "there is no tensor-product structure here and no `n` parties in any state-space sense". The general-`n` value is the standard MK/GHZ maximum of the Bell literature, evaluated numerically at `n = 2`–`5`, not a general-`n` theorem proved in-framework. This mirrors R-027, whose CHSH value was retiered FRAMING 2026-07-29 on those same two imports; R-028 rides them through its dependency and was missed in that pass. **Engine↔companion drift, flagged not patched:** `mermin_value` and `mermin_klyshko_value` still self-tag `[DERIVED]` in `twt.py` while naming the consistency-confirmation scope in their own prose — a docstring correction is owed (docstrings are not asserted, so the harness cannot catch it). W (non-GHZ) class is a located construction gap (`w_state_located_gap`). |
| R-029 | `ρ_A = (1/2)𝟙` identity — no-signaling and non-separability are the same fact | DERIVED (standard QM identity; engine partial-trace check proposed, none exists yet) | — | B.4 | R-027 | R-030, R-031 | All structure drained into correlations; locally pure noise, jointly perfectly ordered. |
| R-030 | Bell-memory bridge: same `Im χ` governs decoherence and pair-memory | FRAMING + value-gated | im_chi_falsifier_budget_KSS_GW_macromolecule | B.4 | R-029 | R-119 | Canonical falsifier §E.3 VG-1. |
| R-031 | Selection foliation = comoving frame (testable corollary) | FRAMING + **consistency-check-testable, NOT a discriminating falsifier** (scope corrected 2026-07-30) | — | B.4 | R-029 | — | §E.3.1 rows 4–5 carry this result, and both were demoted 2026-07-30: a finite influence speed *"would also be inconsistent with quantum mechanics' exact predictions"* (V1 §25.7's parenthetical, dropped by V3 and restored at the row), so the measurement tests QM at least as much as it tests TWT — the framework is isomorphic to QM in this channel (import I-11) and inherits the verdict either way. The rows stay in the table as null-result consistency checks; they are not framework-vs-SM discriminators. |
| R-032 | Maxwell `∇F = J` in Cl(4,0); grade-1 source delivers Gauss + Ampère, grade-3 source = 0 delivers Faraday + ∇·B = 0 | DERIVED-A | maxwell_grade_structure + maxwell_four_laws | B.5 | R-009 | R-033, R-034, R-035 | Substrate origin: `J` is wavefront projection of L-orbit bivector winding. |
| R-033 | No magnetic monopoles: the grade-3 *source* of `∇F` vanishes because `J` is grade-1 only | DERIVED-A (the grade decomposition) + DERIVED-CONDITIONAL (the no-monopole verdict, on the winding-as-source identification) | maxwell_grade_structure | B.5.2 | R-032 | — | Note corrected 2026-07-28: **not** a pure algebraic forbiddance. The grade-3 slot is *not* empty as Clifford structure — `maxwell_grade_structure` returns four grade-3 components, and GA-EM with monopoles is `∇F = J − I_4 K` (Hestenes) with `F` still a bivector. It is empty because TWT identifies the only current as the grade-1 wavefront projection of bivector winding; a different source identification refills it (the re-attack handle). The engine cite covers the grade decomposition only — no primitive asserts the vanishing. Matches §B.5.2, §E.3 row 10, and Section 5 catalog item 4. |
| R-034 | Coulomb potential `V(R) = Σ_1 · Σ_2 / (4π R)`; like-repels, unlike-attracts | DERIVED | coulomb_potential + coulomb_sign_rule + coulomb_is_harmonic | B.5 | R-032 | — | Green's function in 3D. Two scope facts: (i) Poisson does NOT follow from `∇F = J` by differentiation (`∇` gives `∇²F = ∇J`, source differentiated, not `−J`); (ii) the `1/r` object is potential-like, NOT the Faraday bivector (Coulomb falls as `1/r²`); the symbol `J` denotes a grade-1 current at §B.5.1 and a bivector source at §B.5.3 — not the same object. |
| R-035 | Photon as L↔Q-bridging bivector strain mode; masslessness from topological winding-charge conservation (not EWSB) | DERIVED | photon_strain_mode | B.5 | R-032, R-009 | R-035a | EWSB-independent masslessness — topological. |
| R-035a | Fine-structure constant `α_em` as reactive grade-0 Clifford invariant — L↔Q reconversion strength `α-object = ⟨Σ̃_F · Γ_recon · Σ_L⟩_0`; Type-B (analytic in coupling, no `exp(−S)`) | DERIVED (ontology) + GATED (magnitude) | alpha_em_meaning + alpha_em_value (raises) | B.5b | R-035, R-012a | R-035b, R-035c | What α *is*, not what it equals. Magnitude #1-gap-gated via Im χ. |
| R-035b | `g` is α's algebraic sibling via `g² = 4πα / sin²θ_W = 4πα · (8/3)` with `sin²θ_W = 3/8` proven (R-082) — **at the `g_1 = g_2` CROSSING SCALE, so the `α` in it is the crossing-scale coupling, NOT `α_em(M_Z)`**; EW sector reduces to ONE #1-gap magnitude, not two | DERIVED-A (the algebraic sibling relation, AT the crossing scale) | weinberg_sin2 | B.5b | R-035a, R-082 | — | Parameter-economy hook. Three SM EW couplings collapse to one dial; same `Im χ` samples both. Engine cite covers the 3/8 only; the sibling relation is algebra given it. **Scope correction 2026-07-30 (review item III-20):** because it inherits `sin²θ_W = 3/8` the relation is scale-locked to the crossing; with the descent withdrawn (§C.4.5 table, §B.5b.2, N55) it makes NO numerical contact with the measured `α_em`. The parameter-economy content survives; the bridge to laboratory `α_em` does not exist. |
| R-035c | Length-ladder relations `r_e = α λ̄_C`, `a_0 = λ̄_C / α` ⇒ `r_e · a_0 = λ̄_C²` — **definitional arithmetic on the standard-QM length definitions**; the surviving TWT content is the ontological reading of `λ̄_C` (L-orbit soliton core scale) and `a_0` (resonant-cavity scale) as two configurations of one field | FRAMING (definitional; standard-QM arithmetic, not a TWT derivation; no parameter cost) | — (no engine primitive asserts the ladder) | B.5b | R-035a, R-055 | — | Demoted 2026-07-28 to match §B.5b.1. Withdrawn: "DERIVED-A", "from one geometric overlap", and "one geometric overlap underlies three independently measured lengths". `r_e ≡ α² a_0` and `λ̄_C ≡ α a_0` hold by the definitions of those lengths, so `α` cancels and the three lengths are three parametrizations of one scale, not independent measurements; the identity carries no substrate content. It is also **not** a value over-determination of `α`. Ontological reading: Section 5 catalog item 3. |
| R-036 | Rotor field as local Lorentz frame; substrate carries 4D frame with local Spin(4) symmetry | DERIVED-STRUCTURAL | — | B.6 | **R-102**, R-002 | R-037, R-039, R-042 | **A-1c edge STRUCK (J,D/Γ rework; keeper CONFIRMED, `VERDICT_KEEPER_2026-08-21.md` collision 2): a sweep residue.** The state-space repair rewrote this row to say the frame FOLLOWS FROM the six-parameter orientation, deleting the old `U(x) ∈ SU(2)` + canting-orientation + `e₄` assembly — and the canting orientation was the only thing A-1c ever supplied here — but left A-1c standing in the Depends column. Consequence: the gravity route (R-037, R-039, R-042, the Sakharov Λ and every dispersion consumer) is NOT conditional on the S1c truncation pick. Process finding recorded in the handoff: a pass that rewrites a row's content must re-verify its Depends column in the same pass. Spin(4) → Spin(3,1) after wavefront iso. The frame FOLLOWS FROM the six-parameter local orientation (R-102) — its six generators are already `so(4)` — rather than being assembled from a smaller object plus a canting direction and `e_4`. **Not usable as a source for R-002:** R-002 is a parent here, so deriving the two windings from this frame statement would be circular; R-002's target is the state space itself (R-102). |
| R-037 | Sakharov induced EH: `G_N⁻¹ ~ N_eff Λ²/(12π)`; `Λ_S = √(2π) M_Pl` (scheme) · `Λ_L = 1/a ∈ [0.39, 0.73] M_Pl` (which-Λ ruled 2026-07-30) | DERIVED-generic-given-4D | sakharov_induced_gravity + induced_G_bracket_mode_count + induced_G_only_monad_scale_enters + induced_G_leading_coefficient_mass_independent + induced_G_quadratic_divergence_from_4D | B.6 | **R-102** (N_eff = 6 IS dim of the local state space), R-036, A-1a | R-038, R-041 | The Λ² scaling is generic-given-4D, not a dynamical derivation. Absolute magnitude #1-gap-gated. **RESOLVED (2026-07-29) + WHICH-Λ RULED (coordinator, 2026-07-30).** History: the 2026-07-28 pass widened the bracket to `[0.13, 2.5] M_Pl` over (i) a determinate unit-convention fix — the engine's `Lambda_over_MPl = 4π` is against the REDUCED `M_red = M_Pl/√(8π)`, i.e. `2.51 M_Pl` non-reduced — and (ii) an apparently UNRECONCILED three-way `c_reg` disagreement. The 2026-07-29 pass RESOLVED (ii): ONE coefficient, `c_reg = 1/12` exactly in the proper-time variable; `≈1.8 = c_lat/12` is the SAME computation written in `Λ := 1/a` (R-163), and `~1` was a never-computed placeholder. The which-Λ ruling then SPLIT the symbol — `Λ_S = √(2π) M_Pl` (scheme; Sakharov/`G` bookkeeping only, no substrate information) vs `Λ_L = 1/a ∈ [0.39, 0.73] M_Pl` (every lattice-dispersion consumer; band from OA-LF-ii `κ ∈ [½, 2]` on `c_lat = 21.83`) — and RETIRED the wide bracket. Naive `η⁽⁴⁾` re-cut to `[1.9, 6.7]`, excluded 3–9 orders (VG-6). |
| R-038 | Newton 1/r law from Sakharov slow-motion limit; `T^{μν} = ρ u^μ u^ν` worldline stress | DERIVED | — | B.6 | R-037 | R-124 | Universal attraction from spin-2 sourcing by positive T^00. **Engine-tier mismatch flagged 2026-08-02 (keeper, I-23 round):** this row's DERIVED has no engine column while the content sits in the engine at FRAMING/CANDIDATE (`texture_matter_gravity_coupling`: "Newtonian sourcing FRAMING"; suite: "Explicit Phi(r)=-G_N*M/r remains CANDIDATE (N25)") — the companion-outranks-engine drift class. Reconciliation OWED (worklist): either back the row with the primitive and reconcile the tier down, or state why the engine tag does not govern. §B.6.1 now carries the linearized-point-defect-idealization clause; the §B.6 intro jurisdiction block (I-23) locates the empirical backing. |
| R-039 | `γ = 1` from matter-as-defect Lorentz protection | FRAMING + removed-falsifier + structural identification (**cooled 2026-07-27** to match the engine self-tag on `equivalence_principle_protection`, its sole engine backing) | equivalence_principle_protection | B.6 | R-016, R-037 | R-124, R-165 | One substrate, one light-cone. Inherits R-016's named scope: the protection is dimension-four relative-boost only. |
| R-040 | Induced G sign positive: spin-2 spectral positivity (`C_T > 0` by unitarity) ≡ substrate stability | DERIVED-sign-only | induced_G_sign_cross_check | B.6 | R-037 | — | Two-pillar unification — same physics in different language. Removes RF-1 falsifier. |
| R-041 | `ξ = 0` at leading order via Maurer–Cartan shift symmetry; catastrophic `ξ = 1/6` cancellation excluded | FRAMING + CONDITIONAL (engine self-tag: shift-symmetry lemma — substrate supplies the symmetry, QFT the implication) | sakharov_xi_minimal_coupling | B.6 | **R-102** (the six grade-2 fluctuation directions ARE the six parameters R-102 declares), R-037 | — | Goldstone-protected. Residual ξ ~ (f_π/Λ)² ~ 10⁻⁴⁰-class (2–8 × 10⁻⁴⁰ on the `Λ_L` band; reading-immaterial, not force-assigned by the 2026-07-30 ruling). Removes RF-2 falsifier. |
| R-042 | Texture tetrad `e^a_μ[R, ∂R]` structural geometry CLOSED conditional | DERIVED-STRUCTURAL-CONDITIONAL | texture_tetrad + texture_metric_candidate + texture_metric_diffinvariance + texture_metric_tt_graviton + texture_metric_vierbein + texture_matter_gravity_coupling | B.6 | R-036 | — | Metric `h_{μν} = ⟨Ω_μ I_4 Ω_ν⟩_0` forced up to one premise. |
| R-043 | Arrow of time as `+e_4` propagation; causality is the same fact | DERIVED-STRUCTURAL | — | B.7 | R-001, A-3 | R-044 | Not a separate postulate. |
| R-044 | **One** asymmetry (the causal arrow) from the wave's propagation direction `+e_4`; weak handedness rides an unpinned orientation plus the RH-singlet datum; the thermodynamic arrow is *reduced*, not derived | DERIVED-STRUCTURAL for the causal arrow ↔ `+e_4` identification; the weak-handedness leg is **NOT** a face of `+e_4` — it is settled by the `weak = SD` assignment (R-079, DERIVED-given-{A-P2 + RH-singlet datum}) on an orientation convention nothing banked pins; the thermodynamic arrow is NOT part of the derived count — it carries a **separate cosmological input**, the low-entropy past | — | B.7 | R-043, R-086 | — | **Count corrected 2026-08-23 (RUL-094 Q4, human ruling "RULE ONE"):** the previous cell read "**Two** asymmetries (causal, weak handedness) from one cosmological IC". The orientation reversal `x ↦ e_4 x e_4` **fixes `+e_4` exactly** while flipping `I_4` and exchanging the chiral factors (PROBE_K3, engine-computed), so one propagation direction is compatible with either handedness and weak handedness is not an observable face of `+e_4`. Ledger now: one from the wave's direction + the weak assignment's two named supports + one separate cosmological input. §B.7.2's heading and its three count-bearing sentences moved in the same pass. **Scope corrected 2026-07-30**, restoring V1 §24.2's own concession — *"the low-entropy past is a separate cosmological input — the framework reduces rather than fully derives the second law"* — which the V2 compression truncated (V2 archive line 2990 keeps only "the medium's irreversible response") and V3 inherited truncated. ~~One direction picks the causal and weak arrows~~ (superseded by the 2026-08-23 count correction above). The thermodynamic arrow's behaviour under `+e_4 → −e_4` depends on whether the low-entropy boundary is itself wave-direction-correlated: plausible, not derived. ~~Ledger: two from the IC + one counted bit + one separate cosmological input.~~ The 2026-07-30 cell read "One direction picks all three", and §B.7.2's heading read "Three asymmetries from one initial condition"; both were corrected in that pass. |
| R-045 | `c_meta = c` on average across the wavefront — a CONVENTION: a uniform global offset is removable by coordinate redefinition, so the statement's negation is unobservable and it makes no claim | FRAMING (a convention/definition, NOT a prediction — retagged 2026-07-30, review item III-23; earlier revisions read "DERIVED-STRUCTURAL + falsifier-testable", which over-read it, per §B.7.3) | — | B.7 | A-3 | R-047 | **The falsifier credit belongs to the DIFFERENTIAL version**, not to R-045: sector-dependent or epoch-varying `c_meta` IS observable and IS canonical falsifier §E.3 row 6, and that is where the section's testable claim lives. R-045 only makes the differential statement well-posed. (This companion's falsifier cross-references already credit the row as "differential `c_meta`"; the Class-4 knowability list already states the uniform offset has no signature.) |
| R-046 | Hubble radius as causal/crossover scale, not geometric radius of curvature | DERIVED-STRUCTURAL | — | B.7 | R-001 | R-119 | Topological S³ identification compatible with observed flatness if R_curv ≫ R_H. |
| R-047 | Volovik dissolution of CC problem: self-sustained medium has zero gravitating vacuum energy at equilibrium (`ε − μn = −P = 0`) | DERIVED + framing-of-residual | gravitating_vacuum_energy + lambda_resolution_structure | B.7 | R-037 | R-119 | Equilibrium value zero by Gibbs-Duhem identity. The residual is the driven-dissipative deviation — **magnitude only, value-gated**; the `ρ_vac ∝ H(t)²` epoch law is excluded (N54, §E.1.1), so the residual carries no derived epoch dependence. The equilibrium identity itself is untouched by that negative. |
| R-048 | Macroscopic COM bivector reduction: six conserved blades collapse to three on `P = 0, R_cm = 0` | DERIVED-A | macroscopic_LQ_split + worldline_bivector + polar_moment_of_inertia | B.8 | R-009 | R-049, R-050 | Central-force pairwise cancellation by Newton-3. |
| R-049 | L/Q split sorts micromatter species (R-009) AND macroscale conserved-invariant vs spent-integral — one algebraic split, two manifestations | FRAMING (the "one split, two manifestations" reading — the row's whole content; the DERIVED-STRUCTURAL half, the orthogonal `e_4`-partition itself, is **R-009's** content and is banked there, not here. Retiered 2026-08-18, external-review round-1 item 0.7; the FRAMING half was already carried from 2026-07-30, review item III-26) | macroscopic_LQ_split + L_Q_orthogonal_decomposition | B.8 | R-009, R-048 | — | **Standing: retained as a definitional observation, not a result-tier structural coincidence.** Nothing downstream leans on it — the Feeds column is empty, and R-050a's listing of R-049 among its antecedents is section-adjacent context (§B.8.4's argument uses no L/Q content), not a load-bearing input; verified by grep across paper, companion, engines, suites and ledgers on 2026-08-18. **Triviality caveat (§B.8.2, 2026-07-30):** the L/Q split IS the `e_4`-content partition, and BOTH sortings are graded by that same `e_4` — the macroscopic invariant is purely spatial by construction (§B.8.1 annihilates the `e_4`-mixed blades) and the lepton orbit IS the purely spatial triple — so their agreement is a definitional observation, not an independent structural coincidence, and NOT an over-determination. Substantive only if the macroscopic invariant lands in the lepton orbit for a reason beyond sharing that partition; no such argument exists in the corpus. Nothing downstream should lean on the two-manifestations reading. |
| R-050 | Sundman: triple collision forbidden unless `L = 0` | DERIVED-A-given-§B.6 | — | B.8 | R-048, R-034 | — | Cauchy-Schwarz on bivector norm + Newtonian far-field. |
| R-050a | Eulerian reframing — bodies are defect-features of one wavefront; the atlas-with-seams of the classical N-body problem is a projection artifact of field → feature extraction, not a feature of the dynamics; baryon-density integral bridges field to body positions | FRAMING | — | B.8 | R-004, R-049, R-006 | R-120 | Dynamics-coherent version depends on multi-defect well-posedness (§E.3 SC-1, structural-coherence condition). The ontology — bodies as features of one wavefront — is solid; the multi-defect Cl(4,1) wave equation with N back-reacting topological sources is a structural target. The **R-049** entry in this row's Depends column is section-adjacent context, not a load-bearing input: §B.8.4's argument uses no L/Q content (see R-049's standing note). |
| R-123 | Defect-ω → front-k_4 keystone bridge: a meta-time rotor restricted to the wavefront lock `x_4 = c_meta·τ_5` is x_4-periodic at `k_4 = ω/c_meta` (exact, axis-independent incl. central `E`; half-angle sign flip at 2π/k_4); two residues NAMED — (ii) one-particle sector AT k_4, (iii) `E → B_a` complex-unit hand-off | DERIVED-A (restriction identity) + FRAMING (residues ii, iii) | defect_rotor_frequency_reads_as_k4_on_front | B.2.1 | R-007, R-013, R-045 | R-017, R-125, R-127 | Banked 2026-07-02 (ledger N36; twt-reviewer HOLDS at the split tier). Hardens R-017's engine support — "m = k_4" previously existed only as a docstring string. Residue (ii) is the item's actual remaining gap (§D.4.6 soliton-fluctuation Paper-2 question); checked on generic non-special configurations per the Phase F lesson. WP-MASS-MEASURE chains 1/2/5 inherit. |
| R-124 | Charged-defect worldline EOM `ṗ = qF·u` + cyclotron readout `ω_c = qB/m` (WP-MASS-MEASURE chain 1): rest-frame anchor from R-034 elastic overlap (static force reads the 𝓠-part only; pure 𝓛-strain exerts zero static force on a monopole winding by exact ⟨Σ_Q Σ_L⟩₀ = 0) + Spin covariance via transitivity determine the force law everywhere; Schur commutant-2 cross-check (equivariant bilinear maps Λ²×V→V = span{F·u, (I₄F)·u} exactly; the I₄-dual killed by the anchor; u-cubic candidates collapse exactly); `f·u = 0` exact ⇒ `dm/dτ = 0` a consequence; exact rotor solution rotates at `ω_c = qB/m` | DERIVED-A (algebraic spine) + DERIVED-conditional (worldline/point-monopole limit, R-038 class; AND the Spin-covariance premise R-014 + R-039 (cooled 2026-07-27 to FRAMING + removed-falsifier + structural identification; was DERIVED-STRUCTURAL) — named condition per reviewer amendment) + INHERITED-CONDITIONAL (inertia leg `m = k_4 = ω/c_meta` via R-123 residue (ii)) | charged_defect_worldline_eom_cyclotron | B.5.5 | R-032, R-034, R-014, R-038, R-039, R-123 | — | Banked 2026-07-02 (twt-reviewer HOLDS + 2 amendments applied; commutant-2 independently reproduced by the reviewer via rep theory + a separate generating set). Chains (1)+(2) now both sit MODULO residue (ii) alone; residue (ii) gates three of five signature chains — the item's critical path. α_em magnitude stays #1-gap; magnetic-moment/gradient-B forces, nonlinear-in-F corrections, g-factor, radiation reaction all named NOT-derived. First Class-1 queue item (companion Section 12) to close. |
| R-125 | Defect phase collective mode sits at `k₄ = ω/c_meta` (R-123 residue (ii), existence/location half): `Ω = R̃∂R` exactly invariant under the constant left shift `R → gR` (Spin(4) `g`) ⇒ by the symmetry-linearization lemma the shift generator applied to the rest defect `R* = exp(ûωτ₅/2)R₀(x)` is an exact solution of the linearized EOM — the co-rotating zero mode `(û/2)R*`, reading at lab frequency exactly `ω`, front `k₄ = ω/c_meta`; equals `(1/ω)∂_τ₅R*` so `τ₅`-autonomy is an independent sufficient premise. AXIS-SPLIT (reviewer amendment): bivector `û` rides the banked left-Spin(4) shift; `û = E` does NOT (`Ω(g_E R) = e^{Eθ}Ω(R)` exactly, engine — the Ω-built sector is not E-phase invariant) and routes through τ₅-autonomy or an unbanked U(1)_E dynamical invariance | DERIVED-via-symmetry-CONDITIONAL (C1: û-phase symmetry OR τ₅-autonomy of the full EOM, axis-split, coherence-argued NOT proven for the §D.5 kernel; C2: separable rest-defect ansatz = R-123's idealization) | defect_phase_collective_mode_at_k4 | D.4.6 (+ §B.2.1 cross-cite) | R-123, R-041 (shift symmetry), R-112 (master eq) | R-126 | Banked 2026-07-02 (twt-reviewer MISLABELED→fixed→HOLDS: the E-axis premise was scoped down per the reviewer's engine finding, which is itself now banked as a check). SHARPENS residue (ii), does NOT close it: remaining (H1) localization/normalizability vs the carrier, (H2) identification as THE one-particle pole (§D.4.6 shape-mode spectrum, Paper-2). New falsifier face: a computed spectrum whose one-particle pole sits elsewhere than `ω/c_meta` falsifies `m = k₄`. The s=3/Adler-zero symmetry-shortcut move class, applied to the one object it can reach (the Goldstone phase mode itself). |
| R-126 | Zero-mode multiplet labels: the rest defect's EXACT symmetry-mode sector reads ONLY `k₄ = ±ω/c_meta`. Left shifts split by the û-commutant (commuting dim-2 → `+ω` incl. the R-125 phase mode; anticommuting dim-4 → `−ω` exactly, via `B·Q(τ₅) = Q(−τ₅)·B` — the conjugate branch); right shifts → `+ω` (NEW engine facts: `Ω(Rg) = g̃Ωg` exact ⇒ every scalar Ω-word right-invariant by cyclicity); translation-type → `+ω`. No third label anywhere in the catalog | DERIVED-via-symmetry-CONDITIONAL (per-class premises: P1 left banked; P2 right scalar-sector engine-exact, DM/topological right-status OPEN — and the DM caveat is two-sided at kernel level, covered by the inherited C1; P3 translations = homogeneity, continuum-limit over discrete D4, WP-LV1 class; C1/C2 inherited from R-125) + DERIVED-A (right-covariance facts; label table; commutant dims (2,4)) + FRAMING (−ω antiparticle reading; boost/moving family FIRED as R-132 — a consistency check, NOT an independent second angle, D-8 sweep 2026-07-31; multiplet-as-(H2)-skeleton on the defect-linearized side; multiplicity gloss is prose, NOT an engine-backed count — mode families overlap, do not cite a multiplet dimension) | defect_zero_mode_multiplet_labels | D.4.6 | R-125, R-123, R-041, R-112 | — | Banked 2026-07-02 (twt-reviewer HOLDS; 3 non-blocking notes applied — multiplicity gloss scoped, DM two-sidedness noted, same-pass sync). Supports residue (ii)'s (H2) half: one rest label + conjugate, no spread. Two new falsifier faces: a DM-induced right-sextet lift (predicted fine structure); any symmetry-mode label ≠ ±ω/c_meta. |
| R-127 | Front-phase hand-off resolves R-123 residue (iii) AS A SELECTION: projecting the defect history `B_a·s₀·q_h(τ₅)` onto the observer's forced complex line `{1, B_a}` (R-020) gives an exact dichotomy — only `û = ±B_a` (the winding blade itself) stays in the line as a pure propagating phase at exactly `±ω` (`k₄ = ω/c_meta` on the lock); other ℍ axes read as spin precession (in-ideal, amplitude-only shadow); the central `E` leaves the Cl(4,0) ideal (density-node shadow). One blade, two roles — §A.3's two-faces made exact; no `E → B_a` conversion owed; `E` keeps its global/colour complex-structure role | DERIVED-A (dichotomy: exact, all three B_a, orthogonal line basis, left/right convention-free for winner and E) + DERIVED-CONDITIONAL (the selection; C1 §B.3.1/R-020 grade-2 ansatz — the corpus B_a grade double-use flagged for disambiguation; C2 banked Part-B pure-phase criterion + empirical face; C3 L-orbit scope, axis menu = ℍ ∪ {E}) + FRAMING (ξ-gloss reconciliation: rotation ALONG a flat direction is kinetic, not a potential lift — reviewer verified nothing engine-checked in sakharov_xi_minimal_coupling pins mass to E) | front_phase_handoff_selects_winding_axis | B.3.1 (+ §B.2.1, §A.4 superseded-gloss notes) | R-020, R-123, R-021 | R-128 | **A-1c edge STRUCK at present (J,D/Γ rework; keeper CONFIRMED, `VERDICT_KEEPER_2026-08-21.md` collision 2): the derivation is a pure Cl(4,0) projection dichotomy and its named conditions C1–C3 contain no bond content — the recorded edge asserted a dependence the row's own text denies. OWED-IF-BUILT, not deleted as a possibility: a future EOM-level axis lock would plausibly route through the vacuum's canting PLANE, and that plane is now BRANCH-DEPENDENT (`E₁₄` on the axis branch, a different plane on the body-diagonal branch — R-108's branch structure, negatives ledger N62), so the prospective edge cannot even be written down until branch selection resolves at §D.5.7.** Banked 2026-07-02 (twt-reviewer HOLDS + 2 sweep fixes applied: §A.4 stale glosses annotated; C1 corrected to the R-020 grade-2 form). Retroaction: R-125's unbanked E-axis premise MOOT for the physical mass phase (winner rides the banked left-Spin(4) branch); residue (ii) (H2) target = the B_a-phase mode. Still open: EOM-level axis lock (selection is consistency-forced, not dynamical); baryon Q-orbit analog. New falsifier face: a matter-wave mass signature that is not a propagating phase. **INSTRUMENT SCOPE (K-O1 close-out, keeper-C3 wording adopted verbatim):** R-127's E-branch exclusion is a statement about the NET (relative) E-phase. The primitive computes it on the trivial background R_∞ = 1, where net = absolute. On a carrier background the identical exclusion applies to the DETUNING dk by the centrality identity (companion `ecarrier_common_mode_certificates` leg 1). Not covered by the trivial-background computation: the MATCHED case dk = 0 (no net E-phase — nothing to exclude; outside R-127's original axis menu) and the common-mode reading question (hinge H). |
| R-128 | Q-orbit extension of R-127: for a baryon-sector winding `B_q`, the observer's forced complex line is `{1, I₄B_q}` — the Hodge dual (up to sign), all three `B_q` (true-nullspace-verified by reviewer) — and the mass phase locks to `û = ±I₄B_q` (exact dichotomy; winding axis leaks to the complementary idempotent sector). The lepton lock is parity-EVEN (identity); the quark lock is parity-ODD (`P(I₄X) = −I₄P(X)`, any improper reflection) ⇒ a ℤ₂ relative-orientation label parity flips: quark-sector defects come in statically-degenerate parity-mirror pairs (the SEAT of the up/down doubling), charged leptons provably carry no label; the mirror pair ≠ the antiparticle pair (σ rotation-invariant). Lock operator = I₄ ⇒ the `⟨I₄⟩`/µΨ₀ dial enters quark mass-phase geometry through the lock, absent from the lepton lock | DERIVED-A (centralizer, dichotomy, parity facts — exact; reflection-choice-immune per reviewer) + DERIVED-CONDITIONAL (C1′ Q-orbit analog ansatz — R-020's 'structural analog, not load-bearing' inherited; C2′ same-observer premise; C3′ R-127 criterion) + FRAMING (up/down SEAT; the µΨ₀-through-the-lock tie — the coupling not constructed; split stays dynamical per N28) | qorbit_mass_phase_dual_lock_parity_odd | B.3.1 (+ §C.3.13 note) | R-127, R-020, R-077, R-123 | — | Banked 2026-07-02 (twt-reviewer HOLDS + 3 cosmetic fixes; N28 verified untouched — statics gives two-ness, not the split; N32a tie verbatim-accurate). New falsifier faces: a charged-lepton parity-mirror mass-partner tower; a third comparable tower per Q-orbit slot. Would change if: banked Q-orbit defect construction hardens C1′; quantitative ⟨I₄⟩-through-the-lock coupling → a 2b mechanism row. |
| R-129 | ⟨I₄⟩-condensate ideal-channel rule (the R-128 mechanism face, first move — ELIMINATION): s₀Ms₀ = Ms₀ if [M,e₄]=0, = 0 if {M,e₄}=0 (complete 16-blade table; survivors = the e₄-commutant = the (W) family; bare I₄ dies identically — Ψ̃I₄Ψ = 0 all grades, both sectors); the R-128 mirror pair is ONE ray at snapshot level ⇒ diagonal bilinears σ-blind; the linear defect-vacuum pairing ⟨vac~I₄Ψ⟩ is nonzero and σ-ODD (reviewer's engine finding, banked) and is excluded by the NAMED sign-gauge premise (Ω(−R) = Ω(R) exact + R-020 rays) ⇒ any up/down-splitting µΨ₀ coupling must engage the spatial winding topology; §D.4.4's ρ_L boundary term (R-110) is the standing candidate seat, pointed to not confirmed | DERIVED-A (channel rule; blindness facts; linear-channel facts; Ω sign gauge) + DERIVED-CONDITIONAL (the elimination, on the named sign-gauge premise) + FRAMING (ρ_L candidate seat; Skyrmion-degree anchor for σ) | i4_condensate_ideal_channel_rule | B.3.1 vicinity (+ ledger N38) | R-128, R-020, R-110 | — | Banked 2026-07-02 (twt-reviewer OVER-CLAIM→5 fixes→consensus; the reviewer's linear-channel finding is itself banked as a check). Sharpens the 2b mechanism row: the µΨ₀ coupling construction = the §D.4.4 boundary integral on an explicit profile (P2-7-class). R-128's ℤ₂ seat clarified same pass (snapshot collapse; distinctness anchored by spatial topological degree). |
| R-130 | Residue (ii) (H1) localization half DISCHARGED into the defect's own finite-norm existence: the R-125 phase mode's defect-excess is EXACTLY as localized as the defect — pointwise `N(exc) = ½N(R₀−1)`, τ₅-free ⇒ mode-L² ⟺ defect-L² (factor ½ exact); the raw mode is provably non-normalizable (constant norm ½ everywhere); the carrier subtraction is UNIQUELY forced (asymptotic residual `\|sin((ω−ω_c)τ₅/4)\|` ⇒ ω_c = ω — R-125's vacuum-relative subtlety DERIVED as a dichotomy, not assumed); hedgehog criterion `‖R₀−1‖² = 4sin²(F/4)` (n̂-independent; half-angle convention) ⇒ normalizable iff tail p > 3/2; static drive→0 face (§C.1.1 BVP): exterior Euler equation, indicial roots {−2, 1} ⇒ r^−2 tail — criterion met with margin | DERIVED-A (facts F1–F5 + static-face indicial exponent; isometries exact for SIMPLE unit bivectors — reviewer probe: non-simple fails, both physical axes simple) + DERIVED-CONDITIONAL (the (H1) closure, on named (C2) inherited + (T) tail + (N) norm equivalence) + FRAMING (below-continuum reading of (T-kernel) as the (H2) bridge) | phase_mode_excess_inherits_defect_localization | D.4.6 | R-125, R-126, R-127, R-123 | — | Banked 2026-07-02 (twt-reviewer HOLDS + 2 required wording fixes + 2 recommended annotations applied; F4/F5 symbolically re-proved by reviewer). Residue (ii) narrows to (H2) + (T-kernel) — a genuine open pair, (T-kernel) not minimized under (H2). New falsifier face: a banked kernel tail slower than r^−3/2 strips m = k₄ of its discrete carrier. SCOPE (τ₅ adjudication 2026-08-13): the ω_c = ω dichotomy is derived WITHIN the (C2) separable rest ansatz — whether it extends to a boosted (two-frequency-class) family is UNDECIDED (adjudication RULINGS-OWED (i)); this row's subtraction acts at the FIELD/NORM level, the sibling of the ruled cost's DENSITY-level subtraction (conjugation identity in companion `one_sided_rotor_uniform_density_identity`), and the map between the two levels is OPEN (the O1 gap; N61; `TAU5_ADJUDICATION_2026-08-13.md`). |
| R-131 | Residue (ii) (H2) QUANTIZATION-STEP skeleton: the phase modulus (the finite orbit of R-125's mode generator) is COMPACT — rotor period 4π, `θ+2π ⇒ −R`, Ω sign-blind (R-129 gauge) ⇒ physical ray-orbit a closed 2π circle — so the conjugate charge is DISCRETE (given (Q)); and the tower's leading spacing is EXACTLY ω: on the ansatz `Ω_τ₅ = R₀~(ûω/2)R₀` (τ₅-free, linear in ω) and `Ω_i` ω-free ⇒ any Ω-built action reduces to `L(ω, shape)`; relative equilibria are shape-stationary and along the family `dE/dN = ω` exactly — the envelope identity engine-proved symbolically for FULLY GENERIC `L(ω, shape)` (kernel-form-free), δ-independent across all charge-lattice sectors. First quantized phase excitation carries the same front label `k₄ = ω/c_meta` (inherited from R-125) that R-017 consumes | DERIVED-A (A1/A2 reduction; compactness/orbit facts; the universal envelope factorization) + DERIVED-via-symmetry-CONDITIONAL (`dE/dN = ω` on the family; named (C1) conservative-sector shift symmetry + (C2′) relative-equilibrium family) + DERIVED-given-(Q) (discreteness; corpus-standard collective-quantization premise; lattice menu {0,½} rides on rotor-double-cover single-valuedness — reviewer fix) + FRAMING (moduli↔KG-pole identification; Planck-form remark) | defect_phase_modulus_charge_tower_spacing | D.4.6 | R-125, R-123, R-127, R-129, R-130 | — | Banked 2026-07-03 (twt-reviewer HOLDS + 1 required θ-angle-conditionality fix + 3 recommended annotations applied; reviewer proved the envelope identity MORE generally than claimed and the upgrade is banked). ℤ vs ℤ+½ lattice = FR-family selection, NAMED not decided (fork-neutral; spacing δ-independent); P2-4's induced level becomes a free cross-check. Remaining (H2) core: pole uniqueness + moduli↔pole identification. With R-130: residue (ii) = (H2-uniqueness/identification) + (T-kernel). |
| R-132 | R-126's boost/moving-family handle FIRED: the finite Lorentz-boost orbit of the rest one-particle label, computed INSIDE Cl(4,0) via the γ-embedding — `B_ζ = exp(ζeⱼ/2)` hyperbolic (because `eⱼ² = +1`; the observer's boost bivector `γ⁰γʲ = eⱼ` is a substrate VECTOR — the iso not grade-preserving at the boost planes), exact rapidity addition, vector action `Bγ⁰B⁻¹ = cosh ζ γ⁰ − sinh ζ γʲ`; rest label `mγ⁰` (`m = ω/c_meta`, R-123) ⇒ `(E,p) = m(cosh ζ, sinh ζ)`, `E² − p² = m²` EXACT (algebraic + componentwise; generic directions; boost∘rotation) ⇒ chain (2) dispersion's KINEMATIC CONSISTENCY CHECK on R-017's dynamical KG route — **NOT an independent second derivation and NOT over-determination of any kind** (scope corrected 2026-07-30, review item III-12, to §B.2.2's own language: once the Lorentz group acts and `m` is *defined* as the rest label, "the orbit of the rest label is the mass shell" is close to tautological; the two routes share the isomorphism and the front label, so their agreement is corroboration). REVERSION HAZARD banked: `B̃ = B ≠ B⁻¹`, the corpus `R·x·R̃` sandwich is a silent NO-OP here (`Bγ⁰B = γ⁰` exact) — use `B·x·B⁻¹` (= the Cl(1,3)-reversion sandwich through the iso). Caveat defused side-by-side: `e₁₄` rotation circular (`E = m cos θ`), `e₁` boost hyperbolic — `e_i4_squares_to_minus_one` intact, scope-annotated | DERIVED-A (orbit algebra, grade-shift fact, shell invariance, reversion hazard, caveat defusal) + DERIVED implied-by-banked (the dispersion CONSISTENCY CHECK — NOT a second independent angle, retagged 2026-07-30 per §B.2.2; NAMED (P) substrate-realization premise, R-039 class as in R-124, + (I) inherited residue-(ii) remainder) + imported group theory (orbit transitivity, cited like Schur) | boost_orbit_rest_label_mass_shell | B.2.2 (+ §D.4.6 R-126 handle-fired note) | R-013, R-014, R-123, R-039, R-126 | — | Banked 2026-07-03 (twt-reviewer HOLDS + 1 required reversion-hazard annotation + 3 recommended fixes applied; the no-op hazard is the reviewer's own engine finding, banked as a check). B is NOT a Cl(4,0) rotor (mixed parity, not Spin(4)) — the even Cl(1,3) rotor through the embedding. Falsifier alignment: an off-shell moving defect would break (P), which WP-LV1 protection predicts cannot happen. Named next: the wave-level (x₄-profile) orbit reading would hand chain (5) the same second angle. |
| R-133 | The rotational-band baryon mass equation `M(J) = M₀ + J(J+1)/(2Θ₀)` with BOTH coefficients from the exact hedgehog BVP: `M₀ = 36.46 f_π/e` (validates the banked 36.47; Derrick virial `E2 = E4` < 0.1%) and `Θ₀ = 106.76/(e³f_π)` — **CORRECTING the long-banked 97.27** (= `36.47·8/3 = 97.253` to within 0.02%, provenance suspect; exact `Λ = 50.98` matches the ANW literature ~50.9, and the truncated-grid route reproduces how a spurious ~97 arises). At the counted ANW couplings: `M_N = 936.4` (−0.3%), `M_Δ = 1229.8` (−0.2%), split `293.4` (+0.1%) — the banked M₀'s "8% ANW deficit" EXPLAINED as the missing band term. Knock-ons swept: `1/Θ₀` 214.7→195.6 MeV; R-111 Λ_QCD candidate 215→196 (in-range; scheme-dependent whether closer); top exclusion 6.5→7.2 (STRENGTHENED); `Σ_c−Λ_c` 171 (2.4%)→151.9 (−9.0%) — NEW TRACKED RESIDUAL (the old agreement rode the wrong constant); `Σ_b−Λ_b` 201→181.9 (−4.8%, improved) | DERIVED dressed-level (§D.4.3 branch-(c) conditional, as R-051) + DERIVED-given-(Q)+FR-selection (J = ½, 3/2 — the FR fermionic SELECTION, W-LIVE-4 fork untouched) + CORRECTION (THETA0_COEFF swept corpus-wide) + R-131-class band instance (spin/isospin moduli, distinct from the U(1) phase tower) | skyrmion_rotational_band_nucleon_delta | C.1.2 (+ D.4.5 correction, C.5.9/E.3 numbers) | R-051, R-131, R-130, R-111, R-091a | — | Banked 2026-07-03. HONESTY: `f_π, e` were historically FITTED to N/Δ (ANW) — pipeline consistency, not a new prediction; no new parameter. Candidate resolution of the c-leg residual: bound-state-class inertia ≠ rigid-rotor Θ₀ (P2-7-adjacent). Would change if: pion-mass-term BVP shifts the pair *(fired 2026-07-03, adjudicated by R-137/R-138: the pair shifts only in the massive scheme — 37.90/70.20, a second distinct scheme axis; refit executed at R-138, baseline stays massless, banked coefficients unchanged; Θ₀-downstream numbers — Λ_QCD candidate, top exclusion, Σ_c−Λ_c residual — fork-invariant per R-138's `1/Θ₀ = (2/3)·split = 195.4 MeV`)*; P2-4 decides FR. Consumes the §A.4 `m = E₀` premise (counted 2026-08-12) — here in CALIBRATION mode (`f_π`, `e` historically fitted to N/Δ; the ANW honesty note). |
| R-134 | Brannen-scale ↔ nucleon-third convergence: `μ² = 313.85 MeV` vs `m_N/3 = 312.97 MeV` — 0.28% with ZERO parameters; amplitude form `√(m_N/3)/μ = 0.9986` (0.14% — the SAME single convergence, √ halves the deviation) — the baryon per-rotor amplitude = the lepton tower's DEMOCRATIC component (the generation-blind `μ·1`; ℤ₃ offsets average out). Legal reading: `m_N/3` = mean per-rotor frequency of the `Ω_B = Σω` lock (itself DERIVED-conditional, E-channel premise), NOT a quark mass (canon §5 intact). Look-elsewhere scan banked: 4 comparators × rationals p/q ≤ 8 at 0.5% → EXACTLY two hits (m_N/3 at 1/1; the fit-tied 8/5 of 1/Θ₀ — same hit via the N/Δ fit). FLOOR reading (`M₀/3 = 287.7`) does NOT converge (~9%) — the convergence stakes the full-mass side of the freq-sum-vs-full-mass fork. Specific to `m_N/3` (not `f_π`, not `1/Θ₀`) | CANDIDATE (zero-parameter cross-sector convergence, recorded per canon §0a; observation literature-known in the Koide circle, imported as such; post-hoc/look-elsewhere caveat named) + FRAMING (per-rotor lock reading; democratic-axis reading) + engine-checked arithmetic on INPUTs | brannen_scale_nucleon_third_convergence | C.3.11 | R-064–R-066 (Brannen), R-051, N12, cogear lock | — | Banked 2026-07-03 (coordinator question). Naive `I₄` derivation route BLOCKED by N12 (amplitude-blind Hodge map) — mechanism must be cell-scale/kernel class. Would become a RESULT if a P2-1/P2-5-class mechanism pins the per-rotor lock frequency to the lepton democratic component ⇒ `m_N = 3μ²` co-derives the nucleon mass from the lepton tower (one fewer counted INPUT dial; 2b table row). Would weaken if the E-floor bridge resolves the lock to the floor reading. |
| R-135 | P2-7 first half — nuclear binding exists classically: the `B = 2` rational-map configuration (`R(z) = z²`; the reduction to the radial BVP is the EXACT 3D energy — angular content enters only via the computed `I(z²) = 5.8083` and the exact degree identity `(1/4π)∫ψ² = B = 2`, certified <1e-10) has energy `71.543 f_π/e < 2×36.462 = 72.923` — **strictly below the two-defect threshold, margin 1.89%** (numerical error ~1e-5; independently re-solved by the reviewer with different window/domain/tolerances to 4e-5 agreement) ⇒ the `B = 2` channel is classically BOUND (strict sub-additivity), attraction SIGN predicted, magnitude NOT claimed. At the counted ANW couplings: binding ≥ 32.7 MeV vs observed 2.22 MeV — classical overbinding honestly imported (known massless-Skyrme character; quantization + pion mass = named follow-ups). Indicial generalization `s²+s−2B = 0` of R-130's `{+1,−2}` (`B = 2`: `(−1±√17)/2`, non-integer origin exponent, steeper tail — no long-tail matching problem). Certificates: Derrick virial ~3e-6 both profiles; `B = 1` regression to the banked 36.46; per-baryon 1.2081·12π² (HMS 1.208 corroboration, not load-bearing) | DERIVED dressed-level VARIATIONAL (below-threshold inequality; branch-(c) conditional as R-051/R-133; conclusion ansatz-independent GIVEN the inherited hedgehog-minimality premise — reviewer fix F1; value = upper bound only) + DERIVED-A (indicial generalization; degree identity) + FRAMING (deuteron identification `J^π = 1⁺` awaits `B = 2` collective quantization — classical SEAT only) | multi_skyrmion_b2_classical_binding | C.1.2 (+ E.3 SC-1 row note) | R-051, R-133, R-130 | — | Banked 2026-07-03 (twt-reviewer HOLDS + 2 required fixes F1/F2 + 3 annotations R1–R3 applied; the reviewer's clean-room re-solve and the B=1-origin marginality sympy fact are recorded in the docstring). First SC-1 `N = 2` datum, scoped: reduced-BVP + variational existence, NOT full 3D well-posedness. NOT done: tensor force from D4 anisotropy (P2-7 second half); `B = 2` quantization (the 2.22 MeV face); pion-mass BVP; Callan-Klebanov bound-state inertia (the R-133 `Σ_c−Λ_c` residual adjudicator — adjacent, distinct). Would change if: pion-mass BVP shifts the pair (re-check margin — *DISCHARGED 2026-07-03 by R-137/R-138: the margin survives across the entire fork — 1.96% at the probe couplings, 1.87% at the refit couplings; non-monotonic in μ*); full-field torus computation (deepens, never un-binds) — *FIRED 2026-07-05 (R-144): the full-3D ansatz-free flow keeps the binding, deepening at N = 96 same-grid (stall-vs-stall 3.06%, ≥ 2.95% after the reviewer's B1-side probe; the toroidal minimizer) — as predicted*. Consumes the §A.4 `m = E₀` premise (counted 2026-08-12) wherever its elastic values meet measured masses. |
| R-136 | P2-7 quantization face — the quantized axial `B = 2` sector's ground state has EXACTLY the deuteron's quantum numbers: the `z²` map symmetries (engine-symbolic; axial iso-lock ⇒ `L₃ + 2K₃ = 0`) + FR loop signs (Krusch homotopy formula: S2 loop `N = 2` → +1, mixed S3 loop `N = 1` → −1) give the `K₃ = 0` tower rule **`I + J` ODD** — `(0,1) = J^π = 1⁺, I = 0` THE DEUTERON (parity from the derived internal parity map `R_P = −R`, anchored to nucleon `+`; `\|K₃\| ≥ 1` towers provably higher), scalar `(0,0)` dibaryon TOPOLOGICALLY FORBIDDEN, `(1,0)` np-singlet ~40 MeV up at ansatz level (`V_⊥ = 312.5 > U_⊥ = 194.6`; certificates: four-way `B = 1` regression to R-133's 106.76, `V₃₃ = 4U₃₃` exact, `W_⊥ = 0` block-diagonality < 1e-14 — the reviewer's probe banked; S2's +1 doubles as the axial no-anomaly certificate). FORK FACE: bosonic branch flips to `I + J` EVEN (bound scalar ground state) — empirically refuted ⇒ SECOND independent anchor for the fermionic FR selection (independent data, shared (Q) premise) | DERIVED-A (map symmetries; parity MAP identity; `V₃₃ = 4U₃₃`; `W_⊥ = 0`; factorization via hedgehog reduction = R-133) + IMPORTED-AS-CITED (Krusch formula, consistency-checked; mod-2-weak composition asserts noted — the S2 loop is the form discriminator) + DERIVED-given-(Q)+FR-selection (rule + quantum numbers incl. state-level parity; W-LIVE-4/N35 fork UNTOUCHED) + ANSATZ-LEVEL (ordering; torus corroboration cited not banked) + FRAMING/ESTIMATE (MeV spectrum; rigid-rotor overbinding stated). **Headline physics LITERATURE-KNOWN** (Braaten–Carson 1988; Leese–Manton–Schroers 1995; Krusch 2003 — to-be-verified citations, R-134 precedent); new content = tiering + certificated moments + fork-face bookkeeping | b2_axial_quantization_deuteron_ground_state | C.1.2 (+ B.3.5 anchor note) | R-135, R-133, R-025, N35 | — | Banked 2026-07-03 (twt-reviewer HOLDS + 3 required fixes + 5 recommendations applied; the reviewer's `W_⊥ = 0` probe and the Krusch-form discrimination via the S2 loop are recorded). Upgrades the deuteron identification from R-135's FRAMING to the quantum-number level; binding VALUE still open. NOT done: `\|K₃\| ≥ 1` allowed sets; tensor force/D4 (P2-7 remaining half); pion mass; torus moments; Callan–Klebanov inertia. Would change if: P2-4's induced level lands EVEN (anchor becomes a standing tension); torus flips `V_⊥` vs `U_⊥` (literature: no); pion-mass BVP shifts moments *(pion-mass face DISCHARGED: R-137 — the topological selection is mass-untouched; R-138 — the massive-branch moment-ordering re-check done, `V_⊥ = 222.1 > U_⊥ = 135.6`, deuteron stays the ground state in-branch)*. |
| R-137 | Pion-mass robustness re-check (the R-133/R-135/R-136 owed face, DISCHARGED for existence/sign): deforming by the standard chiral-breaking term `(μ²/4)x²(1−cosF)` at the physical `m_π = 138` (isospin-averaged; `μ = m_π/(e·f_π) = 0.196`; normalization re-derived against the banked conventions — canonical-pion check `−½m_π²π²` exact) leaves the R-135 inequality intact and marginally STRONGER: `74.31 < 2×37.90 = 75.80`, margin **1.96% vs massless 1.89% (widens; assert-backed > 0.0189)**, binding ≥ 35.2 MeV. Certificates: mass-extended Derrick `E2 + 3E_m = E4` (~3–5e-6 both profiles); Bessel tail `x^(−1/2)K_ν(μx)`, `ν = √(2B+¼)`, with the DERIVED-A identity `√(2B+¼)+½ = (1+√(1+8B))/2` (μ→0 reproduces the massless exponents exactly); margin stable to 4 decimals under window/xmax/bracket variation (reviewer probe). THE INERTIA FACE: massive-profile `Λ = 33.52` vs massless `50.98` (θ-coeff `106.76 → 70.20`, −34%) ⇒ the massless `N/Δ` closure does NOT transfer at fixed couplings (reviewer hand-check: `M_N ≈ 1009`, split ≈ 446 — fails) ⇒ the massive variant is a SECOND, DISTINCT scheme axis alongside §C.1.2's local/phason fork (object-dependent: masses +3.9%, inertia −34%); refit fork NAMED, not taken; banked baseline stays massless | DERIVED dressed-level VARIATIONAL ROBUSTNESS (branch-(c) conditional; hedgehog-minimality premise EXTENDED to the massive functional — same class, different functional) + DERIVED-A (Bessel-index identity; mass-extended Derrick) + NAMED IMPORT (`m_π` witness, probe-only, both sides identically — not a counted dial; `(1−cosF)` form = imported chiral-breaking deformation, not a banked substrate term) + LOCATED (massive-scheme refit fork named, not taken) | massive_pion_bvp_binding_margin_robust | C.1.2 (R-137 passage) | R-135, R-136, R-133, R-051 | — | Banked 2026-07-03 (twt-reviewer HOLDS + 3 required fixes + 2 recommendations applied; normalization/Derrick/Bessel spine independently re-derived by the reviewer; widen-claim tightened to assert-backed). Would change if: the massive-scheme refit is banked (re-anchor all massive numbers, re-check margin at refit couplings — literature keeps B=2 bound there, imported not banked); a substrate derivation of the chiral-breaking term lands (probe → sector). *Refit face FIRED at R-138 same day: margin at refit couplings 1.87% — survives; the margin is non-monotonic in μ (1.89/1.96/1.87), so the widening is probe-point-specific.* Consumes the §A.4 `m = E₀` premise (counted 2026-08-12) at its measured-mass contact points. |
| R-138 | Massive-scheme refit branch, executed + adjudicated (coordinator-approved fork execution): self-consistent 2D fit lands at `f_π* = 108.26 MeV`, `e* = 4.8427` (`μ* = 0.2632`; corroborates Adkins–Nappi 1984's 108/4.84 — citation to-be-verified; reviewer re-derived the point by a different algorithm from two bracketing starts, unique to 4e-6), `N/Δ` closed. FIT-INVARIANCE (DERIVED-A given the band form + J-assignment): `1/Θ₀ = (2/3)·split = 195.4 MeV` in any exact-closure scheme ⇒ Λ_QCD candidate, top exclusion, AND the `Σ_c−Λ_c` residual all fork-INVARIANT — "scheme artifact" eliminated; weight redistributes to BOTH R-133 candidates (CK-class inertia; `hf_c` re-fit). OWED RE-CHECKS at refit couplings: margin 1.87% (75.997 < 77.442, binding ≥ 32.3 MeV — the binding conclusion verified across the ENTIRE fork {μ = 0, 0.196, 0.263}, no fourth corner: the massless margin is coupling-independent; margin non-monotonic in μ, banked); ordering `V_⊥ = 222.1 > U_⊥ = 135.6` (deuteron stays ground state in-branch). BASELINE DECISION (bookkeeping, not derivation): **massless stays** — D1 parameter economy (2 vs 3 counted inputs; the third buys the physical pion tail), D2 hedged convergence-preservation (two-route × two-scheme grid: only sub-2% entry is massless-`√18`, hedge carried; sign flips on the `√12` route), D4 import-minimization (the `(1−cosF)` form is a load-bearing underived import in-branch) | FIT in-branch (same 2 dials; branch counts 3 inputs — `m_π` load-bearing; the `(1−cosF)` FORM a load-bearing structural import in-branch) + DERIVED-A (Θ₀ fit-invariance, band-form + (Q)+FR-conditional) + DERIVED variational robustness (margin + ordering at refit couplings; branch-(c) + extended hedgehog-minimality conditionals) + SCHEME DECISION (bookkeeping entry) | massive_scheme_refit_branch | C.1.2 (R-138 passage) | R-137, R-136, R-135, R-133, R-111, R-091a | — | Banked 2026-07-03 (twt-reviewer HOLDS on every number + 5 required fixes F1–F5 + 6 recommendations applied — F1 √18-hedge carried, F2 decision-grounding reworded, F3 both `Σ_c−Λ_c` candidates restored, F4 in-branch form-import restated, F5 sweep executed; `D/J` wired to `DoverJ_from_lepton_masses()`). Would change if: substrate chiral-breaking derivation lands (D1/D4 dissolve, fork re-opens on D2); the D/J calibration moves; a P2-5-class cell-scale derivation pins `e·f_π` from the substrate. Consumes the §A.4 `m = E₀` premise (counted 2026-08-12) at its measured-mass contact points. |
| R-139 | P2-7 tensor-force face + item close-out: the asymptotic Skyrmion is an exact TRIPLET OF ORTHOGONAL PION DIPOLES `π_a = −C∂_aY` (at `B = 1` the Bessel index `ν = 3/2` makes the massive tail elementarily the dipole-Yukawa profile `(1+μr)e^{−μr}/r²` — sympy identity), so the two-defect asymptotic interaction is `V(R,O) = πC²[(3O_RR−TrO)(1+μR+μ²R²/3) + TrO·μ²R²/3]e^{−μR}/R³` — the OPE central+TENSOR radial structure EXACT (central `∝ μ²` vanishes massless = the aligned-channel zero). Dipole strength nearly FORK-INVARIANT, all solved in-primitive: `C = 8.634/7.91/7.66` (massless/probe/refit; **the drafted refit 4.24 was REFUTED by the reviewer** — a provenance misread of R-137's B=2-at-probe constant; fix F1). Sign/magnitude pinned by the GRID, not convention (source-vs-field-energy bookkeeping ambiguity named): 169³ development record — aligned channel vanishes (+0.34/+0.068/+0.005/−0.013), ∥ π-rotation REPULSIVE (ratios 0.81→0.92), ⊥ π-rotation ATTRACTIVE (0.66→0.83; the R-135 binding channel), channel ratio → 2.2 vs exact 2; reviewer systematics probe banked (Richardson → ~0.9–1.0) — magnitude scoped 10–20% raw, residual = named grid systematics; 81³ in-suite regression | DERIVED-A (K_{3/2} elementary; dipole identity; OPE decomposition + μ→0 limits) + DERIVED dressed-level ASYMPTOTIC (the law; product-ansatz class, branch-(c) conditional) + GRID-CERTIFICATED scoped + CORRECTED PREMISE-DRIFT (N39: the "from D4 anisotropy" worklist phrasing was drift — `eta_DM` always said dominant tensor = OPE; the `η_DM = (D/J)²/144` CALIBRATED face preserved as the P2-5-gated subleading row; `eta_DM` docstring garble fixed same pass) + NAMED FOLLOW-UP (nucleon-state projection → quantum OPE strength). **Headline physics LITERATURE-KNOWN** (Skyrme; Jackson–Jackson–Pasquier 1985; Manton–Sutcliffe — to-be-verified citations); new content = in-framework derivation from banked tails + fork-resolved constants + certificates + the drift correction | two_defect_asymptotic_tensor_force | C.1.2 (R-139 passage) | R-135, R-137, R-138, R-133, R-086 (eta_DM) | — | Banked 2026-07-03 (twt-reviewer HOLDS on law/identities/grid + REFUTED on the drafted refit constant + MISLABELED on the premise framing — all 5 required fixes applied; the reviewer's independent 169³ reproduction, refit-tail solve 0.8251, and systematics probe recorded). **P2-7 CLOSED AT SCOPE** (R-135–R-139 + first SC-1 N=2 datum). LOCATED residual: binding magnitude ~113/~124 MeV (massless/refit) rigid-rotor overbinding — needs torus + beyond-rigid-rotor quantization. Adjacent rows: CK inertia (`Σ_c−Λ_c`); OPE-projection strength face; `η_DM` 1/144 (P2-5-gated). |
| R-140 | P2-4 leg 2 structural core — the explicit DM-twisted D4 plaquette holonomy: minimal curvature-carrying loops = the 32 triangles (8 spatial, trivial; **24 two-`e₄`-bond, ALL non-trivial** — pure-gauge lift EXPLICIT; the 36 chordless 4-cycles all carry trivial holonomy — reviewer probe banked as a check; the `e₄`-triangles engage ONLY the banked 48 non-commuting pairs); exact law `W = cos²θ + sinθcosθ(B̂₁+B̂₂) + sin²θ·e_ab` in the canonical lattice frame (invariant content: the chiral angle `arccos(cos²θ_D)` + non-triviality); the abelianized rotor has NO L-grade content while W's L-grade is exactly `sin²θ` — the 48/66 commutator content as the holonomy's non-abelian signature; consistency forces the orientation-ODD convention (= physical DM antisymmetry; convention-robust); **chiral factorization `W = W₊P₊ + W₋P₋` with IDENTICAL angles — the DM plaquette is chirally BLIND** (weak-sector chirality NOT sourced here; "weak = SD" stays the banked INPUT bit; §C.4.6(iii) qualifier added); per-sector Lie closure = FULL su(2)± (rank 3) ⇒ the `π₃(U(1)) = 0` instanton obstruction ABSENT at structure-group level | DERIVED-A (census incl. 4-cycle triviality; exact law; forced odd convention; chiral factorization + closed-form angle; non-abelian signature; per-sector rank 3) + DERIVED-structural (instanton obstruction-absence) + FRAMING preserved (dynamical YM — kernel-gated as banked; NO value claimed) + HONEST CONSTRAINT (chirally symmetric plaquette) | d4_dm_plaquette_holonomy_explicit | C.4.6(ii)-(iii) | R-103, D4_DM_bond_bivectors_non_commuting, R-088, N35 | — | Banked 2026-07-03 (twt-reviewer HOLDS + 5 wording/record fixes; reviewer's chordless-4-cycle probe banked). P2-4: leg 1 banked + leg 2 CORE DONE + leg 3 half-banked + leg 4 ANSWERED-AT-PARITY same day (R-141); leg 3 STRUCTURAL CORE DONE 2026-07-04 (R-143). |
| R-141 | P2-4 leg 4, the W-LIVE-4 decider, answered at the PARITY level: the induced topological term on the `B = 1` baryon worldline is the `π₄(SU(2)) = ℤ₂` class (no integer WZW for SU(2), consistent with the banked L3 refutation) with weight `(−1)^N`; N assembles from BANKED facts — roster 4 doublets/gen (evenness = the banked SU(2) gaugeability, same roster); baryon-coupled subset = the 3 colour modes/gen (lepton EXCLUDED by the one L/Q sector assignment seen in two banked faces — R-002 winding split + R-127/R-128 lock split — plus a third independent face: the single-Weyl neutrino cannot complete a chirally-linked determinant unit); counting unit fixed (one chirally-linked doublet pair per colour facet; `(u,d)` = R-128 σ-mirror components, QCD's own anchor N_c = 3 not 6); EVEN variants adversarially enumerated and each excluded (4/12 lepton-in; 6/18 double-counting; N = 0 = the P1b-refusal revert branch, not an established zero) ⇒ **N ∈ {3, 9} under the named generation fork — ODD in both branches ⇒ weight −1 ⇒ FERMIONIC SKYRMION QUANTIZATION INDUCED** | DERIVED-given-(P1)+(P1b)+(Q) (the parity; P1b = a FRESH CANDIDATE-class channel-identification premise — the one genuine vulnerability, named and revocable, inheriting R-127/R-128's ansatz conditions) + IMPORTED-AS-CITED (P1: D'Hoker–Farhi 1984 (NPB 248) / Witten 1982 (PLB 117), to-be-verified; R-088-class at the parity/mod-2-index level) + DERIVED (roster census, banked) + DERIVED-given-P1b (coupled-subset selection) + NAMED FORK parity-robust (3 vs 9) | induced_level_parity_on_baryon_worldline | C.4.6 (+ B.3.5 upgrade paragraph) | R-002, R-088, R-127, R-128, R-140, N35, §C.4.6(i) | — | Banked 2026-07-03 (twt-reviewer HOLDS at the conditional tier + 6 required fixes + 3 recommendations; no joint refuted — the reviewer verified the π₄ carrier, the (−1)^N form, the A.5.2 fibration split, and the R-127/R-128 channel facts in source; its even-variant enumeration (6/18) banked in the excluded table). W-LIVE-4's W1: **CLOSED-CONDITIONAL(P1+P1b+Q), POSITIVE**; N35 (a) PARTIALLY discharged at parity level (substrate computation face open); both anchors become consistency checks. **P1b is SPLIT by R-161**: its structural half (the channel identity, winding-assignment-relative) is now exact `Cl(4,0)` algebra given C1′–C4′; only P1b-DYN (the mode determinant actually generating the term) remains CANDIDATE. Would change if: P1b-DYN refuted (revert; anchors stand); mode determinant substrate-derived (P1 discharges); generation fork decided (parity unchanged); roster changes. |
| R-142 | WP-MASS-MEASURE residue (ii), the (H2) core, answered at the structural level: (identification, LABEL half CLOSED) the CLOCK-ORBIT IDENTITY `exp(ûθ/2)R*(x,τ₅) = R*(x,τ₅+θ/ω)` — exact, engine, generic config AND the quark axis `I₄B_q` — makes the observer's R-127 channel phase and R-131's phase modulus ONE U(1) (integrated form of R-125's fact 2a; NEW content = the same-U(1) bookkeeping killing the different-circle gap) ⇒ the channel pole's LABEL = the `ΔN = 1` tower step = ω exactly (R-131 cited live) → `k₄ = ω/c_meta` (R-123(i)); degeneracy carried by the R-126 moduli (overlap caveat inherited, no dimension citable); the ABSOLUTE tower-to-vacuum anchoring = a NAMED face (R-007 ontology + kernel-gated) — R-131's FRAMING PARTIALLY discharged; (uniqueness) the pole = the winding-1 sector GROUND STATE — every sector state ≥ M given (S)+(M) in the (Q)-semiclassical description (the ≥ M bound rides (M)+(Q) alone; classical sidebands ω−ν are not states); **(S)-static ENGINE-CERTIFIED in the breathing channel**: ℓ=0 Hessian strictly positive (form-eigenvalue ~0.21, resolution-robust, box-SATURATING 0.2171→0.2078 at boxes 24→80, core-localized below the B_eff(∞)=¼ floor) | DERIVED-A (clock-orbit identity + same-U(1) bookkeeping) + ENGINE-CERTIFIED-numerical ((S)-static breathing-channel bound; NOT DERIVED-A) + DERIVED-given-(Q)+(S)+(M) with (C1)/(C2') + R-127-locks inherited + LOCATED (residue (ii) → kernel faces (S/M/T-kernel) + anchoring face + ω≠0 co-rotating face; no structural face OUTSIDE the named premise set) | one_particle_pole_moduli_identification | D.4.6 (+ B.2.1 status note) | R-123, R-125, R-126, R-127, R-130, R-131, R-007 | — | Banked 2026-07-04 (twt-reviewer HOLDS on the core + OVER-CLAIM fixes F1–F8 — incl. a VACUOUS harness check caught (operator precedence; suite-dead-check class), the label-vs-anchoring split, the breathing-channel scoping, the (M)-premise honesty; reviewer's box-saturation probe recorded). Falsifiers: kernel spectrum with a sub-ω channel pole kills `m = k₄`; any sub-mass excitation in a one-particle channel (none observed — consistency anchor). Would change if: kernel spectrum computed; a negative/zero ℓ=0 mode at finer analysis; P2-4/R-141 decides the FR-family lattice. |
| R-143 | P2-4 leg 3 structural core — lattice-instanton access + DM background neutrality: the DM background carries **EXACTLY ZERO site-based topological density in each chiral sector at all θ_D** (ι-mechanism: the twist plane `r∧e₄` is e₄-reflection-BLIND while the 4-volume ε-pairing is e₄-reflection-ODD and ι is free ⇒ orbit-pair cancellation across the whole site-based density class — any holonomy-built Lie factor, any pseudoscalar pairing; 6912 individually O(1) terms, genuine cancellation; per-axis-class blocks vanish independently; variant-b also neutral by a SEPARATE numerical fact — not the ι-mechanism; genericity witness banked: a seeded-random homogeneous connection has Q₊ = +29.06/Q₋ = −62.48 — per-site neutrality NOT generic; generic parity would only give `q₊ = −q₋`); the D4 charge operator calibrates integer-EXACTLY as `Q_form(F) = 576·ε(F)` (pseudoscalar-pure; continuum norm 4π²; exactly gauge-invariant); an EXPLICIT compactly-supported SU(2)₊ singular-gauge winding-1 fluctuation over the background has exact SU(2)₋ transparency (`T_aP₋ = 0`), exactly-localized finite action excess (far-dev = 0.0), boundary map = the identity S³-map (banked π₃ degree 1), and measured charge → 1 (0.79/0.90/0.94 at ρ = 2/3/4, deficit ∝ 1/ρ²; in-suite regression 0.672); cross-term tensor in closed form `c(θ) = 4√2·a·sin²θ/sin a` (machine-exact across θ, reviewer sweep; third-θ pin banked) — the linear instanton–background coupling sourced by the 48/66 non-abelian excess, orientation-BLIND (no CP claim); located face: log(R) excess for uncut tails under the NAMED Wilson-class premise ⇒ compact support is the finite-action object; LATT-π₃ premise NAMED (strong-twist local reading not integer-faithful: 0.78 → 0.63 continuous in θ_D) | DERIVED-A (ι-mechanism; calibration identity; cross-term tensor + closed form; transparency/winding identities) + DERIVED-A-construction + CERTIFICATE (plateau → 1; dev record + in-suite regression) + LOCATED (linear-coupling face; Wilson-class premise named) + NAMED PREMISE (LATT-π₃) + FRAMING preserved (no minimizer/action value/size/rate — kernel-gated, R-140 fence inherited) | d4_lattice_instanton_access_and_dm_background_neutrality | C.4.6(iv) | R-088, R-103, R-140 | — | Banked 2026-07-04 (twt-reviewer HOLDS at the proposed tiers on all five claims + 4 record fixes F1–F4 applied; the reviewer's genericity attack PRODUCED the nonzero counter-example — banked as a check — and its θ-sweep verified the closed form to 1.8e-15; full dev record reproduced digit-for-digit). Leg 3 structurally closed; remaining face = instanton solution/action value (kernel-adjacent). R-088's ΔB = ΔL = N_gen selection rule now has its substrate carrier structurally in place (rate face gated). |
| R-144 | SC-1 second datum — the full-field, ansatz-FREE `B = 2` minimization of the banked dressed Skyrme static sector: the 3D functional certified as the banked sector (hedgehog reduction to R-135's `u/x²` = sympy identity on generic rays, in-suite; compact-profile discretization regression `h²`-convergent at N = 48→96 for both the hedgehog and the `z²` map); charge-conserving flow (SGD + exact Derrick rescaling, every step variational; charge-guard `\|ΔB\| < 0.04`) with no symmetry CONSTRAINT during descent stalls BELOW the two-defect threshold at matched grid — **stall-vs-stall margins 1.79% (N=64) / 3.06% (N=96, 30k-step continuation; E = 71.6169, virial 0.990, B_disc = −1.98198), ≥ 2.95% after the reviewer's B1-side continuation probe (banked; both stalls are upper bounds — "descent only deepens" was one-sided, reviewer-corrected F1; sign independently protected by the continuum anchor 72.923 > 71.617)** vs R-135's ansatz-reduced 1.89%; the minimizer found is the TOROIDAL B = 2 (ring r = 1.553, center 2.1% of max, sharpening; axial-init + cubic-grid qualifier banked, F2 — corroborative); R-135's would-change-if (c) FIRED (KEEPS the binding, deepening at N = 96); B = 1 regression N=96 machine-virial 1.00004, +1.3% of the banked 36.462 (same-grid comparisons the honest ones — the N=64 coincidence with the continuum is a recorded, understood cancellation). METHODOLOGY banked: lattice winding smooth-sector-protected only (two unwinding events, reproducible-on-demand incl. by the reviewer; charge-guard discipline load-bearing — the flow-level face of R-143's LATT-π₃ caveat); rigid fat-tail boundary artifact recorded (+12.6%), hence compact-support regression; margin values = stall-vs-stall records (rescale-free flows fake-stall at 6.8–7.3%), banked content = SIGN + ~3% order | DERIVED-A (reduction identity; h² regression) + DERIVED dressed-level VARIATIONAL full-field (below threshold; branch-(c)/hedgehog-minimality inherited from R-135) + STRUCTURE-corroborative (the torus) + SC-1-SECOND-DATUM scoped (STATIC face only; dynamical multi-defect EOM open, kernel-gated) + METHODOLOGY | full_field_b2_below_threshold_sc1_datum | C.1.2 (+ E.1.2/E.3 SC-1 rows) | R-135, R-133, R-120, R-050a, R-143 | — | Banked 2026-07-05 (twt-reviewer HOLDS at all five stated tiers + required fixes F1/F2 and recommendations F3–F5 applied; the reviewer independently re-measured all three saved fields digit-for-digit, ran its own B1-side continuation and unwinding-reproduction probes — both banked). SC-1 static face: two N = 2 data; remaining core = the dynamical multi-defect Cl(4,1) EOM (kernel-gated) + optional B ≥ 3 third datum. P2-7 magnitude residual SHARPENED: the classical full-field half done; remains beyond-rigid-rotor quantization + the massive full-field run. |
| R-145 | P2-2 structural half — the 6→4 frame reduction (first-order/Cartan face): the banked texture metric is EXACTLY a rank-4 frame square `g = δ + QᵀQ − PᵀP = Eᵀ κ E`, `E = [δ; Q; P]` (10×4, rank 4 ALWAYS — frame nondegeneracy, not metric nondegeneracy), `κ = diag(+1₇, −1₃)` (the 10 legs = the Janet–Cartan count as an ECHO only — legs not gradients, flat-frame factorization not an embedding); pointwise the grade-2 frame quadruple is FREE (`Ω_μ(0) = B_μ` coefficient-exact for exp-linear proper rotor fields); SIGNATURE-MENU theorem — `λ_max(g) ≥ 1` ALWAYS (the reviewer's stronger form of ≥1-spacelike, its adversarial optimizer floored at exactly 1; engine-asserted), negative index ≤ 3 ⇒ NONDEGENERATE menu `{(0,4),(1,3),(2,2),(3,1)}` with det g = 0 at transitions, **all-timelike (4,0) structurally excluded**, each item realized by an explicit proper rotor field; invariant Lorentzian threshold `‖P‖_op > 1` (necessary only; the family-free form of the banked θ₀ > 2 — NO perturbative texture is Lorentzian; light-cone birth at det g = 0); THE REDUCTION: signature (1,3) ⇒ canonical tetrad — `E = ι e`, `ιᵀκι = η` machine-exact, unique up to O(1,3) (tetrad-existence-per-metric already banked at texture_metric_vierbein — credited; NEW = the frame-level ι factorization + uniqueness + the ledger split) ⇒ the strategic map's "6→4 needs EOM" is SPLIT: the reduction is structural and selection-free, the EOM owes ONLY the signature pick; Maurer–Cartan FLATNESS `dΩ + Ω∧Ω = 0` SYMPY-EXACT (faithful Cl(4,0) rep, non-commuting family) + numeric generic MV field ⇒ both first-order variables (frame AND spin connection) from the ONE rotor field, Cartan structure equation automatic — the Gauss-equation face (Riem(g) from ∂E against flat Ω) = the NAMED next handle toward C_T (kernel-adjacent, not done); internal gauge action on the legs = compact SO(3)×SO(3) (`P → O_SDᵀP`, `Q → O_ASDᵀQ` — the map itself engine-asserted per reviewer F1; zero split leak; dets +1; g exactly invariant) ⇒ tetrad boosts NOT substrate-internal — local Lorentz emergent at the reduced description | DERIVED-A (extended-frame identity; pointwise freedom; gauge-action facts incl. the leg map; MC flatness sympy-exact + numeric) + DERIVED-structural (signature menu incl. (4,0) exclusion + λ_max ≥ 1; canonical reduction + O(1,3) uniqueness) + DERIVED necessary-condition (`‖P‖ > 1` threshold, convention-conditional on the banked c2 = +1; menu convention-ROBUST under c2-swap, reviewer-verified) + FRAMING (emergent-local-Lorentz reading, scope-guarded vs R-132 spacetime boosts; Janet–Cartan echo) + NOT-DERIVED (the (1,3) PICK — vacuum/EOM residue, named; menu vs pick) | texture_frame_6to4_reduction | B.6.6–B.6.7 | R-042, texture_metric_vierbein, equivalence_principle_protection | — | Banked 2026-07-05 (twt-reviewer HOLDS at ALL stated tiers + 3 required record fixes F1–F3 applied — F1 an engine-FALSE transpose in the claim-7 docstring, now the corrected map is asserted in-suite; F2 nondegenerate-menu qualifier; F3 prior-art credit — + recommendations R1 (λ_max ≥ 1 banked) / R2 (frame-vs-metric nondegeneracy clause) / R3 (this sync); the reviewer's own probes: 4000-frame sweep + Nelder–Mead (4,0) attack floored at exactly 1.0, c2-swap menu robustness, threshold necessity witness (0,4) at ‖P‖ = 2.07). Fence: no C_T, no absolute EH coefficient, no value (#1-gap as banked); U2 gauge-projection premise NOT discharged; the amplitude FRAMING sharpened (Lorentzian = finite-amplitude texture phase), not discharged. **SCOPE NOTE (2026-07-29, review item III-21 — probe-level, NOT engine-asserted; nothing banked):** the menu, the `λ_max ≥ 1` floor and the (4,0) exclusion are carried by the `δ` legs of the banked convention `g = δ₄ + c₂h` — the outside-frame Euclidean background of Axiom A-1a — not by `h`; on `η = diag(−1,1,1,1)` with the same `h` each of them reverses (an independent 20,000-frame probe sweep realises (4,0) 74 times on `η`, 0 times on `δ`). The threshold's VALUE additionally rides the undetermined `c₂` — `‖P‖ > 1` is the statement that the texture amplitude exceeds `1/√c₂`, a length the framework has not fixed. NEITHER point is a background inconsistency with §B.6.1's `g₀₀ = −1 + 2GM/r`: fact (5) IS the map — a Lorentzian texture metric reduces to `g = eᵀηe`, so §B.6.1's `η` is the tetrad frame of a finite-amplitude Lorentzian vacuum, and what is owed is only its VALUE = the already-named signature pick. What IS newly located (N56) is narrower: the threshold cannot bear on §B.1–§B.5 at all — that Lorentzian structure is the algebraic `φ` embedding, holds at every amplitude, and Part B carries no texture-metric dependence — so the kinematic (§B.1) and dynamical (§B.6.6) Lorentzian faces are separate and no map between them is constructed anywhere in the corpus: an OPEN coherence item. Would change if: vacuum EOM selects a non-(1,3) signature (kills the pick, not the menu); a substrate-internal tetrad boost is exhibited (kills the emergent-Lorentz reading); ~~the Gauss-equation face needs data beyond (E, Ω) (locates a first-order-scaffold gap)~~ **[FIRED-NEGATIVE 2026-07-05: R-149 executed the Gauss face — Riem(g) closes algebraically in (E, Ω, dE); no data beyond the scaffold needed]**. |
| R-146 | DM-V2-1 differential-coupling lead ADJUDICATED — clean structural negative + one located gap: the texture-metric source of ANY grade-2 excitation is IDENTICALLY its E·B-type L–Q cross term — `h(B_L,B_L) = h(B_Q,B_Q) = 0` exactly, `h(B,B) = 2⟨B_L I4 B_Q⟩₀` exactly (the banked P6 balanced-fact REWRITTEN in the EM basis; Hodge duality pairing a signed permutation ±1, engine-asserted incl. column-permutation per reviewer R1); `span(L)⊕span(Q)` = ALL of grade-2 (rank 6) ⇒ NO EM-orthogonal gravitating polarization; `\|h\| ≤ 2\|B_L\|\|B_Q\|` (Cauchy–Schwarz, saturated by pure SD/ASD — the maximally gravitating polarizations are exactly half-magnetic half-electric; gravity SD/ASD and EM L/Q splits maximally unbiased); `[SD_i,ASD_j] = 0` (all 9) while L/Q is not commutator-closed ⇒ no non-abelian rescue; COROLLARY: the transverse photon strain mode (E⊥B) is h-DARK at bilinear order; grade-3 doubly dead (A·T₃·B has NO even part — parity; the even substrate field can never produce grade-3 MC content ⇒ new-field scope gap, §E.1.3 posture REINFORCED); THE LOCATED GAP: the grade-0×grade-4 AMPLITUDE channel — a non-unit even excitation `a + c·I4` has MC form with ZERO grade-2 content yet `h = 2(aa′+cc′)(ac′+a′c)` (coefficient-exact); closed identically on unit rotors; DM-shaped (gapped Higgs-class) but DOUBLY conditional: #1-gap amplitude modes + the h-formula's grade-2-specific Schur scope | DERIVED-A (cross-term identity + pairing; rank-6; CS floor + unbiasedness + saturation; commutator facts; photon h-darkness; grade-3 parity kill + even closure) + DERIVED-structural NEGATIVE (no EM-polarization-dark gravitating excitation in the banked even unit-rotor content at the DIRECT-bilinear level — conditional on the photon-strain identification, U2, AND the open matter→h face of caveat (d), reviewer F1) + LOCATED-GAP/CANDIDATE (amplitude channel) | dm_differential_coupling_no_em_dark_texture | E.1.3 | R-042, R-145, photon_strain_mode, R-121/R-122 | — | Banked 2026-07-05 (developer-agent build + lead-session independent re-run + twt-reviewer HOLDS at all six tiers; F1 caveat-(d) rider + F2 same-pass sync + R1 permutation assert + R2 wording applied; the reviewer independently re-derived every identity with its own values incl. the amplitude-channel formula by hand). Includes the texture_metric_candidate SCOPE FIX (the "any even-grade field" over-generalization — engine-false for grade-0 MC content, reviewer-verified both directions). N40. Would change if: kernel amplitude modes; odd-grade content; U2 falls; the matter→h face resolves via indirect L–Q mixing (re-run). |
| R-147 | DM-V2-1 lead (ii) wave-train phase defects ADJUDICATED — clean negative; DM-V2-1's V2-era lead list EXHAUSTED: THE BLADE, NOT THE TOPOLOGY, FIXES h (a unit-amplitude phase defect `R = exp(B̂θ)`; topology fixes only ∮dθ; varying-blade defects still carry pure grade-2 MC — reviewer F1 probe) — blade table engine-exact (six coordinate bivectors h-null; SD/ASD ∓1; carrier blade `E = I4·e5` h-null, span{1,E} h-null even NON-unit); pure-L and E-phase dislocations h = 0 machine-exact (U2-conditional reading, c1-witness −0.64 nonzero, named); the ONLY gravitating dislocation (SD-blade chiral-ideal U(1)) has `h = −½dθ⊗dθ` EXACT with its ENTIRE h = the R-146 EM cross term POINTWISE (\|Ω_L\|/\|Ω_Q\| = 1) — topology buys no evasion; NO π₁ protection (π₁(Spin(4)) = 0, π₂ = π₀ = 0; `exp(e12π) = −1` exact; belt-trick unwinding homotopy engine-exact; negative survives the SO(4)/ℤ₂ OP fork — reviewer R1 probe) ⇒ nothing simultaneously gravitating, EM-dark, topologically protected (metastability cannot reopen DM — reviewer F2); KZ forms no dark network; SHARPENING: vortex cores naturally populate the R-146 amplitude channel (SD-core `Ω_r = s + sI4` automatic, h = 2sp digit-exact; balanced-blade core asserted I4-free) — but only EM-VISIBLE vortices force I4-core content ⇒ the single DM loophole carries TWO named EOM conditions | DERIVED-A (blade table; dislocation metrics; homotopy; core facts) + DERIVED-structural (π₁/π₂/π₀; KZ) + CONDITIONAL named (U2; the EM-visible cross-term reading inherited from R-146; E-phase-as-OP FRAMING, load-free) + CLEAN NEGATIVE | dm_wavetrain_phase_defect_negative | E.1.3 | R-146, R-123, R-042, R-145 | — | Banked 2026-07-05 (developer-agent build + lead-session re-run + twt-reviewer HOLDS at all tiers; F1 varying-blade generality + F2 topological-protection wording + F3 same-pass coverage + R1 π₂/π₀ + OP-fork robustness banked + R2 balanced-blade-core assert applied; the reviewer re-verified the belt trick on a denser 25×37 grid at 0.0). N41. Would change if: kernel EOM populates the amplitude channel from EM-dark cores (both named conditions); U2 falls. |
| R-148 | P2-3 sign face DECIDED-conditional-generic — `β₃ = μ d(1/e²)/dμ ≤ 0`, the AF-SIGNED branch; the wrong-sign risk for the qcd-UV arc REMOVED (conditional on I-13, revert clause named): machinery Weinberg-calibrated (series C24 = 1/48 ⇒ `M(π¹π² → π¹π²) = t/f²` exact); VERTEX SIGN DERIVED IN-SUITE (reviewer-forced correction): quartic-form coefficient +1 series-extracted at rational configurations + STATIC-ENERGY ANCHOR `E₄ > 0` tying the Minkowski Lagrangian sign `+(1/32e²)Tr([L,L][L^μ,L^ν])` to R-085's Hamiltonian-boundedness + slot = −1/4 COMPUTED; channel map `A_Skyrme(s,t,u) = −(s²/2 + tu)/(2e²f⁴)` (Bose s↔u; identical-cartesian channel identically zero) ⇒ POSITIVE forward weight `+1/(2f⁴)` — tree positivity SATISFIED automatically (the amplitude-side twin of R-085's bare sign); dispersive monotonicity (sympy-exact) ⇒ `1/e²(μ)` non-increasing in μ; l₁-mixing MOOT at forward order (l₁ multiplies t², vanishing forward — reviewer-verified independently); the sign's source is the ADDITIVE f²-loop drift, NOT antiscreening — SIGN-CONSISTENCY IS NOT AF-ACHIEVED; DGLAP + magnitude stay N7/Class 2 | DERIVED-A (anchored channel map + monotonicity) + DERIVED-conditional-GENERIC (β₃ ≤ 0 given P-disp/I-13 + P-action one-coupling + P-chan + P-conv; generic per canon §5 — any two-term chiral action; substrate content = the banked action IS that action + engine-exact weights) + LITERATURE-KNOWN-CLASS credited (Pham–Truong) + HARD FENCE + CORRECTION-HISTORY (first build REFUTED — Euclidean-sign transplant, N42; corrected build independently re-derived by a FRESH reviewer on separate code paths) | marginal_skyrme_beta3_sign_dispersive | C.5.2 | R-085, N7, I-13, banked two-term dressed action | — | Banked 2026-07-05 (first build REFUTED by twt-reviewer — five routes incl. static-energy kill; corrected build FRESH-reviewed HOLDS at all tiers — scipy-expm series confirmation, own plane-wave end-to-end map match, l₁-forward-zero verified, branch label attacked and survived). I-13 registered same pass; 13.3 KL row FIRED, a-theorem NOT PURSUED. N42 process lesson banked. Would change if: a new operator class with forward-surviving weight; the I-13 package fails inside-frame (revert to R-085's located gap); one-loop coefficient zero in channel; convention re-anchored. |
| R-149 | P2-2 Gauss-equation face EXECUTED — the R-145 first-order scaffold is CLOSED: `Riem(g)` of the texture metric is ALGEBRAIC in the pointwise first-order data `(E, Ω, dE)` — no derivatives of the FRAME DATA beyond first order (no ddE/ddΩ; the closure drops Riem from THIRD- to SECOND-derivative order in the rotor field — dE itself carries ddR, reviewer-F1 wording). THE CHAIN: (1) CURL CLOSURE `∂_μE_ν − ∂_νE_μ = −L([Ω_μ,Ω_ν])` (E LINEAR in Ω + MC flatness — for a generic non-flat connection the curl would be independent second-derivative data); (2) LEG-MAP INVERSION (the I₄ grade-2 pairing is the signed Hodge pairing ⇒ ALL of dΩ recoverable from dE); (3) GAUSS EQUATION for the induced torsionful metric connection `Γ̃^λ_{μν} = g^{λρ}κ(E_ρ, ∂_μE_ν)`: `R̃_{ρσμν} = κ(S_μρ,S_νσ) − κ(S_νρ,S_μσ)`, `S = (1−Π)dE` the κ-normal part (S NOT symmetric — the torsion is its antisymmetric part; classical subbundle machinery, hypotheses engine-checked, NO QFT import — registry-exempt per canon §2, and independently re-verified in-suite); (4) CONTORSION: `Γ_LC = Γ̃ + C` with C algebraic in `κ(E, L([Ω,Ω]))`; (5) the assembled full identity with `d_μC` itself algebraic in `(E, Ω, dE)` — verified end-to-end against an independent ddg computation, SIGNATURE-BLIND at ALL FOUR nondegenerate menu items (0,4),(1,3),(2,2),(3,1); NON-VACUOUS (Gauss and torsion blocks each the same order as Riem) | DERIVED-A (all five facts — each sympy-exact on a faithful-rep 2-parameter non-commuting family + numeric on generic three-factor rotor fields, Richardson-extrapolated FD) + FRAMING (C_T-skeleton: fluctuations enter the induced-EH spectral sum only through `(S, [Ω,Ω])` at quadratic order — the kernel's mode measure is the missing C_T ingredient, not kinematics) + NOT-DONE (C_T value / absolute EH coefficient — #1-gap as banked; the (1,3) pick; U2 untouched) | texture_gauss_equation_riemann_closure | B.6.6–B.6.7 | R-145, R-042 | — | Banked 2026-07-05 (twt-reviewer HOLDS at all stated tiers; required fix F1 applied — "no second derivatives of the rotor field" was engine-FALSIFIED by the reviewer's ddR probe (two fields with identical (R, dR) but different ddR give different Riem) and reworded to frame-data order; recommendation R1 applied — the (3,1) config added after the reviewer's own independent (3,1) run confirmed the closure at 1.7e-6; the reviewer rebuilt the whole pipeline FROM SCRATCH on its own rotor fields incl. an FD-computed MC form and a large-amplitude stress config max\|Riem\| ≈ 42, all four signatures). First executed move of the Class-2 program (2a: statics cornering the kernel computation's FORM). R-145's would-change-if (3) FIRED-NEGATIVE. Would change if: a proper-rotor-field class breaks MC flatness while keeping the banked g (reopens the face); C_T needs the fluctuation expansion beyond quadratic order in S (skeleton true but partial); vacuum EOM lands non-(1,3) (the reading's target moves, the identity is unaffected). |
| R-150 | Class-2 route-2b campaign dashboard (W2.1) — the kernel OVER-DETERMINATION TABLE: N33's prose meta-result GRADUATED into a checkable, self-validating engine artifact. Ten registry constraints on the #1-gap driven-dissipative kernel, each a structured row (observable; banked kernel_link; value/bracket; frequency_window; frequency_justification; independence; status ∈ {usable-anchor, structural-target, bracket-only, candidate-anchor, numberless, non-anchor, future-falsifier}; is_usable_anchor; caveat). Exactly ONE usable anchor (the KSS/GW bracket — itself not numerically closed: reconciling the η/s-floor with the η-ceiling needs an unstated entropy density s) against a ≥2-parameter causal kernel ⟹ RANK-DEFICIENT by ≥1 dof (= N33's headline; robust: `rank_deficient` holds whether the honest count is 1 or 0). Anchor-counting discipline enforced by LIVE guards: sin²θ_W = 3/8 gate-free ⇒ EXCLUDED (the exact N33 miscount); g/α_s/α_W folded into the single unknown α via g² = 4πα·(8/3); τ_mem [3,380] NOT a target (N34). Carries N33's four named missing inputs (the campaign's acceptance criteria) + the FDT-forbidden/KK-safe jurisdiction (I-12: Θ_rel IS the FDT-violation residual). | FRAMING (over-determination dashboard; the anchor-count operationalizes N33's judgment) + DERIVED-A (live engine cross-validation of the sharpest row values — Kc ratio = (19/2)√38, running µΨ₀ decreasing/sign>0/ratio>2, Brannen 0.28% — + the two exclusion guards: sin²θ_W gate-free, alpha_em_value GATED-raises) | kernel_overdetermination_table | — (companion §4 over-determination opportunity / §12 Class-2 program; not paper-body — a dashboard, not a paper-worthy physics result) | N33, N34, N37, N32a, R-149, R-138, R-111, R-134, im_chi_falsifier_budget_KSS_GW_macromolecule, Kc_magnon_stiffness_canted_FM_at_DJ, I-12 | — | Banked 2026-07-05 (twt-reviewer HOLDS at the proposed tier and scope — independently rebuilt every load-bearing check on the engine; sole finding a cosmetic open_cat1_kernel cite, fixed same pass). First move of the Class-2 (2b) infrastructure; the campaign's live dashboard. NOT a kernel value, NOT a new anchor, NOT a resolution of the rank deficiency — a census. The count increments when a genuine new (frequency, value) anchor (N33 input (3), e.g. the W2.2 static sum-rule datum) is manufactured. Suite 397→398 (twt_algebra 31). |
| R-151 | W3.1 — the C_T mode-measure MOMENT COUNT (the P2-2 endgame's first quantitative reduction): the R-145 internal symmetry `SO(4)_tangent × SO(3)_SD × SO(3)_ASD` — a PRODUCT (the fact-(7) gauge rotates leg-values tangent-index-free, so it commutes with SO(4)_tangent; NOT a locked diagonal, which the verifiers computed at ~21–29) — forces R-149's C_T integrand (a quadratic form in the fluctuation data `S_sym ⊕ [Ω,Ω]`) into an **8-dimensional space of invariant quadratic forms** (S-block 4, [Ω,Ω]-block 4, cross 0 by SO(4)-irrep disjointness Sym²4={(3,3),(1,1)} vs Λ²4={(3,1),(1,3)}), split **4 parity-even + 4 parity-odd** (SD/ASD channels exchanged by parity; the su(2)⊕su(2) block structure `[SD,ASD]=0` IS the substrate I4-Hodge split — I4·SD=+SD, I4·ASD=−ASD — engine-exact). CONSEQUENCE: *given the unbroken product symmetry*, C_T (parity-even) is a kernel-weighted combination of **at most 4 numbers** — C_T's kernel-dependence reduced from an unknown FUNCTION to ≤4 NUMBERS (an UPPER BOUND: treating (S,[Ω,Ω]) as general over-counts in the honest direction; the spin-2/Ricci sub-projection pins the exact ≤4). | DERIVED-A (su(2)⊕su(2) block-exact + the COUNT given the group, exact commutant algebra + seeded character MC) + DERIVED-given-R-145-fact-(7) (the product group; a dynamical diagonal-locking would raise the count) + FRAMING (spin-2/Ricci sub-count = would-sharpen) | ct_kernel_moment_count_symmetry_reduction | B.6.7 | R-149, R-145, R-124 (commutant method), chirality_is_a_reflection (parity), texture_frame_6to4_reduction fact (7) | — | Banked 2026-07-05 (THREE independent methods via a Workflow fan-out — exact commutant + basis-independent solver; analytic Clebsch-Gordan; Reynolds character MC — reproduced 8 / 4+4 / cross-0, confirmed the product group by [tangent,value]≈2.2e-16 + the locked-alternative ~21–29; twt-reviewer HOLDS at the stated tier — rebuilt the count by a 4th method (hand irrep-decomposition), verified fact (7)'s g-invariance and the I4-Hodge split (substrate-specific, NOT generic-given-4D), and confirmed the ≤4 upper-bound framing is fenced everywhere). Would change if: a substrate-dynamics diagonal-locking shrinks the group; the spin-2/Ricci projection pins the exact ≤4; cubic-order fluctuations grow the space. Suite 399→400 (twt_cosmo 95). |
| R-152 | W3.2/A2 — the µΨ₀ ρ_L SEAT INTEGRAL (R-129's "remaining construction: the §D.4.4 boundary integral on an explicit profile") COMPUTED on the banked Q-orbit baryons (R-133 hedgehog, R-144 torus). The LITERAL §D.4.4 (V2 §10.5) scalar ρ_L boundary term `ρ_L = ⟨Ω³⟩₀` VANISHES IDENTICALLY on any Q-orbit rotor field (`e₁₄·e₂₄·e₃₄ = −I₄` grade-4 ⇒ the Q-orbit su(2) winding density is PARITY-ODD / I₄-valued, scalar part 0; profile/geometry-independent — hedgehog, squashed, B=2-twist all give `⟨Ω³⟩₀ = 0` to ~1e-14) — a CLEAN NEGATIVE confirming N32a "ρ_L sources L-orbit winding, not Q-orbit baryon winding" (physically: a baryon has B≠0 but L=0). BUT the R-128 parity-odd Hodge-dual quark-lock (I₄·Ω) recovers the scalar L-winding EXACTLY (`⟨(I₄Ω)³⟩₀ = \|⟨Ω_L³⟩₀\|` to ~1e-15) ⇒ the corrected seat FORM `L_θ = µΨ₀·B_Q`, parity-odd, linear in the integrated winding B_Q (π₃ degree). The `⟨⟩₀` scalar-grade projection is TWT's standing trace convention (§D.4.4/R-109 defines the whole medium Lagrangian with it; the gravity sector uses ⟨Ω I₄ Ω⟩₀) — the vanishing is a genuine consequence of the banked L/Q = Hodge-grade split, not a definitional artifact. | DERIVED-A (Clifford core: `e₁₄e₂₄e₃₄=−I₄`, the literal-seat vanishing, parity-odd winding, exact Hodge-recovery) + the PHYSICAL seat identification INHERITS R-128's OWN FRAMING tier (the up/down-seat + µΨ₀-through-the-lock tie are FRAMING; NOT promoted) + value µΨ₀ #1-gap GATED (∝B_Q ⊥ generation index ⇒ does NOT give N37's inter-gen running) | updown_seat_rhoL_parity_odd_hodge_form | C.3.13 (+ §B.3.1, §D.4.4 note) | R-128, R-129, R-110, R-109, N32a | — | Banked 2026-07-05 (W3.2/A2, twt-reviewer HOLDS + 2 wording softenings applied: seat-FORM reads as conditional on R-128's FRAMING µΨ₀-tie; "linear" is of the integrated B_Q not the local density; the reviewer independently reproduced the grade decomposition — L-hedgehog Ω³ pure grade-0, Q-hedgehog Ω³ pure grade-4 same magnitude — and confirmed the ⟨⟩₀ convention is banked upstream). Resolves R-129's "pointed to not confirmed" ρ_L seat: literal seat = clean negative; Hodge-dual seat FORM derived; value + N37 running stay #1-gap gated. Suite 401→402 (twt_spectra). |
| R-153 | The #1-gap kernel CANDIDATE FORM (the KS selection campaign, Grade B): `Im χ(ω)` odd, passive, KK-causal, IR exponent s ≥ 3 (the Adler/Goldstone floor), UV cutoff — *constraints-by-construction* (the hard properties exact by construction, never filtered after); three spectral members — nodal algebraic-edge `xᵖ/(xᵖ+1)` (p ≥ 3), s-wave exponentially-gapped edge, and their positive composite — plus the EXCLUDED edge-less reference (kstar, culled by the two-sided D3 test) | CANDIDATE (Grade B — a surviving CLASS, not a pinned kernel) | kernel_candidate_form | E.5 | R-113, R-114, R-115, R-118, R-030 | R-154, R-155, R-156, R-157, R-158 | Banked 2026-07-22 from the simulator KS campaign (commits ec11cfc…1ae53b7; every phase adversarially reviewed to consensus; corpus frozen throughout per the campaign's RULE 1; simulator suite 144→172). The Section-12 Class-2b closure route EXECUTED. Selection within the class is NOT supplied by the executable scores (R-157). |
| R-154 | Composite closure: the constraints-by-construction properties (oddness, passivity, KK-integrability/causality, s_IR = 3 Adler floor) are CLOSED under the positive Goldstone+magnon summation `[nodal(p=3) + r·swave]/(1+r)` — the F2 edge-class fork DISSOLVES into a single measured ratio r (r=0 → nodal exactly; r→∞ → swave; boundary recovery exact) | DERIVED-A (the closure property; sympy + numeric witnessed) + CANDIDATE/FRAMING ("the substrate kernel IS this two-sector sum" — the SN-16 grounding) | kernel_composite_closure | E.5 | R-153 | R-155 | The candidate's one algebraic-DERIVED content (with the exact-by-construction hard properties); everything about the *selection* stays CANDIDATE. Mirrors the simulator witness `kernel_space.composite_closed_under_summation`. |
| R-155 | The counted candidate economy: genuine dials = IR exponent p, edge width wT, UV plateau width W, memory time τ_mem (+ the composite ratio r); one redundant edge scale exactly absorbable (SN-15 — NOT a dial); ONE binary INPUT bit = the hysteretic memory branch (the F4 PICK; the **Koide `c = √2`** menu-vs-pick pattern — exemplar swapped 2026-08-21, since `weak = SD`'s menu was computed and CLOSED under C-32 and no longer illustrates an open menu — consistent with §D.5.3's adopted working branch: a pick, NOT a derivation); minimal member = 2 dials + 1 bit | INPUT/FIT (candidate-scoped: counted within the candidate's OWN ledger; joins the §E.2.1 framework ledger ONLY if the candidate is adopted) | kernel_candidate_dials | E.5 | R-153, R-115 | R-156 | The fading class is dropped from the space by the pick; the campaign's bathless forcing attempt (KS-0a) remains FRAMING/CANDIDATE — the pick is NOT upgraded to derived. |
| R-156 | Constraint provenance, scoped (2026-07-31, E-7): every member passes the constraints-by-construction SUBSET by construction (C1 causality/KK, C2 memory, C3 s≥3, C4 passivity; C5 near-KSS is compatibility-not-confirmation with `η/s` gated — so on the inventory's own full pass criterion the candidate is label-level covered, NOT passed); the 3 channel TARGETS ((19/2)√38 ≈ 58.56 [N31]; Λ~H² c ≈ 2.05 [N33]; ≤ 4 spin-2 C_T moments [R-151]) stay GATED — the candidate supplies form-side inputs only; the numbers are never fitted (their kernel→observable maps are themselves #1-gap objects) | CANDIDATE/FRAMING | kernel_candidate_constraints | E.5 | R-153, R-114, R-040, R-150, R-151 | R-157 | The registry over-determination activates only when a gated forward map is built (the Class-2b promise, honestly conditional). Fitting a channel target through an unbuilt map is reward-hacking — forbidden (campaign T-any). |
| R-157 | The reading-conditional executable RANK-DEFICIENCY: under the F-strong (optimistic, two-sided) flatness reading a plateau class survives (kstar culled); under the ADJ-1-OPERATIVE (one-sided ceiling) reading the executable flatness selects NOTHING; the a_e discriminator CONFOUNDS τ with p in a free-scale search — the F1 (exact-3 vs ≥3) and F2/r (edge-class/ratio) forks stay OPEN; discrimination deferred to the virgin band (P1) + the fixed-τ a_e ratio (P2) | FRAMING (confirmed BY SEARCH over 344 candidates, not merely asserted) | kernel_overdetermination_table | E.5 | R-150, R-156 | R-158 | Exactly the registry's own `n_usable_anchors = 1` situation (R-150) — the sanctioned Class-2b state; BOTH readings must always be stated together. |
| R-158 | Seven pre-registered virgin-sector falsifiers P1–P7 (two-commit git-proven: REGISTER `27e2847` strictly before EVALUATE `7f2d52d`) + the two-sided D3 edge-less cull: P1 μeV-band knee vs the SC-persistence ceiling (consistent-structural), P2 a_e two-point ratio (separates the classes at fixed τ; external test FUTURE), P3 knee·τ_mem train-cadence (FUTURE), P4 mass-frequency containment (consistent), P5 activated driven-rate landscape (FUTURE), P6 near-KSS (compatibility NOT confirmation — η/s gated; the commitment STANDS, no renegotiation), P7 the dissipative generation route (structural pass) — NO MISSES on the evaluable-now set {P1, P6} | CANDIDATE (register + outcomes; every magnitude gated) | kernel_candidate_falsifiers | E.5 | R-153, R-157 | — | An edge-less substrate kernel finding would kill the class (the structural falsifier). The paper's near-KSS commitment (§E.3.3 VG-1) is not challenged. JURISDICTION HEDGE (N49/KC-1 class, load-bearing): P1's SC-persistence ceiling and R-157's superallowed-flatness datum are INSIDE-frame data — they bind the outside-frame kernel only through the un-built outside↔inside projection; the numeric comparisons gate on exactly that leg. |
| R-160 | Born exponent = 2 as a theorem: F2+F3 ⇒ additivity (coarse-graining) ⇒ Gleason ⇒ `Tr(ρP)`; F4 ⇒ `ρ = \|ψ⟩⟨ψ\|`. No power-law family assumed anywhere; dim-2 sectors inherit through the joint system–detector sector | DERIVED-conditional-on-(F1–F4) + import-exempt pure math (Gleason 1957) | born_exponent_gleason_closure | B.3.3 | R-021, R-023, R-029 | R-027 | **F2** (statistical noncontextuality of the Role-3 selection functional) is the single NEW substantive premise; it does NOT follow from §B.3.1 frame-equivalence — covariance ≠ noncontextuality (engine counterexample). F1 carries single-outcome definiteness; F3 = total function on the JOINT lattice incl. entangled contexts (not "mild"). The coarse-graining reduction is literature-standard, not TWT-novel. Supersedes R-023's "plausibility-modulo-degree". **CARRIER-BACKGROUND INHERIT-NOTE (RUL-035; K-O1 keeper L2):** F3's total-function premise fails on the comb `x₄ = (2n+1)π/(2k_c)` under a reverse-referenced functional (all channels identically zero — no normalized weight exists there); under the ruled adjoint `t` the reference is carrier-free and F3 is unobstructed. Fires only when a carrier background is admitted into Part B; trivial-background content unchanged. |
| R-161 | P1b SPLIT — the mass-phase lock channel carries exactly the induced-term theorem's mass-form structure: quark lock axial / lepton lock vector *relative to the winding assignment*; R-128's parity dichotomy extended from 3 lattice axes to generic coset directions; lepton exclusion hardened at the 4-doublet count | DERIVED-A (the Cl(4,0) identities) + DERIVED-CONDITIONAL (the channel reading) given C1′+C2′+C3′+C4′ | lock_channel_is_axial_chiral_channel_p1b_split | B.3.5, C.4.6 | R-127, R-128, R-002, R-141 | R-141 | The dichotomy is **winding-assignment-relative**, not intrinsic (the lepton generator has axial form about its own dual axis); the intrinsic load-bearing facts are quark-line U-slaved phase at ω vs lepton-line coset-phase-blindness, riding R-002's L/Q assignment. C4′ = roster colour modes' local winding = the baryon field's local coset orientation. **P1b-DYN** (the mode determinant actually generating the term) stays CANDIDATE and carries all dynamical load. No sign is produced by these identities (L1–L3 / N35 honored). Lepton hardening is 4/12 only, NOT 6/18. |
| R-162 | Coupling-sector channel disjointness: `⟨X I₄ X⟩₀ ≡ 0` on the colour sector; signed `⟨B I₄ B⟩₀ = \|B_ASD\|² − \|B_SD\|² = 2⟨B_L I₄ B_Q⟩₀`; EM = spin-1 multiplicity-2 block vs coset-5 = spin-2 multiplicity-1 block, cross-invariants 0; blocks dimensionally inequivalent (6 vs 5) ⇒ no intertwiner under any subgroup chain | DERIVED-A (the channel classification) + LOCATED-GAP (the α_s fold-in reduction) | coupling_sector_channel_disjointness | B.5b.3 | R-035a, R-081, R-085, R-151 | — | Closes the symmetry route to a derived shared-condition: the fold-in is equivalent to ONE named kernel property (cross-block rigidity) **plus an OPEN cross-block weight** (the missing 8/3-analogue). Conditional on the gluon-FRAMING channel assignment + the couplings-as-Im-χ-moments FRAMING. Scenario-scoped: the zero-cross statement is Spin(4)/spatial-SO(3); under Z₃-only — and a fortiori N10's Z₃-broken NESS — crosses are allowed-but-unforced (count 10). Two-point / magnitude-source scope ONLY, never the running or AF face. Vindicates the 2026-07-26 audit demotion of the fold-in. |
| R-163 | Induced-EH coefficient computed on the framework's own DERIVED linear face: the proper-time integral over the derived D4 NN band converges with no regularization choice entering the flat-band measure; I-3's premise triple → two named assumptions | DERIVED-given-the-NN-band-INPUT (flat-band numbers) + DERIVED-conditional-on-(OA-LF-i ∧ OA-LF-ii) (the EH-coefficient reading) | induced_G_from_linear_face_band | B.6.2 | **R-102** (via N_eff = 6 → c_lat → Λ_L), R-112 (inherits its isotropic-projection conditional, D-1 2026-07-31), R-037, R-041 | — | **OA-LF-i** = NESS occupation is the ground-state one (a statement about the STATE); **OA-LF-ii** = covariant curvature coupling at grain scale (about the OPERATOR) — carries ~93% of the integral's support, i.e. the old regulator freedom RELOCATED and localized, not removed. "Regulator-free" describes the flat-band measure ONLY. Bracket stays CANDIDATE/conditional; inherits R-041's FRAMING+CONDITIONAL. In §B.6.2's own normalization this reads c_reg ≈ 1.8; the convention-invariant statement is that the grain spacing is Planckian within O(1). **RECONCILIATION CLOSED (2026-07-29) + WHICH-Λ RULED (2026-07-30):** this `c_reg ≈ 1.8 = c_lat/12` and `sakharov_induced_gravity`'s `1/12` are ONE coefficient in two `Λ`-variables (`Λ_L = 1/a` vs the proper-time `Λ_S`); the apparent factor ~21.6 was the variable ratio `c_lat`, not a physics gap (`c_reg_from_substrate_mode_content`). The coordinator's ruling assigns `Λ_S = √(2π) M_Pl` to Sakharov/`G` bookkeeping and `Λ_L = 1/a ∈ [0.39, 0.73] M_Pl` (OA-LF-ii band) to the lattice-dispersion consumers per the scoped §B.6.2 assignment; the R-037 wide bracket is RETIRED. Gapless-shared-band idealization — canted-vacuum (N_G = 2) refinement softens it by tens of percent. Method externally validated (Z⁴ tadpole reproduced to 2e-8; independent Monte Carlo). Reproduction status: the `c_reg = 1/12` settlement stands on a single pass — its adversarial verification round terminated without a verdict, so it has NOT been independently reproduced (the paper states the gap in present tense at §B.6.2). Retirement handle: a cross-class re-derivation of `a_1 = 6·(R/6) = R` from the six grade-2 `so(4)` channels. |
| R-164 | The banked Skyrme quartic contains NO tree-level Einstein–Hilbert term: quartic (Killing-built, parity-EVEN) and `√gR` (h-built, parity-ODD) fall in disjoint sectors of the R-151 invariant space with exactly zero overlap; nonperturbative kills at all four menu signatures | DERIVED-A (decomposition / orthogonality) + DERIVED-structural (the EH-ABSENT verdict), conditional on U2 + the banked Ω-algebraic action class + the {cc, R², Ric², Riem²} menu quantifier | skyrme_quartic_contains_no_tree_EH | B.6.6 | R-042, R-107, R-109, R-149, R-151 | — | Mechanism: the definiteness that makes the quartic a Derrick stabilizer is exactly what makes it EH-blind — stretching vs bending elasticity, with the Sakharov loop the standard generation of the second from fluctuations of the first. Kill chain (sequential, do not compress): parity/S-block disjointness ⇒ λ=0 at quadratic order; ddR-freeze ⇒ λ=0 nonperturbatively vs a cc term + any Ω-algebraic remainder; one-blade family ⇒ λ=Λ_cc=0 with Gauss–Bonnet the sole surviving direction; frozen-quartic sweeps ⇒ GB dies. R³/∇Riem-class fall to the same dE-independence schema but were NOT run. Sole-route consequence is CLASS-SCOPED (a new dE-dependent term or the Paper-2 thermodynamic route would reopen it). Negatives ledger **N51**; probes preserved at knowledge/candidates/probes_2026-07-27/. |
| R-165 | Lorentz-violation orders separated: D4's bond-set **fourth** moment is EXACTLY isotropic (`M_1111 = 12 = 3 M_1122`, residual 0), which `Z⁴` is not — so rotational anisotropy is pushed past dimension six to **dimension eight**, `(E/Λ_L)⁴ ≈ 2.0×10⁻³¹` at the loose corner of the ruled `Λ_L` band (`0.39 M_Pl`; which-Λ ruling 2026-07-30) and smaller still at its tight end; but the **rotationally invariant** dimension-six residual `η⁽⁴⁾ p⁴/M²_Pl` (equivalently `c·p⁴/Λ²`) is protected by neither R-016 nor D4 and is #1-gap GATED | DERIVED-A (the lattice moment identities AND the invariant-space dimensions, exact) + **DERIVED-conditional-on-(P-an ∧ P-pg)** for the dimension-eight *inference* + INPUT (published n = 4 bounds, import **I-19**) + GATED (the dim-6 isotropic coefficient itself) | d4_lattice_lorentz_violation_orders | B.1.5, B.6.3, B.6.4, E.3.3 VG-6, E.3.5(4) | R-004, R-016, R-112 | R-016, R-039, R-112 (`eom_constraint_class` H4 + E1) | **Two results in one, of opposite sign.** POSITIVE: the reason is REPRESENTATION-THEORETIC, not a kernel model (canon §3 — the nearest-neighbour-Laplacian argument was a model and is NOT what this rests on). `\|Aut(D4 root system)\| = 1152 = \|W(F4)\|`, whose invariant degrees `{2,6,8,12}` make the **degree-4 invariant space one-dimensional** (only `(k²)²`) — so symmetry forces the quartic isotropic for ANY point-group-symmetric analytic kernel, whatever the dynamics. The degree-6 space is 2-dimensional and D4's sixth bond moment is anisotropic (residual 12), so dim-8 is REACHED, not merely an upper bound — checked on both sides. Substrate-specific, not generic: `Z⁴`'s point group `B4` admits a 2-dimensional degree-4 space containing `Σk_i⁴` (and `N_1111 = 2`, `N_1122 = 0`, moment residual 2). **TWO PREMISES, named not buried — (P-an)** analyticity in `k`, i.e. a derivative expansion exists (a non-analytic driven-dissipative memory kernel, the #1 gap itself, is NOT covered by a polynomial-invariant argument); **(P-pg)** the FULL point group INCLUDING TRIALITY — `W(D4)` (order 192) alone has a 3-dim degree-4 space, and the shell-2 sub-orbits `{±2e_i}` and `(±1,±1,±1,±1)` are each anisotropic (residual 32 apiece), cancelling ONLY at equal weight, so a substrate coupling weighting triality-related orbits unequally would RESTORE dim-6 anisotropy (N52 risk note); **(P-gs)** the ground state preserves the point group (added 2026-07-31, D-2): the §D.4.3 spiral vacuum BREAKS it — the species-universal `O(q²)` stiffness splitting is absorbed by the I-22 rescaling class, and the space-fixed (sidereal) residual is exactly SC-2's open question. NEGATIVE: the isotropic dim-6 term is unprotected, and at dimension six species-universality is **not** a symmetry (the induced velocity shift `≈ (3/2)η p²/Λ²` is momentum-dependent, so no rescaling removes it; Stecker's constrained combination is `η_π − 25η_p`, i.e. `−24η` for universal `η`, not zero). Setting the SUBSTRATE coefficient `c` to unity gives `η⁽⁴⁾ = c_lat/(2π) ∈ [1.9, 6.7]` (ruled `Λ_L = 1/a` band), excluded by 3–9 orders — reported ONLY to size the exposure, never as a prediction. **(Λ NOTE, 2026-07-28 → 2026-07-30: the 2026-07-28 pass widened the bracket to `Λ ∈ [0.13, 2.5] M_Pl` over a reduced-vs-non-reduced Planck-mass unit fix PLUS what was then read as an unreconciled three-way `c_reg` disagreement. The 2026-07-29 pass CLOSED the `c_reg` half: `c_reg_from_substrate_mode_content` computes `a_1 = R` on TWT's own linear face, giving one value `c_reg = 1/12`, with `≈1.8` the same coefficient written in `Λ := 1/a` and `~1` a never-computed placeholder. The coordinator's 2026-07-30 which-`Λ` ruling then assigned the lattice-dispersion quantities that produce THIS exposure `Λ_L = 1/a ∈ [0.39, 0.73] M_Pl` and RETIRED the wide bracket — this row's numbers are re-cut accordingly. Two caveats stand: the `c_reg` settlement is ONE-PASS ONLY (its adversarial verifier died mid-response) and it is tier-CAPPED by R-041, whose shift symmetry — not the substrate dynamics — is what excludes the conformal corner. See R-037.)** The defect form factor supplies `(f_π/m_p)² ~ 10⁻²` (two orders where six to nine are needed across the ruled band) and supplies NOTHING for the photon, which §B.5.4 makes a **bulk** strain mode with no internal structure — the most exposed sector, not the exempt one. NORMALIZATION (the two conventions must not collide): `η⁽⁴⁾` is the coefficient of `p⁴/M²_Pl` (Liberati); the substrate's own form is `c·p⁴/Λ²` with `c = O(1)`; hence `η⁽⁴⁾ = c·(M_Pl/Λ)²`, and "natural coefficient unity" means `c = 1`, NOT `η⁽⁴⁾ = 1`. FRAME: the **inertial**-frame question is a coherence WIN (the bounds are CMB-frame and the framework's τ₅-foliation IS the comoving frame, §B.4.5); the **jurisdiction** question is separate and hedged — these are INSIDE-frame inferences bounding an OUTSIDE-frame object through the un-built outside↔inside projection, so the exposure is named per canon §0a while its BINDINGNESS stays conditional (I-19 premise (e); same hedge as §E.3.1 rows 7–8). Supersedes the pre-2026-07-27 §B.1.5/§B.6.3 gloss and DELETED §E.3.1 rows 1–2 (documented V1→V2 drift, not fabrication: V1's "`10⁻¹⁵` to `10⁻²⁰`" dim-4 range had its **loose** end promoted to "the tightest matter-sector bound"). Negatives ledger **N52**; adjudication record `knowledge/audit/UHECR_VERDICT_2026-07-27.md`. **PRIOR ART, added 2026-07-29 — the physics is NOT original here.** The D4/F4 lattice's suppression of rotational cutoff effects relative to the hypercubic lattice is established lattice field theory: Neuberger, *Spinless fields on F(4) lattices*, Phys. Lett. B **199**, 536 (1987); used since by Celmaster, by Bhanot-Bitar-Heller-Neuberger, and by Klomfass; and live today in Katz & Nogradi, *QCD on the 16-cell honeycomb* (arXiv:2512.10604, Dec 2025), which states the dispersion form directly (first failure at `O(a⁴)`, not `O(a²)`). The 24-cell as a spherical 5-design is classical (Delsarte-Goethals-Seidel 1977). Both citations verified (INSPIRE / arXiv API). What R-165 claims as its own is NARROWER: the kernel-independent invariant-ring form (covering improved actions and radiative corrections at once), the two-sided sharpness (dim-8 REACHED), the explicit (P-pg) triality premise, and the transfer into LIV-EFT language. An external reviewer's "genuinely new and publishable on its own" verdict does NOT survive the lattice literature. Standalone treatment: `knowledge/corpus/D4_lattice_quartic_isotropy.md`. **POINTER (J,D/Γ rework, 2026-08-21): the trigger for re-examining this row's dimension-eight inference is the DRESSED entry coefficient of the driven-group Γ survivor — the named piece held at §D.5.7 (tree level gives `0/0`; #1-gap-routed, hence CANDIDATE by definition). No claim is adopted here about WHICH premise of the forced-isotropic-quartic theorem a nonzero survivor would evade: that question is under separate arbitration and this row records only the pointer.** |
| R-167 | The Bell wing is the `e_4`-commutant qubit, not the phase sector. `Z_{Cl⁺(4,0)}(e_4) = span{1, e₁₂, e₁₃, e₂₃} ≅ ℍ` is real dim 4 = **complex dim 2** for R-020's complex structure (right-multiplication by `B_a`), `ℂ`-basis `{1, e₁₃}`, with the one-sided L-orbit rotor action `= SU(2)` (unitary, det 1) and right-multiplication by `exp(αB_a)` the global phase. `span{1, B_a}` is `ℂ¹` and CANNOT host a wing: it is commutative, so the left measurement rotor IS §B.3.1's global phase and every rotor-rotated state is one ray (Hermitian modulus 1 at every angle), and `Λ²(ℂ¹) = 0` so no singlet exists there. NO NEW INNER PRODUCT IS NEEDED: §B.3.3's own complex overlap `z(ψ,D) = ∫⟨D̃ψ⟩_{{1,B_a}} d³r`, applied unchanged on the commutant, IS the `ℂ²` Hermitian inner product (agreement 9.9e-16 over 500 random pairs, engine-checked inside the banked primitive). The half-angle SURVIVES: `⟨ψ_a\|ψ_b⟩ = cos(Δθ/2)` under that same formula, no grade truncation, once the measurement rotor leaves the phase plane. The singlet pairing `ε(u,v) = ⟨u·j, v⟩` with `j ∈ {e₁₃, e₂₃}` (RIGHT multiplication — the antilinear structure) is antisymmetric + `ℂ`-bilinear + `SU(2)`-invariant. R-020's `{1, B_a}` is exactly the `ℂ`-linear Schur commutant of that `SU(2)` (dim_ℝ 2), so the enlargement spends NO uniqueness | **DERIVED-A** — the wing algebra (commutant dimensions, the `ℂ`-structure, `SU(2)` unitarity, the half-angle as an honest `ℂ²` Hermitian overlap, the identity of §B.3.3's own `z(ψ,D)` with that `ℂ²` Hermitian form, the symplectic pairing, the Schur commutant, the charge grading) consists of exact Clifford identities, banked 2026-07-30 as a `twt.py` primitive with two suite checks (suite 460 → 462). The `Z(e_4)` module restriction remains a named CHOICE, not a derivation. The two-wing TENSOR PRODUCT and the SINGLET SELECTION remain IMPORTS (N53; `bell_correlation` stays FRAMING) | `bell_wing_needs_the_e4_commutant_qubit` — banked 2026-07-30, 2 suite checks in `check_twt_spectra`; `half_angle_overlap` swept in the same pass (retiered: it returns the GRADE-0 part, i.e. the degenerate `ℂ¹` case this row rules out) | B.3.1, B.4 | R-020, R-021, R-011, R-127, R-160 | R-027, R-029 | Resolves the `ℂ¹` vs `ℂ²` contradiction N53 flagged and left explicitly unresolved. Discharges the charge-sector half of §B.3.1's own named open item: under `U(1)_{B_a}` the eight even blades split charge-0 `{1, e₁₂, e₃₄, I₄}` / charged `{e₁₃, e₁₄, e₂₃, e₂₄}`, and the set-aside residue shrinks from six blades to the four that FAIL (W) — `{e₁₄, e₂₄, e₃₄, I₄}`, i.e. R-128's three Q-orbit winding blades together with `I₄`, the operator that implements its lock. COSTS NAMED: (S) must not be imposed on the STATE (phase-plane rotors are diagonal in the `ℂ`-basis and fix `ψ_0 = 1` up to phase, generating no second state — a measurement is by construction an (S)-violating rotation); `ψ` becomes a two-component complex field, so R-024's envelope reduction needs an added named premise that the linearized operator is `ℂ`-scalar at leading order; and the analyzer angle is no longer a rotation in the transverse winding plane. HONEST LIMIT: with `ψ_0 = 1` and real rotor angles the states explored span a REAL two-plane inside `ℂ²`, so the second complex dimension is needed for CONSISTENCY (a projective space with more than one point; `Λ² ≠ 0`), not because the wing sweeps all of `ℂ²`. R-127 undisturbed and sharpened: the mass phase is the global `ℂ` scalar and commutes exactly with the spin action. REJECTED ALTERNATIVES: full `Cl⁺(4,0)` (`ℂ⁴`, but four blades fail (W)); the charge-0 sector `{1, e₁₂, e₃₄, I₄}` (that is the (S)-commutant, and `e₃₄`, `I₄` fail (W)); the FR-odd `j = 1/2` collective band of `L²(SU(2))` (dim 4 = `ℂ²_spin ⊗ ℂ²_iso`, but it is an ALREADY-QUANTIZED collective space — circular for §B.3 — rides the unregistered Finkelstein–Rubinstein / Atiyah–Hitchin imports flagged in N53, and is hadron-scale, so it is the baryon sector's tool and not the lepton wing's).). **★ ANNOTATED 2026-08-23 (R-172; ADAPT verdict — the algebra only). ALGEBRAIC COINCIDENCE, stated in C-33 form:** the set `span{1, e₁₂, e₁₃, e₂₃}` occurs in two different roles — here as this row's wing **MODULE** inside `Cl⁺` (`Z_{Cl⁺(4,0)}(e₄)`, real dim 4), and in `weak_host_must_be_body_frame` as the even right-**STABILISER ALGEBRA** of the minimal left ideal `S = Cl·s₀` (real dim 8). Same four blades, two roles; **verified to be the identical set**. That is worth recording and is all that is adopted. **NOT adopted, on evidence: (i)** "the Bell construction is *already* a body-frame construction" — **wrong side**: this row's `su(2)` is the **one-sided L-orbit rotor action acting on the LEFT**, with right multiplication supplying only the global phase `exp(αB_a)` and the antilinear singlet pairing; **(ii)** "on the minimal-ideal carrier" — **wrong carrier**: this row's module is `Z_{Cl⁺}(e₄)` (real dim 4), not `S` (real dim 8); **(iii)** "R-167's named CHOICE of the `Z(e₄)` restriction becomes a consequence of the carrier node" — it does not follow, because the carrier node's `Cl⁺` reading is not `S`. Reading the same four blades as a module in one place and as an acting algebra in the other is precisely the **module-conflation class C-33 exists to stop**. **★ AND AN ORPHAN, recorded here and riding the (unopened, escalated) carrier node:** this row's REJECTED ALTERNATIVES clause rejects **full `Cl⁺(4,0)`** as the wing carrier, while A-P2′/RUL-091 makes **full `Cl⁺`** the internal host's module. **Reconcilable by ROLE** — Bell-wing module vs internal-host module — **but the reconciling passage does not exist**, and it is owed before any pick at that node. Neither this row's tier nor the `Z(e₄)` restriction's status as a **named CHOICE** is changed by any of the above. |
| R-168 | No spin(4,1)-invariant positive-definite pairing exists on Cl(4,1); `t = α₅∘reverse` IS positive-definite on all 32 blades (`⟨X t(X)⟩₀ = Σx_A²`, exact anti-involution), Spin(4)- and E-phase-invariant, boost-NON-invariant — while reverse is boost-invariant and indefinite: positivity is bought by selecting the `e₅` axis, exactly as the Dirac adjoint selects `γ⁰`. Sign tables: reverse negative on exactly the e₅-containing blades; conjugation flips grades 1/3 (positive on E and the Cl(4,0) bivectors, e_i5 stays negative); E central in the FULL algebra ⇒ no commutator-quartic backstop for wrong-sign E-content (banked-functional quantifier fence) | **DERIVED-A** (theorem + tables) + **INPUT** (the RULED cost convention: pairing (iv) `⟨Ω t(Ω)⟩₀` adopted 2026-08-12, reversing the 2026-08-03 pick (iii) — a counted named pick on a four-option menu; restricted to Cl(4,0) it IS the banked reverse pairing, so the hadronic spine is untouched; boost-covariance duty CARRIES; the (iii)-era gapless-mode duty is VOID) | cl41_pairing_sign_tables + cl41_positive_definite_pairing (12 checks in check_twt_algebra incl. the leak identity) | A.5.6, D.1 | R-127, R-147 | every carrier/moving-defect cost bookkeeping; R-169 | Banked 2026-08-12 (ADJUDICATION3 §2a; ruling R1). Refutes the probe-7 "every involution fails" universal. Pick justification = the TWO-LAWS/NESS meaning-note (worklist): first law = the NESS's steadiness read through the lock, second law = its drivenness; a costless carrier leaves the H8/NESS licence idle. Carrier volume energy `(k_c/2)²` = a Λ-like face, FENCED (no Λ derivation); texture-invisible (R-147 h-null). Defect costs are VACUUM-SUBTRACTED under (iv). |
| R-169 | Moving-defect outside cost laws. SHEAR (pattern) family: `E₂ → (1+v²/3)E₂`, `E₄ → (1+2v²/3)E₄` exact; total `E₀(1+v²/2)` at Derrick balance, TERMINATING at v² — so translational inertia = `E₀` at `O(v²)` IFF stress-balanced (von Laue in Euclidean form), and "close to γ" on a translated pattern carries no evidential weight. TILT (isometry) family, slice held fixed: `E(θ) = E₀·secθ = E₀√(1+v²)` — pointwise density identity + measure Jacobian; the SO(4)-invariant object is the 4-volume ACTION (divergent for a static tube), never the banked 3-slice `E₀`. All three laws agree at `O(v²)`; they split at `O(v⁴)` as `(0, −1/8, +3/8)` (shear, tilt, γ) — the relative sign is N56's energetic face (third surfacing). The leak identity `\|g₂(BAB⁻¹)\|² = \|A_⊥\|² + cosh²ζ\|A_∥\|²` — over-count `= sinh²ζ\|A_∥\|²`, hence **strict iff `A_∥ ≠ 0` AND `ζ ≠ 0`** (the bare "iff `A_∥ ≠ 0`" was a FALSE iff, refuted by the primitive's own `ζ = 0` row; corrected at the P6-1 repair 2026-08-21) — explains why the 8b γ-criterion was unreachable by construction | **DERIVED-A-given** (hedgehog isotropy + grade-2 cost sectors; x₄-independent rest density) — the shear identities are FENCE-IMMUNE (profile-independent); the leak identity is flat DERIVED-A | pattern_shear_sector_identities + tilt_family_fixed_slice_cost_law + boost_projection_leak_identity (7 checks in check_twt_matter + 4 in check_twt_algebra) | A.4, B.1/B.6.6 (the map gap) | R-132, R-168 | mass_equals_elastic_cost_premise; the N56 third surfacing | Banked 2026-08-12 (ADJUDICATION3 §2b; ruling R2 — amends the 8b-round prior `E(v) = E₀`, a two-integrals conflation). The tilt is the isometry-generated NAMED family, not established as "the" moving defect (that is the N56 map question). Under ruled (iv) the laws hold for the vacuum-subtracted cost. VARIABLE NOTE (τ₅ adjudication 2026-08-13, keeper L2): this row's v is dx₁/dx₄ (the tilt variable); the τ₅-route's v = dx₁/dτ₅ is a DIFFERENT variable joined only by the wavefront lock — the O(v⁴) split (0, −1/8, +3/8) is stated in THIS row's variable, and no τ₅-route coefficient enters it without the lock-bridge stated (N61). |
| R-170 | ℤ3 harmonic collapse + the reparametrization-invariant Brannen phase: at N=3 the second harmonic aliases into the first (`cos(2φ_n−ψ) ≡ cos(φ_n+ψ)`, both conventions), so `(b,ε,ψ)` is a 3→2 map at fixed Λ and ψ is NOT FIXED BY THE MASS SPECTRUM (mass-gauge; ψ still parameterizes model observables — eigenvector orientation in the CKM constructions); the mass-observable content of a ℤ3 triple is the resultant `(A, ψ_inv)` = its 3-point DFT, `ψ_inv = atan2((1−ε)sinψ, (1+ε)cosψ)`, computable model-free ≡ Żenczykowski 2012 Eq. (12). Down sector: MS-bar indicator-triple invariant `ψ_inv,d = 6.294°` (mixed-scheme: m_d, m_s at 2 GeV, m_b at m_b; scheme-dependent ≈5.8–8.5°; indicator-level, canon §5), vs the CREDITED hadron-route band \|δ_d\| ≈ 5.8–8.5° (physical channel, probe 5, brackets 4/27 rad); both ≪ `δ_L = 12.73°` — the `ψ_d ≈ δ_L` clause struck over-determined. Cross-route: `A_d = 1.546 ⇒ K_down = (2+A²)/6 = 0.7318` (reciprocal 1.367). Convention scope: FOUR ε-variants in-corpus; 2ψ-form PHASE STRUCTURE derivation-backed (FORM only — coefficient sign is the unpinned e₄-dip axis, keeper L2); inter-convertible only under re-fit; r²-orbit amplitude cap A ≤ 1 → located gap N60 | DERIVED-A GIVEN the two-harmonic form (generic N-point aliasing, not a Clifford/D4 identity) + arithmetic on banked FIT inputs (values indicator-level, scheme-labeled) | brannen_z3_harmonic_collapse_invariant (2 checks in check_twt_spectra) | C.3.10 | R-064, R-066, R-068, R-073 | R-073 (corrected clause), N60 | Banked-pending 2026-08-13 (ψ-repair pass, ADJUDICATION2 keeper C1; §8a round: reviewer HOLDS-with-fixes, MO referent fixes incl. the 6.294° model-free confirmation, keeper collision fixes — all executed; coordinator provenance correction applied: hadron route outranks the indicator invariant). Prior art credited: Żenczykowski PRD 86 (2012) 117303 (non-observability + Eq. (12) closed form), PRD 87 (2013) 077302 (δ_D vs δ_L comparison), Koide J. Phys. G 34 (2007) 1653, Brannen 2006, Rosen MPLA 22 (2007) 283 (the struck all-δ-equal hypothesis class); internal antecedents koide_from_c/dft_K_from_r. δ_d RULED (RUL-033, 2026-08-13): δ_d ≔ the hadron-route/physical-channel object; ψ and ψ_inv,d are WITNESSES, never carriers; 4/27 = its candidate rational point ("lands within 0.03°", never "brackets"). |
| R-171 | **The weak-`su(2)` menu is CLOSED**: exactly three conjugacy classes of 3-dim Lie subalgebra exist in grade-2 `so(4)` — `{SD, ASD, the diagonal so(3) class = {Stab(v)}}`, computed by a finite Goursat sweep whose Lie-theoretic inputs are the engine-exact structure constants `T = c·ε`; ASD is the SD mirror under an orientation-reversing reflection (residual 2.2e-16, `I₄` sign flips) so the menu is TWO classes up to `Aut(so(4))`; and the diagonal class is refuted by the right-handed fermions' weak-isospin-singlet character. ★ Includes the correction that a single-Weyl neutrino **cannot** discriminate: `rank(SD\|W₊) = rank(L\|W₊) = rank(union) = 3`, while `rank(SD\|W₋) = 0` vs `rank(L\|W₋) = 3` | DERIVED-A (the classification and both refutations) **GIVEN premise A-P2′-RIGHT** (FRAMING in the engine; **stamped ENDORSED, RUL-084** — a preferred direction, so this row sits in the CORE+ENDORSED column; **sharpened 2026-08-23, RUL-091**: the premise now names the MODULE and the SIDE) + INPUT (the right-handed-singlet datum) [side ruled RUL-091: body-frame/right action on the even-module ideals; left reading retired; chirality structure carried by the `H±` ideal split — ADJUDICATION_R3 §4-bis. **The classification itself is side-independent** — it is a statement about 3-dim Lie subalgebras of grade-2 `so(4)`, so it carries to the body copy VERBATIM; what the ruling corrects is the PHYSICAL READING of the module, not the enumeration] | weak_su2_menu_exhaustion | C.4 | R-009, R-010, R-075, R-076, R-099 — R-075 supplies the chirality↔Weyl-half identification without which "right-handed" has no referent, R-076 the two-ideal occupancy without which the datum does not bite | R-079, R-078, R-060, R-061, R-077 | The engine ground of the C-32 exhausted-menu promotion of `weak = SD`. Four suite checks, each with a demonstrated failure mode (simplicity dropped ⇒ 5 tuples not 3; the vector module instead of the spinor module ⇒ the kernel discriminator inverts; an inner rather than orientation-reversing element ⇒ no SD↔ASD exchange; the Weyl-half restriction dropped ⇒ union rank 6 not 3). Controls inside the primitive: dropping reality/compactness takes the sweep 3 → 6 classes, and `so(3)` gives 1 — an enumeration that returned the same menu under a broken premise would not be enumerating. **Conditioning class (RUL-049):** "exactly three" holds WITHIN grade-2 `so(4)`; hosts outside the substrate's own rotation algebra are untouched, unexplored and unstamped. |
| R-172 | **WHICH SIDE THE WEAK HOST ACTS ON — computed, closing the transfer R-171/RUL-091 asserted.** R-171 closed the menu of 3-dim `su(2)` hosts inside grade-2 `so(4)`; it never asked on which SIDE of the carrier the host acts, and RUL-091 ruled the side (body/right, on the even-subalgebra module) while naming the engine primitive as OWED. This is that primitive. **(1) The defect:** with the lock in the **BANKED GRADE-ONE realization** (`J_i = −½e_jk`, `K_j = ½e_j`, a Cl(4,0) *vector*), a chiral factor acting by LEFT multiplication fails to commute with the lock — `[L_J, L_SD]` **6 of 9** and `[L_K, L_SD]` **9 of 9** nonzero (**6 of 9** on the boost rows under the grade-two realization `K_j = ½e_{j4}` — nonzero either way, so **the conclusion is realization-robust and only the counts move**, computed not asserted), and identically `J₁ = −½e₂₃ = (+¼e₁₄ −¼e₂₃) + (−¼e₁₄ −¼e₂₃)`: every lab rotation IS half an SD rotation plus half an ASD one. **(2) The repair is associativity at full strength:** `max\|[L_g, R_h]\| = 0` **exactly over ALL `g, h` in the 16-blade basis**, not merely over the host's generators — a body-frame host is Lorentz-scalar *by construction*. **(3)** The body copy is the **opposite** Lie algebra (`[R_X,R_Y] = −R_{[X,Y]}`), isomorphic via `X → −X`, so R-171's classification carries over verbatim; `I₄` central in `Cl⁺` ⇒ the same SD/ASD split there. **(4) The owed transfer, COMPUTED:** on the **`I₄` grading** of `Cl⁺`, `image_dim(R_SD\|W₊) = 3, (R_SD\|W₋) = 0, (R_ASD\|W₊) = 0, (R_ASD\|W₋) = 3` on the **OPERATOR-SPAN** reading (`4/0/0/4` on the image-subspace reading — the word carries two readings and both are returned), and the LEFT action gives the **identical** table ⇒ the annihilation is an ideal fact and IS side-independent, as RUL-091(iii) claimed and no primitive computed. **(5) Bimodule identities, ALGEBRA ONLY:** the `L` and `R` Casimirs on `W₊` are the **same** scalar (−6 in the NAMED normalization `u_a² = −1 − I₄`, so the VALUE is normalization-dependent and the load-bearing content is the **EQUALITY**) and both vanish on `W₋`; `W₊` is irreducible under `(L_SD, R_SD)` jointly (generated algebra dim 16 = `End(W₊)`). **(6) Controls:** `hosting="space"` returns the nonzero tables (the shipped failure mode, run in the harness in the same breath); `carrier="S"` returns a **different verdict** — the even right-stabiliser of `S = Cl·s₀` is the `e₄`-commutant `span{1,e₁₂,e₁₃,e₂₃} ≅ ℍ`, ONE `su(2)` charging **both** halves (the qualifier *among even elements* is load-bearing: the full stabiliser is 8-dimensional), i.e. the diagonal-class occupancy the singlet datum kills | **DERIVED-A** (the commutator tables *on the banked grade-one lock realization*; the associativity identity; the opposite-algebra identity; the `I₄`-ideal image dims *on the operator-span reading*; the `Cl⁺`-vs-`S` right-stabiliser computation; the bimodule Casimir-equality and joint-irreducibility identities *on the `I₄` grading*) **+ DERIVED-structural CONDITIONAL on {CORE LS, CORE S3 via §B.1.3 in the grade-one realization, A-P2′-RIGHT (RUL-091), the carrier node, the right-handed-singlet datum as scoped by its FAMILY INPUTS register row}**. ★ **Two conditions carried INSIDE this cell** (keeper's binding rider): the **lock realization** (the conclusion survives either, the quoted counts do not) and the **`I₄`-grading ↔ observer-chirality bridge, which is UNBUILT** — computed here: with the banked grade-one boosts the observer's Lorentz action does not even preserve `Cl⁺` (`leak(L_K, Cl⁺) = √2`, `leak(L_K, W±) = 1`) while the rotations do, and `so(1,3)` is simple over ℝ, so the `I₄` grading has **no** Lorentzian real counterpart. **`W±` is the `I₄` grading and is NEVER to be restated as the observer's chirality.** ★ **NOT tiered here, and not in the engine at all: the physics reading of (5).** Promoting the bimodule to a statement about one-defect STATES consumes step **S4** (the defect's collective manifold = the full `Spin(4)`), which is **UNBUILT and #1-gap-routed**, against the corpus's only built band (the one-inertia ANW band) — it is **CANDIDATE**, it lives on the OPEN V4-ASD family-tree node, and no CORE string carries it | `weak_host_must_be_body_frame` (banked 2026-08-23, 8 suite checks in `check_twt_weak`, the failure demonstration run in-process against `hosting="space"`); **and, riding the same pass, `lock_left_centralizer_is_u1`** — the left-centralizer theorem `Z_left(so(1,3)) = span{1, e₁₂₃} ≅ ℂ` (dim 2, commutative, a U(1) never an `su(2)`), which RUL-091 cited as a **ground** for retiring the left reading while it was **unbanked**; that phantom cite is now closed, with its own demonstrated failure mode (drop the boosts and the answer moves 2 → 4) | C.4 | R-171, R-167 (the `e₄`-commutant `ℍ`), R-102 / R-012 (the `S` carrier), R-075, R-076, §B.1.3 (the lock generators), §B.3.5 (the one-sided observer action) | R-079, R-078, R-060, R-061, R-062, R-077, `weak_su2_menu_exhaustion`'s MODULE AND SIDE block (iii)/(iv)/(v), **and the right-handed-singlet datum's FIVE prose/returned-value sites** — `TWT_foundational_paper.md:5163`, `TWT_core_paper.md:468`, `twt_core.py`'s EMPIRICAL LEG docstring, `twt_core.py`'s `empirical_leg` returned string, `twt_test.py`'s diagonal-class-kill message — **all five scoped to the datum's own register row in this pass** | **The record's own defect, closed.** `weak_su2_menu_exhaustion`'s kernel numbers are computed on the 4-dim spinor module under the LEFT (matrix-on-column-vector) action — the retired reading — while the RULED hosting is RIGHT action on `Cl⁺`; the transfer was **argued** ("an ideal fact, hence side-independent") and **computed nowhere**. Part (4) is that computation, and it is the strongest single argument for the row. **The primitive's MODULE AND SIDE block is the record; this row cites it and does not restate it.** **Provenance:** drafted at external review 2026-08-23 (Fable-class, `knowledge/reviews/twt_body_frame.py`); every DERIVED-A claim independently recomputed at exact zero by a cross-class verification pass (Opus) that imported no engine code, and again by the coherence keeper; integrated per `VERDICT_KEEPER_BODY_FRAME_2026-08-23.md` + the verification's §CONSENSUS. **What did NOT move:** R-171's classification and both refutations; R-079's tier; **R-058's tier and its posited `T₃` slot (P7)** — the draft's claim that R-172 dissolves R-058's `1 ⊕ 3` objection is **REJECTED** (different referents: R-058 is about the meta-time rotor pair, R-172(5) about `W₊` on the even module; the re-carrying primitive remains OWED and CANDIDATE); the `dim Λ²₋(ℝ⁴) = 3` count and §E.3 row 13; the ANW band; **any value, any scale, any falsifier count.** **What this does NOT license:** any scale or mass; hosts outside grade-2 `so(4)`; any promotion of (5) to states; **and no demotion of `generations = ASD`** — the body move commutes the ASD copy with the observer exactly as it does the SD copy, so what the body-ASD triple carries is an **OPEN** node (family tree, V4-ASD), not a demotion. Negatives ledger: **N63** (the refuted left/space-frame route). **RESTATED AT FAMILY LEVEL in Core §2.4** (2026-08-24 revision pass): the paragraph *"Which side the host acts on is computed, not assumed"* carries the associativity/commuting identity, the retirement of the space-frame reading, the side-independence of the discriminator, and **three fences** — the collective-coordinate scope, the 3-dim-host scope (a larger two-scale host is outside it, not refuted by it), and the module/realization fence carrying **the open carrier node and exposure E-2** (on the even-subalgebra reading a vector-realized boost does not preserve the module, so there the invariance is inherited from the algebra rather than tested on the module). The `U(1)` descriptor is **not** used at the paper site — it is grade-one-specific (grade-two gives `span{1, I₄} ≅ ℝ⊕ℝ`), and the realization-robust content is *dim 2, commutative, never an `su(2)`*. |
| R-173 | **★ ONE RESULT, TWO INSEPARABLE HALVES. (i) NO GEOMETRIC CEILING ON THE BRANNEN AMPLITUDE IS A SUBSTRATE PROPERTY — the reachable `c` is dominated by the UNBANKED M-3 commitment** (how the CELL-layer meta-time ℤ₃ generation phase acts on the GRAIN-layer helix configuration). On the banked `{J,D}` reduced energy at `D/J = 0.787`, GLOBAL-vacuum subtracted: `c ≤ 1.216468` on closed combs whose step is a **translation** (exhaustive over the 80 non-degenerate classes of `D4*/3D4*` with a free base point), against `c ≤ 2.000000` (`1.827129` under a non-degeneracy guard) on closed combs whose step is an **order-3 affine map** `h(k) = ρk + t`, `h³ = id` — on which **`c = √2` and `K = 2/3` are ATTAINED EXACTLY and non-degenerately** (exhibited point HIT B, `min/mean = 0.2608`, closure exact to machine epsilon). The two closed readings **straddle** the Koide point, differing by a factor `1.64`. The two ray-scan numbers (`1.303371` unit-gear, `1.994608` at `λ = 2,5`) are **WITHDRAWN by both parties** — `λk̂ ∉ D4*`, so they are not ℤ₃ orbits at all. A fifth row — any order-3 map outside `{translation, ρ·translation}` — is **NAMED AND UNSCANNED**. Riding inside: the **period lattice `= 2π·D4*`** as a Fourier-support theorem, and the 81/80 residue enumeration with `ℤ⁴ → D4*/3D4*` an isomorphism | **CANDIDATE** (the commitment dominance; the screw as a generation mechanism, legality OPEN) + **FIT, COUNTED — 2 of 6 consumed, NEVER DERIVED** (the hit on the measured triple) + **DERIVED-numeric** (each maximum; `|t|*`, `|t|_c`) + **DERIVED-A** (the period lattice; the EIGHT order-3 symmetries; lattice-`t` mass blindness; the `π/12` window; `rank(N) = 2`) — conditioning class: the banked `{J,D}` reduced energy, `D/J = 0.787`, the single-`q` simple-bivector family (RUL-049: multi-`q`, conical, non-simple-`B` unscanned), the D4 siting. **CANDIDATE-half by consumption; no `CORE_PROVENANCE` row** | `brannen_comb_commitment_dominance_and_dof_vacuity` (RENAMED 2026-08-23 from `brannen_amplitude_is_M3_commitment_dominated` when the vacuity kill superseded the commitment-dominance as the operative finding) — **12 suite checks** in `check_twt_matter` (5 amplitude-half + 5 joint-search + 2 inseparability-guard); the mandated inequality `1.216468 < √2 < 1.827129` is asserted INSIDE the primitive so the numbers cannot be separated; the period test is SEEN TO REJECT at `2π(½,½,0,0)`; the order-3 enumeration is SEEN TO REJECT at a non-symmetry of the same 1152 group (`3.34 > 1`); and an **AST-level INSEPARABILITY GUARD** fails if `measured_triple_attained` and the vacuity keys are ever returned by different functions — demonstrated firing on THREE planted splits, in-suite in memory and on-disk at `closure_scripts/cl_01` | C.3, D.4.3 | R-065, R-066 (`c = √2` NOT independently forced — six routes negative), R-064, `canting_vacuum_branch_structure`, `mass_equals_elastic_cost_premise`, `generation_z3_is_metatime_phase`, `brannen_z3_harmonic_collapse_invariant`, N60 | — (a negative about forcing; nothing builds on it) | ★ **THE ROW EXISTS TO STOP A SENTENCE.** *No clause of the form "c = √2 requires structure outside the banked family" may be added to the Koide rows* — that claim is **FALSE** and this row refutes it. `c = √2` remains a **COUNTED, UNFORCED INPUT** (canon §2, §7); this is the **SEVENTH negative forcing route** (after R-065/R-066's six) and the **SECOND non-negativity amplitude cap** (after **N60**, whose scan T2′'s MAP-E re-ran uncredited and whose SCOPE line is T2′ §3.6's escape — `TONGUES_T2PRIME` §LINEAGE). ★ **MASS-RATIO CAVEAT, load-bearing:** every `c` in the AMPLITUDE half is `c` ALONE — matching `K` is ONE equation, the ladder is TWO. The two exhibited `√2` screw points give √m ladders `1 : 7.83 : 235.62` and `1 : 1.56 : 85.66` against `1 : 206.77 : 3477.37`, so no configuration measured in the AMPLITUDE dispute came near the ladder. ~~**N64/T2's RATIO KILL IS UNTOUCHED**~~ **[SUPERSEDED by the closing round — see the EXTENDED block at the end of this cell: the JOINT `(c, δ)` search REACHES the ladder exactly. RUL-049 conditioning, in the same sentence: the cannot-reach form of the kill does not survive ON THE SCREW FAMILY, whose generation-legality is an OPEN COORDINATOR CALL, and is UNTOUCHED on the TRANSLATION-STEP family; it is REPLACED by a dof/VACUITY kill, never removed.]** What the amplitude dispute demolished is the *explanation* offered for the kill. ★ **OPEN COORDINATOR CALL (RUL-030 class 3), not pre-empted:** does canon §5's *"L-orbit blades are never generation LABELS"* extend to *"never inside the generation STEP MAP"*? The screw is generated by an L-orbit blade (`G_generator`'s spatial ℤ₃, DERIVED mass-blind — and at `t = 0` it splits nothing, computed) yet is the **literal corkscrew** of the originator's image. That one ruling selects between the two closed rows — **and the closing round makes it CHEAP: the family buys nothing, so excluding it forfeits nothing.** Committing to the screw is **CORE-touching** (RUL-048: branch node + plain-language sign-off first). **Provenance:** the four-round §8a estate dispute, closed with nothing contested — `VERDICT_REVIEWER_ESTATE_2026-08-23.md` (verdict + addendum §R5.4), `TONGUES_T2PRIME_2026-08-23.md` (§CONSENSUS, §CONSENSUS-R4), enacted per `ESTATE_BANKING_2026-08-23.md`. Both sides' subtraction defect (ray-minimum instead of global vacuum) is corrected here, and the correction produced the cross-check that the axis `λ=1` value **equals** the translation-closed maximum. **The 45° kinematic bridge has no computed face** — same-day addendum, N64 (Y5). ★★ **EXTENDED 2026-08-23, THE CLOSING ROUND (the joint `(c, δ)` search + its ratification, five passes, nothing contested) — AND THIS IS THE HALF THAT MAY NEVER BE QUOTED APART: (ii) THE MEASURED CHARGED-LEPTON LADDER IS ATTAINED EXACTLY ON THE CLOSED SCREW FAMILY — `1 : 206.768282988 : 3477.365266602` against the identical measured values, `log-err = 0`, on ALL EIGHT order-3 symmetries, at 19 mutually-distant solutions plus 14 more from the ratification round's INDEPENDENT solver — ON A 4-DIMENSIONAL SOLUTION MANIFOLD RETURNING `0 of 19` SM QUANTITIES.** 6 free reals (`k₀` 4 + `t`'s `ker(N)` components 2) against 2 constraints (`K` is not a third — `K = (2+c²)/6` identically); the mod-`L` reduction removes redundancy, not dimension. **THE KILL IS JACOBIAN-ATTACK-PROOF BY COUNTING ALONE:** a `2×6` Jacobian has rank `≤ 2` identically, so `dim ≥ 4` AT EVERY SOLUTION whatever the rank is; rank 2 (measured) is the MAXIMUM, i.e. the LEAST vacuous case available, and any rank DROP makes the manifold LARGER. **Widening the family makes the kill STRONGER** — a widening adds parameters or branches, never constraints. ⇒ **THE NEGATIVE IS REPLACED, NOT REMOVED, AND THE REPLACEMENT IS OF A DIFFERENT AND STRONGER CLASS:** no longer *"the geometry cannot reach the data"* (a reachability kill) but *"the geometry reaches the data with four spare dimensions, so reaching it is worth nothing"* (a **dof/vacuity kill**). **RUL-049 CONDITIONING, carried in the same sentence wherever this is stated:** batch 1's kill in its *cannot-reach-the-data* form does not survive **on the SCREW family — whose generation-legality is an OPEN COORDINATOR CALL**; it is **untouched on the TRANSLATION-STEP family**, where the ladder remains unreached. T2P-1 (the first-harmonic `c = 1` theorem) is untouched throughout. **THE PITCH ESTATE, riding inside:** `L = ker(N) ∩ 2π·D4* = 2π·A₂` hexagonal (DERIVED — a half-integer `D4*` vector has no zero coordinate, so it cannot meet `{x₄ = 0}`), minimal vector `2π√2 = 8.885766`, covering radius `5.130199`; **lattice-`t` mass blindness DERIVED-A in three lines** and shown to be a **MEASURE-ZERO KNIFE-EDGE** (`c = 0` identically ON the lattice; `max c ≈ 2` already at reduced pitch `0.10`) — so 100 % of the splitting rides the NON-LATTICE part of `t`; `|t|* = 0.616296` (isotropic to 0.09 %, measured at NON-SYMMETRIC angles because 60° spacing is `ρ`'s own symmetry and would have manufactured it) vs `|t|_c = 0.702693`, ⇒ **★ `δ` BINDS BEFORE `c` DOES BY `1.1402` — the one strategic finding of the whole dispute: every ceiling in four rounds measured the WEAKER face**; the `δ`-window at `c = √2` is the FULL non-negativity window `[0, π/12]`, saturated and empty outside, so **the substrate contributes exactly ZERO constraint beyond `E₀ ≥ 0`**; and screws must be quoted **reduced mod `L`** (`9.08/15.61/15.28/15.78 → 0.6268/0.4448/0.4482/0.6036` — all four published points are ONE small-pitch regime the raw coordinates concealed). **The step-form count is EIGHT, not two** (1152 / 96 / 8, rebuilt from scratch by both sides), with the exhaustiveness ARGUMENT repaired to run through `ρᵀ(D4) = D4` and the scope tightened to **"exhaustive of the order-3 linear SYMMETRIES of `E_reduced`"** — the `ρ³ = I`-without-symmetry class is strictly LARGER and DECLARED UNSCANNED. **`min/mean = 0.040350` is NOT corroboration** (a function of `(c, δ)` alone) — and it is **below the 5 % non-degeneracy guard the dispute imposed on every `c`-maximisation**, i.e. that guard would have excluded the physical target (the reviewer's finding against its own instrument; promoted to a standing class in `TWT_CHECKER_CALIBRATION.md`). **RUL-098 accounting: consumes 2 of the 4–6 budget and compresses NOTHING; net yield NEGATIVE** — by the corpus's own MAP-G vacuity control (4 free INTEGERS, VACUOUS BY CONSTRUCTION), `log-err = 0` on 6 free REALS is MORE vacuous. **`D/J = 0.787` is NOT corroborated by the hit** — the 6 reals absorb everything. **What would convert it (NAMED, NOT COMPUTED):** the quark/CKM comb on the SAME parameters, or the neutrino phase with none new, or a #1-gap kernel cutting the 4 spare dimensions, or an independent structure FIXING the pitch (which would make `|t|*` a falsifier). **No further SINGLE-SECTOR work on this family can change its status: the branch is not blocked, it is EMPTY at single-sector resolution — and that makes the OPEN coordinator call CHEAP, since excluding the family forfeits nothing.** Governing records for the extension: `SCREW_JOINT_SEARCH_2026-08-23.md` (+ `screw_joint_scripts/` and its frozen pre-registration), `VERDICT_REVIEWER_ESTATE_2026-08-23.md` **SECOND ADDENDUM §S1–§S8** (the closing ratification: all three keystones re-derived independently and RATIFIED), enacted per `ESTATE_CLOSURE_2026-08-23.md`. |
| R-174 | **THE SIX-BAND MAGNON STIFFNESS SPECTRUM OF THE CANTED VACUUM.** At `Γ`: **2 gapless + 4 EXACTLY fourfold-degenerate gapped** on BOTH single-`q` branches — `[0, 0, g×4]` with `g = 0.412121` (body-diagonal) and `g = 0.405987` (axis) at `D/J = 0.787`. ★ The **2 + 4 split with fourfold degeneracy is BRANCH-ROBUST**; ★ the **value `g` is BRANCH-SPECIFIC** (1.5 % apart) and branch selection is #1-gap OPEN. At `D = 0` the shared band is an **EXACT OPERATOR IDENTITY** `H(k) = 12·J·k̃²(k)·𝟙₆` (`1.4e-14`), where `induced_G_from_linear_face_band` STEP 1 previously only *licensed* it from WP-LV1 | **DERIVED-A** (the `D = 0` operator identity) + **DERIVED-numeric** (the `Γ` spectrum and `g`, **branch- and `D/J`-labelled**) + **DERIVED-structural** (branch-robustness of the split). CANDIDATE-half by consumption (D4 siting + `D/J` + branch pick); **no `CORE_PROVENANCE` row** | `magnon_stiffness_bands_canted_vacuum` — banked 2026-08-23, 3 suite checks in `check_twt_matter` with **two shipped failure modes**: the `6·J·k̃²` label form SEEN TO FAIL by `O(30)`, and the EVEN DM convention SEEN TO DESTROY the 2+4 structure (all six modes gapless) | D.4.3, B.6.2 | `canting_vacuum_branch_structure`, `n_goldstone_canted_FM`, `pi3_orientation_class_two_windings` | `induced_G_from_linear_face_band` (STEP 1 upgraded; the B1 annotation consumes `g`) | ★ **STIFFNESS, NOT BOGOLIUBOV (F2), and the name carries it.** Bosonic Bogoliubov problems are **paraunitary** against a `τ₃` metric (I-29; Shindou et al. 2013) and that operator is not this one — so this row **does NOT discharge** the two banked *"exact 6-band Bogoliubov structure UN-BANKED"* IOUs at `n_goldstone_canted_FM` and `induced_G_from_linear_face_band`. **They name a different object and are correctly left standing;** rewriting them to "now banked" would be exactly the F2 drift the caution exists to prevent. ★ **THE BRANCH LABEL IS MANDATORY:** the banked `N_G = 2` is scoped to the **AXIS** branch, while these numbers (and every number in the B1 annotation) are **body-diagonal**. The suite asserts `g_axis ≠ g_diag` precisely so a branch-blind quotation cannot silently return. **Basis limit:** the six `so(4)` generators are complete for the banked **rotor field** — not for the medium should the family ever add a grain-substance/amplitude DOF (a newly-opened node with no existing home). **Provenance:** axiom-arc `PROBE_SPECTRAL_NODE_2026-08-23.md` (B2), adjudicated HOLDS in the estate dispute as the batch's best result (needing a branch label and the naming fix), enacted per `ESTATE_BANKING_2026-08-23.md`. The probe script's `12·J·k̃²` print-label defect (a factor 2, sitting directly under the line this row banks on) was repaired in the same pass and is shipped as the primitive's own failure mode. |
| R-175 | **KC-1 — A ONE-WAY SYMMETRY-CLASS FILTER ON #1-GAP KERNEL CANDIDATES.** A kernel is spectral-branch-compatible **ONLY IF** its symplectic/kinetic structure `Ω` makes `Ω⁻¹H(k)` leave the real (orthogonal) class on the banked D4 Hessian. Measured (body-diagonal branch, `D/J = 0.787`): `H(k)* = H(−k)` and `spectrum(k) = spectrum(−k)`, both **exactly** ⇒ an antiunitary acts at fixed `k` ⇒ REAL class ⇒ degeneracies have **codimension 2** ⇒ **Jacobian rank 3 NEVER occurs**. ★ **And the fourth measurement is DEFINABILITY, not a value:** a small `S²` around a real-class crossing **cuts** the degeneracy locus (two-band gap on the sphere collapses to `~1e-7…1e-9` at radius `1e-3`), so **no ℤ-valued Chern number is definable there** — the same instrument returns `0` at some crossings and `−1` at others | **DERIVED-numeric** (the four measurements, branch- and `D/J`-labelled) + **CANDIDATE** (the filter as a kernel constraint); the real-class **ASSIGNMENT** explicitly **EVIDENCE-NOT-THEOREM**. CANDIDATE-half by consumption (D4 siting + `D/J` + branch vacuum — the case canon §6's consumption rule is aimed at, since the filter *feels* family-level); **no `CORE_PROVENANCE` row** | `spectral_branch_symmetry_class_filter` — banked 2026-08-23, 3 suite checks in `check_twt_matter`, with the **MANDATED FAILURE MODE** run in-process: the same instrument on a synthetic complex-class Weyl node returns Chern `±1` with the sphere gap bounded away at `2r`, and that node FAILS the real-class test the substrate passes | D.5 | `canting_vacuum_branch_structure`, R-174, R-112 (the hyperbolic linear face that fails the filter), I-29 (the named passing class) | — (a constraint on #1-gap kernel candidates; nothing banked rides it) | ★ **TWO CORRECTIONS TO GOVERNING RECORDS, both enacted.** (1) **"iff" → "ONLY IF":** failing is decisive, **passing is necessary-not-sufficient** — a complex-class kernel can still be nodeless, and the banked substrate fails the second test independently (gapless set exactly `{Γ, ±k₀}`, the helimagnet Goldstones). (2) **"escape (a) measured EMPTY" is a MIS-TRANSCRIPTION and is WITHDRAWN.** Only a *sub-class* was measured empty — four modifications of the time-derivative structure and of the hopping (dissipative real `Γ`, gyroscopic `Γ`, uniform Peierls phase, real antisymmetric hopping), each exactly zero, with only a genuinely **complex** hopping firing. The **`Ω`/paraunitary escape was never touched** (`Ω` is #1-gap content and unbanked). Correct status: **UNMEASURED / KERNEL-GATED** — writing "empty" converts a named gate into a closed measurement, the canon §4 / RUL-049 mirror-rule failure. `TONGUES_L2_2026-08-23.md` also *defines* escape (a) two incompatible ways (lines 32 and 400); both annotated there. ★ **A THIRD, found by this pass's own check design:** `PROBE_SPECTRAL_NODE` L1's **"Chern ≡ 0" is not robust** and is replaced by the codimension statement — quoting a tolerance on a quantity that is not defined is the tight-tolerance-on-a-vacuous-check tell in a new dress. **L1's verdict (no Weyl node on this substrate) is UNCHANGED and better evidenced.** ★ **SOFT SPOT that travels with the primitive:** the real-class **assignment** is strong computed evidence, not a theorem — the inversion operator `M` was never built and `M H(−k) M⁻¹ = H(k)` never verified matrix-wise. `inversion_operator_exhibited` is returned `False` so no consumer can forget; exhibiting `M` is the cheapest closing computation and is **OWED**. **Frame jurisdiction (N49): CLEAN** — substrate-internal end to end; no inside-frame rate or bound is routed into an outside-frame kernel property, so no N33-1-class hedge is warranted and none was manufactured. **Import:** I-29 (paraunitary bosonic-BdG), the one named PASSING class. |
| R-176 | **THE BOND-INVARIANT MENU IS COMPUTED EXHAUSTIVE AT TEN UNDER THE DRIVEN GROUP — IN THE FRAME-BILINEAR (RELATIVE-FRAME) REALIZATION.** Ladder 2 / 8 / 10 / 12 across `Aut(D4)`[1152] / `Stab(e₄-axis)`[96] / **`Stab(+e₄)`[48], the driven group** / `Stab⁺(+e₄)`[24], with the split `J:2 ⊕ D:2 ⊕ Γ:6` at [48] and the measured tensor characters (`J` internal scalar, `D` bond-reversal odd, `Γ` symmetric-traceless, per-bond trace `3e-16`). ★ **C-33:** the ROTOR-LINEAR realization gives a DIFFERENT ladder 1 / 2 / 4 / 8 — `Γ` does not exist at that order and the grade-4 pseudoscalar `χ` sits in its place (dim **0** at [48], **2** at [24]) — and WHICH realization is *the* menu is the **V3-2-class PICK**, family tree `LS-ℤ₂`, where the 4-vs-10 fork was **ALREADY RECORDED** (this result is CONFIRMED-ALREADY-RECORDED, not originating). ★★ **THE EXHAUSTIVENESS IS ANALYTIC, NOT A RESIDUE MEASUREMENT** — `V⊗V = 1⊕6⊕9` is a complete orthogonal split and both constraints preserve it (`[P,R] = [P,H] = 0`, computed exact) | **DERIVED-A on the COUNTS** (four independent pipelines: this Reynolds+SVD, the 2026-08-21 arbiter's constraint null-space, the reviewer's null-space, the reviewer's character/trace recount with no SVD) · **DERIVED-A but ANALYTIC on the EXHAUSTIVENESS** · the realization is a **PICK, not a measurement**. CANDIDATE-half by consumption (D4 siting); **no `CORE_PROVENANCE` row** | `bond_invariant_menu_frame_bilinear` — banked 2026-08-23, 2 suite checks in `check_twt_matter`, with the **DEMONSTRATED FAILURE MODE** run in-process: a planted rank-1 projector that does NOT commute with the constraints makes the SVD ranks *fail to add* (16 + 18 = 34 vs 10), which is the check that the residue tests COMMUTATION and not the lattice | C.3, D.3, D.4 | `canting_vacuum_branch_structure`, `D4_spatial_bond_isotropy`, `D4_DM_bond_bivectors_non_commuting`, family tree V3-1/V3-2 | R-177, R-178, R-179, R-180, R-181 | ★ **TWO CORRECTIONS CARRIED IN THE ROW ITSELF.** (1) *"residue = 0"* was submitted as **the exhaustiveness measurement** with a pre-registered failure criterion; that criterion is **UNFALSIFIABLE inside the parametrisation** and is relabelled — canon §8a's *a tight tolerance on a vacuous check is not rigour, it is a tell*. (2) **WORDING FENCE:** *computed EXHAUSTIVE at ten*, **never** C-32's *computed closed* — in C-32 the menu is exhausted AND every alternative refuted, whereas here the pick (keep `{J,D}`, zero the rest) is LIVE and counted (V3-2). ★ **THE OPEN PREMISE, NAMED:** `E_b = Tr(K_b W_b)` restricts the general bond-bilinear form (256 dims/bond) to the right-invariant subspace (16 dims/bond) — it **assumes** the bond energy depends only on the RELATIVE frame, and NOTHING in this round measures that. Licensed sentence: *no unnamed channel exists **within the relative-frame bilinear ansatz***, never *at bilinear order*. Record `knowledge/audit/gamma_referent_2026-08-23/` |
| R-177 | **THE CHANNEL→PARITY EXCLUSIVITY THEOREM, AT TRACE-PAIRING STRENGTH — the Γ round's most durable result, and it was submitted at a fraction of its scope.** `Tr(K Wᵀ) = Tr(Kᵀ W)` for **ARBITRARY real `W`**, so symmetric couplings (`J`, `Γ`) are reversal-EVEN and antisymmetric ones (`D`) reversal-ODD — **no helix, no simple bivector, not even a rotor** is required (verified on independent random `SO(4)` rotors per bond AND on random non-orthogonal real `W`, relative deviations at the `1e-13` floor). ⇒ **`Γ` can only renormalise the parity-EVEN denominator; `D_spatial` is the ONLY channel in the exhaustive menu that can reach the parity-ODD numerator — a SELECTION RULE inheriting NO branch risk and no configuration-class risk.** ★ ALL the physics sits in ONE NAMED PREMISE: *chirality reversal acts as `W_b → W_bᵀ`*, which on a helix is the identity `q → −q`; the algebra is free | **DERIVED-A, CONFIGURATION-INDEPENDENT** — recorded as an **UNDER-CLAIM correction** (RUL-076) against the submitting round, then strengthened past the reviewer's own form (arbitrary real `W`, not merely arbitrary rotors). CANDIDATE-half by consumption | `bond_channel_parity_exclusivity` — banked 2026-08-23, 2 suite checks in `check_twt_matter`, with the **DEMONSTRATED FAILURE MODE** run in-process: a deliberately MIXED-symmetry coupling (`J#1 + D#1`) returns **MIXED**, not EVEN and not ODD, both residuals `O(1)` relative | C.3, D.4 | R-176 (exhaustiveness is what makes this a selection rule rather than a statement about three named channels) | R-179, R-180, R-181; family tree V3-2 (the `D_spatial` half of the risk ordering) | ★ **TWO SCOPE FENCES RIDE IN THE ROW.** (a) *"EXACTLY TWO amplitudes"* is **CLASS-CONDITIONED** (RUL-049): true only within single-`q` families generated by a unit **SIMPLE** bivector — see R-178's `(1,3)` counterexample. The parity half above is unaffected and stays general. (b) **"JD-5 HALF-DISCHARGED" IS WITHDRAWN AS A LABEL.** JD-5's RECORDED scope is *the cos/sin parity assignment **of the ℤ₃ amplitudes***; the pitch statement is a fact about a DIFFERENT functional, on which the question was never the open one. **Nothing of JD-5 as recorded is discharged, and RUL-071(vi)'s conditioning of `0.79` on JD-5 is UNCHANGED.** At dressed level the assignment additionally needs the reversal to be a symmetry of the driven kernel — #1-gap-routed |
| R-178 | **THE BOND-BILINEAR HARMONIC CEILING IS A PROPERTY OF THE TWIST-GENERATOR CLASS, NOT OF BILINEAR ORDER.** For a generator with plane angles `(a,b)` the rep-level frequencies are `{a,b}` and the adjoint-level ones `{0, ±2a, ±2b, ±(a+b), ±(a−b)}`; so at bond-bilinear order the ceiling is `m ≤ 1` (rep) / `m ≤ 2` (adjoint) **GIVEN a SIMPLE or ISOCLINIC (SD/ASD) generator**, hence `< 3`, hence every ℤ₃ harmonic vanishes identically and the entry coefficients are `0/0`. The premise is verified and its source named: **every SD and every ASD bivector satisfies `B² = −λ²I`, i.e. is ISOCLINIC**, so canon §5's *GENERATIONS = the anti-self-dual triple* **SUPPLIES** the ceiling premise — as an **IDENTIFICATION, not a theorem** | **DERIVED-A-given-(a SIMPLE or ISOCLINIC (SD/ASD) one-parameter twist)** — and **REFUTED without that premise**, with the counterexample shipped. CANDIDATE-half by consumption | `bond_harmonic_ceiling_by_generator_class` — banked 2026-08-23, 2 suite checks in `check_twt_matter`. **THE COUNTEREXAMPLE *IS* THE FAILURE MODE and the primitive asserts it NONZERO:** a bond-**bilinear** energy on a helix generated by a NON-isoclinic `(1,3)` bivector carries `|c₃| = |c₁| = 6.00` on the **banked `J`** coupling, so the unconditioned ceiling can never be re-asserted from the engine | C.3, D.5.7 | R-176; canon §5 (the ASD identification the premise comes from) | JD-6 (worklist), N62 | ★ **THE OVER-CLAIM THIS ROW EXISTS TO PREVENT.** The submitting round asserted *"either way the ceiling is `m ≤ 2 < 3`"* and *"no bilinear-order computation, **however refined**, can compute `αᵢ` or `β`"* — bare necessity claims with no conditioning class (**RUL-049**) and **FALSE AS WRITTEN**. ⇒ **JD-6's upgrade is DERIVED-CONDITIONAL**, and conditioned on the **TWIST/CONFIGURATION class**, *not* on "the banked action class" (the submitted phrase mislocated it); it stays an ASSEMBLY RECORD at §D.5.7 (RUL-030 class 2), not a ruling. This is the **better** result: it locates the ceiling in the ASD identification, where it is contestable and re-attackable. ★ **AND THE VACUITY CENSUS IS REPAIRED IN THE PRIMITIVE:** the round's second construction `E = Tr(Rᵀ(Σ_b K_b)R Q)` is **VACUOUS for 8 of 12** couplings (four give `Σ_b K_b = 0` ⇒ `E ≡ 0`; four give `Σ_b K_b ∝ I` ⇒ `E` constant) — the identical defect was self-caught in one script of that round and NOT swept into the other, where it was load-bearing (canon §2, *sweep after a patch*) |
| R-179 | **GR-1 — THE LORENTZ-SAFE Γ SURVIVOR'S INERTNESS IS NON-GENERIC.** On the two banked high-symmetry branches the survivor is EXACTLY pitch-blind (`≤2e-16`), with pitch-visible `Γ` dimension **1** (axis) / **2** (body-diagonal); on generic single-`q` branches the visible dimension is **4** on essentially every branch and the survivor's own pitch entry is NONZERO. So *"the Γ survivor contributes exactly zero at all orders"* is SCOPED to the banked high-symmetry `k̂` — a property of the vacuum, **not a lattice identity** — and any protection argument resting on it is COUPLED TO THE BRANCH QUESTION, which is #1-gap open. Alongside: the pitch-visible `Γ` direction enters the pitch's even amplitude at `a_visible/a_J = 1/2` **exactly, q-independent** (an identity, not a coincidence at the calibrated pitch) | **DERIVED-A** on the banked branches; **DERIVED-numeric** off them (seed named, 200 random branches). CANDIDATE-half by consumption | `gamma_survivor_pitch_genericity` — banked 2026-08-23, 2 suite checks in `check_twt_matter`, with the **DEMONSTRATED FAILURE MODE (positive control)** run in-process: the pseudo-dipolar `W(F₄)`-invariant `Γ` direction **IS** visible on both banked branches at `O(1)`, so the measured blindness is not an artefact of a profile map that returns zero for everything | D.4, D.5 | R-176, R-177; `canting_vacuum_branch_structure` | keeper latent **L-2** (FED, not discharged); family tree **V3-2** (one annotation) and **V3-2a**(iii) (annotated, not discharged) | ★ **THE NUMBER IS CORRECTED AND THE OLD ONE WITHDRAWN.** The submitting round headlined *"worst pitch weight `7.134e-01` — i.e. `O(1)`"*; that was a **BARE NUMBER compared against nothing**, violating the same report's own normalisation discipline. At **EQUAL PER-BOND SCALE** the leak is **a few percent of `J`'s own even weight worst case (~3.4e-2), median ~0.1% (~9e-4)** — real, but markedly weaker than the pitch-visible directions' exact `1/2`, and **NOT a protection**. The worst case is a SAMPLE MAXIMUM; the median is stable. Normalisation-dependence is stated with the number (per-basis-member normalisation gives `1/3` for the same content ⇒ quote *a few percent, ~2-3%*, never one end). ★ **BLAST RADIUS OF THE UNSCOPED CLAIM: EMPTY** — every live corpus site already carries the scope, so GR-1 **confirms and quantifies the record and corrects nothing in it**; *"the finding with the widest reach"* is WITHDRAWN. **ONE** annotation was owed (family-tree V3-2's risk ordering) and it is repaired **ASYMMETRICALLY**: the `D_spatial` half is branch-INDEPENDENT by R-177's selection rule, the `Γ` half is branch-CONDITIONAL. `Q(k) ≡ 0` is **definitional** (the survivor is defined as that kernel) and is not reported as a confirming measurement |
| R-180 | **★ WHAT `D/J ≈ 0.79` MEASURES — THE REFERENT REVIEW, CLOSED NEGATIVELY.** `0.79 = tan(3δ_L)` is an invariant of the three charged-lepton masses computed with **no bond datum**; its substrate referent, given §C.3.7's form and the parity assignment, is **`D_total / J_effective`, a RATIO OF TOTALS**, with an exact channel exclusivity — `B = D_{e₄} + β·D_spatial` is exactly `Γ`-clean, `A = J + Σᵢ αᵢΓᵢ` is exactly `D`-clean, and by R-176 nothing else can enter either; the admixture SIZES are #1-gap-routed. **THE REVIEW STANDING SINCE 2026-08-17 CLOSES NEGATIVELY: `D/J ≈ 0.79` is NOT re-pinnable as a single-parameter measurement of `J` and `D`**, on three independent computed refusals (the calibration's functional sits OUTSIDE the scalar sector so tracelessness gives zero protection; `Γ` enters at the SAME order as `J`; the one blind direction loses blindness off the banked branches). ★ **THE ARC-RATIO RIDER [CANDIDATE]:** under the endorsed arc-ratio reading `δ_L = 2/9` rad exactly (`= 6/27`, the `n = 3` rung of the 2:4:6 ladder) ⇒ `D/J = tan(2/3) = 0.7868428894729773`, `1.57e-5` from the fit on the engine's own constants — **tighter than the banked rounded quote `0.787`'s own `2.0e-4`** | **PART 1 DERIVED-conditional** (frame-bilinear class pick; bilinear order; **JD-5 open on the ℤ₃ leg**) · **PART 2 CANDIDATE**. CANDIDATE-half by consumption | `DoverJ_calibration_referent` — banked 2026-08-23, **7 suite checks** in `check_twt_spectra`, with **THREE shipped failure modes** run in-process: the **PLANTED-VIOLATION DEMO** (relabelling the tautology as *agreement / confirmation* is REJECTED by the fence predicate), the **MASS-DEFINITION CONTROL** (a 0.1% coherent `m_τ` shift moves the result to ~20 PDG-σ), and the **WIRING FENCE verified against the live engine** (no consumer re-wired; `DoverJ_from_lepton_masses` still returns the fitted value) | C.3.5, C.3.7, C.3.11, D.3.3 | R-068, R-070, R-176, R-177 | R-074, R-103, R-107, R-108, R-181; canon §2's INPUT bullet (diff PROPOSED, unapplied) | ★★ **THE TAUTOLOGY FENCE IS THE PRIMITIVE'S CORE DESIGN, not a caveat.** The chain's **single empirical fact** is `δ_L ≈ 2/9` rad — **Brannen's observation**, at `0.41σ` from the fitted value. The `D/J`-level *"0.00157% agreement"* is a **TAUTOLOGICAL RESTATEMENT**: `D/J := tan(3δ_L)` **by definition**, so it is `tan(3·)` applied to **both sides of one fact** — not an agreement, not a confirmation, not corroboration. Precedent cited **by name** in the returned label: `brannen_comb_commitment_dominance_and_dof_vacuity`'s `min_over_mean_is_NOT_corroboration`. **The σ is NEVER a confidence level** (it propagates only PDG mass uncertainties; the mass-MEASURE conditional dwarfs it by orders — the control is IN the return dict). **The ladder is POSTDICTIVE** (formed on the already-known δ values, entered as *noted non-coincidences ONLY*, governing record `TWT_worklist.md` THE 1/27 PHASE LADDER, coordinator input 2026-08-03): it buys **COMPRESSION — one integer for one real — at ZERO predictive weight**. **THE NON-TAUTOLOGICAL TESTS ARE THE RIDER'S ONLY EVIDENTIAL FUTURE, and the first is NOT YET DISCRIMINATING (RUL-100(2), 2026-08-24 sweep — the earlier *"CURRENTLY FAILING"* characterization is RETIRED):** the exact reading demands `e = √18/tan(2/3) = 5.391979` against the historical `e_ANW = 5.45` — **1.06% low**, stated as plainly as a success would be, and as a *test* it fails nothing, because the historical Skyrme `e` is itself a fit whose spread across determinations exceeds the deviation; the test bites only against a determination at or below the ~1% level, read from primaries before any promotion. Then the GR-2 read-out at 0.1%; then a second sector on the 1/27 ladder with no new freedom. **The value banks as a REPORTED COMPARISON, WIRED TO NOTHING** — `does_not_license` forbids feeding `tan(2/3)` into any consumer. **`0.787` stops being the quoted figure**; the honest quotable is the fitted `0.78686` with its band, or conditionally `tan(2/3)`. **Still NOT licensed:** the flat assertion *"0.79 is a combination measurement"*. **CREDIT:** `2/9` is Brannen's; `2/27`, `4/27` are Żenczykowski's — **F3 bibliography duty OPEN** |
| R-181 | **JD-6(b) (= GR-2) — THE THREE `J_eff` FACES, AND THE FIRST NUMBER FOR A `Γ` ADMIXTURE.** `J` is not one constant: `f_π² = 8J/a` (R-106) is a quadratic-fluctuation object, the pitch is a branch-dependent `(1−cos)`-weighted object, and the ℤ₃ amplitude is a dressed harmonic — `Γ` renormalises each through a **different** functional, and the three coincide **only if the `Γ` admixture vanishes**. ★ **THE FENCE:** *NEVER CARRY A RATIO CALIBRATED ON ONE FUNCTIONAL INTO ANOTHER.* ★ **THE DISCRIMINATOR:** since R-177 puts `Γ` in the denominator ONLY, any difference between two legs' measured ratios is entirely a difference of denominators — `J_eff(pitch)/J_eff(ℤ₃) ≈ 1.0108`, and through R-179's exact entry ratio `1/2`, **`Δ(Γ/J) ≈ +2.15% of J` between the two functionals** | **CANDIDATE — a ROUTE, not a measurement.** Filed as a named **COROLLARY of JD-6**, deliberately NOT an independent fourth gap (it is empty if JD-6's coefficients vanish; gap-inventory inflation is a real cost). CANDIDATE-half by consumption | `gamma_admixture_cross_functional_route` — banked 2026-08-23, 2 suite checks in `check_twt_matter`, with the **DEMONSTRATED FAILURE MODE** run in-process: the same route on the `√12` bridge instead of the disclaimed `√18` one returns a number whose relative spread from the `√18` answer is **larger than the answer itself**, so `2.15%` can never be quoted as a measurement | D.5.7 (bidirectional pointers to JD-6), C.3.11 | R-177, R-179, R-180, R-106 | the cross-leg consumers; `over_determination_scan`'s band rationale; R-074, R-103, R-107, R-108 | ★ **THE FENCE WAS WIDENED at consensus.** The submitted form said *"never combine `D/J` with an independently-fixed `J` such as `f_π² = 8J/a`"* and then placed every cross-leg consumer in NOT-EXPOSED on the ground that *"the ratio is self-consistent"* — a ground valid **within one functional** and **exactly what GR-2 denies across functionals**. The exposure is not a junction; **it is the default-argument wiring itself**, reaching `spiral_angle_deg`, `dressed_coupling`, `eta_DM`, `canting_pitch_q_rad`/`canting_cos_q` at the calibrated value, `electron_f_L_MeV`, the hard-wired `D/J` defaults, `over_determination_scan`'s band rationale and the shipped lepton↔baryon over-determination headline. **VALUES DO NOT MOVE**; what moves is the claim that the formula is being fed the right substrate quantity (the unnamed premise `α = a`). ★ **CONDITIONING CLASS, RUL-049, complete:** (i) the arc-ratio reading (CANDIDATE); (ii) the `√18` bridge, whose `√12` alternative sits ~20% away and whose referent *the framework itself disclaims*; (iii) `e_ANW`'s own fit systematics; (iv) that the `Γ` admixture is the ONLY difference between the two faces. **Any one failing voids the number.** ★ **RESOLUTION ROUTE:** an independent `e` — or the `J` that `f_π² = 8J/a` fixes — **at the 0.1% level** would READ OUT the admixture instead of absorbing it into a *"1.1% agreement"*: a measurement programme with a stated target precision |
| R-182 | **THE Φ BRIDGE — the graded-left-module isomorphism `Cl⁺(4,0) ≅ S`.** `Φ : Cl⁺(4,0) → S = Cl(4,0)·s₀`, `x ↦ x·s₀`, is a **left-`Cl(4,0)`-linear bijection** carrying the `I₄` grading to the `I₄` grading: **`Φ(W±) = S±` exactly**. The evidence is the IDENTITY, not the residuals — `e₄s₀ = s₀ ⇒ Cl·s₀ = Cl⁺·s₀`; `x·s₀ = 0` with `x` even forces `x ∈ Cl⁺ ∩ Cl⁻ = 0`; left-linearity **is** associativity; `P± = (1±I₄)/2` is **central in `Cl⁺`** so `Φ(W±) = P±·S = S±`. ★ **IT CLOSES THE GRADED-LEFT-MODULE HALF OF THE TWO-MODULE ORPHAN** (the corpus named `Cl⁺` and `S` for the same one-sided internal action with **no passage relating them**) and thereby **licenses the previously silent `W₊/S₊` identification** | **DERIVED-A by IDENTITY** for the bridge; **DERIVED-A + REALIZATION-CONDITIONED** for the two mandatory checks. **CORE-half** — it consumes `s0` and Clifford multiplication and NO V3 pick; it rides no entered datum and no posited premise, so **no `CORE_PROVENANCE` row is owed** | `spinor_module_graded_iso` — banked 2026-08-23, **5 suite checks** in `check_twt_weak`, with **BOTH MANDATORY FAILURE-MODE CHECKS** run in-process and seen to fire | A.5, B.3, C.3.12, D.2 | `s0` (§6.1), R-012, R-102, R-076, R-172 | the V4-ASD node; R-076's carrier statement; R-172(viii) | ★ **MANDATORY CHECK #1 — THE BODY SIDE GENUINELY DIFFERS.** `S` is **not** a right `Cl⁺`-module (`leak(R_ASD, S) = 2.0` vs `leak(R_ASD, Cl⁺) = 0`); the body action reaches `S` only through the `s₀`-dependent transport `ρ(h): x·s₀ ↦ x·h·s₀`. **BUT a genuine intrinsic Lorentz-scalar body action on `S` DOES exist** — `End_Cl(S)`, the 8-dim right-stabiliser `{1,e₄,e₁₂,e₁₃,e₂₃,e₁₂₄,e₁₃₄,e₂₃₄}` whose even part is the single `ℍ` = exactly R-172(6)C2's diagonal-class algebra — **and `ρ` is NOT in it** (`max‖[L_odd, ρ(ASD)]‖ = 4.0`). Without this check the *"only through Φ"* over-claim re-enters, and that omission **hides the very fact that makes V4-0 a branch point**. ★ **MANDATORY CHECK #2 — THE C-33 REALIZATION SPLIT, both realizations under their own keys.** Under the **BANKED grade-one lock** `leak(L_K¹, S₊) = 1.0` exactly (vs `0` under grade-two) and `[L_K¹, ρ(ASD)]` on `S` is nonzero for **all 9** pairs (vs 0 of 9 under grade-two, and 0 of 9 against lab rotations in both): **on `S` the transported body label FAILS the canon §5 / RUL-099 invariance test against the banked lock.** The identity `[L_g, R_h] = 0` is about `Cl(4,0)` acting on **itself** and does not transfer to (observer on `S`, label on `S`). ★ **TWO EXPOSURES, both PRE-EXISTING and neither previously carried: E-1** — R-076's `I₄`-graded occupancy is **not boost-invariant** in the banked realization (`e₁P₊ − P₋e₁ = 0` exactly, `L_{e₁}(S₊) ⊆ S₋`), so *"occupies one ideal / occupies both"* is not a Lorentz-stable species property there; **E-2** — RUL-099 on the V4-0-signed carrier `Cl⁺` against the banked lock is **VACUOUS** (`leak(L_K¹, Cl⁺) = √2`: the banked boost is a vector and is not an operator on `Cl⁺` at all), recorded as **RUL-099's first refinement** at its register row. ★★ **WHAT THIS ROW DELIBERATELY DOES NOT CARRY:** the Layer-A round's menu-DISCRIMINATING verdict, **WITHDRAWN IN FULL** at consensus — *"no `j=1` anywhere in the local field module"* (one DOES occur: the ASD triple itself under the **adjoint** action at exactly the `j=1` Casimir, ratio 8/3 — the C-33 **action** axis was named in the setup and dropped at the headline), the strike of any seat reading, the *"only door"* dichotomy, the FCNC re-basing (a non-sequitur; **the debt is UNTOUCHED**), and the claimed asymmetry (`⟨(L_J, ρ(ASD))⟩ = End(S₋) = 16`, but the weak-side mirror `⟨(L_J, R_SD)⟩ = End(W₊) = 16` too, so that argument form would refute banked **R-079** when mirrored). **LAYER A DID NOT DISCRIMINATE**: the V4-ASD node stays OPEN, its menu reverts three-way, and Layer B is the sole decider |
| R-166 | Self-adjointness forced by the `{1, B}` projection: `⟨ψ̃ M̂ ψ⟩_B = 0` for all `ψ` has solution space EXACTLY the reversion-fixed subspace — dimension 2, basis `{1, I₄}`, on `Cl⁺(4,0)`; dimension 6, basis `{1, e₁, e₂, e₃, e₄, I₄}`, on `Cl(4,0)`, for all three L-orbit winding choices `B_a` | DERIVED-A (exact rational kernel computation) + NAMED PREMISES (expectation values are real — the QM postulate being expressed, not derived; and observables act ℂ-linearly: 28 real dimensions survive without that, 16 with it) | self_adjointness_from_one_B_projection | B.3.2 | R-021 | R-022 | Replaces the vacuous "requiring reality" derivation of R-022; R-022's conclusion is unchanged. The `{1, B}` subalgebra itself is R-020. The pairing splits into a symmetric unimodular `⟨φ̃ ψ⟩_0` and an antisymmetric nondegenerate (symplectic) `⟨φ̃ ψ⟩_B`, with right-multiplication by `B` a compatible complex structure — the Hermitian form of `ℂ⁴`. Scope limit recorded: the phase sector `span{1, B}` ALONE under-determines the condition (7 of 8 dimensions survive) — the full even subalgebra is needed as the state space. The same primitive withdraws the §B.3.2 grade-3 "eigenvector of the corresponding observable" gloss: the `T_a` are orthonormal but reversion-ODD (anti-self-adjoint), square to −1, and do not commute pairwise. |

---

## Part C — Matter, charges, generations, gauge group

| ID | Statement | Tier | Engine | § | Deps | Used by | Notes |
|---|---|---|---|---|---|---|---|
| R-051 | Skyrme mass formula `M_0 = 36.47 f_π/e` at dressed-coupling level | DERIVED at dressed-coupling | skyrme_BVP_audit + skyrmion_mass_MeV + skyrme_length_fm | C.1 | R-007, A-1c | R-053 | Conditional on dressed-sector closure. ~1% favourable scheme, ~10% cross-scheme spread. Consumes the §A.4 `m = E₀` premise (counted 2026-08-12) wherever its elastic value meets a measured mass. |
| R-052 | Exactly two conserved topological windings `(B, L)` — chiral counting from `Spin(4) = SU(2)_+ × SU(2)_−` relabeled to the orbit basis `(n_𝓛, n_𝓠)` via the §A.5.2 symmetric-pair / fibration bridge | DERIVED-A | pi3_orientation_class_two_windings (the `ℤ × ℤ` itself — chiral factorization, cover-blind) + pi3_S3_integer_completion (the per-sector degree facts: lepton-sector π_3(S³)=ℤ + baryon integer completion) | C.1 | R-002, R-009 | R-053, R-054, R-087 | Structural skeleton of all matter. The chiral basis gives the `ℤ × ℤ` directly; the orbit basis is the framework's working basis. Lepton hedgehog is subgroup-valued (into `Spin(3) = exp(𝓛)`); baryon hedgehog is coset-valued (into `Spin(4) / Spin(3) ≅ S³_𝓠`). Both yield `ℤ` degree; the targets are topologically distinct map types. Open residue: the `(n_𝓛, n_𝓠)` basis needs a splitting of `0 → ℤ → ℤ×ℤ → ℤ → 0` — always exists (free quotient), never canonical, nowhere named. The per-sector-degree handle (`L = deg(S³→S³_𝓛)`, `B = deg(S³→S³_𝓠)`) avoids the splitting but PRESUPPOSES the sector assignment — a handle, not an answer. |
| R-053 | Baryon as one Q-orbit defect with three orthogonal facets (V2 §3.2 / §16.5.1.1) | DERIVED-STRUCTURAL | nonuniform_orbit_baryon_model + cogear_linkage_kinematic + baryon_mass_shared_rotor_nonadditive + e4_content_confines_quarks_not_leptons | C.1 | R-005, R-052, R-051 | R-084, R-085 | Three "quarks" are three facets of one circular winding. |
| R-054 | Proton stability from `B ∈ π_3(SU(2)) = ℤ` integer winding | DERIVED-A | pi3_S3_integer_completion + lepton_number_topological_conservation | C.1 | R-006, R-052 | R-089 | Canonical falsifier §E.3 row 2. |
| R-055 | Electron as Hopf defect on L-orbit; QCP scaling `f_L = f_π · (1 − D/J)^{9/2}` at L1 — a STIFFNESS, not a mass | DERIVED-CONDITIONAL (the `f_L` scaling). The `f_L → m_e` conversion is **EXCISED**, not open: it is no longer part of this result | electron_two_windings + electron_QCP_nu + electron_f_L_MeV | C.1 | A-1c, R-007 | — | **SCOPE (2026-08-20, Gate C branch (b)):** the result is the `f_L` scaling law and the structural Hopf identification. It delivers NO electron mass, and no accuracy figure. **EXCISED:** the `m_e = f_L · e_L` conversion with `e_L = √36.47 ≈ 6.04`, together with all three numbers it produced — the ~36% `f_L` residual, the 4.4% exponent match against `ν_emp ≈ 4.696`, and the 0.34% `ν = 3π/2` match (that third figure is the same artifact: `ν_emp` is only definable through the conversion, and moves to 5.123 — an 8.0% mismatch to `3π/2` — on the Faddeev branch). Grounds for excision rather than counting: `e_L` was an undeclared, uncounted coupling, not an eigenvalue — `36.47` is the ANW hedgehog BVP energy evaluated at the solution (the BVP's SELECTED parameter is `F'(0) = −1.0038`), entering the baryon formula as `M_0 = 36.47 f_π/e`, so `m_e = f_L · e_L` silently placed the L-sector Skyrme coupling at the self-consistent fixed point `coeff/e = e`, 11% off the baryon sector's `e = 5.45` for no stated reason, with no engine primitive and no derivation anywhere in the corpus — and nothing banked consumed it. **The counted-input headline is UNMOVED (four counted substrate inputs plus measured `G_N`): `e_L` was never counted, so excising it changes no count.** **THE DECISIVE GROUND, found on the post-cut keeper round and stronger than the one the ruling recorded: NO CONSTANT COULD HAVE BRIDGED `f_L` TO `m_e` AT ALL.** R-068/R-069's banked Brannen parametrization (`delta_L_from_DoverJ`) makes `√m_e` vanish LINEARLY at `δ_L = π/12`, so `m_e ∝ (1 − D/J)²` near the balance — engine-measured `d ln m_e / d ln(1 − D/J)` = 2.2555 at the calibrated `D/J = 0.79`, → 2.0000 as `D/J → 1` — against `f_L`'s `9/2`. A constant `e_L` cannot relate two different exponents, so `m_e = f_L · e_L` was incompatible with two OTHER banked results, independently of `e_L`'s value. **This also means branch (a) was never actually available:** counting `e_L` would not have repaired an exponent mismatch. **THE OBSTRUCTION IS UPSTREAM OF THE COUPLING, and it is why the mass step cannot be repaired by substituting a different number:** which functional stabilises the L-orbit defect is OPEN, so no dimensionless coefficient exists for the L-sector at all — and even a coefficient would not suffice, per the exponent above. `ring_core.py` states the L-orbit profile is genuinely open, and GF-5 proposes a fixed-charge stabiliser that is not a quartic at all. In the matched normalisation (`c₂ = f_π²/8`, `c₄ = 1/(2e²)`, `√(c₂c₄) = f_π/(4e)`) the Skyrme hedgehog `B = 1` minimum is `145.85 = 4 × 36.46`, confirming 36.47 for the BARYON functional and for no other; on the S²-director Faddeev–Skyrme branch the rigorous Vakulenko–Kapitanski floor is `32π²√2 (3/16)^{3/8} = 238.4` (coefficient floor 59.6), EXCLUDING 36.47, with the literature `H = 1` value `552.1` giving coefficient `138.0`; and GF-5's fixed-charge balance admits neither. NOT engine-banked: no primitive computes any of these coefficients. L2 mechanism unidentified; `ν = 3π/2 = 4.712` survives as a CANDIDATE VALUE with no mechanism and no live empirical target. **R-069 restatement does NOT reopen Gate C (J,D/Γ rework, keeper item 4):** the decisive exponent comparison (`m_e ∝ (1 − D/J)²` against `f_L`'s `9/2`) is made at the **parametrization level**, with the same banked `A = J, B = D` ansatz in force on both legs, so re-basing R-069 on the amplitude form `B = A` leaves the incompatibility argument untouched. Additional conditional inherited from the branch structure: `f_L`'s stiffness is computed on the AXIS branch of §D.4.3 and acquires that branch label (it delivers no mass either way). |
| R-056 | Per-blade hypercharge from `e_4`-bilinear `B̃ e_4 B` (±1 eigenvalues, engine-verified) | DERIVED-A | hypercharge + doublet_hypercharge + winding_charge | C.2 | R-010 | R-057, R-062, R-080 | — |
| R-057 | Fractional quark charges `±2/3, ±1/3` from algebraic three-quark blade structure | DERIVED-A | gmn_coefficient + triple_product_Q + triple_product_color | C.2 | R-056, R-053 | R-062, R-063, R-073 | Algebraic identity. |
| R-058 | Weak isospin from the meta-time rotor pair `(sin(ωτ/2), cos(ωτ/2))` | FRAMING/INPUT-given-{weak=SD, i.e. A-P2′-RIGHT + the RH-singlet datum} [side ruled RUL-091: body-frame/right action on the even-module ideals; left reading retired; chirality structure carried by the `H±` ideal split — ADJUDICATION_R3 §4-bis] (re-tiered 2026-07-31, C-6: under rotations of the rotor axis the pair transforms `1 ⊕ 3`, NOT as a doublet — the doublet reading needs LEFT multiplication on `ℍ ≅ ℂ²`, which is not "rotation of the axis" and is not derived; the `T₃` slot assignment is posited in-engine, cf. P7). **Dated correction 2026-08-23 (RUL-091):** the LEFT-multiplication sentence just above described the reading that is now RETIRED as internal host (left-centralizer theorem; Lorentz-scalar character of the datum) — it is kept as the record of what was tiered, not deleted. The banked structure TRANSFERS to the right (body-frame) action: `[L_A, R_X] = 0` exactly, and the chirality selection is an ideal fact (SD ⊂ `H₊` annihilates `W⁻`, acts full-rank on `W⁺`), so the doublet reading is to be re-carried on the even-subalgebra module per §4-bis. The re-carrying primitive is owed and enters as CANDIDATE; the row's FRAMING/INPUT tier is unchanged by the side ruling | doublet_hypercharge (Y-side only; the T₃ doublet content is posited in-engine) | C.2 | R-007 | R-060, R-061 | The minimal-SD-rep reading is the honest form; §C.4.5(i)'s `ΣT₃² = 2` consumes the posited table. |
| R-059 | Lepton-quark weak universality — the blade identity `e_{ij4}·s₀ = e_{ij}·s₀` | DERIVED-A (the identity — one line of projector algebra, immediate from `e₄s₀ = s₀`) + FRAMING (its reading as WEAK-coupling universality: the compared objects are L-orbit/spin blades, and the SD-generator action is NOT computed; re-tiered 2026-07-31, C-9) — the FRAMING half is conditioned on **A-P2′-RIGHT + the RH-singlet datum** [side ruled RUL-091: body-frame/right action on the even-module ideals; left reading retired; chirality structure carried by the `H±` ideal split — ADJUDICATION_R3 §4-bis]; the owed SD-action computation is now owed on the **body-frame** action | universality_theorem | C.2 | R-058, R-079 | — | Universality-as-physics awaits the SD action computation. |
| R-060 | V−A structure from SD's half-module kernel (couples one Weyl chirality only) | DERIVED-given-R-079, i.e. DERIVED-given-{A-P2′-RIGHT + the RH-singlet datum} (R-079 is itself no longer an INPUT — see that row) [side ruled RUL-091: body-frame/right action on the even-module ideals; left reading retired; chirality structure carried by the `H±` ideal split — ADJUDICATION_R3 §4-bis. **V−A is NOT forfeited on the right branch**: SD ⊂ `H₊` and ASD ⊂ `H₋` are the even algebra's two CENTRAL ideals, so annihilation of a chirality half is an **ideal fact, side-independent** — body-SD annihilates `W⁻` and acts full-rank on `W⁺`, coordinator-verified same-day. The earlier "right action is chirality-blind ⇒ V−A forfeited" cost line was a module conflation (the 16-dim `P₊Cl` regular module vs the even-subalgebra ideals) and is withdrawn, owned] | weak_isospin_SD_parity_exclusion + vminusa_is_spin4_factor_chirality | C.2 | R-058, R-079 | — | DERIVED-given the weak = SD assignment (R-079), which is itself DERIVED-given-{A-P2 + the right-handed-singlet datum} — **not an input bit**. |
| R-061 | Generation-blindness / no tree FCNC from SD centralizing ASD generation triple | DERIVED-given-R-079, i.e. DERIVED-given-{A-P2′-RIGHT + the RH-singlet datum} (R-079 is itself no longer an INPUT — see that row) [side ruled RUL-091: body-frame/right action on the even-module ideals; left reading retired; chirality structure carried by the `H±` ideal split — ADJUDICATION_R3 §4-bis. The centralizing structure is the `H₊`/`H₋` ideal separation and is side-independent; on the right branch it additionally coheres with the generation carrier, whose meta-time ℤ₃ phase is already a RIGHT phase] | weak_isospin_zero_on_generations + weak_isospin_centralizer_is_SD | C.2 | R-079, R-071 | — | Canonical falsifier §E.3 row 15. |
| R-062 | Gell-Mann–Nishijima `Q = T_3 + Y/2` as DERIVED algebraic identity (not imported) | DERIVED-A (the identity and the non-circularity) — **the exact `1/2` is DERIVED-GIVEN-THE-ASSIGNED-TABLE**, not extracted from the substrate independently of it; the `T₃` slot the table fills is conditioned on **A-P2′-RIGHT + the RH-singlet datum** [side ruled RUL-091: body-frame/right action on the even-module ideals; left reading retired; chirality structure carried by the `H±` ideal split — ADJUDICATION_R3 §4-bis. Only the REFERENT of the `T₃` slot is touched; the `c`-free arithmetic and the non-circularity are side-neutral and untouched] | gmn_coefficient + generation_spectrum | C.2 | R-056, R-058 | R-063 | The combination — including the exact 1/2 — is derived, and the non-circularity is genuine (`Y` never defined as `2(Q − T_3)`). **Note added (keeper R3): the tier cell read unconditional while the primitive's own SCOPE paragraph says `c = 1/2` is exact GIVEN the assigned table** — `Q` from `charge_assignment_from_anchor` (entered anchor + composition), `T_3` from the posited slot table (P7). What is non-trivial and does not ride the anchor: the quark row and the lepton row return the SAME `c`, and P4-universality forces `Q_p − Q_n = 1` identically (`charge_sector_provenance`). |
| R-063 | Charge discreteness/commensurability `{0, ±1/3, ±2/3, ±1}·\|Q_e\|` exactly; `\|Q_p\| = \|Q_e\|` protected (tested `< 10⁻²¹`) | DERIVED-A (discreteness + GMN non-circularity); the equality NORMALIZATION conditional on the neutrality-of-atoms anchor — an inside-frame empirical import (engine tier note 2026-06-30) | winding_charge + gmn_coefficient + generation_spectrum + pi3_S3_integer_completion | C.2 | R-062, R-054 | (paper headline) | Anti-circularly grounded via §C.5 topological winding (integer-valuedness); equality protected by commensurability. **The normalization anchor is CONDITIONALLY REPLACED by R-159** — `Q_p + Q_e = 0` holds identically in `c` given (P4, P5, P6, P7 — P7 the cross-sector weak-isospin alignment, added 2026-07-31, C-5), so the neutrality-of-atoms datum is no longer consumed at this site (it reverts to being the anchor if those premises fail). Cleanest spine result (ranking updated per the 2026-07-29 signature relabel — the §C.2 body said so; this row now agrees, C-2). **HEADLINE SCOPED (charge-sector repair):** what is carried end to end is the DISCRETENESS (π₃ integer-valuedness) and the c-free NEUTRALITY IDENTITY (R-159); the per-state VALUE assignment is not — it rides P4–P7 and the entered anchor. The abstract, §C.2's opening and §C.2.8 previously read as if the whole spectrum were derived; they now state the two halves separately, and the engine draws the same line at `charge_sector_provenance` with `charge_assignment_from_anchor` renamed off the computational name. |
| R-064 | Brannen amplitude form `A_k = 1 + c cos(...)` from V_4⊥ projection geometry | DERIVED | brannen_amplitude + koide_K + koide_from_c | C.3 | R-009 | R-065, R-066, R-068 | Projection of meta-time circle on V_4⊥. |
| R-065 | `√2` projection coefficient — the equivalence content: `K = (1+2r²)/3` gives `K = 2/3 ⇔ c = √2` (the same INPUT bit as `K = 2/3`, seen through the projection geometry) | INPUT-equivalent (the value); the equivalence itself DERIVED-A | dft_K_from_r | C.3 | R-064 | R-066 | NOT independently forced — six forcing routes NEGATIVE (see R-066); the primitive computes the equivalence, not a forcing. |
| R-066 | Koide `K = 2/3` ⇔ `c = √2` Brannen-Koide equivalence theorem | DERIVED-A | koide_K + koide_from_c + koide_charge_unification + dft_K_from_r | C.3 | R-064, R-065 | R-067, R-068 | Theorem; K=2/3 is INPUT (exact-but-unforced; six forcing routes NEGATIVE). |
| R-067 | Foot 45° signature-free characterization | DERIVED-A | foot_angle_deg | C.3 | R-066 | — | Independent of mass-measure convention. |
| R-068 | Three lepton mass ratios at `δ_L = 12.73°` to <0.01% | FIT (post WP-MASS-MEASURE) | brannen_amplitude + delta_L_from_DoverJ + DoverJ_from_lepton_masses + hierarchy_type | C.3 | R-064, R-066 | R-069, R-074 | Tier qualified: forward derivation `L-orbit τ=0 → lepton ε=0` REFUTED in V2 Phase F. Mass-measure `√m = r²` (mass_measure_from_omega) sits at CANDIDATE-strong. NAMED REVERT CLAUSE (2026-08-13, ψ-repair keeper L1): `δ_L`'s status as a mass-observable is CONDITIONAL on `ε_lepton = 0` being structural — at ε = 0 the N=3 aliasing degeneracy is absent and the resultant phase IS δ_L (R-170); if `ε_lepton` is ever re-tiered to FIT, or a two-harmonic lepton parametrization is banked, the collapse argument makes δ_L mass-gauge exactly as ψ_d. Blast radius on firing: FORMATION_CORE §1 δ-ontology (δ_L as measured arc ratio), §C.3.5/§C.3.11, the R-070/R-074 lepton calibration legs. |
| R-069 | `B = A ⇔ δ_L = π/12 ⇔ m_e = 0` structural identity at leading order — the two AMPLITUDES of the chiral ℤ₃ potential, equal | DERIVED-STRUCTURAL (in the amplitude form) | delta_L_from_DoverJ + D_crit_over_J | C.3 | R-068 | — | **Restated at the J,D/Γ rework — same theorem, honest referent** (`VERDICT_KEEPER_2026-08-21.md` item 4; report §6/§14(b5)). The derivation only ever established `tan 3δ_L = B/A`; the `D = J` form is its **corollary GIVEN R-070's asserted `A = J, B = D` ansatz**, and is kept as such (the instance-level face). The "chirality nearly balances / 79% of critical" narrative in §C.3.6 is conditional on that ansatz and now says so. Provenance rider (RUL-025) carried from `DoverJ_from_lepton_masses`: the 0.79 is conditional on (a) the `√m = r²` mass-measure choice AND (b) the ansatz. `D_crit_over_J`'s docstring carries the note that "D = J" is the ansatz-mapped face of `B = A`. Does NOT reopen Gate C — see R-055. |
| R-070 | δ_L from chiral-ℤ_3 potential FORM (coefficient identification A=J, B=D is ASSERTED ANSATZ) | DERIVED (form) + ASSERTED (coefficient identification) | delta_L_from_DoverJ | C.3 | A-1c, R-176, R-177 | R-180 | Honest scope. ★ **REFERENT SHARPENED 2026-08-23 (R-180):** the `A = J, B = D` ansatz's referent is now computed — the menu is **exhaustive at ten** in the frame-bilinear realization, and by an exact parity selection rule `B = D_{e₄} + β·D_spatial` (exactly `Γ`-clean) while `A = J + Σᵢ αᵢΓᵢ` (exactly `D`-clean), so what the ansatz identifies is **`D_total/J_effective`, a ratio of TOTALS**, with both admixture sizes #1-gap-routed. On THIS (ℤ₃) leg the parity assignment still rides **JD-5, UNDISCHARGED** — RUL-071(vi)'s conditioning is unchanged, and the earlier *"half-discharged"* label is WITHDRAWN. Record `knowledge/audit/gamma_referent_2026-08-23/` |
| R-071 | Three generations — the COUNT = dim Λ²₋(ℝ⁴) = 3, generic-given-4D and COMPUTED in-engine (trace of the `(1−I₄·)/2` projector; 2026-07-31, C-1 — replaces a `len()`-of-a-literal cert); Frobenius demoted to structural remark via the named ASSOCIATIVITY premise; + ASD-triple + ℍ-unit identification | DERIVED-generic-given-4D (the count) + LOCATED (the identification + associativity) | why_three_generation_triple + generations_dynamical_count_structural + phase_to_h_unit_map_located_residual | C.3 | R-009, A-1a | R-061 | LOCATED-conditional on the orbit-phase → ℍ-unit map AND the associativity premise (drop associativity → octonions offer seven units; cf. Furey, cited §C.3.8). |
| R-072 | `G` is the colour ℤ_3 (not the generation ℤ_3) per the §C.3.9 reidentification (V2 §17.4) | DERIVED | G_generator + G_cycles_generations + generation_z3_is_metatime_phase | C.3 | R-009 | — | Spatial generator G is colour cycle; generation ℤ_3 is meta-time phase. |
| R-073 | Cabibbo as frequency ratio `\|V_us\|² = m_d/m_s ≈ 0.05`, 0.6% match — **the relation is the Gatto–Sartori–Tonin relation (GST 1968), not original here**; only the frequency-ratio *reading* is claimed | CANDIDATE | quark_brannen_table + quark_mass_reconstruction + cabibbo_transition_probability | C.3 | R-057, R-068 | — | TWT-untestable on `m_t` ratio (no top hadrons). Engine numbers: `\|V_us\|² = 0.0503` vs `m_d/m_s = 0.0500` (PDG 4.67/93.4), 0.62% off (`cabibbo_transition_probability`, inline assert < 1%). Cite `cabibbo_angle_rad` removed 2026-07-02 — that primitive is formally DEPRECATED (returns the lepton phase δ_L, not a Cabibbo angle; V1 identification refuted 2026-06-29). Attribution corrected 2026-07-28: `sin θ_C ≃ √(m_d/m_s)` is Gatto, Sartori & Tonin, *Phys. Lett. B* **28**, 128 (1968), DOI 10.1016/0370-2693(68)90150-0 — see §C.3.10 and Section 10 Bibliography. The 0.6% agreement is GST's, not evidence for the substrate. ψ-repair 2026-08-13 (ADJUDICATION2 keeper C1; §8a round fixes + coordinator provenance correction same day — see R-170): the engine's old `ψ_d ≈ 12.76° ≈ δ_L` clause STRUCK — ψ is NOT FIXED BY THE MASS SPECTRUM (mass-gauge; harmonic collapse `cos(2φ_n−ψ) ≡ cos(φ_n+ψ)` at N=3; two distinct `(b,ε,ψ)` triples hit the same three masses, one with ε=0). The invariant down phase is `ψ_inv,d = 6.294°` computed MODEL-FREE from the three MS-bar indicator masses (3-point DFT ≡ Żenczykowski 2012 Eq. (12); ADJUDICATION2's 6.294° was CORRECT AS STATED — a first-round worker annotation calling it a `ψ_d→δ_L` insertion artifact was WRONG and is withdrawn; the fit route gives 6.305°, a fit-residual difference). Scheme + provenance: the MS-bar value is scheme-dependent (≈5.8–8.5° across quark-mass schemes) and indicator-level (canon §5); the corpus's CREDITED down phase is the probe-5 HADRON-route band |δ_d| ≈ 5.8–8.5° (physical channel, N57-free, brackets 4/27 rad = 8.488°); the strike is over-determined — both routes ≪ `δ_L = 12.73°`. ε-conventions SCOPED (not "unified"): FOUR epicycle variants coexist (ψ-form `+εb`; 2ψ-form `−√ε`; 2ψ-form `−sin²τ/2`; 2ψ-form `+sin²τ/2` — the sign pair = the unpinned e₄-dip axis); the 2ψ-form PHASE STRUCTURE is derivation-backed (FORM only, `mass_measure_from_omega`); variants inter-convert on the orbit only UNDER A RE-FIT of `(b,ε)` — the same `(b,ε)` may NOT be carried across forms (×4.6 √m-ratio distortion for down); ε values and the `ε_u/ε_d = 2^{3/2}` counted fit are convention-pinned. Coefficient constraint filed as N60 (r²-orbit caps A ≤ 1 < banked √2, 1.546). New MAIN primitive `brannen_z3_harmonic_collapse_invariant` = R-170 (+2 checks, MAIN 412→414). Noted-non-coincidence (banked as nothing): `ψ_inv ≈ δ_L/2` numerically only because `(1−ε_d)/(1+ε_d) = 0.488 ≈ 1/2`. δ_d RULED (RUL-033, 2026-08-13): the three-object question is closed — δ_d ≔ the hadron-route object; the parametrization/indicator are witnesses. |
| R-074 | Cross-sector D/J agreement: lepton 0.787 ↔ baryon 0.778, ~1.1% | **DERIVED-CALIBRATED, and CONDITIONED 2026-08-23 (R-180/R-181)** | DoverJ_from_lepton_masses + DoverJ_from_skyrme + over_determination_scan + dressed_coupling + `DoverJ_calibration_referent` + `gamma_admixture_cross_functional_route` | C.3 | R-068, R-051, R-177, R-180, R-181 | — | ★ **THE GLOSS *"genuine over-determination signal"* IS CONDITIONED — this is the review's load-bearing exposure and it SHIPS.** What each leg measures is a **ratio of totals** (parity-odd bond amplitude over parity-even), and the two legs' parity-EVEN totals belong to **different functionals** — the generation amplitude and the helix pitch — which are the same substrate number **only if the symmetric-traceless (`Γ`) bond admixture vanishes** (R-181). Indeed `e ≈ √18/(D/J) = cot q`, so **the baryon leg IS the pitch functional**: the two legs are not two reads of one quantity. So the agreement is evidence that **two different readings of the chirality cohere**; it is **not a second reading of one pinned parameter**. The `√18`-bridge geometric-coincidence caveat (R-107) is unchanged and rides alongside. **Same conditioning was owed at three sites and is now APPLIED at two of them (2026-08-24 revision pass, record `knowledge/audit/gamma_referent_2026-08-23/CORE_REVISION_2026-08-24.md`):** §C.3.11 — **APPLIED**, rewritten as *"what the two legs actually measure"* with the different-functionals condition, the `Γ`-admixture size and the standing never-carry-across-functionals fence, and its stale `0.779` corrected to `0.778`; the Core paper's shipped headline — **APPLIED**, at earned strength with *"nothing fitted between them"* and the e-test at its RUL-100 characterization; **STILL OWED:** `over_determination_scan`'s band rationale (*"THREE reads of the SAME quantity"* — the stated ground for the pre-registered ≤1.5% band, hence for the pinned Cabibbo FLAG's *rationale*; the FLAG itself is band-independent by its own note and survives). ★ AND THE ARC-RATIO READING SHARPENS THE SAME FACT FROM THE OTHER SIDE (CANDIDATE): if `δ_L = 2/9` exactly then the lepton leg fixes the ratio and the baryon leg **demands** `e = 5.391979` against the literature's `5.45` — the residual becomes a statement about **one constant** rather than a scatter between two fits, at 1.06%, and **as a test it is NOT YET DISCRIMINATING** (RUL-100(2): the historical `e` is itself a fit whose spread across determinations exceeds the deviation; the test bites only at or below ~1%, read from primaries). Record `knowledge/audit/gamma_referent_2026-08-23/` |
| R-075 | Neutrino forced left-handed from `+e_4` wave direction | DERIVED | forced_handedness | C.3 | A-3, R-007 | R-079, R-060 | Substrate-derived chirality. |
| R-076 | Neutrino lightness from single Weyl ideal | DERIVED | neutrino_lightness (+ `spinor_module_graded_iso` for the carrier relation and the exposure) | C.3 | R-012, R-075 | R-089, R-121, R-182 | Structural consequence of single ideal. ★ **CARRIER RELATION BUILT 2026-08-23 (R-182):** this row's occupancy lives on `S = Cl(4,0)·s₀`, **not** on the V4-0-signed carrier `Cl⁺` — and the two are now known to be canonically isomorphic **as graded LEFT modules** (`Φ(W±) = S±`), so an `I₄`-graded statement about one transports to the other. ★★ **EXPOSURE E-1, RECORDED HERE (pre-existing, not created by that round, not previously carried): THE OCCUPANCY IS NOT BOOST-INVARIANT IN THE BANKED LOCK REALIZATION.** `e₁P₊ − P₋e₁ = 0` exactly and `L_{e₁}(S₊) ⊆ S₋`, i.e. an observer boost (grade-one, the banked realization) maps one `I₄` half INTO the other — so *"the charged lepton occupies both / the neutrino occupies one"* is **not a Lorentz-stable species property** there. Under the grade-two lock alternative the leak is zero. This does NOT touch the row's structural consequence; it names the frame in which the occupancy statement is stable, and it is the same `I₄`-grading↔observer-chirality bridge R-172(viii) declares UNBUILT. Also sited at family-tree node **V4-ASD**. Record `knowledge/audit/external_review_2026-08-22/V4ASD_LAYERA_2026-08-23.md` |
| R-077 | Up/down mirror SD ↔ ASD under spatial parity; up = SD chirality identification | DERIVED-given-R-079, i.e. DERIVED-given-{A-P2′-RIGHT + the RH-singlet datum} (the mirror itself is DERIVED-A at R-099; the *up = SD* side-assignment consumes the weak assignment) [side ruled RUL-091: body-frame/right action on the even-module ideals; left reading retired; chirality structure carried by the `H±` ideal split — ADJUDICATION_R3 §4-bis. "Side" in *up = SD side-assignment* means the SD/ASD chiral factor, NOT the left/right multiplication side — the two senses must not be conflated] | updown_mass_operators_commute + updown_mirror_value_three_handles | C.3 | R-099, R-079 | — | V2 W-LIVE-2 promotion. **Edge direction repaired 2026-08-21:** this row previously listed R-079 under *Used-by* while R-079 listed R-077 under *Used-by* — a two-row cycle, one direction of which had to be wrong. R-077 DEPENDS ON R-079, not the reverse. |
| R-078 | Substrate carriers of SM gauge content (SD, Q-orbit, I_4 + bivector, `e_4`-bond pairing) | DERIVED-STRUCTURAL **for the algebra**; the weak-slot *identification* is **FRAMING** (premise **A-P2**) | spatial_vs_phase_partition + L_Q_orthogonal_decomposition + weak_su2_menu_exhaustion *(names A-P2 explicitly)* | C.4 | R-009, R-010 | R-171, R-079, R-080, R-081, R-082 | Four substrate-distinct sectors match SM gauge content. **A-P2 is now named here rather than left implicit** (the 2026-08-18 Core/Instance sweep rated this row UNCERTAIN with "one adjudication line owed"; that line was the A-P2 stamp, **ruled 2026-08-21 — ENDORSED, RUL-084**). **The stamp does NOT collapse R-079's conditioning to the datum alone:** ENDORSED is a preferred direction, not a Core axiom, so A-P2 remains a named conditioning premise and this row sorts CORE+ENDORSED. A raise would need A-P2 *derived* or stamped CORE. |
| R-079 | Weak = SD (chiral Spin(4) factor) | **DERIVED-given-{A-P2′-RIGHT + the right-handed-singlet datum}** [side ruled RUL-091: body-frame/right action on the even-module ideals; left reading retired; chirality structure carried by the `H±` ideal split — ADJUDICATION_R3 §4-bis] — *tier RAISED from INPUT (2026-08-21, RUL-082, the first C-32 exhausted-menu promotion; tier-raise pass per `manuals/banking.md` §3a, reversal-ledger row logged); premise SHARPENED A-P2 → A-P2′ (2026-08-23, RUL-091) — the module and the side, previously silent, are now named: a 3-dim `su(2)` acting by RIGHT (body-frame) multiplication on the even-subalgebra module. The tier is NOT dropped: the exposure lives inside this cell (keeper's binding rider, D2), because a drop to FRAMING would dissolve the one bit that has been located* | weak_su2_menu_exhaustion *(the closure)* + weak_isospin_SD_parity_exclusion + weak_isospin_centralizer_is_SD + weak_isospin_verdict + weak_isospin_rank_table + vminusa_is_spin4_factor_chirality | C.4 | R-171, R-078 | R-060, R-061, R-077 | **No longer a pick: the menu is closed by computation (R-171).** ASD is the same assignment mirrored (orientation relabelling, RUL-051 family freedom); the diagonal `so(3)` class is refuted by the right-handed fermions' weak-isospin-**singlet** character. **A-P2** — that weak isospin is a 3-dim `su(2)` inside grade-2 `so(4)` at all — is the surviving conditioning premise; it is FRAMING in the engine and is **stamped ENDORSED (RUL-084)**, i.e. a preferred direction a family member may go the other way on, which puts this row in the CORE+ENDORSED conditional column rather than a column of its own. **WOULD-REVERT-IF (C-31 mirror):** A-P2 re-stamped away from ENDORSED, or a fourth conjugacy class exhibited, or the substrate's orientation independently pinned — then INPUT is restored with the "empirically closed at family level" annotation. ★ The old causal gloss *"neutrino-forced (forced-LH + single-Weyl ⇒ chiral)"* is **withdrawn**: R-075/R-076 compute without consuming this row (the arrow runs substrate → neutrino), and the single-Weyl neutrino provably CANNOT discriminate SD from the L-orbit (R-171). V−A, gen-blindness, doublet, up=SD remain DERIVED-given-it. **★ 2026-08-23: the side and module named in this cell's premise (A-P2′-RIGHT — RIGHT/body-frame action on the even-subalgebra module) are now COMPUTED rather than ruled-and-argued — see R-172, `weak_host_must_be_body_frame`. This row is therefore already 'read on the BODY copy' by its own premise and does not restate it; the primitive's MODULE AND SIDE block is the record. Two increments reach this cell and neither moves the tier: (i) the generation-blindness is now blindness to **all** space-frame structure, not only to ASD — `[L_g, R_h] = 0` for every `g, h`, so a body-frame host commutes with everything acting from the observer's side; (ii) the annihilation structure the V−A chain rides is COMPUTED side-independent (R-172(4)), where RUL-091(iii) had only asserted it.** |
| R-080 | U(1)_Y from I_4 + bivector compactness; I_4 cannot be the compact gauge generator (`I_4² = +1` non-compact) | DERIVED | hypercharge + winding_charge + I4_squared | C.4 | R-056, R-010 | R-082 | Gauge field is bivector-generated; I_4 labels the conserved-charge direction only. |
| R-081 | Colour octet `8 = 3 ⊕ 5` symmetric-space split; `C_A/C_F = 9/4 = 2.25` consistent with LEP `2.277 ± 0.02 ± 0.05` (DELPHI/Uvarov 2002, preliminary, colour-dipole-model-dependent; the alternative fit variant gives 2.093 and the variant choice rides partly on agreement with 9/4 — corroboration, NOT an independent test) | DERIVED-A (algebra) + LOCATED-GAP (dynamics) | gluon_octet_symmetric_space_split + colour_quartic_charge_handle + colour_relative_phase_is_coset + colour_sector_E_hermitian_form + colour_su3_located_gap + colour_SO3_re_realization_forbidden | C.4 | R-053, R-072 | R-085 | Static algebra constructed; dynamical running #1-gap-gated. |
| R-082 | `sin²θ_W = 3/8` at the scale where `g_1 = g_2` — a native normalization identity, NOT a prediction of the measured angle | DERIVED-A (the `Σ T_3²/Σ Q² = 2/(16/3)` identity) + INPUT (import I-6, the RG run-down) — the run-down is an OPEN EXPOSURE, not a passed test | weinberg_sin2 | C.4 | R-056, R-062, R-079, R-080, R-009 | (paper headline) | Engine-exact for the identity itself (`twt_test.py` checks the numeric `3/8`). No SU(5) group import — but under GUT normalization `sin²θ_W = 3/8` is *algebraically identical* to `g_1 = g_2`, and it still assumes a single common trace form for `Y` and `T_3`; the `√(3/5)` is native to the algebra, not free of that assumption. `g_1 = g_2` comes from the dim-4 D4 isotropy theorem (same theorem as Lorentz protection, R-016 / R-039) — a *grain-layer* statement, which is why the crossing is placed at the lattice scale `Λ_L = 1/a` (which-Λ ruling 2026-07-30). **That placement is a NAMED PREMISE, not a forced consequence**: identifying bare-lattice stiffness equality with continuum-scheme coupling equality owes the standard lattice→continuum matching correction (Hasenfratz & Hasenfratz 1980; Weisz 1981; Billoire 1981 — Section 10), uncomputed here, so the descent window should not be read past its leading digits. **RETRACTION SWEPT IN 2026-07-29; the paper §C.4.5 was corrected 2026-07-28 and this row was not — a stale-label trail of exactly the canon §2 class.** The earlier claim that running `3/8` down gives `≈ 0.231` is FALSE and withdrawn: with TWT's own content (15 Weyl/gen, one Higgs, no superpartners; the three sterile RH neutrinos of R-121 are total gauge singlets, `δb_1 = δb_2 = 0`, so TWT runs exactly as the SM) `sin²θ_W(M_Z) = 3/8 − 0.0355·t` with `t = ln(M_X/M_Z)/2π`. At `M_X = Λ_L` (ruled band `[0.39, 0.73] M_Pl`) this lands at `0.154–0.158`, some 32–33% below the measurement (`0.147–0.164` at the retired wide bracket). **ESCAPE ROUTES COMPUTED AND CLOSED 2026-07-29** (negatives ledger N55; probes at `knowledge/candidates/probes_2026-07-29/`, nothing banked to the engine): two-loop running moves it `+0.0004` (0.6% of the gap); GUT-style thresholds reach `0.011`; the required `M_X = 1.09 × 10¹³ GeV` sits 5.6 decades below the ruled `Λ_L` band floor (5.2 below the retired wide bracket's) and matches no scale currently on the framework's books, a seesaw scale being structurally forbidden by exact `B − L` (R-089); closing it by field content needs `(δb_1 − δb_2)·ln(M_X/M_T) ≈ −102`, which costs `SU(2)_L` its asymptotic freedom for any threshold above `1.4 × 10⁵ GeV`. |
| R-083 | 24-bond count = 12 + 12; SU(5) labeling as historical translation only (no physical SU(5), no X/Y bosons) | DERIVED-STRUCTURAL | D4_spatial_bond_isotropy + D4_DM_bond_bivectors_non_commuting | C.4 | A-1b | R-104 | Representation-theoretic match with GUT literature; not load-bearing. |
| R-084 | Confinement: ontological-first (one defect, three facets) — topology is formal consequence | DERIVED-STRUCTURAL | pi3_S3_integer_completion + e4_content_confines_quarks_not_leptons | C.5 | R-053, R-006 | — | V2 W-LIVE-5 reframing. |
| R-085 | No fundamental SU(3)_c gauge field; colour octet is elastic-response algebra (3 + 5), not eight gluons | DERIVED-STRUCTURAL | gluon_octet_symmetric_space_split + colour_SO3_re_realization_forbidden | C.5 | R-081, R-053, R-008 | — | Asymptotic freedom β_3 < 0 LOCATED-GAP (Paper 2). |
| R-086 | `⟨I_4⟩ ≠ 0` (DM condensate) delivers parity violation, not EWSB | DERIVED | eta_DM + chirality_does_not_source_P + chirality_is_a_reflection | C.5 | A-1c, R-010 | R-044, R-090 | I_4 is a gauge singlet; condensate invariant under G can't break G. |
| R-086a | Doublet condensate `Φ` on spinor minimal ideal as EWSB order parameter; `⟨Φ⟩ = (0, v/√2)ᵀ` with `v ≈ 246 GeV` breaks `SU(2)_L × U(1)_Y → U(1)_em` via standard mechanism | FRAMING + GATED (magnitude) | — | C.5.3a | R-086, R-062 | — | Structural identification of EWSB on spinor module; absolute `v` and Higgs mass #1-gap-gated. The negative half (⟨I_4⟩ NOT EWSB) is R-086. |
| R-087 | B − L anomaly cancellation from `3 × 1/3 = 1` | DERIVED-A | B_minus_L_anomaly + anomaly | C.5 | R-057 | R-089 | One quark of charge 1/3, three colours; one lepton of charge 1. |
| R-088 | BPST instanton + index theorem ⇒ `ΔB = ΔL = N_gen = 3` selection rule | DERIVED-given-I-2 (imported instanton + index theorem, Section 13) | bpst_charge_Q + bpst_selection_rule | C.5 | R-087 | R-089 | Non-perturbative violation respects B − L exactly. |
| R-089 | No proton decay + Dirac neutrinos + no `0νββ` as one structural fact | DERIVED | B_minus_L_anomaly + bpst_selection_rule + lepton_number_topological_conservation + pi3_S3_integer_completion | C.5 | R-054, R-076, R-087, R-088 | R-121 | Three SM "extras" collapse to one substrate fact. Canonical falsifiers §E.3 rows 2, 3. |
| R-090 | β-decay as L-pair creation through I_4 Hodge map; same D underwrites parity violation + Cabibbo + δ_L + Skyrme stabilizer | DERIVED | I4_maps_L_to_Q + lepton_number_topological_conservation | C.5 | R-010, R-086 | — | One D, multiple manifestations. |
| R-091 | Wave-phase stability ladder across 20 states | CANDIDATE (re-tiered 2026-07-31, C-3/E-5: the prior DERIVED-STRUCTURAL rested on a PHANTOM CITE — `wave_E_complex_structure`/`wave_E5` compute no lifetime, rung, state count or correlation, and no ladder primitive exists) | — (uncited until a `wave_phase_ladder` primitive computes the table and `corr(log N, mass)`) | C.5 | R-007 | — | Referent collision also corrected: §C.5.8's "20 states" (the stable set) and Section 9's 20-state `N = m/Γ` table are DIFFERENT sets; the stable-set result is the separate, real `topological_overproduction_test` (Section 8). Span is ~31+ orders, not the "9" previously printed (Section 9 corrected). |
| R-091a | Top quark exclusion: `Γ_t · Θ_0 ≈ 7.2 ≫ 1` — top facet unwinds before circular winding completes; no top hadrons | DERIVED-STRUCTURAL | top_excluded + alpha_H_gap + x_Q | C.5 | R-053, R-008 | (falsifier §E.3 row 12) | Timescale-exclusion structural argument. The top mass is SM bookkeeping, not a TWT verifier (per canon §5). Was ≈6.5 before the R-133 Θ₀-coefficient correction (2026-07-03); STRENGTHENED. |
| R-091b | Nuclear length hierarchy: hard core `√2 ℓ_S ≈ 0.397 fm` vs empirical 0.40–0.50 fm (12%, no new parameter); pion Yukawa `~1.46 fm`; 25-cell footprint (1 + 24 = D4 kissing); `r_{90} ≈ 0.518 fm`, soliton diameter `~ 1.12 fm` | DERIVED-given-(e, f_π) — no NEW parameter (ℓ_S = ℏc/(e·f_π) rides the two ANW-fitted constants) | nuclear_length_hierarchy + skyrme_length_fm (cover the four lengths; the r_90/25-cell prose is not engine-covered) | C.5 | R-051, R-053 | — | Cell-exclusion phenomena set both hard core and confining-string diameter. 25-cell structure ties directly to A-1b D4 kissing. |
| R-091c | Mesons are NOT topologically protected (`n_𝓠 = 0`, `H = 0` — trivial class on both orbits); stability is empirical: π Goldstone, K/η pseudo-Goldstone, η_c/η_b heavy quarkonia, σ/ρ/ω CANDIDATE substrate identifications. Kinematic mass formula `m = 2 ω · \|cos(α/2)\|` for two opposite-E-sign defect facets | DERIVED-STRUCTURAL (no-protection) + CANDIDATE (σ/ρ/ω) | meson_topological_status + meson_dynamical_current_split | C.5.11 | R-006, R-053 | — | Resolves §A.4's forward-reference to meson decomposition. The no-protection result is the DERIVED content; σ/ρ/ω identifications are CANDIDATE pending §D.5. |
| R-159 | Charge-normalization ANCHOR-FREE: `Q_p + Q_e = 0` identically in `c` — the T₃ bracket and the hypercharge bracket `3Y_Q + Y_lep = 0` vanish separately; `uud` is the unique three-facet composite at `−Q_e`; hydrogen neutrality becomes a theorem rather than a consumed datum | DERIVED-structural CONDITIONAL on (P4, P5, P6, P7), inheriting the weak=SD assignment (R-079, DERIVED-given-{A-P2 + RH-singlet datum}) via R-058/R-079 | charge_normalization_anchor_free | C.2.7, C.2.8 | R-056, R-057, R-058, R-087 | R-063 | **P4** = one universal linear charge functional `Q = T₃ + c·Y` across all sectors — FRAMING-supported by R-035 (single photon bridge) + R-086a (unbroken combination); **R-086a has NO engine primitive — never cite this support as engine-checked**. **P5** = per-defect chirality-independence. **P6** = proton = `uud`, an inside-frame state identification. **P7** = cross-sector weak-isospin alignment `T₃(e) = T₃(d) = −T₃(u)` (INPUT/posited, added 2026-07-31, C-5): flipping the lepton slot alone gives `Q_p + Q_e = +1`, the quark slots alone `−1` (only the global flip is a convention); the engine's `T₃` table is posited in-code, §C.2.3 does not derive the slot assignment, and the SM fixes this alignment BY the charges — so the anchor is RELOCATED into P7, not retired. Counterfactual (derived-vs-generic): delete R-057's `/3` and the residue is `2c ≠ 0` — substrate-specific, not generic. `c = 1/2` fixings, honestly counted: ONE native route (itself conditional on the wave-decoupled ⇒ `Y(S_−) = 0` inference — its own would-change-if) + TWO independent conditions under the I-18 anomaly import + ONE downstream condensate check. Retires the neutrality-of-atoms import at this site CONDITIONALLY; would revert if per-orbit normalizations can differ. New falsifier §E.3 row 16. **ENGINE↔ROW ALIGNMENT REPAIRED (charge-sector repair):** this row and §C.2.7 named P7 while the engine primitive's own premise list, `tier` and `headline` named only P4–P6 — and the code used the alignment regardless, so the engine was understating its conditionality against its own record. The four-premise reading is the correct one; P7 is now named in the primitive AND computed there (`counterfactual_P7_slot_flips`: lepton-only flip → +1, quark-only → −1, global → 0), with the harness assertion moved to match. |

---

## Part D — The substrate, technically

| ID | Statement | Tier | Engine | § | Deps | Used by | Notes |
|---|---|---|---|---|---|---|---|
| R-092 | Cl(4,0) ≅ M₂(ℍ) by Bott periodicity | DERIVED-A | cl_dimension + _cl40 + cl40_quaternion_triple + cl40_vs_cl41 | D.1 | A-1a | R-014 | Engine-verified. |
| R-093 | The quaternion subalgebra `ℍ = Cl⁺(3,0) = span{1, e₂₃, e₁₃, e₁₂} ⊂ Cl(4,0)` — the `ℍ` of the native formalism `Cl(4,0) + ℍ`; **distinct from** the SD/ASD split `Cl⁺(4,0) ≅ ℍ ⊕ ℍ`, of which it is neither summand nor ideal | DERIVED-A | cl40_quaternion_triple + cl40_vs_cl41 + cl41_grounding_litmus | D.1 | R-092 | R-020 | Row title corrected 2026-07-28: previously read "Cl⁺(4,0) ≅ ℍ ⊕ ℍ — the quaternion subalgebra", which fused the two ℍ's this row exists to keep apart, so §A.5.6 cited R-093 for a statement its own title contradicted. Engine-verified: the span is closed under the geometric product (16/16 products in-span) and neither `(1±I₄)/2` projection fixes it. Three objects wear the name ℍ (this subalgebra; the two SD/ASD summands; the ASD summand hosting generations, R-098) — §D.1.2. |
| R-094 | `e_5` grounding litmus: Cl(4,1) constructions are grounded iff `e_5`-content reduces to PHASE under Cl(4,0)+ℍ picture | DERIVED-A | cl41_grounding_litmus + cl41_phase_is_external_u1 + cl41_idempotents_note | D.1 | R-092 | R-095 | Canon §5 guardrail. Catches `e_5`-as-spatial-DOF errors. |
| R-095 | Primitive idempotents in Cl(4,1); meta-time phase as external U(1) | DERIVED-A | cl41_idempotents_note + cl41_phase_is_external_u1 + dirac_ideal_idempotent | D.2 | R-094, R-012 | R-007 | Meta-time rotor lives here. |
| R-096 | Dirac spinor as M₂(ℍ)-module element; wave field structure | DERIVED-A | spinor_real_dof + dirac_ideal_idempotent | D.2 | R-012, R-014 | R-026 | Standard. |
| R-097 | Anchoring triple products: Q-orbit bivector triple `e_{14} e_{24} e_{34} = −I_4` (→ pseudoscalar); Q-orbit trivector triple `e_{124} e_{134} e_{234} = +e_4` (colour singlet, → vector). The L-orbit triple `e_{12} e_{13} e_{23} = +1` closes to a scalar and is not an anchoring identity | DERIVED-A | L_Q_orthogonal_decomposition + triple_product_Q + triple_product_color + L_algebra_su2_closure | D.2 | R-009, R-010 | R-057, R-061 | Engine-verified. Two anchoring triples. Row corrected 2026-07-02: the previous statement `e_{12} e_{13} e_{23} = −e_4` was the stale pre-γ-5 error (engine: `+1`); paper §D.2.3 was already correct — the Index row had not been synced. |
| R-098 | Anti-self-dual generation triple `{e_{12}+e_{34}, e_{13}−e_{24}, e_{14}+e_{23}}` engine-exact | DERIVED-A | anti_self_dual + self_dual + self_dual_blade + chiral_split_demo + spin4_generator_count | D.2 | R-009 | R-071, R-077 | Hosts ℍ ≅ ASD bivectors. |
| R-099 | SD ↔ ASD mirror under spatial parity (engine-exact) | DERIVED-A | self_dual + anti_self_dual + duality_map + chiral_split_demo | D.2 | R-098 | R-077, R-079 | Underwrites up/down mirror. |
| R-100 | Grade dictionary (load-bearing reference) | DERIVED-A | spatial_vs_phase_partition + wave_E_complex_structure + wave_E5 + spin4_generator_count | D.2 | R-009, R-010, R-098 | (downstream Cl-typed claims) | Full lookup. |
| R-101 | D4 lattice: kissing number 24 (densest 4D packing, Cohn-Kumar 2017) | INPUT (premise A-1b unpacked) | — | D.3 | A-1b | R-103, R-104 | Empirical. |
| R-102 | Grain as unit Clifford rotor at each D4 site: the local state is a **4D ORIENTATION — a unit even element of `Cl⁺(4,0) ≅ ℍ⊕ℍ`, SIX real parameters** — acting one-sidedly on the spinor module | FRAMING | s0 + spinor_real_dof + pi3_orientation_class_two_windings | D.3 | R-101, R-012 | R-103, R-110, R-036, R-041, R-037, R-163, R-108, `n_goldstone_canted_FM` chain (→ `canting_critical_stiffness_at_DJ` → R-109/`electron_QCP_nu`) | Substrate building block; the medium's local degrees of freedom. **Six, not three:** `dim so(4) = C(4,2) = 6`, engine-censused, and the chiral factorization of that grade-2 sector into two commuting oppositely-oriented su(2) triples is what carries R-002's TWO windings. The continuum field inherits this target unchanged (D.4.1) — the layer-inheritance clause R-002 rests on. **WHERE the ℤ₂ sign lives is an OPEN BRANCH** (family tree Core node LS-ℤ₂): sign-in-the-state (`Spin(4)`, the one-sided action) vs sign-in-the-emergent-covering-sector (`SO(4)` + the odd character of π₁(Q_N) = ℤ₂ at B.3.5). Nothing in the winding column depends on the branch — covering maps are isomorphisms on π_n for n ≥ 2, so π₃ and π₄ agree. The 2-parameter (D.4.3 `E(q)`, DM vector) and 3-parameter (`n_goldstone_canted_FM`, `sigma_model_kinetic_normalization`) readings are **explicitly-stated L-orbit-SECTOR reductions** of this state space, not rival declarations of it. **WITNESS SITING (RUL-083, 2026-08-21): this row is V3's D4-sited WITNESS of the Core LS axiom, not the axiom's family-level carrier — the axiom is stated witness-free for any grain structure (charter LS note; family-tree LS-6); a family member on a different grain re-witnesses.** |
| R-103 | J + D coupling structure: symmetric exchange on 24 NN bonds + DM on 12 `e_4`-bonds | DERIVED-STRUCTURAL (uniform-J on the 24 bonds is FORCED by leading-order isotropy — engine-verified) + **PICK** (the `{J, D}` truncation, and the `e₄`-only DM support) + INPUT (ratio) | D4_spatial_bond_isotropy + D4_DM_bond_bivectors_non_commuting + **dm_chirality_polarisation_lock** + dressed_coupling + DoverJ_from_lepton_masses | D.3 | A-1c, R-101, R-102 | R-107, R-108 | **"The unique pair allowed by parity on D4" is STRUCK as known-false.** The pair is a truncation pick from the ten-constant driven-group menu (see the A-1c row; family-tree V3-2 / V3-2a); parity cannot exclude the parity-even Γ channel, and the spatial-bond second `D` is symmetry-allowed at the same group. **Two findings that run the corpus's way, banked with the correction:** uniform-J across all 24 bonds is forced, not assumed; and at the driven group `Stab(+e₄)` the allowed DM space is 2-dimensional with NO chirally polarised element — every allowed `D` is forced exactly 50/50 SD:ASD, so "two chiral dials, one turned" is an over-statement there (the doubling to 4 = 2 SD + 2 ASD is bought by dropping the 24 reflections, i.e. by Hamiltonian-level reflection breaking the drive axis does not supply). Tier note on that zero (canon §5): GENERIC-GIVEN-ONE-ORIENTATION-REVERSING-ELEMENT, not a D4 discovery. Fence: bond-coupling SD/ASD content licenses nothing about weak isospin. The ℤ₃ `cos`/`sin` **parity assignment** remains ASSERTED (negatives ledger N62, sub-note JD-5). ★ **CROSS-FUNCTIONAL FENCE ADDED 2026-08-23 (R-181):** this row's branch/pitch objects carry their **own** `J_eff`, distinct from the ℤ₃ amplitude's and from the `f_π` stiffness's, because `Γ` renormalises each through a different functional — *never carry a ratio calibrated on one functional into another*. ★ **AND JD-5 IS RESTATED AT HONEST SCOPE (R-177):** on the PITCH functional the parity assignment is an **identity** (`q → −q` **is** `W → Wᵀ`, and `Tr(K Wᵀ) = Tr(Kᵀ W)` holds for arbitrary real `W`) — but that is a **different functional**, so **nothing of JD-5 as recorded (the ℤ₃ amplitudes) is discharged**; the *"half-discharged"* label is WITHDRAWN. Record `knowledge/audit/gamma_referent_2026-08-23/` |
| R-104 | 24-bond 12+12 split: 12 spatial + 12 `e_4`-bearing | DERIVED-A | D4_spatial_bond_isotropy + D4_DM_bond_bivectors_non_commuting | D.3 | R-101 | R-083 | Underwrites §C.4. |
| R-105 | Two-scale framework — forced GIVEN the two anchored empirical scales (`G_N`-backfit Planckian grain layer + `f_π` hadronic cell layer) | DERIVED-generic-given-(`G_N`, `f_π`) / FRAMING (re-tiered 2026-07-31, D-10; no engine cite — the Editorial rule governs a no-cite DERIVED row) | — | D.3 | R-037, A-1c | R-039, R-119 | What is forced: a single-scale substrate cannot host two numbers ~20 orders apart. The two-layer ARCHITECTURE with its open cell-formation map is adopted, not derived. |
| R-106 | Magnon kinetic stiffness identifies `f_π² = 8J/a` | DERIVED at dressed-coupling | f_pi_squared + sigma_model_kinetic_normalization | D.4 | R-103 | R-051, R-181 | Condensate identification (T0b.2). ★ **JD-6(b) POINTER (R-181, 2026-08-23):** the `J` this row fixes is a **quadratic-fluctuation** object — exactly where `Γ`'s dispersion kernel `Q(k) = Σ_b (k·b)²K_b` lives — so it is **its own** `J_eff`, distinct in general from the pitch's and from the ℤ₃ amplitude's. The three coincide only if the `Γ` admixture vanishes. **Combining this `J` with the lepton-calibrated `D/J` crosses two different `J_eff` and is unlicensed** under the standing fence *never carry a ratio calibrated on one functional into another*. Values unmoved; what moves is the claim that the formula is fed the right substrate quantity. Record `knowledge/audit/gamma_referent_2026-08-23/` |
| R-107 | Skyrme stabilizer relation `e ≈ √18/(D/J) ≈ 5.37` (dressed-coupling) | DERIVED at dressed-coupling | dressed_coupling + kappa_F_bare + spiral_angle_deg | D.4 | R-103 | R-051, R-074 | Geometric-coincidence caveat noted (per V2 §10.3.3). |
| R-108 | Canted-helix vacuum: the closed form `tan q = D√2/(6J)`, `cos q ≈ 0.983` at D/J ≈ 0.79, and the branch structure of the single-`q` helical family (§D.4.3) | DERIVED-A (the closed form as the leading-order helical-rate invariant `\|k\|·λ = √2D/(6J)`, direction-degenerate at O(q²); AND the stationarity of the axis configuration `k = q·e₁`, `B = E₁₄`; AND the transverse second variation `4J(cos q+3)(cos q−1)/cos q`, an identity) + DERIVED-numeric (the axis configuration is an INDEX-2 SADDLE for every D/J > 0 and the body-diagonal branch lies lower by `ΔE = −(1/243)(D/J)⁴·J` at leading order — **exact-arithmetic minimisation owed**; every minimality claim scoped "within the single-`q` simple-bivector helical family", RUL-049) + LOCATED-GAP (`K_c` and any genuine substrate criticality — the "transition"/"critical at `D = J`" wording WITHDRAWN 2026-07-31, D-5: V1's stability scan finds the spiral locally stable `D/J ≈ 0.75–7.35` with no feature at `√18` or `D = J`, but that scan varies the PITCH at fixed `k̂` and is blind to the transverse directions the saddle result uses; the `D = J` "QCP" is the lepton-parametrization zero of §C.3.6, conditional on the `A = J, B = D` ansatz, not a substrate transition) + LOCATED-GAP (**branch selection** — which branch the DRIVEN kernel picks; static energetics need not govern a NESS vacuum; assembly-recorded at §D.5.7, RUL-030 class 2, hence CANDIDATE by definition) | canting_pitch_q_rad + canting_cos_q + **canting_vacuum_branch_structure** + canting_critical_stiffness_at_DJ + Kc_magnon_stiffness_canted_FM_at_DJ + n_goldstone_canted_FM | D.4 | R-103 | R-055, R-117 | Two of the five original cites are themselves LOCATED-GAP-REFINED; the old flat DERIVED-A over-read them. **Retiered at the J,D/Γ rework (governing record `knowledge/candidates/probes_2026-08-20/`: report §7 + §14(b1), `REDERIVATION_HELIX_MINIMUM_2026-08-21.md`, `VERDICT_REF1_JD2B_2026-08-21.md`, `VERDICT_KEEPER_2026-08-21.md` collision 1; negatives ledger N62).** The word "ground state" is struck: §D.4.3 fixed `k̂` by hand and minimised in one variable — an LT ansatz, not an LT minimisation. **NORMALISATION MUST TRAVEL WITH THE GAP:** 1.548e-3 J per site at D/J = 0.787 is 3.2e-5 of the full frame-bilinear bond total (−48J) and 6.4e-5 of §D.4.3's own printed `E(q)` total (−24.2J). Both stationary points are screw states `B = k̂ ∧ e₄`; the diagonal's sign pattern is a symmetry orbit, not a distinguished direction. Prior art, not the framework's: axis-vs-diagonal helix selection at ~1e-5 splitting is standard cubic-helimagnet physics (Bak & Jensen 1980), and LT certifies a global minimum only under the strong constraint (Lyons & Kaplan 1960), unverified here. ★ **CROSS-FUNCTIONAL FENCE ADDED 2026-08-23 (R-181), and a scope quantification (R-179):** the pitch is its own `J_eff`-bearing functional, so feeding it the **lepton-calibrated** `D/J` carries the unnamed premise that the two functionals' parity-even totals coincide — values unmoved, the CLAIM about what the formula is being fed moves. And the `Γ` survivor's exact inertness holds **on these two banked high-symmetry branches only**: off them its pitch entry is a few percent of `J`'s own even weight worst case (~0.1% median, equal per-bond scale), so branch selection and the survivor's protection are **coupled** (GR-1; keeper latent L-2). Record `knowledge/audit/gamma_referent_2026-08-23/` |
| R-109 | Skyrme Lagrangian with coefficients fixed at the DRESSED level (full medium Lagrangian; V1's branch-(c) verdict restored at §D.4.4, 2026-07-31 D-9: bare `κ_F = J/24` gives `e_bare ≈ 0.87` — ~6× off and `D`-independent — while the DM-dressed contribution diverges through the gapless phason) | DERIVED at dressed-coupling, **branch-(c) conditional** (the referent of the six rows carrying that tier) | skyrme_BVP_audit + sigma_model_kinetic_normalization | D.4 | R-106, R-107, R-108 | R-051 | Standard ANW phenomenology applies at the dressed level. |
| R-110 | DM-induced topological boundary term `𝓛_top = µ Ψ_0 ρ_L` | DERIVED form (coefficient µ OPEN) | DM_operator_gaussian_dim | D.4 | R-103, R-102 | R-090 | Source of β-decay channel. |
| R-111 | `1/Θ_0 ≈ 196 MeV ~ Λ_QCD` as CANDIDATE for QCD scale identification | CANDIDATE | nuclear_length_hierarchy + qcd_uv_conformal_phaseCD | D.4 | R-106, R-103 | — | Identification not closed. Was ≈215 before the R-133 Θ₀-coefficient correction (2026-07-03); stays in the Λ_QCD range (scheme caveat: closer to folk ≈200, farther from Λ^(5)_MSbar ≈ 210 — no strengthening claimed). |
| R-112 | Master wave equation and its three faces — linear, topological, collective. Face 1's isotropic 5D form is an IDEALIZATION of the anisotropic-stiffness quadratic order (`K_long = √38·J ≠ K_⊥` on the canted vacuum — the engine's own N31 result; restated §D.4.6, 2026-07-31 D-1) | DERIVED-STRUCTURAL, conditional on the isotropic-projection question (whether the `O(q²)` splitting reaches the locked observer is OPEN; species-universal part I-22-absorbable at dim-4; sidereal part = SC-2) | wave_E_complex_structure + wave_E5 + eom_constraint_class | D.4 | R-106, R-103, R-007 | R-117, R-118 | Three faces of one EOM; the spine consumes the idealization with a named, bounded correction. COMPLETION NOTE (τ₅ adjudication 2026-08-13): any τ₅-hyperbolic completion of the nonlinear functional carries an undetermined mixed-quartic coefficient λ (a MENU; the covariant value is pinned only by the one-metric index-raising convention, which itself holds only inside this row's isotropic idealization — N31's five stiffnesses; §D.4.4 note); hyperbolicity on the defect background BOUNDS λ ∈ (−0.124, +2.903), does not pin it (N61 round). |
| R-113 | Memory effect — mechanism on driven D4 substrate | FRAMING | eom_compatible_field_forks + eom_invariant_variant_audit | D.5 | A-2, R-112 | R-114, R-115 | The substrate kernel's role. |
| R-114 | Memory requirement: a memoryless kernel cannot supply `τ_mem ≫ τ_wave`, which Role-3 selection and §D.5.4's roles need — the former "monostability theorem" wording is WITHDRAWN (its no-stable-Skyrmion premise contradicted §A.3's topological stability: the drive-zero limit is the static Skyrme BVP with stable integer-winding solitons) | FRAMING (re-tiered 2026-07-31, D-3 — Section 2's line always said FRAMING; this row now agrees, resolving the 303/563 contradiction) | eom_compatible_field_forks | D.5 | R-113 | R-115 | The sole cite is itself `[FRAMING —`-tagged and its relevant assert checks a Python enum. `kernel_candidate_constraints` C2 re-sourced to the memory-requirement claim. |
| R-115 | Rich/hysteretic kernel ADOPTED on physical motivation (defect persistence); fading-vs-hysteretic is #1-gap GATED | CANDIDATE (committed by choice) | eom_compatible_field_forks | D.5 | R-114, A-2 | R-118 | W-LIVE-3. Leans hysteretic — but N46 (W3.3/A1) shows this "lean" is a LARGE-BARRIER-regime effect, NOT a clean-symmetry result: the SNIC escape is governed by kernel numbers non-monotonically, a small barrier PROMOTES it. |
| R-116 | Three roles of memory: cell formation; Role-3 (selection); Bell-pair memory | FRAMING + value-gated | im_chi_falsifier_budget_KSS_GW_macromolecule + identify_the_floor | D.5 | R-113 | R-030 | One kernel, three faces. |
| R-117 | Linear face structurally safe — leak-independence, symmetry-protected unitarity, Goldstone-protected decoherence (WP-IX3/IX4/DC2) | DERIVED-STRUCTURAL (inherits R-112's isotropic-projection conditional, D-1 2026-07-31) | eom_invariant_variant_audit + interference_can_reduce_mass_goldstone + identify_the_floor + massless_H_squared + protection_mechanism_located | D.5 | R-112, R-108 | R-023, R-027 | Why QM and Bell are unaffected by which side of memory fork wins. |
| R-118 | Θ_rel as highest-value target — coset-Cartan FDT-violation residual ties colour-U(3), CKM-P, memory fork, SOC coupling | FRAMING + #1-gap-gated | theta_rel_universality_located + theta_rel_pinnability_from_data + theta_rel_equivariant_bifurcation_spine + theta_rel_rotating_wave_escape_located + theta_rel_fork_escape_kernel_number_governed + theta_rel_z3_isotropy_dichotomy + colour_relative_phase_is_coset + colour_quartic_charge_handle + colour_abare_static_holomorphic + colour_arich_kernel_dependent | D.5 | R-115, R-053, R-073, R-081 | R-119 | Z3-breaking shared condition derived (engine-exact); single kernel value gating four faces is candidate. |

---

## Part E — Cosmology, status, frontiers

| ID | Statement | Tier | Engine | § | Deps | Used by | Notes |
|---|---|---|---|---|---|---|---|
| R-119 | Cosmological-constant residual is the driven-dissipative deviation from Volovik equilibrium (value-gated, #1-gap-routed) — **scope narrowed 2026-07-29 to a present-epoch remark**: `ρ_vac ≈ 3Ω_Λ,0 M̄_Pl² H_0²` (near-definitional); the DYNAMICAL reading `ρ_vac ∝ H(t)²` at all epochs is EXCLUDED | FRAMING + value-gated (magnitude only; no epoch law) | gravitating_vacuum_energy + lambda_resolution_structure + lambda_H2_dynamical_reading_excluded | E.1 | R-047, R-115 | — | Canonical falsifier §E.3 VG-2. Exclusion computed at N54 / §E.1.1. **TWT claims no dark-energy prediction at V3.** |
| R-120 | Multi-defect well-posedness of the wavefront field equation as structural-coherence condition (not currently testable since EOM unformulated) | FRAMING + coherence-condition | — | E.1 | A-2, R-053 | — | Canonical falsifier §E.3 SC-1. |
| R-121 | Three sterile right-handed neutrinos as parameter-free DERIVED prediction (B−L conservation forces Dirac character; RH partner is `S_−`) | DERIVED | sterile_rh_relic_check | E.1 | R-089, R-076 | R-122 | Structural; engine-banked. |
| R-122 | Sterile RH relic: sterile SHARE ~1.1% of Ω_DM, 94× shortfall (the active+sterile TOTAL is ~2.1%/47× — the engine key predating the relabel reports the total; E-6, 2026-07-31); the remaining ~98% is now the inter-front programme's TARGET (handoff §7, 2026-07-31), not a standing scope fence | LOCATED-GAP | sterile_rh_relic_check + sterile_rh_z2_separate_mass_scale_check + sterile_rh_substrate_production_via_L_theta | E.1 | R-121 | — | Canonical falsifier §E.3 VG-4. Z1/Z2 LOCATED-GAP-REFINED; Z3 still OPEN. Lead (i) differential coupling and (ii) wave-train phase-defect remain OPEN. |

---

## Coverage check (Phase α-7 to verify in detail)

**Engine primitive coverage.** Every engine name in the *Engine* column above must exist in
`twt.py`. Phase α-7 runs the cross-check; the full primitive list is at
`scratchpad/twt_primitives.txt`.

**V2 result coverage.** Every load-bearing V2 result should map to an R-NNN or to a paper-only
synthesis result that doesn't need an R-NNN. Phase α-7 walks V2 §-by-§ to catch orphans.

**Falsifier cross-references.** §E.3's four tables reference the R-NNN above; the canonical
falsifiers from V2 §25.2 are:

- *Named near-term* (16 rows, in table order): `c_GW = c_γ` (R-039), proton decay (R-054),
  `0νββ` (R-089), Geneva influence speed (R-031), Bell-foliation (R-031), differential `c_meta`
  (R-045), optical-clock decoherence (R-117), macromolecule decoherence (R-030), CHSH > 2√2
  (R-027), monopole (R-033), fractional charge (R-062), top baryon (R-091a), 4th generation
  (R-071), TRULY-independent `θ_C` (R-073), tree FCNC (R-061), proton–electron charge sum
  (R-159).
  **Retired 2026-07-27:** the two former head rows — UHE-CR LV and `α_3` — were DELETED, not
  renumbered away. The LV row read a dimension-six prediction against a dimension-four bound and
  claimed "at current bounds"; the correct dimension-six comparison excludes the *naive* coefficient
  by 3–9 orders (which-Λ ruled 2026-07-30: naive `η⁽⁴⁾ ∈ [1.9, 6.7]` on the `Λ_L = 1/a` band —
  see R-037; the 2026-07-28 wide bracket and its 2–10-order restatement are RETIRED), so the item is
  not a near-term test at all. It is now VG-6 (value-gated) plus the
  §E.3.5(4) pre-mortem item, and negative N52. The `α_3` row rode the same ceiling against a
  solar-scale `(E/Λ)² ~ 10⁻⁹¹` and was never a near-term test. See R-165.
- *Removed*: chiral matter wrong-sign gravity (R-040), `ξ = 1/6` cancellation (R-041), Koide
  modus-tollens (R-061 family), Cabibbo f_perp (R-073 family), V_PMNS=I phantom (resolved
  per V2 Phase C; no R-NNN — defused prediction), nu-asymmetric (resolved per V2 Phase D; no
  R-NNN), over-production test (R-091 via `topological_overproduction_test`).
- *Value-gated*: VG-1 Im χ budget (R-030), VG-2 Λ ~ H² (R-119), VG-3 1/T_2 (R-117), VG-4 dark
  matter (R-122), VG-5 GW dispersion (R-039), VG-6 dim-6 isotropic LV coefficient `η⁽⁴⁾` (R-165).
- *Structural coherence*: SC-1 multi-defect (R-120), SC-2 cell-order (R-016).

---

## Editorial reminder

- A row with **no engine cite** (`—`) is *paper-only*. That is honest if the result is kinematic
  or synthesizing (e.g. R-024, Schrödinger from the KG envelope — a kinematic reduction best
  stated in the body). It is **dishonest** if the row claims an engine-verified
  derivation without one. Phase α-7 grep `Engine: —` and audit each case. **A third failure mode,
  found the hard way at R-022 (review item III-13, 2026-07-29): a paper-only row can carry a
  derivation that is not merely unchecked but VACUOUS.** "Requiring reality" of `⟨φ̃ M̂ ψ⟩_0`
  constrains nothing in a real Clifford algebra, and no harness reads prose. When a paper-only row
  is load-bearing, write the primitive.
- A row whose engine cite **does not yet exist in `twt.py`** is a phantom cite (CLAUDE.md §2:
  bank before you cite). Phase α-7 checks the primitive list. Any phantom found is either
  (a) downgraded to no-cite, or (b) flagged for engine-banking BEFORE V3 ships.
- A row whose **tier is unstable** (e.g. R-068 FIT post WP-MASS-MEASURE) should say so in the
  Notes column. The Result Index is the place where tier qualifications live.

---

# Section 2 — Dependency Graph

*Structural picture: axioms → Layer 1 (algebraic) → Layer 2 (dynamical, gated) → Layer 3 (structural deep gates).*


*Version 3 · Phase α draft · 2026-06-30.*
*Companion to Section 1 (Result Index). Where the Result Index is a flat lookup table, this file
is the structural picture: which results are axioms, which fall out algebraically, which depend
on the open dynamics, which are deep structural gates. Both files cover the same R-NNN inventory;
this one renders it as a causal chain.*

---

## METHOD

Each result has at most one of three positions in the graph:

- **LAYER 0 — Axioms.** Ontological premises (A-1a/b/c, A-2, A-3, A-1*, A-2\*). Listed in the
  V3 paper's Opening; expanded at the top of this file.
- **LAYER 1 — Algebraic / kinematic consequences.** Each follows from Layer 0 by an explicit
  Cl(4,0) algebra mechanism or a kinematic identity. Engine-verifiable. Most R-NNN of Part B's
  spine sit here.
- **LAYER 2 — Dynamical consequences (gated on A-2 closure).** Magnitude or running results that
  depend on the substrate dynamics having a specific form. The framework's #1 gap (§D.5) lives
  here. Engine cites raise.
- **LAYER 3 — Structural deep gates.** Open constructions of decade-class difficulty (the
  texture tetrad's absolute coefficient; the QCD UV gate). Each is its own structural decision,
  not a single calculation.

Each edge in the graph is named: `R-X depends on R-Y because <mechanism>`. The mechanism must be
statable in one line, or the edge is a *gap* and the dependency is flagged.

---

## LAYER 0 — Axioms

The seven axioms listed in the V3 Opening. Reproduced here with their direct-consequence edges.

### A-1a — 4D Euclidean substrate
Direct consequences: R-001 (wave-train exists), R-009 (L/Q bivector split is a structural fact
of grade-2), R-014 (Cl(4,0) is M₂(ℍ), forcing the Lorentzian-partner algebra), R-037
(Sakharov Λ² comes from 4D), R-071 (count = dim Λ²₋(ℝ⁴) = 3, generic-given-4D; Frobenius a remark via associativity — ℍ-units identified
with generations), R-092 (Cl(4,0) ≅ M₂(ℍ) by Bott periodicity).

### A-1b — D4 cell lattice
Direct consequences: R-083 (24-bond count), R-101 (kissing number 24), R-104 (12+12 spatial /
e_4-bearing split). Inheritor of the lemma that ties §C.4's `sin²θ_W = 3/8` to D4 isotropy
(through R-082's `g_1 = g_2`).

### A-1c — J + D bond couplings (a TRUNCATION PICK from the ten-constant driven-group menu)
Direct consequences — **ONE dependent set, reconciled with the Section 1 rows at the J,D/Γ
rework (the two faces of this record previously asserted two different sets, which is why the
reconciliation is stated rather than silently applied):**
**{R-051, R-055, R-070, R-086, R-103, R-105}**, plus the pending-values registry's `f_π` row.
Every member genuinely consumes the coupling content (the pair itself, or the `D/J` ratio).

**Three edges re-typed or struck in the same pass** (keeper-confirmed; the rows carry the
reasoning): **R-007** (mass = meta-time rotor frequency) → **re-typed to A-2** — this block's own
former gloss said "sustained by drive", and drivenness is A-2 / Core S5, not A-1c's coupling
content; **R-036** (rotor field as local Lorentz frame) → **struck**, a residue of the
`U(x) ∈ SU(2)` + canting + `e₄` assembly the state-space repair deleted; **R-127** (front-phase
hand-off) → **struck at present**, with an owed-if-built prospective edge that cannot be written
until the §D.4.3 branch question resolves. Net effect: three rows move Core-side and S1c's blast
radius does **not** exceed the numerical-spine reading.

**Also formerly listed in this block but not carrying an A-1c edge in the rows:** R-068 (its own
Depends are R-064, R-066 — the Brannen fit, not the couplings); R-107, R-108 and R-110, all of
which reach A-1c *through R-103*, which is in the set above.

### A-2 — Driven dynamics premise (#1-gap placeholder)
Direct consequences: R-113 / R-114 / R-115 (memory effect), R-116 (three roles), R-118 (Θ_rel).
**This is the gating axiom.** Every Layer-2 result depends on A-2 closure for its absolute
magnitude. Engine primitives `alpha_em_value`, `texture_tetrad`, `qcd_collider_phenomenology`,
`theta_rel_*` raise until A-2 is closed.

### A-3 — Wavefront / signature locking
Direct consequences: R-013 (`γ⁰ = e_4`), R-015 (Lorentzian signature emerges), R-043 (arrow of
time as `+e_4`), R-045 (`c_meta = c` on average), R-075 (neutrino forced left-handed by `+e_4`).

### A-1* — Matter = defect
Direct consequences: R-004 (load-bearing ontology), R-005 (two faces coupled by I_4), R-016
(one substrate, one light-cone — Lorentz protection), R-039 (γ = 1 from R-016).

### A-2* — Outside-frame working method
Direct consequences: R-003 (discipline). Not a generator of numbered results; it's a method.

---

## LAYER 1 — Algebraic / kinematic consequences

All Cl(4,0) / Cl(1,3) results that fall out of A-1a + A-3 by explicit mechanism, plus
identities involving A-1c's structural part. Tier: DERIVED-A throughout.

### 1.1 The spinor and grade structure
- **R-009** (L/Q bivector orthogonal decomposition) ← A-1a, via grade-2 decomposition
- **R-010** (I_4 Hodge map) ← R-009, via `I_4 = e_1 e_2 e_3 e_4`
- **R-011** (rotor sandwich half-angle) ← R-009, via `R = exp(θ B/2)`, `B² = −1`
- **R-012** (spinor minimal left ideal) ← A-1a + idempotent
- **R-012a** (Cl(4,1)+meta-time phase E; native Cl(4,0)+ℍ; e_5 grounding litmus) ← R-010 + R-012 (full at §D.1)
- **R-092** (Cl(4,0) ≅ M₂(ℍ)) ← A-1a + Bott
- **R-093** (Cl⁺(4,0) ≅ ℍ ⊕ ℍ) ← R-092
- **R-097** (L/Q triple products) ← R-009 + R-010
- **R-098** (ASD generation triple) ← R-009 + chirality
- **R-099** (SD ↔ ASD mirror) ← R-098 + spatial parity
- **R-100** (full grade dictionary) ← R-009 + R-010 + R-098

### 1.2 The wavefront isomorphism and emergent Lorentzian signature
- **R-013** (γ-matrices satisfy Cl(1,3) Dirac relations) ← R-009 + A-3
- **R-014** (φ is isomorphism; lands on M₂(ℍ) not M₄(ℝ)) ← R-013 + R-092
- **R-015** (Lorentzian signature = algebraic shadow) ← R-013 + R-014. **Posit plus derived implication, relabelled 2026-07-29 (coordinator):** `e_5² = −1` is an INPUT placement of the signature, not a theorem; what is DERIVED-A is R-014 (`Cl(4,0) ≅ Cl(1,3)`), which then *forces* the wavefront-locked observer's signature rather than leaving it a second free choice. Charge quantization (R-063/§C.2.8) is the one spine result derived end to end — and it is carried SPLIT: the discreteness and the c-free neutrality identity are what run end to end; the 15-value assignment rides an entered anchor plus P4–P7.
- **R-165a** (no anisotropic quartic ⇒ leading rotational anisotropy at **dimension eight**) ← R-004
  + the D4 point group. Mechanism in one line: `Aut(D4 root system)` has order 1152 = `\|W(F4)\|`
  (invariant degrees {2,6,8,12}), so its degree-4 invariant space is 1-dimensional — `(k²)²` alone —
  and no point-group-symmetric analytic kernel admits an anisotropic quartic. **Edge premises
  (P-an, P-pg)** ride this edge, not the node: analyticity in `k`, and the FULL group including
  triality. Substrate-specific, not generic — `Z⁴`'s point group admits `Σk_i⁴`.

### 1.3 Special relativity
- **R-017** (Klein–Gordon via Fourier at `k_4 = m`) ← R-007 + R-013
- **R-018** (Lorentz generators K_j, J_i; so(1,3) closure) ← R-013
- **R-019** (Thomas precession sign) ← R-018

### 1.4 QM postulates
- **R-020** (Born subspace `{1, B}` forced by centralizer intersection) ← R-009 + R-012
- **R-021** (Postulate 1: complex Hilbert) ← R-020
- **R-166** (self-adjointness forced by the `{1, B}` projection: `⟨ψ̃ M̂ ψ⟩_B = 0` ⇒ the reversion-fixed subspace, dim 2 on `Cl⁺(4,0)` / dim 6 on `Cl(4,0)`, all three `B_a`) ← R-021
- **R-022** (Postulate 2: self-adjointness as `M̃ = M`) ← R-021, R-166
- **R-023** (Postulate 3: Born even-power) ← R-021, structural + plausibility-modulo-degree
- **R-024** (Postulate 4: Schrödinger from KG envelope) ← R-017 + R-021
- **R-025** (Postulate 5: spin-statistics SELECTION + Spin(4) consistency) ← R-011 + R-012
- **R-026** (Dirac equation from KG factorization) ← R-013 + R-017 + R-012

### 1.5 Bell, Tsirelson, non-separability
- **R-167** (the Bell wing is the `e_4`-commutant qubit `Z_{Cl⁺(4,0)}(e_4) ≅ ℍ ≅ ℂ²`, not the `ℂ¹` phase sector; `span{1, B_a}` is the `ℂ`-linear Schur commutant of the one-sided `SU(2)`, so R-020 spends no uniqueness) ← R-020 + R-021 + R-011 + R-127 + R-160, **engine-exact**
- **R-027** (Tsirelson `S = 2√2`) ← R-011 + R-023 + R-167, **engine-exact**
- **R-028** (multipartite MK bound) ← R-027
- **R-029** (`ρ_A = (1/2)𝟙` identity) ← R-027

### 1.6 Electromagnetism
- **R-032** (Maxwell `∇F = J`) ← R-009
- **R-033** (no magnetic monopoles) ← R-032 (grade-3 part of ∇F vanishes)
- **R-034** (Coulomb potential) ← R-032 + 3D Green's function
- **R-035** (photon as L↔Q-bridging strain) ← R-032 + R-009

### 1.7 Matter, charges, generations (algebraic core)
- **R-052** (exactly two windings (B, L)) ← R-002 + Spin(4) factorization
- **R-056** (per-blade hypercharge) ← R-010 + `e_4`-bilinear
- **R-057** (fractional ±2/3, ±1/3) ← R-056 + R-053 (algebraic 3-quark structure)
- **R-062** (GMN `Q = T_3 + Y/2` as derived identity) ← R-056 + R-058
- **R-063** (charge quantization `|Q_p| = |Q_e|`) ← R-062, **cleanest spine result** (C-2 sweep 2026-07-31)
- **R-064** (Brannen amplitude form from V_4⊥ projection) ← R-009
- **R-065** (√2 factor forced by 3D projection) ← R-064
- **R-066** (Koide K=2/3 ⇔ c=√2 Brannen-Koide equivalence) ← R-064 + R-065
- **R-067** (Foot 45° characterization) ← R-066
- **R-087** (B − L anomaly cancellation from 3 × 1/3 = 1) ← R-057
- **R-088** (BPST + index ⇒ ΔB = ΔL = N_gen) ← R-087
- **R-097** + **R-098** + **R-099** (Cl-grade dictionary, as above)

### 1.8 Gauge group from D4 orbits
- **R-171** (the weak-`su(2)` menu is CLOSED at three conjugacy classes) ← R-009 + R-010 +
  **R-075** + **R-076** + R-099, **given premise A-P2** (weak isospin ⊂ grade-2 `so(4)`; FRAMING in
  the engine, **stamped ENDORSED — RUL-084**) + the right-handed-singlet datum. *(R-075 = the chirality↔Weyl-half identification;
  R-076 = the two-ideal Dirac occupancy that makes `W₋` non-empty. Both are inbound HERE and are
  NOT directly inbound to R-079 — the two edge sets are reconciled to exactly this form.)*
- **R-079** (weak = SD) ← **R-171** + R-078 — *the edge that carries the 2026-08-21 tier raise:
  R-079 was INPUT and is now DERIVED-given-{A-P2 + the datum}; R-075/R-076 are NO LONGER inbound
  edges of R-079* (they compute without it — the arrow runs substrate → neutrino, and the
  single-Weyl neutrino cannot discriminate SD from the L-orbit)
- **R-172** (WHICH SIDE the weak host acts on) ← **R-171** + R-167 (the `e₄`-commutant `ℍ`) +
  R-102/R-012 (the `S` carrier) + R-075 + R-076 + §B.1.3 (the lock generators, in the **banked
  grade-one realization** — the edge is realization-labelled because the counts depend on it) +
  §B.3.5 (the one-sided observer action), **given A-P2′-RIGHT** (RUL-091) + the carrier node
  (OPEN) + the right-handed-singlet datum. *Outbound:* R-079, R-078, R-060, R-061, R-062, R-077.
  *(This edge closes an ORPHAN: R-171's kernel numbers are taken LEFT-on-`S`, the ruled hosting is
  RIGHT-on-`Cl⁺`, and the transfer between them was asserted and computed nowhere until R-172(4).
  The `I₄`-grading ↔ observer-chirality bridge is an UNBUILT inbound condition, carried in the
  tier cell.)*
- **R-173** (no geometric ceiling on the Brannen amplitude; M-3-commitment-dominated) ← `canting_vacuum_branch_structure` (the banked `{J,D}` reduced energy + the branch pick) + `mass_equals_elastic_cost_premise` (which fixes the subtraction to the GLOBAL vacuum — the correction that made the axis cross-check work) + `generation_z3_is_metatime_phase` (the ℤ₃ is the CELL meta-time phase, so the step onto the GRAIN helix is the unbanked M-3 channel) + `brannen_z3_harmonic_collapse_invariant` (which is why the ‘Brannen form’ is content-free on a comb) + R-065/R-066 + N60. **Outbound: none by design** — it is a negative about FORCING, and the row exists to keep a false conditioning clause OUT of the Koide rows. *The inbound edge that decides it is not banked at all:* the **M-3 step-form**, whose two named readings give `1.216468` and `2.000000`; a fifth step-form row is named and unscanned.
- **R-174** (six-band magnon STIFFNESS spectrum) ← `canting_vacuum_branch_structure` + `n_goldstone_canted_FM` (whose `N_G = 2` is AXIS-scoped, which is what makes the branch label a correction) + `pi3_orientation_class_two_windings` (the six-parameter local state, i.e. why the so(4) basis is complete for the rotor field). *Outbound:* `induced_G_from_linear_face_band` — STEP 1's WP-LV1 LICENCE is upgraded to an exact operator identity, and the B1 annotation consumes `g`. **A NON-EDGE, stated because it looks like one:** this does NOT reach the two ‘exact 6-band Bogoliubov UN-BANKED’ IOUs — paraunitary (I-29) is a different operator (F2).
- **R-175** (KC-1, the one-way symmetry-class filter) ← `canting_vacuum_branch_structure` + R-174 (the same Bloch stiffness rig) + I-29 (the paraunitary class named as the one that CAN pass). *Outbound:* none banked — it constrains #1-gap kernel CANDIDATES, and its most consequential outbound is a **negative on TWT's own R-112 hyperbolic linear face**, which fails the filter identically (`Ω` absent, `ω² ∝ eig H`). **An UNBUILT inbound condition, carried in the tier cell:** the inversion operator `M` is not exhibited, so the real-class *assignment* is evidence, not theorem.
- **R-078** (substrate carriers of SM gauge content) ← R-009 + R-010, **weak slot given A-P2**
- **R-080** (U(1)_Y from I_4 + bivector compactness) ← R-056 + R-010
- **R-081** (colour octet 8 = 3 ⊕ 5 split; C_A/C_F = 9/4) ← R-053 + R-072
- **R-082** (`sin²θ_W = 3/8` at unification) ← R-056 + R-062 + R-079 + R-080 + R-009, **engine-exact identity — NOT a prediction of the measured angle** (the only computable descent misses by 33%, N55; exposure §E.3.5(5); marker added 2026-07-31)
- **R-083** (24-bond count; SU(5) labeling as translation only) ← A-1b

### 1.9 Cosmology / macroscopic limit kinematic results
- **R-029** + **R-044** + **R-046** + **R-048** + **R-049** + **R-050** — all kinematic
  consequences of Cl(4,0)'s structure plus A-3 (signature locking)

### 1.10 The medium's LOCAL STATE SPACE (R-102) and what consumes it

R-102 declares the medium's per-site state: a **4D orientation, six real parameters** — a unit
even element of `Cl⁺(4,0) ≅ ℍ⊕ℍ` — a GRAIN-layer statement inherited unchanged by the continuum
field through §D.4.1. It is the framework's most-consumed single quantity, and the edges below
were previously **absent from this graph in both directions**; their absence is why the
three-resolution drift at §D.3.2 / §D.4.3 / §B.6.5 went unseen. Each edge is named:

- **R-102** ← R-101, R-012 (D4 sites carry the spinor module the orientation acts on)
- **R-002** ← **R-102** — *because* `π_3` is a property of the field's TARGET, and the target is
  the local state space; six parameters chirally factorize (`so(4) = su(2) ⊕ su(2)`, computed at
  `pi3_orientation_class_two_windings`) into `ℤ × ℤ`, i.e. TWO windings. This edge is what
  discharges R-002's layer transport; it removes any dependency of the two-winding result on the
  unbuilt grain→cell map. **Cover-blind** — the count is the same on both branches of the open
  `ℤ₂` node (covering maps are isomorphisms on `π_n`, `n ≥ 2`).
- **R-036** ← **R-102** — *because* the local Lorentz frame is read off the orientation field
  directly (its six generators ARE `so(4)`), rather than assembled from a smaller object plus a
  canting direction and `e_4`. (R-036 also lists R-002 as a parent; the frame statement must
  therefore not be used as a source for R-002, which would be circular.)
- **R-041** ← **R-102** — *because* R-041's "six grade-2 fluctuation directions … on the
  homogeneous target" ARE the six parameters R-102 declares; the shift symmetry is a shift on
  that state space.
- **R-037 / R-163** ← **R-102** — *because* Sakharov's `N_eff = 6` is exactly `dim` of the local
  state space. This edge is the one that carries the numerical exposure: `N_eff` fixes
  `Λ_S = √(2π) M_Pl` and, through R-163's `c_lat`, `Λ_L = 1/a`, hence every dispersion consumer
  (E1 / N52 / the dim-6 LV coefficient). The value depends only on the DIMENSION, so it too is
  blind to the open `ℤ₂` branch.
- **R-108** ← **R-102** (SECTOR EDGE) — §D.4.3's `E(q)` single-`q` spiral minimisation is an
  L-orbit-sector reduction of the six-parameter state space, now stated as such in the paper.
  The 4D-bivector restatement over all six directions is owed.
- **`n_goldstone_canted_FM`** ← **R-102** (SECTOR EDGE) → `canting_critical_stiffness_at_DJ`
  → R-109 / `electron_QCP_nu`. The `N_G = 2` count holds **within the L-orbit sub-sector**; the
  full-state-space count would come from the un-banked 6-band Bogoliubov structure
  (`induced_G_from_linear_face_band`). Every result on this chain carries that named premise.

**Open at this node (recorded, not a gap in the above):** WHERE the `ℤ₂` sign lives —
sign-in-the-state (one-sided action) vs sign-in-the-emergent-covering-sector (`π₁(Q_N) = ℤ₂`,
§B.3.5) — is a deliberately unpicked branch in the family tree. No edge above depends on it.

---

## LAYER 2 — Dynamical consequences (gated on A-2)

Results whose existence is structural but whose **absolute magnitude or qualitative outcome**
depends on the substrate dynamics A-2. Each entry names what gates the open value.

### 2.1 Electroweak couplings (α, g and their siblings)
- **R-035a** (α as reactive L↔Q reconversion strength) — *ontology* DERIVED at Layer 1; the
  *magnitude* sits in Layer 2 gated on `Im χ` (the #1 gap). Engine: `alpha_em_value` raises.
- **R-035b** (g is α's algebraic sibling via `g² = 4πα · (8/3)` since `sin²θ_W = 3/8` proven) —
  DERIVED-A at Layer 1 once R-082 lands; given R-082 the EW sector reduces to ONE Layer-2
  magnitude (α), not two. Same `Im χ` samples α and g.
- **R-035c** (length ladder `r_e · a_0 = λ̄_C²`) — **definitional arithmetic**, not a Layer-1
  derivation and not a gated Layer-2 magnitude: `α` cancels identically because `r_e` and `λ̄_C`
  are *defined* through `α` and `a_0`. It is α-independent in the trivial sense of having no
  α-content at all. No engine primitive asserts it (paper-only, §B.5b.1).
- *Same single-dial logic ties α_s and α_W to α through `Im χ`*: §C.5 / §D.5 narrative. The
  framework's four SM EW couplings collapse to one Layer-2 magnitude.

### 2.2 Gravity
- **R-037** (Sakharov induced EH) — DERIVED-generic-given-4D, magnitude at `Λ_S = √(2π) M_Pl` (scheme), with `Λ_L = 1/a ∈ [0.39, 0.73] M_Pl` for dispersion consumers (which-Λ ruled 2026-07-30); absolute coefficient `Im χ`-gated. *(History: widened 2026-07-28 over an apparent three-way `c_reg` disagreement; RESOLVED 2026-07-29 — one `c_reg = 1/12` in three `Λ`-variables; the wide bracket is RETIRED by the ruling.)*
- **R-040** (induced G sign) — sign DERIVED via spin-2 spectral positivity (Layer-1 reasoning), magnitude #1-gap-gated
- **R-041** (ξ = 0 at leading order) — via Maurer–Cartan shift symmetry (engine tier: FRAMING+CONDITIONAL; Layer-1), residual ξ ~ (f_π/Λ)² ~ 10⁻⁴⁰-class (reading-immaterial) is dimension-6 gated
- **R-042** (texture tetrad) — structural geometry CLOSED conditional; absolute coefficient OPEN; 6→4 frame reduction BANKED structural (R-145, 2026-07-05 — residue: the signature pick + U2); Gauss-equation face EXECUTED (R-149, 2026-07-05 — Riem(g) algebraic in (E, Ω, dE), scaffold closed; C_T residue = the kernel's mode measure alone)

### 2.3 Strong sector
- **R-085** (no fundamental SU(3)_c; colour as elastic-response) — structural; β_3 sign LOCATED-GAP (named re-attack `beta3_sign_from_reflection_positivity`)
- **R-111** (1/Θ_0 ~ Λ_QCD) — CANDIDATE identification
- **R-118** (Θ_rel as highest-value target) — derived shared-condition; single-kernel-value gating four faces is CANDIDATE

### 2.4 Substrate dynamics core
- **R-113** / **R-114** / **R-115** (memory effect; memory REQUIREMENT — the "monostability theorem" wording withdrawn 2026-07-31, D-3: memoryless cannot supply `τ_mem ≫ τ_wave` for the selection roles, and the old no-stable-Skyrmion premise contradicted §A.3; rich/hysteretic ADOPTED as originator pick) — all FRAMING/CANDIDATE, #1-gap structure
- **R-116** (three roles of memory) — FRAMING + value-gated
- **R-117** (linear face structurally safe) — DERIVED-STRUCTURAL (this is why QM and Bell are unaffected by A-2 closure)

### 2.5 Cosmological constant
- **R-119** (Λ ~ H² residual) — driven-dissipative deviation from R-047 Volovik equilibrium; #1-gap-gated

### 2.6 Mass spectrum at value
- **R-051** (Skyrme `M_0 = 36.47 f_π/e`) — DERIVED at dressed-coupling
- **R-055** (L-orbit stiffness QCP scaling) — DERIVED-CONDITIONAL on four named identities; delivers `f_L`, NOT `m_e` (the conversion is excised); L2 mechanism unidentified
- **R-068** (three lepton mass ratios at δ_L = 12.73°) — FIT post WP-MASS-MEASURE (forward derivation REFUTED in V2 Phase F)
- **R-074** (cross-sector D/J agreement) — DERIVED-CALIBRATED, and CONDITIONED (two different functionals cohere; **not** an independent over-determination — see R-074's row and R-180/R-181)

### 2.7 Dark sector
- **R-121** (3 sterile RH neutrinos) — DERIVED
- **R-122** (sterile RH ~2% Ω_DM relic; ~98% out of V2 scope) — LOCATED-GAP

### 2.8 Lorentz violation — the isotropic dimension-six residual
- **R-165b** (the rotationally invariant dim-6 coefficient is protected by NEITHER R-016 nor the
  point group, and is #1-gap GATED) ← R-016 (scope: dim-4 boost only) + R-165a (scope: anisotropy
  only) + the §D.5 strain-mode dispersion. **The graph's only empirically-bounded gated node**:
  every other Layer-2 node is a value the gap fails to deliver; this one has a published ceiling
  it must fit under (VG-6, N52, boundary entry `E1`). Import edge: I-19, whose premise (e) makes
  the bound's *bindingness* conditional on the un-built outside↔inside projection.

---

## LAYER 3 — Structural deep gates

Decade-class open constructions. Each is its own structural decision.

### 3.1 Texture tetrad — gravity-as-dynamics on g_{μν}
The full nonlinear EH coefficient from the texture-tetrad construction. V2 Phase H closed the
structural geometry conditional on one premise (the gauge-projection postulate). What remains:
the absolute coefficient (requires the #1-gap nonlinear substrate propagator). The Layer-3
6→4 frame reduction is **banked at the structural level (R-145, 2026-07-05,
`texture_frame_6to4_reduction`)** — rank-4 (7,3) extended frame, signature menu with (4,0)
excluded, canonical selection-free tetrad up to O(1,3), Maurer–Cartan first-order scaffold,
compact internal gauge action; the residue is the SIGNATURE PICK (vacuum EOM) + the
gauge-projection premise (unchanged).

Engine: `texture_tetrad`, `texture_metric_candidate`, `texture_metric_diffinvariance`,
`texture_metric_tt_graviton`, `texture_metric_vierbein`, `texture_matter_gravity_coupling`,
`texture_frame_6to4_reduction` (R-145).
The first three raise; the latter four are structural reductions banked.

### 3.2 QCD UV gate — asymptotic freedom from marginal 4D-Skyrme sector
The emergent-antiscreening route is closed by a derived absence (paramagnetic spin contribution
requires a charged spin-1 field; TWT has none). The marginal-Skyrme route is genuinely open
but unmotivated. Located re-attack: `beta3_sign_from_reflection_positivity` flagged in V2 §25.1
"Located-gap with named re-attack handle".

Engine: `qcd_uv_conformal_phaseCD`, `qcd_collider_phenomenology` (raises).

### 3.3 Value gate — S coefficient (≡ Θ_rel via Im χ)
The framework's #1 gap. Closing this gives the entire pending-values registry's left column:
α_em, g, α_s, α_W, decoherence rate 1/T_2, Λ ~ H² residual, absolute mass scales, CKM hierarchy,
PMNS, neutrino masses, σ_QCD, τ_mem, Bell-pair memory — and the isotropic dimension-six LV
coefficient `η⁽⁴⁾` (R-165), which differs from every other item on the list in already having been
measured against. For that one the gate is not "we cannot compute it yet" but "we must compute it
and it must come out small": see `eom_constraint_class`'s `E1` entry and §E.3 VG-6.

Engine: `alpha_em_value`, `theta_rel_universality_located`, `theta_rel_pinnability_from_data`,
`theta_rel_equivariant_bifurcation_spine`, `theta_rel_rotating_wave_escape_located`,
`theta_rel_z3_isotropy_dichotomy` (the first raises; the rest are structural located-gap
banks).

---

## Concentration of the open frontier

Across ~26 open items, the concentration onto a small number of deep unconstructed objects
holds (preserved from V2 §25.1):

- **Structural gate 1: texture tetrad** (§3.1) — gravity-as-dynamics
- **Structural gate 2: QCD UV gate** (§3.2) — asymptotic freedom
- **Value gate: S coefficient ≡ Θ_rel via Im χ** (§3.3) — the #1 gap

V2's simplification from V1 (instead of "two structural gates + one value-fork", we have **one
value coefficient `S` to derive on the now-committed rich branch**, per W-LIVE-3) is preserved
in V3.

---

## Dependency edges flagged for closer audit (Phase α-7)

These edges are stated above but should be re-examined for hidden gaps:

- **R-070** δ_L from chiral-ℤ_3 potential: form is DERIVED but coefficient identification
  `A = J, B = D` is ASSERTED ANSATZ. The edge `A-1c → R-070` carries a hidden assumption.
- **R-165a** dimension-eight anisotropy: the edge carries premise **(P-an)**, analyticity of the
  dispersion kernel in `k`, and this is a *structurally unusual* hazard worth flagging — the node is
  placed in Layer 1 (pure invariant theory, no dynamics), but the object that would break its
  premise lives in Layer 2. A non-analytic driven-dissipative memory kernel — the #1 gap itself —
  escapes any polynomial-invariant argument. So a Layer-1 result is conditional on a Layer-2
  object, which is the reverse of the usual direction and should not be lost in a compression.
  Premise **(P-pg)** is the companion hazard: unequal weighting of triality-related shell-2 orbits
  restores dimension-six anisotropy (this is the *scalar-sector* breaker and remains correct).
  A third premise is implicit and now stated: **the kernel is a scalar in the internal index**
  (the theorem governs the polarization-averaged dispersion). Internal-index-carrying kernels are
  not covered and the point group cannot close them — the fully `W(F4)`-invariant pseudo-dipolar
  Γ direction already carries an anisotropic four-derivative polarization splitting; the Γ channel
  is invisible to the scalar sector at every order (traceless bond-by-bond), and its only dim-6
  reach is a polarization-splitting anisotropy gated on the dressed survivor coefficient
  (§D.5.7 assembly record, #1-gap-routed).
- **R-082** `sin²θ_W = 3/8`: depends on R-080 (U(1)_Y from I_4 + bivector compactness). R-080
  itself depends on the gauge-boson-as-bivector-strain ontology — that ontology is FRAMING and
  is what R-080's "DERIVED" really means. The edge should be explicit.
- **R-068** three lepton mass ratios: depends on `mass_measure_from_omega` which tiers as
  CANDIDATE-strong (post WP-MASS-MEASURE). The edge `R-066 + R-064 → R-068` carries the
  Phase-F-REFUTED dependency. Result Index notes this; the dependency graph should too.
- **R-025** Spin(4) half-angle spin-statistics: SELECTION, not forced in bare SU(2). Three
  closure routes (W1 colour-sector ℤ_3 holonomy, W2 — §D.5 (V2 §9.6) driven dynamics induces τ_5 flow,
  W3 V2 §3.2 refinement) are flagged as Paper-2 work in the engine
  `skyrmion_collective_quantization_under_v2_3p2`.
- **R-053** baryon as one defect with three facets — DERIVED-STRUCTURAL but the *substrate
  dynamics* picking out exactly three facets reads as derived only at the static-algebra level;
  the dynamical selection is gated on A-2.

---

## Maintenance protocol

When a new result is banked or an existing result's tier changes:

1. Update its row in Section 1 (Result Index) (tier, engine, notes).
2. Update its position in this file's Layer 0 / 1 / 2 / 3 stratification.
3. Update edges: re-check that all `Deps` and `Used by` references are consistent.
4. If the change moves a result between layers (e.g., a Layer-2 result becomes Layer-1 because
   the closure landed), record it in `Annex N.G — Development log` in the paper.

---

# Section 3 — Engine ↔ Paper Map

*Which engine primitive — MAIN `twt.py` or COMPANION `twt_companion.py` — is the witness for which §; which harness check (`twt_test.py` or `twt_companion_test.py`) verifies which result.*


*Version 3 · Phase α draft · 2026-06-30.*
*Cross-reference between `twt.py` engine primitives, `twt_test.py` checks, and V3 paper sections.
For every engine primitive: which §/R-NNN cites it, and which test (if any) verifies it.
For every V3 §: which engine primitives carry its claims.*

---

## How to read this file

Two views of the same content:

- **View A — engine-keyed.** Every engine primitive — MAIN `twt.py` or COMPANION
  `twt_companion.py` — listed alphabetically, with the V3 § that cites it (via R-NNN) and the
  harness line (`twt_test.py` or `twt_companion_test.py`) that verifies it.
- **View B — section-keyed.** Each V3 § with its engine primitives, organized by R-NNN
  appearance order.

Phase α-7 audit task: verify that every R-NNN engine cite in Section 1 (Result Index) is
either (a) listed in View A here, or (b) a primitive that exists in `twt.py` and gets added to
View A. No phantom cites (CLAUDE.md §2).

---

## View A — engine-keyed (primitive → V3 §, R-NNN, test)

*Total primitives in the engine: 387 as of 2026-08-23 (FOUR files since the 2026-08-23 family split — the MAIN engine is `twt.py`, a pure import FACADE defining nothing, over two halves: `twt_core.py` CORE (family-level) and `twt_candidate_v3.py` CANDIDATE (V3-instance). MAIN: 310 module-level defs = 271 public + 29 helpers prefixed `_` + 10 classes, split 202 CORE (171 public + 21 helpers + 10 classes) + 108 CANDIDATE (100 public + 8 helpers); `twt_companion.py` COMPANION: 77 defs = 64 public + 13 helpers, carrying the same cut as an in-file SECTION split — 29 defs in SECTION CORE (21 public) and 48 in SECTION CANDIDATE (43 public). The split MOVED code and rewrote nothing: the only non-move edits are the two the ruling mandated — the `CORE_PROVENANCE` registry and R-161's witness split. Re-counted by AST 2026-08-23, not incremented. Refresh this count+date at each banking pass, and count rather than increment). The table below lists the
258 load-bearing-primitive rows (re-counted 2026-08-23, not incremented; 258 distinct primitives —
the second, byte-identical `B_minus_L_anomaly` row was removed at the 2026-08-18 archivist
pass, so rows and primitives agree; `weak_su2_menu_exhaustion`, `charge_assignment_from_anchor` and `charge_sector_provenance` added 2026-08-21; `weak_host_must_be_body_frame` and `lock_left_centralizer_is_u1` added 2026-08-23 (R-172); `brannen_comb_commitment_dominance_and_dof_vacuity`, `magnon_stiffness_bands_canted_vacuum` and `spectral_branch_symmetry_class_filter` added 2026-08-23 (the estate of N64, R-173/R-174/R-175); `spinor_module_graded_iso` added 2026-08-23 (R-182, the V4-ASD Layer-A round's only bankable result); and the six-primitive Γ-channel referent closure `bond_invariant_menu_frame_bilinear`, `bond_channel_parity_exclusivity`, `bond_harmonic_ceiling_by_generator_class`, `gamma_survivor_pitch_genericity`, `DoverJ_calibration_referent`, `gamma_admixture_cross_functional_route` added 2026-08-23 (R-176…R-181)) that V3 R-NNNs cite
directly, plus primitives the V3 body names directly without an R-NNN, plus body-cited ledger primitives
carrying an I-series row instead of an R-NNN. Helpers and not-cited primitives are
listed in §View A.Δ at the bottom for completeness.*

| Primitive | V3 § | R-NNN | Test |
|---|---|---|---|
| born_exponent_gleason_closure | B.3.3 | R-160 | twt_test.py |
| charge_normalization_anchor_free | C.2.7, C.2.8 | R-159 | twt_test.py |
| coupling_sector_channel_disjointness | B.5b.3 | R-162 | twt_test.py |
| D4_DM_bond_bivectors_non_commuting | C.4, D.3 | R-083, R-104 | twt_test.py |
| D4_spatial_bond_isotropy | C.4, D.3 | R-083, R-103, R-104 | twt_test.py |
| DM_operator_gaussian_dim | D.4 | R-110 | twt_test.py |
| D_crit_over_J | C.3 | R-069 | twt_test.py |
| DoverJ_from_lepton_masses | C.3, D.3 | R-068, R-074, R-103 | twt_test.py |
| DoverJ_from_skyrme | C.3 | R-074 | twt_test.py |
| G_cycles_generations | C.3 | R-072 | twt_test.py |
| d4_lattice_lorentz_violation_orders | B.1.5, B.6.3, B.6.4, E.3.3 VG-6, E.3.5(4) | R-165 | twt_test.py |
| G_generator | C.3 | R-072 | twt_test.py |
| I4_maps_L_to_Q | A.3, A.5, C.5 | R-005, R-010, R-090 | twt_test.py |
| I4_squared | A.5, C.4 | R-010, R-080 | twt_test.py |
| induced_G_from_linear_face_band | B.6.2 | R-163 | twt_test.py |
| Kc_magnon_stiffness_canted_FM_at_DJ | D.4 | R-108 | twt_test.py |
| L_Q_orthogonal_decomposition | A.5, B.8, C.4, D.2 | R-009, R-049, R-078, R-097 | twt_test.py |
| L_algebra_su2_closure | D.2 | R-097 | twt_test.py |
| alpha_em_meaning | B.5b | R-035a | twt_test.py |
| alpha_em_value | B.5b, D.5 | R-035a (raises until #1-gap closes) | twt_test.py expects raise |
| alpha_H_gap | C.5 | R-091a | twt_test.py |
| anti_self_dual | D.2 | R-098, R-099 | twt_test.py |
| B_minus_L_anomaly | C.5 | R-087, R-089 | twt_test.py |
| baryon_mass_shared_rotor_nonadditive | C.1 | R-053 | twt_test.py |
| bell_correlation | B.4 | R-027 | twt_test.py |
| bell_wing_needs_the_e4_commutant_qubit | B.3.1, B.4 | R-167 | twt_test.py (check_twt_spectra) |
| beta3_sign_from_reflection_positivity | E.2, Layer-3 | (located re-attack) | twt_test.py (located-gap bank) |
| bivector_inner_product | A.5 (background) | (kinematic) | twt_test.py |
| born_subspace_one_B_forced | B.3 | R-020, R-021 | twt_test.py |
| boost | B.2 | R-018 | twt_test.py |
| bpst_charge_Q | C.5 | R-088 | twt_test.py |
| bpst_selection_rule | C.5 | R-088, R-089 | twt_test.py |
| brannen_amplitude | C.3 | R-064, R-068 | twt_test.py |
| brannen_z3_harmonic_collapse_invariant | C.3.10 | R-170 (ψ-repair: collapse identity, ψ mass-gauge, model-free invariant ψ_inv, ε-convention scoping, N60 cap) | twt_test.py |
| c_reg_from_substrate_mode_content | B.6.2 | R-037, R-163 (no own Result-Index row yet — owed) | twt_test.py |
| cabibbo_angle_rad | C.3 | (deprecated — returns δ_L, not a Cabibbo angle; removed from R-073's cites 2026-07-02) | twt_companion_test.py |
| cabibbo_transition_probability | C.3 | R-073 | twt_test.py |
| canting_cos_q | D.4 | R-108 | twt_test.py |
| canting_critical_stiffness_at_DJ | D.4 | R-108 | twt_test.py |
| canting_pitch_q_rad | D.4 | R-108 | twt_test.py |
| chiral_split_demo | D.2 | R-098, R-099 | twt_test.py |
| chirality_does_not_source_P | C.5 | R-086 | twt_test.py |
| chirality_is_a_reflection | C.5 | R-086 | twt_test.py |
| chsh_S | B.4 | R-027 | twt_test.py |
| cl_dimension | B.1, D.1 | R-014, R-092 | twt_test.py |
| cl40_quaternion_triple | D.1, D.2 | R-092, R-093 | twt_test.py |
| cl40_vs_cl41 | D.1 | R-092, R-093 | twt_test.py |
| cl41_grounding_litmus | D.1 | R-094 | twt_test.py |
| cl41_idempotents_note | D.1, D.2 | R-094, R-095 | twt_test.py |
| cl41_phase_is_external_u1 | D.1, D.2 | R-094, R-095 | twt_test.py |
| cogear_linkage_kinematic | C.1 | R-053 | twt_test.py |
| colour_SO3_re_realization_forbidden | C.4, C.5 | R-081, R-085 | twt_test.py |
| colour_abare_static_holomorphic | D.5 | R-118 | twt_test.py |
| colour_arich_kernel_dependent | D.5 | R-118 | twt_test.py |
| colour_quartic_charge_handle | C.4, D.5 | R-081, R-118 | twt_test.py |
| colour_relative_phase_is_coset | C.4, D.5 | R-081, R-118 | twt_test.py |
| colour_sector_E_hermitian_form | C.4 | R-081 | twt_test.py |
| colour_su3_located_gap | C.4 | R-081 | twt_test.py |
| colour_z3_holonomy_cannot_source_fr_sign | B.3.5 | R-025 (W1 reduction, N35) | twt_test.py |
| coulomb_is_harmonic | B.5 | R-034 | twt_test.py |
| coulomb_potential | B.5 | R-034 | twt_test.py |
| coulomb_sign_rule | B.5 | R-034 | twt_test.py |
| charged_defect_worldline_eom_cyclotron | B.5.5 | R-124 | twt_test.py |
| defect_phase_collective_mode_at_k4 | D.4.6 | R-125 | twt_test.py |
| defect_zero_mode_multiplet_labels | D.4.6 | R-126 | twt_test.py |
| front_phase_handoff_selects_winding_axis | B.3.1 | R-127 | twt_test.py |
| lock_channel_is_axial_chiral_channel_p1b_split | B.3.5, C.4.6 | R-161 | twt_test.py |
| qorbit_mass_phase_dual_lock_parity_odd | B.3.1 | R-128 | twt_test.py |
| i4_condensate_ideal_channel_rule | B.3.1 (N38) | R-129 | twt_test.py |
| phase_mode_excess_inherits_defect_localization | D.4.6 | R-130 | twt_test.py |
| corotating_stability_fixed_charge_hessian | D.4.6 | R-142 (A6, N45 refine) | twt_test.py |
| defect_phase_modulus_charge_tower_spacing | D.4.6 | R-131 | twt_test.py |
| boost_orbit_rest_label_mass_shell | B.2.2 | R-132 | twt_test.py |
| skyrme_quartic_contains_no_tree_EH | B.6.6 | R-164 | twt_test.py |
| skyrmion_rotational_band_nucleon_delta | C.1.2 (D.4.5) | R-133 | twt_test.py |
| brannen_scale_nucleon_third_convergence | C.3.11 | R-134 | twt_test.py |
| multi_skyrmion_b2_classical_binding | C.1.2 (E.3 SC-1) | R-135 | twt_test.py |
| b2_axial_quantization_deuteron_ground_state | C.1.2 (B.3.5) | R-136 | twt_test.py |
| massive_pion_bvp_binding_margin_robust | C.1.2 | R-137 | twt_test.py |
| massive_scheme_refit_branch | C.1.2 | R-138 | twt_test.py |
| two_defect_asymptotic_tensor_force | C.1.2 | R-139 | twt_test.py |
| d4_dm_plaquette_holonomy_explicit | C.4.6 | R-140 | twt_test.py |
| induced_level_parity_on_baryon_worldline | C.4.6 (B.3.5) | R-141 | twt_test.py |
| one_particle_pole_moduli_identification | D.4.6 (B.2.1) | R-142 | twt_test.py |
| d4_lattice_instanton_access_and_dm_background_neutrality | C.4.6(iv) | R-143 | twt_test.py |
| full_field_b2_below_threshold_sc1_datum | C.1.2 (E.1.2/E.3) | R-144 | twt_test.py |
| texture_frame_6to4_reduction | B.6.6–B.6.7 | R-145 | twt_test.py |
| texture_gauss_equation_riemann_closure | B.6.6–B.6.7 | R-149 | twt_test.py |
| ct_kernel_moment_count_symmetry_reduction | B.6.7 | R-151 | twt_test.py (check_twt_cosmo) |
| kernel_overdetermination_table | E.5 (via R-157; companion §4/§12) | R-150, R-157 | twt_test.py (check_twt_algebra) |
| kernel_candidate_constraints | E.5 (via R-156; companion §12; candidates/2026-07-05_phaseB memo) | R-156 | twt_test.py (check_twt_algebra) |
| single_relaxation_family_exclusion_probe | — (Phase B/B2; candidates/2026-07-05_phaseB memo) | (Phase B) | twt_companion_test.py (check_twt_algebra) |
| d4_langevin_calibration_gate | — (Phase B/B3; candidates/2026-07-05_phaseB memo) | (Phase B) | twt_companion_test.py (check_twt_algebra) |
| static_susceptibility_sumrule_and_kss_channel_mismatch | — (ledger N43; companion §4) | N43 | twt_companion_test.py (check_twt_algebra) |
| stress_tensor_shear_channel_static_moment | — (ledger N47; companion §12 ceiling) | N47 (A3) | twt_companion_test.py (check_twt_algebra) |
| dm_differential_coupling_no_em_dark_texture | E.1.3 | R-146 | twt_test.py |
| dm_wavetrain_phase_defect_negative | E.1.3 | R-147 | twt_test.py |
| marginal_skyrme_beta3_sign_dispersive | C.5.2 | R-148 | twt_test.py |
| defect_rotor_frequency_reads_as_k4_on_front | B.2.1 | R-123 | twt_test.py |
| delta_L_from_DoverJ | C.3 | R-068, R-069, R-070 | twt_test.py |
| dft_K_from_r | C.3 | R-065, R-066 | twt_test.py |
| dirac_ideal_idempotent | B.3, D.2 | R-025, R-026, R-095, R-096 | twt_test.py |
| doublet_hypercharge | C.2 | R-056, R-058 | twt_test.py |
| dressed_coupling | C.3, D.3, D.4 | R-074, R-103, R-107 | twt_test.py |
| duality_map | A.5, D.2 | R-010, R-099 | twt_test.py |
| e_i4_squares_to_minus_one | B.8.1 | — (named directly in the body; no R-NNN) | twt_test.py |
| e4_content_confines_quarks_not_leptons | C.1, C.5 | R-053, R-084 | twt_test.py |
| electron_QCP_nu | C.1 | R-055 | twt_test.py |
| electron_f_L_MeV | C.1 | R-055 | twt_test.py |
| electron_two_windings | C.1 | R-055 | twt_test.py |
| eom_compatible_field_forks | D.5 | R-113, R-114, R-115 | twt_test.py |
| eom_constraint_class | D.4 | R-112 | twt_test.py |
| eom_invariant_variant_audit | D.5 | R-113, R-117 | twt_test.py |
| equivalence_principle_protection | B.1, B.6 | R-016, R-039 | twt_test.py |
| eta_DM | C.5 | R-086 | twt_test.py |
| exp_unit_bivector | A.5 | R-011 | twt_test.py |
| f_pi_squared | D.4 | R-106 | twt_test.py |
| foot_angle_deg | C.3 | R-067 | twt_test.py |
| forced_handedness | C.3 | R-075 | twt_test.py |
| gamma0_gammaj_reduces_to_ej | B.1 | R-013 | twt_test.py |
| gammas | B.1 | R-013, R-015 | twt_test.py |
| generation_spectrum | C.2 | R-062, R-063 | twt_test.py |
| generation_z3_is_metatime_phase | C.3 | R-072 | twt_test.py |
| generations_dynamical_count_structural | C.3 | R-071 | twt_test.py |
| gluon_octet_symmetric_space_split | C.4, C.5 | R-081, R-085 | twt_test.py |
| gmn_coefficient | C.2 | R-057, R-062, R-063 | twt_test.py |
| gravitating_vacuum_energy | B.7, E.1 | R-047, R-119 | twt_test.py |
| half_angle_overlap | A.5, B.4 | R-011, R-027 | twt_test.py |
| hestenes_Isigma3 | B.3 | R-026 | twt_test.py |
| hierarchy_type | C.3 | R-068 | twt_test.py |
| hodge_star | A.5 | R-010 | twt_test.py |
| hypercharge | C.2, C.4 | R-056, R-080 | twt_test.py |
| identify_the_floor | D.5 | R-116, R-117 | twt_test.py |
| im_chi_falsifier_budget_KSS_GW_macromolecule | B.4, D.5 | R-030, R-116 | twt_test.py |
| induced_G_bracket_mode_count | B.6 | R-037 | twt_test.py |
| induced_G_leading_coefficient_mass_independent | B.6 | R-037 | twt_test.py |
| induced_G_only_monad_scale_enters | B.6 | R-037 | twt_test.py |
| induced_G_quadratic_divergence_from_4D | B.6 | R-037 | twt_test.py |
| induced_G_sign_cross_check | B.6 | R-040 | twt_test.py |
| interference_can_reduce_mass_goldstone | D.5 | R-117 | twt_test.py |
| is_L_bivector | A.5 | R-009 | twt_test.py |
| is_Q_bivector | A.5 | R-009 | twt_test.py |
| is_idempotent | A.5 | R-012 | twt_test.py |
| kappa_F_bare | D.4 | R-107 | twt_test.py |
| kernel_candidate_dials | E.5 | R-155 | twt_test.py |
| kernel_candidate_falsifiers | E.5 | R-158 | twt_test.py |
| kernel_candidate_form | E.5 | R-153 | twt_test.py |
| kernel_composite_closure | E.5 | R-154 | twt_test.py |
| koide_K | C.3 | R-064, R-066 | twt_test.py |
| koide_charge_unification | C.3 | R-066 | twt_test.py |
| koide_from_c | C.3 | R-064, R-066 | twt_test.py |
| koide_modus_tollens_consistency | C.3.9 (via §E.3 RF-3) | — (named directly in the body; no R-NNN) | twt_test.py |
| lambda_H2_dynamical_reading_excluded | E.1 | R-119 | twt_test.py |
| lambda_resolution_structure | B.7, E.1 | R-047, R-119 | twt_test.py |
| lepton_number_topological_conservation | C.1, C.5 | R-054, R-089, R-090 | twt_test.py |
| macroscopic_LQ_split | B.8 | R-048, R-049 | twt_test.py |
| mass_measure_from_omega | C.3 | R-068 (Brannen δ_L chain; CANDIDATE-strong) | twt_test.py |
| mass_weight_empirical_chain | B.6 (intro block) | — (jurisdiction ledger; import I-23 — never an R-NNN) | twt_test.py |
| massless_H_squared | D.5 | R-117 | twt_test.py |
| matter_stability_outside_frame | A.2, A.3, B.1 | R-003, R-004, R-016 | twt_test.py |
| maxwell_four_laws | B.5 | R-032 | twt_test.py |
| maxwell_grade_structure | B.5 | R-032, R-033 | twt_test.py |
| mermin_klyshko_value | B.4 | R-028 | twt_test.py |
| mermin_value | B.4 | R-028 | twt_test.py |
| n_goldstone_canted_FM | D.4 | R-108 | twt_test.py |
| neutrino_lightness | C.3 | R-076 | twt_test.py |
| neutrino_orbit_asymmetry_attempt | C.3.12 (via §E.3 RF-6) | — (named directly in the body; no R-NNN) | twt_test.py |
| nonuniform_orbit_baryon_model | C.1 | R-053 | twt_test.py |
| nuclear_length_hierarchy | C.5, D.4 | R-091b, R-111 | twt_test.py |
| over_determination_scan | C.3 | R-074 | twt_test.py |
| photon_strain_mode | B.5 | R-035 | twt_test.py |
| phase_to_h_unit_map_located_residual | C.3 | R-071 | twt_test.py |
| pi3_S3_integer_completion | A.2, A.3, C.1, C.5 | R-002 (lepton-sector π_3(S³)=ℤ + baryon integer completion only — NOT the ℤ×ℤ), R-006, R-052 (same scope: the per-sector degrees only — the ℤ×ℤ half of R-052 is `pi3_orientation_class_two_windings`), R-054, R-084, R-089 | twt_test.py |
| pi3_orientation_class_two_windings | A.2, C.1, D.3 | R-002 (the ℤ×ℤ), R-052 (the ℤ×ℤ its headline claims), R-102 | twt_test.py |
| pmns_no_substrate_derivation | C.3.12 (via §E.3 RF-5) | — (named directly in the body; no R-NNN) | twt_test.py |
| polar_moment_of_inertia | B.8 | R-048 | twt_test.py |
| protection_mechanism_located | D.5 | R-117 | twt_test.py |
| qcd_collider_phenomenology | E.2 | (raises, gated; Layer-3 deep gate) | twt_test.py expects raise |
| qcd_uv_conformal_phaseCD | D.4 | R-111 | twt_test.py |
| quark_brannen_table | C.3 | R-073 | twt_test.py |
| quark_mass_reconstruction | C.3 | R-073 | twt_test.py |
| rotation | B.2 | R-018 | twt_test.py |
| s0 | A.5, D.3 | R-012, R-102 | twt_test.py |
| sakharov_induced_gravity | B.6 | R-037 | twt_test.py |
| sakharov_xi_minimal_coupling | B.6 | R-041 | twt_test.py |
| self_adjointness_from_one_B_projection | B.3.2 | R-022, R-166 | twt_test.py (check_twt_spectra) |
| self_dual | D.2 | R-098, R-099 | twt_test.py |
| self_dual_blade | D.2 | R-098 | twt_test.py |
| sigma_model_kinetic_normalization | D.4 | R-106, R-109 | twt_test.py |
| single_quark_no_rest_mass_axis | A.4 | R-008 | twt_test.py |
| skyrme_BVP_audit | C.1, D.4 | R-051, R-109 | twt_test.py |
| skyrme_length_fm | C.1 | R-051 | twt_test.py |
| skyrmion_collective_quantization_under_v2_3p2 | B.3 | R-025 | twt_test.py (located-gap bank) |
| skyrmion_mass_MeV | C.1 | R-051 | twt_test.py |
| so13_closure_signs | B.2 | R-018 | twt_test.py |
| spatial_vs_phase_partition | C.4, D.2 | R-078, R-100 | twt_test.py |
| spin4_generator_count | D.2 | R-098, R-100 | twt_test.py |
| spinor_real_dof | A.5, D.2, D.3 | R-012, R-096, R-102 | twt_test.py |
| spiral_angle_deg | D.4 | R-107 | twt_test.py |
| sterile_rh_relic_check | E.1 | R-121, R-122 | twt_test.py |
| sterile_rh_substrate_production_via_L_theta | E.1 | R-122 | twt_test.py (located-gap bank) |
| sterile_rh_z2_separate_mass_scale_check | E.1 | R-122 | twt_test.py (located-gap bank) |
| texture_matter_gravity_coupling | B.6 | R-042 | twt_test.py |
| texture_metric_candidate | B.6 | R-042 | twt_test.py |
| texture_metric_diffinvariance | B.6 | R-042 | twt_test.py |
| texture_metric_tt_graviton | B.6 | R-042 | twt_test.py |
| texture_metric_vierbein | B.6 | R-042 | twt_test.py |
| texture_tetrad | B.6 | R-042 (raises until coefficient closes) | twt_test.py expects raise |
| theta_rel_equivariant_bifurcation_spine | D.5 | R-118 | twt_test.py |
| theta_rel_fork_escape_kernel_number_governed | D.5 | R-118 (N46, W3.3/A1) | twt_test.py |
| theta_rel_pinnability_from_data | D.5 | R-118 | twt_test.py |
| theta_rel_rotating_wave_escape_located | D.5 | R-118 | twt_test.py |
| theta_rel_universality_located | D.5 | R-118 | twt_test.py |
| theta_rel_z3_isotropy_dichotomy | D.5 | R-118 | twt_test.py |
| thomas_KK | B.2 | R-019 | twt_test.py |
| top_excluded | C.5, E.3 row 12 | R-091a | twt_test.py |
| topological_overproduction_test | C.5, E.3 RF-7 | R-091 | twt_test.py |
| triple_product_Q | C.2, D.2 | R-057, R-097 | twt_test.py |
| triple_product_color | C.2, D.2 | R-057, R-097 | twt_test.py |
| tsirelson_S | B.4 | R-027 | twt_test.py |
| universality_theorem | C.2 | R-059 | twt_test.py |
| updown_mass_operators_commute | C.3 | R-077 | twt_test.py |
| updown_mirror_value_three_handles | C.3 | R-077 | twt_test.py |
| updown_seat_rhoL_parity_odd_hodge_form | C.3.13 | R-152 (W3.2/A2) | twt_test.py |
| vminusa_is_spin4_factor_chirality | C.2, C.4 | R-060, R-079 | twt_test.py |
| w_state_located_gap | B.4 (scope note) | R-028 (located-gap remark) | twt_test.py (located-gap bank) |
| wave_E5 | D.1, D.2, D.4, C.5 | R-007, R-100, R-112 (R-091 cite struck 2026-07-31, C-3) | twt_test.py |
| wave_E_complex_structure | A.4, D.2, D.4, C.5 | R-007, R-100, R-112 (R-091 cite struck 2026-07-31, C-3) | twt_test.py |
| brannen_comb_commitment_dominance_and_dof_vacuity | C.3, D.4.3 | R-173 | twt_test.py |
| magnon_stiffness_bands_canted_vacuum | D.4.3, B.6.2 | R-174 | twt_test.py |
| spectral_branch_symmetry_class_filter | D.5 | R-175 | twt_test.py |
| weak_host_must_be_body_frame | C.4 | R-172, R-079 | twt_test.py |
| spinor_module_graded_iso | A.5, B.3, C.3.12, D.2 | R-182, R-076, R-172 | twt_test.py |
| bond_invariant_menu_frame_bilinear | C.3, D.3, D.4 | R-176 | twt_test.py |
| bond_channel_parity_exclusivity | C.3, D.4 | R-177 | twt_test.py |
| bond_harmonic_ceiling_by_generator_class | C.3, D.5.7 | R-178 | twt_test.py |
| gamma_survivor_pitch_genericity | D.4, D.5 | R-179 | twt_test.py |
| DoverJ_calibration_referent | C.3.5, C.3.7, C.3.11, D.3.3 | R-180, R-074 | twt_test.py |
| gamma_admixture_cross_functional_route | D.5.7, C.3.11 | R-181, R-106 | twt_test.py |
| weak_su2_menu_exhaustion | C.4 | R-171, R-079, R-078, R-172 | twt_test.py |
| weak_isospin_SD_parity_exclusion | C.2, C.4 | R-060, R-079 | twt_test.py |
| weak_isospin_centralizer_is_SD | C.2, C.4 | R-061, R-079 | twt_test.py |
| lock_left_centralizer_is_u1 | C.4, B.1 | R-172 (and the ground RUL-091 cited before it was banked) | twt_test.py |
| weak_isospin_rank_table | C.4 | R-079 | twt_test.py |
| weak_isospin_verdict | C.4 | R-079 | twt_test.py |
| weak_isospin_zero_on_generations | C.2 | R-061 | twt_test.py |
| weinberg_sin2 | C.4, B.5b | R-082, R-035b | twt_test.py (load-bearing test, engine-exact 3/8) |
| why_three_generation_triple | C.3 | R-071 | twt_test.py |
| charge_assignment_from_anchor | C.2 | R-056, R-063, R-080 | twt_test.py (the renamed body of `winding_charge`: anchor + composition solve, ASSIGNED side of the §2a boundary) |
| charge_sector_provenance | C.2 | R-063, R-159 | twt_test.py (the anchor-free/assigned boundary, machine-readable; the harness fails on an unclassified charge-block primitive) |
| winding_charge | C.2, C.4 | R-056, R-063, R-080 | twt_test.py (LEGACY ALIAS of `charge_assignment_from_anchor`; the name is a misnomer — no winding is computed) |
| worldline_bivector | B.8 | R-048 | twt_test.py |
| x_Q | C.5 | R-091a | twt_test.py |
| winding_sense_sets_mass_measure | — (companion engine `twt_companion.py`; pre-split orphan; row added at the 2026-08-13 sweep; no paper cite) | [DERIVED (winding sense) + FRAMING (the measure consequence)] | twt_companion_test.py (check_twt_matter) |
| conjugating_extension_omega_identities | — (companion engine `twt_companion.py`; banked 2026-08-12 from ADJUDICATION_2026-08-03) | [DERIVED-A] | twt_companion_test.py (check_twt_cosmo) |
| alpha_family_parallelogram_law | — (companion engine `twt_companion.py`; banked 2026-08-12 from ADJUDICATION_2026-08-03) | [DERIVED-A] | twt_companion_test.py (check_twt_cosmo) |
| ecarrier_matched_defect_hblock_null | — (companion engine `twt_companion.py`; banked 2026-08-12 from ADJUDICATION_2026-08-03) | [DERIVED-A] | twt_companion_test.py (check_twt_cosmo) |
| lambda_perp_anw_half_theta | — (companion engine `twt_companion.py`; banked 2026-08-12 from ADJUDICATION2_2026-08-03) | [DERIVED-A given the frozen-profile (rigid-rotor) ansatz] | twt_companion_test.py (check_twt_hadrons) |

### View A.Δ — primitives not cited by any V3 R-NNN

The following 85 entries (counted 2026-08-18, not incremented) exist in the engine (`twt.py` or
`twt_companion.py`) but are not directly cited by an R-NNN in V3. Primitives that the V3 body
names directly without an R-NNN are listed in View A above, not here.
Most are (a) helpers (prefixed `_`), (b) historical / V1-era constructions superseded by V2,
(c) re-attack-handle banks for located gaps that the V3 text references narratively rather than
by R-NNN, or (d) primitives whose role is sub-primitive to a V3 R-NNN.

Phase α-7 will audit each: does the primitive cover content that V3 should reference? If yes,
add an R-NNN; if no, it stays in this Δ list as engine-internal infrastructure.

`_E_W_qm`, `_F`, `_Mcirc`, `_R_axis`, `_Wembeddings`, `_Wgenspaces`, `_Wrank`, `_adV`,
`_axis_rotation`, `_biv`, `_blade_mul`, `_cl40`, `_eigenvalue`, `_genV`, `_ip`,
`_metatime_sqrt_m`, `_mixing`, `_nrm`, `_orbit_vectors`, `_rand_colour_state`, `_spans_both`,
`_sqrt_m`, `_sqrt_masses`,
`amplitude_to_operator`, `anomaly`, `baryon_rank2_mode_cross_sector`,
`blade_amplitude_extract`, `bu_offset_not_charge_sourced`, `cabibbo_vector_vs_spinor`,
`cand1_24cell_ratio_computed`, `charge_in_the_window_picture`, `ckm_arc_*`, `ckm_frame_fit_is_vacuous`,
`ckm_from_mass_pinned_psi`, `ckm_from_metatime_operator`, `ckm_from_triplet_overlap`,
`ckm_hierarchy_and_cp_seed`, `ckm_metatime_status`,
`closure_report`, `comm`, `compact_spin4_favors_limit_cycle`, `cp_chirality_90_120_mismatch`,
`deferent_from_offset_lepton_consistent`, `dip_planes_multiaxis_but_uniform_is_single_axis`,
`e`, `e4_acts_as_identity_on_Splus`, `e4_conjugation_is_LQ_not_updown`,
`epicycle_reading_dependent`, `epicycle_reading_resolved`,
`gate_B_branch`, `gear_eigenvalues`, `gear_inertia_form_from_S2_symmetry`, `gell_mann_okubo_gamma`,
`generation_cost_step_structure`, `generation_gen2_chirality_mirror`,
`generation_index_survives_brannen_excision`, `generation_ladder_needs_inverse_square`,
`generation_loose_windows_vacuum_relative`, `generation_subharmonic_ladder`,
`generation_values_monad_forked`, `generations_are_defect_flows_on_spinor_S3`,
`geometric_ladder_is_nonselfadjoint`,
`heavy_baryon_predictions`, `hodge_split_invariance_theorem`,
`i4_generation_overdetermination`, `i4_lepton_quark_amplitude_blind`,
`induced_G_gate_A_linearized_sufficient`, `induced_G_knowability_verdict`,
`mass_operator_form`, `mass_reconciliation_U1_Spin3`,
`meson_dynamical_current_split`, `meson_topological_status`,
`metatime_brannen_vs_v4perp_projection_reach`, `metatime_generation_operator`,
`numerical_chain`,
`phase_D_colour_updown_blind`, `pure_L_rotor_preserves_spatial_radius`,
`q_l_stiffness_ratio_is_gap_gated`, `quark_regimes`, `same_composition_baryons_pin_internal_mode`,
`subharmonic_transition_cost`, `su6_pairs_are_rotor_orientation`,
`updown_mass_operators_commute`, `v2_section_3_2_audit_log`,
`vacuum_relative_map_and_cp_commensurability`

(*Note: some entries appear here AND in View A above when V3 cites only one of multiple
related primitives in a family — e.g., V3 cites `theta_rel_z3_isotropy_dichotomy` but not
`theta_rel_equivariant_bifurcation_spine`. Audit pass.*)

---

## View B — section-keyed (V3 § → engine primitives via R-NNN)

Compressed list — for the full set see Section 1 (Result Index) rows.

### §A.1 Time is a wave
- R-001: no direct engine cite (kinematic statement of the wave-train)

### §A.2 The wavefront and the observer
- R-002: `pi3_orientation_class_two_windings` (the ℤ×ℤ), `pi3_S3_integer_completion`
  (the lepton-sector π_3(S³) = ℤ + the baryon integer-completion facts)
- R-003: `matter_stability_outside_frame`

### §A.3 Matter is a defect; the vacuum is the wave
- R-004: `matter_stability_outside_frame`
- R-005: `I4_maps_L_to_Q`
- R-006: `pi3_S3_integer_completion`

### §A.4 Mass is meta-time rotor frequency
- R-007: `wave_E_complex_structure`, `wave_E5`
- R-008: `single_quark_no_rest_mass_axis`

### §A.5 Mathematical setting (just enough algebra)
- R-009 (A.5.2): `L_Q_orthogonal_decomposition`, `is_L_bivector`, `is_Q_bivector`
- R-010 (A.5.3): `I4_squared`, `I4_maps_L_to_Q`, `duality_map`, `hodge_star`
- R-012 (A.5.4): `s0`, `is_idempotent`, `spinor_real_dof`
- R-011 (A.5.5): `exp_unit_bivector`, `half_angle_overlap`
- R-012a (A.5.6): `wave_E5`, `wave_E_complex_structure`, `spatial_vs_phase_partition`,
  `cl41_grounding_litmus`, `cl41_phase_is_external_u1`, `cl41_idempotents_note`

### §B.1 Lorentzian signature
- R-013: `gammas`, `gamma0_gammaj_reduces_to_ej`
- R-014: `cl_dimension`
- R-015: `gammas`, `cl_dimension`
- R-016: `equivalence_principle_protection`, `matter_stability_outside_frame`,
  `d4_lattice_lorentz_violation_orders` (the dim-4-only scope, R-165)

### §B.2 Special relativity
- R-017: `wave_E_complex_structure`
- R-018: `boost`, `rotation`, `so13_closure_signs`
- R-019: `thomas_KK`
- R-123: `defect_rotor_frequency_reads_as_k4_on_front` (2026-07-02 keystone bridge, §B.2.1)

### §B.3 Quantum mechanics from one move
- R-020: `born_subspace_one_B_forced`
- R-021, R-023, R-024: `born_subspace_one_B_forced` (subspace), no direct (postulate 4 is paper-only)
- R-022, R-166: `self_adjointness_from_one_B_projection` — postulate 2 is no longer paper-only: self-adjointness is forced by the `{1, B}` projection (`⟨ψ̃ M̂ ψ⟩_B = 0`), the "requiring reality" argument having been vacuous
- R-025: `dirac_ideal_idempotent`, `skyrmion_collective_quantization_under_v2_3p2`,
- R-160: `born_exponent_gleason_closure` — Born exponent = 2 as a theorem given F1–F4 + import-exempt Gleason (F2 = the open premise)
- R-161: `lock_channel_is_axial_chiral_channel_p1b_split` — P1b structural half (winding-assignment-relative); P1b-DYN stays CANDIDATE
  `colour_z3_holonomy_cannot_source_fr_sign` (2026-07-02 W1 reduction, N35)
- R-026: `hestenes_Isigma3`, `dirac_ideal_idempotent`

### §B.4 Bell, Tsirelson, non-separability
- R-027: `tsirelson_S`, `bell_correlation`, `chsh_S`, `half_angle_overlap`
- R-028: `mermin_klyshko_value`, `mermin_value`, `w_state_located_gap` (scope note)
- R-029: paper-only kinematic identity (no engine cite needed)
- R-030: `im_chi_falsifier_budget_KSS_GW_macromolecule`
- R-031: paper-only corollary

### §B.5 Electromagnetism
- R-032: `maxwell_grade_structure`, `maxwell_four_laws`
- R-033: `maxwell_grade_structure`
- R-034: `coulomb_potential`, `coulomb_sign_rule`, `coulomb_is_harmonic`
- R-035: `photon_strain_mode`

### §B.5b The fine-structure constant and its sibling g
- R-035a: `alpha_em_meaning`, `alpha_em_value` (raises until #1-gap closes)
- R-035b: `weinberg_sin2`
- R-035c: — (paper-only; definitional arithmetic, no engine primitive asserts the ladder)
- R-162: `coupling_sector_channel_disjointness` — EM vs colour channels provably disjoint; the α_s fold-in located, not derived

### §B.6 Gravity
- R-036: paper-only structural
- R-037: `sakharov_induced_gravity`, `induced_G_bracket_mode_count`,
  `induced_G_only_monad_scale_enters`, `induced_G_leading_coefficient_mass_independent`,
  `induced_G_quadratic_divergence_from_4D`
- R-163: `induced_G_from_linear_face_band` — I-3 narrowed to OA-LF-i ∧ OA-LF-ii; the flat-band measure derived
- R-164: `skyrme_quartic_contains_no_tree_EH` — no tree-level EH in the banked action class (ledger N51)
- R-165: `d4_lattice_lorentz_violation_orders` — point-group invariant theory ⇒ dim-8 anisotropy, conditional
  on (P-an ∧ P-pg) (positive); the isotropic dim-6 coefficient unprotected and GATED (negative; VG-6,
  §E.3.5(4), ledger N52, import I-19)
- R-038: paper-only Newton 1/r
- R-039: `equivalence_principle_protection`
- R-040: `induced_G_sign_cross_check`
- R-041: `sakharov_xi_minimal_coupling`
- R-042: `texture_tetrad`, `texture_metric_candidate`, `texture_metric_diffinvariance`,
  `texture_metric_tt_graviton`, `texture_metric_vierbein`, `texture_matter_gravity_coupling`
- R-145: `texture_frame_6to4_reduction`
- R-149: `texture_gauss_equation_riemann_closure`

### §B.7 The cosmic frame
- R-043: paper-only (arrow as +e_4)
- R-044: paper-only (one asymmetry — the causal arrow — from `+e_4`; weak handedness datum-selected on an unpinned orientation; thermodynamic arrow reduced, not derived)
- R-045: paper-only (c_meta = c on average)
- R-046: paper-only (Hubble radius identification)
- R-047: `gravitating_vacuum_energy`, `lambda_resolution_structure`

### §B.8 The macroscopic limit
- R-048: `macroscopic_LQ_split`, `worldline_bivector`, `polar_moment_of_inertia`
- R-049: `macroscopic_LQ_split`, `L_Q_orthogonal_decomposition`
- R-050: paper-only (Sundman + Cauchy-Schwarz)

### §C.1 The Skyrmion
- R-051: `skyrme_BVP_audit`, `skyrmion_mass_MeV`, `skyrme_length_fm`
- R-052: `pi3_orientation_class_two_windings`, `pi3_S3_integer_completion`
- R-053: `nonuniform_orbit_baryon_model`, `cogear_linkage_kinematic`,
  `baryon_mass_shared_rotor_nonadditive`, `e4_content_confines_quarks_not_leptons`
- R-054: `pi3_S3_integer_completion`, `lepton_number_topological_conservation`
- R-055: `electron_two_windings`, `electron_QCP_nu`, `electron_f_L_MeV`

### §C.2 Charges and the first generation
- R-056: `hypercharge`, `doublet_hypercharge`  *(the `winding_charge` cite is pruned: R-056 is an ANCHOR-FREE-side result — the `e₄`-bilinear eigenvalue — and the charge-assignment primitive is not one of its backers)*
- R-057: `gmn_coefficient`, `triple_product_Q`, `triple_product_color`
- R-058: `doublet_hypercharge`
- R-059: `universality_theorem`
- R-060: `weak_isospin_SD_parity_exclusion`, `vminusa_is_spin4_factor_chirality`
- R-061: `weak_isospin_zero_on_generations`, `weak_isospin_centralizer_is_SD`
- R-062: `gmn_coefficient`, `generation_spectrum`
- R-063: `winding_charge`, `gmn_coefficient`, `generation_spectrum`,
- R-159: `charge_normalization_anchor_free` — Q_p + Q_e = 0 identically in c given (P4,P5,P6,P7); neutrality import conditionally replaced (all four premises — the lepton-slot flip returns +1 with P4+P5 intact)
  `pi3_S3_integer_completion`

### §C.3 Three generations, Koide, neutrinos
- R-064: `brannen_amplitude`, `koide_K`, `koide_from_c`
- R-065: `dft_K_from_r`
- R-066: `koide_K`, `koide_from_c`, `koide_charge_unification`, `dft_K_from_r`
- R-067: `foot_angle_deg`
- R-068: `brannen_amplitude`, `delta_L_from_DoverJ`, `DoverJ_from_lepton_masses`,
  `hierarchy_type` (CANDIDATE-strong: also pulls `mass_measure_from_omega`)
- R-069: `delta_L_from_DoverJ`, `D_crit_over_J`
- R-070: `delta_L_from_DoverJ`
- R-071: `why_three_generation_triple`, `generations_dynamical_count_structural`,
  `phase_to_h_unit_map_located_residual`
- R-072: `G_generator`, `G_cycles_generations`, `generation_z3_is_metatime_phase`
- R-073: `quark_brannen_table`, `quark_mass_reconstruction`,
  `cabibbo_transition_probability` (`cabibbo_angle_rad` deprecated, removed 2026-07-02)
- R-074: `DoverJ_from_lepton_masses`, `DoverJ_from_skyrme`, `over_determination_scan`,
  `dressed_coupling`
- R-075: `forced_handedness`
- R-076: `neutrino_lightness`
- R-077: `updown_mass_operators_commute`, `updown_mirror_value_three_handles`

### §C.4 The gauge group from D4 orbits
- R-078: `spatial_vs_phase_partition`, `L_Q_orthogonal_decomposition`
- R-079: `weak_su2_menu_exhaustion`, `weak_isospin_SD_parity_exclusion`,
  `weak_isospin_centralizer_is_SD`,
  `weak_isospin_verdict`, `weak_isospin_rank_table`, `vminusa_is_spin4_factor_chirality`
- R-171: `weak_su2_menu_exhaustion`
- R-172: `weak_host_must_be_body_frame`, `lock_left_centralizer_is_u1`
- R-173: `brannen_comb_commitment_dominance_and_dof_vacuity`
- R-174: `magnon_stiffness_bands_canted_vacuum`
- R-175: `spectral_branch_symmetry_class_filter`
- R-080: `hypercharge`, `winding_charge`, `I4_squared`
- R-081: `gluon_octet_symmetric_space_split`, `colour_quartic_charge_handle`,
  `colour_relative_phase_is_coset`, `colour_sector_E_hermitian_form`,
  `colour_su3_located_gap`, `colour_SO3_re_realization_forbidden`
- R-082: `weinberg_sin2` (engine-exact 3/8)
- R-083: `D4_spatial_bond_isotropy`, `D4_DM_bond_bivectors_non_commuting`

### §C.5 Strong, electroweak, stability ladder
- R-084: `pi3_S3_integer_completion`, `e4_content_confines_quarks_not_leptons`
- R-085: `gluon_octet_symmetric_space_split`, `colour_SO3_re_realization_forbidden`
- R-086: `eta_DM`, `chirality_does_not_source_P`, `chirality_is_a_reflection`
- R-087: `B_minus_L_anomaly`, `anomaly`
- R-088: `bpst_charge_Q`, `bpst_selection_rule`
- R-089: `B_minus_L_anomaly`, `bpst_selection_rule`,
  `lepton_number_topological_conservation`, `pi3_S3_integer_completion`
- R-090: `I4_maps_L_to_Q`, `lepton_number_topological_conservation`
- R-091: — (cites struck 2026-07-31, C-3; `topological_overproduction_test` belongs to the over-production result, Section 8, not the ladder)
- R-091a: `top_excluded`, `alpha_H_gap`, `x_Q`
- R-091b: `nuclear_length_hierarchy`, `skyrme_length_fm`

### §D.1 The Clifford algebras
- R-092: `cl_dimension`, `_cl40`, `cl40_quaternion_triple`, `cl40_vs_cl41`
- R-093: `cl40_quaternion_triple`, `cl40_vs_cl41`, `cl41_grounding_litmus`
- R-094: `cl41_grounding_litmus`, `cl41_phase_is_external_u1`, `cl41_idempotents_note`

### §D.2 Spinors, grades, the dictionary
- R-095: `cl41_idempotents_note`, `cl41_phase_is_external_u1`, `dirac_ideal_idempotent`
- R-096: `spinor_real_dof`, `dirac_ideal_idempotent`
- R-097: `L_Q_orthogonal_decomposition`, `triple_product_Q`, `triple_product_color`,
  `L_algebra_su2_closure`
- R-098: `anti_self_dual`, `self_dual`, `self_dual_blade`, `chiral_split_demo`,
  `spin4_generator_count`
- R-099: `self_dual`, `anti_self_dual`, `duality_map`, `chiral_split_demo`
- R-100: `spatial_vs_phase_partition`, `wave_E_complex_structure`, `wave_E5`,
  `spin4_generator_count`

### §D.3 The D4 grain layer
- R-101: no direct engine cite (D4 packing fact is INPUT premise A-1b)
- R-102: `s0`, `spinor_real_dof`, `pi3_orientation_class_two_windings` (the dim-6 census
  of `Cl⁺(4,0)` and its chiral factorization — the local state's six real parameters)
- R-103: `D4_spatial_bond_isotropy`, `D4_DM_bond_bivectors_non_commuting`,
  `dressed_coupling`, `DoverJ_from_lepton_masses`
- R-104: `D4_spatial_bond_isotropy`, `D4_DM_bond_bivectors_non_commuting`
- R-105: paper-only structural (forced two-scale)

### §D.4 Medium Lagrangian, wave equation
- R-106: `f_pi_squared`, `sigma_model_kinetic_normalization`
- R-107: `dressed_coupling`, `kappa_F_bare`, `spiral_angle_deg`
- R-108: `canting_pitch_q_rad`, `canting_cos_q`, `canting_critical_stiffness_at_DJ`,
  `Kc_magnon_stiffness_canted_FM_at_DJ`, `n_goldstone_canted_FM`
- R-109: `skyrme_BVP_audit`, `sigma_model_kinetic_normalization`
- R-110: `DM_operator_gaussian_dim`
- R-111: `nuclear_length_hierarchy`, `qcd_uv_conformal_phaseCD`
- R-112: `wave_E_complex_structure`, `wave_E5`, `eom_constraint_class`

### §D.5 The driven-dissipative dynamics — the #1 gap
- R-113: `eom_compatible_field_forks`, `eom_invariant_variant_audit`
- R-114: `eom_compatible_field_forks`
- R-115: `eom_compatible_field_forks`
- R-116: `im_chi_falsifier_budget_KSS_GW_macromolecule`, `identify_the_floor`
- R-117: `eom_invariant_variant_audit`, `interference_can_reduce_mass_goldstone`,
  `identify_the_floor`, `massless_H_squared`, `protection_mechanism_located`
- R-118: `theta_rel_universality_located`, `theta_rel_pinnability_from_data`,
  `theta_rel_equivariant_bifurcation_spine`, `theta_rel_rotating_wave_escape_located`,
  `theta_rel_z3_isotropy_dichotomy`, `colour_relative_phase_is_coset`,
  `colour_quartic_charge_handle`, `colour_abare_static_holomorphic`,
  `colour_arich_kernel_dependent`

### §E.1 Cosmology and the arrow of time (frontier)
- R-119: `gravitating_vacuum_energy`, `lambda_resolution_structure`,
  `lambda_H2_dynamical_reading_excluded`
- R-120: paper-only (coherence condition)
- R-121: `sterile_rh_relic_check`
- R-122: `sterile_rh_relic_check`, `sterile_rh_z2_separate_mass_scale_check`,
  `sterile_rh_substrate_production_via_L_theta`

### §E.5 A candidate for the #1-gap kernel (the KS campaign, 2026-07-22)
- R-153: `kernel_candidate_form`
- R-154: `kernel_composite_closure`
- R-155: `kernel_candidate_dials`
- R-156: `kernel_candidate_constraints` (pre-existing — the acceptance inventory the candidate reports against)
- R-157: `kernel_overdetermination_table` (pre-existing — the rank-deficiency live invariant, R-150)
- R-158: `kernel_candidate_falsifiers`

### §E.2 / §E.3 / §E.4 / §E.6
These sections synthesize; they introduce no new R-NNN. Engine cites carried by their referenced
R-NNN above. §E.3's falsifier rows cross-reference R-NNNs per the Result Index.

---

## Engine primitives that RAISE (GATED — magnitude blocked)

Per CLAUDE.md §6: GATED primitives raise when called, so users cannot accidentally consume an
ungrounded magnitude. The V3 paper cites these only with explicit "(raises)" notation:

- `alpha_em_value` (R-035 / D.5 context; α magnitude #1-gap-gated)
- `texture_tetrad` (R-042 / B.6; absolute coefficient gated)
- `qcd_collider_phenomenology` (Layer-3 deep gate)

`twt_test.py` includes positive tests that each of these raises — that's part of suite discipline.

---

# Section 4 — Pending-Values Registry

*Open items by kernel object: S, Θ_rel, absolute ω, Im χ, L2 mechanism, located-gap handles.*


*Version 3 · Phase α draft · 2026-06-30.*
*All open numerical values the framework owes, organized by which deep gate they share. The
"over-determination" thesis is operative here: pin-and-check across the registry collectively
constrains the gates more tightly than any single item.*

---

## How to read this file

The framework has **one value gate** (`S` ≡ Θ_rel via `Im χ`, the #1 gap, §D.5) and **two
structural gates** (texture tetrad, QCD UV gate). Almost every open numerical item routes
through one of these. The registry groups them so the reader can see, at a glance:

- **What's collectively gated on `Im χ`** — α_em, g, α_s, α_W, decoherence rate 1/T_2,
  Λ ~ H² residual
- **What's gated on Θ_rel** — colour-U(3) → SU(3) breaking; CKM hierarchy + Jarlskog;
  asymptotic freedom β_3 sign; coupling universality
- **What's gated on absolute ω scale** — f_π absolute MeV; M_0; 1/Θ_0; m_e (via L-orbit QCP);
  same-composition mass split magnitudes; vector meson absolute masses
- **What's gated on S (rich-branch barrier action)** — τ_mem coefficient; tunneling rates;
  Born selection rate
- **What's gated on L2 mechanism** — anomalous dimension `ν = 3π/2` for L-orbit QCP; active-sterile
  overlap for m_ν
- **Located-gap items** with named re-attack handles

Columns:
- **Item** — the value or mechanism that's open
- **Gates on** — which deep gate's closure unlocks it
- **Tier** — current honest tier
- **R-NNN** — link to Result Index row that mentions this item (where applicable)
- **Engine** — primitive that banks the located-gap (raises if magnitude is sought)
- **Re-attack handle** — what would advance the item

---

## Gated on `Im χ` (the #1 gap; §D.5; structural gate 3.3)

| Item | Tier | R-NNN | Engine | Notes |
|---|---|---|---|---|
| Fine-structure constant `α_em` | GATED (magnitude) + DERIVED (ontology) | R-035a | `alpha_em_value` (raises), `alpha_em_meaning` | The α-object is a reactive grade-0 Clifford invariant — L↔Q reconversion strength (Annex N.E catalog item 8). DERIVED ontology, GATED magnitude. |
| Weak coupling `g` | GATED, but α-sibling not independent gate | R-035b | `weinberg_sin2` | Given R-082's `sin²θ_W = 3/8`, `g² = 4πα · (8/3)` — `g` is α's algebraic sibling. Same `Im χ` functional samples both; EW sector reduces to ONE magnitude. |
| Strong coupling `α_s` | GATED | C.5 context | `qcd_collider_phenomenology` (raises) | Layer-3 / D.5. Same `Im χ` dial at different frequency. |
| Weak coupling `α_W` | GATED | — | — | Same `Im χ` functional as α_em, different frequency. |

**The single-dial economy** (§B.5b hook). Where the SM treats α_em, g, g_s, α_W as four
independent fits, TWT identifies them as four samples of one transport function `Im χ`. Closing
the #1 gap (§D.5) would simultaneously pin all four. Until then, the **count** (one magnitude,
not four) and the **meaning** (reactive L↔Q reconversion for α; algebraic siblings via the proven
gauge-mixing angles) are DERIVED; the **value** of α is OPEN. **[2026-07-22: a candidate kernel
FORM now exists (§E.5, R-153, CANDIDATE/Grade B); the VALUES remain gated on the kernel's own
gated forward maps — these gates stay live.]**
| Decoherence rate `1/T_2` | GATED + falsifier-testable | R-117 (paper context) | `identify_the_floor`, `interference_can_reduce_mass_goldstone` | Floor structurally safe per WP-DC2 / WP-IX4. Canonical falsifier §E.3 VG-3. A candidate kernel FORM exists (§E.5, R-153); the value stays gated. |
| Cosmological-constant residual (magnitude; present-epoch `ρ_vac ≈ 3Ω_Λ,0 M̄_Pl² H_0²`) | GATED + falsifier-testable | R-119 | `gravitating_vacuum_energy`, `lambda_resolution_structure`, `lambda_H2_dynamical_reading_excluded` | Driven-dissipative deviation from Volovik equilibrium. §E.3 VG-2. A candidate kernel FORM exists (§E.5, R-153); the coefficient stays gated. **The epoch law is not pending — the dynamical `ρ_vac ∝ H(t)²` reading is excluded (N54, §E.1.1); only a magnitude is owed.** |
| Macromolecule-interferometry decoherence (KSS-floor to GW170817-ceiling bracket) | GATED + falsifier-testable | R-030 | `im_chi_falsifier_budget_KSS_GW_macromolecule` | One dial, two operational windows (Bell + macromolecule). §E.3 VG-1. |
| Isotropic dimension-six LV coefficient `η⁽⁴⁾` (≡ substrate `c` via `η⁽⁴⁾ = c(M_Pl/Λ)²`) | GATED + **empirically bounded** | R-165 | `d4_lattice_lorentz_violation_orders` (moments, invariant dims, `implied_substrate_c_ceiling`); the gate itself is `Cl41Wave().wave_speed_c()`, which raises | **The registry's only entry with an existing measurement.** Every other row is a value the gap fails to deliver; this one the gap must deliver *beneath a published ceiling* — `\|η⁽⁴⁾\| ≲ 10⁻⁶` (matter), `≲ 10⁻⁸` (photon), i.e. `\|c\| ≲ 1.5×10⁻⁹ … 5.4×10⁻⁷` across {species, `Λ_L`-corner}. At the naive `c = 1` (NOT a TWT claim — `c` is gated) it would read `η⁽⁴⁾ = c_lat/(2π) ∈ [1.9, 6.7]`, excluded by 3–9 orders. **(Which-Λ ruled 2026-07-30: dispersion consumers take `Λ_L = 1/a ∈ [0.39, 0.73] M_Pl` — the OA-LF-ii band on `c_lat = 21.83`; the 2026-07-28 wide bracket `[0.13, 2.5]` / `η⁽⁴⁾ ∈ [0.16, 59]` / 2–10 orders is RETIRED. The ceiling row NARROWED and its favourable end got *worse*. See R-037/R-163.)** **`is_usable_anchor = FALSE`, and the reason is structural, not provisional: a ceiling is an inequality and supplies no equation, so it contributes ZERO rank to the over-determination programme — it can refute a candidate kernel but cannot help pin one.** Bindingness conditional on I-19 premise (e) (inside-frame data, outside-frame object). §E.3 VG-6, §E.3.5(4), N52; boundary entry `E1` in `eom_constraint_class`. |

---

## Gated on `Θ_rel` (the FDT-violation residual; structural gate 3.3 + dynamics)

| Item | Tier | R-NNN | Engine | Notes |
|---|---|---|---|---|
| Colour-U(3) → SU(3) breaking magnitude | GATED | R-081, R-118 | `colour_relative_phase_is_coset`, `colour_quartic_charge_handle`, `colour_abare_static_holomorphic`, `colour_arich_kernel_dependent` | Z3-isotropy-dichotomy direction derived; magnitude #1-gap-gated. |
| CKM hierarchy + Jarlskog | GATED | C.3 context | `ckm_arc_channel_identity_and_verdict`, `ckm_arc_circulant_linchpin`, `ckm_arc_sector_and_corotation`, `ckm_hierarchy_and_cp_seed` | Frequency-ratio `\|V_us\|² = m_d/m_s` (R-073, the **Gatto–Sartori–Tonin relation** — not original here) is CANDIDATE; full hierarchy requires Θ_rel closure. |
| Asymptotic-freedom `β_3 < 0` sign | LOCATED-GAP | R-085 | `beta3_sign_from_reflection_positivity` | Reflection positivity bounds bare coefficient sign, sign-agnostic on running. Re-attack via c/a-theorem analogue on marginal-Skyrme RG flow. |
| Coupling-universality (SOC) | CANDIDATE | — | — | Gemini-originated speculation; not yet implemented. Would give a-priori reason `g_1 = g_2 = g_3` at substrate scale. |
| Θ_rel kernel value itself | #1-gap-gated | R-118 | `theta_rel_*` family (located-gap banks) | Single highest-value target in the framework. |

---

## Gated on absolute ω scale

| Item | Tier | R-NNN | Engine | Notes |
|---|---|---|---|---|
| `f_π` absolute MeV (currently INPUT 129 — the **ANW fitted** value, not the measured decay constant; physical `F_π ≈ 186 MeV` in ANW's normalization) | INPUT | A-1c, R-106 | `f_pi_squared` | Could become GATED-then-derived under §D.5 closure. |
| The `ω` ↔ **renormalized-mass** identification — at which MASS DEFINITION does `mass = ω` hold? | **OPEN** (unlabelled in the corpus until 2026-07-30; not GATED — no gate was ever named) | R-064–R-066, R-068, R-074, R-134; §A.4 | none — **no primitive fixes the identification**; `LEPTON_MASS_SCALE_NOTE` now records what the inputs are | **The framework's tightest empirical fit rides an unfixed bridge.** §A.4's `mass = ω` is a grain-layer statement; `K = 2/3` is a relation among the **physical (on-shell / pole)** charged-lepton masses (engine `M_E, M_MU, M_TAU`; PDG 2026). Nothing in paper, companion or engine says which renormalized mass `ω` equals, so *why Koide holds at that mass definition* is OPEN, not derived — the canon §0 two-scales problem at the headline result. The objection is NOT that the pole is the wrong choice: for an ontology in which mass IS a rotor frequency the pole is the natural default, and it is itself scale-independent. It is that the identification is **unstated and unargued**, and that a substrate-scale derivation has no stated reason to descend to the pole point rather than to a running mass. Size, from §C.3.3 (own one-loop computation, **not banked, not engine-verified**): `−3.3 × 10⁻⁶` at the pole point vs `+(1.72 – 1.89) × 10⁻³` under a one-loop QED pole→`MS-bar` conversion, i.e. 520–571×; Foot angle `45.000° → ≈ 45.05°`; `δ_L` `12.73° → ≈ 12.67°`. **R-074 is NOT weakened — it tightens:** the lepton leg moves `0.787 → 0.781` toward the unmoved baryon leg `0.778`, so lepton↔baryon goes `1.08% → 0.34–0.40%`. **R-134 is the most exposed:** `μ²` is an *absolute* scale, not a ratio, so it feels the common rescaling too and that part IS `μ`-dependent — its `0.28%` becomes `+0.8%` / `−0.2%` / `−1.6%` at `μ = m_μ` / `m_τ` / `M_Z`. **Honest contrast:** `sin²θ_W` HAS a descent account and it FAILS openly (§C.4.5, N55); Koide has none. Prior art on the objection: Sumino 2009a/b — `U(3)` family gauge bosons cancelling the QED correction (Section 10); TWT has no family gauge sector and does not adopt it. Re-attack: derive what the substrate → inside-frame descent does to a rotor frequency. **`is_usable_anchor = FALSE`** — a missing *definition*, not a missing number, so it adds no rank to the over-determination programme; it can invalidate a Koide-dependent claim but cannot help pin a kernel. Negatives ledger N57. |
| `M_0` baryon mass at dressed coupling | DERIVED at dressed-coupling | R-051 | `skyrmion_mass_MeV`, `skyrme_BVP_audit` | `M_0 = 36.47 f_π/e`. Absolute number gated on `f_π`. |
| `1/Θ_0 ≈ 196 MeV` CANDIDATE for `Λ_QCD` | CANDIDATE | R-111 | `nuclear_length_hierarchy`, `qcd_uv_conformal_phaseCD` | Identification owed; mechanism not closed. (Was 215 pre-R-133 correction; stays in the Λ_QCD range — scheme caveat, no strengthening claimed.) |
| `f_L` (L-orbit stiffness) via QCP scaling — **`m_e` itself is NOT a pending value of this row; the framework has no route to it** | DERIVED-CONDITIONAL (scaling) | R-055 | `electron_f_L_MeV`, `electron_QCP_nu` | The scaling law delivers a stiffness `f_L ≈ 0.115 MeV`, gated on the absolute ω scale like every other absolute MeV number. The `f_L → m_e` conversion is **EXCISED** (2026-08-20, Gate C branch (b)), and its three residuals with it — ~36% on `f_L`, 4.4% on the exponent, 0.34% on `ν = 3π/2`. What blocks a mass is upstream of any coupling: **which functional stabilises the L-orbit defect is open**, so no dimensionless coefficient exists for the L-sector. The SU(2) Skyrme hedgehog's `36.47` is the BARYON functional's and applies only if the L-orbit defect is the S³-valued degree-1 Skyrmion; on the S²-director Faddeev–Skyrme branch the rigorous Vakulenko–Kapitanski floor (coefficient 59.6, from `32π²√2 (3/16)^{3/8} = 238.4`) **excludes** it outright, and GF-5's fixed-charge balance admits neither static coefficient. No engine primitive computes any L-sector coefficient. L2 mechanism unidentified. |
| `λ̄_C` (Compton wavelength) | Inherited | C.1 | — | Inherits from `m_e`. |
| Same-composition mass splits (77, 294, 193, 217 MeV) | DERIVED-STRUCTURAL (sign) + GATED (magnitude) | C.3, C.5 | `same_composition_baryons_pin_internal_mode`, `interference_can_reduce_mass_goldstone`, `gell_mann_okubo_gamma` | Directional prediction (anti-aligned < aligned) DERIVED; magnitudes gated. |
| Vector meson absolute masses (σ, ρ, ω) | CANDIDATE | C.5 | `meson_dynamical_current_split`, `meson_topological_status` | Q-orbit field-mode identification; magnitudes open. |

---

## Gated on `S` (rich-branch barrier action; §D.5 closure)

| Item | Tier | R-NNN | Engine | Notes |
|---|---|---|---|---|
| `τ_mem` coefficient (memory lifetime) | GATED | R-115 (paper context) | `eom_compatible_field_forks` | Rich-branch barrier action sets the e^{S/ℏ} prefactor. A candidate kernel FORM exists (§E.5, R-153–R-155: τ_mem a counted candidate dial, F3-pinned economy-preferred); the value stays gated. |
| Tunneling / decay rates | GATED | D.5 context | — | Type-A / "probability ↔ action" lens applies. Distinct from Type-B (analytic) — see Annex N.E catalog item 8 on α. |
| Born selection rate | GATED | B.3 context, R-117 | `protection_mechanism_located` | The Role-3 §D.5 selection law's rate constant. |

---

## Gated on L2 mechanism (the electron's second residual)

| Item | Tier | R-NNN | Engine | Notes |
|---|---|---|---|---|
| `ν = 3π/2 = 4.712` anomalous dimension — a candidate VALUE, with no accuracy figure attached | CANDIDATE | R-055 | `electron_QCP_nu` | Mechanism unidentified. The former "0.34% match" is **excised with the conversion** (2026-08-20): the empirical exponent it matched, `ν_emp ≈ 4.696`, is only definable through the `f_L → m_e` conversion and moves to 5.123 (8.0% off `3π/2`) on the Faddeev branch. A mechanism would still be wanted; it would not by itself unblock a mass, which needs the functional settled first. |
| Active-sterile overlap → `m_ν` | GATED | R-076 (paper context) | — | Active-sterile overlap calculation is Paper-2; would also unlock DM-V2-1 Z3 lead. |

---

## Located-gap items with named re-attack handles

Each row: (a) primitive that banks the located gap; (b) failure mode of attempted closures so
far; (c) named handle for re-attack.

| Item | Engine (located-gap bank) | Tried → Failed → Would change if |
|---|---|---|
| `K_c = (2/19)·J` vortex-line stiffness prefactor at D=J QCP | `canting_critical_stiffness_at_DJ` (engine-banked; Lead A validated, Leads B and C rejected) | The 19 is DERIVED from static Luttinger-Tisza; the 2 is `N_G = dim(SU(2)_L / U(1)_canting) = 2` via Hopf S¹ fiber. *Kernel FORM* `K_c = N_G · sin²(q) · J` is what remains §9.6-gated. Re-attack: §9.6 driven-dissipative kernel closure, or a static vortex-line linear-response normalization that closes Lead A into an identity. |
| DM-V2-1 sterile RH relic shortfall (~47× / hot-DM excluded / m_s~keV unavailable) | `sterile_rh_relic_check`, `sterile_rh_z2_separate_mass_scale_check` (Z1 LOCATED-GAP-REFINED), `sterile_rh_substrate_production_via_L_theta` (Z2 LOCATED-GAP-REFINED) | Three substrate routes for Z1 (separate mass scale) fail by §17.1 KK structure + §19.8.3 B−L. Z2 fails because §10.5 sources L-pairs in S_+ but RH sterile lives in S_−. Z3 (active-sterile overlap > 1 without B−L violation) STILL OPEN. Re-attack handles: B−L-charged condensate connecting two e_5 modes (not in current TWT); resonant Shi-Fuller with TWT-derived primordial lepton asymmetry (CANDIDATE only); substrate channel creating pure-S_- L-pairs directly (requires breaking S_- wave-decoupling, tension with §19.8.1). |
| `β_3 < 0` sign via Euclidean reflection positivity | `beta3_sign_from_reflection_positivity` | RP forces only the bare coefficient sign; sign-agnostic on running (counterexamples both ways — 2D O(N) σ-model RP+AF; 4D φ⁴ RP+IR-free). Re-attack: c/a-theorem analogue on marginal-Skyrme RG flow, or Källén-Lehmann positivity + a unitarity bound on the running quartic. |
| `m_p/m_e ≈ 1836` vs `v_EW/f_π ≈ 1909` absolute-scale hierarchy (item #14) | `q_l_stiffness_ratio_is_gap_gated`, `cand1_24cell_ratio_computed` (negatives ledger N12) | The gate-free Layer-1 route (a D4 24-cell triality/Casimir projection ratio) was COMPUTED and CLOSED — every natural scale-free ratio is O(1) (largest `8/3≈2.67`), ~690× short of the ~1836× target; the 24-cell is self-dual with F₄/D₄ triality, so the lepton (anti-self-dual bivector) and quark (colour trivector) sectors are triality-equivalent octads — structurally the *opposite* of a large hierarchy. The hierarchy sits entirely at the #1 gap, no surviving gate-free remnant. Re-attack: a motivated exotic (non-combinatorial, e.g. determinant/exponential) 24-cell functional targeting a physical observable — not foreclosed, but unmotivated. |

---

## INPUTs (the framework's empirical inputs, for parameter-counting)

Not "pending" — these are the framework's empirical anchors. Listed for completeness; they appear
in V3 §E.2 "Status" as the parameter ledger.

| Input | Value | Notes |
|---|---|---|
| `f_π` | ≈ 129 MeV | Cell-scale mass scale; condensate-identified. **The ANW *fitted* coupling**, ~30 % below the physical `F_π ≈ 186 MeV` in ANW's own normalization — its proximity to the measured `f_π⁺ = 130.2(1.7) MeV` is a convention collision, not agreement. Counted as an INPUT because it is fitted, not measured |
| `Λ_S` — Sakharov proper-time cutoff | `√(2π) M_Pl ≈ 2.51 M_Pl` at `N_eff = 6`, `c_reg = 1/12` | The heat-kernel truncation VARIABLE in `G⁻¹ = N_eff Λ_S²/(12π)`. `Λ_S = √(12π/N_eff)·M_Pl`: fixed by measured `G`, by `N_eff`, and by the proper-time scheme alone, and EXACTLY independent of the lattice (checked over arbitrary `c_lat` in `c_reg_from_substrate_mode_content`). It carries no substrate information — it is measured `G` restated. |
| `Λ_L ≡ 1/a` — inverse grain spacing (Brillouin-zone edge) | `0.537 M_Pl` central (affine `κ=1`; flat-band `c_lat = 21.83` gives `0.536` — same at 2 d.p.); `[0.386, 0.735] M_Pl` across OA-LF-ii's `κ ∈ [½, 2]` through the affine `c_lat(κ) = 1.51 + 20.28κ` | The PHYSICAL lattice scale: `Λ_L = √(12π/(N_eff·c_lat))·M_Pl`, hence **`Λ_S = √(c_lat)·Λ_L` exactly**, for every `N_eff` and every `M_Pl`. The two are NOT one quantity in two schemes: under a change of kernel `c_lat` and the quartic dispersion coefficient move by different factors, so `√(c_lat)` is not a universal conversion constant. Conditional on (OA-LF-i ∧ OA-LF-ii) + `N_eff = 6` + matching to the empirical `G` — never "TWT derives the grain spacing" (R-163). |
| `Λ` (legacy, ambiguous — do not add new uses) | Planckian within O(1) | Retained only where the corpus has not yet been disambiguated into `Λ_S` / `Λ_L`. **RULED (coordinator, 2026-07-30):** `Λ_S = √(2π) M_Pl` (scheme; Sakharov/`G` bookkeeping) · `Λ_L = 1/a ∈ [0.39, 0.73] M_Pl` (dispersion consumers, per the scoped assignment at §B.6.2). The §B.6 wide bracket `[0.13, 2.5] M_Pl` is RETIRED — R-037. **COUNT (Branch B, coordinator 2026-07-30): `Λ` is NOT an independent counted INPUT** — both scales are back-fits of measured `G_N`, which is the counted gravitational anchor; the ledger is four substrate inputs + `G_N` (§E.2.1). |
| `e_ANW = 5.45` (provisional same-object determination) | Skyrme quartic stabilizer, massless-pion scheme | **Counted PROVISIONALLY (coordinator ruling 2026-07-31, C-7 i′):** the hadron-sector determination of the SAME object the substrate relation `√18/(D/J)` predicts (`≈ 5.37–5.39`, the digit depending on which `D/J` leg — 0.79 engine default vs 0.7869 lepton leg; 1.1–1.5% apart, reconciled band 2026-07-31). Hedges: the massless baseline was chosen partly on that very agreement (massive-pion branch `e* = 4.84`, an 11% scheme spread), and the substrate relation carries NO scheme label (dictionary row below). RETIREMENT both ways: sharpened legs converge → `e` retires, count drops back to four; they split → the `√18` bridge dies. Consumed by every §C.1.2 number. |
| **The renormalization dictionary** (missing object; named 2026-07-31) | which inside-frame scheme/scale a substrate-level quantity lands on | The outside↔inside projection OWES this entry. THREE known faces: **N57** (`ω` ↔ which mass definition — Koide exact at pole, degraded ~2.5 orders at MS-bar), **C-7** (`√18/(D/J)` ↔ which scheme's `e`), and **`m = E₀`** (the lock-units elastic↔frequency line, counted premise 2026-08-12 per ruling R3(a) — it NAMES the classical/tree branch and carries NO scheme label; a label is owed the moment an `E₀`-derived number is quoted at a scheme — the N57/K-L5 trap). Until the entry exists, cross-frame numeric agreements cannot be fully credited nor discrepancies interpreted. Worklist item (ledger). |
| `m = E₀` (soliton-mass identification) | counted PREMISE (2026-08-12, ruling R3(a)) | The §A.4 outside-face bridge: rest frequency = VACUUM-SUBTRACTED elastic cost (lock units; v = 0 reading only — moduli evaluation at v ≠ 0 fires the boost-covariance duty). Standard soliton identification (ANW / Schroers Lsk1 / Manton–Sutcliffe; enters via the I-5 amendment). ADJACENT to — never the content of — R-123 residue (ii) (presupposed), N57 (no scheme picked; classical branch named), C-7 (distinct face). Consumed by R-051/R-133 (calibration)/R-135/R-137/R-138; NOT by R-144. Derived fragment: inertia = E₀ at O(v²) iff Derrick-balanced (R-169). Engine: `mass_equals_elastic_cost_premise`. |
| `D/J` | ≈ 0.79 | Chirality **ratio of totals**; calibrated to leptons; the baryon leg agrees to ~1.1% but reads a *different functional* (R-074 as conditioned by R-180/R-181) — not an independent over-determination |
| `c = √2` ⇔ `K = 2/3` | exact (10⁻⁵) **at the pole point** | Brannen phase coefficient. Six forcing routes investigated NEGATIVE. **DEFINITION-SPECIFIC** (flagged 2026-07-30): the `10⁻⁵` is a property of the **physical (on-shell / pole)** charged-lepton masses; a one-loop QED pole→`MS-bar` conversion degrades it to `~1.8 × 10⁻³` (§C.3.3 — own computation, not banked, not engine-verified). The `ω` ↔ renormalized-mass identification that would say *why* the pole point is the right one is fixed nowhere — see the `Gated on absolute ω scale` row and negatives ledger N57. |
| `A` (lepton amplitude scale) | empirical | Free Koide calibration; cancels in ratios |
| `weak = SD` | one bit, **read not tuned** | The chiral `Spin(4)` factor. **The bit is the right-handed fermions' weak-isospin-singlet character**, which closes the computed three-class menu (R-171); it is not a free choice among geometric options, and it is not forced by the neutrino — the single-Weyl neutrino provably cannot discriminate SD from the diagonal class (RV-7). Carried with it, and **named but not counted here** because it is a structural premise rather than an empirical input: **A-P2** — weak isospin is a 3-dim `su(2)` inside grade-2 `so(4)` at all (FRAMING in the engine; **stamped ENDORSED, RUL-084** — a preferred direction, not a counted input). Number in this tally unchanged; kind changed. |

---

## The over-determination opportunity

Per V2 §25.1 user-direction 2026-06-29: the registry's collective set provides constraints on
the kernel objects beyond what any one item gives. Pin-and-check across the registry is the
analog of the lepton ↔ baryon cross-sector ~1.1% validation, lifted to the #1-gap output level.

When a future closure attempt produces a candidate `Im χ` or `Θ_rel` value, it must be checked
against **all** registry items it gates simultaneously, not just one. A candidate that lands α_em
correctly but fails on `1/T_2` is not a closure — it is a contradiction the registry surfaces.

**2026-07-02 update.** A session attempted exactly this — treating the registry's collective set
as constraints on a physically-motivated kernel ansatz and trying to fit/check it against them.
Verdict: rank-deficient with current data (effectively one usable numeric anchor — the
KSS-to-GW170817 bracket — against a kernel needing ≥2 free parameters); see negatives ledger N33
for the full attempt and the named missing inputs. A follow-on argument (anchoring `τ_wave` to the
Planck scale to argue the fading branch is laboratory-incapable of sourcing the VG-1
macromolecule-interferometry pillar) was adversarially reviewed and found to be an OVER-CLAIM — see
N34. Neither is banked as a physics result; both are recorded so the same ground isn't re-covered.

**2026-07-05 update (W2.1, R-150).** N33's meta-result is now GRADUATED into the engine as
`kernel_overdetermination_table` (suite 397→398) — the Class-2 (2b) campaign dashboard. It
enumerates the registry's kernel constraints as structured rows, tags each with an anchor
STATUS, and asserts the usable-anchor count (== 1, the KSS/GW bracket) so the rank-deficiency
is now a LIVE, self-validating invariant rather than prose: the count increments the moment a
genuine new (frequency, value) anchor (N33 input (3), e.g. the W2.2 static sum-rule datum from
the canted-D4 LSWT machinery) is manufactured. The primitive cross-validates its sharpest rows
against their source primitives live (Kc = (19/2)√38; running µΨ₀; Brannen 0.28%) and enforces
the two N33 exclusions (sin²θ_W = 3/8 is gate-free, NOT an Im χ sample; g/α_s/α_W = one unknown)
by assert. Jurisdiction recorded: a new anchor may ride causality/Kramers-Kronig + equal-time
f-sum moments, NOT FDT (I-12, whose violation residual IS Θ_rel).

**2026-07-05 (W2.2, ledger N43).** First attempt to LIFT the rank-deficiency via N33 input (3).
Input (3) IS partially deliverable from statics — the canted-D4 LSWT static susceptibility
`χ_long = 1/K_long = 1/(√38 J)` (KK-safe, FDT-free) — but it is WRONG-OBJECT for the one usable
anchor (KSS/GW = shear viscosity η, a stress-tensor transport coefficient; the datum is the
order-parameter magnon susceptibility χ_θθ — SAME cell layer, DIFFERENT operator/channel,
bridged only by the unbuilt kernel). So the usable-anchor count stays 1 (rank-deficiency
unchanged); the datum is instead channel-MATCHED to the K_c structural-target row (its bare
static-susceptibility companion; the kernel must soften it by the `(19/2)√38` factor). The next
anchor attempt must target the STRESS-TENSOR / shear channel to be KSS-matched. See N43.

---

## Maintenance protocol

When the framework closes an open value (or an item moves between gates):

1. Update its row here.
2. Update the corresponding R-NNN row in Section 1 (Result Index) (tier change).
3. Update its position in Section 2 (Dependency Graph) (Layer 2 → Layer 1 if closed).
4. Bank the new derivation in `twt.py` + add a check to `twt_test.py` (CLAUDE.md §6).
5. Record in `Annex N.G — Development log` in the paper.

---

# Section 5 — Geometric reinterpretation catalog (nine items)


The framework's central kind of contribution is **geometric reinterpretation**: taking a known
SM identity or unexplained feature and supplying a structural derivation from the substrate that
leaves the numerical value unchanged but shifts the ontological status from input to consequence.
This annex consolidates the full catalog. The six representative headlines also appear in §E.4.1;
the four additional catalog items below complete the inventory.

**Convention.** "Substrate" generally denotes the *cell layer* — the D4 cell lattice with `J`, `D`
couplings and the `Cl(4,0)` rotor algebra. The fundamental Planckian grain layer is the
substrate's other scale; it enters reinterpretations primarily via the gravity-related items.

### Catalog item 1 — Tsirelson bound `S = 2√2` as the fingerprint of S³ → S² projection (§B.4.2)

Numerically `2√2 ≈ 2.828`, the standard QM upper bound. **Reinterpretation:** the half-angle
`cos²(θ/2)` that produces it is the rotor sandwich on a `Cl(4,0)` spinor — a substrate-level
geometric fact, not an axiom of Hilbert-space formalism. QM gets the same value by axiom; TWT
supplies the substrate reason.

### Catalog item 2 — Weinberg `sin²θ_W = 3/8` at unification, native (§C.4.5)

Numerically the standard GUT-scale value. **Reinterpretation:** forced from three substrate
ingredients — D4 trivector charges, the Clifford trace bridge giving native `√(3/5)`, and
`g_1 = g_2` from D4 isotropy — without any SU(5) embedding. The historical `24 = z(D₄) = dim
SU(5)` is a representation-theoretic match, not a load-bearing identification.

### Catalog item 3 — Bohr radius `a_0 = λ̄_C/α` (§B.5b)

Numerically a definitional identity of ordinary QM. **Reinterpretation:** in standard QM,
`a_0` and `λ̄_C` are kinematic length scales of a point-like electron, and their ratio is `1/α`
by definition of `a_0`. In TWT, `λ̄_C` is the **L-orbit soliton core size** (a real field
structure of §C.1.6) and `a_0` is the **resonant cavity scale** (the standing-wave mode of the
same L-orbit field in the nuclear Coulomb potential). Both are actual geometric scales of one
field. Their ratio `1/α` is not a kinematic accident — it is a ratio between two physical
configurations of the same matter field. The numerical value is unchanged; the *ontological
status* of the relation shifts.

### Catalog item 4 — GA Maxwell `∇F = J` and the no-monopole result (§B.5)

Numerically standard Hestenes-form electromagnetism. **Reinterpretation:** TWT inherits the
geometric-algebra formulation directly. The no-monopoles result has the same status as `∇·B = 0`
in standard EM — a consequence of the *source* being grade-1 only, not of `F` being a bivector:
geometric-algebra electromagnetism *with* monopoles keeps `F` bivector and adds a grade-3 source,
`∇F = J − I_4 K` (Hestenes), and the engine confirms the slot is there to fill —
`maxwell_grade_structure` returns `∇F ∈` grades `{1, 3}` with **four** grade-3 components, not
zero. What TWT *adds* is a structural reason for the field/source grading: `F` is grade-2 because
EM acts on observers via the spatial bivectors `γⁱ = e_4 e_i` of §A.5; the wavefront current `J`
is grade-1 because it is the wavefront projection of the soliton's substrate-level *bivector
winding*, and a grade-2 → grade-1 projection cannot produce grade-3 content, so `K = 0`. "No
magnetic monopoles" in TWT therefore rides a substrate-level *identification* of the source —
conditional, and refillable by a different source identification — not an algebraic forbiddance
(§B.5.2, corrected 2026-07-28).

### Catalog item 5 — `α` as a reactive grade-0 Clifford invariant (§B.5b)

Numerically `1/α = 137.036` is what QED measures; TWT does not change it. **Reinterpretation:**
the `α`-object is identified as

> `α-object = ⟨Σ̃_F · Γ_recon · Σ_L⟩_0`,

the grade-0 projection of a geometric product in `Cl(4,0)`: `Σ_L` is the L-orbit bivector
winding, `Σ_F` is the photon bivector-strain mode, and `Γ_recon` is the §B.1 wavefront-locking
reconversion. This is a **reactive grade-0 Clifford invariant** — representation-independent,
picking out the common bivector content of the L-orbit field and the EM strain. Type-B (analytic
at coupling, no `exp(−S)` essential singularity; the probability ↔ action lens of tunneling does
not apply to `α`). The **length ladder** `r_e = α λ̄_C`, `a_0 = λ̄_C/α`, `r_e · a_0 = λ̄_C²` is
**definitional arithmetic**, not a coherence success: `r_e ≡ α² a_0` and `λ̄_C ≡ α a_0` hold by
the definitions of those lengths, so the three lengths are three parametrizations of one scale
rather than three independent measurements, and `α` cancels in `r_e · a_0 = λ̄_C²`. The wording
"one geometric overlap underlies three independently-measured lengths" is **withdrawn** (§B.5b.1;
R-035c row, demoted 2026-07-28). It is also not a value over-determination of `α`.
**Magnitude #1-gap-gated** via `Im χ`; what's DERIVED is the *ontology* (what `α` *is*), the
*category* (reactive Type-B), and the *coherence* (one object, several roles).

### Catalog item 6 — Frobenius generation count (§C.3.8)

Numerically standard mathematics: only `ℝ`, `ℂ`, `ℍ` are finite-dimensional associative real
division algebras. **Reinterpretation:** TWT identifies the three generations with the three
imaginary units of `ℍ` on the `V_4⊥` generation circle. Re-scoped 2026-07-31 (C-1): the *count*
exclusion is `dim Λ²₋(ℝ⁴) = 3` — generic-given-4D, computed in-engine — while Frobenius forbids
enlargement only through a named **associativity premise** (drop it and the octonions offer
seven units). What TWT supplies is the identification plus that premise, honestly counted.

### Catalog item 7 — Parity violation and β-decay share one substrate parameter D (§C.5.3, §C.5.7)

Numerically a known SM observation: weak interactions violate parity; β-decay creates `e^-` +
`ν̄_e`. **Reinterpretation:** both ride on the same `D` coupling. The 4 no-shared-index
`e_4`-bonds generate a topological boundary term `𝓛_top(D) ∝ D · I_4 · …`, proportional to the
pseudoscalar, which under spatial parity reverses sign — sourcing parity violation. The same
boundary term provides the substrate channel for β-decay's L-pair creation through the `I_4`
Hodge map. **One number, multiple manifestations** — the same `D` that produces the Cabibbo
angle, the generation phase, the Skyrme stabilizer, parity violation, and β-decay.

### Catalog item 8 — The electron's smallness (§C.1.6, §C.3.6)

Numerically `m_e/m_τ ≈ 2.9 × 10⁻⁴`. The SM treats this as a free fitted Yukawa coupling.
**Reinterpretation:** the electron is light because the substrate's chirality is *near, but not
at*, the leading-order massless balance `D = J`. The substrate-level mechanism is QCP scaling
of the L-orbit kinetic stiffness near the chirality-frustration balance: at L1,
`f_L = f_π · (1 − D/J)^{9/2}` from D4 DQCP universality (R-055). The L-orbit electron itself is a
topological defect — a vortex in the canted FM vacuum's residual `S¹`, equivalently a
Skyrme hedgehog in `SU(2)_L` via the Hopf fibration with `H = 1`. The SM's "free Yukawa" becomes
the substrate's QCP scaling near the chirality-frustration balance.

### Catalog item 9 — The Lorentzian signature of observed spacetime (§B.1)

Numerically the `(+, −, −, −)` signature universally used in relativistic physics.
**Reinterpretation:** *not* an independent postulate. The induced spatial frame
`γ⁰ = e_4`, `γⁱ = e_4 e_i` on `Cl(4,0)` satisfies Dirac relations with signature `(+, −, −, −)`
— engine-verified. The Lorentzian signature is the *algebraic shadow of a wavefront-locked
observer in a Euclidean substrate*, the conjunction of an algebra-level theorem (`Cl(4,0) ≅ Cl(1,3)`)
and a labeled stipulation (the observer reads `e_4` as time). Two of the most foundational
features of relativistic physics — the signature and the conserved charge spectrum — fall out of
the substrate algebra.

### The pattern

Each item turns an SM postulate or unexplained feature into a substrate consequence. The
numerical value is typically unchanged; the *ontological status* shifts. The few new predictions
(§E.2.2 CANDIDATE, §E.3 falsifiers) are secondary to this structural reorganization. The catalog
is the framework's primary kind of contribution.

---


---

# Section 6 — Methodology principles (eight)

The framework's open-items and tier-tagging discipline rests on the following principles,
recorded here so a reader can see how the status of each entry was determined. Mapping to
current canon is given inline.

**The apparatus these principles run on is published separately** — the complete research
operating system (the rule sets, the role definitions with their deliberately different
information diets, the banking and record-invariant gates, the honesty telemetry, and the
versioned worker-formation prefix) is at **https://github.com/yaerhf/research-ratchet**, as it
actually runs. A reader who wants to audit not only the results but the *process that admitted
them* — which verdicts exist, what a claim must survive before it is recorded, and what a
recorded reversal looks like — will find every instrument there, each with the measured incident
that motivated it.

**1. Tiers.** Every quantity carries exactly one tag from the scheme DERIVED-A / DERIVED-P /
DERIVED / INPUT / FIT / GATED / FRAMING / CANDIDATE. Earlier versions used a coarser scheme
(PREMISE / DERIVED / INPUT / SCAFFOLD); the current finer-grained scheme captures more cases
honestly. *Canon §2.*

**2. Over-determination is the test of an input.** A calibration tests the framework only where
the calibrated quantity is over-determined — forced to serve several independent observables
with no further freedom. Run consistency *before* attempting to force a magnitude. Pre-register
PASS/FLAG/FAIL bands BEFORE the computation, on a principled basis; a passed over-determination
is tagged INPUT, over-determined, NOT DERIVED — the value remains an input; what passed is its
consistency across roles. *Canon §0a: "actively seek the second angle — a cross-checked fit is
worth far more than a lone one."*

**3. The categorical / SSB escape.** Pre-registration discipline carries an explicit escape for
outcomes that are *categorical* (a fork) or *spontaneous-symmetry-breaking* rather than a
continuous value: report **not-applicable with a physics ruling**, not goalpost-moved into a
continuous bin. *Canon §2 "menu vs pick": geometry offers a menu, nature picks one — the pick
is INPUT, the consequences are DERIVED.*

**4. Force structure, not magnitudes (first).** Forcing is appropriate for *structural*
quantities (counts, geometric factors, symmetry-fixed ratios — e.g., three generations, the √2
factor, `sin²θ_W = 3/8`). For *magnitudes*, the order is: map and check consistency first, force
only after the consistency scan is clean AND a substrate-native handle for the magnitude has
appeared — one derivable from the framework's own premises without importing an outside
mechanism. *Canon §7 Layer 1 vs Layer 2 fault line, and the canon "derived-vs-generic"
pressure-test.*

**5. Two independent builds.** Any load-bearing result is built twice independently and
reconciled stage by stage. The discipline catches normalization conventions, sign errors, and
branch-of-inverse-function errors that look right on a single pass. *Canon §8a: adversarial
review via the twt-reviewer subagent + iterate-to-consensus loop. The current implementation
runs the second build in a fresh-context agent attacking the failure modes.*

**6. Coherence-as-falsifier scoring.** When a fork between two readings is open and both
alternatives predict the same coherence between two observables (likelihood ratio ≈ 1), then
observed coherence is **a consequence, not fork-validation** — it shows the observables are
related (undoubted under either reading), not which reading is correct. Score such a check as
a *potential* falsifier only: if it closes, "consistent with the selection," never "validates
it." **Incoherence is far more informative than coherence.** The genuine discriminators in such
forks are (a) breaking the symmetry between alternatives via an independent prediction one fork
makes and the other does not, or (b) an independently-anchored or derived underlying object
that threads all the footholds *without freedom* — where structural rigidity bites (see #7).
*No canon successor* — operative only by being recorded here. Load-bearing for the framework's
adjudication of open forks (e.g., the fading-vs-rich §D.5 memory kernel).

**7. Over-constraint of a free function requires structural rigidity, not channel-counting.** A
*free function* (e.g., an undetermined kernel like `Im χ`) cannot be over-constrained by
point-counting — finitely many sampled values are always interpolable. The over-constraint's
teeth come from the function's *structural* constraints: analyticity (Kramers–Kronig),
positivity (KSS-type floors), and sum rules (fixed integrals from short-distance / equal-time
data). These constraints limit how the function can *bend between* sampled points — that
rigidity is the only thing that can make sampled values mutually inconsistent. **A could-fail
consistency check is therefore real iff the structural rigidity is actually invoked** (which
requires the constraints' own inputs: sum-rule values, a static-susceptibility datum for KK,
tight rather than order-of-magnitude brackets). *No canon successor* — operative only by being
recorded here. Load-bearing for the §E.3 VG-1 `Im χ` falsifier budget and any future
construction that claims to over-constrain a free kernel from a finite set of value-checks.

**8. Import registry — mandatory on import (coordinator-directed, Yaer, 2026-07-05).** Any use
of an EXTERNAL theorem or result whose conclusion is load-bearing (positive, negative-closure,
or defensive) MUST, in the same banking pass, add or update its row in **Section 13 (Import
Registry)**: the premises the theorem needs, the level it is applied at (substrate vs
inside-frame/effective — the jurisdiction discriminator), the premise status on the ontology
(JUSTIFIED / NAMED-CRACK / OPEN / N/A), and the retirement handle. **An unregistered import is
a banking-stopper, the same class as a phantom cite** — the suite cannot catch it, so the
discipline must. Exemption: pure mathematics whose hypotheses are engine-checkable substrate
facts (homotopy, Schur, Derrick, Frobenius, linear algebra) is not an import. Before REUSING a
registered import in a new result, read its row — the ontology status and premise caveats
travel with it. **Excisability is part of the rule (Section 13.4):** the row's Used-at column
must stay the complete blast radius, every dependent result must carry a conditional tier + a
named revert clause, and paper use-sites carry an import notice — so that a wrong import is
excised by striking the row and firing the revert clauses, with nothing else in the corpus
moving. *Canon §2 successor (fourth error-avoidance rule, added same day).*

**Net.** Principles (1), (2), (4), (5), (8) have current canon successors. Principle (3) is
implicit in canon §2's menu/pick framing. Principles (6) and (7) have **no canon successor**
and remain operative *only* by being recorded here. They are load-bearing for the framework's
current adjudication discipline and were the motivating reason this annex was preserved.

---


---

# Section 7 — Development log: V1 → V2 → V3

The framework's development history. The paper body does not narrate its own history; this
annex does.

### G.1 V1 → V2

V2 (2026-06-29) installed:
- **The matter-as-defect ontology (§3.2).** V1 carried an implicit "matter is localized
  stuff" reading; V2 made matter explicitly a topological defect / driven attractor in the
  rotor field, with the inside-frame "positive contrast" and outside-frame "hole" reading as
  frame-images of one circular winding. This unblocked five derivations V1 was leaving
  asserted: M-4 (Q_u/Q_d charge-split coherence under up/down mirror), W-LIVE-2 (up = SD),
  W-LIVE-3 (rich/hysteretic memory kernel adopted on physical motivation), W-LIVE-5 (baryon as
  one defect with three orthogonal facets), W-LIVE-6 (V−A from SD half-module kernel).
- **D/J decoupled from Cabibbo per Q1 (2026-06-29).** V1 calibrated D/J via the Cabibbo angle.
  V2 corrected this: D/J calibrates to the *lepton* sector via Brannen `δ_L = 12.73°`, with
  the baryon-side `√18/e` as an independent cross-sector check. The Cabibbo prediction lives
  at §C.3.10 as the frequency-ratio `|V_us|² = m_d/m_s`.
- **Willis-gear metaphor removed.** V1's quantitative mass machinery used a "gear" language
  that read as a model dependency on a constructed apparatus. V2 retired the metaphor; what
  it was paramaterizing — the V2 §3.2 three-facet structure — was the actual content, made
  explicit.
- **Weak-sector derivation arc.** V2 established that `weak = SD` is the weak sector's single
  INPUT bit, with V−A, generation-blindness, the doublet structure, and `up = SD` all derived
  from it.

### G.2 V2 → V3 (this paper's restructuring)

V3 (2026-06-30) installed:
- **SOLID → SPECULATIVE arc.** Traditional foundational papers run axioms → consequences →
  open problems. V3 inverts: ontology in plain language (Part A), spine results delivered
  first (Part B), SM-structural derivations next (Part C), substrate engineering and the #1
  gap (Part D), open frontier (Part E). The reader meets the framework's strongest content
  first.
- **Result Index discipline.** Inline tier tags (`[DERIVED]`, `[FRAMING]`, `[CANDIDATE]`,
  ~152 in V2) removed from prose; every numbered result lives in Section 1 (Result Index)
  with tier, engine primitive, dependencies. The body reads cleanly; the Index handles the
  bookkeeping.
- **L/Q vs SD/ASD distinction restored.** V2 §8.4 stated correctly that the bivector
  orbit-split is not the chiral split. V3 §A.5.2 adds the *missing bridge* — the
  symmetric-pair Cartan relations + Spin(3) ↪ Spin(4) ↠ S³_𝓠 fibration with
  `π_2(Spin(3)) = 0` giving `0 → ℤ → ℤ × ℤ → ℤ → 0`, so the orbit basis `(n_𝓛, n_𝓠)` is a
  change of basis from the chiral basis. V3 §C.1.3 + §C.1.4 carry the subgroup-vs-coset
  hedgehog distinction.
- **§D.4.6 vacuum-linearization rationale (not defect).** V2's compressed wording could be
  read as linearizing around a defect (a non-standard choice with shape-mode complications).
  V3 says explicitly: linearize around the canted vacuum in the twist-gauge; a defect, when
  present, sources a classical `V(x)` on top of the same free wave operator.
- **§E.3 falsifier consolidation.** V2 had scattered falsifiers across the body; V3 collects
  the named near-term (16 since the 2026-07-27 LV-row deletion; was 17 at V3 issue, 18 after R-159) + 7 removed
  + 6 value-gated (VG-6 added in the same pass) + 2 structural-coherence falsifiers at §E.3 alone. No falsifier sits forgotten in the middle of the paper.
- **§24 cosmology hooks promoted.** V2 buried "arrow of time as +e_4", "three asymmetries
  from one IC", Volovik dissolution of Λ, and the macroscopic-limit Eulerian reframing at the
  back. V3 §B.7 + §B.8 make these reader-facing hooks.
- **α/g sibling identification.** V2 mentioned `g² = 4πα / sin²θ_W` only as electroweak
  commentary. V3 §B.5b promotes it to a hook: given `sin²θ_W = 3/8` proven, g is α's
  algebraic sibling; the EW sector has one #1-gap-gated magnitude, not two.
- **Glossary, units convention, signature convention, methodology paragraph.** All stated
  once at the front.

### G.3 V3 review history — what the rounds caught

V3 ran through nine substantive review rounds. The catches:

| Round | Substantive catches |
|---|---|
| β-5 | L/Q vs SD/ASD bridge (the symmetric-pair / fibration mathematics V2 was missing). Restored. Plus subgroup-vs-coset hedgehog clause for §C.1. |
| β-6 | I_4 Hodge map signs (V2 had them under form-Hodge convention, V3 standardizes to Clifford-I_4·). Collins-2004 author list. ξ_eff vs ξ disambiguation. e_4²=+1 vs e_5²=−1 startling fact named. Units convention added. §D.4 forward-dependency flagged. |
| β-7 | Particle/antiparticle branches not "no ambiguity". Signature convention. û defined. E vs i = e_{12}. N_eff "O(100)" not "124". Substrate τ_5 ordering vs observer Lorentz ordering. Finkelstein–Rubinstein attribution. Maxwell-table units. Diff-invariance for the constraint. A-1\*/A-2\* asterisk legend. R-NNN sweep clean. |
| γ-5 | C.3.5 direction: D/J set from δ_L, not the other way. §D.4.6 actual vacuum-linearization. §D.2.3 wrong triple product. §C.3.10 percentage. §C.2.1 hypercharge labeling. D4 packing citation (Korkin–Zolotarev, not Cohn–Kumar). e ≈ 5.45. UHE-CR bracket lower bound. §C.4.5(ii) generic. §C.4.4 Casimir consistency check. |
| γ-6 | **Three algebra bugs caught.** Koide formula `(Σm)/(Σ√m)² = 2/3`, not the inverse. Foot 45° actual formula (Foot 1994). `(1+E)/2` not idempotent since `E² = −1`. Plus 10 minors. |
| γ-7 | **Two more structural fixes.** §B.2.1 + §B.3 vacuum-linearization propagation. **Cl(4,1) ≅ M_4(ℂ)** (not M₂(ℍ) ⊕ M₂(ℍ); the latter is Cl(1,4)). Spiral-vs-canting twist-gauge clarification. C.1.2 D/J specification. SM-19 list adds θ_QCD. |
| γ-8 | c = √2 self-contradiction (forced vs INPUT). Weak = SD circular argument (now: linked binary pair). GMN anti-circularity restored (Q topological, not Y := 2(Q − T_3)). B.3 vs D.4.6 reconciliation. Hedgehog σ neutral. E.4.1 sin²θ_W headline. D.4.2 e-value vs mass. Opening D4 packing. |
| γ-9 | **Restoration pass.** Θ_0 formula. Vector mesons. Confining string. Higgs/EWSB doublet condensate. Nucleon/Δ J-values. Front-embedding obstruction. Electron 9/2 derivation breakdown. 25-cell. Tunneling. Gauge-sector gate. Compton-screening. UV-completion argument. Uncertainty emergent. ν/e cross-check. 18-state count. LV-table Crab/LHC rows. Same-composition mass-difference table. BPST zero-mode counting. |

Three were genuine algebra bugs (Koide flipped, Foot wrong formula, `(1+E)/2` not idempotent).
Two were classification bugs (the L/Q triple product `e_{12}·e_{13}·e_{23}` actually equals
`+1`, not `−e_4`; Cl(4,1) is `M_4(ℂ)`, not `M_2(ℍ) ⊕ M_2(ℍ)`). One was the load-bearing Part B
→ §D.4 forward dependency that earlier drafts asserted without delivering. Several were
overclaim → honest scope shifts (M_0 ≈ 1% → ~8%; Casimir ratio independent → consistency
check; c = √2 forced → equivalent to INPUT). And one major silent-drop scan with three
worker-agents found ~20 additional substantive items beyond the user's own list, most of
which were restored in Phase γ-9.

### G.4 Phase-tracking (terse)

The numbered phases referenced in the body and above:
- **Phase α** — V3 scaffold, Result Index seed, dep-graph and engine-map skeletons.
- **Phase β** — Parts A + B prose drafted; user revisions (α/g hook, A.4 reframe, Cl(4,1) addition); three review rounds (β-5, β-6, β-7) producing the bugs/clarifications/restorations above.
- **Phase γ** — Parts C + D + E prose drafted; four review rounds (γ-5 through γ-8); restoration pass (γ-9).
- **Phase δ** — these annexes (current).
- **Phase ε** — final cross-check.
- **Phase ζ** — archive V2.

The V1 Phase-G/M/N/O markers from V2 prose ("restored 2026-06-30 per Phase G audit SS-X" etc.)
referred to development phases internal to V2's own rewrite cycle. They are not preserved
verbatim here — the substantive content they referenced has either been integrated into V3's
body (most cases) or named in §G.3 above. The literal phase-tags are V2-internal bookkeeping
that the V3 body no longer carries.

### G.5 What V3 is honest about not deriving

For completeness: items the framework *does not yet derive*, named here once instead of
distributed across sections, with their gates:

| Item | Gate | Section |
|---|---|---|
| α_em, g, α_s, α_W magnitudes | Im χ (#1 gap) | §B.5b, §D.5, §E.2.2 |
| Decoherence rate 1/T_2 | Im χ | §D.5.5, §E.3 VG-3 |
| Cosmological-constant residual Λ ~ H² | Im χ | §B.7, §E.1.1, §E.3 VG-2 |
| CKM hierarchy + Jarlskog | Θ_rel | §C.3.10, §D.5.6 |
| Asymptotic-freedom β_3 sign | Θ_rel | §C.5.2, §E.2.2 |
| Absolute mass scales (f_π MeV, m_e, m_ν) | absolute ω | §E.2.2 |
| Higgs VEV v, Higgs mass | #1-gap | §C.5.3a, §E.2.3 |
| PMNS matrix | defused — no substrate prediction | §C.3.12, §E.3 RF-5 |
| Top quark mass | TWT-abstains | §A.4, §C.5.9, canon §5 |
| Dark matter (~98% of Ω_DM) | out of V3 scope | §E.1.3, §E.3 VG-4 |

The framework's posture is *claim the structure, not the magnitudes*. Part B's spine results
are structural derivations that survive the gap; Part C's SM-structural arc carries a mixed-tier
inventory; the magnitudes are honestly named OPEN in Section 4 (Pending-Values Registry) above.

### G.6 What V3 contributes over V2 — summary (moved from paper §E.4.3)

The V3 body focuses on the physics; the administrative summary of what V3 changed lives here:

- **SOLID → SPECULATIVE arc.** The traditional foundational-paper shape (axioms → derivations →
  open problems) is honest but forces the reader through machinery before meeting the result.
  V3 inverts it: ontology stated in plain language (Part A), spine results delivered first (Part
  B), SM structural derivations next (Part C), substrate engineering and the #1 gap (Part D),
  open frontier (Part E). The reader meets the framework's strongest content first.
- **Result-Index-as-discipline.** Inline tier tags removed from prose; every numbered result
  lives in the Result Index (Section 1 of this companion) with tier, engine primitive,
  dependencies. The body reads cleanly; the Index handles the bookkeeping.
- **Consolidated falsifier table.** §E.3 is the single home for all falsifier-tier content. No
  falsifier sits forgotten in the middle of the paper. The E.3 disclaimer (added 2026-07-01)
  frames what "falsification" means for a framework under active construction.
- **Honest reporting throughout.** Mixed-tier sections (e.g. §C.3 lepton-mass triplet at
  FIT-tier post WP-MASS-MEASURE) are flagged in prose without disguising; the Index resolves any
  ambiguity.
- **Companion file consolidation** (this file, 2026-07-01). All annexes and back-of-book
  bookkeeping consolidated in one out-of-paper location so the paper file is pure physics
  narrative.

### G.7 De-residue pass (2026-07-26) — audit-trail material relocated from the paper body

A style audit (2026-07-26) found the paper body had accreted ~20–25k chars of inline
audit-trail residue during the 07-02..07-06 banking week: dated verification/supersession
notes, engine primitive names, worklist/ledger IDs, and review-process language — against the
V3 design rule that bookkeeping lives in this companion. A de-residue pass rewrote the affected
passages to state the current physics directly (R-cites kept; no physics content removed) and
relocated the audit-trail material here verbatim, grouped by paper section of origin. The same
pass fixed the errors caught by the audit (logged at the end of this subsection). Nothing in
this list changes any result's tier or scope; the Result Index rows remain authoritative.

**Dated supersession/status notes (removed from body; physics restated in place):**
- §A.4: *"(Superseded gloss, 2026-07-02 — R-127, §B.3.1: for the observer-visible mass phase
  the axis is NOT free and NOT E. … E retains its global/colour complex-structure role.)"* —
  the passage now states the R-127 lock directly; the pre-R-127 claim ("û can be taken as the
  central element E") is retired from the body.
- §A.4: *"(Sector-split note, 2026-07-02 sweep — R-127/R-128 at §B.3.1: … engine shows the
  Hodge-dual axis is excluded there …)"* — now stated directly as the sector-split.
- §B.2.1 (R-123): engine cite `defect_rotor_frequency_reads_as_k4_on_front`, banked
  2026-07-02; "engine-exact on generic configurations"; the residues' FRAMING tier note; and
  the nested status insert *"(Residue-(ii) status, 2026-07-04 — R-142: the (H2) core is
  answered at the structural level — label half closed via the clock-orbit identity;
  uniqueness conditional on the named (Q)+(S)+(M) set with certified static slices; residue
  (ii) reduces to the kernel-face set + the anchoring face)"*.
- §B.3.5: worklist ID W-LIVE-4; engine cites `skyrmion_collective_quantization_under_v2_3p2`
  and `colour_z3_holonomy_cannot_source_fr_sign`; ledger N35; route W1 "reduced on
  2026-07-02"; the D'Hoker–Farhi/Witten import's "cited to-be-verified" status (tracked in
  Section 13).
- §B.3.6: worklist ID WP-TUN-1, "resolved 2026-07-06", engine cite
  `tunneling_evanescent_decay_constant`; the superseded V2-era figure was "5% in the
  deep-tunneling regime `V_0/E ≥ 5`".
- §C.2.3: the su(2)-identification caveat was recorded as *"Reconciliation note, 2026-07-02
  sweep"*, resolution deferred to "a future pass".
- §C.1.2 (R-051): *"(re-verified by an independent in-engine solve, 2026-07-03: 36.46, with
  the Derrick virial E2 = E4 holding at the minimum to <0.1%)"*.
- §C.1.2 (R-133): the Θ₀ coefficient was "**corrected 2026-07-03, R-133**, from the
  long-banked 97.27 — which equals 36.47·8/3 = 97.253 to within 0.02%, an unexplained
  algebraic relation to the mass coefficient, not an inertia integral; … the truncated-grid
  route shows how a spurious ~97 arises".
- §C.1.2 (R-135): certificate "Derrick virial ~3×10⁻⁶"; the forward-duplicated margin note
  "the margin survives across the entire fork, widening at the probe couplings and reading
  1.87% at the refit couplings" (the margins live at R-137/R-138).
- §C.1.2 (R-136): "engine-symbolic" label; the Krusch-formula import "consistency-checked
  in-engine"; certificates "certified by the four-way B = 1 regression to R-133's 106.76, the
  exact axial identity V₃₃ = 4U₃₃, and vanishing iso–spatial cross moments"; the caps tier
  label "DERIVED-given-(Q)+FR"; the margin restatement "the classical margin barely moves
  across the fork, 1.89/1.96/1.87%".
- §C.1.2 (R-138): "The coordinator-approved refit"; the wording-reconciliation note "R-137's
  'widens' holds at the probe point"; the hedge-carriage note "the hedge on that face's
  'coincidence-riding' status is carried, not dropped".
- §C.1.2 (R-139): "all solved in-engine"; "the reviewer's box-size/refinement probe"; the
  worklist-drift narrative "the old worklist phrasing 'tensor force *from* D4 anisotropy' was
  drift — the framework's own η_DM entry always said …"; the row pointer "a named P2-5-gated
  row; ledger N39".
- §C.1.2 (R-144): engine cite `full_field_b2_below_threshold_sc1_datum`; "sympy identity";
  "after the reviewer's B = 1-side continuation probe"; "two recorded unwinding events …
  independently reproduced at review"; the caveat label `LATT-π₃`.
- §C.3.2/§C.3.3: the six-negative-routes record was cited as "per V2 §19.4" (archived; the
  companion rows R-065/R-066 carry it).
- §C.3.5 / §E.2.3: the FIT re-tiering was recorded as "under WP-MASS-MEASURE (the V2
  re-tiering of 2026-06-30, V2 Phase F)" / "post Phase F REFUTED".
- §C.3.8: engine cite `why_three_generation_triple` (Engine↔Paper Map row R-071).
- §C.3.9: provenance "V2 §17.4 reidentified …" (the reidentification history).
- §C.3.10: engine cites `cabibbo_transition_probability` and `quark_mass_reconstruction`
  ("which audits the dial count honestly"); the ε-rule provenance "(V2 §19.7)".
- §C.3.11: attribution "— engine `dressed_coupling`" for the disclaimed-coincidence quote;
  the closing "This is V2-V3 discipline."; in R-134: "per the 2026-07-02 sweep" and "ledger
  N12"; the engine's `dressed_coupling` return "5.37 at the rounded D/J = 0.79" (quoted in
  §C.1.2/§D.4.2; Engine↔Paper Map row R-107).
- §C.3.13: the seat notes were dated *"Seat sharpened 2026-07-02"* and *"Seat construction
  2026-07-05, W3.2/A2"* (worklist row); R-129's quoted status phrase "standing candidate
  seat, pointed to not confirmed"; the R-128 FRAMING-tier note; the N37 pointer
  (inter-generation running).
- §C.4.2: the V2-accounting history "V2's framing presented R-075 … and weak = SD … as
  separate facts … V3's accounting books them as one."
- §C.4.6: engine cites `D4_DM_bond_bivectors_non_commuting`, `d4_dm_plaquette_holonomy_explicit`,
  `d4_lattice_instanton_access_and_dm_background_neutrality`; timeline phrases "as of
  R-140/R-143", "the leg the R-140 fence left open"; worklist ID W-LIVE-4; neutrality detail
  "thousands of individually O(1) terms; per-axis-class blocks vanish independently; the
  variant-b convention is also neutral, by a separate numerical fact"; "(the reviewer's
  genericity probe, banked as a check)"; charge-operator qualifiers "integer arithmetic;
  pseudoscalar-pure"; certificate values "0.79 / 0.90 / 0.94 at instanton size ρ = 2/3/4 …
  the same operator reads the bare background at < 10⁻⁵"; the premise label "(a
  named-premise, located face)"; the sweep "0.78 → 0.63 from θ_D = 0.05 to 0.3".
- §C.5.2 (R-148): "engine-exact with the vertex sign derived in-suite"; "revert clause
  named" (Section 13, I-13); "credited".
- §C.5.3: the attribution history "V2 corrected V1's earlier overstatement; V3 preserves the
  corrected attribution." (also "preserved from V1 correction" in the header).
- §C.5.9 (R-091a): "was ≈ 6.5 before the R-133 Θ_0 correction — the exclusion
  *strengthened*".
- §C.5.10 / §C.5.3a: content provenance "(V2 §16.4)" / "(V2 §20.7)" (archived).
- §C.5.11: engine cites `meson_dynamical_current_split`, `meson_topological_status`.
- §D.2.6 / §D.3.1 / §D.3.2: provenance "(V2 §8.5)" / "(V2 §9.2)" / the V2-vs-V3
  naming-history framing of the monad note (V2 §9.3).
- §D.4.5 (R-133): "**corrected 2026-07-03, R-133**, from the long-banked 97.27 …"; the
  knock-on narrative "`Σ_c − Λ_c` moves from the accidental 171 MeV (2.4%) to 151.9 MeV";
  "the correction moved it from 215".
- §D.4.6: the appended insert *"(Handle FIRED 2026-07-03, R-132, §B.2.2: … the 'Euclidean
  engines cannot do hyperbolic' reading of the caveat was mis-scoped)"*; the insert *"Both
  answered at the structural level 2026-07-04, R-142: … the breathing-channel Hessian
  engine-certified strictly positive (~0.21, box-saturating)"*; the protection-class label
  WP-LV1; "carried honestly"; "engine-proved"; "the multiplicity gloss is prose, not an
  engine-backed count".
- §D.5.3: provenance "V2 W-LIVE-3 adopted"; the §E.5 pointer's "the companion Section 12
  Class-2b closure route, executed".
- §D.5.6: engine cite `theta_rel_z3_isotropy_dichotomy` (Engine↔Paper Map row R-118).
- §E.1.3: "no replacement has survived *adversarial* review"; "a sharpening banked with the
  negative".
- §E.2.2: the retired-row record "(The former β_3-sign row is retired: the
  reflection-positivity route closed as a banked negative — companion Import Registry row
  I-10 — and the sign face is now decided-conditional at R-148, §C.5.2.)"; the directive
  provenance "per V2 user-direction 2026-06-29".
- §E.3.2 (RF-6): the dev-phase stamp "(Phase D 2026-06-30)".
- §E.3.5: the banking date "(2026-06-28)" on the gravity structural-geometry closure.
- §E.5: campaign provenance "(2026-07)", "the GA-native `simulator/` subproject", engine cite
  `kernel_candidate_constraints` (×2), "adversarially reviewed to consensus and the corpus
  frozen throughout", the campaign grade "**Grade B**", "(two-commit, git-proven)", "the cull
  that removed the campaign's own reference kernel", "(the wavefront caveat the campaign's
  constraint records carry as their frame hedge)".
- Opening/front matter: the star-convention provenance ("stated in canon §0 but not in V2's
  original Opening; V3 promotes them …"); the canon cross-references (canon §0/§4/§5/§8a)
  replaced by in-paper or companion pointers; the Notation-table "Canon-§0" label.
- Small verbatim removals (recorded for zero-loss completeness): "Engine-verified for
  n = 2, 3, 4, 5" (§B.4.2, R-028); "(Engine: max |Ω(g_0 R) − Ω(R)| ≈ 3 × 10⁻¹¹.)" (§B.6.5,
  R-041); "three independent methods confirm the count" (§B.6.7, R-151); the engine-internal
  "fact (7)" pointer (§B.6.7, → `texture_frame_6to4_reduction`); the duplicated sentence "The
  Born rule's even-power structure is forced by chirality-reversal symmetry" (§B.3.3; stated
  9 lines above); the closing sentence "The rest of the framework is properly tier-tagged
  downstream." (§C.2.8); the duplicated "(companion Section 4)" pointer (§E.6); "sympy-exact"
  ×2 → "exact" (§B.6.6, R-145/R-149).

**Errors corrected in the same pass** (each verified against the engine or the file itself):
Notation δ_L row pinned to the calibrated `D/J ≈ 0.787` (0.79 gives 12.77°); §B.4 "singlet"
misnomer → "spinor"; "rotor sandwich's half-angle" → one-sided rotor action (§B.4.1 and the
§E.4.1 Tsirelson bullet, which also mis-cited §B.4.2 → §B.4.1); §B.3.1's stale "named open:
the baryon Q-orbit analog" (constructed in the next paragraph, R-128); R-038/R-039 cite swap
in §B.6.1; the §B.6.6 stale "named next handle" vs R-149-closed contradiction; §C.2.7
"remaining 14" → 13 Weyl states; R-064's malformed argument list → `A_k(c, δ) = 1 +
c·cos(δ − 2πk/3)` (engine convention); "have all investigated NEGATIVE" grammar ×2; "none of
which" → "neither of which"; §C.3.8's false "four-dimensional associative real division
algebra … does not exist" → fourth imaginary unit / beyond-ℍ (ℍ itself is 4-dimensional and
exists); "the four-generation prediction" → no-fourth-generation; §C.3.10's "0.973/0.344 =
2.83 — a 0.6% match" → ε_u is *set by* the rule (engine: replaces the tautological check; the
raw ratio agreement is ~0.02%, and "0.6%" was bleed-over from the Cabibbo figure); broken
markdown emphasis in the §C.3.11 side note and the §B.2.1 nested italics; §C.4.6 header/count
"three legs / Three sub-questions" → four (populated added); SU(2)_+ / SU(2)₊ notation
unified; §C.5.10 "monad-exclusion" → cell-exclusion (two-scales discipline; the
reconciliation sentence remains the one place the monad-scale tie is stated);
Cohn–Kumar–Miller–**Parker**–Viazovska → **Radchenko**; §D.4.5's wrong Λ_QCD pointer
"(§C.5.2 / §D.4.1)" → R-111; §D.4.6's misquote of §B.3.4 aligned to the actual sentence;
"(§C canon holds)" → §A.4's mass-scope rule; §E.2.3 "four CKM angles" → four CKM parameters
(three angles + one CP phase); §E.3.1 rows 9/10 bound-direction wording aligned with the
rows' own kill conditions (floor, not ceiling) *[row numbers as of that pass — these are rows
7/8 after the 2026-07-27 deletion of the two LV head rows]*; row 10 / VG-1 Bell-memory-bridge cites
§B.4.4 → §B.4.5; RF-5/RF-6 grouping sentence corrected (RF-6 is an adjudicated negative, not
a clarified-status removal); `2 × 36.462 = 72.923` → `≈` (last-digit rounding); the
`#1-gap-gated.`-at-column-0 line starts re-wrapped (fragile in permissive Markdown); §C.1.6's
9/2 counting and the C.1.6 status sentence now carry the `K_c = (2/19)·J` conditionality the
engine records (DERIVED-conditional, not unconditional).

The full audit note (first pass + workflow findings) is archived at
`knowledge/audit/paper_audit_note_2026-07-26.md`.

---

### G.8 Lorentz-violation correction pass (2026-07-27) — the citation sweep's largest catch

**How it was found.** Not by an internal audit but by the citation sweep: checking what Liberati
2013 and Stecker 2009 *actually say* (read as primaries, not via a search summary) against what
§E.3.1 row 1 claimed they say. The paper's flagship near-term falsifier compared a **dimension-six**
prediction against a **dimension-four** bound and reported the result as "at current bounds". The
correct dimension-six comparison excludes the naive coefficient by three to nine orders — re-stated
as **two to ten orders** after the 2026-07-28 Λ-bracket audit widened `Λ` to `[0.13, 2.5] M_Pl` (a
reduced-vs-non-reduced `M_Pl` unit fix plus an OPEN three-way `c_reg` disagreement; see R-037).
*(Subsequently: the disagreement RESOLVED 2026-07-29 — one `c_reg` in three `Λ`-variables — and the
2026-07-30 which-Λ ruling re-cut the naive value to `η⁽⁴⁾ ∈ [1.9, 6.7]` / three to nine orders on
the `Λ_L = 1/a` band, retiring the wide bracket.)*
Escalated
to adversarial review under canon §8a rather than patched in place, because it is a physics
adjudication, not a citation fix; verdict and verbatim replacement wording at
`knowledge/audit/UHECR_VERDICT_2026-07-27.md`.

**Provenance of the error — drift, not fabrication, and worth recording as such.** V1 wrote a
matter-sector range "`|δ| ≲ 10⁻¹⁵` to `10⁻²⁰`" and claimed agreement "within 3 orders" against the
`10⁻²⁰` end. V2 lowered `Λ` to `0.16 M_Pl` and promoted the **loose** end of that range to "the
tightest matter-sector bound". Both ends were dimension-four Coleman–Glashow-class figures. No step
was dishonest; the composition of two reasonable-looking steps produced a claim neither step
supported. This is the failure mode the sweep-after-patch rule exists for, appearing across
*versions* rather than across sections.

**The tier finding underneath it.** `(E/Λ)²` appeared four times in the paper and **zero** times in
the companion — no R-NNN, no tier, no engine cite — while `Cl41Wave().wave_speed_c()` raises
`UnderivedError`. The row was using a numerical consequence of a GATED object by silently setting
its coefficient to 1. Canon §2's "you may not use it by accident" was defeated because the *number*
travelled into the paper while the *object* stayed behind in the engine. Bookkeeping lesson: a bare
numeral with no companion row is exactly as dangerous as a phantom engine cite, and the suite cannot
catch either.

**The correction is not uniformly negative.** The same pass found the paper *underselling* its own
protection. D4's bond-set fourth moment is exactly isotropic (`M_1111 = 12 = 3 M_1122`, residual 0),
which `Z⁴`'s is not — so rotational anisotropy is pushed to dimension **eight**, `(E/Λ)⁴ ≈ 7×10⁻³⁰`
(evaluated at the then-current loose corner `Λ = 0.16 M_Pl`; `≈ 1.6×10⁻²⁹` at the 2026-07-28 widened
bracket's loose corner `Λ = 0.13 M_Pl`; `≈ 2.0×10⁻³¹` on the ruled `Λ_L = 1/a` band after the
2026-07-30 which-Λ ruling, and smaller at each tight corner),
one order of protection better than claimed, and substrate-specific rather than generic. What is
unprotected is the *rotationally invariant* dimension-six term, which is neither a relative-boost
observable (so R-016 misses it) nor an anisotropy (so D4 misses it). Separating those two objects is
the whole content of R-165.

**What the implementation review then changed (canon §8a, second round).** The reviewer was asked to
attack the implementation, not re-litigate the verdict, and it did two useful things in opposite
directions. It **strengthened the positive half**: the dimension-eight claim had been argued from a
nearest-neighbour Laplacian — a *model*, and therefore exposed to canon §3 — when the real reason is
representation-theoretic and model-free. `Aut(D4 root system)` has order 1152 (it is `W(F4)`, invariant
degrees `{2,6,8,12}`), so its degree-four invariant space is one-dimensional: symmetry alone forbids an
anisotropic quartic for *any* point-group-symmetric analytic kernel. The engine now computes the group
by closure and the invariant dimensions by Molien, so the argument is checked rather than asserted, and
the degree-six space being two-dimensional (plus an anisotropic sixth bond moment) makes dimension eight
*reached* rather than merely bounded — the claim is now verified on both sides. It also **weakened the
claim where it was over-stated**: the inference is conditional on two premises now named in the paper,
the docstring and the R-165 row — analyticity in `k` (a non-analytic memory kernel, i.e. the #1 gap
itself, escapes any polynomial-invariant argument) and the full point group including triality (the
reflection subgroup `W(D4)` alone has a three-dimensional degree-four space, and the second shell's two
sub-orbits cancel only at equal weight, so unequal weighting restores dimension-six anisotropy).

Four further defects the review caught, all fixed: a **normalization collision** — the paragraph defined
`η⁽⁴⁾` as the coefficient of `p⁴/M²_Pl` and then said "setting that coefficient to unity gives
`η⁽⁴⁾ = (M_Pl/Λ)²`", which is self-contradictory; the two conventions (`η⁽⁴⁾ p⁴/M²_Pl` versus the
substrate's own `c·p⁴/Λ²`, related by `η⁽⁴⁾ = c(M_Pl/Λ)²`) are now stated once and used consistently.
§B.6.4's margin was quoted at solar-system wavenumbers but claimed for the GW band too, where
`(k/Λ)²` is eleven orders larger — corrected to the LISA-to-LIGO range with the margin stated against
the actual dispersion bound, and the category slip fixed (the remnant is a *dispersion* correction, not
a mass term: it vanishes as `k → 0` and so cannot be what graviton-mass bounds constrain). §B.6.3's
"closed" anisotropy claim now carries the SC-2 pointer, since it is a monad-scale statement and the
cell-scale orientational-order question is separately open. And I-19 gained **premise (e)**: the
published bounds are inside-frame inferences about an outside-frame object, so the transfer rides the
un-built outside↔inside projection — the same hedge §E.3.1 rows 7–8 already carry. Naming the exposure
remains right (canon §0a); what is now honest is that its *bindingness* is itself conditional.

**What changed.** §E.3.1 rows 1–2 deleted and the table renumbered 18 → 16 rows, with every
cross-reference in the paper and this companion re-pointed; §B.1.5, §B.6.3 and §B.6.4 rewritten;
new value-gated falsifier VG-6; new internal-pre-mortem item §E.3.5(4), taking that section from
three items to four; the LV-EFT constraint machinery registered as import **I-19** (inside-frame
data bridge, sibling of I-6) with a revert clause; R-016 and R-039 cooled from DERIVED-STRUCTURAL to
the engine's own self-tag, with their dimension-four-only scope stated; new primitive
`d4_lattice_lorentz_violation_orders` (suite 438 → 448 across both review rounds); negatives ledger **N52**; COVER_NOTE §0's
"one falsifier sits at experimental limits" replaced with the honest statement that none does.

**A bookkeeping correction made in the same pass.** The stated primitive total (323) was found to be
over-counted by one against a direct `grep -c "^def "` of the committed engine (322). Adding R-165's
primitive made the stated number true rather than incrementing it. The count line now says to
*count* rather than increment at each banking pass.

**The framing that belongs in the record.** The framework was falsifiable enough to be caught by its
own citation sweep; the error is traceable drift rather than invention; and the correction
strengthens one claim while converting an overstated test into a named tension. The advertised
flagship near-term *test* is now the framework's most acute live empirical *exposure* — recorded at
§E.3.5(4) rather than omitted.

---

### G.9 De-historicization pass — the paper made history-blind

**The rule.** The paper does not narrate its own past: no revision dates, no audit or finding IDs,
no ruling stamps, no review-pass references, no "earlier revisions said X" narratives, no
version-compression stories, no process anecdotes. That role belongs to this companion — the
Result Index row notes and this development log. The paper states the **current** claim in a
straightforward voice, fully conscious of the **theory's** flaws (premises, conditionals,
exposures and open gaps are stated as present-tense facts about the theory) and unconscious of the
**document's** history.

**What changed, and what did not.** Roughly 150 sites were rewritten. Nothing was deleted that
carried physics, scope, or a conditional: every premise, posited/assumed/not-derived statement,
exposure, open gap, import notice and scope limit survives, restated in present tense. The live
cross-reference system is untouched — R-NNN, N-NN (negatives ledger, shipped with the paper), I-NN
(imports), the P-premise names, the VG-/RF-/SC- row IDs, all §-refs, and every prior-art citation
with its delta sentence. What went was the frame around them.

**The five recurring forms, and how each was rewritten:**

| form in the old text | rewritten as |
|---|---|
| a dated ruling stamp on a live convention (`which-Λ ruled 2026-07-30`, `coordinator ruling`) | the convention stated as the paper's convention, with the scoping argument intact |
| a retraction narrative (`earlier revisions said X; that is withdrawn`) | the current position stated directly and negatively where needed (`the descent does **not** give 0.231`) |
| a restoration narrative (`restored from V1 §N, deleted in the V3 compression`) | the restored content, unmarked |
| an audit/finding ID appended to a live caveat (`D-1, 2026-07-31`; `C-5`; `III-3`) | the caveat, ID removed; the ID lives in the Result Index row |
| a process anecdote (`its adversarial verifier died mid-response`) | the present-tense epistemic content (`this settlement has not been independently reproduced`) |

**Sections most affected:** §B.6.2/§B.6.3 (the which-`Λ` cluster, densest single site — the
three-pass normalization narrative and the explicit `(History: …)` parenthetical both removed, the
`Λ_S`/`Λ_L` split and every provenance fence kept); §C.4.5 (`3/8` run-down: the withdrawal
narrative removed, the negative statement and N55's four closed escape routes kept); §C.1.6
(`e_L`: the "two defects are now on the record" framing removed, both defects and the
OPEN-uncounted-input status kept); §E.3.1 rows 4/5 (the V1→V3 restoration story removed, the
QM-shared consistency-check character kept); §D.4.3, §D.5.2, §D.5.3 (restoration and
re-tier stamps removed, R-108/R-114/R-115 tiers unchanged).

**Structural removals.** The title block's version-and-revision line, and the "End-of-draft note",
whose content was entirely about the document's drafting state; the latter is replaced by a short
closing note pointing at this companion and the suite.

**Residue deliberately left in the paper** (each a judgement call, not an oversight):
- the probe-script path `knowledge/candidates/probes_2026-07-29/` at §C.4.5 — a repository
  artifact identifier and the reproducibility provenance for the four computed escape routes, not
  a revision stamp. Renaming the directory would make the cite date-free.
- Section 6's technical uses of "relabeling" (chiral basis → orbit basis, §A.2/§A.5.2/§C.1.3) and
  "restoration" (the units convention's local restoration of `c` and `ℏ`), which are physics
  vocabulary, not document history.
- "historical" where it refers to the *literature's* history (ANW's fitted `f_π, e`; the SU(5)
  translation at §C.4.7; the GUT-era leptoquark labels), not this paper's.

### G.10 The mass→weight empirical-jurisdiction block (I-23, added 2026-08-02)

**Coordinator-directed** (opening move of the gravity/inter-front arc): before the paper links
mass with weight, the reader is told which parts of that link are measured and which are
extrapolated — *"this 22-orders-of-magnitude extrapolation has quietly been forgotten by some
people... a lot of intermediate scale mechanisms can emerge in those 22 orders... It's not a
sure thing and we could end up discovering perfect additivity... But it's far from obvious."*

**What was added, in bank-before-cite order:** the engine ledger `mass_weight_empirical_chain`
(a jurisdiction ledger — deliberately OUTSIDE `eom_constraint_class`'s E-namespace, which stays
E1-only; never an Hn/R-NNN) + one suite check in the cosmo module (a duplicate-literal drift
guard + wording-guard: the 5.5×10²² proton-mass / 1.0×10²⁶ electron-mass gap factors recomputed
from the 92.1 mg Westphal source and CODATA-2022 masses; suite 463 → 464); the §B.6 intro block
"What the laboratory pins before mass is linked to weight" (two paragraphs, four links + three
link-attributed fences, placed before **Mathematical setting** so no heading/TOC surgery); the
Section 10 bibliography subsection (21 records); Import Registry row I-23 (Section 13.2 —
no-forward-exposure class, ontology status N/A).

**Cross-class review round (canon §8a; change-set Fable-authored, both checkers Opus):**
reviewer NOT-SAFE (7 blocking) + keeper COLLISION (2 hard, 2 structural) — all fixed same day.
The catches, so the lesson survives: (1) the block's first draft licensed a non-additivity
escape hatch ("collective sourcing has room to differ") that §B.6.6 itself denies — the banked
route COMMITS to per-particle additive `T_μν` sourcing (`m_i = m_g` forced, R-016/R-039; R-038
additive), and the honest statement is that this *commitment* is untested below 92.1 mg;
(2) "tree-level texture coupling vanishing **identically**" contradicted §B.6.6's own scope
correction (computed blocks only; `h₀ₖ` an open fork) and mis-cited R-146 — the same quantifier
the corpus had already withdrawn, plus the §B.6.1 frame note carried the same unscoped wording
pre-existing and was scoped in the same pass; (3) "5.5×10²² protons" was proton *masses*
(gold's actual proton count is 2.2×10²² — a 2.475× referent error at the headline number);
(4) `ħ` vs `h` twice (CGPM fixes `h`); (5) the "E2" identity was a category error against the
eom E-namespace (E1 = a ceiling that can refute a kernel; this ledger refutes nothing) —
label dropped; (6) I-23 sat in 13.1 asserting no forward exposure — moved to 13.2, status N/A,
with the frame-jurisdiction statement made explicit (fences bind the inside-frame effective
description; no outside-frame object bounded; I-19 premise-(e) not invoked); (7) the keeper
found the render script's suite-count drift guard DEAD (f-string print + de-historicization
killed both greps) — fixed in the same pass; and the R-038 companion-DERIVED vs
engine-FRAMING/CANDIDATE tier mismatch was surfaced and flagged on the row (reconciliation
owed, worklist). The keeper's open taxonomy question was RULED by the coordinator the same day:
the per-particle commitment **stays as bookkeeping** — no §E.3.1 falsifier row; I-23 is the
record. Programme posture set with the ruling: mass-mechanism (lab) and gravity-mechanism
(cosmos) are held to *compatibility, not perfection* across the 22-order gap.

**Verification provenance:** every number read from the primary record (journal/arXiv/INSPIRE/
BIPM/NIST) by two web agents on 2026-08-02. Two recall errors were caught and corrected before
anything was written: COW 1975 agreed at ~10% (54.3(2.0) vs 59.8(1) rad), not the often-quoted
1% (that belongs to 1980s refinements), and the spin-pendulum PRL is 97, 021603 (2006), not
PRL 100, 041101 (the Schlamminger Be/Ti EP test). Upgrades taken: Singh et al. 2023 (3.9×10⁻¹⁴
active/passive, 100× beyond Bartlett–Van Buren); Westphal source mass stated exactly (92.1 mg);
the Fuchs 2024 "milligram" result classified correctly (test mass, not source — the record
stands).

### G.11 The grain rename (2026-08-18)

The substrate's smallest constituent was **renamed monad → grain** family-wide (RUL-055,
2026-08-18; coordinator's ground: plain words over learned ones, and the Leibniz name-liability
retired). One sweep across the paper, this companion, the canon, the family tree, the charter,
the worklist and the handoff; the paper's §D.3.2 naming note carries the only present-tense
bridge ("elsewhere also called the monad"). **Nothing was renamed in code:** the two public
primitives `induced_G_only_monad_scale_enters` (main) and `generation_values_monad_forked`
(companion) keep their names — each now opens its docstring with the bridge line — and every
returned string literal / dict key containing "monad" is untouched, so no computation and no
suite check moved (416 MAIN + 87 COMPANION, both green before and after). Archives, dated
governing records, and the dev-log entries above are history and keep the old word.

---

### G.12 Phase-0 pass of the round-1 external review (2026-08-18)

The structure-independent half of the round-1 external-review action plan, executed on the paper
and this companion without touching a tier, a number or a claim's scope. Ten items.

**Four prior-art credits, each placed AT its claim site with a specific delta** (the round's
meta-observer verdict, Q1/Q2 and the §B.3.3 confirmation; every bibliographic record and every
characterization re-verified against the primary before writing, per the round's own R1 rule —
Crossref, INSPIRE, arXiv and the publishers' deposited metadata):

- §B.4 mathematical setting — **Mosseri–Dandoloff 2001** and **Urbantke 1991 / 2003** for the
  single-qubit `S³` / Bloch-sphere / Hopf geometry, credited as established literature (M–D is
  itself a review of the single-qubit case; its own new content is the two-qubit `S⁷`
  fibration). Delta stated: the *selection* of the complex unit by the defect background and the
  *physical* referent claimed for the `S³`.
- §B.4.1 — **Doran–Lasenby–Gull 1993**, with the 1996 review chapter (with Somaroo and
  Challinor), for the multiparticle spacetime algebra the CHSH calculation runs on. The corpus
  previously cited these authors only under their gauge-theory-gravity hat. Delta stated: which
  bivector is the complex unit, and that their construction does not supply the two-defect state
  space §B.4.1 records as missing.
- §B.3.3 — **Horwitz–Biedenharn 1984**, naming the complex-linearity ("complex geometry")
  condition *and what it is for*: it is what allows tensor products of quaternion modules to be
  built preserving complex linearity. This locates the missing multi-defect state space as a
  specific, already-studied construction rather than an open-ended absence.
- §B.4 opening — a one-sentence scope distinction from **Christian's** Clifford-algebra-valued
  local-variable programme: this framework evades no Bell premise and violates factorizability,
  the leg orthodox quantum mechanics violates. No position is taken in the dispute.

**Two integrity fixes.** §B.8.4 carried a text corruption — a paragraph opening mid-sentence at
"is not constructed in this paper;" with the block one parenthesis unbalanced; the lost head
("(*Honest scope.* The multi-defect `Cl(4,1)` wave equation with `N` back-reacting topological
sources") was recovered from the pre-V3 text and restored verbatim, and the block now balances.
§B.6.3's face table said bare **closed** for the dim-4 relative-boost row while its own §B.1.5
prose puts the radiative half on the OPEN import I-22; the cell now reads
"closed (tree-level, structural) / open (radiative, I-22)", matching its sibling row.

**R-049 demoted, not deleted** (coordinator ruling; lesson 7). The row's own triviality caveat —
the L/Q split *is* the `e₄`-content partition, so the two sortings agreeing is a definitional
observation — was already the authoritative content and stays. What changed is the standing: the
row is now **FRAMING**, its DERIVED-STRUCTURAL half is recorded as R-009's content rather than
its own, and the row states that it is retained as a definitional observation with nothing
downstream leaning on it. Verified by grep across paper, companion, both engines, both suites and
the ledgers: no primitive, check or result consumes R-049; the only reference is R-050a's
antecedent list, annotated in both rows as section-adjacent context. The paper's §B.8 callout
was cooled to match ("a definitional observation, not an independent coincidence"); the demotion
itself is not narrated in the paper.

**`f_π = 129 MeV` labelled, no identifier renamed** (coordinator ruling, the RUL-055 precedent).
Zero engine identifiers and zero returned values changed. The Opening's input list now states
once that `f_π` denotes the **ANW fitted** coupling throughout, ~30 % below the physical
`F_π ≈ 186 MeV` in ANW's own normalization, and that its resemblance to the measured
`f_π⁺ = 130.2(1.7) MeV` is a collision of conventions rather than agreement. The use-sites where
the fitted value feeds a *physical* estimate rather than an internal Skyrme relation are flagged
where they occur: §B.6.3's `(f_π/M_defect)²` defect form factor (and its §E.3 VG-6 restatement),
§C.5.3's `v/f_π ≈ m_p/m_e` near-coincidence, and §D.4.5's `1/Θ_0 ≈ 196 MeV`, which is quoted
inside the ANW scheme because `e` and `f_π` were fitted together. The bibliography's ANW entry
carries the full nomenclature caution with its primary sources.

**Coverage discipline, folded in while the files were open.** Markers restored: **R-071** at
§C.3.8 (the `dim Λ²₋(ℝ⁴) = 3` count, whose marker the generations narrative had lost) and
**R-167** at §B.3.1 (the `e₄`-commutant qubit, banked with the marker never placed). **R-150**
needed no marker and got none: its Result-Index row already declares it a dashboard, not
paper-body content, and that declaration is correct. Ten Section-3 View A rows were added for
primitives that had none — the four `kernel_candidate_*` / `kernel_composite_closure` rows,
`hierarchy_type`, `lambda_H2_dynamical_reading_excluded`, and the four primitives the paper body
names directly without an R-NNN (`e_i4_squares_to_minus_one`,
`koide_modus_tollens_consistency`, `pmns_no_substrate_derivation`,
`neutrino_orbit_asymmetry_attempt`) — and the ones that had been sitting in View A.Δ were removed
from it. Both count-bearing prose lines in Section 3 were refreshed **by counting**, not
incrementing.

### G.13 The archivist pass: two duplicated record IDs, and the invariant that now catches them (2026-08-18)

Structural hygiene only — **no claim, tier, scope or number moved except by counting.** Two
defects of one class were fixed in this file at the consolidation's archivist pass, and the
class was promoted to an executable invariant.

**The `I-23` collision.** Import-Registry ID `I-23` named **two different rows**: the measured
mass→weight chain (Section 13.2) and Collins–Perez–Sudarsky–Urrutia–Vucetich 2004 (Section
13.1). A dozen sites across the corpus cited "I-23" by number, so each of those citations was
ambiguous — and because Section 13.4's excision discipline is keyed to the ID (Used-at column =
the complete blast radius, plus a named revert clause), a duplicated ID makes a blast radius
uncomputable. Resolved by **priority of institution, established from the git record rather than
from section order**: the mass→weight chain was instituted 2026-08-02 and **keeps `I-23`**;
the Collins row was back-filled later, on 2026-08-16 under RUL-046, and **becomes `I-28`** — the
next free ID after the registry's then-highest, `I-27`. Every by-number cross-reference was swept
in reader order: this file (the row itself and the I-25 and I-27 rows, which both cite the
Collins row by number), the paper body's §B.6.3 percolation paragraph, the ruling register's
RUL-046 row (whose revert clause names the row), the engines and both harnesses (their `I-23`
citations are all mass→weight-class and correctly unchanged), the ledgers, the canon, the
worklist and the handoff.

**The duplicate View A row.** Section 3's View A carried **two byte-identical
`B_minus_L_anomaly` rows**, which is why its row count and its primitive count disagreed. The
duplicate was removed — the surviving row is the one inside the table's dominant
case-insensitive alphabetical run — and the count prose was refreshed **by counting**: 243 rows,
243 distinct primitives.

**The promotion (RUL-024 / canon §2's extension duty).** A drift class caught twice in prose is
a process failure, and this one was caught twice on one day. `scripts/check_records.py` gained a
**record-ID uniqueness** section covering import-registry IDs, View A primitive rows,
ruling-register IDs and the family tree's branch-node run, plus checks that Section 3's three
count-bearing sentences (View A rows, View A.Δ entries, the engine census) match the tree.
Every one of them was **negative-tested** — demonstrated to fail against the pre-fix state and
to pass after.

### G.14 The §C.1.6 `e_L` excision — the electron-mass conversion struck rather than counted (2026-08-20)

**What was claimed.** §C.1.6 converted its derived L-orbit stiffness into the electron mass by
`m_e = f_L · e_L` with `e_L = √36.47 ≈ 6.04`, and reported the residuals that conversion produced:
a **~36%** match in `f_L`, an empirical exponent `ν_emp ≈ 4.696` giving a **4.4%** mismatch against
the derived `9/2`, and a **0.34%** match of the L2 candidate `ν = 3π/2 = 4.712` to that same
`ν_emp`. The rest-frame extent `ℓ_e = ℏc/(f_L · e_L)` rode the same factor, which the section
already flagged as agreeing by construction.

**Why it fell.** A blind calibration probe established that `e_L` is a **coupling, not an
eigenvalue of anything**, and an undeclared, uncounted one. `36.47` is the ANW hedgehog BVP's
energy *evaluated at* its solution — the BVP's selected parameter is `F'(0) = −1.0038` — and it
enters the baryon formula as `M_0 = 36.47 f_π/e`, coefficient **divided** by the Skyrme coupling.
Writing `m_e = f_L · e_L` reproduces that form only by placing the L-sector coupling at the
self-consistent fixed point `coeff/e = e`, 11% away from the baryon sector's `e = 5.45` for no
stated reason, with no engine primitive behind it and no derivation anywhere in the corpus. Worse,
the functional it borrows from had never been established to apply: if the L-orbit defect is the
Hopf soliton the section's own title names, the rigorous Vakulenko–Kapitanski floor puts the
coefficient at **59.60 > 36.46**, so `36.47` is **excluded** for that branch, not merely
unjustified.

**Why excision rather than counting it as an input.** Both branches were costed. Counting `e_L`
would have spent one counted parameter to keep a conversion the corpus had already tiered
OPEN-INPUT and whose own audit block named the defect — buying nothing. A pre-cut sweep confirmed
the load-bearing fact that made excision cheap: **nothing banked consumed the conversion.** No
engine primitive computes `e_L` or `m_e`; `electron_f_L_MeV` computes `f_L` alone; neither
harness has a check that touches it; no Result Index row depends on it (R-035c depends on R-055
only for the `λ̄_C` ontological reading, which is standard-QM definitional arithmetic); and the
simulator cites only the scaling law.

**What survives.** The scaling law `f_L = f_π(1 − D/J)^{9/2}` (R-055), which never used `e_L`, and
the structural Hopf identification. §C.1.6 now states plainly that `f_L` is a stiffness, that the
framework has no stiffness-to-mass coupling, and that **the electron mass is not derived there**.
The functional-openness analysis is kept, because it is what says how the gap would be closed: the
prerequisite for any L-sector coefficient is settling which functional stabilises the defect, and
the prerequisite for a mass is a coefficient.

**What went with it.** All three residuals. The 0.34% figure was **not** independent of the
conversion — `ν_emp` is definable only through it, and moves to 5.123 (an 8.0% mismatch to
`3π/2`) on the Faddeev branch — so it is the same artifact as the 4.4% and was struck alongside
it. `ν = 3π/2` survives as a candidate *value* with no mechanism and no accuracy figure.

**What did not move: the counted-input headline.** `e_L` was never among the four counted
substrate inputs (`weak = SD`, `f_π`, `D/J`, `c = √2 ⇔ K = 2/3`), nor the measured `G_N`, nor the
provisionally-counted `e = 5.45`, nor the counted `m = E₀` premise. Striking an uncounted quantity
changes no count anywhere in the corpus — which is the whole point of taking this branch.

**A stronger ground, found after the cut.** The post-excision keeper round produced a reason for
branch (b) that does not depend on `e_L`'s value at all: R-068/R-069's banked Brannen
parametrization makes `√m_e` vanish **linearly** at `δ_L = π/12`, hence `m_e ∝ (1 − D/J)²` near
the chirality balance (engine-measured slope 2.2555 at the calibrated `D/J = 0.79`, tending to
2.0000 as `D/J → 1`), while `f_L` carries `9/2`. **A constant cannot bridge two different
exponents**, so `m_e = f_L · e_L` was in collision with two other banked results whatever value
`e_L` took. The collision was invisible because the conversion was only ever evaluated at one
`D/J`. It dissolves on excision — and it means **branch (a) was never really available**: counting
`e_L` repairs no exponent. RUL-070's ground and revert clause were amended to say so.

**Two byproducts.** The `e_L` **symbol collision** with the left-handed electron field (§C.2.2,
§C.5, the engine's `T_3` tables) is resolved: the coupling was the other reader of that name, and
it is gone, leaving only the field. And the loose repaired sentence calling `36.47` "the
eigenvalue" of the BVP left the corpus with the passage that contained it.

**Untouched by design:** `36.47` itself, `skyrmion_mass_MeV`, and the entire baryon sector. The
excision was of the L-sector *conversion* only.

---

# Section 8 — Stable-spectrum enumeration (the over-production test)

*Restored from V2 Annex N.1 (which itself preserved V1 §25.6). The positive-result content — the
wave-phase stability ladder validated on 20 states across 9 orders of magnitude in `N = m/Γ` — is
given its own section immediately below. This section is the falsifier face of the same
enumeration: a check that the framework predicts **exactly** the observed stable spectrum, with
no orphan stable states and no missing predicted-stable states.*

## The over-production test

Enumerating stable sectors — homotopy classes of L/Q windings crossed with Clifford grades,
filtered by Derrick / Skyrme stability — yields the following `(B, L)` table:

| `(B, L)` | Ground state(s) | Observed? |
|---|---|---|
| `(0, 0)`, massless | photon (`U(1)/I_4` boson) | ✓ |
| `(0, 0)`, massive singlet | none (pion decays weakly) | ✓ (none) |
| `(1, 0)` | proton (neutron decays weakly) | ✓ |
| `(0, 1)` | electron, three neutrinos (μ, τ decay weakly) | ✓ |
| `(≥ 2, 0)` | bound nuclei (stability per binding energy, not topology — the engine's own wording; the former "up to Fe stable, above unstable" was factually wrong: stable nuclides run to Pb-208, Fe-56 is only the binding-energy-per-nucleon peak; corrected 2026-07-31, E-11) | ✓ |
| Negative `B, L` | antiparticles (all above) | ✓ |

**The topologically stable set is `{γ, p, e, ν, stable nuclei, antiparticles}` — precisely the
observed stable spectrum. No orphans, no gaps.**

Two structural reasons underwrite this:

- (i) **TWT carries *exactly* the SM's two topological charges** — `B` in `π_3(S³_𝓠)` and `L` in
  `π_1(S¹) ≅ ℤ` on the L-orbit (per the row's own engine cite `lepton_number_topological_conservation`;
  this passage previously wrote `π_3(SU(2)_L)`, contradicting the cite — corrected 2026-07-31, E-11;
  note the electron's §C.1.6 Hopf `H = 1` is a third, distinct object and the engine string still
  conflates two of the three — flagged for the engine sweep) (§C.1, §C.5). Not one, not three; exactly two.
- (ii) **Internal multiplicity is capped at three** — three colours (Q-orbit trivectors,
  §C.4.1) and three generations (count generic-given-4D; ℍ-units, §C.3.8) — by the 4D `ℤ_3` structure of
  `Cl(4,0)`. So no fourth-generation stable orphan and no exotic-colour stable orphan can
  exist within the framework.

A framework wide enough to host non-existent stable particles would fail here. TWT does not.
This is the canonical **§E.3 RF-7 removed-falsifier** — engine `topological_overproduction_test`.

*The mass spectrum within each class is a separate question.* Some masses are DERIVED (lepton
ratios via Brannen, §C.3.5; Skyrme mass formula, §C.1.2); some remain open (which nuclei are
stable, neutrino masses).

---

# Section 9 — Wave-phase stability ladder (20 states across 9 orders of magnitude)

The stability enumeration of Section 8 tells us *which* particles are stable. This section tells
us *why the observed lifetimes fall where they do* — the wave-phase rule that quantifies the
20-state spectrum across the meta-time rotor frequency scale `N = m/Γ` (dimensionless).

## The wave-phase rule

For a defect with meta-time rotor frequency `ω = m`, the stability index

> `N = m / Γ`

is set by the substrate channel(s) available for the winding-integer discharge. Four **Rungs**
by channel:

| Rung | Channel | Physical mechanism | Empirical `N` band |
|---|---|---|---|
| Rung 0 | *Resonance* (strong sector) | Same-orbit Skyrme rearrangement; drive → 0 register is unstable | `N ~ 1–10²` |
| Rung 1 | Electromagnetic | L↔Q photon-strain reconversion (§B.5) | `N ~ 10²–10⁶` |
| Rung 2 | Weak (charged current) | L-pair creation through I_4 (§C.5.7) | `N ~ 10⁵–10¹⁴` |
| Rung 3 | Weak (neutral / rare) | Suppressed by additional I_4 pair or GIM | `N ~ 10¹⁴–10²⁰⁺` |

The 20 empirically stable states — π⁰, π±, K±, K^0_S, K^0_L, η, η', ρ, ω, ϕ, J/ψ, Υ, D, B, τ, μ,
n, p, e, γ — fall on their expected Rung by channel, spanning `N ≈ 1` (ρ, `Γ ~ 150 MeV`) to
`N ≈ 10³¹` (proton, `Γ < ~10⁻³⁴ s⁻¹`; with `N = m/Γ` at the Super-K bound the proton in fact sits `> 10⁵⁸`, so even `10³¹` is understated). **Thirty-one-plus orders of magnitude in `N`** — the former "nine orders" was arithmetically wrong (corrected 2026-07-31, C-3) — parameter-free in form but UNCOMPUTED in-engine; see R-091's re-tier.

## The π⁰ / π± discriminator

The pion doublet illustrates the rule sharply:

- **π⁰** (135 MeV; `Γ ≈ 7.8 eV`; `N ≈ 1.7 × 10⁷`) — decays electromagnetically (`π⁰ → γγ`) via
  the axial anomaly. Rung 1.
- **π±** (140 MeV; `Γ ≈ 2.5 × 10⁻⁸ eV`; `N ≈ 5.6 × 10¹⁵`) — decays weakly (`π± → μ± ν`).
  Rung 2.

Two particles of nearly identical mass differ in stability by **eight orders of magnitude in
`N`**, driven entirely by which substrate channel the framework says they can decay through.
This is the ladder's most striking discriminator.

## Cross-state correlation

Across the 20-state ladder,

> `corr(log N, mass)` ≈ `−0.24`,

a weak *negative* correlation. Heavier particles have on average slightly *lower* stability
(faster decay), but the correlation is far from ±1: the channel Rung dominates over mass. This is
the signature of a rule where **channel sets the band, mass modulates within the band** — exactly
what the wave-phase framing predicts.

## Structural content

The ladder is not a fit: no `N` value is adjusted. What the framework supplies is (a) the
enumeration of stable sectors (Section 8), (b) the Rung-by-channel structure (§C.5.7 β-decay,
§B.5b α), and (c) the qualitative "channel dominates, mass modulates" rule. The empirical 20-state
match across 9 orders of magnitude in `N` with `corr(log N, mass) ≈ −0.24` is a *validation*, not
a calibration.

Tier: **DERIVED-STRUCTURAL** across the 20-state enumeration. Engine primitives: `wave_E_complex_structure`,
`wave_E5`, `topological_overproduction_test`.

---

# Section 10 — Bibliography

*All external citations that appear inline in the V3 body, consolidated for reference. Some are
foundational works; some are contemporary measurements the framework compares against.*

## Attribution for results the body uses (added 2026-07-28)

*A review pass found several results whose **content** the paper uses or reproduces while citing
nobody. Each was verified against Crossref or INSPIRE before being entered here; items that could
not be verified are marked and are deliberately not given DOIs.*

- **Neuberger, H.** (1987). *Spinless fields on F(4) lattices*. Phys. Lett. B **199**, 536. —
  **The origin of the D4/F4 lattice's rotational-improvement property**, which §B.1.5 and R-165 use.
  Verified at INSPIRE. Proposed F4 lattices for scalar regularization precisely because the
  hypercubic lattice's leading Lorentz-breaking operator is absent there. Related use: Celmaster
  (1982 onward); Bhanot, Bitar, Heller & Neuberger (1990/91); Klomfass (1993) — *these three are
  cited from secondary reference lists and are **not** independently verified.*
- **Katz, D., & Nógrádi, D.** (2025). *QCD on the four-dimensional 16-cell honeycomb*.
  arXiv:2512.10604. — Same lattice, live use, verified via the arXiv API (posted 2025-12-11).
  Abstract: *"a higher degree of rotational symmetry as compared to a traditional cubic lattice
  leading to much smaller cut-off effects."* States the dispersion form of the R-165 theorem
  directly: the first order at which Lorentz invariance fails is `O(a⁴)`, not `O(a²)`. **This is the
  citation that retires the claim that R-165's physics is new.**
- **Delsarte, P., Goethals, J. M., & Seidel, J. J.** (1977). *Spherical codes and designs*. —
  The 24-cell is a spherical 5-design, which is essentially the same fact in combinatorial dress.
  **UNVERIFIED**: taken from a secondary reference list; confirm venue and pagination before use.
- **Gatto, R., Sartori, G., & Tonin, M.** (1968). *Weak self-masses, Cabibbo angle, and broken
  SU₂ × SU₂*. Phys. Lett. B **28**(2), 128–130. DOI: 10.1016/0370-2693(68)90150-0. — **The origin
  of `sin θ_C ≃ √(m_d/m_s)`, i.e. `|V_us|² ≈ m_d/m_s`**, universally known as the *GST relation*
  and one of the two classic fermion mass-ratio predictions alongside Koide's. §C.3.10 previously
  presented this relation as a TWT candidate identification without credit; it is not original to
  this work, and only the *frequency-ratio reading* offered there is. Cited at §C.3.10, §E.3 row 14.
- **Bruns, H.** (1887). *Über die Integrale des Vielkörper-Problems*. Acta Math. **11**, 25–96.
  DOI: 10.1007/BF02612319. — No first integral of the Newtonian *n*-body problem algebraic in
  coordinates, momenta and time is independent of the ten classical integrals. Cited at §B.8.4.
  *Note:* the published proof contained an error later repaired (see Julliard-Tosel, Celest. Mech.
  Dyn. Astron. **76** (2000), DOI: 10.1023/A:1008346516349).
- **Poincaré, H.** (1890). *Sur le problème des trois corps et les équations de la dynamique*.
  Acta Math. **13**, 1–270; and *Les méthodes nouvelles de la mécanique céleste*, Vol. I,
  Gauthier-Villars (1892), Ch. V. — No first integral besides `H` that is uniform and analytic in
  the coordinates **and in the perturbation parameter**, under non-degeneracy. Cited at §B.8.4.
  *Two cautions, both applied in the body:* this is a perturbative statement with hypotheses, not a
  blanket non-integrability theorem; and **"the Poincaré–Bruns theorem" is not standard
  terminology** — no authoritative source uses it as a single named result. The body now cites the
  two theorems separately. (No DOI is given: Project Euclid splits the memoir into per-chapter DOIs
  and the commonly-copied identifier resolves only to the three-page introduction.)
- **Sundman, K. F.** (1907). *Recherches sur le problème des trois corps*. Acta Societatis
  Scientiarum Fennicae **34**, No. 6. — Triple collision requires the simultaneous vanishing of all
  three components of total angular momentum. Cited at §B.8.3. **PARTIALLY VERIFIED:** the 1907
  paper could not be obtained; the attribution rests on the authoritative historical study
  (Barrow-Green, J., *The dramatic episode of Sundman*, Historia Mathematica **37**(2), 164–203
  (2010), DOI: 10.1016/j.hm.2009.12.004), which also records that the result was **first stated by
  Weierstrass**, Sundman supplying the first proof. Note the theorem is *not* in Sundman's famous
  Acta Mathematica memoir (**36**, 105–179), which is the convergent-series solution.
- **Atiyah, M. F., & Hitchin, N. J.** (1985). *Low-energy scattering of non-abelian monopoles*.
  Phys. Lett. A **107**(1), 21–25. DOI: 10.1016/0375-9601(85)90238-5. Also Phil. Trans. R. Soc. A
  **315**(1533), 459–469. DOI: 10.1098/rsta.1985.0052. Monograph: *The Geometry and Dynamics of
  Magnetic Monopoles*, Princeton University Press (1988). — Moduli-space (geodesic) dynamics of
  slowly-moving solitons, with 90° monopole scattering as the canonical example. This is the
  literature underlying §B.8.4's defensible core — that solitons in a smooth field have no
  collision singularities and only the *particle* description breaks — which §B.8.4 now cites explicitly
  under import-registry row **I-21** (Section 13.2), with the premise-failure recorded there.

## Prior art in adjacent programmes (added 2026-07-28)

*None of the following was reached by this project's own workflow, and none was used in deriving
any result here — they are cited because a reader needs them to judge the contribution, and because
independent arrival carries no stigma while silence would. Each entry states the adjacency; the
specific delta belongs in the body where the corresponding claim is made.*

- **Trayling, G., & Baylis, W. E.** (2001). *A geometric basis for the standard-model gauge group*.
  J. Phys. A: Math. Gen. **34**(15), 3309–3324. DOI: 10.1088/0305-4470/34/15/309; arXiv:hep-th/0103137.
  Preceded by **Trayling, G.** (1999), *A geometric approach to the standard model*,
  arXiv:hep-th/9912231 (unpublished preprint) — which already claims the bare coupling ratios
  `g_s/g = 1`, `g′/g = √(3/5)` (⇒ `sin²θ_W = 3/8`) "without invoking the notion of master
  groups"; cited at §C.4.5 (added 2026-07-31, primary-verified).
  — **The closest published precedent to §C.4.** Derives the full SM gauge group from rotations in a
  Cl(7) framework — left-sided rotations giving SU(2)_L, right-sided SU(3)_C, a coupled double-sided
  rotation U(1)_Y — with fermion and Higgs charge assignments. §C.4's "no GUT embedding" claim must
  be defended against this specifically, not against SU(5) alone.
- **Lasenby, A., Doran, C., & Gull, S.** (1998). *Gravity, gauge theories and geometric algebra*.
  Phil. Trans. R. Soc. A **356**(1737), 487–582. DOI: 10.1098/rsta.1998.0178. — Gauge Theory
  Gravity: gravity as a gauge theory on a *flat* background in the spacetime algebra, with
  displacement and rotation gauge fields. Directly adjacent to §B.6's frame/connection construction.
- **Plebański, J. F.** (1977). *On the separation of Einsteinian substructures*. J. Math. Phys.
  **18**(12), 2511–2520. DOI: 10.1063/1.523215. — GR with a triple of self-dual two-forms as the
  fundamental variable, subject to a quadratic simplicity constraint `Σⁱ ∧ Σʲ ∝ δ^{ij}`.
- **Urbantke, H.** (1984). *On integrability properties of SU(2) Yang–Mills fields. I.* J. Math.
  Phys. **25**(7), 2321–2324. DOI: 10.1063/1.526402. — The Urbantke metric, recovering a conformal
  structure from a triple of two-forms. **Scope note, engine-checked:** it has been suggested that
  the framework's `h_{μν} = ⟨Ω_μ I₄ Ω_ν⟩₀` is an Urbantke-family object. It is **not**. The Urbantke
  metric is *cubic* in the two-forms (three powers, one spacetime ε, one internal ε); `⟨A I₄ B⟩₀` is
  *bilinear* — verified by direct MV computation (2026-07-30; a computation, not a banked
  primitive) to equal the wedge coefficient `λ` in `A ∧ B = λ I₄` — so it
  carries one epsilon and two powers. The two are structurally different objects, and the
  signature/reality results of the Urbantke literature therefore do **not** transfer to R-145's
  signature menu without further work.
- **Krasnov, K.** (2011). *Plebański formulation of general relativity: a practical introduction*.
  Gen. Relativ. Gravit. **43**(1), 1–15. DOI: 10.1007/s10714-010-1061-x; arXiv:0904.0423. Also
  *Self-dual gravity*, Class. Quantum Grav. **34**(9), 095001 (2017), DOI: 10.1088/1361-6382/aa65e5.
  — Chiral formulations using only the self-dual half of the frame rotation group. The nearest
  published thinking to the framework's SD/ASD organizing principle and its chirality selection,
  which bears on the single counted weak-sector input bit.
- **Furey, C.** (2015). *Charge quantization from a number operator*. Phys. Lett. B **742**,
  195–199. DOI: 10.1016/j.physletb.2015.01.023. Also *Three generations, two unbroken gauge
  symmetries, and one eight-dimensional algebra*, Phys. Lett. B **785**, 84–89 (2018), DOI:
  10.1016/j.physletb.2018.08.032. — Division-algebraic SM structure (ℝ⊗ℂ⊗ℍ⊗𝕆). **Read defensively:**
  the same *shape* of argument as §C.3.8, and it forces the question §C.3.8 does not answer — why ℍ
  rather than 𝕆? Frobenius yields three imaginary units only because *associativity* was assumed;
  dropping it gives the octonions and seven. (*Name note:* published as C. Furey through ~2018,
  N. Furey thereafter; cited here as printed.) Body-cited records at §C.3.8 (primary-verified
  2026-07-30): *Standard model physics from an algebra?*, arXiv:1611.09182 (thesis); Eur. Phys.
  J. C **78** (2018) 375, DOI: 10.1140/epjc/s10052-018-5844-7; Furey & Hughes, Phys. Lett. B
  **827** (2022) 136959, DOI: 10.1016/j.physletb.2022.136959.
- **Chisholm, J. S. R., & Farwell, R. S.** (1987). *Electroweak spin gauge theories and the frame
  field*. J. Phys. A: Math. Gen. **20**(18), 6561–6580. DOI: 10.1088/0305-4470/20/18/052. Also
  *Unified spin gauge theory of electroweak and gravitational interactions*, ibid. **22**(8),
  1059–1071 (1989), DOI: 10.1088/0305-4470/22/8/020. — Spin-gauge unification: gauge transformations
  as inner automorphisms of a Clifford algebra, with a frame field generating gauge-boson masses and
  a gravitational Lagrangian without a Higgs scalar. Prior art on the same programme. *The
  electroweak papers use C(2,6); signatures reported elsewhere in secondary sources could not be
  confirmed and are not repeated here.*
- **Boyle, L., & Farnsworth, S.** (2014). *Non-commutative geometry, non-associative geometry and
  the standard model of particle physics*. New J. Phys. **16**, 123027. DOI:
  10.1088/1367-2630/16/12/123027. Also *The standard model, the Pati–Salam model, and 'Jordan
  geometry'*, New J. Phys. **22**, 073023 (2020), DOI: 10.1088/1367-2630/ab9709. — Algebraic/spectral
  SM constructions; adjacent ambition, different algebra. (*Author order alternates across the
  series; it is given per paper.*)

## Empirical constants and measurements (PDG edition of record: PDG 2024)

- **Navas, S., et al.** (Particle Data Group) (2024). *Review of Particle Physics*. Phys. Rev. D
  **110**, 030001. — **The edition of record for every empirical constant in this paper.** Lepton
  masses `m_e = 0.51099895000(15)`, `m_μ = 105.6583755(23)`, `m_τ = 1776.93 ± 0.09` MeV; quark
  masses, `|V_us|`, hadron splittings, `Γ_t`, and the `sin²θ_W` scheme conventions. *Cross-edition
  note:* the τ mass moved from `1776.86 ± 0.12` (pre-2024), which shifts the Brannen scale
  `μ² = 313.84 → 313.85` MeV; every quantity derived from it survives at its stated precision
  (`m_N/3` convergence 0.28%, ratio 1.0028, amplitude form 0.9986), and both `K = 2/3` (to
  `2.2×10⁻⁶`) and Foot's `45.000° ± 0.001°` survive the update. Engine and paper were
  re-synchronised in one pass on 2026-07-28.
- **Campbell, N. A., Michael, C., & Rakow, P. E. L.** (1984). *The string tension from lattice
  QCD*. Phys. Lett. **139B**, 288. — Source of the hadron-spectrum string tension
  `√σ = 0.44 GeV` quoted at §C.5.12. Note the value enters that paper as an *input* from the
  high-spin light-quark meson spectrum, not as a lattice output.
- **Necco, S., & Sommer, R.** (2001). *The `N_f = 0` heavy quark potential from short to
  intermediate distances*. hep-lat/0108008 (DESY 01-095). — Quenched static force; eq. (3.5)
  `σ r₀² = 1.65 − π/12`. Consulted for §C.5.12; note this is not an independent determination of
  `σ` but follows from the `r₀` definition plus the bosonic-string assumption.
- **Uvarov, V. A.** (for the DELPHI Collaboration) (2002). *Study of charge multiplicity in
  hadronic three-jet Z decays at LEP*. hep-ex/0211010. — Preliminary
  `C_A/C_F = 2.277 ± 0.02 (stat) ± 0.05 (syst)`, quoted at §C.4.4. **Model-dependent:** a
  colour-dipole-model extraction whose alternative fit variant gives 2.093, the variant choice
  riding partly on agreement with `9/4` — so this corroborates rather than independently tests
  the framework's `C_A/C_F = 9/4`.

## Lorentz-invariance tests (import I-19)

- **Liberati, S.** (2013). *Tests of Lorentz invariance: a 2013 update*. Class. Quantum Grav.
  **30**, 133001; arXiv:1304.5795. — The dimension-six (`n = 4`) constraint tables: eq. (77)
  photon `−10⁻⁷ ≲ ξ⁽⁴⁾ ≲ 10⁻⁸` and electron `−10⁻⁷ ≲ η⁽⁴⁾ ≲ 10⁻⁶`; eq. (78) proton
  `−10⁻³ ≲ η⁽⁴⁾_p ≲ 10⁻⁶` at 99% CL for pure-proton composition. Cited at §B.6.3, §E.3.3 VG-6.
- **Stecker, F. W.** (2009). *Gamma-ray and cosmic-ray tests of Lorentz invariance violation and
  quantum gravity models and their implications*. arXiv:0912.0500. — Eq. (18),
  `δ^π_p < 4.5 × 10⁻²³` from the Auger spectrum above the GZK energy; the constrained combination
  is `η_π − 25η_p`, which is why species-universality does not evade the bound at dimension six.
- **Collins, J., Perez, A., Sudarsky, D., Urrutia, L., & Vucetich, H.** (2004). *Lorentz
  invariance and quantum gravity: an additional fine-tuning problem?* Phys. Rev. Lett. **93**,
  191301; arXiv:gr-qc/0403053. — The radiative-naturalness obstacle defused at §B.1.5.

## The mass→weight empirical chain (§B.6 intro block; import I-23, added 2026-08-02)

*Every entry below was primary-source-verified 2026-08-02 (journal/arXiv/INSPIRE/NIST records
read directly; two web agents, reports archived in the session record). These carry the §B.6
"what the laboratory pins" block and the engine's `mass_weight_empirical_chain` ledger.
Link 1 — clock ↔ inertial mass:*

- **Sturm, S., Köhler, F., Zatorski, J., Wagner, A., Harman, Z., Werth, G., Quint, W., Keitel,
  C. H., & Blaum, K.** (2014). *High-precision measurement of the atomic mass of the electron*.
  Nature **506**, 467. — Electron mass at 2.8×10⁻¹¹ via the Larmor-to-cyclotron frequency ratio
  of one bound electron in ¹²C⁵⁺ plus bound-state QED (a frequency measurement, but not a
  two-particle cyclotron ratio — that distinction is recorded here; the paper states only the
  frequency-ratio fact, which holds for both).
- **Heiße, F., et al.** (2017). *High-precision measurement of the proton's atomic mass*. Phys.
  Rev. Lett. **119**, 033001. — Proton mass at 32 ppt as a proton-vs-¹²C⁶⁺ cyclotron-frequency
  ratio. Dating trap: the 2017 value was later shifted by reanalysis; cited only for the
  precision class, no value imported.
- **Morel, L., Yao, Z., Cladé, P., & Guellati-Khélifa, S.** (2020). *Determination of the
  fine-structure constant with an accuracy of 81 parts per trillion*. Nature **588**, 61. —
  `h/m(⁸⁷Rb)` by photon recoil at ~1.4×10⁻¹⁰.
- **Lan, S.-Y., Kuan, P.-C., Estey, B., English, D., Brown, J. M., Hohensee, M. A., & Müller,
  H.** (2013). *A clock directly linking time to a particle's mass*. Science **339**, 554. —
  A Cs interferometer operated as a clock at a subharmonic of the atom's Compton frequency;
  microscopic mass at 4×10⁻⁹.
- **CGPM** (2018). *Resolution 1 of the 26th CGPM: On the revision of the International System
  of Units (SI)*. BIPM. — The kilogram defined via fixed `h`, effective 20 May 2019.

*Link 2 — inertia ↔ passive weight:*

- **Touboul, P., Métris, G., Rodrigues, M., et al. (MICROSCOPE collaboration)** (2022).
  *MICROSCOPE mission: final results of the test of the equivalence principle*. Phys. Rev. Lett.
  **129**, 121102. — `η(Ti,Pt) = [−1.5 ± 2.3 (stat) ± 1.5 (syst)] × 10⁻¹⁵`. (Not the 2017
  first-results paper.)
- **Wagner, T. A., Schlamminger, S., Gundlach, J. H., & Adelberger, E. G.** (2012).
  *Torsion-balance tests of the weak equivalence principle*. Class. Quantum Grav. **29**,
  184002. — `η(Be,Ti) = (0.3 ± 1.8)×10⁻¹³`, `η(Be,Al) = (−0.7 ± 1.3)×10⁻¹³`.
- **Peters, A., Chung, K. Y., & Chu, S.** (1999). *Measurement of gravitational acceleration by
  dropping atoms*. Nature **400**, 849. — A falling corner cube and a Cs atom agree to 7×10⁻⁹.
- **Asenbaum, P., Overstreet, C., Kim, M., Curti, J., & Kasevich, M. A.** (2020).
  *Atom-interferometric test of the equivalence principle at the 10⁻¹² level*. Phys. Rev. Lett.
  **125**, 191101. — `η(⁸⁵Rb,⁸⁷Rb) = [1.6 ± 1.8 ± 3.4] × 10⁻¹²`.
- **Colella, R., Overhauser, A. W., & Werner, S. A.** (1975). *Observation of gravitationally
  induced quantum interference*. Phys. Rev. Lett. **34**, 1472. — First observation, neutrons;
  measured 54.3(2.0) rad vs 59.8(1) rad predicted — agreement at the ~10% level (the
  often-recalled "1%" belongs to 1980s refinements).
- **Littrell, K. C., Allman, B. E., & Werner, S. A.** (1997). *Two-wavelength-difference
  measurement of gravitationally induced quantum interference phases*. Phys. Rev. A **56**,
  1767. — Statistical precision ~10⁻³ with a ~0.6–0.8% discrepancy from theory, reported as
  statistically significant and unexplained at publication.
- **Witteborn, F. C., & Fairbank, W. M.** (1967). *Experimental comparison of the gravitational
  force on freely falling electrons and metallic electrons*. Phys. Rev. Lett. **19**, 1049. —
  Net vertical force on free-falling electrons < 0.09 mg (~10% level); depends on a
  low-temperature patch-potential shielding never reproduced elsewhere. The positron version
  (announced in Witteborn & Fairbank, Nature **220**, 436 (1968)) was never performed.
- **Anderson, E. K., et al. (ALPHA collaboration)** (2023). *Observation of the effect of
  gravity on the motion of antimatter*. Nature **621**, 716. — Antihydrogen falls down:
  `a_g̅ = [0.75 ± 0.13 (stat+syst) ± 0.16 (sim)] g`.

*Link 3 — passive ↔ active:*

- **Kreuzer, L. B.** (1968). *Experimental measurement of the equivalence of active and passive
  gravitational mass*. Phys. Rev. **169**, 1007. — Density-matched Teflon/liquid Cavendish-type
  test; active/passive material-independence to ~5×10⁻⁵.
- **Bartlett, D. F., & Van Buren, D.** (1986). *Equivalence of active and passive gravitational
  mass using the moon*. Phys. Rev. Lett. **57**, 21. — Fe vs Al via the lunar
  center-of-figure/center-of-mass offset: 4×10⁻¹².
- **Singh, V. V., Müller, J., Biskupek, L., Hackmann, E., & Lämmerzahl, C.** (2023).
  *Equivalence of active and passive gravitational mass tested with lunar laser ranging*. Phys.
  Rev. Lett. **131**, 021401. — The current record: 3.9×10⁻¹⁴ (Al vs Fe).

*Link 4 — active gravity of small sources, and the two sharpest fences:*

- **Westphal, T., Hepach, H., Pfaff, J., & Aspelmeyer, M.** (2021). *Measurement of
  gravitational coupling between millimetre-sized masses*. Nature **591**, 225. — The smallest
  measured gravitational SOURCE: a 92.1 ± 0.1 mg gold sphere of radius 1.07 mm. Anchors the
  gap arithmetic: 5.5×10²² proton *masses* / 1.0×10²⁶ electron masses (CODATA 2022; the
  sphere's actual proton count, Z = 79, is 2.2×10²² — the gap quantity is a mass ratio).
- **Fuchs, T. M., et al.** (2024). *Measuring gravity with milligram levitated masses*. Sci.
  Adv. **10**, eadk2949. — The 0.43 mg levitated particle is the TEST mass; the sources are
  2.45 kg brass masses — press summaries notwithstanding, this does not lower the
  smallest-source record.
- **Bose, S., et al.** (2017). *Spin entanglement witness for quantum gravity*. Phys. Rev. Lett.
  **119**, 240401; **Marletto, C., & Vedral, V.** (2017). *Gravitationally induced entanglement
  between two massive particles is sufficient evidence of quantum effects in gravity*. Phys.
  Rev. Lett. **119**, 240402. — The BMV proposals; as of the verification date no experiment has
  demonstrated gravity-mediated entanglement or the field of a superposed mass.
- **Heckel, B. R., et al.** (2008). *Preferred-frame and CP-violation tests with polarized
  electrons*. Phys. Rev. D **78**, 092006. — Spin-polarized torsion pendulum (~10²³ polarized
  electrons): the gravitational mass of an electron differs by less than ~1 part in 10²¹
  between opposite spin orientations — **the abstract's own statement**, not a conversion made
  here (the underlying published quantity is preferred-frame `|A_X,Y| ≤ 1.5×10⁻²² eV`); the
  per-electron reading rides linearity across the pendulum's spins, and the paper says so. (The
  companion PRL is **97**, 021603 (2006) — not PRL 100, 041101, which is the Schlamminger Be/Ti
  EP test.)

## Foundational geometric algebra & Clifford

- **Hestenes, D.** (1966). *Space–Time Algebra*. Gordon and Breach. — Foundational reference for
  the Clifford-algebra formulation of Dirac / Maxwell used throughout Parts A, B, D.
- **Lawson, H. B., & Michelsohn, M.-L.** (1989). *Spin Geometry*. Princeton University Press. —
  Standard reference for the Cl(p,q) classification cited at §D.1.3.
- **Frobenius, F. G.** (1878). *Über lineare Substitutionen und bilineare Formen*. — Frobenius
  theorem on finite-dimensional associative real division algebras, used at §C.3.8.
- **Doran, C., Lasenby, A., & Gull, S.** (1993). *States and operators in the spacetime
  algebra*. Found. Phys. **23**(9), 1239–1264. DOI: 10.1007/BF01883678. — The GA-native
  treatment of states as multivectors with one-sided rotor action, the unit imaginary as a
  fixed bivector, and the **multiparticle spacetime algebra** (a separate copy of the algebra
  per particle, with the standard unit imaginary inducing correlations between the particle
  spaces). Cited **at the use-site**, §B.4.1, as the antecedent of that section's calculation;
  distinct from the same authors' gauge-theory-gravity work below.
- **Doran, C., Lasenby, A., Gull, S., Somaroo, S., & Challinor, A.** (1996). *Spacetime
  algebra and electron physics*. Adv. Imaging Electron Phys. **95**, 271–386. DOI:
  10.1016/S1076-5670(08)70158-7; arXiv quant-ph/0509178 (posted 2005, the 1996 text). —
  Book-length development covering spin measurement and multiparticle quantum mechanics;
  §B.4.1. Note the author list is larger than the 1993 paper's.
- **Horwitz, L. P., & Biedenharn, L. C.** (1984). *Quaternion quantum mechanics: second
  quantization and gauge fields*. Ann. Phys. **157**(2), 432–488. DOI:
  10.1016/0003-4916(84)90068-X. — The quaternionic Hilbert module with its hierarchy of
  real / complex / quaternion-linear scalar products; the **complex-linearity ("complex
  geometry") condition** under which tensor products of quaternion modules are constructed
  preserving complex linearity, and creation/annihilation operators with them. Cited at
  §B.3.3 as the prior art for that section's projection of the overlap onto `{1, B}`, and as
  the named function that locates §B.4.1's unbuilt multi-defect state space.
- **Mosseri, R., & Dandoloff, R.** (2001). *Geometry of entangled states, Bloch spheres and
  Hopf fibrations*. J. Phys. A **34**(47), 10243–10252. DOI: 10.1088/0305-4470/34/47/324;
  arXiv quant-ph/0108137. — Reviews the single-qubit case (`S³` state space, Bloch sphere as
  Hopf base, fibre = overall phase) and extends it to two qubits via the `S⁷` fibration, the
  paper's own new content. Cited at §B.4's mathematical-setting block as **established
  literature**, not as the origin of the single-qubit picture.
- **Urbantke, H.** (1991). *Two-level quantum systems: states, phases, and holonomy*. Am. J.
  Phys. **59**(6), 503–509. DOI: 10.1119/1.16809. — Pictorial treatment of two-level-system
  states, phases and their evolution on the two- and three-sphere; §B.4.
- **Urbantke, H. K.** (2003). *The Hopf fibration — seven times in physics*. J. Geom. Phys.
  **46**(2), 125–150. DOI: 10.1016/S0393-0440(02)00121-3. — Survey of the Hopf fibration's
  appearances in physics; §B.4. Distinct from the 1984 Urbantke-metric paper cited under
  §B.6 / R-145, which is a different result and must not be conflated with it.

## Skyrme model and topological solitons

- **Skyrme, T. H. R.** (1961). *A non-linear field theory*. Proc. Roy. Soc. A **260**, 127. —
  Original Skyrme construction; cited at §C.1.
- **Adkins, G. S., Nappi, C. R., & Witten, E.** (1983). *Static properties of nucleons in the
  Skyrme model*. Nucl. Phys. B **228**, 552. DOI: 10.1016/0550-3213(83)90559-X. — ANW Skyrme
  phenomenology; `e = 5.45`, `f_π = 129 MeV`; §C.1.2, §D.4.2. **Nomenclature caution:** the
  `129 MeV` is ANW's *fitted* `F_π`, obtained by fitting `N` and `Δ`; the physical decay
  constant in the same normalization is `F_π ≈ 186 MeV` (see e.g. Hahm, Han & Shin, *Phys.
  Rev. D* **56** (1997) 1812, Table 2, which lists the ANW-class fit at `129 MeV` against an
  experiment column of `186 MeV`). It must not be read as the measured `f_π⁺ = 130.2(1.7) MeV`
  of the `√2` convention (Rosner, Stone & Van de Water, arXiv 1509.02220 — the PDG leptonic-decay
  review; PDG 2014 value `130.41(21) MeV`), which it merely resembles numerically.
- **Finkelstein, D., & Rubinstein, J.** (1968). *Connection between spin, statistics, and
  kinks*. J. Math. Phys. **9**, 1762. — Finkelstein–Rubinstein construction for spin-statistics
  via `π_4(SU(2)) = ℤ_2`; §B.3.5.

## Koide, Foot, and lepton mass structure

- **Koide, Y.** (1983). *A fermion-boson composite model of quarks and leptons*. Phys. Lett. B
  **120**, 161. — The empirical Koide identity `K = 2/3`.
- **Foot, R.** (1994). *A note on Koide's lepton mass relation*. arXiv:hep-ph/9402242. — The
  Foot angle characterization `cos θ = (Σ√m) / √(3 Σ m)` = 45°; §C.3.4.
- **★ Koide, Y.** (2000). *Quark and Lepton Mass Matrices with a Cyclic Permutation Invariant
  Form*. arXiv:hep-ph/0005137. — **PRIORITY for the ℤ_3 circulant parametrization** underlying
  what this corpus labels the Brannen amplitude form; §C.3.1. *Priority correction recorded
  2026-08-18 (prior-art pass, RUL-050): the corpus previously credited the parametrization to
  Brannen 2006. The split is stated in the literature itself — Rivero, A. & Gsponer, A.,
  arXiv:hep-ph/0505220, p. 8: "This possibility has also been noticed recently by Carl Brannen
  [21] in a variant, **previously used by Koide [12]**, of the democratic mixing…", where [12]
  is this 2000 paper; Żenczykowski splits the credit identically.*
- **Brannen, C. A.** (2006). *The lepton masses*. `brannenworks.com/MASSES2.pdf`, 2 May 2006 —
  **self-published; no journal, no arXiv.** — The independent 2006 re-noticing of the
  charged-lepton case of Koide's circulant form: Eq. (4) `λ_n = μ(1 + 2η cos(δ + 2nπ/3))`,
  Eq. (14) `η₁² = 0.500003(23)`, `δ₁ = 0.2222220(19)` — i.e. `2η = √2`. **What is credited to
  Brannen is that numerical pinning of the amplitude and phase, not the parametrization**; the
  refereed entry point for the result is Koide's own 2007 paper below, whose abstract opens
  *"Brannen has recently pointed out that the observed charged lepton masses satisfy the
  relation…"*. §C.3.1, §C.3.5.
- **Koide, Y.** (2007). *Tribimaximal Neutrino Mixing and a Relation Between Neutrino- and
  Charged Lepton-Mass Spectra*. J. Phys. G **34**, 1653–1664. — Carries the single-harmonic ℤ_3
  form whose parameter counting the R-170 collapse identity expresses. *Verified 2026-08-13
  against the INSPIRE-HEP REST API: title, journal, volume, pages, author and year confirmed.*
- **Rosen, G.** (2007). Mod. Phys. Lett. A **22**, 283. — The all-sectors-equal-phase
  hypothesis (δ_f equal across fermion sectors) — the class of claim struck by R-170's repair,
  already problematized by Żenczykowski 2012. *Metadata supplied by the 2026-08-13 §8a review
  round; INSPIRE lookup did not resolve this record in the same pass — bibliographic details NOT
  independently verified; known in the Koide-circle literature via Żenczykowski (2012)'s
  citations. Verify before external use.*
- **Żenczykowski, P.** (2012). *Remark on Koide's Z3-symmetric parametrization of quark masses*.
  Phys. Rev. D **86**, 117303. arXiv:1210.4125. — Prior art for R-170: states the N = 3
  parameter-counting non-observability, and its Eq. (12) is the model-free closed form for the
  invariant phase (`tan δ_f = √3(√m₂−√m₁)/(2√m₃−√m₂−√m₁)`), verified in-engine ≡ the 3-point
  DFT phase; abstract states δ is experimentally indistinguishable from 2/9. *Verified
  2026-08-13 against the INSPIRE-HEP REST API and the arXiv abstract: title, journal, volume,
  article id, author and year confirmed.*
- **Żenczykowski, P.** (2013). *Koide's Z_3-symmetric parametrization, quark masses, and
  mixings*. Phys. Rev. D **87**, 077302. arXiv:1301.4143. — The δ_D-vs-δ_L non-equality
  comparison itself (prior art for R-170's strike). *Verified 2026-08-13 against the INSPIRE-HEP
  REST API: title, journal, volume, article id, author and year confirmed.*
- **Sumino, Y.** (2009a). *Family Gauge Symmetry and Koide's Mass Formula*. Phys. Lett. B **671**,
  477–480. arXiv:0812.2090 (Dec 2008). — **Prior art on the mass-definition objection to Koide**
  (§C.3.3, §C.3.3a, negatives ledger N57). From the abstract, read directly: it proposes "a mechanism
  for cancelling the QED correction to Koide's formula", in an effective theory with `U(3)` family
  gauge symmetry unified with `SU(2)_L` at the `10²–10³` TeV scale. This is the standard response in
  the literature — family gauge bosons whose contribution cancels the QED correction that spoils the
  relation away from the pole point. TWT has **no family gauge sector** and does not adopt the
  mechanism; the citation is here so that TWT's own definition gap is not presented as an
  unrecognized problem. *Verified 2026-07-30 against the INSPIRE-HEP REST API
  (`literature?q=arxiv:0812.2090`): title, journal, volume, pages, year and abstract all confirmed.*
- **Sumino, Y.** (2009b). *Family Gauge Symmetry as an Origin of Koide's Mass Formula and Charged
  Lepton Spectrum*. JHEP **05**, 075. arXiv:0812.2103 (Dec 2008). — The companion model paper.
  *Verified 2026-07-30 against the INSPIRE-HEP REST API (`literature?q=arxiv:0812.2103`): title,
  journal, volume, article id, author and year confirmed.*
- **Koide, Y.** (2017). *Sumino's cancellation mechanism in an anomaly-free model*. Mod. Phys.
  Lett. A **32**, 1750062. arXiv:1608.04514. — Koide's own follow-up on the cancellation mechanism,
  cited as evidence that the objection is live in the primary literature rather than a referee's
  invention. *Verified 2026-07-30 against the INSPIRE-HEP REST API (`literature?q=arxiv:1608.04514`):
  title, journal, volume, article id, author and year confirmed; abstract not read.*

## Sakharov induced gravity and Lorentz-violation constraints

- Visser, M., *Sakharov's induced gravity: a modern perspective*, Mod. Phys. Lett. A **17** (2002)
  977–992, arXiv:gr-qc/0204062. (Survey of the induced-gravity programme; bibliographic record
  verified via arXiv 2026-07-30. Added on external-review advice as the standard modern survey of
  the mechanism §B.6.2 uses; no specific result is imported from it.)

### Lattice→continuum coupling matching (the §C.4.5 named premise; added 2026-07-30)

- Hasenfratz, A. & Hasenfratz, P., *The connection between the Λ parameters of lattice and
  continuum QCD*, Phys. Lett. B **93** (1980) 165.
- Weisz, P., *On the connection between the Λ parameters of Euclidean lattice and continuum QCD*,
  Phys. Lett. B **100** (1981) 331.
- Billoire, A., *Another connection between the Λ parameters of the Euclidean lattice and
  continuum QCD*, Phys. Lett. B **104** (1981) 472.

(All three verified against INSPIRE publisher metadata 2026-07-30. Cited as the standard
treatments of the lattice→continuum matching that the §C.4.5 crossing-at-`Λ_L` premise owes;
no numerical value is imported — the correction is named as UNCOMPUTED.)

- **Sakharov, A. D.** (1967). *Vacuum quantum fluctuations in curved space and the theory of
  gravitation*. Sov. Phys. Dokl. **12**, 1040. — Original induced-gravity construction; §B.6.
- **Volovik, G. E.** (2003). *The Universe in a Helium Droplet*. Oxford University Press. —
  Self-sustained-medium identity for the cosmological constant; §B.7, §E.1.1.
- **Collins, J., Perez, A., Sudarsky, D., Urrutia, L., & Vucetich, H.** (2004). *Lorentz
  invariance and quantum gravity: an additional fine-tuning problem?*. Phys. Rev. Lett. **93**,
  191301. — Radiative-naturalness argument that TWT's matter-as-defect Lorentz protection
  defuses; §B.1.5.
- **Weinberg, S., & Witten, E.** (1980). *Limits on massless particles*. Phys. Lett. B **96**,
  59. — Weinberg-Witten no-go for massless composite gauge bosons; §B.6.7 free win.

## Bell tests, non-locality timing

- **Salart, D., et al.** (2008). *Testing the speed of "spooky action at a distance"*. Nature
  **454**, 861. — Geneva-class influence-speed lower bound; §E.3 row 4.
- **Yin, J., et al.** (2013). *Bounding the speed of "spooky action at a distance"*. Phys. Rev.
  Lett. **110**, 260407. — Higher-precision follow-up; §E.3 row 4.
- **Toner, B. F., & Bacon, D.** (2003). *Communication cost of simulating Bell correlations*.
  Phys. Rev. Lett. **91**, 187904. — One-bit-per-run result; §B.4.5.
- **Tsirelson, B. S.** (1980). *Quantum generalizations of Bell's inequality*. Lett. Math.
  Phys. **4**, 93. — Tsirelson bound `2√2`; §B.4.2.
- **Mermin, N. D.** (1990). *Extreme quantum entanglement in a superposition of macroscopically
  distinct states*. Phys. Rev. Lett. **65**, 1838. — Mermin's operator; §B.4 scope note.
- **Klyshko, D. N.** (1993). *The Bell and GHZ theorems: a possible three-photon interference
  experiment and the question of nonlocality*. Phys. Lett. A **172**, 399. — Belinskii–Klyshko
  polynomial; §B.4.2 subsection.
- **Christian, J.** (2007). *Disproof of Bell's theorem by Clifford algebra valued local
  variables*. arXiv quant-ph/0703179. — Cited **once, for a scope distinction**, in §B.4's
  opening paragraph: that programme claims a local, deterministic, Clifford-algebra-valued
  variable reproducing the EPR–Bohm correlations, i.e. an evasion of Bell's theorem. This
  framework claims no such thing — §B.4.3 names **factorizability** as the premise it
  violates, the leg orthodox quantum mechanics violates too. The citation marks the
  difference and takes no position in the dispute over that programme.

## Cosmology and multi-messenger

- **LIGO / Virgo Collaboration** (2017). *Gravitational waves and gamma-rays from a binary
  neutron star merger: GW170817 and GRB 170817A*. Astrophys. J. Lett. **848**, L13. —
  `|c_GW/c − 1| ≲ 10⁻¹⁵`; §E.3 row 1, §E.3 VG-1.
- **Planck Collaboration** (2020). *Planck 2018 results: cosmological parameters*. Astron.
  Astrophys. **641**, A6. — `Ω_k`, `Ω_DM`, `Σ m_ν` bounds; §A.2, §E.1.3.

## Sphere-packing, kissing numbers

- **Korkin, A., & Zolotarev, G.** (1872). *Sur les formes quadratiques positives quaternaires*.
  Math. Ann. **5**, 581. — D4 as densest 4D **lattice** packing; §D.3.1.
- **Cohn, H., Kumar, A., Miller, S. D., Radchenko, D., & Viazovska, M.** (2017). *The
  sphere-packing problem in dimension 24*. Ann. of Math. **185**, 1017. — The 24D case
  (unrelated to D4; cited only to clarify the misattribution corrected at §D.3.1).

## Isometric embedding (Janet–Cartan)

- **Janet, M.** (1926). *Sur la possibilité de plonger un espace riemannien donné dans un
  espace euclidien*. Ann. Soc. Pol. Math. **5**, 38. — Isometric embedding lower bound; §B.6.6.
- **Cartan, É.** (1927). *Sur la possibilité de plonger un espace riemannien donné dans un
  espace euclidien*. Ann. Soc. Pol. Math. **6**, 1. — Complementary embedding result; §B.6.6.

## Kovtun–Son–Starinets viscosity bound

- **Kovtun, P., Son, D. T., & Starinets, A. O.** (2005). *Viscosity in strongly interacting
  quantum field theories from black-hole physics*. Phys. Rev. Lett. **94**, 111601. — KSS
  bound `η/s ≥ ℏ/(4π)`; §E.3 VG-1.

## Adler
- **Adler, S. L.** (1982). *Einstein gravity as a symmetry-breaking effect in quantum field
  theory*. Rev. Mod. Phys. **54**, 729. — Review of induced-gravity sign considerations
  referenced at §B.6.4.

## Deconfined-quantum-critical-point universality

- **Senthil, T., Vishwanath, A., Balents, L., Sachdev, S., & Fisher, M. P. A.** (2004).
  *Deconfined quantum critical points*. Science **303**, 1490. — DQCP framework underwriting
  the electron mass exponent `9/2`; §C.1.6.

## Empirical particle-data references

- **Particle Data Group** (2024). *Review of Particle Physics*. Prog. Theor. Exp. Phys. — Source
  of empirical masses, widths, CKM elements, `sin²θ_W(M_Z) = 0.2312`, `α_em`, `α_s(M_Z)`, and
  the ~20 stable-state widths of Section 9's ladder.

---

---

# Section 11 — Paper 2 agenda

*Moved from paper §E.4.4. What Paper 2 would derive, organized by which kernel object closes
what.*

## The #1 gap target

Derive `S` (equivalently `Θ_rel` via `Im χ`) from the substrate's driven-dissipative dynamics
(§D.5). Closes the entire pending-values registry's left column. **The framework's single
highest-value Paper-2 task.** *[2026-07-22 update: the kernel FORM is now a named candidate
class (§E.5, R-153–R-158, CANDIDATE / Grade B — the Section-12 Class-2b route executed); the
remaining Paper-2 task is the SELECTION within the class (the virgin-sector discriminators P1/P2,
or any gated forward map) + the magnitudes, which all stay gated.]*

## Structural gates

- **Texture tetrad explicit construction** (paper §B.6.6; absolute coefficient open).
- **QCD UV gate** — asymptotic freedom from the marginal 4D-Skyrme sector (paper §C.5.2).
- **Gauge sector explicit construction** — substrate non-commutativity verification + explicit
  Yang-Mills + finite-action instanton at the substrate level. *Inherits W-LIVE-4 W1 (reduced
  2026-07-02, N35): compute the induced level-N_c topological term on the B = 1 worldline —
  odd level forces fermionic Skyrmion quantization; zero/even makes the FR SELECTION permanent.*

## Value-gate calibrations (all derivable once `S` is pinned)

- Absolute mass scales: `f_π` absolute MeV; `M_0` baryon mass.
- The four EW/strong couplings: `α_em`, `g`, `α_s`, `α_W` — one dial via §B.5b's parameter economy.
- `m_e` via L-orbit QCP; `m_ν` via active-sterile overlap.
- CKM hierarchy + Jarlskog.
- Cosmological constant residual `Λ ~ H²`.
- Same-composition mass-split magnitudes (77, 294, 193, 217 MeV from paper §C.1.4 table).
- QCD running and confining-string tension `σ_QCD ≈ 0.19 GeV²` (`√σ ≈ 0.44 GeV`, Campbell–Michael–Rakow 1984).

## Other Paper 2 items

- **Cell-formation mechanism** — the two-scale keystone; D4 packing-fact derivation from
  dynamics; cell-order requirement for LV safety (§B.6.3 SC-2).
- **Dark sector candidates** — sterile-RH leads Z1/Z2/Z3 from paper §E.1.3; differential
  coupling (spin-2 gravitational vs spin-2 EM channels); wave-train phase-defect cosmological
  accumulation.
- **L-orbit Skyrmion sector** — explicit derivation of the electron QCP scaling exponent from
  a full linear-spin-wave calculation, including the L2 residual mechanism.
- **Strong-field gravity** — texture-tetrad EH action beyond linearized order; black-hole
  interior structure.
- **Active-sterile overlap for neutrino Dirac mass** — the m_ν absolute scale, gated on §D.5.
- **Multi-Skyrmion BVP** — deuteron as `B = 2` Skyrmion; nuclear binding; tensor force.
  ***CLOSED AT SCOPE 2026-07-03 — the five-result arc R-135→R-139 (each twt-reviewer
  HOLDS; suite 367→377):*** *existence + binding SIGN (R-135: 1.89% strictly below the
  two-defect threshold; first SC-1 `N = 2` datum); deuteron QUANTUM NUMBERS (R-136:
  `I + J` odd ⇒ ground state `1⁺, I = 0`, scalar dibaryon forbidden; W-LIVE-4 second
  anchor; headline literature-known, credited); PION-MASS ROBUSTNESS + SCHEME FORK
  EXECUTED (R-137/R-138: margin survives across the entire fork 1.89/1.96/1.87%;
  `1/Θ₀` fit-invariant; baseline stays massless — bookkeeping decision); TENSOR FORCE
  (R-139: dipole-dipole law with the OPE radial structure exact, from the banked tails;
  D4-anisotropy premise-drift corrected, N39; `η_DM` 1/144 preserved as the P2-5-gated
  subleading row). LOCATED residual → Paper-2 refinement: binding MAGNITUDE
  (~113/~124 MeV rigid-rotor overbinding; torus + beyond-rigid-rotor quantization).
  Adjacent rows: CK inertia (`Σ_c−Λ_c`); OPE-projection strength face.*
- **Vector-meson dynamics** — the σ/ρ/ω CANDIDATE identifications of paper §C.5.11 lifted to
  dynamical content once §D.5 closes.
- **W-LIVE-4 spin-statistics closure** — the named routes tested for whether any promotes
  fermionic Skyrmion quantization from SELECTION to DERIVED. *(W1's finite-ℤ_3-holonomy
  instance closed-negative 2026-07-02, N35 — W1 merged into the gauge-sector item above;
  remaining: W2 §D.5 driven-flow, W3 V2 §3.2 refinement.)*
- **Soliton-fluctuation one-particle pole (R-123 residue ii)** — compute the linearized
  fluctuation spectrum around a defect-bearing configuration (§D.4.6 Paper-2 carve-out); a
  one-particle pole at `k_4 = ω/c_meta` closes R-123's residue (ii) and upgrades the
  WP-MASS-MEASURE dispersion chain to fully implied-by-banked. *(Leverage RAISED 2026-07-02:
  with the cyclotron EOM banked as R-124, residue (ii) now gates chains (1), (2), and (5)'s
  FORM — three of the five signature chains — the item's critical path.)* *(HALVED same day,
  R-125: the existence/location half is derived — the defect's phase collective mode sits
  exactly at `k_4 = ω/c_meta`; the computation's remaining target is (H1) normalizability +
  (H2) that this mode is THE one-particle pole.)* *(R-126 adds multiplet-level support: the
  whole exact symmetry-mode catalog reads ONLY `±ω/c_meta` — the (H2) skeleton on the
  defect-linearized side; plus the named boost-family handle for a chain-(2) second angle
  and a DM-induced right-sextet lift as a predicted fine structure / falsifier face.)*

---

# Section 12 — Closability classification (2026-07-02)

*Status: **FRAMING / program-planning assessment** — a judgment layer over the worklist,
coordinator-directed (2026-07-02), developed after the N35/N36 banking pass. It classifies
every open item by **what actually blocks it** and states the realistic closure route with
concrete leads. Nothing here changes any tier in Section 1; the worklist carries the same
classes as per-item tags. Re-assess whenever a class assignment's premise moves (each premise
is cited).*

## The central diagnosis

The obstacle to the remaining frontier is **not**, for most items, the wavefront-locking
epistemology (being made of the wave one measures). It is the **static/dynamic fault line**
the strategic map already names: the Clifford/D4 static structure is essentially one-to-one
(which is why Layer 1 kept winning), but a static structure is compatible with **many**
dynamics — *under-determination by construction*. One cannot derive a kernel from kinematics;
A-2 is honestly a placeholder axiom. Wavefront locking walls off only a narrow class of
**absolute substrate normalizations** (Class 4 below) — plus, in a worst case worth watching,
the memory-kernel fork.

## The four classes

**Class 1 — closes with ordinary (possibly hard) well-posed work.** No gate, no missing
principle: constructions and computations that are well-posed today. Some are decade-class
effort; none are blocked.

**Class 2 — closes conditional on the #1-gap kernel; realistic closure form is
input-plus-over-determination.** Two honest routes:
- *(2a) Invariant-hunting* — more monostability-class forced facts, where statics corners
  dynamics ("stable defects exist ⇒ memoryless kernel excluded", R-114, is the existence
  proof that this route is real; the s=3 Adler-zero and the Θ_rel Z3-isotropy dichotomy are
  the other two wins of this kind). Each such fact shrinks the kernel's allowed family.
- *(2b) Kernel-as-counted-INPUT + registry over-determination* **[EXECUTED 2026-07-22 → §E.5,
  R-153–R-158: a Grade-B constraints-by-construction candidate CLASS proposed at CANDIDATE; the
  executable rank-deficiency confirmed by search; the over-determination remains conditional on
  a gated forward map]** — promote a minimal causal
  kernel family (1–2 dials: amplitude + relaxation scale) to an honest, counted INPUT, then
  over-determine it across the pending-values registry once N33's named missing numbers exist
  (a real macromolecule-interferometry floor number; the `Λ ~ H²` residual coefficient; a
  genuine sum-rule / Kramers-Kronig datum; independently-justified frequency assignments per
  anchor). Under (2b), α_em, g, α_s, α_W, the mass scales, and the CKM ladder become
  **derived-given-2-inputs** — weaker than the ab-initio ambition, still a collapse of ~15 SM
  parameters onto ~2 dials, and *falsifiable by the over-determination itself* (a candidate
  kernel that lands α but fails 1/T_2 is a contradiction the registry surfaces). The
  Bell-memory bridge ("one dial, two operational windows", R-030) is why the
  one-usable-anchor problem N33 found looks like data poverty, not a structural theorem.
An ab-initio (input-free) closure of Class 2 would require a genuine dynamical selection
principle the framework does not currently possess (SOC universality was the one candidate;
structurally disfavored per the Floquet limit-cycle lean, not excluded).

**Class 3 — menu-picks; not expected to close, and that is not a failure.** Genuine
contingent picks per canon §2 menu-vs-pick: geometry offers the menu, nature picked, and a
pick is an initial condition, not a pending derivation. Members: `K = 2/3 ⇔ c = √2` (six
forcing routes investigated NEGATIVE, V2 §19.4 — the strongest evidence any item on this
list is a permanent pick); the `D/J ≈ 0.79` value (cross-validated at ~1.1%, but a value); the lepton
amplitude scale `A`; the `+e_4` orientation (a cosmological IC). Watch-item on the boundary:
the orbit-phase → ℍ-unit identification behind the generation count (R-071's LOCATED
residual) — could yet close via dynamics (Class 2) or settle as a pick.

**★ A Class-3 member CLOSED, and the class survives the counterexample stronger.** `weak = SD`
was listed here, in wording now WITHDRAWN (RV-7), as "one bit of a real two-option chiral menu,
neutrino-linked". It has been
**removed from Class 3**: the menu was never two-option (it is three conjugacy classes, computed),
and it **closed** — both alternatives are refuted, so there is no pick left to make (R-171,
R-079). The honest reading of the counterexample is not that Class 3 was wrong to exist but that
its membership test was never applied: *a menu asserted in prose is not a menu that has been
computed*, and until the enumeration is run, "not expected to close" is a prediction rather than a
finding. The remaining members are re-affirmed on that stricter test — `K = 2/3` has six
investigated forcing routes behind it, and `+e_4` is a cosmological initial condition, not a menu
at all. What `weak = SD` cost to leave the class is one structural premise (**A-P2**, since stamped
ENDORSED — RUL-084) plus one measurement.

**Class 4 — knowability-limited: the genuine wavefront-locking wall.** Absolute substrate
normalizations that inside-frame observers cannot reach in principle, because the inside
frame measures contrasts against the homogeneous background:
- A **uniform `c_meta ≠ c` offset** — provably without observational signature (R-045 states
  this openly; also gauge-like, so physically inert). Permanently walled, and harmlessly so.
- **Absolute `Λ`** beyond the O(1) Sakharov bracket — currently reachable only through the
  gravity channel. **UNLOCKABLE**: P2-5 delivering `Λ·ℓ_S` as a dimensionless pure number
  moves this to knowable (the corpus's own "knowability handle").
- The **N22 branch-(a) grain endpoint** (if the R→0 resolution is the conservative
  D4-3-body-contact parameter, the values are a grain-scale INPUT of Λ/f_π knowability shape).
- **WATCH-ITEM — the fading-vs-hysteretic fork.** It joins this class only if ALL inside-frame
  observables prove fork-blind. The linear-face safety chain that protects QM (R-117, WP-DC2)
  also *screens* the fork in the macromolecule window (N34 died partly on exactly this).
  Current expectation: fork-sensitivity survives in nonlinear observables (τ_mem hysteresis,
  plausibly the `Λ ~ H²` residual) plus the theory-side discriminator (whether hysteretic
  τ_mem clears the SNIC/Adler locking threshold, `theta_rel_rotating_wave_escape_located`).
  **UPDATE 2026-07-05 (W3.3/A1, N46, `theta_rel_fork_escape_kernel_number_governed`):** the
  theory-side discriminator was COMPUTED (explicit non-Markovian memory sim) and does NOT cleanly
  resolve the fork — above the SNIC threshold the escape/lock outcome is governed by kernel NUMBERS
  (α/α*, τ·ω, barrier height) NON-MONOTONICALLY, not by the fading-vs-hysteretic branch LABEL (the
  sticky-hysteresis handle is REFUTED as a clean discriminator: a small barrier PROMOTES the escape).
  So the theory-side route does NOT rescue the fork from this class on its own; it re-locates it on
  three #1-gap numbers. If fork-discriminating observables keep failing to materialize, that is the
  signal this epistemic barrier is real.

**Scope-gap note (outside the classes):** the ~98% of Ω_DM is not *blocked* — it is possibly
**absent**: the framework may simply not contain that answer. §E.1.3's deliberate scope
statement is the right posture; DM-V2-1's surviving leads are Class-1 work on a question the
framework might not own.

## Per-item classification and closure leads

| Item | Class | What blocks it | Closure lead(s) |
|---|---|---|---|
| P2-1 — `S`/`Θ_rel`/`Im χ` (the #1 gap) | **2** (the kernel item itself) | Static/dynamic under-determination; N33: registry currently rank-deficient (one usable anchor vs ≥2-parameter kernel) | (2a) invariant-hunting for further monostability-class forced facts; (2b) minimal kernel family as counted INPUT + over-determination once N33's four named missing inputs exist — **(2b) EXECUTED 2026-07-22 (§E.5, R-153–R-158): the KS campaign proposed a Grade-B constraints-by-construction candidate CLASS; the rank-deficiency stands CONFIRMED-BY-SEARCH (344 candidates); selection deferred to the virgin-sector discriminators (P1/P2) or a gated forward map**; ~~resolve the fork on its own dynamical terms via the SNIC/Adler threshold computation~~ **the SNIC/Adler fork computation is DONE (W3.3/A1, N46) and does NOT cleanly resolve the fork — the escape/lock outcome is set by 3 kernel NUMBERS (α/α*, τ·ω, barrier) non-monotonically, not the branch label; the fork now needs those 3 numbers from the kernel, or a structural bound on the barrier height** |
| P2-2 — texture tetrad / absolute EH coefficient | **1 (structural part — BANKED 2026-07-05, R-145; Gauss face EXECUTED same day, R-149) + 2 (coefficient)** | Was: 6→4 frame reduction unbuilt. Now: the reduction is banked structural (R-145 `texture_frame_6to4_reduction`) AND the Gauss-equation face is executed (R-149 `texture_gauss_equation_riemann_closure`: Riem(g) ALGEBRAIC in the first-order data (E, Ω, dE), signature-blind across the whole nondegenerate menu — the first-order scaffold is CLOSED, R-145's would-change-if (3) fired negative); the EOM owes ONLY the signature pick; absolute coefficient still needs the #1-gap propagator | Remaining: the `C_T` spin-2 spectral sum itself — the integrand's shape is fixed (quadratic in (S, [Ω,Ω]), R-149 FRAMING), and **the mode measure now enters through AT MOST 4 kernel moments (W3.1 / R-151 `ct_kernel_moment_count_symmetry_reduction`, 2026-07-05, suite 399→400; twt-reviewer HOLDS + 3 independent methods):** the R-145 product symmetry SO(4)_tangent × SO(3)_SD × SO(3)_ASD forces the integrand into an 8-dim space of invariant quadratic forms (4 parity-even + 4 parity-odd, SD/ASD parity-conjugate) — C_T reduced from an unknown FUNCTION to ≤4 NUMBERS *given the unbroken product* (an upper bound; a diagonal-locking raises it; the exact ≤4 needs the spin-2/Ricci sub-projection). Still needs: the kernel VALUES themselves; the (1,3) signature pick (vacuum EOM); the gauge-projection premise U2 (unchanged) |
| P2-3 — QCD UV gate (`β_3 < 0`) | **1 (sign) — CLOSED POSITIVE-conditional-generic 2026-07-05 (R-148) + 2 (running/DGLAP)** | Was: sign genuinely open (N7). Now: `β₃ ≤ 0` AF-SIGNED at the dressed one-coupling level via the dispersive/I-13 package (`marginal_skyrme_beta3_sign_dispersive`; vertex sign derived in-suite; wrong-sign risk REMOVED, conditional on I-13 with revert clause) — NOT AF-achieved: additive f²-loop drift, no antiscreening | Remaining (Class 2, the kernel): the DGLAP structure, the magnitude, the UV completion above Λ_cell; the a-theorem lead NOT PURSUED (13.3); first-build refutation lesson = N42 |
| P2-4 — gauge sector explicit construction | **1** (well-posed; high payoff) — legs 2+4 advanced 2026-07-03 (R-140, R-141); leg 3 closed 2026-07-04 (R-143) | Was: construction not yet done. Now: leg 1 banked (48/66); leg 2 STRUCTURAL CORE banked (R-140: explicit plaquette holonomy — pure-gauge lift explicit, chirally-blind Spin(4) curvature, per-sector su(2) closure ⇒ instanton π₃-obstruction absent); leg 3 STRUCTURAL CORE banked (R-143: background topologically neutral per sector — ι-mechanism exact; D4 charge operator `576·ε(F)`/4π² calibrated; explicit compactly-supported SU(2)₊ winding-1 configuration, charge → 1, exact SU(2)₋ transparency; cross-term closed form; R-088 index half already banked); leg 4 ANSWERED-AT-PARITY (R-141: induced level ODD, conditional on P1/P1b ⇒ fermionic INDUCED; W1 CLOSED-CONDITIONAL POSITIVE) | Remaining — ALL kernel-class (the item's gate-free frontier is EMPTY): the fluctuation Yang-Mills action + coupling (kernel-adjacent); the instanton SOLUTION/action value (kernel-adjacent); the SUBSTRATE COMPUTATION of the induced worldline term (parity answered; magnitude/value face open) |
| P2-5 — cell-formation mechanism | **2** (dynamics) — **and the Class-4 unlock** | Self-organization is kernel physics (memory Role 1); Gate B neutral in V2 | Drive the Gate-B question with the kernel's cell-formation role; deliverable: `Λ·ℓ_S` as a pure number — pins absolute G, moves absolute-Λ from Class 4 to knowable, and closes SC-2's cell-order requirement |
| P2-6 — L-orbit QCP / L2 mechanism (`ν = 3π/2`; K_c) | **2** | N31: static LSWT route ELIMINATED; single named route remains | §9.6 kernel must produce the SPECIFIC renormalization factor `(19/2)√38 ≈ 58.6` between bare LSWT stiffness and K_c — an unusually sharp numerical target for any kernel candidate (a free over-determination row for the 2b program); DQCP-literature comparison for the ν = 3π/2 candidate value (no empirical exponent is available to compare against — the former coincidence rode the excised conversion) |
| P2-7 — multi-Skyrmion BVP (deuteron) | **CLOSED AT SCOPE 2026-07-03** (R-135–R-139) | Was: genuinely unattempted. Now: existence + binding SIGN banked (R-135: 1.89% strictly below threshold; first SC-1 `N = 2` datum); quantum-number face banked (R-136: `I + J` odd ⇒ ground state = deuteron `1⁺, I = 0`, scalar dibaryon forbidden; W-LIVE-4 second anchor); pion-mass robustness banked (R-137: margin survives at physical `m_π`; −34% inertia shift = second scheme axis); refit branch executed + adjudicated (R-138: `(108.26, 4.843)`, margin 1.87% at refit, ordering fork-robust, `1/Θ₀` fit-invariant, baseline stays massless) | Residual rows (named): binding MAGNITUDE ~113/~124 MeV rigid-rotor overbinding (torus + beyond-rigid-rotor quantization — Paper-2 refinement); OPE-projection strength face (g_πNN-analog); CK bound-state inertia (`Σ_c−Λ_c` adjudicator, both candidates standing per R-138); `η_DM = (D/J)²/144` D4 face (P2-5-gated, preserved per N39). Tensor force DONE (R-139) |
| P2-8 — active-sterile overlap (`m_ν`) | **2** | Overlap magnitude is Θ_rel/dynamics-gated (§C.3.12) | Inherits R-123: state the overlap as a front-restricted rotor-frequency matching; absolute scale waits on the kernel; also the DM-V2-1 Z3 handle (would need breaking one-Dirac-eigenvalue-per-generation — likely a clean negative to bank en route) |
| WP-MASS-MEASURE — residue (ii) (one-particle pole) | **1** (halved 2026-07-02) | Existence/location half DERIVED (R-125, symmetry shortcut): an exact collective mode sits at `k_4 = ω/c_meta`; remaining: (H1) normalizability vs the carrier + (H2) identification as THE one-particle pole | The §D.4.6 shape-mode computation now needs only to confirm the derived mode is the lowest localized pole — a sharper, smaller target; closing (H1)+(H2) upgrades chains (1)/(2)/(5)-FORM to fully implied-by-banked; new falsifier face: a pole elsewhere than `ω/c_meta` kills `m = k_4` |
| WP-MASS-MEASURE — chain (1) cyclotron EOM | **CLOSED 2026-07-02** (R-124) | Was: point-defect EOM in external F unbuilt | Banked as `charged_defect_worldline_eom_cyclotron` (twt-reviewer HOLDS + 2 amendments applied): `f = qF·u` forced by rest-anchor + covariance premise, Schur commutant-2 cross-check, `ω_c = qB/m` exact; inherits the R-123 residue-(ii) conditional like chain (2) — residue (ii) now gates three of five chains |
| WP-MASS-MEASURE — residue (iii) (`E → B_a` hand-off) | **RESOLVED-AS-SELECTION 2026-07-02** (R-127, Class 1 — no defect dynamics needed) | Was: hand-off as a construction unbuilt | `front_phase_handoff_selects_winding_axis` (twt-reviewer HOLDS + 2 sweep fixes): exact ideal-projection dichotomy — only `û = ±B_a` reads as a propagating phase in R-020's forced line; other ℍ axes = spin precession; `E` leaves the Cl(4,0) ideal (density-node shadow). No conversion owed; the mass phase rides the winding blade. Still open: EOM-level axis lock; Q-orbit analog |
| WP-MASS-MEASURE — chains (4) decay-energy, (5) oscillation values | **2** | (4) is the Im χ energy budget; (5) needs the mass mechanism + mixing (PMNS defused) | (4) carries a free falsifier face — anomalous missing energy in precision decay spectra would *measure* Im χ (an over-determination row for 2b); (5) beat-phase FORM already inherits from R-123 conditional on residue (ii) |
| W-LIVE-1 — up/down mirror value | **2** | N32a: all three handles = one open dial µΨ₀ (= ⟨I_4⟩ condensate coefficient, §10.5(d)); N37 (2026-07-02): the dial RUNS between generations — `c_common = c_lepton` REFUTED at gen-2→3 (top-free), gen-1→2 agreement survives gen-1→2-only | The four-sectors-one-dial row is now a RUNNING-dial row: a fifth constraint face for 2b (the inter-generation drift, implied 1.69 → 0.56) but no one-number closure; gate-free partial DONE-NEGATIVE (`updown_mirror_multigen_avg_vs_lepton`) |
| W-LIVE-4 — spin-statistics | **1 via P2-4** (W1); **2** (W2); open-ended search (W3) | W1 reduced 2026-07-02 (N35) to P2-4's induced-level fork; W2 kernel-gated; W3: three audits found nothing. 2026-07-03 (R-136): the fermionic SELECTION gains a second independent empirical anchor (bosonic branch ⇒ bound scalar dibaryon at `B = 2`, refuted by the deuteron) — fork status UNCHANGED, evidence not derivation | W1 **CLOSED-CONDITIONAL(P1+P1b+Q), POSITIVE (R-141, 2026-07-03)**: induced level ODD at the parity level — FR fermionic quantization INDUCED-given-(P1)+(P1b), revert clause named (refusing P1b restores the selection with both anchors standing); the substrate-computation face remains open; W2/W3 relevant only if P1b falls |
| DM-V2-1 — dark matter | **GATE-FREE FRONTIER EMPTY — both V2-era leads ADJUDICATED-NEGATIVE 2026-07-05 (R-146 differential coupling; R-147 wave-train phase defects)** | Sterile-RH leads resolved-negative or refined-closed; the h-source of any grade-2 excitation IS the E·B-type L–Q cross term (= the EM-bridging resource); the blade, not the topology, fixes h; no π₁ protection; grade-3 doubly dead | Residue = ONE located loophole: the grade-0×grade-4 amplitude channel, carrying TWO named EOM conditions (amplitude modes exist; EM-dark cores couple into c·I4) — kernel-gated, **Class 2**; honest posture REINFORCED: the framework may not contain the dominant-DM answer; in-scope DM = sterile-RH ~2% (R-121/R-122) |
| SC-1 — multi-defect well-posedness | **1** (hard PDE; SECOND `N = 2` datum banked 2026-07-05) | Multi-defect Cl(4,1) wave equation with N back-reacting sources unconstructed; R-135 datum = ansatz-reduced static BVP; **R-144 datum = full-3D ansatz-free static minimization (the torus; below threshold at matched grid, stall-vs-stall 1.79/3.06%, ≥ 2.95% after the reviewer's B1-side probe; charge-conserving flow)** — the STATIC variational face is now coherent without reduction; the Eulerian reframing (R-050a) hardened at the static level | Next: the dynamical multi-defect EOM face (kernel-gated — the genuine core); optional B ≥ 3 static third datum; the massive-pion full-field run (named follow-up) |
| SC-2 — cell-order requirement | **2** (tied to P2-5) | Needs the cell-formation mechanism to show local coordination without space-fixed cubic order | Falls out of whichever mechanism closes P2-5; until then remains the load-bearing OPEN for §B.6.3 |
| Isotropic dim-6 LV coefficient `η⁽⁴⁾` (R-165 / VG-6 / N52) | **2** | Blocked on the #1-gap kernel's strain-mode dispersion. Emphatically NOT Class 4: knowability is precisely what does *not* limit it — the number is already measured; what is missing is the substrate computation to compare against it | Four named handles (N52): a symmetry forcing the isotropic quartic coefficient to vanish; `Λ_LV` decoupled from the Sakharov cutoff; ≥6–9 orders of form-factor suppression *plus* a photon-sector account (the requirement is `Λ`-dependent: which-Λ ruled 2026-07-30, dispersion consumers take `Λ_L = 1/a ∈ [0.39, 0.73] M_Pl`, naive `η⁽⁴⁾ ∈ [1.9, 6.7]` / 3–9 orders — R-037); heavy UHECR composition (worth only 1–2 orders, and nothing for the photon) |
| K_c kernel form | **2** | See P2-6 | The `(19/2)√38` target |
| `K = 2/3`, `D/J` value, `A`, `+e_4` | **3** | Menu-picks (`weak = SD` **left this class 2026-08-21**: its menu was computed and CLOSED — R-171/R-079) | None expected; the framework's win is the count (four counted INPUTs + measured `G_N`, not nineteen — Branch B ruling 2026-07-30) |
| Uniform `c_meta` offset; absolute `Λ`; N22 branch-(a) endpoint | **4** | Wavefront locking (inside frame measures contrasts only) | `c_meta` offset: permanently walled, harmlessly (gauge-like); absolute `Λ`: unlocked by P2-5's `Λ·ℓ_S`; N22(a): resolved only by winning the N22 fork toward branch (b) |

## Reading the priorities through this lens

**FRONTIER STATE 2026-07-05 (end of the coordinator-directed Class-1 sweep):** the Class-1
gate-free frontier is EMPTY — P2-2 structural half (R-145), P2-3 sign (R-148,
positive-conditional-generic), DM-V2-1 both leads (R-146/R-147, negative), on top of the
already-closed P2-4 legs / P2-7 / W-LIVE-4 W1 / WP-MASS-MEASURE structural faces. Gate-free
leftovers are compute-heavy refinements (beyond-rigid-rotor quantization; massive full-field
run; optional B ≥ 3) and the ω ≠ 0 co-rotating Hessian face. The next session belongs to the
Class-2 program (2a + 2b); the R-145-named Gauss-equation face is the natural entry.
**[2026-07-05, session tail: that entry is EXECUTED — R-149 closed the Gauss face (Riem(g)
algebraic in the first-order data; the C_T integrand's shape fixed, the kernel's mode
measure now the single missing C_T ingredient). The Class-2 program is underway; remaining
2a candidates: further monostability-class forced facts; 2b: the over-determination table
(P2-6's `(19/2)√38`, W-LIVE-1's running µΨ₀).]**
**[2026-07-05, W2.1: the over-determination table is now BANKED as an engine artifact —
`kernel_overdetermination_table` (R-150, suite 397→398; twt-reviewer HOLDS). N33's prose
finding is graduated into a self-validating, checkable dashboard: 10 registry rows, exactly
ONE usable anchor (KSS/GW), RANK-DEFICIENT against a ≥2-dial kernel — a live invariant whose
count increments when a genuine new (frequency, value) anchor is manufactured (N33 input (3),
next = the W2.2 static sum-rule datum). The 2b infrastructure's first piece is in place.]**
**[2026-07-05, W2.2 (N43): the first attempt to lift the rank-deficiency — a KK-safe/FDT-free
static-susceptibility datum from the canted-D4 LSWT (`χ_long = 1/√38 J`) — is WRONG-OBJECT for
the KSS/GW usable anchor (order-parameter magnon χ_θθ vs stress-tensor shear viscosity η, SAME
cell layer, DIFFERENT operator/channel); the count stays 1. The datum is channel-matched to the
K_c row instead (its bare static-susceptibility companion). A precise located gap: the next
anchor attempt must target the STRESS-TENSOR / shear channel.]**
**[2026-07-22, the KS campaign (run in `simulator/`, corpus frozen throughout; integrated on
coordinator sign-off): the Class-2b route is EXECUTED — a Grade-B constraints-by-construction
candidate CLASS for the kernel FORM is proposed into the paper as §E.5 (R-153–R-158; imports
I-14 Preisach / I-15 Floquet registered in Section 13). The executable rank-deficiency is now
confirmed BY SEARCH, not just by census; the selection within the class and every #1-gap
magnitude stay gated — the 2a invariant-hunt and the anchor-manufacture program continue
unchanged.]**

The **Class 1 queue** (nothing blocked; ordered by value × tractability): P2-4 (resolves
spin-statistics for free) *(2026-07-04 status: legs 1/2/3 structural cores ALL banked —
R-140, R-143 — and leg 4 answered at parity, R-141; the item's GATE-FREE FRONTIER IS EMPTY,
every remaining face is kernel-class — the queue's next gate-free items are the P2-2
structural half and P2-3's sign lead)*, WP-MASS-MEASURE residue (ii) *(leverage raised: gates chains
(1), (2), (5)-FORM since R-124; HALVED by R-125 — existence/location derived; (H1) then
DISCHARGED by R-130, 2026-07-02 — the mode's excess inherits the defect's own localization
exactly; the (H2) QUANTIZATION STEP given its skeleton by R-131, 2026-07-03 — compact phase
modulus ⇒ discrete charge tower with leading spacing exactly ω, kernel-form-free; remaining
target (H2) pole uniqueness + moduli↔pole identification + (T-kernel) tail; *(H2) core ANSWERED at the structural level 2026-07-04, R-142: label half closed via the clock-orbit identity; uniqueness conditional on the named (Q)+(S)+(M) set with the breathing-channel Hessian engine-certified; residue (ii) → kernel faces + anchoring face + named premises*)*, ~~the cyclotron worldline EOM~~
*(CLOSED 2026-07-02, R-124 — the first Class-1 queue item to close)*, P2-7
(which seeds SC-1), ~~the W-LIVE-1 multi-generation cross-check~~ *(FIRED 2026-07-02 → DONE-NEGATIVE, N37)*, ~~the P2-2 structural half~~ *(BANKED 2026-07-05, R-145 — the 6→4 reduction is structural and selection-free; the EOM owes only the signature pick; next gate-free queue item: P2-3's sign lead)*.
The **Class 2 program** is ONE program, not eight items: hunt invariants (2a) while building
the over-determination table (2b) — every Class-2 row above contributes either a forced fact
or a constraint row, and P2-6's `(19/2)√38` and W-LIVE-1's four-sectors-one-dial are the two
sharpest constraint rows currently known. Classes 3 and 4 are recorded so that no future
session mistakes a pick or a wall for an unfinished derivation.

---


# Section 13 — Import Registry (2026-07-05)

*Coordinator-directed (Yaer, 2026-07-05), following the R-145-session import audit. This
registry is the single authoritative list of every EXTERNAL theorem or result whose conclusion
is load-bearing anywhere in the corpus. Its purpose is the honesty test the tier system cannot
perform alone: a tag says a result is conditional; this registry says WHAT it is conditional
ON, whether the ontology justifies that premise, and what would retire the import. Maintenance
is MANDATORY: see methodology principle 8 (Section 6) and canon §2 — an import without a row
here is a banking-stopper, same class as a phantom cite.*

**What counts as an import.** An external theorem/result whose conclusion is used load-bearing
and whose PREMISES are not engine-checkable substrate facts. **Pure mathematics is NOT an
import** (homotopy/π₃/π₄ classifications, Schur's lemma, Derrick's virial identity, Frobenius,
Janet–Cartan, linear algebra): its hypotheses are verifiable substrate-side, and the engine
checks them. The import class is, in practice, QFT / many-body / statistical-mechanics
theorems whose premises (unitarity, Lorentz invariance, thermal equilibrium, a standard QFT
vacuum, specific field content) are exactly what TWT must derive or may violate.

**The level discriminator (load-bearing for the whole table).** TWT derives QM inside-frame
(§B.3) and protects emergent Lorentz invariance (§B.1.4, §B.6.3); the substrate itself is
Euclidean, driven-dissipative, and non-unitary at the NESS. Therefore:
- an import applied at the **inside-frame / effective level** (quantizing collective
  coordinates, spectral arguments in observable channels) rides banked TWT results — its
  premises have standing;
- an import applied at the **substrate level** (loop expansions over substrate modes,
  positivity of the substrate measure, equilibrium identities) rides premises only the #1-gap
  kernel can confirm or refute — its ontology-status is OPEN until then. This is the canon's
  inside/outside method applied to theorems: inside-frame theorems operate within their
  jurisdiction; substrate-level imports are placeholders for missing kernel derivations.

**Premise-status legend.** JUSTIFIED = premises are substrate properties (derived or
engine-checked) or the import was recast as one. NAMED-CRACK = equilibrium-premised on a
driven substrate; valid at the equilibrium anchor with the deviation named and gated
(implicitly "up to Θ_rel-class corrections", not yet quantified). OPEN = unitarity/Lorentz
premised at a level where TWT has not established them; conditional as tagged. N/A = negative,
defensive, definitional, or inherited-by-isomorphism uses with no forward exposure.

## 13.1 Load-bearing conditional imports

| # | Import (external result) | Used at | Level applied | Premises required | Ontology status | Retirement handle |
|---|---|---|---|---|---|---|
| I-1 | **D'Hoker–Farhi 1984 / Witten 1982** induced-term theorem (integrating out chiral fermions induces the topological worldline term) | R-141 (P1), §C.4.6, §B.3.5 — the spin-statistics decider | Effective (fermion determinant on the baryon worldline) | 4D chiral fermion determinant; unitary, Lorentz-invariant effective action; the lock-channel identification (P1b, separate CANDIDATE premise) | **OPEN** — the fermions are themselves emergent windings; tagged IMPORTED-AS-CITED "to-be-verified"; result DERIVED-given-(P1)+(P1b) with revert clause | The substrate computation of the induced term (R-141's named remaining face, kernel-adjacent) — retires I-1 entirely. NOTE (R-161, 2026-07-27): the lock-channel identification P1b is now SPLIT — its structural half is DERIVED-A-given-C1′–C4′; the premise this row rides is the reduced P1b-DYN |
| I-2 | **Atiyah–Singer index theorem** (chiral zero-mode count on the instanton background) | R-088, §C.5.5 — ΔB = ΔL = N_gen selection rule; cited at parity level by R-141 | Effective (Dirac operator on the derived background) | Elliptic operator on a smooth background + the FERMION-CONTENT identification (TWT's own, banked) | **JUSTIFIED-conditional-on-content** — the index step is mathematics once operator + content are given; the content identification is banked TWT structure; the RATE face is kernel-gated as banked | A substrate-level mode count on the R-143 lattice access (the D4 carrier is now structurally in place) |
| I-3 | **Sakharov induced-gravity one-loop** (heat kernel / Seeley–DeWitt; scaling form `M_Pl² ~ N·Λ²`) | R-037, §B.6.2 — the entire induced-EH magnitude bracket; the `a ↔ ℓ_Pl` identification this inversion effects is the renormalization dictionary's **length/scale face** (worklist dictionary item, sixth face, 2026-08-16) | **Substrate-level loop** | A standard QFT vacuum for substrate modes; validity of the one-loop expansion; covariant regularization | **OPEN** — the substrate is a driven-dissipative NESS, not a QFT vacuum; the scaling FORM is tagged "QFT INPUT" in-suite; `N_eff = 6` is generic-given-dim-4 (canon §5) | The #1-gap kernel supplying the actual spin-2 spectral sum (`C_T`) — via the R-145-named Gauss-equation face; P2-2 Class-2 half. **NARROWED by R-163 (2026-07-27)**: computed on the derived linear face, the flat-band mode measure is derived and finite (no regularization choice), reducing this row's premise triple to TWO named assumptions — OA-LF-i (NESS ground-state occupation, the STATE) and OA-LF-ii (grain-scale covariant curvature coupling, the OPERATOR, carrying ~93% of the integral's support: the old regulator freedom relocated and localized, NOT removed). Status stays OPEN; the retirement handle is unchanged. **REGULATOR COEFFICIENT RESOLVED (2026-07-29) + WHICH-Λ RULED (coordinator, 2026-07-30):** the apparent three-way `c_reg` disagreement was ONE coefficient in three `Λ`-variables — `1/12` exactly in the proper-time variable (`sakharov_induced_gravity`), `≈1.8 = c_lat/12` the same computation in `Λ := 1/a` (R-163), `~1` a never-computed placeholder. The ruling SPLIT the symbol: `Λ_S = √(2π) M_Pl` (scheme; this row's Sakharov bookkeeping; absorbs the determinate unit fix — `Lambda_over_MPl = 4π` is against the REDUCED `M_red = M_Pl/√(8π)`, i.e. `2.51 M_Pl` non-reduced) vs `Λ_L = 1/a ∈ [0.39, 0.73] M_Pl` (lattice-dispersion consumers per the scoped §B.6.2 assignment). The R-037 wide bracket is RETIRED |
| I-4 | **Volovik's Gibbs–Duhem identity** for self-sustained media (**read with I-25**, the prior-art registration of the same author's vacuum-as-medium *ontology* — this row imports only the thermodynamic identity; the ontological kinship is registered separately and carries no forward exposure) (`ε − μn = −P = 0` ⇒ gravitating vacuum energy vanishes in equilibrium) | R-047, §B.7.4 — the Λ-catastrophe dissolution | Substrate-level thermodynamics | Thermal EQUILIBRIUM at zero external pressure; self-sustainment (the substrate satisfies the latter by construction) | **NAMED-CRACK** — the substrate is driven, not equilibrium, and the deviation IS the gated residual (§E.1, VG-2); valid at the equilibrium anchor. **Narrowed 2026-07-29:** the crack buys a *magnitude*, not an epoch law — the `ρ_vac ∝ H(t)²` reading of that residual is excluded (N54), so the import no longer underwrites a dark-energy claim | The off-equilibrium computation at §D.5 (#1 gap) — quantifies the crack rather than removing the import |
| I-5 | **Semiclassical soliton toolbox**: ANW collective quantization, rigid-rotor band, Callan–Klebanov bound-state method, rational-map ansatz, FR quantization framework incl. the axial `K₃ = 0` selection rule (Krusch-class) — the Finkelstein–Rubinstein construction itself is separately registered as **I-20**, which carries its §B.3.5 spin-statistics face; this row carries only its use inside the hadron machinery. **AMENDED 2026-08-12 (ADJUDICATION3 §3; ruling R3(a)):** the soliton-mass identification `m(rest) = E₀(static minimum)` this toolbox silently carried is now STATED and COUNTED as the §A.4 `m = E₀` premise (`mass_equals_elastic_cost_premise`) — this row's consumers cross it wherever an elastic value meets a measured mass (R-133 in calibration mode; R-144 does NOT use it — dimensionless margin) | R-025, R-133–R-144, §C.1 — the entire quantitative hadron arc | Inside-frame / effective (collective-coordinate quantization) | Semiclassical QM; adiabatic separation of collective modes; the imported selection-rule machinery (R-136: "literature-known, credited; consistency-checked in-engine") | **JUSTIFIED at the emergent level** — QM is derived §B.3, so quantization operates in-jurisdiction; method artifacts honestly tracked (rigid-rotor overbinding ~113/124 MeV; the `Σ_c−Λ_c` CK-inertia fork) | Beyond-rigid-rotor quantization (P2-7 residual row); the dynamical multi-defect EOM (SC-1 core, kernel-gated) |
| I-6 | **SM renormalization-group run-down** (gauge-coupling running between the unification and measured scales) | §C.4.5 — the `3/8 → M_Z` run-down (the earlier "→ 0.231" reading is **RETRACTED**: with TWT's own SM content the run-down from the ruled `Λ_L` lands at `0.154–0.158` — before the uncomputed lattice→continuum matching premise, §C.4.5; `0.147–0.164` at the retired wide bracket — and reproducing the measured `0.23122` needs an underived `M_X ≈ 1.09 × 10¹³ GeV`), Λ_QCD comparisons (R-133 knock-on). **EXTENDED 2026-07-29 to two loops** (Machacek–Vaughn SM gauge beta functions plus the top Yukawa) for the N55 escape-route closure — same import one order higher, but note it adds two premises the one-loop use did not carry: the **MS-bar scheme** (two-loop betas are scheme-dependent) and the `y_t(M_Z)` input. Both were tested: the two-loop shift is `+0.0004`, i.e. 0.6% of the gap, and is stable to `~10⁻⁵` against ±10% in `y_t` and against dropping the Yukawa entirely; the absolute band carries a `~10⁻⁴` systematic from `α_em(M_Z)` and omitted weak-scale matching, so it is not to be read past the fourth decimal | Inside-frame data bridge | Full SM field content; perturbative unitarity over the run | **OPEN as derivation, SANCTIONED as data import** — canon §7 states plainly TWT does not derive the running; this is the inside-for-data method, not a disguise | TWT-native running (P2-3's β and the P2-1 kernel) — the registry's largest single exposure by headline-value |
| I-7 | **KSRF / hidden-local-symmetry relation** (ρ-meson as gauge boson of the Q-orbit local symmetry) | The rho30 asset (N5's would-change-if handle); not yet load-bearing in a banked R-NNN | Effective | Vector-meson dominance phenomenology; HLS structure | **CANDIDATE-calibrated** — g_ρ calibrated, not derived; flagged as the re-attack template for the colour octet | A TWT derivation of the Q-orbit gauge structure (P2-4 fluctuation-YM face) would replace the calibration |
| I-13 | **The dispersive/S-matrix package** (analyticity, crossing, ≤2 subtractions/boundedness, optical-theorem positivity — the KL+unitarity route R-085 named; FIRED 2026-07-05) | R-148, §C.5.2 — the β₃ sign (AF-signed at the dressed level; the wrong-sign risk removed) | Inside-frame / effective (elastic ππ-class forward channel of the dressed coset Goldstones) | Analyticity/causality of the inside-frame amplitude; crossing; polynomial boundedness (≤2 subtractions); optical-theorem positivity | **DATA-LIKE jurisdiction (13.4)**; the positivity leg PARTIALLY RECAST onto the banked §B.3-derived unitary QM (probability conservation of the derived theory — the 13.3 stability-recast directive satisfied for that leg); analyticity + boundedness NOT yet recast (named residual premises) | Retired by the kernel's own UV spectral computation (the same object that owes DGLAP). REVERT CLAUSE: refusing the package restores R-085's located-gap status (β₃ sign genuinely open); R-148 reverts to the pre-import state; nothing else moves |
| I-14 | **Preisach hysteresis-operator theory** (representation of rate-independent hysteretic operators as hysteron superpositions; Mayergoyz representation theorem = wiping-out + congruency; the Everett function) | §E.5 kernel memory face — the F4 hysteretic branch made representable (R-153/R-155); TWT slot: hysteron = elementary bistable winding/flip unit, the Preisach density = the substrate's flip-barrier distribution (FRAMING) | PURE MATH with checkable hypotheses (the Section-13-EXEMPT class, like KK/Titchmarsh) — registered for completeness | The operator has the wiping-out AND congruency properties (both numerically witnessed, simulator `verify_preisach.py`) | **N/A** (a math theorem; no substrate premise). The TWT hysteron identification is FRAMING | None needed (a theorem); the FRAMING TWT slot retires if the substrate flip-unit picture is refuted |
| I-15 | **Floquet theory** (linear response about a T-periodic drive: monodromy matrix, Floquet multipliers/exponents, the \|trM\| = 2 stability boundary; machinery witnessed on the exactly-solvable Meissner oscillator) | §E.5 kernel drive face (R-153); TWT slot: the wavetrain = the periodic drive, the kernel = linear response about the Floquet state (R-007's driven attractor; the Section-12 Floquet limit-cycle lean) (FRAMING) | SUBSTRATE-level formalism (the drive IS the wave) — but the machinery witness is a lossless toy; no physics premise rides on the witness | Linearity about a periodic reference; T-periodicity of the drive (the wavetrain cadence). **Caveat preserved: the real substrate kernel is driven-DISSIPATIVE (\|ρ\| < 1); the lossless witness validates the machinery, never the dissipative content** | **OPEN** for the substrate application (the actual Floquet state IS the #1-gap object); the machinery itself is a math theorem (JUSTIFIED) | Retired/replaced if the substrate NESS is shown NOT a limit cycle (the fading/SOC arm of `eom_compatible_field_forks` Fork B) |
| I-16 | **DQCP universality framework** (deconfined-quantum-critical-point scaling, Senthil et al. class) | R-055, §C.1.6 — the QCP exponent's `Δ_v` ingredient and the universality frame | Cell-layer critical scaling | A DQCP-class critical point governs the L-orbit `D = J` balance; engineering-dimension counting valid at leading order | OPEN (registered 2026-07-26 per coherence audit — previously unregistered) | Derive the exponent from the §D.5 kernel, or replace the universality frame with a substrate RG computation |
| I-17 | **Witten SU(2) global anomaly** (odd number of LH Weyl doublets ⇒ SU(2) gauge theory inconsistent — the fermion-measure statement over the exempt-pure-math `π₄(SU(2)) = ℤ₂` classification) | §C.4.6 step (i) — gaugeability of weak SU(2)₊ | Inside-frame effective (fermion path-integral measure) | 4D chiral fermion path integral | JUSTIFIED as inside-frame theorem (registered 2026-07-26 per coherence audit — previously unregistered) | A substrate-level derivation of the mod-2 obstruction on the D4 rotor field |
| I-18 | **Gauge-anomaly cancellation package** (mixed-gravitational `Tr Y = 0` and cubic `[U(1)_Y]³` conditions on a chiral fermion spectrum; the colour condition only under a continuous-completion reading, since TWT colour is ℤ₃-discrete) | R-159, §C.2.7 — the corroborating fixings of `c = 1/2` and the right-handed hypercharges; NOT used for the anchor-free identity itself | Inside-frame effective (fermion path-integral measure) | 4D chiral fermion content; a gauged U(1)_Y at the effective level; for the colour condition additionally that colour completes to a gauged SU(3) at that level | JUSTIFIED as inside-frame theorem (registered 2026-07-27) | Revert clause: strike this row and R-159's flagship identity is UNAFFECTED (it is import-free, holding identically in `c`); only the corroborating `c = 1/2` routes (ii)/(iii) and the RH-hypercharge forcing fall back, leaving the native sterile-Dirac route and §C.2.1's posited assignments |
| I-19 | **Dimension-six Lorentz-violation EFT constraint machinery** (the `E² = p² + m² + η⁽⁴⁾ p⁴/M²_Pl` parametrization and the published n = 4 bounds derived in it: Liberati 2013 eqs. 77–78 — photon `−10⁻⁷ ≲ ξ⁽⁴⁾ ≲ 10⁻⁸`, electron `−10⁻⁷ ≲ η⁽⁴⁾ ≲ 10⁻⁶`, proton `−10⁻³ ≲ η⁽⁴⁾_p ≲ 10⁻⁶` at 99% CL for pure-proton composition; Stecker 2009 eq. 18, `δ^π_p < 4.5 × 10⁻²³` from the Auger spectrum above the GZK energy) | R-165, §B.1.5, §B.6.3, §B.6.4, §E.3.3 VG-6, §E.3.5(4) — the entire statement of the framework's dim-6 LV exposure — **and, since 2026-07-27, `eom_constraint_class`'s `E1_dim6_isotropic_LV_ceiling`**, the #1-gap compatible-field boundary's first empirical entry (kept in its own bucket, never renumbered `H12`, precisely so this excision fires against E1 alone and leaves H1–H11 untouched) | **Inside-frame data bridge** (sibling of I-6): the bounds are inferences from observed spectra *within* an effective-field-theory parametrization, imported as data, not derived | (a) an EFT description of propagation at the relevant energies; (b) the CPT-even dim-6 operator basis is the right parametrization; (c) the coefficients are defined in the CMB frame; (d) for the proton rows, the UHECR composition assumed in the fit (pure proton at 99% CL — Liberati §7.5 notes heavy composition, which Auger favours above 10¹⁹·⁶ eV, weakens the proton limits by 1–2 orders); **(e) FRAME JURISDICTION** — that the measured `η⁽⁴⁾` may be identified with the *substrate's own* quartic dispersion coefficient. The bounds are INSIDE-frame inferences about propagating particles; the object bounded is the OUTSIDE-frame strain-mode dispersion (`Cl41Wave().wave_speed_c()`, which raises). The transfer runs through the un-built outside↔inside projection; the SCALE half of the same crossing (`a ↔ ℓ_Pl`) is the renormalization dictionary's length/scale face (worklist dictionary item, sixth face, 2026-08-16) | **OPEN as derivation, SANCTIONED as data import** — the same status as I-6. Premise (c) closes the **inertial-frame** question only, and there it is a coherence *win* rather than a crack: TWT's τ₅-foliation IS the comoving/CMB frame (§B.4.5), so the frames agree. The **frame-jurisdiction** question is separate and is premise (e) — the same crack §E.3.1 rows 7–8 and §E.5 already carry for inside-frame laboratory limits binding outside-frame floors; it does not weaken the case for NAMING the exposure (canon §0a), but the exposure's BINDINGNESS is itself conditional and saying so costs nothing. Premise (d) is the one live *empirical* loosening, and it is far too small to close a six-to-nine-order gap (the gap size is `Λ`-dependent: the 2026-07-30 which-Λ ruling assigns dispersion consumers `Λ_L = 1/a ∈ [0.39, 0.73] M_Pl`, naive `η⁽⁴⁾ ∈ [1.9, 6.7]` — R-037) | A TWT-native computation of the substrate strain-mode dispersion (the #1 gap, §D.5) — which would let the framework state its own `η⁽⁴⁾` and read the bounds directly rather than through the EFT parametrization. **REVERT CLAUSE:** strike this row and the *positive* half of R-165 (D4 fourth-moment isotropy ⇒ dim-8 anisotropy) is UNAFFECTED — it is a pure lattice identity with no import. What falls is the *exposure* statement: VG-6, §E.3.5(4) and N52 revert to "the dim-6 isotropic coefficient is uncomputed and untested", and §E.3.1 does not regain its deleted rows 1–2 (those were deleted for reading a dim-6 object against a dim-4 bound — an error independent of this import) |
| I-20 | **Finkelstein–Rubinstein 1968** (spin-statistics for kinks: on the soliton configuration space `Q_N` the exchange loop is homotopic to the `2π`-rotation loop, so a single-valued wavefunction is a `±1` character of `π₁(Q_N) = ℤ₂`). The *quantization prescription* is the import; the bare homotopy classification is Section-13-exempt pure math | §B.3.5 — R-025 (the Pauli/spin-statistics statement and its four protecting negatives; `skyrmion_collective_quantization_under_v2_3p2`, `colour_z3_holonomy_cannot_source_fr_sign`); §C.1.2 — R-133 (the `J = 1/2, 3/2` lattice, `skyrmion_rotational_band_nucleon_delta`) and R-136 (the `I + J` odd deuteron rule via the FR loop signs, `b2_axial_quantization_deuteron_ground_state`), with R-137 and R-138 INHERITING that conditional (`massive_pion_bvp_binding_margin_robust` re-checks R-136's selection under the mass term; `massive_scheme_refit_branch` states in-code that it inherits R-133's (Q)+FR-selection conditional); §C.4.6 + §B.3.5 — R-141 (the induced-parity upgrade *of* the FR pick, `induced_level_parity_on_baryon_worldline`; R-161 further splits R-141's P1b premise but does not itself use this import); §D.4.6 — R-131 (the integer-vs-half-integer charge-lattice menu, `defect_phase_modulus_charge_tower_spacing`); §B.4.1 — R-027, residual only (the exchange-`ℤ₂` statement; the tensor product and the singlet are *separate* named assumptions, not this import). **NOT exposed** (checked 2026-07-29 across paper, companion, `twt.py`, `twt_test.py`): R-135, whose classical below-threshold inequality is FR-free (its own docstring files the FR constraint under NOT-done), and R-142, whose `dE/dN = ω` envelope identity is proved independent of which FR-class lattice is picked (§D.4.6). N32b / N35 / N53 are negative uses | **Inside-frame / effective** — quantization of configuration-space topology, riding the §B.3-derived QM. Sibling of I-5, which already carries the FR *machinery* on the hadron side | (a) the multi-defect configuration space is the standard Skyrmion one, `Q_N = Maps_{deg N}(S³,S³)`; (b) wavefunctions are single-valued sections of a flat line bundle over it, so statistics is a character of `π₁`; (c) semiclassical collective quantization (shared with I-5) | **OPEN on premise (a); MENU-ONLY on the conclusion.** The theorem supplies the two-element menu `Hom(ℤ₂,{±1})`; the fermionic PICK is TWT's own 1 INPUT bit (canon §2 menu-vs-pick, unchanged from N32b/N35), anchored twice empirically (proton; deuteron, R-136) and conditionally induced by R-141. Premise (a) is the crack: N53 (2026-07-29) established that TWT has **no** constructed multi-defect state space — five independent routes failed — so `π₁` is imported on a space the framework has not built | Construct the substrate multi-defect configuration space (N53; §E.3 SC-1) and compute its `π₁` natively; or R-141's substrate computation of the induced worldline term, which would supply the pick from the substrate. **REVERT CLAUSE:** strike this row and the one-defect `Spin(4)` half-angle of §B.3.5 is UNAFFECTED (engine-exact, import-free). What falls is the exchange↔rotation identification: R-025 reverts to a statement about a single rotor's `2π` sign; R-133's `J` lattice and R-136's `I + J` rule (and R-137/R-138's inheritance of them) fall back to imported Skyrme phenomenology (I-5); R-141 has no selection left to upgrade; R-131's charge-lattice menu loses its `ℤ₂` framing. R-027's Tsirelson value and R-135's classical inequality do not move Verified explicitly on the two-defect states: totally antisymmetric combinations exist for ALL FOUR spin states (‖T + T_exchanged‖ = 0 in every case), so exchange antisymmetry constrains the total state to the odd sector but selects nothing within it; the singlet is selected by angular-momentum conservation at the source — a dynamical preparation fact, separate from this import. |
| I-22 | **Universality-plus-rescaling removal of a species-universal dimension-four Lorentz-violation coefficient** (a maximum speed common to all species is absorbed by a coordinate/units rescaling and carries no relative observable — standard LV-EFT lore, sibling of I-19; the *conclusion* is the import, the algebra of the rescaling is not) | §B.1.5 — the loop-order-independent half of the R-016 defusal (restored from V1 §12.6, 2026-07-30); the dimension-four scope of R-016/R-039; §B.6.3's dimension-four protection statement ("The dimension-four boost bound is closed by matter-as-defect") | **Substrate-level** — the loops run over substrate modes and the rescaling is applied to the substrate's own light-cone, i.e. it sits on the borrowed-mechanism side of the 13.4 discriminator, not the data-like side | (a) the ONE substrate field generates all the radiative corrections, so the induced dim-4 coefficient is genuinely common to every defect species — the premise the whole step rides, and the one that is not engine-checkable; (b) a loop/derivative expansion over substrate modes exists at all (a non-analytic #1-gap memory kernel leaves 'loop order' undefined and the argument's framing lapses); (c) the removed coefficient is a *constant*, not momentum-dependent — which is exactly why the step does NOT extend to dimension six | **OPEN** — premise (a) is a substrate claim only the #1-gap kernel can confirm; premise (b) is the #1 gap itself. Recorded at DEFUSAL tier: the step closes the dim-4 exposure *conditionally* and never claimed the substrate's interacting Lorentz invariance, which V1 §12.6 conceded open in the same paragraph. V1 carried this reasoning at a flat DERIVED tag; that tag is deliberately not restored with it | The #1-gap kernel's own dispersion computation (§D.5) — the same object I-19 waits on. **REVERT CLAUSE:** strike this row and §B.1.5's *relative-boost* half is UNAFFECTED (R-016's one-field/one-light-cone statement is import-free — it is a claim about which coefficient *exists*, not about what cancels). What falls is the *radiative* half: the Collins-class obstacle reverts from 'defused at its precondition, independently of loop order' to 'defused at the classical/tree level, with the radiative case named open'. §E.3.5(4), VG-6, N52 and I-19 do not move |

| I-28 | **Collins–Perez–Sudarsky–Urrutia–Vucetich 2004** (interacting QFT with a Lorentz-violating regulator: LV percolates to low-dimension operators with unsuppressed coefficients — radiative non-decoupling of UV Lorentz violation) | §B.1.5 (the dimension-four defusal by precondition-denial — the one-field structure removes the multi-field counterterm channel; a DEFENSIVE use, 13.2-class) · §B.6.3 (the magnitude-channel caveat on the dim-6 isotropic exposure) · the D4 standalone note §8.3 (anisotropy protection survives loops; the magnitude channel is not closed) | Inside-frame QFT loop argument invoked at the substrate seam — the jurisdiction question is I-3's (the substrate is a driven-dissipative NESS, not a QFT vacuum; whether QFT loop percolation models the outside↔inside transfer at all is the same unbuilt projection I-19 premise (e) hedges) | An interacting QFT description at the seam; a perturbative loop expansion; for the §B.1.5 defusal, the multi-species field structure whose ABSENCE is the defusal's ground | **OPEN as a transfer model** (row back-filled 2026-08-16, RUL-046 — the load-bearing uses predate the row): the §B.1.5 use is negative/defensive, the §B.6.3 use names an unclosed channel; no result's tier consumes the theorem affirmatively | A substrate-native loop/coarse-graining computation (the §D.5 kernel), replacing the QFT percolation model with the actual transfer. Strike the row: §B.1.5's defusal reverts to the bare "no multi-field channel exists" (unchanged in substance); §B.6.3's caveat loses its named citation; nothing else moves |
| I-29 | **Paraunitary bosonic-Bogoliubov band theory** — a bosonic BdG Hamiltonian is diagonalised NOT by a unitary but by a **paraunitary** transformation against the `τ₃` (para-)metric `T† τ₃ T = τ₃`, so the relevant band operator is `τ₃ H(k)` rather than `H(k)`; the resulting non-Hermitian-but-pseudo-Hermitian structure supports Berry curvature, Chern numbers and Weyl points in a *bosonic* magnon spectrum. Shindou, R., Matsumoto, R., Murakami, S. & Ohe, J., "Topological chiral magnonic edge mode in a magnonic crystal", *Phys. Rev. B* **87**, 174427 (2013), DOI 10.1103/PhysRevB.87.174427 · Li, F.-Y. *et al.*, "Weyl magnons in breathing pyrochlore antiferromagnets", *Nat. Commun.* **7**, 12691 (2016), DOI 10.1038/ncomms12691 | **KC-1's one named PASSING class** — `spectral_branch_symmetry_class_filter` (`twt_candidate_v3`), the clause *"paraunitary bosonic-BdG kernels (τ₃ metric) are the named class that CAN pass"*; and, by inheritance, the escape-(a) status statement (UNMEASURED / KERNEL-GATED) in that primitive, in `TONGUES_L2_2026-08-23.md` §CORRECTION and in N64's SALVAGE line. Also the F2 naming fence at `magnon_stiffness_bands_canted_vacuum` — *"stiffness, NOT Bogoliubov"* — which is this row read as a NEGATIVE: the banked Hessian is not that operator | **Substrate level** (a property of the #1-gap kernel's own kinetic/symplectic structure `Ω`, outside-frame) — so its premises ride what only the #1-gap kernel can confirm | A bosonic quadratic Hamiltonian with a genuine BdG (particle–hole-doubled) structure and a positive-definite `H` admitting Williamson/Colpa diagonalisation. **TWT supplies none of this today:** the banked object is a real symmetric STIFFNESS Hessian, `Ω` is unbanked, and no particle–hole doubling exists in the corpus | **OPEN — and the row's whole point is that the exposure runs the OTHER way.** Nothing banked is *derived* from this import; it is used to NAME the one kernel class that could evade a negative, i.e. to keep KC-1 honest as a one-way filter rather than an impossibility. Registered because naming a passing class is a load-bearing external claim even when the claim is about what has NOT been ruled out (canon §4 / RUL-049: an exclusion must carry its escape, and the escape must be citable) | Exhibit a paraunitary `Ω` with genuinely complex entries on the banked D4 substrate and re-run KC-1 on it — that single computation either fires the escape or closes it. **REVERT:** strike this row and KC-1's *passing*-class clause falls with it; the filter's measured content (the two exact isospectralities, rank-3 absence, the codimension-2 definability collapse) is untouched, because none of it consumes the import |

## 13.2 Negative and defensive uses (closures conditional on the import)

| # | Import | Used at | Exposure |
|---|---|---|---|
| I-8 | **Nielsen–Hughes** (antiscreening requires the paramagnetic response of a charged spin-1 field) | N5 — closed the emergent-AF route | The CLOSURE is conditional: if the theorem's premises fail on the substrate, the route could reopen. Recorded so the conditionality is visible; the octet-as-oscillation would-change-if already covers the live re-attack |
| I-9 | **Weinberg–Witten** | §B.6.7 — preemption | None forward: the theorem is EVADED (composite graviton), its premises deliberately not satisfied. Registered for completeness |
| I-10 | **Reflection positivity** (Osterwalder–Schrader-class). Source of record: Osterwalder, K. & Schrader, R., "Axioms for Euclidean Green's Functions", *Commun. Math. Phys.* **31**, 83–112 (1973), DOI 10.1007/BF01645738 — *"We establish necessary and sufficient conditions for Euclidean Green's functions to define a unique Wightman field theory."*; sequel ibid. **42**, 281–305 (1975), DOI 10.1007/BF01608978. The five conditions are OS0 temperedness, OS1 Euclidean invariance, OS2 permutation symmetry, **OS3 reflection positivity**, OS4 clustering | R-085 `beta3_sign_from_reflection_positivity` — a NEGATIVE (RP insufficient for the running sign) | Low: the banked result is a negative either way. FLAG: whether the substrate measure itself is reflection-positive has never been checked — any future POSITIVE use of RP must first address that (see 13.3). **THE DEBT NAMED (2026-08-18, prior-art pass, RUL-050): OS3 is the hinge of the Euclidean-substrate premise itself, not only of this negative.** OS is the theorem that makes "Euclidean substrate, Lorentzian appearance" a licensed move rather than a category error — a Euclidean theory satisfying reflection positivity *is* a relativistic quantum field theory, exactly — and the framework has not exhibited an OS3-type positivity for its substrate. **What this does and does not touch.** It does NOT touch §B.1: the kinematic Lorentzian face there is the *algebraic* route (`Cl(4,0) ≅ Cl(1,3)` DERIVED-A, R-014, plus the wavefront-lock observer stipulation, A-3/R-015) and both inputs are already labeled, so that face is asserted-and-labeled, not silently reconstructed. What it DOES touch is any statement — present or future — that the Euclidean substrate *inherits* a relativistic quantum field theory, i.e. a Hilbert space, a vacuum and a self-adjoint Hamiltonian, by virtue of being Euclidean. That inheritance is exactly what OS licenses and exactly what is unpaid. The comparative-warning context, carried from the same pass and not softened: the Euclidean gravitational action is unbounded below (Gibbons, Hawking & Perry, *Nucl. Phys. B* **138**, 141–150 (1978), DOI 10.1016/0550-3213(78)90161-X — indefiniteness from the conformal factor), purely Euclidean dynamical triangulations produced degenerate phases, and the programme that **recovered** reflection positivity did so precisely by reintroducing causal structure with a distinguished time (Ambjørn, Jurkiewicz & Loll, *Phys. Rev. Lett.* **85**, 924–927 (2000), arXiv:hep-th/0002050: *"The reflection positivity of the model ensures the existence of a well-defined Hamiltonian."*). Read as one chain that is external, refereed support for the *architecture* — Euclidean substrate **plus** a lock and a foliation — and evidence that the Euclidean half alone does not work. TWT's action is a medium's elastic energy, not Einstein–Hilbert, so the conformal-mode disease is not automatically inherited; **the burden of showing the difference is TWT's.** Named handle (two ways to discharge, and only two): exhibit an OS3-type positivity for the substrate measure, or state plainly at every inheritance site that the Lorentzian *field-theoretic* face is asserted rather than reconstructed. Pre-registered as a 13.3 lead so that any future positive use enters as a load-bearing import with premises, not as a free win |
| I-11 | **Bell's theorem / Gleason** | §B.4 — inherited-by-isomorphism; Gleason explicitly NOT claimed | None: any theory isomorphic to QM inherits Bell; the paper says so plainly |
| I-12 | **FDT (fluctuation–dissipation theorem)** | §D.5.6 — Θ_rel is DEFINED as its violation residual | Definitional, not an import that must hold: Θ_rel measures exactly how far the substrate sits from the regime where equilibrium imports are exact. Registered because it is the QUANTIFIER of the I-4-class crack |
| I-21 | **Atiyah–Hitchin 1985/1988** — moduli-space (geodesic-approximation) dynamics of slowly-moving solitons; `90°` monopole scattering as the canonical case | (i) §B.8.4 — **illustrative precedent only** for "solitons in a smooth field have no collision singularity; only the *particle* description breaks". The section's own argument is self-contained (`R_a` is a smooth functional of a smooth field, and what fails is individuation, not evolution), so no banked result's tier rides the theorem. Registered because the bibliography asserted the connection while the body cited nothing. (ii) **N53 route (a)** — moduli-space quantization `L²(M_N)` as a candidate multi-defect state space: a NEGATIVE use, nothing banked | **Level applied:** inside-frame / effective (collective-coordinate dynamics), same jurisdiction as I-5. **Premises:** BPS or near-BPS solitons, so that relative positions are flat (zero-mode) directions of the energy. **Ontology status: N/A for (i)** — no forward exposure; **PREMISE-FAILS-ON-SUBSTRATE for (ii)** — TWT's defects are non-BPS on the framework's own banked coefficients: per-baryon energy in units of the Bogomolny–Faddeev bound is `≈ 1.231` at `B = 1` and `≈ 1.208` at `B = 2`, i.e. roughly **23 %** and **21 %** above the bound (N53's figures, recomputed 2026-07-29 from `multi_skyrmion_b2_classical_binding`'s banked `36.46` and `71.54`; the `B = 2` ratio is the engine's own `per_baryon_12pi2`, and an independent re-solve by a different algorithm — direct discretized-functional minimization rather than the engine's shooting method — reproduces both to ± 0.02 percentage points; both agree with the standard Skyrme values 1.232 / 1.208). Non-BPS ⇒ the `3(N−1)` relative positions are *massive* modes, so `dim M_N ≤ 9` for every N (N-independent) against the `6N` a tensor product needs (N53). **Retirement handle:** a BPS or near-BPS sector, or an index theorem supplying exact zero modes beyond the symmetry-guaranteed nine (N53 would-change-if (1) and (2)) — either would move this row into 13.1 with real forward exposure |
| I-23 | **The measured mass→weight chain** (published values only: single-particle inertial-mass-as-frequency ~10⁻¹¹; passive-fall universality 10⁻¹⁵ bulk / 10⁻¹² atoms / only 10⁻¹–10⁻² free elementary particles; active/passive material-independence 5×10⁻⁵ lab, 3.9×10⁻¹⁴ LLR; smallest measured gravitational SOURCE 92.1 mg = 5.5×10²² proton masses; electron spin-direction asymmetry < ~10⁻²¹ — the source's own abstract statement; superposed-source gravity untested, BMV proposals only) | §B.6 intro block ("What the laboratory pins before mass is linked to weight"); engine `mass_weight_empirical_chain` (jurisdiction ledger — deliberately OUTSIDE the eom E-namespace, which stays E1-only) + one cosmo-module suite check (duplicate-literal drift guard + wording-guard); Section 10 bibliography subsection "The mass→weight empirical chain" | **None forward — jurisdictional data import** (inside-frame data bridge, kin of I-6/I-19 but transferring no bound): the fences bind the inside-frame effective description §B.6 is written in, which the banked route SATISFIES and to which it COMMITS per-particle (`T_μν` coupling; `m_i = m_g` forced, R-016/R-039; R-038 additive) — no outside-frame substrate object is bounded, so I-19's premise-(e) projection is NOT invoked. Ontology status **N/A** (definitional/inventory; no forward exposure). Premises: each experiment's systematics taken at face value from the primary record (all read directly 2026-08-02; two recall errors caught at import: COW-1975 agreed at ~10% not 1%; the spin-pendulum PRL is 97, 021603); the four-link decomposition is an operational classification, not a theorem. Retirement: each entry names its record holder — a superseding measurement (a sub-92.1 mg source; a BMV-class experiment; a precise free-particle UFF test) is a row edit, not an excision. **REVERT:** strike this row and the §B.6 block + the primitive + its suite check fall together; nothing else moves — no banked result cites the ledger as support |

## 13.3 Prospective imports (named leads, not yet used — pre-registered exposure)

| Lead | Would be used at | Premises | Pre-registered status |
|---|---|---|---|
| **a-theorem / c-theorem analogue** (Komargodski–Schwimmer class) | P2-3 sign lead — **NOT PURSUED** (superseded 2026-07-05: the KL route fired first, R-148/I-13) | Unitary, Lorentz-invariant 4D QFT with defined UV/IR fixed points | The premise gap stands as recorded; any future use still enters at conditional tier + a 13.1 row, mandatory |
| ~~**Källén–Lehmann + unitarity bound** on the running quartic~~ | **FIRED 2026-07-05 → promoted to 13.1 row I-13** (R-148) | — | The stability-recast-first directive was satisfied for the positivity leg (recast onto the banked §B.3-derived QM); analyticity/boundedness remain un-recast, named in I-13 |
| **Osterwalder–Schrader reconstruction** (Euclidean Schwinger functions satisfying OS0–OS4 reconstruct a Wightman QFT on Minkowski space: Hilbert space, vacuum, self-adjoint Hamiltonian). Full citation and the warning chain at **I-10**, which is this lead's counterpart row | Any statement that the Euclidean substrate *inherits* a relativistic quantum field theory by virtue of being Euclidean — i.e. the field-theoretic half of the S1a premise. **NOT** §B.1's algebraic/kinematic Lorentzian face (R-014 + A-3, both inputs labeled), which does not route through this theorem | OS0 temperedness · OS1 Euclidean invariance · OS2 permutation symmetry · **OS3 reflection positivity** · OS4 clustering — of the substrate's own correlation functions. OS3 is the hinge and the one the framework has not exhibited; the substrate is additionally driven and non-unitary at the NESS, so OS1's Euclidean invariance and OS4's clustering are not free either | **PRE-REGISTERED DEBT, unpaid** (recorded 2026-08-18, prior-art pass, RUL-050). This lead is registered *before* any use, which is the point: a Euclidean substrate that cannot exhibit an OS3-type positivity has not earned the Lorentzian reconstruction, it has only asserted it. Two discharge routes and only two — exhibit the positivity, or state at every inheritance site that the field-theoretic Lorentzian face is asserted rather than reconstructed. Any future POSITIVE use fires the 13.1 promotion with premises and a revert clause; the debt is **within Layer 1, not behind the §D.5 gap**, which is what makes it the sharpest checkable item the prior-art pass found for this premise |

## 13.4 Reading the registry

The imports concentrate exactly along the canon §7 fault line — they are stand-ins for the
missing #1-gap dynamics, which is why the retirement handles in 13.1 are dominated by kernel
faces. Three summary judgments (from the 2026-07-05 audit): (i) the record is HONEST — every
load-bearing import found was already labeled and conditional; the registry adds premise-level
accounting, not corrections; (ii) the genuine exposure class is unitarity/Lorentz-premised
imports applied at the substrate level (I-1, I-3, and both 13.3 leads); (iii) the two model
moves for retiring an import are the §B.6.4 stability recast (bring the premise inside the
ontology) and R-141's named substrate-computation face (replace the theorem with the
derivation).

**What the level column MEANS: data-like vs borrowed-mechanism (2026-07-05, coordinator Q&A —
the sharp form of the discriminator).** On this framework's own account, QFT is the
inside-frame effective description — so a theorem of QFT applied at the **inside-frame /
effective level** is epistemically like structured empirical data: a compressed inside-frame
regularity, imported under the canon §0 inside-for-data method, to which the outside-frame
theory owes a mechanism (that mechanism is the row's retirement handle; the SM RG run-down is
the purest case — the running is literally measured). An import applied at the **substrate
level** is a different object entirely: it is NOT data awaiting explanation but a **borrowed
fragment of the would-be outside mechanism itself** — a claim about the substrate imported
wholesale from neighboring physics, occupying the very seat the #1-gap kernel is supposed to
fill. The failure modes differ accordingly: inside-frame data can only CONSTRAIN (the theory
must reproduce it or lose); borrowed mechanism can MISLEAD (if its premises fail on the actual
substrate dynamics, it silently substitutes a wrong dynamics rather than waiting for a right
one). Volovik (I-4) is the well-handled exemplar — its equilibrium premise is known-cracked and
the crack itself was converted into the gated `Λ ~ H²` prediction; Sakharov (I-3) has no
crack-quantifier yet, which is exactly why its status is OPEN. The end state the registry
drives toward is dissolution: either the premise becomes an engine-checkable substrate fact
(the §B.6.4 stability recast — the theorem stops being an import) or the theorem is replaced
by a substrate derivation (the R-141 route — the import is deleted). Note also the coherence
check that keeps inside-level borrowing non-circular: the results that LICENSE inside-frame
jurisdiction (§B.3 QM reconstruction; §B.1.4/§B.6.3 emergent Lorentz) were themselves derived
without any of these imports.

**Excision discipline (BINDING — coordinator-directed, 2026-07-05).** The registry exists so
that a wrong import can be removed PRECISELY, not archaeologically. Requirements: (a) each
row's **Used-at column is the import's complete blast radius** — every result whose tier rides
the import must be listed there, and adding a new dependent means updating the row in the same
banking pass; (b) every dependent result must carry a **conditional tier + a named revert
clause** stating what it falls back to without the import (R-141 is the model: "refusing P1b
restores the SELECTION with both empirical anchors standing"); (c) no import may be woven into
paper prose as if unconditional — the use-site carries a conditionality marker or an explicit
import notice (§B.6.2 and §B.7.4 carry them for I-3/I-4). **Excising an import = strike the
row, fire the listed revert clauses, and the dependents revert to their pre-import tiers** —
nothing else in the corpus moves. A dependent result discovered WITHOUT a revert clause is
mis-banked: the fix is to write the clause (or re-derive without the import), never to quietly
absorb the import. **Two cases, and they are NOT the same case (corrected 2026-08-21, R7(a) of the
restriction analysis; adopt-all).** (1) An import **used load-bearing but UNREGISTERED** is a
**banking-stopper** of the phantom-cite class — one of the four canonical stoppers, unchanged.
(2) An import **registered but woven in without a revert path** is a **RECORDED DEFECT WITH A NAMED
OWNER**, not a stopper: **owner = the next consolidation's banking triage**, docketed on
`knowledge/ledgers/TWT_worklist.md`. The distinction is a measurement, not a softening —
`APPARATUS_TESTS_2026-08-19` Test 2 found **0 of 8** dependents compliant, so the universal reading
made the tree formally unbankable and therefore restrained no one; it was untrue rather than strict.
The duty to write the clause is unchanged and the docket item that fixes the eight ships with this
correction, not instead of it.

## 13.5 Prior-art and premise-kinship registrations (premise-holders; no forward exposure)

*Added under RUL-050 (the prior-art pass). These are NOT load-bearing imports: no banked result's
tier rides any of them, and striking a row here changes no TWT claim. They are registered because
the registry is also the corpus's answer to "who else holds this premise, formalized?" — and
because a premise-holder who is **not** cited is a disguise risk of its own kind: an originality
claim made in ignorance of a published claimant is as dishonest as an unlabeled import. Each row
therefore records what the tradition actually built, in what capacity TWT stands beside it, and
the single named condition under which the row would have to move into 13.1 or 13.2. Format is
13.1's; the "Ontology status" column here records **the capacity of the registration**, not a
premise TWT consumes. Citations are read off the governing record — the ontological prior-art
founding pass — and carry its access flags unchanged.*

*Provenance and adoption (RUL-059, coordinator 2026-08-18). Two readings of this subsection are
wrong and one is right. Wrong: that these rows are sources TWT drew on — the framework's ideas
were arrived at independently and the convergences here were discovered afterwards, by the
literature sweep; kinship is not lineage. Also wrong: that a piece appearing here is thereby
off-limits — the program does not refuse a compatible piece on the principle of not having
invented it, and it does not re-invent what a row already names in order to avoid the debt of
credit. Right: a candidate adoption from any tradition named here is a legitimate move,
SUBMITTED TO STUDY like any other candidate — a 13.1 row with premises and a revert clause,
adversarial review, an honest imported-and-counted label — and admitted or refused on that
study, never on origin.*

| # | Import (external result) | Used at | Level applied | Premises required | Ontology status | Retirement handle |
|---|---|---|---|---|---|---|
| I-24 | **Kleinert's world crystal** — spacetime modelled as a crystal of Planck-scale lattice spacing whose **defects carry the gravitational content**: the elasticity/defect gauge-field formalism maps disclinations to curvature and dislocations to torsion, and a quantum phase transition to a *nematic* phase by condensation of dislocations removes torsion, leaving a medium whose curvature rigidity is indistinguishable from Einstein's spacetime at large distances; the lattice additionally yields a Brillouin-zone-modified uncertainty relation. Kleinert, H. & Zaanen, J., "World Nematic Crystal Model of Gravity Explaining the Absence of Torsion", *Phys. Lett. A* **324**, 361–365 (2004), arXiv:gr-qc/0307033 — abstract verbatim: *"We attribute the gravitational interaction between sources of curvature to the world being a crystal which has undergone a quantum phase transition to a nematic phase by a condensation of dislocations. The model explains why spacetime has no observable torsion and predicts the existence of curvature sources in the form of world sheets."* · Kleinert, H., "Emerging gravity from defects in world crystal", *Braz. J. Phys.* **35**, 359–361 (2005), DOI 10.1590/S0103-97332005000200022 **[bibliographic only]** · Jizba, P., Kleinert, H. & Scardigli, F., "Uncertainty Relation on World Crystal and its Applications to Micro Black Holes", *Phys. Rev. D* **81**, 084030 (2010), arXiv:0912.2253 — *"generalized uncertainty relations in a crystal-like universe whose lattice spacing is of the order of Planck length -- 'world crystal'."* | **NO load-bearing use — prior-art registration.** The kinship bears at: family-tree node **V3-1** (the arrangement pick — a Planck-spaced *material* lattice is Kleinert's premise as well as this instance's) and node **V3-6** (the gravity route — Kleinert's defect-elasticity ↔ curvature dictionary reaches the same crossing the Sakharov instance-pick reaches by another road); the charter's kin section, which before this pass named only the SHP tradition; §B.6 and the D4 arrangement material as the neighbourhood a reader will place them in. No paper prose asserts the kinship today, and none is required to — the registration is the record | **N/A — no conclusion is used.** Nothing is transferred: not the nematic mechanism, not the defect ↔ curvature identification, not the modified uncertainty relation | **None consumed.** Recorded for the reverse reason: the row exists so that no TWT statement of the form "a material lattice whose defects are the physics is our own move" can be made without meeting this claimant | **PRIOR ART — the closest formalized relative found anywhere in the sweep, and the highest-value previously un-cited neighbourhood.** Kinship, stated strictly: same premise (a Planck-scale material lattice; defects as the physical content; gravity as the medium's elastic response); **different payload** — Kleinert's defects give *gravity* (curvature/torsion sources), not the matter spectrum; the signature is not relocated; there is no advancing front, no meta-time, no lock. **The named debt this row carries in:** Kleinert has a *published answer to the torsion question* (the nematic transition) and TWT does not — that is the question a reader asks of any lattice-with-defects ontology, and the corpus currently has no reply | None needed while nothing rides it. **Promotion trigger:** the moment any TWT result leans on the defect-elasticity ↔ curvature dictionary — rather than reaching curvature through the induced/Sakharov route — this row moves to 13.1 with premises and a revert clause, because the dictionary would then be doing load-bearing work |
| I-25 | **Volovik's quantum-vacuum-as-medium ontology** (distinct from, and cross-referenced to, **I-4**, which carries only his q-theory Gibbs–Duhem identity as a load-bearing thermodynamic import). The formalization: (i) **momentum-space topology at a Fermi point** — a Green's-function winding invariant whose non-triviality forces gaplessness *"irrespective of the deformation of the parameters of the microscopic theory"*, from which chiral fermions, gauge fields, the tetrad and an emergent Lorentz symmetry follow in the low-energy corner; (ii) two-fluid Landau–Khalatnikov hydrodynamics as an effective theory of gravity; (iii) q-theory of vacuum thermodynamics (the I-4 object). Volovik, G.E., *The Universe in a Helium Droplet*, Clarendon/Oxford (2003), Int. Series of Monographs on Physics **117**, ISBN 0198507828; 2009 OUP reissue ISBN 9780199564842, DOI 10.1093/acprof:oso/9780199564842.001.0001 — **publisher abstract read verbatim off the Crossref record for the book DOI; the book's interior was NOT read [bibliographic only on contents]**: *"elementary particles (electrons, neutrinos, quarks, etc.) are excitations of a more fundamental medium called the quantum vacuum. This is the new 'aether' of the 21st century."* · "Superfluid analogies of cosmological phenomena", *Phys. Rep.* **351**, 195–348 (2001), DOI 10.1016/S0370-1573(00)00139-3, arXiv:gr-qc/0005091 — §I is titled "INTRODUCTION. PHYSICAL VACUUM AS CONDENSED MATTER"; §II, first-hand: *"the superfluid vacuum flow of 3He-A can have a continuous vorticity, ∇ × v_s ≠ 0"* · "Topology of quantum vacuum", arXiv:1111.4627, *Lecture Notes in Physics* **870**, 343–383 (2013) — §1: *"The only difference between the topological materials and the quantum vacuum of the Standard Model is that the latter obeys several symmetries"* · *Phil. Trans. R. Soc. A* **366**, 2935–2951 (2008), DOI 10.1098/rsta.2008.0070, arXiv:0801.0724 | **NO load-bearing use — prior-art registration** (the one load-bearing Volovik use in the corpus is I-4's Gibbs–Duhem identity at R-047/§B.7.4, and this row does not touch it). The kinship bears at: the **carrier** premise wherever it is stated as the framework's own (§A.3/§9.6-class carrier material, canon §0's named-premise block); the substrate-realism block of the comparative ledger's ontology lines; the charter's kin section. Registered so that **any originality claim on the carrier — or on "the vacuum is a real structured medium" generally — is argued *against* Volovik rather than in ignorance of him** | **N/A — no conclusion is used** beyond what I-4 already carries under its own premises | **None consumed.** The Fermi-point protection mechanism is noted, not imported | **PRIOR ART — SAME PREMISE, held outright and in print.** Strictness note carried from the governing record: a first reading scored Volovik COUSIN on the *Physics Reports* abstract alone (which is analogical in framing) and was **corrected to SAME PREMISE** on the book's publisher abstract and the 2013 review; his paper-level prose does oscillate between ontology and analogy ("our analogy", "mimics") and that oscillation is reported, not smoothed. **What is TWT's and what is not:** "the vacuum is a medium" is not TWT's; "the vacuum flows" is not TWT's either (his superfluid vacuum carries continuous vorticity). What is TWT's is the **conjunction** — that the vacuum's motion *is* the τ₅-advance a defect's phase must match, welding the carrier to the second time and the drive. Describe it as a joint, never as an unprecedented premise | None needed while nothing rides it. **Promotion trigger:** any TWT use of the Fermi-point/momentum-space-topology protection argument — or of any Volovik result other than I-4's identity — enters 13.1 with its own premises. **Standing discipline, both directions:** do not report Volovik as having answered the radiative-naturalness objection (I-28 Collins-class; a sweep of his corpus found no paper responding to it), and do not under-cite him either |
| I-26 | **Bombelli–Henson–Sorkin "Discreteness without symmetry breaking: a theorem"** — for sprinklings into Minkowski space (Poisson processes) there exists no equivariant measurable map from sprinklings to spacetime directions, even locally; hence an intrinsically associated discrete structure picks out no preferred frame, and — the corollary this row is registered for — **no finite-valency graph can be associated to a sprinkling consistently with Lorentz invariance.** Bombelli, L., Henson, J. & Sorkin, R.D., *Mod. Phys. Lett. A* **24**, 2579–2587 (2009), DOI 10.1142/S0217732309031958, arXiv:gr-qc/0605006; abstract verbatim in full at the governing record. Mechanism (Surya, S., "The causal set approach to quantum gravity", *Living Rev. Relativity* **22**, 5 (2019), arXiv:1903.11544, §3.2): nearest-neighbour links lie on a hyperboloid, *"a non-compact, infinite volume region and hence the number of future links to `e` is (almost surely) infinite"*. Founding paper: Bombelli, L., Lee, J., Meyer, D. & Sorkin, R.D., "Space-time as a causal set", *Phys. Rev. Lett.* **59**, 521–524 (1987), DOI 10.1103/PhysRevLett.59.521 | **A CONSTRAINT ON THE FAMILY MENU, not on any banked result.** Used at: family-tree node **V3-1**, whose menu line already records the irregular-discrete branch as *"causal-set-adjacent; BHS-constrained"* — this row is that clause's citation; the **reopened S1b arrangement menu** (carry into P-6); and the discreteness/frame-cost material wherever the frame is defended. **It binds no V3 number**: the pinned instance is a *regular* D4 lattice, not a sprinkling, so the theorem's hypothesis is not met by the banked arrangement and no banked quantity moves either way | **Pure mathematics with checkable hypotheses** — the Section-13-EXEMPT class (kin of I-14). Registered for completeness and because it *forecloses a family branch*, which is a registry-visible fact | Its own hypothesis: the discrete structure is associated to a **sprinkling** (Poisson process into Minkowski) in an intrinsic, equivariant manner. A structure that is not sprinkling-like is outside the theorem's reach — and saying which side a proposed arrangement falls on is the family's work, not the theorem's | **N/A as a premise (a theorem); LOAD-BEARING AS A FENCE on the menu.** The trilemma it makes provable: no arrangement can have all three of *discreteness*, *Lorentz invariance* and *finite coordination number*. Causal sets keep discreteness and Lorentz invariance and pay with infinite-valency non-locality; TWT keeps discreteness and finite valency (the {J, D} bond structure) and pays with the preferred frame. **Both are settlements, and that the one mature sibling also had to pay is evidence about the premise class, not about this instance** — which is the best available external defence of the S3/B-6 frame cost, and the reason this row is worth its space | None (a theorem does not retire). **The live consequence to carry forward:** a family member with an irregular arrangement **AND** finite bond valency **AND** a claim to Lorentz invariance is excluded by this theorem. Any candidate proposed at V3-1's irregular branch must state which of the three it gives up, and this row is the check |
| I-27 | **Gomes–Koslowski shape dynamics** — a linking theory establishing that general relativity is **dynamically equivalent** to a theory with **fixed foliation but spatial conformal invariance**: refoliation invariance is traded for conformal invariance rather than lost. Gomes, H. & Koslowski, T., "The Link between General Relativity and Shape Dynamics", *Class. Quantum Grav.* **29**, 075009 (2012), DOI 10.1088/0264-9381/29/7/075009, arXiv:1101.5974; abstract verbatim: *"a linking theory that proves the equivalence of General Relativity and Shape Dynamics, a theory with fixed foliation but spatial conformal invariance."* Complementary lesson from the neighbouring foliation-preserving programme, registered with it because it travels with it: Hořava, P. & Melby-Thompson, C.M., "General Covariance in Quantum Gravity at a Lifshitz Point", *Phys. Rev. D* **82**, 064027 (2010), arXiv:1007.2410 — *"the gauge symmetries of the system are foliation-preserving diffeomorphisms of spacetime. Consequently, compared to general relativity, the spectrum contains an extra scalar graviton polarization."* | **NO load-bearing use — registered as the published REPLY to a standing objection.** The objection is "a preferred foliation violates relativity", and it is put to the framework wherever the foliation and the comoving identification are stated: the S3/B-6 material, §B.4.5's τ₅-foliation ↔ CMB-frame identification, the comparative ledger's preferred-structure and Lorentz-invariance lines, and the charter's kill-condition section. Nothing in the corpus is *derived* from shape dynamics; what the row supplies is a citable answer in place of a concession | **N/A — no conclusion is used.** In particular TWT does not claim shape-dynamical equivalence for itself: the equivalence is GR's, and TWT is not GR | **None consumed** | **PRIOR ART / DEFENCE-CLASS.** The honest form of the reply, and it must be stated this way or not at all: *not* "we accept a violation of relativity", and *not* "our foliation is therefore harmless", but **"there is a published equivalence in which a fixed foliation costs no empirical content, its price being a traded symmetry"** — i.e. the premise class is not self-refuting, which is all the theorem gives. It gives nothing about whether *this* framework's foliation is empirically safe; that question is answered by the measured preferred-frame ceilings (I-19, I-28 Collins-class, the α₁/α₂ and GW-speed bounds), which are unaffected by this row | None needed. **The warning that travels with the row and must not be dropped:** foliation-preserving gravity buys its extra structure at the price of an **extra scalar graviton polarization**, which is that programme's chief technical problem. Any TWT gravity sector built on a foliation should expect a scalar mode and should say where it goes — an owed sentence, not a refutation |

---

# Section 14 — Core / Instance bookkeeping (the family split)

*The paper's §A.6 states the architecture — **TWT-Core**, the family, and **Instance V3**, the
first candidate — as a present-tense fact about the theory. This section carries what §A.6 cannot,
because the paper body is history-blind: the dated record of when the split was made, the
row-by-row sort of the Result Index against it, and the pointers to the governing files. The
authoritative source for the axioms, the endorsements and the pick nodes is not this file: it is
`knowledge/audit/pivot_2026-08-17/CORE_CHARTER_DRAFT_2026-08-18.md` (the charter) and
`knowledge/ledgers/TWT_FAMILY_TREE.md` (the tree). Where the paper, this section and those files
differ, the charter and the tree govern.*

## 14.1 The three levels, and what they mean for a Result Index row

- **CORE** — family-defining. Seven axioms (S1a, S2, S3, S4, S5, LS, B-6) and one refusal (the
  substrate is a material medium, not a field). A theory that drops one is a different theory.
- **ENDORSED** — a preferred direction: highly plausible, taken by this instance, and *not*
  family-defining. **Eight as stamped, eight as now standing — and they are not the same eight.**
  Seven of the original eight are unchanged: grain discreteness · Skyrmion-class defects · carrier
  structure · the measured-`G` anchor practice · Koide `c = √2` · `m = E₀` · generations as the
  ℍ-triple with associativity. **`weak = SD` was the eighth and has been PROMOTED OUT** — its menu
  is computed closed (R-171), so it is not a direction a family member may simply reverse; it is
  forced given the structural premise **A-P2** plus the right-handed-singlet datum (R-079). **A-P2
  itself was then stamped ENDORSED (RUL-084) and occupies the eighth slot**: a family member
  diverges by hosting weak isospin outside the substrate's rotation algebra, which is going the
  other way on a preferred direction like any other. A result consuming `weak = SD` therefore DOES
  belong in the CORE+ENDORSED column — conditional on A-P2, not on the retired S7-1 endorsement —
  see Section 14.2's note.
- **PINNED** — an instance parameter of V3, no endorsement implied. Ten at the stamping pass;
  **eleven nodes in the tree today** (`V3-1 … V3-11`, plus the sub-node `V3-2a`). Both numbers are
  correct and are not to be "reconciled": `V3-11` (the Finkelstein–Rubinstein fermionic
  quantization scheme) was added after the stamping tally, when a dependency sweep caught it as a
  load-bearing pick carrying no stamp at all. Quote the tally **as at stamping** and the node count
  **as current**.

A result's row therefore sorts into one of: **CORE-ONLY** (consumes axioms alone),
**CORE+ENDORSED** (axioms plus one or more preferred directions — a *conditional* column, each row
standing or falling with the endorsement it consumes), or **PINNED-CONSUMING** (needs a choice
that belongs to V3).

## 14.2 The sort, as swept

The dependency sweep of 2026-08-18 (`knowledge/audit/pivot_2026-08-17/CORE_INSTANCE_SWEEP_2026-08-18.md`)
classified all 179 Result Index rows against the final stamps, mechanically, by the rows' own
recorded dependencies. **CORE-ONLY 59 · CORE+ENDORSED 55 · PINNED-CONSUMING 64 · UNCERTAIN 1**
(R-078, whose recorded deps are pure algebra while its fourth listed carrier is a
lattice-arrangement object — one adjudication line owed). The two left-hand columns are never to
be merged into a single headline: 59 is a count of results that consume no pick, 55 is a count of
results conditional on an endorsement.

**Amended by the A-1c re-typing (2026-08-21).** The sweep's finding F1 flagged three
PINNED-CONSUMING rows whose only pinned consumption was a recorded `A-1c` edge sitting on purely
structural content. The J,D/Γ rework adjudicated all three as over-recorded and the Section 2
`A-1c` block now carries the disposition: **R-007** (`m = ω`) re-typed to `A-2` — drivenness, per
the block's own former gloss — and **R-036** (rotor field as local Lorentz frame) and **R-127**
(front-phase hand-off) struck, the latter with an owed-if-built prospective edge that cannot be
written until the §D.4.3 branch question resolves. Net effect on the sort: three rows move
Core-side, giving **62 · 55 · 61 · 1** *(a snapshot of the sort as executed — no gate pins these
four numbers; refresh them by re-running the sort, never by incrementing, and treat the tally as
carrying **two named movers**: R-036 below, and the LS-witness question at R-102, held for the
charter)*. S1c's blast radius does **not** exceed the numerical-spine reading. One honesty flag
travels with the arithmetic: R-036's surviving parent is the orientation field (R-102), which is
itself lattice-sited, so its Core-side placement rides the sweep's rule M2 (structural use of a
pinned row's algebraic content does not propagate the pin) rather than being independent of the
arrangement. If M2 is ever narrowed, R-036 is the first row to re-examine.

**What the Core keeps, read off the lists — and the two columns are kept apart here, because the
sweep's own read-out states them as one run and the charter forbids merging them into a single
headline.** *On the axioms alone (the CORE-ONLY column):* the wavefront-isomorphism and
Lorentzian-appearance arc (R-013…R-019); the full QM-postulate and Bell sector (R-020…R-031,
R-160, R-166, R-167); the texture scaffold (R-042, R-145, R-149, R-151); the algebra reference
block (R-092…R-100); the mass-measure cluster at its structural face; and most of the Part-A
picture. *On the axioms plus a named endorsement (the CORE+ENDORSED column — conditional, each
row standing or falling with the direction it consumes):* the Maxwell/Coulomb/photon/charge arc
(R-032…R-035b, R-056…R-063, R-159) and the topology/stability/`B − L` arc (R-052…R-054,
R-084…R-089, R-091c, R-120, R-121), both on the S4b defect-class endorsement; and generations and Koide
structure (R-064…R-068, R-071, R-170) on B-7 and S7-5. **The electroweak structure arc
(R-058…R-062, R-077, R-079, R-082) STAYS in this column, but on a different endorsement than
before (2026-08-21, RUL-082 then RUL-084): S7-1 `weak = SD` is no longer an endorsement but a
forced consequence of a closed menu (R-171), and what the arc now consumes is premise **A-P2** —
that weak isospin is a 3-dim `su(2)` inside grade-2 `so(4)` at all — together with the
right-handed-singlet datum. A-P2 is FRAMING in the engine and is **stamped ENDORSED (RUL-084)**, so
the arc is conditional on a preferred direction exactly as the other rows in this column are, and
the column of its own that it briefly occupied while A-P2 was unstamped is CLOSED. It is not
Core-clean: the conditioning is an endorsement plus a datum, never the axioms alone.** **What the Core does not have at either
level: any gravity result, any absolute mass or scale number, any kernel-branch result, and any
lattice-sited computation.**

**Rider on "Core-clean" (charter §4, and it travels with every quotation of the count).**
Core-clean is a *consumption* classification — it says a result uses no instance pick — **not** a
claim of derivation-completeness. The QM package in particular buys its structure with registered
imported mathematics (Section 13: the tensor-product composition rule, the singlet form, Gleason),
so it is a relocation with a gain, exactly as the signature is.

## 14.3 Falsifier levels

The same sweep classified §E.3.1's sixteen rows. **Fifteen are family-level; one is
instance-level** — row 12 (no baryon containing a top quark), whose kill number `Γ_t · Θ_0 ≈ 7.2`
rides the ANW inertia and hence the pinned hadron toolbox and calibrations. Rows 4 and 5 are
family-level *by deliberate choice*: B-6 was stamped CORE, which is what makes the Bell-ordering
channel the family's kill condition rather than the instance's. Row 11's former wording sited the
charge spectrum "on D4 trivector content"; the trivectors are Clifford objects and the row is
family-level, and the paper's wording is corrected accordingly.

## 14.4 The sweep's standing findings

Recorded here because each is a bookkeeping consequence with no home in the paper body:

- **F2 — the Core has no gravity sector.** Every gravity result (R-037…R-041, R-047, R-050,
  R-105's values, R-119, R-163, R-164) and the LV-protection result R-165 is PINNED-consuming.
  Structural gravity is owed to the family as a re-grounding on the axioms, stated as an open
  jurisdiction rather than papered over (paper §B.6 opening; §A.6.5).
- **F3 — the QM sector is Core, but its dynamical-safety argument is not.** R-117 ("why QM and
  Bell are unaffected by the memory fork") consumes the canted-vacuum stiffness chain, so the
  family keeps the postulates and, as things stand, loses its own protection argument. A
  family-level restatement of R-117's symmetry content is a cheap, high-value item.
- **F4 — the fermionic-quantization pick was unstamped** when the sweep ran; it is now tree node
  V3-11, PINNED, costing one bit, branch-blind with respect to the open LS-ℤ₂ node.
- **F5 — electroweak *structure* is family; electroweak *breaking* is instance.** R-086/R-086a/
  R-090 ride the D condensate; `weak = SD`, V−A, GMN, charge quantization and the `3/8` identity
  do not.
- **F6 — carrier-face riders.** R-023/R-027/R-028/R-160 consume the pairing and costed-carrier
  picks on carrier backgrounds only (sweep rule M4). If the carrier face is ever promoted into
  Part B proper, those four rows become PINNED-consuming as written.

## 14.5 Pointers

- **The family definition:** `knowledge/audit/pivot_2026-08-17/CORE_CHARTER_DRAFT_2026-08-18.md`
  (ratified; no open business). Paper: §A.6.1–§A.6.3.
- **The pick register:** `knowledge/ledgers/TWT_FAMILY_TREE.md` — root, preferred directions, the
  V3 branch table with each node's menu, the named result that required it, what rides it, and its
  revert clause; plus the Core-level open branch LS-ℤ₂. Paper: §A.6.4 carries the compressed form.
- **The stamps:** `knowledge/audit/pivot_2026-08-17/STAMPING_SHEET.md` (final tally: 6 CORE + the
  refusal / 8 ENDORSED / 10 PINNED).
- **The sort:** `knowledge/audit/pivot_2026-08-17/CORE_INSTANCE_SWEEP_2026-08-18.md`.
- **The kin registrations** (SHP, Kleinert, Volovik, causal sets, shape dynamics): Section 13.5
  above, rows I-24 through I-27, plus the SHP verification report in the same audit directory.

## 14.6 History (dates live here)

- **2026-08-17** — the Core/Instance split adopted as the programme's architecture after an
  external review diagnosed a family→instance collapse: at every branching junction the choice had
  been made and recorded as a consequence rather than as a branch. The human coordinator performed
  the stamping pass the same day, which ratified the split by execution.
- **2026-08-18** — the stamps refined into the four-term vocabulary (CORE / ENDORSED / PINNED /
  HELD) and the final tally re-stamped; the dependency sweep run against it; the family tree
  instituted as the standing pick register; the charter drafted and ratified; the LS axiom added
  by signed amendment after a keeper adjudication found the local degrees of freedom fixed nowhere
  in the original six and asserted at three incompatible resolutions across the corpus.
- **2026-08-19** — measured: the split had reached none of the paper's ~6,800 lines, so a reader
  still met every pick and both empirical exposures as facts about *the theory*.
- **2026-08-21** — the split executed through the paper: §A.6 added, the front matter and the
  falsifier section given the family/instance reading, and the picks re-attributed at their
  first load-bearing sites. This section added in the same pass.

---

*End of companion file.*
