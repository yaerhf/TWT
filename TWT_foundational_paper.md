# Time-Wave Theory — the V3 Instance Dossier

### The first candidate of TWT-Core, at full technical depth: Parts A–E

*Yaer Aharon Haddad Fennech · Independent Researcher · hfyaer@gmail.com*
*Engine, verification suite, and all three documents: **https://github.com/yaerhf/TWT** —*
*`pip install -r requirements.txt && python twt_test.py` reproduces every algebraic claim below.*

**What this document is, and which one to read first.** This is the **instance dossier**: the
complete technical development of **V3**, the first candidate member of the TWT-Core family, in the
substrate machinery it is built on — the picks in full, the calibrations, the mass, charge, gauge
and mixing material, the open dynamics, and the wounds at full depth. It is the family's technical
corpus, and it is the document that carries every `(R-NNN)` result marker.

**The family itself is stated elsewhere, and that is the entry point.** The seven axioms and the
one refusal, what the family derives with no candidate at all, what that costs measured against the
alternatives, what would kill it, and where this candidate is wounded — those are the **Core
paper**, `TWT_core_paper.md`, which cites this dossier by section for everything instance-specific.
A reader meeting the programme for the first time should read the Core paper first and come here
for the depth behind any of its claims. Nothing below is superseded by it: the Core paper is
shorter, not newer.

*This dossier ships with a **companion file** — `TWT_foundational_paper_companion.md` — that consolidates
all annexes, the back-of-book bookkeeping (Result Index, Dependency Graph, Engine ↔ Paper Map,
Pending-Values Registry), the geometric reinterpretation catalog, the methodology principles,
the development log, the stable-spectrum enumeration, the wave-phase stability ladder, and the
bibliography. Load both together for the full picture; the paper file is pure physics narrative.*

---

# Abstract

**What this is.** A structural-derivation programme, not a completed theory: a framework in which
observed physics is the inside view of a four-dimensional Euclidean substrate — a D4 lattice of
unit Clifford rotors carrying a wave that advances along a distinguished axis. Observers are
wavefront-locked configurations of the wave; matter is a topologically protected defect of the
rotor field; mass is the frequency of the defect's meta-time rotor. One object is named as unbuilt
from the outset — the driven-dissipative substrate dynamics (§D.5) — and it gates every coupling
magnitude and absolute scale in the framework. The claims are about *structure*: which
Standard-Model facts follow from which premises, at which explicitly audited status.

**What the object is.** Not one theory but a **family and its first candidate**. **TWT-Core** is
the family — seven axioms and one refusal, stated in full at §A.6 — and what this paper develops
is **V3**, the first candidate instance built all the way down to numbers. The lattice
arrangement, the bond truncation, the calibrated ratios, the gravity route and the hadron toolbox
are **instance-level** picks, each with a recorded menu and a recorded revert condition; so are
both of the already-measured exposures named below. The programme's deliverable at family level is
the list of surviving candidates, and V3 is its first entry. The Core is not vindicated by
carrying neither wound: it carries neither because it makes no numerical claim at either place.

**What is derived, at its strongest.** From four counted substrate inputs plus the measured Newton
constant (an amplitude input cancels in ratios; one hadron-sector determination is counted
provisionally — §E.2.1): the Lorentzian signature of observed spacetime as posit plus forced
implication (`Cl(4,0) ≅ Cl(1,3)` is a theorem; the timelike placement is an input); quantum
mechanics' postulate structure from one geometric projection, with the Born exponent a theorem
given four named premises plus Gleason's theorem (an import), and the Tsirelson bound `2√2`
exact given the standard tensor-product state space — which the framework assumes rather than
constructs; electromagnetism with the monopole absence conditional on the winding-as-source
identification; induced gravity with the sign derived and `γ = 1` structural; charge quantization
from topology — winding number is an integer, so the charge spectrum is discrete and the
proton–electron equality is protected rather than tuned — together with hydrogen neutrality as an
identity in the charge normalization constant, holding for every value of it, which turns the
`10⁻²¹` neutrality measurement from a calibration into a test, with its condition that the
*assignment* of values across the 15-state spectrum rides four named structural premises and an
entered anchor;
a three-generation count that is a dimension count of four-dimensional space, conditional on one
named identification plus an associativity premise; `sin²θ_W = 3/8` as a native normalization
identity at the scale where the two electroweak stiffnesses coincide; and a matter-stability triad
(no proton decay, Dirac neutrinos, no `0νββ`) from one conservation law. Probability is not a
primitive: the framework is configuration-realist, and what standard quantum mechanics postulates
is here computed, with the single-outcome mechanism and the Born distribution both named open.

**The strongest objections, stated first by us.** Two already-measured exposures are named up
front, and they are independent failures. The isotropic dimension-six Lorentz-violation
coefficient's natural value at the substrate's own lattice scale is excluded unconditionally by about one order of magnitude (a single model-independent cosmic-ray analysis, superluminal branch), and by six to seven orders only under a mass-composition assumption the same observatory's data disfavours (direct gamma-ray limits contribute nothing at this operator dimension) — and that coefficient is
gated on the open dynamics (§E.3.5(4)). The electroweak crossing scale is not gated at all: the
framework simply has no derivation of it, and its own lattice-scale reading lands a third below
the measured `sin²θ_W(M_Z)` (§E.3.5(5), §C.4.5, N55). We regard these as the most likely routes
by which the framework is wrong, and we would rather they were tested than overlooked.

**How to check it.** Every numbered result carries an auditable tier in a companion result index;
the algebraic content is backed by an executable, public verification suite in which the
quantities the framework cannot compute raise exceptions rather than return numbers
(https://github.com/yaerhf/TWT).
A passing suite is a statement about Clifford identities and bookkeeping, not evidence about
physics; where a section's conclusion outruns what its engine primitive asserts, the paper says so
at that section.

---

# To the reviewer

**Scope.** This is not a claim to a completed unified theory. It is a structural-derivation
programme with one explicitly named unbuilt object — the driven-dissipative substrate dynamics of
§D.5 — which gates every coupling magnitude and absolute scale in the framework. No coupling
magnitude or absolute scale here is independent of that gap. The claims are about structure: which structural facts
follow from which premises, and at what status.

**The architecture — a family, and the first candidate that realizes it.** Read §A.6 before
Part B. The programme is **TWT-Core**, a family fixed by seven axioms and one refusal, together
with a list of candidate members; this paper develops **V3**, the family's **first candidate
instance** and the first one built down to numbers. Three consequences for a reviewer. (i) The
picks are visible and reversible: eleven of them (three carrying recorded sub-choices), each recorded with the menu it came from and
what un-picks it (§A.6.4) — the D4 arrangement and the `{J, D}` bond truncation among them, so
two of the Opening's own premises are instance-level rather than axioms. (ii) Both already-measured
exposures in the table below belong to V3, not to the family: they ride pinned choices, and the
Core carries neither. (iii) That is not a defence. The Core carries neither wound because it makes
no numerical claim at either place — a family that has not yet said a number cannot be wrong about
one — and V3's wounds are the price of being the only member that says numbers at all. What the
family *does* carry is a single total kill condition (§A.6.2), deliberately taken.

**Read the tiers, not the register.** Every numbered result carries an `(R-NNN)` marker whose tier —
DERIVED, INPUT, FIT, CANDIDATE, FRAMING — is recorded in the companion's Result Index, together with
its dependencies and its engine primitive. Where the text reads CANDIDATE it is a proposal, not a
claim. Seven premise rows (thirteen-plus named premises) condition otherwise-derived results; they are listed with
their discharge conditions at §E.2.2. Where prose register and tier label disagree, the tier label
is the claim.

**Development method, stated plainly.** This paper was produced with AI assistance under the
protocol described in the Methodology section and companion Section 6. The magnitudes it does not
deliver are gated for a stated reason of knowability rather than left undone: the exact microscopic
kernel of a driven medium is underdetermined from inside the lock in principle, so what is reachable
is a compatible effective kernel class with a small counted constant set, and the deliverable is a
family of surviving candidates rather than one kernel — empirically bounded, because nothing in hand
excludes the members that would also have worked. The risk the protocol actually carries is an
instrument that generates findings about itself faster than the physics moves; the counter is the
published ratio of premises interrogated to premises discharged, and the tier system, the executable
suite and the import registry exist to keep both checkable rather than assertable.

**Our own strongest objection, stated first.** The framework's natural value for the isotropic
dimension-six Lorentz-violation coefficient is excluded unconditionally by about one order of magnitude (a single model-independent cosmic-ray analysis, superluminal branch), and by six to seven orders only under a mass-composition assumption the same observatory's data disfavours, and we cannot presently compute the suppression the conditional corner would require. It heads the
table below, with the second already-measured exposure beside it.

**Four checks, five minutes each.**

1. `git clone https://github.com/yaerhf/TWT && cd TWT && pip install -r requirements.txt && python twt_test.py`
   *(The research apparatus itself — the rules, roles, gates and telemetry the programme runs
   on — is published in the same repository's `apparatus/` directory; companion
   Section 6.)*
   — expect `ALL CHECKS PASSED` (on Windows, set `PYTHONUTF8=1` first). The suite is executable
   and public.
2. §B.1.5's lattice result: the full automorphism group of the D4 root system (order 1152, `= W(F4)`,
   invariant degrees `{2, 6, 8, 12}` — the triality premise P-pg) has a one-dimensional degree-four
   invariant space, so the quartic dispersion term is forced isotropic. Checkable against any
   reference on F4 invariant theory; self-contained and independent of the rest of the framework
   (prior art credited in place — Neuberger 1987; Chow 1999; Katz & Nogradi 2025).
3. Pick any `(R-NNN)` at random and trace it: Result Index → Dependency Graph → engine primitive →
   test. The bookkeeping is meant to survive spot-checking.
4. Confirm that the gated primitives raise rather than return: `alpha_em_value()`,
   `qcd_collider_phenomenology()`, `texture_tetrad()`. Where the framework cannot compute, it is
   designed to fail loudly.

**Published negatives.** Sixty-plus dead ends and located gaps are recorded as
tried → failed-because → would-change-if entries in the negatives ledger shipped with this paper
(`TWT_NEGATIVES_LEDGER.md`; N0–N57 with primed variants) — including closed routes through the
framework's own favoured constructions. They are published because closed doors are useful to
others working the same territory, whether or not this framework survives.

**Prior art and lineage.** Related programmes reach related conclusions by different means; §E.4.2
records the intellectual lineage, and prior art the programme itself surfaced is credited at its
use-sites (Neuberger 1987 and Katz & Nogradi 2025 at §B.1.5; Gatto–Sartori–Tonin 1968 at §C.3.10;
Sumino 2009 at §C.3.3a). The comparison against adjacent programmes is at §E.4.2 —
Trayling–Baylis; Lasenby–Doran–Gull; Plebanski/Urbantke/Krasnov; Furey; Chisholm–Farwell;
Boyle–Farnsworth — developed independently, with the specific deltas at §C.4.5 and §C.3.8 and
primary-verified records in companion Section 10.

**What would kill this — and what it does not predict.** The framework is at present **more
falsifiable than predictive**, and the distinction matters. It makes no unconditional novel
prediction of a coupling magnitude or an absolute scale: those are where novel numbers would
come from, and every one of them is downstream of a single named unbuilt object — the
driven-dissipative substrate dynamics of §D.5 and the `Θ_rel` residual. That is a stated debt
with a named source, not an oversight, and no restatement of the structural results discharges
it. What the framework stakes instead is a set of prohibitions, and two places where the
measurement already exists and the framework is behind.

Read the table at two levels. Three rows are **instance-level**: the two **already-measured**
rows — each rides choices V3 pins (a regular lattice at a back-fit size, one induced-gravity
chain, the instance's calibrations), and a family member that goes another way at those nodes
inherits neither — and the propagation-speed row, which rides this candidate's `c ↔ c_meta`
identification. The three prohibition rows are **family-level**: they follow from the axioms, or
from the axioms plus a stated preferred direction, and a positive detection on any of them
reaches every candidate.
§E.3 carries the level for all sixteen falsifier rows; §A.6 gives the architecture.

| The exposure | What it kills | Where it stands |
|---|---|---|
| **Already measured** — the isotropic dimension-six Lorentz-violation coefficient | any completed §D.5 dynamics that fails to deliver a suppression of about one order unconditionally (six to seven under the disfavoured pure-proton conditioning) — historically quoted as three to nine orders — dead on arrival, not evolved | The coefficient is gated on the open dynamics, so the framework asserts no value for it; what existing cosmic-ray and gamma-ray limits exclude is its *naive* value at the substrate's own lattice scale, and they bind every future completion (§E.3.5(4), §E.3.3 VG-6) |
| **Already measured** — `sin²θ_W(M_Z) = 0.2312` | the framework's own lattice-scale descent | Its one computable reading lands `0.154–0.158`, a third below the measured value; the four standard escape routes are computed and closed. Descent and closures alike ride the imported elementary-field RGE premise (`I-6`) for a gauge sector this candidate holds emergent / composite at `Λ_L`; were it to fail, the reading returns from refuted to gated (§E.3.5(5), §C.4.5, N55) |
| Proton decay | topological protection of baryon number (`B ∈ π₃(S³) = ℤ`) — exact in the smooth sector; a grainy member carries a resolution condition (the winding rides the arrangement, deficit ∝ 1/ρ²) | Super-K, Hyper-K, DUNE. The framework's one distinctive forward bet: grand unification expects decay at *some* level, and this framework forbids it in the smooth sector — non-perturbative violation respects `ΔB = ΔL = 3` (§C.1.5, §C.5.6) |
| Neutrinoless double beta decay | exact `B − L` conservation, and with it the Dirac neutrino character that conservation forces | KamLAND-Zen, LEGEND, nEXO, CUPID (§C.3.12, §C.5.6). What does *not* die with it: anomaly cancellation is a trace identity on the charge assignment, untouched by a broken conservation law (§C.5.4) |
| A sterile neutrino at any mass far above the active scale | the Dirac-partner mass tie `m_sterile = m_active` at the sub-tenth-eV cosmological scale (`≲ 0.12 eV` at the Planck + BAO bound, `≲ 0.064 eV` under ΛCDM at the current DESI bound, `≲ 0.16 eV` once the dark-energy equation of state is freed) | KATRIN's kink search, extended into the keV range by the TRISTAN detector upgrade (§E.1.3, §E.3.3 VG-4) |
| A sector- or epoch-dependence of the observed propagation speed `c` against the lock rate `c_meta` | this candidate's identification of the observed `c` with the average lock rate (the `A-3`-downstream chain) — the axioms state no rate and no uniformity, so on a positive detection it is `c`, the emergent observer-side speed, that carries the non-uniform label, and the axioms stand | Precision multimessenger astronomy. An instance-level exposure: a candidate that pins the `c ↔ c_meta` identification differently re-derives or loses it, and the family's only total kill condition remains the foliation axiom (§E.3.5(3)) |

Rows three and four are independent experiments but a single underlying derivation: in this
framework proton stability, Dirac character and the absence of `0νββ` are one structural fact
(R-089), and the two rows probe it through different mechanisms — topological winding versus the
conservation law. §E.3 carries the full sixteen-row falsifier table, including the
consistency-class and floor-gated rows deliberately kept out of this one.

**What it costs to buy this.** The Standard Model carries 19 free parameters (26–28 with
neutrinos). This framework carries four counted substrate inputs — the cell mass scale, the
chirality ratio, the measured Newton constant, and one hadron-sector stabilizer counted
provisionally — and pins **zero of the 19 unconditionally**; one conditionally, and two more
only if a route this programme itself records as currently refuted is repaired. Its output is on the structural axis, not the magnitude axis
(§E.2.1, §E.2.3) — it converts Standard-Model postulates into substrate consequences, and does
not pretend to have bought magnitudes.

Structure has been proposed before its dynamics before: Minkowski's spacetime geometry preceded
general relativity by seven years, and Einstein dismissed it as superfluous learnedness before it
became indispensable. That is a statement about stage, not about merit. We would rather be shown
wrong on a specific claim than credited on a general one — and the place to start is the two rows
above where the framework is already losing.

---

# A note to the reader before you start

**This paper is organized from solid to speculative, not from axioms to consequences.**

The traditional foundational-paper shape — premises, derivations, corollaries, open problems — is
honest, but it forces the reader to wade through machinery before meeting the result it serves.
This paper inverts that. Part A states the ontology in plain language, gives just enough algebra
to read on, and closes at §A.6 with the architecture: which of the paper's commitments are
**family-defining**, which are **preferred directions**, and which are **picks belonging to V3,
the first candidate instance** — the level a claim sits at is not recoverable from the derivation
alone, so it is stated once, in one place, before the derivations start. Part B uses it: emergent Lorentzian signature, special relativity, quantum
mechanics, Bell, electromagnetism, the fine-structure constant, gravity, the cosmic frame,
the macroscopic limit. These are the framework's most solidly derived results, and they are what
the rest of the paper exists to support.

Parts C and D then do the engineering. Part C derives Standard-Model structure (charges, three
generations, the gauge group). Part D opens the substrate: the Clifford algebras in full, the D4
grain layer, the wave equation, and the open driven-dissipative dynamics — the framework's #1
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
(Section 12), the Import Registry (Section 13), and the **Core / Instance bookkeeping**
(Section 14) — which result belongs to the family and which to the first candidate, the
falsifier levels, and the dated history of the split that §A.6 states without dates. **Load the
companion alongside this paper for the full picture.**

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
premises; the unstarred IDs `A-1a/b/c, A-2, A-3` are the Opening's structural premises. **They are
not all at the same level**, and §A.6 states which is which: `A-1a`, `A-3`, `A-1*` and `A-2` are
family-defining, while **`A-1b` and `A-1c` are picks belonging to the first candidate instance**
— an arrangement chosen from a menu of arrangements, and a two-constant truncation of a
ten-constant menu. Three further family-defining commitments do not appear as Opening premises
because they are developed later: the signature placement `e_5² = −1` (§A.5.6, §D.1.3), the local
state at a site (six real parameters, §D.3.2), and the identification of the preferred foliation
with the cosmic rest frame (§B.4.5, §B.7).

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
  A structural premise at the cell layer (§D.3) — and an **instance-level pick**, chosen from a
  menu that also contains irregular-discrete arrangements and a continuum medium with a cell
  scale (§A.6.4, node V3-1).
- **(A-1c) — Two bond couplings.** Symmetric exchange `J` on all 24 NN bonds; Dzyaloshinskii–Moriya
  `D` on the 12 `e_4`-bonds. The ratio `D/J ≈ 0.79` is INPUT, calibrated to the lepton sector.
  Also **instance-level**: the pair is a two-constant truncation of the ten-constant menu the
  driven point group allows, and the `e_4`-only support of `D` is a second pick inside the first
  (§D.3.3; §A.6.4, nodes V3-2 and V3-2a).

**Empirical inputs** (the framework's parameter ledger), ordered by structural weight:

- `weak = SD` — one bit, but **not a free one, and not a choice**. The menu of three-dimensional
  subalgebras that could host weak isospin is computed and closed at three entries, two of which
  are refuted: one is the same assignment under a mirrored orientation, the other charges the
  right-handed fermions, which are observed to be weak-isospin singlets (§C.4.2, R-171). What the
  sector actually costs is an **endorsed structural premise** — that weak isospin lives in a
  three-dimensional `su(2)` inside the substrate's own rotation algebra at all, which this paper
  does not derive and which is a **preferred direction** of the family (§A.6.3) — plus **one
  empirical bit the framework reads rather than tunes**. Given those, V−A, generation-blindness,
  the doublet and `up = SD` follow. The assignment itself is neither an axiom nor a preference; a
  candidate diverges here by going the other way on the endorsed premise, not by assigning the
  weak factor elsewhere within the substrate's rotation algebra.
- `G_N` — the measured Newton constant, the gravitational anchor. Both cutoff scales
  (`Λ_S = √(2π) M_Pl`, the Sakharov scheme variable; `Λ_L = 1/a`, the grain spacing) are
  **back-fits of measured `G`** through the induced-gravity form, not independent inputs.
  Planckian within a factor of a few.
- `f_π ≈ 129 MeV` — the cell-scale mass scale. **This is the ANW *fitted* coupling, not a
  measured constant**, and `f_π` denotes it throughout this paper: it is the value Adkins, Nappi
  and Witten obtained by fitting the Skyrme model to the nucleon and `Δ` masses, and in their own
  normalization the physical pion decay constant is `F_π ≈ 186 MeV` — so the number carried here
  sits about 30 % *below* the measured one. Its proximity to the measured `f_π⁺ = 130.2(1.7) MeV`
  is a collision of two normalization conventions, not an agreement, and the two must not be read
  as the same number. Where the fitted value feeds a *physical* estimate rather than an internal
  Skyrme relation, the use-site says so.
- `D/J ≈ 0.79` — chirality ratio (calibrated to leptons; cross-checked by baryon sector). An
  instance-level calibration whose referent rides the `A-1c` truncation: if the discarded channel
  is non-zero the number re-reads as a measurement of a combination (§D.3.3; §A.6.4, node V3-4).
- `c = √2` ⇔ Koide `K = 2/3` — Brannen phase coefficient (exact-but-unforced). A **preferred
  direction**, not an axiom (§A.6.3).
- `A` — lepton amplitude scale (free Koide calibration; cancels in ratios).

The scale inputs are instance-level in the same sense: `f_π` and the Skyrme stabilizer are this
candidate's anchoring choices (§A.6.4, nodes V3-3 and V3-5), and the measured-`G` anchor
*practice* — anchoring on a measured constant and back-fitting the substrate scale from it — is a
preferred direction of the family, while the particular induced-gravity chain that converts it
into a Planckian cutoff is a pick (node V3-6).

(Counting convention: **four counted substrate inputs plus measured `G_N`** — `Λ` is not counted
separately since both `Λ` scales are back-fits of `G`, and `A` cancels in
ratios and is not counted. The ANW Skyrme stabilizer `e = 5.45` is counted **provisionally** as a
same-object determination pending the scheme-label question; §E.2.1 states the
full convention.)

**Units convention.** Throughout the paper, *natural* units are the default: `c = ℏ = 1`, so
`m = ω` is read literally (R-007), substrate frequencies and masses share a scale, and grade-0
inner products are bare numbers. Explicit `c` and `ℏ` are restored in two situations only:
(i) when a formula is being compared to data quoted in SI / lab units (e.g. `ω = m_e c²/ℏ` when
the electron rest energy is on display); (ii) when the Maxwell-table laws are written in the
mixed-grade form readers expect from EM textbooks. Both are local restorations for legibility,
not switches of convention.

Everything else the framework claims as structure — three generations, `sin²θ_W = 3/8` (at its
§C.4.5 crossing-scale scope), charge
quantization, the L/Q split, the Skyrmion's winding label, fractional quark charges, the
Lorentzian signature itself — is a consequence of these premises and inputs, derived in the body.

---

# Methodology — how this paper was developed

This paper is the product of a structured workflow combining a developer (Claude) with an
adversarial reviewer dispatched in a fresh context, plus an automated suite (`twt_test.py`) that
checks all engine-banked algebraic results on every revision. **The engine and suite are public**
(https://github.com/yaerhf/TWT): the reader is not asked to take any algebraic claim on trust, and
the primitives that gate underived magnitudes raise rather than return, so the framework's own
limits are executable too. No load-bearing claim is banked on
the developer's say-so alone: each is attacked by an independent reviewer, verified on the
substrate engine where applicable, and only graduated when developer and reviewer agree on its
tier and scope. The discipline is described in companion Section 6; companion Section 7 records
what it has caught — algebra bugs, precision overstatements, citation slips, and one undelivered
forward dependency — round by round, so the claim that the protocol works is inspectable rather
than asserted. The Result
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
| `q_h(τ_5) = exp(m τ_5 û/2)` | Meta-time rotor of frequency `m = ω` (= mass); `û` unit element with `û² = −1`. The simple (single-plane-angle) `û` is the leading ansatz; the general defect rotor carries two plane angles and is a product of two such exponentials | §A.4 |
| `J`, `D`, `D/J` | Symmetric exchange / Dzyaloshinskii–Moriya couplings on D4 bonds; `D/J ≈ 0.79` calibrated to leptons | §D.3.3 |
| `f_π ≈ 129 MeV` | Cell-scale mass; substrate condensate identification. The **ANW fitted** coupling (~30 % below the physical `F_π ≈ 186 MeV` in ANW's normalization), not the measured pion decay constant | §D.4.1, Opening inputs |
| `Λ` | Substrate cutoff; Planckian within O(1) | §D.3.5 |
| **ANW** | Adkins–Nappi–Witten Skyrme-model phenomenology | §C.1.2 |
| **BVP** | Boundary value problem (the Skyrme variational equations) | §C.1.1 |
| **QCP** | Quantum critical point — the L-orbit critical balance `D = J` underlying the L-orbit stiffness scaling | §C.1.6 |
| **`δ_L`** | Brannen lepton phase; `δ_L = (1/3) arctan(D/J) = 12.73°` at the lepton-calibrated `D/J ≈ 0.787` | §C.3.5 |
| **`Θ_rel`** | FDT-violation residual on the coset-Cartan channel; the framework's highest-value target | §D.5.6 |
| **`Im χ`** | Substrate transport function; the #1 gap's master dial | §D.5.4 |
| **KSS** | Kovtun–Son–Starinets viscosity-to-entropy lower bound `η/s ≥ ℏ/(4π)`; the substrate sits near this floor | §E.3.3 VG-1 |
| **FDT** | Fluctuation–dissipation theorem; its violation residual is `Θ_rel` | §D.5.6 |
| **R-NNN** | Numbered result, looked up in the Result Index (Section 1 of the companion file) | throughout |
| **signature `(n₋, n₊)`** | Metric signature written as (negative, positive) eigenvalue counts — i.e. (timelike, spacelike) in the mostly-plus convention `η = diag(−1, 1, 1, 1)` used in §B.6, so `(1,3)` is one time and three space and all-timelike is `(4,0)`. Distinct from the Clifford `(p, q)` label of `Cl(1,3)` in §B.1, where `p` counts generators squaring `+1` and `η = diag(+1, −1, −1, −1)`. The two conventions describe the *same* physical signature by opposite sign conventions, but the Clifford algebra TYPE is convention-sensitive (§B.1.2: `Cl(1,3) ≅ M₂(ℍ)` while `Cl(3,1) ≅ M₄(ℝ)`) — so check which convention is in force before carrying a `(1,3)` across sections | §B.1 / §B.6.6 |
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
preferred frame exists for electromagnetic propagation. TWT does not answer this by denying
that the substrate has a rest frame. It has one, and the framework says which: the `τ_5` foliation
the wave advances along, identified — as a testable claim (R-031) — with the cosmological comoving
(CMB) frame (§B.4.5); and defects do carry a worldline velocity through that medium (§B.5.5,
R-124). What Michelson–Morley measured is nevertheless zero here, for a **dynamical** reason rather
than an ontological one: observers and matter are defects of the *one* rotor field, so every
species inherits that one field's light cone and there is no independent coefficient for a
relative-boost violation to live in — relative-boost Lorentz violation is structurally zero rather
than tuned (§B.1.5, R-016, a structural identification), which is why the relative-boost row of
§B.6.3's face table reads exactly zero (the rotational-anisotropy faces close by a separate
argument, the D4 point group, R-165). That closes the aether's failure mode; it does not close the
question. What these protections do not reach is the rotationally invariant dimension-six residual,
whose coefficient the framework cannot presently compute and which is carried as an **open
exposure**, not a passed test (§B.6.3, §E.3.5(4)).

---

## §A.2 — The wavefront and the observer

A wavefront — the locus of constant phase of the wave — is a three-dimensional hypersurface within
the 4D bulk. Topologically it is the three-sphere `S³` — the *domain* of the
defect map, not a group: the spatial slice compactifies to `S³` under the asymptotic boundary
condition `R(∞) = 𝟙` that defines matter (§C.1), allowing topological winding numbers to classify
matter (R-002). The group-theoretic structure sits on the map's *target*, and that target is the
medium's local state space: the **4D-orientation class**, six real parameters (§D.3.2), whose
`π_3` is `ℤ × ℤ` — two independent windings. The count is insensitive to whether the `ℤ₂` sign
belongs to the local state or to the emergent covering sector, since a double cover is an
isomorphism on `π_n` for `n ≥ 2` (engine: `pi3_orientation_class_two_windings`).

*Inside* that one target sit the two **sector winding targets** the framework actually maps into:
the lepton subgroup `exp(𝓛) = Spin(3)` and the baryon coset `Spin(4)/Spin(3)`. These are
three-dimensional winding targets *within* the six-parameter state space — two topologically
distinct map types, kept apart at §C.1.1 and §C.1.3 — and not competing declarations of what the
state space is. Reading a *general* configuration in that sector basis requires a choice of
splitting that the framework has not made; §C.1.3 states that residue in full.

The "two ℤ" come most directly from the **chiral factorization**
`Spin(4) = SU(2)_+ × SU(2)_−`, where the two factors are the Hodge-eigenvalue (self-dual / anti-self-dual)
halves of the bivector algebra. The framework's *working* basis is a different one: the
**L-orbit / Q-orbit split** by `e_4`-content (§A.5.2), with leptons winding into the L-orbit
and baryons into the Q-orbit. The two decompositions are genuinely distinct — the self-dual
bivector `e_{12} − e_{34}` mixes one L-blade with one Q-blade, so `𝓛 ⊕ 𝓠 ≠ SU(2)_+ × SU(2)_−` as
decompositions of `so(4)`. **The relabeling from chiral basis `(n_+, n_−)` to orbit basis
`(n_L, n_Q)` is justified by a symmetric-pair / fibration bridge, given at §A.5.2.** Treating
them as the same split is the most error-prone conflation available here; the
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
spatial coordinates. We will see in §A.4 that spin and the rotor frequency we call mass act on the
same blades by *different actions* — spin two-sidedly, mass one-sidedly — algebraically separable
as observables, but in matter they are two faces of one defect, dynamically coupled through the
circular structure of §A.3.

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
spinor minimal left ideal `𝒮` (§A.5.4). **This homogeneous form is the twist-gauge reference, not a
claim that the ground state is featureless**: it is the rotating-frame representative in which the
helimagnetic spiral is absorbed into a field redefinition, so the reference value carries no
`x`-dependence — see the note on what "vacuum" means at §D.4.6. The substrate's ordered ground
state is *canted*, not fully aligned — a small canting angle quantifies the chiral-symmetry
breaking that the framework's hadronic-sector
derivations rest on. (The numerical specifics — the `D/J` calibration, the
Luttinger–Tisza spiral pitch — sit at §D.3 / §D.4.)

**Matter is a defect** in the wavefront's rotor field — a configuration that fails to match the
homogeneous vacuum (R-004). Geometrically: the rotor orientation is deflected from the surrounding
canted vacuum, and the deflections compose around the defect into a topological winding that
cannot be continuously undone to uniformity. The framework names the deflection a **lack of spin** — spin
orientation missing relative to the vacuum's homogeneity. The winding is an integer in `π_3(S³)`
for baryons (the L/Q split of §D.2 routes the winding to the Q-orbit) or the Hopf invariant `H = 1`
for leptons (routed to the L-orbit; §C.1).

The wave-level ansatz for an isolated defect:

> `Ψ_a(χ, τ_5) = F(χ) · B_a · s_0 · q_h(τ_5)`,

with `F(χ)` the spatial profile (the localized winding pattern), `B_a` a grade-3 blade specifying
particle type (§C.2), and `q_h(τ_5)` a meta-time rotor of frequency `m = ω` (§A.4).

**Which part of this is family-defining.** *Matter is a defect* is an axiom (§A.6.1, S4), and so
is the medium being driven, which is what the carrier picture above rests on. The **class** of
defect is not: reading the defect as a topological knot of Skyrmion type — the volume-twist class
— is a **preferred direction**, highly plausible and taken throughout this paper, but a family
member that stabilizes its defects another way, or that chooses a different compass space, is
still a family member. Likewise the **carrier** — vacuum structure along the advance direction
that a defect matches at infinity — is endorsed rather than axiomatic (§A.6.3). The distinction
matters downstream: results that consume the ansatz stand or fall with it, and the paper's
Result Index records which ones do.

### Two faces, one defect

The defect has two geometric faces, linked at the substrate level by the Hodge duality `I_4`
(R-005). **The link is sector-split, and Part A states the substrate-level version only.** R-127/R-128
later refine it: the map between the spatial-winding face and the meta-time-rotor face is the
*identity* for leptons and `I_4` for quarks, so the visible rotor axis is **not** always the Hodge
dual of the winding. Readers should carry that caveat forward from here rather than meeting it for
the first time in Part B: the unqualified version of the link does not hold, and Part A states
only the sector-split one.

With that said, the two faces are: 

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

**The two faces are dynamically locked.** They remain separately parametrizable as algebraic
observables — whether the lock is one-to-one is a question about the substrate's dynamics, not
about the algebra (§A.4, §D.5) — but in matter neither varies freely of the other.
The spatial winding cycles in space at fixed meta-time;
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

The same defect has an **outside-frame face**: the elastic cost `E₀` of its shape — the
vacuum-subtracted 3-slice value of the substrate functional at rest. The identification

> `m = E₀` (in lock units)

is a **named, counted premise** of the mass sector — the standard soliton-mass identification of
the Skyrme literature, stated here rather than silently assumed: every comparison of an elastic
value with a measured mass crosses it (§C.1.2). It sits at the **preferred-direction** level
(§A.6.3), not the axiom level: `m = ω` is family ontology, while reading `ω` as the shape's
vacuum-subtracted rest cost is an endorsement this instance takes and a family member may decline. It presupposes, and does not supply, the
one-particle spectral identification (§D.4.6 residue); it picks no renormalization scheme
(§C.3.3a); and its velocity extension is open in a sharp form — the outside cost of the
tilted-worldtube family obeys `E(v) = E₀·√(1+v²)` (a slice-measure identity), agreeing with the
observer's `γ` law at `O(v²)` and departing at `O(v⁴)`, where the candidate laws split as
`(0, −1/8, +3/8)` for the sheared pattern, the tilted tube, and `γ` respectively (R-169). That
relative sign at `O(v⁴)` is the energetic face of the same unbuilt observer↔substrate map named
at §B.1 and §B.6.6.

The half-angle convention `q_h = exp(m τ_5 û / 2)` is forced by spinor inheritance: under
`τ_5 → τ_5 + 4π/m` the rotor returns to itself, with sign flip at `τ_5 + 2π/m` — the `SU(2)`
double cover. Here `û` is a unit element with `û² = −1` — the meta-time rotor axis in the
`ℍ` subalgebra of the native `Cl(4,0) + ℍ` formalism (§A.5.6) — and the **simple** (single
plane angle) form written here is the *leading ansatz*, the one every computation in this
dossier rides. It is not the general case. A defect's twist generator is in general a `Spin(4)`
element carrying **two** plane angles: a transverse rate in the `e_4`-free `𝓛` planes and a
wave-parallel rate in the `e_4`-bearing `𝓠` planes. The two are separately invariant because
the drive axis `+e_4` distinguishes them — the wave's own axis is what lets a defect's two
rotations be told apart, and without a pinned advance axis the split has no invariant referent
at all. **This candidate adopts that drive-referenced two-rate form** — a pinned choice, stated
relative to and standing or falling with the drive-axis alignment pick of §A.6.4, and recorded
with the candidate's other choices in the programme's family tree; the ratio of the two rates is
an open kernel-level quantity (§D.5). A two-rate generator
`a·e_12 + b·e_34` squares to `−(a² + b²) + 2a b·I_4`, a pure scalar only when `a b = 0`, so a
two-rate rotor is a **product** of exponentials — `exp(B_a ω τ_5 / 2) · exp(v Ω τ_5 / 2)` — and
not a single simple `û`. The mass reading does not move under it: projecting the two-rotation
history onto the observer's complex line returns the **first** plane angle exactly, for every
choice of second axis, whether or not it commutes with the first — so `m = ω` stands as
written, read as *the plane angle in the observer's own winding plane* rather than as the
defect's only rate. The second rate is kinematically invisible to the mass; any dependence of
`ω` on where that rate locks would have to be a dynamical coupling, and is #1-gap content
(§D.5). The form does carry one exposure the simple one does not: a defect whose second rate
is not locked to the drive modulates its matter-wave amplitude as `|cos(Ω τ / 2)|` — an
amplitude beat, not an impurity of the phase — and the wavefront lock is expected to suppress
it for a locked, hence stable, defect, but that suppression is asserted and not computed.
For the observer-visible mass phase
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
frequency advancement along `τ_5`. The two are separated by **how they act, not by which blade they
act on** — spin acts *two-sidedly* on the L-orbit spatial bivectors (the rotor sandwich `R x R̃`),
mass acts *one-sidedly* as a right-multiplication phase. The distinction is not one of orthogonal
supports: R-127 later forces the observer-visible mass axis onto `û = ±B_a`, which is itself one of
the L-orbit blades carrying spin, so the two observables share a blade and are separated by the
sidedness of the action alone. (The two supports are emphatically *not* orthogonal blades; that
reading is inconsistent with R-127.)
In free-field linearization a configuration
can carry spin without mass (the photon: zero meta-time frequency, nonzero spin) or both (an
electron), so the two are independently parametrizable as algebraic observables.

In matter, the two are **dynamically coupled through the defect** (R-005). Per §A.3 the spatial
winding (which the spin field carries) and the meta-time rotor (which mass measures) are two
faces of one circular geometric object related by the `I_4` Hodge map. The algebraic separability
is what lets us *discuss* spin and mass as distinct observables on a fluctuation; the dynamical
coupling is the substrate fact that for a defect, the spin field carries the topology and the
meta-time rotor sustains it. **Two faces of one object: algebraically independent and
dynamically locked.** Whether that lock is one-to-one — whether the two rates are pinned to a
single ratio — is a separate question, and it is a question about the substrate's dynamics
(§D.5), not about the algebra.

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
falsifier §E.3 row 6.

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
  quark-sector epicycle parametrization): `ε_u` is *set by* the rule from the fitted `ε_d`, so
  the ratio is realized by construction rather than tested, and the rule is structurally
  untestable against `m_t` because no top hadrons exist.
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
orthogonal under the bivector inner product

> `⟨A, B⟩ := ⟨A B̃⟩_0 = Σ_{i<j} a_{ij} b_{ij}`,

the **reversion-conjugated** grade-0 part, which is positive-definite: `⟨e_{12}, e_{12}⟩ = +1`.
The conjugation is not cosmetic. For a bivector `B̃ = −B`, so the *unconjugated* `⟨A B⟩_0` carries
the opposite sign on this subspace (`⟨e_{12} e_{12}⟩_0 = −1`) and would invert every sign rule
built on it — in particular the Coulomb like-repels/unlike-attracts reading of §B.5.3. The
definition above is the one the engine implements (`bivector_inner_product`).

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
formalism throughout this paper is `Cl(4,0) + ℍ`, and the `ℍ` in that name is a **subalgebra of
`Cl(4,0)`**, not an external tensor factor — hence the "+", not "⊗". It is the even subalgebra
`Cl⁺(3,0)` of the `Cl(3,0) ⊂ Cl(4,0)` generated by `{e_1, e_2, e_3}`; as a vector space it is the
scalars plus the span of the L-orbit,

> `ℍ = span_ℝ{1, e_{23}, e_{13}, e_{12}} = ℝ ⊕ 𝓛`,  with  `(i, j, k) := (e_{23}, e_{13}, e_{12})`,
> `i² = j² = k² = −1`,  `ij = k`,  `jk = i`,  `ki = j`,  `ijk = −1`.

That span is closed under the geometric product, and the relations above are exactly the
quaternion relations, so the subalgebra *is* `ℍ` (R-093; engine: `cl40_quaternion_triple`). This
is the `ℍ` whose units supply the meta-time rotor axis `û` of §A.4 — in both sectors, by
R-127/R-128 — and which contains the QM complex unit `i = e_{12}` of §B.3.1 (a transverse simple
bivector, `e_{12}² = −1`). Rotors, idempotents, and the meta-time phase live here.

Do not confuse this `ℍ` with either summand of the even subalgebra `Cl⁺(4,0) ≅ ℍ ⊕ ℍ`. That
decomposition is the SD/ASD split, and `e_{12}` is **not contained in either `ℍ` factor**:
`e_{12} = ½(e_{12} + e_{34}) + ½(e_{12} − e_{34})` has a nonzero component in *each* summand. The
quaternion subalgebra above is not a summand, and not an ideal of `Cl⁺(4,0)` at all; it embeds in
both summands at once (§D.1.2). A *third* use of the symbol appears at §C.3.8/§D.2.4, where the
three generations are the imaginary units of the **ASD summand** — that `ℍ` is a factor of
`ℍ ⊕ ℍ`, not this subalgebra. `Cl(4,1)` is the same content with
`e_5` written explicitly, useful when meta-time dependencies need to be tracked through a
calculation.

Costing `Cl(4,1)` content requires a pairing, and the algebra constrains the menu sharply: **no
`spin(4,1)`-invariant positive-definite pairing exists** (non-compactness), while
`t = α₅ ∘ reverse` — reversion composed with `e_5 → −e_5` — *is* positive-definite on all 32
blades, invariant under `Spin(4)` and under the `E`-phase, and non-invariant under the boosts:
positivity is bought by selecting the `e_5` axis, exactly as the Dirac adjoint selects `γ⁰`
(R-168). This instance's cost convention adopts this pairing — a **named, counted pick** at the
instance level (§A.6.4, node V3-7), together with the decision to cost the carrier's own advance
(node V3-8); what survives any re-pick is the theorem, not the choice (the
reversion pairing is indefinite on `e_5`-content with no commutator-quartic backstop, since `E`
is central; the conjugation pairing leaves the boosts negative; a `Spin(4)`-projected cost makes
the carrier phase dispersionless). Restricted to `Cl(4,0)` the adopted pairing coincides with
the reversion pairing already used throughout the hadron sector, so nothing banked moves; its
one substantive consequence is that the vacuum carrier's own advance is **costed** — the drive
of the substrate's steady state (§D.5) has an object to sustain.

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
needs `e_5` as a *spatial* degree of freedom (a new winding direction, a soliton coordinate) is an
escape from the framework's ontology, not physics. Rebuild it in `Cl(4,0) + ℍ` and the spurious
dimension disappears. That `τ_5` is the timelike direction the 5D master equation advances *along*
(§D.4.6) is the permitted meta-time role, not a red flag: what the rule forbids is a fifth
*spatial* axis, never the evolution parameter. (Full `Cl(4,1)` treatment at §D.1.)

That is the algebra. The next part of the paper uses it; the observer's gamma matrices
`γ⁰ := e_4`, `γʲ := e_4 e_j` are introduced and verified in §B.1.

---

## §A.6 — The architecture: a family and its first candidate

Read this before Part B, because it fixes what everything after it is a claim *about*.

Time-Wave Theory is not one theory. It is a **family** — **TWT-Core**, defined by seven axioms
and one refusal — together with a list of candidate members that realize it. Everything from
Part B onward develops **V3**, the family's **first candidate instance**: the first member built
all the way down to numbers. That V3 exists is an existence result, and that is all it is. V3
can be dismantled entirely without a line of this section changing.

The distinction is load-bearing in one direction in particular. The framework's two
already-measured exposures — the dimension-six Lorentz-violation ceiling (§B.6.3, §E.3.3 VG-6,
§E.3.5(4)) and the electroweak crossing-scale miss (§C.4.5, §E.3.5(5)) — are **instance-level**:
they ride choices V3 makes, not axioms the family holds. So does every calibrated number in
Parts C and D.

The honesty rider belongs in the same breath, or the architecture becomes a shield: **the Core
is not vindicated by carrying neither wound.** It carries neither because it makes no numerical
claim at either place, and a family that has not yet said a number cannot be wrong about one.
The wounds are the price of being the only member that says numbers at all.

### A.6.1 TWT-Core — the family definition

Seven axioms and one refusal. A theory that has all seven is a member of the family. A theory
that drops any one of them is a different theory, however much else it shares.

- **S1a — The substrate.** Reality is a four-dimensional Euclidean material substrate;
  everything else the theory talks about is a property or a pattern of that substrate.
- **S2 — Meta-time.** There is a second time, `τ_5`, whose direction squares to `−1`, and the
  state of the substrate advances in it.
- **S3 — The lock and the slice.** The substrate carries an advancing wavefront; an observer is
  mechanically locked to it and can only ever see a slice, so a preferred foliation exists
  whether or not anything inside the slice can see it.
- **S4 — Matter is a defect.** A particle is not a piece of stuff sitting in the medium; it is a
  protected pattern of the medium itself — a defect.
- **S5 — The medium is driven.** The advance is one-way and constitutive: the medium is not
  resting and not merely relaxing toward rest, it is driven.
- **LS — The local state.** The medium's local state at each site is a 4D orientation — six real
  parameters — stated for **any grain structure** a family member realizes, witness-free at
  family level (each member re-witnesses it on its own grain); whether its `ℤ₂` sign lives in the state itself or enters only at the emergent
  covering sector is a deliberately open branch (§D.3.2). The continuum field inherits this
  target unchanged, and the wave's advance direction splits its generators into wave-parallel
  and wave-transverse.
- **B-6 — The preferred foliation is the cosmic rest frame.** The foliation of S3 is not left
  free: it is the frame in which the cosmic microwave background is isotropic — the comoving
  frame. This is the strongest option available at family level, and taking it is why the family
  has a kill condition at all (§A.6.2).

**The refusal — the substrate is a material medium, not a field.** The consequence binds every
reader of this paper: the **rotor field** that runs through the body and the engine is
**instance-level description** of the medium — a way of writing down what the medium is doing —
and is **not the ontology**. An argument that needs the field to *be* the world is not a Core
argument. Note what the refusal does not say: it is about what the substrate *is*, not about
whether it is grainy — graininess is a preferred direction, not an axiom (§A.6.3). And the
refusal is scoped: a field is refused only as a *fundamental description of what the world is
made of*, never as a mathematical description of an **emergent property** of the medium, the way
temperature is a field-description of molecular motion — which is why the field formalism works
as well as it does. Two things ride that reading as Core commitments rather than conveniences:
the **grain → cell map is a real physical relation**, plausibly driven by the wave, not a
bookkeeping device between two levels of description (§D.3.5); and the cell's initial description
is "an emergent pattern."

Against the Opening's premise list, the correspondence is one-to-one where it exists:

| Core axiom | Opening premise / paper object | Developed at |
|---|---|---|
| S1a | `A-1a` — 4D Euclidean substrate | §A.1 |
| S2 | the signature placement `e_5² = −1` | §A.5.6, §D.1.3 |
| S3 | `A-3` — wavefront / signature locking (with `A-2*`, the outside-frame method) | §A.2, §B.1 |
| S4 | `A-1*` — matter is defect | §A.3 |
| S5 | `A-2` — driven dynamics | §D.5 |
| LS | the local state at a site, six real parameters — stated witness-free, for any grain structure; this candidate's D4-sited construction (R-102, §D.3.2) is V3's witness of it | §D.3.2 |
| B-6 | the `τ_5`-foliation ↔ comoving-frame identification (R-031) | §B.4.5, §B.7 |

The Opening's two remaining premises are **not** Core. `A-1b` (the D4 arrangement) and `A-1c`
(the `J`, `D` bond couplings) are V3's first two picks, and they appear as such in §A.6.4.

### A.6.2 The kill condition

**If the ordering that Bell-correlation selections follow is measured and found to be a foliation
measurably distinct from the cosmic rest frame, the family is finished** — not one version of
it, all of it. That is what it means for B-6 to sit in the definition rather than in a branch.

The safe option was available and was declined: leave the foliation unnamed. A theory with an
unnamed preferred foliation cannot be caught, because "there is a frame, somewhere" survives
every measurement. Naming it as the comoving frame turns a metaphysical posture into a target.

Two riders belong with it, and neither is optional. First, the asymmetry: the measurement that
would fire this is one that standard quantum mechanics *also* forbids, so in this channel
agreement confirms nothing — it is a consistency check, and the family inherits quantum
mechanics' verdict either way — while disagreement kills. Maximum downside, no matching upside;
that is the price of naming the frame. Second, this is the family's only *total* kill condition:
of the sixteen falsifier rows at §E.3.1, fourteen stand at family level and two are instance-level
(rows 6 and 12; §E.3 carries the reading row by row). Said at its truest: this is a research programme with one
inherited kill condition, and empirical exposure otherwise lives in instances.

Because this channel fires only where quantum mechanics also breaks, the family has no
*independent* empirical exposure **in it**. Two qualifications keep that from being read as
safety. One other row reaches deeper than most picks, through a channel the shared quantum
formalism does not itself close: a sector- or epoch-dependence of the observed `c` against the
lock rate `c_meta`, which lands on this candidate's identification of the two (the
`A-3`-downstream chain) — the axioms state no rate and no uniformity, so a detection would label
the emergent `c` non-uniform while the axioms stand; it is flagged at §E.3.5(3) as the sharpest
instance-level exposure. The contrast with the Bell channel is structural, not a claim to sole exposure — the
incumbent forbids a sector-differential limiting speed too, so a positive detection there would
also be a Lorentz-invariance violation and would cost the incumbent a symmetry. The difference is
*how* each forbids: in the Bell channel the prohibition is a theorem of the very formalism this
framework is isomorphic to (§B.4), so agreement is guaranteed if quantum mechanics holds and
confirms nothing; in the `c_meta` channel the incumbent's zero is an imposed symmetry, and a
completed candidate could in principle differ from it. A positive result there does not end the
family: it forces reformulation inside it — the failing object is the candidate's `c ↔ c_meta`
identification, and the axioms, which state no rate, stand while the emergent `c` takes the
non-uniform label. And the family's
one identified route to building an exposure of its own is the finite-grain / bounded-amplitude
higher-order-interference channel, where the Born rule's deviation law — sourced by the medium's
grain (vanishing with it) or by its amplitude ceiling (present at fixed grain), two sources with
different scaling laws the channel's protocol must separate — would be a
structure-derived number the incumbent inputs as exactly zero and the triple-slit programme
already supplies a bound. That deviation law is not derived in this paper; it is named here as a
route family, not a result.

### A.6.3 The preferred directions

Eight further commitments are endorsed as highly plausible and are **not** part of the
definition. A candidate that goes the other way on any of them is still a member of the family:

grain discreteness (§D.3.2) · Skyrmion-class defects (§A.3, §C.1) · carrier structure (§A.3) ·
the measured-`G` anchor practice (§B.6.2) · Koide `c = √2` (§C.3.2) ·
`m = E₀` (§A.4) · generations as the anti-self-dual triple with the associativity premise
(§C.3.8, §D.2.4) · the weak-hosting premise — that weak isospin is hosted by a
three-dimensional `su(2)` inside the substrate's grade-2 rotation algebra at all (§C.4.2).

`weak = SD` is **not** itself one of those directions, and it is not a pick either: its menu is
closed by computation and both alternatives are refuted (§C.4.2), so it is not a preference a
family member may simply reverse. It is forced given the last endorsement on the list above —
the weak-hosting premise — together with the observed weak-isospin-singlet character of the
right-handed fermions. Divergence at that node therefore happens one level down, at the
endorsement rather than at the assignment: a candidate that hosts weak isospin somewhere other
than the substrate's own rotation algebra goes the other way on a preferred direction exactly as
it may on any other, and that is the only door open there.

This is the reader's most consequential fork after the axioms themselves. A large block of
Parts B and C is derived *given* one of the endorsements above, and those results are family
property only in that conditional sense: they stand or fall with the endorsement they consume,
and an endorsement is a preference, not an axiom.

### A.6.4 Instance V3 — the picks

V3 buys its numbers with eleven pinned choices — fifteen rows below, because three of them turned
out to contain a further choice inside them, and one of those contains two. Each is a branch point: what the choice was picked
*from* is recorded, and so is what un-picks it.

| # | The pick | The menu it came from | What un-picks it, and what moves |
|---|---|---|---|
| V3-1 | Substrate arrangement = a **regular D4 lattice**, at the `G`-back-fit (Planckian) size (`A-1b`) | regular lattices (D4 and others) / irregular-discrete arrangements (causal-set-adjacent) / a continuum medium with a cell scale | Re-arrange or re-size: the dimension-six and dimension-eight numerics recompute and the `Λ_L` band's provenance goes with them; Layer-1 structure is untouched |
| V3-1a | Drive-axis alignment = the advance axis is a **lattice symmetry axis** | aligned (the banked driven-group apparatus, stabilizer order 48) / misaligned-generic (trivial stabilizer; the spatial quartic permission opens to its full 15 dimensions) / lower-symmetry alignments | A misaligned member recomputes every driven-group count from its own stabilizer; the orbit-constancy failure channel is keyed axis-independently and survives |
| V3-1b | Two-rate defect rotor, **drive-referenced** (§A.4): the twist generator is in general a `Spin(4)` element with a transverse and a wave-parallel plane rate, separately invariant only because V3-1a pins the advance axis; the candidate adopts the two-rate form, with the rate ratio an open kernel-level quantity (§D.5) | the simple one-rate restriction / the drive-referenced two-rate form / a free-standing two-rate form (no invariant referent without V3-1a) | Re-impose the simple restriction: §A.4 reverts to the single-`û` form, the bond-harmonic ceiling's premise re-becomes physical, and the amplitude-beat exposure closes; the node also un-picks automatically if V3-1a does |
| V3-2 | Bond structure = the `{J, D}` **truncation** (`A-1c`) | the ten-constant bilinear menu allowed on D4 under the driven point group — `J`: 2, `D`: 2, `Γ`: 6 | Turn on the surviving `Γ` direction or the second `D` dial (§D.3.3): the numerical spine re-reads; the quadratic spine is conditionally protected, the amplitude identification is not |
| V3-2a | DM support = the 12 `e_4`-bonds only | the two-dimensional allowed DM space — the `e_4`-bond coupling and a spatial-bond coupling of the same symmetry type, which no substrate argument separates | A non-zero second `D`: the amplitude identification behind `D/J` moves; the canting — and with it the chiral symmetry breaking — can switch off entirely on a cancellation line; and the `Γ` survivor's vanishing, a property of the vacuum's high-symmetry direction, is exposed with it |
| V3-3 | `f_π` = the ANW **fitted** value | any cell-scale anchoring | Re-anchor: the hadron chain recalibrates |
| V3-4 | `D/J ≈ 0.79`, lepton-calibrated | any calibration channel | `Γ ≠ 0` established: `0.79` re-reads as a measurement of a combination and both legs re-fit |
| V3-5 | `e_ANW = 5.45` | the Skyrme-stabilizer determinations (the massless-pion scheme picked partly on the `√18/(D/J)` agreement) | The two legs converge → the pick retires; the legs split → the `√18` bridge dies (§E.2.1, both ways) |
| V3-6 | Gravity route = **Sakharov induced gravity**, in one banked action class | thermodynamic / entropic / gauge-gravity / a thermodynamic reading of the same medium — every route on the menu taxed by the analog-gravity caution | Re-route: the `Λ` anchor moves or dissolves, and the dimension-six coefficient's denomination goes with it; the class-scoped uniqueness result stays true of its class |
| V3-7 | Cost pairing = `t = α_5 ∘ reverse` (§A.5.6) | the four-option pairing menu; the no-invariant-pairing theorem survives any re-pick | The pairing's own class revert list; the hadron sector, which uses the coinciding restriction, does not move |
| V3-8 | The vacuum carrier is **costed**, at `(k_c/2)²` | costed / costless / other densities | Rides the pairing re-pick |
| V3-9 | Kernel branch = the **driven-hysteretic** class (§D.5.3) | the full kernel-class menu — this is the #1 gap itself | Free re-pick: no banked physics falls with it |
| V3-10 | Hadron machinery = the **ANW/Skyrme semiclassical toolbox** | soliton-quantization toolboxes | The import's own excision row (companion Section 13) |
| V3-10a | **Cell-scale target space = the same target as the grain state** (named 2026-08-26; the identification the Skyrmion sector rests on) | same target / the Goldstone coset of the grain vacuum / an unrelated emergent target | A surviving target of dimension < 3 has `π₃ = 0` — no Skyrmion and no hadron sector; a three-dimensional one licenses the Skyrme construction from below. Deciding computation docketed (surviving-manifold dimension + gap comparison, LSWT) |
| V3-11 | Fermionic quantization = the **Finkelstein–Rubinstein** scheme (§B.3.5) | fermionic-quantization schemes for solitons; induced-term routes are the named alternative | The import's own excision row; a substrate-induced Wess–Zumino-class term would force the odd sector from the dynamics and retire the pick altogether |

The full table — each node with the named result that required it, what rides it, and its complete
revert clause — is the programme's **family tree** (`TWT_FAMILY_TREE.md`), the standing register
in which a branch point is recorded at the moment it presents itself. The table above is its
compressed form, and **the tree is authoritative where the two differ**; companion Section 14
carries the pointer and the result-by-result sort.

These are where the wounds live. The dimension-six ceiling rides three pinned choices in series,
carried by two nodes: a **regular** arrangement at a **back-fit** size (V3-1), and **one**
induced-gravity chain to denominate that size in Planck units at all (V3-6). The crossing-scale
miss rides the same arrangement's gauge sector together with the instance's calibrations (V3-1
with V3-3 and V3-4). Neither wound touches an axiom — and, per the opening of this section,
neither is thereby answered.

### A.6.5 What the Core has, what it does not claim, and what the programme delivers

Sorting every numbered result against the definition (the companion's Result Index carries the
sort per row): roughly a third consume nothing but the axioms; a comparable block consumes
the axioms plus one or more preferred directions, each row standing or falling with the
endorsement it consumes; the remainder need a choice that belongs to V3. The two blocks are
never to be merged into one headline.

**What the Core keeps — each block at its own level, the conditional ones conditionally.**
Unconditionally, on the axioms alone: most of the Part-A picture, the wavefront-isomorphism and
Lorentzian-appearance arc, the full quantum-postulate and Bell sector, the texture scaffold, and
the algebra reference block. Conditionally, on the axioms **plus a named preferred direction**:
the Maxwell/Coulomb/charge arc and the topology/stability/`B − L` arc (both riding the
defect-class endorsement), and the
generation-and-Koide structure (riding the ℍ-triple with associativity, and `c = √2`). The second
group is family property only in the sense §A.6.3 gives that phrase: each row stands or falls with
the endorsement it consumes. A further rider binds the phrase, by the Core's own standard: **Core-clean is a
*consumption* classification — it says a result uses no instance pick — not a claim of
derivation-completeness.** The quantum package in particular buys
its structure with imported, registered mathematics (the tensor-product composition rule, the
singlet form, Gleason's theorem among them), so it is a **relocation with a gain, not a
derivation**, exactly as the signature is (§B.1), and it must be quoted that way.

**What the Core does not claim.** No scales: the family has **zero earned dimensionful scales**,
and the two the corpus uses are a back-fit of measured gravity and a fitted hadronic scale, with
the ratio between them neither derived nor protected (§D.3.5, §E.2.1). No gravity results today:
every gravity result in this paper rides an instance pick, and structural gravity — one medium
so one light cone, the equivalence principle, the Newtonian limit with the right sign,
compatibility with general relativity — is owed as a re-grounding on the axioms rather than
inherited from §B.6. No magnitudes: couplings, running, absolute masses and decoherence rates all
wait on the one unbuilt object of §D.5; the family owns the kernel *programme* and owns no
kernel. And one standing debt the refusal creates rather than discharges: fields won historically
by doing work a medium could not be shown to do — retardation, radiation reaction, local
conservation in transit, gauge structure — and every item on that list is now work the *medium*
must be shown to do instead. If gauge structure proves to be on the un-reclaimed list, that is
Core-relevant knowledge, not an instance detail.

**The deliverable is a list.** At family level the programme delivers the **list of surviving
candidates** — self-coherent, empirically plausible members — not one maximally pinned instance;
V3 is the list's first entry, and a second candidate would be a new table beside §A.6.4's rather
than a rewrite of this paper. One consequence for reading: questions that cannot be decided from
inside the lock, by the theory's own structure, are **family freedom**. They are recorded and not
expanded on, because candidates differing only there are one member with several descriptions.

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
observer in a Euclidean substrate.

**Scope of the claim, stated up front.** What is derived here is
the **emergence of observer-frame Lorentz structure**, *given* the framework's signature posit — not
the signature itself. Axiom A-1a takes the spatial substrate `(ℝ⁴, g)` positive-definite, and
§A.5.6 places the framework's one negative square on the meta-time generator, `e_5² = −1` — a
posit that supplies the central complex structure `E = I_4·e_5`, not the observer's timelike
direction, which the wavefront lock places on the advance axis `e_4` (`γ⁰ = e_4`, `(γ⁰)² = +1`).
That placement is a **posit**, not a theorem: every theory must locate its negative square
somewhere, and TWT locates it there. Read strictly, the framework *relocates* the signature rather
than deriving it, and this section should not be read as claiming otherwise.

What the section does establish, and what makes it a spine result, is the non-trivial half: that
`Cl(4,0)` and `Cl(1,3)` are the **same real algebra**, so a wavefront-locked observer inside a
positive-definite substrate necessarily reads its own kinematics as Lorentzian with signature
`(+,−,−,−)` — the observed signature is then forced, not a second free choice. That implication is
DERIVED-A; the antecedent is INPUT. §A.5.6 states the same thing in the substrate's own voice.

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

> **The wavefront construction lands on a nondegenerate Lorentzian partner, not the split (2,2).**

What the wavefront geometry delivers is an **algebra identity**, not a forced signature. The
substrate algebra `Cl(4,0)` — all four generators squaring `+1`, no convention in play — is
`≅ M_2(ℍ)` by Bott periodicity, and `φ` carries it onto the algebra generated by `{e_4, e_4 e_j}`,
whose generator squares read `(+, −, −, −)`. In the convention where `p` counts generators squaring
`+1`, that is `Cl(1,3)`, and `Cl(1,3) ≅ M_2(ℍ)`. What is convention-*independent* here is the
**pattern** — one generator squaring one way and three the other, rather than two and two — and
that is what excludes the split partner `Cl(2,2)`.

**A remark on scope, in the menu-vs-pick idiom (canon §2).** The overall metric *sign convention* —
`(+, −, −, −)` versus `(−, +, +, +)` — remains conventional, **with `Spin(1,3) = SL(2,ℂ)` acting
identically in either**. And the *algebra type is itself convention-sensitive*: the same physics presented in
the mostly-plus convention is generated by squares `(−, +, +, +)`, i.e. `Cl(3,1) ≅ M_4(ℝ)`. So
geometry supplies a **menu of presentations** — `M_2(ℍ)` read through `(+, −, −, −)`, `M_4(ℝ)` read
through `(−, +, +, +)` — one physics in two labels, with nothing observable distinguishing them and
no *pick* between them for nature to make. What is derived is therefore the *substrate* identity
`Cl(4,0) ≅ M_2(ℍ)` together with the fact that `φ` lands on a **nondegenerate Lorentzian** partner
rather than the split `(2,2)` one; what is **not** derived is a preferred real algebra for
"observed spacetime". To call the real Clifford algebra of observed spacetime *forced* to be
`M_2(ℍ)` would over-read a convention as a forcing. The glossary entry for
**signature** states the same thing — that the algebra type is convention-sensitive — and cites
this subsection for it; N56 records the hazard.

Two disambiguations, so the remark is not over-read. First, this changes nothing about *where* the
framework locates its signature: the Lorentzian signature remains an INPUT **placement** on `e_5`
plus a derived implication, and that relocation is not re-litigated here — only the word "forced"
as applied to the algebra type is. Second, this **presentation** menu is a different object from
R-145's texture-metric **signature** menu; N56 records that the kinematic (§B.1) and dynamical
(§B.6.6) Lorentzian faces are separate constructions with no map between them built anywhere in the
corpus, and nothing here supplies one.

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

**Why the leading-order answer does not depend on how the substrate-Lorentz question is settled.**
The Collins-class mechanism needs
**species-dependent** coefficients to produce an observable: what it computes is a set of maximum
speeds `c_i`, and what is measured is a *difference* `c_i − c_j`. In TWT the radiative corrections
are generated by the *one* substrate field, so whatever induced violation the loops carry is
inherited **universally** — and a species-universal dimension-four coefficient is **removed by a
coordinate rescaling**, because it is a single overall factor relating the substrate's light-cone to
the observer's units rather than a relative observable. Since that removal does not care what the
loops produced, it does not care at what order they produced it. The consequences split cleanly:

- if the substrate is exactly Lorentz-invariant under its interacting dynamics, every defect is
  too, exactly;
- if the substrate carries residual violation, every defect inherits it universally, which is
  unobservable by that rescaling;
- the only route to observable *leading-order* violation is for substrate breaking to couple
  differently to different defects' *internal structure* — which requires resolving defects at
  scale `Λ`, and that is a dimension-six form-factor effect, not a dimension-four one.

The conclusion is that *the leading-order answer comes out right regardless of how the
substrate-Lorentz question is resolved*, and that is the claim, no more.

**This is a DEFUSAL, not a proof.** The argument does *not*
show the substrate is itself exactly Lorentz-invariant under its interacting dynamics; that
question is open and stays open. What it does is *collapse* a generically-fatal problem about `N`
independent fields into a single tractable question about one field. The universality-plus-rescaling
step carries one substrate assumption that is not engine-checkable — that one field generates all
the radiative corrections, so the induced coefficient really is common to every species — and it is
registered as such (companion Section 13, row **I-22**) rather than carried at a flat DERIVED tag.
What this closes is the **dimension-four** half of R-016; the dimension-six residual
below is expressly *not* closed by it.

**Prior art — the physics here is not ours.** Before the argument, the credit.
That the D4 / F4 lattice suppresses rotational-symmetry-breaking cutoff effects relative to the
hypercubic lattice is **established lattice field theory**, not a TWT discovery. Neuberger proposed
F4 lattices for exactly this reason (*Spinless fields on F(4) lattices*, Phys. Lett. B **199**, 536
(1987)), and the property has been used since — Celmaster; Bhanot, Bitar, Heller & Neuberger;
Klomfass. It remains live: Katz & Nogradi formulate QCD on the same lattice (the "16-cell
honeycomb", arXiv:2512.10604, Dec 2025), motivated by *"a higher degree of rotational symmetry as
compared to a traditional cubic lattice leading to much smaller cut-off effects"*, and state the
dispersion form of the theorem directly — the first order at which Lorentz invariance fails is
`O(a⁴)`, not `O(a²)`. The related fact that the 24-cell is a spherical 5-design is classical
(Delsarte, Goethals & Seidel 1977). The result is **not** new: any claim of novelty for it does
not survive contact with the lattice literature.

What this section adds is narrower and is claimed as such. The group-level form of the statement,
with triality named as the protecting mechanism, is also prior art: Chow (1999) states that D4 is
exactly isotropic at order `a²` and *"the only unexceptional root lattice with this property"*,
protected by the accidental threefold Dynkin-diagram symmetry; and the two-sided sharpness
(dimension eight *reached*, not merely bounded) is established in the lattice-kinetic-theory
literature (Chen, Goldhirsch & Orszag 2008, who compute the anisotropic sixth moment and treat the
degree-four isotropy as well known). What remains claimed here is the **generality of the proof** —
one-dimensionality of the degree-four invariant space for *every* analytic point-group-symmetric
kernel at once, via the `W(F4)` invariant degrees, with the explicit triality premise **(P-pg)** —
and one narrow transfer: Lorentz-violation EFT already uses the point-group protection argument at
dimension four (Mattingly 2005; Jacobson, Liberati & Mattingly 2006, crediting the lattice
literature), and what appears not to have been carried there is that the argument *fails* at
dimension six for the hypercubic lattice and *holds* for D4. A standalone treatment with full
reproduction code is at `knowledge/corpus/D4_lattice_quartic_isotropy.md`.

With that said: the complementary rotational-anisotropy bound is closed by the D4 point group
(R-165), and the reason is representation-theoretic rather than a property of any particular kernel.
The automorphism group of the D4 root system has order 1152 — it is `W(F4)`, whose invariant degrees
are `{2, 6, 8, 12}` — and its space of **degree-four** invariant polynomials is consequently
*one-dimensional*, spanned by `(k²)²` alone. So for any dispersion kernel invariant under the
lattice point group and analytic in `k`, there is no anisotropic quartic at all: the quartic term
is forced isotropic by symmetry, whatever the kernel — given the premises below, the operative-
symmetry premise in particular, since the drive is itself a dynamics that reduces the operative
group. The degree-six invariant
space is two-dimensional, so an anisotropic sextic does exist, and the leading rotational
anisotropy of the polarization-averaged dispersion therefore sits at **dimension eight** — reached,
not merely bounded —
`(E/Λ_L)⁴ ≈ 2 × 10⁻³¹` at the highest observed cosmic-ray energies (ruled band's loose corner,
§B.6.2): structurally out of any observational range. The concrete face of the same fact is the bond-moment tower: second moment
`Σ v_i v_j = 12 δ_ij`, fourth moment exactly `4(δδ + δδ + δδ)` (`M_1111 = 12 = 3 M_1122`), sixth
moment anisotropic. This is **not** generic to lattices: simple-cubic `Z⁴` has `N_1111 = 2` while
`N_1122 = 0`, and its point group admits a two-dimensional degree-four invariant space containing
`Σ k_i⁴`. Five premises carry the inference and are stated rather than buried: that a derivative
expansion exists (a non-analytic driven-dissipative memory kernel — the #1 gap itself — is not
covered by a polynomial-invariant argument); that the *full* point group including triality
acts (the reflection subgroup `W(D4)` alone has a three-dimensional degree-four space, and the
second shell's two sub-orbits are each anisotropic, cancelling only at equal weight — so a
substrate coupling weighting triality-related orbits unequally would restore dimension-six
anisotropy); that the **ground state preserves the point group** (the §D.4.3 spiral vacuum
breaks it: the species-universal `O(q²)` stiffness splitting is absorbed by the rescaling
class, and the space-fixed — sidereal — residual is an open question the exposure ledger
carries); that the symmetry **operative** on the sector the claim is quoted for is that full
point group and not the **driven** subgroup — the theorem is proved in four Euclidean variables,
while leading *rotational* anisotropy is a three-dimensional statement and the drive singles out
the advance axis `e₄`. The stabilizer `Stab(e₄)` has order 48 and restricts faithfully onto the
full octahedral group `W(B₃)`, whose invariant degrees are `{2,4,6}`: at the driven group the
degree-four *spatial* invariant space is **two**-dimensional, spanned by `(k_sp²)²` and
`Σ_{i≤3} k_i⁴`, so an anisotropic spatial quartic is **permitted** there. What carries the
protection at the driven group is then not the driven symmetry but a *full-group property of the
coupling*: the 24 bonds form a single equal-weight orbit of the full point group, which forces
`Σ_b (b·k)⁴ = 12(k²)²` identically in four variables, so the spatial fourth moment is exactly
isotropic — full tensor, on every 3-plane. The `+4/−4` split between the twelve `e₄`-bearing
bonds and the twelve in the `e₄ = 0` hyperplane is the advance-axis *sensitivity decomposition*
of that protection, not its mechanism: at a generic axis no such split exists and the isotropy
persists. Any driven-sector coupling whose bond weighting fails to be constant on the full
orbit — invariant under the driven group but not the full one — would
restore dimension-six spatial anisotropy, facing SME-type sidereal bounds rather than the
isotropic ones; that is this premise's would-change-if, and it is the group-theoretic content of
the arbitration the `Γ`-survivor pointer below dockets. And a fifth, implicit in "invariant
polynomials" and stated here: **the kernel is a
scalar in the internal index** — the theorem governs the polarization-averaged dispersion. It does
not cover internal-index-carrying (matrix-valued) kernels, and the point group cannot close that
sector: the unique fully `W(F4)`-invariant symmetric-traceless bond coupling (the pseudo-dipolar
direction) already carries a direction-dependent four-derivative polarization splitting (exact
spectra: eigenvalues `(−6, 2, 2, 2)` on an axis vs `(−12, 4, 4, 4)` on a face diagonal). The
scalar sector is nonetheless closed against that entire channel at every order — every
symmetric-traceless coupling is traceless bond-by-bond, so `Tr Σ_b f(k·b)K_b ≡ 0` — and what the
channel can source at dimension six, if its dressed coefficient is nonzero (the §D.5.7 assembly
record; tree-level zero on both computed vacuum branches, #1-gap-routed), is a
polarization-splitting (birefringence-class) anisotropy, bounded by SME-type anisotropic/sidereal
limits rather than the isotropic ones.

What these protections do **not** reach is the *rotationally invariant* dimension-six residual,
conventionally `η⁽⁴⁾ p⁴/M²_Pl` — it is not a relative-boost observable (so R-016 does not apply)
and it is not an anisotropy (so D4 does not apply), and at dimension six a *species-universal*
coefficient is not removable by any rescaling, since the induced velocity shift `≈ (3/2) η p²/Λ²`
is momentum-dependent. Its coefficient is set by the substrate's own strain-mode dispersion — an
object the engine gates (`Cl41Wave().wave_speed_c()` raises) — and by each defect's form factor.
**It is named as an open exposure at §E.3.5(4), not as a prediction.**

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

The linearization of the master wave equation (§D.4) **around the canted vacuum** (whose
quadratic order is anisotropic at `O(q²)` — §D.4.6's Face 1; the isotropic form used
here is that section's named idealization, with the observer-projection question open) — not around a
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

**Which `i` was that, at the vacuum?** Nothing at the Fourier step selects `e_{12}`. The
linearization is performed about the canted vacuum, where §B.3.1's condition (S) is empty and the
centralizer of `e_4` in `Cl⁺(4,0)` is the full four-dimensional `{1, e_{12}, e_{13}, e_{23}}`, so
there is no unique complex line at that point — and per §B.3.1's reconciliation paragraph a defect
*orients* a complex line rather than establishing one. The reduction therefore decomposes against a
**conventionally fixed** transverse blade (the §B.3.1 frame-equivalence note): legitimate inside a
single defect's sector, where R-127 then fixes the unit, but that fix is **per defect**, so with
several defects present there is no one complex structure to decompose the whole field against.
That global half is not addressed by residue (iii) — which names only *which* unit carries the front
phase for a given defect — and it sits with §B.4.1's open multi-defect state space, not with
anything this reduction closes.

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
This hands the dispersion relation a *kinematic* **consistency check**, not an independent second
derivation. Calling it an independent route would over-read it. Once the Lorentz
group acts and `m` is *defined* as the rest label, the statement "the orbit of the rest label is the
mass shell" is close to tautological — it is the definition of the orbit, not new information about
the substrate. What the check does establish is that the `Cl(4,0)` conjugation action and the
§B.2.1 Fourier reduction agree where they overlap, which is worth verifying and is not automatic;
but the two share their foundations (the isomorphism and the front label), so agreement is
corroboration rather than over-determination. That each moving label is realized by an actual moving
defect solution is a named premise of this result, the same class §B.5.5's force law carries.
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
by linearization around the canted vacuum (the §D.4.6 isotropic idealization) — no defect
needed for the free propagator. The
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

The fluctuation field is then **taken to be**

> `ψ(r) = f(r) + g(r) · B`, with `f, g : ℝ³ → ℝ`,

isomorphic to complex-valued functions (R-021).

**This step is an ansatz, not a consequence — and as written it is too strong: it makes the
one-defect state space `ℂ¹`, which §B.4 then contradicts.** The centralizer computation above
establishes which *operators* preserve the background; it does not by itself confine the
*fluctuation* to the commutant. And `span{1, B_a}` is real dimension two, i.e. **complex dimension
one** for the very complex structure just derived. A `ℂ¹` state space has a single projective
point: `span{1, B_a}` is commutative, so the one-sided rotor action and the global phase
`ψ → ψ · exp(α B_a)` coincide on it, and by the ray theorem stated below every state `R ψ_0` is the
*same* state. `Λ²(ℂ¹) = 0` as well, so no antisymmetric pairing — and therefore no singlet — can be
written on it at all. A defect that carries spin, or two distinguishable measurement outcomes, does
not fit.

**The wavefront-frame condition alone supplies a larger object.** Condition (W) by itself picks the
even blades commuting with `e_4`, namely `{1, e_{12}, e_{13}, e_{23}}` — the commutant
`Z_{Cl⁺(4,0)}(e_4)`, closed under the geometric product and a copy of `ℍ`. Right-multiplication by
the defect-selected `B_a` squares to `−1` on it, so it is a **complex vector space of dimension
two** with `ℂ`-basis `{1, e_{13}}`; left multiplication commutes with that structure by
associativity, so the one-sided L-orbit rotor action of §B.3.5 is `ℂ`-linear and lands in `SU(2)`.
The per-defect internal space that (W) alone leaves standing is a **qubit**, and its two
`ℂ`-coordinates are exactly the charge-0 and charge-`±1` parts of the `U(1)` generated by `B_a` —
the decomposition the next paragraph asks for. Nothing about §B.3.3's Born amplitude has to change
to use it: the complex overlap `z(ψ, D) = ∫ ⟨D̃ ψ⟩_{{1, B_a}} d³r` defined there, applied unchanged
on this four-blade commutant, *is* the ordinary Hermitian inner product of the resulting `ℂ²`
(R-167).

Read against this section's own open item, that **discharges the charge-sector half and shrinks the
residue from six modes to four**. The eight even blades split under `U(1)_{B_a}` into charge-0
`{1, e_{12}, e_{34}, I_4}` and charge-`±1` `{e_{13}, e_{14}, e_{23}, e_{24}}`; intersecting with (W)
gives the phase line `{1, e_{12}}` and the second `ℂ`-direction `{e_{13}, e_{23}}`. The four blades
left over — `{e_{14}, e_{24}, e_{34}, I_4}` — are precisely the ones that *fail* (W): they
anticommute with `e_4` rather than being merely unaddressed, and they are R-128's three Q-orbit
winding blades together with `I_4`, the operator that implements its lock. What they are —
additional fields, gauge redundancy, or gapped excitations — is still owed, and if any are physical
and light the framework predicts degrees of freedom that are not observed.

**What the enlargement costs, stated plainly.** (i) The uniqueness this section rests on is **not**
spent. `(W) ∩ (S) ∩ (E) = {1, B_a}` is a statement about *operators*, and the corresponding
right-multiplications are exactly the `ℂ`-linear commutant — Schur's — of the `SU(2)` action on
`Z(e_4)`; enlarging the *module* to `ℂ²` leaves it verbatim. What is given up is only the separate
ansatz that the fluctuation itself lies in the operator commutant. (ii) Condition (S) must **not**
be imposed on the state. Rotors in the plane `B_a` are *diagonal* in the `ℂ`-basis, so they fix
`ψ_0 = 1` up to phase and generate no second state from it; a measurement that distinguishes
outcomes is by construction a rotation that violates (S) — which is the geometric content of
tilting a defect's winding axis. (iii) `ψ` is then a **two-component** complex field on `ℝ³`, not a
complex scalar, so §B.3.4's envelope reduction (R-024) goes through component-wise only if the
linearized operator is `ℂ`-scalar at leading order; that is a named added premise, not a free one.
(iv) R-127 is undisturbed and in fact sharpened: the mass phase is right-multiplication by
`exp(ω τ₅ B_a/2)`, which is the *global `ℂ` scalar* of this qubit and commutes with the `SU(2)`
spin action — "the mass phase never leaves `B_a`" and "spin acts on the left" are the two halves of
the `ℍ ≅ ℂ²` picture, here supplied by the substrate rather than imported. The same left/right
division of labour sets where the internal quantum numbers live: spin and the Lorentz generators act
on the **left** (the space frame), while weak isospin acts on the **right** (the body frame), the
two commuting identically — which is why a rotation or boost of the apparatus moves the spin label
and leaves the weak label alone.

What remains open is narrower but real: restricting the fluctuation to `Z(e_4)` is still a *choice*
— weaker than `span{1, B_a}`, and motivated by (W), but not derived from it — and the four
(W)-failing blades still owe an account. The phase-sector restriction does **not** follow from the
centralizer, and the state space is **not** `ℂ¹` — a `ℂ¹` reading would be inconsistent with §B.4.

The inner product

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

**Self-adjointness, derived — by the `{1, B}` projection, not by "requiring reality".** The
obvious route fails, and is worth recording so it is not re-attempted: in a *real* Clifford
algebra every grade-0 coefficient is already a real number, so demanding that `⟨φ̃ M̂ ψ⟩_0` be
real imposes nothing whatever. It is worse than empty — reversion fixes the scalar grade, so
`⟨ψ̃ M̂ ψ⟩_0 = ⟨(ψ̃ M̂ ψ)~⟩_0 = ⟨ψ̃ M̃̂ ψ⟩_0` for every `ψ`, and the anti-self-adjoint part of `M̂`
therefore contributes *exactly zero* to the scalar expectation. The grade-0 part cannot see the
violation it was supposed to forbid.

The condition that does the work is the one §B.3.3 already relies on. Expectation values live in
the derived `{1, B}` subalgebra (§B.3.1; R-020/R-021), in which `1` is the real axis and `B` the
imaginary one (`i := B`) — and §B.3.3 makes the same point from the other side, rejecting a
grade-0-only Born formula because it *undercounts*. "The expectation value is real" therefore
means *the `B` component vanishes*:

> `⟨ψ̃ M̂ ψ⟩_B = 0` for all `ψ`. (R-166)

That is exactly the familiar `⟨ψ, M̂ψ⟩ ∈ ℝ` written in Clifford form. On `Cl⁺(4,0)` the `{1, B}`
pairing splits into `⟨φ̃ ψ⟩_0`, which is symmetric and unimodular — the Euclidean metric — and
`⟨φ̃ ψ⟩_B`, which is *antisymmetric* and nondegenerate: a symplectic form. Right multiplication
by `B` squares to `−1` and preserves both. The two are the real and imaginary parts of the
Hermitian form of `ℂ⁴`, and the condition is the vanishing of its imaginary part.

Solved (operators acting by left multiplication, ℂ-linearly — see the premises below), it returns
precisely reversion self-adjointness and nothing else. On the even subalgebra the solution space
is **two-dimensional, spanned by `{1, I₄}`**; on the full `Cl(4,0)` it is **six-dimensional,
spanned by `{1, e₁, e₂, e₃, e₄, I₄}`** — in both cases exactly the reversion-fixed subspace
`{M̂ : M̂ = M̃̂}`, since grades 0, 1 and 4 are reversion-even while grades 2 and 3 are reversion-odd.
This holds for all three L-orbit winding choices `B_a ∈ {e₁₂, e₁₃, e₂₃}`, so nothing in it depends
on which blade is taken as the phase axis (engine-exact). So `M̂ = M̃̂` (R-022) stands as stated;
only its derivation is replaced. This is the Cl-native expression of self-adjointness, equivalent
to `M̂ = M̂†` in the matrix realization.

Two limits on that forcing are part of the result rather than caveats attached to it. **The phase
sector alone does not force it.** With the states restricted to `span{1, B}`, the condition kills
only the `B` component of `M̂` and leaves seven of eight dimensions standing; it sharpens to the
right answer — `span{1}`, the reals inside `ℂ` — only once the operators are also required to
preserve that sector. The forcing needs the full even subalgebra as the state space. **And
ℂ-linearity is a named premise, not a derivation.** Over *arbitrary* real-linear maps of
`Cl⁺(4,0)` the same condition leaves a 28-dimensional space, because it admits ℂ-antilinear
pieces; restricted to maps commuting with the derived phase structure `B` — which left
multiplication is automatically — it leaves the 16 real dimensions of the self-adjoint operators
on `ℂ⁴`. That observables commute with the phase structure is assumed here, and is stated rather
than hidden. Reality of expectation values is likewise the postulate being *expressed* in Clifford
form, not derived from the substrate.

**Spectral structure — what holds, and what does not.** The four grade-3 blades `T_a` do form
an exact orthonormal set, `⟨T_a T̃_b⟩_0 = δ_{ab}` (engine-exact). Past that, the algebra supports
nothing further. The `T_a` are reversion-**odd**
(`T̃_a = −T_a`), hence *anti*-self-adjoint by the criterion just derived; they square to `−1`, so
left multiplication by them carries no real eigenvalues; and they do not commute pairwise, so they
admit no simultaneous eigenbasis. There is accordingly no "corresponding observable" of which each
blade is an eigenvector — the phrase named none, and none exists at this level. Nor are the four a
uniform quadruplet: by `e₄`-content they split 3 + 1, the three colour slots `e₁₂₄, e₁₃₄, e₂₃₄`
against the spatial pseudoscalar `e₁₂₃`. The identification of the colour trivectors, and any
route from them to the fermion spectrum, is made on physical grounds in Part C (§C.4, §C.5);
nothing in this subsection establishes it, and this subsection no longer gestures at it.

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

On the trivial background the tilde is the reverse; on the costed carrier vacuum (§A.4's rotating
reference) the reference operation is the ruled adjoint `t = α₅∘reverse` — at rest, with the boost
extension deferred to the outside↔inside dictionary — which reduces to the reverse on all `Cl(4,0)`
content, so every trivial-background statement here is unchanged.

The grade-0-only formula `|∫ ⟨D̃_n ψ⟩_0 d³r|²` undercounts: for `D = 1` and `ψ = e_{12}` (the
same physical state, phase-rotated by 90°), `⟨e_{12}⟩_0 = 0`, so a grade-0-only formula predicts
zero probability for an identical-up-to-phase state. The correct formula projects onto `{1, B}`
and squares the full complex magnitude.

*Prior art at this claim site, and what the operation is for.* Reading a quaternion-valued overlap
through a chosen complex line inside `ℍ` is not new: it is the complex-linearity restriction —
the "complex geometry" of the quaternionic-quantum-mechanics literature — constructed by Horwitz
and Biedenharn (*Ann. Phys.* **157** (1984) 432), whose quaternionic Hilbert module carries a
hierarchy of scalar products and operators graded by real, complex or quaternion linearity, and
whose working layer is the complex-linear one. Its established function is precisely the object
this framework separately lacks: it is the condition under which **tensor products of quaternion
modules can be constructed preserving complex linearity**, and with them creation and annihilation
operators for the second-quantized theory. What is this framework's own here is the *argument* for
the projection — the grade-0 undercount above — and the *selection* of the unit `B` by the defect
background (§B.3.1) rather than by hand. Naming the known function matters for scope: the
multi-defect state space §B.4.1 records as unbuilt is not an open-ended absence but a specific,
already-studied construction, and importing it would import its premises with it.

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
from a Role-3 construction carrying the channel-pairwise drag structure sketched above
**together with an offset-measure class and a read-out class: the structure alone is
demonstrably insufficient, since the naive single-fibre rule carries exactly that structure and
still violates F2**. Until such a construction is built, the Born exponent is a theorem
conditional on it.

*A second road to the same conclusion, sharing no premise with the first.* Set combinatorics alone
reach exponent 2 without Gleason and without F1–F4: for the three-slit inclusion–exclusion operator
`I₃`, any detection functional bilinear in the slit amplitudes — on any finite-dimensional state
space, with any bilinear kernel, Hermiticity and locality not assumed, provided only that the kernel
does not depend on which slits are open — is annihilated identically, while every strictly higher
homogeneous power is not (R-184, `bilinear_detection_third_order_null`). The corroboration is real
but one-way, and its cost is named: this route fixes no exponent until the observed absence of
third-order interference is adjoined, a datum the Gleason route does not need.

The substrate-level
mechanism realizing single-outcome selection is the memory dissipation of §D.5, Role 3. The
detector couples at a rate set by `|c_n|²` — the squared *configuration-space* amplitude (not the
squared *local* field amplitude). When entanglement is present, the relevant overlap is global
(`∫ d³r`), and the selection law is on the joint configuration.

**A distinct open problem: the Born *distribution*, as against the Born *rule*.** Gleason's theorem
constrains the functional **form** of a noncontextual measure on a projection lattice — it delivers
`Tr(ρP)`. In a configuration-realist framework the physically prior question is different, and is
not touched by anything above: **given the actual distribution of substrate configurations over an
ensemble of runs, why do observed frequencies match `|ψ|²`?**

Answering that needs a typicality or equilibrium argument over the substrate's own state space — a
measure on configurations together with a reason it is the *right* measure, or a relaxation argument
showing it is reached dynamically. This is precisely the burden Bohmian mechanics carries, and the
reason quantum equilibrium and the Valentini relaxation programme exist. Gleason does not reach it,
and neither does §D.5's Role 3, which addresses single-outcome *selection* rather than the
*distribution over outcomes across runs*.

The framework must eventually say which branch it is on, and the two have different costs. If
probability is ignorance of a deterministic mechanism, then TWT owes both the measure over initial
substrate configurations *and* an argument that it is Born-distributed. If instead Role 3 carries
any genuinely stochastic element, then the irreducible chance this programme set out to eliminate
(the abstract's configuration-realist claim) has been reintroduced through the back door. This
is recorded here as an **open problem in its own right**, distinct both from the Born rule's form and
from the #1 gap.

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

**Honest scope — what is delivered is FREE Schrödinger from the KG parent plus an ASSERTED `V`.**
The envelope reduction above derives the *free* Schrödinger equation; the `V ψ` term is asserted,
not derived. §D.4.6's "Where defects enter" paragraph is explicit that the defect-linearization is
**not the route taken** — the actual soliton-fluctuation problem is deferred to Paper 2, and the
framework's stated strategy is instead to *treat* the defect's static profile as a c-number
background, because a c-number background is what the QM machinery consumes.

**The deferral does not answer the technical objection, and nothing else in the corpus does
either.** The second variation of the master action about a soliton background is **matrix-valued**
— an operator on the multi-component rotor fluctuation, carrying zero modes from the broken
translations, rotations and phase (§D.4.6's own R-125/R-126 catalog exhibits exactly such modes) —
and it is not shown anywhere to reduce to a single scalar function `V(x)` multiplying a
one-component complex `ψ`. §B.3.1 already records the matching exposure from the state-space side:
its point (iii) notes that `ψ` is a **two-component** complex field, so this section's reduction
"goes through component-wise only if the linearized operator is `ℂ`-scalar at leading order; that is
a named added premise, not a free one." So the scalar-`V` Schrödinger form above is a **modelling
assumption about the fluctuation operator**, not a substrate result: until the matrix problem is
diagonalized (Paper 2) the potential term is neither derived nor shown to be derivable in this form.

(A note on the parent equation. Substituting an envelope into `□_4 Φ = 0`, the 4D *Euclidean*
Laplacian, does not work: the elliptic Cauchy problem is Hadamard-ill-posed in `x_4`, the
dispersion gives complex energy `ℰ = mc² ± icp`, and the first relativistic correction comes out
with the wrong sign. The derivation above uses the hyperbolic parent, which is what the observer
actually sees.)

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

*Import notice (companion Section 13, row I-20).* Reading exchange as a `2π` rotation in configuration
space is the Finkelstein–Rubinstein construction — an external import, registered with its premises. It
presumes the multi-defect configuration space is the standard Skyrmion one, `Q_N = Maps_{deg N}(S³,S³)`,
a space this framework has **not** constructed (five independent construction routes failed; negatives
ledger N53). What the import delivers is a two-element menu — a single-valued wavefunction is a `±1`
character of `π₁(Q_N) = ℤ₂` — and never the pick. Refusing it leaves the one-defect `Spin(4)` half-angle
above untouched and returns the fermionic option to a bare INPUT bit carrying its two empirical anchors.
The pick itself belongs to this instance (§A.6.4, node V3-11): it is contingent in the mathematics
— a non-simply-connected configuration space admits both quantization sectors and each is
internally coherent — and over-determined in the data, since the bosonic sector has no exclusion
principle and hence no shell structure and no stable bulk matter. It is excluded by the world, not
by the topology, and it costs the instance one bit. It is also blind to the family's open branch
over where the local state's `ℤ₂` sign lives (§D.3.2): both branches deliver the same `π₃` and
`π₄`, so neither can pay for this pick and this pick cannot pay for that branch.

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
an axiomatic system — *given* the two-particle tensor-product state space, which §B.4.1's
honest-scope note records as assumed rather than constructed, so what this section establishes is
compatibility, not derivation. The calculation of CHSH reaches `S = 2√2` exactly. The multipartite
Mermin–Klyshko hierarchy follows from the same commuting-rotor identity, checked at finite `n`. And the identity `ρ_A = (1/2) 𝟙`
behind no-signaling turns out to be the *same fact* as Bell-violation — locally each side is pure
noise, jointly they are perfectly ordered. Since the ingredients invite the comparison, the scope
is worth stating at the outset: nothing here evades a premise of Bell's theorem — §B.4.3 names the
premise this framework violates as **factorizability**, outcome independence at `λ = Ψ_joint`,
which is the leg orthodox quantum mechanics violates too — so this is not a construction of the
kind that claims a local, deterministic, Clifford-algebra-valued disproof of the theorem
(Christian, arXiv quant-ph/0703179).

**Mathematical setting.** One wing's internal space is the wavefront-frame commutant
`Z_{Cl⁺(4,0)}(e_4) = span{1, e_{12}, e_{13}, e_{23}} ≅ ℍ` of §B.3.1: real dimension four, and
**complex dimension two** for the complex structure R-020 forces — right-multiplication by the
defect-selected winding blade `B_a` (we use `B_a = e_{12}` by convention), which squares to `−1`
there. In the `ℂ`-basis `{|0⟩ = 1, |1⟩ = e_{13}}` this is a qubit: left multiplication by the
L-orbit rotors is `ℂ`-linear and unitary with unit determinant, so the **one-sided** rotor action
`ψ → R ψ` of §B.3.5 is the `SU(2)` action on `ℂ²`, and right multiplication by `exp(α B_a)` is the
global phase, so states are rays. No new inner product is introduced: §B.3.3's complex overlap
`z(ψ, D) = ∫ ⟨D̃ ψ⟩_{{1, B_a}} d³r`, applied unchanged on this commutant, is exactly the Hermitian
inner product of that `ℂ²`.

*Prior art at this claim site.* That a single qubit's state space is the three-sphere `S³`, with
the Bloch sphere the base of a suitably oriented Hopf fibration and the circular fibre the overall
phase, is established literature and is not claimed here as a result. It is the standard
single-qubit picture reviewed by Mosseri and Dandoloff (*J. Phys. A* **34** (2001) 10243; arXiv
quant-ph/0108137 — whose own new content is the two-qubit `S⁷` fibration, not this), and the
two-level-system geometry of states, phases and their evolution on the two- and three-sphere
developed by Urbantke (*Am. J. Phys.* **59** (1991) 503; see also his survey of the Hopf
fibration's appearances in physics, *J. Geom. Phys.* **46** (2003) 125). The delta is the
selection and the referent, not the geometry: *which* bivector plays the complex unit is fixed
here by the defect background — the `(W) ∩ (S) ∩ (E)` centralizer of §B.3.1, with R-127 locking
the observer-visible mass phase to the same blade — rather than taken as a frame convention; and
the `S³` is offered as a *physical* target of the rotor field rather than an ideal state space, a
reading that earns its keep only once the multi-defect state space recorded as unbuilt below
exists.

**The wing does not fit in the phase sector.** Writing the wing as `ψ = a + b B` in
`span{1, B_a}` and reading the overlap off the grade-0 part does **not** work, on two grounds
internal to this paper. *First*, `span{1, B_a}` is
**commutative**, so the left measurement rotor `exp(θ B_a/2)` used here and the global phase
`ψ → ψ · exp(α B_a)` of §B.3.1 are the *same operation*; §B.3.1's own conclusion — states are rays,
projective Hilbert space is a theorem — then makes `ψ_a` and `ψ_b` one and the same state, from
which no `θ`-dependent correlation can be read. *Second*, the `cos((θ_b − θ_a)/2)` such a reading
returns is the **grade-0-only** overlap, which §B.3.3 rejects by name as an undercount, using
`D = 1`, `ψ = e_{12}` as its counterexample; the phase-sector states are precisely a
one-parameter family of that counterexample. Under §B.3.3's own amplitude — the complex overlap `z`
projected onto `{1, B_a}` — the modulus on `span{1, B_a}` is 1 at every pair of angles, so the Born
probability is identically 1. And `Λ²(ℂ¹) = 0`, so the singlet below cannot even be written there.

**The half-angle survives the repair intact.** Take `ψ_0 = 1` and let each wing's measurement rotor
lie in a commutant plane *other than* the phase plane — `R_a = exp(θ_a e_{13}/2)`, or equally
`e_{23}`. These are the off-diagonal `SU(2)` generators, and they move the ray; the rotor in the
plane `B_a` is diagonal in that basis and fixes `ψ_0 = 1` up to phase, producing no second state —
which is exactly why this section's former choice of measurement plane could not generate a wing.
§B.3.3's overlap is then the ordinary `ℂ²` Hermitian inner product,

> `⟨ψ_a | ψ_b⟩ = cos((θ_b − θ_a)/2)`,

with no grade truncation anywhere, and the Born probability is `cos²((θ_b − θ_a)/2)`. So the one
ingredient §B.4.6 calls genuinely geometric — the `Spin(3)` double-cover half-angle — is unchanged.
(The two-sided sandwich `R ψ R̃` is still not the right action: on `ψ_0 = 1` it is the identity. The
half-angle comes from the one-sided spinor action, exactly as in §B.3.5.)

**What the repair changes, and what it does not buy.** The analyzer angle is no longer a rotation in
the transverse winding plane `B_a`; it is a rotation in a plane *containing* the winding axis —
tilting the defect's winding axis rather than advancing its phase. And with `ψ_0 = 1` and real rotor
angles the states explored span a **real** two-plane inside `ℂ²`, which is the ordinary
coplanar-settings Bell scenario; the second complex dimension is required for **consistency** — a
projective space with more than one point, and a nonvanishing `Λ²` — not because the wing sweeps
all of `ℂ²`.

**Where the singlet's antisymmetry would live.** The two commutant units outside the phase sector,
`{e_{13}, e_{23}}`, are not spare parts. Right-multiplication by either is *antilinear*
for the `B_a` complex structure, and `ε(u, v) = ⟨u·j, v⟩` with `j ∈ {e_{13}, e_{23}}` is
antisymmetric, `ℂ`-bilinear and `SU(2)`-invariant — the symplectic form on the wing, and the object
a singlet would be written from once a two-wing tensor product is supplied. It vanishes identically
when restricted to `span{1, B_a}`. The side matters: *left* multiplication by the same `j` is
`ℂ`-linear and gives a form that is neither antisymmetric nor invariant, and right multiplication by
`B_a` itself gives no antisymmetric form either. This does **not** construct the two-wing tensor
product — that remains imported, per the honest-scope note below — but the *pairing* is a substrate
object, living exactly on the directions the `ℂ¹` setting threw away.

### B.4.1 The TWT calculation of CHSH

Take the singlet

> `|Ψ_singlet⟩ = (1/√2) · (|↑⟩_A |↓⟩_B − |↓⟩_A |↑⟩_B)`.

**What antisymmetry does and does not do.** Antisymmetric exchange does **not** *force* the
singlet. Exchange antisymmetry constrains the
**total** state to the odd sector — and that exchange `ℤ₂` is itself the Finkelstein–Rubinstein
import (companion Section 13, row I-20), not a substrate result. It does not select a state within it — an antisymmetric spatial
factor paired with any of the three symmetric (triplet) spin states is equally odd overall. Verified
explicitly: totally antisymmetric two-defect states exist for **all four** spin states
(`‖T + T_exchanged‖ = 0` in every case). What actually selects the singlet is **angular-momentum
conservation at the source**, which is a *dynamical* fact about how the pair was prepared, not a
kinematic consequence of exchange — and dynamics is the #1 gap. The singlet is therefore taken as
given here, in line with this section's honest-scope note below.

Born rule:

> `P(↑_a, ↓_b) = (1/2) cos²((θ_b − θ_a)/2)`,
> `P(↑_a, ↑_b) = (1/2) sin²((θ_b − θ_a)/2)`.

The correlation function is then

> `E(a, b) = −cos θ_{ab}`,

and at optimal angles `S = 2√2` (R-027). **TWT reproduces the Tsirelson bound exactly.** The
`cos(θ/2)` of the one-sided rotor action's half-angle is the dimensional fingerprint of
`S³ → S²` projection.

*Prior art at this claim site.* The geometric-algebra machinery this calculation runs on is
established work of Doran, Lasenby and Gull: spinors replaced by multivectors acted on one-sidedly
by rotors, the unit imaginary of quantum mechanics played by a fixed bivector rather than an
external scalar `i`, and the extension to several particles carried out with a separate copy of
the algebra for each particle, in which — as they state — the standard unit imaginary induces
correlations between the particle spaces (*Found. Phys.* **23** (1993) 1239, developed at length
in the review chapter with Somaroo and Challinor, *Adv. Imaging Electron Phys.* **95** (1996) 271;
arXiv quant-ph/0509178). This paper cites the same authors elsewhere under their gauge-theory-gravity
work; the debt at *this* site is the multiparticle-algebra one, and it is theirs. Two things are
not taken from them. Which bivector is the complex unit is fixed here by the defect background
(§B.3.1) rather than chosen; and their multiparticle construction does not discharge what the
scope note below records as missing — it *takes* a separate algebra copy per particle, where what
this framework owes is a two-defect state space built out of its own one-defect ontology.

**Honest scope — the two-particle state space is assumed, not constructed.** The singlet above is
written in Dirac notation, and nothing in §A.5 or §B.3 builds a tensor product of two defect state
spaces out of `Cl(4,0)`; the engine has no multi-particle construction either, and its
`bell_correlation` returns `−cos(a − b)` as a closed-form expression rather than deriving it from
a joint rotor configuration. So the accurate claim is: **given** the standard tensor-product state
space and the Born rule of §B.3.3, TWT's rotor geometry reproduces the singlet correlation and the
Tsirelson bound — the `cos(θ/2)` half-angle being the one genuinely geometric ingredient. It is a
consistency result, not a derivation of quantum non-locality from the substrate. Constructing the
multi-defect state space is an open item (§B.3.5 carries the same caveat), and until it exists this
section demonstrates compatibility rather than derivation.

### B.4.2 Multipartite Mermin–Klyshko

The same rotor construction extends to `n` parties with one additional factor per party. The
per-party measurement is a rotor in the transverse plane, so the joint `n`-party correlation is
the grade-0 part of the product of `n` coplanar rotors:

> `E_n(φ_1, ..., φ_n) = ⟨exp(φ_1 B) · exp(φ_2 B) ⋯ exp(φ_n B)⟩_0 = cos(φ_1 + φ_2 + ⋯ + φ_n)`.

At the Mermin–Klyshko optimal settings `θ_j = −(j − 1) π/(2n)`, `θ'_j = θ_j + π/2`, the MK
polynomial evaluates to

> `|M_n| = 2^{(n + 1)/2}` (R-028),

the Tsirelson-type bound for `n` parties. At `n = 2`,
`|M_2| = 2√2` recovers Tsirelson; at `n = 3`, `|M_3| = 4` recovers the GHZ value. Two provenances
are worth keeping apart. The correlation identity `E_n = cos(Σ_j φ_j)` is exact at every `n`;
the evaluation of the MK polynomial at the optimal settings is *checked numerically at finite `n`*
(`n = 2`–`5`), and the value it returns is the standard MK/GHZ maximum of the Bell literature —
not a general-`n` theorem proved inside the framework.

**What this is, stated at the engine's own scope.** It is **not** "*independent* evidence that
TWT reproduces QM at every multipartite `n`" — that would over-read it. The engine's
`mermin_value` docstring is the accurate statement: *"a consistency confirmation, not a falsifier"*,
scoped to *"n = 3, GHZ/symmetric class, optimal settings."*

The reason for the narrower reading is visible in the formula. Every party's rotor lies in the
**same** bivector plane `B`, so the rotors commute and
`exp(φ_1 B) ⋯ exp(φ_n B) = exp((Σφ_j) B)` identically — the `n`-party correlation collapses to a
one-line trigonometric identity in a single algebra. There is no tensor-product structure here and
no `n` parties in any state-space sense: there are `n` angles added together. That the MK polynomial
then attains `2^{(n+1)/2}` follows from the identity, not from a multipartite substrate calculation.

A further scope note: the rotor economy is specific to the GHZ / symmetric class. The W (non-GHZ) class
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

### B.5.2 No magnetic monopoles, given the source identification

The last entry deserves a moment. **Magnetic monopoles are absent in TWT (R-033) — by the source
identification, not by algebra.**

The grade-3 slot in `∇F` is *not* empty as a matter of Clifford structure. Grade 3 in `Cl(4,0)` is
four-dimensional, and `I_4 K` is grade-3 for any grade-1 `K` — which is exactly how geometric-algebra
electromagnetism *with* monopoles is written, `∇F = J − I_4 K` (Hestenes). The engine reports the
slot's dimension rather than its vanishing: `maxwell_grade_structure` computes `∇F ∈` grades
`{1, 3}` with the grade-3 part carrying four components.

What TWT supplies is that nothing fills it. The framework's only current is `J`, the wavefront
projection of L-orbit bivector winding to grade 1 (§B.5.1), and a grade-2 → grade-1 projection
cannot produce grade-3 content. So the correct statement is **conditional on the winding-as-source
identification**: given that identification, `K = 0` and no monopole term arises. Not "there is no
place for one in the grade structure" — there is a place, and it is empty because of what TWT
identifies as the source. A different source identification would refill it, and that is the honest
re-attack handle.

### B.5.3 The Coulomb potential

A static defect's field follows from a Poisson equation sourced by the defect's bivector content.
Two things must be said plainly about that step.

First, the Poisson equation does **not** follow from `∇F = J` by differentiation. Applying `∇` to
`∇F = J` gives `∇²F = ∇J` — the source appears differentiated, not as `−J`. Second, the object
carrying a `1/r` profile is **potential-like, not the Faraday bivector**: a Coulomb *field* falls as
`1/r²`, and it is the *potential* that falls as `1/r`. Writing both as `F` would conflate
the field of §B.5.1 with the potential used here; note also that the symbol `J` denotes a grade-1
current there and a bivector source here.

What is banked is the interaction energy. For two static defects with bivector contents `Σ_1, Σ_2`
separated by `R`, the elastic overlap of their `1/r` potentials gives

> `V(R) = ⟨Σ_1, Σ_2⟩ / (4π R)`, (R-034)

with `⟨·,·⟩` the positive-definite bivector inner product of §A.5.2. Same-chirality content gives
`⟨Σ_1, Σ_2⟩ > 0` — repulsion; opposite-chirality gives `⟨Σ_1, Σ_2⟩ < 0` — attraction. **Coulomb's
law and like-repels-unlike-attracts follow from elastic overlap.** The sign rule rides the
*reversion-conjugated* inner product; under the unconjugated `⟨A B⟩_0` it would invert (§A.5.2).

*Open, and named.* The explicit construction of the static potential from `∇F = J` — which grade
carries it, and the exact Green's-function step — is **not exhibited here**. The `1/r` scaling and
the sign rule are robust (they follow from three-dimensionality and from the inner product
respectively), but the chain from the field equation to the potential is a gap, not a completed
step, and R-034's tier is scoped to the overlap energy accordingly.

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
electromagnetism. One scope line: this identification fixes what `Q` *means*,
not what `Q` *equals*. The winding supplies integer-valuedness, and with it discreteness and drift
protection; the per-state values of §C.2 come from the charge functional and its single
normalization `c` (§C.2.7), not from any winding computation. The masslessness is then **EWSB-independent**: the winding charge is conserved
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
economy: combined with §C.4's `sin²θ_W = 3/8` (a crossing-scale normalization identity, §C.4.5), the weak coupling `g`
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

is **definitional arithmetic**, not a result. It is not a "coherence success", and it is not the
case that *one geometric overlap underlies three independently measured lengths*. `r_e ≡ α² a_0` and `λ̄_C ≡ α a_0` hold **by the definitions of those
lengths**, so `r_e · a_0 = λ̄_C²` is arithmetic and carries no physical content; `α` cancels, and
the three lengths are not independent measurements but three parametrizations of one scale. The
honest statement is the narrow one: the framework assigns α a consistent role in each of the three
length definitions, which is a *check that nothing is inconsistent*, not evidence for the substrate.
R-035c is retained as a definition, not as a derivation.

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
embedding and no unifying *group* — though, as §C.4.5 now states, a single common trace form for
`Y` and `T_3` is still assumed, which is what the embedding encodes elsewhere.

**Scope, corrected.** `sin²θ_W = 3/8` is exact and native *at the scale where the substrate sets
both electroweak stiffnesses equal*. It is **not** the measured angle, and the descent does not
reach it: see the table in §C.4.5, where the one-loop run-down from `3/8` lands at `0.154–0.158` if
the crossing sits at the ruled lattice scale `Λ_L` (the lattice reading of the D4-isotropy
argument, a named premise — §C.4.5), against a measured `0.2312`. The descent does **not** give
`0.231`. The consequence for the present section is stated below.

Granted that, the weak coupling becomes

> `g² = 4π α · (8/3)`,

making `g` algebraically siblinged to `α`. **The EW sector therefore reduces to one #1-gap-gated
magnitude (α), not two** (R-035b). Same `Im χ` functional samples both — different frequencies of
one transport function. **Which `α`, though.** The relation inherits `sin²θ_W = 3/8` and
therefore holds *at the `g_1 = g_2` crossing scale*: the `α` in it is the crossing-scale coupling,
not the measured `α_em(M_Z)`. Since the descent does not reach the measured value, the relation
makes no numerical contact with laboratory `α_em`. The parameter-economy content survives — one
gated magnitude, not two — but the bridge to the measured value does not exist.

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

This is the parameter-economy hook stated cleanly. The SM has 19 free parameters; TWT pins **none** of
those magnitudes at their measured values — `sin²θ_W = 3/8` is a crossing-scale normalization
identity whose only computable descent misses the measured angle by a third (§E.2.3) — names the
four EW couplings as one open
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

**Whose gravity this is.** The induced route is a **pick of this candidate instance** (§A.6.4,
node V3-6), not a commitment of the family, and the menu it was chosen from is live: a
thermodynamic derivation, an entropic one, a tree-level gauge-gravity construction, and a
thermodynamic reading of this same medium all remain family-available — every one of them, this
route included, taxed by the same caution, that emergent metrics have been produced in many media
and emergent Einstein *dynamics* in none. Two consequences the reader should carry through §B.6.
First, no uniqueness claim here is unconditional: what is established is uniqueness *within the
banked action class under its stated premise*, and the exits are named in the same place.
Second, the family as such currently derives **nothing** about gravity — every result in this
section consumes a pinned choice, and structural gravity (one medium so one light cone, the
equivalence principle, the Newtonian limit with the right sign, compatibility with general
relativity) is owed to the family as a re-grounding on the axioms rather than inherited from
what follows.

**What the laboratory pins before mass is linked to weight.** This section connects the defect's
rotor frequency to gravitational sourcing. The framework identifies mass with that frequency
(§A.4); modern mass metrology is, as it happens, frequency metrology — which makes the first
link below unusually direct — but the identification is the framework's own, and the laboratory
facts below stand independently of it. Honesty requires stating which parts of the mass→weight
connection are measured and which are extrapolated. The measured chain has four links of very
unequal strength.
*(i) Clock ↔ inertia* is single-particle, direct, and now definitional: Penning traps read the
electron and proton masses as frequency ratios at parts in `10¹¹` (Sturm et al. 2014; Heiße et
al. 2017), photon-recoil interferometry reads `h/m` at `~10⁻¹⁰` (Morel et al. 2020), a cesium
interferometer has been operated as a clock at a subharmonic of the atom's Compton frequency
(Lan et al. 2013), and since 2019 the kilogram itself is defined through a fixed `h` (CGPM
2018). *(ii) Inertia ↔ passive weight* — what has inertia falls universally — is tested at
`10⁻¹⁵` for bulk matter (MICROSCOPE: Touboul et al. 2022; laboratory torsion balances at
`~10⁻¹³`: Wagner et al. 2012) and at `10⁻⁹–10⁻¹²` for whole atoms (Peters, Chung & Chu 1999;
Asenbaum et al. 2020) — but only coarsely for free elementary particles: neutron interferometry
agreed with gravity at the `~10%` level at first observation (Colella, Overhauser & Werner
1975), and its refined two-wavelength version still carries an unexplained `~0.6–0.8%`
discrepancy (Littrell, Allman & Werner 1997); free electrons are tested at the `~10%` level by
an experiment whose critical low-temperature shielding effect was never reproduced
(Witteborn & Fairbank 1967; the positron version was never performed); the *direction* of
antihydrogen's fall was first measured in 2023, at `~25%` (ALPHA: Anderson et al. 2023). Since
`~99%` of nucleon mass is confined field energy, the bulk tests do establish that field energy
falls like rest mass — but always in aggregate. *(iii) Passive ↔ active* — what falls also
pulls — is tested only on macroscopic bodies, as material-independence of the active/passive
ratio: `5×10⁻⁵` in the laboratory (Kreuzer 1968), `3.9×10⁻¹⁴` from lunar laser ranging (Singh et
al. 2023, sharpening Bartlett & Van Buren 1986). *(iv) The active weight of a single particle* —
that one defect sources the field this section derives — has never been measured, at any
precision. The smallest body whose gravitational pull has been detected is a `92.1 mg` gold
sphere (Westphal et al. 2021): `5.5×10²²` proton masses. Between it and one particle lie
twenty-two-plus orders of magnitude in mass — `~10²⁶` for the electron — with no direct data
anywhere in between; whether a quantum-superposed mass sources a superposed field is likewise
untested (the proposed entanglement witnesses: Bose et al. 2017; Marletto & Vedral 2017).

Single-defect sourcing is therefore an extrapolation across a factor `5.5×10²²` in mass,
empirically underwritten by the linearity of the aggregate theory and by nothing else. The
measured record fences the inside-frame effective description this section is written in, link
by link: universality of passive fall at `10⁻¹⁵` (link ii); material-independence of the
active/passive ratio at `~10⁻¹⁴` (link iii — different materials mean different binding-energy,
`Z/A` and electron-mass fractions, so composition cuts across the aggregate); and, sharpest of
all, spin-direction blindness — the gravitational mass of an electron differs by less than `~1`
part in `10²¹` between opposite spin orientations (the source's own statement: Heckel et al.
2008; the per-electron reading itself rides linearity across the pendulum's `~10²³` polarized
spins). This framework's banked route satisfies all three and *commits* to per-particle
sourcing: matter couples to gravity through the conserved `T_{μν}` alone, with `m_i = m_g`
forced by single-field monism rather than assumed (§B.6.3; engine:
`equivalence_principle_protection`) — so MICROSCOPE and its kin are passes for the framework,
not merely fences — and the two-defect potential of §B.6.1 is additive down to single defects.
That commitment is exactly what has never been tested below the `92.1 mg` scale: twenty-two
orders of magnitude in which this framework, like general relativity, predicts perfect
additivity while measurement is silent. The point is jurisdictional, in both directions: the
reader should know that per-particle weight is an inference riding aggregate linearity, not a
measured fact — and that nothing banked here predicts any deviation in the unmeasured range.
(Engine: `mass_weight_empirical_chain`; records at companion Section 10.)

**Mathematical setting.** The substrate's grain is a unit rotor at each D4 site — a 4D
orientation, six real parameters (§D.3.2) — and the continuum field `R(x)` inherits that target
unchanged. A local Lorentz frame then **follows from** the orientation field rather than being
assembled from a smaller object plus a canting direction and `e_4`: the orientation's six
generators are already the generators of `so(4)`, so the field supplies a 4D local Lorentz frame
with local `Spin(4)` symmetry directly, by acting on a fixed reference tetrad (R-036). A frame
field carries a connection; the spin connection `ω(R)` emerges from
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
(R-039). The slow-motion limit gives Newton's law `V_{12} = −G M_1 M_2 / R`, attractive (R-038) —
the linearized point-defect idealization, additive by construction; the section opening locates
how far measurement tests that —
with the force `F = −∇V ∝ M_1 M_2 / R²` — the potential falls as `1/R`, the force as `1/R²`, the
same distinction §B.5.3 draws on the electrostatic side.

The `1/r` comes from the wavefront being three-dimensional (same reason as Coulomb's `1/r`,
§B.5.3). The attraction is automatic in induced EH: matter couples to the full stress-energy
tensor through the metric; the dominant Newtonian component is `T^{00} = ρ > 0`. *Frame note:* that positivity is the
inside-frame **observed** source, not a positive-substance reading of matter. Gravity here is a
local lag of the wavefront — a geometric effect — and matter stays a defect; what is positive
frame-independently is the σ-model gradient energy `∝ |∇φ|²`, a sum of squares, which the
wavefront-locked observer reads as the gravitating mass. Consistent with that, the texture metric's
tree-level value on ordinary matter vanishes on every *computed* block — the time–space row `h_{0k}`
is an open fork (§B.6.6) — and gravity is induced only at one loop.
Newton's constant
itself, `G ~ 1/(N_eff Λ²)`, is *derived* (within an `O(1)` factor) from the Sakharov mechanism,
not put in by hand — we develop that next.

### B.6.2 Induced Einstein–Hilbert: Sakharov, with Planckian Λ scales

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

with `ρ_2(s) ∝ C_T · s²` the spin-2 spectral density — a form the dimensions fix rather than a form
chosen: the displayed integral must carry mass dimension 2, and `[dμ²] = 2`, `[μ⁴] = 4`, so
`[ρ_2] = 4`, which `s²` with a dimensionless `C_T` is what saturates. Like the `Λ²` scaling itself
this is generic-given-4D — it fixes the leading UV form, not the theory. The same counting sends the
`k⁰` piece, `∫ dμ² ρ_2/μ²`, to dimension 4: the `C_T Λ⁴` vacuum energy of §B.7.4. Both routes deliver `1/(16π G) ∝ Λ² × (dof
count)` at leading order. **Newton's constant is therefore derived** (R-037),
`G ~ 1/(N_eff · Λ²)`, rather than input. Setting `1/G = M_Pl²` — the non-reduced convention pinned
just below — inverts this to

> `Λ = M_Pl · √( π / (c_reg · N_eff) )`,

which is the relation every `Λ` quoted in this section is computed from, including all six cells of
the table below. Read in that direction it is also plain what kind of number `Λ` is: what the
Sakharov mechanism supplies is the *form*, `G ~ 1/(N_eff Λ²)`; the *value* of `Λ` is that form
inverted against the measured `G` over the `(c_reg, N_eff)` menu.

**Normalization, stated explicitly — and which `Λ` each consumer takes.** `Λ` is quotable in more
than one normalization, and mixing them corrupts every number downstream, so three things are
settled explicitly here: the Planck-mass convention, the regulator coefficient, and the assignment
of a scale to each consumer.

*Planck-mass convention (determinate).* Throughout this paper `M_Pl` is the **non-reduced** Planck
mass, `M_Pl = G^{−1/2} ≈ 1.22 × 10¹⁹ GeV`. The engine primitive `sakharov_induced_gravity` reports
`Lambda_over_MPl = 4π ≈ 12.57`, which is stated against the **reduced** mass `M_red = M_Pl/√(8π)`;
converted to this paper's convention that is `Λ = 2.51 M_Pl`. Same physics, differing by
`√(8π) ≈ 5.01`. Any comparison of the two artifacts must convert first.

*Regulator coefficient — one value, and a different thing left open.* Three numbers for `c_reg`
circulate across this framework's artifacts; they are **not** rival determinations. The engine primitive
`c_reg_from_substrate_mode_content` computes the coefficient from the framework's *own* linear-face
mode content — the six grade-2 `so(4)` channels of §D.4.6, free Bochner operator, no endomorphism and
no mass at quadratic order — and gets the heat-kernel coefficient `a_1 = 6·(R/6) = R`, hence

> `c_reg = 1/12`, exactly, in the Sakharov proper-time-cutoff variable.

| Source | `c_reg` | `Λ` at `N_eff ≈ 6` | `Λ` at `N_eff ~ 100` |
|---|---|---|---|
| An uncomputed placeholder — **superseded**: never computed, so not a rival value | `~ 1` | `0.72 M_Pl` | `0.18 M_Pl` |
| `sakharov_induced_gravity` — `G^{−1} = N_eff Λ²/(12π)`, the textbook Sakharov heat-kernel value for minimally coupled modes with a proper-time cutoff (`a_1` at `ξ = 0`); **this is also the framework's own mode-content value** | `1/12` | `2.51 M_Pl` | `0.61 M_Pl` |
| `induced_G_from_linear_face_band` (R-163) — the same coefficient written in the variable `Λ := 1/a` instead of `Λ_eff`, computed on the framework's *own* derived D4 nearest-neighbour band | `≈ 1.8` | `0.54 M_Pl` | `0.13 M_Pl` |

What makes the third row the same value rather than a second one is that both branches use the same
`a_1 = R` and the same `N_eff = 6`. The bare *ratio* between the two entries carries no evidential
weight and is not offered as any: `c_reg` is by construction the coefficient multiplying `Λ²`, so it
rescales the same way under any change of `Λ`-variable whatever the assembly behind it. The content is
in the shared inputs, not in the arithmetic.

**The reading is capped, not free.** What fixes `a_1` is the exclusion of a curvature-coupled
non-derivative term (`ξ = 0`, `E = 0`), and that exclusion is R-041's left-`Spin(4)` shift symmetry —
symmetry-protected, *not* derived from the substrate dynamics. So the conformal corner (`ξ = 1/6`,
where `a_1 = 0` and there is no induced gravity at all) is held off only at R-041's conditional tier,
and that is the real exposure in this number. One caveat is recorded with it: this settlement has
**not been independently reproduced**.

*What is open is `c_lat`, not `c_reg`.* OA-LF-ii — that curvature couples covariantly at grain scale —
moves the derived band integral `c_lat ≈ 21.8` by a factor of a few across its own stated `O(1)`
tolerance. In the proper-time variable that costs nothing: `c_reg = 1/12` is exactly
`c_lat`-independent, and the `Λ_eff = √(2π) M_Pl` it delivers is measured `G` restated in that scheme
rather than a prediction of it. Read instead in `Λ := 1/a`, the coefficient inherits roughly 93% of
the integral's support linearly. R-163's real content is therefore relocated to where it actually
lives — the grain spacing `a`, which is what moves.

*The which-`Λ` assignment.* The symbol is **split**, because the two things it
names are different physical quantities. `Λ_S` is the Sakharov
proper-time **scheme** scale — measured `G` restated, exactly `c_lat`-independent, carrying no
substrate information — and serves the induced-`G` bookkeeping only. `Λ_L ≡ 1/a` is the **inverse
grain spacing**. The assignment is scoped by what the argument actually reaches. For the two
consumers that are Taylor coefficients of the finite-range lattice difference kernel — the
§B.6.3/§E.3.3 dimension-six exposure and the D4 anisotropy corners — the only available length is
the lattice spacing, so `Λ_L` is **forced** (the bond geometry's `O(1)` factors, e.g. the D4
nearest-neighbour distance `√2·a`, are absorbed into the uncomputed coefficient `c`). The §C.4.5
descent start takes `Λ_L` as a **named premise, not a forced consequence**: the D4 second-moment
argument for `g_1 = g_2` is a dimension-four stiffness statement, distinct from the
Taylor-coefficient argument, and identifying bare-lattice stiffness equality with continuum-scheme
coupling equality owes the standard lattice→continuum matching correction (Hasenfratz & Hasenfratz
1980; Weisz 1981; Billoire 1981 — companion Section 10), uncomputed here. Two consumers are
deliberately **not** assigned: the §B.6.4 GW-dispersion denominator (the graviton is an induced
composite, so its effective scale is a property of the loop that generates it and stays
VG-5-gated; §B.6.4 uses the `Λ_L` floor illustratively only) and the §B.6.5 `ξ` residual
(reading-immaterial at `~10⁻⁴⁰`). The split moves a number quoted against a published bound — in
the *sharper* direction, and it is adopted on that understanding. No wide
`Λ ∈ [0.13, 2.5] M_Pl` bracket survives it: such a bracket would be justified only by treating the
three `c_reg` numbers as rival determinations, which they are not. The scales are:

> `Λ_S = √(2π) M_Pl ≈ 2.51 M_Pl` (exact; scheme) · `Λ_L = 1/a ∈ [0.39, 0.73] M_Pl` (central `0.54`;
> band from OA-LF-ii's `κ ∈ [½, 2]` **through the affine** `c_lat(κ) = 1.51 + 20.28·κ`; flat-band
> central `c_lat = 21.83`).

Provenance fences on the `Λ_L` band, so it cannot be over-read: `κ` scales OA-LF-ii's ~93%
sub-grain support fraction, *not* `c_lat` wholesale (wholesale would give `[0.38, 0.76]`, a
different band); the band is conditional on **(OA-LF-i ∧ OA-LF-ii) + `N_eff = 6` + the induced-`G`
identification with measured `G`** (companion Section 4), and OA-LF-i's independent `−5…−25%`
`c_lat` refinement window is *not* spanned by these corners and would widen them further. The
exclusion below survives at every corner of every window.

**The substrate cutoff lands at the Planck scale within a factor of a few** — the right order of
magnitude for an emergent-gravity cutoff. What is not put in is the `O(1)`: the scale itself is
measured `G` restated (`Λ_S` exactly so; `Λ_L` through the derived `c_lat`). That statement is
convention-independent and holds in both variables; the sharp per-consumer values are
fixed by the assignment above.
The remaining `O(1)` freedom is
localized rather than diffuse: it sits in `c_lat` (through OA-LF-ii) and in the second gate below —
the non-minimal coupling `ξ`, underived, where `ξ = 1/6` would cancel the leading term outright, and
which is exactly the corner R-041's shift symmetry rather than the substrate dynamics is holding off.

The upper-row `N_eff` is the dof count when the matter spectrum is treated as fundamental and fed
through a standard heat-kernel sum. The exact number depends on conventions (Weyl-vs-Dirac
weights, transverse-vs-longitudinal vector counting, scheme of the heat-kernel coefficient
`c_reg`); under typical conventions it lands at `O(100)`. The full convention pinning lives at
§D.5 with the rest of the substrate-dynamics machinery; for the bracket here, **what matters is
that the upper-row `N_eff` is order-of-magnitude `10²` and the lower-row is order-of-magnitude
`10⁰`**.

The matter-as-defect ontology favors the low-`N_eff` reading (the fermions and gauge bosons are not
independent fundamental fields — they are textures and spin-waves of the one rotor field), i.e. the
`N_eff ≈ 6` column of the table above. At `c_reg = 1/12` that column reads
`Λ_eff = √(2π) M_Pl ≈ 2.51 M_Pl`; the `0.54 M_Pl` entry is the same result expressed as `1/a`, and
`0.72 M_Pl` belongs to the superseded placeholder. Which of the first two a given downstream quantity
is evaluated at is fixed by the assignment above — the Sakharov/`G` bookkeeping stays in `Λ_S`,
every *lattice*-dispersion consumer (per the scoped assignment above) takes `1/a` — not by any
residual disagreement about `c_reg`.

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
the curvature couples covariantly at grain scale, a statement about the *operator*. The second
is where the old regulator freedom now lives — it carries the bulk of the integral's support —
so the `O(1)` uncertainty is *relocated and localized*, not removed, and the bracket keeps its
conditional status. Read with `Λ := 1/a` the result sits at `c_reg ≈ 1.8`; read in the proper-time
variable `Λ_eff` the same computation is `1/12`, and the two branches are identified by sharing
`a_1 = R` and `N_eff = 6`. The line this paragraph used to carry — a factor `≈ 21.6` apart from
`sakharov_induced_gravity`, with the reconciliation open between two banked primitives — was wrong
twice over: it mis-stated the number (the derived band integral is `c_lat ≈ 21.8`) and it described a
change of `Λ`-variable as a disagreement. What OA-LF-ii moves is `c_lat`, hence this branch's
normalization, not the coefficient. The
convention-independent statement that survives either way is that the grain spacing is Planckian
within a factor of a few **given the `G` match** (the inversion I-3 effects; the identification is
never derived from the substrate side) — which is the bracket's actual content. The value is an idealization of a
gapless shared band; the canted vacuum's two Goldstone modes and four gapped ones would soften it by
some tens of percent.

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

The complementary rotational-anisotropy bound is closed by the D4 point group, which drives
polarization-averaged anisotropy to dimension eight (R-165, given §B.1.5's five premises,
including the scalar-kernel premise and the operative-symmetry premise — the theorem is proved at
the full point group, while the drive leaves only the order-48 stabilizer of `e₄`, at which an
anisotropic spatial quartic is permitted and is absent by the bond set's computed zero spatial
fourth moment rather than by symmetry) — at the *grain* scale; the separate cell-scale question,
whether the emergent cell pattern carries long-range space-fixed orientational order, remains open
as §E.3.4 SC-2. The dimension-four boost bound is closed by matter-as-defect — given the
one-medium universality premise (import I-22, whose species-independence leg is load-bearing
there and currently UNSUPPORTED, §C.2.5-class conditioning). What survives is the
**rotationally invariant dimension-six residual**, conventionally written
`E² = p² + m² + η⁽⁴⁾ p⁴/M²_Pl`. The theory-side object is therefore **not** an energy-dependent `δ`
but a single energy-**independent** coefficient `η⁽⁴⁾`, which every dimension-six probe — photon,
electron, proton — tests simultaneously.

**Two normalizations, kept apart.** `η⁽⁴⁾` is by definition the coefficient of `p⁴/M²_Pl` — the
convention the published bounds are quoted in. The substrate's own natural form is `c · p⁴/Λ²` with
`c = O(1)`, since `Λ` is the substrate cutoff. The two are related by `η⁽⁴⁾ = c · (M_Pl/Λ)²`, so
"the substrate's natural coefficient is unity" means `c = 1`, **not** `η⁽⁴⁾ = 1`. That factor is
the entire content of what follows.

**The `Λ`-symbol collision — resolved by the split above.** Two
distinct scales can wear that symbol, and they differ by a factor of about five. §B.6.2's
Sakharov coefficient is written in the heat-kernel proper-time truncation variable `Λ_S`, which at
`N_eff = 6` and `c_reg = 1/12` is the pure number `√(2π) M_Pl` and is *exactly* independent of the
lattice — it is measured `G` restated in a scheme, and carries no substrate information. The
dispersion relation above is something else: it is a Taylor expansion of a finite-range difference
kernel on the grain lattice, and the only length such an expansion can produce is the bond length,
`E² = p² + c·a²p⁴ + O(a⁴p⁶)`. Its denominator is therefore `Λ_L ≡ 1/a`, the inverse grain spacing.
The two are related exactly by `Λ_S = √(c_lat)·Λ_L`, with `c_lat ≈ 21.8` the derived band integral
of §B.6.2's linear-face computation — they are not one quantity in two schemes, since under a change
of kernel `c_lat` and the quartic Taylor coefficient move by different factors. **The lattice-dispersion consumers take `Λ_L`
(per the scoped §B.6.2 assignment — this exposure is one of
the two *forced* Taylor-coefficient consumers)**, with the consequence: the naive value
reads `η⁽⁴⁾ = c·N_eff·c_lat/(12π) = c·c_lat/(2π)`, *linear* in `c_lat`, so its entire uncertainty is
the OA-LF-ii uncertainty of §B.6.2 and nothing else's — a narrower bracket whose favourable end is
*worse*, not better.

Setting the substrate coefficient `c` to unity at the ruled lattice scale gives
`η⁽⁴⁾ = c_lat/(2π) ∈ [1.9, 6.7]`, central `3.5`. (The bracket's whole width is the `Λ_L` band's:
`c_reg = 1/12` is a single coefficient written in three `Λ`-variables, not three rival values, so
no wider `η⁽⁴⁾ ∈ [0.16, 59]`-class bracket is warranted.)
**This is excluded — at full conditioning split: unconditionally by about one order (Auger 2022's model-independent hadronic bound, `η⁽⁴⁾_p < 0.149`, superluminal branch, the one analysis of that kind), and by six to seven orders only under pure-proton composition, which Auger's own data disfavours.** The conditional corners, each with its condition: photon `ξ⁽⁴⁾ ≲ 10⁻⁸` (a projected bound — "not real constraints" in its authors' words — contingent on a UHE-photon detection that has not occurred; plus pure-proton GZK secondaries), electron `−10⁻⁷ ≲ η⁽⁴⁾ ≲ 10⁻⁶` (the same pure-proton-conditioned rectangle; AT LEAST ONE side of it is the projected γ-decay line, and which sides is unresolved — Liberati 2013, eq. 77, v1 numbering = eq. 75 in v3), proton `−10⁻³ ≲ η⁽⁴⁾_p ≲ 10⁻⁶` (Liberati 2013, eq. 78, v1 numbering = eq. 76 in v3, 99% CL, pure-proton composition; the `−10⁻³` corner is a subluminal grid edge),
and equivalently `δ^π_p < 4.5 × 10⁻²³` from the Auger spectrum above the GZK energy (Stecker 2009,
eq. 18).

**The framework does not claim `c = 1`, and it cannot presently compute `c`.** The coefficient is
fixed by the substrate strain-mode dispersion, which is the #1 gap (§D.5; the engine gates it).
Survival requires `|η⁽⁴⁾| ≲ 10⁻⁶` in the photon and superluminal-matter channels. The one
suppression the framework can point to — the defect form factor — scales as `(f_π/M_defect)² ~ 10⁻²`
for the proton and does not apply to the photon at all, since §B.5.4 makes the photon a *bulk*
strain mode with no internal structure. (This is one of the places where the ANW *fitted* `f_π`
of the Opening's input list feeds a *physical* estimate rather than an internal Skyrme relation.
Substituting the physical decay constant in ANW's own normalization, `F_π ≈ 186 MeV`, moves the
estimate by about a factor of two — immaterial against the exposure's conditional span, but
the substitution is the honest one to make here, and the estimate should not be read as though
`129 MeV` were a measured input.) **This is recorded as an open exposure (§E.3.5(4), §E.3.3
VG-6), not as a passed test.** Coefficients are defined in the substrate rest frame, which the
framework identifies with the cosmological comoving (CMB) frame (§B.4.5) — the same frame the cited
bounds use.

**Whose exposure this is, stated exactly.** It belongs to **this candidate instance**, not to the
family (§A.6). Every link that turns the ontology into a number here is a pinned choice, and there
are three in series: a **regular** arrangement supplies the Taylor expansion of a finite-range
kernel (node V3-1); the **back-fit** size fixes the only length that expansion can produce, `a`
(node V3-1 again, through the gravity anchor); and **one** induced-gravity chain is what denominates
that length in Planck units at all (node V3-6). Change any of the three and the arithmetic above is
not merely re-run — it loses its input. What the family retains if this instance falls is
everything the exposure does not touch: the axioms, the structural results that consume no pinned
choice, and the dimension-four protection, which is matter-as-defect and survives any arrangement.
What it emphatically does **not** retain is a defence. A family member with an irregular
arrangement or a continuum medium does not inherit this number because it has not yet computed
one — and, on present knowledge, a discrete arrangement that keeps finite bond valency and claims
Lorentz invariance is excluded outright (companion Section 13, row I-26), so a member proposed at
that branch owes a statement of which of the three it gives up. The exposure is instance-level;
the *problem* is the family's.

**The magnitude channel is also where the known radiative loophole lives.** Collins, Perez,
Sudarsky, Urrutia and Vucetich showed that in an interacting theory regulated by a
Lorentz-violating cutoff, violations generically percolate into low-dimension operators with
unsuppressed coefficients. The D4 fourth-moment isotropy that removes the *anisotropic* channel is
robust to this in tensor structure — a counterterm generated by a point-group-preserving regulator
is itself point-group-invariant, so its analytic quartic part is again isotropic — but it is no
answer to the percolation problem itself, which concerns the **magnitude of the isotropic
coefficient**: exactly the open-exposure channel of the table below (import I-28). Nor does the
framework possess an argument in either direction about what the outside↔inside projection does to
that magnitude — whether the substrate coefficient reaches the observed dispersion at full strength
or suppressed — because the projection is unbuilt (I-19 premise (e)). The ceiling is therefore a
constraint on the analytic, unsuppressed reading; no wash-out is claimed, and none is excluded.

*Import notice:* two registered imports meet in the paragraph above. The `Λ_L` band that converts a
coefficient of unity into the number `[1.9, 6.7]` rides **I-3** (the grain spacing `a` is fixed by
inverting measured `G` through the Sakharov one-loop form), which
is OPEN — strike it and the *size* of the naive value becomes unstated, though the exposure itself
does not go away, since the framework would then owe both `Λ` and `η⁽⁴⁾`. The published limits are
imported as data under **I-19** (an inside-frame data bridge, sibling of I-6); strike that row and
the exposure statement reverts to "uncomputed and untested", while the D4 dimension-eight anisotropy
result is unaffected — its moment and invariant-dimension identities are pure lattice facts,
though the dimension-eight *inference* they carry rides §B.1.5's five premises (P-op included). Both retirement handles are the same object: the
§D.5 kernel.

| Face | Order | Magnitude at `E = 10¹¹ GeV`, `Λ_L` across the ruled band (§B.6.2) | Status |
|---|---|---|---|
| dim-4 relative-boost LV between species | — | 0 (R-016, structural) | closed (tree-level, structural) / open (radiative, I-22) |
| dim-4 rotational anisotropy | — | 0 on the point-group-symmetric bond set; the §D.4.3 spiral vacuum breaks the point group (premise P-gs), leaving a species-universal `O(q²)` splitting absorbable by the I-22 rescaling class | closed-conditional (P-gs ∧ I-22) |
| dim-6 **anisotropy** | `(E/Λ)⁴` | `2.0 × 10⁻³¹` (loose corner `Λ_L = 0.39 M_Pl`) … `1.6 × 10⁻³²` (tight corner `Λ_L = 0.73 M_Pl`); pushed to dim-8 by D4 fourth-moment isotropy | structurally out of range for the polarization-averaged dispersion **given §B.1.5's five premises, P-op included** (at the driven subgroup the spatial quartic is *permitted*; it is empty because the coupling is constant on the full 24-bond orbit — full-orbit isotropy, with the `±4` split as the advance-axis sensitivity decomposition, R-185); a nonzero dressed Γ survivor (§D.5.7 assembly record, #1-gap-routed) would open a dim-6 polarization-splitting anisotropy facing SME-type sidereal bounds — coupled to the second-D exposure (family-tree V3-2a) |
| dim-6 **isotropic** `c · p⁴/Λ²` (≡ `η⁽⁴⁾ p⁴/M²_Pl`) | `c (E/Λ)²` | `c` **uncomputed**; `c = 1` ⇒ `η⁽⁴⁾ ∈ [1.9, 6.7]`, excluded per the E21 split (~1 order unconditional / 6–7 conditional; §B.6.3) | **open exposure** |

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
stable medium, and it is massless: matter couples covariantly through the spin connection, the
induced action is diffeomorphism-invariant, and there is **no graviton mass term at all**. The only
preferred-frame remnant is the dimension-six *dispersion* correction `c (k/Λ)²`, which vanishes as
`k → 0` and therefore cannot produce the Yukawa suppression that graviton-mass bounds constrain —
it is a different observable, bounded separately. Its coefficient `c` is the same #1-gap-gated
object §B.6.3 records as an open exposure, but the conclusion here does not turn on it: across the
band where GW dispersion is actually measured, `(k/Λ)²` evaluated **illustratively** at the lattice
band's floor (`Λ_L = 0.39 M_Pl`, §B.6.2 — illustrative only: the GW sector's own effective `Λ` is a
property of the induced-EH loop and remains VG-5-gated, deliberately unassigned in the which-`Λ`
split) runs from `7.7 × 10⁻⁹¹` (LISA, `10⁻³` Hz) to
`7.7 × 10⁻⁸¹` (LIGO, `10²` Hz) — more than sixty-five orders under the tightest dispersion
constraint `|c_GW/c − 1|` of order `10⁻¹⁵`, and the margin is insensitive to any remotely Planckian choice. (The band value is a *naturalness* estimate, not an upper bound
on `c`; the point is only that the margin is enormous even there.) The masslessness conclusion is
structural and the dispersion margin is coefficient-insensitive; the coefficient itself remains open
(§E.3.3 VG-6). For a stable medium, every physical propagating mode has
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
`(f_π/Λ)² ~ 10⁻⁴⁰`-class (`2–8 × 10⁻⁴⁰` on the `Λ_L` band; the which-`Λ` reading is immaterial
here and this consumer is deliberately not force-assigned, §B.6.2) — same protection
class as the weak-equivalence-principle residuals, negligible.

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
gauge-projection postulate). (It is not an Urbantke-family object: the Urbantke metric is *cubic*
in its two-forms where this bilinear carries a single epsilon — companion Section 10 scope note —
so that literature's signature/reality theorems do not transfer here.) The Schur-lemma uniqueness step is exact — the commutant is
2D, `{id, I_4}`; the `c_1 = 0` step requires the gauge-projection postulate, which remains an
open premise (companion Result Index, R-042). What that postulate *says* is worth making explicit,
because it is the same statement as the baryon result below and not an independent one. Both the L-
and the Q-orbit are exactly balanced between SD and ASD, so for any such blade `A` the `I_4`-twisted
term is blind, `⟨A I_4 A⟩_0 = 0`, while the untwisted one is not, `⟨A A⟩_0 = −|A|²` — the `c_1` term
alone would therefore give `h(A, A) = −c_1 ≠ 0`, a tree-level metric dimple from ordinary matter.
Demanding the Sakharov separation — that matter source gravity through loops, not through a
tree-level texture — *is* `c_1 = 0`. Gauge projection and the Sakharov premise are **one** premise,
not two (engine: `texture_metric_candidate`, `U_uniqueness`). The structural geometry is therefore **closed
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
`θ₀ > 2` threshold (R-145) is that the SD legs must beat the flat background (`‖P‖ > 1`), so on
this background no perturbative texture is Lorentzian and the Euclidean→Lorentzian transition
passes through a degenerate metric — light-cone birth.

**Three fences belong with that threshold (scope note).** *(a) It is a statement about the banked
convention* `g = δ₄ + c₂h`, whose `δ₄` is the outside-frame Euclidean background of Axiom A-1a. The
menu, the `λ_max(g) ≥ 1` floor and the exclusion of all-timelike are carried by those `δ` legs
rather than by `h` — replacing `δ₄` by `η = diag(−1, 1, 1, 1)` with the *same* `h` reverses each of
them — so they are facts about the convention, not free-standing facts about the texture bilinear.
*(b) The threshold's numerical value rides the undetermined normalization* `c₂` of R-042 (`h` is
unique only up to scale): `‖P‖ > 1` says `|Ω| > 1/√c₂`, and `√c₂` is a length the framework has not
fixed. *(c) The threshold does not, and cannot, put the Lorentzian structure of §B.1–§B.5 at risk.*
That structure is algebraic — the `φ` embedding `γ⁰ = e_4`, `γʲ = e_4e_j` of §B.1.1, which satisfies
the Dirac relations at every amplitude — and §B.1–§B.5 carry no texture-metric dependence at all.
The two Lorentzian faces are therefore *separate*: §B.1's is kinematic and unconditional, §B.6.6's is
dynamical and amplitude-gated. Nothing in this paper shows they agree; constructing the map between
them is an open coherence item (negatives ledger N56), and until it exists the "light-cone birth"
phrase should be read as FRAMING about the texture metric alone, not as an account of how the
observed light cone arises.

**No conflict with §B.6.1 — but its link is owed a value.** §B.6.1 linearizes the Newtonian limit
about `η = diag(−1, 1, 1, 1)` while this section writes `g = δ₄ + h`. These are not competing
backgrounds: consequence (ii) below *is* the map — whenever `g` is Lorentzian it reduces to
`g = eᵀηe`, so §B.6.1's `η` is the tetrad frame of a finite-amplitude Lorentzian vacuum. What is
owed is only that vacuum's *value*, which is exactly the named EOM residue (the signature pick).
Relatedly, `Ω = 0` is not the physical expansion point either: per §D.4.6 the substrate ground state
is a helimagnet whose twist-gauge Maurer–Cartan form carries a *constant* background `Ω_vac ∝ q`.
Two consequences are worth recording as leads, both **CANDIDATE**. A single-blade (planar) helix has
exactly balanced SD/ASD content, so `texture_metric_candidate`'s P6 fact gives `h = 0` on it
identically — only a chirally *imbalanced* `Ω_vac` can move the signature, and the blade content of
the D4 ground state is not established here. (This is P6 alone; the baryon vanishing above needs the
strictly stronger L×Q cancellation as well.) And about a nonzero `Ω_vac` the difference
`h[Ω_vac + δΩ] − h[Ω_vac]` is *linear* in `δΩ` rather than quadratic — immediately, since `h` is
bilinear — which is the one place a linear graviton could enter a construction that has none at
`Ω = 0` (R-042 honest-tier (b)).

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

**What the texture metric does *not* do: baryons.** One computed fact belongs in the body rather
than in the engine alone, because it bounds everything above. Evaluated on the standard `B = 1`
Skyrmion — whose winding lives in the Q-orbit `{e_{14}, e_{24}, e_{34}}` — the texture metric
vanishes on every computed block: the spatial block `h_{kl} = 0` (k, l = 1, 2, 3) exactly, and the time row/column under the static ansatz `Ω_0 = 0` — a *premise*, not a result: §A.4's mass ontology (R-123) makes a massive defect's rotor `x_4`-dependent on the lock, and the `h_{0k}` row has not been computed anywhere in the corpus. R-146's cross-term identity (`h(B_L, B_L) = h(B_Q, B_Q) = 0` exactly,
`h(B, B) = 2⟨B_L I_4 B_Q⟩_0`) supplies half of this and no more: it kills the `Q×Q` block, but the
`B = 1` hedgehog's Maurer–Cartan form is *not* pure Q-orbit content. Writing
`R = cos f + sin f · Q̂`,

> `Ω_k = (∂_k f) Q̂ + sin f cos f (∂_k Q̂) − sin²f · [Q̂, ∂_k Q̂]/2`,

whose last term is L-orbit, generated by the substrate's own `[Q, Q] = −2L` commutator. The
surviving `L×Q` Hodge cross terms are individually nonzero; what makes `h_{kl}` vanish is that they
cancel **exactly**, `⟨Ω_k^L I_4 Ω_l^Q⟩_0 = −⟨Ω_k^Q I_4 Ω_l^L⟩_0` for every hedgehog configuration
(at the north pole with `f = π/4`: `+0.25` against `−0.25`). `h_{00} = 0` holds separately, and more
robustly than the recorded warrant states. That warrant ("the static `Ω_0` vanishes, and the `Q×Q`
`I_4` pairing is zero at all orders of Q-orbit content") **names the wrong orbit for the framework's
own selected mass axis** — R-128 locks the baryon mass phase to `û = ±I_4 B_q`, which is an
**L-orbit** blade. The zero nevertheless survives *every* axis on the R-127/R-128 menu, because every
`Spin(4)` bivector is SD/ASD-balanced, so `⟨û I_4 û⟩_0 = 0` identically. **The conclusion is
therefore stronger than the argument that was given for it**, and no admissible mass-phase axis
produces a tree-level Newtonian `h_{00}`.

**What the static ansatz concealed — the open fork.** Setting `Ω_0 = 0` is a *premise*, and §A.4's
own mass ontology forbids it for a massive defect: mass **is** the meta-time rotor frequency, and
R-123 makes that an explicit `x_4`-dependence on the wavefront lock. Restoring it with
`Ω_0 = (k_4/2) û` leaves `h_{00}` and `h_{kl}` untouched but makes `h_{0k}` generically nonzero — a
single L×Q Hodge pairing with no partner term to cancel, `h_{0k} ∝ ω f′(r)`, linear in the mass. Whether
that row is pure gauge, a genuine stationary cross term, or exactly zero depends on how R-128's
single-blade lock extends over the hedgehog *field*, which this framework does not fix: the
co-rotating extension gives an exact 1-form `h_{0k}` *row* (curl-free, removable by a time shift —
the row's linearized Riemann vanishes; the same extension's slice-conditional oscillating `h_{kl}`
is a separate matter and is not gauge); the
rigid extension gives a non-removable gravitomagnetic-type term; the conjugating extension
`R = A(τ_5) R_h A^{-1}` gives `h ≡ 0`. **This is a located gap, not a result**, and nothing downstream
may assume a branch. Note what does *not* change under any branch: there is no `1/r` Newtonian tail
anywhere in `h` (the surviving row falls as a dipole, `~ω/r³`), so baryons still source gravity
through the Sakharov `T_{μν}` route of §B.6.2, which is untouched. The prior art cuts against the
optimistic reading too — in every known gravitating soliton with internal rotation (boson stars,
spinning Skyrmions) the internal frequency sources the **Newtonian** block, which the texture
bilinear is structurally blind to, and frame dragging cannot be switched on infinitesimally.

The `h_{kl} = 0` result is
engine-computed in the dedicated primitive `texture_matter_gravity_coupling` (nine checks, including
the cancellation over 20 random hedgehog configurations built from the exact `R̃ ∂_k R`; an earlier
hand-formula that made `h_{kl}` look nonzero carried a sign error — negatives ledger N26), and
asserted independently inside `texture_metric_candidate`. The result is exact given the hedgehog
ansatz. Since baryons carry essentially all the mass in
the universe, **the texture metric's computed blocks vanish on the objects that dominate the gravitational source — and no admissible mass-phase axis produces a tree-level Newtonian `h_{00}`; the uncomputed `h_{0k}` row is the open fork named above.**

This does not leave gravity sourceless, and the distinction is the point. Read the other way round,
the vanishing is not a shortfall of the construction but the **Sakharov mechanism made explicit** —
it is the same separation that fixed `c_1 = 0` above, now seen on the object it was about, and the
two are therefore one premise rather than two. The identification is nonetheless not empty:
`c_1 = 0` by itself kills only the `Q×Q` block, and that the surviving `L×Q` cross terms cancel too
is an independent exact fact — it is what makes the premise *satisfiable* on the computed blocks — `h_{kl} = 0` and `h_{00} = 0` on the baryon for **every** `c_2` — rather than over-determined; the identification's full-`h` form is conditional on the open fork named above. Baryons source gravity
through the **Sakharov route** of §B.6.2 — their rotor kinetic energy enters `T_{μν}` and induces
EH at loop level — and that is the route this paper actually uses. What is absent is a *direct*
tree-level coupling: an L–Q-mixing mechanism letting baryonic content source `h_{μν}` itself. The
engine records this as unresolved, and it is a **located gap**, not a closed door.

Read together with R-164 (no tree-level EH anywhere in the banked action class; ledger N51) and with
`texture_tetrad()` — which *raises* `UnderivedError`, the ten metric degrees of freedom being
unconstructed — the honest status of this section is narrower than its length suggests: the
first-order scaffold and the Gauss-equation face close at the **structural** level, while the tetrad
itself, `C_T`, and any direct matter coupling remain open. §B.6.6 is a completed kinematic scaffold,
not a completed gravity sector.

### B.6.7 The unification

Combined with `γ = 1` from matter-as-defect (B.6.3), the induced EH term satisfies all three
conditions for physical gravity on TWT-structural grounds:

| condition | reduces to |
|---|---|
| magnitude Planckian (`Λ_S = √(2π) M_Pl`, `Λ_L = 1/a ∈ [0.39, 0.73] M_Pl`; `c_reg = 1/12`; which-`Λ` split at §B.6.2) | substrate spectral density and cutoff |
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
- **GW170817 multimessenger consistency.** `|c_GW/c − 1|` of order `10⁻¹⁵` is automatic for matter-loop
  induced gravity riding the same wavefront — `c_GW = c_γ` structurally, not coincidentally.

---

## §B.7 — The cosmic frame

The arrow of time, the asymmetries it does and does not unify, the constancy of `c`, and the
cosmological constant.
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

### B.7.2 One asymmetry from the wave's direction — and what the other two still need

Three observed asymmetries usually treated as independent (R-044):

- **Thermodynamic arrow** — entropy increases toward the future.
- **Causal arrow** — causes precede effects.
- **Weak handedness** — parity violation, weak sector left-handed.

In TWT these are not three independent cosmological inputs — but neither are all three
manifestations of one fact. **One** of them, the causal arrow, is the observable face of the wave's
propagation direction `+e_4`; weak handedness is selected by a datum on an orientation the
framework does not pin, and the thermodynamic arrow is correlated with `+e_4` only partially — the
paragraphs below say exactly how far. The causal arrow is `+e_4` directly. **Weak handedness does
not follow from `+e_4` alone.**
Chirality is the `I_4`-grading of the substrate's rotation algebra — `I_4` is central in the even
subalgebra, squares to `+1`, and grades the self-dual triple by `+1` and the anti-self-dual triple
by `−1` — and the orientation reversal `x ↦ e_4 x e_4` **fixes `+e_4` exactly** while flipping `I_4`
and exchanging the two chiral factors. One and the same propagation direction is therefore
compatible with either handedness, and the propagation axis does not define chirality. What `+e_4`
fixes is the causal arrow. *Which* chiral factor the weak force gauges is settled without a further
choice, but by a different support: the two chiral factors are exchanged by an orientation
relabelling, so naming one of them "the weak one" costs nothing, and the alternative host that is
*not* a relabelling is excluded by the right-handed fermions' weak-singlet character (§C.4.2). The
`SD`/`ASD` label is an orientation convention that nothing in the framework pins. The thermodynamic arrow is the medium's irreversible
response to its own drive — the retarded boundary condition plus observer-relative coarse-graining
giving entropy increase; **but the low-entropy past is a separate cosmological input, and the
framework reduces rather than fully derives the second law**.

**Counterfactual, and where the correlation is not derived.** In a universe with the wave
propagating along `−e_4`, the causal arrow reverses; whether the weak handedness reverses with it
depends on the relabelling used, since an orientation-preserving one leaves `I_4` fixed. The
thermodynamic arrow's behaviour under wave-direction reversal is more subtle: it depends on whether
the cosmological low-entropy boundary condition is correlated with the wave's propagation
direction. If the low-entropy IC is itself a wavefront-direction phenomenon — plausible, **not
derived in this framework** — it flips with the causal arrow. If the low-entropy IC is independent
of propagation direction, the thermodynamic arrow stays set by whichever direction the low-entropy
boundary lies in. **In either case it is the causal arrow alone that `+e_4` fixes** — the weak
handedness rides an unpinned orientation together with the right-handed-singlet datum — while
**the thermodynamic arrow has a separate, only partially-correlated origin**.

This is a unification claim, and the count it supports is smaller than an unqualified reading
suggests. The SM treats parity violation as an empirical fact added by hand (`V−A`); the framework
does not derive it from `+e_4` either, but it locates it in the same algebra, with the weak
assignment of §C.4.2 doing the selecting. The honest ledger is therefore **one** asymmetry from the
wave's propagation direction — the causal arrow — plus weak handedness, which rides an orientation
convention nothing in the framework pins together with the two named supports of that assignment (a
structural premise the paper does not derive, and the right-handed fermions' weak-singlet
character), plus **one separate cosmological input** (the low-entropy past) that the thermodynamic
arrow still requires. One from the wave's direction, not three; and the second law is *reduced*
here, not derived.

### B.7.3 `c_meta = c` on average

For a uniform offset `c_meta ≠ c` across the entire wavefront, the framework provides no
observational signature: a global rescaling of all length and time scales would be removed by
coordinate redefinition. **`c_meta = c` when averaged across the wavefront** (R-045) is therefore a
**definition**, not a prediction: it cannot be a structural prediction, because a statement whose
negation is unobservable makes no claim. It fixes a convention, and
that is all.

All the content is in the **differential** version — sector-dependent or epoch-varying `c_meta`,
which *is* observable and *is* a falsifier (canonical row 6). That is where the section's testable
claim lives, and R-045 should be read as the convention that makes the differential statement
well-posed.

A time-varying global `c_meta(τ_5)` is observable as cosmological expansion dynamics (and is a
falsifier handle — sector-dependent or epoch-varying differential `c_meta` is canonical falsifier
§E.3 row 6, closely tied to the `c_GW = c_γ` constraint §E.3 row 1).

### B.7.4 The Hubble radius as causal/crossover scale; Volovik's dissolution of Λ

The Hubble radius is the **causal/crossover scale** at which wavefront-expansion dynamics overtake
well-attraction (R-046) — not the geometric radius of curvature. The §A.2 topological-`S³`
identification does not commit to a finite radius of curvature equal to `R_H`. The genuine
geometric curvature radius, if any, must satisfy `|Ω_k| ≲ 0.0026` (Planck 2018 + BAO, 1σ upper),
giving `R_curv ≳ 20 R_H` — effectively spatially flat at observational precision.

**Dark energy and the cosmological constant.** Induced gravity (§B.6) cannot consistently disclaim
the cosmological-constant problem: the same heat-kernel expansion that yields `1/(16π G) ~ C_T Λ²`
at order `k²` generates a vacuum energy `~ C_T Λ⁴` at order `k⁰`, with naive value `~ M_Pl⁴ ≈
10¹²⁰ ρ_obs`. This is the standard Λ catastrophe. (Which-`Λ` note: the `Λ²` coefficient is `Λ_S`
scheme bookkeeping, while a `Λ⁴` mode sum would read as a lattice quantity; the assignment is
deliberately left open — immaterial at the `10¹²⁰` order-of-magnitude level, it would matter only
if VG-2 ever became a number.)

Volovik's self-sustained-medium identity supplies the native resolution (R-047). For a
self-sustained quantum medium at zero external pressure, the Gibbs–Duhem relation

> `ε − μ n = −P = 0`

forces the **gravitating** vacuum energy to vanish *exactly in equilibrium*. Sub-Planckian and
trans-Planckian contributions cancel as a thermodynamic identity, not as a tuning. The substrate is
exactly the textbook self-sustained medium.

The TWT-specific adaptation. The substrate is driven-dissipative, not equilibrium, so the
gravitating vacuum energy need not vanish exactly; the deviation from equilibrium is set by the
drive. What that deviation is *worth* is an off-equilibrium computation at the §D.5 #1 gap, and it
is not done here. Two readings of the frequently-quoted `Λ ~ H²` must be kept apart, because only
one of them survives contact with data:

- **Dynamical** — `ρ_vac(t) = 3ν M̄_Pl² H(t)²` at every epoch (`M̄_Pl` the reduced Planck mass).
  **Excluded.** Substituting into the Friedmann constraint gives `Ω_vac(z) ≡ ν` identically, so the
  vacuum *fraction* is epoch-independent and matching today forces the same ≈ 68.5 % at
  recombination and at nucleosynthesis. The arithmetic and the bounds are in §E.1.1.
- **Present-epoch** — `ρ_vac` is constant, and `ρ_vac ≈ 3Ω_Λ,0 M̄_Pl² H_0²` is a statement about
  *today*. This is the reading TWT is entitled to, and the one the engine already carries:
  `kernel_overdetermination_table` writes it as `ρ_Λ = c M̄_Pl² H_0²` with the reduced Planck mass —
  `H_0`, not `H(t)` — and already flags `c = 3Ω_Λ` as semi-definitional.

Under the surviving reading the substrate's contribution here is the **dissolution**, not a
dark-energy prediction: the off-equilibrium residual is named as an open magnitude with no derived
epoch law, and no claim is made that it accounts for the observed ≈ 69 % of the energy budget.
Value-gated; full treatment and the exclusion arithmetic in §E.1.1 (canonical falsifier §E.3 VG-2).

The hook here is the **dissolution at equilibrium**. The standard Λ catastrophe is not just
suppressed — it is *removed at the equilibrium identity level*, by many-body physics that the
substrate exactly satisfies. (*Import notice:* Volovik's identity is an equilibrium theorem
applied at the substrate level — registered as **I-4 in companion Section 13**, status
NAMED-CRACK: the substrate is driven, and the deviation from the equilibrium premise is
precisely the off-equilibrium residual, whose magnitude stays gated. The crack is therefore
NAMED, not cashed: it buys a residual with no derived epoch law — the `ρ_vac ∝ H(t)²` reading
is excluded (N54, §E.1.1) — so it underwrites no dark-energy prediction.) What remains is the off-equilibrium residual, named openly. This is
the kind of move the framework makes elsewhere — turn a fine-tuning problem into a structural
identity plus a named open residual.

---

## §B.8 — The macroscopic limit

The last hook of Part B. Bodies — planets, stars, the N-body problem — read in TWT as defect
features of one wavefront. The L/Q split that sorts micromatter species (lepton vs baryon) is the
same algebraic split that sorts macroscale conserved invariants (angular momentum vs spent
integrals). One algebraic structure, two manifestations.

At macroscopic separations the internal microscale structure — the L-orbit and Q-orbit defects
that make up each body — is irrelevant to the others: each body presents only its centre of mass,
its mass, and its far field. This is the **standard effective-particle reduction**. Going
macroscopic does not open new dynamical doors; it removes the substrate detail behind which a door
might have hidden.

What the substrate contributes at this scale is therefore **ontological, not dynamical**. It gives
a physical referent for each device of the classical celestial-mechanics bookkeeping — the global
clock is the wavefront's monotonic `e_4`-advance (§B.7.1), the global frame is the wavefront
hypersurface itself (§B.7), a worldline `R_a` is a defect cluster's trace on that front (§A.3),
the connective invariants are the scalar energy and the L-orbit bivector `L` (§B.8.2), and the
far-field force is the induced Newtonian potential of §B.6.1 — and it identifies which structural
objects of the `Cl(4,0)` algebra carry the conserved quantities. Those are clean results. Nothing
dynamical is added here: the far-field law belongs to §B.6, the substrate's own dissipative
dynamics to §D.5, and neither is altered by coarse-graining to bodies.
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
time-mixed ones; **Metric status of the barycentric shift.** The shift `T_{V_cm} : r ↦ r − V_cm · t` used above is
a *Galilean shear* (affine), not a rotor conjugation in `Cl(4,0)`. Because `(e_{i4})² = −1`
(engine: `e_i4_squares_to_minus_one`), a rotor `exp(½ θ e_{i4})` in an `(e_i, e_4)` plane is
*circular* — `cos(θ/2) + e_{i4} sin(θ/2)` — so no boost-like element lives in those planes. The
restriction is to those planes, not to `Cl(4,0)` as a whole: genuine Lorentz boosts are hosted
through the γ-embedding as the mixed-parity element `B_ζ = exp(ζ e_j/2)` with `e_j² = +1`
(§B.2.2, R-132), which is precisely not a `Cl(4,0)` rotor. The shear costs the present argument
nothing: `L`, `I`, and the collision structure of §B.8.3 are intrinsic to the bivector and
untouched by it. The reduction is a choice of adapted coordinates, not a rotation of the frame.

### B.8.2 The L/Q split, micromatter and macroscale

The conserved bivector `L` lands in the **L-orbit** — the same algebraic space that hosts leptons
(§C.1) — and the spent integrals `(P, R_cm)` live in the orthogonal **Q-orbit** that hosts baryons
(§C.1). The decomposition is orthogonal under the bivector inner product.

> **One algebraic split, two manifestations — a definitional observation, not an independent
> coincidence.** (R-049)

At microscale the split sorts matter content: leptons in `𝓛`, baryons in `𝓠`. At macroscale the
same split sorts conserved invariants: angular momentum in `𝓛`, spent integrals in `𝓠`. The
identification is not metaphor; it is the same `Cl(4,0)` bivector inner-product split, doing two
jobs at two scales.

**Triviality caveat.** "Not metaphor" is true but weak, and nothing stronger should be read into
it. The L/Q split *is* the `e_4`-content partition of the six
bivectors, and both sortings compared here are graded by that same distinguished `e_4`: the
macroscopic invariant is purely spatial by construction (barycentric coordinates annihilate the
`e_4`-mixed blades, §B.8.1) and the lepton orbit *is* the purely spatial triple. So the two sortings
agree because both reduce to the one question "does this blade involve `e_4`?" — a **definitional
observation**, not an independent structural coincidence, and not an over-determination. The claim
becomes substantive only if the macroscopic conserved invariant can be shown to land in the lepton
orbit for a reason *beyond* sharing that partition; no such argument is constructed here, and
nothing downstream should lean on this as an over-determination.

### B.8.3 Sundman's collision condition

Let `I = Σ_a m_a · |s_a|²` (polar moment of inertia), `T = (1/2) Σ_a m_a · |w_a|²` (kinetic
energy). Cauchy–Schwarz applied to the bivector norm gives

> `|L|² = |Σ_a m_a · s_a ∧ w_a|² ≤ (Σ_a m_a · |s_a| · |w_a|)² ≤ (Σ_a m_a |s_a|²) · (Σ_a m_a |w_a|²) = 2 I T`.

As `I → 0` with `T = E − U` and `U → −∞`, kinetic and potential energies diverge in magnitude at
the same rate: `T ~ |U| ~ 1/r`. The bound then forces `|L|² ≲ 2 I T ~ r → 0`. Since `|L|` is
conserved along the flow, `L = 0`: **triple collision forbidden unless `L = 0`** (R-050).
Worldlines can fall onto their common `e_4` axis only when they are not circulating about it.

The chain depends on §B.6.1's Newtonian far-field `U ~ 1/r`; Cauchy–Schwarz on the bivector norm is
generic. The Sundman condition follows.

### B.8.4 The atlas is a projection artifact

Here is the closing hook of Part B. The N-body problem in classical mechanics carries an *atlas
with seams* — local coordinate patches that fail at close approach, where the standard variables
diverge, and the system is known not to admit new integrals: no new *algebraic* ones (Bruns 1887)
and no new *uniform* ones analytic in the perturbation parameter (Poincaré 1890/1892). These are two
distinct theorems with different hypotheses, customarily cited together; "the Poincaré–Bruns
theorem" is not a standard named result and is not used as one here.
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
when one extracts individual `R_a(t)` as separate computational objects — and what that
re-extraction hits is **individuation failure**, not non-integrability.

*This correction matters and reverses an earlier claim.* Previous revisions said the re-extraction
"is what hits Poincaré–Bruns non-integrability." That is wrong, for a reason visible in this
section's own formula. Bruns (1887) and Poincaré (1890/1892) are statements about the global
structure of the dynamical system — no new algebraic integrals, no new uniform integrals analytic
in the perturbation parameter — manifesting as homoclinic tangles and sensitive dependence.
Rewriting a chaotic finite-dimensional system as a smooth infinite-dimensional PDE does not make it
integrable, and `R_a(t) = (1/B_a) ∫_{V_a} x b(x,t) d³x` is a *smooth functional of a smooth field*,
so the projection cannot manufacture non-integrability either. The chaos is in the dynamics and
survives the change of representation.

What the projection genuinely cannot do is **individuate**. `V_a` is defined as "a spatial region
enclosing only the `a`-th cluster", and when two clusters merge no such region exists — the
projection is undefined, not divergent. That is the honest content of R-050a: the seam is in the
field → feature map, and it is a failure of *labelling*, not of *evolution*.

Close approach is, at the field level, a smooth localized superposition of two
topological-density features; it only *looks* like a near-collision after one has chosen to read
the field as a set of bodies. The substrate has no near-collision problem because the substrate is
not a set of bodies — it is one wavefront with `N` localized features in it.

*Import notice (companion Section 13, row I-21).* The literature precedent for this reading is
Atiyah–Hitchin's moduli-space treatment of slowly-moving solitons (1985/1988), whose `90°` monopole
scattering is the canonical case of a soliton *collision* that is smooth at field level and singular
only in the particle description. It is cited as precedent and carries **no load** here: the argument
above is self-contained — `R_a` is a smooth functional of a smooth field — and the import's own premise
(BPS or near-BPS solitons, so that relative positions are flat directions) fails on this substrate,
whose defects sit roughly `23 %` (`B = 1`) and `21 %` (`B = 2`) above the Bogomolny–Faddeev bound on
the banked energy coefficients of §C.1.2 (R-133, R-135). That failure is also why the moduli route to
a multi-defect state space is a recorded negative (N53), not a resource.

*What the substrate does not provide: elimination of the classical difficulty.* A mechanism that
generates the patched atlas and a mechanism that eliminates it are different mechanisms; only the
first is available here. At Newtonian order the far-field force between coarse-grained bodies is
the potential `−G M_1 M_2 / R` of §B.6.1 (R-038), with `G ~ 1/(N_eff Λ²)` from the Sakharov
induction (§B.6.2) — the substrate delivers the very problem Bruns and Poincaré are theorems
about, so the verdict stated at the head of this section applies to TWT's macroscopic limit
directly rather than by analogy. That verdict is about the *dynamics*, and the Eulerian rewriting
does not touch it: the field picture relocates the *ontological* seam — what a body is, and where
individuation fails — not the computational difficulty of integrating the Lagrangian description,
whose local expansions keep their finite radius of convergence set by the nearest singularity in
complex time. **A better picture of a patch is still a patch.** This is not a gap in the
framework; it is a property of the macroscopic regime, where there is no substrate detail left in
which an escape from non-integrability could hide.

*The driven-dissipative attractor edge, and why it does not help here.* Bruns and Poincaré are
theorems about *conservative Hamiltonian* dynamics, and the substrate beneath is
driven-dissipative (§D.5) — formally a different object, whose long-time behaviour is organized by
attractors rather than by energy minimisation. Dissipative systems are generically *more* chaotic,
but they can also collapse many initial conditions onto a low-dimensional attractor, and a
macroscopic dynamics that fell onto one would admit a closed *reduced description* — a finite
effective system valid on the attractor — without admitting a closed *form*. Three things keep
this a motivation rather than a result. (i) It is unbuilt: it requires the substrate's dissipation
equations and their timescale separation written explicitly, which is the §D.5 fork, the
framework's #1 gap. (ii) It would not repair the seam this section is about. Individuation failure
is *kinematic* — a property of the projection formula, whose `V_a` must enclose exactly one
cluster — so an attractor in the dynamics could at most change how often clusters merge; it could
not make the field → feature map well defined where two features have merged. (iii) It does not
reach the macroscopic force law at the precision at which the framework claims its Newtonian
limit: force-law measurements on the front return `−G M_1 M_2 / R` (§B.6.1), and the substrate's
dissipation surfaces instead in the value-gated channels — the `Im χ` budget and macromolecule
decoherence, `Λ ~ H²`, `1/T_2`, the dark sector (§E.3 VG-1 … VG-4) — and, as a genuine
inside-frame exposure, in the dimension-six Lorentz-violation coefficient of §E.3 VG-6, not as a
deviation from Newton here. The measurement that would decide the question is the *two-body* far
field: a departure from conservative Newton/Kepler at PPN precision would test §B.6's induction
derivation before it touched anything in this section.

(*Honest scope.* The multi-defect `Cl(4,1)` wave equation with `N` back-reacting topological sources
is not constructed in this paper; its construction is a structural target. What we claim here is
the **ontology** — bodies are defect-features of one wavefront — and the **reframing** that
follows from it. The dynamics-coherent version of the reframing depends on the
multi-defect well-posedness named as canonical structural-coherence falsifier §E.3 SC-1.)

### Closing of Part B

This closes Part B's "emergent classical physics" arc. From `Cl(4,0)` + `e_4` propagation + the
matter-as-defect ontology, we have recovered: Lorentzian signature, special relativity, quantum
mechanics (with the phase-sector restriction of §B.3.1 assumed, not derived), Bell at the Tsirelson
bound (with the tensor-product state space assumed, not constructed), electromagnetism with no
monopoles (given the winding-as-source identification), the fine-structure
constant as a reactive grade-0 invariant with its sibling g, induced gravity with sign + form +
magnitude bracket, the cosmic arrow of time, and the macroscopic limit — where what the substrate adds is *ontological, not dynamical*: a
substrate referent for the classical bookkeeping, the L/Q split doing a second job at a second
scale, and a reframing that locates the N-body *individuation* seam in the field → feature
projection. The classical dynamics itself, chaos included, is unchanged. None of these are postulates of the framework: each is a consequence of the premises
listed in the Opening — in places through the registered imports the body labels at their
use-sites (companion Section 13).

Part C now develops the Standard-Model structural skeleton — charges, three generations, the
gauge group. The reader who wants only the picture can stop here. The reader who wants the
engineering continues.

---

# Part C — Matter, charges, generations, the gauge group

*The Standard Model's structural skeleton, derived from the substrate. The tier mix begins to
diversify here: charge discreteness and the Weinberg ratio are tight algebraic identities — the
first from topology, the second a trace taken over the charge table §C.2 assigns; the
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

and comparing this elastic value with measured baryon masses crosses the `m = E₀` premise of
§A.4 (elastic cost ↔ rest frequency — the counted identification, not a derived step). The
comparison here is additionally a **calibration**: `f_π` and `e` were historically fitted to the
N/Δ masses, so it exercises the premise without independently testing it.

**This whole sector is instance-level.** Four pinned choices of the first candidate meet here and
none of them is an axiom (§A.6.4): the semiclassical soliton-quantization toolbox this section
runs on (node V3-10), the fitted cell scale `f_π` (V3-3), the stabilizer value `e` (V3-5), and —
one level up — the arrangement whose bond couplings the dressed relation `e ≈ √18/(D/J)` reaches
back to (V3-1, V3-2). What survives at family level here is the ontology — matter as defect, which
is an axiom — together with the topological reading and the stabilization class, both of which are
**preferred directions rather than family property**: the family endorses the volume-twist class,
it does not hold it, and the compass space and the dynamical-stabilization alternative stay open
(§A.3, §A.6.3). What the family holds in no sense at all is a baryon mass, and it would not
inherit one from a re-anchored candidate.

with `f_π ≈ 129 MeV` the cell-scale mass — the ANW **fitted** value, per the Opening's input list,
not the measured decay constant — and `e ≈ 5.45` the **empirical** (ANW) Skyrme
stabilizer. The dressed-coupling relation `e ≈ √18 / (D/J)` (§D.4) *reproduces* this value at
the ~1% level from the lepton-calibrated `D/J ≈ 0.787` (predicted `e ≈ 5.37–5.39`; the `√18`
identification is itself flagged as possibly coincidence-riding, §C.3.11). Quoting `≈ 5.45` as
the *output* of the relation would be circular — the
baryon-side `D/J ≈ 0.778` of §C.3.11 is itself *defined* by back-solving `√18/e` at the
empirical `e = 5.45`. The ~1.1% cross-sector spread between the two calibrations is the honest
content of the cross-sector **agreement** (§C.3.11, which states what each leg measures). The numerical coefficient
`36.47` is the exact hedgehog-BVP eigenvalue (R-051); ANW publish it to three figures as
`M = 36.5 F_π/e`. With the displayed
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
rides the Finkelstein–Rubinstein fermionic *selection* (§B.3.5; an external import, companion
Section 13 row I-20 — compatible, not forced;
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
an imported topology theorem, companion Section 13 rows I-5 and I-20) give, on the `K₃ = 0` tower,
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

**The refit branch (R-138).** The refit of
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
physics is literature-known (Skyrme; Jackson–Jackson–Pasquier 1985; Manton–Sutcliffe **§9.2–§9.3**,
where Eq. (9.23) and the sentence following it give the massless asymptotic Skyrmion as a triplet of
orthogonal pion dipoles and Eqs. (9.26)–(9.31) compute the dipole-dipole interaction and identify the
perpendicular-rotation attractive channel — *verified against the source*; the Skyrme and
Jackson–Jackson–Pasquier citations remain pending). One scope note, which makes the result
**less** import-dependent rather than more: Manton–Sutcliffe carry the **massless** dipole triplet
only — their sole massive-tail statement (§9.9, Eq. 9.147) does not solve the linearized massive
profile equation — so the massive dipole-Yukawa tail `(1+μr)e^{−μr}/r²` used here is TWT's own
identity, not an import. What R-139 adds is the in-framework
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

The substrate's rotor field takes values in the 4D-orientation class — the six-parameter local
state space of §D.3.2 — and `π_3` of that class is `ℤ × ℤ` (R-002); the count is the same whether
the class is written as `Spin(4)` or as `SO(4)`, since a double cover is an isomorphism on `π_n`
for `n ≥ 2`. Writing it as `Spin(4)` below is a convenience of notation, not a commitment. The
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

*Would-change-if — a located alternative strategy, recorded not adopted.* The `(n_𝓛, n_𝓠)` basis
above comes from the exact sequence, and reading a *general* `Spin(4)`-valued configuration in that
basis requires a *choice* of splitting of `0 → ℤ → ℤ × ℤ → ℤ → 0`. Such a splitting always exists —
the quotient `ℤ` is free, so the sequence splits — but it is not canonical, and the framework has
never said which one it uses; a general configuration’s `n_𝓛` depends on that choice. One
available move sidesteps it: define the two integers as **per-sector degrees into a fixed
target** — `L = deg(S³ → S³_𝓛)` for a subgroup-valued map and `B = deg(S³ → S³_𝓠)` for a
coset-valued one — each a single degree, with no splitting entering either definition. That is
**not** an answer to the objection, and it is recorded here as a handle rather than a repair: it
presupposes exactly what would have to be justified, since one must already know which target a
configuration maps into before either degree is defined. What it locates is the shape of the escape —
**the choice disappears if the sector assignment is DERIVED** from the defect’s own construction
rather than assumed. At that point the per-sector degree formulation is available immediately, and
the exact sequence is needed only to relate the two sectors, not to define either one.

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
a process from any lower-`B` configuration. The empirical lower bound
`τ/B(p → e⁺π⁰) > 2.4 × 10³⁴` years at 90% CL
(Super-K) is structurally consistent.

### C.1.6 The electron as Hopf defect; QCP scaling

The electron is the L-orbit lepton-sector defect — a Hopf-like soliton with Hopf invariant
`H = 1`, equivalent to a winding into `π_3(SU(2)_L)` via the Hopf fibration. Its existence as a
stable defect does not follow from the choice of target manifold. Derrick's theorem analyses the
static minimum of an energy functional under spatial rescaling, and its counting is blind to what
the field maps into: in `d = 3` a two-derivative term scales as `λ¹` and a quartic as `λ⁻¹`, so a
*static* L-orbit defect needs the Skyrme quartic exactly as the baryon does — which is what §C.1.1
already says. (*Which* quartic is not fixed anywhere in this framework — the `SU(2)`-valued Skyrme
term for an `S³` field, or the Faddeev `F²` term for an `S²` director, or neither; the
consequences for the coefficient are set out in **the functional note** below.) What differs for the
electron is the register, not the target: by §A.4 mass is the meta-time rotor frequency, so the
rest electron is an oscillator at `ω_0 = m_e c²/ℏ` with no static limit (R-007). The stability
functional for an internally rotating defect at conserved charge is then the fixed-charge one the
framework already banks at R-142, `V_eff(λ) = E_static(λ) + N²/(2Θ(λ))` (banked there on the `B = 1`
background; the scaling structure is the same), whose second term supplies a rescaling contribution
a purely static energy does not have. Stated at its true strength: this **removes the no-go, it
does not by itself exhibit a stabiliser** — Derrick's scaling test is a necessary condition, not a
sufficient one — and R-142's own `E_static = E_2 λ + E_4/λ` keeps the quartic in place. In the
drive-zero register of §A.3 the §C.1.1 quartic is what holds the size; the driven-attractor
functional that would replace it lives at the §D.5 gap.

The L-orbit **stiffness** scale comes out of QCP (quantum critical point) scaling near the
chirality balance `D = J`. At leading order

> `f_L = f_π · (1 − D/J)^{9/2}`  (R-055).

At the empirical `D/J ≈ 0.79` this gives `f_L ≈ 0.115 MeV`.

**What this section delivers, and what it does not.** `f_L` is a stiffness, not a mass. Converting
a stiffness into a mass requires an L-sector coupling, and **the framework has no *derived* one**:
no substrate argument fixes an L-sector coupling, no engine primitive computes one, and this
section states no conversion. Borrowing the baryon sector's `e` would not repair this — it would be
a further uncounted cross-sector import, and §C.3.6 shows it could not work in any case, since the
lepton parametrization makes `m_e` vanish as `(1 − D/J)²` near the chirality balance while `f_L`
carries the exponent `9/2`; **no constant bridges two different exponents.** **The electron mass is
therefore not derived here.** What is derived — conditionally,
on the ingredients set out below — is how the L-orbit stiffness scales with the distance from the
chirality balance, and that is the whole of the section's quantitative content. No accuracy figure
for `m_e` is quoted anywhere in it, because none would be a prediction: any residual would be
reporting the coupling that was chosen to produce it.

The obstruction sits upstream of the coupling, and naming it is what says how the gap would be
closed. **Which functional stabilises the L-orbit defect is open, so within the static-functional
class no dimensionless coefficient is fixed for the L-sector.** Write the candidate models in one normalisation,
`E = c₂ ∫ Σ_i |∂_i n|² + c₄ ∫ Σ_{i<j} |∂_i n ∧ ∂_j n|²`. The dimensionless minimum
`Ẽ = E/√(c₂c₄)` is model-intrinsic, and the coefficient in any `M = coeff · f/e` formula is `Ẽ/4`.
For the `SU(2)`-valued Skyrme case `c₂ = f_π²/8` and `c₄ = 1/(2e²)`, so `√(c₂c₄) = f_π/(4e)`, and
substituting the hedgehog reproduces §C.1.2's radial density term for term; solving that BVP at
`c₂ = c₄ = 1` gives `Ẽ = 145.85 = 4 × 36.46` (Derrick virial `E₄/E₂ = 1.0001`). That coefficient
is the **baryon** sector's, and it belongs to that functional and to no other. The framework's own
artifacts say the L-orbit functional is a different question: `ring_core.py` records that the
L-orbit defect "is not literally Faddeev-stabilized — the true profile is genuinely open", while
the simulator's GF-5 identifies the stabiliser as a fixed-charge `S¹` meta-time winding
(`E(μ) = aμ + b/μ³`) that is not a quartic at all. Three branches, three answers. If the defect is
the `S³`-valued degree-1 Skyrmion that `π_3(SU(2)_L)` literally names, the Skyrme coefficient is
the one that would apply — borrowed from the baryon sector, and uncounted if used. If it is the `S²`-director Hopf soliton — the object this section's title suggests
and `ring_core.py` records as toroidal — the governing functional is Faddeev–Skyrme and the Skyrme
coefficient is not merely inapplicable but **excluded**: the rigorous Vakulenko–Kapitanski bound
reads `Ẽ ≥ 32π²√2 · (3/16)^{3/8} · |H|^{3/4} = 238.4 · |H|^{3/4}` in these units, a coefficient
floor of `59.6`, strictly above `36.46`; the literature `H = 1` minimum (`E₁ = 1.236` in units of
`32π²√2`, Foster arXiv:1012.2595, massless) sits at `Ẽ = 552.1`, coefficient `138.0`. If it is
GF-5's fixed-charge balance, neither static coefficient applies. Sublinearity underlines that
these are genuinely different physics rather than a choice of units — Skyrme energies grow
linearly in `B` while Faddeev energies are bounded below by `∝ |H|^{3/4}`, so numerical agreement
at one charge could not identify the functional in any case. **Within this static-functional class,
settling the functional is the prerequisite for an L-sector coefficient, and a coefficient is a
prerequisite for a mass** — and by §C.3.6's exponent, not a sufficient one.

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
choice. An alternative value `ν = 3π/2 = 4.712` is carried as an L2 candidate, but it has neither
a mechanism nor a live empirical target: extracting an exponent from the electron mass would
require exactly the stiffness-to-mass conversion this framework does not have, and the exponent so
extracted moves with the choice of coupling. There is no accuracy figure attached to it.
The L-orbit electron is one of the framework's mixed-tier results: structural ontology derived,
the stiffness scaling derived at leading order (conditional on the `K_c` ingredient), and **no
route from that stiffness to the electron mass** — so the section's output stops at `f_L`, and
`ν = 3π/2` remains an unmotivated candidate value rather than a measured one.

**The rest-frame extent.** The electron-at-rest is the L-orbit defect oscillating at meta-time
frequency `ω_0` while carrying its winding (`H = 1`, equivalently `π_3 = 1` and `π_1 = 1`). The
spatial extent of the vortex worldsheet is the wavelength of that oscillation,

> `ℓ_e ~ c/ω_0 = ℏc/(m_e c²) = λ̄_C`  (R-055),

the reduced Compton wavelength. (`ℓ_e` here is the defect's extent, *not* the classical electron
radius `r_e = α · λ̄_C` of §B.5b; the engine's `electron_two_windings` docstring writes this
quantity `r_e`.) Two scope notes. It is **not a quantum-mechanical uncertainty-principle radius**
— the framework does not take the uncertainty principle as primitive, it is emergent from the
rotor structure of §B.3 — so no QM postulate is imported here. And it is **not an independent
size determination**: `ω_0` is read off the *measured* electron mass, so `ℓ_e = λ̄_C` restates that
measurement in the framework's register rather than predicting it. Since the section derives no
`m_e`, it derives no `ℓ_e` either. The identification is dimensional — a consistency statement,
not a measurement of the size.

**The moving case.** At rest the defect's phase varies in meta-time only: a pure `ω_0` oscillation
with no spatial phase gradient — the configuration is *rolled up* in the sense that its whole clock
sits on one axis. Under the finite boost of §B.2 that clock-phase tilts into space, and what an
inside-frame observer reads off the very same defect is a travelling phase pattern: the de Broglie
wave, the same defect with its phase unrolled. Its content is the §B.2 mass-shell orbit and nothing
beyond it — with `(E, p) = m(cosh ζ, sinh ζ)` and `E² − p² = m²` exact, the phase relation is
`ω² = c²k² + ω_0²`, and `v_phase · v_group = c²` follows identically. Both are consequences of that
banked boost machinery and inherit its conditioning unchanged: the algebra is exact inside
`Cl(4,0)`, and it acts through the timelike placement §B.2.1's reduction also rides, so this is a
**reading of the mass shell in the register of a defect's own phase, not a second derivation of the
dispersion relation** — the same caution R-132 carries against over-reading its own consistency
check. **The winding survives all of it.** A boost deforms the profile and tilts the clock; it
cannot move a configuration between homotopy classes, so there is no boost at which the defect
dissolves into a non-defect wave — `π₃` forbids it. "The electron becomes a wave" is therefore the
wrong picture of what a moving electron is: the phase unrolls, the topology does not.

**And the unrolling is about phase, not about size — the two axes must not be merged.** A
travelling electron is phase-unrolled while its amplitude core stays compact at `λ̄_C`, exactly as
the rest-frame paragraph above has it; the boost changes the phase structure and not the envelope.
The spreading of a *bound* electron over `a_0` is the other axis entirely — the resonant-cavity face
of the field ontology of §B.3, an envelope statement about confinement rather than a phase statement
about motion. Running the two together is how a compact travelling shape gets carried into an
orbital where it does not belong.

---

## §C.2 — Charges and the first generation

The framework's cleanest spine result lives here, and it is two things.

**Charge is quantized because winding number is an integer.** `π₃(S³) = ℤ` gives a discrete charge
lattice and protects it against drift: there is no continuous parameter available by which a proton
and an electron could come to differ. **And hydrogen neutrality is an identity in the normalization
constant** — `Q_p + Q_e = 0` holds for *every* value of `c`, so nothing was tuned to make the two
cancel, which is what turns the `< 10⁻²¹` neutrality measurement into a test of the framework rather
than the datum that calibrates it (R-063, R-159). The Standard Model postulates both: its
hypercharge assignments are chosen — anomaly-constrained, but chosen — and within the gauge group
alone nothing forbids a proton and an electron whose charges fail to cancel. (A grand-unified
embedding or a Dirac monopole would supply it; the point is that the Standard Model as such does
not, and that this framework gets it from topology without a unifying group.)

The condition, stated here once: the **spectrum of charge values** — which state carries `+2/3` and
which `−1/3` — is an *assignment*, not a computation. It rides four named structural premises
(P4–P7, §C.2.7), the entered anchor `(Q_p, Q_n) = (1, 0)`, and the weak assignment of §C.4.2. The
winding chain supplies integer-valuedness and protection; the charge functional supplies the
normalization. Everything that follows — hypercharge, the fractional quark charges, weak isospin,
V−A, GMN — is computed from the Clifford spectrum *given* that assignment, and the engine marks the
boundary between the two sides explicitly (`charge_sector_provenance`; the right-handed singlet
values below are GMN-consistent assignments, fixed by the blade spectrum plus the charge chain
rather than independently derived — see the normalization note at the end of §C.2.1).

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
this is canonical falsifier §E.3 row 11.

### C.2.3 Weak isospin from the meta-time rotor doublet

A massive defect's meta-time rotor `q_h(τ_5) = exp(m τ_5 û/2)` (§A.4; `m = ω`) splits into two
half-amplitude components — `sin(ω τ_5/2)` and `cos(ω τ_5/2)` — the pair the weak sector reads
as the isospin doublet (R-058 — FRAMING, given the §C.4.2 weak assignment: under
rotations of the rotor axis the pair transforms as `1 ⊕ 3`, scalar plus vector, NOT as a
doublet; the doublet reading requires *left* multiplication on `ℍ ≅ ℂ²`, a different action,
posited rather than derived).
*(An honest-scope note: with R-127's lock, a rotation of the rotor axis within
the L-orbit span is generated by the spin su(2) and reads as precession — the standing
don't-conflate hazard. Which su(2) performs the doublet rotation here — the weak SD factor vs
the spin L-orbit factor — is left unspecified by this passage and needs an explicit
identification; the cos/sin doublet components themselves are unaffected.)* The
charged-current vertex `W^+: cos → sin (e^− → ν_e)` and `W^−: sin → cos` is read off the
posited doublet structure; the `T₃` slot assignment is likewise posited in-engine (P7, §C.2.7).

### C.2.4 Lepton-quark weak universality

The weak couplings to lepton and quark sectors are identical because both sectors carry the
same meta-time rotor doublet structure (R-059). The proof is algebraic: both lepton and quark
blades transform under the same `SU(2)` action on the `S_+` chiral half of the spinor module.
This is a theorem, not a coincidence requiring tuning.

### C.2.5 V−A from SD's half-module kernel

Weak isospin is the chiral Spin(4) factor SD = `su(2)_+` (R-079, established at §C.4). On the
4-component spinor module SD has a **half-module kernel**: it acts non-trivially on exactly one
Weyl chirality, trivially on the other. So a `W` boson can only couple to one chirality (R-060) —
the **V−A** structure. Given the §C.4.2 assignment, V−A is derived, not stipulated.

### C.2.6 Generation-blindness and no tree-level FCNC

SD is the unique centralizer of the ASD generation triple. Acting on a generation-eigenstate
basis, SD treats all three generations identically: the weak vertex carries no off-diagonal
generation matrix element (R-061). This is the **no tree-level FCNC** result. It is also a
consequence of the §C.4.2 weak assignment, and is canonical falsifier §E.3 row 15.

### C.2.7 GMN as algebraic identity (non-circular by construction)

The Gell-Mann–Nishijima relation

> `Q = T_3 + c · Y`  (R-062)

is a derived algebraic identity in the substrate, **with `c = 1/2` returned non-circularly**. The
non-circularity matters: a derivation that defines `Y := 2(Q − T_3)` would make `Q = T_3 + Y/2`
a tautology. The relation's three ingredients are independently determined:

- **Q** is fixed independently of GMN — but *not* by an independent computation of its values,
  and the distinction is load-bearing. What the **topological-winding
  chain** (§C.5.1 / R-054 / §C.1.5) supplies is integer-valuedness alone: `π_3(SU(2))` gives
  `B ∈ ℤ`, hence a discrete charge *lattice* and its drift protection — no unit, no sign, no
  per-state value. Carried honestly with an unknown unit `q_0` and unknown integer windings
  `w_p, w_n`, the three-facet composition returns `Q_u = q_0(2w_p − w_n)/3` and
  `Q_d = q_0(2w_n − w_p)/3`: three free parameters, nothing determined. (The engine computes no
  winding here: the primitive is `charge_assignment_from_anchor` — the anchor `Q_p, Q_n = 1, 0`
  plus that composition solve — and it is named for what it does. `winding_charge` survives only
  as a legacy alias so that earlier citations resolve. The anchor is a parameter of the function
  rather than a frozen literal, which makes the counterfactual runnable: requiring one universal
  `c` across both orbits, as (P4) does, forces `Q_p − Q_n = 1` exactly and leaves the absolute
  anchor free, so the entered `Q_p = 1` buys the normalization `c = 1/2` and nothing more. Delete
  the `/3` of §C.2.2 and the only anchor admitting one universal `c` is `(+1/2, −1/2)` — so that
  `/3` is what makes an integer nucleon anchor compatible with (P4) at all.) The specific anchor
  `Q_p = +1`,
  `Q_n = 0` still need not be imported: given two structural premises — **(P4)** measured electric
  charge is the eigenvalue of *one* universal linear generator `Q = T_3 + c·Y` across all
  sectors, and **(P5)** `Q` is chirality-independent per defect — the proton–electron relation
  follows for *every* `c` (R-159, below), so the neutrality-of-atoms datum this anchor used to
  consume is **conditionally replaced** rather than imported. Either way it enters no GMN step, so
  the `c = 1/2` check below stays non-circular — the point of this bullet. What it does *not*
  establish is a second, topological determination of the fifteen charge *values* racing GMN:
  those come from the charge functional and its single normalization `c`. **The winding supplies
  protection; the functional structure supplies normalization.**
- **T_3** is fixed independently by the **meta-time rotor doublet** (R-058 / §C.2.3): the
  rotor's `SU(2)_+` generator with eigenvalues `±1/2` on each doublet member.
- **Y** is fixed independently by the **`e_4`-bilinear** (R-056 / §C.2.1).

With `T_3` and `Y` independently determined, the relation `Q = T_3 + c · Y` must hold for some
`c` on every blade. **The lepton doublet converts one normalization datum into `c`** — gate-free,
with no quark content and no facet structure: `(ν_L: Q = 0, T_3 = +1/2; e_L: Q = −1,
T_3 = −1/2)` with `Y_L = −1` from the e_4-bilinear gives `Q = T_3 − 1/2 = T_3 + (1/2)·Y` on both
members, so `c = 1/2`. Stated honestly, that step is a *conversion*, not a
manufacture. The datum doing the work is `Q(ν_L) = 0`, and the `e_4`-bilinear cannot itself supply
it: the bilinear returns the hypercharge `Y`, not `Q`, and it is a **per-blade** map, while `ν_L`
and `e_L` share the single lepton blade `e_{123}` — so it returns `−1` for both members alike and
cannot split the doublet. The provenance of `Q(ν_L) = 0` is therefore the native `S_−` route or
the anomaly conditions catalogued at the end of this section — or, failing both, the empirical
neutrality datum — never the doublet arithmetic itself. The remaining 13 Weyl states of the first
generation then return `c = 1/2` consistently — non-trivially for the left-handed quark doublet
(whose `Q` comes from the facet composition and whose `Y` from the blade bilinear),
definitionally for the right-handed singlets (whose `Y` normalization is fixed at `T_3 = 0`,
§C.2.1). This consistency, with `c` pinned by the lepton doublet alone, is **the derived
content** — the relation `Q = T_3 + Y/2` is not a definition; on the doublet sector it is a
non-trivial Clifford identity returning the same coefficient on every blade.

**The proton–electron relation needs no anchor at all (R-159).** The determination above runs
from independently-fixed charges to `c`. Running it the other way is stronger. Take the
functional *form* `Q = T_3 + c·Y` as structural (P4) with `c` left free, take `Q`
chirality-independent per defect (P5), identify the proton with the three-facet composite
`uud` (P6 — an inside-frame state identification, the canon-legitimate use of the inside view),
and posit the **cross-sector weak-isospin alignment** `T_3(e) = T_3(d) = −T_3(u)` (P7 —
INPUT/posited: the charged lepton occupies the slot opposite
the doubly-represented quark. Flipping the lepton slot alone gives `Q_p + Q_e = +1`, the quark
slots alone `−1`; only the global flip is a convention. Nothing in §C.2.3 derives which member
of the doublet the electron is, and the engine posits the `T_3` table in-code).
Then

> `Q_p + Q_e = [2T_3(u) + T_3(d) + T_3(e)] + c·[3Y_Q + Y_lep] = 0 + c·0 = 0`

**identically in `c`.** Both brackets vanish separately, and each is already derived: the `T_3`
bracket because `uud + e` is one complete quark doublet plus an up-versus-down-opposed pair
(R-058, given the weak assignment of §C.4.2); the hypercharge bracket because `3Y_Q + Y_lep = 0` is
exactly the `3 × 1/3 = 1` arithmetic of §C.5.4 — the `e_4`-bilinear's sign opposition between
the orbits (R-056) combined with the trivector triple-product `/3` (R-057). The same
computation returns `Q_n + Q_ν = 0` identically, and singles `uud` out uniquely: of the four
three-facet composites only `uud` lands at `−Q_e` (`uuu`, `udd`, `ddd` give `+1`, `−1`, `−2`
relative to the electron), which also dissolves the apparent circularity in §C.3.13's
side-assignment. The result is substrate-specific rather than generic — delete the `/3` and the
residue is `2c ≠ 0` in this document's hypercharge normalization, the one in which
`Y_lep / Y_Q = −3`; in the conventional normalization with `Y_Q = 1/3` the same residue reads
`−2c/3`. The number is normalization-dependent and the *point* is not: it is nonzero for every
value of the free constant.

So **hydrogen neutrality is a theorem of the framework given (P4, P5, P6, P7)**, not a datum it
consumes, and the `10⁻²¹` measurement changes role from calibrating the anchor to *testing*
those premises. Honest scope: P4, P5 and P7 are structural premises, not closed Clifford
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
structural premises (P4, P5, P6, P7)** of §C.2.7, holding identically in the normalization constant
`c` (R-159). The neutrality-of-atoms anchor is thereby **conditionally replaced (P4–P7), not
retired**: P7 — the weak-isospin alignment — is exactly the bit the
Standard Model fixes *by* the charges, so the anchor is relocated into a named posited premise
rather than dissolved. **Charge quantization is the framework's cleanest spine result**, and it is
worth being exact about which part of it is carried end to end: the **discreteness**, by exact
algebra from `π₃(S³) = ℤ`, and the **neutrality identity**, which holds for every `c` and so
consumes no empirical anchor. What is *not* carried end to end is the assignment of values across
the spectrum — that rides P4–P7 and the entered anchor, and the engine separates the two sides
explicitly (`charge_sector_provenance`). Read against §B.1, whose signature result is
posit-plus-implication rather than a derivation of the signature, this is the sharper of *those two*
comparisons: the conserved discrete charge spectrum falls out of the substrate algebra, while the
signature is a posited placement whose observed form the algebra then forces. It is not the only
Standard-Model fact this framework obtains from structure rather than postulate — the generation
count, the monopole absence, the `B − L` triad and the weak-host closure are others, each with its
own stated conditions — and the conditioning class matters more here than the ranking does.

---

## §C.3 — Three generations, Koide, neutrinos

This section carries the framework's mixed-tier content. The structural derivations (three-count
with its count generic-given-4D (Frobenius as remark, §C.3.8), Koide form `K = 2/3 ⇔ c = √2`, Foot 45° characterization, forced-left-handed
neutrino, single-Weyl lightness) are clean. The lepton-mass-ratio values currently sit at FIT
tier rather than forward-derived — the cross-sector `D/J` agreement is a real coherence signal
between two different functionals (§C.3.11), not a forward derivation. The Result Index (companion Section 1) keeps the
distinction crisp.

### C.3.1 The Z_3 of V_4-perp; the Brannen amplitude form

The generation circle lives on a Z_3-symmetric reduction of the meta-time rotor's phase space.
The three generations are identified with the three imaginary units of `ℍ` on the `V_4⊥`
generation circle. Here `V_4 := span{e_{14}, e_{24}, e_{34}}` is the Q-orbit `𝓠` (§A.5.2),
orthonormal under that section's bivector inner product `⟨X, Y⟩ = ⟨X Ỹ⟩_0`; the
substrate-distinguished diagonal in `V_4` is

> `d = (e_{14} + e_{24} + e_{34})/√3`,  with `⟨d, d⟩ = 1` and `⟨d, e_{i4}⟩ = 1/√3`,

and `V_4⊥` is the 2-plane inside `V_4` orthogonal to `d` (the superscript `⊥` is relative to `d`,
not to `V_4` itself), with orthonormal basis

> `t_1 = (e_{14} − e_{24})/√2`,  `t_2 = (e_{14} + e_{24} − 2 e_{34})/√6`.

The three `e_{i4}` project onto `V_4⊥` as a triangle with exact 120° spacing — `Z_3`-symmetric
about `d`; any other orthonormal basis of the 2-plane differs by a rotation and only moves the
zero of the phase. (The three `ℍ` units the generations are identified with are those of the
**anti-self-dual triple** — the ASD summand of `Cl⁺(4,0)`, §D.2.4 / R-098 — not the quaternion
subalgebra of §A.5.6; that identification is the conditional structural step recorded in the
Result Index.) Projecting
the meta-time circle onto `V_4⊥` gives the Brannen amplitude form

> `A_k(c, δ) = 1 + c · cos(δ − 2πk/3)`  (R-064)

for `k ∈ {0, 1, 2}`, with `δ` the Brannen phase (the `δ_L` of §C.3.5) and `c` the
projection-geometry coefficient. The form follows from the
projection geometry; the `c` value remains an input.

**Attribution.** "Brannen amplitude" and "Brannen phase" are this text's internal labels, not a
priority claim. The cyclic-permutation-invariant (`Z_3` circulant) parametrization is **Koide's**
(arXiv:hep-ph/0005137, 2000); Brannen's 2006 note independently re-notices the charged-lepton case
and pins the modulation amplitude at `√2` and the phase numerically, reaching the refereed
literature through Koide's own 2007 paper. What this framework takes from Brannen is the numerical
pinning; the form is Koide's, and the form *by itself* carries no content — three parameters fit
any three-particle spectrum, so the empirical claim lives in the amplitude *value* alone
(the parameter-counting statement is §C.3.10's, following Żenczykowski).

### C.3.2 The √2 factor

The projection geometry of the 3D Euclidean meta-time circle onto a 2D `V_4⊥` slice carries a
natural normalization

> `c = √2`  (R-065),

the value the metric ratio of the projection would assign — with `V_4⊥` as defined in §C.3.1,
`|e_{i4}^⊥| = √(2/3)` and `⟨e_{i4}, d⟩ = 1/√3`, so that ratio is `√(2/3) / (1/√3) = √2` exactly.
The *ratio* is exact; that `c` **equals** it is the part that is not forced. This is **equivalent to the INPUT
`K = 2/3`** of §C.3.3 (Brannen–Koide equivalence theorem): the `√2` is what the geometric reading
of the lepton sector commits to *if* `K = 2/3` is the framework's empirical input — and given
the empirical input, the geometry returns the matching `√2`. The √2 is therefore not an
*independent* derived constant — it is the same INPUT bit as `K = 2/3`, seen through the
projection's geometric lens. (Six independent forcing routes for `K = 2/3` have all been
investigated and returned negative — companion, R-065/R-066 rows; the equivalence theorem
propagates that result to `c = √2` and to the
`Σ T_3·Y = 0` cross-term value, neither of which is independently forced.)

The Brannen amplitude is therefore `A_k = 1 + √2 · cos(...)`.

*Level.* `c = √2` — equivalently `K = 2/3` — is a **preferred direction** of the family, not an
axiom and not a pick of this instance alone (§A.6.3). What is family-structural in this sector is
the `ℤ_3` triplet organization and the *type* of hierarchy it produces; the value is endorsed as
highly plausible and remains unforced, which is exactly what the six negative forcing routes
record. A candidate that organizes the lepton triple with a different phase coefficient is still a
member of the family.

### C.3.3 Koide K = 2/3 ⇔ c = √2 — the Brannen-Koide equivalence

The Koide mass identity

> `K := (m_e + m_μ + m_τ) / (√m_e + √m_μ + √m_τ)² = 2/3`

is empirically exact to 10⁻⁵ — **at one specific mass definition**, which the corpus has until now
left unstated. The three numbers the framework feeds in (engine `M_E, M_MU, M_TAU`) are the PDG
**physical / on-shell (pole)** charged-lepton masses `0.51099895`, `105.6583755`, `1776.93` MeV, so
`K = 2/3` is a statement at that **one mass definition**, not a definition-independent identity. The
precise word is *definition*, not *scale*: a pole mass is a resonance position and is itself
renormalization-scale-independent, so the inputs are unambiguous once "pole" is chosen. What moves
`K` is switching to a **running** definition.

Why a redefinition can move it at all: `K` is exactly invariant under a common rescaling
`m_i → λ m_i`, so only the *flavour-differential* part of a definition change can shift it — and the
pole → `MS-bar` conversion supplies precisely that, through its per-flavour `ln m_i`. Using the
one-loop QED conversion `m̄_i(μ) = m_i [1 − (α/4π)(4 + 3 ln(μ²/m_i²))]`, computed for this passage
(**own computation — a one-loop estimate, not an engine primitive, not banked, and not to
be cited as engine-verified**), `K` moves from `0.6666645` to `≈ 0.6678 – 0.6679`: from a relative
deviation of `−3.3 × 10⁻⁶` to `+1.8 × 10⁻³`. The estimate is stable across the choices one could
argue about — `+(1.72 – 1.89) × 10⁻³` over `μ ∈ {m_μ, m_τ, M_Z}` and `α ∈ {1/137.0, 1/128.0}`, i.e.
**520 – 571× the pole-point deviation** — and it is essentially `μ`-independent at fixed `α`, because
the `μ`-dependent term `+3 ln μ²` is *common* to all three flavours and a common factor cancels in a
ratio, while the flavour-differential term `−3 ln m_i²` carries no `μ`. So this is a one-off
*matching* shift, not a gradual running away from `2/3`: at a running definition it is simply a
different relation.

The honest reading, then: the `10⁻⁵` headline belongs to the pole point, two and a half orders of it
are a property of the mass definition, and the framework has nowhere said which mass definition its
`ω` is (§C.3.3a). Nothing here rescues or refutes `K = 2/3`; it scopes it. With that scope stated,
the Brannen-Koide equivalence theorem (R-066) states

> `K = 2/3 ⇔ c = √2` for the Brannen amplitude.

So K = 2/3 has a geometric reading: it is the empirical signature of the √2 projection geometry.
The value `K = 2/3` itself is INPUT (exact-but-unforced, §C.3.2) — and INPUT *at a
named mass definition*. What the framework derives
is the *form* `K = 2/3` carries
— the equivalence with c = √2 and the Foot 45° characterization that follows.

### C.3.3a At which mass definition? — the `ω` ↔ renormalized-mass identification is not fixed (OPEN)

The framework's mass ontology is `mass = the meta-time rotor frequency ω` (§A.4). That is a
substrate-level, **grain-layer** statement. `K = 2/3` is a relation among the **inside-frame measured,
physical (on-shell / pole)** charged-lepton masses. **Nowhere in the corpus is the bridge between the
two fixed:** there is no passage, and no engine primitive, that says which mass `ω` is supposed to
equal — the pole mass, an `MS-bar` mass at some scale, or a substrate-scale quantity that descends to
one of these under a running the framework has not computed.

One leg of that bridge is now stated as a premise: `m = E₀` (§A.4) identifies `ω` with the
defect's classical elastic cost — the tree-level, substrate-scale member of the menu above. That
NAMES the classical branch; it does not answer this section's question, because the premise picks
no scheme — which renormalized mass the pole-point relation rides remains open, now sharpened: a
scheme label is owed wherever an `E₀`-derived number meets scheme-dependent data (the third face
of the missing renormalization dictionary, §E.2.1).

**Two things this objection is not.** It is not the claim that pole masses are the wrong masses: a
pole is a resonance position, and for an ontology in which mass *is* a rotor frequency the pole is
the natural default identification. Nor is it an ambiguity in the inputs: the pole mass is itself
renormalization-scale-independent. What is open is narrower, and real:

1. the identification is **unstated and unargued** — the corpus has never written "`ω` = the pole
   mass", so the choice has never been defended, and it has never been counted; and
2. a *derivation* from the substrate would naturally deliver a quantity at the substrate scale, and
   nothing in the framework says it descends to the pole point rather than to a running mass at some
   high scale — which is precisely Sumino's concern (below).

So

> *why does the relation hold at* that *mass definition?*

is an **OPEN QUESTION, not a derived feature** of the construction. It is the canon §0 two-scales
problem — Planckian grain layer versus emergent hadronic cell — landing squarely on the framework's
most quantitatively impressive result, and it is recorded here rather than left unstated.

**Downstream inheritance — sized, not merely asserted.** All figures below come from the same
one-loop pole → `MS-bar` estimate of §C.3.3 (own computation, **not banked**):

- **Foot 45° (§C.3.4):** `45.000° → ≈ 45.05°`. Inherits `K`'s shift exactly, since `K = 1/(3cos²θ)`.
- **The fitted `δ_L` (§C.3.5):** `12.73° → ≈ 12.67°`.
- **The lepton-sector determination of `D/J`:** `0.787 → 0.781`. **This does not weaken R-074's
  cross-sector agreement — it tightens it.** The baryon-sector leg (`0.778`, from the Skyrme
  stabilizer) uses no lepton mass and does not move, so the lepton↔baryon agreement goes from `1.08%`
  to `0.34 – 0.40%`. Recorded because the direction is favourable and must not be quietly dropped.
- **The `μ² ↔ m_N/3` convergence (R-134) is the most exposed item**, for a structural reason worth
  stating: `K`, `θ`, `δ_L` and `D/J` are all **scale-invariant** in the masses, so a common rescaling
  cancels and only the flavour-differential part reaches them — which is why they are essentially
  `μ`-independent. But `μ² = ((Σ√m)/3)²` is an **absolute** scale, so it feels the common part too,
  and *that* part is `μ`-dependent. Its `0.28%` agreement becomes `+0.8%` at `μ = m_μ`, `−0.2%` at
  `μ = m_τ`, and `−1.6%` at `μ = M_Z`. So R-134 is definition- **and** scale-dependent where the
  ratio-type results are only definition-dependent.

**The contrast the framework can draw honestly is with `sin²θ_W`.** There, §C.4.5 *does* have a
descent account: the tree value `3/8` is run down with real beta functions, and the honest result is
that the descent **fails** — it lands near `0.15` against a measured `0.2312`, the failure is written
into the paper, and four standard escape routes were computed and closed (negatives ledger N55) —
descent and closures alike inside the imported elementary-field RGE frame (`I-6`), whose failure
would gate that reading rather than refute it. For
Koide the framework has **no descent account at all** — not even a failing one. That asymmetry is the
point: `sin²θ_W`'s scale dependence was faced and cost the framework a headline; Koide's mass-definition
dependence was never raised. Until an `ω` ↔ renormalized-mass identification is derived, the
`10⁻⁵`-level agreement must be read as agreement **at the pole point**, with the coincidence
unexplained.

Prior art on precisely this objection is Sumino's: the QED radiative correction spoils Koide's
relation, and the standard response is to cancel it with `U(3)` family gauge bosons at `10²–10³` TeV
(Sumino 2009a, 2009b; followed up by Koide 2017 — companion Section 10, all three citations verified
against INSPIRE-HEP). TWT has **no family gauge sector** and does not adopt that mechanism; the only
obvious native handle would be the substrate's own `Z_3` structure supplying a flavour-differential
cancellation, and nothing in the corpus computes it.

**Labelling this gap does not fix the objection.** It converts an unlabelled blind spot into a named
open item (negatives ledger N57; companion Section 4 registry row, `Gated on absolute ω scale`). The
exposure runs in both directions: a derived descent could land on a definition in which `K ≠ 2/3`.

### C.3.4 Foot 45° signature-free characterization

Equivalently, K = 2/3 is the condition that the Foot angle `θ(m_e, m_μ, m_τ) = 45°`. The Foot
angle is the angle between the vector `(√m_e, √m_μ, √m_τ)` and the diagonal `(1, 1, 1)` in ℝ³,
given by

> `cos θ = (√m_e + √m_μ + √m_τ) / √(3 · (m_e + m_μ + m_τ))`  (Foot 1994; R-067).

Plugging in the measured charged-lepton masses gives `θ = 45.000° ± 0.001°` — strikingly exact, and
(per §C.3.3) strikingly exact **at the pole point**. `θ` inherits `K`'s mass-definition specificity
exactly, since `K = 1/(3 cos²θ)` is a bijection: under the one-loop QED pole → `MS-bar` conversion of
§C.3.3 the angle moves to `≈ 45.05°` (`45.049° – 45.054°` across the same `μ` and `α` range), i.e.
around **50× outside** the `±0.001°` band just quoted. So `45.000°` is a statement about PDG physical
(pole) masses, not a definition-independent one.
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

### C.3.6 The B = A ⇔ δ_L = π/12 ⇔ m_e = 0 identity

The identity is a statement about the two **amplitudes** of the chiral `ℤ_3` potential of
§C.3.7, and it is exact there: when the parity-odd amplitude equals the parity-even one,

> `B = A ⇔ δ_L = π/12 = 15° ⇔ m_e = 0` at leading order  (R-069),

since `tan 3δ_L = B/A` and `√m_e` vanishes linearly in `δ_L − π/12` in the fitted Brannen form.
Equal amplitudes are the balance point; the lightest lepton is massless there.

**The `D = J` form is a corollary, not the theorem.** Reading `B = A` as `D = J` requires the
coefficient identification `A = J`, `B = D` — §C.3.7's asserted ansatz, at the dressed-coupling
level. Given that ansatz, `D = J` is the balance point and the empirical `D/J ≈ 0.79` sits at
79% of it; without it, what the lepton fit measures is the amplitude ratio `B/A` and nothing
finer. So the narrative that "the substrate's chirality nearly balances, and the electron is
light because of how near" is **conditional on the ansatz** — it is the ansatz, not the
identity, that converts an amplitude ratio into a statement about the bond couplings. What is
unconditional is the structure: the hierarchy `m_e ≪ m_μ < m_τ` is generated by proximity to a
balance point of the two amplitudes, and that proximity is what the one-parameter fit measures.

§C.1.6 expands a *different* quantity
about this same parameter point — the L-orbit stiffness `f_L` — and the two vanishings are **not
known to correspond**: in the fitted Brannen form above `√m_e` vanishes linearly in `δ_L − π/12`,
so `m_e ∝ (1 − D/J)²` near the balance, while §C.1.6's stiffness carries the exponent `9/2`.
Two vanishings at one point, with different exponents and **no passage relating them** — which is
exactly why §C.1.6 delivers no mass. Both exponents are read off inside the *same* banked
parametrization, so the amplitude restatement above does not touch that comparison.

### C.3.7 δ_L from the chiral Z_3 potential

The form of `δ_L(D/J)` follows from a chiral Z_3 potential built from `J` (kinetic) and `D`
(chirality-breaking) couplings on the substrate (R-070). The *form* is DERIVED; the coefficient
identification `A = J, B = D` (which fixes the absolute calibration) is an asserted ansatz at
the dressed-coupling level, not a substrate forward derivation. Honest scope flagged in the
result row.

**Two amplitudes, however many channels.** Given the potential's two premises — one angle with
`ℤ_3` periodicity, truncated to the lowest `ℤ_3` harmonic — the admissible potentials span the
two-dimensional space `{cos 3ψ, sin 3ψ}`, and that dimension is a fact about functions on a
circle, not about the Hamiltonian. Additional bond channels (§D.3.3's `Γ` directions, a
spatial-bond `D`) therefore cannot create a third amplitude; they **repopulate** the two that
exist, `A = J + Σᵢ αᵢΓᵢ` on the parity-even side and `B = D + β·D_spatial` on the parity-odd
side. So the *form* `δ_L = ⅓·arctan(B/A)` is robust to the truncation pick, and what the pick
buys is the *identification* `B/A = D/J` — which holds exactly when every entry coefficient
`αᵢ`, `β` vanishes. Whether a static computation reaches those coefficients turns on the
defect's twist class. Restrict the twist to a single plane angle — or to two equal ones — and
the bond-bilinear harmonic ceiling sits below the third harmonic, so every `ℤ_3` harmonic of the
substrate's own orientation potential vanishes identically, `J`'s included, and the ratio that
would decide them is `0/0`. The two-rate twist this candidate adopts (§A.4) is not so
restricted, and a bond-bilinear determination of the `αᵢ` and `β` is open, owed and unbuilt
(§D.5.7). Their **dressed** values remain kernel-level, so any claim that `Γ` does or does not
enter `A` at dressed level is a claim about that kernel.

### C.3.8 Three generations from Frobenius

Why exactly three generations? The generation circle is identified with the three imaginary
units of `ℍ` on `V_4⊥`. **The count's operative theorem is sharper than this section's
title suggests:** what forbids a fourth generation is
`dim Λ²₋(ℝ⁴) = 3` — four-dimensional space carries exactly three anti-self-dual planes, a
dimension count now *computed* in the engine (the trace of the `(1 − I₄·)/2` projector on
grade-2) rather than asserted over a hand-written list (R-071). Frobenius's theorem (ℝ, ℂ, ℍ the only
finite-dimensional associative real division algebras) enters as a structural remark, and only
through an **associativity premise** the framework must own: drop associativity and the
octonions offer seven imaginary units — cf. Furey's division-algebraic programme, which builds
one generation's *representation content* from exactly the non-associative factor (arXiv
1611.09182; *Eur. Phys. J. C* **78** (2018) 375; Furey & Hughes, *Phys. Lett. B* **827** (2022)
136959; developed independently of TWT, related conclusions by different means). The
no-fourth-generation prediction is therefore a structural forbiddance — **generic-given-4D**
(canon §5 class), not a tuning of mass scales. Canonical falsifier §E.3 row 13.

The result is LOCATED-conditional: the orbit-phase → ℍ-unit identification is a structural
mapping that is asserted rather than derived from substrate dynamics. So "exactly three" is a
generic-given-4D count **given** the identification and the associativity restriction named
above; those conditionals are the residual gap, flagged in the result's companion row.

*Level.* The dimension count is family property — it is a fact about four-dimensional space and
consumes no pick. The two conditionals are not: reading the three anti-self-dual planes as
**generation seats**, with associativity, is a **preferred direction** (§A.6.3), and the octonion
route is the named family alternative rather than an outside objection. So the family makes
exactly three seats *available* by its own geometry; which seat nature occupies, and why, is not
derived at either level.

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
`|V_us|² ≈ 0.0503` at ~0.6% (§E.3 row 14).

**Attribution — this relation is not ours.** `sin θ_C ≃ √(m_d/m_s)` is the **Gatto–Sartori–Tonin
relation** (Gatto, Sartori & Tonin, *Phys. Lett. B* **28**, 128 (1968)), one of the two classic
fermion mass-ratio predictions alongside Koide's, with a fifty-eight-year literature behind it.
It is credited here rather than presented as a TWT candidate identification. What is *possibly*
TWT's own is not the
relation but the **reading** offered below — that the ratio arises as a frequency ratio between
mass eigenvalues on a generalized Brannen ellipse. The numerical agreement is GST's, not evidence
for the substrate.

The reading is the
quark sector's Brannen-with-epicycle reading: the deviation from the lepton-sector circular
projection is encoded as an eccentricity `ε ≠ 0` on a generalized Brannen ellipse — a
parametrization-dependent encoding (see below) — and the
Cabibbo angle reads as the frequency ratio between the two leading mass eigenvalues. The
relation is structurally testable for `|V_us|² = m_d/m_s` (the d–s ratio); the analogous
prediction for `m_t` is structurally untestable because no top hadrons exist (R-091a; §C.5). The
identification stands as a CANDIDATE pending the Θ_rel closure.

The up-sector eccentricity itself carries a candidate rule inherited from the quark-sector
epicycle parametrization: `ε_u/ε_d = 2^{3/2} ≈ 2.828`, heuristically motivated as the spinor
half-angle structure times the up-vs-down chirality flip. The `ε` values are parameters of the
two-harmonic epicycle parametrization, not orbit observables: at three sample points the second
harmonic aliases into the first, so `ε` is defined only jointly with the parametrization's phase
*and amplitude* conventions (the corpus's variants differ in both the phase reference of the
second harmonic and its amplitude coefficient), which the three masses do not fix — the
reparametrization-invariant content of a mass triple is a single resultant amplitude and phase;
parameter values inter-convert between variants only under a re-fit, never by carrying the same
`(b, ε)` across forms. The invariant content of the down triple is the resultant amplitude
`A_d ≈ 1.546`, against the lepton triple's `√2` — equivalently, the down-sector Koide value
`K ≈ 0.73` differs from the leptons' `2/3`: the quark/lepton asymmetry lives in the invariant
amplitude, not in any single parametrization's `ε`. For the lepton triple the second harmonic
vanishes (`ε = 0`), the aliasing degeneracy is absent, and the resultant phase *is* `δ_L` — so
the `δ_L` of §C.3.5 remains an observable of the three lepton masses. The ratio rule is
accordingly a statement
about the fitted parametrization. In that parametrization `ε_u` is *set
by* the rule (`ε_u = ε_d · 2^{3/2} = 0.973` from the fitted `ε_d = 0.344`), so the ratio
realizes the rule by construction rather than testing it; and the rule is untestable on the
framework's own terms: only `u, c` are hadron-indicated, and `m_t` is a Standard-Model
bookkeeping number (no top hadrons, §C.5.9), so it cannot be falsified against the top. It
stands as a counted fit recorded in the companion registry, not a numbered result; §A.4's
forward reference resolves here.

### C.3.11 Cross-sector `D/J` — what the two legs actually measure

The lepton sector calibrates `D/J ≈ 0.787` via Brannen `δ_L = 12.73°`. Independently, the baryon
sector reads `D/J = √18 / e ≈ 0.778` from the Skyrme stabilizer with the ANW-historical
`e ≈ 5.45` (matching the ANW fitted `f_π = 129 MeV`) (R-074). The two values agree to ~1.1%
**at the pole mass definition; §C.3.3a sizes the inheritance, and the direction is favourable —
under the one-loop pole→MS-bar estimate the lepton leg moves toward the unmoved baryon leg. That
estimate is not banked, so the quoted figure stays 1.1%.**

**What that agreement is, at earned strength (R-180, R-181).** Each leg measures a **ratio of
totals** — a parity-odd bond amplitude over a parity-even one — and not a single-parameter
measurement of `J` and `D`. By the exact channel→parity selection rule the numerator
`B = D_{e₄} + β·D_spatial` is exactly `Γ`-clean and the denominator `A = J + Σᵢ αᵢΓᵢ` is exactly
`D`-clean, with nothing else able to enter either (R-176, R-177); the admixture **sizes** are
uncomputed, and the bond-bilinear route to them — closed by a harmonic ceiling while the defect's
twist is restricted to one plane angle — is open under the two-rate rotor this candidate adopts
(§A.4, §D.5.7), with dressed values still kernel-level (§D.5). Decisively, the two legs' parity-**even** totals belong to **different functionals**
— the `ℤ₃` generation amplitude and the helix pitch — and are the same substrate number **only if
the symmetric-traceless (`Γ`) bond admixture vanishes** (R-181, JD-6(b)). Indeed
`e ≈ √18/(D/J) = cot q`, so the baryon leg **is** the pitch functional. The agreement is therefore
evidence that **two different readings of the chirality cohere**; it is **not** a second reading of
one pinned parameter and **not** an independent over-determination. Nothing is fitted between the
two legs — but the `Γ` admixture is not nothing: R-181's route sizes the implied difference of
denominators at `Δ(Γ/J) ≈ +2.15%` of `J`, under a four-part conditioning class any one of whose
failures voids the number. The standing fence follows directly: **never carry a ratio calibrated on
one functional into another** — `f_π² = 8J/a` and this lepton↔baryon comparison included.

**The arc-ratio reading sharpens the same fact from the other side [CANDIDATE].** If `δ_L = 2/9`
rad exactly — Brannen's observation — then
`D/J = tan(2/3) = 0.786843` and the lepton leg fixes the ratio with no continuous freedom left in
it. The residual is quoted as an **offset**: `δ_fit − 2/9 = +2.5×10⁻⁶` rad, a fractional agreement
of `1.1×10⁻⁵` in `δ` (`1.6×10⁻⁵` in `D/J`). **No significance is quoted** — there is no null
hypothesis here, and the residual sits below the sensitivity of the inputs themselves: a 0.1%
coherent shift in `m_τ` moves `δ_L` by some fifty times the residual, and two published `m_τ`
vintages a mere 0.07 MeV apart move the residual by a factor of three, so any propagated-mass
significance would report how well `m_τ` is *measured* rather than how well the reading holds.
What can honestly be said instead is a **trials factor**: over the rational menu
`{p/q, pπ/q, p/(qπ), p/(q√2)}` with `q < 20`, at a tolerance equal to the observed residual,
`2/9` is the **only** hit, with a chance expectation of about `0.16` — the conservative figure
of the spread-uniform accounting; the measured-local-density accounting gives `0.004`, and the
conservative one is what is quoted. That bounds the
look-elsewhere *within that menu only* — and the menu was itself written down after `2/9` was
known, so it speaks to which rung, not to whether a rational-menu reading was the thing to seek.
The claim is asserted **at the pole-mass point**: `δ_L` is built from pole masses, a Koide-type
relation is not RG-stable, and no substrate argument yet fixes that point as the right one.
The `n = 3` rung `6/27` of the 2:4:6 ladder is recorded as **a noted regularity carrying no
evidential weight**: the geometry reaches the measured triple on a four-dimensional solution
manifold (R-173), so every nearby ladder value is reached as well — the ladder labels a point in a
continuum and excludes nothing, and compression is evidence only where the compressed description
is constrained.
The baryon leg then **demands** `e = √18/tan(2/3) = 5.391979` against the literature's
`e_ANW = 5.45`: a residual of 1.06% that is a statement about **one constant** rather than a
scatter between two fits. **As a test this is not yet discriminating.** The historical Skyrme `e`
is itself a fit whose spread across determinations exceeds the deviation, so a ~1% offset fails
nothing; the test bites only against a determination at or below the ~1% level, read from primary
sources before any promotion. And the `D/J`-level "agreement" internal to the lepton leg is a
**tautological restatement** — `D/J := tan(3δ_L)` by definition, so it is `tan(3·)` applied to both
sides of one empirical fact — never a confirmation of anything.

*(Side note on the geometric coincidence. The baryon-side back-derivation rides on
`e ≈ √18/(D/J)`, where the √18 itself rides a geometric coincidence whose physical referent the
framework itself disclaims. The cross-sector agreement is
honest; the chain has one acknowledged geometric coincidence at the relating link.)*

**A second cross-sector convergence, recorded as a candidate (R-134).** The Brannen lepton scale
`μ = (√m_e + √m_μ + √m_τ)/3` satisfies `μ² = 313.85 MeV` against the nucleon's per-rotor share
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
one fewer counted dial. Until then: a recorded candidate convergence row, with the
post-hoc/look-elsewhere caveat carried — and carried with a number rather than a gesture.
The pairing was noticed in the literature, not predicted here, so the relevant question is how
many comparisons the menu affords: over the four canonical cell-scale comparators
(`f_π`, `1/Θ₀`, `M₀/3`, `m_N/3`) times all reduced rationals `p/q ≤ 8`, a 172-combination menu,
exactly two matches land inside 0.5% — `m_N/3` at multiplier one, and an `8/5` that is tied to
`m_N/3` by the same fit and so is not a second convergence. Those candidates sit at roughly sixty
per natural-log unit near ratio one, so the menu by itself expects about **0.6** chance matches
against the one independent match observed — a match scored **at pole masses**: in MS-bar the
same comparison fails the 0.5% criterion (+0.80% at m_μ, −1.56% at M_Z), so the scheme label is
part of the observation (§C.3.4's N57 scope). The convergence is therefore **suggestive and not
compelling** — that verdict is now quantified rather than asserted — and the menu bounds only
*which* comparator and rational, never whether a cell-scale pairing was the thing to look for.

### C.3.12 Neutrino forced left-handed; single Weyl; lightness

The arrow runs from the substrate to the neutrino, not the other way. The `+e_4` propagation
direction (R-043) forces wave-coupled matter into a single Weyl ideal of the spinor module
unconditionally — `forced_handedness` and the lightness argument both compute without consuming
any weak-sector assignment — so it is the substrate that fixes the neutrino's handedness (R-075,
R-076). *Which* half gets the name "left" rides the same orientation convention that names the
two chiral factors (§C.4.2), which is a relabelling and not a further commitment. The
right-handed partner sits in the `S_-` mode that is wave-decoupled — sterile.

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

This is the framework's headline **normalization identity**: **`sin²θ_W = 3/8` at the scale
where the two electroweak stiffnesses coincide, with no GUT group** (R-082). The route is short —
three native ingredients plus a **premised** `g_1 = g_2` (the common-trace-form assumption and the
lattice→continuum matching premise, both named in §C.4.5) — and what it delivers is a structural
identity, **not** a prediction of the measured angle: §C.4.5's scope statement governs this whole
section.

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

### C.4.2 Weak = SD chiral Spin(4) factor — a closed menu, not a pick

The **weak isospin gauge group is the self-dual bivector algebra**

> `SD = span{e_{12} − e_{34}, e_{13} + e_{24}, e_{14} − e_{23}} = su(2)_+`  (R-079),

one of the two factors of `Spin(4) = SU(2)_+ × SU(2)_−` — the `I_4 = +1` (self-dual / chiral)
one.

**The menu is complete, and it is computed** (R-171). Ask which three-dimensional Lie subalgebras
of the substrate's grade-2 rotation algebra `so(4)` exist at all. The answer is exactly three, up
to conjugacy:

> **SD** · **ASD** · **the diagonal `so(3)` class** `{Stab(v) : v a unit vector}`, of which the
> L-orbit `𝓛 = Stab(e_4)` is one member.

This is a classification, not a survey. On an orthonormal basis of either chiral factor the
structure tensor is exactly `c·ε_{ijk}`, and total antisymmetry alone forces three facts about
that factor: it has no two-dimensional subalgebra, it is simple, and all of its automorphisms are
inner. Goursat's lemma then reduces the classification of three-dimensional subalgebras of a sum
of two such factors to a finite sweep over the possible projection and kernel dimensions, which
returns those three cases and no others. Two candidates the geometry might seem to offer are not
on the list because they are not subalgebras at all: the parity-odd Q-orbit `{e_{14}, e_{24},
e_{34}}` and every proper "handed" mixture `cos t·SD + sin t·ASD` fail to close, the mixtures
because the two factors carry *opposite* structure-constant signs.

**ASD is not a rival — it is the same assignment mirrored.** The two chiral factors are
distinguished only by the sign of `I_4`, and an orientation-reversing frame reflection exchanges
them exactly while fixing the diagonal class and flipping that sign. Counted up to the
automorphisms of `so(4)`, the menu has *two* entries, not three. A candidate that "assigns weak
isospin to ASD" is this candidate with the opposite orientation convention on `{e_1, e_2, e_3}` —
one assignment with two descriptions. Nothing in the substrate's driven bond action distinguishes
them either: the driven point group contains a reflection that exchanges the two halves, and the
allowed chirally polarised bond coupling has dimension zero (§D.2.5, §D.4). If some independent
object ever pins the substrate's orientation, this paragraph reverts and ASD becomes a real branch.

**The diagonal class is excluded by data — but not by the datum one would expect.** Every grade-2
element commutes with `I_4`, so *every* candidate on the menu preserves the two Weyl halves of the
spinor module. Restricted to the half the neutrino occupies, the L-orbit and SD span the **same**
three-dimensional algebra. A left-handed single-Weyl neutrino therefore cannot tell them apart,
and any argument that it can is mistaken. The discriminator is the *other* half: SD annihilates it
outright — that half is a weak **singlet** sector — while the diagonal class charges it exactly as
strongly as the first. Under a diagonal host the right-handed fermions would form a second weak
doublet sector at full strength. They do not: the right-handed fermions are weak-isospin singlets,
and no right-handed charged current is observed at any accessible energy. The datum is read, not
tuned, and it is reversible: an observed right-handed charged current reverses it. The framework
supplies the occupancy this argument
needs from its own structure — the charged lepton occupies *both* Weyl ideals, and that two-ideal
occupancy is its Dirac-mass channel (§C.3.12, R-076) — so the other half is not empty and the
datum bites.

**What this leaves standing, stated exactly.** With both alternatives closed, the assignment is
not a choice the framework makes; it is what the substrate leaves once the classification is
computed and one measurement is read. Two things are consumed and both are named. The first is a
**structural premise**: that weak isospin is hosted by a three-dimensional `su(2)` *inside the
substrate's own grade-2 rotation algebra at all*. That premise is not derived anywhere in this
paper; it is one of the family's **preferred directions** (§A.6.3), and a candidate that hosts weak
isospin somewhere else goes the other way on it — such a candidate is not on this menu and is
untouched by anything above. The second is the **datum**: no right-handed charged current is
observed at any accessible energy, so the right-handed fermions are read as weak-isospin singlets —
read from experiment rather than tuned, and reversible, an observed right-handed charged current
reversing it (the datum's FAMILY INPUTS register row carries that would-change-if, and no
restatement of it may be stronger than the row).
Given those two, `SD` is forced, and V−A, generation-blindness, the doublet structure and
`up = SD` follow from it (R-060, R-061, R-077) — not as a family-level derivation free of
measurement, but as consequences of a forced assignment whose two supports are on the table.

**On the accounting.** This sector's cost was formerly booked as one free input bit, "the choice
of SD". That reading does not survive the classification: SD-versus-ASD is not a bit at all, since
the two are related by a relabelling; and chiral-versus-diagonal is not a free choice either,
since it is settled by measurement rather than selected. What the sector actually costs is the
named structural premise above plus one empirical bit, and the empirical bit is one the framework
reads rather than tunes. The parameter economy is unchanged in *number* and changed in *kind*, and
the honest statement of it is the two-line one just given, not "the framework picks SD."

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

is forced by pure representation theory, and is consistent with the LEP three-jet-multiplicity
value `C_A/C_F = 2.277 ± 0.02 (stat) ± 0.05 (syst)` (DELPHI/Uvarov 2002, preliminary). **Read this as
corroboration, not as an independent test:** the extraction is colour-dipole-model-dependent, and its
alternative fit variant gives `2.093` — the variant being chosen partly by agreement with `9/4`, so
the comparison is not model-independent. The
match is **a consistency check** that the framework's elastic-response octet is `su(3)` as a
static algebra — not an independent quantitative output; the same consistency-check status that
§C.4.5 assigns `sin²θ_W = 3/8` itself (the
U(3)→SU(3) restriction and all colour dynamics remain gated, §C.5.2). A subtly
different colour algebra would have given a different Casimir ratio; the framework's algebra
gives the empirically correct one.

**Ontology preserved.** There is no fundamental spin-1 colour gauge boson in TWT (R-085). The
octet is an elastic-response algebra — 3 geometric L-rotations + a spin-2 strain quintet — not
eight gauge bosons. The colour force is identified with the dynamical coset-5 = the §D.5
defect-vacuum kernel; asymptotic-freedom `β_3 < 0` is a Layer-3 deep gate (§E.2). The static
algebra is exact; the dynamical running is open.

### C.4.5 sin²θ_W = 3/8 — the headline normalization identity

The electroweak mixing angle is

> `sin²θ_W = g_1² / (g_1² + g_2²)`,

depending on the U(1)_Y and SU(2)_L couplings only (never on the colour coupling). Three native
ingredients deliver the result:

**(i) Native charges.** Summing over one full generation in the all-left-handed convention:

> `Σ T_3² = 2`,  `Σ Q² = 16/3`,

from the per-blade hypercharge eigenvalues (R-056) plus the trivector triple-product structure
(R-057) plus the GMN identity (R-062) plus the complete 15-Weyl spectrum (§C.2.8) — **plus the
posited `T₃` doublet-membership table** (R-058: `Σ T₃² = 2` is eight doublet
states × ¼, and *which* states are doublet members is posited in-engine, not derived; the slot
*alignment* within the doublets is P7, to which the squared sum is insensitive).

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
gives all bivector planes one stiffness coefficient. `g_1 = g_2` therefore rides the same dim-4
isotropy theorem as the emergent-Lorentz protection **plus two named assumptions it does not
share**: the single common trace form for `Y` and `T_3` (below), and the lattice→continuum
matching premise of the crossing-at-the-lattice-scale reading (§B.6.2, §C.4.5). One theorem, one
job each — with the extra premises named.

Combining:

> **`sin²θ_W = Σ T_3² / Σ Q² = 2 / (16/3) = 3/8 = 0.375`**  (R-082).

No SU(5) embedding and no unifying *group*. But two qualifications belong here rather than in the
engine alone, and the second is a substantial limitation on the claim.

**What `3/8` is, and what it is not.** Under GUT normalization `g_1² = (5/3) g′²`, the statement
`sin²θ_W = 3/8` is *algebraically identical* to `g_1 = g_2`. The `Σ T_3²/Σ Q² = 2/(16/3)`
computation is that normalization written in Clifford notation; the engine's own docstring for
`weinberg_sin2` says so plainly, calling `3/8` "the SU(5)/SO(10) group-theory normalization of the
SM charge assignments" and "NOT a from-substrate prediction of the observed angle." That wording is
the accurate one and governs here. What TWT avoids is importing the *Lie group*; what it still
assumes is a **single common trace form for `Y` and `T_3`** — the Clifford grade-0 norm on the
spinor module — which is the same physical assumption the embedding encodes, in different clothes.
The `√(3/5)` is native to the algebra, not free of the assumption.

**Prior art at this exact claim.** The `3/8`-without-a-master-group claim has a
direct shape-precedent: Trayling (hep-th/9912231, 1999, unpublished preprint) already obtains
`g′/g = √(3/5)` — i.e. `sin²θ_W = 3/8` — "without invoking the notion of master groups", developed
further in Trayling & Baylis, *J. Phys. A* **34** (2001) 3309. The delta: that construction lives
in `Cl(7)` with an algebraic-spinor generation and four extra spacelike dimensions supplying the
Higgs isodoublet; TWT's lives in the 4D `Cl(4,0)`/D4 substrate with defect matter, `ℤ₃`-discrete
colour, and the weak chirality forced on a closed menu (§C.4.2). Developed independently; the
convergence of the *number* across such different constructions underlines that `3/8` is
normalization content, not dynamical content — consistent with this section's own scope.

**Import notice — the descent rides `I-6`.** Everything in the run-down below, and every
escape-route closure computed against it, imports the Standard Model's renormalization-group
equations (companion Section 13, row `I-6`). That import carries a premise this section must state
rather than leave in the registry: the validity of *elementary-field* renormalization-group
equations for a gauge sector this candidate holds **emergent / composite** at `Λ_L`. Near
compositeness the two-point function develops form factors and "running" is not defined, so what
rides the premise is the import's *applicability*, not merely its accuracy — the four closures
below included, since all four were computed inside the elementary-field frame. If the premise
fails, the descent-window reading below reverts from refuted-as-a-reading to **gated**: no
computable descent at all.

**The run-down does not land on the measured value.** Running `3/8` to `M_Z` does **not** give
`sin²θ_W(M_Z) ≈ 0.231` and does **not** match the empirical `0.2312`. With TWT's own spectrum (15 Weyl per generation, one Higgs, no superpartners) the
one-loop SM coefficients `b_1 = 41/10`, `b_2 = −19/6` give, using the measured `α_em(M_Z)`,

> `sin²θ_W(M_Z) = 3/8 − 0.0355 · t`,  `t ≡ ln(M_X/M_Z)/2π`,

where `M_X` is the scale at which `g_1 = g_2`. The value obtained therefore depends entirely on a
scale the framework does not predict:

| Reading of where `g_1 = g_2` holds | `M_X` | `sin²θ_W(M_Z)` |
|---|---|---|
| Three-coupling unification (minimal-SU(5)-style; TWT does **not** claim this) | `6.8 × 10¹⁴ GeV` | `0.208` |
| At the substrate cutoff — the D4-isotropy argument is a *lattice* statement, so the ruled `Λ_L = 1/a` (§B.6.2) | `[0.39, 0.73] M_Pl` | `0.154 – 0.158` |
| Whatever scale reproduces the measurement | `1.0 × 10¹³ GeV` | `0.2312` (by construction) |

The middle row is the one that matters, because the argument offered above for `g_1 = g_2` — that
both electroweak stiffnesses are set by the same dim-4 D4 elastic form — is a **lattice-scale**
statement. Taken at face value it places the crossing at `Λ`, and the descent then lands near
`0.15`, roughly **33% below** a five-digit measurement. The bottom row reproduces `0.2312` only by
choosing `M_X ≈ 10¹³ GeV`, which is neither the GUT scale nor `Λ`, and for which the framework
supplies no reason.

So the honest status of R-082 is: `3/8` is a **derived normalization statement** — the charge
assignments, expressed in Clifford grade structure, force `g_1 = g_2` *wherever* the substrate sets
both stiffnesses equal. It is **not** a prediction of the observed mixing angle, and the framework
currently has no derivation of the crossing scale that would turn it into one. This is a genuine
open exposure of the electroweak sector, of the same kind as (and independent from) the §B.6.3
dimension-six exposure, and it is recorded as such rather than as a passed test.

**And, like that one, it is an exposure of this candidate instance rather than of the family**
(§A.6). The `3/8` identity itself is family property **in the conditional sense of §A.6.3** — it
is a normalization statement about the charge assignments and consumes the arrangement nowhere,
but it does consume the weak assignment of §C.4.2, so it stands or falls with that assignment's
own two supports — a named structural premise and one measurement — rather than with an axiom. What consumes the arrangement is the
*placement* of the crossing — the middle row of the table above is a lattice-scale statement, and
both the lattice and its back-fit size are pinned choices (§A.6.4, nodes V3-1, V3-3, V3-4). A
family member without a regular arrangement inherits the identity and does not inherit the
descent. That is not a rescue: it means the miss is evidence against this instance's arrangement
and its calibrations specifically, and the family has bought nothing by not yet having a rival
placement to offer.

**The escape routes, computed rather than waved at.** A referee will reach for four
standard ways to rescue a gap of this size. All four were computed; none of them closes it. The
calculations use real two-loop SM gauge beta functions (Machacek–Vaughn in MS-bar, top Yukawa
included) with TWT's own content — and TWT's content runs *exactly* as the Standard Model's,
because the three sterile right-handed neutrinos the framework does predict (§E.1.3, R-121) are
total gauge singlets and contribute `δb_1 = δb_2 = 0`. Probe scripts are preserved at
`knowledge/candidates/probes_2026-07-29/`; **nothing here is banked to the engine**, and none of it
may be cited as engine-verified.

- **Two loops.** Integrating the two-loop RGEs and shooting on `sin²θ_W(M_Z)` so that `g_1 = g_2`
  holds at `M_X` moves a wide-bracket band from `0.14704 – 0.16374` to
  `0.14751 – 0.16418`; on the `Λ_L` band the one-loop window is `0.1539 – 0.1576` and the same
  two-loop shift applies. The shift is
  `≈ +4 × 10⁻⁴` — the right *direction*, and **0.6% of the gap**. The shift is stable: varying
  `y_t(M_Z)` by ±10% moves it by `~10⁻⁵`, dropping the top Yukawa altogether moves it by
  `1.2 × 10⁻⁵`, and `α_s(M_Z)` is negligible. The *absolute* band carries a separate `~10⁻⁴`
  systematic from the `α_em(M_Z)` input and from weak-scale two-loop matching, which is not
  included — which is why the band should not be read past the fourth decimal, and which is
  irrelevant against a gap of `0.074 – 0.077` on the ruled band (`0.067 – 0.084` at the retired
  wide bracket). Three loops would contribute of order `10⁻⁵`.
- **Thresholds.** A multiplet decoupling at `M_T` shifts the prediction by
  `Δsin²θ_W = −(5/8) α_em (δb_1 − δb_2) ln(M_X/M_T)/2π`. For GUT-style splittings —
  `|δb_1 − δb_2| ≲ 3` spread over one to two decades — this is `|Δsin²θ_W| = 0.0009 … 0.011`. The
  MS-bar ↔ DR-bar scheme conversion contributes `2.6 × 10⁻⁴`. Against a gap of `0.074 – 0.077`,
  thresholds are a percent-level effect, not a factor-of-1.5 one.
- **A scale the framework already owns.** The required crossing is `M_X = 1.09 × 10¹³ GeV` at two
  loops — `8.9 × 10⁻⁷ M_Pl`, i.e. **5.6 decades below the floor** of the ruled `Λ_L` band
  `[0.39, 0.73] M_Pl` (5.2 decades below even the retired wide bracket's floor). Every scale the
  framework currently has on its books was checked against
  it: the nearest is `Λ_L`'s own low end at `+5.6` decades, and the next is the cell scale
  `e·f_π ≈ 0.7 GeV` at `−13.2`. Nothing sits in between — the framework has a Planckian layer and
  a hadronic layer and no third one (§D.3.5). The single intermediate scale that generically lands
  near `10¹³ GeV` in the GUT literature, a Majorana seesaw scale, is here not merely absent but
  **structurally forbidden**: exact `B − L` conservation makes the neutrinos Dirac (§C.5.6, R-089).
  A blind scan of two-scale monomials does produce near-hits — 38 of 148 land within a decade — but
  they all belong to the single family `(Λ² · m)^{1/3}`, and those near-hits are bought by trading
  the retired wide bracket's factor-of-19 freedom against the choice of `m`. On the ruled band the
  `Λ`-contribution collapses from 0.85 to 0.19 decades, which only *tightens* this negative. The
  family covered 2.15 decades at the wide bracket once *both* floated, so *some* pair landed on
  `10¹³ GeV` without any pair being singled out; at the retired corner `Λ = 0.13 M_Pl`, for
  instance, `m = f_π` gave `6.9 × 10¹¹ GeV`, 1.2 decades off — on the ruled band `m = f_π` gives
  `1.4 × 10¹² GeV`, 0.9 decades off. Hitting the target exactly needs `m ≈ 58 GeV` at the ruled
  floor or `m ≈ 16 GeV` at its ceiling (`513 GeV` / `1.39 GeV` at the retired corners), and no
  banked scale supplies any of these values.
  No mechanism in the framework produces the form. It is a content-free fit, not a derived scale.
- **New states.** Closing the gap by field content requires
  `(δb_1 − δb_2) · ln(M_X/M_T) ≈ −102` for `M_X = M_Pl` (`−108` at `2.5 M_Pl`, `−87` at
  `0.13 M_Pl` — retired-bracket corners kept as the computation record; the ruled band lies
  between). The sign is the binding part: the new states must feed `SU(2)_L` **more** than
  `U(1)_Y`. Spread from `M_Z` upward that is `δb_1 − δb_2 ≈ −2.6` — about two `SU(2)` triplet Weyl
  fermions, or twenty extra lepton doublets, or forty extra Higgs doublets, all at the weak scale,
  where electroweak-charged states of that kind are collider-excluded. Raise the threshold and the
  requirement worsens: `≈ −4.9` at `10¹⁰ GeV`, `≈ −14` at `10¹⁶ GeV`. And past
  `δb_1 − δb_2 = −19/6` sourced from `SU(2)` alone, `SU(2)_L` loses asymptotic freedom — which for
  `M_X = M_Pl` happens for any threshold above `1.4 × 10⁵ GeV`. There is no comfortable corner.

Two related rescues fail for the record. The figure `0.231` is reproduced by
**MSSM** content (`b_1 = 33/5`, `b_2 = 1`) crossing at `M_X = 2.0 × 10¹⁶ GeV` — the classic
supersymmetric unification, a spectrum TWT does not have; and even those coefficients run from `Λ`
to only `0.203`. Nor does the three-coupling row rescue anything at two loops: imposing
`g_1 = g_2 = g_3` at one scale gives `0.2076` at `6.76 × 10¹⁴ GeV` at one loop and `0.2107` at
`4.16 × 10¹⁴ GeV` at two loops, still `0.021` short — and the non-supersymmetric couplings do not
in fact meet at all, their `1/α` spread bottoming out at `3.2` near `10¹⁴ GeV`.

The exposure is therefore not an artifact of working at leading order, and it is not something a
plausible threshold absorbs. What is missing is a **derivation of the crossing scale**. The one
handle the framework has is the two-scale structure of §D.3.5: the D4-isotropy argument for
`g_1 = g_2` is a *grain-layer* statement, and if the two bivector stiffnesses were instead set
equal at some emergent layer, the crossing would move. That mechanism is not built, and until it
is, R-082's `3/8` is a normalization identity and not a measurement of `θ_W`. Negatives ledger
**N55**.

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
"weak = SD" assignment (§C.4.2) — not from the plaquette** (the plaquette is chirally symmetric;
what breaks the symmetry is the matter coupling, and §C.4.2 shows the breaking is forced rather
than picked). The `Im χ`-mediated dynamics delivering the
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
"weak = SD" assignment would name a gauge group that the substrate might not actually
admit. With it, the assignment is honest.

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

The DM sector's parity-odd content is carried, if anywhere, by the pseudoscalar expectation

> `⟨I_4⟩`,

since `I_4 → −I_4` under orientation reversal. **`⟨I_4⟩ ≠ 0` is a named premise inherited from
`D ≠ 0`, not a computed result**: no primitive in either engine computes `⟨I_4⟩`, its magnitude or
its sign, and the sign of `D` is itself a convention — reversing the helical wavevector is exactly
equivalent to reversing `D`. A non-zero `⟨I_4⟩` would be the algebraic carrier of parity violation,
and it would fix a handedness **relative to the bond convention only**. It does not fix the
substrate's orientation absolutely: the reversal `x ↦ e_4 x e_4` fixes the propagation axis `+e_4`
exactly while flipping `I_4` and exchanging the two chiral factors; every banked bond term is
invariant under it; and the banked helical vacuum is exactly invariant under it, with zero
grade-four content. Nothing banked pins the orientation, and the `SD`/`ASD` label is a recorded
convention (R-086).

**Honest scope.** `⟨I_4⟩` is a *gauge singlet* — it commutes with
every bivector, so for every rotor `R`, `R I_4 R̃ = I_4` exactly. A condensate invariant under
`G` *cannot* break `G`. Therefore **⟨I_4⟩ delivers parity violation, NOT electroweak symmetry
breaking.**

**The substrate-level origin is not built, and the route named here previously is refuted in the
class in which it was stated.** Every DM bond bivector is a `Q`-orbit blade; the product of any two
`Q`-blades has grades `{0, 2}` only, so **no bilinear in the DM bond data can be proportional to
`I_4`** — and at the driven point group `Stab(+e_4)` the pseudoscalar channel has dimension zero,
so there is no orientation-odd invariant to write down at all and every allowed DM coupling is
forced exactly `50 : 50` between the two chiral sectors. `I_4` first becomes reachable at **cubic**
order, `e_14 e_24 e_34 = −I_4`, which is where §D.4.4's candidate seat `𝓛_top = µ Ψ_0 ρ_L` (R-110)
lives: that term is cubic, **not linear in `D`**, and its coefficient `µ` is gated on the substrate
dynamics (§D.5). The framework's dedicated channel result already records that the bare `I_4`
insertion vanishes identically in all grades and both sectors, and that the `ρ_L` seat is pointed
to rather than confirmed. **The conditioning class:** this non-existence is exact *within the
bilinear bond-action class on the driven group* `Stab(+e_4)`; the cubic and derivative classes are
unscanned, and extending the invariant count to them is the computation that would close the
question either way.

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

**Honest scope.** The Higgs sector at the substrate-derivation level is FRAMING: the framework derives
the symmetry-breaking *structure* (which gauge subgroup is broken to which) from the doublet
identification on the spinor ideal, but does not derive the absolute scale `v ≈ 246 GeV` or the
Higgs mass. These are #1-gap-gated absolute magnitudes (§E.2.2), comparable in tier to α_em.
The two-scale conjecture `v / f_π ≈ m_p / m_e` is a numerical near-coincidence with
no mechanism — an intriguing lead, not derived. It is also a place where the ANW *fitted* `f_π`
enters a *physical* comparison: the ratio is quoted at `129 MeV`, and it is sensitive at the
tens-of-percent level to which normalization of the decay constant is read into it — a further
reason to treat it as a lead rather than a result.

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
per-blade hypercharge eigenvalues (R-056). Itemized (engine `B_minus_L_anomaly`, rescoped): the
three gauge-trace conditions above vanish on the gauged fifteen states alone; the two
singlet-inclusive sums — `Σ(B−L)` and `Σ(B−L)³` — are each `−1` there and complete to zero
exactly with the sterile partner (R-121). With that itemization, the anomaly-free combination
is a structural identity.

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
- **Dirac neutrinos.** `B − L` is exactly conserved (the doublet-sector anomaly condition,
  §C.5.4; the singlet-inclusive sums complete to zero exactly with the sterile partner —
  R-121 doing classical completion work, engine `B_minus_L_anomaly`); a Majorana mass
  would violate `Δ(B−L) = −2`. **Forbidden.**
- **No 0νββ.** The same `B − L` exact conservation forbids the neutrinoless double-beta-decay
  signature. **Forbidden.**

Three predictions, one substrate reason. Canonical falsifiers §E.3 rows 2 + 3.

### C.5.7 β-decay as L-pair creation through I_4

The β-decay channel `n → p + e^- + ν̄_e` reads in the substrate as an L-pair creation through
the `I_4` Hodge map (R-090). The L-orbit's bivector winding source `J` is connected to the
Q-orbit's facet structure via `I_4`; the L-pair (electron + antineutrino) is created by the
algebraic mediation of `I_4` — the Hodge map itself, which this channel consumes independently of
whether any `⟨I_4⟩` condensate exists (that question is open at §C.5.3).
**One `D`, multiple manifestations** — the same `D` that fixes the Cabibbo angle, the generation
phase, and the Skyrme stabilizer also supplies the β-decay channel; parity violation is withdrawn
from this list — its candidate substrate seat is cubic with an open coefficient (§C.5.3).

### C.5.8 Stable-sector enumeration; the wave-phase ladder

Two distinct results, kept apart. **(a) The over-production
result (real, engine-cited):** the empirically stable set — photon, proton, electron, three
neutrinos, stable nuclei, antiparticles — matches the framework's enumeration of stable sectors
(`B` integer, `L` integer, massless / massive single-defect or bound-multi-defect) with no
orphans and no gaps: `topological_overproduction_test`, companion Section 8, §E.3 row RF-7. A
consistency check against the SM's inventory (which member of each sector is lightest rides
imported SM dynamics), not an independent prediction. **(b) The wave-phase stability ladder
(R-091, CANDIDATE):** the separate companion-Section-9 table ranks twenty mostly
*unstable* states by `N = m/Γ` — a lifetime index, not a defect count — spanning thirty-one-plus
orders. No engine primitive
computes that table or its claimed mass–stability correlation, so it stays CANDIDATE until a
`wave_phase_ladder` primitive exists.

### C.5.9 Top quark exclusion

The top quark facet's decay rate `Γ_t` and the baryon-circularizing timescale `Θ_0` satisfy

> `Γ_t · Θ_0 ≈ 7.2 ≫ 1`  (R-091a).

The top facet decays before the baryon's circular winding can complete. **The top has no
hadrons** — recovering the standard QCD result (Bigi–Dokshitzer–Khoze–Kühn–Zerwas 1986: the top
decays before hadronizing) within the framework's own timescale structure — a single-detection-away falsifier
(§E.3 row 12). The top mass remains a Standard-Model bookkeeping number, useful as an
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
hadronic-cell scale of the lattice's coordination structure at the grain scale.

The 25-cell Skyrmion gives the inter-nucleon force hierarchy (R-091b):

| Range | Cutoff | Mechanism |
|---|---|---|
| Hard core | `r < √2 · ℓ_S ≈ 0.397 fm` | Cell-exclusion (1+24 cell footprint) |
| Soliton core | `r ≈ 2 · ℓ_S ≈ 0.56 fm` | 25-cell body overlap |
| Pion Yukawa | `r ≈ 5.2 · ℓ_S ≈ 1.46 fm` | π Goldstone exchange |

The hard-core distance is `√2·ℓ_S ≈ 0.397 fm`, introducing no parameter beyond the counted `e` and
`f_π`. Against the customary 0.40–0.50 fm range it sits 0.8% below the near edge and 21% below the
far edge — **a range whose own width means the comparison discriminates little, and whose referent is
a feature of particular NN-potential parametrizations rather than a directly measured length. No
agreement figure is quoted, because a midpoint-referenced one would conceal that spread.**

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
constraint. Its tension — `√σ_QCD ≈ 0.44 GeV`, i.e. `σ_QCD ≈ 0.19 GeV²`, the value the high-spin
light-quark meson spectrum requires (Campbell, Michael & Rakow 1984)
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

**Three distinct objects wear the name `ℍ` in this paper; keep them apart.**

1. The **quaternion subalgebra** `ℍ = span_ℝ{1, e_{23}, e_{13}, e_{12}} = Cl⁺(3,0) = ℝ ⊕ 𝓛`,
   closed under the geometric product, with `(i, j, k) = (e_{23}, e_{13}, e_{12})` satisfying
   `i² = j² = k² = −1`, `ij = k`, `jk = i`, `ki = j`, `ijk = −1` (engine:
   `cl40_quaternion_triple`). This is the `ℍ` of the native formalism `Cl(4,0) + ℍ` (§A.5.6): the
   home of the meta-time rotor axis `û` (§A.4; R-127's axis menu is `ℍ ∪ {E}`, and R-128's
   quark-sector lock axis `±I_4 B_q` lands back inside `𝓛` because `I_4` exchanges the L- and
   Q-orbits) and of the QM complex unit `i = e_{12}` (§B.3.1).
2. The **two summands** of `Cl⁺(4,0) ≅ ℍ ⊕ ℍ` above — the SD and ASD chiral halves.
3. The **ASD summand** specifically, whose three imaginary units are the generation triple
   (§C.3.8, §D.2.4, R-098).

Object 1 is neither of the summands in 2, and is not an ideal of `Cl⁺(4,0)` at all: no nonzero
`x ∈ ℝ ⊕ 𝓛` satisfies `P_± x = x` for the central idempotents `P_± = (1 ± I_4)/2`, and
`e_{14} · e_{12} = e_{24}` leaves the span. What *is* true is that `P_±` are central in
`Cl⁺(4,0)`, so each of `x ↦ P_± x` is an injective algebra map carrying `ℝ ⊕ 𝓛` onto a full
4-dimensional summand:

> `2 P_+ (1, e_{23}, e_{13}, e_{12}) = (1 + I_4,  e_{23} − e_{14},  e_{13} + e_{24},  e_{12} − e_{34})` (SD),
> `2 P_− (1, e_{23}, e_{13}, e_{12}) = (1 − I_4,  e_{23} + e_{14},  e_{13} − e_{24},  e_{12} + e_{34})` (ASD),

spanning §D.2.4's SD and ASD triples. So object 1 sits **diagonally** in `ℍ ⊕ ℍ` — one isomorphic
copy inside each summand, with `x = P_+ x + P_− x`. That is exactly why `e_{12}` is contained in
neither factor (§A.5.6).

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

If a construction requires `e_5` as a **spatial** degree of freedom — a new winding direction or a
soliton coordinate — then the construction is **not grounded**. It is an escape from the
framework's ontology, not physics. Being the *timelike* direction along which the 5D master
equation advances is **not** on that forbidden list — that is the third bullet above, and it is
what the engine's `Cl41Wave` signature `(+, +, +, +, −)` encodes. The fix for a genuinely
ungrounded construction is to rebuild it in `Cl(4,0) + ℍ`,
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
`V_4⊥` generation circle — the structural home of the three-generation count (generic-given-4D; Frobenius as remark via associativity, §C.3.8)
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
physical roles. Conflating grades is the easiest place for errors to creep
into the framework (cf. §A.5.2, §D.2.4).

---

## §D.3 — The D4 grain layer

The substrate beneath the wave.

### D.3.1 The D4 lattice

The D4 lattice is the densest 4D **lattice** packing (Korkine–Zolotareff 1877). Whether it is
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
It is the premise `A-1b` of the Opening — and, at the architecture level, the **first pick of the
first candidate instance** (§A.6.4, node V3-1), not a commitment of the family. The family holds
that the substrate is a material medium and endorses its being grainy; it does not hold that the
grains are *regularly arranged*, and it does not fix their size. The menu this pick came from is
open and populated: other regular lattices; an irregular-discrete arrangement, which is the
causal-set-adjacent branch and the one an external theorem constrains sharply (companion
Section 13, row I-26); and a continuum medium carrying a cell scale, which is the least explored
region of the family and costs the D4 results outright. Everything in §D.3–§D.4 that is sited on
the lattice inherits this pick, including — through the size — the dimension-six exposure of
§B.6.3.

### D.3.2 The grain as unit Clifford rotor

At each D4 site sits a **4D orientation** — a unit even element of `Cl⁺(4,0) ≅ ℍ ⊕ ℍ`, that is a
unit Clifford rotor `R_i`, carrying **six real parameters** — acting one-sidedly on the spinor
module (R-102). Six is the dimension of the grade-2 sector, `dim so(4) = C(4,2) = 6`, and the
chiral factorization of that sector into two commuting, oppositely-oriented `su(2)` triples is
what carries the two windings of §A.2 (R-002; engine: `pi3_orientation_class_two_windings`).

The one-sided action is what would make the sign `±1` part of the local state. Whether it does —
whether the `ℤ₂` lives in the state itself or enters only at the emergent covering sector, where
`π₁(Q_N) = ℤ₂` (§B.3.5) — is left open. Every winding statement the framework uses is insensitive
to the choice, because a double cover is an isomorphism on `π_n` for `n ≥ 2`, so `π₃` and `π₄`
are the same either way.

The continuum field `R(x)` inherits this target **unchanged**; it is the rotor field whose
dynamics §D.4 develops.

**Levels, at the one place they are easiest to confuse.** Three different statuses meet in this
subsection. That the local state is a **4D orientation with six real parameters**, inherited
unchanged by the continuum field, is a **family axiom** (§A.6.1, LS) — it is what carries the
generations, the weak sector, and the second winding, and two- or three-parameter readings survive
only as explicitly stated reductions to the L-orbit sector. Where the `ℤ₂` lives is a **family
branch left deliberately open**, exactly as the paragraph above says. That the medium is **grainy
at all** is a **preferred direction**, not an axiom: a continuous-medium candidate would still be
a member. And that the grains sit at **D4 sites** is the instance's arrangement pick (§D.3.1). One
further consequence of the family's refusal belongs here: the rotor **field** is a *description*
of the medium, not the ontology — the medium is material, and the field is how this paper writes
down what it does (§A.6.1).

**Note on naming.** "Grain" names the Planckian-layer atom of the substrate — elsewhere also
called the monad, the term two engine primitive names retain. When discussing cell-layer
phenomenology (hadrons, the chirality balance, the canted vacuum), "grain" is avoided in
favor of "substrate site" or "rotor", since the cell layer's constituents are not the Planckian
grains themselves but their cell-scale collective configurations. The "grain as unit Clifford
rotor" identification is a Planckian-layer statement.

### D.3.3 The two couplings J and D — calibration to leptons

Each D4 nearest-neighbour bond carries:
- a **symmetric exchange `J`** on all 24 bonds, and
- a **Dzyaloshinskii–Moriya `D`** on the 12 `e_4`-bonds only (R-103).

The DM coupling is parity-odd (the wave's chiral contribution; the substrate alone is achiral).
The ratio `D/J ≈ 0.79` is the framework's chirality calibration, INPUT to the lepton sector via
Brannen `δ_L = 12.73°` (§C.3.5, §C.3.11).

**`{J, D}` is a truncation pick, not a forced pair.** The bilinear bond couplings allowed on D4
under the driven point group `Stab(+e_4)` form a **ten-constant menu** — `J`: 2, `D`: 2, and a
symmetric-traceless channel `Γ`: 6, in the frame-bilinear reading of the site variable (the
pseudoscalar channel `χ` has allowed dimension zero there). Keeping `J` and `D` and setting the
rest to zero is a **pick**, and it is counted as one. Three consequences are stated plainly:

- **Parity does not do the excluding.** `Γ` is parity-**even**, so no parity argument reaches it;
  exactly one `Γ` direction survives the leading-order isotropy requirement, and it is dropped by
  choice. That survivor is quadratically inert on the aligned state and vanishes identically on
  the canted configurations of §D.4.3, which is why it was never visible — not why it is absent.
- **The `e_4`-only DM support is also a pick.** The two-dimensional allowed `D` space at the
  driven group is spanned by the `e_4`-bond coupling used here **and** a spatial-bond coupling of
  the same symmetry type; no point-group, chirality, or spatial-parity argument separates them,
  and every larger group kills both at once. Turning the second dial on is not a perturbation of
  the canted vacuum but a switch on it: the two couple to the *same* unique reflection-even
  chiral invariant `Σ_a k_a B_{a4}` with a fixed coefficient ratio, so a cancellation line exists
  in the `(D, D₂)` plane at which the canting — and with it the chiral symmetry breaking — goes
  away entirely. The candidate reason to exclude the spatial-bond coupling is the origin story
  already stated above (the DM coupling as the *wave's* chiral contribution, hence supported on
  the `e_4` bonds the drive singles out); that is a physical candidate routed through the open
  substrate dynamics (§D.5), not a symmetry exclusion.
- **The `cos`/`sin` parity assignment is an assertion.** That `J` (and `Γ`) feed only the
  parity-even amplitude of the chiral `ℤ_3` potential while `D` feeds only the parity-odd one —
  the step that turns §C.3.7's two-amplitude form into a `D/J` reading — is asserted, not
  measured; nothing computed here pins it (negatives ledger N62).

The pick's blast radius is bounded and named: the quadratic spine (`f_π² = 8J/a`, the pitch) does
not move under the `Γ` survivor, while the amplitude identification behind `D/J ≈ 0.79` and the
canted vacuum itself are exposed to the second `D`.

**Whose pick, and what survives if it falls.** Both of the picks named above belong to the
**first candidate instance** — the truncation itself and the `e_4`-only support of `D` (§A.6.4,
nodes V3-2 and V3-2a) — and so does the calibrated ratio that reads off them (node V3-4). None of
the three is an axiom, and the family does not hold that the medium's bonds carry exactly two
constants. What survives if any of them falls is the whole of the structural layer — charge
quantization, the `sin²θ_W = 3/8` identity, the generation count, the weak-sector assignment —
**each at the level it already carries**, not promoted to axiom by surviving this pick: the
assignment is a preferred direction and the identity and the generation count ride preferred
directions of their own (§A.6.3). What moves is the numerical spine of Parts C and D — the cell-scale relation, the pitch,
and the meaning of `D/J ≈ 0.79`, which under a non-zero discarded channel stops being a
measurement of a ratio of two couplings and becomes a measurement of a combination. That is why
the ratio is quoted throughout this paper as a calibrated input with a named referent condition,
and not as a pinned single-parameter measurement.

Cross-sector consistency: independently, the baryon Skyrme stabilizer gives `D/J ≈ 0.778`
(§C.3.11). The ~1.1% cross-sector agreement is a **hedged cross-check** (the engine's own tag):
the `√18` bridge's physical referent is disclaimed, the
massless-pion scheme was chosen partly on this very agreement, and the substrate relation
carries no scheme label (see §E.2.1's provisional-`e` entry and §C.3.11's full hedge).

A layer note, made explicit: `J`, `D`, and the spacing `a` are defined on the D4 bond
structure, but every load-bearing use in this paper consumes them as **cell-layer effective
couplings** — `f_π² = 8J/a` with the ANW fitted `f_π ≈ 129 MeV` fixes the working layer as the hadronic cell
(a Planckian-layer reading would misplace `f_π` by ~38 orders of magnitude). The grain-layer
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
- A **grain layer at the `G`-back-fit Planckian scale** (the D4 lattice, fundamental rotor medium;
  sets the cutoff `Λ` — the two-layer architecture is the structural claim; the Planckian *value* is
  measured `G` restated, three lines below).
- An **emergent hadronic cell layer** (where solitons, hadrons, and their masses live; the `f_π`
  scale at `ℓ_S ≈ 0.281 fm`).

The two scales are forced **given the framework's two anchored empirical scales** (R-105 —
DERIVED-generic-given-(`G_N`, `f_π`)): both `Λ` scales are back-fits
of measured `G` and `f_π` is a counted input, so what is genuinely forced is only that a
single-scale substrate cannot host two numbers ~20 orders apart. The two-layer *architecture*
with its open cell-formation map is adopted as the resolution, not derived. The two-scale
framework is what makes the framework internally consistent at the gravity/hadron interface.

The **cell-formation mechanism** — how the cell layer emerges from the grain layer — is open
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

### D.4.3 The canted-helix vacuum and its branch structure

*What this section is a statement about.* Everything below is downstream of the arrangement and
the bond truncation — the first candidate instance's first two picks (§A.6.4, nodes V3-1, V3-2,
V3-2a). It is the vacuum of *this* candidate, not of the family, and the chiral symmetry breaking
it supplies can be switched off entirely by turning on a second coupling the truncation discards
(§D.3.3). Read the branch analysis that follows with that scope in force.

Under combined `J + D` couplings the aligned state is unstable to canting: the DM term buys a
twist that the exchange term pays for, and the balance fixes a pitch. The configuration whose
bond energy is minimised below is a **single-`q` spatial helix**, and naming it is part of the
result:

> `k = q·e_1` — the wavevector, along a **spatial** axis — and `B = E_14` — the rotation plane.

Neither feature is presentational. The helix is spatial because **the DM energy vanishes
identically on an `e_4`-axis helix**: the drive axis supports no DM gain at all. The rotation
plane is the bond plane of the `±e_1±e_4` bonds, which is what puts the DM projection weight
`1/√2` on the four `±e_1±e_4`-class bonds and produces the `2√2`. On that configuration the
per-site bond energy is

> `E(q) = −12J cos q − 12J − 2√2·D sin q`,

minimised at `tan q = D√2/(6J)`, giving the canting angle `q ≈ 10.5°` and `cos q ≈ 0.983` at
`D/J ≈ 0.79` (R-108). The canted state breaks chiral symmetry; the breaking pattern is what the
lepton-sector Brannen amplitude form parametrizes.

**What is minimised, and what is not.** The wavevector direction `k̂` is *fixed by hand* in the
expression above rather than scanned: the four twisting bonds are named in advance and the
minimisation then runs in the single variable `q`. That is a Luttinger–Tisza **ansatz**, not a
Luttinger–Tisza **minimisation**, and the difference is load-bearing.

**Branch structure of the single-`q` family.** Scanning `k̂` over the full four-dimensional
wavevector and the rotation plane over all simple bivectors gives three facts:

- The configuration above **is** a genuine stationary point of the full `(k, B)` problem — every
  component of the gradient vanishes there at the closed-form pitch.
- It is nevertheless an **index-2 saddle for every `D/J > 0`**. The second variation transverse
  to the helix axis has the closed form
  `∂²E/∂k_2² = ∂²E/∂k_3² = 4J(cos q + 3)(cos q − 1)/cos q`, strictly negative for all
  `0 < cos q < 1`, vanishing only in the ferromagnetic limit `D → 0`.
- The lowest state **within the single-`q` simple-bivector helical family** sits on the
  **body-diagonal orbit** `k̂ ∝ (1, ±1, ±1, 0)`-class, where all twelve `e_4`-bonds twist by one
  common angle instead of the axis branch's 4 + 8 split. It lies below the axis branch by
  `ΔE = −(1/243)(D/J)⁴·J` at leading order — `1.5×10⁻³ J` per site at the calibrated ratio, which
  is `6.4×10⁻⁵` of `E(q)`'s own printed total (`3.2×10⁻⁵` of the full frame-bilinear bond total;
  the normalization travels with the figure). Both stationary points are screw states
  `B = k̂ ∧ e_4`, and the sign pattern of the diagonal is a symmetry orbit, not a distinguished
  direction.

The splitting has a closed-form mechanism. The two families are **degenerate through `O(q²)`** —
the exchange cost is isotropic and the DM gain is direction-blind at leading order — and the
degeneracy is lifted at cubic order by the DM term's own `Σ_a k_a⁴` anisotropy, minimal on the
body diagonal and maximal on a coordinate axis. The axis branch is therefore **not** a
leading-order error.

**What survives the branch question.** `D√2/(6J)` is a **leading-order invariant of the whole
helical problem**, not a property of one branch: it appears as `tan q` on the axis branch and as
the total helical rate `|k|·λ` (with `λ` the rotation plane's eigen-angle) on the body-diagonal
branch. R-108's closed form therefore stands on both, with a re-interpreted referent — while
"the canting angle `q`" names a *different geometric object* on each: four bonds at `q` on one,
twelve bonds at a smaller common angle on the other.

**Status, scope, and what is open.** Stationarity and the transverse second variation are exact
identities; the body-diagonal branch's lower energy is a numerical result carrying the
closed-form mechanism above, with an exact-arithmetic minimisation still owed; and every
minimality claim here is made **within the single-`q` simple-bivector helical family** —
multi-`q`, conical and non-simple-`B` states are unscanned. **Which branch the driven dynamics
selects is open.** These are static energetics, and a driven steady state is not obliged to sit
at the static minimum; the question is held at §D.5 as a named piece of the kernel problem.

**Prior art.** Selection between a coordinate axis and a body diagonal, split by a tiny residual
anisotropy, is the standard phenomenology of cubic Dzyaloshinskii–Moriya helimagnets (Bak &
Jensen, *J. Phys. C* **13** (1980) 10.1088/0022-3719/13/31/002); and Luttinger–Tisza certifies a
*global* minimum only when its strong constraint is satisfied (Lyons & Kaplan, *Phys. Rev.* **120**
(1960) 1580), which is not verified here. What is the framework's own is the substrate bond
structure being minimised, not the helimagnet phenomenon.

**Scope of this minimisation — a stated sector reduction.** `E(q)` is Heisenberg-plus-DM
arithmetic on a unit 3-vector: it is written in the **L-orbit sector** of the site variable, not
over the full six-parameter 4D orientation that §D.3.2 declares. The 4D-bivector restatement —
the same problem carried over all six grade-2 directions — reproduces `E(q)` exactly on the
configuration named above, and is what yields the branch structure just described; the sector
reduction is therefore legitimate and is stated rather than left silent. What it does **not**
settle is the coupling menu: the D4/driven bilinear budget is larger than `{J, D}` alone
(§D.3.3), so `q`, the `D/J` calibration that rides it, and everything downstream remain
**truncation-conditional**, and `D/J` may be measuring a combination rather than a single bond
invariant.

**What this state is not.** A direct
stability scan finds the matched spiral **locally stable** from `D/J ≈ 0.75` through `~7.35` —
including the calibrated point and `D = J` — with *no static criticality anywhere in that range*
(the genuine instability is a cone transition near `D/J ≈ 8 ± 1`). That scan varies the **pitch**
at fixed `k̂`; it is blind to the transverse wavevector directions in which the axis branch is
unstable, so it does not conflict with the index-2 result above and does not survive as a
statement about the full `(k, B)` problem. The `D = J` point that
§C.1.6's L-orbit stiffness scaling calls "the QCP" is a zero of the **lepton-mass parametrization**
(`B = A ⇔ δ_L = π/12 ⇔ m_e = 0`, §C.3.6 — exact in the fitted Brannen form; the `D = J` form of
it is the corollary given the `A = J, B = D` ansatz), **not** a phase transition of the
helimagnet: `q(D/J)` is smooth through `D = J`. Nothing "becomes critical" there; R-108 is
DERIVED-A (the closed form as leading-order helical-rate invariant, and the stationarity of the
axis configuration) + DERIVED-numeric (the branch ordering, exact-arithmetic proof owed) +
LOCATED-GAP (`K_c`, branch selection, and any genuine substrate criticality).

### D.4.4 The full medium Lagrangian

Combining §D.4.1–§D.4.3, the substrate Lagrangian at the σ-model level is the **full Skyrme
Lagrangian with coefficients fixed at the dressed level, conditional on branch (c)** (R-109):

> `𝓛_medium = (1/2) · ⟨Ω_μ Ω^μ⟩_0 + (1/4e²) · ⟨[Ω_μ, Ω_ν][Ω^μ, Ω^ν]⟩_0 + 𝓛_top(D)`,

with `𝓛_top(D)` the DM-induced topological boundary term (R-110) of the form
`µ · Ψ_0 · ρ_L`, sourcing L-pair creation in the wave-riding sector (the substrate channel for
β-decay, §C.5.7). The kinetic coefficient is fixed by `f_π² = 8J/a` (R-106), the quartic
stabilizer by `e ≈ √18 / (D/J)` (R-107); the DM-topological coefficient `µ` is open (gated
on the substrate dynamics), and any τ₅-hyperbolic completion of this Lagrangian carries one
further undetermined coefficient — the weight `λ` of the mixed quartic sector
`⟨[Ω_5, Ω_i][Ω^5, Ω^i]⟩_0` — a menu whose covariant value is pinned only by the convention
that a single metric raises every index above, a convention that itself holds only within
§D.4.6's isotropic idealization.

**Branch (c).** The
bare exchange quartic is `κ_F = J/24`, giving `e_bare ≈ 0.87` — wrong by ~6× and
`D`-independent — while the DM-induced dressed contribution *diverges* as `k → 0` through the
gapless phason. So `e ≈ √18/(D/J)` is a relation among **dressed** couplings whose locality
rides the phason question — this is "branch (c)", the referent of the six companion rows
carrying the "§D.4.3 branch-(c) conditional" tier, and of §E.3.5(2)'s local-vs-phason-spoiled
fork.

### D.4.5 The Skyrmion collective inertia and the QCD scale

The Skyrmion's collective-coordinate inertia (the moment of inertia for rigid `SU(2)` rotations
of the soliton) at the dressed-coupling level is

> `Θ_0 = 106.76 / (e³ · f_π)`,

with `106.76` the exact-BVP inertia coefficient (`Λ = 50.98`; R-133 — an earlier `97.27`,
provenance suspect, is consistent with a truncated-grid artifact, §C.1.2). At the ANW fitted pair
`e ≈ 5.45`, `f_π = 129 MeV` — a pair fitted together, so the value below is quoted inside the ANW
scheme and is not a scheme-free number — this gives `1/Θ_0 ≈ 196 MeV`, used in three places
downstream: as the candidate identification with `Λ_QCD` (R-111 below), as the timescale in the top-quark
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

*A note on what "vacuum" means here.* The DM-coupled D4 vacuum is generically a **helimagnet**
with a spiral wavevector — `q ≈ 10.5°` per cell on the axis branch of §D.4.3, whose branch
structure and open branch selection that section states. The twist-gauge construction below needs
only that the reference is a helix of a single `q`; where a *numerical* stiffness is quoted, it is
computed on the axis branch and carries that label. For the
linearization, we work in the standard **twist-gauge** (rotating frame): the position-dependent
spiral rotation is absorbed by a field redefinition, so the rotor field in the twisted frame has
an `x`-independent (homogeneous) reference value `R_vac`. The Maurer–Cartan form in the twisted
frame carries a *constant* background term proportional to `q` rather than a position-dependent
gradient. We refer to this twist-gauge homogeneous reference as "the vacuum" below.

**The quadratic order, stated honestly — the engine's own canted-vacuum stiffnesses rule out an
isotropic form here.** Three
corrections, all `O(q)` or `O(q²)` in the spiral pitch: (i) the constant twist-gauge background
`Ω̄` **does** contribute at quadratic order — the banked N31 spin-wave result gives
direction-dependent stiffnesses on this very state (`K_long = √38·J ≠ K_trans` at `D = J`; a
~1–2% splitting at the working point), so the four spatial coefficients are *not* equal;
(ii) the Skyrme stabilizer is not `(∂Ω)²`-only — on the spiral background
`δF_μν = (q/2)[B, δΩ] ≠ 0`, an `O(q²(δΩ)²)` contribution; (iii) the fluctuation multiplet on the
canted vacuum is 1 gapless phason + 2 DM-gapped tilt modes (KP-1), not one massless multiplet.
The topological boundary term `𝓛_top(D)` still contributes only a constant. The linearized EL
equation is therefore the **anisotropic-stiffness form**

> `K_{μν} ∂^μ ∂^ν Ψ = 0`,  `K_{μν} = diag(c_meta⁻², K_1, K_⊥, K_⊥, K_⊥)` in the twisted frame,
> `K_1/K_⊥ − 1 = O(q²)` along the spiral axis,

whose **isotropic idealization**

> **`c_meta⁻² · ∂²_{τ_5} Ψ = (∂_1² + ∂_2² + ∂_3² + ∂_4²) Ψ`**

— timelike in `τ_5`, four Euclidean spatial slices — is what **Part B's QM/SR spine consumes**:
§B.2.1's Klein–Gordon (via Fourier reduction at `k_4 = m`), §B.3's Schrödinger, §B.4's Bell,
§B.5's Maxwell. *Whether the `O(q²)` splitting reaches a wavefront-locked observer* is an open
projection question (the same outside↔inside leg as I-19 premise (e)); a species-universal
splitting is additionally absorbable at leading order by the I-22 rescaling class, and the
space-fixed (sidereal) question is SC-2's. R-112 is conditional on that projection: the spine's
use of the isotropic form is an idealization with a named, bounded correction — not an exact
consequence of the canted vacuum. This linearization is around the *vacuum*, not around a defect.

**Where defects enter.** Linearizing around a *defect* background `R = R_def(x) + δR` would
generically give a wave operator with a position-dependent potential `V(x)` sourced by the
soliton profile — the standard story for soliton fluctuation spectra (shape modes, bound states).
That is **not the route taken in this section**, and the reason is conceptual rather than
evasive: the QM machinery of Part B only ever needs the **free propagator** plus a classical
**potential `V(x)`** — Schrödinger's equation is `i ℏ ∂_t ψ = (−ℏ²/2m) ∇² ψ + V ψ`, with `V`
treated as a c-number background. So a vacuum-linearization that produces the free wave operator,
plus a defect that sources `V(x)` as a classical background, would deliver what QM consumes —
**but the scalar-`V` form is a modelling assumption, not a substrate result** (§B.3.4's own
concession: the second variation about a soliton is matrix-valued
with zero modes and has not been shown to reduce to a single scalar `V(x)`). Soliton-shape modes and soliton-fluctuation bound states *are* genuinely there in
the substrate dynamics; they are a Paper-2 question about the full nonlinear fluctuation
spectrum, not about the QM machinery. So the framework's strategy is:

1. The linearization here is around the **vacuum**, giving the free 5D hyperbolic form.
2. The presence of a defect introduces a **classical background contribution** to the linearized
   equation as a source term `V(x)` — recovered as the static profile entering the linearization
   when matter is added back to the picture.
3. That `V(x)` is what §B.3.4 *names* as the Schrödinger-envelope potential — while conceding,
   as this section concedes with it, that the reduction of the matrix-valued second
   variation to a scalar `V` is asserted, not derived. The honest chain ends at "free wave
   operator + named modelling assumption".

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
Lorentz-protection class); and the boost-generated *moving* family — whose delivery hands the
dispersion chain a kinematic **consistency check**, not an independent second angle (in §B.2.2's
own language: the two routes share the
isomorphism and the front label, so their agreement is corroboration) — is delivered at §B.2.2
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
rotor-double-cover single-valuedness — the Finkelstein–Rubinstein frame, an external import
(companion Section 13, row I-20) — and *which* of the two
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

### D.5.2 The memory requirement — memoryless excluded for the selection roles

The substrate cannot have a **memoryless / Newtonian** kernel and still do what §B.3/§B.4's
Role-3 selection and §D.5.4's three roles require: an instantaneous-response medium supplies no
memory timescale at all, and `τ_mem ≫ τ_wave` is what those roles consume (R-114). Any
consistent substrate dynamics must therefore have a finite `τ_mem > 0`.

**This is not a monostability theorem.** One might try to argue that a defect relaxes to vacuum
under instantaneous response, "contradicting the existence of stable matter." That premise contradicts
§A.3's own topological stability — the drive-zero limit is the static Skyrme BVP with stable
integer-winding solitons, and a continuous flow cannot change `π₃(S³)` — and no derivation of
the stronger claim exists (the sole engine cite is FRAMING-tagged and asserts an enum). R-114 is
**FRAMING**: a requirement of the selection/memory machinery, not a stability theorem.

### D.5.3 The rich/hysteretic kernel — adopted on physical motivation

The **rich/hysteretic** branch of the kernel — `τ_mem = τ_wave · exp(S/ℏ)`
with `S` a barrier action — was adopted on physical motivation (defect persistence demands a
finite hysteresis), **not as a forced consequence** (R-115). The alternative is a **fading** kernel
with no hysteresis but finite relaxation; the memory requirement excludes only the
strict-memoryless limit (R-114, FRAMING), not the fading branch.

So the fading-vs-hysteretic fork is **gated on the substrate dynamics**, not closed. The rich
branch is the framework's working hypothesis, and the alternative is not refuted. **The fork is the framework's #1 gap.** (A concrete
candidate *class* for this kernel is proposed in §E.5.)

*Level.* The branch is the **first candidate instance's** exploration choice (§A.6.4, node V3-9),
and it is the cheapest of the eleven to revert: nothing banked in this paper rides it, so a
different family member may take the fading branch at no cost to anything above. What the family
owns is the kernel **programme** — that a memory kernel exists and does the three jobs of §D.5.4;
it owns no kernel.

### D.5.4 Three roles of memory

The memory kernel sources three physical roles (R-116):

- **Cell formation** at the substrate's cell-layer emergence — the mechanism by which the
  Planckian grain layer self-organizes into the cell layer (§D.3.5). Open.
- **Selection** (the Role-3 Born selection of §B.3 / §B.4) — the substrate-level mechanism by
  which a measurement outcome settles into a definite eigenstate. The linear-face safety chain
  protects QM and Bell from kernel uncertainty here.
- **Bell-pair memory** — the same kernel governs the §B.4.5 Bell-memory bridge, with the same
  `Im χ` transport function appearing as a single dial for both decoherence and pair-correlation
  memory.

Three operational windows, one kernel. The macromolecule-interferometry falsifier (§E.3 VG-1)
probes this kernel through the decoherence rate's `Im χ` dependence — an **inside-frame** datum
binding the outside-frame kernel only through the un-built outside↔inside projection (the
N33-1/N49 hedge; every sibling use carries it).

### D.5.5 Linear face structurally safe

What the linear face of §D.4 delivers — Klein–Gordon, Schrödinger, Dirac, Bell, Maxwell — is
structurally safe under the §D.5 fork (R-117). Three substrate-level results underwrite this:

- **Leak-independence** (WP-IX3): linear-face unitarity is preserved regardless of which kernel
  branch is realized, provided the required symmetry conditions hold — and they do (R-117).
- **Symmetry-protected unitarity** (WP-IX4): the substrate's `Spin(4)` symmetry prevents unitarity
  violation on the linear face.
- **Goldstone-symmetry-protected decoherence** (WP-DC2): the decoherence rate's lower bound is
  set by Goldstone-symmetry constraints (Adler-zero protection), not by the kernel's specific
  form. The macromolecule-interferometry rate is bracketed regardless of fork outcome (same
  inside-frame hedge as §D.5.4).

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

### D.5.7 Named pieces held at this gap

Some questions are not open because nobody has worked on them; they are open because their
answers live *inside* the unbuilt kernel. Those are recorded here as named pieces rather than
ruled, so that a future assembly finds them all in one place. Two belong to the bond sector.

**The entry coefficients of the extra bond channels into the `ℤ_3` amplitudes.** §C.3.7's
potential has exactly two amplitudes, `A` (parity-even) and `B` (parity-odd), and §D.3.3's menu
has more channels than `{J, D}` to fill them: `A = J + Σᵢ αᵢΓᵢ`, `B = D + β·D_spatial`. Whether
the `αᵢ` and `β` vanish is precisely what decides whether the lepton calibration measures `D/J`
or a combination. **Restrict the defect's twist to a single plane angle — or to two equal ones —
and it cannot be settled at bond-bilinear order at all:** the harmonic ceiling is then two, below
the third harmonic the `ℤ_3` amplitudes need, so every such harmonic vanishes identically, `J`'s
included, and the ratio is `0/0`. That ceiling is a property of the twist class and not of
bilinear order, and **the two-rate twist this candidate adopts (§A.4) is not subject to it**: a
twist whose two plane angles stand in a three-to-one ratio reaches the third harmonic at the same
bilinear order and at the same magnitude as the first, on the banked `J` coupling. So a
bond-bilinear determination of the `αᵢ` and `β` is **open, owed and unbuilt** — it needs no
kernel. What remains inside the kernel is their **dressed** values, and any statement that `Γ`
does, or does not, enter `A` at dressed level is a claim *about the kernel* and must be labelled
as one. (Pointers: §C.3.7 and R-070 forward here; §D.3.3 states the menu.)

**Which single-`q` branch the driven dynamics selects.** §D.4.3's canted vacuum has two
stationary branches — the coordinate-axis helix whose closed form the calibration rides, and a
body-diagonal helix lying lower in *static* energy. The static ordering is not automatically the
physical one: the substrate is a driven steady state, and a steady state under drive is not
obliged to sit at the minimum of a static energy functional. The selection is therefore a kernel
question, and until it is answered the branch-dependent content of §D.4.3 — the identity of the
canting plane, the geometric referent of "the canting angle `q`", and the exposure of the `Γ`
survivor, which vanishes on both high-symmetry branches but not on a generic wavevector — stays
conditional. (Pointers: §D.4.3 forward here; negatives ledger N62.)

Both pieces are candidates by construction: nothing routed through this gap may harden past
candidate status before the gap closes.

### D.5.8 Status summary

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

### E.1.1 The cosmological-constant residual — a present-epoch remark, not a dark-energy prediction

§B.7 covered the structural half of the cosmological-constant story: Volovik's self-sustained
medium identity (R-047) makes the gravitating vacuum energy vanish exactly at equilibrium. The
substrate is, however, driven-dissipative (per the §D.5 rich-branch commitment) — not in
equilibrium — so a residual survives, and its magnitude is an off-equilibrium computation at the
§D.5 #1 gap.

The residual is **not** to be written `Λ_residual ~ H²` (R-119) and read as a *structural
reason dark energy is small, nonzero, and tied to the front dynamics*. **That gloss does not hold.**
The expression `Λ ~ H²` admits two inequivalent readings, and the dynamical one is excluded by data.

**(a) The dynamical reading is excluded.** Take `ρ_vac(t) = 3ν M̄_Pl² H(t)²` at all epochs, with
`M̄_Pl` the reduced Planck mass. Substituting into the flat Friedmann constraint
`3 M̄_Pl² H² = ρ_m + ρ_r + ρ_vac` gives `3 M̄_Pl² H² (1 − ν) = ρ_m + ρ_r`, hence

> `Ω_vac(z) ≡ ρ_vac /(3 M̄_Pl² H²) ≡ ν`  for every `z`.

The vacuum *fraction* is epoch-independent — an identity, not an approximation — so this reading
cannot deliver a vacuum that is negligible early and dominant late. Matching today forces
`ν = Ω_Λ,0 ≈ 0.685`, i.e. the same 68.5 % at recombination and at nucleosynthesis. (A
separately-conserved `w = −1` component would give `ρ_vac = const`, which is reading (b); so (a)
necessarily runs on vacuum–matter exchange, as the literature treats it.) Two independent
consequences follow, each already measured against, plus one supporting estimate:

1. *Early dark energy.* The Planck 2015 dark-energy analysis (arXiv:1502.01590) reports in its
   abstract that the early dark-energy density "has to be below ≈2% of the critical density even
   when forced to play a role for `z<50` only" — and that `z<50`-only case is the **weakest** form
   of the bound. Reading (a)'s 68.5 % exceeds it by ≈ 34×. This is a direct comparison: a vacuum
   fraction against a bound on a vacuum fraction, with no translation step.
2. *No acceleration transition.* With `ρ_vac` locked to `H²`, total-energy conservation gives a
   single power law `a(t) ∝ t^{2/[3(1+w)(1−ν)]}` and a **constant** deceleration parameter
   `q = −1 + (3/2)(1+w)(1−ν)` (`−0.528` matter-era, `−0.370` radiation-era). There is no
   deceleration→acceleration transition at any redshift — not one at the wrong redshift, none.
   Flat ΛCDM on the same Planck parameters puts it at `1 + z_t = (2Ω_Λ/Ω_m)^{1/3}`, `z_t ≈ 0.63`.
   This prong imports no bound at all beyond the flat-FRW background, and it is the load-bearing one.
3. *Nucleosynthesis (supporting).* The extra `MeV`-epoch energy density is `ρ_vac/ρ_rad = ν/(1−ν)
   = 2.17`. Normalized as at the BBN epoch proper, where `T_ν = T_γ`, that is an equivalent
   `ΔN_eff ≈ 9.1`, against `ΔN_eff = −0.14 ± 0.21` from the light elements alone
   (arXiv:2401.15054) — over the 95 % ceiling by ≈ 33×. (The post-`e⁺e⁻`-annihilation
   normalization would give ≈ 16 and ≈ 58× instead; both are quoted so the convention is not
   hidden.) Stated openly: a `w = −1` component is not radiation, so this is an equivalent-energy
   translation used only to size the violation. The verdict does not rest on it. Matter–radiation
   equality is likewise displaced by many orders, but by how much depends on how the vacuum–matter
   exchange is partitioned between the two fluids — which reading (a) does not fix — so that is an
   illustration, not a forced consequence.

This is not a novel confrontation. Running-vacuum models are exactly this form, and the literature
form always retains an additive constant, `ρ_vac(H) = (3/8πG_N)(c₀ + νH² + ν̃Ḣ) + O(H⁴)` with `c₀`
fixed by `ρ_vac(H_0) = ρ_vac⁰` — that is, reading (b) plus a *small* running, with global fits
giving `ν_eff ≡ ν/4 = 0.00024 ⁺⁰·⁰⁰⁰³⁹₋₀·₀₀₀₄₀`. Reading (a) is the `c₀ = 0`, `ν = O(1)` corner of
that family, sitting ≈ 168× above the fitted 95 % ceiling.

There is **no `ν`-tuning escape** — it is a dichotomy. Either `ν = O(1)`, and the reading is
excluded on the probes above; or `ν ≲ 10⁻³`, in which case the residual survives but is a
sub-per-mille correction and is *not* the observed dark energy. On either prong the "structural
reason dark energy is small and nonzero" claim does not follow.

**(b) What survives is a present-epoch remark.** `ρ_vac` is constant, and what is true is the
*present-day* near-equality `ρ_vac = c M̄_Pl² H_0²` with `c = 3Ω_Λ,0 ≈ 2.06`. This is the reading
the engine already carries — `kernel_overdetermination_table` writes it with `H_0`, not `H(t)`, and
already calls `c = 3Ω_Λ` semi-definitional; the channel target `C6b` in
`kernel_candidate_constraints` carries the same coefficient. It must be labelled for what it is: in
a flat FRW universe `ρ_vac /(M̄_Pl² H_0²) = 3Ω_Λ,0` is the *definition* of `Ω_Λ,0` rearranged, so
its physical content is one bit — that `Ω_Λ,0` is of order unity rather than `10⁻¹²⁰`. That is the
coincidence problem restated, not a value predicted. **TWT makes no dark-energy prediction.**

What the framework does contribute here is R-047's dissolution of the Λ *catastrophe* at the
equilibrium-identity level — untouched by the above, being an equilibrium statement — plus an
off-equilibrium residual whose **magnitude** is #1-gap-gated and whose epoch dependence, should the
gap ever supply one, is now bounded in advance by the arithmetic of (a).

**Tier consequence.** R-119 keeps its tier (FRAMING + value-gated) but its scope narrows to a
magnitude with no derived epoch law; the dynamical branch is recorded as a located negative (N54).
Canonical falsifier §E.3 VG-2 is narrowed accordingly — the epoch-law face is not pending, it is
closed.

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

**The relic contribution is ~1% of Ω_DM (sterile share).** With Dirac character tying
`m_sterile = m_active` per generation, the sterile mass scale inherits the active scale
`Σ m_ν ≲ 0.12 eV` (Planck + BAO, 95%) — and the cosmological bound has since tightened to
`≲ 0.064 eV` under ΛCDM while relaxing to `≲ 0.16 eV` once the dark-energy equation of state is
freed (DESI DR2, PRD 112, 083515 (2025)), so the shortfall below is quoted at the looser, older
input and the tighter input roughly doubles it. The thermal upper bound gives
`Ω_{ν+s} h² ≤ 0.00255` for the
active+sterile **total** (~2.1% of Ω_DM; 47×); the standard relation `Ω_ν h² = Σm_ν/94 eV`
already counts the active species, so the **sterile share is half: `Ω_s h² ≤ 0.00128`, ~1.1% of
Ω_DM — a 94×–176× shortfall depending on which cosmological bound is taken** vs the needed
dark-matter density (R-122). **The larger figure is the ΛCDM one, so the current primary makes
this scope-line worse rather than better; it is quoted as a range for that reason.** Sub-eV thermal Dirac fermions are independently
hot-DM-excluded by free-streaming (Planck + LSS `f_HDM < 0.01`); the Dodelson–Widrow sterile
window requires `m_s ~ keV`, four orders above TWT's tied-to-active scale. This is the *expected*
first-cut outcome — sterile RH neutrinos are notoriously hard to make up all of dark matter — and
is recorded as a quantitative scope-line, not a refutation of the structural three-count
prediction.

**The remaining ~98% of Ω_DM is outside TWT's current derivational scope.** The framework does
not predict a specific mechanism, particle, or substrate texture for the dominant
dark-matter component. A wavefront-texture proposal is ruled out by the §B.6
induced-GR result, which removes its scalar-gravity premise; no replacement has survived
review. This is a **deliberate scope statement**, not a placeholder claim.

Three re-attack handles within the sterile-RH lead remain as Paper-2 research leads (Z1, Z2, Z3
in the pending-values registry — companion Section 4). Of the two additional leads, the
**differential-coupling lead is a clean structural negative (R-146)**: the
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

The **wave-train phase-defect lead is also a clean
negative (R-147)**: the blade, not the topology, fixes the metric source — balanced-blade and
carrier-phase (`U(1)_E`) defects are h-null exactly (even at non-unit amplitude), the only
gravitating dislocation (the chiral-ideal SD-phase one, `h = −½dθ⊗dθ` exact) sources geometry
identically through the EM-visible L–Q cross term pointwise, and no `π₁` protection exists in
the rotor field (the winding-1 dislocation loop is explicitly unwindable; the one ℤ-protected
class, carrier-phase vortices, is exactly the h-null one). Nothing is simultaneously
gravitating, EM-dark, and topologically protected.

Both leads thus funnel into the
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

**Four counted substrate INPUTs plus measured `G_N`** (see the Opening, ordered by structural
weight): the weak sector's one empirical bit — the right-handed fermions' weak-singlet character,
which closes §C.4.2's computed menu and is read rather than tuned, carried together with that
section's named structural premise — `f_π` (cell mass scale), `D/J` (chirality), `c = √2 ⇔ K = 2/3`
(the circulant-parametrization amplitude), and the measured Newton constant `G_N` as the
gravitational anchor — both `Λ`
scales are back-fits of `G` through the induced-gravity form and are not counted separately
Plus `A` (lepton
amplitude scale — cancels in ratios; not counted), **and `δ_L` (the generation phase — not counted
separately, because `D/J := tan(3δ_L)` by definition, so `δ_L` and `D/J` are one piece of empirical
information under two descriptions; counting both would double-count a single measurement, and the
`D/J`-level agreement between them is a tautological restatement rather than a confirmation)**.
**`c = √2` and `K = 2/3` are ONE counted bit,
not two:** in the circulant parametrization the Koide relation *is* the statement that the
modulation amplitude squared equals `1/2`, independently of the phase `δ` (§C.3.2, §C.3.3), so
counting them separately would double-count a single piece of empirical information.
`Λ` is not a separate empirical quantity here:
the framework posits no independent cutoff scale, and counting one would overstate the ledger.

One further piece of information is counted **provisionally**:
the ANW Skyrme stabilizer `e = 5.45`, consumed by every §C.1.2 hadron number.
It is counted as the **hadron-sector determination of the same object** the substrate relation
`e = √18/(D/J)` predicts — `≈ 5.37–5.39` depending on the `D/J` digit (0.79 engine default vs
0.7869 lepton leg) — one object, two determinations, agreeing at
1.1–1.5%. That agreement is a **hedged** cross-check, not a blind one:
the massless-pion baseline scheme was itself chosen partly on this agreement (the banked
massive-pion branch gives `e* = 4.84`, an 11% scheme spread), and the substrate relation carries
**no scheme label** — the same blind spot N57 found for the Koide mass definition; both point at
the missing **renormalization dictionary** of the outside↔inside projection. Retirement
conditions, both ways: if the sharpened legs (massive-pion/beyond-rigid-rotor on the fit side;
branch-(c) closure and the `√18` referent on the prediction side) **converge**, `e` retires from
the ledger and the count drops back to four; if they **split**, the `√18` bridge dies and the
convergence claim with it.

One structural **premise** is also counted — an identification rather than a numeric input, but
information the framework consumes without deriving: **`m = E₀`** (§A.4), the defect's rest
frequency equals its vacuum-subtracted outside elastic cost in lock units. It is the standard
soliton-mass identification, and every comparison of an elastic value with a measured mass
crosses it (§C.1.2); stating and counting it replaces its previous silent use. It presupposes
the one-particle spectral identification (§D.4.6 residue) and carries **no scheme label** — the
third named face of the missing renormalization dictionary, beside N57's mass-definition face
and the `e`-scheme face above.

**The ledger is the candidate's, not the family's.** Every item counted above is consumed by
**Instance V3** (§A.6): `f_π`, `D/J` and `e` are its calibration picks; the measured-`G` anchor is
a family-endorsed *practice* whose conversion into a cutoff runs through its gravity pick;
`c = √2` and `m = E₀` are preferred directions this candidate takes, while the weak assignment is
not itself a preference but a forced consequence of §C.4.2's closed menu and its two named
supports — one of which, the weak-hosting premise, is a preferred direction like the other two. The family's own
ledger is shorter and emptier in a way that must not be mistaken for economy: **the family has
zero earned dimensionful scales.** Everything it genuinely earns is dimensionless or structural,
the two scales in use here are a back-fit and a fit, and the ratio between them is neither derived
nor protected (§D.3.5). A candidate that declines these picks does not thereby carry a smaller
parameter count — it carries no numbers at all, which is a different thing and a worse one.

### E.2.2 Pending-values registry — what each gap unlocks

The framework's open numerical values cluster on a small number of deep objects:

- **Gated on `Im χ` (the #1 gap):** `α_em`, `g`, `α_s`, `α_W` — the four EW + strong couplings,
  via §B.5b's single-dial economy. Decoherence rate `1/T_2` (the macromolecule-interferometry
  decoherence floor is the same dial's second operational window, §B.4.5), cosmological-constant
  residual (present-epoch **magnitude only** — the `∝ H²` epoch law is excluded, N54/§E.1.1).
  **Six magnitudes, one transport function.**
- **Gated on `Θ_rel` (the FDT-violation residual):** colour-U(3) → SU(3) breaking, CKM
  hierarchy + Jarlskog, asymptotic-freedom DGLAP structure + magnitude (the *sign* face is
  decided-conditional — the AF-signed branch `β_3 ≤ 0`, R-148 §C.5.2, conditional on the
  registered dispersive import I-13), coupling-universality (a candidate route via SOC).
- **Gated on absolute ω scale:** `f_π` absolute MeV, `M_0` baryon mass, `1/Θ_0`, `f_L` via
  L-orbit QCP scaling, same-composition mass split magnitudes, vector meson absolute masses — all read
  through the `ω` ↔ renormalized-mass identification, itself unfixed (N57; one face of the
  missing renormalization dictionary, with the `e`-scheme label §E.2.1 names as the second).
- **Already measured against, second instance:** the `g_1 = g_2` crossing
  scale — the framework's lattice-scale reading misses `sin²θ_W(M_Z)` by 33% (N55, §C.4.5;
  exposure §E.3.5(5)). Like the dim-6 ceiling, a number the framework owes, not lacks.
- **Gated on `S` (rich-branch barrier action):** `τ_mem`, tunneling rates, Born selection rate.
- **Gated on L2 mechanism:** active-sterile overlap for `m_ν`. (The L-orbit `ν = 3π/2` is **not**
  listed here as a pending value: it is a candidate *value* with no mechanism and no empirical
  target, and closing an L2 mechanism would not by itself unlock a mass — the stabilising
  functional would have to be settled first.)
- **Located-gap items with named re-attack handles:** the critical canting/magnon stiffness
  `K_c`; the sterile-RH dark-matter lead (Z1/Z2/Z3).
- **Gated on the strain-mode dispersion — and, uniquely, already measured against:** the
  isotropic dimension-six Lorentz-violation coefficient `η⁽⁴⁾` (§E.3.3 VG-6). Every other entry
  above is a magnitude the gap fails to *deliver*; this one the gap must deliver *beneath an
  existing number*. At the substrate's natural coefficient — `c = 1`, a naive value the framework
  does not claim and cannot presently compute — it would read `η⁽⁴⁾ ∈ [1.9, 6.7]` (ruled `Λ_L`
  band, §B.6.2), excluded unconditionally by about one order of magnitude (a single model-independent cosmic-ray analysis, superluminal branch), and by six to seven orders only under a mass-composition assumption the same observatory's data disfavours. It is therefore a **ceiling, not a target**: it can refute a candidate
  kernel outright, but supplies no equation and so adds nothing to the over-determination count
  below.

Alongside the *value* gates above, the framework's structural results carry a second, shorter
inventory: the **named premises** on which otherwise-derived conclusions still rest. These are
not open numbers but open lemmas, each with a stated would-change-if, and together they are the
honest distance between the current text and a fully forward-derived spine:

| Premise | What it conditions | What would discharge it |
|---|---|---|
| **F2** — statistical noncontextuality of the Role-3 selection functional | the Born exponent's theorem status (§B.3.3, R-160) | a Role-3 construction carrying the channel-pairwise drag structure **and an offset-measure class and a read-out class — the structure alone is insufficient, computed** |
| **P1b-DYN** — the mode determinant generates the induced term | fermionic Skyrmion quantization as *induced* rather than selected (§B.3.5, R-161) | the substrate computation of the induced term (#1-gap adjacent) |
| **OA-LF-i / OA-LF-ii** — ground-state occupation; grain-scale covariant curvature coupling | the induced-gravity magnitude bracket (§B.6.2, R-163) | the kernel, or a curved-lattice band construction |
| **cross-block rigidity** (+ an open cross-block weight) | folding `α_s` into the single-dial economy (§B.5b.3, R-162) | a kernel with the named universality across inequivalent Schur blocks |
| **P4 / P5 / P6 / P7** — one universal charge functional; per-defect chirality-independence; proton = `uud` state identification; cross-sector weak-isospin alignment `T_3(e) = T_3(d) = −T_3(u)` | the proton–electron equality as theorem rather than anchor (§C.2.7, R-159) | an EM-sector construction fixing the functional's universality, plus a derivation of the doublet slot assignment |
| **the ℍ-unit identification (+ the associativity premise)** | the three-generation count (§C.3.8; count itself generic-given-4D) | a substrate-dynamical selection of the generation triple, and a substrate reason for associativity (vs the octonionic route) |
| **P-an / P-pg / P-gs / P-op** — analyticity of the dispersion kernel in `k`; the *full* point group including triality; the ground state preserving the point group (the §D.4.3 spiral breaks it; the residual is SC-2's sidereal question); and that the symmetry *operative* on the spatial anisotropy sector is that full point group rather than the **driven** subgroup — the order-48 stabilizer of the advance axis, which restricts onto `W(B₃)` and admits a two-dimensional degree-four spatial invariant space containing `Σ_{i≤3}k_i⁴` | the dimension-eight anisotropy result (§B.1.5, R-165) | a kernel shown analytic at grain scale (a non-analytic memory kernel — the #1 gap itself — escapes any polynomial-invariant argument), a substrate coupling shown to weight triality-related orbits equally (unequal weighting restores dimension-six anisotropy), either a point-group-symmetric vacuum or the sidereal residual computed (SC-2), and — for **P-op** — either a demonstration that the effective real-time kernel is invariant under the full point group and not merely the driven one, or the driven-sector spatial fourth moment shown to stay zero once dressed (at tree level it is zero, but by a `+4`/`−4` cancellation between the `e₄`-bearing and in-hyperplane bonds, not by symmetry) |

Five of the seven route into the same place the value gates do — the driven-dissipative dynamics
of §D.5 — which is the framework's central structural claim about its own incompleteness: not
many independent gaps, but one object with many faces. P-an is the sharpest instance: the premise
that would discharge it and the object that would break it are the same object.

The **over-determination opportunity**: pin-and-check across
the registry's collective set provides constraints on the kernel objects beyond what any one
item gives. A candidate `Im χ` value must satisfy all the gates simultaneously. That programme has
a second and different kind of leverage: one of the gates is a
measured *ceiling* rather than an unpinned target, so a candidate kernel can be **refuted by
existing data** before any over-determination is assembled. This does not raise the anchor count —
an inequality supplies no equation — but it changes the programme's character, from purely
internal consistency-checking to a search that external measurement can already cut.

### E.2.3 Parameter reduction — honest count

The textbook SM count is 19 free parameters (three gauge couplings, the strong-CP phase `θ_QCD`,
Higgs VEV, Higgs mass, six
quark masses, three charged-lepton masses, and the four CKM parameters — three angles plus one
CP phase), rising to 26-28 with neutrinos.

**On the magnitude axis**, TWT pins:
- **0 of the 19 at their measured values.** The one entry that might read as unconditional —
  `sin²θ_W = 3/8` (R-082) — is a normalization *identity* (`g_1 = g_2`
  restated), pinned at a crossing scale the framework does not derive; its only computable
  descent lands `0.154–0.158` against the measured `0.2312` (N55, §C.4.5), carried as an open
  exposure (§E.3.5(5)), not a pinned parameter.
- **Up to 3 conditionally**: the Cabibbo angle via the frequency-ratio reading
  `|V_us|² = m_d/m_s` (§C.3.10, a candidate — the relation itself is Gatto–Sartori–Tonin's,
  1968; only the reading is claimed), rising by **two** more if `δ_L` is forward-derived
  (§C.3.5's route, currently refuted): the charged-lepton sector is otherwise a
  three-parameter fit to three masses — net magnitude content zero, and only two independent
  ratios exist once the amplitude is stripped.
- **TWT does NOT derive**: any coupling magnitude (#1-gap-gated), individual quark masses
  (the framework's mass-scope rule, §A.4: abstention from independent quark masses), Higgs VEV, Higgs mass, CKM hierarchy
  (#1-gap-routed), PMNS matrix (defused — no substrate prediction), neutrino masses (gated).

**Headline: 0 of 19 unconditional + up to 3 conditional** on the magnitude axis.

**On the structural axis**, TWT delivers **ten structural derivations** of SM choices
the SM treats as postulates rather than parameters: the gauge group structure (§C.4); the charge
spectrum (§C.2 — the discreteness unconditional, the normalization conditional on P4–P7 plus the entered anchor);
the three-generation count (§C.3.8, generic-given-4D, conditional on the ℍ-unit identification
+ the associativity premise); `B − L` conservation +
anomaly cancellation + Dirac neutrino character as one fact (§C.5.4–§C.5.6); no proton decay +
no `0νββ` (§C.5.6); the up/down mirror (§C.3.13); V−A + generation-blindness + doublet (all from
the §C.4.2 weak assignment); the Lorentzian signature flip (§B.1 — posit plus derived implication, per §E.4.1);
the no-monopole result (§B.5.2, conditional on the
winding-as-source identification); the Tsirelson bound (§B.4, conditional on the assumed
tensor-product state space).

**This is the parameter reduction TWT actually claims.** On the magnitude axis the framework
honestly leaves most of the SM's 19 parameters #1-gap-gated. On the structural axis, the
framework's contribution is the conversion of SM postulates into substrate consequences.

---

## §E.3 — Falsifiers

### Disclaimer — the scope of falsifiability in a framework under construction

**Two levels, and the reader must keep them apart.** The architecture of §A.6 is what makes this
section readable: there is a **family** — TWT-Core, seven axioms and one refusal — and there is
**V3, the first candidate instance**, which is what this paper builds. A falsifier can therefore
land at either level, and the difference is not rhetorical. A row that reaches only an instance
pick kills *this candidate* and leaves the family intact with a named menu to re-pick from. A row
that reaches an axiom kills *every* candidate at once.

This theory is under active construction. The falsifiers listed below concern, in the main, the
**current formulation** — the specific derivations, identifications, and structural claims this
paper makes. Most of them, if triggered, would falsify the current formulation and *force an
evolution of the framework*: a reformulation of the substrate, a different identification of a
symmetry, a modified derivation chain.

**The exception is the family's kill condition, and it is deliberate.** The preferred foliation is
not left free — it is identified with the cosmic rest frame (§A.6.1, B-6), which is a
family-defining axiom rather than a pick. **If the ordering that Bell-correlation selections
follow is measured and found to be a foliation measurably distinct from the comoving frame, the
family is finished** — not one version of it, all of it (rows 4 and 5 below). The safe option was
available and declined: an unnamed preferred foliation cannot be caught, because "there is a
frame, somewhere" survives every measurement. Two riders travel with the choice and neither is
optional. The measurement that would fire it is one standard quantum mechanics *also* forbids, so
in this channel agreement confirms nothing and disagreement kills — maximum downside, no matching
upside. And it is the family's *only* total kill condition: of the sixteen rows in §E.3.1, fourteen
stand at family level and two are instance-level (row 6, this candidate's `c ↔ c_meta`
identification, and row 12, whose kill number rides a pinned hadronic
calibration). Because the channel fires only where quantum mechanics also breaks, the family
carries **no independent empirical exposure in it**, and §A.6.2 names the one identified route to
building an exposure of its own. That is not the same as saying the family is untouchable by
experiment: row 6 below reaches this candidate's identification of the observed `c` with the
average lock rate — the axioms themselves state no rate and no uniformity, so the exposure is
instance-level and a positive detection would put the non-uniform label on `c`, the emergent
observer-side speed, not on the axioms — and "How to read the tables" states exactly what is and
is not settled about it.

Outside that channel, the underlying ontological premise — a wave-based Euclidean substrate with
matter-as-defect — is compatible with a wide range of specific realizations and would evolve to
accommodate an observed fact that contradicts the current formulation. That robustness is a fact
about the family's generality, not a credit to it: **generality is what makes a family hard to
kill and a candidate worth having**, and the two already-measured exposures below are the price
this candidate pays for saying numbers at all.

Given TWT's **extensive overlap with the Standard Model on observable predictions** (exact
wherever the framework's derived structure reaches — the QCD dynamical sector is underived;
the framework's contribution is to *derive* SM structural facts from a substrate rather than
take them as input), a large fraction of the falsifiers below would simultaneously kill the SM if they
triggered — because they test predictions the SM and TWT share. The truly framework-versus-SM
discriminators are a smaller subset.

**Row-by-row classification against this scope.** Reading E.3.1 with this lens:

- *Kills TWT-current AND SM together* (both would need to reformulate): CHSH > 2√2 (row 9),
  fractional charge outside `{±1/3, ±2/3, ±1}` (row 11), tree-level FCNC (row 15), and a
  baryon containing a top quark (row 12 — standard QCD's `Γ_t ≫` hadronization-rate argument
  makes the same exclusion). These test
  QM-Tsirelson, algebraic charge quantization, Schur-lemma constraints, and a decay-timescale
  argument that the SM also commits to.
- *TWT-current specific, SM survives* (would falsify TWT's current formulation but leave the SM
  unaffected): proton decay (row 2; SM predicts stability too, but TWT's topological route is
  what fails), `0νββ` (row 3; SM allows Majorana, TWT commits to Dirac), magnetic monopole
  (row 10; SM allows monopoles, TWT forbids), fourth generation (row 13; SM allows,
  TWT forbids).
- *Non-discriminating — consistency checks rather than falsifiers*: finite Geneva-class influence
  speed (row 4) and Bell-selection foliation ≠ comoving
  (row 5). A finite influence speed *would also be
  inconsistent with quantum mechanics' exact predictions*, so the influence-speed experiment tests
  QM at least as much as it tests TWT. Row 9
  (CHSH > 2√2) is non-discriminating in the same way and is already classified above as killing
  both. A framework that derives QM inside-frame (§B.3) cannot be discriminated from QM by an
  experiment whose possible outcomes QM already fixes; naming these as near-term *kills* would
  over-sell them, and they sit in the table as null-result checks rather than as discriminators.
- *Framework-general vs specific-derivation* (kill the current derivation but the framework's
  ontology can plausibly evolve): `c_GW ≠ c_γ` (row 1),
  differential `c_meta` (row 6), optical-clock decoherence (row 7), macromolecule decoherence
  (row 8), truly independent `θ_C` (row 14).

A fifth exposure sits outside all four categories: the dimension-six LV coefficient (§E.3.5(4))
is not a pending detection but a **standing tension with existing data**, awaiting a substrate
computation rather than an experiment. It is also, with the crossing-scale miss, one of the two
exposures that belong to **this candidate instance** rather than to the family (§B.6.3, §C.4.5).

**The same rows, sorted by level.** Fourteen of the sixteen are **family-level**: rows 1, 2, 3,
9, 10, 11, 13, 15 and 16 follow from the axioms or from the axioms plus one stated preferred
direction; rows 4 and 5 are the family's kill condition itself; rows 7, 8 and 14 are family-level
but value-gated or weak. Two rows are **instance-level**: row 6, because it rides this
candidate's `c ↔ c_meta` identification — the axioms state no rate and no uniformity, so a
positive detection labels the emergent `c` non-uniform and the axioms stand — and row 12 (no
top-quark baryon), because its
kill number is built on this candidate's fitted hadronic calibration and its semiclassical
inertia — a different anchoring re-derives the timescale or loses it.

**How to read the tables.** For most rows a single positive detection triggers the next
candidate, not a framework obituary: the ontological core is more robust than any specific
derivation, and the family's honest exposure there is *what would force a re-pick*.

**Two rows are different, because they reach an axiom rather than a derivation — and they reach
different axioms through different channels.** Rows 4 and 5 reach B-6, the identification of the
preferred foliation with the comoving frame: that is the family's total kill condition, and it
fires only in a channel where standard quantum mechanics is also wrong, so it carries maximum
downside and no matching upside. Row 6 reaches this candidate's `c ↔ c_meta` identification (the
`A-3`-downstream chain), through a channel the shared quantum formalism does not itself close —
the axioms state no rate and no uniformity, so a robust detection would label `c`, the emergent
observer-side speed, non-uniform while the axioms stand, and the row is the sharpest
*instance-level* exposure with an independent experimental route. The row is not this
framework's alone: exact Lorentz invariance forbids a sector-differential limiting speed as well,
so a positive detection costs the incumbent a symmetry at the same time. What separates it from
rows 4–5 is the *kind* of prohibition — there, a theorem of the formalism this framework
reproduces, so agreement is guaranteed in advance; here, an imposed symmetry a completed
candidate could in principle depart from. And what row 6 reaches is this candidate's
`c ↔ c_meta` identification, not an axiom: the axioms state no rate and no uniformity, so a
positive result there labels the emergent `c` non-uniform, the axioms stand, and the family
reformulates at the instance layer — it does not end.

The four operational categories: named near-term (single-detection-away), removed
(achievements), value-gated (await #1-gap closure), structural-coherence (would break internal
construction). The internal pre-mortem (§E.3.5) is the fifth category — internal exposures
rather than external detections.

### E.3.1 Named near-term falsifiers (single-detection-away kills)

The rows below are ordered by channel, not by tightness. **The framework has no LV row in this
table**: its dimension-six residual coefficient is gated on the #1 gap and is recorded at §E.3.3
(VG-6) and §E.3.5(4) as an open exposure rather than a near-term test.

| # | Falsifier | Channel / apparatus | Current bound | TWT prediction | What it kills | Origin |
|---|---|---|---|---|---|---|
| 1 | `c_GW ≠ c_γ` beyond the multimessenger interval | GW + EM multimessenger (GW170817-class) | `−3 × 10⁻¹⁵ ≤ (c_GW − c)/c ≤ +7 × 10⁻¹⁶` (ApJL 848, L13 (2017) §4.1 — two-sided and asymmetric, conditional on the assumed emission-time offset and on `D = 26 Mpc`) | structural `c_GW = c_γ`, automatic for matter-loop-induced gravity riding the same wavefront | induced gravity riding the wave | §B.6.3 |
| 2 | Proton decay (`p → e⁺π⁰`, the strongest channel; other channels ~3× weaker) | Super-K, Hyper-K, DUNE | `τ/B(p → e⁺π⁰) > 2.4 × 10³⁴` yr, 90% CL (Super-K, PRD 102, 112011 (2020)); the same collaboration's `p → μ⁺η` and `p → e⁺π⁰π⁰` limits sit near `7 × 10³³` yr | absolutely stable **in the smooth sector** (`B ∈ π_3 = ℤ`; a grainy member carries a resolution condition, deficit ∝ 1/ρ²; non-perturbative violation only as `ΔB = ΔL = 3`) | topological protection of `B` | §C.1.5, §C.5.6 |
| 3 | `0νββ` detected | KamLAND-Zen, LEGEND, nEXO, CUPID | `T_{1/2}(¹³⁶Xe) > 3.8 × 10²⁶` yr, 90% CL (KamLAND-Zen, complete dataset — the 800 phase combined with the previous phase; PRL 135, 262501 (2025)) | forbidden (Dirac neutrino forced by `B − L` conservation; Majorana requires `Δ(B−L) = −2`) | Dirac character of the neutrino | §C.3.12, §C.5.6 |
| 4 | Finite Geneva-class influence speed found (Salart et al. 2008; Yin et al. 2013) | Bell-correlation timing in candidate preferred frames | `v_inf > 10⁴ c`, conditional on the candidate frame's velocity relative to Earth staying below `10⁻³ c` (the primary's own stated condition) | no finite influence speed — operationally, signaling does not exist | non-separability without signaling (`τ_5`-foliation = cosmological comoving) — **consistency check, not a discriminating falsifier**: a finite influence speed *would also be inconsistent with quantum mechanics' exact predictions*, so the experiment tests QM at least as much as it tests TWT — the framework is isomorphic to QM in this channel (§B.4, import I-11) and inherits the verdict either way | §B.4.5 |
| 5 | Bell-selection foliation ≠ cosmological comoving frame | precision Bell + cosmology cross-comparison | n/a (corollary of row 4) | identical | the `τ_5`-foliation = comoving identification — **the family's kill condition** (§A.6.2): the identification is a family-defining axiom, not a pick, so what a mismatch kills is every candidate at once, not this formulation. It remains a **consistency check rather than a discriminating falsifier** in the empirical sense — being row 4's own corollary it inherits row 4's QM-shared character, so the channel fires only where quantum mechanics also breaks, and agreement in it confirms nothing. Maximum downside, no matching upside; that is the price of naming the frame | §B.4.5 |
| 6 | A sector- or epoch-dependence of the observed `c` against the lock rate `c_meta` | precision multimessenger astronomy | `c_meta = c` on average | structural identity globally | §A.4, §B.7 average-`c` identification — this candidate's `A-3`-downstream chain, an **instance-level** exposure: the axioms state no rate and no uniformity, so a detection labels the emergent `c` non-uniform while the axioms stand; what that does and does not settle is stated at "How to read the tables" above | §A.4 |
| 7 | Optical-clock decoherence below Goldstone-symmetry floor | atom-interferometry, optical clocks | **no computed floor exists** (#1-gap gated; `Im χ` uncomputed) — this row is VG-3's operational face, kept here as a null-result check, **not** single-detection-away | rate bounded below by the Goldstone floor (Adler-zero protection) — floor value gated | symmetry-protected decoherence safety | §D.5.5, VG-3 |
| 8 | Macromolecule-interferometry decoherence below `Im χ` floor | macromolecule interferometry | **no computed floor exists** (#1-gap gated) — VG-1's operational face, kept as a null-result check, **not** single-detection-away | substrate sits near the conjectured KSS `η/s ≥ ℏ/4π` floor; bracketed KSS-to-GW-propagation — floor value gated | the `Im χ` master dial (one dial, two windows) | §B.4.5 Bell-memory bridge, VG-1 |
| 9 | CHSH violation `> 2√2` | quantum optics | bounded by Tsirelson | bounded by `2√2` | one-sided rotor half-angle structure | §B.4.1 |
| 10 | Magnetic monopole detected | various | none observed | absent — the grade-3 slot exists (4 components) but the winding-as-source identification supplies nothing to fill it | the winding-as-source identification (**not** a pure algebraic forbiddance) | §B.5.2 |
| 11 | Fractional charge outside `±1/3, ±2/3, ±1` | direct searches | none observed | forbidden (algebraic identity from the Clifford algebra's trivector content — the spectrum does not ride the lattice arrangement) | charge-spectrum algebraic identity | §C.2.2 |
| 12 | Baryon containing a top quark | LHC | none observed | forbidden (`Γ_t · Θ_0 ≈ 7.2 ≫ 1`) | timescale-exclusion structural argument — **the one instance-level row in this table**: the kill number rides this candidate's fitted hadronic scale and its semiclassical inertia, so a re-anchored family member re-derives the timescale or loses it | §C.5.9 |
| 13 | Fourth fermion generation | LHC + neutrino-oscillation precision | none observed | forbidden (`dim Λ²₋(ℝ⁴) = 3` — exactly three anti-self-dual planes in four dimensions, computed in-engine; Frobenius a structural remark via the associativity premise) | generic-given-4D count + `ℍ`-unit identification + associativity premise (conditional) | §C.3.8 |
| 14 | Hierarchical CKM `θ_C` shown demonstrably independent of the `m_d, m_s` relation at sub-percent precision | high-precision CKM data | `\|V_us\|² ≈ 0.0503`; `m_d/m_s ≈ 0.0500` (~0.6% agreement) | frequency-ratio reading of the **Gatto–Sartori–Tonin** relation `\|V_us\|² = m_d/m_s` (GST 1968 — the relation is not TWT's; only the reading is) | the frequency-ratio reading of Cabibbo | §C.3.10 |
| 15 | Tree-level FCNC observed | precision flavour physics | no tree-level signal; the `ΔS = 1` neutral-current decays sit at `B(K_L → μ⁺μ⁻) = (6.84 ± 0.11) × 10⁻⁹` and `B(K_L → e⁺e⁻) ≈ 9 × 10⁻¹²` — the smallest measured branching fraction of any particle decay — with `B(K_S → μ⁺μ⁻) < 2.1 × 10⁻¹⁰` at 90% CL (PDG 2025). These are measured rates that the incumbent generates at loop/long-distance level, so what they bound is the tree-level contribution on top of that | forbidden at tree level (weak = SD couples generation-blindly) | the §C.4.2 weak assignment, i.e. its structural premise or its empirical leg | §C.4.2 |
| 16 | Proton–electron charge sum non-zero | neutrality-of-matter / bulk-matter charge tests | `\|Q_p + Q_e\|/e ≲ 10⁻²¹` | exactly zero, identically in the charge normalization `c` | the (P4–P7) premise set — the framework reverts to an empirical charge anchor | §C.2.7, §C.2.8 |

Each row is a single positive detection away from falsification, or a null result still consistent
at current precision. (A frame hedge on rows 7–8: the laboratory limits there are
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
| RF-2 | Catastrophic `ξ = 1/6` Sakharov cancellation | Maurer-Cartan shift-symmetry forces `ξ = 0` at leading order; `ξ R φ²` is shift-non-invariant. Residual `(f_π/Λ)² ~ 10⁻⁴⁰`-class (`2–8 × 10⁻⁴⁰` on the `Λ_L` band; reading-immaterial), not `1/6` | `sakharov_xi_minimal_coupling` | §B.6.5 |
| RF-3 | Lepton-sector G-as-colour-Z_3 single-domain breakdown | Modus tollens: framework's commitment to spontaneous (not explicit) SSB on lepton mass operator is consistent with empirical Koide at `~10⁻⁵` **at pole masses** — ~5 orders inside the band (scheme-dependent: the one-loop pole→MS-bar conversion degrades the margin to ~2.7 orders; N57 flag) | `koide_modus_tollens_consistency` | §C.3.9 |
| RF-4 | Cabibbo `f_perp` hypothesis | 0%-or-82% categorical fork, no few-percent branch. Closed NEGATIVE | `over_determination_scan` | §C.3.10 corollary |
| RF-5 | `V_PMNS = I` phantom prediction | Defused: substrate provides no amplitudes pinning PMNS; never was a TWT prediction. PMNS magnitude #1-gap GATED | `pmns_no_substrate_derivation` | §C.3.12 |
| RF-6 | ν-asymmetric reframing route | Counter-indicated by substrate-level checks | `neutrino_orbit_asymmetry_attempt` | §C.3.12 |
| RF-7 | Over-production test (predicted stable orphans) | Stable set `{γ, p, e, ν, stable nuclei, antiparticles}` matches observation exactly — no orphans, no gaps. Two reasons: SM's two topological charges exactly, internal multiplicity capped at 3 by 4D Z_3 | `topological_overproduction_test` | §C.5.8 |

RF-5 is a clarified-status removal (never a real prediction) and RF-6 a closed negative
route; RF-1, RF-2, RF-3, RF-4,
RF-7 are substantive structural saves or positive empirical-coherence passes.

### E.3.3 Value-gated / coherence-class falsifiers

Falsifier-tier statements that cannot become single-detection kills until the #1 gap closes.
Each records the operational shape of an open commitment.

| # | Falsifier handle | Gated on | Operational form | Origin |
|---|---|---|---|---|
| VG-1 | `Im χ` budget (one dial, three pillars) | `Im χ` (#1 gap) | the **conjectured** KSS floor `η/s ≥ ℏ/4π` (its authors offer it as a bound that *may* hold, not as a theorem); a GW-propagation ceiling `η ≲ 10⁹–10¹⁰ Pa·s`, derived here via the standard viscous gravitational-wave damping rate `Γ ~ 16πGη/c²` from the requirement that the wave not be over-damped **across its observed propagation distance** — with the published cosmological-fluid bound of the same form (`η < 2.3 × 10⁹ Pa·s`, PRD 95, 103509 (2017), from GW150914 over 410 Mpc) sitting at the tight end of that band; macromolecule decoherence floor. Bracket position (near KSS) is the framework's commitment. Same `Im χ` governs Bell decoherence (§B.4.5 Bell-memory bridge) | §B.4.5 + §D.5.4 |
| VG-2 | Cosmological-constant residual — **magnitude only**, present-epoch `ρ_vac ≈ 3Ω_Λ,0 M̄_Pl² H_0²` | `Im χ` (Volovik equilibrium is zero; residual is the drive signature) | **The epoch-law face is already closed, not pending:** the dynamical reading `ρ_vac ∝ H(t)²` at all epochs forces `Ω_vac(z) ≡ ν` and is excluded ≈34× by the Planck 2015 XIV early-DE bound, ≈33× in equivalent `ΔN_eff`, and outright by the absence of any deceleration→acceleration transition (N54, §E.1.1). What remains gated is the residual's magnitude with no epoch law attached; a magnitude inconsistent with the driven-dissipative deviation from Volovik equilibrium falsifies the structural identification | §E.1.1 |
| VG-3 | `1/T_2` substrate-decoherence rate | `Im χ` / WP-IX4 | A measured `1/T_2` above the symmetry-protected boundary would falsify the symmetry-protection result | §D.5.5 |
| VG-4 | Dark-matter signatures | (Mostly) outside this paper's derivational scope; sterile-RH 3-prediction is structural | The 3 sterile RH neutrinos are structural; relic (sterile share) ~1.1% Ω_DM — a 94×–176× shortfall depending on which cosmological Σm_ν bound is taken, the larger figure being the ΛCDM one (active+sterile total ~2.1%/47×, or ~88× at the tighter bound); remaining ~98% out of scope — the inter-front programme's target, not a standing scope fence. Laboratory detection of heavy sterile RH at Dodelson–Widrow `keV` window would falsify the `m_sterile = m_active` sub-tenth-eV Dirac-character prediction (`≲ 0.12 eV` at the Planck + BAO bound, `≲ 0.064 eV` under ΛCDM at the current DESI bound, `≲ 0.16 eV` under w₀wₐ) | §E.1.3 |
| VG-5 | Gravitational-wave dispersion at high `E` | dim-6 dispersion correction once GW propagation scale identified | Concrete prediction once the induced-EH propagator's effective `Λ` for the GW sector is computed (Paper-2). The which-`Λ` split deliberately does **not** assign this sector — the graviton is an induced composite, so its effective scale is a property of the generating loop; §B.6.4's margin uses `Λ_L` illustratively only. **Not independent of VG-6:** per §B.6.4 the graviton's preferred-frame remnant is the same dimension-six coefficient in the tensor sector — one gated number, two sectors | §B.6.3, VG-6 |
| VG-6 | Dimension-six isotropic LV coefficient `η⁽⁴⁾` | substrate strain-mode dispersion (#1 gap; `Cl41Wave().wave_speed_c()` raises) | Published n = 4 limits: photon `\|ξ⁽⁴⁾\| ≲ 10⁻⁸`, electron `≲ 10⁻⁶`, proton `−10⁻³ … +10⁻⁶`. **At the substrate's natural coefficient `c = 1` this reads `η⁽⁴⁾ = c_lat/(2π) ∈ [1.9, 6.7]` (ruled `Λ_L = 1/a` band, §B.6.2) — excluded unconditionally by ~1.1–1.7 orders (Auger 2022 model-independent, `η⁽⁴⁾_p < 0.149`, superluminal) and by 6.3–6.8 orders only under pure-proton composition; the photon `10⁻⁸` corner is a projected bound whose triggering detection has not occurred.** Survival requires either a substrate suppression to `\|η⁽⁴⁾\| ≲ 10⁻⁶` (the defect form factor supplies only `(f_π/m)² ~ 10⁻²` — quoted at the ANW fitted `f_π`, factor-of-two immaterial here, §B.6.3 — and none for the photon), or `Λ_LV ≳ 10³ M_Pl` for the matter rows (`≳ 10⁴ M_Pl` for the photon row, which has no form factor) decoupled from the Sakharov cutoff, or a substrate symmetry forcing the isotropic quartic dispersion coefficient to vanish. Riding the OPEN import I-3 for the `Λ_L` band and the inside-frame data import I-19 (whose premise (e) hedges the outside↔inside transfer). Sibling of VG-5: same coefficient, tensor sector | §B.6.3, §D.5 |

### E.3.4 Structural-coherence falsifiers

Coherence conditions that, if they fail to close, do not constitute external single-detection
kills but break the internal construction.

| # | Coherence condition | What fails if it doesn't close | Origin |
|---|---|---|---|
| SC-1 | Multi-defect well-posedness of the wavefront field equation | The Eulerian "atlas as projection artifact" reframing (§B.8.4) breaks; the multi-defect `Cl(4,1)` wave equation with `N` back-reacting topological sources not currently constructed. *Two `N = 2` static results exist (R-135 ansatz-reduced BVP; R-144 full-3D ansatz-free minimization, §C.1.2): the static two-defect sector is variationally coherent and strictly below threshold — the dynamical multi-defect EOM stays open (the condition's core face)* | §B.8.4, §E.1.2, §C.1.2 |
| SC-2 | Cell-order requirement: emergent D4 cell pattern carries local coordination WITHOUT coherent long-range space-fixed cubic orientational order | A space-fixed cell crystal would produce hadronic-scale `(E/f_π)²` anisotropy — load-bearing OPEN for §B.6.3 closure | §B.6.3 |

### E.3.5 Internal pre-mortem — five things to be wrong about

The four preceding categories list *external* detections that would kill the current
formulation. The complement is the **internal pre-mortem**: the five biggest structural
exposures inside TWT itself, where the framework could be right about its pillars and still fail
because a load-bearing construction does not close. The first three are not falsifiers in the
E.3.1–E.3.4 sense (there is nothing to detect); they are *internal* places where the framework's own
machinery is loaded against open questions. The fourth and fifth are different in kind and are
stated last: there the measurements already exist and it is the framework that owes numbers.

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
predicted (§B.6, §B.7), but the GW170817 multimessenger constraint `|c_GW − c_γ|/c ≲ 10⁻¹⁵` is
already tight. A robust sector-dependent or time-varying difference between the observed `c` and the lock rate
falsifies **this candidate's identification of the two**; the induced-gravity story rides on the
average identity, so such a detection would break this candidate's unified-frame picture rather
than just trim a coefficient. The axioms themselves state no rate and no uniformity, so the
failing object is the `A-3`-downstream identification chain, not `A-3`: on a positive detection
it is `c`, the emergent observer-side speed, that carries the non-uniform label, the axioms
stand, and the family reformulates at the instance layer — the sharpest instance-level exposure
in this list, distinct in kind from the foliation axiom's family-level kill condition.

**(4) Lorentz violation at dimension six — the pillars are protected, the residual is not.**
Dimension-four LV is closed structurally (one field, one light-cone — the canted vacuum's
universal `O(q²)` stiffness splitting is absorbed by the I-22 rescaling class, conditional on
premise P-gs), and dimension-six anisotropy is closed by D4 *on the
point-group-symmetric state* (P-gs — the spiral's space-fixed/sidereal residual is SC-2's
question) *and at the full point group* (P-op — under the driven subgroup an anisotropic spatial
quartic is permitted, and is absent by the bond set's computed zero spatial fourth moment rather
than by symmetry; §B.1.5). What is not closed is the rotationally invariant dimension-six term, whose coefficient
the framework cannot yet compute and whose *naive* value at `c = 1` is excluded unconditionally by about one order of magnitude (a single model-independent cosmic-ray analysis, superluminal branch), and by six to seven orders only under a mass-composition assumption the same observatory's data disfavours. This
is a measured exposure, not merely a pending detection: **a number is already measured, and the framework owes a coefficient that fits under it — under the unconditional bound today, and under the conditional corner if composition resolves against the family.** If the substrate
dynamics deliver `η⁽⁴⁾ ~ O(1)`, the current formulation is dead — not evolved. And "the current
formulation" is exact rather than a hedge: what dies is **this candidate instance**, killed at
three pinned choices in series — a regular arrangement, its back-fit size, and one induced-gravity
chain to denominate it (§B.6.3, §A.6.4). The family would survive holding the *problem*, not an
answer to it, and a member proposed at the irregular-discrete branch inherits a different
constraint rather than a lighter one (companion Section 13, row I-26).

**(5) The electroweak crossing scale — the second already-measured exposure; §C.4.5's own text
calls it the twin of (4).** `sin²θ_W = 3/8` is a normalization identity
at the `g_1 = g_2` crossing; the framework does not derive the crossing scale, and its own
lattice-scale reading lands `0.154–0.158` against the measured `0.2312` — a 33% miss of a
five-digit number, with the four standard escape routes computed and closed (N55, §C.4.5) —
descent and closures alike riding the imported elementary-field RGE premise (`I-6`) for a sector
this candidate holds emergent / composite, whose failure gates the reading rather than refuting
it. Its
level is the same as (4)'s: the `3/8` identity is family property in §A.6.3's conditional sense —
riding the weak assignment of §C.4.2 and its two named supports, not an axiom — while the
*placement* of the crossing is
instance-level, and what the miss indicts is this candidate's arrangement and calibrations. Neither
exposure is inherited by a family member that has not made those picks — and neither is answered
by one either.

---

## §E.4 — What TWT contributes; landscape; Paper 2 agenda

The framework's content distilled to its synthesized headlines, situated in the intellectual
landscape, and pointed forward to Paper 2.

### E.4.1 Seven synthesized headlines

The framework's primary contribution is **geometric reinterpretation**: turning an SM postulate
or unexplained feature into a structural consequence of the substrate, with the numerical value
typically unchanged. Seven representative items:

- **Three generations are a dimension count**, not a free count.
  Four-dimensional space carries exactly three anti-self-dual planes (`dim Λ²₋(ℝ⁴) = 3`,
  computed in-engine), identified with the three imaginary units of `ℍ` on the `V_4⊥`
  generation circle. Frobenius enters as a structural remark through a named associativity
  premise — not as the operative exclusion. Generic-given-4D, conditional on the ℍ-unit
  identification (§C.3.8).

- **`sin²θ_W = 3/8` at unification is native, not GUT.** The load-bearing substrate ingredients
  are (i) the D4 trivector charges that determine `Σ T_3² = 2`, `Σ Q² = 16/3`, and (ii) the
  Clifford trace bridge giving native `√(3/5)`. The cross-term `Σ T_3 · Y = 0` enters too, but as
  a *generic* SU(2)×U(1) doublet-Schur-lemma fact (§C.4.5(ii) honest scope) — its TWT-specific
  expression as grade-0 L⊥Q orthogonality is Cl-native phrasing, not new content. With those
  ingredients in hand, `g_1 = g_2` is enforced by D4 isotropy — specifically the bond set's
  *second*-moment isotropy, the dimension-four statement, which is a different fact from the
  degree-four invariant-space argument that pushes anisotropy to dimension eight (§B.1.5) — and
  `sin²θ_W = 3/8` follows. SU(5) is removed throughout; the
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

- **β-decay shares the substrate parameter `D` with the flavour sector.** The same `D` that
  produces the Cabibbo angle, the generation phase, and the Skyrme stabilizer also supplies the
  β-decay channel. The 4 no-shared-index `e_4`-bonds are where a topological boundary term would
  have to live, but the substrate origin of parity violation is **not** built: no orientation-odd
  invariant exists at bilinear order in the bond data, and the candidate seat of §D.4.4 is cubic
  with an open coefficient (§C.5.3). The electron in β⁻ is *created* as an L-winding excitation,
  not drawn from a pool; the mediator is the same `I_4` Hodge map. **One number, multiple
  manifestations** (§C.5.3, §C.5.7).

- **The Lorentzian signature of observed spacetime is the algebraic shadow of a
  wavefront-locked observer in a Euclidean substrate.** The induced spatial frame
  `γ⁰ = e_4, γʲ = e_4 e_j` on `Cl(4,0)` satisfies the Dirac relations with signature `(+, −, −, −)`.
  **Read this as posit plus derived implication, not as a derivation of the signature** (§B.1): the
  timelike placement `e_5² = −1` is an INPUT — every theory locates its signature somewhere — while
  what is DERIVED-A is that `Cl(4,0) ≅ Cl(1,3)` as real algebras, so once the posit is made the
  observer's signature is *forced* rather than separately chosen. The result carried end to end
  from the substrate is charge quantization — the discreteness and the neutrality identity, not the
  assignment of values across the spectrum (§C.2.8).

- **Matter is a defect.** The single load-bearing ontological commitment from which the
  framework's "primary contribution" character follows. Defects are configurations of one
  substrate rotor field; stability is topological, mass is meta-time rotor frequency, and Lorentz
  invariance is *protected* against the radiative species-splitting that plagues generic
  emergent-LI programs — one fundamental field, not `N` independent ones. The protection is
  **dimension-four**; the lattice point group independently pushes rotational anisotropy of the
  polarization-averaged dispersion to dimension eight (on §B.1.5's five premises — the
  scalar-kernel and operative-symmetry ones included); and the
  rotationally invariant dimension-six residual escapes both and is the framework's named open
  exposure (§B.1.5, §E.3.5(4)).

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
- **Koide** and the empirical lepton mass relation — and, separately, the
  cyclic-permutation-invariant (`Z_3` circulant) parametrization of it, whose priority is
  Koide's own (*Quark and Lepton Mass Matrices with a Cyclic Permutation Invariant Form*,
  arXiv:hep-ph/0005137, 2000).
- **Brannen** for the independent 2006 re-noticing of that form's charged-lepton case, which
  pinned the modulation amplitude at `√2` (η² = 1/2) and fitted the lepton phase numerically;
  it reached the refereed literature through Koide's own 2007 paper. The corpus's "Brannen
  amplitude" and "Brannen phase" are internal labels for the objects that re-noticing pinned,
  not a priority claim on the parametrization (§C.3.1).
- **Skyrme** and topological solitons as particles.
- The geometric-algebra school, the lattice spin-system tradition, the Dzyaloshinskii–Moriya
  literature in condensed matter, and Sakharov's induced-gravity program.

**Adjacent programmes (prior art, primary-verified; full records in companion
Section 10).** Several independent programmes reach related conclusions by different means, and
this work was developed independently of all of them: **Trayling & Baylis** (the `Cl(7)`
gauge-group construction — Trayling's 1999 preprint already claims `g′/g = √(3/5)` "without
invoking master groups"; the specific delta is stated at §C.4.5); **Lasenby–Doran–Gull** Gauge
Theory Gravity (tree-level gauge gravity over a flat Lorentzian background, where TWT's tree
routes are closed within the banked action class (R-164), forcing the induced route); the **Plebanski–Urbantke–Krasnov**
self-dual family (family-level kin of the SD/ASD organizing principle — the Urbantke metric is
cubic where TWT's texture bilinear is not, so its signature/reality theorems do not transfer;
companion Section 10 scope note); **Furey's** division-algebraic programme (representation content from the non-associative
factor — one generation in Furey & Hughes 2022, three-generation structure in Furey 2018; the
foil that forces §C.3.8's named associativity premise); **Chisholm–Farwell** spin-gauge unification; and **Boyle–Farnsworth's**
spectral constructions.

The revision history and the *Paper 2 agenda* are administrative and forward-looking
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
and is not a dial. One binary INPUT bit fixes the memory branch as **hysteretic** — a genuine
menu-and-pick, of the kind §C.4.2 turns out *not* to be: here the menu {hysteretic, fading} is
offered and nothing closes it, so the candidate picks
hysteretic, consistent with the working branch §D.5.3 already adopts on defect-persistence
motivation (a pick, not a derivation; the hysteresis and driven-response modeling ride
registered imports — companion Section 13, I-14/I-15). A minimal member is **two dials + one
bit**. These are
counted within the candidate's own ledger: they would join the framework's parameter ledger
(§E.2.1) only if the candidate is adopted; until then the #1 gap remains open exactly as §D.5
states it.

**Constraint provenance (R-156).** Every member passes the
constraints-by-construction subset of both
oracles — the substrate-testbench's gate bench and the corpus engine's acceptance
inventory — *by construction*. The engine's three channel *targets* — the
`(19/2)√38 ≈ 58.6` stiffness renormalization, the `Λ ~ H²` coefficient `≈ 2.05`, and the `≤ 4`
spin-2 `C_T` moments — are **not** fitted: their kernel→observable maps are themselves #1-gap
objects, so the candidate supplies their form-side inputs while the numbers stay gated. The
over-determination that would pin a single candidate therefore activates only once one of those
maps is built — the Class-2b promise, honestly conditional.

**Scope of "passes".** The four constraints-by-construction rows (C1
causality/KK, C2 memory, C3 `s ≥ 3`, C4 passivity) are satisfied exactly; C5 (near-KSS) is
compatibility-not-confirmation with `η/s` gated; and the C6 channel targets are **not
evaluated** — their forward maps are #1-gap objects. On the acceptance inventory's own full
pass criterion (C1–C5 hard + C6 within tolerance + C7 branch declared + C8 avoided), the
candidate is therefore *label-level covered*, not passed — which is what "by construction"
can honestly mean here.

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

This is what the framework can honestly offer toward the #1 gap: a named candidate class
with counted economy and pre-registered falsifiers, where §D.5 otherwise names only a hole. Its
value magnitudes remain gated; its selection remains a Paper-2 task.

---

## §E.6 — Closing

The framework's claim is **measured**. One continuous medium with a discrete D4 substrate and a
propagating wave reproduces the structural skeleton of known physics from fewer independent
inputs than the Standard Model requires, and the reduction is genuine rather than cosmetic. The
ontology (matter = defect; spatial winding and meta-time rotor as two faces of one
circular object linked by `I_4` Hodge duality) does the work a heavier modeling apparatus would
otherwise have to do — and does it more cleanly.

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

**`TWT_foundational_paper_companion.md`** — distributed with this paper and at
https://github.com/yaerhf/TWT

The companion file contains thirteen sections:

1. **Result Index** — every R-NNN result with tier, engine primitive, target section, dependencies.
2. **Dependency Graph** — layered picture of axioms → algebraic → dynamical → deep gates.
3. **Engine ↔ Paper Map** — `twt.py` primitive ↔ paper section cross-reference.
4. **Pending-Values Registry** — open items by kernel object.
5. **Geometric reinterpretation catalog** — the nine items (Tsirelson, Weinberg 3/8, Bohr, GA Maxwell, α, Frobenius, parity-D-decay, electron smallness, Lorentzian signature).
6. **Methodology principles** — the eight principles, with canon-successor mapping.
7. **Development log** — the project's revision history and the review-round catches.
8. **Stable-spectrum enumeration** — the over-production `(B, L)` table.
9. **Wave-phase stability ladder** — 20 states across 31+ orders of magnitude in `N = m/Γ` (CANDIDATE); π⁰/π± discriminator.
10. **Bibliography** — consolidated citations.
11. **Paper 2 agenda** — the forward research program.
12. **Closability classification** — every open item classified by what actually blocks it, with the realistic closure route.
13. **Import Registry** — every load-bearing external theorem: premises, level applied, ontology status, retirement handle, revert clause.

The companion file additionally opens with a **diff-of-intent** memo. Load it
alongside this paper for the full picture.

---

# Closing note

All annexes and back-of-book bookkeeping live in the companion file
`TWT_foundational_paper_companion.md`; the engine suite (`twt_test.py`) is the executable
cross-check, with the current check count and per-result engine cites tracked in the companion.
