# Time-Wave Theory — Foundational Paper V3, Companion File

*Companion to `TWT_foundational_paper.md` (V3). This file consolidates all annexes, the
back-of-book bookkeeping (Result Index, Dependency Graph, Engine ↔ Paper Map, Pending-Values
Registry), the geometric-reinterpretation catalog, the methodology principles, the development
log, the stable-spectrum enumeration, the wave-phase stability ladder, and the bibliography.
Unconventional but practical: everything a reader might want beyond the main narrative is here.*

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
| A-1c | J + D coupling structure on D4 NN bonds | FRAMING (structure) + INPUT (ratio) | Opening, D.3 | Coupling structure (symmetric exchange + chiral DM on `e_4`-bonds) is structural — the unique pair allowed by parity. Ratio `D/J ≈ 0.79` is INPUT, calibrated to leptons. |
| A-2 | Driven dynamics premise — the substrate is driven; EOM is the #1-gap placeholder | AXIOM-with-#1-gap | Opening, D.5 | Not on par with A-1a / A-3 in solidity. Gates absolute coupling magnitudes, masses, Θ_rel. |
| A-3 | Wavefront / signature locking — observers read `e_4` as time | AXIOM | Opening, A.2 | The Lorentzian signature follows (R-014, R-015). |
| A-1* | Matter = defect (canon §0) | AXIOM | Opening, A.3 | Matter is topologically protected pattern; mass is meta-time rotor frequency. Inside-positive / outside-hole are frame images. |
| A-2* | Working frame is outside the wavefront (canon §0) | AXIOM (method) | Opening, A.2 | Inside-frame for data, outside-frame for derivation. |

---

## Part A — The Picture

| ID | Statement | Tier | Engine | § | Deps | Used by | Notes |
|---|---|---|---|---|---|---|---|
| R-001 | Wave-train as succession of S³ wavefronts advancing along `e_4` | DERIVED-STRUCTURAL | — | A.1 | A-1a, A-3 | R-002, R-043 | The wave is `e_4`-propagating; observers are mechanically locked to a primary resonant wavelet. |
| R-002 | S³ wavefront topology; π_3(Spin(4)) = ℤ × ℤ classifies matter | DERIVED-A | pi3_S3_integer_completion | A.2 | R-001 | R-006, R-009, R-052 | Two ℤ factors come most directly from the chiral factorization Spin(4) = SU(2)_+ × SU(2)_−. The framework's working basis is the L-orbit / Q-orbit decomposition (by e_4-content), which is DIFFERENT — `𝓛 ⊕ 𝓠 ≠ SU(2)_+ × SU(2)_−` as decompositions of so(4). The relabeling from chiral basis (n_+, n_−) to orbit basis (n_𝓛, n_𝓠) is justified by the symmetric-pair / fibration bridge of A.5.2: `Spin(3) ↪ Spin(4) ↠ S³_𝓠 = Spin(4)/Spin(3)` with π_2(Spin(3))=0 gives `0 → ℤ → ℤ × ℤ → ℤ → 0`, so (n_𝓛, n_𝓠) is a change of basis of π_3(Spin(4)). Leptons wind into the diagonal Spin(3) (subgroup); baryons wind into the coset S³_𝓠 (coset). Coset-respecting relabeling of a chiral counting, not identification of the two splits. |
| R-003 | Working-frame discipline: outside-frame for derivation | METHOD | matter_stability_outside_frame | A.2 | A-2* | (all derivations) | Inside view used only to import data. |
| R-004 | Matter as defect — topological winding in rotor field, not piece of stuff | DERIVED-STRUCTURAL | matter_stability_outside_frame | A.3 | A-1*, R-001 | R-005, R-006, R-016, R-039 | Load-bearing throughout. Canon §0 statement. |
| R-005 | Defect's two faces (spatial winding + meta-time rotor) coupled by I_4 Hodge duality | DERIVED-STRUCTURAL | I4_maps_L_to_Q | A.3 | R-004, R-010 | R-007, R-053 | The two faces are not independent observables.  Sector-split (2026-07-02 sweep, R-127/R-128): the observer-visible winding↔mass-phase-axis relation is identity in L (lepton), I₄-dual in Q (quark); R-005's coupling is substrate-level. |
| R-006 | Topological stability of winding integer (cannot deform to vacuum) | DERIVED-A | pi3_S3_integer_completion | A.3 | R-002, R-004 | R-054, R-084, R-089 | π_3(S³) = ℤ for baryons; Hopf invariant for leptons. |
| R-007 | Mass = meta-time rotor frequency `m = ω` | DERIVED-STRUCTURAL | wave_E_complex_structure + wave_E5 | A.4 | R-005, A-1c | R-008, R-017, R-038 | Half-angle convention forced by spinor inheritance. |
| R-008 | Quarks are decomposition-components of one baryon defect (NOT independent objects that happen to be bound); the mass-bearing object is the baryon | DERIVED-STRUCTURAL | single_quark_no_rest_mass_axis | A.4 | R-007, R-004, R-053 | R-051, R-085, R-091a | V2 §3.2 ontology. Per-flavour MS-bar "quark masses" remain *indicators* of facet structure, never *verifiers* of standalone-quark predictions (canon §5). Reframed in V3 from V2's "quarks have no mass" — the cleaner statement is that quarks are not the kind of object that has mass, because they are not independent objects in the first place. |
| R-009 | L-orbit `{e_{12}, e_{13}, e_{23}}` and Q-orbit `{e_{14}, e_{24}, e_{34}}` orthogonally decompose grade-2; the pair `so(4) = 𝓛 ⊕ 𝓠` carries a symmetric-pair Cartan structure `[𝓛,𝓛] ⊆ 𝓛, [𝓛,𝓠] ⊆ 𝓠, [𝓠,𝓠] ⊆ 𝓛` (𝓛 = isotropy of e_4, exp = diagonal Spin(3); 𝓠 = coset complement, exp not a subgroup, hosts S³_𝓠 = Spin(4)/Spin(3)); fibration `Spin(3) ↪ Spin(4) ↠ S³_𝓠` bridges chiral and orbit bases of π_3(Spin(4)) = ℤ × ℤ | DERIVED-A | L_Q_orthogonal_decomposition + is_L_bivector + is_Q_bivector + L_algebra_su2_closure | A.5.2 | A-1a | R-002, R-052, (many downstream) | Both 3-dim bivector triples; both square to −1. Engine-banked decomposition; the symmetric-pair Cartan relations and the fibration framing are stated explicitly in V3 prose (V2 left the relabeling implicit). |
| R-010 | Pseudoscalar `I_4 = e_1 e_2 e_3 e_4`; `I_4² = +1`; Hodge map L ↔ Q | DERIVED-A | I4_squared + I4_maps_L_to_Q + duality_map + hodge_star | A.5 | R-009 | R-005, R-019, R-080, R-090 | A real duality, not a complex unit. |
| R-011 | Rotor sandwich half-angle: `R = exp(θ B/2)`, `R(2π) = −1` on spinors | DERIVED-A | exp_unit_bivector + half_angle_overlap | A.5.5 | R-009 | R-025, R-027 | One-sided action on spinors gives half-angle; two-sided on vectors gives ordinary angle. |
| R-012 | Spinor minimal left ideal `𝒮 = Cl(4,0) · s_0`, `s_0 = (1+e_4)/2` idempotent | DERIVED-A | s0 + is_idempotent + spinor_real_dof | A.5.4 | A-1a | R-024, R-026, R-095 | Real dim 8, quaternionic dim 2. |
| R-012a | Cl(4,1) extension: `e_5² = −1`, central `E = I_4 · e_5` with `E² = −1` supplies the global geometric complex unit (external U(1) phase); native formalism is `Cl(4,0) + ℍ`; `e_5` grounding rule | DERIVED-A | wave_E5 + wave_E_complex_structure + spatial_vs_phase_partition + cl41_grounding_litmus + cl41_phase_is_external_u1 + cl41_idempotents_note | A.5.6 | R-010, R-012 | R-007, R-035a, R-094, R-095 | A Cl(4,1) construction is grounded iff its `e_5`-content reduces to PHASE in the Cl(4,0)+ℍ picture (canon §5 guardrail). Introduced in A.5.6; full at §D.1. |

---

## Part B — Spine results

| ID | Statement | Tier | Engine | § | Deps | Used by | Notes |
|---|---|---|---|---|---|---|---|
| R-013 | `γ⁰ := e_4, γʲ := e_4 e_j` satisfy Cl(1,3) Dirac relations `{γ^μ, γ^ν} = 2η^{μν}` | DERIVED-A | gammas + gamma0_gammaj_reduces_to_ej | B.1 | A-3, R-009 | R-014, R-017, R-026 | Engine-verified directly. |
| R-014 | Cl(4,0) ≅ Cl(1,3) ≅ M₂(ℍ) — wavefront isomorphism lands on (1,3), not (3,1)/(2,2) | DERIVED-A | cl_dimension | B.1 | R-013 | R-015, R-038 | The Lorentzian signature is forced; the algebra (M₂(ℍ) vs M₄(ℝ)) is what's determined, not the sign convention. One of two cleanest spine results. |
| R-015 | Lorentzian signature of observed spacetime is algebraic shadow of wavefront-locked observer in Euclidean substrate | DERIVED-A | gammas + cl_dimension | B.1 | A-3, R-013, R-014 | (paper headline) | Engine-verified. Two inputs: algebra fact + observer stipulation; both labeled. |
| R-016 | Matter-as-defect Lorentz protection: one substrate, one light-cone | DERIVED-STRUCTURAL | equivalence_principle_protection + matter_stability_outside_frame | B.1, B.6 | R-004 | R-039, R-040 | Defuses Collins-2004 radiative naturalness obstacle. Offensive win, not defensive tuning. |
| R-017 | Klein–Gordon from 5D hyperbolic master by Fourier reduction at `k_4 = m` | DERIVED | wave_E_complex_structure | B.2 | R-007, R-013, R-123 | R-024, R-026 | Identifies rest mass with `e_4`-Fourier label. Engine support hardened 2026-07-02 by R-123: the consuming identification = R-123's derived restriction identity ∧ its named residue (ii) (one-particle sector at k_4) — previously the "m = k_4" identification existed in the engine only as a docstring string. |
| R-018 | Lorentz generators K_j = (1/2)e_j (non-compact), J_i = −(1/2)e_{jk} (compact); so(1,3) closure | DERIVED-A | boost + rotation + so13_closure_signs | B.2 | R-013 | R-019 | Bulk's compact so(4) becomes observer's non-compact so(1,3) via φ. |
| R-019 | Thomas precession from algebra: `[K_i, K_j] = −ε_{ijk} J_k` | DERIVED-A | thomas_KK | B.2 | R-018 | — | The minus sign is the signature of so(1,3) vs so(4). |
| R-020 | Born subspace `{1, B}` forced by centralizer intersection in Cl⁺(4,0), not stipulated | DERIVED-A | born_subspace_one_B_forced | B.3 | R-009, R-012 | R-021, R-023 | (W) ∩ (S) ∩ (E) = `{1, B_a}` — engine-exact intersection. |
| R-021 | QM Postulate 1: complex Hilbert space from transverse bivector plane | DERIVED | born_subspace_one_B_forced | B.3 | R-020 | R-022, R-023, R-024 | `i = B`; standard L² inner product from grade-0 part of Cl product. |
| R-022 | QM Postulate 2: self-adjointness as `M̃ = M` (Clifford reversion) | DERIVED | — | B.3 | R-021 | R-023 | Reality of measurement outcomes forces reversion-self-adjointness. |
| R-023 | QM Postulate 3 (Born rule): squaring forced even-power by chirality symmetry | DERIVED structurally (even-power); the EXPONENT is upgraded by R-160 from plausibility-modulo-degree to a theorem given (F1–F4) + import-exempt Gleason | — | B.3 | R-020, R-021 | R-027, R-160 | Not a Gleason re-derivation: the framework supplies Gleason's hypotheses (R-160), it does not re-prove the theorem. |
| R-024 | QM Postulate 4: Schrödinger from KG envelope, exact `mc²` cancellation | DERIVED | — | B.3 | R-017, R-021 | — | Correct sign of kinetic term and of first relativistic correction. |
| R-025 | QM Postulate 5: spin-statistics from Spin(4) half-angle; fermionic Skyrmion quantization is SELECTION (not forced in bare SU(2)) | DERIVED + SELECTION | dirac_ideal_idempotent + skyrmion_collective_quantization_under_v2_3p2 + colour_z3_holonomy_cannot_source_fr_sign | B.3 | R-011, R-012 | — | Honest tier per V2 §14.6 W-LIVE-4 re-attack: three substrate routes all FAIL. 2026-07-02 (N35): closure route W1's finite-ℤ_3-holonomy instance closed-negative (DERIVED-generic group theory); W1 reduced to P2-4's induced-level question — SELECTION now protected by four engine-checked negatives. 2026-07-03 (R-141): the induced level answered at the PARITY level — ODD ⇒ the selection upgrades to INDUCED-given-(P1)+(P1b), conditional and revocable; the four negatives still protect all substrate-internal routes. 2026-07-03 (R-136): the selection gains a SECOND independent empirical anchor — the bosonic branch predicts a bound scalar `(0,0)` dibaryon ground state at `B = 2`, refuted by the observed deuteron (evidence for the pick, not a derivation; shared (Q) premise). |
| R-026 | Dirac equation from KG factorization `𝒟 ψ = ±m ψ B` with right-acting `B`; equivalent to Hestenes form on the minimal left ideal | DERIVED | hestenes_Isigma3 + dirac_ideal_idempotent | B.3 | R-013, R-017, R-012 | — | Right-acting `B` is mandatory for `□ + m²`. |
| R-027 | Tsirelson bound `S = 2√2` from rotor-sandwich half-angle on Cl(4,0) spinor | DERIVED-A | tsirelson_S + bell_correlation + chsh_S + half_angle_overlap | B.4 | R-011, R-023 | R-028, R-031 | Dimensional fingerprint of S³ → S² projection. |
| R-028 | Multipartite MK bound `\|M_n\| = 2^{(n+1)/2}`, engine-verified n=2-5 | DERIVED-structural | mermin_klyshko_value + mermin_value | B.4 | R-027 | — | GHZ class. W (non-GHZ) class is a located construction gap (`w_state_located_gap`). |
| R-029 | `ρ_A = (1/2)𝟙` identity — no-signaling and non-separability are the same fact | DERIVED (standard QM identity; engine partial-trace check proposed, none exists yet) | — | B.4 | R-027 | R-030, R-031 | All structure drained into correlations; locally pure noise, jointly perfectly ordered. |
| R-030 | Bell-memory bridge: same `Im χ` governs decoherence and pair-memory | FRAMING + value-gated | im_chi_falsifier_budget_KSS_GW_macromolecule | B.4 | R-029 | R-119 | Canonical falsifier §E.3 VG-1. |
| R-031 | Selection foliation = comoving frame (testable corollary) | FRAMING + falsifier-testable | — | B.4 | R-029 | — | Canonical falsifier §E.3 rows 6–7. |
| R-032 | Maxwell `∇F = J` in Cl(4,0); grade-1 source delivers Gauss + Ampère, grade-3 source = 0 delivers Faraday + ∇·B = 0 | DERIVED-A | maxwell_grade_structure + maxwell_four_laws | B.5 | R-009 | R-033, R-034, R-035 | Substrate origin: `J` is wavefront projection of L-orbit bivector winding. |
| R-033 | No magnetic monopoles: grade-3 part of `∇F` vanishes because `J` is grade-1 only | DERIVED-A | maxwell_grade_structure | B.5 | R-032 | — | Geometric forbiddance, not mere observation. |
| R-034 | Coulomb potential `V(R) = Σ_1 · Σ_2 / (4π R)`; like-repels, unlike-attracts | DERIVED | coulomb_potential + coulomb_sign_rule + coulomb_is_harmonic | B.5 | R-032 | — | Green's function in 3D. |
| R-035 | Photon as L↔Q-bridging bivector strain mode; masslessness from topological winding-charge conservation (not EWSB) | DERIVED | photon_strain_mode | B.5 | R-032, R-009 | R-035a | EWSB-independent masslessness — topological. |
| R-035a | Fine-structure constant `α_em` as reactive grade-0 Clifford invariant — L↔Q reconversion strength `α-object = ⟨Σ̃_F · Γ_recon · Σ_L⟩_0`; Type-B (analytic in coupling, no `exp(−S)`) | DERIVED (ontology) + GATED (magnitude) | alpha_em_meaning + alpha_em_value (raises) | B.5b | R-035, R-012a | R-035b, R-035c | What α *is*, not what it equals. Magnitude #1-gap-gated via Im χ. |
| R-035b | `g` is α's algebraic sibling via `g² = 4πα / sin²θ_W = 4πα · (8/3)` with `sin²θ_W = 3/8` proven (R-082); EW sector reduces to ONE #1-gap magnitude, not two | DERIVED-A | weinberg_sin2 | B.5b | R-035a, R-082 | — | Parameter-economy hook. Three SM EW couplings collapse to one dial; same `Im χ` samples both. Engine cite covers the 3/8 only; the sibling relation is algebra given it. |
| R-035c | Length-ladder identity `r_e · a_0 = λ̄_C²` from one geometric overlap (NOT a value over-determination of α) | DERIVED-A | alpha_em_meaning | B.5b | R-035a, R-055 | — | `r_e = α λ̄_C`, `a_0 = λ̄_C / α`; the ratio identity falls out, α cancels. |
| R-036 | Rotor field as local Lorentz frame; substrate carries 4D frame with local Spin(4) symmetry | DERIVED-STRUCTURAL | — | B.6 | R-002, A-1c | R-037, R-039, R-042 | Spin(4) → Spin(3,1) after wavefront iso. |
| R-037 | Sakharov induced EH: `G_N⁻¹ ~ N_eff Λ²/(12π)`; `Λ ∈ [0.16, 0.72] M_Pl` bracket | DERIVED-generic-given-4D | sakharov_induced_gravity + induced_G_bracket_mode_count + induced_G_only_monad_scale_enters + induced_G_leading_coefficient_mass_independent + induced_G_quadratic_divergence_from_4D | B.6 | R-036, A-1a | R-038, R-041 | The Λ² scaling is generic-given-4D, not a dynamical derivation. Absolute magnitude #1-gap-gated. |
| R-038 | Newton 1/r law from Sakharov slow-motion limit; `T^{μν} = ρ u^μ u^ν` worldline stress | DERIVED | — | B.6 | R-037 | R-124 | Universal attraction from spin-2 sourcing by positive T^00. |
| R-039 | `γ = 1` from matter-as-defect Lorentz protection | DERIVED-STRUCTURAL | equivalence_principle_protection | B.6 | R-016, R-037 | R-124 | One substrate, one light-cone. |
| R-040 | Induced G sign positive: spin-2 spectral positivity (`C_T > 0` by unitarity) ≡ substrate stability | DERIVED-sign-only | induced_G_sign_cross_check | B.6 | R-037 | — | Two-pillar unification — same physics in different language. Removes RF-1 falsifier. |
| R-041 | `ξ = 0` at leading order via Maurer–Cartan shift symmetry; catastrophic `ξ = 1/6` cancellation excluded | FRAMING + CONDITIONAL (engine self-tag: shift-symmetry lemma — substrate supplies the symmetry, QFT the implication) | sakharov_xi_minimal_coupling | B.6 | R-037 | — | Goldstone-protected. Residual ξ ~ (f_π/Λ)² ~ 10⁻⁴⁰–10⁻³⁹. Removes RF-2 falsifier. |
| R-042 | Texture tetrad `e^a_μ[R, ∂R]` structural geometry CLOSED conditional | DERIVED-STRUCTURAL-CONDITIONAL | texture_tetrad + texture_metric_candidate + texture_metric_diffinvariance + texture_metric_tt_graviton + texture_metric_vierbein + texture_matter_gravity_coupling | B.6 | R-036 | — | Metric `h_{μν} = ⟨Ω_μ I_4 Ω_ν⟩_0` forced up to one premise. |
| R-043 | Arrow of time as `+e_4` propagation; causality is the same fact | DERIVED-STRUCTURAL | — | B.7 | R-001, A-3 | R-044 | Not a separate postulate. |
| R-044 | Three asymmetries (thermodynamic, causal, weak handedness) unified as one cosmological IC | DERIVED-STRUCTURAL | — | B.7 | R-043, R-086 | — | One direction picks all three. |
| R-045 | `c_meta = c` on average across the wavefront | DERIVED-STRUCTURAL + falsifier-testable | — | B.7 | A-3 | R-047 | Sector- or epoch-varying differential c_meta is canonical falsifier §E.3 row 8. |
| R-046 | Hubble radius as causal/crossover scale, not geometric radius of curvature | DERIVED-STRUCTURAL | — | B.7 | R-001 | R-119 | Topological S³ identification compatible with observed flatness if R_curv ≫ R_H. |
| R-047 | Volovik dissolution of CC problem: self-sustained medium has zero gravitating vacuum energy at equilibrium (`ε − μn = −P = 0`) | DERIVED + framing-of-residual | gravitating_vacuum_energy + lambda_resolution_structure | B.7 | R-037 | R-119 | Equilibrium value zero by Gibbs-Duhem identity. Λ ~ H² residual is the driven-dissipative deviation (value-gated). |
| R-048 | Macroscopic COM bivector reduction: six conserved blades collapse to three on `P = 0, R_cm = 0` | DERIVED-A | macroscopic_LQ_split + worldline_bivector + polar_moment_of_inertia | B.8 | R-009 | R-049, R-050 | Central-force pairwise cancellation by Newton-3. |
| R-049 | L/Q split sorts micromatter species (R-009) AND macroscale conserved-invariant vs spent-integral — one algebraic split, two manifestations | DERIVED-STRUCTURAL | macroscopic_LQ_split + L_Q_orthogonal_decomposition | B.8 | R-009, R-048 | — | The structural payoff of the bivector-native picture. |
| R-050 | Sundman: triple collision forbidden unless `L = 0` | DERIVED-A-given-§B.5 | — | B.8 | R-048, R-034 | — | Cauchy-Schwarz on bivector norm + Newtonian far-field. |
| R-050a | Eulerian reframing — bodies are defect-features of one wavefront; the atlas-with-seams of the classical N-body problem is a projection artifact of field → feature extraction, not a feature of the dynamics; baryon-density integral bridges field to body positions | FRAMING | — | B.8 | R-004, R-049, R-006 | R-120 | Dynamics-coherent version depends on multi-defect well-posedness (§E.3 SC-1, structural-coherence condition). The ontology — bodies as features of one wavefront — is solid; the multi-defect Cl(4,1) wave equation with N back-reacting topological sources is a structural target. |
| R-123 | Defect-ω → front-k_4 keystone bridge: a meta-time rotor restricted to the wavefront lock `x_4 = c_meta·τ_5` is x_4-periodic at `k_4 = ω/c_meta` (exact, axis-independent incl. central `E`; half-angle sign flip at 2π/k_4); two residues NAMED — (ii) one-particle sector AT k_4, (iii) `E → B_a` complex-unit hand-off | DERIVED-A (restriction identity) + FRAMING (residues ii, iii) | defect_rotor_frequency_reads_as_k4_on_front | B.2.1 | R-007, R-013, R-045 | R-017, R-125, R-127 | Banked 2026-07-02 (ledger N36; twt-reviewer HOLDS at the split tier). Hardens R-017's engine support — "m = k_4" previously existed only as a docstring string. Residue (ii) is the item's actual remaining gap (§D.4.6 soliton-fluctuation Paper-2 question); checked on generic non-special configurations per the Phase F lesson. WP-MASS-MEASURE chains 1/2/5 inherit. |
| R-124 | Charged-defect worldline EOM `ṗ = qF·u` + cyclotron readout `ω_c = qB/m` (WP-MASS-MEASURE chain 1): rest-frame anchor from R-034 elastic overlap (static force reads the 𝓠-part only; pure 𝓛-strain exerts zero static force on a monopole winding by exact ⟨Σ_Q Σ_L⟩₀ = 0) + Spin covariance via transitivity determine the force law everywhere; Schur commutant-2 cross-check (equivariant bilinear maps Λ²×V→V = span{F·u, (I₄F)·u} exactly; the I₄-dual killed by the anchor; u-cubic candidates collapse exactly); `f·u = 0` exact ⇒ `dm/dτ = 0` a consequence; exact rotor solution rotates at `ω_c = qB/m` | DERIVED-A (algebraic spine) + DERIVED-conditional (worldline/point-monopole limit, R-038 class; AND the Spin-covariance premise R-014 + R-039 DERIVED-STRUCTURAL — named condition per reviewer amendment) + INHERITED-CONDITIONAL (inertia leg `m = k_4 = ω/c_meta` via R-123 residue (ii)) | charged_defect_worldline_eom_cyclotron | B.5.5 | R-032, R-034, R-014, R-038, R-039, R-123 | — | Banked 2026-07-02 (twt-reviewer HOLDS + 2 amendments applied; commutant-2 independently reproduced by the reviewer via rep theory + a separate generating set). Chains (1)+(2) now both sit MODULO residue (ii) alone; residue (ii) gates three of five signature chains — the item's critical path. α_em magnitude stays #1-gap; magnetic-moment/gradient-B forces, nonlinear-in-F corrections, g-factor, radiation reaction all named NOT-derived. First Class-1 queue item (companion Section 12) to close. |
| R-125 | Defect phase collective mode sits at `k₄ = ω/c_meta` (R-123 residue (ii), existence/location half): `Ω = R̃∂R` exactly invariant under the constant left shift `R → gR` (Spin(4) `g`) ⇒ by the symmetry-linearization lemma the shift generator applied to the rest defect `R* = exp(ûωτ₅/2)R₀(x)` is an exact solution of the linearized EOM — the co-rotating zero mode `(û/2)R*`, reading at lab frequency exactly `ω`, front `k₄ = ω/c_meta`; equals `(1/ω)∂_τ₅R*` so `τ₅`-autonomy is an independent sufficient premise. AXIS-SPLIT (reviewer amendment): bivector `û` rides the banked left-Spin(4) shift; `û = E` does NOT (`Ω(g_E R) = e^{Eθ}Ω(R)` exactly, engine — the Ω-built sector is not E-phase invariant) and routes through τ₅-autonomy or an unbanked U(1)_E dynamical invariance | DERIVED-via-symmetry-CONDITIONAL (C1: û-phase symmetry OR τ₅-autonomy of the full EOM, axis-split, coherence-argued NOT proven for the §D.5 kernel; C2: separable rest-defect ansatz = R-123's idealization) | defect_phase_collective_mode_at_k4 | D.4.6 (+ §B.2.1 cross-cite) | R-123, R-041 (shift symmetry), R-112 (master eq) | R-126 | Banked 2026-07-02 (twt-reviewer MISLABELED→fixed→HOLDS: the E-axis premise was scoped down per the reviewer's engine finding, which is itself now banked as a check). SHARPENS residue (ii), does NOT close it: remaining (H1) localization/normalizability vs the carrier, (H2) identification as THE one-particle pole (§D.4.6 shape-mode spectrum, Paper-2). New falsifier face: a computed spectrum whose one-particle pole sits elsewhere than `ω/c_meta` falsifies `m = k₄`. The s=3/Adler-zero symmetry-shortcut move class, applied to the one object it can reach (the Goldstone phase mode itself). |
| R-126 | Zero-mode multiplet labels: the rest defect's EXACT symmetry-mode sector reads ONLY `k₄ = ±ω/c_meta`. Left shifts split by the û-commutant (commuting dim-2 → `+ω` incl. the R-125 phase mode; anticommuting dim-4 → `−ω` exactly, via `B·Q(τ₅) = Q(−τ₅)·B` — the conjugate branch); right shifts → `+ω` (NEW engine facts: `Ω(Rg) = g̃Ωg` exact ⇒ every scalar Ω-word right-invariant by cyclicity); translation-type → `+ω`. No third label anywhere in the catalog | DERIVED-via-symmetry-CONDITIONAL (per-class premises: P1 left banked; P2 right scalar-sector engine-exact, DM/topological right-status OPEN — and the DM caveat is two-sided at kernel level, covered by the inherited C1; P3 translations = homogeneity, continuum-limit over discrete D4, WP-LV1 class; C1/C2 inherited from R-125) + DERIVED-A (right-covariance facts; label table; commutant dims (2,4)) + FRAMING (−ω antiparticle reading; boost/moving family named NOT banked — the chain-(2) second-angle handle; multiplet-as-(H2)-skeleton on the defect-linearized side; multiplicity gloss is prose, NOT an engine-backed count — mode families overlap, do not cite a multiplet dimension) | defect_zero_mode_multiplet_labels | D.4.6 | R-125, R-123, R-041, R-112 | — | Banked 2026-07-02 (twt-reviewer HOLDS; 3 non-blocking notes applied — multiplicity gloss scoped, DM two-sidedness noted, same-pass sync). Supports residue (ii)'s (H2) half: one rest label + conjugate, no spread. Two new falsifier faces: a DM-induced right-sextet lift (predicted fine structure); any symmetry-mode label ≠ ±ω/c_meta. |
| R-127 | Front-phase hand-off resolves R-123 residue (iii) AS A SELECTION: projecting the defect history `B_a·s₀·q_h(τ₅)` onto the observer's forced complex line `{1, B_a}` (R-020) gives an exact dichotomy — only `û = ±B_a` (the winding blade itself) stays in the line as a pure propagating phase at exactly `±ω` (`k₄ = ω/c_meta` on the lock); other ℍ axes read as spin precession (in-ideal, amplitude-only shadow); the central `E` leaves the Cl(4,0) ideal (density-node shadow). One blade, two roles — §A.3's two-faces made exact; no `E → B_a` conversion owed; `E` keeps its global/colour complex-structure role | DERIVED-A (dichotomy: exact, all three B_a, orthogonal line basis, left/right convention-free for winner and E) + DERIVED-CONDITIONAL (the selection; C1 §B.3.1/R-020 grade-2 ansatz — the corpus B_a grade double-use flagged for disambiguation; C2 banked Part-B pure-phase criterion + empirical face; C3 L-orbit scope, axis menu = ℍ ∪ {E}) + FRAMING (ξ-gloss reconciliation: rotation ALONG a flat direction is kinetic, not a potential lift — reviewer verified nothing engine-checked in sakharov_xi_minimal_coupling pins mass to E) | front_phase_handoff_selects_winding_axis | B.3.1 (+ §B.2.1, §A.4 superseded-gloss notes) | R-020, R-123, R-021, A-1c | R-128 | Banked 2026-07-02 (twt-reviewer HOLDS + 2 sweep fixes applied: §A.4 stale glosses annotated; C1 corrected to the R-020 grade-2 form). Retroaction: R-125's unbanked E-axis premise MOOT for the physical mass phase (winner rides the banked left-Spin(4) branch); residue (ii) (H2) target = the B_a-phase mode. Still open: EOM-level axis lock (selection is consistency-forced, not dynamical); baryon Q-orbit analog. New falsifier face: a matter-wave mass signature that is not a propagating phase. |
| R-128 | Q-orbit extension of R-127: for a baryon-sector winding `B_q`, the observer's forced complex line is `{1, I₄B_q}` — the Hodge dual (up to sign), all three `B_q` (true-nullspace-verified by reviewer) — and the mass phase locks to `û = ±I₄B_q` (exact dichotomy; winding axis leaks to the complementary idempotent sector). The lepton lock is parity-EVEN (identity); the quark lock is parity-ODD (`P(I₄X) = −I₄P(X)`, any improper reflection) ⇒ a ℤ₂ relative-orientation label parity flips: quark-sector defects come in statically-degenerate parity-mirror pairs (the SEAT of the up/down doubling), charged leptons provably carry no label; the mirror pair ≠ the antiparticle pair (σ rotation-invariant). Lock operator = I₄ ⇒ the `⟨I₄⟩`/µΨ₀ dial enters quark mass-phase geometry through the lock, absent from the lepton lock | DERIVED-A (centralizer, dichotomy, parity facts — exact; reflection-choice-immune per reviewer) + DERIVED-CONDITIONAL (C1′ Q-orbit analog ansatz — R-020's 'structural analog, not load-bearing' inherited; C2′ same-observer premise; C3′ R-127 criterion) + FRAMING (up/down SEAT; the µΨ₀-through-the-lock tie — the coupling not constructed; split stays dynamical per N28) | qorbit_mass_phase_dual_lock_parity_odd | B.3.1 (+ §C.3.13 note) | R-127, R-020, R-077, R-123 | — | Banked 2026-07-02 (twt-reviewer HOLDS + 3 cosmetic fixes; N28 verified untouched — statics gives two-ness, not the split; N32a tie verbatim-accurate). New falsifier faces: a charged-lepton parity-mirror mass-partner tower; a third comparable tower per Q-orbit slot. Would change if: banked Q-orbit defect construction hardens C1′; quantitative ⟨I₄⟩-through-the-lock coupling → a 2b mechanism row. |
| R-129 | ⟨I₄⟩-condensate ideal-channel rule (the R-128 mechanism face, first move — ELIMINATION): s₀Ms₀ = Ms₀ if [M,e₄]=0, = 0 if {M,e₄}=0 (complete 16-blade table; survivors = the e₄-commutant = the (W) family; bare I₄ dies identically — Ψ̃I₄Ψ = 0 all grades, both sectors); the R-128 mirror pair is ONE ray at snapshot level ⇒ diagonal bilinears σ-blind; the linear defect-vacuum pairing ⟨vac~I₄Ψ⟩ is nonzero and σ-ODD (reviewer's engine finding, banked) and is excluded by the NAMED sign-gauge premise (Ω(−R) = Ω(R) exact + R-020 rays) ⇒ any up/down-splitting µΨ₀ coupling must engage the spatial winding topology; §D.4.4's ρ_L boundary term (R-110) is the standing candidate seat, pointed to not confirmed | DERIVED-A (channel rule; blindness facts; linear-channel facts; Ω sign gauge) + DERIVED-CONDITIONAL (the elimination, on the named sign-gauge premise) + FRAMING (ρ_L candidate seat; Skyrmion-degree anchor for σ) | i4_condensate_ideal_channel_rule | B.3.1 vicinity (+ ledger N38) | R-128, R-020, R-110 | — | Banked 2026-07-02 (twt-reviewer OVER-CLAIM→5 fixes→consensus; the reviewer's linear-channel finding is itself banked as a check). Sharpens the 2b mechanism row: the µΨ₀ coupling construction = the §D.4.4 boundary integral on an explicit profile (P2-7-class). R-128's ℤ₂ seat clarified same pass (snapshot collapse; distinctness anchored by spatial topological degree). |
| R-130 | Residue (ii) (H1) localization half DISCHARGED into the defect's own finite-norm existence: the R-125 phase mode's defect-excess is EXACTLY as localized as the defect — pointwise `N(exc) = ½N(R₀−1)`, τ₅-free ⇒ mode-L² ⟺ defect-L² (factor ½ exact); the raw mode is provably non-normalizable (constant norm ½ everywhere); the carrier subtraction is UNIQUELY forced (asymptotic residual `\|sin((ω−ω_c)τ₅/4)\|` ⇒ ω_c = ω — R-125's vacuum-relative subtlety DERIVED as a dichotomy, not assumed); hedgehog criterion `‖R₀−1‖² = 4sin²(F/4)` (n̂-independent; half-angle convention) ⇒ normalizable iff tail p > 3/2; static drive→0 face (§C.1.1 BVP): exterior Euler equation, indicial roots {−2, 1} ⇒ r^−2 tail — criterion met with margin | DERIVED-A (facts F1–F5 + static-face indicial exponent; isometries exact for SIMPLE unit bivectors — reviewer probe: non-simple fails, both physical axes simple) + DERIVED-CONDITIONAL (the (H1) closure, on named (C2) inherited + (T) tail + (N) norm equivalence) + FRAMING (below-continuum reading of (T-kernel) as the (H2) bridge) | phase_mode_excess_inherits_defect_localization | D.4.6 | R-125, R-126, R-127, R-123 | — | Banked 2026-07-02 (twt-reviewer HOLDS + 2 required wording fixes + 2 recommended annotations applied; F4/F5 symbolically re-proved by reviewer). Residue (ii) narrows to (H2) + (T-kernel) — a genuine open pair, (T-kernel) not minimized under (H2). New falsifier face: a banked kernel tail slower than r^−3/2 strips m = k₄ of its discrete carrier. |
| R-131 | Residue (ii) (H2) QUANTIZATION-STEP skeleton: the phase modulus (the finite orbit of R-125's mode generator) is COMPACT — rotor period 4π, `θ+2π ⇒ −R`, Ω sign-blind (R-129 gauge) ⇒ physical ray-orbit a closed 2π circle — so the conjugate charge is DISCRETE (given (Q)); and the tower's leading spacing is EXACTLY ω: on the ansatz `Ω_τ₅ = R₀~(ûω/2)R₀` (τ₅-free, linear in ω) and `Ω_i` ω-free ⇒ any Ω-built action reduces to `L(ω, shape)`; relative equilibria are shape-stationary and along the family `dE/dN = ω` exactly — the envelope identity engine-proved symbolically for FULLY GENERIC `L(ω, shape)` (kernel-form-free), δ-independent across all charge-lattice sectors. First quantized phase excitation carries the same front label `k₄ = ω/c_meta` (inherited from R-125) that R-017 consumes | DERIVED-A (A1/A2 reduction; compactness/orbit facts; the universal envelope factorization) + DERIVED-via-symmetry-CONDITIONAL (`dE/dN = ω` on the family; named (C1) conservative-sector shift symmetry + (C2′) relative-equilibrium family) + DERIVED-given-(Q) (discreteness; corpus-standard collective-quantization premise; lattice menu {0,½} rides on rotor-double-cover single-valuedness — reviewer fix) + FRAMING (moduli↔KG-pole identification; Planck-form remark) | defect_phase_modulus_charge_tower_spacing | D.4.6 | R-125, R-123, R-127, R-129, R-130 | — | Banked 2026-07-03 (twt-reviewer HOLDS + 1 required θ-angle-conditionality fix + 3 recommended annotations applied; reviewer proved the envelope identity MORE generally than claimed and the upgrade is banked). ℤ vs ℤ+½ lattice = FR-family selection, NAMED not decided (fork-neutral; spacing δ-independent); P2-4's induced level becomes a free cross-check. Remaining (H2) core: pole uniqueness + moduli↔pole identification. With R-130: residue (ii) = (H2-uniqueness/identification) + (T-kernel). |
| R-132 | R-126's boost/moving-family handle FIRED: the finite Lorentz-boost orbit of the rest one-particle label, computed INSIDE Cl(4,0) via the γ-embedding — `B_ζ = exp(ζeⱼ/2)` hyperbolic (because `eⱼ² = +1`; the observer's boost bivector `γ⁰γʲ = eⱼ` is a substrate VECTOR — the iso not grade-preserving at the boost planes), exact rapidity addition, vector action `Bγ⁰B⁻¹ = cosh ζ γ⁰ − sinh ζ γʲ`; rest label `mγ⁰` (`m = ω/c_meta`, R-123) ⇒ `(E,p) = m(cosh ζ, sinh ζ)`, `E² − p² = m²` EXACT (algebraic + componentwise; generic directions; boost∘rotation) ⇒ chain (2) dispersion's KINEMATIC second route, independent of R-017's dynamical KG route (route-level over-determination over shared foundations). REVERSION HAZARD banked: `B̃ = B ≠ B⁻¹`, the corpus `R·x·R̃` sandwich is a silent NO-OP here (`Bγ⁰B = γ⁰` exact) — use `B·x·B⁻¹` (= the Cl(1,3)-reversion sandwich through the iso). Caveat defused side-by-side: `e₁₄` rotation circular (`E = m cos θ`), `e₁` boost hyperbolic — `e_i4_squares_to_minus_one` intact, scope-annotated | DERIVED-A (orbit algebra, grade-shift fact, shell invariance, reversion hazard, caveat defusal) + DERIVED implied-by-banked (the dispersion second angle; NAMED (P) substrate-realization premise, R-039 class as in R-124, + (I) inherited residue-(ii) remainder) + imported group theory (orbit transitivity, cited like Schur) | boost_orbit_rest_label_mass_shell | B.2.2 (+ §D.4.6 R-126 handle-fired note) | R-013, R-014, R-123, R-039, R-126 | — | Banked 2026-07-03 (twt-reviewer HOLDS + 1 required reversion-hazard annotation + 3 recommended fixes applied; the no-op hazard is the reviewer's own engine finding, banked as a check). B is NOT a Cl(4,0) rotor (mixed parity, not Spin(4)) — the even Cl(1,3) rotor through the embedding. Falsifier alignment: an off-shell moving defect would break (P), which WP-LV1 protection predicts cannot happen. Named next: the wave-level (x₄-profile) orbit reading would hand chain (5) the same second angle. |
| R-133 | The rotational-band baryon mass equation `M(J) = M₀ + J(J+1)/(2Θ₀)` with BOTH coefficients from the exact hedgehog BVP: `M₀ = 36.46 f_π/e` (validates the banked 36.47; Derrick virial `E2 = E4` < 0.1%) and `Θ₀ = 106.76/(e³f_π)` — **CORRECTING the long-banked 97.27** (= `36.47·8/3 = 97.253` to within 0.02%, provenance suspect; exact `Λ = 50.98` matches the ANW literature ~50.9, and the truncated-grid route reproduces how a spurious ~97 arises). At the counted ANW couplings: `M_N = 936.4` (−0.3%), `M_Δ = 1229.8` (−0.2%), split `293.4` (+0.1%) — the banked M₀'s "8% ANW deficit" EXPLAINED as the missing band term. Knock-ons swept: `1/Θ₀` 214.7→195.6 MeV; R-111 Λ_QCD candidate 215→196 (in-range; scheme-dependent whether closer); top exclusion 6.5→7.2 (STRENGTHENED); `Σ_c−Λ_c` 171 (2.4%)→151.9 (−9.0%) — NEW TRACKED RESIDUAL (the old agreement rode the wrong constant); `Σ_b−Λ_b` 201→181.9 (−4.8%, improved) | DERIVED dressed-level (§D.4.3 branch-(c) conditional, as R-051) + DERIVED-given-(Q)+FR-selection (J = ½, 3/2 — the FR fermionic SELECTION, W-LIVE-4 fork untouched) + CORRECTION (THETA0_COEFF swept corpus-wide) + R-131-class band instance (spin/isospin moduli, distinct from the U(1) phase tower) | skyrmion_rotational_band_nucleon_delta | C.1.2 (+ D.4.5 correction, C.5.9/E.3 numbers) | R-051, R-131, R-130, R-111, R-091a | — | Banked 2026-07-03. HONESTY: `f_π, e` were historically FITTED to N/Δ (ANW) — pipeline consistency, not a new prediction; no new parameter. Candidate resolution of the c-leg residual: bound-state-class inertia ≠ rigid-rotor Θ₀ (P2-7-adjacent). Would change if: pion-mass-term BVP shifts the pair *(fired 2026-07-03, adjudicated by R-137/R-138: the pair shifts only in the massive scheme — 37.90/70.20, a second distinct scheme axis; refit executed at R-138, baseline stays massless, banked coefficients unchanged; Θ₀-downstream numbers — Λ_QCD candidate, top exclusion, Σ_c−Λ_c residual — fork-invariant per R-138's `1/Θ₀ = (2/3)·split = 195.4 MeV`)*; P2-4 decides FR. |
| R-134 | Brannen-scale ↔ nucleon-third convergence: `μ² = 313.84 MeV` vs `m_N/3 = 312.97 MeV` — 0.28% with ZERO parameters; amplitude form `√(m_N/3)/μ = 0.9986` (0.14% — the SAME single convergence, √ halves the deviation) — the baryon per-rotor amplitude = the lepton tower's DEMOCRATIC component (the generation-blind `μ·1`; ℤ₃ offsets average out). Legal reading: `m_N/3` = mean per-rotor frequency of the `Ω_B = Σω` lock (itself DERIVED-conditional, E-channel premise), NOT a quark mass (canon §5 intact). Look-elsewhere scan banked: 4 comparators × rationals p/q ≤ 8 at 0.5% → EXACTLY two hits (m_N/3 at 1/1; the fit-tied 8/5 of 1/Θ₀ — same hit via the N/Δ fit). FLOOR reading (`M₀/3 = 287.7`) does NOT converge (~9%) — the convergence stakes the full-mass side of the freq-sum-vs-full-mass fork. Specific to `m_N/3` (not `f_π`, not `1/Θ₀`) | CANDIDATE (zero-parameter cross-sector convergence, recorded per canon §0a; observation literature-known in the Koide circle, imported as such; post-hoc/look-elsewhere caveat named) + FRAMING (per-rotor lock reading; democratic-axis reading) + engine-checked arithmetic on INPUTs | brannen_scale_nucleon_third_convergence | C.3.11 | R-064–R-066 (Brannen), R-051, N12, cogear lock | — | Banked 2026-07-03 (coordinator question). Naive `I₄` derivation route BLOCKED by N12 (amplitude-blind Hodge map) — mechanism must be cell-scale/kernel class. Would become a RESULT if a P2-1/P2-5-class mechanism pins the per-rotor lock frequency to the lepton democratic component ⇒ `m_N = 3μ²` co-derives the nucleon mass from the lepton tower (one fewer counted INPUT dial; 2b table row). Would weaken if the E-floor bridge resolves the lock to the floor reading. |
| R-135 | P2-7 first half — nuclear binding exists classically: the `B = 2` rational-map configuration (`R(z) = z²`; the reduction to the radial BVP is the EXACT 3D energy — angular content enters only via the computed `I(z²) = 5.8083` and the exact degree identity `(1/4π)∫ψ² = B = 2`, certified <1e-10) has energy `71.543 f_π/e < 2×36.462 = 72.923` — **strictly below the two-defect threshold, margin 1.89%** (numerical error ~1e-5; independently re-solved by the reviewer with different window/domain/tolerances to 4e-5 agreement) ⇒ the `B = 2` channel is classically BOUND (strict sub-additivity), attraction SIGN predicted, magnitude NOT claimed. At the counted ANW couplings: binding ≥ 32.7 MeV vs observed 2.22 MeV — classical overbinding honestly imported (known massless-Skyrme character; quantization + pion mass = named follow-ups). Indicial generalization `s²+s−2B = 0` of R-130's `{+1,−2}` (`B = 2`: `(−1±√17)/2`, non-integer origin exponent, steeper tail — no long-tail matching problem). Certificates: Derrick virial ~3e-6 both profiles; `B = 1` regression to the banked 36.46; per-baryon 1.2081·12π² (HMS 1.208 corroboration, not load-bearing) | DERIVED dressed-level VARIATIONAL (below-threshold inequality; branch-(c) conditional as R-051/R-133; conclusion ansatz-independent GIVEN the inherited hedgehog-minimality premise — reviewer fix F1; value = upper bound only) + DERIVED-A (indicial generalization; degree identity) + FRAMING (deuteron identification `J^π = 1⁺` awaits `B = 2` collective quantization — classical SEAT only) | multi_skyrmion_b2_classical_binding | C.1.2 (+ E.3 SC-1 row note) | R-051, R-133, R-130 | — | Banked 2026-07-03 (twt-reviewer HOLDS + 2 required fixes F1/F2 + 3 annotations R1–R3 applied; the reviewer's clean-room re-solve and the B=1-origin marginality sympy fact are recorded in the docstring). First SC-1 `N = 2` datum, scoped: reduced-BVP + variational existence, NOT full 3D well-posedness. NOT done: tensor force from D4 anisotropy (P2-7 second half); `B = 2` quantization (the 2.22 MeV face); pion-mass BVP; Callan-Klebanov bound-state inertia (the R-133 `Σ_c−Λ_c` residual adjudicator — adjacent, distinct). Would change if: pion-mass BVP shifts the pair (re-check margin — *DISCHARGED 2026-07-03 by R-137/R-138: the margin survives across the entire fork — 1.96% at the probe couplings, 1.87% at the refit couplings; non-monotonic in μ*); full-field torus computation (deepens, never un-binds) — *FIRED 2026-07-05 (R-144): the full-3D ansatz-free flow keeps the binding, deepening at N = 96 same-grid (stall-vs-stall 3.06%, ≥ 2.95% after the reviewer's B1-side probe; the toroidal minimizer) — as predicted*. |
| R-136 | P2-7 quantization face — the quantized axial `B = 2` sector's ground state has EXACTLY the deuteron's quantum numbers: the `z²` map symmetries (engine-symbolic; axial iso-lock ⇒ `L₃ + 2K₃ = 0`) + FR loop signs (Krusch homotopy formula: S2 loop `N = 2` → +1, mixed S3 loop `N = 1` → −1) give the `K₃ = 0` tower rule **`I + J` ODD** — `(0,1) = J^π = 1⁺, I = 0` THE DEUTERON (parity from the derived internal parity map `R_P = −R`, anchored to nucleon `+`; `\|K₃\| ≥ 1` towers provably higher), scalar `(0,0)` dibaryon TOPOLOGICALLY FORBIDDEN, `(1,0)` np-singlet ~40 MeV up at ansatz level (`V_⊥ = 312.5 > U_⊥ = 194.6`; certificates: four-way `B = 1` regression to R-133's 106.76, `V₃₃ = 4U₃₃` exact, `W_⊥ = 0` block-diagonality < 1e-14 — the reviewer's probe banked; S2's +1 doubles as the axial no-anomaly certificate). FORK FACE: bosonic branch flips to `I + J` EVEN (bound scalar ground state) — empirically refuted ⇒ SECOND independent anchor for the fermionic FR selection (independent data, shared (Q) premise) | DERIVED-A (map symmetries; parity MAP identity; `V₃₃ = 4U₃₃`; `W_⊥ = 0`; factorization via hedgehog reduction = R-133) + IMPORTED-AS-CITED (Krusch formula, consistency-checked; mod-2-weak composition asserts noted — the S2 loop is the form discriminator) + DERIVED-given-(Q)+FR-selection (rule + quantum numbers incl. state-level parity; W-LIVE-4/N35 fork UNTOUCHED) + ANSATZ-LEVEL (ordering; torus corroboration cited not banked) + FRAMING/ESTIMATE (MeV spectrum; rigid-rotor overbinding stated). **Headline physics LITERATURE-KNOWN** (Braaten–Carson 1988; Leese–Manton–Schroers 1995; Krusch 2003 — to-be-verified citations, R-134 precedent); new content = tiering + certificated moments + fork-face bookkeeping | b2_axial_quantization_deuteron_ground_state | C.1.2 (+ B.3.5 anchor note) | R-135, R-133, R-025, N35 | — | Banked 2026-07-03 (twt-reviewer HOLDS + 3 required fixes + 5 recommendations applied; the reviewer's `W_⊥ = 0` probe and the Krusch-form discrimination via the S2 loop are recorded). Upgrades the deuteron identification from R-135's FRAMING to the quantum-number level; binding VALUE still open. NOT done: `\|K₃\| ≥ 1` allowed sets; tensor force/D4 (P2-7 remaining half); pion mass; torus moments; Callan–Klebanov inertia. Would change if: P2-4's induced level lands EVEN (anchor becomes a standing tension); torus flips `V_⊥` vs `U_⊥` (literature: no); pion-mass BVP shifts moments *(pion-mass face DISCHARGED: R-137 — the topological selection is mass-untouched; R-138 — the massive-branch moment-ordering re-check done, `V_⊥ = 222.1 > U_⊥ = 135.6`, deuteron stays the ground state in-branch)*. |
| R-137 | Pion-mass robustness re-check (the R-133/R-135/R-136 owed face, DISCHARGED for existence/sign): deforming by the standard chiral-breaking term `(μ²/4)x²(1−cosF)` at the physical `m_π = 138` (isospin-averaged; `μ = m_π/(e·f_π) = 0.196`; normalization re-derived against the banked conventions — canonical-pion check `−½m_π²π²` exact) leaves the R-135 inequality intact and marginally STRONGER: `74.31 < 2×37.90 = 75.80`, margin **1.96% vs massless 1.89% (widens; assert-backed > 0.0189)**, binding ≥ 35.2 MeV. Certificates: mass-extended Derrick `E2 + 3E_m = E4` (~3–5e-6 both profiles); Bessel tail `x^(−1/2)K_ν(μx)`, `ν = √(2B+¼)`, with the DERIVED-A identity `√(2B+¼)+½ = (1+√(1+8B))/2` (μ→0 reproduces the massless exponents exactly); margin stable to 4 decimals under window/xmax/bracket variation (reviewer probe). THE INERTIA FACE: massive-profile `Λ = 33.52` vs massless `50.98` (θ-coeff `106.76 → 70.20`, −34%) ⇒ the massless `N/Δ` closure does NOT transfer at fixed couplings (reviewer hand-check: `M_N ≈ 1009`, split ≈ 446 — fails) ⇒ the massive variant is a SECOND, DISTINCT scheme axis alongside §C.1.2's local/phason fork (object-dependent: masses +3.9%, inertia −34%); refit fork NAMED, not taken; banked baseline stays massless | DERIVED dressed-level VARIATIONAL ROBUSTNESS (branch-(c) conditional; hedgehog-minimality premise EXTENDED to the massive functional — same class, different functional) + DERIVED-A (Bessel-index identity; mass-extended Derrick) + NAMED IMPORT (`m_π` witness, probe-only, both sides identically — not a counted dial; `(1−cosF)` form = imported chiral-breaking deformation, not a banked substrate term) + LOCATED (massive-scheme refit fork named, not taken) | massive_pion_bvp_binding_margin_robust | C.1.2 (R-137 passage) | R-135, R-136, R-133, R-051 | — | Banked 2026-07-03 (twt-reviewer HOLDS + 3 required fixes + 2 recommendations applied; normalization/Derrick/Bessel spine independently re-derived by the reviewer; widen-claim tightened to assert-backed). Would change if: the massive-scheme refit is banked (re-anchor all massive numbers, re-check margin at refit couplings — literature keeps B=2 bound there, imported not banked); a substrate derivation of the chiral-breaking term lands (probe → sector). *Refit face FIRED at R-138 same day: margin at refit couplings 1.87% — survives; the margin is non-monotonic in μ (1.89/1.96/1.87), so the widening is probe-point-specific.* |
| R-138 | Massive-scheme refit branch, executed + adjudicated (coordinator-approved fork execution): self-consistent 2D fit lands at `f_π* = 108.26 MeV`, `e* = 4.8427` (`μ* = 0.2632`; corroborates Adkins–Nappi 1984's 108/4.84 — citation to-be-verified; reviewer re-derived the point by a different algorithm from two bracketing starts, unique to 4e-6), `N/Δ` closed. FIT-INVARIANCE (DERIVED-A given the band form + J-assignment): `1/Θ₀ = (2/3)·split = 195.4 MeV` in any exact-closure scheme ⇒ Λ_QCD candidate, top exclusion, AND the `Σ_c−Λ_c` residual all fork-INVARIANT — "scheme artifact" eliminated; weight redistributes to BOTH R-133 candidates (CK-class inertia; `hf_c` re-fit). OWED RE-CHECKS at refit couplings: margin 1.87% (75.997 < 77.442, binding ≥ 32.3 MeV — the binding conclusion verified across the ENTIRE fork {μ = 0, 0.196, 0.263}, no fourth corner: the massless margin is coupling-independent; margin non-monotonic in μ, banked); ordering `V_⊥ = 222.1 > U_⊥ = 135.6` (deuteron stays ground state in-branch). BASELINE DECISION (bookkeeping, not derivation): **massless stays** — D1 parameter economy (2 vs 3 counted inputs; the third buys the physical pion tail), D2 hedged convergence-preservation (two-route × two-scheme grid: only sub-2% entry is massless-`√18`, hedge carried; sign flips on the `√12` route), D4 import-minimization (the `(1−cosF)` form is a load-bearing underived import in-branch) | FIT in-branch (same 2 dials; branch counts 3 inputs — `m_π` load-bearing; the `(1−cosF)` FORM a load-bearing structural import in-branch) + DERIVED-A (Θ₀ fit-invariance, band-form + (Q)+FR-conditional) + DERIVED variational robustness (margin + ordering at refit couplings; branch-(c) + extended hedgehog-minimality conditionals) + SCHEME DECISION (bookkeeping entry) | massive_scheme_refit_branch | C.1.2 (R-138 passage) | R-137, R-136, R-135, R-133, R-111, R-091a | — | Banked 2026-07-03 (twt-reviewer HOLDS on every number + 5 required fixes F1–F5 + 6 recommendations applied — F1 √18-hedge carried, F2 decision-grounding reworded, F3 both `Σ_c−Λ_c` candidates restored, F4 in-branch form-import restated, F5 sweep executed; `D/J` wired to `DoverJ_from_lepton_masses()`). Would change if: substrate chiral-breaking derivation lands (D1/D4 dissolve, fork re-opens on D2); the D/J calibration moves; a P2-5-class cell-scale derivation pins `e·f_π` from the substrate. |
| R-139 | P2-7 tensor-force face + item close-out: the asymptotic Skyrmion is an exact TRIPLET OF ORTHOGONAL PION DIPOLES `π_a = −C∂_aY` (at `B = 1` the Bessel index `ν = 3/2` makes the massive tail elementarily the dipole-Yukawa profile `(1+μr)e^{−μr}/r²` — sympy identity), so the two-defect asymptotic interaction is `V(R,O) = πC²[(3O_RR−TrO)(1+μR+μ²R²/3) + TrO·μ²R²/3]e^{−μR}/R³` — the OPE central+TENSOR radial structure EXACT (central `∝ μ²` vanishes massless = the aligned-channel zero). Dipole strength nearly FORK-INVARIANT, all solved in-primitive: `C = 8.634/7.91/7.66` (massless/probe/refit; **the drafted refit 4.24 was REFUTED by the reviewer** — a provenance misread of R-137's B=2-at-probe constant; fix F1). Sign/magnitude pinned by the GRID, not convention (source-vs-field-energy bookkeeping ambiguity named): 169³ development record — aligned channel vanishes (+0.34/+0.068/+0.005/−0.013), ∥ π-rotation REPULSIVE (ratios 0.81→0.92), ⊥ π-rotation ATTRACTIVE (0.66→0.83; the R-135 binding channel), channel ratio → 2.2 vs exact 2; reviewer systematics probe banked (Richardson → ~0.9–1.0) — magnitude scoped 10–20% raw, residual = named grid systematics; 81³ in-suite regression | DERIVED-A (K_{3/2} elementary; dipole identity; OPE decomposition + μ→0 limits) + DERIVED dressed-level ASYMPTOTIC (the law; product-ansatz class, branch-(c) conditional) + GRID-CERTIFICATED scoped + CORRECTED PREMISE-DRIFT (N39: the "from D4 anisotropy" worklist phrasing was drift — `eta_DM` always said dominant tensor = OPE; the `η_DM = (D/J)²/144` CALIBRATED face preserved as the P2-5-gated subleading row; `eta_DM` docstring garble fixed same pass) + NAMED FOLLOW-UP (nucleon-state projection → quantum OPE strength). **Headline physics LITERATURE-KNOWN** (Skyrme; Jackson–Jackson–Pasquier 1985; Manton–Sutcliffe — to-be-verified citations); new content = in-framework derivation from banked tails + fork-resolved constants + certificates + the drift correction | two_defect_asymptotic_tensor_force | C.1.2 (R-139 passage) | R-135, R-137, R-138, R-133, R-086 (eta_DM) | — | Banked 2026-07-03 (twt-reviewer HOLDS on law/identities/grid + REFUTED on the drafted refit constant + MISLABELED on the premise framing — all 5 required fixes applied; the reviewer's independent 169³ reproduction, refit-tail solve 0.8251, and systematics probe recorded). **P2-7 CLOSED AT SCOPE** (R-135–R-139 + first SC-1 N=2 datum). LOCATED residual: binding magnitude ~113/~124 MeV (massless/refit) rigid-rotor overbinding — needs torus + beyond-rigid-rotor quantization. Adjacent rows: CK inertia (`Σ_c−Λ_c`); OPE-projection strength face; `η_DM` 1/144 (P2-5-gated). |
| R-140 | P2-4 leg 2 structural core — the explicit DM-twisted D4 plaquette holonomy: minimal curvature-carrying loops = the 32 triangles (8 spatial, trivial; **24 two-`e₄`-bond, ALL non-trivial** — pure-gauge lift EXPLICIT; the 36 chordless 4-cycles all carry trivial holonomy — reviewer probe banked as a check; the `e₄`-triangles engage ONLY the banked 48 non-commuting pairs); exact law `W = cos²θ + sinθcosθ(B̂₁+B̂₂) + sin²θ·e_ab` in the canonical lattice frame (invariant content: the chiral angle `arccos(cos²θ_D)` + non-triviality); the abelianized rotor has NO L-grade content while W's L-grade is exactly `sin²θ` — the 48/66 commutator content as the holonomy's non-abelian signature; consistency forces the orientation-ODD convention (= physical DM antisymmetry; convention-robust); **chiral factorization `W = W₊P₊ + W₋P₋` with IDENTICAL angles — the DM plaquette is chirally BLIND** (weak-sector chirality NOT sourced here; "weak = SD" stays the banked INPUT bit; §C.4.6(iii) qualifier added); per-sector Lie closure = FULL su(2)± (rank 3) ⇒ the `π₃(U(1)) = 0` instanton obstruction ABSENT at structure-group level | DERIVED-A (census incl. 4-cycle triviality; exact law; forced odd convention; chiral factorization + closed-form angle; non-abelian signature; per-sector rank 3) + DERIVED-structural (instanton obstruction-absence) + FRAMING preserved (dynamical YM — kernel-gated as banked; NO value claimed) + HONEST CONSTRAINT (chirally symmetric plaquette) | d4_dm_plaquette_holonomy_explicit | C.4.6(ii)-(iii) | R-103, D4_DM_bond_bivectors_non_commuting, R-088, N35 | — | Banked 2026-07-03 (twt-reviewer HOLDS + 5 wording/record fixes; reviewer's chordless-4-cycle probe banked). P2-4: leg 1 banked + leg 2 CORE DONE + leg 3 half-banked + leg 4 ANSWERED-AT-PARITY same day (R-141); leg 3 STRUCTURAL CORE DONE 2026-07-04 (R-143). |
| R-141 | P2-4 leg 4, the W-LIVE-4 decider, answered at the PARITY level: the induced topological term on the `B = 1` baryon worldline is the `π₄(SU(2)) = ℤ₂` class (no integer WZW for SU(2), consistent with the banked L3 refutation) with weight `(−1)^N`; N assembles from BANKED facts — roster 4 doublets/gen (evenness = the banked SU(2) gaugeability, same roster); baryon-coupled subset = the 3 colour modes/gen (lepton EXCLUDED by the one L/Q sector assignment seen in two banked faces — R-002 winding split + R-127/R-128 lock split — plus a third independent face: the single-Weyl neutrino cannot complete a chirally-linked determinant unit); counting unit fixed (one chirally-linked doublet pair per colour facet; `(u,d)` = R-128 σ-mirror components, QCD's own anchor N_c = 3 not 6); EVEN variants adversarially enumerated and each excluded (4/12 lepton-in; 6/18 double-counting; N = 0 = the P1b-refusal revert branch, not an established zero) ⇒ **N ∈ {3, 9} under the named generation fork — ODD in both branches ⇒ weight −1 ⇒ FERMIONIC SKYRMION QUANTIZATION INDUCED** | DERIVED-given-(P1)+(P1b)+(Q) (the parity; P1b = a FRESH CANDIDATE-class channel-identification premise — the one genuine vulnerability, named and revocable, inheriting R-127/R-128's ansatz conditions) + IMPORTED-AS-CITED (P1: D'Hoker–Farhi 1984 (NPB 248) / Witten 1982 (PLB 117), to-be-verified; R-088-class at the parity/mod-2-index level) + DERIVED (roster census, banked) + DERIVED-given-P1b (coupled-subset selection) + NAMED FORK parity-robust (3 vs 9) | induced_level_parity_on_baryon_worldline | C.4.6 (+ B.3.5 upgrade paragraph) | R-002, R-088, R-127, R-128, R-140, N35, §C.4.6(i) | — | Banked 2026-07-03 (twt-reviewer HOLDS at the conditional tier + 6 required fixes + 3 recommendations; no joint refuted — the reviewer verified the π₄ carrier, the (−1)^N form, the A.5.2 fibration split, and the R-127/R-128 channel facts in source; its even-variant enumeration (6/18) banked in the excluded table). W-LIVE-4's W1: **CLOSED-CONDITIONAL(P1+P1b+Q), POSITIVE**; N35 (a) PARTIALLY discharged at parity level (substrate computation face open); both anchors become consistency checks. **P1b is SPLIT by R-161**: its structural half (the channel identity, winding-assignment-relative) is now exact `Cl(4,0)` algebra given C1′–C4′; only P1b-DYN (the mode determinant actually generating the term) remains CANDIDATE. Would change if: P1b-DYN refuted (revert; anchors stand); mode determinant substrate-derived (P1 discharges); generation fork decided (parity unchanged); roster changes. |
| R-142 | WP-MASS-MEASURE residue (ii), the (H2) core, answered at the structural level: (identification, LABEL half CLOSED) the CLOCK-ORBIT IDENTITY `exp(ûθ/2)R*(x,τ₅) = R*(x,τ₅+θ/ω)` — exact, engine, generic config AND the quark axis `I₄B_q` — makes the observer's R-127 channel phase and R-131's phase modulus ONE U(1) (integrated form of R-125's fact 2a; NEW content = the same-U(1) bookkeeping killing the different-circle gap) ⇒ the channel pole's LABEL = the `ΔN = 1` tower step = ω exactly (R-131 cited live) → `k₄ = ω/c_meta` (R-123(i)); degeneracy carried by the R-126 moduli (overlap caveat inherited, no dimension citable); the ABSOLUTE tower-to-vacuum anchoring = a NAMED face (R-007 ontology + kernel-gated) — R-131's FRAMING PARTIALLY discharged; (uniqueness) the pole = the winding-1 sector GROUND STATE — every sector state ≥ M given (S)+(M) in the (Q)-semiclassical description (the ≥ M bound rides (M)+(Q) alone; classical sidebands ω−ν are not states); **(S)-static ENGINE-CERTIFIED in the breathing channel**: ℓ=0 Hessian strictly positive (form-eigenvalue ~0.21, resolution-robust, box-SATURATING 0.2171→0.2078 at boxes 24→80, core-localized below the B_eff(∞)=¼ floor) | DERIVED-A (clock-orbit identity + same-U(1) bookkeeping) + ENGINE-CERTIFIED-numerical ((S)-static breathing-channel bound; NOT DERIVED-A) + DERIVED-given-(Q)+(S)+(M) with (C1)/(C2') + R-127-locks inherited + LOCATED (residue (ii) → kernel faces (S/M/T-kernel) + anchoring face + ω≠0 co-rotating face; no structural face OUTSIDE the named premise set) | one_particle_pole_moduli_identification | D.4.6 (+ B.2.1 status note) | R-123, R-125, R-126, R-127, R-130, R-131, R-007 | — | Banked 2026-07-04 (twt-reviewer HOLDS on the core + OVER-CLAIM fixes F1–F8 — incl. a VACUOUS harness check caught (operator precedence; suite-dead-check class), the label-vs-anchoring split, the breathing-channel scoping, the (M)-premise honesty; reviewer's box-saturation probe recorded). Falsifiers: kernel spectrum with a sub-ω channel pole kills `m = k₄`; any sub-mass excitation in a one-particle channel (none observed — consistency anchor). Would change if: kernel spectrum computed; a negative/zero ℓ=0 mode at finer analysis; P2-4/R-141 decides the FR-family lattice. |
| R-143 | P2-4 leg 3 structural core — lattice-instanton access + DM background neutrality: the DM background carries **EXACTLY ZERO site-based topological density in each chiral sector at all θ_D** (ι-mechanism: the twist plane `r∧e₄` is e₄-reflection-BLIND while the 4-volume ε-pairing is e₄-reflection-ODD and ι is free ⇒ orbit-pair cancellation across the whole site-based density class — any holonomy-built Lie factor, any pseudoscalar pairing; 6912 individually O(1) terms, genuine cancellation; per-axis-class blocks vanish independently; variant-b also neutral by a SEPARATE numerical fact — not the ι-mechanism; genericity witness banked: a seeded-random homogeneous connection has Q₊ = +29.06/Q₋ = −62.48 — per-site neutrality NOT generic; generic parity would only give `q₊ = −q₋`); the D4 charge operator calibrates integer-EXACTLY as `Q_form(F) = 576·ε(F)` (pseudoscalar-pure; continuum norm 4π²; exactly gauge-invariant); an EXPLICIT compactly-supported SU(2)₊ singular-gauge winding-1 fluctuation over the background has exact SU(2)₋ transparency (`T_aP₋ = 0`), exactly-localized finite action excess (far-dev = 0.0), boundary map = the identity S³-map (banked π₃ degree 1), and measured charge → 1 (0.79/0.90/0.94 at ρ = 2/3/4, deficit ∝ 1/ρ²; in-suite regression 0.672); cross-term tensor in closed form `c(θ) = 4√2·a·sin²θ/sin a` (machine-exact across θ, reviewer sweep; third-θ pin banked) — the linear instanton–background coupling sourced by the 48/66 non-abelian excess, orientation-BLIND (no CP claim); located face: log(R) excess for uncut tails under the NAMED Wilson-class premise ⇒ compact support is the finite-action object; LATT-π₃ premise NAMED (strong-twist local reading not integer-faithful: 0.78 → 0.63 continuous in θ_D) | DERIVED-A (ι-mechanism; calibration identity; cross-term tensor + closed form; transparency/winding identities) + DERIVED-A-construction + CERTIFICATE (plateau → 1; dev record + in-suite regression) + LOCATED (linear-coupling face; Wilson-class premise named) + NAMED PREMISE (LATT-π₃) + FRAMING preserved (no minimizer/action value/size/rate — kernel-gated, R-140 fence inherited) | d4_lattice_instanton_access_and_dm_background_neutrality | C.4.6(iv) | R-088, R-103, R-140 | — | Banked 2026-07-04 (twt-reviewer HOLDS at the proposed tiers on all five claims + 4 record fixes F1–F4 applied; the reviewer's genericity attack PRODUCED the nonzero counter-example — banked as a check — and its θ-sweep verified the closed form to 1.8e-15; full dev record reproduced digit-for-digit). Leg 3 structurally closed; remaining face = instanton solution/action value (kernel-adjacent). R-088's ΔB = ΔL = N_gen selection rule now has its substrate carrier structurally in place (rate face gated). |
| R-144 | SC-1 second datum — the full-field, ansatz-FREE `B = 2` minimization of the banked dressed Skyrme static sector: the 3D functional certified as the banked sector (hedgehog reduction to R-135's `u/x²` = sympy identity on generic rays, in-suite; compact-profile discretization regression `h²`-convergent at N = 48→96 for both the hedgehog and the `z²` map); charge-conserving flow (SGD + exact Derrick rescaling, every step variational; charge-guard `\|ΔB\| < 0.04`) with no symmetry CONSTRAINT during descent stalls BELOW the two-defect threshold at matched grid — **stall-vs-stall margins 1.79% (N=64) / 3.06% (N=96, 30k-step continuation; E = 71.6169, virial 0.990, B_disc = −1.98198), ≥ 2.95% after the reviewer's B1-side continuation probe (banked; both stalls are upper bounds — "descent only deepens" was one-sided, reviewer-corrected F1; sign independently protected by the continuum anchor 72.923 > 71.617)** vs R-135's ansatz-reduced 1.89%; the minimizer found is the TOROIDAL B = 2 (ring r = 1.553, center 2.1% of max, sharpening; axial-init + cubic-grid qualifier banked, F2 — corroborative); R-135's would-change-if (c) FIRED (KEEPS the binding, deepening at N = 96); B = 1 regression N=96 machine-virial 1.00004, +1.3% of the banked 36.462 (same-grid comparisons the honest ones — the N=64 coincidence with the continuum is a recorded, understood cancellation). METHODOLOGY banked: lattice winding smooth-sector-protected only (two unwinding events, reproducible-on-demand incl. by the reviewer; charge-guard discipline load-bearing — the flow-level face of R-143's LATT-π₃ caveat); rigid fat-tail boundary artifact recorded (+12.6%), hence compact-support regression; margin values = stall-vs-stall records (rescale-free flows fake-stall at 6.8–7.3%), banked content = SIGN + ~3% order | DERIVED-A (reduction identity; h² regression) + DERIVED dressed-level VARIATIONAL full-field (below threshold; branch-(c)/hedgehog-minimality inherited from R-135) + STRUCTURE-corroborative (the torus) + SC-1-SECOND-DATUM scoped (STATIC face only; dynamical multi-defect EOM open, kernel-gated) + METHODOLOGY | full_field_b2_below_threshold_sc1_datum | C.1.2 (+ E.1.2/E.3 SC-1 rows) | R-135, R-133, R-120, R-050a, R-143 | — | Banked 2026-07-05 (twt-reviewer HOLDS at all five stated tiers + required fixes F1/F2 and recommendations F3–F5 applied; the reviewer independently re-measured all three saved fields digit-for-digit, ran its own B1-side continuation and unwinding-reproduction probes — both banked). SC-1 static face: two N = 2 data; remaining core = the dynamical multi-defect Cl(4,1) EOM (kernel-gated) + optional B ≥ 3 third datum. P2-7 magnitude residual SHARPENED: the classical full-field half done; remains beyond-rigid-rotor quantization + the massive full-field run. |
| R-145 | P2-2 structural half — the 6→4 frame reduction (first-order/Cartan face): the banked texture metric is EXACTLY a rank-4 frame square `g = δ + QᵀQ − PᵀP = Eᵀ κ E`, `E = [δ; Q; P]` (10×4, rank 4 ALWAYS — frame nondegeneracy, not metric nondegeneracy), `κ = diag(+1₇, −1₃)` (the 10 legs = the Janet–Cartan count as an ECHO only — legs not gradients, flat-frame factorization not an embedding); pointwise the grade-2 frame quadruple is FREE (`Ω_μ(0) = B_μ` coefficient-exact for exp-linear proper rotor fields); SIGNATURE-MENU theorem — `λ_max(g) ≥ 1` ALWAYS (the reviewer's stronger form of ≥1-spacelike, its adversarial optimizer floored at exactly 1; engine-asserted), negative index ≤ 3 ⇒ NONDEGENERATE menu `{(0,4),(1,3),(2,2),(3,1)}` with det g = 0 at transitions, **all-timelike (4,0) structurally excluded**, each item realized by an explicit proper rotor field; invariant Lorentzian threshold `‖P‖_op > 1` (necessary only; the family-free form of the banked θ₀ > 2 — NO perturbative texture is Lorentzian; light-cone birth at det g = 0); THE REDUCTION: signature (1,3) ⇒ canonical tetrad — `E = ι e`, `ιᵀκι = η` machine-exact, unique up to O(1,3) (tetrad-existence-per-metric already banked at texture_metric_vierbein — credited; NEW = the frame-level ι factorization + uniqueness + the ledger split) ⇒ the strategic map's "6→4 needs EOM" is SPLIT: the reduction is structural and selection-free, the EOM owes ONLY the signature pick; Maurer–Cartan FLATNESS `dΩ + Ω∧Ω = 0` SYMPY-EXACT (faithful Cl(4,0) rep, non-commuting family) + numeric generic MV field ⇒ both first-order variables (frame AND spin connection) from the ONE rotor field, Cartan structure equation automatic — the Gauss-equation face (Riem(g) from ∂E against flat Ω) = the NAMED next handle toward C_T (kernel-adjacent, not done); internal gauge action on the legs = compact SO(3)×SO(3) (`P → O_SDᵀP`, `Q → O_ASDᵀQ` — the map itself engine-asserted per reviewer F1; zero split leak; dets +1; g exactly invariant) ⇒ tetrad boosts NOT substrate-internal — local Lorentz emergent at the reduced description | DERIVED-A (extended-frame identity; pointwise freedom; gauge-action facts incl. the leg map; MC flatness sympy-exact + numeric) + DERIVED-structural (signature menu incl. (4,0) exclusion + λ_max ≥ 1; canonical reduction + O(1,3) uniqueness) + DERIVED necessary-condition (`‖P‖ > 1` threshold, convention-conditional on the banked c2 = +1; menu convention-ROBUST under c2-swap, reviewer-verified) + FRAMING (emergent-local-Lorentz reading, scope-guarded vs R-132 spacetime boosts; Janet–Cartan echo) + NOT-DERIVED (the (1,3) PICK — vacuum/EOM residue, named; menu vs pick) | texture_frame_6to4_reduction | B.6.6–B.6.7 | R-042, texture_metric_vierbein, equivalence_principle_protection | — | Banked 2026-07-05 (twt-reviewer HOLDS at ALL stated tiers + 3 required record fixes F1–F3 applied — F1 an engine-FALSE transpose in the claim-7 docstring, now the corrected map is asserted in-suite; F2 nondegenerate-menu qualifier; F3 prior-art credit — + recommendations R1 (λ_max ≥ 1 banked) / R2 (frame-vs-metric nondegeneracy clause) / R3 (this sync); the reviewer's own probes: 4000-frame sweep + Nelder–Mead (4,0) attack floored at exactly 1.0, c2-swap menu robustness, threshold necessity witness (0,4) at ‖P‖ = 2.07). Fence: no C_T, no absolute EH coefficient, no value (#1-gap as banked); U2 gauge-projection premise NOT discharged; the amplitude FRAMING sharpened (Lorentzian = finite-amplitude texture phase), not discharged. Would change if: vacuum EOM selects a non-(1,3) signature (kills the pick, not the menu); a substrate-internal tetrad boost is exhibited (kills the emergent-Lorentz reading); ~~the Gauss-equation face needs data beyond (E, Ω) (locates a first-order-scaffold gap)~~ **[FIRED-NEGATIVE 2026-07-05: R-149 executed the Gauss face — Riem(g) closes algebraically in (E, Ω, dE); no data beyond the scaffold needed]**. |
| R-146 | DM-V2-1 differential-coupling lead ADJUDICATED — clean structural negative + one located gap: the texture-metric source of ANY grade-2 excitation is IDENTICALLY its E·B-type L–Q cross term — `h(B_L,B_L) = h(B_Q,B_Q) = 0` exactly, `h(B,B) = 2⟨B_L I4 B_Q⟩₀` exactly (the banked P6 balanced-fact REWRITTEN in the EM basis; Hodge duality pairing a signed permutation ±1, engine-asserted incl. column-permutation per reviewer R1); `span(L)⊕span(Q)` = ALL of grade-2 (rank 6) ⇒ NO EM-orthogonal gravitating polarization; `\|h\| ≤ 2\|B_L\|\|B_Q\|` (Cauchy–Schwarz, saturated by pure SD/ASD — the maximally gravitating polarizations are exactly half-magnetic half-electric; gravity SD/ASD and EM L/Q splits maximally unbiased); `[SD_i,ASD_j] = 0` (all 9) while L/Q is not commutator-closed ⇒ no non-abelian rescue; COROLLARY: the transverse photon strain mode (E⊥B) is h-DARK at bilinear order; grade-3 doubly dead (A·T₃·B has NO even part — parity; the even substrate field can never produce grade-3 MC content ⇒ new-field scope gap, §E.1.3 posture REINFORCED); THE LOCATED GAP: the grade-0×grade-4 AMPLITUDE channel — a non-unit even excitation `a + c·I4` has MC form with ZERO grade-2 content yet `h = 2(aa′+cc′)(ac′+a′c)` (coefficient-exact); closed identically on unit rotors; DM-shaped (gapped Higgs-class) but DOUBLY conditional: #1-gap amplitude modes + the h-formula's grade-2-specific Schur scope | DERIVED-A (cross-term identity + pairing; rank-6; CS floor + unbiasedness + saturation; commutator facts; photon h-darkness; grade-3 parity kill + even closure) + DERIVED-structural NEGATIVE (no EM-polarization-dark gravitating excitation in the banked even unit-rotor content at the DIRECT-bilinear level — conditional on the photon-strain identification, U2, AND the open matter→h face of caveat (d), reviewer F1) + LOCATED-GAP/CANDIDATE (amplitude channel) | dm_differential_coupling_no_em_dark_texture | E.1.3 | R-042, R-145, photon_strain_mode, R-121/R-122 | — | Banked 2026-07-05 (developer-agent build + lead-session independent re-run + twt-reviewer HOLDS at all six tiers; F1 caveat-(d) rider + F2 same-pass sync + R1 permutation assert + R2 wording applied; the reviewer independently re-derived every identity with its own values incl. the amplitude-channel formula by hand). Includes the texture_metric_candidate SCOPE FIX (the "any even-grade field" over-generalization — engine-false for grade-0 MC content, reviewer-verified both directions). N40. Would change if: kernel amplitude modes; odd-grade content; U2 falls; the matter→h face resolves via indirect L–Q mixing (re-run). |
| R-147 | DM-V2-1 lead (ii) wave-train phase defects ADJUDICATED — clean negative; DM-V2-1's V2-era lead list EXHAUSTED: THE BLADE, NOT THE TOPOLOGY, FIXES h (a unit-amplitude phase defect `R = exp(B̂θ)`; topology fixes only ∮dθ; varying-blade defects still carry pure grade-2 MC — reviewer F1 probe) — blade table engine-exact (six coordinate bivectors h-null; SD/ASD ∓1; carrier blade `E = I4·e5` h-null, span{1,E} h-null even NON-unit); pure-L and E-phase dislocations h = 0 machine-exact (U2-conditional reading, c1-witness −0.64 nonzero, named); the ONLY gravitating dislocation (SD-blade chiral-ideal U(1)) has `h = −½dθ⊗dθ` EXACT with its ENTIRE h = the R-146 EM cross term POINTWISE (\|Ω_L\|/\|Ω_Q\| = 1) — topology buys no evasion; NO π₁ protection (π₁(Spin(4)) = 0, π₂ = π₀ = 0; `exp(e12π) = −1` exact; belt-trick unwinding homotopy engine-exact; negative survives the SO(4)/ℤ₂ OP fork — reviewer R1 probe) ⇒ nothing simultaneously gravitating, EM-dark, topologically protected (metastability cannot reopen DM — reviewer F2); KZ forms no dark network; SHARPENING: vortex cores naturally populate the R-146 amplitude channel (SD-core `Ω_r = s + sI4` automatic, h = 2sp digit-exact; balanced-blade core asserted I4-free) — but only EM-VISIBLE vortices force I4-core content ⇒ the single DM loophole carries TWO named EOM conditions | DERIVED-A (blade table; dislocation metrics; homotopy; core facts) + DERIVED-structural (π₁/π₂/π₀; KZ) + CONDITIONAL named (U2; the EM-visible cross-term reading inherited from R-146; E-phase-as-OP FRAMING, load-free) + CLEAN NEGATIVE | dm_wavetrain_phase_defect_negative | E.1.3 | R-146, R-123, R-042, R-145 | — | Banked 2026-07-05 (developer-agent build + lead-session re-run + twt-reviewer HOLDS at all tiers; F1 varying-blade generality + F2 topological-protection wording + F3 same-pass coverage + R1 π₂/π₀ + OP-fork robustness banked + R2 balanced-blade-core assert applied; the reviewer re-verified the belt trick on a denser 25×37 grid at 0.0). N41. Would change if: kernel EOM populates the amplitude channel from EM-dark cores (both named conditions); U2 falls. |
| R-148 | P2-3 sign face DECIDED-conditional-generic — `β₃ = μ d(1/e²)/dμ ≤ 0`, the AF-SIGNED branch; the wrong-sign risk for the qcd-UV arc REMOVED (conditional on I-13, revert clause named): machinery Weinberg-calibrated (series C24 = 1/48 ⇒ `M(π¹π² → π¹π²) = t/f²` exact); VERTEX SIGN DERIVED IN-SUITE (reviewer-forced correction): quartic-form coefficient +1 series-extracted at rational configurations + STATIC-ENERGY ANCHOR `E₄ > 0` tying the Minkowski Lagrangian sign `+(1/32e²)Tr([L,L][L^μ,L^ν])` to R-085's Hamiltonian-boundedness + slot = −1/4 COMPUTED; channel map `A_Skyrme(s,t,u) = −(s²/2 + tu)/(2e²f⁴)` (Bose s↔u; identical-cartesian channel identically zero) ⇒ POSITIVE forward weight `+1/(2f⁴)` — tree positivity SATISFIED automatically (the amplitude-side twin of R-085's bare sign); dispersive monotonicity (sympy-exact) ⇒ `1/e²(μ)` non-increasing in μ; l₁-mixing MOOT at forward order (l₁ multiplies t², vanishing forward — reviewer-verified independently); the sign's source is the ADDITIVE f²-loop drift, NOT antiscreening — SIGN-CONSISTENCY IS NOT AF-ACHIEVED; DGLAP + magnitude stay N7/Class 2 | DERIVED-A (anchored channel map + monotonicity) + DERIVED-conditional-GENERIC (β₃ ≤ 0 given P-disp/I-13 + P-action one-coupling + P-chan + P-conv; generic per canon §5 — any two-term chiral action; substrate content = the banked action IS that action + engine-exact weights) + LITERATURE-KNOWN-CLASS credited (Pham–Truong) + HARD FENCE + CORRECTION-HISTORY (first build REFUTED — Euclidean-sign transplant, N42; corrected build independently re-derived by a FRESH reviewer on separate code paths) | marginal_skyrme_beta3_sign_dispersive | C.5.2 | R-085, N7, I-13, banked two-term dressed action | — | Banked 2026-07-05 (first build REFUTED by twt-reviewer — five routes incl. static-energy kill; corrected build FRESH-reviewed HOLDS at all tiers — scipy-expm series confirmation, own plane-wave end-to-end map match, l₁-forward-zero verified, branch label attacked and survived). I-13 registered same pass; 13.3 KL row FIRED, a-theorem NOT PURSUED. N42 process lesson banked. Would change if: a new operator class with forward-surviving weight; the I-13 package fails inside-frame (revert to R-085's located gap); one-loop coefficient zero in channel; convention re-anchored. |
| R-149 | P2-2 Gauss-equation face EXECUTED — the R-145 first-order scaffold is CLOSED: `Riem(g)` of the texture metric is ALGEBRAIC in the pointwise first-order data `(E, Ω, dE)` — no derivatives of the FRAME DATA beyond first order (no ddE/ddΩ; the closure drops Riem from THIRD- to SECOND-derivative order in the rotor field — dE itself carries ddR, reviewer-F1 wording). THE CHAIN: (1) CURL CLOSURE `∂_μE_ν − ∂_νE_μ = −L([Ω_μ,Ω_ν])` (E LINEAR in Ω + MC flatness — for a generic non-flat connection the curl would be independent second-derivative data); (2) LEG-MAP INVERSION (the I₄ grade-2 pairing is the signed Hodge pairing ⇒ ALL of dΩ recoverable from dE); (3) GAUSS EQUATION for the induced torsionful metric connection `Γ̃^λ_{μν} = g^{λρ}κ(E_ρ, ∂_μE_ν)`: `R̃_{ρσμν} = κ(S_μρ,S_νσ) − κ(S_νρ,S_μσ)`, `S = (1−Π)dE` the κ-normal part (S NOT symmetric — the torsion is its antisymmetric part; classical subbundle machinery, hypotheses engine-checked, NO QFT import — registry-exempt per canon §2, and independently re-verified in-suite); (4) CONTORSION: `Γ_LC = Γ̃ + C` with C algebraic in `κ(E, L([Ω,Ω]))`; (5) the assembled full identity with `d_μC` itself algebraic in `(E, Ω, dE)` — verified end-to-end against an independent ddg computation, SIGNATURE-BLIND at ALL FOUR nondegenerate menu items (0,4),(1,3),(2,2),(3,1); NON-VACUOUS (Gauss and torsion blocks each the same order as Riem) | DERIVED-A (all five facts — each sympy-exact on a faithful-rep 2-parameter non-commuting family + numeric on generic three-factor rotor fields, Richardson-extrapolated FD) + FRAMING (C_T-skeleton: fluctuations enter the induced-EH spectral sum only through `(S, [Ω,Ω])` at quadratic order — the kernel's mode measure is the missing C_T ingredient, not kinematics) + NOT-DONE (C_T value / absolute EH coefficient — #1-gap as banked; the (1,3) pick; U2 untouched) | texture_gauss_equation_riemann_closure | B.6.6–B.6.7 | R-145, R-042 | — | Banked 2026-07-05 (twt-reviewer HOLDS at all stated tiers; required fix F1 applied — "no second derivatives of the rotor field" was engine-FALSIFIED by the reviewer's ddR probe (two fields with identical (R, dR) but different ddR give different Riem) and reworded to frame-data order; recommendation R1 applied — the (3,1) config added after the reviewer's own independent (3,1) run confirmed the closure at 1.7e-6; the reviewer rebuilt the whole pipeline FROM SCRATCH on its own rotor fields incl. an FD-computed MC form and a large-amplitude stress config max\|Riem\| ≈ 42, all four signatures). First executed move of the Class-2 program (2a: statics cornering the kernel computation's FORM). R-145's would-change-if (3) FIRED-NEGATIVE. Would change if: a proper-rotor-field class breaks MC flatness while keeping the banked g (reopens the face); C_T needs the fluctuation expansion beyond quadratic order in S (skeleton true but partial); vacuum EOM lands non-(1,3) (the reading's target moves, the identity is unaffected). |
| R-150 | Class-2 route-2b campaign dashboard (W2.1) — the kernel OVER-DETERMINATION TABLE: N33's prose meta-result GRADUATED into a checkable, self-validating engine artifact. Ten registry constraints on the #1-gap driven-dissipative kernel, each a structured row (observable; banked kernel_link; value/bracket; frequency_window; frequency_justification; independence; status ∈ {usable-anchor, structural-target, bracket-only, candidate-anchor, numberless, non-anchor, future-falsifier}; is_usable_anchor; caveat). Exactly ONE usable anchor (the KSS/GW bracket — itself not numerically closed: reconciling the η/s-floor with the η-ceiling needs an unstated entropy density s) against a ≥2-parameter causal kernel ⟹ RANK-DEFICIENT by ≥1 dof (= N33's headline; robust: `rank_deficient` holds whether the honest count is 1 or 0). Anchor-counting discipline enforced by LIVE guards: sin²θ_W = 3/8 gate-free ⇒ EXCLUDED (the exact N33 miscount); g/α_s/α_W folded into the single unknown α via g² = 4πα·(8/3); τ_mem [3,380] NOT a target (N34). Carries N33's four named missing inputs (the campaign's acceptance criteria) + the FDT-forbidden/KK-safe jurisdiction (I-12: Θ_rel IS the FDT-violation residual). | FRAMING (over-determination dashboard; the anchor-count operationalizes N33's judgment) + DERIVED-A (live engine cross-validation of the sharpest row values — Kc ratio = (19/2)√38, running µΨ₀ decreasing/sign>0/ratio>2, Brannen 0.28% — + the two exclusion guards: sin²θ_W gate-free, alpha_em_value GATED-raises) | kernel_overdetermination_table | — (companion §4 over-determination opportunity / §12 Class-2 program; not paper-body — a dashboard, not a paper-worthy physics result) | N33, N34, N37, N32a, R-149, R-138, R-111, R-134, im_chi_falsifier_budget_KSS_GW_macromolecule, Kc_magnon_stiffness_canted_FM_at_DJ, I-12 | — | Banked 2026-07-05 (twt-reviewer HOLDS at the proposed tier and scope — independently rebuilt every load-bearing check on the engine; sole finding a cosmetic open_cat1_kernel cite, fixed same pass). First move of the Class-2 (2b) infrastructure; the campaign's live dashboard. NOT a kernel value, NOT a new anchor, NOT a resolution of the rank deficiency — a census. The count increments when a genuine new (frequency, value) anchor (N33 input (3), e.g. the W2.2 static sum-rule datum) is manufactured. Suite 397→398 (twt_algebra 31). |
| R-151 | W3.1 — the C_T mode-measure MOMENT COUNT (the P2-2 endgame's first quantitative reduction): the R-145 internal symmetry `SO(4)_tangent × SO(3)_SD × SO(3)_ASD` — a PRODUCT (the fact-(7) gauge rotates leg-values tangent-index-free, so it commutes with SO(4)_tangent; NOT a locked diagonal, which the verifiers computed at ~21–29) — forces R-149's C_T integrand (a quadratic form in the fluctuation data `S_sym ⊕ [Ω,Ω]`) into an **8-dimensional space of invariant quadratic forms** (S-block 4, [Ω,Ω]-block 4, cross 0 by SO(4)-irrep disjointness Sym²4={(3,3),(1,1)} vs Λ²4={(3,1),(1,3)}), split **4 parity-even + 4 parity-odd** (SD/ASD channels exchanged by parity; the su(2)⊕su(2) block structure `[SD,ASD]=0` IS the substrate I4-Hodge split — I4·SD=+SD, I4·ASD=−ASD — engine-exact). CONSEQUENCE: *given the unbroken product symmetry*, C_T (parity-even) is a kernel-weighted combination of **at most 4 numbers** — C_T's kernel-dependence reduced from an unknown FUNCTION to ≤4 NUMBERS (an UPPER BOUND: treating (S,[Ω,Ω]) as general over-counts in the honest direction; the spin-2/Ricci sub-projection pins the exact ≤4). | DERIVED-A (su(2)⊕su(2) block-exact + the COUNT given the group, exact commutant algebra + seeded character MC) + DERIVED-given-R-145-fact-(7) (the product group; a dynamical diagonal-locking would raise the count) + FRAMING (spin-2/Ricci sub-count = would-sharpen) | ct_kernel_moment_count_symmetry_reduction | B.6.7 | R-149, R-145, R-124 (commutant method), chirality_is_a_reflection (parity), texture_frame_6to4_reduction fact (7) | — | Banked 2026-07-05 (THREE independent methods via a Workflow fan-out — exact commutant + basis-independent solver; analytic Clebsch-Gordan; Reynolds character MC — reproduced 8 / 4+4 / cross-0, confirmed the product group by [tangent,value]≈2.2e-16 + the locked-alternative ~21–29; twt-reviewer HOLDS at the stated tier — rebuilt the count by a 4th method (hand irrep-decomposition), verified fact (7)'s g-invariance and the I4-Hodge split (substrate-specific, NOT generic-given-4D), and confirmed the ≤4 upper-bound framing is fenced everywhere). Would change if: a substrate-dynamics diagonal-locking shrinks the group; the spin-2/Ricci projection pins the exact ≤4; cubic-order fluctuations grow the space. Suite 399→400 (twt_cosmo 95). |
| R-152 | W3.2/A2 — the µΨ₀ ρ_L SEAT INTEGRAL (R-129's "remaining construction: the §D.4.4 boundary integral on an explicit profile") COMPUTED on the banked Q-orbit baryons (R-133 hedgehog, R-144 torus). The LITERAL §D.4.4 (V2 §10.5) scalar ρ_L boundary term `ρ_L = ⟨Ω³⟩₀` VANISHES IDENTICALLY on any Q-orbit rotor field (`e₁₄·e₂₄·e₃₄ = −I₄` grade-4 ⇒ the Q-orbit su(2) winding density is PARITY-ODD / I₄-valued, scalar part 0; profile/geometry-independent — hedgehog, squashed, B=2-twist all give `⟨Ω³⟩₀ = 0` to ~1e-14) — a CLEAN NEGATIVE confirming N32a "ρ_L sources L-orbit winding, not Q-orbit baryon winding" (physically: a baryon has B≠0 but L=0). BUT the R-128 parity-odd Hodge-dual quark-lock (I₄·Ω) recovers the scalar L-winding EXACTLY (`⟨(I₄Ω)³⟩₀ = \|⟨Ω_L³⟩₀\|` to ~1e-15) ⇒ the corrected seat FORM `L_θ = µΨ₀·B_Q`, parity-odd, linear in the integrated winding B_Q (π₃ degree). The `⟨⟩₀` scalar-grade projection is TWT's standing trace convention (§D.4.4/R-109 defines the whole medium Lagrangian with it; the gravity sector uses ⟨Ω I₄ Ω⟩₀) — the vanishing is a genuine consequence of the banked L/Q = Hodge-grade split, not a definitional artifact. | DERIVED-A (Clifford core: `e₁₄e₂₄e₃₄=−I₄`, the literal-seat vanishing, parity-odd winding, exact Hodge-recovery) + the PHYSICAL seat identification INHERITS R-128's OWN FRAMING tier (the up/down-seat + µΨ₀-through-the-lock tie are FRAMING; NOT promoted) + value µΨ₀ #1-gap GATED (∝B_Q ⊥ generation index ⇒ does NOT give N37's inter-gen running) | updown_seat_rhoL_parity_odd_hodge_form | C.3.13 (+ §B.3.1, §D.4.4 note) | R-128, R-129, R-110, R-109, N32a | — | Banked 2026-07-05 (W3.2/A2, twt-reviewer HOLDS + 2 wording softenings applied: seat-FORM reads as conditional on R-128's FRAMING µΨ₀-tie; "linear" is of the integrated B_Q not the local density; the reviewer independently reproduced the grade decomposition — L-hedgehog Ω³ pure grade-0, Q-hedgehog Ω³ pure grade-4 same magnitude — and confirmed the ⟨⟩₀ convention is banked upstream). Resolves R-129's "pointed to not confirmed" ρ_L seat: literal seat = clean negative; Hodge-dual seat FORM derived; value + N37 running stay #1-gap gated. Suite 401→402 (twt_spectra). |
| R-153 | The #1-gap kernel CANDIDATE FORM (the KS selection campaign, Grade B): `Im χ(ω)` odd, passive, KK-causal, IR exponent s ≥ 3 (the Adler/Goldstone floor), UV cutoff — *constraints-by-construction* (the hard properties exact by construction, never filtered after); three spectral members — nodal algebraic-edge `xᵖ/(xᵖ+1)` (p ≥ 3), s-wave exponentially-gapped edge, and their positive composite — plus the EXCLUDED edge-less reference (kstar, culled by the two-sided D3 test) | CANDIDATE (Grade B — a surviving CLASS, not a pinned kernel) | kernel_candidate_form | E.5 | R-113, R-114, R-115, R-118, R-030 | R-154, R-155, R-156, R-157, R-158 | Banked 2026-07-22 from the simulator KS campaign (commits ec11cfc…1ae53b7; every phase adversarially reviewed to consensus; corpus frozen throughout per the campaign's RULE 1; simulator suite 144→172). The Section-12 Class-2b closure route EXECUTED. Selection within the class is NOT supplied by the executable scores (R-157). |
| R-154 | Composite closure: the constraints-by-construction properties (oddness, passivity, KK-integrability/causality, s_IR = 3 Adler floor) are CLOSED under the positive Goldstone+magnon summation `[nodal(p=3) + r·swave]/(1+r)` — the F2 edge-class fork DISSOLVES into a single measured ratio r (r=0 → nodal exactly; r→∞ → swave; boundary recovery exact) | DERIVED-A (the closure property; sympy + numeric witnessed) + CANDIDATE/FRAMING ("the substrate kernel IS this two-sector sum" — the SN-16 grounding) | kernel_composite_closure | E.5 | R-153 | R-155 | The candidate's one algebraic-DERIVED content (with the exact-by-construction hard properties); everything about the *selection* stays CANDIDATE. Mirrors the simulator witness `kernel_space.composite_closed_under_summation`. |
| R-155 | The counted candidate economy: genuine dials = IR exponent p, edge width wT, UV plateau width W, memory time τ_mem (+ the composite ratio r); one redundant edge scale exactly absorbable (SN-15 — NOT a dial); ONE binary INPUT bit = the hysteretic memory branch (the F4 PICK; the weak=SD menu-vs-pick pattern, consistent with §D.5.3's adopted working branch — a pick, NOT a derivation); minimal member = 2 dials + 1 bit | INPUT/FIT (candidate-scoped: counted within the candidate's OWN ledger; joins the §E.2.1 framework ledger ONLY if the candidate is adopted) | kernel_candidate_dials | E.5 | R-153, R-115 | R-156 | The fading class is dropped from the space by the pick; the campaign's bathless forcing attempt (KS-0a) remains FRAMING/CANDIDATE — the pick is NOT upgraded to derived. |
| R-156 | Constraint provenance: every member passes both oracles' EXECUTABLE constraints by construction (the simulator bench's hard gates + the engine's 5 hard rows of `kernel_candidate_constraints`); the 3 channel TARGETS ((19/2)√38 ≈ 58.56 [N31]; Λ~H² c ≈ 2.05 [N33]; ≤ 4 spin-2 C_T moments [R-151]) stay GATED — the candidate supplies form-side inputs only; the numbers are never fitted (their kernel→observable maps are themselves #1-gap objects) | CANDIDATE/FRAMING | kernel_candidate_constraints | E.5 | R-153, R-114, R-040, R-150, R-151 | R-157 | The registry over-determination activates only when a gated forward map is built (the Class-2b promise, honestly conditional). Fitting a channel target through an unbuilt map is reward-hacking — forbidden (campaign T-any). |
| R-157 | The reading-conditional executable RANK-DEFICIENCY: under the F-strong (optimistic, two-sided) flatness reading a plateau class survives (kstar culled); under the ADJ-1-OPERATIVE (one-sided ceiling) reading the executable flatness selects NOTHING; the a_e discriminator CONFOUNDS τ with p in a free-scale search — the F1 (exact-3 vs ≥3) and F2/r (edge-class/ratio) forks stay OPEN; discrimination deferred to the virgin band (P1) + the fixed-τ a_e ratio (P2) | FRAMING (confirmed BY SEARCH over 344 candidates, not merely asserted) | kernel_overdetermination_table | E.5 | R-150, R-156 | R-158 | Exactly the registry's own `n_usable_anchors = 1` situation (R-150) — the sanctioned Class-2b state; BOTH readings must always be stated together. |
| R-158 | Seven pre-registered virgin-sector falsifiers P1–P7 (two-commit git-proven: REGISTER `27e2847` strictly before EVALUATE `7f2d52d`) + the two-sided D3 edge-less cull: P1 μeV-band knee vs the SC-persistence ceiling (consistent-structural), P2 a_e two-point ratio (separates the classes at fixed τ; external test FUTURE), P3 knee·τ_mem train-cadence (FUTURE), P4 mass-frequency containment (consistent), P5 activated driven-rate landscape (FUTURE), P6 near-KSS (compatibility NOT confirmation — η/s gated; the commitment STANDS, no renegotiation), P7 the dissipative generation route (structural pass) — NO MISSES on the evaluable-now set {P1, P6} | CANDIDATE (register + outcomes; every magnitude gated) | kernel_candidate_falsifiers | E.5 | R-153, R-157 | — | An edge-less substrate kernel finding would kill the class (the structural falsifier). The paper's near-KSS commitment (§E.3.3 VG-1) is not challenged. JURISDICTION HEDGE (N49/KC-1 class, load-bearing): P1's SC-persistence ceiling and R-157's superallowed-flatness datum are INSIDE-frame data — they bind the outside-frame kernel only through the un-built outside↔inside projection; the numeric comparisons gate on exactly that leg. |
| R-160 | Born exponent = 2 as a theorem: F2+F3 ⇒ additivity (coarse-graining) ⇒ Gleason ⇒ `Tr(ρP)`; F4 ⇒ `ρ = \|ψ⟩⟨ψ\|`. No power-law family assumed anywhere; dim-2 sectors inherit through the joint system–detector sector | DERIVED-conditional-on-(F1–F4) + import-exempt pure math (Gleason 1957) | born_exponent_gleason_closure | B.3.3 | R-021, R-023, R-029 | R-027 | **F2** (statistical noncontextuality of the Role-3 selection functional) is the single NEW substantive premise; it does NOT follow from §B.3.1 frame-equivalence — covariance ≠ noncontextuality (engine counterexample). F1 carries single-outcome definiteness; F3 = total function on the JOINT lattice incl. entangled contexts (not "mild"). The coarse-graining reduction is literature-standard, not TWT-novel. Supersedes R-023's "plausibility-modulo-degree". |
| R-161 | P1b SPLIT — the mass-phase lock channel carries exactly the induced-term theorem's mass-form structure: quark lock axial / lepton lock vector *relative to the winding assignment*; R-128's parity dichotomy extended from 3 lattice axes to generic coset directions; lepton exclusion hardened at the 4-doublet count | DERIVED-A (the Cl(4,0) identities) + DERIVED-CONDITIONAL (the channel reading) given C1′+C2′+C3′+C4′ | lock_channel_is_axial_chiral_channel_p1b_split | B.3.5, C.4.6 | R-127, R-128, R-002, R-141 | R-141 | The dichotomy is **winding-assignment-relative**, not intrinsic (the lepton generator has axial form about its own dual axis); the intrinsic load-bearing facts are quark-line U-slaved phase at ω vs lepton-line coset-phase-blindness, riding R-002's L/Q assignment. C4′ = roster colour modes' local winding = the baryon field's local coset orientation. **P1b-DYN** (the mode determinant actually generating the term) stays CANDIDATE and carries all dynamical load. No sign is produced by these identities (L1–L3 / N35 honored). Lepton hardening is 4/12 only, NOT 6/18. |
| R-162 | Coupling-sector channel disjointness: `⟨X I₄ X⟩₀ ≡ 0` on the colour sector; signed `⟨B I₄ B⟩₀ = \|B_ASD\|² − \|B_SD\|² = 2⟨B_L I₄ B_Q⟩₀`; EM = spin-1 multiplicity-2 block vs coset-5 = spin-2 multiplicity-1 block, cross-invariants 0; blocks dimensionally inequivalent (6 vs 5) ⇒ no intertwiner under any subgroup chain | DERIVED-A (the channel classification) + LOCATED-GAP (the α_s fold-in reduction) | coupling_sector_channel_disjointness | B.5b.3 | R-035a, R-081, R-085, R-151 | — | Closes the symmetry route to a derived shared-condition: the fold-in is equivalent to ONE named kernel property (cross-block rigidity) **plus an OPEN cross-block weight** (the missing 8/3-analogue). Conditional on the gluon-FRAMING channel assignment + the couplings-as-Im-χ-moments FRAMING. Scenario-scoped: the zero-cross statement is Spin(4)/spatial-SO(3); under Z₃-only — and a fortiori N10's Z₃-broken NESS — crosses are allowed-but-unforced (count 10). Two-point / magnitude-source scope ONLY, never the running or AF face. Vindicates the 2026-07-26 audit demotion of the fold-in. |
| R-163 | Induced-EH coefficient computed on the framework's own DERIVED linear face: the proper-time integral over the derived D4 NN band converges with no regularization choice entering the flat-band measure; I-3's premise triple → two named assumptions | DERIVED-given-the-NN-band-INPUT (flat-band numbers) + DERIVED-conditional-on-(OA-LF-i ∧ OA-LF-ii) (the EH-coefficient reading) | induced_G_from_linear_face_band | B.6.2 | R-112, R-037, R-041 | — | **OA-LF-i** = NESS occupation is the ground-state one (a statement about the STATE); **OA-LF-ii** = covariant curvature coupling at monad scale (about the OPERATOR) — carries ~93% of the integral's support, i.e. the old regulator freedom RELOCATED and localized, not removed. "Regulator-free" describes the flat-band measure ONLY. Bracket stays CANDIDATE/conditional; inherits R-041's FRAMING+CONDITIONAL. In §B.6.2's own normalization this reads c_reg ≈ 1.8 (inside its "c_reg ~ 1"); the convention-invariant statement is that the monad spacing is Planckian within O(1). Gapless-shared-band idealization — canted-vacuum (N_G = 2) refinement softens it by tens of percent. Method externally validated (Z⁴ tadpole reproduced to 2e-8; independent Monte Carlo). |
| R-164 | The banked Skyrme quartic contains NO tree-level Einstein–Hilbert term: quartic (Killing-built, parity-EVEN) and `√gR` (h-built, parity-ODD) fall in disjoint sectors of the R-151 invariant space with exactly zero overlap; nonperturbative kills at all four menu signatures | DERIVED-A (decomposition / orthogonality) + DERIVED-structural (the EH-ABSENT verdict), conditional on U2 + the banked Ω-algebraic action class + the {cc, R², Ric², Riem²} menu quantifier | skyrme_quartic_contains_no_tree_EH | B.6.6 | R-042, R-107, R-109, R-149, R-151 | — | Mechanism: the definiteness that makes the quartic a Derrick stabilizer is exactly what makes it EH-blind — stretching vs bending elasticity, with the Sakharov loop the standard generation of the second from fluctuations of the first. Kill chain (sequential, do not compress): parity/S-block disjointness ⇒ λ=0 at quadratic order; ddR-freeze ⇒ λ=0 nonperturbatively vs a cc term + any Ω-algebraic remainder; one-blade family ⇒ λ=Λ_cc=0 with Gauss–Bonnet the sole surviving direction; frozen-quartic sweeps ⇒ GB dies. R³/∇Riem-class fall to the same dE-independence schema but were NOT run. Sole-route consequence is CLASS-SCOPED (a new dE-dependent term or the Paper-2 thermodynamic route would reopen it). Negatives ledger **N51**; probes preserved at knowledge/candidates/probes_2026-07-27/. |

---

## Part C — Matter, charges, generations, gauge group

| ID | Statement | Tier | Engine | § | Deps | Used by | Notes |
|---|---|---|---|---|---|---|---|
| R-051 | Skyrme mass formula `M_0 = 36.47 f_π/e` at dressed-coupling level | DERIVED at dressed-coupling | skyrme_BVP_audit + skyrmion_mass_MeV + skyrme_length_fm | C.1 | R-007, A-1c | R-053 | Conditional on dressed-sector closure. ~1% favourable scheme, ~10% cross-scheme spread. |
| R-052 | Exactly two conserved topological windings `(B, L)` — chiral counting from `Spin(4) = SU(2)_+ × SU(2)_−` relabeled to the orbit basis `(n_𝓛, n_𝓠)` via the §A.5.2 symmetric-pair / fibration bridge | DERIVED-A | pi3_S3_integer_completion | C.1 | R-002, R-009 | R-053, R-054, R-087 | Structural skeleton of all matter. The chiral basis gives the `ℤ × ℤ` directly; the orbit basis is the framework's working basis. Lepton hedgehog is subgroup-valued (into `Spin(3) = exp(𝓛)`); baryon hedgehog is coset-valued (into `Spin(4) / Spin(3) ≅ S³_𝓠`). Both yield `ℤ` degree; the targets are topologically distinct map types. |
| R-053 | Baryon as one Q-orbit defect with three orthogonal facets (V2 §3.2 / §16.5.1.1) | DERIVED-STRUCTURAL | nonuniform_orbit_baryon_model + cogear_linkage_kinematic + baryon_mass_shared_rotor_nonadditive + e4_content_confines_quarks_not_leptons | C.1 | R-005, R-052, R-051 | R-084, R-085 | Three "quarks" are three facets of one circular winding. |
| R-054 | Proton stability from `B ∈ π_3(SU(2)) = ℤ` integer winding | DERIVED-A | pi3_S3_integer_completion + lepton_number_topological_conservation | C.1 | R-006, R-052 | R-089 | Canonical falsifier §E.3 row 4. |
| R-055 | Electron as Hopf defect on L-orbit; QCP scaling `f_L = f_π · (1 − D/J)^{9/2}` at L1 | DERIVED-CONDITIONAL | electron_two_windings + electron_QCP_nu + electron_f_L_MeV | C.1 | A-1c, R-007 | — | 35% in `f_L`, 4.5% in exponent. L2 mechanism unidentified (`ν = 3π/2 = 4.712`, CANDIDATE). |
| R-056 | Per-blade hypercharge from `e_4`-bilinear `B̃ e_4 B` (±1 eigenvalues, engine-verified) | DERIVED-A | hypercharge + doublet_hypercharge + winding_charge | C.2 | R-010 | R-057, R-062, R-080 | — |
| R-057 | Fractional quark charges `±2/3, ±1/3` from algebraic three-quark blade structure | DERIVED-A | gmn_coefficient + triple_product_Q + triple_product_color | C.2 | R-056, R-053 | R-062, R-063, R-073 | Algebraic identity. |
| R-058 | Weak isospin from meta-time rotor doublet `(sin(ωτ/2), cos(ωτ/2))` | DERIVED | doublet_hypercharge (Y-side only; the T₃ doublet content is posited in-engine) | C.2 | R-007 | R-060, R-061 | Realizes lepton/quark doublet. |
| R-059 | Lepton-quark weak universality as algebraic theorem on S_+ | DERIVED | universality_theorem | C.2 | R-058, R-079 | — | Algebraic, not coincidence. |
| R-060 | V−A structure from SD's half-module kernel (couples one Weyl chirality only) | DERIVED-given-input-R-079 | weak_isospin_SD_parity_exclusion + vminusa_is_spin4_factor_chirality | C.2 | R-058, R-079 | — | DERIVED-given the weak=SD input bit. |
| R-061 | Generation-blindness / no tree FCNC from SD centralizing ASD generation triple | DERIVED-given-input-R-079 | weak_isospin_zero_on_generations + weak_isospin_centralizer_is_SD | C.2 | R-079, R-071 | — | Canonical falsifier §E.3 row 17. |
| R-062 | Gell-Mann–Nishijima `Q = T_3 + Y/2` as DERIVED algebraic identity (not imported) | DERIVED-A | gmn_coefficient + generation_spectrum | C.2 | R-056, R-058 | R-063 | The combination — including the exact 1/2 — is derived. |
| R-063 | Charge discreteness/commensurability `{0, ±1/3, ±2/3, ±1}·\|Q_e\|` exactly; `\|Q_p\| = \|Q_e\|` protected (tested `< 10⁻²¹`) | DERIVED-A (discreteness + GMN non-circularity); the equality NORMALIZATION conditional on the neutrality-of-atoms anchor — an inside-frame empirical import (engine tier note 2026-06-30) | winding_charge + gmn_coefficient + generation_spectrum + pi3_S3_integer_completion | C.2 | R-062, R-054 | (paper headline) | Anti-circularly grounded via §C.5 topological winding (integer-valuedness); equality protected by commensurability. **The normalization anchor is CONDITIONALLY REPLACED by R-159** — `Q_p + Q_e = 0` holds identically in `c` given (P4, P5, P6), so the neutrality-of-atoms datum is no longer consumed at this site (it reverts to being the anchor if those premises fail). Second-cleanest spine result. |
| R-064 | Brannen amplitude form `A_k = 1 + c cos(...)` from V_4⊥ projection geometry | DERIVED | brannen_amplitude + koide_K + koide_from_c | C.3 | R-009 | R-065, R-066, R-068 | Projection of meta-time circle on V_4⊥. |
| R-065 | `√2` projection coefficient — the equivalence content: `K = (1+2r²)/3` gives `K = 2/3 ⇔ c = √2` (the same INPUT bit as `K = 2/3`, seen through the projection geometry) | INPUT-equivalent (the value); the equivalence itself DERIVED-A | dft_K_from_r | C.3 | R-064 | R-066 | NOT independently forced — six forcing routes NEGATIVE (see R-066); the primitive computes the equivalence, not a forcing. |
| R-066 | Koide `K = 2/3` ⇔ `c = √2` Brannen-Koide equivalence theorem | DERIVED-A | koide_K + koide_from_c + koide_charge_unification + dft_K_from_r | C.3 | R-064, R-065 | R-067, R-068 | Theorem; K=2/3 is INPUT (exact-but-unforced; six forcing routes NEGATIVE). |
| R-067 | Foot 45° signature-free characterization | DERIVED-A | foot_angle_deg | C.3 | R-066 | — | Independent of mass-measure convention. |
| R-068 | Three lepton mass ratios at `δ_L = 12.73°` to <0.01% | FIT (post WP-MASS-MEASURE) | brannen_amplitude + delta_L_from_DoverJ + DoverJ_from_lepton_masses + hierarchy_type | C.3 | R-064, R-066 | R-069, R-074 | Tier qualified: forward derivation `L-orbit τ=0 → lepton ε=0` REFUTED in V2 Phase F. Mass-measure `√m = r²` (mass_measure_from_omega) sits at CANDIDATE-strong. |
| R-069 | `D = J ⇔ δ_L = π/12 ⇔ m_e = 0` structural identity at leading order | DERIVED-STRUCTURAL | delta_L_from_DoverJ + D_crit_over_J | C.3 | R-068 | — | Substrate-side identity. |
| R-070 | δ_L from chiral-ℤ_3 potential FORM (coefficient identification A=J, B=D is ASSERTED ANSATZ) | DERIVED (form) + ASSERTED (coefficient identification) | delta_L_from_DoverJ | C.3 | A-1c | — | Honest scope. |
| R-071 | Three generations from Frobenius + ASD-triple + ℍ-unit identification | DERIVED-STRUCTURAL-LOCATED | why_three_generation_triple + generations_dynamical_count_structural + phase_to_h_unit_map_located_residual | C.3 | R-009, A-1a | R-061 | LOCATED-conditional on the orbit-phase → ℍ-unit map (`why_three_generation_triple`). |
| R-072 | `G` is the colour ℤ_3 (not the generation ℤ_3) per the §C.3.9 reidentification (V2 §17.4) | DERIVED | G_generator + G_cycles_generations + generation_z3_is_metatime_phase | C.3 | R-009 | — | Spatial generator G is colour cycle; generation ℤ_3 is meta-time phase. |
| R-073 | Cabibbo as frequency ratio `\|V_us\|² = m_d/m_s ≈ 0.05`, 0.6% match | CANDIDATE | quark_brannen_table + quark_mass_reconstruction + cabibbo_transition_probability | C.3 | R-057, R-068 | — | TWT-untestable on `m_t` ratio (no top hadrons). Engine numbers: `\\|V_us\\|² = 0.0503` vs `m_d/m_s = 0.0500` (PDG 4.67/93.4), 0.62% off (`cabibbo_transition_probability`, inline assert < 1%). Cite `cabibbo_angle_rad` removed 2026-07-02 — that primitive is formally DEPRECATED (returns the lepton phase δ_L, not a Cabibbo angle; V1 identification refuted 2026-06-29). |
| R-074 | Cross-sector D/J over-determination: lepton 0.787 ↔ baryon 0.778, ~1.1% | DERIVED-CALIBRATED | DoverJ_from_lepton_masses + DoverJ_from_skyrme + over_determination_scan + dressed_coupling | C.3 | R-068, R-051 | — | Genuine over-determination signal. |
| R-075 | Neutrino forced left-handed from `+e_4` wave direction | DERIVED | forced_handedness | C.3 | A-3, R-007 | R-079, R-060 | Substrate-derived chirality. |
| R-076 | Neutrino lightness from single Weyl ideal | DERIVED | neutrino_lightness | C.3 | R-012, R-075 | R-089, R-121 | Structural consequence of single ideal. |
| R-077 | Up/down mirror SD ↔ ASD under spatial parity; up = SD chirality identification | DERIVED | updown_mass_operators_commute + updown_mirror_value_three_handles | C.3 | R-099 | R-079 | V2 W-LIVE-2 promotion. |
| R-078 | Substrate carriers of SM gauge content (SD, Q-orbit, I_4 + bivector, `e_4`-bond pairing) | DERIVED-STRUCTURAL | spatial_vs_phase_partition + L_Q_orthogonal_decomposition | C.4 | R-009, R-010 | R-079, R-080, R-081, R-082 | Four substrate-distinct sectors match SM gauge content. |
| R-079 | Weak = SD (chiral Spin(4) factor); the weak sector's single INPUT bit | INPUT | weak_isospin_SD_parity_exclusion + weak_isospin_centralizer_is_SD + weak_isospin_verdict + weak_isospin_rank_table + vminusa_is_spin4_factor_chirality | C.4 | R-075, R-076, R-078 | R-060, R-061, R-077 | Neutrino-forced (forced-LH + single-Weyl ⇒ chiral). V−A, gen-blindness, doublet, up=SD all DERIVED-given-it. |
| R-080 | U(1)_Y from I_4 + bivector compactness; I_4 cannot be the compact gauge generator (`I_4² = +1` non-compact) | DERIVED | hypercharge + winding_charge + I4_squared | C.4 | R-056, R-010 | R-082 | Gauge field is bivector-generated; I_4 labels the conserved-charge direction only. |
| R-081 | Colour octet `8 = 3 ⊕ 5` symmetric-space split; `C_A/C_F = 9/4 = 2.25` matches LEP `2.27 ± 0.06` | DERIVED-A (algebra) + LOCATED-GAP (dynamics) | gluon_octet_symmetric_space_split + colour_quartic_charge_handle + colour_relative_phase_is_coset + colour_sector_E_hermitian_form + colour_su3_located_gap + colour_SO3_re_realization_forbidden | C.4 | R-053, R-072 | R-085 | Static algebra constructed; dynamical running #1-gap-gated. |
| R-082 | `sin²θ_W = 3/8` at unification, unconditional native derivation | DERIVED-A | weinberg_sin2 | C.4 | R-056, R-062, R-079, R-080, R-009 | (paper headline) | Engine-verified EXACTLY. No SU(5), no foreign Lie-algebra import. `g_1 = g_2` from dim-4 D4 isotropy theorem (same theorem as Lorentz protection, R-016 / R-039). |
| R-083 | 24-bond count = 12 + 12; SU(5) labeling as historical translation only (no physical SU(5), no X/Y bosons) | DERIVED-STRUCTURAL | D4_spatial_bond_isotropy + D4_DM_bond_bivectors_non_commuting | C.4 | A-1b | R-104 | Representation-theoretic match with GUT literature; not load-bearing. |
| R-084 | Confinement: ontological-first (one defect, three facets) — topology is formal consequence | DERIVED-STRUCTURAL | pi3_S3_integer_completion + e4_content_confines_quarks_not_leptons | C.5 | R-053, R-006 | — | V2 W-LIVE-5 reframing. |
| R-085 | No fundamental SU(3)_c gauge field; colour octet is elastic-response algebra (3 + 5), not eight gluons | DERIVED-STRUCTURAL | gluon_octet_symmetric_space_split + colour_SO3_re_realization_forbidden | C.5 | R-081, R-053, R-008 | — | Asymptotic freedom β_3 < 0 LOCATED-GAP (Paper 2). |
| R-086 | `⟨I_4⟩ ≠ 0` (DM condensate) delivers parity violation, not EWSB | DERIVED | eta_DM + chirality_does_not_source_P + chirality_is_a_reflection | C.5 | A-1c, R-010 | R-044, R-090 | I_4 is a gauge singlet; condensate invariant under G can't break G. |
| R-086a | Doublet condensate `Φ` on spinor minimal ideal as EWSB order parameter; `⟨Φ⟩ = (0, v/√2)ᵀ` with `v ≈ 246 GeV` breaks `SU(2)_L × U(1)_Y → U(1)_em` via standard mechanism | FRAMING + GATED (magnitude) | — | C.5.3a | R-086, R-062 | — | Structural identification of EWSB on spinor module; absolute `v` and Higgs mass #1-gap-gated. The negative half (⟨I_4⟩ NOT EWSB) is R-086. |
| R-087 | B − L anomaly cancellation from `3 × 1/3 = 1` | DERIVED-A | B_minus_L_anomaly + anomaly | C.5 | R-057 | R-089 | One quark of charge 1/3, three colours; one lepton of charge 1. |
| R-088 | BPST instanton + index theorem ⇒ `ΔB = ΔL = N_gen = 3` selection rule | DERIVED-given-I-2 (imported instanton + index theorem, Section 13) | bpst_charge_Q + bpst_selection_rule | C.5 | R-087 | R-089 | Non-perturbative violation respects B − L exactly. |
| R-089 | No proton decay + Dirac neutrinos + no `0νββ` as one structural fact | DERIVED | B_minus_L_anomaly + bpst_selection_rule + lepton_number_topological_conservation + pi3_S3_integer_completion | C.5 | R-054, R-076, R-087, R-088 | R-121 | Three SM "extras" collapse to one substrate fact. Canonical falsifiers §E.3 rows 4, 5. |
| R-090 | β-decay as L-pair creation through I_4 Hodge map; same D underwrites parity violation + Cabibbo + δ_L + Skyrme stabilizer | DERIVED | I4_maps_L_to_Q + lepton_number_topological_conservation | C.5 | R-010, R-086 | — | One D, multiple manifestations. |
| R-091 | Wave-phase stability ladder across 20 states (engine-verified empirical-coherence) | DERIVED-STRUCTURAL | wave_E_complex_structure + wave_E5 | C.5 | R-007 | — | Validated on 9 orders of magnitude in N. |
| R-091a | Top quark exclusion: `Γ_t · Θ_0 ≈ 7.2 ≫ 1` — top facet unwinds before circular winding completes; no top hadrons | DERIVED-STRUCTURAL | top_excluded + alpha_H_gap + x_Q | C.5 | R-053, R-008 | (falsifier §E.3 row 14) | Timescale-exclusion structural argument. The top mass is SM bookkeeping, not a TWT verifier (per canon §5). Was ≈6.5 before the R-133 Θ₀-coefficient correction (2026-07-03); STRENGTHENED. |
| R-091b | Nuclear length hierarchy: hard core `√2 ℓ_S ≈ 0.397 fm` vs empirical 0.40–0.50 fm (12%, no new parameter); pion Yukawa `~1.46 fm`; 25-cell footprint (1 + 24 = D4 kissing); `r_{90} ≈ 0.518 fm`, soliton diameter `~ 1.12 fm` | DERIVED-given-(e, f_π) — no NEW parameter (ℓ_S = ℏc/(e·f_π) rides the two ANW-fitted constants) | nuclear_length_hierarchy + skyrme_length_fm (cover the four lengths; the r_90/25-cell prose is not engine-covered) | C.5 | R-051, R-053 | — | Cell-exclusion phenomena set both hard core and confining-string diameter. 25-cell structure ties directly to A-1b D4 kissing. |
| R-091c | Mesons are NOT topologically protected (`n_𝓠 = 0`, `H = 0` — trivial class on both orbits); stability is empirical: π Goldstone, K/η pseudo-Goldstone, η_c/η_b heavy quarkonia, σ/ρ/ω CANDIDATE substrate identifications. Kinematic mass formula `m = 2 ω · \|cos(α/2)\|` for two opposite-E-sign defect facets | DERIVED-STRUCTURAL (no-protection) + CANDIDATE (σ/ρ/ω) | meson_topological_status + meson_dynamical_current_split | C.5.11 | R-006, R-053 | — | Resolves §A.4's forward-reference to meson decomposition. The no-protection result is the DERIVED content; σ/ρ/ω identifications are CANDIDATE pending §D.5. |
| R-159 | Charge-normalization ANCHOR-FREE: `Q_p + Q_e = 0` identically in `c` — the T₃ bracket and the hypercharge bracket `3Y_Q + Y_lep = 0` vanish separately; `uud` is the unique three-facet composite at `−Q_e`; hydrogen neutrality becomes a theorem rather than a consumed datum | DERIVED-structural CONDITIONAL on (P4, P5, P6), inheriting the counted weak=SD INPUT via R-058/R-079 | charge_normalization_anchor_free | C.2.7, C.2.8 | R-056, R-057, R-058, R-087 | R-063 | **P4** = one universal linear charge functional `Q = T₃ + c·Y` across all sectors — FRAMING-supported by R-035 (single photon bridge) + R-086a (unbroken combination); **R-086a has NO engine primitive — never cite this support as engine-checked**. **P5** = per-defect chirality-independence. **P6** = proton = `uud`, an inside-frame state identification. Counterfactual (derived-vs-generic): delete R-057's `/3` and the residue is `2c ≠ 0` — substrate-specific, not generic. `c = 1/2` fixings, honestly counted: ONE native route (itself conditional on the wave-decoupled ⇒ `Y(S_−) = 0` inference — its own would-change-if) + TWO independent conditions under the I-18 anomaly import + ONE downstream condensate check. Retires the neutrality-of-atoms import at this site CONDITIONALLY; would revert if per-orbit normalizations can differ. New falsifier §E.3 row 18. |

---

## Part D — The substrate, technically

| ID | Statement | Tier | Engine | § | Deps | Used by | Notes |
|---|---|---|---|---|---|---|---|
| R-092 | Cl(4,0) ≅ M₂(ℍ) by Bott periodicity | DERIVED-A | cl_dimension + _cl40 + cl40_quaternion_triple + cl40_vs_cl41 | D.1 | A-1a | R-014 | Engine-verified. |
| R-093 | Cl⁺(4,0) ≅ ℍ ⊕ ℍ — the quaternion subalgebra | DERIVED-A | cl40_quaternion_triple + cl40_vs_cl41 + cl41_grounding_litmus | D.1 | R-092 | R-020 | Even subalgebra structure. |
| R-094 | `e_5` grounding litmus: Cl(4,1) constructions are grounded iff `e_5`-content reduces to PHASE under Cl(4,0)+ℍ picture | DERIVED-A | cl41_grounding_litmus + cl41_phase_is_external_u1 + cl41_idempotents_note | D.1 | R-092 | R-095 | Canon §5 guardrail. Catches `e_5`-as-spatial-DOF errors. |
| R-095 | Primitive idempotents in Cl(4,1); meta-time phase as external U(1) | DERIVED-A | cl41_idempotents_note + cl41_phase_is_external_u1 + dirac_ideal_idempotent | D.2 | R-094, R-012 | R-007 | Meta-time rotor lives here. |
| R-096 | Dirac spinor as M₂(ℍ)-module element; wave field structure | DERIVED-A | spinor_real_dof + dirac_ideal_idempotent | D.2 | R-012, R-014 | R-026 | Standard. |
| R-097 | Anchoring triple products: Q-orbit bivector triple `e_{14} e_{24} e_{34} = −I_4` (→ pseudoscalar); Q-orbit trivector triple `e_{124} e_{134} e_{234} = +e_4` (colour singlet, → vector). The L-orbit triple `e_{12} e_{13} e_{23} = +1` closes to a scalar and is not an anchoring identity | DERIVED-A | L_Q_orthogonal_decomposition + triple_product_Q + triple_product_color + L_algebra_su2_closure | D.2 | R-009, R-010 | R-057, R-061 | Engine-verified. Two anchoring triples. Row corrected 2026-07-02: the previous statement `e_{12} e_{13} e_{23} = −e_4` was the stale pre-γ-5 error (engine: `+1`); paper §D.2.3 was already correct — the Index row had not been synced. |
| R-098 | Anti-self-dual generation triple `{e_{12}+e_{34}, e_{13}−e_{24}, e_{14}+e_{23}}` engine-exact | DERIVED-A | anti_self_dual + self_dual + self_dual_blade + chiral_split_demo + spin4_generator_count | D.2 | R-009 | R-071, R-077 | Hosts ℍ ≅ ASD bivectors. |
| R-099 | SD ↔ ASD mirror under spatial parity (engine-exact) | DERIVED-A | self_dual + anti_self_dual + duality_map + chiral_split_demo | D.2 | R-098 | R-077, R-079 | Underwrites up/down mirror. |
| R-100 | Grade dictionary (load-bearing reference) | DERIVED-A | spatial_vs_phase_partition + wave_E_complex_structure + wave_E5 + spin4_generator_count | D.2 | R-009, R-010, R-098 | (downstream Cl-typed claims) | Full lookup. |
| R-101 | D4 lattice: kissing number 24 (densest 4D packing, Cohn-Kumar 2017) | INPUT (premise A-1b unpacked) | — | D.3 | A-1b | R-103, R-104 | Empirical. |
| R-102 | Monad as unit Clifford rotor `R_i ∈ S³ ≅ SU(2) ≅ Spin(3)` at each D4 site | FRAMING | s0 + spinor_real_dof | D.3 | R-101, R-012 | R-103, R-110 | Substrate building block. |
| R-103 | J + D coupling structure: symmetric exchange on 24 NN bonds + DM on 12 `e_4`-bonds; parity assignment structural | DERIVED-STRUCTURAL (structure) + INPUT (ratio) | D4_spatial_bond_isotropy + D4_DM_bond_bivectors_non_commuting + dressed_coupling + DoverJ_from_lepton_masses | D.3 | A-1c, R-101, R-102 | R-107, R-108 | The unique pair allowed by parity on D4. |
| R-104 | 24-bond 12+12 split: 12 spatial + 12 `e_4`-bearing | DERIVED-A | D4_spatial_bond_isotropy + D4_DM_bond_bivectors_non_commuting | D.3 | R-101 | R-083 | Underwrites §C.4. |
| R-105 | Two-scale framework FORCED (Planckian monad layer + emergent hadronic cell layer) | DERIVED-STRUCTURAL | — | D.3 | R-037, A-1c | R-039, R-119 | Without it, framework self-contradictory at G/hadron interface. |
| R-106 | Magnon kinetic stiffness identifies `f_π² = 8J/a` | DERIVED at dressed-coupling | f_pi_squared + sigma_model_kinetic_normalization | D.4 | R-103 | R-051 | Condensate identification (T0b.2). |
| R-107 | Skyrme stabilizer relation `e ≈ √18/(D/J) ≈ 5.37` (dressed-coupling) | DERIVED at dressed-coupling | dressed_coupling + kappa_F_bare + spiral_angle_deg | D.4 | R-103 | R-051, R-074 | Geometric-coincidence caveat noted (per V2 §10.3.3). |
| R-108 | Luttinger-Tisza canted-helix transition; canting cos q ≈ 0.983 at D/J ≈ 0.79 | DERIVED-A | canting_pitch_q_rad + canting_cos_q + canting_critical_stiffness_at_DJ + Kc_magnon_stiffness_canted_FM_at_DJ + n_goldstone_canted_FM | D.4 | R-103 | R-055, R-117 | Substrate-side ground state. |
| R-109 | Skyrme Lagrangian with determined coefficients (full medium Lagrangian) | DERIVED at dressed-coupling | skyrme_BVP_audit + sigma_model_kinetic_normalization | D.4 | R-106, R-107, R-108 | R-051 | Standard ANW phenomenology applies. |
| R-110 | DM-induced topological boundary term `𝓛_top = µ Ψ_0 ρ_L` | DERIVED form (coefficient µ OPEN) | DM_operator_gaussian_dim | D.4 | R-103, R-102 | R-090 | Source of β-decay channel. |
| R-111 | `1/Θ_0 ≈ 196 MeV ~ Λ_QCD` as CANDIDATE for QCD scale identification | CANDIDATE | nuclear_length_hierarchy + qcd_uv_conformal_phaseCD | D.4 | R-106, R-103 | — | Identification not closed. Was ≈215 before the R-133 Θ₀-coefficient correction (2026-07-03); stays in the Λ_QCD range (scheme caveat: closer to folk ≈200, farther from Λ^(5)_MSbar ≈ 210 — no strengthening claimed). |
| R-112 | Master wave equation and its three faces — linear, topological, collective | DERIVED-STRUCTURAL | wave_E_complex_structure + wave_E5 + eom_constraint_class | D.4 | R-106, R-103, R-007 | R-117, R-118 | Three faces of one EOM. |
| R-113 | Memory effect — mechanism on driven D4 substrate | FRAMING | eom_compatible_field_forks + eom_invariant_variant_audit | D.5 | A-2, R-112 | R-114, R-115 | The substrate kernel's role. |
| R-114 | Monostability theorem: Newtonian (memoryless) kernel forbidden | DERIVED | eom_compatible_field_forks | D.5 | R-113 | R-115 | Defect persistence is incompatible with instant relaxation. |
| R-115 | Rich/hysteretic kernel ADOPTED on physical motivation (defect persistence); fading-vs-hysteretic is #1-gap GATED | CANDIDATE (committed by choice) | eom_compatible_field_forks | D.5 | R-114, A-2 | R-118 | W-LIVE-3. Leans hysteretic — but N46 (W3.3/A1) shows this "lean" is a LARGE-BARRIER-regime effect, NOT a clean-symmetry result: the SNIC escape is governed by kernel numbers non-monotonically, a small barrier PROMOTES it. |
| R-116 | Three roles of memory: cell formation; Role-3 (selection); Bell-pair memory | FRAMING + value-gated | im_chi_falsifier_budget_KSS_GW_macromolecule + identify_the_floor | D.5 | R-113 | R-030 | One kernel, three faces. |
| R-117 | Linear face structurally safe — leak-independence, symmetry-protected unitarity, Goldstone-protected decoherence (WP-IX3/IX4/DC2) | DERIVED-STRUCTURAL | eom_invariant_variant_audit + interference_can_reduce_mass_goldstone + identify_the_floor + massless_H_squared + protection_mechanism_located | D.5 | R-112, R-108 | R-023, R-027 | Why QM and Bell are unaffected by which side of memory fork wins. |
| R-118 | Θ_rel as highest-value target — coset-Cartan FDT-violation residual ties colour-U(3), CKM-P, memory fork, SOC coupling | FRAMING + #1-gap-gated | theta_rel_universality_located + theta_rel_pinnability_from_data + theta_rel_equivariant_bifurcation_spine + theta_rel_rotating_wave_escape_located + theta_rel_fork_escape_kernel_number_governed + theta_rel_z3_isotropy_dichotomy + colour_relative_phase_is_coset + colour_quartic_charge_handle + colour_abare_static_holomorphic + colour_arich_kernel_dependent | D.5 | R-115, R-053, R-073, R-081 | R-119 | Z3-breaking shared condition derived (engine-exact); single kernel value gating four faces is candidate. |

---

## Part E — Cosmology, status, frontiers

| ID | Statement | Tier | Engine | § | Deps | Used by | Notes |
|---|---|---|---|---|---|---|---|
| R-119 | Cosmological constant `Λ ~ H²` residual is the driven-dissipative deviation from Volovik equilibrium (value-gated, #1-gap-routed) | FRAMING + value-gated | gravitating_vacuum_energy + lambda_resolution_structure | E.1 | R-047, R-115 | — | Canonical falsifier §E.3 VG-2. |
| R-120 | Multi-defect well-posedness of the wavefront field equation as structural-coherence condition (not currently testable since EOM unformulated) | FRAMING + coherence-condition | — | E.1 | A-2, R-053 | — | Canonical falsifier §E.3 SC-1. |
| R-121 | Three sterile right-handed neutrinos as parameter-free DERIVED prediction (B−L conservation forces Dirac character; RH partner is `S_−`) | DERIVED | sterile_rh_relic_check | E.1 | R-089, R-076 | R-122 | Structural; engine-banked. |
| R-122 | Sterile RH relic ~2% of Ω_DM (47× shortfall vs needed); ~98% out of TWT V2 derivational scope | LOCATED-GAP | sterile_rh_relic_check + sterile_rh_z2_separate_mass_scale_check + sterile_rh_substrate_production_via_L_theta | E.1 | R-121 | — | Canonical falsifier §E.3 VG-4. Z1/Z2 LOCATED-GAP-REFINED; Z3 still OPEN. Lead (i) differential coupling and (ii) wave-train phase-defect remain OPEN. |

---

## Coverage check (Phase α-7 to verify in detail)

**Engine primitive coverage.** Every engine name in the *Engine* column above must exist in
`twt.py`. Phase α-7 runs the cross-check; the full primitive list is at
`scratchpad/twt_primitives.txt`.

**V2 result coverage.** Every load-bearing V2 result should map to an R-NNN or to a paper-only
synthesis result that doesn't need an R-NNN. Phase α-7 walks V2 §-by-§ to catch orphans.

**Falsifier cross-references.** §E.3's four tables reference the R-NNN above; the canonical
falsifiers from V2 §25.2 are:

- *Named near-term* (17 rows): UHE-CR LV (R-039 / R-016), `α_3` (R-039), `c_GW = c_γ` (R-039),
  proton decay (R-054), `0νββ` (R-089), Geneva influence speed (R-031), Bell-foliation (R-031),
  differential `c_meta` (R-045), optical-clock decoherence (R-117), macromolecule decoherence
  (R-030), CHSH > 2√2 (R-027), monopole (R-033), fractional charge (R-062), top baryon (R-091a),
  4th generation (R-071), TRULY-independent `θ_C` (R-073), tree FCNC (R-061).
- *Removed*: chiral matter wrong-sign gravity (R-040), `ξ = 1/6` cancellation (R-041), Koide
  modus-tollens (R-061 family), Cabibbo f_perp (R-073 family), V_PMNS=I phantom (resolved
  per V2 Phase C; no R-NNN — defused prediction), nu-asymmetric (resolved per V2 Phase D; no
  R-NNN), over-production test (R-091 via `topological_overproduction_test`).
- *Value-gated*: VG-1 Im χ budget (R-030), VG-2 Λ ~ H² (R-119), VG-3 1/T_2 (R-117), VG-4 dark
  matter (R-122), VG-5 GW dispersion (R-039).
- *Structural coherence*: SC-1 multi-defect (R-120), SC-2 cell-order (R-016).

---

## Editorial reminder

- A row with **no engine cite** (`—`) is *paper-only*. That is honest if the result is kinematic
  or synthesizing (e.g. R-022 self-adjointness from Cl reversion; the proof is two lines of algebra
  and is best stated in the body). It is **dishonest** if the row claims an engine-verified
  derivation without one. Phase α-7 grep `Engine: —` and audit each case.
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
(Sakharov Λ² comes from 4D), R-071 (Frobenius classification has ℝ, ℂ, ℍ only — ℍ-units identified
with generations), R-092 (Cl(4,0) ≅ M₂(ℍ) by Bott periodicity).

### A-1b — D4 cell lattice
Direct consequences: R-083 (24-bond count), R-101 (kissing number 24), R-104 (12+12 spatial /
e_4-bearing split). Inheritor of the lemma that ties §C.4's `sin²θ_W = 3/8` to D4 isotropy
(through R-082's `g_1 = g_2`).

### A-1c — J + D bond couplings
Direct consequences: R-007 (mass = meta-time rotor frequency, sustained by drive), R-055 (electron
QCP scaling — D/J near `D = J` critical point), R-068 (Brannen `δ_L` from D/J), R-070
(δ_L from chiral-ℤ_3 potential), R-103 (coupling structure), R-107 (Skyrme stabilizer at dressed
coupling), R-108 (Luttinger-Tisza canted state), R-110 (DM-induced topological boundary term).

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
- **R-015** (Lorentzian signature = algebraic shadow) ← R-013 + R-014, **one of two cleanest spine results**

### 1.3 Special relativity
- **R-017** (Klein–Gordon via Fourier at `k_4 = m`) ← R-007 + R-013
- **R-018** (Lorentz generators K_j, J_i; so(1,3) closure) ← R-013
- **R-019** (Thomas precession sign) ← R-018

### 1.4 QM postulates
- **R-020** (Born subspace `{1, B}` forced by centralizer intersection) ← R-009 + R-012
- **R-021** (Postulate 1: complex Hilbert) ← R-020
- **R-022** (Postulate 2: self-adjointness as `M̃ = M`) ← R-021
- **R-023** (Postulate 3: Born even-power) ← R-021, structural + plausibility-modulo-degree
- **R-024** (Postulate 4: Schrödinger from KG envelope) ← R-017 + R-021
- **R-025** (Postulate 5: spin-statistics SELECTION + Spin(4) consistency) ← R-011 + R-012
- **R-026** (Dirac equation from KG factorization) ← R-013 + R-017 + R-012

### 1.5 Bell, Tsirelson, non-separability
- **R-027** (Tsirelson `S = 2√2`) ← R-011 + R-023, **engine-exact**
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
- **R-063** (charge quantization `|Q_p| = |Q_e|`) ← R-062, **second cleanest spine result**
- **R-064** (Brannen amplitude form from V_4⊥ projection) ← R-009
- **R-065** (√2 factor forced by 3D projection) ← R-064
- **R-066** (Koide K=2/3 ⇔ c=√2 Brannen-Koide equivalence) ← R-064 + R-065
- **R-067** (Foot 45° characterization) ← R-066
- **R-087** (B − L anomaly cancellation from 3 × 1/3 = 1) ← R-057
- **R-088** (BPST + index ⇒ ΔB = ΔL = N_gen) ← R-087
- **R-097** + **R-098** + **R-099** (Cl-grade dictionary, as above)

### 1.8 Gauge group from D4 orbits
- **R-078** (substrate carriers of SM gauge content) ← R-009 + R-010
- **R-080** (U(1)_Y from I_4 + bivector compactness) ← R-056 + R-010
- **R-081** (colour octet 8 = 3 ⊕ 5 split; C_A/C_F = 9/4) ← R-053 + R-072
- **R-082** (`sin²θ_W = 3/8` at unification) ← R-056 + R-062 + R-079 + R-080 + R-009, **engine-exact, headline result**
- **R-083** (24-bond count; SU(5) labeling as translation only) ← A-1b

### 1.9 Cosmology / macroscopic limit kinematic results
- **R-029** + **R-044** + **R-046** + **R-048** + **R-049** + **R-050** — all kinematic
  consequences of Cl(4,0)'s structure plus A-3 (signature locking)

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
- **R-035c** (length-ladder algebraic identity `r_e · a_0 = λ̄_C²`) — DERIVED-A at Layer 1;
  doesn't depend on α's value.
- *Same single-dial logic ties α_s and α_W to α through `Im χ`*: §C.5 / §D.5 narrative. The
  framework's four SM EW couplings collapse to one Layer-2 magnitude.

### 2.2 Gravity
- **R-037** (Sakharov induced EH) — DERIVED-generic-given-4D, magnitude bracketed `Λ ∈ [0.16, 0.72] M_Pl`; absolute coefficient `Im χ`-gated
- **R-040** (induced G sign) — sign DERIVED via spin-2 spectral positivity (Layer-1 reasoning), magnitude #1-gap-gated
- **R-041** (ξ = 0 at leading order) — via Maurer–Cartan shift symmetry (engine tier: FRAMING+CONDITIONAL; Layer-1), residual ξ ~ (f_π/Λ)² ~ 10⁻⁴⁰–10⁻³⁹ is dimension-6 gated
- **R-042** (texture tetrad) — structural geometry CLOSED conditional; absolute coefficient OPEN; 6→4 frame reduction BANKED structural (R-145, 2026-07-05 — residue: the signature pick + U2); Gauss-equation face EXECUTED (R-149, 2026-07-05 — Riem(g) algebraic in (E, Ω, dE), scaffold closed; C_T residue = the kernel's mode measure alone)

### 2.3 Strong sector
- **R-085** (no fundamental SU(3)_c; colour as elastic-response) — structural; β_3 sign LOCATED-GAP (named re-attack `beta3_sign_from_reflection_positivity`)
- **R-111** (1/Θ_0 ~ Λ_QCD) — CANDIDATE identification
- **R-118** (Θ_rel as highest-value target) — derived shared-condition; single-kernel-value gating four faces is CANDIDATE

### 2.4 Substrate dynamics core
- **R-113** / **R-114** / **R-115** (memory effect; monostability theorem; rich/hysteretic ADOPTED) — all FRAMING/CANDIDATE, #1-gap structure
- **R-116** (three roles of memory) — FRAMING + value-gated
- **R-117** (linear face structurally safe) — DERIVED-STRUCTURAL (this is why QM and Bell are unaffected by A-2 closure)

### 2.5 Cosmological constant
- **R-119** (Λ ~ H² residual) — driven-dissipative deviation from R-047 Volovik equilibrium; #1-gap-gated

### 2.6 Mass spectrum at value
- **R-051** (Skyrme `M_0 = 36.47 f_π/e`) — DERIVED at dressed-coupling
- **R-055** (electron QCP scaling) — DERIVED-CONDITIONAL on four named identities; L2 mechanism unidentified
- **R-068** (three lepton mass ratios at δ_L = 12.73°) — FIT post WP-MASS-MEASURE (forward derivation REFUTED in V2 Phase F)
- **R-074** (cross-sector D/J over-determination) — DERIVED-CALIBRATED (the genuine over-determination signal)

### 2.7 Dark sector
- **R-121** (3 sterile RH neutrinos) — DERIVED
- **R-122** (sterile RH ~2% Ω_DM relic; ~98% out of V2 scope) — LOCATED-GAP

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
PMNS, neutrino masses, σ_QCD, τ_mem, Bell-pair memory.

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

*Which twt.py primitive is the witness for which §; which twt_test.py check verifies which result.*


*Version 3 · Phase α draft · 2026-06-30.*
*Cross-reference between `twt.py` engine primitives, `twt_test.py` checks, and V3 paper sections.
For every engine primitive: which §/R-NNN cites it, and which test (if any) verifies it.
For every V3 §: which engine primitives carry its claims.*

---

## How to read this file

Two views of the same content:

- **View A — engine-keyed.** Every `twt.py` primitive listed alphabetically, with the V3 § that
  cites it (via R-NNN) and the `twt_test.py` line that verifies it.
- **View B — section-keyed.** Each V3 § with its engine primitives, organized by R-NNN
  appearance order.

Phase α-7 audit task: verify that every R-NNN engine cite in Section 1 (Result Index) is
either (a) listed in View A here, or (b) a primitive that exists in `twt.py` and gets added to
View A. No phantom cites (CLAUDE.md §2).

---

## View A — engine-keyed (primitive → V3 §, R-NNN, test)

*Total primitives in `twt.py`: 323 as of 2026-07-27 (297 public + 26 helpers prefixed `_`; refresh this count+date at each banking pass). The table below lists the
~150 load-bearing primitives that V3 R-NNNs cite directly. Helpers and not-cited primitives are
listed in §View A.Δ at the bottom for completeness.*

| Primitive | V3 § | R-NNN | Test |
|---|---|---|---|
| B_minus_L_anomaly | C.5 | R-087, R-089 | twt_test.py |
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
| G_generator | C.3 | R-072 | twt_test.py |
| I4_maps_L_to_Q | A.3, A.5, C.5 | R-005, R-010, R-090 | twt_test.py |
| I4_squared | A.5, C.4 | R-010, R-080 | twt_test.py |
| induced_G_from_linear_face_band | B.6.2 | R-163 | twt_test.py |
| Kc_magnon_stiffness_canted_FM_at_DJ | D.4 | R-108 | twt_test.py |
| L_Q_orthogonal_decomposition | A.5, B.8, C.4, D.2 | R-009, R-049, R-078, R-097 | twt_test.py |
| L_algebra_su2_closure | D.2 | R-097 | twt_test.py |
| alpha_em_meaning | B.5b | R-035a, R-035c | twt_test.py |
| alpha_em_value | B.5b, D.5 | R-035a (raises until #1-gap closes) | twt_test.py expects raise |
| alpha_H_gap | C.5 | R-091a | twt_test.py |
| anti_self_dual | D.2 | R-098, R-099 | twt_test.py |
| B_minus_L_anomaly | C.5 | R-087, R-089 | twt_test.py |
| baryon_mass_shared_rotor_nonadditive | C.1 | R-053 | twt_test.py |
| bell_correlation | B.4 | R-027 | twt_test.py |
| beta3_sign_from_reflection_positivity | E.2, Layer-3 | (located re-attack) | twt_test.py (located-gap bank) |
| bivector_inner_product | A.5 (background) | (kinematic) | twt_test.py |
| born_subspace_one_B_forced | B.3 | R-020, R-021 | twt_test.py |
| boost | B.2 | R-018 | twt_test.py |
| bpst_charge_Q | C.5 | R-088 | twt_test.py |
| bpst_selection_rule | C.5 | R-088, R-089 | twt_test.py |
| brannen_amplitude | C.3 | R-064, R-068 | twt_test.py |
| cabibbo_angle_rad | C.3 | (deprecated — returns δ_L, not a Cabibbo angle; removed from R-073's cites 2026-07-02) | twt_test.py |
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
| kernel_overdetermination_table | — (companion §4/§12; not paper-body) | R-150 | twt_test.py (check_twt_algebra) |
| kernel_candidate_constraints | — (Phase B/B1; companion §12; candidates/2026-07-05_phaseB memo) | (Phase B) | twt_test.py (check_twt_algebra) |
| single_relaxation_family_exclusion_probe | — (Phase B/B2; candidates/2026-07-05_phaseB memo) | (Phase B) | twt_test.py (check_twt_algebra) |
| d4_langevin_calibration_gate | — (Phase B/B3; candidates/2026-07-05_phaseB memo) | (Phase B) | twt_test.py (check_twt_algebra) |
| static_susceptibility_sumrule_and_kss_channel_mismatch | — (ledger N43; companion §4) | N43 | twt_test.py (check_twt_algebra) |
| stress_tensor_shear_channel_static_moment | — (ledger N47; companion §12 ceiling) | N47 (A3) | twt_test.py (check_twt_algebra) |
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
| koide_K | C.3 | R-064, R-066 | twt_test.py |
| koide_charge_unification | C.3 | R-066 | twt_test.py |
| koide_from_c | C.3 | R-064, R-066 | twt_test.py |
| lambda_resolution_structure | B.7, E.1 | R-047, R-119 | twt_test.py |
| lepton_number_topological_conservation | C.1, C.5 | R-054, R-089, R-090 | twt_test.py |
| macroscopic_LQ_split | B.8 | R-048, R-049 | twt_test.py |
| mass_measure_from_omega | C.3 | R-068 (Brannen δ_L chain; CANDIDATE-strong) | twt_test.py |
| massless_H_squared | D.5 | R-117 | twt_test.py |
| matter_stability_outside_frame | A.2, A.3, B.1 | R-003, R-004, R-016 | twt_test.py |
| maxwell_four_laws | B.5 | R-032 | twt_test.py |
| maxwell_grade_structure | B.5 | R-032, R-033 | twt_test.py |
| mermin_klyshko_value | B.4 | R-028 | twt_test.py |
| mermin_value | B.4 | R-028 | twt_test.py |
| n_goldstone_canted_FM | D.4 | R-108 | twt_test.py |
| neutrino_lightness | C.3 | R-076 | twt_test.py |
| nonuniform_orbit_baryon_model | C.1 | R-053 | twt_test.py |
| nuclear_length_hierarchy | C.5, D.4 | R-091b, R-111 | twt_test.py |
| over_determination_scan | C.3 | R-074 | twt_test.py |
| photon_strain_mode | B.5 | R-035 | twt_test.py |
| phase_to_h_unit_map_located_residual | C.3 | R-071 | twt_test.py |
| pi3_S3_integer_completion | A.2, A.3, C.1, C.5 | R-002, R-006, R-052, R-054, R-084, R-089 | twt_test.py |
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
| top_excluded | C.5, E.3 row 14 | R-091a | twt_test.py |
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
| wave_E5 | D.1, D.2, D.4, C.5 | R-007, R-091, R-100, R-112 | twt_test.py |
| wave_E_complex_structure | A.4, D.2, D.4, C.5 | R-007, R-091, R-100, R-112 | twt_test.py |
| weak_isospin_SD_parity_exclusion | C.2, C.4 | R-060, R-079 | twt_test.py |
| weak_isospin_centralizer_is_SD | C.2, C.4 | R-061, R-079 | twt_test.py |
| weak_isospin_rank_table | C.4 | R-079 | twt_test.py |
| weak_isospin_verdict | C.4 | R-079 | twt_test.py |
| weak_isospin_zero_on_generations | C.2 | R-061 | twt_test.py |
| weinberg_sin2 | C.4, B.5b | R-082, R-035b | twt_test.py (load-bearing test, engine-exact 3/8) |
| why_three_generation_triple | C.3 | R-071 | twt_test.py |
| winding_charge | C.2, C.4 | R-056, R-063, R-080 | twt_test.py |
| worldline_bivector | B.8 | R-048 | twt_test.py |
| x_Q | C.5 | R-091a | twt_test.py |

### View A.Δ — primitives not cited by any V3 R-NNN

The following ~110 primitives exist in `twt.py` but are not directly cited by an R-NNN in V3.
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
`e`, `e4_acts_as_identity_on_Splus`, `e4_conjugation_is_LQ_not_updown`, `e_i4_squares_to_minus_one`,
`epicycle_reading_dependent`, `epicycle_reading_resolved`,
`gate_B_branch`, `gear_eigenvalues`, `gear_inertia_form_from_S2_symmetry`, `gell_mann_okubo_gamma`,
`generation_cost_step_structure`, `generation_gen2_chirality_mirror`,
`generation_index_survives_brannen_excision`, `generation_ladder_needs_inverse_square`,
`generation_loose_windows_vacuum_relative`, `generation_subharmonic_ladder`,
`generation_values_monad_forked`, `generations_are_defect_flows_on_spinor_S3`,
`geometric_ladder_is_nonselfadjoint`,
`heavy_baryon_predictions`, `hierarchy_type`, `hodge_split_invariance_theorem`,
`i4_generation_overdetermination`, `i4_lepton_quark_amplitude_blind`,
`induced_G_gate_A_linearized_sufficient`, `induced_G_knowability_verdict`,
`koide_modus_tollens_consistency`, `mass_operator_form`, `mass_reconciliation_U1_Spin3`,
`meson_dynamical_current_split`, `meson_topological_status`,
`metatime_brannen_vs_v4perp_projection_reach`, `metatime_generation_operator`,
`neutrino_orbit_asymmetry_attempt`, `numerical_chain`,
`phase_D_colour_updown_blind`, `pmns_no_substrate_derivation`, `pure_L_rotor_preserves_spatial_radius`,
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
- R-002: `pi3_S3_integer_completion`
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
- R-016: `equivalence_principle_protection`, `matter_stability_outside_frame`

### §B.2 Special relativity
- R-017: `wave_E_complex_structure`
- R-018: `boost`, `rotation`, `so13_closure_signs`
- R-019: `thomas_KK`
- R-123: `defect_rotor_frequency_reads_as_k4_on_front` (2026-07-02 keystone bridge, §B.2.1)

### §B.3 Quantum mechanics from one move
- R-020: `born_subspace_one_B_forced`
- R-021–R-024: `born_subspace_one_B_forced` (subspace), no direct (postulates 2 + 4 are paper-only)
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
- R-035c: `alpha_em_meaning`
- R-162: `coupling_sector_channel_disjointness` — EM vs colour channels provably disjoint; the α_s fold-in located, not derived

### §B.6 Gravity
- R-036: paper-only structural
- R-037: `sakharov_induced_gravity`, `induced_G_bracket_mode_count`,
- R-163: `induced_G_from_linear_face_band` — I-3 narrowed to OA-LF-i ∧ OA-LF-ii; the flat-band measure derived
- R-164: `skyrme_quartic_contains_no_tree_EH` — no tree-level EH in the banked action class (ledger N51)
  `induced_G_only_monad_scale_enters`, `induced_G_leading_coefficient_mass_independent`,
  `induced_G_quadratic_divergence_from_4D`
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
- R-044: paper-only (three asymmetries unified)
- R-045: paper-only (c_meta = c on average)
- R-046: paper-only (Hubble radius identification)
- R-047: `gravitating_vacuum_energy`, `lambda_resolution_structure`

### §B.8 The macroscopic limit
- R-048: `macroscopic_LQ_split`, `worldline_bivector`, `polar_moment_of_inertia`
- R-049: `macroscopic_LQ_split`, `L_Q_orthogonal_decomposition`
- R-050: paper-only (Sundman + Cauchy-Schwarz)

### §C.1 The Skyrmion
- R-051: `skyrme_BVP_audit`, `skyrmion_mass_MeV`, `skyrme_length_fm`
- R-052: `pi3_S3_integer_completion`
- R-053: `nonuniform_orbit_baryon_model`, `cogear_linkage_kinematic`,
  `baryon_mass_shared_rotor_nonadditive`, `e4_content_confines_quarks_not_leptons`
- R-054: `pi3_S3_integer_completion`, `lepton_number_topological_conservation`
- R-055: `electron_two_windings`, `electron_QCP_nu`, `electron_f_L_MeV`

### §C.2 Charges and the first generation
- R-056: `hypercharge`, `doublet_hypercharge`, `winding_charge`
- R-057: `gmn_coefficient`, `triple_product_Q`, `triple_product_color`
- R-058: `doublet_hypercharge`
- R-059: `universality_theorem`
- R-060: `weak_isospin_SD_parity_exclusion`, `vminusa_is_spin4_factor_chirality`
- R-061: `weak_isospin_zero_on_generations`, `weak_isospin_centralizer_is_SD`
- R-062: `gmn_coefficient`, `generation_spectrum`
- R-063: `winding_charge`, `gmn_coefficient`, `generation_spectrum`,
- R-159: `charge_normalization_anchor_free` — Q_p + Q_e = 0 identically in c given (P4,P5,P6); neutrality import conditionally retired
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
- R-079: `weak_isospin_SD_parity_exclusion`, `weak_isospin_centralizer_is_SD`,
  `weak_isospin_verdict`, `weak_isospin_rank_table`, `vminusa_is_spin4_factor_chirality`
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
- R-091: `wave_E_complex_structure`, `wave_E5`, `topological_overproduction_test`
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

### §D.3 The D4 monad layer
- R-101: no direct engine cite (D4 packing fact is INPUT premise A-1b)
- R-102: `s0`, `spinor_real_dof`
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
- R-119: `gravitating_vacuum_energy`, `lambda_resolution_structure`
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
| Cosmological constant residual `Λ ~ H²` | GATED + falsifier-testable | R-119 | `gravitating_vacuum_energy`, `lambda_resolution_structure` | Driven-dissipative deviation from Volovik equilibrium. §E.3 VG-2. A candidate kernel FORM exists (§E.5, R-153); the coefficient stays gated. |
| Macromolecule-interferometry decoherence (KSS-floor to GW170817-ceiling bracket) | GATED + falsifier-testable | R-030 | `im_chi_falsifier_budget_KSS_GW_macromolecule` | One dial, two operational windows (Bell + macromolecule). §E.3 VG-1. |

---

## Gated on `Θ_rel` (the FDT-violation residual; structural gate 3.3 + dynamics)

| Item | Tier | R-NNN | Engine | Notes |
|---|---|---|---|---|
| Colour-U(3) → SU(3) breaking magnitude | GATED | R-081, R-118 | `colour_relative_phase_is_coset`, `colour_quartic_charge_handle`, `colour_abare_static_holomorphic`, `colour_arich_kernel_dependent` | Z3-isotropy-dichotomy direction derived; magnitude #1-gap-gated. |
| CKM hierarchy + Jarlskog | GATED | C.3 context | `ckm_arc_channel_identity_and_verdict`, `ckm_arc_circulant_linchpin`, `ckm_arc_sector_and_corotation`, `ckm_hierarchy_and_cp_seed` | Frequency-ratio `|V_us|² = m_d/m_s` (R-073) is CANDIDATE; full hierarchy requires Θ_rel closure. |
| Asymptotic-freedom `β_3 < 0` sign | LOCATED-GAP | R-085 | `beta3_sign_from_reflection_positivity` | Reflection positivity bounds bare coefficient sign, sign-agnostic on running. Re-attack via c/a-theorem analogue on marginal-Skyrme RG flow. |
| Coupling-universality (SOC) | CANDIDATE | — | — | Gemini-originated speculation; not yet implemented. Would give a-priori reason `g_1 = g_2 = g_3` at substrate scale. |
| Θ_rel kernel value itself | #1-gap-gated | R-118 | `theta_rel_*` family (located-gap banks) | Single highest-value target in the framework. |

---

## Gated on absolute ω scale

| Item | Tier | R-NNN | Engine | Notes |
|---|---|---|---|---|
| `f_π` absolute MeV (currently INPUT 129) | INPUT | A-1c, R-106 | `f_pi_squared` | Could become GATED-then-derived under §D.5 closure. |
| `M_0` baryon mass at dressed coupling | DERIVED at dressed-coupling | R-051 | `skyrmion_mass_MeV`, `skyrme_BVP_audit` | `M_0 = 36.47 f_π/e`. Absolute number gated on `f_π`. |
| `1/Θ_0 ≈ 196 MeV` CANDIDATE for `Λ_QCD` | CANDIDATE | R-111 | `nuclear_length_hierarchy`, `qcd_uv_conformal_phaseCD` | Identification owed; mechanism not closed. (Was 215 pre-R-133 correction; stays in the Λ_QCD range — scheme caveat, no strengthening claimed.) |
| `m_e` via L-orbit QCP scaling | DERIVED-CONDITIONAL | R-055 | `electron_f_L_MeV`, `electron_QCP_nu` | 35% on `f_L`, 4.5% in exponent. L2 mechanism unidentified. |
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
| `ν = 3π/2 = 4.712` anomalous dimension match (0.34%) | CANDIDATE | R-055 | `electron_QCP_nu` | Mechanism unidentified. Would unblock electron mass derivation. |
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
| `f_π` | ≈ 129 MeV | Cell-scale mass scale; condensate-identified |
| `Λ` | Planckian within O(1) | Substrate cutoff; §B.6 bracket `[0.16, 0.72] M_Pl` |
| `D/J` | ≈ 0.79 | Chirality ratio; calibrated to leptons; cross-checked by baryons (R-074 over-determination) |
| `c = √2` ⇔ `K = 2/3` | exact (10⁻⁵) | Brannen phase coefficient. Six forcing routes investigated NEGATIVE. |
| `A` (lepton amplitude scale) | empirical | Free Koide calibration; cancels in ratios |
| `weak = SD` | one bit | The chiral Spin(4) factor (neutrino-forced) |

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
couplings and the `Cl(4,0)` rotor algebra. The fundamental Planckian monad layer is the
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
geometric-algebra formulation directly. The no-monopoles result is the same status as `∇·B = 0`
in standard EM — a consequence of `F` being a bivector with vector source `J`. What TWT *adds*
is a structural reason for the field/source grading: `F` is grade-2 because EM acts on observers
via the spatial bivectors `γⁱ = e_4 e_i` of §A.5; the wavefront current `J` is grade-1 because
it is the wavefront projection of the soliton's substrate-level *bivector winding*. And
grade-1 + grade-3 are the only grades produced by `∇F` with `F` bivector. "No magnetic
monopoles" in TWT comes with a substrate-level derivation of the field grading itself, not just
the standard Maxwell consequence.

### Catalog item 5 — `α` as a reactive grade-0 Clifford invariant (§B.5b)

Numerically `1/α = 137.036` is what QED measures; TWT does not change it. **Reinterpretation:**
the `α`-object is identified as

> `α-object = ⟨Σ̃_F · Γ_recon · Σ_L⟩_0`,

the grade-0 projection of a geometric product in `Cl(4,0)`: `Σ_L` is the L-orbit bivector
winding, `Σ_F` is the photon bivector-strain mode, and `Γ_recon` is the §B.1 wavefront-locking
reconversion. This is a **reactive grade-0 Clifford invariant** — representation-independent,
picking out the common bivector content of the L-orbit field and the EM strain. Type-B (analytic
at coupling, no `exp(−S)` essential singularity; the probability ↔ action lens of tunneling does
not apply to `α`). The **length ladder** `r_e = α λ̄_C`, `a_0 = λ̄_C/α`, `r_e · a_0 = λ̄_C²` is a
coherence success — one geometric overlap underlies three independently-measured lengths — not
a value over-determination (`α` cancels in `r_e · a_0 = λ̄_C²`, an algebraic identity).
**Magnitude #1-gap-gated** via `Im χ`; what's DERIVED is the *ontology* (what `α` *is*), the
*category* (reactive Type-B), and the *coherence* (one object, several roles).

### Catalog item 6 — Frobenius generation count (§C.3.8)

Numerically standard mathematics: only `ℝ`, `ℂ`, `ℍ` are finite-dimensional associative real
division algebras. **Reinterpretation:** TWT identifies the three generations with the three
imaginary units of `ℍ` on the `V_4⊥` generation circle, and uses Frobenius to forbid enlargement
to a fourth-generation algebra. The theorem is unchanged; what TWT supplies is the
*identification* that turns it into a generation-count theorem.

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
topological defect — a vortex in the canted FM ground state's residual `S¹`, equivalently a
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
  the named near-term (17 at V3 issue; 18 since R-159) + 7 removed + 5 value-gated + 2 structural-coherence falsifiers at
  §E.3 alone. No falsifier sits forgotten in the middle of the paper.
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
rows' own kill conditions (floor, not ceiling); row 10 / VG-1 Bell-memory-bridge cites
§B.4.4 → §B.4.5; RF-5/RF-6 grouping sentence corrected (RF-6 is an adjudicated negative, not
a clarified-status removal); `2 × 36.462 = 72.923` → `≈` (last-digit rounding); the
`#1-gap-gated.`-at-column-0 line starts re-wrapped (fragile in permissive Markdown); §C.1.6's
9/2 counting and the C.1.6 status sentence now carry the `K_c = (2/19)·J` conditionality the
engine records (DERIVED-conditional, not unconditional).

The full audit note (first pass + workflow findings) is archived at
`knowledge/audit/paper_audit_note_2026-07-26.md`.

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
| `(≥ 2, 0)` | bound nuclei (up to Fe stable, above unstable) | ✓ |
| Negative `B, L` | antiparticles (all above) | ✓ |

**The topologically stable set is `{γ, p, e, ν, stable nuclei, antiparticles}` — precisely the
observed stable spectrum. No orphans, no gaps.**

Two structural reasons underwrite this:

- (i) **TWT carries *exactly* the SM's two topological charges** — `B` in `π_3(S³_𝓠)` and `L` in
  `π_3(SU(2)_L) ≅ ℤ` on the L-orbit (§C.1, §C.5). Not one, not three; exactly two.
- (ii) **Internal multiplicity is capped at three** — three colours (Q-orbit trivectors,
  §C.4.1) and three generations (Frobenius ℍ-units, §C.3.8) — by the 4D `ℤ_3` structure of
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
`N ≈ 10³¹` (proton, `Γ < ~10⁻³⁴ s⁻¹`). **Nine orders of magnitude in `N`, parameter-free.**

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

## Foundational geometric algebra & Clifford

- **Hestenes, D.** (1966). *Space–Time Algebra*. Gordon and Breach. — Foundational reference for
  the Clifford-algebra formulation of Dirac / Maxwell used throughout Parts A, B, D.
- **Lawson, H. B., & Michelsohn, M.-L.** (1989). *Spin Geometry*. Princeton University Press. —
  Standard reference for the Cl(p,q) classification cited at §D.1.3.
- **Frobenius, F. G.** (1878). *Über lineare Substitutionen und bilineare Formen*. — Frobenius
  theorem on finite-dimensional associative real division algebras, used at §C.3.8.

## Skyrme model and topological solitons

- **Skyrme, T. H. R.** (1961). *A non-linear field theory*. Proc. Roy. Soc. A **260**, 127. —
  Original Skyrme construction; cited at §C.1.
- **Adkins, G. S., Nappi, C. R., & Witten, E.** (1983). *Static properties of nucleons in the
  Skyrme model*. Nucl. Phys. B **228**, 552. — ANW Skyrme phenomenology; `e = 5.45`,
  `f_π = 129 MeV`; §C.1.2, §D.4.2.
- **Finkelstein, D., & Rubinstein, J.** (1968). *Connection between spin, statistics, and
  kinks*. J. Math. Phys. **9**, 1762. — Finkelstein–Rubinstein construction for spin-statistics
  via `π_4(SU(2)) = ℤ_2`; §B.3.5.

## Koide, Foot, and lepton mass structure

- **Koide, Y.** (1983). *A fermion-boson composite model of quarks and leptons*. Phys. Lett. B
  **120**, 161. — The empirical Koide identity `K = 2/3`.
- **Foot, R.** (1994). *A note on Koide's lepton mass relation*. arXiv:hep-ph/9402242. — The
  Foot angle characterization `cos θ = (Σ√m) / √(3 Σ m)` = 45°; §C.3.4.
- **Brannen, C. A.** (2006). *The lepton masses*. Unpublished note. — The ℤ_3 parametrization
  underlying the Brannen amplitude form; §C.3.1.

## Sakharov induced gravity and Lorentz-violation constraints

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
  **454**, 861. — Geneva-class influence-speed lower bound; §E.3 row 6.
- **Yin, J., et al.** (2013). *Bounding the speed of "spooky action at a distance"*. Phys. Rev.
  Lett. **110**, 260407. — Higher-precision follow-up; §E.3 row 6.
- **Toner, B. F., & Bacon, D.** (2003). *Communication cost of simulating Bell correlations*.
  Phys. Rev. Lett. **91**, 187904. — One-bit-per-run result; §B.4.5.
- **Tsirelson, B. S.** (1980). *Quantum generalizations of Bell's inequality*. Lett. Math.
  Phys. **4**, 93. — Tsirelson bound `2√2`; §B.4.2.
- **Mermin, N. D.** (1990). *Extreme quantum entanglement in a superposition of macroscopically
  distinct states*. Phys. Rev. Lett. **65**, 1838. — Mermin's operator; §B.4 scope note.
- **Klyshko, D. N.** (1993). *The Bell and GHZ theorems: a possible three-photon interference
  experiment and the question of nonlocality*. Phys. Lett. A **172**, 399. — Belinskii–Klyshko
  polynomial; §B.4.2 subsection.

## Cosmology and multi-messenger

- **LIGO / Virgo Collaboration** (2017). *Gravitational waves and gamma-rays from a binary
  neutron star merger: GW170817 and GRB 170817A*. Astrophys. J. Lett. **848**, L13. —
  `|c_GW/c − 1| ≲ 10⁻¹⁵`; §E.3 row 3, §E.3 VG-1.
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
- QCD running and confining-string tension `σ_QCD ≈ 0.18–0.19 GeV²`.

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
list is a permanent pick); `weak = SD` (one bit of a real two-option chiral menu,
neutrino-linked); the `D/J ≈ 0.79` value (cross-validated at ~1.1%, but a value); the lepton
amplitude scale `A`; the `+e_4` orientation (a cosmological IC). Watch-item on the boundary:
the orbit-phase → ℍ-unit identification behind the generation count (R-071's LOCATED
residual) — could yet close via dynamics (Class 2) or settle as a pick.

**Class 4 — knowability-limited: the genuine wavefront-locking wall.** Absolute substrate
normalizations that inside-frame observers cannot reach in principle, because the inside
frame measures contrasts against the homogeneous background:
- A **uniform `c_meta ≠ c` offset** — provably without observational signature (R-045 states
  this openly; also gauge-like, so physically inert). Permanently walled, and harmlessly so.
- **Absolute `Λ`** beyond the O(1) Sakharov bracket — currently reachable only through the
  gravity channel. **UNLOCKABLE**: P2-5 delivering `Λ·ℓ_S` as a dimensionless pure number
  moves this to knowable (the corpus's own "knowability handle").
- The **N22 branch-(a) monad endpoint** (if the R→0 resolution is the conservative
  D4-3-body-contact parameter, the values are a monad-scale INPUT of Λ/f_π knowability shape).
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
| P2-6 — L-orbit QCP / L2 mechanism (`ν = 3π/2`; K_c) | **2** | N31: static LSWT route ELIMINATED; single named route remains | §9.6 kernel must produce the SPECIFIC renormalization factor `(19/2)√38 ≈ 58.6` between bare LSWT stiffness and K_c — an unusually sharp numerical target for any kernel candidate (a free over-determination row for the 2b program); DQCP-literature comparison for the ν = 3π/2 coincidence |
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
| K_c kernel form | **2** | See P2-6 | The `(19/2)√38` target |
| `K = 2/3`, `weak = SD`, `D/J` value, `A`, `+e_4` | **3** | Menu-picks | None expected; the framework's win is the count (five INPUTs, not nineteen) |
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
| I-3 | **Sakharov induced-gravity one-loop** (heat kernel / Seeley–DeWitt; scaling form `M_Pl² ~ N·Λ²`) | R-037, §B.6.2 — the entire induced-EH magnitude bracket | **Substrate-level loop** | A standard QFT vacuum for substrate modes; validity of the one-loop expansion; covariant regularization | **OPEN** — the substrate is a driven-dissipative NESS, not a QFT vacuum; the scaling FORM is tagged "QFT INPUT" in-suite; `N_eff = 6` is generic-given-dim-4 (canon §5) | The #1-gap kernel supplying the actual spin-2 spectral sum (`C_T`) — via the R-145-named Gauss-equation face; P2-2 Class-2 half. **NARROWED by R-163 (2026-07-27)**: computed on the derived linear face, the flat-band mode measure is derived and finite (no regularization choice), reducing this row's premise triple to TWO named assumptions — OA-LF-i (NESS ground-state occupation, the STATE) and OA-LF-ii (monad-scale covariant curvature coupling, the OPERATOR, carrying ~93% of the integral's support: the old regulator freedom relocated and localized, NOT removed). Status stays OPEN; the retirement handle is unchanged |
| I-4 | **Volovik's Gibbs–Duhem identity** for self-sustained media (`ε − μn = −P = 0` ⇒ gravitating vacuum energy vanishes in equilibrium) | R-047, §B.7.4 — the Λ-catastrophe dissolution | Substrate-level thermodynamics | Thermal EQUILIBRIUM at zero external pressure; self-sustainment (the substrate satisfies the latter by construction) | **NAMED-CRACK** — the substrate is driven, not equilibrium; the deviation IS the gated `Λ ~ H²` residual (§E.1, VG-2); valid at the equilibrium anchor | The off-equilibrium computation at §D.5 (#1 gap) — quantifies the crack rather than removing the import |
| I-5 | **Semiclassical soliton toolbox**: ANW collective quantization, rigid-rotor band, Callan–Klebanov bound-state method, rational-map ansatz, FR quantization framework incl. the axial `K₃ = 0` selection rule (Krusch-class) | R-025, R-133–R-144, §C.1 — the entire quantitative hadron arc | Inside-frame / effective (collective-coordinate quantization) | Semiclassical QM; adiabatic separation of collective modes; the imported selection-rule machinery (R-136: "literature-known, credited; consistency-checked in-engine") | **JUSTIFIED at the emergent level** — QM is derived §B.3, so quantization operates in-jurisdiction; method artifacts honestly tracked (rigid-rotor overbinding ~113/124 MeV; the `Σ_c−Λ_c` CK-inertia fork) | Beyond-rigid-rotor quantization (P2-7 residual row); the dynamical multi-defect EOM (SC-1 core, kernel-gated) |
| I-6 | **SM renormalization-group run-down** (gauge-coupling running between the unification and measured scales) | §C.4.5 (sin²θ_W: 3/8 → 0.231), Λ_QCD comparisons (R-133 knock-on) | Inside-frame data bridge | Full SM field content; perturbative unitarity over the run | **OPEN as derivation, SANCTIONED as data import** — canon §7 states plainly TWT does not derive the running; this is the inside-for-data method, not a disguise | TWT-native running (P2-3's β and the P2-1 kernel) — the registry's largest single exposure by headline-value |
| I-7 | **KSRF / hidden-local-symmetry relation** (ρ-meson as gauge boson of the Q-orbit local symmetry) | The rho30 asset (N5's would-change-if handle); not yet load-bearing in a banked R-NNN | Effective | Vector-meson dominance phenomenology; HLS structure | **CANDIDATE-calibrated** — g_ρ calibrated, not derived; flagged as the re-attack template for the colour octet | A TWT derivation of the Q-orbit gauge structure (P2-4 fluctuation-YM face) would replace the calibration |
| I-13 | **The dispersive/S-matrix package** (analyticity, crossing, ≤2 subtractions/boundedness, optical-theorem positivity — the KL+unitarity route R-085 named; FIRED 2026-07-05) | R-148, §C.5.2 — the β₃ sign (AF-signed at the dressed level; the wrong-sign risk removed) | Inside-frame / effective (elastic ππ-class forward channel of the dressed coset Goldstones) | Analyticity/causality of the inside-frame amplitude; crossing; polynomial boundedness (≤2 subtractions); optical-theorem positivity | **DATA-LIKE jurisdiction (13.4)**; the positivity leg PARTIALLY RECAST onto the banked §B.3-derived unitary QM (probability conservation of the derived theory — the 13.3 stability-recast directive satisfied for that leg); analyticity + boundedness NOT yet recast (named residual premises) | Retired by the kernel's own UV spectral computation (the same object that owes DGLAP). REVERT CLAUSE: refusing the package restores R-085's located-gap status (β₃ sign genuinely open); R-148 reverts to the pre-import state; nothing else moves |
| I-14 | **Preisach hysteresis-operator theory** (representation of rate-independent hysteretic operators as hysteron superpositions; Mayergoyz representation theorem = wiping-out + congruency; the Everett function) | §E.5 kernel memory face — the F4 hysteretic branch made representable (R-153/R-155); TWT slot: hysteron = elementary bistable winding/flip unit, the Preisach density = the substrate's flip-barrier distribution (FRAMING) | PURE MATH with checkable hypotheses (the Section-13-EXEMPT class, like KK/Titchmarsh) — registered for completeness | The operator has the wiping-out AND congruency properties (both numerically witnessed, simulator `verify_preisach.py`) | **N/A** (a math theorem; no substrate premise). The TWT hysteron identification is FRAMING | None needed (a theorem); the FRAMING TWT slot retires if the substrate flip-unit picture is refuted |
| I-15 | **Floquet theory** (linear response about a T-periodic drive: monodromy matrix, Floquet multipliers/exponents, the \|trM\| = 2 stability boundary; machinery witnessed on the exactly-solvable Meissner oscillator) | §E.5 kernel drive face (R-153); TWT slot: the wavetrain = the periodic drive, the kernel = linear response about the Floquet state (R-007's driven attractor; the Section-12 Floquet limit-cycle lean) (FRAMING) | SUBSTRATE-level formalism (the drive IS the wave) — but the machinery witness is a lossless toy; no physics premise rides on the witness | Linearity about a periodic reference; T-periodicity of the drive (the wavetrain cadence). **Caveat preserved: the real substrate kernel is driven-DISSIPATIVE (\|ρ\| < 1); the lossless witness validates the machinery, never the dissipative content** | **OPEN** for the substrate application (the actual Floquet state IS the #1-gap object); the machinery itself is a math theorem (JUSTIFIED) | Retired/replaced if the substrate NESS is shown NOT a limit cycle (the fading/SOC arm of `eom_compatible_field_forks` Fork B) |
| I-16 | **DQCP universality framework** (deconfined-quantum-critical-point scaling, Senthil et al. class) | R-055, §C.1.6 — the QCP exponent's `Δ_v` ingredient and the universality frame | Cell-layer critical scaling | A DQCP-class critical point governs the L-orbit `D = J` balance; engineering-dimension counting valid at leading order | OPEN (registered 2026-07-26 per coherence audit — previously unregistered) | Derive the exponent from the §D.5 kernel, or replace the universality frame with a substrate RG computation |
| I-17 | **Witten SU(2) global anomaly** (odd number of LH Weyl doublets ⇒ SU(2) gauge theory inconsistent — the fermion-measure statement over the exempt-pure-math `π₄(SU(2)) = ℤ₂` classification) | §C.4.6 step (i) — gaugeability of weak SU(2)₊ | Inside-frame effective (fermion path-integral measure) | 4D chiral fermion path integral | JUSTIFIED as inside-frame theorem (registered 2026-07-26 per coherence audit — previously unregistered) | A substrate-level derivation of the mod-2 obstruction on the D4 rotor field |
| I-18 | **Gauge-anomaly cancellation package** (mixed-gravitational `Tr Y = 0` and cubic `[U(1)_Y]³` conditions on a chiral fermion spectrum; the colour condition only under a continuous-completion reading, since TWT colour is ℤ₃-discrete) | R-159, §C.2.7 — the corroborating fixings of `c = 1/2` and the right-handed hypercharges; NOT used for the anchor-free identity itself | Inside-frame effective (fermion path-integral measure) | 4D chiral fermion content; a gauged U(1)_Y at the effective level; for the colour condition additionally that colour completes to a gauged SU(3) at that level | JUSTIFIED as inside-frame theorem (registered 2026-07-27) | Revert clause: strike this row and R-159's flagship identity is UNAFFECTED (it is import-free, holding identically in `c`); only the corroborating `c = 1/2` routes (ii)/(iii) and the RH-hypercharge forcing fall back, leaving the native sterile-Dirac route and §C.2.1's posited assignments |

## 13.2 Negative and defensive uses (closures conditional on the import)

| # | Import | Used at | Exposure |
|---|---|---|---|
| I-8 | **Nielsen–Hughes** (antiscreening requires the paramagnetic response of a charged spin-1 field) | N5 — closed the emergent-AF route | The CLOSURE is conditional: if the theorem's premises fail on the substrate, the route could reopen. Recorded so the conditionality is visible; the octet-as-oscillation would-change-if already covers the live re-attack |
| I-9 | **Weinberg–Witten** | §B.6.7 — preemption | None forward: the theorem is EVADED (composite graviton), its premises deliberately not satisfied. Registered for completeness |
| I-10 | **Reflection positivity** (Osterwalder–Schrader-class) | R-085 `beta3_sign_from_reflection_positivity` — a NEGATIVE (RP insufficient for the running sign) | Low: the banked result is a negative either way. FLAG: whether the substrate measure itself is reflection-positive has never been checked — any future POSITIVE use of RP must first address that (see 13.3) |
| I-11 | **Bell's theorem / Gleason** | §B.4 — inherited-by-isomorphism; Gleason explicitly NOT claimed | None: any theory isomorphic to QM inherits Bell; the paper says so plainly |
| I-12 | **FDT (fluctuation–dissipation theorem)** | §D.5.6 — Θ_rel is DEFINED as its violation residual | Definitional, not an import that must hold: Θ_rel measures exactly how far the substrate sits from the regime where equilibrium imports are exact. Registered because it is the QUANTIFIER of the I-4-class crack |

## 13.3 Prospective imports (named leads, not yet used — pre-registered exposure)

| Lead | Would be used at | Premises | Pre-registered status |
|---|---|---|---|
| **a-theorem / c-theorem analogue** (Komargodski–Schwimmer class) | P2-3 sign lead — **NOT PURSUED** (superseded 2026-07-05: the KL route fired first, R-148/I-13) | Unitary, Lorentz-invariant 4D QFT with defined UV/IR fixed points | The premise gap stands as recorded; any future use still enters at conditional tier + a 13.1 row, mandatory |
| ~~**Källén–Lehmann + unitarity bound** on the running quartic~~ | **FIRED 2026-07-05 → promoted to 13.1 row I-13** (R-148) | — | The stability-recast-first directive was satisfied for the positivity leg (recast onto the banked §B.3-derived QM); analyticity/boundedness remain un-recast, named in I-13 |

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
absorb the import. Arbitrary imports — used load-bearing but unregistered, or registered but
woven in without a revert path — are banking-stoppers of the phantom-cite class.

---

*End of companion file.*
