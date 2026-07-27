# Time-Wave Theory — Foundational Paper (V3)

*Version 3 · 2026-07-01 · revised 2026-07-27.*
*Yaer Aharon Haddad Fennech · Independent Researcher · hfyaer@gmail.com*
*Ships with a **companion file** — `TWT_foundational_paper_companion.md` — that consolidates
all annexes, the back-of-book bookkeeping (Result Index, Dependency Graph, Engine ↔ Paper Map,
Pending-Values Registry), the geometric reinterpretation catalog, the methodology principles,
the development log, the stable-spectrum enumeration, the wave-phase stability ladder, and the
bibliography. Load both together for the full picture; the paper file is pure physics narrative.*

---

# Abstract

We develop a framework in which observed physics is the inside view of a four-dimensional
Euclidean substrate — a D4 lattice of unit Clifford rotors — carrying a wave that advances
along a distinguished axis. Observers are wavefront-locked configurations of the wave; matter
is a topologically protected defect of the rotor field; mass is the frequency of the defect's
meta-time rotor. From five counted empirical inputs (a sixth, an overall amplitude, cancels in
ratios), the framework derives — at explicitly labeled and audited tiers — the structural
skeleton of known physics: the Lorentzian signature of observed spacetime as the algebraic
shadow of wavefront locking (`Cl(4,0) ≅ Cl(1,3)`, and specifically the `(1,3)` partner);
quantum mechanics' postulate structure recovered from one geometric projection — including the
Born exponent as a theorem given four named structural premises, and spin-statistics by an
empirically anchored selection whose structural half is exact algebra — with the Tsirelson
bound `2√2` exact; electromagnetism with magnetic monopoles algebraically forbidden; induced
gravity with the sign and the form (`γ = 1`) established, and a Planckian magnitude bracket
via a registered spectral-sum import; exact charge
discreteness across the 15-state generation spectrum, with the proton–electron equality
topologically protected; a three-generation count from the
quaternionic structure (conditional on one named identification); the electroweak mixing angle
`sin²θ_W = 3/8` at unification with no GUT embedding; and a matter-stability triad — no proton
decay, Dirac neutrinos, no neutrinoless double-beta decay — from one conservation law. A
structural consequence worth stating separately: the framework carries **no irreducible chance**
as a primitive — it is configuration-realist, and probability enters as a derived measure over
definite configurations rather than as an axiom, so what standard quantum mechanics postulates
is here computed (the mechanism of single-outcome selection remains open). The
framework's principal open object, the driven-dissipative substrate dynamics that gates all
coupling magnitudes and absolute scales, is named explicitly, with a candidate kernel class
and pre-registered falsifiers. Every numbered result carries an auditable status tier
(derived / input / fit / candidate) in a companion result index, and the algebraic content is
backed by an executable verification suite (438 checks at this revision).

---

# A note to the reader before you start

**This paper is organized from solid to speculative, not from axioms to consequences.**

The traditional foundational-paper shape — premises, derivations, corollaries, open problems — is
honest, but it forces the reader to wade through machinery before meeting the result it serves.
This paper inverts that. Part A states the ontology in plain language and gives just enough
algebra to read on. Part B uses it: emergent Lorentzian signature, special relativity, quantum
mechanics, Bell, electromagnetism, the fine-structure constant, gravity, the cosmic frame,
the macroscopic limit. These are the framework's most solidly derived results, and they are what
the rest of the paper exists to support.

Parts C and D then do the engineering. Part C derives Standard-Model structure (charges, three
generations, the gauge group). Part D opens the substrate: the Clifford algebras in full, the D4
monad layer, the wave equation, and the open driven-dissipative dynamics — the framework's #1
gap. Part E addresses cosmology, falsifiers, and the open frontier.

The reader meets the framework's spine first, then sees what it is built on, then sees what is
still open. As the paper progresses, the uncertainty increases. Naming that honestly is part of
the reporting discipline; the deepest open questions are at the back, not buried in the middle.

**Where the bookkeeping lives.** Rather than inline tier tags (`[DERIVED]`, `[FRAMING]`, `[CANDIDATE]`
etc.) scattered through the prose, every numbered result carries a compact `(R-NNN)` marker; the
tier, engine primitive, target section, and dependency edges live in the **Result Index** —
Section 1 of the **companion file** `TWT_foundational_paper_companion.md`. The Index is
authoritative; the paper reads cleanly. Section 2 of the companion is the **Dependency Graph**
— the same content laid out as a layered structural picture (which results are axioms, which
fall out algebraically, which depend on the open dynamics). The companion also carries the
Engine ↔ Paper Map (Section 3), the Pending-Values Registry (Section 4), a full geometric
reinterpretation catalog (Section 5), methodology principles (Section 6), the development log
(Section 7), the stable-spectrum enumeration and wave-phase stability ladder (Sections 8–9), a
bibliography (Section 10), the Paper-2 agenda (Section 11), the closability classification
(Section 12), and the Import Registry (Section 13). **Load the companion alongside
this paper for the full picture.**

---

# Opening

*Time is a wave. We're riding it.*

The framework develops from one ontological premise — a four-dimensional Euclidean substrate
carrying a wave propagating along a distinguished direction — to derivable consequences.
Observers are wavefront-locked configurations of the wave. Matter is what departs from the wave's
homogeneous configuration: a topologically protected pattern in the rotor field. Mass is the
frequency of the meta-time rotor that sustains that pattern.

This Opening states the premises in a list, names the inputs, and points the reader at the
falsifiers. It does **not** re-derive the spine or tour the falsifier table. Both live where they
belong — derivations in Parts B and C, falsifiers in §E.3.

**Premises** (axiom IDs in the Dependency Graph — companion Section 2), ordered by structural
depth — most foundational first. The starred IDs `A-1*` and `A-2*` are the two ontology / method
premises promoted to first-class status in this version; the unstarred IDs `A-1a/b/c, A-2, A-3`
are the original Opening premises, preserved verbatim.

- **(A-1a) — 4D Euclidean substrate.** `(ℝ⁴, g)` with positive-definite metric. The ontological
  ground.
- **(A-3) — Wavefront / signature locking.** Observers are wavefront-locked configurations of
  the wave and read `e_4` as time. The Lorentzian signature of observed spacetime follows.
- **(A-1\*) — Matter is defect.** Matter is a topologically protected pattern in the rotor field,
  not a piece of stuff. Mass is the meta-time rotor frequency. Two frame-appearances
  (inside-frame positive contrast; outside-frame hole in the carrier envelope) are images of the
  one defect.
- **(A-2\*) — Working frame is outside the wavefront.** Methodological discipline: the inside
  view is used only to import empirical data; reasoning *from* the inside frame imports the
  Standard Model's frame and risks circular derivation.
- **(A-2) — Driven dynamics premise.** The substrate is driven: the wave drives the medium along
  `e_4`. The explicit form of this dynamics is the framework's #1 gap (§D.5). An axiom
  placeholder rather than a closed structural premise.
- **(A-1b) — D4 cell lattice.** The substrate's coherence-cell structure is the D4 lattice.
  Empirically motivated (D4 is the densest 4D **lattice** packing, with kissing number 24 — among
  all packings the question is the open 24-cell conjecture), not derived inside the framework.
  A structural premise at the cell layer (§D.3).
- **(A-1c) — Two bond couplings.** Symmetric exchange `J` on all 24 NN bonds; Dzyaloshinskii–Moriya
  `D` on the 12 `e_4`-bonds. The ratio `D/J ≈ 0.79` is INPUT, calibrated to the lepton sector.

**Empirical inputs** (the framework's parameter ledger), ordered by structural weight:

- `weak = SD` — one bit: the gauged Spin(4) factor is the chiral one (neutrino-forced). The
  most economical input — a single binary choice fixing V−A, generation-blindness, the doublet,
  and `up = SD`.
- `Λ` — substrate cutoff (Planckian within a factor of order unity). Sets the gravity scale.
- `f_π ≈ 129 MeV` — the cell-scale mass scale.
- `D/J ≈ 0.79` — chirality ratio (calibrated to leptons; cross-checked by baryon sector).
- `c = √2` ⇔ Koide `K = 2/3` — Brannen phase coefficient (exact-but-unforced).
- `A` — lepton amplitude scale (free Koide calibration; cancels in ratios).

(Counting convention: **five counted inputs** — `A` cancels in ratios and is not counted;
§E.2.1 states the same convention.)

**Units convention.** Throughout the paper, *natural* units are the default: `c = ℏ = 1`, so
`m = ω` is read literally (R-007), substrate frequencies and masses share a scale, and grade-0
inner products are bare numbers. Explicit `c` and `ℏ` are restored in two situations only:
(i) when a formula is being compared to data quoted in SI / lab units (e.g. `ω = m_e c²/ℏ` when
the electron rest energy is on display); (ii) when the Maxwell-table laws are written in the
mixed-grade form readers expect from EM textbooks. Both are local restorations for legibility,
not switches of convention.

Everything else the framework claims as structure — three generations, `sin²θ_W = 3/8`, charge
quantization, the L/Q split, the Skyrmion's winding label, fractional quark charges, the
Lorentzian signature itself — is a consequence of these premises and inputs, derived in the body.

---

# Methodology — how this paper was developed

This paper is the product of a structured workflow combining a developer (Claude) with an
adversarial reviewer dispatched in a fresh context, plus an automated suite (`twt_test.py`) that
checks all engine-banked algebraic results on every revision. No load-bearing claim is banked on
the developer's say-so alone: each is attacked by an independent reviewer, verified on the
substrate engine where applicable, and only graduated when developer and reviewer agree on its
tier and scope. This iterate-to-consensus discipline (companion Section 6) has caught — in V3 alone — three
algebra bugs (the Koide fraction inversion, the Foot 45° formula, the `(1±E)/2` non-idempotent),
two physics-precision overstatements (`M_0 ≈ 1%` → `~8%`, the L⊥Q orthogonality framing), several
citation slips (Cohn–Kumar attribution; the Collins-2004 author list), and the central forward
dependency owed to Part B from §D.4 that earlier drafts asserted without delivering. The Result
Index, Dependency Graph, Engine ↔ Paper Map, and Pending-Values Registry — Sections 1–4 of the
companion file — make every claim's tier, engine cite, and dependencies inspectable.

**External theorems are imports, and imports are registered — never arbitrary.** In several
places this paper leans on theorems proven elsewhere (an induced-term theorem, one-loop
induced-gravity machinery, an equilibrium many-body identity, semiclassical soliton methods).
These come in two epistemically different kinds, and the distinction matters. Theorems applied
at the *inside-frame effective level* are data-like: on this framework's own account QFT is the
inside-frame effective description, so its theorems are compressed inside-frame regularities,
imported the same way measured values are — legitimate, and owed an outside-frame mechanism.
Theorems applied at the *substrate level* are not data at all: they are borrowed fragments of
the would-be outside mechanism itself, standing in for the unbuilt substrate dynamics, and if
their premises fail on the actual substrate they do not merely await explanation — they can
steer the theory wrong. Every load-bearing import of either kind is therefore registered in
**companion Section 13 (Import Registry)** with its premises, the level it is applied at, its
justification status on the ontology, and the handle that would retire it; and every result
depending on one carries a conditional tier with a **named revert clause**, so that a wrong
import can be **excised precisely** — strike the registry row, fire the listed revert clauses,
and the dependent results fall back to their pre-import tiers rather than collapsing
ambiguously. A reader who distrusts any single import can see exactly what survives without it.

The methodology is itself part of the framework's case: ambitious foundational claims need a
discipline that catches their own errors before publication.

---

# Notation — a glossary at hand

A compact reference for the framework's shorthand. Each entry points to the section that
introduces it.

| Symbol / term | Meaning | First in |
|---|---|---|
| `Cl(4,0)`, `Cl(4,1)` | Real Clifford algebras over Euclidean ℝ⁴ and ℝ⁴¹; the native and extended formalisms | §A.5 / §D.1 |
| `e_1, e_2, e_3, e_4, e_5` | Generators; `e_i² = +1` for `i ≤ 4`, `e_5² = −1` | §A.5.1 / §D.1 |
| `I_4 = e_1 e_2 e_3 e_4` | Pseudoscalar of `Cl(4,0)`; `I_4² = +1`; Hodge map L ↔ Q | §A.5.3 |
| `I_5 = E = I_4 · e_5` | Pseudoscalar of `Cl(4,1)`; `E² = −1`; central; global complex unit | §A.5.6, §D.1.3 |
| `𝓛` (L-orbit) | `{e_{12}, e_{13}, e_{23}}` — `e_4`-free bivector triple; closes as `so(3)`; spatial-rotation generators | §A.5.2 |
| `𝓠` (Q-orbit) | `{e_{14}, e_{24}, e_{34}}` — `e_4`-bearing bivector triple; coset complement of `𝓛` | §A.5.2 |
| **SD** / **ASD** | Self-dual / anti-self-dual bivectors — the two chiral halves of `so(4) = su(2)_+ ⊕ su(2)_−` under the `I_4·` eigenvalue split | §C.4.2, §D.2.4 |
| `𝒮 = Cl(4,0) · s_0` | Spinor minimal left ideal, real dimension 8 | §A.5.4 |
| `s_0 = (1 + e_4)/2` | Primitive idempotent of `𝒮` | §A.5.4 |
| `q_h(τ_5) = exp(m τ_5 û/2)` | Meta-time rotor of frequency `m = ω` (= mass); `û` simple unit element with `û² = −1` | §A.4 |
| `J`, `D`, `D/J` | Symmetric exchange / Dzyaloshinskii–Moriya couplings on D4 bonds; `D/J ≈ 0.79` calibrated to leptons | §D.3.3 |
| `f_π ≈ 129 MeV` | Cell-scale mass; substrate condensate identification | §D.4.1 |
| `Λ` | Substrate cutoff; Planckian within O(1) | §D.3.5 |
| **ANW** | Adkins–Nappi–Witten Skyrme-model phenomenology | §C.1.2 |
| **BVP** | Boundary value problem (the Skyrme variational equations) | §C.1.1 |
| **QCP** | Quantum critical point — the L-orbit critical balance `D = J` underlying the electron mass scaling | §C.1.6 |
| **`δ_L`** | Brannen lepton phase; `δ_L = (1/3) arctan(D/J) = 12.73°` at the lepton-calibrated `D/J ≈ 0.787` | §C.3.5 |
| **`Θ_rel`** | FDT-violation residual on the coset-Cartan channel; the framework's highest-value target | §D.5.6 |
| **`Im χ`** | Substrate transport function; the #1 gap's master dial | §D.5.4 |
| **KSS** | Kovtun–Son–Starinets viscosity-to-entropy lower bound `η/s ≥ ℏ/(4π)`; the substrate sits near this floor | §E.3.3 VG-1 |
| **FDT** | Fluctuation–dissipation theorem; its violation residual is `Θ_rel` | §D.5.6 |
| **R-NNN** | Numbered result, looked up in the Result Index (Section 1 of the companion file) | throughout |
| **WP-IX3 / IX4 / DC2** | Substrate-level "Wave-Phase" safety lemmas: leak-independence, symmetry-protected unitarity, Goldstone-protected decoherence | §D.5.5 |
| **A-1\* / A-2\*** | Promoted ontology / method premises (matter-as-defect; outside-frame discipline); see Opening | Opening |

---

# Part A — The Picture

*The smallest set of facts you need to read Part B.*

---

## §A.1 — Time is a wave

The substrate is a four-dimensional Euclidean manifold (A-1a). On it lives a wave field `Ψ`
propagating along a distinguished direction `e_4`. The wave's advance is parameterized by an
external scalar `τ_5` — what we will call *meta-time*.

What kind of wave is it? A **wave-train**: a continuous succession of three-dimensional
wavefronts traveling together along the propagation direction. **The wavefronts directly succeed
one another along `e_4` — there is no empty space between them.** Every value of `τ_5` selects a
wavefront filled with rotor content, and the substrate is continuous along the propagation axis;
the wave-train is the medium's structure, not a string of pulses through vacuum. Each wavefront is
a 3D hypersurface within the 4D bulk, advancing in `e_4` as `τ_5` flows. A thermodynamic observer
— any configuration that requires continuous state change to persist — is mechanically locked to a
primary resonant wavelet of the advancing train (R-001).

The direction `e_4` is *distinguished*. It breaks the four-fold symmetry of the bulk and selects
the wave's propagation axis; a cosmological initial condition picks it. In the algebra it is the
**only ontologically distinguished multivector**: every other "distinguished" direction we will
meet (the pseudoscalar `I_4`, the orbit-connecting operator, the wavefront's gamma matrices, the
spinor's primitive idempotent `s_0`) is *built* from `e_4` plus spatial completion, and is
therefore derived rather than postulated.

The wave-train structure is load-bearing later: it shapes quantum tunneling (§B.3), accommodates
time crystals (§B.7), supplies the substrate channel for β-decay's L-pair creation (§C.5),
Compton-screens the would-be light scalar mode of induced gravity and so delivers `γ = 1` (§B.6),
and sources the thermodynamic arrow of time at the substrate level (§B.7).

A note about what this picture is **not**. It is not the luminous aether. The aether was an inert
medium *through which* material objects propagated; Michelson–Morley ruled it out by showing no
preferred frame exists for electromagnetic propagation. The TWT substrate is not a medium through
which observers move. Observers are configurations *of* the wave; matter is a defect in the same
wave; there is no observer-relative-to-substrate motion to detect. Michelson–Morley is structurally
consistent with the framework, not a problem it has to defuse.

---

## §A.2 — The wavefront and the observer

A wavefront — the locus of constant phase of the wave — is a three-dimensional hypersurface within
the 4D bulk. Topologically it is the three-sphere `S³`, identified algebraically with
`SU(2) ≅ Spin(3)`: the spatial slice compactifies to `S³` under the asymptotic boundary condition
`R(∞) = 𝟙` that defines matter (§C.1), allowing topological winding numbers
`π_3(Spin(4)) = ℤ × ℤ` to classify matter (R-002).

The "two ℤ" come most directly from the **chiral factorization**
`Spin(4) = SU(2)_+ × SU(2)_−`, where the two factors are the Hodge-eigenvalue (self-dual / anti-self-dual)
halves of the bivector algebra. The framework's *working* basis is a different one: the
**L-orbit / Q-orbit split** by `e_4`-content (§A.5.2), with leptons winding into the L-orbit
and baryons into the Q-orbit. The two decompositions are genuinely distinct — the self-dual
bivector `e_{12} − e_{34}` mixes one L-blade with one Q-blade, so `𝓛 ⊕ 𝓠 ≠ SU(2)_+ × SU(2)_−` as
decompositions of `so(4)`. **The relabeling from chiral basis `(n_+, n_−)` to orbit basis
`(n_L, n_Q)` is justified by a symmetric-pair / fibration bridge, given at §A.5.2.** Treating
them as the same split has historically been the framework's most error-prone conflation; the
rest of the paper is careful to keep the two distinct.

A scope note. The "topological `S³`" used here is not a claim about the observable universe's
spatial curvature. The geometric radius of curvature is a separate question; cosmological
observation requires `R_curv ≳ 20 R_H` (Planck 2018 + BAO, `|Ω_k| ≤ 0.0026` at 1σ), so the universe
is effectively spatially flat at observational precision. Topological-`S³` identification (used in
§C.1 to define winding numbers) and observed geometric flatness coexist if `R_curv ≫ R_H`, which is
consistent with what is measured.

**The wavefront-locked observer.** Such an observer takes the propagation direction `e_4` as their
time axis and the bivectors `e_4 e_j` (`j = 1, 2, 3`) as their three spatial directions. We will
verify in §B.1 that these satisfy the `Cl(1,3)` Dirac relations — that verification is the
*wavefront isomorphism*, and the Lorentzian signature of observed spacetime falls out as its
algebraic shadow.

A particle's **spin** is its transformation under the `Spin(3)` rotation of the wavefront-internal
spatial coordinates. We will see in §A.4 that spin and the rotor frequency we call mass act on
*different (orthogonal) blades* of the Clifford algebra — algebraically separable as observables —
but in matter they are two faces of one defect, dynamically coupled through the circular structure
of §A.3.

**The working frame is outside the wavefront.** We develop the derivations *from outside the
wavefront*. The inside (observer-locked) view is used only to import empirical data. This is
methodological discipline (R-003), not interpretation:

- **Inside-frame**: matter reads as positive spin density against a homogeneous vacuum at zero.
- **Outside-frame**: matter reads as a defect — a hole — in the carrier-envelope vacuum.

Both readings are frame-appearances of the same substrate fact: a topologically protected pattern
in the rotor field. Reasoning *from* the inside frame imports the Standard Model's frame of
reference (matter as positive substance) and risks circular derivations. We work from outside.
The algebra is the algebra.

---

## §A.3 — The vacuum is the bulk of the wave; matter is a defective part

**The vacuum is the bulk of the wave field** — the substrate in its homogeneous configuration on
the observer's wavefront. **Matter is also part of the wave** — but a *defective* part: a
topological deviation from homogeneity that cannot be unwound smoothly. The vacuum and matter are
the same wave-medium; what distinguishes matter is the topological structure of the configuration,
not the substance.

The vacuum spinor is

> `Ψ_vac(χ, τ_5) = c_0 · s_0`,

with `c_0` a normalization constant and `s_0 = (1 + e_4)/2` the primitive idempotent of the
spinor minimal left ideal `𝒮` (§A.5.4). The substrate's ordered ground state is *canted*, not
fully aligned — a small canting angle quantifies the chiral-symmetry breaking that the framework's
hadronic-sector derivations rest on. (The numerical specifics — the `D/J` calibration, the
Luttinger–Tisza spiral pitch — sit at §D.3 / §D.4.)

**Matter is a defect** in the wavefront's rotor field — a configuration that fails to match the
homogeneous vacuum (R-004). Geometrically: the rotor orientation is deflected from the surrounding
canted ground state, and the deflections compose around the defect into a topological winding that
cannot be continuously undone to uniformity. The framework names the deflection a **lack of spin** — spin
orientation missing relative to the vacuum's homogeneity. The winding is an integer in `π_3(S³)`
for baryons (the L/Q split of §D.2 routes the winding to the Q-orbit) or the Hopf invariant `H = 1`
for leptons (routed to the L-orbit; §C.1).

The wave-level ansatz for an isolated defect:

> `Ψ_a(χ, τ_5) = F(χ) · B_a · s_0 · q_h(τ_5)`,

with `F(χ)` the spatial profile (the localized winding pattern), `B_a` a grade-3 blade specifying
particle type (§C.2), and `q_h(τ_5)` a meta-time rotor of frequency `m = ω` (§A.4).

### Two faces, one defect

The defect has two equivalent geometric faces, linked by the Hodge duality `I_4` (R-005):

*The spatial face — circular winding.* At each point within the defect's extent, the rotor's
orientation is rotated off the local vacuum orientation. The orientation-deficit decomposes onto
three orthogonal spatial generators — the L-orbit bivector triplet `{e_{12}, e_{13}, e_{23}}` for
leptons, the Q-orbit triplet `{e_{14}, e_{24}, e_{34}}` for baryons — and the three components
combine into a **Skyrme/Hopf hedgehog**: the spatial profile `F(χ)`, with rotor orientation winding
once around `Spin(3) ≅ S³` as the position traces a sphere around the defect's center. The
winding integer is `B` in `π_3(SU(2)) = ℤ`, or its Hopf-fibration shadow `H = 1` for leptons.

(A heuristic for readers familiar with optical polarization: a two-component circular polarization
is the rotating-vector pattern produced by two orthogonal phase-offset components. The
`Spin(3)`-valued case here is a three-component generalization where the "rotation" lives in
`Spin(3)` rather than `U(1)`, and the topological winding is `π_3` rather than `π_1`. The
heuristic motivates the picture; the load-bearing object is the Skyrme/Hopf hedgehog.)

*The meta-time face — rotor at frequency `ω`.* The same configuration, viewed in the meta-time
direction at fixed spatial position, advances in phase at frequency `ω = m`. This is the meta-time
rotor `q_h(τ_5) = exp(m τ_5 û / 2)` of the ansatz. The wave-drive of A-2 operates at this same
frequency; the driven attractor whose invariant label is the winding integer is the one whose
drive frequency equals the configuration's mass.

**The two faces are not independent.** The spatial winding cycles in space at fixed meta-time;
the meta-time rotor cycles in meta-time at fixed spatial point; *they are one circular object read
along orthogonal axes*, related by the `e_4` / `I_4` Hodge duality that interchanges the L-orbit
spatial bivectors with the Q-orbit `e_4`-bearing bivectors (§A.5.3, §D.2). The spatial winding is
the inside-frame appearance of the same object whose outside-frame appearance is the inverse
circular envelope of §A.2's outside frame — the "hole in the carrier-envelope vacuum." Both are
frame-appearances; the substrate fact is the defect itself.

### Stability is topological

The winding cannot be continuously deformed to the homogeneous vacuum without passing through a
higher-energy state, regardless of whether the defect is read as a static defect (the drive-zero
limit) or as a driven attractor (the ontological register under A-2). For baryons the winding is
the degree of `U: S³ → S³`, an integer in `π_3(S³) = ℤ`; for leptons it is the analogous L-orbit
Hopf winding with `H = 1` (R-006).

At the substrate level, the topological label is the *invariant* of the driven attractor —
preserved under drive variation while the attractor exists. The static Skyrmion of §C.1 is the
signature of this winding in the drive-zero limit, the regime where standard ANW/Skyrme
phenomenology applies and matches the empirical hadron spectrum to within ~10%. The static-limit
register and the driven-attractor register are not in tension: a winding number cannot jump under
continuous deformation in the drive parameter, so the proton-as-`B = 1` identification survives
the reframe.

### Observer-relative vs absolute vacuum

In the absolute description, the vacuum is a nonzero homogeneous configuration with definite
energy density. In the observer-relative description, observers measure the *contrast* between
their local configuration and the surrounding wave; the homogeneous background registers as zero.

The two descriptions are dynamically equivalent — the observer's "zero" is the bulk's `c_0 s_0` —
but only the absolute description carries the medium's energy density responsible for gravity and
cosmology.

---

## §A.4 — Mass is meta-time rotor frequency

A massive defect has a meta-time rotor advancing in `τ_5`. The angular frequency of this rotor *is*
the mass:

> `m = ω`. (R-007)

A photon has no meta-time rotor (it is a propagating bivector strain, not a defect; §B.5); its mass
is zero. An electron has rotor frequency `ω = m_e c² / ℏ`.

The half-angle convention `q_h = exp(m τ_5 û / 2)` is forced by spinor inheritance: under
`τ_5 → τ_5 + 4π/m` the rotor returns to itself, with sign flip at `τ_5 + 2π/m` — the `SU(2)`
double cover. Here `û` is a simple unit element with `û² = −1` — the meta-time rotor axis in the
`ℍ` factor of the native `Cl(4,0) + ℍ` formalism (§A.5.6). For the observer-visible mass phase
the axis is not free: projecting the rotor history onto the observer's forced complex line shows
that only the defect's own winding direction — the transverse blade R-020 forces as the QM
complex unit — reads as a propagating phase, while an `E`-carried front phase would leave the
observer's `Cl(4,0)` ideal and present as density nodes; the meta-time axis is thereby locked to
the winding direction (R-127, §B.3.1). The central `E = I_4 · e_5` retains its global/colour
complex-structure role (§A.5.6). (Compare with the per-defect grade-3 blade `B_a` of §A.3's
spatial ansatz: `B_a` selects particle type and lives in spatial bivector-trivector content,
while `û` is a meta-time rotation axis — by R-127 locked, for the visible phase, to the defect's
transverse winding blade.)

The meta-time rotor is, by R-005, the inverse face of the spatial winding under Hodge duality —
a substrate-level statement. For the observer-visible mass phase the winding↔rotor-axis relation
is sector-split (R-127/R-128, §B.3.1): the identity in the lepton sector (the rotor axis *is*
the winding blade; the Hodge-dual axis is excluded there) and the `I₄` Hodge map in the quark
sector — so R-005's two-faces coupling should not be read as "the visible rotor axis is always
the Hodge dual." The
wave-drive operates at the rotor's frequency, sustaining the defect as a driven attractor; `ω` is
what *holds* the spatial winding against substrate relaxation. So mass is not just "what mass is"
kinematically — it is the dynamical sustainer of the defect's stability under the wave-drive.
**Mass is what the defect's persistence costs the substrate.**

### Spin and mass — two faces of the defect

Spin arises from the `Spin(3)` action on `𝒮` (§A.2, §A.5). Mass arises from the meta-time rotor's
frequency advancement along `τ_5`. The two act on **different (orthogonal) blades** of the
Clifford algebra — spin on the L-orbit spatial bivectors via the rotor sandwich, mass on the
`ℍ`-subalgebra meta-time rotor via right-action phase. In free-field linearization a configuration
can carry spin without mass (the photon: zero meta-time frequency, nonzero spin) or both (an
electron), so the two are independently parametrizable as algebraic observables.

In matter, the two are **dynamically coupled through the defect** (R-005). Per §A.3 the spatial
winding (which the spin field carries) and the meta-time rotor (which mass measures) are two
faces of one circular geometric object related by the `I_4` Hodge map. The algebraic separability
is what lets us *discuss* spin and mass as distinct observables on a fluctuation; the dynamical
coupling is the substrate fact that for a defect, the spin field carries the topology and the
meta-time rotor sustains it. **Two faces of one object, not two independent observables.**

### Meta-time and observable time

`τ_5` is the wave's propagation parameter through the substrate. Observer time `τ` is the rate of
internal change a wavefront-locked configuration registers against the homogeneous vacuum. **Both
are real.** We do not yet know how meta-time ultimately appears in observation beyond the
wavefront-locked identification `τ = τ_5` on the front; that is part of the open frontier (§D.5,
§E.1).

The relation `E = mc²` is the structural identity between two readings: mass is the meta-time
rotor frequency; energy is the broader category including this frequency and the rest of what the
configuration is doing. On the wavefront, `x_4 = c_meta · τ_5`. The observer's `c` agrees with
`c_meta` *on average across the wavefront* (R-045); local variations near mass concentrations are
predicted (§B.6, §B.7) but small. The §B.2 Fourier-at-`k_4` reduction makes the on-average
identification rigorous — the same `c` enters the Klein–Gordon dispersion as enters the kinematic
constraint `x_4 = c_meta · τ_5`. Sector- or epoch-varying differential `c_meta` is canonical
falsifier §E.3 row 8.

### Quarks are not stable independent objects

A canonical commitment, load-bearing through Part C and beyond. A quark in TWT is not an
independent stable object — it is a **facet** (a decomposition-component) of a hadron defect
(R-008, R-053). The "three quarks in a baryon" are three orthogonal facets of one circular winding
in the Q-orbit, not three independently existing objects bound together by a force. Mesons admit
an analogous decomposition (§C.5). During high-energy hadron collisions, transient quark-like
degrees of freedom appear and disappear within a fraction of the wavefront's transit time —
entirely consistent with the framework's continuous-substrate ontology, where short-lived
field-configuration fluctuations are exactly what one would expect.

Quark masses **remain useful as mathematical abstractions** — they parametrize how the facet's
geometric and dynamic properties shift the mass of the host hadron. What TWT commits to is mass
**scope**: **the framework abstains from considering quark masses independently.** The
mass-bearing objects are hadrons (baryons and mesons). Per-flavour MS-bar quark masses, treated as
indicators of facet structure, are useful for parametrizing hadron-mass derivations but are not
standalone *verifiers* of TWT predictions. An apparent disagreement between a TWT quark-property
prediction and an SM quark current mass is an indicator-level signal, not a falsification.

Three consequences worth flagging here:
- The baryon mass formula (§C.1) acts on hadron-level mass eigenvalues, not quark masses.
- The up-sector eccentricity ratio `ε_u/ε_d = 2^{3/2}` (§C.3.10 — a candidate rule of the
  quark-sector epicycle parametrization) matches the *ratio* of two
  hadron-indicated quark masses (u, c) but is structurally untestable against `m_t` because no
  top hadrons exist.
- The top quark exclusion `Γ_t · Θ_0 ≈ 7.2 ≫ 1` (§C.5) — the top facet unwinds before the baryon's
  circular winding can complete. The top has no hadrons, by the framework's own prediction;
  consequently the top mass is a Standard-Model bookkeeping number, not a TWT verifier.

---

## §A.5 — Mathematical setting (just enough algebra)

The minimum Clifford-algebra fluency needed to read Part B. Each sub-block does one specific job
in the hooks that follow. The full algebra returns at §D.1–§D.2 for the reader who wants the
machinery; here we keep it lean.

### A.5.1 Generators and grades

`Cl(4,0)` is the real Clifford algebra with four generators `{e_1, e_2, e_3, e_4}` satisfying

> `e_i² = +1`, `e_i e_j = −e_j e_i` for `i ≠ j`.

It is 16-dimensional as a real vector space, with grade-dimensions `(1, 4, 6, 4, 1)`: one scalar,
four vectors, six bivectors, four trivectors, one pseudoscalar. **Reverse** is the involutive
antiautomorphism `(e_{i_1} ⋯ e_{i_k})~ = e_{i_k} ⋯ e_{i_1}`. **Grade projection** `⟨X⟩_k` returns
the grade-`k` component of `X`. As a real algebra, `Cl(4,0) ≅ M_2(ℍ)` by Bott periodicity (R-092 in
full at §D.1).

### A.5.2 Bivectors as rotation planes — the L/Q split, the symmetric pair, the fibration

The six bivectors split into two physically distinct triples (R-009):

- **L-orbit** `𝓛 = {e_{12}, e_{13}, e_{23}}`: the three `e_4`-free planes. Under commutator they
  close as `so(3)`. These are the spatial rotation generators; `exp(𝓛) = Spin(3)`.
- **Q-orbit** `𝓠 = {e_{14}, e_{24}, e_{34}}`: the three `e_4`-bearing planes. Each squares to `−1`
  too, but they involve the propagation direction and so play a different role — observer's spatial
  frame, quark winding-sector host, and the `V_4⊥` chart on which the generation circle is
  sampled (§C.3.1; the generation `Z_3` itself is meta-time phase, §C.3.9).

Both triples are 3-dimensional bivector triples; both square element-wise to `−1`. The split is
orthogonal under the bivector inner product (`⟨A B⟩_0`).

**A symmetric-pair structure on so(4).** The bracket relations are

> `[𝓛, 𝓛] ⊆ 𝓛`,  `[𝓛, 𝓠] ⊆ 𝓠`,  `[𝓠, 𝓠] ⊆ 𝓛`,

which is exactly the Cartan relation of a *symmetric pair* `so(4) = 𝓛 ⊕ 𝓠`, with `𝓛` the isotropy
subalgebra and `𝓠` the coset complement. Concretely:

- `𝓛` is the **diagonal `Spin(3) ⊂ Spin(4)`** — the stabilizer of `e_4`. It closes, so
  `exp(𝓛) = Spin(3) ≅ S³_𝓛` is a genuine subgroup; leptons wind into it cleanly
  (`π_3(Spin(3)) = ℤ`).
- `𝓠` is the **tangent space of the coset `Spin(4) / Spin(3) ≅ S³_𝓠`**. It does *not* close —
  and that is not a defect, it is the definition of a symmetric-space complement. Baryons wind
  into the coset `S³_𝓠`, which still has `π_3 = ℤ` because the coset is a 3-sphere.

So `exp(𝓛)` and "`exp(𝓠)`" are not parallel constructions: the L-orbit hosts a subgroup, the
Q-orbit hosts a coset. Lepton hedgehogs are subgroup-valued maps; baryon hedgehogs are
coset-valued maps. Both yield a `ℤ` winding degree, but via topologically different targets
(§C.1 returns to this).

**The fibration bridges the chiral and orbit bases.** The fibration

> `Spin(3) ↪ Spin(4) ↠ S³_𝓠`  (= `Spin(4) / Spin(3)`)

has `π_2(Spin(3)) = 0`, so the long exact sequence reduces to

> `0 → π_3(Spin(3)) → π_3(Spin(4)) → π_3(S³_𝓠) → 0`,  i.e.  `0 → ℤ → ℤ × ℤ → ℤ → 0`.

The pair `(n_𝓛, n_𝓠) = (`fiber winding into the diagonal `Spin(3)`, base winding into the coset
`S³_𝓠)` is therefore a perfectly valid basis for `π_3(Spin(4)) = ℤ × ℤ` — it is a *change of basis*
from the chiral `(n_+, n_−)` basis the `Spin(4) = SU(2)_+ × SU(2)_−` factorization produces. The
two splits live on the same total `ℤ × ℤ`; they pick different `ℤ × ℤ` bases of it. **This is the
bridge promised at §A.2.** Lepton-into-`𝓛` and baryon-into-`𝓠` is therefore a coset-respecting
relabeling of a chiral counting, not a re-identification of the chiral split with the orbit
split (which would be false).

That sorted out, the L/Q split organizes nearly everything in Parts B and C.

### A.5.3 The pseudoscalar `I_4` and Hodge duality

The pseudoscalar is `I_4 = e_1 e_2 e_3 e_4`. Direct computation gives `I_4² = +1` (R-010) —
a real duality, **not** an imaginary unit. Left-multiplication by `I_4` interchanges the L-orbit
and Q-orbit triples bivector-for-bivector:

> `I_4 · e_{12} = −e_{34}`,  `I_4 · e_{13} = +e_{24}`,  `I_4 · e_{23} = −e_{14}`  (and similarly).

This is the **Clifford** Hodge action on grade-2.

A convention note. The form-side metric Hodge star `⋆` (familiar in the convention
`⋆e_{12} = +e_{34}`) and Clifford left-multiplication `I_4 ·` differ by an overall sign on grade-2
in `Cl(4,0)`:

> `⋆ ω = −I_4 · ω`  for bivectors `ω`.

Both operations interchange `𝓛 ↔ 𝓠`; they assign opposite `±1` labels to the same bivector.
**Throughout this paper, "self-dual" means `+1` eigenvector of `I_4 ·`** — so `e_{12} − e_{34}`
is self-dual (consistent with §A.2), and `e_{12} + e_{34}` is anti-self-dual. If you import a
result stated under the form-Hodge convention, flip the sign.

The Hodge map (in either sign) is what couples a defect's spatial-winding face to its
meta-time-rotor face (R-005), and is the L↔Q algebraic connector behind β-decay (§C.5) and the
EM strain modes (§B.5).

### A.5.4 The spinor minimal left ideal

`s_0 := (1 + e_4)/2` is an idempotent: `s_0² = s_0` (direct check). The minimal left ideal of
`Cl(4,0)` is

> `𝒮 = Cl(4,0) · s_0`,

real dimension 8, quaternionic dimension 2 (R-012). Spinors are elements of this ideal; the wave
field `Ψ` of §A.3 takes values here. **This is where QM lives.** (For the full grade dictionary —
primitive idempotents in Cl(4,1), Dirac spinor as `M_2(ℍ)`-module, the chiral split into Weyl
ideals, the ASD generation triple, the SD ↔ ASD mirror — see §D.2.)

### A.5.5 Rotors and the rotor sandwich

A rotor is `R = exp(θ B/2)` for a simple unit bivector `B` (`B² = −1`). It acts on Clifford
elements in two ways:

- **One-sided** on spinors `ψ ∈ 𝒮`: `ψ → R ψ`. Under `R(2π) = exp(π B) = −1`, the spinor picks
  up a sign: `ψ → −ψ`. Spinors return to themselves only after `4π`. This is the half-angle, the
  SU(2) double cover, the source of the Tsirelson bound `2√2` (§B.4).
- **Two-sided** (the sandwich) on vectors and trivectors: `v → R v R̃`. Under `R(2π) = −1`,
  `(−1) v (−1)~ = v`. Vectors return to themselves after `2π`.

The half-angle structure of one-sided action and the full-angle structure of the sandwich are
both load-bearing later (R-011).

### A.5.6 Cl(4,1), the meta-time phase, and a grounding rule

When meta-time `τ_5` is made explicit, the algebra extends to `Cl(4,1)` with an extra generator
`e_5`, `e_5² = −1`. The central element `E := I_4 · e_5` satisfies `E² = −1` and supplies the
global geometric complex unit — the "external `U(1)` phase" that QM uses (R-012a). The native
formalism throughout this paper is `Cl(4,0) + ℍ`: the `ℍ` factor of `Cl⁺(4,0) ≅ ℍ ⊕ ℍ` supplies
the QM complex unit `i = e_{12}` (a transverse simple bivector); `Cl(4,1)` is the same content with
`e_5` written explicitly, useful when meta-time dependencies need to be tracked through a
calculation.

Why two complex structures coexist. `E` is **central** (it commutes with everything) and **global**
— it gives a single `U(1)` phase that any configuration can carry. `i = e_{12}` is a specific
**transverse simple bivector**, forced **per-defect** by the `(W) ∩ (S) ∩ (E)` centralizer
intersection of §B.3.1. Both square to `−1`, but for different structural reasons (a central
unit with `E² = −1` vs. a transverse simple bivector with `B² = −1`). They live at different
algebraic positions and do different jobs; identifying which is in play is just reading what
acts on what.

**One conceptually startling fact, named once.** The axis a wavefront-locked observer reads as
*time* is `e_4` with `e_4² = +1` — a bulk *spatial* axis in the Euclidean substrate. The *genuine*
evolution direction the wave actually advances along is the meta-time generator `e_5` with
`e_5² = −1` — the one carrying timelike signature. Observer-time is what bulk-space *reads as*
once the wavefront isomorphism (R-014/R-015 in §B.1) turns the substrate's compact `so(4)` into
the observer's non-compact `so(1,3)`; meta-time `τ_5` is what the wave evolves in. The Lorentzian
signature observers attribute to "their time" is therefore an artifact of the isomorphism, not a
property of `e_4` per se. (The full force of this is felt at §B.1.)

A grounding rule used throughout. A `Cl(4,1)` construction is *grounded* iff its `e_5`-content
reduces to PHASE in the `Cl(4,0) + ℍ` picture — that is, `e_5` appears only via the central
element `E`, or as the meta-time axis of the rotor frequency `ω` (= mass). A construction that
needs `e_5` as a *spatial* degree of freedom (a new winding direction, a soliton coordinate, a
propagation axis) is an escape from the framework's ontology, not physics. Rebuild it in
`Cl(4,0) + ℍ` and the spurious dimension disappears. (Full `Cl(4,1)` treatment at §D.1.)

That is the algebra. The next part of the paper uses it; the observer's gamma matrices
`γ⁰ := e_4`, `γʲ := e_4 e_j` are introduced and verified in §B.1.

---

# Part B — What the framework gives you, fast

*The framework's spine. Each chapter opens with the small mathematical addition it needs (a 5–15
line "Mathematical setting" block), then delivers its hook.*

---

## §B.1 — Lorentzian signature

The wavefront isomorphism is the framework's cleanest spine result. We will show that the
Euclidean substrate algebra `Cl(4,0)` is the *same real algebra* as the Lorentzian spacetime
algebra `Cl(1,3)`, realized through a specific embedding rather than a generator-by-generator map.
The Lorentzian signature of observed spacetime is the algebraic shadow of a wavefront-locked
observer in a Euclidean substrate — not an independent postulate.

**Mathematical setting.** A dimension-preserving algebra homomorphism between simple real algebras
is an isomorphism. Both `Cl(4,0)` and `Cl(1,3)` are 16-dimensional and `≅ M_2(ℍ)` as real
algebras. The neighbouring algebras `Cl(3,1)` and `Cl(2,2)` are isomorphic to `M_4(ℝ)`, a
*different* real algebra. So the question "which signature does the wavefront construction
realize" is a question about which real algebra it lands on.

### B.1.1 Building Cl(1,3) inside Cl(4,0)

Take the observer's gamma matrices to be the following specific elements of `Cl(4,0)`:

> `γ⁰ := e_4`, `γʲ := e_4 e_j` (`j = 1, 2, 3`).

These are constructed from the only ontologically distinguished multivector `e_4` (the wave's
propagation axis, §A.1) plus the three spatial generators of §A.5.1. They are specific elements
of `Cl(4,0)`, not abstract generators of a separate algebra. The naive
direct map `Cl(4,0) → Cl(1,3)` with `e_j ↦ γ^j` would fail at the algebra level since `e_j² = +1`
while `(γ^j)² = −1` is required by `Cl(1,3)`. Our construction goes the other way: `Cl(1,3)` is
embedded inside `Cl(4,0)` via the wavefront prescription. We now check that it satisfies the
`Cl(1,3)` Dirac relations `{γ^μ, γ^ν} = 2 η^{μν}` with `η = diag(+1, −1, −1, −1)`.

**Time-time.** `(γ⁰)² = e_4² = +1`. ✓

**Space-space, equal indices.** Using `e_j e_4 = −e_4 e_j`,
`(γʲ)² = (e_4 e_j)(e_4 e_j) = e_4(e_j e_4)e_j = −e_4² · e_j² = −1`. ✓

**Time-space.** `{γ⁰, γʲ} = e_4(e_4 e_j) + (e_4 e_j)e_4 = e_j + e_4 e_j e_4 = e_j − e_j = 0`. ✓

**Space-space, distinct indices.** For `i ≠ j`, `γ^i γ^j = (e_4 e_i)(e_4 e_j) = −e_i e_j` and
`γ^j γ^i = +e_i e_j`, so `{γ^i, γ^j} = 0`. ✓

All four hold. The map `φ` sending the four `Cl(1,3)` generators to these four elements of
`Cl(4,0)` extends to a real-algebra homomorphism (R-013).

### B.1.2 φ is an isomorphism

`φ` maps four generators of `Cl(1,3)` to four elements satisfying the `Cl(1,3)` relations,
extending to an algebra homomorphism. Both source and target have real dimension 16, both are
isomorphic to `M_2(ℍ)` — `Cl(4,0)` by Bott periodicity, `Cl(1,3)` as the standard spacetime
algebra. A dimension-preserving homomorphism between simple algebras is an isomorphism.

**`φ` is an isomorphism of real algebras** (R-014). And crucially, the neighbouring algebras
`Cl(3,1)` and `Cl(2,2)` are `≅ M_4(ℝ)`, a *different* real algebra from `M_2(ℍ)`.

> **The wavefront construction lands on the (1,3) partner, not the (3,1) or the (2,2).**

The real Clifford algebra of observed spacetime is *forced* to be `M_2(ℍ)`, by the wavefront
geometry, rather than `M_4(ℝ)`. The overall metric *sign convention* — `(+, −, −, −)` versus
`(−, +, +, +)` — remains conventional; what the wavefront construction determines is the **algebra
type**, not the sign convention.

### B.1.3 What the bridge says

The Euclidean bulk `Cl(4,0)` and the Lorentzian spacetime `Cl(1,3)` are *the same algebra*,
relabeled through `φ`. The sign flips `(γʲ)² = −1` follow from the relabeling, not from indefinite
structure in the substrate. From outside the wave everything is Euclidean; from inside locked to
the wavefront the same algebra reads as Lorentzian (R-015). Neither description is more fundamental
as algebra; the substrate is fundamental, and the Lorentzian reading is the observer's.

This result has two distinct components that should not be conflated:

- **Algebra-level fact**: `Cl(4,0) ≅ Cl(1,3) ≅ M_2(ℍ)` as real associative algebras. This is a
  theorem about Clifford algebras; it holds independently of any observer.
- **Observer reading**: an observer locked to the wavefront *reads* the propagation generator
  `e_4` as the time axis. This is not derived from the algebra; it is the wavefront-locking
  premise A-3.

The Lorentzian signature of observed spacetime is the *conjunction* of the two. The algebra
identity tells you `Cl(4,0)` is *available* as `Cl(1,3)`; the observer stipulation tells you which
generator gets read as `γ⁰`. Without the second the same algebra reads as Euclidean; without the
first the wavefront reading would not land on the `(1,3)` partner. The cleanness of the result is
that both inputs are honestly accounted for — one is a theorem, the other a labeled premise — and
nothing else is smuggled.

### B.1.4 The observer's spatial basis as bivectors

Under `φ`, the observer's three spatial axes `γʲ = e_4 e_j` are *bivectors* of the substrate, each
a 2-plane containing `e_4` and one absolute-spatial direction. **The observer's "space" is
literally built from the propagation direction**: every spatial direction is a plane through the
wave's line of travel.

The Q-orbit bivectors `{e_{14}, e_{24}, e_{34}}` thereby acquire a triple role:

- (a) the observer's spatial frame under `φ` (this section)
- (b) the quark winding-sector hosts (per §C.1)
- (c) the `V_4⊥` chart sampled by the Brannen generation circle (§C.3.1; the generation `Z_3`
  itself is meta-time phase, §C.3.9)

**One algebraic structure, three roles.** Visible only because the description is bivector-native
rather than vector-decomposed.

### B.1.5 Matter-as-defect Lorentz protection

A free-standing principle used throughout the framework wherever emergent Lorentz invariance is at
stake: **all matter species inherit the substrate's one light cone exactly because they are
defects of one field** (R-016). This is best read as a *structural advantage*, not a defensive
safety check.

Matter is not `N` independent fundamental fields each with its own kinetic term. Matter is
windings, solitons, and textures of the *one* substrate rotor field (R-004). A defect inherits the
substrate light-cone exactly: it is the boosted rest solution of the field-theoretic dynamics, and
its dispersion is `E² = M² + p²` with the speed in that relation being the *field's* light-cone,
not a coefficient the defect carries on its own. A second defect of different width and mass obeys
the same dispersion with the *same* `c`. **Different rest masses, one light-cone. Relative-boost
Lorentz violation between two matter species is structurally zero, not tuned** — because there is
no independent coefficient for it to live in. Both defects are reading the one substrate's clock.

This defuses a well-known obstacle. Programs that treat Lorentz invariance as emergent from a
preferred-frame substrate face a radiative-naturalness problem (Collins, Perez, Sudarsky,
Urrutia & Vucetich 2004, PRL 93, 191301): with a hard, frame-dependent cutoff, loops feed dimension-six
Lorentz violation *down* into dimension-four marginal operators with coefficients
`δ_rad ~ g²/(16π²) ~ 10⁻³` to `10⁻²`. Against the `~10⁻²⁰` matter-sector bound this misses by 17
orders. **The naturalness obstacle presupposes its precondition**: `N` independent fundamental
fields with `N − 1` relative-speed observables. **TWT denies the precondition**: one field,
defects, one light-cone — the species the mechanism would split are not there to be split. This is
an *offensive win*: it is a reason the construction *succeeds where the genre generically fails*,
not a defense survived by tuning.

The complementary rotational-anisotropy bound is closed by the D4 cubic point group, which forbids
dimension-four anisotropy at all orders and pushes the leading anisotropy to dimension six. The two
protections together leave the residual at dimension six `(E/Λ)²`, set by the defect's own form
factor.

---

## §B.2 — Special relativity

Special relativity, in this framework, is the algebra of the wavefront isomorphism, read as
kinematics. The Lorentz invariance the reader knows from SR is the symmetry of the algebra the
observer's frame already is; it is not an added postulate.

**Mathematical setting.** Fourier reduction at fixed `e_4`-momentum identifies the rest mass with
the `e_4`-Fourier label `k_4`. The boost generators `K_j` have `K_j² = +1/4` (non-compact:
`exp(ζ K_j)` gives `cosh, sinh`); the rotation generators `J_i` have `J_i² = −1/4` (compact:
`exp(θ J_i)` gives `cos, sin`). The compact bulk `so(4)` will read as the observer's non-compact
`so(1, 3)` through `φ`, as §B.2.2 develops.

### B.2.1 Klein–Gordon from the 5D hyperbolic master

The linearization of the master wave equation (§D.4) **around the canted vacuum** — not around a
defect — gives the free 5D hyperbolic form

> `c_meta⁻² ∂_{τ_5}² Ψ = (∂_1² + ∂_2² + ∂_3² + ∂_4²) Ψ`.

This is **5D hyperbolic**: timelike in `τ_5`, with 4D Euclidean spatial slices. The
*vacuum-linearization* is what produces a free wave operator; a defect, when present, enters
separately as a classical potential `V(x)` (§B.3.4), exactly as standard QM consumes it.
§D.4.6 carries the full derivation and the rationale.

The naive substitution "`∂_4|_wavefront → c_meta⁻¹ ∂_τ`" is a kinematic constraint, not a signature
flip; it identifies operators acting on different coordinates of the 5D problem and does not
produce KG. **The correct reduction is Fourier decomposition at fixed `k_4`.** Substrate modes
carry a definite `e_4`-momentum, identified with rest mass (§A.4, R-007). Writing

> `Ψ(τ_5, x, x_4) = exp(i k_4 x_4) · φ(τ_5, x)` (with `i = e_{12}` per §A.5.6)

and substituting,

> `c_meta⁻² ∂_{τ_5}² φ = (∂_1² + ∂_2² + ∂_3²) φ − k_4² φ`,

which rearranges to

> `c_meta⁻² ∂_τ² φ − ∇_3² φ + m² φ = 0` ⇔ `(□_{1,3} + m²) φ = 0` (R-017),

with `τ_5 = τ` on the front and `m = k_4`. This is the **Klein–Gordon equation in the observer's
Lorentzian frame**, derived from the substrate's 5D hyperbolic master by Fourier reduction at the
`e_4`-momentum that the observer reads as rest mass.

*The `ω ↔ k_4` identification, made exact (R-123).* The rest-mass identification this reduction
consumes — the defect's meta-time rotor frequency `ω` (R-007) numerically equal to the
fluctuation label `k_4` — has a derived core and two named residues. Derived core: restricting
the meta-time rotor to the wavefront lock `x_4 = c_meta · τ_5` (§A.4) yields exact
`x_4`-periodicity at `k_4 = ω/c_meta` — the chain rule, axis-independent (any simple `û` with
`û² = −1`, including the central `E`). The two named residues — numbered **(ii)** and **(iii)**
after the derived restriction core, the labels the cross-references throughout this paper use —
are: **(ii)** that the vacuum-linearized one-particle sector of a defect-bearing region sits
*at* this `k_4` (the identification the reduction above actually consumes — the §D.4.6
soliton-fluctuation Paper-2 question), and **(iii)** which complex unit (the central `E` vs the
defect-selected transverse `B_a` of §B.3.1) carries the front phase. Residue (ii)'s
existence/location half is derived by symmetry (R-125, §D.4.6): the defect's phase collective
mode sits exactly at `k₄ = ω/c_meta`; its identification half — normalizability and uniqueness
as *the* one-particle pole — is answered at the structural level by R-142 (§D.4.6), with
uniqueness conditional on a named set of structural premises, leaving the kernel-level tail
condition and the absolute anchoring face as the surviving opens. Residue (iii) is resolved as
a selection (R-127, §B.3.1): only `û = ±B_a` reads as a propagating phase in the observer's
forced complex line, so the mass phase rides the winding blade itself and no `E → B_a`
conversion is owed; `E` is excluded as the visible carrier.

**Signature convention.** Throughout the paper `□_{1,3} = c⁻² ∂_τ² − ∇_3²` and the metric is
`η = diag(+, −, −, −)`, so the `(□ + m²) φ = 0` form above carries `+m²`. A reader importing the
`(−, +, +, +)` convention will see the sign of the `m²` term flipped; nothing else changes.

The induced Dirac operator `𝒟 = γ⁰ c_meta⁻¹ ∂_τ + γʲ ∂_j` squares (using §B.1.1's Cl(1,3) Dirac
relations) to `𝒟² = □_{1,3}`. So `𝒟² φ = −m² φ` is just the Lorentzian KG form, recovered as a
factorization.

Time dilation, length contraction, the constancy of `c` are all consequences of being a
wavefront-locked configuration of a 5D hyperbolic wave, with rest mass identified as the
`e_4`-Fourier label. The observer's effective speed `c` *is* `c_meta`: the same `c` enters the KG
dispersion as enters the kinematic constraint `x_4 = c_meta · τ_5`.

### B.2.2 Boosts and rotations, Thomas precession

The Lorentz generators are the grade-2 sector of the induced algebra (R-018):

> `K_j = (1/2) γ⁰ γ^j = (1/2) e_j`, `J_i = (1/2) γ^j γ^k = −(1/2) e_{jk}` (cyclic).

Their squares give the compact/non-compact distinction explicitly: `K_j² = (1/4) e_j² = +1/4`
(non-compact — boosts give cosh/sinh, hyperbolic), `J_i² = (1/4) e_{jk}² = −1/4` (compact —
rotations give cos/sin, circular).

The bulk Q/L split is *not* the boost/rotation split. All six bulk bivectors `e_{ab}` square to
`−1` and close as compact `so(4)`. The element `e_{i4} ∈ 𝓠` equals `−γ^i` under `φ` — a Dirac
matrix, not a Lorentz generator. The genuine boost `K_j = (1/2) e_j` is a `Cl(4,0)` *vector* with
square `+1`. **The bulk's compact `so(4)` becomes the observer's non-compact `so(1, 3)` because
`φ` gives `e_4` timelike character.** Q/L organizes particle spectrum; boost/rotation organizes
relativistic kinematics; they are related by `φ` but they are not the same partition.

The Lorentz algebra closes from the Clifford relations (R-018):

> `[J_i, J_j] = ε_{ijk} J_k`,
> `[J_i, K_j] = ε_{ijk} K_k`,
> `[K_i, K_j] = −ε_{ijk} J_k`.

The minus sign in the last bracket is the signature of `so(1, 3)` rather than `so(4)` — **Thomas
precession in algebra form** (R-019). It is the cleanest possible expression of the fact that
boosts close to rotations only with a sign, and that sign is the Lorentzian one.

**The finite boost orbit and the mass shell (R-132).** The generator-level facts above extend to
the finite orbit, computed entirely inside `Cl(4,0)`: the boost element
`B_ζ = exp(ζe_j/2) = cosh(ζ/2) + sinh(ζ/2)·e_j` is hyperbolic (because `e_j² = +1` — the same
Euclidean signature fact that keeps the `e_{i4}` rotations circular), adds rapidities exactly,
and acts on the γ-frame as a genuine Lorentz transformation:
`B γ⁰ B⁻¹ = cosh ζ · γ⁰ − sinh ζ · γʲ`, with the `η`-signs riding the derived Dirac relations
rather than an imported metric. Applied to the rest one-particle label `k̸ = m γ⁰` (with
`m = k₄ = ω/c_meta`, the §D.4.6 front label of the defect), the orbit is exactly the mass shell:
`(E, p) = m(cosh ζ, sinh ζ)` with `E² − p² = m²` — exact algebraically (conjugation preserves the
Clifford square) and componentwise, for generic boost directions and boost-rotation compositions.
This hands the dispersion relation a *kinematic* second route, independent of §B.2.1's dynamical
Fourier-reduction route over their shared foundations — the isomorphism and the front label.
That each moving label is realized by an actual moving defect solution is a named premise of
this result, the same class §B.5.5's force law carries.
One algebraic caution: in `Cl(4,0)` reversion fixes vectors, so `B̃ = B ≠ B⁻¹`
and the familiar `R·x·R̃` sandwich applied to `B` is a *silent no-op* (`Bγ⁰B = γ⁰`
exactly); the correct action `B·x·B⁻¹` is what equals the `Cl(1,3)`-reversion rotor sandwich
through the isomorphism, which fails to intertwine the two reversions precisely because it is
not grade-preserving at the boost planes.

---

## §B.3 — Quantum mechanics from one move

The five postulates of standard quantum mechanics are independent axioms. In TWT they are
consequences of Face-1 linearization of the wave equation around the **canted vacuum**, combined
with the wavefront isomorphism — *with a defect, when present, entering as a classical
background potential `V(x)` on top of the free wave operator*. **QM in TWT is the linearized
theory of free fluctuations of the substrate plus a defect-sourced classical potential, not a
theory of the defect fields themselves.**

The unifying claim, stated once: **the five independent QM axioms collapse to a single geometric
operation — projecting the 4D-oriented fluctuation onto the observer's 3D wavefront frame.** From
that one move everything follows: the transverse `e_{12}` rotation plane supplies the complex unit
`i` (Postulate 1); the Spin(4) bilinear projected to grade 0 supplies the Born measure
(Postulate 3); the hyperbolic KG parent supplies Schrödinger and Dirac evolution (Postulate 4);
and the one-sided rotor half-angle supplies the interference structure that yields the Tsirelson
bound `2√2` (§B.4).

Equally important is what TWT does **not** claim. It does not re-prove Gleason's theorem — it
supplies, from substrate structure, the hypotheses that theorem consumes (§B.3.3) — it does not
make Pauli exclusion an algebraic identity in bare SU(2), and it does not beat Bell's theorem.
Each non-claim is flagged where it arises, and the restraint is part of the result.

**The uncertainty principle is emergent in this framework, not primitive.** Position-momentum
non-commutativity follows from the rotor-sandwich structure on the spinor ideal plus the Born
projection of §B.3.3: position and momentum are not separately fundamental observables of the
substrate; they are *derived* readings on the linearized fluctuation, and their commutator
inherits the bivector-product structure of the underlying Clifford algebra. No `[x, p] = iℏ`
postulate is imported.

**Mathematical setting.** Linearize around the **canted vacuum** `Ψ_vac` (§D.4.6): the
fluctuation `Ψ = Ψ_vac + δΨ` satisfies the free linearized wave equation of §B.2.1. A defect
configuration `Ψ_def` (a Skyrmion of §C.1), when present, enters this linearized equation as a
classical source — its static profile contributes the potential `V(x)` that §B.3.4 below
identifies as Schrödinger's `V`. Linearized fluctuation theory is exactly
linear, exactly complex (with a transverse simple bivector providing `i`), exactly unitary; the
defect sector is none of those. The background selects a direction; the low-energy fluctuation is
transverse in one bivector rotation plane.

### B.3.1 Postulate 1 — complex Hilbert space, but the subspace is forced

A naive route would say "QM uses complex numbers; the framework supplies them via the transverse
bivector `B = e_{12}`." The deeper derivation runs the other way (R-020).

Per §A.3, the soliton background is `Ψ_def = F(χ) · B_a · s_0 · q_h(τ_5)`, with a single chosen
winding direction `B_a` from the L-orbit triplet `{e_{12}, e_{13}, e_{23}}` (for the lepton sector;
the baryon Q-orbit case is structurally analogous). The spinor fluctuation `ψ` lives in the even
subalgebra `Cl⁺(4,0)` (eight blades). Three substrate conditions on a rotor element `X` acting on
`Ψ_def` by left-multiplication:

- **(W)** wavefront-frame: `[X, e_4] = 0` (L-orbit).
- **(S)** soliton-background preserving: `[X, B_a] = 0`.
- **(E)** even-grade: `X ∈ Cl⁺(4,0)`.

The intersection `(W) ∩ (S) ∩ (E)` is exactly `{1, B_a}` — a 2-dimensional
commutative subalgebra closed under multiplication: `1 · 1 = 1`, `1 · B = B = B · 1`, `B · B = −1`.

So the complex structure `i := B` is the *derived consequence* of the subalgebra — any element
with `B² = −1` generates a `U(1)` phase — not its premise. **One-way derivation chain:**

> §A.3 defect ansatz + wavefront frame ⇒ `{1, B}` ⇒ complex structure ⇒ Born projection.

**Reconciliation with §D.4.6's vacuum-linearization.** §D.4.6 derives the *free wave operator*
by linearization around the canted vacuum — no defect needed for the free propagator. The
complex-structure derivation here uses a *different* role for the defect: the defect's winding
direction `B_a` selects which transverse simple bivector represents the QM complex unit. The
defect doesn't change the wave operator (it sources a classical potential `V(x)` on the same
free operator, §B.3.4); it only **orients** the complex structure by picking out `B_a` from
the L-orbit triplet. If no defect is present, condition (S) is empty, the centralizer of just
`e_4` in `Cl⁺(4,0)` is 4-dimensional `{1, e_{12}, e_{13}, e_{23}}`, and there is no unique
complex line — exactly the SO(3) ambiguity of free space, which a defect breaks by selecting
one orientation. So vacuum-linearization (§D.4.6) gives the free propagator; defect presence
adds the potential `V(x)` *and* fixes the complex unit `B_a` per defect. The free wave operator
and the complex structure are linearized at the same point (the vacuum), but the complex
structure's *orientation* is supplied by the defect when one is present.

The fluctuation field is then

> `ψ(r) = f(r) + g(r) · B`, with `f, g : ℝ³ → ℝ`,

isomorphic to complex-valued functions (R-021). The inner product

> `⟨φ | ψ⟩ = ∫ ⟨φ̃ ψ⟩_0 d³r`

evaluates (since `B̃ = −B` for a simple bivector) to `∫ (f_φ f_ψ + g_φ g_ψ) d³r`, the standard `L²`
inner product. A global phase `ψ → ψ · exp(α B)` leaves `ρ = ⟨ψ̃ ψ⟩_0` invariant; states are rays.
**Projective Hilbert space is a theorem.**

A frame-equivalence note. The bivector `B` is taken as `e_{12}` for presentational uniformity, but
the structural content is independent of which simple bivector represents the transverse plane.
All such choices are related by spatial rotations and give equivalent physical content. No
load-bearing claim depends on `B = e_{12}` specifically.

**The mass phase rides the same blade (R-127).** Which unit carries the front mass phase `k₄`
in this forced complex line — the meta-time rotor axis `û` was left free by §B.2.1's restriction
identity (R-123, residue (iii)). Projecting the defect's rotor history `B_a·s₀·q_h(τ₅)` onto the
line `{1, B_a}` settles it as an exact dichotomy: only `û = ±B_a` — the defect's *own winding
direction*, the very blade the centralizer above forces as `i` — stays in the line as a pure
propagating phase, at exactly `ω` (front `k₄ = ω/c_meta`). Any other `ℍ`-axis reads instead as
spin *precession* into the orthogonal state sector (an amplitude-modulated shadow in the line),
and the central `E` leaves the observer's `Cl(4,0)` ideal entirely (its shadow would be density
*nodes* along `x₄`, not a phase). So, given the §A.3 ansatz and the fact that the observed
one-particle mode *is* a propagating phase (this is what interferometry sees), the hand-off
residue resolves as a **selection**: there is no `E → B_a` conversion to construct — the
observer-visible mass phase never leaves `B_a`. One blade, two roles: topological winding
direction and the QM complex unit carrying the mass phase — §A.3's "two faces of one defect"
made exact. `E` retains its global/colour complex-structure role (§B.5b, §D.1); the conjugate
sign `−B_a` is the antiparticle branch. Named open: an EOM-level derivation of the axis lock
(here consistency-forced, not dynamical); the baryon Q-orbit analog is constructed next.

**The Q-orbit analog: the quark-sector lock is the Hodge dual, and it is parity-odd (R-128).**
Running the same centralizer and projection machinery for a defect with a *Q-orbit* winding
`B_q ∈ {e₁₄, e₂₄, e₃₄}` — the same observer, conditions (W)∩(S′)∩(E) — forces the complex line
`{1, I₄B_q}`: the observer's `i` for a baryon-sector defect is the **Hodge dual** of its winding
(up to sign), and the mass phase locks to `û = ±I₄B_q` (exact dichotomy; the winding axis itself
leaks into the complementary idempotent sector; `E` exits the ideal as before). The two sector
locks then differ in one structurally loaded way: the lepton lock (identity on the winding
blade) is parity-**even**, while the quark lock (multiplication by `I₄`) is parity-**odd** —
`P(I₄X) = −I₄P(X)` exactly, for *any* improper spatial reflection. A Q-orbit defect therefore
carries a ℤ₂ relative-orientation label that its own mirror image reverses — quark-sector
defects come in parity-mirror pairs, statically degenerate, while charged-lepton defects
provably carry no such label; and the mirror pair is not the antiparticle pair (the label is
rotation-invariant and flips only under reflection). At the algebraic-snapshot level the mirror
pair collapses to one ray — the species-distinctness is anchored by the spatial topological
degree (§C.1), which parity reverses and the snapshot drops; correspondingly, no
sign-gauge-respecting snapshot pairing can couple the `⟨I₄⟩` condensate to the split — the µΨ₀
coupling must engage the winding topology, with §D.4.4's `ρ_L` boundary term (R-110) the
standing candidate seat (R-129). Computed on the Q-orbit baryon profiles, that boundary integral
vanishes identically for the literal scalar `⟨Ω³⟩₀` (the Q-orbit winding is parity-odd /
`I₄`-valued), but the R-128 Hodge dual `I₄·Ω` recovers the scalar L-winding exactly, fixing the
seat's *form* `L_θ = µΨ₀·B_Q`; its value remains open (R-152). The operator implementing the
quark lock is `I₄` — precisely the object whose parity-odd vacuum condensate `⟨I₄⟩` is §C.3.13's
one-dial µΨ₀ — so the up/down *splitting* dial enters the quark sector's mass-phase geometry
through its lock and is absent from the lepton lock (the coupling itself is not constructed;
the split stays dynamical — no static sub-split). Conditions: the Q-orbit ansatz carries
R-020's "structural analog" status (an explicit Q-orbit defect construction would harden it);
the same-observer premise is named.

**The L/Q differentiation, in one place (R-141).** The two lock results above are
one face of a single sector assignment that the framework uses load-bearingly, so it is
worth stating in one place. **What differentiates a lepton-sector from a quark-sector defect
is the orbit its winding and its mass-phase lock live in**, seen in three faces:
(i) the **winding face** (R-002, §A.5.2): `π₃(Spin(4)) = ℤ × ℤ` in the orbit basis — leptons
wind the *diagonal `Spin(3)` subgroup* factor, baryons the *coset `S³_𝓠`* factor: two
independent integer charges, which is why lepton number and baryon number are separately
conserved windings (§C.1.3); (ii) the **lock face** (R-127/R-128, above): the lepton
mass-phase lock is the *identity on the winding blade* — parity-**even** — while the quark
lock is the *Hodge dual* `I₄B_q` — parity-**odd**, carrying the ℤ₂ mirror label and the
`⟨I₄⟩`/µΨ₀ dial that the lepton sector provably lacks; (iii) the **coupling face** (R-141,
§C.4.6): this same assignment is what excludes the lepton mode from the induced-level count
on the baryon worldline — only the three colour modes couple to the Q-orbit chiral field, so
the induced level is *odd* and the Skyrmion's fermionic character is conditionally induced.
Faces (i) and (ii) are two projections of the one L/Q assignment (they would co-fail
together); face (iii) is where the differentiation became load-bearing for spin-statistics.
A guard worth restating: this L/Q (e₄-content) decomposition is **not** the chiral
SD/ASD split — `𝓛 ⊕ 𝓠 ≠ SU(2)₊ × SU(2)₋` (the A.5.2 fibration is the honest bridge between
the two bases), and R-140's chirally-blind plaquette result lives in the *chiral* basis, not
this one.

### B.3.2 Postulate 2 — observables, spectrum, measurement

Linearity from the linearization: on the linearized theory, observables are linear operators by
construction.

**Self-adjointness, derived.** Measurement outcomes are real. The scalar built from two
multivectors and an operator `M̂` has the form `⟨φ̃ M̂ ψ⟩_0`. Requiring reality forces `M̂ = M̃̂`
— the operator equals its Clifford reversion (R-022). This is the Cl-native expression of
self-adjointness, equivalent to `M̂ = M̂†` in the matrix realization.

**Spectral structure, derived.** The four grade-3 blades `T_a` form an exact orthonormal set
`⟨T_a T̃_b⟩_0 = δ_{ab}`, each blade an eigenvector of the corresponding observable.

**Measurement, configuration-realist.** TWT is configuration-realist: at every moment the system
has a definite configuration. "Measurement" is the §D.5 Role-3 selection process — not a stochastic
collapse and not a purely local geometric transition. TWT satisfies *signal locality* and
*configuration realism*; it violates Bell *factorizability*, because the selection law takes the
joint configuration as its argument with consistency secured by the `τ_5` ordering. Nothing travels
and no signal can be sent. We will see this clearly at §B.4.

### B.3.3 Postulate 3 — the Born rule

The natural Spin(4)-invariant bilinear is the squared full overlap on the derived `{1, B}`
subalgebra (§B.3.1). Defining the complex overlap

> `z(ψ, D_n) = ∫ ⟨D̃_n ψ⟩_{{1, B}} d³r`

— that is, projecting onto both the scalar grade 0 and the `B` component, which together carry the
complex amplitude information — the probability is

> `P(D_n) = z · z̃ = |⟨D_n | ψ⟩|²`. (R-023)

The grade-0-only formula `|∫ ⟨D̃_n ψ⟩_0 d³r|²` undercounts: for `D = 1` and `ψ = e_{12}` (the
same physical state, phase-rotated by 90°), `⟨e_{12}⟩_0 = 0`, so a grade-0-only formula predicts
zero probability for an identical-up-to-phase state. The correct formula projects onto `{1, B}`
and squares the full complex magnitude.

**Squaring is forced** (up to parity of the exponent) by chirality-reversal symmetry. A linear
(odd-power) coupling would break `Ψ → −Ψ` symmetry, producing directional drift with no source —
a contradiction. The drag overlap must therefore be even in `ψ`.

**The exponent is then exactly 2, as a theorem given four named premises (R-160).** The
restriction no longer rests on lowest-order plausibility. Four structural properties of the
Role-3 selection functional suffice: **(F1)** it assigns each detector channel a normalized
weight, one outcome per run; **(F2)** that weight depends on the channel alone, not on the
surrounding orthogonal decomposition it is read in (statistical noncontextuality); **(F3)** it
is defined on every orthogonal decomposition of the sector — coarse-grainings and joint
system–detector sectors included; **(F4)** it is blind to the global phase, a function of the
ray (R-021). F2 and F3 together give additivity over orthogonal channels by a coarse-graining
argument — the same channel read in two decompositions carries the same weight, and subtracting
the shared remainder leaves `μ(P ⊕ Q) = μ(P) + μ(Q)`; this reduction is the standard move of
the quantum-foundations literature, not novel here. That is exactly Gleason's hypothesis set on
the projection lattice, so on sectors of dimension ≥ 3 the weight is `Tr(ρ P)` for some density
operator `ρ`, and F4 pins `ρ = |ψ⟩⟨ψ|`: the Born rule with exponent exactly 2, with no
power-law family assumed anywhere. Two-dimensional sectors, where Gleason genuinely fails,
inherit the result through the joint system–detector sector that the selection law already
takes as its argument (§B.4.3), which has dimension ≥ 4.

*Honest scope.* Gleason's theorem is imported pure mathematics with checkable hypotheses; the
framework supplies those hypotheses rather than re-proving the theorem. Three of the four are
already carried by its own commitments — F1 is the single-outcome definiteness §D.5's Role 3 is
built to deliver, F3 states that the functional is total on the joint lattice (including
entangled contexts no laboratory will ask about), F4 is R-021. **F2 is the one genuinely new
substantive premise**, and it does *not* follow from the frame-equivalence of §B.3.1:
covariance of the functional under substrate rotations is strictly weaker than independence of
context, and an explicit covariant-but-contextual counterexample exists. F2 would be derivable
from a Role-3 construction carrying the channel-pairwise drag structure sketched above; until
that is built, the Born exponent is a theorem conditional on it.

The substrate-level
mechanism realizing single-outcome selection is the memory dissipation of §D.5, Role 3. The
detector couples at a rate set by `|c_n|²` — the squared *configuration-space* amplitude (not the
squared *local* field amplitude). When entanglement is present, the relevant overlap is global
(`∫ d³r`), and the selection law is on the joint configuration.

### B.3.4 Postulate 4 — Schrödinger from the Klein–Gordon parent

The wave equation in observer coordinates is the KG equation `(□_{1,3} + m²) φ = 0`, derived in
§B.2.1 by Fourier reduction. Writing the slowly varying envelope

> `φ(x, τ) = ψ(x, τ) · exp(−i m c² τ / ℏ)`

(with `i = e_{12}` per §A.5.6, `c = c_meta`), substituting into KG, and dropping `∂_τ² ψ` under
`|∂_τ² ψ| ≪ |(m c²/ℏ) ∂_τ ψ|`:

> `i ℏ ∂_τ ψ = −(ℏ²/(2m)) ∇² ψ + V ψ`. (R-024)

**The Schrödinger equation, with the rest energy `m c²` exactly canceled by the envelope phase.**
The cancellation is total: the KG parent has both `∂_τ²` (with negative sign relative to `∇²`,
the Lorentzian signature) and the `+m²` mass term, and the envelope phase rotates both into
commensurate quantities that cancel completely. The leading-order kinetic term sign is correct.
The first relativistic correction is the standard `−p⁴/(8 m³ c²)`, with the correct sign;
fine-structure of hydrogen comes out at order `α⁴`.

The potential `V` is the defect-background term of the linearization — the wavefunction `ψ` is the
small fluctuation around the defect; `V` is the defect's static profile entering the linearization.

(A historical note. Earlier framings derived Schrödinger by substituting an envelope into
`□_4 Φ = 0`, the 4D *Euclidean* Laplacian, which is the wrong parent: the elliptic Cauchy problem
is Hadamard-ill-posed in `x_4`, the dispersion gives complex energy `ℰ = mc² ± icp`, and the first
relativistic correction comes out with the wrong sign. The current derivation uses the hyperbolic
parent, which is what the observer actually sees.)

### B.3.5 Postulate 5 — symmetrization from Spin(4)

In `Cl(4,0)`, `Spin(4)` is the double cover of `SO(4)`.

*Even-grade objects* (scalars + bivectors) include the spinors of the minimal ideal `𝒮`
(even-grade by construction). A spinor transforms by the **one-sided** rotor action `ψ → R ψ`.
Under `R(2π) = exp(π e_{12}) = −1`, the spinor picks up the half-angle sign: `ψ → −ψ`. Spinors
return to themselves only after `R(4π)`.

*Odd-grade objects* (vectors + trivectors) transform by the **two-sided adjoint** sandwich
`v → R v R̃`. Under `R(2π) = −1`: `(−1) v (−1)~ = v`. Vectors and trivectors are integer-spin and
return to themselves after `R(2π)`.

Two identical spinor defects under exchange, viewed as a `2π` relative rotation of one against
the other in configuration space (the Finkelstein–Rubinstein 1968 construction), pick up the
half-angle sign. The combined state transforms as

> `|Ψ_{AB}⟩ → R(2π) |Ψ_{AB}⟩ = −|Ψ_{AB}⟩`,

antisymmetric under exchange. If both occupy the same state: `|Ψ_{AA}⟩ = −|Ψ_{AA}⟩ ⇒ 0`. **Pauli
exclusion is the half-angle's signature on the joint spinor configuration** (R-025).

A note on honest scope. The `Spin(4)` half-angle argument *consistently selects* fermionic
statistics for spinor configurations, but in pure SU(2) Skyrme it does not *force* the fermionic
option over the bosonic one. `π_4(SU(2)) = ℤ_2` allows either quantization, and absent a WZW term
both are topologically consistent. The Finkelstein–Rubinstein (1968) construction shows that *if*
one quantizes the Skyrmion as a fermion, the half-angle sign is exactly what one gets. So the
algebraic / topological structure of `Spin(4)` is compatible with and structurally supports
fermionic Skyrmion statistics, and the half-angle calculation produces the correct fermionic phase
under exchange — but the selection of the fermionic option in the bare-SU(2) Skyrme model is,
technically, an empirical choice rather than an algebraic identity. In SU(3) Skyrme, the WZW term
forces fermionic quantization for odd `N_c`; the substrate gauge structure of §C.4 supplies the
analogous mechanism in the present framework. This is Paper-2 work.

Three substrate routes to promote fermionic Skyrmion quantization from selection to derivation
have been tested, and all three fail by exact `Cl(4,0)` checks: (L1) the Hodge-duality push
gives `A → −A` as a collective-coordinate redundancy; (L2) the s=3 Adler-zero protection doesn't
discriminate; (L3) the three-facet WZW-analog gives per-facet sign `+1`, not `(−1)³`. A fourth
route — sourcing the sign from a finite `ℤ_3` colour holonomy — is closed negative by group
theory: `ℤ_3` has no order-2 element, and the `ℤ_6`/`S_3` completions leave the rotation-loop
sign independent of, or trivial on, the colour part. What survives of it is only the U(1)-valued
level-`N_c` action-term form, merged into the §C.4.6 gauge-sector gate (an odd induced level
would force fermionic quantization; zero/even would make the Finkelstein–Rubinstein selection
permanent). The selection status here is thus protected by *four exact negative substrate
routes*, not by absence of evidence. The selection also carries a **second, independent
empirical anchor** (R-136, §C.1.2): under the bosonic branch the quantized `B = 2` sector's
selection rule flips to `I + J` even — predicting a bound scalar `(0,0)` dibaryon ground state
and no distinguished `(0,1)` — refuted by the observed deuteron (`1⁺, I = 0`, no scalar
partner). Independent data, sharing the collective-quantization premise; evidence for the pick,
not a derivation of it.
**Conditional upgrade (R-141, §C.4.6).** The selection is conditionally *induced*: the
parity of the induced topological term on the `B = 1` worldline is ODD — from the derived mode
roster (3 colour modes per generation coupled to the Q-orbit field; the lepton excluded by the
L/Q sector assignment, with the single-Weyl neutrino as an independent third face) and the
imported induced-term theorem (D'Hoker–Farhi 1984; Witten 1983 — an external import, companion
Section 13) under one fresh named working premise (P1b: the mass-phase lock channel *is* the
chiral-coupling channel). Under those named premises the Skyrmion is a fermion by anomaly
matching — the fermionic pick becomes induced given (P1)+(P1b), parity-robust across the named
generation fork (N = 3 or 9, both odd).

**P1b splits, and its structural half is exact algebra (R-161).** The premise carried two
distinct burdens: that the lock channel has the *form* the induced-term theorem couples to, and
that the substrate's mode determinant actually *generates* the term. The first now falls to
`Cl(4,0)` identities. Relative to a defect's own winding assignment, the quark-sector
mass-phase lock (R-128) sits in the axial, chirality-linking channel — the mass-form channel
the theorem consumes — while the lepton lock (R-127) sits in the vector channel; equivalently
and more intrinsically, the quark observer line responds to motion of the local chiral field as
a pure phase at exactly `ω`, whereas the lepton line is *blind* to coset phase under every
coset axis. The dichotomy is **relative to the winding assignment**, not intrinsic to the
generators (the lepton generator has axial form about its own dual axis), so it rides the
banked L/Q assignment of R-002 — with that named, the exclusion of the lepton mode from the
induced count is exact rather than assumed, and R-128's parity dichotomy extends from the three
lattice axes to generic coset directions. What remains as **P1b-DYN**, still a candidate, is
strictly the dynamical half: that the colour modes appear in the determinant with the lock as
their mass. The structural premise set is thereby shorter, the lepton exclusion is hardened at
the four-doublet count, and all dynamical load stays behind the #1 gap. The four exact negatives still protect all
substrate-*internal* routes (the upgrade walks through the one door the holonomy negative left
open — the U(1)-valued action-term form — at mode-determinant level, not blade level); refusing
P1b reverts to the selection, with both empirical anchors standing.

### B.3.6 Tunneling as substrate evanescent tail

A standard QM result — quantum-mechanical tunneling — emerges from TWT's wave-train ontology
with one substrate twist worth naming. **Tunneling isn't amplitude leaking through a wall; it's
the medium's leading edge already sampling the far side.** A massive defect's wave-train carries
a slowly-dissipating inter-wavefront imprint — the evanescent tail at a barrier — that
pre-conditions the barrier region before the defect's bulk arrives. Solving the linearized wave
equation in the classically-forbidden region `V > E` returns the standard exponential decay
constant

> `κ = √(2m(V − E)) / ℏ`.

The recovery is **exact** in the non-relativistic (Schrödinger) limit — the forbidden-region
equation `ψ'' = (2m(V−E)/ℏ²)ψ` **is** the tail's defining equation, not an approximation. The
leading deviation is a **relativistic** correction from the KG parent (§B.3.7): with the total
energy `E = mc² + W`, the forbidden-region KG decay gives
`κ_rel/κ_NR = √(1 − (V−E)/2mc²) ≈ 1 − (V−E)/4mc²`, controlled by the barrier-to-rest-mass ratio
`(V−E)/mc²` — **not** the tunneling depth `V_0/E` (an earlier "5% in the deep-tunneling regime"
figure was mis-parametrized: a 5% deviation needs `(V−E) ≈ 0.2 mc²`, a semi-relativistic
barrier, independent of `V_0/E` — superseded by this derived correction). The standard result is
recovered, with the substrate reinterpretation riding on top.

**TWT-specific candidate prediction.** A small deviation from standard QM should appear when the
wave-train extent and the barrier scale are comparable — the leading-edge pre-conditioning would
be modified by interference with the barrier's own length scale. The deviation is not yet
quantified; the prediction is a candidate, not a derived result. The same evanescent-tail
mechanism supplies the substrate channel for β-decay's L-pair creation (§C.5.7).

### B.3.7 The Dirac equation from the hyperbolic parent

Dropping the slow-envelope approximation and applying the KG parent directly to a spinor field
`ψ`, `(□_{1,3} + m²) ψ = 0` admits an exact GA factorization once the right-acting complex
structure is introduced explicitly.

Define the right-multiplication operator `Ĵ ψ := ψ B` (with `B = e_{12}` per §A.5.6). Since left
and right multiplications on a Clifford algebra commute, `[𝒟, Ĵ] = 0`, and `Ĵ² ψ = ψ B² = −ψ`,
so `Ĵ² = −1`. With `𝒟 = γ⁰ c⁻¹ ∂_τ + γʲ ∂_j` the Lorentzian Dirac operator (`𝒟² = □_{1,3}`),
the factorization is exact:

> `(𝒟 + m Ĵ)(𝒟 − m Ĵ) = 𝒟² − m² Ĵ² = 𝒟² + m² = □_{1,3} + m²`.

So `(□_{1,3} + m²) ψ = 0` factors as `(𝒟 + m Ĵ)(𝒟 − m Ĵ) ψ = 0`, and either first-order branch

> `𝒟 ψ = ±m · ψ · B` (R-026)

squares to `□_{1,3} ψ = −m² ψ`. Both branches square to the same KG; the sign distinguishes the
particle and antiparticle branches, which is the standard Dirac feature, not an ambiguity in the
derivation. And the complex unit is visibly a right-acting
bivector (`B` on the right), not an inserted scalar.

The standard Hestenes spacetime-algebra Dirac equation `∇ψ · I σ³ = m ψ γ⁰` (with `I = γ⁰γ¹γ²γ³`
and `σ³ = γ³ γ⁰`) reduces, in the wavefront frame, to `I σ³ = e_{12}`. The Hestenes equation reads
`𝒟 ψ e_{12} = m ψ γ⁰`, and squares to KG by direct calculation. The branch equation
`𝒟 ψ = −m ψ e_{12}` and the Hestenes equation coincide on the minimal left ideal selected by the
right-acting idempotent `P_+ := (1 + γ⁰)/2` (`P_+² = P_+`), where `ψ γ⁰ = ψ` (the defining
property of the ideal). On this ideal the `(−)` branch and the Hestenes form are equivalent, and
the standard 4-component Dirac equation `i γ^μ ∂_μ ψ = m ψ` falls out.

That is QM. Five postulates from one geometric move. The next chapter shows how the same one-sided
rotor sandwich produces the Tsirelson bound.

---

## §B.4 — Bell, Tsirelson, non-separability

This is the framework's most direct demonstration that QM is a substrate-level geometric fact, not
an axiomatic system. The calculation of CHSH reaches `S = 2√2` exactly. The multipartite
Mermin–Klyshko hierarchy comes out by structural induction. And the identity `ρ_A = (1/2) 𝟙`
behind no-signaling turns out to be the *same fact* as Bell-violation — locally each side is pure
noise, jointly they are perfectly ordered.

**Mathematical setting.** The spinor `ψ = a + b B` with `B² = −1` (any transverse simple
bivector; we use `B = e_{12}` by convention) is isomorphic to `ℂ`. Physical-space rotation by `θ`
acts on the spinor by the **one-sided** rotor action `ψ → R ψ` with `R = exp(θ B/2)`, the
half-angle of the `Spin(3)` double cover. Two oriented states `ψ_a = R_a ψ_0`, `ψ_b = R_b ψ_0` have
geometric overlap

> `⟨ψ_a | ψ_b⟩ = ⟨ψ_0 | R̃_a R_b | ψ_0⟩ = ⟨exp((θ_b − θ_a) B/2)⟩_0 = cos((θ_b − θ_a)/2)`.

(The two-sided sandwich `R ψ R̃` does *not* produce the half-angle on an even-grade `ψ` in
`span{1, B}`, because `ψ` commutes with `R, R̃` and the sandwich is the identity. The half-angle
comes from the one-sided spinor action, exactly as in §B.3.5.)

### B.4.1 The TWT calculation of CHSH

The antisymmetric exchange forces the singlet

> `|Ψ_singlet⟩ = (1/√2) · (|↑⟩_A |↓⟩_B − |↓⟩_A |↑⟩_B)`.

Born rule:

> `P(↑_a, ↓_b) = (1/2) cos²((θ_b − θ_a)/2)`,
> `P(↑_a, ↑_b) = (1/2) sin²((θ_b − θ_a)/2)`.

The correlation function is then

> `E(a, b) = −cos θ_{ab}`,

and at optimal angles `S = 2√2` (R-027). **TWT reproduces the Tsirelson bound exactly.** The
`cos(θ/2)` of the one-sided rotor action's half-angle is the dimensional fingerprint of
`S³ → S²` projection.

### B.4.2 Multipartite Mermin–Klyshko

The same rotor construction extends to `n` parties with one additional factor per party. The
per-party measurement is a rotor in the transverse plane, so the joint `n`-party correlation is
the grade-0 part of the product of `n` coplanar rotors:

> `E_n(φ_1, ..., φ_n) = ⟨exp(φ_1 B) · exp(φ_2 B) ⋯ exp(φ_n B)⟩_0 = cos(φ_1 + φ_2 + ⋯ + φ_n)`.

At the Mermin–Klyshko optimal settings `θ_j = −(j − 1) π/(2n)`, `θ'_j = θ_j + π/2`, the MK
polynomial evaluates to

> `|M_n| = 2^{(n + 1)/2}` (R-028),

the Tsirelson-type bound for `n` parties. At `n = 2`,
`|M_2| = 2√2` recovers Tsirelson; at `n = 3`, `|M_3| = 4` recovers the GHZ value.

This is *independent* evidence that TWT reproduces QM at every multipartite `n`, not just CHSH.
A scope note: the rotor economy is specific to the GHZ / symmetric class. The W (non-GHZ) class
runs on pairwise phase *differences*, not phase sums, and requires the full multiparticle
`Cl⁺(4,0) ≅ ℍ ⊕ ℍ` correlator across two non-commuting rotation planes. The faithful TWT object
for W reproduces QM through that full machinery; developing it in a Cl-native form is an open
construction item, not a falsifier.

### B.4.3 Bell's three premises, and which TWT violates

Bell's theorem encodes three independent premises:

- **Signal locality (causal locality).** No signal propagates faster than the medium's wave speed;
  settings on one side cannot reach the other side's measurement event within the spacetime
  interval.
- **Configuration realism.** The system has a definite configuration `λ` at every moment,
  determining outcomes as functions of own-setting and `λ`.
- **Factorizability (parameter independence).** The outcome at each wing is a function of its
  *own* setting and `λ` only — Alice's outcome `A(a, λ)` does not depend on Bob's setting `b`, and
  vice versa.

**TWT satisfies signal locality and configuration realism; it violates factorizability**, because
the §D.5 selection law takes the joint configuration as its argument with consistency secured by
the `τ_5` ordering. **Nothing travels and no signal can be sent.**

The selection law's argument list is the joint multivector `Ψ_joint`, not the local field at
Alice's wing in isolation; given the `τ_5`-ordered front structure, the law has an objective global
clock by which to order the wings' selections. *Which* of the two sub-conditions fails depends
on how finely `λ` is resolved, and the framework should be read at both levels. At
`λ = Ψ_joint` — the joint configuration itself — the single-wing weight is independent of
Bob's setting: this is the noncontextual structure §B.3.3's F2 states, and it is what returns
`ρ_A = (1/2)𝟙` at §B.4.4. There **parameter independence holds and it is *outcome*
independence that fails** — the same leg orthodox quantum mechanics and Bohmian mechanics
break. At a finer `λ` resolving the Role-3 selection's own sub-configuration detail, the
conditional acquires a setting dependence, `P(A | a, b, λ) ≠ P(A | a, λ)` — parameter
independence in the strict hidden-variable sense. Either way the marginal
`P(A | a, b) = ∫ P(A | a, b, λ) ρ(λ | a, b) dλ` remains `b`-independent: `P(A | a, b) = P(A | a)`,
no-signaling at the operational level. The marginal independence — that no statistical regularity
Alice can build from her own outcomes is changed by Bob's setting — is a *requirement imposed on*
the Role-3 Born structure (to be discharged when §D.5's Role 3 is built), not an extra
assumption beyond it. The Toner–Bacon (2003) one-bit-per-run
result quantifies the precise way in which configuration-space dependence is compatible with
marginal independence.

### B.4.4 The single fact behind both no-signaling and Bell-violation

The reduced local state at Alice is maximally mixed:

> `ρ_A = Tr_B |Ψ⟩⟨Ψ| = (1/2) 𝟙` (eigenvalues `1/2`, `1/2`), (R-029)

independent of Bob's setting `b`. In Cl-native terms, `ρ_A` is the `Cl_A`-restriction of the
bipartite multivector `Ψ Ψ̃` obtained by partial grade-projection over the `Cl_B` factor; the
result is the unit scalar `𝟙 ∈ Cl_A` with the `1/2` normalization fixing the trace to 1.

**This one identity does two jobs at once:**

- *Why no signal can be sent.* Alice's marginal is the identity, independent of Bob's setting.
  Nothing Bob does shifts `ρ_A`.
- *What non-separability means.* All structure has drained out of the local marginals and into the
  correlations. Locally each side is pure noise; jointly they are perfectly ordered.

**No-signaling and non-separability are the same fact.** A common mistake to avoid: "the
correlation is fixed at pair production and read out independently by each party" describes a
*local hidden-variable model* (outcomes as separate functions `A(a, λ)`, `B(b, λ)` of a shared
variable `λ`), bounded by Bell at `S ≤ 2`. The grade or dimension of `λ` does not help; Bell allows
`λ` to be a multivector, a whole field. **What matters is whether the outcomes factorize, and in
TWT they do not** — the rotor/Clifford correlation `E(a, b) = −cos θ_{ab}` is an inner product of
*both* settings, irreducibly joint.

### B.4.5 The Bell-memory bridge

A non-separable joint configuration (an entangled pair) is a single **shared** accumulate-to-fire
build-up — one memory mechanism (§D.5), not two independent ones; the reduced state
`ρ_A = (1/2)𝟙` is the static face of exactly that — "one shared build-up" — and it is the same fact
as no-signaling. **Decoherence is the splitting** of that one shared build-up into two independent
ones.

The decoherence rate is therefore governed by the same transport function `Im χ` that sets cell
formation, memory, criticality, and the `Λ ~ H²` residual — a single EFT dial spanning the static
(Bell) and dynamical (memory) faces of non-separability (R-030). One dial, two operational
windows: the macromolecule-interferometry decoherence floor and the Bell-pair memory time are
*two readouts of the same kernel*.

A testable corollary follows. The `τ_5`-ordering is the *same* preferred frame that governs
cosmological observations — the comoving frame. The testable claim (R-031): **the foliation along
which Bell-correlation selections are time-ordered coincides with the cosmological comoving
frame.** A measurable discrepancy between Bell-selection-ordering and the comoving frame would
falsify the identification. The Geneva-class influence-speed experiments (Salart 2008, Yin 2013,
lower bounds `> 10⁴ c` in candidate preferred frames) are, for TWT, direct probes; the sharp
prediction is that no finite influence speed will ever be found, with the Bell-selection foliation
coinciding with the cosmological comoving frame — operationally, signaling does not exist.

### B.4.6 Honest scope

What TWT contributes is *not* locality — Bell is a theorem; any theory isomorphic to QM inherits
the non-locality. TWT adds two things:

- **Geometrization of the structure.** Standard QM postulates the complex numbers, the half-angle,
  and the Born squaring; TWT grounds all three in one move — projecting a 4D-oriented object
  onto a 3D frame forces the bivector representation, the one-sided rotor action, `cos(θ/2)`,
  and hence `2√2` (the Born squaring at §B.3.3's stated plausibility level). Four postulates
  become one piece of geometry.
- **Dissolution of the instantaneity.** In the 4D Euclidean block both measurement events
  co-exist; there is **no Lorentz-invariant observer-side time-ordering** between spacelike-separated
  measurement events that would make one measurement "first" and force a collapse to propagate to
  the other. The substrate *does* carry a preferred `τ_5`-ordering, used by the §B.4.3 / §B.4.4
  selection law for substrate-level consistency; what the substrate has and the wavefront-locked
  observer does not is a Lorentz-invariant clock for spacelike pairs. The correlation is a
  *timeless property of the static joint configuration* from the observer's view; from the
  substrate's view it is `τ_5`-consistent by construction. The appearance of "spooky action at a
  distance" is an artifact of imposing the observer's dynamical measurement time-order on a joint
  configuration that is `τ_5`-ordered at the substrate level but admits no observer-Lorentz-invariant
  ordering. Nothing travels; the joint configuration *is* correlated.

Quantum non-classicality is the imprint of non-separability on observable correlations. TWT,
having an explicit non-separable joint structure plus a `τ_5`-ordered front, can state *where*
Bell non-locality physically lives — in the joint configuration that is the selection law's
argument — where other frameworks must leave it as an axiom.

---

## §B.5 — Electromagnetism

Electromagnetism in this framework is the medium's elastic response to defect bivector winding. A
defect's internal bivector content produces a bivector-valued strain pattern `F` in the surrounding
bulk, decaying with distance. Under wavefront projection, the observer reads `F`'s `𝓠`-component
as a vector field (electric field `E`) and its `𝓛`-component as a bivector field (magnetic field
`B`, dualized to pseudovector via the observer's spatial pseudoscalar).

**Mathematical setting.** `F` is a multivector field on the 4D bulk taking values in the grade-2
sector. The vector derivative is `∇ = ∂_τ + ∇_3`, a grade-1 (vector) differential operator. The
current `J` is a grade-1 (vector) field carrying defect charge and 3-current density. `∇F`
decomposes by grade into grade-1 plus grade-3 multivectors only.

### B.5.1 The consolidated Maxwell equation

In the small-deformation regime, the strain field obeys, on the wavefront:

> `∇ F = J` (R-032)

— the geometric-algebra form of the consolidated Maxwell equations. The source `J` is the
wavefront projection of a substrate-level **bivector winding** — the L-orbit topological winding
number of the defect, integer-valued, with algebraic carrier in grade 2. Integrated over a
3-surface on the wavefront, this bivector winding gives the integer enclosed charge.

The grade decomposition gives the four standard laws:

| Grade of `∇F` | Spatial-slice equation | Standard name |
|---|---|---|
| Grade-1 (scalar of 4-vector) | `∇ · E = ρ` | Gauss's law |
| Grade-1 (3-vector of 4-vector) | `∇ × B − ∂_τ E/c = j` | Ampère–Maxwell |
| Grade-3 (3-vector of 4-trivector) | `∇ × E + ∂_τ B/c = 0` | Faraday |
| Grade-3 (pseudoscalar of 4-trivector) | `∇ · B = 0` | No monopoles |

(*Units. The two time-derivative rows carry an explicit `c` for textbook continuity; the two
time-independent rows do not need it. Both are the same convention — the local restoration of `c`
per the Opening's units note, not a switch of system.*)

### B.5.2 No magnetic monopoles, by geometry

The last entry deserves a moment. **Magnetic monopoles are geometrically forbidden** in TWT
(R-033): the grade-3 part of `∇F` vanishes because `J` — the projection of bivector winding to the
wavefront — is grade-1 only. There is no grade-3 source available, by algebra. Not "we have never
observed one"; *there is no place for one in the grade structure*. The closest analogous fact in
standard physics is `∇ · B = 0` as a consequence of `B` being a bivector with vector source `J`;
here the absence is one notch deeper, sitting on the substrate-level statement that the EM current
is the wavefront projection of L-orbit winding (grade 2 → grade 1).

### B.5.3 The Coulomb potential

A static defect satisfies `∇_3² F_static = −J_static`. The Green's function in 3D is
`1/(4π r)`; for a point defect with bivector content `Σ`,

> `F_static(r) = Σ / (4π r)`. (R-034)

Interaction energy: `V(R) = Σ_1 · Σ_2 / (4π R)`. Same-chirality bivector content gives
`Σ_1 · Σ_2 > 0` — repulsion. Opposite-chirality gives `Σ_1 · Σ_2 < 0` — attraction. **Coulomb's
law and like-repels-unlike-attracts follow from elastic overlap.**

The `1/r` law is intrinsically 3D: it comes from the wavefront being three-dimensional, and is the
geometric reason gravity (§B.6) also goes as `1/r` in the Newtonian limit.

### B.5.4 The photon as the L↔Q-bridging strain mode

In source-free regions `∇ F = 0`, the homogeneous wave equation. Solutions: propagating bivector
strain patterns at `c_meta` — **photons**. Two transverse polarizations are the two bivector planes
orthogonal to propagation. The photon is massless because a pure bulk wave-mode carries no
rotational lag — mass is meta-time momentum (§A.4), and a source-free transverse mode has none.

The strain `F` carries a magnetic part in `𝓛` (spatial bivectors `e_{jk}`) and an electric part in
`𝓠` (the `e_{i4}`), so a propagating `F`-mode spans both orbits: the photon is the
**L↔Q-bridging strain** (R-035). This is the bridge whose coupling strength is `α_em` — its
ontology derived at §B.5b, its value open (§D.5).

The source of this strain is the L-orbit winding (per B.5.1), so the topological winding charge
*is* the electric charge — this is what licenses reading the §C.2 charge spectrum `Q` as
electromagnetism. The masslessness is then **EWSB-independent**: the winding charge is conserved
*by topology* (integer winding; §C.5), so its long-range gauge field — the photon — stays massless
no matter what any condensate does. The §C.5 weak bosons couple to charges the electroweak
condensate *can* break and are gapped at that breaking; "photon massless, W/Z massive" reflects
"topological charge ⇒ massless, breakable charge ⇒ gapped," not a hand-insertion.

### B.5.5 The worldline force law and the cyclotron readout of mass

How does a charged defect *move* in an external strain field? The answer closes the loop between
`mass = ω` (§A.4) and the workhorse of every precision mass measurement — the cyclotron frequency
`ω_c = qB/m` of a charge circling in a magnetic field.

In the point-defect (worldline) limit — the same idealization §B.6.1 uses for the gravitational
source — the defect is characterized by its integer L-orbit winding `q` alone, carried as the
grade-1 current `J = q u` along the worldline tangent `u` (the rank-1 sibling of the worldline
stress `T^{μν} = ρ u^μ u^ν`). Static internal structure beyond the winding (a magnetic-dipole
moment) is a form-factor correction, in the same class §B.6's protection argument relegates to
dim-6.

Two established facts then pin the full force law:

- **The rest-frame anchor.** From the elastic-overlap energy (§B.5.3), the static force on a
  monopole probe reads the external strain's `𝓠`-component — the observer's `E` — *only*. A pure
  `𝓛`-component (magnetostatic) strain exerts **no** static force, by exact grade-0 orthogonality
  `⟨Σ_Q Σ_L⟩₀ = 0`: the grade split that separates `E` from `B` (§B.5) is also what decouples a
  static charge from a static magnet.
- **Covariance.** The defect's worldline dynamics inherits the wavefront Lorentz structure — the
  §B.1 isomorphism plus the §B.6 one-substrate-one-light-cone protection (the latter a named
  premise of this result; its violations sit in the same dim-6 form-factor class). Spin(4) acts transitively on unit tangents, so the rest-frame anchor
  plus equivariance *determine* the force at every velocity — no linearity assumption needed:

> `ṗ = q F·u`, `p = m u`. (R-124)

An independent Schur-style cross-check pins the same answer: the space of Spin(4)-equivariant
bilinear maps `(F, u) → f` is exactly two-dimensional — `F·u` and its Hodge twin `(I₄F)·u` — and
the anchor kills the twin (it would exert a static force on a charge from a pure magnetostatic
strain). Cubic-in-`u` candidates collapse by exact contraction identities. `f·u = 0` holds
exactly, so `dm/dτ = 0` is a *consequence* of the derived law — the elastic coupling cannot pump
the meta-time rotor frequency at this order.

In a uniform `𝓛`-strain `F = B e₁₂` the equation of motion has an exact rotor solution: the
in-plane velocity rotates at precisely

> `ω_c = qB/m`,

with the `e₄`-component and speed preserved — the cyclotron orbit. The `m` in the denominator is
the worldline inertia coefficient; that it equals the defect's meta-time rotor frequency read on
the front, `k₄ = ω/c_meta`, is R-123's identification, conditional on its residue (ii) (§B.2.1).
The cyclotron chain therefore closes *modulo residue (ii) alone* — the same conditional status as
the dispersion chain — and a Penning-trap mass measurement is, in this framework's terms, a direct
readout of a defect's rotor frequency. What is *not* supplied here: the coupling magnitude
(`α_em`, §B.5b — the #1 gap), magnetic-moment/gradient forces (form-factor class), nonlinear-in-`F`
corrections beyond the small-deformation elastic regime, the g-factor, and radiation reaction
(dissipative, #1-gap class).

---

## §B.5b — The fine-structure constant and its sibling g

A two-layer hook. The first layer is the ontology: in TWT, the fine-structure constant `α_em` is
not a free parameter standing for "how strong electromagnetism happens to be." It is the
**strength of the L↔Q rotation↔wave reconversion** between matter's spatial-winding face (the
L-orbit) and the photon's bridging strain mode (the Q-orbit). The second layer is the parameter
economy: combined with §C.4's `sin²θ_W = 3/8` (proved unconditionally), the weak coupling `g`
turns out to be α's algebraic *sibling*, not an independent gate. The framework's electroweak
sector therefore reduces to one #1-gap-gated magnitude, not two.

**Mathematical setting.** The reactive grade-0 invariant is

> `α-object = ⟨Σ̃_F · Γ_recon · Σ_L⟩_0`,

with `Σ_L` an L-orbit bivector winding (matter's spatial face, §A.3 / §C.1), `Σ_F` the photon
strain mode (§B.5.4), and `Γ_recon` the wavefront-locking reconversion built from `φ` (§B.1).
The Type-B / Type-A distinction separates couplings analytic in the interaction (Type-B) from
tunneling-action `exp(−S)` effects (Type-A): α is Type-B — perturbative, no essential
singularity — while tunneling rates are Type-A. They sample the *same* underlying `Im χ` at
different frequencies.

### B.5b.1 What α is

The α-object identifies as a **reactive grade-0 Clifford invariant** — representation-independent,
picking out the common bivector content of the L-orbit field and the EM strain (R-035a). The
native inner product is quaternionic-Hermitian on the spinor ideal `𝒮 = Cl(4,0) · s_0` (§A.5.4);
the Dirac vertex rides alongside via §B.1.

The length ladder

> `r_e = α · λ̄_C`, `a_0 = λ̄_C / α`, `r_e · a_0 = λ̄_C²` (R-035c)

is a **coherence success**, not a value over-determination of α. `α` cancels in `r_e · a_0`; the
identity `λ̄_C²` is algebraic. What the length ladder shows is that *one geometric overlap*
underlies three independently measured lengths (classical electron radius, Compton wavelength,
Bohr radius) — the vertex role and both scale-setting roles.

The framework supplies the **ontology** (what α *is*) plus the **category** (reactive, Type-B,
not tunneling) plus the **coherence** (one object, several roles). It does **not** supply the
**value**: the magnitude of `α_em` lives in the same `Im χ` transport function as everything else
in the open frontier — the framework's #1 gap (§D.5).

### B.5b.2 g is α's algebraic sibling

The standard SM relation `g² = 4π α / sin²θ_W` becomes operational once `sin²θ_W` is known. In
§C.4 we will derive natively that

> `sin²θ_W = 3/8` at the unification scale, (R-082)

derived from the forced-core charges, grade-0 L⊥Q orthogonality, the Clifford trace-bridge
giving the native `√(3/5)`, and `g_1 = g_2` from the dim-4 D4 isotropy theorem. No SU(5)
embedding; no foreign Lie-algebra import. The descent to the measured `0.231` at `M_Z` is
standard one-loop RG, which the framework does not derive — but the *unification value* `3/8`
is exact, native, and GUT-free, carrying only the framework's own counted inputs (weak = SD;
the 15-state spectrum) and the D4-isotropy `g_1 = g_2`.

Granted that, the weak coupling becomes

> `g² = 4π α · (8/3)`,

making `g` algebraically siblinged to `α`. **The EW sector therefore reduces to one #1-gap-gated
magnitude (α), not two** (R-035b). Same `Im χ` functional samples both — different frequencies of
one transport function.

### B.5b.3 The single-dial economy

The same logic ties `α_W` (weak) in exactly; extending the identification to `α_s` (strong) is
a structural conjecture — the strong sector is gluon-free and its dynamics gated (§C.5.2).
Where the SM treats α, g, g', g_s as four independently fitted couplings, **TWT derives the
electroweak trio as samples of one transport function `Im χ` and conjectures the strong
coupling as a fourth** — the framework's #1 gap. Closing that gap would simultaneously pin
them. Until then, the derived *count* is the EW sector's (one magnitude, not three), the
four-coupling reading is a framing claim, and the *value* of α is open, recorded in the
pending-values registry (companion Section 4).

**The strong fold-in is a conjecture with a located obstruction (R-162).** It is not merely
unproven: it cannot be obtained the cheap way. The electromagnetic dial and the colour dial
read *provably different* channels of one substrate response — the `α`-object is an
`I_4`-odd invariant of the grade-2 sector (a spin-1 channel of multiplicity two, whose
cross-term `⟨B_L I_4 B_Q⟩₀` is exactly the L↔Q reconversion), while the colour force rides the
coset-5 (a spin-2 channel of multiplicity one, and the same coset-Cartan channel `Θ_rel`
occupies). The reconversion-type invariant *vanishes identically* on the colour sector, the two
blocks are dimensionally inequivalent (6 versus 5) so no intertwiner exists under any subgroup
chain, and there is no invariant cross-pairing under the substrate's symmetries. A shared
transport function across both therefore cannot be forced by symmetry the way `g` was forced by
algebra: the fold-in is exactly equivalent to one named property of the kernel — cross-block
rigidity, together with a cross-block weight that is itself open (the strong-sector analogue of
the `8/3` that made `g` a genuine sibling). Scope: this concerns the *magnitude* source at the
two-point level, never the running or asymptotic freedom, whose burden is unchanged (§C.5.2).

This is the parameter-economy hook stated cleanly. The SM has 19 free parameters; TWT pins one of
those magnitudes unconditionally (`sin²θ_W = 3/8`), names the four EW couplings as one open
magnitude, and tags the rest of the open frontier explicitly. On the *structural* axis — what each
parameter *is* — the framework's contribution is far larger than the magnitude count suggests. We
return to the honest comparison at §E.2.

---

## §B.6 — Gravity

In TWT, gravity is the induced general relativity of the rotor field as local Lorentz frame,
structurally unified with the gauge sector (§C.5) through the same frame-connection mechanism.
The case has three settled structural pillars: magnitude (Λ Planckian within `O(1)`), sign
(positive — `1/G > 0` — locked to spin-2 spectral positivity, equivalently substrate stability),
and form (`γ = 1` from matter-as-defect Lorentz protection). The texture-tetrad route to a full
nonlinear Einstein–Hilbert coefficient is structurally closed conditional on one premise; the
absolute coefficient remains the #1-gap output.

This is **not** a derivation from scratch of the Einstein equations. It is the recognition that
the framework's existing structure — rotor field + emergently Lorentz-invariant matter — is
precisely the standard input for *induced gravity* (Sakharov 1967), and that the framework's
particular ingredients make this route unusually clean. We claim the sign, the form, and the
magnitude bracket. We do not claim the theory.

**Mathematical setting.** The substrate's monad is a unit rotor at each D4 site; the continuum
field `U(x) ∈ SU(2)` provides the spatial Spin(3) part of a local Lorentz frame, and combined
with the canting orientation and `e_4` it supplies a 4D local Lorentz frame with local `Spin(4)`
symmetry (R-036). A frame field carries a connection; the spin connection `ω(R)` emerges from
the rotor exactly as the spin connection of GR emerges from the vielbein, with curvature
`𝓡(ω) = dω + ω ∧ ω`. The bare rotor action is of σ-model form `∫ (∂R)² ~ ∫ ω²` — connection
squared, not Einstein–Hilbert. Integrating out matter and substrate fluctuations in a curved frame
background generates the Einstein–Hilbert action radiatively (Sakharov mechanism). The graviton
`h_{μν}` decomposes into spin-2 (transverse-traceless, two polarizations, the physical graviton)
and spin-0 (the conformal mode / trace). EH assigns these opposite-sign kinetic terms; this is the
well-known conformal-factor problem, and it is what we now address.

### B.6.1 The Newtonian limit

A massive defect in TWT is never at rest along `e_4` — every defect has a worldline tangent with
`e_4`-component, with `Ṙ_a = e_4` the rest idealization. The gravitational source is therefore the
**worldline stress** `T^{μν} = ρ u^μ u^ν` (rank 2), not a scalar mass density. The traceless part
is nonzero even at rest, so the spin-2 channel is sourced from the start by the structure of
matter itself.

In the linearized static limit of induced Einstein–Hilbert, the metric perturbation around a point
mass is

> `g_{00} = −1 + 2GM/r`, `g_{ij} = (1 + 2GM/r) δ_{ij}`,

both components carrying the same `2GM/r` — the structural origin of `γ = 1`, deferred to §B.6.3
(R-039). The slow-motion limit gives Newton's law `V_{12} = −G M_1 M_2 / R`, attractive (R-038).

The `1/r` comes from the wavefront being three-dimensional (same reason as Coulomb's `1/r`,
§B.5.3). The attraction is automatic in induced EH: matter couples to the full stress-energy
tensor through the metric; the dominant Newtonian component is `T^{00} = ρ > 0`. Newton's constant
itself, `G ~ 1/(N_eff Λ²)`, is *derived* (within an `O(1)` factor) from the Sakharov mechanism,
not put in by hand — we develop that next.

### B.6.2 Induced Einstein–Hilbert: Sakharov, with a Planckian Λ bracket

The bare rotor action is σ-model-shaped, not EH-shaped: `∫ (∂R)² ~ ∫ ω²` is connection squared
(a kinetic term), not linear in curvature. **This is the generic starting point of induced
gravity.** Integrating out matter and substrate fluctuations in a curved frame background generates
EH radiatively (Sakharov 1967). Two routes give the magnitude consistently:

**Heat-kernel** (Schwinger–DeWitt) expansion at one loop places EH at the quadratically divergent
order:

> `1/(16π G) ~ (c_reg · N_eff / (16π²)) · Λ²`,

with `N_eff` a degree-of-freedom count and `c_reg` an `O(1)` regulator coefficient.

**Spectral** route via the matter stress-tensor two-point function `⟨T_{μν} T_{αβ}⟩`:

> `1/(16π G) ~ ∫ dμ² · ρ_2(μ²) / μ⁴ ~ C_T · Λ²`,

with `ρ_2(s) ∝ C_T · s²` the spin-2 spectral density. Both routes deliver `1/(16π G) ∝ Λ² × (dof
count)` at leading order. **Newton's constant is therefore derived** (R-037),
`G ~ 1/(N_eff · Λ²)`, rather than input. For `c_reg ~ 1` the dof count is bracketed:

| Reading | `N_eff` | `Λ` |
|---|---|---|
| Full emergent SM treated as independent (1 Higgs + 48 Weyl + 12 vectors) | `O(100)` | `0.16 M_Pl` |
| Rotor Spin(4) dof only (matter-as-defect, fundamental dof) | ≈ 6 | `0.72 M_Pl` |

The upper-row `N_eff` is the dof count when the matter spectrum is treated as fundamental and fed
through a standard heat-kernel sum. The exact number depends on conventions (Weyl-vs-Dirac
weights, transverse-vs-longitudinal vector counting, scheme of the heat-kernel coefficient
`c_reg`); under typical conventions it lands at `O(100)`. The full convention pinning lives at
§D.5 with the rest of the substrate-dynamics machinery; for the bracket here, **what matters is
that the upper-row `N_eff` is order-of-magnitude `10²` and the lower-row is order-of-magnitude
`10⁰`**.

The matter-as-defect ontology favors the upper bound (the fermions and gauge bosons are not
independent fundamental fields — they are textures and spin-waves of the one rotor field). So
`Λ ∈ [0.16, 0.72] M_Pl` for `c_reg ~ 1`. **The substrate cutoff lands at the Planck scale within
a factor of order unity** — at the right order of magnitude for an emergent-gravity cutoff, and
not put in.

*Import notice:* the one-loop/heat-kernel machinery this section runs on is an external theorem
applied at the **substrate level** — borrowed mechanism, not inside-frame data — and its
premises (a standard QFT vacuum for substrate modes) are not yet derived from the ontology. It
is registered as **I-3 in companion Section 13** with its retirement handle (the `C_T` spectral
sum); the scaling form enters as an imported QFT input, so this section's magnitude
bracket is excisable without touching the sign (§B.6.4) or `γ = 1` (§B.6.3) results, which do
not ride it (the §B.6.1 Newtonian-limit presentation rides the same machinery and falls back
with it).

*Import narrowed (R-163).* The same coefficient computed directly on the framework's **own**
derived linear face — the free 5D hyperbolic operator of §D.4.6 with its six grade-2 channels
sharing one stiffness — makes the mode content and the finiteness of the sum derived rather
than assumed: the proper-time integral over the derived D4 nearest-neighbour band converges on
its own, with no regularization choice entering the flat-band measure. Two named assumptions
replace the import's original triple: **(OA-LF-i)**, that the driven steady state's occupation
of those modes is the ground-state one, a statement about the *state*; and **(OA-LF-ii)**, that
the curvature couples covariantly at monad scale, a statement about the *operator*. The second
is where the old regulator freedom now lives — it carries the bulk of the integral's support —
so the `O(1)` uncertainty is *relocated and localized*, not removed, and the bracket keeps its
conditional status. Read in this section's own normalization the result sits at `c_reg ≈ 1.8`,
inside the `c_reg ~ 1` this section assumes, and the convention-independent statement is that
the monad spacing is Planckian within a factor of order unity — which is the bracket's actual
content. The value is an idealization of a gapless shared band; the canted vacuum's two
Goldstone modes and four gapped ones would soften it by some tens of percent.

### B.6.3 γ = 1 from matter-as-defect Lorentz protection

The same one-substrate, one-light-cone argument we used at §B.1.5 (R-016) acts directly on the
induced-gravity sector. Matter loops integrated to produce EH are *one-field loops* on the rotor
field, so the induced action inherits the substrate light-cone exactly. The metric perturbation
components `g_{00} = −1 + 2GM/r` and `g_{ij} = (1 + 2GM/r) δ_{ij}` carry the **same** `2GM/r`
because both come from the same Lorentz-invariant induced action evaluated on the same source.
This is `γ = 1` (R-039) — the Eddington PPN parameter takes the GR value structurally, not by
tuning.

**The Compton-screening mechanism for the scalar mode.** A generic concern with induced gravity
is that a light scalar mode (the trace / conformal channel) might leak through and shift `γ`. In
TWT the wave-train structure screens this: the front-phase-locked-to-wave-train coupling gaps any
would-be scalar partner at the Compton scale `λ̄_C = ℏ/(m c)` of the matter sourcing the gravity.
Three scalar candidates are protected: (i) the rotor-norm direction, frozen by `|R| = 1`
(non-propagating, §D.3.2); (ii) the phason, a distinct Goldstone with positive spectral density;
(iii) the conformal-mode artifact, removed by the diffeomorphism (Hamiltonian) constraint
(§B.6.4). None survives as a light propagating scalar — `γ = 1` is uncontaminated.

The complementary rotational-anisotropy bound is closed by the D4 cubic point group; the boost
bound is closed by matter-as-defect. The two together drive the residual to dimension six,
`(E/Λ)²`. The four-probe table at the bracket lower corner `Λ = 0.16 M_Pl`:

| Probe | `E` | `(E/Λ)²` |
|---|---|---|
| LHC collision | `1.4 × 10⁴ GeV` | `5.1 × 10⁻²⁹` |
| Crab synchrotron electrons | `1.5 × 10⁶ GeV` | `5.9 × 10⁻²⁵` |
| UHE cosmic ray (~10²⁰ eV) | `1.0 × 10¹¹ GeV` | `2.6 × 10⁻¹⁵` |
| Solar-system gravity | `k ~ 1/AU` | `~ 10⁻⁹¹` |

The UHE-CR row sits *at* current matter-sector bounds `|δ| ≲ 10⁻¹⁵` — a tight near-term
falsifier (§E.3 row 1). Crab is ~4 orders below current sensitivity; LHC and solar-system are
structurally out of any observational range.

### B.6.4 Sign positive — substrate stability ≡ spin-2 spectral positivity

The induced-gravity sign problem is famously delicate. The Sakharov-induced `1/G` comes from a
quadratically divergent loop whose sign is regulator-sensitive in generic field theory, and a
naive evaluation of TWT's matter content (chiral fermions with effective `ξ_eff = 1/4` from the
Lichnerowicz endomorphism) lands on the wrong side: `(1/6 − 1/4) = −1/12 < 0`. **The resolution is
that the apparent negative lives in the trace (conformal) channel — which is constrained, not
propagating — while the physical spin-2 graviton's sign is set by spin-2 spectral positivity,
which is positive by unitarity** (R-040).

In one paragraph: the graviton `h_{μν}` decomposes into spin-2 (the physical TT graviton, two
polarizations) and spin-0 (the conformal mode / trace). EH assigns these opposite-sign kinetic
terms; the conformal mode is non-dynamical in pure gravity, constrained away by the Hamiltonian
constraint, and is *not* a physical propagating fluctuation. (The constraint argument inherits
to the Sakharov-induced theory provided the induced action is diffeomorphism-invariant — which
is the case here, since the σ-model action `⟨Ω Ω⟩_0` plus matter is built from invariant
combinations and the Sakharov reduction preserves them.) Matter induces both channels through
the corresponding parts of `⟨T_{μν} T_{αβ}⟩`, and because EH assigns them opposite-sign kinetic
terms, they enter `1/G` with opposite signs. The trace channel comes in negative; the spin-2
channel comes in positive with coefficient `C_T > 0` (the central charge), positive by unitarity
in any consistent QFT. **The physical Newton constant is the spin-2 channel value, and it is
positive.**

The same physics in different language is **substrate stability**. The substrate's ordered phase
is stable: linear spin-wave theory for the canted DM ground state gives `ω²(k) ≥ 0` across the
Brillouin zone (no imaginary modes). The induced graviton is a collective fluctuation of this
stable medium, and it is massless (matter couples covariantly through the spin connection, the
induced action is diffeomorphism-invariant, and the only graviton mass term is the dim-6 preferred
frame remnant `(E/Λ)²`, far below bounds). For a stable medium, every physical propagating mode has
`E(k) ≥ 0` at every `k`; with no mass term to compensate, the gradient coefficient itself must
satisfy `1/G ≥ 0`, strictly positive for a non-marginal stable phase. **The sign carries no scheme
dependence**: a regulator rescales the magnitude but cannot make a stable medium's massless
collective mode carry negative energy.

**Why this works for TWT but not for generic induced-gravity programs.** The classical
induced-gravity sign problem arises in field theory *without* a stable ultraviolet completion:
integrating out matter against a hard cutoff with no medium underneath, the graviton's sign is a
property of the loop scheme rather than of any physical fluctuation, and it floats. For some
matter content and some regulators it comes out negative — the worry that motivated Adler's
review. **TWT is not in that case.** It has a real stable ultraviolet completion — the ordered
rotor phase — so the stability bound *applies*, and it forces `1/G > 0`. The same structural
property that distinguishes TWT (having a real substrate, not just a mathematical theory) is what
makes the sign argument bite where it does not bite generically. Note also that the chiral fermion
contributes positively to spin-2 (not just magnons), and the graviton is the *composite spin-2
projection* of the total stress-tensor correlator — positivity rests on the projected total
spectral density, not on any single substrate mode.

The honest scope. The claim is that the **sign** is correct within the induced-gravity
framework — *not* that "TWT has derived gravity." The result *removes a potential falsifier*
(wrong-sign gravity from chiral matter loops would have been fatal) and confirms consistency with
attractive Newtonian/Einstein gravity. The two genuinely hard parts remain open: the `C_T`
magnitude (pinning `Λ` within the bracket) and the explicit nonlinear graviton from the texture
tetrad below. *Claim the sign, not the theory.*

### B.6.5 ξ = 0 at leading order

A second potential falsifier looms in the non-minimal coupling `ξ R_curv φ²` of the heat-kernel
expansion. A naming note: the `ξ` here is **not** the fermionic effective coupling `ξ_eff = 1/4`
of §B.6.4 — those are two different objects doing two different jobs. The §B.6.4 `ξ_eff` is the
chiral fermion's contribution to the **trace (conformal) channel** via the Lichnerowicz
endomorphism `X = R/4`; the `ξ` of this subsection is the **rotor-scalar** non-minimal coupling
on the σ-model side, the parameter that would multiply `R_curv φ²` if the action carried such a
term. The conformal-cancellation worry below concerns this second `ξ`, not `ξ_eff`.

The Sakharov coefficient enters with a factor `(1/6 − ξ)`. At the **conformal value
`ξ = 1/6`** the leading `Λ²` Sakharov term cancels entirely — `G_N⁻¹ → 0` — a catastrophic latent
falsifier for the whole induced-gravity arc. If `ξ` were undetermined, the very existence of
induced `G` would be open.

The framework forces `ξ = 0` at leading order via a Maurer–Cartan shift symmetry (R-041). The
rotor σ-model action is built entirely from the Maurer–Cartan form `Ω_μ = R̃ ∂_μ R` — both the
kinetic term `⟨Ω Ω⟩_0` and the Skyrme stabilizer `⟨[Ω, Ω]²⟩_0` are functions of `Ω` only. Hence
the action has an exact global left-Spin(4) shift symmetry `R → g_0 R` (constant `g_0`), under
which `Ω` is invariant:

> `Ω_μ(g_0 R) = (g_0 R)~ · ∂_μ(g_0 R) = R̃ · g̃_0 · g_0 · ∂_μ R = R̃ · ∂_μ R = Ω_μ(R)`.

This is a non-linearly realized Goldstone shift on
the six grade-2 fluctuation directions — they are flat / Goldstone directions on the homogeneous
Spin(4) target.

A non-minimal coupling `ξ R_curv φ²` requires the *non-derivative* quadratic operator
`φ² = ⟨δR²⟩_0` (rotor fluctuation, *not* a derivative). Under the left-Spin(4) shift
`φ → φ + c`, this operator is *not* invariant: `⟨(φ + c)²⟩_0 ≠ ⟨φ²⟩_0`. Therefore the `ξ`-term
*breaks* the left-Spin(4) symmetry and is forbidden — the Adler-zero / Goldstone protection of a
derivatively-coupled field. Therefore

> `ξ = 0` at leading order; `ξ = 1/6` excluded. (R-041)

The catastrophic conformal-cancellation branch is removed. The residual is the dim-6
`(f_π/Λ)² ~ 10⁻⁴⁰–10⁻³⁹` order (across the §B.6.2 `Λ`-bracket) — same protection class as the
weak-equivalence-principle residuals, negligible.

### B.6.6 The texture tetrad — what closes, what doesn't

**Why naive front-embedding cannot source gravity.** A natural first guess is to identify the
symmetric spacetime metric with a 3D wavefront embedded in the 4D bulk via `x_4 = f(x)`. This
fails three ways: (i) the induced perturbation `δg_{ij} = ∂_i f · ∂_j f` is *quadratic* in `f`, so
no linear graviton exists; (ii) it is *rank-one*, so it cannot carry the two transverse-traceless
polarizations `h_+, h_×`; (iii) it is *positive semidefinite*, so a gravitational wave that
alternately stretches and contracts perpendicular axes is structurally forbidden. **Janet–Cartan
counting seals the verdict**: a generic 4D Riemannian metric requires up to `n(n+1)/2 = 10` flat
embedding dimensions; the TWT bulk offers only `5` (the `Cl(4,1)` ambient). Front-embedding
cannot source the gravitational metric.

**Why the substrate's own elasticity cannot source it either (R-164).** The second natural
guess is that gravity is *tree-level* rather than induced — that the Einstein–Hilbert term is
already sitting inside the banked quartic stabilizer, whose commutator `[Ω_μ, Ω_ν]` is the very
object the curvature is built from (R-149). It is not, and the reason is structural rather than
accidental. Projected onto the classified space of invariant quadratic forms (R-151), the
quartic and the Einstein–Hilbert density fall in **disjoint parity sectors** with exactly zero
overlap: the quartic is built on the definite Killing pairing — the same definiteness that lets
it play Derrick stabilizer — while the curvature is built on the indefinite `I_4` pairing, the
same indefiniteness that makes Lorentzian signature reachable at all (R-145, below). Internal
parity preserves the first and flips the second. *The property that makes the term a stabilizer
is the property that makes it gravitationally blind.* The conclusion survives beyond the
quadratic order: the quartic is algebraic in `Ω` while the curvature carries irreducible
second-derivative content, so configurations exist along which the quartic is exactly frozen
while `√g R` sweeps — which also excludes repackaging it as a cosmological term or as the
curvature-squared invariants (the Gauss–Bonnet direction included). More generally, no term in
the framework's banked first-derivative action class can contain the Einstein–Hilbert density:
**the substrate action is *stretching* elasticity, while gravity is *bending* elasticity**, and
the Sakharov loop is precisely the standard mechanism by which the second is generated from
fluctuations of the first. With front-embedding closed above, both tree-level routes are shut,
which leaves induced gravity not as a preference but as the only surviving route *within the
banked action class* — a genuinely new tree-level term, or the thermodynamic reading of Paper 2,
would reopen the question (negatives ledger N51).

The right object is the **texture tetrad** `e^a_μ[R, ∂R]` built from rotor *gradients* (not the
local value). The spatial winding face of a defect is exactly this kind of gradient structure:
the defect's spatial winding pattern is encoded in `∂R`, which IS what the texture tetrad uses.

The texture-tetrad metric `h_{μν} = ⟨Ω_μ I_4 Ω_ν⟩_0` is forced up to one premise (the
gauge-projection postulate). The Schur-lemma uniqueness step is exact — the commutant is
2D, `{id, I_4}`; the `c_1 = 0` step requires the gauge-projection postulate, which remains an
open premise (companion Result Index, R-042). The structural geometry is therefore **closed
conditional** (R-042); the absolute coefficient (#1-gap propagator) remains open. The **6→4
frame reduction is established at the structural level (R-145)**: the full texture metric is exactly a rank-4 frame square
`g = δ + QᵀQ − PᵀP = Eᵀ κ E`, with the ten-row extended frame `E = [δ; Q; P]` valued in a flat
internal space of signature `(7,3)` — the frame always nondegenerate (the δ legs absorb the
background; ten legs is numerically the Janet–Cartan count quoted above, but the legs are not
gradients: a flat-frame factorization, not an isometric embedding — the counting objection is
bypassed, not answered). Three structural consequences follow.

**(i) The signature menu is
forced:** the 3+3 split of grade-2 gives `λ_max(g) ≥ 1` always (at least one spacelike
direction) and at most three timelike ones — the nondegenerate menu is
`{(0,4), (1,3), (2,2), (3,1)}`, an all-timelike `(4,0)` texture is structurally impossible,
and each menu item is realized by an explicit rotor field. The menu is derived; nature's
`(1,3)` pick is not — it is the vacuum/EOM selection. The invariant form of the
`θ₀ > 2` threshold (R-145) is that the SD legs must beat the flat background (`‖P‖ > 1`): no
perturbative texture is Lorentzian, and the Euclidean→Lorentzian transition passes through a
degenerate metric — light-cone birth.

**(ii) The reduction is canonical and selection-free:**
whenever the signature is Lorentzian, the ten-row frame factors through a κ-isometric
embedding onto a four-row tetrad, unique up to `O(1,3)` (tetrad existence per metric is
R-042's vierbein; the frame-level factorization and its uniqueness go beyond it)
— so what the EOM owes is only the signature pick, not any additional frame choice.

**(iii)
The first-order scaffold is complete:** the Maurer–Cartan form is exactly flat
(`dΩ + Ω∧Ω = 0`), so the substrate supplies both first-order variables — the
frame (the `I₄`-bilinear components of `Ω`) and the spin connection (`Ω` itself) — from the
one rotor field, with the Cartan structure equation automatic; all metric curvature rides the
frame-leg derivatives (the Gauss-equation face — closed below, R-149). The
substrate's internal action on the frame legs is the compact `SO(3)×SO(3)`; tetrad boosts are
not substrate-internal, so local Lorentz symmetry is a redundancy of the reduced description —
the coherent companion of the §B.6.3 emergent-Lorentz protection.

The Gauss-equation face **closes at the structural level (R-149)**, completing the
first-order scaffold. Four exact facts chain: the frame legs' curl is
**algebraic** in the flat connection — `∂_μE_ν − ∂_νE_μ = −L([Ω_μ, Ω_ν])` (Maurer–Cartan
flatness plus the legs' linearity in `Ω`; for a generic non-flat connection this curl would
be independent second-derivative data); the leg map inverts on grade-2 (the `I₄` pairing is
the signed Hodge pairing), so all of `dΩ` is recoverable from `dE`; the induced tangential
connection `Γ̃^λ_{μν} = g^{λρ}κ(E_ρ, ∂_μE_ν)` is metric-compatible with torsion equal to that
curl and obeys the flat-ambient **Gauss equation** — its curvature is a *quadratic form* in
the κ-normal part `S = (1−Π)dE` of the frame-leg derivatives (no symmetry of `S` is assumed;
the torsion lives in its antisymmetric part); and Levi-Civita differs from it by a contorsion
*algebraic* in `κ(E, L([Ω,Ω]))`. Net result: **`Riem(g)` is an algebraic function of the
pointwise first-order data `(E, Ω, dE)`** — no derivatives of the frame data beyond first
order enter (no `ddE`/`ddΩ`; equivalently the closure drops `Riem` from third- to
second-derivative order in the rotor field, since `dE` itself carries `ddR`). The identity is
exact and holds at **all four nondegenerate menu items** `(0,4), (1,3), (2,2), (3,1)` — it
needs nondegeneracy, not the Lorentzian pick — with the Gauss block and the torsion block each
the same order as `Riem` itself (neither decorative). This settles, in the negative, the
question R-145 left open — whether the Gauss-equation face needs data beyond `(E, Ω)`.
Fluctuations enter the induced-EH spectral sum only through `(S, [Ω,Ω])` at quadratic order,
so what `C_T` still lacks is the kernel's mode measure, not more kinematics (the settled-core
verdict for the gravity arc as a whole is §B.6.7's).

### B.6.7 The unification

Combined with `γ = 1` from matter-as-defect (B.6.3), the induced EH term satisfies all three
conditions for physical gravity on TWT-structural grounds:

| condition | reduces to |
|---|---|
| magnitude Planckian (`Λ ∈ [0.16, 0.72] M_Pl`) | substrate spectral density and cutoff |
| sign positive (`1/G > 0`) | substrate stability + spin-2 spectral positivity |
| Lorentz-invariant form (`γ = 1`) | matter-as-defect (covariant regulator) |

All three reduce to substrate properties — stability, unitarity, single-light-cone matter — each
independently established, the magnitude row through the registered spectral-sum import (I-3,
§B.6.2). **The conceptual core is settled, at that stated conditionality.** What remains is the explicit `C_T`
computation, the `O(1)` spin-2 projection coefficient, and the substrate spectral sum on the
single emergent light-cone — best carried out in the first-order (Cartan / spin-connection)
formulation of §B.6.6 (R-145, R-149): the frame and the spin connection are both supplied by
the one rotor field with the Cartan structure equation automatic, `Riem(g)` is algebraic in the
first-order data `(E, Ω, dE)`, the spectral sum's integrand shape is fixed as a quadratic form
in `(S, [Ω,Ω])`, and what remains for `C_T` is the dynamical mode measure alone. And that
mode measure now enters through only a **finite, small** number of channels (R-151): the
R-145 internal symmetry — the product `SO(4)_tangent × SO(3)_SD × SO(3)_ASD` (a product,
not a locked diagonal, because the internal gauge freedom (R-145) rotates leg-*values*
tangent-index-free)
— forces the quadratic form in `(S, [Ω,Ω])` into an **8-dimensional space of invariant
quadratic forms** (4 parity-even + 4 parity-odd, the SD/ASD channels exchanged by parity via
the exact `[SD,ASD] = 0` block structure). So, *given the unbroken symmetry*, `C_T` is
a kernel-weighted combination of **at most 4 numbers** — not an unknown function; the residual
is the kernel values themselves plus the spin-2/Ricci sub-projection that pins the exact `≤ 4`
(a dynamical diagonal-locking of the frame would raise the count). The sign is unaffected by the formulation choice: the stability argument never
invoked either.

Two free wins inherited at the structural level, worth flagging in passing:

- **Weinberg–Witten preemption.** The theorem's operative premise fails here: it requires an
  exactly Lorentz-covariant conserved fundamental stress tensor, and in TWT Lorentz invariance
  is emergent over the D4 substrate — there is no such exact fundamental `T^{μν}` for the
  theorem to act on (compositeness per se is not the evasion; the premise failure is).
  Weinberg–Witten does not apply.
- **GW170817 multimessenger consistency.** `|c_GW/c − 1| ≲ 10⁻¹⁵` is automatic for matter-loop
  induced gravity riding the same wavefront — `c_GW = c_γ` structurally, not coincidentally.

---

## §B.7 — The cosmic frame

The arrow of time, the three asymmetries, the constancy of `c`, and the cosmological constant.
This chapter shows how four facts about the universe a reader would treat as separate input
constraints fall out of `+e_4` propagation and one identity from many-body physics (Volovik's).

**Mathematical setting.** The substrate's phase-locking direction is `+e_4`. The wavefront
foliation along which `τ_5` advances is what we will call the comoving frame — coincident with the
cosmological one. Volovik's identity for self-sustained quantum liquids: in thermal equilibrium at
zero external pressure, the Gibbs–Duhem relation forces `ε − μ n = −P = 0`.

### B.7.1 The arrow of time as `+e_4` propagation

The arrow of time is not a separate postulate. The wave propagates along `e_4` in a definite
direction; observers experience this as the passage of time. "Time goes forward" is the statement
"the wave propagates along `+e_4`" read from inside the wavefront (R-043).

Causality is the same fact from another angle: causes precede effects along `e_4` because `e_4` is
the direction the wave carries influence. The light-cone structure of relativistic causality
emerges from `+e_4` under the wavefront isomorphism (§B.1).

### B.7.2 Three asymmetries from one initial condition

Three observed asymmetries usually treated as independent (R-044):

- **Thermodynamic arrow** — entropy increases toward the future.
- **Causal arrow** — causes precede effects.
- **Weak handedness** — parity violation, weak sector left-handed.

In TWT these are not three independent cosmological inputs. They are three observable
manifestations of **one fact**: the wave's propagation direction `+e_4`. The causal arrow is `+e_4`
directly. Weak handedness traces to `+e_4` because chirality is defined by orientation relative to
the propagation axis: the parity-odd condensate `⟨I_4⟩ ≠ 0` rides the wave's chiral DM
contribution (§C.5.3), while *which* chiral factor the weak force gauges remains the one counted
weak-sector bit (`weak = SD`, §C.4.2). The thermodynamic arrow is the medium's irreversible
response to its own drive.

This is a unification claim, stated with its one condition. The SM treats parity violation as an
empirical fact added by hand (`V−A`); the framework ties it to the same `+e_4` that picks the
arrow of time, given the weak = SD bit (§C.4.2). One IC plus one counted bit, three asymmetries.

### B.7.3 `c_meta = c` on average

For a uniform offset `c_meta ≠ c` across the entire wavefront, the framework provides no
observational signature: a global rescaling of all length and time scales would be removed by
coordinate redefinition. The structural prediction is therefore **`c_meta = c` when averaged
across the wavefront** (R-045).

A time-varying global `c_meta(τ_5)` is observable as cosmological expansion dynamics (and is a
falsifier handle — sector-dependent or epoch-varying differential `c_meta` is canonical falsifier
§E.3 row 8, closely tied to the `c_GW = c_γ` constraint §E.3 row 3).

### B.7.4 The Hubble radius as causal/crossover scale; Volovik's dissolution of Λ

The Hubble radius is the **causal/crossover scale** at which wavefront-expansion dynamics overtake
well-attraction (R-046) — not the geometric radius of curvature. The §A.2 topological-`S³`
identification does not commit to a finite radius of curvature equal to `R_H`. The genuine
geometric curvature radius, if any, must satisfy `|Ω_k| ≲ 0.0026` (Planck 2018 + BAO, 1σ upper),
giving `R_curv ≳ 20 R_H` — effectively spatially flat at observational precision.

**Dark energy and the cosmological constant.** Induced gravity (§B.6) cannot consistently disclaim
the cosmological-constant problem: the same heat-kernel expansion that yields `1/(16π G) ~ C_T Λ²`
at order `k²` generates a vacuum energy `~ C_T Λ⁴` at order `k⁰`, with naive value `~ M_Pl⁴ ≈
10¹²⁰ ρ_obs`. This is the standard Λ catastrophe.

Volovik's self-sustained-medium identity supplies the native resolution (R-047). For a
self-sustained quantum medium at zero external pressure, the Gibbs–Duhem relation

> `ε − μ n = −P = 0`

forces the **gravitating** vacuum energy to vanish *exactly in equilibrium*. Sub-Planckian and
trans-Planckian contributions cancel as a thermodynamic identity, not as a tuning. The substrate is
exactly the textbook self-sustained medium.

The TWT-specific adaptation. The substrate is driven-dissipative, not equilibrium. The deviation
from equilibrium is set by the drive. This offers a *structural reason* dark energy is small,
nonzero, and tied to the front dynamics — rather than a tuning of `Λ` against quantum vacuum
contributions. The residual value `Λ ~ H²` is the wave drive's signature, and computing it
requires the off-equilibrium computation at the §D.5 #1 gap. We name this value-gated and move on
(canonical falsifier §E.3 VG-2; full treatment §E.1).

The hook here is the **dissolution at equilibrium**. The standard Λ catastrophe is not just
suppressed — it is *removed at the equilibrium identity level*, by many-body physics that the
substrate exactly satisfies. (*Import notice:* Volovik's identity is an equilibrium theorem
applied at the substrate level — registered as **I-4 in companion Section 13**, status
NAMED-CRACK: the substrate is driven, and the deviation from the equilibrium premise is
precisely the gated `Λ ~ H²` residual, so here the crack in the import's premise has itself
been converted into the physical prediction.) What remains is the off-equilibrium residual, named openly. This is
the kind of move the framework makes elsewhere — turn a fine-tuning problem into a structural
identity plus a named open residual.

---

## §B.8 — The macroscopic limit

The last hook of Part B. Bodies — planets, stars, the N-body problem — read in TWT as defect
features of one wavefront. The L/Q split that sorts micromatter species (lepton vs baryon) is the
same algebraic split that sorts macroscale conserved invariants (angular momentum vs spent
integrals). One algebraic structure, two manifestations.

**Mathematical setting.** Worldlines are Cl(4,0) grade-1 elements `R_a(t) = r_a(t) + t · e_4`.
The mass-weighted grade-2 object `𝓛 = Σ_a m_a · R_a ∧ Ṙ_a` has `𝓛̇ = 0` (central-force pairwise
interactions cancel by Newton-3). Barycentric coordinates `s_a = r_a − R_cm`, `w_a = v_a − V_cm`
satisfy `Σ_a m_a · s_a = 0` and `Σ_a m_a · w_a = 0`.

### B.8.1 COM reduction in Cl(4,0)

Expanding `R_a ∧ Ṙ_a = r_a ∧ v_a + (r_a − t · v_a) ∧ e_4` splits `𝓛` into six bivector
components: three "spatial" blades `r ∧ v` in the L-orbit `span{e_{12}, e_{13}, e_{23}}` and
three "time-mixed" blades involving `e_4` in the Q-orbit `𝓠`. Barycentric coordinates annihilate the time-mixed
blade and leave

> `𝓛̃ = Σ_a m_a · s_a ∧ w_a ≡ L ∈ span{e_{12}, e_{13}, e_{23}}`. (R-048)

Six conserved blades collapse to three on `P = 0, R_cm = 0`. The three that vanish are the
time-mixed ones; the three that survive are the L-orbit ones.

### B.8.2 The L/Q split, micromatter and macroscale

The conserved bivector `L` lands in the **L-orbit** — the same algebraic space that hosts leptons
(§C.1) — and the spent integrals `(P, R_cm)` live in the orthogonal **Q-orbit** that hosts baryons
(§C.1). The decomposition is orthogonal under the bivector inner product.

> **One algebraic split, two manifestations.** (R-049)

At microscale the split sorts matter content: leptons in `𝓛`, baryons in `𝓠`. At macroscale the
same split sorts conserved invariants: angular momentum in `𝓛`, spent integrals in `𝓠`. The
identification is not metaphor; it is the same `Cl(4,0)` bivector inner-product split, doing two
jobs at two scales.

### B.8.3 Sundman's collision condition

Let `I = Σ_a m_a · |s_a|²` (polar moment of inertia), `T = (1/2) Σ_a m_a · |w_a|²` (kinetic
energy). Cauchy–Schwarz applied to the bivector norm gives

> `|L|² = |Σ_a m_a · s_a ∧ w_a|² ≤ (Σ_a m_a · |s_a| · |w_a|)² ≤ (Σ_a m_a |s_a|²) · (Σ_a m_a |w_a|²) = 2 I T`.

As `I → 0` with `T = E − U` and `U → −∞`, kinetic and potential energies diverge in magnitude at
the same rate: `T ~ |U| ~ 1/r`. The bound then forces `|L|² ≲ 2 I T ~ r → 0`. Since `|L|` is
conserved along the flow, `L = 0`: **triple collision forbidden unless `L = 0`** (R-050).
Worldlines can fall onto their common `e_4` axis only when they are not circulating about it.

The chain depends on §B.5.3's Newtonian far-field `U ~ 1/r`; Cauchy–Schwarz on the bivector norm is
generic. The Sundman condition follows.

### B.8.4 The atlas is a projection artifact

Here is the closing hook of Part B. The N-body problem in classical mechanics carries an *atlas
with seams* — local coordinate patches that fail at close approach, where the standard variables
diverge and Hamiltonian-integrability analysis hits the Poincaré–Bruns non-integrability barrier.
The TWT picture says: **that seam is in the projection from field to bodies, not in the dynamics**
(R-050a).

The matter-as-defect ontology (§A.3) makes the *Eulerian* picture natural. There is one wavefront field

> `U(x, t) : ℝ⁴ → S³` (the Skyrme target, §C.1)

on `Cl(4,0)` spatial slices, evolved through meta-time `τ_5` by the `Cl(4,1)` substrate wave
equation, carrying `N` topological-density features. The Skyrme baryon density

> `b(x, t) = (1/(24π²)) · εⁱʲᵏ · Tr[U⁻¹ ∂_i U · U⁻¹ ∂_j U · U⁻¹ ∂_k U]`,
> `∫_{ℝ³} b · d³x = B = Σ_a B_a ∈ π_3(S³) = ℤ`,

is conserved and localized on the defect clusters. The Lagrangian-side body position is then the
projection

> `R_a(t) = (1/B_a) · ∫_{V_a} x · b(x, t) · d³x`,

where `V_a` is a spatial region enclosing only the `a`-th cluster.

**In the Eulerian representation, the field evolves once.** The atlas with seams reappears only
when one extracts individual `R_a(t)` as separate computational objects — and that re-extraction
is what hits Poincaré–Bruns non-integrability. The seam is in the field → feature projection, not
in the dynamics. Close approach is, at the field level, a smooth localized superposition of two
topological-density features; it only *looks* like a near-collision after one has chosen to read
the field as a set of bodies. The substrate has no near-collision problem because the substrate is
not a set of bodies — it is one wavefront with `N` localized features in it.

(Honest scope. The multi-defect `Cl(4,1)` wave equation with `N` back-reacting topological sources
is not constructed in this paper; its construction is a structural target. What we claim here is
the **ontology** — bodies are defect-features of one wavefront — and the **reframing** that
follows from it. The dynamics-coherent version of the reframing depends on the
multi-defect well-posedness named as canonical structural-coherence falsifier §E.3 SC-1.)

### Closing of Part B

This closes Part B's "emergent classical physics" arc. From `Cl(4,0)` + `e_4` propagation + the
matter-as-defect ontology, we have recovered: Lorentzian signature, special relativity, quantum
mechanics, Bell at the Tsirelson bound, electromagnetism with no monopoles, the fine-structure
constant as a reactive grade-0 invariant with its sibling g, induced gravity with sign + form +
magnitude bracket, the cosmic arrow of time, and the macroscopic limit — including a reframing
that locates the classical N-body seam in the field → feature projection rather than in the
dynamics. None of these are postulates of the framework: each is a consequence of the premises
listed in the Opening — in places through the registered imports the body labels at their
use-sites (companion Section 13).

Part C now develops the Standard-Model structural skeleton — charges, three generations, the
gauge group. The reader who wants only the picture can stop here. The reader who wants the
engineering continues.

---

# Part C — Matter, charges, generations, the gauge group

*The Standard Model's structural skeleton, derived from the substrate. The tier mix begins to
diversify here: charge quantization and the Weinberg angle are tight algebraic identities; the
gauge group structure follows from D4 orbit content; the lepton-mass triplet is currently a
cross-validated fit rather than a forward derivation; the Cabibbo ratio is a candidate
identification. The Result Index (companion Section 1) keeps the bookkeeping crisp.*

---

## §C.1 — The Skyrmion

A defect is a topologically protected pattern in the rotor field. The standard mathematical
realization is the **Skyrmion**: a localized field configuration with a non-zero winding integer
in `π_3` of an `S³`-target. This section gives the construction in the form the rest of Part C
uses.

### C.1.1 Hedgehog ansatz, Skyrme BVP, Derrick stability

A static defect localized at the origin is described by a rotor field `R(x)` with hedgehog
boundary conditions

> `R(0) = −𝟙`,  `R(|x| → ∞) = 𝟙`,  with `R(x) = exp(i n̂ · σ · F(r))`

where `n̂ = x̂` and `F(r)` is a radial profile with `F(0) = π`, `F(∞) = 0`. The Pauli matrices
`σ_j` here are a basis of three imaginary units (`σ_j² = −1`) of whichever target three-sphere
the defect winds into — for leptons the subgroup `S³_𝓛 = exp(𝓛)`, for baryons the coset
`S³_𝓠 = Spin(4)/Spin(3)` (§C.1.3). The Skyrme energy functional has the same form in both
cases because both targets are *round* three-spheres; the L-orbit subgroup and Q-orbit coset
differ in their group-theoretic role, not in the local metric of the target manifold. This is
a notational bridge to the standard Skyrme literature, not a convention switch. The Skyrme boundary
value problem (BVP) for `F(r)` extremizes a kinetic + quartic-stabilizer action. Derrick's theorem
forbids a stable finite-size defect built from the kinetic term alone (it scales away under
dilation); the Skyrme quartic stabilizer provides the size-fixing term, and the BVP has a
well-defined ground state of integer winding.

The asymptotic boundary condition `R(∞) = 𝟙` compactifies the spatial slice `ℝ³` to `S³` —
the topological 3-sphere named in §A.2 — and the configuration becomes a map `R : S³ → S³`. Its
homotopy class is its degree: an integer in `π_3(S³) = ℤ`.

### C.1.2 The Skyrme mass formula and the B = 2 sector

The minimum of the Skyrme functional gives a baryon mass at the dressed-coupling level

> `M_0 = 36.47 · f_π / e`  (R-051),

with `f_π ≈ 129 MeV` the cell-scale mass and `e ≈ 5.45` the **empirical** (ANW) Skyrme
stabilizer. The dressed-coupling relation `e ≈ √18 / (D/J)` (§D.4) *reproduces* this value at
the ~1% level from the lepton-calibrated `D/J ≈ 0.787` (predicted `e ≈ 5.39`; the `√18`
identification is itself flagged as possibly coincidence-riding, §C.3.11). Quoting `≈ 5.45` as
the *output* of the relation would be circular — the
baryon-side `D/J ≈ 0.778` of §C.3.11 is itself *defined* by back-solving `√18/e` at the
empirical `e = 5.45`. The ~1.1% cross-sector spread between the two calibrations is the honest
content of the over-determination signal. The numerical coefficient
`36.47` is standard ANW Skyrme phenomenology, fixed by the BVP (R-051). With the displayed
inputs this
lands at `M_0 ≈ 863 MeV` — about **8% below the empirical nucleon mass** of `939 MeV`.

**The rotational band — the deficit explained (R-133).** The 8% is not a model failure: it is
the missing collective-rotation term. The improved mass equation is the band

> `M(J) = M_0 + J(J+1)/(2Θ_0)`,  `Θ_0 = 106.76/(e³·f_π)`  (R-133),

with both coefficients from the *same* exact BVP profile (the exact inertia integral is
`Λ = 50.98`, matching the standard literature value; an earlier coefficient `97.27` —
numerically `36.47·8/3` to 0.02%, an unexplained algebraic relation to the mass coefficient
rather than an inertia integral — is consistent with a truncated-grid artifact, provenance
suspect; corrected at R-133). At the counted ANW
couplings this gives `M_N = 936.4 MeV` (−0.3%),
`M_Δ = 1229.8 MeV` (−0.2%), splitting `293.4 MeV` (+0.1%) — with the honesty note carried
explicitly: `f_π` and `e` were *historically fitted to N and Δ* (ANW), so the closure is a
pipeline consistency, not a new prediction; no new parameter enters. The `J = 1/2, 3/2` lattice
rides the Finkelstein–Rubinstein fermionic *selection* (§B.3.5 — compatible, not forced;
conditionally induced per R-141, the result unchanged either way), and
the `J(J+1)` band is the concrete static-face instance of the moduli-correction class §D.4.6's
charge tower (R-131) names — here on the spin/isospin moduli, distinct from the `U(1)` phase
tower. The leading-order static BVP delivers the 8% `M_0` figure honestly; the rotational band
term (R-133) supplies the missing rotor correction at the counted couplings — further
refinements (centroid corrections, spin-orbit terms) live at the level of §D.4's full
medium Lagrangian. The ~10% cross-scheme spread reflects the open fork between local and
phason-spoiled dressed couplings (§D.4.2, §E.3.5).

**Beyond one defect — nuclear binding exists classically (R-135).** The first `B = 2`
(two-defect) computation of the dressed sector: the rational-map ansatz `U = exp(iF(x) n_R·τ)`
with the standard degree-2 map `R(z) = z²` reduces the full 3D energy *exactly* to a radial
BVP (the angular content enters through the computed integral `I(z²) = 5.8083` and the exact
degree identity `(1/4π)∫ψ² = B`), solved with the same certificated machinery as R-133
(the `B = 1` limit regresses to `36.46`). The result is
the inequality

> `E(B = 2) ≤ 71.543 · f_π/e  <  2 × 36.462 · f_π/e`  (R-135),

a strict 1.89% below the two-nucleon threshold: the `B = 2` channel is **classically bound**
(strict sub-additivity), with the attraction's *sign* predicted and no magnitude claimed —
conditional on the inherited hedgehog-minimality premise of the `B = 1` sector. At the
counted couplings the classical binding is `≥ 32.7 MeV`; the observed deuteron binding is
`2.22 MeV`, and the gap is the *known* classical-overbinding character of the massless Skyrme
sector — the physical magnitude lives at the `B = 2` collective quantization + pion-mass
level, both named follow-ups (the pion-mass face is discharged for the *existence/sign*
conclusion by R-137/R-138 below; the magnitude stays open). The indicial structure generalizes
cleanly (`s² + s − 2B = 0`; the `B = 1` pair
`{+1, −2}` is §D.4.6's derived tail, and the `B = 2` tail steepens to `x^{−2.56}`). This is
also the first `N = 2` datum for the multi-defect well-posedness falsifier (§E.3 SC-1),
scoped honestly: the ansatz-reduced BVP is clean and certificated; the full-3D *static*
face is now delivered ansatz-free by R-144 (below); the dynamical face remains open.

**The quantization face — the deuteron's quantum numbers (R-136).** Quantizing the axial
`B = 2` configuration's collective coordinates upgrades the identification to the
quantum-number level. The `z²` map's exact symmetries (the axial iso-lock
`R(e^{iα}z) = e^{2iα}R` ⇒ body constraint `L₃ + 2K₃ = 0`; `R(−z) = R`; `R(1/z) = 1/R`) plus
the Finkelstein–Rubinstein loop signs (via the Krusch homotopy formula for rational maps —
an imported topology theorem, companion Section 13) give, on the `K₃ = 0` tower,
the selection rule **`I + J` odd**: the ground state has *exactly the deuteron's quantum
numbers* `J^π = 1⁺, I = 0` (parity from the derived internal parity map `R_P = −R`,
convention anchored to the nucleon's `+`; the `|K₃| ≥ 1` towers provably lie higher), the
scalar `(0,0)` dibaryon is **topologically forbidden**, and the lowest isovector `(1,0)` —
the `np` spin-singlet channel — sits above by `~40 MeV` at ansatz level (exact factorized
moments on the R-135 profile: `V_⊥ = 312.5 > U_⊥ = 194.6` in `1/(e³f_π)` units). The headline
physics is literature-known (Braaten–Carson 1988; Leese–Manton–Schroers 1995; Krusch 2003 —
citations pending independent verification); what R-136 records is the conditional tiering —
the rule holds given the collective-quantization premise and the fermionic selection (§B.3.5,
*not* decided here; conditionally induced per R-141, the result unchanged either way) — the
certificated moments, and one further consequence: under the *bosonic* branch
of the spin-statistics fork the rule flips to `I + J` even, predicting a bound scalar
dibaryon ground state — empirically refuted, so the observed deuteron is a **second,
independent empirical anchor** (sharing the collective-quantization premise) selecting the
fermionic branch. Spectrum *values* remain rigid-rotor estimates (overbound, as stated
above); the binding magnitude stays open at the quantization-refinement level (the
pion-mass face is discharged by R-137/R-138 below).

**Pion-mass robustness (R-137).** The owed pion-mass re-check of both results above is
discharged: deforming the functional by the standard chiral-breaking term
`(μ²/4)x²(1−cosF)` at the *physical* pion mass (`μ = m_π/(e·f_π) = 0.196`, `m_π = 138 MeV`
isospin-averaged — a named witness import used identically on both sides, not a counted
dial; the term's form is an imported probe, not a substrate term) leaves the
below-threshold inequality intact and marginally *stronger*: massive coefficients
`74.31 < 2×37.90 = 75.80`, margin `1.96%` vs the massless `1.89%` (binding `≥ 35.2 MeV`;
mass-extended Derrick virial `E2 + 3E_m = E4` certifies both profiles; the tail becomes the
Bessel form `x^{−1/2}K_ν(μx)` with `ν = √(2B+¼)`, whose `μ → 0` index reproduces the
massless exponents exactly). R-136's topological selection is untouched by the mass term.
The same computation quantifies a *second, distinct* scheme axis alongside the local/phason
fork above: the pion-mass axis is object-dependent — mass coefficients shift mildly
(`+3.9%`) but the collective inertia strongly (`Λ = 50.98 → 33.52`, `−34%`, the exponential
tail killing the long-ranged integrand) — so the massless-model `N/Δ` closure (R-133) does
*not* transfer to the massive variant at the same couplings: the massive scheme requires
its own `(f_π, e)` refit (the known massive-ANW direction) — a fork named at R-137 and
**executed at R-138** as a parallel branch; the standing baseline remains the massless model.

**The refit branch, executed and adjudicated (R-138).** The refit of
the *same two dials* to the *same two observables* in the massive functional (self-consistent
`μ = m_π/(e·f_π)` per trial) lands at `f_π* = 108.26 MeV`, `e* = 4.843` (`μ* = 0.263`) —
corroborating the massive-ANW literature values — with `M_N`, `M_Δ` closed exactly. Three
consequences follow. *First*, an exact fit-invariance: in any scheme closing `N/Δ` with
the band equation, the splitting alone pins `1/Θ₀ = (2/3)(M_Δ − M_N) = 195.4 MeV` — so the
`Λ_QCD` candidate, the top exclusion, and the `Σ_c−Λ_c` residual are all fork-invariant; in
particular the fork does *not* resolve that residual ("scheme artifact" is eliminated, and
the weight redistributes to both of R-133's named candidates — the Callan–Klebanov-class
inertia and the `hf_c` re-fit). *Second*, the owed re-checks: the `B = 2` margin at the
refit couplings is `1.87%` (binding `≥ 32.3 MeV`), and the moment ordering
`V_⊥ = 222.1 > U_⊥ = 135.6` keeps the deuteron the ground state — the binding and ordering
conclusions are now verified across the entire fork (the margin is non-monotonic in `μ`:
`1.89% → 1.96% → 1.87%`). *Third*, the baseline
decision, recorded as bookkeeping rather than derivation: **the massless model stays the
standing baseline**, on parameter economy (2 counted inputs vs the branch's 3 — `m_π` is
load-bearing in-branch), on one *hedged* empirical face (of the two-route × two-scheme
`√N/e`-vs-`D/J` grid, the only sub-2% convergence is massless-`√18`, itself flagged as
possibly coincidence-riding), and on import-minimization
(the branch functional carries the underived `(1−cosF)` chiral-breaking form as a
load-bearing structural import; the massless functional carries none). The branch constants
are retained for uses where the physical pion tail is essential — e.g. asymptotic
nucleon–nucleon interactions.

**The tensor force — from the dipole tails, not from lattice anisotropy (R-139).** The
derived tails make the asymptotic defect an exact **triplet of orthogonal pion dipoles**:
`π_a = −C∂_aY` with `Y = e^{−μr}/r` (at `B = 1` the Bessel index `ν = 3/2` is half-integer,
so the massive tail is *elementarily* the dipole-Yukawa profile `(1+μr)e^{−μr}/r²`; the
dipole strength is nearly **fork-invariant** — `C = 8.63` massless, `7.91` at the probe
couplings, `7.66` in the refit branch, gently screened by `μ`). Two
well-separated defects with relative iso-orientation `O` then interact as dipole pairs:

> `V(R, O) = πC² [ (3O_RR − TrO)(1 + μR + μ²R²/3) + TrO·μ²R²/3 ] e^{−μR}/R³`  (R-139),

whose tensor radial function is *identical* to the one-pion-exchange tensor shape and whose
central piece (`∝ μ²`) vanishes in the massless limit — the aligned-channel zero. The sign
and magnitude are pinned by a 3D product-ansatz grid computation, not by convention (the
quadratic cross term carries the classic source-vs-field-energy bookkeeping ambiguity): the
aligned channel vanishes, π-rotation about the axis *parallel* to the separation is
repulsive, and π-rotation about a *perpendicular* axis is **attractive** — the same channel
the bound `B = 2` configuration (R-135) realizes — with magnitudes matching the law at the
10–20% level raw and the residual accounted by named grid systematics (an independent
box-size/refinement probe puts the Richardson-extrapolated ratios at ~0.9–1.0). The headline
physics is literature-known (Skyrme; Jackson–Jackson–Pasquier 1985; Manton–Sutcliffe —
citations pending independent verification); what R-139 adds is the in-framework
derivation from the derived tails with fork-resolved constants, the exact-identity
certificates, and one scope correction: the dominant tensor
force is OPE-class — D4 lattice anisotropy contributes only the sub-percent
`η_DM = (D/J)²/144 ≈ 0.43%` (a calibrated face preserved as a named gated
row). The quantum OPE strength (`g_πNN`-class) awaits the nucleon-state projection of
`O_ab` — a named follow-up; the deuteron's S–D mixing and quadrupole moment live there.
With R-135–R-139 in place, the `B = 2` program's constructive faces are complete; the one
located residual is the binding *magnitude* (rigid-rotor overbinding `~113/~124 MeV`,
massless/refit), which requires the full-field torus and beyond-rigid-rotor quantization.

**The full-field torus — the ansatz-free `B = 2` computation, and SC-1's second datum
(R-144).** The reduction caveat of R-135 is discharged at the classical level
(R-144): a full 3D, **ansatz-free** minimization of the
same static energy — the 3D functional is certified as *being* that sector (its
hedgehog reduction to R-135's radial integrand is an exact symbolic identity, and its
discretization is `h²`-certified against the 1D quadrature) — confirms the below-threshold binding with no
symmetry *constraint* during the flow: charge-conserving gradient descent from a degree-2
configuration stalls at `E(B=2) < 2·E(B=1)` on the same grid at both resolutions
(stall-vs-stall margins `1.79%`/`3.06%` at `N = 64/96`, and `≥ 2.95%` under an independent
`B = 1`-side continuation check — both stalls are upper bounds, and the binding *sign* is
independently protected by the continuum anchor `2 × 36.462 ≈ 72.923 > 71.617`), and the
minimizer it finds is the **toroidal** `B = 2` solution — baryon density maximal on a ring
at `r ≈ 1.55`, center density `2%` of maximum, sharpening along the descent (the literature
torus; corroborative — the initial condition was axial and the cubic grid enforces the
moment equality, so the ring/center profile is the genuine evidence). R-135's
would-change-if (c) fired as predicted: the full field *keeps* the binding, deepening at
`N = 96`; it does not un-bind. This is also the **second datum** for the multi-defect
structural-coherence condition (§E.3 SC-1): the two-defect sector is variationally coherent
in full 3D with no reduction — scoped honestly as the *static* face; the dynamical
multi-defect `Cl(4,1)` EOM remains unformulated (kernel-gated), and no binding *magnitude*
is claimed (the classical massless overbinding is the known character; the magnitude
residual now rests on beyond-rigid-rotor quantization over this torus plus the massive-pion
full-field run, both named). A methodological fact rides with it: lattice winding is
protected only in the smooth sector — recorded unwinding events (an under-resolved core;
adaptive-optimizer vacuum noise) make a charge-guard
and resolution discipline load-bearing for any future lattice flow on the substrate (the
flow-level face of R-143's lattice-`π₃` caveat).

### C.1.3 Exactly two conserved windings — chiral counting, orbit relabeling

The substrate's rotor field takes values in `Spin(4)`, and `π_3(Spin(4)) = ℤ × ℤ` (R-002). The
**two `ℤ` factors come most directly from the chiral factorization**
`Spin(4) = SU(2)_+ × SU(2)_−`. There is exactly one winding integer per chiral factor; that is
the cleanest source of the "exactly two windings (B, L)" result.

The framework's working basis is the **orbit basis** `(n_𝓛, n_𝓠)`, obtained by the symmetric-pair
/ fibration bridge of §A.5.2: `Spin(3) ↪ Spin(4) ↠ S³_𝓠 = Spin(4)/Spin(3)`, with
`π_2(Spin(3)) = 0`, gives `0 → ℤ → ℤ × ℤ → ℤ → 0`. The pair (fiber-winding into the diagonal
`Spin(3) = exp(𝓛)`, base-winding into the coset `S³_𝓠`) is a valid basis for `π_3(Spin(4))` —
a change of basis from the chiral basis, not an identification with it. So the framework's
working assignment **leptons wind into the L-orbit `S³_𝓛`** and **baryons wind into the coset
`S³_𝓠`** is a coset-respecting relabeling of the chiral counting (R-052).

**A subgroup-vs-coset clause to honor.** The lepton hedgehog is a *subgroup-valued* map into
`exp(𝓛) = Spin(3)` — a genuine subgroup, with `π_3 = ℤ` directly. The baryon hedgehog is a
*coset-valued* map into `Spin(4)/Spin(3) ≅ S³_𝓠` — a coset 3-sphere, with `π_3 = ℤ` because the
coset is also `S³`. Both targets are three-spheres and both inherit the standard Skyrme degree
formula, but they are topologically distinct map types. The standard SU(2)-group ansatz reads
as the lepton case; the baryon ansatz is the coset case. Both deliver an integer winding; the
two should not be conflated as "the same map into the same `S³`."

### C.1.4 The baryon as one defect with three orthogonal facets

A baryon is **one defect** with one circular winding in the Q-orbit, decomposed into three
orthogonal facets — the three Q-orbit trivectors `{e_{124}, e_{134}, e_{234}}` (R-053). The
"three quarks" are not three independently existing objects bound together by a force; they are
the three orthogonal-component decomposition of one circular winding, as §A.4 prepared. The
three-fold count is forced by the three orthogonal `e_4`-bearing trivector directions in
`Cl(4,0)`. The colour singlet `e_{124} · e_{134} · e_{234} = e_4` is the combined three-facet
circular winding pointing purely along the propagation axis `e_4` — the rest-mass direction
(§A.4's front-locked reading).

This is §A.3's ontological reading of confinement: a single quark in isolation is *not a
valid stable configuration of the rotor field* — it's not "an object held in by a force from
leaving the baryon", it's not the right shape to be a configuration at all. The three facets
must be present together because they *are* the one circular winding. (§C.5 returns to this for
the topological / formal-consequence reading.)

**Same-composition mass-difference test.** The three-facet structure predicts that two baryons
with the *same* quark composition can have different masses if the facet orientations differ. The
sign of the split follows from constructive vs. destructive interference of the facet
orientations. The framework predicts the signs structurally (magnitudes gated on §D.5):

| Pair | Composition | Predicted sign | Observed |
|---|---|---|---|
| Σ⁰ vs Λ | uds | `Σ⁰ > Λ` | ✓ (Σ⁰ − Λ ≈ 77 MeV) |
| Δ⁺ vs p | uud | `Δ⁺ > p` | ✓ (~294 MeV) |
| Σ*⁺ vs Σ⁺ | uus | `Σ*⁺ > Σ⁺` | ✓ (~193 MeV) |
| Ξ*⁰ vs Ξ⁰ | uss | `Ξ*⁰ > Ξ⁰` | ✓ (~217 MeV) |

Four pairs, four matching signs — the structural prediction passes. A theory of additive
quark-mass composition would predict no split at all and would fail this test. Magnitudes await
§D.5 closure.

### C.1.5 Proton stability

The proton is the `B = 1` Skyrmion, with `B ∈ π_3(SU(2)) = ℤ`. As an integer winding it cannot
continuously deform to vacuum without passing through higher energy, regardless of whether read
as a static defect or as a driven attractor (R-054). Proton stability is a topological theorem
in this framework, not a finely-tuned hierarchy of decay rates: there is no operator that lowers
the winding integer continuously, and the non-perturbative violation that the BPST instanton
supplies (R-088) respects `ΔB = ΔL = N_gen = 3` — the proton's `B = 1` cannot be reached by such
a process from any lower-`B` configuration. The empirical lower bound `τ_p > 1.6 × 10³⁴` years
(Super-K) is structurally consistent.

### C.1.6 The electron as Hopf defect; QCP scaling

The electron is the L-orbit lepton-sector defect — a Hopf-like soliton with Hopf invariant
`H = 1`, equivalent to a winding into `π_3(SU(2)_L)` via the Hopf fibration. Its existence as a
stable defect uses Derrick's theorem differently from the baryon case: the L-orbit's wrap
structure on `S¹` × `S²` requires no quartic stabilizer of the Skyrme type.

The electron's mass comes out of QCP (quantum critical point) scaling near the chirality balance
`D = J`. At leading order

> `f_L = f_π · (1 − D/J)^{9/2}`  (R-055).

At the empirical `D/J ≈ 0.79` this gives `f_L ≈ 0.115 MeV`, vs the empirical electron-mass-set
scale `m_e/e_L ≈ 0.0846 MeV`, where `e_L = √36.47 ≈ 6.04` is the L-orbit Skyrme-BVP eigenvalue
(the lepton-sector analog of §C.1.2's baryon coefficient, with `m_e = f_L · e_L`) — a
~36% match in `f_L` itself, equivalent to a ~4% match in the
exponent: solving `m_e/e_L = f_π · (1 − D/J)^{ν_emp}` for the empirical exponent gives
`ν_emp ≈ 4.696` (from `log(0.0846/129) / log(1 − 0.79)`), vs the predicted `9/2 = 4.5` — a
`(4.696 − 4.5)/4.5 ≈ 4.4%` mismatch in the exponent.

*The exponent `9/2` is itself derived* from D4 deconfined-quantum-critical-point (DQCP)
universality. The breakdown:

> `ν = N_dir · Δ_v · (1/2) · ν_corr = 3 · 3 · (1/2) · 1 = 9/2`,

with the four ingredients carrying four distinct statuses, stated honestly: `N_dir = 3` is the
number of independent L-orbit rotation directions (exact); `Δ_v = 3` is the engineering
dimension of the relevant order-parameter operator under L-orbit DQCP scaling — riding the
critical canting/magnon stiffness `K_c = (2/19) · J` at the chirality balance, whose kernel
form remains a located gap routed through §D.5; the factor `1/2` is a σ-model
kinetic-normalization **convention** (a counted convention choice, not a substrate derivation);
and `ν_corr = 1` is generic at the Gaussian fixed point. The other substrate input is
`N_Goldstone = 2` from `dim(SU(2)_L / U(1)_canting) = 2`, and the DQCP universality frame
itself is an imported many-body framework (companion Section 13). So **the 9/2 is a structural
counting within an imported universality class, not a fit to the empirical exponent** — but it
is conditional on the `K_c` ingredient and carries the normalization convention as a counted
choice. A separate empirical fit,
`ν = 3π/2 = 4.712`, matches the measured exponent to 0.34%, but no mechanism for that value is
identified — a candidate coincidence, not a derivation.
The L-orbit electron is one of the framework's mixed-tier results: structural ontology derived,
leading-order scaling derived at leading order (conditional on the `K_c` ingredient),
sub-percent precision empirically present but mechanism open.

---

## §C.2 — Charges and the first generation

The framework's second cleanest spine result lives here. Charge quantization is not assumed; it
is an algebraic identity in the substrate, with `|Q_p| = |Q_e|` tested to `< 10⁻²¹` empirically
(R-063). The whole construction — hypercharge, fractional quark charges, weak isospin, V−A, GMN
— follows from the Clifford spectrum plus one input bit (weak = SD).

### C.2.1 Hypercharge from the e_4-bilinear

A defect's hypercharge enters through the `e_4`-bilinear on its grade-3 blade. For
`B ∈ Cl_3(4,0)`, direct computation gives

> `B̃ · e_4 · B = (±1) · e_4`,

i.e. the bilinear maps each grade-3 blade onto `e_4` with a sign `±1` that depends on the blade
(R-056). The two cases are: Q-orbit trivectors (e.g. `B = e_{124}`) give `+e_4`; the L-orbit
trivector `e_{123}` gives `−e_4`. Reading the coefficient `±1` per blade and combining with the
doublet structure gives the per-blade hypercharge contribution. (A normalization note, kept
honest: the left-handed doublet values below follow from the bilinear signs plus doublet
constancy; the right-handed singlet values are the GMN-consistent assignments at `T_3 = 0` —
fixed by the blade spectrum plus the charge chain, not independently derived.)

Hypercharge `Y` is **constant across each SU(2)_L doublet** (forced by Schur's
lemma — `Y` must commute with the SU(2)_L generators). So both members of a doublet share `Y`:

- Left-handed lepton doublet `(ν_L, e_L)`: `Y = −1`.
- Left-handed quark doublet `(u_L, d_L)`: `Y = +1/3`.
- Right-handed singlets: `Y_{e_R} = −2`, `Y_{u_R} = +4/3`, `Y_{d_R} = −2/3`.

The standard `Q = T_3 + Y/2` then gives the empirical electric charges, since `T_3 = ±1/2` within
each doublet and `T_3 = 0` for singlets. All values follow from the `e_4`-bilinear plus the
doublet structure of §B.3.

### C.2.2 Fractional quark charges from three-quark blade structure

The Q-orbit trivectors `{e_{124}, e_{134}, e_{234}}` satisfy

> `e_{124} · e_{134} · e_{234} = e_4`  (the colour singlet),

so a configuration that decomposes into three such facets carries one third of the integer
charge per facet. The fractional charges `±2/3, ±1/3` follow algebraically from this trivector
triple-product structure plus the per-blade hypercharge eigenvalues of §C.2.1 (R-057). No
fractional-charge value outside the `{±1/3, ±2/3, ±1}` spectrum is reachable in the algebra —
this is canonical falsifier §E.3 row 13.

### C.2.3 Weak isospin from the meta-time rotor doublet

A massive defect's meta-time rotor `q_h(τ_5) = exp(m τ_5 û/2)` (§A.4; `m = ω`) splits into two
half-amplitude components — `sin(ω τ_5/2)` and `cos(ω τ_5/2)` — that transform as a doublet
under `SU(2)` rotations of the rotor axis. This is the **weak isospin doublet** (R-058).
*(An honest-scope note: with R-127's lock, a rotation of the rotor axis within
the L-orbit span is generated by the spin su(2) and reads as precession — the standing
don't-conflate hazard. Which su(2) performs the doublet rotation here — the weak SD factor vs
the spin L-orbit factor — is left unspecified by this passage and needs an explicit
identification; the cos/sin doublet components themselves are unaffected.)* The
charged-current vertex `W^+: cos → sin (e^− → ν_e)` and `W^−: sin → cos` is read directly off
the rotor's doublet structure. No further machinery is required.

### C.2.4 Lepton-quark weak universality

The weak couplings to lepton and quark sectors are identical because both sectors carry the
same meta-time rotor doublet structure (R-059). The proof is algebraic: both lepton and quark
blades transform under the same `SU(2)` action on the `S_+` chiral half of the spinor module.
This is a theorem, not a coincidence requiring tuning.

### C.2.5 V−A from SD's half-module kernel

Weak isospin is the chiral Spin(4) factor SD = `su(2)_+` (R-079, established at §C.4). On the
4-component spinor module SD has a **half-module kernel**: it acts non-trivially on exactly one
Weyl chirality, trivially on the other. So a `W` boson can only couple to one chirality (R-060) —
the **V−A** structure. Given the weak=SD input, V−A is derived, not stipulated.

### C.2.6 Generation-blindness and no tree-level FCNC

SD is the unique centralizer of the ASD generation triple. Acting on a generation-eigenstate
basis, SD treats all three generations identically: the weak vertex carries no off-diagonal
generation matrix element (R-061). This is the **no tree-level FCNC** result. It is also a
consequence of the weak=SD input bit, and is canonical falsifier §E.3 row 17.

### C.2.7 GMN as algebraic identity (anti-circularity restored)

The Gell-Mann–Nishijima relation

> `Q = T_3 + c · Y`  (R-062)

is a derived algebraic identity in the substrate, **with `c = 1/2` returned non-circularly**. The
non-circularity matters: a derivation that defines `Y := 2(Q − T_3)` would make `Q = T_3 + Y/2`
a tautology. The relation's three ingredients are independently determined:

- **Q** is fixed independently of GMN by the **topological-winding chain** (§C.5.1 / R-054 /
  §C.1.5): `π_3(SU(2))` supplies integer-valuedness (`B ∈ ℤ`). The specific anchor `Q_p = +1`,
  `Q_n = 0` need not be imported: given two structural premises — **(P4)** measured electric
  charge is the eigenvalue of *one* universal linear generator `Q = T_3 + c·Y` across all
  sectors, and **(P5)** `Q` is chirality-independent per defect — the proton–electron relation
  follows for *every* `c` (R-159, below), so the neutrality-of-atoms datum this anchor used to
  consume is **conditionally replaced** rather than imported. Either way it enters no GMN step,
  so the `c = 1/2` check below stays non-circular.
- **T_3** is fixed independently by the **meta-time rotor doublet** (R-058 / §C.2.3): the
  rotor's `SU(2)_+` generator with eigenvalues `±1/2` on each doublet member.
- **Y** is fixed independently by the **`e_4`-bilinear** (R-056 / §C.2.1).

With these three independent determinations, the relation `Q = T_3 + c · Y` must hold for some
`c` on every blade. **The lepton doublet alone determines `c`** gate-free: `(ν_L: Q = 0,
T_3 = +1/2; e_L: Q = −1, T_3 = −1/2)` with `Y_L = −1` from the e_4-bilinear gives
`Q = T_3 − 1/2 = T_3 + (1/2)·Y` on both members. So `c = 1/2`, fixed by the lepton doublet alone
without any quark content or facet structure. The remaining 13 Weyl states of the first
generation then return `c = 1/2` consistently — non-trivially for the left-handed quark doublet
(whose `Q` comes from the facet composition and whose `Y` from the blade bilinear),
definitionally for the right-handed singlets (whose `Y` normalization is fixed at `T_3 = 0`,
§C.2.1). This consistency, with `c` pinned by the lepton doublet alone, is **the derived
content** — the relation `Q = T_3 + Y/2` is not a definition; on the doublet sector it is a
non-trivial Clifford identity returning the same coefficient on every blade.

**The proton–electron relation needs no anchor at all (R-159).** The determination above runs
from independently-fixed charges to `c`. Running it the other way is stronger. Take the
functional *form* `Q = T_3 + c·Y` as structural (P4) with `c` left free, take `Q`
chirality-independent per defect (P5), and identify the proton with the three-facet composite
`uud` (P6 — an inside-frame state identification, the canon-legitimate use of the inside view).
Then

> `Q_p + Q_e = [2T_3(u) + T_3(d) + T_3(e)] + c·[3Y_Q + Y_lep] = 0 + c·0 = 0`

**identically in `c`.** Both brackets vanish separately, and each is already derived: the `T_3`
bracket because `uud + e` is one complete quark doublet plus an up-versus-down-opposed pair
(R-058, given the counted weak = SD bit); the hypercharge bracket because `3Y_Q + Y_lep = 0` is
exactly the `3 × 1/3 = 1` arithmetic of §C.5.4 — the `e_4`-bilinear's sign opposition between
the orbits (R-056) combined with the trivector triple-product `/3` (R-057). The same
computation returns `Q_n + Q_ν = 0` identically, and singles `uud` out uniquely: of the four
three-facet composites only `uud` lands at `−Q_e` (`uuu`, `udd`, `ddd` give `+1`, `−1`, `−2`
relative to the electron), which also dissolves the apparent circularity in §C.3.13's
side-assignment. The result is substrate-specific rather than generic — delete the `/3` and the
residue is `2c ≠ 0`.

So **hydrogen neutrality is a theorem of the framework given (P4, P5, P6)**, not a datum it
consumes, and the `10⁻²¹` measurement changes role from calibrating the anchor to *testing*
those premises. Honest scope: P4 and P5 are structural premises, not closed Clifford
identities. P4's support is the single-photon L↔Q bridge (R-035) together with the
unbroken-combination reading of §C.5.3a — the latter a structural identification rather than
an engine-checked result; a demonstration that the two orbits could carry *different*
normalizations would revert this section to the empirical anchor.

The normalization `c = 1/2` — needed for the *individual* values (`Q_n = 0`, the quark charges,
the right-handed hypercharges), not for the relation above — is fixed natively and corroborated
twice. Natively: the sterile partner `S_−` is wave-decoupled (§C.3.12) and so carries no charge
of the wave-sector gauge field, while the Dirac pairing forced by exact `B − L` conservation
(§C.5.4–§C.5.6) makes `(ν_L, S_−)` one defect, so P5 gives `Q(ν_L) = 0`, i.e. `1/2 − c = 0`.
(The step "wave-decoupled ⇒ `Y(S_−) = 0`" is an inference from the EM-as-wave-mode
identification, not a computation — named here as this route's own residual.) Independently,
two anomaly-cancellation conditions on the one-generation spectrum — the mixed gravitational
condition and the cubic `[U(1)_Y]³` — each force `c = 1/2` alone, and the same system forces
the right-handed hypercharges `Y_{e_R} = −2` and `{Y_{u_R}, Y_{d_R}} = {4/3, −2/3}`; these
ride an imported anomaly package (companion Section 13) and are labeled as such, with a third,
condensate-based check downstream of them.

### C.2.8 Charge quantization to 10⁻²¹

Combining §C.2.1–§C.2.7, the complete 15-Weyl spectrum of the first generation has charges in
`{0, ±1/3, ±2/3, ±1}` exactly — a **discreteness/commensurability theorem**: every reachable
charge is an exact rational multiple of `Q_e`, so the proton–electron equality

> `|Q_p| = |Q_e|`  (empirically tested to `< 10⁻²¹`)  (R-063, R-159)

is topologically **protected** against drift rather than tuned — there is no continuous
parameter available for the two charges to differ by — and its absolute *normalization*
(`Q_p = −Q_e` exactly, rather than some other commensurate value) is a **theorem given the
structural premises (P4, P5, P6)** of §C.2.7, holding identically in the normalization constant
`c` (R-159). The framework no longer consumes the neutrality-of-atoms datum here; it predicts
it. Together with the Lorentzian signature emergence of §B.1, **charge quantization is one of
the framework's two cleanest spine results** — the discreteness by exact algebra, the
proton–electron equality conditional on two named structural premises rather than on an
empirical anchor. Two of the most foundational features of relativistic physics — the signature
of spacetime and the conserved discrete charge spectrum — fall out of the substrate algebra.

---

## §C.3 — Three generations, Koide, neutrinos

This section carries the framework's mixed-tier content. The structural derivations (three-count
from Frobenius, Koide form `K = 2/3 ⇔ c = √2`, Foot 45° characterization, forced-left-handed
neutrino, single-Weyl lightness) are clean. The lepton-mass-ratio values currently sit at FIT
tier rather than forward-derived — the cross-sector D/J over-determination is a real coherence
signal but not a forward derivation. The Result Index (companion Section 1) keeps the
distinction crisp.

### C.3.1 The Z_3 of V_4-perp; the Brannen amplitude form

The generation circle lives on a Z_3-symmetric reduction of the meta-time rotor's phase space.
The three generations are identified with the three imaginary units of `ℍ` on the `V_4⊥`
generation circle (`V_4⊥` = the orthogonal complement of `e_4`; its associated bivector ASD
triple carries the three `ℍ` units). Projecting
the meta-time circle onto `V_4⊥` gives the Brannen amplitude form

> `A_k(c, δ) = 1 + c · cos(δ − 2πk/3)`  (R-064)

for `k ∈ {0, 1, 2}`, with `δ` the Brannen phase (the `δ_L` of §C.3.5) and `c` the
projection-geometry coefficient. The form follows from the
projection geometry; the `c` value remains an input.

### C.3.2 The √2 factor

The projection geometry of the 3D Euclidean meta-time circle onto a 2D `V_4⊥` slice carries a
natural normalization

> `c = √2`  (R-065),

the value the metric ratio of the projection would assign. This is **equivalent to the INPUT
`K = 2/3`** of §C.3.3 (Brannen–Koide equivalence theorem): the `√2` is what the geometric reading
of the lepton sector commits to *if* `K = 2/3` is the framework's empirical input — and given
the empirical input, the geometry returns the matching `√2`. The √2 is therefore not an
*independent* derived constant — it is the same INPUT bit as `K = 2/3`, seen through the
projection's geometric lens. (Six independent forcing routes for `K = 2/3` have all been
investigated and returned negative — companion, R-065/R-066 rows; the equivalence theorem
propagates that result to `c = √2` and to the
`Σ T_3·Y = 0` cross-term value, neither of which is independently forced.)

The Brannen amplitude is therefore `A_k = 1 + √2 · cos(...)`.

### C.3.3 Koide K = 2/3 ⇔ c = √2 — the Brannen-Koide equivalence

The Koide mass identity

> `K := (m_e + m_μ + m_τ) / (√m_e + √m_μ + √m_τ)² = 2/3`

is empirically exact to 10⁻⁵. The Brannen-Koide equivalence theorem (R-066) states

> `K = 2/3 ⇔ c = √2` for the Brannen amplitude.

So K = 2/3 has a geometric reading: it is the empirical signature of the √2 projection geometry.
The value `K = 2/3` itself is INPUT (exact-but-unforced, §C.3.2). What the framework derives
is the *form* `K = 2/3` carries
— the equivalence with c = √2 and the Foot 45° characterization that follows.

### C.3.4 Foot 45° signature-free characterization

Equivalently, K = 2/3 is the condition that the Foot angle `θ(m_e, m_μ, m_τ) = 45°`. The Foot
angle is the angle between the vector `(√m_e, √m_μ, √m_τ)` and the diagonal `(1, 1, 1)` in ℝ³,
given by

> `cos θ = (√m_e + √m_μ + √m_τ) / √(3 · (m_e + m_μ + m_τ))`  (Foot 1994; R-067).

Plugging in the measured charged-lepton masses gives `θ = 45.000° ± 0.001°` — strikingly exact.
The equivalence `K = 2/3 ⇔ θ = 45°` is immediate: `K = 1 / (3 cos²θ)`, so `K = 2/3` requires
`cos²θ = 1/2`, i.e. `θ = 45°`. This characterization is signature-free (it doesn't depend on
which sign convention is used for the square roots) and is independent of the Brannen projection
geometry. So three independent characterizations — K = 2/3, c = √2, Foot 45° — coincide; that
coincidence is itself a derived theorem.

### C.3.5 Three lepton mass ratios at δ_L = 12.73°

The direction of derivation is: fit the three Brannen amplitudes to the three measured
charged-lepton masses; this is a one-parameter fit in `δ_L`, and it lands on `δ_L = 12.73°` with
< 0.01% residual (R-068). The substrate relation `δ_L = (1/3) · arctan(D/J)` then *infers*
`D/J ≈ 0.79` from the fitted `δ_L`. So the data goes: lepton masses → `δ_L` (the Brannen
phase) → `D/J` (the substrate chirality ratio). The cross-sector consistency check (§C.3.11)
then validates the `D/J ≈ 0.79` against an independent baryon-side back-derivation. This is
the framework's tightest empirical fit. **Honest scope:** the forward derivation
`L-orbit τ = 0 → lepton ε = 0`
was attempted and *refuted at the bridge gaps*; the lepton-mass triplet currently sits at FIT
tier, not derived-forward. It is a fruitful, sub-percent fit cross-validated by the Koide form,
not a derivation. The structural result (Koide form, Foot 45°) survives; the magnitude triple
is a fit until the substrate forward derivation lands.

### C.3.6 The D = J ⇔ δ_L = π/12 ⇔ m_e = 0 identity

At the chirality balance `D = J`, `δ_L = π/12 = 15°` and the electron mass goes to zero at
leading order (R-069). This is a substrate-side structural identity: at the critical chirality
ratio the lightest lepton is massless. The empirical `D/J ≈ 0.79` (vs the critical `D/J = 1`)
puts the framework near, but not at, the critical balance — which is what generates the
hierarchy `m_e ≪ m_μ < m_τ`. The hierarchy is structural; its magnitude scaling is the QCP
result of §C.1.6.

### C.3.7 δ_L from the chiral Z_3 potential

The form of `δ_L(D/J)` follows from a chiral Z_3 potential built from `J` (kinetic) and `D`
(chirality-breaking) couplings on the substrate (R-070). The *form* is DERIVED; the coefficient
identification `A = J, B = D` (which fixes the absolute calibration) is an asserted ansatz at
the dressed-coupling level, not a substrate forward derivation. Honest scope flagged in the
result row.

### C.3.8 Three generations from Frobenius

Why exactly three generations? The generation circle is identified with the three imaginary
units of `ℍ` on `V_4⊥`. Frobenius's theorem states that the only finite-dimensional associative
real division algebras are `ℝ`, `ℂ`, `ℍ` — three imaginary units in the largest. A hypothetical
fourth generation would require a fourth imaginary unit — an associative real division algebra
beyond `ℍ` — which by Frobenius does not exist (R-071). The no-fourth-generation prediction is
therefore not a tuning of mass scales; it is a structural forbiddance from the algebra.
Canonical falsifier §E.3 row 15.

The result is LOCATED-conditional: the orbit-phase → ℍ-unit identification is a structural
mapping that is asserted rather than derived from substrate dynamics. So "three generations from
Frobenius" is a structural derivation **given** the identification; the identification is the
residual gap, flagged in the result's companion row.

### C.3.9 G is the colour Z_3, not the generation Z_3

The spatial generator `G` is the **colour** `Z_3`, not the
generation `Z_3` (R-072). The generation `Z_3` is the meta-time phase advance — a different
algebraic object. The colour `Z_3` is the cyclic interchange of the three Q-orbit trivectors
`{e_{124}, e_{134}, e_{234}}`, and it is the proper spatial 120° rotation about the (1,1,1) axis
in `span{e_1, e_2, e_3}`. This separation matters in §C.4 (colour-sector construction).

### C.3.10 Cabibbo as frequency ratio

The CKM matrix element `V_us` admits a candidate identification

> `|V_us|² = m_d / m_s ≈ 0.05`  (R-073),

with the empirical ratio `m_d/m_s ≈ 0.0500` (PDG `4.67/93.4`) matching the empirical
`|V_us|² ≈ 0.0503` at ~0.6% (§E.3 row 16). This is the
quark sector's Brannen-with-epicycle reading: the deviation from the lepton-sector circular
projection is encoded as an eccentricity `ε ≠ 0` on a generalized Brannen ellipse, and the
Cabibbo angle reads as the frequency ratio between the two leading mass eigenvalues. The
relation is structurally testable for `|V_us|² = m_d/m_s` (the d–s ratio); the analogous
prediction for `m_t` is structurally untestable because no top hadrons exist (R-091a; §C.5). The
identification stands as a CANDIDATE pending the Θ_rel closure.

The up-sector eccentricity itself carries a candidate rule inherited from the quark-sector
epicycle parametrization: `ε_u/ε_d = 2^{3/2} ≈ 2.828`, heuristically motivated as the spinor
half-angle structure times the up-vs-down chirality flip. In that parametrization `ε_u` is *set
by* the rule (`ε_u = ε_d · 2^{3/2} = 0.973` from the fitted `ε_d = 0.344`), so the ratio
realizes the rule by construction rather than testing it; and the rule is untestable on the
framework's own terms: only `u, c` are hadron-indicated, and `m_t` is a Standard-Model
bookkeeping number (no top hadrons, §C.5.9), so it cannot be falsified against the top. It
stands as a counted fit recorded in the companion registry, not a numbered result; §A.4's
forward reference resolves here.

### C.3.11 Cross-sector D/J — the over-determination

The lepton sector calibrates `D/J ≈ 0.787` via Brannen `δ_L = 12.73°`. Independently, the baryon
sector reads `D/J = √18 / e ≈ 0.779` from the Skyrme stabilizer with the ANW-historical
`e ≈ 5.45` (matching `f_π = 129 MeV`) (R-074). The two values agree to
~1.1%. This is the framework's **genuine cross-sector over-determination signal** — two
independently-calibrated sector fits convergent on the same value to within 1%, with no
adjustable parameter between them. The structural meaning is that the same chirality ratio
parameterizes both leptonic and baryonic phenomenology, as the framework requires; the
quantitative ~1% agreement is empirically positive but not yet a forward derivation.

*(Side note on the geometric coincidence. The baryon-side back-derivation rides on
`e ≈ √18/(D/J)`, where the √18 itself rides a geometric coincidence whose physical referent the
framework itself disclaims. The cross-sector agreement is
honest; the chain has one acknowledged geometric coincidence at the relating link.)*

**A second cross-sector convergence, recorded as a candidate (R-134).** The Brannen lepton scale
`μ = (√m_e + √m_μ + √m_τ)/3` satisfies `μ² = 313.84 MeV` against the nucleon's per-rotor share
`m_N/3 = 312.97 MeV` — a **0.28% zero-parameter convergence** between two measured quantities
(in the framework's own `√m` measure — the *same single convergence*, the square root halving
the deviation identically: `√(m_N/3) = 17.691` vs `μ = 17.716 MeV^{1/2}`, 0.14% — the baryon's
per-rotor amplitude sits at the lepton tower's *democratic component*, the generation-blind
`μ·1` term whose `√2·cosθ` ℤ₃ offsets average to zero).

The observation is long known informally in the Koide-formula literature; the framework's
contribution is the legal reading — `m_N/3` is *not* a quark mass (§A.4's mass-scope rule
holds) but the mean per-rotor frequency of the `Ω_B = Σω` baryon lock (itself conditional on
the E-channel composition premise) — and the honest constraint map: the naive derivation route
through the `I₄` map is *blocked* (the Hodge map is amplitude-blind), so any mechanism must
live at the shared cell-scale/kernel layer; and the *floor* reading of the lock
(`M₀/3 = 287.7`) does **not** converge (~9%), making this convergence a stakeholder in the
open frequency-sum-vs-full-mass fork.

If a mechanism ever pins the per-rotor lock frequency to the lepton democratic component,
`m_N = 3μ²` would co-derive the nucleon mass from the lepton tower with zero hadronic input —
one fewer counted dial. Until then: a recorded candidate over-determination row, with the
post-hoc/look-elsewhere caveat carried.

### C.3.12 Neutrino forced left-handed; single Weyl; lightness

The neutrino's handedness is fixed by the framework's one weak-sector input bit — the same
linked binary choice as `weak = SD`, counted once (§C.4.2's honest-scope note: the substrate
chiral coupling structure that selects the handedness *is* the SD-vs-ASD selection). Given that
bit, the `+e_4` propagation direction (R-043) forces the neutrino into a single Weyl ideal of
the spinor module: only the left-handed Weyl is wave-coupled (R-075). The right-handed partner
sits in the `S_-` mode that is wave-decoupled — sterile.

Neutrino lightness then follows from the single-Weyl structure (R-076). A two-Weyl Dirac
fermion's mass term mixes the two chiral halves; a single Weyl with a sterile partner has only
the Dirac-mass overlap as the mass-generating channel, and the overlap is set by the
active-sterile bridge — a small parameter. The full overlap computation is gated on Θ_rel /
substrate dynamics; what the structure gives is *why* neutrinos are light without tuning.

### C.3.13 Up/down mirror — SD ↔ ASD under parity; up = SD

The SD and ASD chiral factors of `Spin(4)` are exchanged under spatial parity. Under §A.3's
matter-as-defect ontology, this exchange is the **up/down mirror**: the up-sector is the SD
chirality realization of the framework's weak coupling, and the down-sector is the ASD
realization (R-077). The identification "up = SD" reads `Q_u = +2/3, Q_d = −1/3` charge
assignments correctly via the per-blade hypercharge eigenvalues. The mirror is a structural fact
of the algebra; the side-assignment (which is up, which is down) is fixed by the charge
opposition to the lepton sector. *(R-128, §B.3.1: the quark
sector's mass-phase lock is the parity-odd Hodge-dual map, giving each Q-orbit defect a ℤ₂
orientation label that parity flips — the static seat of this two-element orbit inside a single
defect's frame — while the lepton lock is parity-even (no label, no doubling). The two species
are statically degenerate; the splitting remains the `⟨I₄⟩`/µΨ₀ dial, which R-128 shows enters
through the quark lock and not the lepton lock.)* *(R-152:
the §D.4.4 ρ_L boundary integral — R-129's standing candidate seat — computed
on the Q-orbit baryon profiles. The literal scalar
`ρ_L = ⟨Ω³⟩₀` vanishes identically on Q-orbit matter (`e₁₄e₂₄e₃₄ = −I₄` ⇒ the Q-orbit winding
density is parity-odd / I₄-valued; physically a baryon has `B ≠ 0` but `L = 0`) — a clean negative
confirming ρ_L is intrinsically the L-orbit winding. But the R-128 parity-odd Hodge dual `I₄·Ω`
recovers the scalar L-winding exactly, deriving the corrected seat *form* `L_θ = µΨ₀·B_Q` — parity-odd,
linear in the integrated baryon winding. The algebraic recovery is exact; the physical seat
remains a structural identification, the value µΨ₀ stays #1-gap gated, and this form does not
fix the inter-generation running.)*

**Exactly two quark types, no third.** The up/down mirror is a binary structural fact —
SD ↔ ASD under parity is a two-element orbit. There is no third quark type beyond up/down at the
substrate level; what the SM calls heavier-generation up-type (c, t) and down-type (b, s) are the
*same* SD / ASD assignments at higher generation index. So the count across the three
generations is **two quark types × three colours × three generations = 18 quark species**, plus
the lepton sector's `2 × 1 × 3 = 6` lepton species (with `2` = ν and e) — the SM's familiar 24
fermion species in total, forced by the mirror's binary structure plus the colour count plus
three generations. (Counting chiralities, each generation carries exactly the 15-Weyl spectrum
of §C.2.8 — 16 with the sterile `S_-` partner of §C.3.12.)

**ν/e mirror cross-check — two predictions from one mechanism.** The same mirror structure that
gives up/down on the quark side gives ν/e on the lepton side — but the lepton mirror is broken
by electromagnetism. EM acts on the L-orbit (R-035), and charged leptons couple to it with both
chiralities (Dirac mass needs both halves), while the neutral neutrino remains single-Weyl
(§C.3.12). So:

- **Quark sector**: up/down mirror unbroken at tree level (no electromagnetic distinction; both
  participate in QCD identically modulo charge).
- **Lepton sector**: ν/e mirror broken by EM (the charged member doubles to two chiralities; the
  neutral stays single).

**Two predictions from one mechanism** — the unbroken quark mirror and the EM-broken lepton
mirror are forced by the *same* SD ↔ ASD parity structure interacting with the *charge-bearing*
L-orbit field. Empirically: the proton-neutron mass split is small (mirror nearly intact); the
charged-lepton mass spectrum has no neutrino counterpart (mirror fully broken). The two facts
agree with the mechanism.

---

## §C.4 — The gauge group from D4 orbits

This is the framework's headline derivation: **`sin²θ_W = 3/8` at unification, with no GUT
embedding, on the framework's counted inputs** (R-082). The route is short — three native ingredients
plus a proven `g_1 = g_2` — and the result it delivers is one of the framework's most directly
testable structural claims against the SM.

### C.4.1 Substrate carriers of SM gauge content

The D4 orbit structure carries four substrate-distinct sectors matching the SM's gauge content
(R-078):

- **Self-dual bivector algebra SD = `su(2)_+`** → the **weak sector** (one of two `Spin(4)`
  factors, the chiral one). Distinct from the L-orbit `𝓛` (which is the spin algebra, §A.5.2).
- **Q-orbit trivectors `{e_{124}, e_{134}, e_{234}}`** → host the **quark colour content** (the
  three colours = the three trivectors). Internal Z_3 interchange is the colour cyclic group.
- **I_4 central direction + bivector gauge field** → the **hypercharge sector**.
- **e_4-bearing bonds (12 of 24)** → the **L ↔ Q transition channels** (no physical X, Y bosons).

The total D4 generator count is `12 + 12 = 24` (the D4 kissing number); see R-083 for the
historical SU(5) translation.

### C.4.2 Weak = SD chiral Spin(4) factor (the one INPUT bit)

The **weak isospin gauge group is the self-dual bivector algebra**

> `SD = span{e_{12} − e_{34}, e_{13} + e_{24}, e_{14} − e_{23}} = su(2)_+`  (R-079),

one of the two factors of `Spin(4) = SU(2)_+ × SU(2)_−` — the `I_4 = +1` (self-dual / chiral)
one.

*Why not the L-orbit?* The L-orbit `𝓛` *is* the spin algebra (§A.5.2). A weak interaction built
on it would be **parity-even** (vector) — it would couple both chiralities and require a
right-handed neutrino to interact. SD has a **half-module kernel** (acts on one Weyl factor only);
the L-orbit has **zero kernel** (acts on both). So a left-handed, single-Weyl neutrino is
compatible with weak = SD but excludes weak = L-orbit.

**An honest scope note on what's input and what's derived.** The pair
**{weak gauge = SD}** and **{neutrino is left-handed}** is **one linked binary choice**: given the
chiral-factor structure of Spin(4), the framework's single-Weyl neutrino must be coupled to the
chiral factor that hosts the weak gauge force, and *which* chiral factor (SD vs ASD) is "the
weak one" is identical to *which* chirality (LH vs RH) the neutrino lives in. The pair is one
binary bit, counted once: the chiral coupling structure of the substrate that
forces the neutrino's handedness (R-075) *is* the SD-vs-ASD selection, so the two are not
independent and the accounting books them as one. The framework picks the SD branch of this linked binary
as the INPUT (equivalently, picks LH as the neutrino handedness); everything else in the weak
sector (V−A, generation-blindness, doublet structure, up = SD) is DERIVED-given-it (R-060,
R-061, R-077).

### C.4.3 U(1)_Y from I_4 + bivector compactness

The hypercharge gauge field `B_μ` corresponds to the `I_4` direction. But `I_4² = +1` is
non-compact (it generates `cosh + I_4 sinh`, hyperbolic), so `I_4` itself cannot be the gauge
generator — gauge fields must be compact (`exp(2π i T_Y) = 𝟙` at integer charges).

The compact alternative is the **bivector algebra**. In `Cl(4,0)`, bivectors square to `−1`
(closure as `so(4)`), so they generate compact `U(1)` rotations. The hypercharge gauge field is
therefore **bivector-generated**, with `I_4` labeling the conserved-charge direction only
(R-080). This makes both electroweak factors bivector-generated — which is the structural input
to §C.4.5's `g_1 = g_2`.

### C.4.4 The colour octet — 8 = 3 ⊕ 5

The colour sector is carried by the three Q-orbit trivectors. The cyclic Z_3 interchange of the
trivectors is the discrete center. The full `su(3)` algebra is constructed via the gluon octet
split

> `8 = 3 ⊕ 5`  (R-081, the exact symmetric-space decomposition),

with the **L = 1 triplet** the L-orbit bivector rotations (the Cl-native `so(3)` triplet) and
the **L = 2 quintet** the `SU(3)/SO(3)` coset complement.

*Consistency check (not an independent prediction).* Once the construction `8 = 3 ⊕ 5` lands on
`su(3)`, the ratio of colour Casimirs

> `C_A / C_F = 9/4 = 2.25`

is forced by pure representation theory, and matches the empirical LEP value `2.27 ± 0.06`. The
match is **a consistency check** that the framework's elastic-response octet is `su(3)` as a
static algebra — not an independent quantitative output the way `sin²θ_W = 3/8` is (the
U(3)→SU(3) restriction and all colour dynamics remain gated, §C.5.2). A subtly
different colour algebra would have given a different Casimir ratio; the framework's algebra
gives the empirically correct one.

**Ontology preserved.** There is no fundamental spin-1 colour gauge boson in TWT (R-085). The
octet is an elastic-response algebra — 3 geometric L-rotations + a spin-2 strain quintet — not
eight gauge bosons. The colour force is identified with the dynamical coset-5 = the §D.5
defect-vacuum kernel; asymptotic-freedom `β_3 < 0` is a Layer-3 deep gate (§E.2). The static
algebra is exact; the dynamical running is open.

### C.4.5 sin²θ_W = 3/8 — the headline derivation

The electroweak mixing angle is

> `sin²θ_W = g_1² / (g_1² + g_2²)`,

depending on the U(1)_Y and SU(2)_L couplings only (never on the colour coupling). Three native
ingredients deliver the result:

**(i) Native charges.** Summing over one full generation in the all-left-handed convention:

> `Σ T_3² = 2`,  `Σ Q² = 16/3`,

from the per-blade hypercharge eigenvalues (R-056) plus the trivector triple-product structure
(R-057) plus the GMN identity (R-062) plus the complete 15-Weyl spectrum (§C.2.8).

**(ii) The cross-term vanishes.** The cross-term in `Σ Q² = Σ T_3² + Σ(Y/2)² + Σ T_3 · Y`
satisfies

> `Σ T_3 · Y = 0`.

*Honest scope.* This vanishing is **automatic** in any `SU(2)_L × U(1)_Y` theory with doublets
and singlets: `Y` is constant across each doublet by Schur's lemma (it must commute with the
`SU(2)_L` generators), and `T_3 = ±1/2` sums to zero within each doublet. The vanilla Standard
Model satisfies this without any bivector content. What the framework's L⊥Q orthogonality
(R-009) supplies here is the **Cl-native expression** of the cross-term vanishing — not new
information about the sum. The structural role of this step is to make `Σ Q² = Σ T_3² + Σ(Y/2)²`
compute cleanly without cross-term contamination; the vanishing itself is generic.

**(iii) Native √(3/5) via the Clifford trace bridge.** The bridge `Tr_𝒮(X) = dim(𝒮) · ⟨X⟩_0`
identifies the Clifford grade-0 norm on the spinor module with the rep-trace, giving

> `c² = Σ T_3² / Σ(Y/2)² = 3/5`,  so  `Y_native = √(3/5) · Y_SM`.

This is the *same* `√(3/5)` factor the GUT literature derives from the SU(5) embedding —
delivered here by Clifford grade structure, not by foreign Lie-algebra import.

**Plus `g_1 = g_2` from D4 isotropy.** Both electroweak factors are bivector-generated (§C.4.2,
§C.4.3), so both stiffnesses are set by the *same* dim-4 D4 elastic form. The dim-4 D4 isotropy
theorem — the same theorem that protects emergent Lorentz invariance in §B.1.4 and §B.6.3 —
gives all bivector planes one stiffness coefficient. `g_1 = g_2` is therefore exactly as solid as
the emergent-Lorentz protection: one theorem, two jobs.

Combining:

> **`sin²θ_W = Σ T_3² / Σ Q² = 2 / (16/3) = 3/8 = 0.375`**  (R-082).

No SU(5) embedding, no unifying group, no foreign Lie-algebra import. The result is the GUT-scale
value; running to `M_Z` via standard one-loop RG gives `sin²θ_W(M_Z) ≈ 0.231`, matching the
empirical `0.2312` — but the run-down is imported, not derived.

### C.4.6 The gauge-sector gate — SU(2)₊ gaugeable, required, realized, populated

A structural question precedes §C.4.5's calculation: *can* the weak SU(2)₊ be consistently
gauged on the substrate at all? Four sub-questions, all settled:

**(i) Gaugeable — Witten global-anomaly cancellation.** SU(2) carries a global anomaly under
`π_4(SU(2)) = ℤ_2`: an odd number of left-handed Weyl doublets would render SU(2)_L
non-gaugeable. TWT has **4 left-handed doublets per generation** (lepton + 3-colour quark) =
even, so the global anomaly cancels per generation. Three generations preserve this. Gaugeable.

**(ii) Required — the DM-twist non-commutativity and the explicit plaquette (R-140).**
With *rotor-only* lattice links the plaquette would telescope to identity (`F = 0`); the
would-be gauge field would be pure-gauge. The Dzyaloshinskii–Moriya bond bivectors break this:
**48 of 66 e₄-bearing D4 bond-pair commutators are
non-zero** (convention-robust) — and the plaquette holonomy itself is computed
explicitly (R-140): the minimal curvature-carrying loops of the
D4 root lattice are its 32 triangles (8 spatial, holonomy trivial; 24 with two `e₄`-bonds,
**all non-trivial**, with the exact law `W = cos²θ_D + sinθ_D cosθ_D(B̂₁+B̂₂) + sin²θ_D·e_ab`
in the canonical lattice frame — the conjugation-invariant content being the rotation angle
`arccos(cos²θ_D)` and the non-triviality; the 36 chordless 4-cycles all carry trivial
holonomy). Consistency of the loop product forces the orientation-*odd* refinement of the
bond-bivector convention — precisely the physical DM antisymmetry `D_ij = −D_ji`. The
holonomy's Lie closure is **full su(2) in each chiral sector** (rank 3, not reducible to any
`U(1)`), so the `π₃(U(1)) = 0` obstruction to instanton sectors is absent — `ℤ` sectors exist
at the structure-group level, and the instanton sector is **explicitly populated
at the configuration level** (R-143; (iv) below). Gauge degrees of freedom are required, and the
pure-gauge lift is now explicit.

**(iii) Realized — DM-induced field strength, with one honest qualifier (R-140).** The
plaquette of DM-twisted bond bivectors gives a non-trivial `F ≠ 0` — explicitly, per (ii). The
R-140 computation adds a constraint carried honestly: the plaquette drives **both** chiral
sectors with identical strength (`W = W₊P₊ + W₋P₋` with equal angles — the DM plaquette is
chirally blind), so the *substrate lattice* delivers `Spin(4) = SU(2)₊ × SU(2)₋` curvature
symmetrically, and the **SU(2)₊ restriction comes from the matter/SD coupling — the
"weak = SD" INPUT bit (§C.4.2) — not from the plaquette** (the menu-vs-pick pattern: the plaquette is
the symmetric menu; SD is the counted pick). The `Im χ`-mediated dynamics delivering the
Yang-Mills sector at the dressed-coupling level and the full Yang-Mills construction remain
Paper-2 work; the explicit finite-action instanton is established at the structural level
(R-143, (iv) below; R-088 covers the index-theorem ΔB = ΔL = N_gen part, whose rate face
stays gated). The remaining question — the induced level on the `B = 1`
worldline — is answered at the *parity* level (R-141): the level is ODD (3 per generation from
the derived roster; the parity is fork-robust), so fermionic Skyrmion quantization is induced,
conditional on the named premises (the imported induced-term theorem + the lock-channel
identification P1b, whose structural half is now exact algebra — R-161, §B.3.5 — leaving the
dynamical half P1b-DYN); the substrate *computation* of the term remains open.

**(iv) Populated — the explicit lattice instanton sector over a topologically neutral
background (R-143).** The question R-140 left open — explicit finite-action instanton
configurations — is structurally closed (R-143). Three exact statements and one
certificate.

*Neutrality:* the DM background itself carries **exactly zero site-based
topological density in each chiral sector, at every twist angle** — the mechanism is that the
DM twist plane `r ∧ e₄` is blind to the bond's `e₄`-orientation while the 4-volume ε-pairing
of triangle areas is `e₄`-reflection-odd, so every density of the site-based class cancels in
reflection-orbit pairs (a genuine cancellation of individually O(1) terms; the variant
convention is also neutral). Generic parity covariance would only relate the two sectors
(`q₊ = −q₋`); the per-sector vanishing is substrate-specific to the DM twist assignment
— a seeded-random homogeneous connection has robustly nonzero per-sector density (a
genericity control).

*The charge operator:* the canonical
site-based pairing form on the 192 based triangle loops calibrates as `Q_form(F) = 576·ε(F)`
**exactly** (continuum normalization `4π²`), giving a
normalized, exactly gauge-invariant lattice topological charge.

*Access:* an explicit,
compactly supported, singular-gauge winding-1 fluctuation valued in `SU(2)₊` (the SD
quaternion units) over the DM background has (a) `SU(2)₋` holonomies *identically* the
background's — the instanton lives in one chiral sector, with the mirrored construction giving
the other; (b) action excess of any plaquette-angle action supported on a finite,
box-independent triangle set (measured far deviation exactly zero); (c) boundary map = the
identity map `S³ → SU(2)`, the degree-1 `π₃` generator.

*Certificate:* the measured
charge of the exhibited configuration approaches 1 with a discretization deficit
`∝ 1/ρ²` in the instanton size — the signature of a unit-charge configuration — while
the same operator reads the bare background as zero. A derived by-product with a closed
form: the background couples *linearly* to an instanton's SD-spatial flux with coefficient
`4√2·a·sin²θ_D/sin a` (`a = arccos(cos²θ_D)`) — sourced exactly by the holonomy's non-abelian
excess `sin²θ_D` (the 48/66 commutator content) and orientation-blind (no
instanton/anti-instanton discrimination, no CP content) — so an *uncut* instanton tail would
pay a logarithmically growing excess in any Wilson-class action: compact support is the
correct finite-action object. Honest scope: no instanton
*solution* (no minimizer, size, action value, or tunneling rate — all kernel-gated with the
fluctuation dynamics); at strong twist the composite's integer sector label is carried by the
constructive family (neutral background + unit-winding fluctuation), not by a local operator
(the local reading on the composite degrades continuously with
`θ_D`). With R-088's index theorem, the `ΔB = ΔL = N_gen` selection rule
now has its substrate carrier structurally in place; the *rate* stays gated.

This is the **structural justification that weak SU(2)₊ can be gauged**. Without it, §C.4.2's
"weak = SD" INPUT bit would be picking a gauge group that the substrate might not actually
admit. With it, the bit is honest.

### C.4.7 The 24-bond count; SU(5) as historical translation

The D4 lattice's 24 nearest-neighbour bonds split as `12 + 12` (R-083): 12 spatial bonds
carrying the electroweak bivector multiplicities + colour rep content, and 12 e_4-bearing bonds
carrying the L ↔ Q transition channels (§D.3). In the GUT literature, the smallest gauge group
containing the SM is SU(5) with `dim(SU(5)) = 24` — a representation-theoretic match with the
historical embedding, but **not a load-bearing identification in TWT**. SU(5) is a removable
scaffold; TWT's gauge content emerges from D4 orbit structure directly, and the Weinberg angle
is derived without invoking SU(5) at any step. The historical 24-as-SU(5)-dim is preserved as a
translation for literature interoperability. **No physical SU(5), no X/Y bosons.**

---

## §C.5 — Strong, electroweak, matter-stability

The remaining SM-structural derivations: confinement and the strong sector, the electroweak
finishing layer, and the matter-stability ladder including the famous "one structural fact"
(no proton decay + Dirac neutrinos + no `0νββ`).

### C.5.1 Confinement — ontological-first, topology as formal consequence

Under §A.3 and §C.1.4, a baryon **is** one defect with one circular winding decomposed into
three orthogonal Q-orbit facets. A single quark in isolation = one orthogonal facet without the
other two = **not a valid stable configuration of the rotor field at all** (R-084). A free quark
is not "an object held in by a force from leaving the baryon" — it is not the right shape to be
an object. The three facets must be present together because they *are* the one circular
winding.

The **topological** reading is the formal consequence: a fractional-winding configuration
`B = 1/3` cannot smoothly interpolate to the vacuum at infinity, because there is no smooth map
`S³ → S³` of degree `1/3`. The integer-completion theorem requires three facets to compose; the
ontological reading says they already are one object. **Topology is what the ontology looks like
once formalized.**

### C.5.2 No fundamental SU(3)_c gauge field

The colour octet of §C.4.4 is **not eight fundamental spin-1 gluons** — it is an elastic-response
algebra of the rotor field, geometric L-rotations + a spin-2 strain quintet (R-085; the static
`su(3)` construction and its `C_A/C_F = 9/4` LEP consistency check are §C.4.4's). There is **no
chromoelectric flux** in TWT, no fundamental colour gauge field. The "gluon force" is identified
with the dynamical coset-5 = the §D.5 defect-vacuum kernel.

**Asymptotic freedom `β_3 < 0`** is a located, mechanism-less, dynamics-gated gap (§E.2). The
emergent-antiscreening route is closed by a derived absence: paramagnetic screening requires a
charged spin-1 field; TWT has none. **The sign face is decided-conditional (R-148):** the
Skyrme quartic enters the positivity-bounded elastic forward channel with positive
weight (`A_Skyrme(s,t,u) = −(s²/2 + tu)/(2e²f⁴)`, the vertex sign anchored to the
Hamiltonian-boundedness of R-085), and the dispersive
monotonicity of the arc-defined forward coefficient then forces `β_3 ≤ 0` — **the AF-signed
branch** — conditional on the registered inside-frame dispersive package (companion Section 13,
row I-13: analyticity, crossing, boundedness, optical-theorem positivity — the positivity leg
recast onto the §B.3-derived unitary QM). The result is
generic given the package (any two-term chiral action obeys it; the substrate content is that
the dressed action *is* that action) and of a literature-known class (Pham–Truong-type
dispersive sum rules). What it removes is the *wrong-sign risk* — conditional on
I-13; what it does **not** deliver is asymptotic freedom itself: the sign's source is the
additive `f²`-loop drift, not an antiscreening mechanism, and the full DGLAP structure and
magnitude remain the §D.5 kernel's burden. Gated to Paper-2.

### C.5.3 The ⟨I_4⟩ parity-breaking condensate

The DM coupling `D/J ≈ 0.79` means the D4 ground state has

> `⟨I_4⟩ ≠ 0`.

`I_4` is the pseudoscalar, and `I_4 → −I_4` under spatial parity. So `⟨I_4⟩ ≠ 0` is the
algebraic carrier of parity violation — it picks out one handedness for the substrate (R-086).

**Honest scope.** `⟨I_4⟩` is a *gauge singlet* — it commutes with
every bivector, so for every rotor `R`, `R I_4 R̃ = I_4` exactly. A condensate invariant under
`G` *cannot* break `G`. Therefore **⟨I_4⟩ delivers parity violation, NOT electroweak symmetry
breaking.**

The substrate-level origin of `⟨I_4⟩ ≠ 0` is the **DM-induced topological boundary term**
`𝓛_top(D) ∝ D · I_4 · ...` of §D.4.4 (R-110): the 4 no-shared-index `e_4`-bonds of §D.3 source a
term linear in `D` proportional to `I_4`, which on integration over a domain delivers the
`⟨I_4⟩`-condensate parity-odd structure. One `D`, multiple manifestations (§C.5.7).

### C.5.3a The doublet-condensate Φ as EWSB order parameter

What `⟨I_4⟩` does *not* do, the doublet condensate `Φ` does (R-086a). `Φ` is a complex `SU(2)_L` doublet
field on the spinor minimal ideal `𝒮` (§A.5.4), transforming under `SU(2)_L` by left
multiplication and under `U(1)_Y` by the central `e_4`-bilinear phase. Its vacuum expectation
value is non-zero,

> `⟨Φ⟩ = (0, v / √2)^T`  with `v ≈ 246 GeV`,

breaking `SU(2)_L × U(1)_Y → U(1)_em` via the standard mechanism: the gauge-covariant kinetic
term `|D_μ Φ|²` evaluated on `⟨Φ⟩` gives `W^±` and `Z^0` masses, while the unbroken combination
`T_3 + Y/2` (R-062) — the electric charge — leaves the photon massless. This is the standard
electroweak symmetry breaking, identified in the substrate as the doublet condensate on the
spinor ideal rather than imported as an independent ingredient.

**Honest scope.** The Higgs sector at the substrate-derivation level is FRAMING: V3 derives
the symmetry-breaking *structure* (which gauge subgroup is broken to which) from the doublet
identification on the spinor ideal, but does not derive the absolute scale `v ≈ 246 GeV` or the
Higgs mass. These are #1-gap-gated absolute magnitudes (§E.2.2), comparable in tier to α_em.
The two-scale conjecture `v / f_π ≈ m_p / m_e` is a numerical near-coincidence with
no mechanism — an intriguing lead, not derived.

### C.5.4 B − L anomaly cancellation from 3 × 1/3 = 1

The anomaly cancellation for `B − L` follows from one numerical fact. The per-generation
fermion sum

> three quarks of `(B − L) = 1/3` per quark + one lepton of `(B − L) = −1` per lepton = 0
  per generation,

is the *bookkeeping* statement of "three colours × one-third = one." The *anomaly-cancellation*
statement is that the gauge-trace anomalies vanish:

> `Tr[T_a T_b · (B − L)] = 0`  for the SU(3)_c × SU(2)_L × U(1)_Y gauge generators (R-087).

The two statements are deeply related — the same `3 × 1/3 = 1` fact that zeroes the per-fermion
sum also makes the gauge-trace anomalies vanish across one generation. The cancellation is not a
tuning of quark / lepton quantum numbers; it is forced by the colour count (R-053) and the
per-blade hypercharge eigenvalues (R-056). The anomaly-free combination is a structural
identity.

### C.5.5 BPST instanton + index theorem ⇒ ΔB = ΔL = N_gen

The BPST instanton in `Spin(4)` carries a finite Euclidean action

> `S_inst = 8π² / g²`

and a topological charge `Q = 1`. The Atiyah–Singer index theorem counts the chiral fermion
zero modes in the instanton background: for each generation, the Weyl-doublet zero mode gives
`ΔB = +1/3 × 3_colours = +1` and `ΔL = +1`. Summed across three generations, the index theorem
forces

> `ΔB = ΔL = N_gen = 3`

for any non-perturbative process mediated by the instanton (R-088). Three generations
collectively shift `B` and `L` by 3, with `B − L` preserved (per §C.5.4). This is the
standard-model 't Hooft selection rule, obtained here from the substrate's Spin(4) topology plus
the per-generation anomaly cancellation. (*Import notice:* the instanton + index-theorem pair
is an external effective-level import — registered as **I-2 in companion Section 13**; the
substrate carrier is structural (R-140/R-143) and the rate face stays gated.)

### C.5.6 No proton decay + Dirac neutrinos + no 0νββ — one structural fact

Three SM "extras" collapse to one substrate fact (R-089):

- **No proton decay.** `B` is integer winding in `π_3(S³)`; non-perturbative violation respects
  `ΔB = ΔL = 3` (§C.5.5); a `B = 1 → B = 0` channel would violate this. **Proton stable.**
- **Dirac neutrinos.** `B − L` is exactly conserved (anomaly-free, §C.5.4); a Majorana mass
  would violate `Δ(B−L) = −2`. **Forbidden.**
- **No 0νββ.** The same `B − L` exact conservation forbids the neutrinoless double-beta-decay
  signature. **Forbidden.**

Three predictions, one substrate reason. Canonical falsifiers §E.3 rows 4 + 5.

### C.5.7 β-decay as L-pair creation through I_4

The β-decay channel `n → p + e^- + ν̄_e` reads in the substrate as an L-pair creation through
the `I_4` Hodge map (R-090). The L-orbit's bivector winding source `J` is connected to the
Q-orbit's facet structure via `I_4`; the L-pair (electron + antineutrino) is created by the
algebraic mediation of the same `I_4` that the parity-violation condensate carries (§C.5.3).
**One `D`, multiple manifestations** — the same `D` that fixes the Cabibbo angle, the generation
phase, the Skyrme stabilizer, and parity violation also supplies the β-decay channel.

### C.5.8 The wave-phase stability ladder

Empirically, 20 stable particle states (photon + proton + electron + 3 neutrinos + stable
nuclei + antiparticles) match the framework's enumeration of stable sectors — `B` integer,
`L` integer, massless / massive single-defect or bound-multi-defect (R-091). The match holds
across 9 orders of magnitude in `N` (defect-count). This is a positive empirical-coherence pass,
not a derivation of stability mechanisms; what the framework provides is the structural
enumeration that yields exactly this stable set with no orphans (§E.3 row RF-7).

### C.5.9 Top quark exclusion

The top quark facet's decay rate `Γ_t` and the baryon-circularizing timescale `Θ_0` satisfy

> `Γ_t · Θ_0 ≈ 7.2 ≫ 1`  (R-091a).

The top facet decays before the baryon's circular winding can complete. **The top has no
hadrons**, by the framework's own structural prediction — a single-detection-away falsifier
(§E.3 row 14). The top mass remains a Standard-Model bookkeeping number, useful as an
abstraction (§A.4), but it is not a TWT verifier because no top-baryon mass eigenvalue exists
in the framework's mass spectrum.

### C.5.10 Nuclear length hierarchy and the 25-cell structure

The baryon Skyrmion has a **25-cell footprint**: one central cell + 24 nearest neighbours,
matching the D4 kissing number 24 exactly. The numerical structure:

- 90% mass radius `r_{90} ≈ 1.845 · ℓ_S ≈ 0.518 fm`.
- Soliton diameter `≈ 4 · ℓ_S ≈ 1.12 fm`.
- Nuclear hard core at `√2 · ℓ_S ≈ 0.397 fm` — the cell-exclusion distance below which two
  baryon Skyrmions cannot interpenetrate, set by the same cell-exclusion that fixes the
  confining-string diameter.

The 25-cell structure ties directly to A-1b D4 kissing — it is the geometric expression at the
hadronic-cell scale of the lattice's coordination structure at the monad scale.

The 25-cell Skyrmion gives the inter-nucleon force hierarchy (R-091b):

| Range | Cutoff | Mechanism |
|---|---|---|
| Hard core | `r < √2 · ℓ_S ≈ 0.397 fm` | Cell-exclusion (1+24 cell footprint) |
| Soliton core | `r ≈ 2 · ℓ_S ≈ 0.56 fm` | 25-cell body overlap |
| Pion Yukawa | `r ≈ 5.2 · ℓ_S ≈ 1.46 fm` | π Goldstone exchange |

The hard-core distance matches empirical 0.40–0.50 fm at 12% with no free parameter.

### C.5.11 Mesons — topological status and identifications

A meson is a `B = 0` configuration of the rotor field. Topologically: mesons carry `n_𝓠 = 0` in
`π_3(S³_𝓠)` and `H = 0` (trivial Hopf invariant) on the L-orbit — **the trivial class on both
orbits**. So **mesons are not topologically protected in TWT** (R-091c). Their observed
stability is *empirical*, sector by sector:

- **π** (135–140 MeV) — a true Goldstone of broken chiral SU(2). Stability against strong decay
  is the Goldstone mass-gap-from-zero.
- **K, η⁰** — pseudo-Goldstones of approximate SU(3)_flavor; η⁰ contaminated by η′ / U(1)_A.
- **η_c, η_b** — heavy quarkonia; no Goldstone character. The pseudo-scalar / vector splitting
  shrinks with quark mass; the pion alone shows ~2.5× chiral enhancement.
- **σ, ρ, ω** — CANDIDATE identifications at the substrate level: σ as the amplitude mode of the
  chiral condensate; ρ as a local Q-orbit SU(2) gauge boson; ω as the Q-orbit U(1)
  baryon-number gauge boson. None are derived here; the topological-status result above is
  what *is* derived.

The kinematic mass formula for a same-composition `B = 0` mode reads

> `m = 2 ω · |cos(α/2)|`,

with `ω` the meta-time rotor frequency and `α` the relative orientation of the two
opposite-`E`-sign defect facets composing the meson. This is the rotor-overlap formula and is
the substrate kinematics that the σ / ρ / ω identifications would lift to dynamical content.

*The §A.4 forward reference* — "Mesons admit an analogous decomposition" — points here: a meson
is two facets in the Q-orbit (or L-orbit, depending on flavour content) with opposite winding
sense, composing to a `B = 0` excitation rather than a `B = 1` baryon. Whether this realizes
as (A) a topologically trivial excitation of the Q-orbit vacuum or (B) a localized Q-orbit
soliton mode is the substrate-dynamics question routed through §D.5 (R-091c).

### C.5.12 The confining string

The confining string diameter is set by the cell length `ℓ_S = 0.281 fm`. **It is NOT a
chromoelectric flux tube** — TWT is gluon-free (R-085). The transverse map `S² → S³` has
`π_2(S³) = 0`, so no stable topological vortices of the chromoelectric type exist.

The string is the **integer-completion defect** of §C.5.1: a fractional facet trying to
separate from the baryon's three-facet circular winding cannot smoothly interpolate to
vacuum, and the string is the energy-minimizing configuration of the integer-completion
constraint. Its tension `σ_QCD ≈ 0.18–0.19 GeV²` (lattice / Regge slope `(440 MeV)² ≈ 0.194 GeV²`)
is a Q-orbit dynamical quantity at the §D.5 layer — **open**, gated on the substrate
dynamics. The chiral topology explains *why* a string is required (integer completion); it
does not yet compute what it *costs*.

---

# Part D — The substrate, technically

*The engineering layer. The reader who only wants the picture can stop after Part C; this part is
for the reader who wants to know what is under the hood, including where the framework's biggest
gap lives. The Clifford algebras are first, then the spinor / grade dictionary, then the D4
substrate, then the medium Lagrangian and wave equation (the linear face of which Part B's whole
QM/SR spine builds on), then the open driven-dissipative dynamics — explicitly named as the #1
gap at the layer where it lives.*

---

## §D.1 — The Clifford algebras

`Cl(4,0)` and `Cl(4,1)` in full. The native formalism throughout the paper is `Cl(4,0) + ℍ`
(§A.5.6); `Cl(4,1)` enters when meta-time is made explicit.

### D.1.1 Cl(4,0): generators, grades, M₂(ℍ)

Generators `{e_1, e_2, e_3, e_4}` with `e_i² = +1` and `e_i e_j = −e_j e_i` for `i ≠ j`. Real
dimension `2⁴ = 16`, with grade dimensions `(1, 4, 6, 4, 1)`: one scalar, four vectors, six
bivectors, four trivectors, one pseudoscalar.

The pseudoscalar `I_4 = e_1 e_2 e_3 e_4` satisfies `I_4² = +1`. As a real algebra,
`Cl(4,0) ≅ M_2(ℍ)` by Bott periodicity (R-092). This is the algebra the wavefront isomorphism of
§B.1 lands on; `Cl(1,3) ≅ M_2(ℍ)` is the same real algebra, which is what makes the Lorentzian
signature emergence (R-014/R-015) honest.

### D.1.2 Cl⁺(4,0) ≅ ℍ ⊕ ℍ — the even subalgebra

The even subalgebra `Cl⁺(4,0)` consists of grade-0 + grade-2 + grade-4 elements; dimension 8. It
splits as two copies of the quaternions:

> `Cl⁺(4,0) ≅ ℍ ⊕ ℍ`  (R-093),

with the two factors the self-dual (SD) and anti-self-dual (ASD) projections under the `I_4`
eigenvalue split (§D.2). This is where spinors live; this is where the spin and weak chiral
sectors live.

### D.1.3 Cl(4,1): adding e_5 explicitly

When meta-time is made explicit, the algebra extends with an extra generator `e_5`, with
`e_5² = −1` and `e_5 e_i = −e_i e_5` for `i ≤ 4`. The central element `E = I_4 · e_5` satisfies
`E² = −1` and is central (commutes with everything in `Cl(4,1)`).

`Cl(4,1)` has real dimension 32. The central pseudoscalar `I_5 = e_1 e_2 e_3 e_4 e_5` satisfies
`I_5² = −1` (n = 5 odd, q = 1 negative-signature direction: `(−1)^{n(n−1)/2 + q} = (−1)^{11} = −1`).
A central element squaring to `−1` is a **complex structure**, not a real splitting — so `Cl(4,1)`
does not decompose as a real direct sum. It is a simple real algebra with a central copy of `ℂ`,
realized as

> `Cl(4,1) ≅ M_4(ℂ)`,

real dimension `2 · 4² = 32`. (The neighbouring algebra `Cl(1,4)` has `I_5² = +1` and *does* split
as `M_2(ℍ) ⊕ M_2(ℍ)`; the two are distinct.)

The `M_4(ℂ)` reading lines up cleanly with §A.5.6's central element `E = I_5`: `E` is exactly the
complex unit of the central `ℂ`, and the "external `U(1)` phase" QM uses is the phase rotation
generated by it. **This is what the e_5 grounding rule (R-094) builds on** — `e_5` reduces to
phase under the `Cl(4,0) + ℍ` picture because `E` is the central complex unit of the larger
algebra.

`Cl(4,1)` contains `Cl(4,0) ≅ M_2(ℍ)` as a subalgebra (generated by
`{e_1, ..., e_4}`); the meta-time content lives in the `e_5`-bearing sectors.

### D.1.4 The e_5 grounding rule

A `Cl(4,1)` construction is **grounded** iff its `e_5`-content reduces to PHASE in the
`Cl(4,0) + ℍ` picture (R-094). That is:

- `e_5` may appear via the central element `E = I_4 · e_5` (global geometric complex unit), or
- `e_5` may appear as the meta-time axis of the rotor frequency `ω` (the mass-bearing rotor), or
- `e_5` may appear through the global **evolution/foliation parameter** `τ_5` — the timelike
  coordinate of the 5D master equation (§B.2.1, §D.4.6) and the Bell selection ordering
  (§B.4) — the meta-time role of §A.1/§A.5.6, reconciled with the phase reading through the
  wavefront lock `x_4 = c_meta · τ_5` (R-123).

If a construction requires `e_5` as a **spatial** degree of freedom — a new winding direction, a
soliton coordinate, a propagation axis — then the construction is **not grounded**. It is an
escape from the framework's ontology, not physics. The fix is to rebuild it in `Cl(4,0) + ℍ`,
where the spurious dimension disappears. This rule has caught several attempted derivations in
the framework's development history and is preserved here as a guardrail.

---

## §D.2 — Spinors, grades, the dictionary

The grade dictionary load-bearing through Parts B and C. Already previewed at §A.5; expanded here
to the full dictionary.

### D.2.1 The spinor minimal left ideal

`s_0 := (1 + e_4)/2` is the primitive idempotent: `s_0² = s_0` (direct check). The minimal left
ideal of `Cl(4,0)` is

> `𝒮 = Cl(4,0) · s_0`,

with real dimension 8, quaternionic dimension 2. Spinors are elements of this ideal. As a
quaternionic module, `𝒮 ≅ ℍ²`, which under `Cl(4,0) ≅ M_2(ℍ)` makes the algebra act on spinors
in the natural way.

### D.2.2 Primitive idempotents in Cl(4,1); the Dirac spinor

The primitive idempotents that build the Dirac spinor structure live in the `Cl(4,0)` subalgebra
of `Cl(4,1)`. The spatial-time projection

> `s_0 = (1 + e_4)/2`,  `s_0² = s_0`

is a real idempotent because `e_4² = +1`. The **chiral / Hodge projection**

> `s_± = (1 ± I_4)/2`,  `s_±² = s_±`

is also a real idempotent — *not* the analog `(1 ± E)/2` which a careful reader might guess
from §A.5.6's central `E = I_4 · e_5`. The reason: `E² = −1` (it acts as a complex structure,
not a real splitting), so `((1 + E)/2)² = E/2 ≠ (1 + E)/2`. The chiral / Hodge real-idempotent
projection uses `I_4`, which satisfies `I_4² = +1` in both `Cl(4,0)` and the `Cl(4,0)`-subalgebra
of `Cl(4,1)`, and acts as `±1` on the SD / ASD bivector halves (§D.2.4). The combined
`s_+ · s_0` projects onto a 4-component Dirac spinor (R-095). The central `E` of `Cl(4,1)`
plays a different role: it supplies the global geometric complex unit (§A.5.6), not a chiral
splitting.

The Dirac spinor as an `M_2(ℍ)`-module element (R-096) realizes the standard 4-spinor in a
Clifford-native frame: two quaternionic components, eight real components, the same content as
the standard Dirac spinor expressed via gamma matrices.

### D.2.3 The L/Q bivector decomposition (full)

The six bivectors split as `𝓛 ⊕ 𝓠`. The L-orbit closes as `so(3)` under commutator —
`exp(𝓛) = Spin(3)` is a genuine subgroup. There are two anchoring triple-product identities, and
they are **not parallel** — the L-orbit and Q-orbit triple products live at different grades:

> `e_{14} · e_{24} · e_{34} = −I_4`     (Q-orbit bivector triple → pseudoscalar)
> `e_{124} · e_{134} · e_{234} = +e_4`  (Q-orbit trivector triple → vector — the colour singlet, §C.4.4)  (R-097)

The L-orbit's own triple product `e_{12} · e_{13} · e_{23} = +1` is a *scalar* (the L-orbit's
so(3) closes back to grade 0), and is not informative as an anchoring identity. The two
anchoring triples that *are* load-bearing — the Q-orbit bivector triple landing on `I_4` and the
Q-orbit trivector triple landing on `e_4` — are what couple the orbit structure to the
pseudoscalar duality (R-005, R-010) and to the colour-singlet construction (§C.4.4).

The L-orbit closes as `so(3)`; the Q-orbit does not close. The symmetric-pair Cartan relations of
§A.5.2 — `[𝓛, 𝓛] ⊆ 𝓛`, `[𝓛, 𝓠] ⊆ 𝓠`, `[𝓠, 𝓠] ⊆ 𝓛` — make `so(4) = 𝓛 ⊕ 𝓠` a symmetric pair,
with `𝓠` the coset complement. The fibration `Spin(3) ↪ Spin(4) ↠ S³_𝓠` bridges chiral and
orbit bases of `π_3(Spin(4))` (§A.5.2, §C.1.3).

### D.2.4 The anti-self-dual generation triple

The chiral split of `Cl⁺(4,0) ≅ ℍ ⊕ ℍ` gives the self-dual (SD) and anti-self-dual (ASD) factors:

- SD = `span{e_{12} − e_{34}, e_{13} + e_{24}, e_{14} − e_{23}}` (the +1 eigenvectors of `I_4·`)
- ASD = `span{e_{12} + e_{34}, e_{13} − e_{24}, e_{14} + e_{23}}` (the −1 eigenvectors of `I_4·`)

The **ASD triple** (R-098) hosts the three imaginary units of `ℍ` on the
`V_4⊥` generation circle — the structural source of the three-generation count via Frobenius
(§C.3.8). The SD factor is the weak chiral sector (R-079).

### D.2.5 SD ↔ ASD mirror under spatial parity

Under spatial parity `P: e_i → −e_i` for `i = 1, 2, 3` (and `e_4` unchanged), SD and ASD are
exchanged (R-099). This is the algebraic source of the up/down mirror (R-077, §C.3.13). The
mirror is exact at the algebra level; the side-assignment "up = SD" is fixed by charge opposition
to the lepton sector.

### D.2.6 The grade dictionary

| Grade | Dim | Cl(4,0) content | Physical role |
|---|---|---|---|
| 0 | 1 | `𝟙` | Scalar — masses, charges as numbers |
| 1 | 4 | `e_1, e_2, e_3, e_4` | Vector — boost generators (B.2), position |
| 2 | 6 | `𝓛 ⊕ 𝓠` | Bivector — rotation generators, EM field strength, gauge content |
| 3 | 4 | `e_{ijk}` | Trivector — charge-species labels, colour trivectors |
| 4 | 1 | `I_4` | Pseudoscalar — Hodge duality, parity-breaking condensate |

The grade dictionary (R-100) is the load-bearing reference for which Cl elements play which
physical roles. Conflating grades has historically been the easiest place for errors to creep
into the framework's development (cf. §A.5.2, §D.2.4).

---

## §D.3 — The D4 monad layer

The substrate beneath the wave.

### D.3.1 The D4 lattice

The D4 lattice is the densest 4D **lattice** packing (Korkin–Zolotarev 1872). Whether it is
densest among *all* 4D packings is the open 24-cell conjecture; the recent optimality results
(Viazovska, dimension 8; Cohn–Kumar–Miller–Radchenko–Viazovska, dimension 24) do not cover
dimension 4. Its kissing number is 24. The bond structure is what the substrate's coherence-cell
pattern realizes: each lattice site has 24 nearest neighbours, splitting as `12 + 12` (R-101,
R-104) — 12 spatial bonds (`e_4`-free) and 12 `e_4`-bearing bonds.

Two motivating gates support the D4 identification:
- **Gate A (energetic):** D4 minimizes the substrate's exchange-energy density among 4D lattices.
- **Gate B (self-organization from melt):** *neutral* — the question of dynamical
  self-selection from a disordered phase is open.

The D4 identification is therefore **empirically motivated, not derived inside the framework**.
It is the axiom A-1b of the Opening.

### D.3.2 The monad as unit Clifford rotor

At each D4 site sits a unit Clifford rotor `R_i ∈ S³ ≅ SU(2) ≅ Spin(3)`, acting one-sidedly on
the spinor module (R-102). The continuum field `R(x)` is the rotor field whose dynamics §D.4
develops.

**Note on naming.** "Monad" names the Planckian-layer atom of the substrate. When discussing
cell-layer phenomenology (hadrons, the chirality balance, the canted ground state), "monad" is
avoided in favor of "substrate site" or "rotor", since the cell layer's constituents are not
the Planckian monads themselves but their cell-scale collective configurations. The "monad as
unit Clifford rotor" identification is a Planckian-layer statement.

### D.3.3 The two couplings J and D — calibration to leptons

Each D4 nearest-neighbour bond carries:
- a **symmetric exchange `J`** on all 24 bonds, and
- a **Dzyaloshinskii–Moriya `D`** on the 12 `e_4`-bonds only (R-103).

The DM coupling is parity-odd (the wave's chiral contribution; the substrate alone is achiral).
Its parity assignment is **structural** — the unique pair allowed by parity on D4. The ratio
`D/J ≈ 0.79` is the framework's chirality calibration, INPUT to the lepton sector via Brannen
`δ_L = 12.73°` (§C.3.5, §C.3.11).

Cross-sector consistency: independently, the baryon Skyrme stabilizer gives `D/J ≈ 0.779`
(§C.3.11). The ~1.1% cross-sector agreement is the framework's genuine over-determination
signal.

A layer note, made explicit: `J`, `D`, and the spacing `a` are defined on the D4 bond
structure, but every load-bearing use in this paper consumes them as **cell-layer effective
couplings** — `f_π² = 8J/a` with `f_π ≈ 129 MeV` fixes the working layer as the hadronic cell
(a Planckian-layer reading would misplace `f_π` by ~38 orders of magnitude). The monad-layer
couplings of the same form are related to these by the open cell-formation map (§D.3.5); the
two layers' couplings are not interchangeable.

### D.3.4 24-bond 12+12 split

The 24 bonds split as

> `z(D_4) = 24 = 12_spatial + 12_{e_4-bearing}`  (R-104).

The 12 spatial bonds carry the electroweak bivector multiplicities (the SD chiral algebra +
hypercharge) and the colour-sector representation content. The 12 `e_4`-bearing bonds carry the
L ↔ Q transition channels — historically labeled SU(5) X, Y leptoquarks in the GUT translation
(§C.4.6), but **no physical X, Y bosons exist in TWT.**

### D.3.5 The two-scale framework

The substrate is two-layered:
- A **Planckian monad layer** (the D4 lattice, fundamental rotor medium; sets the cutoff `Λ`).
- An **emergent hadronic cell layer** (where solitons, hadrons, and their masses live; the `f_π`
  scale at `ℓ_S ≈ 0.281 fm`).

The two scales are **forced**, not adopted for convenience (R-105). Without the two-scale
structure, the framework would be self-contradictory at the gravity / hadron-scale interface:
the Sakharov `Λ ~ M_Pl` of §B.6.2 cannot coexist with the cell-scale `f_π ~ 100 MeV` if the
substrate is single-scale. The two-scale framework is what makes the entire framework
internally consistent.

The **cell-formation mechanism** — how the cell layer emerges from the monad layer — is open
(a Layer-3 deep gate, §E.2). The two-scale structure is forced by self-consistency; its
realization is a Paper-2 target.

---

## §D.4 — Medium Lagrangian, wave equation, three faces

This section delivers what Part B was promised: the master wave equation, its linearization to
the 5D hyperbolic form, and the three physical faces (linear / topological / collective). This
is the *layer at which Part B's QM/SR/Bell content sits as an EFT-style readout*; without §D.4
the forward references at §B.2.1, §B.3, §B.4 dangle.

### D.4.1 Lattice-to-continuum mapping

The D4 lattice with cell spacing `a` maps to a continuum rotor field `R(x)` via the standard
expansion: lattice bond differences `R_i⁻¹ R_j ↦ exp(a · ∂_μ R · e^μ + O(a²))`. The leading
kinetic action is the σ-model

> `S_kin = ∫ d⁴x · (1/2) · Tr(∂_μ R · ∂^μ R) = ∫ d⁴x · (1/2) · ⟨Ω_μ Ω^μ⟩_0`,

with `Ω_μ = R̃ ∂_μ R` the Maurer–Cartan form. The lattice exchange `J` translates to the
kinetic stiffness via

> `f_π² = 8J/a`  (R-106).

This identifies `f_π` (the cell-scale mass-bearing condensate, §A.4) with the lattice kinetic
stiffness up to a numerical factor that is determined by the cell-formation mechanism (Layer-3
deep gate).

### D.4.2 The Skyrme stabilizer

Derrick's theorem (§C.1.1) requires a higher-derivative quartic term to stabilize finite-size
solitons. The natural candidate is the Skyrme stabilizer

> `S_Skyrme = ∫ d⁴x · (1/4e²) · ⟨[Ω_μ, Ω_ν][Ω^μ, Ω^ν]⟩_0`,

with `e` the dimensionless Skyrme coupling. At the dressed-coupling level

> `e ≈ √18 / (D/J) ≈ 5.39`  (lepton-calibrated `D/J ≈ 0.787`)  (R-107),

related to the chirality ratio by the geometric coincidence flagged at §C.3.11. This *reproduces*
the empirical ANW Skyrme **`e` value** `5.45` at ~1% in the favorable scheme — the *e-value
match* only, a prediction-vs-empirical comparison rather than an output of `5.45` itself; the
nucleon mass derived from the BVP via `M_0 = 36.47 · f_π/e` remains ~8% below empirical at the
leading-order BVP level (§C.1.2).

### D.4.3 The Luttinger–Tisza canted-helix transition

The substrate's ground state under combined `J + D` couplings is a **canted ferromagnet**, not
fully aligned. The canting angle `q ≈ 10.5°` is the Luttinger–Tisza spiral pitch at
`D/J ≈ 0.79` (R-108), with `cos q ≈ 0.983`. The canted ground state breaks chiral symmetry; the
breaking pattern is what the lepton-sector Brannen amplitude form parametrizes.

At the critical chirality balance `D = J`, the canted-helix structure becomes critical — the
quantum critical point (QCP) that underwrites the L-orbit electron mass scaling (§C.1.6).

### D.4.4 The full medium Lagrangian

Combining §D.4.1–§D.4.3, the substrate Lagrangian at the σ-model level is the **full Skyrme
Lagrangian with determined coefficients** (R-109):

> `𝓛_medium = (1/2) · ⟨Ω_μ Ω^μ⟩_0 + (1/4e²) · ⟨[Ω_μ, Ω_ν][Ω^μ, Ω^ν]⟩_0 + 𝓛_top(D)`,

with `𝓛_top(D)` the DM-induced topological boundary term (R-110) of the form
`µ · Ψ_0 · ρ_L`, sourcing L-pair creation in the wave-riding sector (the substrate channel for
β-decay, §C.5.7). The kinetic coefficient is fixed by `f_π² = 8J/a` (R-106), the quartic
stabilizer by `e ≈ √18 / (D/J)` (R-107); only the DM-topological coefficient `µ` is open (gated
on the substrate dynamics).

### D.4.5 The Skyrmion collective inertia and the QCD scale

The Skyrmion's collective-coordinate inertia (the moment of inertia for rigid `SU(2)` rotations
of the soliton) at the dressed-coupling level is

> `Θ_0 = 106.76 / (e³ · f_π)`,

with `106.76` the exact-BVP inertia coefficient (`Λ = 50.98`; R-133 — an earlier `97.27`,
provenance suspect, is consistent with a truncated-grid artifact, §C.1.2). At `e ≈ 5.45`,
`f_π = 129 MeV`, this gives `1/Θ_0 ≈ 196 MeV` — used in three places downstream: as the
candidate identification with `Λ_QCD` (R-111 below), as the timescale in the top-quark
exclusion `Γ_t · Θ_0 ≈ 7.2 ≫ 1` (§C.5.9), and as the band scale in §C.1.2's `M(J)` equation
(R-133). The heavy-baryon anchor predictions carry a tracked residual (R-133/R-138):
`Σ_c − Λ_c = 151.9 MeV` (−9.0%; candidate resolutions — a Callan–Klebanov-class bound-state
inertia, which is a different object, or a re-fit of the fit-inherited `hf_c` anchor
(independence unverified) — neither excluded, and the residual is fork-invariant under the
R-138 massive-scheme refit, which eliminated "scheme artifact" as an explanation), while
`Σ_b − Λ_b = 181.9 MeV` (−4.8%).

The natural mass-scale `1/Θ_0 ≈ 196 MeV` sits squarely in the `Λ_QCD` range (scheme-dependent:
the folk value is `≈ 200 MeV`, `Λ^(5)_MSbar ≈ 210`; no strengthening is claimed from
proximity). This is a candidate
identification (R-111): structurally
plausible (the cell-formation mechanism and the QCD running scale both live at the cell layer),
mechanism not yet pinned. The identification stands as a candidate pending the §D.5 closure.

### D.4.6 The master wave equation and its three faces

The Euler–Lagrange equation of the medium Lagrangian (§D.4.4) reads, varying with respect to the
rotor `R`,

> `∂_μ Ω^μ + [Skyrme stabilizer source] + [topological boundary source] = 0`,

with `Ω_μ = R̃ ∂_μ R`. This is a nonlinear equation in `R`. It has three physical faces (R-112);
Face 1 is what Part B builds on.

**Face 1 — Linear regime around the vacuum: the free wave operator.** Expand around the
substrate's **canted vacuum** `R = R_vac · (1 + δR)` (§D.4.3).

*A note on what "vacuum" means here.* The DM-coupled D4 ground state is generically a
**helimagnet** with a Luttinger–Tisza spiral wavevector `q ≈ 10.5°` per cell (§D.4.3). For the
linearization, we work in the standard **twist-gauge** (rotating frame): the position-dependent
spiral rotation is absorbed by a field redefinition, so the rotor field in the twisted frame has
an `x`-independent (homogeneous) reference value `R_vac`. The Maurer–Cartan form in the twisted
frame carries a *constant* background term proportional to `q` rather than a position-dependent
gradient. We refer to this twist-gauge homogeneous reference as "the vacuum" below.

At quadratic order in `δR`, the Skyrme stabilizer contributes terms of the form `(∂Ω)²` that
vanish on the homogeneous twist-gauge background (the constant Ω background does not
contribute at the kinetic-quadratic order in δR), and the topological boundary term `𝓛_top(D)`
contributes a constant. The linearized EL equation therefore reduces to the kinetic-term
equation alone:

> `∂_μ ∂^μ Ψ = 0`  in lattice-coordinate Minkowski form with metric `diag(+, −, −, −, −)` on
> `(τ_5, x_1, x_2, x_3, x_4)`,

which written out is the **5D hyperbolic form**

> **`c_meta⁻² · ∂²_{τ_5} Ψ = (∂_1² + ∂_2² + ∂_3² + ∂_4²) Ψ`**

— timelike in `τ_5`, four Euclidean spatial slices. *This is the linearization around the
vacuum*, not around a defect — the standard calculation, with no position-dependent potential
because `R_vac` carries no profile `F(r)` and the stabilizer terms vanish on a constant
background. This is the form **Part B's whole QM/SR spine builds on**: §B.2.1's Klein–Gordon
(via Fourier reduction at `k_4 = m`), §B.3's Schrödinger (envelope of the KG parent), §B.4's
Bell (computed on the linear face), §B.5's Maxwell (the linearized EM strain sector).

**Where defects enter.** Linearizing around a *defect* background `R = R_def(x) + δR` would
generically give a wave operator with a position-dependent potential `V(x)` sourced by the
soliton profile — the standard story for soliton fluctuation spectra (shape modes, bound states).
That is **not the route taken in this section**, and the reason is conceptual rather than
evasive: the QM machinery of Part B only ever needs the **free propagator** plus a classical
**potential `V(x)`** — Schrödinger's equation is `i ℏ ∂_t ψ = (−ℏ²/2m) ∇² ψ + V ψ`, with `V`
treated as a c-number background. So a vacuum-linearization that produces the free wave operator,
plus a defect that sources `V(x)` as a classical background contribution, delivers exactly what
QM consumes. Soliton-shape modes and soliton-fluctuation bound states *are* genuinely there in
the substrate dynamics; they are a Paper-2 question about the full nonlinear fluctuation
spectrum, not about the QM machinery. So the framework's strategy is:

1. The linearization here is around the **vacuum**, giving the free 5D hyperbolic form.
2. The presence of a defect introduces a **classical background contribution** to the linearized
   equation as a source term `V(x)` — recovered as the static profile entering the linearization
   when matter is added back to the picture.
3. That `V(x)` is precisely what §B.3.4 identifies as the potential in the Schrödinger envelope:
   *"The potential `V` is the defect-background term of the linearization."*

So the chain is: vacuum-linearization gives the free wave operator (§D.4.6 here); adding a defect
sources a position-dependent potential `V` (§B.3.4); the Schrödinger equation with `V` is what
QM uses. Soliton-fluctuation shape modes are a separate Paper-2 question.

**A first exact fact about that Paper-2 spectrum (R-125).** The shape-mode computation is still
owed, but one mode is already pinned exactly, by a symmetry shortcut. The master equation is
built from `Ω_μ = R̃∂_μR`, which is *exactly* invariant under the constant left shift `R → gR`
for `g` a Spin(4) rotor — so the symmetry derivative of any solution solves the linearized
equation around that solution, whatever the (unbuilt) kernel's form. Applied to a rest defect
`R* = exp(ûωτ₅/2)·R₀(x)`, the left `û`-shift generator yields the collective mode
`δR = (û/2)R*` — the zero mode of the co-rotating linearization — which in the lab frame
oscillates at exactly the defect's `ω` and, restricted to the wavefront lock, is `x₄`-periodic
at `k₄ = ω/c_meta`: precisely the Fourier label §B.2.1's Klein–Gordon reduction consumes as rest
mass. On the separable ansatz the mode coincides with the `τ₅`-translation mode, so a
`τ₅`-autonomous equation of motion suffices as an alternative premise — which is also the route
the central-`E` axis must take, since the `Ω`-built sector is *not* `E`-phase invariant
(`Ω(g_E R) = e^{Eθ}Ω(R)` exactly; the `E`-axis symmetry premise is open).
This derives the *existence and location* half of R-123's residue (ii); what remains is the
*identification* half — that the mode is normalizable relative to the carrier and is *the*
one-particle pole, with no other pole below it — which is exactly the shape-mode question above.
It also sharpens the falsifier face: a computed soliton-fluctuation spectrum whose one-particle
pole sat anywhere other than `ω/c_meta` would falsify the `m = k₄` identification.

**The full zero-mode catalog (R-126).** The lemma is a factory, and running it over the whole
symmetry catalog gives a multiplet-level statement: the rest defect's *exact* symmetry-mode
sector reads **only** the front labels `k₄ = ±ω/c_meta`. Left shifts split by the `û`-commutant
(the commuting 2-plane reads `+ω`, including the R-125 phase mode; the anticommuting 4-plane
reads `−ω` exactly — the conjugate branch, by the flip `B·Q(τ₅) = Q(−τ₅)·B`); right shifts —
newly established here as exact symmetries of the scalar `Ω`-word sector, since
`Ω(Rg) = g̃Ωg` makes every scalar `Ω`-word right-invariant by cyclicity — read `+ω`; translation
modes read `+ω`. No third label appears anywhere in the catalog: on the defect-linearized side,
the defect presents to the linearized theory as one rest label plus its conjugate, carried by
collective moduli, not as a spread of frequencies — the skeleton of the identification half
above (a qualitative multiplet statement, not an exact count — the mode families overlap).
Named conditions: the DM/topological sector's right-symmetry status is open (a breaking would
lift the right modes at the DM scale — a predicted fine structure); translations ride substrate
homogeneity (a continuum-limit statement over the discrete D4 lattice, in the §B.1.5
Lorentz-protection class); and the boost-generated *moving* family — which hands the dispersion
chain an independent second angle through §B.1's Lorentz orbit — is delivered at §B.2.2
(R-132): the boost orbit of the rest label is the mass shell, computed inside `Cl(4,0)` through
the γ-embedding; only the `e_{i4}`-plane rotations are circular.

**The localization half, discharged (R-130).** Of R-125's two named identification halves, the
localization one — that the mode is normalizable *relative to the carrier* — reduces exactly to
the defect's own localization. The raw mode is provably not normalizable: its pointwise norm is
constant `1/2` everywhere (`R₀` is a rotor, and both the `τ₅`-rotation and the axis
multiplication are Frobenius isometries) — a uniform global phase mode, which is why the excess
over the carrier's own phase mode is the only candidate object. That excess factorizes exactly,
`δR − (û/2)Q(τ₅) = (û/2)Q(τ₅)(R₀(x) − 1)`, and its pointwise norm is `½‖R₀(x) − 1‖`,
independent of `τ₅`: the mode's defect-excess is *exactly as localized as the defect itself*, so
mode-normalizability is equivalent to the defect's own finite-norm property (factor `½` exact).
The vacuum-relative-frequency subtlety R-125 flagged becomes a derived dichotomy rather than an
assumption: subtracting a carrier phase mode at any other frequency `ω_c` leaves an asymptotic
residual of norm `|sin((ω−ω_c)τ₅/4)|`, vanishing for all `τ₅` only at `ω_c = ω` — the
same-frequency subtraction is forced by localization itself (a genuinely two-frequency
configuration is non-separable and sits outside the rest ansatz; named, untreated). For the
hedgehog winding profile the criterion is explicit — `‖R₀ − 1‖² = 4sin²(F/4)`,
direction-independent (half-angle convention; the §C.1.1 profile is full-angle, and the tail
*exponent* criterion is convention-invariant) — so normalizability holds iff the profile tail
falls faster than `r^{−3/2}`. On the drive → 0 static face (Face 2 below), the exterior
linearization of the §C.1.1 radial equation is the Euler equation `r²F″ + 2rF′ − 2F = 0` with
indicial roots exactly `{−2, 1}`: the decaying branch is `r^{−2}`, and the static face
satisfies the criterion with margin. What remains of residue (ii) is therefore the pole
identification half (H2) *plus the tail condition for the full kernel* — a genuine open pair,
not one item: for a gapless carrier the rotating profile's tail is the standard below-continuum
bound-state question, plausibly the same discreteness condition (H2) needs (a bridging
conjecture, not folded in). The falsifier face sharpens correspondingly: an adopted kernel whose defect tail
fell slower than `r^{−3/2}` would make the phase-excess non-normalizable and strip the `m = k₄`
reading of its discrete carrier.

**The quantization step, given a skeleton (R-131).** The other named half — that the mode's
*quantization* produces the discrete one-particle label — also yields to the symmetry machinery.
On the rest ansatz the Maurer–Cartan form reduces exactly: `Ω_τ₅ = R₀~(ûω/2)R₀` (τ₅-free,
linear in ω) and `Ω_i = R₀~∂ᵢR₀` (ω-free), so any `Ω`-built action reduces to a function
`L(ω, shape)` whose ω-dependence funnels through one linear channel. The phase modulus — the
finite orbit of the same shift whose generator is R-125's mode — is *compact*: the rotor period
is `4π` exactly, `θ + 2π` gives exactly `−R`, and the `Ω`-built dynamics is blind to that sign
(the R-129 sign gauge), so the physical ray-orbit is a closed circle of period `2π`. Wave
mechanics on a compact modulus makes the conjugate charge discrete (a bare compact modulus would
admit a full `θ`-angle; the restriction to the integer vs half-integer menu rides on
rotor-double-cover single-valuedness — the Finkelstein–Rubinstein frame — and *which* of the two
is a ℤ₂ selection in exactly the FR family: named, not decided, and distinct from §B.3.5's
two-sided orientation sandwich, which is sign-blind where this one-sided orbit keeps the sign).
The spacing is then fixed by an envelope identity that is *universal in the kernel*: for any
conservative reduced Lagrangian, rest defects are relative equilibria (shape-stationary at fixed
ω), and along the family `dE/dN = ω` exactly — proved symbolically for fully generic
`L(ω, shape)`, and independent of which charge lattice the FR-class selection picks. So the
quantized phase tower is discrete with leading spacing exactly the defect's rotor frequency: the
first quantized phase excitation carries the same front label `k₄ = ω/c_meta` the classical mode
occupies (the label is inherited from R-125; the two surviving pieces of the identification
half — identifying the `N → N+1` transition quantum *with* §B.2.1's one-particle pole, and pole
uniqueness — are answered at the structural level by R-142: the clock-orbit identity
`exp(ûθ/2)R* = R*(τ₅+θ/ω)` makes the observer's channel phase and this modulus one `U(1)`, so
the channel pole's label is the `ΔN = 1` step at exactly `ω`, with the absolute tower-to-vacuum
anchoring a named face riding the R-007 ontology plus the kernel; and the pole is the winding-1
sector ground state conditional on named structural premises — the breathing channel is
certified strictly stable, non-breathing static channels ride the minimality premise, and the
kernel faces remain named opens). The inertia correction `O(d²E/dN²)` to the spacing is kernel-gated
— a rotational-band-class fine structure that becomes computable when the kernel lands, and the
energy-per-phase-quantum = ω form is the Planck relation's shape at the defect, consistent with
`mass = ω` (a framing observation, not a derivation of `ℏ`).

The linear face is structurally safe — the substrate-level safety chain (leak-independence,
symmetry-protected unitarity, Goldstone-symmetry-protected decoherence) operates here
(R-117, §D.5). This is *why* QM and Bell are unaffected by which side of the §D.5 memory fork
wins.

**Face 2 — Topological sector: matter as soliton (drive → 0 register).** In the drive → 0 limit,
the master equation reduces to the static Skyrme BVP of §C.1.1. Solutions are topological
solitons with integer winding; this is the *static face* of matter-as-defect.

**Face 3 — Collective regime: rotational spectrum.** Slow collective rotations of the `B = 1`
Skyrmion generate the collective spectrum via standard quantization of the rigid `SU(2)` rotor
coordinate. The lowest rotational excitations split by total angular momentum `J`:

> `J = 1/2` — the **nucleon** (lightest baryon),
> `J = 3/2` — the **Δ baryon**,

with the splitting set by `Δ E = J(J+1) / (2 Θ_0)`, giving the standard nucleon–Δ mass splitting
of order `300 MeV` for `Θ_0 ≈ 5 GeV⁻¹` — within the ANW Skyrme phenomenology spread. This is
Skyrme's most concrete hadron-physics output: the nucleon and Δ identifications are not separate
inputs but a single rotational tower over the same `B = 1` defect (§C.1).
The spectrum's coefficients (rotational moments of inertia) are dressed-coupling quantities at
this level; the absolute scales depend on §D.5 closure.

The **conservative master wave equation** in this section is the *fast / unitary face* of the
substrate dynamics. The full driven-dissipative dynamics (§D.5) reduces to this conservative form
on the linear face; the nonlinear face and the memory effect are what §D.5 opens.

---

## §D.5 — The driven-dissipative dynamics — the #1 gap

This is the framework's largest unbuilt object. Naming it here, at the layer where it lives,
rather than distributing the acknowledgement across multiple sections, is deliberate.

### D.5.1 The memory effect — mechanism

The substrate is driven (axiom A-2): the wave drives the medium along `e_4`. A driven nonlinear
medium with internal degrees of freedom develops a **memory effect** — a finite timescale
`τ_mem ≫ τ_wave` over which the medium's response to past drive accumulates and dissipates
(R-113). The memory kernel form is what §D.5 opens.

### D.5.2 The monostability theorem — Newtonian forbidden

The substrate cannot have a **memoryless / Newtonian** kernel: a defect would relax to vacuum
under instantaneous response, contradicting the existence of stable matter (R-114). So the
memoryless limit is excluded structurally; any consistent substrate dynamics must have a
finite `τ_mem > 0`.

### D.5.3 The rich/hysteretic kernel — adopted on physical motivation

The **rich/hysteretic** branch of the kernel — `τ_mem = τ_wave · exp(S/ℏ)`
with `S` a barrier action — was adopted on physical motivation (defect persistence demands a
finite hysteresis), **not as a forced consequence** (R-115). The alternative is a **fading** kernel
with no hysteresis but finite relaxation; defect persistence excludes only the strict-memoryless
limit (R-114), not the fading branch.

So the fading-vs-hysteretic fork is **gated on the substrate dynamics**, not closed. V3 inherits
V2's working commitment to the rich branch as the framework's working hypothesis, while honestly
flagging that the alternative is not refuted. **The fork is the framework's #1 gap.** (A concrete
candidate *class* for this kernel is proposed in §E.5.)

### D.5.4 Three roles of memory

The memory kernel sources three physical roles (R-116):

- **Cell formation** at the substrate's cell-layer emergence — the mechanism by which the
  Planckian monad layer self-organizes into the cell layer (§D.3.5). Open.
- **Selection** (the Role-3 Born selection of §B.3 / §B.4) — the substrate-level mechanism by
  which a measurement outcome settles into a definite eigenstate. The linear-face safety chain
  protects QM and Bell from kernel uncertainty here.
- **Bell-pair memory** — the same kernel governs the §B.4.5 Bell-memory bridge, with the same
  `Im χ` transport function appearing as a single dial for both decoherence and pair-correlation
  memory.

Three operational windows, one kernel. The macromolecule-interferometry falsifier (§E.3 VG-1)
probes this kernel directly through the decoherence rate's `Im χ` dependence.

### D.5.5 Linear face structurally safe

What the linear face of §D.4 delivers — Klein–Gordon, Schrödinger, Dirac, Bell, Maxwell — is
structurally safe under the §D.5 fork (R-117). Three substrate-level results underwrite this:

- **Leak-independence** (WP-IX3): linear-face unitarity is preserved regardless of which kernel
  branch is realized, provided the required symmetry conditions hold — and they do (R-117).
- **Symmetry-protected unitarity** (WP-IX4): the substrate's `Spin(4)` symmetry prevents unitarity
  violation on the linear face.
- **Goldstone-symmetry-protected decoherence** (WP-DC2): the decoherence rate's lower bound is
  set by Goldstone-symmetry constraints (Adler-zero protection), not by the kernel's specific
  form. The macromolecule-interferometry rate is bracketed regardless of fork outcome.

So **QM and Bell are structurally independent of the §D.5 closure**. The Tsirelson bound `2√2`
remains `2√2` regardless. This is what makes the framework's strongest spine results (Part B)
robust against the largest gap (Part D).

### D.5.6 Θ_rel — the framework's highest-value target

The **coset-Cartan FDT-violation residual `Θ_rel`** is the single object that ties together four
faces of the open frontier (R-118):

- **Colour-U(3) → SU(3) breaking** (the coset-5 mediated dynamical colour force, §C.4.4 / §C.5.2).
- **CKM property P** (the non-circulant 3-distinct splitting of the CKM hierarchy).
- **Memory fork** (fading vs hysteretic; §D.5.3).
- **Possibly coupling-universality via SOC universality** (a candidate route
  to `g_1 = g_2 = g_3` at the substrate scale).

What's currently DERIVED is the **shared Z_3-breaking / coset-Cartan *direction*** as one
engine-checked binary condition across colour-U(3) and CKM-P (R-118). What is **not yet built**
is the single Θ_rel *kernel value* that would source all four faces at once. The dynamical
merge is a candidate; the value is #1-gap-gated.

**Closing Θ_rel — equivalently, closing the §D.5.3 kernel fork — is the single biggest move
available to the framework.** It is the framework's #1 gap. Almost every open numerical value
in the pending-values registry (α_em, α_s, α_W, individual mass scales, the cosmological
constant residual, CKM hierarchy, decoherence rate, memory timescale — full inventory at
companion Section 4) routes through Θ_rel.

### D.5.7 Status summary

- **Structural geometry: closed conditional.** The shared Z_3-breaking direction is derived;
  the symmetric-pair structure and the fibration bridge are derived; the matter-as-defect
  ontology is solid.
- **Substrate dynamics form: open.** Fading-vs-hysteretic fork uncommitted; rich branch adopted
  as working hypothesis.
- **Magnitude pinning: open.** Θ_rel value, `Im χ` form, individual coupling magnitudes,
  individual mass scales — all gated.
- **Linear face: structurally safe.** QM, SR, Bell, Maxwell content of Part B robust.

The framework's posture on the #1 gap is the canonical "claim the structure, not the
magnitudes." Part B's spine claims are not magnitude predictions; they are structural derivations
that survive the gap. Part C's mixed-tier content is honestly reported. Part E's open-frontier
section names what closing the gap would unlock.

---

# Part E — Cosmology, status, frontiers

*The open frontier. The reader who got this far has met the framework's case at its strongest;
what follows is the framework's case at its most honest. Candidates, falsifiers, dark sector
scope, Paper-2 agenda — and the synthesis of what TWT actually contributes.*

---

## §E.1 — Cosmology and the arrow of time (frontier)

What §B.7 did not cover: the value-gated half of cosmology, the macroscopic-limit reframing's
falsifier face, and the dark-matter scope statement.

### E.1.1 The cosmological-constant residual Λ ~ H²

§B.7 covered the structural half of the cosmological-constant story: Volovik's self-sustained
medium identity (R-047) makes the gravitating vacuum energy vanish exactly at equilibrium. The
substrate is, however, driven-dissipative (per the §D.5 rich-branch commitment) — not in
equilibrium. The deviation from equilibrium is set by the drive. So **dark energy is small,
nonzero, and tied to the front dynamics** — rather than tuned against vacuum-energy contributions.

The expected residual scale is

> `Λ_residual ~ H²`  (R-119),

with the precise coefficient gated on `Im χ` (the §D.5 transport function). A measured value
inconsistent with the substrate's driven-dissipative deviation from Volovik equilibrium would
falsify the structural identification. Canonical falsifier §E.3 VG-2.

### E.1.2 The macroscopic limit — frontier face

§B.8 covered the Eulerian reframing — bodies as defect-features of one wavefront, with the
atlas-with-seams of the classical N-body problem reading as a projection artifact (R-050a). The
**dynamics-coherent version** of that reframing depends on multi-defect well-posedness of the
wavefront field equation — and the multi-defect `Cl(4,1)` wave equation with `N` back-reacting
topological sources **is not constructed in this paper**. The Eulerian ontology (bodies as
features of one wavefront) is solid; the dynamics-coherent reframing is a structural target
(R-120). Two *static* data now exist for it: the ansatz-reduced `B = 2` BVP (R-135) and the
full-3D ansatz-free `B = 2` minimization (R-144, §C.1.2) — the static variational face of
the two-defect sector is coherent; what remains genuinely unconstructed is the *dynamical*
multi-defect wave equation itself.

This is canonical falsifier §E.3 SC-1 — a *structural-coherence* condition rather than a
single-detection-away kill. If the multi-defect EOM cannot be coherently constructed, the
framework's macroscopic-limit reframing breaks; what survives is the kinematic content of §B.8.1
through §B.8.3.

### E.1.3 Dark matter — what TWT structurally predicts and what is out of scope

The framework structurally predicts **three sterile right-handed neutrinos** — the wave-decoupled
`S_-` partners of the three active left-handed neutrinos, one per generation (R-121). This is
DERIVED: Dirac character is forced by exact `B − L` conservation (§C.5.4–§C.5.6), and the
right-handed partner is the sterile, wave-decoupled `S_-` mode (§C.3.12).

**The relic contribution is ~2% of Ω_DM.** With Dirac character tying `m_sterile = m_active` per
generation, the sterile mass scale inherits the active scale `Σ m_ν ≲ 0.12 eV` (Planck + BAO).
The thermal upper bound gives `Ω_s h² ≤ 0.00255`, **~2.1% of Ω_DM** — a 47× shortfall vs the
needed dark-matter density (R-122). Sub-eV thermal Dirac fermions are independently
hot-DM-excluded by free-streaming (Planck + LSS `f_HDM < 0.01`); the Dodelson–Widrow sterile
window requires `m_s ~ keV`, four orders above TWT's tied-to-active scale. This is the *expected*
first-cut outcome — sterile RH neutrinos are notoriously hard to make up all of dark matter — and
is recorded as a quantitative scope-line, not a refutation of the structural three-count
prediction.

**The remaining ~98% of Ω_DM is outside TWT's current derivational scope.** The framework does
not, at V3, predict a specific mechanism, particle, or substrate texture for the dominant
dark-matter component. The V1 wavefront-texture proposal was retired in V2 when the §B.6
induced-GR result removed its scalar-gravity premise; no replacement has survived
review. This is a **deliberate scope statement**, not a placeholder claim.

Three re-attack handles within the sterile-RH lead remain as Paper-2 research leads (Z1, Z2, Z3
in the pending-values registry — companion Section 4). Of the two additional V2-era leads, the
**differential-coupling lead is now adjudicated — a clean structural negative (R-146)**: the
texture-metric source of any grade-2 substrate excitation is identically its E·B-type L–Q
cross-correlation, `h(B,B) = 2⟨B_L I₄ B_Q⟩₀` — exactly the L↔Q-bridging content that
constitutes the electromagnetic strain channel — so no EM-polarization-dark gravitating
excitation exists in the derived field content (the maximally gravitating pure-SD/ASD
polarizations are exactly half-magnetic, half-electric; the transverse photon itself is h-dark
at bilinear order; the grade-3 route is doubly dead — odd parity in the metric bilinear, and
outside the even substrate field entirely). The negative is conditional on the
photon-strain identification (R-035), the gauge-projection premise, and the direct-bilinear accounting
(whose matter→h face is itself open); its one located loophole is the **grade-0×grade-4
amplitude channel** — a non-unit scalar–pseudoscalar excitation would gravitate with zero EM
strain, but only if the §D.5 dynamics supports gapped amplitude modes (a DM-shaped,
kernel-gated handle).

The **wave-train phase-defect lead is also adjudicated — a clean
negative (R-147)**: the blade, not the topology, fixes the metric source — balanced-blade and
carrier-phase (`U(1)_E`) defects are h-null exactly (even at non-unit amplitude), the only
gravitating dislocation (the chiral-ideal SD-phase one, `h = −½dθ⊗dθ` exact) sources geometry
identically through the EM-visible L–Q cross term pointwise, and no `π₁` protection exists in
the rotor field (the winding-1 dislocation loop is explicitly unwindable; the one ℤ-protected
class, carrier-phase vortices, is exactly the h-null one). Nothing is simultaneously
gravitating, EM-dark, and topologically protected.

Both V2-era leads thus funnel into the
single amplitude-channel loophole — now carrying two named conditions on the §D.5 dynamics
(amplitude modes must exist, and EM-dark defect cores must couple into the grade-4 amplitude
channel); phase-vortex cores are the natural
population mechanism of that channel (R-147). The structural
3-count prediction stands either way; it is canonical falsifier §E.3 VG-4.

---

## §E.2 — Status: derived, input, open

This section is the narrative companion to the **Result Index** (companion Section 1). The Index is the
flat-table version; this section is the synthesis. For row-by-row tier honesty, the Index is
authoritative.

### E.2.1 The parameter ledger

**Five INPUTs** (see the Opening, ordered by structural weight): `weak = SD` (one bit), `Λ` (Planckian
cutoff), `f_π` (cell mass scale), `D/J` (chirality), `c = √2 ⇔ K = 2/3` (Brannen phase), plus
`A` (lepton amplitude scale — cancels in ratios).

### E.2.2 Pending-values registry — what each gap unlocks

The framework's open numerical values cluster on a small number of deep objects:

- **Gated on `Im χ` (the #1 gap):** `α_em`, `g`, `α_s`, `α_W` — the four EW + strong couplings,
  via §B.5b's single-dial economy. Decoherence rate `1/T_2` (the macromolecule-interferometry
  decoherence floor is the same dial's second operational window, §B.4.5), cosmological-constant
  residual `Λ ~ H²`. **Six magnitudes, one transport function.**
- **Gated on `Θ_rel` (the FDT-violation residual):** colour-U(3) → SU(3) breaking, CKM
  hierarchy + Jarlskog, asymptotic-freedom DGLAP structure + magnitude (the *sign* face is
  decided-conditional — the AF-signed branch `β_3 ≤ 0`, R-148 §C.5.2, conditional on the
  registered dispersive import I-13), coupling-universality (a candidate route via SOC).
- **Gated on absolute ω scale:** `f_π` absolute MeV, `M_0` baryon mass, `1/Θ_0`, `m_e` via
  L-orbit QCP, same-composition mass split magnitudes, vector meson absolute masses.
- **Gated on `S` (rich-branch barrier action):** `τ_mem`, tunneling rates, Born selection rate.
- **Gated on L2 mechanism:** anomalous-dim `ν = 3π/2` for L-orbit QCP, active-sterile overlap
  for `m_ν`.
- **Located-gap items with named re-attack handles:** the critical canting/magnon stiffness
  `K_c`; the sterile-RH dark-matter lead (Z1/Z2/Z3).

Alongside the *value* gates above, the framework's structural results carry a second, shorter
inventory: the **named premises** on which otherwise-derived conclusions still rest. These are
not open numbers but open lemmas, each with a stated would-change-if, and together they are the
honest distance between the current text and a fully forward-derived spine:

| Premise | What it conditions | What would discharge it |
|---|---|---|
| **F2** — statistical noncontextuality of the Role-3 selection functional | the Born exponent's theorem status (§B.3.3, R-160) | a Role-3 construction carrying the channel-pairwise drag structure |
| **P1b-DYN** — the mode determinant generates the induced term | fermionic Skyrmion quantization as *induced* rather than selected (§B.3.5, R-161) | the substrate computation of the induced term (#1-gap adjacent) |
| **OA-LF-i / OA-LF-ii** — ground-state occupation; monad-scale covariant curvature coupling | the induced-gravity magnitude bracket (§B.6.2, R-163) | the kernel, or a curved-lattice band construction |
| **cross-block rigidity** (+ an open cross-block weight) | folding `α_s` into the single-dial economy (§B.5b.3, R-162) | a kernel with the named universality across inequivalent Schur blocks |
| **P4 / P5** — one universal charge functional; per-defect chirality-independence | the proton–electron equality as theorem rather than anchor (§C.2.7, R-159) | an EM-sector construction fixing the functional's universality |
| **the ℍ-unit identification** | the three-generation count (§C.3.8) | a substrate-dynamical selection of the generation triple |

Four of the six route into the same place the value gates do — the driven-dissipative dynamics
of §D.5 — which is the framework's central structural claim about its own incompleteness: not
many independent gaps, but one object with many faces.

The **over-determination opportunity**: pin-and-check across
the registry's collective set provides constraints on the kernel objects beyond what any one
item gives. A candidate `Im χ` value must satisfy all the gates simultaneously.

### E.2.3 Parameter reduction — honest count

The textbook SM count is 19 free parameters (three gauge couplings, the strong-CP phase `θ_QCD`,
Higgs VEV, Higgs mass, six
quark masses, three charged-lepton masses, and the four CKM parameters — three angles plus one
CP phase), rising to 26-28 with neutrinos.

**On the magnitude axis**, TWT pins:
- **1 at unification, on the counted inputs alone**: `sin²θ_W = 3/8` (R-082).
- **Up to 4 conditionally**: the three charged-lepton mass ratios, conditional on a forward
  Brannen derivation that is currently refuted (FIT tier, §C.3.5), plus the Cabibbo angle via
  the frequency-ratio reading `|V_us|² = m_d/m_s` (§C.3.10, a candidate).
- **TWT does NOT derive**: any coupling magnitude (#1-gap-gated), individual quark masses
  (the framework's mass-scope rule, §A.4: abstention from independent quark masses), Higgs VEV, Higgs mass, CKM hierarchy
  (#1-gap-routed), PMNS matrix (defused — no substrate prediction), neutrino masses (gated).

**Headline: 1 of 19 unconditional + up to 4 conditional** on the magnitude axis.

**On the structural axis**, TWT delivers **ten structural derivations** of SM choices
the SM treats as postulates rather than parameters: the gauge group structure (§C.4); the charge
spectrum (§C.2); the three-generation count (§C.3.8, conditional on the ℍ-unit
identification); `B − L` conservation +
anomaly cancellation + Dirac neutrino character as one fact (§C.5.4–§C.5.6); no proton decay +
no `0νββ` (§C.5.6); the up/down mirror (§C.3.13); V−A + generation-blindness + doublet (all from
weak = SD); the Lorentzian signature flip (§B.1); the no-monopole result (§B.5.2); the Tsirelson
bound (§B.4).

**This is the parameter reduction TWT actually claims.** On the magnitude axis the framework
honestly leaves most of the SM's 19 parameters #1-gap-gated. On the structural axis, the
framework's contribution is the conversion of SM postulates into substrate consequences.

---

## §E.3 — Falsifiers

### Disclaimer — the scope of falsifiability in a framework under construction

This theory is under active construction. The falsifiers listed below concern its **current
formulation** — the specific derivations, identifications, and structural claims that V3 makes.
Most of them, if triggered, would falsify the current formulation and *force an evolution of the
framework*: a reformulation of the substrate, a different identification of a symmetry, a
modified derivation chain. **Very few can kill the theory *itself*** — the underlying
ontological premise of a wave-based Euclidean substrate with matter-as-defect — because that
premise is compatible with a wide range of specific realizations and would evolve to accommodate
any observed fact that contradicts the current formulation.

Given TWT's **extensive overlap with the Standard Model on observable predictions** (exact
wherever the framework's derived structure reaches — the QCD dynamical sector is underived;
the framework's contribution is to *derive* SM structural facts from a substrate rather than
take them as input), a large fraction of the falsifiers below would simultaneously kill the SM if they
triggered — because they test predictions the SM and TWT share. The truly framework-versus-SM
discriminators are a smaller subset.

**Row-by-row classification against this scope.** Reading E.3.1 with this lens:

- *Kills TWT-current AND SM together* (both would need to reformulate): CHSH > 2√2 (row 11),
  fractional charge outside `{±1/3, ±2/3, ±1}` (row 13), tree-level FCNC (row 17), and a
  baryon containing a top quark (row 14 — standard QCD's `Γ_t ≫` hadronization-rate argument
  makes the same exclusion). These test
  QM-Tsirelson, algebraic charge quantization, Schur-lemma constraints, and a decay-timescale
  argument that the SM also commits to.
- *TWT-current specific, SM survives* (would falsify TWT's current formulation but leave the SM
  unaffected): proton decay (row 4; SM predicts stability too, but TWT's topological route is
  what fails), `0νββ` (row 5; SM allows Majorana, TWT commits to Dirac), magnetic monopole
  (row 12; SM allows monopoles, TWT forbids), fourth generation (row 15; SM allows,
  TWT forbids), finite Geneva-class influence speed (row 6), Bell-selection foliation ≠
  comoving (row 7).
- *Framework-general vs specific-derivation* (kill the current derivation but the framework's
  ontology can plausibly evolve): UHE-CR LV (rows 1–2), `c_GW ≠ c_γ` (row 3),
  differential `c_meta` (row 8), optical-clock decoherence (row 9), macromolecule decoherence
  (row 10), truly independent `θ_C` (row 16).

**How to read the tables.** A single-positive-detection kill for a specific row triggers the
next paper, not a framework obituary. The ontological premise (wave + substrate + matter-as-defect)
is more robust than any specific derivation. The framework's honest exposure is *what would
trigger the next paper*, not *what could kill the framework outright*. The one class that could
genuinely kill the underlying premise is fundamental incompatibility between a robust
`c_meta ≠ c` differential detection (row 8) and the wavefront-locking premise (A-3) — which is
why §E.3.5's internal pre-mortem (3) also flags this as the framework's tightest existential
exposure.

The four operational categories: named near-term (single-detection-away), removed
(achievements), value-gated (await #1-gap closure), structural-coherence (would break internal
construction). The internal pre-mortem (§E.3.5) is the fifth category — internal exposures
rather than external detections.

### E.3.1 Named near-term falsifiers (single-detection-away kills)

The framework's tightest near-term LV test sits at the top: at the §B.6.2 `Λ`-bracket lower
corner, the UHE-CR prediction is at-bounds with the tightest matter-sector LV bound
`|δ| ≲ 10⁻¹⁵`. A factor-~3 tightening of UHE LV searches, or detection of LV at the current
`~10⁻¹⁵` level, falsifies the framework's `Λ` two-scale closure across most of the bracket.

| # | Falsifier | Channel / apparatus | Current bound | TWT prediction | What it kills | Origin |
|---|---|---|---|---|---|---|
| 1 | LV `δ` at UHE cosmic rays | UHE-CR observatories | `\|δ\| ≲ 10⁻¹⁵` | `(E/Λ)² ∈ [1.3×10⁻¹⁶, 2.6×10⁻¹⁵]` across the `Λ`-bracket — at-bounds at the lower corner | the `(E/Λ)²` two-scale + cubic-isotropy + matter-as-defect closure | §B.6.3, §B.1.4 |
| 2 | Binary-pulsar `\|α_3\|` tightened | radio binary-pulsar timing | `\|α_3\| < 4 × 10⁻²⁰` | reads against the same `(E/Λ)²` ceiling | same closure as row 1 | §B.6.3 |
| 3 | `c_GW ≠ c_γ` beyond `10⁻¹⁵` | GW + EM multimessenger (GW170817-class) | `\|c_GW/c − 1\| ≲ 10⁻¹⁵` | structural `c_GW = c_γ`, automatic for matter-loop-induced gravity riding the same wavefront | induced gravity riding the wave | §B.6.3 |
| 4 | Proton decay (`p → e⁺π⁰` etc.) | Super-K, Hyper-K, DUNE | `τ_p > 1.6 × 10³⁴` yr | absolutely stable (`B ∈ π_3 = ℤ`; non-perturbative violation only as `ΔB = ΔL = 3`) | topological protection of `B` | §C.1.5, §C.5.6 |
| 5 | `0νββ` detected | KamLAND-Zen, LEGEND, nEXO, CUPID | `T_{1/2}(¹³⁶Xe) > 2.3 × 10²⁶` yr | forbidden (Dirac neutrino forced by `B − L` conservation; Majorana requires `Δ(B−L) = −2`) | Dirac character of the neutrino | §C.3.12, §C.5.6 |
| 6 | Finite Geneva-class influence speed found (Salart et al. 2008; Yin et al. 2013) | Bell-correlation timing in candidate preferred frames | `v_inf > 10⁴ c` | no finite influence speed — operationally, signaling does not exist | non-separability without signaling (`τ_5`-foliation = cosmological comoving) | §B.4.5 |
| 7 | Bell-selection foliation ≠ cosmological comoving frame | precision Bell + cosmology cross-comparison | n/a (corollary of row 6) | identical | the `τ_5`-foliation = comoving identification | §B.4.5 |
| 8 | Time-varying differential `c_meta` between sectors / epochs | precision multimessenger astronomy | `c_meta = c` on average | structural identity globally | §A.4, §B.7 average-`c` identification | §A.4 |
| 9 | Optical-clock decoherence below Goldstone-symmetry floor | atom-interferometry, optical clocks | experimental upper limits sit above the predicted floor | rate bounded below by the Goldstone floor (Adler-zero protection) | symmetry-protected decoherence safety | §D.5.5 |
| 10 | Macromolecule-interferometry decoherence below `Im χ` floor | macromolecule interferometry | current experimental upper limits sit above the predicted floor | substrate sits near KSS `η/s ≥ ℏ/4π` floor; bracketed KSS-to-GW170817 | the `Im χ` master dial (one dial, two windows) | §B.4.5 Bell-memory bridge |
| 11 | CHSH violation `> 2√2` | quantum optics | bounded by Tsirelson | bounded by `2√2` | one-sided rotor half-angle structure | §B.4.1 |
| 12 | Magnetic monopole detected | various | none observed | forbidden (`F` is bivector, `∇F = J` with grade-1 source only) | geometric forbiddance | §B.5.2 |
| 13 | Fractional charge outside `±1/3, ±2/3, ±1` | direct searches | none observed | forbidden (algebraic identity from D4 trivector content) | charge-spectrum algebraic identity | §C.2.2 |
| 14 | Baryon containing a top quark | LHC | none observed | forbidden (`Γ_t · Θ_0 ≈ 7.2 ≫ 1`) | timescale-exclusion structural argument | §C.5.9 |
| 15 | Fourth fermion generation | LHC + neutrino-oscillation precision | none observed | forbidden (`ℍ` has only three imaginary units; Frobenius) | Frobenius classification + `ℍ`-unit identification (conditional) | §C.3.8 |
| 16 | Hierarchical CKM `θ_C` shown demonstrably independent of the `m_d, m_s` relation at sub-percent precision | high-precision CKM data | `\|V_us\|² ≈ 0.0503`; `m_d/m_s ≈ 0.0500` (~0.6% agreement) | frequency-ratio reading `\|V_us\|² = m_d/m_s` | the frequency-ratio reading of Cabibbo | §C.3.10 |
| 17 | Tree-level FCNC observed | precision flavour physics | tight upper bounds | forbidden at tree level (weak = SD couples generation-blindly) | the `weak = SD` INPUT bit | §C.4.2 |
| 18 | Proton–electron charge sum non-zero | neutrality-of-matter / bulk-matter charge tests | `\|Q_p + Q_e\|/e ≲ 10⁻²¹` | exactly zero, identically in the charge normalization `c` | the (P4, P5, P6) premise set — the framework reverts to an empirical charge anchor | §C.2.7, §C.2.8 |

Each row is a single positive detection away from falsification, or a null result still consistent
at current precision. (A frame hedge on rows 9–10: the laboratory limits there are
*inside-frame* data, binding the outside-frame `Im χ`/Goldstone floors only through the
un-built outside↔inside projection — the same hedge §E.5 carries for its own inside-frame
comparisons.) The parameter reduction (§E.2.3) is the framework's case; the falsifiers
are its price.

### E.3.2 Removed falsifiers (achievements)

Frameworks that could have been killed by an internal structural failure and were not — recorded
per the framework's negatives discipline (companion Section 6). Not experimental kills but
constructions where a latent kill-condition was located
and discharged by substrate-level structure (or shown to never have been a real prediction).

| # | What it would have killed | How TWT discharges | Engine | Origin |
|---|---|---|---|---|
| RF-1 | Wrong-sign / repulsive gravity from chiral matter loops | Spin-2 channel decomposition: apparent negative lives in the constrained trace channel; physical spin-2 channel is positive by `C_T > 0` (unitarity) ≡ substrate stability | `induced_G_sign_cross_check` | §B.6.4 |
| RF-2 | Catastrophic `ξ = 1/6` Sakharov cancellation | Maurer-Cartan shift-symmetry forces `ξ = 0` at leading order; `ξ R φ²` is shift-non-invariant. Residual `(f_π/Λ)² ~ 10⁻⁴⁰–10⁻³⁹`, not `1/6` | `sakharov_xi_minimal_coupling` | §B.6.5 |
| RF-3 | Lepton-sector G-as-colour-Z_3 single-domain breakdown | Modus tollens: framework's commitment to spontaneous (not explicit) SSB on lepton mass operator is consistent with empirical Koide at `~10⁻⁵` — passes inside the band by ~5 orders | `koide_modus_tollens_consistency` | §C.3.9 |
| RF-4 | Cabibbo `f_perp` hypothesis | 0%-or-82% categorical fork, no few-percent branch. Closed NEGATIVE | `over_determination_scan` | §C.3.10 corollary |
| RF-5 | `V_PMNS = I` phantom prediction | Defused: substrate provides no amplitudes pinning PMNS; never was a TWT prediction. PMNS magnitude #1-gap GATED | `pmns_no_substrate_derivation` | §C.3.12 |
| RF-6 | ν-asymmetric reframing route | Counter-indicated by substrate-level checks | `neutrino_orbit_asymmetry_attempt` | §C.3.12 |
| RF-7 | Over-production test (predicted stable orphans) | Stable set `{γ, p, e, ν, stable nuclei, antiparticles}` matches observation exactly — no orphans, no gaps. Two reasons: SM's two topological charges exactly, internal multiplicity capped at 3 by 4D Z_3 | `topological_overproduction_test` | §C.5.8 |

RF-5 is a clarified-status removal (never a real prediction) and RF-6 an adjudicated negative
route; RF-1, RF-2, RF-3, RF-4,
RF-7 are substantive structural saves or positive empirical-coherence passes.

### E.3.3 Value-gated / coherence-class falsifiers

Falsifier-tier statements that cannot become single-detection kills until the #1 gap closes.
Each records the operational shape of an open commitment.

| # | Falsifier handle | Gated on | Operational form | Origin |
|---|---|---|---|---|
| VG-1 | `Im χ` budget (one dial, three pillars) | `Im χ` (#1 gap) | KSS floor `η/s ≥ ℏ/4π`; GW170817 ceiling `η ≲ 10⁹-10¹⁰ Pa·s` derived via Hawking `Γ ~ 16πGη/c²` from the multimessenger arrival-time bound; macromolecule decoherence floor. Bracket position (near KSS) is the framework's commitment. Same `Im χ` governs Bell decoherence (§B.4.5 Bell-memory bridge) | §B.4.5 + §D.5.4 |
| VG-2 | `Λ ~ H²` cosmological-constant residual | `Im χ` (Volovik equilibrium is zero; residual is the drive signature) | A measured value inconsistent with the driven-dissipative deviation from Volovik equilibrium falsifies the identification | §E.1.1 |
| VG-3 | `1/T_2` substrate-decoherence rate | `Im χ` / WP-IX4 | A measured `1/T_2` above the symmetry-protected boundary would falsify the symmetry-protection result | §D.5.5 |
| VG-4 | Dark-matter signatures (DM-V2-1) | (Mostly) outside V3 derivational scope; sterile-RH 3-prediction is structural | The 3 sterile RH neutrinos are structural; relic ~2% Ω_DM (47× shortfall); remaining ~98% out of scope. Laboratory detection of heavy sterile RH at Dodelson–Widrow `keV` window would falsify the `m_sterile = m_active ≲ 0.12 eV` Dirac-character prediction | §E.1.3 |
| VG-5 | Gravitational-wave dispersion at high `E` | dim-6 dispersion correction once GW propagation scale identified | Concrete prediction once the induced-EH propagator's effective `Λ` for the GW sector is computed (Paper-2) | §B.6.3 |

### E.3.4 Structural-coherence falsifiers

Coherence conditions that, if they fail to close, do not constitute external single-detection
kills but break the internal construction.

| # | Coherence condition | What fails if it doesn't close | Origin |
|---|---|---|---|
| SC-1 | Multi-defect well-posedness of the wavefront field equation | The Eulerian "atlas as projection artifact" reframing (§B.8.4) breaks; the multi-defect `Cl(4,1)` wave equation with `N` back-reacting topological sources not currently constructed. *Two `N = 2` static results exist (R-135 ansatz-reduced BVP; R-144 full-3D ansatz-free minimization, §C.1.2): the static two-defect sector is variationally coherent and strictly below threshold — the dynamical multi-defect EOM stays open (the condition's core face)* | §B.8.4, §E.1.2, §C.1.2 |
| SC-2 | Cell-order requirement: emergent D4 cell pattern carries local coordination WITHOUT coherent long-range space-fixed cubic orientational order | A space-fixed cell crystal would produce hadronic-scale `(E/f_π)²` anisotropy — load-bearing OPEN for §B.6.3 closure | §B.6.3 |

### E.3.5 Internal pre-mortem — three things to be wrong about

The four preceding categories list *external* detections that would kill the current
formulation. The complement is the **internal pre-mortem**: the three biggest structural
exposures inside TWT itself, where the framework could be right about its pillars and still fail
because a load-bearing construction does not close. These are not falsifiers in the E.3.1–E.3.4
sense (there is nothing to detect); they are *internal* places where the framework's own
machinery is loaded against open questions.

**(1) Gravity — sign-and-pillars right, achievability open.** §B.6 has structural geometry
closed conditionally and the sign derived, but the absolute coefficient is #1-gap-gated
through the texture tetrad's full nonlinear EH action. The framework commits to
the sign and the geometric pillars; if the substrate dynamics turn out incompatible with
delivering the texture tetrad's nonlinear EH action at the right coefficient, the gravity sector
forces a rework. The resolving computation is the explicit texture-tetrad construction feeding
into §D.5 dynamics.

**(2) Skyrme dressed-coupling — local-quartic vs phason-spoiled fork.** §D.4's dressed Skyrme
stabilizer reads `e ≈ √18/(D/J)` with branch-c phason non-locality explicit. Either (a) the
dressed EFT is clean local Skyrme (the favorable reading), or (b) the gapless phason
persistently spoils the local quartic. Under (b), §C.1.2's `M_0 = 36.47 f_π/e` is a re-fit,
not a derivation. The
resolving computation is an explicit phason-coupled effective-action calculation.

**(3) `c_meta = c` on average — global identity vs differential breakdown.** §A.4 commits
`c_meta = c` averaged across the wavefront. Local variations near mass concentrations are
predicted (§B.6, §B.7), but the GW170817 multimessenger constraint `|c_GW − c_γ| < 10⁻¹⁵` is
already tight. Sector-dependent or time-varying `c_meta` falsifies; the induced-gravity story
rides on the average identity, so any robust differential-`c` detection would break the
unified-frame picture rather than just trim a coefficient. Per the disclaimer above, this is the
one internal exposure that could plausibly reach the ontological premise itself: `c_meta = c` is
downstream of A-3 (wavefront / signature locking), and a robust differential-`c` finding would
force reformulation at the axiom layer rather than the derivation layer.

---

## §E.4 — What TWT contributes; landscape; Paper 2 agenda

The framework's content distilled to its synthesized headlines, situated in the intellectual
landscape, and pointed forward to Paper 2.

### E.4.1 Seven synthesized headlines

The framework's primary contribution is **geometric reinterpretation**: turning an SM postulate
or unexplained feature into a structural consequence of the substrate, with the numerical value
typically unchanged. Seven representative items:

- **Three generations are Frobenius**, not a free count. The three imaginary units of `ℍ` on the
  `V_4⊥` generation circle, identified with the anti-self-dual bivector triple. Frobenius
  forbids a fourth generation. The theorem is unchanged; the identification turns it into a
  generation-count theorem (§C.3.8).

- **`sin²θ_W = 3/8` at unification is native, not GUT.** The load-bearing substrate ingredients
  are (i) the D4 trivector charges that determine `Σ T_3² = 2`, `Σ Q² = 16/3`, and (ii) the
  Clifford trace bridge giving native `√(3/5)`. The cross-term `Σ T_3 · Y = 0` enters too, but as
  a *generic* SU(2)×U(1) doublet-Schur-lemma fact (§C.4.5(ii) honest scope) — its TWT-specific
  expression as grade-0 L⊥Q orthogonality is Cl-native phrasing, not new content. With those
  ingredients in hand, `g_1 = g_2` is enforced by D4 isotropy (the same theorem protecting
  Lorentz invariance, §B.1.4), and `sin²θ_W = 3/8` follows. SU(5) is removed throughout; the
  historical `24 = z(D_4) = dim(SU(5))` is a representation-theoretic match, not a load-bearing
  identification (§C.4.5).

- **The Tsirelson bound `S = 2√2` is the dimensional fingerprint of `S³ → S²` projection** — the
  half-angle `cos²(θ/2)` is the one-sided rotor action on a `Cl(4,0)` spinor, a substrate-level
  geometric fact (§B.4.1). QM gets the same value by axiom; TWT supplies the substrate reason.

- **Probability is not a primitive of the world.** The framework's cheapest claim, in the
  ontological sense: it needs no irreducible chance. The substrate is configuration-realist —
  at every moment the field has a definite configuration — and probability enters as a *derived
  measure* over that configuration space rather than as an axiom, with the Born exponent now a
  theorem given four named premises plus Gleason's theorem (§B.3.3). Standard quantum mechanics
  must postulate the Born rule and a primitive stochastic collapse; many-worlds avoids the
  collapse but owes the measure to contested branch-counting and pays in world-proliferation;
  Bohmian mechanics recovers determinism at the price of a dual particle-plus-wave ontology.
  Here there is **one field**: what reads as a particle and what reads as its wave are the same
  defect seen along orthogonal axes (§A.3), and the non-locality Bell's theorem forces is
  located — in the joint configuration the selection law takes as its argument — with nothing
  travelling and no signal sendable (§B.4.6). What remains open is the *mechanism* of
  single-outcome selection (§D.5, Role 3), so this is a structural commitment with a named open
  mechanism rather than a completed account of measurement; the measure itself is no longer
  assumed.

- **Parity violation and β-decay share one substrate parameter.** The same `D` that produces the
  Cabibbo angle, the generation phase, the Skyrme stabilizer, *and* parity violation also
  supplies the β-decay channel. The 4 no-shared-index `e_4`-bonds generate a topological boundary
  term linear in `D`, proportional to `I_4` — the substrate origin of parity violation. The
  electron in β⁻ is *created* as an L-winding excitation, not drawn from a pool; the mediator is
  the same `I_4` Hodge map. **One number, multiple manifestations** (§C.5.3, §C.5.7).

- **The Lorentzian signature of observed spacetime is the algebraic shadow of a
  wavefront-locked observer in a Euclidean substrate.** Not an independent postulate. The
  induced spatial frame `γ⁰ = e_4, γʲ = e_4 e_j` on `Cl(4,0)` satisfies the Dirac relations with
  signature `(+, −, −, −)`. One of the framework's two cleanest spine results
  (alongside charge quantization). Two of the most foundational features of relativistic physics
  — signature and conserved charge spectrum — fall out of the substrate algebra (§B.1, §C.2.8).

- **Matter is a defect.** The single load-bearing ontological commitment from which the
  framework's "primary contribution" character follows. Defects are configurations of one
  substrate rotor field; stability is topological, mass is meta-time rotor frequency, and Lorentz
  invariance is *protected* against the radiative species-splitting that plagues generic
  emergent-LI programs — one fundamental field, not `N` independent ones (§B.1.4).

**The pattern.** Each turns an SM postulate or unexplained feature into a substrate consequence.
The numerical value is typically unchanged; the *ontological status* shifts. What TWT does that
the SM does not is *answer the "why" questions* the SM cannot. What TWT does *not* do yet is
derive the coupling magnitudes, individual mass values, the CKM / PMNS angles, or absolute
scales — these are #1-gap-gated and live in the OPEN registry (§E.2.2).

### E.4.2 Intellectual lineage

The framework's foundational tools rest on several traditions:

- **David Hestenes** and the geometric-algebra program: the Dirac equation, complex structure of
  QM, spinor formalism, consolidated Maxwell — all admit clean Clifford expression. TWT departs
  in one decisive choice: Hestenes formulates physics in Lorentzian `Cl(1,3)` with time
  foundational; TWT formulates in Euclidean `Cl(4,0)` and recovers Minkowski signature as an
  emergent observer feature.
- **Koide** and the empirical lepton mass relation.
- **Brannen** and the `Z_3` parametrization of the Koide formula.
- **Skyrme** and topological solitons as particles.
- The geometric-algebra school, the lattice spin-system tradition, the Dzyaloshinskii–Moriya
  literature in condensed matter, and Sakharov's induced-gravity program.

*What V3 contributes over V2* and the *Paper 2 agenda* are administrative and forward-looking
meta-content; they live in the companion file (Section 7 Development log, and Section 11
Paper 2 agenda) rather than the body.

---

## §E.5 — A candidate for the #1-gap kernel

§D.5 named the framework's largest unbuilt object: the driven-dissipative substrate dynamics,
whose master dial is the transport function `Im χ(ω)`. This section proposes a concrete
**candidate** for it — not a derivation, but the execution of the closure route the companion's
Section 12 already sanctioned (**Class 2b**: a minimal counted-INPUT kernel family + registry
over-determination). It was produced by a dedicated selection campaign run on the
framework's numerical substrate testbench against the
engine's own acceptance inventory, with every phase
independently reviewed to consensus. It is proposed strictly as a
**candidate** — a surviving candidate *class*, not a single pinned kernel.

**The form (R-153).** `Im χ(ω)` is taken to be an odd, passive, Kramers–Kronig-causal function
with IR exponent `s ≥ 3` (the s=3 Adler/Goldstone floor, §D.5.5) and a UV cutoff — a
*constraints-by-construction* family in which causality, oddness, passivity, and the Adler floor
are exact by construction rather than imposed after the fact. Three spectral members share those
properties: a **nodal** (algebraic-edge) family `∝ xᵖ/(xᵖ+1)` with `x = |ω|τ` and `p ≥ 3`; an
**s-wave** (exponentially-gapped-edge) family; and their positive **composite** sum
`[nodal(p=3) + r·swave]/(1+r)`, in which a single measured ratio `r` interpolates the two edge
classes (R-154). On the candidate's substrate-native reading, the medium carries both a gapless
Goldstone sector (the s=3 face) and a Dzyaloshinskii–Moriya-gapped canting-magnon sector (the
dissipation edge), and `Im χ` is their sum; that constraints-by-construction survive the
positive summation is an exact algebraic fact (R-154).

**The counted economy (R-155).** The genuine dials are the IR exponent `p`, the edge width, the
UV plateau width `W`, and the memory time `τ_mem`; a redundant edge scale is exactly absorbable
and is not a dial. One binary INPUT bit fixes the memory branch as **hysteretic** — the
`weak = SD` pattern: the geometry offers the menu {hysteretic, fading}; the candidate picks
hysteretic, consistent with the working branch §D.5.3 already adopts on defect-persistence
motivation (a pick, not a derivation; the hysteresis and driven-response modeling ride
registered imports — companion Section 13, I-14/I-15). A minimal member is **two dials + one
bit**. These are
counted within the candidate's own ledger: they would join the framework's parameter ledger
(§E.2.1) only if the candidate is adopted; until then the #1 gap remains open exactly as §D.5
states it.

**Constraint provenance (R-156).** Every member passes the executable constraints of both
oracles — the substrate-testbench's gate bench and the corpus engine's acceptance
inventory — *by construction*. The engine's three channel *targets* — the
`(19/2)√38 ≈ 58.6` stiffness renormalization, the `Λ ~ H²` coefficient `≈ 2.05`, and the `≤ 4`
spin-2 `C_T` moments — are **not** fitted: their kernel→observable maps are themselves #1-gap
objects, so the candidate supplies their form-side inputs while the numbers stay gated. The
over-determination that would pin a single candidate therefore activates only once one of those
maps is built — the Class-2b promise, honestly conditional.

**What stays open — the reading-conditional rank-deficiency (R-157).** The candidate is a
**class**, not a single kernel. The executable constraints do not uniquely select within it:
under the framework's optimistic (two-sided) reading of the superallowed-flatness datum a plateau
class is preferred, but under the operative (one-sided ceiling) reading the flatness selects
nothing, and the fluctuation-side (`a_e`) discriminator confounds the memory scale with the IR
exponent in a free-scale search. The framework reports this honestly: the executable constraints
are rank-deficient (one usable anchor against a ≥2-dial kernel), exactly as the pending-values
registry already records. The discrimination is deferred to the virgin sectors below.

**The falsifiers it adds (R-158).** The candidate is falsifiable seven ways, pre-registered
before evaluation: (P1) a knee/edge in the μeV–meV anchor-free band
inconsistent with the superconducting-persistence ceiling; (P2) a precision fluctuation (`a_e`)
two-point ratio that does not match the fixed-scale exponent atlas; (P3) a knee·τ_mem that
violates the train-cadence relation once the barrier action is pinned; (P4) a knee falling
outside the mass-frequency containment bracket; (P5) a driven identity-transfer rate landscape
that is not activated; (P6) a viscosity-to-entropy ratio off the near-KSS bracket; (P7) a
generation sector that starves the dissipative route. It also adds a *structural* falsifier: an
edge-less (no-plateau) kernel is disqualified from sustaining identity transfer. On the current
data none of the evaluable-now
predictions is violated — at the compatibility level, not confirmation, since their numerics are
themselves gated — and the near-KSS commitment (§E.3.3 VG-1) **stands**. One jurisdiction hedge
is carried explicitly: the superconducting-persistence ceiling and the superallowed-flatness
datum are *inside-frame* data — they bind the outside-frame kernel only through the un-built
outside↔inside projection, and the numeric comparisons gate on exactly that leg.

This is what the framework can honestly offer toward the #1 gap today: a named candidate class
with counted economy and pre-registered falsifiers, where §D.5 previously named only a hole. Its
value magnitudes remain gated; its selection remains a Paper-2 task.

---

## §E.6 — Closing

The framework's claim is **measured**. One continuous medium with a discrete D4 substrate and a
propagating wave reproduces the structural skeleton of known physics from fewer independent
inputs than the Standard Model requires, and the reduction is genuine rather than cosmetic. The
V2 → V3 ontology (matter = defect; spatial winding and meta-time rotor as two faces of one
circular object linked by `I_4` Hodge duality) does the work the earlier modeling apparatus was
doing — and does it more cleanly.

The quantitative theory that would complete the framework is **not yet in hand**. The open
frontier concentrates onto a single value gate (the `S` coefficient / `Im χ`) plus two structural
gates (texture tetrad, QCD UV gate). The pending-values registry (companion Section 4) surfaces
the collective constraint these gates jointly carry; closing the #1 gap unlocks most of the
registry's left column.

What this paper offers is the **structural framework**, an explicit account of what within it is
derived and what is open, and the methodology by which the distinction is maintained. The
falsifier table (§E.3) names what would kill the current formulation; the parameter reduction
(§E.2.3) states its case; the pending-values registry names what remains
open. Each is honestly labeled.

*Time is a wave. We're riding it.*

---

# Annexes → companion file

*All annexes, the back-of-book bookkeeping (Result Index, Dependency Graph, Engine ↔ Paper Map,
Pending-Values Registry), the geometric-reinterpretation catalog, the methodology principles,
the development log, the stable-spectrum enumeration, the wave-phase stability ladder, and the
bibliography — are consolidated in the companion file:*

**`TWT_foundational_paper_companion.md`**

The companion file contains thirteen sections:

1. **Result Index** — every R-NNN result with tier, engine primitive, target section, dependencies.
2. **Dependency Graph** — layered picture of axioms → algebraic → dynamical → deep gates.
3. **Engine ↔ Paper Map** — `twt.py` primitive ↔ paper section cross-reference.
4. **Pending-Values Registry** — open items by kernel object.
5. **Geometric reinterpretation catalog** — the nine items (Tsirelson, Weinberg 3/8, Bohr, GA Maxwell, α, Frobenius, parity-D-decay, electron smallness, Lorentzian signature).
6. **Methodology principles** — the eight principles, with canon-successor mapping.
7. **Development log** — V1 → V2 → V3 history and the review-round catches.
8. **Stable-spectrum enumeration** — the over-production `(B, L)` table.
9. **Wave-phase stability ladder** — 20 states across 9 orders of magnitude in `N = m/Γ`; π⁰/π± discriminator.
10. **Bibliography** — consolidated citations.
11. **Paper 2 agenda** — the forward research program.
12. **Closability classification** — every open item classified by what actually blocks it, with the realistic closure route.
13. **Import Registry** — every load-bearing external theorem: premises, level applied, ontology status, retirement handle, revert clause.

The companion file additionally opens with the **diff-of-intent (V2 → V3)** memo. Load it
alongside this paper for the full picture.

---

# End-of-draft note

Parts A, B, C, D, E are all drafted prose. The full V3 paper — from the Opening through §E.6 —
is readable end-to-end, with all R-NNN markers grounded in the Result Index and all forward
references resolving. All annexes and back-of-book bookkeeping live in the companion file
`TWT_foundational_paper_companion.md`; the engine suite (`twt_test.py`) is the executable
cross-check, with the current check count and per-result engine cites tracked in the companion.
V2 is archived at `knowledge/corpus/archive/V2/` (2026-07-01).
